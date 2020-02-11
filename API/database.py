from API import db, app
from werkzeug.security import generate_password_hash as hash, check_password_hash

# User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), unique=True, nullable=False)
    name = db.Column(db.String(), nullable = False)
    is_admin = db.Column(db.Boolean)
    is_comunity = db.Column(db.Boolean)
    is_student = db.Column(db.Boolean)
    hours = db.Column(db.Integer, nullable=True)
    unconfHours = db.Column(db.PickleType)
    confHours = db.Column(db.PickleType)
    pub_ID = db.Column(db.String(), nullable = False, unique=True)
    PastOpps = db.Column(db.PickleType)
    BookedOpps = db.Column(db.PickleType)

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
        self.hours = None
        self.unconfHours = []
        self.confHours = []
        self.pub_ID = ID
        self.PastOpps = []
        self.BookedOpps = []
