import json
import random
from API import db
from string import digits
from API.database import (User, Opportunity, Booked,
                          Past, District, NewUnconfHoursMessages,
                          School)
import datetime
import pickle

# Full names list
NAMES = json.load(open("Names.json", "r"))

user_data = {}
students = []
admins = []
cmembers = []
opps = []
oppsI = 0
lastSId = 00000000
lastAId = 10000000
lastCId = 20000000


# District
d = District("Waterside School District")
s = School("Waterside Public School")
db.session.add(d)


# Student Gen
stuNames = random.choices(NAMES, k=100)
for name in stuNames:
    username = name + str(random.randint(0, 20))
    stuId = str(lastSId).zfill(8)
    lastSId += 1
    Stu = User(username, "password", name, stuId, d, s, student=True)
    students.append(Stu)
    db.session.add(Stu)
    user_data[name] = {
        "Uname": username,
        "role": "student"
    }


# Admin Gen
adminNames = random.choices(NAMES, k=5)
for name in adminNames:
    username = name + str(random.randint(0, 20))
    admId = str(lastAId).zfill(8)
    lastAId += 1
    Adm = User(username, "password", name, admId, d, s, admin=True)
    db.session.add(Adm)
    admins.append(Adm)
    user_data[name] = {
        "Uname": username,
        "role": "admin"
    }


# Community Gen
communityNames = random.choices(NAMES, k=5)
for name in communityNames:
    username = name + str(random.randint(0, 20))
    comId = str(lastCId).zfill(8)
    lastCId += 1
    Adm = User(username, "password", name, comId, d, s, community=True)
    db.session.add(Adm)
    cmembers.append(Adm)
    user_data[name] = {
        "Uname": username,
        "role": "community"
    }


# Past Opportunities
end_date = datetime.date.today() - datetime.timedelta(days=1)
start_date = end_date - datetime.timedelta(weeks=10)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

for usr in admins:
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    opp = Opportunity(f"Opp{oppsI + 1}", "School", random_date, random.randint(0, 5), usr)
    oppsI += 1
    opps.append(opp)
    usr.Opportunities.append(opp)
    db.session.add(usr)
    db.session.add(opp)

for usr in cmembers:
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    opp = Opportunity(f"Opp{oppsI + 1}", "School", random_date, random.randint(1, 5), usr)
    oppsI += 1
    opps.append(opp)
    usr.Opportunities.append(opp)
    db.session.add(usr)
    db.session.add(opp)


# Make an Opp Past
for usr in students:
    bOpps = random.choices(opps, k=2)
    for opp in bOpps:
        usr.PastOpps.append(opp)
        usr.hours += opp.Hours
        db.session.add(usr)
        db.session.commit()

# Future Opportunities
start_date = datetime.date.today() + datetime.timedelta(days=1)
end_date = start_date + datetime.timedelta(weeks=10)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

for usr in admins:
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    opp = Opportunity(f"Opp{oppsI + 1}", "School", random_date, random.randint(1, 5), usr)
    oppsI += 1
    opps.append(opp)
    usr.Opportunities.append(opp)
    db.session.add(usr)
    db.session.add(opp)

for usr in cmembers:
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    opp = Opportunity(f"Opp{oppsI + 1}", "School", random_date, random.randint(1, 5), usr)
    oppsI += 1
    opps.append(opp)
    usr.Opportunities.append(opp)
    db.session.add(usr)
    db.session.add(opp)


# Booke Opp
for usr in students:
    bOpps = random.choices(opps, k=2)
    for opp in bOpps:
        usr.BookedOpps.append(opp)
        db.session.add(usr)
        db.session.commit()

# Unconf and Conf Hours:
for user in students:
    id = user.HoursId
    user.HoursId += 1
    ConfHours = pickle.loads(user.confHours)
    hours = random.randint(1, 10)
    ConfHours.append({
        'id': id,
        'hours': hours,
        'reason': "Example Reason"
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
            'reason': "Example Reason"
        })
        user.unconfHours = pickle.dumps(UnConfHours)

        Message = NewUnconfHoursMessages()
        user.UnconfHoursMessages.append(Message)

        db.session.add(user)
        db.session.add(Message)

# Make a file with Usernames
with open("Users.json", "w") as f:
    json.dump(user_data, f)

# Commit all users and opps
db.session.commit()
