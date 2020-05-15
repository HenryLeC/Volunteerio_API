from API import db
from API.database import User, District, School


def makeDB():
    db.drop_all()
    db.create_all()

    d = District("Miami Dade County")
    s = School("Highland Oaks Middle")

    u1 = User("U1", "12345", "User, User 1", "1111111", d,
              s, "lecompteh18@gmail.com", student=True)
    u2 = User("U2", "12345", "User, User 2", "2222222", d,
              s, "2222222@volunteerio.us", admin=True)
    u3 = User("U3", "12345", "User, User 3", "3333333", d,
              s, "3333333@volunteerio.us", community=True)
    u4 = User("U4", "12345", "User, User 4", "4444444", None,
              None, "4444444@volunteerio.us", webmaster=True)

    db.session.add(d)
    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)
    db.session.add(u4)
    db.session.commit()


if __name__ == "__main__":
    makeDB()
