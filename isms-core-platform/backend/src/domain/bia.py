"""BIA domain model — Business Impact Analysis records."""

import uuid
from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class BIARecord(Base):
    __tablename__ = "bia_records"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organisations.id", ondelete="CASCADE"), nullable=False)
    project_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("projects.id", ondelete="SET NULL"))
    control_group_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("control_groups.id", ondelete="SET NULL"))
    asset_name: Mapped[str] = mapped_column(String(300), nullable=False)
    asset_type: Mapped[str] = mapped_column(String(20), nullable=False, default="process")
    owner_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    rto_hours: Mapped[int | None] = mapped_column(Integer)
    rpo_hours: Mapped[int | None] = mapped_column(Integer)
    mtpd_hours: Mapped[int | None] = mapped_column(Integer)
    financial_impact: Mapped[int | None] = mapped_column(Integer)
    operational_impact: Mapped[int | None] = mapped_column(Integer)
    reputational_impact: Mapped[int | None] = mapped_column(Integer)
    regulatory_impact: Mapped[int | None] = mapped_column(Integer)
    recovery_tested: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    last_tested_date: Mapped[date | None] = mapped_column(Date)
    continuity_plan_ref: Mapped[str | None] = mapped_column(String(300))
    notes: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
