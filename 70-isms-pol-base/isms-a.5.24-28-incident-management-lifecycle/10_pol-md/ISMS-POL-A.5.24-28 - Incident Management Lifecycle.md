# ISMS-POL-A.5.24-28 – Incident Management Lifecycle

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Incident Management Lifecycle |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.24-28 |
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
- Technical: Incident Response Manager / CSIRT Lead
- Legal: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide)
- ISMS-IMP-A.5.24-28.S1 through S5 (Implementation Assessments)
- ISO/IEC 27001:2022 Controls A.5.24, A.5.25, A.5.26, A.5.27, A.5.28
- ISMS-POL-A.8.15 (Logging)
- ISMS-POL-A.8.16 (Monitoring Activities)
- ISMS-POL-A.6.8 (Information Security Event Reporting)
- ISMS-POL-A.5.29-30 (Business Continuity & Disaster Recovery)
- ISMS-POL-A.5.31 (Legal, Statutory, Regulatory Requirements)

---

## Executive Summary

This policy establishes [Organization]'s requirements for managing information security incidents throughout their complete lifecycle in accordance with ISO/IEC 27001:2022 Controls A.5.24 (Planning & Preparation), A.5.25 (Assessment & Decision), A.5.26 (Response), A.5.27 (Learning), and A.5.28 (Evidence Collection & Preservation).

**Scope**: This policy applies to all information security events and incidents affecting [Organization]'s information assets, systems, networks, and services, regardless of source (internal, external, third-party) or deployment model (on-premises, cloud, hybrid).

**Purpose**: Define organizational requirements for incident management control implementation and governance. This policy establishes WHAT incident management capabilities are required, WHO is accountable, WHEN actions must occur, and WHY these controls are essential. Implementation procedures (HOW to execute incident response) are documented separately in ISMS-IMP-A.5.24-28 Implementation Guides. Technical standards, forensic techniques, and incident classification taxonomies are intentionally defined outside this policy to preserve operational agility.

**Combined Control Approach**: These five controls are implemented as a unified lifecycle framework because they represent sequential and interconnected phases of the same incident management process. All five controls operate on the same organizational capabilities (CSIRT/SOC, procedures, training, tools) and share common assessment and evidence collection processes. Despite unified implementation, each control maintains distinct requirements for Statement of Applicability (SoA) purposes.

**Lifecycle Phases**:
1. **Planning & Preparation (A.5.24)** - Establish capabilities before incidents occur
2. **Assessment & Decision (A.5.25)** - Determine if event is an incident requiring response
3. **Response Operations (A.5.26)** - Contain, eradicate, recover from incidents
4. **Evidence Collection (A.5.28)** - Preserve forensic evidence (parallel to response)
5. **Learning & Improvement (A.5.27)** - Extract lessons, improve controls

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including GDPR 72-hour breach notification (Art. 33-34), Swiss nDSG breach notification (Art. 24), and ISO/IEC 27001:2022. Conditional sector-specific requirements (PCI DSS, FINMA, DORA, NIS2) apply where [Organization]'s business activities trigger applicability.

**Why Incident Management Matters**: Security incidents are inevitable - the question is not "if" but "when." Industry data shows the average cost of a data breach exceeds $4.45M USD, mean time to identify (MTTD) is 204 days, and mean time to contain (MTTC) is 73 days. Organizations with mature incident response capabilities reduce breach costs by an average of $2M USD through faster detection, containment, and recovery. This framework addresses these risks through systematic preparation, response, and continuous improvement.

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control Statements

**ISO/IEC 27001:2022 Annex A.5.24 - Information Security Incident Management Planning and Preparation**

> *The organization shall plan and prepare for managing information security incidents by defining, establishing and communicating information security incident management processes, roles and responsibilities.*

**Control Objective**: Establish incident management capabilities BEFORE incidents occur through documented procedures, trained personnel, defined roles, appropriate tools, and integration with organizational processes.

**Focus**: Planning - Preparing procedures & training

---

**ISO/IEC 27001:2022 Annex A.5.25 - Assessment and Decision on Information Security Events**

> *The organization shall assess information security events and decide if they are to be categorized as information security incidents.*

**Control Objective**: Systematically evaluate security events to determine if they constitute incidents requiring response, ensuring appropriate classification, prioritization, and escalation based on organizational risk.

**Focus**: Assessment - Determining if an event is an incident

---

**ISO/IEC 27001:2022 Annex A.5.26 - Response to Information Security Incidents**

> *Information security incidents shall be responded to in accordance with the documented procedures.*

**Control Objective**: Execute coordinated response to contain, eradicate, and recover from security incidents, minimizing business impact while maintaining communication and service restoration.

**Focus**: Response - Containing & Eradicating the threat

---

**ISO/IEC 27001:2022 Annex A.5.27 - Learning from Information Security Incidents**

> *Knowledge gained from information security incidents shall be used to strengthen and improve the information security controls.*

**Control Objective**: Extract lessons from incidents through systematic analysis and translate findings into tangible control improvements, ensuring the organization becomes more resilient with each incident.

**Focus**: Learning - Post-incident analysis & improvement

---

**ISO/IEC 27001:2022 Annex A.5.28 - Collection of Evidence**

> *The organization shall establish and implement procedures for the identification, collection, acquisition and preservation of evidence related to information security events.*

**Control Objective**: Preserve forensic evidence with legal admissibility, maintaining chain of custody and supporting potential legal proceedings, regulatory investigations, or root cause analysis.

**Focus**: Evidence - Forensic collection & preservation

---

### 1.2 Lifecycle Integration & Process Flow

These five controls form a **complete incident management lifecycle**:

```
                          ┌───────────────────────────────────────┐
                          │         A.5.24 - PLANNING            │
                          │   Procedures, Roles, Tools, Training  │
                          │   (Establish capabilities BEFORE)     │
                          └───────────────┬───────────────────────┘
                                          │
                                          ↓
                          ┌───────────────────────────────────────┐
                          │     SECURITY EVENT DETECTED           │
                          │   (A.8.16 Monitoring, A.6.8 Reporting)│
                          └───────────────┬───────────────────────┘
                                          │
                                          ↓
                          ┌───────────────────────────────────────┐
                          │      A.5.25 - ASSESSMENT              │
                          │  Event → Incident Determination        │
                          │  Severity Classification, Escalation   │
                          └───────────┬───────────────────────────┘
                                      │
                    ┌─────────────────┴─────────────────┐
                    │                                   │
                    ↓                                   ↓
        ┌───────────────────────┐         ┌───────────────────────┐
        │   A.5.26 - RESPONSE   │         │  A.5.28 - EVIDENCE    │
        │   • Containment       │◄────────┤  • Forensic capture   │
        │   • Eradication       │────────►│  • Chain of custody   │
        │   • Recovery          │         │  • Legal preservation │
        └───────────┬───────────┘         └───────────────────────┘
                    │                                   │
                    └─────────────────┬─────────────────┘
                                      │
                                      ↓
                          ┌───────────────────────────────────────┐
                          │      A.5.27 - LEARNING                │
                          │   Post-Incident Review (PIR)           │
                          │   Root Cause Analysis, Improvements    │
                          └───────────────┬───────────────────────┘
                                          │
                                          ↓
                          ┌───────────────────────────────────────┐
                          │   CONTROL IMPROVEMENTS IMPLEMENTED     │
                          │   Feeds back to A.5.24 (Preparation)   │
                          │   Updates procedures, training, tools  │
                          └───────────────────────────────────────┘
```

**Critical Integration Points**:

- **A.5.24 ↔ A.8.16 (Monitoring)**: Monitoring infrastructure detects events, triggers assessment
- **A.5.25 ↔ A.6.8 (Event Reporting)**: User reports feed event assessment process
- **A.5.26 ↔ A.5.28 (Parallel)**: Evidence collection occurs DURING response, not after
- **A.5.26 ↔ A.5.29-30 (BC/DR)**: Major incidents may trigger business continuity procedures
- **A.5.27 → A.5.24 (Feedback)**: Lessons learned improve preparation for future incidents
- **All phases ↔ A.5.31 (Legal/Regulatory)**: Compliance obligations throughout lifecycle

**Statement of Applicability Independence**: Although implemented as a unified lifecycle framework, Controls A.5.24, A.5.25, A.5.26, A.5.27, and A.5.28 are assessed independently in the Statement of Applicability. Each control retains distinct requirements, evidence collection, and compliance scoring for audit purposes.

### 1.3 What This Policy Does

This policy:
- **Defines** incident management requirements aligned with organizational risk assessment
- **Establishes** governance framework for incident response decision-making
- **Specifies** accountability for incident management control implementation
- **Mandates** lifecycle phases from planning through learning
- **References** applicable regulatory requirements per ISMS-POL-00
- **Integrates** five sequential controls into unified framework for implementation efficiency
- **Sets** minimum standards for incident classification, response times, evidence handling, and learning

### 1.4 What This Policy Does NOT Do

This policy does NOT:
- **Specify technical implementation details** (see ISMS-IMP-A.5.24-28 Implementation Guides)
- **Define incident response procedures step-by-step** (see ISMS-IMP-A.5.24-28.S3 Response Procedures)
- **Provide incident classification taxonomy** (see ISMS-REF-A.5.24-28 Section 1)
- **Select incident management tools** (SIEM, ticketing, forensics - selected per risk assessment)
- **Define forensic techniques** (see ISMS-REF-A.5.24-28 Section 3)
- **Establish CSIRT/SOC organizational structure** (structure based on [Organization] size and risk)
- **Document response playbooks** (playbooks per incident type in IMP)
- **Replace risk assessment** (incident management controls selected based on [Organization]'s risk treatment)

**Rationale**: Separating policy requirements from implementation guidance enables:
- Policy stability despite evolving threat landscape and incident response techniques
- Technical agility for tool and procedure updates without policy revision
- Clear distinction between governance (policy) and execution (implementation)
- Focused audit scope (auditors audit policy compliance, not specific tool configurations)
- Technology-agnostic approach applicable to any incident management architecture

### 1.5 Scope & Applicability

**In Scope:**

**Information Security Incidents** affecting:
- IT systems (servers, workstations, network devices, databases)
- Applications (internal, customer-facing, third-party SaaS)
- Data and information assets (confidential, personal, proprietary)
- Network infrastructure (on-premises, cloud, hybrid)
- Users and authentication systems
- Third-party systems interfacing with [Organization] systems
- Physical security incidents affecting information assets

**Incident Categories** (all categories):
- Malware and ransomware
- Unauthorized access and privilege escalation
- Data breaches and exfiltration
- Denial of service (DoS/DDoS)
- Social engineering and phishing
- Insider threats (malicious, negligent)
- Physical security incidents affecting IT
- Supply chain and third-party incidents
- Configuration errors causing security impact
- Lost or stolen devices containing organizational data

**Out of Scope** (exclusions require Executive Management approval and documented risk acceptance):
- Incidents affecting only Public (unclassified) information with no business impact
- Incidents explicitly managed by separate frameworks (e.g., safety incidents, HR violations without security component)
- Third-party incidents with contractual incident management delegation (must be documented)

**Risk-Based Scaling**: Incident management capabilities SHALL be proportional to:
- [Organization]'s risk assessment outcomes (likelihood and impact of security incidents)
- Regulatory obligations (breach notification requirements)
- Business criticality of affected systems
- Data classification and sensitivity

**Applicability to Third Parties**: Third-party service providers, contractors, and partners accessing [Organization] systems or handling [Organization] data MUST:
- Report security events and incidents per [Organization] reporting requirements
- Cooperate with [Organization] incident response activities
- Comply with evidence preservation requirements
- Participate in post-incident reviews when third-party actions contributed to incident

**Cloud Services**: Cloud service providers (AWS, Azure, GCP, SaaS vendors) incidents affecting [Organization]:
- Cloud provider incidents impacting [Organization] services SHALL be assessed per A.5.25
- [Organization] SHALL respond to shared responsibility incidents per cloud security model
- Cloud provider incident response capabilities SHALL be evaluated per A.5.23 (Cloud Services)

### 1.6 Regulatory Applicability

This policy implements incident management requirements to comply with regulations per **ISMS-POL-00 (Regulatory Applicability Framework)**:

**Tier 1: Mandatory Compliance**

| Regulation | Requirement | Applicability |
|------------|-------------|---------------|
| **Swiss nDSG (Federal Data Protection Act)** | Art. 24 - Data breach notification to FDPIC "as soon as possible" when high risk to personality/rights | All Swiss operations |
| **EU GDPR (General Data Protection Regulation)** | Art. 33 - Breach notification to supervisory authority within 72 hours; Art. 34 - Communication to data subjects when high risk | When processing EU personal data |
| **ISO/IEC 27001:2022** | Controls A.5.24, A.5.25, A.5.26, A.5.27, A.5.28 | Certification scope |

**Tier 2: Conditional Applicability**

| Regulation | Requirement | Trigger Condition |
|-----------|-------------|-------------------|
| **PCI DSS v4.0 (Payment Card Industry Data Security Standard)** | Req. 12.10 - Incident response plan, documented procedures, personnel training, forensic investigation | Processing, storing, or transmitting payment card data |
| **FINMA (Swiss Financial Market Supervisory Authority)** | Circular 2023/1 - Operational incident reporting to FINMA, incident response capabilities | Swiss financial institution supervised by FINMA |
| **DORA (Digital Operational Resilience Act)** | Art. 17-20 - Major ICT incident classification, reporting to competent authorities, root cause analysis | EU financial entity or critical ICT third-party service provider |
| **NIS2 Directive (Network and Information Security)** | Art. 23 - Significant incident notification within 24 hours (early warning), detailed report within 72 hours | Essential or important entity under NIS2 (EU) |
| **HIPAA (Health Insurance Portability and Accountability Act)** | 45 CFR §164.400-414 - Breach notification rules for ePHI (electronic protected health information) | US healthcare data processing |

**Tier 3: Informational Guidance**

Best practice frameworks referenced but not mandatory compliance requirements:
- NIST SP 800-61 Rev. 2 (Computer Security Incident Handling Guide)
- SANS Incident Handler's Handbook
- ISO/IEC 27035 (Information Security Incident Management)
- ENISA Threat Landscape Reports
- MITRE ATT&CK Framework (adversary tactics and techniques)
- CISA Cybersecurity Incident Response Guide

**United States Federal Requirements**: References to US federal frameworks (FISMA, FIPS, FedRAMP, NIST cybersecurity requirements) apply only where [Organization] has explicit US federal contractual obligations, as defined in ISMS-POL-00.

**Compliance Determination**: Legal/Compliance Officer determines applicability of Tier 2 regulations based on [Organization]'s business activities and regulatory status. Data Protection Officer (DPO) advises on GDPR and nDSG breach notification requirements.

**Operational Guidance**: ISMS-REF-A.5.24-28 Section 2 (Regulatory Notification Quick Reference) provides operational procedures, timelines, templates, and contacts for regulatory notifications once applicability is determined.

### 1.7 Definitions & Terminology

**Information Security Event**: An identified occurrence of a system, service, or network state indicating a possible breach of information security policy or failure of safeguards, or a previously unknown situation that may be security relevant. Events may or may not become incidents upon assessment.

**Information Security Incident**: A single or a series of unwanted or unexpected information security events that have a significant probability of compromising business operations and threatening information security. Incidents require response actions.

**Incident Severity**: Classification of incident impact and urgency. [Organization] uses four severity levels: Critical, High, Medium, Low. Severity determines response priorities and escalation requirements.

**Incident Category**: Classification of incident type based on attack vector, threat actor, or impact. Examples: malware, unauthorized access, data breach, denial of service. Full taxonomy in ISMS-REF-A.5.24-28 Section 1.

**CSIRT (Computer Security Incident Response Team)**: Organizational team responsible for receiving, reviewing, and responding to information security incidents. May be dedicated team or virtual team assembled from multiple departments.

**SOC (Security Operations Center)**: Team or function responsible for monitoring, detecting, analyzing, and responding to security events and incidents. May be combined with or separate from CSIRT.

**Containment**: Actions taken to limit the scope and magnitude of an incident. Short-term containment (immediate isolation) and long-term containment (temporary fixes) prepare for eradication.

**Eradication**: Actions to eliminate the root cause of an incident (remove malware, close vulnerabilities, revoke compromised credentials).

**Recovery**: Actions to restore affected systems and services to normal operations. Includes verification that systems are functioning normally and threats are eliminated.

**Post-Incident Review (PIR)**: Structured review conducted after incident closure to document timeline, assess response effectiveness, identify lessons learned, and recommend improvements. Also known as "After Action Review" or "Lessons Learned Session."

**Root Cause Analysis (RCA)**: Systematic investigation to identify the fundamental cause(s) that allowed an incident to occur, enabling preventive measures to address systemic issues.

**Forensic Evidence**: Information collected and preserved in a manner suitable for legal proceedings, regulatory investigations, or detailed technical analysis. Requires chain of custody and integrity protection.

**Chain of Custody**: Documented trail showing who collected evidence, when, where, how, and every transfer of evidence between parties. Essential for legal admissibility.

**Mean Time to Detect (MTTD)**: Average time from when an incident occurs to when it is detected by [Organization]. Key performance metric for monitoring effectiveness.

**Mean Time to Respond (MTTR)**: Average time from incident detection to initial response action. Key performance metric for incident response effectiveness.

**Mean Time to Contain (MTTC)**: Average time from incident detection to containment of the threat. Key metric for measuring damage limitation capability.

**False Positive**: Security event flagged as potential incident but determined through assessment to be benign or expected behavior. False positive rate indicates alert tuning effectiveness.

**Escalation**: Process of elevating incident to higher authority or expertise level based on severity, complexity, or lack of progress. Includes management escalation and technical escalation.

**Legal Hold**: Directive to preserve all potentially relevant evidence related to pending or reasonably anticipated legal proceedings or regulatory investigations. Overrides normal data retention/deletion policies.

---

## 2. Requirements Framework

### 2.1 Incident Management Planning & Preparation (A.5.24)

[Organization] SHALL establish incident management capabilities BEFORE incidents occur through documented procedures, trained personnel, defined roles, appropriate tools, and integration with organizational processes.

#### 2.1.1 Incident Management Governance

**Organizational Structure**:

[Organization] MUST establish incident response capability through one or both of:
- **CSIRT (Computer Security Incident Response Team)**: Dedicated or virtual team responsible for incident response coordination
- **SOC (Security Operations Center)**: Team responsible for security monitoring and initial incident triage

**Minimum Staffing Requirements**:
- **Incident Response Manager/CSIRT Lead**: Overall accountability for incident response program
- **Incident Handlers**: Minimum 2 trained personnel capable of leading incident response (support 24/7 on-call rotation)
- **Forensic Specialists**: Access to forensic expertise (internal or contracted)
- **Communications Coordinator**: Responsible for internal/external incident communications

**Authority & Decision Rights**:
- **Incident Response Manager**: Authority to escalate to executive management, engage external resources, declare major incident
- **CISO**: Authority to approve exceptions, accept residual risk, approve major incident response plans
- **Executive Management**: Authority for business-critical decisions (service shutdown, public disclosure, law enforcement engagement)

**Documentation Requirements**:

[Organization] MUST document:
- Incident response organizational structure (RACI matrix for incident lifecycle phases)
- Roles and responsibilities for incident response team members
- Escalation paths and authority levels
- Integration with organizational functions (IT operations, legal, HR, communications, executive management)

**Implementation Reference**: ISMS-IMP-A.5.24-28.S1 Section 2 provides assessment framework for evaluating governance maturity.

#### 2.1.2 Incident Classification Framework

[Organization] MUST establish and maintain an incident classification framework defining:

**Severity Levels** (minimum 4 levels required):

| Severity | Definition | Response SLA | Escalation Requirement |
|----------|------------|--------------|------------------------|
| **Critical** | Significant business impact: large-scale data breach, ransomware affecting production systems, compromise of critical infrastructure, regulatory breach notification triggered | Initial response: ≤15 minutes; Containment target: ≤1 hour | Immediate escalation to CISO and Executive Management; activate crisis management |
| **High** | Moderate business impact: targeted attack, confirmed data exfiltration, compromise of sensitive systems, service degradation | Initial response: ≤1 hour; Containment target: ≤4 hours | Escalation to Incident Response Manager; CISO notification within 2 hours |
| **Medium** | Limited business impact: isolated malware infection, unsuccessful attack attempts, minor policy violations with security implications | Initial response: ≤4 hours; Containment target: ≤24 hours | Team Lead notification; escalation if not resolved within 24 hours |
| **Low** | Minimal business impact: single false positive, minor security anomaly, informational security event | Initial response: ≤8 hours (next business day acceptable); Containment target: ≤5 business days | Standard incident handling; no escalation required unless pattern emerges |

**Note**: Specific SLA times may be adjusted based on [Organization]'s risk assessment and operational capabilities, but MUST be documented and approved by CISO.

**Incident Categories**:

[Organization] MUST categorize incidents using a structured taxonomy covering at minimum:
- Malware and ransomware incidents
- Unauthorized access and privilege escalation
- Data breaches and data exfiltration
- Denial of service attacks
- Social engineering and phishing
- Insider threats (malicious and negligent)
- Physical security incidents affecting information assets
- Third-party and supply chain incidents
- Configuration errors with security impact

**Detailed Taxonomy**: ISMS-REF-A.5.24-28 Section 1 provides comprehensive incident classification taxonomy with subcategories, examples, and severity indicators.

**Classification Requirements**:
- All security events MUST be assessed using the incident classification framework
- Classification MUST occur within response SLA timeframes per severity level
- Classification MUST be documented in incident management system
- Severity reassessment MUST occur as incident investigation progresses

#### 2.1.3 Incident Response Procedures

[Organization] MUST document and maintain incident response procedures covering:

**Mandatory Procedure Coverage**:

1. **Event Detection and Reporting**:
   - How security events are detected (A.8.16 monitoring integration)
   - How users report suspected incidents (A.6.8 reporting integration)
   - Initial event triage procedures

2. **Incident Assessment** (A.5.25 procedures):
   - Event to incident determination criteria
   - Severity classification procedure
   - Escalation decision process

3. **Incident Response** (A.5.26 procedures):
   - Containment procedures (short-term and long-term)
   - Eradication procedures
   - Recovery and service restoration procedures
   - Communications protocols (internal, external, regulatory)

4. **Evidence Collection** (A.5.28 procedures):
   - When to collect forensic evidence
   - Evidence collection techniques
   - Chain of custody requirements
   - Evidence preservation and storage

5. **Post-Incident Activities** (A.5.27 procedures):
   - Post-Incident Review (PIR) requirements
   - Root cause analysis methodology
   - Lessons learned documentation
   - Control improvement process

**Procedure Format Requirements**:
- Procedures MUST be written clearly for target audience (incident handlers)
- Procedures MUST include roles and responsibilities
- Procedures MUST reference external resources (ISMS-REF, technical guides)
- Procedures MUST be version controlled and reviewed annually minimum

**Playbook Development**:

[Organization] SHOULD develop incident-specific playbooks for common incident types:
- Ransomware response playbook
- Data breach response playbook
- Phishing/social engineering playbook
- Insider threat playbook
- DDoS attack playbook
- Cloud service compromise playbook

**Playbook Requirements**:
- Step-by-step procedures specific to incident type
- Decision trees for common scenarios
- Pre-authorized actions (what can be done without escalation)
- Communication templates
- Evidence collection checklists

**Implementation Reference**: ISMS-IMP-A.5.24-28.S3 provides response procedure assessment framework and playbook coverage evaluation.

#### 2.1.4 Training & Awareness Requirements

[Organization] MUST ensure incident response personnel are trained and competent:

**Incident Response Team Training**:

**Initial Training** (before assuming incident response duties):
- Incident response procedures and lifecycle
- Incident classification and severity determination
- Use of incident management tools (ticketing, SIEM, forensic tools)
- Communication protocols and escalation procedures
- Evidence handling and chain of custody
- Legal and regulatory requirements

**Ongoing Training** (annual minimum):
- Threat landscape updates
- New attack techniques and adversary tactics (MITRE ATT&CK)
- Procedure updates and lessons learned from recent incidents
- Tool and technology updates
- Regulatory requirement changes

**Tabletop Exercises**:

[Organization] MUST conduct incident response tabletop exercises:
- **Frequency**: Minimum twice annually
- **Scope**: Major incident scenarios (ransomware, data breach, DDoS)
- **Participants**: Incident response team, IT operations, executive management (as appropriate)
- **Documentation**: Exercise scenarios, outcomes, lessons learned, improvement actions

**Technical Exercises** (for technical incident handlers):
- Forensic analysis exercises
- Malware analysis practice
- Log analysis and correlation exercises
- Evidence collection practice

**Awareness Training** (all personnel):

[Organization] MUST provide security awareness training including:
- How to recognize and report security incidents
- Incident reporting channels (A.6.8 integration)
- User responsibilities during incidents
- Examples of common incidents (phishing, malware, data loss)

**Competency Assessment**:
- Incident Response Manager MUST verify team member competency through exercises, assessments, or certification
- Training records MUST be maintained (training date, topic, attendees)
- Gaps in competency MUST be addressed through additional training

#### 2.1.5 Tools & Technology Capabilities

[Organization] MUST provide incident response team with appropriate tools:

**Mandatory Capabilities**:

**Incident Management System**:
- Incident logging and tracking (ticketing system)
- Workflow management (status tracking, assignment, escalation)
- Communication and collaboration features
- Evidence attachment and documentation
- Reporting and metrics

**Security Monitoring Integration**:
- SIEM (Security Information and Event Management) access for incident handlers
- Log analysis capabilities
- Threat intelligence integration
- Alert triage and enrichment capabilities

**Forensic Capabilities**:
- Disk imaging tools (for evidence collection)
- Memory capture tools
- Log preservation mechanisms
- Forensic analysis workstation (isolated environment)
- Evidence storage (secure, access-controlled)

**Communication Tools**:
- Secure communication channels for incident team (encrypted chat, conference bridge)
- Pre-defined distribution lists (incident response team, management, stakeholders)
- Templates for common communications (user notifications, management updates, regulatory notifications)

**Tool Selection Criteria**:
- Tools selected based on [Organization]'s risk assessment and operational requirements
- Tool capabilities documented in ISMS-REF-A.5.24-28 Section 3 (Forensic Techniques Library)
- Tool access restricted to incident response team members
- Tool usage tracked for audit purposes

**Cloud-Based Incident Response**:
- Cloud service provider incident response APIs and tools (AWS GuardDuty, Azure Sentinel, GCP Chronicle)
- Cloud forensic capabilities (snapshot, export, analysis)
- Cloud-native SIEM/SOAR platforms

#### 2.1.6 Integration with Organizational Processes

Incident management MUST integrate with:

**A.8.16 (Monitoring Activities)**:
- Monitoring infrastructure detects security events
- Alerts feed incident assessment process (A.5.25)
- Incident response team has access to monitoring data for investigation

**A.8.15 (Logging)**:
- Comprehensive logs available for incident investigation
- Log retention sufficient for forensic analysis and regulatory requirements
- Logs protected from tampering

**A.6.8 (Information Security Event Reporting)**:
- User reporting mechanism feeds incident assessment
- Users trained on what to report and how
- Reporting channel monitored by incident response team

**A.5.29-30 (Business Continuity & Disaster Recovery)**:
- Major incidents may trigger BC/DR procedures
- Incident severity assessment considers business continuity impact
- Incident response coordinates with BC/DR team for major incidents

**A.5.31 (Legal, Statutory, Regulatory Requirements)**:
- Incident response procedures incorporate regulatory notification requirements
- Legal team engaged for incidents with legal implications
- Regulatory reporting procedures documented and tested

**A.5.19-23 (Third-Party Management)**:
- Third-party security incidents reported to [Organization]
- Third-party vendors cooperate with incident response
- Contracts include incident response and notification requirements

**Change Management**:
- Emergency changes during incident response follow expedited change approval
- Post-incident changes (control improvements) follow standard change management

**Human Resources**:
- HR engaged for insider threat incidents
- HR supports employee communications during incidents
- HR coordinates employee training requirements

### 2.2 Event Assessment & Incident Classification (A.5.25)

[Organization] SHALL systematically assess all security events to determine if they constitute incidents requiring response, ensuring appropriate classification, prioritization, and escalation.

#### 2.2.1 Event Assessment Process

**Trigger Conditions**:

Assessment MUST occur when:
- Security monitoring system generates alert (A.8.16 integration)
- User reports suspected security issue (A.6.8 integration)
- Third-party notifies [Organization] of potential incident
- Security scan or audit identifies anomaly requiring investigation
- Threat intelligence indicates [Organization] may be affected

**Assessment Procedure**:

**Step 1: Initial Triage** (within 15 minutes for Critical alerts, 1 hour for High):
1. Review alert/report details
2. Verify event is not false positive
3. Gather initial context (affected systems, users, data)
4. Determine if event meets incident criteria

**Step 2: Incident Determination**:

Event is classified as **incident** if it meets ANY of:
- Confirmed or suspected compromise of system confidentiality, integrity, or availability
- Confirmed or suspected unauthorized access to data or systems
- Confirmed malware infection or malicious activity
- Confirmed or suspected data exfiltration or breach
- Attack in progress (even if unsuccessful so far)
- Policy violation with security implications
- Regulatory breach notification trigger

Event is classified as **non-incident** if:
- False positive (alert on expected/authorized behavior)
- Attempted attack successfully blocked by security controls (log for trending, no response needed)
- Informational only (no security impact)

**Ambiguous Cases**:
- When in doubt, treat as incident and escalate
- Incident Response Manager makes final determination for ambiguous cases
- Reclassification allowed as investigation progresses

#### 2.2.2 Severity Classification

All incidents MUST be assigned severity level per framework in Section 2.1.2.

**Severity Determination Factors**:

**Confidentiality Impact**:
- What data classification level is affected? (Public/Internal/Confidential/Restricted)
- Volume of data potentially compromised
- Sensitivity of data (personal data, financial, trade secrets, credentials)
- Regulatory notification requirements triggered?

**Integrity Impact**:
- Are systems or data modified by unauthorized party?
- Can we trust system/data integrity?
- Malware infection confirmed?
- Potential for malicious code persistence?

**Availability Impact**:
- Are critical services disrupted?
- Number of users or systems affected
- Revenue or operational impact
- Violation of SLAs or commitments to customers

**Additional Factors**:
- Threat actor sophistication (automated attack vs. targeted APT)
- Attack stage (reconnaissance vs. data exfiltration)
- Containment difficulty (isolated system vs. widespread)
- Media/reputational risk

**Severity Examples** (detailed examples in ISMS-REF-A.5.24-28 Section 1):

**Critical**:
- Ransomware encrypting production systems
- Confirmed exfiltration of Restricted data or large volume of Confidential data
- Compromise of privileged accounts (domain admin, cloud admin)
- Customer-facing service completely unavailable
- GDPR breach notification threshold exceeded

**High**:
- Malware on endpoint with Confidential data access
- Unauthorized access to production database
- Targeted phishing with credential compromise
- DDoS causing service degradation
- Insider threat with confirmed data access

**Medium**:
- Isolated malware infection on endpoint (no data access)
- Unsuccessful privilege escalation attempt
- Phishing email delivered but no user interaction
- Minor configuration error exposing Internal data

**Low**:
- Port scan against perimeter (no breach)
- Single failed login attempt
- Minor policy violation (no data at risk)

#### 2.2.3 Category Classification

All incidents MUST be assigned category per taxonomy:

**Primary Categories** (detailed subcategories in ISMS-REF-A.5.24-28 Section 1):

1. **Malware**: Virus, worm, trojan, ransomware, cryptominer, spyware, rootkit
2. **Unauthorized Access**: Compromised credentials, privilege escalation, backdoor access, account takeover
3. **Data Breach**: Data exfiltration, data leakage, unauthorized disclosure, theft of data
4. **Denial of Service**: DDoS, resource exhaustion, service disruption
5. **Social Engineering**: Phishing, spear-phishing, BEC (business email compromise), pretexting, impersonation
6. **Insider Threat**: Malicious insider, negligent insider, compromised insider
7. **Physical Security**: Unauthorized physical access, theft of equipment, damage to infrastructure
8. **Third-Party**: Supplier compromise, supply chain attack, vendor security incident
9. **Configuration Error**: Misconfiguration exposing data, unauthorized change, security control failure
10. **Web Application**: SQL injection, XSS, authentication bypass, API abuse

**Multiple Categories**: Incident may have multiple categories (e.g., phishing leading to malware infection). Record primary category and secondary categories.

**Category-Specific Response**: Category determines which playbook to use for response (Section 2.3).

#### 2.2.4 Escalation Requirements

Incidents MUST be escalated per severity matrix:

**Immediate Escalation (within 15 minutes)**:
- **Critical** severity incidents → CISO + Executive Management + Crisis Management Team
- **High** severity with regulatory notification potential → CISO + Legal + DPO
- Suspected APT or nation-state attack → CISO + External threat intelligence

**Timely Escalation**:
- **High** severity incidents → Incident Response Manager (immediate), CISO (within 2 hours)
- **Medium** severity not resolved within 24 hours → Team Lead → Incident Response Manager
- **Low** severity showing pattern or trend → Team Lead

**Management Notification**:
- Critical incidents: Executive Management briefing within 1 hour of classification
- High incidents: Executive Management daily status updates
- All incidents: Weekly executive summary report

**External Escalation**:
- Law enforcement (if criminal activity suspected): CISO decision, Executive Management approval
- Regulatory authorities (if breach notification triggered): Legal + DPO coordination
- Cyber insurance carrier (if incident covered): CFO + Legal coordination
- Customers/partners (if their data affected): Executive Management approval, Communications team execution

#### 2.2.5 Assessment Documentation

All event assessments MUST be documented in incident management system:

**Required Documentation**:
- Event details (timestamp, source, affected systems)
- Assessment outcome (incident vs. non-incident)
- Severity and category classification
- Rationale for classification decisions
- Escalation actions taken
- Time to assess (metric for continuous improvement)

**False Positive Handling**:
- False positives documented with rationale
- False positive rate tracked per alert source
- Alert tuning recommendations generated
- Quarterly false positive review

**Quality Control**:
- Incident Response Manager MUST review classification for High and Critical incidents
- Quarterly review of severity classification accuracy
- Reclassification process for incidents where initial assessment was incorrect

### 2.3 Incident Response Operations (A.5.26)

[Organization] SHALL respond to confirmed incidents in accordance with documented procedures, executing coordinated response to contain, eradicate, and recover from security incidents.

#### 2.3.1 Response Lifecycle Phases

**Phase 1: Containment**

**Objective**: Limit the scope and magnitude of an incident, preventing further damage.

**Short-Term Containment** (immediate actions to stop spread):
- Isolate affected systems from network (quarantine)
- Disable compromised user accounts
- Block malicious IP addresses, domains, or URLs at perimeter
- Increase logging and monitoring on potentially affected systems
- Preserve evidence BEFORE containment actions if possible (coordinate with A.5.28)

**Long-Term Containment** (temporary fixes to maintain business operations while preparing for eradication):
- Apply temporary patches or workarounds
- Implement additional monitoring for affected areas
- Restore systems from clean backups to isolated environment
- Enable enhanced authentication for potentially compromised areas

**Containment Decisions**:
- **Critical/High Severity**: Aggressive containment prioritized over service availability (isolate systems even if causes disruption)
- **Medium/Low Severity**: Balanced approach between containment and business continuity
- **Business-Critical Systems**: Containment decision requires Incident Response Manager or CISO approval

**Containment Verification**:
- Verify threat is successfully contained (no lateral movement, no continued exfiltration)
- Monitor for signs of reinfection or persistent threat
- Document containment actions and effectiveness

**Phase 2: Eradication**

**Objective**: Remove the root cause of the incident, ensuring threat is completely eliminated.

**Eradication Actions** (vary by incident category):

**Malware Incidents**:
- Remove malware from infected systems (reimaging preferred over cleaning)
- Identify and close vulnerability that allowed infection
- Scan all potentially affected systems
- Verify malware removal through forensic analysis

**Unauthorized Access Incidents**:
- Revoke compromised credentials (passwords, API keys, certificates)
- Close backdoors and persistent access mechanisms
- Patch vulnerabilities exploited for access
- Review and remove unauthorized accounts
- Force password reset for affected users

**Configuration Error Incidents**:
- Correct misconfiguration
- Verify configuration across environment (check for other similar issues)
- Update configuration management baseline
- Implement controls to prevent recurrence

**Eradication Verification**:
- Confirm root cause eliminated through testing
- Verify no signs of threat actor presence
- Obtain approval from Incident Response Manager before proceeding to recovery

**Phase 3: Recovery**

**Objective**: Restore affected systems and services to normal operations, verifying systems are functioning properly and threat is eliminated.

**Recovery Actions**:

**System Restoration**:
- Restore systems from clean backups (verified pre-incident) OR rebuild from known good baseline
- Apply all security patches and updates
- Reconfigure systems per security baseline
- Restore data from clean backups (if applicable)
- Verify system integrity before returning to production

**Service Restoration Priority**:
- Restore services per business criticality (align with BC/DR priorities, A.5.29-30)
- Coordinate with IT operations for service dependencies
- Phased restoration for complex systems (pilot → full production)

**Verification Before Production**:
- Security scan of restored systems (vulnerability assessment)
- Integrity verification (file integrity monitoring, clean bill of health from AV/EDR)
- Functionality testing (basic operational testing)
- Enhanced monitoring for 72 hours post-restoration

**User Communication**:
- Notify users of service restoration
- Provide guidance on verification (how to confirm service is working properly)
- Remind users of security best practices
- Hotline or support for questions

**Incident Closure Criteria**:

Incident may be closed when ALL of:
- Threat completely contained and eradicated (verified)
- All affected systems restored to normal operation
- Enhanced monitoring in place and no signs of reinfection
- Evidence collected and preserved (A.5.28)
- Initial lessons learned documented
- Incident Response Manager approves closure

**Note**: Incident closure does NOT mean end of all activities. Post-Incident Review (A.5.27) occurs after closure.

#### 2.3.2 Communication Requirements

**Internal Communication**:

**Incident Response Team Communication**:
- Dedicated secure communication channel (encrypted chat, conference bridge)
- Real-time updates during active response
- Status updates minimum every 4 hours for Critical incidents, every 8 hours for High
- All decisions and actions logged in incident management system

**Management Communication**:

**Critical Incidents**:
- Initial notification to Executive Management within 1 hour
- Status updates every 4 hours (or as requested by management)
- Executive Management briefing prepared for each status update
- Final incident summary within 24 hours of closure

**High Incidents**:
- CISO notification within 2 hours
- Daily status updates to CISO and relevant department heads
- Executive summary within 48 hours of closure

**Medium/Low Incidents**:
- Weekly summary report to CISO
- Escalation to management only if becomes High severity

**User Communication**:

[Organization] MUST communicate with affected users when:
- Service is disrupted or degraded
- User action required (password reset, account verification)
- User data potentially compromised
- Phishing campaign targeting users

**User Communication Requirements**:
- Clear, non-technical language
- Specific actions required (if any)
- Timeline for resolution
- Support resources available
- Communications team involvement for widespread incidents

**External Communication**:

**Regulatory Authorities**:
- Breach notification per regulatory requirements (GDPR 72 hours, etc.)
- Legal team + DPO coordinate notification
- Use templates from ISMS-REF-A.5.24-28 Section 2
- Documentation of notification (when sent, to whom, content)

**Customers/Partners**:
- Executive Management approval required
- Communications team drafts customer communication
- Legal review of communication content
- Notification when customer data affected or service SLA violated
- Transparency about incident scope, impact, remediation

**Law Enforcement**:
- CISO decision, Executive Management approval
- Legal counsel involved in reporting decision
- Cooperation with investigation
- Limitations on information sharing (protect [Organization] legal position)

**Media/Public**:
- Executive Management ONLY authorized to speak to media
- Communications team prepares statements
- Legal review of all public statements
- No speculation about attackers or motives

**Third Parties**:
- Notify third parties if their services or data involved
- Coordinate response for shared responsibility incidents (cloud services)
- Contractual notification requirements per agreements

**Communication OPSEC** (Operational Security):
- Avoid disclosing technical details that could aid attackers
- Avoid disclosing incomplete or speculative information
- Use secure channels for sensitive communications
- Limit communication to need-to-know basis during active response

#### 2.3.3 Response Coordination

**Roles During Response** (detailed RACI in ISMS-IMP-A.5.24-28.S3):

**Incident Commander** (Incident Response Manager or designee):
- Overall incident coordination
- Decision-making authority for response actions
- Communication with management
- Resource allocation

**Technical Lead** (Senior Incident Handler):
- Technical investigation and analysis
- Coordinate containment/eradication/recovery actions
- Interface with IT operations, system administrators, cloud providers
- Technical documentation

**Communications Lead** (Communications Coordinator):
- Internal and external communications
- Message consistency
- Stakeholder management

**Forensic Lead** (Forensic Specialist):
- Evidence collection coordination (A.5.28)
- Chain of custody management
- Forensic analysis

**Legal Liaison** (Legal team representative):
- Legal implications assessment
- Regulatory notification coordination
- Law enforcement interface
- Privilege and confidentiality protection

**Business Liaison** (Department representative):
- Business impact assessment
- Service restoration priorities
- User communication
- Business process continuity

**Coordination Mechanisms**:
- Incident response bridge (conference call) for Critical incidents (24/7 until contained)
- Dedicated chat channel for all incidents
- Status page for internal tracking
- Incident management system for documentation and workflow

#### 2.3.4 Service Restoration & Business Continuity Integration

**BC/DR Activation Decision**:

Incident Response Manager MUST assess if incident triggers BC/DR procedures (A.5.29-30):

**BC/DR Activation Criteria**:
- Critical services unavailable for >1 hour
- Data center unavailable or inaccessible
- Ransomware affecting production systems requiring failover
- Disaster declared by Executive Management

**BC/DR Coordination**:
- Incident Response Manager coordinates with BC/DR Coordinator
- Incident response continues in parallel with BC/DR activation
- Forensic evidence preserved even during BC/DR activities
- Joint decision on service restoration approach (restore from backup vs. failover)

**Service Restoration Priorities**:

Based on Business Impact Analysis (BIA) from BC/DR framework:
1. **Tier 1 - Critical Services** (RTO ≤4 hours): Restore first
2. **Tier 2 - Important Services** (RTO ≤24 hours): Restore second
3. **Tier 3 - Normal Services** (RTO ≤7 days): Restore third

**Coordinated Recovery**:
- Incident eradication MUST be complete before restoration
- Do not restore to compromised environment (verify environment clean first)
- Phased restoration to detect potential reinfection early

### 2.4 Forensic Evidence Collection & Preservation (A.5.28)

[Organization] SHALL establish and implement procedures for forensic evidence identification, collection, acquisition, and preservation to support incident response, legal proceedings, regulatory investigations, and root cause analysis.

#### 2.4.1 When to Collect Evidence

Evidence collection MUST occur for:

**Mandatory Evidence Collection**:
- **Critical severity** incidents (all)
- **High severity** incidents with potential legal or regulatory implications
- Incidents involving criminal activity (fraud, theft, sabotage)
- Insider threat incidents
- Data breaches triggering breach notification
- Incidents where law enforcement may be involved
- Incidents potentially covered by cyber insurance claims

**Optional Evidence Collection**:
- **Medium severity** incidents (based on Incident Response Manager decision)
- **Low severity** incidents if pattern/trend requires investigation

**Evidence Collection Timing**:
- Evidence collection begins **immediately upon incident detection**
- Runs **parallel to response operations** (A.5.26), NOT after incident closure
- Forensic Lead coordinates with Incident Commander to avoid evidence loss during containment

**Exception**: If evidence collection delays Critical containment actions (active ransomware encryption), containment takes priority. Document why evidence not collected.

#### 2.4.2 Evidence Types & Collection Procedures

**Digital Evidence Categories**:

**System Evidence**:
- Disk images (full forensic images of affected systems)
- Memory dumps (capture of system RAM)
- Configuration files (system settings, application configs)
- System logs (OS logs, application logs, security logs)

**Network Evidence**:
- Network traffic captures (PCAP files)
- Firewall logs
- IDS/IPS alerts and logs
- Proxy logs
- DNS query logs

**Cloud Evidence**:
- Cloud service provider logs (AWS CloudTrail, Azure Activity Log, GCP Audit Logs)
- Cloud resource snapshots (EBS snapshots, Azure disk snapshots)
- Cloud configuration exports
- SaaS application logs

**Application Evidence**:
- Application logs
- Database logs and audit trails
- Web server logs
- Email headers and content (for phishing incidents)

**User Evidence**:
- User account logs
- Authentication logs
- Access logs
- User activity logs

**Collection Procedures**:

[Organization] MUST use forensically sound methods:
- **Read-only access** to evidence sources where possible
- **Cryptographic hashing** (SHA-256 minimum) of all collected evidence
- **Timestamps** recorded in UTC
- **Write blockers** used for physical media
- **Forensic tools** (validated and tested) used for collection

**Collection Documentation**:
- Who collected evidence
- When evidence collected (date/time UTC)
- Where evidence collected from (system name, IP, location)
- How evidence collected (tool, method)
- Why evidence collected (incident relation)

**Technical Guidance**: ISMS-REF-A.5.24-28 Section 3 (Forensic Collection Techniques Library) provides detailed technical procedures for evidence collection per evidence type.

#### 2.4.3 Chain of Custody

**Chain of Custody Requirements**:

All evidence MUST have documented chain of custody from collection through disposal:

**Required Documentation** (for EACH evidence item):
- **Evidence ID**: Unique identifier
- **Description**: What evidence is (disk image of Server-XYZ, memory dump of Workstation-123)
- **Collection Information**: Who, when, where, how, why (as above)
- **Custody Transfer Log**: Every person who had access to evidence
  - Transfer date/time
  - Transferring party (name, signature)
  - Receiving party (name, signature)
  - Reason for transfer
  - Storage location
- **Storage Information**: Where evidence stored, security controls, access restrictions
- **Disposal Information**: When/how evidence disposed (when retention period expires)

**Chain of Custody Integrity**:
- Minimize transfers (limit access to evidence)
- Evidence sealed or access-logged between transfers
- Cryptographic hash verified before and after transfers (ensure integrity)
- Break in chain of custody documented with explanation

**Legal Admissibility**:
- Chain of custody documentation sufficient for legal proceedings
- Evidence handling procedures meet forensic standards
- External forensic experts may be engaged for high-stakes incidents

#### 2.4.4 Evidence Preservation & Storage

**Evidence Storage Requirements**:

**Physical Security**:
- Evidence stored in secure, access-controlled location
- Access limited to Forensic Lead and designated personnel
- Access logged (who accessed, when, purpose)

**Logical Security**:
- Evidence files encrypted at rest (AES-256 minimum)
- Evidence files stored on separate system (not on production infrastructure)
- Evidence files backed up (protect against loss)
- Integrity verification through cryptographic hashing

**Retention Requirements**:

**Retention Periods**:
- **Incident evidence**: Retained per [Organization] records retention policy (minimum 1 year from incident closure)
- **Legal hold**: Retained indefinitely until legal hold lifted
- **Regulatory requirement**: Retained per regulatory requirement (may exceed 1 year)
- **Insurance claim**: Retained until claim resolved
- **No requirement**: Deleted per retention schedule

**Disposal Procedure**:
- Evidence securely deleted (per A.8.10 requirements) when retention period expires
- Chain of custody documentation retained even after evidence disposal
- Disposal logged and approved by CISO or Incident Response Manager

#### 2.4.5 Legal Hold Procedures

**Legal Hold Triggers**:

Legal hold MUST be implemented when:
- Litigation commenced or reasonably anticipated
- Regulatory investigation commenced
- Law enforcement requests evidence preservation
- Cyber insurance claim investigation
- Internal investigation with potential disciplinary or legal action

**Legal Hold Process**:

1. **Initiation**: Legal Counsel issues legal hold notice
2. **Identification**: Identify all evidence sources potentially relevant (systems, users, data)
3. **Preservation**: Suspend normal deletion/destruction processes for held evidence
4. **Notification**: Notify IT operations, system administrators, affected personnel of hold
5. **Segregation**: Segregate held evidence from normal operations (separate storage)
6. **Duration**: Legal hold remains until Legal Counsel issues release notice
7. **Release**: Normal retention policies resume after release

**Legal Hold Documentation**:
- Legal hold notice (what evidence, why, duration)
- Evidence sources identified
- Personnel notified
- Preservation actions taken
- Release documentation

**Integration with Incident Management**:
- Incident evidence automatically subject to 1-year minimum retention
- Legal Counsel assesses if legal hold required beyond normal retention
- Evidence not destroyed while legal hold pending

#### 2.4.6 External Forensic Support

[Organization] MAY engage external forensic expertise for:
- Complex incidents requiring specialized skills (APT, nation-state)
- Incidents with significant legal implications
- Incidents where [Organization] lacks internal forensic capability
- Cyber insurance requirements for claims
- Regulatory requirements for independent investigation

**External Forensic Engagement**:
- Pre-vetted forensic firms (retainer or on-demand)
- Contractual agreements including confidentiality, evidence handling, reporting
- Coordination between internal incident response and external forensic team
- Evidence handoff with chain of custody maintained

### 2.5 Post-Incident Learning & Improvement (A.5.27)

[Organization] SHALL systematically extract lessons from incidents and translate findings into tangible control improvements, ensuring the organization becomes more resilient with each incident.

#### 2.5.1 Post-Incident Review (PIR) Requirements

**PIR Mandate**:

Post-Incident Review MUST be conducted for:
- **All Critical incidents** (within 5 business days of incident closure)
- **All High incidents** (within 10 business days of incident closure)
- **Medium incidents** meeting criteria:
  - Novel attack technique or threat actor
  - Significant control failure revealed
  - Multiple similar incidents (pattern)
  - Incident Response Manager determination

**PIR Participants** (minimum):
- Incident Response Manager (facilitator)
- Incident Commander from response
- Technical personnel who handled incident
- Representatives from affected business units
- IT operations representatives
- CISO or designee

**PIR Agenda** (structured format):

1. **Incident Timeline Review** (factual reconstruction):
   - When incident occurred (initial compromise)
   - When incident detected (detection method)
   - When incident responded to (initial response action)
   - Key milestones in containment, eradication, recovery
   - When incident closed

2. **Detection Assessment**:
   - How was incident detected? (monitoring alert, user report, external notification)
   - Time to detect (MTTD) - could we have detected earlier?
   - Gaps in monitoring or alerting revealed?

3. **Response Effectiveness Assessment**:
   - Were procedures followed?
   - Were procedures adequate?
   - Were response times within SLA?
   - Communication effectiveness (internal, external)
   - Coordination effectiveness

4. **Technical Analysis**:
   - Root cause identification (what vulnerability or weakness allowed incident)
   - Attack vector and techniques used
   - Effectiveness of existing controls (what worked, what didn't)

5. **Impact Assessment**:
   - Business impact (downtime, data loss, revenue impact)
   - Financial impact (response costs, recovery costs, potential liabilities)
   - Reputation impact

6. **Lessons Learned**:
   - What went well (successes to replicate)
   - What could be improved (gaps to address)
   - Specific recommendations for improvement

**PIR Documentation**:

PIR MUST produce written report containing:
- Executive summary (1 page for management)
- Incident timeline
- Assessment findings (detection, response, technical, impact)
- Lessons learned
- Improvement recommendations (prioritized)
- Action items with owners and deadlines

**PIR Distribution**:
- CISO (required)
- Executive Management (for Critical incidents)
- Incident Response Team (all)
- IT Operations (relevant sections)
- Affected business units (relevant sections)
- Stored in incident management system

**No Blame Culture**:
- PIR focus on process and control improvement, NOT individual blame
- Honest assessment requires psychological safety
- Disciplinary actions (if needed) handled separately through HR, not during PIR

#### 2.5.2 Root Cause Analysis

[Organization] MUST identify root cause(s) for incidents to enable preventive measures.

**Root Cause vs. Proximate Cause**:
- **Proximate Cause**: Immediate trigger (user clicked phishing link, unpatched vulnerability exploited)
- **Root Cause**: Underlying systemic issue (inadequate security awareness training, patch management process failure)

**Root Cause Analysis Methods**:

**5 Whys Technique**:
- Ask "Why?" five times to drill down from symptom to root cause
- Example:
  1. Why was server compromised? → Unpatched vulnerability
  2. Why was vulnerability unpatched? → Patch not applied
  3. Why was patch not applied? → Patch not tested
  4. Why was patch not tested? → No test environment for this system
  5. Why no test environment? → System not in patch management scope

**Root Cause**: System not properly included in patch management program (process failure)

**Fishbone Diagram** (Ishikawa):
- Organize potential causes into categories: People, Process, Technology, Environment
- Identify contributing factors across categories
- Determine which are root causes vs. contributing factors

**Fault Tree Analysis**:
- Logical diagram showing combinations of events leading to incident
- Useful for complex incidents with multiple contributing factors

**Root Cause Documentation**:
- Root cause(s) identified and documented in PIR
- Distinction between root cause and contributing factors
- Validation that addressing root cause would have prevented incident

#### 2.5.3 Control Improvement Process

**From Lessons Learned to Action**:

PIR recommendations MUST be translated into actionable improvements:

**Improvement Categories**:

**Policy/Process Improvements**:
- Update incident response procedures
- Update security policies
- Enhance user training and awareness
- Improve vendor management processes

**Technical Improvements**:
- Implement new security controls
- Enhance monitoring and detection capabilities
- Patch vulnerable systems or applications
- Improve configuration management

**Organizational Improvements**:
- Increase incident response staffing or training
- Reorganize responsibilities
- Enhance communication procedures
- Improve coordination with external parties

**Improvement Prioritization**:

Recommendations prioritized by:
1. **High Priority** (implement within 30 days):
   - Address critical control failures
   - Prevent recurrence of Critical/High severity incidents
   - Address regulatory compliance gaps
2. **Medium Priority** (implement within 90 days):
   - Enhance detection or response capabilities
   - Address Medium severity incident lessons
3. **Low Priority** (implement within 180 days):
   - Process optimizations
   - Nice-to-have enhancements

**Action Tracking**:

All improvement actions MUST be:
- Assigned to specific owner (not "team" - individual accountability)
- Given target completion date
- Tracked in [Organization] project management or ticketing system
- Reviewed at least monthly by CISO or Incident Response Manager
- Closed only when implemented and verified

**Improvement Verification**:
- Implementation verified by action owner
- Effectiveness assessed through testing (tabletop exercise, technical test)
- Reviewed in next PIR if similar incident occurs

**Integration with ISMS**:

Incident-driven improvements feed into:
- **Risk Assessment** (A.5.1): New risks identified, risk ratings updated
- **Control Implementation**: New controls implemented, existing controls enhanced
- **Policy Updates**: Policies revised based on lessons learned
- **Training**: Training content updated based on user-related incidents
- **Monitoring**: New alerts or detection rules implemented

#### 2.5.4 Knowledge Management

**Lessons Learned Repository**:

[Organization] MUST maintain organizational knowledge base:

**Knowledge Base Contents**:
- PIR reports (all completed PIRs)
- Incident summaries (sanitized for broader distribution)
- Response playbooks (updated with lessons learned)
- Attack techniques observed (tactics, techniques, procedures)
- Effective response actions (what worked well)
- Pitfalls to avoid (what didn't work)

**Knowledge Base Access**:
- Incident response team: Full access
- IT operations: Relevant technical content
- Management: Executive summaries
- General employees: Sanitized case studies for awareness

**Playbook Updates**:

Incident response playbooks MUST be updated based on lessons learned:
- Add new incident types if novel attack observed
- Enhance existing playbooks with effective techniques
- Remove ineffective procedures
- Add decision trees for common scenarios
- Include lessons learned annotations ("watch out for...", "don't forget to...")

**Trend Analysis & Metrics**:

[Organization] MUST track incident metrics over time:

**Incident Volume Metrics**:
- Total incidents per month/quarter
- Incidents by severity
- Incidents by category
- Repeat incidents (same root cause)

**Incident Response Performance Metrics**:
- Mean Time to Detect (MTTD)
- Mean Time to Respond (MTTR)
- Mean Time to Contain (MTTC)
- Mean Time to Recover
- False positive rate
- Escalation rate

**Control Effectiveness Metrics**:
- Detection rate (incidents detected by monitoring vs. external notification)
- SLA compliance rate (incidents meeting response SLA)
- PIR completion rate
- Improvement action completion rate

**Trend Identification**:
- Quarterly metrics review by CISO and Incident Response Manager
- Identification of trends (improving, worsening, static)
- Root cause analysis of negative trends
- Action plans to address concerning trends

**Metrics Reporting**:
- Incident metrics reported to Executive Management quarterly
- Trends and improvement actions highlighted
- Comparison to industry benchmarks (where available)

#### 2.5.5 Continuous Improvement Framework

**Improvement Cycle**:

Incident management operates on continuous improvement cycle:

```
    INCIDENT → RESPONSE → PIR → IMPROVEMENTS → TESTING
         ↑                                           ↓
         └───────────── ENHANCED CAPABILITY ←────────┘
```

**Annual Program Review**:

Incident Response Manager MUST conduct annual review of entire incident management program:
- Review year's incidents (volume, severity, categories)
- Assess program effectiveness (metrics trends)
- Identify systemic issues (recurring problems)
- Benchmark against industry standards
- Update incident management strategy
- Update procedures and playbooks
- Adjust training programs
- Update tools and technology roadmap

**Annual Review Deliverable**:
- Incident Management Annual Report to CISO and Executive Management
- Program maturity assessment
- Recommendations for next year
- Budget requirements for improvements

**Maturity Assessment**:

[Organization] SHALL assess incident management maturity using industry frameworks:
- NIST Cybersecurity Framework maturity tiers
- ISO/IEC 27035 maturity model
- CMMI for incident management
- Internal assessment against ISMS-IMP-A.5.24-28 assessment frameworks

**Maturity Goals**:
- Year 1: Establish basic incident management capability (Tier 2 - Repeatable)
- Year 2: Optimize and automate (Tier 3 - Defined)
- Year 3: Mature and measure (Tier 4 - Managed)
- Long-term: Industry-leading (Tier 5 - Optimizing)

---

## 3. Governance & Exception Management

### 3.1 Roles & Responsibilities

**Executive Management**:
- **Accountable**: Overall incident management program effectiveness
- **Responsible**: Approve incident management policy and major procedure changes
- **Consulted**: Critical incident decisions (service shutdown, public disclosure, law enforcement)
- **Informed**: Critical incident status updates, High incident summaries, quarterly metrics

**Chief Information Security Officer (CISO)**:
- **Accountable**: Incident management policy compliance, program maturity
- **Responsible**: Approve procedures, accept residual risk, budget allocation, resource assignment
- **Consulted**: High/Critical incident response decisions, escalations, external engagement
- **Informed**: All incident reports, PIR reports, metrics

**Incident Response Manager / CSIRT Lead**:
- **Accountable**: Day-to-day incident response operations, SLA compliance, PIR completion
- **Responsible**: Incident assessment, response coordination, resource allocation, communications, training
- **Consulted**: Technical response decisions, tool selection
- **Informed**: All incidents real-time

**Incident Handlers / SOC Analysts**:
- **Accountable**: Individual incident handling per assignment
- **Responsible**: Incident triage, investigation, containment, eradication, recovery execution, documentation
- **Consulted**: Technical approach, evidence collection
- **Informed**: Incident assignments, procedure updates

**Forensic Specialists**:
- **Accountable**: Evidence collection integrity, chain of custody
- **Responsible**: Forensic analysis, evidence preservation, legal liaison for evidence matters
- **Consulted**: Evidence admissibility, forensic tool selection
- **Informed**: Incidents requiring forensic collection

**IT Operations**:
- **Accountable**: System availability and restoration
- **Responsible**: Execute containment/eradication/recovery actions on systems
- **Consulted**: Service restoration priorities, technical feasibility
- **Informed**: Incidents affecting their systems

**Legal Counsel**:
- **Accountable**: Legal risk mitigation, regulatory compliance
- **Responsible**: Legal advice, regulatory notification, law enforcement liaison, legal hold
- **Consulted**: Incidents with legal implications, communications
- **Informed**: All High/Critical incidents, data breaches

**Data Protection Officer (DPO)**:
- **Accountable**: Privacy compliance, breach notification
- **Responsible**: Breach assessment per GDPR/nDSG, notification coordination
- **Consulted**: Incidents involving personal data
- **Informed**: All incidents involving personal data

**Communications Team**:
- **Accountable**: External communications, reputation management
- **Responsible**: Draft user, customer, media communications
- **Consulted**: High/Critical incident communications, regulatory notifications
- **Informed**: Incidents requiring external communication

**Human Resources**:
- **Accountable**: Employee-related incidents (insider threats)
- **Responsible**: Employee investigations, disciplinary actions, employee communications
- **Consulted**: Insider threat incidents, compromised employee accounts
- **Informed**: Incidents involving employees

**Business Unit Representatives**:
- **Accountable**: Business impact assessment, business continuity
- **Responsible**: Business process restoration, user communication
- **Consulted**: Service restoration priorities, business impact
- **Informed**: Incidents affecting their business unit

**All Personnel**:
- **Responsible**: Report suspected security incidents per A.6.8
- **Consulted**: N/A
- **Informed**: Security awareness communications

### 3.2 Incident Severity & Response SLA Matrix

**SLA Definitions**:

| Severity | Detection to Assessment | Assessment to Response Initiation | Containment Target | Recovery Target | Executive Notification | PIR Required |
|----------|------------------------|----------------------------------|-------------------|-----------------|----------------------|--------------|
| **Critical** | 15 minutes | 15 minutes | 1 hour | 4 hours | Within 1 hour | Yes (within 5 business days) |
| **High** | 1 hour | 1 hour | 4 hours | 24 hours | Within 2 hours | Yes (within 10 business days) |
| **Medium** | 4 hours | 4 hours | 24 hours | 5 business days | If escalated | Conditional |
| **Low** | 8 hours (next business day acceptable) | 8 hours | 5 business days | 10 business days | No | No |

**SLA Measurement**:
- SLA measured from incident detection timestamp to completion of phase
- SLA violations tracked as metrics
- SLA violations for Critical/High incidents require explanation
- Chronic SLA violations indicate resource or process issues requiring escalation to CISO

**SLA Exceptions**:
- Complex incidents may require SLA extensions (Incident Response Manager approval)
- Resource constraints may impact SLA (documented)
- SLA targets are goals, not guarantees (best-effort basis)

**After-Hours Coverage**:

**Critical/High Incidents**:
- 24/7 on-call coverage required
- On-call personnel must respond within 30 minutes
- Escalation if on-call does not respond within 30 minutes

**Medium/Low Incidents**:
- Business hours coverage (Monday-Friday, [Organization] business hours)
- After-hours incidents queued for next business day

### 3.3 Communication & Reporting Requirements

**Incident Status Reports**:

**Critical Incidents**:
- Initial notification: Within 1 hour (Executive Management, CISO)
- Status updates: Every 4 hours during active response
- Final report: Within 24 hours of closure
- PIR: Within 5 business days

**High Incidents**:
- Initial notification: Within 2 hours (CISO, Incident Response Manager)
- Status updates: Daily during active response
- Final report: Within 48 hours of closure
- PIR: Within 10 business days

**Medium/Low Incidents**:
- Weekly summary to CISO
- Final report: Included in weekly summary
- PIR: Conditional

**Report Content**:
- Incident summary (severity, category, affected systems)
- Timeline (detection, response, containment, eradication, recovery)
- Business impact
- Response actions taken
- Current status
- Next steps

**Executive Reporting**:

**Quarterly Incident Summary** (to Executive Management):
- Total incidents by severity
- Incident categories and trends
- MTTD, MTTR, MTTC metrics
- SLA compliance
- PIR completion rate
- Top 5 lessons learned
- Program improvements implemented
- Budget and resource needs

**Annual Incident Report** (to Board/Executive Management):
- Year-over-year trends
- Program maturity assessment
- Benchmark comparison (industry)
- Major incidents summary
- Control improvements implemented
- Regulatory compliance status
- Strategic recommendations

### 3.4 Exception Management

**Exception Policy**:

Exceptions to this incident management policy are **rare** and require:
- Written exception request with business justification
- Risk assessment of exception (what risk is accepted)
- Compensating controls (if applicable)
- CISO approval (minimum)
- Executive Management approval (for Critical control exceptions)
- Time-bound (maximum 12 months, renewal required)

**Examples of Exceptions**:
- Excluding specific system from incident response scope (due to legacy constraints)
- Extended SLA for specific incident type (due to complexity or resource limitations)
- Alternative evidence collection method (due to technical constraints)
- Exemption from PIR requirement for specific incident category

**Exception Documentation**:
- Exception request form
- Risk assessment
- Approval signatures
- Review date
- Stored in ISMS exception register

**Exception Review**:
- All exceptions reviewed annually
- Renewal requires re-justification
- Expired exceptions revoked automatically

### 3.5 Incident Management Metrics & KPIs

[Organization] SHALL track the following Key Performance Indicators (KPIs):

**Volume Metrics**:
- Total incidents per month/quarter/year
- Incidents by severity (Critical, High, Medium, Low)
- Incidents by category (malware, unauthorized access, etc.)
- Repeat incidents (same root cause)

**Performance Metrics**:
- Mean Time to Detect (MTTD): Average time from incident occurrence to detection
- Mean Time to Respond (MTTR): Average time from detection to initial response
- Mean Time to Contain (MTTC): Average time from detection to containment
- Mean Time to Recover: Average time from detection to full recovery
- SLA Compliance Rate: % of incidents meeting SLA targets

**Quality Metrics**:
- False Positive Rate: % of alerts that are false positives
- Detection Source Distribution: % detected by monitoring vs. user report vs. external
- Severity Classification Accuracy: % of incidents where initial severity was correct
- PIR Completion Rate: % of required PIRs completed on time

**Improvement Metrics**:
- Lessons Learned Actions Completed: % of improvement actions completed on time
- Procedure Update Frequency: Number of procedure updates from lessons learned
- Training Effectiveness: Incident volume/severity trends after training

**Benchmark Targets** (industry average):
- MTTD: <24 hours (target: <8 hours)
- MTTR: <1 hour (target: <30 minutes for Critical)
- MTTC: <24 hours (target: <4 hours for Critical)
- False Positive Rate: <5% (target: <2%)
- SLA Compliance: >90% (target: >95%)

**Metrics Reporting**:
- Monthly: Incident Response Manager reviews metrics, identifies trends
- Quarterly: CISO reviews metrics, reports to Executive Management
- Annually: Board-level reporting, benchmark comparison

### 3.6 Policy Governance & Review

**Policy Review**:
- **Frequency**: Annual minimum
- **Triggers**: Major incident revealing policy gap, regulatory changes, organizational changes, significant threat landscape changes, audit findings, maturity evolution
- **Reviewers**: CISO (owner), Incident Response Manager (contributor), Legal (compliance), IT Operations (operational feasibility)
- **Approval**: CISO (technical), Executive Management (strategic)

**Implementation Standards Review**:
- **Frequency**: Based on threat landscape evolution and lessons learned (at least semi-annual)
- **Authority**: Incident Response Manager proposes updates, CISO approves
- **Note**: Implementation standard updates (ISMS-IMP-A.5.24-28) do not require policy revision

**Reference Document Review**:
- **ISMS-REF-A.5.24-28 Review**: Quarterly minimum (incident taxonomy, regulatory requirements, forensic techniques)
- **Authority**: Incident Response Manager maintains, CISO reviews annually
- **Note**: Reference document updates do not require policy revision

**Policy Updates**:
- **Minor** (clarifications, references, formatting): CISO approval, communication within 30 days
- **Major** (scope changes, new requirements, SLA changes): Full approval chain, implementation timeline per change management
- **Emergency** (critical regulatory change, major incident lessons learned requiring immediate policy change): CISO approval, immediate communication and implementation

**Communication**: Policy published in ISMS document repository. Changes communicated organization-wide via email, security awareness platform, and training for significant changes affecting user responsibilities or procedures.

**Training Impact**: Policy changes triggering new training requirements MUST be incorporated into training within 90 days of policy approval.

---

## 4. Implementation & References

### 4.1 Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**ISO/IEC 27001:2022 Clause 6.1 - Risk Assessment**:

Incident management controls implemented based on [Organization]'s risk assessment:
- Incident management capability risks (inability to respond effectively) identified and assessed
- Incident types and severities anticipated based on threat and vulnerability assessment
- Risk treatment decisions document incident management controls implemented and to what level
- Residual risks (accepted gaps in incident response capability) documented

**ISO/IEC 27001:2022 Clause 6.1.3 - Statement of Applicability**:

This policy supports the following SoA entries:

| Control | Status | Justification | Implementation |
|---------|--------|---------------|----------------|
| **A.5.24 - Planning & Preparation** | ☑ Applicable | [Organization] requires incident management capabilities to detect and respond to security incidents | Section 2.1, ISMS-IMP-A.5.24-28.S1 |
| **A.5.25 - Assessment & Decision** | ☑ Applicable | [Organization] requires systematic event assessment to identify incidents requiring response | Section 2.2, ISMS-IMP-A.5.24-28.S2 |
| **A.5.26 - Response** | ☑ Applicable | [Organization] requires documented incident response procedures to minimize incident impact | Section 2.3, ISMS-IMP-A.5.24-28.S3 |
| **A.5.27 - Learning** | ☑ Applicable | [Organization] requires continuous improvement of security controls based on incident experience | Section 2.5, ISMS-IMP-A.5.24-28.S5 |
| **A.5.28 - Evidence Collection** | ☑ Applicable | [Organization] requires forensic evidence capabilities for legal, regulatory, and investigative purposes | Section 2.4, ISMS-IMP-A.5.24-28.S4 |

**Related Controls** (integration points):

**A.8.15 - Logging**:
- Comprehensive logs required for incident investigation
- Log retention supports forensic analysis and regulatory requirements
- Incident response team has access to centralized logs
- Integration: Logging infrastructure provides evidence for incident investigation per A.8.15 requirements

**A.8.16 - Monitoring Activities**:
- Monitoring infrastructure detects security events
- Alerts feed incident assessment process (A.5.25)
- SIEM provides real-time visibility into security posture
- Integration: Monitoring capabilities enable incident detection per A.8.16 requirements

**A.6.8 - Information Security Event Reporting**:
- User reporting mechanism feeds event assessment
- All personnel trained on incident reporting
- Reporting channels monitored by incident response team
- Integration: User reports assessed per this policy Section 2.2

**A.5.29-30 - Business Continuity & Disaster Recovery**:
- Major incidents may trigger BC/DR activation
- Incident severity assessment considers business continuity impact
- BC/DR procedures coordinate with incident response for major incidents
- Integration: BC/DR integration per this policy Section 2.3.4

**A.5.31 - Legal, Statutory, Regulatory Requirements**:
- Incident response incorporates regulatory breach notification requirements
- Legal team engaged for incidents with legal implications
- Regulatory compliance tracked through incident management
- Integration: Regulatory requirements per ISMS-POL-00, operational execution per this policy Section 1.6

**A.5.19-23 - Third-Party Management**:
- Third-party security incidents reported to [Organization] per contracts
- Third-party vendors cooperate with incident response
- Supplier contracts include incident notification requirements
- Integration: Third-party incident handling per supplier agreements, assessed per A.5.22

**A.8.9 - Configuration Management**:
- Configuration baselines support incident recovery
- Configuration changes tracked for incident investigation
- Known-good configurations used for system restoration
- Integration: Configuration management data used in recovery per this policy Section 2.3.1 Phase 3

**A.5.9 - Inventory of Information and Assets**:
- Asset inventory identifies systems requiring incident response capability
- Asset criticality classification drives incident severity and response priorities
- Changes to asset inventory trigger incident response capability review
- Integration: Asset inventory provides context for incident impact assessment

**A.5.15-18 - Identity & Access Management**:
- Compromised accounts revoked per incident response procedures
- Access logs provide evidence for unauthorized access investigations
- Account provisioning/deprovisioning integrated with incident response (revoke access)
- Integration: IAM capabilities support incident response per this policy Section 2.3.1 Phase 2

### 4.2 Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.5.24-28):

| Document | Purpose | Scope |
|----------|---------|-------|
| **ISMS-IMP-A.5.24-28.S1** | Incident Management Framework Assessment | Governance assessment: CSIRT/SOC structure, roles, procedures, training, tools. Evaluates planning & preparation maturity (A.5.24 focus). Part I: User Guide (~50 pages). Part II: Technical Spec (~40 pages). |
| **ISMS-IMP-A.5.24-28.S2** | Event Detection & Classification Assessment | Event assessment effectiveness: Event vs. incident accuracy, severity determination, categorization, triage, false positives, escalation (A.5.25 focus). Part I: User Guide (~45 pages). Part II: Technical Spec (~40 pages). |
| **ISMS-IMP-A.5.24-28.S3** | Incident Response Capabilities Assessment | Response operations effectiveness: Playbook coverage, containment/eradication/recovery procedures, SLA compliance, communications, escalation, service restoration (A.5.26 focus). Part I: User Guide (~50 pages). Part II: Technical Spec (~45 pages). |
| **ISMS-IMP-A.5.24-28.S4** | Forensic Evidence Management Assessment | Evidence collection maturity: Forensic procedures, chain of custody, evidence tools, preservation, storage, legal hold, integration with legal/law enforcement (A.5.28 focus). Part I: User Guide (~45 pages). Part II: Technical Spec (~40 pages). |
| **ISMS-IMP-A.5.24-28.S5** | Learning & Continuous Improvement Assessment | Learning effectiveness: PIR completion, root cause analysis quality, lessons learned documentation, improvement tracking, knowledge management, metrics (A.5.27 focus). Part I: User Guide (~40 pages). Part II: Technical Spec (~35 pages). |

**Reference Materials** (ISMS-REF-A.5.24-28):

| Section | Purpose | Content |
|---------|---------|---------|
| **Section 1: Incident Classification Taxonomy** | Provide detailed incident categorization structure | Primary categories (10+), subcategories (50+ total), examples, severity indicators, MITRE ATT&CK mapping (~200 lines) |
| **Section 2: Regulatory Notification Quick Reference** | Operational guidance for regulatory breach notifications | GDPR notification procedures, Swiss nDSG procedures, PCI DSS reporting, sector-specific requirements, templates, contacts, quick reference table (~150 lines) |
| **Section 3: Forensic Collection Techniques Library** | Technical guidance for evidence collection | Disk imaging methods, memory capture, log preservation, network traffic capture, chain of custody templates, evidence storage, tool comparison (~200 lines) |

### 4.3 Technical Standards & Frameworks

**Industry Standards Referenced**:

**Incident Response Frameworks**:
- **NIST SP 800-61 Rev. 2**: Computer Security Incident Handling Guide (preparation, detection, analysis, containment, eradication, recovery, post-incident)
- **ISO/IEC 27035**: Information Security Incident Management (incident management lifecycle, organizational structure, response)
- **SANS Incident Handler's Handbook**: Practical incident response methodology

**Threat Intelligence Frameworks**:
- **MITRE ATT&CK**: Adversary tactics, techniques, and procedures (TTPs)
- **MITRE D3FEND**: Defensive countermeasures knowledge graph
- **Cyber Kill Chain**: Lockheed Martin attack lifecycle model

**Forensic Standards**:
- **ISO/IEC 27037**: Guidelines for identification, collection, acquisition, and preservation of digital evidence
- **NIST SP 800-86**: Guide to Integrating Forensic Techniques into Incident Response
- **RFC 3227**: Guidelines for Evidence Collection and Archiving

**Compliance Frameworks**:
- **GDPR**: Breach notification requirements (Art. 33-34)
- **Swiss nDSG**: Breach notification (Art. 24)
- **PCI DSS v4.0**: Incident response requirements (Req. 12.10)

**Note**: Industry standards provide guidance and best practices. [Organization] adapts frameworks to organizational context, risk profile, and maturity level. Compliance with ISO 27001:2022 (certification goal) takes precedence over voluntary frameworks.

### 4.4 External Resources & Support

**Threat Intelligence Sources**:
- CISA (Cybersecurity & Infrastructure Security Agency) alerts
- ENISA (European Union Agency for Cybersecurity) threat landscape
- Vendor threat intelligence (Microsoft Security Intelligence, Cisco Talos, etc.)
- ISAC (Information Sharing and Analysis Center) for relevant sector
- Commercial threat intelligence feeds (if subscribed)

**Forensic Resources**:
- Pre-vetted forensic firms (retainer or on-demand)
- Law enforcement contacts (FBI Cyber Division, Europol EC3, local cybercrime units)
- Forensic tool vendors (support for forensic software)

**Incident Response Community**:
- Local CSIRT community (FIRST - Forum of Incident Response and Security Teams)
- Industry-specific information sharing groups
- Cloud provider incident response services (AWS Incident Response, Microsoft Incident Response)

**Regulatory Contacts**:
- FDPIC (Swiss Federal Data Protection and Information Commissioner)
- EU Supervisory Authorities (for GDPR notifications)
- Sector-specific regulators (FINMA, national cyber authorities)

**Insurance & Legal**:
- Cyber insurance carrier (incident notification per policy)
- External legal counsel (data breach counsel, regulatory counsel)
- Public relations firm (for major incidents with media attention)

---

## 5. Evidence

### 5.1 Evidence Requirements Overview

This section defines the expected evidence to demonstrate compliance with ISO/IEC 27001:2022 Controls A.5.24-28 (Incident Management Lifecycle). Evidence requirements are organized into two stages:

- **Stage 1 Evidence**: Documentation of policies, procedures, roles, and capabilities (existence and design)
- **Stage 2 Evidence**: Operational effectiveness through incident response activities, metrics, and continuous improvement (implementation and operation)

**Audit Approach**: ISO 27001 auditors assess both stages. Stage 1 evidence demonstrates controls exist and are designed appropriately. Stage 2 evidence demonstrates controls operate effectively and achieve intended outcomes. This policy defines WHAT evidence is expected; ISMS-IMP-A.5.24-28 Implementation Guides define HOW to collect and organize evidence.

**Evidence Collection**: ISMS-IMP-A.5.24-28.S1 through S5 (Implementation Assessment) workbooks provide structured evidence collection frameworks. Evidence Register sheets in each assessment workbook document WHERE evidence is located and verification status.

### 5.2 Stage 1 Evidence (Policy Documentation & Design)

Stage 1 evidence demonstrates that incident management controls are **documented, designed, and ready to operate**:

#### 5.2.1 Governance & Planning (A.5.24)

**Policy & Procedure Documentation**:
- **ISMS-POL-A.5.24-28**: This policy document (approved, current version)
- **Incident Response Procedures**: Documented procedures covering detection, assessment, response, evidence collection, learning (per Section 2.1.3)
- **Incident Response Playbooks**: Documented playbooks for common incident types (ransomware, data breach, phishing, DDoS, insider threat)

**Organizational Structure**:
- **CSIRT/SOC Charter**: Documented organizational structure, mission, authority
- **RACI Matrix**: Roles and responsibilities for incident lifecycle phases (per Section 3.1)
- **Escalation Matrix**: Escalation paths and authority levels (per Section 3.2)

**Incident Classification Framework**:
- **Severity Definitions**: Documented severity levels and criteria (per Section 2.1.2)
- **Incident Categories**: Documented incident taxonomy (reference to ISMS-REF-A.5.24-28 Section 1)
- **Response SLA Matrix**: Documented response SLAs per severity (per Section 3.2)

**Training & Competency**:
- **Training Program Documentation**: Training requirements, content, frequency (per Section 2.1.4)
- **Training Records**: Evidence personnel have received initial and ongoing training (training roster, completion certificates, competency assessments)
- **Tabletop Exercise Plans**: Documented tabletop exercise scenarios and schedules

**Tools & Technology**:
- **Incident Management System**: Documentation of ticketing/workflow system capabilities
- **Forensic Tools Inventory**: List of forensic tools available (disk imaging, memory capture, log preservation)
- **Communication Tools**: Documented secure communication channels for incident team

**Integration Documentation**:
- **Integration Points Documented**: How incident management integrates with monitoring (A.8.16), logging (A.8.15), event reporting (A.6.8), BC/DR (A.5.29-30), legal requirements (A.5.31)

#### 5.2.2 Assessment & Classification (A.5.25)

**Assessment Procedures**:
- **Event Assessment Procedure**: Documented process for event-to-incident determination (per Section 2.2.1)
- **Severity Classification Procedure**: Documented process for severity assignment (per Section 2.2.2)
- **Escalation Procedure**: Documented escalation triggers and paths (per Section 2.2.4)

**Classification Criteria**:
- **Event vs. Incident Criteria**: Documented criteria for determining if event is incident
- **Severity Factors**: Documented factors for severity determination (confidentiality, integrity, availability impact)
- **Category Taxonomy**: Reference to ISMS-REF-A.5.24-28 Section 1 (Incident Classification Taxonomy)

#### 5.2.3 Response Operations (A.5.26)

**Response Procedures**:
- **Containment Procedures**: Documented short-term and long-term containment procedures (per Section 2.3.1 Phase 1)
- **Eradication Procedures**: Documented eradication procedures per incident category (per Section 2.3.1 Phase 2)
- **Recovery Procedures**: Documented recovery and service restoration procedures (per Section 2.3.1 Phase 3)

**Communication Procedures**:
- **Internal Communication Plan**: Documented procedures for incident team, management, user communications (per Section 2.3.2)
- **External Communication Plan**: Documented procedures for regulatory, customer, partner, law enforcement, media communications (per Section 2.3.2)
- **Communication Templates**: Templates for common communications (user notifications, management updates, breach notifications)

**Coordination Procedures**:
- **Response Coordination Procedure**: Documented roles and coordination mechanisms during response (per Section 2.3.3)
- **BC/DR Integration**: Documented process for BC/DR activation during incidents (per Section 2.3.4)

#### 5.2.4 Evidence Collection (A.5.28)

**Forensic Procedures**:
- **Evidence Collection Procedures**: Documented procedures for evidence identification, collection, acquisition (per Section 2.4.2)
- **Evidence Type Guidance**: Documented evidence types and collection methods (reference to ISMS-REF-A.5.24-28 Section 3)
- **Tool Selection Guidance**: Documented forensic tools and their use cases

**Chain of Custody Procedures**:
- **Chain of Custody Templates**: Documented templates for chain of custody tracking (per Section 2.4.3)
- **Evidence Storage Procedure**: Documented procedures for evidence preservation and storage (per Section 2.4.4)
- **Legal Hold Procedure**: Documented legal hold process (per Section 2.4.5)

#### 5.2.5 Learning & Improvement (A.5.27)

**PIR Procedures**:
- **Post-Incident Review Process**: Documented PIR requirements, participants, agenda, timeline (per Section 2.5.1)
- **PIR Report Template**: Documented template for PIR reports

**Improvement Procedures**:
- **Root Cause Analysis Method**: Documented RCA methodology (5 Whys, Fishbone, etc.) (per Section 2.5.2)
- **Improvement Tracking Process**: Documented process for tracking improvement actions (per Section 2.5.3)
- **Knowledge Management**: Documented lessons learned repository and access controls (per Section 2.5.4)

### 5.3 Stage 2 Evidence (Operational Effectiveness)

Stage 2 evidence demonstrates that incident management controls **operate effectively in practice**:

#### 5.3.1 Operational Incident Response

**Incident Records** (sampling of recent incidents):
- **Incident Tickets**: Sample of 20-50 recent incident tickets from incident management system showing:
  - Event detection source (monitoring alert, user report, external notification)
  - Assessment outcome (event vs. incident determination)
  - Severity and category classification
  - Timestamps (detection, assessment, response initiation, containment, recovery, closure)
  - Response actions taken
  - Documentation quality

**Incident Timeline Analysis**:
- **Response Time Metrics**: Evidence of response times meeting SLAs (MTTD, MTTR, MTTC calculations)
- **SLA Compliance**: Percentage of incidents meeting response SLA targets (per severity)
- **Escalation Evidence**: Examples of appropriate escalation for High/Critical incidents

**Quality Indicators**:
- **Severity Classification Accuracy**: Evidence severity was correctly assigned (or corrected during investigation)
- **False Positive Handling**: Evidence false positives are identified, documented, and used for alert tuning
- **Completeness**: Evidence incidents are fully documented per procedure requirements

#### 5.3.2 Training & Competency Demonstration

**Training Completion**:
- **Training Records**: Evidence incident response personnel completed required training (roster with completion dates, certificates)
- **Competency Assessments**: Results of competency assessments or technical exercises
- **New Hire Training**: Evidence new incident response team members receive training before assuming duties

**Tabletop Exercises**:
- **Exercise Documentation**: Evidence of tabletop exercises conducted (minimum twice annually):
  - Exercise scenarios used
  - Participant list
  - Exercise outcomes (what worked, what didn't)
  - Lessons learned from exercises
  - Improvements implemented from exercise findings

**Awareness Training**:
- **User Awareness**: Evidence all personnel received training on incident reporting (completion rates, training content)

#### 5.3.3 Communication Effectiveness

**Management Reporting**:
- **Critical Incident Notifications**: Evidence Executive Management notified within 1 hour for Critical incidents (notification emails, timestamps)
- **Status Updates**: Evidence of regular status updates per Section 3.3 requirements

**External Communications**:
- **Regulatory Notifications**: Evidence of timely breach notifications (GDPR 72-hour compliance, Swiss nDSG "as soon as possible")
- **Customer Communications**: Evidence of customer notification when data affected
- **Third-Party Coordination**: Evidence of coordination with third parties during incidents

#### 5.3.4 Forensic Evidence Management

**Evidence Collection Examples**:
- **Chain of Custody Records**: Sample chain of custody documentation for incidents requiring forensic evidence
- **Evidence Integrity**: Evidence of cryptographic hashing for integrity verification
- **Evidence Storage**: Evidence of secure evidence storage (access logs, encryption)

**Legal Hold Compliance**:
- **Legal Hold Records**: Evidence legal hold procedures followed when required
- **Evidence Retention**: Evidence retention requirements followed per Section 2.4.4

#### 5.3.5 Post-Incident Learning

**PIR Completion**:
- **PIR Reports**: Sample PIR reports for Critical and High incidents (evidence PIR conducted within required timeline)
- **PIR Participants**: Evidence appropriate personnel participated in PIRs

**Root Cause Analysis**:
- **RCA Documentation**: Evidence root cause analysis conducted for major incidents
- **RCA Quality**: Evidence RCA identified systemic issues, not just proximate causes

**Improvement Implementation**:
- **Improvement Actions Tracked**: Evidence improvement actions tracked with owners and deadlines
- **Improvement Completion Rate**: Percentage of improvement actions completed on time
- **Control Enhancements**: Evidence of specific control improvements implemented from incidents:
  - Updated procedures (version history, change log)
  - New monitoring rules (alert rule changes)
  - Enhanced training (training content updates)
  - Policy updates (policy revision history)

**Knowledge Management**:
- **Lessons Learned Repository**: Evidence lessons learned are documented and accessible
- **Playbook Updates**: Evidence playbooks updated based on lessons learned (version history)
- **Trend Analysis**: Evidence of quarterly trend analysis and management review

#### 5.3.6 Metrics & Continuous Improvement

**Incident Metrics**:
- **Volume Metrics**: Trend data on incident volume by severity and category (monthly/quarterly reports)
- **Performance Metrics**: Trend data on MTTD, MTTR, MTTC over time
- **SLA Compliance Rate**: Trend data showing SLA compliance percentage

**Improvement Trends**:
- **Improving Metrics**: Evidence metrics improving over time (faster detection, faster response)
- **Negative Trends Addressed**: Evidence negative trends identified and action plans implemented

**Executive Reporting**:
- **Quarterly Reports**: Evidence quarterly incident summary provided to Executive Management (per Section 3.3)
- **Annual Report**: Evidence annual incident management program review conducted (per Section 2.5.5)

**Maturity Assessment**:
- **Maturity Self-Assessment**: Evidence of periodic maturity assessment against industry frameworks
- **Improvement Roadmap**: Evidence of continuous improvement roadmap based on maturity gaps

### 5.4 Evidence Collection Procedures

**Evidence Organization**:

Evidence MUST be organized systematically for audit readiness:

**Evidence Repository Structure**:
```
Evidence/
├── A.5.24-Planning/
│   ├── Policy_Procedures/
│   ├── Training_Records/
│   ├── Tabletop_Exercises/
│   └── Tools_Documentation/
├── A.5.25-Assessment/
│   ├── Classification_Framework/
│   ├── Sample_Assessments/
│   └── False_Positive_Analysis/
├── A.5.26-Response/
│   ├── Incident_Tickets/
│   ├── Response_Metrics/
│   ├── Communication_Examples/
│   └── SLA_Compliance_Reports/
├── A.5.27-Learning/
│   ├── PIR_Reports/
│   ├── Improvement_Tracking/
│   ├── Lessons_Learned/
│   └── Annual_Reviews/
├── A.5.28-Evidence/
│   ├── Chain_of_Custody_Examples/
│   ├── Forensic_Procedures/
│   └── Legal_Hold_Records/
└── Cross-Cutting/
    ├── Metrics_Dashboards/
    ├── Executive_Reports/
    └── Regulatory_Notifications/
```

**Evidence Register**:

ISMS-IMP-A.5.24-28.S1 through S5 (Implementation Assessments) include Evidence Register sheets documenting:
- Evidence ID (unique identifier)
- Evidence Type (policy, procedure, record, report, etc.)
- Evidence Description
- Related Control (A.5.24, A.5.25, A.5.26, A.5.27, A.5.28)
- Storage Location (file path, system location)
- Date Collected
- Verification Status (verified, pending, not applicable)

**Sampling Strategy**:

For operational evidence (Stage 2):
- **Incident Tickets**: Sample 20-50 incidents from past 12 months covering:
  - All severity levels (Critical, High, Medium, Low)
  - Various incident categories
  - Mix of recent (past month) and historical (6-12 months ago)
- **PIR Reports**: All Critical incidents, sample of High incidents (minimum 5)
- **Training Records**: All incident response team members
- **Tabletop Exercises**: All exercises from past 12 months (minimum 2)

**Evidence Freshness**:

Evidence should be current:
- **Policies/Procedures**: Current approved version
- **Operational Evidence**: Past 12 months (demonstrates sustained operation)
- **Training Records**: Past 24 months (demonstrates ongoing training)
- **Metrics**: Rolling 12-month trends

**Audit Preparation**:

Prior to audit:
1. Conduct evidence gap analysis using ISMS-IMP-A.5.24-28.S1-S5 assessment workbooks
2. Collect missing evidence
3. Organize evidence per repository structure
4. Complete Evidence Registers in assessment workbooks
5. Verify evidence is accessible and current
6. Prepare evidence summary for auditors (what evidence is available, where located)

### 5.5 Evidence Sufficiency & Quality

**Sufficiency Criteria**:

Evidence is sufficient when auditor can verify:
- **Existence**: Control exists (Stage 1 - policy, procedure documented)
- **Design**: Control designed appropriately (Stage 1 - procedure covers required elements)
- **Implementation**: Control implemented in practice (Stage 2 - incidents handled per procedures)
- **Operation**: Control operates consistently over time (Stage 2 - metrics show sustained operation)
- **Effectiveness**: Control achieves intended outcome (Stage 2 - incidents contained, response times improving)

**Quality Criteria**:

Evidence quality assessed by:
- **Authenticity**: Evidence is genuine (created by [Organization], not fabricated)
- **Accuracy**: Evidence is correct (data is accurate, not manipulated)
- **Completeness**: Evidence covers the control requirement fully
- **Reliability**: Evidence is from trustworthy source (system logs, official records)
- **Relevance**: Evidence directly demonstrates the control requirement
- **Timeliness**: Evidence is current (not outdated)

**Common Evidence Gaps**:

Typical gaps to avoid:
- **Procedures documented but not followed**: Stage 1 exists but Stage 2 shows procedures not used
- **Training planned but not delivered**: Training program documented but no completion records
- **PIRs required but not completed**: Policy requires PIR but incident tickets show PIRs not conducted
- **Improvements identified but not implemented**: PIRs document recommendations but no evidence of implementation
- **Metrics collected but not reviewed**: Metrics available but no evidence of management review or action on trends

**Continuous Evidence Collection**:

Incident management generates evidence naturally through operations:
- Incident tickets (operational evidence)
- PIR reports (learning evidence)
- Training records (competency evidence)
- Metrics dashboards (performance evidence)

**Best Practice**: Treat evidence collection as ongoing activity, not pre-audit scramble. ISMS-IMP-A.5.24-28 assessment workbooks facilitate continuous evidence collection and readiness.

---

## 6. Definitions & Annexes

### 6.1 Glossary

**Additional Definitions** (beyond Section 1.7):

**APT (Advanced Persistent Threat)**: Prolonged and targeted cyberattack in which intruder gains access to network and remains undetected for extended period, typically nation-state or sophisticated organized crime.

**BEC (Business Email Compromise)**: Social engineering attack where attacker impersonates executive or business partner via email to trick employees into transferring funds or disclosing sensitive information.

**CSIRT (Computer Security Incident Response Team)**: See Section 1.7 definition. Synonyms: CERT (Computer Emergency Response Team), IRT (Incident Response Team), SOC (when combined with monitoring function).

**DDoS (Distributed Denial of Service)**: Attack overwhelming system with traffic from multiple sources simultaneously, designed to make service unavailable to legitimate users.

**EDR (Endpoint Detection and Response)**: Security solution monitoring endpoint devices (workstations, servers) for suspicious activity and enabling incident response actions (isolation, remediation).

**Indicator of Compromise (IoC)**: Artifact observed on network or system indicating potential security incident (malicious IP, file hash, domain name, behavior pattern).

**Incident Commander**: Role during incident response responsible for overall coordination, decision-making, and communication. Typically Incident Response Manager or senior incident handler.

**Lateral Movement**: Techniques used by attacker to move from initial foothold to other systems within network, expanding access and control.

**Malware**: Malicious software including viruses, worms, trojans, ransomware, spyware, rootkits, cryptominers designed to harm systems or steal data.

**Phishing**: Social engineering attack using fraudulent email or communication to trick recipient into revealing sensitive information or downloading malware.

**Privilege Escalation**: Exploitation technique gaining elevated access rights beyond original authorization level, often targeting administrative or root access.

**Ransomware**: Malware encrypting victim's data and demanding payment for decryption key. Modern variants combine encryption with data exfiltration threats (double extortion).

**SIEM (Security Information and Event Management)**: Technology aggregating and analyzing log data from multiple sources to detect security events and support incident investigation.

**SOC (Security Operations Center)**: See Section 1.7 definition. Team or function responsible for continuous monitoring, detection, and response to security events.

**Threat Actor**: Entity responsible for security incident, including cybercriminals, nation-states, hacktivists, insiders, competitors.

**TTP (Tactics, Techniques, and Procedures)**: Behavior patterns of threat actors documented in frameworks like MITRE ATT&CK, used to understand adversary behavior and improve detection.

**Zero-Day**: Previously unknown vulnerability exploited by attackers before vendor has released patch, representing high risk due to lack of defense.

### 6.2 References

**Regulatory References**:
- **EU GDPR** (General Data Protection Regulation): Regulation (EU) 2016/679, Articles 33-34 (Breach Notification)
- **Swiss nDSG** (Federal Data Protection Act): Bundesgesetz über den Datenschutz (nDSG), Art. 24 (Breach Notification)
- **ISO/IEC 27001:2022**: Information Security Management Systems - Requirements, Annex A.5.24-28
- **ISO/IEC 27002:2022**: Information Security Controls, Sections 5.24-28 (Implementation Guidance)

**Technical Standards**:
- **NIST SP 800-61 Rev. 2**: Computer Security Incident Handling Guide
- **ISO/IEC 27035-1:2023**: Information Security Incident Management - Part 1: Principles and Process
- **ISO/IEC 27037:2012**: Guidelines for Identification, Collection, Acquisition and Preservation of Digital Evidence
- **NIST SP 800-86**: Guide to Integrating Forensic Techniques into Incident Response
- **RFC 3227**: Guidelines for Evidence Collection and Archiving

**Threat Intelligence**:
- **MITRE ATT&CK Framework**: Adversary tactics and techniques knowledge base
- **MITRE D3FEND**: Defensive countermeasures knowledge graph
- **CISA Alerts**: Cybersecurity & Infrastructure Security Agency threat advisories
- **ENISA Threat Landscape**: European Union Agency for Cybersecurity annual threat reports

**Industry Resources**:
- **SANS Incident Handler's Handbook**: Practical incident response methodology
- **Verizon Data Breach Investigations Report (DBIR)**: Annual breach statistics and trends
- **FIRST (Forum of Incident Response and Security Teams)**: Global incident response community
- **CERT/CC**: CERT Coordination Center incident response resources

**Internal References**:
- **ISMS-POL-00**: Regulatory Applicability Framework
- **ISMS-REF-A.5.24-28**: Incident Response Reference Guide (Taxonomy, Regulatory Quick Reference, Forensic Techniques)
- **ISMS-IMP-A.5.24-28.S1-S5**: Implementation Assessment Guides (Framework, Detection, Response, Forensics, Learning)
- **ISMS-POL-A.8.15**: Logging
- **ISMS-POL-A.8.16**: Monitoring Activities
- **ISMS-POL-A.6.8**: Information Security Event Reporting
- **ISMS-POL-A.5.29-30**: Business Continuity & Disaster Recovery Framework
- **ISMS-POL-A.5.31**: Legal, Statutory, Regulatory Requirements

### 6.3 Approval Record

| Role | Name | Date | Signature |
|------|------|------|-----------|
| **Document Owner (CISO)** | [Name] | [Date] | [Signature] |
| **Technical Review (Incident Response Manager)** | [Name] | [Date] | [Signature] |
| **Technical Review (CIO)** | [Name] | [Date] | [Signature] |
| **Legal Review (Legal Counsel)** | [Name] | [Date] | [Signature] |
| **Privacy Review (DPO)** | [Name] | [Date] | [Signature] |
| **Final Approval (Executive Management)** | [Name] | [Date] | [Signature] |

---

**END OF DOCUMENT**

**Document Status**: Draft - Awaiting Approval  
**Next Review Date**: [Effective Date + 12 months]  
**Document Location**: [Organization] Internal Policy Portal / ISMS Document Repository

---

*This policy establishes requirements for information security incident management covering the complete lifecycle: planning & preparation (A.5.24), assessment & decision (A.5.25), response operations (A.5.26), forensic evidence collection (A.5.28), and learning & improvement (A.5.27). Implementation procedures (HOW) are documented in ISMS-IMP-A.5.24-28 Implementation Guides (.S1 through .S5). Technical references (incident taxonomy, regulatory notifications, forensic techniques) are provided in ISMS-REF-A.5.24-28. Assessment and compliance evidence is generated via ISMS-IMP-A.5.24-28 assessment workbooks for systematic incident management capability evaluation.*
