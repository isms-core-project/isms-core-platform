"""Organisation domain model — Phase 7.15 (governance mode schema)."""

import uuid

from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base, SAEnum, TimestampMixin
from src.database.enums import GovernanceMode, PrivacyRole


class Organisation(TimestampMixin, Base):
    """Represents an ISMS CORE installation (single-tenant — one row expected).

    governance_mode controls how policy content authority works:
      - platform: WebUI edits flow DB → publish as MD (Platform mode)
      - local:    File edits flow file → import → DB read-only view (Local mode)
    """

    __tablename__ = "organisations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    governance_mode: Mapped[GovernanceMode] = mapped_column(
        SAEnum(GovernanceMode, name="governance_mode", create_type=False),
        nullable=False,
        server_default="platform",
    )
    privacy_role: Mapped[PrivacyRole] = mapped_column(
        SAEnum(PrivacyRole, name="privacyrole", create_type=False),
        nullable=False,
        server_default="BOTH",
    )
    description: Mapped[str | None] = mapped_column(Text)
    settings: Mapped[dict] = mapped_column(
        JSONB, default=dict, server_default="{}"
    )
