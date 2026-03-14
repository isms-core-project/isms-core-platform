import logging

from sqlalchemy.orm import Session as DBSession

from src.core.config import get_settings
from src.importers.bundle_loader import BundleLoader

logger = logging.getLogger(__name__)


def load_all_bundles(db: DBSession) -> dict:
    """Load all dataset bundles into the database."""
    settings = get_settings()
    loader = BundleLoader(db, settings.datasets_path)
    return loader.load_all()


def needs_seed(db: DBSession) -> bool:
    """Check if the frameworks table is empty (first boot)."""
    from src.domain.frameworks import Framework
    result = db.query(Framework).first()
    return result is None
