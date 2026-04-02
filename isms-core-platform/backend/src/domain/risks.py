"""Risk Register domain models — risk_matrices, risk_scenarios, acceptances, remediation."""

import uuid
from datetime import date, datetime, timezone

from sqlalchemy import Boolean, Date, DateTime, Enum as SAEnum, ForeignKey, Integer, Numeric, String, Text
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
    score_map:          Mapped[dict]      = mapped_column(JSONB, nullable=False)
    colour_map:         Mapped[dict]      = mapped_column(JSONB, nullable=False)
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
    probability:          Mapped[int]            = mapped_column(Integer, nullable=False, default=1)
    impact:               Mapped[int]            = mapped_column(Integer, nullable=False, default=1)
    risk_score:           Mapped[int]            = mapped_column(Integer, nullable=False, default=1)
    risk_level:           Mapped[str]            = mapped_column(SAEnum('low', 'medium', 'high', 'critical', name='risklevel'), nullable=False, default='low')
    treatment_status:     Mapped[str]            = mapped_column(SAEnum('pending', 'accept', 'mitigate', 'transfer', 'avoid', name='risktreatmentstatus'), nullable=False, default='pending')
    treatment_notes:      Mapped[str|None]       = mapped_column(Text, nullable=True)
    residual_probability: Mapped[int|None]       = mapped_column(Integer, nullable=True)
    residual_impact:      Mapped[int|None]       = mapped_column(Integer, nullable=True)
    residual_score:       Mapped[int|None]       = mapped_column(Integer, nullable=True)
    residual_level:       Mapped[str|None]       = mapped_column(SAEnum('low', 'medium', 'high', 'critical', name='risklevel'), nullable=True)
    owner_id:             Mapped[uuid.UUID|None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    target_date:          Mapped[date|None]      = mapped_column(Date, nullable=True)
    status:               Mapped[str]            = mapped_column(SAEnum('open', 'in_treatment', 'closed', 'accepted', name='riskstatus'), nullable=False, default='open')
    created_at:           Mapped[datetime]       = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at:           Mapped[datetime]       = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    organisation       = relationship('Organisation',    back_populates='risk_scenarios',    lazy='select')
    project            = relationship('Project',         back_populates='risk_scenarios',    lazy='select')
    control_group      = relationship('ControlGroup',    back_populates='risk_scenarios',    lazy='select')
    owner              = relationship('User',            back_populates='risk_scenarios',    lazy='select', foreign_keys=[owner_id])
    acceptances        = relationship('RiskAcceptance',  back_populates='risk_scenario',     lazy='select', cascade='all, delete-orphan')
    remediation_actions = relationship('RemediationAction', back_populates='risk_scenario',  lazy='select')


class RiskAcceptance(Base):
    __tablename__ = 'risk_acceptances'

    id:               Mapped[uuid.UUID]      = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    risk_scenario_id: Mapped[uuid.UUID]      = mapped_column(UUID(as_uuid=True), ForeignKey('risk_scenarios.id', ondelete='CASCADE'), nullable=False)
    approver_id:      Mapped[uuid.UUID|None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    approver_name:    Mapped[str]            = mapped_column(String(255), nullable=False)
    justification:    Mapped[str]            = mapped_column(Text, nullable=False)
    expiry_date:      Mapped[date|None]      = mapped_column(Date, nullable=True)
    status:           Mapped[str]            = mapped_column(String(20), nullable=False, default='active')
    revoked_by:       Mapped[uuid.UUID|None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    revoked_at:       Mapped[datetime|None]  = mapped_column(DateTime(timezone=True), nullable=True)
    created_at:       Mapped[datetime]       = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    risk_scenario = relationship('RiskScenario', back_populates='acceptances',    lazy='select')
    approver      = relationship('User', foreign_keys=[approver_id],              lazy='select')
    revoker       = relationship('User', foreign_keys=[revoked_by],               lazy='select')


class RemediationAction(Base):
    __tablename__ = 'remediation_actions'

    id:               Mapped[uuid.UUID]      = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    org_id:           Mapped[uuid.UUID]      = mapped_column(UUID(as_uuid=True), ForeignKey('organisations.id', ondelete='CASCADE'), nullable=False)
    project_id:       Mapped[uuid.UUID|None] = mapped_column(UUID(as_uuid=True), ForeignKey('projects.id', ondelete='SET NULL'), nullable=True)
    risk_scenario_id: Mapped[uuid.UUID|None] = mapped_column(UUID(as_uuid=True), ForeignKey('risk_scenarios.id', ondelete='SET NULL'), nullable=True)
    gap_id:           Mapped[uuid.UUID|None] = mapped_column(UUID(as_uuid=True), ForeignKey('gaps.id', ondelete='SET NULL'), nullable=True)
    control_group_id: Mapped[uuid.UUID|None] = mapped_column(UUID(as_uuid=True), ForeignKey('control_groups.id', ondelete='SET NULL'), nullable=True)
    title:            Mapped[str]            = mapped_column(String(255), nullable=False)
    description:      Mapped[str|None]       = mapped_column(Text, nullable=True)
    status:           Mapped[str]            = mapped_column(String(20), nullable=False, default='planned')
    owner_id:         Mapped[uuid.UUID|None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    eta:              Mapped[date|None]      = mapped_column(Date, nullable=True)
    effort:           Mapped[str|None]       = mapped_column(String(10), nullable=True)
    cost_estimate:    Mapped[float|None]     = mapped_column(Numeric(12, 2), nullable=True)
    progress:         Mapped[int]            = mapped_column(Integer, nullable=False, default=0)
    evidence_id:      Mapped[uuid.UUID|None] = mapped_column(UUID(as_uuid=True), ForeignKey('evidence.id', ondelete='SET NULL'), nullable=True)
    created_at:       Mapped[datetime]       = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at:       Mapped[datetime]       = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    organisation  = relationship('Organisation',  lazy='select')
    risk_scenario = relationship('RiskScenario',  back_populates='remediation_actions', lazy='select')
    owner         = relationship('User',          foreign_keys=[owner_id],              lazy='select')
