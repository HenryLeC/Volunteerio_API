import API, os
from API import app, db
from API.database import User

# CLI command to make DB
@app.cli.command("StartDB")
def makeDB():
    db.drop_all()
    db.create_all()

    u1 = User("U1", "12345","User, User 1","1111111", student=True)
    u2 = User("U2", "12345","User, User 2","2222222", admin=True)
    u3 = User("U3", "12345","User, User 3","3333333", community=True)

    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)
    db.session.commit()


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port="80")
