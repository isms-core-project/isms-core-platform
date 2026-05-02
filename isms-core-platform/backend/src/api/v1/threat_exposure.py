"""Threat Exposure — correlates active TI feed techniques with ISO 27001 control gaps.

Joins:
  ti_iocs.mitre_tids  →  crosswalk (MITRE_ATTACK_V19 → ISO27001_2022, direct + transitive via NIST 800-53)
                       →  control_groups.framework_status + assessments.overall_score

Returns a prioritised list of active MITRE techniques, the ISO 27001 controls that
mitigate them, and the current assessment status of each control so auditors can
immediately see where live threat activity maps to implementation gaps.
"""

import json
import logging
import os
from collections import defaultdict

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import ARRAY, String, bindparam, select, text
from sqlalchemy.orm import Session as DBSession

from src.core.config import get_settings
from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.domain.assessments import Assessment
from src.domain.control_groups import ControlGroup

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/threat-intel", tags=["threat-intel"])


def _ti_enabled() -> bool:
    return get_settings().threat_intel_enabled


def _require_ti_enabled():
    if not _ti_enabled():
        raise HTTPException(
            status_code=503,
            detail="Threat intelligence module not active — enable with --profile threat-intel",
        )


# ── Schemas ────────────────────────────────────────────────────────────────────

class ExposedControl(BaseModel):
    control_code: str
    control_name: str | None = None
    framework_status: str | None = None
    assessment_score: float | None = None
    gap: bool

class ExposureTechnique(BaseModel):
    mitre_tid: str
    ioc_count: int
    sources: list[str]
    iso_controls: list[ExposedControl]
    max_gap_score: float | None = None  # lowest assessment score among mapped controls

class ThreatExposureResponse(BaseModel):
    technique_count: int
    affected_controls: int
    gap_controls: int
    items: list[ExposureTechnique]


# ── Crosswalk loader ────────────────────────────────────────────────────────────

def _build_mitre_to_iso() -> dict[str, set[str]]:
    """
    Returns {mitre_technique_id: {iso_control_code, ...}}.
    Combines direct ISO→MITRE mappings and transitive ISO→NIST→MITRE mappings.
    """
    datasets_path = os.environ.get("DATASETS_PATH", "/app/datasets")
    path = os.path.join(datasets_path, "crosswalk.json")
    try:
        with open(path) as f:
            objects = json.load(f).get("objects", [])
    except Exception as exc:
        logger.warning("Crosswalk load failed: %s", exc)
        return {}

    iso_to_mitre: dict[str, set[str]] = defaultdict(set)
    iso_to_nist:  dict[str, set[str]] = defaultdict(set)
    nist_to_mitre: dict[str, set[str]] = defaultdict(set)

    for obj in objects:
        sf = obj.get("source_framework", "")
        tf = obj.get("target_framework", "")
        sc = obj.get("source_control", "")
        tc = obj.get("target_control", "")
        if not (sc and tc):
            continue
        if sf == "ISO27001_2022" and tf == "MITRE_ATTACK_V19":
            iso_to_mitre[sc].add(tc)
        elif sf == "ISO27001_2022" and tf == "NIST_800_53_R5":
            iso_to_nist[sc].add(tc)
        elif sf == "NIST_800_53_R5" and tf == "MITRE_ATTACK_V19":
            nist_to_mitre[sc].add(tc)

    # Transitive: ISO → NIST → MITRE
    for iso_ctrl, nist_ctrls in iso_to_nist.items():
        for nist in nist_ctrls:
            iso_to_mitre[iso_ctrl].update(nist_to_mitre.get(nist, set()))

    # Invert — exclude tactic codes (TA prefix; too broad to be actionable)
    mitre_to_iso: dict[str, set[str]] = defaultdict(set)
    for iso_ctrl, tids in iso_to_mitre.items():
        for tid in tids:
            if tid.startswith("T") and not tid.startswith("TA"):
                mitre_to_iso[tid].add(iso_ctrl)

    return dict(mitre_to_iso)


# ── Endpoint ───────────────────────────────────────────────────────────────────

@router.get("/exposure", response_model=ThreatExposureResponse)
def get_threat_exposure(
    db: DBSession = Depends(get_db),
    _current_user=Depends(get_current_user),
):
    """
    Correlates active TI feed IOCs (via MITRE technique IDs) with ISO 27001
    control assessments. Returns prioritised exposure list: technique → affected
    controls → implementation gap status.
    """
    _require_ti_enabled()

    mitre_to_iso = _build_mitre_to_iso()
    if not mitre_to_iso:
        return ThreatExposureResponse(technique_count=0, affected_controls=0, gap_controls=0, items=[])

    # Active MITRE techniques in our TI feeds
    tid_rows = db.execute(text("""
        SELECT mitre_tid,
               COUNT(*)                         AS ioc_count,
               array_agg(DISTINCT source)       AS sources
        FROM   ti_iocs,
               jsonb_array_elements_text(mitre_tids) AS mitre_tid
        WHERE  mitre_tid <> ''
        GROUP  BY mitre_tid
        ORDER  BY ioc_count DESC
        LIMIT  500
    """)).all()

    # Keep only TIDs we have ISO mappings for
    matched = [(r.mitre_tid, r.ioc_count, list(r.sources))
               for r in tid_rows if r.mitre_tid in mitre_to_iso]

    if not matched:
        return ThreatExposureResponse(technique_count=0, affected_controls=0, gap_controls=0, items=[])

    # Collect all ISO control codes we need
    all_iso_codes: set[str] = set()
    for tid, _, _ in matched:
        all_iso_codes.update(mitre_to_iso[tid])

    # Control group status
    cg_rows = db.execute(
        select(ControlGroup.group_code, ControlGroup.name, ControlGroup.framework_status)
        .where(ControlGroup.group_code.in_(all_iso_codes))
    ).all()
    cg_map = {r.group_code: r for r in cg_rows}

    # Most recent assessment score per control group (DISTINCT ON)
    score_rows = db.execute(
        text("""
            SELECT DISTINCT ON (cg.group_code)
                   cg.group_code,
                   a.overall_score
            FROM   control_groups cg
            JOIN   assessments a ON a.control_group_id = cg.id
            WHERE  cg.group_code = ANY(:codes)
            ORDER  BY cg.group_code, a.updated_at DESC
        """).bindparams(bindparam("codes", type_=ARRAY(String))),
        {"codes": list(all_iso_codes)},
    ).all()
    score_map = {r.group_code: float(r.overall_score) for r in score_rows if r.overall_score is not None}

    # Build response
    items: list[ExposureTechnique] = []
    gap_control_codes: set[str] = set()

    for tid, ioc_count, sources in matched:
        iso_codes = sorted(mitre_to_iso[tid])
        controls: list[ExposedControl] = []
        for code in iso_codes:
            cg = cg_map.get(code)
            score = score_map.get(code)
            status = cg.framework_status if cg else None
            gap = score is None or float(score) < 70 or str(status) in ("incomplete", "not_started")
            if gap:
                gap_control_codes.add(code)
            controls.append(ExposedControl(
                control_code=code,
                control_name=cg.name if cg else None,
                framework_status=str(status) if status else None,
                assessment_score=score,
                gap=gap,
            ))
        min_score = min((c.assessment_score for c in controls if c.assessment_score is not None), default=None)
        items.append(ExposureTechnique(
            mitre_tid=tid,
            ioc_count=ioc_count,
            sources=sources,
            iso_controls=controls,
            max_gap_score=min_score,
        ))

    # Sort: most gaps first, then lowest assessment score (worst exposure), then most IOCs
    items.sort(key=lambda x: (
        -sum(1 for c in x.iso_controls if c.gap),
        x.max_gap_score if x.max_gap_score is not None else 200,
        -x.ioc_count,
    ))

    all_affected = set(c.control_code for it in items for c in it.iso_controls)

    return ThreatExposureResponse(
        technique_count=len(items),
        affected_controls=len(all_affected),
        gap_controls=len(gap_control_codes),
        items=items,
    )
