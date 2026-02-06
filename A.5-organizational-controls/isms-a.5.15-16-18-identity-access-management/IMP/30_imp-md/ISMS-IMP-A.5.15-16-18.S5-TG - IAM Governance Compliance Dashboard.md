**ISMS-IMP-A.5.15-16-18.S5-TG - Lifecycle Compliance Detailed Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.16: Identity Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Lifecycle Compliance Detailed Assessment - Joiner/Mover/Leaver Analysis |
| **Related Policy** | ISMS-POL-A.5.15-16-18 (All Sections) |
| **Purpose** | Detailed analysis of identity lifecycle compliance across joiner/mover/leaver events with SLA tracking and HR integration status |
| **Target Audience** | IAM Team, HR Operations, IT Operations, Security Operations, Internal Audit |
| **Assessment Type** | Lifecycle Event Analysis |
| **Review Cycle** | Monthly (Lifecycle Review), Quarterly (Process Review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Lifecycle Compliance Detailed Assessment | ISMS Implementation Team |

---

# Technical Specification

## Workbook Structure

### Workbook Metadata

| Attribute | Value |
|-----------|-------|
| **Filename** | ISMS-IMP-A.5.15-16-18.5_Lifecycle_Compliance_Detailed_YYYYMMDD.xlsx |
| **Total Sheets** | 10 |
| **File Format** | Excel Workbook (.xlsx) |
| **Excel Version** | Excel 2016 or later |
| **Macros** | None (formulas only) |
| **External Links** | None |

### Sheet Overview

| Sheet # | Sheet Name | Purpose | Rows (Est.) |
|---------|-----------|---------|-------------|
| 1 | Instructions & Legend | Usage guidance and lifecycle standards | 50 |
| 2 | Joiner_Events | New hire provisioning compliance tracking | 65 (60 events) |
| 3 | Mover_Events | Role change and transfer processing | 45 (40 events) |
| 4 | Leaver_Events | Termination deprovisioning compliance | 55 (50 events) |
| 5 | Contractor_Lifecycle | Time-bound contractor access management | 40 (30 contractors) |
| 6 | Orphaned_Remediation | Orphaned account tracking and remediation | 25 (15 accounts) |
| 7 | Timeliness_Metrics | SLA compliance metrics summary | 20 |
| 8 | HR_Integration | HR system integration status | 15 |
| 9 | Gap_Analysis | Process gaps and remediation tracking | 15 |
| 10 | Evidence_Register | Evidence collection for A.5.16 compliance | 20 |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions & Legend

**Purpose**: Usage guidance and lifecycle compliance standards

**Header Section (Rows 1-4)**:
- **Row 1**: "ISMS-IMP-A.5.15-16-18.S5 - Lifecycle Compliance Detailed Assessment" (merged, title style)
- **Row 2**: Document metadata (italic)
- **Row 4**: Column headers

**Content Sections**:
- Document control information
- How to use this workbook
- Lifecycle SLA definitions (provisioning, deprovisioning, mover)
- Status legend (Compliant, Non-Compliant, Warning)
- Evidence collection instructions

---

### Sheet 2: Joiner_Events

**Purpose**: Track new hire provisioning compliance against SLA

**Header Section (Rows 1-4)**:
- **Row 1**: "Joiner Events - New Hire Provisioning Compliance" (merged A1:L1, title style)
- **Row 2**: Assessment Period metadata (italic)
- **Row 3**: Total Joiner Events count (italic)
- **Row 5**: Column headers

**Column Structure (Row 5+)**:

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Event ID | 12 | Unique joiner identifier (JOIN-1000) |
| B | User ID | 10 | User account identifier |
| C | Username | 18 | User login name |
| D | Full Name | 20 | User's display name |
| E | Department | 15 | User's department |
| F | Job Title | 18 | User's position |
| G | Hire Date | 12 | HR hire date |
| H | Provision Date | 15 | Account creation date |
| I | Days to Provision | 15 | Days between hire and provision |
| J | SLA | 8 | SLA threshold in days |
| K | Compliance | 15 | Compliant/Non-Compliant |
| L | Notes | 30 | Additional context for non-compliant events |

**Sample Data**: Generator pre-populates 60 joiner events.

**Conditional Formatting**:
- Column K: Green = Compliant, Red = Non-Compliant

---

### Sheet 3: Mover_Events

**Purpose**: Track role change and transfer processing timeliness

**Header Section (Rows 1-4)**:
- **Row 1**: "Mover Events - Role Change & Transfer Processing" (merged A1:L1, title style)
- **Row 2**: Assessment Period metadata (italic)
- **Row 3**: Total Mover Events count (italic)
- **Row 5**: Column headers

**Column Structure (Row 5+)**:

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Event ID | 12 | Unique mover identifier (MOVE-1000) |
| B | User ID | 10 | User account identifier |
| C | Username | 18 | User login name |
| D | Full Name | 20 | User's display name |
| E | Change Type | 20 | Department Transfer, Promotion, Role Change, Team Reassignment |
| F | From Dept | 15 | Previous department |
| G | To Dept | 15 | New department |
| H | Effective Date | 15 | HR effective date of change |
| I | Access Updated | 15 | Date access was modified |
| J | Days to Update | 15 | Days between effective and update |
| K | Compliance | 15 | Compliant/Delayed |
| L | Notes | 35 | Additional context for delayed events |

**Sample Data**: Generator pre-populates 40 mover events.

**Conditional Formatting**:
- Column K: Green = Compliant, Yellow = Delayed

---

### Sheet 4: Leaver_Events

**Purpose**: Track termination deprovisioning compliance (critical security)

**Header Section (Rows 1-4)**:
- **Row 1**: "Leaver Events - Termination Deprovisioning Compliance" (merged A1:L1, title style)
- **Row 2**: Assessment Period metadata (italic)
- **Row 3**: Total Leaver Events count (italic)
- **Row 5**: Column headers

**Column Structure (Row 5+)**:

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Event ID | 12 | Unique leaver identifier (LEAVE-1000) |
| B | User ID | 10 | User account identifier |
| C | Username | 18 | User login name |
| D | Full Name | 20 | User's display name |
| E | Department | 15 | User's department |
| F | Termination Date | 15 | HR termination date |
| G | Account Disabled | 18 | Date/time account was disabled |
| H | Hours to Disable | 15 | Hours between termination and disable |
| I | SLA | 8 | SLA threshold in hours |
| J | Compliance | 15 | Compliant/Non-Compliant |
| K | Security Risk | 15 | No/YES - flags security exposure |
| L | Notes | 50 | Security risk details for non-compliant |

**Sample Data**: Generator pre-populates 50 leaver events.

**Conditional Formatting**:
- Column J: Green = Compliant, Red = Non-Compliant
- Column K: Green = No, Red = YES

**Security Note**: Late deprovisioning is a critical security risk. Terminated employees with active access can cause data exfiltration, sabotage, or compliance violations.

---

### Sheet 5: Contractor_Lifecycle

**Purpose**: Track time-bound contractor access and contract expiration

**Header Section (Rows 1-4)**:
- **Row 1**: "Contractor Lifecycle - Time-Bound Access Management" (merged A1:K1, title style)
- **Row 2**: Assessment Date metadata (italic)
- **Row 3**: Active Contractors count (italic)
- **Row 5**: Column headers

**Column Structure (Row 5+)**:

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Contractor ID | 12 | Unique contractor identifier |
| B | Username | 22 | Contractor login name |
| C | Full Name | 20 | Contractor's display name |
| D | Sponsor | 20 | Business sponsor (manager) |
| E | Department | 15 | Department contractor works with |
| F | Contract Start | 15 | Contract start date |
| G | Contract End | 15 | Contract end date |
| H | Days Remaining | 15 | Days until contract expiration |
| I | Expiration Status | 18 | Active, Expiring Soon, EXPIRED |
| J | Extension Approved | 18 | Approved, Pending, Not Requested, N/A |
| K | Compliance | 15 | Compliant, Warning, Non-Compliant |

**Sample Data**: Generator pre-populates 30 contractors.

**Conditional Formatting**:
- Column K: Green = Compliant, Yellow = Warning, Red = Non-Compliant
- Column I: Red = EXPIRED, Yellow = Expiring Soon

**Status Logic**:
- **Active**: Days Remaining > 30
- **Expiring Soon**: Days Remaining 1-30
- **EXPIRED**: Days Remaining < 0

---

### Sheet 6: Orphaned_Remediation

**Purpose**: Track orphaned account detection and remediation

**Header Section (Rows 1-4)**:
- **Row 1**: "Orphaned Account Remediation Tracking" (merged A1:K1, title style)
- **Row 2**: Assessment Date metadata (bold, red - highlights security concern)
- **Row 3**: Orphaned Accounts count (bold, red)
- **Row 5**: Column headers

**Column Structure (Row 5+)**:

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Account ID | 10 | Unique account identifier |
| B | Username | 18 | Account login name |
| C | Account Type | 15 | Employee, Contractor, Service Account |
| D | Last Login | 15 | Last successful login date |
| E | Detection Date | 15 | When orphaned status was detected |
| F | Orphan Reason | 45 | Why account is considered orphaned |
| G | Assigned To | 20 | Team responsible for remediation |
| H | Remediation Action | 22 | Disable account, Delete account, Reassign owner, Document exception |
| I | Completion Date | 15 | Date remediation was completed |
| J | Days to Remediate | 18 | Days from detection to completion |
| K | Status | 15 | Remediated/Pending |

**Sample Data**: Generator pre-populates 15 orphaned accounts.

**Orphan Reasons**:
- No login for 120+ days
- User terminated but account not disabled
- No valid business owner
- Contractor contract ended, account still active

**Conditional Formatting**:
- Column K: Green = Remediated, Red = Pending

---

### Sheet 7: Timeliness_Metrics

**Purpose**: Summary of lifecycle SLA compliance metrics

**Header Section (Rows 1-3)**:
- **Row 1**: "Lifecycle Timeliness Metrics - SLA Compliance" (merged A1:F1, title style)
- **Row 2**: Assessment Period metadata (italic)
- **Row 4**: Section header
- **Row 5**: Column headers

**Column Structure (Row 5+)**:

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Metric | 35 | Compliance metric name |
| B | Target | 15 | Target threshold |
| C | Actual | 15 | Current performance |
| D | Status | 18 | Compliant, Warning, Non-Compliant |
| E | Gap | 10 | Difference from target |
| F | Comments | 50 | Context and affected items |

**Standard Metrics**:
- Joiner On-Time Provisioning (Target: ≥95%)
- Leaver On-Time Deprovisioning (Target: ≥98%)
- Mover Access Update (Target: ≥90%)
- Contractor Expiration Compliance (Target: 100%)
- Orphaned Account Remediation (Target: ≥90%)

**Conditional Formatting**:
- Column D: Green = Compliant, Yellow = Warning, Red = Non-Compliant

---

### Sheet 8: HR_Integration

**Purpose**: Document HR system integration status for lifecycle automation

**Header Section (Rows 1-3)**:
- **Row 1**: "HR System Integration Status" (merged A1:G1, title style)
- **Row 2**: Assessment Date metadata (italic)
- **Row 4**: Section header
- **Row 5**: Column headers

**Column Structure (Row 5+)**:

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Component | 35 | Integration component name |
| B | Status | 18 | Active, Partial, Not Implemented |
| C | Integration Method | 20 | API, CSV Import, Manual, N/A |
| D | Frequency | 15 | Real-time, Daily, Weekly, N/A |
| E | Last Sync | 18 | Last synchronization timestamp |
| F | Issues | 20 | Current issues or blockers |
| G | Notes | 35 | Additional context |

**Standard Components**:
- Employee Data Feed
- Termination Feed
- Department Transfer Feed
- Contractor Data Feed
- Authoritative Source Validation

**Conditional Formatting**:
- Column B: Green = Active, Yellow = Partial, Red = Not Implemented

---

### Sheet 9: Gap_Analysis

**Purpose**: Document lifecycle process gaps and remediation plans

**Header Section (Rows 1-3)**:
- **Row 1**: "Gap Analysis - Lifecycle Process Non-Compliance" (merged A1:J1, title style)
- **Row 2**: Assessment Date metadata (italic)
- **Row 4**: Column headers

**Column Structure (Row 4+)**:

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Gap ID | 10 | Unique identifier (GAP-001) |
| B | Category | 18 | Provisioning, Deprovisioning, Orphaned Accounts, Contractor Management |
| C | Description | 35 | What is the gap? |
| D | Risk Level | 12 | High, Medium, Low |
| E | Affected Items | 15 | Count or scope of impact |
| F | Root Cause | 35 | Why did this happen? |
| G | Remediation Plan | 45 | What action will fix this? |
| H | Owner | 18 | Who is responsible? |
| I | Due Date | 12 | Target resolution date |
| J | Status | 15 | Open, In Progress, Planned, Closed |

**Sample Data**: Generator pre-populates 4 common gaps.

**Conditional Formatting**:
- Column D: Red = High, Yellow = Medium, Green = Low
- Column J: Red = Open, Yellow = In Progress/Planned, Green = Closed

---

### Sheet 10: Evidence_Register

**Purpose**: Evidence collection for A.5.16 Identity Management compliance

**Header Section (Rows 1-3)**:
- **Row 1**: "Evidence Register - A.5.16 Identity Management" (merged A1:H1, title style)
- **Row 2**: Evidence Collection Date metadata (italic)
- **Row 4**: Column headers

**Column Structure (Row 4+)**:

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Evidence ID | 12 | Unique identifier (EV-001) |
| B | Requirement | 25 | A.5.16 requirement area |
| C | Evidence Type | 20 | Event Log, Report, Configuration, Screenshot |
| D | Evidence Location | 35 | File path, sheet reference, URL |
| E | Collection Date | 18 | Date evidence was collected |
| F | Completeness | 15 | Complete, Partial, Missing |
| G | Reviewed By | 20 | Who verified the evidence? |
| H | Notes | 40 | Additional context |

**Sample Data**: Generator pre-populates evidence items for:
- Joiner Process (Joiner_Events sheet)
- Mover Process (Mover_Events sheet)
- Leaver Process (Leaver_Events sheet)
- Contractor Management (Contractor_Lifecycle sheet)
- Orphaned Account Remediation (Orphaned_Remediation sheet)
- Timeliness Compliance (Timeliness_Metrics sheet)
- HR Integration (HR_Integration sheet)

**Conditional Formatting**:
- Column F: Green = Complete, Yellow = Partial, Red = Missing

---

## Styling Standards

### Color Scheme

| Style | Background | Font | Usage |
|-------|------------|------|-------|
| Title | Navy (#003366) | White, Bold, 14pt | Sheet titles |
| Header | Blue (#4472C4) | White, Bold, 11pt | Section headers |
| Column Header | Dark Blue (#305496) | White, Bold, 10pt | Column headers |
| Data | White | Black, 10pt | Data cells |
| Compliant | Green (#C6EFCE) | Dark Green (#006100), Bold | Compliant status |
| Warning | Yellow (#FFEB9C) | Dark Yellow (#9C5700), Bold | Warning status |
| Non-Compliant | Red (#FFC7CE) | Dark Red (#9C0006), Bold | Non-compliant status |

### Data Validation

**Compliance Status Fields**: Dropdown validation
- Joiner_Events Column K: Compliant, Non-Compliant
- Mover_Events Column K: Compliant, Delayed
- Leaver_Events Column J: Compliant, Non-Compliant
- Contractor_Lifecycle Column K: Compliant, Warning, Non-Compliant
- Orphaned_Remediation Column K: Remediated, Pending

**Risk Level Fields**: Dropdown validation
- Gap_Analysis Column D: High, Medium, Low

**Status Fields**: Dropdown validation
- Gap_Analysis Column J: Open, In Progress, Planned, Closed
- HR_Integration Column B: Active, Partial, Not Implemented

---

## Formula Reference

### Timeliness Calculations

**Days to Provision** (Joiner_Events Column I):
```
= Provision_Date - Hire_Date
```

**Compliance Check** (Joiner_Events Column K):
```
=IF(I6 <= SLA, "Compliant", "Non-Compliant")
```

**Hours to Disable** (Leaver_Events Column H):
```
= (Account_Disabled - Termination_Date) * 24
```

### Metrics Calculations

**On-Time Provisioning %**:
```
= COUNTIF(Joiner_Events!K:K, "Compliant") / COUNT(Joiner_Events!K:K)
```

**On-Time Deprovisioning %**:
```
= COUNTIF(Leaver_Events!J:J, "Compliant") / COUNT(Leaver_Events!J:J)
```

---

## Integration Notes

### Data Sources

This workbook documents detailed lifecycle events from:
- HR system (hire dates, termination dates, transfers)
- Identity management system (account creation, modification, disabling)
- Service desk tickets (provisioning requests, access change requests)

### Relationship to Other IAM Assessments

**This workbook (S5) provides detailed lifecycle data that feeds into**:
- S1 (User Inventory): Validates user lifecycle compliance
- S3 (Access Review): Identifies users requiring immediate review due to role changes

**Prerequisites**:
- HR system access for authoritative employee data
- Identity system logs for account provisioning timestamps
- Contractor management system for contract dates

---

**END OF SPECIFICATION**

---

*"The sum of an infinite series of fractions whose denominators are the squares of the natural numbers is equal to π²/6."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->