"""Phase 7.17 — Content state (approval workflow).

Revision ID: 007_content_state
Revises: 006_governance_mode
Create Date: 2026-03-08

Changes:
  1. CREATE TYPE content_state AS ENUM ('draft', 'review', 'approved', 'published')
  2. ALTER TABLE policies ADD COLUMN content_state content_state NOT NULL DEFAULT 'published'
     (imported content defaults to published — it's already QA'd)
  3. ALTER TABLE implementations ADD COLUMN content_state content_state NOT NULL DEFAULT 'published'
  4. Indexes on both tables for state filtering

Platform mode: content starts as 'draft' on WebUI creation, moves draft→review→approved→published.
Local mode: content arrives as 'published' from import pipeline (files are master).
"""

from alembic import op

revision = "007_content_state"
down_revision = "006_governance_mode"
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE TYPE content_state AS ENUM ('draft', 'review', 'approved', 'published')")

    op.execute("""
        ALTER TABLE policies
        ADD COLUMN content_state content_state NOT NULL DEFAULT 'published'
    """)
    op.execute("CREATE INDEX ix_policies_content_state ON policies(content_state)")

    op.execute("""
        ALTER TABLE implementations
        ADD COLUMN content_state content_state NOT NULL DEFAULT 'published'
    """)
    op.execute("CREATE INDEX ix_implementations_content_state ON implementations(content_state)")


def downgrade():
    op.execute("DROP INDEX IF EXISTS ix_implementations_content_state")
    op.execute("ALTER TABLE implementations DROP COLUMN IF EXISTS content_state")
    op.execute("DROP INDEX IF EXISTS ix_policies_content_state")
    op.execute("ALTER TABLE policies DROP COLUMN IF EXISTS content_state")
    op.execute("DROP TYPE IF EXISTS content_state")
