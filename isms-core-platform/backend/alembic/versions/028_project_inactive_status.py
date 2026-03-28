"""Add 'inactive' value to project_status enum + lib_checklist_id to project_checklists

Revision ID: 028_project_inactive
Revises: 027_projects
Create Date: 2026-03-28
"""
from alembic import op

revision = "028_project_inactive"
down_revision = "027_projects"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add 'inactive' to project_status enum
    # PostgreSQL allows adding values to existing enums without recreating them
    op.execute("ALTER TYPE project_status ADD VALUE IF NOT EXISTS 'inactive'")

    # Add lib_checklist_id to project_checklists (tracks which library SCR was cloned)
    op.execute("""
        ALTER TABLE project_checklists
        ADD COLUMN IF NOT EXISTS lib_checklist_id UUID REFERENCES assessments(id) ON DELETE SET NULL
    """)
    op.execute("""
        CREATE INDEX IF NOT EXISTS ix_project_checklists_lib_checklist_id
        ON project_checklists(lib_checklist_id)
    """)


def downgrade() -> None:
    # PostgreSQL does not support removing enum values — downgrade is a no-op for the enum
    op.execute("ALTER TABLE project_checklists DROP COLUMN IF EXISTS lib_checklist_id")
