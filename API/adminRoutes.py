from flask import Flask, request, jsonify
from API import app, db
from API.database import User
from API.auth import verify_auth_token, generate_auth_token, token_required
from werkzeug.security import generate_password_hash as hash, check_password_hash
from json import loads
import pickle

@app.route('/confirmHours', methods=["POST"])
@token_required
def confirmHours(user):
    # Move an Unconfiremd Hours to Confirmed

    if user.is_admin != True:
        return jsonify({
            'msg': 'Must be Administrator to preform this task'
        })
    try:
        Id = request.form['HoursId']
        StuId = request.form['StudentId']
    except:
        return jsonify({
            'msg': "Please provide an 'HoursId' and 'StudentId'"
        })
    
    # Find The Student
    Student = User.query.filter_by(pub_ID = StuId).first()
    
    # Preform the move
    for Hours in pickle.loads(Student.unconfHours):
        if Hours['id'] == int(Id):
            ConfHrs = pickle.loads(Student.confHours)
            UnconfHrs = pickle.loads(Student.unconfHours)
            ConfHrs.append(Hours)
            UnconfHrs.remove(Hours)
            Student.hours += Hours['hours']
            Student.confHours = pickle.dumps(ConfHrs)
            Student.unconfHours = pickle.dumps(UnconfHrs)

            db.session.add(Student)
            db.session.commit()
    return jsonify({
        'msg' : 'Hours Confirmed',
        'unconfHours' : pickle.loads(Student.unconfHours),
        'confHours' : pickle.loads(Student.confHours)
    })

@app.route('/deleteHours', methods=["POST"])
@token_required
def deleteHours(user):
    if user.is_admin != True:
        return jsonify({
            'msg': 'Must be Administrator to preform this task'
        })
    try:
        Id = request.form['HoursId']
        StuId = request.form['StudentId']
    except:
        return jsonify({
            'msg': "Please provide an 'HoursId' and 'StudentId'"
        })
    
    # Find The Student
    Student = User.query.filter_by(pub_ID = StuId).first()
    
    # Preform the move
    for Hours in pickle.loads(Student.unconfHours):
        if Hours['id'] == int(Id):
            UnconfHrs = pickle.loads(Student.unconfHours)
            UnconfHrs.remove(Hours)
            Student.unconfHours = pickle.dumps(UnconfHrs)

            db.session.add(Student)
            db.session.commit()

    return jsonify({
        'msg' : 'Hours Removed',
        'unconfHours' : pickle.loads(Student.unconfHours),
        'confHours' : pickle.loads(Student.confHours)
    })