#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.11 — Data Masking Compliance Checklist

Control A.8.11: Data Masking
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Data Class and Masking Reqs (2 reqs)
4. Approved Masking Techniques (9 reqs)
5. Environment Coverage Reqs (23 reqs)
6. Testing and Validation (3 reqs)
7. Logging and Monitoring (5 reqs)
8. Incident Response Masking (2 reqs)
9. Exception Management (1 reqs)
10. Optional Payment Card Data (4 reqs)
11. Third-Party Data Sharing Reqs (3 reqs)

Total: 52 requirements across 9 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.11"
CONTROL_ID = "A.8.11"
CONTROL_NAME = "Data Masking"
SOURCE_POLICY = "ISMS-OP-POL-A.8.11"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.11
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Data Class and Masking Reqs", [
        ("A.8.11-01", "Maintain An Inventory Of Sensitive Data",
         "The organisation shall maintain an inventory of sensitive data requiring masking, including:."),
        ("A.8.11-02", "Data Discovery",
         "Data discovery shall be automated for all environments containing Restricted or Confidential data, using [Data Discovery Tool] or equivalent. Automated discovery shall scan for known sensitive data patterns (PII patterns, credit card numbers, AHV/SSN formats, health identifiers) on at least a quarterly basis. Manual inventory is acceptable for organisations with limited data estates and no Restricted data, but shall be supplemented by automated discovery as the data estate grows."),
    ]),

    ("Approved Masking Techniques", [
        ("A.8.11-03", "The Following Factors",
         "When selecting a masking technique, the following factors shall be considered:."),
        ("A.8.11-04", "New Masking Techniques Or Significant",
         "New masking techniques or significant modifications to approved techniques shall be proposed to the Security Team, undergo security review and testing, and be approved by the CISO before use."),
        ("A.8.11-05", "Under Both Gdpr And Nfadp, Pseudonymised",
         "Under both GDPR and nFADP, pseudonymised data remains personal data because re-identification is possible with the separately held key. Anonymised data — where re-identification is no longer reasonably possible — falls outside the scope of data protection regulation. The organisation shall ensure the correct technique is applied based on whether the data must remain within data protection scope (pseudonymisation) or can be removed from scope entirely (anonymisation)."),
        ("A.8.11-06", "Anonymisation Data Utility Assessment*:",
         "Anonymisation data utility assessment*: Before applying anonymisation, the Data Owner shall assess whether the anonymised data retains sufficient business utility for its intended purpose. The assessment shall consider:."),
        ("A.8.11-07", "Pseudonymisation Keys",
         "Pseudonymisation keys shall be stored separately from the pseudonymised data, with the following separation requirements:."),
        ("A.8.11-08", "Physical Or Logical Separation: Keys",
         "Physical or logical separation: Keys shall be stored in a different system, database, or security domain from the pseudonymised data. Co-locating keys and data on the same server or in the same database is prohibited."),
        ("A.8.11-09", "Access Separation: Personnel With Access",
         "Access separation: Personnel with access to pseudonymised data shall not have access to re-identification keys unless specifically authorised for a documented purpose. Dual-control (two-person authorisation) shall be required for re-identification of Restricted data."),
        ("A.8.11-10", "Re-Identification Logging: All",
         "Re-identification logging: All re-identification events shall be logged with requestor identity, justification, data scope, and approval reference."),
        ("A.8.11-11", "Key Management",
         "Key management shall follow the Use of Cryptography Policy (A.8.24)."),
    ]),

    ("Environment Coverage Reqs", [
        ("A.8.11-12", "Sensitive Data",
         "Sensitive data shall be masked in environments where full data visibility is not required for legitimate business operations."),
        ("A.8.11-13", "Be Applied Before Data Leaves The",
         "SDM shall be applied BEFORE data leaves the production environment."),
        ("A.8.11-14", "Maintain Referential Integrity Across",
         "SDM shall maintain referential integrity across related tables. Where multi-table relationships exist, masking shall be applied consistently using the same masking key or mapping to preserve foreign key relationships, join integrity, and cross-table business rules. Referential integrity shall be validated through automated testing after each masking cycle."),
        ("A.8.11-15", "Preserve Data Format For Application",
         "SDM shall preserve data format for application compatibility. Note: format preservation may reduce the masking entropy (number of possible masked values), which increases re-identification risk. For Restricted data, the organisation shall assess whether format-preserving masking provides sufficient security or whether non-format-preserving techniques with application-layer adaptation are required."),
        ("A.8.11-16", "Masked Data",
         "Masked data shall be realistic enough for application testing."),
        ("A.8.11-17", "Masked Data Refresh: Non-Production",
         "Masked data refresh: Non-production environments using SDM shall be refreshed with newly masked data at a defined frequency — at minimum quarterly for active development environments and semi-annually for less active environments. Refresh frequency shall account for production data changes that may affect test validity and for reducing the risk of masking circumvention through accumulated knowledge of stale masked datasets."),
        ("A.8.11-18", "Be Enforced At The Database Or",
         "DDM shall be enforced at the database or application layer — not client-side."),
        ("A.8.11-19", "Ddm Rules",
         "DDM rules shall be based on documented user roles and least privilege."),
        ("A.8.11-20", "Not Be Bypassable By Users Without",
         "DDM shall not be bypassable by users without appropriate authorisation. Bypass prevention controls shall include:."),
        ("A.8.11-21", "Direct Database Access (Bypassing The",
         "Direct database access (bypassing the application layer) shall be restricted to authorised database administrators."),
        ("A.8.11-22", "Ddm Rules",
         "DDM rules shall be enforced at the database engine level where supported, not solely at the application layer."),
        ("A.8.11-23", "Attempts To Query Underlying Unmasked",
         "Attempts to query underlying unmasked data through views, stored procedures, or alternate access paths shall be blocked or logged and alerted."),
        ("A.8.11-24", "Periodic Testing",
         "Periodic testing shall verify that DDM cannot be circumvented through SQL injection, privilege escalation, or schema manipulation."),
        ("A.8.11-25", "Performance Impact",
         "Performance impact shall be assessed and kept within defined thresholds:."),
        ("A.8.11-26", "Query Latency: Ddm",
         "Query latency: DDM shall not add more than 15% latency to baseline query response times for standard queries."),
        ("A.8.11-27", "Throughput: Ddm",
         "Throughput: DDM shall not reduce database throughput by more than 10% under normal operating conditions."),
        ("A.8.11-28", "Baseline Measurement: Performance",
         "Baseline measurement: Performance baselines shall be established before DDM deployment and re-measured quarterly."),
        ("A.8.11-29", "Escalation: Where Ddm Exceeds",
         "Escalation: Where DDM exceeds performance thresholds, the Security Team shall evaluate alternative masking approaches (SDM pre-processing, application-layer masking, or DDM rule optimisation)."),
        ("A.8.11-30", "The Token Vault",
         "The token vault shall be secured with access controls and encryption. Vault encryption keys shall be:."),
        ("A.8.11-31", "Access-Controlled Separately From The",
         "Access-controlled separately from the tokenised data — vault administrators shall not have direct access to tokenised datasets, and vice versa."),
        ("A.8.11-32", "Be Format-Preserving Where Required",
         "Tokens shall be format-preserving where required (e.g., credit card format for PCI DSS)."),
        ("A.8.11-33", "De-Tokenisation",
         "De-tokenisation shall require explicit authorisation and be logged. De-tokenisation access shall be reviewed quarterly as part of privileged access reviews."),
        ("A.8.11-34", "Vault Key Management",
         "Vault key management shall follow the Use of Cryptography Policy (A.8.24)."),
    ]),

    ("Testing and Validation", [
        ("A.8.11-35", "Masking Implementations",
         "Masking implementations shall be tested before deployment and after any changes to masking configuration."),
        ("A.8.11-36", "Data Utility",
         "Where k-anonymity thresholds cannot be met, data utility shall be assessed against the risk of re-identification, and alternative techniques (generalisation, suppression, noise addition) shall be applied to achieve the target threshold."),
        ("A.8.11-37", "Be Corrected Before Production Use, Root",
         "When testing identifies failures, implementation shall be corrected before production use, root cause documented, and re-testing performed."),
    ]),

    ("Logging and Monitoring", [
        ("A.8.11-38", "The Following Masking-Related Events",
         "The following masking-related events shall be logged where technically feasible:."),
        ("A.8.11-39", "Masking Configuration Changes (Technique",
         "Masking configuration changes (technique changes, rule updates). Configuration changes shall follow the organisation's change management process: requested by authorised personnel, reviewed by the Security Team, tested in a non-production environment, approved by the Data Owner and Security Team Lead before production deployment, and logged with before/after configuration states."),
        ("A.8.11-40", "Monitor For Masking Process Failures,",
         "The organisation shall monitor for masking process failures, repeated bypass attempts, unauthorised configuration changes, and DDM performance degradation. Alerts shall be integrated with the organisation's security monitoring programme."),
        ("A.8.11-41", "Re-Identification Attempt Detection*:",
         "Re-identification attempt detection*: The organisation shall implement monitoring to detect potential re-identification attempts, including:."),
        ("A.8.11-42", "Detected Re-Identification Attempts",
         "Detected re-identification attempts shall be treated as High-severity security incidents and investigated immediately."),
    ]),

    ("Incident Response Masking", [
        ("A.8.11-43", "Data Exposure Incidents",
         "Data exposure incidents shall be assessed for breach notification requirements:."),
        ("A.8.11-44", "The Dpo And Legal/Compliance",
         "The DPO and Legal/Compliance shall be involved in all breach notification decisions."),
    ]),

    ("Exception Management", [
        ("A.8.11-45", "Active Exceptions",
         "Active exceptions shall be reviewed quarterly, revoked if business justification changes, and automatically expired at end of approved duration (no implicit renewal)."),
    ]),

    ("Optional Payment Card Data", [
        ("A.8.11-46", "Primary Account Numbers (Pans)",
         "Primary Account Numbers (PANs) shall be rendered unreadable anywhere they are stored, per PCI DSS Req. 3.4 (tokenisation, truncation, hashing, or strong encryption)."),
        ("A.8.11-47", "Show At Most The First Six",
         "When PANs are displayed, masking shall show at most the first six and last four digits, per PCI DSS Req. 3.5.1."),
        ("A.8.11-48", "Full Pans",
         "Full PANs shall not be present in non-production environments unless the non-production environment meets all applicable PCI DSS controls. SDM or tokenisation shall be applied before data leaves the cardholder data environment."),
        ("A.8.11-49", "Non-Production Use Of Payment Card Data",
         "Non-production use of payment card data shall be governed by a documented data usage policy per PCI DSS Req. 12.3."),
    ]),

    ("Third-Party Data Sharing Reqs", [
        ("A.8.11-50", "Contractual Requirements: Data Sharing",
         "Contractual requirements: Data sharing agreements shall specify:."),
        ("A.8.11-51", "Risk Assessment: A Data Sharing Risk",
         "Risk assessment: A data sharing risk assessment shall be performed before initial sharing, evaluating re-identification risk, the third party's data handling maturity, and regulatory implications."),
        ("A.8.11-52", "Ongoing Monitoring: Data Sharing",
         "Ongoing monitoring: Data sharing arrangements shall be reviewed annually and upon material changes to the third party's environment or the shared data scope."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.11
# =============================================================================
