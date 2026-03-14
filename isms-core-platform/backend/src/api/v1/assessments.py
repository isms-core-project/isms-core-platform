import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.domain.assessments import Assessment, AssessmentItem, AssessmentSheet
from src.domain.users import User
from src.schemas.assessments import (
    AssessmentCreate,
    AssessmentItemPatch,
    AssessmentItemRead,
    AssessmentListRead,
    AssessmentRead,
    AssessmentRowCreate,
    AssessmentRowUpdate,
    AssessmentSheetRead,
)
from src.services.assessment_service import (
    add_assessment_row,
    create_platform_assessment,
    delete_assessment_row,
    get_assessment,
    list_assessments,
    update_assessment_row,
    update_item_status,
)

router = APIRouter(prefix="/assessments", tags=["assessments"])


@router.get("/", response_model=list[AssessmentListRead])
def list_all_assessments(
    product: str | None = None,
    product_family: str | None = None,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    return list_assessments(db, product=product, product_family=product_family)


@router.post("/", response_model=AssessmentRead, status_code=201)
def create_assessment(
    body: AssessmentCreate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Create a new platform (WebUI) assessment for a control group."""
    try:
        assessment = create_platform_assessment(
            db,
            group_code=body.group_code,
            product_type=body.product_type,
            workbook_name=body.workbook_name,
            sheet_names=[],
            label=body.label,
            assessor=body.assessor,
            scope=body.scope,
            purpose=body.purpose,
            target_date=body.target_date,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return assessment


@router.get("/{assessment_id}/sheets", response_model=list[AssessmentSheetRead])
def list_assessment_sheets(
    assessment_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Return all sheets with their items for an assessment."""
    sheets = db.execute(
        select(AssessmentSheet)
        .where(AssessmentSheet.assessment_id == assessment_id)
        .order_by(AssessmentSheet.sheet_name)
    ).scalars().all()
    result = []
    for sheet in sheets:
        items = db.execute(
            select(AssessmentItem)
            .where(AssessmentItem.sheet_id == sheet.id)
            .order_by(AssessmentItem.row_number)
        ).scalars().all()
        result.append(AssessmentSheetRead(
            id=sheet.id,
            sheet_name=sheet.sheet_name,
            sheet_type=sheet.sheet_type.value if hasattr(sheet.sheet_type, "value") else sheet.sheet_type,
            row_count=sheet.row_count or 0,
            items=[AssessmentItemRead.from_orm_item(i) for i in items],
        ))
    return result


@router.post("/{assessment_id}/rows", response_model=AssessmentItemRead, status_code=201)
def add_row(
    assessment_id: uuid.UUID,
    body: AssessmentRowCreate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    try:
        item = add_assessment_row(
            db,
            assessment_id=assessment_id,
            sheet_name=body.sheet_name,
            row_number=body.row_number,
            item_text=body.item_text,
            status_dv=body.status,
            evidence_reference=body.evidence_reference,
            notes=body.notes,
            col_data=body.col_data,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return AssessmentItemRead.from_orm_item(item)


@router.patch("/items/{item_id}", response_model=AssessmentItemRead)
def patch_item(
    item_id: uuid.UUID,
    body: AssessmentRowUpdate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    item = update_assessment_row(
        db,
        item_id=item_id,
        item_text=body.item_text,
        status_dv=body.status,
        evidence_reference=body.evidence_reference,
        notes=body.notes,
        col_data=body.col_data,
    )
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return AssessmentItemRead.from_orm_item(item)


@router.delete("/items/{item_id}", status_code=204)
def delete_item(
    item_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    if not delete_assessment_row(db, item_id):
        raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/{assessment_id}", status_code=204)
def delete_assessment(
    assessment_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Delete a platform (WebUI) assessment. Only platform:webui assessments may be deleted."""
    a = db.get(Assessment, assessment_id)
    if not a:
        raise HTTPException(status_code=404, detail="Assessment not found")
    if a.file_path != "platform:webui":
        raise HTTPException(status_code=403, detail="Only platform assessments can be deleted via the UI")
    db.delete(a)
    db.commit()


@router.get("/{assessment_id}", response_model=AssessmentRead)
def get_one_assessment(
    assessment_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    a = get_assessment(db, assessment_id)
    if not a:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return a
