from API import db
from werkzeug.security import generate_password_hash as hash
from flask_login import UserMixin
import pickle
import datetime


# User table
class User(db.Model, UserMixin):
    # All
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), unique=True, nullable=False)
    name = db.Column(db.String(), nullable=False)
    pub_ID = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=True)
    emailConfirmed = db.Column(db.Boolean, nullable=False)
    firstTime = db.Column(db.Boolean, nullable=False)

    District_Id = db.Column(db.Integer, db.ForeignKey('district.id'))
    District = db.relationship('District', backref="Members", lazy=True)
    School_Id = db.Column(db.Integer, db.ForeignKey('school.id'))
    School = db.relationship('School', backref="Members", lazy=True)

    # Student
    HoursId = db.Column(db.Integer)
    is_student = db.Column(db.Boolean)
    hours = db.Column(db.Integer, nullable=True)
    unconfHours = db.Column(db.LargeBinary())
    confHours = db.Column(db.LargeBinary())
    CurrentOpps = db.Column(db.LargeBinary())
    UnconfHoursMessages = db.relationship("NewUnconfHoursMessages",
                                          backref="Student", lazy=True,
                                          cascade="delete, delete-orphan")
    InCompleteOppMessages = db.relationship("InCompleteOppMessages",
                                            backref="Student", lazy=True,
                                            cascade="delete, delete-orphan")

    PastOpps = db.relationship('Opportunity', secondary="past")
    BookedOpps = db.relationship('Opportunity', secondary="booked")

    # Admin
    is_admin = db.Column(db.Boolean)

    # Teacher
    is_teacher = db.Column(db.Boolean)

    # Community
    is_community = db.Column(db.Boolean)

    # Admin / Community
    Opportunities = db.relationship('Opportunity', backref="Sponsor",
                                    lazy=True)

    # WebBackend
    is_webmaster = db.Column(db.Boolean)

    def __init__(self, username, password, name, ID, district, school,
                 email=None, admin=False, community=False, student=False,
                 teacher=False, webmaster=False):
        # If no role set default to student
        if not admin and not community and not student and not teacher and not webmaster:
            student = True
        self.username = username
        self.password = hash(password)
        self.name = name
        self.is_admin = admin
        self.is_community = community
        self.is_student = student
        self.is_teacher = teacher
        self.hours = 0
        self.unconfHours = pickle.dumps([])
        self.confHours = pickle.dumps([])
        self.CurrentOpps = pickle.dumps([])
        self.pub_ID = ID
        self.HoursId = 1
        self.District = district
        self.School = school
        self.is_webmaster = webmaster
        self.email = email
        self.firstTime = True
        self.emailConfirmed = False


class Opportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Time = db.Column(db.DateTime())
    Location = db.Column(db.String())
    Hours = db.Column(db.Integer)
    Name = db.Column(db.String())
    Class = db.Column(db.String())
    MaxVols = db.Column(db.Integer)
    Confirmed = db.Column(db.Boolean)
    Description = db.Column(db.String(500))

    SponsorID = db.Column(db.Integer, db.ForeignKey('user.id'))

    BookedStudents = db.relationship("User", secondary="booked")
    PastStudents = db.relationship("User", secondary="past")

    InCompleteOppMessages = db.relationship("InCompleteOppMessages",
                                            backref="Opportunity", lazy=True,
                                            cascade="delete, delete-orphan")

    def __init__(self, Name, Location, Time, Hours, Class, MaxVols,
                 Sponsor, Description, Confirmed):
        self.Name = Name
        self.Time = Time
        self.Location = Location
        self.Hours = Hours
        self.SponsorID = Sponsor.id
        self.Class = Class
        self.MaxVols = MaxVols
        self.Confirmed = Confirmed
        self.Description = Description

    def getTime(self):
        return self.Time.strftime("%a %b %d, %I:%M %p")


class NewUnconfHoursMessages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    StudentId = db.Column(db.Integer, db.ForeignKey("user.id"))


class InCompleteOppMessages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    StudentId = db.Column(db.Integer, db.ForeignKey("user.id"))
    HoursCompleted = db.Column(db.Integer)
    MinutesCompleted = db.Column(db.Integer)
    OpportunityId = db.Column(db.Integer, db.ForeignKey("opportunity.id"))

    def __init__(self, HoursCompleted, MinutesCompleted):
        self.HoursCompleted = HoursCompleted
        self.MinutesCompleted = MinutesCompleted


class District(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    hoursGoal = db.Column(db.Integer, nullable=True)
    schools = db.relationship("School", back_populates="district")

    def __init__(self, Name, hoursGoal=None):
        self.name = Name
        self.hoursGoal = hoursGoal


class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    hoursGoal = db.Column(db.Integer, nullable=True)
    district_id = db.Column(db.Integer, db.ForeignKey("district.id"))
    district = db.relationship("District", back_populates="schools")

    def __init__(self, Name, hoursGoal=None):
        self.name = Name
        self.hoursGoal = hoursGoal


class Booked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Opp_id = db.Column(db.Integer, db.ForeignKey('opportunity.id'))

    user = db.relationship(User, backref=db.backref("Booked"))
    opp = db.relationship(Opportunity, backref=db.backref("Booked"))


class Past(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Opp_id = db.Column(db.Integer, db.ForeignKey('opportunity.id'))

    user = db.relationship(User, backref=db.backref("Past"))
    opp = db.relationship(Opportunity, backref=db.backref("Past"))


class Logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exc = db.Column(db.String())
    time = db.Column(db.DateTime())

    def __init__(self, exc: str):
        self.exc = exc
        self.time = datetime.datetime.now()
