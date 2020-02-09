from flask import Flask, request, jsonify
from API import app, db
from API.database import User
from API.auth import verify_auth_token, generate_auth_token, token_required
from werkzeug.security import generate_password_hash as hash, check_password_hash

@app.route("/hours", methods=["POST"])
@token_required
def getHours(user):
    return jsonify({'hours' : user.hours})

@app.route('/login', methods=["POST"])
def login():
    # Check for Username and Password
    try:
        uname = request.form["username"]
        passw = request.form["password"]
    except:
        return jsonify({'msg' : 'Login information required'}), 401

    # Find user by Uname and check hashed password
    user = User.query.filter_by(username=uname).first()
    if check_password_hash(user.password, passw):
        # Make role
        role = ''
        if user.is_student == True:
            role = 'student'
        elif user.is_admin == True:
            role = 'admin'
        else:
            role = 'community'
        
        #return auth token and role
        return jsonify({
            'key' : generate_auth_token(user.id).decode("utf-8"),
            'role' : role
        })
    else:
        return jsonify({'msg' : 'Invalid Login information'})

@app.route('/addhours', methods=["POST"])
@token_required
def add_hours(user):
    # Check for hours and reason in request
    try:
        hours = request.form["hours"]
        reason = request.form["reason"]
    except:
        return jsonify({'msg' : 'Hours and reason is required.'})
    # Add hous and reason to unconfirmed list
    user.unconfHours.append({
        'id' : len(user.unconfHours) + 1,
        'hours' : int(hours),
        'reason' : reason
    })
    db.session.commit()

    return jsonify({'msg' : 'Hours added'})
    