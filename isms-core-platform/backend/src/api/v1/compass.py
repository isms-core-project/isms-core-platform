"""ISMS Compass — gap analysis endpoints.

POST /api/v1/compass/analyse  — analyse a document against the Gold Standard
GET  /api/v1/compass/status   — check if Compass is available
"""

import logging

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.session import get_db
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
