import API, os, secrets
from API import app, db
from API.database import User

app.config["DEBUG"] = True
app.config["SECRET_KEY"] = secrets.token_urlsafe(32)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')

@app.cli.command("StartDB")
def makeDB():
    db.drop_all()
    db.create_all()

    u1 = User("U1", "12345", student=True)
    u2 = User("U2", "12345", admin=True)
    u3 = User("U3", "12345", community=True)

    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)
    db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
