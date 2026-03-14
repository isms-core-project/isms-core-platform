"""Phase 7.14 — Workbook regeneration service.

Two execution modes:
  - framework:              Render Jinja2 template → validate → execute in tmpdir
  - operational/privacy/cloud: Run original source script directly; engine located via PYTHONPATH injection

Security: framework scripts are validated by validate_rendered_script before execution.
Non-framework scripts are QA-verified source files from read-only content mounts.
All subprocesses run with a timeout and write output to a temporary directory.
"""
import logging
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from src.core.config import get_settings
from src.domain.content import GeneratorDefinition
from src.services.generator_service import render_generator, validate_rendered_script

logger = logging.getLogger(__name__)

_SUBPROCESS_TIMEOUT_SECS = 120  # Checklist scripts can be large


class WorkbookRegenError(Exception):
    """Raised when workbook regeneration fails."""


def _product_base_path(product_type: str) -> Path:
    s = get_settings()
    paths = {
        "framework":   s.framework_path,
        "operational": s.operational_path,
        "privacy":     s.privacy_path,
        "cloud":       s.cloud_path,
    }
    raw = paths.get(product_type, s.framework_path)
    return Path(raw)


def _engine_path(product_type: str) -> str | None:
    """Return the engine directory to inject into PYTHONPATH, if any."""
    s = get_settings()
    if product_type == "operational":
        return str(Path(s.operational_path) / "00-checklist-engine")
    if product_type in ("privacy", "cloud"):
        # CLD reuses the PRIV engine
        return str(Path(s.privacy_path) / "00-checklist-engine")
    return None


def _run_direct(gen: GeneratorDefinition) -> tuple[Path, Path]:
    """Execute a non-framework checklist script directly from its source location.

    The script writes its .xlsx output to cwd (tmp_path).
    Engine imports are satisfied via PYTHONPATH injection.
    """
    base = _product_base_path(gen.product_type)
    script_path = base / (gen.source_file or "")
    if not script_path.exists():
        raise WorkbookRegenError(
            f"Source script not found: {script_path}"
        )

    engine_dir = _engine_path(gen.product_type)
    env = os.environ.copy()
    if engine_dir:
        env["PYTHONPATH"] = engine_dir + os.pathsep + env.get("PYTHONPATH", "")

    tmpdir = tempfile.TemporaryDirectory(prefix="isms_wkbk_")
    tmp_path = Path(tmpdir.name)

    logger.info("Running direct script %s for %s", script_path.name, gen.document_id)

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=_SUBPROCESS_TIMEOUT_SECS,
            cwd=str(tmp_path),
            env=env,
        )
    except subprocess.TimeoutExpired:
        tmpdir.cleanup()
        raise WorkbookRegenError(
            f"Script timed out after {_SUBPROCESS_TIMEOUT_SECS}s"
        )
    except Exception as exc:
        tmpdir.cleanup()
        raise WorkbookRegenError(f"Subprocess error: {exc}") from exc

    if result.returncode != 0:
        stderr = result.stderr.strip()[-500:] if result.stderr else "(no stderr)"
        tmpdir.cleanup()
        raise WorkbookRegenError(
            f"Script exited with code {result.returncode}: {stderr}"
        )

    xlsx_files = list(tmp_path.glob("*.xlsx"))
    if not xlsx_files:
        tmpdir.cleanup()
        raise WorkbookRegenError("Script ran successfully but produced no .xlsx file")

    return xlsx_files[0], tmpdir


def regenerate_workbook(gen: GeneratorDefinition) -> tuple[Path, Path]:
    """
    Render and execute a generator script, returning the path to the produced .xlsx.

    Returns:
        (xlsx_path, tmpdir): caller MUST call tmpdir.cleanup() after consuming the file.

    Raises:
        WorkbookRegenError: if rendering, QA validation, or script execution fails.
    """
    product = getattr(gen, "product_type", "framework") or "framework"

    # Non-framework products: run original source script directly
    if product != "framework":
        return _run_direct(gen)

    # Framework: render Jinja2 template → QA gate → execute
    try:
        source = render_generator(gen)
    except Exception as exc:
        raise WorkbookRegenError(f"Template render failed: {exc}") from exc

    qa = validate_rendered_script(source)
    if qa["status"] == "FAIL":
        raise WorkbookRegenError(
            f"Rendered script failed QA gate: {'; '.join(qa['issues'])}"
        )

    tmpdir = tempfile.TemporaryDirectory(prefix="isms_wkbk_")
    tmp_path = Path(tmpdir.name)
    script_path = tmp_path / f"generate_{gen.document_id.replace('.', '_').replace('-', '_')}.py"
    script_path.write_text(source, encoding="utf-8")

    logger.info("Regenerating workbook for %s in %s", gen.document_id, tmp_path)

    try:
        result = subprocess.run(
            [sys.executable, str(script_path), "--output", str(tmp_path)],
            capture_output=True,
            text=True,
            timeout=_SUBPROCESS_TIMEOUT_SECS,
            cwd=str(tmp_path),
        )
    except subprocess.TimeoutExpired:
        tmpdir.cleanup()
        raise WorkbookRegenError(
            f"Generator script timed out after {_SUBPROCESS_TIMEOUT_SECS}s"
        )
    except Exception as exc:
        tmpdir.cleanup()
        raise WorkbookRegenError(f"Subprocess error: {exc}") from exc

    if result.returncode != 0:
        stderr = result.stderr.strip()[-500:] if result.stderr else "(no stderr)"
        tmpdir.cleanup()
        raise WorkbookRegenError(
            f"Generator script exited with code {result.returncode}: {stderr}"
        )

    xlsx_files = list(tmp_path.glob("*.xlsx"))
    if not xlsx_files:
        tmpdir.cleanup()
        raise WorkbookRegenError(
            "Generator script ran successfully but produced no .xlsx file"
        )

    xlsx_path = xlsx_files[0]
    logger.info("Workbook regenerated: %s (%d bytes)", xlsx_path.name, xlsx_path.stat().st_size)

    return xlsx_path, tmpdir
