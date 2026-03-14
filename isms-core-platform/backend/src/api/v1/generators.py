"""Generator definitions API — Phase 7.3/7.4."""

import re
from collections import defaultdict
from datetime import datetime, timezone

import logging

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse, Response

logger = logging.getLogger(__name__)
from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, require_content_editable
from src.database.session import get_db
from src.domain.content import GeneratorDefinition
from src.domain.control_groups import ControlGroup
from src.domain.users import User
from src.schemas.generators import GeneratorGrouped, GeneratorRead, GeneratorUpdate
from src.core.config import get_settings
from src.services.generator_service import render_generator, validate_rendered_script
from src.services.workbook_service import WorkbookRegenError, regenerate_workbook, _product_base_path

router = APIRouter(prefix="/generators", tags=["generators"])

_SECTION_RE = re.compile(r"^(a\.\d+)", re.IGNORECASE)


def _section(group_code: str) -> str:
    m = _SECTION_RE.match(group_code.lower())
    return m.group(1).upper() if m else group_code.upper()


def _apply_product_filter(q, product: str | None):
    """Filter generator query by product.

    product values:
      framework   → FW only
      operational → OP only
      privacy     → PRIV only
      cloud       → CLD only
      isms        → FW + OP (both ISMS-family products)
      None        → all products
    """
    if product == "isms":
        q = q.where(GeneratorDefinition.product_type.in_(["framework", "operational"]))
    elif product in ("framework", "operational", "privacy", "cloud"):
        q = q.where(GeneratorDefinition.product_type == product)
    return q


@router.get("/form/{group_code}")
def get_form_schema(
    group_code: str,
    product_type: str = "framework",
    generator_id: str | None = None,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Return input-only sheet schemas for a control group — used by the WebUI assessment form renderer.
    Optionally filter to a single generator via generator_id (document_id)."""
    if product_type != "framework":
        return []

    q = (
        select(GeneratorDefinition)
        .where(GeneratorDefinition.group_code == group_code.lower())
        .order_by(GeneratorDefinition.domain_number)
    )
    if generator_id:
        q = q.where(GeneratorDefinition.document_id == generator_id)

    gens = db.execute(q).scalars().all()

    if not gens:
        raise HTTPException(status_code=404, detail=f"No generators found for group_code={group_code}")

    result = []
    seen: set[str] = set()
    for gen in gens:
        for schema in (gen.sheet_schemas or []):
            if not isinstance(schema, dict):
                continue
            if schema.get("sheet_type") != "input":
                continue
            sheet_name = schema.get("sheet_name", "")
            key = f"{gen.document_id}::{sheet_name}"
            if key in seen:
                continue
            seen.add(key)
            result.append({
                "generator_document_id": gen.document_id,
                "sheet_name": sheet_name,
                "title_text": schema.get("title_text") or sheet_name,
                "subtitle_text": schema.get("subtitle_text"),
                "columns": schema.get("columns", []),
                "sample_row": schema.get("sample_row", []),
                "status_column_letter": schema.get("status_column_letter"),
            })
    return result


@router.get("/", response_model=list[GeneratorRead])
def list_generators(
    group_code: str | None = None,
    section: str | None = None,
    product: str | None = None,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """List all generator definitions. Filter by group_code, section, and/or product."""
    q = select(GeneratorDefinition).order_by(
        GeneratorDefinition.group_code,
        GeneratorDefinition.domain_number,
    )
    if group_code:
        q = q.where(GeneratorDefinition.group_code.ilike(group_code))
    if section:
        if section == "00":
            q = q.where(GeneratorDefinition.group_code == "00")
        else:
            prefix = section.lower().rstrip(".") + "."
            q = q.where(GeneratorDefinition.group_code.ilike(f"{prefix}%"))
    q = _apply_product_filter(q, product)

    rows = db.execute(q).scalars().all()
    return [GeneratorRead.model_validate(r) for r in rows]


@router.get("/grouped", response_model=list[GeneratorGrouped])
def list_generators_grouped(
    section: str | None = None,
    product: str | None = None,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Generators grouped by control group. Filter by section and/or product."""
    q = select(GeneratorDefinition).order_by(
        GeneratorDefinition.group_code,
        GeneratorDefinition.domain_number,
    )
    if section:
        if section == "00":
            q = q.where(GeneratorDefinition.group_code == "00")
        else:
            prefix = section.lower().rstrip(".") + "."
            q = q.where(GeneratorDefinition.group_code.ilike(f"{prefix}%"))
    q = _apply_product_filter(q, product)

    rows = db.execute(q).scalars().all()

    # Group by group_code
    groups: dict[str, list[GeneratorDefinition]] = defaultdict(list)
    for row in rows:
        groups[row.group_code].append(row)

    # Resolve control names from control_groups table where available
    group_codes = list(groups.keys())
    cg_rows = db.execute(
        select(ControlGroup.group_code, ControlGroup.name).where(
            ControlGroup.group_code.in_(group_codes)
        )
    ).all()
    cg_names = {r[0]: r[1] for r in cg_rows}

    result: list[GeneratorGrouped] = []
    for code in sorted(groups.keys()):
        gens = groups[code]
        first = gens[0]
        result.append(
            GeneratorGrouped(
                group_code=code,
                control_name=cg_names.get(code, first.control_name),
                section=_section(code),
                generators=[GeneratorRead.model_validate(g) for g in gens],
                total_domains=max(
                    (g.domain_total or g.domain_number or 1) for g in gens
                ),
            )
        )

    return result


@router.get("/{document_id}", response_model=GeneratorRead)
def get_generator(
    document_id: str,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Single generator definition by document_id."""
    row = db.execute(
        select(GeneratorDefinition).where(
            GeneratorDefinition.document_id == document_id
        )
    ).scalar_one_or_none()
    if not row:
        raise HTTPException(status_code=404, detail="Generator not found")
    return GeneratorRead.model_validate(row)


@router.put("/{document_id}", response_model=GeneratorRead)
def update_generator(
    document_id: str,
    body: GeneratorUpdate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(require_content_editable),
):
    """
    Update editable fields on a generator definition.
    Sets user_override=true so the importer will not overwrite manual edits.
    """
    row = db.execute(
        select(GeneratorDefinition).where(
            GeneratorDefinition.document_id == document_id
        )
    ).scalar_one_or_none()
    if not row:
        raise HTTPException(status_code=404, detail="Generator not found")

    row.workbook_name = body.workbook_name
    row.domain_number = body.domain_number
    row.domain_total = body.domain_total
    row.sheets = [s.model_dump() for s in body.sheets]
    row.sheet_count = len(body.sheets)
    row.user_override = True
    row.parsed_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(row)
    return GeneratorRead.model_validate(row)


@router.post("/{document_id}/generate")
def generate_script(
    document_id: str,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """
    Regenerate a runnable Python generator script from the DB definition.
    Returns the .py source as an application/octet-stream download.
    """
    row = db.execute(
        select(GeneratorDefinition).where(
            GeneratorDefinition.document_id == document_id
        )
    ).scalar_one_or_none()
    if not row:
        raise HTTPException(status_code=404, detail="Generator not found")

    product = getattr(row, "product_type", "framework") or "framework"

    # Non-framework: return original source script from disk
    if product != "framework":
        base = _product_base_path(product)
        script_path = base / (row.source_file or "")
        if not script_path.exists():
            raise HTTPException(
                status_code=404,
                detail=f"Source script not found: {row.source_file}",
            )
        source = script_path.read_text(encoding="utf-8")
        filename = script_path.name
        return Response(
            content=source.encode("utf-8"),
            media_type="application/octet-stream",
            headers={"Content-Disposition": f'attachment; filename="{filename}"'},
        )

    # Framework: render Jinja2 template → QA gate
    source = render_generator(row)

    # Task 7.13 — QA gate: validate rendered script before serving
    qa = validate_rendered_script(source)
    if qa["status"] == "FAIL":
        raise HTTPException(
            status_code=500,
            detail=f"Rendered script failed QA gate: {'; '.join(qa['issues'])}",
        )

    filename = f"generate_{document_id.lower().replace('.', '_').replace('-', '_')}.py"
    headers = {
        "Content-Disposition": f'attachment; filename="{filename}"',
        "X-QA-Status": qa["status"],
        "X-QA-Issues": "; ".join(qa["issues"]) if qa["issues"] else "none",
    }
    return Response(
        content=source.encode("utf-8"),
        media_type="application/octet-stream",
        headers=headers,
    )


@router.post("/{document_id}/workbook")
def generate_workbook(
    document_id: str,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """
    Regenerate the Excel workbook (.xlsx) for a generator from DB data.
    Renders the Python script via Jinja2, validates it, executes it in a
    sandboxed subprocess, and returns the produced .xlsx as a download.

    This is the Task 7.14 workbook regeneration endpoint.
    """
    row = db.execute(
        select(GeneratorDefinition).where(
            GeneratorDefinition.document_id == document_id
        )
    ).scalar_one_or_none()
    if not row:
        raise HTTPException(status_code=404, detail="Generator not found")

    try:
        xlsx_path, tmpdir = regenerate_workbook(row)
    except WorkbookRegenError as exc:
        raise HTTPException(status_code=500, detail=str(exc))

    xlsx_filename = xlsx_path.name

    # FileResponse streams the file, tmpdir is cleaned up after the response is sent.
    # We attach tmpdir to the response so it stays alive until streaming is complete.
    response = FileResponse(
        path=str(xlsx_path),
        filename=xlsx_filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f'attachment; filename="{xlsx_filename}"'},
    )

    # Attach cleanup hook: tmpdir.cleanup() called after response body is sent.
    # FastAPI / Starlette does not natively support this, so we hold a reference
    # and schedule cleanup via a background task.
    # For simplicity, we close it immediately after FileResponse reads the file.
    # FileResponse reads synchronously before returning in the ASGI context, so this is safe.
    response.background = _TmpCleanup(tmpdir)
    return response


class _TmpCleanup:
    """Background task that cleans up a TemporaryDirectory after FileResponse sends the file."""
    def __init__(self, tmpdir):
        self._tmpdir = tmpdir

    async def __call__(self):
        try:
            self._tmpdir.cleanup()
        except Exception:
            pass


@router.delete("/{document_id}/override", response_model=GeneratorRead)
def clear_override(
    document_id: str,
    db: DBSession = Depends(get_db),
    _user: User = Depends(require_content_editable),
):
    """Clear user_override flag — next importer run will restore parsed values."""
    row = db.execute(
        select(GeneratorDefinition).where(
            GeneratorDefinition.document_id == document_id
        )
    ).scalar_one_or_none()
    if not row:
        raise HTTPException(status_code=404, detail="Generator not found")

    row.user_override = False
    db.commit()
    db.refresh(row)
    return GeneratorRead.model_validate(row)
