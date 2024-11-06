import enum
from typing import List
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from models.entities.base import Base


class Role(enum.Enum):
    
    MANAGEMENT = 'MANAGEMENT'
    COMMERCIAL = 'COMMERCIAL'
    SUPPORT = 'SUPPORT'


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(255))
    role: Mapped[Role] = mapped_column(Enum(Role))

    # Опциональные отношения
    clients: Mapped[List["Client"]] = relationship(
        "Client",
        back_populates="commercial",
        foreign_keys="[Client.commercial_id]"
    )
    
    supported_events: Mapped[List["Event"]] = relationship(
        "Event",
        back_populates="support_contact",
        foreign_keys="[Event.support_contact_id]"
    )

    managed_contracts: Mapped[List["Contract"]] = relationship(
        "Contract",
        back_populates="commercial",
        foreign_keys="[Contract.commercial_id]"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r})"