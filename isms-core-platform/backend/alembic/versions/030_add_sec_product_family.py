"""Add SEC to ProductType and ProductFamily enums (ISO 27017:2025)

Revision ID: 030_add_sec_product
Revises: 029_fix_a512612
Create Date: 2026-04-02
"""
from alembic import op

revision = "030_add_sec_product"
down_revision = "029_fix_a512612"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TYPE product_type ADD VALUE IF NOT EXISTS 'sec'")
    op.execute("ALTER TYPE productfamily ADD VALUE IF NOT EXISTS 'SEC'")


def downgrade() -> None:
    # Postgres does not support removing enum values — downgrade is a no-op.
    # To fully revert: drop and recreate the enum types (destructive, manual step).
    pass
