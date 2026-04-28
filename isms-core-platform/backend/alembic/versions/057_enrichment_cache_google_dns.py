"""Add google_dns column to ti_enrichment_cache.

Revision ID: 057
Revises: 056
Create Date: 2026-04-26
"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB

revision = "057"
down_revision = "056"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "ti_enrichment_cache",
        sa.Column("google_dns", JSONB(), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("ti_enrichment_cache", "google_dns")
