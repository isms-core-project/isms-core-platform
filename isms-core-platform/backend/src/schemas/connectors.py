"""Pydantic schemas for v2.0 connector evidence API."""

import uuid
from datetime import datetime

from pydantic import BaseModel, Field


# ── Connector registration ────────────────────────────────────────────────────

class ConnectorRegister(BaseModel):
    name: str = Field(..., description="Human-readable name, e.g. 'Entra ID — Contoso'")
    source_system: str = Field(
        ...,
        description=(
            "System identifier. "
            "Microsoft: entra_id | defender | sentinel | intune | o365 | purview. "
            "ITSM: servicenow | jira. "
            "Network: fortigate | panw | cisco_asa | cisco_ise | zscaler. "
            "EDR: crowdstrike | sentinelone. "
            "Vuln: tenable_sc | tenable_io | qualys | openvas. "
            "Identity: active_directory | openldap | freeipa | authentik | keycloak | cisco_ise. "
            "Monitoring: prtg | zabbix. "
            "Asset: glpi | netbox. "
            "PAM: cyberark. "
            "Cloud: aws_security_hub | azure_cspm | gcp_scc. "
            "Filigran: opencti | openaev. "
            "Generic: siem | threat_intel"
        ),
    )


class ConnectorRead(BaseModel):
    id: uuid.UUID
    name: str
    source_system: str
    status: str
    last_run: datetime | None = None
    last_item_count: int | None = None
    sync_requested_at: datetime | None = None
    last_error: str | None = None
    last_error_at: datetime | None = None
    evidence_count: int = 0
    retention_days: int | None = None
    created_at: datetime

    model_config = {"from_attributes": True}


class ConnectorRegistered(ConnectorRead):
    """Returned once on registration — includes the plain API token (not stored)."""
    api_token: str = Field(..., description="Bearer token for this connector. Store securely — shown once only.")


# ── Evidence ingestion ────────────────────────────────────────────────────────

class ConnectorEvidenceIngest(BaseModel):
    """Payload a connector POSTs for each evidence item."""
    group_code: str = Field(..., description="Control group code, e.g. 'a.8.8' or 'a.16.1'")
    source_ref: str | None = Field(None, description="Unique reference in source system, e.g. INC0012345")
    source_url: str | None = Field(None, description="Direct URL to the item in source system")
    title: str = Field(..., description="Short descriptive title")
    classification: str | None = Field(None, description="incident | change | asset | user | vulnerability | network | policy")
    status: str | None = Field(None, description="Status in source system, e.g. resolved, open, compliant")
    event_date: datetime | None = Field(None, description="When the event occurred or item was created")
    raw: dict | None = Field(None, description="Full raw payload from source system (stored for audit)")


class ConnectorEvidenceRead(BaseModel):
    id: uuid.UUID
    connector_id: uuid.UUID
    control_group_id: uuid.UUID
    group_code: str | None = None
    source_ref: str | None = None
    source_url: str | None = None
    title: str
    classification: str | None = None
    status: str | None = None
    event_date: datetime | None = None
    created_at: datetime
    archived_at: datetime | None = None
    raw: dict | None = None

    model_config = {"from_attributes": True}


class ConnectorEvidenceIngestResponse(BaseModel):
    accepted: int
    skipped: int  # duplicates (source_ref already exists for this connector)
    errors: int


# ── Connector config ──────────────────────────────────────────────────────────

class ConnectorConfigUpdate(BaseModel):
    """Admin sets the connector's credentials via PUT /{id}/config."""
    config: dict = Field(default_factory=dict, description="Key/value credential map (stored encrypted)")


class ConnectorConfigRead(BaseModel):
    """Returned to the connector on GET /me/config."""
    config: dict = Field(default_factory=dict)


class ConnectorSyncPending(BaseModel):
    """Returned to the connector on GET /me/sync-pending. Flag is cleared on read."""
    sync_requested: bool


class ConnectorRename(BaseModel):
    """Admin renames a connector's display name via PATCH /{id}/rename."""
    name: str = Field(..., min_length=1, max_length=120)


# ── Activity log ──────────────────────────────────────────────────────────────

class ConnectorLogEntry(BaseModel):
    """One audit_log entry scoped to a connector."""
    id: uuid.UUID
    event_type: str
    severity: str
    description: str | None = None
    created_at: datetime

    model_config = {"from_attributes": True}
