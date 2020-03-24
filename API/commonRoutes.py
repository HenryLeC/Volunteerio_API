from API import app, db
from API.auth import verify_auth_token, generate_auth_token, token_required
from werkzeug.security import check_password_hash
from API.database import User, Opportunity
from flask import jsonify, request
import datetime, jwt

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

@app.route('/AddOpp', methods=["POST"])
@token_required
def AddOpp(user):
    if user.is_admin != True and user.is_community != True:
        return jsonify({
            'msg': 'Must not be a Student to preform this task'
        })
    try:
        Name = request.form["Name"]
        Date = request.form["Date"]
        Location = request.form["Location"]
        Hours = request.form["Hours"]
    except:
        return jsonify({
            'msg': 'Please attach the proper parameters'
        })
    
    Parsed = datetime.datetime.strptime(Date, "%Y-%m-%dT%H:%M:%S.%f%z")
    print(Parsed)
    
    Opp = Opportunity(Name, Location, Parsed, Hours, user)
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
    if user.is_admin != True and user.is_community != True:
        return jsonify({
            'msg': 'Must not be a Student to preform this task'
        })
    try:
        OppId = request.form["OppId"]
    except:
        return jsonify({
            'msg': 'Please attach the proper parameters'
        })
    return jwt.encode({'ID': OppId}, 'VerySecret', algorithm='HS256')

@app.route('/MyOpps', methods=["POST"])
@token_required
def MyOpps(user):
    if user.is_admin != True and user.is_community != True:
        return jsonify({
            'msg': 'Must not be a Student to preform this task'
        })
    Opps = user.Opportunities
    CleanOpps = []
    for opp in Opps:
        CleanOpps.append({
            "ID": str(opp.id),
            "Name": opp.Name
        })
    return jsonify(CleanOpps)
