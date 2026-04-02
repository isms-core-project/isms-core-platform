"""EBIOS RM domain models — Study, FearedEvent, RiskSource, StrategicScenario, AttackPath, Measure."""

import uuid
from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class EbiosStudy(Base):
    __tablename__ = "ebios_studies"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organisations.id", ondelete="CASCADE"), nullable=False)
    project_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("projects.id", ondelete="SET NULL"), nullable=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    scope: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="draft")
    owner: Mapped[str | None] = mapped_column(Text)
    started_at: Mapped[date | None] = mapped_column(Date)
    reviewed_at: Mapped[date | None] = mapped_column(Date)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

    feared_events: Mapped[list["EbiosFearedEvent"]] = relationship(back_populates="study", cascade="all, delete-orphan")
    risk_sources: Mapped[list["EbiosRiskSource"]] = relationship(back_populates="study", cascade="all, delete-orphan")
    strategic_scenarios: Mapped[list["EbiosStrategicScenario"]] = relationship(back_populates="study", cascade="all, delete-orphan")
    attack_paths: Mapped[list["EbiosAttackPath"]] = relationship(back_populates="study", cascade="all, delete-orphan")
    measures: Mapped[list["EbiosMeasure"]] = relationship(back_populates="study", cascade="all, delete-orphan")


class EbiosFearedEvent(Base):
    __tablename__ = "ebios_feared_events"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    study_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("ebios_studies.id", ondelete="CASCADE"), nullable=False)
    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organisations.id", ondelete="CASCADE"), nullable=False)
    asset_name: Mapped[str] = mapped_column(Text, nullable=False)
    asset_type: Mapped[str] = mapped_column(String(50), nullable=False, default="primary")
    description: Mapped[str | None] = mapped_column(Text)
    gravity: Mapped[int | None] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    study: Mapped["EbiosStudy"] = relationship(back_populates="feared_events")


class EbiosRiskSource(Base):
    __tablename__ = "ebios_risk_sources"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    study_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("ebios_studies.id", ondelete="CASCADE"), nullable=False)
    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organisations.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False, default="cybercriminal")
    motivation: Mapped[str | None] = mapped_column(Text)
    pertinence: Mapped[int | None] = mapped_column(Integer)
    activity: Mapped[int | None] = mapped_column(Integer)
    resources: Mapped[int | None] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    study: Mapped["EbiosStudy"] = relationship(back_populates="risk_sources")


class EbiosStrategicScenario(Base):
    __tablename__ = "ebios_strategic_scenarios"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    study_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("ebios_studies.id", ondelete="CASCADE"), nullable=False)
    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organisations.id", ondelete="CASCADE"), nullable=False)
    risk_source_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("ebios_risk_sources.id", ondelete="SET NULL"), nullable=True)
    feared_event_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("ebios_feared_events.id", ondelete="SET NULL"), nullable=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    likelihood: Mapped[int | None] = mapped_column(Integer)
    gravity: Mapped[int | None] = mapped_column(Integer)
    # risk_level is a DB-generated column (likelihood * gravity) — not mapped here
    retained: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    study: Mapped["EbiosStudy"] = relationship(back_populates="strategic_scenarios")
    attack_paths: Mapped[list["EbiosAttackPath"]] = relationship(back_populates="strategic_scenario", cascade="all, delete-orphan")
    measures: Mapped[list["EbiosMeasure"]] = relationship(back_populates="scenario", cascade="all, delete-orphan")


class EbiosAttackPath(Base):
    __tablename__ = "ebios_attack_paths"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    study_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("ebios_studies.id", ondelete="CASCADE"), nullable=False)
    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organisations.id", ondelete="CASCADE"), nullable=False)
    strategic_scenario_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("ebios_strategic_scenarios.id", ondelete="SET NULL"), nullable=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    mitre_techniques: Mapped[list] = mapped_column(JSONB, nullable=False, default=list)
    difficulty: Mapped[int | None] = mapped_column(Integer)
    detectability: Mapped[int | None] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    study: Mapped["EbiosStudy"] = relationship(back_populates="attack_paths")
    strategic_scenario: Mapped["EbiosStrategicScenario | None"] = relationship(back_populates="attack_paths")


class EbiosMeasure(Base):
    __tablename__ = "ebios_measures"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    study_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("ebios_studies.id", ondelete="CASCADE"), nullable=False)
    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organisations.id", ondelete="CASCADE"), nullable=False)
    scenario_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("ebios_strategic_scenarios.id", ondelete="SET NULL"), nullable=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="planned")
    iso_control_ref: Mapped[str | None] = mapped_column(Text)
    control_group_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("control_groups.id", ondelete="SET NULL"), nullable=True)
    effectiveness: Mapped[int | None] = mapped_column(Integer)
    due_date: Mapped[date | None] = mapped_column(Date)
    owner: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

    study: Mapped["EbiosStudy"] = relationship(back_populates="measures")
    scenario: Mapped["EbiosStrategicScenario | None"] = relationship(back_populates="measures")
