#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.7 — Threat Intelligence Compliance Checklist

Control A.5.7: Threat Intelligence
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Intelligence Types and Layers (6 reqs)
4. Source Categories (3 reqs)
5. Vendor-Provided Intelligence (3 reqs)
6. Collection and Analysis (9 reqs)
7. Intelligence Data Lifecycle (2 reqs)
8. Dissemination and Sharing (8 reqs)
9. Risk Assessment Integration (13 reqs)
10. Incident Management Integration (9 reqs)
11. Security Monitoring Integration (7 reqs)
12. Avail & Business Cont (7 reqs)
13. Effectiveness Measurement (3 reqs)
14. Testing and Validation (2 reqs)
15. Customer Threat Intelligence (2 reqs)
16. Compliance Measurement (2 reqs)

Total: 76 requirements across 14 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.5.7"
CONTROL_ID = "A.5.7"
CONTROL_NAME = "Threat Intelligence"
SOURCE_POLICY = "ISMS-OP-POL-A.5.7"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.7
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Intelligence Types and Layers", [
        ("A.5.7-01", "Produce Or Consume Threat Intelligence",
         "The organisation shall produce or consume threat intelligence at three layers, each serving a distinct audience and purpose. Not all organisations will produce intelligence at every layer internally; consumption from external sources is acceptable where internal production capacity is limited."),
        ("A.5.7-02", "Strategic Intelligence",
         "Strategic intelligence shall address:."),
        ("A.5.7-03", "Production Frequency*: Quarterly At",
         "Production frequency*: Quarterly at minimum, or triggered by significant threat landscape changes. Where the organisation does not produce strategic intelligence internally, it shall subscribe to or access at least one source of sector-relevant strategic threat reporting (e.g., Swiss NCSC semi-annual reports, CERT advisories, or commercial strategic intelligence services)."),
        ("A.5.7-04", "Tactical Intelligence",
         "Tactical intelligence shall address:."),
        ("A.5.7-05", "Production Frequency*: Monthly At",
         "Production frequency*: Monthly at minimum, or triggered by emerging threats. Where internal analysis capacity is limited, the organisation shall consume tactical intelligence from at least one structured source (e.g., MITRE ATT&CK, Swiss NCSC advisories, CERT feeds, or commercial threat reports)."),
        ("A.5.7-06", "Operational Intelligence",
         "Operational intelligence shall include:."),
    ]),

    ("Source Categories", [
        ("A.5.7-07", "Maintain Threat Intelligence Sources",
         "The organisation shall maintain threat intelligence sources across multiple categories to avoid single-source dependency and ensure comprehensive coverage. The number and depth of sources shall be proportionate to organisational size and risk exposure."),
        ("A.5.7-08", "Threat Intelligence Sources",
         "All threat intelligence sources shall be evaluated before operationalisation and periodically thereafter. Evaluation shall consider:."),
        ("A.5.7-09", "Sources That Consistently Provide",
         "Sources that consistently provide inaccurate, irrelevant, or excessively noisy information shall be replaced or deprioritised. Source performance shall be reviewed at least annually."),
    ]),

    ("Vendor-Provided Intelligence", [
        ("A.5.7-10", "Commercial Threat Intelligence Vendors",
         "Commercial threat intelligence vendors shall be evaluated against:."),
        ("A.5.7-11", "Contracts With Commercial Threat",
         "Contracts with commercial threat intelligence vendors shall include:."),
        ("A.5.7-12", "Commercial Intelligence Vendors",
         "Commercial intelligence vendors shall be reviewed annually covering:."),
    ]),

    ("Collection and Analysis", [
        ("A.5.7-13", "Implement A Documented Process For",
         "The organisation shall implement a documented process for collecting threat intelligence that includes:."),
        ("A.5.7-14", "Automated Collection: Threat Feeds",
         "Automated collection: Threat feeds shall be ingested automatically where feasible, using standard protocols (STIX/TAXII where supported) or vendor-specific APIs. Automated feeds shall be directed to [SIEM] or [Threat Intelligence Platform] for centralised processing."),
        ("A.5.7-15", "Manual Collection: Security Personnel",
         "Manual collection: Security personnel shall review advisory sources, security news, and community forums on a defined schedule. Manual collection findings shall be documented and entered into the threat intelligence register."),
        ("A.5.7-16", "Internal Collection: Security Events,",
         "Internal collection: Security events, incident findings, and forensic analysis results shall be captured as internal threat intelligence. Post-incident reviews shall explicitly identify and record IOCs and TTPs encountered."),
        ("A.5.7-17", "Data Protection: All Collected",
         "Data protection: All collected intelligence shall comply with applicable data protection requirements. Personal data included in threat intelligence (e.g., email addresses in phishing indicators) shall be processed only for the legitimate interest of information security and retained only as long as the indicator remains operationally relevant."),
        ("A.5.7-18", "Raw Threat Data",
         "Raw threat data shall be analysed before dissemination to ensure quality and relevance. Analysis shall:."),
        ("A.5.7-19", "Analysis Responsibilities",
         "Where the organisation does not have dedicated threat intelligence analysts, analysis responsibilities shall be assigned to the CISO or designated security personnel. Analysis need not be a full-time function for smaller organisations, but it shall be a documented, recurring activity with clear ownership."),
        ("A.5.7-20", "Threat Intelligence — Whether Produced",
         "All threat intelligence — whether produced internally or consumed from external sources — shall meet the following quality criteria before being acted upon:."),
        ("A.5.7-21", "Intelligence That Does Not Meet These",
         "Intelligence that does not meet these criteria shall be flagged, investigated, or discarded. Source evaluation records shall document quality issues."),
    ]),

    ("Intelligence Data Lifecycle", [
        ("A.5.7-22", "Threat Intelligence Data",
         "Threat intelligence data shall be retained according to operational and regulatory requirements:."),
        ("A.5.7-23", "Indicators Of Compromise Deployed To",
         "Indicators of compromise deployed to detection systems shall be managed through a lifecycle process:."),
    ]),

    ("Dissemination and Sharing", [
        ("A.5.7-24", "Threat Intelligence",
         "Threat intelligence shall be distributed to the appropriate audience based on intelligence type:."),
        ("A.5.7-25", "Tlp Classification: All Shared",
         "TLP classification: All shared intelligence shall be classified using Traffic Light Protocol v2.0 (TLP:RED, TLP:AMBER+STRICT, TLP:AMBER, TLP:GREEN, TLP:CLEAR). Sharing shall not exceed the TLP designation assigned by the originator."),
        ("A.5.7-26", "Sharing Agreements: Formal Agreements",
         "Sharing agreements: Formal agreements (NDA, information sharing agreement, or membership terms) shall be in place before sharing with external parties."),
        ("A.5.7-27", "Data Protection: Shared Intelligence",
         "Data protection: Shared intelligence shall not include personal data beyond what is necessary for threat detection (e.g., IOCs). Where personal data is shared, a lawful basis under nFADP shall be established."),
        ("A.5.7-28", "Regulatory Reporting: Where Swiss Ncsc",
         "Regulatory reporting: Where Swiss NCSC mandatory reporting obligations apply (critical infrastructure operators — ISG Art. 74b), the organisation shall report relevant cyber incidents to the NCSC within 24 hours per applicable requirements."),
        ("A.5.7-29", "Respect Tlp Markings: Intelligence",
         "Respect TLP markings: Intelligence received with TLP designations shall not be shared beyond the permitted boundaries."),
        ("A.5.7-30", "Validate Before Acting: Externally",
         "Validate before acting: Externally received IOCs shall be validated against the organisation's environment before deployment to blocking or detection systems to minimise false positives."),
        ("A.5.7-31", "Acknowledge Receipt: Where Sharing Is",
         "Acknowledge receipt: Where sharing is bidirectional, the organisation shall acknowledge receipt and provide feedback on intelligence utility when requested."),
    ]),

    ("Risk Assessment Integration", [
        ("A.5.7-32", "Threat Intelligence",
         "Threat intelligence shall inform the organisation's risk assessment process per ISO 27001:2022 Clause 6.1. This integration is mandatory — threat intelligence that does not influence risk decisions provides limited value."),
        ("A.5.7-33", "Likelihood Assessment: Threat",
         "Likelihood assessment: Threat intelligence on active campaigns, exploitation activity, and threat actor targeting shall inform the likelihood estimates assigned to identified risks."),
        ("A.5.7-34", "Impact Assessment: Intelligence On",
         "Impact assessment: Intelligence on attack techniques and observed consequences in peer organisations shall inform impact assessments."),
        ("A.5.7-35", "Risk Register Updates: When Threat",
         "Risk register updates: When threat intelligence identifies new threats or changes to existing threats, the risk register shall be updated accordingly. Each update shall reference the supporting threat intelligence source."),
        ("A.5.7-36", "Control Effectiveness: Threat",
         "Control effectiveness: Threat intelligence on bypassed or ineffective controls observed in the wild shall trigger re-evaluation of the organisation's control effectiveness."),
        ("A.5.7-37", "The Ciso Or Designated Security",
         "The CISO or designated security personnel shall review strategic and tactical threat intelligence outputs at least quarterly against the current risk register."),
        ("A.5.7-38", "New Threats Identified Through",
         "New threats identified through intelligence analysis shall be submitted to Risk Management for formal risk assessment."),
        ("A.5.7-39", "Changes To Threat Likelihood Or Impact",
         "Changes to threat likelihood or impact based on intelligence shall be documented with traceable references to supporting intelligence reports."),
        ("A.5.7-40", "Risk Treatment Decisions Influenced By",
         "Risk treatment decisions influenced by threat intelligence shall be recorded in the risk register."),
        ("A.5.7-41", "Threat Intelligence",
         "Where the organisation processes personal data subject to nFADP or GDPR, threat intelligence shall specifically address threats to data confidentiality and privacy:."),
        ("A.5.7-42", "Risks Related To Personal Data",
         "Risks related to personal data processing (e.g., “R-DATA-01: Unauthorised access to customer personal data”) shall be reviewed quarterly against threat intelligence findings."),
        ("A.5.7-43", "Threat Intelligence Indicating Increased",
         "Threat intelligence indicating increased targeting of data controllers in the organisation’s sector shall trigger re-assessment of data protection control adequacy."),
        ("A.5.7-44", "Detection Rules For Data Exfiltration",
         "Detection rules for data exfiltration attempts shall be updated based on observed attacker techniques."),
    ]),

    ("Incident Management Integration", [
        ("A.5.7-45", "Threat Intelligence",
         "Threat intelligence shall enhance incident detection, investigation, and response per Controls A.5.24-28."),
        ("A.5.7-46", "Iocs From Threat Intelligence Sources",
         "IOCs from threat intelligence sources shall be deployed to detection systems ([SIEM], [EDR], email gateway, web filter) to enable automated alerting."),
        ("A.5.7-47", "Threat Actor Ttps From Tactical",
         "Threat actor TTPs from tactical intelligence shall be translated into detection rules or monitoring use cases where feasible."),
        ("A.5.7-48", "Detection Rule Effectiveness",
         "Detection rule effectiveness shall be reviewed periodically and rules updated based on evolving intelligence."),
        ("A.5.7-49", "Available Threat Intelligence",
         "When a security incident occurs, available threat intelligence shall be queried for related indicators, known threat actor profiles, and attack pattern context."),
        ("A.5.7-50", "Threat Intelligence Context",
         "Threat intelligence context shall be included in incident investigation records to support root cause analysis and attribution assessment."),
        ("A.5.7-51", "Incident Findings —",
         "Incident findings — including newly discovered IOCs, observed TTPs, and attack infrastructure — shall be captured as internal threat intelligence."),
        ("A.5.7-52", "Post-Incident Reviews",
         "Post-incident reviews shall assess whether existing threat intelligence sources provided adequate warning and whether detection rules performed as expected."),
        ("A.5.7-53", "Lessons Learned",
         "Lessons learned shall feed back into source evaluation, detection rule tuning, and risk assessment updates."),
    ]),

    ("Security Monitoring Integration", [
        ("A.5.7-54", "Threat Intelligence",
         "Threat intelligence shall be integrated with security monitoring capabilities to enhance detection effectiveness."),
        ("A.5.7-55", "[Siem] Integration: Operational Iocs",
         "[SIEM] integration: Operational IOCs shall be ingested into the [SIEM] for correlation with internal security events. Where automated ingestion is not feasible, manual IOC entry shall be performed on a defined schedule."),
        ("A.5.7-56", "Endpoint Detection: Where [Edr] Or",
         "Endpoint detection: Where [EDR] or endpoint protection platforms support threat intelligence feed integration, relevant IOCs shall be deployed to endpoint detection systems."),
        ("A.5.7-57", "Email Security: Known Phishing Domains,",
         "Email security: Known phishing domains, malicious sender addresses, and attachment hashes shall be deployed to email gateway filtering rules."),
        ("A.5.7-58", "Web Filtering: Malicious Domains And",
         "Web filtering: Malicious domains and URLs from threat intelligence shall be deployed to web filtering or DNS security systems."),
        ("A.5.7-59", "Firewall Rules: Known Malicious Ip",
         "Firewall rules: Known malicious IP addresses and network indicators shall be deployed to perimeter and internal firewall blocklists, subject to false positive validation."),
        ("A.5.7-60", "Track The Following To Assess",
         "The organisation shall track the following to assess integration effectiveness:."),
    ]),

    ("Avail & Business Cont", [
        ("A.5.7-61", "Threat Intelligence",
         "Threat intelligence shall inform business continuity planning and service availability protection per Controls A.5.29-30."),
        ("A.5.7-62", "The Following Threat Categories",
         "The following threat categories shall be prioritised for detection and response due to their potential impact on service availability:."),
        ("A.5.7-63", "Threat Intelligence",
         "Threat intelligence shall provide the following inputs to business continuity and disaster recovery planning:."),
        ("A.5.7-64", "Threat Scenarios — Annual Review Of",
         "Threat scenarios — Annual review of plausible threat scenarios (ransomware, DDoS, data destruction) based on observed industry incidents shall inform business impact analysis (BIA) and recovery strategies."),
        ("A.5.7-65", "Recovery Time Objectives (Rto)",
         "Recovery time objectives (RTO) validation — Observed attack speeds in the wild (e.g., ransomware encryption time, DDoS attack duration) shall be compared against RTO assumptions to validate recovery feasibility."),
        ("A.5.7-66", "Third-Party Dependency Risks —",
         "Third-party dependency risks — Intelligence on supply chain attacks or cloud service provider incidents shall trigger reviews of vendor contingency plans and alternative provider readiness."),
        ("A.5.7-67", "Tabletop Exercise Scenarios — Annual",
         "Tabletop exercise scenarios — Annual business continuity exercises shall incorporate realistic threat scenarios derived from current threat intelligence."),
    ]),

    ("Effectiveness Measurement", [
        ("A.5.7-68", "Measure Threat Intelligence Programme",
         "The organisation shall measure threat intelligence programme effectiveness to justify investment, identify improvement opportunities, and demonstrate value to stakeholders."),
        ("A.5.7-69", "The Following Metrics",
         "The following metrics shall be tracked and reported to the CISO quarterly:."),
        ("A.5.7-70", "The Ciso",
         "The CISO shall conduct an annual review of the threat intelligence programme covering:."),
    ]),

    ("Testing and Validation", [
        ("A.5.7-71", "Test Threat Intelligence Effectiveness",
         "The organisation shall test threat intelligence effectiveness to validate that intelligence sources and detection integrations perform as intended."),
        ("A.5.7-72", "Testing Activities",
         "All testing activities shall be documented with:."),
    ]),

    ("Customer Threat Intelligence", [
        ("A.5.7-73", "For Customers With Dedicated Service",
         "For customers with dedicated service agreements, the organisation shall:."),
        ("A.5.7-74", "Be Invited To Provide Feedback On",
         "Customers shall be invited to provide feedback on intelligence utility and relevance."),
    ]),

    ("Compliance Measurement", [
        ("A.5.7-75", "The Following Metrics",
         "The following metrics shall be tracked and reported to the CISO quarterly:."),
        ("A.5.7-76", "Metrics Breaching Red Thresholds",
         "Metrics breaching red thresholds shall be escalated to the CISO for immediate attention and reported at the next Management Review."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.7
# =============================================================================
