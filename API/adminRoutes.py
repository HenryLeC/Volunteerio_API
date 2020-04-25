from flask import request, jsonify
from sqlalchemy import or_, and_
from API import app, db
from API.database import User, NewUnconfHoursMessages
from API.auth import token_required
import pickle


@app.route('/confirmHours', methods=["POST"])
@token_required
def confirmHours(user):
    # Move an Unconfiremd Hours to Confirmed

    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task'
        })
    try:
        StuHrData = request.form['StuHrData']
    except KeyError:
        return jsonify({
            'msg': "Please provide an 'HoursId' and 'StudentId'"
        })
    StuHrDataList = StuHrData.split(", ")
    Id = StuHrDataList[0]
    HrId = StuHrDataList[1]

    # Find The Student
    Student = User.query.get(Id)

    # Preform the move
    for Hours in pickle.loads(Student.unconfHours):
        if Hours['id'] == int(HrId):
            ConfHrs = pickle.loads(Student.confHours)
            UnconfHrs = pickle.loads(Student.unconfHours)
            ConfHrs.append(Hours)
            UnconfHrs.remove(Hours)
            if len(UnconfHrs) == 0:
                Student.UnconfHoursMessages = []
            Student.hours += Hours['hours']
            Student.confHours = pickle.dumps(ConfHrs)
            Student.unconfHours = pickle.dumps(UnconfHrs)

            db.session.add(Student)
            db.session.commit()
    return jsonify({
        'msg': 'Hours Confirmed',
        'unconfHours': pickle.loads(Student.unconfHours),
        'confHours': pickle.loads(Student.confHours)
    })


@app.route('/deleteHours', methods=["POST"])
@token_required
def deleteHours(user):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task'
        })
    try:
        StuHrData = request.form['StuHrData']
        StuHrDataList = StuHrData.split(", ")
        Id = StuHrDataList[0]
        HrId = StuHrDataList[1]
    except KeyError:
        return jsonify({
            'msg': "Please provide an 'HoursId' and 'StudentId'"
        })

    # Find The Student
    Student = User.query.get(Id)

    # Preform the move
    for Hours in pickle.loads(Student.unconfHours):
        if Hours['id'] == int(HrId):
            UnconfHrs = pickle.loads(Student.unconfHours)
            UnconfHrs.remove(Hours)
            if len(UnconfHrs) == 0:
                Student.UnconfHoursMessages = []
            Student.unconfHours = pickle.dumps(UnconfHrs)

            db.session.add(Student)
            db.session.commit()

    return jsonify({
        'msg': 'Hours Removed',
        'unconfHours': pickle.loads(Student.unconfHours),
        'confHours': pickle.loads(Student.confHours)
    })


@app.route('/StudentsList', methods=["POST"])
@token_required
def StudentsList(user):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        })
    try:
        Filter = "%{}%".format(request.form["Filter"])
    except KeyError:
        return jsonify({
            'msg': ""
        })
    ReturnList = []
    # Filter for students that Have a name or ID like like the Filter.
    Students = User.query.filter(and_(
        User.is_student,
        User.District == user.District,
        or_(
            User.name.like(Filter),
            User.pub_ID.like(Filter),
        )
    )).limit(5)
    for student in Students:
        ReturnList.append({
            "Name": student.name,
            "StuId": student.pub_ID,
            "Hours": str(student.hours),
            "ID": student.id
        })
    return jsonify(ReturnList)


@app.route('/StudentHours', methods=["POST"])
@token_required
def StudentHours(user):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        })
    try:
        StudentId = request.form["id"]
    except KeyError:
        return jsonify({
            'msg': "Please Supply a Student Id"
        })

    student = User.query.get(int(StudentId))

    PastOpps = student.PastOpps
    PastOppsClean = []
    for opp in PastOpps:
        PastOppsClean.append({
            "Name": opp.Name,
            "Hours": opp.Hours,
            "Time": opp.Time.strftime("%m/%d/%Y, %H:%M")
        })
    confHours = pickle.loads(student.confHours)
    ConfHoursClean = []
    for opp in confHours:
        ConfHoursClean.append({
            "Hours": opp["hours"],
            "Reason": opp["reason"],
            "Confirmed": "Confirmed"
        })
    unconfHours = pickle.loads(student.unconfHours)
    UnConfHoursClean = []
    for opp in unconfHours:
        UnConfHoursClean.append({
            "StuHrData": "{}, {}".format(student.id, opp["id"]),
            "Hours": opp["hours"],
            "Reason": opp["reason"],
            "Confirmed": "Unconfirmed"
        })

    FullClean = {
        "PastOpps": PastOppsClean,
        "ConfHours": ConfHoursClean,
        "UnConfHours": UnConfHoursClean
    }
    return jsonify(FullClean)


@app.route('/Notifications', methods=["POST"])
@token_required
def Notifications(user):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        })
    Messages = NewUnconfHoursMessages.query.join(User).filter(
        User.District == user.District).all()
    CleanMessages = []
    for Message in Messages:
        CleanMessages.append({
            'ID': Message.Student.id,
            'Name': Message.Student.name,
            'StuId': Message.Student.pub_ID,
            'Hours': Message.Student.hours,
            'Message': f"{Message.Student.name} requested new hours."
        })
    return jsonify(CleanMessages)
