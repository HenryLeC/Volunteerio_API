from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import secrets
import logging

logging.basicConfig(filename='example.log')

app = Flask(__name__)
# Set path for DB
dbpathl = os.path.join(os.path.abspath(os.path.dirname(__file__))).split("\\")
dbpath = ""
for sect in dbpathl[:-1]:
    dbpath += sect + "\\"

# Set Flask Config
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = secrets.token_urlsafe(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbpath + '\\app.db'

db = SQLAlchemy(app)

import API.studentRoutes
import API.adminRoutes
import API.commonRoutes
import API.database
