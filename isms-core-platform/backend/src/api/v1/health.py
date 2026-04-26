from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import select, text
from sqlalchemy.orm import Session as DBSession

from src.core.config import get_settings
from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.schemas.common import HealthResponse
from src.services import search_service

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check(db: DBSession = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        db_status = "ok"
    except Exception:
        db_status = "error"

    os_status = "ok" if search_service.is_available() else "unavailable"

    return HealthResponse(
        status="ok" if db_status == "ok" else "degraded",
        database=db_status,
        opensearch=os_status,
    )


# ── Platform Features (Phase 40) ─────────────────────────────────────────────


class PlatformFeatures(BaseModel):
    threat_intel_enabled: bool


@router.get("/api/v1/platform/features", response_model=PlatformFeatures)
def get_platform_features(_current_user=Depends(get_current_user)):
    """Return which optional platform features are active.

    Controlled by env vars on the backend container — no DB query needed.
    Frontend uses this to show/disable menu items without a build-time Vite variable.
    """
    settings = get_settings()
    return PlatformFeatures(
        threat_intel_enabled=settings.threat_intel_enabled,
    )


# ── Health Alerts (Phase 28) ───────────────────────────────────────────────────

class HealthAlert(BaseModel):
    type: str        # feed_failure | connector_failure | opensearch_down
    severity: str    # error | warning
    message: str
    detected_at: str
    entity: str | None = None


@router.get("/api/v1/health/alerts", response_model=list[HealthAlert])
def get_health_alerts(
    db: DBSession = Depends(get_db),
    _current_user=Depends(get_current_user),
):
    """Return active platform health alerts (last 24h).

    Checks: feed pull failures, connector errors, OpenSearch availability.
    Used by the UI health banner and sidebar badges.
    """
    from src.domain.feeds import FeedRun
    from src.domain.connectors import Connector

    alerts: list[HealthAlert] = []
    now    = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=24)

    # ── Feed failures ──────────────────────────────────────────────────────────
    try:
        failed_runs = db.scalars(
            select(FeedRun)
            .where(FeedRun.status == "error", FeedRun.started_at >= cutoff)
            .order_by(FeedRun.started_at.desc())
        ).all()
        seen_feeds: set[str] = set()
        for run in failed_runs:
            if run.feed_name in seen_feeds:
                continue
            seen_feeds.add(run.feed_name)
            alerts.append(HealthAlert(
                type="feed_failure",
                severity="error",
                message=f"Feed '{run.feed_name}' failed: {(run.error_message or 'unknown error')[:200]}",
                detected_at=run.started_at.isoformat(),
                entity=run.feed_name,
            ))
    except Exception:
        pass

    # ── Connector errors ───────────────────────────────────────────────────────
    try:
        failed_connectors = db.scalars(
            select(Connector)
            .where(Connector.last_error_at >= cutoff)
        ).all()
        for conn in failed_connectors:
            if not conn.last_error:
                continue
            alerts.append(HealthAlert(
                type="connector_failure",
                severity="error",
                message=f"Connector '{conn.name}' error: {conn.last_error[:200]}",
                detected_at=conn.last_error_at.isoformat(),
                entity=conn.name,
            ))
    except Exception:
        pass

    # ── OpenSearch ─────────────────────────────────────────────────────────────
    if not search_service.is_available():
        alerts.append(HealthAlert(
            type="opensearch_down",
            severity="error",
            message="OpenSearch is unavailable — search, QA engine and CVE index are degraded.",
            detected_at=now.isoformat(),
            entity="opensearch",
        ))

    return alerts
