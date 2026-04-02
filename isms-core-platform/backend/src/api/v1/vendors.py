"""TPRM — Vendor/Supplier management API.

GET/POST        /api/v1/vendors
GET             /api/v1/vendors/summary
GET             /api/v1/vendors/dora
GET/PATCH/DEL   /api/v1/vendors/{id}
GET/POST        /api/v1/vendors/{id}/assessments
GET/POST        /api/v1/vendors/{id}/contracts
"""

import uuid
from datetime import date, timedelta

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, get_org_context
from src.database.session import get_db
from src.domain.tprm import Vendor, VendorAssessment, VendorContract
from src.domain.users import User

router = APIRouter(prefix="/vendors", tags=["vendors"])


# ── Schemas (inline for simplicity) ──────────────────────────────────────────

class VendorCreate(BaseModel):
    name: str
    vendor_type: str = "supplier"
    criticality: str = "medium"
    status: str = "active"
    description: str | None = None
    website: str | None = None
    primary_contact: str | None = None
    dora_entity_type: str | None = None
    dora_ict_service_type: str | None = None
    dora_substitutability: str | None = None
    dora_register_ref: str | None = None

class VendorPatch(BaseModel):
    name: str | None = None
    vendor_type: str | None = None
    criticality: str | None = None
    status: str | None = None
    description: str | None = None
    website: str | None = None
    primary_contact: str | None = None
    dora_entity_type: str | None = None
    dora_ict_service_type: str | None = None
    dora_substitutability: str | None = None
    dora_register_ref: str | None = None

class AssessmentCreate(BaseModel):
    score: int | None = None
    status: str = "not_assessed"
    notes: str | None = None
    assessment_date: date | None = None
    next_review_date: date | None = None
    control_group_id: uuid.UUID | None = None

class ContractCreate(BaseModel):
    title: str
    contract_ref: str | None = None
    start_date: date | None = None
    expiry_date: date | None = None
    auto_renews: bool = False
    security_clauses_present: bool = False


def _v(v: Vendor) -> dict:
    return {
        "id": str(v.id), "org_id": str(v.org_id), "name": v.name,
        "vendor_type": v.vendor_type, "criticality": v.criticality, "status": v.status,
        "description": v.description, "website": v.website, "primary_contact": v.primary_contact,
        "dora_entity_type": v.dora_entity_type, "dora_ict_service_type": v.dora_ict_service_type,
        "dora_substitutability": v.dora_substitutability, "dora_register_ref": v.dora_register_ref,
        "assessment_count": len(v.assessments), "contract_count": len(v.contracts),
        "last_assessment_date": max((a.assessment_date for a in v.assessments if a.assessment_date), default=None),
        "contracts_expiring_soon": sum(
            1 for c in v.contracts
            if c.expiry_date and date.today() <= c.expiry_date <= date.today() + timedelta(days=90)
        ),
        "created_at": v.created_at.isoformat(),
    }


# ── Endpoints ─────────────────────────────────────────────────────────────────

@router.get("/summary")
def vendor_summary(
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    vendors = db.execute(select(Vendor).where(Vendor.org_id == org_id)).scalars().all()
    today = date.today()
    in_90 = today + timedelta(days=90)
    return {
        "total":    len(vendors),
        "active":   sum(1 for v in vendors if v.status == "active"),
        "critical": sum(1 for v in vendors if v.criticality == "critical"),
        "dora_regulated": sum(1 for v in vendors if v.dora_entity_type),
        "contracts_expiring_soon": db.scalar(
            select(func.count(VendorContract.id))
            .join(Vendor, VendorContract.vendor_id == Vendor.id)
            .where(Vendor.org_id == org_id, VendorContract.expiry_date.between(today, in_90))
        ) or 0,
    }


@router.get("/dora")
def dora_register(
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    """DORA-regulated vendors only."""
    vendors = db.execute(
        select(Vendor).where(Vendor.org_id == org_id, Vendor.dora_entity_type.isnot(None))
        .order_by(Vendor.criticality.desc(), Vendor.name)
    ).scalars().all()
    return [_v(v) for v in vendors]


@router.get("")
def list_vendors(
    criticality: str | None = Query(None),
    status: str | None = Query(None),
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    q = select(Vendor).where(Vendor.org_id == org_id)
    if criticality:
        q = q.where(Vendor.criticality == criticality)
    if status:
        q = q.where(Vendor.status == status)
    q = q.order_by(Vendor.criticality.desc(), Vendor.name)
    return [_v(v) for v in db.execute(q).scalars().all()]


@router.post("", status_code=201)
def create_vendor(
    body: VendorCreate,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    v = Vendor(org_id=org_id, **body.model_dump())
    db.add(v); db.commit(); db.refresh(v)
    return _v(v)


@router.get("/{vendor_id}")
def get_vendor(
    vendor_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    v = db.get(Vendor, vendor_id)
    if not v or v.org_id != org_id:
        raise HTTPException(404, "Vendor not found")
    return _v(v)


@router.patch("/{vendor_id}")
def update_vendor(
    vendor_id: uuid.UUID,
    body: VendorPatch,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    v = db.get(Vendor, vendor_id)
    if not v or v.org_id != org_id:
        raise HTTPException(404, "Vendor not found")
    for k, val in body.model_dump(exclude_none=True).items():
        setattr(v, k, val)
    db.commit(); db.refresh(v)
    return _v(v)


@router.delete("/{vendor_id}", status_code=204)
def delete_vendor(
    vendor_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    v = db.get(Vendor, vendor_id)
    if not v or v.org_id != org_id:
        raise HTTPException(404, "Vendor not found")
    db.delete(v); db.commit()


# ── Assessments sub-resource ──────────────────────────────────────────────────

@router.get("/{vendor_id}/assessments")
def list_assessments(
    vendor_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    v = db.get(Vendor, vendor_id)
    if not v or v.org_id != org_id:
        raise HTTPException(404, "Vendor not found")
    return [{"id": str(a.id), "vendor_id": str(a.vendor_id), "score": a.score, "status": a.status,
             "notes": a.notes, "assessment_date": str(a.assessment_date) if a.assessment_date else None,
             "next_review_date": str(a.next_review_date) if a.next_review_date else None,
             "control_group_id": str(a.control_group_id) if a.control_group_id else None,
             "created_at": a.created_at.isoformat()} for a in v.assessments]


@router.post("/{vendor_id}/assessments", status_code=201)
def create_assessment(
    vendor_id: uuid.UUID,
    body: AssessmentCreate,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    current_user: User = Depends(get_current_user),
):
    v = db.get(Vendor, vendor_id)
    if not v or v.org_id != org_id:
        raise HTTPException(404, "Vendor not found")
    a = VendorAssessment(vendor_id=vendor_id, assessor_id=current_user.id, **body.model_dump())
    db.add(a); db.commit(); db.refresh(a)
    return {"id": str(a.id), "status": a.status, "score": a.score}


# ── Contracts sub-resource ────────────────────────────────────────────────────

@router.get("/{vendor_id}/contracts")
def list_contracts(
    vendor_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    v = db.get(Vendor, vendor_id)
    if not v or v.org_id != org_id:
        raise HTTPException(404, "Vendor not found")
    today = date.today()
    return [{"id": str(c.id), "vendor_id": str(c.vendor_id), "title": c.title,
             "contract_ref": c.contract_ref, "start_date": str(c.start_date) if c.start_date else None,
             "expiry_date": str(c.expiry_date) if c.expiry_date else None,
             "auto_renews": c.auto_renews, "security_clauses_present": c.security_clauses_present,
             "is_expired": bool(c.expiry_date and c.expiry_date < today),
             "expiring_soon": bool(c.expiry_date and today <= c.expiry_date <= today + timedelta(days=90)),
             "created_at": c.created_at.isoformat()} for c in v.contracts]


@router.post("/{vendor_id}/contracts", status_code=201)
def create_contract(
    vendor_id: uuid.UUID,
    body: ContractCreate,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    v = db.get(Vendor, vendor_id)
    if not v or v.org_id != org_id:
        raise HTTPException(404, "Vendor not found")
    c = VendorContract(vendor_id=vendor_id, **body.model_dump())
    db.add(c); db.commit(); db.refresh(c)
    return {"id": str(c.id), "title": c.title}
