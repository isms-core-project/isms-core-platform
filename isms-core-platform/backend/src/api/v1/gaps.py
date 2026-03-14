"""Gap management endpoints.

GET    /api/v1/gaps                              — list gaps (filters: severity, status, product, control_group_id)
POST   /api/v1/gaps                              — create a gap
PATCH  /api/v1/gaps/{id}                         — update status, owner, due_date, remediation_plan, etc.
DELETE /api/v1/gaps/{id}                         — delete a gap
GET    /api/v1/gaps/{id}/evidence                — list evidence linked to a gap
POST   /api/v1/gaps/{id}/evidence/{evidence_id}  — attach evidence to a gap
DELETE /api/v1/gaps/{id}/evidence/{evidence_id}  — detach evidence from a gap
"""

import uuid
from datetime import date, timezone
from datetime import datetime as dt

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.enums import GapSeverity, GapStatus
from src.database.session import get_db
from src.domain.compliance import Evidence, Gap
from src.domain.control_groups import ControlGroup
from src.domain.users import User
from src.schemas.evidence import EvidenceRead
from src.schemas.gaps import GapCreate, GapPatch, GapRead

router = APIRouter(prefix="/gaps", tags=["gaps"])


def _enrich(gap: Gap, db: DBSession) -> GapRead:
    cg = db.get(ControlGroup, gap.control_group_id)
    return GapRead(
        id=gap.id,
        control_group_id=gap.control_group_id,
        control_group_code=cg.group_code if cg else "",
        control_group_name=cg.name if cg else "",
        gap_description=gap.gap_description,
        severity=gap.severity.value,
        status=gap.status.value,
        product_type=gap.product_type,
        owner=gap.owner,
        due_date=gap.due_date,
        remediation_plan=gap.remediation_plan,
        closed_date=gap.closed_date,
        closed_by=gap.closed_by,
        created_at=gap.created_at,
        evidence_count=len(gap.evidence_items),
    )


@router.get("/", response_model=list[GapRead])
def list_gaps(
    severity: str | None = Query(None),
    status: str | None = Query(None),
    product: str | None = Query(None),
    control_group_id: uuid.UUID | None = Query(None),
    limit: int = Query(200, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    q = select(Gap)
    if severity:
        q = q.where(Gap.severity == severity)
    if status:
        q = q.where(Gap.status == status)
    if product:
        q = q.where(Gap.product_type.in_([product, "both"]))
    if control_group_id:
        q = q.where(Gap.control_group_id == control_group_id)
    q = q.order_by(Gap.created_at.desc()).offset(offset).limit(limit)
    gaps = db.execute(q).scalars().all()
    return [_enrich(g, db) for g in gaps]


@router.post("/", response_model=GapRead, status_code=201)
def create_gap(
    body: GapCreate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    cg = db.get(ControlGroup, body.control_group_id)
    if not cg:
        raise HTTPException(status_code=404, detail="Control group not found")

    try:
        sev = GapSeverity(body.severity)
    except ValueError:
        raise HTTPException(status_code=422, detail=f"Invalid severity: {body.severity}")

    meta: dict = {}
    if body.workbook_document_id:
        meta["workbook_document_id"] = body.workbook_document_id

    gap = Gap(
        control_group_id=body.control_group_id,
        requirement_id=body.requirement_id,
        product_type=body.product_type,
        gap_description=body.gap_description,
        severity=sev,
        status=GapStatus.OPEN,
        owner=body.owner,
        due_date=body.due_date,
        remediation_plan=body.remediation_plan,
        metadata_=meta,
    )
    db.add(gap)
    db.commit()
    db.refresh(gap)
    return _enrich(gap, db)


@router.patch("/{gap_id}", response_model=GapRead)
def patch_gap(
    gap_id: uuid.UUID,
    body: GapPatch,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    gap = db.get(Gap, gap_id)
    if not gap:
        raise HTTPException(status_code=404, detail="Gap not found")

    if body.gap_description is not None:
        gap.gap_description = body.gap_description
    if body.severity is not None:
        try:
            gap.severity = GapSeverity(body.severity)
        except ValueError:
            raise HTTPException(status_code=422, detail=f"Invalid severity: {body.severity}")
    if body.status is not None:
        try:
            new_status = GapStatus(body.status)
        except ValueError:
            raise HTTPException(status_code=422, detail=f"Invalid status: {body.status}")
        gap.status = new_status
        if new_status == GapStatus.CLOSED and gap.closed_date is None:
            gap.closed_date = dt.now(timezone.utc).date()
    if body.owner is not None:
        gap.owner = body.owner or None
    if body.due_date is not None:
        gap.due_date = body.due_date
    if body.remediation_plan is not None:
        gap.remediation_plan = body.remediation_plan or None
    if body.closed_by is not None:
        gap.closed_by = body.closed_by or None

    db.commit()
    db.refresh(gap)
    return _enrich(gap, db)


@router.delete("/{gap_id}", status_code=204)
def delete_gap(
    gap_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    gap = db.get(Gap, gap_id)
    if not gap:
        raise HTTPException(status_code=404, detail="Gap not found")
    db.delete(gap)
    db.commit()


# ---------------------------------------------------------------------------
# Gap ↔ Evidence linking
# ---------------------------------------------------------------------------


@router.get("/{gap_id}/evidence", response_model=list[EvidenceRead])
def list_gap_evidence(
    gap_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """List all evidence items linked to a gap."""
    gap = db.get(Gap, gap_id)
    if not gap:
        raise HTTPException(status_code=404, detail="Gap not found")
    return gap.evidence_items


@router.post("/{gap_id}/evidence/{evidence_id}", response_model=GapRead)
def attach_evidence(
    gap_id: uuid.UUID,
    evidence_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Attach an evidence item to a gap."""
    gap = db.get(Gap, gap_id)
    if not gap:
        raise HTTPException(status_code=404, detail="Gap not found")
    ev = db.get(Evidence, evidence_id)
    if not ev:
        raise HTTPException(status_code=404, detail="Evidence not found")
    if ev not in gap.evidence_items:
        gap.evidence_items.append(ev)
        db.commit()
        db.refresh(gap)
    return _enrich(gap, db)


@router.delete("/{gap_id}/evidence/{evidence_id}", response_model=GapRead)
def detach_evidence(
    gap_id: uuid.UUID,
    evidence_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Detach an evidence item from a gap (does not delete the evidence record)."""
    gap = db.get(Gap, gap_id)
    if not gap:
        raise HTTPException(status_code=404, detail="Gap not found")
    ev = db.get(Evidence, evidence_id)
    if ev and ev in gap.evidence_items:
        gap.evidence_items.remove(ev)
        db.commit()
        db.refresh(gap)
    return _enrich(gap, db)
