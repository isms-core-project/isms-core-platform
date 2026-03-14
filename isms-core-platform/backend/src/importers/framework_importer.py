"""Framework workbook importer.

Scans the Framework mount for the 188 active SCR generator scripts
(*/SCR/generate_*.py, excluding SCR_ORG/ and SCR_N/), extracts workbook
structure via regex/AST, and upserts into:
  - assessments (type=detailed, product=framework)
  - assessment_sheets (one per sheet name extracted from generator)

AssessmentItems are NOT imported here — the framework workbooks are
heterogeneous (inventories, gap registers, config baselines, etc.).
Items are populated via WebUI data entry (Phase 6).

Change detection via SHA-256 of the generator script source.
"""

import hashlib
import logging
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import delete, func, select

from src.database.enums import (
    AssessmentType,
    ProductFamily,
    ProductType,
    SheetType,
)
from src.domain.assessments import Assessment, AssessmentSheet
from src.domain.control_groups import ControlGroup
from src.importers.base_importer import BaseImporter

logger = logging.getLogger(__name__)

# Sheet name → SheetType classification keywords
_DASHBOARD_NAMES = {"summary dashboard", "dashboard", "overview dashboard"}
_REFERENCE_NAMES = {
    "instructions & legend", "instructions and legend",
    "instructions", "legend", "approval sign-off", "approval sign off",
    "acceptance sign-off", "acceptance sign off",
    "change log", "reference",
}
_CONFIG_NAMES = {"action plan", "action items", "config", "settings"}


def _classify_sheet(name: str) -> SheetType:
    """Classify a sheet by its name."""
    lower = name.lower().strip()
    if lower in _DASHBOARD_NAMES:
        return SheetType.DASHBOARD
    if lower in _REFERENCE_NAMES:
        return SheetType.REFERENCE
    if lower in _CONFIG_NAMES:
        return SheetType.CONFIG
    return SheetType.ASSESSMENT


class FrameworkWorkbookImporter(BaseImporter):
    """Imports framework workbook structure from the 188 SCR generator scripts."""

    def __init__(self, db, framework_path: str):
        super().__init__(db, framework_path)

    def import_all(self) -> dict:
        """Scan Framework mount for generator scripts. Returns stats."""
        stats = {
            "assessments_imported": 0,
            "assessments_skipped": 0,
            "sheets_total": 0,
            "errors": 0,
            "error_details": [],
        }

        history = self._start_history("framework_workbook_import")

        try:
            isms_count = self.db.scalar(
                select(func.count(ControlGroup.id)).where(
                    ControlGroup.product_family == ProductFamily.ISMS
                )
            ) or 0
            if isms_count == 0:
                raise RuntimeError(
                    "ISMS control groups have not been seeded. "
                    "Run /admin/load before importing framework workbooks."
                )

            scripts = self._discover_scripts()
            logger.info(
                "Discovered %d framework generator scripts (path=%s)",
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
            logger.info("Framework workbook import complete: %s", stats)
        except Exception as e:
            self._fail_history(history, e)
            raise

        return stats

    # ------------------------------------------------------------------
    # Discovery
    # ------------------------------------------------------------------

    def _discover_scripts(self) -> list[Path]:
        """Find all active generator scripts (exclude SCR_ORG/ and SCR_N/).

        Covers:
        - Standard A.*/isms-*/SCR/generate_*.py (188 control generators)
        - Foundation 00-foundation-policies/*/SCR/ISMS-SCR-CHK-*.py
        """
        if not self.framework_path.exists():
            logger.warning("Framework path does not exist: %s", self.framework_path)
            return []
        scripts = set()
        for s in self.framework_path.rglob("SCR/generate_*.py"):
            if "SCR_ORG" not in s.parts and "SCR_N" not in s.parts:
                scripts.add(s)
        for s in self.framework_path.rglob("00-foundation-policies/*/SCR/ISMS-SCR-CHK-*.py"):
            scripts.add(s)
        return sorted(scripts)

    # ------------------------------------------------------------------
    # Single file import
    # ------------------------------------------------------------------

    def _import_single(self, script_path: Path, stats: dict):
        """Parse one generator script and upsert assessment + sheets."""
        source = script_path.read_text(encoding="utf-8", errors="replace")
        content_hash = hashlib.sha256(source.encode()).hexdigest()

        constants = _extract_constants(source)
        doc_id = constants.get("DOCUMENT_ID")
        control_id = constants.get("CONTROL_ID", "")
        workbook_name = constants.get("WORKBOOK_NAME", "")

        if not doc_id:
            raise ValueError("DOCUMENT_ID not found in script")

        # Resolve control group — strip any " & A.X.X" suffix first
        # Always prefer ISMS groups for framework workbooks
        group_code = re.sub(r"\s*&.*$", "", control_id).strip().lower()
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

        # Change detection
        existing = self.db.execute(
            select(Assessment).where(Assessment.document_id == doc_id)
        ).scalar_one_or_none()

        if existing and existing.file_hash == content_hash:
            stats["assessments_skipped"] += 1
            logger.debug("Skip %s (unchanged)", doc_id)
            return

        sheet_names = _extract_sheet_names(source)
        sheets_count = len(sheet_names)

        if existing:
            existing.control_group_id = group_id
            existing.workbook_name = workbook_name
            existing.file_path = str(script_path)
            existing.file_hash = content_hash
            existing.sheets_count = sheets_count
            existing.last_parsed = datetime.now(timezone.utc)
            assessment = existing

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
                product_type=ProductType.FRAMEWORK,
                assessment_type=AssessmentType.DETAILED,
                document_id=doc_id,
                workbook_name=workbook_name,
                file_path=str(script_path),
                file_hash=content_hash,
                sheets_count=sheets_count,
                last_parsed=datetime.now(timezone.utc),
                summary={},
            )
            self.db.add(assessment)
            self.db.flush()

        _create_sheets(self.db, assessment, sheet_names)

        stats["assessments_imported"] += 1
        stats["sheets_total"] += sheets_count

        logger.info(
            "Imported %s: %s (%d sheets)",
            doc_id,
            workbook_name,
            sheets_count,
        )


# ------------------------------------------------------------------
# Sheet creation
# ------------------------------------------------------------------

def _create_sheets(db, assessment: Assessment, sheet_names: list[str]):
    """Create AssessmentSheet records for one assessment."""
    now = datetime.now(timezone.utc)
    for name in sheet_names:
        sheet = AssessmentSheet(
            id=uuid.uuid4(),
            assessment_id=assessment.id,
            sheet_name=name[:50],
            sheet_type=_classify_sheet(name),
            created_at=now,
        )
        db.add(sheet)


# ------------------------------------------------------------------
# Extraction helpers
# ------------------------------------------------------------------

_CONST_RE = re.compile(
    r'^(DOCUMENT_ID|WORKBOOK_NAME|CONTROL_ID|CONTROL_NAME|POLICY_ID|POLICY_NAME)\s*=\s*"([^"]+)"',
    re.MULTILINE,
)


def _extract_constants(source: str) -> dict:
    """Extract DOCUMENT_ID, WORKBOOK_NAME, CONTROL_ID/POLICY_ID, CONTROL_NAME."""
    constants = {m.group(1): m.group(2) for m in _CONST_RE.finditer(source)}
    # Normalise: POLICY_ID → CONTROL_ID fallback for foundation scripts
    if "CONTROL_ID" not in constants and "POLICY_ID" in constants:
        constants["CONTROL_ID"] = constants["POLICY_ID"]
    return constants


def _extract_sheet_names(source: str) -> list[str]:
    """Extract all sheet names using 3-pattern combined approach.

    Pattern 1: ws.title = "Name"
    Pattern 2: wb.create_sheet("Name") or wb.create_sheet(title="Name")
    Pattern 3: for name in ["Name1", "Name2", ...]: followed by wb.create_sheet
    """
    seen: set[str] = set()
    names: list[str] = []

    def _add(name: str):
        if name and name not in seen:
            seen.add(name)
            names.append(name)

    # Pattern 1: ws.title = "literal"
    for m in re.finditer(r'ws\.title\s*=\s*"([^"]+)"', source):
        _add(m.group(1))

    # Pattern 2: wb.create_sheet("literal") or wb.create_sheet(title="literal")
    for m in re.finditer(r'wb\.create_sheet\(\s*(?:title=)?"([^"]+)"', source):
        _add(m.group(1))

    # Pattern 3: inline list in for loop before wb.create_sheet
    for m in re.finditer(
        r'for \w+ in \[([^\]]+)\]:\s*\n\s*\w+\.create_sheet',
        source,
        re.MULTILINE,
    ):
        for nm in re.finditer(r'"([^"]+)"', m.group(1)):
            _add(nm.group(1))

    return names
