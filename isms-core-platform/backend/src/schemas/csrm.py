import uuid
from datetime import datetime

from pydantic import BaseModel


class ProtectionObjectCreate(BaseModel):
    name: str
    description: str | None = None
    architecture_notes: str | None = None
    processes_served: str | None = None
    data_classification: str | None = "standard"
    protection_level: str = "standard"
    elevated_rationale: str | None = None
    sort_order: int = 0


class ProtectionObjectPatch(BaseModel):
    name: str | None = None
    description: str | None = None
    architecture_notes: str | None = None
    processes_served: str | None = None
    data_classification: str | None = None
    protection_level: str | None = None
    elevated_rationale: str | None = None
    sort_order: int | None = None


class BaselineRatingUpsert(BaseModel):
    requirement_id: str
    status: str
    exception_justification: str | None = None
    notes: str | None = None


class BaselineRatingRead(BaseModel):
    id: uuid.UUID
    object_id: uuid.UUID
    requirement_id: str
    status: str
    exception_justification: str | None
    notes: str | None
    updated_at: datetime
    model_config = {"from_attributes": True}


class ElevatedTomCreate(BaseModel):
    threat_category: str
    tom_description: str
    status: str = "planned"
    notes: str | None = None


class ElevatedTomPatch(BaseModel):
    threat_category: str | None = None
    tom_description: str | None = None
    status: str | None = None
    notes: str | None = None


class ElevatedTomRead(BaseModel):
    id: uuid.UUID
    object_id: uuid.UUID
    threat_category: str
    tom_description: str
    status: str
    notes: str | None
    created_at: datetime
    updated_at: datetime
    model_config = {"from_attributes": True}


class ProtectionObjectRead(BaseModel):
    id: uuid.UUID
    assessment_id: uuid.UUID
    name: str
    description: str | None
    architecture_notes: str | None
    processes_served: str | None
    data_classification: str | None
    protection_level: str
    elevated_rationale: str | None
    sort_order: int
    created_at: datetime
    updated_at: datetime
    baseline_ratings: list[BaselineRatingRead] = []
    elevated_toms: list[ElevatedTomRead] = []
    model_config = {"from_attributes": True}


class CsrmAssessmentCreate(BaseModel):
    name: str
    description: str | None = None
    organisation: str | None = None
    assessor: str | None = None
    scope: str | None = None


class CsrmAssessmentPatch(BaseModel):
    name: str | None = None
    description: str | None = None
    organisation: str | None = None
    assessor: str | None = None
    scope: str | None = None
    status: str | None = None


class CsrmAssessmentRead(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None
    organisation: str | None
    assessor: str | None
    scope: str | None
    status: str
    created_at: datetime
    updated_at: datetime
    model_config = {"from_attributes": True}


class CsrmAssessmentDetail(CsrmAssessmentRead):
    objects: list[ProtectionObjectRead] = []


class CsrmAssessmentSummary(CsrmAssessmentRead):
    objects_count: int = 0
    elevated_count: int = 0
    baseline_met_pct: float | None = None
    objects_fully_assessed: int = 0
