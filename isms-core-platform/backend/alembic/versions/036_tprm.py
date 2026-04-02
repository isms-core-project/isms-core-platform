"""TPRM — vendors, vendor_assessments, vendor_contracts.

Revision ID: 036
Revises: 035
Create Date: 2026-04-02
"""

from alembic import op

revision = '036'
down_revision = '035'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        CREATE TABLE IF NOT EXISTS vendors (
            id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            org_id                  UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
            name                    VARCHAR(200) NOT NULL,
            vendor_type             VARCHAR(20)  NOT NULL DEFAULT 'supplier',
            criticality             VARCHAR(20)  NOT NULL DEFAULT 'medium',
            status                  VARCHAR(20)  NOT NULL DEFAULT 'active',
            description             TEXT,
            website                 VARCHAR(500),
            primary_contact         VARCHAR(200),
            -- DORA-specific fields
            dora_entity_type        VARCHAR(50),
            dora_ict_service_type   VARCHAR(50),
            dora_substitutability   VARCHAR(30),
            dora_register_ref       VARCHAR(100),
            created_at              TIMESTAMPTZ NOT NULL DEFAULT now(),
            updated_at              TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_vendors_org ON vendors(org_id)")

    op.execute("""
        CREATE TABLE IF NOT EXISTS vendor_assessments (
            id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            vendor_id         UUID NOT NULL REFERENCES vendors(id) ON DELETE CASCADE,
            control_group_id  UUID REFERENCES control_groups(id) ON DELETE SET NULL,
            assessor_id       UUID REFERENCES users(id) ON DELETE SET NULL,
            score             INT,
            status            VARCHAR(20) NOT NULL DEFAULT 'not_assessed',
            notes             TEXT,
            assessment_date   DATE,
            next_review_date  DATE,
            created_at        TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_vendor_assessments_vendor ON vendor_assessments(vendor_id)")

    op.execute("""
        CREATE TABLE IF NOT EXISTS vendor_contracts (
            id                        UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            vendor_id                 UUID NOT NULL REFERENCES vendors(id) ON DELETE CASCADE,
            title                     VARCHAR(300) NOT NULL,
            contract_ref              VARCHAR(100),
            start_date                DATE,
            expiry_date               DATE,
            auto_renews               BOOLEAN NOT NULL DEFAULT FALSE,
            security_clauses_present  BOOLEAN NOT NULL DEFAULT FALSE,
            created_at                TIMESTAMPTZ NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_vendor_contracts_vendor ON vendor_contracts(vendor_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_vendor_contracts_expiry ON vendor_contracts(expiry_date)")


def downgrade():
    op.execute("DROP TABLE IF EXISTS vendor_contracts")
    op.execute("DROP TABLE IF EXISTS vendor_assessments")
    op.execute("DROP TABLE IF EXISTS vendors")
