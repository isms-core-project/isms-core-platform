"""Multi-organisation architecture (Phase 11)

Adds organisation_id FK to users, projects, connectors.
Adds active_projects JSONB to users.
Drops org_name from projects (replaced by organisation.name).
Adds super_admin to user_role enum.
Data migration: assigns all existing rows to the default (first) organisation.

Revision ID: 031_multi_org
Revises: 030_add_sec_product
Create Date: 2026-04-02
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB, UUID

revision = "031_multi_org"
down_revision = "030_add_sec_product"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 1. Extend user_role enum with super_admin
    op.execute("ALTER TYPE user_role ADD VALUE IF NOT EXISTS 'super_admin'")

    # 2. Add active_projects JSONB to users
    op.add_column(
        "users",
        sa.Column("active_projects", JSONB, nullable=False, server_default="{}"),
    )

    # 3. Add organisation_id (nullable) to users, projects, connectors
    op.add_column(
        "users",
        sa.Column("organisation_id", UUID(as_uuid=True), nullable=True),
    )
    op.add_column(
        "projects",
        sa.Column("organisation_id", UUID(as_uuid=True), nullable=True),
    )
    op.add_column(
        "connectors",
        sa.Column("organisation_id", UUID(as_uuid=True), nullable=True),
    )

    # 4. Data migration — assign all existing rows to the default org
    op.execute("""
        UPDATE users
           SET organisation_id = (SELECT id FROM organisations ORDER BY created_at LIMIT 1)
         WHERE organisation_id IS NULL
    """)
    op.execute("""
        UPDATE projects
           SET organisation_id = (SELECT id FROM organisations ORDER BY created_at LIMIT 1)
         WHERE organisation_id IS NULL
    """)
    op.execute("""
        UPDATE connectors
           SET organisation_id = (SELECT id FROM organisations ORDER BY created_at LIMIT 1)
         WHERE organisation_id IS NULL
    """)

    # 5. Make NOT NULL and add FK constraints
    op.alter_column("users", "organisation_id", nullable=False)
    op.alter_column("projects", "organisation_id", nullable=False)
    op.alter_column("connectors", "organisation_id", nullable=False)

    op.create_foreign_key(
        "fk_users_organisation_id",
        "users", "organisations",
        ["organisation_id"], ["id"],
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        "fk_projects_organisation_id",
        "projects", "organisations",
        ["organisation_id"], ["id"],
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        "fk_connectors_organisation_id",
        "connectors", "organisations",
        ["organisation_id"], ["id"],
        ondelete="RESTRICT",
    )

    # 6. Drop org_name from projects (now derived from organisation.name)
    op.drop_column("projects", "org_name")


def downgrade() -> None:
    # Re-add org_name (populated from organisation name for continuity)
    op.add_column(
        "projects",
        sa.Column("org_name", sa.String(255), nullable=True),
    )
    op.execute("""
        UPDATE projects p
           SET org_name = o.name
          FROM organisations o
         WHERE p.organisation_id = o.id
    """)
    op.alter_column("projects", "org_name", nullable=False)

    # Drop FK constraints and columns
    op.drop_constraint("fk_connectors_organisation_id", "connectors", type_="foreignkey")
    op.drop_constraint("fk_projects_organisation_id", "projects", type_="foreignkey")
    op.drop_constraint("fk_users_organisation_id", "users", type_="foreignkey")

    op.drop_column("connectors", "organisation_id")
    op.drop_column("projects", "organisation_id")
    op.drop_column("users", "organisation_id")
    op.drop_column("users", "active_projects")

    # Note: super_admin enum value cannot be removed from Postgres without
    # dropping and recreating the type (destructive — manual step if needed).
