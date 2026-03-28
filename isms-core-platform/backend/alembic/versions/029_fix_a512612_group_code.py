"""Fix A.5.1-2-6.1-2 control group: correct group_code and stacked_control_ids

group_code was incorrectly set to 'a.5.1-2' (missing the cross-section suffix).
stacked_control_ids was missing A.6.1 and A.6.2 (they were only in also_covers
in the dataset, but also_covers is not persisted to the DB column).

Revision ID: 029_fix_a512612
Revises: 028_project_inactive
Create Date: 2026-03-28
"""
from alembic import op

revision = "029_fix_a512612"
down_revision = "028_project_inactive"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        UPDATE control_groups
        SET
            group_code = 'a.5.1-2-6.1-2',
            stacked_control_ids = ARRAY['A.5.1', 'A.5.2', 'A.6.1', 'A.6.2']
        WHERE group_code = 'a.5.1-2'
    """)


def downgrade() -> None:
    op.execute("""
        UPDATE control_groups
        SET
            group_code = 'a.5.1-2',
            stacked_control_ids = ARRAY['A.5.1', 'A.5.2']
        WHERE group_code = 'a.5.1-2-6.1-2'
    """)
