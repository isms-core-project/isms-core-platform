"""Remediation Tracker + Risk Acceptance API endpoints.

Risk acceptances (sub-resource of risk scenarios):
  POST   /api/v1/risks/{id}/accept           create acceptance record
  GET    /api/v1/risks/{id}/acceptances       list acceptances for scenario
  DELETE /api/v1/risks/{id}/accept/{aid}      revoke acceptance

Remediation actions:
  GET    /api/v1/remediation                  list (filters: status, owner_id, risk_id, gap_id)
  POST   /api/v1/remediation                  create action
  GET    /api/v1/remediation/summary          counts by status + overdue
  GET    /api/v1/remediation/{id}             get detail
  PATCH  /api/v1/remediation/{id}             update
  DELETE /api/v1/remediation/{id}             delete
"""

import logging
import uuid
from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, get_org_context, require_qa_access
from src.database.session import get_db
from src.domain.risks import RemediationAction, RiskAcceptance, RiskScenario
from src.domain.users import User
from src.schemas.risks import (
    RemediationActionCreate,
    RemediationActionPatch,
    RemediationActionRead,
    RemediationSummary,
    RiskAcceptanceCreate,
    RiskAcceptanceRead,
)

logger = logging.getLogger(__name__)

acceptance_router = APIRouter(prefix="/risks", tags=["risks"])
remediation_router = APIRouter(prefix="/remediation", tags=["remediation"])


# ── helpers ───────────────────────────────────────────────────────────────────

def _enrich_action(a: RemediationAction, db: DBSession) -> RemediationActionRead:
    owner_name = None
    if a.owner_id:
        owner = db.get(User, a.owner_id)
        owner_name = (owner.full_name or owner.email) if owner else None
    risk_name = None
    if a.risk_scenario_id:
        r = db.get(RiskScenario, a.risk_scenario_id)
        risk_name = r.name if r else None
    return RemediationActionRead(
        id=a.id, org_id=a.org_id, title=a.title, description=a.description,
        status=a.status, owner_id=a.owner_id, owner_name=owner_name,
        eta=a.eta, effort=a.effort, cost_estimate=float(a.cost_estimate) if a.cost_estimate else None,
        progress=a.progress, project_id=a.project_id,
        risk_scenario_id=a.risk_scenario_id, risk_name=risk_name,
        gap_id=a.gap_id, control_group_id=a.control_group_id,
        evidence_id=a.evidence_id, created_at=a.created_at, updated_at=a.updated_at,
    )


# ── Risk acceptance endpoints ─────────────────────────────────────────────────

@acceptance_router.post("/{risk_id}/accept", response_model=RiskAcceptanceRead, status_code=201)
def create_acceptance(
    risk_id: uuid.UUID,
    body: RiskAcceptanceCreate,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    current_user: User = Depends(require_qa_access),
):
    r = db.get(RiskScenario, risk_id)
    if not r or r.org_id != org_id:
        raise HTTPException(status_code=404, detail="Risk scenario not found")

    acceptance = RiskAcceptance(
        risk_scenario_id=risk_id,
        approver_id=current_user.id,
        approver_name=current_user.full_name or current_user.email,
        justification=body.justification,
        expiry_date=body.expiry_date,
        status='active',
    )
    db.add(acceptance)
    # Auto-update risk status to accepted
    r.status = 'accepted'
    r.treatment_status = 'accept'
    db.commit()
    db.refresh(acceptance)
    return acceptance


@acceptance_router.get("/{risk_id}/acceptances", response_model=list[RiskAcceptanceRead])
def list_acceptances(
    risk_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    r = db.get(RiskScenario, risk_id)
    if not r or r.org_id != org_id:
        raise HTTPException(status_code=404, detail="Risk scenario not found")
    rows = db.execute(
        select(RiskAcceptance)
        .where(RiskAcceptance.risk_scenario_id == risk_id)
        .order_by(RiskAcceptance.created_at.desc())
    ).scalars().all()
    return rows


@acceptance_router.delete("/{risk_id}/accept/{accept_id}", status_code=204)
def revoke_acceptance(
    risk_id: uuid.UUID,
    accept_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    current_user: User = Depends(require_qa_access),
):
    r = db.get(RiskScenario, risk_id)
    if not r or r.org_id != org_id:
        raise HTTPException(status_code=404, detail="Risk scenario not found")
    a = db.get(RiskAcceptance, accept_id)
    if not a or a.risk_scenario_id != risk_id:
        raise HTTPException(status_code=404, detail="Acceptance record not found")

    from datetime import datetime, timezone
    a.status = 'revoked'
    a.revoked_by = current_user.id
    a.revoked_at = datetime.now(timezone.utc)
    # Revert risk status if no other active acceptances
    active = db.execute(
        select(RiskAcceptance).where(
            RiskAcceptance.risk_scenario_id == risk_id,
            RiskAcceptance.status == 'active',
            RiskAcceptance.id != accept_id,
        )
    ).scalar_one_or_none()
    if not active:
        r.status = 'open'
    db.commit()


# ── Remediation action endpoints ──────────────────────────────────────────────

@remediation_router.get("/summary", response_model=RemediationSummary)
def get_summary(
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    rows = db.execute(
        select(RemediationAction).where(RemediationAction.org_id == org_id)
    ).scalars().all()
    today = date.today()
    summary = RemediationSummary(total=0, planned=0, in_progress=0, completed=0, cancelled=0, overdue=0)
    for a in rows:
        summary.total += 1
        if a.status == 'planned':        summary.planned += 1
        elif a.status == 'in_progress':  summary.in_progress += 1
        elif a.status == 'completed':    summary.completed += 1
        elif a.status == 'cancelled':    summary.cancelled += 1
        if a.eta and a.eta < today and a.status not in ('completed', 'cancelled'):
            summary.overdue += 1
    return summary


@remediation_router.get("", response_model=list[RemediationActionRead])
def list_actions(
    status:          str | None = Query(None),
    owner_id:        str | None = Query(None),
    risk_scenario_id: str | None = Query(None),
    gap_id:          str | None = Query(None),
    limit:           int        = Query(200, le=500),
    offset:          int        = Query(0),
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    q = select(RemediationAction).where(RemediationAction.org_id == org_id)
    if status:
        q = q.where(RemediationAction.status == status)
    if owner_id:
        q = q.where(RemediationAction.owner_id == uuid.UUID(owner_id))
    if risk_scenario_id:
        q = q.where(RemediationAction.risk_scenario_id == uuid.UUID(risk_scenario_id))
    if gap_id:
        q = q.where(RemediationAction.gap_id == uuid.UUID(gap_id))
    q = q.order_by(RemediationAction.eta.asc().nullslast(), RemediationAction.created_at.desc()).limit(limit).offset(offset)
    return [_enrich_action(a, db) for a in db.execute(q).scalars().all()]


@remediation_router.post("", response_model=RemediationActionRead, status_code=201)
def create_action(
    body: RemediationActionCreate,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    a = RemediationAction(
        org_id=org_id,
        title=body.title,
        description=body.description,
        status=body.status,
        owner_id=body.owner_id,
        eta=body.eta,
        effort=body.effort,
        cost_estimate=body.cost_estimate,
        progress=body.progress,
        project_id=body.project_id,
        risk_scenario_id=body.risk_scenario_id,
        gap_id=body.gap_id,
        control_group_id=body.control_group_id,
        evidence_id=body.evidence_id,
    )
    db.add(a)
    db.commit()
    db.refresh(a)
    return _enrich_action(a, db)


@remediation_router.get("/{action_id}", response_model=RemediationActionRead)
def get_action(
    action_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    a = db.get(RemediationAction, action_id)
    if not a or a.org_id != org_id:
        raise HTTPException(status_code=404, detail="Remediation action not found")
    return _enrich_action(a, db)


@remediation_router.patch("/{action_id}", response_model=RemediationActionRead)
def update_action(
    action_id: uuid.UUID,
    body: RemediationActionPatch,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(require_qa_access),
):
    a = db.get(RemediationAction, action_id)
    if not a or a.org_id != org_id:
        raise HTTPException(status_code=404, detail="Remediation action not found")
    for field in ('title', 'description', 'status', 'owner_id', 'eta', 'effort',
                  'cost_estimate', 'progress', 'project_id', 'risk_scenario_id',
                  'gap_id', 'control_group_id', 'evidence_id'):
        val = getattr(body, field, None)
        if val is not None:
            setattr(a, field, val)
    db.commit()
    db.refresh(a)
    return _enrich_action(a, db)


@remediation_router.delete("/{action_id}", status_code=204)
def delete_action(
    action_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(require_qa_access),
):
    a = db.get(RemediationAction, action_id)
    if not a or a.org_id != org_id:
        raise HTTPException(status_code=404, detail="Remediation action not found")
    db.delete(a)
    db.commit()
