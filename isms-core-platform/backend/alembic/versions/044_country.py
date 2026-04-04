"""Phase 22 — Country localisation: add country column to organisations.

Revision ID: 044
Revises: 043
Create Date: 2026-04-04

Adds an optional ISO 3166-1 alpha-2 country code to each organisation.
None / NULL means Switzerland (CH) — the default, no token substitution.
When set to a supported country (fr, be, lu, de, at, it), policy content
is rendered with country-specific regulatory token substitutions at request time.
"""

from alembic import op
import sqlalchemy as sa

revision = "044"
down_revision = "043"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "organisations",
        sa.Column(
            "country",
            sa.String(2),
            nullable=True,
            comment="ISO 3166-1 alpha-2 country code. NULL = Switzerland (CH, default).",
        ),
    )


def downgrade() -> None:
    op.drop_column("organisations", "country")
