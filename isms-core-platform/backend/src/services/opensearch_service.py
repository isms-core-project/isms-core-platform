"""OpenSearch operational service — org provisioning, ISM/SM status, evidence index management."""
from __future__ import annotations

import logging
from typing import Any

from src.services.search_service import get_client

logger = logging.getLogger(__name__)


# ── Org provisioning (Phase 5) ────────────────────────────────────────────────

def provision_org(org_id: str) -> bool:
    """
    Create evidence-{org_id} index for a new org.
    The index template applies mapping + ISM policy automatically.
    Idempotent — safe to call multiple times.
    Returns True if created, False if already existed or OpenSearch unavailable.
    """
    client = get_client()
    if not client:
        logger.warning("OpenSearch unavailable — skipping org provisioning for %s", org_id)
        return False

    index = f"evidence-{org_id}"
    try:
        if client.indices.exists(index=index):
            logger.debug("OpenSearch index already exists: %s", index)
            return False
        client.indices.create(index=index)
        logger.info("OpenSearch index created: %s", index)
        return True
    except Exception as exc:
        logger.warning("Failed to provision OpenSearch index %s: %s", index, exc)
        return False


# ── ISM policy status (Phase 7) ───────────────────────────────────────────────

def get_ism_policies() -> list[dict[str, Any]]:
    """Return ISM policies with their current state machine definition."""
    client = get_client()
    if not client:
        return []
    try:
        resp = client.transport.perform_request("GET", "/_plugins/_ism/policies")
        policies = resp.get("policies", [])
        return [
            {
                "id": p.get("_id"),
                "description": p.get("policy", {}).get("description", ""),
                "default_state": p.get("policy", {}).get("default_state"),
                "states": [s["name"] for s in p.get("policy", {}).get("states", [])],
                "last_updated_time": p.get("policy", {}).get("last_updated_time"),
            }
            for p in policies
        ]
    except Exception as exc:
        logger.warning("Failed to fetch ISM policies: %s", exc)
        return []


def get_ism_managed_indices() -> list[dict[str, Any]]:
    """Return ISM managed index states (which indices are in which ISM state)."""
    client = get_client()
    if not client:
        return []
    try:
        resp = client.transport.perform_request("GET", "/_plugins/_ism/explain?size=50")
        managed = resp.get("managed_indices", [])
        return [
            {
                "index": m.get("index"),
                "policy_id": m.get("policy_id"),
                "state": m.get("state", {}).get("name") if isinstance(m.get("state"), dict) else m.get("state"),
                "action": m.get("action", {}).get("name") if isinstance(m.get("action"), dict) else None,
            }
            for m in managed
        ]
    except Exception as exc:
        logger.warning("Failed to fetch ISM managed indices: %s", exc)
        return []


# ── Snapshot Management status (Phase 7) ─────────────────────────────────────

def get_sm_policies() -> list[dict[str, Any]]:
    """Return SM snapshot policies with status."""
    client = get_client()
    if not client:
        return []
    try:
        resp = client.transport.perform_request("GET", "/_plugins/_sm/policies")
        policies = resp.get("policies", [])
        return [
            {
                "id": p.get("_id"),
                "description": p.get("sm_policy", {}).get("description", ""),
                "repository": p.get("sm_policy", {}).get("snapshot_config", {}).get("repository"),
                "creation_schedule": p.get("sm_policy", {}).get("creation", {}).get("schedule", {}).get("cron", {}).get("expression"),
                "enabled": p.get("sm_policy", {}).get("enabled", True),
                "last_creation": p.get("sm_policy", {}).get("creation", {}).get("latest_execution", {}).get("status"),
                "last_creation_time": p.get("sm_policy", {}).get("creation", {}).get("latest_execution", {}).get("end_time"),
            }
            for p in policies
        ]
    except Exception as exc:
        logger.warning("Failed to fetch SM policies: %s", exc)
        return []


def get_snapshot_repos() -> list[dict[str, Any]]:
    """Return registered snapshot repositories."""
    client = get_client()
    if not client:
        return []
    try:
        resp = client.snapshot.get_repository()
        return [
            {
                "name": name,
                "type": info.get("type"),
                "bucket": info.get("settings", {}).get("bucket"),
                "endpoint": info.get("settings", {}).get("endpoint"),
            }
            for name, info in resp.items()
        ]
    except Exception as exc:
        logger.warning("Failed to fetch snapshot repositories: %s", exc)
        return []


# ── Evidence indices per org (Phase 7) ────────────────────────────────────────

def get_evidence_indices() -> list[dict[str, Any]]:
    """Return all evidence-* indices with doc counts."""
    client = get_client()
    if not client:
        return []
    try:
        resp = client.cat.indices(index="evidence-*", h="index,docs.count,store.size", format="json")
        return [
            {
                "index": r.get("index"),
                "doc_count": int(r.get("docs.count") or 0),
                "store_size": r.get("store.size"),
            }
            for r in (resp or [])
        ]
    except Exception as exc:
        logger.warning("Failed to fetch evidence indices: %s", exc)
        return []
