"""ISO 27018:2025 cloud control groups — seed A.1 through A.12.

Inserts 12 control groups for the ISO 27018:2025 Annex A section-level policy
suite (CLD-POL-A.1–A.12) so that CLD-POL documents can be resolved during import.

product_family = 'CLOUD' (added in migration 013_privacy_product).

Revision ID: 014_iso27018_cloud_control_groups
Revises: 013_privacy_product
Create Date: 2026-03-09
"""

from alembic import op

revision = "014_cloud_groups"
down_revision = "013_privacy_product"
branch_labels = None
depends_on = None

# ISO 27018:2025 Annex A sections: (group_code, name, section, section_name, folder_name)
_ISO27018_GROUPS = [
    ("a.1",  "General",                                  "A.1",  "General",                                  "cld-a.1-general"),
    ("a.2",  "Consent and Choice",                       "A.2",  "Consent and Choice",                       "cld-a.2-consent-and-choice"),
    ("a.3",  "Purpose Legitimacy and Specification",     "A.3",  "Purpose Legitimacy and Specification",     "cld-a.3-purpose-legitimacy"),
    ("a.4",  "Collection Limitation",                    "A.4",  "Collection Limitation",                    "cld-a.4-collection-limitation"),
    ("a.5",  "Data Minimisation",                        "A.5",  "Data Minimisation",                        "cld-a.5-data-minimisation"),
    ("a.6",  "Use, Retention and Disclosure Limitation", "A.6",  "Use, Retention and Disclosure Limitation", "cld-a.6-use-retention-disclosure"),
    ("a.7",  "Accuracy and Quality",                     "A.7",  "Accuracy and Quality",                     "cld-a.7-accuracy-quality"),
    ("a.8",  "Openness, Transparency and Notice",        "A.8",  "Openness, Transparency and Notice",        "cld-a.8-openness-transparency"),
    ("a.9",  "Individual Participation and Access",      "A.9",  "Individual Participation and Access",      "cld-a.9-individual-participation"),
    ("a.10", "Accountability",                           "A.10", "Accountability",                           "cld-a.10-accountability"),
    ("a.11", "Information Security",                     "A.11", "Information Security",                     "cld-a.11-information-security"),
    ("a.12", "Privacy Compliance",                       "A.12", "Privacy Compliance",                       "cld-a.12-privacy-compliance"),
]


def upgrade() -> None:
    for group_code, name, section, section_name, folder_name in _ISO27018_GROUPS:
        op.execute(f"""
            INSERT INTO control_groups (
                id, group_code, name, section, section_name, folder_name,
                is_stacked, has_framework, has_operational,
                framework_status, operational_status,
                product_family, metadata, created_at, updated_at
            ) VALUES (
                gen_random_uuid(),
                '{group_code}', '{name}', '{section}', '{section_name}', '{folder_name}',
                false, true, false,
                'incomplete', 'incomplete',
                'CLOUD', '{{}}', NOW(), NOW()
            )
            ON CONFLICT (group_code) DO NOTHING
        """)


def downgrade() -> None:
    codes = ", ".join(f"'{g[0]}'" for g in _ISO27018_GROUPS)
    op.execute(
        f"DELETE FROM control_groups WHERE group_code IN ({codes}) "
        f"AND product_family = 'CLOUD'"
    )
