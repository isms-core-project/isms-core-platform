"""Cloud computing glossary endpoints — powered by ISO/IEC 22123 corpus."""

import logging
from typing import Annotated

from fastapi import APIRouter, Query

from src.services import search_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/glossary", tags=["glossary"])

_STANDARDS = {
    "vocabulary": "ISO/IEC 22123-1:2023",
    "concepts":   "ISO/IEC 22123-2:2023",
    "architecture": "ISO/IEC 22123-3:2023",
}


@router.get("/cloud")
def get_cloud_glossary(
    part: Annotated[str, Query(description="vocabulary | concepts | architecture")] = "vocabulary",
    q: Annotated[str | None, Query(description="Optional full-text search query")] = None,
):
    """Return ISO/IEC 22123 cloud computing glossary entries.

    - **part=vocabulary** (default) — ISO 22123-1 terms and definitions
    - **part=concepts** — ISO 22123-2 concept clauses
    - **part=architecture** — ISO 22123-3 CCRA clauses

    Optionally filter by **q** (full-text search within the selected part).
    """
    standard = _STANDARDS.get(part, _STANDARDS["vocabulary"])

    if q:
        # Full-text search within the selected standard
        raw = search_service.search_iso_reference_by_standard(
            query=q, standard=standard, max_results=20
        )
        # Return as structured entries for the UI
        return {"standard": standard, "part": part, "query": q, "results_text": raw, "entries": []}

    # Return all chunks for the selected standard
    entries = search_service.get_iso_reference_by_standard_all(standard=standard)
    return {"standard": standard, "part": part, "query": None, "entries": entries}
