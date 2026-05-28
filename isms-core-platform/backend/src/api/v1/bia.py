"""BIA — Business Impact Analysis API.

GET/POST        /api/v1/bia
GET             /api/v1/bia/summary
GET/PATCH/DEL   /api/v1/bia/{id}
"""

import uuid
from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, get_org_context
from src.database.session import get_db
from src.domain.bia import BIARecord
from src.domain.users import User

router = APIRouter(prefix="/bia", tags=["bia"])


class BIACreate(BaseModel):
    asset_name: str
    asset_type: str = "process"
    project_id: uuid.UUID | None = None
    control_group_id: uuid.UUID | None = None
    rto_hours: int | None = None
    rpo_hours: int | None = None
    mtpd_hours: int | None = None
    financial_impact: int | None = None
    operational_impact: int | None = None
    reputational_impact: int | None = None
    regulatory_impact: int | None = None
    recovery_tested: bool = False
    last_tested_date: date | None = None
    continuity_plan_ref: str | None = None
    notes: str | None = None

class BIAPatch(BIACreate):
    asset_name: str | None = None
    asset_type: str | None = None


def _r(r: BIARecord) -> dict:
    impacts = [r.financial_impact, r.operational_impact, r.reputational_impact, r.regulatory_impact]
    avg_impact = round(sum(i for i in impacts if i) / max(len([i for i in impacts if i]), 1), 1)
    return {
        "id": str(r.id), "org_id": str(r.org_id),
        "project_id": str(r.project_id) if r.project_id else None,
        "asset_name": r.asset_name, "asset_type": r.asset_type,
        "rto_hours": r.rto_hours, "rpo_hours": r.rpo_hours, "mtpd_hours": r.mtpd_hours,
        "financial_impact": r.financial_impact, "operational_impact": r.operational_impact,
        "reputational_impact": r.reputational_impact, "regulatory_impact": r.regulatory_impact,
        "avg_impact": avg_impact,
        "recovery_tested": r.recovery_tested,
        "last_tested_date": str(r.last_tested_date) if r.last_tested_date else None,
        "continuity_plan_ref": r.continuity_plan_ref,
        "notes": r.notes, "created_at": r.created_at.isoformat(),
    }


@router.get("/summary")
def bia_summary(
    project_id: str | None = Query(None),
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    q = select(BIARecord).where(BIARecord.org_id == org_id)
    if project_id:
        try:
            q = q.where(BIARecord.project_id == uuid.UUID(project_id))
        except ValueError:
            return {"total": 0, "tested": 0, "tested_pct": 0, "rto_missing": 0, "high_impact": 0}
    records = db.execute(q).scalars().all()
    total = len(records)
    tested = sum(1 for r in records if r.recovery_tested)
    rto_missing = sum(1 for r in records if not r.rto_hours)
    high_impact = sum(1 for r in records if any(
        (i or 0) >= 4 for i in [r.financial_impact, r.operational_impact, r.reputational_impact, r.regulatory_impact]
    ))
    return {
        "total": total,
        "tested": tested,
        "tested_pct": round(tested / max(total, 1) * 100, 1),
        "rto_missing": rto_missing,
        "high_impact": high_impact,
    }


@router.get("")
def list_bia(
    project_id: str | None = Query(None),
    asset_type: str | None = Query(None),
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    q = select(BIARecord).where(BIARecord.org_id == org_id)
    if project_id:
        try:
            q = q.where(BIARecord.project_id == uuid.UUID(project_id))
        except ValueError:
            return []
    if asset_type:
        q = q.where(BIARecord.asset_type == asset_type)
    q = q.order_by(BIARecord.asset_name)
    return [_r(r) for r in db.execute(q).scalars().all()]


@router.post("", status_code=201)
def create_bia(
    body: BIACreate,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    current_user: User = Depends(get_current_user),
):
    r = BIARecord(org_id=org_id, owner_id=current_user.id, **body.model_dump())
    db.add(r); db.commit(); db.refresh(r)
    return _r(r)


@router.get("/{record_id}")
def get_bia(
    record_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    r = db.get(BIARecord, record_id)
    if not r or r.org_id != org_id:
        raise HTTPException(404, "BIA record not found")
    return _r(r)


@router.patch("/{record_id}")
def update_bia(
    record_id: uuid.UUID,
    body: BIAPatch,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    r = db.get(BIARecord, record_id)
    if not r or r.org_id != org_id:
        raise HTTPException(404, "BIA record not found")
    for k, val in body.model_dump(exclude_none=True).items():
        setattr(r, k, val)
    db.commit(); db.refresh(r)
    return _r(r)


@router.delete("/{record_id}", status_code=204)
def delete_bia(
    record_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    r = db.get(BIARecord, record_id)
    if not r or r.org_id != org_id:
        raise HTTPException(404, "BIA record not found")
    db.delete(r); db.commit()
