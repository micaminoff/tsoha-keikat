from flask_wtf import FlaskForm
from wtforms import DateField, FieldList, FormField, SelectField, StringField, validators


class PerformerEntryForm(FlaskForm):
    performer = SelectField(u'Performer')


class EventForm(FlaskForm):
    name = StringField("Event name")
    performers = FieldList(FormField(PerformerEntryForm), min_entries=1)
    # performer = SelectField(u'Performer', coerce=int)
    venue = StringField('Venue', [validators.DataRequired()])
    date = DateField('Date', [validators.DataRequired()])

    class Meta:
        csrf = False
