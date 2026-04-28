"""TI feed expansion — actor_type column + ti_tools table.

Revision ID: 056
Revises: 055
Create Date: 2026-04-26
"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB, UUID

revision = "056"
down_revision = "055"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Distinguish threat actors from ransomware groups (same table, different type)
    op.add_column(
        "ti_actors",
        sa.Column("actor_type", sa.String(30), nullable=False, server_default="threat-actor"),
    )
    op.create_index("ix_ti_actors_type", "ti_actors", ["actor_type"])

    # Attacker tooling from MISP galaxy tool.json
    op.create_table(
        "ti_tools",
        sa.Column("id",          UUID(),                     nullable=False),
        sa.Column("slug",        sa.String(200),             nullable=False),
        sa.Column("name",        sa.String(200),             nullable=False),
        sa.Column("aliases",     JSONB(),                    nullable=False, server_default=sa.text("'[]'")),
        sa.Column("description", sa.Text(),                  nullable=True),
        sa.Column("mitre_tids",  JSONB(),                    nullable=False, server_default=sa.text("'[]'")),
        sa.Column("updated_at",  sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    op.create_index("ix_ti_tools_name", "ti_tools", ["name"])


def downgrade() -> None:
    op.drop_table("ti_tools")
    op.drop_index("ix_ti_actors_type", table_name="ti_actors")
    op.drop_column("ti_actors", "actor_type")
