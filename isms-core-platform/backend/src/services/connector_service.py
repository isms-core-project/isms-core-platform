"""Service layer for v2.0 connector evidence ingestion."""

import hashlib
import logging
import secrets
from datetime import datetime, timedelta, timezone

from src.utils.encryption import decrypt_config, encrypt_config

from sqlalchemy import select, func, update as sa_update
from sqlalchemy.orm import Session as DBSession

from src.domain.connectors import Connector, ConnectorEvidence
from src.domain.control_groups import ControlGroup
from src.database.enums import ProductFamily
from src.schemas.connectors import ConnectorEvidenceIngest, ConnectorRegister

logger = logging.getLogger(__name__)


# ── Token helpers ─────────────────────────────────────────────────────────────

def _generate_token() -> tuple[str, str]:
    """Return (plain_token, sha256_hash). Store hash, return plain once."""
    plain = secrets.token_urlsafe(32)
    hashed = hashlib.sha256(plain.encode()).hexdigest()
    return plain, hashed


def _hash_token(plain: str) -> str:
    return hashlib.sha256(plain.encode()).hexdigest()


# ── Connector management ──────────────────────────────────────────────────────

def register_connector(db: DBSession, payload: ConnectorRegister) -> tuple[Connector, str]:
    """Create a new connector and return (connector, plain_token)."""
    plain, hashed = _generate_token()
    connector = Connector(
        name=payload.name,
        source_system=payload.source_system,
        api_token_hash=hashed,
        status="active",
    )
    db.add(connector)
    db.commit()
    db.refresh(connector)
    logger.info("Connector registered: %s (%s)", connector.name, connector.source_system)
    return connector, plain


def list_connectors(db: DBSession) -> list[dict]:
    """List connectors with live evidence_count from the DB."""
    evidence_subq = (
        select(ConnectorEvidence.connector_id, func.count().label("evidence_count"))
        .group_by(ConnectorEvidence.connector_id)
        .subquery()
    )
    rows = db.execute(
        select(Connector, func.coalesce(evidence_subq.c.evidence_count, 0).label("evidence_count"))
        .outerjoin(evidence_subq, Connector.id == evidence_subq.c.connector_id)
        .order_by(Connector.created_at)
    ).all()
    return [{**c.__dict__, "evidence_count": cnt} for c, cnt in rows]


def get_connector_by_id(db: DBSession, connector_id) -> Connector | None:
    return db.get(Connector, connector_id)


def deregister_connector(db: DBSession, connector: Connector) -> None:
    db.delete(connector)
    db.commit()


def get_connector_by_token(db: DBSession, plain_token: str) -> Connector | None:
    """Validate a connector bearer token. Returns Connector or None."""
    hashed = _hash_token(plain_token)
    return db.execute(
        select(Connector).where(
            Connector.api_token_hash == hashed,
            Connector.status == "active",
        )
    ).scalar_one_or_none()


# ── Sync trigger ──────────────────────────────────────────────────────────────

def request_sync(db: DBSession, connector: Connector) -> None:
    """Flag a connector for immediate sync on its next 30s sleep-check tick."""
    connector.sync_requested_at = datetime.now(timezone.utc)
    db.commit()
    logger.info("Sync requested: %s", connector.name)


def pop_sync_requested(db: DBSession, connector: Connector) -> bool:
    """Return True if a sync was pending and clear the flag atomically."""
    if connector.sync_requested_at is None:
        return False
    connector.sync_requested_at = None
    db.commit()
    return True


# ── Connector config (GUI-managed credentials) ────────────────────────────────

def store_config(db: DBSession, connector: Connector, config: dict) -> None:
    """Encrypt and persist config dict (credentials) for a connector."""
    connector.config_encrypted = encrypt_config(config) if config else None
    db.commit()
    logger.info("Connector %s: config updated", connector.name)


def rename_connector(db: DBSession, connector: Connector, name: str) -> None:
    """Update the display name of a connector."""
    connector.name = name.strip()
    db.commit()
    logger.info("Connector %s renamed to: %s", connector.id, connector.name)


def get_connector_config(db: DBSession, connector: Connector) -> dict:
    """Return decrypted config dict, or empty dict if none stored."""
    if not connector.config_encrypted:
        return {}
    try:
        return decrypt_config(connector.config_encrypted)
    except Exception as e:
        logger.error("Connector %s: failed to decrypt config: %s", connector.name, e)
        return {}


# ── Evidence ingestion ────────────────────────────────────────────────────────

def _resolve_control_group(db: DBSession, group_code: str) -> ControlGroup | None:
    """Resolve group code case-insensitively (connector sends 'a.8.8' or 'A.8.8')."""
    return db.execute(
        select(ControlGroup).where(
            ControlGroup.group_code.ilike(group_code)
        )
    ).scalar_one_or_none()


def ingest_evidence(
    db: DBSession,
    connector: Connector,
    items: list[ConnectorEvidenceIngest],
) -> dict:
    """Bulk-ingest evidence items from a connector. Returns accepted/skipped/errors counts."""
    accepted = skipped = errors = 0

    for item in items:
        try:
            group = _resolve_control_group(db, item.group_code)
            if not group:
                logger.warning("Connector %s: unknown group_code '%s' — skipping", connector.name, item.group_code)
                errors += 1
                continue

            # Duplicate check — source_ref must be unique per connector
            if item.source_ref:
                existing = db.execute(
                    select(ConnectorEvidence).where(
                        ConnectorEvidence.connector_id == connector.id,
                        ConnectorEvidence.source_ref == item.source_ref,
                    )
                ).scalar_one_or_none()
                if existing:
                    skipped += 1
                    continue

            evidence = ConnectorEvidence(
                connector_id=connector.id,
                control_group_id=group.id,
                source_ref=item.source_ref,
                source_url=item.source_url,
                title=item.title,
                classification=item.classification,
                status=item.status,
                event_date=item.event_date,
                raw=item.raw,
            )
            db.add(evidence)
            accepted += 1

        except Exception as e:
            logger.error("Connector %s: error ingesting item '%s': %s", connector.name, item.source_ref, e)
            errors += 1

    if accepted:
        # Update connector sync stats and clear any previous error
        connector.last_run = datetime.now(timezone.utc)
        connector.last_item_count = accepted
        connector.last_error = None
        connector.last_error_at = None
        db.commit()
    elif errors == 0 and skipped > 0:
        # All duplicates — still update last_run and clear error
        connector.last_run = datetime.now(timezone.utc)
        connector.last_error = None
        connector.last_error_at = None
        db.commit()

    logger.info("Connector %s ingest: accepted=%d skipped=%d errors=%d", connector.name, accepted, skipped, errors)
    return {"accepted": accepted, "skipped": skipped, "errors": errors}


def report_error(db: DBSession, connector: Connector, message: str) -> None:
    """Record that a connector sync failed with an error message."""
    connector.last_error = message[:2000]  # cap at 2000 chars
    connector.last_error_at = datetime.now(timezone.utc)
    db.commit()
    logger.warning("Connector %s reported error: %s", connector.name, message[:200])


# ── Evidence queries ──────────────────────────────────────────────────────────

def list_evidence_for_group(db: DBSession, control_group_id, limit: int = 100) -> list[dict]:
    rows = db.execute(
        select(ConnectorEvidence, ControlGroup.group_code)
        .join(ControlGroup, ConnectorEvidence.control_group_id == ControlGroup.id)
        .where(ConnectorEvidence.control_group_id == control_group_id)
        .order_by(ConnectorEvidence.event_date.desc().nulls_last())
        .limit(limit)
    ).all()
    return [{**ev.__dict__, "group_code": gc} for ev, gc in rows]


def count_evidence_for_group(db: DBSession, control_group_id) -> int:
    from sqlalchemy import func
    result = db.execute(
        select(func.count()).select_from(ConnectorEvidence).where(
            ConnectorEvidence.control_group_id == control_group_id
        )
    ).scalar()
    return result or 0


def list_all_evidence(
    db: DBSession,
    limit: int = 200,
    product_family: str | None = None,
    include_archived: bool = False,
) -> list[dict]:
    """List all automated evidence across all control groups, most recent first."""
    q = (
        select(ConnectorEvidence, ControlGroup.group_code)
        .join(ControlGroup, ConnectorEvidence.control_group_id == ControlGroup.id)
        .order_by(ConnectorEvidence.event_date.desc().nulls_last())
        .limit(limit)
    )
    if not include_archived:
        q = q.where(ConnectorEvidence.archived_at.is_(None))
    if product_family:
        try:
            pf = ProductFamily(product_family.upper())
            q = q.where(ControlGroup.product_family == pf)
        except ValueError:
            pass
    rows = db.execute(q).all()
    return [{**ev.__dict__, "group_code": gc} for ev, gc in rows]


def delete_evidence_item(db: DBSession, evidence_id) -> bool:
    """Delete a single evidence item by ID. Returns True if found and deleted."""
    import uuid as _uuid
    try:
        eid = _uuid.UUID(str(evidence_id))
    except (ValueError, AttributeError):
        return False
    item = db.get(ConnectorEvidence, eid)
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True


def delete_connector_evidence(db: DBSession, connector: Connector) -> int:
    """Delete all evidence items for a connector. Returns count deleted."""
    from sqlalchemy import delete as sa_delete
    result = db.execute(
        sa_delete(ConnectorEvidence).where(ConnectorEvidence.connector_id == connector.id)
    )
    db.commit()
    return result.rowcount


# ── Archiving ─────────────────────────────────────────────────────────────────

GLOBAL_RETENTION_DAYS = 90  # default if connector has no retention_days set


def set_retention_days(db: DBSession, connector: Connector, days: int | None) -> None:
    """Set per-connector retention period. None = revert to global default."""
    connector.retention_days = days
    db.commit()


def archive_old_evidence(db: DBSession, connector: Connector | None = None) -> int:
    """Soft-archive evidence older than the retention period.

    If connector is provided, only archives evidence for that connector using its
    retention_days (or global default). If connector is None, runs globally across
    all connectors using per-connector or global retention.

    Returns number of items archived.
    """
    now = datetime.now(timezone.utc)

    if connector:
        retention = connector.retention_days or GLOBAL_RETENTION_DAYS
        cutoff = now - timedelta(days=retention)
        result = db.execute(
            sa_update(ConnectorEvidence)
            .where(
                ConnectorEvidence.connector_id == connector.id,
                ConnectorEvidence.archived_at.is_(None),
                ConnectorEvidence.created_at < cutoff,
            )
            .values(archived_at=now)
        )
        db.commit()
        count = result.rowcount
        logger.info("Archived %d evidence items for connector %s (retention=%dd)", count, connector.name, retention)
        return count

    # Global sweep — group by connector to respect per-connector retention
    connectors = db.execute(select(Connector)).scalars().all()
    total = 0
    for c in connectors:
        retention = c.retention_days or GLOBAL_RETENTION_DAYS
        cutoff = now - timedelta(days=retention)
        result = db.execute(
            sa_update(ConnectorEvidence)
            .where(
                ConnectorEvidence.connector_id == c.id,
                ConnectorEvidence.archived_at.is_(None),
                ConnectorEvidence.created_at < cutoff,
            )
            .values(archived_at=now)
        )
        total += result.rowcount
    db.commit()
    logger.info("Global archive sweep complete: %d items archived", total)
    return total


def purge_archived_evidence(db: DBSession, connector: Connector | None = None) -> int:
    """Permanently delete archived evidence. Returns count deleted."""
    from sqlalchemy import delete as sa_delete
    stmt = sa_delete(ConnectorEvidence).where(ConnectorEvidence.archived_at.is_not(None))
    if connector:
        stmt = stmt.where(ConnectorEvidence.connector_id == connector.id)
    result = db.execute(stmt)
    db.commit()
    return result.rowcount


def get_archive_stats(db: DBSession) -> dict:
    """Return counts of active vs archived evidence per connector."""
    rows = db.execute(
        select(
            Connector.id,
            Connector.name,
            Connector.source_system,
            Connector.retention_days,
            func.count(ConnectorEvidence.id).filter(ConnectorEvidence.archived_at.is_(None)).label("active"),
            func.count(ConnectorEvidence.id).filter(ConnectorEvidence.archived_at.is_not(None)).label("archived"),
        )
        .outerjoin(ConnectorEvidence, ConnectorEvidence.connector_id == Connector.id)
        .group_by(Connector.id, Connector.name, Connector.source_system, Connector.retention_days)
    ).all()
    return [
        {
            "connector_id": str(r.id),
            "name": r.name,
            "source_system": r.source_system,
            "retention_days": r.retention_days or GLOBAL_RETENTION_DAYS,
            "active": r.active,
            "archived": r.archived,
        }
        for r in rows
    ]
