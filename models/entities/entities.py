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





