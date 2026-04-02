"""Phase 20 — Custom Framework Import.

Allows orgs to upload YAML-based custom/sector-specific control frameworks.
Two tables: custom_frameworks (header) + custom_controls (individual controls).

Revision ID: 040
Revises: 039
Create Date: 2026-04-02
"""

from alembic import op

revision = '040'
down_revision = '039'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        CREATE TABLE IF NOT EXISTS custom_frameworks (
            id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            org_id          UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
            name            TEXT NOT NULL,
            short_code      VARCHAR(30) NOT NULL,
            version         VARCHAR(20) NOT NULL DEFAULT '1.0',
            description     TEXT,
            source_yaml     TEXT,
            control_count   INTEGER NOT NULL DEFAULT 0,
            status          VARCHAR(20) NOT NULL DEFAULT 'active',
            created_by      UUID REFERENCES users(id) ON DELETE SET NULL,
            created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
            UNIQUE(org_id, short_code)
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_custom_frameworks_org ON custom_frameworks(org_id)")

    op.execute("""
        CREATE TABLE IF NOT EXISTS custom_controls (
            id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            framework_id    UUID NOT NULL REFERENCES custom_frameworks(id) ON DELETE CASCADE,
            org_id          UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
            control_id      VARCHAR(50) NOT NULL,
            title           TEXT NOT NULL,
            description     TEXT,
            category        TEXT,
            subcategory     TEXT,
            priority        VARCHAR(10),
            iso_mappings    JSONB NOT NULL DEFAULT '[]',
            tags            JSONB NOT NULL DEFAULT '[]',
            created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_custom_controls_framework ON custom_controls(framework_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_custom_controls_org ON custom_controls(org_id)")


def downgrade():
    op.execute("DROP TABLE IF EXISTS custom_controls")
    op.execute("DROP TABLE IF EXISTS custom_frameworks")
