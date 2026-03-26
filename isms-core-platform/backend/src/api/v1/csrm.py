import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.domain.users import User
from src.schemas.csrm import (
    BaselineRatingRead,
    BaselineRatingUpsert,
    CsrmAssessmentCreate,
    CsrmAssessmentDetail,
    CsrmAssessmentPatch,
    CsrmAssessmentRead,
    CsrmAssessmentSummary,
    ElevatedTomCreate,
    ElevatedTomPatch,
    ElevatedTomRead,
    ProtectionObjectCreate,
    ProtectionObjectPatch,
    ProtectionObjectRead,
)
from src.services.csrm_service import (
    create_assessment,
    create_elevated_tom,
    create_protection_object,
    delete_assessment,
    delete_elevated_tom,
    delete_protection_object,
    get_assessment,
    list_assessments,
    patch_assessment,
    patch_elevated_tom,
    patch_protection_object,
    upsert_baseline_ratings,
)

router = APIRouter(prefix="/csrm", tags=["csrm"])


# ── Assessments ───────────────────────────────────────────────────────────────

@router.get("/assessments", response_model=list[CsrmAssessmentSummary])
def list_all(
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    return list_assessments(db)


@router.post("/assessments", response_model=CsrmAssessmentRead, status_code=201)
def create(
    body: CsrmAssessmentCreate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    return create_assessment(db, body)


@router.get("/assessments/{assessment_id}", response_model=CsrmAssessmentDetail)
def get_one(
    assessment_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    try:
        return get_assessment(db, assessment_id)
    except ValueError as e:
        raise HTTPException(404, str(e))


@router.patch("/assessments/{assessment_id}", response_model=CsrmAssessmentRead)
def update(
    assessment_id: uuid.UUID,
    body: CsrmAssessmentPatch,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    try:
        return patch_assessment(db, assessment_id, body)
    except ValueError as e:
        raise HTTPException(404, str(e))


@router.delete("/assessments/{assessment_id}", status_code=204)
def delete(
    assessment_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    if not delete_assessment(db, assessment_id):
        raise HTTPException(404, "Assessment not found")


# ── Protection Objects ────────────────────────────────────────────────────────

@router.post("/assessments/{assessment_id}/objects", response_model=ProtectionObjectRead, status_code=201)
def create_object(
    assessment_id: uuid.UUID,
    body: ProtectionObjectCreate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    try:
        return create_protection_object(db, assessment_id, body)
    except ValueError as e:
        raise HTTPException(404, str(e))


@router.patch("/objects/{object_id}", response_model=ProtectionObjectRead)
def update_object(
    object_id: uuid.UUID,
    body: ProtectionObjectPatch,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    try:
        return patch_protection_object(db, object_id, body)
    except ValueError as e:
        raise HTTPException(404, str(e))


@router.delete("/objects/{object_id}", status_code=204)
def delete_object(
    object_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    if not delete_protection_object(db, object_id):
        raise HTTPException(404, "Protection object not found")


# ── Baseline Ratings ──────────────────────────────────────────────────────────

@router.put("/objects/{object_id}/ratings", response_model=list[BaselineRatingRead])
def upsert_ratings(
    object_id: uuid.UUID,
    body: list[BaselineRatingUpsert],
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    try:
        return upsert_baseline_ratings(db, object_id, body)
    except ValueError as e:
        raise HTTPException(404, str(e))


# ── Elevated TOMs ─────────────────────────────────────────────────────────────

@router.post("/objects/{object_id}/toms", response_model=ElevatedTomRead, status_code=201)
def create_tom(
    object_id: uuid.UUID,
    body: ElevatedTomCreate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    try:
        return create_elevated_tom(db, object_id, body)
    except ValueError as e:
        raise HTTPException(404, str(e))


@router.patch("/toms/{tom_id}", response_model=ElevatedTomRead)
def update_tom(
    tom_id: uuid.UUID,
    body: ElevatedTomPatch,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    try:
        return patch_elevated_tom(db, tom_id, body)
    except ValueError as e:
        raise HTTPException(404, str(e))


@router.delete("/toms/{tom_id}", status_code=204)
def delete_tom(
    tom_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    if not delete_elevated_tom(db, tom_id):
        raise HTTPException(404, "TOM not found")
