from API import app, db
from API.auth import generate_auth_token, token_required
from werkzeug.security import check_password_hash
from API.database import (User, Opportunity, Logs,
                          NewUnconfHoursMessages, InCompleteOppMessages)
from flask import jsonify, request, redirect
import datetime
import jwt
import traceback
import pickle


@app.route('/')
def index():
    return redirect("https://volunteerio.us")


@app.route('/login', methods=["POST"])
def login():
    # Check for Username and Password
    try:
        uname = request.form["username"]
        passw = request.form["password"]
    except KeyError:
        return jsonify({'msg': 'Login information required'}), 401

    try:
        # Find user by Uname and check hashed password
        user = User.query.filter_by(username=uname).first()
        if check_password_hash(user.password, passw):
            # Make role
            role = ''
            if user.is_student:
                role = 'student'
            elif user.is_admin:
                role = 'admin'
            elif user.is_teacher:
                role = 'teacher'
            else:
                role = 'community'

            # return auth token and role
            return jsonify({
                'key': generate_auth_token(user.id).decode("utf-8"),
                'role': role
            })
        else:
            return jsonify({'msg': 'Invalid Login information'}), 401
    except Exception:
        return jsonify({'msg': 'Invalid Login information'}), 401


@app.route('/AddOpp', methods=["POST"])
@token_required
def AddOpp(user: User):
    try:
        if not user.is_admin and not user.is_community:
            return jsonify({
                'msg': 'Must not be a Student to preform this task'
            }), 500
        try:
            Name = request.form["Name"]
            Date = request.form["Date"]
            Location = request.form["Location"]
            Hours = request.form["Hours"]
            Class = request.form["Class"]
            MaxVols = int(request.form["MaxVols"])
            Description = request.form["Description"]
        except KeyError:
            return jsonify({
                'msg': 'Please attach the proper parameters'
            }), 500

        # Take Colon Seperated UTC offset and make it non Colon Seperated
        if ":" == Date[-3:-2]:
            Date = Date[:-3] + Date[-2:]
        Parsed = datetime.datetime.strptime(Date, "%Y-%m-%dT%H:%M:%S%z")

        Opp = Opportunity(Name, Location, Parsed, Hours, Class,
                          MaxVols, user, Description, user.is_admin)
        user.Opportunities.append(Opp)

        db.session.add(Opp)
        db.session.add(user)
        db.session.commit()

        return jsonify({
            'msg': 'Opportunity Added'
        })
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/SignInStudents', methods=["POST"])
@token_required
def SignInStudents(user):
    try:
        if not user.is_admin and not user.is_community:
            return jsonify({
                'msg': 'Must not be a Student to preform this task'
            }), 500
        try:
            OppId = request.form["OppId"]
        except KeyError:
            return jsonify({
                'msg': 'Please attach the proper parameters'
            }), 500
        return jwt.encode({'ID': str(OppId)}, app.config['SECRET_KEY'],
                          algorithm='HS256')
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/MyOpps', methods=["POST"])
@token_required
def MyOpps(user):
    try:
        if not user.is_admin and not user.is_community:
            return jsonify({
                'msg': 'Must not be a Student to preform this task'
            }), 500
        Opps = user.Opportunities
        CleanOpps = []
        for opp in Opps:
            CleanOpps.append({
                "ID": str(opp.id),
                "Name": opp.Name,
                "Location": opp.Location,
                "Hours": opp.Hours,
                "Time": opp.getTime(),
                "Sponsor": User.query.get(int(opp.SponsorID)).name,
                "Class": opp.Class,
                "CurrentVols": len(opp.BookedStudents),
                "MaxVols": opp.MaxVols
            })
        return jsonify(CleanOpps)
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/BookedStudents', methods=["POST"])
@token_required
def BookedStudents(user):
    try:
        if not user.is_admin and not user.is_community:
            return jsonify({
                'msg': 'Must not be a Student to preform this task'
            }), 500
        try:
            Id = request.form["OppId"]
        except KeyError:
            return jsonify({
                'msg': 'Please attach the proper parameters'
            }), 500

        opp = Opportunity.query.get(Id)
        students = [student for student in opp.BookedStudents]
        studentsLofD = []
        for student in students:
            studentsLofD.append({"name": student.name})
        return jsonify(studentsLofD)
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/DeleteOpp', methods=["POST"])
@token_required
def DeleteOpp(user):
    try:
        if not user.is_admin and not user.is_community:
            return jsonify({
                'msg': 'Must not be a Student to preform this task'
            }), 500

        try:
            OppId = request.form["OppId"]
        except KeyError:
            return jsonify({
                'msg': 'Please attach the proper parameters'
            }), 500

        Opp = Opportunity.query.get(int(OppId))
        Opp: Opportunity

        # Fun issues (Wont Delete Opp with Booked or Past Students)
        Opp.BookedStudents = []
        Opp.Booked = []
        Opp.Past = []
        Opp.PastStudents = []

        db.session.delete(Opp)
        db.session.commit()

        return jsonify({
            "msg": "Opportunity Deleted"
        })

    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/Notifications', methods=["POST"])
@token_required
def Notifications(user: User):
    try:
        CleanMessages = []

        if user.is_admin:
            HourMessages = NewUnconfHoursMessages.query.join(User).filter(
                User.District == user.District).all()
            # OppMessages = Opportunity.query.join(User).filter(
            #     User.District == user.District,
            #     Opportunity.Confirmed.is_(False)
            # ).all()
            for Message in HourMessages:
                schoolGoal = user.School.hoursGoal
                districtGoal = user.District.hoursGoal
                goal = 0
                if schoolGoal is not None:
                    goal = schoolGoal
                elif districtGoal is not None:
                    goal = districtGoal

                CleanMessages.append({
                    'ID': Message.Student.id,
                    'Name': Message.Student.name,
                    'StuId': Message.Student.pub_ID,
                    'Hours': Message.Student.hours,
                    'Message': f"{Message.Student.name} requested new hours.",
                    'Type': "Hour",
                    'HoursGoal': str(goal)
                })
            # for Message in OppMessages:
            #     CleanMessages.append({
            #         'ID': str(Message.id),
            #         'Name': Message.Name,
            #         'Location': Message.Location,
            #         'Hours': Message.Hours,
            #         'Time': Message.getTime(),
            #         'Sponsor': Message.Sponsor.name,
            #         'Class': Message.Class,
            #         'MaxVols': Message.MaxVols,
            #         'Message': f"{Message.Sponsor.name} posted a new Opportunity.",
            #         'Type': "Opportunity"
            #     })
        if user.is_community or user.is_admin:
            IncompleteOpps = InCompleteOppMessages.query.join(Opportunity).filter(
                Opportunity.Sponsor == user
            ).all()

            for Message in IncompleteOpps:
                CleanMessages.append({
                    'ID': str(Message.id),
                    'Message': f"{Message.Student.name} only completed part of your opportunity.",
                    'Student': Message.Student.name,
                    'OppName': Message.Opportunity.Name,
                    'OppHours': Message.Opportunity.Hours,
                    "StuCompleted": f"{Message.HoursCompleted} Hours, {Message.MinutesCompleted} Minutes",
                    'Type': 'IncompleteOpp'
                })

        return jsonify(CleanMessages)
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/ConfParticipation', methods=["POST"])
@token_required
def ConfParticipation(user: User):
    try:
        if user.is_student:
            return jsonify({
                'msg': "Must not be a student to preform this action"
            })
        try:
            msgId = int(request.form["ID"])
            hours = int(request.form["Hours"])
        except KeyError:
            return({
                'msg': "Please pass correct parameters"
            }), 500
        msg = InCompleteOppMessages.query.get(msgId)
        stu = msg.Student
        opp = msg.Opportunity
        db.session.delete(msg)

        stu.hours += hours

        RightDict = None

        for Dict in pickle.loads(stu.CurrentOpps):
            if Dict["ID"] == str(opp.id):
                RightDict = Dict
                break

        if RightDict is None:
            return jsonify({
                'msg': "Server Error"
            }), 500

        stu.CurrentOpps = pickle.dumps(pickle.loads(stu.CurrentOpps).remove(RightDict))
        stu.PastOpps.append(msg.Opportunity)

        db.session.add(stu)
        db.session.add(opp)
        db.session.commit()

        return jsonify({
            'msg': "Success, Hours Awarded"
        })

    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500
