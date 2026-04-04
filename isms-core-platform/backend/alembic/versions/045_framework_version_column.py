"""Widen frameworks.version from VARCHAR(20) to VARCHAR(100).

Revision ID: 045
Revises: 044
Create Date: 2026-04-04

VARCHAR(20) was too narrow for framework versions like
'Rundschreiben 10/2021' (21 chars) and 'PS21/3 + PS7/26' etc.
Widened to VARCHAR(100) to accommodate all current and future framework versions.
"""

from alembic import op
import sqlalchemy as sa

revision = '045'
down_revision = '044'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'frameworks', 'version',
        existing_type=sa.String(20),
        type_=sa.String(100),
        existing_nullable=True,
    )


def downgrade():
    op.alter_column(
        'frameworks', 'version',
        existing_type=sa.String(100),
        type_=sa.String(20),
        existing_nullable=True,
    )
