"""Rename CLD-POL-/CLD-IMP-/CLD-CHK- → CLD-PII-POL-/CLD-PII-IMP-/CLD-PII-CHK-

ISO 27017:2025 will share the cloud product slot under 52-isms-core-cloud.
To disambiguate ISO 27018 (PII) from ISO 27017 (Security) documents at the
document-ID level, the 27018 prefix is renamed from CLD- to CLD-PII-.

Revision ID: 067_cld_rename_pii_prefix
Revises: 066_projects_add_ai_product_family
Create Date: 2026-06-02
"""

from alembic import op

revision = "067_cld_rename_pii_prefix"
down_revision = "066"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # policies table — POL docs (EN + DE/FR/IT language variants)
    op.execute("""
        UPDATE policies
        SET document_id = REPLACE(document_id, 'CLD-POL-', 'CLD-PII-POL-')
        WHERE document_id LIKE 'CLD-POL-%'
    """)
    # policies table — IMP docs (UG + TG)
    op.execute("""
        UPDATE policies
        SET document_id = REPLACE(document_id, 'CLD-IMP-', 'CLD-PII-IMP-')
        WHERE document_id LIKE 'CLD-IMP-%'
    """)
    # assessments table — CHK workbook document_ids
    op.execute("""
        UPDATE assessments
        SET document_id = REPLACE(document_id, 'CLD-CHK-', 'CLD-PII-CHK-')
        WHERE document_id LIKE 'CLD-CHK-%'
    """)


def downgrade() -> None:
    op.execute("""
        UPDATE policies
        SET document_id = REPLACE(document_id, 'CLD-PII-POL-', 'CLD-POL-')
        WHERE document_id LIKE 'CLD-PII-POL-%'
    """)
    op.execute("""
        UPDATE policies
        SET document_id = REPLACE(document_id, 'CLD-PII-IMP-', 'CLD-IMP-')
        WHERE document_id LIKE 'CLD-PII-IMP-%'
    """)
    op.execute("""
        UPDATE assessments
        SET document_id = REPLACE(document_id, 'CLD-PII-CHK-', 'CLD-CHK-')
        WHERE document_id LIKE 'CLD-PII-CHK-%'
    """)
