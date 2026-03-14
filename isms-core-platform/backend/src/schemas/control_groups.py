import uuid
from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class ControlGroupList(BaseModel):
    id: uuid.UUID
    group_code: str
    name: str
    section: str
    section_name: str
    is_stacked: bool
    has_framework: bool
    has_operational: bool
    framework_status: str
    operational_status: str
    product_family: str = "ISMS"

    model_config = {"from_attributes": True}


class ControlGroupDetail(ControlGroupList):
    folder_name: str
    stacked_control_ids: list[str] = []
    metadata: dict = Field(default={}, validation_alias="metadata_")

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Rich detail sub-schemas (Task 3.6)
# ---------------------------------------------------------------------------

class PolicySummary(BaseModel):
    id: uuid.UUID
    document_id: str
    title: str
    policy_type: str
    product_type: str
    requirements_count: int = 0
    word_count: int | None = None
    last_parsed: datetime | None = None

    model_config = {"from_attributes": True}


class ImplSummary(BaseModel):
    id: uuid.UUID
    document_id: str
    title: str
    impl_type: str
    word_count: int | None = None
    last_parsed: datetime | None = None

    model_config = {"from_attributes": True}


class AssessmentItemSummary(BaseModel):
    id: str
    row_number: int
    item_text: str | None = None
    status: str = "not_assessed"
    owner: str | None = None
    due_date: str | None = None
    notes: str | None = None

    model_config = {"from_attributes": True}


class SheetSummary(BaseModel):
    id: str
    sheet_name: str
    sheet_type: str
    row_count: int = 0
    items: list[AssessmentItemSummary] = []

    model_config = {"from_attributes": True}


class AssessmentSummary(BaseModel):
    id: str
    document_id: str
    workbook_name: str
    product_type: str
    assessment_type: str
    sheets_count: int = 0
    overall_score: Decimal | None = None
    items_total: int = 0
    items_compliant: int = 0
    items_partial: int = 0
    items_non_compliant: int = 0
    items_na: int = 0
    sheets: list[SheetSummary] = []

    model_config = {"from_attributes": True}


class ExternalMappingEntry(BaseModel):
    framework: str
    framework_code: str
    control_id: str
    control_title: str
    mapping_type: str
    confidence: float = 0.85


class IsoControlSummary(BaseModel):
    control_id: str
    title: str
    description: str | None = None
    mappings: list[ExternalMappingEntry] = []


class GapItem(BaseModel):
    id: uuid.UUID
    description: str
    severity: str
    status: str
    owner: str | None = None
    due_date: date | None = None
    product_type: str

    model_config = {"from_attributes": True}


class EvidenceItem(BaseModel):
    id: uuid.UUID
    title: str
    evidence_type: str
    collected_date: date | None = None
    verified_by: str | None = None

    model_config = {"from_attributes": True}


class ControlGroupRichDetail(ControlGroupDetail):
    """Full per-control deep view: policies, implementations, assessments,
    ISO framework links, cross-framework mappings, gaps, evidence."""

    # Content artefacts
    policies: list[PolicySummary] = []
    implementations: list[ImplSummary] = []
    assessments: list[AssessmentSummary] = []

    # Framework linkage
    iso_controls: list[IsoControlSummary] = []

    # Compliance data
    gaps: list[GapItem] = []
    evidence: list[EvidenceItem] = []

    # Summary counts
    requirements_total: int = 0
    gaps_open: int = 0
    evidence_total: int = 0
