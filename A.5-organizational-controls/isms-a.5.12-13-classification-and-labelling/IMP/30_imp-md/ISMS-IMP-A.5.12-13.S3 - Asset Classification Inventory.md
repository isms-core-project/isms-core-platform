# ISMS-IMP-A.5.12-13.S3 - Asset Classification Inventory

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.12-13.S3 |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.12-13 Classification and Labelling |
| **Parent Policy** | ISMS-POL-A.5.12-13 - Information Classification and Labelling |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Workbook Structure](#14-workbook-structure)
   - [1.5 Completion Walkthrough](#15-completion-walkthrough)
   - [1.6 Evidence Collection](#16-evidence-collection)
   - [1.7 Common Pitfalls](#17-common-pitfalls)
   - [1.8 Quality Checklist](#18-quality-checklist)
   - [1.9 Review and Approval](#19-review-and-approval)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Technical Details](#21-workbook-technical-details)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Conditional Formatting](#23-conditional-formatting)
   - [2.4 Integration Points](#24-integration-points)
   - [2.5 Related Documents](#25-related-documents)

---

# PART I: USER COMPLETION GUIDE

---

## 1.1 Assessment Overview

### Purpose

This workbook maintains an inventory of all classified information assets, ensuring complete coverage of the classification scheme and enabling compliance tracking and reporting.

The assessment serves multiple purposes:
- **Inventory**: Maintain complete catalogue of information assets with classification
- **Track Coverage**: Measure classification implementation across the organisation
- **Identify Gaps**: Find unclassified or improperly classified assets
- **Monitor Changes**: Log reclassification events with justification
- **Support Audit**: Provide evidence of classification implementation

### Scope

The Asset Classification Inventory covers:

| Inventory Domain | Coverage | Key Metrics |
|------------------|----------|-------------|
| **Asset Catalogue** | All information assets | Total count, classification distribution |
| **Classification Status** | Assignment tracking | % classified, % labelled |
| **Ownership** | Custodian assignments | Owner coverage |
| **Reclassification** | Change tracking | Upgrade/downgrade counts |
| **Gap Analysis** | Non-compliance items | Unclassified assets, labelling gaps |

**Inclusions:**
- Digital documents (files, databases, applications)
- Physical documents and records
- Data repositories and storage systems
- Information systems and applications
- Communication channels and email repositories

**Exclusions:**
- Transient operational data (covered by system classification)
- Automatically generated logs (classified at system level)
- Backup copies (inherit source classification)

### Business Value

| Value Area | Benefit |
|------------|---------|
| **Visibility** | Know what classified information exists and where |
| **Compliance** | Track classification coverage for audit |
| **Risk Management** | Identify unprotected sensitive assets |
| **Governance** | Enable accountability through ownership |
| **Trend Analysis** | Monitor classification changes over time |

### Assessment Frequency

| Assessment Type | Frequency | Trigger Events |
|-----------------|-----------|----------------|
| Full Inventory Review | Annual | Certification audit, M&A activity |
| Classification Verification | Quarterly | Policy changes, audit findings |
| New Asset Classification | Per deployment | System onboarding, data acquisition |
| Reclassification Review | Quarterly | Business changes, regulatory updates |

---

## 1.2 Control Requirements

### ISO 27001:2022 Controls A.5.12 & A.5.13

Per ISO/IEC 27001:2022:

**Control A.5.12:**
> *"Information should be classified according to the information security needs of the organization based on confidentiality, integrity, availability and relevant interested party requirements."*

**Control A.5.13:**
> *"An appropriate set of procedures for information labelling should be developed and implemented in accordance with the information classification scheme adopted by the organization."*

**Control Type:** Preventive
**Security Properties:** Confidentiality, Integrity, Availability
**Cybersecurity Concepts:** Identify, Protect
**Operational Capabilities:** Asset Management, Information Protection

### Key Control Objectives

| Objective | Description |
|-----------|-------------|
| **Complete Coverage** | All information assets have assigned classification |
| **Owner Assignment** | Every asset has accountable information owner |
| **Labelling Compliance** | Classified assets are appropriately labelled |
| **Current Classification** | Classifications reviewed and updated as needed |
| **Change Control** | Reclassifications documented and approved |

### What Auditors Look For

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Asset Coverage** | Inventory showing all information assets |
| **Classification Assignments** | Evidence of classification decisions |
| **Owner Accountability** | Named owners for each asset |
| **Labelling Status** | Evidence of labels applied |
| **Review Currency** | Recent review dates on classifications |
| **Reclassification Records** | Documentation of classification changes |

---

## 1.3 Prerequisites

### Required Access

| System | Purpose | Access Level Needed |
|--------|---------|---------------------|
| Asset Inventory (A.5.9) | Asset list source | Read access |
| Document Management | Document metadata | Read access |
| File Servers | File classification status | Read access |
| Application Inventory | System classification | Read access |

### Required Documents

- [ ] ISMS-IMP-A.5.9 - Asset Inventory (completed)
- [ ] ISMS-IMP-A.5.12-13.S1 - Classification Scheme Definition (completed)
- [ ] ISMS-IMP-A.5.12-13.S2 - Labelling Procedures (completed)
- [ ] Prior classification inventory (if applicable)
- [ ] Data discovery scan results (if available)

### Required Personnel

| Role | Responsibility | Time Commitment |
|------|----------------|-----------------|
| **Assessment Lead** | Coordinate inventory compilation | 12-16 hours |
| **Information Owners** | Confirm asset classification | 2-4 hours each |
| **IT Operations** | Provide system-level classification | 4-6 hours |
| **Data Governance** | Validate inventory completeness | 4-6 hours |
| **Internal Audit** | Independent validation | 4 hours |

---

## 1.4 Workbook Structure

### Sheet Overview

| Sheet | Purpose | Assessor Action |
|-------|---------|-----------------|
| **Instructions** | Guidance and methodology | Read before starting |
| **Asset_Inventory** | Master list of classified assets | Populate all assets |
| **Classification_Summary** | Statistics by level and type | Review aggregates |
| **Reclassification_Log** | Track classification changes | Log all changes |
| **Gap_Analysis** | Items requiring attention | Address gaps |
| **Evidence_Register** | Audit evidence tracking | Document evidence |
| **Approval_SignOff** | Inventory authorisation | Obtain signatures |

### Data Flow

```
Asset Inventory (A.5.9)
        │
        ▼
Asset_Inventory ────────────► Classification_Summary
        │                              │
        │                              ▼
        │                    Gap_Analysis
        │                              │
        ├──────────────────────────────┤
        │                              │
        ▼                              ▼
Reclassification_Log          Evidence_Register
        │                              │
        └──────────────────────────────┤
                                       ▼
                              Approval_SignOff
```

---

## 1.5 Completion Walkthrough

### Step 1: Populate Asset Inventory

**Time allocation:** 4-6 hours

**Purpose:** Create comprehensive list of information assets with classification details.

**Fields to Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| Asset_ID | Unique identifier | AST-001 |
| Asset_Name | Descriptive name | Customer Database |
| Asset_Type | Category | Database |
| Description | What the asset contains | Production customer records including PII |
| Classification | Assigned level | RESTRICTED |
| Owner | Accountable person/role | CRM Manager |
| Custodian | Day-to-day responsibility | DBA Team |
| Location_System | Where asset resides | SQL Server Prod |
| Labelling_Status | Label application status | Labelled |
| Last_Review | When classification last reviewed | 2026-01-15 |
| Next_Review | When classification due for review | 2026-07-15 |
| Regulatory_Req | Applicable regulations | GDPR, nDSG |
| Notes | Additional information | Contains 50,000 customer records |

**Data Sources:**
- Asset inventory (ISMS-IMP-A.5.9)
- Application portfolio
- Data catalogue/discovery tools
- Department inventories
- Records management register

**Worked Example - Asset Inventory:**

| Asset_ID | Asset_Name | Asset_Type | Classification | Owner | Labelling_Status |
|----------|------------|------------|----------------|-------|------------------|
| AST-001 | Customer Database | Database | RESTRICTED | CRM Manager | Labelled |
| AST-002 | Financial Reports | Document Set | CONFIDENTIAL | CFO | Labelled |
| AST-003 | Employee Handbook | Document | INTERNAL | HR Director | Labelled |
| AST-004 | Marketing Materials | Document Set | PUBLIC | Marketing Lead | Labelled |
| AST-005 | Security Configs | Configuration | RESTRICTED | CISO | Labelled |

### Step 2: Review Classification Summary

**Time allocation:** 2-3 hours

**Purpose:** Analyse classification distribution and identify coverage gaps.

**Summary Metrics to Review:**

| Metric | Target | What to Check |
|--------|--------|---------------|
| Total Assets | N/A | Matches A.5.9 inventory |
| % Classified | 100% | All assets have classification |
| % RESTRICTED | Variable | Appropriate for data types |
| % CONFIDENTIAL | Variable | Bulk of sensitive business data |
| % INTERNAL | Variable | Operational documentation |
| % PUBLIC | Variable | Approved external content |
| % Labelled | 100% (CONF+REST) | Labels applied per policy |
| % Current Review | 100% | Classifications reviewed within policy period |

**By Asset Type Analysis:**

| Asset Type | Total | RESTRICTED | CONFIDENTIAL | INTERNAL | PUBLIC |
|------------|-------|------------|--------------|----------|--------|
| Database | | | | | |
| Document | | | | | |
| Document Set | | | | | |
| Application | | | | | |
| System | | | | | |
| Repository | | | | | |
| Email | | | | | |
| Media | | | | | |
| Other | | | | | |

**By Department Analysis:**

| Department | Total Assets | Compliance % | RESTRICTED Count |
|------------|--------------|--------------|------------------|
| Finance | | | |
| HR | | | |
| IT | | | |
| Sales | | | |
| Marketing | | | |
| Operations | | | |
| Legal | | | |

### Step 3: Log Reclassifications

**Time allocation:** 1-2 hours

**Purpose:** Document any classification changes during the assessment period.

**Reclassification Record Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Change_ID | Unique identifier | CHG-CL-2026-001 |
| Asset_ID | Asset being reclassified | AST-002 |
| Asset_Name | Asset name | Financial Reports |
| Previous_Class | Former classification | CONFIDENTIAL |
| New_Class | Updated classification | RESTRICTED |
| Reason_for_Change | Justification | Regulatory requirement - FINMA data |
| Requested_By | Who requested change | CFO |
| Approved_By | Who approved change | CISO |
| Change_Date | When changed | 2026-02-01 |
| Status | Change status | Complete |

**Valid Reclassification Reasons:**
- Value change (information became more/less sensitive)
- Regulatory requirement (new regulation applies)
- Business need (protection requirements changed)
- Data lifecycle (information aged/declassified)
- Merger/divestiture (ownership changed)
- Error correction (original classification incorrect)
- Periodic review (scheduled reassessment)

### Step 4: Identify and Address Gaps

**Time allocation:** 3-4 hours

**Purpose:** Find assets requiring classification attention and plan remediation.

**Gap Types to Identify:**

| Gap Type | Description | Example |
|----------|-------------|---------|
| Unclassified Assets | Assets with no classification assigned | Legacy file server contents |
| Incomplete Labelling | Classified but not labelled | Historical emails |
| Misclassification | Classification appears incorrect | Personal data marked INTERNAL |
| No Labelling Capability | System cannot apply labels | Third-party SaaS |
| Inconsistent Labels | Different labels same classification | Mixed label formats |
| Missing Metadata | Visual label but no metadata | PDF without properties |

**Gap Record Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Gap_ID | Unique identifier | GAP-001 |
| Asset_Area | Affected asset or area | Legacy File Server |
| Gap_Type | Type of gap | Unclassified Assets |
| Description | Detailed description | File server contains unclassified documents from pre-policy era |
| Risk_Level | Impact rating | High |
| Remediation_Action | Planned fix | Conduct classification sweep of all files |
| Owner | Responsible person | IT Manager |
| Due_Date | Deadline | 2026-03-31 |
| Status | Current state | Open, In Progress, Resolved |

**Remediation Priority:**

| Risk Level | SLA | Escalation |
|------------|-----|------------|
| Critical | 7 days | CISO, Executive |
| High | 30 days | CISO |
| Medium | 60 days | IT Security Manager |
| Low | 90 days | Security Team |

### Step 5: Document Evidence

**Time allocation:** 1-2 hours

**Purpose:** Track evidence supporting asset classification.

**Evidence Types:**

| Evidence Type | Description | Example |
|---------------|-------------|---------|
| Inventory export | Asset inventory snapshot | Asset inventory spreadsheet |
| Classification report | Classification distribution | MIP classification report |
| Label screenshot | Example of labelled asset | Sample labelled document |
| Audit finding | Previous audit observations | Internal audit report |
| Training record | Owner training completion | LMS certificate |
| Policy acknowledgment | Owner signed policy | Acknowledgment form |

### Step 6: Obtain Approvals

**Time allocation:** 1-2 hours

**Purpose:** Secure formal approval for the classification inventory.

**Required Approvals:**

| Approver | What They Approve | Criteria |
|----------|-------------------|----------|
| **CISO** | Security adequacy | Inventory supports protection |
| **Data Governance Lead** | Inventory completeness | All data assets covered |
| **IT Asset Manager** | System coverage | All systems included |
| **Compliance Officer** | Regulatory alignment | Regulatory data identified |

---

## 1.6 Evidence Collection

### Evidence Requirements

| Evidence Type | Source | Retention |
|---------------|--------|-----------|
| This assessment workbook | Generated | 7 years |
| Asset inventory exports | Systems | 3 years |
| Classification reports | Tools | 3 years |
| Reclassification approvals | Email/workflow | Duration + 2 years |
| Gap remediation evidence | Change tickets | 3 years |
| Approval signatures | This workbook | Duration + 2 years |

### Evidence Storage

**Primary Location:** `[SharePoint/Evidence Library]/A.5.12-13/Asset-Inventory/[Year]/`

**Folder Structure:**
```
A.5.12-13/
|-- Asset-Inventory/
|   |-- 2026/
|   |   |-- Assessment-Workbooks/
|   |   |   |-- ISMS-IMP-A.5.12-13.S3_Asset_Classification_Inventory_20260204.xlsx
|   |   |-- Evidence/
|   |   |   |-- Inventory-Exports/
|   |   |   |-- Classification-Reports/
|   |   |   |-- Reclassification-Approvals/
|   |   |   |-- Gap-Remediation/
|   |   |   |-- Approvals/
```

---

## 1.7 Common Pitfalls

Avoid these common mistakes when completing the asset classification inventory:

### Inventory Completeness Pitfalls

❌ **MISTAKE**: Only including formal "documents" - missing databases, applications, media
✅ **CORRECT**: Include all information assets: documents, databases, applications, systems, repositories, media

❌ **MISTAKE**: Excluding cloud and SaaS applications from inventory
✅ **CORRECT**: Include all cloud resources where organisation data resides

❌ **MISTAKE**: Counting backups separately (inflating inventory)
✅ **CORRECT**: Backups inherit source classification; count primary copies only

❌ **MISTAKE**: Missing shared drives, departmental repositories, personal OneDrive
✅ **CORRECT**: Conduct data discovery across all storage locations

### Classification Assignment Pitfalls

❌ **MISTAKE**: Defaulting everything to CONFIDENTIAL to "be safe"
✅ **CORRECT**: Apply appropriate classification based on actual content and impact

❌ **MISTAKE**: Single classification for entire system (e.g., "SharePoint is CONFIDENTIAL")
✅ **CORRECT**: Classify at appropriate granularity - site, library, folder, or document level

❌ **MISTAKE**: Not considering aggregation (many INTERNAL items = CONFIDENTIAL together)
✅ **CORRECT**: Consider whether aggregated access creates higher sensitivity

❌ **MISTAKE**: Classification owner different from information owner
✅ **CORRECT**: Information owner determines and maintains classification

### Labelling Status Pitfalls

❌ **MISTAKE**: Marking "Labelled" without verification
✅ **CORRECT**: Verify labels actually applied (check document properties, visible markers)

❌ **MISTAKE**: Assuming automated labelling worked without validation
✅ **CORRECT**: Sample check that auto-labelling rules applied correctly

❌ **MISTAKE**: Ignoring labelling exceptions
✅ **CORRECT**: Document systems unable to label with compensating controls

### Review and Currency Pitfalls

❌ **MISTAKE**: Setting review dates far in future (5+ years)
✅ **CORRECT**: Review annually minimum; more frequently for RESTRICTED

❌ **MISTAKE**: Backdating review dates without actual review
✅ **CORRECT**: Review means actual reassessment, not just date update

---

## 1.8 Quality Checklist

Before submitting the assessment, verify:

### Inventory Completeness Checks

- [ ] All asset types represented (documents, databases, applications, systems, media)
- [ ] Cloud and SaaS assets included
- [ ] All departments covered
- [ ] Count reconciles with A.5.9 asset inventory
- [ ] No obvious gaps in coverage

### Classification Accuracy Checks

- [ ] Every asset has classification assigned
- [ ] Classifications appropriate for content
- [ ] Regulatory data correctly identified (GDPR, nDSG)
- [ ] RESTRICTED used sparingly for truly sensitive data
- [ ] Aggregation effects considered

### Labelling Status Checks

- [ ] CONFIDENTIAL and RESTRICTED assets labelled
- [ ] Labelling verified (not just assumed)
- [ ] Labelling exceptions documented with compensating controls
- [ ] Labelling coverage metric calculated

### Ownership Checks

- [ ] Every asset has named owner
- [ ] Owners are appropriate (business, not IT for business data)
- [ ] Custodians identified where different from owner
- [ ] Contact information current

### Gap Remediation Checks

- [ ] All gaps identified have remediation plans
- [ ] Remediation owners assigned
- [ ] Due dates realistic but timely
- [ ] High/Critical gaps escalated appropriately

---

## 1.9 Review and Approval

### Review Workflow

```
Assessment Lead Compiles Inventory
        │
        ▼
Information Owners Validate (Sample)
        │
        ▼
Data Governance Review (Completeness)
        │
        ▼
IT Review (System Coverage)
        │
        ▼
Internal Audit Validation
        │
        ▼
CISO Approval
        │
        ▼
Inventory Approved
```

### Approval Signatures

The Approval_SignOff sheet requires:

1. **Assessment Lead Certification:**
   - Confirms methodology was followed
   - Confirms all asset types covered
   - Date and signature

2. **Data Governance Validation:**
   - Confirms inventory complete
   - Confirms classification appropriate
   - Date and signature

3. **IT Asset Manager Validation:**
   - Confirms system coverage
   - Confirms technical accuracy
   - Date and signature

4. **CISO Approval:**
   - Approves overall inventory
   - Accepts gap remediation plans
   - Date and signature

---

# PART II: TECHNICAL SPECIFICATION

---

## 2.1 Workbook Technical Details

### File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.12-13.S3_Asset_Classification_Inventory_YYYYMMDD.xlsx` |
| Generator | `generate_a512_13_3_asset_classification_inventory.py` |
| Sheets | 7 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 40 | 8 |
| 2 | Asset_Inventory | Master asset list | 500+ | 13 |
| 3 | Classification_Summary | Statistics | 40 | 7 |
| 4 | Reclassification_Log | Change tracking | 50+ | 10 |
| 5 | Gap_Analysis | Non-compliance items | 50+ | 9 |
| 6 | Evidence_Register | Audit evidence | 30 | 8 |
| 7 | Approval_SignOff | Authorisation | 20 | 6 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

| Row | Content | Purpose |
|-----|---------|---------|
| 1 | Title (merged A1:H1) | Document identification |
| 3-10 | Purpose and scope | Methodology guidance |
| 12-20 | Classification ownership | Responsibility guidance |
| 22-30 | How to use instructions | Step-by-step guidance |
| 32-40 | Review cycle guidance | Timing expectations |

### Sheet 2: Asset_Inventory

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Asset_ID | 12 | Text | Required |
| B | Asset_Name | 25 | Text | Required |
| C | Asset_Type | 15 | List | Database, Document, Document Set, Application, System, Repository, Email, Media, Other |
| D | Description | 30 | Text | None |
| E | Classification | 15 | List | RESTRICTED, CONFIDENTIAL, INTERNAL, PUBLIC |
| F | Owner | 18 | Text | Required |
| G | Custodian | 15 | Text | None |
| H | Location_System | 20 | Text | None |
| I | Labelling_Status | 15 | List | Labelled, Partial, Not Labelled, N/A |
| J | Last_Review | 12 | Date | None |
| K | Next_Review | 12 | Date | None |
| L | Regulatory_Req | 15 | Text | None |
| M | Notes | 25 | Text | None |

### Sheet 3: Classification_Summary

| Column | Header | Width | Type | Content |
|:------:|--------|:-----:|------|---------|
| A | Classification | 20 | Text | Pre-populated levels |
| B | Count | 12 | Number | Formula/Input |
| C | Percentage | 12 | Percent | Formula |
| D | Labelled | 12 | Number | Formula/Input |
| E | Unlabelled | 12 | Number | Formula/Input |
| F | Compliance_% | 12 | Percent | Formula |

**Sections:**
- Assets by Classification Level (rows 5-11)
- Assets by Type (rows 15-26)
- Assets by Department (rows 29-40)

### Sheet 4: Reclassification_Log

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Change_ID | 12 | Text | None |
| B | Asset_ID | 12 | Text | From Asset_Inventory |
| C | Asset_Name | 25 | Text | Auto-populated |
| D | Previous_Class | 15 | List | RESTRICTED, CONFIDENTIAL, INTERNAL, PUBLIC |
| E | New_Class | 15 | List | RESTRICTED, CONFIDENTIAL, INTERNAL, PUBLIC |
| F | Reason_for_Change | 25 | List | Value change, Regulatory requirement, Business need, Data lifecycle, Merger/divestiture, Error correction, Periodic review, Other |
| G | Requested_By | 18 | Text | None |
| H | Approved_By | 18 | Text | None |
| I | Change_Date | 12 | Date | None |
| J | Status | 18 | List | Complete, Pending Approval, Rejected, In Progress |

### Sheet 5: Gap_Analysis

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Gap_ID | 12 | Text | None |
| B | Asset_Area | 20 | Text | None |
| C | Gap_Type | 22 | List | Unclassified Assets, Incomplete Labelling, Misclassification, No Labelling Capability, Inconsistent Labels, Missing Metadata, Other |
| D | Description | 45 | Text | None |
| E | Risk_Level | 12 | List | Critical, High, Medium, Low |
| F | Remediation_Action | 40 | Text | None |
| G | Owner | 15 | Text | None |
| H | Due_Date | 12 | Date | None |
| I | Status | 15 | List | Resolved, In Progress, Open, Accepted |

### Sheet 6: Evidence_Register

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Evidence_ID | 15 | Text | None |
| B | Description | 40 | Text | None |
| C | Evidence_Type | 22 | List | Inventory export, Classification report, Label screenshot, Audit finding, Training record, Policy acknowledgment, Other |
| D | Related_Asset_Gap | 20 | Text | None |
| E | Location | 30 | Text | None |
| F | Collected_Date | 15 | Date | None |
| G | Collected_By | 15 | Text | None |
| H | Verification_Status | 18 | List | Verified, Pending Review, Not Verified, Expired |

### Sheet 7: Approval_SignOff

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Role | 30 | Text | Pre-populated |
| B | Name | 25 | Text | Input |
| C | Signature | 20 | Text | Input |
| D | Date | 15 | Date | Input |
| E | Decision | 22 | List | Approved, Approved with conditions, Rejected, Pending |
| F | Comments | 30 | Text | Input |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| Asset_Inventory | E:E | ="RESTRICTED" | Red fill (#FF6B6B), White bold |
| Asset_Inventory | E:E | ="CONFIDENTIAL" | Orange fill (#FFA94D) |
| Asset_Inventory | E:E | ="INTERNAL" | Green fill (#69DB7C) |
| Asset_Inventory | E:E | ="PUBLIC" | Blue fill (#74C0FC) |
| Asset_Inventory | I:I | ="Labelled" | Green fill (#C6EFCE) |
| Asset_Inventory | I:I | ="Not Labelled" | Red fill (#FFC7CE) |
| Asset_Inventory | I:I | ="Partial" | Yellow fill (#FFEB9C) |
| Reclassification_Log | J:J | ="Complete" | Green fill (#C6EFCE) |
| Reclassification_Log | J:J | ="Pending Approval" | Yellow fill (#FFEB9C) |
| Reclassification_Log | J:J | ="Rejected" | Red fill (#FFC7CE) |
| Gap_Analysis | E:E | ="Critical" | Red fill (#FFC7CE), Bold |
| Gap_Analysis | E:E | ="High" | Orange fill (#FABF8F) |
| Gap_Analysis | I:I | ="Open" | Red fill (#FFC7CE) |
| Gap_Analysis | I:I | ="Resolved" | Green fill (#C6EFCE) |
| Evidence_Register | H:H | ="Verified" | Green fill (#C6EFCE) |
| Evidence_Register | H:H | ="Not Verified" | Red fill (#FFC7CE) |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| Asset Inventory (A.5.9) | Asset list source | A.5.9 -> Asset_Inventory |
| A.5.12-13.1 Workbook | Classification scheme | A.5.12-13.1 -> Classification levels |
| A.5.12-13.2 Workbook | Labelling standards | A.5.12-13.2 -> Labelling_Status |
| A.5.12-13.4 Workbook | Compliance monitoring | This workbook -> Compliance metrics |
| Data Discovery Tools | Classification scan results | Tools -> Asset_Inventory |
| GRC Platform | Compliance status | This workbook -> GRC |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.12-13 | Information Classification and Labelling | Parent policy |
| ISMS-IMP-A.5.12-13.S1 | Classification Scheme Definition | Classification scheme |
| ISMS-IMP-A.5.12-13.S2 | Labelling Procedures and Standards | Labelling standards |
| ISMS-IMP-A.5.12-13.S4 | Compliance Dashboard | Compliance monitoring |
| ISMS-IMP-A.5.12-13.S5 | Consolidation Dashboard | Executive view |
| ISMS-IMP-A.5.9 | Asset Inventory | Asset source |

---

**END OF SPECIFICATION**

---

*"You can't protect what you don't know you have."*
— Security Industry Proverb

<!-- QA_VERIFIED: 2026-02-04 -->
