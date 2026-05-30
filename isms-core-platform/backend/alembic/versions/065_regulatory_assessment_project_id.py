"""add project_id to compliance_assessments

Revision ID: 065
Revises: 064
Create Date: 2026-05-30
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision = '065'
down_revision = '064'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        "ALTER TABLE compliance_assessments ADD COLUMN IF NOT EXISTS project_id UUID "
        "REFERENCES projects(id) ON DELETE SET NULL"
    )
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_compliance_assessments_project_id "
        "ON compliance_assessments (project_id)"
    )


def downgrade() -> None:
    op.execute("DROP INDEX IF EXISTS ix_compliance_assessments_project_id")
    op.drop_column('compliance_assessments', 'project_id')
