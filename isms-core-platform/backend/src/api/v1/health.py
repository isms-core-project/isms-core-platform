from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session as DBSession

from src.database.session import get_db
from src.schemas.common import HealthResponse
from src.services import search_service

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check(db: DBSession = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        db_status = "ok"
    except Exception:
        db_status = "error"

    os_status = "ok" if search_service.is_available() else "unavailable"

    return HealthResponse(
        status="ok" if db_status == "ok" else "degraded",
        database=db_status,
        opensearch=os_status,
    )
