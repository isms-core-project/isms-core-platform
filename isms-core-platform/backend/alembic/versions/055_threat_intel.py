"""Create threat intelligence tables (ti_*).

Revision ID: 055
Revises: 054
Create Date: 2026-04-26
"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB, UUID

revision = "055"
down_revision = "054"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # IOC store — deduplicated by (ioc_type, value, source)
    op.create_table(
        "ti_iocs",
        sa.Column("id",           UUID(),                       nullable=False),
        sa.Column("ioc_type",     sa.String(20),                nullable=False),   # ip|domain|url|md5|sha1|sha256
        sa.Column("value",        sa.Text(),                    nullable=False),
        sa.Column("source",       sa.String(50),                nullable=False),   # circl_misp|botvrij_misp|abuseipdb
        sa.Column("confidence",   sa.Integer(),                 nullable=True),    # 0-100
        sa.Column("tags",         JSONB(),                      nullable=False, server_default=sa.text("'[]'")),
        sa.Column("mitre_tids",   JSONB(),                      nullable=False, server_default=sa.text("'[]'")),
        sa.Column("family_slugs", JSONB(),                      nullable=False, server_default=sa.text("'[]'")),
        sa.Column("actor_slugs",  JSONB(),                      nullable=False, server_default=sa.text("'[]'")),
        sa.Column("event_uuids",  JSONB(),                      nullable=False, server_default=sa.text("'[]'")),  # source event refs
        sa.Column("first_seen",   sa.DateTime(timezone=True),   nullable=True),
        sa.Column("last_seen",    sa.DateTime(timezone=True),   nullable=True),
        sa.Column("raw",          JSONB(),                      nullable=True),
        sa.Column("created_at",   sa.DateTime(timezone=True),   nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("ioc_type", "value", "source", name="uq_ti_iocs_type_value_source"),
    )
    op.create_index("ix_ti_iocs_ioc_type",    "ti_iocs", ["ioc_type"])
    op.create_index("ix_ti_iocs_source",      "ti_iocs", ["source"])
    op.create_index("ix_ti_iocs_last_seen",   "ti_iocs", ["last_seen"])
    op.create_index("ix_ti_iocs_value",       "ti_iocs", ["value"])

    # Malware families from Malpedia
    op.create_table(
        "ti_malware_families",
        sa.Column("id",          UUID(),                       nullable=False),
        sa.Column("slug",        sa.String(200),               nullable=False),
        sa.Column("name",        sa.String(200),               nullable=False),
        sa.Column("aliases",     JSONB(),                      nullable=False, server_default=sa.text("'[]'")),
        sa.Column("description", sa.Text(),                    nullable=True),
        sa.Column("actor_slugs", JSONB(),                      nullable=False, server_default=sa.text("'[]'")),
        sa.Column("mitre_tids",  JSONB(),                      nullable=False, server_default=sa.text("'[]'")),
        sa.Column("updated_at",  sa.DateTime(timezone=True),   nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    op.create_index("ix_ti_malware_name", "ti_malware_families", ["name"])

    # Threat actors from Malpedia
    op.create_table(
        "ti_actors",
        sa.Column("id",          UUID(),                       nullable=False),
        sa.Column("slug",        sa.String(200),               nullable=False),
        sa.Column("name",        sa.String(200),               nullable=False),
        sa.Column("country",     sa.String(5),                 nullable=True),   # ISO-3166-1 alpha-2
        sa.Column("motivation",  sa.String(100),               nullable=True),
        sa.Column("description", sa.Text(),                    nullable=True),
        sa.Column("updated_at",  sa.DateTime(timezone=True),   nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    op.create_index("ix_ti_actors_country", "ti_actors", ["country"])

    # On-demand enrichment cache — 24h TTL enforced by application
    op.create_table(
        "ti_enrichment_cache",
        sa.Column("ip",          sa.String(45),                nullable=False),   # IPv4 or IPv6
        sa.Column("abuseipdb",   JSONB(),                      nullable=True),
        sa.Column("shodan",      JSONB(),                      nullable=True),
        sa.Column("cached_at",   sa.DateTime(timezone=True),   nullable=False),
        sa.PrimaryKeyConstraint("ip"),
    )

    # MISP feed delta state — tracks processed event UUIDs per source
    op.create_table(
        "ti_misp_state",
        sa.Column("source",       sa.String(50),               nullable=False),   # circl_misp|botvrij_misp
        sa.Column("event_uuid",   sa.String(36),               nullable=False),
        sa.Column("processed_at", sa.DateTime(timezone=True),  nullable=False),
        sa.PrimaryKeyConstraint("source", "event_uuid"),
    )
    op.create_index("ix_ti_misp_state_source", "ti_misp_state", ["source"])


def downgrade() -> None:
    op.drop_table("ti_misp_state")
    op.drop_table("ti_enrichment_cache")
    op.drop_table("ti_actors")
    op.drop_table("ti_malware_families")
    op.drop_table("ti_iocs")
