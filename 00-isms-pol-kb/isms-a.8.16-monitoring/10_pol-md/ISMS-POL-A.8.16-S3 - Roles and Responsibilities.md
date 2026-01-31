# ISMS-POL-A.8.16-S3
## Monitoring Activities - Roles and Responsibilities

**Document ID**: ISMS-POL-A.8.16-S3
**Title**: Monitoring Activities - Roles and Responsibilities  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]  | SOC Lead / Information Security Manager | Initial RACI definition |

**Review Cycle**: Annual (or upon significant organizational restructuring)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Operational Approval: Security Operations Center (SOC) Lead
- HR Approval: Human Resources Director (for role alignment)
- Management Approval: IT Director / CIO (for resource commitment)

**Distribution**: All stakeholders with defined roles, management, HR  
**Related Documents**: Organizational Chart, Job Descriptions, ISMS-POL-A.8.16 (Master)

---

## 3.1 Purpose and Scope

This section defines **roles and responsibilities** for monitoring activities implementation, operation, and governance. Clear accountability ensures effective detection, timely response, and continuous improvement of monitoring capabilities.

**Key Principle**: Responsibilities are assigned to **roles**, not specific individuals. Role assignments may change as organization evolves, but responsibilities remain consistent.

**In Scope**: All roles involved in monitoring lifecycle (policy, infrastructure, detection, triage, investigation, governance)  
**Primary Stakeholders**: All organizational personnel (everyone has some responsibility)  
**Implementation Evidence**: ISMS-IMP-A.8.16 (all assessments demonstrate role execution)

---

## 3.2 Responsibility Model

### 3.2.1 RACI Framework

This policy uses the **RACI model** to clarify responsibilities:

- **R - Responsible**: Performs the work, executes the task
- **A - Accountable**: Ultimately answerable, has approval authority (only ONE per task)
- **C - Consulted**: Provides input, must be consulted before action
- **I - Informed**: Kept informed, notified of outcomes

### 3.2.2 Separation of Duties

Where appropriate, responsibilities are separated to ensure checks and balances:

- Monitoring configuration separated from system administration (detect unauthorized changes)
- Alert triage separated from alert generation (avoid bias)
- Approval authority separated from requestor (no self-approval for exceptions)
- Investigation separated from remediation authority (detective vs. corrective controls)

Organizations **MAY** combine roles in small organizations where separation is impractical, but **SHALL** document combined roles and implement compensating controls (e.g., enhanced audit reviews, external SOC services).

---

## 3.3 Policy Owner (CISO)

### 3.3.1 Role Assignment

**Typical Role**: Chief Information Security Officer (CISO) or designated Deputy  
**Delegation**: CISO **MAY** delegate day-to-day responsibilities to SOC Lead or Security Manager but retains ultimate accountability.

### 3.3.2 Responsibilities

The Policy Owner is **ACCOUNTABLE** for:

**Policy Governance**:
- Establishing and maintaining monitoring policy framework (this document suite)
- Approving policy changes and updates
- Ensuring policy alignment with organizational risk appetite
- Reviewing policy effectiveness annually
- Approving baseline establishment methodology

**Strategic Decisions**:
- Defining monitoring scope and priorities (which assets MUST be monitored)
- Approving monitoring technology selection (SIEM, EDR, IDS/IPS, etc.)
- Allocating budget and resources for monitoring capabilities
- Approving detection strategy and approach
- Setting acceptable false positive rates and detection rate targets

**Risk Management**:
- Defining acceptable risk levels for undetected threats
- Approving monitoring coverage gaps and exceptions
- Accepting residual risks (systems not monitored, limited baseline coverage)
- Escalating significant risks to executive management

**Compliance**:
- Ensuring monitoring controls meet ISO 27001:2022 Control A.8.16 requirements
- Ensuring compliance with legal and regulatory monitoring obligations
- Supporting internal and external audits
- Approving audit remediation plans

**Performance Oversight**:
- Reviewing monitoring effectiveness metrics (MTTD, MTTR, detection rate)
- Approving detection improvement initiatives
- Holding SOC and Security Engineering accountable for performance
- Ensuring adequate SOC staffing and training

---

## 3.4 Security Operations Center (SOC) - Tier 1 Analysts

### 3.4.1 Role Assignment

**Typical Roles**: SOC Analyst (Junior/Entry-level), Security Analyst Level 1  
**Shift Coverage**: 24/7 for organizations with continuous monitoring, business hours for others

### 3.4.2 Responsibilities

SOC Tier 1 Analysts are **RESPONSIBLE** for:

**Alert Monitoring**:
- Monitoring security dashboards continuously (or per shift schedule)
- Acknowledging alerts within defined SLA (per ISMS-POL-A.8.16-S2.3)
- Prioritizing alerts by severity (Critical → High → Medium → Low)
- Tracking alert queue and ensuring no alerts are missed

**Alert Triage**:
- Conducting initial triage per documented procedures (ISMS-POL-A.8.16-S5.C)
- Determining alert disposition (True Positive / False Positive / Benign / Needs Investigation)
- Documenting triage findings in alert tracking system
- Closing false positive alerts with rationale
- Escalating confirmed incidents to Tier 2 or Incident Response

**Basic Investigation**:
- Gathering initial evidence (relevant logs, user/system context)
- Checking threat intelligence for IOC matches
- Correlating related alerts
- Following investigation playbooks for common scenarios

**Communication**:
- Notifying stakeholders per notification procedures (system owners, managers, executives)
- Providing status updates on alert investigation
- Escalating to on-call personnel for after-hours Critical alerts
- Documenting all actions in alert records

**Metrics**:
- Tracking personal triage times (MTTA, MTTT)
- Reporting alert volume and trends
- Identifying noisy detection rules requiring tuning

---

## 3.5 Security Operations Center (SOC) - Tier 2/3 Analysts

### 3.5.1 Role Assignment

**Typical Roles**: SOC Analyst (Senior), Security Analyst Level 2/3, Threat Hunter  
**Experience**: Advanced technical skills, deep security knowledge

### 3.5.2 Responsibilities

SOC Tier 2/3 Analysts are **RESPONSIBLE** for:

**Advanced Investigation**:
- Investigating complex security alerts escalated by Tier 1
- Conducting deep-dive forensic analysis
- Correlating events across multiple systems and time periods
- Identifying attack chains and lateral movement patterns
- Determining scope and impact of security incidents

**Detection Engineering**:
- Developing new detection rules and correlation logic
- Tuning existing detection rules to reduce false positives
- Implementing threat intelligence feeds
- Creating custom detections for organization-specific threats
- Testing detection effectiveness (validating rules work)

**Threat Hunting**:
- Proactively searching for threats not detected by automated monitoring
- Hypothesis-driven investigation (what if attacker did X?)
- Identifying detection gaps and proposing improvements
- Analyzing adversary TTPs (MITRE ATT&CK framework)

**Baseline Management**:
- Establishing baselines for critical systems (per ISMS-POL-A.8.16-S2.2)
- Reviewing and updating baselines quarterly
- Validating baseline accuracy
- Documenting baseline methodology

**Knowledge Management**:
- Creating and maintaining investigation playbooks
- Documenting lessons learned from investigations
- Training Tier 1 analysts
- Sharing threat intelligence internally and externally

**Escalation Support**:
- Supporting Incident Response Team during major incidents
- Providing technical expertise for complex investigations
- Recommending containment and remediation actions

---

## 3.6 SOC Lead / Security Operations Manager

### 3.6.1 Role Assignment

**Typical Role**: SOC Manager, Security Operations Manager  
**Reports To**: CISO or Security Director

### 3.6.2 Responsibilities

The SOC Lead is **ACCOUNTABLE** for:

**Operational Management**:
- Managing SOC team (hiring, training, performance management)
- Ensuring 24/7 coverage (shift scheduling, on-call rotations)
- Allocating work across team (alert distribution, investigation assignments)
- Managing SOC performance metrics (MTTA, MTTR, false positive rate)
- Ensuring SLA compliance for alert response

**Detection Management**:
- Approving new detection rules before production deployment
- Prioritizing detection rule development (what to build next?)
- Reviewing detection effectiveness metrics
- Conducting quarterly detection coverage assessment (MITRE ATT&CK mapping)
- Approving baseline establishment and updates

**Process Management**:
- Maintaining and improving SOC procedures
- Conducting lessons learned reviews after incidents
- Implementing continuous improvement initiatives
- Managing escalation procedures and handoffs to Incident Response
- Coordinating with other teams (IT Ops, Security Engineering, IR)

**Communication**:
- Reporting SOC metrics to CISO (weekly/monthly)
- Escalating critical incidents to CISO
- Representing SOC in management meetings
- Communicating with business stakeholders about security events

**Budget and Resources**:
- Proposing SOC budget (staffing, tools, training)
- Justifying resource needs to CISO
- Managing vendor relationships (SIEM, threat intel, training providers)

---

## 3.7 Security Engineering / Infrastructure

### 3.7.1 Role Assignment

**Typical Roles**: Security Engineer, Security Architect, Information Security Engineer  
**Team Lead**: Security Engineering Manager or Security Architect

### 3.7.2 Responsibilities

Security Engineering is **RESPONSIBLE** for:

**Monitoring Infrastructure**:
- Deploying and configuring monitoring platforms (SIEM, IDS/IPS, EDR, NDR)
- Ensuring monitoring coverage across all network segments (per ISMS-POL-A.8.16-S2.1)
- Integrating log sources (configuring log forwarding, parsers, normalization)
- Maintaining monitoring infrastructure (patches, upgrades, capacity)
- Implementing high availability and disaster recovery

**Technical Architecture**:
- Designing monitoring architecture (scalability, performance, resilience)
- Evaluating and selecting monitoring technologies
- Integrating monitoring with other security controls (threat intel, SOAR, ticketing)
- Planning capacity and storage (hot/warm/cold tiers per ISMS-POL-A.8.16-S2.4)
- Implementing secure monitoring infrastructure (access controls, encryption)

**Automation and Integration**:
- Developing automation scripts (alert enrichment, response playbooks)
- Integrating with Security Orchestration (SOAR) platforms
- Implementing automated containment actions (where appropriate)
- Creating custom integrations and tools
- Developing APIs for monitoring data access

**Performance Optimization**:
- Optimizing query performance
- Tuning indexing and storage
- Implementing caching and aggregation
- Monitoring infrastructure health (meta-monitoring)
- Troubleshooting performance issues

**Documentation**:
- Maintaining architecture diagrams
- Documenting integrations and configurations
- Creating runbooks for common issues
- Providing technical documentation for SOC

---

## 3.8 Threat Intelligence Team

### 3.8.1 Role Assignment

**Typical Roles**: Threat Intelligence Analyst, Cyber Threat Analyst  
**Team Lead**: Threat Intelligence Lead (may report to CISO or SOC Lead)

### 3.8.2 Responsibilities

Threat Intelligence Team is **RESPONSIBLE** for:

**Threat Intelligence Collection**:
- Consuming external threat intelligence feeds
- Participating in threat sharing communities (ISACs, CERTs)
- Monitoring threat actor campaigns and TTPs
- Collecting open-source intelligence (OSINT)
- Purchasing commercial threat intelligence (if budgeted)

**Threat Intelligence Integration**:
- Operationalizing threat intelligence (converting to detections)
- Providing IOCs to monitoring platforms (IPs, domains, hashes, URLs)
- Mapping threats to MITRE ATT&CK framework
- Enriching alerts with threat context
- Updating detection rules based on new TTPs

**Threat Analysis**:
- Analyzing threat actor motivations and capabilities
- Assessing organizational threat exposure (which threats are relevant?)
- Producing threat intelligence reports for stakeholders
- Conducting threat landscape briefings for management
- Supporting incident investigations with threat intelligence

**Detection Improvement**:
- Identifying detection gaps based on threat landscape
- Recommending new detection rules for emerging threats
- Validating detection coverage against known TTPs
- Participating in red team / purple team exercises

---

## 3.9 Incident Response Team

### 3.9.1 Role Assignment

**Typical Roles**: Incident Response Manager, Incident Handler, CSIRT Member  
**Team Lead**: Incident Response Manager (may report to CISO or separate CISO/CIO)

### 3.9.2 Responsibilities

Incident Response Team is **RESPONSIBLE** for:

**Incident Management**:
- Managing confirmed security incidents (per ISMS-POL-A.5.24-28)
- Coordinating containment, eradication, and recovery
- Making containment decisions (isolate systems, disable accounts)
- Coordinating with business stakeholders
- Managing incident communications

**Investigation**:
- Conducting detailed forensic investigation of incidents
- Determining root cause and attack timeline
- Identifying compromised accounts and systems
- Assessing data loss or impact
- Collecting evidence for legal proceedings (if needed)

**Coordination**:
- Coordinating with SOC (receiving escalations, providing updates)
- Coordinating with IT Operations (remediation execution)
- Coordinating with Legal/HR (data breaches, insider threats)
- Coordinating with external parties (law enforcement, regulators, customers)
- Coordinating with vendors (if vendor systems involved)

**Post-Incident Activities**:
- Conducting post-incident reviews (lessons learned)
- Documenting incident timelines and findings
- Recommending improvements to detection and response
- Updating incident response playbooks
- Reporting to CISO and management

**Integration with Monitoring**:
- Providing feedback to SOC on detection effectiveness (what was detected? what wasn't?)
- Requesting new detection rules based on incident TTPs
- Validating detection improvements
- Participating in tabletop exercises and simulations

---

## 3.10 System Owners

### 3.10.1 Role Assignment

**Typical Roles**: Application Owners, Database Administrators, System Administrators (for specific systems)  
**Identification**: Defined in asset inventory / CMDB

### 3.10.2 Responsibilities

System Owners are **ACCOUNTABLE** for:

**System Monitoring**:
- Ensuring their systems are monitored per policy requirements
- Coordinating with Security Engineering for log source onboarding
- Providing system context for baseline establishment
- Reviewing monitoring coverage for their systems annually

**Baseline Collaboration**:
- Providing input on normal system behavior (business cycles, maintenance windows)
- Reviewing proposed baselines for accuracy
- Notifying SOC of planned changes that affect baselines
- Approving baseline updates for their systems

**Alert Response**:
- Responding to security alerts affecting their systems
- Providing system-specific expertise during investigations
- Implementing remediation actions as directed by Incident Response
- Participating in post-incident reviews

**Compliance**:
- Ensuring system configurations support monitoring (logging enabled, logs forwarded)
- Maintaining system availability for monitoring integration
- Notifying Security Team of system decommissioning (remove from monitoring)

---

## 3.11 IT Operations

### 3.11.1 Role Assignment

**Typical Roles**: System Administrators, Network Administrators, IT Operations Engineers, Cloud Infrastructure Teams

### 3.11.2 Responsibilities

IT Operations is **RESPONSIBLE** for:

**Infrastructure Support**:
- Maintaining systems being monitored (patching, updates, availability)
- Configuring systems to generate logs (per ISMS-POL-A.8.15)
- Forwarding logs to monitoring platforms
- Maintaining network connectivity for log collection
- Supporting monitoring infrastructure deployment

**Incident Remediation**:
- Executing remediation actions directed by Incident Response
- Isolating compromised systems
- Rebuilding compromised systems
- Restoring from backups
- Implementing security improvements post-incident

**Change Coordination**:
- Notifying Security Team of infrastructure changes (new systems, network changes)
- Coordinating maintenance windows with SOC (avoid baseline confusion)
- Testing changes in dev/staging before production
- Documenting changes for monitoring team awareness

---

## 3.12 Legal and Compliance

### 3.12.1 Role Assignment

**Typical Roles**: General Counsel, Legal Counsel, Compliance Officer, Data Protection Officer (DPO)

### 3.12.2 Responsibilities

Legal and Compliance is **RESPONSIBLE** for:

**Regulatory Compliance**:
- Advising on legal requirements for monitoring and log retention
- Ensuring monitoring practices comply with privacy laws (GDPR, FADP)
- Reviewing monitoring scope and data collection for legal compliance
- Conducting or reviewing Data Protection Impact Assessments (DPIA)

**Retention and Privacy**:
- Defining legal retention requirements (per ISMS-POL-A.8.16-S2.4)
- Approving retention periods
- Managing legal holds on monitoring data
- Handling data subject requests (access, erasure)

**Incident Support**:
- Advising on legal implications of security incidents
- Managing breach notification requirements (GDPR, sector-specific)
- Coordinating with law enforcement
- Managing litigation holds
- Protecting attorney-client privilege during investigations

---

## 3.13 Internal Audit and Risk Management

### 3.13.1 Role Assignment

**Typical Roles**: Internal Auditors, Risk Managers, Compliance Auditors

### 3.13.2 Responsibilities

Audit and Risk Management is **RESPONSIBLE** for:

**Independent Verification**:
- Auditing monitoring controls for effectiveness
- Verifying policy compliance
- Testing detection capabilities (red team coordination)
- Reviewing exception management
- Validating baseline documentation

**Risk Assessment**:
- Including monitoring capabilities in enterprise risk assessments
- Evaluating residual detection risks
- Tracking risk metrics (detection rate, MTTD, coverage gaps)
- Recommending risk treatments

**Compliance Auditing**:
- Verifying ISO 27001:2022 Control A.8.16 implementation
- Supporting external audits (certification, regulatory)
- Reviewing audit findings and tracking remediation
- Ensuring documentation is audit-ready

**Reporting**:
- Reporting audit findings to senior management and board
- Providing independent assessment of SOC maturity
- Recommending improvements
- Tracking remediation progress

---

## 3.14 Executive Management

### 3.14.1 Role Assignment

**Typical Roles**: CEO, CIO, CFO, Board of Directors

### 3.14.2 Responsibilities

Executive Management is **ACCOUNTABLE** for:

**Governance**:
- Setting organizational risk appetite for undetected threats
- Approving monitoring strategy and budget
- Allocating resources for SOC operations
- Holding CISO accountable for monitoring effectiveness

**Risk Acceptance**:
- Accepting residual risks (monitoring gaps, limited coverage)
- Approving high-risk exceptions escalated by CISO
- Understanding and accepting limitations of detection
- Reviewing risk reports

**Oversight**:
- Reviewing periodic SOC metrics and effectiveness reports
- Ensuring compliance with legal and regulatory monitoring requirements
- Supporting security initiatives and SOC improvements
- Championing security culture

**Incident Escalation**:
- Serving as ultimate escalation point for critical incidents
- Authorizing emergency response actions
- Approving communications to external parties (regulators, media, customers)
- Ensuring lessons learned are implemented

---

## 3.15 End Users

### 3.15.1 Responsibilities

All employees and contractors are **RESPONSIBLE** for:

**Awareness**:
- Understanding that organizational systems are monitored
- Accepting monitoring as security control (no expectation of privacy on corporate systems)
- Following acceptable use policies

**Reporting**:
- Reporting suspected security incidents to Security Team / Help Desk
- Cooperating with security investigations
- Providing context during alert investigation (if contacted by SOC)

**Compliance**:
- Complying with security policies
- Not attempting to disable or circumvent monitoring
- Understanding monitoring is for security, not performance management

---

## 3.16 Responsibility Matrix (RACI)

The following table summarizes key responsibilities across roles:

| Activity | CISO | SOC Lead | SOC T1/T2 | SecEng | ThreatIntel | IR Team | SysOwner | Legal | Audit |
|----------|------|----------|-----------|--------|-------------|---------|----------|-------|-------|
| Define monitoring policy | A | R/C | C | C | C | C | I | C | I |
| Deploy monitoring infrastructure | I | C | I | A/R | I | I | C | I | I |
| Establish baselines | C | A | R | C | I | I | C | I | I |
| Develop detection rules | C | A | R | C | R | C | I | I | I |
| Monitor alerts 24/7 | I | A | R | I | I | I | I | I | I |
| Triage alerts | I | A | R | I | C | I | I | I | I |
| Investigate incidents | C | C | R | C | R | A/R | R | C | I |
| Escalate to IR | I | R | R | I | I | A | I | I | I |
| Tune detection rules | C | A | R | C | C | C | I | I | I |
| Approve monitoring exceptions | A | R | I | C | I | I | R | C | I |
| Define retention periods | A | C | I | R | I | I | I | A/R | C |
| Conduct audit | C | C | C | C | C | C | C | C | A/R |
| Accept residual risk | A | C | I | I | I | I | I | C | I |

**Legend**: A = Accountable, R = Responsible, C = Consulted, I = Informed, - = Not involved

---

## 3.17 Role Transitions and Handovers

### 3.17.1 Personnel Changes

When personnel change roles affecting monitoring responsibilities:

**Departing Personnel**:
- Document current state (in-progress investigations, pending baselines, detection rules)
- Transfer knowledge to successor (system-specific quirks, tribal knowledge)
- Complete handover checklist
- Revoke access to monitoring systems

**New Personnel**:
- Complete role-specific training (SOC procedures, investigation playbooks, tools)
- Obtain necessary access (SIEM, ticketing, alert systems)
- Shadow predecessor or experienced team member
- Review documentation (baselines, detection rules, procedures)

### 3.17.2 Organizational Changes

When organizational structure changes:

- Review and update role assignments
- Ensure no responsibilities are orphaned (especially for system owners)
- Document any role consolidations and compensating controls
- Communicate changes to all stakeholders
- Update this policy section (S3) as needed

---

## 3.18 Accountability and Escalation

### 3.18.1 Performance Accountability

Role performance is measured through:

- Monitoring metrics (MTTD, MTTR, false positive rate, detection rate)
- Incident outcomes (effective response, containment time, lessons learned)
- Audit findings (baseline documentation, detection coverage, SLA compliance)
- Quality metrics (alert quality, investigation thoroughness)
- Continuous improvement contributions (new detections, process improvements)

### 3.18.2 Escalation Paths

**Technical Escalation** (skill/complexity):
- SOC Tier 1 → Tier 2 → Tier 3 → Security Engineering → External Experts

**Incident Escalation** (severity):
- SOC → Incident Response → CISO → Executive Management

**Timeline for Critical Incidents**:
- SOC to IR: Immediate (alert escalation)
- IR to CISO: Within 1 hour
- CISO to Exec Management: Within 4 hours (if significant business impact)
- Exec Management to Board: Within 24 hours (if material impact)

**Policy/Risk Escalation**:
- System Owner → SOC Lead → CISO → Executive Management
- Security Engineering → CISO → Executive Management

---

**END OF DOCUMENT**

---

## Related Documents in Framework

- **ISMS-POL-A.8.16-S1** (Purpose, Scope, Definitions) - Foundation
- **ISMS-POL-A.8.16-S2.x** (Requirements) - What these roles must accomplish
- **ISMS-POL-A.8.16-S4** (Policy Governance) - How roles govern this policy
- **ISMS-POL-A.8.16-S5.C** (Alert Response Procedures) - SOC operational procedures
- **ISMS-POL-A.5.24-28** (Incident Management) - IR Team detailed responsibilities

---

*"Clear roles prevent finger-pointing. Clear accountability prevents dropped balls. Clear escalation prevents disasters."*  
*—Security Operations Wisdom*