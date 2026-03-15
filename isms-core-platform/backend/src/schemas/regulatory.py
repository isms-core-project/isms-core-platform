"""Pydantic schemas for generic regulatory compliance assessment API (NIS2, DORA)."""

import uuid
from datetime import datetime

from pydantic import BaseModel


# ── Score labels ───────────────────────────────────────────────────────────────

SCORE_LABELS = {
    0: "Non-compliant",
    1: "Initial",
    2: "Developing",
    3: "Defined",
    4: "Optimised",
}

STATUS_LABELS = {
    "not_assessed": "Not Assessed",
    "not_applicable": "N/A",
    "non_compliant": "Non-Compliant",
    "partial": "Partial",
    "compliant": "Compliant",
}


# ── Requirement (a single assessable control from the framework) ───────────────

class RequirementRead(BaseModel):
    id: uuid.UUID
    control_id: str
    title: str
    description: str | None = None
    level: int
    sort_order: int
    group_id: str | None = None    # parent control_id (e.g. chapter for DORA)
    group_title: str | None = None


# ── Assessments ────────────────────────────────────────────────────────────────

class AssessmentCreate(BaseModel):
    framework_code: str
    name: str
    description: str | None = None
    assessor: str | None = None
    scope: str | None = None
    organisation: str | None = None


class AssessmentUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    assessor: str | None = None
    scope: str | None = None
    organisation: str | None = None
    status: str | None = None


class AssessmentRead(BaseModel):
    id: uuid.UUID
    framework_code: str
    name: str
    description: str | None
    assessor: str | None
    scope: str | None
    organisation: str | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class AssessmentSummary(AssessmentRead):
    rated_count: int = 0
    total_requirements: int = 0
    avg_current_score: float | None = None
    avg_target_score: float | None = None
    compliant_count: int = 0
    partial_count: int = 0
    non_compliant_count: int = 0
    not_applicable_count: int = 0


# ── Ratings ────────────────────────────────────────────────────────────────────

class RatingUpsert(BaseModel):
    requirement_id: uuid.UUID
    current_score: int | None = None
    target_score: int | None = None
    rating_status: str = "not_assessed"
    notes: str | None = None
    evidence_ref: str | None = None


class RatingRead(BaseModel):
    id: uuid.UUID
    assessment_id: uuid.UUID
    requirement_id: uuid.UUID
    requirement_control_id: str = ""
    requirement_title: str = ""
    group_id: str | None = None
    current_score: int | None
    target_score: int | None
    rating_status: str
    notes: str | None
    evidence_ref: str | None
    updated_at: datetime

    model_config = {"from_attributes": True}


# ── Full assessment (metadata + all ratings) ───────────────────────────────────

class FullAssessment(BaseModel):
    assessment: AssessmentRead
    requirements: list[RequirementRead]
    ratings: list[RatingRead]
