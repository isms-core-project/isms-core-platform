#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.14 — Information Transfer Compliance Checklist

Control A.5.14: Information Transfer
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Information Virus Checking (1 reqs)
4. Information Encryption (2 reqs)
5. Transfer Agreements (2 reqs)
6. Data Transfer Methods (30 reqs)
7. Cross-Border Data Transfers (4 reqs)
8. Lost or Missing Information (2 reqs)

Total: 41 requirements across 6 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.5.14"
CONTROL_ID = "A.5.14"
CONTROL_NAME = "Information Transfer"
SOURCE_POLICY = "ISMS-OP-POL-A.5.14"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.14
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Information Virus Checking", [
        ("A.5.14-01", "Information That Is Transferred",
         "Information that is transferred shall be checked for malware before being sent or before being opened when received. This applies to all electronic transfers including email attachments, file transfers, and removable media."),
    ]),

    ("Information Encryption", [
        ("A.5.14-02", "Personal And Confidential Information",
         "Personal and confidential information shall always be encrypted before being transferred, in line with the Use of Cryptography Policy."),
        ("A.5.14-03", "Encryption Credentials For Username And",
         "Encryption credentials for username and password, where used, shall be shared via two separate and distinct communication methods. The preferred method is to share the access link or username via email and the password or passphrase via a voice call or secure messaging channel."),
    ]),

    ("Transfer Agreements", [
        ("A.5.14-04", "Formal Transfer Agreements",
         "Formal transfer agreements shall be established with all third-party recipients of personal or confidential data. Transfer agreements shall address:."),
        ("A.5.14-05", "Transfer Agreements",
         "Transfer agreements shall be reviewed annually or upon material changes to the transfer arrangement."),
    ]),

    ("Data Transfer Methods", [
        ("A.5.14-06", "Organisation-Approved Transfer Methods",
         "All organisation-approved transfer methods shall support:."),
        ("A.5.14-07", "For Automated Or Bulk File Transfers",
         "For automated or bulk file transfers, the following protocols shall be used:."),
        ("A.5.14-08", "Always Be Given To An Alternative",
         "Consideration shall always be given to an alternative secure method of transferring sensitive data wherever possible and practicable."),
        ("A.5.14-09", "Email Communication",
         "Email communication shall not be used to transfer unencrypted personal or confidential information."),
        ("A.5.14-10", "An Encrypted Attachment",
         "An encrypted attachment shall be used with a key length that meets the Use of Cryptography Policy requirements (AES-256 minimum)."),
        ("A.5.14-11", "The Password Or Decryption Key",
         "The password or decryption key shall be shared via a separate communication channel (voice call, secure messaging)."),
        ("A.5.14-12", "Filename Or Subject Line",
         "Filename or subject line shall not reveal the full contents of attachments or disclose any sensitive personal data."),
        ("A.5.14-13", "Email Messages",
         "Email messages containing sensitive transfers shall include clear instructions of the recipient's responsibilities and instructions on what to do if they are not the correct recipient."),
        ("A.5.14-14", "The Use Of Personal Email Accounts",
         "The use of personal email accounts for transferring organisation data is prohibited. Where technically feasible, the organisation shall implement controls to prevent forwarding of organisation email to external personal accounts (e.g., mail flow rules, DLP policies, conditional access)."),
        ("A.5.14-15", "Implement Email Domain Authentication",
         "The organisation shall implement email domain authentication (SPF, DKIM, DMARC) to protect against email spoofing and interception. DMARC policy shall be set to quarantine or reject (not none) for production domains."),
        ("A.5.14-16", "Data Transfers Which Occur Via Physical",
         "Data transfers which occur via physical media such as paper reports, memory cards, or external drives shall only be dispatched via an organisation-approved secure courier (a courier service providing tracked, signed-for delivery with tamper-evident packaging and chain of custody documentation, e.g., Swiss Post registered mail, DHL Express with signature, or equivalent). Standard postal services shall not be used for confidential or personal data."),
        ("A.5.14-17", "The Recipient",
         "The recipient shall be clearly stated on the parcel and the physical media shall be securely packaged to prevent damage or tampering. Tamper-evident packaging shall be used for confidential material."),
        ("A.5.14-18", "The Recipient",
         "The recipient shall be advised in advance that the information is being sent so that they are aware when to expect it. The recipient shall confirm safe receipt as soon as the information arrives. The sender is responsible for confirming the data has arrived safely."),
        ("A.5.14-19", "Only Organisation-Owned Removable Media",
         "Only organisation-owned removable media shall be used for transferring information, in line with the Asset Management Policy. The device shall be approved, recorded in the asset register, assigned to a user, and encrypted (AES-256 full-disk or file-level encryption). Encryption shall be verified by IT before the device is approved for confidential data transfers."),
        ("A.5.14-20", "Unencrypted Usb Drives, Personal Storage",
         "Unencrypted USB drives, personal storage devices, and unapproved cloud storage shall not be used for organisation data transfers."),
        ("A.5.14-21", "The Removable Media",
         "The removable media shall be returned to the owner on completion of the transfer and the transferred data shall be securely erased from the storage device after use. The asset register shall be updated."),
        ("A.5.14-22", "Clear Instructions Of The Recipient'S",
         "Clear instructions of the recipient's responsibilities and instructions on what to do if they are not the intended recipient shall be given."),
        ("A.5.14-23", "Any Accompanying Message Or Filename",
         "Any accompanying message or filename shall not reveal the contents of the media."),
        ("A.5.14-24", "The Process Described For Data Transfers",
         "The process described for data transfers by post or courier shall be followed for physical dispatch of removable media."),
        ("A.5.14-25", "As Phone Calls May Be Monitored",
         "As phone calls may be monitored, overheard, or intercepted (either deliberately or accidentally), care shall be taken as follows:."),
        ("A.5.14-26", "Personal Data",
         "Personal data shall not be transferred or discussed over the telephone unless you have confirmed the identity and authorisation of the recipient."),
        ("A.5.14-27", "Not Be Approved As A Communication",
         "Bluetooth shall not be approved as a communication method for unencrypted confidential, personal, or otherwise sensitive data."),
        ("A.5.14-28", "Device Mutual Authentication",
         "Device mutual authentication shall be performed for all connections."),
        ("A.5.14-29", "Be Enabled For All Transmissions",
         "Encryption shall be enabled for all transmissions."),
        ("A.5.14-30", "Bluetooth Security Mode 4, Level 3",
         "Bluetooth Security Mode 4, Level 3 (authenticated encryption) or higher shall be used. Security Modes 1 and 2 are prohibited."),
        ("A.5.14-31", "Be Set To Non-Discoverable Mode When",
         "Devices shall be set to non-discoverable mode when not actively pairing."),
        ("A.5.14-32", "Be Performed In A Secure, Non-Public",
         "Pairing shall be performed in a secure, non-public area."),
        ("A.5.14-33", "Not Accept Transmissions Of Any Kind",
         "Users shall not accept transmissions of any kind from unknown or suspicious devices."),
        ("A.5.14-34", "Bluetooth File Transfer (Obex)",
         "Bluetooth file transfer (OBEX) shall be disabled unless specifically approved."),
        ("A.5.14-35", "Bluetooth Profiles",
         "Bluetooth profiles shall be limited to those required for the approved function."),
    ]),

    ("Cross-Border Data Transfers", [
        ("A.5.14-36", "Personal Data",
         "Personal data shall not be transferred to a country outside Switzerland unless one of the following conditions is met:."),
        ("A.5.14-37", "A Register Of All Cross-Border Data",
         "A register of all cross-border data transfers shall be maintained in the organisation's GRC platform, document management system, or equivalent central location. The register shall document the recipient, destination country, legal basis, safeguards, and review date. The register shall be reviewed annually by the CISO or Data Protection Advisor."),
        ("A.5.14-38", "For Transfers To Countries Without An",
         "For transfers to countries without an adequacy decision (relying on SCCs or other safeguards), a Transfer Impact Assessment shall be conducted before the transfer commences. The TIA shall evaluate:."),
        ("A.5.14-39", "Tia Results",
         "TIA results shall be documented and approved by the CISO or Data Protection Advisor before the transfer is authorised. TIAs shall be reviewed annually or when circumstances change (legal changes in destination country, security incident)."),
    ]),

    ("Lost or Missing Information", [
        ("A.5.14-40", "Is Missing, Did Not Arrive, Or",
         "If it is discovered or suspected that information has been lost, is missing, did not arrive, or has gone to the wrong person, then the employee or third-party user shall immediately inform their line manager and the information security management team. The Incident Management process shall be followed."),
        ("A.5.14-41", "Lost Or Misdirected Information",
         "Lost or misdirected information shall be classified as:."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.14
# =============================================================================
