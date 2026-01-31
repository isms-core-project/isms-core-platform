# ISMS-POL-A.8.15 Logging
## Comprehensive Policy & Implementation Framework

**Document ID**: ISMS-POL-A.8.15  
**Title**: Logging Policy  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Information Security Manager | Initial policy framework |

**Review Cycle**: Annual (or upon significant changes to logging infrastructure, regulations, or security incidents)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Information Security Manager / IT Operations Manager
- Operational Review: Security Operations Center (SOC) Lead
- Compliance Review: Legal/Compliance Officer (for data retention and privacy)

**Distribution**: All IT staff, system owners, security team, audit team, management  
**Related Policies**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.8.16 (Monitoring Activities)
- ISMS-POL-A.8.17 (Clock Synchronization)
- Incident Response Policy
- Data Retention Policy
- Privacy Policy

---

## Table of Contents

1. Executive Summary
2. Policy Framework Structure
3. Section Overview (S1-S5)
4. Quick Reference Matrix
5. Compliance & Audit
6. Policy Governance
7. Approval & Sign-Off

---

## 1. Executive Summary

### 1.1 Purpose

This policy establishes the organization's requirements for **event logging** to support:

- Detection and investigation of information security incidents
- Compliance with legal, regulatory, and contractual obligations
- Accountability for user and administrator actions
- Forensic analysis and evidence collection
- Performance monitoring and capacity planning
- Audit trail requirements

**ISO 27001:2022 Alignment**: This policy implements Control A.8.15 (Logging) as specified in ISO/IEC 27001:2022 Annex A and ISO/IEC 27002:2022 Section 8.15.

### 1.2 Scope

**In Scope**:
- All information systems, applications, and infrastructure components
- Network devices (routers, switches, firewalls, load balancers)
- Security tools (SIEM, IDS/IPS, anti-malware, DLP, web filters)
- Database systems and data storage platforms
- Cloud services and SaaS applications
- Administrative and privileged access activities
- Authentication and access control systems

**Out of Scope**:
- Business application audit trails (covered by application-specific policies)
- Financial transaction logs (covered by financial controls)
- Clinical/medical record access logs (covered by healthcare-specific policies, if applicable)
- Real-time monitoring and alerting processes (covered by ISMS-POL-A.8.16 - Monitoring Activities)

### 1.3 Regulatory Framework

This policy framework demonstrates compliance with:

**Mandatory Compliance** (refer to ISMS-POL-00 for authoritative interpretation):
- ISO/IEC 27001:2022 Annex A Control 8.15 (certification requirement)
- Swiss Federal Data Protection Act (FADP) - Art. 8 (data security obligations)
- EU General Data Protection Regulation (GDPR) - Art. 32(1)(d) (where applicable to EU data processing)

**Conditional Applicability** (when organization falls within scope):
- Digital Operational Resilience Act (DORA) - Art. 17 (ICT-related incident management)
- NIS2 Directive - Art. 21 (cybersecurity risk management measures)
- PCI DSS 4.0 - Requirement 10 (if processing payment card data)
- HIPAA Security Rule - 45 CFR § 164.312(b) (if handling US healthcare data)

**Informational Reference / Best Practice Alignment**:
- NIST SP 800-92 (Guide to Computer Security Log Management)
- CIS Controls v8 - Control 8 (Audit Log Management)
- ISO/IEC 27002:2022 - Section 8.15 (implementation guidance)

**Note**: For questions about regulatory applicability, refer to **ISMS-POL-00 (Regulatory Applicability Framework)**, which provides authoritative interpretation of all compliance obligations.

### 1.4 Key Principles

**Principle 1: Comprehensive Logging**  
*"What isn't logged, can't be investigated."*  
All security-relevant events SHALL be logged across systems, applications, and infrastructure.

**Principle 2: Log Integrity**  
*"A log you can't trust is worse than no log at all."*  
Logs SHALL be protected from unauthorized modification or deletion. As Feynman warned: "The first principle is that you must not fool yourself."

**Principle 3: Timely Review**  
*"Logs aren't write-only storage."*  
Logs SHALL be regularly reviewed, both manually and through automated analysis, to detect anomalies and incidents.

**Principle 4: Appropriate Retention**  
*"Storage is cheap, but compliance violations aren't."*  
Logs SHALL be retained according to regulatory requirements, business needs, and legal obligations.

**Principle 5: Privacy by Design**  
*"Log what you need, protect what you log."*  
Logging SHALL balance security requirements with privacy obligations, minimizing collection of personal data where possible.

**Principle 6: No Cargo Cult Logging**  
*"We log because we understand WHY, not just because ISO says so."*  
Every logging requirement SHALL have a clear security or compliance justification.

### 1.5 Policy Framework Overview

This policy is structured as a modular framework for maintainability and clarity:
```
ISMS-POL-A.8.15 (This Document - Master Policy)
├── Section 1 (S1): Purpose, Scope, Definitions
├── Section 2 (S2): Requirements (broken into subsections)
│   ├── S2.1: Event Logging Requirements
│   ├── S2.2: Log Protection & Integrity
│   ├── S2.3: Log Retention & Storage
│   └── S2.4: Log Review & Analysis
├── Section 3 (S3): Roles & Responsibilities
├── Section 4 (S4): Policy Governance
└── Section 5 (S5): Annexes
    ├── S5.A: Logging Standards (technical specifications)
    ├── S5.B: Log Source Template
    ├── S5.C: Log Review Procedures
    └── S5.D: Quick Reference Guide
```

**Document Navigation**: Each section is a standalone document that can be read independently while maintaining consistency with the overall framework.

---

## 2. Policy Framework Structure

### 2.1 Core Policy Sections

The following sections constitute the complete logging policy framework:

#### **ISMS-POL-A.8.15-S1: Purpose, Scope, Definitions**
Establishes the foundation, scope boundaries, regulatory context, and key terminology.

**Key Topics**:
- Detailed purpose and objectives
- Scope boundaries (what's in/out)
- Regulatory applicability analysis
- Definitions and glossary
- Document structure and navigation

**Target Audience**: All stakeholders, auditors, new employees

---

#### **ISMS-POL-A.8.15-S2: Requirements Overview**
High-level summary of all logging requirements organized by domain.

**Key Topics**:
- Requirement categories (event logging, protection, retention, review)
- SHALL/SHOULD/MAY requirement summary
- Cross-references to detailed subsections (S2.1 - S2.4)
- Requirement applicability matrix

**Target Audience**: Policy implementers, system owners, auditors

---

#### **ISMS-POL-A.8.15-S2.1: Event Logging Requirements**
Detailed requirements for WHAT to log, WHERE to log it, and HOW to structure log events.

**Key Topics**:
- Mandatory log events (authentication, access, changes, errors, security events)
- System-specific logging requirements (OS, databases, applications)
- Network device logging requirements
- Security tool logging requirements
- Log content standards (timestamp, user ID, action, outcome, source)
- Log format specifications (syslog, CEF, JSON)

**Target Audience**: System administrators, application developers, security engineers

**Implementation Evidence**: ISMS-IMP-A.8.15.1 (Log Source Inventory Assessment)

---

#### **ISMS-POL-A.8.15-S2.2: Log Protection & Integrity**
Requirements for protecting logs from unauthorized access, modification, and deletion.

**Key Topics**:
- Access control requirements (who can view/manage logs)
- Integrity protection mechanisms (write-once storage, digital signatures, hashing)
- Tamper detection and alerting
- Secure log transmission (encryption in transit)
- Separation of duties (log administrators vs. system administrators)
- Protection from malicious insiders

**Target Audience**: Security engineers, SOC analysts, IT operations

**Implementation Evidence**: ISMS-IMP-A.8.15.3 (Log Protection & Retention Assessment)

---

#### **ISMS-POL-A.8.15-S2.3: Log Retention & Storage**
Requirements for HOW LONG to retain logs and WHERE/HOW to store them.

**Key Topics**:
- Retention periods by log type (security logs, authentication, administrative, application)
- Storage tier architecture (hot storage, warm storage, cold archive)
- Archival procedures and format standards
- Disposal procedures (secure deletion after retention period)
- Legal hold procedures (suspension of disposal for investigations/litigation)
- Storage capacity planning and scalability

**Target Audience**: IT operations, storage administrators, legal/compliance

**Implementation Evidence**: ISMS-IMP-A.8.15.3 (Log Protection & Retention Assessment)

---

#### **ISMS-POL-A.8.15-S2.4: Log Review & Analysis**
Requirements for reviewing, analyzing, and acting upon logged events.

**Key Topics**:
- Manual review schedules (daily, weekly, monthly)
- Automated analysis requirements (SIEM correlation rules, anomaly detection)
- Alert configuration and escalation
- Investigation procedures
- Reporting requirements (to management, regulators, auditors)
- Key Performance Indicators (KPIs) for logging effectiveness
- Integration with incident response processes

**Target Audience**: SOC analysts, security engineers, incident responders

**Implementation Evidence**: ISMS-IMP-A.8.15.4 (Log Analysis & Review Assessment)

---

#### **ISMS-POL-A.8.15-S3: Roles & Responsibilities**
Defines who is responsible and accountable for logging activities.

**Key Topics**:
- Governance model and organizational structure
- RACI matrix (Responsible, Accountable, Consulted, Informed)
- Role definitions (Log Administrator, System Owner, SOC Analyst, etc.)
- Escalation paths and decision authority
- Competency requirements and training
- Separation of duties requirements

**Target Audience**: Management, HR, system owners, security team

---

#### **ISMS-POL-A.8.15-S4: Policy Governance**
Establishes how the policy itself is managed, updated, and governed.

**Key Topics**:
- Policy lifecycle (development, approval, publication, review, retirement)
- Version control and change management
- Approval workflow and authority
- Policy distribution and training
- Periodic review schedule
- Exception management process
- Integration with broader ISMS

**Target Audience**: CISO, policy authors, compliance team

---

#### **ISMS-POL-A.8.15-S5: Annexes**
Supporting materials, templates, and detailed technical specifications.

##### **S5.A: Logging Standards**
Technical specifications for log formats, protocols, and configurations.

**Contents**:
- Syslog protocol configuration (RFC 5424)
- Common Event Format (CEF) specification
- JSON logging standards
- Timestamp format standards (ISO 8601)
- Time synchronization requirements (NTP)

##### **S5.B: Log Source Template**
Standardized template for documenting new log sources added to the environment.

**Contents**:
- Log source identification form
- Required fields (system name, log type, format, volume, retention)
- Integration checklist
- Approval workflow

##### **S5.C: Log Review Procedures**
Detailed operational procedures for log review activities.

**Contents**:
- Daily review procedures (what to check, how to escalate)
- Weekly review procedures (trend analysis, capacity planning)
- Monthly review procedures (effectiveness assessment, reporting)
- Incident response procedures (forensic log analysis)
- Forensic investigation procedures (chain of custody, evidence handling)

##### **S5.D: Quick Reference Guide**
Practical guidance for common scenarios and decision-making.

**Contents**:
- Decision trees (when to log, what retention period to use)
- Common scenarios and solutions
- Troubleshooting guide (missing logs, storage issues, performance problems)
- FAQ (frequently asked questions)

**Target Audience**: All stakeholders (operational reference)

---

## 3. Section Overview (Summary)

| Section | Document ID | Purpose | Lines | Audience |
|---------|-------------|---------|-------|----------|
| **Master** | ISMS-POL-A.8.15 | Policy framework overview | ~400 | All |
| **S1** | ISMS-POL-A.8.15-S1 | Purpose, Scope, Definitions | ~300 | All |
| **S2** | ISMS-POL-A.8.15-S2 | Requirements Overview | ~300 | Implementers |
| **S2.1** | ISMS-POL-A.8.15-S2.1 | Event Logging Requirements | ~350 | Admins, Devs |
| **S2.2** | ISMS-POL-A.8.15-S2.2 | Log Protection & Integrity | ~350 | Security Team |
| **S2.3** | ISMS-POL-A.8.15-S2.3 | Retention & Storage | ~350 | IT Ops, Legal |
| **S2.4** | ISMS-POL-A.8.15-S2.4 | Review & Analysis | ~350 | SOC, Analysts |
| **S3** | ISMS-POL-A.8.15-S3 | Roles & Responsibilities | ~300 | Management |
| **S4** | ISMS-POL-A.8.15-S4 | Policy Governance | ~300 | CISO, Compliance |
| **S5** | ISMS-POL-A.8.15-S5 | Annexes Overview | ~250 | All |
| **S5.A** | ISMS-POL-A.8.15-S5.A | Logging Standards | ~350 | Engineers |
| **S5.B** | ISMS-POL-A.8.15-S5.B | Log Source Template | ~300 | System Owners |
| **S5.C** | ISMS-POL-A.8.15-S5.C | Log Review Procedures | ~350 | SOC, IT Ops |
| **S5.D** | ISMS-POL-A.8.15-S5.D | Quick Reference Guide | ~300 | All |

**Total Framework**: 14 documents, ~4,700 lines

---

## 4. Quick Reference Matrix

### 4.1 Requirement Summary (SHALL/SHOULD/MAY)

| Requirement Domain | SHALL (Mandatory) | SHOULD (Expected) | MAY (Optional) |
|-------------------|-------------------|-------------------|----------------|
| **Event Logging** | Authentication events, access to sensitive data, privilege escalation, security events, errors/failures, administrative actions | Application transactions, data exports, configuration queries | Performance metrics, debug logs |
| **Log Protection** | Access controls, integrity mechanisms, tamper alerting, encrypted transmission | Digital signatures, WORM storage, centralized collection | Blockchain-based immutability |
| **Retention** | Security logs 12mo, Authentication 12mo, comply with legal requirements | Hot storage 6-12mo, warm storage 1-3yr, cold archive 3-7yr | Extended retention beyond minimum |
| **Review & Analysis** | Critical alerts within 15min, daily review of security events, monthly reporting | Automated correlation, anomaly detection, weekly trend analysis | AI/ML-based analytics, predictive analysis |

### 4.2 Log Source Checklist

| System Type | Examples | Logging Required? | Retention Minimum |
|------------|----------|-------------------|-------------------|
| Operating Systems | Windows, Linux, macOS | YES (security events, auth, admin) | 12 months |
| Network Devices | Routers, switches, firewalls | YES (config changes, auth, rules) | 12 months |
| Security Tools | SIEM, IDS/IPS, AV, DLP, WAF | YES (all alerts and blocks) | 12 months |
| Databases | SQL Server, Oracle, PostgreSQL | YES (auth, queries, schema changes) | 12 months |
| Applications | Custom apps, COTS, SaaS | YES (if sensitive data/access control) | 6-12 months |
| Cloud Services | AWS, Azure, GCP, M365 | YES (IAM, data access, config) | 12 months |
| Authentication | AD, LDAP, SSO, MFA | YES (all authentication attempts) | 12 months |
| Web Servers | Apache, IIS, nginx | SHOULD (access logs, errors) | 6 months |

### 4.3 Common Scenarios Decision Tree

**Scenario: "Do I need to log this?"**
```
Is it related to security (auth, access, changes)?
├─ YES → LOG IT (SHALL)
└─ NO → Is it business-critical or compliance-required?
    ├─ YES → LOG IT (SHOULD)
    └─ NO → Is it useful for troubleshooting?
        ├─ YES → LOG IT (MAY)
        └─ NO → Don't log it (reduces noise)
```

**Scenario: "How long do I keep these logs?"**
```
Are these security/authentication logs?
├─ YES → 12 months minimum (hot), 7 years archive
└─ NO → Are there regulatory requirements?
    ├─ YES → Follow regulatory minimum
    └─ NO → 6 months minimum (hot), 1 year archive
```

---

## 5. Compliance & Audit

### 5.1 Mandatory Requirements

This policy framework demonstrates compliance with:

**Primary Standards**:
- ISO/IEC 27001:2022 Annex A Control 8.15
- ISO/IEC 27002:2022 Control 8.15 (implementation guidance)

**Regulatory Alignment** (refer to ISMS-POL-00 for definitive applicability):
- Swiss Federal Data Protection Act (FADP) - data security and audit trails
- EU General Data Protection Regulation (GDPR) - security of processing (Art. 32)
- Digital Operational Resilience Act (DORA) - incident logging and reporting (conditional)
- NIS2 Directive - security monitoring and logging (conditional)
- PCI DSS 4.0 - Requirement 10: Log and Monitor All Access (conditional)

**Framework Alignment**:
- NIST Cybersecurity Framework (CSF) - DE.CM (Detection: Continuous Monitoring)
- CIS Controls v8 - Control 8 (Audit Log Management)
- NIST SP 800-92 - Guide to Computer Security Log Management

### 5.2 Audit Evidence

Auditors should expect the following evidence:

**Policy Documentation**:
- Complete policy framework (ISMS-POL-A.8.15 and subsections S1-S5)
- Approval records (CISO, IT Operations, SOC, Legal/Compliance)
- Distribution records (training acknowledgments, policy portal access logs)
- Version history and change records

**Implementation Evidence**:
- Completed assessment workbooks (5 Excel files from ISMS-IMP-A.8.15.1 through .5)
- Log source inventory with coverage analysis
- SIEM/log management platform configuration documentation
- Log retention schedules and storage architecture diagrams
- Evidence artifacts (sample logs, SIEM screenshots, retention policies)

**Operational Evidence**:
- Log collection statistics (volume, sources, success rates)
- Log review records (daily/weekly/monthly checklists completed)
- SIEM correlation rules and alert configurations
- Incident investigation reports referencing log analysis
- Log storage capacity reports and trending
- Access control lists for log systems
- Integrity verification reports (tamper detection, hash verification)

**Effectiveness Evidence**:
- Key Performance Indicators (KPIs) from compliance dashboard
- Incident detection statistics (time to detect, log-based detections)
- Gap remediation tracking and closure evidence
- Trend analysis (log volume growth, storage utilization, review coverage)
- Audit findings remediation tracking

### 5.3 Audit Approach

**Recommended Audit Methodology**:

1. **Document Review**: Verify policy completeness, approval, distribution
2. **Technical Assessment**: Review generated workbooks, validate log source inventory
3. **Sampling**: Select representative systems for logging verification
4. **Testing**: 
   - Verify critical events are logged (authentication, privilege escalation)
   - Test log integrity protection (attempt unauthorized modification)
   - Validate retention compliance (check old logs still available)
   - Review log analysis procedures (examine review records)
5. **Interview**: Discuss with IT Operations, SOC analysts, system owners
6. **Gap Analysis**: Compare actual implementation vs. policy requirements
7. **Remediation Review**: Assess gap closure plans and timelines

**Audit Frequency**:
- **Internal Audit**: Annual (minimum), aligned with ISMS audit program
- **External Audit**: As required by ISO 27001 certification body (annual surveillance)
- **Regulatory Audit**: As required by applicable regulations (e.g., FINMA, FADPIC)
- **Self-Assessment**: Quarterly (using ISMS-IMP-A.8.15.5 Compliance Dashboard)

### 5.4 Common Audit Findings

**Typical Gaps** (and how to avoid them):

| Finding | Root Cause | Prevention |
|---------|-----------|------------|
| Incomplete log coverage | Shadow IT, undocumented systems | Regular asset inventory, IMP-1 assessment |
| Insufficient retention | Storage cost reduction | Tiered storage (hot/warm/cold), S2.3 requirements |
| Logs not reviewed | Lack of automation, resource constraints | SIEM implementation, IMP-4 assessment |
| No tamper protection | Default configurations | S2.2 requirements, integrity verification |
| Missing admin activity logs | Privileged access not logged | Mandatory logging requirements in S2.1 |
| Clock synchronization issues | Related Control 8.17 not implemented | NTP configuration, coordinate with A.8.17 |

---

## 6. Policy Governance

### 6.1 Policy Lifecycle

This policy follows the standard ISMS policy lifecycle:

**Development** → **Review** → **Approval** → **Publication** → **Training** → **Implementation** → **Monitoring** → **Review** → **Update**

Detailed governance procedures are specified in **ISMS-POL-A.8.15-S4 (Policy Governance)**.

### 6.2 Change Management

**Minor Changes** (typos, clarifications, formatting):
- Approval: Information Security Manager
- Process: Direct update with version increment (e.g., 1.0 → 1.1)
- Notification: Email to stakeholders

**Major Changes** (requirement changes, scope changes):
- Approval: CISO + Security Steering Committee
- Process: Full review cycle with stakeholder consultation
- Notification: Mandatory training for affected personnel

**Emergency Changes** (incident-driven, regulatory changes):
- Approval: CISO with expedited review
- Process: Implement immediately, formalize retrospectively
- Notification: Immediate communication to all stakeholders

### 6.3 Version Control

- All policy documents maintained in version control system (Git)
- Previous versions retained for audit trail
- Change log maintained in each document
- Major version increments for substantive changes
- Minor version increments for editorial changes

### 6.4 Review Schedule

- **Annual Review**: Full policy framework review
- **Triggered Review**: Within 30 days of significant incidents or regulatory changes
- **Quarterly Review**: Assessment of implementation effectiveness (using IMP dashboards)
- **Continuous Monitoring**: Gap tracking and remediation progress

---

## 7. Implementation Assessment Framework

### 7.1 Assessment Workbooks

The following Excel workbooks support systematic implementation assessment:

**ISMS-IMP-A.8.15.1: Log Source Inventory** (~12 sheets, ~800 rows)
- Purpose: Catalog all systems generating logs, assess completeness
- Key Outputs: Comprehensive log source inventory, gap identification
- Frequency: Annual full assessment, quarterly updates for new systems
- Owner: IT Operations Manager + System Owners

**ISMS-IMP-A.8.15.2: Log Collection & Centralization** (~11 sheets, ~700 rows)
- Purpose: Assess SIEM/log management infrastructure and collection coverage
- Key Outputs: Collection reliability metrics, integration status, data flows
- Frequency: Annual assessment, quarterly reliability reporting
- Owner: Security Operations Center (SOC) Lead

**ISMS-IMP-A.8.15.3: Log Protection & Retention** (~11 sheets, ~700 rows)
- Purpose: Assess log integrity protection, access controls, and retention compliance
- Key Outputs: Protection mechanism validation, retention compliance report
- Frequency: Semi-annual assessment
- Owner: Information Security Manager + IT Operations

**ISMS-IMP-A.8.15.4: Log Analysis & Review** (~11 sheets, ~700 rows)
- Purpose: Assess log review effectiveness, automation maturity, KPI tracking
- Key Outputs: Review process validation, automation coverage, effectiveness metrics
- Frequency: Quarterly assessment
- Owner: SOC Lead + Security Engineers

**ISMS-IMP-A.8.15.5: Compliance Dashboard** (~12 sheets, ~800 rows)
- Purpose: Consolidated view of Control A.8.15 compliance across all domains
- Key Outputs: Executive summary, maturity score, gap prioritization, action plan
- Frequency: Quarterly (aggregates data from IMP-1 through IMP-4)
- Owner: CISO / Information Security Manager

### 7.2 Assessment Process

1. **Distribute Workbooks**: Send assessment workbooks to domain owners
2. **Data Collection**: Owners complete workbooks with evidence (30-60 day period)
3. **Validation**: Security team validates entries and evidence quality
4. **Gap Analysis**: Identify gaps between requirements and actual state
5. **Dashboard Consolidation**: Aggregate all domain data into IMP-5 dashboard
6. **Executive Review**: Present findings to CISO and Security Steering Committee
7. **Action Planning**: Develop prioritized remediation roadmap
8. **Remediation Tracking**: Monitor gap closure progress quarterly
9. **Continuous Improvement**: Update policies and procedures based on lessons learned

---

## 8. Related Controls & Integration

### 8.1 Control Dependencies

**Control A.8.15 (Logging)** integrates closely with:

**A.8.16 - Monitoring Activities**: 
- Logging provides data source for monitoring
- Monitoring consumes and analyzes logs
- Coordinated requirements for anomaly detection

**A.8.17 - Clock Synchronization**: 
- Accurate timestamps essential for log correlation
- NTP implementation required for logging accuracy
- Coordinated implementation recommended

**A.5.24 - Information Security Incident Management Planning**: 
- Logs are primary evidence source for incident investigations
- Incident response procedures reference log analysis
- Coordinated training and exercises

**A.8.11 - Data Masking**: 
- Logs may contain sensitive data requiring protection
- Balance logging needs with privacy requirements
- Coordinated implementation for data minimization

### 8.2 Technology Integration

**SIEM/Log Management Platform**:
- Central aggregation point for all logs
- Correlation engine for cross-system analysis
- Alert generation and workflow management
- Reporting and dashboard capabilities

**Security Information & Event Management (SIEM) Products**:
- Splunk, IBM QRadar, Microsoft Sentinel, LogRhythm, ArcSight, etc.
- Selection criteria in S2 subsections
- Integration requirements in S5.A (Logging Standards)

**Cloud Logging Services**:
- AWS CloudWatch, Azure Monitor, GCP Cloud Logging
- Integration with on-premises SIEM
- Retention and export configurations

**Endpoint Detection & Response (EDR)**:
- Endpoint-level detailed logging
- Integration with SIEM for correlation
- Complementary to traditional log sources

---

## 9. Approval & Sign-Off

### 9.1 Policy Approval

This policy and all subsections (S1-S5) require approval from:

| Role | Name | Date | Signature | Status |
|------|------|------|-----------|--------|
| **Chief Information Security Officer (CISO)** | [Name] | [DD.MM.YYYY] | __________ | ☐ Approved |
| **Information Security Manager** | [Name] | [DD.MM.YYYY] | __________ | ☐ Reviewed |
| **IT Operations Manager** | [Name] | [DD.MM.YYYY] | __________ | ☐ Reviewed |
| **SOC Lead** | [Name] | [DD.MM.YYYY] | __________ | ☐ Reviewed |
| **Legal/Compliance Officer** | [Name] | [DD.MM.YYYY] | __________ | ☐ Reviewed |

### 9.2 Acknowledgment

By approving this policy, the signatories confirm:

- ✅ The policy framework is complete and adequate for Control A.8.15
- ✅ Requirements are clear, implementable, and auditable
- ✅ Resources are committed for policy implementation
- ✅ Training and awareness programs will be conducted
- ✅ Assessment workbooks will be completed as scheduled
- ✅ Gaps will be remediated according to priority and timelines
- ✅ Annual review will be conducted on schedule

### 9.3 Publication Authorization

Upon final approval, this policy is authorized for publication to:
- [ ] Internal policy portal (intranet)
- [ ] IT Operations documentation repository
- [ ] Security Operations Center (SOC) knowledge base
- [ ] Training materials and onboarding programs
- [ ] Audit team for compliance verification

**Publication Date**: [DD.MM.YYYY]  
**Effective Date**: [DD.MM.YYYY]  
**Mandatory Compliance Date**: [DD.MM.YYYY + 90 days]

---

## 10. Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-POL-A.8.15 |
| **ISO 27001:2022 Control** | Annex A Control 8.15 (Logging) |
| **ISO 27002:2022 Section** | 8.15 (Event logging) |
| **Document Type** | Master Policy (Framework Navigation) |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Page Count** | [Auto-generated] |
| **Word Count** | ~4,500 words |
| **Line Count** | ~390 lines |
| **Subsection Count** | 13 documents (S1, S2, S2.1-S2.4, S3, S4, S5, S5.A-S5.D) |
| **Related IMPs** | 5 assessment workbooks (IMP-1 through IMP-5) |
| **Related Scripts** | 6 Python scripts (generators + sanity check) |
| **Next Review Date** | [Approval Date + 12 months] |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Policy Steward** | Information Security Manager |

---

**END OF MASTER POLICY**

---

## Appendix: Navigation Quick Reference

**Need to understand the scope?** → Read **S1** (Purpose, Scope, Definitions)

**Need to know what to log?** → Read **S2.1** (Event Logging Requirements)

**Need to protect logs?** → Read **S2.2** (Log Protection & Integrity)

**Need retention requirements?** → Read **S2.3** (Log Retention & Storage)

**Need review procedures?** → Read **S2.4** (Log Review & Analysis) and **S5.C** (Procedures)

**Need to know who does what?** → Read **S3** (Roles & Responsibilities)

**Need technical specs?** → Read **S5.A** (Logging Standards)

**Need quick answers?** → Read **S5.D** (Quick Reference Guide)

**Need to assess compliance?** → Use **ISMS-IMP-A.8.15.5** (Compliance Dashboard)

---

*"The logs are out there. Someone just needs to read them."*  
— Ancient SOC Wisdom

*"In God we trust. All others must bring data... and logs."*  
— W. Edwards Deming (adapted for InfoSec)

*"What I cannot log, I cannot investigate."*  
— Richard Feynman (if he were a CISO)