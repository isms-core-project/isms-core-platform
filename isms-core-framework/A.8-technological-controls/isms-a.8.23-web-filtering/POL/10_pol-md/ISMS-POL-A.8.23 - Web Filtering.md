**ISMS-POL-A.8.23 — Web Filtering**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Web Filtering |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.23 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO)
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.23.1-UG/TG (Filtering Infrastructure Assessment)
- ISMS-IMP-A.8.23.2-UG/TG (Network Coverage Assessment)
- ISMS-IMP-A.8.23.3-UG/TG (Policy Configuration Assessment)
- ISO/IEC 27001:2022 Control A.8.23

---

## Executive Summary

This policy establishes [Organization]'s requirements for web filtering controls to protect users and organizational information from web-based threats in accordance with ISO/IEC 27001:2022 Control A.8.23.

**Scope**: This policy applies to all network segments where users access internet resources, all organizational personnel, and all web filtering technologies regardless of deployment model.

**Purpose**: Define organizational requirements for web filtering control implementation and governance. This policy establishes WHAT web filtering protection is required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8.23 (UG/TG variants).

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (PCI DSS, FINMA, DORA, NIS2) apply where [Organization]'s business activities trigger applicability.

---

# Control Alignment & Scope

## ISO/IEC 27001:2022 Control A.8.23

**ISO/IEC 27001:2022 Annex A.8.23 - Web Filtering**

> *Access to external websites shall be managed to reduce exposure to malicious content.*

**Control Objective**: Establish organizational policy for web filtering controls protecting users and information from web-based threats throughout the organization's network infrastructure.

**This Policy Addresses**:

- Web filtering control requirements based on threat landscape and organizational risk appetite
- Network coverage requirements ensuring comprehensive protection
- Organizational roles and responsibilities for web filtering governance
- Exception and incident management frameworks
- Integration with [Organization]'s risk assessment and treatment processes

## What This Policy Does

This policy:

- **Defines** web filtering control requirements aligned with organizational risk assessment
- **Establishes** governance framework for web filtering decision-making
- **Specifies** accountability for web filtering control implementation
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Specify technical implementation details** (see ISMS-IMP-A.8.23 Implementation Guides)
- **Define specific filtering categories or URL lists** (see ISMS-IMP-A.8.23 Policy Configuration Assessment)
- **Provide system-specific configuration procedures** (see ISMS-IMP-A.8.23 Assessment Guides)
- **Select filtering technologies or vendors** (technology selection based on [Organization]'s risk assessment)
- **Replace risk assessment** (web filtering controls selected based on [Organization]'s risk treatment)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite evolving threat landscape
- Technical agility for technology updates without policy revision
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- All network segments providing internet connectivity (on-premises, wireless, remote access, cloud)
- All users (employees, contractors, temporary staff, guests where applicable)
- All devices accessing organizational network resources
- All web filtering implementations regardless of deployment model (gateway, cloud-based, endpoint, DNS-based)
- All third-party services providing network access

**Out of Scope**:

- Email filtering (covered under separate email security policies)
- Network intrusion prevention beyond web-based threats (covered under network security policies)
- Endpoint antivirus/anti-malware (covered under endpoint protection policies)
- Data loss prevention (covered under DLP policies, though web filtering may support DLP objectives)

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**. 

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG** | All Swiss operations | Art. 8 - Appropriate technical and organizational measures |
| **EU GDPR** | When processing EU personal data | Art. 32 - Security measures including access controls |
| **ISO/IEC 27001:2022** | Certification scope | Control A.8.23 - Documented policy and implementation |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Web Filtering Requirements |
|-----------|-------------------|----------------------------|
| **PCI DSS v4.0** | Processing payment card data | Network security controls, malware protection |
| **FINMA** | Swiss regulated financial institution | Technical and organizational measures per risk assessment |
| **DORA** | EU financial services entity | Network security controls, cyber resilience |
| **NIS2** | Essential/important entity (EU) | Security measures for network and information systems |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- NIST Cybersecurity Framework (Protect function)
- CIS Controls v8 (Control 9: Email and Web Browser Protections)
- MITRE ATT&CK Framework (Defense techniques)
- OWASP (Web Security Testing Guide)

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent requirements apply where multiple regulations overlap.

---

# Web Filtering Requirements Framework

## Threat Protection Requirements (Mandatory)

[Organization] implements web filtering capabilities to protect against web-based threats.

**Required Protection Categories**:

| Threat Category | Protection Requirement | Implementation Priority |
|----------------|------------------------|-------------------------|
| **Malicious Content** | Block known malware distribution sites | **Mandatory** |
| **Phishing** | Block credential harvesting and brand impersonation | **Mandatory** |
| **Command & Control** | Block C2 infrastructure and botnet communication | **Mandatory** |
| **Exploit Delivery** | Block sites hosting exploit kits and vulnerability exploitation | **Mandatory** |

**Implementation Note**: Specific threat intelligence feeds, update frequencies, and blocking mechanisms are defined in ISMS-IMP-A.8.23-1 (Filtering Infrastructure Assessment) and ISMS-IMP-A.8.23-3 (Policy Configuration Assessment).

**Threat Intelligence**: [Organization] SHALL utilize threat intelligence from reputable sources to maintain current protection against emerging threats. Threat intelligence integration procedures documented in ISMS-IMP-A.8.23-3.

## Category Filtering Approach (Risk-Based)

[Organization] defines web filtering category approach based on organizational risk appetite and compliance requirements.

**Organizational Approach Options**:

[Organization] SHALL document one of the following approaches:

1. **Restrictive Blocking**: Specific website categories blocked based on risk assessment and compliance requirements
2. **Trust-Based Monitoring**: Most categories permitted with activity monitoring and acceptable use policy enforcement
3. **Hybrid Risk-Based**: High-risk categories blocked, medium-risk monitored, low-risk permitted based on risk classification

**Implementation Note**: Selected approach, specific blocked/monitored categories, and risk classification criteria are documented in ISMS-IMP-A.8.23-3 (Policy Configuration Assessment). Category decisions reviewed based on risk assessment and communicated to all users.

**Adopted Organizational Approach:** [Organization] implements a **Hybrid Risk-Based** approach:

- **Blocked (High-Risk):** Malware distribution, phishing, C2/botnets, exploit kits, illegal content, anonymizers/open proxies
- **Monitored (Medium-Risk):** File sharing, streaming media, social networking, personal webmail
- **Permitted (Low-Risk):** Business, news, education, technology, government, financial services

Category classifications and blocking rules are documented in ISMS-IMP-A.8.23-3 (Policy Configuration Assessment) and reviewed quarterly. Changes to category classifications require Security Team review and CISO approval.

## Network Coverage Requirements

[Organization] implements web filtering controls to achieve comprehensive coverage.

**Coverage Principle**: All paths to internet from organizational devices SHALL traverse web filtering controls.

**Required Coverage**:

- Primary internet connection points
- Wireless networks (corporate access)
- Remote access infrastructure
- Cloud-hosted resources accessing internet
- Branch office connections

**Implementation Note**: Network topology documentation, coverage verification procedures, and gap identification methods are defined in ISMS-IMP-A.8.23-2 (Network Coverage Assessment).

**Coverage Verification**: [Organization] SHALL verify filtering coverage through technical testing. Testing methodology and frequency defined in ISMS-IMP-A.8.23-2.

**Acceptable Coverage Exceptions**:

- Guest networks (requirements defined in Annex A: Guest Network Filtering Requirements)
- Dedicated B2B partner connections (documented, risk-assessed, approved by CISO)
- Air-gapped networks with no internet connectivity
- Specific user groups with documented and approved exceptions

## Logging and Monitoring

[Organization] implements logging of web filtering events to support security monitoring and incident investigation.

**Logging Requirements**:

- Web access events (permitted and blocked)
- Security events (threat blocks, policy violations)
- User attribution (where technically available and privacy-compliant)
- Sufficient detail for incident investigation and forensic analysis

**Log Retention:**

- Security events (threat blocks, C2 attempts, circumvention attempts, policy violations): Minimum **12 months**
- General web access logs (permitted requests): Minimum **90 days**
- Extended retention applies where regulatory requirements mandate longer periods (per ISMS-POL-00 Section 4.2)
- Logs protected with appropriate integrity and confidentiality controls per A.8.15
- Log deletion requires documented approval and follows data retention policy procedures

**Implementation Note**: Specific logging fields, retention periods, storage requirements, and monitoring procedures are defined in ISMS-IMP-A.8.23-4 (Monitoring & Response Assessment).

**Privacy Compliance**: Logging SHALL comply with applicable privacy regulations per ISMS-POL-00. Users informed of monitoring through acceptable use policy. Access to logs restricted to authorized personnel with legitimate need.

---

# Roles, Governance & Incident Response

## Roles and Responsibilities

**Executive Management / Board**:

- Accountable for approving web filtering policy and strategy
- Ensuring adequate resources and budget
- Accepting residual risks
- Supporting security program

**Chief Information Security Officer (CISO)**:

- Accountable for overall web filtering policy and program effectiveness
- Approving high-risk exceptions and policy changes
- Defining organizational risk appetite for web filtering
- Escalating critical issues to Executive Management
- Annual policy review and approval

**Security Team**:

- Responsible for implementing web filtering policy requirements
- Configuring and maintaining filtering solutions
- Monitoring events and responding to security incidents
- Processing exception requests and conducting risk assessments
- Integrating threat intelligence feeds
- Conducting periodic coverage assessments

**IT Operations / Network Team**:

- Responsible for deploying and maintaining web filtering infrastructure
- Ensuring network topology supports filtering coverage
- Providing technical support for filtering systems
- Coordinating changes with Security Team

**Users (All Personnel)**:

- Responsible for complying with web filtering policies and acceptable use policy
- Reporting false positives and security concerns
- Using exception process for legitimate business needs
- Prohibited from attempting to bypass web filtering controls

**Detailed RACI Matrix**: Complete roles and responsibilities matrix documented in ISMS-IMP-A.8.23 Implementation Guides.

## Assessment and Verification

[Organization] verifies web filtering control effectiveness through structured assessment.

**Assessment Domains**:
1. Filtering Infrastructure: Deployed technologies and capabilities
2. Network Coverage: Topology mapping and coverage verification
3. Policy Configuration: Filtering rules, categories, and threat feeds
4. Monitoring & Response: Logging, alerting, and incident response capabilities
5. Compliance Summary: Consolidated metrics and gap analysis

**Implementation Note**: Assessment methodology, evidence requirements, workbooks, and compliance calculation procedures are defined in ISMS-IMP-A.8.23 (Implementation Guidance Suite). Assessment tools maintained separately from policy to enable frequent updates.

**Assessment Frequency:**

- Comprehensive assessment: **Annually** (aligned with internal audit programme, typically Q4)
- Periodic verification: **Quarterly** (coverage testing, threat feed currency, policy effectiveness)
- Triggered assessment: **Within 30 days** of:
  - Significant security incidents involving web-based threats
  - Major infrastructure changes affecting filtering coverage
  - Deployment of new filtering solutions or major version upgrades
  - Audit findings requiring remediation verification

## Exception Management

**Exception Request Requirements**:

Exceptions to web filtering policy requirements require:

- Documented business or technical justification
- Risk assessment (likelihood, impact, residual risk)
- Compensating controls (where feasible)
- Timeline for achieving full compliance (where applicable)
- Formal approval per authority matrix

**Approval Authority**:

- **Single URL/domain exceptions**: Security Team Lead approval
- **Category exceptions (individual)**: Security Team Lead + Manager approval
- **Category exceptions (group/department)**: CISO + Department Head approval
- **High-risk exceptions**: CISO + Executive Management approval
- **Threat protection exceptions**: NOT PERMITTED (malware, phishing, C2 blocks cannot be bypassed)

**Monitoring**: Active exceptions reviewed based on risk level. Exception activity monitored for policy compliance. Exceptions revoked if risk profile changes or business justification no longer valid.

**Exception Template**: ISMS-IMP-A.8.23 Exception Request procedures provide standardized documentation format and workflow.

## Incident Response

**Web Filtering Security Incidents** include:

- Command and Control (C2) communication attempts (indicates potential compromise)
- Repeated malware or phishing attempts from specific users/systems
- Circumvention attempts (proxy usage, VPN to bypass filtering)
- Web filtering system failures or coverage gaps
- False positive patterns indicating misconfiguration

**Response Process**:
1. **Detection & Reporting**: Security events trigger alerts per severity
2. **Assessment**: Incident classification based on threat level
3. **Investigation**: Root cause analysis and scope determination
4. **Containment**: Immediate actions based on incident type
5. **Recovery**: System restoration and preventive measures
6. **Post-Incident**: Lessons learned and control improvements

**Critical Incidents**: C2 communication attempts treated as high-priority security incidents requiring immediate investigation of potentially compromised systems.

**Detailed Procedures**: ISMS-IMP-A.8.23-4 (Monitoring & Response Assessment) provides incident classification criteria, response workflows, escalation procedures, and coordination with endpoint security teams.

## Policy Governance

**Policy Review**:

- **Frequency**: Annual minimum
- **Triggers**: Regulatory changes, major incidents, significant threat landscape changes, organizational changes, audit findings
- **Reviewers**: CISO, IT Security Team, Legal/Compliance, IT Operations
- **Approval**: CISO (technical), Executive Management (strategic)

**Implementation Standards Review**:

- **Frequency**: Based on threat landscape evolution (at least semi-annual)
- **Authority**: Security Team proposes updates, CISO approves
- **Note**: Implementation standard updates (ISMS-IMP-A.8.23) do not require policy revision

**Policy Updates**:

- **Minor** (clarifications, references): CISO approval, communication within 30 days
- **Major** (scope changes, new requirements): Full approval chain, implementation timeline per change management
- **Emergency** (critical threats): CISO approval, immediate communication and implementation

**Communication**: Policy published in ISMS document repository. Changes communicated organization-wide. Training provided for significant changes affecting user behavior or responsibilities.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Web filtering controls selected based on [Organization]'s risk assessment
- Threat landscape assessment determines protection requirements
- Risk treatment plans document web filtering control implementation

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Control A.8.23 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported

**Related Controls**:

- A.5.10 (Acceptable Use of Information): Defines acceptable internet usage
- A.8.7 (Protection against malware): Malware protection controls including web-based threats
- A.8.16 (Monitoring Activities): Integrates with security monitoring program
- A.8.20 (Networks Security): Network-level security controls
- A.8.22 (Segregation of Networks): Network segmentation strategy
- A.5.24 (Information Security Incident Management): Incident response framework

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.8.23 Suite):

- ISMS-IMP-A.8.23-1: Filtering Infrastructure Assessment (technologies, capabilities, threat intelligence)
- ISMS-IMP-A.8.23-2: Network Coverage Assessment (topology mapping, coverage verification)
- ISMS-IMP-A.8.23-3: Policy Configuration Assessment (categories, rules, blocking policies)
- ISMS-IMP-A.8.23-4: Monitoring & Response Assessment (logging, alerting, incident procedures)
- ISMS-IMP-A.8.23-5: Compliance Dashboard (consolidated compliance reporting)

**Assessment Tools**:

- Excel-based assessment workbooks with automated compliance calculations
- Evidence registers
- Gap analysis templates
- Remediation tracking

**Supporting Materials**:

- Exception request procedures
- User communication templates
- Quick reference guides
- Incident response playbooks

## Regulatory Mapping

This policy addresses web filtering requirements from:

| Requirement Category | Swiss nDSG | EU GDPR | ISO 27001 | PCI DSS* | FINMA* | DORA/NIS2* |
|---------------------|-----------|---------|-----------|---------|--------|------------|
| Web threat protection | Art. 8 | Art. 32 | A.8.23 | Req. 1, 2, 5 | Risk-Based | Network Security |
| Access controls | Art. 8 | Art. 32 | A.8.23 | Req. 7 | Risk-Based | Access Controls |
| Logging & monitoring | Art. 8 | Art. 32 | A.8.23, A.8.15 | Req. 10 | Risk-Based | Monitoring |
| Incident response | Art. 8 | Art. 33 | A.8.23, A.5.24 | Req. 12.10 | Incident Mgmt | Incident Response |

*Conditional applicability per ISMS-POL-00

**Note**: Specific regulatory interpretation and compliance verification procedures are documented in ISMS-IMP-A.8.23-5 (Compliance Dashboard).

## Training & Awareness

**Security Awareness** (All Personnel):

- Annual training module on web filtering and acceptable use
- User responsibilities and reporting procedures
- Recognizing phishing and suspicious websites

**Technical Training** (IT/Security Staff):

- Web filtering technology configuration and maintenance
- Threat intelligence integration
- Incident response procedures
- Exception request evaluation

**Operational Training** (IT Operations, Help Desk):

- False positive handling and escalation
- User support procedures
- Common blocking scenarios and resolution

---

# Definitions

**Web Filtering**: Technology-based controls that monitor, restrict, or block access to web resources based on defined security policies. Web filtering analyzes URLs, domains, content, and protocols to permit, deny, or log access attempts.

**Threat Protection**: Capabilities to block access to known malicious websites including malware distribution sites, phishing pages, command-and-control infrastructure, and exploit delivery mechanisms.

**Category Filtering**: Capability to block or monitor access to website categories (e.g., social media, gambling, streaming) based on organizational acceptable use policies and risk appetite.

**Network Coverage**: The extent to which web filtering controls are deployed across all network segments and access methods where users can reach the internet.

**Exception**: Temporary or permanent deviation from standard filtering policies, granted through formal approval process with documented business justification and risk acceptance.

**C2 (Command and Control)**: Infrastructure used by malware to communicate with attackers, enabling remote control and data exfiltration.

**False Positive**: Legitimate website incorrectly blocked by web filtering system, requiring review and policy adjustment.

**Threat Intelligence**: Curated information about current and emerging web-based threats, used to update filtering policies and protect against new attack vectors.

**Threat Intelligence Feed**: Automated, continuously-updated data stream from threat intelligence providers that supplies current indicators of compromise (IOCs), malicious URLs, IP addresses, domains, and threat actor infrastructure. Feeds integrate with web filtering solutions to enable real-time protection against newly-identified threats.

---

# Annex A: Guest Network Filtering Requirements

**Scope:** This annex defines web filtering requirements for guest network segments providing internet access to non-organizational users (visitors, contractors without corporate credentials, BYOD on guest SSID).

**Filtering Approach:** Guest networks implement a **Restrictive Blocking** approach:

- **Blocked:** All threat protection categories (malware, phishing, C2, exploits) — no exceptions permitted
- **Blocked:** High-risk content categories (adult content, illegal content, anonymizers/proxies)
- **Permitted:** General web access for legitimate business use

**Coverage:** All guest network egress points SHALL traverse web filtering controls before reaching the internet.

**Logging:** Guest network web access logging is enabled for security event detection. User attribution is limited to IP/MAC address (no personal identification) in compliance with privacy requirements.

**Exceptions:** No category exceptions are permitted for guest networks. Users requiring broader access must connect via corporate network with appropriate credentials.

**Governance:** Guest network filtering configuration is managed by the Security Team and reviewed quarterly as part of the standard web filtering assessment cycle (ISMS-IMP-A.8.23-3).

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements. Implementation procedures are documented in ISMS-IMP-A.8.23 (UG/TG).*
<!-- QA_VERIFIED: 2026-02-01 -->
