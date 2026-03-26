import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class CsrmAssessment(Base):
    __tablename__ = "csrm_assessments"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    organisation: Mapped[str | None] = mapped_column(String(200))
    assessor: Mapped[str | None] = mapped_column(String(100))
    scope: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="draft")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default="now()")
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default="now()")

    objects: Mapped[list["CsrmProtectionObject"]] = relationship(
        back_populates="assessment",
        cascade="all, delete-orphan",
        order_by="CsrmProtectionObject.sort_order",
    )


class CsrmProtectionObject(Base):
    __tablename__ = "csrm_protection_objects"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    assessment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("csrm_assessments.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    architecture_notes: Mapped[str | None] = mapped_column(Text)
    processes_served: Mapped[str | None] = mapped_column(Text)
    data_classification: Mapped[str | None] = mapped_column(String(50), default="standard")
    protection_level: Mapped[str] = mapped_column(String(20), nullable=False, default="standard")
    elevated_rationale: Mapped[str | None] = mapped_column(Text)
    sort_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default="now()")
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default="now()")

    assessment: Mapped["CsrmAssessment"] = relationship(back_populates="objects")
    baseline_ratings: Mapped[list["CsrmBaselineRating"]] = relationship(
        back_populates="protection_object", cascade="all, delete-orphan"
    )
    elevated_toms: Mapped[list["CsrmElevatedTom"]] = relationship(
        back_populates="protection_object", cascade="all, delete-orphan"
    )


class CsrmBaselineRating(Base):
    __tablename__ = "csrm_baseline_ratings"
    __table_args__ = (UniqueConstraint("object_id", "requirement_id", name="uq_csrm_baseline_rating"),)

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    assessment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("csrm_assessments.id", ondelete="CASCADE"), nullable=False
    )
    object_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("csrm_protection_objects.id", ondelete="CASCADE"), nullable=False
    )
    requirement_id: Mapped[str] = mapped_column(String(10), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="not_assessed")
    exception_justification: Mapped[str | None] = mapped_column(Text)
    notes: Mapped[str | None] = mapped_column(Text)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default="now()")

    protection_object: Mapped["CsrmProtectionObject"] = relationship(back_populates="baseline_ratings")


class CsrmElevatedTom(Base):
    __tablename__ = "csrm_elevated_toms"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    assessment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("csrm_assessments.id", ondelete="CASCADE"), nullable=False
    )
    object_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("csrm_protection_objects.id", ondelete="CASCADE"), nullable=False
    )
    threat_category: Mapped[str] = mapped_column(String(100), nullable=False)
    tom_description: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="planned")
    notes: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default="now()")
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default="now()")

    protection_object: Mapped["CsrmProtectionObject"] = relationship(back_populates="elevated_toms")
