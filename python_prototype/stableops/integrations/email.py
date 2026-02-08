"""Email integration for sending newsletters. Stubbed when no credentials."""

import os
from typing import Optional

# Placeholder: could use SMTP or SendGrid etc.
SMTP_CONFIGURED = bool(os.environ.get("STABLEOPS_SMTP_HOST") or os.environ.get("SENDGRID_API_KEY"))


def send_newsletter(
    to: str,
    subject: str,
    body_plain: str,
    body_html: Optional[str] = None,
) -> dict:
    """
    Send a newsletter email. Returns {"ok": True, "message_id": "..."} or {"ok": False, "error": "..."}.
    Stub returns ok=False with a message when not configured.
    """
    if not SMTP_CONFIGURED:
        return {
            "ok": False,
            "error": "Email not configured. Set STABLEOPS_SMTP_HOST (and user/pass) or SENDGRID_API_KEY for real sending.",
        }
    # TODO: implement SMTP or SendGrid
    return {"ok": False, "error": "Email integration not yet implemented."}
