"""Add PRIVACY foundation control group for PRIV-POL-00 and PRIV-POL-01.

The PRIVACY product has 21 control groups (A.1.x–A.3) but no foundation
group. PRIV-POL-00 and PRIV-POL-01 are cross-cutting governance documents
(Privacy Regulatory Applicability Framework, Privacy Governance and
Decision-Making Framework) that belong to the PRIVACY product but have no
group to attach to. Without this group the importer falls back to the ISMS
"00" group, contaminating the ISMS policy list.

group_code "priv-00" (globally unique, distinct from ISMS "00") with
section "00" and product_family PRIVACY. The importer's _resolve_control_group
step 2 uses a per-family fallback code map so PRIV-POL docs resolve here.

Revision ID: 024_privacy_foundation_group
Revises: 023_compliance_assessments
Create Date: 2026-03-15
"""

from alembic import op

revision = "024_privacy_foundation_group"
down_revision = "023_compliance_assessments"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        INSERT INTO control_groups (
            id, group_code, name, section, section_name, folder_name,
            is_stacked, has_framework, has_operational,
            framework_status, operational_status,
            product_family, metadata, created_at, updated_at
        ) VALUES (
            gen_random_uuid(),
            'priv-00', 'Privacy Foundation Policies', '00',
            'Foundation', '00-priv-foundation-policies',
            false, true, false,
            'incomplete', 'incomplete',
            'PRIVACY', '{}', NOW(), NOW()
        )
        ON CONFLICT (group_code) DO NOTHING
    """)


def downgrade() -> None:
    op.execute(
        "DELETE FROM control_groups WHERE group_code = 'priv-00' "
        "AND product_family = 'PRIVACY'"
    )
