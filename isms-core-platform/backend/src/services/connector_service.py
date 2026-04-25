"""Service layer for v2.0 connector evidence ingestion."""

import hashlib
import logging
import secrets
from datetime import datetime, timedelta, timezone

from src.utils.encryption import decrypt_config, encrypt_config

from sqlalchemy import select, func, update as sa_update
from sqlalchemy.orm import Session as DBSession

from src.core.config import get_settings
from src.domain.connectors import Connector, ConnectorEvidence
from src.domain.control_groups import ControlGroup
from src.database.enums import ProductFamily
from src.schemas.connectors import ConnectorEvidenceIngest, ConnectorRegister

logger = logging.getLogger(__name__)


_ROUTED_SOURCES = {
    # Microsoft
    "entra_id", "o365", "defender", "sentinel", "intune", "purview",
    # EDR
    "crowdstrike", "sentinelone",
    # Vulnerability
    "tenable_sc", "tenable_io", "qualys", "openvas",
    # Network
    "fortigate", "panw", "cisco_asa", "cisco_ise", "zscaler",
    # Identity
    "active_directory", "openldap", "freeipa", "authentik", "keycloak",
    # Monitoring
    "prtg", "zabbix",
    # Asset
    "glpi", "netbox",
    # PAM
    "cyberark",
    # Cloud
    "aws_security_hub", "azure_cspm", "gcp_scc",
    # Filigran / TI
    "opencti", "openaev", "siem", "threat_intel",
}


def _promote_fields(source_system: str, raw: dict) -> dict:
    """Extract source-specific fields from raw payload into typed top-level fields.

    Best-effort: unknown keys are silently skipped. The promoted dict is merged
    into the OpenSearch document alongside the standard fields.
    """
    if not raw:
        return {}
    p: dict = {}

    if source_system == "entra_id":
        for src, dst in [
            ("userPrincipalName", "user_principal"),
            ("displayName",       "display_name"),
            ("department",        "department"),
            ("jobTitle",          "job_title"),
            ("accountEnabled",    "account_enabled"),
            ("isCompliant",       "is_compliant"),
            ("isManaged",         "is_managed"),
            ("deviceOwnership",   "device_ownership"),
            ("operatingSystem",   "os_name"),
            ("mail",              "email"),
        ]:
            if src in raw:
                p[dst] = raw[src]
        groups = raw.get("groupMemberships") or raw.get("memberOf") or []
        if groups:
            p["group_names"] = [g.get("displayName", g) if isinstance(g, dict) else g for g in groups]

    elif source_system == "o365":
        for src, dst in [
            ("Operation",      "operation"),
            ("Workload",       "workload"),
            ("ObjectId",       "object_id"),
            ("UserId",         "user_id"),
            ("UserType",       "user_type"),
            ("ExternalAccess", "external_access"),
            ("ClientIP",       "client_ip"),
            ("ResultStatus",   "result_status"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "defender":
        for src, dst in [
            ("severity",       "alert_severity"),
            ("status",         "alert_status"),
            ("machineId",      "machine_id"),
            ("osPlatform",     "os_platform"),
            ("relatedCveId",   "cve_id"),
            ("category",       "alert_category"),
            ("alertId",        "alert_id"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "sentinel":
        for src, dst in [
            ("severity",       "alert_severity"),
            ("status",         "incident_status"),
            ("incidentNumber", "incident_number"),
            ("title",          "incident_title"),
            ("tactics",        "tactics"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "intune":
        for src, dst in [
            ("complianceState",  "compliance_state"),
            ("deviceName",       "device_name"),
            ("osVersion",        "os_version"),
            ("managedDeviceId",  "device_id"),
            ("userPrincipalName","user_principal"),
            ("manufacturer",     "manufacturer"),
            ("model",            "model"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "crowdstrike":
        for src, dst in [
            ("Severity",        "alert_severity"),
            ("Status",          "alert_status"),
            ("ComputerName",    "machine_name"),
            ("Tactic",          "tactic"),
            ("Technique",       "technique"),
            ("EventType",       "event_type"),
            ("HostGroups",      "host_groups"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "sentinelone":
        for src, dst in [
            ("severity",        "alert_severity"),
            ("agentComputerName","machine_name"),
            ("classification",  "classification"),
            ("mitreTechnique",  "technique"),
            ("mitreTactic",     "tactic"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system in ("tenable_sc", "tenable_io"):
        for src, dst in [
            ("severity",        "severity"),
            ("cvssV3BaseScore", "cvss_score"),
            ("pluginName",      "plugin_name"),
            ("pluginId",        "plugin_id"),
            ("assetId",         "asset_id"),
            ("hostDnsName",     "fqdn"),
            ("cve",             "cve_id"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "qualys":
        for src, dst in [
            ("Severity",        "severity"),
            ("QdsScore",        "qds_score"),
            ("Title",           "plugin_name"),
            ("Qid",             "plugin_id"),
            ("Fqdn",            "fqdn"),
            ("Type",            "detection_type"),
            ("Cve",             "cve_id"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "openvas":
        for src, dst in [
            ("severity",        "severity"),
            ("nvt_name",        "plugin_name"),
            ("nvt_oid",         "plugin_id"),
            ("host",            "fqdn"),
            ("port",            "port"),
            ("threat",          "threat_level"),
            ("cve",             "cve_id"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "purview":
        for src, dst in [
            ("activityType",    "activity_type"),
            ("workload",        "workload"),
            ("userId",          "user_id"),
            ("objectName",      "object_name"),
            ("sensitivityLabel","sensitivity_label"),
            ("policyName",      "policy_name"),
            ("action",          "action"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "fortigate":
        for src, dst in [
            ("type",            "log_type"),
            ("subtype",         "log_subtype"),
            ("action",          "action"),
            ("srcip",           "src_ip"),
            ("dstip",           "dst_ip"),
            ("dstport",         "dst_port"),
            ("proto",           "protocol"),
            ("policyid",        "policy_id"),
            ("severity",        "severity"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "panw":
        for src, dst in [
            ("type",            "log_type"),
            ("subtype",         "log_subtype"),
            ("action",          "action"),
            ("src",             "src_ip"),
            ("dst",             "dst_ip"),
            ("dport",           "dst_port"),
            ("proto",           "protocol"),
            ("rule",            "policy_name"),
            ("severity",        "severity"),
            ("threat_name",     "threat_name"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system in ("cisco_asa", "cisco_ise"):
        for src, dst in [
            ("messageId",       "message_id"),
            ("severity",        "severity"),
            ("sourceAddress",   "src_ip"),
            ("destinationAddress","dst_ip"),
            ("destinationPort", "dst_port"),
            ("protocol",        "protocol"),
            ("userName",        "user_id"),
            ("action",          "action"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "zscaler":
        for src, dst in [
            ("action",          "action"),
            ("category",        "url_category"),
            ("url",             "url"),
            ("srcIp",           "src_ip"),
            ("user",            "user_id"),
            ("cloudName",       "cloud_name"),
            ("policyName",      "policy_name"),
            ("threatName",      "threat_name"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system in ("active_directory", "openldap", "freeipa", "authentik", "keycloak"):
        for src, dst in [
            ("sAMAccountName",  "username"),
            ("uid",             "username"),
            ("userPrincipalName","user_principal"),
            ("distinguishedName","distinguished_name"),
            ("department",      "department"),
            ("enabled",         "account_enabled"),
            ("accountExpires",  "account_expires"),
            ("memberOf",        "group_names"),
            ("lastLogon",       "last_logon"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "prtg":
        for src, dst in [
            ("sensor",          "sensor_name"),
            ("device",          "device_name"),
            ("group",           "group_name"),
            ("status",          "sensor_status"),
            ("message",         "message"),
            ("priority",        "priority"),
            ("lastvalue",       "last_value"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "zabbix":
        for src, dst in [
            ("host",            "host_name"),
            ("trigger",         "trigger_name"),
            ("severity",        "severity"),
            ("status",          "alert_status"),
            ("value",           "metric_value"),
            ("units",           "metric_units"),
            ("itemkey",         "item_key"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "glpi":
        for src, dst in [
            ("name",            "asset_name"),
            ("itemtype",        "asset_type"),
            ("serial",          "serial_number"),
            ("otherserial",     "asset_tag"),
            ("states_id",       "asset_status"),
            ("locations_id",    "location"),
            ("users_id_tech",   "assigned_tech"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "netbox":
        for src, dst in [
            ("display",         "asset_name"),
            ("device_type",     "asset_type"),
            ("serial",          "serial_number"),
            ("asset_tag",       "asset_tag"),
            ("status",          "asset_status"),
            ("site",            "site"),
            ("role",            "role"),
            ("primary_ip",      "primary_ip"),
        ]:
            if isinstance(raw.get(src), dict):
                p[dst] = raw[src].get("label") or raw[src].get("display") or str(raw[src])
            elif src in raw:
                p[dst] = raw[src]

    elif source_system == "cyberark":
        for src, dst in [
            ("AccountName",     "account_name"),
            ("Safe",            "safe_name"),
            ("UserName",        "username"),
            ("Address",         "address"),
            ("PlatformId",      "platform"),
            ("Action",          "action"),
            ("Reason",          "reason"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "aws_security_hub":
        for src, dst in [
            ("Severity.Label",  "severity"),
            ("Title",           "finding_title"),
            ("Type",            "finding_type"),
            ("ProductName",     "product_name"),
            ("AwsAccountId",    "aws_account_id"),
            ("Region",          "aws_region"),
            ("RecordState",     "record_state"),
            ("WorkflowStatus",  "workflow_status"),
        ]:
            # Support dotted keys
            parts = src.split(".")
            val = raw
            for part in parts:
                if isinstance(val, dict):
                    val = val.get(part)
                else:
                    val = None
                    break
            if val is not None:
                p[dst] = val

    elif source_system == "azure_cspm":
        for src, dst in [
            ("severity",        "severity"),
            ("displayName",     "finding_title"),
            ("resourceType",    "resource_type"),
            ("resourceName",    "resource_name"),
            ("subscriptionId",  "subscription_id"),
            ("status",          "compliance_status"),
            ("policyName",      "policy_name"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "gcp_scc":
        for src, dst in [
            ("severity",        "severity"),
            ("displayName",     "finding_title"),
            ("category",        "finding_type"),
            ("resourceName",    "resource_name"),
            ("projectId",       "gcp_project_id"),
            ("state",           "finding_state"),
            ("findingClass",    "finding_class"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "opencti":
        for src, dst in [
            ("type",            "indicator_type"),
            ("name",            "indicator_name"),
            ("confidence",      "confidence"),
            ("pattern",         "pattern"),
            ("labels",          "labels"),
            ("valid_from",      "valid_from"),
            ("valid_until",     "valid_until"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system == "openaev":
        for src, dst in [
            ("type",            "event_type"),
            ("severity",        "severity"),
            ("source",          "source"),
            ("indicator",       "indicator"),
            ("tlp",             "tlp"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    elif source_system in ("siem", "threat_intel"):
        for src, dst in [
            ("severity",        "severity"),
            ("category",        "category"),
            ("source",          "source"),
            ("indicator",       "indicator"),
            ("action",          "action"),
            ("host",            "host_name"),
            ("user",            "user_id"),
        ]:
            if src in raw:
                p[dst] = raw[src]

    return p


def _build_evidence_item(connector: Connector, item: ConnectorEvidenceIngest):
    """Map ConnectorEvidenceIngest → EvidenceItem for OpenSearch upsert."""
    from src.services.evidence_store.base import EvidenceItem

    src_sys = connector.source_system or ""
    routed = src_sys in _ROUTED_SOURCES
    # Shared indices: multiple source_systems → one index
    _INDEX_MAP = {
        "tenable_sc":     "tenable",
        "tenable_io":     "tenable",
        "cisco_asa":      "cisco",
        "cisco_ise":      "cisco",
        "active_directory":"identity",
        "openldap":       "identity",
        "freeipa":        "identity",
        "authentik":      "identity",
        "keycloak":       "identity",
        "opencti":        "threat-intel",
        "openaev":        "threat-intel",
        "siem":           "threat-intel",
        "threat_intel":   "threat-intel",
    }
    _index_name = _INDEX_MAP.get(src_sys, src_sys.replace("_", "-"))
    os_index = f"evidence-{_index_name}" if routed else ""
    promoted = _promote_fields(src_sys, item.raw or {}) if routed else {}

    return EvidenceItem(
        connector_id=str(connector.id),
        org_id=str(connector.organisation_id),
        resource_id=item.source_ref or "",
        evidence_type=item.classification or "general",
        title=item.title,
        summary=item.status or "",
        payload=item.raw or {},
        control_ids=[item.group_code],
        tags=[t for t in [item.status, item.classification] if t],
        collected_at=item.event_date,
        source_system=src_sys,
        os_index=os_index,
        promoted=promoted,
    )


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


def _index_connector_run(
    connector: Connector,
    started_at: datetime,
    evidence_count: int,
    errors: int,
) -> None:
    """Write a connector run record to the OpenSearch connector-runs alias (non-fatal)."""
    try:
        from opensearchpy import OpenSearch
        s = get_settings()
        client = OpenSearch(hosts=[s.opensearch_url], use_ssl=False, verify_certs=False)
        finished_at = datetime.now(timezone.utc)
        doc = {
            "started_at":      started_at.isoformat(),
            "finished_at":     finished_at.isoformat(),
            "connector_name":  connector.name,
            "connector_id":    str(connector.id),
            "org_id":          connector.organisation_id,
            "status":          "error" if errors and not evidence_count else "success",
            "evidence_count":  evidence_count,
            "error_message":   f"{errors} item(s) failed" if errors else "",
        }
        client.index(index="connector-runs", body=doc)
    except Exception as exc:
        logger.debug("OpenSearch connector-runs index failed (non-fatal): %s", exc)


def ingest_evidence(
    db: DBSession,
    connector: Connector,
    items: list[ConnectorEvidenceIngest],
) -> dict:
    """Bulk-ingest evidence items from a connector. Returns accepted/skipped/errors counts."""
    accepted = skipped = errors = 0
    started_at = datetime.now(timezone.utc)

    # Lazy-init OpenSearch store once per call (v2 only)
    os_store = None
    if get_settings().evidence_store == "opensearch":
        try:
            from src.services.evidence_store import get_evidence_store
            os_store = get_evidence_store()
        except Exception as exc:
            logger.warning("OpenSearch store init failed (falling back to postgres-only): %s", exc)

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

            # OpenSearch upsert (v2) — non-fatal
            if os_store and item.source_ref:
                try:
                    os_store.upsert(_build_evidence_item(connector, item))
                except Exception as os_exc:
                    logger.warning("OpenSearch upsert failed (non-fatal): %s", os_exc)

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

    # Write connector run record to OpenSearch (non-fatal)
    if os_store:
        _index_connector_run(connector, started_at, accepted, errors)

    return {"accepted": accepted, "skipped": skipped, "errors": errors}


def report_error(db: DBSession, connector: Connector, message: str) -> None:
    """Record that a connector sync failed with an error message."""
    prev_error_at = connector.last_error_at
    now = datetime.now(timezone.utc)
    connector.last_error = message[:2000]  # cap at 2000 chars
    connector.last_error_at = now
    db.commit()
    logger.warning("Connector %s reported error: %s", connector.name, message[:200])

    if get_settings().evidence_store == "opensearch":
        _index_connector_run(connector, now, 0, 1)

    # Notify only on first error or if 24 h have passed since last notification
    is_first = prev_error_at is None
    is_repeat = not is_first and (now - prev_error_at).total_seconds() >= 86400
    if is_first or is_repeat:
        try:
            from src.services.notification_service import notify_connector_failure
            notify_connector_failure.delay(
                connector_id=str(connector.id),
                connector_name=connector.name,
                error_message=message,
            )
        except Exception as exc:
            logger.warning("Could not queue connector failure notification: %s", exc)


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
