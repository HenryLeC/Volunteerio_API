from API import db, api
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, BadSignature

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
        self.password = password
        self.is_admin = admin
        self.is_comunity = community
        self.is_student = student

    def generate_auth_token(self, u_id, expiration=3600):
        s = TimedJSONWebSignatureSerializer(
               api.config['SECRET_KEY'],
               expires_in=expiration
               )
        return s.dumps({'id': u_id})

    @staticmethod
    def verify_auth_token(self, token):
        s = TimedJSONWebSignatureSerializer(
               api.config['SECRET_KEY']
               )
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.filter_by(id=data['id']).first()
        return user

    
