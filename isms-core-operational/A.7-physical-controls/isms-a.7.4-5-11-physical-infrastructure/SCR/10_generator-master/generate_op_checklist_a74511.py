#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.7.4-5-11 — Physical Infrastructure Security Compliance Checklist

Controls A.7.4-5-11: Physical Infrastructure Security
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Physical Security Monitoring (23 reqs)
4. Environmental Protection (24 reqs)
5. Supporting Utilities (18 reqs)
6. Facility Criticality Tiers (2 reqs)
7. Incident Classification (2 reqs)
8. Compliance Measurement (1 reqs)

Total: 70 requirements across 6 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.7.4-5-11"
CONTROL_ID = "A.7.4-5-11"
CONTROL_NAME = "Physical Infrastructure Security"
SOURCE_POLICY = "ISMS-OP-POL-A.7.4-5-11"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.7.4-5-11
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Physical Security Monitoring", [
        ("A.7.4-5-11-01", "Physical Security Monitoring",
         "Physical security monitoring shall detect and deter unauthorised physical access to facilities and restricted areas. Monitoring system design and implementation shall be proportionate to facility criticality."),
        ("A.7.4-5-11-02", "The Following Physical Security Systems",
         "The following physical security systems shall be implemented and maintained. Organisations shall specify the actual systems deployed (or document selection status) for each category:."),
        ("A.7.4-5-11-03", "Integration Requirements*: Where",
         "Integration requirements*: Where technically feasible, physical security systems should feed events to [SIEM] for correlation with logical security events. At minimum, access control events and intrusion detection alarms shall be forwarded."),
        ("A.7.4-5-11-04", "Electronic Access Control",
         "Electronic access control shall be implemented at all facility entry and exit points with authentication, event logging, and integration with identity management."),
        ("A.7.4-5-11-05", "Access Events (Granted, Denied, Forced",
         "Access events (granted, denied, forced door, door held open) shall be logged with timestamp, individual identity, and door identifier."),
        ("A.7.4-5-11-06", "Access Logs",
         "Access logs shall be retained for a minimum of 12 months."),
        ("A.7.4-5-11-07", "Access Rights",
         "Access rights shall be reviewed semi-annually and revoked when no longer required (e.g., role change, termination)."),
        ("A.7.4-5-11-08", "Same-Day Access Revocation",
         "Same-day access revocation shall be enforced upon employment termination."),
        ("A.7.4-5-11-09", "Physical Access Rights",
         "Physical access rights shall be reviewed semi-annually using the following structured workflow:."),
        ("A.7.4-5-11-10", "Cctv Coverage",
         "CCTV coverage shall be provided at facility entrances, restricted area access points, and critical infrastructure locations (server rooms, utility rooms)."),
        ("A.7.4-5-11-11", "Cctv Systems",
         "CCTV systems shall record continuously during operational hours at minimum; 24/7 recording is required for Tier 1 facilities."),
        ("A.7.4-5-11-12", "Cctv Systems",
         "CCTV systems shall comply with applicable data protection requirements (Swiss nFADP, cantonal regulations). Signage indicating video surveillance shall be displayed at monitored areas."),
        ("A.7.4-5-11-13", "Camera Health (Connectivity, Image",
         "Camera health (connectivity, image quality, storage capacity) shall be verified weekly."),
        ("A.7.4-5-11-14", "Intrusion Detection Systems (Ids)",
         "Intrusion detection systems (IDS) shall be installed at Tier 1 facilities, covering perimeter doors, windows, and access points to restricted areas."),
        ("A.7.4-5-11-15", "Be Connected To A Monitored Response",
         "Alarms shall be connected to a monitored response point (security operations, alarm monitoring service, or [Alarm Monitoring Provider])."),
        ("A.7.4-5-11-16", "Be Tested Quarterly To Confirm Correct",
         "IDS shall be tested quarterly to confirm correct operation."),
        ("A.7.4-5-11-17", "Register Upon Arrival, Receive Temporary",
         "All visitors shall register upon arrival, receive temporary identification, and be escorted in restricted areas."),
        ("A.7.4-5-11-18", "Visitor Records (Name, Organisation,",
         "Visitor records (name, organisation, host, arrival/departure time) shall be retained for a minimum of 12 months."),
        ("A.7.4-5-11-19", "Visitor Badges",
         "Visitor badges shall clearly identify visitor status, deny access to restricted areas, and expire at the end of the business day on which issued."),
        ("A.7.4-5-11-20", "Repeated Failed Access Attempts (3 Or",
         "Repeated failed access attempts (3 or more within 30 minutes) shall trigger alert and investigation."),
        ("A.7.4-5-11-21", "The Design And Configuration Of",
         "The design and configuration of monitoring systems shall be kept confidential."),
        ("A.7.4-5-11-22", "Monitoring Systems",
         "Monitoring systems shall be protected against tampering, unauthorised disabling, and remote interference."),
        ("A.7.4-5-11-23", "Monitoring Equipment",
         "Monitoring equipment shall be on UPS-backed power to ensure continued operation during power interruptions."),
    ]),

    ("Environmental Protection", [
        ("A.7.4-5-11-24", "Environmental Protection Controls",
         "Environmental protection controls shall prevent or mitigate damage from fire, water, climate extremes, and other physical threats. Protection levels shall be proportionate to facility criticality."),
        ("A.7.4-5-11-25", "An Environmental Threat Risk Assessment",
         "An environmental threat risk assessment shall be conducted for each facility, considering geographic location, building characteristics, historical events, and surrounding hazards."),
        ("A.7.4-5-11-26", "The Assessment",
         "The assessment shall be reviewed annually and updated following incidents or significant facility changes."),
        ("A.7.4-5-11-27", "Fire Detection",
         "Fire detection shall be implemented in all facilities containing information processing equipment."),
        ("A.7.4-5-11-28", "Notes On Suppression Agents*: Clean",
         "Notes on suppression agents*: Clean agent systems compliant with NFPA 2001 and ISO 14520 are required for occupied spaces containing electronic equipment. Water-based sprinkler systems shall not be used in server rooms or datacentres. Organisations should consider the long-term availability and environmental profile of selected agents when specifying suppression systems."),
        ("A.7.4-5-11-29", "Fire Doors On Security Perimeters",
         "Fire doors on security perimeters shall be alarmed, monitored, and tested in accordance with applicable fire codes."),
        ("A.7.4-5-11-30", "Emergency Lighting And Evacuation Routes",
         "Emergency lighting and evacuation routes shall be maintained and tested semi-annually."),
        ("A.7.4-5-11-31", "Water Detection Sensors",
         "Water detection sensors shall be installed in Tier 1 facilities — below raised floors, above suspended ceilings, near cooling infrastructure, and in all zones where water ingress is possible."),
        ("A.7.4-5-11-32", "Tier 2 Facilities",
         "Tier 2 facilities shall have water detection in high-risk areas (near plumbing, HVAC systems, ground-level rooms)."),
        ("A.7.4-5-11-33", "Water Alarms",
         "Water alarms shall trigger immediate alert to facilities management."),
        ("A.7.4-5-11-34", "Implement Drainage, Waterproofing, And",
         "Facilities shall implement drainage, waterproofing, and physical barriers appropriate to identified flood risk."),
        ("A.7.4-5-11-35", "Information Processing Equipment",
         "Information processing equipment shall be maintained within controlled temperature and humidity ranges to prevent damage and ensure reliable operation."),
        ("A.7.4-5-11-36", "Tier 1 Facilities*: Temperature",
         "Tier 1 facilities*: Temperature shall be maintained within 18–27 °C with tolerance of +/- 2 °C. Continuous environmental monitoring with real-time alerting is required."),
        ("A.7.4-5-11-37", "Tier 2 Facilities*: Temperature",
         "Tier 2 facilities*: Temperature shall be maintained within 18–27 °C with tolerance of +/- 5 °C. Environmental monitoring with alerting during staffed hours is required."),
        ("A.7.4-5-11-38", "Environmental Monitoring Data",
         "Environmental monitoring data (temperature, humidity) shall be logged and retained for a minimum of 12 months."),
        ("A.7.4-5-11-39", "Environmental Monitoring Systems",
         "Environmental monitoring systems shall be configured with the following alert thresholds, response requirements, and escalation paths:."),
        ("A.7.4-5-11-40", "Alert Testing*: Environmental Monitoring",
         "Alert testing*: Environmental monitoring alert paths shall be tested quarterly (simulate threshold excursion; verify alert delivery to all configured recipients within target timeframes)."),
        ("A.7.4-5-11-41", "Building Exterior (Roof, Walls,",
         "Building exterior (roof, walls, flooring) shall be of solid construction appropriate to identified threats."),
        ("A.7.4-5-11-42", "Lightning Protection",
         "Lightning protection shall be applied to buildings housing information processing facilities. Surge protection shall be fitted to incoming power and telecommunications lines."),
        ("A.7.4-5-11-43", "Equipment Siting",
         "Equipment siting shall minimise risk from identified environmental threats (e.g., avoid basement locations in flood-prone areas, avoid locations adjacent to hazardous processes)."),
        ("A.7.4-5-11-44", "Guidelines For Eating, Drinking, And",
         "Guidelines for eating, drinking, and smoking in proximity to information processing facilities shall be established and communicated."),
        ("A.7.4-5-11-45", "Emergency Response Procedures",
         "Emergency response procedures shall be documented for environmental incidents and tested regularly. Emergency contact information shall be posted at facility entrances and within server rooms."),
        ("A.7.4-5-11-46", "Emergency Procedures",
         "Emergency procedures shall be tested at least annually through drills or tabletop exercises."),
        ("A.7.4-5-11-47", "Personnel With Facility Access",
         "All personnel with facility access shall complete physical security awareness training. Training is delivered annually with new-hire completion required within 10 business days of facility access being granted."),
    ]),

    ("Supporting Utilities", [
        ("A.7.4-5-11-48", "Utility Systems",
         "Utility systems shall be implemented with capacity and redundancy proportionate to facility criticality, and tested regularly to ensure reliability."),
        ("A.7.4-5-11-49", "Ups Systems",
         "UPS systems shall protect all critical information processing equipment, network infrastructure, and security systems (access control, CCTV, fire detection)."),
        ("A.7.4-5-11-50", "Ups Systems",
         "UPS systems shall be configured to support orderly shutdown of equipment that supports critical business operations if extended outage exceeds UPS runtime."),
        ("A.7.4-5-11-51", "Ups Capacity",
         "UPS capacity shall be calculated using the following four-step process to ensure adequate runtime for protected equipment:."),
        ("A.7.4-5-11-52", "Be Inspected Weekly And Load-Tested",
         "Where generators are installed, they shall be inspected weekly and load-tested according to the testing schedule below."),
        ("A.7.4-5-11-53", "The Fuel Type",
         "The fuel type shall be selected based on facility requirements, local infrastructure, and environmental considerations:."),
        ("A.7.4-5-11-54", "Cooling Capacity",
         "Cooling capacity shall be sufficient for the current heat load plus planned growth."),
        ("A.7.4-5-11-55", "Cooling Systems",
         "Cooling systems shall be maintained per manufacturer service schedules, with air filters replaced at recommended intervals."),
        ("A.7.4-5-11-56", "Power And Telecommunications Cabling",
         "Power and telecommunications cabling carrying data or supporting information services shall be protected from interception, interference, or damage."),
        ("A.7.4-5-11-57", "Power Cables",
         "Power cables shall be segregated from communications cables to prevent interference."),
        ("A.7.4-5-11-58", "Access To Cable Rooms And Patch",
         "Access to cable rooms and patch panels shall be restricted by physical access control."),
        ("A.7.4-5-11-59", "Automated And Manual Failover Procedures",
         "Automated and manual failover procedures shall be documented and tested to ensure connectivity continuity:."),
        ("A.7.4-5-11-60", "Single-Isp Backup For Tier 2 Facilities*",
         "Single-ISP backup for Tier 2 facilities*: Where a single ISP is deployed, a 4G/5G mobile broadband failover device (e.g., Cradlepoint, Peplink, or equivalent) shall be available as backup. Failover device shall be tested quarterly to confirm SIM activation and bandwidth sufficiency for critical services."),
        ("A.7.4-5-11-61", "Utility Resilience Systems",
         "All utility resilience systems shall be tested at regular intervals to verify operational readiness:."),
        ("A.7.4-5-11-62", "Test Results",
         "Test results shall be documented with: test date, system tested, test procedure, pass/fail result, issues identified, and corrective actions. Test records shall be retained for 5 years."),
        ("A.7.4-5-11-63", "Failed Test Response*: Any Test Failure",
         "Failed test response*: Any test failure shall trigger immediate investigation, interim compensating controls (e.g., restrict facility use, increase monitoring), and remediation within 30 days. Repeat failures shall be escalated to the CISO."),
        ("A.7.4-5-11-64", "Utility Systems (Power, Cooling,",
         "Utility systems (power, cooling, telecommunications) shall be monitored in real-time with alerting for failures, threshold excursions, and degraded conditions."),
        ("A.7.4-5-11-65", "Utility Incidents",
         "Utility incidents shall be logged and reported per the incident management process."),
    ]),

    ("Facility Criticality Tiers", [
        ("A.7.4-5-11-66", "Be Classified Into Criticality Tiers",
         "Facilities shall be classified into criticality tiers based on business impact analysis. The tier classification drives monitoring intensity, environmental protection requirements, and utility resilience levels throughout this policy."),
        ("A.7.4-5-11-67", "Tier Assignment Process*: System Owners,",
         "Tier assignment process*: System owners, in consultation with the Facilities Manager and CISO, shall determine the appropriate tier for each facility based on business impact analysis results. Tier assignments shall be reviewed annually."),
    ]),

    ("Incident Classification", [
        ("A.7.4-5-11-68", "Physical Infrastructure Security Events",
         "Physical infrastructure security events shall be classified and responded to based on severity:."),
        ("A.7.4-5-11-69", "Physical Security Incidents",
         "Physical security incidents shall be reported and managed through the organisation's incident management process (A.5.24–28)."),
    ]),

    ("Compliance Measurement", [
        ("A.7.4-5-11-70", "Be Assessed Using The Following Weighted",
         "Compliance shall be assessed using the following weighted metrics:."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.7.4-5-11
# =============================================================================
