"""Phase 21 — QA Engine v2: add qa_keyword_translations table.

Revision ID: 043
Revises: 042
Create Date: 2026-04-03

Stores pre-translated ISO control keywords for FR/DE/IT so the keyword
QA check can match against documents in those languages without needing
a live translation service at runtime.

Seeded from datasets/data/qa_keyword_translations.json at bootstrap.
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision = "043"
down_revision = "042"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "qa_keyword_translations",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("keyword", sa.String(100), nullable=False),       # EN base keyword
        sa.Column("language", sa.String(5), nullable=False),        # 'fr' | 'de' | 'it'
        sa.Column("translation", sa.String(200), nullable=False),   # translated equivalent
        sa.Column("notes", sa.Text, nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.UniqueConstraint("keyword", "language", "translation", name="uq_kw_translation"),
    )
    op.create_index(
        "ix_qa_keyword_translations_keyword_lang",
        "qa_keyword_translations",
        ["keyword", "language"],
    )


def downgrade() -> None:
    op.drop_index("ix_qa_keyword_translations_keyword_lang", table_name="qa_keyword_translations")
    op.drop_table("qa_keyword_translations")
