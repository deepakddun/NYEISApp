import datetime

from flask_wtf import FlaskForm
from wtforms.fields import StringField, DateField, EmailField, SelectField, SubmitField
from datetime import date
from wtforms.validators import DataRequired, Length, Email, ValidationError

STATES_TUPLE = [("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"), ("AR", "Arkansas"), ("CA", "California"),
                ("CO", "Colorado"),
                ("CT", "Connecticut"), ("DC", "Washington DC"), ("DE", "Delaware"), ("FL", "Florida"),
                ("GA", "Georgia"),
                ("HI", "Hawaii"), ("ID", "Idaho"), ("IL", "Illinois"), ("IN", "Indiana"), ("IA", "Iowa"),
                ("KS", "Kansas"), ("KY", "Kentucky"),
                ("LA", "Louisiana"), ("ME", "Maine"), ("MD", "Maryland"), ("MA", "Massachusetts"), ("MI", "Michigan"),
                ("MN", "Minnesota"),
                ("MS", "Mississippi"), ("MO", "Missouri"), ("MT", "Montana"), ("NE", "Nebraska"), ("NV", "Nevada"),
                ("NH", "New Hampshire"),
                ("NJ", "New Jersey"), ("NM", "New Mexico"), ("NY", "New York"), ("NC", "North Carolina"),
                ("ND", "North Dakota"), ("OH", "Ohio"),
                ("OK", "Oklahoma"), ("OR", "Oregon"), ("PA", "Pennsylvania"), ("RI", "Rhode Island"),
                ("SC", "South Carolina"), ("SD", "South Dakota"),
                ("TN", "Tennessee"), ("TX", "Texas"), ("UT", "Utah"), ("VT", "Vermont"), ("VA", "Virginia"),
                ("WA", "Washington"), ("WV", "West Virginia"),
                ("WI", "Wisconsin"), ("WY", "Wyoming")]


def type_check(form, field):
    val: str = field.data
    if not val.isdigit():
        raise ValidationError('Can contain only numbers')


def date_check(form, field):
    val:date  = field.data
    if val > date.today():
        raise ValidationError("Date cannot be greater than today's date")


class IntakeForm(FlaskForm):
    child_firstname = StringField("Child First Name", validators=[DataRequired()])
    child_middlename = StringField("Child Middle Name", validators=[DataRequired()])
    child_lastname = StringField("Child Last Name", validators=[DataRequired()])
    child_dob = DateField("Date Of Birth", validators=[DataRequired() , date_check], default=date.today)
    father_name = StringField("Father Name")
    father_dob = DateField("Father's Date Of Birth", default=date.today ,validators=[date_check])
    mother_name = StringField("Mother Name")
    mother_dob = DateField("Mother's Date Of Birth", default=date.today , validators=[date_check])
    save_form = SubmitField('Save')


class ContactForm(FlaskForm):
    ph_areacode = StringField('Area Code', validators=[type_check, Length(min=1, max=3)])
    ph_phonenumber = StringField('PhoneNumber', validators=[type_check, Length(min=7, max=7)])
    email_addr = EmailField('Email Address', validators=[Email()])


class AddressForm(FlaskForm):
    address_line1 = StringField('Address Line 1', validators=[DataRequired(), Length(min=1, max=3)])
    address_line2 = StringField('Address Line 2', validators=[Length(min=1, max=3)])
    address_city = StringField('City', validators=[DataRequired(), Length(min=1, max=3)])
    address_state = SelectField('State', choices=STATES_TUPLE, validators=[DataRequired()])
    address_zip = StringField('Zip', validators=[type_check, Length(max=5)])
