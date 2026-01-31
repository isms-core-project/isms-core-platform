# ISMS-IMP-A.8.15.3 - Log Protection & Retention Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.15 - Logging

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.15.3  
**Assessment Area:** Log Protection, Integrity, and Retention Compliance  
**Related Policy:** ISMS-POL-A.8.15-S2.2 (Protection), S2.3 (Retention)  
**Purpose:** Assess log protection mechanisms and retention compliance  
**Python Generator:** `generate_a815_3_log_protection_retention.py`  
**Target Audience:** Log Administrators, Compliance Team, Legal, IT Security

---

## Workbook Structure Overview

**Total Sheets:** 13  
**Estimated Rows:** ~750 (varies by organization)  
**Estimated Completion Time:** 5-8 hours  
**Review Cycle:** Semi-annual

### Sheet List
1. Instructions & Legend
2. Access Control Assessment
3. Integrity Protection Mechanisms
4. Secure Transmission Assessment
5. Retention Period Compliance
6. Storage Tier Implementation
7. Log Backup & Recovery
8. Disposal Procedures
9. Separation of Duties
10. Legal Hold Management
11. Gap Analysis
12. Summary Dashboard
13. Approval & Sign-Off

---

## Sheet 1: Instructions & Legend

Same structure as A.8.15.1 and A.8.15.2 with updated document information:

**Document ID:** ISMS-IMP-A.8.15.3  
**Assessment Area:** Log Protection, Integrity, and Retention Compliance  
**Related Policy:** ISMS-POL-A.8.15-S2.2, S2.3  
**Review Cycle:** Semi-annual

**Key Definitions:**
- **WORM:** Write-Once-Read-Many (immutable storage)
- **Cryptographic Hashing:** SHA-256/SHA-512 for integrity verification
- **Digital Signature:** Cryptographic proof of authenticity
- **Hot/Warm/Cold Storage:** Tiered retention based on access frequency
- **Legal Hold:** Suspension of normal retention/disposal for litigation
- **Separation of Duties:** System admins cannot modify their own logs
- **Secure Disposal:** Cryptographic erasure or physical destruction

---

## Sheet 2: Access Control Assessment

### Purpose
Assess log access controls per ISMS-POL-A.8.15-S2.2.2

### Column Structure (16 columns: A-P)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Log Source / SIEM Component | 30 | Text |
| B | Access Control Type | 20 | Dropdown: RBAC, ACL, None, Other |
| C | Authentication Required | 18 | Dropdown: Yes, No |
| D | Authorization Model | 20 | Dropdown: Role-Based, User-Based, Group-Based, None |
| E | Read Access Controlled | 18 | Dropdown: Yes, No, Partial |
| F | Write Access Prevented | 20 | Dropdown: Yes (read-only), No, Partial |
| G | Delete Access Controlled | 20 | Dropdown: Yes (restricted), No |
| H | Admin Separation | 20 | Dropdown: Yes (separated), No, N/A |
| I | Access Logged (Meta-logging) | 20 | Dropdown: Yes, No |
| J | MFA Required for Admin | 20 | Dropdown: Yes, No, N/A |
| K | Last Access Review Date | 18 | Date: DD.MM.YYYY |
| L | Access Review Frequency | 20 | Dropdown: Quarterly, Semi-annual, Annual, None |
| M | Non-Compliance Issues | 40 | Text |
| N | Compliance Score | 15 | Formula: Based on Yes/No answers |
| O | Remediation Required | 18 | Dropdown: Yes, No |
| P | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers and instructions
- **Row 8:** Example data
- **Rows 9-100:** Data entry (92 rows)

### Formula
**Compliance Score (Column N):**
```excel
=IF(A2="","",(COUNTIF(C2:J2,"Yes")+COUNTIF(C2:J2,"Yes (read-only)")+COUNTIF(C2:J2,"Yes (restricted)")+COUNTIF(C2:J2,"Yes (separated)"))/8*100)
```

### Target Compliance
- **Critical logs (P1):** 100% compliance (all "Yes")
- **High priority (P2):** ≥95% compliance
- **Medium priority (P3):** ≥90% compliance

---

## Sheet 3: Integrity Protection Mechanisms

### Purpose
Assess integrity protection per ISMS-POL-A.8.15-S2.2.4

### Column Structure (17 columns: A-Q)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Log Source / Storage | 30 | Text |
| B | Log Criticality | 18 | Dropdown: Critical, High, Medium, Low |
| C | Write-Once Storage (WORM) | 20 | Dropdown: Yes, No, N/A |
| D | WORM Technology | 25 | Dropdown: Hardware WORM, Software WORM, Cloud Object Lock, None |
| E | Cryptographic Hashing | 20 | Dropdown: Yes, No |
| F | Hash Algorithm | 18 | Dropdown: SHA-256, SHA-512, SHA-3, MD5 (weak), None |
| G | Hash Storage Location | 25 | Text: Separate from logs? |
| H | Digital Signatures | 18 | Dropdown: Yes, No |
| I | File Sealing | 18 | Dropdown: Yes, No, N/A |
| J | Integrity Check Frequency | 20 | Dropdown: Daily, Weekly, Monthly, None |
| K | Last Integrity Check | 18 | Date: DD.MM.YYYY |
| L | Tampering Detected | 18 | Dropdown: Never, Historical, Recent |
| M | Backup Protected | 18 | Dropdown: Yes, No |
| N | Compliance with Policy | 20 | Formula: Based on criticality requirements |
| O | Gap Description | 40 | Text |
| P | Remediation Plan | 40 | Text |
| Q | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-100:** Data entry

### Minimum Requirements by Criticality
**Critical:** WORM + Hashing (SHA-256+) + Daily integrity checks  
**High:** Hashing (SHA-256+) + Weekly integrity checks  
**Medium:** Access controls + Monthly integrity checks  
**Low:** Basic access controls

---

## Sheet 4: Secure Transmission Assessment

### Purpose
Assess log transmission security per ISMS-POL-A.8.15-S2.2.3

### Column Structure (14 columns: A-N)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Source System | 30 | Text |
| B | Destination (SIEM) | 25 | Text |
| C | Transport Protocol | 20 | Dropdown: TLS, TCP, UDP, HTTPS, Other |
| D | Encryption in Transit | 18 | Dropdown: Yes (TLS), No |
| E | TLS Version | 15 | Dropdown: TLS 1.3, TLS 1.2, TLS 1.1 (weak), TLS 1.0 (weak), None |
| F | Certificate Validation | 20 | Dropdown: Yes, No, N/A |
| G | Network Segment | 20 | Dropdown: Isolated Mgmt Network, Internal Network, Internet, DMZ |
| H | Firewall Protection | 18 | Dropdown: Yes, No |
| I | Source Authentication | 20 | Dropdown: Yes (mutual TLS/certs), No |
| J | Vulnerability Risk | 18 | Dropdown: None, Low, Medium, High |
| K | Compliance Status | 18 | Formula: TLS 1.2+ on untrusted = compliant |
| L | Remediation Required | 18 | Dropdown: Yes, No |
| M | Target Date | 15 | Date |
| N | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-200:** Data entry (one per log transmission path)

### Policy Requirement
TLS 1.2 or higher required for log transmission across untrusted networks (Internet, DMZ)

---

## Sheet 5: Retention Period Compliance

### Purpose
Assess retention period compliance per ISMS-POL-A.8.15-S2.3.2

### Column Structure (18 columns: A-R)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Log Source / Type | 30 | Text |
| B | Log Category | 20 | Dropdown: Security, Authentication, Admin, Application, System, Network, Database |
| C | Regulatory Requirement | 25 | Dropdown: PCI DSS, HIPAA, SOX, GDPR, FADP, ISO 27001, None |
| D | Policy Retention (months) | 20 | Number: Per S2.3 |
| E | Hot Storage Period (months) | 22 | Number: Actual current |
| F | Warm Storage Period (months) | 22 | Number: Actual |
| G | Cold Storage Period (years) | 20 | Number: Actual |
| H | Total Retention (months) | 20 | Formula: =E+F+(G*12) |
| I | Meets Policy Requirement | 20 | Formula: =H>=D |
| J | Retention Gap (months) | 20 | Formula: =IF(I="Yes",0,D-H) |
| K | Over-Retention (months) | 20 | Formula: =IF(H<=D*1.5,0,H-D) |
| L | Automated Disposal | 18 | Dropdown: Yes, No |
| M | Last Disposal Date | 18 | Date: DD.MM.YYYY |
| N | Legal Hold Capability | 18 | Dropdown: Yes, No |
| O | Compliance Status | 18 | Formula: Green if meets requirement |
| P | Remediation Action | 40 | Text |
| Q | Target Date | 15 | Date |
| R | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-100:** Data entry (log types)

### Quick Reference Table (Below data, rows 105-120)
Standard retention periods by log type from ISMS-POL-A.8.15-S2.3.2.3:

| Log Category | Minimum Retention | Regulatory Notes |
|--------------|-------------------|------------------|
| Security Events | 12 months | ISO 27001, most regulations |
| Authentication | 12 months | PCI DSS: 12 months |
| Administrative Actions | 12 months | SOX: audit trail |
| Financial Transactions | 7 years | SOX compliance |
| Healthcare Access | 6 years | HIPAA |
| Payment Card Data | 12 months | PCI DSS |

---

## Sheet 6: Storage Tier Implementation

### Purpose
Assess tiered storage implementation per ISMS-POL-A.8.15-S2.3.3

### Column Structure (15 columns: A-O)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Storage Tier | 20 | Dropdown: Hot, Warm, Cold |
| B | Technology | 25 | Dropdown: Local Disk/SSD, SAN, NAS, Object Storage, Tape, Other |
| C | Capacity (TB) | 15 | Number |
| D | Used (TB) | 15 | Number |
| E | % Used | 12 | Formula: =D/C |
| F | Retention Period | 20 | Text: What's stored here |
| G | Access Performance | 20 | Dropdown: Real-time (<1 min), Fast (<15 min), Slow (hours), Very Slow (days) |
| H | Encryption at Rest | 18 | Dropdown: Yes, No |
| I | Encryption Method | 20 | Dropdown: AES-256, AES-128, None |
| J | Geographic Location | 25 | Text: Data center, cloud region |
| K | Redundancy | 20 | Dropdown: None, Local (RAID), Remote (Replication), Both |
| L | Backup Implemented | 18 | Dropdown: Yes, No |
| M | Meets Policy Requirements | 20 | Formula: Based on tier expectations |
| N | Issues | 40 | Text |
| O | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-30:** Data entry (storage tiers per system)

### Tiering Assessment Questions (Rows 35-45)
- Is 3-tier model implemented (hot/warm/cold)?
- Are transitions automated?
- Are retention periods matched to tiers?
- Is encryption at rest implemented for all tiers?
- Is geographic redundancy implemented?

---

## Sheet 7: Log Backup & Recovery

### Purpose
Assess backup and recovery capabilities per ISMS-POL-A.8.15-S2.2.7

### Column Structure (16 columns: A-P)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Backup Scope | 30 | Dropdown: All Logs, Hot Storage Only, Critical Logs Only, None |
| B | Backup Frequency | 20 | Dropdown: Daily, Weekly, Monthly |
| C | Backup Technology | 25 | Text: Product/solution |
| D | Backup Location | 30 | Dropdown: Same Site, Offsite, Cloud, Multiple |
| E | Backup Encrypted | 18 | Dropdown: Yes, No |
| F | Encryption Algorithm | 20 | Dropdown: AES-256, AES-128, None |
| G | Backup Integrity Verified | 20 | Dropdown: Yes (periodic), Yes (always), No |
| H | Last Backup Date | 18 | Date: DD.MM.YYYY |
| I | Last Restore Test Date | 18 | Date: DD.MM.YYYY |
| J | Restore Test Frequency | 20 | Dropdown: Quarterly, Semi-annual, Annual, Never |
| K | Last Restore Success | 18 | Dropdown: Yes, No, Not Tested |
| L | RTO (Recovery Time) | 20 | Text: Hours/days |
| M | RPO (Recovery Point) | 20 | Text: Hours/days data loss acceptable |
| N | Backup Retention Period | 20 | Text: How long backups kept |
| O | Compliance Status | 18 | Formula |
| P | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-25:** Data entry (backup configurations)

### Minimum Requirements
- Daily backups for critical logs
- Offsite/separate location storage
- Quarterly restore testing
- Encryption for backups

---

## Sheet 8: Disposal Procedures

### Purpose
Assess secure disposal practices per ISMS-POL-A.8.15-S2.3.5

### Column Structure (14 columns: A-N)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Log Type / Source | 30 | Text |
| B | Retention Period Expired | 20 | Date: When eligible |
| C | Automated Disposal | 18 | Dropdown: Yes, No |
| D | Disposal Method | 25 | Dropdown: Cryptographic Erasure, Multi-pass Overwrite, Physical Destruction, Deletion |
| E | Disposal Approval Required | 22 | Dropdown: Yes (manual), No (automated), N/A |
| F | Legal Hold Check | 18 | Dropdown: Yes (checked), No, N/A |
| G | Disposal Logged | 18 | Dropdown: Yes, No |
| H | Last Disposal Date | 18 | Date: DD.MM.YYYY |
| I | Volume Disposed (GB) | 20 | Number |
| J | Disposal Verification | 20 | Dropdown: Verified, Not Verified |
| K | Compliance with Policy | 20 | Formula |
| L | Issues | 40 | Text |
| M | Remediation | 40 | Text |
| N | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-50:** Data entry

### Key Checks
- No premature disposal (before retention period)
- Legal hold respected
- Disposal logged (meta-logging)
- Secure disposal methods used
- Cryptographic erasure preferred over simple deletion

---

## Sheet 9: Separation of Duties

### Purpose
Assess separation of duties per ISMS-POL-A.8.15-S2.2.6

### Column Structure (14 columns: A-N)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | System / Component | 30 | Text |
| B | System Administrator(s) | 30 | Text: Names/roles |
| C | Log Administrator(s) | 30 | Text: Names/roles |
| D | Roles Separated | 18 | Dropdown: Yes (different people), No (same people), Partial |
| E | Sys Admin Can Modify Logs | 25 | Dropdown: No (compliant), Yes (violation), Limited |
| F | Compensating Controls | 40 | Text: If separation not feasible |
| G | Break-Glass Procedure | 20 | Dropdown: Yes (documented), No |
| H | Break-Glass Usage Logged | 22 | Dropdown: Yes, No, N/A |
| I | Independent Review | 20 | Dropdown: Yes, No, Frequency |
| J | Last Review Date | 18 | Date: DD.MM.YYYY |
| K | Violations Detected | 18 | Dropdown: None, Historical, Recent |
| L | Compliance Status | 18 | Formula |
| M | Remediation Plan | 40 | Text |
| N | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-50:** Data entry

### Critical Assessment
Systems with poor separation of duties = **HIGH RISK**
- System admins should not be able to modify logs they generate
- Compensating controls required if technical separation not feasible
- Independent review of admin actions mandatory

---

## Sheet 10: Legal Hold Management

### Purpose
Track legal holds per ISMS-POL-A.8.15-S2.3.6

### Column Structure (13 columns: A-M)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Hold ID | 15 | Auto: HOLD-001 |
| B | Hold Name / Matter | 30 | Text: Case name |
| C | Initiation Date | 15 | Date: DD.MM.YYYY |
| D | Initiated By | 25 | Text: Legal counsel name |
| E | Scope Description | 40 | Text: What logs covered |
| F | Systems/Sources Affected | 30 | Text |
| G | Date Range | 20 | Text: From date to date |
| H | Hold Status | 15 | Dropdown: Active, Released, Suspended |
| I | Review Date | 15 | Date: Quarterly review |
| J | Disposal Prevented | 18 | Dropdown: Yes (verified), No |
| K | Release Date | 15 | Date: If released |
| L | Release Authorized By | 25 | Text |
| M | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-30:** Data entry (active legal holds)

### Compliance Check
Verify no logs under legal hold have been disposed of prematurely

---

## Sheet 11: Gap Analysis

### Purpose
Consolidated protection & retention gaps

### Column Structure (12 columns: A-L)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Gap ID | 12 | Auto: GAP-001 |
| B | Gap Category | 25 | Dropdown: Access Control, Integrity Protection, Transmission Security, Retention Non-Compliance, Backup, Disposal, Separation of Duties, Other |
| C | Description | 50 | Text |
| D | Affected Systems | 30 | Text |
| E | Policy Requirement | 30 | Text: S2.2.x or S2.3.x reference |
| F | Risk Level | 15 | Dropdown: Critical, High, Medium, Low |
| G | Remediation Action | 50 | Text |
| H | Owner | 25 | Text |
| I | Target Date | 15 | Date: DD.MM.YYYY |
| J | Budget Required | 15 | Dropdown: Yes, No |
| K | Status | 15 | Dropdown: Open, In Progress, Resolved, Deferred |
| L | Notes | 40 | Text |

Same structure as previous IMPs.

---

## Sheet 12: Summary Dashboard

### Section 1: Protection Compliance Summary (Rows 3-15)

| Protection Measure | Compliant Count | Non-Compliant | % Compliant | Target |
|-------------------|-----------------|---------------|-------------|--------|
| Access Controls | COUNTIF | COUNTIF | Formula | 100% |
| Integrity Protection | COUNTIF | COUNTIF | Formula | >95% |
| Secure Transmission | COUNTIF | COUNTIF | Formula | 100% (critical) |
| Backup Implemented | COUNTIF | COUNTIF | Formula | >95% |
| Separation of Duties | COUNTIF | COUNTIF | Formula | >90% |

### Section 2: Retention Compliance Summary (Rows 17-25)

| Log Category | Compliant | Under-Retained | Over-Retained | % Compliant |
|--------------|-----------|----------------|---------------|-------------|
| Security | COUNT | COUNT | COUNT | Formula |
| Authentication | COUNT | COUNT | COUNT | Formula |
| Administrative | COUNT | COUNT | COUNT | Formula |
| Application | COUNT | COUNT | COUNT | Formula |
| Overall | TOTAL | TOTAL | TOTAL | Formula |

### Section 3: Gap Summary by Risk (Rows 27-35)

| Risk Level | Open Gaps | In Progress | Resolved | Overdue |
|------------|-----------|-------------|----------|---------|
| Critical | COUNT | COUNT | COUNT | COUNT |
| High | COUNT | COUNT | COUNT | COUNT |
| Medium | COUNT | COUNT | COUNT | COUNT |
| Low | COUNT | COUNT | COUNT | COUNT |

### Section 4: Charts (Rows 37-60)
- Compliance status pie chart
- Retention period distribution
- Protection mechanisms in use (WORM, Hashing, etc.)

### Section 5: Key Findings & Recommendations (Rows 62-80)

---

## Sheet 13: Approval & Sign-Off

### Approval Table

| Role | Name | Date | Signature | Status |
|------|------|------|-----------|--------|
| Log Administrator | [Name] | DD.MM.YYYY | _____ | ☐ Reviewed |
| IT Operations Manager | [Name] | DD.MM.YYYY | _____ | ☐ Reviewed |
| Information Security Manager | [Name] | DD.MM.YYYY | _____ | ☐ Approved |
| Legal/Compliance Officer | [Name] | DD.MM.YYYY | _____ | ☐ Reviewed |

---

## File Naming Convention

**Filename:** `ISMS-IMP-A_8_15_3_Log_Protection_Retention_YYYYMMDD.xlsx`

---

**END OF ISMS-IMP-A.8.15.3 SPECIFICATION**