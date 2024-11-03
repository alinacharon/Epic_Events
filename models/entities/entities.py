from datetime import datetime
import sqlalchemy as db

metadata = db.MetaData()

class Contract:
    def __init__(self, 
                 id: int, 
                 client: str, 
                 commercial_contact: str, 
                 total_amount: float, 
                 amount_remaining: float, 
                 creation_date: datetime, 
                 is_signed: bool):
        self.id = id
        self.client = client
        self.commercial_contact = commercial_contact
        self.total_amount = total_amount
        self.amount_remaining = amount_remaining
        self.creation_date = creation_date
        self.is_signed = is_signed


class Event:
    def __init__(self,                
                 id: int, 
                 contract: Contract, 
                 clientName: str, 
                 clientContact: str, 
                 startDate: datetime, 
                 endDate: datetime, 
                 supportContact: str, 
                 location: str, 
                 numAttendees: int, 
                 notes: str):
        self.id = id
        self.contract = contract
        self.clientName = clientName
        self.clientContact = clientContact
        self.startDate = startDate
        self.endDate = endDate
        self.supportContact = supportContact
        self.location = location
        self.numAttendees = numAttendees
        self.notes = notes


class User:
    def __init__(self, 
                 id: int, 
                 name: str, 
                 email: str, 
                 department: str, 
                 role: str):
        self.id = id
        self.name = name
        self.email = email
        self.department = department
        self.role = role
        



# Таблица контрактов
contracts = db.Table('contracts', metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('client_id', db.Integer, db.ForeignKey('clients.id'), nullable=False),  # Внешний ключ на клиента
    db.Column('commercial_contact', db.String(length=255), nullable=True),
    db.Column('total_amount', db.Float, nullable=False),
    db.Column('amount_remaining', db.Float, nullable=False),
    db.Column('creation_date', db.DateTime, default=datetime),
    db.Column('is_signed', db.Boolean, default=False),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable=True)  # Внешний ключ на пользователя
)

# Таблица событий
events = db.Table('events', metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('contract_id', db.Integer, db.ForeignKey('contracts.id'), nullable=False),  # Внешний ключ на контракт
    db.Column('client_name', db.String(length=255), nullable=False),
    db.Column('client_contact', db.String(length=255), nullable=False),
    db.Column('start_date', db.DateTime, nullable=False),
    db.Column('end_date', db.DateTime, nullable=False),
    db.Column('support_contact', db.String(length=255), nullable=True),
    db.Column('location', db.String(length=255), nullable=False),
    db.Column('num_attendees', db.Integer, nullable=False),
    db.Column('notes', db.Text, nullable=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable=True)  # Внешний ключ на пользователя
)

# Таблица пользователей
users = db.Table('users', metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('name', db.String(length=255), nullable=False),
    db.Column('email', db.String(length=255), nullable=False, unique=True),
    db.Column('department', db.String(length=255), nullable=True),
    db.Column('role', db.String(length=255), nullable=False)
)