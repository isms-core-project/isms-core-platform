#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 7.7 Pre-work — Status DV Normalisation

For every input sheet in sheet_schemas:
  1. Detect false-positive is_status_col flags (type/category columns)
  2. Add emoji prefix to plain-text status values (✅/⚠️/❌)
  3. Fix ⚠ (bare U+26A0) → ⚠️ (U+26A0 + U+FE0F variation selector)
  4. Leave already-correct emoji values untouched
  5. Report values that could not be classified

Updates sheet_schemas JSONB in generator_definitions table.

Run from repo root (60-isms-core-api/):
  python3 datasets/scripts/normalise_status_dvs.py [--dry-run]
"""

import json
import logging
import os
import re
import sys
from pathlib import Path

import psycopg2

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger(__name__)

SCHEMA_FILE = Path(__file__).resolve().parent.parent / "data" / "workbook_schemas.json"
DB_DSN = os.environ.get(
    "DATABASE_URL",
    "postgresql://isms_user:change_this_password_in_production@localhost:5432/isms_db",
)
DRY_RUN = "--dry-run" in sys.argv

CHECK = "✅"
WARN  = "⚠️"   # U+26A0 U+FE0F
XMARK = "❌"

# ── Compliance vocabulary ──────────────────────────────────────────────────────
# Positive (✅): control in place, goal achieved, compliant state
POSITIVE = {
    "compliant", "yes", "implemented", "fully implemented", "fully_implemented",
    "complete", "completed", "active", "pass", "passed", "verified", "covered",
    "encrypted", "achieved", "met", "addressed", "resolved", "closed", "approved",
    "authorised", "authorized", "deployed", "enabled", "operational", "done",
    "effective", "present", "exists", "in place", "configured", "applied",
    "maintained", "adequate", "satisfactory", "established", "defined",
    "documented", "controlled", "permitted", "accepted", "risk accepted",
    "validated", "full", "enforced", "mitigated", "remediated",
    "applicable", "current", "labelled", "released", "fully staffed",
    "physical destruction", "continuously improving", "substantially implemented",
    "permitted with conditions",
    # Additional positive states
    "no gap", "compliance achieved", "correlated", "fully masked", "integrated",
    "fully_integrated", "on schedule", "running", "stable", "installed", "renewed",
    "delivered", "verified closed", "updated baseline", "authorised only",
    "clustered", "active-active", "active-passive", "active/active", "active/passive",
    "authorised retroactively", "approved retroactively",
    "active - acceptable", "active - recommended", "no restriction",
    "100% (all equipment)", "prohibited - block",
}

# Partial / in-progress (⚠️): work started but not complete, needs attention
PARTIAL = {
    "partial", "partially", "partially implemented", "partially_implemented",
    "in progress", "in-progress", "pending", "under review", "under-review",
    "planned", "limited", "needs improvement", "partially compliant",
    "partially encrypted", "conditional", "some", "mixed", "informal",
    "partially addressed", "partially met", "partially covered", "on hold",
    "not tested", "draft", "pending rotation", "partially configured",
    "partially applied", "partially deployed", "partial compliance",
    "partially achieved", "partially done", "partially established",
    "partially defined", "partially controlled", "partially documented",
    "partially verified", "partially enforced", "partially mitigated",
    "proposed", "pilot", "testing", "under enforcement", "scheduled",
    "pending approval", "pending verification", "expiring soon", "maintenance",
    "implementation in progress", "in development", "in draft", "partially staffed",
    "partially effective", "postponed",
    # Additional partial states
    "improving", "enrollment in progress", "onboarding in progress",
    "remediation in progress", "in procurement", "in testing", "planning",
    "revalidating", "under evaluation", "under investigation", "under_review",
    "paused", "legal review", "pending review", "awaiting signature", "submitted",
    "ordered", "partially masked", "partially adequate", "barely adequate",
    "minimal", "standby", "pending revocation", "degraded",
    "over-deployed", "under-utilised", "discovered", "partial coverage",
    "partial (critical only)", "urgent", "verification pending",
    "scheduled for enrollment", "partially_integrated",
}

# Negative (❌): control not in place, failed, non-compliant state
NEGATIVE = {
    "non-compliant", "non compliant", "noncompliant", "no", "not implemented",
    "not done", "incomplete", "inactive", "fail", "failed", "not verified",
    "not covered", "not encrypted", "not achieved", "not met", "not addressed",
    "missing", "absent", "not-compliant", "not complete", "not completed",
    "not active", "not configured", "not applied", "not deployed", "not enabled",
    "not operational", "not present", "not effective", "not established",
    "not defined", "not documented", "not controlled", "not started", "not-started",
    "not permitted", "inadequate", "unsatisfactory", "not maintained", "blocked",
    "overdue", "expired", "cancelled", "rejected", "revoked", "retired",
    "superseded", "archived", "deprecated", "destroyed", "suspended", "ineffective",
    "not_used", "not used", "no capability", "prohibited",
    "not-implemented", "not-covered", "not-compliant",
    "open", "disabled", "terminated", "escalated", "unauthorised",
    "not labelled", "decommissioned", "never",
    # Additional negative states
    "gap identified", "worsening", "unresolved", "uncontrolled", "all expired",
    "expired - not renewed", "deprecated - migrate", "failed assessment",
    "verification failed", "pattern failure", "sync failure", "configuration error",
    "rolled back", "excessive drift (critical)", "excessive drift (general)",
    "ntp not configured", "ntp server unreachable", "revoked - controls failed",
    "revoked - risk changed", "lost", "single point of failure", "no ups",
    "not_integrated", "not correlated", "not masked", "not supported",
    "departed", "withdrawn", "offline", "removed", "unresolved",
}

# Neutral: not applicable / unknown — keep without emoji
NEUTRAL = {
    "n/a", "not applicable", "unknown", "not assessed", "deferred",
    "accepted risk", "accepted-risk", "out of scope", "not in scope",
    "exempted", "excluded", "not relevant", "not required", "tbd",
    "to be determined", "not evaluated", "none", "other",
    "n/a (not applicable)",
    # Additional neutral states
    "waived", "not needed", "uncertain", "unknown status", "excluded system",
    "n/a - sole occupant", "n/a (named account)", "n/a (service account)",
    "conditionally applicable", "new", "on leave", "on_leave", "required",
    "optional", "system decommissioned", "factory reset", "secure overwrite",
    "crypto erase", "cryptographic erasure", "3-pass overwrite",
    "multi-pass overwrite", "config wipe", "format", "deletion",
    "reverted to baseline", "vacant", "standby", "not correlated",
    "will_use_later", "recommended", "no action (false positive)",
    "active obligations", "no guidelines", "no labels",
}

# ── False-positive token detection ────────────────────────────────────────────
# If a DV set contains ≥2 of these, it is a type/category column — not a status column
FALSE_POSITIVE_TOKENS = {
    # Authentication / credential types
    "password", "mfa", "certificate", "token", "sso", "federation",
    "biometric", "api key", "service account", "hkdf",
    # Cryptographic algorithm names
    "aes-128", "aes-256", "rsa", "ecdsa", "3des",
    # DR / resilience test types
    "backup restore", "failover test", "full dr scenario", "tabletop exercise",
    "component test", "integration test",
    # Degradation / bypass types
    "temporary bypass", "reduced capability", "alternative method",
    # Physical workspace types
    "meeting room", "open plan office", "private office", "reception", "shared space",
    # Attack / incident types (these are incident type columns)
    "tailgating", "unauthorised access",
    # Risk / severity rating levels
    "high", "medium", "low", "critical", "informational", "info", "very high", "very low",
    "negligible", "minor", "moderate", "major", "catastrophic", "severe",
    # Data classification levels
    "internal", "public", "confidential", "restricted", "top secret", "secret",
    "unclassified", "sensitive", "private", "proprietary",
    # Frequency / schedule values
    "daily", "weekly", "monthly", "quarterly", "annually", "annual", "biannual",
    "biannually", "bi-annual", "continuous", "continuously", "real-time", "hourly",
    "per event", "as needed", "ad hoc", "on demand", "never",
    # Day-of-week abbreviations / calendar
    "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",
    "s", "m", "t", "w", "f", "su", "sa", "p",
    # Environment / infrastructure types
    "production", "staging", "development", "dev", "test", "uat", "sandbox",
    "cloud", "hybrid", "on-premises", "on-premise", "on premises", "saas", "paas",
    "iaas", "faas", "container", "serverless", "virtual", "physical",
    # Data / system types
    "database", "email", "file server", "web server", "application", "api",
    "endpoint", "network", "firewall", "proxy", "vpn", "dmz",
    # Evidence / document types
    "policy document", "procedure", "meeting minutes", "audit log", "audit trail",
    "configuration export", "risk assessment", "vulnerability scan", "penetration test",
    "screenshot", "report", "log file", "ticket", "training record",
    # Traffic light / RAG colours
    "amber", "green", "red", "clear", "blue", "grey", "gray", "orange", "yellow",
    # Numeric / score values (single digits or short numerics)
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    # Asset / data sensitivity types
    "personal data", "pii", "financial data", "health data", "business data",
    "intellectual property", "trade secret",
    # Ownership / responsibility types
    "owner", "custodian", "processor", "controller", "administrator",
    # Impact / likelihood descriptors
    "almost certain", "likely", "possible", "unlikely", "rare",
    "insignificant", "marginal",
    # Retention / lifecycle terms
    "immediate", "1 year", "2 years", "3 years", "5 years", "7 years", "10 years",
    "permanent", "indefinite",
    # Attack / incident type columns
    "brute force attack", "phishing", "xss", "sql injection", "malware", "ddos",
    "authentication bypass", "authorisation issue", "insider threat",
    "data exfiltration", "sensitive data exposure", "reinfection",
    "clickjacking", "ransomware", "social engineering",
    "clicked phishing", "submitted credentials",
    # Personnel / role type columns
    "contractor", "consultant", "employee", "vendor rep", "customer rep",
    "partner rep", "board member", "third-party admin", "authorised signatory",
    "witness", "visitor", "active member", "former member",
    # Authentication method type columns (compound values)
    "password only", "password vaulting", "certificate-based", "smart card",
    "saml idp", "ldap", "oauth provider", "database auth",
    "hardware token (fido2)", "ssо (password-based)",
    # Approval / change process types
    "cab meeting", "email approval", "emergency verbal",
    # Bracket-coded category values (if ≥2 found it's a coded-category column)
    "[bug]", "[disk]", "[tool]", "[unlock]", "[web]",
}


def _is_false_positive(dv_values: list[str]) -> bool:
    """Return True if this DV set is a type/category column, not a compliance status column."""
    lower_vals = {v.strip().lower() for v in dv_values if v}
    fp_hits = sum(1 for v in lower_vals if v in FALSE_POSITIVE_TOKENS)
    return fp_hits >= 2


def _fix_emoji(v: str) -> str:
    """Replace bare ⚠ (U+26A0) with ⚠️ (U+26A0 + U+FE0F variation selector)."""
    return re.sub(r"⚠(?!\uFE0F)", "⚠️", v)


def _classify(v: str) -> str | None:
    """
    Classify a plain-text DV value.
    Returns emoji prefix (CHECK/WARN/XMARK/'') or None if unknown.
    '' = neutral (no emoji needed).
    None = cannot classify (needs human review).
    """
    clean = v.strip()
    if not clean:
        return ""
    first = clean[0]
    if ord(first) > 127:
        return ""   # already has emoji — handled by _fix_emoji
    if first == "[":
        return ""   # bracket-coded value (e.g. [PASS], [FAIL], [WARN]) — leave as-is
    lower = clean.lower()
    # Compound "Yes - ..." / "No - ..." prefix matching
    if lower == "yes" or lower.startswith("yes -") or lower.startswith("yes ("):
        return CHECK
    if lower == "no" or lower.startswith("no -") or lower.startswith("no ("):
        return XMARK
    if lower in POSITIVE:
        return CHECK
    if lower in PARTIAL:
        return WARN
    if lower in NEGATIVE:
        return XMARK
    if lower in NEUTRAL:
        return ""
    return None


def normalise_dv_value(v: str) -> tuple[str, bool]:
    """
    Normalise a single DV value.
    Returns (normalised_value, changed: bool).
    """
    if not v:
        return v, False
    fixed = _fix_emoji(v)
    # If it now starts with emoji, done
    if fixed and ord(fixed[0]) > 127:
        return fixed, fixed != v
    # Add emoji prefix to plain-text values
    prefix = _classify(fixed)
    if prefix is None or prefix == "":
        return fixed, fixed != v   # unknown or neutral — return as-is (emoji-fixed only)
    result = f"{prefix} {fixed}"
    return result, True


def normalise_sheet_schemas(schemas: list[dict]) -> tuple[list[dict], dict]:
    """Apply normalisation to all columns in all sheets. Returns (schemas, stats)."""
    stats = {
        "sheets_processed": 0,
        "cols_updated": 0,
        "false_positives_fixed": 0,
        "values_updated": 0,
        "unknowns": [],
    }

    for sheet in schemas:
        stats["sheets_processed"] += 1
        for col in sheet.get("columns", []):
            dv = col.get("dv_values", [])
            if not dv:
                continue

            # Step 1: false-positive check
            if col.get("is_status_col") and _is_false_positive(dv):
                col["is_status_col"] = False
                if sheet.get("status_column_index") == col["index"]:
                    sheet["status_column_index"] = None
                    sheet["status_column_letter"] = None
                stats["false_positives_fixed"] += 1
                logger.info(
                    "  FP fixed: sheet='%s' col=%s '%s' %s",
                    sheet["sheet_name"], col["letter"], col["header"], dv,
                )
                continue

            # Step 2: normalise DV values
            is_status = col.get("is_status_col", False)
            norm_dvs = []
            any_changed = False
            for v in dv:
                norm, changed = normalise_dv_value(v)
                norm_dvs.append(norm)
                if changed:
                    any_changed = True
                # Track unknowns only for status columns (other DV columns may have any vocabulary)
                if is_status and v and ord(v[0]) < 128 and _classify(v.strip()) is None:
                    stats["unknowns"].append(f"{sheet['sheet_name']}:{col['header']}:{v}")

            if any_changed:
                col["dv_values"] = norm_dvs
                stats["cols_updated"] += 1
                stats["values_updated"] += sum(1 for a, b in zip(dv, norm_dvs) if a != b)

    return schemas, stats


def main() -> None:
    records = json.loads(SCHEMA_FILE.read_text())
    logger.info("Loaded %d generator records", len(records))
    if DRY_RUN:
        logger.info("DRY RUN — no DB changes will be made")

    conn = psycopg2.connect(DB_DSN)
    conn.autocommit = False
    cur = conn.cursor()

    totals = {
        "generators_updated": 0,
        "cols_updated": 0,
        "false_positives_fixed": 0,
        "values_updated": 0,
        "unknowns": [],
    }

    for rec in records:
        doc_id = rec["document_id"]
        sheets = rec.get("sheets", [])
        if not sheets:
            continue

        normalised, stats = normalise_sheet_schemas(sheets)

        changed = stats["cols_updated"] > 0 or stats["false_positives_fixed"] > 0
        if changed:
            if not DRY_RUN:
                cur.execute(
                    "UPDATE generator_definitions SET sheet_schemas = %s WHERE document_id = %s",
                    (json.dumps(normalised), doc_id),
                )
            totals["generators_updated"] += 1

        totals["cols_updated"] += stats["cols_updated"]
        totals["false_positives_fixed"] += stats["false_positives_fixed"]
        totals["values_updated"] += stats["values_updated"]
        totals["unknowns"].extend(stats["unknowns"])

    if not DRY_RUN:
        conn.commit()
    cur.close()
    conn.close()

    unknowns = sorted(set(totals["unknowns"]))
    logger.info("=" * 60)
    logger.info("Generators updated:       %d", totals["generators_updated"])
    logger.info("Columns updated:          %d", totals["cols_updated"])
    logger.info("Values updated:           %d", totals["values_updated"])
    logger.info("False positives fixed:    %d", totals["false_positives_fixed"])
    logger.info("Remaining unknowns:       %d unique (sheet:col:value)", len(unknowns))

    if unknowns:
        logger.warning("Values needing manual review:")
        from collections import Counter
        just_vals = Counter(u.rsplit(":", 1)[1] for u in unknowns)
        for val, cnt in just_vals.most_common():
            logger.warning("  %3dx  '%s'", cnt, val)

    if DRY_RUN:
        logger.info("DRY RUN complete — re-run without --dry-run to apply")


if __name__ == "__main__":
    main()
