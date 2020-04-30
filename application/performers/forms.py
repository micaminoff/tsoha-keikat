from flask_wtf import FlaskForm
from wtforms import StringField, validators


class PerformerForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired(), validators.Length(max=144)])
    genre = StringField("Genre", [validators.Length(max=144)])

    class Meta:
        csrf = False
