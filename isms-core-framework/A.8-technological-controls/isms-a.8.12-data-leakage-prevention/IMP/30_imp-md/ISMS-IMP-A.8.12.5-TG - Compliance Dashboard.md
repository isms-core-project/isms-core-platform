**ISMS-IMP-A.8.12.5-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention


---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.12.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | DLP Compliance Dashboard and Consolidated Reporting |
| **Related Policy** | ISMS-POL-A.8.12 (Data Leakage Prevention Policy) - All Sections |
| **Purpose** | Consolidate data from all DLP assessments (Infrastructure, Classification, Channel Coverage, Monitoring & Response) into unified executive dashboard for CISO reporting and audit readiness verification |
| **Target Audience** | CISO, DPO, Compliance Officers, Internal Audit, Executive Management, External Auditors |
| **Assessment Type** | Consolidation & Executive Reporting |
| **Review Cycle** | Quarterly (after all source assessments completed) |
| **Date** | 21.01.2026 |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Compliance Dashboard | ISMS Implementation Team |

---

# Technical Specification
**Audience:** Python Developers, Excel Workbook Developers, Quality Assurance, ISMS Implementation Team

---

# Workbook Structure Overview

## Sheet List

**Total Sheets:** 12

| # | Sheet Name | Rows (approx) | Purpose | User Input |
|---|------------|---------------|---------|------------|
| 1 | Instructions_Legend | 45 | User guidance, metadata | Metadata only |
| 2 | Executive_Summary | 50 | Board-ready summary, overall compliance | Manual summary text |
| 3 | Domain_Rollup_Summary | 40 | Compliance % by domain, KPIs | No (formulas) |
| 4 | Consolidated_Gap_Analysis | 60 | All critical gaps from 4 sources | No (formulas) |
| 5 | Risk_Register | 40 | DLP-related risk tracking | Yes (risk details) |
| 6 | Remediation_Roadmap | 45 | Remediation planning and tracking | Yes (roadmap items) |
| 7 | Evidence_Master_Index | 35 | Evidence count verification and index | No (formulas) |
| 8 | Trend_Analysis | 40 | Quarter-over-quarter comparison | Manual analysis |
| 9 | KPI_Dashboard | 35 | Key performance indicators dashboard | No (formulas) |
| 10 | Budget_Planning | 30 | DLP budget and resource planning | Yes (budget items) |
| 11 | CISO_DPO_Approval | 25 | Multi-level approval workflow | Yes (signatures) |
| 12 | Summary_Dashboard | 40 | Overall summary and status | No (formulas) |

**Total:** ~485 rows + external link formulas

---

# Detailed Sheet Specifications

## Sheet: Instructions_Legend

**Purpose:** User guidance and dashboard metadata

**Layout:**

- Rows 1-5: Document header
- Rows 7-14: Organization metadata (yellow cells)
- Rows 16-30: How to use dashboard
- Rows 32-40: External link troubleshooting guide
- Rows 42-45: Color coding legend

**Organization Metadata:**

| Row | Field | Type | Example |
|-----|-------|------|---------|
| 7 | Dashboard Period | Text | Q1 2026 |
| 8 | Dashboard Date | Date | 21.01.2026 |
| 9 | Prepared By | Text | Jane Doe |
| 10 | Role | Text | DLP Program Manager |
| 11 | Organization | Text | [Organization] |
| 12 | CISO | Text | John Smith |
| 13 | Next Review | Date | 21.04.2026 |
| 14 | Audit Date (if scheduled) | Date | 15.05.2026 |

---

## Sheet: Executive_Summary

**Purpose:** Board-ready executive summary with overall compliance status

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Metric | Text | 35 | None | Pre-populated |
| B | Value | Various | 20 | None | External link formula or manual |
| C | Target | Text | 15 | None | Policy target |
| D | Status | Dropdown | 12 | ✅/⚠️/❌ | Auto or manual |
| E | Trend | Text | 15 | None | +/- vs. previous quarter |
| F | Notes | Text (wrap) | 50 | None | Executive commentary |

**Pre-Populated Metrics (Rows 6-50):**

| Section | Metrics |
|---------|---------|
| **Overall Status** | Overall DLP Compliance %, Status, Trend vs. Q4 2025 |
| **Domain Compliance** | Infrastructure %, Classification %, Channel Coverage %, Monitoring & Response % |
| **Critical Metrics** | Total Critical Gaps, Total Evidence Items, Audit Readiness Status |
| **Key Findings** | DLP Infrastructure Status, Data Classification Maturity, Channel Coverage %, MTTR - Critical Alerts, False Positive Rate, SIEM Integration Status |
| **Executive Concerns** | Top 5 Critical Gaps (auto-populated from consolidated gaps) |
| **Resource Requirements** | Budget Needs, Staffing Needs, Tool Requirements |
| **Risk Acceptance** | Gaps Accepted, Gaps Remediation Required, Board Escalation Required |
| **Executive Summary Text** | Free-form summary (manual entry, 1-2 paragraphs) |

**Key External Link Formulas:**

```excel
# Overall DLP Compliance % (Cell B6)
=ROUND(
  ([ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25),
  0
)

# Infrastructure Compliance % (Cell B10)
=[ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx]Summary_Dashboard!$B$7

# Classification Compliance % (Cell B11)
=[ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Summary_Dashboard!$B$7

# Channel Coverage Compliance % (Cell B12)
=[ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx]Summary_Dashboard!$B$7

# Monitoring & Response Compliance % (Cell B13)
=[ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]Summary_Dashboard!$B$7

# Total Critical Gaps (Cell B16)
=[ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45 (COUNTIF "Critical") +
=[ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45 (COUNTIF "Critical") +
=[ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45 (COUNTIF "Critical") +
=[ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45 (COUNTIF "Critical")
```

**Conditional Formatting:**

```python
# Overall Compliance % (Cell B6)
compliance_format = {
    'green': ('>=', 90),   # Audit-ready
    'yellow': ('and', [('>=', 80), ('<', 90)]),  # Partially ready
    'red': ('<', 80)       # Not audit-ready
}

# Status (Column D)
status_format = {
    '✅ Compliant': 'green',
    '⚠️ Partial': 'yellow',
    '❌ Non-Compliant': 'red'
}
```

---

## Sheet: Consolidated_Metrics

**Purpose:** Detailed metrics consolidated from all 4 source assessments

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Metric Category | Text | 25 | None | Domain grouping |
| B | Metric Name | Text | 35 | None | Specific metric |
| C | Source | Text | 30 | None | Which assessment |
| D | Value | Various | 20 | None | External link formula |
| E | Target | Text | 15 | None | Policy target |
| F | Status | Auto | 12 | ✅/⚠️/❌ | Formula-driven |
| G | Notes | Text (wrap) | 40 | None | Context |

**Pre-Populated Metrics (Rows 6-40):**

**From A.8.12.1 Infrastructure:**

- DLP Technology Inventory Completeness (%)
- Network DLP Coverage (%)
- Endpoint DLP Coverage (%)
- Email DLP Coverage (%)
- Cloud DLP Coverage (%)

**From A.8.12.2 Classification:**

- Data Classification Scheme Maturity Level
- Sensitive Data Categories Inventoried (#)
- DLP Pattern Accuracy (%)
- False Positive Rate (%)

**From A.8.12.3 Channel Coverage:**

- Channels Fully Covered (#/7)
- Bypass Tests Passed (%)
- Shadow IT Channels Identified (#)
- Unprotected Restricted Data Channels (#)

**From A.8.12.4 Monitoring & Response:**

- Alert Backlog (#)
- MTTR - Critical Alerts (hours)
- SIEM Integration Status
- SOC Playbooks Documented (Yes/No)
- GDPR 72-Hour Compliance (%)

**External Link Formula Pattern:**

```excel
# Generic pattern for pulling metrics from source workbooks
=[SourceWorkbookName.xlsx]SheetName!$CellReference

# Example: DLP Pattern Accuracy from A.8.12.2
=[ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Summary_Dashboard!$B$15

# Example: MTTR Critical from A.8.12.4
=[ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]Summary_Dashboard!$B$12
```

---

## Sheet: Critical_Gaps_Consolidated

**Purpose:** Consolidate all critical gaps from 4 source Gap_Analysis sheets

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Gap ID | Text | 15 | From source (e.g., GAP-001) |
| B | Source Assessment | Text | 25 | Infrastructure/Classification/Coverage/Monitoring |
| C | Gap Description | Text (wrap) | 45 | From source Gap_Analysis |
| D | Current State | Text (wrap) | 30 | From source |
| E | Required State | Text (wrap) | 30 | From source |
| F | Risk Level | Text | 12 | Should all be "Critical" |
| G | Regulatory Impact | Text | 25 | GDPR, nDSG, etc. |
| H | Remediation Action | Text (wrap) | 40 | From source |
| I | Owner | Text | 20 | From source |
| J | Target Date | Date | 15 | From source |
| K | Status | Text | 15 | From source (Open/In Progress) |
| L | Priority Rank | Number | 10 | 1-10 (manual prioritization) |

**Data Population Method:**

**CRITICAL NOTE:** This sheet CANNOT use simple external link formulas because:

- Each source workbook has variable number of critical gaps
- Gap_Analysis rows are user-populated (not pre-defined structure)
- Need to filter for Risk Level = "Critical" only

**Two Implementation Options:**

**Option A: Manual Consolidation (Recommended for initial dashboard)**
1. Open each source workbook
2. Filter Gap_Analysis sheet for Risk Level = "Critical"
3. Copy critical gap rows
4. Paste into Consolidated_Gaps_Dashboard
5. Add "Source Assessment" column manually
6. Sort by Target Date or Priority Rank

**Option B: Power Query / Automated (Advanced, requires Excel Power Query)**
1. Use Power Query to connect to 4 source workbooks
2. Query each Gap_Analysis sheet
3. Filter for Risk Level = "Critical"
4. Append all queries
5. Add calculated column for "Source Assessment"
6. Refresh query to update dashboard

**For Python Script Generation:**

- Include commented-out Power Query code
- Provide manual consolidation instructions as default
- Note that full automation requires VBA or Power Query

**Data Rows:** 60 total (accommodate up to 15 critical gaps per source × 4 sources)

---

## Sheet: Evidence_Summary

**Purpose:** Verify evidence completeness across all assessments

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Source Assessment | Text | 30 | None | Pre-populated |
| B | Evidence Count | Number | 15 | None | External link formula |
| C | Expected Count | Number | 15 | None | Target (e.g., 15) |
| D | Status | Auto | 12 | ✅/⚠️/❌ | Formula-driven |
| E | Evidence Types | Text (wrap) | 50 | None | Summary of types |
| F | Gaps | Text (wrap) | 40 | None | Missing evidence |

**Pre-Populated Assessments (Rows 6-10):**

| Assessment | Expected Count | Status Criteria |
|------------|----------------|-----------------|
| A.8.12.1 Infrastructure | 15 | ✅ if ≥15, ⚠️ if 10-14, ❌ if <10 |
| A.8.12.2 Classification | 15 | ✅ if ≥15, ⚠️ if 10-14, ❌ if <10 |
| A.8.12.3 Channel Coverage | 15 | ✅ if ≥15, ⚠️ if 10-14, ❌ if <10 |
| A.8.12.4 Monitoring & Response | 10 | ✅ if ≥10, ⚠️ if 7-9, ❌ if <7 |
| **TOTAL** | **55** | ✅ if ≥55, ⚠️ if 40-54, ❌ if <40 |

**External Link Formula for Evidence Count:**

```excel
# Count evidence items in source Evidence_Register
# Evidence IDs are in column A, starting row 6

# A.8.12.1 Infrastructure Evidence Count (Cell B6)
=COUNTA([ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx]Evidence_Register!$A$6:$A$105)

# A.8.12.2 Classification Evidence Count (Cell B7)
=COUNTA([ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Evidence_Register!$A$6:$A$105)

# Total Evidence Count (Cell B10)
=SUM(B6:B9)
```

**Conditional Formatting:**

```python
# Evidence Count Status (Column D)
status_formula = {
    '✅': '=B6>=C6',           # Meets or exceeds target
    '⚠️': '=AND(B6>=C6*0.7, B6<C6)',  # 70-99% of target
    '❌': '=B6<C6*0.7'         # <70% of target
}
```

---

## Sheet: Trend_Analysis

**Purpose:** Quarter-over-quarter trend comparison

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Metric | Text | 35 | Pre-populated |
| B | Previous Quarter (Q4 2025) | Number/Text | 20 | Manual entry from previous dashboard |
| C | Current Quarter (Q1 2026) | Number/Text | 20 | External link formula |
| D | Change | Number | 12 | =C-B (for percentages/counts) |
| E | Trend | Auto | 12 | ⬆️ / ➡️ / ⬇️ (improving/stable/degrading) |
| F | Analysis | Text (wrap) | 50 | Manual commentary |

**Pre-Populated Metrics for Trending (Rows 6-40):**

| Category | Metrics |
|----------|---------|
| **Overall** | Overall Compliance %, Total Critical Gaps |
| **By Domain** | Infrastructure %, Classification %, Coverage %, Monitoring % |
| **Infrastructure** | DLP Technologies Deployed, Channel Coverage Count |
| **Classification** | Pattern Accuracy %, False Positive Rate % |
| **Coverage** | Bypass Tests Passed %, Shadow IT Channels |
| **Monitoring** | Alert Backlog, MTTR Critical (hours), SOC 24/7 Coverage |

**Trend Determination Formula:**

```excel
# Trend indicator (Column E)
# For compliance % (higher is better)
=IF(D6>5, "⬆️ Improving", IF(D6<-5, "⬇️ Degrading", "➡️ Stable"))

# For gap counts (lower is better)
=IF(D6<-2, "⬆️ Improving", IF(D6>2, "⬇️ Degrading", "➡️ Stable"))

# For MTTR (lower is better)
=IF(D6<-1, "⬆️ Improving", IF(D6>1, "⬇️ Degrading", "➡️ Stable"))
```

**Conditional Formatting:**

- ⬆️ Improving = Green
- ➡️ Stable = Yellow
- ⬇️ Degrading = Red

---

## Sheet: Approval_Sign-Off

**Purpose:** Multi-level approval workflow for dashboard

*(Same structure as previous IMP documents)*

**Approval Levels:**
1. Completed By: DLP Program Manager
2. Reviewed By: Compliance Officer / Internal Audit
3. Approved By: CISO
4. Presented To: Executive Management / Board (optional signature)

---

## Sheet: Link_Management

**Purpose:** External link status monitoring and troubleshooting reference

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Source Workbook | Text | 40 | Filename |
| B | File Path | Text | 60 | Full path |
| C | Link Status | Auto | 15 | OK / Error / Unknown |
| D | Last Updated | Auto | 20 | Timestamp |
| E | Sheet Referenced | Text | 25 | Which sheets linked |
| F | Formula Count | Number | 15 | How many formulas reference this workbook |
| G | Notes | Text (wrap) | 40 | Troubleshooting notes |

**Pre-Populated Source Workbooks (Rows 6-9):**

| Source Workbook | Sheets Referenced | Typical Formula Count |
|-----------------|-------------------|------------------------|
| ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx | Summary_Dashboard, Gap_Analysis, Evidence_Register | ~10 formulas |
| ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx | Summary_Dashboard, Gap_Analysis, Evidence_Register | ~10 formulas |
| ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx | Summary_Dashboard, Gap_Analysis, Evidence_Register | ~10 formulas |
| ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx | Summary_Dashboard, Gap_Analysis, Evidence_Register | ~10 formulas |

**Link Status Check:**

Excel: Data → Edit Links → Shows status for each external workbook
LibreOffice: Edit → Links → Shows status

**Status Values:**

- **OK:** Link functional, data updating
- **Error:** File not found, moved, or renamed
- **Unknown:** Excel can't determine status (may need manual update)

**Troubleshooting Guide (Rows 15-30):**

| Issue | Cause | Solution |
|-------|-------|----------|
| #REF! Error | Source workbook moved/renamed | Data → Edit Links → Change Source |
| Stale Data | Source updated but dashboard not refreshed | Data → Edit Links → Update Values |
| "Links Disabled" Warning | Excel security setting | File → Options → Trust Center → Enable automatic link updates |
| Circular Reference | Dashboard formula references itself | Check formula, ensure references external workbook only |
| Slow Performance | Too many external links | Consider consolidating formulas, use fewer references |

---

# External Link Formula Patterns

## Standard External Link Syntax

**Excel External Link Format:**
```excel
=[WorkbookName.xlsx]SheetName!CellReference

# Example:
=[ISMS-IMP-A.8.12.1_Infrastructure_20260121.xlsx]Summary_Dashboard!$B$7
```

**Components:**

- `[WorkbookName.xlsx]` - Source workbook filename in brackets
- `SheetName` - Sheet name in source workbook
- `!` - Separator
- `CellReference` - Cell address (use $ for absolute reference)

**Full Path External Link (when workbooks in different directories):**
```excel
='C:\Path\To\File\[WorkbookName.xlsx]SheetName'!CellReference

# Example:
='C:\ISMS\A.8.12_DLP\Q1_2026\[ISMS-IMP-A.8.12.1_Infrastructure_20260121.xlsx]Summary_Dashboard'!$B$7
```

## Common Formula Patterns

**Pattern 1: Direct Value Reference**
```excel
# Pull single value from source Summary_Dashboard
=[SourceWorkbook.xlsx]Summary_Dashboard!$B$7
```

**Pattern 2: COUNT / COUNTIF Across External Range**
```excel
# Count critical gaps in source Gap_Analysis
=COUNTIF([SourceWorkbook.xlsx]Gap_Analysis!$F$6:$F$45,"Critical")
```

**Pattern 3: Weighted Average Across Multiple Sources**
```excel
# Overall compliance from 4 sources (25% weight each)
=ROUND(
  ([Source1.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([Source2.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([Source3.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([Source4.xlsx]Summary_Dashboard!$B$7 * 0.25),
  0
)
```

**Pattern 4: SUM Across Multiple External Sources**
```excel
# Total critical gaps from all sources
=COUNTIF([Source1.xlsx]Gap_Analysis!$F$6:$F$45,"Critical") +
 COUNTIF([Source2.xlsx]Gap_Analysis!$F$6:$F$45,"Critical") +
 COUNTIF([Source3.xlsx]Gap_Analysis!$F$6:$F$45,"Critical") +
 COUNTIF([Source4.xlsx]Gap_Analysis!$F$6:$F$45,"Critical")
```

**Pattern 5: Conditional Status Based on External Value**
```excel
# Status based on compliance %
=IF([Source.xlsx]Summary_Dashboard!$B$7>=90, "✅ Compliant",
    IF([Source.xlsx]Summary_Dashboard!$B$7>=80, "⚠️ Partial",
       "❌ Non-Compliant"))
```

## Link Update and Maintenance

**Manual Link Update:**
1. Excel: Data → Edit Links
2. Select link to update
3. Click "Update Values" (refresh data from source)
4. Click "Change Source" (if file moved/renamed)

**Automatic Link Update:**

- File → Options → Advanced → General → "Update automatic links at open"
- Warning: May slow workbook opening if many links

**Breaking Links (Converting to Values):**

- Data → Edit Links → Select link → Break Link
- Converts formulas to static values (loses connection to source)
- Use when archiving historical dashboards

---

# Data Validation Rules

## Executive Summary Sheet

**Manual Entry Fields:**

- Executive Summary Text (rows 40-50): Free-form text, no validation
- Resource Requirements: Free-form text
- Risk Acceptance Decisions: Free-form text

**Dropdown Validations:**
```python
# Status fields (where not auto-calculated)
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False
}

# Audit Readiness
validation_audit = {
    'type': 'list',
    'formula1': '"Ready,Partially Ready,Not Ready"',
    'allow_blank': False
}
```

## Trend Analysis Sheet

**Previous Quarter Values:**

- Manual entry (copied from previous quarter dashboard)
- Numeric validation for percentages (0-100)
- Date validation for timestamps

---

# Conditional Formatting Rules

## Compliance Percentage Formatting

**Applied to:** All compliance % cells across all sheets

```python
compliance_format = {
    'dark_green': ('>=', 90),   # 90-100%: Audit-ready
    'light_green': ('and', [('>=', 85), ('<', 90)]),  # 85-89%: Nearly compliant
    'yellow': ('and', [('>=', 80), ('<', 85)]),       # 80-84%: Partially compliant
    'orange': ('and', [('>=', 70), ('<', 80)]),       # 70-79%: Needs improvement
    'red': ('<', 70)            # <70%: Non-compliant
}
```

## Gap Count Formatting

**Applied to:** Critical gaps count cells

```python
gap_count_format = {
    'green': ('=', 0),          # Zero critical gaps = excellent
    'yellow': ('and', [('>', 0), ('<=', 5)]),   # 1-5 gaps = acceptable
    'red': ('>', 5)             # >5 gaps = too many
}
```

## Evidence Count Formatting

**Applied to:** Evidence completeness cells

```python
evidence_format = {
    'green': ('>=', 'target'),      # Meets or exceeds target
    'yellow': ('>=', 'target*0.7'), # 70-99% of target
    'red': ('<', 'target*0.7')      # <70% of target
}
```

---

# Cell Protection

**Protected Cells (Formula Cells):**

- All external link formulas (prevent accidental editing)
- All calculated status cells
- All auto-generated IDs
- Pre-populated metric names

**Unprotected Cells (User Input):**

- Organization metadata (yellow cells)
- Executive summary text (manual commentary)
- Trend analysis commentary
- Risk acceptance decisions
- Approval signatures and dates

**Sheet Protection:**

- Enable protection on all sheets
- Allow: Format cells, Sort, Filter
- Disallow: Delete rows, Modify formulas, Unprotect sheet

---

# Dashboard Summary Formulas (Consolidated)

## Overall DLP Compliance %

```excel
# Executive_Summary!B6
=ROUND(
  ([ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25),
  0
)
```

## Total Critical Gaps

```excel
# Executive_Summary!B16
=COUNTIF([ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45,"Critical") +
 COUNTIF([ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45,"Critical") +
 COUNTIF([ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45,"Critical") +
 COUNTIF([ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45,"Critical")
```

## Total Evidence Items

```excel
# Evidence_Summary!B10
=COUNTA([ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx]Evidence_Register!$A$6:$A$105) +
 COUNTA([ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Evidence_Register!$A$6:$A$105) +
 COUNTA([ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx]Evidence_Register!$A$6:$A$105) +
 COUNTA([ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]Evidence_Register!$A$6:$A$105)
```

## Audit Readiness Status

```excel
# Executive_Summary!B18
=IF(AND(B6>=90, B16=0, B17>=55), "✅ Ready",
    IF(AND(B6>=80, B16<=5, B17>=40), "⚠️ Partially Ready",
       "❌ Not Ready"))

# Where:
# B6 = Overall Compliance %
# B16 = Total Critical Gaps
# B17 = Total Evidence Items
```

---

# APPENDIX: Technical Notes for Python Developers

## A.1 Python Script Integration

**Script Name:** `generate_a812_5_compliance_dashboard.py`

**CRITICAL CUSTOMIZATION REQUIRED:**

This script MUST be customized for each implementation because:
1. Source workbook filenames contain organization-specific dates (YYYYMMDD)
2. File paths are environment-specific
3. External link formulas require exact filenames

**Script Structure:**

```python
import openpyxl
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from datetime import datetime

# ============================================
# CONFIGURATION - CUSTOMIZE FOR YOUR DEPLOYMENT
# ============================================

# Assessment date (used in filenames)
ASSESSMENT_DATE = "20260121"  # Format: YYYYMMDD

# Source workbook filenames (MUST match actual files)
SOURCE_FILES = {
    'infrastructure': f'ISMS-IMP-A.8.12.1_Infrastructure_{ASSESSMENT_DATE}.xlsx',
    'classification': f'ISMS-IMP-A.8.12.2_Classification_{ASSESSMENT_DATE}.xlsx',
    'coverage': f'ISMS-IMP-A.8.12.3_Channel_Coverage_{ASSESSMENT_DATE}.xlsx',
    'monitoring': f'ISMS-IMP-A.8.12.4_Monitoring_Response_{ASSESSMENT_DATE}.xlsx'
}

# Dashboard workbook filename
DASHBOARD_FILE = f'ISMS-IMP-A.8.12.5_Compliance_Dashboard_{ASSESSMENT_DATE}.xlsx'

# Directory containing all workbooks (use relative path or absolute)
WORKBOOK_DIR = './'  # Current directory, or '/path/to/workbooks/'

# ============================================
# EXTERNAL LINK FORMULA TEMPLATES
# ============================================

def create_external_link_formula(source_file, sheet, cell):
    """
    Create Excel external link formula
    
    Args:
        source_file: Source workbook filename
        sheet: Sheet name in source workbook
        cell: Cell reference (e.g., "$B$7")
    
    Returns:
        Formula string (e.g., "=[SourceFile.xlsx]SheetName!$B$7")
    """
    return f"=[{source_file}]{sheet}!{cell}"

def create_overall_compliance_formula(source_files):
    """
    Create weighted average formula for overall compliance
    
    Returns formula: (Infra*0.25 + Class*0.25 + Coverage*0.25 + Monitor*0.25)
    """
    formulas = []
    for key in ['infrastructure', 'classification', 'coverage', 'monitoring']:
        link = create_external_link_formula(
            source_files[key],
            'Summary_Dashboard',
            '$B$7'
        )
        formulas.append(f"({link} * 0.25)")
    
    return f"=ROUND({' + '.join(formulas)}, 0)"

def create_critical_gaps_formula(source_files):
    """
    Create SUM formula for total critical gaps across all sources
    
    Returns formula: COUNTIF(Source1...) + COUNTIF(Source2...) + ...
    """
    countifs = []
    for key in ['infrastructure', 'classification', 'coverage', 'monitoring']:
        link_range = create_external_link_formula(
            source_files[key],
            'Gap_Analysis',
            '$F$6:$F$45'
        )
        countifs.append(f'COUNTIF({link_range},"Critical")')
    
    return f"={' + '.join(countifs)}"

# ============================================
# WORKBOOK GENERATION
# ============================================

def create_dashboard_workbook():
    """Main function to create dashboard workbook"""
    wb = Workbook()
    
    # Create sheets
    sheets = [
        'Instructions_Legend',
        'Executive_Summary',
        'Consolidated_Metrics',
        'Critical_Gaps_Consolidated',
        'Evidence_Summary',
        'Trend_Analysis',
        'Approval_Sign-Off',
        'Link_Management'
    ]
    
    # Implementation continues...
    # (See full script in separate file)
    
    return wb

if __name__ == "__main__":
    # Generate dashboard workbook
    wb = create_dashboard_workbook()
    wb.save(DASHBOARD_FILE)
    print(f"Dashboard created: {DASHBOARD_FILE}")
    print("IMPORTANT: Update source file paths if workbooks in different directory")
```

## A.2 Deployment Instructions

**Step 1: Prepare Environment**
```bash
# Ensure all 4 source assessments completed and saved
ls -la ISMS-IMP-A.8.12.*_YYYYMMDD.xlsx

# Expected output:
# ISMS-IMP-A.8.12.1_Infrastructure_20260121.xlsx
# ISMS-IMP-A.8.12.2_Classification_20260121.xlsx
# ISMS-IMP-A.8.12.3_Channel_Coverage_20260121.xlsx
# ISMS-IMP-A.8.12.4_Monitoring_Response_20260121.xlsx
```

**Step 2: Customize Python Script**
```python
# Edit generate_a812_5_compliance_dashboard.py
# Update ASSESSMENT_DATE to match your files
ASSESSMENT_DATE = "20260121"  # Change to your date
```

**Step 3: Generate Dashboard**
```bash
python3 generate_a812_5_compliance_dashboard.py

# Output: ISMS-IMP-A.8.12.5_Compliance_Dashboard_20260121.xlsx
```

**Step 4: Verify External Links**
```bash
# Open in Excel
# Data → Edit Links → Verify all 4 source workbooks show "OK" status
# If "Error" → Check file paths, ensure all workbooks in same directory
```

**Step 5: Test Link Updates**
```bash
# Modify value in source workbook (e.g., change compliance % in A.8.12.1)
# Save source workbook
# Refresh dashboard: Data → Edit Links → Update Values
# Verify dashboard reflects change
```

## A.3 Quality Assurance

**Validation Script:** `excel_sanity_check_a812_5.py`

```python
def validate_dashboard(workbook_path):
    """Comprehensive dashboard validation"""
    checks = [
        check_all_sheets_exist(),
        check_external_links_functional(),
        check_formulas_no_errors(),
        check_compliance_calculation(),
        check_critical_gaps_sum(),
        check_evidence_count(),
        check_approval_workflow()
    ]
    return all(checks)

def check_external_links_functional():
    """Verify all external links return values (not #REF!)"""
    # Open workbook
    # For each external link formula:
    #   - Check formula doesn't contain #REF!
    #   - Verify cell value is numeric or text (not error)
    pass

def check_compliance_calculation():
    """Verify overall compliance % matches manual calculation"""
    # Extract 4 domain compliance %
    # Calculate: (sum of 4) / 4
    # Compare to dashboard Overall Compliance %
    # Assert difference <0.1% (rounding tolerance)
    pass
```

## A.4 Troubleshooting Guide

**Issue: #REF! Errors in Dashboard**

*Cause:* Source workbook file not found or moved

*Solution:*
1. Data → Edit Links
2. Select broken link
3. Change Source → Browse to correct file
4. Update Values

**Issue: Formulas Not Auto-Updating**

*Cause:* Automatic link updates disabled

*Solution:*
1. File → Options → Advanced → General
2. Enable "Update automatic links at open"
3. Close and reopen workbook

**Issue: Circular Reference Warning**

*Cause:* Dashboard formula accidentally references itself

*Solution:*
1. Formulas → Error Checking → Circular References
2. Review formula, ensure references external workbook only
3. Fix formula to point to correct source

---

**END OF PART II: TECHNICAL SPECIFICATION**

**Status:** Complete  
**Next Action:** Implement Python generator, deploy dashboard, verify external links

---

**Final Note for Implementers:**

This dashboard is the CONSOLIDATION LAYER. Its value depends entirely on the quality of the 4 source assessments. Invest time in high-quality source assessments before creating dashboard.

**Maintenance:**

- Quarterly: Update dashboard when source assessments refreshed
- After major DLP changes: Update relevant source assessment, dashboard auto-reflects change
- Before audit: Verify all links functional, evidence complete, gaps documented

**Archive Strategy:**

- Keep historical dashboards (one per quarter) for trend analysis
- Break links in archived dashboards (convert formulas to values) to prevent link errors when source files archived

---

**END OF SPECIFICATION**

---

*"Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
