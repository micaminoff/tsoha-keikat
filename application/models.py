from application import db


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


event_performer_rel_table = db.Table('event_performer_rel_table',
                                     db.Column('performer_id',
                                               db.Integer,
                                               db.ForeignKey('performer.id'),
                                               primary_key=True),
                                     db.Column('event_id',
                                               db.Integer, db.ForeignKey(
                                                   'event.id'),
                                               primary_key=True),
                                     )
