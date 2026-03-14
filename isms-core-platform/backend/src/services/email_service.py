"""Email service — Phase 9.5.

Thin smtplib wrapper.  All public functions are graceful no-ops when
MAIL_HOST is not configured — the application works fully without email.

Architecture (pluggable via env vars):
  Dev:       MAIL_HOST=isms-core-mailhog  MAIL_PORT=1025  (catch-all, web UI :8025)
  Prod LAN:  MAIL_HOST=<postfix-relay>    MAIL_PORT=25
  Prod M365: MAIL_HOST=<smtp-bridge>      MAIL_PORT=25    (SmtpToGraphBridge)

No authentication is configured here — the SMTP relay handles auth upstream.
TLS is not used because the relay is always on the same Docker network (LAN).
For external SMTP with auth/TLS, extend _send_message() accordingly.

Usage:
    from src.services.email_service import send_email

    send_email(
        to=["john@example.com"],
        subject="Evidence expiring soon",
        html_body="<p>Your evidence <b>EV-001</b> expires in 7 days.</p>",
        text_body="Your evidence EV-001 expires in 7 days.",  # optional plain-text fallback
    )
"""

import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from src.core.config import get_settings

logger = logging.getLogger(__name__)

# Jinja2 environment — loads from backend/templates/email/
_TEMPLATES_DIR = Path(__file__).parent.parent.parent / "templates" / "email"
_jinja_env = Environment(
    loader=FileSystemLoader(str(_TEMPLATES_DIR)),
    autoescape=select_autoescape(["html"]),
)


def is_enabled() -> bool:
    """Return True if email sending is configured."""
    return bool(get_settings().mail_host)


def send_email(
    to: list[str],
    subject: str,
    html_body: str,
    text_body: str | None = None,
    cc: list[str] | None = None,
    reply_to: str | None = None,
) -> bool:
    """Send an email.  Returns True on success, False on failure or if disabled.

    Args:
        to:        List of recipient addresses.
        subject:   Email subject line.
        html_body: HTML content (required).
        text_body: Plain-text fallback (optional — auto-stripped from HTML if omitted).
        cc:        CC recipients (optional).
        reply_to:  Reply-To header (optional).

    Returns:
        True  — email accepted by SMTP relay.
        False — email disabled (MAIL_HOST not set) or delivery failed.
    """
    settings = get_settings()

    if not settings.mail_host:
        logger.debug("Email disabled (MAIL_HOST not set) — skipping send to %s", to)
        return False

    try:
        msg = _build_message(
            to=to,
            subject=subject,
            html_body=html_body,
            text_body=text_body,
            cc=cc,
            reply_to=reply_to,
            settings=settings,
        )
        _send_message(msg, to, cc or [], settings)
        logger.info("Email sent: subject=%r to=%s", subject, to)
        return True

    except Exception as e:
        logger.error("Email send failed: %s", e, exc_info=True)
        return False


# ---------------------------------------------------------------------------
# Template renderer
# ---------------------------------------------------------------------------

def render_template(template_name: str, context: dict) -> str:
    """Render a Jinja2 email template and return HTML string.

    Args:
        template_name: Filename in templates/email/, e.g. 'welcome.html'
        context:       Variables passed to the template.
    """
    template = _jinja_env.get_template(template_name)
    return template.render(**context)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _build_message(
    to: list[str],
    subject: str,
    html_body: str,
    text_body: str | None,
    cc: list[str] | None,
    reply_to: str | None,
    settings,
) -> MIMEMultipart:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = formataddr((settings.mail_from_name, settings.mail_from))
    msg["To"] = ", ".join(to)
    if cc:
        msg["Cc"] = ", ".join(cc)
    if reply_to:
        msg["Reply-To"] = reply_to

    # Plain-text part first (lowest priority for MIMEMultipart/alternative)
    plain = text_body or _strip_html(html_body)
    msg.attach(MIMEText(plain, "plain", "utf-8"))
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    return msg


def _send_message(
    msg: MIMEMultipart,
    to: list[str],
    cc: list[str],
    settings,
) -> None:
    recipients = to + cc
    with smtplib.SMTP(settings.mail_host, settings.mail_port, timeout=settings.mail_timeout) as smtp:
        smtp.sendmail(settings.mail_from, recipients, msg.as_string())


def _strip_html(html: str) -> str:
    """Very basic HTML → plain-text strip for fallback bodies."""
    import re
    text = re.sub(r"<br\s*/?>", "\n", html, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
