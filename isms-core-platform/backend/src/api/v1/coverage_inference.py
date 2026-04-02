"""Cross-framework coverage inference API.

GET /api/v1/coverage/infer
    ?project_id=&target_framework=NIS2    single framework inferred coverage

GET /api/v1/coverage/multi-framework
    ?project_id=                          all target frameworks coverage summary

GET /api/v1/coverage/gap-map
    ?project_id=&target_framework=DORA    uncovered target controls + missing ISO sources

GET /api/v1/coverage/custom/{framework_id}
    ?project_id=                          custom framework coverage based on iso_mappings
"""

import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, get_org_context
from src.database.session import get_db
from src.domain.control_groups import ControlGroup
from src.domain.custom_framework import CustomControl, CustomFramework
from src.domain.frameworks import Framework
from src.domain.users import User
from src.services.mapping_engine import (
    compute_gap_map,
    compute_multi_framework,
    get_covered_fc_ids,
    get_project_covered_cg_ids,
    infer_single_framework,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/coverage", tags=["coverage"])


def _resolve_framework(db: DBSession, code: str) -> Framework:
    fw = db.execute(
        select(Framework).where(Framework.code.ilike(f'{code}%'))
    ).scalar_one_or_none()
    if not fw:
        raise HTTPException(status_code=404, detail=f"Framework '{code}' not found")
    return fw


@router.get("/infer")
def infer_coverage(
    target_framework: str = Query(..., description="Framework code prefix, e.g. NIS2, DORA, GDPR"),
    project_id: str | None = Query(None),
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    """Inferred coverage of a single target framework based on project assessments."""
    target_fw = _resolve_framework(db, target_framework)
    covered_cg_ids = get_project_covered_cg_ids(db, project_id, str(org_id))
    covered_fc_ids = get_covered_fc_ids(db, covered_cg_ids)
    return infer_single_framework(db, covered_fc_ids, target_fw)


@router.get("/multi-framework")
def multi_framework_coverage(
    project_id: str | None = Query(None),
    frameworks: str | None = Query(None, description="Comma-separated codes, e.g. NIS2,DORA,GDPR"),
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    """Inferred coverage across all (or selected) target frameworks for a project."""
    covered_cg_ids = get_project_covered_cg_ids(db, project_id, str(org_id))
    covered_fc_ids = get_covered_fc_ids(db, covered_cg_ids)
    fw_codes = [c.strip() for c in frameworks.split(',')] if frameworks else None
    results = compute_multi_framework(db, covered_fc_ids, fw_codes)
    return {
        'project_id':         project_id,
        'assessed_controls':  len(covered_cg_ids),
        'frameworks':         results,
    }


@router.get("/gap-map")
def coverage_gap_map(
    target_framework: str = Query(..., description="Framework code prefix, e.g. DORA"),
    project_id: str | None = Query(None),
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    """Target framework controls not yet covered by the project's ISO 27001 assessments."""
    target_fw = _resolve_framework(db, target_framework)
    covered_cg_ids = get_project_covered_cg_ids(db, project_id, str(org_id))
    covered_fc_ids = get_covered_fc_ids(db, covered_cg_ids)
    gaps = compute_gap_map(db, covered_fc_ids, target_fw)
    return {
        'framework':      target_fw.name,
        'framework_code': target_fw.code,
        'gap_count':      len(gaps),
        'gaps':           gaps,
    }


@router.get("/custom/{framework_id}")
def custom_framework_coverage(
    framework_id: uuid.UUID,
    project_id: str | None = Query(None),
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
    _: User = Depends(get_current_user),
):
    """Coverage of a custom framework's controls based on ISO mapping strings and project assessments."""
    # Load framework and verify org ownership
    fw = db.execute(
        select(CustomFramework).where(
            CustomFramework.id == framework_id,
            CustomFramework.org_id == org_id,
        )
    ).scalar_one_or_none()
    if not fw:
        raise HTTPException(status_code=404, detail="Custom framework not found")

    # Load all controls for this framework
    controls = db.execute(
        select(CustomControl).where(CustomControl.framework_id == framework_id)
    ).scalars().all()

    # Get covered ControlGroup IDs from assessments, then resolve their group_codes
    covered_cg_ids = get_project_covered_cg_ids(db, project_id, str(org_id))
    covered_codes: set[str] = set()
    if covered_cg_ids:
        groups = db.execute(
            select(ControlGroup).where(ControlGroup.id.in_(covered_cg_ids))
        ).scalars().all()
        covered_codes = {g.group_code.lower() for g in groups}

    # Evaluate each custom control against covered ISO codes
    result_controls = []
    covered_count = 0
    for ctrl in controls:
        iso_refs: list[str] = ctrl.iso_mappings or []
        # A control is covered if any iso_mapping substring-matches a covered group_code
        # (dots stripped for comparison, e.g. "A.5.15" → "a515" matches "a.5.15" → "a515")
        matched = [
            ref for ref in iso_refs
            if any(
                ref.lower().replace('.', '') in code.replace('.', '')
                for code in covered_codes
            )
        ]
        is_covered = len(matched) > 0
        if is_covered:
            covered_count += 1
        result_controls.append({
            'control_id':  ctrl.control_id,
            'title':       ctrl.title,
            'category':    ctrl.category,
            'covered':     is_covered,
            'matched_iso': matched,
        })

    total = len(controls)
    coverage_pct = round((covered_count / total * 100), 1) if total > 0 else 0.0

    return {
        'framework_id':     str(framework_id),
        'framework_name':   fw.name,
        'short_code':       fw.short_code,
        'total_controls':   total,
        'covered_controls': covered_count,
        'coverage_pct':     coverage_pct,
        'controls':         result_controls,
    }
