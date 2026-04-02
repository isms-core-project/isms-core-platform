"""TPRM domain models — Vendor, VendorAssessment, VendorContract."""

import uuid
from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class Vendor(Base):
    __tablename__ = "vendors"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organisations.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    vendor_type: Mapped[str] = mapped_column(String(20), nullable=False, default="supplier")
    criticality: Mapped[str] = mapped_column(String(20), nullable=False, default="medium")
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="active")
    description: Mapped[str | None] = mapped_column(Text)
    website: Mapped[str | None] = mapped_column(String(500))
    primary_contact: Mapped[str | None] = mapped_column(String(200))
    dora_entity_type: Mapped[str | None] = mapped_column(String(50))
    dora_ict_service_type: Mapped[str | None] = mapped_column(String(50))
    dora_substitutability: Mapped[str | None] = mapped_column(String(30))
    dora_register_ref: Mapped[str | None] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

    assessments: Mapped[list["VendorAssessment"]] = relationship(back_populates="vendor", cascade="all, delete-orphan")
    contracts: Mapped[list["VendorContract"]] = relationship(back_populates="vendor", cascade="all, delete-orphan")


class VendorAssessment(Base):
    __tablename__ = "vendor_assessments"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    vendor_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("vendors.id", ondelete="CASCADE"), nullable=False)
    control_group_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("control_groups.id", ondelete="SET NULL"))
    assessor_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    score: Mapped[int | None] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="not_assessed")
    notes: Mapped[str | None] = mapped_column(Text)
    assessment_date: Mapped[date | None] = mapped_column(Date)
    next_review_date: Mapped[date | None] = mapped_column(Date)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    vendor: Mapped["Vendor"] = relationship(back_populates="assessments")


class VendorContract(Base):
    __tablename__ = "vendor_contracts"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    vendor_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("vendors.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    contract_ref: Mapped[str | None] = mapped_column(String(100))
    start_date: Mapped[date | None] = mapped_column(Date)
    expiry_date: Mapped[date | None] = mapped_column(Date)
    auto_renews: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    security_clauses_present: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    vendor: Mapped["Vendor"] = relationship(back_populates="contracts")
