#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.7.8-9 — Equipment Siting and Protection Compliance Checklist

Controls A.7.8-9: Equipment Siting and Protection
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Equipment Class for Prot (2 reqs)
4. Equipment Siting Requirements (36 reqs)
5. Security of Assets Off-Premises (43 reqs)
6. Incident Classification (2 reqs)
7. Compliance Measurement (1 reqs)

Total: 84 requirements across 5 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.7.8-9"
CONTROL_ID = "A.7.8-9"
CONTROL_NAME = "Equipment Siting and Protection"
SOURCE_POLICY = "ISMS-OP-POL-A.7.8-9"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.7.8-9
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Equipment Class for Prot", [
        ("A.7.8-9-01", "Be Classified Into Protection Categories",
         "Equipment shall be classified into protection categories to determine appropriate siting requirements and off-premises protection levels:."),
        ("A.7.8-9-02", "Category Assignment",
         "Category assignment shall be recorded in [Asset Management System] or [CMDB] as part of asset registration."),
    ]),

    ("Equipment Siting Requirements", [
        ("A.7.8-9-03", "Equipment Processing Or Storing",
         "Equipment processing or storing information shall be sited to reduce risks from physical and environmental threats, unauthorised access, and damage."),
        ("A.7.8-9-04", "Be Placed In Areas With Controlled",
         "Equipment shall be placed in areas with controlled physical access, appropriate to the classification of information it processes."),
        ("A.7.8-9-05", "Critical Equipment (Servers, Network",
         "Critical equipment (servers, network infrastructure, storage systems) shall be located in dedicated, access-controlled rooms — not in general office areas, reception zones, or publicly accessible spaces."),
        ("A.7.8-9-06", "Be Positioned To Minimise Risk Of",
         "Equipment shall be positioned to minimise risk of overlooking (shoulder surfing). Screens displaying sensitive or confidential information shall be positioned away from windows, corridors, and high-traffic areas."),
        ("A.7.8-9-07", "Information Processing Facilities",
         "Information processing facilities handling classified data should be positioned carefully so that unauthorised persons cannot view information displayed on screens during use. Where repositioning is not feasible, privacy screens shall be used."),
        ("A.7.8-9-08", "Organisation-Managed Equipment",
         "Organisation-managed equipment shall be clearly segregated from equipment not under organisational control (e.g., personal devices, visitor equipment, shared-tenancy infrastructure)."),
        ("A.7.8-9-09", "Storage Facilities (Server Racks,",
         "Storage facilities (server racks, storage cabinets, safe rooms) shall be secured to prevent unauthorised access."),
        ("A.7.8-9-10", "Be Protected From Temperature Extremes,",
         "Equipment shall be protected from temperature extremes, humidity, dust, vibration, and corrosive atmospheres. Acceptable environmental conditions for equipment operation shall be defined based on manufacturer specifications."),
        ("A.7.8-9-11", "Adequate Ventilation And Cooling",
         "Adequate ventilation and cooling shall be provided for equipment rooms. Server rooms and datacentres shall maintain temperature within 18-27 degrees C and humidity within 20-80% relative humidity, consistent with ASHRAE thermal guidelines."),
        ("A.7.8-9-12", "Be Elevated Or Protected Where Flood",
         "Equipment shall be elevated or protected where flood risk exists (e.g., raised floors, ground-level barriers, avoidance of basement locations in flood-prone areas)."),
        ("A.7.8-9-13", "Smoking, Eating, And Drinking",
         "Smoking, eating, and drinking shall be prohibited in server rooms, datacentres, and equipment closets. Guidelines for eating and drinking near workstations shall be communicated to all personnel."),
        ("A.7.8-9-14", "Environmental Conditions That May",
         "Environmental conditions that may disrupt operations (temperature, humidity, airborne particulates) shall be continuously monitored in rooms housing Category A (critical infrastructure) equipment, with automated alerting within 15 minutes when thresholds are exceeded. For rooms housing Category B equipment, continuous monitoring should be implemented where technically feasible."),
        ("A.7.8-9-15", "Be Protected From Power Failures Using",
         "Equipment shall be protected from power failures using uninterruptible power supply (UPS) systems appropriate to equipment criticality."),
        ("A.7.8-9-16", "Power Cables",
         "Power cables shall be protected from interception or damage through conduit, trunking, or enclosed cable trays."),
        ("A.7.8-9-17", "Emergency Power-Off (Epo) Switches",
         "Emergency power-off (EPO) switches shall be located near server room and datacentre exits for use in emergencies. EPO switches shall be clearly labelled, protected against accidental activation (e.g., hinged cover, break-glass enclosure), and tested annually as part of the electrical safety programme."),
        ("A.7.8-9-18", "Power Supplies",
         "Power supplies shall be redundant for critical equipment (N+1 configuration recommended)."),
        ("A.7.8-9-19", "Lightning Protection",
         "Lightning protection shall be applied to buildings housing information processing facilities. Surge protection filters shall be fitted to all incoming power and telecommunications lines."),
        ("A.7.8-9-20", "Network Cables Carrying Data Or",
         "Network cables carrying data or supporting information services shall be protected from interception, interference, or damage."),
        ("A.7.8-9-21", "Power Cables",
         "Power cables shall be segregated from communications cables to prevent electromagnetic interference."),
        ("A.7.8-9-22", "Cable Runs",
         "Cable runs shall be documented in the asset register and reviewed at least annually and upon material changes."),
        ("A.7.8-9-23", "Cabling Closets And Patch Panels",
         "Cabling closets and patch panels shall have appropriate physical access controls."),
        ("A.7.8-9-24", "Network Jacks In Public Areas",
         "Network jacks in public areas shall not provide access to the internal network unless explicitly authorised and monitored."),
        ("A.7.8-9-25", "Ensure That Siting, Physical Access,",
         "The organisation shall ensure that siting, physical access, environmental protection, and power resilience meet the requirements of this policy, verified through contractual obligations and periodic assurance."),
        ("A.7.8-9-26", "Third-Party Facility Assurance",
         "Third-party facility assurance shall be obtained through one or more of: SOC 2 Type II audit report (reviewing PE-related controls specifically), ISO 27001 certification (confirming Annex A physical controls in scope), or documented on-site inspection using the organisation's physical security checklist. Where SOC 2 or ISO 27001 reports are relied upon, the organisation shall verify:."),
        ("A.7.8-9-27", "A Formal Responsibility Matrix",
         "A formal responsibility matrix shall be maintained in the colocation contract, documenting which party is responsible for each physical security and environmental control."),
        ("A.7.8-9-28", "Evidence Of Third-Party Compliance",
         "Evidence of third-party compliance shall be retained and reviewed annually. Material changes to third-party facility security shall be reported to the organisation under contractual notification clauses."),
        ("A.7.8-9-29", "Vendor Risk Management (Soc 2: Cc9.2)",
         "Vendor risk management (SOC 2: CC9.2): Colocation and datacentre providers shall be included in the organisation's vendor risk management programme. Equipment-related vendor risks (physical security, environmental resilience, staffing, financial stability) shall be assessed at onboarding and reviewed annually. SLA compliance for uptime, incident response, and physical access notification shall be monitored against contractual thresholds."),
        ("A.7.8-9-30", "Visitor Devices",
         "Visitor devices shall not connect to the organisation's internal network. A segregated guest WiFi network shall be provided where visitor Internet access is required."),
        ("A.7.8-9-31", "Visitors Bringing Equipment Into",
         "Visitors bringing equipment into access-controlled areas (server rooms, secure areas) shall declare the equipment at reception and confirm its removal upon departure."),
        ("A.7.8-9-32", "Vendor Diagnostic Tools, Auditor",
         "Where visitor equipment must interface with organisation systems (e.g., vendor diagnostic tools, auditor equipment), IT Operations shall inspect the device, confirm current endpoint protection, and provide a time-limited, scope-restricted network connection."),
        ("A.7.8-9-33", "Visitor Equipment Use",
         "Visitor equipment use shall be documented in the visitor log, recording: device type, purpose, areas accessed, and time on-premises."),
        ("A.7.8-9-34", "Additional Protective Measures",
         "Additional protective measures shall be implemented, including dust covers, sealed enclosures, and protective housings rated to appropriate IP (Ingress Protection) standards."),
        ("A.7.8-9-35", "Equipment Ratings",
         "Equipment ratings shall match or exceed environmental conditions. IP65 or higher should be used for environments with significant dust or water exposure."),
        ("A.7.8-9-36", "Special Protection Methods",
         "Special protection methods shall be considered, such as keyboard membranes in industrial settings to prevent contamination."),
        ("A.7.8-9-37", "Maintenance Frequency",
         "Maintenance frequency shall be increased for equipment in hostile environments, with inspection intervals defined in the maintenance schedule."),
        ("A.7.8-9-38", "Equipment Processing Classified",
         "Equipment processing classified information in exposed locations shall be protected against information leakage due to electromagnetic emanation, where risk assessment warrants it."),
    ]),

    ("Security of Assets Off-Premises", [
        ("A.7.8-9-39", "Off-Site Assets",
         "Off-site assets shall be protected to prevent loss, damage, theft, or compromise of devices and to prevent interruption to the organisation's information processing activities."),
        ("A.7.8-9-40", "Removal Of Equipment From Organisational",
         "Removal of equipment from organisational premises shall be authorised by the appropriate line manager prior to removal."),
        ("A.7.8-9-41", "Authorisation Records",
         "Authorisation records shall document: equipment details (asset tag, serial number, type), purpose of removal, responsible person, expected return date, and any special handling requirements."),
        ("A.7.8-9-42", "High-Value Equipment (Value Exceeding",
         "High-value equipment (value exceeding [CHF threshold]) or equipment containing classified data shall require additional approval from [IT Operations Manager] or equivalent."),
        ("A.7.8-9-43", "Bulk Equipment Moves (E.G., Office",
         "Bulk equipment moves (e.g., office relocation, project deployment) shall be authorised through a formal equipment movement request."),
        ("A.7.8-9-44", "Equipment Removed From Premises",
         "Equipment removed from premises shall be logged in [Asset Management System] or [CMDB] with current location, custodian, and expected return date."),
        ("A.7.8-9-45", "Chain Of Custody",
         "Chain of custody shall be maintained when equipment transfers between individuals. Transfer records shall include both the releasing and receiving party, date, and equipment condition."),
        ("A.7.8-9-46", "Return Of Equipment",
         "Return of equipment shall be verified and recorded. Equipment shall be inspected upon return for damage, tampering, or missing components."),
        ("A.7.8-9-47", "Equipment Not Returned By The Expected",
         "Equipment not returned by the expected date shall trigger follow-up by the asset owner. Equipment overdue by more than 30 days shall be escalated to the line manager and IT Operations."),
        ("A.7.8-9-48", "Not Be Left Unattended In Public",
         "Equipment shall not be left unattended in public places (airports, cafes, conference venues, public transport, vehicles)."),
        ("A.7.8-9-49", "Be Carried In Unmarked, Nondescript Bags",
         "Equipment shall be carried in unmarked, nondescript bags during transport — not in manufacturer-branded bags or cases that advertise high-value contents."),
        ("A.7.8-9-50", "Be Secured In Hotel Safes (Noting",
         "When not in active use, equipment shall be secured in hotel safes (noting size limitations — laptops may not fit standard hotel safes), locked storage, or other secured areas. Where hotel safe capacity is insufficient, equipment shall be kept in locked luggage or the employee shall take equipment with them. Equipment shall not be left visible in hotel rooms."),
        ("A.7.8-9-51", "Vehicle Storage",
         "Vehicle storage shall only be used when absolutely necessary, and equipment shall be placed in the boot (trunk) out of sight — never on seats or visible through windows."),
        ("A.7.8-9-52", "Be Protected From Extreme Temperatures",
         "Equipment shall be protected from extreme temperatures during transport and storage. Manufacturer guidelines for safe operating and storage temperature ranges shall be observed."),
        ("A.7.8-9-53", "Not Be Exposed To Direct Sunlight",
         "Equipment shall not be exposed to direct sunlight for extended periods."),
        ("A.7.8-9-54", "Moisture And Humidity Protection",
         "Moisture and humidity protection shall be maintained during transport (padded bags, weatherproof cases for outdoor transport)."),
        ("A.7.8-9-55", "Be Transported In Padded Carrying Cases",
         "Equipment shall be transported in padded carrying cases to protect against physical shock and vibration."),
        ("A.7.8-9-56", "Be Physically Secured Where Possible",
         "Equipment shall be physically secured where possible using cable locks, lockdown plates, or equivalent physical tethering in shared or semi-public environments."),
        ("A.7.8-9-57", "Gps Tracking Or Location Services",
         "GPS tracking or location services shall be enabled on supported devices where technically feasible and legally permitted. GPS tracking configuration shall:."),
        ("A.7.8-9-58", "Compensating Controls",
         "Where GPS tracking is not technically feasible or legally permitted, compensating controls shall be documented (e.g., enhanced physical security awareness, encrypted full-disk protection, reduced data residency on device)."),
        ("A.7.8-9-59", "Remote Wipe Capability",
         "Remote wipe capability shall be configured on all supported mobile devices through [MDM] and shall be:."),
        ("A.7.8-9-60", "For After-Hours Incidents: An Emergency",
         "For after-hours incidents: an emergency contact procedure shall be documented and communicated to all personnel, enabling out-of-hours remote wipe initiation through [on-call IT Operations contact / MDM self-service portal]."),
        ("A.7.8-9-61", "Equipment Serial Numbers, Asset Tags,",
         "Equipment serial numbers, asset tags, and descriptions shall be recorded in [Asset Management System] to support police reports and insurance claims in case of theft."),
        ("A.7.8-9-62", "Be Stored Securely When Not In",
         "Equipment shall be stored securely when not in use — in a locked room, cabinet, or desk drawer where feasible."),
        ("A.7.8-9-63", "Network Connections",
         "Network connections shall be secured with encrypted WiFi (WPA3 preferred, WPA2 minimum). VPN shall be used for all access to organisation systems, except where the organisation has implemented a zero-trust network architecture or where access is exclusively to SaaS applications over HTTPS with enforced SSO and device certificate validation."),
        ("A.7.8-9-64", "Family Members, Visitors, And Other",
         "Family members, visitors, and other household members shall not have access to organisation equipment. Screen lock shall be activated when the employee steps away."),
        ("A.7.8-9-65", "Acknowledge Home Office Security",
         "Employees shall acknowledge home office security requirements as a condition of remote working authorisation."),
        ("A.7.8-9-66", "Privacy Screens",
         "Privacy screens shall be used when working with sensitive or confidential information in environments where shoulder surfing is possible (public transport, cafes, airport lounges, co-working spaces)."),
        ("A.7.8-9-67", "Public Wifi",
         "Public WiFi shall only be used with VPN protection, except where the organisation has implemented zero-trust network architecture or where access is limited to SaaS applications over HTTPS with enforced SSO and device certificate validation. Direct connection to public WiFi without VPN or equivalent protection for accessing organisation systems or data is prohibited."),
        ("A.7.8-9-68", "Bluetooth, Airdrop, And Other Wireless",
         "Bluetooth, AirDrop, and other wireless sharing protocols shall be disabled when not actively required."),
        ("A.7.8-9-69", "Never Be Left Unattended In Public",
         "Equipment shall never be left unattended in public spaces, even briefly."),
        ("A.7.8-9-70", "Physical Tamper Detection",
         "Physical tamper detection shall be implemented (tamper-evident seals, chassis intrusion detection, tamper alarms) appropriate to asset criticality."),
        ("A.7.8-9-71", "Environmental Monitoring",
         "Environmental monitoring shall be continuous where technically feasible, with remote alerting for threshold excursions."),
        ("A.7.8-9-72", "Regular Physical Inspection Schedules",
         "Regular physical inspection schedules shall be established, with frequency based on risk assessment and equipment criticality."),
        ("A.7.8-9-73", "Remote Monitoring And Management",
         "Remote monitoring and management capabilities shall be enabled to maintain visibility of equipment health, security status, and configuration integrity."),
        ("A.7.8-9-74", "Logical Access Restrictions (Encrypted",
         "Logical access restrictions (encrypted communications, strong authentication, certificate-based access) shall compensate for reduced physical security."),
        ("A.7.8-9-75", "Incident Response Procedures",
         "Incident response procedures shall account for remote locations, including response time expectations and local contact arrangements."),
        ("A.7.8-9-76", "Environmental Failure Failover (Soc 2:",
         "Environmental failure failover (SOC 2: A1.2): For permanently off-site equipment supporting critical services, failover procedures shall be documented for environmental failure scenarios (power loss, cooling failure, network outage). Failover may include: automatic switchover to redundant equipment at alternate location, graceful degradation with reduced service, or manual relocation to a pre-approved recovery site. Failover procedures shall be tested annually as part of business continuity testing."),
        ("A.7.8-9-77", "Manufacturer Protection Instructions",
         "Manufacturer protection instructions (electromagnetic fields, moisture, temperature, dust) shall be followed for permanently installed equipment."),
        ("A.7.8-9-78", "Be Kept In Hand Luggage During",
         "Equipment shall be kept in hand luggage during air travel — never checked into hold baggage."),
        ("A.7.8-9-79", "Not Be Left In Vehicles Overnight",
         "Equipment shall not be left in vehicles overnight or for extended periods, even in locked vehicles."),
        ("A.7.8-9-80", "International Travel With Encrypted",
         "International travel with encrypted devices shall comply with destination country import/export regulations for cryptographic equipment."),
        ("A.7.8-9-81", "Lost Or Stolen Equipment During Travel",
         "Lost or stolen equipment during travel shall be reported immediately to IT Operations (for remote wipe initiation) and to the local police. The employee shall document the circumstances and report through the incident management process upon return."),
    ]),

    ("Incident Classification", [
        ("A.7.8-9-82", "Equipment-Related Security Events",
         "Equipment-related security events shall be classified and responded to based on severity:."),
        ("A.7.8-9-83", "Equipment Security Incidents",
         "Equipment security incidents shall be reported and managed through the organisation's incident management process (A.5.24-28)."),
    ]),

    ("Compliance Measurement", [
        ("A.7.8-9-84", "Be Assessed Using The Following Metrics",
         "Compliance shall be assessed using the following metrics:."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.7.8-9
# =============================================================================
