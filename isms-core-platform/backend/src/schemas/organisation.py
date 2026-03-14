"""Pydantic schemas for Organisation — Phase 7.15."""

import uuid
from datetime import datetime

from pydantic import BaseModel, computed_field

from src.database.enums import GovernanceMode, PrivacyRole


class OrganisationRead(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    governance_mode: GovernanceMode
    privacy_role: PrivacyRole
    description: str | None
    settings: dict
    created_at: datetime
    updated_at: datetime

    @computed_field  # type: ignore[prop-decorator]
    @property
    def is_editable_in_ui(self) -> bool:
        """True when governance_mode is 'platform' — frontend uses this to show/hide edit controls."""
        return self.governance_mode == GovernanceMode.PLATFORM

    model_config = {"from_attributes": True}


class OrganisationUpdate(BaseModel):
    name: str | None = None
    governance_mode: GovernanceMode | None = None
    privacy_role: PrivacyRole | None = None
    description: str | None = None
    settings: dict | None = None
