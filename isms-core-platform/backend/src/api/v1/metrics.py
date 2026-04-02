"""KPI Metrics API — Phase 15.

GET /api/v1/metrics              compute + return all metrics (stores snapshot)
GET /api/v1/metrics/{name}       single metric + 90-day history
"""

import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, get_org_context
from src.database.session import get_db
from src.domain.users import User
from src.services.metrics_service import (
    METRIC_LABELS,
    METRIC_UNITS,
    compute_all_metrics,
    get_metric_history,
)

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
