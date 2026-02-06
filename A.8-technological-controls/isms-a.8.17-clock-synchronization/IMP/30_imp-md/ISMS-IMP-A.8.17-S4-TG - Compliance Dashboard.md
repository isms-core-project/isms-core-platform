**ISMS-IMP-A.8.17-S4-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Clock Synchronization Compliance Dashboard |
| **Related Policy** | ISMS-POL-A.8.17 (Clock Synchronization Policy) |
| **Purpose** | Provide executive dashboard aggregating S1-S3 findings, showing overall clock synchronization compliance status and metrics |
| **Target Audience** | CISO, Executive Management, ISMS Officers, Auditors, Risk Managers |
| **Assessment Type** | Executive Reporting & Compliance Tracking |
| **Review Cycle** | Monthly or As Required |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original Date] | Initial technical specification for compliance dashboard | ISMS Officer |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.17-S4-UG.

---

# Technical Specification

**Audience:** Workbook developers, Python script maintainers, technical implementers

**Note:** This section provides technical specifications for compliance dashboard workbook structure. Users completing the assessment should refer to Part I above.

---

# Implementation Requirement Mapping

**This section maps dashboard metrics to policy requirements for traceability.**

## Dashboard Metrics to Policy Mapping

| Dashboard Metric | Policy Requirement(s) | Source Assessment |
|-----------------|----------------------|-------------------|
| External Source Count | REQ-817-001, REQ-817-002 | S1 |
| Internal Server Count | REQ-817-005, REQ-817-006 | S1 |
| Monitoring Coverage | REQ-817-008 | S1 |
| System Compliance % | REQ-817-009, REQ-817-010 | S2 |
| Exception Count | REQ-817-017, REQ-817-019 | S3 |
| Gap Remediation | All REQ-817-xxx | S1, S2, S3 |

---

# SECTION A: Implementation Guidance

## Introduction

This section provides technical guidance for creating and maintaining the compliance dashboard, including metric calculations, data aggregation, and visualization best practices.

**Purpose:** Enable ISMS Officers to create consistent, accurate compliance dashboards that aggregate findings from S1, S2, S3 assessments.

**Scope:** Executive-level reporting on clock synchronization compliance.

**Related Documents:**

- ISMS-POL-A.8.17 (Clock Synchronization Policy)
- ISMS-IMP-A.8.17-S1 (Time Source Configuration)
- ISMS-IMP-A.8.17-S2 (Synchronization Verification)
- ISMS-IMP-A.8.17-S3 (Exception Management)

---

## Compliance Calculation Methodology

### Overall Compliance Score

**Formula:**

```
Overall Compliance % = ((Compliant Systems + Systems with Approved Exceptions) / Total Systems in Scope) × 100
```

**Components:**

| Component | Source | Description |
|-----------|--------|-------------|
| Compliant Systems | S2 Verification_Results | Systems verified as synchronized to approved time sources |
| Systems with Approved Exceptions | S3 Active_Exceptions | Systems with approved exceptions and compensating controls |
| Total Systems in Scope | S2 System_Inventory | All systems subject to clock synchronization policy |

**Example Calculation:**

```
Total Systems: 1,234
Compliant Systems: 1,200
Approved Exceptions: 3

Overall Compliance = (1,200 + 3) / 1,234 × 100 = 97.5%
```

**Important Notes:**

- Systems with approved exceptions count toward compliance (they have compensating controls)
- Systems pending exception approval do NOT count toward compliance
- Systems pending remediation do NOT count toward compliance

### Infrastructure Health Score

**Formula:**

```
Infrastructure Health = (Metrics Met / Total Metrics) × 100
```

**Metrics Evaluated:**

| Metric | Requirement | Weight |
|--------|-------------|--------|
| External Sources ≥ 2 | REQ-817-001 | Critical |
| Primary Sources ≥ 2 | REQ-817-002 | Critical |
| Internal Servers ≥ 2 | REQ-817-005 | Critical |
| All Servers Stratum 2/3 | REQ-817-006 | High |
| All Servers Monitored with Alerting | REQ-817-008 | Critical |
| All Sources/Servers Active | Operational | High |

**Status Determination:**

| Health Score | Status |
|--------------|--------|
| 100% | Green |
| 80-99% | Yellow (minor gaps) |
| <80% | Red (critical gaps) |

---

## Data Aggregation Logic

### From S1 (Time Source Configuration)

**Metrics to Extract:**

```excel
External Source Count = COUNTA(S1_Time_Sources!A2:A100)
Primary Sources (Stratum 0/1) = COUNTIFS(S1_Time_Sources!D2:D100,"<=1")
Internal Server Count = COUNTA(S1_Internal_NTP_Servers!A2:A100)
Servers with Alerting = COUNTIF(S1_Internal_NTP_Servers!H2:H100,"*Monitored with Alerting*")
Active Sources = COUNTIF(S1_Time_Sources!I2:I100,"*Active*")
Active Servers = COUNTIF(S1_Internal_NTP_Servers!J2:J100,"*Active*")
```

### From S2 (Synchronization Verification)

**Metrics to Extract:**

```excel
Total Systems = COUNTA(S2_System_Inventory!A2:A5000)
Compliant Systems = COUNTIF(S2_Verification_Results!F2:F5000,"Compliant")
Non-Compliant Systems = COUNTIF(S2_Verification_Results!F2:F5000,"Non-Compliant")
```

### From S3 (Exception Management)

**Metrics to Extract:**

```excel
Active Exceptions = COUNTA(S3_Active_Exceptions!A2:A100)
Pending Requests = COUNTIF(S3_Exception_Requests!P2:P100,"<>Approved")
Expiring Soon = COUNTIFS(S3_Active_Exceptions!J2:J100,"<="&TODAY()+30,S3_Active_Exceptions!J2:J100,">="&TODAY())
```

---

## Visualization Guidelines

### Compliance Score Display

**Design:**

- Large font (36-48pt) for percentage
- Color-coded background (Green/Yellow/Red)
- Trend arrow (up/down/flat)

**Example:**

```
┌─────────────────────┐
│    COMPLIANCE       │
│                     │
│      97.5%  ↑       │
│                     │
│  [GREEN BACKGROUND] │
└─────────────────────┘
```

### Trend Chart

**Type:** Line chart

**X-Axis:** Time periods (monthly or quarterly)

**Y-Axis:** Compliance percentage (0-100%)

**Guidelines:**

- Show 6-12 months of data
- Include target line (e.g., 95%)
- Annotate significant events

### Status Indicators

**Green/Yellow/Red Indicators:**

Use consistent colors across dashboard:

- Green: RGB(0, 176, 80) or Hex #00B050
- Yellow: RGB(255, 192, 0) or Hex #FFC000
- Red: RGB(255, 0, 0) or Hex #FF0000

---

# SECTION B: Assessment Workbook Specification

## Workbook Overview

**Filename:** ISMS-IMP-A.8.17-S4_Compliance_Dashboard_[YYYYMMDD].xlsx

**Generated By:** `generate_a817_s4_compliance_dashboard.py`

**Purpose:** Executive dashboard aggregating S1-S3 compliance findings

**Sheets:**
1. **Instructions** - Dashboard guidance
2. **Executive_Summary** - Overall compliance score and status
3. **Infrastructure_Health** - NTP infrastructure health metrics
4. **System_Compliance** - System-level sync compliance
5. **Gaps_Action_Items** - Remediation tracking

**Total Sheets:** 5

---

## Common Styling Definitions

**Header Style:**

- Font: Bold, White (FFFFFF), Size 11
- Fill: Dark Blue (366092)
- Alignment: Center, Vertical Center, Wrap Text
- Border: Thin borders all sides

**Title Style:**

- Font: Bold, Size 14, Dark Blue (366092)
- Alignment: Left, Vertical Center

**Big Number Style (Compliance Score):**

- Font: Bold, Size 36, Color based on threshold
- Alignment: Center, Vertical Center

**Status Green:**

- Fill: RGB(0, 176, 80)
- Font: White, Bold

**Status Yellow:**

- Fill: RGB(255, 192, 0)
- Font: Black, Bold

**Status Red:**

- Fill: RGB(255, 0, 0)
- Font: White, Bold

---

## Sheet 1: Instructions

**Purpose:** Provide dashboard usage instructions and metric definitions.

**Layout:**

**Row 1-2:** Title Block

- A1: "ISMS A.8.17-S4 - Compliance Dashboard" (Font: Bold 16, Dark Blue, Merged A1:F1)
- A2: "Version 1.0 | [Last Updated Date]" (Font: Italic 10, Merged A2:F2)

**Row 4-5:** Document Metadata

- A4: "Document ID:" (Bold) | B4: "ISMS-IMP-A.8.17-S4" (Bold, Dark Blue)
- A5: "Title:" (Bold) | B5: "Clock Synchronization Compliance Dashboard"

**Row 7+:** Instructions Content

- Purpose statement
- Data source descriptions (S1, S2, S3)
- Metric definitions
- Update frequency guidance
- Risk rating definitions
- Contact information

**Column Widths:**

- A: 20
- B: 80
- C-F: 15 each

---

## Sheet 2: Executive_Summary

**Purpose:** Single-page executive view of compliance status.

**Layout:**

**Section 1: Compliance Score (Rows 1-8)**

| Cell | Content | Format |
|------|---------|--------|
| A1:D1 | "Clock Synchronization Compliance Dashboard" | Title, merged |
| A2:D2 | "Last Updated: [Date]" | Subtitle, merged |
| B4:C6 | [Compliance %] | Big Number, 36pt, color-coded, merged |
| D4:D6 | [Trend Arrow] | Arrow icon |
| A8 | "Risk Rating:" | Label |
| B8 | [Green/Yellow/Red] | Status indicator |

**Section 2: Key Metrics (Rows 10-18)**

| Row | Column A | Column B | Column C |
|-----|----------|----------|----------|
| 10 | "KEY METRICS" (Header) | | |
| 11 | "Metric" | "Value" | "Status" |
| 12 | "Total Systems in Scope" | [Number] | |
| 13 | "Compliant Systems" | [Number] | |
| 14 | "Non-Compliant Systems" | [Number] | |
| 15 | "Systems with Exceptions" | [Number] | |
| 16 | "Pending Remediation" | [Number] | Warning if >0 |
| 17 | "Infrastructure Status" | [Green/Yellow/Red] | |

**Section 3: Executive Summary Narrative (Rows 20-30)**

| Row | Content |
|-----|---------|
| 20 | "EXECUTIVE SUMMARY" (Header) |
| 21-30 | Free-form text area for narrative |

**Section 4: Trend Chart (Rows 32-45)**

Embedded line chart showing compliance trend over time.

---

## Sheet 3: Infrastructure_Health

**Purpose:** Show NTP infrastructure health from S1 assessment.

**Layout:**

**Section 1: External Time Sources (Rows 1-10)**

| Row | Column A | Column B | Column C | Column D |
|-----|----------|----------|----------|----------|
| 1 | "EXTERNAL TIME SOURCES" (Header, merged A1:D1) | | | |
| 2 | "Metric" | "Requirement" | "Actual" | "Status" |
| 3 | "External Source Count" | "≥2" | [Formula] | [Pass/Fail] |
| 4 | "Primary Sources (Stratum 0/1)" | "≥2" | [Formula] | [Pass/Fail] |
| 5 | "Sources Active" | "100%" | [Formula] | [Pass/Fail] |

**Section 2: Internal NTP Servers (Rows 12-20)**

Similar structure.

**Section 3: Monitoring (Rows 22-28)**

Similar structure.

**Section 4: Overall Infrastructure Status (Rows 30-35)**

Summary with overall Green/Yellow/Red status.

---

## Sheet 4: System_Compliance

**Purpose:** Show system-level compliance from S2 assessment.

**Layout:**

**Section 1: Overall Compliance (Rows 1-12)**

| Row | Column A | Column B | Column C |
|-----|----------|----------|----------|
| 1 | "SYSTEM COMPLIANCE OVERVIEW" (Header) | | |
| 2 | "Metric" | "Count" | "Percentage" |
| 3 | "Total Systems in Scope" | [Number] | "100%" |
| 4 | "Compliant Systems" | [Number] | [Formula] |
| 5 | "Non-Compliant Systems" | [Number] | [Formula] |
| 6 | "With Approved Exceptions" | [Number] | [Formula] |
| 7 | "Pending Remediation" | [Number] | [Formula] |
| 9 | "EFFECTIVE COMPLIANCE" | [Number] | [Formula] |

**Section 2: By Category (Rows 14-25)**

Table with categories: Servers, Workstations, Network Devices, OT/ICS, Cloud, Other.

**Section 3: By Department (Rows 27-40)**

Table with department breakdown.

**Section 4: Non-Compliant Summary (Rows 42-50)**

Breakdown of non-compliant systems by status.

---

## Sheet 5: Gaps_Action_Items

**Purpose:** Track remediation of gaps from S1, S2, S3.

**Headers (Row 1):**

| Column | Header | Width |
|--------|--------|-------|
| A | Gap ID | 18 |
| B | Source Assessment | 12 |
| C | Gap Description | 40 |
| D | Severity | 12 |
| E | Policy Requirement | 15 |
| F | Impact | 30 |
| G | Remediation Plan | 40 |
| H | Responsible Party | 20 |
| I | Target Date | 12 |
| J | Status | 15 |
| K | Progress Notes | 35 |
| L | Completion Date | 12 |

**Data Validation:**

**Column B (Source Assessment):**

- Type: List
- Formula: `"S1,S2,S3"`

**Column D (Severity):**

- Type: List
- Formula: `"Critical,High,Medium,Low"`

**Column J (Status):**

- Type: List
- Formula: `"Open,In Progress,Completed,Deferred"`

**Conditional Formatting:**

- Severity = "Critical": Red fill
- Severity = "High": Orange fill
- Status = "Completed": Green fill, strikethrough text
- Target Date < TODAY() AND Status <> "Completed": Red text (overdue)

**Summary Section (Rows 50+):**

Status distribution and severity distribution tables.

---

## Python Script Reference

**Script File:** `generate_a817_s4_compliance_dashboard.py`

**Script Location:** `10-isms-scr-base/isms-a.8.17-clock-synchronization/10_generator-master/`

**Key Functions:**

- `create_styles()` - Defines all styling
- `create_instructions_sheet()` - Generates Instructions sheet
- `create_executive_summary_sheet()` - Generates Executive_Summary sheet
- `create_infrastructure_health_sheet()` - Generates Infrastructure_Health sheet
- `create_system_compliance_sheet()` - Generates System_Compliance sheet
- `create_gaps_action_items_sheet()` - Generates Gaps_Action_Items sheet
- `main()` - Orchestrates workbook generation

**To regenerate workbook:**

```bash
cd 10-isms-scr-base/isms-a.8.17-clock-synchronization/10_generator-master
python3 generate_a817_s4_compliance_dashboard.py
mv *.xlsx ../90_workbooks/
```

**Output:** Excel workbook ready for user completion per Part I User Guide.

---

## Linking to Source Workbooks

**For automated updates, link cells to source workbooks:**

**Example Formulas (assuming workbooks in same folder):**

```excel
' External Source Count (from S1)
='[ISMS-IMP-A.8.17-S1_Time_Source_Configuration.xlsx]Time_Sources'!$A$1:COUNTA($A:$A)-1

' Compliant Systems (from S2)
='[ISMS-IMP-A.8.17-S2_Synchronization_Verification.xlsx]Summary'!$B$5

' Active Exceptions (from S3)
='[ISMS-IMP-A.8.17-S3_Exception_Management.xlsx]Summary_Dashboard'!$B$5
```

**Best Practice:**

- Store all A.8.17 workbooks in same folder for easy linking
- Update all workbooks together to maintain consistency
- Document linked workbook locations in Instructions sheet

---

**END OF SPECIFICATION**

---

*"Time is the wisest counselor of all."*
— Pericles

<!-- QA_VERIFIED: 2026-02-06 -->
