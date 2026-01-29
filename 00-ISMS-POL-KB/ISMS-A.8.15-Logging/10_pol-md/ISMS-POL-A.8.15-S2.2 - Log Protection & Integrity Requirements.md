# ISMS-POL-A.8.15-S2.2
## Logging - Log Protection & Integrity Requirements

**Document ID**: ISMS-POL-A.8.15-S2.2  
**Title**: Logging - Log Protection & Integrity Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager / Security Architect | Initial log protection requirements |

**Review Cycle**: Annual (or upon security incidents involving log tampering)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Information Security Manager / Security Architect
- Operational Review: IT Operations Manager
- Audit Review: Internal Audit Lead

**Distribution**: Security team, IT operations, log administrators, system administrators, auditors  
**Related Documents**: ISMS-IMP-A.8.15.3 (Log Protection & Retention Assessment), ISMS-POL-A.5.16 (Identity Management)

---

## 2.2.1 Purpose and Scope

This section establishes **mandatory requirements** for protecting logs from unauthorized access, modification, and deletion. Log integrity is critical - compromised logs cannot be trusted for incident investigation, forensic analysis, or compliance evidence.

**Core Principle**: *"A log you can't trust is worse than no log at all."*

**In Scope**: Access controls, integrity protection mechanisms, tamper detection, secure transmission, separation of duties  
**Primary Stakeholders**: Security Team, Log Administrators, IT Operations, Compliance Officers  
**Implementation Evidence**: ISMS-IMP-A.8.15.3 (Log Protection & Retention Assessment)

**Key Threat Scenarios This Section Addresses**:
- Malicious insiders attempting to cover their tracks by deleting or modifying logs
- External attackers tampering with logs to hide evidence of compromise
- Accidental deletion or corruption of log data
- Unauthorized access to sensitive information contained in logs
- Log data exfiltration for reconnaissance purposes

---

## 2.2.2 Access Control Requirements

### 2.2.2.1 Read Access to Logs

**Principle of Least Privilege**: Access to logs SHALL be granted only to personnel with legitimate business need.

Organizations **SHALL** implement access controls restricting log read access to:

**Authorized Roles**:
- **Security Operations Center (SOC) Analysts**: Full read access to security logs for monitoring and investigation
- **Incident Responders**: Full read access during active incident investigations
- **System Administrators**: Read access to logs for systems they manage (principle: admin of server X can read server X logs)
- **Application Support Personnel**: Read access to application logs for troubleshooting
- **Auditors**: Read access to audit-relevant logs during audits
- **Compliance Officers**: Read access for compliance verification purposes
- **Forensic Investigators**: Full read access during authorized investigations

**Access Control Mechanisms** SHALL include:
- Authentication (unique user accounts, no shared credentials)
- Role-based access control (RBAC) based on job function
- Need-to-know restrictions (users see only logs relevant to their responsibilities)
- Time-bounded access for temporary assignments (e.g., contractors, temporary auditors)

### 2.2.2.2 Write/Modification Access to Logs

**Critical Requirement**: Once logs are written, they **SHALL NOT** be modifiable by any user, including administrators.

Organizations **SHALL**:
- Implement write-once storage mechanisms (see Section 2.2.4)
- Prohibit direct modification of log files on source systems
- Prohibit modification of logs in centralized log management system
- Implement technical controls preventing log modification (file system permissions, WORM storage, append-only databases)

**Exception**: Log rotation and archival processes may move or compress logs but SHALL NOT modify log content.

### 2.2.2.3 Delete Access to Logs

**Principle**: Logs SHALL NOT be deleted before retention period expires (see S2.3).

Organizations **SHALL**:
- Prohibit manual deletion of logs before retention period
- Implement automated deletion ONLY after retention period expires
- Require dual-authorization for emergency log deletion (e.g., legal hold, disk space emergency)
- Log all log deletion events (meta-logging)
- Implement technical controls preventing premature deletion (file system immutability, WORM storage)

**Authorized Deletion Scenarios**:
- Automated deletion after retention period expires (approved process)
- Legal hold removal (authorized by legal counsel)
- Emergency disk space recovery (approved by CISO with compensating controls)
- Data subject deletion request (GDPR "right to erasure" - see Section 2.2.2.6)

### 2.2.2.4 Administrative Access to Log Infrastructure

**Separation of Duties**: Log administrators SHALL be separate from system administrators where feasible.

Organizations **SHALL**:
- Designate specific individuals as Log Administrators with access to log management infrastructure
- Restrict log administrator role to log infrastructure management (not system administration)
- Require multi-person approval for sensitive log operations
- Monitor and audit all administrative actions on log infrastructure
- Implement break-glass procedures for emergency access (with full audit trail)

**Log Administrator Privileges** (SHALL be limited to):
- Configuration of log collection and forwarding
- Management of log retention policies (within policy limits)
- Creation of log search/analysis queries
- Management of log storage infrastructure
- Troubleshooting log collection issues

**Log Administrator Prohibited Actions**:
- Modifying existing log content
- Deleting logs before retention period
- Accessing systems being logged (separation of duties)
- Disabling logging on source systems without authorization

### 2.2.2.5 Logging of Log Access

**Meta-Logging Requirement**: All access to logs SHALL itself be logged.

Organizations **SHALL** log:
- Log read access (who viewed which logs, when, search queries executed)
- Log export operations (who exported logs, what data, when)
- Log deletion events (who deleted, what logs, justification)
- Log configuration changes (who changed what setting, when)
- Failed access attempts to log systems

**Rationale**: Meta-logging deters misuse of log access privileges and provides audit trail of log review activities.

### 2.2.2.6 Privacy Considerations for Log Access

Logs may contain personal data subject to data protection regulations (GDPR, FADP).

Organizations **SHALL**:
- **Document legitimate purposes** for log access (security monitoring, incident investigation, compliance)
- **Limit access** to personnel with legitimate need related to documented purposes
- **Train authorized personnel** on privacy obligations when accessing logs
- **Monitor log access** for inappropriate curiosity or privacy violations
- **Implement data subject access request procedures** (GDPR Article 15)
- **Implement deletion request procedures** where legally required (GDPR Article 17, with security exceptions)

**GDPR Exemption**: Organizations MAY refuse data deletion requests where logs are necessary for security purposes (GDPR Article 17(3)(f) - exercising rights or legal claims).

---

## 2.2.3 Secure Log Transmission

### 2.2.3.1 Encryption in Transit

Logs **SHALL** be transmitted securely from log sources to centralized log management systems.

Organizations **SHALL**:
- **Encrypt log data in transit** using:
  - TLS/SSL for syslog (RFC 5425 - TLS Transport Mapping for Syslog)
  - HTTPS for web-based log APIs
  - Encrypted VPN tunnels for log forwarding across untrusted networks
  - SSH/SFTP for log file transfers
- Use modern TLS versions (TLS 1.2 minimum, TLS 1.3 recommended)
- Implement certificate validation (prevent man-in-the-middle attacks)
- Document which log sources use encrypted vs. unencrypted transmission

**Exception**: Logs transmitted within secure, isolated network segments (e.g., dedicated management network) MAY use unencrypted transmission if documented and risk-accepted.

### 2.2.3.2 Authentication of Log Sources

Log management systems **SHOULD**:
- Authenticate log sources before accepting log data (prevent log injection attacks)
- Use mutual TLS authentication where supported
- Implement source IP restrictions (accept logs only from known IP ranges)
- Validate log source identity (hostname, certificate CN)

### 2.2.3.3 Log Forwarding Reliability

Log forwarding mechanisms **SHALL**:
- Implement store-and-forward capability (buffer logs locally if collector unavailable)
- Retry failed transmissions with exponential backoff
- Alert administrators when log forwarding fails or falls behind
- Prioritize security logs over operational logs when bandwidth constrained

---

## 2.2.4 Log Integrity Protection Mechanisms

### 2.2.4.1 Write-Once-Read-Many (WORM) Storage

Organizations **SHOULD** implement WORM storage for logs requiring highest integrity assurance.

**WORM Implementation Options**:
- Hardware-based WORM storage (tape, optical media, dedicated WORM appliances)
- Software-based WORM (file system immutability flags, append-only databases)
- Cloud-based WORM (AWS S3 Object Lock, Azure Immutable Blob Storage)

**WORM Storage Requirements**:
- Logs written to WORM storage SHALL NOT be modifiable or deletable until retention period expires
- WORM status SHALL be verified periodically (quarterly)
- WORM implementation SHALL be documented and tested

**Use WORM for**:
- Audit logs required for regulatory compliance
- Logs of privileged user activities
- Security event logs
- Financial transaction logs
- Any logs that may be used as legal evidence

### 2.2.4.2 Cryptographic Hashing

Organizations **SHOULD** implement cryptographic hashing to detect log tampering.

**Hash-Based Integrity Protection**:
- Generate cryptographic hash (SHA-256 or stronger) of log files/records
- Store hashes separately from logs (ideally on different system)
- Periodically verify log integrity by recomputing hashes and comparing to stored values
- Alert security team immediately if hash mismatch detected (indicates tampering)

**Implementation Approaches**:
- Hash individual log entries (fine-grained integrity verification)
- Hash log files periodically (e.g., upon rotation)
- Use hash chains/Merkle trees for tamper-evident log sequences

### 2.2.4.3 Digital Signatures

Organizations **MAY** implement digital signatures for highest-assurance log integrity.

**Digital Signature Requirements**:
- Sign log files or log entries using private key controlled by log infrastructure
- Store signatures separately from logs
- Use timestamping service to prove signature time (prevent backdating)
- Implement key management procedures per cryptography policy

**Digital signatures provide**:
- Non-repudiation (proves log was generated by specific system at specific time)
- Tamper detection (signature verification fails if log modified)
- Legal admissibility (stronger evidence than unsigned logs)

**Note**: Digital signatures are computationally expensive. Use selectively for audit logs and logs requiring legal admissibility.

### 2.2.4.4 Log File Sealing

Organizations **MAY** implement log file sealing to protect log integrity on source systems.

**Sealing Mechanisms**:
- Mark log files as append-only (file system attributes)
- Implement mandatory access control (MAC) preventing modification
- Use kernel-level protections (Linux audit system, Windows Protected Event Logging)
- Seal logs immediately upon generation or rotation

**Sealing prevents**:
- Root/administrator from modifying logs on source system
- Malware from tampering with local logs
- Accidental deletion or corruption

---

## 2.2.5 Tamper Detection and Response

### 2.2.5.1 Tamper Detection Mechanisms

Organizations **SHALL** implement mechanisms to detect log tampering:

**Detection Methods**:
- **Hash verification**: Periodic comparison of stored hashes to recomputed hashes
- **Signature verification**: Validate digital signatures on signed logs
- **Sequence number gaps**: Detect missing log entries in sequential logs
- **Timestamp anomalies**: Detect logs with out-of-order or impossible timestamps
- **File size monitoring**: Detect unexpected log file shrinkage (deletion indicator)
- **File integrity monitoring (FIM)**: Monitor log files for unauthorized changes

Organizations **SHALL**:
- Implement automated tamper detection (not manual checks)
- Run tamper detection checks at least daily for critical logs
- Alert security team immediately upon tamper detection

### 2.2.5.2 Response to Detected Tampering

Upon detection of log tampering, organizations **SHALL**:

1. **Immediate Actions**:
   - Alert CISO and security team
   - Preserve evidence (copy tampered logs, capture forensic images)
   - Isolate potentially compromised systems
   - Initiate incident response procedures

2. **Investigation**:
   - Determine what logs were tampered with
   - Identify when tampering occurred
   - Determine who had access during tampering timeframe
   - Assess scope of compromise (what evidence is lost)
   - Identify root cause (technical vulnerability, insider threat, process failure)

3. **Remediation**:
   - Restore logs from backup if possible
   - Implement compensating controls for lost evidence
   - Fix vulnerability that allowed tampering
   - Review and strengthen log protection controls
   - Update incident response procedures based on lessons learned

4. **Reporting**:
   - Document incident per incident management policy
   - Report to management and relevant authorities (if required by regulation)
   - Notify affected parties (if personal data compromised)

---

## 2.2.6 Separation of Duties

### 2.2.6.1 Role Separation Principles

Organizations **SHALL** implement separation of duties to prevent conflicts of interest and reduce insider threat risk.

**Critical Separations**:

1. **System Administrators ≠ Log Administrators**
   - System administrators should not have ability to modify or delete logs of systems they administer
   - Prevents administrators from covering tracks of malicious actions
   - Where complete separation is not feasible (small organizations), implement compensating controls (frequent log review by independent party, WORM storage)

2. **Log Administrators ≠ Log Reviewers**
   - Personnel configuring logging should not be sole reviewers of logs
   - Prevents log administrators from hiding configuration mistakes or malicious activity
   - Independent review provides oversight

3. **Development ≠ Production Log Access**
   - Developers should not have access to production logs containing real user data
   - Use sanitized/anonymized logs for development troubleshooting
   - Prevents unauthorized access to sensitive production data

### 2.2.6.2 Implementation in Small Organizations

For organizations too small to fully separate duties:

Organizations **SHALL** implement compensating controls:
- **Enhanced monitoring**: More frequent independent review of logs
- **Dual authorization**: Require two people to authorize sensitive log operations
- **WORM storage**: Prevent single individual from tampering with logs
- **External audit**: More frequent third-party audits of log integrity
- **Management oversight**: Regular review by management of log activities

### 2.2.6.3 Break-Glass Procedures

Organizations **SHALL** document break-glass procedures for emergency access:
- Define emergency scenarios requiring exception to separation of duties
- Require approval from CISO or designated backup
- Implement enhanced logging during break-glass access
- Require post-event review and justification
- Review break-glass usage quarterly

---

## 2.2.7 Log Backup and Recovery

### 2.2.7.1 Log Backup Requirements

Organizations **SHALL** backup logs to protect against:
- Hardware failures (disk crashes, storage system failures)
- Accidental deletion
- Ransomware attacks encrypting log storage
- Natural disasters affecting primary log storage

**Backup Requirements**:
- Backup logs regularly (daily for critical logs, weekly for others)
- Store backups separately from primary log storage (different system, ideally different location)
- Encrypt backups (protect confidentiality)
- Test backup restoration quarterly (verify recoverability)
- Retain backups according to retention policy (see S2.3)

### 2.2.7.2 Backup Security

Log backups **SHALL** be protected with:
- Access controls (same rigor as primary logs)
- Encryption (AES-256 or equivalent)
- Integrity protection (hashes or signatures)
- Secure storage location (physically separate from primary logs)
- Regular testing (verify integrity and recoverability)

### 2.2.7.3 Recovery Procedures

Organizations **SHALL** document and test log recovery procedures:
- Identify recovery time objective (RTO) - how quickly logs must be restored
- Identify recovery point objective (RPO) - maximum acceptable data loss
- Document step-by-step recovery procedures
- Test recovery procedures annually
- Train personnel on recovery procedures

---

## 2.2.8 Protection from Malicious Insiders

### 2.2.8.1 Insider Threat Scenarios

Log protection controls SHALL defend against:
- **Administrator covering tracks**: Admin deletes logs of malicious actions
- **Privilege abuse**: User with log access exfiltrates sensitive data from logs
- **Log manipulation**: Insider modifies logs to frame another person or hide evidence
- **Log disabling**: Insider disables logging before performing malicious actions

### 2.2.8.2 Defense-in-Depth Controls

Organizations **SHALL** implement layered controls:

**Technical Controls**:
- Write-once storage (prevents deletion/modification)
- Real-time log forwarding (immediately sends logs off-system before tampering possible)
- Cryptographic integrity protection (tamper detection)
- Separation of duties (no single person can commit and hide action)

**Procedural Controls**:
- Dual authorization for sensitive operations
- Regular independent log review
- Anomaly detection alerting on unusual patterns
- Background checks for personnel with log access
- Mandatory vacation policy for log administrators (detect irregularities during absence)

**Detective Controls**:
- Audit log access (meta-logging)
- Alert on log tampering attempts
- Regular integrity checks
- Behavioral analysis of log access patterns

### 2.2.8.3 Privileged User Monitoring

For users with elevated privileges (administrators, log administrators):

Organizations **SHALL**:
- Implement enhanced logging of all privileged actions
- Require justification for privileged access to logs
- Alert on anomalous privileged user behavior
- Conduct periodic access reviews (quarterly)
- Implement session recording for privileged log access (if feasible)

---

## 2.2.9 Cloud and Third-Party Log Services

### 2.2.9.1 Cloud Log Storage Protection

For logs stored in cloud services (AWS, Azure, GCP):

Organizations **SHALL**:
- **Enable cloud-native protection mechanisms**:
  - AWS: S3 Object Lock, CloudTrail Integrity Validation, MFA Delete
  - Azure: Immutable Blob Storage, Azure Policy restrictions
  - GCP: Bucket Lock, Retention Policies, IAM restrictions
- Implement least-privilege IAM policies (restrict who can delete/modify logs)
- Enable multi-region replication (protect against regional failures)
- Enable versioning (recover from accidental deletion)
- Monitor cloud audit logs (CloudTrail, Azure Activity Log, GCP Audit Logs)

### 2.2.9.2 Third-Party SIEM/Log Management Services

When using third-party log management services (Splunk Cloud, Datadog, etc.):

Organizations **SHALL**:
- Review service provider's security controls (SOC 2 report, ISO 27001 certification)
- Implement strong authentication (SSO with MFA)
- Configure role-based access controls within service
- Enable all available integrity protection features
- Retain contractual right to audit provider
- Maintain local backup of critical logs (don't rely solely on provider)
- Review provider's data retention and deletion policies

---

## 2.2.10 Log Protection Metrics

Organizations **SHALL** measure log protection effectiveness through:

- **Access control compliance**: Percentage of users with appropriate log access (target: 100%)
- **Integrity check success rate**: Percentage of integrity checks passing (target: 100%)
- **Tamper detection incidents**: Number of tampering attempts detected (investigate all)
- **Backup success rate**: Percentage of log backups successful (target: >99%)
- **Recovery test success**: Percentage of recovery tests successful (target: 100%)
- **Separation of duties violations**: Number of instances where duties not separated (target: 0)
- **Failed log access attempts**: Number of unauthorized access attempts (investigate spikes)

Metrics SHALL be reviewed **monthly** by Security Team and reported to CISO **quarterly**.

---

## 2.2.11 Exceptions to Log Protection Requirements

### 2.2.11.1 When Exceptions May Be Granted

Exceptions to log protection requirements **MAY** be approved for:
- Systems with technical limitations preventing full protection implementation
- Non-critical systems where logs have minimal security/compliance value
- Legacy systems nearing decommission (with decommission plan)
- Test/development environments (not processing real data)

### 2.2.11.2 Exception Process

Organizations requesting log protection exceptions **SHALL**:
- Document technical or business justification
- Identify compensating controls
- Assess risk of reduced protection
- Obtain risk acceptance from system owner and CISO
- Review exceptions annually
- Plan remediation path

### 2.2.11.3 Non-Negotiable Requirements

The following protection requirements **SHALL NOT** be waived:

- Logs required for regulatory compliance (PCI DSS, HIPAA, SOX, etc.)
- Logs of privileged user activities
- Security event logs
- Logs of financial transactions
- Any logs that may be used as legal evidence

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-POL-A.8.15-S2.2 |
| **ISO 27001:2022 Control** | Annex A Control 8.15 (Logging) |
| **ISO 27002:2022 Section** | 8.15 (Event logging) |
| **Document Type** | Policy Section - Detailed Requirements |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Page Count** | [Auto-generated] |
| **Word Count** | ~3,400 words |
| **Line Count** | ~400 lines |
| **Parent Policy** | ISMS-POL-A.8.15 (Master) |
| **Related Sections** | S1, S2, S2.1, S2.3, S2.4 |
| **Implementation Evidence** | ISMS-IMP-A.8.15.3 |

---

**END OF SECTION S2.2**

---

*"Trust, but verify. Better yet, log everything and make it tamper-proof."*  
— Adapted from Ronald Reagan (by security engineers)

*"The first principle is that you must not fool yourself—and you are the easiest person to fool. That's why we make logs immutable."*  
— Richard P. Feynman (adapted for InfoSec)

*"A log you can modify is just creative fiction waiting to be written."*  
— Forensic Investigator Wisdom