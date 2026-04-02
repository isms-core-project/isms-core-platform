"""EBIOS RM — Risk management study API.

GET             /api/v1/ebios/summary
GET/POST        /api/v1/ebios
GET/PATCH/DEL   /api/v1/ebios/{study_id}
GET/POST        /api/v1/ebios/{study_id}/feared-events
PATCH/DEL       /api/v1/ebios/{study_id}/feared-events/{fe_id}
GET/POST        /api/v1/ebios/{study_id}/risk-sources
PATCH/DEL       /api/v1/ebios/{study_id}/risk-sources/{rs_id}
GET/POST        /api/v1/ebios/{study_id}/scenarios
PATCH/DEL       /api/v1/ebios/{study_id}/scenarios/{sc_id}
GET/POST        /api/v1/ebios/{study_id}/attack-paths
PATCH/DEL       /api/v1/ebios/{study_id}/attack-paths/{ap_id}
GET/POST        /api/v1/ebios/{study_id}/measures
PATCH/DEL       /api/v1/ebios/{study_id}/measures/{m_id}
"""

import uuid
from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, get_org_context
from src.database.session import get_db
from src.domain.ebios import (
    EbiosAttackPath,
    EbiosFearedEvent,
    EbiosMeasure,
    EbiosRiskSource,
    EbiosStrategicScenario,
    EbiosStudy,
)
from src.domain.users import User

router = APIRouter(prefix="/ebios", tags=["ebios"])


# ── Schemas ────────────────────────────────────────────────────────────────────

class StudyCreate(BaseModel):
    name: str
    description: str | None = None
    scope: str | None = None
    status: str = "draft"
    owner: str | None = None
    project_id: uuid.UUID | None = None
    started_at: date | None = None
    reviewed_at: date | None = None

class StudyPatch(BaseModel):
    name: str | None = None
    description: str | None = None
    scope: str | None = None
    status: str | None = None
    owner: str | None = None
    project_id: uuid.UUID | None = None
    started_at: date | None = None
    reviewed_at: date | None = None

class FearedEventCreate(BaseModel):
    asset_name: str
    asset_type: str = "primary"
    description: str | None = None
    gravity: int | None = None

class FearedEventPatch(BaseModel):
    asset_name: str | None = None
    asset_type: str | None = None
    description: str | None = None
    gravity: int | None = None

class RiskSourceCreate(BaseModel):
    name: str
    category: str = "cybercriminal"
    motivation: str | None = None
    pertinence: int | None = None
    activity: int | None = None
    resources: int | None = None

class RiskSourcePatch(BaseModel):
    name: str | None = None
    category: str | None = None
    motivation: str | None = None
    pertinence: int | None = None
    activity: int | None = None
    resources: int | None = None

class ScenarioCreate(BaseModel):
    name: str
    description: str | None = None
    risk_source_id: uuid.UUID | None = None
    feared_event_id: uuid.UUID | None = None
    likelihood: int | None = None
    gravity: int | None = None
    retained: bool = True

class ScenarioPatch(BaseModel):
    name: str | None = None
    description: str | None = None
    risk_source_id: uuid.UUID | None = None
    feared_event_id: uuid.UUID | None = None
    likelihood: int | None = None
    gravity: int | None = None
    retained: bool | None = None

class AttackPathCreate(BaseModel):
    name: str
    description: str | None = None
    strategic_scenario_id: uuid.UUID | None = None
    mitre_techniques: list = []
    difficulty: int | None = None
    detectability: int | None = None

class AttackPathPatch(BaseModel):
    name: str | None = None
    description: str | None = None
    strategic_scenario_id: uuid.UUID | None = None
    mitre_techniques: list | None = None
    difficulty: int | None = None
    detectability: int | None = None

class MeasureCreate(BaseModel):
    name: str
    description: str | None = None
    scenario_id: uuid.UUID | None = None
    status: str = "planned"
    iso_control_ref: str | None = None
    control_group_id: uuid.UUID | None = None
    effectiveness: int | None = None
    due_date: date | None = None
    owner: str | None = None

class MeasurePatch(BaseModel):
    name: str | None = None
    description: str | None = None
    scenario_id: uuid.UUID | None = None
    status: str | None = None
    iso_control_ref: str | None = None
    control_group_id: uuid.UUID | None = None
    effectiveness: int | None = None
    due_date: date | None = None
    owner: str | None = None


# ── Serializers ────────────────────────────────────────────────────────────────

def _study(s: EbiosStudy) -> dict:
    return {
        "id": str(s.id),
        "org_id": str(s.org_id),
        "project_id": str(s.project_id) if s.project_id else None,
        "name": s.name,
        "description": s.description,
        "scope": s.scope,
        "status": s.status,
        "owner": s.owner,
        "started_at": str(s.started_at) if s.started_at else None,
        "reviewed_at": str(s.reviewed_at) if s.reviewed_at else None,
        "feared_event_count": len(s.feared_events),
        "risk_source_count": len(s.risk_sources),
        "scenario_count": len(s.strategic_scenarios),
        "attack_path_count": len(s.attack_paths),
        "measure_count": len(s.measures),
        "created_at": s.created_at.isoformat(),
        "updated_at": s.updated_at.isoformat(),
    }


def _fe(fe: EbiosFearedEvent) -> dict:
    return {
        "id": str(fe.id),
        "study_id": str(fe.study_id),
        "org_id": str(fe.org_id),
        "asset_name": fe.asset_name,
        "asset_type": fe.asset_type,
        "description": fe.description,
        "gravity": fe.gravity,
        "created_at": fe.created_at.isoformat(),
    }


def _rs(rs: EbiosRiskSource) -> dict:
    return {
        "id": str(rs.id),
        "study_id": str(rs.study_id),
        "org_id": str(rs.org_id),
        "name": rs.name,
        "category": rs.category,
        "motivation": rs.motivation,
        "pertinence": rs.pertinence,
        "activity": rs.activity,
        "resources": rs.resources,
        "created_at": rs.created_at.isoformat(),
    }


def _sc(sc: EbiosStrategicScenario) -> dict:
    return {
        "id": str(sc.id),
        "study_id": str(sc.study_id),
        "org_id": str(sc.org_id),
        "risk_source_id": str(sc.risk_source_id) if sc.risk_source_id else None,
        "feared_event_id": str(sc.feared_event_id) if sc.feared_event_id else None,
        "name": sc.name,
        "description": sc.description,
        "likelihood": sc.likelihood,
        "gravity": sc.gravity,
        "risk_level": (sc.likelihood or 0) * (sc.gravity or 0),
        "retained": sc.retained,
        "created_at": sc.created_at.isoformat(),
    }


def _ap(ap: EbiosAttackPath) -> dict:
    return {
        "id": str(ap.id),
        "study_id": str(ap.study_id),
        "org_id": str(ap.org_id),
        "strategic_scenario_id": str(ap.strategic_scenario_id) if ap.strategic_scenario_id else None,
        "name": ap.name,
        "description": ap.description,
        "mitre_techniques": ap.mitre_techniques or [],
        "difficulty": ap.difficulty,
        "detectability": ap.detectability,
        "created_at": ap.created_at.isoformat(),
    }


def _m(m: EbiosMeasure) -> dict:
    return {
        "id": str(m.id),
        "study_id": str(m.study_id),
        "org_id": str(m.org_id),
        "scenario_id": str(m.scenario_id) if m.scenario_id else None,
        "name": m.name,
        "description": m.description,
        "status": m.status,
        "iso_control_ref": m.iso_control_ref,
        "control_group_id": str(m.control_group_id) if m.control_group_id else None,
        "effectiveness": m.effectiveness,
        "due_date": str(m.due_date) if m.due_date else None,
        "owner": m.owner,
        "created_at": m.created_at.isoformat(),
        "updated_at": m.updated_at.isoformat(),
    }


# ── Helper: load + validate study belongs to org ───────────────────────────────

def _get_study(study_id: uuid.UUID, org_id: uuid.UUID, db: DBSession) -> EbiosStudy:
    s = db.get(EbiosStudy, study_id)
    if not s or s.org_id != org_id:
        raise HTTPException(404, "Study not found")
    return s


# ── Summary ────────────────────────────────────────────────────────────────────

@router.get("/summary")
def ebios_summary(
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    studies = db.execute(select(EbiosStudy).where(EbiosStudy.org_id == org_id)).scalars().all()

    def _count(model, col):
        return db.scalar(
            select(func.count(model.id))
            .join(EbiosStudy, col == EbiosStudy.id)
            .where(EbiosStudy.org_id == org_id)
        ) or 0

    status_counts: dict[str, int] = {}
    for s in studies:
        status_counts[s.status] = status_counts.get(s.status, 0) + 1

    return {
        "total_studies": len(studies),
        "by_status": status_counts,
        "total_feared_events": _count(EbiosFearedEvent, EbiosFearedEvent.study_id),
        "total_risk_sources": _count(EbiosRiskSource, EbiosRiskSource.study_id),
        "total_strategic_scenarios": _count(EbiosStrategicScenario, EbiosStrategicScenario.study_id),
        "total_attack_paths": _count(EbiosAttackPath, EbiosAttackPath.study_id),
        "total_measures": _count(EbiosMeasure, EbiosMeasure.study_id),
    }


# ── Studies ────────────────────────────────────────────────────────────────────

@router.get("")
def list_studies(
    status: str | None = Query(None),
    project_id: uuid.UUID | None = Query(None),
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    q = select(EbiosStudy).where(EbiosStudy.org_id == org_id)
    if status:
        q = q.where(EbiosStudy.status == status)
    if project_id:
        q = q.where(EbiosStudy.project_id == project_id)
    q = q.order_by(EbiosStudy.created_at.desc())
    return [_study(s) for s in db.execute(q).scalars().all()]


@router.post("", status_code=201)
def create_study(
    body: StudyCreate,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    s = EbiosStudy(org_id=org_id, **body.model_dump())
    db.add(s); db.commit(); db.refresh(s)
    return _study(s)


@router.get("/{study_id}")
def get_study(
    study_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    return _study(_get_study(study_id, org_id, db))


@router.patch("/{study_id}")
def update_study(
    study_id: uuid.UUID,
    body: StudyPatch,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    s = _get_study(study_id, org_id, db)
    for k, val in body.model_dump(exclude_none=True).items():
        setattr(s, k, val)
    db.commit(); db.refresh(s)
    return _study(s)


@router.delete("/{study_id}", status_code=204)
def delete_study(
    study_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    s = _get_study(study_id, org_id, db)
    db.delete(s); db.commit()


# ── Feared Events ──────────────────────────────────────────────────────────────

@router.get("/{study_id}/feared-events")
def list_feared_events(
    study_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    rows = db.execute(
        select(EbiosFearedEvent).where(EbiosFearedEvent.study_id == study_id).order_by(EbiosFearedEvent.created_at)
    ).scalars().all()
    return [_fe(fe) for fe in rows]


@router.post("/{study_id}/feared-events", status_code=201)
def create_feared_event(
    study_id: uuid.UUID,
    body: FearedEventCreate,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    fe = EbiosFearedEvent(study_id=study_id, org_id=org_id, **body.model_dump())
    db.add(fe); db.commit(); db.refresh(fe)
    return _fe(fe)


@router.patch("/{study_id}/feared-events/{fe_id}")
def update_feared_event(
    study_id: uuid.UUID,
    fe_id: uuid.UUID,
    body: FearedEventPatch,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    fe = db.get(EbiosFearedEvent, fe_id)
    if not fe or fe.study_id != study_id:
        raise HTTPException(404, "Feared event not found")
    for k, val in body.model_dump(exclude_none=True).items():
        setattr(fe, k, val)
    db.commit(); db.refresh(fe)
    return _fe(fe)


@router.delete("/{study_id}/feared-events/{fe_id}", status_code=204)
def delete_feared_event(
    study_id: uuid.UUID,
    fe_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    fe = db.get(EbiosFearedEvent, fe_id)
    if not fe or fe.study_id != study_id:
        raise HTTPException(404, "Feared event not found")
    db.delete(fe); db.commit()


# ── Risk Sources ───────────────────────────────────────────────────────────────

@router.get("/{study_id}/risk-sources")
def list_risk_sources(
    study_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    rows = db.execute(
        select(EbiosRiskSource).where(EbiosRiskSource.study_id == study_id).order_by(EbiosRiskSource.created_at)
    ).scalars().all()
    return [_rs(rs) for rs in rows]


@router.post("/{study_id}/risk-sources", status_code=201)
def create_risk_source(
    study_id: uuid.UUID,
    body: RiskSourceCreate,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    rs = EbiosRiskSource(study_id=study_id, org_id=org_id, **body.model_dump())
    db.add(rs); db.commit(); db.refresh(rs)
    return _rs(rs)


@router.patch("/{study_id}/risk-sources/{rs_id}")
def update_risk_source(
    study_id: uuid.UUID,
    rs_id: uuid.UUID,
    body: RiskSourcePatch,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    rs = db.get(EbiosRiskSource, rs_id)
    if not rs or rs.study_id != study_id:
        raise HTTPException(404, "Risk source not found")
    for k, val in body.model_dump(exclude_none=True).items():
        setattr(rs, k, val)
    db.commit(); db.refresh(rs)
    return _rs(rs)


@router.delete("/{study_id}/risk-sources/{rs_id}", status_code=204)
def delete_risk_source(
    study_id: uuid.UUID,
    rs_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    rs = db.get(EbiosRiskSource, rs_id)
    if not rs or rs.study_id != study_id:
        raise HTTPException(404, "Risk source not found")
    db.delete(rs); db.commit()


# ── Strategic Scenarios ────────────────────────────────────────────────────────

@router.get("/{study_id}/scenarios")
def list_scenarios(
    study_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    rows = db.execute(
        select(EbiosStrategicScenario).where(EbiosStrategicScenario.study_id == study_id)
        .order_by(EbiosStrategicScenario.created_at)
    ).scalars().all()
    return [_sc(sc) for sc in rows]


@router.post("/{study_id}/scenarios", status_code=201)
def create_scenario(
    study_id: uuid.UUID,
    body: ScenarioCreate,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    sc = EbiosStrategicScenario(study_id=study_id, org_id=org_id, **body.model_dump())
    db.add(sc); db.commit(); db.refresh(sc)
    return _sc(sc)


@router.patch("/{study_id}/scenarios/{sc_id}")
def update_scenario(
    study_id: uuid.UUID,
    sc_id: uuid.UUID,
    body: ScenarioPatch,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    sc = db.get(EbiosStrategicScenario, sc_id)
    if not sc or sc.study_id != study_id:
        raise HTTPException(404, "Scenario not found")
    for k, val in body.model_dump(exclude_none=True).items():
        setattr(sc, k, val)
    db.commit(); db.refresh(sc)
    return _sc(sc)


@router.delete("/{study_id}/scenarios/{sc_id}", status_code=204)
def delete_scenario(
    study_id: uuid.UUID,
    sc_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    sc = db.get(EbiosStrategicScenario, sc_id)
    if not sc or sc.study_id != study_id:
        raise HTTPException(404, "Scenario not found")
    db.delete(sc); db.commit()


# ── Attack Paths ───────────────────────────────────────────────────────────────

@router.get("/{study_id}/attack-paths")
def list_attack_paths(
    study_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    rows = db.execute(
        select(EbiosAttackPath).where(EbiosAttackPath.study_id == study_id).order_by(EbiosAttackPath.created_at)
    ).scalars().all()
    return [_ap(ap) for ap in rows]


@router.post("/{study_id}/attack-paths", status_code=201)
def create_attack_path(
    study_id: uuid.UUID,
    body: AttackPathCreate,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    ap = EbiosAttackPath(study_id=study_id, org_id=org_id, **body.model_dump())
    db.add(ap); db.commit(); db.refresh(ap)
    return _ap(ap)


@router.patch("/{study_id}/attack-paths/{ap_id}")
def update_attack_path(
    study_id: uuid.UUID,
    ap_id: uuid.UUID,
    body: AttackPathPatch,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    ap = db.get(EbiosAttackPath, ap_id)
    if not ap or ap.study_id != study_id:
        raise HTTPException(404, "Attack path not found")
    for k, val in body.model_dump(exclude_none=True).items():
        setattr(ap, k, val)
    db.commit(); db.refresh(ap)
    return _ap(ap)


@router.delete("/{study_id}/attack-paths/{ap_id}", status_code=204)
def delete_attack_path(
    study_id: uuid.UUID,
    ap_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    ap = db.get(EbiosAttackPath, ap_id)
    if not ap or ap.study_id != study_id:
        raise HTTPException(404, "Attack path not found")
    db.delete(ap); db.commit()


# ── Measures ───────────────────────────────────────────────────────────────────

@router.get("/{study_id}/measures")
def list_measures(
    study_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    rows = db.execute(
        select(EbiosMeasure).where(EbiosMeasure.study_id == study_id).order_by(EbiosMeasure.created_at)
    ).scalars().all()
    return [_m(m) for m in rows]


@router.post("/{study_id}/measures", status_code=201)
def create_measure(
    study_id: uuid.UUID,
    body: MeasureCreate,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    m = EbiosMeasure(study_id=study_id, org_id=org_id, **body.model_dump())
    db.add(m); db.commit(); db.refresh(m)
    return _m(m)


@router.patch("/{study_id}/measures/{m_id}")
def update_measure(
    study_id: uuid.UUID,
    m_id: uuid.UUID,
    body: MeasurePatch,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    m = db.get(EbiosMeasure, m_id)
    if not m or m.study_id != study_id:
        raise HTTPException(404, "Measure not found")
    for k, val in body.model_dump(exclude_none=True).items():
        setattr(m, k, val)
    db.commit(); db.refresh(m)
    return _m(m)


@router.delete("/{study_id}/measures/{m_id}", status_code=204)
def delete_measure(
    study_id: uuid.UUID,
    m_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_study(study_id, org_id, db)
    m = db.get(EbiosMeasure, m_id)
    if not m or m.study_id != study_id:
        raise HTTPException(404, "Measure not found")
    db.delete(m); db.commit()
