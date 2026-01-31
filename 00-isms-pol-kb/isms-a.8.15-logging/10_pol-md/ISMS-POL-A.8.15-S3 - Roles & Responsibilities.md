# ISMS-POL-A.8.15-S3
## Logging - Roles & Responsibilities

**Document ID**: ISMS-POL-A.8.15-S3  
**Title**: Logging - Roles & Responsibilities  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager / HR | Initial roles and responsibilities |

**Review Cycle**: Annual (or upon organizational structure changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- HR Review: Human Resources Director
- Management Review: IT Director / CIO

**Distribution**: All personnel with logging responsibilities, HR, management  
**Related Documents**: ISMS-POL-A.8.15 (Master), Job Descriptions, RACI Matrix

---

## 3.1 Governance Model

### 3.1.1 Oversight Structure

**Executive Oversight**:
- **Chief Information Security Officer (CISO)**: Ultimate accountability for logging program
- **Security Steering Committee**: Quarterly review of logging effectiveness and compliance
- **Executive Management**: Annual review of security posture including logging capabilities

**Operational Management**:
- **Information Security Manager**: Day-to-day management of logging policy and standards
- **SOC Lead**: Management of log analysis and incident detection
- **IT Operations Manager**: Management of log infrastructure and collection

### 3.1.2 Decision Authority

**Policy Decisions**: CISO with input from Legal/Compliance
**Technical Standards**: Information Security Manager with Security Architect
**Operational Procedures**: SOC Lead and IT Operations Manager
**Exception Approvals**: CISO (or designated deputy for non-critical exceptions)

---

## 3.2 RACI Matrix

### 3.2.1 RACI Definitions

- **R (Responsible)**: Performs the work
- **A (Accountable)**: Ultimate accountability, decision authority (only one A per task)
- **C (Consulted)**: Provides input, two-way communication
- **I (Informed)**: Kept informed, one-way communication

### 3.2.2 Logging Lifecycle RACI

| Activity | CISO | Info Sec Mgr | SOC Lead | IT Ops Mgr | System Owner | Log Admin | SOC Analyst | Legal |
|----------|------|--------------|----------|------------|--------------|-----------|-------------|-------|
| **Policy Development** | A | R | C | C | I | I | I | C |
| **Standards Definition** | A | R | C | C | C | I | I | I |
| **Log Source Identification** | I | C | C | C | R | I | I | I |
| **Log Collection Configuration** | I | C | I | R | C | R | I | I |
| **Log Infrastructure Management** | I | C | C | A | I | R | I | I |
| **Log Review (Daily)** | I | I | C | I | I | I | R | I |
| **Log Analysis (Automated)** | I | C | A | I | I | R | R | I |
| **Incident Investigation** | I | C | A | C | C | I | R | I |
| **Retention Compliance** | A | C | I | R | C | R | I | C |
| **Exception Approval** | A | C | I | I | I | I | I | C |
| **Audit Support** | A | R | C | C | C | C | C | C |

---

## 3.3 Role Definitions

### 3.3.1 Chief Information Security Officer (CISO)

**Accountability**: Ultimate responsibility for logging program effectiveness and compliance

**Responsibilities**:
- Approve logging policy and standards
- Allocate resources for logging infrastructure and personnel
- Review quarterly logging effectiveness reports
- Approve exceptions to logging requirements
- Ensure regulatory compliance
- Report to executive management on security posture

**Authority**:
- Final decision on logging policy
- Budget approval for logging investments
- Risk acceptance for logging gaps

**Competencies**: Executive leadership, risk management, regulatory compliance

**Time Commitment**: 2-4 hours/month (policy review, management reporting)

---

### 3.3.2 Information Security Manager

**Accountability**: Day-to-day management of logging policy, standards, and compliance

**Responsibilities**:
- Develop and maintain logging policy and standards
- Coordinate logging implementation across organization
- Conduct quarterly compliance assessments
- Manage logging exceptions and risk acceptance process
- Provide technical guidance to IT and SOC teams
- Report to CISO on logging program status
- Coordinate with Legal/Compliance on regulatory requirements

**Authority**:
- Define technical logging standards
- Approve minor policy updates
- Grant temporary exceptions (with CISO notification)

**Competencies**: Security architecture, policy development, log management technologies, regulatory knowledge

**Time Commitment**: 20-40% of full-time role

---

### 3.3.3 Security Operations Center (SOC) Lead

**Accountability**: Management of log analysis, monitoring, and incident detection

**Responsibilities**:
- Manage SOC analyst team
- Oversee daily log review and analysis
- Develop and maintain detection use cases
- Tune SIEM correlation rules and alerts
- Manage incident response activities
- Report on detection effectiveness metrics
- Coordinate with Incident Response Team
- Train SOC analysts on log analysis

**Authority**:
- Prioritize SOC workload and resources
- Escalate incidents per incident response policy
- Request additional log sources for detection coverage

**Competencies**: Security operations, SIEM administration, threat detection, team management

**Time Commitment**: Full-time role

---

### 3.3.4 IT Operations Manager

**Accountability**: Management of log collection infrastructure and reliability

**Responsibilities**:
- Manage log collection infrastructure (log forwarders, SIEM ingest)
- Ensure log collection reliability (uptime, completeness)
- Plan and manage log storage capacity
- Coordinate system owner compliance with logging requirements
- Manage log infrastructure performance and scaling
- Implement log retention and archival processes
- Support SOC with infrastructure troubleshooting

**Authority**:
- Allocate IT resources for log infrastructure
- Approve infrastructure changes
- Coordinate system maintenance windows

**Competencies**: IT operations, storage management, infrastructure architecture, capacity planning

**Time Commitment**: 10-20% of full-time role (varies with infrastructure maturity)

---

### 3.3.5 System Owner

**Accountability**: Ensure systems generate and forward appropriate logs

**Responsibilities**:
- Configure systems to generate required log events (per S2.1)
- Implement log forwarding to centralized log management
- Maintain system logging configuration during updates/changes
- Notify Log Administrator of new systems requiring log collection
- Support incident investigations with system-specific expertise
- Complete log source inventory assessments (ISMS-IMP-A.8.15.1)

**Authority**:
- System configuration within organizational policies
- Request logging exceptions with business justification

**Competencies**: System administration, application support, system-specific logging configuration

**Time Commitment**: 2-4 hours/month per system (initial configuration + ongoing maintenance)

---

### 3.3.6 Log Administrator

**Accountability**: Management of centralized log management platform (SIEM)

**Responsibilities**:
- Configure log collection from sources
- Manage SIEM platform (health, performance, updates)
- Create and maintain log parsing rules
- Implement log retention policies
- Manage user access to SIEM
- Troubleshoot log collection issues
- Support SOC analysts with SIEM queries
- Perform log integrity checks
- Manage log archival and disposal

**Authority**:
- SIEM configuration and administration
- Log collection troubleshooting
- User access provisioning (with approval)

**Competencies**: SIEM administration, log parsing, storage management, scripting

**Time Commitment**: Full-time role (for mature logging programs) or 20-40% (smaller organizations)

**Separation of Duties**: Log Administrator SHALL NOT have administrative access to systems being logged (see S2.2.6)

---

### 3.3.7 SOC Analyst / Security Analyst

**Accountability**: Daily log review, alert triage, and incident investigation

**Responsibilities**:
- Conduct daily log review per procedures (S5.C)
- Monitor SIEM alerts and dashboards
- Triage security alerts (true positive vs. false positive)
- Investigate security incidents using log analysis
- Document findings in incident tickets
- Escalate incidents per incident response procedures
- Tune detection rules to reduce false positives
- Provide feedback on detection effectiveness

**Authority**:
- Initiate incident investigations
- Escalate incidents to Incident Response Team
- Request additional log data for investigations

**Competencies**: Log analysis, threat detection, incident investigation, SIEM querying

**Time Commitment**: Full-time role(s) (24x7 coverage for mature SOCs)

---

### 3.3.8 Security Architect / Security Engineer

**Accountability**: Design and implementation of logging and detection capabilities

**Responsibilities**:
- Design log collection architecture
- Develop technical logging standards
- Create SIEM correlation rules and use cases
- Implement automated analysis capabilities
- Integrate new log sources into SIEM
- Develop custom parsing rules
- Optimize log collection and analysis performance
- Support SOC with advanced analytics

**Authority**:
- Technical architecture decisions
- Tool selection recommendations
- Standards development

**Competencies**: Security architecture, SIEM engineering, scripting/development, data analysis

**Time Commitment**: 20-40% of full-time role

---

### 3.3.9 Incident Response Manager / Team

**Accountability**: Investigation and resolution of security incidents

**Responsibilities**:
- Lead major incident investigations
- Coordinate incident response activities
- Leverage logs for forensic analysis
- Document incident timeline using logs
- Provide feedback on detection gaps
- Update incident response procedures

**Authority**:
- Incident command during active incidents
- Request emergency access to systems/logs
- Coordinate with external parties (law enforcement, forensics vendors)

**Competencies**: Incident response, forensic analysis, crisis management

**Time Commitment**: On-call basis for incidents (full-time during active incidents)

---

### 3.3.10 Legal Counsel / Compliance Officer

**Accountability**: Interpret legal and regulatory logging requirements

**Responsibilities**:
- Advise on regulatory retention requirements
- Review logging policies for legal compliance
- Manage legal hold procedures
- Approve data subject deletion requests (GDPR)
- Support audit and regulatory examinations
- Advise on privacy considerations in logging

**Authority**:
- Legal interpretation of regulations
- Approve/deny data deletion requests
- Initiate/release legal holds

**Competencies**: Legal expertise, regulatory knowledge, privacy law, data protection

**Time Commitment**: Consultative (as needed)

---

### 3.3.11 Internal Audit / Compliance Audit

**Accountability**: Independent verification of logging policy compliance

**Responsibilities**:
- Conduct periodic audits of logging program
- Verify compliance with policy requirements
- Review log access controls and integrity
- Validate retention compliance
- Report findings to management and CISO
- Track remediation of audit findings

**Authority**:
- Audit access to systems and logs
- Report compliance issues to Audit Committee

**Competencies**: Audit methodology, IT controls, regulatory frameworks

**Time Commitment**: Annual audit cycle (1-2 weeks of effort)

---

### 3.3.12 Records Management Officer

**Accountability**: Oversight of log retention and disposal compliance

**Responsibilities**:
- Coordinate logging retention with records retention policy
- Ensure disposal procedures comply with records management standards
- Manage legal hold coordination
- Maintain retention schedule documentation

**Authority**:
- Records management policy interpretation
- Retention schedule approval

**Competencies**: Records management, information governance

**Time Commitment**: Consultative (integration with records management program)

---

## 3.4 Escalation Paths

### 3.4.1 Technical Issues

**Log Collection Failures**:
System Owner → Log Administrator → IT Operations Manager → Information Security Manager

**SIEM Performance Issues**:
Log Administrator → IT Operations Manager → Information Security Manager

**Detection Coverage Gaps**:
SOC Analyst → SOC Lead → Information Security Manager → CISO

### 3.4.2 Security Incidents

**Low/Medium Severity**:
SOC Analyst → SOC Lead (investigation and resolution)

**High Severity**:
SOC Analyst → SOC Lead → Incident Response Manager → Information Security Manager (notify)

**Critical Severity**:
SOC Analyst → SOC Lead → Incident Response Manager → Information Security Manager → CISO → Executive Management (immediate notification)

### 3.4.3 Policy Exceptions

**Standard Exception Request**:
Requestor → System Owner → Information Security Manager → CISO (approval)

**Emergency Exception**:
Requestor → On-Call Security Manager → CISO (immediate approval), followed by formal documentation

---

## 3.5 Competency Requirements

### 3.5.1 Minimum Competencies by Role

**SOC Analyst**:
- Understanding of common attack vectors and TTPs
- Log analysis fundamentals
- SIEM query language proficiency
- Incident investigation methodology
- **Certifications** (preferred): Security+, GCIA, GCIH, vendor SIEM certifications

**Log Administrator**:
- SIEM platform administration
- Log parsing and normalization
- Storage and capacity management
- Scripting (Python, PowerShell, Bash)
- **Certifications** (preferred): Vendor SIEM certifications, Linux/Windows administration

**Security Engineer**:
- Security architecture principles
- Data analysis and statistics
- Scripting and development
- SIEM platform engineering
- **Certifications** (preferred): CISSP, GCIA, vendor SIEM architect certifications

**Information Security Manager**:
- Security program management
- Risk management frameworks
- Regulatory compliance (ISO 27001, GDPR, sector-specific)
- Policy development
- **Certifications** (required): CISSP, CISM, or equivalent

### 3.5.2 Training Requirements

**Initial Training** (for new personnel):
- Logging policy and procedures: 4 hours
- SIEM platform training: 1-2 weeks (vendor-provided or internal)
- Role-specific training: 1-2 weeks

**Ongoing Training**:
- Annual policy review: 2 hours/year
- Quarterly threat briefings: 1 hour/quarter
- New tool/capability training: As needed

**Certification Maintenance**:
- Support for certification renewals (CPE credits, exam fees)
- Annual training budget per security team member

---

## 3.6 Resource Requirements

### 3.6.1 Personnel Requirements

Organizations **SHOULD** allocate personnel based on:

**Small Organization** (<500 employees, <50 servers):
- 1 FTE: Combined Log Administrator + SOC Analyst (daytime coverage)
- 0.2 FTE: Information Security Manager (part-time oversight)
- On-call rotation for after-hours incidents

**Medium Organization** (500-2000 employees, 50-200 servers):
- 2-3 FTE: SOC Analysts (8x5 or 16x5 coverage)
- 1 FTE: Log Administrator
- 1 FTE: SOC Lead / Information Security Manager
- On-call rotation for after-hours

**Large Organization** (>2000 employees, >200 servers):
- 6-12 FTE: SOC Analysts (24x7 coverage, follow-the-sun or shift rotation)
- 2-3 FTE: Log Administrators
- 1-2 FTE: Security Engineers (SIEM/detection engineering)
- 1 FTE: SOC Manager
- 1 FTE: Information Security Manager
- 24x7 on-call Incident Response capability

### 3.6.2 Tool and Infrastructure Requirements

- SIEM or log management platform (licensing, infrastructure)
- Log storage (hot, warm, cold tiers)
- Log forwarders/collectors (agents on all systems)
- Threat intelligence feeds
- Ticketing/case management system
- Security orchestration platform (optional, for automation)

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-POL-A.8.15-S3 |
| **ISO 27001:2022 Control** | Annex A Control 8.15 (Logging) |
| **Document Type** | Policy Section - Roles & Responsibilities |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Line Count** | ~295 lines |
| **Parent Policy** | ISMS-POL-A.8.15 (Master) |

---

**END OF SECTION S3**