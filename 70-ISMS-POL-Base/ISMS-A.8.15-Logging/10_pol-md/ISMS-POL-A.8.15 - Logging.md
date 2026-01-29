# ISMS-POL-A.8.15 – Logging

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Logging |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.15 |
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
| 1.0 | [Date] | CISO | Initial modular policy framework (14 documents) |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Information Security Manager
- Operational Review: Security Operations Center (SOC) Lead / IT Operations Manager
- Privacy Review: Data Protection Officer (DPO)
- Compliance Review: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.15 (Implementation Guidance Suite - 5 assessment workbooks)
- ISMS-REF-A.8.15 (Logging Standards Reference - Technical Reference)
- ISMS-POL-A.8.16 (Monitoring Activities)
- ISMS-POL-A.8.17 (Clock Synchronization)
- ISMS-POL-A.5.24 (Information Security Incident Management)
- ISO/IEC 27001:2022 Control A.8.15

---

## Executive Summary

This policy establishes [Organization]'s requirements for event logging to support incident detection, forensic investigation, compliance obligations, and accountability in accordance with ISO/IEC 27001:2022 Control A.8.15.

**Scope**: This policy applies to all information systems, applications, and infrastructure components; all network devices (routers, switches, firewalls, load balancers); all security tools (SIEM, IDS/IPS, anti-malware, DLP, web filters); all database systems and storage platforms; all cloud services and SaaS applications; all administrative and privileged access activities; and all authentication and access control systems.

**Purpose**: Define organizational requirements for event logging control implementation and governance. This policy establishes WHAT events must be logged, HOW LONG logs must be retained, WHO is accountable for log management, and WHEN logs must be reviewed. Implementation procedures (HOW logs are technically configured) are documented separately in ISMS-IMP-A.8.15.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG Article 8 (data security obligations), EU GDPR Article 32 (security of processing), and ISO/IEC 27001:2022 Annex A.8.15. Conditional sector-specific requirements (DORA, NIS2, PCI DSS, HIPAA) apply where [Organization]'s business activities trigger applicability.

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.15

**ISO/IEC 27001:2022 Annex A.8.15 - Logging**

> *Event logs recording user activities, exceptions, faults and information security events shall be produced, kept and regularly reviewed.*

**Control Objective**: Establish organizational policy for event logging across information systems and infrastructure to enable incident detection, investigation, forensic analysis, compliance demonstration, and accountability for user and administrator actions.

**This Policy Addresses**:
- Event logging requirements based on system criticality and data classification
- Log protection and integrity mechanisms preventing unauthorized modification or deletion
- Log retention periods aligned with regulatory requirements and business needs
- Log review and analysis procedures ensuring timely incident detection
- Privacy considerations balancing security requirements with data protection obligations
- Organizational roles and responsibilities for logging governance
- Exception and incident management frameworks
- Integration with [Organization]'s risk assessment and treatment processes

### 1.2 What This Policy Does

This policy:
- **Defines** event logging control requirements aligned with data classification, system criticality, and regulatory obligations
- **Establishes** governance framework for logging decision-making and accountability
- **Specifies** mandatory log events, protection mechanisms, retention periods, and review procedures
- **References** applicable regulatory requirements per ISMS-POL-00
- **Identifies** organizational roles and responsibilities for logging controls
- **Provides** framework for managing exceptions and logging-related incidents

### 1.3 What This Policy Does NOT Do

This policy does NOT:
- **Specify technical logging configurations** (see ISMS-IMP-A.8.15 Implementation Guides)
- **Define specific log formats or field structures** (see ISMS-REF-A.8.15 Logging Standards Reference)
- **Provide system-specific logging procedures** (see ISMS-IMP-A.8.15 Assessment Guides)
- **Select logging technologies or SIEM vendors** (technology selection based on [Organization]'s risk assessment and operational requirements)
- **Replace risk assessment** (logging controls selected based on [Organization]'s risk treatment decisions)
- **Define detailed incident response procedures** (see ISMS-POL-A.5.24 Incident Management)
- **Establish real-time monitoring requirements** (see ISMS-POL-A.8.16 Monitoring Activities)

**Rationale**: Separating policy requirements from implementation guidance enables:
- Policy stability despite evolving logging technologies and SIEM solutions
- Technical agility for log format and collection method updates without policy revision
- Clear distinction between governance (policy) and execution (implementation)
- Focused audit scope (auditors audit policy compliance, not technical implementation details)

### 1.4 Scope

**This policy applies to**:

**Information Systems and Infrastructure**:
- All information systems, applications, and infrastructure components
- Network devices (routers, switches, firewalls, VPN gateways, load balancers, proxies)
- Security tools (SIEM, IDS/IPS, anti-malware, endpoint protection, DLP, web filters, email gateways)
- Database systems and data storage platforms (relational databases, NoSQL, object storage, file servers)
- Cloud services and SaaS applications (IaaS, PaaS, SaaS platforms)
- Authentication and identity management systems (Active Directory, LDAP, SSO, MFA)
- Administrative access infrastructure (jump hosts, bastion hosts, privileged access management)

**Activity Categories**:
- Authentication events (successful and failed login attempts, logout, account lockouts, password changes)
- Authorization and access events (privilege escalation, access to sensitive data, access control changes)
- Administrative actions (configuration changes, user account management, privilege grants, policy changes)
- Security events (malware detection, intrusion attempts, firewall blocks, DLP alerts, encryption operations)
- System events (startup/shutdown, service status changes, errors, resource exhaustion)
- Application events (errors, exceptions, database transactions for sensitive data, API authentication)

**Deployment Models**:
- On-premises infrastructure (physical and virtual servers, network equipment)
- Cloud environments (public cloud, private cloud, hybrid cloud)
- Third-party hosted services (managed services, SaaS applications)

**Out of Scope**:
- Business application audit trails not related to security (covered by application-specific policies)
- Financial transaction logs for accounting purposes (covered by financial control policies)
- Clinical or medical record access logs (covered by healthcare-specific policies, if applicable)
- Real-time monitoring and alerting processes (covered by ISMS-POL-A.8.16 Monitoring Activities)
- Endpoint user activity monitoring beyond security events (unless required by regulatory obligations)

### 1.5 Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

All [Organization] operations must comply with:

| Regulation | Logging Requirements | Article/Section |
|-----------|---------------------|-----------------|
| **ISO/IEC 27001:2022** | Event logs recording user activities, exceptions, faults, and information security events SHALL be produced, kept, and regularly reviewed | Annex A.8.15 |
| **Swiss nDSG** (Federal Data Protection Act) | Appropriate technical and organizational measures including logging for data security and accountability | Art. 8 |
| **EU GDPR** (where processing EU personal data) | Logging as security measure for protecting personal data processing, demonstrating accountability, and supporting breach notification | Art. 32(1)(d), Art. 33 |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Logging Requirements |
|-----------|-------------------|---------------------|
| **DORA** (Digital Operational Resilience Act) | EU financial services entity | ICT-related incident detection and management supported by comprehensive logging (Art. 17), ICT system event logging for operational resilience |
| **NIS2** (Network and Information Security Directive) | Essential or important entity (EU) | Logging as cybersecurity risk management measure (Art. 21), incident detection and response logging, security monitoring logs |
| **PCI DSS v4.0** | Processing payment card data | Requirement 10: Comprehensive logging of all access to system components and cardholder data, log protection and integrity, minimum 12-month online retention, centralized log management, automated log review |
| **HIPAA** (Health Insurance Portability and Accountability Act) | Handling US healthcare data | §164.312(b) Audit controls: Log information system activity, implement hardware/software mechanisms to record and examine activity in systems containing ePHI, minimum 6-year retention |
| **SOX** (Sarbanes-Oxley Act) | Publicly traded companies (financial reporting) | Logging for financial systems integrity, audit trail protection, change management logging, minimum 7-year retention for financial audit trails |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- **NIST SP 800-92**: Guide to Computer Security Log Management
- **CIS Controls v8 - Control 8**: Audit Log Management
- **ISO/IEC 27002:2022 - Section 8.15**: Implementation guidance for logging controls
- **BSI IT-Grundschutz**: Logging and monitoring recommendations

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment documented in ISMS-POL-00. The most stringent requirements apply where multiple regulations overlap.

**Note**: For complete regulatory categorization and applicability assessment methodology, refer to **ISMS-POL-00 (Regulatory Applicability Framework)**.

---

## 2. Requirements Framework

### 2.1 Event Logging Requirements

[Organization] SHALL log security-relevant events across all in-scope systems to enable incident detection, investigation, and compliance demonstration.

#### 2.1.1 Mandatory Log Events

**Authentication Events** (SHALL log):
- Successful login attempts (all users, all systems)
- Failed login attempts (all users, all systems)
- Logout events (session termination)
- Account lockouts (threshold exceeded)
- Password changes and resets (user-initiated and administrative)
- Multi-factor authentication events (enrollment, authentication attempts, bypass)
- Service account authentication (API keys, tokens, certificates)

**Authorization and Access Events** (SHALL log):
- Access to sensitive data (classified as Confidential or Restricted per data classification policy)
- Privilege escalation events (sudo, Run As Administrator, role assumption)
- Access control changes (permission modifications, ACL updates, role assignments)
- File and object access for classified data (create, read, update, delete)
- Database queries accessing sensitive tables or columns
- Unauthorized access attempts (denied by access controls)

**Administrative Actions** (SHALL log):
- System configuration changes (OS, application, network device configuration)
- User account creation, modification, and deletion
- Privilege grants and revocations (administrative rights, group memberships)
- Security policy changes (firewall rules, access policies, logging configuration)
- Installation and removal of software, services, and system components
- Certificate management actions (issuance, renewal, revocation)
- Backup and restore operations
- System time changes (NTP synchronization, manual adjustments)

**Security Events** (SHALL log):
- Malware detection and prevention actions (quarantine, deletion, block)
- Intrusion detection and prevention system alerts (IDS/IPS events)
- Firewall blocks and rule violations (denied connections, blocked traffic)
- Data loss prevention alerts (DLP policy violations, data exfiltration attempts)
- Encryption and decryption operations for audit trails (key usage, certificate validation)
- Security tool failures or configuration errors
- Vulnerability scan results (critical and high severity findings)
- Patch deployment and security update installation

**System Events** (SHALL log):
- System startup and shutdown (planned and unplanned)
- Service starts, stops, and crashes
- System errors and critical failures
- Resource exhaustion warnings (disk space, memory, CPU)
- Application crashes and exceptions
- Database connection failures
- Hardware failures and environmental alerts (for on-premises systems)

**Network Events** (SHALL log):
- Firewall rule matches for security-relevant traffic
- VPN connections and disconnections (remote access)
- Network segmentation boundary traversals (zone-to-zone traffic)
- DNS query anomalies (C2 indicators, DGA detection)
- TLS/SSL certificate validation failures
- Network device configuration changes

**Application Events** (SHALL log):
- Application errors and exceptions (unhandled errors, stack traces for troubleshooting)
- Database transactions for sensitive data (SQL queries, data modifications)
- API authentication and authorization events (API key usage, token validation)
- File uploads and downloads from web applications
- Privileged function execution (administrative operations, sensitive operations)
- Application-specific security events (payment processing, PHI access, PII handling)

#### 2.1.2 Log Content Requirements

Each log entry SHALL include at minimum:

| Required Field | Description | Example |
|----------------|-------------|---------|
| **Timestamp** | Date and time (ISO 8601 format, UTC or local with timezone) | 2026-01-21T14:32:15+01:00 |
| **User Identity** | User ID, service account, or system identifier | username@domain, system.service |
| **Source System** | Hostname, IP address, or system identifier | server01.example.com, 192.168.1.10 |
| **Event Type** | Category and specific action | Authentication.Login.Success |
| **Outcome** | Success or failure | Success, Failure, Error |
| **Source IP** | Originating IP address (if applicable) | 10.0.1.50 |
| **Target Resource** | Affected system, file, or data object | /data/confidential/file.xlsx |
| **Additional Context** | Event-specific details (error codes, transaction IDs) | ErrorCode: 0x80004005 |

**Implementation Note**: Detailed log format specifications (syslog RFC 5424, CEF, JSON schemas) are documented in ISMS-REF-A.8.15 (Logging Standards Reference).

#### 2.1.3 Log Format Standards

[Organization] SHOULD use structured log formats for consistent parsing and analysis:

- **Syslog (RFC 5424)**: Infrastructure devices, operating systems, network equipment
- **Common Event Format (CEF)**: SIEM integration, security tools
- **JSON**: Application logs, cloud services, microservices
- **Structured logging**: Key-value pairs, machine-readable formats

Plain text logs MAY be used where structured formats are not supported, provided log parsing rules are documented.

**Time Synchronization**: All log sources SHALL synchronize time with authoritative time sources per ISMS-POL-A.8.17 (Clock Synchronization) to ensure accurate event correlation.

### 2.2 Log Protection & Integrity Requirements

[Organization] SHALL protect logs from unauthorized access, modification, and deletion to maintain evidential value and ensure trustworthiness.

#### 2.2.1 Access Control

**Read Access** (SHALL restrict):
- Logs SHALL be accessible only to authorized personnel with legitimate need
- Read access limited to: SOC analysts, security engineers, IT operations (for operational logs), auditors, legal counsel (with approval)
- Access SHALL be granted based on least privilege principle
- Access requests SHALL be documented and approved by Information Security Manager or CISO

**Write Access** (SHALL restrict):
- Write access to logs SHALL be restricted to logging service or daemon only
- Applications and systems SHALL have write-only permissions to log destinations
- No user or administrator SHALL have direct write access to logs
- Log modification capabilities SHALL require administrative privileges with dual authorization

**Administrative Access** (SHALL control):
- Log administration (configuration, deletion, archival) SHALL require elevated privileges
- Separation of duties: System administrators SHALL NOT be log administrators
- Log administrator actions SHALL be logged separately (logging the loggers)
- Emergency access procedures SHALL be documented for log system failures

#### 2.2.2 Integrity Protection

[Organization] SHALL implement mechanisms to detect log tampering:

**Write-Once Storage** (SHOULD implement):
- Security logs and audit trails SHOULD use write-once, read-many (WORM) storage where feasible
- Append-only log files preventing modification or deletion
- Immutable storage for compliance-critical logs (financial, healthcare, PCI)

**Cryptographic Protection** (SHOULD implement):
- Digital signatures or cryptographic hashing for log integrity verification
- Hash chains for tamper detection (each log entry includes hash of previous entry)
- Signed log forwarding from sources to centralized collection

**Centralized Collection** (SHALL implement):
- Logs SHALL be forwarded to centralized log management system (SIEM or log aggregation platform)
- Centralization prevents local deletion or tampering
- Forwarding SHALL occur in real-time or near-real-time (within 5 minutes for security logs)
- Retention of local logs SHOULD be minimized (7-30 days maximum before overwrite)

#### 2.2.3 Secure Transmission

**Encryption in Transit** (SHALL implement):
- Logs SHALL be transmitted encrypted using TLS 1.2 or higher
- Log forwarding protocols SHALL use authenticated and encrypted channels
- No cleartext transmission of security logs over untrusted networks
- Certificate validation SHALL be enforced for log forwarding connections

#### 2.2.4 Tamper Detection and Alerting

[Organization] SHALL implement automated detection of log integrity violations:

**Alert Conditions** (SHALL monitor):
- Log integrity violations (hash mismatch, signature verification failure)
- Log collection failures (log sources not sending data for more than 15 minutes)
- Unauthorized log access (access by non-authorized users)
- Log storage capacity issues (approaching 80% capacity threshold)
- Log forwarding failures (network errors, authentication failures)
- Suspicious log deletion or modification attempts

**Alert Response** (SHALL define):
- Critical alerts SHALL trigger immediate notification to SOC and Information Security Manager
- Log integrity violations SHALL trigger incident response procedures
- Failed log forwarding SHALL trigger automated remediation or manual investigation within 1 hour

**Implementation Note**: Technical protection mechanisms (WORM storage, hash chains, encryption protocols) are detailed in ISMS-IMP-A.8.15.3 (Log Protection & Retention Assessment).

### 2.3 Log Retention & Storage Requirements

[Organization] SHALL retain logs for sufficient periods to support incident investigation, forensic analysis, and compliance obligations.

#### 2.3.1 Retention Periods

**Retention Requirements by Log Category**:

| Log Category | Online Storage | Archive Storage | Total Retention | Rationale |
|--------------|----------------|-----------------|-----------------|-----------|
| **Security Events** (malware, intrusion, firewall) | 12 months | 7 years | 8 years total | Forensic investigation, legal evidence, compliance (PCI DSS, SOX) |
| **Authentication Logs** (login, logout, lockout) | 12 months | 7 years | 8 years total | Accountability, incident investigation, compliance (GDPR, nDSG) |
| **Administrative Actions** (config changes, user mgmt) | 12 months | 7 years | 8 years total | Audit trail, change management, compliance (SOX, ISO 27001) |
| **Database Logs** (queries accessing sensitive data) | 12 months | 7 years | 8 years total | Compliance (SOX, HIPAA), data access accountability |
| **Application Logs** (errors, exceptions, transactions) | 6 months | 1 year | 1.5 years total | Troubleshooting, performance analysis, operational support |
| **Network Device Logs** (firewall, router, switch) | 6 months | 1 year | 1.5 years total | Network troubleshooting, incident investigation |
| **System Logs** (OS events, service status) | 6 months | 1 year | 1.5 years total | System troubleshooting, capacity planning |

**Conditional Requirements** (apply when applicable):

| Regulation | Minimum Retention | Applicable Log Types |
|-----------|-------------------|---------------------|
| **PCI DSS** | 12 months online, readily accessible | All logs related to payment card data processing and cardholder data environment |
| **HIPAA** | 6 years minimum | All logs related to ePHI (electronic protected health information) access and systems |
| **SOX** | 7 years minimum | All logs related to financial systems and audit trails for financial reporting |
| **GDPR** | Document necessity, typically 6-24 months | Personal data access logs, data subject right requests, consent management logs |
| **Swiss nDSG** | Document necessity based on legal basis for processing | Personal data processing logs, access logs for sensitive data |

**Implementation Note**: Organizations SHALL document retention period determination and legal basis in ISMS-IMP-A.8.15.3 (Log Protection & Retention Assessment). Longer retention periods may be adopted where organizational risk assessment justifies extended retention.

#### 2.3.2 Storage Architecture

[Organization] SHALL implement tiered storage architecture optimizing cost and accessibility:

**Hot Storage** (online, immediate access):
- Purpose: Active investigation, real-time analysis, recent incident response
- Retention: Typically 1-12 months depending on log category
- Performance: Sub-second query response, full-text search, SIEM integration
- Technology: High-performance storage (SSD, fast disk arrays), indexed databases

**Warm Storage** (nearline, slower retrieval):
- Purpose: Historical analysis, compliance audits, older incident investigation
- Retention: Typically 1-3 years (beyond hot storage period)
- Performance: Minutes to hours for data retrieval, batch processing
- Technology: Object storage, compressed archives, slower disk tiers

**Cold Storage** (offline, archive):
- Purpose: Long-term compliance retention, legal hold, historical reference
- Retention: Typically 3-7+ years (compliance-driven)
- Performance: Hours to days for data retrieval, restoration required before analysis
- Technology: Tape backup, cloud archive storage (S3 Glacier, Azure Archive), optical media

#### 2.3.3 Capacity Planning

**Storage Capacity Management** (SHALL implement):
- Monitor log storage capacity continuously
- Alert at 80% capacity threshold (warning)
- Critical alert at 90% capacity (immediate action required)
- Plan for minimum 20% annual growth in log volume
- Review and adjust storage capacity quarterly
- Implement automated purging of non-essential logs approaching capacity limits

**Growth Planning Factors**:
- New system and application onboarding
- Increased logging verbosity for security enhancement
- Regulatory requirement changes
- Incident investigation needs driving longer retention

#### 2.3.4 Secure Disposal

**Retention Expiry** (SHALL implement):
- Logs SHALL be securely deleted after retention period expires
- Deletion SHALL be performed using secure deletion methods (overwrite, cryptographic erasure)
- Deletion actions SHALL be logged (what was deleted, when, by whom)
- Deletion approvals SHALL be documented for compliance-critical logs

**Legal Hold** (SHALL implement):
- Suspension of deletion during litigation, investigation, or regulatory inquiry
- Legal hold procedures SHALL be documented and communicated
- Chain of custody SHALL be maintained for legally held logs
- Legal hold release SHALL be documented before resuming normal deletion

**Implementation Note**: Disposal procedures and cryptographic erasure methods are documented in ISMS-IMP-A.8.15.3 (Log Protection & Retention Assessment).

### 2.4 Log Review & Analysis Requirements

[Organization] SHALL regularly review and analyze logs to detect security incidents, anomalies, and policy violations.

#### 2.4.1 Review Frequency and Responsibilities

**Review Schedule**:

| Review Type | Frequency | Responsibility | Purpose | Time Investment |
|-------------|-----------|----------------|---------|-----------------|
| **Automated Analysis** | Continuous (24/7) | SIEM / SOC | Real-time threat detection, automated alerting | Automated |
| **Daily Review** | Every business day | SOC Analysts | High-priority alerts, critical events, trend analysis | 1-2 hours |
| **Weekly Review** | Weekly | Security Team | Capacity planning, recurring patterns, tuning opportunities | 2-3 hours |
| **Monthly Review** | Monthly | Information Security Manager | Effectiveness assessment, metrics reporting, policy compliance | 3-4 hours |
| **Quarterly Review** | Quarterly | CISO | Strategic assessment, compliance reporting, resource planning | 4-6 hours |

#### 2.4.2 Review Procedures

**Daily Review Procedures** (SOC Analysts SHALL):
- Review SIEM dashboard for overnight alerts
- Investigate all high and critical severity alerts
- Triage medium severity alerts (document false positives)
- Identify recurring patterns or anomalies
- Escalate incidents per incident response procedures
- Document review activities in SOC ticketing system

**Weekly Review Procedures** (Security Team SHALL):
- Analyze trends in failed authentication attempts
- Review capacity utilization and storage growth
- Identify systems with missing or incomplete logs
- Tune SIEM correlation rules based on false positives
- Review exception requests and temporary access grants
- Update threat intelligence feeds and detection rules

**Monthly Review Procedures** (Information Security Manager SHALL):
- Assess logging effectiveness (coverage, completeness, quality)
- Review key performance indicators (KPIs) and metrics
- Identify gaps in logging coverage or retention
- Plan remediation for identified deficiencies
- Report to CISO on logging program status
- Coordinate with system owners on logging improvements

**Quarterly Review Procedures** (CISO SHALL):
- Review strategic metrics and compliance status
- Assess organizational logging maturity
- Approve resource allocation for logging infrastructure
- Report to Executive Management on logging posture
- Update logging policy based on lessons learned
- Approve logging technology roadmap and investments

**Implementation Note**: Detailed review checklists and procedures are documented in ISMS-IMP-A.8.15.4 (Log Analysis & Review Assessment).

#### 2.4.3 Automated Analysis

[Organization] SHALL implement automated log analysis capabilities:

**Security Information and Event Management (SIEM)** (SHOULD implement):
- Centralized log aggregation and correlation
- Real-time analysis of security events
- Automated detection rules and correlation logic
- Threat intelligence integration
- Incident case management
- Reporting and dashboard capabilities

**Automated Detection Rules** (SHALL implement):
- Brute force attack detection (multiple failed login attempts)
- Privilege escalation detection (unauthorized privilege changes)
- Data exfiltration indicators (large data transfers, unusual access patterns)
- Malware indicators (C2 communication, known malicious IPs)
- Insider threat indicators (off-hours access, unusual data access)
- Policy violations (unauthorized software, disabled security controls)

**Anomaly Detection** (SHOULD implement):
- Baseline normal behavior (user activity patterns, system activity patterns)
- Statistical anomaly detection (deviations from baseline)
- Machine learning-based detection (behavioral analytics)
- Peer group analysis (outlier detection)

#### 2.4.4 Incident Response Integration

**Incident Investigation** (SHALL support):
- Logs SHALL be available for incident investigation within 15 minutes of request
- Log retention SHALL support incident investigation timeframes (typically 90-180 days for hot storage)
- Forensic log preservation SHALL be implemented for active incidents
- Chain of custody SHALL be maintained for logs used as evidence

**Forensic Analysis** (SHALL enable):
- Log export capabilities for forensic tools
- Log integrity verification (hash validation, signature verification)
- Correlation across multiple log sources
- Timeline reconstruction capabilities

**Integration with ISMS-POL-A.5.24** (SHALL coordinate):
- Incident detection triggers from log analysis
- Incident classification based on log evidence
- Incident escalation procedures
- Post-incident review incorporating log findings

#### 2.4.5 Metrics and Key Performance Indicators

[Organization] SHOULD track logging effectiveness through metrics:

**Coverage Metrics**:
- Percentage of systems with logging enabled (target: 100% for in-scope systems)
- Percentage of log sources forwarding to centralized collection (target: 95%+)
- Log completeness score (all required fields present)

**Operational Metrics**:
- Log collection reliability (percentage of expected logs received)
- Mean time to detect (MTTD) security incidents (target: <1 hour for critical incidents)
- Alert false positive rate (target: <10% for high severity alerts)
- Log review completion rate (target: 100% of scheduled reviews completed on time)

**Storage Metrics**:
- Log storage capacity utilization (alert at 80%, critical at 90%)
- Log retention compliance (percentage of logs meeting retention requirements)
- Log archival success rate (target: 100%)

**Implementation Note**: Metrics tracking and reporting procedures are documented in ISMS-IMP-A.8.15.4 (Log Analysis & Review Assessment).

### 2.5 Privacy & Data Protection

[Organization] SHALL implement logging controls in compliance with privacy regulations and data protection principles.

#### 2.5.1 Privacy Compliance

**Regulatory Compliance** (SHALL ensure):
- Logging SHALL comply with Swiss nDSG (data minimization, purpose limitation)
- Logging SHALL comply with EU GDPR where processing EU personal data (Art. 5, Art. 32)
- Users SHALL be informed of monitoring through acceptable use policy, employment contracts, and privacy notices
- Access to logs containing personal data SHALL be restricted to authorized personnel with legitimate need

**Data Protection Officer (DPO) Involvement** (SHALL coordinate):
- DPO SHALL review logging policy for privacy compliance
- DPO SHALL be consulted on new logging implementations affecting personal data
- DPO SHALL have access to logs for data subject rights requests
- Privacy impact assessments SHALL be conducted for extensive monitoring implementations

#### 2.5.2 Prohibited Data in Logs

[Organization] SHALL NOT log the following data types:

**Strictly Prohibited**:
- Passwords (in cleartext or encrypted form - only hash log entries for verification events)
- Full credit card numbers (PCI DSS requirement - only log truncated PANs, first 6 and last 4 digits)
- Card verification codes (CVV, CVV2, CVC)
- National identification numbers (Social Security Numbers, passport numbers)
- Health information details (unless explicitly required and justified per HIPAA addressable safeguard)
- Full contents of personal communications (emails, messages - only metadata permitted)

**Minimize Where Possible**:
- Personal identifiable information (PII) - use pseudonymization or tokenization where feasible
- Authentication tokens or session IDs (use truncated or hashed values)
- API keys or credentials (use key identifier, not full key)

**Exception**: Prohibited data MAY be logged when required by specific regulatory obligations (e.g., HIPAA audit controls) with documented justification, DPO approval, and enhanced protection controls.

#### 2.5.3 Data Minimization

**Minimize Collection** (SHOULD implement):
- Log only events necessary for security, compliance, and operational purposes
- Avoid logging personal data where event can be recorded without PII
- Use pseudonymization techniques (user IDs instead of names where feasible)
- Apply data masking for sensitive fields (partial masking, tokenization)

**Balance Security and Privacy** (SHALL balance):
- Security requirements for comprehensive logging
- Privacy principles of data minimization and purpose limitation
- Legitimate interests assessment for monitoring activities
- Proportionality of logging to identified risks

**Implementation Note**: Privacy-preserving logging techniques are documented in ISMS-IMP-A.8.15.1 (Log Source Inventory Assessment) and ISMS-REF-A.8.15 (Logging Standards Reference).

---

## 3. Governance & Compliance

### 3.1 Roles & Responsibilities

[Organization] defines clear accountability for logging control implementation and governance.

**Executive Management / Board of Directors**:
- Accountable for approving logging policy and strategic direction
- Ensuring adequate resources and budget for logging infrastructure
- Accepting residual risks related to logging limitations
- Supporting organizational security program and logging initiatives

**Chief Information Security Officer (CISO)**:
- Accountable for overall logging policy effectiveness and compliance
- Approving high-risk exceptions and policy changes
- Defining organizational logging requirements based on risk assessment
- Escalating critical logging issues to Executive Management
- Conducting annual policy review and approval
- Allocating resources for logging program

**Information Security Manager**:
- Responsible for implementing logging policy requirements
- Coordinating with system owners on logging enablement
- Conducting monthly logging effectiveness reviews
- Managing exception requests and approvals
- Reporting logging program status to CISO
- Maintaining logging documentation and procedures

**Security Operations Center (SOC) Team**:
- Responsible for daily log review and analysis
- Monitoring SIEM for security events and alerts
- Investigating alerts and escalating incidents
- Tuning detection rules and correlation logic
- Documenting review activities and findings
- Providing 24/7 coverage for critical alerts

**IT Operations / System Administrators**:
- Responsible for configuring system logging per policy requirements
- Ensuring log forwarding to centralized collection system
- Maintaining system time synchronization per ISMS-POL-A.8.17
- Providing storage infrastructure for log management
- Coordinating with Security Team on logging issues
- Implementing logging configuration changes

**System Owners / Application Owners**:
- Responsible for enabling appropriate logging on owned systems and applications
- Documenting what events are logged and log format
- Coordinating with Security Team for log source onboarding
- Ensuring logging does not negatively impact system performance
- Approving logging configuration changes for owned systems
- Providing business context for log events during investigations

**Log Administrators**:
- Responsible for managing SIEM and log management platform
- Configuring log collection, parsing, and retention
- Managing log storage and archival processes
- Troubleshooting log collection issues
- Maintaining separation of duties (not system administrators)
- Performing secure log deletion per retention policy

**Data Protection Officer (DPO)**:
- Responsible for reviewing logging policy for privacy compliance
- Advising on personal data handling in logs
- Responding to data subject access requests involving logs
- Conducting privacy impact assessments for monitoring
- Ensuring user notification requirements are met

**Users (All Personnel)**:
- Responsible for complying with acceptable use policy
- Understanding that activities are logged and monitored
- Reporting suspected security incidents or anomalies
- Not attempting to circumvent or disable logging controls

**Detailed RACI Matrix**: Complete roles and responsibilities with RACI (Responsible, Accountable, Consulted, Informed) assignment are documented in ISMS-IMP-A.8.15 Implementation Guides.

### 3.2 Assessment and Verification

[Organization] verifies logging control effectiveness through structured assessment.

**Assessment Domains**:

1. **Log Source Inventory** (ISMS-IMP-A.8.15.1):
   - Catalog all systems and applications generating logs
   - Assess completeness of log source coverage
   - Identify gaps in logging enablement
   - Verify mandatory log events are captured

2. **Log Collection & Centralization** (ISMS-IMP-A.8.15.2):
   - Assess SIEM infrastructure and capabilities
   - Verify log collection reliability and completeness
   - Validate log forwarding configuration
   - Measure collection performance and latency

3. **Log Protection & Retention** (ISMS-IMP-A.8.15.3):
   - Verify integrity protection mechanisms
   - Validate access control implementation
   - Assess retention compliance by log category
   - Review storage capacity and archival processes

4. **Log Analysis & Review** (ISMS-IMP-A.8.15.4):
   - Assess review process effectiveness
   - Evaluate automation maturity (SIEM correlation rules)
   - Measure key performance indicators
   - Verify incident response integration

5. **Compliance Dashboard** (ISMS-IMP-A.8.15.5):
   - Consolidated compliance reporting across all domains
   - Executive summary with overall compliance percentage
   - Gap prioritization and remediation tracking
   - Quarterly trend analysis

**Assessment Frequency**:
- Domain 1 (Log Source Inventory): Annual full assessment, quarterly updates for new systems
- Domain 2 (Collection & Centralization): Annual full assessment, quarterly reliability metrics
- Domain 3 (Protection & Retention): Semi-annual assessment
- Domain 4 (Analysis & Review): Quarterly assessment
- Domain 5 (Compliance Dashboard): Quarterly consolidation

**Assessment Tools**:
- Excel-based assessment workbooks with automated compliance calculations
- Evidence registers embedded in workbooks
- Gap analysis templates
- Remediation tracking capabilities
- Python scripts for workbook generation

**Implementation Note**: Assessment methodology, workbook structures, evidence requirements, and compliance calculation procedures are defined in ISMS-IMP-A.8.15 suite.

### 3.3 Exception Management

[Organization] provides exception process for temporary non-compliance with logging requirements.

**Exception Request Process**:
- Formal exception request required for non-compliance situations
- Business justification and risk assessment required
- Compensating controls SHALL be implemented where feasible
- Time-limited exceptions (maximum 12 months, renewable with re-approval)
- CISO approval required for all exceptions
- Executive Management approval required for high-risk exceptions

**Valid Exception Scenarios**:
- Legacy systems unable to forward logs (compensating control: local log retention and manual review)
- Performance-sensitive systems where logging impacts operations (compensating control: reduced logging verbosity, targeted event logging)
- Third-party systems without logging capabilities (compensating control: alternative monitoring, change detection)
- Cost-prohibitive logging implementations (compensating control: periodic manual audits, risk acceptance)

**Exception Documentation** (SHALL include):
- System or application affected
- Logging requirement unable to meet
- Business justification for exception
- Risk assessment (likelihood and impact of non-compliance)
- Compensating controls implemented
- Exception duration and renewal conditions
- Approval signatures (Information Security Manager, CISO, System Owner)

**Exception Tracking** (SHALL maintain):
- Centralized exception register
- Quarterly exception review
- Notification before expiration (30 days)
- Automatic expiration without renewal
- Annual reporting to Executive Management on active exceptions

**Implementation Note**: Exception request templates and approval workflows are documented in ISMS-IMP-A.8.15 Implementation Guides.

### 3.4 Incident Response

[Organization] defines procedures for logging-related security incidents.

**Logging-Related Incidents** (SHALL classify):
- Log tampering detected (integrity violation, unauthorized modification)
- Log collection failure (log sources not forwarding, SIEM outage)
- Unauthorized log access (access by non-authorized users, privilege abuse)
- Log storage capacity exhaustion (unable to receive new logs)
- SIEM or log management platform compromise
- Suspicious log deletion or archival tampering
- Log forwarding credential compromise

**Incident Response Procedures** (SHALL implement):
- Immediate escalation to SOC and Information Security Manager for log-related incidents
- CISO notification for critical incidents (SIEM compromise, extensive log tampering)
- Forensic preservation of affected logs (copy to separate storage)
- Root cause analysis (technical investigation, user activity review)
- Remediation plan development (technical fixes, process improvements)
- Post-incident review (lessons learned, policy updates)

**Integration with ISMS-POL-A.5.24**:
- Logging incidents follow organizational incident response framework
- Incident classification based on severity and impact
- Incident documentation in incident management system
- Communication procedures per incident response policy
- Post-incident review incorporating logging lessons learned

**Incident Prevention** (SHALL implement):
- Automated alerting for log integrity violations
- Monitoring of log administrator activities
- Regular testing of log backup and recovery procedures
- Security hardening of SIEM and log management infrastructure
- Least privilege access to logging systems

### 3.5 Policy Governance

**Policy Review**:
- **Frequency**: Annual minimum
- **Triggers**: 
  - Regulatory changes (new laws, updated standards, guidance publications)
  - Major logging incidents (SIEM compromise, extensive log tampering, data breach involving missing logs)
  - Organizational changes (new systems, services, business lines, acquisitions)
  - Audit findings (internal audit recommendations, external audit findings, certification findings)
  - Technology changes (new SIEM, cloud migration, infrastructure modernization)
  - Threat landscape evolution (new attack patterns requiring additional logging)

**Review Process**:
- **Reviewers**: CISO (lead), Information Security Manager, SOC Lead, IT Operations Manager, DPO, Legal/Compliance
- **Approval**: CISO (technical approval), Executive Management (strategic approval)
- **Documentation**: Review findings, changes proposed, approval signatures, communication plan

**Implementation Standards Review**:
- **Frequency**: Quarterly (logging technology and threat landscape evolve rapidly)
- **Authority**: Security Team proposes updates, CISO approves
- **Scope**: ISMS-IMP-A.8.15 suite, ISMS-REF-A.8.15 technical standards
- **Note**: Implementation standard updates do NOT require policy revision or Executive Management approval

**Policy Update Classification**:

| Update Type | Examples | Approval Required | Implementation Timeline |
|------------|----------|-------------------|------------------------|
| **Minor** (Clarifications, references, corrections) | Terminology clarification, reference updates, typo fixes, non-substantive wording improvements | CISO approval | Communication within 30 days |
| **Major** (Scope changes, new requirements, significant modifications) | New log category requirements, retention period changes, new technology mandates, scope expansion | Full approval chain (CISO + Executive Management) | Implementation plan with milestones, training, communication |
| **Emergency** (Critical security issues, urgent regulatory requirements) | Critical vulnerability requiring immediate logging, emergency regulatory mandate, incident-driven emergency change | CISO approval with Executive notification | Immediate communication and implementation, retrospective documentation |

**Communication**:
- Policy published in ISMS document repository
- Changes communicated organization-wide via security bulletin
- Training provided for significant changes affecting user behavior or system owner responsibilities
- System Owners notified of changes impacting their systems
- DPO and Legal/Compliance briefed on privacy or regulatory implications

**Version Control**:
- All policy versions retained for audit trail (minimum 7 years)
- Change history documented in version history table
- Previous versions available for reference and comparison
- Document control maintained per ISMS document management procedures

---

## 4. Implementation & References

### 4.1 Integration with ISMS

**Risk Assessment Linkage** (ISO 27001 Clause 6.1):
- Logging controls selected based on organizational risk assessment
- Log retention periods based on data classification and regulatory requirements
- Review frequency based on system criticality and threat landscape
- SIEM investment justified through risk treatment decisions

**Statement of Applicability** (ISO 27001 Clause 6.1.3):
- Control A.8.15 applicability justified in organizational Statement of Applicability
- Implementation status tracked and reported quarterly
- Gaps documented with remediation plans

**Related Controls** (Integration Points):

| Related Control | Integration with Logging |
|----------------|-------------------------|
| **A.8.16 (Monitoring Activities)** | Real-time monitoring consumes logs for alerting; log review supports monitoring effectiveness; SIEM integration point |
| **A.8.17 (Clock Synchronization)** | Accurate timestamps depend on time synchronization; log correlation requires synchronized time sources |
| **A.5.24 (Incident Management)** | Logs provide evidence for incident detection and investigation; incident response triggers forensic log preservation |
| **A.8.7 (Protection against Malware)** | Malware detection events logged; logs support malware investigation and containment |
| **A.5.17 (Authentication Information)** | Authentication events logged comprehensively; password policy violations logged |
| **A.5.18 (Access Rights)** | Authorization events logged; privilege changes logged; access reviews informed by logs |
| **A.8.23 (Web Filtering)** | Web filtering events logged; blocked URL attempts logged; integration with SIEM |
| **A.8.24 (Use of Cryptography)** | Cryptographic operations logged for audit trail; certificate validation failures logged |

### 4.2 Implementation Resources

**Implementation Guidance Suite** (ISMS-IMP-A.8.15):

| Document ID | Title | Purpose | Target Audience |
|------------|-------|---------|-----------------|
| **ISMS-IMP-A.8.15.1** | Log Source Inventory Assessment | Catalog all systems and assess logging completeness | System Owners, IT Operations, Security Team |
| **ISMS-IMP-A.8.15.2** | Log Collection & Centralization Assessment | Assess SIEM infrastructure and collection reliability | SOC Team, SIEM Administrators, Security Engineers |
| **ISMS-IMP-A.8.15.3** | Log Protection & Retention Assessment | Verify integrity controls and retention compliance | Security Team, Storage Administrators, Compliance |
| **ISMS-IMP-A.8.15.4** | Log Analysis & Review Assessment | Assess review effectiveness and automation maturity | SOC Analysts, Security Managers, CISO |
| **ISMS-IMP-A.8.15.5** | Compliance Dashboard | Consolidated compliance reporting across all domains | CISO, Executive Management, Auditors |

**Assessment Tools**:
- Excel-based assessment workbooks with automated compliance calculations
- Evidence registers embedded in workbooks
- Gap analysis templates with risk scoring
- Remediation tracking capabilities with milestone tracking
- Python scripts for workbook generation (generate_a815_1 through generate_a815_5)

**Technical Reference**:
- **ISMS-REF-A.8.15**: Logging Standards Reference (detailed log format specifications, syslog configuration, CEF schemas, JSON standards, field naming conventions)

**Supporting Materials**:
- Log source onboarding templates (ISMS-IMP-A.8.15.1 Part II)
- Review procedure checklists (ISMS-IMP-A.8.15.4 Part II)
- Exception request forms (ISMS-IMP-A.8.15 Implementation Guides)
- Incident response playbooks for logging events (ISMS-POL-A.5.24 integration)
- Quick reference guides (Annex B of this policy)

### 4.3 Regulatory Mapping

Comprehensive mapping of logging requirements to regulatory frameworks:

| Requirement Domain | Swiss nDSG | EU GDPR | ISO 27001 | PCI DSS* | HIPAA* | DORA/NIS2* | SOX* |
|--------------------|-----------|---------|-----------|---------|--------|------------|------|
| **Event Logging** | Art. 8 | Art. 32 | A.8.15 | Req. 10.2 | §164.312(b) | Art. 17, 21 | Audit Trail |
| **Log Protection** | Art. 8 | Art. 32 | A.8.15 | Req. 10.3 | §164.312(b) | ICT Security | Data Integrity |
| **Log Retention** | Art. 8 | Art. 5(1)(e) | A.8.15 | Req. 10.5 | §164.316(b)(2) | Record Keeping | 7-year min |
| **Log Review** | Art. 8 | Art. 32 | A.8.15 | Req. 10.6 | §164.308(a)(1)(ii)(D) | Monitoring | Control Testing |
| **Audit Trails** | Art. 8 | Art. 30 | A.8.15 | Req. 10 | §164.312(b) | Documentation | Financial Audit |
| **Incident Response** | Art. 8 | Art. 33 | A.5.24, A.8.15 | Req. 12.10 | §164.308(a)(6) | Incident Mgmt | Disclosure |
| **Access Controls** | Art. 8 | Art. 32 | A.8.15 | Req. 10.3 | §164.312(a)(1) | Access Mgmt | Segregation |
| **Integrity Protection** | Art. 8 | Art. 32 | A.8.15 | Req. 10.3 | §164.312(c)(1) | Data Integrity | Prevent Fraud |

*Conditional applicability per ISMS-POL-00

**Compliance Verification**:
- Quarterly assessments using ISMS-IMP-A.8.15 suite
- Annual policy review incorporating regulatory landscape changes
- Internal audit verification of implementation effectiveness
- External audit validation during ISO 27001 certification
- Regulatory-specific audits (PCI DSS QSA, HIPAA assessments) where applicable

**Compliance Evidence**:
- Assessment workbooks with documented findings
- SIEM configuration and correlation rules
- Log retention compliance reports
- Review completion records
- Exception register and approvals
- Incident response records involving logs

---

## Annex A: Logging Decision Matrix

**Purpose**: Quick reference for operational logging decisions. This annex provides decision trees and selection matrices to help stakeholders determine appropriate logging requirements, retention periods, and protection mechanisms.

### A.1 Event Logging Decision Tree

**Question: "Should I Log This Event?"**

```
START: Is this system in scope per Section 1.4?
  |
  NO → Out of policy scope (consult Security Team if uncertain)
  |
  YES
  |
  ↓
Is this system processing sensitive data (Confidential or Restricted classification)?
  |
  YES → MUST LOG (Section 2.1 mandatory events apply)
  |     - Authentication (all attempts)
  |     - Authorization (all access to sensitive data)
  |     - Administrative actions (all changes)
  |     - Security events (all alerts)
  |
  NO
  |
  ↓
Is this system business-critical or required for compliance?
  |
  YES → SHOULD LOG (strong recommendation)
  |     - Authentication events
  |     - System errors and failures
  |     - Configuration changes
  |     - Application exceptions
  |
  NO → MAY LOG (optional, operational benefit)
        - Debug logs (development/troubleshooting)
        - Performance metrics
        - Non-critical informational events
```

### A.2 Retention Period Selection Matrix

**Question: "How Long Should I Retain These Logs?"**

| Log Category | Data Classification | Online Storage | Archive Storage | Total | Legal Basis |
|--------------|-------------------|----------------|-----------------|-------|-------------|
| **Authentication Logs** | Any | 12 months | 7 years | 8 years | GDPR, nDSG, ISO, PCI, HIPAA |
| **Security Events** | Any | 12 months | 7 years | 8 years | ISO, PCI, SOX, Forensics |
| **Administrative Actions** | Any | 12 months | 7 years | 8 years | SOX, ISO, Change Mgmt |
| **Database Logs (sensitive data)** | Confidential/Restricted | 12 months | 7 years | 8 years | SOX, HIPAA, GDPR |
| **Application Logs** | Internal | 6 months | 1 year | 1.5 years | Troubleshooting |
| **Network Device Logs** | Internal | 6 months | 1 year | 1.5 years | Troubleshooting |
| **System Logs (OS events)** | Internal | 6 months | 1 year | 1.5 years | Operations |

**Special Cases**:
- PCI DSS systems → Minimum 12 months online (no flexibility)
- HIPAA systems → Minimum 6 years total retention
- SOX financial systems → Minimum 7 years total retention
- GDPR with no other requirement → Document necessity, typically 6-24 months

**When in Doubt**: Use 12 months online + 7 years archive (highest common requirement)

### A.3 Log Protection Method Selection

**Question: "What Protection Level Do I Need?"**

**Decision Factors**:
1. **Data Classification**: What is the sensitivity of data accessed by the logged system?
2. **Regulatory Requirements**: Are there specific regulatory mandates (PCI, HIPAA, SOX)?
3. **Legal/Forensic Value**: Could these logs be used as legal evidence?

**Protection Recommendations**:

| Protection Level | Data Classification | Regulatory Context | Recommended Controls |
|------------------|---------------------|-------------------|---------------------|
| **MAXIMUM** | Restricted | PCI, HIPAA, SOX, Legal Hold | WORM storage + Cryptographic signing + Centralized collection + Encrypted transmission + Dual authorization for deletion |
| **HIGH** | Confidential | ISO, GDPR, DORA, NIS2 | Centralized collection + Encrypted transmission + Access controls + Integrity monitoring |
| **STANDARD** | Internal | ISO 27001 baseline | Centralized collection + Access controls + Automated backup |
| **BASIC** | Public/Non-sensitive | Operational only | Local logging + Periodic backup |

**Minimum Requirements (All Logs)**:
- Centralized collection (Section 2.2.2)
- Encrypted transmission (Section 2.2.3)
- Access controls (Section 2.2.1)
- Retention compliance (Section 2.3.1)

### A.4 Log Review Frequency Decision

**Question: "How Often Should I Review These Logs?"**

| System Criticality | Review Frequency | Responsibility | Automation |
|-------------------|------------------|----------------|------------|
| **Critical** (Payment, PHI, Financial) | Real-time + Daily | SOC + Security Team | SIEM correlation required |
| **High** (Confidential data, External-facing) | Daily | SOC | SIEM correlation recommended |
| **Medium** (Internal systems, Business apps) | Weekly | Security Team | SIEM or automated scripts |
| **Low** (Development, Test, Internal tools) | Monthly | System Owner | Manual review acceptable |

**Escalation Triggers** (Immediate Review Required):
- Critical or high severity SIEM alerts
- Multiple failed authentication attempts (threshold: 5 within 15 minutes)
- Privilege escalation events
- Administrative account usage outside business hours
- Data exfiltration indicators (large data transfers, unusual access patterns)
- Malware detection
- Log collection failures for critical systems

---

## Annex B: Quick Reference Guide

**Purpose**: One-page operational reference for common logging scenarios. This annex provides practical guidance for system owners, administrators, and security personnel implementing logging controls.

### B.1 Common Logging Scenarios

**Scenario 1: Onboarding a New System**

Checklist:
- [ ] Determine system criticality and data classification
- [ ] Identify mandatory log events per Section 2.1
- [ ] Select appropriate log format (syslog, CEF, JSON) per ISMS-REF-A.8.15
- [ ] Configure log forwarding to SIEM or centralized collection
- [ ] Set retention period per Section 2.3 and Annex A.2
- [ ] Test log collection and verify completeness
- [ ] Document log source in ISMS-IMP-A.8.15.1 inventory
- [ ] Notify SOC team of new log source

**Scenario 2: Investigating Failed Logins**

Quick Steps:
1. Query SIEM for authentication events: `EventType="Authentication.Login.Failure"`
2. Filter by time range (last 24 hours, last 7 days)
3. Group by username to identify targeted accounts
4. Group by source IP to identify attack sources
5. Check for patterns (brute force: many attempts, credential stuffing: distributed IPs)
6. If suspicious, escalate to incident response per ISMS-POL-A.5.24

**Scenario 3: Log Collection Troubleshooting**

Problem: Logs not appearing in SIEM

Troubleshooting Steps:
1. Verify log source is generating logs (check local log files)
2. Check log forwarding configuration (syslog destination, port)
3. Test network connectivity to SIEM (telnet, nc, network trace)
4. Verify firewall rules allow log forwarding traffic
5. Check SIEM parsing rules for log format compatibility
6. Review SIEM ingestion errors and dropped events
7. If still failing, contact SIEM administrators with findings

**Scenario 4: Responding to Storage Capacity Alert**

Alert: Log storage at 85% capacity

Response Actions (Priority Order):
1. Verify alert is accurate (check actual storage utilization)
2. Identify largest log sources contributing to storage growth
3. Review retention policy compliance (are old logs being archived?)
4. Initiate emergency archival of oldest logs to cold storage
5. Request storage expansion if growth exceeds planned capacity
6. Investigate unusual log volume increase (possible DoS, logging misconfiguration)
7. Document incident and update capacity planning

### B.2 Log Format Quick Reference

**When to Use Each Format**:

| Format | Best For | Example Use Cases | Technical Reference |
|--------|----------|-------------------|---------------------|
| **Syslog (RFC 5424)** | Infrastructure, network devices, OS | Firewalls, routers, Linux servers, switches | ISMS-REF-A.8.15 Section 2 |
| **CEF (Common Event Format)** | Security tools, SIEM integration | IDS/IPS, web filters, anti-malware, DLP | ISMS-REF-A.8.15 Section 3 |
| **JSON** | Applications, cloud services, APIs | Web apps, microservices, SaaS, containers | ISMS-REF-A.8.15 Section 4 |
| **Plain Text** | Legacy systems, simple logs | Older applications, basic event logs | Avoid where possible |

**Timestamp Format**: Always use ISO 8601 with timezone (e.g., `2026-01-21T14:32:15+01:00`)

### B.3 Frequently Asked Questions

**Q: What log format should I use for a new application?**  
A: JSON is recommended for modern applications. See ISMS-REF-A.8.15 Section 4 for schema standards.

**Q: How do I know if my logs are being collected?**  
A: Check SIEM dashboard or log management platform. Look for recent events from your system. If none, see "Scenario 3: Log Collection Troubleshooting" above.

**Q: Can I reduce logging to improve system performance?**  
A: Performance impact concerns should be discussed with Security Team. Exception process (Section 3.3) may be appropriate with compensating controls.

**Q: Who can access logs for my system?**  
A: SOC analysts, security engineers, and authorized incident responders. See Section 2.2.1 for access control requirements.

**Q: How long are logs kept?**  
A: Depends on log category. See Section 2.3.1 and Annex A.2 for retention matrix. Most security logs: 12 months online + 7 years archive.

**Q: What if I can't log a required event?**  
A: Submit exception request per Section 3.3. Include business justification, risk assessment, and proposed compensating controls.

**Q: How do I handle logs containing personal data (GDPR)?**  
A: Minimize personal data where possible. Ensure logs comply with privacy requirements (Section 2.5). Consult DPO for questions.

**Q: What happens if logs are tampered with?**  
A: Log tampering is a security incident. Follow incident response procedures per Section 3.4. Immediately notify SOC and Information Security Manager.

**Q: Can I delete logs early to save storage?**  
A: No. Retention periods (Section 2.3.1) are mandatory. Early deletion violates policy and may violate legal/regulatory requirements. Request exception if storage is critical concern.

**Q: How do I export logs for forensic analysis?**  
A: Contact SOC or SIEM administrators. Forensic exports require approval from Information Security Manager and maintain chain of custody.

### B.4 Emergency Contact Information

**Log-Related Incidents**:
- **SOC Team**: [Contact Information]
- **Information Security Manager**: [Contact Information]
- **CISO**: [Contact Information] (critical incidents only)

**Technical Support**:
- **SIEM Administrators**: [Contact Information]
- **IT Operations On-Call**: [Contact Information]

**Compliance Questions**:
- **Data Protection Officer (DPO)**: [Contact Information]
- **Legal/Compliance Officer**: [Contact Information]

---

## Approval Record

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Chief Information Security Officer (CISO)** | [Name] | | [Date] |
| **Information Security Manager** | [Name] | | [Date] |
| **Security Operations Center (SOC) Lead** | [Name] | | [Date] |
| **IT Operations Manager** | [Name] | | [Date] |
| **Data Protection Officer (DPO)** | [Name] | | [Date] |
| **Legal/Compliance Officer** | [Name] | | [Date] |
| **Executive Management (GL)** | [Name] | | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for event logging controls. Implementation procedures are documented in ISMS-IMP-A.8.15. Technical standards are documented in ISMS-REF-A.8.15.*