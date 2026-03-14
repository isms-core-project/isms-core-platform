"""Phase 7.5 — Full workbook schema import (sheet_schemas column).

Revision ID: 005_phase7_5_sheet_schemas
Revises: 004_generator_override
Create Date: 2026-03-07

Changes:
  1. ALTER TABLE generator_definitions ADD COLUMN sheet_schemas JSONB DEFAULT '[]'
     Stores per-sheet: sheet_name, sheet_type, position, header_row, data_start_row,
     freeze_panes, hide_gridlines, status_column_index, status_column_letter,
     columns [{index, letter, header, header_raw, width, dv_values, required, is_status_col}]
     Populated by datasets/scripts/import_sheet_schemas.py from workbook_schemas.json.
"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB

revision = "005_phase7_5_sheet_schemas"
down_revision = "004_generator_override"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "generator_definitions",
        sa.Column(
            "sheet_schemas",
            JSONB(),
            nullable=False,
            server_default="[]",
        ),
    )


def downgrade():
    op.drop_column("generator_definitions", "sheet_schemas")
