from flask_wtf import Form
from wtforms import BooleanField, TextField, validators, ValidationError

class Commitment(Form):
    name = TextField('Full name', [validators.Required(message="You need to enter your name"), validators.Length(max=100)])
    mobile_number = TextField('Mobile number', [validators.Regexp('(07[\d]{8,12}|447[\d]|\+447[\d]{7,11})', message="You need to enter a valid mobile phone number")])
    agree = BooleanField("Let's do it!", [validators.InputRequired(message="You need to agree")])