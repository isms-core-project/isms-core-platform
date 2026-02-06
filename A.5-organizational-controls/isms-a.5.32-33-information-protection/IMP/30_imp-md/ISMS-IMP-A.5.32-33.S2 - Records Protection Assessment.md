**ISMS-IMP-A.5.32-33.S2 - Records Protection Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.33: Protection of Records

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.32-33.S2 |
| **Version** | 1.0 |
| **Assessment Area** | Records Identification, Classification, Protection Controls, and Integrity Verification |
| **Related Policy** | ISMS-POL-A.5.32-33, Section 2.2 (Records Protection) |
| **Purpose** | Guide users through systematic records inventory, classification, protection assessment, and integrity verification |
| **Target Audience** | Records Manager, CISO, Legal Counsel, System Owners, IT Teams, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Annual or After Significant System Changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Records Protection assessment workbook | ISMS Implementation Team |

---

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Sheet-by-Sheet Guidance
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Workbook Structure
  - Sheet-by-Sheet Specifications
  - Cell Styling Reference
  - Integration Points

---

# PART I: USER COMPLETION GUIDE

**Audience:** Records Manager, CISO, Legal Counsel, System Owners, IT Teams, Compliance Officers

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.32-33.S2 - Records Protection Assessment

### ISO/IEC 27001:2022 Control Reference

**Control A.5.33 - Protection of Records:**

> *Records should be protected from loss, destruction, falsification, unauthorised access and unauthorised release in accordance with legislative, regulatory, contractual and business requirements.*

This control ensures that records are properly protected throughout their lifecycle, maintaining confidentiality, integrity, and availability as required by law and business needs.

### What This Assessment Covers

This assessment documents the **protection mechanisms** for organisational records:

- What records does [Organisation] maintain that require protection?
- How are records classified based on retention and protection requirements?
- What controls protect records from loss, destruction, and falsification?
- How is record integrity verified and maintained?
- What access controls restrict unauthorised access and release?
- How are legal hold requirements managed?

### Key Principle

This assessment focuses on **records protection** - the technical and administrative controls that ensure records remain available, accurate, and confidential throughout their required retention period.

### What You'll Document

- **Records Inventory** listing all record categories requiring protection
- **Records Classification** based on retention requirements and sensitivity
- **Protection Controls Assessment** documenting controls per record category
- **Integrity Verification** mechanisms and testing results
- **Access Control Review** for record storage systems
- **Legal Hold Register** for litigation and investigation holds
- **Backup Verification** for records availability protection
- **Gap Analysis** identifying protection deficiencies
- **Evidence Register** linking documentation to audit artefacts
- **Approved Assessment** with Records Manager and CISO sign-offs

### How This Relates to Other A.5.32-33 Assessments

| Assessment | Focus | Relationship to A.5.32-33.2 |
|------------|-------|--------------------------|
| ISMS-IMP-A.5.32-33.S1 | IP Rights Inventory | Provides IP classification that may apply to records |
| **ISMS-IMP-A.5.32-33.S2** | **Records Protection** | **Core - HOW records are protected** |
| ISMS-IMP-A.5.32-33.S3 | Retention & Disposal | Uses protection assessment to inform disposal decisions |
| ISMS-IMP-A.5.32-33.S4 | Compliance Dashboard | Aggregates metrics from all assessments |

## Who Should Complete This Assessment

### Primary Stakeholders

1. **Records Manager** - Leads assessment, ensures records inventory completeness, validates protection controls
2. **Chief Information Security Officer (CISO)** - Validates technical protection controls, integrity mechanisms
3. **Legal Counsel** - Validates legal hold requirements, regulatory retention compliance
4. **IT Operations** - Provides backup verification, system access controls, storage documentation
5. **Internal Audit** - Validates control effectiveness, reviews evidence

### Required Skills

- Understanding of records management principles and lifecycle
- Knowledge of [Organisation]'s record retention requirements
- Familiarity with backup and recovery systems
- Understanding of access control mechanisms
- Ability to assess integrity verification methods

### Time Commitment

- **Initial assessment:** 15-25 hours (depending on organisation size and records complexity)
- **Annual updates:** 4-6 hours (verify changes, update for new record categories)

## Expected Outputs

Upon completion, you will have:

1. **Records Category Inventory** - All record types with classifications
2. **Protection Controls Matrix** - Controls documented per record category
3. **Integrity Verification Results** - Testing outcomes and remediation
4. **Access Control Review** - Access rights verification
5. **Legal Hold Register** - Active holds documented
6. **Backup Verification Report** - Recovery testing results
7. **Gap Analysis** - Protection deficiencies with remediation plans
8. **Evidence Register** - Supporting documentation
9. **Approved Assessment** - Records Manager and CISO sign-offs

---

# Prerequisites

## Information You'll Need

Before starting this assessment, gather:

### Records Documentation

- Existing records inventory or classification scheme
- Retention schedule documentation
- Records management policy
- Filing system documentation (physical and electronic)

### Legal and Regulatory Requirements

- Applicable record retention regulations (Swiss CO, FINMA, sector-specific)
- Legal hold notifications and release records
- Regulatory examination correspondence
- Audit record requirements

### Technical Documentation

- Backup and recovery procedures
- Storage system documentation
- Access control configurations
- Integrity verification mechanisms (checksums, digital signatures)

### Compliance Evidence

- Previous records audit reports
- Backup test results
- Access review documentation
- Integrity check logs

## Access Required

You will need access to:

**Systems:**

- [ ] Document management systems
- [ ] File storage systems (network shares, cloud storage)
- [ ] Backup and recovery systems
- [ ] Access control/identity management systems
- [ ] Records management applications

**Documents:**

- [ ] Records retention schedule
- [ ] Legal hold notices
- [ ] Backup procedures and test results
- [ ] Access control policies

**People:**

- [ ] Records custodians across departments
- [ ] IT backup administrators
- [ ] Legal counsel for hold requirements
- [ ] System administrators for access control

## Tools and Resources

**Assessment Workbook:** Excel workbook (generated by `generate_a532_33_2_records_protection.py`) containing:

- Sheet 1: Instructions & Legend
- Sheet 2: Records Category Inventory
- Sheet 3: Protection Controls Assessment
- Sheet 4: Integrity Verification
- Sheet 5: Access Control Review
- Sheet 6: Legal Hold Register
- Sheet 7: Backup Verification
- Sheet 8: Gap Analysis
- Sheet 9: Evidence Register
- Sheet 10: Approval & Sign-Off

---

# Assessment Workflow

## High-Level Process

```
1. PREPARE (Gather prerequisites, set up assessment team)
   |
2. INVENTORY RECORDS (Identify all record categories)
   |
3. CLASSIFY RECORDS (Assign protection requirements)
   |
4. ASSESS PROTECTION CONTROLS (Technical, administrative, physical)
   |
5. VERIFY INTEGRITY (Test integrity mechanisms)
   |
6. REVIEW ACCESS CONTROLS (Validate authorisation)
   |
7. VERIFY BACKUPS (Test recovery capability)
   |
8. IDENTIFY GAPS (Document deficiencies)
   |
9. COLLECT EVIDENCE (Link to documentation)
   |
10. REVIEW & APPROVE (Records Manager and CISO sign-off)
```

## Detailed Workflow

### Phase 1: Preparation (1-2 hours)

**Objective:** Set up assessment foundation

**Steps:**
1. Read this entire User Guide (PART I)
2. Gather all prerequisites (Section 2.1)
3. Review ISMS-POL-A.5.32-33 Section 2.2 for records classification framework
4. Identify all records custodians and schedule interviews
5. Request backup test results and access control reports
6. Create working folder for evidence collection

**Deliverable:** Assessment plan with custodian interview schedule

### Phase 2: Records Inventory (3-6 hours)

**Objective:** Identify ALL record categories requiring protection

**Steps:**
1. **Review Existing Documentation:**

   - Current retention schedule
   - Records management policy
   - Filing system documentation

2. **Department Interviews:**

   - Finance: Financial records, tax records, invoices
   - HR: Personnel files, payroll, benefits
   - Legal: Contracts, litigation files, regulatory correspondence
   - Operations: Project records, technical documentation
   - IT: System logs, change records, security logs

3. **Inventory Creation (Sheet 2):**

   - List EVERY record category
   - Document record type (financial, personnel, legal, operational, technical)
   - Assign custodian department
   - Note storage location(s) (physical, electronic, cloud)
   - Identify regulatory requirements affecting category

**Deliverable:** Complete Sheet 2 (Records Category Inventory)

**Quality Check:**

- All departments interviewed for record types
- Regulatory record requirements identified
- Both physical and electronic records captured
- Cloud-stored records documented
- Security and audit logs included

### Phase 3: Records Classification (2-4 hours)

**Objective:** Classify records based on protection requirements

**Steps:**
1. Review records classification framework (ISMS-POL-A.5.32-33 Section 2.2):

   | Category | Retention Period | Protection Requirement | Examples |
   |----------|-----------------|----------------------|----------|
   | **Legal/Contracts** | Duration + 10 years | Confidential, integrity protected | Contracts, legal agreements |
   | **Financial** | 10 years (Swiss CO) | Confidential, tamper-evident | Invoices, ledgers, tax records |
   | **Personnel** | Employment + 10 years | Confidential, privacy protected | HR files, payroll |
   | **Regulatory** | Per regulation | Per classification | Audit reports, compliance evidence |
   | **Technical** | System lifecycle + 3 years | Internal minimum | Configurations, change records |
   | **Operational** | 3-7 years | Internal | Meeting minutes, project files |
   | **Security/Audit** | 2-7 years | Confidential, integrity protected | Access logs, incident records |

2. For EACH record category, determine:

   - Retention requirement (regulatory, contractual, business)
   - Confidentiality requirement (Restricted, Confidential, Internal, Public)
   - Integrity requirement (Critical, High, Standard)
   - Availability requirement (Mission Critical, Business Critical, Standard)

**Deliverable:** Sheet 2 complete with classification columns populated

### Phase 4: Protection Controls Assessment (4-8 hours)

**Objective:** Document protection controls for each record category

**Steps:**
1. **Confidentiality Controls:**

   - Access restrictions (role-based, need-to-know)
   - Encryption (at rest, in transit)
   - Physical security (locked storage, secure areas)
   - DLP monitoring

2. **Integrity Controls:**

   - Version control
   - Digital signatures
   - Checksums/hash verification
   - Write-once storage (WORM)
   - Audit logging

3. **Availability Controls:**

   - Backup frequency and type
   - Geographic redundancy
   - Recovery point objectives (RPO)
   - Recovery time objectives (RTO)
   - Media refresh plans

4. **Complete Sheet 3 (Protection Controls Assessment):**

   - One row per record category
   - Document applicable controls
   - Rate control effectiveness
   - Identify protection gaps

**Deliverable:** Sheet 3 complete with controls documented

### Phase 5: Integrity Verification (2-4 hours)

**Objective:** Test and document integrity verification mechanisms

**Steps:**
1. **Identify Integrity Mechanisms:**

   - Checksum/hash algorithms in use
   - Digital signature implementations
   - Write-once storage configurations
   - Audit log tamper protection

2. **Test Integrity Verification:**

   - Run checksum verification on sample records
   - Verify digital signature validity
   - Test audit log integrity
   - Confirm WORM compliance

3. **Complete Sheet 4 (Integrity Verification):**

   - Record category tested
   - Integrity mechanism
   - Test performed
   - Test result (Pass/Fail)
   - Issues identified
   - Remediation actions

**Deliverable:** Sheet 4 complete with test results

### Phase 6: Access Control Review (2-4 hours)

**Objective:** Verify access controls for record storage systems

**Steps:**
1. **Review Access Rights:**

   - Who has access to each record category?
   - Are access rights based on need-to-know?
   - When were access rights last reviewed?
   - Are privileged accounts appropriately restricted?

2. **Verify Access Logging:**

   - Is access logged?
   - Are logs protected from tampering?
   - How long are logs retained?

3. **Complete Sheet 5 (Access Control Review):**

   - Record storage system
   - Access control type
   - Users/groups with access
   - Last access review date
   - Access logging status
   - Issues identified

**Deliverable:** Sheet 5 complete with access review

### Phase 7: Legal Hold Management (1-2 hours)

**Objective:** Document legal hold register

**Steps:**
1. **Review Active Legal Holds:**

   - Current litigation holds
   - Regulatory investigation holds
   - Internal investigation holds

2. **Complete Sheet 6 (Legal Hold Register):**

   - Hold identifier
   - Matter description
   - Effective date
   - Record categories affected
   - Custodians notified
   - Release date (if applicable)
   - Status

**Deliverable:** Sheet 6 complete with legal holds

### Phase 8: Backup Verification (2-3 hours)

**Objective:** Verify backup and recovery capability

**Steps:**
1. **Review Backup Configuration:**

   - Backup frequency
   - Backup type (full, incremental, differential)
   - Retention periods
   - Geographic distribution

2. **Verify Recovery Testing:**

   - When was last recovery test?
   - What was tested?
   - Were RTOs/RPOs met?
   - Issues identified?

3. **Complete Sheet 7 (Backup Verification):**

   - Record category
   - Backup frequency
   - Last backup verified
   - Last recovery test
   - RTO/RPO compliance
   - Issues identified

**Deliverable:** Sheet 7 complete with backup verification

### Phase 9: Gap Analysis (1-2 hours)

**Objective:** Consolidate all identified gaps

**Steps:**
1. Review all previous sheets for gaps:

   - Protection control gaps (Sheet 3)
   - Integrity verification failures (Sheet 4)
   - Access control issues (Sheet 5)
   - Backup deficiencies (Sheet 7)

2. **Complete Sheet 8 (Gap Analysis):**

   - Gap description
   - Category (Confidentiality, Integrity, Availability)
   - Risk rating
   - Remediation action
   - Owner and due date

**Deliverable:** Sheet 8 complete with gaps documented

### Phase 10: Evidence Collection (1-2 hours)

**Objective:** Document supporting evidence

**Steps:**
1. Gather evidence for findings:

   - Backup test reports
   - Access control configurations
   - Integrity check logs
   - Legal hold notifications

2. **Complete Sheet 9 (Evidence Register):**

   - Evidence ID and description
   - Related finding
   - Storage location
   - Verification status

**Deliverable:** Sheet 9 complete

### Phase 11: Review & Approval (1-2 hours)

**Objective:** Obtain formal sign-off

**Steps:**
1. Review with Records Manager
2. Review with CISO
3. Complete Sheet 10 (Approval & Sign-Off)

**Deliverable:** Approved assessment

---

# Sheet-by-Sheet Completion Guidance

## Sheet 2: Records Category Inventory

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Record Category ID | Unique identifier | REC-001 |
| Category Name | Descriptive name | Financial Ledgers |
| Record Type | Financial/Personnel/Legal/etc. | Financial |
| Description | What records are included | General ledger, sub-ledgers, journal entries |
| Custodian Department | Responsible department | Finance |
| Storage Location | Where records are stored | SAP, File Server FS-01 |
| Format | Physical/Electronic/Both | Electronic |
| Retention Requirement | Regulatory/contractual basis | Swiss CO Art. 958f - 10 years |
| Confidentiality | Restricted/Confidential/Internal/Public | Confidential |
| Integrity Requirement | Critical/High/Standard | Critical |
| Availability Requirement | Mission Critical/Business Critical/Standard | Business Critical |

## Sheet 3: Protection Controls Assessment

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Record Category ID | Reference to Sheet 2 | REC-001 |
| Category Name | From Sheet 2 | Financial Ledgers |
| Confidentiality Controls | Access restrictions, encryption | Role-based access, AES-256 at rest |
| Integrity Controls | Version control, signatures | Database audit logging, monthly checksums |
| Availability Controls | Backups, redundancy | Daily backup, geo-redundant storage |
| Physical Controls | If applicable | N/A - Electronic only |
| Control Effectiveness | Effective/Partial/Ineffective | Effective |
| Gap Description | Any protection gaps | No quarterly integrity verification |
| Remediation Needed | Required actions | Implement quarterly checksum verification |

## Sheet 4: Integrity Verification

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Test ID | Unique identifier | INT-001 |
| Record Category | Category tested | Financial Ledgers |
| Integrity Mechanism | How integrity is verified | SHA-256 checksums |
| Test Date | When test performed | 2026-01-15 |
| Test Performed | What was tested | Checksum verification on 2025 year-end close |
| Expected Result | What should happen | Checksums match stored values |
| Actual Result | What happened | All checksums matched |
| Status | Pass/Fail | Pass |
| Issues | Any problems found | None |
| Remediation | Actions if failed | N/A |

## Sheet 5: Access Control Review

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| System Name | Storage system | SAP ERP |
| Record Categories | What records are stored | Financial Ledgers, AR/AP |
| Access Control Type | RBAC/DAC/MAC | Role-based (RBAC) |
| User Count | Number with access | 45 users |
| Privileged Users | Admin/elevated access | 5 basis administrators |
| Last Access Review | When reviewed | 2025-11-15 |
| Access Logging | Yes/No | Yes |
| Log Retention | How long logs kept | 2 years |
| Issues | Problems found | 3 inactive users still with access |
| Remediation | Actions needed | Remove inactive user access |

## Sheet 6: Legal Hold Register

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Hold ID | Unique identifier | LH-2025-001 |
| Matter Name | Case/investigation name | Vendor Contract Dispute |
| Legal Counsel | Responsible attorney | External - Smith & Jones LLP |
| Effective Date | When hold began | 2025-06-01 |
| Record Categories | What records affected | Contracts, Invoices, Correspondence |
| Custodians Notified | Who was notified | Finance, Procurement, Legal |
| Notification Date | When notified | 2025-06-02 |
| Release Date | When hold ended | [Active] |
| Status | Active/Released | Active |
| Notes | Additional information | Annual renewal confirmed 2026-01-15 |

## Sheet 7: Backup Verification

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Record Category | Category backed up | Financial Ledgers |
| Backup System | What performs backup | Veeam Backup |
| Backup Frequency | How often | Daily incremental, weekly full |
| Backup Location | Where stored | Azure Blob Storage (CH North) |
| Last Backup Date | Most recent backup | 2026-02-02 |
| Last Verification | When backup verified | 2026-02-01 |
| Last Recovery Test | When recovery tested | 2025-12-15 |
| RTO Target | Recovery time objective | 4 hours |
| RTO Achieved | Actual recovery time | 2.5 hours |
| RPO Target | Recovery point objective | 24 hours |
| RPO Achieved | Actual data loss | 18 hours |
| Status | Compliant/Non-Compliant | Compliant |
| Issues | Problems found | None |

---

# Evidence Collection

## Required Evidence

For each protection control area, collect:

**Confidentiality:**
- Access control policy documentation
- Encryption configuration evidence
- DLP policy evidence

**Integrity:**
- Checksum/hash verification logs
- Digital signature certificates
- WORM storage configuration
- Audit log samples

**Availability:**
- Backup procedure documentation
- Backup job logs
- Recovery test reports
- Redundancy architecture diagrams

**Legal Holds:**
- Legal hold notices
- Custodian acknowledgments
- Release documentation

## Evidence Storage

Store all evidence in:
- **Primary Location:** ISMS Evidence Library (SharePoint/Confluence or equivalent)
- **Folder Structure:** `/ISMS/A.5.32-33/Records-Protection/[Assessment-Date]/`
- **Naming Convention:** `EV-[ID]_[Description]_[Date].ext`

---

# Common Pitfalls

Avoid these common mistakes:

**MISTAKE: Only assessing electronic records**
- Physical records (paper files, microfiche) also require protection
- Include physical storage locations in assessment

**MISTAKE: Assuming backups mean records are protected**
- Backups address availability, not confidentiality or integrity
- Verify all three protection dimensions

**MISTAKE: Not testing integrity verification mechanisms**
- Having checksums is not enough - they must be verified
- Test integrity mechanisms, not just document them

**MISTAKE: Ignoring legal holds in retention decisions**
- Legal holds override normal retention schedules
- Maintain accurate legal hold register

**MISTAKE: Not verifying backup recovery capability**
- Backups that cannot be restored provide no protection
- Regular recovery testing is essential

**MISTAKE: Treating assessment as one-time activity**
- Records and threats change over time
- Schedule regular reassessment

**MISTAKE: Not coordinating with IT Operations**
- Protection controls often depend on IT systems
- IT must validate technical control effectiveness

**MISTAKE: Missing cloud-stored records**
- SaaS applications may contain records
- Include cloud storage in assessment scope

**MISTAKE: Not considering record metadata**
- Metadata (creation date, author, modifications) requires protection
- Metadata integrity is part of record integrity

**MISTAKE: Overlooking audit logs as records**
- Security and audit logs are records requiring protection
- Apply same protection framework to log data

---

# Quality Checklist

Before submitting for approval, verify:

**Records Inventory (Sheet 2):**
- [ ] All departments interviewed for record types
- [ ] Physical and electronic records captured
- [ ] Cloud-stored records included
- [ ] Regulatory requirements documented
- [ ] Custodians assigned

**Protection Controls (Sheet 3):**
- [ ] All record categories assessed
- [ ] Confidentiality, Integrity, Availability all addressed
- [ ] Control effectiveness evaluated
- [ ] Gaps identified

**Integrity Verification (Sheet 4):**
- [ ] Integrity mechanisms identified
- [ ] Testing performed
- [ ] Results documented
- [ ] Failures remediated

**Access Control (Sheet 5):**
- [ ] All storage systems reviewed
- [ ] Access rights verified
- [ ] Logging confirmed
- [ ] Issues identified

**Legal Holds (Sheet 6):**
- [ ] All active holds documented
- [ ] Custodians notified
- [ ] Status current

**Backup Verification (Sheet 7):**
- [ ] Backup status verified
- [ ] Recovery testing performed
- [ ] RTO/RPO compliance confirmed

**Gap Analysis (Sheet 8):**
- [ ] All gaps consolidated
- [ ] Risk ratings assigned
- [ ] Remediation owners identified

**Evidence (Sheet 9):**
- [ ] Key evidence collected
- [ ] Storage locations documented
- [ ] Verification status current

---

# Review & Approval

## Review Process

1. **Self-Review:** Complete quality checklist
2. **Peer Review:** Another team member validates
3. **Records Manager Review:** Validates inventory and classification
4. **CISO Review:** Validates technical controls
5. **Final Approval:** Records Manager and CISO sign-off

## Escalation Path

- Minor gaps: Remediate within 30 days
- Medium gaps: Escalate to CISO
- Major gaps: Immediate escalation to Legal Counsel and Executive Management

---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook Developers, Python/Excel Script Maintainers

---

# Workbook Structure

## Generated File

**Filename:** `ISMS-IMP-A.5.32-33.S2_Records_Protection_Assessment_[YYYYMMDD].xlsx`

**Generator Script:** `generate_a532_33_2_records_protection.py`

## Sheet Overview

| Sheet # | Sheet Name | Purpose | Rows (Est.) |
|---------|------------|---------|-------------|
| 1 | Instructions | Usage guidance | ~50 |
| 2 | Records_Category_Inventory | Record types | 50+ |
| 3 | Protection_Controls | Controls per category | 50+ |
| 4 | Integrity_Verification | Test results | 30+ |
| 5 | Access_Control_Review | Access assessment | 30+ |
| 6 | Legal_Hold_Register | Active holds | 20+ |
| 7 | Backup_Verification | Backup status | 50+ |
| 8 | Gap_Analysis | Identified gaps | 30+ |
| 9 | Evidence_Register | Audit evidence | 50+ |
| 10 | Approval_SignOff | Formal approval | ~30 |

---

# Sheet-by-Sheet Specifications

## Sheet 2: Records_Category_Inventory

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Record Category ID | 18 | - |
| B | Category Name | 30 | - |
| C | Record Type | 15 | List: Financial, Personnel, Legal, Operational, Technical, Security, Regulatory |
| D | Description | 45 | - |
| E | Custodian Department | 20 | - |
| F | Storage Location | 30 | - |
| G | Format | 12 | List: Physical, Electronic, Both |
| H | Retention Requirement | 30 | - |
| I | Confidentiality | 15 | List: Restricted, Confidential, Internal, Public |
| J | Integrity Requirement | 12 | List: Critical, High, Standard |
| K | Availability Requirement | 18 | List: Mission Critical, Business Critical, Standard |
| L | Notes | 35 | - |

## Sheet 3: Protection_Controls

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Record Category ID | 18 | - |
| B | Category Name | 25 | - |
| C | Confidentiality Controls | 35 | - |
| D | Integrity Controls | 35 | - |
| E | Availability Controls | 35 | - |
| F | Physical Controls | 25 | - |
| G | Control Effectiveness | 15 | List: Effective, Partial, Ineffective |
| H | Gap Description | 35 | - |
| I | Remediation Needed | 35 | - |
| J | Status | 15 | List: Complete, In Progress, Not Started |

## Sheet 4: Integrity_Verification

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Test ID | 10 | - |
| B | Record Category | 25 | - |
| C | Integrity Mechanism | 25 | List: Checksum, Digital Signature, WORM, Audit Log, Database Constraints, Other |
| D | Test Date | 12 | Date |
| E | Test Performed | 35 | - |
| F | Expected Result | 25 | - |
| G | Actual Result | 25 | - |
| H | Status | 10 | List: Pass, Fail, Partial, Not Tested |
| I | Issues | 30 | - |
| J | Remediation | 30 | - |

## Sheet 5: Access_Control_Review

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | System Name | 25 | - |
| B | Record Categories | 30 | - |
| C | Access Control Type | 15 | List: RBAC, DAC, MAC, Mixed |
| D | User Count | 12 | Number |
| E | Privileged Users | 15 | Number |
| F | Last Access Review | 15 | Date |
| G | Access Logging | 12 | List: Yes, No, Partial |
| H | Log Retention | 15 | - |
| I | Issues | 30 | - |
| J | Remediation | 30 | - |
| K | Status | 15 | List: Compliant, Non-Compliant, Partial |

## Sheet 6: Legal_Hold_Register

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Hold ID | 15 | - |
| B | Matter Name | 30 | - |
| C | Legal Counsel | 25 | - |
| D | Effective Date | 12 | Date |
| E | Record Categories | 35 | - |
| F | Custodians Notified | 30 | - |
| G | Notification Date | 15 | Date |
| H | Release Date | 12 | Date |
| I | Status | 12 | List: Active, Released, Pending |
| J | Notes | 35 | - |

## Sheet 7: Backup_Verification

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Record Category | 25 | - |
| B | Backup System | 20 | - |
| C | Backup Frequency | 20 | List: Real-time, Hourly, Daily, Weekly, Monthly |
| D | Backup Location | 25 | - |
| E | Last Backup Date | 15 | Date |
| F | Last Verification | 15 | Date |
| G | Last Recovery Test | 15 | Date |
| H | RTO Target | 12 | - |
| I | RTO Achieved | 12 | - |
| J | RPO Target | 12 | - |
| K | RPO Achieved | 12 | - |
| L | Status | 15 | List: Compliant, Non-Compliant |
| M | Issues | 30 | - |

## Sheet 8: Gap_Analysis

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Gap ID | 10 | - |
| B | Gap Category | 15 | List: Confidentiality, Integrity, Availability, Process |
| C | Description | 45 | - |
| D | Related Record Category | 20 | - |
| E | Risk Rating | 12 | List: High, Medium, Low |
| F | Remediation Action | 40 | - |
| G | Owner | 20 | - |
| H | Due Date | 12 | Date |
| I | Status | 15 | List: Open, In Progress, Complete, Accepted |
| J | Notes | 30 | - |

## Sheet 9: Evidence_Register

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Evidence ID | 12 | - |
| B | Description | 40 | - |
| C | Evidence Type | 18 | List: Document, Screenshot, Report, Log, Configuration, Other |
| D | Related Item | 20 | - |
| E | Storage Location | 35 | - |
| F | Collected Date | 12 | Date |
| G | Collected By | 20 | - |
| H | Verification Status | 18 | List: Verified, Pending Review, Not Verified, Expired |

## Sheet 10: Approval_SignOff

### Layout
- Rows 1-2: Headers
- Rows 4-8: Assessment metadata
- Row 10: Approval section header
- Row 12: Approval table headers
- Rows 13+: Approver rows

### Approver Roles
1. Records Manager
2. Chief Information Security Officer
3. Legal Counsel
4. IT Operations Manager
5. Internal Audit Representative

---

# Cell Styling Reference

## Colour Palette

| Style Name | Hex Code | Usage |
|------------|----------|-------|
| Header Fill | #1F4E79 | Sheet headers |
| Subheader Fill | #2E75B6 | Secondary headers |
| Column Header | #D6DCE4 | Table headers |
| Input Cell | #FFFFCC | User input cells |
| High Risk | #FF6B6B | High priority items |
| Medium Risk | #FFA94D | Medium priority |
| Low Risk | #69DB7C | Low priority |
| Compliant | #C6EFCE | Compliant status |
| Warning | #FFEB9C | Attention needed |
| Non-Compliant | #FFC7CE | Non-compliant |

---

# Integration Points

## Related Workbooks

| Workbook | Integration Type | Data Exchange |
|----------|-----------------|---------------|
| ISMS-IMP-A.5.32-33.S1 | IP classification | IP records protection requirements |
| ISMS-IMP-A.5.32-33.S3 | Retention schedule | Protection informs disposal |
| ISMS-IMP-A.5.32-33.S4 | Dashboard | Metrics feed dashboard |
| ISMS-IMP-A.8.13 | Backup integration | Backup control alignment |
| ISMS-IMP-A.8.10 | Deletion | Secure disposal alignment |

---

**END OF SPECIFICATION**

---

*"Records management is not just about what you keep, but how you keep it."*
-- Anonymous

<!-- QA_VERIFIED: 2026-02-03 -->
