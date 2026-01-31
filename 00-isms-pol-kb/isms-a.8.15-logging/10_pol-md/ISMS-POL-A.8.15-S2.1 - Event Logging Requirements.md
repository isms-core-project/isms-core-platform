# ISMS-POL-A.8.15-S2.1
## Logging - Event Logging Requirements

**Document ID**: ISMS-POL-A.8.15-S2.1  
**Title**: Logging - Event Logging Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager / SOC Lead | Initial event logging requirements |

**Review Cycle**: Semi-annual (or upon significant infrastructure changes or security incidents)  
**Next Review Date**: [Approval Date + 6 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Information Security Manager / Security Architect
- Operational Review: IT Operations Manager / System Owners
- SOC Review: Security Operations Center Lead

**Distribution**: Security team, SOC analysts, IT operations, system administrators, application developers  
**Related Documents**: ISMS-IMP-A.8.15.1 (Log Source Inventory), ISMS-POL-A.8.17 (Clock Synchronization)

---

## 2.1.1 Purpose and Scope

This section establishes **mandatory requirements** for WHAT events must be logged, WHERE they are logged, and HOW log events should be structured. These requirements ensure the organization has sufficient visibility to detect, investigate, and respond to security incidents.

**In Scope**: Event types, log sources, log content standards, log format specifications  
**Primary Stakeholders**: System Owners, Application Developers, Security Engineers, SOC Analysts  
**Implementation Evidence**: ISMS-IMP-A.8.15.1 (Log Source Inventory Assessment), ISMS-IMP-A.8.15.2 (Log Collection Assessment)

**Key Principle**: *"What isn't logged, can't be investigated."* However, organizations must balance comprehensive logging with storage costs, performance impact, and privacy considerations.

---

## 2.1.2 Authentication Logging Requirements

### 2.1.2.1 Successful Authentication Events

All systems providing user authentication **SHALL** log:

- **User login events**, including:
  - User identifier (username, email, employee ID)
  - Timestamp (date and time with timezone)
  - Source IP address and hostname (where user connected from)
  - Authentication method used (password, MFA, certificate, SSO, biometric)
  - Target system or application being accessed
  - Session identifier (where applicable)
- Interactive logins (user physically or remotely logging in)
- Non-interactive logins (service accounts, scheduled tasks, API authentication)
- SSO/federated authentication events
- Multi-factor authentication (MFA) verification events

### 2.1.2.2 Failed Authentication Events

All systems **SHALL** log failed authentication attempts, including:

- User identifier attempted (even if invalid/non-existent)
- Timestamp of failed attempt
- Source IP address
- Reason for failure (invalid password, account locked, account disabled, expired password, MFA failure)
- Number of consecutive failures (if tracked by system)

**Rationale**: Failed authentication attempts indicate potential brute-force attacks, password guessing, or compromised credentials.

### 2.1.2.3 Account Lockouts and Unlocks

Systems implementing account lockout policies **SHALL** log:

- Account lockout events (user ID, timestamp, reason, source of triggering attempt)
- Account unlock events (user ID, timestamp, administrator who unlocked, justification)

### 2.1.2.4 Password Changes

All systems **SHALL** log:

- Password change events (user ID, timestamp, source IP)
- Password reset events (user ID, timestamp, administrator who performed reset)
- Self-service password reset events
- Expired password notifications and forced changes

**Privacy Note**: Passwords themselves SHALL NEVER be logged. Log only the fact that a password was changed.

### 2.1.2.5 Session Events

Systems supporting session management **SHOULD** log:

- Session start (upon successful authentication)
- Session end (logout, timeout, forced termination)
- Session duration
- Concurrent session detection (same user, multiple sessions)

---

## 2.1.3 Authorization Logging Requirements

### 2.1.3.1 Access Grants

Systems **SHALL** log when access is granted to resources, including:

- User identifier requesting access
- Resource being accessed (file, database, application, API endpoint)
- Type of access granted (read, write, execute, delete, admin)
- Timestamp
- Source IP address
- Outcome (granted, denied)

**Note**: For high-volume systems, organizations MAY limit access logging to sensitive resources (defined by data classification) to manage log volume.

### 2.1.3.2 Access Denials

Systems **SHALL** log when access is denied, including:

- User identifier attempting access
- Resource attempted
- Type of access attempted
- Reason for denial (insufficient permissions, resource not found, policy violation)
- Timestamp
- Source IP address

**Rationale**: Access denials may indicate unauthorized access attempts, misconfigured permissions, or insider threats testing boundaries.

### 2.1.3.3 Permission Changes

Systems **SHALL** log changes to access permissions, including:

- User/group whose permissions changed
- Resource affected
- Old permissions vs. new permissions
- Administrator who made the change
- Timestamp
- Justification (if required by change management process)

---

## 2.1.4 Administrative Action Logging

### 2.1.4.1 User and Group Management

Systems **SHALL** log administrative actions including:

- **User account creation** (new user ID, created by, timestamp, assigned roles/groups)
- **User account deletion** (deleted user ID, deleted by, timestamp, justification)
- **User account modification** (user ID, changes made, modified by, timestamp)
- **Group creation/deletion/modification**
- **Role assignment changes** (user ID, role added/removed, changed by, timestamp)
- **Privilege escalation** (user granted administrative rights)
- **Privilege revocation** (user's administrative rights removed)

### 2.1.4.2 Configuration Changes

Systems **SHALL** log configuration changes, including:

- **System configuration changes** (what setting changed, old value, new value, changed by)
- **Security policy changes** (firewall rules, access policies, audit settings)
- **Network configuration changes** (IP addresses, routing, VLANs)
- **Application configuration changes** (connection strings, feature flags, business rules)
- **Service start/stop/restart events**
- **Software installation/uninstallation**
- **Patch/update application**

### 2.1.4.3 Data Manipulation

Systems **SHALL** log administrative data operations, including:

- **Bulk data modifications** (mass updates, imports, exports)
- **Database schema changes** (CREATE/ALTER/DROP TABLE, stored procedures)
- **Data restoration from backup**
- **Data archival or deletion** (especially for sensitive data)

### 2.1.4.4 Privileged Session Logging

For privileged users (administrators, root, SYSTEM), systems **SHOULD**:

- Log all commands executed during privileged sessions
- Capture full command-line arguments (excluding passwords)
- Record interactive session activity
- Implement session recording for critical systems (playback capability)

---

## 2.1.5 Security Event Logging

### 2.1.5.1 Security Tool Events

Security infrastructure **SHALL** log:

- **Firewall events** (allowed connections, blocked connections, rule matches)
- **Intrusion Detection/Prevention (IDS/IPS) alerts** (signature matches, anomalies)
- **Anti-malware detections** (malware found, quarantined, deleted)
- **Data Loss Prevention (DLP) events** (policy violations, data exfiltration attempts)
- **Web filtering events** (blocked sites, allowed sites for sensitive categories)
- **Email gateway events** (spam blocked, phishing blocked, malware attachments)
- **Endpoint Detection and Response (EDR) events** (suspicious behavior, IOCs)

### 2.1.5.2 Vulnerability and Scanning Events

Systems **SHOULD** log:

- Vulnerability scan results (what was scanned, findings, severity)
- Patch deployment events (what patch, which systems, success/failure)
- Security assessment activities (penetration tests, audits)

### 2.1.5.3 Incident Response Events

Systems **SHALL** log:

- Incident declaration and classification
- Incident investigation activities
- Evidence collection actions
- System isolation or quarantine events
- Incident resolution actions

---

## 2.1.6 System Logging Requirements

### 2.1.6.1 Operating System Events

Operating systems (Windows, Linux, Unix, macOS) **SHALL** log:

- **System start and shutdown** (clean shutdown vs. unexpected crash)
- **Service and daemon start/stop** (critical services)
- **System errors and failures** (kernel panics, blue screens, hardware failures)
- **Resource exhaustion events** (disk full, memory exhausted, CPU overload)
- **Time synchronization events** (NTP synchronization success/failure)
- **Audit policy changes** (enabling/disabling logging)

### 2.1.6.2 Application Events

Applications **SHOULD** log:

- Application start and stop
- Application errors and exceptions (with stack traces for debugging)
- Unhandled exceptions and crashes
- Performance degradation events
- Connection pool exhaustion
- Database connection failures

### 2.1.6.3 Scheduled Task Execution

Systems **SHALL** log:

- Scheduled task/job execution (task name, start time, end time, outcome)
- Cron job execution (for Unix/Linux systems)
- Windows Task Scheduler execution
- Failures to execute scheduled tasks

---

## 2.1.7 Application Logging Requirements

### 2.1.7.1 Web Application Events

Web applications **SHALL** log:

- Page access (URL, user, timestamp, HTTP method, response code)
- Form submissions (for audit-significant forms, not all forms)
- File uploads and downloads
- API calls (endpoint, method, user/API key, response code, response time)
- Error pages served (404, 500, 403)

### 2.1.7.2 Business Transaction Events

Applications processing sensitive or audit-significant transactions **SHALL** log:

- Transaction initiation (transaction ID, user, timestamp, transaction type)
- Transaction completion (outcome: success/failure/cancelled)
- Transaction modifications or cancellations
- Approval workflow events (who approved, timestamp, decision)

**Privacy Consideration**: Log transaction metadata (who, what, when) but avoid logging sensitive transaction details (e.g., credit card numbers, health information) unless specifically required.

### 2.1.7.3 Database Application Events

Database applications **SHALL** log:

- Database connections (user, source IP, database, timestamp)
- Failed connection attempts
- Queries on sensitive tables (SELECT/INSERT/UPDATE/DELETE)
- Schema modifications (DDL: CREATE/ALTER/DROP)
- Permission grants (GRANT/REVOKE)
- Stored procedure execution
- Backup and restore operations

---

## 2.1.8 Network Device Logging Requirements

### 2.1.8.1 Network Infrastructure

Network devices **SHALL** log:

- **Firewall events**: Connection attempts (allowed/blocked), rule matches, NAT translations
- **Router events**: Routing changes, BGP peering, interface up/down
- **Switch events**: Port status changes, VLAN changes, spanning tree events
- **Load balancer events**: Pool member status, health checks, failovers
- **VPN concentrator events**: VPN session establishment/termination, tunnel status

### 2.1.8.2 Wireless Infrastructure

Wireless network infrastructure **SHALL** log:

- Client associations and disassociations
- Authentication attempts (successful and failed)
- Rogue access point detection
- Wireless intrusion detection events

### 2.1.8.3 DHCP and DNS

DHCP and DNS servers **SHOULD** log:

- DHCP address assignments (client MAC, assigned IP, lease duration)
- DNS queries (requestor, domain queried, response)
- DNS failures (NXDOMAIN, timeouts)

**Privacy Note**: DNS query logging may reveal user web browsing patterns. Implement appropriate access controls and retention limits.

---

## 2.1.9 Cloud Services Logging Requirements

### 2.1.9.1 Cloud Infrastructure (IaaS)

Cloud infrastructure services **SHALL** log:

- Virtual machine creation/deletion/modification
- Storage resource access (object storage, block storage)
- Network security group changes (firewall rules)
- IAM policy changes (permissions, roles)
- API calls to cloud provider management plane

### 2.1.9.2 Cloud Platform (PaaS)

Cloud platform services **SHALL** log:

- Application deployment events
- Scaling events (auto-scaling triggered)
- Configuration changes
- Application errors and exceptions

### 2.1.9.3 Cloud Software (SaaS)

Cloud software applications **SHALL** log:

- User authentication (login/logout)
- Administrative actions (user provisioning, permission changes)
- Data access (for sensitive data classifications)
- Configuration changes
- Integration/API usage

**Implementation**: SaaS logging typically requires configuration of audit log forwarding to organization's SIEM or log management system.

---

## 2.1.10 Log Content Standards

### 2.1.10.1 Mandatory Log Fields

Every log event **SHALL** include at minimum:

- **Timestamp**: Date and time of event (see section 2.1.11 for format requirements)
- **Event Source**: System, application, or device generating the log
- **Event Type**: Category of event (authentication, authorization, admin, security, system, error)
- **Event Outcome**: Success, failure, error (where applicable)
- **Actor**: User, process, or system that initiated the event
- **Action**: What action was performed (login, access file, modify config, etc.)

### 2.1.10.2 Recommended Log Fields

Log events **SHOULD** include where applicable:

- **Source IP Address**: Origin of the request or action
- **Destination IP Address**: Target of the action (for network events)
- **Session ID**: Unique identifier for user session
- **Transaction ID**: Unique identifier for multi-step transactions
- **Object**: Resource being accessed or modified (file path, database record, API endpoint)
- **Previous Value / New Value**: For configuration or data changes
- **Severity/Priority**: Criticality of the event (INFO, WARNING, ERROR, CRITICAL)

### 2.1.10.3 Fields to Exclude (Privacy and Security)

Log events **SHALL NOT** include:

- **Passwords** (plaintext or hashed)
- **Cryptographic keys or certificates**
- **Authentication tokens** (API keys, session tokens, OAuth tokens)
- **Full credit card numbers** (PCI DSS prohibits logging PANs)
- **Social Security Numbers** or other national identifiers
- **Full medical record details** (HIPAA considerations)
- **Message content** from emails, chats, or documents (log metadata only)

**Exception**: Where logging of sensitive data is legally required (e.g., financial transaction logs), implement appropriate access controls and encryption.

---

## 2.1.11 Log Format and Time Standards

### 2.1.11.1 Timestamp Requirements

All log events **SHALL** include timestamps with:

- **Precision**: Minimum 1-second precision (millisecond precision preferred for high-volume systems)
- **Timezone**: Explicitly specified (UTC recommended for global organizations, local time acceptable if consistently applied)
- **Format**: ISO 8601 format (YYYY-MM-DDTHH:MM:SS.sssZ) preferred
- **Time Synchronization**: All systems SHALL be time-synchronized per ISMS-POL-A.8.17 (Clock Synchronization)

**Example**: `2026-01-06T14:32:15.123Z` (UTC) or `2026-01-06T15:32:15.123+01:00` (CET)

**Rationale**: Accurate, consistent timestamps are essential for log correlation and forensic timeline reconstruction.

### 2.1.11.2 Supported Log Formats

Log events **SHOULD** use one of the following standard formats:

**Syslog (RFC 5424)**:
- Universal protocol supported by nearly all systems
- Structured and unstructured message formats
- Severity levels (0-7) and facility codes
- Example: `<134>1 2026-01-06T14:32:15.123Z hostname appname procid msgid - User login successful`

**Common Event Format (CEF)**:
- Developed by ArcSight, widely supported by SIEM platforms
- Structured key-value format
- Example: `CEF:0|Vendor|Product|Version|EventID|EventName|Severity|src=192.168.1.100 suser=jdoe`

**JSON (JavaScript Object Notation)**:
- Modern structured format, increasingly common in cloud services
- Easily parsed and indexed by log management systems
- Example: `{"timestamp":"2026-01-06T14:32:15.123Z","user":"jdoe","action":"login","outcome":"success"}`

Organizations **MAY** use vendor-specific formats where standard formats are not supported, but SHALL document format specifications for parsing.

### 2.1.11.3 Character Encoding

Log files **SHALL** use UTF-8 encoding to support international characters and ensure consistent parsing.

---

## 2.1.12 Log Volume Management

### 2.1.12.1 Volume Considerations

Organizations **SHALL**:

- Estimate daily log volume per source (MB/day or GB/day)
- Plan storage capacity for retention requirements (see S2.3)
- Implement log filtering or sampling for extremely high-volume sources where full logging is not feasible

### 2.1.12.2 High-Volume Source Strategies

For systems generating excessive log volume, organizations **MAY**:

- **Sample logs** (capture representative subset, e.g., 10% of requests)
- **Filter low-value events** (exclude routine successful operations, retain errors and security events)
- **Summarize logs** (aggregate counts instead of individual events)
- **Use tiered logging** (verbose logging for errors, summary logging for normal operations)

**Critical Requirement**: Security-relevant events (authentication failures, access denials, security alerts) SHALL NEVER be sampled or filtered out.

---

## 2.1.13 Logging Performance and Availability

### 2.1.13.1 Performance Requirements

Logging mechanisms **SHALL**:

- Impose minimal performance impact on logged systems (target: <5% overhead)
- Use asynchronous logging where possible to avoid blocking application threads
- Implement local buffering to handle temporary log collector unavailability

### 2.1.13.2 Logging Availability

Systems **SHALL**:

- Continue operating even if logging fails (fail-open for application availability)
- Alert administrators when logging fails or falls behind
- Retain logs locally if centralized log collector is unavailable (up to local disk capacity)
- Resume forwarding logs when collector becomes available

**Exception**: For systems where logging is legally required (e.g., financial transactions, healthcare records), systems MAY fail-closed (refuse operations) if logging is unavailable. This decision shall be documented and risk-accepted.

---

## 2.1.14 Exceptions to Logging Requirements

### 2.1.14.1 When Exceptions May Be Granted

Exceptions to logging requirements **MAY** be approved for:

- Systems with technical limitations preventing logging implementation
- Legacy systems nearing end-of-life (decommission plan required)
- Systems handling no sensitive data and posing minimal security risk
- Performance-critical systems where logging measurably degrades service

### 2.1.14.2 Exception Process

Organizations requesting logging exceptions **SHALL**:

- Document business or technical justification
- Identify compensating controls (enhanced monitoring, network-based detection, isolated network segment)
- Obtain risk acceptance from system owner and CISO
- Review exceptions annually for continued necessity
- Plan remediation path (upgrade, replacement, decommission)

### 2.1.14.3 Non-Negotiable Requirements

The following logging requirements **SHALL NOT** be waived under any circumstances:

- Authentication logging for systems processing sensitive data
- Administrative action logging for privileged access
- Security event logging (malware, intrusions, policy violations)
- Logging for systems subject to regulatory audit requirements

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-POL-A.8.15-S2.1 |
| **ISO 27001:2022 Control** | Annex A Control 8.15 (Logging) |
| **ISO 27002:2022 Section** | 8.15 (Event logging) |
| **Document Type** | Policy Section - Detailed Requirements |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Page Count** | [Auto-generated] |
| **Word Count** | ~3,200 words |
| **Line Count** | ~395 lines |
| **Parent Policy** | ISMS-POL-A.8.15 (Master) |
| **Related Sections** | S1, S2, S2.2, S2.3, S2.4 |
| **Implementation Evidence** | ISMS-IMP-A.8.15.1, ISMS-IMP-A.8.15.2 |

---

**END OF SECTION S2.1**

---

*"The difference between screwing around and science is writing it down."*  
— Adam Savage (applies equally to security incidents and logging)

*"In the end, all that matters is what you can prove. And you can only prove what you logged."*  
— Forensic Investigator Wisdom

*"Log everything important, but remember: if you log everything, you've logged nothing useful."*  
— SOC Analyst's Paradox