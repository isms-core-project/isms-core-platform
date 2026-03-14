"""Pydantic schemas for Phase 3 Dashboard API responses."""

from __future__ import annotations

import uuid
from datetime import date
from typing import Any

from pydantic import BaseModel


# ---------------------------------------------------------------------------
# 3.1 — Compliance overview
# ---------------------------------------------------------------------------

class SectionSummary(BaseModel):
    section: str
    section_name: str
    total_controls: int
    framework_covered: int
    operational_covered: int
    framework_pct: float
    operational_pct: float


class ProductCoverage(BaseModel):
    total: int
    has_policy: int
    has_ug: int
    has_tg: int
    has_assessment: int
    coverage_pct: float


class OperationalCoverage(BaseModel):
    total: int
    has_policy: int
    has_assessment: int
    coverage_pct: float


class ItemsByStatus(BaseModel):
    not_assessed: int
    compliant: int
    partial: int
    non_compliant: int
    na: int


class DashboardOverview(BaseModel):
    total_controls: int
    sections: list[SectionSummary]
    framework: ProductCoverage
    operational: OperationalCoverage
    items_by_status: ItemsByStatus
    total_policies: int
    total_implementations: int
    total_assessments: int
    total_gaps_open: int
    total_evidence: int


# ---------------------------------------------------------------------------
# 3.2 — Framework coverage matrix
# ---------------------------------------------------------------------------

class FrameworkMappingEntry(BaseModel):
    framework: str
    framework_code: str
    control_id: str
    control_title: str
    mapping_type: str
    confidence: float


class CoverageRow(BaseModel):
    iso_control_id: str
    iso_control_title: str
    control_group_code: str | None
    mappings: list[FrameworkMappingEntry]


class CoverageMatrix(BaseModel):
    frameworks: list[str]
    total_iso_controls: int
    total_mappings: int
    by_framework: dict[str, int]
    rows: list[CoverageRow]


# ---------------------------------------------------------------------------
# 3.3 — Gap analysis
# ---------------------------------------------------------------------------

class GapItem(BaseModel):
    id: uuid.UUID
    control_group_code: str
    control_group_name: str
    description: str
    severity: str
    status: str
    owner: str | None
    due_date: date | None
    product_type: str


class GapSummary(BaseModel):
    total: int
    by_severity: dict[str, int]
    by_status: dict[str, int]
    by_product: dict[str, int]
    items: list[GapItem]


# ---------------------------------------------------------------------------
# 3.4 — Evidence status
# ---------------------------------------------------------------------------

class EvidenceControlItem(BaseModel):
    control_group_code: str
    control_group_name: str
    evidence_count: int
    latest_date: date | None


class EvidenceSummary(BaseModel):
    total: int
    by_type: dict[str, int]
    controls_with_evidence: int
    controls_without_evidence: int
    items: list[EvidenceControlItem]


# ---------------------------------------------------------------------------
# 3.5 — Audit readiness
# ---------------------------------------------------------------------------

class AuditReadiness(BaseModel):
    policies_pct: float
    ug_pct: float
    tg_pct: float
    assessments_pct: float
    evidence_pct: float
    gaps_closed_pct: float
    composite_score: float
    status: str  # "green" | "amber" | "red"
    breakdown: dict[str, Any]


# ---------------------------------------------------------------------------
# 3.10 — Control dependency graph
# ---------------------------------------------------------------------------

class GraphNode(BaseModel):
    id: str
    label: str
    node_type: str  # "control_group" | "iso_control" | "external_ref"
    framework: str | None
    section: str | None
    group_code: str | None


class GraphEdge(BaseModel):
    source: str
    target: str
    edge_type: str
    confidence: float | None


class GraphResponse(BaseModel):
    nodes: list[GraphNode]
    edges: list[GraphEdge]
    total_nodes: int
    total_edges: int
