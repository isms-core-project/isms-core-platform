"""Pydantic schemas for evidence upload and retrieval."""

import uuid
from datetime import date, datetime

from pydantic import BaseModel, Field


class EvidenceRead(BaseModel):
    id: uuid.UUID
    control_group_id: uuid.UUID | None = None
    requirement_id: uuid.UUID | None = None
    assessment_item_id: uuid.UUID | None = None
    evidence_type: str
    evidence_status: str = "active"
    title: str
    file_path: str
    collected_date: date | None = None
    expires_date: date | None = None
    verified_by: str | None = None
    verified_date: date | None = None
    created_at: datetime
    metadata: dict = Field(default={}, validation_alias="metadata_")

    model_config = {"from_attributes": True}


class EvidenceUpdate(BaseModel):
    title: str | None = None
    evidence_type: str | None = None
    collected_date: date | None = None
    expires_date: date | None = None
    verified_by: str | None = None
    verified_date: date | None = None
    notes: str | None = None


class EvidenceAssign(BaseModel):
    """Assign a draft evidence item to a control group."""
    group_code: str | None = None
    control_group_id: uuid.UUID | None = None
    require_approval: bool = False  # True → status becomes pending_review; False → active


class EvidenceReview(BaseModel):
    """Approve or reject a pending_review evidence item."""
    reason: str | None = None
