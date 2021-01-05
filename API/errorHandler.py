from API.database import Logs
import traceback
from API import app, db


@app.errorhandler(Exception)
def serverErrorHandler(e: Exception):
    db.session.add(Logs(traceback.format_exc()))
    db.session.commit()
    return "Your error has been reported", 500
