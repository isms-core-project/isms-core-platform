# ISMS-POL-A.5.7 – Threat Intelligence

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Threat Intelligence |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.7 |
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
- Risk: Chief Risk Officer (CRO)
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.5.7 (Implementation Guidance Suite)
- ISO/IEC 27001:2022 Control A.5.7

---

## Executive Summary

This policy establishes [Organization]'s requirements for threat intelligence to enable proactive defense, inform risk management, and enhance security operations in accordance with ISO/IEC 27001:2022 Control A.5.7.

**Scope**: This policy applies to all threat intelligence activities (collection, analysis, production, dissemination); all intelligence types (strategic, tactical, operational); all intelligence sources (commercial platforms, OSINT, government feeds, internal telemetry); all organizational personnel; and all security tools integrating threat intelligence.

**Purpose**: Define organizational requirements for threat intelligence control implementation and governance. This policy establishes WHAT threat intelligence capabilities are required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.7.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (PCI DSS, FINMA, DORA, NIS2) apply where [Organization]'s business activities trigger applicability.

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control A.5.7

**ISO/IEC 27001:2022 Annex A.5.7 - Threat Intelligence**

> *Information relating to information security threats should be collected and analysed to produce threat intelligence.*

**Control Objective**: Establish organizational policy for threat intelligence controls enabling proactive threat detection, informing risk management decisions, prioritizing security investments, and enhancing incident response effectiveness.

**This Policy Addresses**:
- Threat intelligence collection requirements from multiple source types
- Intelligence analysis and production requirements ensuring accuracy and relevance
- Intelligence dissemination requirements to appropriate stakeholders
- Integration with risk assessment (ISO 27001 Clause 6.1 - MANDATORY)
- Integration with incident management (Controls A.5.24-5.28 - MANDATORY)
- Integration with vulnerability management (Control A.8.8 - OPTIONAL when implemented)
- Organizational roles and responsibilities for threat intelligence governance
- Exception and incident management frameworks
- Integration with [Organization]'s risk assessment and treatment processes

### 1.2 What This Policy Does

This policy:
- **Defines** threat intelligence control requirements aligned with organizational risk assessment
- **Establishes** governance framework for threat intelligence decision-making and accountability
- **Specifies** mandatory threat intelligence capabilities for proactive defense
- **References** applicable regulatory requirements per ISMS-POL-00
- **Identifies** organizational roles and responsibilities for threat intelligence controls

### 1.3 What This Policy Does NOT Do

This policy does NOT:
- **Specify technical implementation details** (see ISMS-IMP-A.5.7 Implementation Guides)
- **Define specific threat intelligence platforms or tools** (technology selection based on [Organization]'s risk assessment)
- **Provide system-specific configuration procedures** (see ISMS-IMP-A.5.7 Assessment Guides)
- **List specific IOCs or threat actor profiles** (operational intelligence maintained in threat intelligence platform)
- **Replace risk assessment** (threat intelligence informs risk assessment per Clause 6.1)
- **Define detailed incident response procedures** (see ISMS-IMP-A.5.7.3 Integration Assessment)

**Rationale**: Separating policy requirements from implementation guidance enables:
- Policy stability despite evolving threat landscape and intelligence sources
- Technical agility for platform updates and source changes without policy revision
- Clear distinction between governance (policy) and execution (implementation)
- Focused audit scope (auditors verify policy compliance, not technical platform configuration)

### 1.4 Scope

**This policy applies to**:

**Intelligence Activities**:
- Collection from commercial threat intelligence platforms, OSINT sources, government feeds, ISACs/ISAOs, internal telemetry
- Analysis producing strategic intelligence (executive risk briefings), tactical intelligence (adversary TTPs, campaign analysis), operational intelligence (IOCs, detection signatures)
- Production of finished intelligence reports, threat assessments, and briefings
- Dissemination to executives, security operations, incident response, risk management, vulnerability management
- Integration into security tools (SIEM, EDR, firewalls, email gateways, proxies)

**Intelligence Types**:
- Strategic intelligence informing executive risk decisions and security strategy
- Tactical intelligence describing adversary capabilities, intentions, and TTPs
- Operational intelligence providing actionable IOCs for detection and blocking
- Technical intelligence detailing malware, exploits, and attack infrastructure
- Vulnerability intelligence combining CVEs with exploitation status for prioritization

**Organizational Coverage**:
- All employees (permanent, temporary, contractors)
- All security operations and incident response teams
- All risk management and compliance functions
- All third-party service providers with access to threat intelligence (MSSPs, vendors)
- All organizational locations and business units

**Technology Coverage**:
- All security monitoring and detection technologies
- All threat intelligence platforms and tools
- All incident response and forensic systems
- All vulnerability management systems (when Control A.8.8 implemented)
- All risk assessment and GRC platforms

**Out of Scope**:
- Offensive cyber operations, hack-back activities, or retaliatory actions (prohibited)
- Counterintelligence operations targeting insider threats (covered under separate HR security policies)
- Law enforcement investigations and criminal prosecutions (cooperation supported, not conducted)
- Vulnerability scanning and penetration testing (covered under Control A.8.8 and penetration testing policies)
- Threat hunting operations themselves (covered under Control A.8.16 Monitoring Activities - threat intelligence informs hunting)
- Malware reverse engineering at scale (performed selectively or outsourced)

### 1.5 Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**. 

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG** | All Swiss operations | Art. 8 - Appropriate technical and organizational measures for threat detection |
| **EU GDPR** | When processing EU personal data | Art. 32 - Security measures including threat monitoring and detection |
| **ISO/IEC 27001:2022** | Certification scope | Control A.5.7 - Documented policy, threat intelligence collection and analysis, integration with risk assessment |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Threat Intelligence Requirements |
|-----------|-------------------|----------------------------------|
| **FINMA** | Swiss regulated financial institution | Operational resilience, threat monitoring, incident preparedness |
| **DORA** | EU financial services entity | ICT risk management, threat intelligence capabilities, scenario analysis |
| **NIS2** | Essential/important entity (EU) | Security measures, threat detection, incident notification |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- NIST SP 800-150 (Guide to Cyber Threat Information Sharing)
- MITRE ATT&CK Framework (adversary tactics and techniques)
- CVSS 4.0/3.1 (vulnerability severity scoring)
- ENISA Threat Landscape Reports
- FIRST (Forum of Incident Response and Security Teams)

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent requirements apply where multiple regulations overlap.

---

## 2. Threat Intelligence Requirements Framework

### 2.1 Intelligence Collection Requirements (Mandatory)

[Organization] implements threat intelligence collection from multiple source types to ensure comprehensive threat visibility.

**Required Source Categories**:

| Source Category | Purpose | Implementation Priority | Minimum Coverage |
|----------------|---------|------------------------|------------------|
| **Commercial Platforms** | Curated threat intelligence feeds with validation and analysis | **Mandatory** | At least one commercial platform subscription |
| **Open-Source Intelligence (OSINT)** | Public threat data, researcher disclosures, vulnerability databases | **Mandatory** | Established collection processes |
| **Government/CERT Feeds** | National CERT advisories, critical infrastructure alerts | **Mandatory** | Subscription to relevant national CERTs |
| **Industry Sharing (ISAC/ISAO)** | Sector-specific threats, campaign intelligence, peer collaboration | Recommended | Participation in relevant industry groups |
| **Internal Telemetry** | Security tool alerts, incident data, forensic findings | **Mandatory** | SIEM, EDR, firewall log analysis |

**Source Evaluation Requirements**:

[Organization] SHALL evaluate threat intelligence sources using Admiralty Code methodology:

- **Source Reliability**: A (Completely reliable ≥95%) through F (Cannot be judged)
- **Information Credibility**: 1 (Confirmed by other sources) through 6 (Cannot be judged)
- **Minimum Acceptable Grade**: Sources rated below C3 require corroboration before operationalization
- **Validation Frequency**: Quarterly assessment of source accuracy and performance
- **Target Accuracy**: ≥85% source accuracy rate (measured quarterly via prevented incident validation)

**Data Protection and Privacy**:

Threat intelligence collection and processing SHALL comply with data protection requirements:
- Personal data in threat intelligence (email addresses, names in IOCs) processed lawfully per GDPR Art. 6
- Data minimization applied - collect only intelligence necessary for security purposes
- Retention aligned with security need and legal obligations (operational logs 90 days, security events 12 months)
- Third-party sharing governed by Traffic Light Protocol (TLP) classifications
- Data processing agreements (DPAs) with commercial threat intelligence vendors

**Implementation Note**: Source inventory, evaluation criteria, and performance tracking documented in ISMS-IMP-A.5.7.1 (Sources Assessment).

### 2.2 Intelligence Analysis and Production Requirements (Mandatory)

[Organization] implements structured intelligence analysis to transform raw threat data into actionable intelligence.

**Analysis Frameworks**:

[Organization] SHALL apply recognized analysis frameworks:

| Framework | Purpose | Application |
|-----------|---------|-------------|
| **MITRE ATT&CK** | Adversary tactics and techniques mapping | Tactical intelligence, detection engineering |
| **Diamond Model** | Intrusion analysis (Adversary, Infrastructure, Capability, Victim) | Incident investigation, attribution |
| **Cyber Kill Chain** | Attack lifecycle stages (Reconnaissance through Actions on Objectives) | Campaign analysis, defensive strategy |
| **Admiralty Code** | Source and information evaluation | Intelligence validation, confidence assessment |
| **CVSS 4.0/3.1** | Vulnerability severity scoring | Vulnerability intelligence prioritization |

**Intelligence Product Types**:

[Organization] produces intelligence at three levels:

**Strategic Intelligence** (Executive Audience):
- Threat landscape assessments and trend analysis
- Adversary capability and intention assessments
- Risk-based security investment recommendations
- Geopolitical and regulatory impact analysis
- **Frequency**: Quarterly minimum, triggered by significant events
- **Distribution**: Executive Management, CISO, CRO, Board (as applicable)

**Tactical Intelligence** (Security Operations Audience):
- Threat actor profiles and TTPs
- Campaign analysis and attack patterns
- Threat hunting recommendations
- Detection engineering guidance
- **Frequency**: Monthly minimum, triggered by emerging threats
- **Distribution**: Security Team, SOC, Incident Response, IT Operations

**Operational Intelligence** (Technical Audience):
- Indicators of Compromise (IOCs) for detection rules
- Malware signatures and behavioral indicators
- Command-and-control infrastructure identification
- Vulnerability exploitation status
- **Frequency**: Continuous (automated feeds), daily analyst review
- **Distribution**: SOC, SIEM, EDR, security tools

**Quality Standards**:

All intelligence products SHALL meet minimum quality criteria:
- **Sourcing**: Sources cited with reliability assessment
- **Validation**: Cross-referenced with multiple sources where possible
- **Relevance**: Explicitly connected to [Organization]'s threat model and assets
- **Actionability**: Clear recommendations or detection signatures provided
- **Timeliness**: Intelligence delivered within operational timeframes
- **Classification**: Marked with TLP and internal classification

**Analyst Capabilities**:

[Organization] ensures adequate analyst capability through:
- Documented analyst skill requirements and competency matrix
- Training programs covering threat analysis methodologies and frameworks
- Access to analysis tools (MITRE ATT&CK Navigator, TIP, SIEM)
- Peer review process for intelligence products
- Continuous professional development

**Implementation Note**: Analysis frameworks, production metrics, and quality criteria documented in ISMS-IMP-A.5.7.2 (Collection & Analysis Assessment).

### 2.3 Intelligence Dissemination Requirements (Mandatory)

[Organization] implements structured intelligence dissemination ensuring the right intelligence reaches the right stakeholders at the right time.

**Stakeholder-Based Distribution**:

| Stakeholder Group | Intelligence Types | Delivery Methods | Frequency |
|-------------------|-------------------|------------------|-----------|
| **Executive Management** | Strategic assessments, risk briefings | Executive summaries, board presentations | Quarterly + triggered |
| **Security Operations (SOC)** | Operational IOCs, tactical TTPs, detection rules | SIEM integration, TIP feeds, alerts | Real-time + daily digest |
| **Incident Response** | Operational IOCs, tactical TTPs, forensic intelligence | IR platform integration, case enrichment | Real-time during incidents |
| **Risk Management** | Strategic assessments, threat scenarios, likelihood data | Risk register updates, threat modeling | Quarterly + triggered |
| **Vulnerability Management** | Vulnerability exploitation status, CVSS scores, prioritization | Vulnerability scanner integration, VTL records | Weekly + emergency |
| **IT Operations** | Tactical blocking recommendations, infrastructure threats | Email bulletins, tool configurations | Weekly + emergency |

**Dissemination Channels**:

[Organization] uses multiple dissemination channels:
- **Automated Integration**: IOC feeds to SIEM, EDR, firewalls via STIX/TAXII or API
- **Intelligence Platform**: Central TIP accessible to authorized personnel
- **Email Distribution**: Threat bulletins to stakeholder distribution lists
- **Briefings**: Regular threat briefings to executives and security teams
- **On-Demand**: Ad-hoc intelligence support during investigations and assessments

**Information Sharing Controls**:

Traffic Light Protocol (TLP) governs external intelligence sharing:
- **TLP:RED**: Not for disclosure outside specific exchange (recipients only)
- **TLP:AMBER**: Limited disclosure, recipients can share within organization on need-to-know
- **TLP:AMBER+STRICT**: Limited disclosure, recipients cannot share beyond organization
- **TLP:GREEN**: Community-wide disclosure, broad sharing within community acceptable
- **TLP:CLEAR**: Public disclosure acceptable, unlimited distribution

**Feedback Mechanisms**:

[Organization] establishes bidirectional feedback between intelligence consumers and producers:
- Intelligence requirements collection (What intelligence do stakeholders need?)
- Effectiveness feedback (Was intelligence actionable? Did it prevent incidents?)
- False positive reporting (Were IOCs incorrect? What was impact?)
- Gap identification (What threats are not covered by current intelligence?)
- **Target**: ≥4.0/5.0 stakeholder satisfaction score (measured quarterly)

**Implementation Note**: Dissemination tracking, stakeholder engagement, and feedback mechanisms documented in ISMS-IMP-A.5.7.3 (Integration & Distribution Assessment).

### 2.4 Risk Assessment Integration Requirements (MANDATORY)

Threat intelligence SHALL inform [Organization]'s risk assessment process per ISO 27001:2022 Clause 6.1.

**Mandatory Integration Points**:

[Organization] integrates threat intelligence into risk assessment through:

**Likelihood Assessment**:
- Threat intelligence findings inform likelihood estimates for information security risks
- Emerging threat campaigns trigger risk reassessment when targeting [Organization]'s sector or technologies
- Threat actor capability assessments inform adversary likelihood judgments
- Historical incident data combined with threat intelligence validates likelihood estimates

**Impact Assessment**:
- Vulnerability exploitation intelligence combined with CVSS scores quantifies technical impact
- Threat actor objectives inform business impact scenarios
- Campaign intelligence indicates potential attack vectors and consequences

**Risk Treatment**:
- Threat intelligence recommendations inform control selection and prioritization
- Intelligence-driven security investments justified by threat landscape analysis
- Risk acceptance decisions informed by current threat environment

**Integration Process**:

[Organization] implements structured risk-intelligence integration:
1. **Quarterly Minimum**: Threat Intelligence Team submits risk assessment update report to Risk Management
2. **Triggered Updates**: Significant threat intelligence findings trigger immediate risk reassessment
3. **Documentation**: Each risk register update cross-references supporting threat intelligence report
4. **Evidence Trail**: ISMS-IMP-A.5.7.3 Sheet 13 tracks risk assessment updates with threat intelligence traceability

**Target**: ≥3 risk assessment updates per quarter driven by threat intelligence

**CVSS-Based Vulnerability Risk Quantification**:

When vulnerability-related risks are assessed:
- CVSS 4.0 (preferred) or 3.1 base scores quantify vulnerability severity
- Active exploitation intelligence from threat intelligence adjusts likelihood
- Combined CVSS + exploitation status enables quantitative risk scoring
- VulnerabilityThreatLink (VTL) records document CVSS scores, exploitation status, and risk determination

**Example**: "TI Report 2025-Q1-003 (CVE-2024-56789, CVSS 4.0 Base Score 9.2, active mass exploitation) → Risk REG-047 (System Availability) impact updated to 'Critical', likelihood 'High' → Emergency patching authorized by CRO on [date]"

**Audit Evidence**:
- Cross-reference: Threat Intelligence Report ID → Risk Register Entry ID
- Documentation: "How threat intelligence changed risk assessment"
- CVSS-based vulnerability risk quantification (when vulnerability-related risks)
- Tracked in: ISMS-IMP-A.5.7.3 Sheet 13 (Risk Assessment Updates)

### 2.5 Incident Management Integration Requirements (MANDATORY)

Threat intelligence SHALL enhance incident detection, investigation, and response per Controls A.5.24-5.28.

**Detection Enhancement**:
- IOCs from threat intelligence deployed to detection tools (SIEM, EDR, IDS/IPS)
- Threat actor TTPs translated into detection rules and behavioral analytics
- Threat intelligence enriches security alerts with context and attribution
- **Target**: ≥70% of P1/P2 incidents enriched with threat intelligence context

**Investigation Support**:
- Threat intelligence provides context during incident investigations
- Known adversary TTPs guide forensic analysis and evidence collection
- IOC correlation accelerates incident scoping and impact assessment
- Attribution intelligence informs response strategy

**Response Optimization**:
- Threat intelligence playbooks guide response to known threat actor campaigns
- Containment strategies informed by adversary behavior patterns
- Eradication procedures aligned with threat actor persistence mechanisms
- Recovery guidance based on similar incident lessons learned

**Feedback Loop**:
- Incident findings contribute to internal threat intelligence collection
- IOCs extracted from incidents shared with threat intelligence community
- Post-incident reviews validate threat intelligence effectiveness
- Lessons learned improve future intelligence requirements

**Integration Evidence**:
- Tracked in: ISMS-IMP-A.5.7.3 Sheet 14 (Incident-TI Integration)
- Metrics: Percentage of incidents with TI enrichment, investigation time reduction
- Documentation: Incident handler feedback on intelligence usefulness

### 2.6 Vulnerability Management Integration Requirements (OPTIONAL)

When [Organization] implements Control A.8.8 (Management of Technical Vulnerabilities), threat intelligence integration is OPTIONAL but recommended.

**VulnerabilityThreatLink (VTL) Integration**:

If implemented, threat intelligence enhances vulnerability management through VTL records:

**VTL Schema Elements**:
- CVE identifier and CVSS score (4.0 preferred, 3.1 acceptable)
- Exploitation status (proof-of-concept, active exploitation, mass exploitation)
- Threat actor attribution (which adversaries are exploiting this vulnerability)
- Campaign intelligence (targeted campaigns leveraging this vulnerability)
- Exploitation timeline (when exploitation began, exploitation velocity)
- Mitigation urgency (priority escalation based on active exploitation)

**Emergency Patching Trigger**:

VTL records enable automated priority escalation:
- **Condition**: CVSS ≥8.0 AND active mass exploitation detected
- **Action**: Automatic escalation to emergency patching workflow
- **Authority**: CRO approval for emergency change management
- **Timeline**: Remediation within 72 hours (critical), 7 days (high)

**Prioritization Formula**:

When VTL integration is enabled:
- Base Priority = CVSS Base Score (0.0-10.0)
- Exploitation Multiplier = 1.0 (no exploitation) to 2.0 (mass exploitation)
- Asset Criticality Multiplier = 1.0 (internal) to 1.5 (customer-facing production)
- Final Priority Score = Base Priority × Exploitation Multiplier × Asset Criticality Multiplier

**Integration Evidence** (if implemented):
- Tracked in: ISMS-IMP-A.5.7.2 Sheet 8 (Vulnerability_Linked_Threats)
- Tracked in: ISMS-IMP-A.8.8 (Vulnerability Management Assessment - when Control A.8.8 implemented)
- Metrics: Emergency patches triggered by threat intelligence, remediation acceleration

**Note**: This integration is OPTIONAL. Organizations may implement Control A.5.7 without Control A.8.8, or vice versa. VTL integration only applies when both controls are implemented.

### 2.7 Effectiveness Measurement Requirements (Mandatory)

[Organization] measures threat intelligence program effectiveness through objective metrics and audit evidence.

**Key Performance Indicators (KPIs)**:

| KPI | Target | Evidence Location | Purpose |
|-----|--------|-------------------|---------|
| **Risk Assessment Updates** | ≥3 per quarter | ISMS-IMP-A.5.7.3 Sheet 13 | Clause 6.1 integration proof |
| **Prevented Incidents** | ≥3 per quarter | ISMS-IMP-A.5.7.3 Sheet 7 | Program value demonstration |
| **Source Accuracy** | ≥85% | ISMS-IMP-A.5.7.1 Sheet 14 | Intelligence quality assurance |
| **Incident TI Enrichment** | ≥70% P1/P2 | ISMS-IMP-A.5.7.3 Sheet 14 | Operational integration proof |
| **Intelligence-Driven Decisions** | ≥5 per quarter | ISMS-IMP-A.5.7.3 Sheet 15 | Strategic impact demonstration |
| **Stakeholder Satisfaction** | ≥4.0/5.0 | ISMS-IMP-A.5.7.3 Sheet 10 | Consumer feedback validation |

**Program Maturity Assessment**:

[Organization] assesses threat intelligence program maturity annually:
- Collection maturity: Source diversity, coverage, reliability
- Analysis maturity: Framework usage, product quality, timeliness
- Dissemination maturity: Stakeholder coverage, integration depth, feedback loops
- Operationalization maturity: Tool integration, automation, incident support
- Governance maturity: Policy compliance, metrics tracking, continuous improvement

**Audit Evidence Categories**:

Per ISMS-POL-A.5.7 Section 4.4, [Organization] maintains six categories of audit evidence:

1. **Risk Assessment Integration**: ≥3 examples per quarter of TI → Risk Register updates
2. **Prevented Incidents**: ≥3 examples per quarter with validation evidence
3. **Source Performance**: Quarterly source accuracy validation report (≥85% target)
4. **Incident Integration**: ≥70% of P1/P2 incidents with TI enrichment evidence
5. **Intelligence-Driven Decisions**: ≥5 examples per quarter with outcomes
6. **Business Continuity**: BCP + annual test results

**Implementation Note**: Effectiveness metrics, KPI tracking, and audit evidence consolidated in ISMS-IMP-A.5.7.4 (Effectiveness Dashboard).

---

## 3. Governance & Compliance

### 3.1 Roles & Responsibilities

Threat intelligence control implementation requires clear accountability across organizational roles.

**Accountability Matrix**:

| Role | Accountabilities | Authority | Key Activities |
|------|------------------|-----------|----------------|
| **Executive Management (GL)** | Strategic approval, resource allocation, risk acceptance for TI exceptions | Final authority for policy approval, budget allocation | Annual policy approval, strategic risk decisions, resource commitment |
| **Chief Information Security Officer (CISO)** | Policy ownership, program oversight, exception approval, risk acceptance within limits | Policy approval authority, exception approval, program governance | Policy development, effectiveness monitoring, exception review, regulatory alignment |
| **Chief Risk Officer (CRO)** | Risk assessment integration, TI-driven risk updates approval, risk treatment decisions | Risk register updates, risk acceptance decisions | Quarterly TI-risk integration review, risk treatment prioritization |
| **Threat Intelligence Team Lead** | Program management, intelligence production, source management, team supervision | Operational decisions, source selection, intelligence distribution | Daily operations, source evaluation, intelligence analysis, dissemination |
| **Threat Intelligence Analysts** | Intelligence collection, analysis, production, dissemination, quality assurance | Analytical judgments within established frameworks | OSINT collection, report production, IOC validation, stakeholder support |
| **Security Operations (SOC)** | Intelligence operationalization, IOC deployment, detection tuning, incident enrichment | Security tool configuration, detection rule implementation | IOC integration into SIEM/EDR, alert triage with TI context, threat hunting |
| **Incident Response Team** | Intelligence application during investigations, IOC extraction, feedback to TI team | Investigation decisions informed by TI, forensic analysis | Incident investigation with TI context, IOC identification, post-incident TI feedback |
| **IT Operations** | Technical implementation of TI-driven blocking, infrastructure threat response | Operational implementation of security controls | Firewall rule updates, email gateway blocks, proxy configuration based on TI |
| **Risk Management Team** | Risk assessment updates based on TI, risk register maintenance | Risk scoring methodology, risk treatment recommendations | Quarterly risk review with TI input, Clause 6.1 compliance verification |
| **Compliance/Legal** | Regulatory interpretation, data protection compliance, intelligence sharing legality | Legal and regulatory guidance | Regulatory mapping, compliance assessment, legal review of TI sharing |
| **All Personnel** | Threat awareness, reporting suspicious activities, following security procedures | Individual compliance responsibility | Security awareness, incident reporting, policy adherence |

**Escalation Path**:
- Operational issues: Analyst → TI Team Lead → Security Team → CISO
- Technical exceptions: TI Team Lead → Security Team → CISO
- Compliance concerns: TI Team Lead → Compliance → CISO → Executive Management
- Risk-related: TI Team Lead → CRO → CISO → Executive Management
- Security incidents: Anyone → SOC → Incident Response → CISO (immediate escalation for critical threats)

**Training Requirements**:
- **All Personnel**: Annual security awareness training including threat landscape overview
- **TI Analysts**: Specialized training on analysis frameworks (MITRE ATT&CK, Diamond Model), source evaluation, report writing
- **SOC Staff**: Training on TI operationalization, IOC deployment, detection tuning
- **Security Leadership**: Strategic threat intelligence briefings, threat landscape trends

**Business Continuity**:

[Organization] ensures continuity of critical threat intelligence capabilities:
- **Primary Analyst**: Designated primary responsible for each intelligence product type
- **Backup Analyst**: Cross-trained backup analyst for each critical function
- **Source Redundancy**: Multiple sources for critical intelligence categories
- **Platform Backup**: Documented failover procedures for threat intelligence platform
- **Annual Testing**: Business continuity test for threat intelligence operations
- **Evidence**: BCP documented in ISMS-IMP-A.5.7.1 Sheet 15, test results tracked annually

### 3.2 Exception Management

Exceptions to threat intelligence requirements require documented business justification, risk assessment, and formal approval.

**Exception Framework**:

**Exception Types**:

| Exception Type | Example Scenario | Approval Authority | Maximum Duration |
|---------------|------------------|-------------------|------------------|
| **Source Coverage Exception** | Budget constraints prevent commercial platform subscription | CISO | 12 months with renewal |
| **Integration Timeline Exception** | Technical complexity delays SIEM integration | Security Team | 6 months (project duration) |
| **Resource Exception** | Insufficient analyst headcount for 24/7 coverage | CISO + Executive Mgmt | 12 months with hiring plan |
| **KPI Target Exception** | Newly implemented program cannot meet full targets | CISO | 6 months (ramp-up period) |

**Exception Process**:
1. **Request Submission**: Requestor documents business justification, technical constraints, compensating controls
2. **Risk Assessment**: Security Team assesses security impact, regulatory implications, risk level
3. **Approval Decision**: CISO (or delegate) approves, approves with conditions, or rejects exception
4. **Implementation**: Exception documented, monitoring established, compensating controls deployed
5. **Review**: Exceptions reviewed quarterly, renewed or remediated based on status

**Exception Requirements**:
- Time-limited exceptions with explicit expiration dates
- Compensating controls documented and verified
- Regular review (quarterly minimum) of exception necessity and effectiveness
- Evidence of progress toward full compliance
- Exception register maintained in ISMS-IMP-A.5.7.4 Dashboard

**Documentation**: Exception requests, approvals, and review logs maintained in exception register.

### 3.3 Incident Response Integration

When threat intelligence identifies imminent or active threats, incident response procedures apply per Controls A.5.24-5.28.

**Incident Classification**:

Threat intelligence findings trigger incident response based on severity:

| Severity | Definition | Response Timeline | Example |
|----------|-----------|-------------------|---------|
| **P1 - Critical** | Active exploitation of organization systems, imminent mass attack | Immediate (1 hour) | Ransomware campaign actively targeting organization, zero-day with active mass exploitation |
| **P2 - High** | Targeted campaign against organization sector, critical vulnerability with public exploit | 4 hours | APT campaign targeting hosting providers, critical vuln (CVSS ≥9.0) with working exploit code |
| **P3 - Medium** | Emerging threat relevant to organization, high-severity vulnerability | 24 hours | New threat actor targeting similar organizations, high vuln (CVSS 7.0-8.9) with PoC |
| **P4 - Low** | General threat landscape information, medium-severity vulnerability | 72 hours | Threat trend analysis, medium vuln (CVSS 4.0-6.9) |

**Response Procedures**:
- P1/P2 findings: Immediate escalation to SOC and Incident Response
- P3/P4 findings: Standard intelligence dissemination process
- Emergency briefings: CISO briefed within 1 hour for P1, 4 hours for P2
- Executive notification: Executive Management notified for P1 within 4 hours

**Coordination**:
- Threat Intelligence Team supports incident investigations with context and intelligence
- Incident Response Team extracts IOCs for threat intelligence sharing
- Post-incident reviews assess threat intelligence effectiveness
- Lessons learned improve future intelligence requirements

### 3.4 Policy Governance

**Policy Review**:
- **Frequency**: Annual minimum
- **Triggers**: Regulatory changes, major incidents, significant threat landscape changes, organizational changes, audit findings
- **Reviewers**: CISO, Threat Intelligence Team Lead, Security Team, Risk Management, Compliance
- **Approval**: CISO (technical), Executive Management (strategic)

**Implementation Standards Review**:
- **Frequency**: Quarterly (IMP assessments updated based on operational needs)
- **Authority**: Security Team proposes updates, CISO approves
- **Note**: Implementation standard updates (ISMS-IMP-A.5.7) do not require policy revision

**Policy Updates**:
- **Minor** (clarifications, references): CISO approval, communication within 30 days
- **Major** (scope changes, new requirements): Full approval chain, implementation timeline per change management
- **Emergency** (critical threats): CISO approval, immediate communication and implementation

**Communication**: Policy published in ISMS document repository. Changes communicated organization-wide. Training provided for significant changes affecting user behavior or responsibilities.

---

## 4. Implementation & References

### 4.1 Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):
- Threat intelligence informs risk identification and analysis (MANDATORY integration)
- Threat landscape assessment determines information security risks
- Risk treatment plans informed by threat intelligence recommendations
- **Target**: ≥3 risk assessment updates per quarter driven by threat intelligence

**Statement of Applicability** (ISO 27001 Clause 6.1.3):
- Control A.5.7 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported

**Internal Audit** (ISO 27001 Clause 9.2):
- Threat intelligence program included in ISMS audit scope
- Compliance with Control A.5.7 requirements verified
- Effectiveness evidence validated (six audit evidence categories)

**Continual Improvement** (ISO 27001 Clause 10):
- Threat intelligence metrics contribute to ISMS performance evaluation
- Non-conformities addressed through corrective actions
- Program maturity continuously improved based on lessons learned

**Related Controls**:
- **A.5.24-5.28 (Incident Management)**: MANDATORY integration - threat intelligence enhances detection, investigation, and response
- **A.8.16 (Monitoring Activities)**: MANDATORY integration - threat intelligence provides detection signatures and enriches monitoring
- **A.8.8 (Vulnerability Management)**: OPTIONAL integration - threat intelligence prioritizes vulnerability remediation via VTL schema (only when A.8.8 implemented)
- **A.5.19-5.22 (Supplier Security)**: OPTIONAL - threat intelligence assesses third-party risks
- **A.5.23 (Cloud Security)**: OPTIONAL - threat intelligence covers cloud-specific threats
- **A.8.23 (Web Filtering)**: OPTIONAL - threat intelligence provides malicious domain/URL feeds

### 4.2 Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.5.7 Suite):
- ISMS-IMP-A.5.7.1: Threat Intelligence Sources Assessment (15 sheets - source inventory, Admiralty Code evaluation, CVSS support verification, source performance validation, business continuity)
- ISMS-IMP-A.5.7.2: Intelligence Collection & Analysis Assessment (14 sheets - collection coverage, analysis frameworks, VulnerabilityThreatLink records with CVSS, production metrics, MITRE ATT&CK mapping)
- ISMS-IMP-A.5.7.3: Intelligence Integration & Distribution Assessment (15 sheets - tool integration, IOC deployment, stakeholder engagement, prevented incidents, risk assessment updates, incident-TI integration, intelligence-driven decisions)
- ISMS-IMP-A.5.7.4: Effectiveness Dashboard (12 sheets - consolidated metrics from all assessments, executive KPI tracking, trend analysis, audit evidence)
- ISMS-IMP-A.5.7.5: Standalone Dashboard (9 sheets - self-contained executive dashboard for board presentations)

**Assessment Tools**:
- Excel-based assessment workbooks with automated compliance calculations
- Python generators for repeatable workbook generation (5 scripts)
- Validation scripts for quality assurance (4 sanity check scripts)
- Filename normalization utility for stable dashboard external references
- Evidence registers and audit tracking
- Gap analysis and remediation tracking

**Supporting Materials**:
- Exception request procedures
- Threat intelligence report templates (strategic, tactical, operational)
- Stakeholder communication templates
- Incident integration playbooks
- Business continuity test procedures

### 4.3 Regulatory Mapping

This policy addresses threat intelligence requirements from:

| Requirement Category | Swiss nDSG | EU GDPR | ISO 27001 | FINMA* | DORA* | NIS2* |
|---------------------|-----------|---------|-----------|--------|-------|-------|
| Threat detection & monitoring | Art. 8 | Art. 32 | A.5.7 | Operational Resilience | ICT Risk Mgmt | Security Measures |
| Risk assessment integration | Art. 8 | Art. 32 | Clause 6.1, A.5.7 | Risk-Based Approach | Risk Assessment | Risk Management |
| Incident preparedness | Art. 8 | Art. 32 | A.5.7, A.5.24-5.28 | Incident Mgmt | Incident Response | Incident Notification |
| Security awareness | Art. 8 | Art. 32 | A.5.7, A.6.3 | Awareness | Training | Staff Training |

*Conditional applicability per ISMS-POL-00

**Note**: Specific regulatory interpretation and compliance verification procedures are documented in ISMS-IMP-A.5.7.4 (Effectiveness Dashboard).

### 4.4 Audit Preparation

**Audit Evidence Package** (maintained per Section 2.7):

[Organization] maintains comprehensive audit evidence demonstrating Control A.5.7 effectiveness:

1. **Risk Assessment Integration** (≥3 examples/quarter): Threat intelligence → Risk register updates with traceability
2. **Prevented Incidents** (≥3 examples/quarter): Documented incidents prevented by threat intelligence with validation
3. **Source Performance** (quarterly): Source accuracy validation report showing ≥85% accuracy rate
4. **Incident Integration** (≥70% P1/P2): Evidence of threat intelligence used during incident investigations
5. **Intelligence-Driven Decisions** (≥5 examples/quarter): Security decisions informed by threat intelligence with outcomes
6. **Business Continuity**: BCP documentation + annual test results

**Audit Preparation Timeline** (T-30 days before ISO 27001 certification audit):
- Generate all assessment workbooks (A.5.7.1 through A.5.7.4)
- Run validation scripts to ensure data quality
- Prepare audit evidence package with supporting documentation
- CISO review of audit readiness at T-14 days
- Auditor briefing materials prepared at T-7 days

**Implementation Note**: Audit preparation procedures and evidence tracking detailed in ISMS-IMP-A.5.7.4 (Effectiveness Dashboard).

---

## 5. Definitions

**Threat Intelligence**: The collection, analysis, and dissemination of information about current or emerging threats to organizational assets, enabling proactive defense and informed security decision-making.

**Strategic Intelligence**: High-level intelligence addressing broad threats, trends, and adversary capabilities, supporting executive decision-making and long-term security strategy.

**Tactical Intelligence**: Intelligence describing adversary tactics, techniques, and procedures (TTPs), campaign patterns, and attack methodologies, supporting security operations and defense planning.

**Operational Intelligence**: Actionable technical intelligence including indicators of compromise (IOCs), malware signatures, and detection rules, supporting immediate security operations and incident response.

**Indicator of Compromise (IOC)**: Observable artifact or forensic evidence indicating that a security breach has occurred or is occurring (IP addresses, domain names, file hashes, registry keys).

**Tactics, Techniques, and Procedures (TTPs)**: Patterns of activities and methods used by threat actors to conduct attacks, documented in frameworks like MITRE ATT&CK.

**MITRE ATT&CK**: Knowledge base of adversary tactics and techniques based on real-world observations, organized in a matrix structure for threat modeling and detection engineering.

**Admiralty Code**: Intelligence evaluation methodology rating source reliability (A-F) and information credibility (1-6) to assess intelligence confidence.

**Traffic Light Protocol (TLP)**: Information sharing standard using color codes (RED, AMBER, AMBER+STRICT, GREEN, CLEAR) to indicate sharing restrictions.

**STIX/TAXII**: Structured Threat Information Expression (STIX) and Trusted Automated Exchange of Intelligence Information (TAXII) are standards for sharing cyber threat intelligence in machine-readable formats.

**CVSS (Common Vulnerability Scoring System)**: Industry standard framework for assessing vulnerability severity, producing scores from 0.0 (informational) to 10.0 (critical). CVSS 4.0 is current standard (Nov 2023), CVSS 3.1 widely deployed in legacy systems.

**VulnerabilityThreatLink (VTL)**: Schema linking CVE identifiers with threat intelligence (exploitation status, threat actor attribution, CVSS scores) to enable intelligence-driven vulnerability prioritization. Optional integration point with Control A.8.8.

**Threat Actor**: Individual, group, or organization conducting malicious cyber activities (nation-states, organized crime, hacktivists, insiders).

**Campaign**: Coordinated series of attacks by a threat actor against specific targets over time, typically sharing TTPs, infrastructure, and objectives.

**Zero-Day Vulnerability**: Previously unknown vulnerability with no available patch, often exploited by advanced threat actors before public disclosure.

**Advanced Persistent Threat (APT)**: Sophisticated, well-resourced threat actor (typically nation-state sponsored) conducting prolonged, stealthy campaigns against specific targets.

**Threat Hunting**: Proactive search for threats that have evaded existing detection capabilities, informed by threat intelligence and hypothesis-driven investigation.

**False Positive**: Security alert or intelligence indicator incorrectly identifying benign activity as malicious, requiring validation and tuning.

**Threat Landscape**: Overall view of current and emerging threats relevant to an organization, sector, or region, including threat actors, attack vectors, and trending campaigns.

**Intelligence Requirement**: Specific question or information need that threat intelligence collection and analysis should address to support organizational decision-making.

**Intelligence Product**: Finished intelligence report, briefing, or analysis delivered to stakeholders (strategic assessment, tactical report, operational IOC feed).

**Dwell Time**: Time between initial compromise and threat detection/containment, reduced through effective threat intelligence and detection capabilities.

---

## 6. Evidence for This Policy

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
- Effectiveness dashboard (ISMS-IMP-A.5.7.4) showing consolidated metrics and KPIs

**Clarification on Compliance Evidence:**

This policy establishes threat intelligence governance framework (collection, analysis, production, and dissemination requirements). It does NOT establish:
- **Technical detection controls** (addressed in A.8.16 Monitoring Activities - threat intelligence provides context for detection rules)
- **Incident response procedures** (addressed in A.5.24-5.28 Incident Management - threat intelligence enhances investigation)
- **Vulnerability prioritization** (addressed in A.8.8 Vulnerability Management - VulnerabilityThreatLink integration is optional)
- **Specific threat actor profiles** (operational intelligence maintained in threat intelligence platform, not policy)
- **Tool selection or platform configuration** (implementation decisions based on organizational requirements)

The boundary is: POL-A.5.7 defines governance framework for threat intelligence capabilities → ISMS-IMP-A.5.7 suite provides assessment procedures → Threat intelligence platform implements technical collection/analysis → Other controls (A.8.16, A.5.24-28, A.8.8) consume threat intelligence outputs for their respective purposes.

---

## Annex A: Threat Intelligence Source Evaluation Framework

**Scope**: This annex provides decision criteria for evaluating and selecting threat intelligence sources using Admiralty Code methodology.

### A.1 Source Reliability Assessment

**Reliability Ratings** (Source Assessment):

| Rating | Description | Accuracy | Selection Criteria | Examples |
|--------|-------------|----------|-------------------|----------|
| **A** | Completely reliable | ≥95% | Established track record, vetted processes, high-quality validation | Government CERTs, premium commercial platforms (Recorded Future, Mandiant) |
| **B** | Usually reliable | 90-95% | Good track record, documented methodology, occasional errors | Mid-tier commercial platforms, established ISACs |
| **C** | Fairly reliable | 85-90% | Moderate track record, basic validation, regular updates | Open-source aggregators (AlienVault OTX), security researcher blogs |
| **D** | Not usually reliable | 80-85% | Limited track record, minimal validation, frequent gaps | Newly established feeds, unvetted community sources |
| **E** | Unreliable | <80% | Poor track record, no validation, high false positive rate | Unmoderated forums, untrusted threat feeds |
| **F** | Cannot be judged | Unknown | Insufficient data, new source, no validation history | Newly discovered sources, zero-day disclosures |

### A.2 Information Credibility Assessment

**Credibility Ratings** (Information Assessment):

| Rating | Description | Validation | Usage Guidance |
|--------|-------------|------------|----------------|
| **1** | Confirmed by other sources | Multiple independent confirmations | Use immediately for detection and response |
| **2** | Probably true | Logical consistency, single confirmation | Deploy to security tools with monitoring |
| **3** | Possibly true | Plausible but unconfirmed | Use for awareness, require corroboration before action |
| **4** | Doubtful | Questionable consistency or logic | Use only for hypothesis generation |
| **5** | Improbable | Contradicts known facts or other intelligence | Do not operationalize, investigate discrepancy |
| **6** | Cannot be judged | Insufficient information to assess | Hold pending additional information |

### A.3 Combined Intelligence Grades

**Operational Decision Matrix**:

| Grade Combination | Confidence Level | Operational Use | Example |
|-------------------|------------------|-----------------|---------|
| **A1, B1, A2** | High Confidence | Immediate operationalization, deploy to all security tools | Government advisory with IOCs confirmed by commercial platform |
| **B2, C1, C2** | Medium Confidence | Operationalize with enhanced monitoring, validate effectiveness | ISAC intelligence corroborated by community sources |
| **C3, D2, B3** | Low Confidence | Use for awareness only, corroborate before operationalization | Single-source OSINT intelligence without validation |
| **D3, D4, E5** | Minimal Confidence | Hypothesis generation only, do not operationalize | Uncorroborated forum posts, speculation |
| **F6** | No Confidence | Information only, no operational use | Rumor, unverified disclosure |

### A.4 Source Selection Criteria

**Mandatory Selection Criteria**:

[Organization] selects threat intelligence sources based on:

**Coverage Requirements**:
- **Threat Actor Coverage**: Sources cover relevant threat actors (nation-states, cybercrime, hacktivists)
- **Geographic Coverage**: Intelligence relevant to [Organization]'s operating regions
- **Technology Coverage**: Sources address [Organization]'s technology stack and infrastructure
- **Vulnerability Coverage**: CVSS 4.0/3.1 support for vulnerability intelligence
- **TTP Coverage**: Sources provide adversary behavior intelligence (MITRE ATT&CK mapping)

**Quality Requirements**:
- **Accuracy Target**: ≥85% source accuracy (validated quarterly)
- **Validation Methodology**: Source documents intelligence collection and validation processes
- **Timeliness**: Intelligence delivered within operational timeframes
- **Format**: Machine-readable formats supported (STIX, JSON, CSV) for automation
- **API Access**: Programmatic access for integration with security tools

**Compliance Requirements**:
- **Data Protection**: Source complies with GDPR, Swiss nDSG for personal data handling
- **Contractual**: Data Processing Agreement (DPA) in place for commercial sources
- **Sharing Rights**: Intelligence sharing permissions clearly documented (TLP classifications)
- **Export Controls**: Source complies with applicable export control regulations

**Operational Requirements**:
- **Support**: Adequate customer support, documentation, training materials
- **Reliability**: Platform uptime ≥99.5% for critical operational feeds
- **Scalability**: Source supports [Organization]'s intelligence volume requirements
- **Integration**: Compatible with [Organization]'s threat intelligence platform and tools

### A.5 Source Performance Monitoring

**Quarterly Performance Validation**:

[Organization] validates source performance quarterly through:

**Accuracy Validation**:
- Sample prevented incidents (n≥10 per quarter)
- Verify threat intelligence correctly predicted or detected threat
- Calculate accuracy rate: (Correct predictions / Total predictions) × 100%
- Target: ≥85% accuracy across all sources
- Remediation: Sources below 80% require immediate review, below 70% consider discontinuation

**Timeliness Assessment**:
- Measure time from threat emergence to intelligence delivery
- Compare source timeliness against peer sources and industry benchmarks
- Target: Critical threats reported within 24 hours of public disclosure

**Coverage Assessment**:
- Verify source addresses [Organization]'s intelligence requirements
- Identify coverage gaps requiring additional sources
- Assess source specialization (e.g., ransomware, cloud threats, APTs)

**False Positive Analysis**:
- Track false positive IOCs causing operational disruption
- Calculate false positive rate per source
- Work with vendors to improve IOC quality and validation

**Documentation**: Source performance tracked in ISMS-IMP-A.5.7.1 Sheet 14 (Source Performance Validation).

---

## Annex B: Quick Reference Guide for Stakeholders

**Purpose**: One-page summary of threat intelligence program for organizational users.

### What is Threat Intelligence?

Threat intelligence is the collection, analysis, and dissemination of information about current or emerging security threats enabling [Organization] to:
- Detect threats before they become incidents
- Respond faster to security events
- Make informed security investment decisions
- Prioritize vulnerability remediation based on real-world risk

### What Threat Intelligence Covers

✓ **Threat Actors**: Who is targeting organizations like ours (nation-states, cybercrime, hacktivists)  
✓ **Attack Methods**: How attackers conduct campaigns (ransomware, phishing, exploits)  
✓ **Indicators**: Technical evidence of threats (malicious IPs, domains, file hashes)  
✓ **Vulnerabilities**: Which vulnerabilities are actively exploited in the wild  
✓ **Campaigns**: Ongoing attack campaigns targeting our sector or technologies  

### Intelligence Types

**Strategic Intelligence** (Executive Audience):
- Threat landscape trends and risk assessments
- Adversary capability analyses
- Security investment recommendations
- **Frequency**: Quarterly + significant events

**Tactical Intelligence** (Security Teams):
- Threat actor profiles and TTPs
- Campaign analysis and attack patterns
- Detection and hunting guidance
- **Frequency**: Monthly + emerging threats

**Operational Intelligence** (Technical Teams):
- Indicators of Compromise (IOCs) for detection
- Malware signatures and behaviors
- Blocking recommendations
- **Frequency**: Continuous automated feeds

### How Threat Intelligence Helps You

**For Executives**:
- Informed risk decisions based on current threat landscape
- Justified security investments aligned with real threats
- Board-ready threat briefings and risk assessments

**For Security Operations**:
- Faster incident detection with threat context
- Reduced investigation time through intelligence enrichment
- Proactive threat hunting based on adversary TTPs

**For IT Operations**:
- Prioritized patching based on active exploitation
- Blocking lists for malicious infrastructure
- Early warning of infrastructure-targeting threats

**For Risk Management**:
- Current threat data for risk assessment (Clause 6.1)
- Likelihood estimates informed by threat intelligence
- Risk treatment prioritization based on threat landscape

### Key Metrics

- **≥3** risk assessment updates per quarter driven by threat intelligence
- **≥3** prevented incidents per quarter with validation evidence
- **≥85%** source accuracy rate (validated quarterly)
- **≥70%** of P1/P2 incidents enriched with threat intelligence context
- **≥5** security decisions per quarter informed by threat intelligence

### Contact Information

**Threat Intelligence Team**: threatintel@[organization].example  
**Emergency Threat Escalation**: SOC hotline (24/7)  
**CISO Office**: ciso@[organization].example  

**For intelligence requests, feedback, or questions, contact the Threat Intelligence Team.**

---

## Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **Chief Risk Officer (CRO)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements. Implementation procedures are documented in ISMS-IMP-A.5.7.*