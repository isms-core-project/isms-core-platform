"""Add notification_routing table for per-event role routing rules.

Revision ID: 059
Revises: 058
Create Date: 2026-04-30
"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import ARRAY

revision = "059"
down_revision = "058"
branch_labels = None
depends_on = None

_DEFAULTS = [
    # event_type,               target_roles,                                     include_override
    ("email.gap_assigned",      ["admin", "isms_manager", "control_owner"],       False),
    ("email.evidence_expiry",   ["admin", "isms_manager"],                        False),
    ("email.qa_fail",           ["admin", "isms_manager"],                        True),
    ("email.import_completed",  ["admin"],                                         True),
    ("email.feed_failure",      ["admin", "isms_manager"],                        True),
    ("email.ti_feed_failure",   ["admin", "isms_manager"],                        True),
    ("email.connector_failure", ["admin", "isms_manager"],                        True),
]


def upgrade() -> None:
    op.create_table(
        "notification_routing",
        sa.Column("event_type", sa.String(100), primary_key=True),
        sa.Column(
            "target_roles",
            ARRAY(sa.String(50)),
            nullable=False,
            server_default="{}",
        ),
        sa.Column("always_include_override", sa.Boolean, nullable=False, server_default="false"),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )

    op.bulk_insert(
        sa.table(
            "notification_routing",
            sa.column("event_type", sa.String),
            sa.column("target_roles", ARRAY(sa.String)),
            sa.column("always_include_override", sa.Boolean),
        ),
        [
            {"event_type": et, "target_roles": roles, "always_include_override": override}
            for et, roles, override in _DEFAULTS
        ],
    )


def downgrade() -> None:
    op.drop_table("notification_routing")
