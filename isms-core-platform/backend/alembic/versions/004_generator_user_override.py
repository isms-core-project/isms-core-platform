"""Phase 7.3 — generator_definitions.user_override column.

Revision ID: 004_generator_override
Revises: 003_phase7_generators
Create Date: 2026-03-07

Changes:
  1. ALTER TABLE generator_definitions ADD COLUMN user_override BOOLEAN DEFAULT FALSE
     When true, the importer skips this row on re-import (preserves manual edits).
"""

import sqlalchemy as sa
from alembic import op

revision = "004_generator_override"
down_revision = "003_phase7_generators"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "generator_definitions",
        sa.Column(
            "user_override",
            sa.Boolean(),
            nullable=False,
            server_default="false",
        ),
    )


def downgrade():
    op.drop_column("generator_definitions", "user_override")
