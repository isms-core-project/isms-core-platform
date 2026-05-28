"""KPI Metrics API — Phase 15.

GET  /api/v1/metrics              compute + return all metrics (stores snapshot)
GET  /api/v1/metrics/portfolio    portfolio view across all orgs (super_admin only)
GET  /api/v1/metrics/snapshots    historical snapshots for a project
POST /api/v1/metrics/snapshots    compute & store a new snapshot
GET  /api/v1/metrics/{name}       single metric + 90-day history
"""

import logging
import uuid
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, get_org_context, require_role
from src.database.enums import ProductFamily, UserRole
from src.database.session import get_db
from src.domain.compliance import Gap
from src.domain.control_groups import ControlGroup
from src.domain.metrics import MetricSnapshot
from src.domain.organisations import Organisation
from src.domain.users import User
from src.services.metrics_service import (
    METRIC_LABELS,
    METRIC_UNITS,
    compute_all_metrics,
    get_metric_history,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/metrics", tags=["metrics"])


@router.get("")
def list_metrics(
    project_id: str | None = Query(None),
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    """Compute and return all KPI metrics, storing a snapshot for trend history."""
    pid = uuid.UUID(project_id) if project_id else None
    return compute_all_metrics(db, org_id, project_id=pid, store_snapshot=True)


@router.get("/portfolio")
def get_portfolio_metrics(
    db: DBSession = Depends(get_db),
    _: User = Depends(require_role(UserRole.SUPER_ADMIN)),
):
    """Return metrics for every active organisation (super_admin only)."""
    orgs = db.execute(select(Organisation).where(Organisation.is_active == True)).scalars().all()  # noqa: E712
    results = []
    for org in orgs:
        try:
            org_metrics = compute_all_metrics(db, org_id=org.id, project_id=None, store_snapshot=False)
            metrics_by_name = {m["name"]: m["value"] for m in org_metrics}
        except Exception as e:
            logger.warning("portfolio: failed to compute metrics for org %s: %s", org.id, e)
            metrics_by_name = {}
        results.append({
            "org_id": str(org.id),
            "org_name": org.name,
            "metrics": metrics_by_name,
        })
    return results


class SnapshotBody(BaseModel):
    project_id: str


def _build_snapshot_row(
    metrics_dict: dict,
    project_id: str,
    total_isms: int,
    open_gaps: int,
    closed_gaps: int,
    computed_at: datetime,
    snap_id: str | None = None,
) -> dict:
    """Synthesise a MetricSnapshot-shaped response from stored metric values."""
    policy_pct     = metrics_dict.get("policy_coverage",   0.0)
    compliance_pct = metrics_dict.get("compliance_score",  0.0)
    evidence_pct   = metrics_dict.get("evidence_freshness", 0.0)
    audit_score    = metrics_dict.get("audit_readiness",   0.0)
    return {
        "id":                     snap_id or str(uuid.uuid4()),
        "project_id":             project_id,
        "snapshot_date":          computed_at.date().isoformat(),
        "created_at":             computed_at.isoformat(),
        "total_controls":         total_isms,
        "controls_with_policy":   round(policy_pct    / 100 * total_isms),
        "controls_with_impl":     0,
        "controls_with_assessment": round(compliance_pct / 100 * total_isms),
        "controls_with_evidence": round(evidence_pct  / 100 * total_isms),
        "open_gaps":              open_gaps,
        "closed_gaps":            closed_gaps,
        "audit_readiness_score":  audit_score,
    }


def _gap_counts(db: DBSession, pid: uuid.UUID) -> tuple[int, int]:
    """Return (open_gaps, closed_gaps) for a project."""
    total = db.scalar(select(func.count(Gap.id)).where(Gap.project_id == pid)) or 0
    open_ = db.scalar(
        select(func.count(Gap.id)).where(Gap.project_id == pid, Gap.status == "open")
    ) or 0
    return open_, total - open_


@router.get("/snapshots")
def list_snapshots(
    project_id: str = Query(...),
    days: int = Query(30, ge=1, le=365),
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    """Return metric snapshots for a project, pivoted by computation batch."""
    pid = uuid.UUID(project_id)
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)

    rows = db.execute(
        select(MetricSnapshot)
        .where(MetricSnapshot.project_id == pid, MetricSnapshot.computed_at >= cutoff)
        .order_by(MetricSnapshot.computed_at.desc())
    ).scalars().all()

    if not rows:
        return []

    total_isms = db.scalar(
        select(func.count(ControlGroup.id)).where(ControlGroup.product_family == ProductFamily.ISMS)
    ) or 1
    open_gaps, closed_gaps = _gap_counts(db, pid)

    # Group by computed_at ISO string — all rows in one batch share the same timestamp
    groups: dict[str, dict] = {}
    for row in rows:
        key = row.computed_at.isoformat()
        if key not in groups:
            groups[key] = {"computed_at": row.computed_at, "id": str(row.id), "metrics": {}}
        groups[key]["metrics"][row.metric_name] = float(row.value)

    result = []
    for g in groups.values():
        m = g["metrics"]
        og = int(m.get("gap_open_count", open_gaps))
        result.append(_build_snapshot_row(m, project_id, total_isms, og, closed_gaps, g["computed_at"], g["id"]))

    return result


@router.post("/snapshots", status_code=201)
def create_snapshot(
    body: SnapshotBody,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    """Compute and store a new metric snapshot for the project."""
    pid = uuid.UUID(body.project_id)
    now = datetime.now(timezone.utc)

    metrics_list = compute_all_metrics(db, org_id, project_id=pid, store_snapshot=True)
    m = {item["name"]: item["value"] for item in metrics_list}

    total_isms = db.scalar(
        select(func.count(ControlGroup.id)).where(ControlGroup.product_family == ProductFamily.ISMS)
    ) or 1
    open_gaps, closed_gaps = _gap_counts(db, pid)

    return _build_snapshot_row(m, body.project_id, total_isms, open_gaps, closed_gaps, now)


@router.get("/{metric_name}")
def get_metric(
    metric_name: str,
    project_id: str | None = Query(None),
    days: int = Query(90, ge=7, le=365),
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    """Single metric with historical trend data."""
    if metric_name not in METRIC_UNITS:
        raise HTTPException(status_code=404, detail=f"Unknown metric '{metric_name}'")
    pid = uuid.UUID(project_id) if project_id else None
    history = get_metric_history(db, org_id, metric_name, project_id=pid, days=days)
    return {
        "name":    metric_name,
        "label":   METRIC_LABELS[metric_name],
        "unit":    METRIC_UNITS[metric_name],
        "history": history,
    }
