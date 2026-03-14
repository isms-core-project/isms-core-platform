import uuid
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class AssessmentRead(BaseModel):
    id: uuid.UUID
    control_group_id: uuid.UUID
    product_type: str
    assessment_type: str
    document_id: str
    workbook_name: str
    file_path: str
    sheets_count: int | None = 0
    overall_score: Decimal | None = None
    items_total: int | None = 0
    items_compliant: int | None = 0
    items_partial: int | None = 0
    items_non_compliant: int | None = 0
    items_na: int | None = 0
    gaps_count: int | None = 0
    last_generated: datetime | None = None
    last_parsed: datetime | None = None
    summary: dict = {}

    model_config = {"from_attributes": True}


class AssessmentListRead(AssessmentRead):
    """AssessmentRead enriched with control group info for list views."""
    group_code: str = ""
    group_name: str = ""

    model_config = {"from_attributes": True}


class SheetRead(BaseModel):
    id: uuid.UUID
    assessment_id: uuid.UUID
    sheet_name: str
    sheet_type: str
    row_count: int | None = 0
    column_count: int | None = 0
    compliance_score: Decimal | None = None

    model_config = {"from_attributes": True}


class AssessmentCreate(BaseModel):
    group_code: str
    product_type: str = "framework"
    workbook_name: str = ""
    # Metadata — stored in summary JSONB
    label: str = ""        # slug appended to document_id
    assessor: str = ""     # lead assessor name / role
    scope: str = ""        # systems / departments in scope
    purpose: str = ""      # purpose / objective
    target_date: str = ""  # expected completion (YYYY-MM-DD)


class AssessmentRowCreate(BaseModel):
    sheet_name: str
    row_number: int
    item_text: str | None = None
    status: str = "not_assessed"
    evidence_reference: str | None = None
    notes: str | None = None
    col_data: dict = {}           # full column values keyed by header


class AssessmentRowUpdate(BaseModel):
    item_text: str | None = None
    status: str | None = None
    evidence_reference: str | None = None
    notes: str | None = None
    col_data: dict | None = None


class AssessmentItemPatch(BaseModel):
    status: str


class AssessmentItemRead(BaseModel):
    id: uuid.UUID
    sheet_id: uuid.UUID
    status: str
    row_number: int
    item_text: str | None = None
    evidence_reference: str | None = None
    owner: str | None = None
    notes: str | None = None
    col_data: dict = {}

    model_config = {"from_attributes": True}

    @classmethod
    def from_orm_item(cls, item) -> "AssessmentItemRead":
        return cls(
            id=item.id,
            sheet_id=item.sheet_id,
            status=item.status.value if hasattr(item.status, "value") else item.status,
            row_number=item.row_number,
            item_text=item.item_text,
            evidence_reference=item.evidence_reference,
            owner=item.owner,
            notes=item.notes,
            col_data=item.metadata_ or {},
        )


class AssessmentSheetRead(BaseModel):
    id: uuid.UUID
    sheet_name: str
    sheet_type: str
    row_count: int | None = 0
    items: list[AssessmentItemRead] = []

    model_config = {"from_attributes": True}
