"""Add sync_requested_at column to connectors table.

Revision ID: 019_connector_sync
Revises: 018_connector_config
"""

from alembic import op
import sqlalchemy as sa

revision = "019_connector_sync"
down_revision = "018_connector_config"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "connectors",
        sa.Column("sync_requested_at", sa.DateTime(timezone=True), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("connectors", "sync_requested_at")
