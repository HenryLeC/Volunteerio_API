from API.database import User, School, Opportunity, Booked, Past
from API import db

schId = int(input("Enter School ID: "))
sch = School.query.get(schId)
us = User.query.filter(User.School == sch).all()
opps = Opportunity.query.join(User).filter(User.School == sch).all()
books = Booked.query.join(User).filter(User.School == sch).all()
pasts = Past.query.join(User).filter(User.School == sch).all()

for book in books:
    db.session.delete(book)
    db.session.commit()

for book in pasts:
    db.session.delete(book)
    db.session.commit()

for opp in opps:
    opp: Opportunity
    db.session.delete(opp)
    db.session.commit()

for u in us:
    u: User
    u.InCompleteOppMessages = []
    u.BookedOpps = []
    u.Opportunities = []
    u.School = None
    u.UnconfHoursMessages = []
    u.PastOpps = []
    db.session.delete(u)

db.session.delete(sch)
db.session.commit()
