"""Privacy and Cloud compliance checklist importer.

Scans extra_paths (isms-privacy and isms-cloud mounts) for:
  - generate_priv_checklist_*.py  → ProductType.PRIVACY
  - generate_cld_checklist_*.py   → ProductType.CLOUD

Extracts REQUIREMENTS via AST (same structure as operational) and upserts into:
  - assessments (type=checklist, product=privacy|cloud)
  - assessment_sheets (exec_summary + dashboard + one per domain)
  - assessment_items (one row per requirement, status=not_assessed)

No xlsx files needed — the Python scripts are the source of truth.
Change detection via SHA-256 of the script source.
"""

import ast
import hashlib
import logging
import re
import uuid
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import delete, select

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

# Matches folder names like priv-a.3.3-4-privacy-policy-and-roles or cld-a.1-general
# Captures the control ref: "a.3.3-4", "a.1", "a.12", etc.
# Pattern: a. followed by digit sequences separated by dots/hyphens, stopping at any letter
_FOLDER_RE = re.compile(r"^(?:priv|cld)-(a\.(?:\d+(?:[-\.]\d+)*))", re.IGNORECASE)


class PrivacyChecklistImporter(BaseImporter):
    """Imports PRIV and CLD compliance checklists from SCR generator scripts."""

    def __init__(self, db, extra_paths: list[str]):
        # Dummy framework_path (not used for scanning)
        super().__init__(db, "/tmp")
        self.extra_paths = [Path(p) for p in extra_paths if p]

    def import_all(self) -> dict:
        stats = {
            "assessments_imported": 0,
            "assessments_skipped": 0,
            "items_total": 0,
            "errors": 0,
            "error_details": [],
        }

        history = self._start_history("privacy_checklist_import")

        try:
            scripts = self._discover_scripts()
            logger.info(
                "Discovered %d privacy/cloud checklist scripts across %d paths",
                len(scripts),
                len(self.extra_paths),
            )

            for script_path, product_type in scripts:
                try:
                    self._import_single(script_path, product_type, stats)
                except Exception as e:
                    stats["errors"] += 1
                    stats["error_details"].append(
                        {"file": str(script_path), "error": str(e)[:200]}
                    )
                    logger.error("Failed to import %s: %s", script_path.name, e)

            self._finish_history(history, stats["assessments_imported"])
            logger.info("Privacy/Cloud checklist import complete: %s", stats)
        except Exception as e:
            self._fail_history(history, e)
            raise

        return stats

    # ------------------------------------------------------------------
    # Discovery
    # ------------------------------------------------------------------

    def _discover_scripts(self) -> list[tuple[Path, ProductType]]:
        """Find all priv/cld checklist generator scripts."""
        results = []
        for base in self.extra_paths:
            if not base.exists():
                logger.warning("Extra path does not exist: %s", base)
                continue
            for script in sorted(base.rglob("SCR/generate_priv_checklist_*.py")):
                results.append((script, ProductType.PRIVACY))
            for script in sorted(base.rglob("SCR/generate_cld_checklist_*.py")):
                results.append((script, ProductType.CLOUD))
        return results

    # ------------------------------------------------------------------
    # Single file import
    # ------------------------------------------------------------------

    def _import_single(self, script_path: Path, product_type: ProductType, stats: dict):
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

        # Map product type to product family for family-aware resolution
        preferred_family = (
            ProductFamily.PRIVACY if product_type == ProductType.PRIVACY else ProductFamily.CLOUD
        )
        group_id = self._resolve_group(script_path, control_id, preferred_family)
        if not group_id:
            raise ValueError(
                f"No control group found for control_id={control_id!r} "
                f"(doc_id={doc_id}, path={script_path})"
            )

        existing = self.db.execute(
            select(Assessment).where(Assessment.document_id == doc_id)
        ).scalar_one_or_none()

        if existing and existing.file_hash == content_hash:
            stats["assessments_skipped"] += 1
            logger.debug("Skip %s (unchanged)", doc_id)
            return

        items_total = sum(len(reqs) for reqs in requirements.values())
        domain_names = list(requirements.keys())
        sheets_count = len(domain_names) + 2
        workbook_name = f"{control_name} Compliance Checklist"

        if existing:
            existing.control_group_id = group_id
            existing.workbook_name = workbook_name
            existing.file_path = str(script_path)
            existing.file_hash = content_hash
            existing.items_total = items_total
            existing.sheets_count = sheets_count
            existing.last_parsed = datetime.now(timezone.utc)
            assessment = existing

            self.db.execute(
                delete(AssessmentItem).where(AssessmentItem.assessment_id == assessment.id)
            )
            self.db.execute(
                delete(AssessmentSheet).where(AssessmentSheet.assessment_id == assessment.id)
            )
            self.db.flush()
        else:
            assessment = Assessment(
                id=uuid.uuid4(),
                control_group_id=group_id,
                product_type=product_type,
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

        _create_sheets_and_items(self.db, assessment, group_id, requirements)

        stats["assessments_imported"] += 1
        stats["items_total"] += items_total

        logger.info(
            "Imported %s: %s (%d domains, %d items)",
            doc_id, control_name, len(domain_names), items_total,
        )

    # ------------------------------------------------------------------
    # Group resolution — handles priv-a.X and cld-a.X folder names
    # ------------------------------------------------------------------

    def _resolve_group(
        self,
        script_path: Path,
        control_id: str,
        preferred_family: ProductFamily | None = None,
    ) -> uuid.UUID | None:
        """Resolve control group from folder name first, then CONTROL_ID fallback."""
        # 1. Try folder name: priv-a.3.3-4-... or cld-a.1-...
        for part in script_path.parts:
            m = _FOLDER_RE.match(part.lower())
            if m:
                code = m.group(1)
                gid = self._resolve_control_group(code, preferred_family)
                if gid:
                    return gid

        # 2. Fallback: use CONTROL_ID, strip sub-control suffixes
        if control_id:
            # Handle slash-format: "A.8 / A.8.1" → take just the first part
            first_part = control_id.split("/")[0].strip()
            code = first_part.lower()
            gid = self._resolve_control_group(code, preferred_family)
            if gid:
                return gid
            # Strip everything after the second dot segment
            # a.10.1-3 → a.10 | a.12.1-2 → a.12
            m = re.match(r"(a\.\d+)\.", code)
            if m:
                gid = self._resolve_control_group(m.group(1), preferred_family)
                if gid:
                    return gid

        return None


# ------------------------------------------------------------------
# Sheet + item creation (same as operational_importer)
# ------------------------------------------------------------------

def _create_sheets_and_items(db, assessment: Assessment, group_id: uuid.UUID, requirements: OrderedDict):
    now = datetime.now(timezone.utc)

    for sheet_type, name in [
        (SheetType.EXECUTIVE_SUMMARY, "Executive Summary"),
        (SheetType.DASHBOARD, "Dashboard"),
    ]:
        db.add(AssessmentSheet(
            id=uuid.uuid4(),
            assessment_id=assessment.id,
            sheet_name=name,
            sheet_type=sheet_type,
            row_count=0,
            column_count=0,
            created_at=now,
        ))

    for domain_name, reqs in requirements.items():
        sheet = AssessmentSheet(
            id=uuid.uuid4(),
            assessment_id=assessment.id,
            sheet_name=domain_name[:50],
            sheet_type=SheetType.ASSESSMENT,
            row_count=len(reqs),
            column_count=8,
            created_at=now,
        )
        db.add(sheet)
        db.flush()

        for row_num, req_tuple in enumerate(reqs, start=1):
            req_id, section, req_text = req_tuple
            db.add(AssessmentItem(
                id=uuid.uuid4(),
                sheet_id=sheet.id,
                assessment_id=assessment.id,
                control_group_id=group_id,
                row_number=row_num,
                item_text=req_text,
                status=ComplianceStatus.NOT_ASSESSED,
                metadata_={"req_id": req_id, "section": section},
            ))


# ------------------------------------------------------------------
# AST extraction (identical to operational_importer)
# ------------------------------------------------------------------

def _extract_constants(source: str) -> dict:
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
    result = OrderedDict()

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
