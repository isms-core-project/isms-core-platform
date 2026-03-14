import uuid
from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import BigInteger, Date, DateTime, ForeignKey, Integer, Numeric
from sqlalchemy import String, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base, SAEnum, TimestampMixin
from src.database.enums import (
    AssessmentType,
    ComplianceStatus,
    ProductType,
    SheetType,
)


class Assessment(TimestampMixin, Base):
    __tablename__ = "assessments"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    control_group_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("control_groups.id", ondelete="CASCADE"),
        nullable=False,
    )
    product_type: Mapped[ProductType] = mapped_column(
        SAEnum(ProductType, name="product_type", create_type=False), nullable=False
    )
    assessment_type: Mapped[AssessmentType] = mapped_column(
        SAEnum(AssessmentType, name="assessment_type", create_type=False),
        nullable=False,
    )
    document_id: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    workbook_name: Mapped[str] = mapped_column(String(200), nullable=False)
    file_path: Mapped[str] = mapped_column(Text, nullable=False)
    file_hash: Mapped[str | None] = mapped_column(String(64))
    file_size: Mapped[int | None] = mapped_column(BigInteger)
    sheets_count: Mapped[int | None] = mapped_column(Integer, server_default="0")
    # CHECK (overall_score >= 0.00 AND overall_score <= 100.00)
    overall_score: Mapped[Decimal | None] = mapped_column(Numeric(5, 2))
    items_total: Mapped[int | None] = mapped_column(Integer, server_default="0")
    items_compliant: Mapped[int | None] = mapped_column(Integer, server_default="0")
    items_partial: Mapped[int | None] = mapped_column(Integer, server_default="0")
    items_non_compliant: Mapped[int | None] = mapped_column(
        Integer, server_default="0"
    )
    items_na: Mapped[int | None] = mapped_column(Integer, server_default="0")
    gaps_count: Mapped[int | None] = mapped_column(Integer, server_default="0")
    last_generated: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    last_parsed: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    summary: Mapped[dict] = mapped_column(
        JSONB, default=dict, server_default="{}"
    )

    # Relationships
    control_group: Mapped["ControlGroup"] = relationship(back_populates="assessments")
    sheets: Mapped[list["AssessmentSheet"]] = relationship(
        back_populates="assessment", cascade="all, delete-orphan"
    )
    items: Mapped[list["AssessmentItem"]] = relationship(
        back_populates="assessment", cascade="all, delete-orphan"
    )


class AssessmentSheet(Base):
    __tablename__ = "assessment_sheets"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    assessment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("assessments.id", ondelete="CASCADE"),
        nullable=False,
    )
    sheet_name: Mapped[str] = mapped_column(String(50), nullable=False)
    sheet_type: Mapped[SheetType] = mapped_column(
        SAEnum(SheetType, name="sheet_type", create_type=False),
        nullable=False,
        server_default="assessment",
    )
    row_count: Mapped[int | None] = mapped_column(Integer, server_default="0")
    column_count: Mapped[int | None] = mapped_column(Integer, server_default="0")
    # CHECK (compliance_score >= 0.00 AND compliance_score <= 100.00)
    compliance_score: Mapped[Decimal | None] = mapped_column(Numeric(5, 2))
    metadata_: Mapped[dict] = mapped_column(
        "metadata", JSONB, default=dict, server_default="{}"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    # Relationships
    assessment: Mapped["Assessment"] = relationship(back_populates="sheets")
    items: Mapped[list["AssessmentItem"]] = relationship(
        back_populates="sheet", cascade="all, delete-orphan"
    )


class AssessmentItem(TimestampMixin, Base):
    __tablename__ = "assessment_items"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    sheet_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("assessment_sheets.id", ondelete="CASCADE"),
        nullable=False,
    )
    assessment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("assessments.id", ondelete="CASCADE"),
        nullable=False,
    )
    control_group_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("control_groups.id", ondelete="CASCADE"),
        nullable=False,
    )
    row_number: Mapped[int] = mapped_column(Integer, nullable=False)
    item_text: Mapped[str | None] = mapped_column(Text)
    status: Mapped[ComplianceStatus] = mapped_column(
        SAEnum(ComplianceStatus, name="compliance_status", create_type=False),
        nullable=False,
        server_default="not_assessed",
    )
    evidence_reference: Mapped[str | None] = mapped_column(Text)
    owner: Mapped[str | None] = mapped_column(String(100))
    due_date: Mapped[date | None] = mapped_column(Date)
    notes: Mapped[str | None] = mapped_column(Text)
    metadata_: Mapped[dict] = mapped_column(
        "metadata", JSONB, default=dict, server_default="{}"
    )

    # Relationships
    sheet: Mapped["AssessmentSheet"] = relationship(back_populates="items")
    assessment: Mapped["Assessment"] = relationship(back_populates="items")
    control_group: Mapped["ControlGroup"] = relationship()
