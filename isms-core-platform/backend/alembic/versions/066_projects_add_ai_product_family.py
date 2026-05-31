"""Projects — add AI to product_family check constraint

The projects table check constraint was created in 027_projects with only
('ISMS', 'PRIVACY', 'CLOUD'). AI product family was added later (050+) to
control_groups but the projects constraint was never updated.

Revision ID: 066_projects_add_ai_product_family
Revises: 065_regulatory_assessment_project_id
Create Date: 2026-05-31
"""
from alembic import op

revision = "066"
down_revision = "065"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE projects DROP CONSTRAINT IF EXISTS projects_product_family_check")
    op.execute("""
        ALTER TABLE projects
        ADD CONSTRAINT projects_product_family_check
        CHECK (product_family IN ('ISMS', 'PRIVACY', 'CLOUD', 'AI'))
    """)


def downgrade() -> None:
    op.execute("ALTER TABLE projects DROP CONSTRAINT IF EXISTS projects_product_family_check")
    op.execute("""
        ALTER TABLE projects
        ADD CONSTRAINT projects_product_family_check
        CHECK (product_family IN ('ISMS', 'PRIVACY', 'CLOUD'))
    """)
