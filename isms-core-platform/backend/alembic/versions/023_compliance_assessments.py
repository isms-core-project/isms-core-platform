"""Add generic compliance_assessments and compliance_ratings tables (NIS2, DORA, extensible).

Revision ID: 023_compliance_assessments
Revises: 022_nist_csf_profiles
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision = "023_compliance_assessments"
down_revision = "022_nist_csf_profiles"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "compliance_assessments",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("framework_code", sa.String(20), nullable=False),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("assessor", sa.String(100), nullable=True),
        sa.Column("scope", sa.Text(), nullable=True),
        sa.Column("organisation", sa.String(200), nullable=True),
        sa.Column("status", sa.String(20), nullable=False, server_default="draft"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    )
    op.create_check_constraint(
        "ck_compliance_assessment_status",
        "compliance_assessments",
        "status IN ('draft', 'in_progress', 'complete')",
    )
    op.create_index("ix_compliance_assessments_framework", "compliance_assessments", ["framework_code"])

    op.create_table(
        "compliance_ratings",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column(
            "assessment_id",
            UUID(as_uuid=True),
            sa.ForeignKey("compliance_assessments.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "requirement_id",
            UUID(as_uuid=True),
            sa.ForeignKey("framework_controls.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("current_score", sa.SmallInteger(), nullable=True),
        sa.Column("target_score", sa.SmallInteger(), nullable=True),
        sa.Column("rating_status", sa.String(20), nullable=False, server_default="not_assessed"),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("evidence_ref", sa.String(500), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.UniqueConstraint("assessment_id", "requirement_id", name="uq_compliance_rating_assessment_req"),
    )
    op.create_index("ix_compliance_ratings_assessment_id", "compliance_ratings", ["assessment_id"])
    op.create_check_constraint(
        "ck_compliance_rating_current_score",
        "compliance_ratings",
        "current_score IS NULL OR (current_score >= 0 AND current_score <= 4)",
    )
    op.create_check_constraint(
        "ck_compliance_rating_target_score",
        "compliance_ratings",
        "target_score IS NULL OR (target_score >= 0 AND target_score <= 4)",
    )
    op.create_check_constraint(
        "ck_compliance_rating_status",
        "compliance_ratings",
        "rating_status IN ('not_assessed', 'not_applicable', 'non_compliant', 'partial', 'compliant')",
    )

    op.execute("""
        CREATE TRIGGER trg_compliance_assessments_updated_at
        BEFORE UPDATE ON compliance_assessments
        FOR EACH ROW EXECUTE FUNCTION update_updated_at();
    """)
    op.execute("""
        CREATE TRIGGER trg_compliance_ratings_updated_at
        BEFORE UPDATE ON compliance_ratings
        FOR EACH ROW EXECUTE FUNCTION update_updated_at();
    """)


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS trg_compliance_ratings_updated_at ON compliance_ratings;")
    op.execute("DROP TRIGGER IF EXISTS trg_compliance_assessments_updated_at ON compliance_assessments;")
    op.drop_table("compliance_ratings")
    op.drop_table("compliance_assessments")
