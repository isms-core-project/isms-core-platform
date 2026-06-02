"""Clean up old CLD-IMP- records from implementations table after rename.

Migration 067 renamed policies + assessments but missed the implementations
table (separate model). Re-import created new CLD-PII-IMP- records, leaving
old CLD-IMP- records as duplicates. Delete the old ones.

Revision ID: 068_cld_rename_pii_implementations
Revises: 067_cld_rename_pii_prefix
Create Date: 2026-06-02
"""

from alembic import op

revision = "068"
down_revision = "067_cld_rename_pii_prefix"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Remove orphaned old CLD-IMP- records — new CLD-PII-IMP- records already
    # exist from the re-import that followed migration 067.
    op.execute("""
        DELETE FROM implementations
        WHERE document_id LIKE 'CLD-IMP-%'
    """)


def downgrade() -> None:
    # Cannot restore deleted records — downgrade is a no-op.
    pass
