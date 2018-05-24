from datetime import datetime
from app import db

class Account(db.Document):
    owner_email = db.StringField(required=True)
    owner_firstname = db.StringField(max_length=50)
    owner_lastname = db.StringField(max_length=50)
    account_state = db.StringField(max_length=50)
