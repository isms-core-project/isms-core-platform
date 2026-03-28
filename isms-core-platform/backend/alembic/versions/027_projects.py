"""Projects — Library/Project workspace architecture

Adds the project layer: projects, project_policies, project_implementations,
project_checklists. Adds nullable project_id FK to assessments, assessment_collections,
gaps, evidence, compliance_assessments.

project_id is nullable so existing admin-seeded content remains valid.
New content created via the UI will always carry a project_id.

Revision ID: 027_projects
Revises: 026_csrm
Create Date: 2026-03-28
"""
from alembic import op

revision = "027_projects"
down_revision = "026_csrm"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ── project_status enum ─────────────────────────────────────────────────
    op.execute("CREATE TYPE project_status AS ENUM ('draft', 'active', 'archived')")

    # ── projects ────────────────────────────────────────────────────────────
    op.execute("""
        CREATE TABLE projects (
            id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            name            VARCHAR(255) NOT NULL,
            org_name        VARCHAR(255) NOT NULL,
            product_family  VARCHAR(20)  NOT NULL
                CHECK (product_family IN ('ISMS', 'PRIVACY', 'CLOUD')),
            description     TEXT,
            owner_id        UUID REFERENCES users(id) ON DELETE SET NULL,
            status          project_status NOT NULL DEFAULT 'active',
            settings        JSONB NOT NULL DEFAULT '{}',
            created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX ix_projects_owner_id ON projects(owner_id)")
    op.execute("CREATE INDEX ix_projects_product_family ON projects(product_family)")
    op.execute("""
        CREATE TRIGGER trg_projects_updated_at
        BEFORE UPDATE ON projects
        FOR EACH ROW EXECUTE FUNCTION update_updated_at()
    """)

    # ── project_policies ────────────────────────────────────────────────────
    op.execute("""
        CREATE TABLE project_policies (
            id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            project_id       UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
            lib_policy_id    UUID REFERENCES policies(id) ON DELETE SET NULL,
            custom_content   TEXT,
            is_edited        BOOLEAN NOT NULL DEFAULT FALSE,
            stacking_locked  BOOLEAN NOT NULL DEFAULT FALSE,
            stale_warning    BOOLEAN NOT NULL DEFAULT FALSE,
            status           VARCHAR(20) NOT NULL DEFAULT 'active'
                CHECK (status IN ('active', 'draft', 'archived')),
            created_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at       TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX ix_project_policies_project_id ON project_policies(project_id)")
    op.execute("CREATE INDEX ix_project_policies_lib_policy_id ON project_policies(lib_policy_id)")
    op.execute("""
        CREATE TRIGGER trg_project_policies_updated_at
        BEFORE UPDATE ON project_policies
        FOR EACH ROW EXECUTE FUNCTION update_updated_at()
    """)

    # ── project_implementations ─────────────────────────────────────────────
    op.execute("""
        CREATE TABLE project_implementations (
            id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            project_id      UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
            lib_impl_id     UUID REFERENCES implementations(id) ON DELETE SET NULL,
            custom_content  TEXT,
            is_edited       BOOLEAN NOT NULL DEFAULT FALSE,
            stale_warning   BOOLEAN NOT NULL DEFAULT FALSE,
            status          VARCHAR(20) NOT NULL DEFAULT 'active'
                CHECK (status IN ('active', 'draft', 'archived')),
            created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX ix_project_implementations_project_id ON project_implementations(project_id)")
    op.execute("CREATE INDEX ix_project_implementations_lib_impl_id ON project_implementations(lib_impl_id)")
    op.execute("""
        CREATE TRIGGER trg_project_implementations_updated_at
        BEFORE UPDATE ON project_implementations
        FOR EACH ROW EXECUTE FUNCTION update_updated_at()
    """)

    # ── project_checklists ──────────────────────────────────────────────────
    op.execute("""
        CREATE TABLE project_checklists (
            id                       UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            project_id               UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
            control_group_id         UUID NOT NULL REFERENCES control_groups(id) ON DELETE CASCADE,
            product_type             VARCHAR(20) NOT NULL
                CHECK (product_type IN ('framework', 'operational', 'privacy', 'cloud')),
            applicability_overrides  JSONB NOT NULL DEFAULT '{}',
            clone_source             VARCHAR(10),
            cloned_content           JSONB,
            created_at               TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at               TIMESTAMPTZ NOT NULL DEFAULT now(),
            CONSTRAINT uq_project_checklist UNIQUE (project_id, control_group_id, product_type)
        )
    """)
    op.execute("CREATE INDEX ix_project_checklists_project_id ON project_checklists(project_id)")
    op.execute("CREATE INDEX ix_project_checklists_control_group_id ON project_checklists(control_group_id)")
    op.execute("""
        CREATE TRIGGER trg_project_checklists_updated_at
        BEFORE UPDATE ON project_checklists
        FOR EACH ROW EXECUTE FUNCTION update_updated_at()
    """)

    # ── project_id FK on operational tables (nullable) ──────────────────────
    op.execute("""
        ALTER TABLE assessments
        ADD COLUMN project_id UUID REFERENCES projects(id) ON DELETE SET NULL
    """)
    op.execute("CREATE INDEX ix_assessments_project_id ON assessments(project_id)")

    op.execute("""
        ALTER TABLE assessment_collections
        ADD COLUMN project_id UUID REFERENCES projects(id) ON DELETE SET NULL
    """)
    op.execute("CREATE INDEX ix_assessment_collections_project_id ON assessment_collections(project_id)")

    op.execute("""
        ALTER TABLE gaps
        ADD COLUMN project_id UUID REFERENCES projects(id) ON DELETE SET NULL
    """)
    op.execute("CREATE INDEX ix_gaps_project_id ON gaps(project_id)")

    op.execute("""
        ALTER TABLE evidence
        ADD COLUMN project_id UUID REFERENCES projects(id) ON DELETE SET NULL
    """)
    op.execute("CREATE INDEX ix_evidence_project_id ON evidence(project_id)")

    op.execute("""
        ALTER TABLE compliance_assessments
        ADD COLUMN project_id UUID REFERENCES projects(id) ON DELETE SET NULL
    """)
    op.execute("CREATE INDEX ix_compliance_assessments_project_id ON compliance_assessments(project_id)")


def downgrade() -> None:
    op.execute("ALTER TABLE compliance_assessments DROP COLUMN IF EXISTS project_id")
    op.execute("ALTER TABLE evidence DROP COLUMN IF EXISTS project_id")
    op.execute("ALTER TABLE gaps DROP COLUMN IF EXISTS project_id")
    op.execute("ALTER TABLE assessment_collections DROP COLUMN IF EXISTS project_id")
    op.execute("ALTER TABLE assessments DROP COLUMN IF EXISTS project_id")

    op.execute("DROP TABLE IF EXISTS project_checklists")
    op.execute("DROP TABLE IF EXISTS project_implementations")
    op.execute("DROP TABLE IF EXISTS project_policies")
    op.execute("DROP TABLE IF EXISTS projects")
    op.execute("DROP TYPE IF EXISTS project_status")
