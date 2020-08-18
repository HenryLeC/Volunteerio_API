import json
from API import db
from API.database import (
    District, School,
    User
)

# Helper Vars
# region
NAMES = json.load(open("SmallNames.json", "r"))  # 100 Names
lastSId = 00000000
lastCId = 10000000
lastAId = 20000000
# endregion

# District / School
d = District("Waterside School District")
s = School("Waterside Public Schools", 20)
db.session.add(d)
db.session.add(s)

# Create Students
# region
for stuName in NAMES[:94]:
    stuId = str(lastSId).zfill(8)
    lastSId += 1
    stu = User(
        stuName, "password", stuName,
        stuId, d, s, student=True
    )
    db.session.add(stu)
# Login Student
stuId = str(lastSId).zfill(8)
lastSId += 1
stu = User(
    "Student", "password", "Daniel",
    stuId, d, s, student=True
)
db.session.add(stu)
db.session.commit()
# endregion

# Create 4 Community Members
# region
for cName in NAMES[94:97]:
    comId = str(lastCId).zfill(8)
    lastCId += 1
    comm = User(
        cName, "password", cName,
        comId, d, None, community=True
    )
    db.session.add(comm)
# Login Community
comId = str(lastCId).zfill(8)
lastCId += 1
comm = User(
    "Community", "password", "Michael",
    comId, d, None, community=True
)
db.session.add(comm)
db.session.commit()
# endregion

# Create 4 Admins
# region
for aName in NAMES[97:]:
    admId = str(lastAId).zfill(8)
    lastAId += 1
    adm = User(
        aName, "password", aName,
        comId, d, None, admin=True
    )
    db.session.add(adm)
# Login Community
admId = str(lastAId).zfill(8)
lastAId += 1
comm = User(
    "Admin", "password", "Harry",
    admId, d, None, admin=True
)
db.session.add(adm)
db.session.commit()
# endregion
