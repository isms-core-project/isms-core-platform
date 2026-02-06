**ISMS-IMP-A.5.15-16-18.S6-TG - IAM Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.5.15, A.5.16, A.5.18: Identity and Access Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S6-TG |
| **Version** | 1.0 |
| **Assessment Area** | IAM Governance Compliance Dashboard - Consolidated Metrics |
| **Related Policy** | ISMS-POL-A.5.15-16-18 (All Sections) |
| **Purpose** | Provide consolidated executive dashboard for IAM compliance across all assessment domains (S1-S5), enabling governance oversight, audit readiness, and continuous improvement tracking |
| **Target Audience** | CISO, Security Management, Internal Audit, Executive Leadership, Board/Audit Committee, External Auditors |
| **Assessment Type** | Executive Dashboard & Governance Reporting |
| **Review Cycle** | Monthly (metric refresh), Quarterly (executive review), Annually (comprehensive audit) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for IAM Compliance Dashboard - consolidates S1-S5 metrics | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.15-16-18.S6-UG.

---

# Technical Specification

## Workbook Structure

### Workbook Metadata

| Attribute | Value |
|-----------|-------|
| **Filename** | ISMS-IMP-A.5.15-16-18.S6_IAM_Compliance_Dashboard_YYYYMMDD.xlsx |
| **Total Sheets** | 9 |
| **File Format** | Excel Workbook (.xlsx) |
| **Excel Version** | Excel 2016 or later |
| **Macros** | None (formulas only) |
| **External Links** | None |

### Sheet Overview

| Sheet # | Sheet Name | Purpose | Rows (Est.) |
|---------|-----------|---------|-------------|
| 1 | Instructions & Legend | Usage guidance and dashboard overview | 60 |
| 2 | Executive_Summary | One-page IAM compliance overview | 40 |
| 3 | Domain_Compliance | Individual S1-S5 domain scores | 25 |
| 4 | Gap_Analysis | Consolidated gap register from S1-S5 | 50 |
| 5 | KPI_Dashboard | Key performance indicators with RAG status | 30 |
| 6 | Evidence_Summary | Consolidated evidence register | 50 |
| 7 | Trend_Analysis | Historical compliance tracking | 25 |
| 8 | Certification_Readiness | ISO 27001 audit readiness | 20 |
| 9 | Approval_Sign_Off | Three-level approval workflow | 15 |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions & Legend

**Purpose:** Usage guidance, field definitions, status legends

**Header Section (Rows 1-2):**

- **Row 1:** "ISMS-IMP-A.5.15-16-18.S6 - IAM Compliance Dashboard" (merged A1:H1, title style)
- **Row 1 (cont.):** "ISO/IEC 27001:2022 - Controls A.5.15, A.5.16, A.5.18" (second line)
- **Row 2:** Document metadata (italic)

**Document Information Block (Rows 4-12):**
```
Document ID:           ISMS-IMP-A.5.15-16-18.S6
Assessment Area:       IAM Governance Compliance Dashboard
Related Policy:        ISMS-POL-A.5.15-16-18 (All Sections)
Version:               1.0
Dashboard Date:        [USER INPUT - yellow cell]
Prepared By:           [USER INPUT - yellow cell]
Organisation:          [USER INPUT - yellow cell]
Assessment Period:     [USER INPUT - e.g., "January 2026"]
Review Cycle:          Monthly (metrics), Quarterly (executive), Annually (audit)
```

**Source Assessments Section (Rows 14-22):**

| Assessment | Document ID | Last Updated | Status |
|------------|-------------|--------------|--------|
| User Inventory & Lifecycle | S1 | [Date] | [Current/Stale] |
| Access Rights Matrix | S2 | [Date] | [Current/Stale] |
| Access Review Results | S3 | [Date] | [Current/Stale] |
| Role Definition & SoD | S4 | [Date] | [Current/Stale] |
| Lifecycle Compliance | S5 | [Date] | [Current/Stale] |

**Status Legend (Rows 24-32):**

| Status | Description | Colour Code |
|--------|-------------|-------------|
| Compliant | Meets or exceeds target (>= 85%) | Green (C6EFCE) |
| Warning | Below target but acceptable (60-84%) | Yellow (FFEB9C) |
| Non-Compliant | Significantly below target (< 60%) | Red (FFC7CE) |
| Critical | Immediate action required | Dark Red (FF0000) |
| N/A | Not assessed or not applicable | Grey (D3D3D3) |

**Maturity Level Legend (Rows 34-42):**

| Level | Score Range | Description |
|-------|-------------|-------------|
| Optimised | 90-100% | Best-in-class, continuous improvement |
| Managed | 75-89% | Strong controls, minor gaps |
| Defined | 60-74% | Documented processes, significant gaps |
| Developing | 40-59% | Basic controls, major gaps |
| Initial | < 40% | Ad-hoc processes, critical gaps |

---

### Sheet 2: Executive_Summary

**Purpose:** One-page IAM compliance overview for executive leadership

**Header Section (Rows 1-3):**

- **Row 1:** "Executive Summary - IAM Compliance Dashboard" (merged A1:G1, title style)
- **Row 2:** Dashboard Date metadata (italic)
- **Row 3:** Assessment Period metadata (italic)

**Composite Score Section (Rows 5-10):**

- **Row 5:** "Overall IAM Compliance Score" (subheader)
- **Row 6:** Large score display (e.g., "82%") with conditional formatting
- **Row 7:** Maturity Level (e.g., "Managed")
- **Row 8:** Score calculation formula reference
- **Row 9:** Previous period score (for trend)
- **Row 10:** Trend indicator (Improving/Stable/Declining)

**Domain Score Summary (Rows 12-20):**

| Domain | Score | Target | Status | Trend |
|--------|-------|--------|--------|-------|
| S1: User Inventory & Lifecycle | [%] | 85% | [RAG] | [Arrow] |
| S2: Access Rights Matrix | [%] | 85% | [RAG] | [Arrow] |
| S3: Access Review Results | [%] | 85% | [RAG] | [Arrow] |
| S4: Role Definition & SoD | [%] | 85% | [RAG] | [Arrow] |
| S5: Lifecycle Compliance | [%] | 85% | [RAG] | [Arrow] |

**Key Findings Section (Rows 22-30):**

- **Strengths:** Top 3 areas of compliance
- **Weaknesses:** Top 3 areas requiring attention
- **Critical Gaps:** Gaps requiring immediate action

**Recommendations Section (Rows 32-38):**

- Priority 1: Critical/High risk actions
- Priority 2: Medium risk actions
- Strategic: Long-term improvements

**Certification Readiness (Row 40):**

- Status: Ready / Mostly Ready / Not Ready
- Next Audit Date: [Date]
- Audit Blockers: [Count]

---

### Sheet 3: Domain_Compliance

**Purpose:** Individual compliance scores for each assessment domain

**Header Section (Rows 1-3):**

- **Row 1:** "Domain Compliance Scores - S1 through S5" (merged A1:I1, title style)
- **Row 2:** Assessment Period metadata (italic)
- **Row 4:** Column headers

**Column Structure (Row 4+):**

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Domain ID | 10 | S1, S2, S3, S4, S5 |
| B | Domain Name | 30 | Full assessment name |
| C | Score | 10 | Compliance percentage |
| D | Target | 10 | Target percentage |
| E | Gap | 10 | Target - Actual |
| F | Status | 15 | Compliant, Warning, Non-Compliant |
| G | Trend | 15 | Improving, Stable, Declining |
| H | Key Metrics | 40 | Summary of contributing metrics |
| I | Findings Summary | 50 | Key findings from assessment |

**Sample Data:**

| Domain ID | Domain Name | Score | Target | Gap | Status | Trend |
|-----------|-------------|-------|--------|-----|--------|-------|
| S1 | User Inventory & Lifecycle | 85% | 85% | 0% | Compliant | Stable |
| S2 | Access Rights Matrix | 78% | 85% | -7% | Warning | Improving |
| S3 | Access Review Results | 92% | 85% | +7% | Compliant | Improving |
| S4 | Role Definition & SoD | 72% | 85% | -13% | Warning | Stable |
| S5 | Lifecycle Compliance | 81% | 85% | -4% | Warning | Improving |

**Conditional Formatting:**

- Column F (Status): Green = Compliant, Yellow = Warning, Red = Non-Compliant

---

### Sheet 4: Gap_Analysis

**Purpose:** Consolidated gap register from all S1-S5 assessments

**Header Section (Rows 1-3):**

- **Row 1:** "Consolidated Gap Analysis - All IAM Domains" (merged A1:L1, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 3:** Total Gaps count (bold)
- **Row 5:** Column headers

**Column Structure (Row 5+):**

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Gap ID | 12 | Unique identifier (GAP-001) |
| B | Source | 8 | S1, S2, S3, S4, or S5 |
| C | Category | 20 | Gap category |
| D | Description | 45 | Gap description |
| E | Risk Level | 12 | Critical, High, Medium, Low |
| F | Affected Items | 15 | Count of affected users/items |
| G | Root Cause | 35 | Why did this happen? |
| H | Remediation Plan | 40 | What action will fix this? |
| I | Owner | 18 | Who is responsible? |
| J | Due Date | 12 | Target resolution date |
| K | Status | 15 | Open, In Progress, Closed |
| L | Notes | 30 | Progress notes |

**Gap Summary Metrics (Row 3):**

- Total Gaps: [Count]
- Critical: [Count]
- High: [Count]
- Medium: [Count]
- Low: [Count]
- Closed This Period: [Count]

**Conditional Formatting:**

- Column E (Risk Level): Dark Red = Critical, Red = High, Yellow = Medium, Green = Low
- Column K (Status): Red = Open, Yellow = In Progress, Green = Closed

---

### Sheet 5: KPI_Dashboard

**Purpose:** Key performance indicators with targets, actuals, and RAG status

**Header Section (Rows 1-3):**

- **Row 1:** "IAM Key Performance Indicators (KPIs)" (merged A1:H1, title style)
- **Row 2:** Assessment Period metadata (italic)
- **Row 4:** Column headers

**Column Structure (Row 4+):**

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | KPI ID | 10 | Unique identifier |
| B | KPI Name | 35 | Performance indicator name |
| C | Target | 12 | Target threshold |
| D | Actual | 12 | Current performance |
| E | Gap | 10 | Difference from target |
| F | Status | 15 | Compliant, Warning, Non-Compliant |
| G | Trend | 12 | Improving, Stable, Declining |
| H | Source | 15 | Source assessment (S1-S5) |

**Standard KPIs:**

| KPI ID | KPI Name | Target | Source |
|--------|----------|--------|--------|
| KPI-001 | User Inventory Completeness | 100% | S1 |
| KPI-002 | Provisioning On-Time Rate | >= 95% | S1, S5 |
| KPI-003 | Deprovisioning On-Time Rate | >= 98% | S1, S5 |
| KPI-004 | Orphaned Account Percentage | <= 1% | S1 |
| KPI-005 | Access Documentation Completeness | >= 90% | S2 |
| KPI-006 | Privileged Access Reviewed | 100% | S2, S3 |
| KPI-007 | Access Review Completion Rate | >= 95% | S3 |
| KPI-008 | RBAC Adoption Rate | >= 80% | S4 |
| KPI-009 | Open SoD Violations | 0 | S4 |
| KPI-010 | Contractor Expiration Compliance | 100% | S5 |

**Conditional Formatting:**

- Column F (Status): Green = Compliant, Yellow = Warning, Red = Non-Compliant

---

### Sheet 6: Evidence_Summary

**Purpose:** Consolidated evidence register for audit readiness

**Header Section (Rows 1-3):**

- **Row 1:** "Evidence Summary - ISO 27001 A.5.15/A.5.16/A.5.18" (merged A1:I1, title style)
- **Row 2:** Evidence Collection Date metadata (italic)
- **Row 4:** Column headers

**Column Structure (Row 4+):**

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Evidence ID | 12 | Unique identifier (EV-001) |
| B | Source | 8 | S1, S2, S3, S4, or S5 |
| C | ISO Requirement | 15 | A.5.15, A.5.16, or A.5.18 |
| D | Requirement Area | 25 | Specific requirement |
| E | Evidence Type | 20 | Spreadsheet, Policy, Process Records |
| F | Evidence Location | 35 | File path, sheet reference, URL |
| G | Collection Date | 15 | Date evidence was collected |
| H | Completeness | 15 | Complete, Partial, Missing |
| I | Verified By | 20 | Who verified the evidence |

**Evidence Summary Metrics:**

- Total Evidence Items: [Count]
- Complete: [Count] ([%])
- Partial: [Count] ([%])
- Missing: [Count] ([%])
- Evidence Completeness Score: [%]

**Conditional Formatting:**

- Column H (Completeness): Green = Complete, Yellow = Partial, Red = Missing

---

### Sheet 7: Trend_Analysis

**Purpose:** Historical compliance tracking and trajectory projection

**Header Section (Rows 1-3):**

- **Row 1:** "Trend Analysis - IAM Compliance Trajectory" (merged A1:G1, title style)
- **Row 2:** Analysis Period metadata (italic)
- **Row 4:** Section header "Historical Composite Scores"
- **Row 5:** Column headers

**Historical Data Table (Rows 5+):**

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Period | 15 | Month/Quarter |
| B | Composite Score | 15 | Overall IAM score |
| C | S1 Score | 12 | User Inventory |
| D | S2 Score | 12 | Access Rights |
| E | S3 Score | 12 | Access Review |
| F | S4 Score | 12 | Role & SoD |
| G | S5 Score | 12 | Lifecycle |

**Trend Summary Section (Rows 15-20):**

- Current Period Score: [%]
- Previous Period Score: [%]
- Month-over-Month Change: [+/- %]
- Quarter-over-Quarter Change: [+/- %]
- Trend Direction: Improving / Stable / Declining
- Projected Target Achievement: [Date] (at current rate)

---

### Sheet 8: Certification_Readiness

**Purpose:** ISO 27001 audit readiness assessment

**Header Section (Rows 1-3):**

- **Row 1:** "Certification Readiness - ISO 27001 Audit Preparation" (merged A1:G1, title style)
- **Row 2:** Assessment Date metadata (italic)
- **Row 4:** Column headers

**Control Assessment Table (Rows 4+):**

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Control | 10 | A.5.15, A.5.16, A.5.18 |
| B | Control Name | 25 | Access Control, Identity Management, Access Rights |
| C | Source Assessments | 15 | Which S1-S5 provide evidence |
| D | Evidence Status | 15 | Complete, Partial, Missing |
| E | Gap Status | 15 | No Gaps, Minor Gaps, Major Gaps |
| F | Readiness | 15 | Ready, Mostly Ready, Not Ready |
| G | Audit Blockers | 35 | Issues that would cause non-conformity |

**Overall Readiness Section (Row 12):**

- **Overall Certification Readiness:** Ready / Mostly Ready / Not Ready
- **Next Scheduled Audit:** [Date]
- **Total Audit Blockers:** [Count]
- **Estimated Remediation Time:** [Days/Weeks]

**Conditional Formatting:**

- Column F (Readiness): Green = Ready, Yellow = Mostly Ready, Red = Not Ready

---

### Sheet 9: Approval_Sign_Off

**Purpose:** Three-level approval workflow for completed dashboard

**Header Section (Rows 1-2):**

- **Row 1:** "Dashboard Approval & Sign-Off" (merged A1:F1, title style)
- **Row 2:** Dashboard Date metadata (italic)

**Approval Table (Row 4+):**

**Subheader:** "3-Level Approval Process" (blue header)

| Column | Header | Width | Description |
|--------|--------|-------|-------------|
| A | Approval Level | 25 | Level 1, 2, 3 |
| B | Role | 20 | IAM Manager, Security Manager, CISO |
| C | Name | 25 | Approver name |
| D | Signature | 20 | User input |
| E | Date | 15 | Approval date |
| F | Status | 15 | Pending, Approved, Rejected |

**Approval Rows:**

| Approval Level | Role | Name | Signature | Date | Status |
|----------------|------|------|-----------|------|--------|
| Level 1: Prepared By | IAM Manager | [Name] | | | Pending |
| Level 2: Reviewed By | Security Manager | [Name] | | | Pending |
| Level 3: Approved By | CISO | [Name] | | | Pending |

**Distribution Section (Row 12):**

- Approved for Distribution: Yes / No
- Distribution Date: [Date]
- Distribution List: CISO, Security Management, Internal Audit, Executive Leadership

---

## Styling Standards

### Colour Scheme

| Style | Background | Font | Usage |
|-------|------------|------|-------|
| Title | Navy (#003366) | White, Bold, 16pt | Sheet titles |
| Header | Blue (#4472C4) | White, Bold, 14pt | Section headers |
| Subheader | Light Blue (#5B9BD5) | White, Bold, 11pt | Subsection headers |
| Column Header | Grey (#D9D9D9) | Black, Bold, 10pt | Column headers |
| Data | White | Black, 10pt | Data cells |
| Compliant | Green (#C6EFCE) | Dark Green (#006100), Bold | Compliant status |
| Warning | Yellow (#FFEB9C) | Dark Yellow (#9C5700), Bold | Warning status |
| Non-Compliant | Red (#FFC7CE) | Dark Red (#9C0006), Bold | Non-compliant status |
| Critical | Dark Red (#FF0000) | White, Bold | Critical items |

### Data Validation

**Status Fields:** Dropdown validation

- Domain_Compliance Column F: Compliant, Warning, Non-Compliant
- Gap_Analysis Column E: Critical, High, Medium, Low
- Gap_Analysis Column K: Open, In Progress, Closed
- KPI_Dashboard Column F: Compliant, Warning, Non-Compliant
- Evidence_Summary Column H: Complete, Partial, Missing
- Certification_Readiness Column F: Ready, Mostly Ready, Not Ready

**Trend Fields:** Dropdown validation

- Trend columns: Improving, Stable, Declining

---

## Formula Reference

### Composite Score Calculation

**Equal Weighting:**
```
= (S1_Score + S2_Score + S3_Score + S4_Score + S5_Score) / 5
```

**Risk-Weighted:**
```
= (S1_Score * 0.15) + (S2_Score * 0.25) + (S3_Score * 0.20) + (S4_Score * 0.15) + (S5_Score * 0.25)
```

### Gap Calculation

```
= Target - Actual
```

### Status Assignment

```
=IF(Score >= 85%, "Compliant", IF(Score >= 60%, "Warning", "Non-Compliant"))
```

### Evidence Completeness Score

```
= COUNTIF(Completeness, "Complete") / COUNT(Completeness)
```

---

## Freeze Panes

- **Sheet 2 (Executive_Summary):** No freeze (single page view)
- **Sheet 3 (Domain_Compliance):** Freeze at A5
- **Sheet 4 (Gap_Analysis):** Freeze at A6
- **Sheet 5 (KPI_Dashboard):** Freeze at A5
- **Sheet 6 (Evidence_Summary):** Freeze at A5
- **Sheet 7 (Trend_Analysis):** Freeze at A6
- **Sheet 8 (Certification_Readiness):** Freeze at A5
- **Sheet 9 (Approval_Sign_Off):** No freeze

---

## File Naming Convention

**Format:** `ISMS-IMP-A.5.15-16-18.S6_IAM_Compliance_Dashboard_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.5.15-16-18.S6_IAM_Compliance_Dashboard_20260203.xlsx`

---

## Monthly Refresh Cycle

1. **Verify source assessments current** (S1-S5 within 30 days)
2. **Extract metrics** from each source assessment
3. **Update Executive Summary** (composite score, findings)
4. **Update Domain Scores** (individual S1-S5 scores)
5. **Update Gap Register** (close completed, add new)
6. **Update KPI Dashboard** (current actuals)
7. **Update Evidence Summary** (new evidence)
8. **Update Trend Analysis** (add current period)
9. **Update Certification Readiness** (if audit approaching)
10. **Obtain approvals** and distribute

**Time:** 2-4 hours per month

---

## Integration Points

### Source Assessments

This dashboard consolidates data from:

| Assessment | Sheets Used | Key Metrics |
|------------|-------------|-------------|
| **S1** | Sheet 7 (Lifecycle_Metrics), Sheet 8 (Gap_Analysis), Sheet 9 (Evidence) | User counts, lifecycle SLAs, orphaned accounts |
| **S2** | Sheet 6 (Compliance_Dashboard), Sheet 8 (Gap_Analysis), Sheet 9 (Evidence) | Access documentation, privileged access |
| **S3** | Sheet 6 (Review_Metrics), Sheet 7 (Gap_Analysis), Sheet 8 (Evidence) | Review completion, attestation |
| **S4** | Sheet 6 (SoD_Dashboard), Sheet 7 (Gap_Analysis), Sheet 8 (Evidence) | RBAC adoption, SoD violations |
| **S5** | Sheet 7 (Timeliness_Metrics), Sheet 9 (Gap_Analysis), Sheet 10 (Evidence) | JML event compliance |

### Output Consumers

Dashboard data feeds into:

- **CISO Governance Reports:** Monthly/Quarterly executive reporting
- **Audit Committee Presentations:** Quarterly board updates
- **ISO 27001 Certification:** Audit evidence package
- **Risk Management:** IAM risk posture input

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
