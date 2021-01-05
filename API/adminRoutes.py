from flask import request, jsonify, send_file
from sqlalchemy import or_, and_
from API import app, db
from API.database import (User,
                          School, Opportunity,
                          Groups)
from API.auth import token_required
import pickle
import requests
import json
import csv
import io


@app.route('/confirmHours', methods=["POST"])
@token_required
def confirmHours(user):
    # Move an Unconfiremd Hours to Confirmed

    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task'
        }), 500
    try:
        StuHrData = request.form['StuHrData']
    except KeyError:
        return jsonify({
            'msg': "Please provide an 'HoursId' and 'StudentId'"
        }), 500
    StuHrDataList = StuHrData.split(", ")
    Id = StuHrDataList[0]
    HrId = StuHrDataList[1]

    # Find The Student
    Student = User.query.get(Id)
    Student: User

    # Preform the move
    for Hours in pickle.loads(Student.unconfHours):
        if Hours['id'] == int(HrId):
            ConfHrs = pickle.loads(Student.confHours)
            UnconfHrs = pickle.loads(Student.unconfHours)
            ConfHrs.append(Hours)
            UnconfHrs.remove(Hours)
            if len(UnconfHrs) == 0:
                Student.UnConfHoursMessages = []
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
        }), 500
    try:
        StuHrData = request.form['StuHrData']
        StuHrDataList = StuHrData.split(", ")
        Id = StuHrDataList[0]
        HrId = StuHrDataList[1]
    except KeyError:
        return jsonify({
            'msg': "Please provide an 'HoursId' and 'StudentId'"
        }), 500

    # Find The Student
    Student = User.query.get(Id)

    # Preform the move
    for Hours in pickle.loads(Student.unconfHours):
        if Hours['id'] == int(HrId):
            UnconfHrs = pickle.loads(Student.unconfHours)
            UnconfHrs.remove(Hours)
            if len(UnconfHrs) == 0:
                Student.UnConfHoursMessages = []
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
def StudentsList(user: User):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        }), 500
    try:
        Filter = "%{}%".format(request.form["Filter"])
    except KeyError:
        return jsonify({
            'msg': ""
        }), 500
    ReturnList = []
    # Filter for students that Have a name or ID like like the Filter.
    Students = User.query.filter(and_(
        User.is_student,
        User.School == user.School,
        or_(
            User.name.like(Filter),
            User.pub_ID.like(Filter),
        )
    )).limit(5)

    for student in Students:
        student: User
        ReturnList.append({
            "Name": student.name,
            "StuId": student.pub_ID,
            "Hours": str(student.hours),
            "ID": student.id,
            "HoursGoal": str(student.getGoal()),
            "userSpecific": "true" if student.UserGoal else "false",
            "group": student.group.name if student.group else "None"
        })
    return jsonify(ReturnList)


@app.route('/StudentHours', methods=["POST"])
@token_required
def StudentHours(user: User):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        }), 500
    try:
        StudentId = request.form["id"]
    except KeyError:
        return jsonify({
            'msg': "Please Supply a Student Id"
        }), 500

    student = User.query.get(int(StudentId))

    PastOpps = student.PastOpps
    Pasts = student.Past
    PastOppsClean = []
    for opp in PastOpps:
        past = None
        for i in Pasts:
            if i.opp_id == opp.id:
                past = i
                break
        if past is not None:
            PastOppsClean.append({
                "Name": opp.Name,
                "Hours": past.hours,
                "Time": opp.Time.strftime("%m/%d/%Y, %H:%M")
            })
    confHours = pickle.loads(student.confHours)
    ConfHoursClean = []
    for opp in confHours:
        ConfHoursClean.append({
            "Hours": opp["hours"],
            "Reason": opp["reason"],
            "Desc": opp["desc"],
            "Confirmed": "Confirmed",
            "UnconfirmedBool": "False"
        })
    unconfHours = pickle.loads(student.unconfHours)
    UnConfHoursClean = []
    for opp in unconfHours:
        UnConfHoursClean.append({
            "StuHrData": "{}, {}".format(student.id, opp["id"]),
            "Hours": opp["hours"],
            "Reason": opp["reason"],
            "Desc": opp["desc"],
            "Confirmed": "Unconfirmed",
            "UnconfirmedBool": "True"
        })

    FullClean = {
        "PastOpps": PastOppsClean,
        "Hours": ConfHoursClean + UnConfHoursClean
    }
    return jsonify(FullClean)


# region NewStudent OLD DEPRECATED
# Implememted Auth Seperately for Json data
# @app.route('/NewStudent', methods=["POST"])
# def NewStudent():
#     try:
#         inputData = request.get_json()
#         InvalidUsers = []

#         if 'x-access-token' in inputData:
#             token = inputData['x-access-token']

#         if not token:
#             return jsonify({'message': 'Token is missing!'}), 401

#         current_user = verify_auth_token(token)
#         if not current_user:
#             return jsonify({'message': 'Token is invalid!'}), 401

#         if not current_user.is_admin:
#             return jsonify({
#                 'msg': 'Must not be a Student to preform this task'
#             }), 500

#         for user in inputData["users"]:
#             try:
#                 UserObj = User(user["username"], user["password"],
#                                user["name"], user["Id"],
#                                student=True)
#                 db.session.add(UserObj)
#             except KeyError:
#                 InvalidUsers.append(user)
#         db.session.commit()
#         return jsonify({
#             "Invalid Users": InvalidUsers
#         })
#     except Exception:
#         db.session.add(Logs(traceback.format_exc()))
#         db.session.commit()
#         return "", 500
# endregion


# region Add District (Districts Removed) DEPRECATED
# @app.route('/addDistrict', methods=['POST'])
# @token_required
# def addDistrict(user):
#     try:
#         if not user.is_admin:
#             return jsonify({
#                 'msg': 'Must be Administrator to preform this task.'
#             }), 500
#         try:
#             DistrictName = request.form["name"]
#         except KeyError:
#             return jsonify({
#                 'msg': "Please Supply a District Name"
#             }), 500

#         district = District(DistrictName)
#         db.session.add(district)
#         db.session.commit()

#         return jsonify({
#             "msg": f"New District {DistrictName} added with id {district.id}",
#             "name": DistrictName,
#             "id": str(district.id)
#         })
#     except Exception:
#         db.session.add(Logs(traceback.format_exc()))
#         db.session.commit()
#         return "", 500
# endregion


@app.route('/addSchool', methods=['POST'])
@token_required
def addSchool(user: User):
    if not user.is_webmaster:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        }), 500
    try:
        SchoolName = request.form["name"]
    except KeyError:
        return jsonify({
            'msg': "Please Supply a School Name"
        }), 500

    school = School(SchoolName)
    db.session.add(school)
    db.session.commit()

    return jsonify({
        "msg": f"New School {SchoolName} added with id {school.id}",
        "name": SchoolName,
        "id": str(school.id)
    })


@app.route('/ConfDelOpp', methods=["POST"])
@token_required
def ConfDelOpp(user: User):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        }), 500
    try:
        mode = request.form["Mode"]
        oppId = request.form["ID"]
    except KeyError:
        return jsonify({
            'msg': "Plese Send Proper Parameters"
        })

    opp = Opportunity.query.get(oppId)
    opp: Opportunity
    spons = opp.sponsor

    APIKey = json.loads(open("APIKeys.json", "r").read())["MailGun"]

    if mode == "Delete":
        db.session.delete(opp)
        if spons.email:
            requests.post(
                "https://api.mailgun.net/v3/volunteerio.us/messages",
                auth=("api", APIKey),
                data={"from": "Volunteerio <noreply@volunteerio.us>",
                      "to": [spons.email],
                      "subject": "Your Opportunity",
                      "text": "Your Opportunity has been deleted"})
    elif mode == "Confirm":
        opp.Confirmed = True
        if spons.email:
            requests.post(
                "https://api.mailgun.net/v3/volunteerio.us/messages",
                auth=("api", APIKey),
                data={"from": "Volunteerio <noreply@volunteerio.us>",
                      "to": [spons.email],
                      "subject": "Your Opportunity",
                      "text": "Your Opportunity has been confirmed"})

    db.session.commit()
    return jsonify({
        'msg': 'Sucsess'
    })


@app.route('/UnconfOpps', methods=["POST"])
@token_required
def UnconfOpps(user: User):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        }), 500

    OppMessages = Opportunity.query.join(User).filter(
        User.School == user.School,
        Opportunity.Confirmed.is_(False)
    ).all()

    CleanMessages = []

    for Message in OppMessages:
        CleanMessages.append({
            'ID': str(Message.id),
            'Name': Message.Name,
            'Location': Message.Location,
            'Hours': Message.Hours,
            'Time': Message.getTime(),
            'Sponsor': Message.sponsor.name,
            'Class': Message.Class,
            'MaxVols': Message.MaxVols
        })

    return jsonify(CleanMessages)


@app.route('/addUsers', methods=["POST"])
@token_required
def addUsers(user: User):
    try:
        usersC = int(request.form["users"])
    except Exception:
        return "", 500

    for i in range(usersC):
        st = False
        t = False
        ad = False
        co = False
        role = request.form["user" + str(i) + "R"]
        if role == "Student":
            st = True
        elif role == "Teacher":
            t = True
        elif role == "Admin":
            ad = True
        elif role == "Community Member":
            co = True
        us = User(
            request.form["user" + str(i) + "UN"],
            request.form["user" + str(i) + "P"],
            request.form["user" + str(i) + "N"],
            request.form["user" + str(i) + "I"],
            user.School,
            student=st, admin=ad,
            teacher=t, community=co
        )
        db.session.add(us)

    db.session.commit()

    return "", 200


@app.route('/schoolSettings', methods=["POST"])
@token_required
def schoolSettings(user: User):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        }), 500

    return jsonify({
        "SGoal": user.School.hoursGoal
    })


@app.route("/schoolGoal", methods=["POST"])
@token_required
def schoolGoal(user: User):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        }), 500

    try:
        hours = int(request.form["Goal"])
    except KeyError:
        return jsonify({
            'msg': "Plese Send Proper Parameters"
        })

    s = user.School
    s: School
    s.hoursGoal = hours

    db.session.add(s)
    db.session.commit()

    return jsonify({
        "msg": "Updated Succsesfully"
    })


@app.route("/StudentReport", methods=["POST"])
@token_required
def StudentReport(user: User):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        }), 500

    users = User.query.filter(
        and_(
            User.is_student,
            User.School == user.School,
        )
    ).all()

    csvf = io.StringIO()
    writer = csv.writer(csvf, delimiter=",")
    writer.writerow(["Name", "ID", "Hours", "HoursGoal"])

    for stu in users:
        stu: User
        writer.writerow([stu.name, stu.pub_ID, stu.hours, stu.getGoal()])

    csvf.seek(0)
    mem = io.BytesIO(csvf.getvalue().encode('utf-8'))
    mem.seek(0)
    csvf.close()
    return send_file(
        mem,
        as_attachment=True,
        mimetype="text/csv",
        attachment_filename="StudentReport.csv"
    )


@app.route("/UserSpecificGoal", methods=["POST"])
@token_required
def UserSpecificGoal(user: User):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        }), 500

    try:
        user = User.query.get(request.form["userId"])
        goal = request.form["goal"]
    except KeyError:
        return jsonify({
            'msg': "Plese Send Proper Parameters"
        })

    if goal != "":
        user.UserGoal = goal
    else:
        user.UserGoal = None
    db.session.add(user)
    db.session.commit()

    return str(user.getGoal())


@app.route('/makeGroup', methods=["POST"])
@token_required
def makeGroup(user: User):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        }), 500

    try:
        goal = request.form["hoursGoal"]
        name = request.form["name"]
    except KeyError:
        return jsonify({
            'msg': "Plese Send Proper Parameters"
        })

    school: School = user.School
    school.groups.append(Groups(name, int(goal)))

    db.session.commit()
    return jsonify({
        'msg': "Success!"
    }), 200


@app.route('/getGroups', methods=["POST"])
@token_required
def getGroups(user: User):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        }), 500

    school: School = user.School
    groups: list[Groups] = school.groups
    returnClean = []

    for group in groups:
        students = []
        for stu in group.users:
            stu: User
            students.append({
                "name": stu.name,
                "id": str(stu.id)
            })
        returnClean.append({
            "id": str(group.id),
            "name": group.name,
            "hoursGoal": str(group.hoursGoal),
            "students": json.dumps(students)
        })

    return jsonify(returnClean), 200


@app.route('/changeUserGroup', methods=["POST"])
@token_required
def changeUserGroup(user: User):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        }), 500

    try:
        groupId = int(request.form["groupId"])
        studentId = request.form["userId"]
    except KeyError:
        return jsonify({
            'msg': "Plese Send Proper Parameters"
        })

    student = User.query.get(studentId)
    student: User
    if groupId == -10:
        student.group = None
    else:
        group = Groups.query.get(groupId)
        student.group = group

    db.session.commit()

    return str(student.getGoal())


@app.route('/deleteGroup', methods=["POST"])
@token_required
def deleteGroup(user: User):
    if not user.is_admin:
        return jsonify({
            'msg': 'Must be Administrator to preform this task.'
        }), 500

    try:
        groupId = request.form["groupId"]
    except KeyError:
        return jsonify({
            'msg': "Plese Send Proper Parameters"
        })

    db.session.delete(Groups.query.get(groupId))
    db.session.commit()

    return jsonify({
        'msg': "Success!"
    })
