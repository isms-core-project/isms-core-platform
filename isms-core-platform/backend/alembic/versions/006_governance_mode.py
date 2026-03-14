"""Phase 7.15 — Governance mode schema.

Revision ID: 006_governance_mode
Revises: 005_phase7_5_sheet_schemas
Create Date: 2026-03-08

Changes:
  1. CREATE TYPE governance_mode AS ENUM ('platform', 'local')
  2. CREATE TABLE organisations (id, name, slug, governance_mode, description, settings,
     created_at, updated_at) — single-tenant, one row expected per deployment
  3. trigger trg_organisations_updated_at
  4. INSERT default organisation row (governance_mode = 'platform')
"""

import uuid
from alembic import op

revision = "006_governance_mode"
down_revision = "005_phase7_5_sheet_schemas"
branch_labels = None
depends_on = None

_DEFAULT_ORG_ID = str(uuid.uuid5(uuid.NAMESPACE_DNS, "isms-core.organisation.default"))
# = c1b6cbcf-1e65-55fb-a389-4c863e208e05


def upgrade():
    # Pure raw SQL — avoids SQLAlchemy sa.Enum auto-create conflicts.
    op.execute("CREATE TYPE governance_mode AS ENUM ('platform', 'local')")

    op.execute("""
        CREATE TABLE organisations (
            id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            name        VARCHAR(255) NOT NULL,
            slug        VARCHAR(100) UNIQUE NOT NULL,
            governance_mode governance_mode NOT NULL DEFAULT 'platform',
            description TEXT,
            settings    JSONB NOT NULL DEFAULT '{}',
            created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
        )
    """)

    op.execute("""
        CREATE TRIGGER trg_organisations_updated_at
        BEFORE UPDATE ON organisations
        FOR EACH ROW EXECUTE FUNCTION update_updated_at()
    """)

    op.execute(f"""
        INSERT INTO organisations (id, name, slug, governance_mode, description, settings)
        VALUES (
            '{_DEFAULT_ORG_ID}',
            'ISMS CORE',
            'isms-core',
            'platform',
            'Default ISMS CORE organisation — update name and governance mode as required.',
            '{{}}'
        )
        ON CONFLICT DO NOTHING
    """)


def downgrade():
    op.execute("DROP TRIGGER IF EXISTS trg_organisations_updated_at ON organisations CASCADE")
    op.execute("DROP TABLE IF EXISTS organisations")
    op.execute("DROP TYPE IF EXISTS governance_mode")
