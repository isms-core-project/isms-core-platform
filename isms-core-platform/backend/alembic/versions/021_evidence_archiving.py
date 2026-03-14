"""Add archived_at to connector_evidence + evidence_retention_days to connectors.

Revision ID: 021_evidence_archiving
Revises: 020_connector_last_error
"""

from alembic import op
import sqlalchemy as sa

revision = "021_evidence_archiving"
down_revision = "020_connector_last_error"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Soft-archive column on connector_evidence
    op.add_column("connector_evidence", sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True))
    op.create_index("ix_connector_evidence_archived_at", "connector_evidence", ["archived_at"])

    # Per-connector retention (days); NULL = use global default (90d)
    op.add_column("connectors", sa.Column("retention_days", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("connectors", "retention_days")
    op.drop_index("ix_connector_evidence_archived_at", table_name="connector_evidence")
    op.drop_column("connector_evidence", "archived_at")
