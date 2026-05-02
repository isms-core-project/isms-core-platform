"""Add tlp column to ti_iocs.

Revision ID: 062
Revises: 061
Create Date: 2026-05-02
"""

import sqlalchemy as sa
from alembic import op

revision = "062"
down_revision = "061"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("ti_iocs", sa.Column("tlp", sa.String(10), nullable=True))
    op.create_index("ix_ti_iocs_tlp", "ti_iocs", ["tlp"])


def downgrade() -> None:
    op.drop_index("ix_ti_iocs_tlp", table_name="ti_iocs")
    op.drop_column("ti_iocs", "tlp")
