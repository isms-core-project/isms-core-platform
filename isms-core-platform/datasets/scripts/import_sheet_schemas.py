#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 7.5 — Sheet Schema Importer

Reads datasets/data/workbook_schemas.json (produced by extract_workbook_schema.py)
and updates the sheet_schemas JSONB column on each generator_definitions row.

Skips rows with user_override=True.

Run from repo root (60-isms-core-api/):
  python3 datasets/scripts/import_sheet_schemas.py
"""

import json
import logging
import os
import sys
from pathlib import Path

import psycopg2

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

SCRIPT_DIR  = Path(__file__).resolve().parent
SCHEMA_FILE = SCRIPT_DIR.parent / "data" / "workbook_schemas.json"

DB_DSN = os.environ.get(
    "DATABASE_URL",
    "postgresql://isms_user:isms_password@localhost:5432/isms_core"
)


def main() -> None:
    schemas = json.loads(SCHEMA_FILE.read_text())
    logger.info("Loaded %d records from %s", len(schemas), SCHEMA_FILE)

    conn = psycopg2.connect(DB_DSN)
    conn.autocommit = False
    cur = conn.cursor()

    stats = {"updated": 0, "skipped_override": 0, "not_found": 0, "no_sheets": 0}

    for rec in schemas:
        doc_id = rec["document_id"]
        sheets = rec.get("sheets", [])

        if not sheets:
            logger.warning("No sheets for %s — skipped", doc_id)
            stats["no_sheets"] += 1
            continue

        # Check user_override
        cur.execute(
            "SELECT id, user_override FROM generator_definitions WHERE document_id = %s",
            (doc_id,),
        )
        row = cur.fetchone()
        if not row:
            logger.warning("Not found in DB: %s", doc_id)
            stats["not_found"] += 1
            continue
        _id, user_override = row

        if user_override:
            logger.info("Skipping (user_override=True): %s", doc_id)
            stats["skipped_override"] += 1
            continue

        cur.execute(
            "UPDATE generator_definitions SET sheet_schemas = %s WHERE id = %s",
            (json.dumps(sheets), _id),
        )
        stats["updated"] += 1
        logger.info("Updated: %s (%d sheets)", doc_id, len(sheets))

    conn.commit()
    cur.close()
    conn.close()

    logger.info("Done. Stats: %s", stats)
    if stats["not_found"]:
        logger.warning("%d document_ids not found in DB", stats["not_found"])


if __name__ == "__main__":
    main()
