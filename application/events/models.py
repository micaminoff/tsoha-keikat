from application import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144))
    date = db.Column(db.Date,
                     default=db.func.current_timestamp(),
                     nullable=False)
    venue = db.Column(db.String(144), nullable=False)
    performer = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name=None, date=None, venue=None, performer=None):
        self.name = name
        self.date = date
        self.venue = venue
        self.performer = performer
