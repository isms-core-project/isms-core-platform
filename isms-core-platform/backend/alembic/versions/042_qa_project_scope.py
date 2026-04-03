"""Phase 21 — QA Engine v2: add project_id, reference_library, result_view to correlation_results.

Revision ID: 042
Revises: 041
Create Date: 2026-04-03

Adds three nullable columns to correlation_results:
  - project_id      UUID → projects.id  (NULL = org-level/global run, backward-compat)
  - reference_library VARCHAR(20)        ('iso_corpus' | 'isms_library' | 'both' | 'crosswalk')
  - result_view      VARCHAR(20)         ('document' | 'control_group', default 'control_group')
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision = "042"
down_revision = "041"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "correlation_results",
        sa.Column(
            "project_id",
            UUID(as_uuid=True),
            sa.ForeignKey("projects.id", ondelete="CASCADE"),
            nullable=True,
        ),
    )
    op.add_column(
        "correlation_results",
        sa.Column("reference_library", sa.String(20), nullable=True),
    )
    op.add_column(
        "correlation_results",
        sa.Column(
            "result_view",
            sa.String(20),
            nullable=False,
            server_default="control_group",
        ),
    )
    op.create_index(
        "ix_correlation_results_project_id",
        "correlation_results",
        ["project_id"],
    )


def downgrade() -> None:
    op.drop_index("ix_correlation_results_project_id", table_name="correlation_results")
    op.drop_column("correlation_results", "result_view")
    op.drop_column("correlation_results", "reference_library")
    op.drop_column("correlation_results", "project_id")
