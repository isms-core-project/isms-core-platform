"""Operational checklist importer.

Scans the Operational mount for generate_op_checklist_*.py scripts,
extracts REQUIREMENTS via AST, and upserts into:
  - assessments (type=checklist, product=operational)
  - assessment_sheets (exec_summary + dashboard + one per domain)
  - assessment_items (one row per requirement, status=not_assessed)

No xlsx files needed — the Python scripts are the source of truth.
Change detection via SHA-256 of the script source.
"""

import ast
import hashlib
import logging
import uuid
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import delete, func, select

from src.database.enums import (
    AssessmentType,
    ComplianceStatus,
    ProductFamily,
    ProductType,
    SheetType,
)
from src.domain.assessments import Assessment, AssessmentItem, AssessmentSheet
from src.domain.control_groups import ControlGroup
from src.importers.base_importer import BaseImporter

logger = logging.getLogger(__name__)


class OperationalChecklistImporter(BaseImporter):
    """Imports operational compliance checklists from SCR generator scripts."""

    def __init__(self, db, operational_path: str):
        # BaseImporter stores this as framework_path — we repurpose it
        super().__init__(db, operational_path)

    def import_all(self) -> dict:
        """Scan operational mount for checklist scripts. Returns stats."""
        stats = {
            "assessments_imported": 0,
            "assessments_skipped": 0,
            "items_total": 0,
            "errors": 0,
            "error_details": [],
        }

        history = self._start_history("operational_checklist_import")

        try:
            isms_count = self.db.scalar(
                select(func.count(ControlGroup.id)).where(
                    ControlGroup.product_family == ProductFamily.ISMS
                )
            ) or 0
            if isms_count == 0:
                raise RuntimeError(
                    "ISMS control groups have not been seeded. "
                    "Run /admin/load before importing operational checklists."
                )

            scripts = self._discover_scripts()
            logger.info(
                "Discovered %d operational checklist scripts (path=%s)",
                len(scripts),
                self.framework_path,
            )

            for script_path in scripts:
                try:
                    self._import_single(script_path, stats)
                except Exception as e:
                    stats["errors"] += 1
                    stats["error_details"].append(
                        {"file": str(script_path), "error": str(e)[:200]}
                    )
                    logger.error(
                        "Failed to import %s: %s", script_path.name, e
                    )

            self._finish_history(history, stats["assessments_imported"])
            logger.info("Operational import complete: %s", stats)
        except Exception as e:
            self._fail_history(history, e)
            raise

        return stats

    # ------------------------------------------------------------------
    # Discovery
    # ------------------------------------------------------------------

    def _discover_scripts(self) -> list[Path]:
        """Find all generate_op_checklist_*.py scripts in the operational mount."""
        if not self.framework_path.exists():
            logger.warning("Operational path does not exist: %s", self.framework_path)
            return []
        return sorted(self.framework_path.rglob("SCR/generate_op_checklist_*.py"))

    # ------------------------------------------------------------------
    # Single file import
    # ------------------------------------------------------------------

    def _import_single(self, script_path: Path, stats: dict):
        """Parse one generator script and upsert assessment + sheets + items."""
        source = script_path.read_text(encoding="utf-8")
        content_hash = hashlib.sha256(source.encode()).hexdigest()

        constants = _extract_constants(source)
        doc_id = constants.get("DOCUMENT_ID")
        control_id = constants.get("CONTROL_ID", "")
        control_name = constants.get("CONTROL_NAME", "")
        requirements: OrderedDict = constants.get("REQUIREMENTS", OrderedDict())

        if not doc_id:
            raise ValueError("DOCUMENT_ID not found in script")
        if not requirements:
            raise ValueError("REQUIREMENTS not found or empty in script")

        # Resolve control group — always ISMS for operational checklists
        group_code = control_id.lower()
        group_id = self._resolve_control_group(group_code, ProductFamily.ISMS)
        if not group_id:
            folder_code = self._group_code_from_path(script_path)
            if folder_code:
                group_id = self._resolve_control_group(folder_code, ProductFamily.ISMS)
        if not group_id:
            raise ValueError(
                f"No control group found for control_id={control_id!r} "
                f"(doc_id={doc_id})"
            )

        # Check for unchanged content
        existing = self.db.execute(
            select(Assessment).where(Assessment.document_id == doc_id)
        ).scalar_one_or_none()

        if existing and existing.file_hash == content_hash:
            stats["assessments_skipped"] += 1
            logger.debug("Skip %s (unchanged)", doc_id)
            return

        items_total = sum(len(reqs) for reqs in requirements.values())
        domain_names = list(requirements.keys())
        sheets_count = len(domain_names) + 2  # + executive_summary + dashboard
        workbook_name = f"{control_name} Compliance Checklist"

        if existing:
            # Update existing assessment metadata
            existing.control_group_id = group_id
            existing.workbook_name = workbook_name
            existing.file_path = str(script_path)
            existing.file_hash = content_hash
            existing.items_total = items_total
            existing.sheets_count = sheets_count
            existing.last_parsed = datetime.now(timezone.utc)
            assessment = existing

            # Clear existing sheets and items before recreating
            self.db.execute(
                delete(AssessmentItem).where(
                    AssessmentItem.assessment_id == assessment.id
                )
            )
            self.db.execute(
                delete(AssessmentSheet).where(
                    AssessmentSheet.assessment_id == assessment.id
                )
            )
            self.db.flush()
        else:
            assessment = Assessment(
                id=uuid.uuid4(),
                control_group_id=group_id,
                product_type=ProductType.OPERATIONAL,
                assessment_type=AssessmentType.CHECKLIST,
                document_id=doc_id,
                workbook_name=workbook_name,
                file_path=str(script_path),
                file_hash=content_hash,
                items_total=items_total,
                sheets_count=sheets_count,
                last_parsed=datetime.now(timezone.utc),
                summary={},
            )
            self.db.add(assessment)
            self.db.flush()

        # Create sheets and items
        _create_sheets_and_items(self.db, assessment, group_id, requirements)

        stats["assessments_imported"] += 1
        stats["items_total"] += items_total

        logger.info(
            "Imported %s: %s (%d domains, %d items)",
            doc_id,
            control_name,
            len(domain_names),
            items_total,
        )


# ------------------------------------------------------------------
# Sheet + item creation
# ------------------------------------------------------------------

def _create_sheets_and_items(
    db,
    assessment: Assessment,
    group_id: uuid.UUID,
    requirements: OrderedDict,
):
    """Create AssessmentSheet and AssessmentItem records for one assessment."""
    now = datetime.now(timezone.utc)

    # Fixed structural sheets (no items)
    for sheet_type, name in [
        (SheetType.EXECUTIVE_SUMMARY, "Executive Summary"),
        (SheetType.DASHBOARD, "Dashboard"),
    ]:
        sheet = AssessmentSheet(
            id=uuid.uuid4(),
            assessment_id=assessment.id,
            sheet_name=name,
            sheet_type=sheet_type,
            row_count=0,
            column_count=0,
            created_at=now,
        )
        db.add(sheet)

    # Domain assessment sheets + items
    for domain_name, reqs in requirements.items():
        sheet = AssessmentSheet(
            id=uuid.uuid4(),
            assessment_id=assessment.id,
            sheet_name=domain_name[:50],
            sheet_type=SheetType.ASSESSMENT,
            row_count=len(reqs),
            column_count=8,  # Req# | Section | Requirement | Status | Evidence | Owner | Due | Notes
            created_at=now,
        )
        db.add(sheet)
        db.flush()

        for row_num, req_tuple in enumerate(reqs, start=1):
            req_id, section, req_text = req_tuple
            item = AssessmentItem(
                id=uuid.uuid4(),
                sheet_id=sheet.id,
                assessment_id=assessment.id,
                control_group_id=group_id,
                row_number=row_num,
                item_text=req_text,
                status=ComplianceStatus.NOT_ASSESSED,
                metadata_={"req_id": req_id, "section": section},
            )
            db.add(item)


# ------------------------------------------------------------------
# AST extraction helpers
# ------------------------------------------------------------------

def _extract_constants(source: str) -> dict:
    """Extract DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, REQUIREMENTS from source."""
    tree = ast.parse(source)
    result = {}

    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if not isinstance(target, ast.Name):
                continue
            name = target.id
            if name in ("DOCUMENT_ID", "CONTROL_ID", "CONTROL_NAME", "SOURCE_POLICY"):
                try:
                    result[name] = ast.literal_eval(node.value)
                except (ValueError, TypeError):
                    pass
            elif name == "REQUIREMENTS":
                result[name] = _extract_requirements_node(node.value)

    return result


def _extract_requirements_node(node: ast.AST) -> OrderedDict:
    """Extract REQUIREMENTS OrderedDict from its AST Call node."""
    result = OrderedDict()

    # REQUIREMENTS = OrderedDict([...])
    if not isinstance(node, ast.Call):
        return result
    if not node.args:
        return result

    list_node = node.args[0]
    if not isinstance(list_node, ast.List):
        return result

    for domain_tuple in list_node.elts:
        if not isinstance(domain_tuple, ast.Tuple) or len(domain_tuple.elts) != 2:
            continue
        try:
            domain_name = ast.literal_eval(domain_tuple.elts[0])
        except (ValueError, TypeError):
            continue

        req_list_node = domain_tuple.elts[1]
        if not isinstance(req_list_node, ast.List):
            continue

        reqs = []
        for req_node in req_list_node.elts:
            if not isinstance(req_node, ast.Tuple) or len(req_node.elts) != 3:
                continue
            try:
                req_id = ast.literal_eval(req_node.elts[0])
                section = ast.literal_eval(req_node.elts[1])
                req_text = ast.literal_eval(req_node.elts[2])
                reqs.append((req_id, section, req_text))
            except (ValueError, TypeError):
                continue

        result[domain_name] = reqs

    return result
