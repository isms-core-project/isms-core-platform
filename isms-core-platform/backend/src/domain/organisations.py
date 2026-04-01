"""Organisation domain model — multi-tenant entity (Phase 11)."""

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base, SAEnum, TimestampMixin
from src.database.enums import GovernanceMode, PrivacyRole

if TYPE_CHECKING:
    from src.domain.users import User
    from src.domain.projects import Project
    from src.domain.connectors import Connector


class Organisation(TimestampMixin, Base):
    """A tenant in the ISMS CORE platform.

    One Organisation per client/company. Users, Projects, and Connectors all
    belong to an Organisation. A platform-level super_admin can cross org
    boundaries; all other roles are scoped to their own org.

    governance_mode controls policy content authority:
      - platform: WebUI edits flow DB → publish as MD
      - local:    File edits flow file → import → DB read-only view
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

    # Relationships
    users: Mapped[list["User"]] = relationship(back_populates="organisation")
    projects: Mapped[list["Project"]] = relationship(back_populates="organisation")
    connectors: Mapped[list["Connector"]] = relationship(back_populates="organisation")
