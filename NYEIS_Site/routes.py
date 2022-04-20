from NYEIS_Site.forms import IntakeForm,AddressForm,ContactForm
from flask import render_template, url_for , flash
from NYEIS_Site import app
from NYEIS_Site.models import Person,Contact,Address

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
        flash("Information submitted successfully" , 'success')

    return render_template('register.html', intakef=intakeForm, contf=contactForm, addrf=addressForm,
                           title='Registration Form')