import datetime
import pickle
import random
import string

from flask_login import UserMixin
from werkzeug.security import generate_password_hash as hash

from API import db


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

    School_Id = db.Column(db.Integer, db.ForeignKey('school.id'))
    School = db.relationship('School', back_populates="users")

    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))
    group = db.relationship('Groups', back_populates="users")

    # Student
    HoursId = db.Column(db.Integer)
    is_student = db.Column(db.Boolean)
    hours = db.Column(db.Integer, nullable=True)
    unconfHours = db.Column(db.LargeBinary())
    confHours = db.Column(db.LargeBinary())
    CurrentOpps = db.Column(db.LargeBinary())
    UserGoal = db.Column(db.Integer, nullable=True)
    UnConfHoursMessages = db.relationship(
        "NewUnconfHoursMessages", back_populates="student",
        cascade="delete, delete-orphan")
    # UnconfHoursMessages = db.relationship("NewUnconfHoursMessages",
    #                                       backref="Student", lazy=True,
    #                                       cascade="delete, delete-orphan")
    InCompleteOppMessages = db.relationship(
        "InCompleteOppMessages", back_populates="student",
        cascade="delete, delete-orphan")
    # InCompleteOppMessages = db.relationship("InCompleteOppMessages",
    #                                         backref="Student", lazy=True,
    #                                         cascade="delete, delete-orphan")

    PastOpps = db.relationship(
        'Opportunity', secondary="past", back_populates="PastStudents")
    BookedOpps = db.relationship(
        'Opportunity', secondary="booked", back_populates="BookedStudents")

    # Admin
    is_admin = db.Column(db.Boolean)

    # Teacher
    is_teacher = db.Column(db.Boolean)

    # Community
    is_community = db.Column(db.Boolean)

    # Admin / Community
    Opportunities = db.relationship('Opportunity', back_populates="sponsor")
    # Opportunities = db.relationship('Opportunity', backref="Sponsor",
    #                                 lazy=True)

    # WebBackend
    is_webmaster = db.Column(db.Boolean)

    def __init__(self, username, password, name, ID, school,
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
        self.School = school
        self.is_webmaster = webmaster
        self.email = email
        self.firstTime = True
        self.emailConfirmed = False
        self.UserGoal = None

    def getGoal(self) -> int:
        userGoal = self.UserGoal
        group = self.group
        schoolGoal = self.School.hoursGoal

        if userGoal is not None:
            return userGoal
        elif group is not None:
            return group.hoursGoal
        elif schoolGoal is not None:
            return schoolGoal
        else:
            return 0


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

    Virtual = db.Column(db.Boolean)
    ClockCode = db.Column(db.String(6), unique=True)

    sponsor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sponsor = db.relationship("User", back_populates="Opportunities")

    # SponsorID = db.Column(db.Integer, db.ForeignKey('user.id'))

    BookedStudents = db.relationship(
        "User", secondary="booked", back_populates="BookedOpps")
    PastStudents = db.relationship(
        "User", secondary="past", back_populates="PastOpps")

    InCompleteOppMessages = db.relationship(
        "InCompleteOppMessages", back_populates="opportunity")
    # InCompleteOppMessages = db.relationship("InCompleteOppMessages",
    #                                         backref="Opportunity", lazy=True,
    #                                         cascade="delete, delete-orphan")

    def __init__(self, Name, Location, Time, Hours, Class, MaxVols,
                 Sponsor, Description, Confirmed, Virtual=False):
        self.Name = Name
        self.Time = Time
        self.Location = Location
        self.Hours = Hours
        self.sponsor_id = Sponsor.id
        self.Class = Class
        self.MaxVols = MaxVols
        self.Confirmed = Confirmed
        self.Description = Description
        self.Virtual = Virtual
        self.ClockCode = ''.join(random.choices(
            string.ascii_letters + string.digits, k=6))

    def getTime(self):
        return self.Time.strftime("%a %b %d, %I:%M %p")


class NewUnconfHoursMessages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    student = db.relationship("User", back_populates="UnConfHoursMessages")


class InCompleteOppMessages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    student = db.relationship("User", back_populates="InCompleteOppMessages")

    HoursCompleted = db.Column(db.Integer)
    MinutesCompleted = db.Column(db.Integer)

    opportunity_id = db.Column(db.Integer, db.ForeignKey("opportunity.id"))
    opportunity = db.relationship(
        "Opportunity", back_populates="InCompleteOppMessages")

    def __init__(self, HoursCompleted, MinutesCompleted):
        self.HoursCompleted = HoursCompleted
        self.MinutesCompleted = MinutesCompleted


class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    hoursGoal = db.Column(db.Integer, nullable=True)
    users = db.relationship("User", back_populates="School")
    groups = db.relationship("Groups", back_populates="school")

    def __init__(self, Name, hoursGoal=None):
        self.name = Name
        self.hoursGoal = hoursGoal


class Booked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    opp_id = db.Column(db.Integer, db.ForeignKey('opportunity.id'))


class Past(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    opp_id = db.Column(db.Integer, db.ForeignKey('opportunity.id'))

    # Needed to access hours prop
    user = db.relationship(User, backref=db.backref("Past"))

    hours = db.Column(db.Integer, nullable=True)


class Logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exc = db.Column(db.String())
    time = db.Column(db.DateTime())

    def __init__(self, exc: str):
        self.exc = exc
        self.time = datetime.datetime.now()


class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))
    school = db.relationship('School', back_populates="groups")

    users = db.relationship("User", back_populates="group")

    hoursGoal = db.Column(db.Integer)
    name = db.Column(db.String(100))

    def __init__(self, name, hoursGoal):
        self.name = name
        self.hoursGoal = hoursGoal
