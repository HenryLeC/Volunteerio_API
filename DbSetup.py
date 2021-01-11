from API import db
from API.database import School, User


def makeDB():
    db.drop_all()
    db.create_all()

    s = School("Highland Oaks Middle", 20)

    u1 = User("U1", "12345", "User, User 1", "1111111",
              s, student=True)
    u2 = User("U2", "12345", "User, User 2", "2222222",
              s, admin=True)
    u3 = User("U3", "12345", "User, User 3", "3333333",
              s, community=True, email="info@volunteerio.us")
    u4 = User("U4", "12345", "User, User 4", "4444444",
              s, teacher=True)
    u5 = User("U5", "12345", "User, User 5", "5555555",
              None, webmaster=True)

    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)
    db.session.add(u4)
    db.session.add(u5)
    db.session.commit()


if __name__ == "__main__":
    makeDB()
