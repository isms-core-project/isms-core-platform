"""Return the active EvidenceStore implementation based on EVIDENCE_STORE setting."""
from __future__ import annotations

import logging

from src.core.config import get_settings
from .base import EvidenceStore

logger = logging.getLogger(__name__)

_cached: EvidenceStore | None = None


def get_evidence_store(db=None) -> EvidenceStore:
    """
    EVIDENCE_STORE=postgres  → PostgresEvidenceStore (v1 compat, requires db session)
    EVIDENCE_STORE=opensearch → OpenSearchEvidenceStore (v2, no db session needed)
    """
    backend = get_settings().evidence_store.lower()

    if backend == "opensearch":
        global _cached
        if _cached is None:
            from .opensearch import OpenSearchEvidenceStore
            _cached = OpenSearchEvidenceStore()
            logger.info("EvidenceStore: OpenSearch backend active")
        return _cached

    # Default: postgres (v1)
    from .postgres import PostgresEvidenceStore
    if db is None:
        raise ValueError("PostgresEvidenceStore requires a db session")
    return PostgresEvidenceStore(db)
