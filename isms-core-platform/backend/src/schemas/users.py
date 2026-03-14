import uuid
from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    full_name: str | None = None
    password: str
    role: str = "viewer"              # admin | isms_manager | auditor | control_owner | viewer


class UserPatch(BaseModel):
    full_name: str | None = None
    role: str | None = None
    is_active: bool | None = None
    password: str | None = None
    notification_prefs: dict | None = None


class UserRead(BaseModel):
    id: uuid.UUID
    email: str
    username: str
    full_name: str | None
    role: str
    is_active: bool
    last_login: datetime | None
    created_at: datetime
    notification_prefs: dict = {}

    model_config = {"from_attributes": True}


# ---------------------------------------------------------------------------
# Notification preferences
# ---------------------------------------------------------------------------

# All toggleable event types with display metadata.
# Missing key in user.notification_prefs means enabled (True is default).
NOTIFICATION_EVENTS: list[dict] = [
    {
        "event_type": "email.gap_assigned",
        "label": "Gap assigned to me",
        "category": "workflow",
        "description": "Receive an email when a gap is assigned to you.",
    },
    {
        "event_type": "email.evidence_expiry",
        "label": "Evidence expiry alerts",
        "category": "workflow",
        "description": "Receive warnings when evidence items are approaching or past expiry.",
    },
    {
        "event_type": "email.qa_fail",
        "label": "QA check failures",
        "category": "system",
        "description": "Receive a summary email when a QA existence check finds failures.",
    },
    {
        "event_type": "email.import_completed",
        "label": "Import completed",
        "category": "system",
        "description": "Receive a summary email when a data import finishes.",
    },
]


class NotificationPrefRead(BaseModel):
    event_type: str
    label: str
    category: str
    description: str
    enabled: bool


class NotificationPrefsResponse(BaseModel):
    prefs: list[NotificationPrefRead]


class NotificationPrefsPatch(BaseModel):
    # Map of event_type → enabled
    prefs: dict[str, bool]
