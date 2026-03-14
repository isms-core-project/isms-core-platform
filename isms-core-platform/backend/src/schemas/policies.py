"""Pydantic schemas for policy and requirement API responses."""

import uuid
from datetime import datetime

from pydantic import BaseModel, Field

from src.database.enums import ContentState


class RequirementRead(BaseModel):
    id: uuid.UUID
    policy_id: uuid.UUID
    control_group_id: uuid.UUID
    requirement_text: str
    section_heading: str | None = None
    requirement_type: str = "mandatory"
    domain_area: str | None = None
    sort_order: int = 0
    compliance_status: str = "not_assessed"
    evidence_count: int = 0
    metadata: dict = Field(default={}, validation_alias="metadata_")

    model_config = {"from_attributes": True}


class PolicyRead(BaseModel):
    id: uuid.UUID
    control_group_id: uuid.UUID
    product_type: str
    policy_type: str
    document_id: str
    title: str
    file_path: str
    content_hash: str | None = None
    word_count: int | None = None
    requirements_count: int | None = 0
    last_parsed: datetime | None = None
    content_state: ContentState = ContentState.PUBLISHED
    metadata: dict = Field(default={}, validation_alias="metadata_")

    model_config = {"from_attributes": True}


class PolicyStateUpdate(BaseModel):
    state: ContentState


class PolicyDetail(PolicyRead):
    requirements: list[RequirementRead] = []


class PolicyListRead(BaseModel):
    """PolicyRead enriched with control group info for list views."""
    id: uuid.UUID
    control_group_id: uuid.UUID
    group_code: str
    group_name: str
    product_type: str
    policy_type: str
    document_id: str
    title: str
    word_count: int | None = None
    requirements_count: int | None = 0
    last_parsed: datetime | None = None
    content_state: ContentState = ContentState.PUBLISHED

    model_config = {"from_attributes": True}
