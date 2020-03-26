from application import db


class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    # Email = username. Uniqueness is enforced in auth/views.py
    email = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

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
