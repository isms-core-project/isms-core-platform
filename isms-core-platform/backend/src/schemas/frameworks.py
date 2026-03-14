import uuid
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class FrameworkRead(BaseModel):
    id: uuid.UUID
    code: str
    name: str
    version: str | None = None
    publisher: str | None = None
    source_url: str | None = None
    description: str | None = None
    jurisdiction: str | None = None
    controls_count: int
    loaded_at: datetime
    metadata: dict = Field(default={}, validation_alias="metadata_")

    model_config = {"from_attributes": True}


class ControlRead(BaseModel):
    id: uuid.UUID
    framework_id: uuid.UUID
    control_id: str
    parent_id: uuid.UUID | None = None
    title: str
    description: str | None = None
    control_type: list[str] = []
    security_properties: list[str] = []
    level: int
    sort_order: int
    metadata: dict = Field(default={}, validation_alias="metadata_")

    model_config = {"from_attributes": True}


class MappingRead(BaseModel):
    id: uuid.UUID
    source_control_id: uuid.UUID
    target_control_id: uuid.UUID
    mapping_type: str
    confidence: Decimal
    source_reference: str | None = None
    notes: str | None = None
    metadata: dict = Field(default={}, validation_alias="metadata_")

    model_config = {"from_attributes": True}
