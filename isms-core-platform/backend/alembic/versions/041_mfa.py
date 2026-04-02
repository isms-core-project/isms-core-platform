"""Phase MFA — add TOTP MFA fields to users table.

Revision ID: 041
Revises: 040
Create Date: 2026-04-02
"""
from alembic import op

revision = '041'
down_revision = '040'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        ALTER TABLE users
            ADD COLUMN IF NOT EXISTS mfa_enabled     BOOLEAN NOT NULL DEFAULT FALSE,
            ADD COLUMN IF NOT EXISTS mfa_secret      TEXT,
            ADD COLUMN IF NOT EXISTS mfa_backup_codes JSONB NOT NULL DEFAULT '[]'
    """)


def downgrade():
    op.execute("""
        ALTER TABLE users
            DROP COLUMN IF EXISTS mfa_enabled,
            DROP COLUMN IF EXISTS mfa_secret,
            DROP COLUMN IF EXISTS mfa_backup_codes
    """)
