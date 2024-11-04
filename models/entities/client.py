from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import validates, relationship

from database import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    phone = Column(String(20))
    company_name = Column(String(100))
    creation_date = Column(DateTime, default=datetime)
    last_update = Column(DateTime, default=datetime, onupdate=datetime)

    commercial_id = Column(Integer, ForeignKey('users.id'))
    commercial = relationship("User", back_populates="clients")

    def __repr__(self):
        return f"<Client {self.full_name}>"

    @validates('full_name')
    def validate_full_name(self, key, value):
        if not value or value.strip() == "":
            raise ValueError("Full name is required.")
        return value

    @validates('email')
    def validate_email(self, key, value):
        if not value or '@' not in value:
            raise ValueError("Valid email is required.")
        return value

    @validates('phone')
    def validate_phone(self, key, value):
        if value and not value.replace('+', '').isdigit():
            raise ValueError("Phone number should contain only digits and '+'.")
        return value
