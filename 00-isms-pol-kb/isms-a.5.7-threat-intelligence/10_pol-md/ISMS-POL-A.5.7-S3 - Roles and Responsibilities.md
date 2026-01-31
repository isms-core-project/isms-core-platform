# ISMS-POL-A.5.7-S3
## Threat Intelligence - Roles and Responsibilities

**Document ID**: ISMS-POL-A.5.7-S3  
**Title**: Threat Intelligence - Roles and Responsibilities  
**Version**: 1.0
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]| [Author Name] | Initial draft |

**Review Cycle**: Annual (mandatory in Q4), quarterly light review (metrics only), or upon significant changes  
**Review Month**: Q4 (October-November) to align with budget planning and annual ISMS reviews  
**Next Review Date**: [Date + 1 year]  
**Approvers**: 
- Chief Information Security Officer (CISO)
- Chief Information Officer (CIO)
- Chief Risk Officer (CRO)
- Legal/Compliance Officer
- Chief Executive Officer (CEO)

---

## 3.1 Overview

### 3.1.1 Purpose

This document defines the roles, responsibilities, and accountabilities for threat intelligence activities within the organization. Clear definition of responsibilities ensures:

- Effective collection, analysis, and dissemination of threat intelligence
- Accountability for threat intelligence program outcomes
- Appropriate allocation of resources and authority
- Integration of threat intelligence across security and risk management functions
- Compliance with organizational policies and regulatory requirements
- **Generation of audit evidence** per ISMS-POL-A.5.7 Section 4.4
- **Business continuity** through backup personnel and cross-training per ISMS-POL-A.5.7 Section 4.4.6

### 3.1.2 Responsibility Assignment Principles

Roles and responsibilities are assigned based on the following principles:

**Separation of Duties**: Critical functions are distributed to prevent conflicts of interest and single points of failure.

**Clear Accountability**: Each function has a clearly identified owner accountable for outcomes.

**Business Continuity**: Each critical role SHALL have documented backup personnel with appropriate cross-training (per ISMS-POL-A.5.7 Section 4.4.6).

**Scalability**: Role definitions are flexible to accommodate organizational size and structure. Smaller organizations may combine multiple roles; larger organizations may distribute across multiple teams.

**Integration**: Threat intelligence roles integrate with and support existing security operations, incident response, risk management, and IT operations functions.

**Competency-Based**: Roles require specific knowledge, skills, and experience appropriate to the function.

**Evidence Generation**: Roles responsible for threat intelligence activities SHALL generate audit evidence per ISMS-POL-A.5.7 Section 4.4.

### 3.1.3 RACI Framework

This document uses a simplified RACI model where applicable:
- **Responsible (R)**: Performs the work
- **Accountable (A)**: Ultimately answerable for outcomes; approves work
- **Consulted (C)**: Provides input and expertise
- **Informed (I)**: Kept informed of progress and decisions

---

## 3.2 Executive and Governance Roles

### 3.2.1 Chief Information Security Officer (CISO)

**Role**: Policy Owner and Executive Sponsor for Threat Intelligence Program

**Accountabilities**:
- Overall accountability for threat intelligence program effectiveness
- Approval of threat intelligence policies, procedures, and standards
- Strategic direction and priority setting for threat intelligence activities
- Resource allocation (budget, personnel, tools) for threat intelligence
- Escalation point for critical threat intelligence and executive decision-making
- Representation of threat intelligence in executive risk discussions
- Approval of external threat intelligence sharing arrangements
- **Audit readiness** for Control A.5.7 certification

**Responsibilities**:
- Review and approve strategic threat intelligence reports and recommendations
- **Ensure threat intelligence is integrated into organizational risk management (Clause 6.1 - MANDATORY)**
- Champion threat intelligence program value to executive leadership and board
- Approve exceptions to threat intelligence policies
- Ensure adequate competency and training for threat intelligence personnel
- Monitor threat intelligence program metrics and effectiveness
- **Quarterly review of KPIs** against targets (per ISMS-POL-A.5.7 Section 4.6)
- **Review audit evidence package** 30 days before certification audit (per ISMS-POL-A.5.7 Section 4.5)
- **Ensure business continuity** through backup personnel and cross-training

**Authority**:
- Final decision authority on threat intelligence program scope and priorities
- Approval authority for threat intelligence technology investments
- Authority to mandate integration of threat intelligence across security functions
- Authority to establish or modify information sharing agreements

**Interfaces**:
- Reports to: Chief Executive Officer (CEO) or equivalent
- Collaborates with: CIO, CTO, Chief Risk Officer (CRO), Legal/Compliance, Business Unit Leaders
- Receives intelligence from: Threat Intelligence Coordinator, SOC Manager

**Business Continuity**:
- **Backup**: Deputy CISO or Senior Security Manager
- **Cross-training**: Documented in ISMS-IMP-A.5.7.1 Sheet 15

### 3.2.2 Executive Leadership and Board

**Role**: Strategic Oversight and Risk Governance

**Accountabilities**:
- Understanding organizational threat landscape at strategic level
- Oversight of threat-informed risk management decisions
- Approval of risk appetite and tolerance in context of threat environment

**Responsibilities**:
- Review strategic threat intelligence reports (quarterly or semi-annually)
- Consider threat intelligence in strategic planning and business decisions
- Ensure adequate resources for threat intelligence and cybersecurity programs
- Oversee organizational response to major threat landscape changes

**Authority**:
- Approval of strategic security investments based on threat intelligence
- Setting of organizational risk appetite considering threat environment

**Interfaces**:
- Receives reports from: CISO
- Collaborates with: Executive management team

---

## 3.3 Threat Intelligence Core Functions

### 3.3.1 Threat Intelligence Coordinator / Manager

**Role**: Day-to-Day Leadership and Coordination of Threat Intelligence Activities

**Note**: In smaller organizations, this role may be performed by the CISO, Security Manager, or SOC Manager. In larger organizations, this may be a dedicated role or team.

**Accountabilities**:
- Execution of threat intelligence program in accordance with policy requirements
- Quality and relevance of threat intelligence products
- Coordination across intelligence collection, analysis, and dissemination functions
- Management of threat intelligence tools and platforms
- Development and maintenance of threat intelligence procedures
- **Generation of audit evidence** per ISMS-POL-A.5.7 Section 4.4

**Responsibilities**:

*Program Management*:
- Develop and maintain threat intelligence procedures and playbooks
- Define and refine intelligence requirements based on organizational needs
- Manage threat intelligence technology platforms and tools
- Establish and maintain relationships with external intelligence sources
- Track and report on threat intelligence program metrics
- Conduct regular program effectiveness reviews
- **Generate quarterly assessment workbooks** (ISMS-IMP-A.5.7.1 through A.5.7.4)
- **Prepare audit evidence package** per ISMS-POL-A.5.7 Section 4.5

*Intelligence Operations*:
- Oversee collection from internal and external threat intelligence sources
- Coordinate analysis activities and prioritization
- Review and approve intelligence products before dissemination
- Ensure timely delivery of intelligence to stakeholders
- Manage indicator feeds and integrations with security tools

*Quality Assurance*:
- Validate intelligence accuracy and relevance
- Implement quality control processes for intelligence products
- **Conduct quarterly source reliability assessments** (Admiralty Code)
- **Track source accuracy rate** (target: ≥85%) per ISMS-POL-A.5.7 Section 4.4.3
- Address consumer feedback and intelligence gaps

*Evidence Tracking*:
- **Document risk assessment updates** (Clause 6.1) in ISMS-IMP-A.5.7.3 Sheet 13
- **Track prevented incidents** with validation evidence in ISMS-IMP-A.5.7.3 Sheet 7
- **Document intelligence-driven decisions** in ISMS-IMP-A.5.7.3 Sheet 15
- **Validate compliance** with sanity check scripts before audit

*Collaboration*:
- Coordinate with SOC, incident response, risk management teams
- **Collaborate with Chief Risk Officer (CRO)** on Clause 6.1 risk assessment updates (MANDATORY)
- **Coordinate with Vulnerability Management** when Control A.8.8 implemented (OPTIONAL)
- Facilitate threat briefings and intelligence sharing sessions
- Represent organization in external threat intelligence sharing forums (ISACs, ISAOs)
- Liaise with vendors and external intelligence providers

**Authority**:
- Selection and prioritization of threat intelligence sources within approved budget
- Approval of operational and tactical intelligence products for dissemination
- Authority to request support from other teams for intelligence analysis
- Recommendation authority for strategic intelligence findings

**Required Competencies**:
- Understanding of threat actor TTPs and cyber threat landscape
- Analytical and critical thinking skills
- Knowledge of threat intelligence frameworks (MITRE ATT&CK, Cyber Kill Chain, Diamond Model)
- Familiarity with threat intelligence platforms and tools
- Strong written and verbal communication skills
- Project management capabilities
- **Understanding of audit evidence requirements** (ISO 27001:2022 Control A.5.7)
- **Proficiency with assessment workbooks** and evidence documentation

**Interfaces**:
- Reports to: CISO or Security Manager
- Manages: Threat Intelligence Analysts (where applicable)
- Collaborates with: SOC, Incident Response, Risk Management (CRO), Vulnerability Management (when A.8.8 implemented), IT Operations
- Interfaces with: External intelligence providers, ISACs/ISAOs, peer organizations

**Business Continuity**:
- **Primary**: Threat Intelligence Coordinator
- **Backup**: Senior Threat Intelligence Analyst or SOC Manager
- **Cross-training**: Documented and tested annually
- **Critical sources access**: Documented in ISMS-IMP-A.5.7.1 Sheet 15
- **Minimal operations playbook**: Daily checks, alert triage, stakeholder notification
- **Evidence tracked in**: ISMS-IMP-A.5.7.1 Sheet 15 (Continuity Plan)

### 3.3.2 Threat Intelligence Analyst(s)

**Role**: Collection, Analysis, and Production of Threat Intelligence

**Note**: In smaller organizations, analysis may be performed by SOC analysts, security engineers, or the Threat Intelligence Coordinator. In larger organizations, dedicated analysts or an analysis team may exist.

**Accountabilities**:
- Quality and accuracy of threat intelligence analysis
- Timely production of intelligence products
- Actionability of intelligence recommendations

**Responsibilities**:

*Collection*:
- Monitor internal security telemetry for threat indicators
- Aggregate intelligence from external sources (feeds, reports, OSINT)
- Validate and enrich raw threat data
- Manage indicator lifecycle (collection, validation, aging, expiration)

*Analysis*:
- Analyze threat actor TTPs and map to frameworks (MITRE ATT&CK)
- Conduct campaign analysis and threat actor profiling
- Correlate indicators across multiple sources
- Assess threat relevance to organizational environment
- Produce strategic, tactical, and operational intelligence
- Assign confidence levels to intelligence assessments

*Production*:
- Author threat intelligence reports and briefings
- Create IOC feeds for security tool integration
- Develop threat hunting hypotheses
- Document emerging threats and attack techniques
- Maintain threat actor and campaign knowledge base

*Integration*:
- Coordinate with SOC for alert triage and enrichment
- **Support incident response** with threat context and attribution (track in ISMS-IMP-A.5.7.3 Sheet 14)
- **Inform vulnerability management** of active exploitation (when Control A.8.8 implemented)
- **Create VulnerabilityThreatLink (VTL) records** for active exploitation (OPTIONAL - when A.8.8 operational)
- Contribute to security awareness training content

*Evidence Generation*:
- **Document prevented incidents** with before/after states and validation evidence
- **Validate intelligence accuracy** through post-event analysis
- **Track intelligence-driven decisions** and outcomes

**Authority**:
- Recommendation authority for intelligence findings
- Authority to request additional information from security teams
- Authority to flag critical threats for immediate escalation

**Required Competencies**:
- Strong analytical and research skills
- Understanding of malware analysis and reverse engineering (beneficial)
- Knowledge of networking, operating systems, and attack techniques
- Proficiency with threat intelligence tools and platforms
- Familiarity with intelligence frameworks and methodologies
- Written communication and reporting skills
- Critical thinking and hypothesis generation
- **Understanding of evidence documentation requirements**

**Interfaces**:
- Reports to: Threat Intelligence Coordinator or SOC Manager
- Collaborates with: SOC Analysts, Incident Responders, Threat Hunters, Risk Management, Vulnerability Management (when A.8.8 implemented)
- Interfaces with: External researchers, intelligence communities

**Business Continuity**:
- **Backup**: Cross-trained with other analysts or SOC personnel
- **Cross-training frequency**: Quarterly

---

## 3.4 Security Operations Roles

### 3.4.1 Security Operations Center (SOC) Team

**Role**: Operationalization and Consumption of Threat Intelligence for Detection and Response

**Accountabilities**:
- Integration of threat intelligence into monitoring and detection (Control A.8.16 - MANDATORY)
- Timely response to intelligence-driven alerts
- Feedback to threat intelligence team on intelligence utility

**Responsibilities**:

*Intelligence Consumption*:
- Deploy IOCs to SIEM, EDR, and other security tools
- Configure detection rules based on tactical intelligence
- Enrich security alerts with threat intelligence context
- Utilize threat actor TTPs for threat hunting

*Alert Triage and Response*:
- Prioritize alerts using threat intelligence severity and context
- Correlate security events with known campaigns and threat actors
- Escalate intelligence-driven detections to incident response
- Document false positives for intelligence feedback
- **Track prevented incidents** (blocked attacks, quarantined malware)

*Feedback and Collaboration*:
- Provide feedback on IOC accuracy and false positive rates
- Request additional context or intelligence for investigations
- Share internal threat observations with threat intelligence team
- Participate in threat briefings and intelligence sharing sessions
- **Complete stakeholder satisfaction surveys** (target: ≥4.0/5.0)

**Authority**:
- Authority to block or quarantine based on high-confidence threat intelligence
- Escalation authority for critical intelligence-driven detections

**Interfaces**:
- Reports to: SOC Manager
- Collaborates with: Threat Intelligence Team, Incident Response, Network Operations
- Receives intelligence from: Threat Intelligence Coordinator/Analysts

**Business Continuity**:
- **Shift-based operations** ensure 24/7 coverage
- **Cross-training**: All SOC analysts trained on TI tool integration

### 3.4.2 Incident Response Team

**Role**: Utilization of Threat Intelligence for Incident Investigation and Response

**Accountabilities**:
- Effective use of threat intelligence during incident response (Controls A.5.24-5.28 - MANDATORY)
- Contribution of incident-derived intelligence back to threat intelligence program
- **Documentation of TI use in incidents** per ISMS-POL-A.5.7 Section 4.4.4

**Responsibilities**:

*Incident Investigation*:
- Leverage threat intelligence for incident scoping and impact assessment
- Use IOCs for compromise assessment and lateral movement tracking
- Apply threat actor TTP knowledge for forensic analysis
- Utilize intelligence for attribution and campaign association
- **Document threat intelligence usage** in incident reports

*Response Actions*:
- Inform containment and eradication based on threat intelligence
- Prioritize remediation using threat context
- Coordinate with threat intelligence team for emerging threat response

*Intelligence Contribution*:
- Extract IOCs and TTPs from incidents for intelligence enrichment
- Document lessons learned and defensive gaps
- Share incident findings (sanitized) with external intelligence communities
- Participate in post-incident reviews with threat intelligence team
- **Rate TI effectiveness** per incident (tracked in ISMS-IMP-A.5.7.3 Sheet 14)

*Evidence Generation*:
- **Document prevented incidents** where TI enabled proactive response
- **Track investigation time savings** due to threat intelligence context

**Authority**:
- Authority to request priority threat intelligence support during active incidents
- Recommendation authority for intelligence-driven response actions

**Interfaces**:
- Reports to: Incident Response Manager or CISO
- Collaborates with: Threat Intelligence Team, SOC, Forensics, Legal
- Receives intelligence from: Threat Intelligence Coordinator/Analysts

**Target**: ≥70% of P1/P2 incidents use threat intelligence (per ISMS-POL-A.5.7 Section 4.6)

---

## 3.5 Risk and Vulnerability Management Roles

### 3.5.1 Risk Management Team / Chief Risk Officer (CRO)

**Role**: Integration of Threat Intelligence into Risk Assessment and Treatment

**Accountabilities**:
- **Incorporation of threat intelligence into organizational risk assessments (Clause 6.1 - MANDATORY)**
- Threat-informed risk treatment decisions
- **Documentation of TI-driven risk updates** per ISMS-POL-A.5.7 Section 4.4.1

**Responsibilities**:

*Risk Assessment (Clause 6.1 - MANDATORY)*:
- **Review quarterly strategic threat intelligence** for risk implications
- **Update threat likelihood and impact assessments** based on intelligence
- **Incorporate emerging threats into risk register** (document TI Report → Risk Register cross-reference)
- Prioritize risk treatment using threat intelligence
- **Approve risk assessment updates** driven by threat intelligence
- **Target**: ≥3 risk assessment updates per quarter driven by TI

*Risk Communication*:
- Communicate threat-informed risk posture to executive leadership
- Provide risk context for threat intelligence findings
- Recommend risk treatment options based on threat landscape

*Collaboration*:
- **Mandatory collaboration** with Threat Intelligence Coordinator on Clause 6.1 updates
- Participate in strategic threat intelligence briefings
- Request specific threat intelligence to support risk assessments
- Provide feedback on threat intelligence relevance to risk decisions

*Evidence Generation*:
- **Document cross-reference**: TI Report ID → Risk Register Entry ID
- **Maintain approval records**: CRO approval of TI-driven risk updates
- **Tracked in**: ISMS-IMP-A.5.7.3 Sheet 13 (Risk Assessment Updates)

**Authority**:
- Authority to request threat intelligence to support risk assessments
- **Approval authority** for risk treatment based on threat intelligence
- **Approval authority** for risk likelihood/impact changes driven by TI

**Interfaces**:
- Reports to: Chief Executive Officer or Board Risk Committee
- Collaborates with: **Threat Intelligence Team (MANDATORY)**, CISO, Business Units
- Receives intelligence from: Threat Intelligence Coordinator

**Business Continuity**:
- **Backup**: Risk Manager or CISO
- **Cross-training**: Annual review of TI-risk integration process

### 3.5.2 Vulnerability Management Team

**Role**: Threat-Informed Vulnerability Prioritization and Remediation

**Note**: This role implements Control A.8.8 when present. Integration with threat intelligence is **OPTIONAL** and only applies when organization has implemented Control A.8.8.

**Accountabilities** (when Control A.8.8 implemented):
- Prioritization of vulnerability remediation based on threat intelligence
- Timely patching of actively exploited vulnerabilities

**Responsibilities** (when Control A.8.8 implemented):

*Intelligence-Driven Prioritization*:
- Integrate threat intelligence into vulnerability risk scoring
- Prioritize patching based on active exploitation intelligence
- Escalate emergency patching for zero-day exploitation
- Track exploitation trends for proactive remediation
- **Process VulnerabilityThreatLink (VTL) records** from threat intelligence

*Collaboration*:
- Coordinate with threat intelligence team on vulnerability exploitation tracking
- Provide vulnerability data to threat intelligence for coverage assessment
- Request intelligence on specific vulnerabilities affecting the organization
- Share patching status for threat exposure assessment
- **Update VTL remediation status** (syncs back to ISMS-IMP-A.5.7.2 Sheet 8)

*Feedback*:
- Report on remediation effectiveness based on threat reduction
- Identify gaps in intelligence coverage for organizational vulnerabilities

**Authority**:
- Authority to prioritize patching based on threat intelligence
- Escalation authority for emergency patching of exploited vulnerabilities

**Interfaces**:
- Reports to: IT Security Manager or CISO
- Collaborates with: Threat Intelligence Team (when A.8.8 implemented), IT Operations, Change Management
- Receives intelligence from: Threat Intelligence Coordinator/Analysts

**Integration Status**:
- **Without Control A.8.8**: Basic threat intelligence consumption (CISA KEV, vendor advisories)
- **With Control A.8.8**: Full VTL schema integration with automated data flow

---

## 3.6 IT Operations and Infrastructure Roles

### 3.6.1 IT Operations / Infrastructure Teams

**Role**: Implementation of Threat Intelligence-Driven Security Controls

**Accountabilities**:
- Deployment of threat intelligence-driven security configurations
- Support for threat intelligence collection from infrastructure

**Responsibilities**:

*Control Implementation*:
- Deploy network security rules based on threat intelligence IOCs
- Configure DNS sinkholing for malicious domains
- Implement firewall and IDS/IPS signatures from intelligence feeds
- Apply threat intelligence to network segmentation decisions

*Telemetry and Logging*:
- Ensure security telemetry is available for threat intelligence collection
- Maintain log quality and retention for intelligence analysis
- Provide infrastructure data for threat hunting and investigations

*Patching and Configuration*:
- Execute emergency patching for actively exploited vulnerabilities
- Implement configuration changes based on threat intelligence recommendations
- Coordinate with vulnerability management on remediation priorities

**Authority**:
- Implementation authority for approved security control changes
- Escalation authority for infrastructure impacts of threat-driven actions

**Interfaces**:
- Reports to: IT Manager or CIO
- Collaborates with: Threat Intelligence Team, SOC, Vulnerability Management, Change Management
- Receives intelligence from: Threat Intelligence Coordinator, SOC

### 3.6.2 Application Development / DevOps Teams

**Role**: Integration of Threat Intelligence into Secure Development and Deployment

**Accountabilities**:
- Secure coding practices informed by threat intelligence
- Remediation of vulnerabilities in developed applications

**Responsibilities**:

*Secure Development*:
- Incorporate threat intelligence on common attack techniques into secure coding
- Review threat intelligence on framework and library vulnerabilities
- Participate in threat modeling using current attack patterns
- Implement security controls based on tactical intelligence

*Vulnerability Response*:
- Prioritize remediation of application vulnerabilities based on exploitation intelligence
- Apply security patches to application dependencies
- Conduct security testing informed by adversary TTPs

*Collaboration*:
- Consult with threat intelligence team on application-specific threats
- Share security findings from application assessments
- Participate in threat briefings relevant to development technologies

**Authority**:
- Authority to request threat intelligence for specific technologies or frameworks
- Recommendation authority for security enhancements based on threat landscape

**Interfaces**:
- Reports to: Development Manager or CTO
- Collaborates with: Threat Intelligence Team, Application Security, Vulnerability Management
- Receives intelligence from: Threat Intelligence Coordinator

---

## 3.7 Support and Enabling Roles

### 3.7.1 Legal and Compliance Team

**Role**: Legal and Regulatory Compliance for Threat Intelligence Activities

**Accountabilities**:
- Legal compliance of threat intelligence collection and sharing
- Protection of organizational legal interests in intelligence activities

**Responsibilities**:

*Compliance Review*:
- Review threat intelligence collection methods for legal compliance
- Assess data protection and privacy implications of threat intelligence
- Review information sharing agreements and NDAs
- Ensure export control compliance for shared intelligence

*Policy and Process*:
- Provide legal guidance on threat intelligence policies and procedures
- Review external intelligence sharing for legal risks
- Advise on lawful monitoring and surveillance boundaries
- Support incident response with legal counsel on threat intelligence use

*Contracts and Agreements*:
- Review contracts with threat intelligence vendors
- Draft or review information sharing agreements
- Ensure contractual protection for shared intelligence

**Authority**:
- Veto authority over intelligence activities with legal or compliance risks
- Approval authority for external information sharing agreements

**Interfaces**:
- Reports to: General Counsel or Chief Legal Officer
- Collaborates with: CISO, Threat Intelligence Coordinator, Privacy Officer
- Consulted by: Threat Intelligence Team, Incident Response

### 3.7.2 Human Resources

**Role**: Personnel Management and Awareness for Threat Intelligence

**Accountabilities**:
- Hiring and competency development for threat intelligence roles
- Employee awareness of threat intelligence program

**Responsibilities**:

*Staffing*:
- Recruit and onboard threat intelligence personnel
- Support competency development and training
- Manage access provisioning for threat intelligence tools and data
- **Ensure business continuity** through backup personnel assignments

*Awareness*:
- Coordinate security awareness training incorporating threat intelligence
- Communicate threat landscape to employees (phishing, social engineering, etc.)
- Support insider threat awareness programs

**Interfaces**:
- Reports to: Chief Human Resources Officer
- Collaborates with: CISO, Threat Intelligence Coordinator
- Supports: Security Awareness Program

### 3.7.3 Training and Awareness Coordinator

**Role**: Integration of Threat Intelligence into Security Awareness

**Accountabilities**:
- Effective communication of relevant threats to employees
- Security awareness training informed by current threat landscape

**Responsibilities**:

*Awareness Content*:
- Incorporate current phishing and social engineering techniques from threat intelligence
- Develop awareness campaigns based on active threat campaigns
- Use real-world threat examples from intelligence in training

*Collaboration*:
- Coordinate with threat intelligence team for awareness-relevant intelligence
- Request specific intelligence on user-targeted threats (phishing, BEC, etc.)
- Share metrics on user reporting and awareness effectiveness

**Interfaces**:
- Reports to: CISO or HR
- Collaborates with: Threat Intelligence Team, SOC
- Receives intelligence from: Threat Intelligence Coordinator

---

## 3.8 External Party Roles

### 3.8.1 Managed Security Service Providers (MSSPs)

**Role**: Third-Party Security Operations and Intelligence Support

**Note**: Where the organization engages MSSPs for SOC, threat intelligence, or related services.

**Accountabilities** (as defined in service agreements):
- Delivery of threat intelligence services per contract
- Quality and timeliness of intelligence products
- Integration with organizational security operations

**Responsibilities**:
- Provide agreed-upon threat intelligence feeds and reports
- Operate threat intelligence platforms on behalf of the organization
- Conduct threat hunting and analysis as contracted
- Escalate critical threats to organizational stakeholders

**Authority**:
- Authority as defined in service level agreements and contracts
- Limited to contracted scope of services

**Governance**:
- Service delivery monitored by Threat Intelligence Coordinator or CISO
- Performance measured against SLAs
- Regular service review meetings

**Interfaces**:
- Contracted by: CISO or Procurement
- Collaborates with: Threat Intelligence Coordinator, SOC, Incident Response
- Monitored by: Threat Intelligence Coordinator, Contract Manager

### 3.8.2 Threat Intelligence Vendors and Providers

**Role**: Commercial Threat Intelligence Products and Services

**Accountabilities**:
- Quality, accuracy, and timeliness of threat intelligence products
- Support and service delivery per contractual terms

**Responsibilities**:
- Deliver threat intelligence feeds, reports, and analysis per contract
- Provide technical support for intelligence platforms and integrations
- Maintain intelligence quality and coverage
- Respond to customer requests for specific intelligence

**Authority**:
- Authority as defined in vendor agreements
- Limited to contracted products and services

**Governance**:
- Vendor performance monitored by Threat Intelligence Coordinator
- **Quarterly reviews** of intelligence quality and value (source accuracy tracking)
- Renewal decisions based on effectiveness metrics
- **Sources <80% accuracy** subject to replacement

**Interfaces**:
- Contracted by: CISO or Procurement
- Managed by: Threat Intelligence Coordinator
- Used by: Threat Intelligence Analysts, SOC

### 3.8.3 Information Sharing Communities (ISACs, ISAOs, Peer Groups)

**Role**: Collaborative Threat Intelligence Sharing

**Accountabilities**:
- Reciprocal value through information sharing
- Adherence to community sharing guidelines and TLP (Traffic Light Protocol)

**Responsibilities**:
- Share sanitized threat intelligence with peer organizations
- Consume intelligence from community members
- Participate in community briefings and threat discussions
- Maintain trust and confidentiality within sharing community

**Authority**:
- Sharing authority as defined in community membership agreements
- Subject to organizational information sharing policy

**Governance**:
- Participation approved and monitored by CISO
- Sharing activities managed by Threat Intelligence Coordinator
- Compliance with TLP and community rules enforced

**Interfaces**:
- Membership managed by: CISO or Threat Intelligence Coordinator
- Represented by: Threat Intelligence Coordinator, Analysts
- Reported to: CISO (significant intelligence findings)

---

## 3.9 Role Mapping Matrix

### 3.9.1 Threat Intelligence Activity RACI

| Activity | CISO | TI Coord | TI Analyst | SOC | IR | CRO/Risk | Vuln Mgmt† | IT Ops | Legal |
|----------|------|----------|------------|-----|----|-----------|-----------| -------|-------|
| Strategic Intelligence Production | A | R | C | I | I | C | I | I | I |
| Tactical Intelligence Production | A | A | R | C | C | I | C | I | I |
| Operational Intelligence Production | I | A | R | C | C | I | I | I | I |
| IOC Feed Management | I | A | R | R | C | I | I | I | I |
| Intelligence Dissemination | I | R | R | I | I | I | I | I | I |
| External Intelligence Sharing | A | R | C | C | C | C | I | I | C |
| Source Evaluation & Selection | A | R | C | C | I | I | I | I | C |
| **Clause 6.1 Risk Assessment Integration** | **A** | **C** | **C** | **I** | **I** | **R** | **I** | **I** | **C** |
| Threat Hunting | I | C | C | R | C | I | I | I | I |
| **Incident Intelligence Usage (A.5.24-5.28)** | **I** | **C** | **C** | **C** | **R** | **I** | **I** | **I** | **I** |
| Vulnerability Prioritization (A.8.8)† | I | C | C | I | I | I | R | C | I |
| **VTL Record Creation (A.8.8)†** | **I** | **C** | **R** | **I** | **I** | **I** | **C** | **I** | **I** |
| Security Tool Integration | I | R | R | A | I | I | C | C | I |
| Intelligence Quality Assurance | A | R | C | C | I | I | I | I | I |
| **Evidence Generation (Section 4.4)** | **A** | **R** | **R** | **C** | **C** | **C** | **I** | **I** | **I** |
| **Source Accuracy Validation (Section 4.4.3)** | **A** | **R** | **C** | **C** | **I** | **I** | **I** | **I** | **I** |
| **Audit Preparation (Section 4.5)** | **A** | **R** | **C** | **I** | **I** | **C** | **I** | **I** | **C** |
| **Business Continuity (Section 4.4.6)** | **A** | **R** | **C** | **I** | **I** | **I** | **I** | **I** | **I** |

**Legend**:
- **A** = Accountable (final authority, approver)
- **R** = Responsible (does the work)
- **C** = Consulted (provides input)
- **I** = Informed (kept updated)
- **†** = OPTIONAL - only applies when Control A.8.8 implemented

**Bold entries** = Added in v1.1 for audit evidence requirements

---

## 3.10 Business Continuity Requirements

### 3.10.1 Backup Personnel (MANDATORY)

Per ISMS-POL-A.5.7 Section 4.4.6, all critical threat intelligence roles SHALL have documented backup personnel:

| Primary Role | Backup Role | Cross-Training Frequency | Test Frequency |
|--------------|-------------|-------------------------|----------------|
| CISO | Deputy CISO / Senior Security Manager | Annual | Annual |
| Threat Intelligence Coordinator | Senior TI Analyst / SOC Manager | Quarterly | Annual |
| Threat Intelligence Analyst | Other TI Analysts / SOC Analysts | Quarterly | Semi-annual |
| SOC Team | Shift-based operations | Ongoing | N/A (continuous) |

**Requirements**:
- Backup personnel SHALL be identified and documented
- Cross-training SHALL be conducted at specified frequencies
- Critical source access SHALL be documented for backup personnel
- Minimal operations playbook SHALL exist (daily checks, alert triage, stakeholder notification)
- Business continuity plan SHALL be tested at specified frequencies

**Documentation**:
- ISMS-IMP-A.5.7.1 Sheet 15 (Continuity Plan)
- Test results maintained for audit verification

### 3.10.2 Continuity Scenarios

Backup personnel must be capable of maintaining operations during:
- Planned leave (vacation, training)
- Unplanned absence (illness, emergency)
- Organizational changes (resignation, reorganization)
- Major incidents (requiring all-hands response)

**Minimum Capability During Continuity Events**:
- Daily source monitoring maintained
- Critical alerts (P1/P2) triaged within SLA (≤4 hours)
- Incident support provided for active P1/P2 incidents
- Strategic intelligence production may be delayed (acceptable)

---

## 3.11 Competency and Training

### 3.11.1 Competency Requirements

Personnel performing threat intelligence functions SHALL possess or develop competencies appropriate to their role:

**Threat Intelligence Coordinator/Manager**:
- Threat intelligence program management
- Understanding of cyber threat landscape and actor ecosystem
- Strategic, tactical, and operational intelligence methodologies
- Threat intelligence frameworks (MITRE ATT&CK, Diamond Model, Kill Chain)
- Leadership and stakeholder communication
- **ISO 27001:2022 Control A.5.7 audit evidence requirements**
- **Assessment workbook generation and validation**

**Threat Intelligence Analysts**:
- Analytical thinking and research methodologies
- Malware analysis fundamentals
- Network security and attack techniques
- Intelligence writing and reporting
- Threat intelligence tools and platforms
- **Evidence documentation practices**
- **Admiralty Code source evaluation**

**SOC Analysts**:
- Understanding of IOCs and threat actor TTPs
- SIEM and security tool operation
- Threat hunting fundamentals
- Incident triage and enrichment

**Risk Management Personnel**:
- **Understanding of threat intelligence integration into Clause 6.1 risk assessment**
- **Cross-reference documentation practices** (TI Report → Risk Register)

### 3.11.2 Training and Development

The organization SHALL provide training and development opportunities including:
- Initial onboarding for threat intelligence roles
- Ongoing training on emerging threats and techniques
- Participation in industry conferences and threat intelligence communities
- Cross-training with incident response and threat hunting
- Vendor-provided training for threat intelligence platforms
- Certification programs (e.g., GCTI, CTIA) where appropriate
- **Audit preparation training** (evidence generation, workbook completion)
- **Business continuity drills** (backup personnel activation)

**Training Frequency**:
- Initial onboarding: Within 30 days of role assignment
- Ongoing training: Quarterly minimum
- Cross-training: Per schedule in Section 3.10.1
- Audit preparation: 30 days before certification audit

---

**END OF DOCUMENT**