"""Add last_error and last_error_at columns to connectors table.

Revision ID: 020_connector_last_error
Revises: 019_connector_sync
"""

from alembic import op
import sqlalchemy as sa

revision = "020_connector_last_error"
down_revision = "019_connector_sync"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("connectors", sa.Column("last_error", sa.Text(), nullable=True))
    op.add_column("connectors", sa.Column("last_error_at", sa.DateTime(timezone=True), nullable=True))


def downgrade() -> None:
    op.drop_column("connectors", "last_error_at")
    op.drop_column("connectors", "last_error")
