"""033 — Risk Register: risk_matrices + risk_scenarios tables

Revision ID: 033
Revises: 032
Create Date: 2026-04-02
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB

revision = '033'
down_revision = '032'
branch_labels = None
depends_on = None


def upgrade():
    # ── risk_matrices ──────────────────────────────────────────────────────────
    op.create_table(
        'risk_matrices',
        sa.Column('id',                  UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('org_id',              UUID(as_uuid=True), sa.ForeignKey('organisations.id', ondelete='CASCADE'), nullable=False),
        sa.Column('name',                sa.String(120), nullable=False, server_default='Default 5×5 Matrix'),
        sa.Column('probability_labels',  JSONB, nullable=False),
        sa.Column('impact_labels',       JSONB, nullable=False),
        sa.Column('score_map',           JSONB, nullable=False),   # {"1,1": 1, "1,2": 2, ...}
        sa.Column('colour_map',          JSONB, nullable=False),   # {"1": "low", "6": "medium", ...}
        sa.Column('is_default',          sa.Boolean, nullable=False, server_default='true'),
        sa.Column('created_at',          sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    )
    op.create_index('ix_risk_matrices_org_id', 'risk_matrices', ['org_id'])

    # ── risk_treatment_status enum ─────────────────────────────────────────────
    op.execute("CREATE TYPE risktreatmentstatus AS ENUM ('pending','accept','mitigate','transfer','avoid')")

    # ── risk_level enum ────────────────────────────────────────────────────────
    op.execute("CREATE TYPE risklevel AS ENUM ('low','medium','high','critical')")

    # ── risk_status enum ───────────────────────────────────────────────────────
    op.execute("CREATE TYPE riskstatus AS ENUM ('open','in_treatment','closed','accepted')")

    # ── risk_scenarios ─────────────────────────────────────────────────────────
    op.create_table(
        'risk_scenarios',
        sa.Column('id',                    UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('org_id',                UUID(as_uuid=True), sa.ForeignKey('organisations.id', ondelete='CASCADE'), nullable=False),
        sa.Column('project_id',            UUID(as_uuid=True), sa.ForeignKey('projects.id', ondelete='SET NULL'), nullable=True),
        sa.Column('control_group_id',      UUID(as_uuid=True), sa.ForeignKey('control_groups.id', ondelete='SET NULL'), nullable=True),
        sa.Column('name',                  sa.String(255), nullable=False),
        sa.Column('description',           sa.Text, nullable=True),
        sa.Column('threat_source',         sa.String(120), nullable=True),
        sa.Column('threat_event',          sa.String(255), nullable=True),
        # Inherent risk
        sa.Column('probability',           sa.Integer, nullable=False, server_default='1'),  # 1–5
        sa.Column('impact',                sa.Integer, nullable=False, server_default='1'),  # 1–5
        sa.Column('risk_score',            sa.Integer, nullable=False, server_default='1'),
        sa.Column('risk_level',            sa.Enum('low', 'medium', 'high', 'critical', name='risklevel'), nullable=False, server_default='low'),
        # Treatment
        sa.Column('treatment_status',      sa.Enum('pending', 'accept', 'mitigate', 'transfer', 'avoid', name='risktreatmentstatus'), nullable=False, server_default='pending'),
        sa.Column('treatment_notes',       sa.Text, nullable=True),
        # Residual risk
        sa.Column('residual_probability',  sa.Integer, nullable=True),
        sa.Column('residual_impact',       sa.Integer, nullable=True),
        sa.Column('residual_score',        sa.Integer, nullable=True),
        sa.Column('residual_level',        sa.Enum('low', 'medium', 'high', 'critical', name='risklevel'), nullable=True),
        # Meta
        sa.Column('owner_id',              UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='SET NULL'), nullable=True),
        sa.Column('target_date',           sa.Date, nullable=True),
        sa.Column('status',                sa.Enum('open', 'in_treatment', 'closed', 'accepted', name='riskstatus'), nullable=False, server_default='open'),
        sa.Column('created_at',            sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at',            sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    )
    op.create_index('ix_risk_scenarios_org_id',      'risk_scenarios', ['org_id'])
    op.create_index('ix_risk_scenarios_project_id',  'risk_scenarios', ['project_id'])
    op.create_index('ix_risk_scenarios_status',      'risk_scenarios', ['status'])
    op.create_index('ix_risk_scenarios_risk_level',  'risk_scenarios', ['risk_level'])


def downgrade():
    op.drop_table('risk_scenarios')
    op.drop_table('risk_matrices')
    op.execute("DROP TYPE IF EXISTS riskstatus")
    op.execute("DROP TYPE IF EXISTS risklevel")
    op.execute("DROP TYPE IF EXISTS risktreatmentstatus")
