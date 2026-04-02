"""Pydantic schemas for Risk Register (risk_matrices + risk_scenarios)."""

import uuid
from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field

# ── Default 5×5 matrix seed data ─────────────────────────────────────────────

DEFAULT_PROBABILITY_LABELS = ["Rare", "Unlikely", "Possible", "Likely", "Almost Certain"]
DEFAULT_IMPACT_LABELS      = ["Negligible", "Minor", "Moderate", "Major", "Critical"]

# score_map: "probability,impact" → numeric score
DEFAULT_SCORE_MAP = {
    "1,1": 1,  "1,2": 2,  "1,3": 3,  "1,4": 4,  "1,5": 5,
    "2,1": 2,  "2,2": 4,  "2,3": 6,  "2,4": 8,  "2,5": 10,
    "3,1": 3,  "3,2": 6,  "3,3": 9,  "3,4": 12, "3,5": 15,
    "4,1": 4,  "4,2": 8,  "4,3": 12, "4,4": 16, "4,5": 20,
    "5,1": 5,  "5,2": 10, "5,3": 15, "5,4": 20, "5,5": 25,
}

# colour_map: score → level string
DEFAULT_COLOUR_MAP = {
    str(s): "low"      for s in range(1,  4)
}
DEFAULT_COLOUR_MAP.update({str(s): "medium"   for s in range(4,  9)})
DEFAULT_COLOUR_MAP.update({str(s): "high"     for s in range(9,  17)})
DEFAULT_COLOUR_MAP.update({str(s): "critical" for s in range(17, 26)})


# ── RiskMatrix ────────────────────────────────────────────────────────────────

class RiskMatrixRead(BaseModel):
    id:                 uuid.UUID
    org_id:             uuid.UUID
    name:               str
    probability_labels: list[str]
    impact_labels:      list[str]
    score_map:          dict[str, int]
    colour_map:         dict[str, str]
    is_default:         bool
    created_at:         datetime

    model_config = {"from_attributes": True}


class RiskMatrixPatch(BaseModel):
    name:               Optional[str]            = None
    probability_labels: Optional[list[str]]      = None
    impact_labels:      Optional[list[str]]      = None
    score_map:          Optional[dict[str, int]] = None
    colour_map:         Optional[dict[str, str]] = None


# ── RiskScenario ──────────────────────────────────────────────────────────────

class RiskScenarioCreate(BaseModel):
    name:                 str              = Field(..., min_length=1, max_length=255)
    description:          Optional[str]    = None
    threat_source:        Optional[str]    = None
    threat_event:         Optional[str]    = None
    probability:          int              = Field(default=1, ge=1, le=5)
    impact:               int              = Field(default=1, ge=1, le=5)
    treatment_status:     str              = "pending"
    treatment_notes:      Optional[str]    = None
    residual_probability: Optional[int]    = Field(default=None, ge=1, le=5)
    residual_impact:      Optional[int]    = Field(default=None, ge=1, le=5)
    owner_id:             Optional[uuid.UUID] = None
    target_date:          Optional[date]   = None
    status:               str              = "open"
    project_id:           Optional[uuid.UUID] = None
    control_group_id:     Optional[uuid.UUID] = None


class RiskScenarioPatch(BaseModel):
    name:                 Optional[str]         = None
    description:          Optional[str]         = None
    threat_source:        Optional[str]         = None
    threat_event:         Optional[str]         = None
    probability:          Optional[int]         = Field(default=None, ge=1, le=5)
    impact:               Optional[int]         = Field(default=None, ge=1, le=5)
    treatment_status:     Optional[str]         = None
    treatment_notes:      Optional[str]         = None
    residual_probability: Optional[int]         = Field(default=None, ge=1, le=5)
    residual_impact:      Optional[int]         = Field(default=None, ge=1, le=5)
    owner_id:             Optional[uuid.UUID]   = None
    target_date:          Optional[date]        = None
    status:               Optional[str]         = None
    project_id:           Optional[uuid.UUID]   = None
    control_group_id:     Optional[uuid.UUID]   = None


class RiskScenarioRead(BaseModel):
    id:                   uuid.UUID
    org_id:               uuid.UUID
    project_id:           Optional[uuid.UUID]
    control_group_id:     Optional[uuid.UUID]
    control_group_code:   Optional[str]          = None   # resolved by service
    name:                 str
    description:          Optional[str]
    threat_source:        Optional[str]
    threat_event:         Optional[str]
    probability:          int
    impact:               int
    risk_score:           int
    risk_level:           str
    treatment_status:     str
    treatment_notes:      Optional[str]
    residual_probability: Optional[int]
    residual_impact:      Optional[int]
    residual_score:       Optional[int]
    residual_level:       Optional[str]
    owner_id:             Optional[uuid.UUID]
    owner_name:           Optional[str]          = None   # resolved by service
    target_date:          Optional[date]
    status:               str
    created_at:           datetime
    updated_at:           datetime

    model_config = {"from_attributes": True}


class RiskSummary(BaseModel):
    total:    int
    critical: int
    high:     int
    medium:   int
    low:      int
    open:     int
    accepted: int
    in_treatment: int
    closed:   int


# ── RiskAcceptance ────────────────────────────────────────────────────────────

class RiskAcceptanceCreate(BaseModel):
    justification: str = Field(..., min_length=1)
    expiry_date:   Optional[date] = None


class RiskAcceptanceRead(BaseModel):
    id:               uuid.UUID
    risk_scenario_id: uuid.UUID
    approver_id:      Optional[uuid.UUID]
    approver_name:    str
    justification:    str
    expiry_date:      Optional[date]
    status:           str
    revoked_by:       Optional[uuid.UUID]
    revoked_at:       Optional[datetime]
    created_at:       datetime

    model_config = {"from_attributes": True}


# ── RemediationAction ─────────────────────────────────────────────────────────

class RemediationActionCreate(BaseModel):
    title:            str              = Field(..., min_length=1, max_length=255)
    description:      Optional[str]    = None
    status:           str              = "planned"
    owner_id:         Optional[uuid.UUID] = None
    eta:              Optional[date]   = None
    effort:           Optional[str]    = None
    cost_estimate:    Optional[float]  = None
    progress:         int              = Field(default=0, ge=0, le=100)
    project_id:       Optional[uuid.UUID] = None
    risk_scenario_id: Optional[uuid.UUID] = None
    gap_id:           Optional[uuid.UUID] = None
    control_group_id: Optional[uuid.UUID] = None
    evidence_id:      Optional[uuid.UUID] = None


class RemediationActionPatch(BaseModel):
    title:            Optional[str]       = None
    description:      Optional[str]       = None
    status:           Optional[str]       = None
    owner_id:         Optional[uuid.UUID] = None
    eta:              Optional[date]      = None
    effort:           Optional[str]       = None
    cost_estimate:    Optional[float]     = None
    progress:         Optional[int]       = Field(default=None, ge=0, le=100)
    project_id:       Optional[uuid.UUID] = None
    risk_scenario_id: Optional[uuid.UUID] = None
    gap_id:           Optional[uuid.UUID] = None
    control_group_id: Optional[uuid.UUID] = None
    evidence_id:      Optional[uuid.UUID] = None


class RemediationActionRead(BaseModel):
    id:               uuid.UUID
    org_id:           uuid.UUID
    title:            str
    description:      Optional[str]
    status:           str
    owner_id:         Optional[uuid.UUID]
    owner_name:       Optional[str]       = None
    eta:              Optional[date]
    effort:           Optional[str]
    cost_estimate:    Optional[float]
    progress:         int
    project_id:       Optional[uuid.UUID]
    risk_scenario_id: Optional[uuid.UUID]
    risk_name:        Optional[str]       = None
    gap_id:           Optional[uuid.UUID]
    control_group_id: Optional[uuid.UUID]
    evidence_id:      Optional[uuid.UUID]
    created_at:       datetime
    updated_at:       datetime

    model_config = {"from_attributes": True}


class RemediationSummary(BaseModel):
    total:       int
    planned:     int
    in_progress: int
    completed:   int
    cancelled:   int
    overdue:     int
