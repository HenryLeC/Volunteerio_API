from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from PrefixMiddleware import PrefixMiddleware
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Set path for DB
dbpathl = os.path.join(os.path.abspath(os.path.dirname(__file__))).split("\\")
dbpath = ""
for sect in dbpathl[:-1]:
    dbpath += sect + "\\"

# Set Flask Config
app.config['SECRET_KEY'] = "VerySecret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbpath + '\\app.db'
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import API.studentRoutes
import API.adminRoutes
import API.commonRoutes
import API.database
import API.webAdmin
