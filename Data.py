import json
from API import db
from API.database import (
    District, School,
    User, Opportunity
)
import datetime
import random

# Helper Vars
# region
NAMES = json.load(open("SmallNames.json", "r"))  # 100 Names
lastSId = 00000000
lastCId = 10000000
lastAId = 20000000
comms = []
adms = []
stus = []
futureApp = []
past = []
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
    stus.append(stu)
# Login Student
stuId = str(lastSId).zfill(8)
lastSId += 1
stu = User(
    "Student", "password", "Daniel",
    stuId, d, s, student=True
)
db.session.add(stu)
stus.append(stu)
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
    comms.append(comm)
# Login Community
comId = str(lastCId).zfill(8)
lastCId += 1
comm = User(
    "Community", "password", "Michael",
    comId, d, None, community=True
)
db.session.add(comm)
comms.append(comm)
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
    adms.append(adm)
# Login Community
admId = str(lastAId).zfill(8)
lastAId += 1
comm = User(
    "Admin", "password", "Harry",
    admId, d, None, admin=True
)
db.session.add(adm)
adms.append(adm)
db.session.commit()
# endregion

# Create Future Opportunities
# region

now = datetime.datetime.now

# Opp 1
date = now()
date = date.replace(hour=18, minute=30)
date += datetime.timedelta(days=5)
opp = Opportunity(
    "Humane Society", "Miami-Dade Humane Society", date, 2,
    "Animals", 20, comms[0], "Come to the Humane Society and help feed and care for the animals",
    False
)
db.session.add(opp)

# Opp 2
date = now()
date = date.replace(hour=8, minute=30)
date += datetime.timedelta(days=20)
opp = Opportunity(
    "Beach Cleanup", "Suny Isles Beach", date, 4,
    "Environment", 40, comms[1], "Come and help clean up sunny isles beach.", True
)
db.session.add(opp)
futureApp.append(opp)

# Opp 3
date = now()
date = date.replace(hour=17, minute=0)
date += datetime.timedelta(days=2)
opp = Opportunity(
    "Football Game", "American Heritage", date, 2,
    "School", 10, adms[0], "Come help setup for the football game",
    True
)
db.session.add(opp)
futureApp.append(opp)

# Opp 4
date = now()
date = date.replace(hour=18, minute=0)
date += datetime.timedelta(days=7)
opp = Opportunity(
    "Help Register Voters", "Voter Station", date, 4,
    "Civic", 40, comms[2], "Help get more voters registered for the upcoming elections", True
)
db.session.add(opp)
futureApp.append(opp)

db.session.commit()
# endregion

# Create Past Opportunities
# region

now = datetime.datetime.now

# Opp 1
date = now()
date = date.replace(hour=18, minute=30)
date -= datetime.timedelta(days=5)
opp = Opportunity(
    "Humane Society", "Miami-Dade Humane Society", date, 2,
    "Animals", 20, comms[0], "Come to the Humane Society and help feed and care for the animals",
    True
)
db.session.add(opp)
past.append(opp)

# Opp 2
date = now()
date = date.replace(hour=8, minute=30)
date -= datetime.timedelta(days=20)
opp = Opportunity(
    "Beach Cleanup", "Suny Isles Beach", date, 4,
    "Environment", 40, comms[1], "Come and help clean up sunny isles beach.", True
)
db.session.add(opp)
past.append(opp)

# Opp 3
date = now()
date = date.replace(hour=17, minute=0)
date -= datetime.timedelta(days=2)
opp = Opportunity(
    "Football Game", "American Heritage", date, 2,
    "School", 10, adms[0], "Come help setup for the football game",
    True
)
db.session.add(opp)
past.append(opp)

# Opp 4
date = now()
date = date.replace(hour=18, minute=0)
date -= datetime.timedelta(days=7)
opp = Opportunity(
    "Help Register Voters", "Voter Station", date, 4,
    "Civic", 40, comms[2], "Help get more voters registered for the upcoming elections", True
)
db.session.add(opp)
past.append(opp)

db.session.commit()
# endregion

# Book Students
# region
for opp in futureApp:
    for stu in random.choices(stus, k=random.randint(opp.MaxVols // 2, opp.MaxVols)):
        stu.BookedOpps.append(opp)
db.session.commit()
# endregion

# Past Students
# region

# endregion
