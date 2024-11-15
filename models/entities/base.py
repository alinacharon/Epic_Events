from datetime import datetime, timezone
from typing import Annotated

from sqlalchemy import DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

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
str_20 = Annotated[str, mapped_column(String(20))]
str_100 = Annotated[str, mapped_column(String(100))]
str_120 = Annotated[str, mapped_column(String(120))]
str_255 = Annotated[str, mapped_column(String(255))]


class Base(DeclarativeBase):
    id: Mapped[intpk]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

