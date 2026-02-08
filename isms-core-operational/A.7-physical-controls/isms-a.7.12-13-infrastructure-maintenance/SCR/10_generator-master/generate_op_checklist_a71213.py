#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.7.12-13 — Cabling Security and Equipment Maintenance Compliance Checklist

Controls A.7.12-13: Cabling Security and Equipment Maintenance
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Cable Protection Standards (10 reqs)
4. Cable Segregation (6 reqs)
5. Cable Documentation & Labelling (14 reqs)
6. Fibre Optic Requirements (3 reqs)
7. Inspection and Cable Maint (6 reqs)
8. Maintenance Programme (6 reqs)
9. Avail and Service Continuity (17 reqs)
10. Maint Personnel Authorisation (9 reqs)
11. Third-Party Maint Provider Mgmt (3 reqs)
12. Security During Maintenance (10 reqs)
13. Remote Maintenance (7 reqs)
14. Equipment Removal and Return (5 reqs)
15. Infra Failure Incident Response (2 reqs)
16. Maintenance Records (7 reqs)
17. Infrastructure Performance Mon (2 reqs)
18. Compliance Measurement (1 reqs)

Total: 108 requirements across 16 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.7.12-13"
CONTROL_ID = "A.7.12-13"
CONTROL_NAME = "Cabling Security and Equipment Maintenance"
SOURCE_POLICY = "ISMS-OP-POL-A.7.12-13"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.7.12-13
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Cable Protection Standards", [
        ("A.7.12-13-01", "Cables Carrying Power, Data, Or",
         "All cables carrying power, data, or supporting information services shall be physically protected:."),
        ("A.7.12-13-02", "Be Routed Through Protected Pathways —",
         "Cables shall be routed through protected pathways — conduits, cable trays, raised floors, or ceiling voids — not exposed across open areas."),
        ("A.7.12-13-03", "Underground Cabling",
         "Underground cabling shall be protected against accidental damage using armoured conduits or duct systems. Route markers shall identify buried cable paths."),
        ("A.7.12-13-04", "Be Protected From Environmental Hazards",
         "Cables shall be protected from environmental hazards including water ingress, heat sources, chemical exposure, and physical impact. Cable routes shall avoid areas with high risk of damage."),
        ("A.7.12-13-05", "Suitable Protection",
         "Where cables traverse between buildings, suitable protection shall be applied (armoured cable, sealed duct, or direct-buried conduit)."),
        ("A.7.12-13-06", "Wiring Closets, Telecommunications",
         "Wiring closets, telecommunications rooms, and cable distribution frames shall be physically secured. These areas shall be locked when unoccupied and access restricted to authorised personnel."),
        ("A.7.12-13-07", "Manhole And Duct Access Points",
         "Manhole and duct access points shall be secured and access logged."),
        ("A.7.12-13-08", "Be Protected From Electromagnetic",
         "Cables shall be protected from electromagnetic interference (EMI) through appropriate shielding, separation from interference sources, and selection of cable type suited to the environment."),
        ("A.7.12-13-09", "In Environments With High",
         "In environments with high electromagnetic interference (e.g., near heavy electrical equipment, industrial machinery, or radio transmission), shielded cable (STP/FTP) or fibre optic cable shall be used."),
        ("A.7.12-13-10", "Cable Installations",
         "Cable installations shall comply with the organisation's adopted structured cabling standard (IEC 11801 / EN 50173 / TIA-568 as applicable) for shielding and separation requirements."),
    ]),

    ("Cable Segregation", [
        ("A.7.12-13-11", "Power Cables And Communications Cables",
         "Power cables and communications cables shall be segregated to prevent electromagnetic interference:."),
        ("A.7.12-13-12", "Minimum Separation Distances",
         "Minimum separation distances shall follow the structured cabling standard adopted by the organisation. As a baseline: minimum 200 mm separation between unshielded data cables and power cables running in parallel. Where crossing is unavoidable, cables shall cross at right angles."),
        ("A.7.12-13-13", "Power And Data Cables",
         "Power and data cables shall use separate conduits, cable trays, or pathways. Shared pathways are not permitted for unshielded data cables and power cables."),
        ("A.7.12-13-14", "Separation Requirements",
         "Separation requirements shall be documented in the organisation's cabling standard and applied consistently across all installations."),
        ("A.7.12-13-15", "Cables Carrying Traffic Of Different",
         "Cables carrying traffic of different security classifications shall be physically separated where feasible, or clearly identified using colour coding or labelling to prevent cross-connection."),
        ("A.7.12-13-16", "High-Security Network Cables (E.G.,",
         "High-security network cables (e.g., management networks, financial systems, security systems) shall be identifiable through consistent colour coding or labelling convention defined by the organisation."),
    ]),

    ("Cable Documentation & Labelling", [
        ("A.7.12-13-17", "Cable Infrastructure",
         "Cable infrastructure shall be documented and maintained:."),
        ("A.7.12-13-18", "A Cable Register Or Cable Management",
         "A cable register or cable management database shall record all structured cabling installations, including cable type, endpoints, route, installation date, and classification."),
        ("A.7.12-13-19", "As-Built Cabling Diagrams",
         "As-built cabling diagrams shall be maintained for all facilities. Diagrams shall show cable routes, patch panel locations, distribution frames, and interconnections."),
        ("A.7.12-13-20", "Cable Documentation",
         "Cable documentation shall be kept current. All cabling changes shall be reflected in documentation within 5 business days of completion."),
        ("A.7.12-13-21", "Cable Documentation",
         "Cable documentation shall be secured and access-controlled. Only authorised personnel shall have access to detailed cabling diagrams (these reveal network topology and physical routes)."),
        ("A.7.12-13-22", "Be Labelled At Both Ends With",
         "All cables shall be labelled at both ends with a unique identifier that maps to the cable register."),
        ("A.7.12-13-23", "Patch Panels, Distribution Frames, And",
         "Patch panels, distribution frames, and telecommunications outlets shall be clearly labelled."),
        ("A.7.12-13-24", "Be Durable, Legible, And Enable",
         "Labels shall be durable, legible, and enable identification without requiring reference to detailed documentation for routine operations."),
        ("A.7.12-13-25", "Define And Document A Consistent",
         "The organisation shall define and document a consistent labelling convention (e.g., building-floor-room-rack-port)."),
        ("A.7.12-13-26", "Cabling Installations, Modifications,",
         "All cabling installations, modifications, and removals shall follow the organisation's change management process (A.8.32) with the following specific requirements:."),
        ("A.7.12-13-27", "Cabling Change Requests",
         "Cabling change requests shall include:."),
        ("A.7.12-13-28", "Cabling Changes",
         "All cabling changes shall include post-implementation testing:."),
        ("A.7.12-13-29", "Unused Cables",
         "Unused cables shall be disconnected, documented, and either removed or clearly marked as inactive."),
        ("A.7.12-13-30", "Quarterly Physical Walkthroughs",
         "Quarterly physical walkthroughs shall be conducted to identify unauthorised additions, modifications, or damage. Findings shall be reconciled against as-built diagrams and change records, with results documented and signed off by the Facilities Manager."),
    ]),

    ("Fibre Optic Requirements", [
        ("A.7.12-13-31", "Fibre Optic Cable",
         "Fibre optic cable shall be used in preference to copper for data transmission in the following circumstances:."),
        ("A.7.12-13-32", "Fusion Splicing",
         "Where fibre optic is deployed, fusion splicing shall be used for permanent connections (not mechanical splicing) in secure areas. Fibre patch panels shall be housed in locked enclosures."),
        ("A.7.12-13-33", "Shielded Cable (Stp/Ftp)",
         "Where copper cable is used in areas with interception risk, shielded cable (STP/FTP) shall be specified and cable routes shall be physically secured."),
    ]),

    ("Inspection and Cable Maint", [
        ("A.7.12-13-34", "Regular Inspection And Maintenance Of",
         "Regular inspection and maintenance of cabling infrastructure shall be performed:."),
        ("A.7.12-13-35", "Cable Infrastructure",
         "Cable infrastructure shall be included in the organisation's maintenance programme with defined inspection intervals."),
        ("A.7.12-13-36", "Visual Inspections",
         "Visual inspections shall be conducted quarterly for accessible cable routes, checking for damage, unauthorised modifications, labelling integrity, and pathway obstructions."),
        ("A.7.12-13-37", "Formal Cable Testing (Continuity,",
         "Formal cable testing (continuity, performance) shall be conducted annually or following any reported issues."),
        ("A.7.12-13-38", "Damaged Cables",
         "Damaged cables shall be repaired or replaced promptly. Temporary repairs shall be documented and permanent repair scheduled within 30 calendar days."),
        ("A.7.12-13-39", "Inspection Findings",
         "Inspection findings shall be documented and retained for a minimum of 3 years."),
    ]),

    ("Maintenance Programme", [
        ("A.7.12-13-40", "Establish And Maintain A Maintenance",
         "The organisation shall establish and maintain a maintenance programme covering all equipment that processes, stores, or supports the processing of information:."),
        ("A.7.12-13-41", "In-Scope Equipment Recorded In The Asset",
         "All in-scope equipment recorded in the asset inventory (per A.5.9) shall be included in the maintenance programme. The asset inventory is the authoritative source for programme completeness."),
        ("A.7.12-13-42", "Quarterly Reconciliation",
         "Quarterly reconciliation shall verify that all inventoried equipment has maintenance coverage. Reconciliation results and sign-off shall be retained as evidence."),
        ("A.7.12-13-43", "Maintenance Schedules",
         "Maintenance schedules shall follow manufacturer recommendations as minimums. Deviations require documented risk acceptance via the exception register."),
        ("A.7.12-13-44", "The Maintenance Programme",
         "The maintenance programme shall be managed through [CMMS] or equivalent maintenance tracking system. Where a dedicated CMMS is not deployed, a controlled spreadsheet or register shall be used."),
        ("A.7.12-13-45", "Maintenance Schedules",
         "Maintenance schedules shall be adjusted based on equipment age, environmental conditions, manufacturer advisories, and incident history. Equipment approaching end-of-life shall have maintenance frequency increased or be scheduled for replacement."),
    ]),

    ("Avail and Service Continuity", [
        ("A.7.12-13-46", "Cabling And Equipment Infrastructure",
         "Cabling and equipment infrastructure directly supports the organisation's service availability commitments to customers. Maintenance activities shall be planned and executed to minimise service disruption."),
        ("A.7.12-13-47", "Maintenance Activities",
         "All maintenance activities shall be assessed for potential service impact before scheduling:."),
        ("A.7.12-13-48", "Non-Emergency Maintenance That May",
         "All non-emergency maintenance that may impact services shall be scheduled during approved maintenance windows."),
        ("A.7.12-13-49", "Infrastructure Maintenance Programme",
         "Infrastructure maintenance programme shall support the organisation's availability commitments:."),
        ("A.7.12-13-50", "Preventive Maintenance Scheduling",
         "Preventive maintenance scheduling constraint*: Total planned downtime for infrastructure maintenance shall not exceed 50% of the annual allowable downtime budget, reserving capacity for unplanned failures."),
        ("A.7.12-13-51", "Equipment Maintenance Programme",
         "Equipment maintenance programme shall account for redundancy design:."),
        ("A.7.12-13-52", "Single Points Of Failure: Equipment With",
         "Single points of failure: Equipment with no redundancy shall have maintenance scheduled during low-usage periods with advance customer notification."),
        ("A.7.12-13-53", "Redundant Systems: Where N+1 Or 2N",
         "Redundant systems: Where N+1 or 2N redundancy exists, maintenance shall be staggered to maintain at least N capacity at all times."),
        ("A.7.12-13-54", "Critical Path Equipment (Ups, Network",
         "Critical path equipment (UPS, network core, primary servers): Maintenance shall include pre-maintenance verification of redundancy status and post-maintenance failover testing."),
        ("A.7.12-13-55", "Remaining Capacity",
         "When redundant equipment is taken offline for maintenance, remaining capacity shall be verified sufficient for current load plus 20% buffer:."),
        ("A.7.12-13-56", "Be Rescheduled Or Additional Temporary",
         "If capacity would fall below buffer threshold, maintenance shall be rescheduled or additional temporary capacity provisioned."),
        ("A.7.12-13-57", "Load Testing After Maintenance",
         "Load testing after maintenance shall verify full redundancy restored before marking equipment 'in service'."),
        ("A.7.12-13-58", "Infrastructure Maintenance Programme",
         "Infrastructure maintenance programme shall support business continuity planning:."),
        ("A.7.12-13-59", "Equipment And Cabling Critical To",
         "Equipment and cabling critical to business continuity shall be identified and prioritised:."),
        ("A.7.12-13-60", "Annual Dr Failover Test",
         "Annual DR failover test shall include infrastructure components:."),
        ("A.7.12-13-61", "Dr Test",
         "DR test shall verify maintenance programme has maintained infrastructure in DR-ready state."),
        ("A.7.12-13-62", "Dr Test Findings That Reveal",
         "DR test findings that reveal infrastructure gaps shall trigger maintenance programme updates."),
    ]),

    ("Maint Personnel Authorisation", [
        ("A.7.12-13-63", "Only Personnel With Documented",
         "Only personnel with documented authorisation shall perform maintenance on information processing equipment."),
        ("A.7.12-13-64", "Maintenance Authorisation",
         "Maintenance authorisation shall specify which equipment categories and which maintenance activities the individual is qualified to perform."),
        ("A.7.12-13-65", "Authorisation Records",
         "Authorisation records shall be maintained and reviewed annually."),
        ("A.7.12-13-66", "Third-Party Maintenance",
         "Third-party maintenance shall be performed only by contracted and approved providers. Maintenance contracts shall include confidentiality obligations and security requirements."),
        ("A.7.12-13-67", "Third-Party Maintenance Personnel",
         "Third-party maintenance personnel shall be identified and verified (government-issued identification) before being granted access to equipment."),
        ("A.7.12-13-68", "Maintain A Register Of Approved",
         "The organisation shall maintain a register of approved third-party maintenance providers, reviewed annually."),
        ("A.7.12-13-69", "Third-Party Maintenance Personnel",
         "Third-party maintenance personnel shall be supervised when accessing equipment that processes or stores sensitive or confidential information, unless a documented risk assessment concludes that unsupervised access is acceptable (e.g., dedicated maintenance contract with background-checked personnel, isolated equipment)."),
        ("A.7.12-13-70", "Unsupervised Third-Party Maintenance",
         "Unsupervised third-party maintenance access shall be logged with individual identification, time in/out, and equipment accessed."),
        ("A.7.12-13-71", "Supervision Records",
         "Supervision records shall be maintained as evidence."),
    ]),

    ("Third-Party Maint Provider Mgmt", [
        ("A.7.12-13-72", "Maintenance Contracts With Third-Party",
         "Maintenance contracts with third-party providers shall include:."),
        ("A.7.12-13-73", "Maintenance Provider Performance",
         "Maintenance provider performance shall be tracked and reviewed:."),
        ("A.7.12-13-74", "Maintenance Provider",
         "Each maintenance provider shall receive an annual review covering:."),
    ]),

    ("Security During Maintenance", [
        ("A.7.12-13-75", "Sensitive Data",
         "Sensitive data shall be protected during all maintenance activities. Maintenance personnel shall not have access to data stored on equipment unless specifically required and authorised."),
        ("A.7.12-13-76", "Equipment",
         "Equipment containing data shall not be removed from premises for maintenance where on-site repair is feasible."),
        ("A.7.12-13-77", "Be Securely Erased From The Equipment",
         "If off-site maintenance is required, data shall be securely erased from the equipment before removal (per A.7.14 secure disposal procedures), or the storage media shall be removed and retained by the organisation."),
        ("A.7.12-13-78", "For Equipment Where Data Erasure Is",
         "For equipment where data erasure is not feasible before removal (e.g., fault prevents access), a documented risk assessment shall be completed and the maintenance provider's data handling obligations confirmed in writing."),
        ("A.7.12-13-79", "After Maintenance, Equipment",
         "After maintenance, equipment shall be physically inspected before being returned to service to verify that no unauthorised modifications have been made."),
        ("A.7.12-13-80", "Tools And Equipment Brought On-Site By",
         "All tools and equipment brought on-site by maintenance personnel shall be accounted for before and after maintenance."),
        ("A.7.12-13-81", "Firmware And Software Versions",
         "Firmware and software versions shall be verified after maintenance to confirm no unauthorised changes."),
        ("A.7.12-13-82", "Maintenance Access",
         "Maintenance access shall be time-limited. Access windows shall be agreed in advance and documented."),
        ("A.7.12-13-83", "Maintenance Access",
         "All maintenance access shall be logged: who performed the work, when, what equipment was accessed, and what work was performed."),
        ("A.7.12-13-84", "Maintenance Personnel",
         "Maintenance personnel shall be issued temporary access credentials (badges, system access) that expire at the end of the maintenance window."),
    ]),

    ("Remote Maintenance", [
        ("A.7.12-13-85", "Remote Maintenance Introduces Additional",
         "Remote maintenance introduces additional risk. The following controls shall apply:."),
        ("A.7.12-13-86", "Remote Maintenance",
         "Remote maintenance shall be explicitly authorised before each session. Standing authorisation for remote access is not permitted."),
        ("A.7.12-13-87", "Remote Maintenance Sessions",
         "Remote maintenance sessions shall use encrypted connections (VPN, SSH, or equivalent secure protocol). Unencrypted remote access is not permitted."),
        ("A.7.12-13-88", "Remote Maintenance Sessions",
         "Remote maintenance sessions shall be logged, including session start/end times, individual identity, and actions performed. Session recording is recommended for critical equipment."),
        ("A.7.12-13-89", "Remote Access",
         "Remote access shall be disabled when not actively in use. Persistent remote access connections for maintenance purposes shall not remain open."),
        ("A.7.12-13-90", "Remote Maintenance Of Equipment",
         "Remote maintenance of equipment containing sensitive data shall require the same authorisation as physical access to that equipment."),
        ("A.7.12-13-91", "A Dedicated Jump Host Or Bastion",
         "Where the maintenance provider requires remote access to internal systems, a dedicated jump host or bastion server with multi-factor authentication shall be used."),
    ]),

    ("Equipment Removal and Return", [
        ("A.7.12-13-92", "Authorisation: Removal",
         "Authorisation: Removal shall be authorised in writing by the equipment owner or designated delegate."),
        ("A.7.12-13-93", "Data Protection: Data",
         "Data protection: Data shall be securely erased before removal. If erasure is not possible, storage media shall be removed and retained by the organisation. The data protection approach shall be documented."),
        ("A.7.12-13-94", "Chain Of Custody: A Chain Of",
         "Chain of custody: A chain of custody record shall be created documenting: equipment identification, condition at removal, removal date/time, authorised by, carrier/transporter, destination, expected return date."),
        ("A.7.12-13-95", "Equipment Return Inspection: Upon",
         "Equipment return inspection: Upon return, the equipment shall be inspected for tampering, unauthorised modifications, and correct configuration. Firmware and software versions shall be verified."),
        ("A.7.12-13-96", "Asset Register Update: Equipment Return",
         "Asset register update: Equipment return shall be logged in [Asset Management System] with maintenance summary and inspection results."),
    ]),

    ("Infra Failure Incident Response", [
        ("A.7.12-13-97", "Infrastructure Failures (Cable Damage,",
         "Infrastructure failures (cable damage, equipment malfunction) that impact or may impact services shall be managed through the organisation's incident management process."),
        ("A.7.12-13-98", "Infrastructure Incidents",
         "Infrastructure incidents shall document:."),
    ]),

    ("Maintenance Records", [
        ("A.7.12-13-99", "Maintenance — Preventive And Corrective",
         "All maintenance — preventive and corrective — shall be documented:."),
        ("A.7.12-13-100", "Maintenance Records",
         "Maintenance records shall be retained for a minimum of 3 years or the lifecycle of the equipment, whichever is longer."),
        ("A.7.12-13-101", "Be Available For Audit At All",
         "Records shall be available for audit at all times."),
        ("A.7.12-13-102", "Be Stored In [Cmms] Or Equivalent",
         "Records shall be stored in [CMMS] or equivalent controlled register."),
        ("A.7.12-13-103", "Maintenance Records",
         "Maintenance records shall be reviewed quarterly for trends: recurring faults, equipment approaching end-of-life, increasing failure frequency, or maintenance SLA breaches."),
        ("A.7.12-13-104", "Trend Analysis",
         "Trend analysis shall inform equipment replacement planning and maintenance programme adjustments."),
        ("A.7.12-13-105", "Quarterly Trend Reports",
         "Quarterly trend reports shall be provided to the IT Operations Manager and CISO."),
    ]),

    ("Infrastructure Performance Mon", [
        ("A.7.12-13-106", "Beyond Maintenance Completion Metrics,",
         "Beyond maintenance completion metrics, the organisation shall monitor infrastructure health indicators to enable predictive maintenance and demonstrate availability effectiveness."),
        ("A.7.12-13-107", "Health Monitoring",
         "Health monitoring shall trigger early maintenance actions before failure:."),
    ]),

    ("Compliance Measurement", [
        ("A.7.12-13-108", "The Following Metrics",
         "The following metrics shall be tracked and reported to the CISO quarterly:."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.7.12-13
# =============================================================================
