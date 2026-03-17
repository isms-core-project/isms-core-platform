import uuid
from datetime import datetime

from pydantic import BaseModel


class SystemStatus(BaseModel):
    frameworks: int
    framework_controls: int
    cross_framework_mappings: int
    control_groups: int
    policies: int
    requirements: int
    implementations: int
    assessments: int
    evidence: int
    automated_evidence: int
    gaps: int
    users: int
    load_history_count: int


class ServiceHealth(BaseModel):
    name: str
    status: str  # "ok" | "error" | "unavailable"
    latency_ms: int | None = None
    detail: str | None = None


class SysInfoResponse(BaseModel):
    generated_at: datetime
    services: list[ServiceHealth]
    db_counts: SystemStatus
    opensearch_cluster_status: str | None = None
    opensearch_indices: dict | None = None
    platform: str
    standard: str
    api_version: str
    framework_path: str
    operational_path: str
    privacy_path: str = ""
    cloud_path: str = ""
    opensearch_url: str
    last_sync_at: datetime | None = None
    last_sync_type: str | None = None
    last_sync_status: str | None = None
    external_path: str = ""
    datasets_path: str = ""
    log_level: str = "INFO"
    debug: bool = False
    smtp_enabled: bool = False
    smtp_host: str = ""
    smtp_port: int = 1025
    smtp_from: str = ""
    platform_url: str = ""
    ai_model: str = ""


class LoadHistoryRead(BaseModel):
    id: uuid.UUID
    bundle_type: str
    bundle_file: str | None = None
    framework_code: str | None = None
    objects_loaded: int | None = 0
    relationships_loaded: int | None = 0
    load_status: str
    load_started: datetime | None = None
    load_completed: datetime | None = None
    error_message: str | None = None

    model_config = {"from_attributes": True}


class AuditLogRead(BaseModel):
    id: uuid.UUID
    event_type: str
    category: str
    severity: str
    user_id: uuid.UUID | None = None
    actor_email: str | None = None
    target_type: str | None = None
    target_id: uuid.UUID | None = None
    description: str | None = None
    ip_address: str | None = None
    metadata_: dict = {}
    created_at: datetime

    model_config = {"from_attributes": True}


class AuditLogPage(BaseModel):
    items: list[AuditLogRead]
    total: int
    page: int
    page_size: int
    pages: int
