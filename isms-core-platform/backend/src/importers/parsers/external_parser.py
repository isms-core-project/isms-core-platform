"""Relaxed parser for external / third-party documents.

Handles MD, PDF, DOCX without requiring ISMS CORE watermarks or ID format.
group_code, source_label, and language are supplied by the caller (not derived
from the document itself).

document_id is generated as: EXT-{group_code}-{stem_slug}
  e.g. EXT-a.5.1-acme-information-security-policy
"""

import logging
import re
import unicodedata
from pathlib import Path

from src.importers.parsers.base import (
    BasePolicyParser,
    ParsedPolicy,
    Section,
    compute_content_hash,
)

logger = logging.getLogger(__name__)

_HEADING_RE = re.compile(r"^(#{1,4})\s+(.+)$", re.MULTILINE)
_PDF_HEADING_RE = re.compile(r"^([A-Z][A-Za-z\s&,\-–—:]{3,80})$", re.MULTILINE)


def _slugify(text: str, max_len: int = 60) -> str:
    """Convert text to a URL-safe lowercase slug."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:max_len].strip("-")


def _extract_sections_from_text(text: str) -> list[Section]:
    """Extract heading/body sections — handles markdown headings first, then PDF heuristic."""
    md_matches = list(_HEADING_RE.finditer(text))
    if md_matches:
        sections: list[Section] = []
        pre = text[: md_matches[0].start()].strip()
        if pre:
            sections.append(Section(heading="(preamble)", body=pre, level=0))
        for i, m in enumerate(md_matches):
            start = m.end()
            end = md_matches[i + 1].start() if i + 1 < len(md_matches) else len(text)
            sections.append(Section(
                heading=m.group(2).strip(),
                body=text[start:end].strip(),
                level=len(m.group(1)),
            ))
        return sections

    pdf_matches = list(_PDF_HEADING_RE.finditer(text))
    if pdf_matches:
        sections = []
        pre = text[: pdf_matches[0].start()].strip()
        if pre:
            sections.append(Section(heading="(preamble)", body=pre, level=0))
        for i, m in enumerate(pdf_matches):
            start = m.end()
            end = pdf_matches[i + 1].start() if i + 1 < len(pdf_matches) else len(text)
            sections.append(Section(heading=m.group(1).strip(), body=text[start:end].strip(), level=1))
        return sections

    return [Section(heading="(document)", body=text.strip(), level=0)]


def _extract_title_from_text(text: str, fallback: str) -> str:
    """Best-effort title from first heading or first non-empty line."""
    m = _HEADING_RE.search(text[:2000])
    if m:
        return m.group(2).strip()

    for line in text.splitlines():
        line = line.strip().strip("*#_").strip()
        if len(line) > 4:
            return line[:200]

    return fallback


class ExternalDocParser:
    """Relaxed parser for third-party documents (MD / PDF / DOCX).

    group_code, source_label, and language are injected by the caller —
    they are NOT derived from the document content.
    """

    def parse(
        self,
        file_path: Path,
        group_code: str,
        source_label: str,
        language: str = "en",
    ) -> ParsedPolicy:
        ext = file_path.suffix.lower()
        if ext == ".md":
            text = self._read_md(file_path)
        elif ext == ".pdf":
            text = self._read_pdf(file_path)
        elif ext in (".docx", ".doc"):
            text = self._read_docx(file_path)
        else:
            raise ValueError(f"Unsupported file type for external import: {ext}")

        content_hash = compute_content_hash(file_path)
        title = _extract_title_from_text(text, file_path.stem)
        slug = _slugify(title)
        document_id = f"EXT-{group_code}-{slug}"[:120]
        sections = _extract_sections_from_text(text)
        word_count = len(text.split())

        return ParsedPolicy(
            document_id=document_id,
            title=title,
            product_type="external",
            policy_type="POL",
            group_code=group_code,
            content_hash=content_hash,
            word_count=word_count,
            sections=sections,
            metadata={"source_format": ext.lstrip("."), "source_file": file_path.name},
            language=language,
            source_label=source_label,
        )

    @staticmethod
    def _read_md(file_path: Path) -> str:
        return file_path.read_bytes().decode("utf-8", errors="replace")

    @staticmethod
    def _read_pdf(file_path: Path) -> str:
        import pdfplumber
        pages = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    pages.append(t)
        text = "\n\n".join(pages)
        if not text.strip():
            raise ValueError(f"No text extracted from PDF: {file_path}")
        return text

    @staticmethod
    def _read_docx(file_path: Path) -> str:
        from docx import Document
        doc = Document(str(file_path))
        paragraphs = []
        for para in doc.paragraphs:
            if para.text.strip():
                # Preserve heading levels as markdown
                if para.style.name.startswith("Heading"):
                    try:
                        level = int(para.style.name.split()[-1])
                    except ValueError:
                        level = 1
                    paragraphs.append(f"{'#' * level} {para.text.strip()}")
                else:
                    paragraphs.append(para.text.strip())
        return "\n\n".join(paragraphs)
