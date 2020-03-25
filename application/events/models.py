from application import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144))
    date = db.Column(db.Date,
                     default=db.func.current_timestamp(),
                     nullable=False)
    venue = db.Column(db.String(144), nullable=False)
    performer = db.Column(db.String(144), nullable=False)

    def __init__(self, name=None, date=None, venue=None, performer=None):
        self.name = name
        self.date = date
        self.venue = venue
        self.performer = performer
