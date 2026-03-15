#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 7.1 — Generator Registry Parser

Reads all 188 QA'd generator scripts from 50-isms-core-framework/**/SCR/generate_*.py
and extracts structured metadata for DB import:

  - document_id, workbook_name, control_id, control_name
  - group_code (parsed from DOCUMENT_ID)
  - domain_number, total_domains (from docstring / DOCUMENT_ID)
  - sheet_names + sheet_types (instructions/input/summary/evidence/approval)
  - stacked_control_ids (for multi-control generators like A.5.1-2-6.1-2)
  - output_filename pattern
  - source_file (relative path)

Output: datasets/data/generator_registry.json

Extraction strategy (in priority order):
  1. Constants block  — DOCUMENT_ID, WORKBOOK_NAME, CONTROL_ID, CONTROL_NAME
  2. Docstring        — "Generated Workbook Structure:" numbered list (sheet names)
  3. Code fallback    — wb.create_sheet("name") and ws.title = "name" patterns
"""

import json
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent  # factory_claude_ai/60-isms-core-api/ → up 2
FRAMEWORK_ROOT = REPO_ROOT.parent / "50-isms-core-framework"
OUTPUT_FILE = SCRIPT_DIR.parent / "data" / "generator_registry.json"

# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------
RE_DOCUMENT_ID = re.compile(r'^DOCUMENT_ID\s*=\s*"([^"]+)"', re.MULTILINE)
RE_WORKBOOK_NAME = re.compile(r'^WORKBOOK_NAME\s*=\s*"([^"]+)"', re.MULTILINE)
RE_CONTROL_ID = re.compile(r'^CONTROL_ID\s*=\s*"([^"]+)"', re.MULTILINE)
RE_CONTROL_NAME = re.compile(r'^CONTROL_NAME\s*=\s*"([^"]+)"', re.MULTILINE)
RE_OUTPUT_FILENAME = re.compile(r'^OUTPUT_FILENAME\s*=\s*(.+)', re.MULTILINE)

# Docstring section: "**Generated Workbook Structure[...]:**" followed by numbered list
# Handles: plain, **bold**, with optional parenthetical (N Sheets) before colon
RE_STRUCTURE_SECTION = re.compile(
    r'\*?\*?Generated Workbook Structure[^:\n]*:\*?\*?\s*\n((?:[ \t]*\d+\.[ \t].+\n?)+)',
    re.IGNORECASE,
)
RE_STRUCTURE_ITEM = re.compile(r'^\s*\d+\.\s+(.+?)(?:\s+-\s+.+)?$')

# Domain line: "Assessment Domain N of M:" in docstring
RE_DOMAIN_LINE = re.compile(
    r'Assessment Domain\s+(\d+)\s+of\s+(\d+)',
    re.IGNORECASE,
)

# Code-level sheet name patterns
# Positional: wb.create_sheet("name") or wb.create_sheet("name", 0)
RE_CREATE_SHEET_NAMED = re.compile(r'wb\.create_sheet\(\s*"([^"]+)"')
# Keyword: wb.create_sheet(title="name")
RE_CREATE_SHEET_TITLE_KW = re.compile(r'wb\.create_sheet\(\s*title\s*=\s*"([^"]+)"')
# ws.title assignment inside sheet creation functions
RE_WS_TITLE = re.compile(r'ws(?:_\w+)?\.title\s*=\s*"([^"]+)"')
# List-of-strings pattern: sheets = ["Name1", "Name2", ...]
# Matches a variable assignment containing a list of quoted strings followed by
# wb.create_sheet(title=<var>) — captures all quoted strings in the list block
RE_SHEET_LIST_BLOCK = re.compile(
    r'(?:sheets|sheet_names|SHEETS)\s*=\s*\[(.*?)\]',
    re.DOTALL,
)
RE_QUOTED_STRING = re.compile(r'"([^"]+)"')

# Standard sheets that appear in every generator — used to fill gaps after docstring parse
STANDARD_SHEETS = {"Instructions & Legend", "Summary Dashboard", "Evidence Register", "Approval Sign-Off"}

# ---------------------------------------------------------------------------
# Sheet type classification
# ---------------------------------------------------------------------------
SHEET_TYPE_MAP = {
    "instructions": "instructions",
    "legend": "instructions",
    "instructions & legend": "instructions",
    "summary dashboard": "summary",
    "summary": "summary",
    "evidence register": "evidence",
    "evidence": "evidence",
    "approval sign-off": "approval",
    "approval": "approval",
    "sign-off": "approval",
}


def classify_sheet(name: str) -> str:
    """Classify sheet name into: instructions / input / summary / evidence / approval."""
    lower = name.lower().strip()
    for key, stype in SHEET_TYPE_MAP.items():
        if key in lower:
            return stype
    return "input"


# ---------------------------------------------------------------------------
# DOCUMENT_ID parsing
# ---------------------------------------------------------------------------
def parse_document_id(doc_id: str) -> dict:
    """
    Extract group_code, domain_number, is_stacked from DOCUMENT_ID.

    Examples:
      ISMS-IMP-A.8.17.1       → group=A.8.17, domain=1, stacked=False
      ISMS-IMP-A.6.3.1        → group=A.6.3,  domain=1, stacked=False
      ISMS-IMP-A.5.1-2-6.1-2.S1 → group=A.5.1-2-6.1-2, domain=1, stacked=True
    """
    # Strip prefix
    core = doc_id
    for prefix in ("ISMS-IMP-", "ISMS-POL-"):
        if core.startswith(prefix):
            core = core[len(prefix):]
            break

    # Stacked pattern: contains .S<N> at end
    stacked_m = re.match(r'^(A\..+?)\.S(\d+)$', core, re.IGNORECASE)
    if stacked_m:
        return {
            "group_code": stacked_m.group(1),
            "domain_number": int(stacked_m.group(2)),
            "is_stacked": True,
        }

    # Standard pattern: A.X.X.N  (last segment is domain number)
    # Split on the last dot — but group codes can be A.5.31, A.8.33-34 etc.
    # Use rsplit with maxsplit=1, but only if the last part is purely numeric
    parts = core.rsplit(".", 1)
    if len(parts) == 2 and parts[1].isdigit():
        return {
            "group_code": parts[0],
            "domain_number": int(parts[1]),
            "is_stacked": False,
        }

    # Non-standard suffix: A.8.6-Assessment-1 → group=A.8.6, domain=1
    word_n = re.match(r'^(A\.\d+\.\d+(?:-\d+)*)-[A-Za-z]+-(\d+)$', core)
    if word_n:
        return {
            "group_code": word_n.group(1),
            "domain_number": int(word_n.group(2)),
            "is_stacked": False,
        }

    # Fallback: no domain suffix recognised
    return {
        "group_code": core,
        "domain_number": None,
        "is_stacked": False,
    }


def parse_stacked_control_ids(control_id: str) -> list[str]:
    """
    For stacked generators like A.5.1-2-6.1-2, expand to individual control IDs.
    For simple generators return [control_id].
    """
    if "-" not in control_id:
        return [control_id]

    # Pattern: A.5.1-2-6.1-2  → A.5.1, A.5.2, A.6.1, A.6.2
    # Strategy: split on hyphen-separated number parts after a dot-letter-dot prefix
    # This is complex enough that we keep it as-is and parse what we can
    # Simple heuristic: if it's A.X.Y-Z, it means A.X.Y and A.X.Z
    # Full expansion: A.5.1-2-6.1-2 → A.5.1, A.5.2, A.6.1, A.6.2

    m = re.match(r'^(A)\.(\d+)\.(.+)$', control_id)
    if not m:
        return [control_id]

    # section = "5.1-2-6.1-2"
    section = m.group(2) + "." + m.group(3)
    # Split alternating groups: "5.1-2-6.1-2" — group by major.minor(-minor)* sequences
    # Parse as "major.minor" chunks separated by additional major shifts
    # e.g. "5.1-2-6.1-2" → group A: 5.(1,2), group B: 6.(1,2)

    ids = []
    # Split on sections that start a new major group (digit-dot after a hyphen)
    segments = re.split(r'-(?=\d+\.)', section)
    for seg in segments:
        major_m = re.match(r'^(\d+)\.(\d+(?:-\d+)*)$', seg)
        if major_m:
            major = major_m.group(1)
            minors = major_m.group(2).split("-")
            for minor in minors:
                ids.append(f"A.{major}.{minor}")
        else:
            ids.append(f"A.{seg}")

    return ids if ids else [control_id]


# ---------------------------------------------------------------------------
# Sheet name extraction
# ---------------------------------------------------------------------------
_PLACEHOLDER_RE = re.compile(r'^\[.*\]$')  # e.g. "[Data sheets]", "[Assessment sheets]"


def extract_sheet_names_from_docstring(src: str) -> tuple[list[str] | None, bool]:
    """
    Extract sheet names from 'Generated Workbook Structure:' numbered list.
    Returns (sheet_names, had_placeholder).
    had_placeholder=True means one or more entries were bracket placeholders like [Data sheets].
    """
    m = RE_STRUCTURE_SECTION.search(src)
    if not m:
        return None, False

    sheets = []
    had_placeholder = False
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line:
            continue
        item_m = RE_STRUCTURE_ITEM.match(line)
        if item_m:
            name = item_m.group(1).strip()
            # Remove trailing bracket annotations like "(Domain 1 only)"
            name = re.sub(r'\s*\(.*\)$', '', name).strip()
            if not name:
                continue
            if _PLACEHOLDER_RE.match(name):
                # Skip template placeholders — real names come from code extraction
                had_placeholder = True
                continue
            sheets.append(name)

    return (sheets if sheets else None), had_placeholder


def extract_sheet_names_from_code(src: str) -> list[str]:
    """
    Extract sheet names from code patterns — used as fallback and supplement.
    Collects wb.create_sheet("name"), wb.create_sheet(title="name"), ws.title = "name".
    Deduplicates while preserving order of first appearance.
    """
    seen: set[str] = set()
    sheets: list[str] = []

    def add(name: str) -> None:
        name = name.strip()
        if name and name not in seen:
            seen.add(name)
            sheets.append(name)

    for m in RE_CREATE_SHEET_NAMED.finditer(src):
        add(m.group(1))
    for m in RE_CREATE_SHEET_TITLE_KW.finditer(src):
        add(m.group(1))
    for m in RE_WS_TITLE.finditer(src):
        add(m.group(1))
    # List-block pattern: sheets = ["Name1", "Name2", ...]
    for block_m in RE_SHEET_LIST_BLOCK.finditer(src):
        for str_m in RE_QUOTED_STRING.finditer(block_m.group(1)):
            add(str_m.group(1))

    return sheets


# ---------------------------------------------------------------------------
# Main parser
# ---------------------------------------------------------------------------
def parse_generator(file_path: Path, framework_root: Path) -> dict | None:
    """Parse one generator file and return structured metadata dict."""
    try:
        src = file_path.read_text(encoding="utf-8")
    except OSError as e:
        logger.error("Cannot read %s: %s", file_path, e)
        return None

    # --- Extract constants ---
    def first(pattern: re.Pattern, default: str = "") -> str:
        m = pattern.search(src)
        return m.group(1).strip() if m else default

    document_id = first(RE_DOCUMENT_ID)
    workbook_name = first(RE_WORKBOOK_NAME)
    control_id = first(RE_CONTROL_ID)
    control_name = first(RE_CONTROL_NAME)

    if not document_id:
        logger.warning("No DOCUMENT_ID in %s — skipping", file_path.name)
        return None

    # --- Parse DOCUMENT_ID ---
    id_info = parse_document_id(document_id)
    group_code = id_info["group_code"]
    domain_number = id_info["domain_number"]
    is_stacked = id_info["is_stacked"]

    # --- Stacked control IDs ---
    stacked_control_ids = parse_stacked_control_ids(control_id) if is_stacked else None

    # --- Domain totals from docstring ---
    domain_m = RE_DOMAIN_LINE.search(src)
    domain_total = int(domain_m.group(2)) if domain_m else None
    if domain_m and domain_number is None:
        domain_number = int(domain_m.group(1))

    # --- Sheet names ---
    sheets_raw, had_placeholder = extract_sheet_names_from_docstring(src)
    code_sheets = extract_sheet_names_from_code(src)
    sheet_source = "docstring"

    if not sheets_raw:
        # No docstring structure at all — use code entirely
        sheets_raw = code_sheets
        sheet_source = "code"
    else:
        # Supplement docstring list with:
        # 1. Standard sheets omitted from some docstrings (Instructions & Legend / Summary Dashboard)
        # 2. If docstring had [Data sheets] placeholder, inject actual input sheets from code
        docstring_names_lower = {s.lower() for s in sheets_raw}
        # Standard sheet supplement (always)
        for name in code_sheets:
            if name in STANDARD_SHEETS and name.lower() not in docstring_names_lower:
                sheets_raw.append(name)
                docstring_names_lower.add(name.lower())
        # Placeholder supplement: inject code-sourced INPUT sheets where placeholder was
        if had_placeholder:
            input_sheets = [
                name for name in code_sheets
                if name not in STANDARD_SHEETS and name.lower() not in docstring_names_lower
            ]
            # Insert input sheets after Instructions & Legend (index 1) or at start
            insert_pos = next(
                (i + 1 for i, s in enumerate(sheets_raw) if classify_sheet(s) == "instructions"),
                0,
            )
            for j, name in enumerate(input_sheets):
                sheets_raw.insert(insert_pos + j, name)
                docstring_names_lower.add(name.lower())

    sheets = [
        {"name": name, "type": classify_sheet(name)}
        for name in sheets_raw
    ]

    # --- Normalise standard sheet names (underscore → space) and deduplicate ---
    _CANONICAL = {
        "Evidence_Register": "Evidence Register",
        "Summary_Dashboard": "Summary Dashboard",
        "Approval_Sign_Off": "Approval Sign-Off",
        "Instructions_Legend": "Instructions & Legend",
    }
    normalised = []
    seen_names: set[str] = set()
    for s in sheets:
        norm_name = _CANONICAL.get(s["name"], s["name"])
        if norm_name not in seen_names:
            seen_names.add(norm_name)
            normalised.append({"name": norm_name, "type": classify_sheet(norm_name)})
    sheets = normalised

    # --- Source file (relative from framework root) ---
    try:
        rel_path = str(file_path.relative_to(framework_root))
    except ValueError:
        rel_path = str(file_path)

    record = {
        "document_id": document_id,
        "workbook_name": workbook_name,
        "control_id": control_id,
        "control_name": control_name,
        "group_code": group_code,
        "domain_number": domain_number,
        "domain_total": domain_total,
        "is_stacked": is_stacked,
        "stacked_control_ids": stacked_control_ids,
        "sheets": sheets,
        "sheet_count": len(sheets),
        "sheet_source": sheet_source,
        "source_file": rel_path,
        "output_filename_pattern": f"{document_id}_{{workbook_name}}_{'{YYYYMMDD}'}.xlsx",
    }

    return record


# ---------------------------------------------------------------------------
# QA validation gate (Task 7.9)
# ---------------------------------------------------------------------------

# Required standard sheets — every production generator must have these.
# Mirrors the GS (Gold Standard Sheet) checks in qa_check_workbooks.py.
_REQUIRED_STANDARD_SHEETS = {
    "Instructions & Legend",
    "Summary Dashboard",
    "Evidence Register",
    "Approval Sign-Off",
}

# Minimum structural thresholds
_MIN_TOTAL_SHEETS = 3      # Instructions + ≥1 input + Summary Dashboard
_MIN_INPUT_SHEETS = 1      # Must have at least one assessment input sheet


def validate_generator_record(record: dict) -> dict:
    """
    Run structural QA checks on a parsed generator record.

    Returns the record with two new fields added:
      qa_status: "PASS" | "WARN" | "FAIL"
      qa_issues: list[str] — human-readable issue descriptions

    FAIL criteria (block DB import with --strict):
      - Missing WORKBOOK_NAME constant
      - Missing CONTROL_ID or CONTROL_NAME constant
      - Zero sheets extracted

    WARN criteria (logged but allowed through):
      - Fewer than _MIN_TOTAL_SHEETS sheets
      - Fewer than _MIN_INPUT_SHEETS input-type sheets
      - Any required standard sheet absent
      - Sheet names extracted from code fallback (not docstring)
    """
    issues: list[str] = []
    status = "PASS"

    # --- FAIL checks ---
    if not record.get("workbook_name"):
        issues.append("FAIL: missing WORKBOOK_NAME constant")
        status = "FAIL"

    if not record.get("control_id"):
        issues.append("FAIL: missing CONTROL_ID constant")
        status = "FAIL"

    if not record.get("control_name"):
        issues.append("FAIL: missing CONTROL_NAME constant")
        status = "FAIL"

    sheets = record.get("sheets", [])
    if not sheets:
        issues.append("FAIL: no sheets extracted (0 sheets)")
        status = "FAIL"

    if status == "FAIL":
        record["qa_status"] = status
        record["qa_issues"] = issues
        return record

    # --- WARN checks ---
    sheet_names = {s["name"] for s in sheets}
    input_count = sum(1 for s in sheets if s.get("type") == "input")

    if len(sheets) < _MIN_TOTAL_SHEETS:
        issues.append(f"WARN: only {len(sheets)} sheet(s) (minimum {_MIN_TOTAL_SHEETS})")
        status = "WARN"

    if input_count < _MIN_INPUT_SHEETS:
        issues.append(f"WARN: no input sheets found (input_count={input_count})")
        status = "WARN"

    missing_standard = _REQUIRED_STANDARD_SHEETS - sheet_names
    if missing_standard:
        issues.append(f"WARN: missing standard sheets: {sorted(missing_standard)}")
        status = "WARN"

    if record.get("sheet_source") == "code":
        issues.append("WARN: sheet names from code fallback (no docstring structure found)")
        # Not a WARN escalation on its own — code extraction is legitimate

    record["qa_status"] = status
    record["qa_issues"] = issues
    return record


def main() -> None:
    if not FRAMEWORK_ROOT.exists():
        logger.error("Framework root not found: %s", FRAMEWORK_ROOT)
        sys.exit(1)

    gen_files = sorted(FRAMEWORK_ROOT.glob("**/SCR/generate_*.py"))
    logger.info("Found %d generator files under %s", len(gen_files), FRAMEWORK_ROOT)

    registry: list[dict] = []
    errors: list[str] = []

    for fp in gen_files:
        record = parse_generator(fp, FRAMEWORK_ROOT)
        if record:
            record = validate_generator_record(record)
            registry.append(record)
        else:
            errors.append(str(fp))

    # Sort by document_id for stable output
    registry.sort(key=lambda r: r["document_id"])

    # Summary stats
    with_docstring = sum(1 for r in registry if r["sheet_source"] == "docstring")
    with_code = sum(1 for r in registry if r["sheet_source"] == "code")
    stacked_count = sum(1 for r in registry if r["is_stacked"])
    qa_pass = sum(1 for r in registry if r.get("qa_status") == "PASS")
    qa_warn = sum(1 for r in registry if r.get("qa_status") == "WARN")
    qa_fail = sum(1 for r in registry if r.get("qa_status") == "FAIL")

    logger.info("Parsed: %d records", len(registry))
    logger.info("  Sheet names from docstring: %d", with_docstring)
    logger.info("  Sheet names from code:      %d", with_code)
    logger.info("  Stacked generators:         %d", stacked_count)
    logger.info("QA Gate: PASS=%d  WARN=%d  FAIL=%d", qa_pass, qa_warn, qa_fail)

    if qa_warn:
        logger.warning("QA WARN generators:")
        for r in registry:
            if r.get("qa_status") == "WARN":
                for issue in r.get("qa_issues", []):
                    logger.warning("  %s — %s", r["document_id"], issue)

    if qa_fail:
        logger.error("QA FAIL generators (will be rejected by import --strict):")
        for r in registry:
            if r.get("qa_status") == "FAIL":
                for issue in r.get("qa_issues", []):
                    logger.error("  %s — %s", r["document_id"], issue)

    if errors:
        logger.warning("Skipped %d files (no DOCUMENT_ID): %s", len(errors), errors)

    # Write output
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(registry, indent=2, ensure_ascii=False))
    logger.info("Written: %s (%d records)", OUTPUT_FILE, len(registry))

    # Print sample
    if registry:
        logger.info("Sample record:\n%s", json.dumps(registry[0], indent=2))


if __name__ == "__main__":
    main()
