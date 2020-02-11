from API import app, db
from API.auth import verify_auth_token, generate_auth_token, token_required
from werkzeug.security import check_password_hash
from API.database import User
from flask import jsonify, request

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