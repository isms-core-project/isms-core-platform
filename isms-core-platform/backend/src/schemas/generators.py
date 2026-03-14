"""Pydantic schemas for generator_definitions API responses."""

import uuid
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

SheetType = Literal["instructions", "input", "summary", "evidence", "approval"]


class SheetInfo(BaseModel):
    name: str
    type: SheetType

    model_config = {"from_attributes": True}


class GeneratorRead(BaseModel):
    id: uuid.UUID
    document_id: str
    workbook_name: str
    control_id: str
    control_name: str
    group_code: str
    control_group_id: uuid.UUID | None = None
    domain_number: int | None = None
    domain_total: int | None = None
    is_stacked: bool = False
    stacked_control_ids: list[str] | None = None
    sheets: list[SheetInfo] = []
    sheet_count: int = 0
    sheet_schemas: list[dict] = []
    product_type: str = "framework"
    source_file: str | None = None
    parsed_at: datetime | None = None
    user_override: bool = False

    model_config = {"from_attributes": True}


class GeneratorUpdate(BaseModel):
    """Fields editable by users. Sets user_override=true on save."""
    workbook_name: str = Field(min_length=1, max_length=200)
    domain_number: int | None = None
    domain_total: int | None = None
    sheets: list[SheetInfo] = Field(min_length=1)


class GeneratorGrouped(BaseModel):
    """Generators for one control group."""
    group_code: str
    control_name: str
    section: str  # "A.5" | "A.6" | "A.7" | "A.8"
    generators: list[GeneratorRead]
    total_domains: int
