#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.10-11 — Acceptable Use and Return of Assets Compliance Checklist

Controls A.5.10-11: Acceptable Use and Return of Assets
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Individual Responsibility (2 reqs)
4. Internet and Email Usage (1 reqs)
5. Cloud and SaaS Services (4 reqs)
6. Artificial Intelligence Tools (7 reqs)
7. Social Media (4 reqs)
8. Working Off-Site (8 reqs)
9. Removable Storage Devices (2 reqs)
10. Monitoring and Filtering (7 reqs)
11. Reporting (1 reqs)
12. Return of Assets (17 reqs)

Total: 53 requirements across 10 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.5.10-11"
CONTROL_ID = "A.5.10-11"
CONTROL_NAME = "Acceptable Use and Return of Assets"
SOURCE_POLICY = "ISMS-OP-POL-A.5.10-11"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.10-11
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Individual Responsibility", [
        ("A.5.10-11-01", "Not",
         "Individuals shall not:."),
        ("A.5.10-11-02", "Line Managers",
         "Line managers shall ensure that individuals are given clear direction on the extent and limits of their authority regarding IT systems and data."),
    ]),

    ("Internet and Email Usage", [
        ("A.5.10-11-03", "Not",
         "Individuals shall not:."),
    ]),

    ("Cloud and SaaS Services", [
        ("A.5.10-11-04", "Organisation Data",
         "Organisation data shall only be processed in sanctioned cloud and SaaS services that have been assessed and approved by the information security management team. The sanctioned services register is maintained in the organisation's GRC platform, document management system, or intranet and shall be accessible to all employees. Employees shall verify a service is on the sanctioned list before storing organisation data."),
        ("A.5.10-11-05", "Not",
         "Individuals shall not:."),
        ("A.5.10-11-06", "Individuals",
         "When using sanctioned cloud services, individuals shall:."),
        ("A.5.10-11-07", "Unsanctioned Cloud Services (Shadow It)",
         "Unsanctioned cloud services (shadow IT) discovered in use shall be reported to the information security management team for assessment. Where an unsanctioned service is found to process personal or confidential data, it shall be treated as a security event."),
    ]),

    ("Artificial Intelligence Tools", [
        ("A.5.10-11-08", "The Use Of Generative Ai Tools",
         "The use of generative AI tools (e.g., ChatGPT, Copilot, Claude, Gemini, or equivalent) shall be governed by the following rules."),
        ("A.5.10-11-09", "Maintain A List Of Approved Ai",
         "The organisation shall maintain a list of approved AI tools for business use. Only approved tools with appropriate data protection agreements shall be used for processing organisation information."),
        ("A.5.10-11-10", "Request Process: Users Requiring New Ai",
         "Request process: Users requiring new AI tools shall submit a request to the information security management team with business justification and tool details. Assessment shall be completed within 14 business days*."),
        ("A.5.10-11-11", "Public Or Free-Tier Ai Tools Without",
         "Public or free-tier AI tools without enterprise data protection agreements shall not be used for organisation data."),
        ("A.5.10-11-12", "The Following Information",
         "The following information shall never be entered into any AI tool (including approved tools) unless the tool has been specifically assessed and approved for that data category:."),
        ("A.5.10-11-13", "Users Remain Accountable For All",
         "Users remain accountable for all AI-generated content. AI-generated outputs shall be reviewed for accuracy, bias, and appropriateness before use in business decisions, external communications, or official documents."),
        ("A.5.10-11-14", "Ai-Generated Content",
         "AI-generated content shall not be presented as human-authored work in contexts where this distinction matters (e.g., regulatory submissions, legal documents, audit evidence)."),
    ]),

    ("Social Media", [
        ("A.5.10-11-15", "Exercise Professional Judgement When",
         "Individuals shall exercise professional judgement when using social media in any context that could be associated with the organisation."),
        ("A.5.10-11-16", "Not",
         "Individuals shall not:."),
        ("A.5.10-11-17", "Official Organisation Social Media",
         "Official organisation social media accounts shall be managed only by authorised personnel. Content published on behalf of the organisation shall follow approved communication guidelines."),
        ("A.5.10-11-18", "Defamation)",
         "If an employee makes a post that creates reputational risk*: the employee shall immediately inform their manager and the communications team. The organisation reserves the right to request removal of the post or public clarification. Disciplinary action may result for serious violations (breach of confidentiality, defamation)."),
    ]),

    ("Working Off-Site", [
        ("A.5.10-11-19", "Laptops And Mobile Devices May Be",
         "Laptops and mobile devices may be taken off-site for business purposes. The following controls shall apply:."),
        ("A.5.10-11-20", "Working Away From The Office",
         "Working away from the office shall be in line with the Remote Working Policy."),
        ("A.5.10-11-21", "Laptop And Mobile Device Encryption",
         "Laptop and mobile device encryption shall be enabled."),
        ("A.5.10-11-22", "Laptops And Mobile Devices",
         "Laptops and mobile devices shall be protected by a password, PIN, or biometric lock."),
        ("A.5.10-11-23", "Equipment And Media Taken Off-Site",
         "Equipment and media taken off-site shall not be left unattended in public places, including on public transport, and shall not be left visible in a vehicle."),
        ("A.5.10-11-24", "Laptops And Mobile Devices",
         "Laptops and mobile devices shall be carried as hand luggage when travelling."),
        ("A.5.10-11-25", "Be Protected Against Loss Or Compromise",
         "Information shall be protected against loss or compromise when working remotely (for example, at home or in public places)."),
        ("A.5.10-11-26", "Public Or Unsecured Wi-Fi Networks",
         "Public or unsecured Wi-Fi networks shall not be used for accessing organisation systems without VPN or equivalent encrypted connection."),
    ]),

    ("Removable Storage Devices", [
        ("A.5.10-11-27", "Removable Storage Devices Such As Usb",
         "Removable storage devices such as USB drives, external hard drives, and optical media shall not be used unless authorised by the information security management team."),
        ("A.5.10-11-28", "Only Organisation-Owned, Managed, And",
         "Only organisation-owned, managed, and encrypted removable storage devices shall be used when transferring internal or confidential data. Personal removable storage devices are prohibited for organisation data."),
    ]),

    ("Monitoring and Filtering", [
        ("A.5.10-11-29", "Comply With Swiss Employment Law And",
         "Monitoring shall comply with Swiss employment law and data protection requirements:."),
        ("A.5.10-11-30", "Purpose Limitation: Monitoring",
         "Purpose limitation: Monitoring shall serve legitimate security purposes (detecting threats, investigating incidents, verifying compliance) — not monitoring employee behaviour (Art. 26 ArGV 3)."),
        ("A.5.10-11-31", "Proportionality: The Least Intrusive",
         "Proportionality: The least intrusive monitoring method shall be used. Anonymous or pseudonymous analysis shall be preferred; nominal analysis shall only occur when anomalies are detected (nFADP Art. 6)."),
        ("A.5.10-11-32", "Transparency: Employees",
         "Transparency: Employees shall be informed in advance that monitoring takes place, what is monitored, and why — through this policy and the information security awareness programme."),
        ("A.5.10-11-33", "Private Communications: The Organisation",
         "Private communications: The organisation shall not access private communications on organisation systems, even where limited personal use is permitted (Art. 328b CO)."),
        ("A.5.10-11-34", "It System Logging",
         "IT system logging shall take place in accordance with the Logging and Monitoring Policy. Investigations shall be commenced where reasonable suspicion exists of a breach of this or any other policy."),
        ("A.5.10-11-35", "Be Conducted By The Information Security",
         "Investigations shall be conducted by the information security management team or designated personnel with appropriate authorisation. Employee rights: Employees investigated shall be informed unless doing so would compromise the investigation or violate legal obligations."),
    ]),

    ("Reporting", [
        ("A.5.10-11-36", "Breaches Of Information Security",
         "All breaches of information security policies shall be investigated. Where investigations reveal misconduct, disciplinary action may follow in line with organisation disciplinary procedures."),
    ]),

    ("Return of Assets", [
        ("A.5.10-11-37", "Employees And Third-Party Users",
         "All employees and third-party users shall return all organisation assets in their possession upon termination of their employment, contract, or agreement."),
        ("A.5.10-11-38", "A Signed Byod Agreement",
         "Where an employee or third-party user uses their own personal equipment (BYOD) to access organisation data, a signed BYOD agreement shall be in place before access is granted. The agreement shall include consent for remote wipe of organisation data upon termination or device loss, and acknowledgement that organisation data will be managed via MDM."),
        ("A.5.10-11-39", "Organisation Data",
         "All organisation data shall be transferred to the organisation and securely erased from the personal device."),
        ("A.5.10-11-40", "Mdm Profiles",
         "MDM profiles shall be removed and remote wipe of organisation data confirmed."),
        ("A.5.10-11-41", "Full Device Wipe Consent",
         "Where selective wipe (organisation data only) is not technically feasible, full device wipe consent shall be documented in the BYOD agreement."),
        ("A.5.10-11-42", "The Byod Record In The Asset",
         "The BYOD record in the asset register shall be updated."),
        ("A.5.10-11-43", "The Return Of Assets",
         "The return of assets shall be coordinated between HR and IT as part of the offboarding process."),
        ("A.5.10-11-44", "Line Managers",
         "Line managers shall verify that all assets assigned to the departing individual have been returned or accounted for."),
        ("A.5.10-11-45", "The Asset Register",
         "The asset register shall be updated to reflect all returned, reassigned, or disposed assets within 5 business days of departure."),
        ("A.5.10-11-46", "During Notice Periods, The Organisation",
         "During notice periods, the organisation shall take reasonable measures to prevent unauthorised copying of organisation information."),
        ("A.5.10-11-47", "Follow Up Within 5 Business Days",
         "HR shall follow up within 5 business days of the scheduled return date."),
        ("A.5.10-11-48", "Access To Organisation Systems From The",
         "Access to organisation systems from the device shall be blocked immediately."),
        ("A.5.10-11-49", "The Employee",
         "The employee shall report the loss immediately to IT and their line manager."),
        ("A.5.10-11-50", "Remotely Wipe The Device Where",
         "IT shall remotely wipe the device where technically feasible (mobile device, laptop with remote management)."),
        ("A.5.10-11-51", "A Security Incident Report",
         "A security incident report shall be created per the Incident Management Policy."),
        ("A.5.10-11-52", "Loss Circumstances",
         "Loss circumstances shall be investigated; disciplinary action may result if negligence is determined."),
        ("A.5.10-11-53", "Assets That Are No Longer Required",
         "When an employee changes role within the organisation, assets that are no longer required for the new role shall be returned and reassigned. Access rights shall be reviewed and adjusted to reflect the new role (per the Access Control Policy)."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.10-11
# =============================================================================
