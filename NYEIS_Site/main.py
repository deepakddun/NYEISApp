import datetime

from flask import Flask, render_template, url_for
from forms import IntakeForm, AddressForm, ContactForm
import uuid

app = Flask(__name__)
app.secret_key = '543af292a648479e77c6b86b13b95179209f77c13bee75ff916d4f888418b09b'

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://demo_user:Password123@@localhost:3306/sample_db'
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.String(30), primary_key=True, autoincrement=False, default=uuid.uuid4)
    child_ref = db.Column(db.String(20), nullable=False)
    child_firstname = db.Column(db.String(50), nullable=False)
    child_middlename = db.Column(db.String(50), nullable=False)
    child_lastname = db.Column(db.String(50), nullable=False)
    child_dob = db.Column(db.Date(), nullable=False)
    father_name = db.Column(db.String(100))
    father_dob = db.Column(db.String(100))
    mother_name = db.Column(db.String(100))
    mother_dob = db.Column(db.String(100))
    created_on = db.Column(db.DateTime())
    updated_on = db.Column(db.DateTime(), default=datetime.datetime)
    addresses = db.relationship('Address', backref='person', lazy=True)
    contact = db.relationship('Contact', backref='person', lazy=True)


class Address(db.Model):
    id = db.Column(db.String(30), primary_key=True, autoincrement=False, default=uuid.uuid4)
    address_line1 = db.Column(db.String(120), nullable=False)
    address_line2 = db.Column(db.String(120), nullable=False)
    address_city = db.Column(db.String(120), nullable=False)
    address_state = db.Column(db.String(120), nullable=False)
    address_zip = db.Column(db.String(120), nullable=False)
    created_on = db.Column(db.DateTime())
    updated_on = db.Column(db.DateTime(), default=datetime.datetime)
    person_id = db.Column(db.String(30), db.ForeignKey('person.id'), nullable=False)


class Contact(db.Model):
    id = db.Column(db.String(30), primary_key=True, autoincrement=False, default=uuid.uuid4)
    ph_areacode = db.Column(db.Integer)
    ph_phonenumber = db.Column(db.Integer)
    email_addr = db.Column(db.String(50))
    person_id = db.Column(db.String(30), db.ForeignKey('person.id'), nullable=False)


children = [
    {
        'ref_no': 12345,
        'first': 'Alpha',
        'last': 'Pandey',
        'address': '10 Main Road, Texas, US',
        'dob': '15 April 2022'
    },
    {
        'ref_no': 64789,
        'first': 'Beta',
        'last': 'Pandey',
        'address': '10 Second Road, Texas, US',
        'dob': '10 April 2022'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', children=children, title='Children List')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    intakeForm = IntakeForm()
    contactForm = ContactForm()
    addressForm = AddressForm()
    if intakeForm.validate_on_submit() and contactForm.validate_on_submit() and addressForm.validate_on_submit():
        pass

    return render_template('register.html', intakef=intakeForm, contf=contactForm, addrf=addressForm,
                           title='Registration Form')


if __name__ == '__main__':
    app.run(debug=True)
