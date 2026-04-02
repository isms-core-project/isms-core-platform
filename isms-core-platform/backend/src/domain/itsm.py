"""ITSM ticket domain model."""

import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class ItsmTicket(Base):
    __tablename__ = "itsm_tickets"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organisations.id", ondelete="CASCADE"), nullable=False)
    source_type: Mapped[str] = mapped_column(String(20), nullable=False)  # gap | remediation
    source_id: Mapped[uuid.UUID] = mapped_column(nullable=False)
    connector_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("connectors.id", ondelete="CASCADE"), nullable=False)
    external_ticket_id: Mapped[str] = mapped_column(String(200), nullable=False)
    external_url: Mapped[str | None] = mapped_column(String(1000))
    status: Mapped[str] = mapped_column(String(30), nullable=False, default="open")
    last_synced_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
