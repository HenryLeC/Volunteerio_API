from flask import Flask, request, jsonify
from API import app, db
from API.database import User, Opportunity
from API.auth import verify_auth_token, generate_auth_token, token_required
from werkzeug.security import generate_password_hash as hash, check_password_hash
from json import loads
import pickle

@app.route("/hours", methods=["POST"])
@token_required
def getHours(user):
    return jsonify({'hours' : user.hours})

@app.route('/addhours', methods=["POST"])
@token_required
def add_hours(user):
    # Check for hours and reason in request
    try:
        hours = request.form["hours"]
        reason = request.form["reason"]
    except:
        return jsonify({'msg' : 'Hours and reason is required.'})
    # Try to get confirmed
    conf = request.form.get('confirmation')
    id = user.HoursId
    if conf == 'True':
        # Increment HoursId by 1
        user.HoursId += 1

        # Add Hours to Confirmed List
        ConfHrs = pickle.loads(user.confHours)
        user.hours += int(hours)
        ConfHrs.append({
            'id' : id,
            'hours' : int(hours),
            'reason' : reason
        })

        # Add To DB
        user.confHours = pickle.dumps(ConfHrs)
        db.session.add(user)
        db.session.commit()
    else:
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
    Opps = Opportunity.query.all()
    CleanOpps = []
    for opp in Opps:
        CleanOpps.append({
            "ID": str(opp.id),
            "Name": opp.Name,
            "Location": opp.Location,
            "Hours": opp.Hours,
            "Time": opp.Time.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
            "Sponsor": User.query.get(int(opp.SponsorId)).name
        })
    return jsonify(CleanOpps)