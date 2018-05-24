from datetime import datetime
from app import db

class Account_token(db.Document):
    ldap_token = db.StringField(required=True)
    ldap_token_expiry = db.StringField(max_length=50)
