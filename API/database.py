from API import db, app
from werkzeug.security import generate_password_hash as hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean)
    is_comunity = db.Column(db.Boolean)
    is_student = db.Column(db.Boolean)

    def __init__(self, username, password, admin = False, community = False, student = False):
        if admin == False & community == False & student == False:
            student = True
        self.username = username
        self.password = hash(password)
        self.is_admin = admin
        self.is_comunity = community
        self.is_student = student
