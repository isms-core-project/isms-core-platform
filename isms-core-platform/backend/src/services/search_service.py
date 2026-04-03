"""OpenSearch search service — full-text indexing and search for ISMS CORE.

Provides:
- Client singleton with lazy initialization
- Index lifecycle management (create, ensure, delete)
- Document indexing (implementations and policies)
- Full-text search across both indices
- Graceful degradation when OpenSearch is unavailable
"""

import logging
from datetime import datetime, timezone

from opensearchpy import OpenSearch

from src.core.config import get_settings

logger = logging.getLogger(__name__)

# Index names
IDX_IMPLEMENTATIONS = "isms-implementations"
IDX_POLICIES = "isms-policies"
IDX_EVIDENCE = "isms-evidence"

# Client singleton
_client: OpenSearch | None = None


# ------------------------------------------------------------------
# Client management
# ------------------------------------------------------------------


def get_client() -> OpenSearch | None:
    """Lazy-init OpenSearch client. Returns None if connection fails."""
    global _client
    if _client is not None:
        # Quick ping to verify connection is still alive
        try:
            _client.info()
            return _client
        except Exception:
            _client = None

    settings = get_settings()
    try:
        client = OpenSearch(
            hosts=[settings.opensearch_url],
            use_ssl=False,
            verify_certs=False,
            timeout=10,
            max_retries=2,
            retry_on_timeout=True,
        )
        info = client.info()
        logger.info(
            "OpenSearch connected: %s",
            info.get("version", {}).get("number", "unknown"),
        )
        _client = client
        return _client
    except Exception as e:
        logger.debug("OpenSearch not available: %s", e)
        return None


def reset_client():
    """Reset client singleton (for reconnection after failure)."""
    global _client
    _client = None


def is_available() -> bool:
    """Quick health probe. get_client() already verifies connectivity."""
    return get_client() is not None


# ------------------------------------------------------------------
# Index mappings
# ------------------------------------------------------------------

_SHARED_SETTINGS = {
    "number_of_shards": 1,
    "number_of_replicas": 0,
    "analysis": {
        "analyzer": {
            "isms_analyzer": {
                "type": "custom",
                "tokenizer": "standard",
                "filter": ["lowercase", "stop", "snowball"],
            }
        }
    },
}

_IMPL_MAPPING = {
    "settings": _SHARED_SETTINGS,
    "mappings": {
        "properties": {
            "document_id": {"type": "keyword"},
            "title": {
                "type": "text",
                "analyzer": "isms_analyzer",
                "fields": {"raw": {"type": "keyword"}},
            },
            "impl_type": {"type": "keyword"},
            "control_group_code": {"type": "keyword"},
            "control_group_name": {
                "type": "text",
                "analyzer": "isms_analyzer",
            },
            "product_type": {"type": "keyword"},
            "full_text": {"type": "text", "analyzer": "isms_analyzer"},
            "sections": {
                "type": "nested",
                "properties": {
                    "heading": {"type": "text", "analyzer": "isms_analyzer"},
                    "body": {"type": "text", "analyzer": "isms_analyzer"},
                    "level": {"type": "integer"},
                },
            },
            "language": {"type": "keyword"},
            "word_count": {"type": "integer"},
            "metadata": {"type": "object", "enabled": False},
            "file_path": {"type": "keyword"},
            "indexed_at": {"type": "date"},
        }
    },
}

_EVIDENCE_MAPPING = {
    "settings": _SHARED_SETTINGS,
    "mappings": {
        "properties": {
            "evidence_id": {"type": "keyword"},
            "title": {
                "type": "text",
                "analyzer": "isms_analyzer",
                "fields": {"raw": {"type": "keyword"}},
            },
            "evidence_type": {"type": "keyword"},
            "control_group_code": {"type": "keyword"},
            "original_filename": {"type": "keyword"},
            "full_text": {"type": "text", "analyzer": "isms_analyzer"},
            "word_count": {"type": "integer"},
            "file_path": {"type": "keyword"},
            "indexed_at": {"type": "date"},
        }
    },
}

_POLICY_MAPPING = {
    "settings": _SHARED_SETTINGS,
    "mappings": {
        "properties": {
            "document_id": {"type": "keyword"},
            "title": {
                "type": "text",
                "analyzer": "isms_analyzer",
                "fields": {"raw": {"type": "keyword"}},
            },
            "policy_type": {"type": "keyword"},
            "product_type": {"type": "keyword"},
            "control_group_code": {"type": "keyword"},
            "control_group_name": {
                "type": "text",
                "analyzer": "isms_analyzer",
            },
            "full_text": {"type": "text", "analyzer": "isms_analyzer"},
            "sections": {
                "type": "nested",
                "properties": {
                    "heading": {"type": "text", "analyzer": "isms_analyzer"},
                    "body": {"type": "text", "analyzer": "isms_analyzer"},
                    "level": {"type": "integer"},
                },
            },
            "requirements": {
                "type": "nested",
                "properties": {
                    "text": {"type": "text", "analyzer": "isms_analyzer"},
                    "type": {"type": "keyword"},
                    "section": {"type": "text"},
                },
            },
            "language": {"type": "keyword"},
            "word_count": {"type": "integer"},
            "metadata": {"type": "object", "enabled": False},
            "indexed_at": {"type": "date"},
        }
    },
}


# ------------------------------------------------------------------
# Index lifecycle
# ------------------------------------------------------------------


def ensure_indices() -> bool:
    """Create indices if they don't exist. Returns True if successful."""
    client = get_client()
    if not client:
        return False
    try:
        _language_field = {"properties": {"language": {"type": "keyword"}}}
        for idx, mapping in [
            (IDX_IMPLEMENTATIONS, _IMPL_MAPPING),
            (IDX_POLICIES, _POLICY_MAPPING),
            (IDX_EVIDENCE, _EVIDENCE_MAPPING),
        ]:
            if not client.indices.exists(index=idx):
                client.indices.create(index=idx, body=mapping)
                logger.info("Created index: %s", idx)
            else:
                # Ensure language field exists (idempotent)
                client.indices.put_mapping(index=idx, body=_language_field)
                logger.debug("Index already exists: %s", idx)
        return True
    except Exception as e:
        logger.error("Failed to ensure indices: %s", e)
        return False


def delete_indices() -> bool:
    """Delete both indices (for reindex). Returns True if successful."""
    client = get_client()
    if not client:
        return False
    try:
        for idx in [IDX_IMPLEMENTATIONS, IDX_POLICIES, IDX_EVIDENCE]:
            if client.indices.exists(index=idx):
                client.indices.delete(index=idx)
                logger.info("Deleted index: %s", idx)
        return True
    except Exception as e:
        logger.error("Failed to delete indices: %s", e)
        return False


# ------------------------------------------------------------------
# Document indexing
# ------------------------------------------------------------------


def index_implementation(
    document_id: str,
    title: str,
    impl_type: str,
    control_group_code: str,
    control_group_name: str,
    product_type: str,
    sections: list[dict],
    word_count: int,
    file_path: str,
    language: str = "en",
    metadata: dict | None = None,
) -> bool:
    """Index a single implementation document. Returns True on success."""
    client = get_client()
    if not client:
        return False
    try:
        full_text = "\n\n".join(
            f"{s['heading']}\n{s['body']}" for s in sections
        )
        doc = {
            "document_id": document_id,
            "title": title,
            "impl_type": impl_type,
            "control_group_code": control_group_code,
            "control_group_name": control_group_name,
            "product_type": product_type,
            "language": language,
            "full_text": full_text,
            "sections": sections,
            "word_count": word_count,
            "file_path": file_path,
            "metadata": metadata or {},
            "indexed_at": datetime.now(timezone.utc).isoformat(),
        }
        client.index(
            index=IDX_IMPLEMENTATIONS,
            id=document_id,
            body=doc,
        )
        return True
    except Exception as e:
        logger.warning("Failed to index implementation %s: %s", document_id, e)
        return False


def index_policy(
    document_id: str,
    title: str,
    policy_type: str,
    product_type: str,
    control_group_code: str,
    control_group_name: str,
    sections: list[dict],
    requirements: list[dict],
    word_count: int,
    language: str = "en",
    metadata: dict | None = None,
) -> bool:
    """Index a single policy document. Returns True on success."""
    client = get_client()
    if not client:
        return False
    try:
        full_text = "\n\n".join(
            f"{s['heading']}\n{s['body']}" for s in sections
        )
        doc = {
            "document_id": document_id,
            "title": title,
            "policy_type": policy_type,
            "product_type": product_type,
            "control_group_code": control_group_code,
            "control_group_name": control_group_name,
            "language": language,
            "full_text": full_text,
            "sections": sections,
            "requirements": requirements,
            "word_count": word_count,
            "metadata": metadata or {},
            "indexed_at": datetime.now(timezone.utc).isoformat(),
        }
        client.index(
            index=IDX_POLICIES,
            id=document_id,
            body=doc,
        )
        return True
    except Exception as e:
        logger.warning("Failed to index policy %s: %s", document_id, e)
        return False


def index_evidence(
    evidence_id: str,
    title: str,
    evidence_type: str,
    control_group_code: str,
    original_filename: str,
    text: str,
    word_count: int,
    file_path: str,
) -> bool:
    """Index evidence document text. Returns True on success."""
    client = get_client()
    if not client:
        return False
    try:
        doc = {
            "evidence_id": evidence_id,
            "title": title,
            "evidence_type": evidence_type,
            "control_group_code": control_group_code,
            "original_filename": original_filename,
            "full_text": text,
            "word_count": word_count,
            "file_path": file_path,
            "indexed_at": datetime.now(timezone.utc).isoformat(),
        }
        client.index(index=IDX_EVIDENCE, id=evidence_id, body=doc)
        return True
    except Exception as e:
        logger.warning("Failed to index evidence %s: %s", evidence_id, e)
        return False


def delete_evidence(evidence_id: str) -> bool:
    """Remove evidence document from index. Returns True on success."""
    client = get_client()
    if not client:
        return False
    try:
        client.delete(index=IDX_EVIDENCE, id=evidence_id, ignore=[404])
        return True
    except Exception as e:
        logger.warning("Failed to delete evidence %s from index: %s", evidence_id, e)
        return False


# ------------------------------------------------------------------
# Search
# ------------------------------------------------------------------


def search_all(
    query: str,
    doc_type: str | None = None,
    control_group: str | None = None,
    product_type: str | None = None,
    impl_type: str | None = None,
    policy_type: str | None = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """Full-text search across implementations and/or policies.

    Returns: {"total": int, "hits": [...], "took_ms": int, "available": bool}
    """
    client = get_client()
    if not client:
        return {"total": 0, "hits": [], "took_ms": 0, "available": False}

    # Determine which indices to search
    if doc_type == "implementation":
        indices = [IDX_IMPLEMENTATIONS]
    elif doc_type == "policy":
        indices = [IDX_POLICIES]
    else:
        indices = [IDX_IMPLEMENTATIONS, IDX_POLICIES]

    # Build query
    must = [
        {
            "multi_match": {
                "query": query,
                "fields": [
                    "title^3",
                    "full_text",
                    "sections.heading^2",
                    "sections.body",
                ],
                "type": "best_fields",
                "fuzziness": "AUTO",
            }
        }
    ]

    filter_clauses = []
    if control_group:
        filter_clauses.append(
            {"term": {"control_group_code": control_group.lower()}}
        )
    if product_type:
        filter_clauses.append({"term": {"product_type": product_type}})
    if impl_type:
        filter_clauses.append({"term": {"impl_type": impl_type}})
    if policy_type:
        filter_clauses.append({"term": {"policy_type": policy_type}})

    body = {
        "query": {
            "bool": {
                "must": must,
                "filter": filter_clauses,
            }
        },
        "highlight": {
            "fields": {
                "full_text": {
                    "fragment_size": 200,
                    "number_of_fragments": 3,
                },
                "title": {},
            },
            "pre_tags": ["<mark>"],
            "post_tags": ["</mark>"],
        },
        "from": offset,
        "size": limit,
        "_source": {"excludes": ["full_text"]},
    }

    try:
        result = client.search(index=",".join(indices), body=body)
        hits = []
        for hit in result["hits"]["hits"]:
            source = hit["_source"]
            highlights = hit.get("highlight", {})
            snippet_parts = highlights.get("full_text", [])
            snippet = " ... ".join(snippet_parts[:3]) if snippet_parts else ""

            hits.append(
                {
                    "document_id": source.get("document_id"),
                    "title": source.get("title"),
                    "type": (
                        "implementation"
                        if hit["_index"] == IDX_IMPLEMENTATIONS
                        else "policy"
                    ),
                    "score": hit["_score"],
                    "control_group_code": source.get("control_group_code"),
                    "control_group_name": source.get("control_group_name"),
                    "product_type": source.get("product_type"),
                    "impl_type": source.get("impl_type"),
                    "policy_type": source.get("policy_type"),
                    "word_count": source.get("word_count"),
                    "highlights": highlights,
                    "snippet": snippet,
                }
            )

        return {
            "total": result["hits"]["total"]["value"],
            "hits": hits,
            "took_ms": result["took"],
            "available": True,
        }
    except Exception as e:
        logger.error("Search failed: %s", e)
        return {
            "total": 0,
            "hits": [],
            "took_ms": 0,
            "available": False,
            "error": str(e),
        }


# ------------------------------------------------------------------
# Status / stats
# ------------------------------------------------------------------


def get_search_status() -> dict:
    """Return OpenSearch cluster health and index document counts."""
    client = get_client()
    if not client:
        return {"available": False}
    try:
        health = client.cluster.health()
        counts = {}
        for idx in [IDX_IMPLEMENTATIONS, IDX_POLICIES, IDX_EVIDENCE]:
            if client.indices.exists(index=idx):
                stats = client.count(index=idx)
                counts[idx] = stats.get("count", 0)
            else:
                counts[idx] = None
        return {
            "available": True,
            "cluster_status": health.get("status"),
            "indices": counts,
        }
    except Exception as e:
        return {"available": False, "error": str(e)}
