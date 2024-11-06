from datetime import datetime
import enum
import re
from typing import List, Optional
from sqlalchemy import Numeric, String, ForeignKey, Float, Boolean, Integer, Text, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from sqlalchemy.types import DateTime

from models.entities.base import Base, str_100, str_120, str_255


class Contract(Base):
    __tablename__ = 'contracts'

    id: Mapped[int] = mapped_column(primary_key=True)
    total_amount: Mapped[float] = mapped_column(Numeric(10, 2))
    remaining_amount: Mapped[float] = mapped_column(Numeric(10, 2))
    signed: Mapped[bool] = mapped_column(default=False)
    creation_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Внешние ключи
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    commercial_id: Mapped[int] = mapped_column(ForeignKey("users.id"))  

    # Отношения
    client: Mapped["Client"] = relationship(back_populates="contracts")
    commercial: Mapped["User"] = relationship(
        back_populates="managed_contracts",
        foreign_keys=[commercial_id]
    )
    events: Mapped[List["Event"]] = relationship(back_populates="contract")


    def __repr__(self) -> str:
        return (
            f"Contract(id={self.id!r}, "
            f"client_id={self.client_id!r}, "
            f"commercial_contact_id={self.commercial_contact_id!r}, "
            f"total_amount={self.total_amount!r}, "
            f"amount_remaining={self.amount_remaining!r}, "
            f"is_signed={self.is_signed!r})"
        )
