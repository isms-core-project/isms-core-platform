from datetime import datetime
from sqlalchemy import DateTime, Enum as _SAEnum, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


def SAEnum(enum_cls, **kw):
    """SAEnum wrapper that maps Python enum values (not names) to PostgreSQL."""
    kw.setdefault("values_callable", lambda e: [m.value for m in e])
    return _SAEnum(enum_cls, **kw)


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )
