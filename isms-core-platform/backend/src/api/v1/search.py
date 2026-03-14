"""Search API endpoints — full-text search across ISMS CORE documents."""

from fastapi import APIRouter, Depends, HTTPException, Query

from src.core.dependencies import get_current_user
from src.domain.users import User
from src.schemas.search import SearchHit, SearchResponse
from src.services import search_service

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/status")
def search_status(_user: User = Depends(get_current_user)):
    """Lightweight OpenSearch availability probe. Used by frontend for polling."""
    return {"available": search_service.is_available()}


@router.get("", response_model=SearchResponse)
def search(
    q: str = Query(..., min_length=1, max_length=500, description="Search query"),
    type: str | None = Query(
        None, description="Filter: 'implementation' or 'policy'"
    ),
    control_group: str | None = Query(
        None, description="Control group code, e.g. 'a.8.24'"
    ),
    product: str | None = Query(
        None, description="Filter: 'framework' or 'operational'"
    ),
    impl_type: str | None = Query(None, description="Filter: 'UG' or 'TG'"),
    policy_type: str | None = Query(
        None, description="Filter: 'POL', 'OP-POL', etc."
    ),
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    _user: User = Depends(get_current_user),
):
    """Full-text search across implementations and policies."""
    if not search_service.is_available():
        raise HTTPException(
            status_code=503,
            detail="Search service unavailable — OpenSearch is not connected",
        )

    result = search_service.search_all(
        query=q,
        doc_type=type,
        control_group=control_group,
        product_type=product,
        impl_type=impl_type,
        policy_type=policy_type,
        limit=limit,
        offset=offset,
    )
    return SearchResponse(
        total=result["total"],
        hits=[SearchHit(**h) for h in result["hits"]],
        took_ms=result["took_ms"],
        available=result.get("available", True),
    )
