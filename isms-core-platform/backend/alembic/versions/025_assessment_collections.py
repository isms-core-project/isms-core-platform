"""assessment_collections tables

Revision ID: 025_assessment_collections
Revises: 024_privacy_foundation_group
Create Date: 2026-03-26
"""
from alembic import op

revision = "025_assessment_collections"
down_revision = "024_privacy_foundation_group"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE assessment_collections (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            name VARCHAR(255) NOT NULL,
            description TEXT,
            product_family VARCHAR(20) NOT NULL,
            product_type VARCHAR(20),
            due_date DATE,
            created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
        )
    """)
    op.execute("""
        CREATE TABLE collection_assessments (
            collection_id UUID NOT NULL REFERENCES assessment_collections(id) ON DELETE CASCADE,
            assessment_id UUID NOT NULL REFERENCES assessments(id) ON DELETE CASCADE,
            added_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
            PRIMARY KEY (collection_id, assessment_id)
        )
    """)
    op.execute("""
        CREATE TRIGGER update_assessment_collections_updated_at
        BEFORE UPDATE ON assessment_collections
        FOR EACH ROW EXECUTE FUNCTION update_updated_at()
    """)


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS collection_assessments")
    op.execute("DROP TABLE IF EXISTS assessment_collections")
