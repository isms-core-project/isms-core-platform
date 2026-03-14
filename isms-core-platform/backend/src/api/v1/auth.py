from fastapi import APIRouter, Depends, HTTPException, status
from jose import JWTError
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.schemas.auth import LoginRequest, RefreshRequest, TokenResponse
from src.schemas.users import (
    NOTIFICATION_EVENTS,
    NotificationPrefRead,
    NotificationPrefsResponse,
    NotificationPrefsPatch,
)
from src.services.auth_service import authenticate_user, create_token_pair, refresh_tokens

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
def login(body: LoginRequest, db: DBSession = Depends(get_db)):
    user = authenticate_user(db, body.email, body.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    return create_token_pair(user)


@router.post("/refresh", response_model=TokenResponse)
def refresh(body: RefreshRequest, db: DBSession = Depends(get_db)):
    try:
        result = refresh_tokens(db, body.refresh_token)
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid refresh token: {e}",
        )
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not refresh token",
        )
    return result


# ---------------------------------------------------------------------------
# Current-user notification preferences
# ---------------------------------------------------------------------------

@router.get("/me/notification-prefs", response_model=NotificationPrefsResponse)
def get_my_notification_prefs(current_user=Depends(get_current_user)):
    """Return the current user's notification preferences with enabled/disabled state."""
    stored = current_user.notification_prefs or {}
    prefs = [
        NotificationPrefRead(
            event_type=ev["event_type"],
            label=ev["label"],
            category=ev["category"],
            description=ev["description"],
            enabled=stored.get(ev["event_type"], True),
        )
        for ev in NOTIFICATION_EVENTS
    ]
    return NotificationPrefsResponse(prefs=prefs)


@router.patch("/me/notification-prefs", response_model=NotificationPrefsResponse)
def update_my_notification_prefs(
    body: NotificationPrefsPatch,
    current_user=Depends(get_current_user),
    db: DBSession = Depends(get_db),
):
    """Update the current user's notification preferences."""
    valid_types = {ev["event_type"] for ev in NOTIFICATION_EVENTS}
    unknown = set(body.prefs) - valid_types
    if unknown:
        raise HTTPException(
            status_code=422,
            detail=f"Unknown event type(s): {', '.join(sorted(unknown))}",
        )

    stored = dict(current_user.notification_prefs or {})
    stored.update(body.prefs)
    current_user.notification_prefs = stored
    db.add(current_user)
    db.commit()
    db.refresh(current_user)

    prefs = [
        NotificationPrefRead(
            event_type=ev["event_type"],
            label=ev["label"],
            category=ev["category"],
            description=ev["description"],
            enabled=stored.get(ev["event_type"], True),
        )
        for ev in NOTIFICATION_EVENTS
    ]
    return NotificationPrefsResponse(prefs=prefs)
