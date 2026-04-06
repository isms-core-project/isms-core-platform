"""Platform settings key-value store.

Revision ID: 048
Revises: 047
Create Date: 2026-04-06

Changes:
  - Add platform_settings table (key TEXT PK, value TEXT, updated_at TIMESTAMPTZ)
"""

from alembic import op
import sqlalchemy as sa

revision = '048'
down_revision = '047'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'platform_settings',
        sa.Column('key', sa.String(100), primary_key=True),
        sa.Column('value', sa.Text, nullable=False, server_default=''),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )


def downgrade():
    op.drop_table('platform_settings')
