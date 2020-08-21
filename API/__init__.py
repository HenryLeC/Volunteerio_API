from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from PrefixMiddleware import PrefixMiddleware
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['SECRET_KEY'] = "9yp0IPC62yB6AScoJ8APFOaYEO6vIDy_MvL7p3SRQ-Q"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://volunteerio:studio@postgres:5432/volunteerio?client_encoding=utf8'
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import API.studentRoutes
import API.adminRoutes
import API.commonRoutes
import API.database
import API.webAdmin
