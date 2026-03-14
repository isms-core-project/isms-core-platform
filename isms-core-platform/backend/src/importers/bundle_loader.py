"""
Bundle loader: reads Phase 0 JSON bundles from datasets/data/ and upserts into PostgreSQL.

5 bundle types, loaded in FK-dependency order:
  1. Single framework (12 files) → Framework + FrameworkControl
  2. Multi-framework (owasp.json) → Framework(s) + FrameworkControl
  3. Control groups (1 file) → ControlGroup + junction rows
  4. Crosswalk (N files) → CrossFrameworkMapping
     - crosswalk.json (inter-framework mappings)
     - control_dependencies.json (intra-ISO-27001 dependencies)
  5. Generator registry (generator_registry.json, list format) → GeneratorDefinition
"""

import json
import logging
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.domain.content import GeneratorDefinition
from src.domain.control_groups import ControlGroup, control_group_controls
from src.domain.frameworks import CrossFrameworkMapping, Framework, FrameworkControl
from src.domain.system import DataLoadHistory
from src.importers.bundle_types import BundleType, detect_bundle_type

logger = logging.getLogger(__name__)

ISO27001_CODE = "ISO27001_2022"
GENERATOR_REGISTRY_FILE = "generator_registry.json"


class BundleLoader:
    """Loads Phase 0 JSON bundles into PostgreSQL."""

    def __init__(self, db: DBSession, datasets_path: str):
        self.db = db
        self.datasets_path = Path(datasets_path)

    def load_all(self) -> dict:
        """Load all bundles in FK-dependency order. Returns stats dict."""
        json_files = sorted(self.datasets_path.glob("*.json"))
        if not json_files:
            logger.warning("No JSON files found in %s", self.datasets_path)
            return self._empty_stats()

        # Separate generator_registry.json (list format) from dict-based bundles
        generator_registry_path: Path | None = None
        fw_bundles: list[tuple[Path, dict, BundleType]] = []
        cg_bundle: tuple[Path, dict] | None = None
        xw_bundles: list[tuple[Path, dict]] = []

        for fp in json_files:
            if fp.name == GENERATOR_REGISTRY_FILE:
                generator_registry_path = fp
                continue
            with open(fp) as f:
                data = json.load(f)
            if not isinstance(data, dict):
                logger.debug("Skipping %s — not a JSON object (got %s)", fp.name, type(data).__name__)
                continue
            btype = detect_bundle_type(data)
            if btype is None:
                logger.debug("Skipping %s — unrecognised bundle format", fp.name)
                continue
            if btype in (BundleType.SINGLE_FRAMEWORK, BundleType.MULTI_FRAMEWORK):
                fw_bundles.append((fp, data, btype))
            elif btype == BundleType.CONTROL_GROUPS:
                cg_bundle = (fp, data)
            elif btype == BundleType.CROSSWALK:
                xw_bundles.append((fp, data))

        logger.info(
            "Found %d framework, %d control-group, %d crosswalk bundles",
            len(fw_bundles),
            1 if cg_bundle else 0,
            len(xw_bundles),
        )

        stats = self._empty_stats()

        # Phase 1: All frameworks (single + multi)
        for fp, data, btype in fw_bundles:
            if btype == BundleType.SINGLE_FRAMEWORK:
                self._load_single_framework(fp.name, data, stats)
            else:
                self._load_multi_framework(fp.name, data, stats)
        self.db.flush()

        # Phase 2: Control groups + junction rows
        if cg_bundle:
            self._load_control_groups(cg_bundle[0].name, cg_bundle[1], stats)
            self.db.flush()

        # Phase 3: Crosswalk mappings (crosswalk + control dependencies)
        for xw_fp, xw_data in xw_bundles:
            self._load_crosswalk(xw_fp.name, xw_data, stats)

        # Phase 4: Generator registry (list-format JSON — must run after control groups)
        if generator_registry_path:
            self._load_generator_registry(generator_registry_path, stats)

        self.db.commit()
        logger.info("Load complete: %s", stats)
        return stats

    # ------------------------------------------------------------------
    # Type 1: Single framework
    # ------------------------------------------------------------------

    def _load_single_framework(self, filename: str, data: dict, stats: dict):
        fw_data = data["framework"]
        content_hash = data.get("content_hash")

        if self._skip_if_unchanged(Framework, fw_data["id"], content_hash, filename):
            stats["skipped"] += 1
            return

        history = self._start_history(
            "single_framework", filename, fw_data["code"],
            fw_data.get("version"), content_hash,
        )

        try:
            self._upsert_framework(fw_data, content_hash, data)
            loaded = self._upsert_controls(data.get("objects", []))

            self._finish_history(history, loaded, 0)
            stats["frameworks"] += 1
            stats["controls"] += loaded
            logger.info("Loaded %s: %s (%d controls)", filename, fw_data["code"], loaded)
        except Exception as e:
            self._fail_history(history, e)
            raise

    # ------------------------------------------------------------------
    # Type 2: Multi-framework (owasp.json)
    # ------------------------------------------------------------------

    def _load_multi_framework(self, filename: str, data: dict, stats: dict):
        content_hash = data.get("content_hash")
        frameworks = data["frameworks"]

        # Check if ALL frameworks are unchanged
        all_unchanged = all(
            self._is_unchanged(Framework, fw["id"], content_hash)
            for fw in frameworks
        )
        if all_unchanged:
            logger.info("Skip %s (all frameworks unchanged)", filename)
            stats["skipped"] += 1
            return

        history = self._start_history(
            "multi_framework", filename,
            "+".join(fw["code"] for fw in frameworks),
            None, content_hash,
        )

        try:
            for fw_data in frameworks:
                self._upsert_framework(fw_data, content_hash, data)
                stats["frameworks"] += 1

            loaded = self._upsert_controls(data.get("objects", []))

            self._finish_history(history, loaded, 0)
            stats["controls"] += loaded
            logger.info(
                "Loaded %s: %d frameworks, %d controls",
                filename, len(frameworks), loaded,
            )
        except Exception as e:
            self._fail_history(history, e)
            raise

    # ------------------------------------------------------------------
    # Type 3: Control groups
    # ------------------------------------------------------------------

    def _load_control_groups(self, filename: str, data: dict, stats: dict):
        content_hash = data.get("content_hash")
        objects = data.get("objects", [])

        history = self._start_history(
            "control_groups", filename, None, None, content_hash,
        )

        try:
            loaded = 0
            junction_rows = 0

            for obj in objects:
                if obj.get("type") != "control_group":
                    continue

                # Extra fields go into metadata
                extra = {
                    "also_covers": obj.get("also_covers", []),
                    "is_iso_standard": obj.get("is_iso_standard", True),
                    "sort_order": obj.get("sort_order", 0),
                }
                obj_metadata = obj.get("metadata", {})
                obj_metadata.update(extra)

                cg = ControlGroup(
                    id=uuid.UUID(obj["id"]),
                    group_code=obj["group_code"],
                    name=obj["name"],
                    section=obj["section"],
                    section_name=obj["section_name"],
                    folder_name=obj["folder_name"],
                    is_stacked=obj.get("is_stacked", False),
                    stacked_control_ids=obj.get("stacked_control_ids", []),
                    has_framework=obj.get("has_framework", True),
                    has_operational=obj.get("has_operational", True),
                    metadata_=obj_metadata,
                )
                self.db.merge(cg)
                loaded += 1

            self.db.flush()

            # Populate junction table: control_group ↔ framework_controls
            junction_rows = self._populate_control_group_junctions(objects)

            self._finish_history(history, loaded, junction_rows)
            stats["groups"] += loaded
            stats["junctions"] += junction_rows
            logger.info(
                "Loaded %s: %d control groups, %d junction rows",
                filename, loaded, junction_rows,
            )
        except Exception as e:
            self._fail_history(history, e)
            raise

    def _populate_control_group_junctions(self, objects: list[dict]) -> int:
        """Link control groups to their ISO 27001 framework_controls."""
        # Find the ISO 27001 framework
        iso_fw = self.db.execute(
            select(Framework).where(Framework.code == ISO27001_CODE)
        ).scalar_one_or_none()

        if not iso_fw:
            logger.warning("ISO27001_2022 framework not found — skipping junction rows")
            return 0

        # Build lookup: control_id → framework_control.id
        iso_controls = self.db.execute(
            select(FrameworkControl.control_id, FrameworkControl.id)
            .where(FrameworkControl.framework_id == iso_fw.id)
        ).all()
        control_lookup = {row[0]: row[1] for row in iso_controls}

        # Clear existing junctions (full replace)
        self.db.execute(control_group_controls.delete())

        rows_inserted = 0
        for obj in objects:
            if obj.get("type") != "control_group":
                continue

            cg_id = uuid.UUID(obj["id"])
            # Combine stacked_control_ids + also_covers
            all_control_ids = list(obj.get("stacked_control_ids", []))
            all_control_ids.extend(obj.get("also_covers", []))

            for ctrl_id in all_control_ids:
                fc_id = control_lookup.get(ctrl_id)
                if fc_id:
                    self.db.execute(
                        control_group_controls.insert().values(
                            control_group_id=cg_id,
                            framework_control_id=fc_id,
                        )
                    )
                    rows_inserted += 1
                else:
                    logger.debug("No ISO control found for %s (group %s)", ctrl_id, obj["group_code"])

        return rows_inserted

    # ------------------------------------------------------------------
    # Type 4: Generator registry (list-format JSON)
    # ------------------------------------------------------------------

    def _load_generator_registry(self, fp: Path, stats: dict):
        """Upsert 188 GeneratorDefinition rows from generator_registry.json."""
        with open(fp) as f:
            entries = json.load(f)

        if not isinstance(entries, list):
            logger.warning("%s: expected a JSON array, got %s — skipping", fp.name, type(entries).__name__)
            return

        # Build group_code → control_group.id lookup (lowercase keys)
        rows = self.db.execute(
            select(ControlGroup.group_code, ControlGroup.id)
        ).all()
        group_lookup: dict[str, uuid.UUID] = {code.lower(): cg_id for code, cg_id in rows}

        _sn_suffix = re.compile(r"-s\d+$", re.IGNORECASE)

        def _resolve_group_code(code: str) -> uuid.UUID | None:
            lcode = code.lower()
            if lcode in group_lookup:
                return group_lookup[lcode]
            # Strip -S1/-S2/-S3 suffix (stacked domain generators)
            stripped = _sn_suffix.sub("", lcode)
            if stripped != lcode and stripped in group_lookup:
                return group_lookup[stripped]
            return None

        loaded = 0
        skipped = 0
        for entry in entries:
            doc_id = entry.get("document_id")
            if not doc_id:
                skipped += 1
                continue

            group_code = entry.get("group_code", "")
            control_group_id = _resolve_group_code(group_code)

            # Look up existing record by document_id
            existing = self.db.execute(
                select(GeneratorDefinition)
                .where(GeneratorDefinition.document_id == doc_id)
            ).scalar_one_or_none()

            if existing:
                if existing.user_override:
                    skipped += 1
                    continue
                # Update in place
                existing.workbook_name = entry.get("workbook_name", "")
                existing.control_id = entry.get("control_id", "")
                existing.control_name = entry.get("control_name", "")
                existing.group_code = group_code
                existing.control_group_id = control_group_id
                existing.domain_number = entry.get("domain_number")
                existing.domain_total = entry.get("domain_total")
                existing.is_stacked = entry.get("is_stacked", False)
                existing.stacked_control_ids = entry.get("stacked_control_ids")
                existing.sheets = entry.get("sheets", [])
                existing.sheet_count = entry.get("sheet_count", 0)
                existing.sheet_source = entry.get("sheet_source")
                existing.source_file = entry.get("source_file")
                existing.product_type = entry.get("product_type", "framework")
            else:
                gd = GeneratorDefinition(
                    document_id=doc_id,
                    workbook_name=entry.get("workbook_name", ""),
                    control_id=entry.get("control_id", ""),
                    control_name=entry.get("control_name", ""),
                    group_code=group_code,
                    control_group_id=control_group_id,
                    domain_number=entry.get("domain_number"),
                    domain_total=entry.get("domain_total"),
                    is_stacked=entry.get("is_stacked", False),
                    stacked_control_ids=entry.get("stacked_control_ids"),
                    sheets=entry.get("sheets", []),
                    sheet_count=entry.get("sheet_count", 0),
                    sheet_source=entry.get("sheet_source"),
                    source_file=entry.get("source_file"),
                    product_type=entry.get("product_type", "framework"),
                )
                self.db.add(gd)
            loaded += 1

        stats["generators"] += loaded
        logger.info(
            "Loaded %s: %d generator definitions (%d skipped)",
            fp.name, loaded, skipped,
        )

    # ------------------------------------------------------------------
    # Type 5: Crosswalk
    # ------------------------------------------------------------------

    def _load_crosswalk(self, filename: str, data: dict, stats: dict):
        content_hash = data.get("content_hash")
        objects = data.get("objects", [])

        history = self._start_history(
            "crosswalk", filename, None, None, content_hash,
        )

        try:
            # Pre-fetch all valid framework_control IDs for FK validation
            rows = self.db.execute(
                select(FrameworkControl.id, Framework.code, FrameworkControl.control_id)
                .join(Framework, FrameworkControl.framework_id == Framework.id)
            ).all()
            valid_ids: set[uuid.UUID] = set()
            # Fallback: (framework_code, control_id) → UUID for bundles that use
            # non-UUID5 hardcoded IDs (e.g. ISO 27018 uses fixed IDs, not uuid5)
            fw_ctrl_lookup: dict[tuple[str, str], uuid.UUID] = {}
            for row in rows:
                valid_ids.add(row[0])
                fw_ctrl_lookup[(row[1], row[2])] = row[0]

            def resolve_control_id(ctrl_uuid_str: str, fw_code: str, ctrl_id: str) -> uuid.UUID | None:
                """Resolve control UUID.

                Prefer (framework_code, control_id) lookup — it is always exact.
                Fall back to the raw UUID only when fw_code/ctrl_id are absent.
                This avoids false positives where UUID5(ISO27018, A.X) happens to
                equal another control's ID due to off-by-one shifts in legacy bundles.
                """
                # Primary: exact lookup by framework code + control_id
                if fw_code and ctrl_id:
                    result = fw_ctrl_lookup.get((fw_code, ctrl_id))
                    if result is not None:
                        return result
                # Fallback: try the UUID directly (for bundles with correct UUID5 IDs)
                try:
                    cid = uuid.UUID(ctrl_uuid_str)
                    if cid in valid_ids:
                        return cid
                except (ValueError, AttributeError):
                    pass
                return None

            loaded = 0
            skipped = 0
            for obj in objects:
                if obj.get("type") != "cross_framework_mapping":
                    continue

                src_id = resolve_control_id(
                    obj.get("source_control_id", ""),
                    obj.get("source_framework", ""),
                    obj.get("source_control", ""),
                )
                tgt_id = resolve_control_id(
                    obj.get("target_control_id", ""),
                    obj.get("target_framework", ""),
                    obj.get("target_control", ""),
                )

                if src_id is None or tgt_id is None:
                    skipped += 1
                    continue

                cfm = CrossFrameworkMapping(
                    id=uuid.UUID(obj["id"]),
                    source_control_id=src_id,   # type: ignore[arg-type]
                    target_control_id=tgt_id,   # type: ignore[arg-type]
                    mapping_type=obj.get("mapping_type", "maps-to"),
                    confidence=obj.get("confidence", 0.85),
                    source_reference=obj.get("source_reference"),
                    notes=obj.get("notes"),
                    metadata_={
                        "source_framework": obj.get("source_framework"),
                        "source_control": obj.get("source_control"),
                        "target_framework": obj.get("target_framework"),
                        "target_control": obj.get("target_control"),
                    },
                )
                self.db.merge(cfm)
                loaded += 1

            self._finish_history(history, loaded, 0)
            stats["mappings"] += loaded
            if skipped:
                logger.warning(
                    "Loaded %s: %d mappings (%d skipped — orphaned FK refs)",
                    filename, loaded, skipped,
                )
            else:
                logger.info("Loaded %s: %d cross-framework mappings", filename, loaded)
        except Exception as e:
            self._fail_history(history, e)
            raise

    # ------------------------------------------------------------------
    # Shared helpers
    # ------------------------------------------------------------------

    def _upsert_framework(self, fw_data: dict, content_hash: str | None, bundle: dict):
        """Create or update a Framework record."""
        objects = bundle.get("objects", [])
        controls_count = sum(1 for o in objects if o.get("framework_id") == fw_data["id"])
        if controls_count == 0:
            controls_count = bundle.get("objects_count", 0)

        framework = Framework(
            id=uuid.UUID(fw_data["id"]),
            code=fw_data["code"],
            name=fw_data["name"],
            version=fw_data.get("version"),
            publisher=fw_data.get("publisher"),
            source_url=fw_data.get("source_url"),
            description=fw_data.get("description"),
            jurisdiction=(fw_data.get("jurisdiction") or "")[:10] or None,
            controls_count=controls_count,
            bundle_hash=content_hash,
            metadata_={},
        )
        self.db.merge(framework)

    def _upsert_controls(self, objects: list[dict]) -> int:
        """Upsert FrameworkControl records. Returns count loaded."""
        # Sort by level so parents exist before children (self-referential FK)
        sorted_objects = sorted(objects, key=lambda o: o.get("level", 0))
        loaded = 0
        for obj in sorted_objects:
            if obj.get("type") != "framework_control":
                continue
            fc = FrameworkControl(
                id=uuid.UUID(obj["id"]),
                framework_id=uuid.UUID(obj["framework_id"]),
                control_id=obj["control_id"],
                parent_id=uuid.UUID(obj["parent_id"]) if obj.get("parent_id") else None,
                title=obj["title"],
                description=obj.get("description"),
                control_type=obj.get("control_type", []),
                security_properties=obj.get("security_properties", []),
                level=obj.get("level", 1),
                sort_order=obj.get("sort_order", 0),
                metadata_=obj.get("metadata", {}),
            )
            self.db.merge(fc)
            loaded += 1
        return loaded

    def _skip_if_unchanged(self, model, pk_str: str, content_hash: str | None, filename: str) -> bool:
        """Return True if the record exists with the same bundle_hash."""
        if not content_hash:
            return False
        if self._is_unchanged(model, pk_str, content_hash):
            logger.info("Skip %s (unchanged, hash=%s…)", filename, content_hash[:12])
            return True
        return False

    def _is_unchanged(self, model, pk_str: str, content_hash: str | None) -> bool:
        existing = self.db.get(model, uuid.UUID(pk_str))
        return existing is not None and existing.bundle_hash == content_hash

    # ------------------------------------------------------------------
    # Data load history
    # ------------------------------------------------------------------

    def _start_history(
        self, bundle_type: str, filename: str,
        framework_code: str | None, version: str | None,
        content_hash: str | None,
    ) -> DataLoadHistory:
        history = DataLoadHistory(
            bundle_type=bundle_type,
            bundle_file=filename,
            framework_code=framework_code,
            version=version,
            bundle_hash=content_hash,
            load_status="running",
        )
        self.db.add(history)
        self.db.flush()
        return history

    def _finish_history(self, history: DataLoadHistory, objects: int, relationships: int):
        history.objects_loaded = objects
        history.relationships_loaded = relationships
        history.load_status = "success"
        history.load_completed = datetime.now(timezone.utc)

    def _fail_history(self, history: DataLoadHistory, error: Exception):
        history.load_status = "failed"
        history.error_message = str(error)[:500]
        history.load_completed = datetime.now(timezone.utc)
        logger.error("Bundle load failed: %s", error)

    @staticmethod
    def _empty_stats() -> dict:
        return {
            "frameworks": 0,
            "controls": 0,
            "groups": 0,
            "junctions": 0,
            "mappings": 0,
            "generators": 0,
            "skipped": 0,
        }
