from flask import Flask, request, jsonify
from API import app, db
from API.database import User
from API.auth import verify_auth_token, generate_auth_token, token_required
from werkzeug.security import generate_password_hash as hash, check_password_hash

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
    try:
        id = int(user.unconfHours[-1].id) + 1
    except IndexError:
        id = 1
    if conf == 'True':
        user.hours += hours
        user.confHours.append({
            'id' : id,
            'hours' : int(hours),
            'reason' : reason
        })
        db.session.add(user)
        db.session.commit()
    else:
        # Add hous and reason to unconfirmed list
        user.unconfHours.append({
            'id' : id,
            'hours' : int(hours),
            'reason' : reason
        })
        db.session.add(user)
        db.session.commit()

    return jsonify({
        'msg' : 'Hours added',
        'unconfHours' : user.unconfHours,
        'confHours' : user.confHours
    })
    