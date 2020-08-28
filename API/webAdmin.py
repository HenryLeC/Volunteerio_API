from API import app
from flask_login import (login_user, login_required, LoginManager,
                         logout_user, current_user)
from werkzeug.security import check_password_hash
from flask import request, redirect, render_template, url_for
from API.database import User, Logs

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/back/logout")
@login_required
def backLogout():
    logout_user()
    return redirect(url_for("backLogin"))


@app.route("/back/login", methods=["GET", "POST"])
def backLogin():
    if request.method == "GET":
        return render_template("login.html")
    else:
        Uname = request.form.get("uname")
        Pass = request.form.get("pass")

        user = User.query.filter_by(username=Uname).first()

        if check_password_hash(user.password, Pass):
            login_user(user, remember=True)
            if user.is_webmaster:
                return redirect(url_for("backLogs"))
            else:
                return "No?"
        else:
            return redirect(url_for("backLogin"))


@app.route('/back/logs')
@login_required
def backLogs():
    if current_user.is_webmaster:
        logs: list = Logs.query.all()

        return render_template("logs.html", logs=logs)
    else:
        return "Nope"
