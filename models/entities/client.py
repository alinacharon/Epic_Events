from datetime import datetime

import sqlalchemy as db

metadata = db.MetaData()


class Client:
    def __init__(self, full_name, email, phone, company_name, commercial_contact, id=None):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.company_name = company_name
        self.commercial_contact = commercial_contact
        self.creation_date = datetime.now().strftime("%d/%m/%Y, %H:%M") 
        self.last_updated = datetime.now().strftime("%d/%m/%Y, %H:%M")  

    def validate(self):
        required_fields = ["full_name", "email", "phone", "company_name", "commercial_contact"]
        for field in required_fields:
            if getattr(self, field) is None or getattr(self, field).strip() == "":
                raise ValueError(f"Le champ '{field}' est requis.")


clients = db.Table('clients', metadata,
                   db.Column('id', db.Integer, primary_key=True),
                   db.Column('full_name', db.String(length=255), nullable=False),
                   db.Column('email', db.String(length=255), nullable=False, unique=True),
                   db.Column('phone', db.String(length=50), nullable=True),
                   db.Column('company_name', db.String(length=255), nullable=True),
                   db.Column('creation_date', db.DateTime, default=datetime),
                   db.Column('last_updated', db.DateTime, default=datetime, onupdate=datetime),
                   db.Column('commercial_contact', db.String(length=255), nullable=True),
                   db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable=True)
                   )
