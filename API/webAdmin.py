from API import webapp, app, db
from flask_login import (login_user, login_required, LoginManager,
                         logout_user, current_user)
from werkzeug.security import check_password_hash
from flask import request, redirect, render_template, url_for
from API.database import User, Logs
import traceback

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@webapp.route('/', methods=["GET"])
def webappIndex():
    return render_template('index.html')


@webapp.route('/privacy-policy')
def privacyPolicy():
    return render_template("PrivacyPolicy.html")


@webapp.route("/logout")
@login_required
def webappLogout():
    logout_user()
    return redirect(url_for("webapp.webappLogin"))


@webapp.route("/login", methods=["GET", "POST"])
def webappLogin():
    if request.method == "GET":
        return render_template("login.html")
    else:
        Uname = request.form.get("uname")
        Pass = request.form.get("pass")

        user = User.query.filter_by(username=Uname).first()

        if check_password_hash(user.password, Pass):
            login_user(user, remember=True)
            if user.is_webmaster:
                return redirect(url_for("webapp.webappLogs"))
            elif user.is_admin:
                return redirect(url_for("webapp.webappAddUsers"))
        else:
            return redirect(url_for("webapp.webappLogin"))


@webapp.route('/logs')
@login_required
def webappLogs():
    if current_user.is_webmaster:
        logs: list = Logs.query.all()

        return render_template("logs.html", logs=logs)
    else:
        return redirect(url_for("webapp.webappAddUsers"))


@webapp.route('/addUsers', methods=["GET"])
@login_required
def webappAddUsers():
    if current_user.is_admin:
        return render_template("addUsers.html")
    elif current_user.is_webmaster:
        return redirect(url_for("webapp.webappLogs"))


@webapp.route('/addUsers', methods=["POST"])
@login_required
def addUsers():
    try:
        try:
            usr = current_user
            usr: User
            usersC = int(request.form["users"])
        except Exception:
            return "", 500

        for i in range(usersC):
            us = User(
                request.form["user" + str(i) + "UN"],
                request.form["user" + str(i) + "P"],
                request.form["user" + str(i) + "N"],
                request.form["user" + str(i) + "I"],
                usr.District,
                usr.School,
                student=True
            )
            db.session.add(us)

        db.session.commit()

        return redirect(url_for("webapp.webappAddUsers"))
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500
