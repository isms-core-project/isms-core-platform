"""ISO 42001:2023 AI control groups — seed foundation + A.2–A.10.

Inserts 11 control groups for the ISO 42001:2023 AI extension pack
(AI-POL-00/01 foundation + 10 Annex A section-level policy groups)
so that AI-POL documents can be resolved during import.

product_family = 'AI' (added in migration 050_add_ai_product_family).

Revision ID: 051
Revises: 050
Create Date: 2026-04-15
"""

from alembic import op

revision = "051"
down_revision = "050"
branch_labels = None
depends_on = None

# (group_code, name, section, section_name, folder_name)
_ISO42001_GROUPS = [
    # ── Annex A — ISO 42001:2023 AIMS controls ────────────────────────────────
    (
        "a.2.2-4",
        "AI Policy Framework",
        "A.2",
        "Policies Relating to AI",
        "ai-a.2.2-4-ai-policy-framework",
    ),
    (
        "a.3.2-3",
        "AI Roles and Responsibilities",
        "A.3",
        "Internal Organisation",
        "ai-a.3.2-3-ai-roles-and-responsibilities",
    ),
    (
        "a.4.2-6",
        "AI System Resources",
        "A.4",
        "Resources for AI",
        "ai-a.4.2-6-ai-system-resources",
    ),
    (
        "a.5.2-5",
        "AI System Impact Assessment",
        "A.5",
        "Planning and Operation",
        "ai-a.5.2-5-ai-system-impact-assessment",
    ),
    (
        "a.6.1",
        "AI Development Governance",
        "A.6",
        "Operation",
        "ai-a.6.1-ai-development-governance",
    ),
    (
        "a.6.2",
        "AI System Lifecycle",
        "A.6",
        "Operation",
        "ai-a.6.2-ai-system-lifecycle",
    ),
    (
        "a.7.2-6",
        "Data for AI Systems",
        "A.7",
        "Data for AI Systems",
        "ai-a.7.2-6-data-for-ai-systems",
    ),
    (
        "a.8.2-5",
        "Information for Interested Parties",
        "A.8",
        "Information for AI Systems",
        "ai-a.8.2-5-information-for-interested-parties",
    ),
    (
        "a.9.2-4",
        "Responsible Use of AI Systems",
        "A.9",
        "Responsible Use of AI",
        "ai-a.9.2-4-responsible-use-of-ai-systems",
    ),
    (
        "a.10.2-4",
        "Third-Party and Customer Relationships",
        "A.10",
        "Third-Party and Customer Relationships",
        "ai-a.10.2-4-third-party-and-customer-relationships",
    ),
]


def upgrade() -> None:
    # Foundation group for AI-POL-00 / AI-POL-01
    op.execute("""
        INSERT INTO control_groups (
            id, group_code, name, section, section_name, folder_name,
            is_stacked, has_framework, has_operational,
            framework_status, operational_status,
            product_family, metadata, created_at, updated_at
        ) VALUES (
            gen_random_uuid(),
            'ai-00', 'AI Foundation Policies', '00',
            'Foundation', '00-ai-foundation-policies',
            false, true, false,
            'incomplete', 'incomplete',
            'AI', '{}', NOW(), NOW()
        )
        ON CONFLICT (group_code) DO NOTHING
    """)

    for group_code, name, section, section_name, folder_name in _ISO42001_GROUPS:
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
                'AI', '{{}}', NOW(), NOW()
            )
            ON CONFLICT (group_code) DO NOTHING
        """)


def downgrade() -> None:
    codes = ", ".join(f"'{g[0]}'" for g in _ISO42001_GROUPS)
    op.execute(
        f"DELETE FROM control_groups WHERE group_code IN ({codes}) "
        f"AND product_family = 'AI'"
    )
    op.execute(
        "DELETE FROM control_groups WHERE group_code = 'ai-00' "
        "AND product_family = 'AI'"
    )
