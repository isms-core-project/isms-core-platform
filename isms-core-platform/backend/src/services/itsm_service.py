"""ITSM service — push gaps/remediation to Jira or ServiceNow."""

import logging
import uuid
from datetime import datetime, timezone
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.domain.compliance import Gap
from src.domain.connectors import Connector
from src.domain.itsm import ItsmTicket
from src.domain.risks import RemediationAction
from src.utils.encryption import decrypt_config

logger = logging.getLogger(__name__)

ITSM_SOURCE_SYSTEMS = {"jira", "servicenow"}


def _get_connector(db: DBSession, connector_id: uuid.UUID, org_id: uuid.UUID) -> Connector:
    c = db.get(Connector, connector_id)
    if not c or c.organisation_id != org_id:
        raise ValueError("Connector not found")
    if c.source_system not in ITSM_SOURCE_SYSTEMS:
        raise ValueError(f"Connector is not an ITSM type (got '{c.source_system}')")
    if not c.config_encrypted:
        raise ValueError("Connector has no credentials configured")
    return c


def _existing_ticket(db: DBSession, source_type: str, source_id: uuid.UUID, connector_id: uuid.UUID) -> ItsmTicket | None:
    return db.execute(
        select(ItsmTicket).where(
            ItsmTicket.source_type == source_type,
            ItsmTicket.source_id == source_id,
            ItsmTicket.connector_id == connector_id,
        )
    ).scalar_one_or_none()


def _create_external_ticket(connector: Connector, summary: str, description: str) -> dict[str, Any]:
    config = decrypt_config(connector.config_encrypted)
    if connector.source_system == "jira":
        from src.integrations.jira_client import from_connector_config
        client = from_connector_config(config)
        return client.create_issue(summary=summary, description=description)
    else:  # servicenow
        from src.integrations.servicenow_client import from_connector_config
        client = from_connector_config(config)
        return client.create_task(short_description=summary, description=description)


def push_gap(
    db: DBSession,
    gap_id: uuid.UUID,
    connector_id: uuid.UUID,
    org_id: uuid.UUID,
) -> dict[str, Any]:
    """Push a gap to ITSM. Returns ticket info. Idempotent — returns existing ticket if already pushed."""
    existing = _existing_ticket(db, "gap", gap_id, connector_id)
    if existing:
        return {"ticket_id": existing.external_ticket_id, "url": existing.external_url, "status": existing.status, "already_exists": True}

    gap = db.get(Gap, gap_id)
    if not gap:
        raise ValueError("Gap not found")

    connector = _get_connector(db, connector_id, org_id)
    summary = f"[ISMS Gap] {gap.title or str(gap_id)}"
    description = gap.description or f"Gap ID: {gap_id}"

    result = _create_external_ticket(connector, summary, description)

    ticket = ItsmTicket(
        org_id=org_id,
        source_type="gap",
        source_id=gap_id,
        connector_id=connector_id,
        external_ticket_id=result["key"],
        external_url=result.get("url"),
        status="open",
        last_synced_at=datetime.now(timezone.utc),
    )
    db.add(ticket)
    db.commit()
    return {"ticket_id": result["key"], "url": result.get("url"), "status": "open", "already_exists": False}


def push_remediation(
    db: DBSession,
    action_id: uuid.UUID,
    connector_id: uuid.UUID,
    org_id: uuid.UUID,
) -> dict[str, Any]:
    """Push a remediation action to ITSM."""
    existing = _existing_ticket(db, "remediation", action_id, connector_id)
    if existing:
        return {"ticket_id": existing.external_ticket_id, "url": existing.external_url, "status": existing.status, "already_exists": True}

    action = db.get(RemediationAction, action_id)
    if not action or action.org_id != org_id:
        raise ValueError("Remediation action not found")

    connector = _get_connector(db, connector_id, org_id)
    summary = f"[ISMS Remediation] {action.title}"
    description = action.description or f"Remediation action ID: {action_id}"
    if action.eta:
        description += f"\nTarget date: {action.eta}"

    result = _create_external_ticket(connector, summary, description)

    ticket = ItsmTicket(
        org_id=org_id,
        source_type="remediation",
        source_id=action_id,
        connector_id=connector_id,
        external_ticket_id=result["key"],
        external_url=result.get("url"),
        status="open",
        last_synced_at=datetime.now(timezone.utc),
    )
    db.add(ticket)
    db.commit()
    return {"ticket_id": result["key"], "url": result.get("url"), "status": "open", "already_exists": False}


def sync_ticket(db: DBSession, ticket_id: uuid.UUID, org_id: uuid.UUID) -> dict[str, Any]:
    """Refresh status from ITSM system."""
    ticket = db.get(ItsmTicket, ticket_id)
    if not ticket or ticket.org_id != org_id:
        raise ValueError("Ticket not found")

    connector = _get_connector(db, ticket.connector_id, org_id)
    config = decrypt_config(connector.config_encrypted)

    if connector.source_system == "jira":
        from src.integrations.jira_client import from_connector_config
        status = from_connector_config(config).get_issue_status(ticket.external_ticket_id)
    else:
        from src.integrations.servicenow_client import from_connector_config
        status = from_connector_config(config).get_task_status(ticket.external_ticket_id)

    ticket.status = status
    ticket.last_synced_at = datetime.now(timezone.utc)
    db.commit()
    return {"ticket_id": ticket.external_ticket_id, "url": ticket.external_url, "status": status}


def list_tickets_for_source(
    db: DBSession,
    source_type: str,
    source_id: uuid.UUID,
    org_id: uuid.UUID,
) -> list[dict[str, Any]]:
    rows = db.execute(
        select(ItsmTicket).where(
            ItsmTicket.org_id == org_id,
            ItsmTicket.source_type == source_type,
            ItsmTicket.source_id == source_id,
        ).order_by(ItsmTicket.created_at.desc())
    ).scalars().all()
    return [{"id": str(t.id), "ticket_id": t.external_ticket_id, "url": t.external_url, "status": t.status, "connector_id": str(t.connector_id), "created_at": t.created_at.isoformat()} for t in rows]
