#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.8 — Information Security in Project Management Compliance Checklist

Control A.5.8: Information Security in Project Management
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Project Classification (6 reqs)
4. Security Reqs Identification (4 reqs)
5. Phase Gate Security Reviews (3 reqs)
6. Sec Testing by Classification (3 reqs)
7. Sec Handover and Acceptance (4 reqs)
8. Project Security Roles (1 reqs)
9. DPIA Integration (3 reqs)
10. Agile & Iterative Project (2 reqs)
11. Procurement Project Security (5 reqs)
12. Compliance Measurement (4 reqs)

Total: 35 requirements across 10 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/A.0-checklist-engine/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(_OP_ROOT / 'A.0-checklist-engine'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.5.8"
CONTROL_ID = "A.5.8"
CONTROL_NAME = "Information Security in Project Management"
SOURCE_POLICY = "ISMS-OP-POL-A.5.8"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.8
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Project Classification", [
        ("A.5.8-01", "Be Classified By Information Security",
         "All projects shall be classified by information security risk to determine proportional security requirements. Classification shall occur at project initiation and be documented in the project charter or equivalent initiation document."),
        ("A.5.8-02", "Be Classified Based On The Highest",
         "Projects shall be classified based on the highest applicable factor across the following dimensions:."),
        ("A.5.8-03", "Classification Rule: If Any Single",
         "Classification rule: If any single factor meets the High Risk criteria, the project shall be classified as High Risk. If any factor meets Medium Risk (and no factor is High Risk), classify as Medium Risk. Only if all factors are Low Risk shall the project be classified as Low Risk*."),
        ("A.5.8-04", "Be Reviewed At Each Phase Gate",
         "Classification shall be reviewed at each phase gate. If project scope, data sensitivity, or external exposure changes materially, the classification shall be updated and re-approved."),
        ("A.5.8-05", "Project Managers",
         "Project managers shall estimate security costs based on project classification when preparing project budgets:."),
        ("A.5.8-06", "Security Budget Estimates",
         "Security budget estimates shall be included in the project initiation documentation and approved as part of the project budget. Where actual security costs are expected to exceed the estimated range, the Project Manager shall notify the Information Security Officer and adjust the project budget accordingly."),
    ]),

    ("Security Reqs Identification", [
        ("A.5.8-07", "Security Requirements For Project",
         "Security requirements for project deliverables shall be identified systematically during the planning phase based on the project's classification and the categories of assets and data involved."),
        ("A.5.8-08", "The Project Manager, With Information",
         "The Project Manager, with Information Security Officer support, shall assess each of the following requirement categories against project scope:."),
        ("A.5.8-09", "High And Medium Risk Projects: Security",
         "High and Medium Risk projects: Security requirements shall be documented in a Security Requirements Register (or equivalent section in [Project Management Tool]) and tracked through to implementation and testing."),
        ("A.5.8-10", "Low Risk Projects: Security Requirements",
         "Low Risk projects: Security requirements shall be documented as risk mitigation items in the project risk register with confirmation of applicable policy compliance."),
    ]),

    ("Phase Gate Security Reviews", [
        ("A.5.8-11", "Security Reviews",
         "Security reviews shall be integrated into project governance at the following phase gates. Projects shall not proceed to the next phase until security criteria for the current phase gate are satisfied or formally accepted by the appropriate authority."),
        ("A.5.8-12", "Security Concerns At Phase Gates",
         "Security concerns at phase gates shall be escalated within:."),
        ("A.5.8-13", "Not Proceed To The Next Phase",
         "Projects shall not proceed to the next phase without resolving Critical security concerns. High security concerns may proceed with formal risk acceptance from the appropriate authority. Medium and Low concerns may proceed with a documented mitigation plan."),
    ]),

    ("Sec Testing by Classification", [
        ("A.5.8-14", "Include Security Testing Proportional To",
         "All projects shall include security testing proportional to their classification level. Testing shall be completed before deployment and the results documented."),
        ("A.5.8-15", "Residual Risk",
         "If remediation targets cannot be achieved before the deployment deadline, residual risk shall be formally accepted per the Exception Management section of this policy."),
        ("A.5.8-16", "Testing Evidence (Scan Reports,",
         "Testing evidence (scan reports, penetration test reports, code review findings) shall be archived per records management requirements."),
    ]),

    ("Sec Handover and Acceptance", [
        ("A.5.8-17", "At Project Closure, Security Handover",
         "At project closure, security handover documentation shall be provided to the operational team and validated as complete before the project is formally closed. Incomplete security handover blocks project closure."),
        ("A.5.8-18", "The Security Handover Package",
         "The security handover package shall include:."),
        ("A.5.8-19", "The Operational Owner",
         "The operational owner shall confirm handover completeness via a signed Security Handover Checklist before the Project Manager requests project closure authorisation. For High Risk projects, the CISO shall additionally approve the handover."),
        ("A.5.8-20", "Upon Handover Acceptance, The Project",
         "Upon handover acceptance, the Project Manager shall ensure:."),
    ]),

    ("Project Security Roles", [
        ("A.5.8-21", "The Information Security Officer",
         "The Information Security Officer shall coordinate the Security Champion programme, including selection criteria, training content, and ongoing support."),
    ]),

    ("DPIA Integration", [
        ("A.5.8-22", "A Data Protection Impact Assessment",
         "Where a project involves the processing of personal data, a Data Protection Impact Assessment (DPIA) screening shall be performed at project initiation to determine whether a full DPIA is required."),
        ("A.5.8-23", "A Dpia Screening",
         "A DPIA screening shall be completed for every project that processes personal data. The screening shall assess whether the planned processing is likely to result in high risk to individuals' personality or fundamental rights, as required by Swiss nFADP Art. 22."),
        ("A.5.8-24", "The Completed Dpia",
         "The completed DPIA shall be reviewed by the Data Protection Officer (or CISO where no DPO is appointed) and approved before the project proceeds to execution. Where the DPIA identifies residual high risks that cannot be mitigated, the organisation shall consult the Federal Data Protection and Information Commissioner (FDPIC) before proceeding, as required by nFADP Art. 23."),
    ]),

    ("Agile & Iterative Project", [
        ("A.5.8-25", "For Projects Using Agile, Scrum, Or",
         "For projects using Agile, Scrum, or other iterative methodologies, security shall be integrated into the iterative process rather than deferred to the end."),
        ("A.5.8-26", "Rather Than Single Phase Gates,",
         "Rather than single phase gates, iterative projects shall implement security checkpoints at the following points:."),
    ]),

    ("Procurement Project Security", [
        ("A.5.8-27", "Projects Involving Procurement Of It",
         "Projects involving procurement of IT systems, software, or services shall include information security requirements in the procurement process."),
        ("A.5.8-28", "Vendor Security Assessment: Vendors",
         "Vendor security assessment: Vendors shall be assessed against the organisation's supplier security requirements (per the Supplier Relationship Security Policy) before contract award."),
        ("A.5.8-29", "Security Requirements In Contracts:",
         "Security requirements in contracts: Contracts shall include information security requirements, including data protection obligations, incident notification requirements, audit rights, and subcontractor controls."),
        ("A.5.8-30", "Security Acceptance Criteria:",
         "Security acceptance criteria: Procurement acceptance criteria shall include security validation (e.g., vulnerability scan of delivered system, security configuration review, access control verification)."),
        ("A.5.8-31", "Data Processing Agreements: Where The",
         "Data processing agreements: Where the vendor processes personal data on behalf of the organisation, a data processing agreement compliant with nFADP Art. 9 (and GDPR Art. 28 where applicable) shall be executed before data processing begins."),
    ]),

    ("Compliance Measurement", [
        ("A.5.8-32", "The Following Metrics",
         "The following metrics shall be tracked and reported to the CISO quarterly:."),
        ("A.5.8-33", "The Ciso",
         "The CISO shall maintain a project security metrics dashboard providing at-a-glance programme health visibility. The dashboard shall include:."),
        ("A.5.8-34", "The Dashboard",
         "The dashboard shall be reviewed at the monthly CISO review and included in the quarterly Executive Management report to provide clear visibility of project security programme effectiveness."),
        ("A.5.8-35", "Metrics Breaching Red Thresholds",
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.8
# =============================================================================
