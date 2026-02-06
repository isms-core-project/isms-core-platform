**ISMS-IMP-A.5.15-16-18.S2-TG - Access Rights Matrix Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Access Rights Matrix & Documentation |
| **Related Policy** | ISMS-POL-A.5.15-16-18, Section 2.3 (Access Rights Management Requirements - A.5.18) |
| **Purpose** | Document complete access rights matrix mapping users to systems/applications/data, assess access documentation completeness, and verify business justification in a technology-agnostic manner |
| **Target Audience** | IAM Team, System Owners, IT Operations, Security Team, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Monthly (access rights updates), Quarterly (comprehensive access audit) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Access Rights Matrix assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.15-16-18.S2-UG.

---

# Technical Specification

## Workbook Structure

### Sheet 1: Instructions_and_Legend

#### Header Section

- **Title:** "ISMS-IMP-A.5.15-16-18.S2 – Access Rights Matrix Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.5.18: Access Rights"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block (Rows 3-12)
```
Document ID:           ISMS-IMP-A.5.15-16-18.S2
Assessment Area:       Access Rights Matrix & Documentation
Related Policy:        ISMS-POL-A.5.15-16-18, Section 2.3 (A.5.18 - Access Rights)
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Assessment Period:     [USER INPUT - e.g., "Q1 2026"]
Review Cycle:          Monthly (access updates), Quarterly (comprehensive audit)
```

#### How to Use This Workbook (Rows 14-25)
1. **Sheet 1 - Instructions & Legend:** Usage guidance, field definitions, and status color legend
2. **Sheet 2 - Access_Matrix:** User-to-system access mapping with 150 sample mappings
3. **Sheet 3 - Role_Assignments:** RBAC role assignments (80 users with roles)
4. **Sheet 4 - Group_Memberships:** Detailed group membership documentation (100 groups)
5. **Sheet 5 - Privileged_Access:** Admin/elevated access tracking (25 privileged users)
6. **Sheet 6 - Access_Documentation:** Business justification completeness (150 access grants)
7. **Sheet 7 - Coverage_Analysis:** System-level access statistics and RBAC adoption
8. **Sheet 8 - Gap_Analysis:** Missing documentation and excessive access findings
9. **Sheet 9 - Evidence_Register:** Evidence collection for A.5.18 compliance
10. **Sheet 10 - Approval_Sign_Off:** Three-level approval workflow

#### Status Legend (Rows 27-35)
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Complete / Approved | Access fully documented with justification and approval | Green (C6EFCE) |
| ⚠️ | Partial | Access documented but missing some information (justification or approval) | Yellow (FFEB9C) |
| ❌ | Missing | Access exists but no documentation (justification, approval, review missing) | Red (FFC7CE) |
| 🚨 | CRITICAL | Privileged access without approval or access to Restricted data undocumented | Dark Red (FF0000) |
| ℹ️ | Under Review | Access documentation being collected or verified | Blue (B4C7E7) |
| N/A | Not Applicable | User does not have access to this system | Gray (D3D3D3) |

#### Access Level Legend (Rows 37-45)
| Access Level | Description | Examples |
|--------------|-------------|----------|
| **Read** | View-only access, no modification | View reports, read emails, browse files |
| **Write** | Create and modify content | Edit documents, create records, post messages |
| **Admin** | System administration, configuration | Manage settings, create users, configure workflows |
| **Privileged** | Elevated access (root, domain admin, database admin) | Domain Admin (AD), sysadmin (SQL), root (Linux) |

#### Data Sensitivity Legend (Rows 47-55)
| Sensitivity Level | Description | Examples | Access Requirements |
|-------------------|-------------|----------|---------------------|
| **Restricted** | Highest sensitivity, regulatory protection | PII/GDPR data, payment card data, trade secrets | CISO approval required |
| **Confidential** | High sensitivity, business impact if disclosed | Contracts, employee data, IP | System owner + manager approval |
| **Internal** | Moderate sensitivity, internal use only | Internal communications, operational data | Manager approval |
| **Public** | No sensitivity, publicly available | Marketing materials, published info | Standard approval |

---

## Sheet 2: Access_Matrix

### Purpose
User-to-system access mapping showing who has access to what systems with what access levels.

### Header Section (Rows 1-4)

- **Row 1:** "Access Rights Matrix - User × System Mapping" (merged A1:K1, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 3:** Access Mappings count (italic)
- **Row 5:** Column headers

### Column Definitions (Row 5+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | User ID | 10 | Unique user identifier (e.g., U10001) |
| B | Username | 18 | User login name (first.last format) |
| C | Full Name | 20 | User's full display name |
| D | Department | 15 | User's department |
| E | System/Application | 30 | System or application name |
| F | Access Level | 15 | Read, Read/Write, Admin, Full Control |
| G | Access Type | 15 | Direct, Role-Based, Group-Based |
| H | Granted Date | 12 | Date access was granted (DD.MM.YYYY) |
| I | Granted By | 18 | Who authorized the access |
| J | Last Used | 12 | Date of last access activity |
| K | Status | 15 | Active, Recently Used, Inactive, Never Used |

### Status Logic

- **Active:** Last used within 30 days (green)
- **Recently Used:** Last used 31-90 days ago (yellow)
- **Inactive:** Last used >90 days ago (red)
- **Never Used:** No recorded usage (red)

### Sample Data

Generator pre-populates 150 access mappings with sample data for assessment template.

---

## Sheet 3: Role_Assignments

### Purpose
RBAC role assignments tracking which users are assigned to which roles.

### Header Section (Rows 1-4)

- **Row 1:** "Role Assignments - RBAC Implementation" (merged A1:H1, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 3:** Users with Roles count (italic)
- **Row 5:** Column headers

### Column Definitions (Row 5+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | User ID | 10 | Unique user identifier |
| B | Username | 18 | User login name |
| C | Full Name | 20 | User's full display name |
| D | Department | 15 | User's department |
| E | Assigned Role | 25 | Role name assigned to user |
| F | Assignment Date | 15 | Date role was assigned (DD.MM.YYYY) |
| G | Assignment Type | 18 | Automatic, Manual, or Inherited |
| H | Status | 12 | Active status (green) |

### Sample Roles

Generator includes sample roles such as:
- Sales Representative, Sales Manager
- Finance Analyst, Finance Manager
- HR Generalist
- Software Developer, Engineering Manager
- IT Administrator, Security Analyst
- Standard User (basic employee access)

### Sample Data

Generator pre-populates 80 user role assignments.

---

## Sheet 4: Group_Memberships

### Purpose
Detailed group membership documentation across directory services.

### Header Section (Rows 1-3)

- **Row 1:** "Group Membership Details" (merged A1:J1, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 4:** Column headers

### Column Definitions (Row 4+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Group Name | 35 | Group name (SEC-*, ROLE-*, PROJECT-*) |
| B | Group Type | 15 | Security, Distribution, Role-Based, Project |
| C | Purpose | 40 | Description of group purpose |
| D | Owner | 18 | Department Manager responsible |
| E | Member Count | 15 | Number of members in group |
| F | Created Date | 15 | Date group was created |
| G | Last Modified | 15 | Date of last membership change |
| H | Nested Groups | 15 | Yes/No - contains other groups |
| I | Review Frequency | 18 | Quarterly, Annual, Biennial |
| J | Status | 12 | Active status (green)

### Sample Data

Generator pre-populates 100 groups with sample data.

---

## Sheet 5: Privileged_Access

### Purpose
Admin and elevated access tracking for high-risk accounts.

### Header Section (Rows 1-4)

- **Row 1:** "Privileged Access Tracking - Admin & Elevated Rights" (merged A1:K1, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 3:** Privileged Users count (bold red)
- **Row 5:** Column headers

### Column Definitions (Row 5+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | User ID | 10 | Unique user identifier |
| B | Username | 18 | User login name |
| C | Full Name | 20 | User's full display name |
| D | Department | 15 | User's department |
| E | System | 25 | System with privileged access |
| F | Privilege Level | 20 | Admin, Root, Domain Admin, etc. |
| G | Granted Date | 12 | Date privilege was granted |
| H | Business Justification | 35 | Why user needs privileged access |
| I | Approved By | 18 | CISO, IT Manager, Security Manager |
| J | Last Review | 12 | Date of last review |
| K | Status | 18 | Compliant, Review Due, Overdue Review |

### Status Logic

- **Compliant:** Review within 90 days (green)
- **Review Due:** Review 91-180 days ago (yellow)
- **Overdue Review:** Review >180 days ago (red)

### Sample Data

Generator pre-populates 25 privileged users.

---

## Sheet 6: Access_Documentation

### Purpose
Business justification completeness tracking for access grants.

### Header Section (Rows 1-3)

- **Row 1:** "Access Documentation Completeness - Business Justification" (merged A1:J1, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 4:** Column headers

### Column Definitions (Row 4+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Access ID | 12 | Unique access grant identifier |
| B | Username | 18 | User login name |
| C | System | 30 | System/Application name |
| D | Access Level | 15 | Read, Read/Write, Admin |
| E | Granted Date | 12 | Date access was granted |
| F | Business Justification | 50 | Why user needs access |
| G | Approver | 18 | Who approved the access |
| H | Approval Date | 15 | When access was approved |
| I | Documentation Quality | 20 | Complete, Incomplete, Missing |
| J | Status | 15 | Compliant, Warning, Non-Compliant |

### Documentation Quality Logic

- **Complete:** Full justification text (green)
- **Incomplete:** Justification <20 characters (yellow)
- **Missing:** No justification provided (red)

### Sample Data

Generator pre-populates 150 access documentation records.

---

## Sheet 7: Coverage_Analysis

### Purpose
System-level access statistics and RBAC adoption metrics.

### Header Section (Rows 1-3)

- **Row 1:** "Coverage Analysis - System-Level Access Statistics" (merged A1:H1, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 4:** Column headers

### Column Definitions (Row 4+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | System/Application | 30 | System name |
| B | Criticality | 15 | Critical, High, Medium, Low |
| C | Total Users | 12 | Number of users with access |
| D | Read Access | 15 | Users with read-only access |
| E | Write Access | 15 | Users with write access |
| F | Admin Access | 15 | Users with admin access |
| G | RBAC Adoption | 18 | Percentage using roles vs. direct |
| H | Review Frequency | 18 | Based on criticality |

### Review Frequency Logic

- **Critical:** Quarterly review
- **High:** Semi-Annual review
- **Medium/Low:** Annual review

---

## Sheet 8: Gap_Analysis

### Purpose
Access rights non-compliance findings and remediation tracking.

### Header Section (Rows 1-3)

- **Row 1:** "Gap Analysis - Access Rights Non-Compliance" (merged A1:J1, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 4:** Column headers

### Column Definitions (Row 4+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Gap ID | 10 | Unique identifier (GAP-001) |
| B | Category | 18 | Documentation, RBAC Adoption, Privileged Access, Unused Access, Group Management |
| C | Description | 45 | What is the gap? |
| D | Risk Level | 12 | Critical, High, Medium, Low |
| E | Affected Items | 15 | Count of affected users/items |
| F | Root Cause | 40 | Why did this happen? |
| G | Remediation Plan | 40 | What action will fix this? |
| H | Owner | 18 | Who is responsible? |
| I | Due Date | 12 | Target resolution date |
| J | Status | 15 | Open, In Progress, Closed |

### Sample Gaps

Generator pre-populates common findings:
- Missing business justification
- Direct access instead of RBAC
- Privileged accounts overdue for review
- Unused access (>90 days)
- Groups missing ownership documentation

---

## Sheet 9: Evidence_Register

### Purpose
Evidence collection for A.5.18 Access Rights compliance.

### Header Section (Rows 1-3)

- **Row 1:** "Evidence Register - A.5.18 Access Rights" (merged A1:H1, title style)
- **Row 2:** Evidence Collection Date metadata (italic)
- **Row 4:** Column headers

### Column Definitions (Row 4+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Evidence ID | 12 | Unique identifier (EV-001) |
| B | Requirement | 25 | What A.5.18 requirement? |
| C | Evidence Type | 20 | Spreadsheet, Process Records, Policy Document, etc. |
| D | Evidence Location | 35 | File path, sheet reference, URL |
| E | Collection Date | 18 | Date evidence was collected |
| F | Completeness | 15 | Complete, Partial, Missing |
| G | Reviewed By | 20 | Who verified the evidence? |
| H | Notes | 45 | Additional context |

### Sample Evidence Items

Generator pre-populates evidence references:
- Access Rights Matrix (this workbook)
- RBAC Implementation records
- Group Memberships documentation
- Privileged Access Tracking
- Access Request Policy
- Access Review Results

---

## Sheet 10: Approval_Sign_Off

### Purpose
Three-level approval workflow for completed assessment.

### Header Section (Rows 1-2)

- **Row 1:** "Assessment Approval & Sign-Off" (merged A1:F1, title style)
- **Row 2:** Assessment Date metadata (italic)

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

- **Main Header:** Font: Calibri 14pt bold white, Fill: 003366 (dark blue), Centered, 40px height
- **Subheader:** Font: Calibri 11pt bold white, Fill: 4472C4 (blue), Centered
- **Column Header:** Font: Calibri 10pt bold black, Fill: D9D9D9 (gray), Centered, Border: thin

### Input Cell Styles

- **Fill:** FFFFCC (light yellow) - user input required
- **Alignment:** Left for text, center for dropdowns, right for numbers
- **Border:** Thin black all sides
- **Protection:** Unlocked

### Formula/Calculated Cell Styles

- **Fill:** White (FFFFFF) or light gray (F2F2F2)
- **Alignment:** Right for numbers, left for text
- **Border:** Thin gray
- **Protection:** Locked

### Status Fill Colors

- **✅ Complete / Approved:** C6EFCE (green)
- **⚠️ Partial / Pending:** FFEB9C (yellow)
- **❌ Missing / Issues:** FFC7CE (red)
- **🚨 CRITICAL:** FF0000 (dark red)
- **ℹ️ Under Review:** B4C7E7 (blue)
- **N/A:** D3D3D3 (gray)

---

## Freeze Panes

- **Sheet 2 (System Inventory):** Freeze at A4
- **Sheet 3 (Access Matrix):** Freeze at A4
- **Sheet 4 (Group/Role Mapping):** Freeze at A4
- **Sheet 5 (Justification):** Freeze at A4
- **Sheet 6 (Excessive Access):** Freeze at A4
- **Sheet 7 (Dashboard):** Freeze at A5
- **Sheet 8 (Gap Analysis):** Freeze at A4
- **Sheet 9 (Evidence):** Freeze at A4
- **Sheet 10 (Approval):** Freeze at A3

---

## File Naming Convention

**Format:** `ISMS-IMP-A.5.15-16-18.S2_Access_Rights_Matrix_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.5.15-16-18.S2_Access_Rights_Matrix_20260122.xlsx`

---

## Monthly Review Cycle

1. **Update System Inventory (Sheet 2):** Add new systems, retire old systems
2. **Update Access Matrix (Sheet 3):** Add new access grants, remove leavers' access
3. **Update Group/Role Mapping (Sheet 4):** New groups, membership changes
4. **Update Justification Documentation (Sheet 5):** Collect justifications for new access
5. **Refresh Dashboard (Sheet 7):** Auto-updates from linked sheets
6. **Update Gap Analysis (Sheet 8):** Close resolved gaps, add new gaps
7. **Add Evidence (Sheet 9):** Current month documentation
8. **System Owner Sign-Off (Sheet 10):** Monthly verification

**Time:** 4-6 hours per month

---

## Integration Points

### Related Assessments

**A.5.15-16-18.1 - User Inventory & Lifecycle:**

- **Input FROM IMP.1:** User list (baseline for access matrix)

**A.5.15-16-18.3 - Access Review Results:**

- **Input FROM this workbook:** Access matrix defines WHAT to review

**A.5.15-16-18.4 - Role & SoD Compliance:**

- **Input FROM this workbook:** Access via roles for SoD detection

**A.5.15-16-18.5 - IAM Governance Dashboard:**

- **Input FROM this workbook:** Access metrics (Sheet 7)

---

**END OF SPECIFICATION**

---

*"For a successful technology, reality must take precedence over public relations, for Nature cannot be fooled."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
