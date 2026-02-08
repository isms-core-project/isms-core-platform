#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.5-6 — Contact with Authorities and Special Interest Groups Compliance Checklist

Controls A.5.5-6: Contact with Authorities and Special Interest Groups
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Authority Contact Register (7 reqs)
4. Mandatory Notifications (5 reqs)
5. Customer and Stakeholder Comms (1 reqs)
6. Authorised Spokespersons (6 reqs)
7. Special Interest Group (3 reqs)
8. Information Sharing Protocols (5 reqs)
9. Testing and Exercising (2 reqs)
10. Compliance Measurement (3 reqs)

Total: 32 requirements across 8 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.5.5-6"
CONTROL_ID = "A.5.5-6"
CONTROL_NAME = "Contact with Authorities and Special Interest Groups"
SOURCE_POLICY = "ISMS-OP-POL-A.5.5-6"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.5-6
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Authority Contact Register", [
        ("A.5.5-6-01", "[Organisation]",
         "[Organisation] shall maintain active, verified contacts with the following authorities:."),
        ("A.5.5-6-02", "The Authority Contact Register",
         "The authority contact register shall be:."),
        ("A.5.5-6-03", "Verified Quarterly — The Ciso Or",
         "Verified quarterly — the CISO or delegate shall confirm that all contact details remain current, contact persons are still in their roles, and communication channels are operational."),
        ("A.5.5-6-04", "Available Offline — A Printed Or",
         "Available offline — a printed or locally stored copy of critical contacts (NCSC, FDPIC, cantonal police, emergency services) shall be maintained for use during incidents when primary systems may be unavailable."),
        ("A.5.5-6-05", "Access-Restricted To Authorised",
         "Access-restricted to authorised personnel only. The register may contain personal contact details of authority liaison officers and shall be classified as Internal."),
        ("A.5.5-6-06", "Changes To The Authority Contact",
         "Changes to the authority contact register shall follow documented change control:."),
        ("A.5.5-6-07", "Version Control*: Contact Registry",
         "Version control*: Contact registry shall use date-based versioning (YYYY-MM-DD format) and retain all historical versions for audit trail."),
    ]),

    ("Mandatory Notifications", [
        ("A.5.5-6-08", "Nfadp Art. 24 Does Not Stipulate",
         "nFADP Art. 24 does not stipulate a fixed notification deadline but requires reporting 'as soon as possible'. The FDPIC has published guidelines clarifying that this means without undue delay once the controller becomes aware of the breach. [Organisation] shall target notification within 72 hours as an internal standard to demonstrate diligence, even though Swiss law does not mandate this specific timeframe."),
        ("A.5.5-6-09", "Swiss Isg (Information Security Act):",
         "Swiss ISG (Information Security Act): Since 1 April 2025, operators of critical infrastructure must report cyberattacks to the NCSC within 24 hours of discovery. Failure to report may result in fines up to CHF 100,000 (penalties in force since 1 October 2025). [Organisation] shall assess whether it falls within the ISG's definition of critical infrastructure and comply accordingly."),
        ("A.5.5-6-10", "Fdpic Breach Reporting Portal:",
         "FDPIC breach reporting portal: Notifications shall be submitted via the FDPIC's dedicated portal at databreach.edoeb.admin.ch/report."),
        ("A.5.5-6-11", "Processor Obligations: Where",
         "Processor obligations: Where [Organisation] acts as a data processor, it shall notify the data controller as soon as possible of any data security breach, in addition to its own notification obligations."),
        ("A.5.5-6-12", "A Data Breach That Also Constitutes",
         "Where an event triggers multiple notification obligations (e.g., a data breach that also constitutes a cyber incident), each obligation shall be addressed independently but coordinated to ensure consistent messaging."),
    ]),

    ("Customer and Stakeholder Comms", [
        ("A.5.5-6-13", "Systems, Or Service Availability,",
         "When a security incident affects customer data, systems, or service availability, [Organisation] shall communicate with affected customers according to:."),
    ]),

    ("Authorised Spokespersons", [
        ("A.5.5-6-14", "No Employee",
         "No employee shall contact authorities regarding [Organisation]'s security matters without prior authorisation from the CISO or Legal Counsel, except for immediate life-safety emergencies."),
        ("A.5.5-6-15", "Authority Communications",
         "All authority communications shall be documented — a record of date, time, authority contacted, contact person, subject, content summary, and any commitments made shall be maintained in the communication log."),
        ("A.5.5-6-16", "Legal Counsel",
         "Legal Counsel shall review all communications involving potential legal liability, regulatory filings, or responses to formal authority requests before submission."),
        ("A.5.5-6-17", "Classified Or Confidential Information",
         "Classified or confidential information requires explicit CISO and Legal Counsel approval before disclosure to any authority, even where a notification obligation exists. Disclosure shall be limited to the minimum information necessary to fulfil the obligation."),
        ("A.5.5-6-18", "Verbal Communications With Authorities",
         "Verbal communications with authorities shall be followed up with a written summary within 24 hours, stored in the communication log."),
        ("A.5.5-6-19", "Route To The Appropriate Spokesperson —",
         "Route to the appropriate spokesperson — the recipient shall forward the inquiry to the CISO and Legal Counsel without providing any substantive response."),
    ]),

    ("Special Interest Group", [
        ("A.5.5-6-20", "[Organisation]",
         "[Organisation] shall maintain active participation in relevant security communities to receive threat intelligence, access best practices, and contribute to collective security improvement."),
        ("A.5.5-6-21", "The Ciso",
         "The CISO shall determine which groups are relevant based on [Organisation]'s industry sector, technology stack, threat landscape, and regulatory environment. The selection shall be reviewed annually."),
        ("A.5.5-6-22", "The Ciso",
         "The CISO shall maintain a register of all special interest group memberships and subscriptions, recording:."),
    ]),

    ("Information Sharing Protocols", [
        ("A.5.5-6-23", "Information Sharing With External",
         "All information sharing with external parties — authorities, special interest groups, and peer organisations — shall use the Traffic Light Protocol (TLP) version 2.0, as defined by FIRST, to classify and control distribution."),
        ("A.5.5-6-24", "Pre-Disclosure Review — All Information",
         "Pre-disclosure review — All information proposed for external sharing shall be reviewed by the CISO (and Legal Counsel where the information involves personal data, contractual obligations, or potential legal liability) to confirm:."),
        ("A.5.5-6-25", "Anonymisation — Incident Data Shared",
         "Anonymisation — Incident data shared with external groups shall be anonymised to remove identifying details of [Organisation], its clients, and affected individuals, unless disclosure is required by law or authorised by the data subjects."),
        ("A.5.5-6-26", "Receiving Intelligence — Information",
         "Receiving intelligence — Information received from external groups shall be handled according to its TLP classification. TLP:RED and TLP:AMBER information shall not be forwarded outside the designated recipients without the originator's explicit consent."),
        ("A.5.5-6-27", "Record Keeping — A Log Of",
         "Record keeping — A log of all information shared externally (excluding routine advisory receipt) shall be maintained, recording: date, recipient group, TLP classification, subject, and approving authority."),
    ]),

    ("Testing and Exercising", [
        ("A.5.5-6-28", "Beyond Quarterly Contact Verification,",
         "Beyond quarterly contact verification, [Organisation] shall conduct:."),
        ("A.5.5-6-29", "Annual Tabletop Exercise",
         "Annual tabletop exercise shall include:."),
    ]),

    ("Compliance Measurement", [
        ("A.5.5-6-30", "The Following Metrics",
         "The following metrics shall be tracked and reported to the CISO quarterly:."),
        ("A.5.5-6-31", "In Addition To Governance Metrics, The",
         "In addition to governance metrics, the following operational metrics shall be tracked:."),
        ("A.5.5-6-32", "Metrics Breaching Red Thresholds",
         "Metrics breaching red thresholds shall be escalated to the CISO for immediate attention and reported at the next Management Review."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.5-6
# =============================================================================
