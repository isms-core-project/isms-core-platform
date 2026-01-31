# ISMS-POL-A.8.15-S2.3
## Logging - Log Retention & Storage Requirements

**Document ID**: ISMS-POL-A.8.15-S2.3  
**Title**: Logging - Log Retention & Storage Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager / Legal Counsel | Initial retention and storage requirements |

**Review Cycle**: Annual (or upon regulatory changes affecting retention requirements)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Legal Review: Legal Counsel / Compliance Officer
- Technical Review: IT Operations Manager / Storage Architect
- Records Management: Records Management Officer (if applicable)

**Distribution**: Security team, IT operations, legal/compliance, records management, auditors  
**Related Documents**: ISMS-IMP-A.8.15.3 (Log Protection & Retention Assessment), Data Retention Policy, Records Management Policy

---

## 2.3.1 Purpose and Scope

This section establishes requirements for **HOW LONG** logs must be retained and **WHERE/HOW** they should be stored to meet regulatory requirements, support investigations, and manage storage costs effectively.

**Core Principle**: *"Storage is cheap, but compliance violations aren't."* However, indefinite retention is neither practical nor legally advisable (privacy regulations limit retention).

**In Scope**: Retention periods, storage tiers, archival procedures, disposal requirements, legal hold  
**Primary Stakeholders**: Legal/Compliance, IT Operations, Storage Administrators, Records Management  
**Implementation Evidence**: ISMS-IMP-A.8.15.3 (Log Protection & Retention Assessment)

**Key Considerations**:
- Regulatory compliance (minimum retention requirements)
- Forensic investigation needs (adequate forensic window)
- Storage cost optimization (tiered storage strategy)
- Privacy requirements (maximum retention limits)
- Legal hold obligations (suspension of disposal)

---

## 2.3.2 Log Retention Periods

### 2.3.2.1 Retention Period Framework

Organizations **SHALL** define retention periods based on:

1. **Regulatory Requirements**: Mandatory minimum retention (compliance floor)
2. **Business Requirements**: Operational and investigative needs
3. **Privacy Requirements**: Maximum retention limits (privacy ceiling)
4. **Legal Hold**: Indefinite retention when litigation anticipated

**Retention Period Determination Process**:
1. Identify applicable regulatory requirements (see Section 2.3.2.2)
2. Assess business needs for log analysis and forensics
3. Apply privacy requirements limiting maximum retention
4. Document retention decision with justification
5. Implement automated retention enforcement

### 2.3.2.2 Regulatory Retention Requirements

Organizations **SHALL** comply with applicable regulatory retention requirements:

**ISO/IEC 27001:2022 / ISO/IEC 27002:2022**:
- No specific retention period mandated
- Logs shall be retained "appropriately" based on risk assessment
- Recommendation: Minimum 12 months for security logs

**Swiss Federal Data Protection Act (FADP)**:
- No specific retention period mandated
- Logs containing personal data shall not be retained longer than necessary for purpose
- Recommendation: 6-12 months with documented justification

**EU General Data Protection Regulation (GDPR)**:
- No specific retention period mandated (Article 5.1.e - storage limitation principle)
- Logs must be retained only as long as necessary for purpose
- Security purposes justify retention (Recital 49 - security monitoring)
- Recommendation: 6-24 months with documented necessity

**Digital Operational Resilience Act (DORA) - Article 17**:
- Financial entities shall maintain comprehensive logs for incident management
- Recommendation: Minimum 12 months online, 5 years archived

**NIS2 Directive - Article 21**:
- Entities shall maintain logs for incident detection and reporting
- Recommendation: Minimum 12 months, aligned with incident reporting windows

**PCI DSS 4.0 - Requirement 10.7**:
- Audit logs shall be retained for at least 12 months
- At least 3 months shall be immediately available online
- Mandatory: 12 months minimum (no flexibility)

**HIPAA Security Rule - 45 CFR § 164.316(b)(2)(i)**:
- Audit logs shall be retained for 6 years
- Mandatory for U.S. healthcare entities

**Sarbanes-Oxley Act (SOX) - Section 802**:
- Audit records for financial systems shall be retained for 7 years
- Applies to publicly traded companies

### 2.3.2.3 Standard Retention Periods by Log Type

Organizations **SHALL** implement the following minimum retention periods (unless stricter regulatory requirements apply):

**Security Event Logs** (12 months online + 7 years archive):
- Malware detection events
- Intrusion detection/prevention alerts
- Data loss prevention events
- Security tool alerts (firewall blocks, web filter blocks, etc.)
- **Rationale**: Long forensic window, potential legal evidence, regulatory compliance

**Authentication & Authorization Logs** (12 months online + 7 years archive):
- User login/logout events (successful and failed)
- Password changes and resets
- Privilege escalation events
- Access grants and denials
- **Rationale**: Accountability, compliance, forensic investigations

**Administrative & Privileged Access Logs** (12 months online + 3 years archive):
- Configuration changes
- User account management
- System administration activities
- Privileged command execution
- **Rationale**: Accountability for administrative actions, change tracking

**Application Logs** (6 months online + 1 year archive):
- Application errors and exceptions
- Transaction logs (non-financial)
- API access logs
- Application performance logs
- **Rationale**: Troubleshooting, performance analysis

**System Logs** (6 months online + 1 year archive):
- Operating system events
- Service start/stop events
- System errors and failures
- Resource utilization logs
- **Rationale**: Troubleshooting, capacity planning

**Network Device Logs** (6 months online + 1 year archive):
- Firewall connection logs
- Router/switch logs
- VPN session logs
- DNS/DHCP logs
- **Rationale**: Network troubleshooting, incident investigation

**Database Logs** (12 months online + 7 years archive):
- Database access logs
- Schema change logs
- Backup/restore operations
- **Rationale**: Data integrity, compliance, forensics

**Audit Logs (Financial/Compliance)** (12 months online + 7-10 years archive):
- Financial transaction logs
- Compliance-relevant audit trails
- SOX-relevant logs
- **Rationale**: Regulatory compliance, legal requirements

### 2.3.2.4 Maximum Retention Limits (Privacy)

Organizations **SHALL** not retain logs indefinitely:

- **General Rule**: Delete logs after retention period expires (automated process)
- **Privacy Principle**: Retain only as long as necessary for legitimate purpose
- **Maximum Retention Guidance**:
  - Security logs: 7-10 years maximum (unless specific legal requirement)
  - Operational logs: 1-3 years maximum
  - Personal data in logs: Minimize retention, document necessity

**Exception**: Legal hold supersedes maximum retention (see Section 2.3.6)

---

## 2.3.3 Storage Tier Architecture

### 2.3.3.1 Three-Tier Storage Model

Organizations **SHOULD** implement tiered storage to balance performance and cost:

**Tier 1: Hot Storage** (Immediate Access):
- **Purpose**: Real-time analysis, active investigations, recent incident review
- **Characteristics**: High-performance storage (SSD, high-speed disk), fully indexed, sub-second query response
- **Retention**: Recent logs (30-90 days typical, 12 months for critical logs)
- **Technology**: SIEM online storage, Elasticsearch, high-performance databases
- **Cost**: High ($$$$)

**Tier 2: Warm Storage** (Archive - Fast Retrieval):
- **Purpose**: Historical analysis, compliance audits, older investigations
- **Characteristics**: Medium-performance storage (standard disk, object storage), indexed or compressed, query response in minutes
- **Retention**: Older logs beyond hot storage period (1-3 years)
- **Technology**: SIEM archive storage, data lakes, compressed file systems, object storage (S3 Standard, Azure Blob Hot)
- **Cost**: Medium ($$)

**Tier 3: Cold Storage** (Long-Term Archive):
- **Purpose**: Regulatory compliance, long-term retention, legal hold
- **Characteristics**: Low-cost storage (tape, glacier-class object storage), not indexed, retrieval in hours/days
- **Retention**: Logs at end of retention period (3-10 years)
- **Technology**: Tape libraries, AWS S3 Glacier, Azure Archive Blob, long-term backup solutions
- **Cost**: Low ($)

### 2.3.3.2 Storage Tier Transition

Organizations **SHALL** implement automated tiering processes:

- **Hot → Warm**: After 30-90 days (configurable by log type)
- **Warm → Cold**: After 12-24 months (configurable by log type)
- **Cold → Deletion**: After retention period expires (automated, audited)

**Transition Requirements**:
- Maintain log integrity during transitions (verify checksums)
- Preserve log format or document format changes
- Test retrieval from each tier quarterly
- Document transition schedules and procedures

### 2.3.3.3 Storage Capacity Planning

Organizations **SHALL**:

- **Estimate daily log volume** (MB/day or GB/day per source)
- **Calculate storage requirements** for each tier based on retention periods
- **Plan for growth** (20% annual growth typical, adjust based on business)
- **Implement capacity monitoring** (alert at 70% and 85% capacity)
- **Review capacity quarterly** and adjust forecasts
- **Budget for storage costs** (include all tiers in TCO calculations)

**Example Calculation**:
- Daily log volume: 100 GB/day
- Hot storage (90 days): 100 GB × 90 = 9 TB
- Warm storage (2 years): 100 GB × 730 = 73 TB
- Cold storage (5 years): 100 GB × 1,825 = 182.5 TB
- Total: ~265 TB raw (plan for 350 TB with growth and overhead)

---

## 2.3.4 Log Archival Procedures

### 2.3.4.1 Archival Process

Organizations **SHALL** implement automated log archival:

**Archival Steps**:
1. **Selection**: Identify logs reaching end of hot/warm storage period
2. **Validation**: Verify log integrity (checksums, completeness)
3. **Compression**: Compress logs to reduce storage costs (gzip, bzip2, vendor-specific)
4. **Encryption**: Encrypt archived logs (AES-256 or equivalent)
5. **Transfer**: Move logs to archive storage tier
6. **Verification**: Confirm successful transfer and integrity
7. **Deletion**: Remove logs from source tier (only after verification)
8. **Cataloging**: Update archive inventory (what logs, where, retention expiration date)

### 2.3.4.2 Archive Format Standards

Archived logs **SHALL**:

- Use open, standard formats (avoid proprietary formats that may become unreadable)
- Include metadata (source system, date range, format version, compression method)
- Be self-describing (include schema or format documentation within archive)
- Support long-term readability (test retrieval periodically)

**Recommended Archive Formats**:
- Compressed text files (gzip .gz, bzip2 .bz2)
- Standard structured formats (JSON, CSV, XML)
- Documented vendor formats with published specifications

### 2.3.4.3 Archive Integrity

Organizations **SHALL** protect archive integrity:

- Generate checksums (SHA-256) for each archive
- Store checksums separately from archives
- Verify archive integrity annually
- Alert on integrity failures
- Maintain multiple archive copies where possible (3-2-1 backup rule)

---

## 2.3.5 Log Disposal Procedures

### 2.3.5.1 Disposal Triggers

Logs **SHALL** be disposed of when:

- Retention period has expired (automated process)
- Regulatory requirement for retention has lapsed
- Legal hold has been lifted (after litigation concluded)
- Data subject deletion request (GDPR "right to erasure" - with security exceptions)

Logs **SHALL NOT** be disposed of:
- Before retention period expires
- During active legal hold
- During ongoing investigation requiring those logs
- Without proper authorization and audit trail

### 2.3.5.2 Secure Disposal Methods

Organizations **SHALL** securely delete logs using:

**Electronic Storage**:
- Cryptographic erasure (delete encryption keys for encrypted storage)
- Multi-pass overwrite (DoD 5220.22-M or equivalent)
- Secure deletion tools (shred, srm, vendor-specific secure delete)
- Physical destruction of storage media (for decommissioned systems)

**Physical Media** (tape, optical):
- Physical destruction (shredding, incineration, degaussing)
- Certificate of destruction from certified vendor
- Chain of custody documentation

### 2.3.5.3 Disposal Audit Trail

Organizations **SHALL** log all log disposal events:

- What logs were disposed of (date range, log types, sources)
- When disposal occurred (date and time)
- Who authorized disposal (automated process or manual authorization)
- Disposal method used
- Verification of disposal completion

**Disposal logs** shall be retained for 7 years (meta-logging).

---

## 2.3.6 Legal Hold Procedures

### 2.3.6.1 Legal Hold Definition

**Legal Hold** (litigation hold, preservation order): Requirement to preserve electronically stored information (ESI) including logs when litigation, investigation, or regulatory action is reasonably anticipated.

Organizations **SHALL** suspend normal disposal procedures for logs subject to legal hold.

### 2.3.6.2 Legal Hold Triggers

Legal hold **SHALL** be implemented when:

- Litigation is filed or reasonably anticipated
- Regulatory investigation is initiated or anticipated
- Internal investigation requires preservation of evidence
- Criminal investigation involves organizational systems
- Data breach requiring preservation of evidence
- Legal counsel advises hold

### 2.3.6.3 Legal Hold Process

Organizations **SHALL** implement legal hold procedures:

**Initiation**:
1. Legal counsel identifies need for legal hold
2. IT/Security receives formal legal hold notice
3. Identify scope of hold (which systems, date ranges, log types)
4. Flag affected logs in archive systems (prevent deletion)
5. Notify relevant personnel (IT, records management, system owners)
6. Document legal hold order and scope

**Maintenance**:
- Review legal hold quarterly (is hold still required?)
- Ensure held logs remain accessible
- Prevent disposal or modification of held logs
- Track costs of extended retention

**Release**:
1. Legal counsel authorizes release of hold
2. Formal release notice issued to IT/Security
3. Remove hold flags from affected logs
4. Resume normal retention schedule (dispose if retention expired)
5. Document hold release

### 2.3.6.4 Legal Hold Management

Organizations **SHALL**:

- Designate Legal Hold Coordinator (typically Legal Counsel or Compliance Officer)
- Maintain legal hold register (all active holds, scope, dates)
- Train IT/Security personnel on legal hold procedures
- Implement technical controls preventing disposal of held logs
- Review legal hold procedures annually

---

## 2.3.7 Storage Security Requirements

### 2.3.7.1 Encryption

Log storage **SHALL** be encrypted:

**Encryption at Rest**:
- All log storage tiers (hot, warm, cold) SHALL be encrypted
- Use AES-256 or equivalent encryption
- Implement key management per cryptography policy
- Protect encryption keys separately from encrypted logs

**Encryption in Transit**: (See S2.2 - Secure Transmission)

### 2.3.7.2 Access Controls

Log storage **SHALL** be protected with access controls:

- Implement principle of least privilege
- Separate storage administrators from log reviewers
- Audit all access to log storage
- Restrict direct file system access to logs

### 2.3.7.3 Physical Security

Physical storage media **SHALL** be protected:

- Store in secured data centers or facilities
- Implement environmental controls (temperature, humidity)
- Control physical access (badges, cameras, logs)
- Protect backup tapes in secure offsite storage

---

## 2.3.8 Cloud Storage Considerations

### 2.3.8.1 Cloud Storage Services

Organizations using cloud storage for logs **SHALL**:

- Select providers with appropriate certifications (SOC 2, ISO 27001)
- Implement data residency controls (ensure compliance with regulations)
- Use cloud-native encryption (AWS S3 SSE, Azure Storage Service Encryption)
- Configure lifecycle policies for automated tiering
- Implement object locking for WORM requirements
- Enable versioning to protect against accidental deletion
- Review cloud provider's retention and deletion capabilities

### 2.3.8.2 Multi-Region Replication

Organizations **SHOULD** consider multi-region replication:

- Protect against regional failures or disasters
- Improve retrieval performance for distributed teams
- Ensure compliance with data residency requirements (replicate only where legally permitted)

---

## 2.3.9 Retrieval and Restoration

### 2.3.9.1 Retrieval Requirements

Organizations **SHALL** define and test retrieval procedures:

**Retrieval SLAs**:
- Hot storage: Real-time access (<1 minute)
- Warm storage: Fast retrieval (<15 minutes)
- Cold storage: Delayed retrieval (hours to days, based on technology)

**Retrieval Testing**:
- Test retrieval quarterly from each storage tier
- Verify log integrity after retrieval
- Measure retrieval time against SLAs
- Document retrieval procedures

### 2.3.9.2 Chain of Custody

For logs retrieved as potential evidence:

Organizations **SHALL**:
- Document who retrieved logs, when, and why
- Generate cryptographic hashes of retrieved logs
- Maintain chain of custody documentation
- Store retrieved logs separately (prevent contamination)
- Restrict access to retrieved evidence

---

## 2.3.10 Retention Metrics

Organizations **SHALL** track retention compliance:

- **Retention compliance rate**: Percentage of log types meeting retention requirements (target: 100%)
- **Storage capacity utilization**: Percentage of allocated storage used (alert at 70%, 85%)
- **Archival success rate**: Percentage of archival operations successful (target: >99%)
- **Disposal success rate**: Percentage of logs disposed on schedule (target: 100%)
- **Retrieval test success**: Percentage of quarterly retrieval tests successful (target: 100%)
- **Legal hold count**: Number of active legal holds (track for cost management)

Metrics **SHALL** be reviewed monthly by IT Operations and reported to CISO quarterly.

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-POL-A.8.15-S2.3 |
| **ISO 27001:2022 Control** | Annex A Control 8.15 (Logging) |
| **ISO 27002:2022 Section** | 8.15 (Event logging) |
| **Document Type** | Policy Section - Detailed Requirements |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Page Count** | [Auto-generated] |
| **Word Count** | ~3,000 words |
| **Line Count** | ~380 lines |
| **Parent Policy** | ISMS-POL-A.8.15 (Master) |
| **Related Sections** | S1, S2, S2.1, S2.2, S2.4 |
| **Implementation Evidence** | ISMS-IMP-A.8.15.3 |

---

**END OF SECTION S2.3**