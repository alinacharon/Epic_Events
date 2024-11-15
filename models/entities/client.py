from typing import List, Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.entities.base import Base, str_100, str_120, str_20


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
