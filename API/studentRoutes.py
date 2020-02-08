from flask import Flask, request, jsonify
from API import app
from API.database import User
from API.auth import verify_auth_token, generate_auth_token, token_required
from werkzeug.security import generate_password_hash as hash, check_password_hash

@app.route("/hours", methods=["POST"])
@token_required
def getHours(user):
    return jsonify(user)

@app.route('/login', methods=["POST"])
def login():
    try:
        uname = request.form["username"]
        passw = request.form["password"]
    except:
        return jsonify({'msg' : 'Login information required'}), 401

    user = User.query.filter_by(username=uname).first()
    if check_password_hash(user.password, passw):
        return jsonify({'key' : generate_auth_token(user.id).decode("utf-8")})
    else:
        return jsonify({'msg' : 'Invalid Login information'})