import uuid
from datetime import datetime, timedelta, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.config import get_settings
from src.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    verify_password,
)
from src.domain.users import Session as UserSession, User


def authenticate_user(db: DBSession, email: str, password: str) -> User | None:
    """Verify credentials. Returns User or None."""
    user = db.execute(
        select(User).where(User.email == email)
    ).scalar_one_or_none()

    if not user or not user.is_active:
        return None
    if not verify_password(password, user.hashed_password):
        return None

    user.last_login = datetime.now(timezone.utc)
    db.commit()
    return user


def create_token_pair(user: User) -> dict:
    """Create access + refresh tokens for a user."""
    access = create_access_token(
        subject=str(user.id),
        extra_claims={
            "role": user.role.value,
            "email": user.email,
            "org_id": str(user.organisation_id),
        },
    )
    refresh = create_refresh_token(subject=str(user.id))
    return {
        "access_token": access,
        "refresh_token": refresh,
        "token_type": "bearer",
    }


def refresh_tokens(db: DBSession, refresh_token: str) -> dict | None:
    """Validate refresh token and issue a new pair. Returns None on failure."""
    payload = decode_token(refresh_token)
    if payload.get("type") != "refresh":
        return None

    user_id = payload.get("sub")
    if not user_id:
        return None

    user = db.get(User, user_id)
    if not user or not user.is_active:
        return None

    return create_token_pair(user)


def create_session(
    db: DBSession,
    user: User,
    refresh_token: str,
    ip_address: str | None = None,
    user_agent: str | None = None,
) -> None:
    """Write a Session row for the given refresh token."""
    settings = get_settings()
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=settings.refresh_token_expire_minutes)
    session = UserSession(
        id=uuid.uuid4(),
        user_id=user.id,
        token=refresh_token,
        expires_at=expires_at,
        ip_address=ip_address,
        user_agent=user_agent[:500] if user_agent else None,
    )
    db.add(session)


def delete_session_by_token(db: DBSession, refresh_token: str) -> None:
    """Remove session row matching the given refresh token (best-effort)."""
    try:
        s = db.execute(
            select(UserSession).where(UserSession.token == refresh_token)
        ).scalar_one_or_none()
        if s:
            db.delete(s)
    except Exception:
        pass
