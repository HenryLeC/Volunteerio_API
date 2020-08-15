from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)
api = Blueprint('api', __name__)
webapp = Blueprint('webapp', __name__, static_folder='static', static_url_path='/webapp/static')
CORS(app, supports_credentials=True)

# Set path for DB
dbpathl = os.path.join(os.path.abspath(os.path.dirname(__file__))).split("\\")
dbpath = ""
for sect in dbpathl[:-1]:
    dbpath += sect + "\\"

# Set Flask Config
app.config['SECRET_KEY'] = "VerySecret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbpath + '\\app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import API.studentRoutes
import API.adminRoutes
import API.commonRoutes
import API.database
import API.webAdmin

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(webapp)
