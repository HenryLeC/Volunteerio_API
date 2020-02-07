from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

import API.studentRoutes
import API.adminRoutes
import API.commRoutes
import API.database