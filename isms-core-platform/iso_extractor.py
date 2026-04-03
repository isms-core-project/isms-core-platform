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
    (re.compile(r"standard.?100",     re.I),   "BSI 100-4"),
    (re.compile(r"basic.*security",   re.I),   "BSI Basic Security"),
    (re.compile(r"vergleich.*manage", re.I),   "BSI Management System Comparison"),
    (re.compile(r"27001.*auflistung|auflistung.*controls", re.I), "ISO 27001 Controls Listing"),
    (re.compile(r"rosenthal",         re.I),   "M365 Security Guide (Rosenthal)"),
    (re.compile(r"eng.*def.*sys",     re.I),   "Engineering Defensive Systems 2022"),
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
        if end >= len(text):
            break  # avoid infinite loop when overlap would repeat the same window
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


_MAX_PAGES        = 200   # cap per document
_MIN_TEXT_RATIO   = 0.05  # if <5% of pages yield text → likely scanned, skip
_PDF_TIMEOUT_SECS = 45    # per-file wall-clock timeout


def _extract_text_from_pdf(path: Path) -> str:
    """Extract full text from a PDF using a three-engine fallback chain.

    1. PyMuPDF (fitz)  — fast, low-memory, handles most PDFs
    2. pypdf            — pure Python, no C crashes, tolerant of bad structure
    3. Ghostscript      — separate parser, handles what MuPDF/Poppler cannot

    Each engine is tried in order; if one raises or produces no text, the next
    is attempted. Falls back to pdfplumber subprocess if nothing else works.
    """
    text = _try_pymupdf(path)
    if text:
        return text

    logger.debug("PyMuPDF yielded nothing for %s — trying pypdf", path.name)
    text = _try_pypdf(path)
    if text:
        return text

    logger.debug("pypdf yielded nothing for %s — trying ghostscript", path.name)
    text = _try_ghostscript(path)
    if text:
        return text

    logger.warning("All PDF engines failed for %s", path.name)
    return ""


def _try_pymupdf(path: Path) -> str:
    try:
        import fitz  # type: ignore
        doc = fitz.open(str(path))
        total_pages = len(doc)
        pages: list[str] = []
        for i in range(min(total_pages, _MAX_PAGES)):
            page = doc[i]
            t = page.get_text("text")
            if t and len(t.strip()) > 20:
                pages.append(t.strip())
            page = None
        doc.close()
        if total_pages > 5 and pages and len(pages) / min(total_pages, _MAX_PAGES) < _MIN_TEXT_RATIO:
            return ""
        return "\n\n".join(pages)
    except Exception as e:
        logger.debug("PyMuPDF error on %s: %s", path.name, e)
        return ""


def _try_pypdf(path: Path) -> str:
    try:
        from pypdf import PdfReader  # type: ignore
        reader = PdfReader(str(path))
        pages: list[str] = []
        for page in reader.pages[:_MAX_PAGES]:
            t = page.extract_text() or ""
            if len(t.strip()) > 20:
                pages.append(t.strip())
        return "\n\n".join(pages)
    except Exception as e:
        logger.debug("pypdf error on %s: %s", path.name, e)
        return ""


def _try_ghostscript(path: Path) -> str:
    import shutil
    import subprocess
    if not shutil.which("gs"):
        return ""
    try:
        result = subprocess.run(
            ["gs", "-q", "-dNOPAUSE", "-dBATCH", "-dSAFER",
             f"-dLastPage={_MAX_PAGES}",
             "-sDEVICE=txtwrite", "-sOutputFile=-", str(path)],
            capture_output=True, text=True, timeout=_PDF_TIMEOUT_SECS,
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        logger.warning("Ghostscript timed out on %s", path.name)
        return ""
    except Exception as e:
        logger.debug("Ghostscript error on %s: %s", path.name, e)
        return ""


def _extract_with_pdfplumber(path: Path) -> str:
    """Run PDF extraction in an isolated subprocess with a hard timeout.

    Uses stdout pipe with a thread-based reader so we can kill the process
    and still drain the pipe without blocking — avoids the proc.communicate()
    hang that occurs when SIGKILL races with a write to the pipe buffer.
    """
    import json
    import queue
    import subprocess
    import sys
    import threading

    _worker = Path(__file__).parent / "_pdf_extract_worker.py"

    try:
        proc = subprocess.Popen(
            [sys.executable, str(_worker), str(path), str(_MAX_PAGES)],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,  # discard stderr — avoids second pipe deadlock
        )
    except Exception as e:
        logger.warning("Failed to start PDF worker for %s: %s", path.name, e)
        return ""

    # Read stdout in a daemon thread so we can kill proc without blocking
    out_q: queue.Queue = queue.Queue()

    def _reader() -> None:
        try:
            data = proc.stdout.read()  # type: ignore[union-attr]
            out_q.put(data)
        except Exception:
            out_q.put(b"")

    t = threading.Thread(target=_reader, daemon=True)
    t.start()
    t.join(timeout=_PDF_TIMEOUT_SECS)

    if t.is_alive():
        # Timeout — kill the process hard, reader thread will unblock shortly
        proc.kill()
        t.join(timeout=5)
        logger.warning("PDF extraction timed out after %ds: %s", _PDF_TIMEOUT_SECS, path.name)
        return ""

    proc.wait()
    stdout = out_q.get_nowait() if not out_q.empty() else b""

    if not stdout or not stdout.strip():
        return ""

    try:
        data = json.loads(stdout)
    except Exception as e:
        logger.warning("Failed to parse PDF worker output for %s: %s", path.name, e)
        return ""

    pages_out: list[str] = data.get("pages", [])
    total_pages: int      = data.get("total", 0)

    if total_pages > 5 and pages_out and len(pages_out) / min(total_pages, _MAX_PAGES) < _MIN_TEXT_RATIO:
        logger.warning("Skipping likely scanned PDF (%.0f%% text yield): %s",
                       len(pages_out) / min(total_pages, _MAX_PAGES) * 100, path.name)
        return ""

    return "\n\n".join(pages_out)


def _extract_text_from_txt(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        logger.warning("Failed to read TXT %s: %s", path.name, e)
        return ""


def _extract_text_from_docx(path: Path) -> str:
    try:
        from docx import Document  # type: ignore
        doc = Document(str(path))
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n\n".join(paragraphs)
    except Exception as e:
        logger.warning("Failed to read DOCX %s: %s", path.name, e)
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

    if suffix == ".docx":
        text = _extract_text_from_docx(path)
        if not text.strip():
            logger.warning("Empty text extracted from %s — skipping", path.name)
            return []
        if standard in _ISO_27002_LIKE:
            return _chunk_iso_27002(text, standard)
        if standard in _ISO_STRUCTURED:
            return _chunk_by_sections(text, standard)
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
        "basic_security",    # BSI Basic Security — scanned, no extractable text
        "bsi-standard-200",  # BSI 200-1/2/3 — complex typeset, extraction too slow
        "fedlex",            # Swiss nDSG — PDF/A archival format, causes timeout
        "cloud-sovereignty", # EU Cloud Sovereignty — corrupt XObject loop, unusable
        "future-of-life",   # FLI AI Act overview — summary, not normative text
        "methode-csrm",     # CSRM 2025 — hangs every PDF library, corrupt structure
        "vergleich",        # BSI comparison doc — OOM-kills any extraction engine
        "standard_100",     # BSI 100-x series — OOM-kills any extraction engine
        "oj_l_202401689",   # EU AI Act (Official Journal) — 1000+ pages, OOM
        "eng-def-sys",      # Engineering Defence Systems — OOM
        "27001-2023",       # German controls listing — OOM
        "amd_1_2024",       # ISO 27001:2022 Amendment 1 — OOM even with fallback chain
        "c073906",          # Old/corrupt ISO 27000:2018 download — crashes PyMuPDF (bin this file)
        "iso_iec_27000_2018",  # ISO 27000:2018 vocabulary — OOM on extraction → convert via Acrobat
        "pci-dss-v4",       # PCI DSS v4 — OOM on extraction → convert via Acrobat
        "nist.fips",        # NIST FIPS — hangs all engines → convert via Acrobat
        "nist.cswp",        # NIST white papers → convert via Acrobat
        "nist.ir",          # NIST interagency reports → convert via Acrobat
    }
    # PDF-only skip patterns: names of documents that OOM/hang all PDF engines.
    # These are still wanted — TXT/DOCX conversions of the same docs bypass the
    # skip and are processed normally.
    _PDF_SKIP_PATTERNS = _SKIP_PATTERNS

    paths: list[Path] = []
    for p in sorted(root.rglob("*")):
        suffix = p.suffix.lower()
        if suffix not in {".pdf", ".txt", ".docx"}:
            continue
        if p.stat().st_size < 10_000:   # skip tiny files (< 10 KB)
            continue
        name_lower = p.name.lower()
        if suffix == ".pdf" and any(skip in name_lower for skip in _PDF_SKIP_PATTERNS):
            continue
        paths.append(p)
    return paths
