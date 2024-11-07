from typing import List
from sqlalchemy import Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from models.entities.base import Base, intpk, created_at


class Contract(Base):
    __tablename__ = 'contracts'

    id: Mapped[intpk]
    total_amount: Mapped[float] = mapped_column(Numeric(10, 2))
    remaining_amount: Mapped[float] = mapped_column(Numeric(10, 2))
    signed: Mapped[bool] = mapped_column(default=False)
    creation_date: Mapped[created_at]

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
