"""Add vt_checked_at to ti_iocs for VirusTotal enrichment tracking.

Revision ID: 063
Revises: 062
Create Date: 2026-05-02
"""

import sqlalchemy as sa
from alembic import op

revision = "063"
down_revision = "062"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("ti_iocs", sa.Column("vt_checked_at", sa.DateTime(timezone=True), nullable=True))
    op.create_index("ix_ti_iocs_vt_checked_at", "ti_iocs", ["vt_checked_at"])


def downgrade() -> None:
    op.drop_index("ix_ti_iocs_vt_checked_at", table_name="ti_iocs")
    op.drop_column("ti_iocs", "vt_checked_at")
