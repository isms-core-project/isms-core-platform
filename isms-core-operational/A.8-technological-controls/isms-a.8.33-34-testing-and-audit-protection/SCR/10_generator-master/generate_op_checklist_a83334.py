#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.33-34 — Test Information and Audit Testing Protection Compliance Checklist

Controls A.8.33-34: Test Information and Audit Testing Protection
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Test Data Selection (4 reqs)
4. Test Data Protection (10 reqs)
5. Test Data Lifecycle (12 reqs)
6. Audit Planning and Governance (7 reqs)
7. Auditor Access Control (4 reqs)
8. Penetration Testing Controls (12 reqs)
9. Audit Tool Management (3 reqs)
10. Audit Log Protection (6 reqs)
11. Incident Handling During Audit (7 reqs)

Total: 65 requirements across 9 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.33-34"
CONTROL_ID = "A.8.33-34"
CONTROL_NAME = "Test Information and Audit Testing Protection"
SOURCE_POLICY = "ISMS-OP-POL-A.8.33-34"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.33-34
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Test Data Selection", [
        ("A.8.33-34-01", "Establish A Clear Hierarchy Of",
         "The organisation shall establish a clear hierarchy of preference for test data sources."),
        ("A.8.33-34-02", "Direct Production Copies",
         "Direct production copies shall only be permitted where all other options are demonstrably inadequate, with documented justification, time-limited approval (maximum 30 days), enhanced access controls, and mandatory deletion upon completion."),
        ("A.8.33-34-03", "The Data Owner And Information Security",
         "Where a decision results in Priority 3 or higher, the Data Owner and Information Security Manager shall be consulted before proceeding."),
        ("A.8.33-34-04", "Test Data Classification*: Test Data",
         "Test Data Classification*: Test data shall be classified according to the organisation's information classification scheme. Production-derived test data inherits the classification of the source data until masking or anonymisation is validated. Synthetic data shall be classified based on business context (typically Internal). Classification determines the protection controls required."),
    ]),

    ("Test Data Protection", [
        ("A.8.33-34-05", "The Organisation",
         "When production data is required for testing, the organisation shall apply data protection techniques before the data is accessible in any test environment."),
        ("A.8.33-34-06", "Render Re-Identification Not Reasonably",
         "Anonymisation shall render re-identification not reasonably possible, considering available means of re-identification, cost of re-identification, and intended purpose."),
        ("A.8.33-34-07", "Anonymisation Techniques",
         "Anonymisation techniques shall be validated before use and reviewed annually for continued effectiveness, accounting for advances in re-identification techniques including AI-assisted methods."),
        ("A.8.33-34-08", "Pseudonymised Data Remains Personal Data",
         "Pseudonymised data remains personal data and shall be protected accordingly."),
        ("A.8.33-34-09", "The Mapping Key (Pseudonym-To-Identity)",
         "The mapping key (pseudonym-to-identity) shall be stored separately from the pseudonymised dataset, with access restricted to authorised personnel."),
        ("A.8.33-34-10", "Pseudonymised Test Data",
         "Pseudonymised test data shall be subject to the same access controls as the original data classification."),
        ("A.8.33-34-11", "Data Masking",
         "Data masking shall be applied using [Data Masking Tool] (e.g., Informatica, Delphix, IBM InfoSphere Optim, or equivalent) or approved scripted methods."),
        ("A.8.33-34-12", "Masking Validation*: Masked Data",
         "Masking Validation*: Masked data shall be validated before release to test environments to confirm that original sensitive values are not recoverable, data format is preserved for application compatibility, referential integrity is maintained across related datasets, and no plaintext personal data exists in the masked output. Validation results shall be documented and approved by the Information Security Manager."),
        ("A.8.33-34-13", "Be Generated To Preserve The Statistical",
         "Where synthetic data is used, it shall be generated to preserve the statistical properties, data distributions, and referential integrity required for effective testing without containing any real personal or business data."),
        ("A.8.33-34-14", "Synthetic Data Generators",
         "Synthetic data generators shall be documented, version-controlled, and reviewed periodically to ensure generated data remains fit for purpose. The organisation shall maintain records of synthetic data generation parameters and validation results."),
    ]),

    ("Test Data Lifecycle", [
        ("A.8.33-34-15", "Test Data Creation Or Refresh",
         "Test data creation or refresh shall be requested through a documented process."),
        ("A.8.33-34-16", "Masking Or Anonymisation",
         "Masking or anonymisation shall be applied before data is accessible in the test environment (not after)."),
        ("A.8.33-34-17", "Data Provisioning Activities",
         "All data provisioning activities shall be logged for audit purposes."),
        ("A.8.33-34-18", "Test Data",
         "Test data containing masked or pseudonymised production data shall be retained only for the duration of the testing requirement. Upon project completion, test data shall be deleted within 30 days."),
        ("A.8.33-34-19", "Test Data",
         "Test data shall be reviewed quarterly for continued need."),
        ("A.8.33-34-20", "Data Older Than 90 Days Without",
         "Data older than 90 days without documented active usage shall be flagged for deletion."),
        ("A.8.33-34-21", "Automated Retention Monitoring",
         "Automated retention monitoring shall alert when data exceeds thresholds."),
        ("A.8.33-34-22", "Disposal*: Test Data Disposal",
         "Disposal*: Test data disposal shall follow the same secure deletion procedures as production data of equivalent classification. Disposal shall be verified and documented."),
        ("A.8.33-34-23", "Fresh Masking",
         "Fresh masking shall be applied to each refresh cycle (prior masking does not carry over)."),
        ("A.8.33-34-24", "Refresh Procedures",
         "Refresh procedures shall be documented and approved by the Data Owner."),
        ("A.8.33-34-25", "Refresh Activities",
         "Refresh activities shall be logged, including source system, volume, masking method, and operator."),
        ("A.8.33-34-26", "Previous Test Data",
         "Previous test data shall be securely deleted before or immediately after refresh completion."),
    ]),

    ("Audit Planning and Governance", [
        ("A.8.33-34-27", "Before Any Audit Testing Commences, The",
         "Before any audit testing commences, the organisation shall establish formal agreement between the tester and appropriate management covering:."),
        ("A.8.33-34-28", "Pre-Audit Agreements",
         "Pre-audit agreements shall be documented, signed by both parties, and retained as evidence."),
        ("A.8.33-34-29", "Audit Testing Activities",
         "Audit testing activities shall be scheduled to minimise operational impact:."),
        ("A.8.33-34-30", "Critical Business Periods (E.G.,",
         "Critical business periods (e.g., month-end close, peak trading, system maintenance windows) shall be avoided unless specifically testing resilience during those periods."),
        ("A.8.33-34-31", "Testing Windows",
         "Testing windows shall be coordinated with IT Operations and relevant system owners."),
        ("A.8.33-34-32", "Affected Stakeholders",
         "Affected stakeholders shall be notified of planned testing activities, including timing, scope, and potential impact."),
        ("A.8.33-34-33", "Emergency Or Unscheduled Testing",
         "Emergency or unscheduled testing shall follow an expedited approval process with post-facto review within 48 hours."),
    ]),

    ("Auditor Access Control", [
        ("A.8.33-34-34", "Access Granted To Auditors, Assessors,",
         "Access granted to auditors, assessors, and penetration testers shall follow the principle of least privilege."),
        ("A.8.33-34-35", "An Administrator With The Necessary",
         "Where read-only access is not feasible, an administrator with the necessary access rights shall perform system or data access on behalf of the auditor, with the auditor observing and directing."),
        ("A.8.33-34-36", "Device Security*: Before Granting",
         "Device Security*: Before granting access, the organisation shall verify that auditor devices meet minimum security requirements, including current operating system patches, active endpoint protection, full disk encryption, and no known malware. Auditors using non-compliant devices shall be provided with organisation-managed devices or virtual desktop access."),
        ("A.8.33-34-37", "Access Deprovisioning*: Auditor Access",
         "Access Deprovisioning*: Auditor access shall be revoked within 24 hours of audit completion or the agreed access expiration date, whichever is earlier. Deprovisioning shall be verified and documented."),
    ]),

    ("Penetration Testing Controls", [
        ("A.8.33-34-38", "Penetration Testing And Active Security",
         "Penetration testing and active security testing shall be authorised in writing by the CISO (or delegate) and relevant system owners before testing begins."),
        ("A.8.33-34-39", "Rules Of Engagement*",
         "Rules of Engagement* shall document:."),
        ("A.8.33-34-40", "It Operations",
         "IT Operations shall be on standby with the ability to intervene if operational systems are affected."),
        ("A.8.33-34-41", "Be Conducted In Isolated Or",
         "Testing shall be conducted in isolated or non-production environments where possible."),
        ("A.8.33-34-42", "Rollback And Recovery Procedures",
         "Where production testing is required, rollback and recovery procedures shall be prepared in advance."),
        ("A.8.33-34-43", "Be Suspended Immediately If Unintended",
         "Testing shall be suspended immediately if unintended operational impact occurs, and shall not resume without explicit approval from the IT Operations Manager and CISO."),
        ("A.8.33-34-44", "Critical Vulnerabilities Discovered",
         "Critical vulnerabilities discovered during testing shall be reported to the Security Team immediately (not deferred to the final report)."),
        ("A.8.33-34-45", "Be Handled Per The Organisation'S",
         "Vulnerabilities shall be handled per the organisation's vulnerability management process (A.8.8)."),
        ("A.8.33-34-46", "Not Exploit Vulnerabilities Beyond The",
         "Testers shall not exploit vulnerabilities beyond the scope necessary for verification and risk assessment."),
        ("A.8.33-34-47", "Penetration Testing Reports",
         "Penetration testing reports shall be classified as Confidential and distributed only to authorised recipients."),
        ("A.8.33-34-48", "During Active Penetration Testing Or",
         "During active penetration testing or extended audit engagements, the tester shall provide daily status updates to the designated organisational contact. Status updates shall include:."),
        ("A.8.33-34-49", "Critical Findings",
         "Critical findings shall be reported immediately by phone to the CISO, in addition to any daily status update. The format and frequency of status reporting shall be agreed in the pre-audit agreement."),
    ]),

    ("Audit Tool Management", [
        ("A.8.33-34-50", "Audit And Testing Tools Used To",
         "Audit and testing tools used to assess the organisation's systems shall be:."),
        ("A.8.33-34-51", "Audit Tools",
         "Audit tools shall not be installed on production systems without explicit CISO approval. Where possible, audit tools shall be run from dedicated audit workstations or isolated virtual environments."),
        ("A.8.33-34-52", "Audit Tools, Scripts, And Configuration",
         "Audit tools, scripts, and configuration files shall be protected from unauthorised access both during and after the engagement. Tools capable of exploiting vulnerabilities or bypassing security controls shall be removed from organisational systems upon audit completion."),
    ]),

    ("Audit Log Protection", [
        ("A.8.33-34-53", "Logs Generated During Audit And Testing",
         "Logs generated during audit and testing activities shall be protected from unauthorised modification or deletion to maintain the integrity of the audit trail."),
        ("A.8.33-34-54", "Audit Logs",
         "Audit logs shall be written to tamper-evident storage (e.g., write-once media, SIEM with integrity controls, or equivalent)."),
        ("A.8.33-34-55", "Capture: Timestamp (Utc), User Identity,",
         "Logs shall capture: timestamp (UTC), user identity, source IP, action performed, system affected, and outcome (success/failure)."),
        ("A.8.33-34-56", "Logs Generated During Audit Testing",
         "Logs generated during audit testing shall be retained per the organisation's log retention policy (minimum 1 year for access events, 3 years for security events)."),
        ("A.8.33-34-57", "Be Available For Review If Audit",
         "Logs shall be available for review if audit findings are disputed or require clarification."),
        ("A.8.33-34-58", "During Active Penetration Testing,",
         "During active penetration testing, enhanced monitoring shall be enabled to distinguish authorised testing activity from genuine security events."),
    ]),

    ("Incident Handling During Audit", [
        ("A.8.33-34-59", "Immediate Suspension: Testing",
         "Immediate suspension: Testing shall cease immediately upon detection of unintended impact."),
        ("A.8.33-34-60", "Notification: It Operations",
         "Notification: IT Operations shall be notified for containment and recovery."),
        ("A.8.33-34-61", "Root Cause Analysis: The Cause Of",
         "Root cause analysis: The cause of the unintended impact shall be documented."),
        ("A.8.33-34-62", "Remediation: Affected Systems",
         "Remediation: Affected systems shall be restored to normal operation."),
        ("A.8.33-34-63", "Resumption Approval: Testing",
         "Resumption approval: Testing shall not resume without explicit approval from the IT Operations Manager."),
        ("A.8.33-34-64", "Lessons Learned: Incident",
         "Lessons learned: Incident shall be documented and incorporated into future pre-audit planning."),
        ("A.8.33-34-65", "Genuine Security Incidents Discovered",
         "Genuine security incidents discovered during audit testing (e.g., evidence of prior compromise, active threats) shall be escalated immediately per the organisation's incident management process (A.5.24-28)."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.33-34
# =============================================================================
