import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.domain.users import User
from src.schemas.control_groups import (
    ControlGroupList,
    ControlGroupRichDetail,
)
from src.services.control_service import (
    get_control_group,
    get_control_group_by_code,
    get_control_group_rich,
    list_control_groups,
)

router = APIRouter(prefix="/controls", tags=["controls"])


@router.get("/", response_model=list[ControlGroupList])
def list_controls(
    section: str | None = None,
    product: str | None = None,
    product_family: str | None = None,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    return list_control_groups(db, section=section, product=product, product_family=product_family)


@router.get("/code/{group_code}", response_model=ControlGroupRichDetail)
def get_control_by_code(
    group_code: str,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Rich control detail by group code (e.g. a.5.1-2). Case-insensitive."""
    cg = get_control_group_by_code(db, group_code)
    if not cg:
        raise HTTPException(status_code=404, detail="Control group not found")
    return get_control_group_rich(db, cg)


@router.get("/{group_id}", response_model=ControlGroupRichDetail)
def get_control(
    group_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Rich control detail by UUID."""
    cg = get_control_group(db, group_id)
    if not cg:
        raise HTTPException(status_code=404, detail="Control group not found")
    return get_control_group_rich(db, cg)
