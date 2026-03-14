"""Fernet symmetric encryption utility for connector config storage.

Key is derived from SECRET_KEY env var (SHA-256 → 32 bytes → base64url).
This ensures config_encrypted is tied to the deployment's secret key.
"""

import base64
import hashlib
import json
import logging
import os

from cryptography.fernet import Fernet

logger = logging.getLogger(__name__)


def _get_fernet() -> Fernet:
    secret = os.environ.get("SECRET_KEY", "")
    if not secret:
        raise RuntimeError("SECRET_KEY env var is not set — cannot encrypt/decrypt connector config")
    # Derive a 32-byte key from SECRET_KEY using SHA-256, then base64url-encode
    key_bytes = hashlib.sha256(secret.encode()).digest()
    fernet_key = base64.urlsafe_b64encode(key_bytes)
    return Fernet(fernet_key)


def encrypt_config(config: dict) -> str:
    """Encrypt a config dict to a Fernet token string."""
    payload = json.dumps(config, separators=(",", ":")).encode()
    return _get_fernet().encrypt(payload).decode()


def decrypt_config(token: str) -> dict:
    """Decrypt a Fernet token string back to a config dict."""
    plaintext = _get_fernet().decrypt(token.encode())
    return json.loads(plaintext)
