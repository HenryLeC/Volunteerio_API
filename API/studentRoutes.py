from flask import request, jsonify, send_file
from API import app, db
from API.database import (User, Opportunity, NewUnconfHoursMessages, Logs,
                          InCompleteOppMessages)
from API.auth import token_required
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, SimpleDocTemplate, TableStyle, Image
from reportlab.platypus import Paragraph, Spacer
import pickle
import datetime
import jwt
import traceback
import io


@app.route("/hours", methods=["POST"])
@token_required
def getHours(user: User):
    try:
        schoolGoal = user.School.hoursGoal
        districtGoal = user.District.hoursGoal
        goal = 0
        if schoolGoal is not None:
            goal = schoolGoal
        elif districtGoal is not None:
            goal = districtGoal

        return jsonify({'hours': str(user.hours), 'goal': goal})
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/addhours', methods=["POST"])
@token_required
def add_hours(user: User):
    try:
        # Check for hours and reason in request
        try:
            hours = request.form["hours"]
            reason = request.form["reason"]
            desc = request.form["desc"]
        except KeyError:
            return jsonify({'msg': 'Hours and reason is required.'}), 500
        id = user.HoursId

        # Increment HoursId by 1
        user.HoursId += 1

        # Add Hours to Unconfirmed List
        UnConfHrs = pickle.loads(user.unconfHours)
        # Add hous and reason to unconfirmed list
        UnConfHrs.append({
            'id': id,
            'hours': int(hours),
            'desc': desc,
            'reason': reason
        })

        # Add To DB
        user.unconfHours = pickle.dumps(UnConfHrs)
        if len(user.UnconfHoursMessages) == 0:
            Message = NewUnconfHoursMessages()
            user.UnconfHoursMessages.append(Message)
            db.session.add(Message)
        db.session.add(user)
        db.session.commit()

        return jsonify({
            'msg': 'Hours added',
            'unconfHours': pickle.loads(user.unconfHours),
            'confHours': pickle.loads(user.confHours)
        })
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/Opps', methods=["Post"])
@token_required
def list_opps(user: User):
    try:
        try:
            dateFilter = request.form["filterDate"]
            nameFilter = "%{}%".format(request.form["filterName"])
        except KeyError:
            return jsonify({'msg': "Please Supply all Paramaters"}), 500

        dateFilter = datetime.datetime.strptime(
            dateFilter, "%Y-%m-%dT%H:%M:%S"
        )

        Opps = Opportunity.query\
            .join(User).filter(
                User.District == user.District,
                Opportunity.Time > dateFilter,
                Opportunity.Name.like(nameFilter)
            ).order_by(
                Opportunity.Time.asc()
            ).all()
        CleanOpps = []
        for opp in Opps:
            if user not in opp.BookedStudents:
                CleanOpps.append({
                    "ID": str(opp.id),
                    "Name": opp.Name,
                    "Location": opp.Location,
                    "Hours": opp.Hours,
                    "Time": opp.getTime(),
                    "Sponsor": User.query.get(int(opp.SponsorID)).name,
                    "Class": opp.Class,
                    "CurrentVols": len(opp.BookedStudents),
                    "MaxVols": opp.MaxVols
                })
        return jsonify(CleanOpps)
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/OppInfo', methods=["POST"])
@token_required
def oppInfo(user: User):
    try:
        try:
            id = request.form["ID"]
        except KeyError:
            return jsonify({'msg': "Please Supply all Paramaters"}), 500

        opp = Opportunity.query.get(int(id))
        return jsonify({
            "Location": opp.Location,
            "Description": opp.Description
        })
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/ClockInOut', methods=["POST"])
@token_required
def Clock(user: User):
    try:
        try:
            Code = request.form["QrCode"]
        except KeyError:
            return jsonify({
                'msg': 'Please Pass in The Correct Parameters'
            }), 500
        try:
            OppId = jwt.decode(Code, app.config['SECRET_KEY'],
                               algorithm="HS256")["ID"]
            Opp = Opportunity.query.get(OppId)
        except(Exception):
            return jsonify({
                'header': "Error",
                'msg': "Please scan an opportunity code."
            })
        res = False
        RightDict = None
        for Dict in pickle.loads(user.CurrentOpps):
            try:
                if Dict["ID"] == str(OppId):
                    res = True
                    RightDict = Dict
                    break
            except KeyError:
                pass

        if res:
            td = datetime.datetime.utcnow() - RightDict["StartTime"]
            Hours = float(td.seconds / 3600)

            if Hours <= 0.15 * Opp.Hours:
                message = {
                    'header': "Scanner",
                    'msg': "You have not completed enough of the opportunity, please either continue the opportunity or you will not get any hours."
                }
                pass
            elif Hours < 0.8 * Opp.Hours:
                hours, remainder = divmod(td.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                OppMessage = InCompleteOppMessages(hours, minutes)
                db.session.add(OppMessage)

                user.InCompleteOppMessages.append(OppMessage)
                Opp.InCompleteOppMessages.append(OppMessage)

                message = {
                    'header': "Scanned",
                    'msg': "You have only completed part of the opportunty, the sponsor will either give you partial credit or no credit."
                }
            elif Hours >= 0.8 * Opp.Hours:
                user.hours += Opp.Hours

                user.PastOpps.append(Opp)
                CurrentOpps = pickle.loads(user.CurrentOpps)
                CurrentOpps.remove(RightDict)
                user.CurrentOpps = pickle.dumps(CurrentOpps)

                message = {
                    'header': "Scanned",
                    'msg': 'Thank You, Your Hours were added.'
                }

            db.session.add(user)
            db.session.add(Opp)
            db.session.commit()

            return jsonify(message)

        else:
            if Opp:
                CurrentOpps = pickle.loads(user.CurrentOpps)
                CurrentOpps.append({
                    'StartTime': datetime.datetime.utcnow(),
                    'ID': str(OppId)
                })
                user.CurrentOpps = pickle.dumps(CurrentOpps)

                db.session.add(user)
                db.session.commit()

                return jsonify({
                    'header': "Scanned",
                    'msg': "Thank you for clocking in, don't forget to clock out later"
                })
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/BookAnOpp', methods=["POST"])
@token_required
def BookAnOpp(user):
    try:
        try:
            Id = request.form["OppId"]
        except KeyError:
            return jsonify({
                'msg': 'Please Pass in The Correct Parameters'
            }), 500
        Opp = Opportunity.query.get(Id)

        user.BookedOpps.append(Opp)
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'msg': 'Opportunity Booked.'
        })
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/BookedOpps', methods=["Post"])
@token_required
def BookedOpps(user):
    try:
        Opps = user.BookedOpps
        CleanOpps = []
        for opp in Opps:
            CleanOpps.append({
                "Name": opp.Name,
                "Hours": opp.Hours,
                "Time": opp.Time.strftime("%m/%d/%Y, %H:%M")
            })
        return jsonify(CleanOpps)
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/PastOpps', methods=["Post"])
@token_required
def PastOpps(user):
    try:
        PastOpps = user.PastOpps
        PastOppsClean = []
        for opp in PastOpps:
            PastOppsClean.append({
                "Name": opp.Name,
                "Hours": opp.Hours,
                "Time": opp.Time.strftime("%m/%d/%Y, %H:%M")
            })
        confHours = pickle.loads(user.confHours)
        HoursClean = []
        for opp in confHours:
            HoursClean.append({
                "Hours": opp["hours"],
                "Reason": opp["reason"],
                "Confirmed": "Confirmed"
            })
        unconfHours = pickle.loads(user.unconfHours)
        for opp in unconfHours:
            HoursClean.append({
                "Hours": opp["hours"],
                "Reason": opp["reason"],
                "Confirmed": "Unconfirmed"
            })

        FullClean = {
            "PastOpps": PastOppsClean,
            "Hours": HoursClean,
        }
        return jsonify(FullClean)
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/GenerateDoc', methods=["POST"])
@token_required
def GenerateDoc(user: User):
    try:
        buffer = io.BytesIO()

        # Make Doc
        p = SimpleDocTemplate(buffer, pagesize=letter)
        elems = []

        # Make Image
        im = Image("Logo.png", 6.5 * inch, 1.04 * inch)
        elems.append(im)

        # Add Student Name
        nm = Paragraph("Student Name: " + user.name)
        elems.append(nm)

        # Add Space
        elems.append(Spacer(0, 1 * inch))

        # Add Paragraph
        elems.append(Paragraph("Total Volunteer Hours: " + str(user.hours)))

        # Add Space
        elems.append(Spacer(0, 1 * inch))

        # Make Table
        data = [
            ["Name", "Date", "Hours*", "Sponsor"]
        ]

        opps = user.PastOpps
        ConfHours = pickle.loads(user.confHours)

        for opp in opps:
            data.append([opp.Name, opp.Time, opp.Hours, opp.Sponsor.name])
        for hour in ConfHours:
            data.append([hour["reason"], "NA", str(hour["hours"]), "NA"])

        t = Table(data)
        styles = TableStyle([
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.Color(0.4, 0.4, 0.6)),
            ('LINENBELOW', (0, 0), (-1, 0), 2, colors.Color(0.4, 0.4, 0.6)),
            ('FONTSIZE', (0, 0), (-1, 0), 14),

            ('ALIGN', (0, 0), (-1, 0), "CENTER"),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),

            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
            ('FONTSIZE', (0, 1), (0, -1), 12),

            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ])

        t.setStyle(styles)
        elems.append(t)

        # Add Space
        elems.append(Spacer(0, 1 * inch))

        # Add Paragraph
        elems.append(Paragraph("* Hours may be incorrect on sponsored opportunities"))

        # Save amd build PDF to buffer
        p.build(elems)

        # Seek on Buffer
        buffer.seek(0)

        return send_file(
            buffer,
            as_attachment=True,
            mimetype="application/pdf",
            attachment_filename="ExportedOpps.pdf"
        )
    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500


@app.route('/Leaderboard', methods=["POST"])
@token_required
def Leaderboard(user):
    try:
        try:
            filt = request.form["filter"]
        except KeyError:
            return jsonify({
                'msg': 'Please Pass in The Correct Parameters'
            }), 500

        if filt == "school":
            users = User.query.filter_by(District=user.District, is_student=True).with_entities(User.name, User.hours).order_by(User.hours.desc()).limit(50).all()
        elif filt == "district":
            users = User.query.filter_by(School=user.School, is_student=True).with_entities(User.name, User.hours).order_by(User.hours.desc()).limit(50).all()

        usersReturn = []
        for i, user in enumerate(users):
            usersReturn.append({
                "name": user.name,
                "hours": user.hours,
                "rank": i + 1
            })

        return jsonify(usersReturn)

    except Exception:
        db.session.add(Logs(traceback.format_exc()))
        db.session.commit()
        return "", 500
