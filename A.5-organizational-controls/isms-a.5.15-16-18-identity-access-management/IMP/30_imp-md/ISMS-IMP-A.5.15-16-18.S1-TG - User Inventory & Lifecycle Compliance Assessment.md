**ISMS-IMP-A.5.15-16-18.S1-TG - User Inventory & Lifecycle Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | User Inventory & Identity Lifecycle Compliance |
| **Related Policy** | ISMS-POL-A.5.15-16-18, Section 2.2 (Identity Management Requirements - A.5.16) |
| **Purpose** | Document complete user inventory across all identity systems, assess identity lifecycle compliance (joiner/mover/leaver timeliness), and identify orphaned accounts in a technology-agnostic manner |
| **Target Audience** | IAM Team, HR Team, IT Operations, Security Team, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Monthly (user inventory updates), Quarterly (comprehensive lifecycle assessment) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for User Inventory & Lifecycle assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.15-16-18.S1-UG.

---

# Technical Specification

## Workbook Structure

### Sheet 1: Instructions & Legend

#### Header Section (Row 1)

- **Title:** "ISMS-IMP-A.5.15-16-18.S1 - User Inventory & Lifecycle Compliance Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.5.16: Identity Management"
- **Styling:** Dark blue header (002060), white text, Calibri 16pt bold, centered, 40px height
- **Span:** Columns A-H merged

#### Document Information Block (Rows 3-6)

| Row | Label | Value |
|-----|-------|-------|
| 3 | Document ID: | ISMS-IMP-A.5.15-16-18.S1 |
| 4 | Assessment: | User Inventory & Lifecycle Compliance |
| 5 | Version: | 1.0 |
| 6 | Generated: | [Auto-generated timestamp DD.MM.YYYY HH:MM] |

#### Purpose Section (Row 8+)

- **Header:** "Purpose" - Blue subheader (4472C4)
- **Content:** Description of workbook purpose including user inventory tracking, provisioning/deprovisioning compliance, orphaned account detection, and A.5.16 compliance scoring

#### Workbook Structure Table (Row 17+)

| Sheet | Purpose | Key Metrics |
|-------|---------|-------------|
| User_Inventory | Complete user list with attributes | Total users, user types, active/disabled |
| Employee_Lifecycle | Employee provisioning/deprovisioning | On-time provisioning rate, deprovisioning rate |
| Contractor_Lifecycle | Contractor time-bound access | Contract compliance, expired access |
| Service_Accounts | Non-human account inventory | Service account count, ownership |
| Orphaned_Accounts | Orphaned account detection | Orphaned count, remediation status |
| Lifecycle_Metrics | Summary KPIs | Overall compliance score |
| Gap_Analysis | Non-compliance tracking | Gap count, remediation progress |
| Evidence_Register | Evidence collection | Evidence completeness |

#### Status Color Legend (Row 27+)

| Status | Description | Fill Color |
|--------|-------------|------------|
| Compliant | Lifecycle event completed within SLA | Green (C6EFCE) |
| Non-Compliant | Lifecycle event exceeded SLA | Red (FFC7CE) |
| Warning | Requires attention (e.g., inactive account, missing data) | Yellow (FFEB9C) |

#### Column Widths

- Column A: 25
- Column B: 50
- Column C: 35

---

## Sheet 2: User_Inventory

### Purpose
Complete inventory of ALL users across ALL identity systems with 100 sample users pre-populated.

### Header Section (Rows 1-4)

- **Row 1:** "User Inventory - All Identity Systems" (merged A1:M1, title style)
- **Row 2:** Assessment Date metadata
- **Row 3:** Total Users count
- **Row 5:** Column headers

### Column Definitions (14 columns)

| Column | Header | Width | Description | Conditional Formatting |
|--------|--------|-------|-------------|----------------------|
| A | User ID | 10 | Unique identifier (U10001, U10002, etc.) | None |
| B | Username | 20 | Account username (first.last or EXT-first.last) | None |
| C | Full Name | 20 | User's display name | None |
| D | Email | 30 | Email address | None |
| E | User Type | 15 | Employee, Contractor, Vendor, or Service Account | None |
| F | Department | 15 | Organizational department | None |
| G | Job Title | 25 | Job title/role | None |
| H | Manager | 20 | Direct manager name | None |
| I | Hire Date | 12 | DD.MM.YYYY format | None |
| J | Termination Date | 15 | DD.MM.YYYY format (blank if active) | None |
| K | Status | 12 | Active, Disabled, or Suspended | **CF:** Green=Active, Red=Disabled, Yellow=Suspended |
| L | Last Login | 12 | DD.MM.YYYY format or "Never" | None |
| M | Account Created | 12 | DD.MM.YYYY format | None |
| N | Comments | 30 | Free-text notes | None |

### Sample Data Distribution

- **User Types:** 70% Employee, 20% Contractor, 5% Vendor, 5% Service Account
- **Status Distribution:** 85% Active, 10% Disabled, 5% Suspended
- **Total Sample Users:** 100

### Freeze Panes
Freeze at A6 (headers remain visible when scrolling)

---

## Sheet 3: Employee_Lifecycle

### Purpose
Track employee provisioning (joiner) and deprovisioning (leaver) compliance in a single sheet with two sections.

### Header Section (Row 1)

- **Title:** "Employee Lifecycle Compliance - Joiner & Leaver Events" (merged A1:J1, title style)
- **Row 2:** Assessment Period metadata
- **Row 3:** Employees Assessed count

### JOINER EVENTS Section (Row 5+)

**Subheader:** "JOINER EVENTS - Provisioning Compliance" (blue subheader, merged A5:J5)

**Column Definitions (10 columns):**

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | User ID | 10 | Employee identifier |
| B | Username | 20 | Account username |
| C | Full Name | 20 | Employee name |
| D | Department | 15 | Department |
| E | Hire Date | 15 | DD.MM.YYYY format |
| F | Provision Date | 18 | DD.MM.YYYY format |
| G | Days to Provision | 15 | Calculated: Provision - Hire |
| H | SLA (Days) | 12 | Target: 0 days |
| I | Compliance Status | 18 | Compliant or Non-Compliant |
| J | Notes | 35 | Late provisioning notes |

**Conditional Formatting:** Column I - Green if Compliant, Red if Non-Compliant

### LEAVER EVENTS Section (Below Joiner section + 3 rows)

**Subheader:** "LEAVER EVENTS - Deprovisioning Compliance" (blue subheader)

**Column Definitions (10 columns):**

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | User ID | 10 | Employee identifier |
| B | Username | 20 | Account username |
| C | Full Name | 20 | Employee name |
| D | Department | 15 | Department |
| E | Termination Date | 15 | DD.MM.YYYY format |
| F | Disable Date | 18 | DD.MM.YYYY HH:MM format |
| G | Hours to Disable | 15 | Calculated time to disable |
| H | SLA (Hours) | 12 | Target: 24 hours |
| I | Compliance Status | 18 | Compliant or Non-Compliant |
| J | Notes | 35 | "Late deprovisioning - security risk" if non-compliant |

**Conditional Formatting:** Column I - Green if Compliant, Red if Non-Compliant

### Freeze Panes
Freeze at A7 (after joiner section header)

### Sample Data
- 50 employee lifecycle events pre-populated
| K | Notes | Text | Additional context | **USER INPUT** | None |

### Filter Criteria for This Sheet

- **Include:** Users with Hire Date in assessment period (e.g., Q1 2026)
- **Exclude:** Service accounts (no hire date), users hired before assessment period

### Summary Metrics (Top of Sheet, Rows 1-2, Columns M-S)

| Metric | Formula | Cell |
|--------|---------|------|
| Total New Hires | `=COUNTA(A:A)-1` | M1 |
| On-Time Provisioning | `=COUNTIF(I:I,"✅ On-Time")` | N1 |
---

## Sheet 4: Contractor_Lifecycle

### Purpose
Track contractor time-bound access compliance - contract periods and access expiration.

### Header Section (Rows 1-4)

- **Row 1:** "Contractor Lifecycle - Time-Bound Access Compliance" (merged A1:K1, title style)
- **Row 2:** Assessment Date metadata
- **Row 3:** Contractors Assessed count

### Column Definitions (11 columns)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | User ID | 10 | Contractor identifier |
| B | Username | 22 | Account username (EXT-first.last) |
| C | Full Name | 20 | Contractor name |
| D | Department | 15 | Department |
| E | Sponsor | 20 | Internal employee sponsor |
| F | Contract Start | 15 | DD.MM.YYYY format |
| G | Contract End | 15 | DD.MM.YYYY format |
| H | Access Expiry | 15 | DD.MM.YYYY format (same as contract end) |
| I | Days Remaining | 15 | Calculated: Contract End - Today |
| J | Status | 15 | Active, Expiring Soon, or Expired |
| K | Compliance | 15 | Compliant, Warning, or Non-Compliant |

### Compliance Logic

- **Days Remaining < 0:** Status = "Expired", Compliance = "Non-Compliant" (Red)
- **Days Remaining < 30:** Status = "Expiring Soon", Compliance = "Warning" (Yellow)
- **Days Remaining ≥ 30:** Status = "Active", Compliance = "Compliant" (Green)

### Freeze Panes
Freeze at A6

### Sample Data
- 30 contractor records pre-populated

---

## Sheet 5: Service_Accounts

### Purpose
Inventory of non-human accounts (service accounts, automation accounts, system accounts).

### Header Section (Rows 1-4)

- **Row 1:** "Service Account Inventory - Non-Human Accounts" (merged A1:J1, title style)
- **Row 2:** Assessment Date metadata
- **Row 3:** Service Accounts count

### Column Definitions (10 columns)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Account ID | 12 | Service account identifier |
| B | Account Name | 30 | Service account username (svc-*) |
| C | Purpose | 25 | Automated Backup, Monitoring Agent, Integration Service, etc. |
| D | Owner | 20 | Technical owner name |
| E | Department | 15 | Typically IT |
| F | Created Date | 15 | DD.MM.YYYY format |
| G | Last Used | 15 | DD.MM.YYYY format or "Unknown" |
| H | Privileged | 12 | Yes or No |
| I | Password Rotation | 18 | 90 Days, 60 Days, Never, Manual |
| J | Status | 12 | Active or Disabled |

### Conditional Formatting

- **Status (Column J):** Green if Active, Red if Disabled

### Freeze Panes
Freeze at A6

### Sample Data
- 20 service accounts pre-populated (40% privileged)

---

## Sheet 6: Orphaned_Accounts

### Purpose
Detection and remediation tracking for orphaned accounts (no valid owner or terminated user still active).

### Header Section (Rows 1-4)

- **Row 1:** "Orphaned Account Detection & Remediation" (merged A1:K1, title style)
- **Row 2:** Detection Date metadata
- **Row 3:** Orphaned Accounts Found count (bold red)

### Column Definitions (11 columns)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | User ID | 10 | Account identifier |
| B | Username | 20 | Account username |
| C | Full Name | 20 | User name |
| D | User Type | 15 | Employee, Contractor, etc. |
| E | Department | 15 | Department |
| F | Last Login | 15 | DD.MM.YYYY or "Never" |
| G | Status | 12 | Account status |
| H | Orphan Reason | 40 | Why flagged as orphaned |
| I | Detected Date | 15 | DD.MM.YYYY format |
| J | Remediation Status | 18 | Open, In Progress, Remediated, Closed |
| K | Notes | 30 | Additional context |

### Orphan Detection Criteria

- Disabled account with no termination record
- No login for >90 days (INACTIVE_THRESHOLD_DAYS)

### Conditional Formatting

- **Remediation Status (Column J):**
  - Green: Remediated, Closed
  - Yellow: In Progress
  - Red: Open

### Freeze Panes
Freeze at A6

### Sample Data
- 15 orphaned accounts pre-populated

---

## Sheet 7: Lifecycle_Metrics

### Purpose
Summary KPIs and compliance metrics for A.5.16 Identity Management.

### Header Section (Rows 1-2)

- **Row 1:** "Identity Lifecycle Compliance Metrics - A.5.16" (merged A1:F1, title style)
- **Row 2:** Assessment Period metadata

### KPI Section (Row 4+)

**Subheader:** "Key Performance Indicators (KPIs)" (blue header)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Metric | 35 | Metric name |
| B | Target | 15 | Target value (e.g., ≥95%) |
| C | Actual | 15 | Actual value |
| D | Status | 18 | Compliant, Warning, Non-Compliant |
| E | Gap | 10 | Difference from target |
| F | Comments | 50 | Explanation |

### Sample Metrics

- Provisioning On-Time Rate: Target ≥95%, Actual 92%
- Deprovisioning On-Time Rate: Target ≥98%, Actual 96%
- Orphaned Account Count: Target ≤1%, Actual 1.5%
- Service Account Documentation: Target 100%, Actual 95%
- Contractor Access Compliance: Target 100%, Actual 90%

### Overall Score Section

- Overall Score: 82%
- Maturity Level: Managed (80-89%)

---

## Sheet 8: Gap_Analysis

### Purpose
Track non-compliance findings and remediation progress.

### Header Section (Rows 1-3)

- **Row 1:** "Gap Analysis - Non-Compliance Findings" (merged A1:J1, title style)
- **Row 2:** Assessment Date metadata

### Column Definitions (10 columns)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Gap ID | 10 | GAP-001, GAP-002, etc. |
| B | Category | 18 | Provisioning, Deprovisioning, Orphaned Accounts, etc. |
| C | Description | 40 | Gap description |
| D | Risk Level | 12 | High, Medium, Low |
| E | Affected Users | 15 | Number of users affected |
| F | Root Cause | 30 | Why the gap exists |
| G | Remediation Plan | 40 | Proposed solution |
| H | Owner | 18 | Responsible person/team |
| I | Due Date | 12 | DD.MM.YYYY format |
| J | Status | 15 | Open, In Progress, Closed |

### Conditional Formatting

- **Risk Level (Column D):** Red=High, Yellow=Medium, Green=Low
- **Status (Column J):** Green=Closed, Yellow=In Progress, Red=Open

### Freeze Panes
Freeze at A5

---

## Sheet 9: Evidence_Register

### Purpose
Centralized evidence repository for audit traceability.

### Header Section (Rows 1-3)

- **Row 1:** "Evidence Register - A.5.16 Identity Management" (merged A1:H1, title style)
- **Row 2:** Evidence Collection Date metadata

### Column Definitions (8 columns)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Evidence ID | 12 | EV-001, EV-002, etc. |
| B | Requirement | 25 | What evidence supports |
| C | Evidence Type | 20 | Spreadsheet, Process Metrics, Policy Document, etc. |
| D | Evidence Location | 35 | File path or sheet reference |
| E | Collection Date | 18 | DD.MM.YYYY format |
| F | Completeness | 15 | Complete, Partial, Not Collected |
| G | Reviewed By | 20 | Reviewer name |
| H | Notes | 40 | Additional context |

### Conditional Formatting

- **Completeness (Column F):** Green=Complete, Yellow=Partial, Red=Not Collected

### Freeze Panes
Freeze at A5

---

## Sheet 10: Approval_Sign_Off

### Purpose
Three-level approval workflow for completed assessment.

### Header Section (Rows 1-2)

- **Row 1:** "Assessment Approval & Sign-Off" (merged A1:F1, title style)
- **Row 2:** Assessment Date metadata

### Approval Table (Row 4+)

**Subheader:** "3-Level Approval Process" (blue header)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Approval Level | 25 | Level 1: Prepared By, Level 2: Reviewed By, Level 3: Approved By |
| B | Role | 20 | IAM Manager, Security Manager, CISO |
| C | Name | 25 | [Name] placeholder |
| D | Signature | 20 | User input |
| E | Date | 15 | User input |
| F | Status | 15 | Pending |

---

## Cell Styling Reference

### Header Styles

- **Main Header:** Font: Calibri 14pt bold white, Fill: 003366 (dark blue), Alignment: centered/wrapped, Height: 40px
- **Subheader:** Font: Calibri 11pt bold white, Fill: 4472C4 (blue), Alignment: centered/wrapped
- **Column Header:** Font: Calibri 10pt bold black, Fill: D9D9D9 (gray), Alignment: centered/wrapped, Border: thin all sides
- **Section Header (within sheet):** Font: Calibri 12pt bold, Fill: E7E6E6 (light gray), Alignment: left, Border: medium bottom

### Input Cell Styles

- **Fill:** FFFFCC (light yellow) - indicates user should fill in
- **Alignment:** Left for text, center for dropdowns, right for numbers
- **Border:** Thin black on all sides
- **Protection:** Unlocked (allow editing)

### Formula/Calculated Cell Styles

- **Fill:** White (FFFFFF) or light gray (F2F2F2) for read-only calculated fields
- **Alignment:** Right for numbers, left for text
- **Border:** Thin gray on all sides
- **Protection:** Locked (prevent editing)

### Status Fill Colors (Conditional Formatting)

- **✅ Compliant / On-Time / Verified:** C6EFCE (green)
- **⚠️ Partial / Late / Pending:** FFEB9C (yellow)
- **❌ Non-Compliant / Very Late / Issues:** FFC7CE (red)
- **🚨 CRITICAL:** FF0000 (dark red) - for critical security issues
- **ℹ️ Under Investigation / In Progress:** B4C7E7 (blue)
- **N/A / Not Applicable:** D3D3D3 (gray)

### Data Bars (Progress Indicators)

- **Color:** Green (63BE7B)
- **Direction:** Left-to-right
- **Min Value:** 0
- **Max Value:** 100
- **Show Bar Only:** No (show value and bar)

---

## Freeze Panes

Apply freeze panes for easier navigation:

- **Sheet 2 (User Inventory):** Freeze at A4 (column headers visible when scrolling down)
- **Sheet 3 (Provisioning):** Freeze at A4
- **Sheet 4 (Deprovisioning):** Freeze at A4
- **Sheet 5 (Orphaned):** Freeze at A4
- **Sheet 6 (Inactive):** Freeze at A4
- **Sheet 7 (Dashboard):** Freeze at A5 (section headers visible)
- **Sheet 8 (Gap Analysis):** Freeze at A4
- **Sheet 9 (Evidence):** Freeze at A4
- **Sheet 10 (Approval):** Freeze at A3

---

## File Naming Convention

**Format:** `ISMS-IMP-A.5.15-16-18.S1_User_Inventory_Lifecycle_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.5.15-16-18.S1_User_Inventory_Lifecycle_20260122.xlsx`

**Version Control:**

- Date in filename indicates assessment date or data snapshot date
- Monthly assessments → New file each month
- Quarterly comprehensive → Major version in filename (e.g., `..._Q1-2026.xlsx`)

---

## Monthly Review Cycle

1. **Update User Inventory (Sheet 2):**

   - Re-export users from all identity systems
   - Re-export HR data
   - Update last login dates
   - Recalculate all formulas

2. **Refresh Provisioning Analysis (Sheet 3):**

   - Filter to current month new hires
   - Calculate current month compliance

3. **Refresh Deprovisioning Analysis (Sheet 4):**

   - Filter to current month terminations
   - Calculate current month compliance
   - **CRITICAL:** Check for any terminated users still active >30 days

4. **Update Orphaned Accounts (Sheet 5):**

   - Run cross-reference (identity systems vs. HR)
   - Update remediation status

5. **Update Inactive Accounts (Sheet 6):**

   - Recalculate days since last login
   - Update inactive account list

6. **Refresh Dashboard (Sheet 7):**

   - All metrics auto-update from linked sheets
   - Review maturity score trend

7. **Update Gap Analysis (Sheet 8):**

   - Close resolved gaps
   - Add new gaps identified in current month
   - Update remediation progress

8. **Add New Evidence (Sheet 9):**

   - Document current month exports and data sources

9. **Update Approval (Sheet 10):**

   - IAM Team Lead monthly review
   - CISO sign-off if significant changes or critical gaps

---

## Quarterly Comprehensive Review Cycle

1. **Deep Dive Analysis:**

   - Analyze trends over last 3 months
   - Identify systemic issues (e.g., provisioning always late by 2 days → process issue)
   - Root cause analysis for recurring gaps

2. **Orphaned Account Cleanup Campaign:**

   - Intensive investigation of all orphaned accounts
   - Target: Close 100% of orphaned accounts identified >90 days ago

3. **Process Improvement:**

   - Review provisioning/deprovisioning procedures
   - Identify automation opportunities
   - Update documentation if processes changed

4. **Benchmark Review:**

   - Compare Q1 vs. Q2 vs. Q3 vs. Q4
   - Are we improving? (maturity score trend)
   - What changed? (staffing, technology, process)

5. **CISO Review and Approval:**

   - Present quarterly summary to CISO
   - Review critical gaps and remediation plans
   - Allocate budget/resources for improvements

---

## Integration Points

### Related Assessments (Other A.5.15-16-18 Workbooks)

**A.5.15-16-18.2 - Access Rights Matrix Assessment:**

- **Input FROM this workbook:** User inventory (Sheet 2) provides baseline user list
- **Usage:** Access rights assessment maps users (from .1) to systems/applications to access levels

**A.5.15-16-18.3 - Access Review Results Assessment:**

- **Input FROM this workbook:** Active user list (Sheet 2) defines review scope
- **Usage:** Access review verifies which users' access was reviewed and confirmed/removed

**A.5.15-16-18.4 - Role Definition & SoD Compliance Assessment:**

- **Input FROM this workbook:** User list (Sheet 2) for role assignment verification
- **Usage:** Role compliance assessment verifies users are assigned to appropriate roles, detects SoD violations

**A.5.15-16-18.5 - IAM Governance Compliance Dashboard:**

- **Input FROM this workbook:** Lifecycle compliance metrics (Sheet 7)
- **Usage:** Dashboard consolidates lifecycle metrics with access rights, reviews, and role compliance into executive summary

### Related ISMS Documents

- **ISMS-POL-A.5.15-16-18:** Identity & Access Management Policy (defines requirements being assessed)
- **Risk Register:** Link orphaned/inactive account gaps to IAM risk items
- **Incident Management:** Link account compromise incidents to lifecycle gaps
- **Change Management:** Link identity system changes to assessment updates
- **Asset Inventory:** Ensure identity systems are tracked as assets

### HR System Integration

- **Joiner Event Triggers:** HR system notifies IAM Team of new hires → provisioning
- **Leaver Event Triggers:** HR system notifies IAM Team of terminations → deprovisioning
- **Mover Event Triggers:** HR system notifies IAM Team of role changes → access review

### Audit Trail

- All evidence referenced in Evidence Register (Sheet 9)
- Gap remediation linked to project management system
- Lifecycle SLA compliance tracked monthly for trend analysis
- Approval sign-off (Sheet 10) maintains complete audit trail for certification

---

**END OF SPECIFICATION**

---

*"I learned very early the difference between knowing the name of something and knowing something."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
