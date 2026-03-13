<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.7:framework:POL:a.5.7 -->
**ISMS-POL-A.5.7 – Threat Intelligence**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Threat Intelligence Policy |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.7 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial policy for ISO 27001:2022 certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO)
- Risk: Chief Risk Officer (CRO)
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.5.7.1-UG/TG (Threat Intelligence Sources Assessment)
- ISMS-IMP-A.5.7.2-UG/TG (Intelligence Collection & Analysis Assessment)
- ISMS-IMP-A.5.7.3-UG/TG (Intelligence Integration & Distribution Assessment)
- ISO/IEC 27001:2022 Control A.5.7

---

# Executive Summary

This policy establishes [Organisation]'s requirements for threat intelligence to enable proactive defense, inform risk management, and enhance security operations in accordance with ISO/IEC 27001:2022 Control A.5.7.

**Purpose**: Define organisational requirements for threat intelligence governance. This policy establishes WHAT threat intelligence capabilities are required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.7 (UG/TG variants).

**Scope**: This policy applies to:

- All threat intelligence activities (collection, analysis, production, dissemination)
- All intelligence types (strategic, tactical, operational)
- All intelligence sources (commercial platforms, OSINT, government feeds, internal telemetry)
- All organisational personnel involved in security operations
- All security tools integrating threat intelligence

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00, including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Sector-specific requirements (PCI DSS v4.0.1, FINMA, DORA, NIS2) apply where [Organisation]'s business activities trigger applicability.

---

# Scope

## ISO/IEC 27001:2022 Control A.5.7

**ISO/IEC 27001:2022 Annex A.5.7 - Threat Intelligence**

> *Information relating to information security threats should be collected and analysed to produce threat intelligence.*

**Control Objective**: Establish organisational policy for threat intelligence controls enabling proactive threat detection, informing risk management decisions, prioritizing security investments, and enhancing incident response effectiveness.

## Policy Boundaries

**This Policy Addresses** (WHAT/WHO):

- Threat intelligence collection requirements from multiple source types
- Intelligence analysis and production requirements
- Intelligence dissemination requirements to stakeholders
- Integration requirements with risk assessment (ISO 27001 Clause 6.1)
- Integration requirements with incident management (Controls A.5.24-5.28)
- Organisational roles and responsibilities
- Exception and governance frameworks

**This Policy Does NOT Address** (HOW - see ISMS-IMP-A.5.7):

- Technical implementation details and platform configuration
- Specific threat intelligence tools or vendor selection
- Detailed analysis frameworks and analyst procedures
- Specific KPI measurement methodologies
- IOC deployment procedures
- Source evaluation scoring criteria

## Organisational Coverage

**In Scope**:

- All employees (permanent, temporary, contractors)
- All security operations and incident response teams
- All risk management and compliance functions
- Third-party service providers with access to threat intelligence
- All organisational locations and business units

**Out of Scope**:

- Offensive cyber operations or retaliatory actions (prohibited)
- Law enforcement investigations (cooperation supported, not conducted)
- Vulnerability scanning and penetration testing (covered under Control A.8.8)
- Threat hunting operations (covered under Control A.8.16)

---

# Policy Statements

## Threat Intelligence Collection

[Organisation] SHALL implement threat intelligence collection from multiple source categories to ensure comprehensive threat visibility.

**Required Source Categories**:

- **Commercial Platforms**: Curated threat intelligence feeds with validation
- **Open-Source Intelligence (OSINT)**: Public threat data, vulnerability databases
- **Government/CERT Feeds**: National CERT advisories, critical infrastructure alerts
- **Industry Sharing (ISAC/ISAO)**: Sector-specific threats and peer collaboration (recommended)
- **Internal Telemetry**: Security tool alerts, incident data, forensic findings

**Source Management Requirements**:

- All sources SHALL be evaluated for reliability and credibility before operationalization
- Sources SHALL be validated periodically for accuracy and performance
- Data protection requirements SHALL be applied to all collected intelligence
- Third-party sharing SHALL be governed by Traffic Light Protocol (TLP) classifications

**Implementation Reference**: Source inventory and evaluation criteria documented in ISMS-IMP-A.5.7.1.

## Threat Intelligence Analysis and Production

[Organisation] SHALL implement structured intelligence analysis to transform raw threat data into actionable intelligence.

**Intelligence Production Requirements**:

**Strategic Intelligence** (Executive Audience):

- Threat landscape assessments and trend analysis
- Risk-based security investment recommendations
- Produced at minimum quarterly, or triggered by significant events

**Tactical Intelligence** (Security Operations Audience):

- Threat actor profiles and TTPs
- Campaign analysis and attack patterns
- Produced at minimum monthly, or triggered by emerging threats

**Operational Intelligence** (Technical Audience):

- Indicators of Compromise (IOCs) for detection
- Malware signatures and behavioral indicators
- Produced continuously via automated feeds, with daily analyst review

**Quality Requirements**:

- All intelligence products SHALL cite sources with reliability assessment
- Intelligence SHALL be validated through multiple sources where possible
- Intelligence SHALL be connected to [Organisation]'s threat model and assets
- Intelligence SHALL include actionable recommendations or detection guidance
- Intelligence SHALL be classified using TLP and internal classification schemes

**Implementation Reference**: Analysis frameworks and production metrics documented in ISMS-IMP-A.5.7.2.

## Threat Intelligence Dissemination

[Organisation] SHALL implement structured intelligence dissemination ensuring the right intelligence reaches the right stakeholders.

**Dissemination Requirements**:

- Executive Management SHALL receive strategic threat assessments
- Security Operations SHALL receive operational IOCs and tactical TTPs
- Incident Response SHALL receive investigation-relevant intelligence
- Risk Management SHALL receive threat data for risk assessment updates
- IT Operations SHALL receive infrastructure-relevant blocking guidance

**Sharing Controls**:

- External sharing SHALL be governed by Traffic Light Protocol (TLP)
- Intelligence consumers SHALL provide feedback on intelligence effectiveness
- Bidirectional feedback loops SHALL be established between consumers and producers

**Implementation Reference**: Dissemination tracking and stakeholder engagement documented in ISMS-IMP-A.5.7.3.

## Risk Assessment Integration (MANDATORY)

Threat intelligence SHALL inform [Organisation]'s risk assessment process per ISO 27001:2022 Clause 6.1.

**Integration Requirements**:

- Threat intelligence findings SHALL inform likelihood estimates for security risks
- Emerging threat campaigns SHALL trigger risk reassessment when targeting [Organisation]'s sector
- Vulnerability exploitation intelligence SHALL inform impact assessments
- Threat intelligence recommendations SHALL inform control selection and prioritization
- Risk register updates SHALL cross-reference supporting threat intelligence reports

**Documentation Requirements**:

- Each risk assessment update SHALL document the threat intelligence source
- Traceability between threat intelligence reports and risk register entries SHALL be maintained

**Implementation Reference**: Risk integration tracking documented in ISMS-IMP-A.5.7.3.

## Incident Management Integration (MANDATORY)

Threat intelligence SHALL enhance incident detection, investigation, and response per Controls A.5.24-5.28.

**Integration Requirements**:

- IOCs from threat intelligence SHALL be deployed to detection tools
- Threat actor TTPs SHALL be translated into detection rules
- Threat intelligence SHALL provide context during incident investigations
- Incident findings SHALL contribute to internal threat intelligence collection
- Post-incident reviews SHALL validate threat intelligence effectiveness

**Implementation Reference**: Incident-TI integration tracking documented in ISMS-IMP-A.5.7.3.

## Vulnerability Management Integration (OPTIONAL)

When [Organisation] implements Control A.8.8 (Management of Technical Vulnerabilities), threat intelligence integration is OPTIONAL but recommended.

**If Implemented**:

- Vulnerability intelligence SHALL combine CVE data with exploitation status
- Active exploitation intelligence SHALL inform remediation prioritization
- CVSS scores combined with threat intelligence SHALL enable risk-based prioritization

**Implementation Reference**: When implemented, VulnerabilityThreatLink integration documented in ISMS-IMP-A.5.7.2 and ISMS-IMP-A.8.8.

## Effectiveness Measurement

[Organisation] SHALL measure threat intelligence program effectiveness through objective metrics.

**Required Measurement Areas**:

- Risk assessment updates driven by threat intelligence
- Incidents prevented or detected through threat intelligence
- Source accuracy and performance
- Incident investigation enrichment with threat intelligence
- Security decisions informed by threat intelligence
- Stakeholder satisfaction with intelligence products

**Program Maturity**:

- [Organisation] SHALL assess threat intelligence program maturity annually
- Assessment SHALL cover collection, analysis, dissemination, operationalization, and governance

**Implementation Reference**: Effectiveness metrics and KPI tracking documented in Summary Dashboard.

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Accountabilities |
|------|------------------|
| **Executive Management** | Strategic approval, resource allocation, policy approval |
| **Chief Information Security Officer (CISO)** | Policy ownership, program oversight, exception approval |
| **Chief Risk Officer (CRO)** | Risk assessment integration, TI-driven risk updates approval |
| **Threat Intelligence Team Lead** | Program management, intelligence production, source management |
| **Threat Intelligence Analysts** | Intelligence collection, analysis, production, quality assurance |
| **Security Operations (SOC)** | Intelligence operationalization, IOC deployment, detection tuning |
| **Incident Response Team** | Intelligence application during investigations, IOC extraction |
| **IT Operations** | Technical implementation of TI-driven controls |
| **Risk Management Team** | Risk assessment updates based on threat intelligence |
| **Compliance/Legal** | Regulatory interpretation, data protection compliance |
| **All Personnel** | Threat awareness, reporting suspicious activities |

## Escalation Path

- Operational issues: Analyst → TI Team Lead → Security Team → CISO
- Technical exceptions: TI Team Lead → Security Team → CISO
- Compliance concerns: TI Team Lead → Compliance → CISO → Executive Management
- Risk-related: TI Team Lead → CRO → CISO → Executive Management
- Security incidents: Anyone → SOC → Incident Response → CISO

## Training Requirements

- **All Personnel**: Annual security awareness including threat landscape overview
- **TI Analysts**: Specialized training on analysis frameworks and report writing
- **SOC Staff**: Training on TI operationalization and IOC deployment
- **Security Leadership**: Strategic threat intelligence briefings

## Business Continuity

[Organisation] SHALL ensure continuity of critical threat intelligence capabilities:

- Primary and backup analysts designated for each intelligence function
- Source redundancy for critical intelligence categories
- Documented failover procedures for threat intelligence platform
- Annual business continuity testing for threat intelligence operations

---

# Compliance and Exceptions

## Regulatory Applicability

**Tier 1: Mandatory Compliance**

| Regulation | Key Requirements |
|------------|------------------|
| **Swiss nDSG** | Art. 8 - Technical and organisational measures for threat detection |
| **EU GDPR** | Art. 32 - Security measures including threat monitoring |
| **ISO/IEC 27001:2022** | Control A.5.7 - Threat intelligence collection and analysis |

**Tier 2: Conditional Applicability** (per ISMS-POL-00)

| Regulation | Trigger Condition |
|-----------|-------------------|
| **FINMA** | Swiss regulated financial institution |
| **DORA** | EU financial services entity |
| **NIS2** | Essential/important entity (EU) |

**Compliance Determination**: [Organisation] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent requirements apply where multiple regulations overlap.

## Exception Management

Exceptions to threat intelligence requirements require documented business justification, risk assessment, and formal approval.

**Exception Types**:

- Source coverage exceptions (budget constraints)
- Integration timeline exceptions (technical complexity)
- Resource exceptions (insufficient headcount)
- KPI target exceptions (newly implemented program)

**Exception Requirements**:

- Time-limited with explicit expiration dates
- Compensating controls documented and verified
- Quarterly review of exception necessity
- Evidence of progress toward full compliance

**Approval Authority**:

- CISO: Source, integration, and KPI exceptions
- CISO + Executive Management: Resource exceptions

**Documentation**: Exception requests and approvals maintained in exception register.

## Incident Response Integration

When threat intelligence identifies imminent or active threats, incident response procedures apply per Controls A.5.24-5.28.

**Severity-Based Response**:

- Critical/High severity findings: Immediate escalation to SOC and Incident Response
- Medium/Low severity findings: Standard intelligence dissemination process
- Emergency briefings: CISO briefed per incident severity classification

**Coordination Requirements**:

- Threat Intelligence Team supports incident investigations
- Incident Response Team extracts IOCs for intelligence sharing
- Post-incident reviews assess threat intelligence effectiveness

---

# Policy Governance

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: Regulatory changes, major incidents, significant threat landscape changes, organisational changes, audit findings
- **Reviewers**: CISO, Threat Intelligence Team Lead, Security Team, Risk Management, Compliance
- **Approval**: CISO (technical), Executive Management (strategic)

## Policy Updates

- **Minor** (clarifications, references): CISO approval, communication within 30 days
- **Major** (scope changes, new requirements): Full approval chain
- **Emergency** (critical threats): CISO approval, immediate communication

## Implementation Standards

Implementation standard updates (ISMS-IMP-A.5.7) do not require policy revision. Implementation guidance is reviewed quarterly by Security Team with CISO approval.

---

# Related Documents

## ISMS Integration

This policy integrates with [Organisation]'s Information Security Management System:

- **Risk Assessment** (Clause 6.1): Threat intelligence informs risk identification and analysis
- **Statement of Applicability** (Clause 6.1.3): Control A.5.7 applicability documented
- **Internal Audit** (Clause 9.2): Threat intelligence program included in ISMS audit scope
- **Continual Improvement** (Clause 10): Metrics contribute to ISMS performance evaluation

## Related Controls

| Control | Integration Type | Description |
|---------|------------------|-------------|
| **A.5.24-5.28** | MANDATORY | Incident Management - TI enhances detection and response |
| **A.8.16** | MANDATORY | Monitoring Activities - TI provides detection context |
| **A.8.8** | OPTIONAL | Vulnerability Management - TI prioritizes remediation |
| **A.5.19-5.22** | OPTIONAL | Supplier Security - TI assesses third-party risks |
| **A.5.23** | OPTIONAL | Cloud Security - TI covers cloud-specific threats |
| **A.8.23** | OPTIONAL | Web Filtering - TI provides malicious domain feeds |

## Implementation Resources

- **ISMS-IMP-A.5.7.1-UG/TG**: Threat Intelligence Sources Assessment
- **ISMS-IMP-A.5.7.2-UG/TG**: Intelligence Collection & Analysis Assessment
- **ISMS-IMP-A.5.7.3-UG/TG**: Intelligence Integration & Distribution Assessment

---

# Definitions

**Threat Intelligence**: Collection, analysis, and dissemination of information about current or emerging threats, enabling proactive defense and informed security decisions.

**Strategic Intelligence**: High-level intelligence addressing broad threats and trends, supporting executive decisions and long-term strategy.

**Tactical Intelligence**: Intelligence describing adversary tactics, techniques, and procedures (TTPs), supporting security operations and defense planning.

**Operational Intelligence**: Actionable technical intelligence including IOCs and detection rules, supporting immediate security operations.

**Indicator of Compromise (IOC)**: Observable artifact indicating a security breach has occurred or is occurring (IP addresses, domains, file hashes).

**Tactics, Techniques, and Procedures (TTPs)**: Patterns of activities used by threat actors, documented in frameworks like MITRE ATT&CK.

**Traffic Light Protocol (TLP)**: Information sharing standard using color codes (RED, AMBER, AMBER+STRICT, GREEN, CLEAR) to indicate sharing restrictions.

**CVSS (Common Vulnerability Scoring System)**: Standard for assessing vulnerability severity (0.0-10.0). CVSS 4.0 is current standard; CVSS 3.1 remains widely deployed.

**Threat Actor**: Individual, group, or organisation conducting malicious cyber activities.

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Evidence required to demonstrate this policy is adequately documented and approved:

- ✅ This policy document (ISMS-POL-A.5.7 v1.0)
- ✅ Approval signatures from CISO, Executive Management
- ✅ Threat intelligence governance framework defined (Section 2.1)
- ✅ Source types and collection requirements documented (Section 2.2)
- ✅ Analysis and production requirements specified (Section 2.3)
- ✅ Distribution and stakeholder requirements documented (Section 2.4)
- ✅ Risk assessment integration requirements defined (Section 2.5)
- ✅ Incident management integration requirements specified (Section 2.6)
- ✅ Roles and responsibilities assigned (Section 3)
- ✅ Governance and exception procedures defined (Section 3.6)
- ✅ Integration with related controls documented (Section 4.1)

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Threat intelligence source assessments completed per ISMS-IMP-A.5.7.1 (source inventory, Admiralty Code evaluations, performance validation)
- Intelligence collection and analysis assessments per ISMS-IMP-A.5.7.2 (coverage analysis, MITRE ATT&CK mapping, production metrics)
- Integration and distribution assessments per ISMS-IMP-A.5.7.3 (tool integration status, IOC deployment, stakeholder engagement)
- Risk assessment updates driven by threat intelligence (≥3 examples per quarter with traceability)
- Prevented incidents documentation (≥3 examples per quarter with validation evidence)
- Source performance validation reports (quarterly, showing ≥85% accuracy rate)
- Incident enrichment records (≥70% of P1/P2 incidents with threat intelligence context)
- Intelligence-driven security decisions (≥5 examples per quarter with documented outcomes)
- Threat intelligence platform operational logs and usage metrics
- Strategic, tactical, and operational intelligence reports distributed to stakeholders
- Threat intelligence sharing agreements (where applicable)
- Business continuity test results for threat intelligence program (annual)
- Exception approvals for threat intelligence deviations (if applicable)
- Training completion records for threat intelligence personnel
- Effectiveness metrics tracked in Summary Dashboards

**Clarification on Compliance Evidence:**

This policy establishes threat intelligence governance framework (collection, analysis, production, and dissemination requirements). It does NOT establish:

- **Technical detection controls** (addressed in A.8.16 Monitoring Activities - threat intelligence provides context for detection rules)
- **Incident response procedures** (addressed in A.5.24-5.28 Incident Management - threat intelligence enhances investigation)
- **Vulnerability prioritization** (addressed in A.8.8 Vulnerability Management - VulnerabilityThreatLink integration is optional)
- **Specific threat actor profiles** (operational intelligence maintained in threat intelligence platform, not policy)
- **Tool selection or platform configuration** (implementation decisions based on organisational requirements)

The boundary is: POL-A.5.7 defines governance framework for threat intelligence capabilities → ISMS-IMP-A.5.7 suite provides assessment procedures → Threat intelligence platform implements technical collection/analysis → Other controls (A.8.16, A.5.24-28, A.8.8) consume threat intelligence outputs for their respective purposes.

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Chief Information Officer (CIO)** | [Name] | [Date to be set] |
| **Chief Risk Officer (CRO)** | [Name] | [Date to be set] |
| **Legal/Compliance Officer** | [Name] | [Date to be set] |
| **Executive Management** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for threat intelligence. Implementation procedures are documented in ISMS-IMP-A.5.7 (UG/TG).*

<!-- QA_VERIFIED: 2026-03-01 -->
