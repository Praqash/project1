from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username')

    password = PasswordField('Password')

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username')

    password = PasswordField('Password')

    submit = SubmitField('Login')
