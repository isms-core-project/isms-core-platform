"""TOTP MFA service using pyotp."""
import hashlib
import hmac
import logging
import secrets
import string
import uuid
from datetime import datetime, timedelta, timezone

import pyotp
from jose import jwt
from sqlalchemy.orm import Session as DBSession

from src.core.config import get_settings
from src.domain.users import User

logger = logging.getLogger(__name__)

ISSUER = "ISMS CORE"
MFA_TOKEN_EXPIRE_MINUTES = 5  # short-lived token for MFA challenge step


def generate_totp_secret() -> str:
    """Generate a new TOTP secret."""
    return pyotp.random_base32()


def get_totp_uri(secret: str, email: str) -> str:
    """Return otpauth:// URI for QR code generation."""
    return pyotp.totp.TOTP(secret).provisioning_uri(name=email, issuer_name=ISSUER)


def verify_totp(secret: str, code: str) -> bool:
    """Verify a TOTP code against the secret. Allows 1 step of clock drift."""
    totp = pyotp.TOTP(secret)
    return totp.verify(code, valid_window=1)


def generate_backup_codes(count: int = 8) -> list[str]:
    """Generate one-time backup codes in format XXXX-XXXX."""
    alphabet = string.ascii_uppercase + string.digits
    codes = []
    for _ in range(count):
        part1 = ''.join(secrets.choice(alphabet) for _ in range(4))
        part2 = ''.join(secrets.choice(alphabet) for _ in range(4))
        codes.append(f"{part1}-{part2}")
    return codes


def hash_backup_code(code: str) -> str:
    """SHA-256 hash of a backup code for storage."""
    return hashlib.sha256(code.upper().encode()).hexdigest()


def verify_backup_code(user: User, code: str, db: DBSession) -> bool:
    """Check if code matches a stored backup code; if so, consume it.

    Uses hmac.compare_digest to prevent timing-based enumeration of valid codes.
    """
    code_hash = hash_backup_code(code)
    stored: list[str] = list(user.mfa_backup_codes or [])
    matched_hash: str | None = None
    for h in stored:
        if hmac.compare_digest(h, code_hash):
            matched_hash = h
            break
    if matched_hash is not None:
        stored.remove(matched_hash)
        user.mfa_backup_codes = stored
        db.commit()
        return True
    return False


def create_mfa_token(user_id: uuid.UUID) -> str:
    """Create a short-lived JWT used as the intermediate MFA challenge token."""
    settings = get_settings()
    expire = datetime.now(timezone.utc) + timedelta(minutes=MFA_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": str(user_id),
        "type": "mfa_challenge",
        "exp": expire,
    }
    return jwt.encode(payload, settings.secret_key, algorithm=settings.jwt_algorithm)


def verify_mfa_token(token: str) -> str | None:
    """Validate the MFA challenge token. Returns user_id string or None."""
    settings = get_settings()
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.jwt_algorithm])
        if payload.get("type") != "mfa_challenge":
            return None
        return payload.get("sub")
    except Exception:
        return None
