from API import db
from API.database import User, District, School


def makeDB():
    db.drop_all()
    db.create_all()

    d = District("Miami Dade County")
    s = School("Highland Oaks Middle", 20)

    u1 = User("U1", "12345", "User, User 1", "1111111", d,
              s, student=True)
    u2 = User("U2", "12345", "User, User 2", "2222222", d,
              s, admin=True)
    u3 = User("U3", "12345", "User, User 3", "3333333", d,
              s, community=True, email="henry@volunteerio.us")
    u4 = User("U4", "12345", "User, User 4", "4444444", None,
              None,  webmaster=True)

    db.session.add(d)
    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)
    db.session.add(u4)
    db.session.commit()


if __name__ == "__main__":
    makeDB()
