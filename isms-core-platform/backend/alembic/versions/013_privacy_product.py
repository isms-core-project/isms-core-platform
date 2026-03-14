"""Privacy product extension — ProductType.PRIVACY/CLOUD, PrivacyRole, ProductFamily.

Adds the three building blocks needed for the PRIVACY product:
  1. product_type enum — add 'privacy' and 'cloud' values
  2. privacyrole enum + organisations.privacy_role — controls coverage denominator
  3. productfamily enum + control_groups.product_family — routes PRIV groups to PRIVACY product

Revision ID: 013_privacy_product
Revises: 012_evidence_status
Create Date: 2026-03-09
"""

from alembic import op

revision = "013_privacy_product"
down_revision = "012_evidence_status"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 1. Extend product_type enum with new product values
    op.execute("ALTER TYPE product_type ADD VALUE IF NOT EXISTS 'privacy'")
    op.execute("ALTER TYPE product_type ADD VALUE IF NOT EXISTS 'cloud'")

    # 2. New privacyrole enum + column on organisations
    #    Drives the coverage denominator: CONTROLLER-only orgs never see A.2 groups.
    op.execute(
        "CREATE TYPE privacyrole AS ENUM ('CONTROLLER', 'PROCESSOR', 'BOTH')"
    )
    op.execute(
        "ALTER TABLE organisations "
        "ADD COLUMN privacy_role privacyrole NOT NULL DEFAULT 'BOTH'"
    )

    # 3. New productfamily enum + column on control_groups
    #    All existing ISMS groups get 'ISMS'; PRIV groups imported later get 'PRIVACY'.
    op.execute(
        "CREATE TYPE productfamily AS ENUM ('ISMS', 'PRIVACY', 'CLOUD')"
    )
    op.execute(
        "ALTER TABLE control_groups "
        "ADD COLUMN product_family productfamily NOT NULL DEFAULT 'ISMS'"
    )


def downgrade() -> None:
    op.execute("ALTER TABLE control_groups DROP COLUMN product_family")
    op.execute("DROP TYPE productfamily")
    op.execute("ALTER TABLE organisations DROP COLUMN privacy_role")
    op.execute("DROP TYPE privacyrole")
    # Note: PostgreSQL does not support removing enum values — 'privacy' and 'cloud'
    # remain in product_type after downgrade. This is safe — no data uses them.
