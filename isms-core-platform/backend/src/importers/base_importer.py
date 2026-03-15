"""Shared base class for ISMS CORE importers.

Extracts common functionality: control group resolution, DataLoadHistory tracking,
parser setup, and group code from file path extraction.
"""

import logging
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.database.enums import ProductFamily
from src.domain.control_groups import ControlGroup
from src.domain.system import DataLoadHistory
from src.importers.parsers.base import BasePolicyParser
from src.importers.parsers.docx_parser import DocxPolicyParser
from src.importers.parsers.markdown_parser import MarkdownPolicyParser
from src.importers.parsers.pdf_parser import PdfPolicyParser

logger = logging.getLogger(__name__)


class BaseImporter:
    """Shared base class for PolicyImporter and ImpImporter."""

    def __init__(self, db: DBSession, framework_path: str):
        self.db = db
        self.framework_path = Path(framework_path)
        self.parsers: dict[str, BasePolicyParser] = {
            ".md": MarkdownPolicyParser(),
            ".pdf": PdfPolicyParser(),
            ".docx": DocxPolicyParser(),
        }
        # Global cache: group_code → control_group.id (all product families)
        self._group_cache: dict[str, uuid.UUID] | None = None
        # Per-family cache: ProductFamily → {group_code → id}
        self._group_cache_by_family: dict[ProductFamily, dict[str, uuid.UUID]] | None = None

    # ------------------------------------------------------------------
    # Control group resolution
    # ------------------------------------------------------------------

    # Section suffix pattern: -S1, -S2, etc. (multi-part policies/IMPs)
    _SECTION_SUFFIX_RE = re.compile(r"-[sS]\d+$")
    # Sub-part suffix: .1, .2, etc. after the main control ref
    _SUBPART_SUFFIX_RE = re.compile(r"\.\d+$")
    # "Also covers" suffix: e.g. a.5.1-2-6.1-2 → strip "-6.1-2"
    _ALSO_COVERS_RE = re.compile(r"(-\d+(?:\.\d+)+)$")

    def _build_group_caches(self) -> None:
        """Build global and per-family group code → id caches from DB."""
        self._group_cache = {}
        self._group_cache_by_family = {}
        rows = self.db.execute(
            select(ControlGroup.group_code, ControlGroup.id, ControlGroup.product_family)
        ).all()
        for code, cg_id, family in rows:
            lcode = code.lower()
            self._group_cache[lcode] = cg_id
            family_map = self._group_cache_by_family.setdefault(family, {})
            family_map[lcode] = cg_id

    def _resolve_control_group(
        self,
        group_code: str,
        preferred_family: ProductFamily | None = None,
    ) -> uuid.UUID | None:
        """Look up control_group.id by group_code with fallback normalisation.

        When preferred_family is supplied all resolution steps (exact match,
        section strip, sub-part strip, compact range, also-covers) are first
        attempted against groups of that family only.  The global cache is
        used as a last-resort fallback so that foundation/multi-product docs
        still resolve correctly.

        Handles:
        - Exact match: a.5.24-28
        - Section suffix: a.5.19-23-s1 → a.5.19-23
        - Sub-part suffix: a.5.31.1 → a.5.31
        - "Also covers" compound: a.5.1-2-6.1-2 → a.5.1-2
        - Compact ranges: a.7.1-2-3 → a.7.1-3, a.8.20-21-22 → a.8.20-22
        - Legacy A.0: 00 → a.0
        """
        if self._group_cache is None:
            self._build_group_caches()

        code = group_code.lower()

        # Ordered list of caches to try: family-specific first, then global.
        caches: list[dict[str, uuid.UUID]] = []
        if preferred_family is not None and preferred_family in self._group_cache_by_family:
            caches.append(self._group_cache_by_family[preferred_family])
        caches.append(self._group_cache)

        def _lookup(key: str) -> uuid.UUID | None:
            for cache in caches:
                if key in cache:
                    return cache[key]
            return None

        # 1. Exact match
        result = _lookup(code)
        if result:
            return result

        # 2. Foundation / non-ISO mapping: group_code "00" or non-A. prefix
        #    (covers ISMS-POL-00, ISMS-POL-01, ISMS-INS-POL-00, ISMS-REF-DORA, etc.)
        #    When a preferred_family is given, only look in that family's cache so
        #    PRIV-POL-00 / CLD-POL-00 etc. never fall back to the ISMS "00" group.
        if code == "00" or not code.startswith("a."):
            if preferred_family is not None:
                family_cache = self._group_cache_by_family.get(preferred_family, {})
                return family_cache.get("00") or None
            return _lookup("00")

        # 3. Strip section suffix (-S1, -S2, etc.)
        stripped = self._SECTION_SUFFIX_RE.sub("", code)
        result = _lookup(stripped)
        if result:
            return result

        # 4. Strip sub-part suffix (.1, .2, etc.)
        stripped = self._SUBPART_SUFFIX_RE.sub("", code)
        result = _lookup(stripped)
        if result:
            return result

        # 5. Compact range: a.7.1-2-3 → a.7.1-3 (first-last)
        compact = self._compact_range(code)
        if compact:
            result = _lookup(compact)
            if result:
                return result

        # 6. "Also covers" compound: a.5.1-2-6.1-2 → a.5.1-2
        stripped = self._ALSO_COVERS_RE.sub("", code)
        if stripped != code:
            result = _lookup(stripped)
            if result:
                return result

        return None

    # Folder name pattern
    _FOLDER_CODE_RE = re.compile(
        r"isms-(?:pol-)?(a[\d.\-]+?)(?:-[a-z]|$)", re.IGNORECASE
    )

    def _group_code_from_path(self, file_path: Path) -> str | None:
        """Extract group_code from the isms-a.X.X-... ancestor folder name."""
        if not hasattr(self, "_folder_cache"):
            self._folder_cache: dict[str, str] = {}
            rows = self.db.execute(
                select(ControlGroup.folder_name, ControlGroup.group_code)
            ).all()
            for fname, gcode in rows:
                self._folder_cache[fname.lower()] = gcode.lower()

        for part in file_path.parts:
            lower_part = part.lower()
            if lower_part.startswith("isms-") and lower_part in self._folder_cache:
                return self._folder_cache[lower_part]

        return None

    def _get_group_name(self, group_id: uuid.UUID) -> str | None:
        """Look up control group name by ID."""
        if not hasattr(self, "_name_cache"):
            self._name_cache: dict[uuid.UUID, str] = {}
            rows = self.db.execute(
                select(ControlGroup.id, ControlGroup.name)
            ).all()
            for cg_id, name in rows:
                self._name_cache[cg_id] = name
        return self._name_cache.get(group_id)

    def _get_group_code(self, group_id: uuid.UUID) -> str | None:
        """Look up the canonical DB group_code by ID."""
        if not hasattr(self, "_code_by_id_cache"):
            self._code_by_id_cache: dict[uuid.UUID, str] = {}
            rows = self.db.execute(
                select(ControlGroup.id, ControlGroup.group_code)
            ).all()
            for cg_id, code in rows:
                self._code_by_id_cache[cg_id] = code
        return self._code_by_id_cache.get(group_id)

    @staticmethod
    def _compact_range(code: str) -> str | None:
        """Convert a.7.1-2-3 → a.7.1-3 or a.8.20-21-22 → a.8.20-22."""
        parts = code.rsplit(".", 1)
        if len(parts) != 2:
            return None

        prefix, controls = parts
        nums = controls.split("-")
        if len(nums) < 3:
            return None

        if not all(n.isdigit() for n in nums):
            return None

        return f"{prefix}.{nums[0]}-{nums[-1]}"

    # ------------------------------------------------------------------
    # DataLoadHistory tracking
    # ------------------------------------------------------------------

    def _start_history(self, bundle_type: str = "import") -> DataLoadHistory:
        history = DataLoadHistory(
            bundle_type=bundle_type,
            bundle_file="(scan)",
            load_status="running",
        )
        self.db.add(history)
        self.db.flush()
        return history

    def _finish_history(
        self, history: DataLoadHistory, objects: int, relationships: int = 0
    ):
        history.objects_loaded = objects
        history.relationships_loaded = relationships
        history.load_status = "success"
        history.load_completed = datetime.now(timezone.utc)

    def _fail_history(self, history: DataLoadHistory, error: Exception):
        history.load_status = "failed"
        history.error_message = str(error)[:500]
        history.load_completed = datetime.now(timezone.utc)
        logger.error("Import failed: %s", error)
