**ISMS-IMP-A.5.32-33.3 - Retention and Disposal Schedule Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.33: Protection of Records

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.32-33.3 |
| **Version** | 1.0 |
| **Assessment Area** | Records Retention Requirements, Disposal Schedule, Secure Destruction Verification |
| **Related Policy** | ISMS-POL-A.5.32-33, Section 2.2 (Retention Requirements, Records Disposal) |
| **Purpose** | Guide users through defining retention periods, managing disposal schedules, and verifying secure destruction |
| **Target Audience** | Records Manager, Legal Counsel, CISO, IT Operations, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Annual or After Regulatory Changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Retention and Disposal assessment workbook | ISMS Implementation Team |

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

**Audience:** Records Manager, Legal Counsel, CISO, IT Operations, Compliance Officers

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.32-33.3 - Retention and Disposal Schedule Assessment

### ISO/IEC 27001:2022 Control Reference

**Control A.5.33 - Protection of Records:**

> *Records should be protected from loss, destruction, falsification, unauthorised access and unauthorised release in accordance with legislative, regulatory, contractual and business requirements.*

This assessment focuses on the **retention** and **disposal** aspects of records protection - ensuring records are kept for required periods and disposed of securely when retention expires.

### What This Assessment Covers

This assessment documents the **lifecycle management** of organisational records:

- What retention periods apply to each record category?
- What regulatory, contractual, and business requirements determine retention?
- How does [Organisation] track retention expiration?
- What disposal methods are used for different record types?
- How is secure destruction verified and documented?
- What exception processes exist for retention extension or early disposal?


### Key Principle

Proper retention and disposal balances two competing requirements:
1. **Minimum Retention:** Records MUST be kept for required periods (regulatory, contractual, business)
2. **Maximum Retention:** Records SHOULD be disposed of after retention expires (storage limitation, risk reduction)

### What You'll Document

- **Retention Schedule** with all record categories and retention periods
- **Regulatory Mapping** showing which regulations drive retention
- **Disposal Tracking** for records approaching or past retention
- **Disposal Methods** appropriate for each record classification
- **Destruction Verification** with certificates and evidence
- **Exception Register** for retention extensions and early disposal
- **Compliance Monitoring** for schedule adherence
- **Gap Analysis** identifying retention/disposal issues
- **Evidence Register** linking documentation to audit artefacts


### How This Relates to Other A.5.32-33 Assessments

| Assessment | Focus | Relationship to A.5.32-33.3 |
|------------|-------|--------------------------|
| ISMS-IMP-A.5.32-33.1 | IP Rights Inventory | IP retention requirements |
| ISMS-IMP-A.5.32-33.2 | Records Protection | Protection during retention |
| **ISMS-IMP-A.5.32-33.3** | **Retention & Disposal** | **Lifecycle - WHEN and HOW** |
| ISMS-IMP-A.5.32-33.4 | Compliance Dashboard | Retention metrics |

## Who Should Complete This Assessment

### Primary Stakeholders

1. **Records Manager** - Leads assessment, maintains retention schedule, oversees disposal
2. **Legal Counsel** - Validates regulatory retention requirements, approves exceptions
3. **CISO** - Validates secure disposal methods, information security alignment
4. **IT Operations** - Executes electronic disposal, provides destruction evidence
5. **Compliance Officer** - Monitors compliance, reviews regulatory changes


### Required Skills

- Understanding of records retention regulations
- Knowledge of [Organisation]'s contractual obligations
- Familiarity with secure disposal methods
- Ability to track retention periods across record categories


### Time Commitment

- **Initial assessment:** 12-20 hours (depending on record complexity)
- **Annual updates:** 4-8 hours (regulatory review, schedule updates)


## Expected Outputs

Upon completion, you will have:

1. **Complete Retention Schedule** - All record categories with retention periods
2. **Regulatory Mapping** - Regulations driving each retention requirement
3. **Disposal Queue** - Records due for disposal
4. **Disposal Method Matrix** - Appropriate methods per classification
5. **Destruction Certificates** - Evidence of secure disposal
6. **Exception Register** - Retention extensions and early disposals
7. **Compliance Report** - Schedule adherence metrics
8. **Gap Analysis** - Issues with remediation plans
9. **Evidence Register** - Supporting documentation


---

# Prerequisites

## Information You'll Need

Before starting this assessment, gather:

### Regulatory Requirements

- Swiss Code of Obligations (CO) Art. 958f - Bookkeeping retention (10 years)
- Tax record requirements (cantonal and federal)
- Employment law record retention
- Sector-specific regulations (FINMA, healthcare, etc.)
- GDPR storage limitation requirements


### Contractual Requirements

- Customer contract data retention clauses
- Vendor agreement retention requirements
- Partnership/joint venture retention terms
- Insurance policy requirements


### Business Requirements

- Operational needs for record access
- Historical reference requirements
- Audit trail requirements
- Knowledge management needs


### Current Documentation

- Existing retention schedule (if any)
- Previous disposal records
- Legal hold register
- Records inventory from A.5.32-33.2


## Access Required

**Systems:**
- [ ] Records management system
- [ ] Document management system
- [ ] Email archival system
- [ ] Backup systems
- [ ] Destruction vendor portals


**Documents:**
- [ ] Regulatory requirements documentation
- [ ] Contract archive (for retention clauses)
- [ ] Previous destruction certificates
- [ ] Legal hold notices


**People:**
- [ ] Legal Counsel for regulatory interpretation
- [ ] IT for electronic disposal capabilities
- [ ] Department heads for business requirements
- [ ] Destruction vendors for service documentation


---

# Assessment Workflow

## High-Level Process

```
1. PREPARE (Gather prerequisites, regulatory requirements)
   |
2. DEFINE RETENTION SCHEDULE (Periods for all record categories)
   |
3. MAP REGULATORY REQUIREMENTS (Link regulations to retention)
   |
4. IDENTIFY DISPOSAL QUEUE (Records past retention)
   |
5. DEFINE DISPOSAL METHODS (Appropriate per classification)
   |
6. VERIFY DESTRUCTION (Certificates and evidence)
   |
7. MANAGE EXCEPTIONS (Extensions and early disposal)
   |
8. MONITOR COMPLIANCE (Schedule adherence)
   |
9. IDENTIFY GAPS (Issues and remediation)
   |
10. REVIEW & APPROVE (Legal Counsel and Records Manager sign-off)
```

## Detailed Workflow

### Phase 1: Preparation (1-2 hours)

**Objective:** Set up assessment foundation

**Steps:**
1. Read this User Guide
2. Gather regulatory requirements
3. Review existing retention schedule (if any)
4. Obtain records inventory from A.5.32-33.2
5. Schedule meetings with Legal Counsel


### Phase 2: Define Retention Schedule (4-8 hours)

**Objective:** Establish retention periods for all record categories

**Steps:**
1. **Regulatory Research:**

   - Swiss CO Art. 958f: Bookkeeping records - 10 years
   - Tax records: 10 years (cantonal variations)
   - Employment records: Employment + 10 years
   - GDPR: Purpose-based (storage limitation)
   - Sector-specific requirements


2. **Contractual Review:**

   - Review customer contracts for data retention clauses
   - Review vendor agreements
   - Identify contractual minimums and maximums


3. **Business Requirements:**

   - Interview department heads
   - Identify operational access needs
   - Document historical reference needs


4. **Complete Retention Schedule (Sheet 2):**

   - Record category from A.5.32-33.2 inventory
   - Retention period (years/months)
   - Retention basis (regulatory, contractual, business)
   - Retention trigger (creation, last activity, contract end)
   - Review cycle


**Deliverable:** Complete Sheet 2 (Retention Schedule)

### Phase 3: Regulatory Mapping (2-4 hours)

**Objective:** Document regulatory drivers for retention

**Steps:**
1. **For EACH Applicable Regulation:**

   - Regulation name and section
   - Record types affected
   - Retention period required
   - Penalties for non-compliance
   - Last review date


2. **Complete Sheet 3 (Regulatory Mapping):**

   - Comprehensive regulatory reference
   - Cross-reference to retention schedule


**Deliverable:** Complete Sheet 3 (Regulatory Mapping)

### Phase 4: Disposal Queue (2-3 hours)

**Objective:** Identify records ready for disposal

**Steps:**
1. **Review Records Inventory:**

   - Identify records past retention period
   - Identify records approaching retention end
   - Check for legal holds affecting disposal


2. **Complete Sheet 4 (Disposal Queue):**

   - Record category
   - Retention end date
   - Volume (physical/electronic)
   - Legal hold status
   - Disposal priority
   - Target disposal date


**Deliverable:** Complete Sheet 4 (Disposal Queue)

### Phase 5: Define Disposal Methods (2-3 hours)

**Objective:** Establish appropriate disposal methods

**Steps:**
1. **Per Classification Level:**

   | Classification | Physical Disposal | Electronic Disposal |
   |----------------|-------------------|---------------------|
   | Restricted | Cross-cut shredding P-5, witnessed incineration | NIST 800-88 Clear/Purge, cryptographic erasure |
   | Confidential | Cross-cut shredding P-4 | NIST 800-88 Clear, secure deletion |
   | Internal | Standard shredding P-3 | Standard deletion with verification |
   | Public | Recycling | Standard deletion |


2. **Complete Sheet 5 (Disposal Method Matrix):**

   - Classification level
   - Physical media method
   - Electronic media method
   - Required verification
   - Approved vendors


**Deliverable:** Complete Sheet 5 (Disposal Method Matrix)

### Phase 6: Destruction Verification (2-4 hours)

**Objective:** Document destruction evidence

**Steps:**
1. **Gather Destruction Records:**

   - Certificates of destruction from vendors
   - Internal disposal logs
   - Witness statements for sensitive destruction
   - Media destruction reports


2. **Complete Sheet 6 (Destruction Verification):**

   - Destruction event ID
   - Record category destroyed
   - Volume
   - Destruction date
   - Method used
   - Performed by
   - Certificate reference
   - Verification status


**Deliverable:** Complete Sheet 6 (Destruction Verification)

### Phase 7: Exception Management (1-2 hours)

**Objective:** Document retention exceptions

**Steps:**
1. **Retention Extensions:**

   - Legal holds (litigation, investigation)
   - Business-critical extensions
   - Regulatory examination periods


2. **Early Disposal:**

   - Business need (approved)
   - Risk-based disposal (approved)
   - Data subject erasure requests


3. **Complete Sheet 7 (Exception Register):**

   - Exception ID
   - Type (extension/early disposal)
   - Record category affected
   - Reason
   - Approval (who, when)
   - New retention period
   - Status


**Deliverable:** Complete Sheet 7 (Exception Register)

### Phase 8: Compliance Monitoring (1-2 hours)

**Objective:** Assess schedule adherence

**Steps:**
1. **Calculate Compliance Metrics:**

   - Records disposed on schedule (%)
   - Overdue disposals (count, age)
   - Records retained past maximum
   - Exception rate


2. **Complete Sheet 8 (Compliance Dashboard):**

   - Metric name
   - Target
   - Current value
   - Trend
   - Status


**Deliverable:** Complete Sheet 8 (Compliance Dashboard)

### Phase 9: Gap Analysis (1-2 hours)

**Objective:** Identify issues requiring remediation

**Steps:**
1. **Review All Sheets for Issues:**

   - Undefined retention periods
   - Overdue disposals
   - Missing destruction certificates
   - Non-compliant disposal methods
   - Unapproved exceptions


2. **Complete Sheet 9 (Gap Analysis):**

   - Gap description
   - Risk rating
   - Remediation action
   - Owner and due date


**Deliverable:** Complete Sheet 9 (Gap Analysis)

### Phase 10: Evidence Collection (1 hour)

**Complete Sheet 10 (Evidence Register)**

### Phase 11: Review & Approval (1-2 hours)

**Complete Sheet 11 (Approval & Sign-Off)**


---

# Sheet-by-Sheet Completion Guidance

## Sheet 2: Retention Schedule

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Record Category ID | Reference to A.5.32-33.2 | REC-001 |
| Category Name | Descriptive name | Financial Ledgers |
| Retention Period | Years/months | 10 years |
| Retention Basis | Regulatory/Contractual/Business | Regulatory - Swiss CO 958f |
| Retention Trigger | When period starts | Year-end close |
| Grace Period | Time after retention before disposal | 90 days |
| Review Cycle | How often reviewed | Annual |
| Last Review | Date of last review | 2025-12-15 |
| Next Review | Date of next review | 2026-12-15 |
| Notes | Additional information | Includes all sub-ledgers |


## Sheet 3: Regulatory Mapping

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Regulation ID | Unique identifier | REG-001 |
| Regulation Name | Full name | Swiss Code of Obligations |
| Section/Article | Specific reference | Art. 958f |
| Record Types Affected | What records | Bookkeeping, financial |
| Required Retention | Period required | 10 years |
| Retention Trigger | When period starts | Fiscal year end |
| Penalty for Non-Compliance | Consequences | Administrative fines, audit findings |
| Last Review | When last verified | 2025-11-01 |
| Notes | Additional context | 10 years from end of fiscal year |


## Sheet 4: Disposal Queue

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Queue ID | Unique identifier | DQ-001 |
| Record Category | Category name | 2014 Financial Records |
| Retention End Date | When retention expires | 2025-12-31 |
| Volume - Physical | Boxes/files | 15 boxes |
| Volume - Electronic | GB/records | 250 GB |
| Legal Hold Status | Yes/No | No |
| Disposal Priority | High/Medium/Low | High |
| Target Disposal Date | Planned disposal | 2026-03-31 |
| Assigned To | Responsible person | Records Manager |
| Status | Pending/In Progress/Complete | Pending |


## Sheet 5: Disposal Method Matrix

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Classification | Restricted/Confidential/Internal/Public | Confidential |
| Physical - Paper | Destruction method | Cross-cut shredding P-4 |
| Physical - Media | HDDs, tapes, etc. | Degaussing + physical destruction |
| Electronic - On-Prem | Servers, storage | NIST 800-88 Clear |
| Electronic - Cloud | Cloud storage | Provider secure deletion + verification |
| Verification Required | What proof needed | Certificate of destruction |
| Approved Vendors | Who can perform | SecureShred AG, IT Internal |
| Special Handling | Additional requirements | Witnessed for Restricted |


## Sheet 6: Destruction Verification

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Destruction ID | Unique identifier | DEST-2026-001 |
| Record Category | What was destroyed | 2014 Financial Records |
| Volume | Amount destroyed | 15 boxes, 250 GB |
| Destruction Date | When destroyed | 2026-03-15 |
| Method Used | How destroyed | Cross-cut shredding, secure deletion |
| Performed By | Who performed | SecureShred AG, IT Operations |
| Witness (if required) | Who witnessed | Records Manager |
| Certificate Reference | Document ID | CERT-SS-2026-0342 |
| Storage Location | Where certificate stored | SharePoint/ISMS/Destruction |
| Verification Status | Verified/Pending | Verified |


## Sheet 7: Exception Register

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Exception ID | Unique identifier | EXC-2026-001 |
| Exception Type | Extension/Early Disposal | Extension |
| Record Category | Affected records | Contract XYZ Files |
| Original Retention | What retention was | 7 years |
| New Retention | What retention is now | Indefinite (legal hold) |
| Reason | Why exception needed | Active litigation - Case 2025-LIT-042 |
| Requested By | Who requested | Legal Counsel |
| Approved By | Who approved | Legal Counsel |
| Approval Date | When approved | 2026-01-15 |
| Expiration | When exception ends | Until case resolution |
| Status | Active/Expired/Cancelled | Active |


## Sheet 8: Compliance Dashboard

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Metric ID | Unique identifier | MET-001 |
| Metric Name | Descriptive name | On-Schedule Disposal Rate |
| Description | What it measures | % of records disposed within grace period |
| Target | Goal value | 95% |
| Current Value | Actual value | 87% |
| Trend | Improving/Stable/Declining | Improving |
| Status | On Target/At Risk/Below Target | At Risk |
| Owner | Responsible person | Records Manager |
| Last Updated | When calculated | 2026-02-01 |


---

# Evidence Collection

## Required Evidence

**Retention Schedule:**
- Regulatory requirement documentation
- Contract extracts with retention clauses
- Business justification documentation


**Disposal:**
- Certificates of destruction
- Vendor contracts and certifications
- Internal disposal logs
- Witness statements (for sensitive records)


**Compliance:**
- Disposal tracking reports
- Exception approval documentation
- Legal hold notices


## Evidence Storage

Store all evidence in:
- **Primary Location:** ISMS Evidence Library
- **Folder Structure:** `/ISMS/A.5.32-33/Retention-Disposal/[Assessment-Date]/`

---

# Common Pitfalls

**MISTAKE: Setting arbitrary retention periods**
- Always base retention on regulatory, contractual, or documented business need
- "Forever" is not a valid retention period

**MISTAKE: Ignoring storage limitation principles**
- GDPR requires data not be kept longer than necessary
- Over-retention creates risk and cost

**MISTAKE: Not checking for legal holds before disposal**
- Always verify no holds exist
- Destroying held records is serious violation

**MISTAKE: Using inadequate disposal methods**
- Match disposal method to classification
- "Delete" does not equal "destroy" for electronic records

**MISTAKE: Not obtaining destruction certificates**
- Third-party destruction requires certification
- Internal destruction requires logging

**MISTAKE: Forgetting backups**
- Backups contain records too
- Disposal must include backup copies

**MISTAKE: Not reviewing regulatory changes**
- Retention requirements can change
- Annual regulatory review is essential

**MISTAKE: Applying retention to records, not categories**
- Manage by category, not individual records
- Exceptions handled separately

**MISTAKE: Not coordinating with IT on electronic disposal**
- IT must execute electronic destruction
- Verify methods and capabilities

**MISTAKE: Assuming cloud deletion is sufficient**
- Cloud providers have different deletion methods
- Verify provider destruction capabilities

---

# Quality Checklist

**Retention Schedule (Sheet 2):**
- [ ] All record categories from A.5.32-33.2 included
- [ ] Retention periods documented with basis
- [ ] Retention triggers defined
- [ ] Review cycle established

**Regulatory Mapping (Sheet 3):**
- [ ] All applicable regulations identified
- [ ] Retention requirements verified current
- [ ] Penalties documented

**Disposal Queue (Sheet 4):**
- [ ] Records past retention identified
- [ ] Legal holds verified
- [ ] Disposal priority assigned

**Disposal Methods (Sheet 5):**
- [ ] Methods appropriate for classification
- [ ] Vendors approved and documented
- [ ] Verification requirements defined

**Destruction Verification (Sheet 6):**
- [ ] Certificates collected
- [ ] Evidence properly stored
- [ ] Verification complete

**Exceptions (Sheet 7):**
- [ ] All exceptions documented
- [ ] Approvals recorded
- [ ] Status current

**Compliance (Sheet 8):**
- [ ] Metrics calculated
- [ ] Targets defined
- [ ] Issues identified

---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook Developers, Python/Excel Script Maintainers

---

# Workbook Structure

## Generated File

**Filename:** `ISMS-IMP-A.5.32-33.3_Retention_Disposal_Schedule_[YYYYMMDD].xlsx`

**Generator Script:** `generate_a532_33_3_retention_disposal.py`

## Sheet Overview

| Sheet # | Sheet Name | Purpose | Rows (Est.) |
|---------|------------|---------|-------------|
| 1 | Instructions | Usage guidance | ~50 |
| 2 | Retention_Schedule | Retention periods | 50+ |
| 3 | Regulatory_Mapping | Regulation reference | 30+ |
| 4 | Disposal_Queue | Records for disposal | 50+ |
| 5 | Disposal_Method_Matrix | Methods per classification | ~10 |
| 6 | Destruction_Verification | Destruction evidence | 100+ |
| 7 | Exception_Register | Extensions/early disposal | 30+ |
| 8 | Compliance_Dashboard | Metrics | ~20 |
| 9 | Gap_Analysis | Issues | 30+ |
| 10 | Evidence_Register | Audit evidence | 50+ |
| 11 | Approval_SignOff | Formal approval | ~30 |

---

# Sheet-by-Sheet Specifications

## Sheet 2: Retention_Schedule

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Record Category ID | 18 | - |
| B | Category Name | 30 | - |
| C | Retention Period | 15 | - |
| D | Retention Basis | 20 | List: Regulatory, Contractual, Business, Mixed |
| E | Basis Detail | 35 | - |
| F | Retention Trigger | 20 | List: Creation, Year-End, Contract End, Last Activity, Event-Based |
| G | Grace Period | 12 | - |
| H | Review Cycle | 12 | List: Annual, Biennial, Triennial |
| I | Last Review | 12 | Date |
| J | Next Review | 12 | Date |
| K | Notes | 35 | - |


## Sheet 3: Regulatory_Mapping

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Regulation ID | 12 | - |
| B | Regulation Name | 30 | - |
| C | Section/Article | 15 | - |
| D | Record Types Affected | 35 | - |
| E | Required Retention | 15 | - |
| F | Retention Trigger | 20 | - |
| G | Penalty for Non-Compliance | 30 | - |
| H | Last Review | 12 | Date |
| I | Reviewer | 20 | - |
| J | Notes | 35 | - |


## Sheet 4: Disposal_Queue

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Queue ID | 12 | - |
| B | Record Category | 30 | - |
| C | Retention End Date | 15 | Date |
| D | Volume - Physical | 15 | - |
| E | Volume - Electronic | 15 | - |
| F | Legal Hold Status | 12 | List: Yes, No, Checking |
| G | Disposal Priority | 12 | List: High, Medium, Low |
| H | Target Disposal Date | 15 | Date |
| I | Assigned To | 20 | - |
| J | Status | 15 | List: Pending, In Progress, Complete, On Hold |
| K | Notes | 30 | - |


## Sheet 5: Disposal_Method_Matrix

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Classification | 15 | List: Restricted, Confidential, Internal, Public |
| B | Physical - Paper | 25 | - |
| C | Physical - Media | 25 | - |
| D | Electronic - On-Prem | 25 | - |
| E | Electronic - Cloud | 25 | - |
| F | Verification Required | 20 | - |
| G | Approved Vendors | 25 | - |
| H | Special Handling | 25 | - |


## Sheet 6: Destruction_Verification

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Destruction ID | 18 | - |
| B | Record Category | 25 | - |
| C | Volume | 15 | - |
| D | Destruction Date | 15 | Date |
| E | Method Used | 25 | - |
| F | Performed By | 20 | - |
| G | Witness | 20 | - |
| H | Certificate Reference | 20 | - |
| I | Storage Location | 30 | - |
| J | Verification Status | 15 | List: Verified, Pending, Not Verified |


## Sheet 7: Exception_Register

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Exception ID | 15 | - |
| B | Exception Type | 15 | List: Extension, Early Disposal |
| C | Record Category | 25 | - |
| D | Original Retention | 15 | - |
| E | New Retention | 15 | - |
| F | Reason | 35 | - |
| G | Requested By | 20 | - |
| H | Approved By | 20 | - |
| I | Approval Date | 12 | Date |
| J | Expiration | 15 | - |
| K | Status | 12 | List: Active, Expired, Cancelled |


## Sheet 8: Compliance_Dashboard

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Metric ID | 10 | - |
| B | Metric Name | 25 | - |
| C | Description | 40 | - |
| D | Target | 12 | - |
| E | Current Value | 12 | - |
| F | Trend | 12 | List: Improving, Stable, Declining, New |
| G | Status | 15 | List: On Target, At Risk, Below Target |
| H | Owner | 20 | - |
| I | Last Updated | 12 | Date |


## Sheet 9: Gap_Analysis

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Gap ID | 10 | - |
| B | Gap Category | 18 | List: Retention, Disposal, Verification, Process |
| C | Description | 45 | - |
| D | Related Item | 20 | - |
| E | Risk Rating | 12 | List: High, Medium, Low |
| F | Remediation Action | 40 | - |
| G | Owner | 20 | - |
| H | Due Date | 12 | Date |
| I | Status | 15 | List: Open, In Progress, Complete |


## Sheet 10: Evidence_Register

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Evidence ID | 12 | - |
| B | Description | 40 | - |
| C | Evidence Type | 18 | List: Certificate, Log, Approval, Report, Other |
| D | Related Item | 20 | - |
| E | Storage Location | 35 | - |
| F | Collected Date | 12 | Date |
| G | Collected By | 20 | - |
| H | Verification Status | 18 | List: Verified, Pending, Expired |


## Sheet 11: Approval_SignOff

### Approver Roles
1. Records Manager
2. Legal Counsel
3. Chief Information Security Officer
4. IT Operations Manager
5. Compliance Officer

---

# Cell Styling Reference

## Colour Palette

| Style Name | Hex Code | Usage |
|------------|----------|-------|
| Header Fill | #1F4E79 | Sheet headers |
| Subheader Fill | #2E75B6 | Secondary headers |
| Column Header | #D6DCE4 | Table headers |
| Input Cell | #FFFFCC | User input cells |
| High Priority | #FF6B6B | Overdue/high risk |
| Medium Priority | #FFA94D | Approaching deadline |
| Low Priority | #69DB7C | On track |
| Compliant | #C6EFCE | Compliant status |
| Warning | #FFEB9C | Attention needed |
| Non-Compliant | #FFC7CE | Non-compliant |

---

# Integration Points

## Related Workbooks

| Workbook | Integration Type | Data Exchange |
|----------|-----------------|---------------|
| ISMS-IMP-A.5.32-33.2 | Record categories | Uses protection classification |
| ISMS-IMP-A.5.32-33.4 | Dashboard | Retention metrics feed dashboard |
| ISMS-IMP-A.8.10 | Secure deletion | Deletion methods alignment |

---

**END OF SPECIFICATION**

---

*"The cost of storage is not just dollars - it is also risk."*
-- Anonymous Records Manager

<!-- QA_VERIFIED: 2026-02-03 -->
