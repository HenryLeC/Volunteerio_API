from itsdangerous import (TimedJSONWebSignatureSerializer,
                          SignatureExpired, BadSignature)
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
