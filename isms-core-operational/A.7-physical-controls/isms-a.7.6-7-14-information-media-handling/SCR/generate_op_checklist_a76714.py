#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.7.6-7-14 — Secure Areas and Media Handling Compliance Checklist

Controls A.7.6-7-14: Secure Areas and Media Handling
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Working in Secure Areas (16 reqs)
4. Clear Desk and Clear Screen (22 reqs)
5. Secure Disposal or Re-Use (29 reqs)
6. SOC 2 Considerations (2 reqs)
7. Optional Payment Card Data (3 reqs)

Total: 72 requirements across 5 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.7.6-7-14"
CONTROL_ID = "A.7.6-7-14"
CONTROL_NAME = "Secure Areas and Media Handling"
SOURCE_POLICY = "ISMS-OP-POL-A.7.6-7-14"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.7.6-7-14
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Working in Secure Areas", [
        ("A.7.6-7-14-01", "Personnel Working In Secure Areas",
         "Personnel working in secure areas shall follow these requirements:."),
        ("A.7.6-7-14-02", "Access To Secure Areas",
         "Access to secure areas shall be granted only to authorised personnel based on job role and need-to-know principle."),
        ("A.7.6-7-14-03", "Only Be Made Aware Of Activities",
         "Personnel shall only be made aware of activities within secure areas on a need-to-know basis."),
        ("A.7.6-7-14-04", "Not Work Alone In Secure Areas",
         "Personnel shall not work alone in secure areas outside normal business hours unless an approved exception exists with compensating controls in place (e.g., check-in procedure with reception or colleague, CCTV monitoring, or buddy system)."),
        ("A.7.6-7-14-05", "Empty Secure Areas",
         "Empty secure areas shall be physically locked and periodically checked."),
        ("A.7.6-7-14-06", "Photography, Video, Audio, Or Other",
         "Photography, video, audio, or other recording in secure areas shall be prohibited unless specifically authorised in writing by the Secure Area Owner."),
        ("A.7.6-7-14-07", "Mobile Phones, Cameras, And",
         "Mobile phones, cameras, and recording-capable devices shall not be brought into high-security areas (e.g., server rooms) unless authorised."),
        ("A.7.6-7-14-08", "Third Parties (Contractors, Vendors,",
         "Third parties (contractors, vendors, visitors) shall be escorted at all times within secure areas."),
        ("A.7.6-7-14-09", "Third-Party Access",
         "Third-party access shall be logged with entry and exit times and shall be time-limited to the duration of the specific task."),
        ("A.7.6-7-14-10", "Third Parties",
         "Third parties shall sign a confidentiality or non-disclosure agreement before entering secure areas."),
        ("A.7.6-7-14-11", "Third-Party Equipment",
         "Third-party equipment shall not be brought into secure areas unless authorised by the Secure Area Owner or Security Team."),
        ("A.7.6-7-14-12", "Sensitive Information",
         "Sensitive information shall not be discussed where it may be overheard by unauthorised persons."),
        ("A.7.6-7-14-13", "Sensitive Documents",
         "Sensitive documents shall be collected from printers, copiers, and fax machines immediately after printing."),
        ("A.7.6-7-14-14", "Deliveries And External Maintenance",
         "Deliveries and external maintenance personnel shall have access restricted to the minimum area necessary. Unsupervised access to secure areas shall not be permitted."),
        ("A.7.6-7-14-15", "Maintain A Register Of All Designated",
         "The organisation shall maintain a register of all designated secure areas, including:."),
        ("A.7.6-7-14-16", "This Register",
         "This register shall be reviewed annually or when organisational changes affect secure area designations."),
    ]),

    ("Clear Desk and Clear Screen", [
        ("A.7.6-7-14-17", "Sensitive Documents",
         "Sensitive documents shall be stored in locked drawers or cabinets when not in immediate active use."),
        ("A.7.6-7-14-18", "Documents Awaiting Printing",
         "Documents awaiting printing shall be collected immediately using secure print release where available."),
        ("A.7.6-7-14-19", "Only Documents Actively Being Worked On",
         "Only documents actively being worked on shall be on desks. Accumulation of classified documents on desks is not permitted."),
        ("A.7.6-7-14-20", "Sensitive Documents",
         "All sensitive documents shall be locked in drawers, cabinets, or safes."),
        ("A.7.6-7-14-21", "Removable Storage Media (Usb Drives,",
         "Removable storage media (USB drives, external drives, SD cards) shall be secured in locked storage."),
        ("A.7.6-7-14-22", "Access Cards, Keys, And Tokens",
         "Access cards, keys, and tokens shall not be left unattended on desks."),
        ("A.7.6-7-14-23", "Notebooks And Sticky Notes",
         "Notebooks and sticky notes containing passwords, PINs, or sensitive information shall be secured or destroyed."),
        ("A.7.6-7-14-24", "Removable Media",
         "Removable media containing classified information shall be locked away when not in use, regardless of classification level."),
        ("A.7.6-7-14-25", "Unmarked Documents",
         "Unmarked documents shall be treated as INTERNAL by default."),
        ("A.7.6-7-14-26", "Confidential Waste Bins",
         "Confidential waste bins shall be provided at workstations or in accessible locations for immediate disposal of sensitive paper documents."),
        ("A.7.6-7-14-27", "Screen Lock Timeout",
         "Screen lock timeout shall be enforced via [Endpoint Management Tool] (Group Policy, MDM, or equivalent) with the following tiered policy:."),
        ("A.7.6-7-14-28", "Manually Lock Screens When Leaving Their",
         "Users shall manually lock screens when leaving their workstation, even briefly, using keyboard shortcuts (Win+L on Windows, Ctrl+Cmd+Q on macOS)."),
        ("A.7.6-7-14-29", "Password-Protected Screensavers Or Lock",
         "Password-protected screensavers or lock screens shall be enabled on all devices."),
        ("A.7.6-7-14-30", "Sensitive Information",
         "Sensitive information shall not be displayed on screens visible to unauthorised persons, including visitors and passers-by."),
        ("A.7.6-7-14-31", "Projector And Screen Sharing Sessions",
         "Projector and screen sharing sessions shall be ended immediately after use. Presenters shall close sensitive applications before sharing screens."),
        ("A.7.6-7-14-32", "Applications",
         "All applications containing sensitive data shall be closed."),
        ("A.7.6-7-14-33", "Be Logged Off Or Shut Down",
         "Workstations shall be logged off or shut down in accordance with IT policy."),
        ("A.7.6-7-14-34", "Remote Desktop And Vpn Sessions",
         "Remote desktop and VPN sessions shall be disconnected."),
        ("A.7.6-7-14-35", "Whiteboards And Flipcharts",
         "Whiteboards and flipcharts shall be erased before the room is vacated."),
        ("A.7.6-7-14-36", "Meeting Rooms With Persistent Displays",
         "Meeting rooms with persistent displays (e.g., wall-mounted screens) shall not be left showing sensitive content after meetings end."),
        ("A.7.6-7-14-37", "Clear Desk And Clear Screen Audits",
         "Clear desk and clear screen audits shall be conducted monthly (minimum 1, maximum 2 per month) by the Facilities Manager or designated auditor."),
        ("A.7.6-7-14-38", "Audit Results",
         "Audit results shall be reported as part of the ISMS management review."),
    ]),

    ("Secure Disposal or Re-Use", [
        ("A.7.6-7-14-39", "Before Any Equipment Is Disposed Of",
         "Before any equipment is disposed of or re-used, the following assessment shall be completed:."),
        ("A.7.6-7-14-40", "Licensed Software Audit — Identify And",
         "Licensed software audit — Identify and decommission licensed software per licensing terms. Licence keys shall be recovered or transferred where applicable."),
        ("A.7.6-7-14-41", "Personal Data Check — Where Equipment",
         "Personal data check — Where equipment may have contained personal data, disposal shall comply with nFADP Art. 8 requirements for rendering data unrecoverable."),
        ("A.7.6-7-14-42", "Ssd And Flash Media — Cryptographic",
         "SSD and flash media — cryptographic erasure verification*: Traditional overwrite methods are unreliable for SSDs due to wear-levelling, over-provisioning, and write amplification. Cryptographic erasure on self-encrypting drives (SEDs) is only effective if: (a) the drive was configured with encryption enabled throughout its lifecycle (verified via asset record), and (b) erasure command completion is verified. The following verification procedure shall be applied:."),
        ("A.7.6-7-14-43", "Mobile Device Disposal — Encryption",
         "Mobile device disposal — encryption pre-requisite*: Device encryption shall be mandatory from day of deployment for all mobile devices handling INTERNAL or CONFIDENTIAL data (enforced via [MDM] policy, documented in device enrolment record). If a device was deployed without encryption (legacy, non-compliant): default to physical destruction regardless of data classification, and conduct root cause analysis for MDM policy remediation."),
        ("A.7.6-7-14-44", "Virtual And Cloud Storage*: Major Cloud",
         "Virtual and cloud storage*: Major cloud providers (AWS, Azure, GCP) do not issue individual destruction certificates for virtual storage. The organisation relies on provider SOC 2 Type II / ISO 27001 certification and data deletion attestations. Risk acceptance for reliance on provider deletion processes shall be documented annually in Management Review. For highest-sensitivity data: client-side encryption before uploading (organisation controls keys in on-premises HSM or separate KMS); upon disposal, delete organisation-managed keys and then delete cloud data; document key deletion with HSM/KMS audit log."),
        ("A.7.6-7-14-45", "Iot And Embedded Devices*: Devices With",
         "IoT and embedded devices*: Devices with embedded storage that cannot be sanitised using standard tools (e.g., IoT sensors, building management controllers, medical devices) shall be physically destroyed if they have stored CONFIDENTIAL or INTERNAL data. Where physical destruction is not feasible, the organisation shall obtain vendor guidance on sanitisation and document the method and any residual risk."),
        ("A.7.6-7-14-46", "As A Pre-Requisite For Disposal, The",
         "As a pre-requisite for disposal, the organisation shall maintain an inventory of IoT and embedded devices with storage:."),
        ("A.7.6-7-14-47", "Inventory Maintained By Facilities + It",
         "Inventory maintained by Facilities + IT Operations, reviewed annually. Unknown devices found during facility changes shall be escalated to CISO for assessment; default assumption: may contain CONFIDENTIAL data → physical destruction."),
        ("A.7.6-7-14-48", "Be Securely Erased Using An Approved",
         "All data shall be securely erased using an approved method appropriate to the previous data classification before reassignment."),
        ("A.7.6-7-14-49", "Licensed Software",
         "Licensed software shall be transferred or removed per licensing terms."),
        ("A.7.6-7-14-50", "[Asset Management System]",
         "[Asset Management System] shall be updated with the new assignee, date, and sanitisation record."),
        ("A.7.6-7-14-51", "Be Inspected And Refurbished If",
         "Equipment shall be inspected and refurbished if necessary before redeployment."),
        ("A.7.6-7-14-52", "Equipment That Has Stored Confidential",
         "Equipment that has stored CONFIDENTIAL data shall not be re-used externally. Storage media shall be physically destroyed."),
        ("A.7.6-7-14-53", "Equipment That Has Stored Internal Data",
         "Equipment that has stored INTERNAL data shall have storage media destroyed or sanitised to Purge level before external transfer."),
        ("A.7.6-7-14-54", "Organisation Identifiers (Asset Tags,",
         "All organisation identifiers (asset tags, stickers, etched markings) shall be removed."),
        ("A.7.6-7-14-55", "Factory Defaults",
         "Factory defaults shall be restored."),
        ("A.7.6-7-14-56", "A Record Of The External Transfer",
         "A record of the external transfer shall be maintained including recipient, date, and sanitisation evidence."),
        ("A.7.6-7-14-57", "Equipment Awaiting Sanitisation Or",
         "Equipment awaiting sanitisation or destruction shall be stored in a designated secure holding area with access limited to authorised disposal personnel."),
        ("A.7.6-7-14-58", "Chain-Of-Custody Documentation",
         "When equipment leaves the organisation's premises for destruction by an approved vendor, chain-of-custody documentation shall include:."),
        ("A.7.6-7-14-59", "Certificates Of Destruction",
         "Certificates of destruction shall be obtained from the vendor and shall include individual serial numbers for each item destroyed. Certificates shall be matched against the handover record. Any discrepancies shall be escalated immediately and logged as a security event."),
        ("A.7.6-7-14-60", "Disposal Records*",
         "Disposal records* shall include:."),
        ("A.7.6-7-14-61", "Retention: Disposal Records",
         "Retention: Disposal records, including certificates of destruction, shall be retained for 7 years*."),
        ("A.7.6-7-14-62", "A Certificate Of Destruction",
         "A certificate of destruction shall be obtained for every batch or individual item destroyed."),
        ("A.7.6-7-14-63", "Reference Individual Serial Numbers, Not",
         "Certificates shall reference individual serial numbers, not only batch identifiers."),
        ("A.7.6-7-14-64", "The Destruction Method",
         "The destruction method shall be stated on the certificate (e.g., shredding to particle size, incineration)."),
        ("A.7.6-7-14-65", "Paper Documents",
         "Paper documents containing CONFIDENTIAL or INTERNAL information shall be shredded to a minimum of DIN 66399 Security Level P-4 (or equivalent cross-cut standard)."),
        ("A.7.6-7-14-66", "Be Filed With The Corresponding Disposal",
         "Certificates shall be filed with the corresponding disposal record and retained for 7 years."),
        ("A.7.6-7-14-67", "Only Use Destruction Vendors Who",
         "The organisation shall only use destruction vendors who:."),
    ]),

    ("SOC 2 Considerations", [
        ("A.7.6-7-14-68", "Systems And Devices That Processed",
         "Systems and devices that processed customer data (CRM, application servers, databases, customer support laptops) shall be flagged in [Asset Management System] with a 'Customer Data' attribute at deployment. At disposal:."),
        ("A.7.6-7-14-69", "Roles With Disposal Responsibilities (It",
         "Roles with disposal responsibilities (IT Operations, Facilities personnel authorised for holding area access) shall be subject to background screening per A.6.1 requirements (minimum Standard level screening). Additional requirement for CONFIDENTIAL equipment disposal: Enhanced screening level (see A.6.1 screening levels table). Documented in role-to-screening-level mapping (maintained by HR + CISO)."),
    ]),

    ("Optional Payment Card Data", [
        ("A.7.6-7-14-70", "Media",
         "Media containing cardholder data shall be physically destroyed when no longer needed for business or legal reasons (PCI DSS Requirement 9.4)."),
        ("A.7.6-7-14-71", "An Inventory Of Media",
         "An inventory of media containing cardholder data shall be maintained and reconciled at least annually."),
        ("A.7.6-7-14-72", "Secure Disposal Of Cardholder Data Media",
         "Secure disposal of cardholder data media shall be documented with destruction certificates retained per PCI DSS Requirement 9.4.7."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.7.6-7-14
# =============================================================================
