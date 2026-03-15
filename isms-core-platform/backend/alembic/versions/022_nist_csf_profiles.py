"""Add nist_csf_profiles and nist_csf_ratings tables.

Revision ID: 022_nist_csf_profiles
Revises: 021_evidence_archiving
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision = "022_nist_csf_profiles"
down_revision = "021_evidence_archiving"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # nist_csf_profiles — named assessment profiles
    op.create_table(
        "nist_csf_profiles",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("assessor", sa.String(100), nullable=True),
        sa.Column("scope", sa.Text(), nullable=True),
        sa.Column("status", sa.String(20), nullable=False, server_default="draft"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    )
    op.create_check_constraint(
        "ck_nist_profile_status",
        "nist_csf_profiles",
        "status IN ('draft', 'in_progress', 'complete')",
    )

    # nist_csf_ratings — one row per subcategory per profile
    op.create_table(
        "nist_csf_ratings",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column(
            "profile_id",
            UUID(as_uuid=True),
            sa.ForeignKey("nist_csf_profiles.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "subcategory_id",
            UUID(as_uuid=True),
            sa.ForeignKey("framework_controls.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("current_tier", sa.SmallInteger(), nullable=True),
        sa.Column("target_tier", sa.SmallInteger(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.UniqueConstraint("profile_id", "subcategory_id", name="uq_nist_rating_profile_subcategory"),
    )
    op.create_index("ix_nist_csf_ratings_profile_id", "nist_csf_ratings", ["profile_id"])
    op.create_check_constraint(
        "ck_nist_rating_current_tier",
        "nist_csf_ratings",
        "current_tier IS NULL OR (current_tier >= 1 AND current_tier <= 4)",
    )
    op.create_check_constraint(
        "ck_nist_rating_target_tier",
        "nist_csf_ratings",
        "target_tier IS NULL OR (target_tier >= 1 AND target_tier <= 4)",
    )

    # Triggers to keep updated_at current
    op.execute("""
        CREATE TRIGGER trg_nist_csf_profiles_updated_at
        BEFORE UPDATE ON nist_csf_profiles
        FOR EACH ROW EXECUTE FUNCTION update_updated_at();
    """)
    op.execute("""
        CREATE TRIGGER trg_nist_csf_ratings_updated_at
        BEFORE UPDATE ON nist_csf_ratings
        FOR EACH ROW EXECUTE FUNCTION update_updated_at();
    """)


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS trg_nist_csf_ratings_updated_at ON nist_csf_ratings;")
    op.execute("DROP TRIGGER IF EXISTS trg_nist_csf_profiles_updated_at ON nist_csf_profiles;")
    op.drop_table("nist_csf_ratings")
    op.drop_table("nist_csf_profiles")
