"""ISMS Compass — gap analysis endpoints.

GET  /api/v1/compass/         — framework coverage summary for a project
POST /api/v1/compass/analyse  — analyse a document against the Gold Standard
GET  /api/v1/compass/status   — check if Compass is available
"""

import logging
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.enums import ProductFamily, ProductType
from src.database.session import get_db
from src.domain.assessments import Assessment
from src.domain.control_groups import ControlGroup
from src.domain.frameworks import Framework, FrameworkControl
from src.domain.regulatory import RegulatoryAssessment, RegulatoryRating
from src.domain.users import User
from src.services.compass_service import analyse_document

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/compass", tags=["compass"])


class CompassRequest(BaseModel):
    group_code: str
    document_text: str


class CompassGap(BaseModel):
    topic: str
    severity: str
    description: str
    iso_clause: str
    recommendation: str


class CompassStrength(BaseModel):
    topic: str
    detail: str


class CompassReport(BaseModel):
    control_group_code: str
    control_group_name: str
    coverage_score: int
    summary: str
    strengths: list[CompassStrength]
    gaps: list[CompassGap]
    disclaimer: str
    model_used: str
    tokens_used: int

    model_config = {"protected_namespaces": ()}


_PT_META: dict[ProductType, dict] = {
    ProductType.FRAMEWORK:   {"framework_code": "iso27001",    "framework_name": "ISO 27001:2022 Framework"},
    ProductType.OPERATIONAL: {"framework_code": "iso27001_op", "framework_name": "ISO 27001:2022 Operational"},
    ProductType.PRIVACY:     {"framework_code": "iso27701",    "framework_name": "ISO 27701:2019"},
    ProductType.CLOUD:       {"framework_code": "iso27018",    "framework_name": "ISO 27018:2019"},
    ProductType.AI:          {"framework_code": "iso42001",    "framework_name": "ISO 42001:2023"},
}

# Mirrors regulatory_service._ASSESSABLE_LEVEL — which level holds assessable leaf controls
_REG_ASSESSABLE_LEVEL: dict[str, int] = {
    "NIS2": 0, "DORA": 1, "CIS_V8": 1, "BSI_IT_GRUNDSCHUTZ": 1,
    "TISAX": 1, "CH_NDSG": 1, "CH_ISG": 1, "EU_CRA": 1,
    "EU_AI_ACT": 1, "EU_CLOUD_SOV": 0, "COBIT_2019": 1,
    "NIST_AI_RMF": 2, "CSA_CCM_V4_1": 1, "CSA_AICM_V1": 1,
    "NIST_800_53_R5": 1, "ISO42001": 1, "NCSC_CAF": 2, "FR_NIS2_RECYF": 1,
}

_REG_META: dict[str, str] = {
    "NIS2": "NIS2 Directive", "DORA": "DORA", "CIS_V8": "CIS Controls v8",
    "BSI_IT_GRUNDSCHUTZ": "BSI IT-Grundschutz", "TISAX": "TISAX",
    "CH_NDSG": "Swiss nDSG", "CH_ISG": "Swiss ISG", "EU_CRA": "EU CRA",
    "EU_AI_ACT": "EU AI Act", "EU_CLOUD_SOV": "EU Cloud Sovereignty",
    "COBIT_2019": "COBIT 2019", "NIST_AI_RMF": "NIST AI RMF 1.0",
    "CSA_CCM_V4_1": "CSA CCM v4.1", "CSA_AICM_V1": "CSA AICM v1",
    "NIST_800_53_R5": "NIST SP 800-53 R5", "ISO42001": "ISO 42001:2023",
    "NCSC_CAF": "NCSC CAF v4.0", "FR_NIS2_RECYF": "ReCyF v2.5",
}


def _coverage_status(pct: float) -> str:
    if pct >= 80:
        return "complete"
    if pct >= 50:
        return "in_progress"
    if pct > 0:
        return "draft"
    return "not_started"


@router.get("/")
def get_coverage(
    project_id: str = Query(...),
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
) -> dict:
    """Framework coverage summary across all product types for a project."""
    pid = uuid.UUID(project_id)
    now = datetime.now(timezone.utc)

    # Assessment counts grouped by product_type
    agg = db.execute(
        select(
            Assessment.product_type,
            func.count(func.distinct(Assessment.control_group_id)).label("mapped"),
            func.avg(Assessment.overall_score).label("avg_score"),
        )
        .where(Assessment.project_id == pid)
        .group_by(Assessment.product_type)
    ).all()

    # Total control counts per product family
    totals: dict[ProductType, int] = {
        ProductType.FRAMEWORK: db.scalar(
            select(func.count(ControlGroup.id))
            .where(ControlGroup.product_family == ProductFamily.ISMS, ControlGroup.has_framework.is_(True))
        ) or 0,
        ProductType.OPERATIONAL: db.scalar(
            select(func.count(ControlGroup.id))
            .where(ControlGroup.product_family == ProductFamily.ISMS, ControlGroup.has_operational.is_(True))
        ) or 0,
        ProductType.PRIVACY: db.scalar(
            select(func.count(ControlGroup.id)).where(ControlGroup.product_family == ProductFamily.PRIVACY)
        ) or 0,
        ProductType.CLOUD: db.scalar(
            select(func.count(ControlGroup.id)).where(ControlGroup.product_family == ProductFamily.CLOUD)
        ) or 0,
        ProductType.AI: db.scalar(
            select(func.count(ControlGroup.id)).where(ControlGroup.product_family == ProductFamily.AI)
        ) or 0,
    }

    frameworks = []
    for row in agg:
        meta = _PT_META.get(row.product_type)
        if not meta:
            continue
        total = totals.get(row.product_type) or 1
        mapped = row.mapped or 0
        pct = round(min(mapped / total * 100, 100), 1)
        frameworks.append({
            "framework_code": meta["framework_code"],
            "framework_name": meta["framework_name"],
            "total_controls": total,
            "mapped_controls": mapped,
            "coverage_pct": pct,
            "avg_score": float(row.avg_score) if row.avg_score is not None else None,
            "status": _coverage_status(pct),
        })

    # Regulatory/compliance assessments (NIS2, DORA, CIS, BSI, TISAX, etc.)
    reg_rows = db.execute(
        select(RegulatoryAssessment.id, RegulatoryAssessment.framework_code, RegulatoryAssessment.status)
        .where(RegulatoryAssessment.project_id == pid)
    ).all()

    by_fw: dict[str, list] = {}
    for ra in reg_rows:
        by_fw.setdefault(ra.framework_code, []).append(ra)

    for code, assessments in by_fw.items():
        level = _REG_ASSESSABLE_LEVEL.get(code, 0)
        fw = db.execute(select(Framework).where(Framework.code == code)).scalar_one_or_none()
        if not fw:
            continue
        total = db.scalar(
            select(func.count(FrameworkControl.id))
            .where(FrameworkControl.framework_id == fw.id, FrameworkControl.level == level)
        ) or 0
        assessment_ids = [a.id for a in assessments]
        mapped = db.scalar(
            select(func.count(func.distinct(RegulatoryRating.requirement_id)))
            .where(
                RegulatoryRating.assessment_id.in_(assessment_ids),
                RegulatoryRating.rating_status != "not_assessed",
            )
        ) or 0
        pct = round(min(mapped / max(total, 1) * 100, 100), 1)
        statuses = [a.status for a in assessments]
        status = "complete" if "complete" in statuses else ("in_progress" if "in_progress" in statuses else "draft")
        frameworks.append({
            "framework_code": code.lower(),
            "framework_name": _REG_META.get(code, code),
            "total_controls": total,
            "mapped_controls": mapped,
            "coverage_pct": pct,
            "avg_score": None,
            "status": status,
        })

    frameworks.sort(key=lambda f: f["coverage_pct"], reverse=True)
    return {"project_id": project_id, "frameworks": frameworks, "generated_at": now.isoformat()}


@router.post("/analyse", response_model=CompassReport)
def analyse(
    body: CompassRequest,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Analyse a document against the ISMS CORE Gold Standard for a given control group."""
    if not body.document_text.strip():
        raise HTTPException(status_code=422, detail="document_text is required.")
    if not body.group_code.strip():
        raise HTTPException(status_code=422, detail="group_code is required.")
    try:
        return analyse_document(db, body.group_code.lower().strip(), body.document_text)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.error("Compass analyse error: %s", e)
        raise HTTPException(status_code=500, detail=f"Analysis failed: {e}")


@router.get("/status")
def compass_status(_user: User = Depends(get_current_user)) -> dict:
    """Check whether ISMS Compass is available."""
    from src.core.config import get_settings
    settings = get_settings()
    return {
        "available": bool(settings.anthropic_api_key),
        "model": settings.ai_model,
    }
