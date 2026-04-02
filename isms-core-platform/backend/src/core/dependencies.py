"""FastAPI dependencies: database session, current user, role guards, org context."""

import uuid

from fastapi import Depends, Header, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError
from sqlalchemy.orm import Session as DBSession

from src.core.security import decode_token
from src.database.enums import GovernanceMode, UserRole
from src.database.session import get_db
from src.domain.users import User

bearer_scheme = HTTPBearer()

# Roles that may write ISMS content (policies, generators, assessments)
_CONTENT_WRITE_ROLES = (UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.ISMS_MANAGER)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: DBSession = Depends(get_db),
) -> User:
    """Extract and validate the JWT, return the User or raise 401."""
    token = credentials.credentials
    try:
        payload = decode_token(token)
        if payload.get("type") != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type",
            )
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    user = db.get(User, uuid.UUID(user_id))
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or inactive",
        )
    return user


def get_org_context(
    x_org_id: str | None = Header(None, alias="X-Org-ID"),
    current_user: User = Depends(get_current_user),
) -> uuid.UUID:
    """Resolve the active organisation UUID for the current request.

    Regular users: always their own organisation_id.
    SUPER_ADMIN: may pass X-Org-ID header to act in any org's context.
    """
    if current_user.role == UserRole.SUPER_ADMIN and x_org_id:
        try:
            return uuid.UUID(x_org_id)
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="X-Org-ID must be a valid UUID",
            )
    return current_user.organisation_id


def require_role(*roles: UserRole):
    """Return a dependency that checks the current user has one of the given roles."""

    def checker(user: User = Depends(get_current_user)) -> User:
        if user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Role {user.role.value} not permitted; need one of {[r.value for r in roles]}",
            )
        return user

    return checker


# Shorthand — admin gate (SUPER_ADMIN also qualifies)
require_admin = require_role(UserRole.SUPER_ADMIN, UserRole.ADMIN)

# Shorthand — QA/content gate (SUPER_ADMIN + ADMIN + ISMS_MANAGER)
require_qa_access = require_role(UserRole.SUPER_ADMIN, UserRole.ADMIN, UserRole.ISMS_MANAGER)


def require_content_editable(
    db: DBSession = Depends(get_db),
    user: User = Depends(get_current_user),
) -> User:
    """Allow writes only when:
      1. governance_mode == 'platform'  (DB is the content authority)
      2. user has SUPER_ADMIN, ADMIN, or ISMS_MANAGER role

    In 'local' governance mode the platform is a read-only view of files;
    content changes must go through the file import pipeline instead.
    """
    from src.domain.organisations import Organisation  # avoid circular at module level

    org = db.get(Organisation, user.organisation_id)
    if org and org.governance_mode == GovernanceMode.LOCAL:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=(
                "Content editing is disabled: governance_mode is 'local'. "
                "Use the file import pipeline to update content."
            ),
        )
    if user.role not in _CONTENT_WRITE_ROLES:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Role '{user.role.value}' cannot edit content; need admin or isms_manager.",
        )
    return user
