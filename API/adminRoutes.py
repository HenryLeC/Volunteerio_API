from flask import request, jsonify
from sqlalchemy import or_, and_
from API import app, db
from API.database import User, NewUnconfHoursMessages, District, Logs, School
from API.auth import token_required, verify_auth_token
import pickle
import traceback


@app.route('/confirmHours', methods=["POST"])
@token_required
def confirmHours(user):
    try:
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
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/deleteHours', methods=["POST"])
@token_required
def deleteHours(user):
    try:
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
                    Student.UnconfHoursMessages = []
                Student.unconfHours = pickle.dumps(UnconfHrs)

                db.session.add(Student)
                db.session.commit()

        return jsonify({
            'msg': 'Hours Removed',
            'unconfHours': pickle.loads(Student.unconfHours),
            'confHours': pickle.loads(Student.confHours)
        })
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/StudentsList', methods=["POST"])
@token_required
def StudentsList(user):
    try:
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
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/StudentHours', methods=["POST"])
@token_required
def StudentHours(user):
    try:
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
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/Notifications', methods=["POST"])
@token_required
def Notifications(user):
    try:
        if not user.is_admin:
            return jsonify({
                'msg': 'Must be Administrator to preform this task.'
            }), 500
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
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500

# Implememted Auth Seperately for Json data
@app.route('/NewStudent', methods=["POST"])
def NewStudent():
    try:
        inputData = request.get_json()
        InvalidUsers = []

        if 'x-access-token' in inputData:
            token = inputData['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        current_user = verify_auth_token(token)
        if not current_user:
            return jsonify({'message': 'Token is invalid!'}), 401

        if not current_user.is_admin:
            return jsonify({
                'msg': 'Must not be a Student to preform this task'
            }), 500

        for user in inputData["users"]:
            try:
                UserObj = User(user["username"], user["password"], user["name"], user["Id"], District.query.filter_by(id=user["District"]).first(), student=True)
                db.session.add(UserObj)
            except KeyError:
                InvalidUsers.append(user)
        db.session.commit()
        return jsonify({
            "Invalid Users": InvalidUsers
        })
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/addDistrict', methods=['POST'])
@token_required
def addDistrict(user):
    try:
        if not user.is_admin:
            return jsonify({
                'msg': 'Must be Administrator to preform this task.'
            }), 500
        try:
            DistrictName = request.form["name"]
        except KeyError:
            return jsonify({
                'msg': "Please Supply a District Name"
            }), 500

        district = District(DistrictName)
        db.session.add(district)
        db.session.commit()

        return jsonify({
            "msg": f"New District {DistrictName} added with id {district.id}",
            "name": DistrictName,
            "id": str(district.id)
        })
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500

@app.route('/addSchool', methods=['POST'])
@token_required
def addSchool(user):
    try:
        if not user.is_admin:
            return jsonify({
                'msg': 'Must be Administrator to preform this task.'
            }), 500
        try:
            SchoolName = request.form["name"]
            DistrictId = request.form["districtId"]
        except KeyError:
            return jsonify({
                'msg': "Please Supply a District Name"
            }), 500

        school = School(SchoolName)
        district = District.query.get(DistrictId)
        district.schools.append(school)
        db.session.add(school)
        db.session.add(district)
        db.session.commit()

        return jsonify({
            "msg": f"New School {SchoolName} added with id {school.id}",
            "name": SchoolName,
            "id": str(school.id)
        })
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500
