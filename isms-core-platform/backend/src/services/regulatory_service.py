"""Service layer for generic regulatory compliance assessments (NIS2, DORA, extensible)."""

import logging
import uuid

from sqlalchemy import func, select
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.orm import Session

from src.domain.frameworks import Framework, FrameworkControl
from src.domain.regulatory import RegulatoryAssessment, RegulatoryRating
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

logger = logging.getLogger(__name__)

# For NIS2: all requirements are level=0
# For DORA: requirements are level=1 (articles), grouped by level=0 (chapters)
_ASSESSABLE_LEVEL = {
    "NIS2": 0,
    "DORA": 1,
    "CIS_V8": 1,
}


# ── Framework helpers ──────────────────────────────────────────────────────────

def _get_framework(db: Session, framework_code: str) -> Framework:
    fw = db.execute(
        select(Framework).where(Framework.code == framework_code)
    ).scalar_one_or_none()
    if not fw:
        raise ValueError(f"Framework '{framework_code}' not loaded — run /admin/load first.")
    return fw


def _get_requirements(db: Session, framework_id: uuid.UUID, framework_code: str) -> list[FrameworkControl]:
    """Return assessable controls for this framework."""
    level = _ASSESSABLE_LEVEL.get(framework_code, 0)
    return list(
        db.execute(
            select(FrameworkControl)
            .where(
                FrameworkControl.framework_id == framework_id,
                FrameworkControl.level == level,
            )
            .order_by(FrameworkControl.sort_order)
        ).scalars().all()
    )


def _get_groups(db: Session, framework_id: uuid.UUID, framework_code: str) -> dict[uuid.UUID, FrameworkControl]:
    """Return {parent_id: FrameworkControl} for grouping (only needed when level=1)."""
    if _ASSESSABLE_LEVEL.get(framework_code, 0) == 0:
        return {}
    groups = db.execute(
        select(FrameworkControl).where(
            FrameworkControl.framework_id == framework_id,
            FrameworkControl.level == 0,
        )
    ).scalars().all()
    return {g.id: g for g in groups}


def _build_requirement_reads(
    requirements: list[FrameworkControl],
    groups: dict[uuid.UUID, FrameworkControl],
) -> list[RequirementRead]:
    result = []
    for r in requirements:
        group = groups.get(r.parent_id) if r.parent_id else None
        result.append(RequirementRead(
            id=r.id,
            control_id=r.control_id,
            title=r.title,
            description=r.description,
            level=r.level,
            sort_order=r.sort_order,
            group_id=group.control_id if group else None,
            group_title=group.title if group else None,
        ))
    return result


def _build_rating_read(rating: RegulatoryRating, req: FrameworkControl | None, group_id: str | None) -> RatingRead:
    return RatingRead(
        id=rating.id,
        assessment_id=rating.assessment_id,
        requirement_id=rating.requirement_id,
        requirement_control_id=req.control_id if req else "",
        requirement_title=req.title if req else "",
        group_id=group_id,
        current_score=rating.current_score,
        target_score=rating.target_score,
        rating_status=rating.rating_status,
        notes=rating.notes,
        evidence_ref=rating.evidence_ref,
        updated_at=rating.updated_at,
    )


# ── List requirements (seed for UI) ───────────────────────────────────────────

def list_requirements(db: Session, framework_code: str) -> list[RequirementRead]:
    fw = _get_framework(db, framework_code)
    reqs = _get_requirements(db, fw.id, framework_code)
    groups = _get_groups(db, fw.id, framework_code)
    return _build_requirement_reads(reqs, groups)


# ── Assessment CRUD ────────────────────────────────────────────────────────────

def list_assessments(db: Session, framework_code: str) -> list[AssessmentSummary]:
    assessments = list(
        db.execute(
            select(RegulatoryAssessment)
            .where(RegulatoryAssessment.framework_code == framework_code)
            .order_by(RegulatoryAssessment.created_at.desc())
        ).scalars().all()
    )

    fw = _get_framework(db, framework_code)
    total = len(_get_requirements(db, fw.id, framework_code))

    result = []
    for a in assessments:
        ratings = a.ratings
        scored = [r for r in ratings if r.current_score is not None]
        not_applicable = [r for r in ratings if r.rating_status == "not_applicable"]
        compliant = [r for r in ratings if r.rating_status == "compliant"]
        partial = [r for r in ratings if r.rating_status == "partial"]
        non_compliant = [r for r in ratings if r.rating_status == "non_compliant"]
        avg_current = (
            sum(r.current_score for r in scored) / len(scored) if scored else None
        )
        scored_target = [r for r in ratings if r.target_score is not None]
        avg_target = (
            sum(r.target_score for r in scored_target) / len(scored_target) if scored_target else None
        )
        result.append(AssessmentSummary(
            **AssessmentRead.model_validate(a).model_dump(),
            rated_count=len(ratings),
            total_requirements=total,
            avg_current_score=round(avg_current, 2) if avg_current is not None else None,
            avg_target_score=round(avg_target, 2) if avg_target is not None else None,
            compliant_count=len(compliant),
            partial_count=len(partial),
            non_compliant_count=len(non_compliant),
            not_applicable_count=len(not_applicable),
        ))
    return result


def create_assessment(db: Session, data: AssessmentCreate) -> AssessmentRead:
    # Validate framework exists
    _get_framework(db, data.framework_code)
    obj = RegulatoryAssessment(**data.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return AssessmentRead.model_validate(obj)


def get_full_assessment(db: Session, assessment_id: uuid.UUID) -> FullAssessment:
    obj = db.get(RegulatoryAssessment, assessment_id)
    if not obj:
        raise ValueError(f"Assessment {assessment_id} not found.")

    fw = _get_framework(db, obj.framework_code)
    reqs = _get_requirements(db, fw.id, obj.framework_code)
    groups = _get_groups(db, fw.id, obj.framework_code)

    req_map = {r.id: r for r in reqs}
    # Build group_id lookup: req.id -> group control_id
    group_map: dict[uuid.UUID, str | None] = {}
    for r in reqs:
        group = groups.get(r.parent_id) if r.parent_id else None
        group_map[r.id] = group.control_id if group else None

    ratings_read = [
        _build_rating_read(rating, req_map.get(rating.requirement_id), group_map.get(rating.requirement_id))
        for rating in obj.ratings
    ]

    return FullAssessment(
        assessment=AssessmentRead.model_validate(obj),
        requirements=_build_requirement_reads(reqs, groups),
        ratings=ratings_read,
    )


def update_assessment(db: Session, assessment_id: uuid.UUID, data: AssessmentUpdate) -> AssessmentRead:
    obj = db.get(RegulatoryAssessment, assessment_id)
    if not obj:
        raise ValueError(f"Assessment {assessment_id} not found.")
    for field, value in data.model_dump(exclude_none=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return AssessmentRead.model_validate(obj)


def delete_assessment(db: Session, assessment_id: uuid.UUID) -> bool:
    obj = db.get(RegulatoryAssessment, assessment_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True


# ── Ratings upsert ─────────────────────────────────────────────────────────────

def upsert_ratings(db: Session, assessment_id: uuid.UUID, ratings: list[RatingUpsert]) -> list[RatingRead]:
    obj = db.get(RegulatoryAssessment, assessment_id)
    if not obj:
        raise ValueError(f"Assessment {assessment_id} not found.")

    fw = _get_framework(db, obj.framework_code)
    reqs = _get_requirements(db, fw.id, obj.framework_code)
    groups = _get_groups(db, fw.id, obj.framework_code)
    req_map = {r.id: r for r in reqs}
    group_map: dict[uuid.UUID, str | None] = {}
    for r in reqs:
        group = groups.get(r.parent_id) if r.parent_id else None
        group_map[r.id] = group.control_id if group else None

    rows = [
        {
            "assessment_id": assessment_id,
            "requirement_id": r.requirement_id,
            "current_score": r.current_score,
            "target_score": r.target_score,
            "rating_status": r.rating_status,
            "notes": r.notes,
            "evidence_ref": r.evidence_ref,
        }
        for r in ratings
    ]

    stmt = pg_insert(RegulatoryRating).values(rows)
    stmt = stmt.on_conflict_do_update(
        constraint="uq_compliance_rating_assessment_req",
        set_={
            "current_score": stmt.excluded.current_score,
            "target_score": stmt.excluded.target_score,
            "rating_status": stmt.excluded.rating_status,
            "notes": stmt.excluded.notes,
            "evidence_ref": stmt.excluded.evidence_ref,
            "updated_at": func.now(),
        },
    )
    db.execute(stmt)
    db.commit()

    # Reload
    saved = list(
        db.execute(
            select(RegulatoryRating).where(
                RegulatoryRating.assessment_id == assessment_id,
                RegulatoryRating.requirement_id.in_([r.requirement_id for r in ratings]),
            )
        ).scalars().all()
    )
    return [
        _build_rating_read(s, req_map.get(s.requirement_id), group_map.get(s.requirement_id))
        for s in saved
    ]
