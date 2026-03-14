"""Add INS policy type and 00-Foundation Policies control group.

Revision ID: 001_foundation
Revises:
Create Date: 2026-03-01

Changes:
  1. ALTER TYPE policy_type ADD VALUE 'INS'  (must run outside transaction)
  2. INSERT control_groups row for "00 - Foundation Policies"
"""

import uuid

import sqlalchemy as sa
from alembic import op

revision = "001_foundation"
down_revision = None
branch_labels = None
depends_on = None

# Deterministic UUID for the foundation control group
_FOUNDATION_ID = str(uuid.uuid5(uuid.NAMESPACE_DNS, "isms-core.control-group.00-foundation"))


def upgrade():
    # ADD VALUE cannot run inside a transaction in PostgreSQL
    with op.get_context().autocommit_block():
        op.execute(sa.text("ALTER TYPE policy_type ADD VALUE IF NOT EXISTS 'INS'"))

    # Insert the foundation policies control group (idempotent via ON CONFLICT)
    op.execute(
        sa.text(
            """
            INSERT INTO control_groups (
                id, group_code, name, section, section_name,
                folder_name, is_stacked, has_framework, has_operational,
                framework_status, operational_status, metadata,
                created_at, updated_at
            ) VALUES (
                :id, '00', 'Foundation Policies', '00', 'Foundation Policies',
                '00-foundation-policies', false, true, false,
                'complete', 'incomplete', '{}',
                now(), now()
            )
            ON CONFLICT (group_code) DO NOTHING
            """
        ).bindparams(id=_FOUNDATION_ID)
    )


def downgrade():
    op.execute(
        sa.text("DELETE FROM control_groups WHERE group_code = '00'")
    )
    # Note: PostgreSQL does not support removing enum values.
    # The 'INS' value in policy_type must be removed manually if required.
