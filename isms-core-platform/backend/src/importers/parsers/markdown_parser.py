"""Markdown policy parser — primary format for ISMS CORE policies."""

import logging
import re
from pathlib import Path

from src.importers.parsers.base import (
    BasePolicyParser,
    ParsedPolicy,
    Section,
    compute_content_hash,
    derive_group_code,
    detect_product_and_type,
)

logger = logging.getLogger(__name__)

# Regex patterns
_HEADING_RE = re.compile(r"^(#{1,4})\s+(.+)$", re.MULTILINE)
_DOC_ID_BOLD_RE = re.compile(r"\*\*(ISMS-(?:OP-)?(?:INS-)?(?:POL|REF|CTX|FORM|IMP)-[A-Za-z0-9][\w.\-]+)\b")
_DOC_ID_PLAIN_RE = re.compile(r"(ISMS-(?:OP-)?(?:INS-)?(?:POL|REF|CTX|FORM|IMP)-[A-Za-z0-9][\w.\-]+)")

# Watermark pattern: <!-- ISMS-CORE:{tag}:{doc_id}:{product}:{type}:{group_code} -->
# Tags: POLICY (for POL/OP-POL), INS, REF, CTX, FORM
_WATERMARK_RE = re.compile(
    r"^<!-- ISMS-CORE:(?:POLICY|INS|REF|CTX|FORM|IMP):([^:]+):([^:]+):([^:]+):([^ ]+) -->",
    re.MULTILINE,
)

# Document Control table field patterns
_TABLE_FIELD_RE = re.compile(
    r"\|\s*\*?\*?(?:Document\s+)?(\w[\w\s]*?)\*?\*?\s*\|\s*(.+?)\s*\|"
)


class MarkdownPolicyParser(BasePolicyParser):
    """Parses ISMS CORE Markdown policy files (.md)."""

    def supported_extensions(self) -> list[str]:
        return [".md"]

    def parse(self, file_path: Path) -> ParsedPolicy:
        raw_bytes = file_path.read_bytes()
        text = raw_bytes.decode("utf-8", errors="replace")
        content_hash = compute_content_hash(file_path)

        # Try watermark first (most reliable — injected by factory script)
        wm = _WATERMARK_RE.search(text[:300])
        if wm:
            document_id = wm.group(1)
            product_type = wm.group(2)
            policy_type = wm.group(3)
            group_code = wm.group(4)
            logger.debug("Watermark hit: %s", document_id)
        else:
            # Fallback: extract from content
            document_id = self._extract_document_id(text, file_path)
            product_type, policy_type = detect_product_and_type(document_id)
            group_code = derive_group_code(document_id)

        # Strip watermark line for content parsing (title, metadata, sections)
        content = _WATERMARK_RE.sub("", text).lstrip("\n") if wm else text

        title = self._extract_title(content, document_id)
        metadata = self._extract_metadata(content)
        sections = self._extract_sections(content)
        word_count = len(content.split())

        return ParsedPolicy(
            document_id=document_id,
            title=title,
            product_type=product_type,
            policy_type=policy_type,
            group_code=group_code,
            content_hash=content_hash,
            word_count=word_count,
            sections=sections,
            metadata=metadata,
        )

    def _extract_document_id(self, text: str, file_path: Path) -> str:
        """Extract document ID from first line bold pattern or filename."""
        # Try bold pattern first (e.g. **ISMS-POL-A.5.24-28 — Title**)
        first_lines = text[:500]
        m = _DOC_ID_BOLD_RE.search(first_lines)
        if m:
            return self._clean_doc_id(m.group(1))

        # Try plain text pattern
        m = _DOC_ID_PLAIN_RE.search(first_lines)
        if m:
            return self._clean_doc_id(m.group(1))

        # Fallback: derive from filename
        stem = file_path.stem
        m = _DOC_ID_PLAIN_RE.search(stem)
        if m:
            return self._clean_doc_id(m.group(1))

        raise ValueError(f"Cannot extract document_id from {file_path}")

    @staticmethod
    def _clean_doc_id(raw: str) -> str:
        """Clean trailing punctuation from a document ID."""
        return raw.rstrip(" \t—-–:*")

    def _extract_title(self, text: str, document_id: str) -> str:
        """Extract policy title from first line or Document Control table."""
        first_line = text.split("\n", 1)[0].strip()

        # Try: **ISMS-POL-A.5.24-28 — Title** / **ISMS-POL-A.5.31.1: Title**
        # Split using document_id as the anchor so hyphens within the ID are never
        # mistaken for the title separator (e.g. "ISMS-POL-A.5.8 - Title" must not
        # split at the first "-" inside "ISMS-POL").
        doc_id_base = document_id.rsplit("-", 1)[0]  # ISMS-POL-00-DE → ISMS-POL-00
        clean_line = first_line.strip("*").strip()
        for id_prefix in [document_id, doc_id_base]:
            if not clean_line.startswith(id_prefix):
                continue
            remainder = clean_line[len(id_prefix):]
            for sep in [" — ", " – ", " - ", ": ", "—", "–", "-", ":"]:
                if remainder.startswith(sep):
                    title = remainder[len(sep):].strip().strip("*").strip()
                    if title:
                        return title

        # Try Document Control table (English and German field names)
        _TITLE_FIELDS = {"title", "document title", "dokumenttitel", "titre", "titolo"}
        for match in _TABLE_FIELD_RE.finditer(text[:2000]):
            field_name = match.group(1).strip().lower()
            if field_name in _TITLE_FIELDS:
                return match.group(2).strip()

        # Fallback: first non-boilerplate heading (skip "Document Control" etc.)
        _SKIP_HEADINGS = {"document control", "dokumentkontrolle", "contrôle de document"}
        for m in _HEADING_RE.finditer(text):
            heading = m.group(2).strip()
            if heading.lower() not in _SKIP_HEADINGS:
                return heading

        return document_id

    def _extract_metadata(self, text: str) -> dict:
        """Extract Document Control table fields into a metadata dict."""
        metadata = {}
        # Only search the first ~2000 chars (Document Control is near the top)
        header_block = text[:2000]

        field_map = {
            "document id": "document_id",
            "document title": "title",
            "document type": "document_type",
            "document creator": "creator",
            "document owner": "owner",
            "approved by": "approved_by",
            "created date": "created_date",
            "version": "version",
            "version date": "version_date",
            "classification": "classification",
            "status": "status",
        }

        for match in _TABLE_FIELD_RE.finditer(header_block):
            field_name = match.group(1).strip().lower()
            field_value = match.group(2).strip()
            key = field_map.get(field_name)
            if key:
                metadata[key] = field_value

        return metadata

    def _extract_sections(self, text: str) -> list[Section]:
        """Split document into heading + body sections."""
        sections: list[Section] = []
        matches = list(_HEADING_RE.finditer(text))

        if not matches:
            # No headings — treat entire document as one section
            return [Section(heading="(document)", body=text.strip(), level=0)]

        # Content before first heading
        pre = text[: matches[0].start()].strip()
        if pre:
            sections.append(Section(heading="(preamble)", body=pre, level=0))

        for i, m in enumerate(matches):
            level = len(m.group(1))
            heading = m.group(2).strip()
            start = m.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            body = text[start:end].strip()
            sections.append(Section(heading=heading, body=body, level=level))

        return sections
