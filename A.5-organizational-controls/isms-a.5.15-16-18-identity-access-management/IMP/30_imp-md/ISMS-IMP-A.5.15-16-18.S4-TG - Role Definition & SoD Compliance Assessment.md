**ISMS-IMP-A.5.15-16-18.S4-TG - Role Definition & SoD Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Role-Based Access Control (RBAC) Maturity & Segregation of Duties (SoD) Compliance |
| **Related Policy** | ISMS-POL-A.5.15-16-18, Section 2.3 (Role Definition & RBAC - A.5.18), Section 2.1.4 (Segregation of Duties - A.5.15) |
| **Purpose** | Assess RBAC adoption, verify role-based access implementation, detect segregation of duties violations, and identify role governance gaps |
| **Target Audience** | IAM Team, Security Operations, Access Control Administrators, Internal Audit, Compliance Officers |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Quarterly (Critical Roles), Semi-Annual (All Roles), Annual (Comprehensive Role Governance Review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Role Definition & SoD Compliance assessment workbook | ISMS Implementation Team |

---

# Technical Specification

## Workbook Structure

### Workbook Metadata

| Attribute | Value |
|-----------|-------|
| **Filename** | ISMS-IMP-A.5.15-16-18.S4_RoleCompliance_YYYY-MM.xlsx |
| **Total Sheets** | 11 |
| **File Format** | Excel Workbook (.xlsx) |
| **Excel Version** | Excel 2016 or later |
| **Macros** | None (formulas only) |
| **External Links** | None (self-contained) |

### Sheet Overview

| Sheet # | Sheet Name | Purpose | Rows (Est.) |
|---------|-----------|---------|-------------|
| 1 | Instructions_and_Legend | Document control, how to use, legends | 50 |
| 2 | Role_Catalog | Complete role inventory (40 roles) | 45 |
| 3 | Role_Assignments | User-to-role mappings (100 users) | 105 |
| 4 | Role_Access_Mapping | Role-to-system access rights | 45 |
| 5 | SoD_Matrix | Conflicting role combinations (30 pairs) | 35 |
| 6 | SoD_Violations | Users with conflicting roles (15 violations) | 20 |
| 7 | Compensating_Controls | SoD violation mitigations (15 controls) | 20 |
| 8 | RBAC_Coverage | RBAC adoption metrics by system | 30 |
| 9 | Gap_Analysis | Role governance gaps and remediation | 35 |
| 10 | Evidence_Register | Evidence for A.5.15/A.5.18 compliance | 55 |
| 11 | Approval_Sign_Off | Three-level approval workflow | 15 |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions_and_Legend

**Purpose**: Document control, navigation guide, status/risk legends

**Layout**:

- **Rows 1-15**: Document Control
- **Rows 17-30**: Assessment Overview
- **Rows 32-45**: How to Use This Workbook
- **Rows 47-60**: Status Legends
- **Rows 62-75**: Risk Level Legends
- **Rows 77-90**: Conditional Formatting Guide
- **Rows 92-105**: Sheet Navigation Links

#### Document Control Section (Rows 1-15)

| Cell | Label | Value | Format |
|------|-------|-------|--------|
| A1 | Title | "ISMS-IMP-A.5.15-16-18.S4 - Role Definition & SoD Compliance Assessment" | Bold, 14pt, Navy |
| A3 | Document ID | "ISMS-IMP-A.5.15-16-18.S4" | Normal |
| A4 | Version | "1.0" | Normal |
| A5 | Assessment Period | "[Start Date] to [End Date]" | Normal, Date format |
| A6 | Prepared By | "[Name, Title]" | Normal |
| A7 | Preparation Date | [Date] | Date format |
| A8 | Review Date | [Date] | Date format |
| A9 | Next Review | [Date] (Quarterly/Semi-Annual/Annual) | Date format |
| A10 | Status | Dropdown: Draft, In Review, Approved | Conditional format |

#### Status Legend (Rows 47-60)

| Status | Description | Color Code |
|--------|-------------|------------|
| Active | Role or assignment currently active | Green background |
| Under Review | Role definition being updated | Yellow background |
| Obsolete | Role no longer used, should be deactivated | Orange background |
| Expired | Time-bounded role past expiration | Red background |
| Remediated | SoD violation resolved | Green background |
| Justified with Controls | SoD violation approved with mitigations | Yellow background |
| Open | SoD violation unresolved | Red background |

#### Risk Level Legend (Rows 62-75)

| Risk Level | Description | Color Code |
|------------|-------------|------------|
| Critical | Unresolved SoD violation with fraud risk | Red text, Red background |
| High | Low RBAC adoption, missing SoD approvals | Red text |
| Medium | Outdated roles, obsolete roles active | Orange text |
| Low | Minor process improvements | Black text |

#### Conditional Formatting Guide (Rows 77-90)

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| RBAC Adoption | >= 80% | 60-79% | < 60% |
| SoD Violations (Unresolved) | 0 | N/A | > 0 |
| Role Review Compliance | >= 95% | 80-94% | < 80% |
| Direct Access % | < 20% | 20-30% | > 30% |
| Overall Maturity Score | >= 80 | 60-79 | < 60 |

---
### Sheet 2: Role_Catalog

**Purpose**: Complete role inventory with definitions and ownership

**Column Structure** (Row 5+):

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Role ID | 12 | Unique identifier (ROLE-001) |
| B | Role Name | 25 | Role display name |
| C | Description | 40 | What this role grants access to |
| D | Department | 18 | Department owning this role |
| E | Business Owner | 20 | Role owner name |
| F | Risk Level | 15 | Critical, High, Medium, Low |
| G | Users Assigned | 12 | Count of users with this role |
| H | Systems Accessed | 25 | Systems this role provides access to |
| I | Last Review | 15 | Date of last role review |
| J | Status | 12 | Active, Under Review, Obsolete |

**Sample Data**: Generator pre-populates 40 roles.

---

### Sheet 3: Role_Assignments

**Purpose**: User-to-role mappings showing who has which roles

**Column Structure** (Row 5+):

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | User ID | 12 | Unique user identifier |
| B | Username | 18 | User login name |
| C | Full Name | 20 | User's display name |
| D | Department | 18 | User's department |
| E | Assigned Role | 25 | Role assigned to user |
| F | Assignment Date | 15 | When role was assigned |
| G | Assigned By | 18 | Who approved assignment |
| H | Expiration Date | 15 | For time-bounded assignments |
| I | Status | 12 | Active, Expired, Pending Review |

**Sample Data**: Generator pre-populates 100 user role assignments.

---

### Sheet 4: Role_Access_Mapping

**Purpose**: Role-to-system access rights documentation

**Column Structure** (Row 5+):

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Role ID | 12 | Role identifier |
| B | Role Name | 25 | Role display name |
| C | System | 30 | System/application name |
| D | Access Level | 18 | Read, Read/Write, Admin |
| E | Access Rights | 40 | Specific permissions granted |
| F | Business Justification | 35 | Why this access is needed |
| G | Last Reviewed | 15 | Date access mapping reviewed |

**Sample Data**: Maps 40 roles to their system access rights.

---

### Sheet 5: SoD_Matrix

**Purpose**: Define conflicting role combinations (Segregation of Duties)

**Column Structure** (Row 5+):

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Conflict ID | 12 | Unique conflict pair identifier |
| B | Role A | 25 | First conflicting role |
| C | Role B | 25 | Second conflicting role |
| D | Conflict Reason | 40 | Why these roles conflict |
| E | Risk Level | 15 | Critical, High, Medium |
| F | Regulatory Basis | 25 | SOX, GDPR, Internal Policy |
| G | Exception Allowed | 12 | Yes/No |
| H | Required Controls | 35 | If exception, what controls needed |

**Sample Data**: Generator pre-populates 30 conflicting role pairs.

---

### Sheet 6: SoD_Violations

**Purpose**: Users with conflicting roles requiring remediation

**Column Structure** (Row 5+):

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Violation ID | 12 | Unique violation identifier |
| B | User ID | 12 | User with conflict |
| C | Username | 18 | User login name |
| D | Role A | 25 | First assigned role |
| E | Role B | 25 | Conflicting assigned role |
| F | Conflict ID | 12 | Reference to SoD_Matrix |
| G | Risk Level | 15 | Critical, High, Medium |
| H | Detection Date | 15 | When violation was found |
| I | Status | 18 | Open, Remediated, Justified |
| J | Resolution Notes | 35 | How violation was addressed |

**Sample Data**: Generator pre-populates 15 SoD violations.

---

### Sheet 7: Compensating_Controls

**Purpose**: Document mitigations for approved SoD violations

**Column Structure** (Row 5+):

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Control ID | 12 | Unique control identifier |
| B | Violation ID | 12 | Reference to SoD_Violations |
| C | User | 20 | Affected user |
| D | Conflicting Roles | 35 | The roles in conflict |
| E | Control Type | 20 | Monitoring, Approval, Review |
| F | Control Description | 40 | What the control does |
| G | Control Owner | 20 | Who is responsible |
| H | Review Frequency | 15 | How often control is verified |
| I | Last Verified | 15 | Date control was last tested |
| J | Effectiveness | 15 | Effective, Partial, Ineffective |

**Sample Data**: Generator pre-populates 15 compensating controls.

---

### Sheet 8: RBAC_Coverage

**Purpose**: RBAC adoption metrics by system

**Column Structure** (Row 5+):

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | System Name | 30 | System/application |
| B | Total Users | 12 | Users with access |
| C | Role-Based Access | 15 | Users via roles |
| D | Direct Access | 15 | Users with direct grants |
| E | RBAC Adoption % | 15 | Percentage using RBAC |
| F | Target % | 12 | Target RBAC adoption |
| G | Gap | 12 | Difference from target |
| H | Status | 15 | Compliant, At Risk, Non-Compliant |

**RBAC Adoption Status**:
- **Compliant**: RBAC >= 80% (green)
- **At Risk**: RBAC 60-79% (yellow)
- **Non-Compliant**: RBAC < 60% (red)

---

### Sheet 9: Gap_Analysis

**Purpose**: Role governance gaps and remediation tracking

**Column Structure** (Row 5+):

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Gap ID | 10 | Unique identifier (GAP-001) |
| B | Category | 18 | Role Definition, RBAC, SoD, Governance |
| C | Description | 45 | What is the gap? |
| D | Risk Level | 12 | Critical, High, Medium, Low |
| E | Affected Items | 15 | Scope of impact |
| F | Root Cause | 35 | Why did this happen? |
| G | Remediation Plan | 40 | What action will fix this? |
| H | Owner | 18 | Who is responsible? |
| I | Due Date | 12 | Target resolution date |
| J | Status | 15 | Open, In Progress, Closed |

**Sample Data**: Generator pre-populates common gaps.

---

### Sheet 10: Evidence_Register

**Purpose**: Evidence collection for A.5.15/A.5.18 role compliance

**Column Structure** (Row 5+):

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Evidence ID | 12 | Unique identifier (EV-001) |
| B | Requirement | 25 | A.5.15/A.5.18 requirement |
| C | Evidence Type | 20 | Spreadsheet, Report, Screenshot |
| D | Evidence Location | 35 | File path, sheet reference |
| E | Collection Date | 18 | Date evidence collected |
| F | Completeness | 15 | Complete, Partial, Missing |
| G | Reviewed By | 20 | Who verified evidence |
| H | Notes | 40 | Additional context |

**Sample Data**: Generator pre-populates 50 evidence items.

---

### Sheet 11: Approval_Sign_Off

**Purpose**: Three-level approval workflow for completed assessment

**Header Section**:
- **Row 1**: "Assessment Approval & Sign-Off" (title style)
- **Row 2**: Assessment Date metadata

**Approval Table** (Row 5+):

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Approval Level | 25 | Level 1, 2, or 3 |
| B | Role | 20 | IAM Manager, Security Manager, CISO |
| C | Name | 25 | Approver name |
| D | Signature | 20 | User input |
| E | Date | 15 | Approval date |
| F | Status | 15 | Pending, Approved |

---

## Cell Styling Reference

### Color Palette

| Element | Background Color | Text Color | Font Size |
|---------|-----------------|------------|-----------|
| Sheet Tab (Active) | Navy (RGB: 31, 73, 125) | White | N/A |
| Header Row | Navy (RGB: 31, 73, 125) | White | 14pt |
| Subheader | Light Blue (RGB: 180, 198, 231) | Black | 12pt |
| Good/Compliant | Light Green (RGB: 198, 224, 180) | Dark Green (RGB: 70, 120, 70) | Normal |
| Warning/Review | Light Yellow (RGB: 255, 235, 156) | Dark Orange (RGB: 204, 102, 0) | Normal |
| Critical/Non-Compliant | Light Red (RGB: 255, 199, 206) | Dark Red (RGB: 192, 0, 0) | Normal |
| Neutral | White (RGB: 255, 255, 255) | Black (RGB: 0, 0, 0) | Normal |

### Font Standards

| Element | Font Family | Font Size | Bold | Italic |
|---------|-------------|-----------|------|--------|
| Main Title (Sheet 1) | Calibri | 14pt | Yes | No |
| Section Header | Calibri | 12pt | Yes | No |
| Column Header | Calibri | 11pt | Yes | No |
| Data Cell | Calibri | 11pt | No | No |
| Metric Label | Calibri | 11pt | Yes | No |
| Metric Value | Calibri | 11pt | No | No |
| Comments/Notes | Calibri | 10pt | No | No |

### Number Formats

| Data Type | Format Code | Example |
|-----------|-------------|---------|
| Percentage | `0.0%` | 85.5% |
| Percentage (No Decimal) | `0%` | 85% |
| Integer | `#,##0` | 1,234 |
| Decimal (2 places) | `#,##0.00` | 1,234.56 |
| Date | `yyyy-mm-dd` | 2025-10-15 |
| Currency | `$#,##0.00` | $1,234.56 |

---

## Freeze Panes Configuration

**All Data Sheets (Sheets 2-9)**:

- Freeze Panes: Row 2 (header row always visible when scrolling)
- Selection before freezing: Cell A2

**How to Apply**:
1. Select cell A2
2. View → Freeze Panes → Freeze Panes
3. Result: Row 1 (header) remains visible when scrolling down

---

## File Naming Convention

**Format**: `ISMS-IMP-A.5.15-16-18.S4_RoleCompliance_YYYY-MM.xlsx`

**Examples**:

- `ISMS-IMP-A.5.15-16-18.S4_RoleCompliance_2025-10.xlsx` (October 2025 assessment)
- `ISMS-IMP-A.5.15-16-18.S4_RoleCompliance_2026-01.xlsx` (January 2026 assessment)

**Versioning**:

- Monthly assessments: YYYY-MM
- Quarterly assessments: YYYY-Q1, YYYY-Q2, etc.
- Annual assessments: YYYY-Annual

---

## Monthly/Quarterly Review Cycles

### Quarterly Update Procedures

**Steps**:
1. **Update Role Assignments** (Sheet 3):

   - Export current role/group memberships from identity systems
   - Add new role assignments (rows)
   - Update Status for expired/removed assignments
   - Recalculate Users_Assigned in Sheet 2 Role_Catalog (formula auto-updates)

2. **Detect New SoD Violations** (Sheet 6):

   - Cross-reference updated Sheet 3 against Sheet 5 SoD_Matrix
   - Add new violations (users who gained conflicting roles)
   - Update Status for remediated violations
   - Remediate or justify new violations

3. **Update Direct Access Users** (Sheet 4):

   - Identify new direct access users (not in Sheet 3 roles)
   - Obtain business justifications
   - Update Last_Review_Date for quarterly reviews
   - Target: Migrate direct access users to roles

4. **Recalculate RBAC Metrics** (Sheet 7):

   - Formulas auto-update based on Sheet 2, 3, 4, 6 changes
   - Compare to previous quarter (trending?)
   - Update gap analysis if new gaps identified

5. **Update Gap Analysis** (Sheet 8):

   - Review existing gaps: Status (Open → In Progress → Closed)
   - Add new gaps identified during quarterly review
   - Verify Target_Date for overdue gaps
   - Update remediation progress

**Time Required**: 3-5 hours

---

### Semi-Annual Comprehensive Review

**Steps**:
1. **Role Catalog Review** (Sheet 2):

   - Review all roles: Still needed? Definition accurate?
   - Deactivate obsolete roles (zero users, outdated job functions)
   - Create new roles (emerging job functions)
   - Update Last_Review_Date for reviewed roles

2. **Role Owner Validation**:

   - Contact all role owners (email or meeting)
   - Confirm role definitions still accurate
   - Update role descriptions if job functions changed
   - Document role owner sign-off (evidence)

3. **Comprehensive SoD Review** (Sheet 6):

   - Review all SoD violations (Sheet 6)
   - Verify justified violations still justified (business reason valid?)
   - Verify compensating controls still in place (logging, audits)
   - Remediate violations where justification expired

4. **Role Accuracy Assessment**:

   - Sample 10-20 users per role
   - Compare Sheet 2 Role_Catalog (role definition) vs. actual access (from Sheet 2 of A.5.15-16-18.2)
   - Identify role drift (users have more/less access than role defines)
   - Remediate discrepancies (update role definitions or fix access)

5. **RBAC Adoption Improvement Plan** (Sheet 8):

   - If RBAC Adoption < 80%: Create plan to improve
   - Identify 3-5 new roles to create (common direct access patterns)
   - Target 20-30 users to migrate from direct access to roles
   - Document improvement plan in Gap Analysis

**Time Required**: 5-8 hours

---

### Annual Strategic Review

**Steps**:
1. **Comprehensive Role Catalog Review** (Sheet 2):

   - Review ALL roles (30-60 minute meetings with each role owner)
   - Validate role definitions, access mappings, business need
   - Deactivate obsolete roles, create new roles
   - Update role hierarchy if needed (junior → senior)
   - Document Last_Review_Date for all roles

2. **Complete Role Accuracy Assessment**:

   - For EVERY role: Sample 10-20 users
   - Compare role definition vs. actual access
   - Calculate role accuracy score: (Correct access / Sampled) × 100
   - Target: >= 95% role accuracy
   - Remediate all role drift

3. **SoD Matrix Review** (Sheet 5):

   - Review SoD matrix with security team and internal audit
   - Identify new conflicts (business changes, new systems)
   - Update risk levels (fraud risk changed?)
   - Document new mitigation controls
   - Validate with regulatory requirements (FINMA, SOX, etc.)

4. **RBAC Maturity Strategic Plan**:

   - Review RBAC Maturity trend (Sheet 7): Improving? Stagnant?
   - If Maturity < 80: Create 12-month improvement plan
   - Target: RBAC adoption >= 90%, SoD violations = 0, Role Review = 100%
   - Identify technology investments (IAM platforms, role mining)
   - Document strategic plan in Gap Analysis

5. **Audit Preparation**:

   - Ensure all evidence collected (Sheet 9)
   - Verify evidence accessible (SharePoint, not laptops)
   - Confirm approvals up to date (CISO sign-off)
   - Prepare executive summary (one-page RBAC maturity overview)

**Time Required**: 8-12 hours

---

## Integration Points

### Data Dependencies

**Inputs from Other Assessments**:
1. **From ISMS-IMP-A.5.15-16-18.S1 (User Inventory)**:

   - Total user count (for RBAC adoption denominator)
   - User status (active/inactive)
   - User type (employee/contractor)

2. **From ISMS-IMP-A.5.15-16-18.S2 (Access Rights Matrix)**:

   - Actual user access (for role accuracy validation)
   - System-level access (Read/Write/Admin)
   - Direct access identification

3. **From ISMS-IMP-A.5.15-16-18.S3 (Access Review Results)**:

   - Role review dates (when roles last validated)
   - Review findings (role accuracy)
   - Role owner sign-offs

**Outputs to Other Assessments**:
1. **To ISMS-IMP-A.5.15-16-18.S5 (IAM Governance Dashboard)**:

   - RBAC Adoption Rate (%)
   - SoD Violation Count (Unresolved, Justified, Remediated)
   - Role Review Compliance (%)
   - Overall RBAC Maturity Score (0-100)
   - Critical Gaps (Unresolved SoD, Low RBAC Adoption)

2. **To ISMS-IMP-A.5.15-16-18.S3 (Access Review Results)**:

   - Role definitions (baseline for role-based reviews)
   - Role owners (who reviews role assignments)
   - Role-based review scope (review by role vs. individual users)

### Cross-Reference Formulas

**Example: Role Catalog Sheet 2 references Role Assignments Sheet 3**:
```
=COUNTIF(Role_Assignments!C:C, B2)
```
This formula in Sheet 2, Column G (Users_Assigned) counts how many times the role name (B2) appears in Sheet 3, Column C (Role_Name).

**Example: RBAC Metrics Sheet 7 references multiple sheets**:
```
Total Users = Role_Assignments!A207 + Direct_Access_Users!A43
```
This formula combines user counts from Sheet 3 (Role Assignments) and Sheet 4 (Direct Access Users).

---

**END OF SPECIFICATION**

---

*"It doesn't matter how beautiful your theory is, it doesn't matter how smart you are. If it doesn't agree with experiment, it's wrong."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
