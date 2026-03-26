"""
Startup dataset loader — called from entrypoint.sh after Alembic migrations.

Scans datasets/data/ and upserts any new or changed bundles into PostgreSQL.
Unchanged files (same content_hash) are skipped in milliseconds.
Idempotent: safe to run on every container start.

Usage (from backend/ directory):
    python3 -m src.cli.load_datasets
"""

import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="[datasets] %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> None:
    from src.database.session import SessionLocal
    from src.services.loader_service import load_all_bundles

    db = SessionLocal()
    try:
        logger.info("Loading reference datasets...")
        stats = load_all_bundles(db)
        logger.info(
            "Done — frameworks: %d, controls: %d, mappings: %d, skipped: %d",
            stats.get("frameworks", 0),
            stats.get("controls", 0),
            stats.get("mappings", 0),
            stats.get("skipped", 0),
        )
    except Exception as e:
        logger.error("Dataset load failed: %s", e)
        sys.exit(1)
    finally:
        db.close()


if __name__ == "__main__":
    main()
