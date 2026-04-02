"""Custom Framework Import API — Phase 20.

GET         /api/v1/custom-frameworks                   list org's custom frameworks
POST        /api/v1/custom-frameworks                   admin-only: import from YAML body
GET         /api/v1/custom-frameworks/{fw_id}           get framework + control list
DELETE      /api/v1/custom-frameworks/{fw_id}           admin-only: delete framework + controls
GET         /api/v1/custom-frameworks/{fw_id}/controls  list controls (filter: category, search)
"""

import uuid

import yaml
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, get_org_context, require_admin
from src.database.session import get_db
from src.domain.custom_framework import CustomControl, CustomFramework
from src.domain.users import User

router = APIRouter(prefix="/custom-frameworks", tags=["custom-frameworks"])


# ── Schemas ─────────────────────────────────────────────────────────────────────

class FrameworkImport(BaseModel):
    yaml_content: str


# ── Serializers ─────────────────────────────────────────────────────────────────

def _fw(f: CustomFramework) -> dict:
    return {
        "id": str(f.id),
        "org_id": str(f.org_id),
        "name": f.name,
        "short_code": f.short_code,
        "version": f.version,
        "description": f.description,
        "control_count": f.control_count,
        "status": f.status,
        "created_by": str(f.created_by) if f.created_by else None,
        "created_at": f.created_at.isoformat(),
        "updated_at": f.updated_at.isoformat(),
    }


def _ctrl(c: CustomControl) -> dict:
    return {
        "id": str(c.id),
        "framework_id": str(c.framework_id),
        "org_id": str(c.org_id),
        "control_id": c.control_id,
        "title": c.title,
        "description": c.description,
        "category": c.category,
        "subcategory": c.subcategory,
        "priority": c.priority,
        "iso_mappings": c.iso_mappings or [],
        "tags": c.tags or [],
        "created_at": c.created_at.isoformat(),
    }


# ── Helper ───────────────────────────────────────────────────────────────────────

def _get_fw(fw_id: uuid.UUID, org_id: uuid.UUID, db: DBSession) -> CustomFramework:
    fw = db.get(CustomFramework, fw_id)
    if not fw or fw.org_id != org_id:
        raise HTTPException(404, "Custom framework not found")
    return fw


# ── Endpoints ────────────────────────────────────────────────────────────────────

@router.get("")
def list_frameworks(
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    rows = db.execute(
        select(CustomFramework)
        .where(CustomFramework.org_id == org_id)
        .order_by(CustomFramework.created_at.desc())
    ).scalars().all()
    return [_fw(f) for f in rows]


@router.post("", status_code=201)
def import_framework(
    body: FrameworkImport,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    current_user: User = Depends(require_admin),
):
    # Parse YAML
    try:
        data = yaml.safe_load(body.yaml_content)
    except yaml.YAMLError as e:
        raise HTTPException(400, f"Invalid YAML: {e}")

    if not isinstance(data, dict):
        raise HTTPException(400, "YAML must be a mapping at the top level")

    # Validate required top-level fields
    for field in ("name", "short_code", "controls"):
        if not data.get(field):
            raise HTTPException(400, f"Missing required field: {field}")

    controls_raw = data["controls"]
    if not isinstance(controls_raw, list) or len(controls_raw) == 0:
        raise HTTPException(400, "controls must be a non-empty list")

    # Validate each control has id and title
    for i, ctrl in enumerate(controls_raw):
        if not isinstance(ctrl, dict):
            raise HTTPException(400, f"controls[{i}] must be a mapping")
        if not ctrl.get("id"):
            raise HTTPException(400, f"controls[{i}] missing required field: id")
        if not ctrl.get("title"):
            raise HTTPException(400, f"controls[{i}] missing required field: title")

    short_code = str(data["short_code"])

    # Check for duplicate short_code within org
    existing = db.execute(
        select(CustomFramework).where(
            CustomFramework.org_id == org_id,
            CustomFramework.short_code == short_code,
        )
    ).scalar_one_or_none()
    if existing:
        raise HTTPException(409, f"A custom framework with short_code '{short_code}' already exists for this organisation")

    # Create framework + controls in one transaction
    fw = CustomFramework(
        org_id=org_id,
        name=str(data["name"]),
        short_code=short_code,
        version=str(data.get("version", "1.0")),
        description=data.get("description"),
        source_yaml=body.yaml_content,
        control_count=len(controls_raw),
        status="active",
        created_by=current_user.id,
    )
    db.add(fw)
    db.flush()  # get fw.id before bulk insert

    for ctrl in controls_raw:
        cc = CustomControl(
            framework_id=fw.id,
            org_id=org_id,
            control_id=str(ctrl["id"]),
            title=str(ctrl["title"]),
            description=ctrl.get("description"),
            category=ctrl.get("category"),
            subcategory=ctrl.get("subcategory"),
            priority=ctrl.get("priority"),
            iso_mappings=ctrl.get("iso_mappings") or [],
            tags=ctrl.get("tags") or [],
        )
        db.add(cc)

    db.commit()
    db.refresh(fw)
    return _fw(fw)


@router.get("/{fw_id}")
def get_framework(
    fw_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    fw = _get_fw(fw_id, org_id, db)
    result = _fw(fw)
    result["controls"] = [_ctrl(c) for c in fw.controls]
    return result


@router.delete("/{fw_id}", status_code=204)
def delete_framework(
    fw_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(require_admin),
):
    fw = _get_fw(fw_id, org_id, db)
    db.delete(fw)
    db.commit()


@router.get("/{fw_id}/controls")
def list_controls(
    fw_id: uuid.UUID,
    category: str | None = Query(None),
    search: str | None = Query(None),
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    _get_fw(fw_id, org_id, db)

    q = select(CustomControl).where(CustomControl.framework_id == fw_id)

    if category:
        q = q.where(CustomControl.category == category)

    if search:
        term = f"%{search.lower()}%"
        q = q.where(
            CustomControl.title.ilike(term)
            | CustomControl.control_id.ilike(term)
            | CustomControl.description.ilike(term)
        )

    q = q.order_by(CustomControl.control_id)
    rows = db.execute(q).scalars().all()
    return [_ctrl(c) for c in rows]
