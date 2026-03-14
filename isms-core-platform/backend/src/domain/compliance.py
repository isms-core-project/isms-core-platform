import uuid
from datetime import date

from sqlalchemy import Column, Date, ForeignKey, String, Table, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base, SAEnum, TimestampMixin
from src.database.enums import EvidenceStatus, EvidenceType, GapSeverity, GapStatus

# Junction table — Gap ↔ Evidence (many-to-many)
gap_evidence_table = Table(
    "gap_evidence",
    Base.metadata,
    Column("gap_id", UUID(as_uuid=True), ForeignKey("gaps.id", ondelete="CASCADE"), primary_key=True),
    Column("evidence_id", UUID(as_uuid=True), ForeignKey("evidence.id", ondelete="CASCADE"), primary_key=True),
)


class Evidence(TimestampMixin, Base):
    __tablename__ = "evidence"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    control_group_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("control_groups.id", ondelete="SET NULL"),
        nullable=True,
    )
    requirement_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("requirements.id", ondelete="SET NULL"),
    )
    assessment_item_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("assessment_items.id", ondelete="SET NULL"),
    )
    evidence_type: Mapped[EvidenceType] = mapped_column(
        SAEnum(EvidenceType, name="evidence_type", create_type=False), nullable=False
    )
    evidence_status: Mapped[EvidenceStatus] = mapped_column(
        SAEnum(EvidenceStatus, name="evidence_status", create_type=False),
        nullable=False,
        server_default="active",
    )
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    file_path: Mapped[str | None] = mapped_column(Text)
    collected_date: Mapped[date | None] = mapped_column(Date)
    expires_date: Mapped[date | None] = mapped_column(Date)
    verified_by: Mapped[str | None] = mapped_column(String(100))
    verified_date: Mapped[date | None] = mapped_column(Date)
    metadata_: Mapped[dict] = mapped_column(
        "metadata", JSONB, default=dict, server_default="{}"
    )

    # Relationships
    control_group: Mapped["ControlGroup | None"] = relationship(
        back_populates="evidence_items"
    )
    requirement: Mapped["Requirement | None"] = relationship()
    assessment_item: Mapped["AssessmentItem | None"] = relationship()


class Gap(TimestampMixin, Base):
    __tablename__ = "gaps"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    control_group_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("control_groups.id", ondelete="CASCADE"),
        nullable=False,
    )
    requirement_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("requirements.id", ondelete="SET NULL"),
    )
    assessment_item_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("assessment_items.id", ondelete="SET NULL"),
    )
    # CHECK (product_type IN ('framework', 'operational', 'both'))
    product_type: Mapped[str] = mapped_column(
        String(15), nullable=False, server_default="both"
    )
    gap_description: Mapped[str] = mapped_column(Text, nullable=False)
    severity: Mapped[GapSeverity] = mapped_column(
        SAEnum(GapSeverity, name="gap_severity", create_type=False),
        nullable=False,
        server_default="medium",
    )
    status: Mapped[GapStatus] = mapped_column(
        SAEnum(GapStatus, name="gap_status", create_type=False),
        nullable=False,
        server_default="open",
    )
    owner: Mapped[str | None] = mapped_column(String(100))
    due_date: Mapped[date | None] = mapped_column(Date)
    remediation_plan: Mapped[str | None] = mapped_column(Text)
    closed_date: Mapped[date | None] = mapped_column(Date)
    closed_by: Mapped[str | None] = mapped_column(String(100))
    metadata_: Mapped[dict] = mapped_column(
        "metadata", JSONB, default=dict, server_default="{}"
    )

    # Relationships
    control_group: Mapped["ControlGroup"] = relationship(back_populates="gaps")
    requirement: Mapped["Requirement | None"] = relationship()
    assessment_item: Mapped["AssessmentItem | None"] = relationship()
    evidence_items: Mapped[list["Evidence"]] = relationship(
        "Evidence", secondary=gap_evidence_table, lazy="select"
    )
