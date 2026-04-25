"""Glossary endpoints — ISO/IEC 22123 (Cloud), ISO/IEC 42001/42005/22989 (AI)."""

import logging
from typing import Annotated

from fastapi import APIRouter, Query

from src.services import search_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/glossary", tags=["glossary"])

_CLOUD_STANDARDS = {
    "vocabulary":   "ISO/IEC 22123-1:2023",
    "concepts":     "ISO/IEC 22123-2:2023",
    "architecture": "ISO/IEC 22123-3:2023",
}

_AI_STANDARDS = {
    "iso42001": "ISO/IEC 42001:2023",
    "iso42005": "ISO/IEC 42005:2025",
    "iso22989": "ISO/IEC 22989:2022",
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
    standard = _CLOUD_STANDARDS.get(part, _CLOUD_STANDARDS["vocabulary"])

    if q:
        raw = search_service.search_iso_reference_by_standard(
            query=q, standard=standard, max_results=20
        )
        return {"standard": standard, "part": part, "query": q, "results_text": raw, "entries": []}

    entries = search_service.get_iso_reference_by_standard_all(standard=standard)
    return {"standard": standard, "part": part, "query": None, "entries": entries}


@router.get("/ai")
def get_ai_glossary(
    part: Annotated[str, Query(description="iso42001 | iso42005")] = "iso42001",
    q: Annotated[str | None, Query(description="Optional full-text search query")] = None,
):
    """Return AI management system glossary entries.

    - **part=iso42001** (default) — ISO/IEC 42001:2023 terms and definitions (26 terms, Clause 3)
    - **part=iso42005** — ISO/IEC 42005:2025 terms and definitions (9 terms + abbreviated terms, Clause 3–4)
    - **part=iso22989** — ISO/IEC 22989:2022 AI concepts and terminology (117 terms, 7 subcategories)

    Optionally filter by **q** (full-text search within the selected part).
    """
    standard = _AI_STANDARDS.get(part, _AI_STANDARDS["iso42001"])

    if q:
        raw = search_service.search_iso_reference_by_standard(
            query=q, standard=standard, max_results=20
        )
        return {"standard": standard, "part": part, "query": q, "results_text": raw, "entries": []}

    entries = search_service.get_iso_reference_by_standard_all(standard=standard)
    return {"standard": standard, "part": part, "query": None, "entries": entries}
