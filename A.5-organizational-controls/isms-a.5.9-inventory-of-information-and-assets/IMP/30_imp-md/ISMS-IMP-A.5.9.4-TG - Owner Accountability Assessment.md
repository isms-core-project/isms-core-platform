**ISMS-IMP-A.5.9.4-TG - Owner Accountability Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Asset Ownership Assignment & Accountability Verification |
| **Related Policy** | ISMS-POL-A.5.9, Section 2.4 (Ownership and Accountability), Section 4 (Roles and Responsibilities) |
| **Purpose** | Verify asset ownership is assigned, acknowledged, and understood; validate owner accountability and performance |
| **Target Audience** | Security Team, Asset Owners, Management, HR, Compliance Officers |
| **Assessment Type** | Ownership Verification & Accountability Audit |
| **Review Cycle** | Quarterly or After Significant Ownership Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial assessment specification following consolidated policy structure | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.9.4-UG.

---

# Technical Specification

**Audience:** Workbook developers (Python/Excel script maintainers)

---

## Document Overview

### Purpose of Technical Specification

This section provides complete technical specifications for developers creating or maintaining the Python script that generates the Owner Accountability Assessment workbook.

**Python Script**: `generate_a59_4_owner_accountability.py`

**Generated Workbook**: `ISMS_A_5_9_Owner_Accountability_Assessment_YYYYMMDD.xlsx`

**Key Design Principles**:
1. **Accountability Focus**: Measure not just assignment, but engagement and performance
2. **Tracking Capability**: Support multi-week attestation campaigns
3. **Performance Metrics**: Objective owner performance measurement
4. **Evidence Collection**: Structured attestation and training record tracking
5. **Trending**: Support quarter-over-quarter accountability improvement

---

## Excel Workbook Structure

### Workbook Metadata

**Workbook Properties**:

- **Title**: ISMS A.5.9 Owner Accountability Assessment
- **Subject**: ISO/IEC 27001:2022 Control A.5.9 - Asset Ownership Verification
- **Author**: [Organization] ISMS Implementation Team
- **Company**: [Organization]
- **Created**: [Generation Date]
- **Version**: 1.0

### Sheet Summary

| Sheet # | Sheet Name | Purpose | User Input | Formulas | Protection |
|---------|-----------|---------|------------|----------|-----------|
| 1 | Instructions | User guide | None (read-only) | None | Full |
| 2 | Ownership Coverage | Verify 100% assignment | Yes | Coverage % calcs | Partial |
| 3 | Owner Acknowledgment | Track attestations | Yes | Acknowledgment % | Partial |
| 4 | Owner Awareness | Verify training/understanding | Yes | Awareness % | Partial |
| 5 | Owner Performance | Measure engagement | Yes | Performance scores | Partial |
| 6 | Accountability Metrics | Aggregate scores | Auto-populated | All metrics | Partial |
| 7 | Evidence Register | Evidence tracking | Yes | None | Partial |

---

## Global Styling Standards

Same as IMP-A.5.9-1/2/3 (refer to those documents for detailed color palette and styling).

---

## Sheet 2: Ownership Coverage - Complete Specification

### Purpose

Verify 100% ownership assignment, identify gaps.

### Column Structure

**Total Columns: 13 (A through M)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Asset Category | 20 | List | Dropdown | None | No |
| B | Total Assets | 12 | Number | Integer ≥0 | None | No |
| C | Assets with Owner | 12 | Number | Integer ≥0 | None | No |
| D | Unowned Assets | 12 | Number | None | Formula | Yes |
| E | Assets with Invalid Owner | 12 | Number | Integer ≥0 | None | No |
| F | Valid Ownership % | 12 | Number | None | Formula | Yes |
| G | Compliance Status | 15 | Text | None | Formula | Yes |
| H | Top Unowned Assets | 40 | Text | None | None | No |
| I | Top Invalid Owners | 30 | Text | None | None | No |
| J | Remediation Plan | 40 | Text | None | None | No |
| K | Target Date | 15 | Date | Date validation | None | No |
| L | Responsible Party | 25 | Text | None | None | No |
| M | Notes | 30 | Text | None | None | No |

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
dv_asset_cat.add('A3:A10')
ws.add_data_validation(dv_asset_cat)
```

### Formulas

**Column D: Unowned Assets**

```python
for row in range(3, 11):
    ws[f'D{row}'] = f'=B{row}-C{row}'
    ws[f'D{row}'].protection = Protection(locked=True)
```

**Column F: Valid Ownership %**

```python
for row in range(3, 11):
    ws[f'F{row}'] = f'=IFERROR((C{row}-E{row})/B{row}*100,0)'
    ws[f'F{row}'].number_format = '0.0"%"'
    ws[f'F{row}'].protection = Protection(locked=True)
```

**Column G: Compliance Status**

```python
for row in range(3, 11):
    formula = f'=IF(F{row}=100,"✅ Pass","❌ Fail")'
    ws[f'G{row}'] = formula
    ws[f'G{row}'].alignment = Alignment(horizontal='center')
    ws[f'G{row}'].protection = Protection(locked=True)
```

### Conditional Formatting

**Column F: Valid Ownership % - Traffic Light**

```python
# Green: 100%
complete_rule = CellIsRule(
    operator='equal',
    formula=['100'],
    fill=PatternFill(start_color='C6EFCE', fill_type='solid'),
    font=Font(color='006100', bold=True)
)
ws.conditional_formatting.add('F3:F10', complete_rule)

# Yellow: 95-99%
near_complete_rule = CellIsRule(
    operator='between',
    formula=['95', '99'],
    fill=PatternFill(start_color='FFEB9C', fill_type='solid'),
    font=Font(color='9C5700', bold=True)
)
ws.conditional_formatting.add('F3:F10', near_complete_rule)

# Red: < 95%
incomplete_rule = CellIsRule(
    operator='lessThan',
    formula=['95'],
    fill=PatternFill(start_color='FFC7CE', fill_type='solid'),
    font=Font(color='9C0006', bold=True)
)
ws.conditional_formatting.add('F3:F10', incomplete_rule)
```

### Summary Section

**Location**: Rows 13-16

```python
# Overall Ownership Coverage
ws['A13'] = "Overall Ownership Coverage %"
ws['B13'] = '=IFERROR(AVERAGE(F3:F10),0)'
ws['B13'].number_format = '0.0"%"'
ws['B13'].font = Font(bold=True, size=12)

ws['A14'] = "Total Assets Across All Categories"
ws['B14'] = '=SUM(B3:B10)'

ws['A15'] = "Total Unowned Assets"
ws['B15'] = '=SUM(D3:D10)'

ws['A16'] = "Total Invalid Owners"
ws['B16'] = '=SUM(E3:E10)'
```

---

## Sheet 3: Owner Acknowledgment - Complete Specification

### Purpose

Track attestations and acceptance of ownership.

### Column Structure

**Total Columns: 14 (A through N)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Owner Name | 25 | Text | None | None | No |
| B | Owner Email | 30 | Text | Email validation | None | No |
| C | Owner Department | 20 | Text | None | None | No |
| D | Assets Owned - Count | 12 | Number | Integer ≥0 | None | No |
| E | Asset Categories | 30 | Text | None | None | No |
| F | Attestation Status | 20 | List | Dropdown | None | No |
| G | Attestation Method | 25 | List | Dropdown | None | No |
| H | Attestation Date | 15 | Date | Date validation | None | No |
| I | Days Since Request | 12 | Number | None | Formula | Yes |
| J | Reminder Count | 12 | Number | Integer ≥0 | None | No |
| K | Last Reminder Date | 15 | Date | Date validation | None | No |
| L | Escalation Required | 15 | List | Dropdown | None | No |
| M | Evidence Reference | 20 | Text | None | None | No |
| N | Notes | 30 | Text | None | None | No |

### Data Validation

**Column B: Owner Email - Email Validation**

```python
dv_email = DataValidation(
    type="custom",
    formula1='=AND(LEN(B3)>0,ISNUMBER(FIND("@",B3)))',
    allow_blank=True,
    showErrorMessage=True,
    errorTitle="Invalid Email",
    error="Please enter a valid email address"
)
dv_email.add('B3:B100')
ws.add_data_validation(dv_email)
```

**Column F: Attestation Status**

```python
attestation_statuses = [
    "✅ Signed",
    "📧 Sent, Pending",
    "❌ Not Sent",
    "🔴 Overdue"
]

dv_attestation = DataValidation(
    type="list",
    formula1=f'"{",".join(attestation_statuses)}"',
    allow_blank=False
)
dv_attestation.add('F3:F100')
ws.add_data_validation(dv_attestation)
```

**Column G: Attestation Method**

```python
attestation_methods = [
    "Email Confirmation",
    "E-Signature (DocuSign, etc.)",
    "Physical Signature",
    "Verbal (Meeting)",
    "Not Yet Attested"
]

dv_method = DataValidation(
    type="list",
    formula1=f'"{",".join(attestation_methods)}"',
    allow_blank=True
)
dv_method.add('G3:G100')
ws.add_data_validation(dv_method)
```

**Column L: Escalation Required**

```python
escalation_options = [
    "Yes",
    "No"
]

dv_escalation = DataValidation(
    type="list",
    formula1=f'"{",".join(escalation_options)}"',
    allow_blank=False
)
dv_escalation.add('L3:L100')
ws.add_data_validation(dv_escalation)
```

### Formulas

**Column I: Days Since Request**

```python
# Assuming attestation request sent on assessment start date (in Instructions sheet, or user-defined)
# For simplicity, calculate from today to attestation date (if signed) or today (if pending)

for row in range(3, 101):
    # If attestation signed, days from request to signature
    # If pending, days since request (ongoing)
    # This requires a "Request Date" - add hidden column or use fixed date
    # For sample: Days since today if not signed
    ws[f'I{row}'] = f'=IF(F{row}="✅ Signed",H{row}-$C$1,TODAY()-$C$1)'
    # Where C1 is "Assessment Start Date" in Instructions sheet
    ws[f'I{row}'].protection = Protection(locked=True)
```

**Simpler approach for template**:

```python
for row in range(3, 101):
    # Days since attestation (if signed) or blank
    ws[f'I{row}'] = f'=IF(H{row}<>"",TODAY()-H{row},"")'
    ws[f'I{row}'].protection = Protection(locked=True)
```

### Conditional Formatting

**Column F: Attestation Status - Color Coding**

```python
# Green: Signed
signed_rule = ContainsText(
    text='✅',
    fill=PatternFill(start_color='C6EFCE', fill_type='solid')
)
ws.conditional_formatting.add('F3:F100', signed_rule)

# Yellow: Pending
pending_rule = ContainsText(
    text='📧',
    fill=PatternFill(start_color='FFEB9C', fill_type='solid')
)
ws.conditional_formatting.add('F3:F100', pending_rule)

# Red: Overdue
overdue_rule = ContainsText(
    text='🔴',
    fill=PatternFill(start_color='FFC7CE', fill_type='solid')
)
ws.conditional_formatting.add('F3:F100', overdue_rule)
```

### Summary Section

**Location**: Rows 105-110

```python
# Acknowledgment Metrics
ws['A105'] = "Total Owners"
ws['B105'] = '=COUNTA(A3:A100)'

ws['A106'] = "Owners with Attestation"
ws['B106'] = '=COUNTIF(F3:F100,"✅ Signed")'

ws['A107'] = "Acknowledgment Rate %"
ws['B107'] = '=IFERROR(B106/B105*100,0)'
ws['B107'].number_format = '0.0"%"'
ws['B107'].font = Font(bold=True, size=12)

ws['A108'] = "Pending Attestations"
ws['B108'] = '=COUNTIF(F3:F100,"📧 Sent, Pending")'

ws['A109'] = "Overdue Attestations"
ws['B109'] = '=COUNTIF(F3:F100,"🔴 Overdue")'

ws['A110'] = "Not Yet Sent"
ws['B110'] = '=COUNTIF(F3:F100,"❌ Not Sent")'
```

---

## Sheet 4: Owner Awareness - Complete Specification

### Purpose

Verify owner training and understanding.

### Column Structure

**Total Columns: 14 (A through N)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Owner Name | 25 | Text | None | None | No |
| B | Training Required | 15 | List | Dropdown | None | No |
| C | Training Completed | 15 | List | Dropdown | None | No |
| D | Training Date | 15 | Date | Date validation | None | No |
| E | Training Method | 25 | List | Dropdown | None | No |
| F | Training Score | 12 | Number | 0-100 or N/A | None | No |
| G | Awareness Verification | 25 | List | Dropdown | None | No |
| H | Verification Date | 15 | Date | Date validation | None | No |
| I | Understanding Level | 15 | List | Dropdown | None | No |
| J | Knowledge Gaps | 35 | Text | None | None | No |
| K | Remediation Plan | 40 | Text | None | None | No |
| L | Target Date | 15 | Date | Date validation | None | No |
| M | Evidence Reference | 20 | Text | None | None | No |
| N | Notes | 30 | Text | None | None | No |

### Data Validation

**Column B: Training Required**

```python
training_required = [
    "Yes",
    "No"
]

dv_training_req = DataValidation(
    type="list",
    formula1=f'"{",".join(training_required)}"',
    allow_blank=False
)
dv_training_req.add('B3:B100')
ws.add_data_validation(dv_training_req)
```

**Column C: Training Completed**

```python
training_completed = [
    "✅ Yes",
    "❌ No",
    "🕒 In Progress"
]

dv_training_comp = DataValidation(
    type="list",
    formula1=f'"{",".join(training_completed)}"',
    allow_blank=False
)
dv_training_comp.add('C3:C100')
ws.add_data_validation(dv_training_comp)
```

**Column E: Training Method**

```python
training_methods = [
    "E-Learning (LMS)",
    "Instructor-Led",
    "Self-Study",
    "Not Yet Trained"
]

dv_training_method = DataValidation(
    type="list",
    formula1=f'"{",".join(training_methods)}"',
    allow_blank=True
)
dv_training_method.add('E3:E100')
ws.add_data_validation(dv_training_method)
```

**Column G: Awareness Verification**

```python
verification_methods = [
    "Quiz",
    "Interview",
    "Document Review",
    "Attestation Only",
    "Not Assessed"
]

dv_verification = DataValidation(
    type="list",
    formula1=f'"{",".join(verification_methods)}"',
    allow_blank=False
)
dv_verification.add('G3:G100')
ws.add_data_validation(dv_verification)
```

**Column I: Understanding Level**

```python
understanding_levels = [
    "Excellent",
    "Good",
    "Fair",
    "Poor",
    "Not Assessed"
]

dv_understanding = DataValidation(
    type="list",
    formula1=f'"{",".join(understanding_levels)}"',
    allow_blank=False
)
dv_understanding.add('I3:I100')
ws.add_data_validation(dv_understanding)
```

### Conditional Formatting

**Column C: Training Completed - Color Coding**

```python
# Green: Yes
yes_rule = ContainsText(text='✅', fill=PatternFill(start_color='C6EFCE', fill_type='solid'))
ws.conditional_formatting.add('C3:C100', yes_rule)

# Red: No
no_rule = ContainsText(text='❌', fill=PatternFill(start_color='FFC7CE', fill_type='solid'))
ws.conditional_formatting.add('C3:C100', no_rule)

# Yellow: In Progress
progress_rule = ContainsText(text='🕒', fill=PatternFill(start_color='FFEB9C', fill_type='solid'))
ws.conditional_formatting.add('C3:C100', progress_rule)
```

**Column I: Understanding Level - Color Coding**

```python
# Green: Excellent/Good
excellent_rule = ContainsText(text='Excellent', fill=PatternFill(start_color='C6EFCE', fill_type='solid'))
ws.conditional_formatting.add('I3:I100', excellent_rule)

good_rule = ContainsText(text='Good', fill=PatternFill(start_color='C6EFCE', fill_type='solid'))
ws.conditional_formatting.add('I3:I100', good_rule)

# Yellow: Fair
fair_rule = ContainsText(text='Fair', fill=PatternFill(start_color='FFEB9C', fill_type='solid'))
ws.conditional_formatting.add('I3:I100', fair_rule)

# Red: Poor
poor_rule = ContainsText(text='Poor', fill=PatternFill(start_color='FFC7CE', fill_type='solid'))
ws.conditional_formatting.add('I3:I100', poor_rule)
```

### Summary Section

```python
# Awareness Metrics
ws['A105'] = "Total Owners Requiring Training"
ws['B105'] = '=COUNTIF(B3:B100,"Yes")'

ws['A106'] = "Owners with Training Complete"
ws['B106'] = '=COUNTIFS(B3:B100,"Yes",C3:C100,"✅ Yes")'

ws['A107'] = "Awareness Rate %"
ws['B107'] = '=IFERROR(B106/B105*100,0)'
ws['B107'].number_format = '0.0"%"'
ws['B107'].font = Font(bold=True, size=12)

ws['A108'] = "Owners with Good/Excellent Understanding"
ws['B108'] = '=COUNTIFS(I3:I100,"Excellent")+COUNTIFS(I3:I100,"Good")'
```

---

## Sheet 5: Owner Performance - Complete Specification

### Purpose

Measure owner engagement and performance.

### Column Structure

**Total Columns: 14 (A through N)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Owner Name | 25 | Text | None | None | No |
| B | Assets Owned - Count | 12 | Number | Integer ≥0 | None | No |
| C | Critical/High Assets | 12 | Number | Integer ≥0 | None | No |
| D | Last Review Date - Avg | 15 | Date | Date | None | No |
| E | Days Since Avg Review | 12 | Number | None | Formula | Yes |
| F | Review Compliance % | 12 | Number | 0-100 | None | No |
| G | Update Responsiveness | 20 | List | Dropdown | None | No |
| H | Response Time - Avg (days) | 12 | Number | ≥0 | None | No |
| I | Engagement Score | 12 | Number | None | Formula | Yes |
| J | Performance Rating | 20 | Text | None | Formula | Yes |
| K | Assets at Risk | 12 | Number | Integer ≥0 | None | No |
| L | Action Required | 40 | Text | None | None | No |
| M | Evidence Reference | 20 | Text | None | None | No |
| N | Notes | 30 | Text | None | None | No |

### Data Validation

**Column G: Update Responsiveness**

```python
responsiveness_levels = [
    "Excellent",
    "Good",
    "Fair",
    "Poor"
]

dv_responsiveness = DataValidation(
    type="list",
    formula1=f'"{",".join(responsiveness_levels)}"',
    allow_blank=False
)
dv_responsiveness.add('G3:G100')
ws.add_data_validation(dv_responsiveness)
```

### Formulas

**Column E: Days Since Avg Review**

```python
for row in range(3, 101):
    ws[f'E{row}'] = f'=IF(D{row}<>"",TODAY()-D{row},"")'
    ws[f'E{row}'].protection = Protection(locked=True)
```

**Column I: Engagement Score**

```python
# Engagement = (Review Compliance × 60%) + (Responsiveness Score × 40%)
# Responsiveness Score: Excellent=100%, Good=80%, Fair=60%, Poor=20%

for row in range(3, 101):
    formula = (
        f'=F{row}*0.6+'
        f'IF(G{row}="Excellent",100,IF(G{row}="Good",80,IF(G{row}="Fair",60,20)))*0.4'
    )
    ws[f'I{row}'] = formula
    ws[f'I{row}'].number_format = '0.0"%"'
    ws[f'I{row}'].protection = Protection(locked=True)
```

**Column J: Performance Rating**

```python
for row in range(3, 101):
    formula = (
        f'=IF(I{row}>=90,"⭐ High Performer",'
        f'IF(I{row}>=70,"Meets Expectations",'
        f'IF(I{row}>=50,"⚠️ Needs Improvement",'
        f'"❌ Poor")))'
    )
    ws[f'J{row}'] = formula
    ws[f'J{row}'].alignment = Alignment(horizontal='center')
    ws[f'J{row}'].protection = Protection(locked=True)
```

### Conditional Formatting

**Column I: Engagement Score - Traffic Light**

```python
# Green: ≥ 90%
high_performer = CellIsRule(
    operator='greaterThanOrEqual',
    formula=['90'],
    fill=PatternFill(start_color='C6EFCE', fill_type='solid'),
    font=Font(color='006100', bold=True)
)
ws.conditional_formatting.add('I3:I100', high_performer)

# Yellow: 70-89%
meets_expectations = CellIsRule(
    operator='between',
    formula=['70', '89'],
    fill=PatternFill(start_color='FFEB9C', fill_type='solid'),
    font=Font(color='9C5700', bold=True)
)
ws.conditional_formatting.add('I3:I100', meets_expectations)

# Red: < 70%
poor_performer = CellIsRule(
    operator='lessThan',
    formula=['70'],
    fill=PatternFill(start_color='FFC7CE', fill_type='solid'),
    font=Font(color='9C0006', bold=True)
)
ws.conditional_formatting.add('I3:I100', poor_performer)
```

**Column J: Performance Rating - Color Coding**

Same emoji-based color coding as other sheets.

### Summary Section

```python
# Performance Metrics
ws['A105'] = "Total Owners"
ws['B105'] = '=COUNTA(A3:A100)'

ws['A106'] = "Average Engagement Score"
ws['B106'] = '=AVERAGE(I3:I100)'
ws['B106'].number_format = '0.0"%"'
ws['B106'].font = Font(bold=True, size=12)

ws['A107'] = "High Performers"
ws['B107'] = '=COUNTIF(J3:J100,"*High Performer*")'

ws['A108'] = "Needs Improvement"
ws['B108'] = '=COUNTIF(J3:J100,"*Needs Improvement*")'

ws['A109'] = "Poor Performers"
ws['B109'] = '=COUNTIF(J3:J100,"*Poor*")'
```

---

## Sheet 6: Accountability Metrics - Complete Specification

### Purpose

Aggregate accountability scores across 4 dimensions.

### Column Structure

**Total Columns: 10 (A through J)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Accountability Dimension | 25 | Text | None | Fixed values | Yes |
| B | Weight | 10 | Number | None | Fixed values | Yes |
| C | Target Score | 10 | Number | None | Fixed values | Yes |
| D | Actual Score | 10 | Number | None | Formula | Yes |
| E | Gap vs. Target | 10 | Number | None | Formula | Yes |
| F | Compliance Status | 15 | Text | None | Formula | Yes |
| G | Trend vs. Last Quarter | 20 | List | Dropdown | None | No |
| H | Key Issues | 40 | Text | None | None | No |
| I | Remediation Actions | 40 | Text | None | None | No |
| J | Notes | 30 | Text | None | None | No |

### Pre-Populated Dimensions

```python
dimensions = [
    ("Coverage", 30, 100),
    ("Acknowledgment", 25, 95),
    ("Awareness", 20, 100),
    ("Performance", 25, 80)
]

# Populate columns A-C (rows 3-6)
for row_num, (dimension, weight, target) in enumerate(dimensions, start=3):
    ws[f'A{row_num}'] = dimension
    ws[f'B{row_num}'] = weight
    ws[f'C{row_num}'] = target
    ws[f'A{row_num}'].protection = Protection(locked=True)
    ws[f'B{row_num}'].protection = Protection(locked=True)
    ws[f'C{row_num}'].protection = Protection(locked=True)

# Format
for row in range(3, 7):
    ws[f'B{row}'].number_format = '0"%"'
    ws[f'C{row}'].number_format = '0"%"'
```

### Formulas

**Column D: Actual Score**

```python
# Row 3: Coverage (from Sheet 2)
ws['D3'] = "='Ownership Coverage'!B13"  # Overall Ownership Coverage %
ws['D3'].number_format = '0.0"%"'

# Row 4: Acknowledgment (from Sheet 3)
ws['D4'] = "='Owner Acknowledgment'!B107"  # Acknowledgment Rate %
ws['D4'].number_format = '0.0"%"'

# Row 5: Awareness (from Sheet 4)
ws['D5'] = "='Owner Awareness'!B107"  # Awareness Rate %
ws['D5'].number_format = '0.0"%"'

# Row 6: Performance (from Sheet 5)
ws['D6'] = "='Owner Performance'!B106"  # Average Engagement Score
ws['D6'].number_format = '0.0"%"'

# Lock all
for row in range(3, 7):
    ws[f'D{row}'].protection = Protection(locked=True)
```

**Column E: Gap vs. Target**

```python
for row in range(3, 7):
    ws[f'E{row}'] = f'=D{row}-C{row}'
    ws[f'E{row}'].number_format = '0.0"%"'
    ws[f'E{row}'].protection = Protection(locked=True)
```

**Column F: Compliance Status**

```python
for row in range(3, 7):
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

**Column G: Trend**

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
dv_trend.add('G3:G6')
ws.add_data_validation(dv_trend)
```

### Overall Accountability Score

**Location**: Rows 10-15

```python
# Overall Accountability Score (weighted average)
ws['A10'] = "Overall Accountability Score"
ws['A10'].font = Font(bold=True, size=14, color='003366')

ws['B10'] = '=(D3*B3/100)+(D4*B4/100)+(D5*B5/100)+(D6*B6/100)'
ws['B10'].number_format = '0.0"%"'
ws['B10'].font = Font(bold=True, size=14)
ws['B10'].fill = PatternFill(start_color='FFEB9C', fill_type='solid')

# Interpretation
ws['A12'] = "Score Interpretation:"
ws['B12'] = '=IF(B10>=95,"Excellent",IF(B10>=85,"Good",IF(B10>=75,"Fair","Poor")))'
ws['B12'].font = Font(bold=True, size=12)

# Target vs. Actual
ws['A13'] = "Target Overall Score"
ws['B13'] = "94%"  # Policy target
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

Same pattern as IMP-A.5.9-3 Quality Metrics (Green/Yellow/Red based on compliance status and overall score).

---

## Sheet 7: Evidence Register - Complete Specification

Same structure as previous assessments with adjusted Related Domain:

**Related Domain** dropdown:

- Ownership Coverage
- Owner Acknowledgment
- Owner Awareness
- Owner Performance
- Accountability Metrics
- All Domains

**Evidence ID format**: `ACCT-NNN`

---

## Python Script Template

```python
"""
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR CONTROL A.5.9-4

Owner Accountability Assessment Workbook Generator
ISO/IEC 27001:2022 Control A.5.9

This script generates the Excel workbook specified in ISMS-IMP-A.5.9.4.

IMPORTANT: This is a SAMPLE script. Customize for your organization:
1. Attestation workflow (adjust to your attestation process)
2. Training requirements (which owners require training)
3. Performance thresholds (adjust engagement score calculation)
4. Weighting of dimensions (adjust to your priorities)

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
    'workbook_name': f'ISMS_A_5_9_Owner_Accountability_Assessment_{datetime.now().strftime("%Y%m%d")}.xlsx',
    'author': '[Organization] ISMS Implementation Team',
    'company': '[Organization]',
    
    # Same color scheme as IMP-A.5.9-1/2/3
    'colors': {
        'header_bg': '003366',
        'header_text': 'FFFFFF',
        # ... (full color scheme)
    },
    
    'sheets': [
        'Instructions',
        'Ownership Coverage',
        'Owner Acknowledgment',
        'Owner Awareness',
        'Owner Performance',
        'Accountability Metrics',
        'Evidence Register'
    ]
}

# CUSTOMIZE: Accountability dimension weights (must sum to 100%)
ACCOUNTABILITY_WEIGHTS = {
    'Coverage': 30,
    'Acknowledgment': 25,
    'Awareness': 20,
    'Performance': 25
}

# CUSTOMIZE: Target scores
ACCOUNTABILITY_TARGETS = {
    'Coverage': 100,
    'Acknowledgment': 95,
    'Awareness': 100,
    'Performance': 80
}

def create_workbook():
    """Main function to create the assessment workbook"""
    
    print("=" * 60)
    print("ISMS A.5.9 Owner Accountability Assessment Generator")
    print("=" * 60)
    print()
    
    wb = openpyxl.Workbook()
    
    # Set properties
    wb.properties.title = "ISMS A.5.9 Owner Accountability Assessment"
    wb.properties.subject = "ISO/IEC 27001:2022 Control A.5.9 - Ownership Verification"
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
    create_ownership_coverage_sheet(wb['Ownership Coverage'])
    create_acknowledgment_sheet(wb['Owner Acknowledgment'])
    create_awareness_sheet(wb['Owner Awareness'])
    create_performance_sheet(wb['Owner Performance'])
    create_accountability_metrics_sheet(wb['Accountability Metrics'])
    create_evidence_sheet(wb['Evidence Register'])
    
    # Save
    output_path = os.path.join(CONFIG['output_dir'], CONFIG['workbook_name'])
    os.makedirs(CONFIG['output_dir'], exist_ok=True)
    wb.save(output_path)
    
    print()
    print("=" * 60)
    print(f"✓ Workbook generated successfully!")
    print(f"  Location: {output_path}")
    print("=" * 60)
    
    return wb

# ... (sheet creation functions per specifications above)

if __name__ == '__main__':
    workbook = create_workbook()
```

---

## Integration with Dashboard

**CSV Export from Sheet 6 (Accountability Metrics)**:

Required columns:

- Accountability Dimension
- Actual Score
- Compliance Status
- Trend

**Export procedure**:
1. Select rows 3-6 in Accountability Metrics sheet
2. Export to CSV: `A59_4_Accountability_Metrics_YYYYMMDD.csv`
3. UTF-8 encoding
4. Include headers

**File format**:
```csv
Accountability Dimension,Actual Score,Compliance Status,Trend
Coverage,98%,⚠️ At Risk,Improved
Acknowledgment,89%,⚠️ At Risk,Stable
Awareness,85%,⚠️ At Risk,Improved
Performance,76%,⚠️ At Risk,Stable
Overall Accountability Score,88.1%,⚠️ At Risk,Improved
```

**Export filename**: `A59_4_Accountability_Metrics_YYYYMMDD.csv`

---

**END OF SPECIFICATION**

---

*"We are all agreed that your theory is crazy. The question which divides us is whether it is crazy enough."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
