from NYEIS_Site.forms import IntakeForm, AddressForm, ContactForm, UserForm
from flask import render_template, url_for, flash, redirect
from NYEIS_Site import app
from NYEIS_Site.models import Person, Contact, Address, User
from random import randint
import datetime
from NYEIS_Site import db
from NYEIS_Site import logger

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
    children = Person.query.all()
    return render_template('home.html', children=children, title='Children List')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register/child", methods=['GET', 'POST'])
def register_child():
    intakeForm = IntakeForm()
    contactForm = ContactForm()
    addressForm = AddressForm()

    if intakeForm.validate_on_submit() and contactForm.validate_on_submit() and addressForm.validate_on_submit():
        child_num = return_ref()
        person = Person(
            child_ref=str(child_num),
            child_firstname=intakeForm.child_firstname.data,
            child_middlename=intakeForm.child_middlename.data,
            child_lastname=intakeForm.child_lastname.data,
            child_dob=intakeForm.child_dob.data,
            father_name=intakeForm.father_name.data,
            father_dob=intakeForm.father_dob.data,
            mother_name=intakeForm.mother_name.data,
            mother_dob=intakeForm.mother_dob.data,
            created_on=datetime.datetime.utcnow(),
            status='Saved'
        )
        address = Address(
            address_line1=addressForm.address_line1.data,
            address_line2=addressForm.address_line2.data,
            address_city=addressForm.address_city.data,
            address_state=addressForm.address_state.data,
            address_zip=addressForm.address_zip.data,
            created_on=datetime.datetime.utcnow()
        )
        contact = Contact(
            ph_areacode=contactForm.ph_areacode.data,
            ph_phonenumber=contactForm.ph_phonenumber.data,
            email_addr=contactForm.email_addr.data,
            created_on=datetime.datetime.utcnow()
        )
        person.addresses.append(address)
        person.contact.append(contact)
        db.session.add(person)
        db.session.commit()
        logger.info(f'The child ref number is {child_num}')
        flash("Information submitted successfully", 'success')
        return redirect(url_for('success', id=person.id))

    return render_template('register_child.html', intakef=intakeForm, contf=contactForm, addrf=addressForm,
                           title='Registration Form')


@app.route("/success/<string:id>")
def success(id):
    person = Person.query.get(id)
    return render_template('register_success.html', first_name=person.child_firstname,
                           middle_name=person.child_middlename,
                           last_name=person.child_lastname, ref_no=person.child_ref,
                           regis_date=person.created_on.date(),
                           title='Confirmation')


@app.route("/details/<string:id>")
def child_details(id):
    logger.info(f'getting child details for {id}')
    child = Person.query.get(id)
    return render_template('child_details.html', child=child,
                           address=child.addresses[0],
                           contact=child.contact[0],
                           title='Details')


@app.route("/child/submit/<string:id>")
def child_submit_approval(id):
    logger.info(f'getting child details for {id}')
    child = Person.query.get(id)
    child.status = 'SUBMIT'
    db.session.add(child)
    db.session.commit()

    ####

    #  ADD CODE TO START AWS

    ####

    return redirect(url_for('success',id=id))


@app.route("/register_user", methods=['GET', 'POST'])
def register_user():
    user_form = UserForm()
    if user_form.validate_on_submit():
        flash("Information submitted successfully", "success")
    return render_template('register_user.html', user_form=user_form, title='')


def return_ref():
    return randint(1234, 999999)
