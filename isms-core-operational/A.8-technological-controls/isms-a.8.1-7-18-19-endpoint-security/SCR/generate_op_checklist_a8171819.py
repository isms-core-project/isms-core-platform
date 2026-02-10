#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.1-7-18-19 — Endpoint Security Compliance Checklist

Controls A.8.1-7-18-19: Endpoint Security
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. User Endpoint Devices (26 reqs)
4. Malware and Antivirus Prot (12 reqs)
5. Education (1 reqs)
6. Privileged Utility Programs (6 reqs)
7. Installation Software Op (11 reqs)

Total: 56 requirements across 5 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.1-7-18-19"
CONTROL_ID = "A.8.1-7-18-19"
CONTROL_NAME = "Endpoint Security"
SOURCE_POLICY = "ISMS-OP-POL-A.8.1-7-18-19"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.1-7-18-19
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("User Endpoint Devices", [
        ("A.8.1-7-18-19-01", "Endpoint Devices",
         "All endpoint devices shall be registered in the asset register before being issued to users. The register shall record the device type, serial number, assigned user, operating system, encryption status, and issue date."),
        ("A.8.1-7-18-19-02", "Devices That Are Lost, Stolen,",
         "Devices that are lost, stolen, decommissioned, or reassigned shall be updated in the asset register promptly."),
        ("A.8.1-7-18-19-03", "Endpoint Devices",
         "All endpoint devices shall be configured to a documented security baseline before deployment. The baseline shall include:."),
        ("A.8.1-7-18-19-04", "The Configuration Baseline",
         "The configuration baseline shall be documented and version-controlled. Baseline standards shall reference vendor hardening guides and CIS Benchmarks. The baseline shall be reviewed at least annually or when significant changes occur to the operating system or threat landscape."),
        ("A.8.1-7-18-19-05", "The Following Categories Of Management",
         "The following categories of management tools shall be deployed to support endpoint security:."),
        ("A.8.1-7-18-19-06", "Endpoint Devices (Laptops, Desktops,",
         "All endpoint devices (laptops, desktops, mobile devices) shall have full-disk encryption enabled:."),
        ("A.8.1-7-18-19-07", "Device Encryption",
         "Device encryption shall not be disabled by the end user."),
        ("A.8.1-7-18-19-08", "Recovery Keys",
         "Recovery keys shall be escrowed centrally via MDM (e.g., Jamf Pro, Intune, or equivalent) or equivalent key escrow solution managed by IT. Recovery key access shall be logged and restricted to authorised IT personnel."),
        ("A.8.1-7-18-19-09", "Encryption Status",
         "Encryption status shall be verified before the device is approved for use with confidential data."),
        ("A.8.1-7-18-19-10", "Lock Automatically After 15 Minutes Of",
         "Devices shall lock automatically after 15 minutes of inactivity. Devices with access to confidential or sensitive personal data shall lock after 5 minutes of inactivity."),
        ("A.8.1-7-18-19-11", "Lock Their Devices Manually When Leaving",
         "Users shall lock their devices manually when leaving them unattended (Windows+L, Ctrl+Command+Q, or equivalent)."),
        ("A.8.1-7-18-19-12", "Authentication (Password, Pin, Or",
         "Authentication (password, PIN, or biometric) shall be required to unlock."),
        ("A.8.1-7-18-19-13", "Lock On Sleep And Lid-Close",
         "Lock on sleep and lid-close shall be enabled on all laptops."),
        ("A.8.1-7-18-19-14", "Not Be Left Unattended In Public",
         "Devices shall not be left unattended in public places or visible in unattended vehicles."),
        ("A.8.1-7-18-19-15", "Portable Devices",
         "Portable devices shall be stored securely when not in use (locked drawer or cabinet)."),
        ("A.8.1-7-18-19-16", "Loss Or Theft Of Any Device",
         "Loss or theft of any device shall be reported immediately to the information security management team."),
        ("A.8.1-7-18-19-17", "Maintain The Capability To Remotely Wipe",
         "The organisation shall maintain the capability to remotely wipe or lock lost or stolen devices via the MDM platform or equivalent management tool."),
        ("A.8.1-7-18-19-18", "Remote Wipe Confirmation",
         "Remote wipe confirmation shall be documented, including the date, device ID, wipe status (confirmed/pending), and authorising person."),
        ("A.8.1-7-18-19-19", "Only The Organisation Container Or Work",
         "Where a BYOD device is wiped, only the organisation container or work profile shall be erased (not personal data), unless the employee has consented to full wipe in the BYOD agreement."),
        ("A.8.1-7-18-19-20", "The Following Requirements",
         "If the organisation permits personally-owned devices to access organisation information, the following requirements shall apply:."),
        ("A.8.1-7-18-19-21", "The Device",
         "The device shall be enrolled in the organisation's mobile device management (MDM) solution."),
        ("A.8.1-7-18-19-22", "Business Data",
         "Business data shall be separated from personal data using containerisation or a managed work profile."),
        ("A.8.1-7-18-19-23", "The Device",
         "The device shall meet the same security baseline as organisation-owned devices (encryption, screen lock, current OS, malware protection)."),
        ("A.8.1-7-18-19-24", "Acknowledge Their Responsibilities",
         "Users shall acknowledge their responsibilities, including physical protection, software updates, and cooperation with security requirements."),
        ("A.8.1-7-18-19-25", "Byod Access",
         "BYOD access shall be revoked on termination or contract end per the Access Control Policy."),
        ("A.8.1-7-18-19-26", "Be Stated And Enforced Through Technical",
         "If BYOD is not permitted, this shall be stated and enforced through technical controls."),
    ]),

    ("Malware and Antivirus Prot", [
        ("A.8.1-7-18-19-27", "Only Organisation-Approved And Licensed",
         "Only organisation-approved and licensed software shall be installed on organisation equipment."),
        ("A.8.1-7-18-19-28", "Unauthorised Software, Downloaded",
         "Unauthorised software, downloaded software, freeware, or unapproved utilities shall not be installed."),
        ("A.8.1-7-18-19-29", "Malware Protection Software (Endpoint",
         "Malware protection software (endpoint detection and response — EDR, or next-generation antivirus — NGAV, as appropriate to the organisation's risk profile) shall be installed on every device that can run it."),
        ("A.8.1-7-18-19-30", "Malware Protection Software",
         "Malware protection software shall:."),
        ("A.8.1-7-18-19-31", "Suspected Infections",
         "Suspected infections shall be managed via the Incident Management process. The following events shall trigger an incident report:."),
        ("A.8.1-7-18-19-32", "Email Servers And Gateways",
         "Email servers and gateways shall have malware scanning that inspects all inbound and outbound email, including attachments."),
        ("A.8.1-7-18-19-33", "Internet Proxies Or Secure Web Gateways",
         "Internet proxies or secure web gateways shall be configured to:."),
        ("A.8.1-7-18-19-34", "Allow-Listing And Deny-Listing",
         "Allow-listing and deny-listing shall be deployed to control access to approved and prohibited web resources."),
        ("A.8.1-7-18-19-35", "File Integrity Monitoring",
         "File integrity monitoring shall be implemented for system-critical files and files that contain or provide access to personal or confidential data, based on risk and business need."),
        ("A.8.1-7-18-19-36", "Autorun And Autoplay",
         "Autorun and autoplay shall be disabled for all removable media."),
        ("A.8.1-7-18-19-37", "Removable Media",
         "Removable media shall be automatically scanned for malware when connected."),
        ("A.8.1-7-18-19-38", "Only Organisation-Owned, Encrypted",
         "Only organisation-owned, encrypted removable media shall be approved for use with confidential data, in line with the Information Transfer Policy."),
    ]),

    ("Education", [
        ("A.8.1-7-18-19-39", "Be Educated Periodically As Part Of",
         "Users shall be educated periodically as part of the security awareness programme on:."),
    ]),

    ("Privileged Utility Programs", [
        ("A.8.1-7-18-19-40", "Access To Privileged Utility Programs",
         "Access to privileged utility programs shall be restricted to authorised personnel only, based on the principle of least privilege."),
        ("A.8.1-7-18-19-41", "Multi-Factor Authentication",
         "Multi-factor authentication shall be required for accessing privileged utility programs on critical systems."),
        ("A.8.1-7-18-19-42", "Execution Of Privileged Utility Programs",
         "All execution of privileged utility programs shall be logged, including the user, timestamp, utility name, and target system."),
        ("A.8.1-7-18-19-43", "Privileged Utility Programs That Are Not",
         "Privileged utility programs that are not required for operational purposes shall be removed or disabled."),
        ("A.8.1-7-18-19-44", "The Use Of Privileged Utility Programs",
         "The use of privileged utility programs shall be subject to periodic review (at least quarterly) to verify continued business justification."),
        ("A.8.1-7-18-19-45", "Maintain A Documented List Of Approved",
         "The organisation shall maintain a documented list of approved privileged utility programs by role."),
    ]),

    ("Installation Software Op", [
        ("A.8.1-7-18-19-46", "Software Installation On Operational",
         "Software installation on operational systems shall be performed only by authorised personnel (IT administrators or designated support staff)."),
        ("A.8.1-7-18-19-47", "Standard Users",
         "Standard users shall not have local administrator rights. Where elevation is required, a managed privilege escalation mechanism shall be used:."),
        ("A.8.1-7-18-19-48", "Privilege Escalations",
         "All privilege escalations shall be logged (user, timestamp, justification, duration, approver)."),
        ("A.8.1-7-18-19-49", "Software Installations",
         "All software installations shall follow the organisation's change management process, including testing, approval, and documentation."),
        ("A.8.1-7-18-19-50", "Only Approved Software From The",
         "Only approved software from the organisation's software catalogue shall be installed. New software requests shall be submitted through a formal approval process."),
        ("A.8.1-7-18-19-51", "Operating Systems, Applications, And",
         "Operating systems, applications, and browser software on endpoint devices shall be kept up to date. Security patches shall be applied according to the following timelines:."),
        ("A.8.1-7-18-19-52", "Be Tested Before Deployment Using The",
         "Patches shall be tested before deployment using the following approach:."),
        ("A.8.1-7-18-19-53", "Patch Failure Handling: If A Patch",
         "Patch failure handling: If a patch causes operational issues in the pilot group, deployment shall be halted, the issue documented, and the vendor contacted. A workaround or compensating control shall be applied until a stable patch is available."),
        ("A.8.1-7-18-19-54", "Automatic Updates",
         "Automatic updates shall be enabled for operating systems and supported applications. Devices that have not applied critical patches within the defined timeframe shall be flagged for remediation or restricted from network access."),
        ("A.8.1-7-18-19-55", "A Rollback Strategy",
         "A rollback strategy shall be agreed upon before applying updates or installations to operational systems to ensure business continuity if a patch causes issues."),
        ("A.8.1-7-18-19-56", "A Record Of All Software Changes",
         "A record of all software changes on operational systems shall be maintained, including the software name, version, date of installation, and the individual who performed the change."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.1-7-18-19
# =============================================================================
