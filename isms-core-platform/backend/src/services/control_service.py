import uuid

from sqlalchemy import func, select
from sqlalchemy.orm import Session as DBSession

from src.domain.assessments import Assessment, AssessmentItem, AssessmentSheet
from src.domain.compliance import Evidence, Gap
from src.domain.content import Implementation, Policy, Requirement
from src.domain.control_groups import ControlGroup, control_group_controls
from src.domain.frameworks import CrossFrameworkMapping, Framework, FrameworkControl


def list_control_groups(
    db: DBSession,
    section: str | None = None,
    product: str | None = None,
    product_family: str | None = None,
) -> list[ControlGroup]:
    stmt = select(ControlGroup).order_by(ControlGroup.group_code)

    if section:
        stmt = stmt.where(ControlGroup.section == section)
    if product_family:
        stmt = stmt.where(ControlGroup.product_family == product_family.upper())
    elif product == "framework":
        stmt = stmt.where(ControlGroup.has_framework.is_(True))
    elif product == "operational":
        stmt = stmt.where(ControlGroup.has_operational.is_(True))

    return db.execute(stmt).scalars().all()


def get_control_group(db: DBSession, group_id: uuid.UUID) -> ControlGroup | None:
    return db.get(ControlGroup, group_id)


def get_control_group_by_code(db: DBSession, group_code: str) -> ControlGroup | None:
    return db.execute(
        select(ControlGroup).where(ControlGroup.group_code == group_code.lower())
    ).scalar_one_or_none()


def get_control_group_rich(db: DBSession, cg: ControlGroup) -> dict:
    """Build rich detail dict for a control group — Task 3.6.

    Returns a dict compatible with ControlGroupRichDetail schema.
    """
    group_id = cg.id

    # Policies
    policies = db.execute(
        select(Policy)
        .where(Policy.control_group_id == group_id)
        .order_by(Policy.product_type, Policy.policy_type, Policy.document_id)
    ).scalars().all()

    # Implementations
    implementations = db.execute(
        select(Implementation)
        .where(Implementation.control_group_id == group_id)
        .order_by(Implementation.impl_type, Implementation.document_id)
    ).scalars().all()

    # Assessments + sheets
    assessments = db.execute(
        select(Assessment)
        .where(Assessment.control_group_id == group_id)
        .order_by(Assessment.product_type, Assessment.document_id)
    ).scalars().all()

    assessments_out = []
    for a in assessments:
        sheets = db.execute(
            select(AssessmentSheet)
            .where(AssessmentSheet.assessment_id == a.id)
            .order_by(AssessmentSheet.sheet_name)
        ).scalars().all()

        # Fetch all items for this assessment in one query, keyed by sheet_id
        items_by_sheet: dict[str, list] = {}
        all_items = db.execute(
            select(AssessmentItem)
            .where(AssessmentItem.assessment_id == a.id)
            .order_by(AssessmentItem.sheet_id, AssessmentItem.row_number)
        ).scalars().all()
        for item in all_items:
            key = str(item.sheet_id)
            if key not in items_by_sheet:
                items_by_sheet[key] = []
            items_by_sheet[key].append({
                "id": str(item.id),
                "row_number": item.row_number,
                "item_text": item.item_text,
                "status": item.status.value if hasattr(item.status, "value") else item.status,
                "owner": item.owner,
                "due_date": str(item.due_date) if item.due_date else None,
                "notes": item.notes,
            })

        assessments_out.append({
            "id": str(a.id),
            "document_id": a.document_id,
            "workbook_name": a.workbook_name,
            "file_path": a.file_path or "",
            "product_type": a.product_type.value if hasattr(a.product_type, "value") else a.product_type,
            "assessment_type": a.assessment_type.value if hasattr(a.assessment_type, "value") else a.assessment_type,
            "sheets_count": a.sheets_count or 0,
            "overall_score": a.overall_score,
            "items_total": a.items_total or 0,
            "items_compliant": a.items_compliant or 0,
            "items_partial": a.items_partial or 0,
            "items_non_compliant": a.items_non_compliant or 0,
            "items_na": a.items_na or 0,
            "sheets": [
                {
                    "id": str(s.id),
                    "sheet_name": s.sheet_name,
                    "sheet_type": s.sheet_type.value if hasattr(s.sheet_type, "value") else s.sheet_type,
                    "row_count": s.row_count or 0,
                    "items": items_by_sheet.get(str(s.id), []),
                }
                for s in sheets
            ],
        })

    # ISO 27001 framework controls via junction + their cross-framework mappings
    iso_fw = db.execute(
        select(Framework).where(Framework.code.ilike("ISO27001%"))
    ).scalar_one_or_none()

    iso_controls_out = []
    if iso_fw:
        iso_ctrl_rows = db.execute(
            select(FrameworkControl)
            .join(control_group_controls,
                  control_group_controls.c.framework_control_id == FrameworkControl.id)
            .where(
                control_group_controls.c.control_group_id == group_id,
                FrameworkControl.framework_id == iso_fw.id,
            )
            .order_by(FrameworkControl.sort_order)
        ).scalars().all()

        for ctrl in iso_ctrl_rows:
            mapping_rows = db.execute(
                select(
                    CrossFrameworkMapping.mapping_type,
                    CrossFrameworkMapping.confidence,
                    FrameworkControl.control_id.label("target_id"),
                    FrameworkControl.title.label("target_title"),
                    Framework.name.label("fw_name"),
                    Framework.code.label("fw_code"),
                )
                .join(FrameworkControl,
                      CrossFrameworkMapping.target_control_id == FrameworkControl.id)
                .join(Framework, FrameworkControl.framework_id == Framework.id)
                .where(CrossFrameworkMapping.source_control_id == ctrl.id)
                .order_by(Framework.name, FrameworkControl.control_id)
            ).all()

            iso_controls_out.append({
                "control_id": ctrl.control_id,
                "title": ctrl.title,
                "description": ctrl.description,
                "mappings": [
                    {
                        "framework": r.fw_name,
                        "framework_code": r.fw_code,
                        "control_id": r.target_id,
                        "control_title": r.target_title,
                        "mapping_type": r.mapping_type.value
                        if hasattr(r.mapping_type, "value") else str(r.mapping_type),
                        "confidence": float(r.confidence) if r.confidence else 0.85,
                    }
                    for r in mapping_rows
                ],
            })

    # Gaps
    gaps = db.execute(
        select(Gap)
        .where(Gap.control_group_id == group_id)
        .order_by(Gap.severity, Gap.created_at.desc())
    ).scalars().all()

    gaps_out = [
        {
            "id": g.id,
            "description": g.gap_description,
            "severity": g.severity.value if hasattr(g.severity, "value") else g.severity,
            "status": g.status.value if hasattr(g.status, "value") else g.status,
            "owner": g.owner,
            "due_date": g.due_date,
            "product_type": g.product_type,
        }
        for g in gaps
    ]

    # Evidence
    evidence = db.execute(
        select(Evidence)
        .where(Evidence.control_group_id == group_id)
        .order_by(Evidence.collected_date.desc())
    ).scalars().all()

    evidence_out = [
        {
            "id": e.id,
            "title": e.title,
            "evidence_type": e.evidence_type.value if hasattr(e.evidence_type, "value") else e.evidence_type,
            "collected_date": e.collected_date,
            "verified_by": e.verified_by,
        }
        for e in evidence
    ]

    # Requirements total
    req_total = db.scalar(
        select(func.count(Requirement.id))
        .where(Requirement.control_group_id == group_id)
    ) or 0

    gaps_open = sum(
        1 for g in gaps
        if (g.status.value if hasattr(g.status, "value") else g.status) == "open"
    )

    return {
        # Base fields (from ORM)
        "id": cg.id,
        "group_code": cg.group_code,
        "name": cg.name,
        "section": cg.section,
        "section_name": cg.section_name,
        "folder_name": cg.folder_name,
        "is_stacked": cg.is_stacked,
        "stacked_control_ids": cg.stacked_control_ids or [],
        "has_framework": cg.has_framework,
        "has_operational": cg.has_operational,
        "framework_status": cg.framework_status.value
        if hasattr(cg.framework_status, "value") else cg.framework_status,
        "operational_status": cg.operational_status.value
        if hasattr(cg.operational_status, "value") else cg.operational_status,
        "metadata_": cg.metadata_,
        # Rich fields
        "policies": list(policies),
        "implementations": list(implementations),
        "assessments": assessments_out,
        "iso_controls": iso_controls_out,
        "gaps": gaps_out,
        "evidence": evidence_out,
        "requirements_total": req_total,
        "gaps_open": gaps_open,
        "evidence_total": len(evidence),
    }
