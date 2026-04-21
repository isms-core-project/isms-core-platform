"""Add euvd_vulnerabilities table.

Revision ID: 052
Revises: 051
Create Date: 2026-04-21
"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB

revision = "052"
down_revision = "051"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "euvd_vulnerabilities",
        sa.Column("id",                 sa.UUID(),                    nullable=False),
        sa.Column("euvd_id",            sa.String(50),                nullable=False),
        sa.Column("cve_id",             sa.String(30),                nullable=True),
        sa.Column("description",        sa.Text(),                    nullable=True),
        sa.Column("date_published",     sa.DateTime(timezone=True),   nullable=True),
        sa.Column("date_updated",       sa.DateTime(timezone=True),   nullable=True),
        sa.Column("base_score",         sa.Float(),                   nullable=True),
        sa.Column("base_score_version", sa.String(10),                nullable=True),
        sa.Column("base_score_vector",  sa.String(200),               nullable=True),
        sa.Column("epss_score",         sa.Float(),                   nullable=True),
        sa.Column("assigner",           sa.String(200),               nullable=True),
        sa.Column("is_exploited",       sa.Boolean(),                 nullable=False, server_default="false"),
        sa.Column("is_critical",        sa.Boolean(),                 nullable=False, server_default="false"),
        sa.Column("aliases",            JSONB(),                      nullable=True),
        sa.Column("cve_ids",            JSONB(),                      nullable=True),
        sa.Column("vendors",            JSONB(),                      nullable=True),
        sa.Column("products",           JSONB(),                      nullable=True),
        sa.Column("created_at",         sa.DateTime(timezone=True),   nullable=False),
        sa.Column("updated_at",         sa.DateTime(timezone=True),   nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("euvd_id"),
    )
    op.create_index("ix_euvd_cve_id",          "euvd_vulnerabilities", ["cve_id"])
    op.create_index("ix_euvd_is_exploited",     "euvd_vulnerabilities", ["is_exploited"])
    op.create_index("ix_euvd_base_score",       "euvd_vulnerabilities", ["base_score"])
    op.create_index("ix_euvd_date_published",   "euvd_vulnerabilities", ["date_published"])


def downgrade() -> None:
    op.drop_table("euvd_vulnerabilities")
