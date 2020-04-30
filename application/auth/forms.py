from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, validators


class LoginForm(FlaskForm):
    email = StringField(
        "Email", [validators.Email(), validators.DataRequired(), validators.Length(max=144)])
    password = PasswordField("Password", [validators.DataRequired()])
    admin = BooleanField("Admin")

    class Meta:
        csrf = False
