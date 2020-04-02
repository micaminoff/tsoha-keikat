from application import db
from application.models import Base, event_performer_rel_table


class Performer(Base):

    name = db.Column(db.String(144), nullable=False)
    genre = db.Column(db.String(144))

    account_id = db.Column(db.Integer,
                           db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name=None, genre=None):
        self.name = name
        self.genre = genre
