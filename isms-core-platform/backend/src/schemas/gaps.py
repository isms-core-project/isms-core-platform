import uuid
from datetime import date, datetime

from pydantic import BaseModel


class GapCreate(BaseModel):
    control_group_id: uuid.UUID
    gap_description: str
    severity: str = "medium"          # critical | high | medium | low
    product_type: str = "both"        # framework | operational | both
    owner: str | None = None
    due_date: date | None = None
    remediation_plan: str | None = None
    requirement_id: uuid.UUID | None = None
    workbook_document_id: str | None = None  # e.g. ISMS-IMP-A.7.4-5-11-S1 — stored in metadata_


class GapPatch(BaseModel):
    gap_description: str | None = None
    severity: str | None = None
    status: str | None = None
    owner: str | None = None
    due_date: date | None = None
    remediation_plan: str | None = None
    closed_by: str | None = None


class GapRead(BaseModel):
    id: uuid.UUID
    control_group_id: uuid.UUID
    control_group_code: str
    control_group_name: str
    gap_description: str
    severity: str
    status: str
    product_type: str
    owner: str | None
    due_date: date | None
    remediation_plan: str | None
    closed_date: date | None
    closed_by: str | None
    created_at: datetime
    evidence_count: int = 0

    model_config = {"from_attributes": True}
