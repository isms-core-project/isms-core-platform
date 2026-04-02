"""Risk Register API endpoints.

GET    /api/v1/risks                  list risk scenarios
POST   /api/v1/risks                  create scenario
GET    /api/v1/risks/summary          counts by level + status
GET    /api/v1/risks/heatmap          5×5 grid with scenario counts
GET    /api/v1/risks/matrix           get org's risk matrix config
PATCH  /api/v1/risks/matrix           update matrix (admin only)
GET    /api/v1/risks/{id}             get detail
PATCH  /api/v1/risks/{id}             update scenario
DELETE /api/v1/risks/{id}             delete scenario
"""

import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, get_org_context, require_admin, require_qa_access
from src.database.session import get_db
from src.domain.control_groups import ControlGroup
from src.domain.risks import RiskMatrix, RiskScenario
from src.domain.users import User
from src.schemas.risks import (
    DEFAULT_COLOUR_MAP,
    DEFAULT_IMPACT_LABELS,
    DEFAULT_PROBABILITY_LABELS,
    DEFAULT_SCORE_MAP,
    RiskMatrixPatch,
    RiskMatrixRead,
    RiskScenarioCreate,
    RiskScenarioPatch,
    RiskScenarioRead,
    RiskSummary,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/risks", tags=["risks"])


# ── helpers ───────────────────────────────────────────────────────────────────

def _compute_score(matrix: RiskMatrix, probability: int, impact: int) -> tuple[int, str]:
    """Return (score, level) from the matrix config."""
    key = f"{probability},{impact}"
    score = matrix.score_map.get(key, probability * impact)
    level = matrix.colour_map.get(str(score), "low")
    return score, level


def _get_or_create_matrix(db: DBSession, org_id: uuid.UUID) -> RiskMatrix:
    matrix = db.execute(
        select(RiskMatrix).where(RiskMatrix.org_id == org_id, RiskMatrix.is_default == True)
    ).scalar_one_or_none()
    if not matrix:
        matrix = RiskMatrix(
            org_id=org_id,
            probability_labels=DEFAULT_PROBABILITY_LABELS,
            impact_labels=DEFAULT_IMPACT_LABELS,
            score_map=DEFAULT_SCORE_MAP,
            colour_map=DEFAULT_COLOUR_MAP,
            is_default=True,
        )
        db.add(matrix)
        db.flush()
    return matrix


def _enrich(r: RiskScenario, db: DBSession) -> RiskScenarioRead:
    cg_code = None
    if r.control_group_id:
        cg = db.get(ControlGroup, r.control_group_id)
        cg_code = cg.group_code if cg else None
    owner_name = None
    if r.owner_id:
        owner = db.get(User, r.owner_id)
        owner_name = (owner.full_name or owner.email) if owner else None
    return RiskScenarioRead(
        id=r.id,
        org_id=r.org_id,
        project_id=r.project_id,
        control_group_id=r.control_group_id,
        control_group_code=cg_code,
        name=r.name,
        description=r.description,
        threat_source=r.threat_source,
        threat_event=r.threat_event,
        probability=r.probability,
        impact=r.impact,
        risk_score=r.risk_score,
        risk_level=r.risk_level,
        treatment_status=r.treatment_status,
        treatment_notes=r.treatment_notes,
        residual_probability=r.residual_probability,
        residual_impact=r.residual_impact,
        residual_score=r.residual_score,
        residual_level=r.residual_level,
        owner_id=r.owner_id,
        owner_name=owner_name,
        target_date=r.target_date,
        status=r.status,
        created_at=r.created_at,
        updated_at=r.updated_at,
    )


# ── Matrix endpoints ──────────────────────────────────────────────────────────

@router.get("/matrix", response_model=RiskMatrixRead)
def get_matrix(
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    """Get the org's default risk matrix configuration."""
    return _get_or_create_matrix(db, org_id)


@router.patch("/matrix", response_model=RiskMatrixRead, dependencies=[Depends(require_admin)])
def update_matrix(
    body: RiskMatrixPatch,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
):
    """Update the org's risk matrix labels and thresholds (admin only)."""
    matrix = _get_or_create_matrix(db, org_id)
    if body.name is not None:
        matrix.name = body.name
    if body.probability_labels is not None:
        matrix.probability_labels = body.probability_labels
    if body.impact_labels is not None:
        matrix.impact_labels = body.impact_labels
    if body.score_map is not None:
        matrix.score_map = body.score_map
    if body.colour_map is not None:
        matrix.colour_map = body.colour_map
    db.commit()
    db.refresh(matrix)
    return matrix


# ── Summary + heatmap ─────────────────────────────────────────────────────────

@router.get("/summary", response_model=RiskSummary)
def get_summary(
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    """Counts by risk level and treatment status."""
    rows = db.execute(
        select(RiskScenario).where(RiskScenario.org_id == org_id)
    ).scalars().all()

    summary = RiskSummary(total=0, critical=0, high=0, medium=0, low=0, open=0, accepted=0, in_treatment=0, closed=0)
    for r in rows:
        summary.total += 1
        setattr(summary, r.risk_level, getattr(summary, r.risk_level) + 1)
        stat = r.status
        if stat == 'in_treatment':
            summary.in_treatment += 1
        elif hasattr(summary, stat):
            setattr(summary, stat, getattr(summary, stat) + 1)
    return summary


@router.get("/heatmap")
def get_heatmap(
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    """5×5 grid with scenario counts per cell. Returns list of {p, i, count, level}."""
    matrix = _get_or_create_matrix(db, org_id)
    rows = db.execute(
        select(RiskScenario).where(RiskScenario.org_id == org_id, RiskScenario.status != 'closed')
    ).scalars().all()

    grid: dict[str, int] = {}
    for r in rows:
        key = f"{r.probability},{r.impact}"
        grid[key] = grid.get(key, 0) + 1

    cells = []
    for p in range(1, 6):
        for i in range(1, 6):
            key = f"{p},{i}"
            score, level = _compute_score(matrix, p, i)
            cells.append({"p": p, "i": i, "count": grid.get(key, 0), "score": score, "level": level})

    return {
        "probability_labels": matrix.probability_labels,
        "impact_labels": matrix.impact_labels,
        "cells": cells,
    }


# ── Risk scenario CRUD ────────────────────────────────────────────────────────

@router.get("", response_model=list[RiskScenarioRead])
def list_risks(
    status:           str | None = Query(None),
    risk_level:       str | None = Query(None),
    treatment_status: str | None = Query(None),
    project_id:       str | None = Query(None),
    limit:            int        = Query(200, le=500),
    offset:           int        = Query(0),
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    """List risk scenarios for the org, with optional filters."""
    q = select(RiskScenario).where(RiskScenario.org_id == org_id)
    if status:
        q = q.where(RiskScenario.status == status)
    if risk_level:
        q = q.where(RiskScenario.risk_level == risk_level)
    if treatment_status:
        q = q.where(RiskScenario.treatment_status == treatment_status)
    if project_id:
        q = q.where(RiskScenario.project_id == uuid.UUID(project_id))
    q = q.order_by(RiskScenario.risk_score.desc(), RiskScenario.created_at.desc()).limit(limit).offset(offset)
    return [_enrich(r, db) for r in db.execute(q).scalars().all()]


@router.post("", response_model=RiskScenarioRead, status_code=201)
def create_risk(
    body: RiskScenarioCreate,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
    org_id: uuid.UUID = Depends(get_org_context),
):
    """Create a new risk scenario. Score and level are computed from the org's matrix."""
    matrix = _get_or_create_matrix(db, org_id)
    score, level = _compute_score(matrix, body.probability, body.impact)

    residual_score = residual_level = None
    if body.residual_probability and body.residual_impact:
        residual_score, residual_level = _compute_score(matrix, body.residual_probability, body.residual_impact)

    r = RiskScenario(
        org_id=org_id,
        project_id=body.project_id,
        control_group_id=body.control_group_id,
        name=body.name,
        description=body.description,
        threat_source=body.threat_source,
        threat_event=body.threat_event,
        probability=body.probability,
        impact=body.impact,
        risk_score=score,
        risk_level=level,
        treatment_status=body.treatment_status,
        treatment_notes=body.treatment_notes,
        residual_probability=body.residual_probability,
        residual_impact=body.residual_impact,
        residual_score=residual_score,
        residual_level=residual_level,
        owner_id=body.owner_id or current_user.id,
        target_date=body.target_date,
        status=body.status,
    )
    db.add(r)
    db.commit()
    db.refresh(r)
    return _enrich(r, db)


@router.get("/{risk_id}", response_model=RiskScenarioRead)
def get_risk(
    risk_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    r = db.get(RiskScenario, risk_id)
    if not r or r.org_id != org_id:
        raise HTTPException(status_code=404, detail="Risk scenario not found")
    return _enrich(r, db)


@router.patch("/{risk_id}", response_model=RiskScenarioRead)
def update_risk(
    risk_id: uuid.UUID,
    body: RiskScenarioPatch,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(require_qa_access),
):
    """Update a risk scenario. Re-computes score when probability or impact changes."""
    r = db.get(RiskScenario, risk_id)
    if not r or r.org_id != org_id:
        raise HTTPException(status_code=404, detail="Risk scenario not found")

    for field in ('name', 'description', 'threat_source', 'threat_event',
                  'treatment_status', 'treatment_notes', 'owner_id', 'target_date',
                  'status', 'project_id', 'control_group_id'):
        val = getattr(body, field, None)
        if val is not None:
            setattr(r, field, val)

    prob_changed = body.probability is not None
    imp_changed  = body.impact is not None
    if prob_changed or imp_changed:
        if prob_changed:
            r.probability = body.probability
        if imp_changed:
            r.impact = body.impact
        matrix = _get_or_create_matrix(db, org_id)
        r.risk_score, r.risk_level = _compute_score(matrix, r.probability, r.impact)

    res_prob_changed = body.residual_probability is not None
    res_imp_changed  = body.residual_impact is not None
    if res_prob_changed or res_imp_changed:
        if res_prob_changed:
            r.residual_probability = body.residual_probability
        if res_imp_changed:
            r.residual_impact = body.residual_impact
        if r.residual_probability and r.residual_impact:
            matrix = _get_or_create_matrix(db, org_id)
            r.residual_score, r.residual_level = _compute_score(matrix, r.residual_probability, r.residual_impact)

    db.commit()
    db.refresh(r)
    return _enrich(r, db)


@router.delete("/{risk_id}", status_code=204, dependencies=[Depends(require_qa_access)])
def delete_risk(
    risk_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
):
    r = db.get(RiskScenario, risk_id)
    if not r or r.org_id != org_id:
        raise HTTPException(status_code=404, detail="Risk scenario not found")
    db.delete(r)
    db.commit()
