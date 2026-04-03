"""ISO Reference Corpus Extractor.

Extracts and chunks normative text from ISO/regulatory PDFs and TXT files
in the iso-reference directory tree. Produces structured chunks keyed by
clause/control ID for indexing into OpenSearch iso-reference index.

Supports:
- ISO 27001:2022 / 27002:2022 — control-level chunking (5.1, 5.2 … 8.34)
- ISO 27701:2025, 27018:2025  — section-level chunking
- NIST CSF 2.0 (TXT)          — function/category chunking
- BSI 200-x, EU Acts, others  — page-level chunking with section headers
"""

import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Standard name inference from filename / directory
# ---------------------------------------------------------------------------

_FILENAME_TO_STANDARD: list[tuple[re.Pattern, str]] = [
    (re.compile(r"27001.*2022.*amd", re.I),   "ISO 27001:2022+Amd1"),
    (re.compile(r"27001.*2022",       re.I),   "ISO 27001:2022"),
    (re.compile(r"27002.*2022",       re.I),   "ISO 27002:2022"),
    (re.compile(r"27018.*2025",       re.I),   "ISO 27018:2025"),
    (re.compile(r"27701.*2025",       re.I),   "ISO 27701:2025"),
    (re.compile(r"27000.*2018",       re.I),   "ISO 27000:2018"),
    (re.compile(r"27017",             re.I),   "ISO 27017"),
    (re.compile(r"nist.*csf.*2\.0|csf.*2\.0|nist.*cybersecurity.*framework.*2", re.I), "NIST CSF 2.0"),
    (re.compile(r"800-53",            re.I),   "NIST SP 800-53r5"),
    (re.compile(r"800-30",            re.I),   "NIST SP 800-30r1"),
    (re.compile(r"800-37",            re.I),   "NIST SP 800-37r2"),
    (re.compile(r"800-61",            re.I),   "NIST SP 800-61r3"),
    (re.compile(r"bsi.*2001",         re.I),   "BSI 200-1"),
    (re.compile(r"bsi.*2002",         re.I),   "BSI 200-2"),
    (re.compile(r"bsi.*2003",         re.I),   "BSI 200-3"),
    (re.compile(r"basic.*security",   re.I),   "BSI Basic Security"),
    (re.compile(r"OJ_L_202401689",    re.I),   "EU AI Act"),
    (re.compile(r"AI.Act",            re.I),   "EU AI Act"),
    (re.compile(r"Cloud.Sovereignty", re.I),   "EU Cloud Sovereignty"),
    (re.compile(r"CSRM.*2025",        re.I),   "CSRM 2025"),
    (re.compile(r"Methode.CSRM",      re.I),   "CSRM 2025"),
    (re.compile(r"fedlex.*nDSG|revDSG|cc-2022-491", re.I), "Swiss nDSG"),
    (re.compile(r"controlli.*sicurezza|27017.*27018", re.I), "ISO Cloud Security Summary"),
]

# Standards for which we do control-level chunking
_ISO_27002_LIKE = {"ISO 27001:2022", "ISO 27002:2022", "ISO 27001:2022+Amd1"}
_ISO_STRUCTURED  = {"ISO 27701:2025", "ISO 27018:2025", "ISO 27017"}


def infer_standard(path: Path) -> str:
    name = path.name
    # Also try parent directory name for context
    context = f"{path.parent.name}/{name}"
    for pattern, standard in _FILENAME_TO_STANDARD:
        if pattern.search(context):
            return standard
    return path.stem.replace("_", " ").replace("-", " ")


# ---------------------------------------------------------------------------
# ISO 27001/27002 control-level chunker
# ---------------------------------------------------------------------------

# Matches headings like "5.1 Policies for information security"
# or "A.5.1.1 Policies for information security" (Amendment style)
_ISO_CTRL_HEADING = re.compile(
    r"^\s*(?:A\.)?(\d+)\.(\d+)(?:\.(\d+))?\s{1,6}([A-Z][^\n]{3,80})\s*$",
    re.MULTILINE,
)

# ISO 27001 clause headings (4 through 10 + Annex A)
_ISO_CLAUSE_HEADING = re.compile(
    r"^\s*((?:\d+|Annex\s+A)(?:\.\d+)*)\s{1,6}([A-Z][^\n]{3,80})\s*$",
    re.MULTILINE,
)


def _normalise_control_id(major: str, minor: str, patch: str | None = None) -> str:
    """Convert ISO control number to group_code style: 5.1 → a.5.1"""
    if patch:
        return f"a.{major}.{minor}.{patch}"
    return f"a.{major}.{minor}"


def _chunk_iso_27002(text: str, standard: str) -> list[dict]:
    """Chunk ISO 27002-style document by control number boundaries."""
    chunks: list[dict] = []
    matches = list(_ISO_CTRL_HEADING.finditer(text))

    if len(matches) < 5:
        # Not enough control headings found — fall back to page chunking
        logger.warning("%s: too few control headings (%d), falling back to page chunking", standard, len(matches))
        return _chunk_by_pages(text, standard)

    for i, m in enumerate(matches):
        major, minor, patch, title = m.group(1), m.group(2), m.group(3), m.group(4).strip()
        clause_id = _normalise_control_id(major, minor, patch)

        start = m.end()
        end   = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body  = text[start:end].strip()

        # Skip very short fragments (likely TOC entries)
        if len(body) < 80:
            continue

        chunks.append({
            "clause_id": clause_id,
            "title":     title,
            "text":      f"{title}\n\n{body}",
            "standard":  standard,
            "language":  "en",
        })

    logger.info("%s: extracted %d control chunks", standard, len(chunks))
    return chunks


# ---------------------------------------------------------------------------
# Section-level chunker for other structured ISOs (27701, 27018)
# ---------------------------------------------------------------------------

_SECTION_HEADING = re.compile(
    r"^\s*(\d+(?:\.\d+){1,3})\s{1,6}([A-Z][^\n]{3,80})\s*$",
    re.MULTILINE,
)


def _chunk_by_sections(text: str, standard: str) -> list[dict]:
    """Chunk by numbered section headings."""
    chunks: list[dict] = []
    matches = list(_SECTION_HEADING.finditer(text))

    if len(matches) < 3:
        return _chunk_by_pages(text, standard)

    for i, m in enumerate(matches):
        section_id = m.group(1).strip()
        title      = m.group(2).strip()
        start      = m.end()
        end        = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body       = text[start:end].strip()

        if len(body) < 80:
            continue

        chunks.append({
            "clause_id": section_id,
            "title":     title,
            "text":      f"{title}\n\n{body}",
            "standard":  standard,
            "language":  "en",
        })

    logger.info("%s: extracted %d section chunks", standard, len(chunks))
    return chunks


# ---------------------------------------------------------------------------
# Page-level chunker (fallback)
# ---------------------------------------------------------------------------

_PAGE_SIZE = 1200   # characters per chunk
_PAGE_OVERLAP = 150


def _chunk_by_pages(text: str, standard: str) -> list[dict]:
    """Split text into fixed-size overlapping windows."""
    chunks: list[dict] = []
    start = 0
    idx   = 0
    while start < len(text):
        end  = min(start + _PAGE_SIZE, len(text))
        body = text[start:end].strip()
        if len(body) > 100:
            chunks.append({
                "clause_id": f"chunk-{idx:04d}",
                "title":     f"{standard} — section {idx + 1}",
                "text":      body,
                "standard":  standard,
                "language":  "en",
            })
            idx += 1
        start = end - _PAGE_OVERLAP

    logger.info("%s: extracted %d page chunks", standard, len(chunks))
    return chunks


# ---------------------------------------------------------------------------
# NIST CSF 2.0 TXT chunker
# ---------------------------------------------------------------------------

# NIST CSF 2.0 TXT has lines like:
# "GOVERN (GV)" and "GV.OC: Organizational Context" and sub-entries
_NIST_FUNCTION = re.compile(r"^([A-Z]{2,7})\s*\(([A-Z]{2,3})\)\s*$", re.MULTILINE)
_NIST_CATEGORY = re.compile(r"^([A-Z]{2,3}\.[A-Z]{2,4}):\s+(.+)$", re.MULTILINE)


def _chunk_nist_csf_txt(text: str) -> list[dict]:
    """Chunk NIST CSF 2.0 TXT by category."""
    chunks: list[dict] = []
    matches = list(_NIST_CATEGORY.finditer(text))

    if len(matches) < 5:
        return _chunk_by_pages(text, "NIST CSF 2.0")

    for i, m in enumerate(matches):
        cat_id = m.group(1)
        title  = m.group(2).strip()
        start  = m.end()
        end    = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body   = text[start:end].strip()

        if len(body) < 40:
            body = title

        chunks.append({
            "clause_id": cat_id,
            "title":     title,
            "text":      f"{cat_id}: {title}\n\n{body}",
            "standard":  "NIST CSF 2.0",
            "language":  "en",
        })

    logger.info("NIST CSF 2.0: extracted %d category chunks", len(chunks))
    return chunks


# ---------------------------------------------------------------------------
# PDF / TXT extraction
# ---------------------------------------------------------------------------


def _extract_text_from_pdf(path: Path) -> str:
    """Extract full text from PDF using pdfplumber."""
    try:
        import pdfplumber  # type: ignore
    except ImportError:
        logger.error("pdfplumber not installed")
        return ""

    pages: list[str] = []
    try:
        with pdfplumber.open(str(path)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    pages.append(page_text)
    except Exception as e:
        logger.warning("Failed to extract PDF %s: %s", path.name, e)
        return ""

    return "\n\n".join(pages)


def _extract_text_from_txt(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        logger.warning("Failed to read TXT %s: %s", path.name, e)
        return ""


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def extract_chunks(path: Path) -> list[dict]:
    """Extract and chunk a single ISO/regulatory document.

    Returns list of dicts: {clause_id, title, text, standard, language}
    Empty list on failure or unsupported format.
    """
    suffix = path.suffix.lower()
    standard = infer_standard(path)

    if suffix == ".txt":
        text = _extract_text_from_txt(path)
        if "NIST CSF" in standard:
            return _chunk_nist_csf_txt(text)
        return _chunk_by_sections(text, standard)

    if suffix == ".pdf":
        text = _extract_text_from_pdf(path)
        if not text.strip():
            logger.warning("Empty text extracted from %s — skipping", path.name)
            return []

        if standard in _ISO_27002_LIKE:
            return _chunk_iso_27002(text, standard)
        if standard in _ISO_STRUCTURED:
            return _chunk_by_sections(text, standard)
        return _chunk_by_pages(text, standard)

    logger.debug("Unsupported file type: %s", path.suffix)
    return []


def discover_documents(root: Path) -> list[Path]:
    """Recursively find all PDF and TXT files under root, excluding irrelevant files."""
    _SKIP_PATTERNS = {
        "profile", "template", "flowchart", "checklist",
        "appendix", "annex-only", "compressed", "anwalt",
    }
    paths: list[Path] = []
    for p in sorted(root.rglob("*")):
        if p.suffix.lower() not in {".pdf", ".txt"}:
            continue
        if p.stat().st_size < 10_000:   # skip tiny files (< 10 KB)
            continue
        name_lower = p.name.lower()
        if any(skip in name_lower for skip in _SKIP_PATTERNS):
            continue
        paths.append(p)
    return paths
