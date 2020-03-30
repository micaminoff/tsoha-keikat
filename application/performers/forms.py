from flask_wtf import FlaskForm
from wtforms import StringField, validators


class PerformerForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired()])
    genre = StringField("Genre")

    class Meta:
        csrf = False
