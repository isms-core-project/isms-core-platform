"""BIA records — Business Impact Analysis.

Revision ID: 038
Revises: 037
Create Date: 2026-04-02
"""

from alembic import op

revision = '038'
down_revision = '037'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        CREATE TABLE IF NOT EXISTS bia_records (
            id                    UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            org_id                UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
            project_id            UUID REFERENCES projects(id) ON DELETE SET NULL,
            control_group_id      UUID REFERENCES control_groups(id) ON DELETE SET NULL,
            asset_name            VARCHAR(300) NOT NULL,
            asset_type            VARCHAR(20)  NOT NULL DEFAULT 'process',
            owner_id              UUID REFERENCES users(id) ON DELETE SET NULL,
            rto_hours             INT,
            rpo_hours             INT,
            mtpd_hours            INT,
            financial_impact      INT CHECK (financial_impact BETWEEN 1 AND 5),
            operational_impact    INT CHECK (operational_impact BETWEEN 1 AND 5),
            reputational_impact   INT CHECK (reputational_impact BETWEEN 1 AND 5),
            regulatory_impact     INT CHECK (regulatory_impact BETWEEN 1 AND 5),
            recovery_tested       BOOLEAN NOT NULL DEFAULT FALSE,
            last_tested_date      DATE,
            continuity_plan_ref   VARCHAR(300),
            notes                 TEXT,
            created_at            TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at            TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_bia_records_org ON bia_records(org_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_bia_records_project ON bia_records(project_id)")


def downgrade():
    op.execute("DROP TABLE IF EXISTS bia_records")
