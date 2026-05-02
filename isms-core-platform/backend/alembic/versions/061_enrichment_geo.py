"""Add maxmind and ipinfo columns to ti_enrichment_cache.

Revision ID: 061
Revises: 060
Create Date: 2026-05-02
"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB

revision = "061"
down_revision = "060"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("ti_enrichment_cache", sa.Column("maxmind",           JSONB(),                    nullable=True))
    op.add_column("ti_enrichment_cache", sa.Column("ipinfo",            JSONB(),                    nullable=True))
    op.add_column("ti_enrichment_cache", sa.Column("maxmind_cached_at", sa.DateTime(timezone=True), nullable=True))
    op.add_column("ti_enrichment_cache", sa.Column("ipinfo_cached_at",  sa.DateTime(timezone=True), nullable=True))


def downgrade() -> None:
    op.drop_column("ti_enrichment_cache", "ipinfo_cached_at")
    op.drop_column("ti_enrichment_cache", "maxmind_cached_at")
    op.drop_column("ti_enrichment_cache", "ipinfo")
    op.drop_column("ti_enrichment_cache", "maxmind")
