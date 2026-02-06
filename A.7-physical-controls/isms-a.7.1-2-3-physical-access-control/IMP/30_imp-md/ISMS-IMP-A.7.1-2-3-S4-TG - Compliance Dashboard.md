**ISMS-IMP-A.7.1-2-3-S4-TG - Physical Access Control Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.7.1, A.7.2, A.7.3: Physical Access Control

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.1-2-3-S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Physical Access Control Compliance Consolidation - Executive Dashboard |
| **Related Policy** | ISMS-POL-A.7.1-2-3 (Physical Access Control) |
| **Purpose** | Consolidate perimeter, entry, and secure areas assessments into unified compliance dashboard |
| **Target Audience** | CISO, Security Management, Facilities Management, Compliance Officers, Auditors |
| **Assessment Type** | Executive Summary & Gap Analysis |
| **Review Cycle** | Quarterly or After Significant Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Physical Access Control Dashboard | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.1-2-3-S4-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.1.4_Compliance_Dashboard_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a71_4_compliance_dashboard.py)

**Sheet Count:** 6 worksheets

**Styling:** Navy blue headers, yellow input cells, conditional formatting for compliance status (green/amber/red)

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Dashboard metadata and guidance | Read-only Reference | ~30 rows |
| 2 | Executive Dashboard | Overall compliance and key metrics | Mixed (formula + input) | ~40 rows |
| 3 | Gap Analysis | Detailed gap identification | Data Entry | 100 data rows |
| 4 | KPIs & Metrics | Performance indicators | Data Entry | ~20 rows |
| 5 | Evidence Register | Consolidated evidence | Data Entry | 200 data rows |
| 6 | Approval & Sign-Off | Executive approval workflow | Data Entry | ~20 rows |

### Workbook Features

**Data Validation:**

- Dropdown lists for standardised input (Control, Severity, Status)
- Date validation (valid date format)

**Conditional Formatting:**

- Compliance scores: Green (90+), Amber (70-89), Red (<70)
- Gap severity: Red (Critical), Orange (High), Yellow (Medium)
- KPI status: Green (Met), Amber (Near), Red (Below)

**Formulas:**

- Overall compliance score calculated from control scores
- Gap counts derived from Gap Analysis sheet
- KPI status calculated from current vs target

**Freeze Panes:**

- Header rows frozen
- First column frozen for horizontal scrolling

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions & Legend

**Purpose:** Dashboard metadata and user guidance

**Content:**

- Document ID and version
- Assessment period
- Completed by
- Source assessment references
- Status legend
- Weighting methodology

### Sheet 2: Executive Dashboard

**Structure:**

| Row | Content | Type |
|-----|---------|------|
| 1-4 | Header with title and period | Static |
| 6-10 | Control Compliance Table | Mixed |
| 12-15 | Overall Compliance Score | Formula |
| 17-22 | Gap Counts by Severity | Formula |
| 24-30 | Key Metrics Summary | Formula |
| 32-35 | Trend Indicators | Input |

**Columns for Control Compliance:**

| Col | Field | Type |
|-----|-------|------|
| A | Control | Static (A.7.1, A.7.2, A.7.3) |
| B | Compliance Score | Input (from source) |
| C | Weight | Static |
| D | Weighted Score | Formula |
| E | Status | Formula (based on score) |
| F | Critical Gaps | Formula (from Sheet 3) |
| G | High Priority | Formula (from Sheet 3) |
| H | Medium Priority | Formula (from Sheet 3) |

### Sheet 3: Gap Analysis

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Gap ID | Text | 12 | None |
| B | Control | Dropdown | 10 | A.7.1/A.7.2/A.7.3 |
| C | Finding | Text | 40 | None |
| D | Severity | Dropdown | 12 | Critical/High/Medium |
| E | Impact | Text | 30 | None |
| F | Current State | Text | 30 | None |
| G | Required State | Text | 30 | None |
| H | Remediation Action | Text | 40 | None |
| I | Owner | Text | 25 | None |
| J | Target Date | Date | 12 | Date format |
| K | Status | Dropdown | 15 | Open/In Progress/Closed/Deferred |
| L | Notes | Text | 40 | None |

### Sheet 4: KPIs & Metrics

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | KPI | Text | 30 | None |
| B | Measurement | Text | 15 | None |
| C | Current | Text | 12 | None |
| D | Previous | Text | 12 | None |
| E | Target | Text | 12 | None |
| F | Status | Dropdown | 15 | Met/Near/Below Target |
| G | Trend | Dropdown | 15 | Improving/Stable/Declining |
| H | Notes | Text | 40 | None |

### Sheet 5: Evidence Register

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Evidence ID | Text | 12 | None |
| B | Control | Dropdown | 10 | A.7.1/A.7.2/A.7.3 |
| C | Source Assessment | Dropdown | 10 | S1/S2/S3 |
| D | Evidence Type | Dropdown | 18 | Floor plan/Photograph/Access log/etc. |
| E | Description | Text | 35 | None |
| F | Collection Date | Date | 12 | Date format |
| G | Collector | Text | 18 | None |
| H | Location/Link | Text | 50 | None |
| I | Status | Dropdown | 15 | Collected/Pending/Missing |

### Sheet 6: Approval & Sign-Off

**Structure:**

| Row | Content |
|-----|---------|
| 1-4 | Header with dashboard title and period |
| 6-8 | Assessment summary (overall score, gap count) |
| 10-25 | Approver table (5 rows) |

**Approver Table Columns:**

| Col | Field | Width |
|-----|-------|-------|
| A | Role | 25 |
| B | Name | 25 |
| C | Date | 12 |
| D | Status | 20 |
| E | Comments | 50 |

---

## Cell Styling Reference

### Colour Palette

**Headers:**

- Primary Header: #003366 (Navy blue), White text
- Column Header: #D9D9D9 (Light grey), Black text

**Data Cells:**

- Input Cell: #FFFFCC (Light yellow)
- Read-Only: White
- Calculated: #E2EFDA (Light green)

**Compliance Scores:**

- 90-100%: #C6EFCE (Green)
- 70-89%: #FFEB9C (Amber)
- Below 70%: #FFC7CE (Red)

**Gap Severity:**

- Critical: #FFC7CE (Light red)
- High: #FFCC99 (Light orange)
- Medium: #FFEB9C (Light amber)

**KPI Status:**

- Met: #C6EFCE (Green)
- Near: #FFEB9C (Amber)
- Below: #FFC7CE (Red)

---

## Integration Points

### Source Assessment Integration

| Source Assessment | Dashboard Component | Data Extracted |
|-------------------|---------------------|----------------|
| S1 - Perimeter Security | Sheet 2 Row A.7.1 | Compliance score |
| S1 - Perimeter Security | Sheet 3 | Gaps (Non-Compliant/Partial items) |
| S1 - Perimeter Security | Sheet 4 | Perimeter inspection KPI |
| S1 - Perimeter Security | Sheet 5 | Evidence items |
| S2 - Entry Control | Sheet 2 Row A.7.2 | Compliance score |
| S2 - Entry Control | Sheet 3 | Gaps |
| S2 - Entry Control | Sheet 4 | Entry control KPIs |
| S2 - Entry Control | Sheet 5 | Evidence items |
| S3 - Secure Areas | Sheet 2 Row A.7.3 | Compliance score |
| S3 - Secure Areas | Sheet 3 | Gaps |
| S3 - Secure Areas | Sheet 4 | Secure areas KPIs |
| S3 - Secure Areas | Sheet 5 | Evidence items |

### Audit Integration

This dashboard serves as the PRIMARY audit deliverable for physical access control. Package includes:

1. This dashboard workbook (S4)
2. S1 Perimeter Security workbook
3. S2 Entry Control workbook
4. S3 Secure Areas workbook
5. All evidence files referenced in evidence registers

### Policy Integration

| Policy Section | Dashboard Component |
|----------------|---------------------|
| ISMS-POL-A.7.1-2-3 Section 2.1 | A.7.1 compliance score |
| ISMS-POL-A.7.1-2-3 Section 2.2 | A.7.2 compliance score |
| ISMS-POL-A.7.1-2-3 Section 2.3 | A.7.3 compliance score |
| ISMS-POL-A.7.1-2-3 Appendix: KPIs | Sheet 4 targets |

### Related Control Integration

| Related Control | Integration Point |
|-----------------|-------------------|
| A.5.1-4 (ISMS Governance) | Dashboard feeds into ISMS management review |
| A.5.35-36 (Compliance & Review) | Dashboard evidence for compliance assessment |
| A.7.4-14 (Other Physical Controls) | May reference similar assessment methodology |

---

**END OF SPECIFICATION**

---

*"In security, the whole is only as strong as its weakest part. This dashboard reveals where those weaknesses lie."*
--- Security Management Principle

<!-- QA_VERIFIED: 2026-02-06 -->
