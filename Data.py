import json
from API import db
from API.database import (
    School,
    User, Opportunity,
    InCompleteOppMessages,
    NewUnconfHoursMessages
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
ladm = None
comms = []
adms = []
stus = []
futureApp = []
past = []
# endregion

# School
s = School("Waterside Public School", 20)
db.session.add(s)

# Create Students
# region
for stuName in NAMES[:94]:
    stuId = str(lastSId).zfill(8)
    lastSId += 1
    stu = User(
        stuName, "password", stuName,
        stuId, s, student=True
    )
    db.session.add(stu)
    stus.append(stu)
# Login Student
stuId = str(lastSId).zfill(8)
lastSId += 1
stu = User(
    "Student", "password", "Daniel",
    stuId, s, student=True
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
        comId, s, community=True
    )
    db.session.add(comm)
    comms.append(comm)
# Login Community
comId = str(lastCId).zfill(8)
lastCId += 1
comm = User(
    "Community", "password", "Michael",
    comId, s, community=True
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
        comId, s, admin=True
    )
    db.session.add(adm)
    adms.append(adm)
# Login Adm
admId = str(lastAId).zfill(8)
lastAId += 1
adm = User(
    "Admin", "password", "Harry",
    admId, s, admin=True
)
db.session.add(adm)
adms.append(adm)
ladm = adm
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
    "Beach Cleanup", "Suny Isles Beach", date, 6,
    "Environment", 40, usr, "Come and help clean up sunny isles beach.", True
)
db.session.add(opp)
futureApp.append(opp)

# Opp 3
date = now()
date = date.replace(hour=17, minute=0)
date += datetime.timedelta(days=2)
usr = ladm
opp = Opportunity(
    "Football Game", "American Heritage", date, 3,
    "School", 10, usr, "Come help setup for the football game",
    True
)
db.session.add(opp)
futureApp.append(opp)

# Opp 4
date = now()
date = date.replace(hour=7, minute=0)
date += datetime.timedelta(days=7)
usr = comms[2]
opp = Opportunity(
    "Help Register Voters", "Voter Station", date, 9,
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
    "Humane Society", "Miami-Dade Humane Society", date, 3,
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
    "Beach Cleanup", "Suny Isles Beach", date, 5,
    "Environment", 40, usr, "Come and help clean up sunny isles beach.", True
)
db.session.add(opp)
past.append(opp)

# Opp 3
date = now()
date = date.replace(hour=17, minute=0)
date -= datetime.timedelta(days=2)
usr = ladm
opp = Opportunity(
    "Football Game", "American Heritage", date, 4,
    "School", 10, usr, "Come help setup for the football game",
    True
)
db.session.add(opp)
past.append(opp)

# Opp 4
date = now()
date = date.replace(hour=8, minute=0)
date -= datetime.timedelta(days=7)
usr = comms[3]
opp = Opportunity(
    "Help Register Voters", "Voter Station", date, 9,
    "Civic", 40, usr, "Help get more voters registered for the upcoming elections", True
)
db.session.add(opp)
past.append(opp)

db.session.commit()
# endregion

# Book Students
# region
stusr = stus[:]
random.shuffle(stusr)
for opp in futureApp:
    for stu in range(random.randint(round(opp.MaxVols / 2), opp.MaxVols)):
        stu = stusr.pop()
        stu.BookedOpps.append(opp)
db.session.commit()
# endregion

# region Past Students
stusr = stus[:]
random.shuffle(stusr)
for opp in past:
    for i in range(random.randint(round(opp.MaxVols / 2), opp.MaxVols)):
        stu = stusr.pop()
        complete = random.randint(1, 4)
        if complete == 2:
            msg = InCompleteOppMessages(random.randint(
                1, opp.Hours - 1), random.randint(1, 59))
            db.session.add(msg)
            opp.InCompleteOppMessages.append(msg)
            stu.InCompleteOppMessages.append(msg)
            cOpps = pickle.loads(stu.CurrentOpps)
            cOpps.append({"ID": str(opp.id)})
            stu.CurrentOpps = pickle.dumps(cOpps)
            db.session.add(stu)
            db.session.add(opp)
        else:
            stu.PastOpps.append(opp)
            for i in stu.Past:
                if i.opp == opp:
                    pastD = i
                    break
            pastD.hours = opp.Hours
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
msg = NewUnconfHoursMessages()
db.session.add(msg)
stud.UnconfHoursMessages.append(msg)

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
