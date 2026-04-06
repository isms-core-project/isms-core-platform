"""Phase 25 — Threat Intelligence & Vulnerability Feeds tables.

Revision ID: 046
Revises: 045
Create Date: 2026-04-06

Tables:
  feed_runs           — per-feed execution log (status, item count, errors)
  mitre_techniques    — MITRE ATT&CK (v18/v19) and ATLAS techniques
  cisa_kev_entries    — CISA Known Exploited Vulnerabilities catalogue
  epss_scores         — FIRST EPSS exploit probability scores (top 5 000)
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB, UUID

revision = '046'
down_revision = '045'
branch_labels = None
depends_on = None


def upgrade():
    # ── feed_runs ──────────────────────────────────────────────────────────────
    op.create_table(
        'feed_runs',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('feed_name', sa.String(50), nullable=False),
        sa.Column('status', sa.String(20), nullable=False, server_default='running'),
        sa.Column('started_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('finished_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('item_count', sa.Integer, nullable=True),
        sa.Column('error_message', sa.Text, nullable=True),
    )
    op.create_index('ix_feed_runs_feed_name', 'feed_runs', ['feed_name'])
    op.create_index('ix_feed_runs_started_at', 'feed_runs', ['started_at'])

    # ── mitre_techniques ───────────────────────────────────────────────────────
    op.create_table(
        'mitre_techniques',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('stix_id', sa.String(100), nullable=False),
        sa.Column('technique_id', sa.String(20), nullable=False),
        sa.Column('source', sa.String(30), nullable=False),   # attack_v18 | attack_v19 | atlas
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('tactics', JSONB, nullable=False, server_default='[]'),
        sa.Column('platforms', JSONB, nullable=False, server_default='[]'),
        sa.Column('is_subtechnique', sa.Boolean, nullable=False, server_default='false'),
        sa.Column('deprecated', sa.Boolean, nullable=False, server_default='false'),
        sa.Column('url', sa.String(512), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.UniqueConstraint('stix_id', 'source', name='uq_mitre_techniques_stix_source'),
    )
    op.create_index('ix_mitre_techniques_source', 'mitre_techniques', ['source'])
    op.create_index('ix_mitre_techniques_technique_id', 'mitre_techniques', ['technique_id'])

    # ── cisa_kev_entries ───────────────────────────────────────────────────────
    op.create_table(
        'cisa_kev_entries',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('cve_id', sa.String(30), nullable=False, unique=True),
        sa.Column('vendor_project', sa.String(255), nullable=True),
        sa.Column('product', sa.String(255), nullable=True),
        sa.Column('vulnerability_name', sa.String(512), nullable=True),
        sa.Column('date_added', sa.Date, nullable=True),
        sa.Column('short_description', sa.Text, nullable=True),
        sa.Column('required_action', sa.Text, nullable=True),
        sa.Column('due_date', sa.Date, nullable=True),
        sa.Column('known_ransomware', sa.Boolean, nullable=False, server_default='false'),
        sa.Column('notes', sa.Text, nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
    )
    op.create_index('ix_cisa_kev_date_added', 'cisa_kev_entries', ['date_added'])
    op.create_index('ix_cisa_kev_known_ransomware', 'cisa_kev_entries', ['known_ransomware'])

    # ── epss_scores ────────────────────────────────────────────────────────────
    op.create_table(
        'epss_scores',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('cve_id', sa.String(30), nullable=False, unique=True),
        sa.Column('score', sa.Float, nullable=False),
        sa.Column('percentile', sa.Float, nullable=False),
        sa.Column('score_date', sa.Date, nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
    )
    op.create_index('ix_epss_scores_score', 'epss_scores', ['score'])
    op.create_index('ix_epss_scores_score_date', 'epss_scores', ['score_date'])


def downgrade():
    op.drop_table('epss_scores')
    op.drop_table('cisa_kev_entries')
    op.drop_table('mitre_techniques')
    op.drop_table('feed_runs')
