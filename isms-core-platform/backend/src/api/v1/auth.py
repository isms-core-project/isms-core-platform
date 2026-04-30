import uuid

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from fastapi.responses import JSONResponse
from jwt.exceptions import InvalidTokenError
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session as DBSession

from src.core.config import get_settings
from src.core.dependencies import get_current_user
from src.core.limiter import limiter
from src.database.session import get_db
from src.schemas.auth import (
    LoginRequest,
    MfaBackupCodesResponse,
    MfaDisableRequest,
    MfaEnableRequest,
    MfaEnableResponse,
    MfaLoginResponse,
    MfaSetupResponse,
    MfaVerifyRequest,
    TokenResponse,
)
from src.schemas.users import (
    NOTIFICATION_EVENTS,
    NotificationPrefRead,
    NotificationPrefsResponse,
    NotificationPrefsPatch,
)
from src.services.audit_service import CAT_SECURITY, SEV_INFO, SEV_WARNING, log_event
from src.services.auth_service import authenticate_user, create_session, create_token_pair, delete_session_by_token, refresh_tokens

router = APIRouter(prefix="/auth", tags=["auth"])


def _token_response_with_cookie(tokens: dict) -> JSONResponse:
    """Build a JSON response with access_token body + refresh_token as HttpOnly cookie."""
    settings = get_settings()
    resp = JSONResponse({"access_token": tokens["access_token"], "token_type": "bearer"})
    resp.set_cookie(
        key="refresh_token",
        value=tokens["refresh_token"],
        httponly=True,
        secure=settings.cookie_secure,
        samesite="strict",
        path="/api/v1/auth",
        max_age=settings.refresh_token_expire_minutes * 60,
    )
    return resp


@router.post("/login")
@limiter.limit("10/minute")
def login(request: Request, body: LoginRequest, db: DBSession = Depends(get_db)):
    client_ip = request.client.host if request.client else None
    user = authenticate_user(db, body.email, body.password)
    if not user:
        log_event(db, event_type="login.failure", category=CAT_SECURITY, severity=SEV_WARNING,
                  actor_email=body.email, ip_address=client_ip,
                  description=f"Failed login attempt for {body.email}")
        db.commit()
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    log_event(db, event_type="login.success", category=CAT_SECURITY, severity=SEV_INFO,
              user_id=user.id, actor_email=user.email, ip_address=client_ip,
              description=f"User {user.email} logged in")
    if user.mfa_enabled:
        db.commit()
        from src.services.mfa_service import create_mfa_token
        mfa_token = create_mfa_token(user.id)
        return MfaLoginResponse(mfa_token=mfa_token)
    tokens = create_token_pair(user)
    user_agent = request.headers.get("user-agent")
    create_session(db, user, tokens["refresh_token"], client_ip, user_agent)
    db.commit()
    return _token_response_with_cookie(tokens)


@router.post("/refresh")
@limiter.limit("20/minute")
def refresh(request: Request, db: DBSession = Depends(get_db)):
    old_token = request.cookies.get("refresh_token")
    if not old_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No refresh token")
    try:
        result = refresh_tokens(db, old_token)
    except InvalidTokenError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid refresh token: {e}")
    if not result:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not refresh token")
    # Rotate session row: delete old, create new
    delete_session_by_token(db, old_token)
    from src.core.security import decode_token
    payload = decode_token(result["refresh_token"])
    user_id = payload.get("sub")
    if user_id:
        from src.domain.users import User
        user = db.get(User, user_id)
        if user:
            user_agent = request.headers.get("user-agent")
            client_ip = request.client.host if request.client else None
            create_session(db, user, result["refresh_token"], client_ip, user_agent)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()  # concurrent refresh already inserted this token — not an error
    return _token_response_with_cookie(result)


@router.post("/logout", status_code=204)
def logout(request: Request, response: Response, db: DBSession = Depends(get_db)):
    """Clear the HttpOnly refresh token cookie and revoke the session."""
    refresh_token = request.cookies.get("refresh_token")
    if refresh_token:
        delete_session_by_token(db, refresh_token)
        db.commit()
    response.delete_cookie(key="refresh_token", path="/api/v1/auth")


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


# ---------------------------------------------------------------------------
# Active project selection (per product family)
# ---------------------------------------------------------------------------

class ActiveProjectPatch(BaseModel):
    product_family: str   # ISMS | PRIVACY | CLOUD | SEC
    project_id: uuid.UUID | None = None  # None clears the active selection


@router.patch("/me/active-project")
def set_active_project(
    body: ActiveProjectPatch,
    current_user=Depends(get_current_user),
    db: DBSession = Depends(get_db),
):
    """Set (or clear) the active project for a given product family.

    Stores in user.active_projects as {"ISMS": "<uuid>", "PRIVACY": "<uuid>", ...}.
    The frontend reads this to determine which project is 'active' per product.
    """
    fam = body.product_family.upper()
    if fam not in ("ISMS", "PRIVACY", "CLOUD", "AI", "SEC"):
        raise HTTPException(status_code=422, detail="product_family must be ISMS, PRIVACY, CLOUD, AI, or SEC")

    active = dict(current_user.active_projects or {})
    if body.project_id is None:
        active.pop(fam, None)
    else:
        active[fam] = str(body.project_id)

    current_user.active_projects = active
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return {"product_family": fam, "project_id": active.get(fam)}


# ---------------------------------------------------------------------------
# MFA — setup / enable / disable / verify / backup-code regeneration
# ---------------------------------------------------------------------------

@router.get("/mfa/status")
def mfa_status(current_user=Depends(get_current_user)):
    """Return current MFA state for the authenticated user."""
    return {
        "mfa_enabled": bool(current_user.mfa_enabled),
        "has_backup_codes": bool(current_user.mfa_backup_codes),
    }

@router.post("/mfa/setup", response_model=MfaSetupResponse)
def mfa_setup(
    current_user=Depends(get_current_user),
    db: DBSession = Depends(get_db),
):
    """Generate a new TOTP secret and QR code for the current user.

    Does NOT enable MFA — user must call /mfa/enable with a verified code.
    Calling setup again overwrites any pending (not-yet-enabled) secret.
    """
    import base64
    import io

    import qrcode
    from src.services.mfa_service import generate_totp_secret, get_totp_uri

    secret = generate_totp_secret()
    current_user.mfa_secret = secret
    db.add(current_user)
    db.commit()

    uri = get_totp_uri(secret, current_user.email)

    qr = qrcode.make(uri)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode()
    data_uri = f"data:image/png;base64,{b64}"

    return MfaSetupResponse(secret=secret, otpauth_uri=uri, qr_data_uri=data_uri)


@router.post("/mfa/enable", response_model=MfaEnableResponse)
def mfa_enable(
    body: MfaEnableRequest,
    current_user=Depends(get_current_user),
    db: DBSession = Depends(get_db),
):
    """Enable MFA after verifying the TOTP code from the authenticator app.

    Returns 8 plaintext backup codes — shown once, user must copy them.
    """
    from src.services.mfa_service import generate_backup_codes, hash_backup_code, verify_totp

    if not current_user.mfa_secret:
        raise HTTPException(status_code=400, detail="Call /mfa/setup first")
    if not verify_totp(current_user.mfa_secret, body.code):
        raise HTTPException(status_code=400, detail="Invalid TOTP code")

    plain_codes = generate_backup_codes(8)
    hashed_codes = [hash_backup_code(c) for c in plain_codes]

    current_user.mfa_enabled = True
    current_user.mfa_backup_codes = hashed_codes
    db.add(current_user)
    log_event(db, event_type="user.mfa_enabled", category=CAT_SECURITY, severity=SEV_INFO,
              user_id=current_user.id, actor_email=current_user.email,
              description=f"MFA enabled for {current_user.email}")
    db.commit()

    return MfaEnableResponse(backup_codes=plain_codes)


@router.post("/mfa/disable", status_code=204)
def mfa_disable(
    body: MfaDisableRequest,
    current_user=Depends(get_current_user),
    db: DBSession = Depends(get_db),
):
    """Disable MFA. Requires the current valid TOTP code."""
    from src.services.mfa_service import verify_totp

    if not current_user.mfa_enabled:
        raise HTTPException(status_code=400, detail="MFA is not enabled")
    if not verify_totp(current_user.mfa_secret, body.code):
        raise HTTPException(status_code=400, detail="Invalid TOTP code")

    current_user.mfa_enabled = False
    current_user.mfa_secret = None
    current_user.mfa_backup_codes = []
    db.add(current_user)
    log_event(db, event_type="user.mfa_disabled", category=CAT_SECURITY, severity=SEV_WARNING,
              user_id=current_user.id, actor_email=current_user.email,
              description=f"MFA disabled for {current_user.email}")
    db.commit()


@router.post("/mfa/verify")
@limiter.limit("10/minute")
def mfa_verify(
    request: Request,
    body: MfaVerifyRequest,
    db: DBSession = Depends(get_db),
):
    """Complete login by verifying TOTP code + mfa_token.

    Returns a full token pair (access_token + refresh_token).
    Accepts either a 6-digit TOTP code or a XXXX-XXXX backup code.
    """
    from src.domain.users import User as UserModel
    from src.services.mfa_service import verify_backup_code, verify_mfa_token, verify_totp

    user_id = verify_mfa_token(body.mfa_token)
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired MFA token")

    user = db.get(UserModel, user_id)
    if not user or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    code = body.code.strip().upper()
    is_backup = "-" in code

    client_ip = request.client.host if request.client else None
    if is_backup:
        if not verify_backup_code(user, code, db):
            log_event(db, event_type="login.mfa_failure", category=CAT_SECURITY, severity=SEV_WARNING,
                      user_id=user.id, actor_email=user.email, ip_address=client_ip,
                      description="Invalid MFA backup code")
            db.commit()
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid backup code")
    else:
        if not verify_totp(user.mfa_secret, code):
            log_event(db, event_type="login.mfa_failure", category=CAT_SECURITY, severity=SEV_WARNING,
                      user_id=user.id, actor_email=user.email, ip_address=client_ip,
                      description="Invalid MFA TOTP code")
            db.commit()
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid TOTP code")

    log_event(db, event_type="login.mfa_success", category=CAT_SECURITY, severity=SEV_INFO,
              user_id=user.id, actor_email=user.email, ip_address=client_ip,
              description=f"User {user.email} completed MFA login")
    tokens = create_token_pair(user)
    create_session(db, user, tokens["refresh_token"], client_ip, request.headers.get("user-agent"))
    db.commit()
    return _token_response_with_cookie(tokens)


@router.post("/mfa/backup-codes/regenerate", response_model=MfaBackupCodesResponse)
def mfa_regenerate_backup_codes(
    body: MfaEnableRequest,  # reuse — just needs `code: str`
    current_user=Depends(get_current_user),
    db: DBSession = Depends(get_db),
):
    """Regenerate backup codes. Requires current TOTP code. Previous codes are invalidated."""
    from src.services.mfa_service import generate_backup_codes, hash_backup_code, verify_totp

    if not current_user.mfa_enabled:
        raise HTTPException(status_code=400, detail="MFA is not enabled")
    if not verify_totp(current_user.mfa_secret, body.code):
        raise HTTPException(status_code=400, detail="Invalid TOTP code")

    plain_codes = generate_backup_codes(8)
    hashed_codes = [hash_backup_code(c) for c in plain_codes]

    current_user.mfa_backup_codes = hashed_codes
    db.add(current_user)
    db.commit()

    return MfaBackupCodesResponse(backup_codes=plain_codes)
