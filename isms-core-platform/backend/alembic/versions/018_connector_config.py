"""Add config_encrypted column to connectors table.

Revision ID: 018_connector_config
Revises: 017_connector_evidence
"""

from alembic import op
import sqlalchemy as sa

revision = "018_connector_config"
down_revision = "017_connector_evidence"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "connectors",
        sa.Column("config_encrypted", sa.Text(), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("connectors", "config_encrypted")
