import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import INET, JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class AuditLog(Base):
    """Immutable audit trail — Phase 9.

    category: 'security' | 'workflow' | 'system'
    severity: 'info' | 'warning' | 'error' | 'critical'
    """

    __tablename__ = "audit_log"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    event_type: Mapped[str] = mapped_column(String(60), nullable=False)
    category: Mapped[str] = mapped_column(
        String(20), nullable=False, server_default="system"
    )
    severity: Mapped[str] = mapped_column(
        String(10), nullable=False, server_default="info"
    )
    user_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
    )
    actor_email: Mapped[str | None] = mapped_column(String(255))
    target_type: Mapped[str | None] = mapped_column(String(50))
    target_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True))
    description: Mapped[str | None] = mapped_column(Text)
    ip_address: Mapped[str | None] = mapped_column(INET)
    user_agent: Mapped[str | None] = mapped_column(Text)
    metadata_: Mapped[dict] = mapped_column(
        "metadata_", JSONB, default=dict, server_default="{}"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    # Relationships
    user: Mapped["User | None"] = relationship()


class DataLoadHistory(Base):
    __tablename__ = "data_load_history"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    bundle_type: Mapped[str] = mapped_column(String(50), nullable=False)
    bundle_file: Mapped[str | None] = mapped_column(String(100))
    framework_code: Mapped[str | None] = mapped_column(String(50))
    version: Mapped[str | None] = mapped_column(String(50))
    objects_loaded: Mapped[int | None] = mapped_column(Integer, server_default="0")
    relationships_loaded: Mapped[int | None] = mapped_column(
        Integer, server_default="0"
    )
    bundle_hash: Mapped[str | None] = mapped_column(String(64))
    # CHECK (load_status IN ('pending', 'running', 'success', 'failed'))
    load_status: Mapped[str] = mapped_column(
        String(20), nullable=False, server_default="pending"
    )
    load_started: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    load_completed: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    error_message: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
