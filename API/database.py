from API import db, app
from werkzeug.security import generate_password_hash as hash, check_password_hash
from flask import jsonify
import pickle

# User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    HoursId = db.Column(db.Integer)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), unique=True, nullable=False)
    name = db.Column(db.String(), nullable = False)
    is_admin = db.Column(db.Boolean)
    is_comunity = db.Column(db.Boolean)
    is_student = db.Column(db.Boolean)
    hours = db.Column(db.Integer, nullable=True)
    unconfHours = db.Column(db.String())
    confHours = db.Column(db.String())
    pub_ID = db.Column(db.String(), nullable = False, unique=True)
    PastOpps = db.Column(db.String())
    BookedOpps = db.Column(db.String())
    Opportunities = db.relationship('Opportunity', backref='Sponsor', lazy=True)


    def __init__(self, username, password, name, ID, admin = False, community = False, student = False):
        # If no role set default to student
        if admin == False and community == False and student == False:
            student = True
        self.username = username
        self.password = hash(password)
        self.name = name
        self.is_admin = admin
        self.is_comunity = community
        self.is_student = student
        self.hours = 0
        self.unconfHours = pickle.dumps([{
            'id' : 0,
            'hours' : 0,
            'reason' : "Initialization"
        }])
        self.confHours = pickle.dumps([{
            'id' : 0,
            'hours' : 0,
            'reason' : "Initialization"
        }])
        self.pub_ID = ID
        self.PastOpps = pickle.dumps([{
            'id' : 0,
            'hours' : 0,
            'reason' : "Initialization"
        }])
        self.BookedOpps = pickle.dumps([{
            'id' : 0,
            'hours' : 0,
            'reason' : "Initialization"
        }])
        self.HoursId = 1

class Opportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Time = db.Column(db.DateTime())
    Location = db.Column(db.String())
    Hours = db.Column(db.Integer)
    Name = db.Column(db.String())
    SponsorId = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(Name, Location, Time, Hours):
        self.Name = Name
        self.Time = Time
        self.Location = Location
        self.Hours = Hours
