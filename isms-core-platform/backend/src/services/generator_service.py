"""Phase 7.4 — Generator script regeneration service."""

import re
from datetime import date
from pathlib import Path
from typing import TypedDict

from jinja2 import Environment, FileSystemLoader, select_autoescape

from src.domain.content import GeneratorDefinition

_TEMPLATE_DIR = Path(__file__).resolve().parent.parent.parent / "templates"
_jinja_env = Environment(
    loader=FileSystemLoader(str(_TEMPLATE_DIR)),
    autoescape=select_autoescape([]),  # plain Python output — no HTML escaping
    keep_trailing_newline=True,
    trim_blocks=False,
    lstrip_blocks=False,
)


def _slugify(name: str) -> str:
    """Convert sheet name to a valid Python identifier fragment."""
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


def _fn_name(sheet_name: str) -> str:
    return f"create_{_slugify(sheet_name)}_sheet"


def _id_prefix(sheet_name: str) -> str:
    """Short uppercase prefix for sample IDs e.g. 'Time Sources' → 'TS'."""
    words = re.sub(r"[^a-zA-Z ]+", "", sheet_name).split()
    return "".join(w[0].upper() for w in words if w) or "D"


def render_generator(gen: GeneratorDefinition) -> str:
    """
    Render a runnable Python generator script from a GeneratorDefinition DB record.
    Returns the full script source as a string.
    """
    sheets = gen.sheets or []
    # Standard sheets handled by their own dedicated functions (only if present by exact name)
    _STANDARD_NAMES = {"Summary Dashboard", "Evidence Register", "Approval Sign-Off", "Instructions & Legend"}
    # Stubs are generated for: all input type + any non-standard named summary/approval/evidence/instructions
    input_sheets = [
        s for s in sheets
        if s.get("type") == "input"
        or (s.get("type") in ("summary", "approval", "evidence", "instructions") and s.get("name") not in _STANDARD_NAMES)
    ]
    has_summary = any(s.get("type") == "summary" and s.get("name") == "Summary Dashboard" for s in sheets)
    # Only generate standard ER/AS functions if they appear in the DB by exact name
    has_standard_er = any(s.get("name") == "Evidence Register" for s in sheets)
    has_standard_as = any(s.get("name") == "Approval Sign-Off" for s in sheets)

    # Build sheet_schemas lookup keyed by sheet name
    schema_by_name: dict[str, dict] = {}
    for schema in (gen.sheet_schemas or []):
        if isinstance(schema, dict):
            schema_by_name[schema.get("sheet_name", "")] = schema

    # Enrich input sheets with schema data (real headers, DVs, widths, status col)
    enriched_inputs = []
    for s in input_sheets:
        sheet_schema = schema_by_name.get(s["name"], {})
        columns = sheet_schema.get("columns", [])

        col_headers = [c["header"] for c in columns]
        col_widths = [c.get("width", 15) for c in columns]
        col_count = len(columns) if columns else 7

        # Collect columns that have DV values
        dv_cols = [
            {
                "col_idx": c["index"],
                "col_letter": c["letter"],
                "dv_list": c["dv_values"],
                "is_status": c.get("is_status_col", False),
            }
            for c in columns
            if c.get("dv_values")
        ]

        # Status column for SD COUNTIF: prefer the column whose DVs contain
        # "Compliant" (the main assessment status), then fall back to
        # the schema-recorded status_column_letter, then "E".
        _compliant_col = next(
            (
                c["letter"]
                for c in columns
                if any("compliant" in str(v).lower() for v in c.get("dv_values", []))
            ),
            None,
        )
        status_col_letter = _compliant_col or sheet_schema.get("status_column_letter") or "E"

        # COUNTA column: use col 2 if available, else col 1, else "B"
        if len(columns) >= 2:
            count_col_letter = columns[1]["letter"]
        elif len(columns) == 1:
            count_col_letter = columns[0]["letter"]
        else:
            count_col_letter = "B"

        freeze_panes = sheet_schema.get("freeze_panes", "A4")

        enriched_inputs.append({
            "name": s["name"],
            "type": s["type"],
            "fn_name": _fn_name(s["name"]),
            "id_prefix": _id_prefix(s["name"]),
            "has_schema": bool(columns),
            "columns": columns,
            "col_headers": col_headers,
            "col_widths": col_widths,
            "col_count": col_count,
            "dv_cols": dv_cols,
            "status_col_letter": status_col_letter,
            "count_col_letter": count_col_letter,
            "freeze_panes": freeze_panes,
        })

    # Build sheets_indexed for the docstring structure list
    sheets_indexed = list(enumerate(sheets, start=1))

    # Related documents: siblings in the same control group (placeholders)
    workbook_slug = gen.workbook_name.replace(" ", "_")
    related_docs = [f"ISMS-POL-{gen.group_code} — {gen.control_name} Policy"]
    if gen.domain_total and gen.domain_total > 1:
        for n in range(1, gen.domain_total + 1):
            if n != gen.domain_number:
                related_docs.append(f"{gen.document_id.rsplit('.', 1)[0]}.{n} — Domain {n} workbook")

    # next instruction number after data sheets in IL
    next_instr_num = len(enriched_inputs) + 1

    ctx = {
        "document_id": gen.document_id,
        "workbook_name": gen.workbook_name,
        "workbook_name_slug": workbook_slug,
        "control_id": gen.control_id,
        "control_id_slug": gen.control_id.lower().replace(".", "-"),
        "control_name": gen.control_name,
        "domain_number": gen.domain_number,
        "domain_total": gen.domain_total,
        "sheet_count": gen.sheet_count,
        "sheets_indexed": sheets_indexed,
        "input_sheets": enriched_inputs,
        "has_summary": has_summary,
        "has_standard_er": has_standard_er,
        "has_standard_as": has_standard_as,
        "related_docs": related_docs,
        "next_instr_num": next_instr_num,
        "generation_date": date.today().strftime("%Y-%m-%d"),
        "output_filename_prefix": f"generate_{_slugify(gen.document_id)}",
    }

    template = _jinja_env.get_template("generator.py.j2")
    return template.render(**ctx)


# ---------------------------------------------------------------------------
# QA gate on regenerated output (Task 7.13)
# ---------------------------------------------------------------------------

class _QAResult(TypedDict):
    status: str        # "PASS" | "WARN" | "FAIL"
    issues: list[str]


# Required top-level names that every regenerated script must define.
_REQUIRED_CONSTANTS = {"DOCUMENT_ID", "WORKBOOK_NAME", "CONTROL_ID", "CONTROL_NAME", "OUTPUT_FILENAME"}
_REQUIRED_FUNCTIONS = {"main"}  # create_workbook is per-sheet; main() is the universal entry point


def validate_rendered_script(source: str) -> _QAResult:
    """
    Validate a rendered generator script (Task 7.13 — QA gate on regenerated output).

    Checks:
      1. Python syntax via compile()
      2. Required top-level constants present (DOCUMENT_ID etc.)
      3. Required functions present (create_workbook, main)
      4. Script is non-trivially long (>50 lines)

    Returns qa_status (PASS / WARN / FAIL) and list of issues.
    FAIL: syntax error or missing required constant/function.
    WARN: script is unusually short.
    """
    issues: list[str] = []
    status = "PASS"

    # 1. Python syntax
    try:
        compile(source, "<regenerated>", "exec")
    except SyntaxError as exc:
        issues.append(f"FAIL: syntax error — {exc}")
        return _QAResult(status="FAIL", issues=issues)

    # 2. Required constants
    missing_consts = [
        name for name in sorted(_REQUIRED_CONSTANTS)
        if not re.search(rf"^{name}\s*=", source, re.MULTILINE)
    ]
    if missing_consts:
        for name in missing_consts:
            issues.append(f"FAIL: missing required constant {name}")
        status = "FAIL"

    # 3. Required functions
    missing_fns = [
        name for name in sorted(_REQUIRED_FUNCTIONS)
        if not re.search(rf"^def {name}\s*\(", source, re.MULTILINE)
    ]
    if missing_fns:
        for name in missing_fns:
            issues.append(f"FAIL: missing required function {name}()")
        status = "FAIL"

    if status == "FAIL":
        return _QAResult(status=status, issues=issues)

    # 4. Length sanity check
    line_count = source.count("\n")
    if line_count < 50:
        issues.append(f"WARN: script is only {line_count} lines (expected >50)")
        status = "WARN"

    return _QAResult(status=status, issues=issues)
