import uuid

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.domain.users import User
from src.schemas.collections import (
    CollectionCreate, CollectionListItem, CollectionMember,
    CollectionPatch, CollectionRead, CollectionStats,
)
from src.services.collection_service import (
    _build_members, _compute_stats,
    add_assessment, create_collection, delete_collection,
    export_csv, export_pdf, export_xlsx,
    get_collection, list_collections, patch_collection, remove_assessment,
)

router = APIRouter(prefix="/collections", tags=["collections"])


def _to_read(coll, db) -> CollectionRead:
    return CollectionRead(
        id=coll.id,
        name=coll.name,
        description=coll.description,
        product_family=coll.product_family,
        product_type=coll.product_type,
        due_date=coll.due_date,
        created_at=coll.created_at,
        updated_at=coll.updated_at,
        stats=_compute_stats(coll.assessments),
        members=_build_members(db, coll.assessments),
    )


def _to_list_item(coll) -> CollectionListItem:
    return CollectionListItem(
        id=coll.id,
        name=coll.name,
        description=coll.description,
        product_family=coll.product_family,
        product_type=coll.product_type,
        due_date=coll.due_date,
        created_at=coll.created_at,
        updated_at=coll.updated_at,
        stats=_compute_stats(coll.assessments),
    )


@router.get("/", response_model=list[CollectionListItem])
def list_all(
    product_family: str | None = None,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    return [_to_list_item(c) for c in list_collections(db, product_family=product_family)]


@router.post("/", response_model=CollectionRead, status_code=201)
def create(
    body: CollectionCreate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    coll = create_collection(db, body)
    return _to_read(coll, db)


@router.get("/{collection_id}", response_model=CollectionRead)
def get_one(
    collection_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    coll = get_collection(db, collection_id)
    if not coll:
        raise HTTPException(404, "Collection not found")
    return _to_read(coll, db)


@router.patch("/{collection_id}", response_model=CollectionRead)
def update(
    collection_id: uuid.UUID,
    body: CollectionPatch,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    coll = get_collection(db, collection_id)
    if not coll:
        raise HTTPException(404, "Collection not found")
    return _to_read(patch_collection(db, coll, body), db)


@router.delete("/{collection_id}", status_code=204)
def delete(
    collection_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    coll = get_collection(db, collection_id)
    if not coll:
        raise HTTPException(404, "Collection not found")
    delete_collection(db, coll)


@router.post("/{collection_id}/assessments/{assessment_id}", status_code=204)
def add(
    collection_id: uuid.UUID,
    assessment_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    coll = get_collection(db, collection_id)
    if not coll:
        raise HTTPException(404, "Collection not found")
    try:
        add_assessment(db, coll, assessment_id)
    except ValueError as e:
        raise HTTPException(404, str(e))


@router.delete("/{collection_id}/assessments/{assessment_id}", status_code=204)
def remove(
    collection_id: uuid.UUID,
    assessment_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    coll = get_collection(db, collection_id)
    if not coll:
        raise HTTPException(404, "Collection not found")
    remove_assessment(db, coll, assessment_id)


@router.get("/{collection_id}/export/csv")
def export_csv_endpoint(
    collection_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    coll = get_collection(db, collection_id)
    if not coll:
        raise HTTPException(404, "Collection not found")
    data = export_csv(db, coll)
    filename = f"collection_{coll.name.replace(' ', '_')}.csv"
    return Response(content=data, media_type="text/csv",
                    headers={"Content-Disposition": f'attachment; filename="{filename}"'})


@router.get("/{collection_id}/export/xlsx")
def export_xlsx_endpoint(
    collection_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    coll = get_collection(db, collection_id)
    if not coll:
        raise HTTPException(404, "Collection not found")
    data = export_xlsx(db, coll)
    filename = f"collection_{coll.name.replace(' ', '_')}.xlsx"
    return Response(content=data,
                    media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    headers={"Content-Disposition": f'attachment; filename="{filename}"'})


@router.get("/{collection_id}/export/pdf")
def export_pdf_endpoint(
    collection_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    coll = get_collection(db, collection_id)
    if not coll:
        raise HTTPException(404, "Collection not found")
    data = export_pdf(db, coll)
    filename = f"collection_{coll.name.replace(' ', '_')}.pdf"
    return Response(content=data, media_type="application/pdf",
                    headers={"Content-Disposition": f'attachment; filename="{filename}"'})
