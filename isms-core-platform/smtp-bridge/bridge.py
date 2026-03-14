"""SMTP → Microsoft Graph API bridge.

Accepts SMTP on port 1025 (internal Docker network only — no auth required)
and forwards every message via Microsoft Graph API sendMail.

Architecture
------------
  Backend / Worker
      │  SMTP  (port 1025, internal)
      ▼
  isms-core-smtp-bridge   ←─ this service
      │  HTTPS  POST /v1.0/users/{from}/sendMail
      ▼
  Microsoft Graph API  →  Exchange Online / M365

Azure App Registration requirements
------------------------------------
  Permissions : Mail.Send  (Application, not Delegated)
  Grant       : Admin consent required

Environment variables
---------------------
  Required:
    TENANT_ID       Azure AD tenant ID (GUID)
    CLIENT_ID       App registration client ID (GUID)
    CLIENT_SECRET   App registration client secret
    FROM_ADDRESS    Sender mailbox, e.g. isms-core@yourdomain.com

  Optional:
    FROM_NAME       Display name (default: ISMS CORE)
    SMTP_PORT       SMTP listen port (default: 1025)
    LOG_LEVEL       INFO | DEBUG | WARNING (default: INFO)
"""

import logging
import os
import signal
import time
from email import message_from_bytes

import msal
import requests
from aiosmtpd.controller import Controller

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger("smtp-bridge")

# ---------------------------------------------------------------------------
# Config  (fail fast on missing required vars)
# ---------------------------------------------------------------------------

def _require(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Required environment variable {name!r} is not set")
    return value


TENANT_ID     = _require("TENANT_ID")
CLIENT_ID     = _require("CLIENT_ID")
CLIENT_SECRET = _require("CLIENT_SECRET")
FROM_ADDRESS  = _require("FROM_ADDRESS")
FROM_NAME     = os.getenv("FROM_NAME", "ISMS CORE")
SMTP_PORT     = int(os.getenv("SMTP_PORT", "1025"))

GRAPH_SCOPE    = ["https://graph.microsoft.com/.default"]
GRAPH_SEND_URL = f"https://graph.microsoft.com/v1.0/users/{FROM_ADDRESS}/sendMail"

# ---------------------------------------------------------------------------
# MSAL token client  (built-in cache — reuses tokens until expiry)
# ---------------------------------------------------------------------------

_msal_app = msal.ConfidentialClientApplication(
    CLIENT_ID,
    authority=f"https://login.microsoftonline.com/{TENANT_ID}",
    client_credential=CLIENT_SECRET,
)


def _get_token() -> str:
    result = _msal_app.acquire_token_silent(GRAPH_SCOPE, account=None)
    if not result:
        result = _msal_app.acquire_token_for_client(scopes=GRAPH_SCOPE)
    if "access_token" not in result:
        err = result.get("error_description") or result.get("error") or str(result)
        raise RuntimeError(f"Token acquisition failed: {err}")
    return result["access_token"]


# ---------------------------------------------------------------------------
# Message builder
# ---------------------------------------------------------------------------

def _build_graph_payload(envelope, raw_bytes: bytes) -> dict:
    msg = message_from_bytes(raw_bytes)
    subject = msg.get("Subject", "(no subject)")

    html_body: str | None = None
    text_body: str | None = None

    if msg.is_multipart():
        for part in msg.walk():
            ct = part.get_content_type()
            payload = part.get_payload(decode=True)
            if payload is None:
                continue
            content = payload.decode("utf-8", errors="replace")
            if ct == "text/html" and html_body is None:
                html_body = content
            elif ct == "text/plain" and text_body is None:
                text_body = content
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            content = payload.decode("utf-8", errors="replace")
            if msg.get_content_type() == "text/html":
                html_body = content
            else:
                text_body = content

    return {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "HTML" if html_body else "Text",
                "content": html_body or text_body or "",
            },
            "from": {
                "emailAddress": {
                    "address": FROM_ADDRESS,
                    "name": FROM_NAME,
                }
            },
            "toRecipients": [
                {"emailAddress": {"address": addr}}
                for addr in envelope.rcpt_tos
            ],
        },
        "saveToSentItems": False,
    }


# ---------------------------------------------------------------------------
# SMTP handler
# ---------------------------------------------------------------------------

class GraphMailHandler:
    async def handle_DATA(self, server, session, envelope):
        subject = "(unknown)"
        try:
            payload = _build_graph_payload(envelope, envelope.content)
            subject = payload["message"]["subject"]
            to_addrs = envelope.rcpt_tos

            token = _get_token()
            resp = requests.post(
                GRAPH_SEND_URL,
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                },
                json=payload,
                timeout=30,
            )

            if resp.status_code == 202:
                logger.info("Sent: subject=%r to=%s", subject, to_addrs)
                return "250 Message accepted"
            else:
                logger.error(
                    "Graph API error %d: subject=%r to=%s — %s",
                    resp.status_code, subject, to_addrs, resp.text[:300],
                )
                return "451 Requested action aborted: upstream error"

        except Exception as e:
            logger.error("Failed: subject=%r error=%s", subject, e, exc_info=True)
            return "451 Requested action aborted: internal error"


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    # Validate token on startup — fail immediately if credentials are wrong
    logger.info("Validating Azure credentials…")
    try:
        _get_token()
        logger.info("Token OK.")
    except Exception as e:
        logger.error("Startup failed — cannot acquire Graph token: %s", e)
        raise SystemExit(1)

    handler = GraphMailHandler()
    controller = Controller(handler, hostname="0.0.0.0", port=SMTP_PORT)
    controller.start()

    logger.info("SMTP bridge ready — port %d → Graph API", SMTP_PORT)
    logger.info("Sending as: %s <%s>", FROM_NAME, FROM_ADDRESS)

    def _stop(sig, frame):
        logger.info("Shutting down…")
        controller.stop()
        raise SystemExit(0)

    signal.signal(signal.SIGTERM, _stop)
    signal.signal(signal.SIGINT, _stop)

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
