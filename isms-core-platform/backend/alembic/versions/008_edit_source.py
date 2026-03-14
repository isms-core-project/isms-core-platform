"""Phase 7.18 — Edit source audit trail.

Revision ID: 008_edit_source
Revises: 007_content_state
Create Date: 2026-03-08

Changes:
  1. CREATE TYPE edit_source AS ENUM ('import', 'webui', 'api')
  2. ALTER TABLE policies ADD COLUMN edit_source edit_source NOT NULL DEFAULT 'import'
     (all existing content arrived via import pipeline)
  3. ALTER TABLE implementations ADD COLUMN edit_source edit_source NOT NULL DEFAULT 'import'

The audit_log table (existing) records full history of changes.
edit_source on the content row shows how the record was last modified.
"""

from alembic import op

revision = "008_edit_source"
down_revision = "007_content_state"
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE TYPE edit_source AS ENUM ('import', 'webui', 'api')")

    op.execute("""
        ALTER TABLE policies
        ADD COLUMN edit_source edit_source NOT NULL DEFAULT 'import'
    """)
    op.execute("CREATE INDEX ix_policies_edit_source ON policies(edit_source)")

    op.execute("""
        ALTER TABLE implementations
        ADD COLUMN edit_source edit_source NOT NULL DEFAULT 'import'
    """)
    op.execute("CREATE INDEX ix_implementations_edit_source ON implementations(edit_source)")


def downgrade():
    op.execute("DROP INDEX IF EXISTS ix_implementations_edit_source")
    op.execute("ALTER TABLE implementations DROP COLUMN IF EXISTS edit_source")
    op.execute("DROP INDEX IF EXISTS ix_policies_edit_source")
    op.execute("ALTER TABLE policies DROP COLUMN IF EXISTS edit_source")
    op.execute("DROP TYPE IF EXISTS edit_source")
