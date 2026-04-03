"""ISO Reference Corpus Service.

Loads pre-extracted ISO/regulatory reference chunks into OpenSearch.

Two modes:
  1. From JSON seeds (production/auto-bootstrap):
     Reads datasets/data/iso-reference/*.json files baked into the image.
     Called automatically on startup if the index is empty.

  2. From PDFs (admin re-extraction):
     Calls iso_extractor to re-process PDFs from the iso_reference_path mount.
     Used when updating seeds after a new ISO version is released.
     Triggered via QA → Reference Corpus → Reload.
"""

import json
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


def _seeds_dir() -> Path:
    """Locate the datasets/data/iso-reference directory baked into the image."""
    # When running in Docker: /app/datasets/iso-reference
    # When running locally:   find relative to this file
    candidates = [
        Path("/app/datasets/iso-reference"),
        Path(__file__).resolve().parents[3] / "datasets" / "data" / "iso-reference",
    ]
    for p in candidates:
        if p.exists():
            return p
    return candidates[0]  # may not exist — caller handles


def load_from_seeds() -> dict:
    """Load pre-extracted JSON seed files into OpenSearch iso-reference index.

    Called automatically on startup if the index is empty.
    Returns stats dict.
    """
    import time
    t0 = time.monotonic()

    seeds_dir = _seeds_dir()
    if not seeds_dir.exists():
        logger.warning("ISO reference seeds directory not found: %s", seeds_dir)
        return {"loaded_files": 0, "failed_files": 0, "total_chunks": 0,
                "standards": [], "duration_ms": 0, "source": "seeds"}

    seed_files = [f for f in seeds_dir.glob("*.json") if not f.name.startswith("_")]
    if not seed_files:
        logger.warning("No JSON seed files found in %s", seeds_dir)
        return {"loaded_files": 0, "failed_files": 0, "total_chunks": 0,
                "standards": [], "duration_ms": 0, "source": "seeds"}

    client = search_service.get_client()
    if not client:
        return {"loaded_files": 0, "failed_files": 0, "total_chunks": 0,
                "standards": [], "error": "OpenSearch not available",
                "duration_ms": 0, "source": "seeds"}

    search_service.ensure_iso_reference_index()

    total_chunks = 0
    loaded_files = 0
    failed_files = 0
    standard_counts: dict[str, int] = {}

    for seed_file in sorted(seed_files):
        try:
            chunks: list[dict] = json.loads(seed_file.read_text(encoding="utf-8"))
        except Exception as e:
            logger.error("Failed to read seed file %s: %s", seed_file.name, e)
            failed_files += 1
            continue

        chunk_errors = 0
        for i, chunk in enumerate(chunks):
            standard = chunk.get("standard", seed_file.stem)
            doc_id = f"{standard}:{chunk['clause_id']}:{i}".replace(" ", "_").replace(":", "_")
            ok = search_service.index_iso_chunk(
                doc_id=doc_id,
                standard=standard,
                clause_id=chunk.get("clause_id", f"chunk-{i}"),
                title=chunk.get("title", ""),
                text=chunk.get("text", ""),
                language=chunk.get("language", "en"),
                source_file=chunk.get("source_file", seed_file.name),
            )
            if ok:
                total_chunks += 1
                standard_counts[standard] = standard_counts.get(standard, 0) + 1
            else:
                chunk_errors += 1

        if chunk_errors == len(chunks):
            failed_files += 1
        else:
            loaded_files += 1

    duration_ms = int((time.monotonic() - t0) * 1000)
    standards = [{"standard": k, "chunks": v} for k, v in sorted(standard_counts.items())]

    logger.info(
        "ISO reference seeds loaded: %d files, %d chunks, %dms",
        loaded_files, total_chunks, duration_ms,
    )
    return {
        "loaded_files": loaded_files,
        "failed_files": failed_files,
        "total_chunks": total_chunks,
        "standards":    standards,
        "duration_ms":  duration_ms,
        "loaded_at":    datetime.now(timezone.utc).isoformat(),
        "source":       "seeds",
    }


def needs_seed() -> bool:
    """Return True if the iso-reference index is empty and should be seeded."""
    client = search_service.get_client()
    if not client:
        return False
    try:
        if not client.indices.exists(index=search_service.IDX_ISO_REFERENCE):
            return True
        count = client.count(index=search_service.IDX_ISO_REFERENCE).get("count", 0)
        return count == 0
    except Exception:
        return False


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
