"""SQLAlchemy models for generic regulatory compliance assessments (NIS2, DORA, extensible)."""

import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, SmallInteger, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.domain.frameworks import FrameworkControl

from src.database.base import Base, TimestampMixin


class RegulatoryAssessment(TimestampMixin, Base):
    __tablename__ = "compliance_assessments"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    framework_code: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    assessor: Mapped[str | None] = mapped_column(String(100), nullable=True)
    scope: Mapped[str | None] = mapped_column(Text, nullable=True)
    organisation: Mapped[str | None] = mapped_column(String(200), nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="draft")

    ratings: Mapped[list["RegulatoryRating"]] = relationship(
        "RegulatoryRating", back_populates="assessment", cascade="all, delete-orphan"
    )


class RegulatoryRating(Base):
    __tablename__ = "compliance_ratings"
    __table_args__ = (
        UniqueConstraint("assessment_id", "requirement_id", name="uq_compliance_rating_assessment_req"),
        Index("ix_compliance_ratings_assessment_id", "assessment_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    assessment_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("compliance_assessments.id", ondelete="CASCADE"), nullable=False
    )
    requirement_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("framework_controls.id", ondelete="CASCADE"), nullable=False
    )
    current_score: Mapped[int | None] = mapped_column(SmallInteger, nullable=True)
    target_score: Mapped[int | None] = mapped_column(SmallInteger, nullable=True)
    rating_status: Mapped[str] = mapped_column(String(20), nullable=False, default="not_assessed")
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    evidence_ref: Mapped[str | None] = mapped_column(String(500), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default="now()", nullable=False
    )

    assessment: Mapped["RegulatoryAssessment"] = relationship("RegulatoryAssessment", back_populates="ratings")
    requirement: Mapped["FrameworkControl"] = relationship("FrameworkControl", lazy="select")
