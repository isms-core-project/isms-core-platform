from __future__ import annotations

import hashlib
import logging
from datetime import datetime, timezone
from typing import Any

from opensearchpy import OpenSearch, NotFoundError

from src.core.config import get_settings
from .base import EvidenceStore, EvidenceItem

logger = logging.getLogger(__name__)


def _get_client() -> OpenSearch:
    s = get_settings()
    return OpenSearch(
        hosts=[s.opensearch_url],
        use_ssl=False,
        verify_certs=False,
    )


def _doc_id(connector_id: str, org_id: str, resource_id: str, date_bucket: str) -> str:
    raw = f"{connector_id}:{org_id}:{resource_id}:{date_bucket}"
    return hashlib.sha256(raw.encode()).hexdigest()


def _index(org_id: str) -> str:
    return f"evidence-{org_id}"


class OpenSearchEvidenceStore(EvidenceStore):

    def upsert(self, item: EvidenceItem, date_bucket: str | None = None) -> str:
        client = _get_client()
        bucket = date_bucket or datetime.now(timezone.utc).strftime("%Y-%m-%d")
        doc_id = _doc_id(item.connector_id, item.org_id, item.resource_id, bucket)

        doc = {
            "org_id": item.org_id,
            "connector_id": item.connector_id,
            "resource_id": item.resource_id,
            "evidence_type": item.evidence_type,
            "title": item.title,
            "summary": item.summary,
            "payload": item.payload,
            "control_ids": item.control_ids,
            "tags": item.tags,
            "file_refs": item.file_refs,
            "collected_at": (item.collected_at or datetime.now(timezone.utc)).isoformat(),
            "status": "active",
            "source_system": item.source_system or "",
        }

        # Merge source-specific promoted fields (Phase 39a)
        if item.promoted:
            doc.update(item.promoted)

        index = item.os_index if item.os_index else _index(item.org_id)
        client.index(index=index, id=doc_id, body=doc)
        logger.debug("upserted evidence %s → %s/%s", item.resource_id, index, doc_id)
        item.doc_id = doc_id
        return doc_id

    def search(
        self,
        org_id: str,
        query: str = "",
        filters: dict[str, Any] | None = None,
        size: int = 50,
    ) -> list[dict[str, Any]]:
        client = _get_client()
        must: list[dict] = [{"term": {"org_id": org_id}}]

        if query:
            must.append({"multi_match": {"query": query, "fields": ["title", "summary"]}})

        if filters:
            for k, v in filters.items():
                must.append({"term": {k: v}})

        body = {"query": {"bool": {"must": must}}, "size": size}
        try:
            resp = client.search(index=_index(org_id), body=body)
            return [h["_source"] | {"_id": h["_id"]} for h in resp["hits"]["hits"]]
        except Exception:
            return []

    def get(self, org_id: str, doc_id: str) -> dict[str, Any] | None:
        client = _get_client()
        try:
            resp = client.get(index=_index(org_id), id=doc_id)
            return resp["_source"] | {"_id": doc_id}
        except NotFoundError:
            return None

    def delete(self, org_id: str, doc_id: str) -> bool:
        client = _get_client()
        try:
            client.delete(index=_index(org_id), id=doc_id)
            return True
        except NotFoundError:
            return False
