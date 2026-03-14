"""Evidence status + nullable control_group_id (bulk draft upload support).

Revision ID: 012_evidence_status
Revises: 011_gap_evidence
Create Date: 2026-03-09
"""

from alembic import op

revision = "012_evidence_status"
down_revision = "011_gap_evidence"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 1. Create the enum type
    op.execute(
        "CREATE TYPE evidence_status AS ENUM "
        "('draft', 'pending_review', 'approved', 'rejected', 'active')"
    )

    # 2. Add evidence_status column (default active — existing records unaffected)
    op.execute(
        "ALTER TABLE evidence "
        "ADD COLUMN evidence_status evidence_status NOT NULL DEFAULT 'active'"
    )

    # 3. Make control_group_id nullable (drafts have no control group yet)
    op.execute(
        "ALTER TABLE evidence "
        "ALTER COLUMN control_group_id DROP NOT NULL"
    )

    # 4. Change ON DELETE CASCADE → SET NULL so drafts survive group deletion
    op.execute(
        "ALTER TABLE evidence "
        "DROP CONSTRAINT IF EXISTS evidence_control_group_id_fkey"
    )
    op.execute(
        "ALTER TABLE evidence "
        "ADD CONSTRAINT evidence_control_group_id_fkey "
        "FOREIGN KEY (control_group_id) REFERENCES control_groups(id) ON DELETE SET NULL"
    )


def downgrade() -> None:
    # Restore NOT NULL (will fail if any draft rows exist — intended)
    op.execute("ALTER TABLE evidence DROP COLUMN IF EXISTS evidence_status")
    op.execute("DROP TYPE IF EXISTS evidence_status")
    op.execute(
        "ALTER TABLE evidence "
        "DROP CONSTRAINT IF EXISTS evidence_control_group_id_fkey"
    )
    op.execute(
        "ALTER TABLE evidence "
        "ADD CONSTRAINT evidence_control_group_id_fkey "
        "FOREIGN KEY (control_group_id) REFERENCES control_groups(id) ON DELETE CASCADE"
    )
    op.execute(
        "ALTER TABLE evidence ALTER COLUMN control_group_id SET NOT NULL"
    )
