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

    if not agg:
        return {"project_id": project_id, "frameworks": [], "generated_at": now.isoformat()}

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
