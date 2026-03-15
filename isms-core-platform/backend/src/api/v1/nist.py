"""NIST CSF 2.0 Assessment endpoints.

GET    /api/v1/nist/subcategories                    — all 106 subcategories with ISO mappings
GET    /api/v1/nist/profiles                         — list all profiles (with summary scores)
POST   /api/v1/nist/profiles                         — create a new profile
GET    /api/v1/nist/profiles/{profile_id}            — full profile with all 106 ratings
PATCH  /api/v1/nist/profiles/{profile_id}            — update profile metadata
DELETE /api/v1/nist/profiles/{profile_id}            — delete profile (cascades ratings)
GET    /api/v1/nist/profiles/{profile_id}/summary    — score summary by function
PUT    /api/v1/nist/profiles/{profile_id}/ratings    — batch upsert ratings
GET    /api/v1/nist/profiles/{profile_id}/export     — CSV download
POST   /api/v1/nist/profiles/{profile_id}/import     — import ratings from NIST XLSX template
GET    /api/v1/nist/profiles/{profile_id}/export/xlsx — XLSX workbook download
"""

import uuid

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.domain.users import User
from src.schemas.nist import (
    NistFullProfile,
    NistImportResult,
    NistProfileCreate,
    NistProfileRead,
    NistProfileSummary,
    NistProfileUpdate,
    NistRatingRead,
    NistRatingUpsert,
    NistSubcategory,
)
from src.services import nist_service

router = APIRouter(prefix="/nist", tags=["nist-csf"])


@router.get("/subcategories", response_model=list[NistSubcategory])
def get_subcategories(
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> list[NistSubcategory]:
    try:
        return nist_service.list_subcategories(db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(e))


@router.get("/profiles", response_model=list[NistProfileSummary])
def list_profiles(
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> list[NistProfileSummary]:
    return nist_service.list_profiles(db)


@router.post("/profiles", response_model=NistProfileRead, status_code=status.HTTP_201_CREATED)
def create_profile(
    data: NistProfileCreate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> NistProfileRead:
    return nist_service.create_profile(db, data)


@router.get("/profiles/{profile_id}", response_model=NistFullProfile)
def get_full_profile(
    profile_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> NistFullProfile:
    try:
        return nist_service.get_full_profile(db, profile_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.patch("/profiles/{profile_id}", response_model=NistProfileRead)
def update_profile(
    profile_id: uuid.UUID,
    data: NistProfileUpdate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> NistProfileRead:
    try:
        return nist_service.update_profile(db, profile_id, data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/profiles/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(
    profile_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> None:
    if not nist_service.delete_profile(db, profile_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found.")


@router.get("/profiles/{profile_id}/summary", response_model=NistProfileSummary)
def get_profile_summary(
    profile_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> NistProfileSummary:
    try:
        return nist_service.get_profile_summary(db, profile_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/profiles/{profile_id}/ratings", response_model=list[NistRatingRead])
def upsert_ratings(
    profile_id: uuid.UUID,
    ratings: list[NistRatingUpsert],
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> list[NistRatingRead]:
    try:
        return nist_service.upsert_ratings(db, profile_id, ratings)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/profiles/{profile_id}/export")
def export_profile_csv(
    profile_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> StreamingResponse:
    try:
        csv_content = nist_service.export_profile_csv(db, profile_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    filename = f"NIST-CSF-Assessment-{profile_id}.csv"
    return StreamingResponse(
        iter([csv_content]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


@router.post("/profiles/{profile_id}/import", response_model=NistImportResult)
def import_profile_xlsx(
    profile_id: uuid.UUID,
    file: UploadFile = File(...),
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> NistImportResult:
    content = file.file.read()
    try:
        result = nist_service.import_from_xlsx(db, profile_id, content)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    return NistImportResult(**result)


@router.get("/profiles/{profile_id}/export/xlsx")
def export_profile_xlsx(
    profile_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> StreamingResponse:
    try:
        xlsx_bytes = nist_service.export_profile_xlsx(db, profile_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    filename = f"NIST-CSF-Assessment-{profile_id}.xlsx"
    return StreamingResponse(
        iter([xlsx_bytes]),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
