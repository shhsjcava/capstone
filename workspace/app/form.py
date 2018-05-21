from wtforms import StringField, PasswordField, validators
from flask_wtf import FlaskForm


class MyForm(FlaskForm):
   username = StringField('Username')

