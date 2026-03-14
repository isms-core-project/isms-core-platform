"""PDF policy parser — extracts text from PDF policy documents."""

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

_DOC_ID_RE = re.compile(r"(ISMS-(?:OP-)?POL-[A-Za-z0-9][\w.\-]+)")
_HEADING_RE = re.compile(r"^(#{1,4})\s+(.+)$", re.MULTILINE)
# Heuristic for PDF headings: short lines in title case or ALL CAPS
_PDF_HEADING_RE = re.compile(r"^([A-Z][A-Za-z\s&,\-–—:]{3,80})$", re.MULTILINE)


class PdfPolicyParser(BasePolicyParser):
    """Parses policy documents from PDF files using pdfplumber."""

    def supported_extensions(self) -> list[str]:
        return [".pdf"]

    def parse(self, file_path: Path) -> ParsedPolicy:
        import pdfplumber

        content_hash = compute_content_hash(file_path)

        # Extract text from all pages
        pages_text = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    pages_text.append(page_text)

        full_text = "\n\n".join(pages_text)
        if not full_text.strip():
            raise ValueError(f"No text extracted from PDF: {file_path}")

        document_id = self._extract_document_id(full_text, file_path)
        product_type, policy_type = detect_product_and_type(document_id)
        group_code = derive_group_code(document_id)
        title = self._extract_title(full_text, document_id)
        sections = self._extract_sections(full_text)
        word_count = len(full_text.split())

        return ParsedPolicy(
            document_id=document_id,
            title=title,
            product_type=product_type,
            policy_type=policy_type,
            group_code=group_code,
            content_hash=content_hash,
            word_count=word_count,
            sections=sections,
            metadata={"source_format": "pdf", "pages": len(pages_text)},
        )

    def _extract_document_id(self, text: str, file_path: Path) -> str:
        """Find ISMS document ID in the extracted text or filename."""
        m = _DOC_ID_RE.search(text[:1000])
        if m:
            return m.group(1).rstrip(" \t—-–:*")

        m = _DOC_ID_RE.search(file_path.stem)
        if m:
            return m.group(1).rstrip(" \t—-–:*")

        raise ValueError(f"Cannot extract document_id from PDF: {file_path}")

    def _extract_title(self, text: str, document_id: str) -> str:
        """Extract title from the text near the document ID."""
        # Look for text after the document ID on the same or next line
        idx = text.find(document_id)
        if idx >= 0:
            after = text[idx + len(document_id) : idx + len(document_id) + 200]
            for sep in ["—", "–", "-", ":"]:
                if sep in after:
                    title = after.split(sep, 1)[1].strip().split("\n", 1)[0].strip()
                    if title:
                        return title
        return document_id

    def _extract_sections(self, text: str) -> list[Section]:
        """Split PDF text into sections using heading heuristics."""
        # Try markdown-style headings first (some PDF extractors preserve them)
        md_matches = list(_HEADING_RE.finditer(text))
        if md_matches:
            return self._sections_from_matches(text, md_matches, use_level=True)

        # Fallback: heuristic heading detection (title case lines)
        heuristic_matches = list(_PDF_HEADING_RE.finditer(text))
        if heuristic_matches:
            return self._sections_from_matches(text, heuristic_matches, use_level=False)

        # No headings detected — single section
        return [Section(heading="(document)", body=text.strip(), level=0)]

    @staticmethod
    def _sections_from_matches(
        text: str, matches: list[re.Match], use_level: bool
    ) -> list[Section]:
        sections: list[Section] = []

        pre = text[: matches[0].start()].strip()
        if pre:
            sections.append(Section(heading="(preamble)", body=pre, level=0))

        for i, m in enumerate(matches):
            if use_level:
                level = len(m.group(1))
                heading = m.group(2).strip()
            else:
                level = 1
                heading = m.group(1).strip()

            start = m.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            body = text[start:end].strip()
            sections.append(Section(heading=heading, body=body, level=level))

        return sections
