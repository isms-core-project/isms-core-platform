"""Add connectors and connector_evidence tables for v2.0 automated evidence.

Revision ID: 017_connector_evidence
Revises: 016_generator_product_type
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB, UUID

revision = "017_connector_evidence"
down_revision = "016_generator_product_type"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # connectors — registry of active connectors + their scoped API tokens
    op.create_table(
        "connectors",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("source_system", sa.String(50), nullable=False),  # entra_id, defender, panw, etc.
        sa.Column("api_token_hash", sa.String(255), nullable=True),
        sa.Column("last_run", sa.DateTime(timezone=True), nullable=True),
        sa.Column("last_item_count", sa.Integer(), nullable=True),
        sa.Column("status", sa.String(20), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    )
    op.create_index("ix_connectors_source_system", "connectors", ["source_system"])

    # connector_evidence — evidence items ingested by connectors
    op.create_table(
        "connector_evidence",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("connector_id", UUID(as_uuid=True), sa.ForeignKey("connectors.id", ondelete="CASCADE"), nullable=False),
        sa.Column("control_group_id", UUID(as_uuid=True), sa.ForeignKey("control_groups.id", ondelete="CASCADE"), nullable=False),
        sa.Column("source_ref", sa.String(200), nullable=True),    # INC0012345, CVE-2024-1234, user@domain
        sa.Column("source_url", sa.String(500), nullable=True),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("classification", sa.String(50), nullable=True),  # incident, change, asset, user, vulnerability, network
        sa.Column("status", sa.String(50), nullable=True),
        sa.Column("event_date", sa.DateTime(timezone=True), nullable=True),
        sa.Column("raw", JSONB, nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.UniqueConstraint("connector_id", "source_ref", name="uq_connector_evidence_ref"),
    )
    op.create_index("ix_connector_evidence_control_group", "connector_evidence", ["control_group_id"])
    op.create_index("ix_connector_evidence_connector", "connector_evidence", ["connector_id"])
    op.create_index("ix_connector_evidence_event_date", "connector_evidence", ["event_date"])

    # Trigger to keep connectors.updated_at current
    op.execute("""
        CREATE TRIGGER trg_connectors_updated_at
        BEFORE UPDATE ON connectors
        FOR EACH ROW EXECUTE FUNCTION update_updated_at();
    """)


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS trg_connectors_updated_at ON connectors;")
    op.drop_table("connector_evidence")
    op.drop_table("connectors")
