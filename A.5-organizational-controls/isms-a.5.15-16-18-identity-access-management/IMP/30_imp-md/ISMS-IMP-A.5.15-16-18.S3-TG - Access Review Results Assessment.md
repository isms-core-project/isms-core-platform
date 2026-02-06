**ISMS-IMP-A.5.15-16-18.S3-TG - Access Review Results Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Access Review Results & Recertification Compliance |
| **Related Policy** | ISMS-POL-A.5.15-16-18, Section 2.3.4 (Access Review and Recertification Requirements) |
| **Purpose** | Document access review execution, track review completion rates, assess reviewer accountability, and verify access removal for findings in a technology-agnostic manner |
| **Target Audience** | Managers, System Owners, Security Team, IAM Team, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Quarterly (review cycle completion), Monthly (tracking progress) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Access Review Results assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.15-16-18.S3-UG.

---

# Technical Specification

## Workbook Structure

### Sheet 1: Instructions_and_Legend

#### Header Section

- **Title:** "ISMS-IMP-A.5.15-16-18.S3 – Access Review Results Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Controls A.5.15 & A.5.18: Access Control & Access Rights"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block (Rows 3-12)
```
Document ID:           ISMS-IMP-A.5.15-16-18.S3
Assessment Area:       Access Review Results & Recertification Compliance
Related Policy:        ISMS-POL-A.5.15-16-18, Section 2.3.4 (Access Review Requirements)
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Period:         [USER INPUT - e.g., "Q1 2026", "H1 2026", "Annual 2025"]
Review Cycle:          Quarterly (critical systems), Semi-Annual (high), Annual (standard)
```

#### How to Use This Workbook (Rows 14-24)
1. **Sheet 1 - Instructions & Legend:** Usage guidance and review standards
2. **Sheet 2 - Review_Schedule:** Planned reviews by system/period (80 scheduled reviews)
3. **Sheet 3 - Review_Execution:** Review completion tracking by cycle
4. **Sheet 4 - Review_Findings:** Access decisions and changes (60 findings)
5. **Sheet 5 - Reviewer_Accountability:** Reviewer participation metrics (20 reviewers)
6. **Sheet 6 - Overdue_Reviews:** Reviews past due date (15 overdue items)
7. **Sheet 7 - Remediation_Tracking:** Access removal/change implementation tracking
8. **Sheet 8 - Coverage_Metrics:** System coverage and completion rates
9. **Sheet 9 - Gap_Analysis:** Review process gaps and improvement actions
10. **Sheet 10 - Evidence_Register:** Evidence collection for A.5.15/A.5.18 compliance
11. **Sheet 11 - Approval_Sign_Off:** Three-level approval workflow

#### Status Legend (Rows 26-34)
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Completed / On-Time | Review completed on time, removal executed ≤5 days | Green (C6EFCE) |
| ⚠️ | In Progress / Late | Review in progress or removal executed 6-10 days | Yellow (FFEB9C) |
| ❌ | Overdue / Very Late | Review not completed or removal executed >10 days | Red (FFC7CE) |
| 🚨 | CRITICAL | Privileged access review not completed or removal not executed | Dark Red (FF0000) |
| ℹ️ | Not Started | Review not yet started | Blue (B4C7E7) |
| N/A | Not Applicable | Not in scope for this review cycle | Gray (D3D3D3) |

---
## Sheet 2: Review_Schedule

### Purpose
Planned access reviews by system and review period.

### Header Section (Rows 1-4)

- **Row 1:** "Access Review Schedule" (merged, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 3:** Scheduled Reviews count (italic)
- **Row 5:** Column headers

### Column Definitions (Row 5+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | System ID | 12 | Unique system identifier |
| B | System Name | 30 | System/application name |
| C | System Criticality | 15 | Critical, High, Medium, Low |
| D | Review Frequency | 18 | Quarterly, Semi-Annual, Annual, Biennial |
| E | Last Review Date | 15 | Date of previous review |
| F | Next Review Due | 15 | Scheduled review date |
| G | Review Owner | 20 | Manager/system owner responsible |
| H | Status | 15 | Scheduled, In Progress, Completed, Overdue |

### Sample Data

Generator pre-populates 80 scheduled reviews.

---

## Sheet 3: Review_Execution

### Purpose
Track review completion by cycle with reviewer accountability.

### Header Section (Rows 1-4)

- **Row 1:** "Review Execution Tracking" (merged, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 5:** Column headers

### Column Definitions (Row 5+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Review ID | 12 | Unique review identifier |
| B | System Name | 30 | System being reviewed |
| C | Review Period | 15 | Q1 2026, H1 2026, etc. |
| D | Reviewer | 20 | Person conducting review |
| E | Assigned Date | 15 | When review was assigned |
| F | Due Date | 15 | Review deadline |
| G | Completed Date | 15 | Actual completion date |
| H | Days to Complete | 12 | Days from assigned to completed |
| I | Status | 15 | Completed, Overdue, In Progress, Not Started |
| J | Users Reviewed | 12 | Number of user access records reviewed |

---

## Sheet 4: Review_Findings

### Purpose
Document access decisions and changes resulting from reviews.

### Header Section (Rows 1-4)

- **Row 1:** "Access Review Findings" (merged, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 3:** Findings count (italic)
- **Row 5:** Column headers

### Column Definitions (Row 5+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Finding ID | 12 | Unique finding identifier |
| B | Review ID | 12 | Link to Review_Execution |
| C | User ID | 12 | User whose access was reviewed |
| D | Username | 18 | User login name |
| E | System | 25 | System/application |
| F | Access Level | 15 | Current access level |
| G | Decision | 18 | Confirm, Remove, Modify, Justify |
| H | Justification | 40 | Reason for decision |
| I | Reviewer | 20 | Person who made decision |
| J | Decision Date | 15 | When decision was made |
| K | Implementation Status | 18 | Pending, Implemented, Verified |

### Sample Data

Generator pre-populates 60 review findings.

---

## Sheet 5: Reviewer_Accountability

### Purpose
Track reviewer participation and response metrics.

### Header Section (Rows 1-4)

- **Row 1:** "Reviewer Accountability Metrics" (merged, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 5:** Column headers

### Column Definitions (Row 5+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Reviewer ID | 12 | Unique reviewer identifier |
| B | Reviewer Name | 25 | Full name |
| C | Department | 18 | Reviewer's department |
| D | Role | 20 | Manager, System Owner, Security |
| E | Reviews Assigned | 15 | Total reviews assigned |
| F | Reviews Completed | 15 | Number completed |
| G | Reviews Overdue | 15 | Number past due |
| H | Completion Rate | 15 | Percentage completed |
| I | Avg Response Time | 18 | Average days to complete |
| J | Status | 15 | Compliant, At Risk, Non-Compliant |

### Sample Data

Generator pre-populates 20 reviewers.

---

## Sheet 6: Overdue_Reviews

### Purpose
Track reviews past their due date requiring escalation.

### Header Section (Rows 1-4)

- **Row 1:** "Overdue Reviews - Escalation Required" (merged, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 3:** Overdue count (bold red)
- **Row 5:** Column headers

### Column Definitions (Row 5+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Review ID | 12 | Unique review identifier |
| B | System Name | 30 | System with overdue review |
| C | Criticality | 15 | System criticality level |
| D | Due Date | 15 | Original due date |
| E | Days Overdue | 12 | Number of days past due |
| F | Assigned Reviewer | 20 | Original reviewer |
| G | Escalation Level | 15 | Level 1, Level 2, Level 3 |
| H | Escalated To | 20 | Person escalated to |
| I | Escalation Date | 15 | When escalation occurred |
| J | New Due Date | 15 | Revised deadline |
| K | Status | 15 | Escalated, Resolved, Critical |

### Sample Data

Generator pre-populates 15 overdue reviews.

---

## Sheet 7: Remediation_Tracking

### Purpose
Track access removal/change implementation from review decisions.

### Header Section (Rows 1-4)

- **Row 1:** "Access Remediation Tracking" (merged, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 5:** Column headers

### Column Definitions (Row 5+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Remediation ID | 12 | Unique identifier |
| B | Finding ID | 12 | Link to Review_Findings |
| C | User | 20 | Affected user |
| D | System | 25 | System to modify |
| E | Action Required | 20 | Remove, Modify, Disable |
| F | Decision Date | 15 | When removal decided |
| G | Target Date | 15 | SLA deadline |
| H | Completed Date | 15 | Actual completion |
| I | Days to Implement | 12 | Decision to implementation |
| J | Implemented By | 20 | IT/IAM team member |
| K | Verification Status | 18 | Verified, Pending, Failed |
| L | Status | 15 | Completed, Overdue, In Progress |

---

## Sheet 8: Coverage_Metrics

### Purpose
System coverage and review completion rate statistics.

### Header Section (Rows 1-4)

- **Row 1:** "Access Review Coverage Metrics" (merged, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 5:** Column headers

### Column Definitions (Row 5+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Metric Category | 25 | Category name |
| B | Metric Name | 35 | Specific metric |
| C | Value | 15 | Metric value |
| D | Target | 15 | Target value |
| E | Status | 15 | Met, At Risk, Not Met |
| F | Notes | 40 | Additional context |

### Standard Metrics

- Total Systems in Scope
- Systems Reviewed This Period
- Coverage Rate
- On-Time Completion Rate
- Average Review Duration
- Reviews by Criticality

---

## Sheet 9: Gap_Analysis

### Purpose
Review process gaps and improvement actions.

### Header Section (Rows 1-4)

- **Row 1:** "Access Review Gap Analysis" (merged, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 5:** Column headers

### Column Definitions (Row 5+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Gap ID | 10 | Unique identifier (GAP-001) |
| B | Category | 18 | Coverage, Timeliness, Quality, Process |
| C | Description | 45 | What is the gap? |
| D | Risk Level | 12 | Critical, High, Medium, Low |
| E | Affected Items | 15 | Count or scope |
| F | Root Cause | 35 | Why did this happen? |
| G | Remediation Plan | 40 | What action will fix this? |
| H | Owner | 18 | Who is responsible? |
| I | Due Date | 12 | Target resolution date |
| J | Status | 15 | Open, In Progress, Closed |

### Sample Data

Generator pre-populates 30 gaps.

---

## Sheet 10: Evidence_Register

### Purpose
Evidence collection for A.5.15/A.5.18 access review compliance.

### Header Section (Rows 1-4)

- **Row 1:** "Evidence Register - Access Reviews" (merged, title style)
- **Row 2:** Evidence Collection Date metadata (italic)
- **Row 5:** Column headers

### Column Definitions (Row 5+)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Evidence ID | 12 | Unique identifier (EV-001) |
| B | Requirement | 25 | A.5.15/A.5.18 requirement |
| C | Evidence Type | 20 | Spreadsheet, Report, Screenshot, etc. |
| D | Evidence Location | 35 | File path, sheet reference, URL |
| E | Collection Date | 18 | Date evidence was collected |
| F | Completeness | 15 | Complete, Partial, Missing |
| G | Reviewed By | 20 | Who verified the evidence? |
| H | Notes | 40 | Additional context |

### Sample Data

Generator pre-populates 50 evidence items.

---

## Sheet 11: Approval_Sign_Off

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

(Same as previous IMPs - consistent styling)

---

## Freeze Panes

- All sheets: Freeze at A4

---

## File Naming Convention

**Format:** `ISMS-IMP-A.5.15-16-18.S3_Access_Review_Results_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.5.15-16-18.S3_Access_Review_Results_Q1-2026.xlsx`

---

## Quarterly Review Cycle

1. **Define Scope** (Sheet 2)
2. **Assign Reviewers** (Sheet 3)
3. **Track Completion** (Sheet 4) - daily/weekly updates
4. **Collect Findings** (Sheet 5)
5. **Execute Removals** (Sheet 6)
6. **Calculate Compliance** (Sheet 7)
7. **Identify Gaps** (Sheet 8)
8. **Register Evidence** (Sheet 9)
9. **Obtain Approval** (Sheet 10)

**Time:** 10-15 hours per quarter

---

## Integration Points

**A.5.15-16-18.2 - Access Rights Matrix:**

- **Input FROM IMP.2:** Access matrix defines WHAT to review

**A.5.15-16-18.1 - User Inventory:**

- **Input FROM IMP.1:** User and manager data

**A.5.15-16-18.5 - IAM Governance Dashboard:**

- **Input FROM this workbook:** Review metrics (Sheet 7)

---

**END OF SPECIFICATION**

---

*"Study hard what interests you the most in the most undisciplined, irreverent and original manner possible."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
