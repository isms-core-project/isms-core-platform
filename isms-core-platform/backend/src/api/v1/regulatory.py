"""Regulatory compliance assessment endpoints (NIS2, DORA).

GET    /api/v1/regulatory/{framework_code}/requirements        — list assessable requirements
GET    /api/v1/regulatory/{framework_code}/assessments         — list all assessments
POST   /api/v1/regulatory/{framework_code}/assessments         — create assessment
GET    /api/v1/regulatory/{framework_code}/assessments/{id}    — full assessment
PATCH  /api/v1/regulatory/{framework_code}/assessments/{id}    — update metadata
DELETE /api/v1/regulatory/{framework_code}/assessments/{id}    — delete assessment
PUT    /api/v1/regulatory/{framework_code}/assessments/{id}/ratings — batch upsert ratings
"""

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.domain.users import User
from src.schemas.regulatory import (
    AssessmentCreate,
    AssessmentRead,
    AssessmentSummary,
    AssessmentUpdate,
    FullAssessment,
    RatingRead,
    RatingUpsert,
    RequirementRead,
)
from src.services import regulatory_service

router = APIRouter(prefix="/regulatory", tags=["regulatory"])

_SUPPORTED = {"NIS2", "DORA", "CIS_V8"}


def _validate_code(framework_code: str) -> str:
    code = framework_code.upper()
    if code not in _SUPPORTED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported framework code '{framework_code}'. Supported: {sorted(_SUPPORTED)}",
        )
    return code


@router.get("/{framework_code}/requirements", response_model=list[RequirementRead])
def list_requirements(
    framework_code: str,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> list[RequirementRead]:
    code = _validate_code(framework_code)
    try:
        return regulatory_service.list_requirements(db, code)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(e))


@router.get("/{framework_code}/assessments", response_model=list[AssessmentSummary])
def list_assessments(
    framework_code: str,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> list[AssessmentSummary]:
    code = _validate_code(framework_code)
    try:
        return regulatory_service.list_assessments(db, code)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(e))


@router.post("/{framework_code}/assessments", response_model=AssessmentRead, status_code=status.HTTP_201_CREATED)
def create_assessment(
    framework_code: str,
    data: AssessmentCreate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> AssessmentRead:
    code = _validate_code(framework_code)
    data.framework_code = code
    try:
        return regulatory_service.create_assessment(db, data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(e))


@router.get("/{framework_code}/assessments/{assessment_id}", response_model=FullAssessment)
def get_full_assessment(
    framework_code: str,
    assessment_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> FullAssessment:
    _validate_code(framework_code)
    try:
        return regulatory_service.get_full_assessment(db, assessment_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.patch("/{framework_code}/assessments/{assessment_id}", response_model=AssessmentRead)
def update_assessment(
    framework_code: str,
    assessment_id: uuid.UUID,
    data: AssessmentUpdate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> AssessmentRead:
    _validate_code(framework_code)
    try:
        return regulatory_service.update_assessment(db, assessment_id, data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{framework_code}/assessments/{assessment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_assessment(
    framework_code: str,
    assessment_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> None:
    _validate_code(framework_code)
    if not regulatory_service.delete_assessment(db, assessment_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Assessment not found.")


@router.put("/{framework_code}/assessments/{assessment_id}/ratings", response_model=list[RatingRead])
def upsert_ratings(
    framework_code: str,
    assessment_id: uuid.UUID,
    ratings: list[RatingUpsert],
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> list[RatingRead]:
    _validate_code(framework_code)
    try:
        return regulatory_service.upsert_ratings(db, assessment_id, ratings)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
