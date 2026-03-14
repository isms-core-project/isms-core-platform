from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class HealthResponse(BaseModel):
    status: str
    database: str
    opensearch: str = "unknown"
    version: str = "1.0.0"


class ErrorResponse(BaseModel):
    error: bool = True
    status_code: int
    detail: str


class PaginatedResponse(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int
    page_size: int
    pages: int
