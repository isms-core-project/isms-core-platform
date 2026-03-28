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
    project_id: uuid.UUID | None = None


class GapPatch(BaseModel):
    gap_description: str | None = None
    severity: str | None = None
    status: str | None = None
    owner: str | None = None
    due_date: date | None = None
    remediation_plan: str | None = None
    closed_by: str | None = None
    # Risk fields — stored in metadata_ JSONB
    risk_level: str | None = None           # LOW | MEDIUM | HIGH | VERY_HIGH
    risk_likelihood: str | None = None      # low | medium | high
    risk_impact: str | None = None          # limited | considerable
    risk_treatment: str | None = None       # free text recommendation
    risk_bsi_threats: list[str] | None = None   # e.g. ["G 0.14", "G 0.28"]
    risk_assessed_by: str | None = None     # "auto" | "manual"


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
    # Risk fields — read from metadata_ JSONB
    risk_level: str | None = None
    risk_likelihood: str | None = None
    risk_impact: str | None = None
    risk_treatment: str | None = None
    risk_bsi_threats: list[str] = []
    risk_assessed_by: str | None = None     # "auto" | "manual" | null
    risk_assessed_at: str | None = None     # ISO timestamp string

    model_config = {"from_attributes": True}
