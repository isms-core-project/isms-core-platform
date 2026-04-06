"""Pydantic schemas for Phase 25 — Threat Intelligence & Vulnerability Feeds."""

from __future__ import annotations

import uuid
from datetime import date, datetime
from typing import Any

from pydantic import BaseModel


# ── Feed status ────────────────────────────────────────────────────────────────

class FeedRunRead(BaseModel):
    id: uuid.UUID
    feed_name: str
    status: str
    started_at: datetime
    finished_at: datetime | None
    item_count: int | None
    error_message: str | None

    model_config = {"from_attributes": True}


class FeedStatusItem(BaseModel):
    feed_name: str
    display_name: str
    enabled: bool
    last_run: datetime | None
    last_status: str | None
    item_count: int | None
    error_message: str | None


class FeedStatusResponse(BaseModel):
    feeds: list[FeedStatusItem]


# ── MITRE techniques ───────────────────────────────────────────────────────────

class MitreTechniqueRead(BaseModel):
    id: uuid.UUID
    stix_id: str
    technique_id: str
    source: str
    name: str
    description: str | None
    tactics: list[str]
    platforms: list[str]
    is_subtechnique: bool
    deprecated: bool
    url: str | None

    model_config = {"from_attributes": True}


class MitreTechniqueList(BaseModel):
    items: list[MitreTechniqueRead]
    total: int
    page: int
    per_page: int


class MitreAttackStats(BaseModel):
    total_techniques: int
    total_subtechniques: int
    deprecated_count: int
    tactic_counts: dict[str, int]      # tactic_name → count
    platform_counts: dict[str, int]    # platform → count
    sources: list[str]


# ── CISA KEV ───────────────────────────────────────────────────────────────────

class CisaKevRead(BaseModel):
    id: uuid.UUID
    cve_id: str
    vendor_project: str | None
    product: str | None
    vulnerability_name: str | None
    date_added: date | None
    short_description: str | None
    required_action: str | None
    due_date: date | None
    known_ransomware: bool
    notes: str | None

    model_config = {"from_attributes": True}


class CisaKevList(BaseModel):
    items: list[CisaKevRead]
    total: int
    page: int
    per_page: int


class CisaKevStats(BaseModel):
    total_entries: int
    ransomware_count: int
    recent_30d: int
    by_month: list[dict[str, Any]]     # [{month: "2025-01", count: 12}, ...]


# ── EPSS ───────────────────────────────────────────────────────────────────────

class EpssScoreRead(BaseModel):
    id: uuid.UUID
    cve_id: str
    score: float
    percentile: float
    score_date: date | None

    model_config = {"from_attributes": True}


class EpssScoreList(BaseModel):
    items: list[EpssScoreRead]
    total: int
    page: int
    per_page: int
