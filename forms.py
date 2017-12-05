from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, BooleanField

from wtforms import validators, ValidationError
from wtforms.validators import DataRequired

class NewSpeakerForm(FlaskForm):
    name = TextField("Name",[validators.Required("Name required")])
    org = TextField("Organization",[validators.Required("Organization required")])
    email = TextField("Email",[validators.Required("Email required."), validators.Email("Email not valid")])
    submit = SubmitField("Add")

class CertForm(FlaskForm):
    submit = SubmitField("Generate")

class InviteForm(FlaskForm):
    submit = SubmitField("Generate")

class SendForm(FlaskForm):
    submit = SubmitField("Send email")
