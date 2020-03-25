# Flask
from flask import Flask
app = Flask(__name__)

# DB
from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///events.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# Application
from application import views

from application.events import models
from application.events import views

from application.auth import models
from application.auth import views


db.create_all()
