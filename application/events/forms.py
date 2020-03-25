from flask_wtf import FlaskForm
from wtforms import StringField, DateField


class EventForm(FlaskForm):
    name = StringField("Event name")
    performer = StringField('Performer')
    venue = StringField('Venue')
    date = DateField('Date')

    class Meta:
        csrf = False
