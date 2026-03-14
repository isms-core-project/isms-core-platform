"""Policy importer: scans Framework and Operational mounts, parses policies,
extracts requirements, and upserts into PostgreSQL.

Follows the same patterns as BundleLoader:
- Content hash change detection (skip unchanged files)
- DataLoadHistory tracking
- Upsert via merge() on unique document_id
"""

import logging
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import delete, func, select
from sqlalchemy.orm import Session as DBSession

from src.database.enums import ComplianceStatus, PolicyType, ProductFamily, ProductType
from src.domain.content import Policy, Requirement
from src.domain.control_groups import ControlGroup
from src.importers.base_importer import BaseImporter
from src.importers.parsers.base import ParsedPolicy
from src.services import search_service

logger = logging.getLogger(__name__)

# Maps ProductType → ProductFamily for group resolution
_PRODUCT_FAMILY: dict[str, ProductFamily] = {
    ProductType.FRAMEWORK: ProductFamily.ISMS,
    ProductType.OPERATIONAL: ProductFamily.ISMS,
    ProductType.PRIVACY: ProductFamily.PRIVACY,
    ProductType.CLOUD: ProductFamily.CLOUD,
}

# Sections to skip when extracting requirements (boilerplate)
_SKIP_SECTIONS = {
    "(preamble)",
    "document control",
    "version history",
    "approval record",
    "areas of the iso27001 standard addressed",
    "document contents page",
    "document version control",
    "related documents",
    "related annex a controls",
    "related internal policies",
    "definitions",
}

# Sentence boundary pattern
_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")

# Bullet point pattern (markdown list items)
_BULLET_RE = re.compile(r"^\s*[-*]\s+", re.MULTILINE)

# "shall" / "should" detection
_SHALL_RE = re.compile(r"\bshall\b", re.IGNORECASE)
_SHOULD_RE = re.compile(r"\bshould\b", re.IGNORECASE)


class PolicyImporter(BaseImporter):
    """Imports POL and OP-POL files into the policies + requirements tables."""

    def __init__(
        self,
        db: DBSession,
        framework_path: str,
        operational_path: str,
        extra_paths: str = "",
    ):
        super().__init__(db, framework_path)
        self.operational_path = Path(operational_path)
        # Extra scan paths: comma-separated, customer-configurable
        self.extra_paths: list[Path] = [
            Path(p.strip())
            for p in extra_paths.split(",")
            if p.strip()
        ]

    def import_all(self) -> dict:
        """Scan both mounts, parse policies, upsert into DB. Returns stats."""
        stats = {
            "policies_imported": 0,
            "policies_skipped": 0,
            "requirements_extracted": 0,
            "errors": 0,
            "error_details": [],
        }

        history = self._start_history("policy_import")

        try:
            # Pre-flight: ensure ISMS control groups have been seeded.
            # Without them, framework/operational policies would be misrouted
            # to non-ISMS groups via the sub-part stripping fallback.
            isms_count = self.db.scalar(
                select(func.count(ControlGroup.id)).where(
                    ControlGroup.product_family == ProductFamily.ISMS
                )
            ) or 0
            if isms_count == 0:
                raise RuntimeError(
                    "ISMS control groups have not been seeded. "
                    "Run /admin/load before importing policies."
                )

            files = self._discover_policies()
            logger.info(
                "Discovered %d policy files (framework_path=%s, operational_path=%s)",
                len(files),
                self.framework_path,
                self.operational_path,
            )

            for file_path, hint_product in files:
                try:
                    self._import_single(file_path, hint_product, stats)
                except Exception as e:
                    stats["errors"] += 1
                    stats["error_details"].append(
                        {"file": str(file_path), "error": str(e)[:200]}
                    )
                    logger.error("Failed to import %s: %s", file_path.name, e)

            self._finish_history(
                history,
                stats["policies_imported"],
                stats["requirements_extracted"],
            )
            logger.info("Policy import complete: %s", stats)
        except Exception as e:
            self._fail_history(history, e)
            raise

        return stats

    # ------------------------------------------------------------------
    # Discovery
    # ------------------------------------------------------------------

    # Content sniff: watermark (preferred) OR bold/heading pattern
    # Watermark: <!-- ISMS-CORE:POLICY:ISMS-POL-... --> (or INS/REF/CTX/FORM)
    # Bold header: **ISMS-POL-A.X.X or **ISMS-REF-A.X.X etc.
    # Plain heading: # ISMS-INS-POL-00 (INS files have no watermark)
    _POLICY_SNIFF_RE = re.compile(
        rb"<!-- ISMS-CORE:(?:POLICY|INS|REF|CTX|FORM):|"
        rb"\*\*ISMS-(?:OP-)?(?:INS-)?(?:POL|REF|CTX|FORM)-|"
        rb"# ISMS-INS-(?:POL|REF)-\d"
    )

    def _discover_policies(self) -> list[tuple[Path, str]]:
        """Find policy files via folder structure, then broad fallback scan.

        Phase 1: Standard paths — A.*/isms-*/POL/10_pol-md/*.{md,pdf,docx}
        Phase 2: Broad scan — walk entire mount for any supported file whose
                 first 512 bytes contain ISMS-POL- or ISMS-OP-POL-
        """
        seen: set[Path] = set()
        results: list[tuple[Path, str]] = []

        for mount, product in [
            (self.framework_path, "framework"),
            (self.operational_path, "operational"),
        ]:
            if not mount.exists():
                logger.warning("Mount path does not exist: %s", mount)
                continue

            # Phase 1: Standard folder structure (POL + REF + CTX + FORM + language subfolders)
            doc_globs = [
                "A.*/isms-*/POL/10_pol-md",
                "A.*/isms-*/POL/10_pol-md/de",
                "A.*/isms-*/POL/10_pol-md/fr",
                "A.*/isms-*/POL/10_pol-md/it",
                "A.*/isms-*/REF/*_ref-md",
                "A.*/isms-*/REF/*_ref-md/de",
                "A.*/isms-*/REF/*_ref-md/fr",
                "A.*/isms-*/REF/*_ref-md/it",
                "A.*/isms-*/CTX/*_ctx-md",
                "A.*/isms-*/CTX/*_ctx-md/de",
                "A.*/isms-*/CTX/*_ctx-md/fr",
                "A.*/isms-*/CTX/*_ctx-md/it",
                "A.*/isms-*/FORM/*_form-md",
                "A.*/isms-*/FORM/*_form-md/de",
                "A.*/isms-*/FORM/*_form-md/fr",
                "A.*/isms-*/FORM/*_form-md/it",
                # Foundation policies (00-foundation-policies/): POL, INS, REF
                "00-foundation-policies/*/POL",
                "00-foundation-policies/*/POL/de",
                "00-foundation-policies/*/POL/fr",
                "00-foundation-policies/*/POL/it",
                "00-foundation-policies/*/INS",
                "00-foundation-policies/*/REF",
            ]
            for gpattern in doc_globs:
                for doc_dir in mount.glob(gpattern):
                    for f in sorted(doc_dir.iterdir()):
                        if f.is_file() and f.suffix.lower() in self.parsers:
                            results.append((f, product))
                            seen.add(f.resolve())

            # Phase 2: Broad fallback — walk entire mount for relocated files
            fallback_count = 0
            for f in mount.rglob("*"):
                if not f.is_file() or f.suffix.lower() not in self.parsers:
                    continue
                if f.resolve() in seen:
                    continue
                # Quick sniff: check first 512 bytes for ISMS policy ID
                try:
                    head = f.read_bytes()[:512]
                    if self._POLICY_SNIFF_RE.search(head):
                        results.append((f, product))
                        seen.add(f.resolve())
                        fallback_count += 1
                except OSError:
                    continue

            if fallback_count:
                logger.info(
                    "Broad scan found %d additional policy files in %s",
                    fallback_count,
                    mount,
                )

        # Phase 3: Extra customer-configured scan paths
        for extra in self.extra_paths:
            if not extra.exists():
                logger.warning("Extra scan path does not exist: %s", extra)
                continue

            extra_count = 0
            for f in extra.rglob("*"):
                if not f.is_file() or f.suffix.lower() not in self.parsers:
                    continue
                if f.resolve() in seen:
                    continue
                try:
                    head = f.read_bytes()[:512]
                    if self._POLICY_SNIFF_RE.search(head):
                        # Product type detected from content, not path
                        results.append((f, "framework"))
                        seen.add(f.resolve())
                        extra_count += 1
                except OSError:
                    continue

            if extra_count:
                logger.info(
                    "Extra path scan found %d policy files in %s",
                    extra_count,
                    extra,
                )

        return results

    # ------------------------------------------------------------------
    # Single file import
    # ------------------------------------------------------------------

    @staticmethod
    def _detect_language(file_path: Path, document_id: str) -> str:
        """Detect language from file path subfolder or document ID suffix.

        Checks in order:
          1. Parent folder name: .../de/file.md → "de"
          2. Document ID suffix: ISMS-POL-A.5.1-DE → "de"
          3. Default: "en"
        """
        parent = file_path.parent.name.lower()
        if parent in ("de", "fr", "it"):
            return parent
        doc_upper = document_id.upper()
        for suffix, lang in (("-DE", "de"), ("-FR", "fr"), ("-IT", "it")):
            if doc_upper.endswith(suffix):
                return lang
        return "en"

    def _import_single(self, file_path: Path, hint_product: str, stats: dict):
        """Parse one policy file and upsert into DB."""
        ext = file_path.suffix.lower()
        parser = self.parsers.get(ext)
        if not parser:
            raise ValueError(f"No parser for extension: {ext}")

        parsed = parser.parse(file_path)

        # Determine which product family to prefer when resolving the control group.
        # This prevents cross-product contamination via the sub-part fallback
        # (e.g. a.5.14 must not resolve to the CLOUD group a.5).
        preferred_family = _PRODUCT_FAMILY.get(ProductType(parsed.product_type))

        # Resolve control group (try doc ID first, then folder name fallback)
        group_id = self._resolve_control_group(parsed.group_code, preferred_family)
        if not group_id:
            folder_code = self._group_code_from_path(file_path)
            if folder_code:
                group_id = self._resolve_control_group(folder_code, preferred_family)
        if not group_id:
            raise ValueError(
                f"No control group found for group_code={parsed.group_code} "
                f"(document_id={parsed.document_id})"
            )

        # Check for unchanged content
        existing = self.db.execute(
            select(Policy).where(Policy.document_id == parsed.document_id)
        ).scalar_one_or_none()

        if existing and existing.content_hash == parsed.content_hash:
            stats["policies_skipped"] += 1
            logger.debug("Skip %s (unchanged)", parsed.document_id)
            return

        # Map enums
        product_type = ProductType(parsed.product_type)
        policy_type = PolicyType(parsed.policy_type)
        language = self._detect_language(file_path, parsed.document_id)

        # Extract requirements
        requirements = self._extract_requirements(parsed)

        # Build relative file path (from mount root)
        rel_path = str(file_path)

        if existing:
            # Update existing policy
            existing.title = parsed.title
            existing.product_type = product_type
            existing.policy_type = policy_type
            existing.control_group_id = group_id
            existing.file_path = rel_path
            existing.content_hash = parsed.content_hash
            existing.word_count = parsed.word_count
            existing.requirements_count = len(requirements)
            existing.last_parsed = datetime.now(timezone.utc)
            existing.metadata_ = parsed.metadata
            existing.language = language
            policy = existing

            # Delete old requirements (cascade rebuild)
            self.db.execute(
                delete(Requirement).where(Requirement.policy_id == policy.id)
            )
            self.db.flush()
        else:
            # Create new policy
            policy = Policy(
                id=uuid.uuid4(),
                control_group_id=group_id,
                product_type=product_type,
                policy_type=policy_type,
                document_id=parsed.document_id,
                title=parsed.title,
                file_path=rel_path,
                content_hash=parsed.content_hash,
                word_count=parsed.word_count,
                requirements_count=len(requirements),
                last_parsed=datetime.now(timezone.utc),
                metadata_=parsed.metadata,
                language=language,
            )
            self.db.add(policy)
            self.db.flush()

        # Insert requirements
        for i, req in enumerate(requirements):
            self.db.add(
                Requirement(
                    id=uuid.uuid4(),
                    policy_id=policy.id,
                    control_group_id=group_id,
                    requirement_text=req["text"],
                    section_heading=req["section"],
                    requirement_type=req["type"],
                    domain_area=req.get("domain"),
                    sort_order=i,
                    compliance_status=ComplianceStatus.NOT_ASSESSED,
                    evidence_count=0,
                    metadata_={},
                )
            )

        stats["policies_imported"] += 1
        stats["requirements_extracted"] += len(requirements)

        # Index into OpenSearch (graceful — won't fail import if OS is down)
        group_name = self._get_group_name(group_id)
        search_service.index_policy(
            document_id=parsed.document_id,
            title=parsed.title,
            policy_type=policy_type.value,
            product_type=product_type.value,
            control_group_code=parsed.group_code,
            control_group_name=group_name or "",
            sections=[
                {"heading": s.heading, "body": s.body, "level": s.level}
                for s in parsed.sections
            ],
            requirements=[
                {"text": r["text"], "type": r["type"], "section": r["section"]}
                for r in requirements
            ],
            word_count=parsed.word_count,
            language=language,
            metadata=parsed.metadata,
        )

        logger.info(
            "Imported %s: %s (%d requirements)",
            parsed.document_id,
            parsed.title,
            len(requirements),
        )

    # ------------------------------------------------------------------
    # Requirement extraction
    # ------------------------------------------------------------------

    def _extract_requirements(self, parsed: ParsedPolicy) -> list[dict]:
        """Extract shall/should requirements from parsed sections."""
        requirements: list[dict] = []

        for section in parsed.sections:
            # Skip boilerplate sections
            if section.heading.lower().strip() in _SKIP_SECTIONS:
                continue

            # Split section body into sentences
            sentences = self._split_sentences(section.body)

            for sentence in sentences:
                sentence = sentence.strip()
                if len(sentence) < 10:
                    continue

                has_shall = bool(_SHALL_RE.search(sentence))
                has_should = bool(_SHOULD_RE.search(sentence))

                if has_shall:
                    requirements.append(
                        {
                            "text": sentence,
                            "section": section.heading,
                            "type": "mandatory",
                            "domain": self._infer_domain(section.heading),
                        }
                    )
                elif has_should:
                    requirements.append(
                        {
                            "text": sentence,
                            "section": section.heading,
                            "type": "recommended",
                            "domain": self._infer_domain(section.heading),
                        }
                    )

        return requirements

    @staticmethod
    def _split_sentences(text: str) -> list[str]:
        """Split text into sentences, handling bullets and paragraphs."""
        # First, split on bullet points
        bullets = _BULLET_RE.split(text)

        sentences: list[str] = []
        for chunk in bullets:
            chunk = chunk.strip()
            if not chunk:
                continue
            # Split on sentence boundaries
            parts = _SENTENCE_RE.split(chunk)
            sentences.extend(parts)

        return sentences

    @staticmethod
    def _infer_domain(heading: str) -> str | None:
        """Infer a domain area from section heading."""
        heading_lower = heading.lower()

        domain_keywords = {
            "access": "Access Control",
            "authentication": "Access Control",
            "identity": "Access Control",
            "encryption": "Cryptography",
            "cryptograph": "Cryptography",
            "incident": "Incident Management",
            "logging": "Logging & Monitoring",
            "monitor": "Logging & Monitoring",
            "network": "Network Security",
            "physical": "Physical Security",
            "supplier": "Supplier Management",
            "third party": "Supplier Management",
            "backup": "Business Continuity",
            "continuity": "Business Continuity",
            "disaster": "Business Continuity",
            "privacy": "Privacy & Data Protection",
            "personal data": "Privacy & Data Protection",
            "classification": "Information Classification",
            "training": "Awareness & Training",
            "awareness": "Awareness & Training",
            "development": "Secure Development",
            "testing": "Secure Development",
            "vulnerability": "Vulnerability Management",
            "patch": "Vulnerability Management",
            "asset": "Asset Management",
            "compliance": "Compliance",
            "audit": "Compliance",
        }

        for keyword, domain in domain_keywords.items():
            if keyword in heading_lower:
                return domain

        return None

    # Control group resolution, DataLoadHistory tracking, and parser setup
    # are inherited from BaseImporter.
