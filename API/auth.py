from itsdangerous import (TimedJSONWebSignatureSerializer,
                          SignatureExpired, BadSignature,
                          URLSafeTimedSerializer)
from API.database import User
from API import app
from functools import wraps
from flask import request, jsonify


# Generate Auth Token Func
def generate_auth_token(u_id):
    s = TimedJSONWebSignatureSerializer(
        app.config['SECRET_KEY'],
        expires_in=3600
    )
    return s.dumps({'id': u_id})


# Check Auth Token Func
def verify_auth_token(token):
    s = TimedJSONWebSignatureSerializer(
        app.config['SECRET_KEY']
    )
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None  # valid token, but expired
    except BadSignature:
        return None  # invalid token
    user = User.query.filter_by(id=data['id']).first()
    return user


# Decorator to check if thre is a valid token in a request
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.form:
            token = request.form['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        current_user = verify_auth_token(token)
        if not current_user:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


# Email Tokens
def generate_confirmation_token(data):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(data, salt=app.config['SECURITY_PASSWORD_SALT'])


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        id = serializer.loads(
            token,
            salt=app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except Exception:
        return False
    return id
