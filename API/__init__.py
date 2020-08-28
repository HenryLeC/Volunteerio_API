from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from PrefixMiddleware import PrefixMiddleware
from flask_cors import CORS
from flask_migrate import Migrate
from API.Secrets import SecretKey, DatabaseURI, SECURITY_PASSWORD_SALT

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Set Flask Config
app.config['SECRET_KEY'] = SecretKey
app.config['SQLALCHEMY_DATABASE_URI'] = DatabaseURI
app.config['SECURITY_PASSWORD_SALT'] = SECURITY_PASSWORD_SALT
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import API.studentRoutes
import API.adminRoutes
import API.commonRoutes
import API.database
import API.webAdmin
