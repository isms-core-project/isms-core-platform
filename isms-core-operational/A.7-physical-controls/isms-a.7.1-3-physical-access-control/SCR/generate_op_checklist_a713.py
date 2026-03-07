#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.7.1-3 — Physical Access Control Compliance Checklist

Controls A.7.1-3: Physical Access Control
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Physical Security Perimeters (22 reqs)
4. Physical Entry Controls (45 reqs)
5. Securing Offices, Rooms (27 reqs)
6. Compliance Measurement (1 reqs)

Total: 95 requirements across 4 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.7.1-3"
CONTROL_ID = "A.7.1-3"
CONTROL_NAME = "Physical Access Control"
SOURCE_POLICY = "ISMS-OP-POL-A.7.1-3"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.7.1-3
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Physical Security Perimeters", [
        ("A.7.1-3-01", "Define And Document Security Zones Using",
         "The organisation shall define and document security zones using the following classification:."),
        ("A.7.1-3-02", "Be Documented On Floor Plans With",
         "Each zone shall be documented on floor plans with clearly marked boundaries, entry points, and the access control mechanisms in use."),
        ("A.7.1-3-03", "External Walls, Roofs, And Floors",
         "External walls, roofs, and floors shall be of solid construction appropriate to the risk."),
        ("A.7.1-3-04", "External Doors",
         "External doors shall be secured with locks and access control mechanisms (e.g., [Access Control System] badge readers, electronic locks)."),
        ("A.7.1-3-05", "Be Secured, Particularly At Ground Level",
         "Windows shall be secured, particularly at ground level; ground-floor windows in proximity to Restricted or High-Security Zones shall be reinforced or fitted with security glazing."),
        ("A.7.1-3-06", "Emergency Exits",
         "Emergency exits shall be alarmed and monitored; emergency exits shall not be usable for routine entry from outside."),
        ("A.7.1-3-07", "Fire Doors On A Security Perimeter",
         "All fire doors on a security perimeter shall be alarmed, monitored, and tested in conjunction with the walls to establish the required level of resistance. Fire doors shall operate in accordance with Swiss fire safety regulations in a failsafe manner."),
        ("A.7.1-3-08", "Ventilation Points And Service Openings",
         "Ventilation points and service openings shall not provide a bypass route into secured areas."),
        ("A.7.1-3-09", "Suitable Intrusion Detection Systems",
         "Suitable intrusion detection systems shall be installed in accordance with applicable national or international standards (e.g., EN 50131)."),
        ("A.7.1-3-10", "Partitions Between Controlled,",
         "Partitions between Controlled, Restricted, and High-Security Zones shall extend floor-to-ceiling, including above suspended ceilings and below raised floors."),
        ("A.7.1-3-11", "Access Points Between Zones",
         "Access points between zones shall have appropriate access controls matching the destination zone."),
        ("A.7.1-3-12", "Walls Of Restricted And High-Security",
         "Walls of Restricted and High-Security Zones shall prevent visual and audio eavesdropping where the risk assessment requires it."),
        ("A.7.1-3-13", "Building Perimeter Inspections",
         "Building perimeter inspections shall be performed at minimum annually."),
        ("A.7.1-3-14", "Restricted And High-Security Zone",
         "Restricted and High-Security Zone perimeters shall be inspected at least quarterly and after any building modification or security incident."),
        ("A.7.1-3-15", "Inspection Findings",
         "Inspection findings shall be documented and any gaps remediated within 30 days (or immediately if they present an imminent risk)."),
        ("A.7.1-3-16", "[Organisation]-Controlled Areas (Cages,",
         "[Organisation]-controlled areas (cages, rooms, floors) shall be clearly delineated and documented."),
        ("A.7.1-3-17", "Contractual Requirements For Physical",
         "Contractual requirements for physical security, access logging, and incident notification shall be in place with the facility provider."),
        ("A.7.1-3-18", "Supplier Assurance Evidence (Iso 27001",
         "Supplier assurance evidence (ISO 27001 certificate, SOC 2 Type II report, or equivalent attestation) shall be obtained and reviewed annually."),
        ("A.7.1-3-19", "Documented Risk Acceptance With",
         "Where the colocation provider's physical security does not meet this policy's requirements, documented risk acceptance with compensating controls shall be recorded."),
        ("A.7.1-3-20", "Shared Infrastructure (Lifts, Corridors,",
         "Shared infrastructure (lifts, corridors, common areas) shall not provide uncontrolled access to the organisation's secured areas."),
        ("A.7.1-3-21", "Key And Card Management For Building",
         "Key and card management for building access in shared facilities shall be coordinated with building management, with [Organisation] maintaining an independent record of all credentials issued."),
        ("A.7.1-3-22", "Information Processing Facilities",
         "Information processing facilities separation*: Information processing facilities managed by the organisation shall be physically separated from those managed by external parties sharing the same building or floor."),
    ]),

    ("Physical Entry Controls", [
        ("A.7.1-3-23", "Entry Points To Secured Areas",
         "All entry points to secured areas shall be protected:."),
        ("A.7.1-3-24", "A Staffed Reception Desk Or Equivalent",
         "A staffed reception desk or equivalent control (intercom, video entry) shall operate during business hours."),
        ("A.7.1-3-25", "An Access Control System ([Access",
         "An access control system ([Access Control System] — e.g., Verkada, Genetec, Honeywell, Lenel, ASSA ABLOY/Salto, or equivalent RFID badge readers, mobile credentials, or biometric readers) shall authenticate all personnel entering beyond the Public Zone. Where systems are in selection, the interim approach and target deployment date shall be documented."),
        ("A.7.1-3-26", "Anti-Tailgating Measures",
         "Anti-tailgating measures shall be implemented at entry points to Restricted and High-Security Zones:."),
        ("A.7.1-3-27", "After-Hours Access",
         "After-hours access shall require additional authentication and shall generate alerts to security personnel or the on-call team."),
        ("A.7.1-3-28", "Side Doors And Secondary Entrances",
         "Side doors and secondary entrances shall have access controls equivalent to the main entrance for the corresponding zone."),
        ("A.7.1-3-29", "Fire Doors And Emergency Exits",
         "Fire doors and emergency exits shall be alarmed and monitored. Emergency exits shall open outward (per fire regulations) but shall not be openable from outside without authorisation."),
        ("A.7.1-3-30", "Roof Access Doors And Service Hatches",
         "Roof access doors and service hatches shall be locked and alarmed."),
        ("A.7.1-3-31", "The Access Control System",
         "The access control system shall log all access events (granted and denied) with identity, timestamp, and entry point."),
        ("A.7.1-3-32", "Access Rights",
         "Access rights shall be role-based and granted on a need-to-know/need-to-access basis."),
        ("A.7.1-3-33", "Access Rights",
         "Access rights shall be reviewed quarterly (at minimum); Restricted and High-Security Zone access shall be re-confirmed by the authorising manager."),
        ("A.7.1-3-34", "Terminated Employee Physical Access",
         "Terminated employee physical access shall be revoked the same day as employment termination, coordinated with HR."),
        ("A.7.1-3-35", "Lost, Stolen, Or Damaged Badges",
         "Lost, stolen, or damaged badges shall be reported immediately and deactivated per the following timeline:."),
        ("A.7.1-3-36", "Badge Sharing And Lending",
         "Badge sharing and lending shall be prohibited."),
        ("A.7.1-3-37", "Temporary Access Cards",
         "Temporary access cards shall be time-limited and automatically expire."),
        ("A.7.1-3-38", "Employee Access",
         "Employee access shall be based on the principle of least privilege, providing access only to the zones required for the employee's role."),
        ("A.7.1-3-39", "Access Control Tokens (Badges, Cards,",
         "Access control tokens (badges, cards, mobile credentials) shall be issued to each employee and shall identify the individual. Badges shall be worn visibly at all times while on premises (lanyard, clip, or badge holder). Covered or concealed badges may be challenged by security personnel."),
        ("A.7.1-3-40", "Employee Badges",
         "Employee badges shall include: photo, name, employee ID, zone access indicator (colour-coded or text)."),
        ("A.7.1-3-41", "Visitor Badges",
         "Visitor badges shall be clearly distinguishable from employee badges (distinct colour, 'VISITOR' marking, no encoded zone access)."),
        ("A.7.1-3-42", "Contractor Badges",
         "Contractor badges shall be distinguishable and include expiry date."),
        ("A.7.1-3-43", "Temporary Badges (Replacement For Lost",
         "Temporary badges (replacement for lost permanent badge) shall be marked 'TEMPORARY' and expire automatically after 7 days."),
        ("A.7.1-3-44", "Access Control Tokens",
         "Access control tokens shall not be shared, transferred, or loaned to other personnel."),
        ("A.7.1-3-45", "Be Revoked Immediately Upon Employment",
         "Access shall be revoked immediately upon employment termination; all physical access tokens shall be disabled and returned. HR shall notify Facilities of all terminations on or before the last working day."),
        ("A.7.1-3-46", "Role Changes",
         "Role changes shall be assessed for physical access implications; access to zones no longer required for the new role shall be revoked within 5 business days."),
        ("A.7.1-3-47", "Access Log Retention*: Physical Access",
         "Access log retention*: Physical access control system logs shall be retained for at least 12 months (or longer where required by applicable regulation or contract), protected against unauthorised modification, and available within 2 business days for audit and incident response purposes."),
        ("A.7.1-3-48", "Sign In At Reception Before Proceeding",
         "All visitors shall sign in at reception before proceeding beyond the Public Zone. Registration shall be recorded in [Visitor Management System] (or paper visitor log) and include: visitor name, company/organisation, host (employee being visited), date and time of arrival, and purpose of visit."),
        ("A.7.1-3-49", "Present Valid Photographic",
         "Visitors shall present valid photographic identification."),
        ("A.7.1-3-50", "Visitor Badges",
         "Visitor badges shall be clearly distinguishable from employee badges (distinct colour, marked 'VISITOR', no zone access encoded)."),
        ("A.7.1-3-51", "Return Badges At Departure And Sign",
         "Visitors shall return badges at departure and sign out. Unreturned badges shall be deactivated by end of business day."),
        ("A.7.1-3-52", "Visitors In Restricted Zones",
         "Visitors in Restricted Zones shall be escorted at all times by an authorised employee."),
        ("A.7.1-3-53", "Visitors In High-Security Zones",
         "Visitors in High-Security Zones shall be escorted at all times by an authorised employee with explicit zone access, and the visit shall be pre-approved by the zone owner."),
        ("A.7.1-3-54", "Visitor Access To High-Security Zones",
         "Visitor access to High-Security Zones shall be pre-authorised in writing (email or [Visitor Management System] approval) before arrival."),
        ("A.7.1-3-55", "Visitor Logs",
         "Visitor logs shall be retained for a minimum of 12 months and protected against unauthorised modification."),
        ("A.7.1-3-56", "Be Available Within 2 Business Days",
         "Logs shall be available within 2 business days for audit or incident investigation."),
        ("A.7.1-3-57", "Contractors And Maintenance Personnel",
         "Contractors and maintenance personnel shall be pre-authorised before arrival, with the scope of work and areas of access documented."),
        ("A.7.1-3-58", "Contractor Access",
         "Contractor access shall be time-limited and logged."),
        ("A.7.1-3-59", "Contractors Accessing Restricted Or",
         "Contractors accessing Restricted or High-Security Zones shall be escorted and their work supervised where sensitive systems or data are accessible."),
        ("A.7.1-3-60", "External Maintenance On Security Systems",
         "External maintenance on security systems (alarms, access control, CCTV) shall be performed under direct supervision by an authorised employee."),
        ("A.7.1-3-61", "Access To Delivery And Loading Areas",
         "Access to delivery and loading areas from outside the building shall be restricted to identified and authorised delivery personnel."),
        ("A.7.1-3-62", "Delivery And Loading Areas",
         "Delivery and loading areas shall be designed (or operationally managed) so that delivery personnel cannot gain access to other parts of the building."),
        ("A.7.1-3-63", "External Doors Of A Delivery And",
         "External doors of a delivery and loading area shall be secured when the internal doors to operational areas are opened; both shall not be open simultaneously where avoidable."),
        ("A.7.1-3-64", "Incoming Materials",
         "Incoming materials shall be inspected for evidence of tampering before being moved from the delivery area."),
        ("A.7.1-3-65", "Incoming Materials",
         "Incoming materials shall be registered in accordance with asset management procedures upon entry to the site."),
        ("A.7.1-3-66", "Incoming And Outgoing Shipments",
         "Incoming and outgoing shipments shall be physically segregated where feasible."),
        ("A.7.1-3-67", "Incoming Materials",
         "Incoming materials shall be inspected for hazardous substances where the risk assessment warrants it (context-dependent: chemical, biological, or explosive risks)."),
    ]),

    ("Securing Offices, Rooms", [
        ("A.7.1-3-68", "Be Locked When Unoccupied Outside",
         "Offices shall be locked when unoccupied outside business hours."),
        ("A.7.1-3-69", "The Clean Desk Policy",
         "The clean desk policy shall be enforced — sensitive documents secured in locked storage when not in active use."),
        ("A.7.1-3-70", "Be Positioned To Prevent Shoulder",
         "Screens shall be positioned to prevent shoulder surfing by visitors or passers-by."),
        ("A.7.1-3-71", "Storage Facilities (Cabinets, Safes,",
         "Storage facilities (cabinets, safes, locked drawers) shall be provided for securing classified documents and portable media."),
        ("A.7.1-3-72", "Areas Processing Confidential Or",
         "Areas processing Confidential or Restricted information (e.g., HR, finance, legal, executive offices) shall have:."),
        ("A.7.1-3-73", "Be Limited To Authorised It Personnel",
         "Access shall be limited to authorised IT personnel only, with named access lists maintained."),
        ("A.7.1-3-74", "Multi-Factor Authentication",
         "Multi-factor authentication shall be required (badge + PIN + biometric, or dual-person control)."),
        ("A.7.1-3-75", "Be Logged With Identity And Timestamp",
         "All access shall be logged with identity and timestamp."),
        ("A.7.1-3-76", "Visitors And Contractors In Server Rooms",
         "Visitors and contractors in server rooms shall be escorted at all times."),
        ("A.7.1-3-77", "Equivalent Protections",
         "Equivalent protections shall be assured through supplier assurance (ISO 27001 certificate, SOC 2 Type II report) and contractual security requirements."),
        ("A.7.1-3-78", "Documented Risk Treatment With",
         "Where exact equivalence is not feasible, documented risk treatment with compensating controls shall be recorded."),
        ("A.7.1-3-79", "Meeting Rooms",
         "Meeting rooms shall be checked for recording devices or materials left behind before sensitive discussions."),
        ("A.7.1-3-80", "Whiteboards And Flip Charts",
         "Whiteboards and flip charts shall be erased or removed after meetings."),
        ("A.7.1-3-81", "Not Be Left In Meeting Rooms",
         "Documents shall not be left in meeting rooms after meetings conclude."),
        ("A.7.1-3-82", "Video Conferencing Equipment",
         "Video conferencing equipment shall be secured when not in use; cameras and microphones shall be in a known-off state between meetings."),
        ("A.7.1-3-83", "Physical Access To Networking Equipment",
         "Physical access to networking equipment (switches, routers, wireless access points, patch panels) shall be restricted to authorised IT personnel."),
        ("A.7.1-3-84", "Network Jacks And Ports In Public",
         "Network jacks and ports in Public Zones shall be disabled or shall not provide access to the internal network."),
        ("A.7.1-3-85", "Network Jacks And Ports In Controlled",
         "Network jacks and ports in Controlled Zones that provide access to the internal network shall be secured by physical access controls to the zone."),
        ("A.7.1-3-86", "Not Connect Devices To Internal Network",
         "Visitors shall not connect devices to internal network ports unless explicitly authorised and escorted."),
        ("A.7.1-3-87", "Power And Telecommunications Cabling",
         "Power and telecommunications cabling carrying data shall be protected from interception, interference, and damage."),
        ("A.7.1-3-88", "Power Cables",
         "Power cables shall be segregated from communications cables to prevent interference."),
        ("A.7.1-3-89", "Access To Cable Rooms And Patch",
         "Access to cable rooms and patch panels shall be restricted by physical access control (Restricted Zone minimum)."),
        ("A.7.1-3-90", "Access Rights To Secure Areas",
         "Access rights to secure areas shall default to deny — access is granted only upon explicit authorisation."),
        ("A.7.1-3-91", "Photographic, Video, Audio, Or Other",
         "Photographic, video, audio, or other recording equipment (including cameras in mobile devices) shall not be permitted in secure areas unless specifically authorised by the zone owner."),
        ("A.7.1-3-92", "Personnel Working In Secure Areas",
         "Personnel working in secure areas shall be informed of the specific security requirements and restrictions applicable to that area."),
        ("A.7.1-3-93", "Compliance With Office, Meeting Room,",
         "Compliance with office, meeting room, and facility security requirements shall be verified through documented physical security walkthroughs:."),
        ("A.7.1-3-94", "Checklist: A Standardised Walkthrough",
         "Checklist: A standardised walkthrough checklist shall be maintained and used for all inspections."),
    ]),

    ("Compliance Measurement", [
        ("A.7.1-3-95", "Metrics Breaching Targets",
         "Metrics breaching targets shall be escalated to CISO immediately and include remediation plan with owner and target date."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.7.1-3
# =============================================================================
