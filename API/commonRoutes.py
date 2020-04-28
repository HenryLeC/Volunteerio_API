from API import app, db
from API.auth import generate_auth_token, token_required
from werkzeug.security import check_password_hash
from API.database import User, Opportunity
from flask import jsonify, request
import datetime
import jwt
import logging


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
            else:
                role = 'community'

            # return auth token and role
            return jsonify({
                'key': generate_auth_token(user.id).decode("utf-8"),
                'role': role
            })
    except Exception:
        return jsonify({'msg': 'Invalid Login information'}), 401


@app.route('/AddOpp', methods=["POST"])
@token_required
def AddOpp(user):
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
        except KeyError:
            return jsonify({
                'msg': 'Please attach the proper parameters'
            }), 500

        Parsed = datetime.datetime.strptime(Date, "%Y-%m-%dT%H:%M:%S")

        Opp = Opportunity(Name, Location, Parsed, Hours, user)
        user.Opportunities.append(Opp)

        db.session.add(Opp)
        db.session.add(user)
        db.session.commit()

        return jsonify({
            'msg': 'Opportunity Added'
        })
    except Exception:
        logging.exception('')
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
        return jwt.encode({'ID': OppId}, 'VerySecret', algorithm='HS256')
    except Exception:
        logging.exception('')
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
                "Time": opp.Time,
                "Location": opp.Location
            })
        return jsonify(CleanOpps)
    except Exception:
        logging.exception('')
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
        logging.exception('')
        return "", 500
