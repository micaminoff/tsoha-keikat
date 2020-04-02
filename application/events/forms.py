from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, SelectMultipleField, StringField, validators


class EventForm(FlaskForm):
    name = StringField("Event name")
    #performer = SelectField(u'Performer', coerce=int)
    performer = SelectMultipleField(u'Performer', coerce=int)
    venue = StringField('Venue', [validators.DataRequired()])
    date = DateField('Date', [validators.DataRequired()])

    class Meta:
        csrf = False
