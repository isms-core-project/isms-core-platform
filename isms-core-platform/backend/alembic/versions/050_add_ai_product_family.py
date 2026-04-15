"""Add AI to ProductType and ProductFamily enums (ISO 42001:2023)

Adds the enum values needed for the ISMS CORE AI extension pack:
  - product_type: 'ai'
  - productfamily: 'AI'

All existing groups default to 'ISMS'; AI groups are inserted in 051_iso42001_ai_control_groups.

Revision ID: 050
Revises: 049
Create Date: 2026-04-15
"""
import sqlalchemy as sa
from alembic import op

revision = "050"
down_revision = "049"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ALTER TYPE ADD VALUE must be committed before the new values can be used
    # in the same session. Use autocommit_block() to issue and commit immediately.
    with op.get_context().autocommit_block():
        op.execute(sa.text("ALTER TYPE product_type ADD VALUE IF NOT EXISTS 'ai'"))
        op.execute(sa.text("ALTER TYPE productfamily ADD VALUE IF NOT EXISTS 'AI'"))


def downgrade() -> None:
    # PostgreSQL does not support removing enum values — downgrade is a no-op.
    # To fully revert: drop and recreate the enum types (destructive, manual step).
    pass
