#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.2-3-5 — Authentication and Privileged Access Compliance Checklist

Controls A.8.2-3-5: Authentication and Privileged Access
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Identity and Access Mgmt Infra (1 reqs)
4. Authentication Requirements (13 reqs)
5. Privileged Access Management (18 reqs)
6. Access Restriction (7 reqs)
7. Key Performance Indicators (2 reqs)

Total: 41 requirements across 5 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/SCR/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_OP_ROOT / 'SCR'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.8.2-3-5"
CONTROL_ID = "A.8.2-3-5"
CONTROL_NAME = "Authentication and Privileged Access"
SOURCE_POLICY = "ISMS-OP-POL-A.8.2-3-5"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.2-3-5
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Identity and Access Mgmt Infra", [
        ("A.8.2-3-5-01", "Integration Points*: Idp",
         "Integration points*: IdP shall integrate with HR system for joiner/mover/leaver automation. PAM, IdP, and SIEM shall be integrated for centralised monitoring. MFA shall be enforced via IdP conditional access policies. Session recording logs shall forward to SIEM."),
    ]),

    ("Authentication Requirements", [
        ("A.8.2-3-5-02", "Access To Systems And Information Is",
         "Access to systems and information is authenticated by passwords or stronger mechanisms. The organisation shall enforce the following password standards, aligned with NIST SP 800-63B:."),
        ("A.8.2-3-5-03", "Passwords Found In Breach Databases",
         "Passwords found in breach databases shall be rejected at set/change and force-changed if detected during monthly scans. Screening coverage metric: percentage of password set/change events validated against breach databases (target: 100%)."),
        ("A.8.2-3-5-04", "Multi-Factor Authentication",
         "Multi-factor authentication shall be required for:."),
        ("A.8.2-3-5-05", "Sms-Based Otp Should Be Phased Out",
         "SMS-based OTP should be phased out where possible due to known vulnerabilities (SIM swapping, interception). Systems relying solely on SMS-based MFA shall be documented in the risk register with a migration plan."),
        ("A.8.2-3-5-06", "Systems Unable To Support Mfa",
         "Systems unable to support MFA shall be documented in the risk register with technical justification, compensating controls (e.g., network segmentation, enhanced monitoring, IP restriction), and CISO-approved risk acceptance reviewed annually."),
        ("A.8.2-3-5-07", "Implement Centralised Sso Via The",
         "The organisation shall implement centralised SSO via the identity provider using SAML 2.0 or OIDC with the following targets:."),
        ("A.8.2-3-5-08", "An Sso Integration Inventory",
         "An SSO integration inventory shall be maintained listing each application, its SSO status (integrated / in progress / exception), priority tier, and target date. The inventory shall be reviewed quarterly."),
        ("A.8.2-3-5-09", "Authentication Events",
         "All authentication events shall be logged and forwarded to the centralised logging system SIEM:."),
        ("A.8.2-3-5-10", "Authentication Logs",
         "Authentication logs shall be retained for a minimum of 12 months."),
        ("A.8.2-3-5-11", "Approved Geographic Locations*:",
         "Approved geographic locations*: Switzerland, [additional countries per business operations]. Logins from unapproved countries shall trigger alerts per table above."),
        ("A.8.2-3-5-12", "Alert Rules",
         "Alert rules shall be reviewed and tuned quarterly to reduce false positive rates. Investigation workflow: receive alert → validate (true/false positive) → enrich with context → escalate if confirmed → document outcome."),
        ("A.8.2-3-5-13", "The Main Access Authentication System",
         "The main access authentication system shall:."),
        ("A.8.2-3-5-14", "Validate The Log-On Information Only On",
         "Validate the log-on information only on completion of all input data. If an error condition arises, the system shall not indicate which part of the data is correct or incorrect."),
    ]),

    ("Privileged Access Management", [
        ("A.8.2-3-5-15", "Privileged Access",
         "Privileged access shall be restricted based on:."),
        ("A.8.2-3-5-16", "Implement Tiered Administration To Limit",
         "The organisation shall implement tiered administration to limit the impact of compromised credentials:."),
        ("A.8.2-3-5-17", "Tier 0 Accounts",
         "Tier 0 accounts shall never authenticate to Tier 1 or Tier 2 systems."),
        ("A.8.2-3-5-18", "Tier 1 Accounts",
         "Tier 1 accounts shall never authenticate to Tier 2 systems."),
        ("A.8.2-3-5-19", "Separate Credentials",
         "Separate credentials shall be used per tier (e.g., j.smith.t0, j.smith.t1)."),
        ("A.8.2-3-5-20", "Daily Work Activities (Email, Web",
         "Daily work activities (email, web browsing) shall not be performed on dedicated admin workstations."),
        ("A.8.2-3-5-21", "Technical Controls",
         "Technical controls shall enforce tier boundaries. The following are implementation options depending on the organisation's identity platform:."),
        ("A.8.2-3-5-22", "Phased Deployment*: Phase 1 (Year 1)",
         "Phased deployment*: Phase 1 (Year 1): Tier 0 PAWs deployed. Phase 2 (Year 2): Tier 1 PAWs deployed. Compensating controls shall be documented for any period where PAWs are not yet in place (e.g., enhanced monitoring, dedicated VMs, restricted admin accounts on standard workstations)."),
        ("A.8.2-3-5-23", "Deployment Status Tracking*: The Current",
         "Deployment status tracking*: The current deployment phase (planning, pilot, partial enforcement, full enforcement) shall be documented for each tier with compensating controls for non-enforced tiers and target completion dates."),
        ("A.8.2-3-5-24", "Privileged Accounts",
         "All privileged accounts shall be:."),
        ("A.8.2-3-5-25", "Implement Privileged Access Controls,",
         "The organisation shall implement privileged access controls, which may include a dedicated PAM solution PAM solution (see IAM Infrastructure table) or equivalent manual controls:."),
        ("A.8.2-3-5-26", "Compensating Controls",
         "Where a dedicated PAM solution is not yet deployed, compensating controls shall be documented (e.g., manual credential rotation, shared password manager with audit trail, alternative session logging via SIEM)."),
        ("A.8.2-3-5-27", "Be Rotated Immediately Upon Suspected Or",
         "All credentials shall be rotated immediately upon suspected or confirmed compromise, regardless of schedule."),
        ("A.8.2-3-5-28", "Service Accounts",
         "Service accounts shall be managed through a defined lifecycle:."),
        ("A.8.2-3-5-29", "Service Account Monitoring*: Siem Alert",
         "Service account monitoring*: SIEM alert rules shall detect interactive logon by service accounts, authentication from unexpected locations, and failed authentication attempts. A quarterly discovery scan shall identify undocumented service accounts."),
        ("A.8.2-3-5-30", "Quarterly Access Reviews",
         "Quarterly access reviews shall follow a structured campaign:."),
        ("A.8.2-3-5-31", "Maintain Emergency Access Procedures For",
         "The organisation shall maintain emergency access procedures for situations where normal authentication channels are unavailable:."),
        ("A.8.2-3-5-32", "Test Records",
         "Test records shall document the date, tester, successful authentication confirmation, and post-test credential rotation."),
    ]),

    ("Access Restriction", [
        ("A.8.2-3-5-33", "Access To Information And Other",
         "Access to information and other associated assets shall be restricted in accordance with this policy and the Identity and Access Management Policy:."),
        ("A.8.2-3-5-34", "System Sessions",
         "System sessions shall enforce the following timeout periods:."),
        ("A.8.2-3-5-35", "Network Segmentation",
         "Network segmentation shall separate trust zones to support access restriction (detailed in the Network Security Policy)."),
        ("A.8.2-3-5-36", "Firewall Rules",
         "Firewall rules shall enforce access boundaries between network segments."),
        ("A.8.2-3-5-37", "Network Access Control (Nac) Or",
         "Network access control (NAC) or equivalent shall verify endpoint compliance before granting access where feasible."),
        ("A.8.2-3-5-38", "The Organisation Masks Data In Line",
         "The organisation masks data in line with legal and regulatory obligations, including Swiss nFADP and GDPR requirements where applicable. Data masking shall be applied to:."),
        ("A.8.2-3-5-39", "Verify Access Controls Through",
         "The organisation shall verify access controls through:."),
    ]),

    ("Key Performance Indicators", [
        ("A.8.2-3-5-40", "The Following Metrics",
         "The following metrics shall be tracked to measure the effectiveness of authentication and privileged access controls:."),
        ("A.8.2-3-5-41", "Be Reported To The Ciso Quarterly",
         "Metrics shall be reported to the CISO quarterly. Metrics falling below target shall include a remediation plan with owner and target date."),
    ]),

])


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS
    ))


# =============================================================================
# QA_VERIFIED: 2026-02-08
# QA_STATUS: PASSED - AUTO-GENERATED (Phase 2 Operational Checklist)
# QA_TOOL: meta_generate_op_checklists.py
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.2-3-5
# =============================================================================
