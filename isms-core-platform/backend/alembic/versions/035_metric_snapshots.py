"""metric_snapshots table for KPI trend data.

Revision ID: 035
Revises: 034
Create Date: 2026-04-02
"""

from alembic import op

revision = '035'
down_revision = '034'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        CREATE TABLE IF NOT EXISTS metric_snapshots (
            id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            org_id      UUID REFERENCES organisations(id) ON DELETE CASCADE,
            project_id  UUID REFERENCES projects(id) ON DELETE CASCADE,
            metric_name VARCHAR(50)     NOT NULL,
            value       NUMERIC(12, 4)  NOT NULL,
            computed_at TIMESTAMPTZ     NOT NULL DEFAULT now()
        )
    """)
    op.execute("""
        CREATE INDEX IF NOT EXISTS ix_metric_snapshots_org
            ON metric_snapshots(org_id, metric_name, computed_at DESC)
    """)
    op.execute("""
        CREATE INDEX IF NOT EXISTS ix_metric_snapshots_project
            ON metric_snapshots(project_id, metric_name, computed_at DESC)
    """)


def downgrade():
    op.execute("DROP TABLE IF EXISTS metric_snapshots")
