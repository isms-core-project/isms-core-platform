**ISMS-IMP-A.5.9.3-TG - Quality & Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Inventory Quality & Policy Compliance Verification |
| **Related Policy** | ISMS-POL-A.5.9, Section 2.3 (Mandatory Attributes), Section 2.5 (Quality Standards), Section 3 (Assessment Methodology) |
| **Purpose** | Verify inventory data quality (accuracy, completeness, currency) and compliance with policy requirements |
| **Target Audience** | Security Team, Quality Assurance, CMDB Administrators, Auditors |
| **Assessment Type** | Quality Verification & Compliance Audit |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial assessment specification following consolidated policy structure | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.9.3-UG.

---

# Technical Specification

**Audience:** Workbook developers (Python/Excel script maintainers)

---

## Document Overview

### Purpose of Technical Specification

This section provides complete technical specifications for developers creating or maintaining the Python script that generates the Quality & Compliance Assessment workbook.

**Python Script**: `generate_a59_3_quality_compliance.py`

**Generated Workbook**: `ISMS_A_5_9_Quality_Compliance_Assessment_YYYYMMDD.xlsx`

**Key Design Principles**:
1. **Statistical Rigor**: Proper sampling methodology, valid extrapolation
2. **Automated Calculations**: Quality scores, compliance percentages auto-calculated
3. **Evidence-Based**: Every assertion backed by documented evidence
4. **Audit-Ready**: Professional appearance, clear methodology documentation
5. **Trending Capable**: Design supports quarter-over-quarter comparison

---

## Excel Workbook Structure

### Workbook Metadata

**Workbook Properties**:

- **Title**: ISMS A.5.9 Quality & Compliance Assessment
- **Subject**: ISO/IEC 27001:2022 Control A.5.9 - Inventory Quality Verification
- **Author**: [Organization] ISMS Implementation Team
- **Company**: [Organization]
- **Created**: [Generation Date]
- **Version**: 1.0

### Sheet Summary

| Sheet # | Sheet Name | Purpose | User Input | Formulas | Protection |
|---------|-----------|---------|------------|----------|-----------|
| 1 | Instructions | User guide and methodology | None (read-only) | None | Full |
| 2 | Accuracy Sampling | Sample assets and verify | Yes | Accuracy % calcs | Partial |
| 3 | Completeness Assessment | Mandatory attribute check | Yes | Completeness % calcs | Partial |
| 4 | Currency Assessment | Staleness verification | Yes | Currency % calcs | Partial |
| 5 | Consistency Checks | Contradiction detection | Yes | Failure rate calcs | Partial |
| 6 | Policy Compliance Matrix | SHALL requirement verification | Yes | Compliance % calcs | Partial |
| 7 | Quality Metrics & Scoring | Aggregate quality scores | Auto-populated | All metrics | Partial |
| 8 | Evidence Register | Evidence documentation | Yes | None | Partial |

---

## Global Styling Standards

### Color Palette (Hex Codes)

Same as IMP-A.5.9-1 and IMP-A.5.9-2 (refer to those documents for detailed specifications).

---

## Sheet 1: Instructions - Technical Specification

Same pattern as IMP-A.5.9-1 and IMP-A.5.9-2, adapted for quality assessment:

- Title: ISMS A.5.9 Quality & Compliance Assessment
- Subtitle: Data Quality Verification & Policy Compliance Audit
- Overview section: 5 quality dimensions explained
- Sampling methodology: Sample size calculation, stratification
- Workflow diagram: 8-phase assessment process
- Color coding legend
- Support information

---

## Sheet 2: Accuracy Sampling - Complete Specification

### Purpose

Document random sample selection and accuracy verification results.

### Column Structure

**Total Columns: 15 (A through O)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Sample ID | 12 | Text | Pattern QA-NNN | None | No |
| B | Asset Category | 20 | List | Dropdown | None | No |
| C | Asset ID | 15 | Text | None | None | No |
| D | Asset Name | 30 | Text | None | None | No |
| E | Attribute to Verify | 25 | Text | None | None | No |
| F | Inventory Value | 30 | Text | None | None | No |
| G | Actual Value | 30 | Text | None | None | No |
| H | Match? | 15 | List | Dropdown | None | No |
| I | Discrepancy Type | 20 | List | Dropdown | None | No |
| J | Impact | 15 | List | Dropdown | None | No |
| K | Root Cause | 35 | Text | None | None | No |
| L | Verification Method | 30 | Text | None | None | No |
| M | Verification Date | 15 | Date | Date validation | None | No |
| N | Verified By | 20 | Text | None | None | No |
| O | Notes | 30 | Text | None | None | No |

### Header Row Formatting

Same styling as IMP-A.5.9-1/2 (dark blue header, white text, wrapped text).

### Data Validation Lists

**Column A: Sample ID - Pattern Validation**

```python
dv_sample_id = DataValidation(
    type="custom",
    formula1='=AND(LEN(A3)=6,LEFT(A3,3)="QA-",ISNUMBER(VALUE(RIGHT(A3,3))))',
    allow_blank=False,
    showErrorMessage=True,
    errorTitle="Invalid Sample ID",
    error="Sample ID must be in format QA-NNN (e.g., QA-001, QA-002)"
)
dv_sample_id.add('A3:A200')
ws.add_data_validation(dv_sample_id)

dv_sample_id.promptTitle = "Sample ID Format"
dv_sample_id.prompt = "Enter ID in format QA-001, QA-002, etc."
dv_sample_id.showInputMessage = True
```

**Column B: Asset Category**

```python
asset_categories = [
    "Information Assets",
    "IT Infrastructure",
    "Applications",
    "Physical Assets",
    "Personnel Assets"
]

dv_asset_cat = DataValidation(
    type="list",
    formula1=f'"{",".join(asset_categories)}"',
    allow_blank=False
)
dv_asset_cat.add('B3:B200')
ws.add_data_validation(dv_asset_cat)
```

**Column H: Match?**

```python
match_options = [
    "Yes (Accurate)",
    "No (Inaccurate)",
    "Cannot Verify"
]

dv_match = DataValidation(
    type="list",
    formula1=f'"{",".join(match_options)}"',
    allow_blank=False
)
dv_match.add('H3:H200')
ws.add_data_validation(dv_match)
```

**Column I: Discrepancy Type** (enabled only if H = "No")

```python
discrepancy_types = [
    "Wrong Value",
    "Outdated",
    "Missing",
    "Duplicate",
    "Other"
]

dv_discrepancy = DataValidation(
    type="list",
    formula1=f'"{",".join(discrepancy_types)}"',
    allow_blank=True  # Can be blank if Match=Yes
)
dv_discrepancy.add('I3:I200')
ws.add_data_validation(dv_discrepancy)
```

**Column J: Impact**

```python
impacts = [
    "Critical",
    "High",
    "Medium",
    "Low",
    "Informational"
]

dv_impact = DataValidation(
    type="list",
    formula1=f'"{",".join(impacts)}"',
    allow_blank=True
)
dv_impact.add('J3:J200')
ws.add_data_validation(dv_impact)
```

**Column M: Verification Date**

```python
dv_verify_date = DataValidation(
    type="date",
    operator="lessThanOrEqual",
    formula1=datetime.now().strftime('%Y-%m-%d'),
    allow_blank=False,
    showErrorMessage=True,
    errorTitle="Invalid Date",
    error="Verification date cannot be in the future"
)
dv_verify_date.add('M3:M200')
ws.add_data_validation(dv_verify_date)
```

### Conditional Formatting

**Column H: Match? - Color Coding**

```python
from openpyxl.formatting.rule import ContainsText

# Green: "Yes (Accurate)"
accurate_rule = ContainsText(
    text='Yes',
    fill=PatternFill(start_color='C6EFCE', fill_type='solid'),
    font=Font(color='006100', bold=True)
)
ws.conditional_formatting.add('H3:H200', accurate_rule)

# Red: "No (Inaccurate)"
inaccurate_rule = ContainsText(
    text='No',
    fill=PatternFill(start_color='FFC7CE', fill_type='solid'),
    font=Font(color='9C0006', bold=True)
)
ws.conditional_formatting.add('H3:H200', inaccurate_rule)

# Yellow: "Cannot Verify"
cannot_verify_rule = ContainsText(
    text='Cannot',
    fill=PatternFill(start_color='FFEB9C', fill_type='solid'),
    font=Font(color='9C5700', bold=True)
)
ws.conditional_formatting.add('H3:H200', cannot_verify_rule)
```

**Column J: Impact - Color Coding**

```python
# Red: Critical
critical_rule = ContainsText(text='Critical', fill=PatternFill(start_color='FFC7CE', fill_type='solid'))
ws.conditional_formatting.add('J3:J200', critical_rule)

# Orange: High
high_rule = ContainsText(text='High', fill=PatternFill(start_color='FFEB9C', fill_type='solid'))
ws.conditional_formatting.add('J3:J200', high_rule)
```

### Summary Section (Below Sample Data)

**Location**: Rows 205-220

**Accuracy Metrics**:

| Metric | Location | Formula |
|--------|----------|---------|
| Total Sample Size | A205 | `=COUNTA(A3:A200)` |
| Verifiable Records | A206 | `=COUNTIF(H3:H200,"<>Cannot Verify")` |
| Accurate Records | A207 | `=COUNTIF(H3:H200,"Yes (Accurate)")` |
| Inaccurate Records | A208 | `=COUNTIF(H3:H200,"No (Inaccurate)")` |
| Cannot Verify | A209 | `=COUNTIF(H3:H200,"Cannot Verify")` |
| **Accuracy Rate %** | **A210** | **`=A207/A206*100`** (locked, bold, large font) |

**Accuracy by Category**:

```python
# Create pivot-style summary
categories = ["Information Assets", "IT Infrastructure", "Applications", "Physical Assets", "Personnel Assets"]

for idx, category in enumerate(categories, start=212):
    ws[f'A{idx}'] = category
    # Count accurate for this category
    ws[f'B{idx}'] = f'=COUNTIFS(B:B,"{category}",H:H,"Yes (Accurate)")'
    # Count verifiable for this category
    ws[f'C{idx}'] = f'=COUNTIFS(B:B,"{category}",H:H,"<>Cannot Verify")'
    # Accuracy % for this category
    ws[f'D{idx}'] = f'=IFERROR(B{idx}/C{idx}*100,0)'
    ws[f'D{idx}'].number_format = '0.0"%"'
```

### Number Formatting

```python
# Column M: Verification Date
for row in range(3, 201):
    ws[f'M{row}'].number_format = 'DD.MM.YYYY'

# Summary: Accuracy Rate %
ws['B210'].number_format = '0.0"%"'
```

---

## Sheet 3: Completeness Assessment - Complete Specification

### Purpose

Check population rate of mandatory attributes.

### Column Structure

**Total Columns: 15 (A through O)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Asset Category | 20 | List | Dropdown | None | No |
| B | Mandatory Attribute | 30 | Text | None | None | No |
| C | Policy Requirement | 15 | Text | None | None | No |
| D | Total Records | 12 | Number | Integer ≥0 | None | No |
| E | Records with Attribute | 12 | Number | Integer ≥0 | None | No |
| F | Missing Count | 12 | Number | None | Formula | Yes |
| G | Completeness % | 12 | Number | None | Formula | Yes |
| H | Compliance Status | 15 | Text | None | Formula | Yes |
| I | Gap Severity | 15 | List | Dropdown | None | No |
| J | Root Cause | 35 | Text | None | None | No |
| K | Remediation Plan | 40 | Text | None | None | No |
| L | Target Date | 15 | Date | Date validation | None | No |
| M | Responsible Party | 25 | Text | None | None | No |
| N | Evidence Reference | 20 | Text | None | None | No |
| O | Notes | 30 | Text | None | None | No |

### Data Validation

**Column A: Asset Category**

```python
asset_categories = [
    "Information Assets",
    "IT Infrastructure",
    "Applications",
    "Physical Assets",
    "Personnel Assets",
    "All"
]

dv_asset_cat = DataValidation(
    type="list",
    formula1=f'"{",".join(asset_categories)}"',
    allow_blank=False
)
dv_asset_cat.add('A3:A100')
ws.add_data_validation(dv_asset_cat)
```

**Columns D, E: Numeric Validation**

```python
dv_numeric = DataValidation(
    type="whole",
    operator="greaterThanOrEqual",
    formula1='0',
    allow_blank=False,
    showErrorMessage=True,
    errorTitle="Invalid Number",
    error="Enter a positive integer"
)
dv_numeric.add('D3:E100')
ws.add_data_validation(dv_numeric)
```

**Column I: Gap Severity**

```python
severities = [
    "Critical",
    "High",
    "Medium",
    "Low",
    "N/A"
]

dv_severity = DataValidation(
    type="list",
    formula1=f'"{",".join(severities)}"',
    allow_blank=True
)
dv_severity.add('I3:I100')
ws.add_data_validation(dv_severity)
```

**Column L: Target Date**

```python
dv_target_date = DataValidation(
    type="date",
    operator="greaterThanOrEqual",
    formula1=datetime.now().strftime('%Y-%m-%d'),
    allow_blank=True,
    showErrorMessage=True,
    errorTitle="Invalid Date",
    error="Target date should be today or future"
)
dv_target_date.add('L3:L100')
ws.add_data_validation(dv_target_date)
```

### Formulas

**Column F: Missing Count**

```python
for row in range(3, 101):
    ws[f'F{row}'] = f'=D{row}-E{row}'
    ws[f'F{row}'].protection = Protection(locked=True)
```

**Column G: Completeness %**

```python
for row in range(3, 101):
    ws[f'G{row}'] = f'=IFERROR(E{row}/D{row}*100,0)'
    ws[f'G{row}'].number_format = '0.0"%"'
    ws[f'G{row}'].protection = Protection(locked=True)
```

**Column H: Compliance Status**

```python
for row in range(3, 101):
    formula = f'=IF(G{row}=100,"✅ Pass","❌ Fail")'
    ws[f'H{row}'] = formula
    ws[f'H{row}'].alignment = Alignment(horizontal='center')
    ws[f'H{row}'].protection = Protection(locked=True)
```

### Conditional Formatting

**Column G: Completeness % - Traffic Light**

```python
# Green: = 100%
complete_rule = CellIsRule(
    operator='equal',
    formula=['100'],
    fill=PatternFill(start_color='C6EFCE', fill_type='solid'),
    font=Font(color='006100', bold=True)
)
ws.conditional_formatting.add('G3:G100', complete_rule)

# Yellow: 95-99%
near_complete_rule = CellIsRule(
    operator='between',
    formula=['95', '99'],
    fill=PatternFill(start_color='FFEB9C', fill_type='solid'),
    font=Font(color='9C5700', bold=True)
)
ws.conditional_formatting.add('G3:G100', near_complete_rule)

# Red: < 95%
incomplete_rule = CellIsRule(
    operator='lessThan',
    formula=['95'],
    fill=PatternFill(start_color='FFC7CE', fill_type='solid'),
    font=Font(color='9C0006', bold=True)
)
ws.conditional_formatting.add('G3:G100', incomplete_rule)
```

**Column H: Compliance Status - Color Coding**

```python
# Green: Pass
pass_rule = ContainsText(
    text='✅',
    fill=PatternFill(start_color='C6EFCE', fill_type='solid')
)
ws.conditional_formatting.add('H3:H100', pass_rule)

# Red: Fail
fail_rule = ContainsText(
    text='❌',
    fill=PatternFill(start_color='FFC7CE', fill_type='solid')
)
ws.conditional_formatting.add('H3:H100', fail_rule)
```

### Summary Section

**Location**: Rows 105-110

```python
# Overall Completeness
ws['A105'] = "Overall Completeness %"
ws['B105'] = '=IFERROR(AVERAGE(G3:G100),0)'
ws['B105'].number_format = '0.0"%"'
ws['B105'].font = Font(bold=True, size=12)

# Count of Attributes
ws['A106'] = "Total Mandatory Attributes"
ws['B106'] = '=COUNTA(B3:B100)'

ws['A107'] = "Attributes 100% Complete"
ws['B107'] = '=COUNTIF(G3:G100,100)'

ws['A108'] = "Attributes < 100% Complete"
ws['B108'] = '=COUNTIF(G3:G100,"<100")'

# Compliance Rate
ws['A109'] = "Attribute Compliance Rate %"
ws['B109'] = '=B107/B106*100'
ws['B109'].number_format = '0.0"%"'
ws['B109'].font = Font(bold=True, size=12)
```

---

## Sheet 4: Currency Assessment - Complete Specification

### Purpose

Verify data currency (staleness) per policy thresholds.

### Column Structure

**Total Columns: 14 (A through N)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Asset Category | 20 | List | Dropdown | None | No |
| B | Criticality | 15 | List | Dropdown | None | No |
| C | Total Assets | 12 | Number | Integer ≥0 | None | No |
| D | Policy Threshold (days) | 12 | Number | Integer >0 | None | No |
| E | Assets Within Threshold | 12 | Number | Integer ≥0 | None | No |
| F | Assets Exceeding Threshold | 12 | Number | None | Formula | Yes |
| G | Currency Compliance % | 12 | Number | None | Formula | Yes |
| H | Avg Days Since Update | 12 | Number | None | None | No |
| I | Max Days Since Update | 12 | Number | None | None | No |
| J | Compliance Status | 15 | Text | None | Formula | Yes |
| K | Remediation Plan | 40 | Text | None | None | No |
| L | Target Date | 15 | Date | Date validation | None | No |
| M | Responsible Party | 25 | Text | None | None | No |
| N | Notes | 30 | Text | None | None | No |

### Data Validation

**Column A: Asset Category**

```python
asset_categories = [
    "Information Assets",
    "IT Infrastructure",
    "Applications",
    "Physical Assets",
    "Personnel Assets"
]

dv_asset_cat = DataValidation(
    type="list",
    formula1=f'"{",".join(asset_categories)}"',
    allow_blank=False
)
dv_asset_cat.add('A3:A50')
ws.add_data_validation(dv_asset_cat)
```

**Column B: Criticality**

```python
criticalities = [
    "Critical",
    "High",
    "Standard",
    "Low"
]

dv_criticality = DataValidation(
    type="list",
    formula1=f'"{",".join(criticalities)}"',
    allow_blank=False
)
dv_criticality.add('B3:B50')
ws.add_data_validation(dv_criticality)
```

### Formulas

**Column F: Assets Exceeding Threshold**

```python
for row in range(3, 51):
    ws[f'F{row}'] = f'=C{row}-E{row}'
    ws[f'F{row}'].protection = Protection(locked=True)
```

**Column G: Currency Compliance %**

```python
for row in range(3, 51):
    ws[f'G{row}'] = f'=IFERROR(E{row}/C{row}*100,0)'
    ws[f'G{row}'].number_format = '0.0"%"'
    ws[f'G{row}'].protection = Protection(locked=True)
```

**Column J: Compliance Status**

```python
for row in range(3, 51):
    formula = f'=IF(G{row}=100,"✅ Pass",IF(G{row}>=95,"⚠️ At Risk","❌ Fail"))'
    ws[f'J{row}'] = formula
    ws[f'J{row}'].alignment = Alignment(horizontal='center')
    ws[f'J{row}'].protection = Protection(locked=True)
```

### Conditional Formatting

**Column G: Currency Compliance % - Traffic Light**

Same pattern as Completeness (Green 100%, Yellow 95-99%, Red <95%).

**Column J: Compliance Status - Color Coding**

Same pattern as previous sheets (Green ✅, Yellow ⚠️, Red ❌).

### Summary Section

```python
# Overall Currency Compliance
ws['A55'] = "Overall Currency Compliance %"
ws['B55'] = '=IFERROR(AVERAGE(G3:G50),0)'
ws['B55'].number_format = '0.0"%"'
ws['B55'].font = Font(bold=True, size=12)
```

---

## Sheet 5: Consistency Checks - Complete Specification

### Purpose

Document automated consistency checks and contradictions.

### Column Structure

**Total Columns: 14 (A through N)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Check ID | 12 | Text | Pattern CHK-NNN | None | No |
| B | Check Type | 25 | List | Dropdown | None | No |
| C | Check Description | 45 | Text | None | None | No |
| D | Check Logic | 45 | Text | None | None | No |
| E | Total Records Checked | 12 | Number | Integer ≥0 | None | No |
| F | Failures Found | 12 | Number | Integer ≥0 | None | No |
| G | Failure Rate % | 12 | Number | None | Formula | Yes |
| H | Example Failures | 40 | Text | None | None | No |
| I | Impact | 15 | List | Dropdown | None | No |
| J | Root Cause | 35 | Text | None | None | No |
| K | Remediation Plan | 40 | Text | None | None | No |
| L | Responsible Party | 25 | Text | None | None | No |
| M | Evidence Reference | 20 | Text | None | None | No |
| N | Notes | 30 | Text | None | None | No |

### Data Validation

**Column A: Check ID - Pattern Validation**

```python
dv_check_id = DataValidation(
    type="custom",
    formula1='=AND(LEN(A3)=7,LEFT(A3,4)="CHK-",ISNUMBER(VALUE(RIGHT(A3,3))))',
    allow_blank=False,
    showErrorMessage=True,
    errorTitle="Invalid Check ID",
    error="Check ID must be in format CHK-NNN (e.g., CHK-001, CHK-002)"
)
dv_check_id.add('A3:A50')
ws.add_data_validation(dv_check_id)
```

**Column B: Check Type**

```python
check_types = [
    "Status Contradiction",
    "Date Inconsistency",
    "Duplicate",
    "Cross-Reference Error",
    "Logical Impossibility",
    "Other"
]

dv_check_type = DataValidation(
    type="list",
    formula1=f'"{",".join(check_types)}"',
    allow_blank=False
)
dv_check_type.add('B3:B50')
ws.add_data_validation(dv_check_type)
```

**Column I: Impact**

```python
impacts = [
    "Critical",
    "High",
    "Medium",
    "Low"
]

dv_impact = DataValidation(
    type="list",
    formula1=f'"{",".join(impacts)}"',
    allow_blank=False
)
dv_impact.add('I3:I50')
ws.add_data_validation(dv_impact)
```

### Formulas

**Column G: Failure Rate %**

```python
for row in range(3, 51):
    ws[f'G{row}'] = f'=IFERROR(F{row}/E{row}*100,0)'
    ws[f'G{row}'].number_format = '0.00"%"'
    ws[f'G{row}'].protection = Protection(locked=True)
```

### Conditional Formatting

**Column G: Failure Rate % - Reverse Traffic Light (lower is better)**

```python
# Green: 0%
zero_failures = CellIsRule(
    operator='equal',
    formula=['0'],
    fill=PatternFill(start_color='C6EFCE', fill_type='solid'),
    font=Font(color='006100', bold=True)
)
ws.conditional_formatting.add('G3:G50', zero_failures)

# Yellow: 0.01-1%
low_failures = CellIsRule(
    operator='between',
    formula=['0.01', '1'],
    fill=PatternFill(start_color='FFEB9C', fill_type='solid'),
    font=Font(color='9C5700', bold=True)
)
ws.conditional_formatting.add('G3:G50', low_failures)

# Red: > 1%
high_failures = CellIsRule(
    operator='greaterThan',
    formula=['1'],
    fill=PatternFill(start_color='FFC7CE', fill_type='solid'),
    font=Font(color='9C0006', bold=True)
)
ws.conditional_formatting.add('G3:G50', high_failures)
```

### Summary Section

```python
# Consistency Score (inverse of average failure rate)
ws['A55'] = "Overall Consistency Score %"
ws['B55'] = '=100-AVERAGE(G3:G50)'
ws['B55'].number_format = '0.0"%"'
ws['B55'].font = Font(bold=True, size=12)

ws['A56'] = "Total Checks Performed"
ws['B56'] = '=COUNTA(A3:A50)'

ws['A57'] = "Checks with Zero Failures"
ws['B57'] = '=COUNTIF(G3:G50,0)'
```

---

## Sheet 6: Policy Compliance Matrix - Complete Specification

### Purpose

Verify compliance with all SHALL requirements from policy.

### Column Structure

**Total Columns: 14 (A through N)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Requirement ID | 15 | Text | None | None | No |
| B | Requirement Text | 50 | Text | None | None | No |
| C | Compliance Criterion | 40 | Text | None | None | No |
| D | Verification Method | 35 | Text | None | None | No |
| E | Evidence Collected | 40 | Text | None | None | No |
| F | Evidence Reference | 20 | Text | None | None | No |
| G | Compliance Status | 15 | List | Dropdown | None | No |
| H | Compliance % | 12 | Number | 0-100 or N/A | None | No |
| I | Gap Description | 40 | Text | None | None | No |
| J | Gap Severity | 15 | List | Dropdown | None | No |
| K | Remediation Plan | 40 | Text | None | None | No |
| L | Target Date | 15 | Date | Date validation | None | No |
| M | Responsible Party | 25 | Text | None | None | No |
| N | Notes | 30 | Text | None | None | No |

### Pre-Populated Requirements

```python
requirements = [
    ("A.5.9-R1", "[Organization] SHALL maintain an inventory of information and associated assets"),
    ("A.5.9-R2", "[Organization] SHALL categorize assets per defined taxonomy"),
    ("A.5.9-R3", "[Organization] SHALL document mandatory attributes for each inventoried asset"),
    ("A.5.9-R4", "[Organization] SHALL assign ownership to all inventoried assets"),
    ("A.5.9-R5", "[Organization] SHALL review and update the inventory on a defined schedule"),
    ("A.5.9-R6", "[Organization] SHALL integrate asset inventory with other ISMS processes"),
    ("A.5.9-R7", "[Organization] SHALL protect inventory data with appropriate access controls"),
    ("A.5.9-R8", "[Organization] SHALL conduct periodic assessments of inventory quality"),
    ("A.5.9-R9", "[Organization] SHALL report inventory metrics to management")
]

# Populate columns A-B (rows 3-11)
for row_num, (req_id, req_text) in enumerate(requirements, start=3):
    ws[f'A{row_num}'] = req_id
    ws[f'B{row_num}'] = req_text
    ws[f'A{row_num}'].protection = Protection(locked=True)
    ws[f'B{row_num}'].protection = Protection(locked=True)
```

### Data Validation

**Column G: Compliance Status**

```python
compliance_statuses = [
    "✅ Met",
    "⚠️ Partially Met",
    "❌ Not Met"
]

dv_compliance = DataValidation(
    type="list",
    formula1=f'"{",".join(compliance_statuses)}"',
    allow_blank=False
)
dv_compliance.add('G3:G11')
ws.add_data_validation(dv_compliance)
```

**Column H: Compliance %**

```python
dv_compliance_pct = DataValidation(
    type="whole",
    operator="between",
    formula1='0',
    formula2='100',
    allow_blank=True,
    showErrorMessage=True,
    errorTitle="Invalid Percentage",
    error="Enter a value between 0 and 100, or leave blank if not quantifiable"
)
dv_compliance_pct.add('H3:H11')
ws.add_data_validation(dv_compliance_pct)
```

**Column J: Gap Severity**

```python
severities = [
    "Critical",
    "High",
    "Medium",
    "Low",
    "N/A"
]

dv_severity = DataValidation(
    type="list",
    formula1=f'"{",".join(severities)}"',
    allow_blank=True
)
dv_severity.add('J3:J11')
ws.add_data_validation(dv_severity)
```

### Conditional Formatting

**Column G: Compliance Status - Color Coding**

```python
# Green: Met
met_rule = ContainsText(
    text='✅',
    fill=PatternFill(start_color='C6EFCE', fill_type='solid')
)
ws.conditional_formatting.add('G3:G11', met_rule)

# Yellow: Partially Met
partial_rule = ContainsText(
    text='⚠️',
    fill=PatternFill(start_color='FFEB9C', fill_type='solid')
)
ws.conditional_formatting.add('G3:G11', partial_rule)

# Red: Not Met
not_met_rule = ContainsText(
    text='❌',
    fill=PatternFill(start_color='FFC7CE', fill_type='solid')
)
ws.conditional_formatting.add('G3:G11', not_met_rule)
```

### Summary Section

```python
# Overall Policy Compliance
ws['A15'] = "Overall Policy Compliance %"
ws['B15'] = '=COUNTIF(G3:G11,"✅ Met")/COUNTA(G3:G11)*100'
ws['B15'].number_format = '0.0"%"'
ws['B15'].font = Font(bold=True, size=12)

ws['A16'] = "Requirements Met"
ws['B16'] = '=COUNTIF(G3:G11,"✅ Met")'

ws['A17'] = "Requirements Partially Met"
ws['B17'] = '=COUNTIF(G3:G11,"⚠️ Partially Met")'

ws['A18'] = "Requirements Not Met"
ws['B18'] = '=COUNTIF(G3:G11,"❌ Not Met")'
```

---

## Sheet 7: Quality Metrics & Scoring - Complete Specification

### Purpose

Aggregate all quality dimensions into overall quality score.

### Column Structure

**Total Columns: 10 (A through J)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Quality Dimension | 25 | Text | None | Fixed values | Yes |
| B | Weight | 10 | Number | None | Fixed values | Yes |
| C | Target Score | 10 | Number | None | Fixed values | Yes |
| D | Actual Score | 10 | Number | None | Formula | Yes |
| E | Gap vs. Target | 10 | Number | None | Formula | Yes |
| F | Compliance Status | 15 | Text | None | Formula | Yes |
| G | Trend vs. Last Quarter | 20 | List | Dropdown | None | No |
| H | Key Issues | 40 | Text | None | None | No |
| I | Remediation Priority | 40 | Text | None | None | No |
| J | Notes | 30 | Text | None | None | No |

### Pre-Populated Dimensions

```python
dimensions = [
    ("Accuracy", 30, 95),
    ("Completeness", 25, 100),
    ("Currency", 20, 100),
    ("Consistency", 15, 99),
    ("Policy Compliance", 10, 100)
]

# Populate columns A-C (rows 3-7)
for row_num, (dimension, weight, target) in enumerate(dimensions, start=3):
    ws[f'A{row_num}'] = dimension
    ws[f'B{row_num}'] = weight
    ws[f'C{row_num}'] = target
    ws[f'A{row_num}'].protection = Protection(locked=True)
    ws[f'B{row_num}'].protection = Protection(locked=True)
    ws[f'C{row_num}'].protection = Protection(locked=True)

# Format weights as percentages
for row in range(3, 8):
    ws[f'B{row}'].number_format = '0"%"'
    ws[f'C{row}'].number_format = '0"%"'
```

### Formulas

**Column D: Actual Score**

```python
# Row 3: Accuracy (from Sheet 2)
ws['D3'] = "='Accuracy Sampling'!B210"  # Accuracy Rate % from summary
ws['D3'].number_format = '0.0"%"'

# Row 4: Completeness (from Sheet 3)
ws['D4'] = "='Completeness Assessment'!B105"  # Overall Completeness % from summary
ws['D4'].number_format = '0.0"%"'

# Row 5: Currency (from Sheet 4)
ws['D5'] = "='Currency Assessment'!B55"  # Overall Currency Compliance % from summary
ws['D5'].number_format = '0.0"%"'

# Row 6: Consistency (from Sheet 5)
ws['D6'] = "='Consistency Checks'!B55"  # Overall Consistency Score % from summary
ws['D6'].number_format = '0.0"%"'

# Row 7: Policy Compliance (from Sheet 6)
ws['D7'] = "='Policy Compliance Matrix'!B15"  # Overall Policy Compliance % from summary
ws['D7'].number_format = '0.0"%"'

# Lock all formula cells
for row in range(3, 8):
    ws[f'D{row}'].protection = Protection(locked=True)
```

**Column E: Gap vs. Target**

```python
for row in range(3, 8):
    ws[f'E{row}'] = f'=D{row}-C{row}'
    ws[f'E{row}'].number_format = '0.0"%"'
    ws[f'E{row}'].protection = Protection(locked=True)
```

**Column F: Compliance Status**

```python
for row in range(3, 8):
    formula = (
        f'=IF(D{row}>=C{row},"✅ Met",'
        f'IF(D{row}>=C{row}-10,"⚠️ At Risk",'
        f'"❌ Not Met"))'
    )
    ws[f'F{row}'] = formula
    ws[f'F{row}'].alignment = Alignment(horizontal='center')
    ws[f'F{row}'].protection = Protection(locked=True)
```

### Data Validation

**Column G: Trend vs. Last Quarter**

```python
trends = [
    "Improved",
    "Stable",
    "Degraded",
    "N/A (first assessment)"
]

dv_trend = DataValidation(
    type="list",
    formula1=f'"{",".join(trends)}"',
    allow_blank=True
)
dv_trend.add('G3:G7')
ws.add_data_validation(dv_trend)
```

### Overall Quality Score Section

**Location**: Rows 10-15

```python
# Overall Quality Score (weighted average)
ws['A10'] = "Overall Quality Score"
ws['A10'].font = Font(bold=True, size=14, color='003366')

ws['B10'] = '=(D3*B3/100)+(D4*B4/100)+(D5*B5/100)+(D6*B6/100)+(D7*B7/100)'
ws['B10'].number_format = '0.0"%"'
ws['B10'].font = Font(bold=True, size=14)
ws['B10'].fill = PatternFill(start_color='FFEB9C', fill_type='solid')

# Interpretation
ws['A12'] = "Score Interpretation:"
ws['B12'] = '=IF(B10>=90,"Excellent",IF(B10>=80,"Good",IF(B10>=70,"Fair","Poor")))'
ws['B12'].font = Font(bold=True, size=12)

# Target vs. Actual
ws['A13'] = "Target Overall Score"
ws['B13'] = "97%"  # Policy target
ws['B13'].font = Font(bold=True)

ws['A14'] = "Actual Overall Score"
ws['B14'] = '=B10'
ws['B14'].number_format = '0.0"%"'
ws['B14'].font = Font(bold=True)

ws['A15'] = "Gap vs. Target"
ws['B15'] = '=B14-VALUE(LEFT(B13,LEN(B13)-1))'
ws['B15'].number_format = '0.0"%"'
ws['B15'].font = Font(bold=True)
```

### Conditional Formatting

**Column F: Compliance Status - Color Coding**

Same pattern as Sheet 6 (Green ✅, Yellow ⚠️, Red ❌).

**Overall Quality Score (B10) - Color Coding**

```python
# Green: ≥90%
excellent_rule = CellIsRule(
    operator='greaterThanOrEqual',
    formula=['90'],
    fill=PatternFill(start_color='C6EFCE', fill_type='solid'),
    font=Font(color='006100', bold=True, size=14)
)
ws.conditional_formatting.add('B10', excellent_rule)

# Yellow: 80-89%
good_rule = CellIsRule(
    operator='between',
    formula=['80', '89'],
    fill=PatternFill(start_color='FFEB9C', fill_type='solid'),
    font=Font(color='9C5700', bold=True, size=14)
)
ws.conditional_formatting.add('B10', good_rule)

# Red: < 80%
poor_rule = CellIsRule(
    operator='lessThan',
    formula=['80'],
    fill=PatternFill(start_color='FFC7CE', fill_type='solid'),
    font=Font(color='9C0006', bold=True, size=14)
)
ws.conditional_formatting.add('B10', poor_rule)
```

---

## Sheet 8: Evidence Register - Complete Specification

Same structure as IMP-A.5.9-1/2 Evidence Registers with adjusted Related Domain:

**Related Domain** dropdown:

- Accuracy Sampling
- Completeness Assessment
- Currency Assessment
- Consistency Checks
- Policy Compliance
- Quality Metrics
- All Domains

**Evidence ID format**: `QUAL-NNN`

---

## Python Script Template

```python
"""
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR CONTROL A.5.9-3

Quality & Compliance Assessment Workbook Generator
ISO/IEC 27001:2022 Control A.5.9

This script generates the Excel workbook specified in ISMS-IMP-A.5.9.3.

IMPORTANT: This is a SAMPLE script. Customize for your organization:
1. Sample size calculations (adjust for your inventory size)
2. Quality thresholds (policy targets may differ)
3. Weighting of quality dimensions (adjust to your priorities)
4. Formula references (verify sheet names, column positions)

DO NOT use this script without reviewing and adapting all sections marked
with "# CUSTOMIZE:" comments.

Author: ISMS Implementation Team
Date: [Date]
Version: 1.0
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment, Protection
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, ContainsText
from datetime import datetime
import os

# CUSTOMIZE: Configuration
CONFIG = {
    'output_dir': './output/',
    'workbook_name': f'ISMS_A_5_9_Quality_Compliance_Assessment_{datetime.now().strftime("%Y%m%d")}.xlsx',
    'author': '[Organization] ISMS Implementation Team',
    'company': '[Organization]',
    
    # Same color scheme as IMP-A.5.9-1/2
    'colors': {
        'header_bg': '003366',
        'header_text': 'FFFFFF',
        # ... (full color scheme)
    },
    
    'sheets': [
        'Instructions',
        'Accuracy Sampling',
        'Completeness Assessment',
        'Currency Assessment',
        'Consistency Checks',
        'Policy Compliance Matrix',
        'Quality Metrics & Scoring',
        'Evidence Register'
    ]
}

# CUSTOMIZE: Quality dimension weights (must sum to 100%)
QUALITY_WEIGHTS = {
    'Accuracy': 30,
    'Completeness': 25,
    'Currency': 20,
    'Consistency': 15,
    'Policy Compliance': 10
}

# CUSTOMIZE: Target scores
QUALITY_TARGETS = {
    'Accuracy': 95,
    'Completeness': 100,
    'Currency': 100,
    'Consistency': 99,
    'Policy Compliance': 100
}

def create_workbook():
    """Main function to create the assessment workbook"""
    
    print("=" * 60)
    print("ISMS A.5.9 Quality & Compliance Assessment Generator")
    print("=" * 60)
    print()
    
    wb = openpyxl.Workbook()
    
    # Set properties
    wb.properties.title = "ISMS A.5.9 Quality & Compliance Assessment"
    wb.properties.subject = "ISO/IEC 27001:2022 Control A.5.9 - Quality Verification"
    wb.properties.creator = CONFIG['author']
    wb.properties.company = CONFIG['company']
    wb.properties.created = datetime.now()
    
    wb.remove(wb.active)
    
    # Create sheets
    print("Creating sheets...")
    for sheet_name in CONFIG['sheets']:
        wb.create_sheet(title=sheet_name)
        print(f"  ✓ {sheet_name}")
    
    print()
    print("Populating sheets...")
    
    create_instructions_sheet(wb['Instructions'])
    create_accuracy_sampling_sheet(wb['Accuracy Sampling'])
    create_completeness_sheet(wb['Completeness Assessment'])
    create_currency_sheet(wb['Currency Assessment'])
    create_consistency_sheet(wb['Consistency Checks'])
    create_policy_compliance_sheet(wb['Policy Compliance Matrix'])
    create_quality_metrics_sheet(wb['Quality Metrics & Scoring'])
    create_evidence_sheet(wb['Evidence Register'])
    
    # Save
    output_path = os.path.join(CONFIG['output_dir'], CONFIG['workbook_name'])
    os.makedirs(CONFIG['output_dir'], exist_ok=True)
    wb.save(output_path)
    
    print()
    print("=" * 60)
    print(f"✓ Workbook generated successfully!")
    print(f"  Location: {output_path}")
    print(f"  Sheets: {len(CONFIG['sheets'])}")
    print("=" * 60)
    
    return wb

# ... (sheet creation functions per specifications above)

if __name__ == '__main__':
    workbook = create_workbook()
```

---

## Integration with Dashboard

**CSV Export from Sheet 7 (Quality Metrics & Scoring)**:

Required columns for dashboard consolidation:

- Quality Dimension
- Actual Score
- Compliance Status
- Trend

**Export procedure**:
1. Select rows 3-7 in Quality Metrics & Scoring sheet
2. Export to CSV: `A59_3_Quality_Metrics_YYYYMMDD.csv`
3. UTF-8 encoding
4. Include headers

**File format**:
```csv
Quality Dimension,Actual Score,Compliance Status,Trend
Accuracy,96%,✅ Met,Improved
Completeness,94%,⚠️ At Risk,Stable
Currency,92%,⚠️ At Risk,Improved
Consistency,98.5%,✅ Met,Stable
Policy Compliance,89%,⚠️ At Risk,Improved
Overall Quality Score,94.2%,⚠️ At Risk,Improved
```

**Export filename**: `A59_3_Quality_Metrics_YYYYMMDD.csv`

---

**END OF SPECIFICATION**

---

*"When it comes to atoms, language can be used only as in poetry."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
