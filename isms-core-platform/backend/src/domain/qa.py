import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.dialects.postgresql import ARRAY, JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base, SAEnum
from src.database.enums import CorrelationMethod, QAStatus


class CorrelationResult(Base):
    __tablename__ = "correlation_results"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    control_group_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("control_groups.id", ondelete="CASCADE"),
        nullable=False,
    )
    framework_control_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("framework_controls.id", ondelete="SET NULL"),
    )
    document_id: Mapped[str] = mapped_column(String(50), nullable=False)
    correlation_method: Mapped[CorrelationMethod] = mapped_column(
        SAEnum(CorrelationMethod, name="correlation_method", create_type=False),
        nullable=False,
    )
    # CHECK (correlation_strength >= 0.00 AND correlation_strength <= 1.00)
    correlation_strength: Mapped[Decimal] = mapped_column(
        Numeric(3, 2), nullable=False, server_default="0.00"
    )
    claimed_score: Mapped[Decimal | None] = mapped_column(Numeric(5, 2))
    verified_score: Mapped[Decimal | None] = mapped_column(Numeric(5, 2))
    qa_status: Mapped[QAStatus] = mapped_column(
        SAEnum(QAStatus, name="qa_status", create_type=False),
        nullable=False,
        server_default="needs_review",
    )
    coverage_keywords: Mapped[list | None] = mapped_column(
        ARRAY(String), server_default="{}"
    )
    missing_keywords: Mapped[list | None] = mapped_column(
        ARRAY(String), server_default="{}"
    )
    run_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    metadata_: Mapped[dict] = mapped_column(
        "metadata", JSONB, default=dict, server_default="{}"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    # Relationships
    control_group: Mapped["ControlGroup"] = relationship(
        back_populates="correlation_results"
    )
    framework_control: Mapped["FrameworkControl | None"] = relationship()


class SynonymRule(Base):
    """DB-backed synonym dictionary for keyword correlation.

    Each row maps one ISO keyword to a list of acceptable equivalents.
    Loaded at runtime by run_keyword_check() and merged with the
    hardcoded _SYNONYMS defaults (DB entry wins on conflict).
    """

    __tablename__ = "synonym_rules"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    keyword: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    synonyms: Mapped[list] = mapped_column(ARRAY(String), nullable=False, server_default="{}")
    notes: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )
