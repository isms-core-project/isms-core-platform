"""ITSM tickets — links gaps/remediation to external Jira/ServiceNow tickets.

Revision ID: 037
Revises: 036
Create Date: 2026-04-02
"""

from alembic import op

revision = '037'
down_revision = '036'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        CREATE TABLE IF NOT EXISTS itsm_tickets (
            id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            org_id              UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
            source_type         VARCHAR(20)  NOT NULL,   -- gap | remediation
            source_id           UUID         NOT NULL,
            connector_id        UUID NOT NULL REFERENCES connectors(id) ON DELETE CASCADE,
            external_ticket_id  VARCHAR(200) NOT NULL,
            external_url        VARCHAR(1000),
            status              VARCHAR(30)  NOT NULL DEFAULT 'open',
            last_synced_at      TIMESTAMPTZ,
            created_at          TIMESTAMPTZ  NOT NULL DEFAULT now()
        )
    """)
    op.execute("CREATE INDEX IF NOT EXISTS ix_itsm_tickets_org ON itsm_tickets(org_id)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_itsm_tickets_source ON itsm_tickets(source_type, source_id)")
    op.execute("CREATE UNIQUE INDEX IF NOT EXISTS uq_itsm_tickets_source_connector ON itsm_tickets(source_type, source_id, connector_id)")


def downgrade():
    op.execute("DROP TABLE IF EXISTS itsm_tickets")
