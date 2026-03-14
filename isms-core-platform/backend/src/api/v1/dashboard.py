"""Dashboard API — compliance coverage, gap analysis, evidence status, audit readiness.

GET /api/v1/dashboard/overview        — 3.1 coverage by product and section
GET /api/v1/dashboard/coverage        — 3.2 framework mapping matrix
GET /api/v1/dashboard/gaps            — 3.3 gap analysis
GET /api/v1/dashboard/evidence        — 3.4 evidence status
GET /api/v1/dashboard/audit-readiness — 3.5 composite readiness score
"""

import logging

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.domain.users import User
from src.schemas.dashboard import (
    AuditReadiness,
    CoverageMatrix,
    DashboardOverview,
    EvidenceSummary,
    GapSummary,
)
from src.services import dashboard_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/overview", response_model=DashboardOverview)
def overview(
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Overall compliance coverage by product and section."""
    return dashboard_service.get_overview(db)


@router.get("/coverage", response_model=CoverageMatrix)
def coverage(
    source_framework: str = Query("ISO27001", description="Source framework code prefix (ISO27001 | ISO27701 | ISO27017)"),
    target_framework: str | None = Query(None, description="Filter by target framework name (partial match)"),
    limit: int = Query(200, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Source framework → cross-framework mapping matrix."""
    return dashboard_service.get_coverage_matrix(
        db, source_framework=source_framework, target_framework=target_framework,
        limit=limit, offset=offset,
    )


@router.get("/gaps", response_model=GapSummary)
def gaps(
    severity: str | None = Query(None, description="Filter: critical|high|medium|low"),
    status: str | None = Query(None, description="Filter: open|in_progress|closed|accepted"),
    product: str | None = Query(None, description="Filter: framework|operational|both"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Gap analysis — open gaps by severity, owner, product."""
    return dashboard_service.get_gaps(
        db, severity=severity, status=status, product=product,
        limit=limit, offset=offset,
    )


@router.get("/evidence", response_model=EvidenceSummary)
def evidence(
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Evidence coverage per control group."""
    return dashboard_service.get_evidence_status(db)


@router.get("/coverage-gaps")
def coverage_gaps(
    product: str = Query("operational", description="framework | operational"),
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Per-control-group artefact gaps for a given product."""
    return dashboard_service.get_coverage_gaps(db, product=product)


@router.get("/framework-overview")
def framework_overview(
    source_framework: str = Query("ISO27701", description="Source framework code prefix (ISO27701 | ISO27017 | ISO27018)"),
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Control count + mapping coverage for a non-ISO27001 framework."""
    return dashboard_service.get_framework_overview(db, source_framework=source_framework)


@router.get("/home-summary")
def home_summary(
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Per-product group/policy/IMP counts for the platform home page."""
    return dashboard_service.get_home_summary(db)


@router.get("/audit-readiness", response_model=AuditReadiness)
def audit_readiness(
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Composite audit readiness score (0-100) across all artefact types."""
    return dashboard_service.get_audit_readiness(db)
