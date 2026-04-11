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


# ── KEV Audit Report (Phase 26 Task 26.7) ─────────────────────────────────────

class KevAuditEntry(BaseModel):
    cve_id: str
    vulnerability_name: str | None
    vendor_project: str | None
    product: str | None
    date_added: date | None
    due_date: date | None
    known_ransomware: bool
    evidence_status: str           # 'no_evidence' | evidence_status values
    evidence_id: str | None
    evidence_title: str | None


class KevAuditReport(BaseModel):
    total: int
    covered: int                   # entries that have at least one evidence item
    uncovered: int                 # entries with no evidence
    ransomware_uncovered: int      # ransomware entries with no evidence
    months: int
    generated_at: str
    entries: list[KevAuditEntry]


# ── NVD CVE / CPE (Phase 27) ──────────────────────────────────────────────────

class NvdCveEntry(BaseModel):
    cve_id: str
    published: str | None
    last_modified: str | None
    vuln_status: str | None
    description: str | None
    cvss_v3_score: float | None
    cvss_v3_severity: str | None
    cvss_v3_vector: str | None
    cvss_v2_score: float | None
    cwe_ids: list[str]
    cpe_affected: list[str]
    in_kev: bool
    epss_score: float | None
    references: list[str]


class NvdCveList(BaseModel):
    items: list[NvdCveEntry]
    total: int
    page: int
    per_page: int


class NvdCveStats(BaseModel):
    total: int
    critical: int
    high: int
    medium: int
    low: int
    in_kev: int
    with_epss: int
    last_indexed: str | None


class NvdCpeEntry(BaseModel):
    cpe_uri: str
    part: str | None
    vendor: str | None
    product: str | None
    version: str | None
    title: str | None
    in_kev: bool
    source: str | None


class NvdCpeList(BaseModel):
    items: list[NvdCpeEntry]
    total: int
    page: int
    per_page: int


class NvdCpeStats(BaseModel):
    total: int
    kev_vendor: int
    cve_config: int
    applications: int
    operating_systems: int
    hardware: int


class NvdIndexStats(BaseModel):
    """Combined stats for the CVE Explorer banner."""
    cve_total: int
    cpe_total: int
    kev_total: int
    last_cve_sync: str | None
    last_cpe_sync: str | None
    nist_api_key_configured: bool
    cpe_full_enabled: bool


class FeedSettings(BaseModel):
    """Platform-level feed toggle settings (stored in platform_settings table)."""
    feeds_cpe_full: bool


# ── MITRE Groups (Phase 28) ────────────────────────────────────────────────────

class MitreGroupRead(BaseModel):
    id: uuid.UUID
    stix_id: str
    source: str
    group_id: str
    name: str
    description: str | None
    aliases: list[str]
    deprecated: bool
    url: str | None

    model_config = {"from_attributes": True}


class MitreGroupList(BaseModel):
    items: list[MitreGroupRead]
    total: int
    page: int
    per_page: int


class MitreGroupStats(BaseModel):
    total_groups: int
    deprecated_count: int
    sources: list[str]


# ── MITRE Software (Phase 28) ──────────────────────────────────────────────────

class MitreSoftwareRead(BaseModel):
    id: uuid.UUID
    stix_id: str
    source: str
    software_id: str
    name: str
    software_type: str
    description: str | None
    aliases: list[str]
    platforms: list[str]
    deprecated: bool
    url: str | None

    model_config = {"from_attributes": True}


class MitreSoftwareList(BaseModel):
    items: list[MitreSoftwareRead]
    total: int
    page: int
    per_page: int


class MitreSoftwareStats(BaseModel):
    total_software: int
    malware_count: int
    tool_count: int
    deprecated_count: int
    sources: list[str]


# ── MITRE Campaigns (Phase 28) ─────────────────────────────────────────────────

class MitreCampaignRead(BaseModel):
    id: uuid.UUID
    stix_id: str
    source: str
    campaign_id: str
    name: str
    description: str | None
    aliases: list[str]
    first_seen: date | None
    last_seen: date | None
    deprecated: bool
    url: str | None

    model_config = {"from_attributes": True}


class MitreCampaignList(BaseModel):
    items: list[MitreCampaignRead]
    total: int
    page: int
    per_page: int
