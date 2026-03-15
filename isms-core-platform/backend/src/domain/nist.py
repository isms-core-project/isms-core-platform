"""SQLAlchemy models for NIST CSF 2.0 assessment profiles."""

import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, SmallInteger, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.domain.frameworks import FrameworkControl

from src.database.base import Base, TimestampMixin


class NistCsfProfile(TimestampMixin, Base):
    __tablename__ = "nist_csf_profiles"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    assessor: Mapped[str | None] = mapped_column(String(100), nullable=True)
    scope: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="draft")

    ratings: Mapped[list["NistCsfRating"]] = relationship(
        "NistCsfRating", back_populates="profile", cascade="all, delete-orphan"
    )


class NistCsfRating(Base):
    __tablename__ = "nist_csf_ratings"
    __table_args__ = (
        UniqueConstraint("profile_id", "subcategory_id", name="uq_nist_rating_profile_subcategory"),
        Index("ix_nist_csf_ratings_profile_id", "profile_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    profile_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("nist_csf_profiles.id", ondelete="CASCADE"), nullable=False
    )
    subcategory_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("framework_controls.id", ondelete="CASCADE"), nullable=False
    )
    current_tier: Mapped[int | None] = mapped_column(SmallInteger, nullable=True)
    target_tier: Mapped[int | None] = mapped_column(SmallInteger, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default="now()", nullable=False
    )

    profile: Mapped["NistCsfProfile"] = relationship("NistCsfProfile", back_populates="ratings")
    subcategory: Mapped["FrameworkControl"] = relationship("FrameworkControl", lazy="select")
