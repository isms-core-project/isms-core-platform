"""Phase 26 — CVE Intelligence Integration.

Revision ID: 047
Revises: 046
Create Date: 2026-04-06

Changes:
  - Add 'threat_intel' to evidence_type Postgres enum
  - Add kev_cve_id VARCHAR(30) nullable column to evidence table
  - Add index on evidence.kev_cve_id for fast KEV evidence lookups
"""

from alembic import op
import sqlalchemy as sa

revision = '047'
down_revision = '046'
branch_labels = None
depends_on = None


def upgrade():
    # Add new enum value (IF NOT EXISTS requires Postgres 9.3+; safe to re-run)
    op.execute("ALTER TYPE evidence_type ADD VALUE IF NOT EXISTS 'threat_intel'")

    # Add kev_cve_id column to evidence table
    op.add_column('evidence', sa.Column('kev_cve_id', sa.String(30), nullable=True))
    op.create_index('ix_evidence_kev_cve_id', 'evidence', ['kev_cve_id'])


def downgrade():
    op.drop_index('ix_evidence_kev_cve_id', table_name='evidence')
    op.drop_column('evidence', 'kev_cve_id')
    # Note: Postgres does not support removing enum values — threat_intel stays in the type
