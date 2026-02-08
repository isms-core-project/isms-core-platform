**ISMS-OP-POL-A.8.15 — Logging**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Logging |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.15 |
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
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.8.15 — Logging
- See also: ISMS-OP-POL-A.8.16 (Monitoring Activities), ISMS-OP-POL-A.8.17 (Clock Synchronisation)

**Related Annex A Controls**:

| Control | Relationship to Logging |
|---------|------------------------|
| A.5.7 Threat intelligence | Threat intelligence informs monitoring rules and detection patterns |
| A.5.15–18 Access control and identity management | Authentication and access events are primary log sources |
| A.5.24–28 Incident management | Log analysis supports incident detection, investigation, and evidence |
| A.5.28 Collection of evidence | Logs serve as forensic evidence; integrity must be preserved |
| A.5.34 Privacy and protection of PII | Employee monitoring must comply with privacy requirements |
| A.8.1 User endpoint devices | Endpoint events logged for security monitoring |
| A.8.7 Protection against malware | Malware detection events logged and forwarded |
| A.8.8 Management of technical vulnerabilities | Vulnerability scan results logged |
| A.8.20 Network security | Network traffic and security events logged |

**Related Internal Policies**:

- Access Control Policy
- Incident Management Policy
- Privacy and Protection of PII Policy
- Network Security Policy
- Endpoint Security Policy
- Information Classification and Handling Policy

---

# Logging Policy

## Purpose

The purpose of this policy is to address the identification and management of security events through the logging of information processing systems. Logs provide the evidence trail for incident detection, investigation, compliance verification, and forensic analysis.

This policy supports Swiss nFADP (revDSG) and the Data Protection Ordinance (DSV) by implementing logging as a technical and organisational measure appropriate to risk, including the specific logging obligations under DSV Art. 4 for processing of sensitive personal data. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply. For monitoring activities, see ISMS-OP-POL-A.8.16. For clock synchronisation, see ISMS-OP-POL-A.8.17.

## Scope

All employees and third-party users.

All devices, systems, and applications used to process, store, or transmit organisation information deemed in scope by the ISO 27001 scope statement.

## Principle

All systems that process, store, or transmit confidential or personal information shall have logging enabled where logging is possible and practical. Logs shall be collected centrally, protected from tampering, retained for a defined period, and reviewed regularly to detect security events.

---

## Event Logging

### Events to Log

Event logs recording user activities, exceptions, faults, and information security events shall be produced, kept, and regularly reviewed. The following events shall be logged:

| # | Event Category | Details |
|---|---------------|---------|
| 1 | **Authentication events** | Successful and rejected logon and logoff attempts, including remote access (VPN, web applications) |
| 2 | **Data and resource access** | Successful and rejected attempts to access files, databases, applications, and network resources |
| 3 | **System configuration changes** | Changes to system settings, security parameters, network configuration, and firewall rules |
| 4 | **Use of elevated privileges** | All actions performed with administrative, root, or sudo access |
| 5 | **System utilities and applications** | Use of privileged utility programs, maintenance tools, and diagnostic utilities |
| 6 | **File operations** | File creation, modification, deletion, and migration on critical systems |
| 7 | **Access control alarms** | Account lockouts, threshold violations, and intrusion detection alerts |
| 8 | **Security system changes** | Activation, deactivation, or modification of antivirus, firewall, IDS/IPS, and other protection systems |
| 9 | **Identity management** | Creation, modification, deletion, and disabling of user accounts and permissions |
| 10 | **Application transactions** | Transactions executed by users in business-critical applications (financial systems, HR, CRM) |

### Log Entry Content

Each log entry shall include, at minimum:

| Field | Description |
|-------|-------------|
| **User/Account ID** | The account that performed the action |
| **Timestamp** | Date and time in ISO 8601 format, synchronised to the organisation's reference time source |
| **Event type** | Description of what occurred (logon, file access, configuration change, etc.) |
| **Success or failure** | Whether the action succeeded or was rejected |
| **System/Device ID** | Hostname, asset ID, or IP address of the system where the event occurred |
| **Source address** | Source IP address or network location (where applicable) |

---

## Event Logging Access Control

Event logging and monitoring shall be performed by authorised personnel only.

Event logs and monitoring systems shall be protected and access restricted in line with the Access Control Policy. Access to raw logs shall be limited to the information security management team and authorised IT personnel.

System administrators shall not have permission to erase or deactivate logs of their own activities. Where this is not technically enforceable, compensating controls shall be implemented (e.g., forwarding logs to a central system outside the administrator's control, periodic review of administrator activity by a separate role).

---

## Protection of Event Log Information

Logging facilities and log information shall be protected against tampering and unauthorised access.

Controls shall protect against:

- **Alteration** of recorded log entries or message types.
- **Deletion** of log files or individual entries.
- **Storage exhaustion** causing loss of log data (logs shall fail open — alert when storage reaches **80% capacity** rather than silently overwriting). Log storage capacity shall be monitored continuously, with automated alerts at 80% and 90% thresholds. When 90% capacity is reached, archived logs shall be offloaded to long-term storage and the platform team shall assess whether additional capacity is required.
- **Unauthorised access** to log data (logs may contain personal data and are classified as INTERNAL minimum).

Log protection shall be achieved through:

- Forwarding logs to a **centralised logging system** separate from the source systems.
- **Append-only** or **write-once** storage for log data where technically feasible.
- **Cryptographic integrity checks** (hashing) to detect tampering where required for forensic or legal purposes.
- **Access controls** restricting log modification to authorised security personnel only.

---

## Centralised Logging

### Centralised Logging Platform

The centralised logging platform shall meet the following requirements:

| Requirement | Specification |
|-------------|---------------|
| **Platform type** | SIEM, log aggregator, or equivalent (e.g., Splunk, Microsoft Sentinel, Elastic SIEM, Wazuh, or equivalent) |
| **Deployment** | Separate from source systems; source system administrators shall not have administrative access |
| **Storage** | Sufficient capacity for defined retention periods; 80% capacity alert threshold |
| **Search** | Full-text and structured query capability for incident investigation and compliance queries |
| **Alerting** | Configurable rules with notification to the information security management team (email, SMS, ticketing system) |
| **Integrity** | Append-only or write-once storage; cryptographic integrity checks where required |
| **Access control** | Role-based access; read-only for analysts; administrative access restricted to platform administrators |

Logs from all critical systems shall be forwarded to the centralised logging platform. The platform shall be:

- **Separate** from the systems generating the logs (source system administrators shall not have administrative access to the central log store).
- **Searchable** to support incident investigation and compliance queries.
- **Alerting-capable** to notify the information security management team of high-risk events.
- **Protected** with the same or higher security controls as the source systems.

Systems to be included in centralised logging as a minimum:

- Authentication and identity systems (Active Directory, identity providers, SSO).
- Firewalls and network security devices.
- Servers hosting confidential or personal data.
- Email and web gateways.
- VPN and remote access systems.
- Endpoint detection and response (EDR) systems.
- Cloud service administrative consoles (Microsoft 365, AWS, Azure, etc.).

Where automated centralised logging is not feasible for a specific system, manual log collection and review shall be performed at a defined frequency with documented justification.

---

## Administrator and Operator Logs

System administrator and system operator activities shall be logged, and the logs protected and regularly reviewed.

Privileged account holders may be able to manipulate logs on systems under their direct control. To maintain accountability for privileged users:

- Administrator actions shall be forwarded to the centralised logging system in real-time or near-real-time.
- A periodic review of privileged user activity shall be conducted (at least quarterly).
- Anomalous privileged activity (e.g., after-hours access, bulk data operations, security configuration changes) shall generate alerts.

---

## Clock Synchronisation

Log timestamps shall be accurate and consistent across all systems. Clock synchronisation requirements are defined in **ISMS-OP-POL-A.8.17 — Clock Synchronisation**. All systems generating log data shall comply with A.8.17 time source and drift tolerance requirements.

---

## Event Log Review

### Review Requirements

Responsibilities shall be assigned for the analysis and monitoring of security events.

| Review Type | Frequency | Owner | Scope |
|-------------|-----------|-------|-------|
| **Automated alerting** | Real-time | Information Security | High-risk events trigger immediate notification to the information security management team |
| **Security event review** | Weekly | Information Security Analyst | All security events, authentication failures, access anomalies |
| **Privileged activity review** | Quarterly | CISO / Information Security Manager | Administrator and operator actions, privilege escalations |
| **Full log review** | Monthly | Information Security | Trends, patterns, and anomalies across all log sources |
| **Log source coverage audit** | Quarterly | IT Operations | Verify all in-scope systems are forwarding logs; identify gaps |

### High-Risk Events

The following events shall trigger immediate automated alerts and be escalated to the incident management process:

| # | High-Risk Event | Alert Threshold | Response |
|---|----------------|-----------------|----------|
| 1 | Multiple failed authentication attempts | **5 failures** within 10 minutes (single account) or **20 failures** within 10 minutes (multiple accounts from single source) | Account lockout; investigate source |
| 2 | Successful authentication from unexpected locations | Login from new country or IP range not in baseline | Verify with user; suspend if unconfirmed |
| 3 | Disabling or modification of security controls | Any change to antivirus, firewall rules, or logging configuration | Immediate alert to information security |
| 4 | Bulk data access, download, or deletion | **>500 files** or **>1 GB** accessed/downloaded within 1 hour by a single user | Investigate; suspend access if warranted |
| 5 | Creation of new privileged accounts or elevation of privileges | Any new admin/root account or privilege escalation | Verify authorisation against change records |
| 6 | Detection of malware or intrusion attempts | Any confirmed detection | Incident management process |
| 7 | Modification or deletion of log files | Any attempt | Immediate alert; forensic investigation |

### Incident Escalation from Monitoring

When a high-risk event is detected, the following escalation process shall be followed:

1. **Alert**: Automated alert generated and sent to the information security management team.
2. **Triage** (within **30 minutes** during business hours; **2 hours** outside business hours): Analyst assesses the alert, determines if it is a true positive, false positive, or requires investigation.
3. **Investigation**: If confirmed as a potential security event, an incident record is created per the Incident Management Policy.
4. **Escalation**: Incidents classified as High or Critical are escalated to the CISO immediately.

---

## Event Log Retention

| Log Type | Online (Searchable) | Archive (Retrievable) | Total Retention |
|----------|--------------------|-----------------------|----------------|
| Security events (authentication, access control) | 90 days | 9 months | **12 months** |
| System and infrastructure logs | 90 days | 6 months | **9 months** |
| Application logs | 90 days | 6 months | **9 months** |
| Firewall and network security logs | 90 days | 9 months | **12 months** |
| Sensitive personal data processing logs (DSV Art. 4) | 90 days | 9 months | **12 months** (minimum per DSV) |
| Financial system logs | 90 days | Per legal retention | **Per Swiss CO Art. 958f** |

**Retention rationale**: Security event and firewall logs are retained for 12 months to support incident investigation (average dwell time for advanced threats is 10–21 days, and regulatory investigations may span 12 months). System and application logs are retained for 9 months to balance operational utility with storage costs. DSV Art. 4 logs require a minimum 12 months per regulation.

### Log Archival and Retrieval

Archived logs shall be encrypted, stored in a secure location, and retrievable within the following timeframes:

| Archive Age | Retrieval Target |
|-------------|-----------------|
| 0–90 days (online) | Immediate (searchable in platform) |
| 91 days – 6 months | Within **4 hours** |
| 6–12 months | Within **24 hours** |
| >12 months (if retained for legal/regulatory) | Within **5 business days** |

Retrieval procedures shall be tested at least annually to verify that archived logs are accessible and intact.

Logs shall not be retained longer than necessary. When retention periods expire, logs shall be securely deleted in line with the Information Classification and Handling Policy.

---

## Swiss nFADP — DSV Article 4 Logging Obligations

Where the organisation processes sensitive personal data (nFADP Art. 5) automatically at large scale or performs high-risk profiling, the following additional logging requirements apply per DSV Art. 4:

**Operations to log**: Storage, alteration, reading, disclosure, deletion, and destruction of sensitive personal data.

**Log content**: Identity of the person or system performing the processing, type of processing, and date and time.

**Log storage**: Logs of sensitive personal data processing shall be stored **separately** from the processing system, retained for a minimum of **1 year**, and access restricted to verifying data security compliance and ensuring confidentiality, integrity, availability, and traceability.

### DSV Art. 4 Applicability Assessment

The organisation shall determine whether DSV Art. 4 applies by assessing the following criteria:

| Criterion | Assessment |
|-----------|-----------|
| Does the organisation process **sensitive personal data** (nFADP Art. 5)? | Yes / No |
| Is the processing **automated** (not purely manual/paper-based)? | Yes / No |
| Is the processing at **large scale** (volume of data subjects, data volume, geographic scope)? | Yes / No |
| Does the organisation perform **high-risk profiling**? | Yes / No |

If the answer to the first criterion AND any of the remaining criteria is **Yes**, DSV Art. 4 logging obligations apply. Where the organisation is uncertain whether Art. 4 applies, implementing these logging requirements is recommended as best practice.

---

## Personal Privacy

The privacy of employees and customers shall be respected in line with Swiss nFADP and applicable legal requirements when implementing logging.

### Employee Monitoring Principles

- Logging systems shall serve **legitimate security purposes** (detecting threats, investigating incidents, verifying compliance) — not primarily for monitoring employee behaviour.
- Employees shall be **informed in advance** that logging takes place, what is logged, and why, through the information security awareness programme and employment documentation.
- Only the **minimum necessary data** shall be collected and retained (data minimisation).
- Access to logs containing employee data shall be restricted to authorised security and compliance personnel only — not line managers for general browsing.
- **Keystroke logging** and **continuous individual activity surveillance** are disproportionate and shall not be implemented.
- Where logs containing personal data are shared with external parties (e.g., vendors for troubleshooting), personal identifiers shall be masked or anonymised.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; approval of monitoring scope; escalation point for critical alerts; quarterly privileged activity review |
| **Information Security Analyst** | Daily/weekly log review; alert triage; incident escalation; detection rule maintenance |
| **IT Operations / Platform Team** | Logging platform administration; capacity management; log source onboarding; NTP configuration; archival |
| **System Administrators** | Ensuring logging is enabled on managed systems; cooperating with log source onboarding; reporting logging failures |
| **Data Protection Advisor** | Guidance on DSV Art. 4 applicability; privacy impact of monitoring activities; employee notification requirements |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Centralised logging platform** configuration and log source inventory | IT Operations | *Log source inventory reviewed quarterly; configuration documented* |
| 2 | **Sample log entries** demonstrating required fields are captured | Information Security | *Verified annually during audit; sample of 5 systems* |
| 3 | **Log protection controls** (access restrictions, append-only storage, integrity checks) | IT Operations | *Configuration reviewed annually; access logs retained 12 months* |
| 4 | **Clock synchronisation** compliance per ISMS-OP-POL-A.8.17 (NTP source, drift monitoring, alert threshold) | IT Operations | *See ISMS-OP-POL-A.8.17 evidence requirements* |
| 5 | **Log retention configuration** matching defined retention periods | IT Operations | *Verified semi-annually; archival retrieval tested annually* |
| 6 | **Security event review records** (weekly reviews, quarterly privileged activity reviews) | Information Security | *Weekly review logs retained 12 months; quarterly reviews presented at management review* |
| 7 | **Alerting rules** and sample alert notifications for high-risk events | Information Security | *Rules reviewed quarterly; sample alerts retained 12 months* |
| 8 | **DSV Art. 4 compliance records** (applicability assessment; sensitive personal data processing logs stored separately) | Data Protection Advisor | *Applicability assessment reviewed annually; log separation verified quarterly* |
| 9 | **Employee notification records** (awareness training, privacy notice regarding monitoring) | HR / Information Security | *Updated per policy change; training completion tracked annually* |
| 10 | **Log source coverage metric** (percentage of in-scope systems forwarding logs) | IT Operations | *Quarterly; target: 100% of critical systems, ≥95% of all in-scope systems* |

---

# Policy Compliance

## Compliance Measurement

The information security management team shall verify compliance with this policy through various methods, including but not limited to, log source coverage audits, retention compliance checks, log review completion, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to logging standards, regulatory requirements (including DSV updates), and lessons learned from incidents.

---

# Areas of the ISO 27001 Standard Addressed

Logging Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 5.37 Documented operating procedures |
| Clause 9.1 Monitoring, measurement, analysis, and evaluation | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | **8.15 Logging** |
| | 8.16 Monitoring activities *(see ISMS-OP-POL-A.8.16)* |
| | 8.17 Clock synchronisation *(see ISMS-OP-POL-A.8.17)* |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures; Art. 6 — Proportionality of monitoring |
| Swiss DSV (Data Protection Ordinance) | Art. 4 — Logging obligations for sensitive personal data processing |
| Swiss CO (Code of Obligations) | Art. 328b — Employee data processing limitations; Art. 958f — Business record retention |
| EU GDPR (where applicable) | Art. 32 — Security of processing (logging as appropriate measure) |
| ISO/IEC 27001:2022 | Annex A Control 8.15 (see also 8.16, 8.17) |
| ISO/IEC 27002:2022 | Section 8.15 — Implementation guidance |
| NIST SP 800-53 Rev 5 | AU-2 (Event Logging), AU-3 (Content of Audit Records), AU-6 (Audit Review/Analysis), AU-8 (Time Stamps), AU-9 (Protection of Audit Information), AU-11 (Audit Record Retention) |
| NIST SP 800-92 | Guide to Computer Security Log Management |
| CIS Controls v8 | Control 8 (Audit Log Management) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
