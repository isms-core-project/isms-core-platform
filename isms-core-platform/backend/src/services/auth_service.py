from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    verify_password,
)
from src.domain.users import User


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
        extra_claims={"role": user.role.value, "email": user.email},
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
