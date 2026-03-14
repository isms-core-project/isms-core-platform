"""Add product_type column to generator_definitions.

Revision ID: 016_generator_product_type
Revises: 015_privacy_groups
"""

from alembic import op
import sqlalchemy as sa

revision = "016_generator_product_type"
down_revision = "015_privacy_groups"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "generator_definitions",
        sa.Column(
            "product_type",
            sa.String(20),
            nullable=False,
            server_default="framework",
        ),
    )
    op.create_index(
        "ix_generator_definitions_product_type",
        "generator_definitions",
        ["product_type"],
    )


def downgrade() -> None:
    op.drop_index(
        "ix_generator_definitions_product_type",
        table_name="generator_definitions",
    )
    op.drop_column("generator_definitions", "product_type")
