"""IMP importer: scans Framework mount for IMP-UG/TG markdown files,
parses them, and upserts into the implementations table.

Follows the same patterns as PolicyImporter:
- Content hash change detection (skip unchanged files)
- Watermark-first identification with bold-header fallback
- 6-layer control group resolution
- DataLoadHistory tracking
- Upsert via document_id unique key
"""

import logging
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import func, select

from src.database.enums import ImplType, ProductFamily
from src.domain.content import Implementation
from src.domain.control_groups import ControlGroup
from src.importers.base_importer import BaseImporter
from src.importers.parsers.base import detect_impl_type
from src.services import search_service

logger = logging.getLogger(__name__)


class ImpImporter(BaseImporter):
    """Imports IMP-UG/TG files into the implementations table."""

    def __init__(self, db, framework_path: str, extra_paths: str = ""):
        super().__init__(db, framework_path)
        self.extra_paths: list[Path] = [
            Path(p.strip()) for p in extra_paths.split(",") if p.strip()
        ]

    def import_all(self) -> dict:
        """Scan Framework mount for IMP files, parse and upsert. Returns stats."""
        stats = {
            "implementations_imported": 0,
            "implementations_skipped": 0,
            "errors": 0,
            "error_details": [],
        }

        history = self._start_history("imp_import")

        try:
            # Pre-flight: ensure ISMS control groups have been seeded.
            isms_count = self.db.scalar(
                select(func.count(ControlGroup.id)).where(
                    ControlGroup.product_family == ProductFamily.ISMS
                )
            ) or 0
            if isms_count == 0:
                raise RuntimeError(
                    "ISMS control groups have not been seeded. "
                    "Run /admin/load before importing implementations."
                )

            files = self._discover_implementations()
            logger.info(
                "Discovered %d IMP files (framework_path=%s)",
                len(files),
                self.framework_path,
            )

            for file_path in files:
                try:
                    self._import_single(file_path, stats)
                except Exception as e:
                    stats["errors"] += 1
                    stats["error_details"].append(
                        {"file": str(file_path), "error": str(e)[:200]}
                    )
                    logger.error("Failed to import %s: %s", file_path.name, e)

            self._finish_history(
                history, stats["implementations_imported"]
            )
            logger.info("IMP import complete: %s", stats)
        except Exception as e:
            self._fail_history(history, e)
            raise

        return stats

    # ------------------------------------------------------------------
    # Discovery
    # ------------------------------------------------------------------

    # Content sniff: watermark (preferred) OR bold header pattern
    # Covers ISMS-IMP-, PRIV-IMP-, CLD-IMP- bold headers in addition to watermark
    _IMP_SNIFF_RE = re.compile(
        rb"<!-- ISMS-CORE:IMP:|"
        rb"\*\*(?:ISMS|PRIV|CLD)-IMP-"
    )

    def _discover_implementations(self) -> list[Path]:
        """Find IMP files via folder structure, then broad fallback scan."""
        seen: set[Path] = set()
        results: list[Path] = []

        if not self.framework_path.exists():
            logger.warning("Framework path does not exist: %s", self.framework_path)
            return results

        # Phase 1: Standard folder structure (EN + language subfolders)
        for doc_dir in self.framework_path.glob("A.*/isms-*/IMP/30_imp-md"):
            for f in sorted(doc_dir.iterdir()):
                if f.is_file() and f.suffix.lower() in self.parsers:
                    results.append(f)
                    seen.add(f.resolve())
            # Language subfolders: de/, fr/, it/
            for lang in ("de", "fr", "it"):
                lang_dir = doc_dir / lang
                if lang_dir.is_dir():
                    for f in sorted(lang_dir.iterdir()):
                        if f.is_file() and f.suffix.lower() in self.parsers:
                            results.append(f)
                            seen.add(f.resolve())

        # Phase 2: Broad fallback — walk framework mount for relocated files
        fallback_count = 0
        for f in self.framework_path.rglob("*"):
            if not f.is_file() or f.suffix.lower() not in self.parsers:
                continue
            if f.resolve() in seen:
                continue
            try:
                head = f.read_bytes()[:512]
                if self._IMP_SNIFF_RE.search(head):
                    results.append(f)
                    seen.add(f.resolve())
                    fallback_count += 1
            except OSError:
                continue

        if fallback_count:
            logger.info(
                "Broad scan found %d additional IMP files in %s",
                fallback_count,
                self.framework_path,
            )

        # Phase 3: Extra paths (PRIV / CLD mounts) — broad sniff scan
        for extra in self.extra_paths:
            if not extra.exists():
                logger.warning("IMP extra path does not exist: %s", extra)
                continue
            extra_count = 0
            for f in extra.rglob("*"):
                if not f.is_file() or f.suffix.lower() not in self.parsers:
                    continue
                if f.resolve() in seen:
                    continue
                try:
                    head = f.read_bytes()[:512]
                    if self._IMP_SNIFF_RE.search(head):
                        results.append(f)
                        seen.add(f.resolve())
                        extra_count += 1
                except OSError:
                    continue
            if extra_count:
                logger.info("Found %d IMP files in extra path %s", extra_count, extra)

        return results

    # ------------------------------------------------------------------
    # Single file import
    # ------------------------------------------------------------------

    def _import_single(self, file_path: Path, stats: dict):
        """Parse one IMP file and upsert into DB."""
        ext = file_path.suffix.lower()
        parser = self.parsers.get(ext)
        if not parser:
            raise ValueError(f"No parser for extension: {ext}")

        parsed = parser.parse(file_path)

        # IMP files are always ISMS — resolve against ISMS groups only to prevent
        # cross-product contamination via sub-part fallback (e.g. a.8.9 → a.8 CLOUD).
        group_id = self._resolve_control_group(parsed.group_code, ProductFamily.ISMS)
        if not group_id:
            folder_code = self._group_code_from_path(file_path)
            if folder_code:
                group_id = self._resolve_control_group(folder_code, ProductFamily.ISMS)
        if not group_id:
            raise ValueError(
                f"No control group found for group_code={parsed.group_code} "
                f"(document_id={parsed.document_id})"
            )

        # Check for unchanged content
        existing = self.db.execute(
            select(Implementation).where(
                Implementation.document_id == parsed.document_id
            )
        ).scalar_one_or_none()

        if existing and existing.content_hash == parsed.content_hash:
            stats["implementations_skipped"] += 1
            logger.debug("Skip %s (unchanged)", parsed.document_id)
            # Still (re-)index in OpenSearch — idempotent, recovers from missed
            # indexing if OpenSearch was unavailable during the initial import.
            _group_code = self._get_group_code(group_id) or parsed.group_code
            _group_name = self._get_group_name(group_id) or ""
            _language = existing.language or "en"
            search_service.index_implementation(
                document_id=parsed.document_id,
                title=parsed.title,
                impl_type=existing.impl_type.value if hasattr(existing.impl_type, "value") else str(existing.impl_type),
                control_group_code=_group_code,
                control_group_name=_group_name,
                product_type=parsed.product_type,
                sections=[
                    {"heading": s.heading, "body": s.body, "level": s.level}
                    for s in parsed.sections
                ],
                word_count=parsed.word_count,
                file_path=str(file_path),
                language=_language,
                metadata=parsed.metadata,
            )
            return

        # Determine impl_type from watermark type field or doc_id
        # Watermark puts "UG"/"TG" in parsed.policy_type for IMP files
        if parsed.policy_type in ("UG", "TG"):
            impl_type = ImplType(parsed.policy_type)
        else:
            impl_type = ImplType(detect_impl_type(parsed.document_id))

        # Detect language from subfolder or document ID suffix
        parent = file_path.parent.name.lower()
        language = parent if parent in ("de", "fr", "it") else "en"
        doc_upper = parsed.document_id.upper()
        if language == "en":
            for suffix, lang in (("-DE", "de"), ("-FR", "fr"), ("-IT", "it")):
                if doc_upper.endswith(suffix):
                    language = lang
                    break

        rel_path = str(file_path)

        if existing:
            # Update existing implementation
            existing.title = parsed.title
            existing.impl_type = impl_type
            existing.control_group_id = group_id
            existing.file_path = rel_path
            existing.content_hash = parsed.content_hash
            existing.word_count = parsed.word_count
            existing.last_parsed = datetime.now(timezone.utc)
            existing.metadata_ = parsed.metadata
            existing.language = language
        else:
            # Create new implementation
            impl = Implementation(
                id=uuid.uuid4(),
                control_group_id=group_id,
                impl_type=impl_type,
                document_id=parsed.document_id,
                title=parsed.title,
                file_path=rel_path,
                content_hash=parsed.content_hash,
                word_count=parsed.word_count,
                last_parsed=datetime.now(timezone.utc),
                metadata_=parsed.metadata,
                language=language,
            )
            self.db.add(impl)
            self.db.flush()

        stats["implementations_imported"] += 1

        # Index into OpenSearch (graceful — won't fail import if OS is down)
        group_name = self._get_group_name(group_id)
        db_group_code = self._get_group_code(group_id) or parsed.group_code
        search_service.index_implementation(
            document_id=parsed.document_id,
            title=parsed.title,
            impl_type=impl_type.value,
            control_group_code=db_group_code,
            control_group_name=group_name or "",
            product_type=parsed.product_type,
            sections=[
                {"heading": s.heading, "body": s.body, "level": s.level}
                for s in parsed.sections
            ],
            word_count=parsed.word_count,
            file_path=rel_path,
            language=language,
            metadata=parsed.metadata,
        )

        logger.info(
            "Imported %s: %s (%s)",
            parsed.document_id,
            parsed.title,
            impl_type.value,
        )
