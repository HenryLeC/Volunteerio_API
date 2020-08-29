import json
from API import db
from API.database import (
    District, School,
    User, Opportunity,
    InCompleteOppMessages
)
import datetime
import random
import pickle

# Helper Vars
# region
NAMES = json.load(open("SmallNames.json", "r"))  # 100 Names
lastSId = 00000000
lastCId = 10000000
lastAId = 20000000
stud = None
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
stud = stu
db.session.commit()
# endregion

# Create 4 Community Members
# region
for cName in NAMES[94:97]:
    comId = str(lastCId).zfill(8)
    lastCId += 1
    comm = User(
        cName, "password", cName,
        comId, d, s, community=True
    )
    db.session.add(comm)
    comms.append(comm)
# Login Community
comId = str(lastCId).zfill(8)
lastCId += 1
comm = User(
    "Community", "password", "Michael",
    comId, d, s, community=True
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
        comId, d, s, admin=True
    )
    db.session.add(adm)
    adms.append(adm)
# Login Adm
admId = str(lastAId).zfill(8)
lastAId += 1
comm = User(
    "Admin", "password", "Harry",
    admId, d, s, admin=True
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
usr = comms[0]
opp = Opportunity(
    "Humane Society", "Miami-Dade Humane Society", date, 2,
    "Animals", 20, usr, "Come to the Humane Society and help feed and care for the animals",
    False
)
db.session.add(opp)

# Opp 2
date = now()
date = date.replace(hour=8, minute=30)
date += datetime.timedelta(days=20)
usr = comms[3]
opp = Opportunity(
    "Beach Cleanup", "Suny Isles Beach", date, 4,
    "Environment", 40, usr, "Come and help clean up sunny isles beach.", True
)
db.session.add(opp)
futureApp.append(opp)

# Opp 3
date = now()
date = date.replace(hour=17, minute=0)
date += datetime.timedelta(days=2)
usr = adms[0]
opp = Opportunity(
    "Football Game", "American Heritage", date, 2,
    "School", 10, usr, "Come help setup for the football game",
    True
)
db.session.add(opp)
futureApp.append(opp)

# Opp 4
date = now()
date = date.replace(hour=18, minute=0)
date += datetime.timedelta(days=7)
usr = comms[2]
opp = Opportunity(
    "Help Register Voters", "Voter Station", date, 4,
    "Civic", 40, usr, "Help get more voters registered for the upcoming elections", True
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
usr = comms[0]
opp = Opportunity(
    "Humane Society", "Miami-Dade Humane Society", date, 2,
    "Animals", 20, usr, "Come to the Humane Society and help feed and care for the animals",
    True
)
db.session.add(opp)
past.append(opp)

# Opp 2
date = now()
date = date.replace(hour=8, minute=30)
date -= datetime.timedelta(days=20)
usr = comms[1]
opp = Opportunity(
    "Beach Cleanup", "Suny Isles Beach", date, 4,
    "Environment", 40, usr, "Come and help clean up sunny isles beach.", True
)
db.session.add(opp)
past.append(opp)

# Opp 3
date = now()
date = date.replace(hour=17, minute=0)
date -= datetime.timedelta(days=2)
usr = adms[3]
opp = Opportunity(
    "Football Game", "American Heritage", date, 2,
    "School", 10, usr, "Come help setup for the football game",
    True
)
db.session.add(opp)
past.append(opp)

# Opp 4
date = now()
date = date.replace(hour=18, minute=0)
date -= datetime.timedelta(days=7)
usr = comms[3]
opp = Opportunity(
    "Help Register Voters", "Voter Station", date, 4,
    "Civic", 40, usr, "Help get more voters registered for the upcoming elections", True
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

# region Past Students
for opp in past:
    for stu in random.choices(stus, k=random.randint(opp.MaxVols // 2, opp.MaxVols)):
        complete = random.randint(1, 10)
        if complete == 5:
            msg = InCompleteOppMessages(random.randint(1, opp.Hours - 1), random.randint(1, 59))
            opp.InCompleteOppMessages.append(msg)
            stu.InCompleteOppMessages.append(msg)
            db.session.add(msg)
            db.session.add(stu)
            db.session.add(opp)
        else:
            stu.PastOpps.append(opp)
            stu.hours += opp.Hours
db.session.commit()
# endregion

# region Hours on Student
id = stud.HoursId
stud.HoursId += 1
unconfs = pickle.loads(stud.unconfHours)
unconfs.append({
    'id': id,
    'hours': 10,
    'reason': "Camp Counselor",
    'desc': "I worked as a camp counselor for a few days."
})
stud.unconfHours = pickle.dumps(unconfs)

id = stud.HoursId
stud.HoursId += 1
confs = pickle.loads(stud.confHours)
confs.append({
    'id': id,
    'hours': 5,
    'reason': "Beach Cleanup",
    'desc': "I helped clean Miami-Beach on Sunday"
})
stud.confHours = pickle.dumps(confs)
stud.hours += 5

db.session.add(stud)
db.session.commit()
# endregion
