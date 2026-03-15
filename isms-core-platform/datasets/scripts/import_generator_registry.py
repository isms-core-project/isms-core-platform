#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 7.2 — Generator Registry DB Importer

Reads datasets/data/generator_registry.json (produced by parse_generators.py)
and upserts into the generator_definitions table.

Control group resolution:
  - Tries exact match on group_code (e.g. "A.8.17")
  - For stacked generators, tries each stacked_control_id
  - Falls back to partial match on the first segment (e.g. "A.8")
  - Logs any unresolved group codes (imported with control_group_id = NULL)

Run inside Docker:
  docker compose exec isms-core-backend python /app/datasets/scripts/import_generator_registry.py
"""

import argparse
import json
import logging
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "backend"))

from src.database.base import Base  # noqa: E402
from src.domain.content import GeneratorDefinition  # noqa: E402
from src.domain.control_groups import ControlGroup  # noqa: E402

import os

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

REGISTRY_FILE = Path(__file__).resolve().parent.parent / "data" / "generator_registry.json"


def get_db_url() -> str:
    return os.environ.get(
        "DATABASE_URL",
        "postgresql://isms_user:isms_pass@localhost:5432/isms_core",
    )


def _build_group_index(session: Session) -> dict[str, uuid.UUID]:
    """Load all control groups into a dict keyed by lowercase group_code."""
    rows = session.execute(select(ControlGroup.group_code, ControlGroup.id)).all()
    return {r[0].lower(): r[1] for r in rows}


def resolve_control_group(
    group_code: str,
    index: dict[str, uuid.UUID],
    cache: dict,
) -> uuid.UUID | None:
    """
    Resolve group_code to control_group.id using the in-memory index.
    Strategy:
      1. Exact match (lowercased)
      2. Prefix match: extract base before first hyphen, find any DB group starting with it
         e.g. "A.7.1" → base "a.7.1" → matches "a.7.1-3"
         e.g. "A.8.20-21-22" → base "a.8.20" → matches "a.8.20-22"
    """
    key = group_code.lower()
    if key in cache:
        return cache[key]

    # 1. Exact
    result = index.get(key)

    # 2. Prefix fallback
    if result is None:
        # Take the part before the first hyphen as the prefix to search
        base = key.split("-")[0]
        for db_key, db_id in index.items():
            if db_key.startswith(base) and db_key != "00":
                result = db_id
                break

    cache[key] = result
    return result


def import_registry(session: Session, registry: list[dict]) -> dict:
    stats = {"inserted": 0, "updated": 0, "unresolved_group": 0, "errors": 0}
    cache: dict[str, uuid.UUID | None] = {}

    # Build in-memory index of all control groups
    group_index = _build_group_index(session)
    logger.info("Loaded %d control groups into index", len(group_index))

    for rec in registry:
        try:
            doc_id = rec["document_id"]
            group_code = rec["group_code"]

            # Resolve control group
            group_id = resolve_control_group(group_code, group_index, cache)

            # For stacked generators, try individual stacked IDs if primary fails
            if group_id is None and rec.get("stacked_control_ids"):
                for cid in rec["stacked_control_ids"]:
                    group_id = resolve_control_group(cid, group_index, cache)
                    if group_id:
                        break

            if group_id is None:
                stats["unresolved_group"] += 1
                logger.warning("No control group for group_code=%s (%s)", group_code, doc_id)

            # Check existing
            existing = session.execute(
                select(GeneratorDefinition).where(
                    GeneratorDefinition.document_id == doc_id
                )
            ).scalar_one_or_none()

            now = datetime.now(timezone.utc)

            if existing and existing.user_override:
                logger.debug("Skip %s (user_override=true)", doc_id)
                stats["updated"] += 1  # count as processed, not re-imported
                continue

            if existing:
                existing.workbook_name = rec["workbook_name"]
                existing.control_id = rec["control_id"]
                existing.control_name = rec["control_name"]
                existing.group_code = group_code
                existing.control_group_id = group_id
                existing.domain_number = rec.get("domain_number")
                existing.domain_total = rec.get("domain_total")
                existing.is_stacked = rec.get("is_stacked", False)
                existing.stacked_control_ids = rec.get("stacked_control_ids")
                existing.sheets = rec.get("sheets", [])
                existing.sheet_count = rec.get("sheet_count", 0)
                existing.sheet_source = rec.get("sheet_source")
                existing.source_file = rec.get("source_file")
                existing.parsed_at = now
                stats["updated"] += 1
            else:
                defn = GeneratorDefinition(
                    id=uuid.uuid4(),
                    document_id=doc_id,
                    workbook_name=rec["workbook_name"],
                    control_id=rec["control_id"],
                    control_name=rec["control_name"],
                    group_code=group_code,
                    control_group_id=group_id,
                    domain_number=rec.get("domain_number"),
                    domain_total=rec.get("domain_total"),
                    is_stacked=rec.get("is_stacked", False),
                    stacked_control_ids=rec.get("stacked_control_ids"),
                    sheets=rec.get("sheets", []),
                    sheet_count=rec.get("sheet_count", 0),
                    sheet_source=rec.get("sheet_source"),
                    source_file=rec.get("source_file"),
                    parsed_at=now,
                )
                session.add(defn)
                stats["inserted"] += 1

        except Exception as e:
            stats["errors"] += 1
            logger.error("Error importing %s: %s", rec.get("document_id", "?"), e)

    return stats


def _apply_qa_gate(registry: list[dict], strict: bool) -> list[dict]:
    """
    Filter registry based on qa_status field (added by parse_generators.py).

    --strict: FAIL records are rejected (logged as errors, not imported).
    Without --strict: all records pass through; FAIL records are logged as warnings.

    Returns the (possibly filtered) list to import.
    """
    qa_pass = sum(1 for r in registry if r.get("qa_status") == "PASS")
    qa_warn = sum(1 for r in registry if r.get("qa_status") == "WARN")
    qa_fail = sum(1 for r in registry if r.get("qa_status") == "FAIL")
    no_status = sum(1 for r in registry if "qa_status" not in r)

    logger.info("QA Gate: PASS=%d  WARN=%d  FAIL=%d  (no_status=%d)", qa_pass, qa_warn, qa_fail, no_status)

    for r in registry:
        if r.get("qa_status") == "WARN":
            for issue in r.get("qa_issues", []):
                logger.warning("  %s — %s", r["document_id"], issue)

    fail_ids: list[str] = []
    for r in registry:
        if r.get("qa_status") == "FAIL":
            fail_ids.append(r["document_id"])
            for issue in r.get("qa_issues", []):
                logger.error("  %s — %s", r["document_id"], issue)

    if fail_ids:
        if strict:
            logger.error(
                "--strict: rejecting %d FAIL generator(s): %s", len(fail_ids), fail_ids
            )
            return [r for r in registry if r.get("qa_status") != "FAIL"]
        else:
            logger.warning(
                "%d FAIL generator(s) included (use --strict to reject): %s",
                len(fail_ids), fail_ids,
            )

    return registry


def main():
    parser = argparse.ArgumentParser(
        description="Import generator_registry.json into the generator_definitions table."
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Reject generators with qa_status=FAIL (block DB import). Without this flag, FAIL "
             "generators are logged but still imported.",
    )
    args = parser.parse_args()

    if not REGISTRY_FILE.exists():
        logger.error("Registry file not found: %s", REGISTRY_FILE)
        logger.error("Run parse_generators.py first.")
        sys.exit(1)

    registry = json.loads(REGISTRY_FILE.read_text())
    logger.info("Loaded %d generator records from %s", len(registry), REGISTRY_FILE)

    # Apply QA gate
    registry = _apply_qa_gate(registry, strict=args.strict)
    logger.info("After QA gate: %d records to import", len(registry))

    engine = create_engine(get_db_url())

    with Session(engine) as session:
        stats = import_registry(session, registry)
        session.commit()

    logger.info("Import complete: %s", stats)
    if stats["unresolved_group"] > 0:
        logger.warning(
            "%d generators have no matching control group in DB — "
            "imported with control_group_id = NULL",
            stats["unresolved_group"],
        )


if __name__ == "__main__":
    main()
