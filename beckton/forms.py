from beckton import app
from flask_wtf import Form
from ukpostcodeutils import validation
from wtforms import BooleanField, TextField, RadioField, validators, ValidationError

class Commitment(Form):
    name = TextField('Full name', [validators.Required(message="You need to enter your name"), validators.Length(max=100)])
    mobile_number = TextField('Mobile number', [validators.Regexp('(07[\d]{8,12}|447[\d]|\+447[\d]{7,11})', message="You need to enter a valid mobile phone number")])
    postcode = TextField('Postcode', [validators.Required(message="You need to enter a valid postcode")])
    rate = RadioField('What hours do you work?', [validators.Required(message="You need to enter what hours you work")], choices=app.config['CONDITION_RATES'])
    agree = BooleanField(app.config['CONDITION_TERMS'], [validators.InputRequired(message="You need to agree")])

    def validate_postcode(form, field):

        #is it a postcode?
        if not validation.is_valid_postcode(field.data.replace(' ', '').upper()):
            raise ValidationError('You need to enter a valid postcode')

        #is it in the an allowed postcode?
        if not app.config['CONDITION_POSTCODE_AREAS'] == []:
            in_bounds = False

            for postcode_area in app.config['CONDITION_POSTCODE_AREAS']:
                if field.data.lower().startswith(postcode_area.lower()):
                  in_bounds = True

            if not in_bounds:
                postcode_areas_formatted = ', '.join(app.config['CONDITION_POSTCODE_AREAS'])
                raise ValidationError('You can currently only sign up if your postcode starts with %s' % postcode_areas_formatted)

