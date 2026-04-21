"""Add is_eu_assigned column to euvd_vulnerabilities.

Revision ID: 053
Revises: 052
Create Date: 2026-04-21
"""

import sqlalchemy as sa
from alembic import op

revision = "053"
down_revision = "052"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "euvd_vulnerabilities",
        sa.Column("is_eu_assigned", sa.Boolean(), nullable=False, server_default="false"),
    )
    op.create_index("ix_euvd_is_eu_assigned", "euvd_vulnerabilities", ["is_eu_assigned"])


def downgrade() -> None:
    op.drop_index("ix_euvd_is_eu_assigned", table_name="euvd_vulnerabilities")
    op.drop_column("euvd_vulnerabilities", "is_eu_assigned")
