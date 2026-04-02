"""033 — Risk Register: risk_matrices + risk_scenarios tables

Revision ID: 033
Revises: 032_org_is_active
Create Date: 2026-04-02
"""

from alembic import op

revision = '033'
down_revision = '032_org_is_active'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        CREATE TABLE IF NOT EXISTS risk_matrices (
            id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            org_id              UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
            name                VARCHAR(120) NOT NULL DEFAULT 'Default 5×5 Matrix',
            probability_labels  JSONB NOT NULL,
            impact_labels       JSONB NOT NULL,
            score_map           JSONB NOT NULL,
            colour_map          JSONB NOT NULL,
            is_default          BOOLEAN NOT NULL DEFAULT true,
            created_at          TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_risk_matrices_org_id ON risk_matrices (org_id)")

    op.execute("""
        DO $$ BEGIN
            CREATE TYPE risktreatmentstatus AS ENUM ('pending','accept','mitigate','transfer','avoid');
        EXCEPTION WHEN duplicate_object THEN null;
        END $$
    """)
    op.execute("""
        DO $$ BEGIN
            CREATE TYPE risklevel AS ENUM ('low','medium','high','critical');
        EXCEPTION WHEN duplicate_object THEN null;
        END $$
    """)
    op.execute("""
        DO $$ BEGIN
            CREATE TYPE riskstatus AS ENUM ('open','in_treatment','closed','accepted');
        EXCEPTION WHEN duplicate_object THEN null;
        END $$
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS risk_scenarios (
            id                   UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            org_id               UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
            project_id           UUID REFERENCES projects(id) ON DELETE SET NULL,
            control_group_id     UUID REFERENCES control_groups(id) ON DELETE SET NULL,
            name                 VARCHAR(255) NOT NULL,
            description          TEXT,
            threat_source        VARCHAR(120),
            threat_event         VARCHAR(255),
            probability          INTEGER NOT NULL DEFAULT 1,
            impact               INTEGER NOT NULL DEFAULT 1,
            risk_score           INTEGER NOT NULL DEFAULT 1,
            risk_level           risklevel NOT NULL DEFAULT 'low',
            treatment_status     risktreatmentstatus NOT NULL DEFAULT 'pending',
            treatment_notes      TEXT,
            residual_probability INTEGER,
            residual_impact      INTEGER,
            residual_score       INTEGER,
            residual_level       risklevel,
            owner_id             UUID REFERENCES users(id) ON DELETE SET NULL,
            target_date          DATE,
            status               riskstatus NOT NULL DEFAULT 'open',
            created_at           TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at           TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_risk_scenarios_org_id     ON risk_scenarios (org_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_risk_scenarios_project_id ON risk_scenarios (project_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_risk_scenarios_status     ON risk_scenarios (status)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_risk_scenarios_risk_level ON risk_scenarios (risk_level)")


def downgrade():
    op.execute("DROP TABLE IF EXISTS risk_scenarios")
    op.execute("DROP TABLE IF EXISTS risk_matrices")
    op.execute("DROP TYPE IF EXISTS riskstatus")
    op.execute("DROP TYPE IF EXISTS risklevel")
    op.execute("DROP TYPE IF EXISTS risktreatmentstatus")
