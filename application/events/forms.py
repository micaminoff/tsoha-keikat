from flask_wtf import FlaskForm
from wtforms import StringField, DateField, validators


class EventForm(FlaskForm):
    name = StringField("Event name")
    performer = StringField('Performer', [validators.Length(min=2)])
    venue = StringField('Venue', [validators.DataRequired()])
    date = DateField('Date', [validators.DataRequired()])

    class Meta:
        csrf = False
