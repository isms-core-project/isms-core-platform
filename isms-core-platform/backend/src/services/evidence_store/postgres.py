"""PostgreSQL EvidenceStore — thin wrapper keeping v1 connector_service behaviour."""
from __future__ import annotations

import logging
from typing import Any

from sqlalchemy.orm import Session

from .base import EvidenceStore, EvidenceItem

logger = logging.getLogger(__name__)


class PostgresEvidenceStore(EvidenceStore):
    """
    Delegates to the existing connector_service / evidence_service.
    EVIDENCE_STORE=postgres (default) — zero behaviour change from v1.

    db is required for write operations; search/get are not implemented here
    (they remain in their existing router handlers which call connector_service directly).
    """

    def __init__(self, db: Session):
        self._db = db

    def upsert(self, item: EvidenceItem, date_bucket: str | None = None) -> str:
        from src.services.connector_service import ingest_evidence
        from src.schemas.connectors import ConnectorEvidenceIngest

        schema = ConnectorEvidenceIngest(
            source_ref=item.resource_id,
            title=item.title,
            summary=item.summary,
            payload=item.payload,
            tags=item.tags,
            evidence_type=item.evidence_type,
        )
        rows = ingest_evidence(self._db, item.connector_id, [schema])
        doc_id = str(rows[0].id) if rows else item.resource_id
        item.doc_id = doc_id
        return doc_id

    def search(self, org_id: str, query: str = "", filters: dict[str, Any] | None = None, size: int = 50) -> list[dict[str, Any]]:
        raise NotImplementedError("Use connector_service.list_evidence for postgres backend")

    def get(self, org_id: str, doc_id: str) -> dict[str, Any] | None:
        raise NotImplementedError("Use connector_service.get_evidence for postgres backend")

    def delete(self, org_id: str, doc_id: str) -> bool:
        raise NotImplementedError("Use connector_service.delete_evidence for postgres backend")
