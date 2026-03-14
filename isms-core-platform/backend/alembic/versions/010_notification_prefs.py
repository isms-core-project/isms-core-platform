"""Add notification_prefs JSONB to users table.

Revision ID: 010_notification_prefs
Revises: 009_audit_log_phase9
Create Date: 2026-03-08
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = "010_notification_prefs"
down_revision = "009_audit_log_phase9"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "notification_prefs",
            JSONB,
            nullable=False,
            server_default="{}",
        ),
    )


def downgrade() -> None:
    op.drop_column("users", "notification_prefs")
