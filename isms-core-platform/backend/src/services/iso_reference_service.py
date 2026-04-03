"""ISO Reference Corpus Service.

Orchestrates loading of all ISO/regulatory PDFs into the OpenSearch
iso-reference index. Used by the QA page "Load Reference Corpus" action.
"""

import logging
from datetime import datetime, timezone
from pathlib import Path

from src.services import search_service
from src.services.iso_extractor import discover_documents, extract_chunks, infer_standard

logger = logging.getLogger(__name__)


def get_status() -> dict:
    """Return current state of the iso-reference index."""
    client = search_service.get_client()
    if not client:
        return {"available": False, "indexed": False, "total_chunks": 0, "standards": []}

    try:
        if not client.indices.exists(index=search_service.IDX_ISO_REFERENCE):
            return {"available": True, "indexed": False, "total_chunks": 0, "standards": []}

        count_result  = client.count(index=search_service.IDX_ISO_REFERENCE)
        total_chunks  = count_result.get("count", 0)

        # Aggregate by standard using terms aggregation
        agg_result = client.search(
            index=search_service.IDX_ISO_REFERENCE,
            body={
                "size": 0,
                "aggs": {
                    "by_standard": {
                        "terms": {"field": "standard", "size": 50}
                    }
                },
            },
        )
        standards = [
            {"standard": b["key"], "chunks": b["doc_count"]}
            for b in agg_result["aggregations"]["by_standard"]["buckets"]
        ]

        return {
            "available":    True,
            "indexed":      total_chunks > 0,
            "total_chunks": total_chunks,
            "standards":    standards,
        }
    except Exception as e:
        logger.error("Failed to get iso-reference status: %s", e)
        return {"available": False, "indexed": False, "total_chunks": 0, "standards": [], "error": str(e)}


def load_corpus(iso_root: str) -> dict:
    """Extract all ISO documents and index them into OpenSearch.

    Clears the existing iso-reference index before loading.
    Returns stats: {loaded_files, failed_files, total_chunks, standards, duration_ms}
    """
    import time
    t0 = time.monotonic()

    root = Path(iso_root)
    if not root.exists():
        return {
            "loaded_files":  0,
            "failed_files":  0,
            "total_chunks":  0,
            "standards":     [],
            "error":         f"ISO reference path not found: {iso_root}",
            "duration_ms":   0,
        }

    client = search_service.get_client()
    if not client:
        return {
            "loaded_files": 0,
            "failed_files": 0,
            "total_chunks": 0,
            "standards":    [],
            "error":        "OpenSearch not available",
            "duration_ms":  0,
        }

    # Ensure index exists (creates or re-creates)
    search_service.ensure_iso_reference_index()

    # Clear existing content
    try:
        client.delete_by_query(
            index=search_service.IDX_ISO_REFERENCE,
            body={"query": {"match_all": {}}},
            wait_for_completion=True,
        )
    except Exception as e:
        logger.warning("Could not clear iso-reference index: %s", e)

    documents = discover_documents(root)
    logger.info("Discovered %d documents under %s", len(documents), root)

    loaded_files  = 0
    failed_files  = 0
    total_chunks  = 0
    standard_counts: dict[str, int] = {}

    for doc_path in documents:
        standard = infer_standard(doc_path)
        logger.info("Processing %s → %s", doc_path.name, standard)

        try:
            chunks = extract_chunks(doc_path)
        except Exception as e:
            logger.error("Extraction failed for %s: %s", doc_path.name, e)
            failed_files += 1
            continue

        if not chunks:
            logger.warning("No chunks extracted from %s", doc_path.name)
            failed_files += 1
            continue

        # Bulk index into OpenSearch
        chunk_errors = 0
        for i, chunk in enumerate(chunks):
            doc_id = f"{standard}:{chunk['clause_id']}:{i}".replace(" ", "_").replace(":", "_")
            ok = search_service.index_iso_chunk(
                doc_id=doc_id,
                standard=chunk["standard"],
                clause_id=chunk["clause_id"],
                title=chunk["title"],
                text=chunk["text"],
                language=chunk.get("language", "en"),
                source_file=doc_path.name,
            )
            if ok:
                total_chunks += 1
            else:
                chunk_errors += 1

        if chunk_errors == len(chunks):
            failed_files += 1
        else:
            loaded_files += 1
            standard_counts[standard] = standard_counts.get(standard, 0) + len(chunks) - chunk_errors

    duration_ms = int((time.monotonic() - t0) * 1000)
    standards   = [{"standard": k, "chunks": v} for k, v in sorted(standard_counts.items())]

    logger.info(
        "ISO reference corpus loaded: %d files, %d chunks, %d failed, %dms",
        loaded_files, total_chunks, failed_files, duration_ms,
    )

    return {
        "loaded_files": loaded_files,
        "failed_files": failed_files,
        "total_chunks": total_chunks,
        "standards":    standards,
        "duration_ms":  duration_ms,
        "loaded_at":    datetime.now(timezone.utc).isoformat(),
    }
