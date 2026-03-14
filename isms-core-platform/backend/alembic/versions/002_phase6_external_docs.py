"""Phase 6 — External document support + multi-language.

Revision ID: 002_phase6_external
Revises: 001_foundation
Create Date: 2026-03-07

Changes:
  1. ALTER TYPE product_type ADD VALUE 'external'
  2. ALTER TABLE policies ADD COLUMN source_label VARCHAR(200)
  3. ALTER TABLE policies ADD COLUMN language VARCHAR(5) DEFAULT 'en'
  4. ALTER TABLE implementations ADD COLUMN language VARCHAR(5) DEFAULT 'en'
"""

import sqlalchemy as sa
from alembic import op

revision = "002_phase6_external"
down_revision = "001_foundation"
branch_labels = None
depends_on = None


def upgrade():
    # 1 — ADD VALUE cannot run inside a transaction in PostgreSQL
    with op.get_context().autocommit_block():
        op.execute(sa.text("ALTER TYPE product_type ADD VALUE IF NOT EXISTS 'external'"))

    # 2 — source_label: free-text origin for external docs (e.g. "Acme Corp", "Previous consultant")
    op.add_column(
        "policies",
        sa.Column("source_label", sa.String(200), nullable=True),
    )

    # 3 — language on policies
    op.add_column(
        "policies",
        sa.Column("language", sa.String(5), nullable=False, server_default="en"),
    )

    # 4 — language on implementations (for FR/IT IMP translations)
    op.add_column(
        "implementations",
        sa.Column("language", sa.String(5), nullable=False, server_default="en"),
    )


def downgrade():
    op.drop_column("implementations", "language")
    op.drop_column("policies", "language")
    op.drop_column("policies", "source_label")
    # Note: PostgreSQL does not support removing enum values.
    # 'external' in product_type must be removed manually if required.
