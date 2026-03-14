"""ISO 27701:2025 privacy control groups — seed A.1.x through A.3.x.

Inserts 21 control groups for the ISO 27701:2025 PRIV-POL policy suite
so that PRIV-POL documents can be resolved during import.

Groups follow the PRIV-POL bundling used in 51-isms-core-privacy/:
  - A.1.x.x  (PII controller controls)
  - A.2.x.x  (PII processor controls)
  - A.3.x    (Shared security controls)

product_family = 'PRIVACY' (available since migration 013_privacy_product).

Revision ID: 015_privacy_groups
Revises: 014_cloud_groups
Create Date: 2026-03-09
"""

from alembic import op

revision = "015_privacy_groups"
down_revision = "014_cloud_groups"
branch_labels = None
depends_on = None

# (group_code, name, section, section_name, folder_name)
_ISO27701_GROUPS = [
    # ── Table A.1 — PII Controller ────────────────────────────────────────────
    (
        "a.1.2.2-5",
        "Lawful Basis and Consent",
        "A.1.2",
        "Conditions for Collection and Processing",
        "priv-a.1.2.2-5-lawful-basis-and-consent",
    ),
    (
        "a.1.2.6-9",
        "Privacy Governance and Records",
        "A.1.2",
        "Conditions for Collection and Processing",
        "priv-a.1.2.6-9-privacy-governance-and-records",
    ),
    (
        "a.1.3.2-4",
        "Transparency and Information Provision",
        "A.1.3",
        "Obligations to PII Principals",
        "priv-a.1.3.2-4-transparency-and-information-provision",
    ),
    (
        "a.1.3.5-10",
        "Data Subject Rights",
        "A.1.3",
        "Obligations to PII Principals",
        "priv-a.1.3.5-10-data-subject-rights",
    ),
    (
        "a.1.3.11",
        "Automated Decision Making",
        "A.1.3",
        "Obligations to PII Principals",
        "priv-a.1.3.11-automated-decision-making",
    ),
    (
        "a.1.4.2-5",
        "Data Minimisation",
        "A.1.4",
        "Privacy by Design and Privacy by Default",
        "priv-a.1.4.2-5-data-minimisation",
    ),
    (
        "a.1.4.6-10",
        "PII Lifecycle, Retention and Disposal",
        "A.1.4",
        "Privacy by Design and Privacy by Default",
        "priv-a.1.4.6-10-pii-lifecycle-retention-and-disposal",
    ),
    (
        "a.1.5.2-5",
        "PII Transfer and Disclosure",
        "A.1.5",
        "PII Sharing, Transfer and Disclosure",
        "priv-a.1.5.2-5-pii-transfer-and-disclosure",
    ),
    # ── Table A.2 — PII Processor ─────────────────────────────────────────────
    (
        "a.2.2.2-7",
        "Processor Agreements and Obligations",
        "A.2.2",
        "Conditions for Collection and Processing",
        "priv-a.2.2.2-7-processor-agreements-and-obligations",
    ),
    (
        "a.2.3.2",
        "PII Principal Obligations (Processor)",
        "A.2.3",
        "Obligations to PII Principals",
        "priv-a.2.3.2-pii-principal-obligations-processor",
    ),
    (
        "a.2.4.2-4",
        "Processor Lifecycle Controls",
        "A.2.4",
        "Privacy by Design and Privacy by Default",
        "priv-a.2.4.2-4-processor-lifecycle-controls",
    ),
    (
        "a.2.5.2-6",
        "Transfer and Disclosure (Processor)",
        "A.2.5",
        "PII Sharing, Transfer and Disclosure",
        "priv-a.2.5.2-6-transfer-and-disclosure-processor",
    ),
    (
        "a.2.5.7-9",
        "Sub-processor Management",
        "A.2.5",
        "PII Sharing, Transfer and Disclosure",
        "priv-a.2.5.7-9-sub-processor-management",
    ),
    # ── Table A.3 — Shared Security Controls ─────────────────────────────────
    (
        "a.3.3-4",
        "Privacy Policy and Roles",
        "A.3",
        "Shared Security Controls",
        "priv-a.3.3-4-privacy-policy-and-roles",
    ),
    (
        "a.3.5-7",
        "Information Classification and Transfer",
        "A.3",
        "Shared Security Controls",
        "priv-a.3.5-7-information-classification-and-transfer",
    ),
    (
        "a.3.8-10",
        "Identity, Access and Supplier Controls",
        "A.3",
        "Shared Security Controls",
        "priv-a.3.8-10-identity-access-and-supplier-controls",
    ),
    (
        "a.3.11-12",
        "Privacy Incident Management",
        "A.3",
        "Shared Security Controls",
        "priv-a.3.11-12-privacy-incident-management",
    ),
    (
        "a.3.13-16",
        "Compliance, Audit and Review",
        "A.3",
        "Shared Security Controls",
        "priv-a.3.13-16-compliance-audit-and-review",
    ),
    (
        "a.3.17-19",
        "Privacy Awareness, NDAs and Clear Desk",
        "A.3",
        "Shared Security Controls",
        "priv-a.3.17-19-people-security-and-clear-desk",
    ),
    (
        "a.3.20-22",
        "Physical Media and Endpoint Security",
        "A.3",
        "Shared Security Controls",
        "priv-a.3.20-22-physical-media-and-endpoint-security",
    ),
    (
        "a.3.23-31",
        "Technical Security Controls for PII",
        "A.3",
        "Shared Security Controls",
        "priv-a.3.23-31-technical-controls-auth-crypto-dev",
    ),
]


def upgrade() -> None:
    for group_code, name, section, section_name, folder_name in _ISO27701_GROUPS:
        # Escape single quotes in name/section_name (none expected, but safe)
        safe_name = name.replace("'", "''")
        safe_section_name = section_name.replace("'", "''")
        op.execute(f"""
            INSERT INTO control_groups (
                id, group_code, name, section, section_name, folder_name,
                is_stacked, has_framework, has_operational,
                framework_status, operational_status,
                product_family, metadata, created_at, updated_at
            ) VALUES (
                gen_random_uuid(),
                '{group_code}', '{safe_name}', '{section}', '{safe_section_name}', '{folder_name}',
                false, true, false,
                'incomplete', 'incomplete',
                'PRIVACY', '{{}}', NOW(), NOW()
            )
            ON CONFLICT (group_code) DO NOTHING
        """)


def downgrade() -> None:
    codes = ", ".join(f"'{g[0]}'" for g in _ISO27701_GROUPS)
    op.execute(
        f"DELETE FROM control_groups WHERE group_code IN ({codes}) "
        f"AND product_family = 'PRIVACY'"
    )
