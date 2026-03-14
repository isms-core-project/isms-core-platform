"""External document importer — Phase 6.

Handles single-file upload of third-party / non-ISMS CORE policies.
Caller supplies: file_path, group_code, source_label, language.
The document is stored with product_type=EXTERNAL and indexed in OpenSearch.
"""

import logging
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.database.enums import ComplianceStatus, PolicyType, ProductType
from src.domain.content import Policy, Requirement
from src.domain.control_groups import ControlGroup
from src.importers.parsers.external_parser import ExternalDocParser
from src.services import search_service

logger = logging.getLogger(__name__)

_SENTENCE_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")
_BULLET_RE = re.compile(r"^\s*[-*]\s+", re.MULTILINE)
_SHALL_RE = re.compile(r"\bshall\b", re.IGNORECASE)
_SHOULD_RE = re.compile(r"\bshould\b", re.IGNORECASE)

SUPPORTED_EXTENSIONS = {".md", ".pdf", ".docx", ".doc"}


class ExternalDocImporter:
    """Imports a single external document into policies + requirements tables."""

    def __init__(self, db: DBSession):
        self.db = db
        self.parser = ExternalDocParser()

    def import_file(
        self,
        file_path: Path,
        group_code: str,
        source_label: str,
        language: str = "en",
    ) -> dict:
        """Parse and import one external document. Returns stats dict."""
        ext = file_path.suffix.lower()
        if ext not in SUPPORTED_EXTENSIONS:
            raise ValueError(f"Unsupported file type: {ext}. Supported: {', '.join(SUPPORTED_EXTENSIONS)}")

        # Resolve control group
        group_id = self._resolve_group(group_code)
        if not group_id:
            raise ValueError(f"Control group not found: {group_code}")

        # Parse
        parsed = self.parser.parse(
            file_path,
            group_code=group_code,
            source_label=source_label,
            language=language,
        )

        # Ensure document_id is unique — append suffix if collision
        parsed.document_id = self._ensure_unique_doc_id(parsed.document_id)

        # Extract requirements
        requirements = self._extract_requirements(parsed)

        # Upsert policy
        existing = self.db.execute(
            select(Policy).where(Policy.document_id == parsed.document_id)
        ).scalar_one_or_none()

        now = datetime.now(timezone.utc)

        if existing:
            existing.title = parsed.title
            existing.control_group_id = group_id
            existing.file_path = str(file_path)
            existing.content_hash = parsed.content_hash
            existing.word_count = parsed.word_count
            existing.requirements_count = len(requirements)
            existing.last_parsed = now
            existing.metadata_ = parsed.metadata
            existing.language = language
            existing.source_label = source_label
            policy = existing
            from sqlalchemy import delete
            self.db.execute(delete(Requirement).where(Requirement.policy_id == policy.id))
            self.db.flush()
        else:
            policy = Policy(
                id=uuid.uuid4(),
                control_group_id=group_id,
                product_type=ProductType.EXTERNAL,
                policy_type=PolicyType.POL,
                document_id=parsed.document_id,
                title=parsed.title,
                file_path=str(file_path),
                content_hash=parsed.content_hash,
                word_count=parsed.word_count,
                requirements_count=len(requirements),
                last_parsed=now,
                metadata_=parsed.metadata,
                language=language,
                source_label=source_label,
            )
            self.db.add(policy)
            self.db.flush()

        # Insert requirements
        for i, req in enumerate(requirements):
            self.db.add(Requirement(
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
            ))

        self.db.commit()

        # Index into OpenSearch
        group_name = self._get_group_name(group_id) or ""
        try:
            search_service.index_policy(
                document_id=parsed.document_id,
                title=parsed.title,
                policy_type="POL",
                product_type="external",
                control_group_code=group_code,
                control_group_name=group_name,
                sections=[{"heading": s.heading, "body": s.body, "level": s.level} for s in parsed.sections],
                requirements=[{"text": r["text"], "type": r["type"], "section": r["section"]} for r in requirements],
                word_count=parsed.word_count,
                metadata={**parsed.metadata, "source_label": source_label, "language": language},
            )
        except Exception as e:
            logger.warning("ExternalDocImporter: OpenSearch indexing failed: %s", e)

        logger.info(
            "ExternalDocImporter: imported %s (%d words, %d reqs) → group %s",
            parsed.document_id, parsed.word_count, len(requirements), group_code,
        )

        return {
            "document_id": parsed.document_id,
            "title": parsed.title,
            "group_code": group_code,
            "source_label": source_label,
            "language": language,
            "word_count": parsed.word_count,
            "requirements_extracted": len(requirements),
        }

    def _resolve_group(self, group_code: str) -> uuid.UUID | None:
        row = self.db.execute(
            select(ControlGroup.id).where(ControlGroup.group_code == group_code.lower())
        ).scalar_one_or_none()
        return row

    def _get_group_name(self, group_id: uuid.UUID) -> str | None:
        return self.db.execute(
            select(ControlGroup.name).where(ControlGroup.id == group_id)
        ).scalar_one_or_none()

    def _ensure_unique_doc_id(self, doc_id: str) -> str:
        """Append numeric suffix if document_id already exists."""
        existing = self.db.execute(
            select(Policy.document_id).where(Policy.document_id == doc_id)
        ).scalar_one_or_none()
        if not existing:
            return doc_id
        # Try suffix -2, -3, ...
        for i in range(2, 100):
            candidate = f"{doc_id[:115]}-{i}"
            row = self.db.execute(
                select(Policy.document_id).where(Policy.document_id == candidate)
            ).scalar_one_or_none()
            if not row:
                return candidate
        return f"{doc_id[:110]}-{uuid.uuid4().hex[:6]}"

    def _extract_requirements(self, parsed) -> list[dict]:
        """Extract shall/should sentences from sections."""
        requirements = []
        _SKIP = {"(preamble)", "document control", "version history", "definitions"}
        for section in parsed.sections:
            if section.heading.lower() in _SKIP:
                continue
            text = section.body
            # Split into sentences (bullet points + sentence boundaries)
            bullets = [b.strip() for b in _BULLET_RE.split(text) if b.strip()]
            sentences = []
            for chunk in bullets:
                sentences.extend(s.strip() for s in _SENTENCE_RE.split(chunk) if s.strip())

            for sentence in sentences:
                if _SHALL_RE.search(sentence):
                    req_type = "mandatory"
                elif _SHOULD_RE.search(sentence):
                    req_type = "recommended"
                else:
                    continue
                if len(sentence) < 20:
                    continue
                requirements.append({
                    "text": sentence[:2000],
                    "type": req_type,
                    "section": section.heading,
                    "domain": None,
                })
        return requirements
