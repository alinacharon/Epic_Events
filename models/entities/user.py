import enum
from typing import List
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from models.entities.base import Base,intpk, str_100, str_120, str_255


class Role(enum.Enum):
    
    MANAGEMENT = 'MANAGEMENT'
    COMMERCIAL = 'COMMERCIAL'
    SUPPORT = 'SUPPORT'
    
   


class User(Base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    username: Mapped[str_100] = mapped_column(unique=True, index=True)
    email: Mapped[str_120] = mapped_column(unique=True, index=True)
    password: Mapped[str_255]
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
    @property
    def role_value(self) -> str:
        return self.role.value
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r},role={self.role!r}, )"