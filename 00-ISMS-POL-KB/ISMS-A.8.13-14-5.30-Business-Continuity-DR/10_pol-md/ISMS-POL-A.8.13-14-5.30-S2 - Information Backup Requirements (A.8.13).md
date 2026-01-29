# ISMS-POL-A.8.13-14-5.30-S2: Information Backup Requirements (A.8.13)

**Document Classification:** Internal - ISMS Policy  
**Version:** 1.0  
**Effective Date:** [To be defined]  
**Review Cycle:** Annual  
**Policy Owner:** Chief Information Security Officer (CISO)  
**Approved By:** [Approval Authority]

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Operations Manager / CISO | Initial backup requirements policy for A.8.13 |

---

## Table of Contents

1. [Control Focus: A.8.13](#1-control-focus-a813)
2. [Backup Scope Requirements](#2-backup-scope-requirements)
3. [Backup Schedule Requirements](#3-backup-schedule-requirements)
4. [RPO Requirements by Criticality](#4-rpo-requirements-by-criticality)
5. [Backup Technology Requirements](#5-backup-technology-requirements)
6. [3-2-1-1-0 Backup Rule (Industry Best Practice)](#6-3-2-1-1-0-backup-rule-industry-best-practice)
7. [Offsite and Offline Backup Requirements](#7-offsite-and-offline-backup-requirements)
8. [Immutability Requirements (DORA/NIS2)](#8-immutability-requirements-doranis2)
9. [Backup Testing Requirements](#9-backup-testing-requirements)
10. [Backup Monitoring Requirements](#10-backup-monitoring-requirements)
11. [Recovery Procedures](#11-recovery-procedures)
12. [Compliance Measurement](#12-compliance-measurement)

---

## 1. Control Focus: A.8.13

### 1.1 ISO 27001:2022 Control Text

**A.8.13 - Information Backup**

> Backup copies of information, software and systems shall be maintained and regularly tested in accordance with the agreed topic-specific policy.

**Purpose:**
To ensure that information, software and systems can be recovered in the event of loss, damage, corruption or unavailability.

### 1.2 Control Objective

The objective of this control is to ensure that [Organization] maintains the capability to recover critical information, software, and systems from backup copies in the event of:
- Hardware failures (disk crashes, server failures)
- Human error (accidental deletion, incorrect configuration)
- Malicious activity (ransomware, sabotage, insider threats)
- Natural disasters (fire, flood, earthquake)
- Cyber incidents (data corruption, system compromise)

### 1.3 Key Principle: Backup vs. Archive

This policy addresses **backup** for recovery purposes, which is distinct from **archival** for long-term retention:

**Backup:**
- Purpose: Enable recovery from recent failure or incident
- Retention: Short to medium term (days to months)
- Access frequency: Accessed when recovery is needed (infrequent)
- Primary metric: Recovery Point Objective (RPO)

**Archive:**
- Purpose: Long-term retention for compliance, legal, historical purposes
- Retention: Long term (years to decades)
- Access frequency: Rarely accessed
- Primary metric: Retention period compliance

While backup and archive may use similar technologies, they serve different purposes. This policy focuses on backup for recovery.

---

## 2. Backup Scope Requirements

### 2.1 What Must Be Backed Up

[Organization] shall maintain backup copies of:

**2.1.1 Business-Critical Data**
- Customer data (CRM systems, databases)
- Financial data (accounting systems, transaction records)
- Intellectual property (product designs, source code, documentation)
- Operational data (inventory, supply chain, production systems)
- Employee data (HR systems, payroll)
- Regulatory and compliance records

**2.1.2 System Configurations**
- Server configurations (operating system settings, network configurations)
- Application configurations (application settings, integration configurations)
- Network device configurations (routers, switches, firewalls, load balancers)
- Security configurations (access controls, security policies, encryption keys)
- Infrastructure-as-Code (Terraform, CloudFormation, Ansible playbooks)

**2.1.3 Application Software**
- Application binaries and executables
- Application dependencies and libraries
- Database schema and stored procedures
- Custom scripts and automation tools

**2.1.4 System Images**
- Virtual machine images (for rapid recovery)
- Container images (for containerized applications)
- Bare-metal system images (for physical servers where applicable)

### 2.2 Criticality-Based Prioritization

Not all systems require the same level of backup protection. Backup requirements shall be aligned with system criticality as determined through Business Impact Analysis (BIA):

**Critical Systems** (Tier 1):
- Must have backup capabilities
- Shortest RPO requirements
- Most frequent testing
- Highest redundancy (see A.8.14)

**Important Systems** (Tier 2):
- Must have backup capabilities
- Moderate RPO requirements
- Regular testing
- Moderate redundancy

**Standard Systems** (Tier 3):
- Should have backup capabilities
- Longer RPO requirements
- Periodic testing
- Minimal or no redundancy

**Low-Criticality Systems** (Tier 4):
- May have backup capabilities or risk acceptance
- Longest RPO requirements or no backup
- Infrequent or no testing

System criticality classification shall be documented in the Asset Inventory (ISMS-POL-A.5.9) and reviewed annually or when significant changes occur.

### 2.3 Exclusions

The following may be excluded from backup scope with documented justification:

**Ephemeral Data:**
- Temporary files that are regenerated automatically
- Cache data that can be rebuilt
- Session data with no persistent value

**Non-Critical Development/Test Data:**
- Development environments that can be rebuilt from code
- Test data that can be regenerated
- Temporary sandbox environments

**Publicly Available Data:**
- Data that can be re-downloaded from public sources
- Open-source software available from repositories

**Acceptable Criteria for Exclusion:**
- Data can be regenerated or re-acquired within acceptable timeframes
- Loss of data has negligible business impact
- Exclusion is documented and risk-accepted by business owner

### 2.4 Documentation Requirements

[Organization] shall maintain:
- **Backup Inventory**: Complete list of all systems and data sets backed up
- **Backup Scope Document**: Detailed documentation of what is included/excluded and why
- **System Criticality Classification**: Mapping of systems to criticality tiers
- **Exclusion Register**: Documented exclusions with risk acceptance

These documents shall be reviewed and updated at least annually.

---

## 3. Backup Schedule Requirements

### 3.1 Backup Frequency Alignment with RPO

Backup frequency shall be determined by the Recovery Point Objective (RPO) for each system. At minimum:

**RPO ≤ 4 hours** (Critical Systems):
- Continuous replication or hourly backups recommended
- Daily full backups with hourly incremental backups minimum

**RPO ≤ 24 hours** (Important Systems):
- Daily backups minimum
- Consider incremental backups during business hours for active systems

**RPO ≤ 7 days** (Standard Systems):
- Weekly full backups minimum
- Daily incremental backups for actively changing systems

**RPO > 7 days** (Low-Criticality Systems):
- Backup frequency determined by business requirements
- Monthly backups acceptable for rarely changing systems

### 3.2 Backup Timing Considerations

**Backup Windows:**
- Backups should be scheduled during periods of lowest system activity where possible
- Backup windows should account for data size and network bandwidth
- Backup operations should not significantly impact application performance during business hours

**Business Hours vs. Off-Hours:**
- Critical 24/7 systems: Continuous or incremental backups during business hours
- Standard business hours systems: Nightly backups after business hours
- Batch processing windows: Coordinate backup timing with batch jobs

**Time Zone Considerations:**
- Organizations operating across multiple time zones should coordinate backup schedules
- Backup logs should use consistent timestamps (UTC recommended)

### 3.3 Backup Retention Requirements

Backup retention periods shall balance:
- Business recovery needs (how far back might we need to restore?)
- Storage costs (longer retention = more storage)
- Regulatory requirements (minimum retention periods)

**Minimum Retention Periods:**

**Critical Systems:**
- Daily backups: Retained for at least 30 days
- Weekly backups: Retained for at least 3 months
- Monthly backups: Retained for at least 1 year

**Important Systems:**
- Daily backups: Retained for at least 14 days
- Weekly backups: Retained for at least 2 months
- Monthly backups: Retained for at least 6 months

**Standard Systems:**
- Weekly backups: Retained for at least 1 month
- Monthly backups: Retained for at least 3 months

**Regulatory Considerations:**
- Systems subject to regulatory retention requirements (financial records, healthcare data, etc.) shall retain backups for the required period or longer
- Backup retention shall be documented in the Retention Schedule (per ISMS-POL-A.8.11)

### 3.4 Backup Strategy Types

**Full Backup:**
- Complete copy of all data
- Longest backup time, highest storage consumption
- Fastest restore time (single restore operation)
- Recommended frequency: Weekly or monthly for large datasets

**Incremental Backup:**
- Only data changed since last backup (full or incremental)
- Fastest backup time, lowest storage consumption
- Slower restore time (requires full + all incrementals)
- Recommended frequency: Daily or hourly for active systems

**Differential Backup:**
- Only data changed since last full backup
- Moderate backup time and storage consumption
- Moderate restore time (requires full + last differential)
- Alternative to incremental for simpler restore process

**Continuous Data Protection (CDP):**
- Near-continuous replication of changes
- Achieves very short RPO (minutes or seconds)
- Suitable for critical systems with RPO < 1 hour
- Higher complexity and cost

[Organization] shall select backup strategies appropriate to system criticality, data change rate, and RPO requirements.

---

## 4. RPO Requirements by Criticality

### 4.1 Recovery Point Objective Definition

**Recovery Point Objective (RPO)** is the maximum acceptable amount of data loss measured in time. It determines how far back in time we can restore data.

**Example:**
- If RPO = 4 hours and a failure occurs at 3:00 PM, we must be able to restore data from at least 11:00 AM
- If last backup was at 9:00 AM (6 hours ago), we do not meet RPO

### 4.2 RPO Requirements by System Criticality

These are **baseline requirements**. Individual systems may have more stringent RPO requirements based on Business Impact Analysis:

| Criticality Tier | Maximum RPO | Backup Frequency Minimum | Example Systems |
|------------------|-------------|-------------------------|-----------------|
| **Critical** (Tier 1) | ≤ 4 hours | Hourly incremental + Daily full | Payment processing, real-time trading, customer-facing applications |
| **Important** (Tier 2) | ≤ 24 hours | Daily backup | ERP, CRM, email, file servers |
| **Standard** (Tier 3) | ≤ 7 days | Weekly backup | Internal tools, reporting systems, development environments |
| **Low** (Tier 4) | > 7 days or Risk Accepted | Monthly or no backup | Archived data, non-critical test systems |

### 4.3 Business-Driven RPO Determination

**Critical Principle:** RPO requirements are **business-driven**, not IT-driven.

**Process for RPO Determination:**
1. Business Impact Analysis identifies financial, operational, and reputational impact of data loss
2. Business owner determines acceptable data loss based on impact assessment
3. RPO requirement is documented and approved by business owner
4. IT implements backup capabilities to meet approved RPO
5. Gap between business requirement and technical capability is identified, accepted, or remediated

**IT cannot unilaterally change RPO requirements.** If technical limitations prevent meeting business requirements:
- Gap is documented
- Risk assessment is conducted
- Business owner either accepts risk or approves investment to close gap

### 4.4 RPO Compliance Verification

Compliance with RPO requirements shall be verified through:
- Automated monitoring of backup frequency
- Regular comparison of backup frequency against RPO requirements
- Quarterly compliance reporting
- Annual review of RPO requirements (BIA update)

Assessment Workbook 1 (Backup Inventory & Coverage) includes RPO compliance calculations.

---

## 5. Backup Technology Requirements

### 5.1 Technology-Agnostic Approach

This policy does not mandate specific backup technologies or vendors. [Organization] maintains flexibility to select backup solutions appropriate to its infrastructure, budget, and requirements.

**Technology Independence:**
- Any backup solution meeting these requirements is acceptable
- On-premises, cloud, or hybrid backup solutions are all viable
- Commercial or open-source backup software is acceptable
- Multiple backup solutions may be used for different systems

### 5.2 Required Backup Solution Capabilities

Any backup solution deployed by [Organization] shall provide:

**Core Capabilities:**
- Scheduled automated backups (no manual intervention required for routine backups)
- Full, incremental, and/or differential backup support
- Centralized backup management (visibility across all backed-up systems)
- Backup job monitoring and alerting (success/failure notifications)
- Configurable retention policies (automatic deletion of old backups per policy)

**Data Integrity:**
- Backup verification (checksums, integrity validation)
- Detection of corrupt backups
- Alert on backup integrity failures

**Recovery Capabilities:**
- File-level restore (granular recovery without full system restore)
- System-level restore (complete system recovery)
- Point-in-time recovery (restore to specific backup date/time)
- Restore to alternate locations (for testing and DR scenarios)

**Security Capabilities:**
- Encryption in transit (data encrypted during backup transmission)
- Encryption at rest (backup data encrypted in storage)
- Access controls (only authorized personnel can restore backups)
- Audit logging (who accessed/restored what data, when)

**Reporting:**
- Backup success/failure reporting
- Storage utilization reporting
- RPO compliance reporting (comparing backup frequency to requirements)
- Recovery testing reporting

### 5.3 Backup Encryption Requirements

**Encryption in Transit:**
- All backup data transmitted over networks shall be encrypted using TLS 1.2 or higher
- Unencrypted backup transmission over public networks is prohibited
- On-premises backups over internal networks should use encryption where performance permits

**Encryption at Rest:**
- Backup data stored offsite or in cloud storage shall be encrypted at rest using AES-256 or equivalent
- Encryption at rest for on-premises backup storage is strongly recommended
- Encryption keys shall be managed per ISMS-POL-A.8.24 (Cryptographic Key Management)

**Regulatory Compliance:**
- Systems subject to DORA (financial services) require encryption at rest for all backups
- Systems subject to NIS2 require encryption at rest and in transit
- Healthcare systems (HIPAA) require encryption for any backups containing ePHI

### 5.4 Backup Integrity Verification

Backup integrity shall be verified through:

**Automated Verification:**
- Checksum validation during backup creation
- Periodic integrity scans of existing backups
- Automated alerts on corrupted backups

**Restore Testing:**
- Regular restore tests verify data integrity (corrupt backups will fail restore)
- Restore tests are the ultimate verification of backup integrity

**Backup Chain Validation:**
- For incremental/differential backup strategies, validate backup chains are complete
- Alert on broken backup chains (missing incrementals)

---

## 6. 3-2-1-1-0 Backup Rule (Industry Best Practice)

### 6.1 The 3-2-1-1-0 Rule Explained

The **3-2-1-1-0 rule** is an industry best practice (promoted by Veeam and other backup vendors) that provides comprehensive backup resilience:

- **3**: Three copies of data (1 production + 2 backups)
- **2**: Two different media types (e.g., disk + cloud, disk + tape)
- **1**: One copy offsite (geographic separation)
- **1**: One copy offline/air-gapped/immutable (ransomware protection)
- **0**: Zero recovery errors (verified recoverability through testing)

### 6.2 Application to [Organization]

While [Organization] does not mandate strict adherence to the 3-2-1-1-0 rule, the principles are strongly recommended and incorporated into requirements:

**Principle 1 - Three Copies:**
- Production data (primary copy)
- Primary backup (on-premises or primary cloud region)
- Secondary backup (offsite, different location)
- **Requirement:** Critical and Important systems should have at least 2 backup copies (primary + secondary)

**Principle 2 - Two Media Types:**
- Protects against single media type failures
- Examples: Disk + Cloud, Disk + Tape, Cloud Region A + Cloud Region B
- **Requirement:** Important and Critical systems should use at least 2 different storage types/locations

**Principle 3 - One Offsite:**
- Protects against site-wide disasters (fire, flood, physical destruction)
- **Requirement:** Critical systems must have offsite backups (see Section 7)

**Principle 4 - One Immutable/Offline:**
- Protects against ransomware and malicious deletion
- **Requirement:** Critical systems should have immutable or offline backups (see Section 8)

**Principle 5 - Zero Errors:**
- Backups are meaningless if they cannot be restored
- **Requirement:** All systems must have regular restore testing (see Section 9)

### 6.3 3-2-1-1-0 Compliance Tracking

Assessment Workbook 1 (Backup Inventory & Coverage) includes a dedicated sheet for tracking 3-2-1-1-0 compliance:
- Each system is scored against all 5 criteria
- Compliance percentage is calculated
- Gaps are identified for remediation

Organizations may use this tracking to measure progress toward best practice adoption.

---

## 7. Offsite and Offline Backup Requirements

### 7.1 Offsite Backup Requirements

**Offsite backup** is a copy of backup data stored in a geographically separate location from the primary data and primary backup.

**7.1.1 Critical Systems (Mandatory)**
All Critical systems shall have at least one offsite backup copy. Offsite location shall be:
- Geographically separated by sufficient distance to avoid single regional disaster (minimum 50km recommended, greater for areas prone to widespread disasters)
- Accessible for recovery operations within RTO requirements
- Protected with equivalent security controls as primary site

**7.1.2 Important Systems (Strongly Recommended)**
Important systems should have offsite backups where technically and economically feasible. Where not implemented, risk shall be documented and accepted by business owner.

**7.1.3 Standard and Low-Criticality Systems (Optional)**
Offsite backups for Standard and Low-Criticality systems are optional based on cost-benefit analysis.

**7.1.4 Implementation Approaches**

**Cloud-Based Offsite:**
- Backup to cloud storage (AWS S3, Azure Blob, Google Cloud Storage, etc.)
- Inherently offsite and geographically diverse
- Cost-effective for most scenarios
- Requires internet connectivity for backup and restore

**Secondary Datacenter:**
- Backup replication to secondary on-premises datacenter
- Higher control and potentially faster recovery
- Higher cost (infrastructure, maintenance)

**Tape Vaulting:**
- Physical tape media transported to secure offsite facility
- Traditional approach, declining in use
- May be required for regulatory compliance in some industries

**Hybrid Approach:**
- Combination of on-premises and cloud backups
- Balances speed (local restore) with resilience (cloud offsite)

### 7.2 Offline and Air-Gapped Backup Requirements

**Offline/air-gapped backup** is a backup copy that is physically or logically disconnected from production networks, making it immune to network-based attacks (ransomware, lateral movement).

**7.2.1 Critical Systems (Strongly Recommended)**
Critical systems should have at least one offline or air-gapped backup copy to protect against ransomware and insider threats.

**7.2.2 Implementation Approaches**

**Physical Air-Gap (Tape):**
- Backup to tape media that is physically disconnected after backup
- Media stored offline in secure location
- Manual restore process (tape must be physically retrieved and mounted)
- Highest protection against cyber threats
- Slowest restore time

**Logical Air-Gap (Immutable Storage):**
- Backup to storage that cannot be deleted or modified for a defined period
- Examples: AWS S3 Object Lock, Azure Blob Immutable Storage, WORM storage
- Ransomware cannot delete or encrypt immutable backups
- Faster restore than physical tape (online recovery)

**Scheduled Network Isolation:**
- Backup target connected to network only during backup windows
- Disconnected from network after backup completes
- Manual or automated isolation (network-controlled)

**7.2.3 Ransomware Protection Strategy**

The combination of offsite + offline/immutable backups provides comprehensive ransomware protection:

**Scenario: Ransomware Encrypts Production and Primary Backups**
- Production data encrypted: ✗ Lost (until ransom paid or restored)
- Primary backup encrypted: ✗ Lost (connected to network, accessible to ransomware)
- Offsite backup not encrypted: ✓ Available (but if connected to network, may also be compromised)
- Offline/immutable backup not encrypted: ✓ Guaranteed available (cannot be reached by ransomware)

**Result:** Recovery is possible from offline/immutable backup without paying ransom.

Without offline/immutable backups, ransomware can encrypt all connected backups, making recovery impossible without paying ransom.

---

## 8. Immutability Requirements (DORA/NIS2)

### 8.1 Regulatory Context

**DORA Article 12 Requirement (Financial Services):**
> "Backup data must be protected from unauthorized access and stored in such a way as to prevent any changes or corruption."

**NIS2 Directive Guidance (Essential/Important Entities):**
> "Immutable backups are required to protect against ransomware and malicious deletion."

Organizations subject to DORA or NIS2 **must** implement immutable backups for systems in scope of these regulations.

### 8.2 Immutability Definition

**Immutable backup** is a backup copy that cannot be modified, deleted, or encrypted for a defined retention period, even by administrators with high privileges.

**Key Characteristics:**
- Write-Once-Read-Many (WORM) behavior
- Protected against malicious deletion (ransomware, insider threats)
- Protected against accidental deletion (human error)
- Cannot be overwritten or modified during retention period
- Automatically released for deletion after retention period expires

### 8.3 Immutability Requirements by System Type

**DORA-Regulated Systems (Financial Services):**
- All critical systems: Immutable backups mandatory
- Retention period: Aligned with regulatory requirements (typically 30+ days)

**NIS2-Regulated Systems (Essential/Important Entities):**
- All essential services systems: Immutable backups mandatory
- Retention period: Sufficient for recovery from delayed-discovery incidents (typically 14-30 days)

**Other Critical Systems (General):**
- Immutable backups strongly recommended for all Critical systems
- Particularly important for systems at high risk of ransomware

**Important and Standard Systems:**
- Immutable backups recommended where cost-effective
- May use standard backups with robust access controls as alternative

### 8.4 Immutability Implementation Approaches

**Cloud Object Storage with Object Lock:**
- AWS S3 Object Lock (Compliance Mode)
- Azure Blob Immutable Storage (Legal Hold or Time-based Policy)
- Google Cloud Storage Retention Policy
- Most flexible and cost-effective approach for cloud-based backups

**WORM Storage:**
- Physical WORM tape media
- WORM-capable disk appliances
- Traditional approach, still used in some environments

**Backup Appliances with Immutability:**
- Purpose-built backup appliances with immutability features
- Examples: Some Dell EMC, HPE, or specialized backup vendors
- May use internal WORM storage or software-enforced immutability

**Software-Enforced Immutability:**
- Backup software with immutability enforcement
- Depends on software security (if software is compromised, immutability may be bypassed)
- Less secure than hardware-enforced immutability but more accessible

### 8.5 Immutability Retention Period

Immutability retention period should be:
- Long enough to detect and recover from delayed-discovery incidents (ransomware dwell time can be weeks/months)
- Short enough to avoid excessive storage costs
- Aligned with regulatory requirements where applicable

**Recommended Retention Periods:**
- **Critical Systems (DORA/NIS2):** 30 days minimum
- **Critical Systems (General):** 14-30 days recommended
- **Important Systems:** 7-14 days recommended

After immutability period expires, backups can be deleted per normal retention policy.

### 8.6 Verification of Immutability

[Organization] shall verify that immutable backups are actually immutable through:
- Periodic testing of immutability (attempt to delete immutable backups - should fail)
- Monitoring of immutability settings (ensure policies remain configured)
- Documentation of immutability implementation per system
- Audit review of immutability compliance

---

## 9. Backup Testing Requirements

### 9.1 The Testing Imperative

**Critical Principle:** Untested backups are not backups. A backup you have never restored is a backup you cannot trust.

**Common Failure Scenarios:**
- Backup appears successful but data is corrupt
- Backup software configuration error (backing up wrong data)
- Restore procedure doesn't work as documented
- Restore time exceeds RTO (too slow)
- Dependencies missing (application backups without database backups)

**Only testing reveals these issues.**

### 9.2 Test Frequency by System Criticality

Minimum restore test frequencies:

| Criticality Tier | Restore Test Frequency | Test Type |
|------------------|------------------------|-----------|
| **Critical** | Monthly | File-level restore minimum; System-level restore quarterly |
| **Important** | Quarterly | File-level or system-level restore |
| **Standard** | Annually | File-level restore |
| **Low** | As needed or never | Optional |

These are **minimum** frequencies. More frequent testing is encouraged.

### 9.3 Backup Test Types

**File-Level Restore Test:**
- Restore individual files or small sets of files
- Quickest and lowest risk test
- Verifies: Backup data integrity, restore process basics
- Does not verify: Full system recovery, application consistency

**System-Level Restore Test:**
- Restore entire system (virtual machine, database, application)
- Moderate risk (requires test environment)
- Verifies: Full system recovery, application functionality, RPO/RTO achievement
- Recommended frequency: Quarterly for Critical, Annually for Important

**Full Disaster Recovery Test:**
- Restore multiple interdependent systems simulating disaster scenario
- Highest complexity and risk
- Verifies: End-to-end recovery, dependencies, coordination, RTO achievement
- Recommended frequency: Annually as part of A.5.30 BC/DR testing

**Cross-Platform Restore Test:**
- Restore backup to different hardware or cloud platform
- Verifies: Portability, ability to restore to alternate location (DORA requirement)
- Recommended frequency: Annually for Critical systems

### 9.4 Test Documentation Requirements

Every backup restore test shall be documented with:
- Test date and duration
- System(s) tested
- Test type (file-level, system-level, full DR)
- Test scope (what was restored)
- Test result (Success, Failure, Partial Success)
- RPO achieved (how old was the restored data?)
- RTO achieved (how long did restore take?)
- Issues encountered (problems, errors, delays)
- Remediation actions (if issues found)
- Next test scheduled date

Test documentation shall be retained for audit purposes.

### 9.5 Testing Without Impacting Production

Restore tests should be conducted in a way that does not risk production systems:

**Isolated Test Environment:**
- Restore to separate test environment (dedicated hardware, separate network)
- Test system can be powered off or destroyed after test
- No risk to production

**Restore to Alternate Location:**
- Restore to cloud test environment (if production is on-premises)
- Restore to disaster recovery site
- Restore to secondary datacenter

**Snapshot-Based Testing:**
- Take snapshot of production
- Restore backup over snapshot in isolated environment
- Test and dispose

**Scheduled Testing Windows:**
- For systems where isolated testing is not possible, test during maintenance windows
- Have rollback plan ready

### 9.6 Test Result Actions

**Successful Test:**
- Document success and metrics (RPO/RTO achieved)
- Collect evidence for audit
- Schedule next test

**Failed Test:**
- Document failure details
- Identify root cause (corrupt backup, misconfiguration, procedure error, etc.)
- Create remediation plan
- Implement remediation
- **Retest after remediation to verify fix**
- Failed test = critical gap requiring immediate attention

**Partial Success:**
- Document what worked and what didn't
- Assess criticality of partial failure
- Remediate if necessary
- Consider retest depending on severity

---

## 10. Backup Monitoring Requirements

### 10.1 Real-Time Backup Monitoring

[Organization] shall implement automated monitoring of backup operations with real-time visibility:

**Backup Job Monitoring:**
- Success/failure status for every backup job
- Backup duration (detect jobs taking longer than expected)
- Data volume backed up (detect anomalies like sudden data growth or shrinkage)
- Backup storage utilization (prevent running out of backup storage space)

**Alert Thresholds:**
- **Immediate (Critical) Alerts:**
  - Backup job failure (any Critical system backup failure)
  - Backup storage capacity critical (>90% full)
  - Backup chain broken (missing incremental backups)
- **Same-Day (High) Alerts:**
  - Backup job failure (Important system)
  - Backup duration exceeded normal time by >50%
  - Backup integrity check failure
- **Daily Summary (Medium) Alerts:**
  - Backup job failure (Standard system)
  - Backup storage capacity warning (>80% full)

### 10.2 Dashboard Requirements

Backup dashboards shall provide:

**Operational Dashboard (IT Operations):**
- Real-time backup job status (in-progress, last completed)
- Last 24 hours: Successful, failed, in-progress backup jobs
- Backup storage utilization (per backup solution/location)
- Critical alerts and issues requiring attention

**Management Dashboard (Weekly/Monthly Reviews):**
- Backup coverage percentage (% of systems backed up per policy)
- RPO compliance percentage (% of systems meeting RPO requirements)
- Testing compliance (% of systems tested on schedule)
- Trend analysis (improving, stable, degrading)

### 10.3 Backup Reporting Requirements

**Daily Reports (Automated):**
- Backup job success/failure summary
- Failed backup details (which systems, error messages)
- Critical alerts requiring action

**Monthly Reports (Management):**
- Backup compliance summary (coverage, RPO, testing)
- Backup storage trends (capacity planning)
- Gaps and remediation status
- Testing summary (tests conducted, results)

**Quarterly Reports (Executive/CISO):**
- Overall BC/DR posture including backup readiness
- Compliance with policy requirements
- Critical gaps requiring investment or risk acceptance
- Audit readiness status

### 10.4 Integration with SIEM/Logging

Backup events shall be integrated with Security Information and Event Management (SIEM) systems per ISMS-POL-A.8.15 (Logging) and A.8.16 (Monitoring):

**Events to Log:**
- Backup job start/completion
- Backup job failures
- Backup restore operations (who restored what, when)
- Backup configuration changes
- Access to backup management interfaces
- Deletion of backups (including scheduled deletion per retention policy)

**Security Monitoring:**
- Alert on unexpected backup deletions (potential ransomware or insider threat)
- Alert on unusual restore operations (off-hours, by unusual accounts)
- Monitor backup storage access (detect unauthorized access attempts)

---

## 11. Recovery Procedures

### 11.1 Documented Recovery Procedures

[Organization] shall maintain documented recovery procedures for each system type. Recovery procedures shall include:

**Step-by-Step Instructions:**
- Prerequisites (access required, tools needed)
- Detailed restore steps (with screenshots where helpful)
- Estimated restore time
- Verification steps (how to confirm restore was successful)
- Rollback plan (if restore fails partway through)

**System-Specific Procedures:**
- Database restore (including transaction log replay if applicable)
- Application restore (including configuration restoration)
- Virtual machine restore
- Physical server restore (if applicable)
- Cloud resource restore

**Disaster Recovery Scenarios:**
- Single server failure recovery
- Multiple server failure recovery
- Complete site loss recovery
- Prolonged outage recovery

### 11.2 Recovery Playbooks

For critical systems, [Organization] shall maintain **recovery playbooks** (runbooks) that provide:
- Quick reference guide for emergency recovery
- Contact information (who to call, escalation paths)
- Decision trees (if X happens, do Y)
- Recovery priority sequence (what to restore first, second, etc.)
- Communication templates (stakeholder notifications)

Recovery playbooks shall be:
- Kept updated (reviewed quarterly)
- Accessible during disaster (offline copies available)
- Tested as part of BC/DR exercises

### 11.3 Escalation Paths

Recovery procedures shall define escalation paths for:

**Escalation Triggers:**
- Restore fails or takes longer than expected
- Required restore time exceeds RTO
- Data corruption detected after restore
- Missing dependencies prevent full recovery

**Escalation Contacts:**
- Level 1: Backup administrator
- Level 2: System owner / Senior engineer
- Level 3: IT manager / Architecture team
- Level 4: BC/DR coordinator / CISO

### 11.4 Recovery Verification

After any restore operation, the following verification shall be performed:

**Data Integrity Verification:**
- Application can access restored data
- Data is consistent and uncorrupted
- No data loss beyond expected RPO

**Application Functionality Verification:**
- Application starts successfully
- Core functionality operates correctly
- Integrations with other systems work
- Users can access application

**Performance Verification:**
- Restored system performs within acceptable parameters
- No degradation suggesting underlying issues

**Security Verification:**
- Access controls are correct (users have appropriate access)
- Security configurations are intact
- Restored system is patched and secure

Only after verification is complete should restored system be returned to production or declared recovery-complete.

---

## 12. Compliance Measurement

### 12.1 Key Backup Metrics

[Organization] shall measure and report the following backup compliance metrics:

**Backup Coverage:**
- **Metric:** Percentage of in-scope systems with backup capabilities
- **Calculation:** (Systems with backup) / (Total in-scope systems) × 100
- **Target:** ≥ 95% for Critical and Important systems combined

**RPO Compliance:**
- **Metric:** Percentage of systems meeting RPO requirements
- **Calculation:** (Systems where backup frequency ≤ RPO requirement) / (Total systems) × 100
- **Target:** ≥ 90% overall; 100% for Critical systems

**Backup Testing Compliance:**
- **Metric:** Percentage of systems tested on schedule
- **Calculation:** (Systems tested within required frequency) / (Total systems requiring testing) × 100
- **Target:** ≥ 80% overall; ≥ 95% for Critical systems

**Backup Success Rate:**
- **Metric:** Percentage of backup jobs completing successfully
- **Calculation:** (Successful backup jobs) / (Total backup jobs attempted) × 100
- **Target:** ≥ 98% for Critical systems; ≥ 95% overall

**3-2-1-1-0 Compliance (Optional):**
- **Metric:** Percentage of systems meeting all 5 criteria of 3-2-1-1-0 rule
- **Target:** ≥ 80% for Critical systems (aspirational)

### 12.2 Assessment Workbook Integration

Assessment Workbook 1 (Backup Inventory & Coverage) automatically calculates these metrics based on data entered. Organizations shall:
- Complete Assessment Workbook 1 at least quarterly
- Review metrics against targets
- Identify gaps and prioritize remediation
- Track trends (improving, stable, degrading)

### 12.3 Audit Evidence Requirements

For audit purposes (internal, ISO 27001, DORA, NIS2), [Organization] shall maintain:

**Backup Configuration Evidence:**
- Backup policy documentation (this document)
- Backup schedule configurations
- Backup retention configurations
- Backup scope documentation (what is backed up)

**Backup Operation Evidence:**
- Backup job logs (success/failure logs for sample period)
- Backup monitoring dashboards (screenshots or exports)
- Backup storage utilization reports

**Backup Testing Evidence:**
- Restore test results (documented per Section 9.4)
- Test schedules and completion records
- Evidence of remediation for failed tests

**Compliance Evidence:**
- RPO compliance reports (from Assessment Workbook)
- Testing compliance reports
- Quarterly/annual compliance summaries

**Regulatory-Specific Evidence (DORA/NIS2):**
- Immutability implementation documentation
- Offsite backup verification
- Restoration to different locations test results
- Encryption implementation verification

Evidence shall be retained for at least 3 years or as required by applicable regulations.

### 12.4 Continuous Improvement

Backup compliance is not a one-time achievement but a continuous process:

**Quarterly Reviews:**
- Review Assessment Workbook 1 metrics
- Identify new gaps or degrading trends
- Update remediation roadmap
- Adjust priorities based on business changes

**Annual Reviews:**
- Update BIA and RPO requirements
- Review backup technology adequacy
- Assess need for additional backup capabilities (offsite, immutable, etc.)
- Update backup procedures based on lessons learned

**Post-Incident Reviews:**
- After any production restore or disaster recovery event
- Review what worked and what didn't
- Update procedures based on lessons learned
- Test any changes to procedures

---

## Conclusion

This policy establishes comprehensive backup requirements for [Organization] in accordance with ISO 27001:2022 Control A.8.13, while also supporting DORA Article 12 and NIS2 Directive requirements for organizations in scope.

**Key Requirements Summary:**
✅ All business-critical systems shall have backup capabilities  
✅ Backup frequency shall align with business-defined RPO requirements  
✅ Critical systems shall have offsite backups  
✅ Critical systems should have immutable backups (mandatory for DORA/NIS2)  
✅ All backups shall be tested regularly (untested backup = no backup)  
✅ Backup operations shall be monitored with automated alerting  
✅ Recovery procedures shall be documented and maintained  
✅ Backup compliance shall be measured and reported  

**Next Steps:**
1. Review and approve this backup policy
2. Conduct or update Business Impact Analysis to determine RPO requirements (IMP-S1)
3. Assess current backup capabilities against these requirements (IMP-S5, Assessment Workbook 1)
4. Identify and remediate gaps
5. Implement regular restore testing cadence
6. Establish backup monitoring and reporting

---

**Document End**

*"A backup you have never tested is a backup you cannot trust."*

*This policy demands evidence, not assumptions.*

---

**APPROVAL SIGNATURES**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | | | |
| IT Operations Manager | | | |
| Backup Administrator | | | |
| Compliance Officer | | | |

**Next Review Date:** [One year from approval date]