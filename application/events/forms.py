from flask_wtf import FlaskForm
from wtforms import DateField, FieldList, FormField, SelectField, StringField, validators


class PerformerEntryForm(FlaskForm):
    performer = SelectField('Performer', coerce=int)

    class Meta:
        csrf = False


class EventForm(FlaskForm):
    name = StringField("Event name")
    performers = FieldList(FormField(PerformerEntryForm), min_entries=1,
                           max_entries=10)
    # performer = SelectField(u'Performer', coerce=int)
    venue = StringField('Venue', [validators.DataRequired()])
    date = DateField('Date', [validators.DataRequired()])

    class Meta:
        csrf = False
