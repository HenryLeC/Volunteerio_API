from flask import Flask, request, jsonify
from API import app
from API.database import User, verify_auth_token

@app.route("/hours", methods=["POST"])
def getHours():
    token = request.form.get("token")
    user = verify_auth_token(token)
    if(user):
        return jsonify(user)