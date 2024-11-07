import re
from typing import List, Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from models.entities.base import Base, intpk, str_100, str_120, str_20


class Client(Base):
    __tablename__ = 'clients' 
    
    full_name: Mapped[str_100] = mapped_column(nullable=False)
    email: Mapped[str_120] = mapped_column(unique=True, nullable=False)
    phone: Mapped[Optional[str_20]] 
    company_name: Mapped[Optional[str_100]] = mapped_column(nullable=True)

    commercial_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    commercial: Mapped["User"] = relationship("User", back_populates="clients")

    contracts: Mapped[List["Contract"]] = relationship(
        "Contract",
        back_populates="client",
        cascade="all, delete-orphan"
    )

    events: Mapped[List["Event"]] = relationship(
        "Event",
        back_populates="client",
        cascade="all, delete-orphan"
    )

    @validates('full_name', 'email', 'phone')
    def validate_fields(self, key, value):
        if key == 'full_name':
            if not value or not value.strip():
                raise ValueError("Full name is required.")
            return value.strip()
        elif key == 'email':
            if not value or not re.match(r"[^@]+@[^@]+\.[^@]+", value):
                raise ValueError("Valid email is required.")
            return value.lower()
        elif key == 'phone':
            if value:
                value = value.strip()
                if not value.replace('+', '').isdigit():
                    raise ValueError("Phone number should contain only digits and '+'.")
            return value
