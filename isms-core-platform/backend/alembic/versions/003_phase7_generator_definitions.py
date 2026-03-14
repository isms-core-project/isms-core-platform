"""Phase 7 — generator_definitions table.

Revision ID: 003_phase7_generators
Revises: 002_phase6_external
Create Date: 2026-03-07

Changes:
  1. CREATE TABLE generator_definitions
     Stores structural metadata extracted from 188 QA'd generator scripts.
     One row per generator file (document_id is the unique key).
"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision = "003_phase7_generators"
down_revision = "002_phase6_external"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "generator_definitions",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("document_id", sa.String(80), nullable=False),
        sa.Column("workbook_name", sa.String(200), nullable=False),
        sa.Column("control_id", sa.String(80), nullable=False),
        sa.Column("control_name", sa.String(300), nullable=False),
        sa.Column("group_code", sa.String(80), nullable=False),
        sa.Column("control_group_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("domain_number", sa.Integer(), nullable=True),
        sa.Column("domain_total", sa.Integer(), nullable=True),
        sa.Column("is_stacked", sa.Boolean(), nullable=False, server_default="false"),
        sa.Column(
            "stacked_control_ids",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column(
            "sheets",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
            server_default="[]",
        ),
        sa.Column("sheet_count", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("sheet_source", sa.String(20), nullable=True),
        sa.Column("source_file", sa.Text(), nullable=True),
        sa.Column("parsed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["control_group_id"],
            ["control_groups.id"],
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("document_id"),
    )
    op.create_index(
        "ix_generator_definitions_group_code",
        "generator_definitions",
        ["group_code"],
    )
    op.create_index(
        "ix_generator_definitions_control_group_id",
        "generator_definitions",
        ["control_group_id"],
    )


def downgrade():
    op.drop_index("ix_generator_definitions_control_group_id", "generator_definitions")
    op.drop_index("ix_generator_definitions_group_code", "generator_definitions")
    op.drop_table("generator_definitions")
