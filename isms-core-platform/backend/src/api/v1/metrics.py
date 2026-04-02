"""KPI Metrics API — Phase 15.

GET /api/v1/metrics              compute + return all metrics (stores snapshot)
GET /api/v1/metrics/portfolio    portfolio view across all orgs (super_admin only)
GET /api/v1/metrics/{name}       single metric + 90-day history
"""

import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, get_org_context, require_role
from src.database.enums import UserRole
from src.database.session import get_db
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
