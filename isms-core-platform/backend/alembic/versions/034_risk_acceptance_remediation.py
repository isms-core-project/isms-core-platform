"""034 — Risk acceptances + remediation actions

Revision ID: 034
Revises: 033
Create Date: 2026-04-02
"""

from alembic import op

revision = '034'
down_revision = '033'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        CREATE TABLE IF NOT EXISTS risk_acceptances (
            id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            risk_scenario_id UUID NOT NULL REFERENCES risk_scenarios(id) ON DELETE CASCADE,
            approver_id      UUID REFERENCES users(id) ON DELETE SET NULL,
            approver_name    VARCHAR(255) NOT NULL,
            justification    TEXT NOT NULL,
            expiry_date      DATE,
            status           VARCHAR(20) NOT NULL DEFAULT 'active',
            revoked_by       UUID REFERENCES users(id) ON DELETE SET NULL,
            revoked_at       TIMESTAMPTZ,
            created_at       TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_risk_acceptances_scenario ON risk_acceptances (risk_scenario_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_risk_acceptances_status   ON risk_acceptances (status)")

    op.execute("""
        CREATE TABLE IF NOT EXISTS remediation_actions (
            id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            org_id           UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
            project_id       UUID REFERENCES projects(id) ON DELETE SET NULL,
            risk_scenario_id UUID REFERENCES risk_scenarios(id) ON DELETE SET NULL,
            gap_id           UUID REFERENCES gaps(id) ON DELETE SET NULL,
            control_group_id UUID REFERENCES control_groups(id) ON DELETE SET NULL,
            title            VARCHAR(255) NOT NULL,
            description      TEXT,
            status           VARCHAR(20) NOT NULL DEFAULT 'planned',
            owner_id         UUID REFERENCES users(id) ON DELETE SET NULL,
            eta              DATE,
            effort           VARCHAR(10),
            cost_estimate    NUMERIC(12, 2),
            progress         INTEGER NOT NULL DEFAULT 0,
            evidence_id      UUID REFERENCES evidence(id) ON DELETE SET NULL,
            created_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at       TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_remediation_org_id     ON remediation_actions (org_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_remediation_status     ON remediation_actions (status)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_remediation_risk_id    ON remediation_actions (risk_scenario_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_remediation_gap_id     ON remediation_actions (gap_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_remediation_owner_id   ON remediation_actions (owner_id)")


def downgrade():
    op.execute("DROP TABLE IF EXISTS remediation_actions")
    op.execute("DROP TABLE IF EXISTS risk_acceptances")
