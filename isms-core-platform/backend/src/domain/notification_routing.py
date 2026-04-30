from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, func
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class NotificationRouting(Base):
    __tablename__ = "notification_routing"

    event_type: Mapped[str] = mapped_column(String(100), primary_key=True)
    target_roles: Mapped[list[str]] = mapped_column(ARRAY(String(50)), nullable=False)
    always_include_override: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
