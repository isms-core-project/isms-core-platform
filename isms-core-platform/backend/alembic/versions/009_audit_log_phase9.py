"""Phase 9 — extend audit_log table for full audit trail.

Renames existing columns to match the Phase 9 schema and adds:
  - event_type  (replaces action, VARCHAR 60)
  - category    ('security' | 'workflow' | 'system')
  - severity    ('info' | 'warning' | 'error' | 'critical')
  - actor_email (denormalised — no join needed on log queries)
  - description (human-readable text)
  - target_type (replaces resource_type)
  - target_id   (replaces resource_id)
  - metadata_   (replaces details)

Revision ID: 009
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB, UUID

revision = "009_audit_log_phase9"
down_revision = "008_edit_source"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # --- Rename existing columns ---
    op.alter_column("audit_log", "action",        new_column_name="event_type")
    op.alter_column("audit_log", "resource_type", new_column_name="target_type")
    op.alter_column("audit_log", "resource_id",   new_column_name="target_id")
    op.alter_column("audit_log", "details",       new_column_name="metadata_")

    # --- Widen event_type from VARCHAR(30) → VARCHAR(60) ---
    op.alter_column(
        "audit_log", "event_type",
        existing_type=sa.String(30),
        type_=sa.String(60),
        nullable=False,
    )

    # --- Widen target_type from VARCHAR(30) → VARCHAR(50) ---
    op.alter_column(
        "audit_log", "target_type",
        existing_type=sa.String(30),
        type_=sa.String(50),
        nullable=True,
    )

    # --- Add new columns ---
    op.add_column(
        "audit_log",
        sa.Column(
            "category",
            sa.String(20),
            nullable=False,
            server_default="system",
        ),
    )
    op.add_column(
        "audit_log",
        sa.Column(
            "severity",
            sa.String(10),
            nullable=False,
            server_default="info",
        ),
    )
    op.add_column(
        "audit_log",
        sa.Column("actor_email", sa.String(255), nullable=True),
    )
    op.add_column(
        "audit_log",
        sa.Column("description", sa.Text, nullable=True),
    )

    # --- Index for common query patterns ---
    op.create_index("ix_audit_log_event_type", "audit_log", ["event_type"])
    op.create_index("ix_audit_log_category",   "audit_log", ["category"])
    op.create_index("ix_audit_log_severity",   "audit_log", ["severity"])
    op.create_index("ix_audit_log_created_at", "audit_log", ["created_at"])


def downgrade() -> None:
    op.drop_index("ix_audit_log_created_at", "audit_log")
    op.drop_index("ix_audit_log_severity",   "audit_log")
    op.drop_index("ix_audit_log_category",   "audit_log")
    op.drop_index("ix_audit_log_event_type", "audit_log")

    op.drop_column("audit_log", "description")
    op.drop_column("audit_log", "actor_email")
    op.drop_column("audit_log", "severity")
    op.drop_column("audit_log", "category")

    op.alter_column(
        "audit_log", "event_type",
        existing_type=sa.String(60),
        type_=sa.String(30),
        nullable=False,
    )
    op.alter_column(
        "audit_log", "target_type",
        existing_type=sa.String(50),
        type_=sa.String(30),
        nullable=True,
    )

    op.alter_column("audit_log", "metadata_",   new_column_name="details")
    op.alter_column("audit_log", "target_id",   new_column_name="resource_id")
    op.alter_column("audit_log", "target_type", new_column_name="resource_type")
    op.alter_column("audit_log", "event_type",  new_column_name="action")
