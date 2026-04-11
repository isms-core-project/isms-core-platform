"""Phase 28 — MITRE ATT&CK Groups, Software, Campaigns, Relationships.

Revision ID: 049
Revises: 048
Create Date: 2026-04-11

New tables:
  mitre_groups         — intrusion-set objects (threat actor groups)
  mitre_software       — malware + tool objects
  mitre_campaigns      — campaign objects
  mitre_relationships  — relationship objects (group→technique, software→technique, etc.)
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB, UUID

revision = '049'
down_revision = '048'
branch_labels = None
depends_on = None


def upgrade():
    # ── mitre_groups ───────────────────────────────────────────────────────────
    op.create_table(
        'mitre_groups',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('stix_id',    sa.String(100), nullable=False),
        sa.Column('source',     sa.String(30),  nullable=False),
        sa.Column('group_id',   sa.String(20),  nullable=False),
        sa.Column('name',       sa.String(255), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('aliases',    JSONB, nullable=False, server_default='[]'),
        sa.Column('deprecated', sa.Boolean, nullable=False, server_default='false'),
        sa.Column('url',        sa.String(512), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.UniqueConstraint('stix_id', 'source', name='uq_mitre_groups_stix_source'),
    )
    op.create_index('ix_mitre_groups_source',   'mitre_groups', ['source'])
    op.create_index('ix_mitre_groups_group_id', 'mitre_groups', ['group_id'])

    # ── mitre_software ─────────────────────────────────────────────────────────
    op.create_table(
        'mitre_software',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('stix_id',       sa.String(100), nullable=False),
        sa.Column('source',        sa.String(30),  nullable=False),
        sa.Column('software_id',   sa.String(20),  nullable=False),
        sa.Column('name',          sa.String(255), nullable=False),
        sa.Column('software_type', sa.String(20),  nullable=False),  # malware | tool
        sa.Column('description',   sa.Text, nullable=True),
        sa.Column('aliases',       JSONB, nullable=False, server_default='[]'),
        sa.Column('platforms',     JSONB, nullable=False, server_default='[]'),
        sa.Column('deprecated',    sa.Boolean, nullable=False, server_default='false'),
        sa.Column('url',           sa.String(512), nullable=True),
        sa.Column('created_at',    sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at',    sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.UniqueConstraint('stix_id', 'source', name='uq_mitre_software_stix_source'),
    )
    op.create_index('ix_mitre_software_source',      'mitre_software', ['source'])
    op.create_index('ix_mitre_software_software_id', 'mitre_software', ['software_id'])
    op.create_index('ix_mitre_software_type',        'mitre_software', ['software_type'])

    # ── mitre_campaigns ────────────────────────────────────────────────────────
    op.create_table(
        'mitre_campaigns',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('stix_id',      sa.String(100), nullable=False),
        sa.Column('source',       sa.String(30),  nullable=False),
        sa.Column('campaign_id',  sa.String(20),  nullable=False),
        sa.Column('name',         sa.String(255), nullable=False),
        sa.Column('description',  sa.Text, nullable=True),
        sa.Column('aliases',      JSONB, nullable=False, server_default='[]'),
        sa.Column('first_seen',   sa.Date, nullable=True),
        sa.Column('last_seen',    sa.Date, nullable=True),
        sa.Column('deprecated',   sa.Boolean, nullable=False, server_default='false'),
        sa.Column('url',          sa.String(512), nullable=True),
        sa.Column('created_at',   sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at',   sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.UniqueConstraint('stix_id', 'source', name='uq_mitre_campaigns_stix_source'),
    )
    op.create_index('ix_mitre_campaigns_source',      'mitre_campaigns', ['source'])
    op.create_index('ix_mitre_campaigns_campaign_id', 'mitre_campaigns', ['campaign_id'])

    # ── mitre_relationships ────────────────────────────────────────────────────
    op.create_table(
        'mitre_relationships',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('stix_id',           sa.String(100), nullable=False),
        sa.Column('source',            sa.String(30),  nullable=False),
        sa.Column('relationship_type', sa.String(50),  nullable=False),
        sa.Column('source_ref',        sa.String(100), nullable=False),
        sa.Column('target_ref',        sa.String(100), nullable=False),
        sa.Column('source_type',       sa.String(50),  nullable=False),
        sa.Column('target_type',       sa.String(50),  nullable=False),
        sa.Column('description',       sa.Text, nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.UniqueConstraint('stix_id', 'source', name='uq_mitre_relationships_stix_source'),
    )
    op.create_index('ix_mitre_rel_source',      'mitre_relationships', ['source'])
    op.create_index('ix_mitre_rel_type',        'mitre_relationships', ['relationship_type'])
    op.create_index('ix_mitre_rel_source_ref',  'mitre_relationships', ['source_ref'])
    op.create_index('ix_mitre_rel_target_ref',  'mitre_relationships', ['target_ref'])


def downgrade():
    op.drop_table('mitre_relationships')
    op.drop_table('mitre_campaigns')
    op.drop_table('mitre_software')
    op.drop_table('mitre_groups')
