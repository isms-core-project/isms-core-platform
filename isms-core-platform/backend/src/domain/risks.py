"""Risk Register domain models — risk_matrices + risk_scenarios."""

import uuid
from datetime import date, datetime, timezone

from sqlalchemy import Boolean, Date, DateTime, Enum as SAEnum, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class RiskMatrix(Base):
    __tablename__ = 'risk_matrices'

    id:                 Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id:             Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('organisations.id', ondelete='CASCADE'), nullable=False)
    name:               Mapped[str]       = mapped_column(String(120), nullable=False, default='Default 5×5 Matrix')
    probability_labels: Mapped[list]      = mapped_column(JSONB, nullable=False)
    impact_labels:      Mapped[list]      = mapped_column(JSONB, nullable=False)
    score_map:          Mapped[dict]      = mapped_column(JSONB, nullable=False)   # "p,i" → score
    colour_map:         Mapped[dict]      = mapped_column(JSONB, nullable=False)   # score → level string
    is_default:         Mapped[bool]      = mapped_column(Boolean, nullable=False, default=True)
    created_at:         Mapped[datetime]  = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    organisation = relationship('Organisation', back_populates='risk_matrices', lazy='select')


class RiskScenario(Base):
    __tablename__ = 'risk_scenarios'

    id:                   Mapped[uuid.UUID]      = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id:               Mapped[uuid.UUID]      = mapped_column(UUID(as_uuid=True), ForeignKey('organisations.id', ondelete='CASCADE'), nullable=False)
    project_id:           Mapped[uuid.UUID|None] = mapped_column(UUID(as_uuid=True), ForeignKey('projects.id', ondelete='SET NULL'), nullable=True)
    control_group_id:     Mapped[uuid.UUID|None] = mapped_column(UUID(as_uuid=True), ForeignKey('control_groups.id', ondelete='SET NULL'), nullable=True)
    name:                 Mapped[str]            = mapped_column(String(255), nullable=False)
    description:          Mapped[str|None]       = mapped_column(Text, nullable=True)
    threat_source:        Mapped[str|None]       = mapped_column(String(120), nullable=True)
    threat_event:         Mapped[str|None]       = mapped_column(String(255), nullable=True)
    # Inherent risk
    probability:          Mapped[int]            = mapped_column(Integer, nullable=False, default=1)
    impact:               Mapped[int]            = mapped_column(Integer, nullable=False, default=1)
    risk_score:           Mapped[int]            = mapped_column(Integer, nullable=False, default=1)
    risk_level:           Mapped[str]            = mapped_column(SAEnum('low', 'medium', 'high', 'critical', name='risklevel'), nullable=False, default='low')
    # Treatment
    treatment_status:     Mapped[str]            = mapped_column(SAEnum('pending', 'accept', 'mitigate', 'transfer', 'avoid', name='risktreatmentstatus'), nullable=False, default='pending')
    treatment_notes:      Mapped[str|None]       = mapped_column(Text, nullable=True)
    # Residual risk
    residual_probability: Mapped[int|None]       = mapped_column(Integer, nullable=True)
    residual_impact:      Mapped[int|None]       = mapped_column(Integer, nullable=True)
    residual_score:       Mapped[int|None]       = mapped_column(Integer, nullable=True)
    residual_level:       Mapped[str|None]       = mapped_column(SAEnum('low', 'medium', 'high', 'critical', name='risklevel'), nullable=True)
    # Meta
    owner_id:             Mapped[uuid.UUID|None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    target_date:          Mapped[date|None]      = mapped_column(Date, nullable=True)
    status:               Mapped[str]            = mapped_column(SAEnum('open', 'in_treatment', 'closed', 'accepted', name='riskstatus'), nullable=False, default='open')
    created_at:           Mapped[datetime]       = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at:           Mapped[datetime]       = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    organisation  = relationship('Organisation', back_populates='risk_scenarios',   lazy='select')
    project       = relationship('Project',      back_populates='risk_scenarios',   lazy='select')
    control_group = relationship('ControlGroup', back_populates='risk_scenarios',   lazy='select')
    owner         = relationship('User',         back_populates='risk_scenarios',   lazy='select', foreign_keys=[owner_id])
