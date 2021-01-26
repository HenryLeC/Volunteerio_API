import datetime
import json
import pickle

import requests
from dateutil import parser
from flask import jsonify, redirect, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash

from API import app, db
from API.auth import (confirm_token, generate_auth_token,
                      generate_confirmation_token, token_required)
from API.database import (InCompleteOppMessages, NewUnconfHoursMessages,
                          Opportunity, Past, User)


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
        user: User
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
                'role': role,
                'firstTime': user.firstTime
            })
        else:
            return jsonify({'msg': 'Invalid Login information'}), 401
    except Exception:
        return jsonify({'msg': 'Invalid Login information'}), 401


@app.route('/AddOpp', methods=["POST"])
@token_required
def AddOpp(user: User):
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
        try:
            Virtual = request.form["Virtual"]
        except KeyError:
            Virtual = "False"
    except KeyError:
        return jsonify({
            'msg': 'Please attach the proper parameters'
        }), 500

    try:
        # Take Colon Seperated UTC offset and make it non Colon Seperated
        if ":" == Date[-3:-2]:
            Date = Date[:-3] + Date[-2:]
        Parsed = datetime.datetime.strptime(Date, "%Y-%m-%dT%H:%M:%S%z")
    except Exception:
        Parsed = parser.isoparse(Date)

    Opp = Opportunity(Name, Location, Parsed, Hours, Class,
                      MaxVols, user, Description, user.is_admin, True if Virtual == "True" else False)
    user.Opportunities.append(Opp)

    db.session.add(Opp)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'msg': 'Opportunity Added'
    })


@app.route('/SignInStudents', methods=["POST"])
@token_required
def SignInStudents(user):
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
    # return jwt.encode({'ID': str(OppId)}, app.config['SECRET_KEY'],
    #                   algorithm='HS256')
    return Opportunity.query.get(OppId).ClockCode


@app.route('/MyOpps', methods=["POST"])
@token_required
def MyOpps(user: User):
    if not user.is_admin and not user.is_community:
        return jsonify({
            'msg': 'Must not be a Student to preform this task'
        }), 500
    Opps = user.Opportunities
    CleanOpps = []
    for opp in Opps:
        opp: Opportunity
        CleanOpps.append({
            "ID": str(opp.id),
            "Name": opp.Name,
            "Location": opp.Location,
            "Hours": opp.Hours,
            "Time": opp.getTime(),
            "Sponsor": User.query.get(opp.sponsor_id).name,
            "Class": opp.Class,
            "CurrentVols": len(opp.BookedStudents),
            "MaxVols": opp.MaxVols,
            "Confirmed": opp.Confirmed
        })
    return jsonify(CleanOpps)


@app.route('/BookedStudents', methods=["POST"])
@token_required
def BookedStudents(user: User):
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


@app.route('/DeleteOpp', methods=["POST"])
@token_required
def DeleteOpp(user):
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

    Opp = Opportunity.query.get(OppId)
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


@app.route('/Notifications', methods=["POST"])
@token_required
def Notifications(user: User):
    CleanMessages = []

    if user.is_admin:
        HourMessages = NewUnconfHoursMessages.query.join(User).filter(
            User.School == user.School).all()
        # OppMessages = Opportunity.query.join(User).filter(
        #     User.District == user.District,
        #     Opportunity.Confirmed.is_(False)
        # ).all()
        for Message in HourMessages:
            Message: NewUnconfHoursMessages

            CleanMessages.append({
                'ID': Message.student.id,
                'Name': Message.student.name,
                'StuId': Message.student.pub_ID,
                'Hours': Message.student.hours,
                'Message': f"{Message.student.name} requested new hours.",
                'Type': "Hour",
                'HoursGoal': str(Message.student.getGoal()),
                'userSpecific': "true" if Message.student.UserGoal else "false",
                "group": Message.student.group.name if Message.student.group else "None"
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
            Opportunity.sponsor == user
        ).all()

        for Message in IncompleteOpps:
            CleanMessages.append({
                'ID': str(Message.id),
                'Message': f"{Message.student.name} completed your opportunity.",
                'Student': Message.student.name,
                'OppName': Message.opportunity.Name,
                'OppHours': Message.opportunity.Hours,
                "StuCompleted": f"{Message.HoursCompleted} Hours, {Message.MinutesCompleted} Minutes",
                'Type': 'IncompleteOpp'
            })

    return jsonify(CleanMessages)


@app.route('/ConfParticipation', methods=["POST"])
@token_required
def ConfParticipation(user: User):
    if user.is_student:
        return jsonify({
            'msg': "Must not be a student to preform this action"
        })
    try:
        msgId = request.form["ID"]
        hours = int(request.form["Hours"])
    except KeyError:
        return({
            'msg': "Please pass correct parameters"
        }), 500
    msg = InCompleteOppMessages.query.get(msgId)
    stu = msg.student
    opp = msg.opportunity
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

    cOpps = pickle.loads(stu.CurrentOpps)
    cOpps.remove(RightDict)

    stu.CurrentOpps = pickle.dumps(cOpps)
    stu.PastOpps.append(msg.opportunity)
    for i in stu.Past:
        i: Past
        if i.opp_id == opp.id:
            i.hours = hours

    db.session.add(stu)
    db.session.add(opp)
    db.session.commit()

    return jsonify({
        'msg': "Success, Hours Awarded"
    })


@app.route("/FirstSetup", methods=["POST"])
@token_required
def FirstSetup(user: User):
    try:
        Pass = request.form["password"]
        Email = request.form["email"]
    except KeyError:
        return({
            'msg': "Please pass correct parameters"
        }), 500

    user.firstTime = False
    user.password = generate_password_hash(Pass)
    user.email = Email

    db.session.add(user)
    db.session.commit()

    APIKey = json.loads(open("APIKeys.json", "r").read())["MailGun"]

    requests.post(
        "https://api.mailgun.net/v3/volunteerio.us/messages",
        auth=("api", APIKey),
        data={"from": "Volunteerio <noreply@volunteerio.us>",
              "to": [Email],
              "subject": "Email Confirmation",
              "text": "Please Confirm Your Email.\n Click {} to confirm. This link will expire in 1 hour.".format("https://www.volunteerio.us/api/confirm/" + generate_confirmation_token(user.id))})

    return jsonify({
        "msg": "Updated Sucsessfully"
    }), 200


@app.route("/confirm/<userT>", methods=["GET"])
def confirmEmail(userT):
    try:
        user = confirm_token(userT)
    except Exception:
        return "Invalid Token"

    user = User.query.get(user)
    user: User

    if user.emailConfirmed:
        return "Email Already Confirmed"
    else:
        user.emailConfirmed = True
        db.session.add(user)
        db.session.commit()

        return "Email Confirmed"


@app.route("/resetPassword", methods=["POST"])
def resetPasswordRequest():
    try:
        uname = request.form["uname"]
    except KeyError:
        return({
            'msg': "Please pass correct parameters"
        }), 500

    user = User.query.filter(
        User.username == uname
    ).first()
    user: User

    if user is None:
        return jsonify({
            "title": "Error",
            "msg": "User does not exist"
        })

    if user.emailConfirmed:
        token = generate_confirmation_token(user.id)

        APIKey = json.loads(open("APIKeys.json", "r").read())["MailGun"]

        requests.post(
            "https://api.mailgun.net/v3/volunteerio.us/messages",
            auth=("api", APIKey),
            data={
                "from": "Volunteerio <noreply@volunteerio.us>",
                "to": [user.email],
                "subject": "Password Reset",
                "text": "Password rest link requested.\n Click {} to reset. If you didnt request this link please disregard. This link will expire in 1 hour.".format("https://www.volunteerio.us/api/resetPassword/" + token)
            }
        )

        return jsonify({
            "title": "Success",
            "msg": "Password reset link sent to your email."
        })
    else:
        if user.is_student:
            return jsonify({
                "title": "Error",
                "msg": "No confirmed email, ask an administrator for help"
            })
        else:
            return jsonify({
                "title": "Error",
                "msg": "No confirmed email."
            })


@app.route("/resetPassword/<Token>", methods=["GET", "POST"])
def resetPasswordWeb(Token):
    if request.method == "GET":
        return render_template("passwordReset.html")
    elif request.method == "POST":
        try:
            passw = request.form["password1"]
        except KeyError:
            return({
                'msg': "Please pass correct parameters"
            }), 500

        user = User.query.get(confirm_token(Token))
        user: User

        user.password = generate_password_hash(passw)
        db.session.add(user)
        db.session.commit()

        return "Password Changed", 200


@app.route("/health")
def healthCheck():
    return "Healthy", 200
