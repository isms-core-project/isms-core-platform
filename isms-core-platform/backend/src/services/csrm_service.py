import uuid

import sqlalchemy
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.orm import Session

from src.domain.csrm import CsrmAssessment, CsrmBaselineRating, CsrmElevatedTom, CsrmProtectionObject
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

BASELINE_REQUIREMENT_IDS = [
    "GV.1", "GV.2", "GV.3", "GV.4",
    "ID.1", "ID.2",
    "PR.1", "PR.2", "PR.3", "PR.4", "PR.5", "PR.6", "PR.7", "PR.8", "PR.9",
    "DE.1", "DE.2",
    "RS.1", "RS.2", "RS.3",
]
TOTAL_REQUIREMENTS = len(BASELINE_REQUIREMENT_IDS)  # 20


def _compute_summary(a: CsrmAssessment) -> CsrmAssessmentSummary:
    objects = a.objects
    elevated_count = sum(1 for o in objects if o.protection_level == "elevated")

    all_ratings = [r for o in objects for r in o.baseline_ratings]
    met_ratings = [r for r in all_ratings if r.status == "met"]

    baseline_met_pct = (
        round(len(met_ratings) / (len(objects) * TOTAL_REQUIREMENTS) * 100, 1)
        if objects else None
    )

    objects_fully_assessed = sum(
        1 for o in objects
        if len([r for r in o.baseline_ratings if r.status != "not_assessed"]) == TOTAL_REQUIREMENTS
    )

    return CsrmAssessmentSummary(
        **CsrmAssessmentRead.model_validate(a).model_dump(),
        objects_count=len(objects),
        elevated_count=elevated_count,
        baseline_met_pct=baseline_met_pct,
        objects_fully_assessed=objects_fully_assessed,
    )


def list_assessments(db: Session) -> list[CsrmAssessmentSummary]:
    rows = db.execute(
        select(CsrmAssessment).order_by(CsrmAssessment.created_at.desc())
    ).scalars().all()
    return [_compute_summary(a) for a in rows]


def create_assessment(db: Session, data: CsrmAssessmentCreate) -> CsrmAssessmentRead:
    obj = CsrmAssessment(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return CsrmAssessmentRead.model_validate(obj)


def get_assessment(db: Session, assessment_id: uuid.UUID) -> CsrmAssessmentDetail:
    obj = db.get(CsrmAssessment, assessment_id)
    if not obj:
        raise ValueError(f"Assessment {assessment_id} not found.")
    return CsrmAssessmentDetail.model_validate(obj)


def patch_assessment(db: Session, assessment_id: uuid.UUID, data: CsrmAssessmentPatch) -> CsrmAssessmentRead:
    obj = db.get(CsrmAssessment, assessment_id)
    if not obj:
        raise ValueError(f"Assessment {assessment_id} not found.")
    for k, v in data.model_dump(exclude_none=True).items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return CsrmAssessmentRead.model_validate(obj)


def delete_assessment(db: Session, assessment_id: uuid.UUID) -> bool:
    obj = db.get(CsrmAssessment, assessment_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True


def create_protection_object(
    db: Session, assessment_id: uuid.UUID, data: ProtectionObjectCreate
) -> ProtectionObjectRead:
    obj = CsrmProtectionObject(assessment_id=assessment_id, **data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return ProtectionObjectRead.model_validate(obj)


def patch_protection_object(
    db: Session, object_id: uuid.UUID, data: ProtectionObjectPatch
) -> ProtectionObjectRead:
    obj = db.get(CsrmProtectionObject, object_id)
    if not obj:
        raise ValueError(f"Protection object {object_id} not found.")
    for k, v in data.model_dump(exclude_none=True).items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return ProtectionObjectRead.model_validate(obj)


def delete_protection_object(db: Session, object_id: uuid.UUID) -> bool:
    obj = db.get(CsrmProtectionObject, object_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True


def upsert_baseline_ratings(
    db: Session, object_id: uuid.UUID, ratings: list[BaselineRatingUpsert]
) -> list[BaselineRatingRead]:
    obj = db.get(CsrmProtectionObject, object_id)
    if not obj:
        raise ValueError(f"Protection object {object_id} not found.")

    rows = [
        {
            "assessment_id": obj.assessment_id,
            "object_id": object_id,
            "requirement_id": r.requirement_id,
            "status": r.status,
            "exception_justification": r.exception_justification,
            "notes": r.notes,
        }
        for r in ratings
    ]
    stmt = pg_insert(CsrmBaselineRating).values(rows)
    stmt = stmt.on_conflict_do_update(
        constraint="uq_csrm_baseline_rating",
        set_={
            "status": stmt.excluded.status,
            "exception_justification": stmt.excluded.exception_justification,
            "notes": stmt.excluded.notes,
            "updated_at": sqlalchemy.func.now(),
        },
    )
    db.execute(stmt)
    db.commit()

    saved = db.execute(
        select(CsrmBaselineRating).where(CsrmBaselineRating.object_id == object_id)
    ).scalars().all()
    return [BaselineRatingRead.model_validate(r) for r in saved]


def create_elevated_tom(
    db: Session, object_id: uuid.UUID, data: ElevatedTomCreate
) -> ElevatedTomRead:
    obj = db.get(CsrmProtectionObject, object_id)
    if not obj:
        raise ValueError(f"Protection object {object_id} not found.")
    tom = CsrmElevatedTom(assessment_id=obj.assessment_id, object_id=object_id, **data.model_dump())
    db.add(tom)
    db.commit()
    db.refresh(tom)
    return ElevatedTomRead.model_validate(tom)


def patch_elevated_tom(db: Session, tom_id: uuid.UUID, data: ElevatedTomPatch) -> ElevatedTomRead:
    tom = db.get(CsrmElevatedTom, tom_id)
    if not tom:
        raise ValueError(f"TOM {tom_id} not found.")
    for k, v in data.model_dump(exclude_none=True).items():
        setattr(tom, k, v)
    db.commit()
    db.refresh(tom)
    return ElevatedTomRead.model_validate(tom)


def delete_elevated_tom(db: Session, tom_id: uuid.UUID) -> bool:
    tom = db.get(CsrmElevatedTom, tom_id)
    if not tom:
        return False
    db.delete(tom)
    db.commit()
    return True
