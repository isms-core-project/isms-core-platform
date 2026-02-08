#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.20-22 — Network Security Compliance Checklist

Controls A.8.20-22: Network Security
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Network Controls (10 reqs)
4. Security of Network Services (3 reqs)
5. Segregation in Networks (27 reqs)
6. Access Networks & Network (4 reqs)
7. Remote Access (5 reqs)
8. Network Locations (4 reqs)
9. Physical Network Devices (3 reqs)
10. Web Filtering (4 reqs)
11. Host Intrusion, Network (4 reqs)

Total: 64 requirements across 9 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/SCR/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_OP_ROOT / 'SCR'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.8.20-22"
CONTROL_ID = "A.8.20-22"
CONTROL_NAME = "Network Security"
SOURCE_POLICY = "ISMS-OP-POL-A.8.20-22"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.20-22
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Network Controls", [
        ("A.8.20-22-01", "Responsibilities And Procedures For The",
         "Responsibilities and procedures for the management of networking equipment shall be established and documented."),
        ("A.8.20-22-02", "Operational Responsibility For Networks",
         "Operational responsibility for networks shall be separated from computer operations where appropriate."),
        ("A.8.20-22-03", "Special Controls",
         "Special controls shall be established to safeguard the confidentiality and integrity of data passing over public networks or over wireless networks and to protect the connected systems and applications."),
        ("A.8.20-22-04", "Appropriate Logging And Monitoring",
         "Appropriate logging and monitoring shall be applied to enable recording and detection of actions that may affect, or are relevant to, information security."),
        ("A.8.20-22-05", "Management Activities",
         "Management activities shall be closely coordinated both to optimise the service to the organisation and to ensure that controls are consistently applied across the information processing infrastructure."),
        ("A.8.20-22-06", "Systems On The Network",
         "Systems on the network shall be authenticated before being granted access."),
        ("A.8.20-22-07", "System Connections To The Network",
         "System connections to the network shall be restricted to authorised and compliant devices."),
        ("A.8.20-22-08", "Network Device Default Passwords And",
         "Network device default passwords and accounts shall be changed or disabled before deployment."),
        ("A.8.20-22-09", "Administrative Access To Network Devices",
         "Administrative access to network devices shall use encrypted management protocols (SSH, HTTPS). Telnet and unencrypted SNMP (v1/v2c) shall not be used."),
        ("A.8.20-22-10", "Network Device Firmware And Software",
         "Network device firmware and software shall be maintained at current, vendor-supported versions. Security patches shall be applied according to the following timelines:."),
    ]),

    ("Security of Network Services", [
        ("A.8.20-22-11", "Security Mechanisms, Service Levels, And",
         "Security mechanisms, service levels, and management requirements of all network services shall be identified and included in network services agreements, whether these services are provided in-house or outsourced."),
        ("A.8.20-22-12", "The Ability Of The Network Service",
         "The ability of the network service provider to manage agreed services in a secure way shall be determined and regularly monitored, and the right to audit shall be agreed."),
        ("A.8.20-22-13", "The Security Arrangements Necessary For",
         "The security arrangements necessary for particular services, such as security features, service levels, and management requirements, shall be identified. The organisation shall ensure that network service providers implement these measures."),
    ]),

    ("Segregation in Networks", [
        ("A.8.20-22-14", "Large Networks",
         "Large networks shall be divided into separate network domains. The domains shall be chosen based on trust levels, data classification, and business function."),
        ("A.8.20-22-15", "The Perimeter Of Each Domain",
         "The perimeter of each domain shall be well defined. Access between network domains shall be controlled at the perimeter using a gateway (e.g., firewall, filtering router) with a default-deny posture."),
        ("A.8.20-22-16", "The Criteria For Segregation Of Networks",
         "The criteria for segregation of networks into domains, and the access allowed through the gateways, shall be based on an assessment of the security requirements of each domain. The assessment shall be in accordance with the access control policy, access requirements, value and classification of information processed, and shall take account of the relative cost and performance impact of incorporating suitable gateway technology."),
        ("A.8.20-22-17", "Firewall Rule Changes",
         "All firewall rule changes shall follow a documented change management process with business justification and approval."),
        ("A.8.20-22-18", "Firewall Rule Sets",
         "Firewall rule sets shall be reviewed at least annually to remove obsolete rules and verify continued business justification."),
        ("A.8.20-22-19", "Be Documented With Sign-Off From The",
         "Reviews shall be documented with sign-off from the network administrator and CISO."),
        ("A.8.20-22-20", "Default-Deny Policy",
         "Default-deny policy shall be verified during each review (all traffic blocked unless explicitly permitted)."),
        ("A.8.20-22-21", "Minimum Network Segments",
         "Minimum network segments shall include:."),
        ("A.8.20-22-22", "Additional Segments (E.G., Dmz For",
         "Additional segments (e.g., DMZ for public-facing services, development/test environments) shall be created based on risk assessment."),
        ("A.8.20-22-23", "Guest Networks",
         "Guest networks shall be configured with the following security controls:."),
        ("A.8.20-22-24", "Isolation: No Access To Corporate",
         "Isolation: No access to corporate network segments (firewall rules shall enforce separation)."),
        ("A.8.20-22-25", "Internet-Only Access: Guests",
         "Internet-only access: Guests shall access only the Internet, not internal resources."),
        ("A.8.20-22-26", "Time-Limited Access: Guest Credentials",
         "Time-limited access: Guest credentials shall expire after a defined period (e.g., 24 hours) and be reissued as needed."),
        ("A.8.20-22-27", "Monitoring: Guest Network Traffic",
         "Monitoring: Guest network traffic shall be logged for security investigation if needed."),
        ("A.8.20-22-28", "The Guest Network Passphrase",
         "The guest network passphrase shall be changed at least quarterly or immediately if compromise is suspected."),
        ("A.8.20-22-29", "Iot (Internet Of Things) And Ot",
         "IoT (Internet of Things) and OT (Operational Technology) devices shall be placed on an isolated network segment with the following controls:."),
        ("A.8.20-22-30", "Iot/Ot Devices",
         "IoT/OT devices shall not have direct, uncontrolled Internet access. Internet communication shall be routed via a proxy or gateway with whitelisted destinations."),
        ("A.8.20-22-31", "Iot/Ot Devices",
         "IoT/OT devices shall not be accessible from the Internet without VPN and explicit authorisation."),
        ("A.8.20-22-32", "Access From The Corporate Network To",
         "Access from the corporate network to the IoT/OT segment shall be restricted to authorised personnel via firewall rules."),
        ("A.8.20-22-33", "Third-Party Vendor Remote Access To",
         "Third-party vendor remote access to IoT/OT devices shall require approval, VPN, and time-limited credentials."),
        ("A.8.20-22-34", "Iot/Ot Device Default Passwords",
         "All IoT/OT device default passwords shall be changed before deployment."),
        ("A.8.20-22-35", "Iot/Ot Devices",
         "All IoT/OT devices shall be registered in the asset register with owner, purpose, and network location."),
        ("A.8.20-22-36", "Wireless Networks Require Special",
         "Wireless networks require special treatment due to the poorly defined network perimeter. For sensitive environments, all wireless access shall be treated as external connections and segregated from internal networks until the access has passed through a gateway before granting access to internal systems."),
        ("A.8.20-22-37", "Wireless Network Access For Personnel",
         "Wireless network access for personnel and guests shall be segregated on separate SSIDs with distinct security controls."),
        ("A.8.20-22-38", "The Following Wireless Security",
         "The following wireless security standards shall apply:."),
        ("A.8.20-22-39", "Not Be Used Under Any Circumstances",
         "WEP shall not be used under any circumstances."),
        ("A.8.20-22-40", "Wpa (Original) And Tkip Encryption",
         "WPA (original) and TKIP encryption shall not be used."),
    ]),

    ("Access Networks & Network", [
        ("A.8.20-22-41", "Only Be Provided With Access To",
         "Users shall only be provided with access to the network and network services that they have been specifically authorised to use."),
        ("A.8.20-22-42", "Access To Networks And Network Services",
         "Access to networks and network services shall be in line with the Access Control Policy."),
        ("A.8.20-22-43", "Before Connecting To The Network,",
         "Before connecting to the network, devices shall have:."),
        ("A.8.20-22-44", "Implement Technical Controls To Enforce",
         "The organisation shall implement technical controls to enforce device compliance before granting network access. Enforcement mechanisms include network access control (NAC) solutions, 802.1X certificate or credential-based authentication, VPN gateway posture assessment, or manual registration and approval by IT. Non-compliant devices shall be placed in a quarantine or restricted segment until compliance is achieved."),
    ]),

    ("Remote Access", [
        ("A.8.20-22-45", "Remote Access To The Organisation",
         "Remote access to the organisation network shall be secured using encrypted tunnels (VPN or equivalent) with multi-factor authentication."),
        ("A.8.20-22-46", "Vpn Connections",
         "VPN connections shall use current, secure protocols:."),
        ("A.8.20-22-47", "Pptp And L2Tp Without Ipsec",
         "PPTP and L2TP without IPsec shall not be used."),
        ("A.8.20-22-48", "Remote Connections",
         "Remote connections shall be set to disconnect after a defined period of inactivity."),
        ("A.8.20-22-49", "A List Of Users With Remote",
         "A list of users with remote access shall be maintained and reviewed quarterly."),
    ]),

    ("Network Locations", [
        ("A.8.20-22-50", "Network Infrastructure And Data",
         "Network infrastructure and data processing locations shall be selected based on risk assessment, data classification, and applicable data protection requirements."),
        ("A.8.20-22-51", "The Following Hierarchy Of Preference",
         "The following hierarchy of preference shall apply for the location of network infrastructure, data centres, and cloud services processing personal or confidential data:."),
        ("A.8.20-22-52", "Within Countries Recognised By The Swiss",
         "Within countries recognised by the Swiss Federal Council as providing adequate data protection per Annex 1 of the Data Protection Ordinance (DSV). The current adequacy list is published by the Federal Data Protection and Information Commissioner (FDPIC) and shall be verified before deploying infrastructure or services in a new jurisdiction."),
        ("A.8.20-22-53", "Cross-Border Data Transfers",
         "Cross-border data transfers shall comply with the Information Transfer Policy and nFADP requirements. Legal counsel shall verify the adequacy status of any country before deployment."),
    ]),

    ("Physical Network Devices", [
        ("A.8.20-22-54", "Physical Network Devices",
         "Physical network devices shall be managed in line with the Physical and Environmental Security Policy, specifically the sections on cabling security, equipment siting and protection, and access control."),
        ("A.8.20-22-55", "Physical Network Devices",
         "Physical network devices shall be destroyed in line with the Information Classification and Handling Policy, specifically the section on the destruction of electronic media and devices."),
        ("A.8.20-22-56", "Physical Network Devices",
         "Physical network devices shall be managed in line with the Asset Management Policy and subject to the asset management process."),
    ]),

    ("Web Filtering", [
        ("A.8.20-22-57", "Access To Websites",
         "Access to websites containing illegal information or known to contain malicious content shall be restricted."),
        ("A.8.20-22-58", "Access To The Following Types Of",
         "Access to the following types of websites shall be blocked where practicable:."),
        ("A.8.20-22-59", "Web Filtering",
         "Web filtering shall be implemented using DNS-based filtering, web proxy, or equivalent technology. Filter categories and exceptions shall be reviewed quarterly."),
        ("A.8.20-22-60", "Internal Dns Zones",
         "Internal DNS zones shall not be exposed to the Internet. Split-horizon DNS is recommended for organisations with internal and external name resolution."),
    ]),

    ("Host Intrusion, Network", [
        ("A.8.20-22-61", "Network Services And Devices",
         "Network services and devices shall be managed in line with the Malware and Antivirus Policy."),
        ("A.8.20-22-62", "Host Intrusion Detection And Network",
         "Host intrusion detection and network intrusion detection/prevention shall be deployed based on risk, business need, and where practical to do so."),
        ("A.8.20-22-63", "Additional Deployment Locations",
         "Additional deployment locations shall be determined by risk assessment. Where dedicated IDS/IPS appliances are not feasible, equivalent detection capabilities (e.g., EDR with network visibility, cloud-native security tools) are acceptable."),
        ("A.8.20-22-64", "Network Traffic",
         "Network traffic shall be monitored for anomalous behaviour. Security alerts shall be triaged and escalated per the Incident Management process."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.20-22
# =============================================================================
