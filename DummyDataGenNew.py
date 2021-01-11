import datetime
import json
import pickle
import random

from API import db
from API.database import (InCompleteOppMessages, NewUnconfHoursMessages,
                          Opportunity, School, User)

NAMES = json.load(open("Names.json", "r"))
NAMES = random.choices(NAMES, k=110)
StuNAMES = NAMES[:100]
CommNAMES = NAMES[100:105]
AdmNAMES = NAMES[105:110]

user_data = {}
students = []
admins = []
cmembers = []
opps = []
oppsI = 0
lastSId = 00000000
lastAId = 10000000
lastCId = 20000000

# School
s = School("Waterside Public Schools", 20)
db.session.add(s)

# Student Gen
for name in StuNAMES:
    username = name + str(random.randint(0, 20))
    stuId = str(lastSId).zfill(8)
    lastSId += 1
    Stu = User(username, "password", name, stuId, s, student=True)
    students.append(Stu)
    db.session.add(Stu)
    user_data[name] = {
        "Uname": username,
        "role": "student"
    }

# Admin Gen
for name in AdmNAMES:
    username = name + str(random.randint(0, 20))
    admId = str(lastAId).zfill(8)
    lastAId += 1
    Adm = User(username, "password", name, admId, s,
               admin=True, email="test.email@volunteerio.us")
    db.session.add(Adm)
    admins.append(Adm)
    user_data[name] = {
        "Uname": username,
        "role": "admin"
    }


# Community Gen
for name in CommNAMES:
    username = name + str(random.randint(0, 20))
    comId = str(lastCId).zfill(8)
    lastCId += 1
    Adm = User(username, "password", name, comId, s, community=True)
    db.session.add(Adm)
    cmembers.append(Adm)
    user_data[name] = {
        "Uname": username,
        "role": "community"
    }

# Past Opportunities Gen
end_date = datetime.date.today() - datetime.timedelta(days=1)
start_date = end_date - datetime.timedelta(weeks=10)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

for usr in admins:
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    opp = Opportunity(f"Opp{oppsI + 1}", "School", random_date, random.randint(
        0, 5), "Environment", 20, usr, "Example Opportunity Description", True)
    oppsI += 1
    opps.append(opp)
    usr.Opportunities.append(opp)
    db.session.add(usr)
    db.session.add(opp)

for usr in cmembers:
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    opp = Opportunity(f"Opp{oppsI + 1}", "School", random_date, random.randint(
        1, 5), "Animals", 20, usr, "Example Opportunity Description", True)
    oppsI += 1
    usr.Opportunities.append(opp)
    db.session.add(usr)
    db.session.add(opp)
    opps.append(opp)

# IDs dont get gened until commit
db.session.commit()

# Make an Opp Past
for usr in students:
    bOpps = random.choices(opps, k=2)
    for opp in bOpps:
        inComp = random.randint(0, 10)
        if inComp == 3:
            msg = InCompleteOppMessages(random.randint(
                int(opp.Hours * 0.15), int(opp.Hours * 0.8)), random.randint(0, 59))
            db.session.add(msg)
            usr.InCompleteOppMessages.append(msg)
            opp.InCompleteOppMessages.append(msg)
            currentOpps = pickle.loads(usr.CurrentOpps)
            currentOpps.append({"ID": str(opp.id), "StartTime": opp.Time})
            usr.CurrentOpps = pickle.dumps(currentOpps)
            db.session.add(usr)
        else:
            usr.PastOpps.append(opp)
            usr.hours += opp.Hours
            db.session.add(usr)

# Future Opportunities Gen
start_date = datetime.date.today() + datetime.timedelta(days=1)
end_date = start_date + datetime.timedelta(weeks=10)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

for usr in admins:
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    opp = Opportunity(f"Opp{oppsI + 1}", "School", random_date, random.randint(
        1, 5), "Environment", 20, usr, "Example Opportunity Description", True)
    oppsI += 1
    opps.append(opp)
    usr.Opportunities.append(opp)
    db.session.add(usr)
    db.session.add(opp)

for usr in cmembers:
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    verified = True
    if random.randint(0, 3) == 2:
        verified = False
    opp = Opportunity(f"Opp{oppsI + 1}", "School", random_date, random.randint(
        1, 5), "Animals", 20, usr, "Example Opportunity Description", verified)
    oppsI += 1
    if verified:
        opps.append(opp)
    usr.Opportunities.append(opp)
    db.session.add(usr)
    db.session.add(opp)

# Book Opp
for usr in students:
    bOpps = random.choices(opps, k=random.randint(1, 4))
    for opp in bOpps:
        usr.BookedOpps.append(opp)
        db.session.add(usr)

# Unconf and Conf Hours:
for user in students:
    id = user.HoursId
    user.HoursId += 1
    ConfHours = pickle.loads(user.confHours)
    hours = random.randint(1, 10)
    ConfHours.append({
        'id': id,
        'hours': hours,
        'reason': "Example Reason",
        "desc": "Example Description"
    })
    user.confHours = pickle.dumps(ConfHours)
    user.hours += hours

    db.session.add(user)

    if random.randint(0, 2) == 2:
        id = user.HoursId
        user.HoursId += 1
        UnConfHours = pickle.loads(user.unconfHours)
        UnConfHours.append({
            'id': id,
            'hours': random.randint(1, 10),
            'reason': "Example Reason",
            'desc': "Example Description"
        })
        user.unconfHours = pickle.dumps(UnConfHours)

        Message = NewUnconfHoursMessages()
        user.UnconfHoursMessages.append(Message)

        db.session.add(user)
        db.session.add(Message)

# Make a file with Usernames
with open("Users.json", "w") as f:
    json.dump(user_data, f)

# Commit To Database
db.session.commit()
