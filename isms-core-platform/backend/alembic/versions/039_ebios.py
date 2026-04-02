"""Phase 19 — EBIOS RM tables.

6 tables: ebios_studies, ebios_feared_events, ebios_risk_sources,
ebios_strategic_scenarios, ebios_attack_paths, ebios_measures.

Revision ID: 039
Revises: 038
Create Date: 2026-04-02
"""

from alembic import op

revision = '039'
down_revision = '038'
branch_labels = None
depends_on = None


def upgrade():
    # ebios_studies — top-level study container (one per assessment exercise)
    op.execute("""
        CREATE TABLE IF NOT EXISTS ebios_studies (
            id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            org_id          UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
            project_id      UUID REFERENCES projects(id) ON DELETE SET NULL,
            name            TEXT NOT NULL,
            description     TEXT,
            scope           TEXT,
            status          VARCHAR(20) NOT NULL DEFAULT 'draft',
            owner           TEXT,
            started_at      DATE,
            reviewed_at     DATE,
            created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_ebios_studies_org ON ebios_studies(org_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_ebios_studies_project ON ebios_studies(project_id)")

    # Workshop 1 — feared events (assets + feared events on those assets)
    op.execute("""
        CREATE TABLE IF NOT EXISTS ebios_feared_events (
            id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            study_id        UUID NOT NULL REFERENCES ebios_studies(id) ON DELETE CASCADE,
            org_id          UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
            asset_name      TEXT NOT NULL,
            asset_type      VARCHAR(50) NOT NULL DEFAULT 'primary',
            description     TEXT,
            gravity         INTEGER CHECK (gravity BETWEEN 1 AND 4),
            created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_ebios_feared_events_study ON ebios_feared_events(study_id)")

    # Workshop 2 — risk sources (threat actors)
    op.execute("""
        CREATE TABLE IF NOT EXISTS ebios_risk_sources (
            id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            study_id        UUID NOT NULL REFERENCES ebios_studies(id) ON DELETE CASCADE,
            org_id          UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
            name            TEXT NOT NULL,
            category        VARCHAR(50) NOT NULL DEFAULT 'cybercriminal',
            motivation      TEXT,
            pertinence      INTEGER CHECK (pertinence BETWEEN 1 AND 4),
            activity        INTEGER CHECK (activity BETWEEN 1 AND 4),
            resources       INTEGER CHECK (resources BETWEEN 1 AND 4),
            created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_ebios_risk_sources_study ON ebios_risk_sources(study_id)")

    # Workshop 3 — strategic scenarios (risk source × feared event pairs with likelihood)
    op.execute("""
        CREATE TABLE IF NOT EXISTS ebios_strategic_scenarios (
            id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            study_id            UUID NOT NULL REFERENCES ebios_studies(id) ON DELETE CASCADE,
            org_id              UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
            risk_source_id      UUID REFERENCES ebios_risk_sources(id) ON DELETE SET NULL,
            feared_event_id     UUID REFERENCES ebios_feared_events(id) ON DELETE SET NULL,
            name                TEXT NOT NULL,
            description         TEXT,
            likelihood          INTEGER CHECK (likelihood BETWEEN 1 AND 4),
            gravity             INTEGER CHECK (gravity BETWEEN 1 AND 4),
            risk_level          INTEGER GENERATED ALWAYS AS (COALESCE(likelihood,0) * COALESCE(gravity,0)) STORED,
            retained            BOOLEAN NOT NULL DEFAULT TRUE,
            created_at          TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_ebios_strategic_scenarios_study ON ebios_strategic_scenarios(study_id)")

    # Workshop 4 — attack paths (operationalised scenarios with MITRE ATT&CK)
    op.execute("""
        CREATE TABLE IF NOT EXISTS ebios_attack_paths (
            id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            study_id                UUID NOT NULL REFERENCES ebios_studies(id) ON DELETE CASCADE,
            org_id                  UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
            strategic_scenario_id   UUID REFERENCES ebios_strategic_scenarios(id) ON DELETE SET NULL,
            name                    TEXT NOT NULL,
            description             TEXT,
            mitre_techniques        JSONB NOT NULL DEFAULT '[]',
            difficulty              INTEGER CHECK (difficulty BETWEEN 1 AND 4),
            detectability           INTEGER CHECK (detectability BETWEEN 1 AND 4),
            created_at              TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_ebios_attack_paths_study ON ebios_attack_paths(study_id)")

    # Workshop 5 — security measures (controls to treat risks, mapped to ISO 27001 control groups)
    op.execute("""
        CREATE TABLE IF NOT EXISTS ebios_measures (
            id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            study_id            UUID NOT NULL REFERENCES ebios_studies(id) ON DELETE CASCADE,
            org_id              UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
            scenario_id         UUID REFERENCES ebios_strategic_scenarios(id) ON DELETE SET NULL,
            name                TEXT NOT NULL,
            description         TEXT,
            status              VARCHAR(20) NOT NULL DEFAULT 'planned',
            iso_control_ref     TEXT,
            control_group_id    UUID REFERENCES control_groups(id) ON DELETE SET NULL,
            effectiveness       INTEGER CHECK (effectiveness BETWEEN 1 AND 4),
            due_date            DATE,
            owner               TEXT,
            created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at          TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_ebios_measures_study ON ebios_measures(study_id)")


def downgrade():
    op.execute("DROP TABLE IF EXISTS ebios_measures")
    op.execute("DROP TABLE IF EXISTS ebios_attack_paths")
    op.execute("DROP TABLE IF EXISTS ebios_strategic_scenarios")
    op.execute("DROP TABLE IF EXISTS ebios_risk_sources")
    op.execute("DROP TABLE IF EXISTS ebios_feared_events")
    op.execute("DROP TABLE IF EXISTS ebios_studies")
