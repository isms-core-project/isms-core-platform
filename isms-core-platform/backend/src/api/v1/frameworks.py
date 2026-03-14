import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.domain.frameworks import CrossFrameworkMapping, Framework, FrameworkControl
from src.domain.users import User
from src.schemas.frameworks import ControlRead, FrameworkRead, MappingRead
from src.services.framework_service import (
    get_framework,
    get_framework_controls,
    get_framework_mappings,
    list_frameworks,
)

router = APIRouter(prefix="/frameworks", tags=["frameworks"])


@router.get("/by-code/control")
def get_control_detail_by_code(
    code: str = Query(..., description="Framework code prefix (ISO27701, ISO27017, ISO27018)"),
    control_id: str = Query(..., description="The control_id to look up (e.g. A.1.2.2)"),
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Return a single FrameworkControl with its cross-framework mappings."""
    fw = db.execute(
        select(Framework).where(Framework.code.ilike(f"{code}%"))
    ).scalar_one_or_none()
    if not fw:
        raise HTTPException(status_code=404, detail=f"Framework '{code}' not found")

    ctrl = db.execute(
        select(FrameworkControl).where(
            FrameworkControl.framework_id == fw.id,
            FrameworkControl.control_id == control_id,
        )
    ).scalar_one_or_none()
    if not ctrl:
        raise HTTPException(status_code=404, detail=f"Control '{control_id}' not found in '{code}'")

    mapping_rows = db.execute(
        select(
            CrossFrameworkMapping.mapping_type,
            CrossFrameworkMapping.confidence,
            FrameworkControl.control_id.label("target_control_id"),
            FrameworkControl.title.label("target_title"),
            Framework.name.label("fw_name"),
            Framework.code.label("fw_code"),
        )
        .join(FrameworkControl, CrossFrameworkMapping.target_control_id == FrameworkControl.id)
        .join(Framework, FrameworkControl.framework_id == Framework.id)
        .where(CrossFrameworkMapping.source_control_id == ctrl.id)
        .order_by(Framework.name, FrameworkControl.control_id)
    ).all()

    return {
        "id": str(ctrl.id),
        "control_id": ctrl.control_id,
        "title": ctrl.title,
        "description": ctrl.description,
        "level": ctrl.level,
        "sort_order": ctrl.sort_order,
        "control_type": ctrl.control_type or [],
        "security_properties": ctrl.security_properties or [],
        "framework_code": fw.code,
        "framework_name": fw.name,
        "mappings": [
            {
                "framework": r.fw_name,
                "framework_code": r.fw_code,
                "control_id": r.target_control_id,
                "control_title": r.target_title,
                "mapping_type": r.mapping_type.value if hasattr(r.mapping_type, "value") else str(r.mapping_type),
                "confidence": float(r.confidence) if r.confidence else 0.85,
            }
            for r in mapping_rows
        ],
    }


@router.get("/by-code/controls", response_model=list[ControlRead])
def list_controls_by_code(
    code: str = Query(..., description="Framework code prefix, e.g. ISO27701, ISO27017, ISO27018"),
    level: int | None = Query(None, description="Filter by level (1=top, 2=leaf for ISO27701)"),
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Return FrameworkControl records for a framework identified by code prefix."""
    fw = db.execute(
        select(Framework).where(Framework.code.ilike(f"{code}%"))
    ).scalar_one_or_none()
    if not fw:
        raise HTTPException(status_code=404, detail=f"Framework '{code}' not found")
    return get_framework_controls(db, fw.id, level=level)


@router.get("/", response_model=list[FrameworkRead])
def list_all_frameworks(
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    return list_frameworks(db)


@router.get("/{framework_id}", response_model=FrameworkRead)
def get_one_framework(
    framework_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    fw = get_framework(db, framework_id)
    if not fw:
        raise HTTPException(status_code=404, detail="Framework not found")
    return fw


@router.get("/{framework_id}/controls", response_model=list[ControlRead])
def list_framework_controls(
    framework_id: uuid.UUID,
    level: int | None = None,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    fw = get_framework(db, framework_id)
    if not fw:
        raise HTTPException(status_code=404, detail="Framework not found")
    return get_framework_controls(db, framework_id, level=level)


@router.get("/{framework_id}/mappings", response_model=list[MappingRead])
def list_framework_mappings(
    framework_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    fw = get_framework(db, framework_id)
    if not fw:
        raise HTTPException(status_code=404, detail="Framework not found")
    return get_framework_mappings(db, framework_id)
