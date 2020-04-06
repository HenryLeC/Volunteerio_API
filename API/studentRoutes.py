from flask import Flask, request, jsonify
from API import app, db
from API.database import User, Opportunity, NewUnconfHoursMessages
from API.auth import verify_auth_token, generate_auth_token, token_required
from werkzeug.security import generate_password_hash as hash, check_password_hash
from json import loads
import pickle, datetime, jwt

@app.route("/hours", methods=["POST"])
@token_required
def getHours(user):
    return jsonify({'hours' : str(user.hours)})

@app.route('/addhours', methods=["POST"])
@token_required
def add_hours(user):
    # Check for hours and reason in request
    try:
        hours = request.form["hours"]
        reason = request.form["reason"]
    except:
        return jsonify({'msg' : 'Hours and reason is required.'})
    id = user.HoursId
    
    # Increment HoursId by 1
    user.HoursId += 1

    # Add Hours to Unconfirmed List
    UnConfHrs = pickle.loads(user.unconfHours)
    # Add hous and reason to unconfirmed list
    print(pickle.loads(user.unconfHours))
    UnConfHrs.append({
        'id' : id,
        'hours' : int(hours),
        'reason' : reason
    })

    # Add To DB
    user.unconfHours = pickle.dumps(UnConfHrs)
    if len(user.UnconfHoursMessages) == 0:
        user.UnconfHoursMessages.append(NewUnconfHoursMessages())
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'msg' : 'Hours added',
        'unconfHours' : pickle.loads(user.unconfHours),
        'confHours' : pickle.loads(user.confHours)
    })

@app.route('/Opps', methods=["Post"])
@token_required
def list_opps(user):
    Opps = Opportunity.query.join(User).filter(User.District == user.District)
    CleanOpps = []
    for opp in Opps:
        CleanOpps.append({
            "ID": str(opp.id),
            "Name": opp.Name,
            "Location": opp.Location,
            "Hours": opp.Hours,
            "Time": opp.Time.strftime("%m/%d/%Y, %H:%M"),
            "Sponsor": User.query.get(int(opp.SponsorID)).name
        })
    return jsonify(CleanOpps)

@app.route('/ClockInOut', methods=["POST"])
@token_required
def Clock(user):
    try:
        Code = request.form["QrCode"]
    except:
        return jsonify({
            'msg': 'Please Pass in The Correct Parameters'
        })
    res = False
    RightDict = None
    for Dict in pickle.loads(user.CurrentOpps):
        try:
            if Dict["JWT"] == Code:
                res = True
                RightDict = Dict
                break
        except:
            pass
    
    if res == True:
        #STime = datetime.datetime.strptime(RightDict["StartTime"], "%Y-%m-%dT%H:%M:%S.%f%z")
        Hours = int(round((datetime.datetime.utcnow() - RightDict["StartTime"]).seconds / 3600))
        user.hours += Hours
        
        OppId = jwt.decode(Code, 'VerySecret', algorithm="HS256")["ID"]
        Opp = Opportunity.query.get(OppId)

        user.PastOpps.append(Opp)
        CurrentOpps = pickle.loads(user.CurrentOpps)
        CurrentOpps.remove(RightDict)
        user.CurrentOpps = pickle.dumps(CurrentOpps)
        
        db.session.add(user)
        db.session.commit()

        return jsonify({
            'msg': 'Thank You, Your Hours were added.'
        })

    else:
        CurrentOpps = pickle.loads(user.CurrentOpps)
        CurrentOpps.append({
            'StartTime': datetime.datetime.utcnow(),
            'JWT': Code
        })
        user.CurrentOpps = pickle.dumps(CurrentOpps)

        db.session.add(user)
        db.session.commit()

        return jsonify({
            'msg': "Thank You for clocking in, don't forget to clock out later."
        })

@app.route('/BookAnOpp', methods=["POST"])
@token_required
def BookAnOpp(user):
    try:
        Id = request.form["OppId"]
    except:
        return jsonify({
            'msg': 'Please Pass in The Correct Parameters'
        })
    try:
        Opp = Opportunity.query.get(Id)
    except:
        return jsonify({
            'msg': 'Inavalid Opportunity ID'
        })
    
    user.BookedOpps.append(Opp)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'msg': 'Opportunity Booked.'
    })

@app.route('/BookedOpps', methods=["Post"])
@token_required
def BookedOpps(user):
    Opps = user.BookedOpps
    CleanOpps = []
    for opp in Opps:
        CleanOpps.append({
            "Name": opp.Name,
            "Hours": opp.Hours,
            "Time": opp.Time.strftime("%m/%d/%Y, %H:%M")
        })
    return jsonify(CleanOpps)

@app.route('/PastOpps', methods=["Post"])
@token_required
def PastOpps(user):
    PastOpps = user.PastOpps
    PastOppsClean = []
    for opp in PastOpps:
        PastOppsClean.append({
            "Name": opp.Name,
            "Hours": opp.Hours,
            "Time": opp.Time.strftime("%m/%d/%Y, %H:%M")
        })
    confHours = pickle.loads(user.confHours)
    HoursClean = []
    for opp in confHours:
        HoursClean.append({
            "Hours": opp["hours"],
            "Reason": opp["reason"],
            "Confirmed": "Confirmed"
        })
    unconfHours = pickle.loads(user.unconfHours)
    for opp in unconfHours:
        HoursClean.append({
            "Hours": opp["hours"],
            "Reason": opp["reason"],
            "Confirmed": "Unconfirmed"
        })
    
    FullClean = {
        "PastOpps": PastOppsClean,
        "Hours": HoursClean,
    }
    return jsonify(FullClean)
