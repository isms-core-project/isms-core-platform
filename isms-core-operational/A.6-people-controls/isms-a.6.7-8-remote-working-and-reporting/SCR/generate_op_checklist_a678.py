#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.6.7-8 — Remote Working and Security Event Reporting Compliance Checklist

Controls A.6.7-8: Remote Working and Security Event Reporting
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Remote Work Authorisation (6 reqs)
4. Mobile Device Reg and Resp (4 reqs)
5. Remote Wipe and Backup (2 reqs)
6. Physical Security (3 reqs)
7. Technical Security (7 reqs)
8. Data Handling (2 reqs)
9. Corporate and BYOD Device Reqs (7 reqs)
10. Remote Work Termination (5 reqs)
11. Reporting Channels (5 reqs)
12. Non-Blame Culture (1 reqs)
13. Response and Feedback (2 reqs)
14. Reporting Metrics (3 reqs)
15. Remote Work Compliance Verif (1 reqs)

Total: 48 requirements across 13 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.6.7-8"
CONTROL_ID = "A.6.7-8"
CONTROL_NAME = "Remote Working and Security Event Reporting"
SOURCE_POLICY = "ISMS-OP-POL-A.6.7-8"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.6.7-8
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Remote Work Authorisation", [
        ("A.6.7-8-01", "Regular Remote Work Arrangements",
         "All regular remote work arrangements shall be formally approved before commencement."),
        ("A.6.7-8-02", "Risk Assessment: A Risk Assessment",
         "Risk assessment: A risk assessment shall be performed for roles that handle Confidential or Restricted data remotely. The assessment shall evaluate at minimum: (a) classification level of data accessed remotely; (b) physical security capability of the remote location; (c) network security posture at the remote site; (d) device security baseline compliance; and (e) any regulatory or contractual restrictions."),
        ("A.6.7-8-03", "Documented Acknowledgment: Remote",
         "Documented acknowledgment: Remote workers shall sign an acknowledgment confirming they understand and accept the security requirements in this policy."),
        ("A.6.7-8-04", "Annual Review: All Remote Work",
         "Annual review: All remote work authorisations shall be reviewed at least annually. Reviews shall confirm that the authorisation remains appropriate, security requirements are maintained, and any changes to role, data access, or work location are reflected."),
        ("A.6.7-8-05", "Location Changes: Permanent Changes To",
         "Location changes: Permanent changes to remote work location (e.g., move to new home, extended travel) shall be reported to line manager and IT Security within 14 days*."),
        ("A.6.7-8-06", "Revocation*: Remote Work Authorisation",
         "Revocation*: Remote work authorisation shall be revoked when employment or contract terminates, the role changes to one unsuitable for remote work, security requirements are not maintained, policy violations occur, or business needs require on-premises presence."),
    ]),

    ("Mobile Device Reg and Resp", [
        ("A.6.7-8-07", "Mobile Devices Issued Or Approved For",
         "Mobile devices issued or approved for remote work shall be recorded in the asset register and assigned to a named individual."),
        ("A.6.7-8-08", "Mobile Devices (Corporate And Approved",
         "All mobile devices (corporate and approved BYOD) shall be registered in the asset register with the assigned owner, device type, serial number, and purpose."),
        ("A.6.7-8-09", "Assigned Owners",
         "Assigned owners shall receive a copy of this policy and be informed of their responsibilities."),
        ("A.6.7-8-10", "Have Appropriate Encryption,",
         "Devices shall have appropriate encryption, anti-virus/endpoint protection, and access controls installed."),
    ]),

    ("Remote Wipe and Backup", [
        ("A.6.7-8-11", "Remote Wipe: All Corporate Mobile",
         "Remote wipe: All corporate mobile devices shall have remote wipe capability enabled before the device is issued to the user. Automatic lockout shall be enabled (maximum 5 failed authentication attempts)."),
        ("A.6.7-8-12", "Backup: Mobile Devices Are Not Backed",
         "Backup: Mobile devices are not backed up by default to corporate backup solutions. Users shall store work files in approved cloud or network locations (e.g., SharePoint, OneDrive for Business, approved file server). Critical work data shall not reside solely on local device storage."),
    ]),

    ("Physical Security", [
        ("A.6.7-8-13", "Remote Workers",
         "Remote workers shall maintain physical security appropriate to the classification of information being handled:."),
        ("A.6.7-8-14", "Clear Desk: The Clear Desk Policy",
         "Clear desk: The clear desk policy (A.7.7 — see Physical and Environmental Security Policy) extends to remote work environments. Sensitive documents shall not be left visible when not actively in use. Work materials shall be secured at the end of each work session."),
        ("A.6.7-8-15", "Document Disposal: Sensitive Documents",
         "Document disposal: Sensitive documents shall be disposed of using approved methods (shredding). Where a shredder is not available at the remote location, sensitive documents shall be returned to the office for secure disposal."),
    ]),

    ("Technical Security", [
        ("A.6.7-8-16", "The Following Technical Security",
         "The following technical security controls shall apply to all remote access:."),
        ("A.6.7-8-17", "Vpn Or Zero Trust: All Connections",
         "VPN or Zero Trust: All connections to internal organisational resources shall use a VPN or equivalent Zero Trust architecture. Split tunnelling may be permitted only where a risk assessment demonstrates acceptable residual risk and all organisational resources are accessed via the encrypted tunnel."),
        ("A.6.7-8-18", "Multi-Factor Authentication (Mfa): Mfa",
         "Multi-factor authentication (MFA): MFA shall be required for all remote access to organisational systems. This includes VPN connections, cloud services, email, and any system containing Internal, Confidential, or Restricted data."),
        ("A.6.7-8-19", "Encryption In Transit: All Data",
         "Encryption in transit: All data transmitted between remote endpoints and organisational systems shall be encrypted using TLS 1.2 as a minimum (TLS 1.3 preferred)."),
        ("A.6.7-8-20", "Wi-Fi Security: Remote Workers",
         "Wi-Fi security: Remote workers shall use only secure, encrypted wireless networks (WPA2 minimum, WPA3 preferred)."),
        ("A.6.7-8-21", "Prohibited Without Vpn: Public,",
         "Prohibited without VPN: Public, unsecured Wi-Fi (airports, hotels, cafes) shall not be used for organisational work without VPN protection."),
        ("A.6.7-8-22", "Session Timeout: Remote Access Sessions",
         "Session timeout: Remote access sessions shall be configured to disconnect after a defined period of inactivity (maximum 15 minutes for systems handling Confidential or Restricted data; maximum 30 minutes for other systems)."),
    ]),

    ("Data Handling", [
        ("A.6.7-8-23", "Remote Workers",
         "Remote workers shall handle data according to its classification level per the Information Classification and Handling Policy:."),
        ("A.6.7-8-24", "Remote Workers",
         "Remote workers shall follow the Information Transfer Policy when sending or receiving organisational data from remote locations. Organisational data shall not be transferred to personal cloud storage, personal email accounts, or unapproved file sharing services."),
    ]),

    ("Corporate and BYOD Device Reqs", [
        ("A.6.7-8-25", "Corporate-Issued Devices Used For Remote",
         "Corporate-issued devices used for remote work shall:."),
        ("A.6.7-8-26", "The Device",
         "The device shall be registered in the asset register."),
        ("A.6.7-8-27", "The User",
         "The user shall receive training and sign an acknowledgment of responsibility."),
        ("A.6.7-8-28", "Organisation Policies",
         "All organisation policies, including this policy and the Access Control Policy, shall apply."),
        ("A.6.7-8-29", "An Mdm (Mobile Device Management) Or",
         "An MDM (mobile device management) or containerisation solution shall be installed to separate personal and organisational data."),
        ("A.6.7-8-30", "No Personal Data Or Sensitive Personal",
         "No personal data or sensitive personal data (per nFADP) shall be stored on the device outside the managed container."),
        ("A.6.7-8-31", "The Following",
         "The following shall not be used for organisational work:."),
    ]),

    ("Remote Work Termination", [
        ("A.6.7-8-32", "Remote Access Credentials",
         "Remote access credentials shall be revoked immediately (same day)."),
        ("A.6.7-8-33", "Vpn And Remote Access Tokens",
         "VPN and remote access tokens shall be disabled."),
        ("A.6.7-8-34", "Organisational Equipment",
         "All organisational equipment shall be returned per the Return of Assets Policy (A.5.11)."),
        ("A.6.7-8-35", "Organisational Data",
         "All organisational data shall be removed from personal devices. For BYOD devices, the MDM remote wipe of the organisational container shall be executed."),
        ("A.6.7-8-36", "Return And Data Removal",
         "Return and data removal shall be verified and documented."),
    ]),

    ("Reporting Channels", [
        ("A.6.7-8-37", "Provide Accessible Mechanisms For All",
         "The organisation shall provide accessible mechanisms for all personnel to report observed or suspected information security events."),
        ("A.6.7-8-38", "At Least Two Distinct Reporting Channels",
         "At least two distinct reporting channels shall be available."),
        ("A.6.7-8-39", "At Least One Channel",
         "At least one channel shall be available outside business hours (24/7)."),
        ("A.6.7-8-40", "Be Accessible From Remote Locations",
         "All channels shall be accessible from remote locations without requiring access to internal systems (to allow reporting of access-related events)."),
        ("A.6.7-8-41", "Publication*: Reporting Channels",
         "Publication*: Reporting channels shall be published on the intranet, included in employee onboarding materials, referenced in annual security awareness training, and displayed on login screens or desktop wallpapers."),
    ]),

    ("Non-Blame Culture", [
        ("A.6.7-8-42", "Recognise And Encourage Exemplary",
         "The organisation shall recognise and encourage exemplary reporting behaviour. Reported events shall be used as learning opportunities, not as triggers for punishment."),
    ]),

    ("Response and Feedback", [
        ("A.6.7-8-43", "Respond To All Security Event Reports",
         "The organisation shall respond to all security event reports within defined timeframes:."),
        ("A.6.7-8-44", "The Organisation",
         "The organisation shall:."),
    ]),

    ("Reporting Metrics", [
        ("A.6.7-8-45", "Track The Following Security Event",
         "The organisation shall track the following security event reporting metrics:."),
        ("A.6.7-8-46", "Be Reported To The Ciso Monthly",
         "Metrics shall be reported to the CISO monthly and to the Management Review Team quarterly."),
        ("A.6.7-8-47", "Event Reporting Kpis Integrated Into",
         "Event reporting KPIs integrated into awareness training*: Annual training shall include reporting volume and success stories to reinforce the non-blame culture."),
    ]),

    ("Remote Work Compliance Verif", [
        ("A.6.7-8-48", "Remote Work Security Compliance",
         "Remote work security compliance shall be verified through:."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.6.7-8
# =============================================================================
