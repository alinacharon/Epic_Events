from typing import Optional
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from sqlalchemy.types import DateTime
from models.entities.base import Base, intpk, str_255

class Event(Base):
    __tablename__ = 'events' 
    
    id: Mapped[intpk]
    start_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    location: Mapped[str_255] = mapped_column(nullable=False)
    num_attendees: Mapped[int]
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    contract_id: Mapped[int] = mapped_column(ForeignKey("contracts.id"))
    contract: Mapped["Contract"] = relationship("Contract", back_populates="events")

    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    client: Mapped["Client"] = relationship("Client", back_populates="events")

    support_contact_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    support_contact: Mapped["User"] = relationship(
        "User",
        back_populates="supported_events",
        foreign_keys=[support_contact_id]
    )

    def __repr__(self) -> str:
        return (
            f"Event(id={self.id!r}, "
            f"contract_id={self.contract_id!r}, "
            f"client_id={self.client_id!r}, "
            f"support_contact_id={self.support_contact_id!r}, "
            f"start_date={self.start_date!r}, "
            f"end_date={self.end_date!r}, "
            f"location={self.location!r}, "
            f"num_attendees={self.num_attendees!r})"
        )
