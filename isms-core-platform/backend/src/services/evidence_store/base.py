from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class EvidenceItem:
    connector_id: str
    org_id: str
    resource_id: str
    evidence_type: str
    title: str
    summary: str
    payload: dict[str, Any]
    control_ids: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    collected_at: datetime | None = None
    # Per-source routing (Phase 39a)
    source_system: str = ""      # e.g. "entra_id", "o365", "defender"
    os_index: str = ""           # target OpenSearch index; empty = fall back to evidence-{org_id}
    promoted: dict[str, Any] = field(default_factory=dict)  # promoted fields from raw payload
    # Populated after upsert
    doc_id: str = ""
    file_refs: list[str] = field(default_factory=list)


class EvidenceStore(ABC):
    @abstractmethod
    def upsert(self, item: EvidenceItem, date_bucket: str | None = None) -> str:
        """Upsert evidence. Returns doc_id."""

    @abstractmethod
    def search(
        self,
        org_id: str,
        query: str = "",
        filters: dict[str, Any] | None = None,
        size: int = 50,
    ) -> list[dict[str, Any]]:
        """Search evidence for an org. Returns list of raw hit dicts."""

    @abstractmethod
    def get(self, org_id: str, doc_id: str) -> dict[str, Any] | None:
        """Fetch a single evidence document."""

    @abstractmethod
    def delete(self, org_id: str, doc_id: str) -> bool:
        """Delete a document. Returns True if deleted."""
