from __future__ import annotations
from datetime import date, datetime
from uuid import UUID
from pydantic import BaseModel


class CollectionCreate(BaseModel):
    name: str
    description: str | None = None
    product_family: str
    product_type: str | None = None
    due_date: date | None = None


class CollectionPatch(BaseModel):
    name: str | None = None
    description: str | None = None
    due_date: date | None = None


class CollectionStats(BaseModel):
    total: int
    started: int
    completion_pct: float
    items_total: int
    items_compliant: int
    items_non_compliant: int
    compliance_pct: float
    status: str  # not_started / in_progress / complete


class CollectionMember(BaseModel):
    assessment_id: str
    document_id: str
    workbook_name: str
    group_code: str
    group_name: str
    product_type: str
    items_total: int
    items_compliant: int
    items_non_compliant: int
    compliance_pct: float
    model_config = {"from_attributes": True}


class CollectionRead(BaseModel):
    id: UUID
    name: str
    description: str | None
    product_family: str
    product_type: str | None
    due_date: date | None
    created_at: datetime
    updated_at: datetime
    stats: CollectionStats
    members: list[CollectionMember]
    model_config = {"from_attributes": True}


class CollectionListItem(BaseModel):
    id: UUID
    name: str
    description: str | None
    product_family: str
    product_type: str | None
    due_date: date | None
    created_at: datetime
    updated_at: datetime
    stats: CollectionStats
    model_config = {"from_attributes": True}
