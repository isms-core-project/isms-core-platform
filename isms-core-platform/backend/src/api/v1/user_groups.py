"""User Groups API — create, list, manage group membership."""

import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import require_admin
from src.database.session import get_db
from src.domain.user_groups import UserGroup, user_group_members
from src.domain.users import User

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1/admin/groups", tags=["admin"])


@router.get("")
def list_groups(_user=Depends(require_admin), db: DBSession = Depends(get_db)):
    groups = (
        db.execute(
            select(UserGroup)
            .where(UserGroup.organisation_id == _user.organisation_id)
            .order_by(UserGroup.name)
        )
        .scalars()
        .all()
    )
    result = []
    for g in groups:
        count = db.execute(
            select(func.count()).select_from(user_group_members).where(
                user_group_members.c.group_id == g.id
            )
        ).scalar() or 0
        result.append({
            "id": str(g.id),
            "name": g.name,
            "description": g.description,
            "member_count": count,
            "created_at": g.created_at.isoformat(),
        })
    return result


@router.post("")
def create_group(body: dict, _user=Depends(require_admin), db: DBSession = Depends(get_db)):
    if not body.get("name", "").strip():
        raise HTTPException(status_code=422, detail="name is required")
    g = UserGroup(
        id=uuid.uuid4(),
        organisation_id=_user.organisation_id,
        name=body["name"].strip(),
        description=body.get("description") or None,
    )
    db.add(g)
    db.commit()
    db.refresh(g)
    return {
        "id": str(g.id),
        "name": g.name,
        "description": g.description,
        "member_count": 0,
        "created_at": g.created_at.isoformat(),
    }


@router.patch("/{group_id}")
def update_group(
    group_id: uuid.UUID,
    body: dict,
    _user=Depends(require_admin),
    db: DBSession = Depends(get_db),
):
    g = db.get(UserGroup, group_id)
    if not g or g.organisation_id != _user.organisation_id:
        raise HTTPException(status_code=404)
    if body.get("name", "").strip():
        g.name = body["name"].strip()
    if "description" in body:
        g.description = body.get("description") or None
    db.commit()
    return {"id": str(g.id), "name": g.name, "description": g.description}


@router.delete("/{group_id}")
def delete_group(
    group_id: uuid.UUID,
    _user=Depends(require_admin),
    db: DBSession = Depends(get_db),
):
    g = db.get(UserGroup, group_id)
    if not g or g.organisation_id != _user.organisation_id:
        raise HTTPException(status_code=404)
    db.delete(g)
    db.commit()
    return {"ok": True}


@router.get("/{group_id}/members")
def list_members(
    group_id: uuid.UUID,
    _user=Depends(require_admin),
    db: DBSession = Depends(get_db),
):
    g = db.get(UserGroup, group_id)
    if not g or g.organisation_id != _user.organisation_id:
        raise HTTPException(status_code=404)
    users = (
        db.execute(
            select(User)
            .join(user_group_members, User.id == user_group_members.c.user_id)
            .where(user_group_members.c.group_id == group_id)
            .order_by(User.email)
        )
        .scalars()
        .all()
    )
    return [
        {
            "user_id": str(u.id),
            "email": u.email,
            "username": u.username,
            "full_name": u.full_name,
            "role": u.role.value if hasattr(u.role, "value") else str(u.role),
        }
        for u in users
    ]


@router.post("/{group_id}/members")
def add_member(
    group_id: uuid.UUID,
    body: dict,
    _user=Depends(require_admin),
    db: DBSession = Depends(get_db),
):
    g = db.get(UserGroup, group_id)
    if not g or g.organisation_id != _user.organisation_id:
        raise HTTPException(status_code=404)
    user_id_raw = body.get("user_id")
    if not user_id_raw:
        raise HTTPException(status_code=422, detail="user_id required")
    try:
        uid = uuid.UUID(str(user_id_raw))
    except ValueError:
        raise HTTPException(status_code=422, detail="Invalid user_id")
    existing = db.execute(
        select(user_group_members).where(
            user_group_members.c.group_id == group_id,
            user_group_members.c.user_id == uid,
        )
    ).first()
    if not existing:
        db.execute(user_group_members.insert().values(group_id=group_id, user_id=uid))
        db.commit()
    return {"ok": True}


@router.delete("/{group_id}/members/{user_id}")
def remove_member(
    group_id: uuid.UUID,
    user_id: uuid.UUID,
    _user=Depends(require_admin),
    db: DBSession = Depends(get_db),
):
    g = db.get(UserGroup, group_id)
    if not g or g.organisation_id != _user.organisation_id:
        raise HTTPException(status_code=404)
    db.execute(
        user_group_members.delete().where(
            user_group_members.c.group_id == group_id,
            user_group_members.c.user_id == user_id,
        )
    )
    db.commit()
    return {"ok": True}
