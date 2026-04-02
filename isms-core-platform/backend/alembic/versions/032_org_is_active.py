"""Add is_active to organisations table.

Revision ID: 032_org_is_active
Revises: 031_multi_org
"""

import sqlalchemy as sa
from alembic import op

revision = "032_org_is_active"
down_revision = "031_multi_org"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "organisations",
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default="true"),
    )


def downgrade():
    op.drop_column("organisations", "is_active")
