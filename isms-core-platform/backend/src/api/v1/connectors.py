"""v2.0 Connector evidence ingestion endpoints.

Connector management (admin-only JWT):
  POST   /api/v1/connectors/register          — register a new connector, returns one-time API token
  GET    /api/v1/connectors/                  — list all connectors + sync status
  DELETE /api/v1/connectors/{id}              — deregister
  PUT    /api/v1/connectors/{id}/config       — store encrypted credentials (GUI config)
  DELETE /api/v1/connectors/{id}/evidence     — delete all evidence for a connector

Connector self-service (connector bearer token):
  GET    /api/v1/connectors/me/config         — fetch own decrypted credentials
  POST   /api/v1/connectors/ingest            — POST a batch of evidence items
  POST   /api/v1/connectors/me/report-error   — record a sync failure message

Evidence retrieval (user JWT):
  GET    /api/v1/connectors/evidence/         — list all automated evidence (cross-group)
  GET    /api/v1/connectors/evidence/{group_code}   — list automated evidence for a control group
  DELETE /api/v1/connectors/evidence/item/{id}      — delete a single evidence item
"""

import csv
import io
import json
import os
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import StreamingResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, require_admin
from src.database.session import get_db
from src.domain.connectors import Connector
from src.domain.users import User
from src.schemas.connectors import (
    ConnectorConfigRead,
    ConnectorConfigUpdate,
    ConnectorEvidenceIngest,
    ConnectorEvidenceIngestResponse,
    ConnectorEvidenceRead,
    ConnectorLogEntry,
    ConnectorRead,
    ConnectorRegister,
    ConnectorRegistered,
    ConnectorRename,
    ConnectorSyncPending,
)
from src.services import connector_service
from src.services.audit_service import CAT_SYSTEM, SEV_ERROR, SEV_INFO, SEV_WARNING, log_event
from src.services.control_service import get_control_group_by_code
from src.utils.encryption import decrypt_config

router = APIRouter(prefix="/connectors", tags=["connectors"])

_connector_bearer = HTTPBearer(auto_error=False)


def _worker_secret() -> str:
    return os.environ.get("CONNECTORS_WORKER_SECRET", "")


def _get_connector(
    request: Request,
    credentials: HTTPAuthorizationCredentials | None = Depends(_connector_bearer),
    db: DBSession = Depends(get_db),
) -> Connector:
    """Validate connector auth. Accepts:
      - Worker mode:     Authorization: Bearer <worker_secret>  +  X-Connector-ID: <uuid>
      - Standalone mode: Authorization: Bearer <per-connector-token>
    """
    if not credentials:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Connector token required")

    token = credentials.credentials
    ws = _worker_secret()

    # Worker auth: shared secret + connector ID header
    if ws and token == ws:
        cid_header = request.headers.get("X-Connector-ID")
        if not cid_header:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="X-Connector-ID header required in worker mode")
        try:
            connector = db.get(Connector, uuid.UUID(cid_header))
        except ValueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid connector ID")
        if not connector:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Connector not found")
        return connector

    # Standalone auth: per-connector token
    connector = connector_service.get_connector_by_token(db, token)
    if not connector:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or inactive connector token")
    return connector


# ── Management (admin JWT) ────────────────────────────────────────────────────

@router.post("/register", response_model=ConnectorRegistered, status_code=201)
def register_connector(
    payload: ConnectorRegister,
    db: DBSession = Depends(get_db),
    _: User = Depends(require_admin),
):
    """Register a new connector. Returns a one-time API token — store it securely."""
    connector, plain_token = connector_service.register_connector(db, payload)
    return ConnectorRegistered(
        **ConnectorRead.model_validate(connector).model_dump(),
        api_token=plain_token,
    )


@router.get("/", response_model=list[ConnectorRead])
def list_connectors(
    db: DBSession = Depends(get_db),
    _: User = Depends(require_admin),
):
    return connector_service.list_connectors(db)


@router.get("/worker/all")
def list_all_for_worker(
    request: Request,
    db: DBSession = Depends(get_db),
):
    """Called by the connectors runner to discover all registered connectors + configs.
    Authenticated via CONNECTORS_WORKER_SECRET only (not JWT).
    Returns connector list with decrypted credentials — never expose to end users.
    """
    ws = _worker_secret()
    if not ws:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Worker mode not configured (CONNECTORS_WORKER_SECRET not set)")
    token = request.headers.get("Authorization", "").removeprefix("Bearer ").strip()
    if token != ws:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid worker secret")

    connectors = connector_service.list_connectors(db)
    result = []
    for c in connectors:
        raw = db.get(Connector, c["id"])
        config = {}
        if raw and raw.config_encrypted:
            try:
                config = decrypt_config(raw.config_encrypted)
            except Exception:
                pass
        result.append({
            "id": str(c["id"]),
            "name": c["name"],
            "source_system": c["source_system"],
            "status": c["status"],
            "config": config,
        })
    return result


@router.delete("/{connector_id}", status_code=204)
def deregister_connector(
    connector_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _: User = Depends(require_admin),
):
    connector = connector_service.get_connector_by_id(db, connector_id)
    if not connector:
        raise HTTPException(status_code=404, detail="Connector not found")
    connector_service.deregister_connector(db, connector)


# ── Connector config (admin JWT writes, connector token reads) ────────────────

@router.get("/me/config", response_model=ConnectorConfigRead)
def get_my_config(
    connector: Connector = Depends(_get_connector),
    db: DBSession = Depends(get_db),
):
    """Called by a connector to fetch its own decrypted credentials.
    The connector POSTs its bearer token; we return the stored config dict.
    Returns {} if no config has been stored yet (connector falls back to env vars).
    """
    return ConnectorConfigRead(config=connector_service.get_connector_config(db, connector))


@router.get("/me/sync-pending", response_model=ConnectorSyncPending)
def get_sync_pending(
    connector: Connector = Depends(_get_connector),
    db: DBSession = Depends(get_db),
):
    """Called by the connector every 30s during its sleep cycle.
    Returns sync_requested=True if an admin triggered a manual sync.
    The flag is cleared atomically on read — connector will not loop.
    """
    pending = connector_service.pop_sync_requested(db, connector)
    return ConnectorSyncPending(sync_requested=pending)


@router.post("/{connector_id}/sync", status_code=202)
def trigger_sync(
    connector_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _: User = Depends(require_admin),
):
    """Request an immediate sync for a connector. The connector wakes up within ~30s."""
    connector = connector_service.get_connector_by_id(db, connector_id)
    if not connector:
        raise HTTPException(status_code=404, detail="Connector not found")
    connector_service.request_sync(db, connector)
    log_event(
        db,
        event_type="connector.sync.requested",
        category=CAT_SYSTEM,
        severity=SEV_INFO,
        description=f"Manual sync requested for connector '{connector.name}'",
        metadata={"connector_id": str(connector_id), "connector_name": connector.name},
    )
    db.commit()
    return {"detail": "Sync requested — connector will run within 30s"}


@router.put("/{connector_id}/config", status_code=204)
def update_connector_config(
    connector_id: uuid.UUID,
    payload: ConnectorConfigUpdate,
    db: DBSession = Depends(get_db),
    _: User = Depends(require_admin),
):
    """Admin stores (or replaces) encrypted credentials for a connector.
    Connector must be restarted / next poll cycle to pick up new config.
    """
    connector = connector_service.get_connector_by_id(db, connector_id)
    if not connector:
        raise HTTPException(status_code=404, detail="Connector not found")
    connector_service.store_config(db, connector, payload.config)


@router.patch("/{connector_id}/rename", status_code=204)
def rename_connector(
    connector_id: uuid.UUID,
    payload: ConnectorRename,
    db: DBSession = Depends(get_db),
    _: User = Depends(require_admin),
):
    """Admin renames a connector's display name."""
    connector = connector_service.get_connector_by_id(db, connector_id)
    if not connector:
        raise HTTPException(status_code=404, detail="Connector not found")
    connector_service.rename_connector(db, connector, payload.name)


# ── Evidence ingestion (connector token) ─────────────────────────────────────

@router.post("/ingest", response_model=ConnectorEvidenceIngestResponse, status_code=202)
def ingest_evidence(
    items: list[ConnectorEvidenceIngest],
    db: DBSession = Depends(get_db),
    connector: Connector = Depends(_get_connector),
):
    """Connector POSTs a batch of evidence items. Duplicates (same source_ref) are silently skipped."""
    if not items:
        return ConnectorEvidenceIngestResponse(accepted=0, skipped=0, errors=0)
    result = connector_service.ingest_evidence(db, connector, items)
    if result.get("accepted", 0) > 0 or result.get("errors", 0) > 0:
        severity = SEV_WARNING if result.get("errors", 0) > 0 else SEV_INFO
        log_event(
            db,
            event_type="connector.evidence.ingested",
            category=CAT_SYSTEM,
            severity=severity,
            description=(
                f"Connector '{connector.name}' sync: "
                f"{result.get('accepted', 0)} accepted, "
                f"{result.get('skipped', 0)} skipped, "
                f"{result.get('errors', 0)} errors"
            ),
            metadata={"connector_id": str(connector.id), "connector_name": connector.name, **result},
        )
        db.commit()
    return ConnectorEvidenceIngestResponse(**result)


@router.post("/me/report-error", status_code=204)
def report_error(
    payload: dict,
    db: DBSession = Depends(get_db),
    connector: Connector = Depends(_get_connector),
):
    """Connector reports a sync failure. Stores the error message against the connector record."""
    message = str(payload.get("error", "Unknown error"))
    connector_service.report_error(db, connector, message)
    log_event(
        db,
        event_type="connector.sync.error",
        category=CAT_SYSTEM,
        severity=SEV_ERROR,
        description=f"Connector '{connector.name}' reported sync error: {message[:200]}",
        metadata={"connector_id": str(connector.id), "connector_name": connector.name, "error": message},
    )
    db.commit()


# ── Evidence retrieval (user JWT) ─────────────────────────────────────────────

@router.get("/evidence/", response_model=list[ConnectorEvidenceRead])
def get_all_evidence(
    limit: int = 200,
    product: str | None = None,
    include_archived: bool = False,
    db: DBSession = Depends(get_db),
    _: User = Depends(get_current_user),
):
    """List all automated evidence across all control groups, most recent first."""
    return connector_service.list_all_evidence(db, limit=limit, product_family=product, include_archived=include_archived)


@router.get("/evidence/export")
def export_all_evidence(
    product: str | None = None,
    include_archived: bool = False,
    db: DBSession = Depends(get_db),
    _: User = Depends(get_current_user),
):
    """Export all automated evidence as CSV (respects product and archived filters)."""
    items = connector_service.list_all_evidence(db, limit=10000, product_family=product, include_archived=include_archived)
    cols = ["id", "group_code", "title", "source_ref", "classification", "status", "event_date", "created_at"]
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=cols, extrasaction="ignore")
    w.writeheader()
    for item in items:
        row = {k: item.get(k, "") for k in cols}
        if row["event_date"] and hasattr(row["event_date"], "isoformat"):
            row["event_date"] = row["event_date"].isoformat()
        if row["created_at"] and hasattr(row["created_at"], "isoformat"):
            row["created_at"] = row["created_at"].isoformat()
        row["id"] = str(row["id"]) if row["id"] else ""
        w.writerow(row)
    buf.seek(0)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"automated_evidence_{product or 'all'}_{ts}.csv"
    return StreamingResponse(
        iter([buf.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@router.delete("/evidence/item/{evidence_id}", status_code=204)
def delete_evidence_item(
    evidence_id: str,
    db: DBSession = Depends(get_db),
    _: User = Depends(require_admin),
):
    """Delete a single evidence item (admin only)."""
    found = connector_service.delete_evidence_item(db, evidence_id)
    if not found:
        raise HTTPException(status_code=404, detail="Evidence item not found")


@router.get("/evidence/{group_code}", response_model=list[ConnectorEvidenceRead])
def get_evidence_for_group(
    group_code: str,
    limit: int = 100,
    db: DBSession = Depends(get_db),
    _: User = Depends(get_current_user),
):
    """List automated evidence items ingested for a control group."""
    group = get_control_group_by_code(db, group_code)
    if not group:
        raise HTTPException(status_code=404, detail=f"Control group '{group_code}' not found")
    return connector_service.list_evidence_for_group(db, group.id, limit=limit)


@router.delete("/{connector_id}/evidence", status_code=200)
def delete_connector_evidence(
    connector_id: str,
    db: DBSession = Depends(get_db),
    _: User = Depends(require_admin),
):
    """Delete all evidence items for a connector (admin only). Used when wrong tenant connected."""
    connector = connector_service.get_connector_by_id(db, connector_id)
    if not connector:
        raise HTTPException(status_code=404, detail="Connector not found")
    count = connector_service.delete_connector_evidence(db, connector)
    return {"deleted": count}


# ── Archiving ─────────────────────────────────────────────────────────────────

@router.get("/archive/stats")
def get_archive_stats(
    db: DBSession = Depends(get_db),
    _: User = Depends(require_admin),
):
    """Return active vs archived evidence counts per connector."""
    return connector_service.get_archive_stats(db)


@router.post("/archive/run", status_code=200)
def run_archive(
    connector_id: str | None = None,
    db: DBSession = Depends(get_db),
    _: User = Depends(require_admin),
):
    """Soft-archive evidence older than the retention period. Optionally scoped to one connector."""
    connector = None
    if connector_id:
        connector = connector_service.get_connector_by_id(db, connector_id)
        if not connector:
            raise HTTPException(status_code=404, detail="Connector not found")
    count = connector_service.archive_old_evidence(db, connector)
    scope = connector.name if connector else "all connectors"
    log_event(
        db,
        event_type="connector.evidence.archived",
        category=CAT_SYSTEM,
        severity=SEV_INFO,
        description=f"Manual archive sweep ({scope}): {count} record(s) archived",
        metadata={"archived_count": count, "scope": scope},
    )
    db.commit()
    return {"archived": count}


@router.post("/archive/purge", status_code=200)
def purge_archived(
    connector_id: str | None = None,
    db: DBSession = Depends(get_db),
    _: User = Depends(require_admin),
):
    """Permanently delete all archived evidence. Optionally scoped to one connector."""
    connector = None
    if connector_id:
        connector = connector_service.get_connector_by_id(db, connector_id)
        if not connector:
            raise HTTPException(status_code=404, detail="Connector not found")
    count = connector_service.purge_archived_evidence(db, connector)
    scope = connector.name if connector else "all connectors"
    log_event(
        db,
        event_type="connector.evidence.purged",
        category=CAT_SYSTEM,
        severity=SEV_WARNING,
        description=f"Permanent purge ({scope}): {count} archived record(s) deleted",
        metadata={"purged_count": count, "scope": scope},
    )
    db.commit()
    return {"purged": count}


@router.patch("/{connector_id}/retention", status_code=204)
def set_retention(
    connector_id: uuid.UUID,
    payload: dict,
    db: DBSession = Depends(get_db),
    _: User = Depends(require_admin),
):
    """Set per-connector retention days. Pass null to revert to global default (90d)."""
    connector = connector_service.get_connector_by_id(db, connector_id)
    if not connector:
        raise HTTPException(status_code=404, detail="Connector not found")
    days = payload.get("retention_days")
    connector_service.set_retention_days(db, connector, int(days) if days else None)


@router.get("/{connector_id}/log", response_model=list[ConnectorLogEntry])
def get_connector_log(
    connector_id: uuid.UUID,
    limit: int = 50,
    db: DBSession = Depends(get_db),
    _: User = Depends(require_admin),
):
    """Return recent audit_log entries for a connector, newest first."""
    from sqlalchemy import cast, String, desc
    from src.domain.system import AuditLog
    connector = connector_service.get_connector_by_id(db, connector_id)
    if not connector:
        raise HTTPException(status_code=404, detail="Connector not found")
    rows = (
        db.query(AuditLog)
        .filter(AuditLog.metadata_["connector_id"].as_string() == str(connector_id))
        .order_by(desc(AuditLog.created_at))
        .limit(min(limit, 200))
        .all()
    )
    return rows
