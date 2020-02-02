from flask import Flask
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__)
db = SQLAlchemy(api)

api.config.from_pyfile("config.py")

api.run()

import API.routes
import API.database