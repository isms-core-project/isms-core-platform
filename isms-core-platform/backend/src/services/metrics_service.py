"""KPI / Metrics computation service — Phase 15.

Computes 9 named metrics from existing DB data for a given org + optional project.
Results are stored as MetricSnapshot rows for trend history.
"""

import logging
import uuid
from datetime import date, datetime, timedelta, timezone
from typing import Any

from sqlalchemy import func, select
from sqlalchemy.orm import Session as DBSession

from src.domain.assessments import Assessment
from src.domain.compliance import Evidence, Gap
from src.domain.control_groups import ControlGroup
from src.domain.metrics import MetricSnapshot
from src.domain.risks import RemediationAction, RiskScenario

logger = logging.getLogger(__name__)

METRIC_UNITS = {
    "compliance_score":    "percent",
    "policy_coverage":     "percent",
    "risk_score_avg":      "numeric",
    "risk_critical_count": "count",
    "evidence_freshness":  "percent",
    "gap_open_count":      "count",
    "gap_closure_rate":    "percent",
    "remediation_overdue": "count",
    "audit_readiness":     "percent",
}

METRIC_LABELS = {
    "compliance_score":    "Compliance Score",
    "policy_coverage":     "Policy Coverage",
    "risk_score_avg":      "Avg Residual Risk",
    "risk_critical_count": "Critical Risks",
    "evidence_freshness":  "Evidence Freshness",
    "gap_open_count":      "Open Gaps",
    "gap_closure_rate":    "Gap Closure Rate",
    "remediation_overdue": "Overdue Remediations",
    "audit_readiness":     "Audit Readiness",
}


def _compliance_score(db: DBSession, org_id: uuid.UUID, project_id: uuid.UUID | None) -> float:
    """Control groups with ≥1 assessment / total ISMS control groups."""
    total = db.scalar(
        select(func.count(ControlGroup.id))
        .where(ControlGroup.product_family == 'isms')
    ) or 0
    if total == 0:
        return 0.0

    q = select(func.count(func.distinct(Assessment.control_group_id)))
    if project_id:
        q = q.where(Assessment.project_id == project_id)
    assessed = db.scalar(q) or 0
    return round(min(assessed / total * 100, 100), 1)


def _policy_coverage(db: DBSession, org_id: uuid.UUID, project_id: uuid.UUID | None) -> float:
    """Control groups with ≥1 policy / total ISMS control groups."""
    from src.domain.content import Policy
    total = db.scalar(
        select(func.count(ControlGroup.id))
        .where(ControlGroup.product_family == 'isms')
    ) or 0
    if total == 0:
        return 0.0
    covered = db.scalar(
        select(func.count(func.distinct(Policy.control_group_id)))
    ) or 0
    return round(min(covered / total * 100, 100), 1)


def _risk_score_avg(db: DBSession, org_id: uuid.UUID, project_id: uuid.UUID | None) -> float:
    """Mean residual score of open risks."""
    q = select(func.avg(RiskScenario.residual_score)).where(
        RiskScenario.org_id == org_id,
        RiskScenario.status.in_(['open', 'in_treatment']),
        RiskScenario.residual_score.isnot(None),
    )
    if project_id:
        q = q.where(RiskScenario.project_id == project_id)
    val = db.scalar(q)
    return round(float(val), 2) if val is not None else 0.0


def _risk_critical_count(db: DBSession, org_id: uuid.UUID, project_id: uuid.UUID | None) -> float:
    q = select(func.count(RiskScenario.id)).where(
        RiskScenario.org_id == org_id,
        RiskScenario.risk_level == 'critical',
        RiskScenario.status.in_(['open', 'in_treatment']),
    )
    if project_id:
        q = q.where(RiskScenario.project_id == project_id)
    return float(db.scalar(q) or 0)


def _evidence_freshness(db: DBSession, org_id: uuid.UUID, project_id: uuid.UUID | None) -> float:
    """Evidence records not expired / total evidence records."""
    q_total = select(func.count(Evidence.id))
    q_fresh = select(func.count(Evidence.id)).where(
        (Evidence.expires_date.is_(None)) | (Evidence.expires_date >= date.today())
    )
    if project_id:
        q_total = q_total.where(Evidence.project_id == project_id)
        q_fresh = q_fresh.where(Evidence.project_id == project_id)
    total = db.scalar(q_total) or 0
    if total == 0:
        return 100.0
    fresh = db.scalar(q_fresh) or 0
    return round(fresh / total * 100, 1)


def _gap_open_count(db: DBSession, org_id: uuid.UUID, project_id: uuid.UUID | None) -> float:
    q = select(func.count(Gap.id)).where(Gap.status == 'open')
    if project_id:
        q = q.where(Gap.project_id == project_id)
    return float(db.scalar(q) or 0)


def _gap_closure_rate(db: DBSession, org_id: uuid.UUID, project_id: uuid.UUID | None) -> float:
    """Gaps closed this calendar month / total gaps (as %)."""
    start_of_month = date.today().replace(day=1)
    q_closed = select(func.count(Gap.id)).where(
        Gap.status == 'closed',
        Gap.updated_at >= start_of_month,
    )
    q_total = select(func.count(Gap.id))
    if project_id:
        q_closed = q_closed.where(Gap.project_id == project_id)
        q_total = q_total.where(Gap.project_id == project_id)
    total = db.scalar(q_total) or 0
    if total == 0:
        return 0.0
    closed = db.scalar(q_closed) or 0
    return round(closed / total * 100, 1)


def _remediation_overdue(db: DBSession, org_id: uuid.UUID, project_id: uuid.UUID | None) -> float:
    today = date.today()
    q = select(func.count(RemediationAction.id)).where(
        RemediationAction.org_id == org_id,
        RemediationAction.eta < today,
        RemediationAction.status.notin_(['completed', 'cancelled']),
    )
    if project_id:
        q = q.where(RemediationAction.project_id == project_id)
    return float(db.scalar(q) or 0)


def _audit_readiness(metrics: dict[str, float]) -> float:
    """Composite: compliance_score×35% + policy_coverage×25% + evidence_freshness×20% + gaps/risks penalty×20%."""
    compliance  = metrics.get("compliance_score",  0.0)
    policy      = metrics.get("policy_coverage",   0.0)
    freshness   = metrics.get("evidence_freshness", 100.0)
    critical    = metrics.get("risk_critical_count", 0.0)
    overdue     = metrics.get("remediation_overdue", 0.0)
    gap_open    = metrics.get("gap_open_count",      0.0)

    # Risk/gap penalty: reduce up to 20 points for outstanding issues
    penalty = min(20.0, (critical * 2) + (overdue * 1) + (gap_open * 0.5))
    base = (compliance * 0.35) + (policy * 0.25) + (freshness * 0.20)
    return round(max(0.0, base + 20.0 - penalty), 1)


# ── Public API ────────────────────────────────────────────────────────────────

def compute_all_metrics(
    db: DBSession,
    org_id: uuid.UUID,
    project_id: uuid.UUID | None = None,
    store_snapshot: bool = True,
) -> list[dict[str, Any]]:
    """Compute all metrics, optionally persist a snapshot row for trend data."""
    now = datetime.now(timezone.utc)

    partial: dict[str, float] = {
        "compliance_score":    _compliance_score(db, org_id, project_id),
        "policy_coverage":     _policy_coverage(db, org_id, project_id),
        "risk_score_avg":      _risk_score_avg(db, org_id, project_id),
        "risk_critical_count": _risk_critical_count(db, org_id, project_id),
        "evidence_freshness":  _evidence_freshness(db, org_id, project_id),
        "gap_open_count":      _gap_open_count(db, org_id, project_id),
        "gap_closure_rate":    _gap_closure_rate(db, org_id, project_id),
        "remediation_overdue": _remediation_overdue(db, org_id, project_id),
    }
    partial["audit_readiness"] = _audit_readiness(partial)

    if store_snapshot:
        for name, value in partial.items():
            db.add(MetricSnapshot(
                org_id=org_id,
                project_id=project_id,
                metric_name=name,
                value=value,
                computed_at=now,
            ))
        try:
            db.commit()
        except Exception:
            db.rollback()
            logger.exception("Failed to store metric snapshots")

    return [
        {
            "name":        name,
            "label":       METRIC_LABELS[name],
            "value":       value,
            "unit":        METRIC_UNITS[name],
            "computed_at": now.isoformat(),
        }
        for name, value in partial.items()
    ]


def get_metric_history(
    db: DBSession,
    org_id: uuid.UUID,
    metric_name: str,
    project_id: uuid.UUID | None = None,
    days: int = 90,
) -> list[dict[str, Any]]:
    """Return up to `days` of daily snapshot history for a single metric."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    q = (
        select(MetricSnapshot)
        .where(
            MetricSnapshot.org_id == org_id,
            MetricSnapshot.metric_name == metric_name,
            MetricSnapshot.computed_at >= cutoff,
        )
        .order_by(MetricSnapshot.computed_at.asc())
    )
    if project_id:
        q = q.where(MetricSnapshot.project_id == project_id)
    else:
        q = q.where(MetricSnapshot.project_id.is_(None))

    rows = db.execute(q).scalars().all()
    return [{"date": r.computed_at.date().isoformat(), "value": float(r.value)} for r in rows]
