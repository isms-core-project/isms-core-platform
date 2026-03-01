<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.12-13.S3-UG:framework:UG:a.5.12-13 -->
**ISMS-IMP-A.5.12-13.S3-UG - Asset Classification Inventory**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.12-13: Classification and Labelling

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Asset Classification Inventory |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.12-13.S3-UG |
| **Related Policy** | ISMS-POL-A.5.12-13 (Classification and Labelling) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.12-13 (Classification and Labelling) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.5.12-13 (Classification and Labelling)
- ISMS-IMP-A.5.12-13.S1 (Classification Scheme Definition)
- ISMS-IMP-A.5.12-13.S2 (Labelling Procedures and Standards)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.12-13.S3-TG.

### Workbook at a Glance

This workbook contains the following 8 sheets:

| Sheet | Purpose |
|-------|---------|
| **Instructions & Legend** | Assessment guidance, control requirements, and field descriptions |
| **Asset Inventory** | Complete inventory of assets with classification assignments |
| **Classification Summary** | Summary statistics and coverage analysis of classification assignments |
| **Reclassification Log** | Audit trail of classification changes with justification and approval |
| **Gap Analysis** | Identification of unclassified assets and classification coverage gaps |
| **Evidence Register** | Tracking of supporting evidence for audit purposes |
| **Summary Dashboard** | Compliance overview auto-populated from your input data |
| **Approval Sign-Off** | Stakeholder sign-off and approval workflow |

---

## Assessment Overview

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

## Control Requirements

### ISO 27001:2022 Controls A.5.12 & A.5.13

Per ISO/IEC 27001:2022:

**Control A.5.12:**
> *"Information should be classified according to the information security needs of the organisation based on confidentiality, integrity, availability and relevant interested party requirements."*

**Control A.5.13:**
> *"An appropriate set of procedures for information labelling should be developed and implemented in accordance with the information classification scheme adopted by the organisation."*

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

## Prerequisites

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

## Completion Walkthrough

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

## Evidence Collection

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

## Common Pitfalls

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

## Quality Checklist

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

## Review and Approval

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

**END OF USER GUIDE**

---

*"Order is the shape upon which beauty depends."*
— Pearl S. Buck

<!-- QA_VERIFIED: 2026-03-01 -->
