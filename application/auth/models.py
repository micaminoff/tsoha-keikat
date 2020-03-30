from application import db
from application.models import Base


class User(Base):

    __tablename__ = "account"

    # Email = username. Uniqueness is enforced in auth/views.py
    email = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean(), unique=False, default=False)

    # One-To-Many relationship, each event has a creator
    events = db.relationship("Event", backref='account', lazy=True)

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
