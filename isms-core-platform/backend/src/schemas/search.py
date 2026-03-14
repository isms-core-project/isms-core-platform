"""Pydantic schemas for search API request/response."""

from pydantic import BaseModel, Field


class SearchHit(BaseModel):
    document_id: str
    title: str
    type: str  # "implementation" or "policy"
    score: float
    control_group_code: str | None = None
    control_group_name: str | None = None
    product_type: str | None = None
    impl_type: str | None = None
    policy_type: str | None = None
    word_count: int | None = None
    highlights: dict = {}
    snippet: str = ""


class SearchResponse(BaseModel):
    total: int
    hits: list[SearchHit]
    took_ms: int
    available: bool = True


class SearchStatus(BaseModel):
    available: bool
    cluster_status: str | None = None
    indices: dict | None = None
    error: str | None = None
