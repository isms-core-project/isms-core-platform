"""Pydantic schemas for NIST CSF 2.0 assessment API."""

import uuid
from datetime import datetime

from pydantic import BaseModel


# ── Profiles ──────────────────────────────────────────────────────────────────

class NistProfileCreate(BaseModel):
    name: str
    description: str | None = None
    assessor: str | None = None
    scope: str | None = None


class NistProfileUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    assessor: str | None = None
    scope: str | None = None
    status: str | None = None


class NistProfileRead(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None
    assessor: str | None
    scope: str | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class FunctionScore(BaseModel):
    function_code: str
    function_name: str
    avg_current: float | None = None
    avg_target: float | None = None
    rated_count: int = 0
    total_count: int = 0


class NistProfileSummary(NistProfileRead):
    rated_count: int = 0
    total_subcategories: int = 106
    avg_current_tier: float | None = None
    avg_target_tier: float | None = None
    function_scores: list[FunctionScore] = []


# ── Ratings ───────────────────────────────────────────────────────────────────

class NistRatingUpsert(BaseModel):
    subcategory_id: uuid.UUID
    current_tier: int | None = None
    target_tier: int | None = None
    notes: str | None = None


class NistRatingRead(BaseModel):
    id: uuid.UUID
    profile_id: uuid.UUID
    subcategory_id: uuid.UUID
    subcategory_code: str = ""
    subcategory_title: str = ""
    function_code: str = ""
    category_code: str = ""
    current_tier: int | None
    target_tier: int | None
    notes: str | None
    iso_mappings: list[str] = []

    model_config = {"from_attributes": True}


# ── Subcategory (seed for UI grid) ────────────────────────────────────────────

class NistSubcategory(BaseModel):
    id: uuid.UUID
    control_id: str
    title: str
    function_code: str
    category_code: str
    sort_order: int
    iso_mappings: list[str] = []


# ── Full profile ──────────────────────────────────────────────────────────────

class NistFullProfile(BaseModel):
    profile: NistProfileRead
    ratings: list[NistRatingRead]


# ── Import result ─────────────────────────────────────────────────────────────

class NistImportResult(BaseModel):
    imported: int
    skipped: int
    not_found: list[str] = []
