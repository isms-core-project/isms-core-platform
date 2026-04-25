"""Fernet symmetric encryption utility for connector config storage.

Key is derived from SECRET_KEY env var using PBKDF2-HMAC-SHA256
(600,000 iterations, fixed app salt) — NIST SP 800-132 compliant.

Migration: run scripts/migrate_reencrypt_configs.py once after upgrading
from v1 (SHA-256 derivation) to v2 (PBKDF2 derivation).
"""

import base64
import hashlib
import json
import logging
import os

from cryptography.fernet import Fernet

logger = logging.getLogger(__name__)

# Fixed application salt — domain-separates the derived key from other uses
# of SECRET_KEY. A fixed salt is appropriate here because SECRET_KEY is
# already a strong random value; the iterations provide brute-force resistance.
_SALT = b"isms-core-connector-config-v2"
_ITERATIONS = 600_000


def _get_fernet() -> Fernet:
    secret = os.environ.get("SECRET_KEY", "")
    if not secret:
        raise RuntimeError("SECRET_KEY env var is not set — cannot encrypt/decrypt connector config")
    key_bytes = hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=secret.encode(),
        salt=_SALT,
        iterations=_ITERATIONS,
        dklen=32,
    )
    return Fernet(base64.urlsafe_b64encode(key_bytes))


def _get_fernet_v1(secret: str) -> Fernet:
    """Legacy SHA-256 derivation — used only by the migration script."""
    key_bytes = hashlib.sha256(secret.encode()).digest()
    return Fernet(base64.urlsafe_b64encode(key_bytes))


def encrypt_config(config: dict) -> str:
    """Encrypt a config dict to a Fernet token string."""
    payload = json.dumps(config, separators=(",", ":")).encode()
    return _get_fernet().encrypt(payload).decode()


def decrypt_config(token: str) -> dict:
    """Decrypt a Fernet token string back to a config dict."""
    plaintext = _get_fernet().decrypt(token.encode())
    return json.loads(plaintext)
