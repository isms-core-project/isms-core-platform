#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.29 — Information Security During Disruption Compliance Checklist

Control A.5.29: Information Security During Disruption
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Minimum Security Baseline (3 reqs)
4. Tiered Security Posture (5 reqs)
5. BC DR Plan Security Reqs (8 reqs)
6. Recovery Site Security (3 reqs)
7. Emergency Access Procedures (3 reqs)
8. Personnel Availability (5 reqs)
9. Post-Disruption Sec Validation (5 reqs)

Total: 32 requirements across 7 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/A.0-checklist-engine/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_OP_ROOT / 'A.0-checklist-engine'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.5.29"
CONTROL_ID = "A.5.29"
CONTROL_NAME = "Information Security During Disruption"
SOURCE_POLICY = "ISMS-OP-POL-A.5.29"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.29
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Minimum Security Baseline", [
        ("A.5.29-01", "The Following Security Controls",
         "The following security controls shall be maintained at all times, regardless of the disruption state. These controls are not subject to relaxation or exception:."),
        ("A.5.29-02", "Mandatory Tracking*: Any Approved",
         "Mandatory tracking*: Any approved control degradation shall immediately create a time-bound entry in the Security Debt Register, including: owner, compensating controls in effect, start date, target closure date, and evidence of closure upon remediation."),
        ("A.5.29-03", "Emergency Changes",
         "Emergency changes shall not disable security controls from the 'Never Acceptable' list (logging, authentication, encryption, firewalls, change management itself)."),
    ]),

    ("Tiered Security Posture", [
        ("A.5.29-04", "Operate At One Of Five Defined",
         "The organisation shall operate at one of five defined security posture levels. The current posture level determines which controls are fully active, which may be degraded, and what additional measures are required."),
        ("A.5.29-05", "Transitions Between Posture Levels",
         "Transitions between posture levels shall be formally authorised. Verbal authorisation is permitted in urgent situations, followed by written confirmation within 4 hours."),
        ("A.5.29-06", "Be Recorded With: Date/Time, Authorising",
         "Each transition shall be recorded with: date/time, authorising person, justification, current state, target state, and any controls affected."),
        ("A.5.29-07", "Be Informed Of The Current Security",
         "All personnel shall be informed of the current security posture level and associated requirements."),
        ("A.5.29-08", "Communication Delivery",
         "Communication delivery shall be verified (email sent, intranet banner live, collaboration platform message posted). Non-receipt triggers escalation to alternative communication methods."),
    ]),

    ("BC DR Plan Security Reqs", [
        ("A.5.29-09", "Business Continuity And Disaster",
         "All business continuity and disaster recovery plans shall include security requirements reviewed and approved by the CISO. Security is not an afterthought in continuity planning — it is a design requirement."),
        ("A.5.29-10", "Bc/Dr Plans",
         "BC/DR plans shall address the following four areas:."),
        ("A.5.29-11", "Crisis Communication Participants",
         "All crisis communication participants shall authenticate using their organisational credentials."),
        ("A.5.29-12", "During Emergency Posture, If Mfa",
         "During Emergency posture, if MFA infrastructure is unavailable, participants shall use pre-shared authentication phrases to verify identity (rotated monthly, distributed via offline contact list)."),
        ("A.5.29-13", "The Ciso Or Designated Backup",
         "The CISO or designated backup shall review and approve the security sections of all BC/DR plans before the plans are approved."),
        ("A.5.29-14", "Security Review",
         "Security review shall occur after each update to a BC/DR plan."),
        ("A.5.29-15", "At Least One Security-Specific Test",
         "At least one security-specific test scenario shall be included in annual BC/DR testing."),
        ("A.5.29-16", "Security Deviations Observed During",
         "Security deviations observed during testing shall be documented and addressed within 30 days."),
    ]),

    ("Recovery Site Security", [
        ("A.5.29-17", "Recovery Sites — Whether Hot, Warm",
         "Recovery sites — whether hot, warm, cold standby, or cloud-based disaster recovery environments — shall maintain security controls equivalent to the primary site. A recovery environment with weaker security than the primary site creates an exploitable gap."),
        ("A.5.29-18", "Failover Testing*: Annual Failover Test",
         "Failover testing*: Annual failover test to recovery site. Security validation during test shall confirm authentication works (including MFA), network segmentation is enforced, logging is active and forwarding to [SIEM], encryption is verified, and access controls match primary site. Security findings documented and remediated within 30 days."),
        ("A.5.29-19", "Recovery Site Security",
         "Recovery site security shall be verified:."),
    ]),

    ("Emergency Access Procedures", [
        ("A.5.29-20", "Maintain Pre-Configured Emergency Access",
         "The organisation shall maintain pre-configured emergency access accounts ('break-glass accounts') for scenarios where normal authentication or access systems are unavailable."),
        ("A.5.29-21", "Break-Glass Accounts And Procedures",
         "Break-glass accounts and procedures shall be tested at least annually to verify:."),
        ("A.5.29-22", "Test Results",
         "Test results shall be documented. Failed tests shall trigger immediate remediation."),
    ]),

    ("Personnel Availability", [
        ("A.5.29-23", "Ensure That Personnel With Security",
         "The organisation shall ensure that personnel with security responsibilities are available during disruption events. Disruptions frequently occur outside business hours and may prevent normal access to the workplace."),
        ("A.5.29-24", "Key Security Roles",
         "Key security roles shall have designated backups documented in a succession plan."),
        ("A.5.29-25", "Contact Information For Security",
         "Contact information for security personnel shall be maintained offline — printed contact lists and/or encrypted USB — accessible when email, intranet, and other digital systems are unavailable."),
        ("A.5.29-26", "Cross-Training",
         "Cross-training shall ensure that at least two individuals can perform each critical security function (break-glass activation, log review, emergency access revocation, security posture assessment)."),
        ("A.5.29-27", "On-Call Rotation",
         "On-call rotation shall be established for 24/7 coverage when the organisation operates at Elevated, Degraded, or Emergency posture levels."),
    ]),

    ("Post-Disruption Sec Validation", [
        ("A.5.29-28", "Before Returning To Normal Posture Level",
         "Before returning to Normal posture level, the organisation shall validate that full security controls have been restored. The recovery-to-normal transition is not complete until security validation is signed off by the CISO."),
        ("A.5.29-29", "Security Relaxations Approved During A",
         "All security relaxations approved during a disruption shall be tracked in the Security Debt Register until fully remediated."),
        ("A.5.29-30", "Security Debt Older Than 30 Days",
         "Security debt older than 30 days shall be escalated to the CISO with a remediation plan and revised target date."),
        ("A.5.29-31", "Security Debt Older Than 90 Days",
         "Security debt older than 90 days shall be escalated to Executive Management for a decision: either approve accelerated remediation with additional resources, or formally accept the residual risk with documented risk acceptance."),
        ("A.5.29-32", "Security Debt That Cannot Be Remediated",
         "Security debt that cannot be remediated shall be converted to a permanent risk entry in the Risk Register with compensating controls and annual review."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.29
# =============================================================================
