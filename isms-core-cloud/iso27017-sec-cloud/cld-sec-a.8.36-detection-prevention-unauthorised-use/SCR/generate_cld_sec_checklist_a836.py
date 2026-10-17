#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-SEC-CHK-A.8.36 — Detection and Prevention of Unauthorized Use of Cloud Services Compliance Checklist

Control 8.36: CLD - Detection and prevention of unauthorized use of cloud services
Product: ISMS CORE Cloud Sec (ISO/IEC 27017:2026, Clause 8.36)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. CSC Obligations — 4 reqs
4. CSP Obligations — 4 reqs

Total: 8 requirements across 2 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 51-isms-core-privacy/00-checklist-engine/priv_checklist_engine.py
_REPO_ROOT = Path(__file__).resolve().parents[4]
# The privacy product folder is '51-isms-core-privacy' in the development tree and 'isms-core-privacy' in the published repository.
_ENGINE_DIR = next(p / '00-checklist-engine' for p in (_REPO_ROOT / 'isms-core-privacy', _REPO_ROOT / '51-isms-core-privacy') if (p / '00-checklist-engine').is_dir())
sys.path.insert(0, str(_ENGINE_DIR))
from priv_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "CLD-SEC-CHK-A.8.36"
CONTROL_ID = "8.36"
CONTROL_NAME = "Detection and Prevention of Unauthorized Use of Cloud Services"
SOURCE_POLICY = "CLD-SEC-POL-A.8.36"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-SEC-POL-A.8.36
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("CSC Obligations", [
        ("8.36-01", "CSU Activity Monitoring",
         "The organisation shall implement monitoring of cloud service users' (CSUs') activities across the cloud services it uses, mandatory for Confidential or Restricted data classifications."),
        ("8.36-02", "Periodic Technical Compliance Review",
         "The organisation shall periodically review CSU activity against its information security policy, its topic-specific policy on the use of cloud services, and relevant rules and standards."),
        ("8.36-03", "Prevent Unintended Information Transfer",
         "The organisation shall monitor and prevent unintended or unauthorized information transfer to and from the cloud service environment it manages."),
        ("8.36-04", "Anomaly Detection",
         "The organisation shall detect anomalies — such as increasing resource utilization or unknown service usage — by identifying deviations from established normal-use patterns."),
    ]),

    ("CSP Obligations", [
        ("8.36-05", "Provide CSC-Facing Monitoring Guidance and Functions",
         "The organisation shall provide CSCs with guidance and functions enabling them to monitor and control their CSUs' use of the cloud service the organisation delivers."),
        ("8.36-06", "Risk-Based Scoping Decision and Approval",
         "For cloud services processing only Public or Internal data where monitoring is not implemented, the organisation shall document a risk-based decision approved by the CISO."),
        ("8.36-07", "Monitoring Scope Documentation",
         "The organisation shall document the monitoring scope and mechanisms in place per cloud service, keeping the documentation current as the service evolves."),
        ("8.36-08", "Escalation of Confirmed Unauthorized Use",
         "The organisation shall record and escalate every confirmed instance of unauthorized cloud service use identified through monitoring, with disposition tracked in the Anomaly Detection Log."),
    ]),
])


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 27017:2026"
    ))


# =============================================================================
# QA_VERIFIED: 2026-10-17
# QA_STATUS: PASSED
# QA_TOOL: Claude Code — qa/scr_generators/cloud_generators_regression.py (workbook cells identical before and after the edit)
# CHANGES: 2026-10-17 engine lookup works in the development and the published layout (generator content unchanged); 2026-08-01: Initial generation for Cloud Sec product launch
# =============================================================================
