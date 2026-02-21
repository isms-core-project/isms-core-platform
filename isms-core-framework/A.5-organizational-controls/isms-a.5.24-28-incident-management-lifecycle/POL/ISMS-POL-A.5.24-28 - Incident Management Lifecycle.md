<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.24-28:framework:POL:a.5.24-28 -->
**ISMS-POL-A.5.24-28 - Incident Management Lifecycle**

---

**Document Control**

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
- ISMS-IMP-A.5.24-28.-UG/TGS1 through S5 (Implementation Assessments)
- ISO/IEC 27001:2022 Controls A.5.24, A.5.25, A.5.26, A.5.27, A.5.28
- ISMS-POL-A.8.15 (Logging)
- ISMS-POL-A.8.16 (Monitoring Activities)
- ISMS-POL-A.6.8 (Information Security Event Reporting)
- ISMS-POL-A.5.29-30 (Business Continuity & Disaster Recovery)
- ISMS-POL-A.5.31 (Legal, Statutory, Regulatory Requirements)

---

# Executive Summary

This policy establishes [Organization]'s requirements for managing information security incidents throughout their complete lifecycle in accordance with ISO/IEC 27001:2022 Controls A.5.24 through A.5.28.

**Purpose**: Define organizational requirements for incident management control implementation and governance. This policy establishes WHAT incident management capabilities are required, WHO is accountable, and WHEN actions must occur. Implementation procedures (HOW to execute incident response) are documented separately in ISMS-IMP-A.5 (UG/TG variants).24-28 Implementation Guides.

**Scope**: This policy applies to all information security events and incidents affecting [Organization]'s information assets, systems, networks, and services, regardless of source (internal, external, third-party) or deployment model (on-premises, cloud, hybrid).

**Combined Control Approach**: These five controls are implemented as a unified lifecycle framework:

1. **Planning & Preparation (A.5.24)** - Establish capabilities before incidents occur
2. **Assessment & Decision (A.5.25)** - Determine if event is an incident requiring response
3. **Response Operations (A.5.26)** - Contain, eradicate, recover from incidents
4. **Evidence Collection (A.5.28)** - Preserve forensic evidence (parallel to response)
5. **Learning & Improvement (A.5.27)** - Extract lessons, improve controls

Despite unified implementation, each control maintains distinct requirements for Statement of Applicability (SoA) purposes.

---

# Scope & Applicability

## In Scope

**Information Security Incidents** affecting:

- IT systems, applications, and databases
- Data and information assets (all classifications)
- Network infrastructure (on-premises, cloud, hybrid)
- Users and authentication systems
- Third-party systems interfacing with [Organization]
- Physical security incidents affecting information assets

**Incident Categories** covered:

- Malware and ransomware
- Unauthorized access and privilege escalation
- Data breaches and exfiltration
- Denial of service (DoS/DDoS)
- Social engineering and phishing
- Insider threats (malicious, negligent)
- Physical security incidents affecting IT
- Supply chain and third-party incidents
- Configuration errors causing security impact

## Out of Scope

The following require Executive Management approval and documented risk acceptance:

- Incidents affecting only Public (unclassified) information with no business impact
- Incidents managed by separate frameworks (e.g., safety incidents, HR violations without security component)
- Third-party incidents with contractual incident management delegation

## Third-Party Applicability

Third-party service providers, contractors, and partners accessing [Organization] systems or handling [Organization] data MUST:

- Report security events and incidents per [Organization] reporting requirements
- Cooperate with [Organization] incident response activities
- Comply with evidence preservation requirements
- Participate in post-incident reviews when third-party actions contributed to incident

## Regulatory Applicability

This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework):

**Tier 1: Mandatory Compliance**

- **Swiss nDSG (FADP)**: Art. 24 - Data breach notification to FDPIC "as soon as possible" when high risk
- **EU GDPR**: Art. 33-34 - Breach notification to supervisory authority within 72 hours
- **ISO/IEC 27001:2022**: Controls A.5.24, A.5.25, A.5.26, A.5.27, A.5.28

**Tier 2: Conditional Applicability**

- PCI DSS v4.0.1, FINMA, DORA, NIS2, HIPAA - Apply where [Organization]'s business activities trigger applicability per ISMS-POL-00

---

# Policy Statements

## Incident Management Planning & Preparation (A.5.24)

[Organization] SHALL establish incident management capabilities BEFORE incidents occur.

**PS-3.1.1 Organizational Capability**: [Organization] MUST establish an incident response capability through designated CSIRT (Computer Security Incident Response Team) and/or SOC (Security Operations Center) functions with defined authority and resources.

**PS-3.1.2 Documented Procedures**: [Organization] MUST document and maintain incident response procedures covering the complete incident lifecycle. Procedures SHALL be version controlled and reviewed annually.

**PS-3.1.3 Classification Framework**: [Organization] MUST establish an incident classification framework defining severity levels and incident categories. The framework SHALL enable consistent incident prioritization and escalation.

**PS-3.1.4 Training Requirements**: Incident response personnel MUST be trained and demonstrate competency before assuming incident response duties. Competency SHALL be assessed through practical tabletop exercises and supervisor verification of response procedure knowledge. Minimum competency standards are defined in ISMS-IMP-A.5.24-28.S1. Training SHALL be refreshed annually (12-month maximum interval from prior completion).

**PS-3.1.5 Exercise Requirements**: [Organization] MUST conduct incident response tabletop exercises minimum twice annually covering major incident scenarios. Exercise findings SHALL be documented, prioritized by risk, and tracked as improvement actions per PS-3.5.3 (Learning & Improvement). Critical capability gaps require immediate remediation with executive escalation.

**PS-3.1.6 Tools & Technology**: [Organization] MUST provide incident response teams with appropriate tools including: (1) incident management system with workflow tracking, (2) forensic acquisition capability, (3) secure communication channel (encrypted), (4) access to monitoring/logging systems per A.8.15/A.8.16. Tool adequacy is assessed annually in ISMS-IMP-A.5.24-28.S1.

**Verification**: Documented procedures, training records, exercise reports, and tool capabilities are verified through ISMS-IMP-A.5.24-28.S1 assessment.

## Event Assessment & Decision (A.5.25)

[Organization] SHALL systematically assess all security events to determine if they constitute incidents requiring response.

**PS-3.2.1 Assessment Requirement**: All security events detected through monitoring or reported by users MUST be assessed to determine if they constitute incidents requiring response. Events SHALL be prioritized for assessment based on: (1) automated severity indicators from monitoring systems (A.8.16), (2) affected system criticality per asset register (A.5.9), (3) event source (SOC alerts prioritized over user reports for duplicate events). Event prioritization methodology is detailed in ISMS-IMP-A.5.24-28.S2.

**PS-3.2.2 Severity Classification**: All confirmed incidents MUST be assigned a severity level based on impact to confidentiality, integrity, and availability using the CIA Impact Scoring Matrix defined in ISMS-REF-A.5.24-28 Section 1. Scoring considers: data volume affected, system criticality (per A.5.9 asset register), business process impact, regulatory notification triggers. Critical and High severity incidents SHALL be scored independently by two analysts to ensure consistency. Incident severity MAY be reclassified if new information changes impact assessment; reclassification to High/Critical requires Incident Response Manager approval with retroactive management notifications per Section 5.2.

**PS-3.2.3 Category Classification**: All incidents MUST be categorized by type using the organizational incident taxonomy to enable appropriate response procedures and trend analysis.

**PS-3.2.4 Escalation Requirements**: Incidents MUST be escalated to appropriate management levels based on severity. Critical incidents require immediate Executive Management notification.

**PS-3.2.5 Documentation**: All event assessments MUST be documented in the incident management system with mandatory fields: (1) event source and detection timestamp, (2) CIA impact analysis with scoring, (3) severity level and assignment rationale, (4) incident category per taxonomy, (5) escalation actions taken with notifications sent, (6) approver name and approval timestamp. The incident management system SHALL enforce mandatory field completion before assessment can be marked complete.

**Verification**: Assessment accuracy, classification consistency, and escalation compliance are verified through ISMS-IMP-A.5.24-28.S2 assessment.

## Incident Response Operations (A.5.26)

[Organization] SHALL respond to confirmed incidents in accordance with documented procedures.

**PS-3.3.1 Response Execution**: All confirmed incidents MUST be responded to following documented procedures appropriate to the incident severity and category. Response procedures are selected based on incident category (PS-3.2.3) with severity level (PS-3.2.2) determining resource allocation and escalation. Incident response playbooks are maintained in ISMS-REF-A.5.24-28 Section 3 for each primary incident category:

- **Malware/Ransomware**: Isolation, forensic imaging, malware analysis, eradication verification
- **Unauthorized Access**: Credential revocation, session termination, access log review, privilege escalation assessment
- **Data Breach**: Scope assessment, regulatory notification analysis (GDPR/nDSG), affected party identification, evidence preservation
- **Denial of Service**: Traffic analysis, mitigation activation (rate limiting, upstream filtering), service restoration prioritization
- **Social Engineering**: User notification, credential reset, awareness reinforcement, similar attack prevention
- **Insider Threat**: Evidence preservation (legal hold), HR coordination, access suspension, investigation scope determination
- **Physical Security**: Asset recovery, access control verification, surveillance review, physical control remediation
- **Supply Chain**: Supplier notification, dependency assessment, compensating control activation, contract review

For incidents spanning multiple categories, primary category is determined by most significant impact (data breach takes precedence over initial access vector). Playbook selection is documented in incident record with rationale. Hybrid or novel incidents without existing playbook default to general incident response procedure with Incident Response Manager guidance.

**PS-3.3.2 Containment**: Incident response SHALL prioritize containment to limit scope and prevent further damage. Containment approach varies by severity with aggressive containment for Critical/High incidents. Containment effectiveness SHALL be verified before proceeding to eradication phase: (1) No additional systems showing compromise indicators, (2) Attack vector is identified and blocked, (3) Threat actor access is terminated (credential revocation, session termination confirmed), (4) Monitoring confirms no lateral movement for minimum 1 hour (Critical/High) or 4 hours (Medium). For ongoing sophisticated attacks, containment may be iterative with Incident Response Manager approval to proceed.

**PS-3.3.3 Eradication**: The root cause of incidents MUST be eliminated before systems are returned to production. Eradication actions SHALL be verified before proceeding to recovery.

**PS-3.3.4 Recovery**: Affected systems and services MUST be restored to normal operations following security verification. Recovery SHALL follow business criticality priorities aligned with BC/DR requirements. System recovery priority is determined by business criticality ratings from the asset register (A.5.9) and Recovery Time Objectives (RTO) from BC/DR plans (A.5.29-30). Priority tiers: (1) Critical systems (RTO < 4 hours) - immediate recovery, (2) High priority (RTO 4-24 hours) - same business day, (3) Medium priority (RTO 1-3 days) - next business day, (4) Low priority (RTO > 3 days) - scheduled restoration. Recovery sequencing considers dependencies (restore supporting infrastructure before dependent applications). Recovery priorities may be overridden by Incident Response Manager with Executive Management approval when incident context requires deviation.

**PS-3.3.5 Communication**: Incident communications MUST follow documented protocols for internal stakeholders, management, users, and external parties (regulators, customers, law enforcement) as required. Communication protocols SHALL specify:

- **Internal stakeholders**: Incident response team (all severities), affected business unit owners (Medium+), IT Operations (all severities), InfoSec management (High+), Executive Management (Critical)
- **Management escalations**: Per Section 5.2 escalation matrix with defined content (incident summary, impact assessment, containment status, estimated resolution time)
- **User communications**: Affected users notified of service impacts (Medium+), with updates per SLA intervals for ongoing incidents
- **External parties**:
  - Regulators (GDPR/nDSG breach notification per Art. 33/Art. 24) - Legal and DPO coordinate
  - Customers (if their data affected) - Communications team drafts, Executive Management approves
  - Law enforcement (if criminal activity suspected) - Legal counsel decides, coordinates handoff
  - Third parties (if supplier incident impacts [Organization]) - Supplier Management coordinates per A.5.22

Communication templates for each severity level and stakeholder type are maintained in ISMS-REF-A.5.24-28 Section 2 and incident management system. All Critical/High incident communications require Incident Response Manager approval before sending.

**PS-3.3.6 Response Time Standards**: [Organization] MUST define and maintain response time standards (SLAs) by severity level per Section 5.1.1. SLA compliance SHALL be measured monthly and reported in quarterly executive summaries. Missed SLAs require root cause analysis per PS-3.5.2 (Post-Incident Review) to identify systemic issues requiring remediation.

**Verification**: Response execution, SLA compliance, and communication effectiveness are verified through ISMS-IMP-A.5.24-28.S3 assessment.

## Forensic Evidence Collection & Preservation (A.5.28)

[Organization] SHALL establish procedures for forensic evidence identification, collection, acquisition, and preservation.

**PS-3.4.1 Evidence Collection Requirement**: Forensic evidence MUST be collected for all Critical severity incidents and High severity incidents with potential legal or regulatory implications.

**PS-3.4.2 Collection Timing**: Evidence collection begins immediately upon incident detection and runs parallel to response operations. Evidence preservation SHALL not be sacrificed except when containment of active threats takes priority.

**PS-3.4.3 Forensically Sound Methods**: Evidence MUST be collected using forensically sound methods that maintain integrity and support potential legal admissibility.

**PS-3.4.4 Chain of Custody**: All evidence MUST have documented chain of custody from collection through disposal including custody transfers, storage locations, and access records.

**PS-3.4.5 Evidence Preservation**: Evidence MUST be preserved securely with access controls, encryption, and integrity verification. Retention periods SHALL comply with regulatory requirements and [Organization] retention policies.

**PS-3.4.6 Legal Hold**: [Organization] MUST implement legal hold procedures when litigation is commenced or reasonably anticipated, suspending normal deletion processes for relevant evidence.

**Verification**: Evidence procedures, chain of custody documentation, and preservation controls are verified through ISMS-IMP-A.5.24-28.S4 assessment.

## Post-Incident Learning & Improvement (A.5.27)

[Organization] SHALL extract lessons from incidents and translate findings into control improvements.

**PS-3.5.1 Post-Incident Review Requirement**: Post-Incident Reviews (PIR) MUST be conducted for all Critical and High severity incidents within defined timeframes. Medium severity incidents require PIR when they reveal novel attack techniques or significant control failures.

**PS-3.5.2 Root Cause Analysis**: Root cause analysis MUST be conducted to identify underlying systemic issues, not just proximate causes. Findings SHALL inform preventive measures.

**PS-3.5.3 Improvement Implementation**: Lessons learned MUST be translated into actionable improvements with assigned owners and target completion dates. Improvement actions SHALL be tracked to completion.

**PS-3.5.4 Knowledge Management**: [Organization] MUST maintain a lessons learned repository accessible to incident response personnel. Response playbooks SHALL be updated based on lessons learned.

**PS-3.5.5 Metrics & Trend Analysis**: [Organization] MUST track incident metrics (volume, severity, response times, SLA compliance) and conduct quarterly trend analysis to identify systemic issues.

**PS-3.5.6 Annual Program Review**: The incident management program MUST be reviewed annually to assess effectiveness, benchmark against standards, and update procedures, training, and tools.

**Verification**: PIR completion, improvement tracking, and metrics reporting are verified through ISMS-IMP-A.5.24-28.S5 assessment.

---

# Roles & Responsibilities

## Executive Management

- **Accountable** for overall incident management program effectiveness
- **Approves** incident management policy and major procedure changes
- **Decides** on business-critical actions (service shutdown, public disclosure, law enforcement engagement)
- **Receives** Critical incident status updates, quarterly metrics, annual program review

## Chief Information Security Officer (CISO)

- **Accountable** for incident management policy compliance and program maturity
- **Approves** procedures, accepts residual risk, allocates budget and resources
- **Decides** on High/Critical incident response escalations and external engagement
- **Receives** all incident reports, PIR reports, weekly metrics

## Incident Response Manager / CSIRT Lead

- **Accountable** for day-to-day incident response operations and SLA compliance
- **Manages** incident assessment, response coordination, resource allocation, communications, training
- **Approves** incident closure, PIR scheduling, procedure updates
- **Reports** to CISO on incident status, metrics, and program health

## Incident Handlers / SOC Analysts

- **Responsible** for incident triage, investigation, containment, eradication, recovery, and documentation
- **Executes** response procedures per severity and category
- **Escalates** incidents per escalation matrix
- **Documents** all incident activities in incident management system

## Forensic Specialists

- **Accountable** for evidence collection integrity and chain of custody
- **Executes** forensic analysis and evidence preservation
- **Coordinates** with Legal on evidence admissibility and legal hold
- **Documents** all evidence collection and custody transfers

## IT Operations

- **Responsible** for executing containment/eradication/recovery actions on systems
- **Coordinates** service restoration with incident response team
- **Provides** technical support and system access for incident investigation
- **Implements** technical control improvements from PIR recommendations

## Legal Counsel

- **Accountable** for legal risk mitigation and regulatory compliance
- **Advises** on legal implications, regulatory notification requirements, evidence preservation
- **Coordinates** regulatory authority notifications with DPO
- **Manages** legal hold procedures and law enforcement liaison

## Data Protection Officer (DPO)

- **Accountable** for privacy compliance and breach notification assessment
- **Assesses** incidents for GDPR/nDSG breach notification requirements
- **Coordinates** data subject notifications when required
- **Advises** on personal data implications of incidents

## Communications Team

- **Responsible** for external communications and reputation management
- **Drafts** user, customer, and media communications
- **Coordinates** messaging with Legal and Executive Management
- **Executes** approved external communications

## All Personnel

- **Responsible** for reporting suspected security incidents per ISMS-POL-A.6.8
- **Cooperates** with incident response activities when requested
- **Completes** security awareness training including incident reporting

---

# Governance Framework

## Incident Severity Framework

[Organization] MUST define severity levels with associated response requirements:

| Severity | Definition | Response Requirement |
|----------|------------|----------------------|
| **Critical** | Significant business impact; large-scale breach, ransomware affecting production, critical infrastructure compromise, regulatory notification triggered | Immediate response, aggressive containment, Executive Management notification, mandatory PIR |
| **High** | Moderate business impact; targeted attack, confirmed data access, sensitive system compromise, service degradation | Urgent response, CISO notification, mandatory PIR |
| **Medium** | Limited business impact; isolated infection, unsuccessful attack, minor policy violation | Standard response, team lead oversight, conditional PIR |
| **Low** | Minimal business impact; blocked attack, minor anomaly, informational event | Standard handling, batch processing acceptable, no PIR required |

## Response Time Standards (SLAs)

[Organization] defines the following response time standards by severity level:

| Severity | Initial Response | Containment Target | Resolution Target | Management Updates |
|----------|------------------|-------------------|-------------------|-------------------|
| **Critical** | 15 minutes | 1 hour | 24 hours | Real-time (hourly) |
| **High** | 1 hour | 4 hours | 72 hours | Daily |
| **Medium** | 4 hours | 24 hours | 5 business days | Weekly (if ongoing) |
| **Low** | 8 hours | 48 hours | 10 business days | Batch reporting |

**Initial Response**: Time from incident confirmation (PS-3.2.1 assessment complete) to response team assigned and containment actions initiated.

**Containment Target**: Time to limit incident scope and prevent further damage. Target is goal, not guarantee - complex incidents may exceed targets with documented justification.

**Resolution Target**: Time to complete eradication and recovery, returning to normal operations. Clock stops when incident is closed by Incident Response Manager.

**Management Updates**: Frequency of status reporting to management per Section 5.3.

SLA compliance is measured monthly and reported in quarterly executive summaries. Missed SLAs require root cause analysis per PS-3.5.2 (Post-Incident Review). SLA targets are reviewed annually in program review (PS-3.5.6) and adjusted based on operational reality and industry benchmarks.

Detailed SLA measurement procedures are defined in ISMS-IMP-A.5.24-28.S3.

## Escalation Requirements

**Critical Incidents**: Immediate escalation to CISO and Executive Management
**High Incidents**: Escalation to Incident Response Manager (immediate), CISO (within defined timeframe)
**Medium/Low Incidents**: Team lead oversight; escalate if severity increases or resolution stalls

Management notification frequency and content requirements are defined in ISMS-IMP-A.5.24-28.S3.

## Reporting Requirements

**Operational Reporting**:

- Critical incidents: Real-time status updates to Executive Management
- High incidents: Daily status updates to CISO
- All incidents: Weekly summary to CISO

**Executive Reporting**:

- Quarterly incident summary to Executive Management (volume, trends, metrics, lessons learned)
- Annual incident management program review to Executive Management

## Integration with Related Controls

This policy integrates with:

| Control | Integration Point |
|---------|-------------------|
| **A.8.16 (Monitoring)** | Monitoring detects events that feed incident assessment |
| **A.8.15 (Logging)** | Logs provide evidence for investigation and forensics |
| **A.6.8 (Event Reporting)** | User reports feed incident assessment process |
| **A.5.29-30 (BC/DR)** | Major incidents may trigger BC/DR activation |
| **A.5.31 (Legal/Regulatory)** | Regulatory notification requirements incorporated |
| **A.5.19-23 (Third-Party)** | Third-party incidents reported and coordinated |

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: Major incident revealing policy gap, regulatory changes, audit findings, organizational changes
- **Reviewers**: CISO (owner), Incident Response Manager (contributor), Legal (compliance)
- **Approval**: CISO (technical), Executive Management (strategic)

Implementation procedures and reference documents may be updated without policy revision when changes do not affect policy statements.

---

# Compliance & Exceptions

## Compliance Requirements

All personnel MUST comply with this policy. Compliance is monitored through:

- Incident management system records and metrics
- Training completion tracking
- PIR completion rates
- Exercise participation
- Improvement action completion

## Exception Management

Exceptions to this policy require:

- Written exception request with business justification
- Risk assessment of exception
- Compensating controls (if applicable)
- CISO approval (minimum); Executive Management approval for Critical control exceptions
- Time-bound duration (maximum 12 months, renewal required)
- Documentation in ISMS exception register

Exceptions are reviewed annually for continued validity.

## Non-Compliance

Non-compliance with this policy may result in:

- Escalation to management
- Increased audit scrutiny
- Disciplinary action per HR policies
- Regulatory findings during certification audits

---

# Related Documents

## Implementation Guides

| Document | Purpose |
|----------|---------|
| **ISMS-IMP-A.5.24-28.S1-UG/TG** | Incident Management Framework Assessment (governance, structure, procedures, training, tools) |
| **ISMS-IMP-A.5.24-28.S2-UG/TG** | Event Detection & Classification Assessment (assessment procedures, classification accuracy, escalation) |
| **ISMS-IMP-A.5.24-28.S3-UG/TG** | Incident Response Capabilities Assessment (response procedures, SLAs, playbooks, communications) |
| **ISMS-IMP-A.5.24-28.S4-UG/TG** | Forensic Evidence Management Assessment (evidence procedures, chain of custody, preservation) |
| **ISMS-IMP-A.5.24-28.S5-UG/TG** | Learning & Continuous Improvement Assessment (PIR, root cause analysis, improvement tracking, metrics) |

## Reference Materials

| Document | Purpose |
|----------|---------|
| **ISMS-REF-A.5.24-28 Section 1** | Incident Classification Taxonomy (categories, subcategories, severity indicators) |
| **ISMS-REF-A.5.24-28 Section 2** | Regulatory Notification Quick Reference (GDPR, nDSG, sector-specific requirements) |
| **ISMS-REF-A.5.24-28 Section 3** | Forensic Collection Techniques Library (technical procedures, tools, templates) |

## Related Policies

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.8.15 (Logging)
- ISMS-POL-A.8.16 (Monitoring Activities)
- ISMS-POL-A.6.8 (Information Security Event Reporting)
- ISMS-POL-A.5.29-30 (Business Continuity & Disaster Recovery)
- ISMS-POL-A.5.31 (Legal, Statutory, Regulatory Requirements)
- ISMS-POL-A.5.19-23 (Third-Party Management)

## External Standards

- ISO/IEC 27001:2022 - Controls A.5.24, A.5.25, A.5.26, A.5.27, A.5.28
- ISO/IEC 27002:2022 - Implementation guidance for incident management controls
- NIST SP 800-61 Rev. 2 - Computer Security Incident Handling Guide
- ISO/IEC 27035 - Information Security Incident Management

---

# Definitions

**Information Security Event**: An identified occurrence indicating a possible breach of information security policy or failure of safeguards. Events may or may not become incidents upon assessment.

**Information Security Incident**: An unwanted or unexpected information security event with significant probability of compromising business operations and threatening information security. Incidents require response actions.

**CSIRT (Computer Security Incident Response Team)**: Organizational team responsible for receiving, reviewing, and responding to information security incidents.

**SOC (Security Operations Center)**: Team or function responsible for monitoring, detecting, analyzing, and responding to security events and incidents.

**Post-Incident Review (PIR)**: Structured review conducted after incident closure to document timeline, assess response effectiveness, identify lessons learned, and recommend improvements.

**Root Cause Analysis (RCA)**: Systematic investigation to identify fundamental cause(s) that allowed an incident to occur.

**Chain of Custody**: Documented trail showing who collected evidence, when, where, how, and every transfer of evidence between parties.

**Legal Hold**: Directive to preserve all potentially relevant evidence related to pending or reasonably anticipated legal proceedings.

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Evidence required to demonstrate this policy is adequately documented and approved:

- ✅ This policy document (ISMS-POL-A.5.24-28 v1.0)
- ✅ Approval signatures from CISO, CIO, Executive Management
- ✅ Incident management capability requirements defined (Section 3.1 - PS-3.1.1 through PS-3.1.6)
- ✅ Event assessment and classification framework documented (Section 3.2 - PS-3.2.1 through PS-3.2.5)
- ✅ Incident response operations procedures specified (Section 3.3 - PS-3.3.1 through PS-3.3.6)
- ✅ Forensic evidence requirements documented (Section 3.4 - PS-3.4.1 through PS-3.4.6)
- ✅ Post-incident learning requirements specified (Section 3.5 - PS-3.5.1 through PS-3.5.6)
- ✅ Incident severity framework defined (Section 5.1)
- ✅ Escalation requirements documented (Section 5.2)
- ✅ Roles and responsibilities assigned (Section 4)
- ✅ Governance and exception procedures defined (Section 6)
- ✅ Integration with related controls documented (Section 5.4)

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Incident register showing all incidents logged with classification (severity, category)
- Incident response timelines demonstrating SLA compliance (detection → containment → resolution)
- Escalation records showing appropriate management notifications by severity
- CSIRT/SOC staffing records and competency verification
- Training completion records for incident response personnel
- Tabletop exercise reports (minimum twice annually)
- Post-Incident Review (PIR) reports for all Critical/High incidents
- Root cause analysis documentation with improvement recommendations
- Lessons learned repository updates
- Improvement action tracking to completion
- Forensic evidence chain of custody documentation
- Evidence preservation and integrity verification records
- Regulatory notification records (GDPR 72-hour, nDSG "as soon as possible")
- Incident metrics dashboards (volume, severity, MTTR, SLA compliance)
- Quarterly trend analysis reports
- Annual program review documentation
- Assessment workbook outputs from ISMS-IMP-A.5.24-28.S1-S5

**Evidence Storage Locations**:

| Evidence Type | Storage Location |
|---------------|------------------|
| Training records | HR Information System / Learning Management System |
| Exercise reports | Incident Management System / Document Repository |
| Tool inventory | Configuration Management Database (CMDB) |
| Procedures | Document Management System |
| Competency assessments | Supervisor records in HRIS |
| Incident records | Incident Management System |
| PIR reports | Incident Management System / SharePoint |
| SLA compliance reports | Business Intelligence Dashboard |

## Clarification on Compliance Evidence

This policy establishes incident management governance framework (planning, assessment, response, evidence, learning requirements). It does NOT establish:

- **Technical detection controls** (addressed in A.8.16 Monitoring Activities - monitoring provides event feeds to incident assessment)
- **Logging infrastructure requirements** (addressed in A.8.15 Logging - logs provide investigation evidence)
- **Business continuity procedures** (addressed in A.5.29-30 BC/DR - major incidents may trigger BC/DR activation)
- **User event reporting procedures** (addressed in A.6.8 Information Security Event Reporting - user reports feed assessment)
- **Specific incident response playbooks** (operational detail in ISMS-IMP-A.5.24-28 and ISMS-REF-A.5.24-28)

The boundary is: POL-A.5.24-28 defines WHAT incident management capabilities are required and WHEN actions must occur → ISMS-IMP-A.5.24-28.S1-S5 provides HOW to assess capability maturity → ISMS-REF-A.5.24-28 provides technical reference materials → Related controls (A.8.15, A.8.16, A.6.8, A.5.29-30) provide supporting capabilities.

---

# Approval Record

| Role | Name | Date | Signature |
|------|------|------|-----------|
| **Document Owner (CISO)** | [Name] | [Date] | [Signature] |
| **Technical Review (Incident Response Manager)** | [Name] | [Date] | [Signature] |
| **Technical Review (CIO)** | [Name] | [Date] | [Signature] |
| **Legal Review (Legal Counsel)** | [Name] | [Date] | [Signature] |
| **Privacy Review (DPO)** | [Name] | [Date] | [Signature] |
| **Final Approval (Executive Management)** | [Name] | [Date] | [Signature] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for information security incident management covering the complete lifecycle (A.5.24-28). Implementation procedures are documented in ISMS-IMP-A.5.24-28 (UG/TG).S1 through S5.*

<!-- QA_VERIFIED: 2026-02-02 -->
