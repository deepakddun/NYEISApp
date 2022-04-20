from datetime import datetime
import uuid
from NYEIS_Site import db


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
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow)
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
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow)
    person_id = db.Column(db.String(30), db.ForeignKey('person.id'), nullable=False)


class Contact(db.Model):
    id = db.Column(db.String(30), primary_key=True, autoincrement=False, default=uuid.uuid4)
    ph_areacode = db.Column(db.Integer)
    ph_phonenumber = db.Column(db.Integer)
    email_addr = db.Column(db.String(50))
    person_id = db.Column(db.String(30), db.ForeignKey('person.id'), nullable=False)
