"""CSRM (Swiss NCSC Cyber Security Risk Management) tables

Revision ID: 026_csrm
Revises: 025_assessment_collections
Create Date: 2026-03-26
"""
from alembic import op

revision = "026_csrm"
down_revision = "025_assessment_collections"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE csrm_assessments (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            name VARCHAR(200) NOT NULL,
            description TEXT,
            organisation VARCHAR(200),
            assessor VARCHAR(100),
            scope TEXT,
            status VARCHAR(20) NOT NULL DEFAULT 'draft'
                CHECK (status IN ('draft', 'in_progress', 'complete')),
            created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)

    op.execute("""
        CREATE TABLE csrm_protection_objects (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            assessment_id UUID NOT NULL REFERENCES csrm_assessments(id) ON DELETE CASCADE,
            name VARCHAR(200) NOT NULL,
            description TEXT,
            architecture_notes TEXT,
            processes_served TEXT,
            data_classification VARCHAR(50) DEFAULT 'standard',
            protection_level VARCHAR(20) NOT NULL DEFAULT 'standard'
                CHECK (protection_level IN ('standard', 'elevated')),
            elevated_rationale TEXT,
            sort_order INTEGER NOT NULL DEFAULT 0,
            created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)

    op.execute("""
        CREATE INDEX ix_csrm_protection_objects_assessment_id ON csrm_protection_objects(assessment_id)
    """)

    op.execute("""
        CREATE TABLE csrm_baseline_ratings (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            assessment_id UUID NOT NULL REFERENCES csrm_assessments(id) ON DELETE CASCADE,
            object_id UUID NOT NULL REFERENCES csrm_protection_objects(id) ON DELETE CASCADE,
            requirement_id VARCHAR(10) NOT NULL,
            status VARCHAR(20) NOT NULL DEFAULT 'not_assessed'
                CHECK (status IN ('not_assessed', 'met', 'partial', 'not_met', 'exception')),
            exception_justification TEXT,
            notes TEXT,
            updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
            CONSTRAINT uq_csrm_baseline_rating UNIQUE (object_id, requirement_id)
        )
    """)

    op.execute("""
        CREATE INDEX ix_csrm_baseline_ratings_assessment_id ON csrm_baseline_ratings(assessment_id)
    """)

    op.execute("""
        CREATE INDEX ix_csrm_baseline_ratings_object_id ON csrm_baseline_ratings(object_id)
    """)

    op.execute("""
        CREATE TABLE csrm_elevated_toms (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            assessment_id UUID NOT NULL REFERENCES csrm_assessments(id) ON DELETE CASCADE,
            object_id UUID NOT NULL REFERENCES csrm_protection_objects(id) ON DELETE CASCADE,
            threat_category VARCHAR(100) NOT NULL,
            tom_description TEXT NOT NULL,
            status VARCHAR(20) NOT NULL DEFAULT 'planned'
                CHECK (status IN ('planned', 'in_progress', 'implemented', 'not_applicable')),
            notes TEXT,
            created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)

    op.execute("""
        CREATE INDEX ix_csrm_elevated_toms_object_id ON csrm_elevated_toms(object_id)
    """)

    op.execute("""
        CREATE OR REPLACE FUNCTION update_csrm_updated_at()
        RETURNS TRIGGER AS $$
        BEGIN NEW.updated_at = now(); RETURN NEW; END;
        $$ LANGUAGE plpgsql
    """)

    op.execute("""
        CREATE TRIGGER trg_csrm_assessments_updated_at
        BEFORE UPDATE ON csrm_assessments
        FOR EACH ROW EXECUTE FUNCTION update_csrm_updated_at()
    """)

    op.execute("""
        CREATE TRIGGER trg_csrm_protection_objects_updated_at
        BEFORE UPDATE ON csrm_protection_objects
        FOR EACH ROW EXECUTE FUNCTION update_csrm_updated_at()
    """)

    op.execute("""
        CREATE TRIGGER trg_csrm_baseline_ratings_updated_at
        BEFORE UPDATE ON csrm_baseline_ratings
        FOR EACH ROW EXECUTE FUNCTION update_csrm_updated_at()
    """)

    op.execute("""
        CREATE TRIGGER trg_csrm_elevated_toms_updated_at
        BEFORE UPDATE ON csrm_elevated_toms
        FOR EACH ROW EXECUTE FUNCTION update_csrm_updated_at()
    """)


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS csrm_elevated_toms")
    op.execute("DROP TABLE IF EXISTS csrm_baseline_ratings")
    op.execute("DROP TABLE IF EXISTS csrm_protection_objects")
    op.execute("DROP TABLE IF EXISTS csrm_assessments")
    op.execute("DROP FUNCTION IF EXISTS update_csrm_updated_at()")
