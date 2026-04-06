"""Phase 26 Track A — Index CISA KEV entries into OpenSearch QA reference corpus.

Indexes each KEV entry as a chunk with standard='cve_kev' so the QA engine
can semantically match A.8.8 / A.8.28 controls against real vulnerability data.

Called:
  - On backend startup (after ISO seeds), if no cve_kev chunks exist
  - Via POST /api/v1/feeds/kev/index-corpus (admin, on-demand re-index)
  - After each CISA KEV feed pull (triggered by Celery beat)
"""

import logging
from datetime import datetime, timezone

from sqlalchemy.orm import Session as DBSession

from src.services import search_service

logger = logging.getLogger(__name__)

STANDARD = "cve_kev"


def needs_index(db: DBSession) -> bool:
    """Return True if cve_kev chunks are absent from OpenSearch."""
    client = search_service.get_client()
    if not client:
        return False
    try:
        if not client.indices.exists(index=search_service.IDX_ISO_REFERENCE):
            return True
        result = client.count(
            index=search_service.IDX_ISO_REFERENCE,
            body={"query": {"term": {"standard": STANDARD}}},
        )
        return result.get("count", 0) == 0
    except Exception:
        return False


def index_from_db(db: DBSession) -> dict:
    """Index all CISA KEV entries from the DB into OpenSearch.

    Clears existing cve_kev chunks first, then re-indexes from current DB state.
    Returns stats dict.
    """
    import time
    t0 = time.monotonic()

    from src.domain.feeds import CisaKevEntry
    from sqlalchemy import select

    client = search_service.get_client()
    if not client:
        return {"indexed": 0, "error": "OpenSearch not available", "duration_ms": 0}

    search_service.ensure_iso_reference_index()

    # Remove existing cve_kev chunks
    try:
        if client.indices.exists(index=search_service.IDX_ISO_REFERENCE):
            client.delete_by_query(
                index=search_service.IDX_ISO_REFERENCE,
                body={"query": {"term": {"standard": STANDARD}}},
                wait_for_completion=True,
            )
    except Exception as e:
        logger.warning("Could not clear cve_kev chunks before re-index: %s", e)

    rows = db.scalars(select(CisaKevEntry)).all()
    indexed = 0

    for entry in rows:
        # Build a dense text combining vendor, product, description and required action
        parts = []
        if entry.vendor_project:
            parts.append(entry.vendor_project)
        if entry.product:
            parts.append(entry.product)
        if entry.vulnerability_name:
            parts.append(entry.vulnerability_name)
        if entry.short_description:
            parts.append(entry.short_description)
        if entry.required_action:
            parts.append(f"Required action: {entry.required_action}")
        if entry.known_ransomware:
            parts.append("Known ransomware campaign use.")
        if entry.due_date:
            parts.append(f"Remediation due: {entry.due_date.isoformat()}")

        text = " ".join(parts)
        if not text.strip():
            continue

        doc_id = f"cve_kev:{entry.cve_id}"
        ok = search_service.index_iso_chunk(
            doc_id=doc_id,
            standard=STANDARD,
            clause_id=entry.cve_id,
            title=entry.vulnerability_name or entry.cve_id,
            text=text,
            language="en",
            source_file="cisa_kev",
        )
        if ok:
            indexed += 1

    duration_ms = int((time.monotonic() - t0) * 1000)
    logger.info("KEV corpus indexed: %d entries in %dms", indexed, duration_ms)
    return {
        "indexed": indexed,
        "duration_ms": duration_ms,
        "indexed_at": datetime.now(timezone.utc).isoformat(),
    }
