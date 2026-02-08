#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.30-8.13-14 — Business Continuity and Disaster Recovery Compliance Checklist

Controls A.5.30-8.13-14: Business Continuity and Disaster Recovery
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Business Impact Analysis (6 reqs)
4. Information Backup (29 reqs)
5. Redundancy Info Process (9 reqs)
6. ICT Continuity Planning (18 reqs)
7. BC DR Metrics and Reporting (2 reqs)

Total: 64 requirements across 5 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.5.30-8.13-14"
CONTROL_ID = "A.5.30-8.13-14"
CONTROL_NAME = "Business Continuity and Disaster Recovery"
SOURCE_POLICY = "ISMS-OP-POL-A.5.30-8.13-14"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.30-8.13-14
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Business Impact Analysis", [
        ("A.5.30-8.13-14-01", "Business Continuity",
         "Business continuity shall be based on a documented business impact analysis (BIA) and risk assessment. The BIA shall:."),
        ("A.5.30-8.13-14-02", "Bia Frequency*: The Bia",
         "BIA frequency*: The BIA shall be conducted initially during ISMS implementation, reviewed annually, and updated upon significant business changes (new services, acquisitions, major system changes) or after major incidents."),
        ("A.5.30-8.13-14-03", "Be Classified Into Criticality Tiers",
         "Systems shall be classified into criticality tiers based on BIA results. These tiers drive backup frequency, redundancy requirements, and testing schedules:."),
        ("A.5.30-8.13-14-04", "System Owners, In Consultation With The",
         "System owners, in consultation with the BC/DR Coordinator, shall determine the appropriate tier for each system based on the BIA results."),
        ("A.5.30-8.13-14-05", "Role Assignment*: Where The Organisation",
         "Role assignment*: Where the organisation does not have a dedicated BC/DR Coordinator, the IT Operations Manager shall assume BC/DR coordination responsibilities. This assignment shall be formally documented in the role description."),
        ("A.5.30-8.13-14-06", "Systems Unable To Meet Their Defined",
         "Systems unable to meet their defined RPO or RTO shall follow the exception management process (see Policy Compliance — Exceptions)."),
    ]),

    ("Information Backup", [
        ("A.5.30-8.13-14-07", "The Following Categories Of Information",
         "The following categories of information shall be backed up:."),
        ("A.5.30-8.13-14-08", "A Backup Schedule, Retention Schedule,",
         "A backup schedule, retention schedule, and testing schedule shall be maintained and made available. Backup frequency shall align with the RPO for each system tier:."),
        ("A.5.30-8.13-14-09", "Extended Retention*: Longer Retention",
         "Extended retention*: Longer retention periods may be required by regulation (e.g., financial records 7–10 years), legal hold requests, or contractual obligations. Extended retention shall be justified (regulatory requirement, legal hold, or contractual obligation) to prevent unnecessary data accumulation. Shorter retention periods require CISO approval with documented risk acceptance."),
        ("A.5.30-8.13-14-10", "Select Appropriate Backup Strategies",
         "The organisation shall select appropriate backup strategies based on system requirements:."),
        ("A.5.30-8.13-14-11", "Implement The 3-2-1 Backup Rule As",
         "The organisation shall implement the 3-2-1 backup rule as a minimum for Tier 1 and Tier 2 systems:."),
        ("A.5.30-8.13-14-12", "Immutable Backups*: For Tier 1 And",
         "Immutable backups*: For Tier 1 and Tier 2 systems, at least one backup copy shall be immutable (write-once-read-many) or air-gapped to protect against ransomware and accidental deletion. Technologies include object storage with object lock (e.g., AWS S3 Object Lock, Azure Immutable Blob Storage, or equivalent), WORM tape, or air-gapped offline media."),
        ("A.5.30-8.13-14-13", "Conditional*: Organisations Subject To",
         "Conditional*: Organisations subject to DORA (EU financial entities) shall implement immutable backup copies where technically feasible (Art. 12(4)) and offsite backup storage at sufficient geographic distance."),
        ("A.5.30-8.13-14-14", "Be Encrypted Both In Transit And",
         "Backups shall be encrypted both in transit and at rest using AES-256 or equivalent, per the Use of Cryptography Policy (A.8.24). The backup solution (e.g., Veeam, Commvault, AWS Backup, Azure Backup, or equivalent) shall support built-in encryption."),
        ("A.5.30-8.13-14-15", "Backups Stored In Cloud-Based Solutions",
         "Backups stored in cloud-based solutions shall as a minimum be hosted with an ISO 27001 certified provider."),
        ("A.5.30-8.13-14-16", "The Media",
         "The media shall be encrypted."),
        ("A.5.30-8.13-14-17", "The Media",
         "The media shall be labelled and stored securely with restricted, authorisation-required access control."),
        ("A.5.30-8.13-14-18", "Offsite Transfer",
         "Offsite transfer shall use an approved secure courier or encrypted electronic transfer."),
        ("A.5.30-8.13-14-19", "Be Protected To At Least The",
         "Backups shall be protected to at least the same security level as the original data."),
        ("A.5.30-8.13-14-20", "Backup Encryption Key Management:",
         "Backup encryption key management: Encryption keys shall be managed separately from backup data. Key recovery procedures shall be documented and tested (keys must be accessible when primary systems are unavailable). Keys shall be rotated annually or upon suspected compromise. Key escrow or split-key custody is recommended for critical system backups. Key management shall comply with the Use of Cryptography Policy (A.8.24)."),
        ("A.5.30-8.13-14-21", "Backup Operations",
         "Backup operations shall be monitored:."),
        ("A.5.30-8.13-14-22", "Backup Logs",
         "Backup logs shall be produced and checked for errors and performance at least weekly. Where errors are found, corrective action shall be taken and recorded."),
        ("A.5.30-8.13-14-23", "Monthly Backup Status Reports",
         "Monthly backup status reports shall be provided to the CISO, including backup coverage, success rates, and outstanding issues."),
        ("A.5.30-8.13-14-24", "Be Regularly Tested To Ensure They",
         "Backups shall be regularly tested to ensure they can be relied upon in an emergency and meet the needs of the business continuity plans:."),
        ("A.5.30-8.13-14-25", "Restore Test",
         "Each restore test shall document: test date, systems tested, backup source, expected vs. actual recovery time, data integrity verification, issues encountered, and sign-off by the test owner."),
        ("A.5.30-8.13-14-26", "Failed Test Response*: Restore Tests",
         "Failed test response*: Restore tests revealing recovery failures shall trigger escalation based on system tier:."),
        ("A.5.30-8.13-14-27", "Occur Within 30 Days Of Remediation",
         "Retest shall occur within 30 days of remediation for Tier 1–2 systems."),
        ("A.5.30-8.13-14-28", "Conditional*: Organisations Subject To",
         "Conditional*: Organisations subject to DORA shall test backup recovery at least annually (Art. 12(6))."),
        ("A.5.30-8.13-14-29", "Backup And Restoration Procedures",
         "Backup and restoration procedures shall be documented, maintained, and kept accessible (including when primary systems are unavailable). Recovery procedures for each critical system shall include:."),
        ("A.5.30-8.13-14-30", "For Cloud-Hosted Systems, The",
         "For cloud-hosted systems, the organisation shall:."),
        ("A.5.30-8.13-14-31", "Cloud Provider Sla Guarantees",
         "Cloud provider SLA guarantees shall be verified against organisational RTO requirements for each system tier."),
        ("A.5.30-8.13-14-32", "Provider Historical Uptime And Incident",
         "Provider historical uptime and incident response performance shall be documented during vendor assessment (per A.5.19–23)."),
        ("A.5.30-8.13-14-33", "Customer-Managed Redundancy",
         "Where provider SLA is insufficient for Tier 1 or Tier 2 systems, customer-managed redundancy shall be implemented."),
        ("A.5.30-8.13-14-34", "Provider Bc/Dr Capabilities (Multi-Az,",
         "Provider BC/DR capabilities (multi-AZ, backup/restore, failover) shall be documented."),
        ("A.5.30-8.13-14-35", "Cloud Provider Bc/Dr Commitments",
         "Cloud provider BC/DR commitments shall be included in the vendor risk assessment."),
    ]),

    ("Redundancy Info Process", [
        ("A.5.30-8.13-14-36", "Information Processing Facilities",
         "Information processing facilities shall be implemented with redundancy sufficient to meet availability requirements:."),
        ("A.5.30-8.13-14-37", "System Owners",
         "System owners shall conduct SPOF analysis for Tier 1 and Tier 2 systems to identify components whose failure would cause complete system unavailability. Common SPOFs include:."),
        ("A.5.30-8.13-14-38", "Spof Remediation*: Identified Spofs For",
         "SPOF remediation*: Identified SPOFs for Tier 1 systems shall be remediated within 90 days or have documented risk acceptance from the CISO. Tier 2 system SPOFs shall be remediated within 180 days or have documented risk acceptance."),
        ("A.5.30-8.13-14-39", "Systems With Redundancy",
         "Systems with redundancy shall have their failover mechanisms tested:."),
        ("A.5.30-8.13-14-40", "Failover Test",
         "Each failover test shall document: systems tested, failover trigger mechanism, actual failover time vs. RTO target, issues identified, and sign-off."),
        ("A.5.30-8.13-14-41", "Failback Testing*: Failover Tests",
         "Failback testing*: Failover tests shall also validate the failback process (returning to primary infrastructure after recovery). Failback procedures shall be documented and tested alongside failover to ensure full recovery cycle capability."),
        ("A.5.30-8.13-14-42", "Failed Failover Response*: Tests",
         "Failed failover response*: Tests revealing inability to meet RTO shall trigger immediate remediation and risk assessment per the escalation table in Backup Testing and Verification."),
        ("A.5.30-8.13-14-43", "Geographic Redundancy*: For Tier 1",
         "Geographic redundancy*: For Tier 1 systems, redundancy shall be implemented at sufficient geographic distance to protect against site-wide disasters:."),
        ("A.5.30-8.13-14-44", "Cost-Benefit Analysis*: Redundancy",
         "Cost-benefit analysis*: Redundancy decisions shall balance the cost of redundant infrastructure against the business impact of extended outages and regulatory requirements. For many SMEs, cloud-native redundancy (multi-AZ deployment) provides cost-effective geographic redundancy without maintaining separate physical infrastructure."),
    ]),

    ("ICT Continuity Planning", [
        ("A.5.30-8.13-14-45", "Maintain Documented Procedures For",
         "The organisation shall maintain documented procedures for responding to a disruptive incident and for continuing or recovering its activities within predetermined timeframes. Business continuity plans shall address the requirements of those who will use them."),
        ("A.5.30-8.13-14-46", "Business Continuity Plans",
         "Business continuity plans shall cover*:."),
        ("A.5.30-8.13-14-47", "Define*: Purpose And Scope, Objectives,",
         "Each plan shall define*: purpose and scope, objectives, activation criteria and procedures, implementation procedures, roles and authorities, communication requirements, internal and external interdependencies, resource requirements, and information flow and documentation processes."),
        ("A.5.30-8.13-14-48", "For Each Tier 1 And Tier",
         "For each Tier 1 and Tier 2 system, the organisation shall maintain ICT recovery plans documenting:."),
        ("A.5.30-8.13-14-49", "Recovery Plans",
         "Recovery plans shall be version-controlled, reviewed annually, and updated after testing exercises, major incidents, or significant system changes."),
        ("A.5.30-8.13-14-50", "A Disaster",
         "A disaster shall be declared when:."),
        ("A.5.30-8.13-14-51", "Activation Notification*: Pre-Approved",
         "Activation notification*: Pre-approved notification templates shall be maintained in the BC/DR plan. Notification shall be issued via primary channel (email, collaboration platform) and backup channel (SMS, phone) simultaneously."),
        ("A.5.30-8.13-14-52", "Business Continuity Plans And Technical",
         "Business continuity plans and technical recovery plans shall be tested at least annually and when significant change occurs."),
        ("A.5.30-8.13-14-53", "Test Documentation*: Each Test",
         "Test documentation*: Each test shall document: test date, scope, objectives, participants, scenario, results (success/partial/failure), actual vs. target RTO/RPO, issues identified, lessons learned, action items, and sign-off."),
        ("A.5.30-8.13-14-54", "Failed Test Response*: Tests Revealing",
         "Failed test response*: Tests revealing inability to meet RTO/RPO shall trigger immediate investigation, gap remediation plan, interim compensating controls, and executive notification for Tier 1 systems."),
        ("A.5.30-8.13-14-55", "Conditional*: Organisations Subject To",
         "Conditional*: Organisations subject to DORA shall test BC arrangements at least annually (Art. 11(9)) and test ICT backup and restoration at least annually (Art. 12(6))."),
        ("A.5.30-8.13-14-56", "Post-Test Training: Bc/Dr Test Results",
         "Post-test training: BC/DR test results and lessons learned shall be communicated to all participants within 30 days of each test."),
        ("A.5.30-8.13-14-57", "Bc/Dr Plans",
         "BC/DR plans shall include communication procedures for:."),
        ("A.5.30-8.13-14-58", "Communication Channels*: Primary",
         "Communication channels*: Primary channels (email, [Collaboration Platform]); backup channels (SMS, phone) if primary channels are unavailable. Contact lists shall be maintained, accessible offline (printed or on mobile devices), and reviewed quarterly."),
        ("A.5.30-8.13-14-59", "Maintain Documented Procedures To",
         "The organisation shall maintain documented procedures to restore and return business activities from temporary measures adopted during an incident to normal business operations."),
        ("A.5.30-8.13-14-60", "Recovery Validation Checklist*: Before",
         "Recovery validation checklist*: Before declaring a system recovered and returning to normal operations, the following shall be verified:."),
        ("A.5.30-8.13-14-61", "Ransom Payment*: The Organisation",
         "Ransom payment*: The organisation shall not make ransom payments without explicit Executive Management approval and prior consultation with legal counsel and cyber insurance provider (if applicable)."),
        ("A.5.30-8.13-14-62", "An Incident Management Process",
         "An incident management process shall be in place and followed. Business continuity incidents shall additionally be:."),
    ]),

    ("BC DR Metrics and Reporting", [
        ("A.5.30-8.13-14-63", "The Following Metrics",
         "The following metrics shall be tracked to measure BC/DR programme effectiveness:."),
        ("A.5.30-8.13-14-64", "Metrics Breaching Targets For Two",
         "Metrics breaching targets for two consecutive reporting periods shall be escalated to the CISO and reported at the next Management Review."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.30-8.13-14
# =============================================================================
