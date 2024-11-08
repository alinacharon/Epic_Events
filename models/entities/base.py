from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy import DateTime, String
from datetime import datetime, timezone
from typing import Annotated

intpk = Annotated[int, mapped_column(primary_key=True, index=True)]
created_at = Annotated[
    datetime,
    mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )
]
updated_at = Annotated[
    datetime,
    mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )
]
str_20 = Annotated [str, mapped_column(String(20))]
str_100 = Annotated[str, mapped_column(String(100))]
str_120 = Annotated[str, mapped_column(String(120))]
str_255 = Annotated[str, mapped_column(String(255))]


class Base(DeclarativeBase):

    id: Mapped[intpk]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    @classmethod
    def get_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    def save(self, session):
        session.add(self)
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
