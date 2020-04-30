from application import db
from application.models import Base

from sqlalchemy.sql import text


class User(Base):

    __tablename__ = "account"

    # Email = username. Uniqueness is enforced in auth/views.py
    email = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean(), unique=False, default=False)

    # One-To-Many relationship, each event has a creator
    events = db.relationship("Event", backref='account', lazy=True)
    performers = db.relationship("Performer", backref='account', lazy=True)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def count_users_events(user=0):
        stmt = text("SELECT COUNT(*) FROM Event e"
                    " WHERE e.account_id = :usr").params(usr=user)
        res = db.engine.execute(stmt).fetchone()
        return res[0]
