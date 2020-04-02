from application import db
from application.models import Base, event_performer_rel_table


class Event(Base):

    name = db.Column(db.String(144))
    date = db.Column(db.Date,
                     default=db.func.current_timestamp(),
                     nullable=False)
    venue = db.Column(db.String(144), nullable=False)
    performers = db.relationship("Performer",
                                 secondary=event_performer_rel_table,
                                 lazy='subquery',
                                 backref=db.backref('events', lazy=True))

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name=None, date=None, venue=None, performers=None):
        self.name = name
        self.date = date
        self.venue = venue
        self.performers = performers
