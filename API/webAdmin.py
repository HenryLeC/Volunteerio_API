from API import app
from flask_login import login_user, login_required, LoginManager, logout_user
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
    return redirect(url_for(back))


@app.route("/back/login", methods=["GET", "POST"])
def backLogin():
    if request.method == "GET":
        return render_template("login.html")
    else:
        Uname = request.form.get("uname")
        Pass = request.form.get("pass")

        user = User.query.filter_by(username=Uname, is_webmaster=True).first()

        if check_password_hash(user.password, Pass):
            login_user(user, remember=True)
            return redirect(url_for("back"))
        else:
            return redirect(url_for("backLogin"))


@app.route('/back')
@login_required
def back():
    logBreaks = ""
    
    logs: list = Logs.query.all()

    for log in logs:
        logBreaks += f"<p>{log.exc}<p>"

    return logBreaks
