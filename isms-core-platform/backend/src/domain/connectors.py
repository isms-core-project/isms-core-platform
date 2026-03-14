"""SQLAlchemy models for v2.0 connector evidence ingestion."""

import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, Integer, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.domain.control_groups import ControlGroup

from src.database.base import Base, TimestampMixin


class Connector(TimestampMixin, Base):
    __tablename__ = "connectors"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    source_system: Mapped[str] = mapped_column(String(50), nullable=False)  # entra_id, defender, panw …
    api_token_hash: Mapped[str | None] = mapped_column(String(255), nullable=True)
    last_run: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    last_item_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="active")
    config_encrypted: Mapped[str | None] = mapped_column(Text, nullable=True)  # Fernet-encrypted JSON
    sync_requested_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    last_error: Mapped[str | None] = mapped_column(Text, nullable=True)
    last_error_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    retention_days: Mapped[int | None] = mapped_column(Integer, nullable=True)  # None = use global default (90d)

    evidence: Mapped[list["ConnectorEvidence"]] = relationship(
        "ConnectorEvidence", back_populates="connector", cascade="all, delete-orphan"
    )


class ConnectorEvidence(Base):
    __tablename__ = "connector_evidence"
    __table_args__ = (
        UniqueConstraint("connector_id", "source_ref", name="uq_connector_evidence_ref"),
        Index("ix_connector_evidence_control_group", "control_group_id"),
        Index("ix_connector_evidence_connector", "connector_id"),
        Index("ix_connector_evidence_event_date", "event_date"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    connector_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("connectors.id", ondelete="CASCADE"), nullable=False
    )
    control_group_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("control_groups.id", ondelete="CASCADE"), nullable=False
    )
    source_ref: Mapped[str | None] = mapped_column(String(200), nullable=True)
    source_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    classification: Mapped[str | None] = mapped_column(String(50), nullable=True)  # incident, change, asset …
    status: Mapped[str | None] = mapped_column(String(50), nullable=True)
    event_date: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    raw: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )
    archived_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    connector: Mapped["Connector"] = relationship("Connector", back_populates="evidence")
    control_group: Mapped["ControlGroup"] = relationship("ControlGroup", lazy="select")
