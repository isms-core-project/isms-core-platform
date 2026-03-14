import re
import uuid
from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.database.enums import AssessmentType, ComplianceStatus, ProductFamily, ProductType, SheetType
from src.domain.assessments import Assessment, AssessmentItem, AssessmentSheet
from src.domain.control_groups import ControlGroup
from src.schemas.assessments import AssessmentListRead, AssessmentRead


def list_assessments(
    db: DBSession,
    product: str | None = None,
    product_family: str | None = None,
) -> list[AssessmentListRead]:
    stmt = (
        select(Assessment, ControlGroup.group_code, ControlGroup.name)
        .join(ControlGroup, Assessment.control_group_id == ControlGroup.id)
        .order_by(Assessment.document_id)
    )
    if product:
        stmt = stmt.where(Assessment.product_type == product)
    if product_family:
        try:
            stmt = stmt.where(ControlGroup.product_family == ProductFamily(product_family.upper()))
        except ValueError:
            pass
    rows = db.execute(stmt).all()
    result = []
    for assessment, group_code, group_name in rows:
        base = AssessmentListRead.model_validate(assessment)
        result.append(base.model_copy(update={"group_code": group_code, "group_name": group_name}))
    return result


def get_assessment(db: DBSession, assessment_id: uuid.UUID) -> Assessment | None:
    return db.get(Assessment, assessment_id)


def update_item_status(
    db: DBSession, item_id: uuid.UUID, status: str
) -> AssessmentItem | None:
    item = db.get(AssessmentItem, item_id)
    if not item:
        return None
    item.status = ComplianceStatus(status)
    db.commit()
    db.refresh(item)
    return item


# ── DV value → ComplianceStatus mapping ──────────────────────────────────────

def _dv_to_status(dv_value: str) -> ComplianceStatus:
    v = dv_value.lower().strip()
    if any(x in v for x in ["compliant", "yes", "implemented", "verified", "complete", "active", "approved", "pass"]):
        return ComplianceStatus.COMPLIANT
    if any(x in v for x in ["partial", "planned", "in progress", "pending"]):
        return ComplianceStatus.PARTIAL
    if any(x in v for x in ["no", "open", "not implemented", "not verified", "rejected", "fail", "non-compliant"]):
        return ComplianceStatus.NON_COMPLIANT
    if any(x in v for x in ["n/a", "not applicable", "na", "not relevant"]):
        return ComplianceStatus.NA
    return ComplianceStatus.NOT_ASSESSED


# ── Assessment create (from WebUI schema) ─────────────────────────────────────

def create_platform_assessment(
    db: DBSession,
    group_code: str,
    product_type: str,
    workbook_name: str,
    sheet_names: list[str],
    label: str = "",
    assessor: str = "",
    scope: str = "",
    purpose: str = "",
    target_date: str = "",
) -> Assessment:
    """Create a new platform-originated assessment (no file, from WebUI form)."""
    group = db.execute(
        select(ControlGroup).where(ControlGroup.group_code == group_code.lower())
    ).scalar_one_or_none()
    if not group:
        raise ValueError(f"Control group not found: {group_code}")

    ts = datetime.now(timezone.utc)
    if label:
        slug = re.sub(r"[^a-zA-Z0-9-]", "-", label.strip())
        slug = re.sub(r"-+", "-", slug).strip("-")[:20]
        doc_id = f"ISMS-ASS-{group_code.upper()}_{slug}_{ts.strftime('%Y%m%d')}"
    else:
        doc_id = f"ISMS-ASS-{group_code.upper()}-{ts.strftime('%Y%m%d%H%M%S')}"

    name = workbook_name or group.name
    summary: dict = {}
    if assessor:     summary["assessor"]    = assessor
    if scope:        summary["scope"]       = scope
    if purpose:      summary["purpose"]     = purpose
    if target_date:  summary["target_date"] = target_date

    assessment = Assessment(
        id=uuid.uuid4(),
        control_group_id=group.id,
        product_type=ProductType(product_type),
        assessment_type=AssessmentType.DETAILED,
        document_id=doc_id,
        workbook_name=name,
        file_path="platform:webui",
        sheets_count=len(sheet_names),
        last_generated=ts,
        summary=summary,
    )
    db.add(assessment)
    db.flush()

    for sheet_name in sheet_names:
        db.add(AssessmentSheet(
            id=uuid.uuid4(),
            assessment_id=assessment.id,
            sheet_name=sheet_name,
            sheet_type=SheetType.ASSESSMENT,
        ))
    db.commit()
    db.refresh(assessment)
    return assessment


def get_assessment_with_items(db: DBSession, assessment_id: uuid.UUID) -> Assessment | None:
    return db.get(Assessment, assessment_id)


def get_or_create_sheet(
    db: DBSession, assessment_id: uuid.UUID, sheet_name: str
) -> AssessmentSheet:
    sheet = db.execute(
        select(AssessmentSheet).where(
            AssessmentSheet.assessment_id == assessment_id,
            AssessmentSheet.sheet_name == sheet_name,
        )
    ).scalar_one_or_none()
    if not sheet:
        assessment = db.get(Assessment, assessment_id)
        sheet = AssessmentSheet(
            id=uuid.uuid4(),
            assessment_id=assessment_id,
            sheet_name=sheet_name,
            sheet_type=SheetType.ASSESSMENT,
        )
        db.add(sheet)
        db.flush()
    return sheet


def add_assessment_row(
    db: DBSession,
    assessment_id: uuid.UUID,
    sheet_name: str,
    row_number: int,
    item_text: str | None,
    status_dv: str,
    evidence_reference: str | None,
    notes: str | None,
    col_data: dict,
) -> AssessmentItem:
    assessment = db.get(Assessment, assessment_id)
    if not assessment:
        raise ValueError(f"Assessment not found: {assessment_id}")

    sheet = get_or_create_sheet(db, assessment_id, sheet_name)
    status = _dv_to_status(status_dv) if status_dv else ComplianceStatus.NOT_ASSESSED

    item = AssessmentItem(
        id=uuid.uuid4(),
        sheet_id=sheet.id,
        assessment_id=assessment_id,
        control_group_id=assessment.control_group_id,
        row_number=row_number,
        item_text=item_text,
        status=status,
        evidence_reference=evidence_reference,
        notes=notes,
        metadata_=col_data,
    )
    db.add(item)

    # Update sheet row count
    sheet.row_count = (sheet.row_count or 0) + 1

    # Recompute assessment totals
    _recompute_totals(db, assessment, flush=True)
    db.commit()
    db.refresh(item)
    return item


def update_assessment_row(
    db: DBSession,
    item_id: uuid.UUID,
    item_text: str | None,
    status_dv: str | None,
    evidence_reference: str | None,
    notes: str | None,
    col_data: dict | None,
) -> AssessmentItem | None:
    item = db.get(AssessmentItem, item_id)
    if not item:
        return None
    if item_text is not None:
        item.item_text = item_text
    if status_dv is not None:
        item.status = _dv_to_status(status_dv)
    if evidence_reference is not None:
        item.evidence_reference = evidence_reference
    if notes is not None:
        item.notes = notes
    if col_data is not None:
        item.metadata_ = col_data
    assessment = db.get(Assessment, item.assessment_id)
    _recompute_totals(db, assessment, flush=False)
    db.commit()
    db.refresh(item)
    return item


def delete_assessment_row(db: DBSession, item_id: uuid.UUID) -> bool:
    item = db.get(AssessmentItem, item_id)
    if not item:
        return False
    assessment = db.get(Assessment, item.assessment_id)
    sheet = db.get(AssessmentSheet, item.sheet_id)
    db.delete(item)
    db.flush()
    if sheet:
        sheet.row_count = max(0, (sheet.row_count or 1) - 1)
    if assessment:
        _recompute_totals(db, assessment, flush=False)
    db.commit()
    return True


def _recompute_totals(db: DBSession, assessment: Assessment, flush: bool = False) -> None:
    """Recompute items_total, items_compliant, etc. and overall_score from current items."""
    from sqlalchemy import func as sa_func
    counts = db.execute(
        select(AssessmentItem.status, sa_func.count().label("n"))
        .where(AssessmentItem.assessment_id == assessment.id)
        .group_by(AssessmentItem.status)
    ).all()
    total = sum(c.n for c in counts)
    compliant = next((c.n for c in counts if c.status == ComplianceStatus.COMPLIANT), 0)
    partial = next((c.n for c in counts if c.status == ComplianceStatus.PARTIAL), 0)
    non_compliant = next((c.n for c in counts if c.status == ComplianceStatus.NON_COMPLIANT), 0)
    na = next((c.n for c in counts if c.status == ComplianceStatus.NA), 0)
    assessed = compliant + partial + non_compliant
    score = round((compliant + partial * 0.5) / assessed * 100, 2) if assessed else None

    assessment.items_total = total
    assessment.items_compliant = compliant
    assessment.items_partial = partial
    assessment.items_non_compliant = non_compliant
    assessment.items_na = na
    assessment.overall_score = score
    if flush:
        db.flush()
