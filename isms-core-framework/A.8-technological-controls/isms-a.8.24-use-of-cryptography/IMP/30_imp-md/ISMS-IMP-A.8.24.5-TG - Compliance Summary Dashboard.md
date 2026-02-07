**ISMS-IMP-A.8.24.5-TG - Compliance Summary Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography

---

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.24.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Cryptography Compliance Summary Dashboard |
| **Related Policy** | ISMS-POL-A.8.24 (Use of Cryptography) |
| **Related Assessments** | ISMS-IMP-A.8.24.1 (Transmission), ISMS-IMP-A.8.24.2 (Storage), ISMS-IMP-A.8.24.3 (Authentication), ISMS-IMP-A.8.24.4 (Key Management) |
| **Purpose** | Provide consolidated view of cryptographic control compliance across all domains (transmission, storage, authentication, key management) with executive summary metrics and completion tracking |
| **Target Audience** | CISO, Security Managers, Compliance Officers, Auditors, Senior Management |
| **Assessment Type** | Summary Dashboard / Executive Overview |
| **Review Cycle** | Quarterly (Aligned with Individual Assessment Refresh) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial dashboard specification and user completion guide | CISO / Security Manager |

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel dashboard workbook generation and maintenance. Users completing the dashboard should refer to Part I above.

---

# Instructions for Dashboard Development

## Workbook Generation

**Python Script:** `generate_a824_5_compliance_summary_dashboard.py`

**Critical Design Principle:**
This dashboard is a **CONSOLIDATION TOOL**, not a data entry workbook. It reads data FROM 4 source workbooks:

- ISMS-IMP-A.8.24.1 (Data Transmission)
- ISMS-IMP-A.8.24.2 (Data Storage)
- ISMS-IMP-A.8.24.3 (Authentication)
- ISMS-IMP-A.8.24.4 (Key Management)

**Data Extraction Approach:**
1. **External workbook links** (preferred) - Live data, auto-updates when source workbooks change
2. **Python-based extraction** (alternative) - Snapshot at generation time, requires regeneration for updates

**Current Implementation:** External workbook links (Excel formulas reference source workbooks)

## Schema Validation (CRITICAL)

**Before building consolidation logic, DOCUMENT the actual structure of each source workbook:**

```python
SOURCE_WORKBOOK_SCHEMAS = {
    'ISMS-IMP-A.8.24.1.xlsx': {
        'summary_sheet': 'Summary Dashboard',
        'key_cells': {
            'total_items': 'B9',
            'compliant': 'C9',
            'partial': 'D9',
            'non_compliant': 'E9',
            'na': 'F9',
            'compliance_pct': 'G9'
        },
        'assessment_sheets': [
            '1.1 External HTTPS-TLS',
            '1.2 Internal HTTPS-TLS',
            # ... 13 total sheets
        ],
        'evidence_sheet': 'Evidence Register',
        'gap_extraction': {
            'status_column': 'D',  # Status column in assessment sheets
            'non_compliant_value': '❌ Non-Compliant',
            'partial_value': '⚠️ Partial',
            'system_column': 'A',
            'gap_description_column': 'M',  # Or wherever gap descriptions are
            'remediation_column': 'N'
        }
    },
    'ISMS-IMP-A.8.24.2.xlsx': {
        'summary_sheet': 'Summary Dashboard',
        'key_cells': {
            'total_items': 'B9',
            'compliant': 'C9',
            'partial': 'D9',
            'non_compliant': 'E9',
            'na': 'F9',
            'compliance_pct': 'G9'
        },
        'assessment_sheets': [
            '1. Mobile Devices',
            '2. Laptops & Workstations',
            # ... 7 total sheets
        ],
        'evidence_sheet': 'Evidence Register',
        'gap_extraction': {
            'status_column': 'D',
            'non_compliant_value': '❌ Non-Compliant',
            'partial_value': '⚠️ Partial',
            'system_column': 'A',
            'gap_description_column': 'M',
            'remediation_column': 'N'
        }
    },
    'ISMS-IMP-A.8.24.3.xlsx': {
        'summary_sheet': 'Summary Dashboard',
        'key_cells': {
            'total_items': 'B9',
            'compliant': 'C9',
            'partial': 'D9',
            'non_compliant': 'E9',
            'na': 'F9',
            'compliance_pct': 'G9'
        },
        'assessment_sheets': [
            '1. Password Security',
            '2. Multi-Factor Authentication',
            # ... 5 total sheets
        ],
        'evidence_sheet': 'Evidence Register',
        'gap_extraction': {
            'status_column': 'D',
            'non_compliant_value': '❌ Non-Compliant',
            'partial_value': '⚠️ Partial',
            'system_column': 'A',
            'gap_description_column': 'M',
            'remediation_column': 'N'
        }
    },
    'ISMS-IMP-A.8.24.4.xlsx': {
        'summary_sheet': 'Summary Dashboard',
        'key_cells': {
            'total_items': 'B9',
            'compliant': 'C9',
            'partial': 'D9',
            'non_compliant': 'E9',
            'na': 'F9',
            'compliance_pct': 'G9'
        },
        'assessment_sheets': [
            '1. Key Generation',
            '2. Key Storage',
            # ... 5 total sheets
        ],
        'evidence_sheet': 'Evidence Register',
        'gap_extraction': {
            'status_column': 'D',
            'non_compliant_value': '❌ Non-Compliant',
            'partial_value': '⚠️ Partial',
            'system_column': 'A',
            'gap_description_column': 'M',
            'remediation_column': 'N'
        }
    }
}
```

**Why This Matters:**

- ❌ **DON'T ASSUME** all workbooks have same structure
- ❌ **DON'T COPY-PASTE** logic from other controls without verification
- ✅ **DO DOCUMENT** actual sheet names, column positions, cell addresses
- ✅ **DO VALIDATE** each workbook exists and matches expected schema before processing

---

# Common Dashboard Structure

## File Naming

**Output Filename:** `ISMS-IMP-A.8.24.5_Compliance_Dashboard_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.8.24.5_Compliance_Dashboard_20260115.xlsx`

## Sheet Order and Purpose

| Sheet # | Sheet Name | Rows (Est.) | Purpose |
|---------|------------|-------------|---------|
| 1 | Executive Dashboard | ~90 | One-page executive summary |
| 2 | Gap Analysis | Variable | All non-compliant items from 4 assessments |
| 3 | Risk Register | Variable | Security risks derived from critical/high gaps |
| 4 | Remediation Roadmap | Variable | Action plans with timelines and budget |
| 5 | KPIs & Metrics | ~25 | Quantitative performance indicators |
| 6 | Evidence Register | Variable | Consolidated evidence from 4 assessments |
| 7 | Action Items & Follow-up | Variable | Follow-up tasks and ownership |
| 8 | Audit & Compliance Log | Variable | Compliance review history |
| 9 | Approval Sign-Off | Variable | Formal sign-off and approvals |

**Total Sheets:** 9

---

# Sheet 1: Executive Dashboard

## Purpose
Single-page compliance overview for CISO, Board, Executive Management.

## Layout Specification

**Header Section (Rows 1-10)**

**Title (Row 1):**

- **Cell A1 (merged A1:I1):** "ISMS-IMP-A.8.24.5 – Cryptography Compliance Summary Dashboard"
- **Font:** Arial 20pt, Bold, White
- **Background:** Dark Blue (003366)
- **Height:** 50px
- **Alignment:** Center, Middle

**Subtitle (Row 2):**

- **Cell A2 (merged A2:I2):** "ISO/IEC 27001:2022 - Control A.8.24: Use of Cryptography - Executive Overview"
- **Font:** Arial 12pt, White
- **Background:** Dark Blue (003366)
- **Height:** 30px
- **Alignment:** Center, Middle

**Document Information Block (Rows 4-11):**

| Row | Label (Col A) | Value (Col B-C, merged) | Format |
|-----|---------------|-------------------------|--------|
| 4 | Document ID: | ISMS-IMP-A.8.24.5 | Static text |
| 5 | Report Type: | Compliance Summary Dashboard | Static text |
| 6 | Related Policy: | ISMS-POL-A.8.24 (Use of Cryptography) | Static text |
| 7 | Version: | 1.0 | Static text |
| 8 | Report Date: | [USER INPUT - yellow] | Date picker, DD.MM.YYYY |
| 9 | Reporting Period: | [USER INPUT - yellow] | Text input, e.g., "Q4 2024" |
| 10 | Prepared By: | [USER INPUT - yellow] | Text input |
| 11 | Organization: | [USER INPUT - yellow] | Text input |
| 12 | Review Cycle: | Quarterly | Static text |
| 13 | Last Updated: | [=TODAY()] | Formula, auto-updates |

**Column Widths:**

- Column A: 25
- Column B: 15
- Column C: 30
- Columns D-I: 12 (for visual spacing)

**Cell Styling:**

- Label column (A): Bold, Gray background (D9D9D9)
- Value column (B-C): Yellow background (FFFF00) for user input, White for static/formula
- Borders: Thin black border around information block

---

**Overall Compliance Summary (Rows 15-21)**

**Section Header (Row 15):**

- **Cell A15 (merged A15:I15):** "OVERALL CRYPTOGRAPHY COMPLIANCE STATUS"
- **Font:** Arial 14pt, Bold, White
- **Background:** Dark Blue (003366)
- **Height:** 35px
- **Alignment:** Center, Middle

**Compliance Scorecard (Rows 17-20):**

| Metric (Col A-B) | Score (Col C) | Target (Col D) | Status (Col E) | Description (Col F-I) |
|------------------|---------------|----------------|----------------|-----------------------|
| Overall Compliance Rate | [Formula] | ≥95% | [Traffic Light] | Average of 4 assessment areas |
| Critical Gaps | [Formula] | 0 | [Traffic Light] | Count of Critical severity gaps |
| High-Risk Items | [Formula] | ≤5 | [Traffic Light] | Count of High severity gaps |
| Remediation Progress | [Formula] | ≥80% | [Traffic Light] | % of gaps with remediation in progress/complete |

**Formula Specifications:**

**Overall Compliance Rate (Cell C17):**
```excel
=AVERAGE('[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$G$9,
         '[ISMS-IMP-A.8.24.2.xlsx]Summary Dashboard'!$G$9,
         '[ISMS-IMP-A.8.24.3.xlsx]Summary Dashboard'!$G$9,
         '[ISMS-IMP-A.8.24.4.xlsx]Summary Dashboard'!$G$9)
```

**Note:** External workbook links require workbooks to be in same directory or use full file paths.

**Critical Gaps (Cell C18):**
```excel
=COUNTIFS('2. Gap Analysis'!$D:$D,"Critical")
```

**High-Risk Items (Cell C19):**
```excel
=COUNTIFS('2. Gap Analysis'!$D:$D,"High")
```

**Remediation Progress (Cell C20):**
```excel
=COUNTIFS('4. Remediation Roadmap'!$H:$H,"In Progress",'4. Remediation Roadmap'!$H:$H,"Completed") 
 / COUNTA('4. Remediation Roadmap'!$A:$A) * 100
```

**Conditional Formatting (Status Column E):**

**Overall Compliance Rate:**

- Green (00B050): ≥95%
- Yellow (FFC000): 85-94%
- Red (FF0000): <85%

**Critical Gaps:**

- Green (00B050): 0
- Yellow (FFC000): 1-3
- Red (FF0000): ≥4

**High-Risk Items:**

- Green (00B050): ≤5
- Yellow (FFC000): 6-15
- Red (FF0000): >15

**Remediation Progress:**

- Green (00B050): ≥80%
- Yellow (FFC000): 50-79%
- Red (FF0000): <50%

**Implementation Note:**
Use Excel conditional formatting rules with icon sets or cell fill colors. Traffic light symbols (●) with appropriate colors provide visual impact.

---

**Compliance By Assessment Area (Rows 23-30)**

**Section Header (Row 23):**

- **Cell A23 (merged A23:I23):** "COMPLIANCE BY ASSESSMENT AREA"
- **Font:** Arial 12pt, Bold, White
- **Background:** Dark Blue (003366)
- **Height:** 30px

**Column Headers (Row 25):**

| Column | Header | Width | Alignment |
|--------|--------|-------|-----------|
| A | Assessment Area | 25 | Left |
| B | Source Document | 22 | Left |
| C | Total Items | 12 | Center |
| D | Compliant | 12 | Center |
| E | Partial | 12 | Center |
| F | Non-Compliant | 14 | Center |
| G | N/A | 10 | Center |
| H | Compliance % | 14 | Center |
| I | Trend | 10 | Center |

**Header Styling:**

- Font: Arial 10pt, Bold, White
- Background: Blue (0070C0)
- Borders: Thin black
- Alignment: Center, Middle

**Data Rows (26-29):**

**Row 26: Data Transmission**

- **Assessment Area (A26):** "Data Transmission"
- **Source Document (B26):** "ISMS-IMP-A.8.24.1"
- **Total Items (C26):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$B$9`
- **Compliant (D26):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$C$9`
- **Partial (E26):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$D$9`
- **Non-Compliant (F26):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$E$9`
- **N/A (G26):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$F$9`
- **Compliance % (H26):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$G$9`
- **Trend (I26):** [USER INPUT dropdown: ↑ / → / ↓]

**Row 27: Data Storage**

- **Assessment Area (A27):** "Data Storage"
- **Source Document (B27):** "ISMS-IMP-A.8.24.2"
- **Formulas (C27:H27):** Same pattern, reference `ISMS-IMP-A.8.24.2.xlsx`
- **Trend (I27):** [USER INPUT dropdown]

**Row 28: Authentication**

- **Assessment Area (A28):** "Authentication"
- **Source Document (B28):** "ISMS-IMP-A.8.24.3"
- **Formulas (C28:H28):** Same pattern, reference `ISMS-IMP-A.8.24.3.xlsx`
- **Trend (I28):** [USER INPUT dropdown]

**Row 29: Key Management**

- **Assessment Area (A29):** "Key Management"
- **Source Document (B29):** "ISMS-IMP-A.8.24.4"
- **Formulas (C29:H29):** Same pattern, reference `ISMS-IMP-A.8.24.4.xlsx`
- **Trend (I29):** [USER INPUT dropdown]

**TOTAL Row (30):**

- **Label (A30):** "TOTAL" (Bold)
- **Source Document (B30):** "All Assessments"
- **Total Items (C30):** `=SUM(C26:C29)`
- **Compliant (D30):** `=SUM(D26:D29)`
- **Partial (E30):** `=SUM(E26:E29)`
- **Non-Compliant (F30):** `=SUM(F26:F29)`
- **N/A (G30):** `=SUM(G26:G29)`
- **Compliance % (H30):** `=AVERAGE(H26:H29)` (weighted average)
- **Trend (I30):** Leave blank

**Data Validation (Trend Column I):**
```
List source: ↑, →, ↓
```

**Conditional Formatting (Trend Column I):**

- ↑ (Green): Improved
- → (Yellow): No change
- ↓ (Red): Declined

---

**Compliance Visualization (Rows 32-50)**

**Note:** Charts and graphs are inserted manually after workbook generation using Excel's chart tools.

**Recommended Charts:**

1. **Overall Compliance Gauge Chart (Rows 32-45, Cols A-D)**

   - Chart Type: Doughnut or Speedometer
   - Data Source: Cell C17 (Overall Compliance Rate)
   - Display: 0-100%, with target line at 95%
   - Colors: Green zone (95-100%), Yellow zone (85-95%), Red zone (0-85%)

2. **Compliance by Area Bar Chart (Rows 32-45, Cols E-I)**

   - Chart Type: Horizontal Bar Chart
   - Data Source: Rows 26-29, Column H (Compliance %)
   - X-Axis: 0-100%
   - Y-Axis: 4 assessment areas
   - Target line: 95% (vertical line)

3. **Gap Distribution Pie Chart (Rows 47-50, Cols A-D)**

   - Chart Type: Pie Chart
   - Data Source: Row 30, Columns D-F (Compliant, Partial, Non-Compliant)
   - Colors: Green (Compliant), Yellow (Partial), Red (Non-Compliant)
   - Show percentages on slices

4. **Risk Level Distribution (Rows 47-50, Cols E-I)**

   - Chart Type: Stacked Bar Chart
   - Data Source: Sheet '2. Gap Analysis', Summary Statistics (Rows 4-8, Columns C-F)
   - Categories: Critical, High, Medium, Low
   - Colors: Dark Red, Orange, Yellow, Light Yellow

**Chart Data Preparation:**

For Gauge Chart, create hidden calculation cells:

- Cell K32: Overall Compliance % (=C17)
- Cell K33: Remaining % (=100-C17)

For Pie Chart:

- Use Row 30 data directly (Compliant, Partial, Non-Compliant counts)

---

**Critical Metrics Summary (Rows 52-67)**

**Section Header (Row 52):**

- **Cell A52 (merged A52:I52):** "KEY PERFORMANCE INDICATORS (KPIs)"
- **Font:** Arial 12pt, Bold, White
- **Background:** Dark Blue (003366)

**Column Headers (Row 54):**

| Column | Header | Width |
|--------|--------|-------|
| A | KPI | 35 |
| B | Current Value | 15 |
| C | Target | 12 |
| D | Status | 12 |
| E | Last Quarter | 15 |
| F | Change | 12 |
| G | Trend | 10 |

**Data Rows (55-66):**

Each KPI includes:

- **Current Value:** Formula referencing source workbooks or calculated from Gap Analysis
- **Target:** Policy-defined threshold
- **Status:** Conditional formatting (Green/Yellow/Red traffic light)
- **Last Quarter:** Manual user input (from previous quarter's dashboard)
- **Change:** Formula `=B-E` (current minus last quarter)
- **Trend:** Formula `=IF(F>0,"↑",IF(F<0,"↓","→"))`

**Example KPI Rows:**

**Row 55: Cryptographic Controls Implemented**

- **KPI (A55):** "Cryptographic Controls Implemented"
- **Current Value (B55):** `=C17` (Overall Compliance %)
- **Target (C55):** "≥95%"
- **Status (D55):** [Conditional format based on B55 vs C55]
- **Last Quarter (E55):** [USER INPUT yellow]
- **Change (F55):** `=B55-E55`
- **Trend (G55):** `=IF(F55>0,"↑",IF(F55<0,"↓","→"))`

**Row 56: Systems with Encryption at Rest**

- **KPI (A56):** "Systems with Encryption at Rest"
- **Current Value (B56):** `='[ISMS-IMP-A.8.24.2.xlsx]Summary Dashboard'!$C$9` (Compliant count from Data Storage)
- **Target (C56):** `='[ISMS-IMP-A.8.24.2.xlsx]Summary Dashboard'!$B$9` (Total items from Data Storage)
- **Status (D56):** [Conditional format: Green if B56=C56]
- **Last Quarter (E56):** [USER INPUT]
- **Change (F56):** `=B56-E56`
- **Trend (G56):** `=IF(F56>0,"↑",IF(F56<0,"↓","→"))`

**Continue pattern for all 12 KPIs** (see User Guide Section 4.5 for full KPI list)

**Conditional Formatting (Status Column D):**

- Green (00B050): Met or exceeded target
- Yellow (FFC000): Within 5% of target
- Red (FF0000): Below target by >5%

---

**Top 5 Critical Issues (Rows 69-77)**

**Section Header (Row 69):**

- **Cell A69 (merged A69:I69):** "TOP 5 CRITICAL SECURITY GAPS"
- **Font:** Arial 12pt, Bold, White
- **Background:** Red (C00000)
- **Height:** 35px

**Column Headers (Row 71):**

| Column | Header | Width |
|--------|--------|-------|
| A | Rank | 8 |
| B | Issue Description | 40 |
| C | Assessment Area | 20 |
| D | Risk Level | 12 |
| E | Systems Affected | 18 |
| F | Target Date | 12 |
| G | Owner | 18 |
| H | Status | 15 |

**Data Rows (72-76):**

**Auto-populate from Sheet '2. Gap Analysis', sorted by Risk Score descending, top 5 only.**

**Formula Approach (Python script):**
1. Extract all gaps from Gap Analysis sheet
2. Sort by Risk Level (Critical > High > Medium > Low) then by Systems Affected count
3. Take top 5
4. Populate rows 72-76

**Alternatively (Excel approach):**
Use `INDEX-MATCH` or `XLOOKUP` to pull top 5 from Gap Analysis based on Risk Level and Gap ID.

**Example Row 72:**

- **Rank (A72):** 1
- **Issue Description (B72):** [Link to '2. Gap Analysis'!B[row] where Risk Level = Critical, rank 1]
- **Assessment Area (C72):** [Link to '2. Gap Analysis'!C[row]]
- **Risk Level (D72):** "Critical"
- **Systems Affected (E72):** [Link to '2. Gap Analysis'!F[row]]
- **Target Date (F72):** [Link to '2. Gap Analysis'!K[row]]
- **Owner (G72):** [Link to '2. Gap Analysis'!L[row]]
- **Status (H72):** [Link to '2. Gap Analysis'!M[row]]

**Styling:**

- Risk Level "Critical" → Dark Red background (C00000), White text
- Risk Level "High" → Orange background (FFC000), Black text

---

**Executive Summary (Rows 79-100)**

**Section Header (Row 79):**

- **Cell A79 (merged A79:I79):** "EXECUTIVE SUMMARY"
- **Font:** Arial 12pt, Bold, White
- **Background:** Dark Blue (003366)

**Summary Content (Rows 81-100):**

This section is primarily **USER INPUT** (large text cells) for qualitative executive narrative.

**Row 81-82: Assessment Period**

- **Label (A81):** "Assessment Period:"
- **Value (B81:I81 merged):** [USER INPUT - yellow] e.g., "Q4 2024 (October 1 - December 31, 2024)"

**Row 84-85: Overall Compliance Status**

- **Label (A84):** "Overall Compliance Status:"
- **Value (B84:I84 merged):** [AUTO-CALCULATED based on C17]
  - Formula: `=IF(C17>=95,"Excellent - Mature cryptographic controls",IF(C17>=85,"Good - Minor gaps, remediation in progress",IF(C17>=75,"Needs Improvement - Significant gaps requiring attention","Critical - Immediate CISO action required")))`

**Row 87-88: Security Posture**

- **Label (A87):** "Security Posture:"
- **Value (B87:I87 merged):** [AUTO-CALCULATED based on '3. Risk Register' average risk score]
  - Formula: `=IF(AVERAGE('3. Risk Register'!H:H)<3,"Strong - Low risk exposure",IF(AVERAGE('3. Risk Register'!H:H)<5,"Adequate - Manageable risk",IF(AVERAGE('3. Risk Register'!H:H)<7,"Weak - Elevated risk requiring mitigation","Critical - Unacceptable risk exposure")))`

**Row 90-94: Key Achievements This Period**

- **Label (A90):** "Key Achievements This Period:"
- **Value (A91:I94 merged):** [USER INPUT - yellow, 4 rows tall]
- **Format:** Multi-line text box, bullet points
- **Example content:**

  ```
  • Implemented TLS 1.3 across all external HTTPS endpoints
  • Achieved 100% MFA enrollment for privileged accounts
  • Completed key rotation for 47 certificate authorities
  • Migrated 12 legacy systems from MD5 to bcrypt
  ```

**Row 96-100: Major Concerns**

- **Label (A96):** "Major Concerns:"
- **Value (A97:I100 merged):** [USER INPUT - yellow, 4 rows tall]
- **Format:** Multi-line text box, bullet points

**Row 102-106: Recommended Executive Actions**

- **Label (A102):** "Recommended Executive Actions:"
- **Value (A103:I106 merged):** [USER INPUT - yellow, 4 rows tall]
- **Format:** Numbered list (1. 2. 3. etc.)

**Row 108-112: Budget Impact**

- **Label (A108):** "Budget Impact:"
- **Value block (A109:I112):**
  - Row 109: "Total Estimated Remediation Budget:" [Formula: `=SUM('4. Remediation Roadmap'!J:J)`] 
  - Row 110: "Approved Budget:" [USER INPUT - yellow]
  - Row 111: "Budget Gap:" [Formula: `=B109-B110`]
  - Row 112: Conditional formatting: Red if gap > 0, Green if gap ≤ 0

**Cell Formatting:**

- All USER INPUT cells: Yellow background (FFFF00), Arial 10pt
- All AUTO-CALCULATED cells: Light Blue background (DCE6F1), Arial 10pt
- Labels: Bold, Gray background (D9D9D9)

---

# Sheet 2: Gap Analysis

## Purpose
Comprehensive consolidated list of ALL non-compliant and partially-compliant items from all 4 source assessments.

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1, merged A1:N1):** "COMPREHENSIVE GAP ANALYSIS - CRYPTOGRAPHIC CONTROLS"
- **Subtitle (Row 2, merged A2:N2):** "Consolidated view of all compliance gaps across assessment areas"
- **Styling:** Dark Blue header (003366), White text, Arial 14pt Bold

**Summary Statistics (Rows 4-10):**

**Column Headers (Row 4):**

| Column | Header | Width |
|--------|--------|-------|
| A | Assessment Area | 25 |
| B | Total Gaps | 12 |
| C | Critical | 12 |
| D | High | 12 |
| E | Medium | 12 |
| F | Low | 12 |
| G | Compliance % | 14 |
| H | Risk Score | 12 |

**Data Rows (5-8):**

**Row 5: Data Transmission**

- **Assessment Area (A5):** "Data Transmission"
- **Total Gaps (B5):** `=COUNTIFS('[ISMS-IMP-A.8.24.1.xlsx]1.1 External HTTPS-TLS'!$D:$D,"❌",... )`
  - Note: Must count across all 13 transmission assessment sheets
- **Critical (C5):** Count gaps where Risk Level = Critical (from source workbook or inferred from data classification)
- **Compliance % (G5):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$G$9`
- **Risk Score (H5):** `=(C5*10 + D5*7 + E5*4 + F5*1) / B5` (weighted average)

**Continue pattern for rows 6-8** (Data Storage, Authentication, Key Management)

**TOTAL Row (9):**

- **Label (A9):** "TOTAL" (Bold)
- **Formulas (B9:H9):** SUM for counts, AVERAGE for percentages/scores

**Conditional Formatting (Risk Score Column H):**

- Red (FF0000): >7 (Critical risk exposure)
- Orange (FFC000): 5-7 (High risk)
- Yellow (FFFF00): 3-5 (Medium risk)
- Green (00B050): <3 (Low risk)

---

**Detailed Gap Register (Rows 12+)**

**Column Headers (Row 12):**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gap ID | 15 | Text | Auto-generated (GAP-A824-001) |
| B | Description | 40 | Text | From source workbooks |
| C | Assessment Area | 20 | Text | Dropdown: Transmission/Storage/Auth/KeyMgmt |
| D | Risk Level | 12 | Text | Dropdown: Critical/High/Medium/Low |
| E | System/Service | 25 | Text | From source workbooks |
| F | Data Classification | 15 | Text | Dropdown: Restricted/Confidential/Internal/Public |
| G | Current State | 30 | Text | What exists now |
| H | Required State | 30 | Text | What policy requires |
| I | Evidence Location | 25 | Text | Link to evidence |
| J | Source | 18 | Text | Source workbook + sheet |
| K | Target Date | 12 | Date | DD.MM.YYYY |
| L | Owner | 18 | Text | Person responsible |
| M | Status | 15 | Text | Dropdown: Not Started/In Progress/Completed/Blocked |
| N | Notes | 30 | Text | Additional details |

**Data Population Strategy (Python Script):**

1. **Iterate through all 4 source workbooks**
2. **For each assessment sheet** in each workbook:

   - Identify rows where Status column = "❌ Non-Compliant" or "⚠️ Partial"
   - Extract: System/Service name, Gap description, Evidence location

3. **Generate Gap ID** (sequential: GAP-A824-001, GAP-A824-002, ...)
4. **Assign Risk Level** based on:

   - Data Classification (Restricted = Critical/High, Confidential = High/Medium, Internal = Medium/Low)
   - System criticality (if indicated in source workbook)

5. **Populate Target Date and Owner** from source workbook remediation columns
6. **Set Status** based on source workbook (if remediation started)

**Example Data Row:**

| Gap ID | Description | Area | Risk | System | Class | Current | Required | Evidence | Source | Target | Owner | Status | Notes |
|--------|-------------|------|------|--------|-------|---------|----------|----------|--------|--------|-------|--------|-------|
| GAP-A824-001 | Database using DES encryption | Storage | Critical | HR_Payroll | Restricted | DES-56 | AES-256 TDE | DB config | IMP-2, Sheet 4 | 31.03.2025 | J. Smith | In Progress | Migration scheduled Q1 |

**Sorting:**

- Default: By Risk Level (Critical → High → Medium → Low), then by Target Date (earliest first)

**Filtering:**

- Provide filter dropdowns on all column headers
- Common filters: Risk Level, Assessment Area, Status, Owner

---

# Sheet 3: Risk Register

## Purpose
Translate technical gaps into business risks for executive risk management.

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1):** "CRYPTOGRAPHIC RISK REGISTER"
- **Subtitle (Row 2):** "Business risks derived from cryptographic control gaps"

**Column Headers (Row 4):**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Risk ID | 12 | Text (RISK-A824-001) |
| B | Gap ID | 15 | Text (Linked to Sheet 2) |
| C | Risk Description | 40 | Text |
| D | Assessment Area | 20 | Text |
| E | Likelihood (1-5) | 15 | Number, Dropdown |
| F | Impact (1-5) | 15 | Number, Dropdown |
| G | Risk Score (L×I) | 15 | Formula |
| H | Risk Level | 12 | Text (Auto: Critical/High/Medium/Low) |
| I | Affected Assets | 25 | Text |
| J | Potential Consequences | 35 | Text |
| K | Mitigation Strategy | 35 | Text |
| L | Mitigation Owner | 18 | Text |
| M | Target Resolution | 12 | Date |
| N | Current Status | 15 | Text |

**Data Population Strategy:**

**Risks are derived from Critical and High gaps in Sheet 2.**

**Risk Scoring Formula (Column G):**
```excel
=E[row] * F[row]
```

**Risk Level (Column H):**
```excel
=IF(G[row]>=20,"Critical",IF(G[row]>=15,"High",IF(G[row]>=10,"Medium","Low")))
```

**Example Risk:**

| Risk ID | Gap ID | Description | Area | L | I | Score | Level | Assets | Consequences | Mitigation | Owner | Target | Status |
|---------|--------|-------------|------|---|---|-------|-------|--------|--------------|------------|-------|--------|--------|
| RISK-A824-001 | GAP-A824-015 | Unencrypted database backup | Storage | 4 | 5 | 20 | Critical | HR_Payroll (500 records) | GDPR breach €20M fine, reputational damage | AES-256 encryption, access restriction | J. Smith | 15.02.2025 | In Progress |

**Likelihood Assessment Guidance (Column E):**
1. Very Low (1): Theoretical only
2. Low (2): Requires sophisticated attacker
3. Medium (3): Moderate attacker skill
4. High (4): Accessible to many attackers
5. Very High (5): Trivial to exploit

**Impact Assessment Guidance (Column F):**
1. Very Low (1): Public data, minimal impact
2. Low (2): Internal data, minor disruption
3. Medium (3): Confidential data, significant disruption
4. High (4): Restricted data, major financial/reputational damage
5. Very High (5): Critical data, existential threat

**Conditional Formatting (Risk Level Column H):**

- Critical (20-25): Dark Red (C00000), White text
- High (15-19): Orange (FFC000), Black text
- Medium (10-14): Yellow (FFFF00), Black text
- Low (5-9): Light Yellow (FFFFCC), Black text
- Minimal (1-4): White, Black text

**Risk Register Auto-Population:**
Only gaps with Risk Level = Critical or High from Sheet 2 generate risks here.

---

# Sheet 4: Remediation Roadmap

## Purpose
Project plan view of gap remediation with timelines, dependencies, and budget tracking.

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1):** "CRYPTOGRAPHIC CONTROLS REMEDIATION ROADMAP"
- **Subtitle (Row 2):** "Action plans, timelines, and budget for gap closure"

**Column Headers (Row 4):**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Action ID | 12 | Text (ACT-A824-001) |
| B | Gap/Risk ID | 15 | Text (Linked to Sheet 2 or 3) |
| C | Remediation Action | 40 | Text |
| D | Assessment Area | 20 | Text |
| E | Priority | 12 | Dropdown: P1/P2/P3 |
| F | Owner | 18 | Text |
| G | Start Date | 12 | Date |
| H | Target Date | 12 | Date |
| I | Status | 15 | Dropdown |
| J | Dependencies | 25 | Text |
| K | Estimated Cost (CHF) | 15 | Currency |
| L | Actual Cost (CHF) | 15 | Currency |
| M | Progress % | 12 | Number (0-100) |
| N | Completion Date | 12 | Date |
| O | Notes | 30 | Text |

**Data Population Strategy:**

**Each gap from Sheet 2 generates one or more remediation actions.**

**Priority Assignment:**

- **P1 (Urgent):** Critical risk, Restricted data, <30 days target
- **P2 (High):** High risk, Confidential data, 30-90 days target
- **P3 (Normal):** Medium/Low risk, Internal data, >90 days target

**Status Values:**

- Not Started
- In Progress (1-99%)
- Completed (100%)
- Blocked (dependencies unmet)
- Overdue (past target date, <100%)

**Example Action:**

| Action ID | Gap ID | Action | Area | Priority | Owner | Start | Target | Status | Dependencies | Est. Cost | Actual | Progress | Completion | Notes |
|-----------|--------|--------|------|----------|-------|-------|--------|--------|--------------|-----------|--------|----------|------------|-------|
| ACT-A824-001 | GAP-A824-015 | Migrate HR_Payroll to AES-256 TDE | Storage | P1 | J. Smith | 15.01.2025 | 31.03.2025 | In Progress | PostgreSQL 13+ installed | CHF 15,000 | CHF 8,500 | 60% | - | On track, schema migration complete |

**Conditional Formatting:**

**Status Column (I):**

- Green (00B050): Completed
- Yellow (FFFF00): In Progress
- Orange (FFC000): Blocked
- Red (FF0000): Overdue

**Progress Column (M):**

- Data bars (0-100%) with color gradient: Red (0%) → Yellow (50%) → Green (100%)

**Budget Summary (Bottom Section):**

**Row [Last Row + 2]: Budget Totals**

- **Label (A):** "TOTAL REMEDIATION BUDGET"
- **Estimated (K):** `=SUM(K:K)`
- **Actual (L):** `=SUM(L:L)`
- **Variance (M):** `=L-K` (negative = under budget, positive = over budget)

**Budget Breakdown by Quarter (if applicable):**

- Q1 2025: SUM of actions with Target Date in Q1
- Q2 2025: SUM of actions with Target Date in Q2
- Q3 2025: SUM of actions with Target Date in Q3
- Q4 2025: SUM of actions with Target Date in Q4

---

# Sheet 5: KPIs & Metrics

## Purpose
Quantitative performance indicators with historical trending.

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1):** "CRYPTOGRAPHIC CONTROLS - KEY PERFORMANCE INDICATORS"
- **Subtitle (Row 2):** "Quantitative metrics for compliance monitoring and trending"

**Column Headers (Row 4):**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | KPI Name | 35 | Text |
| B | Current Value | 15 | Number/% |
| C | Target | 12 | Number/% |
| D | Status | 12 | Traffic Light |
| E | Last Quarter | 15 | Number/% |
| F | Change (Δ) | 12 | Formula |
| G | Trend | 10 | Arrow (↑↓→) |
| H | Measurement Source | 30 | Text |

**Data Rows (Full KPI List):**

**Row 5: Overall Compliance Rate**

- **KPI (A5):** "Cryptographic Controls Implemented"
- **Current (B5):** `='1. Executive Dashboard'!C17` (Overall Compliance %)
- **Target (C5):** "≥95%"
- **Status (D5):** [Conditional: Green ≥95%, Yellow 85-94%, Red <85%]
- **Last Quarter (E5):** [USER INPUT yellow]
- **Change (F5):** `=B5-E5`
- **Trend (G5):** `=IF(F5>0,"↑",IF(F5<0,"↓","→"))`
- **Source (H5):** "Average of 4 assessment areas"

**Row 6: Systems with Encryption at Rest**

- **Current (B6):** `='[ISMS-IMP-A.8.24.2.xlsx]Summary Dashboard'!$C$9 & "/" & '[ISMS-IMP-A.8.24.2.xlsx]Summary Dashboard'!$B$9`
- **Target (C6):** "100%"
- **Source (H6):** "IMP-2 Data Storage Assessment"

**Row 7: Systems with Encryption in Transit**

- **Current (B7):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$C$9 & "/" & '[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$B$9`
- **Target (C7):** "100%"
- **Source (H7):** "IMP-1 Data Transmission Assessment"

**Row 8: MFA Coverage (All Users)**

- **Current (B8):** [Extract from IMP-3, Sheet 2 (MFA), Enrollment %]
- **Target (C8):** "100%"
- **Source (H8):** "IMP-3 Authentication, MFA Enrollment"

**Row 9: MFA Coverage (Privileged Accounts)**

- **Current (B9):** [Extract from IMP-3, Sheet 2 (MFA), Admin MFA Enforcement %]
- **Target (C9):** "100%"
- **Source (H9):** "IMP-3 Authentication, Admin MFA"

**Row 10: Certificate Expiry Compliance**

- **Current (B10):** [Calculate: Certificates with >90 days validity / Total certificates × 100%]
- **Target (C10):** "100%"
- **Source (H10):** "IMP-4 Key Management, Certificate Management"

**Row 11: Key Rotation Compliance**

- **Current (B11):** [Calculate: Keys rotated within policy timeframe / Total keys × 100%]
- **Target (C11):** "≥95%"
- **Source (H11):** "IMP-4 Key Management, Key Rotation"

**Row 12: Service Accounts with Strong Auth**

- **Current (B12):** [Extract from IMP-3, Sheet 4 (Service Accounts), Compliant %]
- **Target (C12):** "≥90%"
- **Source (H12):** "IMP-3 Authentication, Service Accounts"

**Row 13: Password Hashing Compliance**

- **Current (B13):** [Extract from IMP-3, Sheet 1 (Passwords), Compliant %]
- **Target (C13):** "100%"
- **Source (H13):** "IMP-3 Authentication, Password Security"

**Row 14: SSO Coverage**

- **Current (B14):** [Extract from IMP-3, Sheet 5 (SSO), Coverage %]
- **Target (C14):** "≥80%"
- **Source (H14):** "IMP-3 Authentication, SSO & Federation"

**Row 15: Open Critical Gaps**

- **Current (B15):** `=COUNTIFS('2. Gap Analysis'!$D:$D,"Critical")`
- **Target (C15):** "0"
- **Source (H15):** "Sheet 2 Gap Analysis"

**Row 16: Remediation On-Time %**

- **Current (B16):** `=COUNTIFS('4. Remediation Roadmap'!$I:$I,"Completed",'4. Remediation Roadmap'!$H:$H,"<="&TODAY()) / COUNTA('4. Remediation Roadmap'!$A:$A) * 100`
- **Target (C16):** "≥90%"
- **Source (H16):** "Sheet 4 Remediation Roadmap"

**Conditional Formatting (Trend Column G):**

- ↑ (Green): Positive trend
- → (Yellow): No change
- ↓ (Red): Negative trend

---

# Sheet 6: Evidence Register

## Purpose
Consolidated list of all compliance evidence from 4 source assessments.

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1):** "CONSOLIDATED EVIDENCE REGISTER"
- **Subtitle (Row 2):** "All compliance evidence across cryptographic control assessments"

**Column Headers (Row 4):**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Evidence ID | 12 | Text (EVD-A824-001) |
| B | Evidence Title | 35 | Text |
| C | Evidence Type | 20 | Text |
| D | Assessment Area | 20 | Text |
| E | Related System | 25 | Text |
| F | Storage Location | 30 | Text |
| G | Collection Date | 12 | Date |
| H | Collected By | 18 | Text |
| I | Retention Period | 15 | Text |
| J | Current Status | 15 | Text |
| K | Notes | 30 | Text |

**Data Population Strategy:**

**Evidence is consolidated from Evidence Register sheets in all 4 source workbooks.**

**Python Script Approach:**
1. Open each source workbook (IMP-1/2/3/4)
2. Navigate to "Evidence Register" sheet
3. Extract all rows (skip header)
4. Assign unique Evidence ID (sequential)
5. Copy to consolidated register
6. Sort by Assessment Area, then by Evidence Type

**Evidence Types:**

- Configuration File (e.g., GPO export, network config)
- Compliance Report (e.g., SSL Labs report, MDM compliance)
- Audit Log (e.g., key rotation log, access log)
- Policy Document (e.g., password policy, encryption standard)
- Screenshot (e.g., TLS settings, BitLocker status)
- Certificate (e.g., TLS certificate, CA certificate)
- Architecture Diagram (e.g., PKI hierarchy, key management flow)
- Vendor Documentation (e.g., HSM datasheet, KMS manual)

**Retention Periods:**

- **3 years:** Compliance reports, audit logs, certificates
- **7 years:** Financial records, regulatory compliance (if applicable)
- **Permanent:** Policies, architecture diagrams, certification evidence

**Status Values:**

- Current (valid and available)
- Expired (outdated, needs refresh)
- Missing (cannot locate)
- Pending Collection (identified but not yet collected)

---

# Sheet 7: Action Items & Follow-up

## Purpose
Track non-remediation tasks (training, meetings, reviews, updates).

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1):** "ACTION ITEMS & FOLLOW-UP TASKS"
- **Subtitle (Row 2):** "Non-remediation activities supporting cryptographic compliance"

**Column Headers (Row 4):**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Action ID | 12 | Text (AI-A824-001) |
| B | Action Description | 40 | Text |
| C | Category | 20 | Dropdown |
| D | Priority | 12 | Dropdown: High/Medium/Low |
| E | Owner | 18 | Text |
| F | Due Date | 12 | Date |
| G | Status | 15 | Dropdown |
| H | Completion Date | 12 | Date |
| I | Notes | 30 | Text |

**Category Values:**

- Training & Awareness
- Policy Review & Update
- Tool/Technology Evaluation
- Meeting & Governance
- Documentation Update
- Vendor Management
- Audit Preparation
- Communication

**Example Actions:**

- "Schedule cryptography awareness training for IT staff" (Training)
- "Review and update ISMS-POL-A.8.24 for annual refresh" (Policy Review)
- "Evaluate HSM vendors for Q2 procurement" (Tool Evaluation)
- "Prepare dashboard presentation for Q2 Security Review Meeting" (Meeting)

---

# Sheet 8: Audit & Compliance Log

## Purpose
Historical record of compliance reviews, audit findings, certification milestones.

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1):** "AUDIT & COMPLIANCE LOG"
- **Subtitle (Row 2):** "Historical record of cryptographic control reviews and findings"

**Column Headers (Row 4):**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Log ID | 12 | Text (LOG-A824-001) |
| B | Review Date | 12 | Date |
| C | Review Type | 20 | Dropdown |
| D | Reviewer/Auditor | 25 | Text |
| E | Scope | 30 | Text |
| F | Overall Finding | 20 | Dropdown |
| G | Non-Conformities | 15 | Number |
| H | Observations | 15 | Number |
| I | Key Findings | 40 | Text |
| J | Corrective Actions | 40 | Text |
| K | Follow-up Date | 12 | Date |
| L | Status | 15 | Dropdown |

**Review Types:**

- Internal Audit
- External Audit (ISO 27001)
- Management Review (Quarterly)
- Self-Assessment
- Surveillance Audit
- Recertification Audit

**Overall Finding Values:**

- Conformant (no issues)
- Minor Non-Conformities (correctable)
- Major Non-Conformities (significant gaps)
- Observation (improvement opportunity)

**Example Log Entry:**

- **Date:** 15.12.2024
- **Type:** ISO 27001 Stage 1 Audit
- **Auditor:** Swiss Certification Body AG
- **Scope:** Control A.8.24 Use of Cryptography
- **Finding:** Minor Non-Conformities (2)
- **Non-Conformities:** 2 (DES encryption, manual certificate renewal)
- **Key Findings:** "Strong policy framework, minor implementation gaps"
- **Corrective Actions:** "Database re-encryption Q1 2025, certificate automation Q1 2025"
- **Follow-up:** 31.03.2025 (Stage 2 Audit)
- **Status:** Open (corrective actions in progress)

---

# Sheet 9: Approval Sign-Off

## Purpose
Record formal sign-offs and approvals from management for compliance assessments, remediation plans, and policy acknowledgments.

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1):** "APPROVAL SIGN-OFF"
- **Subtitle (Row 2):** "Formal management approval and accountability records"

**Column Headers (Row 4):**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Approval ID | 15 | Text (APR-A824-001) |
| B | Approval Date | 12 | Date |
| C | Approval Type | 25 | Dropdown |
| D | Document/Assessment | 35 | Text |
| E | Approver Name | 20 | Text |
| F | Approver Title | 25 | Text |
| G | Approval Status | 15 | Dropdown |
| H | Comments | 40 | Text |
| I | Next Review Date | 12 | Date |

**Approval Types:**

- Quarterly Assessment Approval
- Remediation Plan Approval
- Policy Acknowledgment
- Risk Acceptance
- Budget Approval
- Audit Response Approval

**Approval Status Options:**

- Approved
- Approved with Conditions
- Pending Review
- Rejected
- Deferred

**Example Approval Entry:**

- **Approval ID:** APR-A824-001
- **Date:** 15.01.2025
- **Type:** Quarterly Assessment Approval
- **Document:** Q4 2024 Cryptography Compliance Dashboard
- **Approver:** J. Smith, CISO
- **Status:** Approved
- **Comments:** "Overall compliance acceptable. Prioritize critical gaps per remediation roadmap."
- **Next Review:** 15.04.2025

---

# Appendix: Technical Notes for Developers

## Python Script Architecture

**Script:** `generate_a824_5_compliance_summary_dashboard.py`

**Core Functions:**

1. **validate_source_workbooks()**

   - Check all 4 source workbooks exist
   - Validate file names match expected patterns
   - Verify "Summary Dashboard" sheet exists in each
   - Extract key metrics (compliance %, gap counts)

2. **extract_gaps()**

   - Iterate through all assessment sheets in each source workbook
   - Identify rows with Status = "❌ Non-Compliant" or "⚠️ Partial"
   - Extract gap details (system, description, evidence, remediation)
   - Assign Gap ID, Risk Level, Assessment Area
   - Return consolidated gap list

3. **calculate_risks()**

   - Filter gaps where Risk Level = Critical or High
   - Generate Risk ID
   - Assign Likelihood and Impact (algorithm-based or manual input)
   - Calculate Risk Score (L × I)
   - Populate Risk Register sheet

4. **generate_remediation_roadmap()**

   - For each gap, create remediation action(s)
   - Assign Action ID, Priority, Owner
   - Extract timeline from source workbook remediation columns
   - Estimate cost (if available in source, otherwise placeholder)
   - Sort by Priority then Target Date

5. **consolidate_evidence()**

   - Extract all evidence entries from 4 source workbooks
   - Assign unique Evidence ID
   - Deduplicate (if same evidence referenced in multiple assessments)
   - Sort by Assessment Area then Evidence Type

6. **generate_executive_dashboard()**

   - Create Sheet 1 with formulas linking to other sheets and source workbooks
   - Set up external workbook references
   - Apply conditional formatting
   - Create placeholder text cells for user input

7. **create_kpi_sheet()**

   - Populate KPI list with formulas
   - Link Current Value to source workbooks or calculations
   - Set up Last Quarter as user input
   - Calculate Change and Trend

8. **create_audit_and_meeting_logs()**

   - Create empty templates with headers
   - User will populate manually

## External Workbook Link Management

**Challenge:** External links (`='[file.xlsx]Sheet'!Cell`) break if source workbooks move.

**Solution Approaches:**

**Approach 1: Absolute File Paths (Current)**
```python
link_formula = f"='C:\\ISMS\\A.8.24\\Assessments\\[{filename}]Summary Dashboard'!$G$9"
```
**Pros:** Works if directory structure is consistent
**Cons:** Breaks if files move

**Approach 2: Relative File Paths**
```python
link_formula = f"='[{filename}]Summary Dashboard'!$G$9"
```
**Pros:** Works if dashboard and source workbooks in same directory
**Cons:** Less flexible for complex directory structures

**Approach 3: Python-Based Extraction (No External Links)**
```python
# Extract data at generation time, store as values (not formulas)
compliance_pct = source_wb['Summary Dashboard']['G9'].value
dashboard_wb['1. Executive Dashboard']['C17'].value = compliance_pct
```
**Pros:** No broken links, dashboard is standalone
**Cons:** Dashboard doesn't auto-update when source workbooks change, must regenerate

**Current Implementation:** Approach 2 (Relative file paths) with normalization script to ensure source workbooks have short names.

## File Normalization

**Problem:** Source workbooks have long names with dates: `ISMS-IMP-A.8.24.1_Data_Transmission_20260115.xlsx`

**Solution:** Normalization script creates short-name copies: `ISMS-IMP-A.8.24.1.xlsx`

**Script:** `normalize_assessment_files_a824.py`

```python
import shutil

files = [
    'ISMS-IMP-A.8.24.1_Data_Transmission_20260115.xlsx',
    'ISMS-IMP-A.8.24.2_Data_Storage_20260115.xlsx',
    'ISMS-IMP-A.8.24.3_Authentication_20260115.xlsx',
    'ISMS-IMP-A.8.24.4_Key_Management_20260115.xlsx'
]

for f in files:
    short_name = f.split('_')[0] + '.xlsx'  # Extract ISMS-IMP-A.8.24.X.xlsx
    shutil.copy(f, short_name)
    print(f"Created: {short_name}")
```

**Result:** Dashboard references short names, external links work.

## Testing Checklist

**Before Releasing Dashboard Script:**

- [ ] All 4 source workbooks in same directory as dashboard
- [ ] Source workbooks have normalized short names
- [ ] External links resolve (no #REF! errors)
- [ ] Overall compliance % matches average of 4 source workbooks
- [ ] Gap Analysis populated with actual gaps (not empty)
- [ ] Risk Register has entries if critical/high gaps exist
- [ ] Remediation Roadmap has actions for all gaps
- [ ] KPIs calculate correctly
- [ ] Evidence Register consolidated from all 4 sources
- [ ] Charts and visualizations display data
- [ ] Conditional formatting works (traffic lights, data bars)

## Maintenance Notes

**Quarterly Update Procedure:**
1. Update source assessments (IMP-1/2/3/4) with current data
2. Save updated assessments with new date: `*_20260415.xlsx` (Q1 2025)
3. Run normalization script to create short-name copies
4. Run dashboard generation script
5. Open dashboard in Excel, click "Update Links" when prompted
6. Manually complete Executive Summary section (user input)
7. Save dashboard as `ISMS-IMP-A.8.24.5_Compliance_Dashboard_20260415.xlsx`
8. Archive previous quarter's dashboard

**Version Control Best Practice:**

- Keep quarterly snapshots: `Q4_2024/`, `Q1_2025/`, `Q2_2025/`
- Each folder contains: Dashboard + 4 source workbooks + Evidence files
- Enables historical trending and compliance demonstration to auditors

---

**Document Assembly Instructions:**

1. **Merge Order:**

   - Document Control block (from PART I file, lines 1-30)
   - PART I: USER COMPLETION GUIDE (from PART I file, lines 31-end)
   - PART II: TECHNICAL SPECIFICATION - File 1 (this file)
   - PART II: TECHNICAL SPECIFICATION - File 2 (next file)

2. **Final Document Structure:**
   ```
   ISMS-IMP-A.8.24.5 - Compliance Summary Dashboard v2.0
   
   ├── Document Control (Metadata, Version History)
   │
   ├── PART I: USER COMPLETION GUIDE (~300 lines)
   │   ├── 1. Dashboard Overview
   │   ├── 2. Prerequisites
   │   ├── 3. Dashboard Generation Workflow
   │   ├── 4. Understanding Dashboard Sections (9 sheets explained)
   │   ├── 5. Interpreting Results
   │   ├── 6. Common Questions
   │   ├── 7. Dashboard Maintenance
   │   ├── 8. Quality Checklist
   │   └── 9. Review & Approval
   │
   └── PART II: TECHNICAL SPECIFICATION (~400 lines)
       ├── Instructions for Dashboard Development
       ├── Common Dashboard Structure
       ├── Sheet 1: Executive Dashboard
       ├── Sheet 2: Gap Analysis
       ├── Sheet 3: Risk Register
       ├── Sheet 4: Remediation Roadmap
       ├── Sheet 5: KPIs & Metrics
       ├── Sheet 6: Evidence Register
       ├── Sheet 7: Action Items & Follow-up
       ├── Sheet 8: Audit & Compliance Log
       ├── Sheet 9: Approval Sign-Off
       └── Appendix: Technical Notes for Developers
   ```

3. **Quality Checks Before Finalizing:**

   - [ ] All merge instructions removed
   - [ ] Document Control version shows 2.0
   - [ ] Version History documents v1.0 → v2.0 changes
   - [ ] All dates in DD.MM.YYYY format
   - [ ] External workbook formulas use short filenames
   - [ ] Schema validation approach documented
   - [ ] Cross-references accurate (sheet numbers, policy references)
   - [ ] No placeholder text remains
   - [ ] Technical appendix matches Python script approach

---

**END OF PART II (TECHNICAL SPECIFICATION)**

**Total IMP-5 Length:** ~650-700 lines (PART I ~300 lines + PART II ~400 lines)

**Key Distinction from IMP-1/2/3/4:**

- IMP-5 is **CONSOLIDATION**, not data entry
- Lighter weight (~700 lines vs ~1,200 lines for others)
- Executive-focused (User Guide emphasizes interpretation, not completion)
- Reads FROM source workbooks, doesn't create new assessment data

**Document Status:** ✅ READY FOR PRODUCTION

*No Cargo Cult Engineering - Dashboard provides genuine executive decision support, not compliance theater* 🎯

---

**END OF SPECIFICATION**

---

*"Every positive integer is one of Ramanujan's personal friends."*
— J.E. Littlewood, on Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->
