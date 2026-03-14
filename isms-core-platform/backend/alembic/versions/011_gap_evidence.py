"""Add gap_evidence junction table for Gap → Evidence linking.

Revision ID: 011_gap_evidence
Revises: 010_notification_prefs
Create Date: 2026-03-09
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision = "011_gap_evidence"
down_revision = "010_notification_prefs"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "gap_evidence",
        sa.Column(
            "gap_id",
            UUID(as_uuid=True),
            sa.ForeignKey("gaps.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column(
            "evidence_id",
            UUID(as_uuid=True),
            sa.ForeignKey("evidence.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column(
            "linked_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    op.create_index("ix_gap_evidence_gap_id", "gap_evidence", ["gap_id"])
    op.create_index("ix_gap_evidence_evidence_id", "gap_evidence", ["evidence_id"])


def downgrade():
    op.drop_index("ix_gap_evidence_evidence_id", table_name="gap_evidence")
    op.drop_index("ix_gap_evidence_gap_id", table_name="gap_evidence")
    op.drop_table("gap_evidence")
