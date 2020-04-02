# Flask
from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# DB
from flask_sqlalchemy import SQLAlchemy
import os

if os.environ.get('HEROKU'):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///events.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# Application
from application import views
from application import models

from application.events import models
from application.events import views

from application.performers import models
from application.performers import views

from application.auth import models
from application.auth import views

# Auth
from application.auth.models import User
app.config["SECRET_KEY"] = os.urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


try:
    #from application.performers.models import Performer
    #from application.auth.models import User
    db.create_all()
    '''u = User(email='super@admin.com', password='guest')
    u.admin = True
    db.session.add(u)
    p = Performer(name='Test performer', genre='Programming')
    p.account_id = u.id
    db.session().add(p)
    db.session().commit()'''
except:
    pass
