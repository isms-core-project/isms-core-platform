"""Consolidate SWISS_NDSG into CH_NDSG — remove duplicate Swiss nDSG framework.

Revision ID: 058
Revises: 057
Create Date: 2026-04-28
"""

from alembic import op
from sqlalchemy import text

revision = "058"
down_revision = "057"
branch_labels = None
depends_on = None


def upgrade() -> None:
    conn = op.get_bind()

    # 1. Rename CH_NDSG to the canonical display name
    conn.execute(text("""
        UPDATE frameworks
        SET name = 'Swiss Federal Act on Data Protection (nFADP/nDSG)'
        WHERE code = 'CH_NDSG'
    """))

    # 2. Delete CrossFrameworkMappings that target SWISS_NDSG FrameworkControls
    conn.execute(text("""
        DELETE FROM cross_framework_mappings
        WHERE target_control_id IN (
            SELECT fc.id
            FROM framework_controls fc
            JOIN frameworks fw ON fc.framework_id = fw.id
            WHERE fw.code = 'SWISS_NDSG'
        )
    """))

    # 3. Delete SWISS_NDSG FrameworkControls
    conn.execute(text("""
        DELETE FROM framework_controls
        WHERE framework_id = (
            SELECT id FROM frameworks WHERE code = 'SWISS_NDSG'
        )
    """))

    # 4. Delete SWISS_NDSG Framework row
    conn.execute(text("""
        DELETE FROM frameworks WHERE code = 'SWISS_NDSG'
    """))


def downgrade() -> None:
    # Non-reversible — re-run bootstrap to restore from swiss_ndsg.json if needed
    pass
