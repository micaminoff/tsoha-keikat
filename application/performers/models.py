from application import db
from application.models import Base, event_performer_rel_table

from sqlalchemy.sql import text


class Performer(Base):

    name = db.Column(db.String(144), nullable=False)
    genre = db.Column(db.String(144))

    account_id = db.Column(db.Integer,
                           db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name=None, genre=None):
        self.name = name
        self.genre = genre

    @staticmethod
    def find_events(perf=0):
        stmt = text("SELECT e.name, e.date, e.venue, e.account_id FROM Event e"
                    " INNER JOIN event_performer_rel_table rel ON (e.id = rel.event_id)"
                    " INNER JOIN Performer p ON (rel.performer_id = :perf)"
                    " WHERE p.id = :perf").params(perf=perf)
        res = db.engine.execute(stmt)
        return [{"name": row[0], "date": row[1], "venue": row[2], "account": row[3]} for row in res]

    @staticmethod
    def count_events(perf=0):
        stmt = text("SELECT COUNT (*) FROM Event e"
                    " INNER JOIN event_performer_rel_table rel ON (e.id = rel.event_id)"
                    " INNER JOIN Performer p ON (rel.performer_id = :perf)"
                    " WHERE p.id = :perf").params(perf=perf)
        res = db.engine.execute(stmt).fetchone()
        return res[0]
