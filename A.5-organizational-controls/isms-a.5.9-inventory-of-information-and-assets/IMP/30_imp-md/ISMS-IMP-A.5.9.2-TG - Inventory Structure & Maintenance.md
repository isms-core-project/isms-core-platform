**ISMS-IMP-A.5.9.2-TG - Inventory Maintenance**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Inventory Structure & Maintenance Procedures |
| **Related Policy** | ISMS-POL-A.5.9, Section 2.2 (Asset Categorization), Section 2.3 (Mandatory Inventory Attributes), Section 2.5 (Inventory Quality Standards), Section 2.6 (Integration Requirements) |
| **Purpose** | Document inventory structure, update procedures, integration mechanisms, and maintenance workflows |
| **Target Audience** | Security Team, IT Operations, System Owners, Information Owners, CMDB Administrators, Integration Engineers |
| **Assessment Type** | Operational & Technical |
| **Review Cycle** | Quarterly or After Inventory Structure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial assessment specification following consolidated policy structure | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.9.2-UG.

---

# Technical Specification

**Audience:** Workbook developers (Python/Excel script maintainers)

---

## Document Overview

### Purpose of Technical Specification

This section provides complete technical specifications for developers creating or maintaining the Python script that generates the Inventory Maintenance Assessment workbook.

**Python Script**: `generate_a59_2_inventory_maintenance.py`

**Generated Workbook**: `ISMS_A_5_9_Inventory_Maintenance_Assessment_YYYYMMDD.xlsx`

**Key Design Principles**:
1. **User-Friendly**: Clear instructions, data validation, conditional formatting
2. **Automated Calculations**: Minimize manual calculations for metrics
3. **Evidence-Based**: Structured evidence collection and tracking
4. **Audit-Ready**: Professional appearance, clear documentation
5. **Generic**: No hardcoded values specific to one organization

---

## Excel Workbook Structure

### Workbook Metadata

**Workbook Properties**:

- **Title**: ISMS A.5.9 Inventory Maintenance Assessment
- **Subject**: ISO/IEC 27001:2022 Control A.5.9 - Inventory Maintenance
- **Author**: [Organization] ISMS Implementation Team
- **Company**: [Organization]
- **Created**: [Generation Date]
- **Version**: 1.0

**Workbook Protection**: Same as IMP-A.5.9-1

### Sheet Summary

| Sheet # | Sheet Name | Purpose | User Input | Formulas | Protection |
|---------|-----------|---------|------------|----------|-----------|
| 1 | Instructions | User guide and workflow | None (read-only) | None | Full |
| 2 | Inventory Structure | Systems, schemas, organization | Yes | None | Partial |
| 3 | Update Triggers & Workflows | Update procedures and SLAs | Yes | None | Partial |
| 4 | Integration Architecture | System integrations | Yes | None | Partial |
| 5 | Data Quality Controls | Validation and review procedures | Yes | None | Partial |
| 6 | Maintenance Metrics | Aggregated compliance metrics | Partial | All metrics | Partial |
| 7 | Evidence Register | Evidence documentation | Yes | None | Partial |

---

## Global Styling Standards

### Color Palette (Hex Codes)

Same as IMP-A.5.9-1:

```python
COLORS = {
    'header_bg': '003366',        # Dark blue
    'header_text': 'FFFFFF',      # White
    'input_bg': 'FFFFFF',         # White
    'formula_bg': 'F2F2F2',       # Light grey
    'input_border': '4F81BD',     # Blue border
    'formula_border': 'A6A6A6',   # Grey border
    'green_bg': 'C6EFCE',         # Light green
    'green_text': '006100',       # Dark green
    'yellow_bg': 'FFEB9C',        # Light yellow
    'yellow_text': '9C5700',      # Dark orange
    'red_bg': 'FFC7CE',           # Light red
    'red_text': '9C0006',         # Dark red
}
```

### Font, Border, and Alignment Standards

Same as IMP-A.5.9-1 (refer to that document for detailed specifications).

---

## Sheet 1: Instructions - Technical Specification

### Purpose

Provide comprehensive user guide for completing the maintenance assessment.

### Layout Structure

Same pattern as IMP-A.5.9-1 Sheet 1:

- Title and version info (Rows 1-10)
- Assessment overview (Rows 12-25)
- Workflow diagram (Rows 27-45)
- Color coding legend (Rows 47-60)
- Support information (Rows 62-75)

### Implementation Notes

```python
def create_instructions_sheet(ws):
    """Create Instructions sheet with user guide"""
    
    # Title
    ws.merge_cells('A1:P1')
    ws['A1'] = "ISMS A.5.9 Inventory Maintenance Assessment"
    ws['A1'].font = Font(size=18, bold=True, color='003366')
    ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
    ws.row_dimensions[1].height = 40
    
    # Subtitle
    ws.merge_cells('A2:P2')
    ws['A2'] = "ISO/IEC 27001:2022 Control A.5.9 - Inventory Structure & Maintenance"
    ws['A2'].font = Font(size=12, color='666666')
    ws['A2'].alignment = Alignment(horizontal='center', vertical='center')
    
    # Version and date info
    ws['A4'] = "Version:"
    ws['B4'] = "1.0"
    ws['A5'] = "Date Generated:"
    ws['B5'] = datetime.now().strftime('%d.%m.%Y')
    ws['A6'] = "Assessment Period:"
    ws['B6'] = "[Quarter YYYY]"  # User fills
    
    # Assessment overview section
    ws.merge_cells('A8:P8')
    ws['A8'] = "Assessment Overview"
    ws['A8'].font = Font(size=14, bold=True, color='003366')
    
    # ... (continue with full content)
    
    # Protect sheet (full read-only)
    ws.protection.sheet = True
    ws.protection.password = None
```

### Sheet Protection

- All cells: Locked
- Sheet protection: Enabled
- Allow: Select locked cells only

---

## Sheet 2: Inventory Structure - Complete Specification

### Purpose

Document inventory systems, schemas, and organization.

### Column Structure

**Total Columns: 16 (A through P)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Inventory System | 30 | Text | None | None | No |
| B | System Type | 20 | List | Dropdown | None | No |
| C | Asset Categories Stored | 30 | Text | None | None | No |
| D | Primary/Secondary | 20 | List | Dropdown | None | No |
| E | Data Structure | 45 | Text | None | None | No |
| F | Mandatory Attributes Coverage | 50 | Text | None | None | No |
| G | Missing Attributes | 30 | Text | None | None | No |
| H | Access Controls | 30 | Text | None | None | No |
| I | Update Mechanism | 25 | List | Dropdown | None | No |
| J | Version Control | 20 | List | Dropdown | None | No |
| K | Backup Frequency | 15 | List | Dropdown | None | No |
| L | Backup Location | 30 | Text | None | None | No |
| M | Schema Documentation | 20 | List | Dropdown | None | No |
| N | Documentation Location | 35 | Text | None | None | No |
| O | Responsible Party | 25 | Text | None | None | No |
| P | Notes | 30 | Text | None | None | No |

### Header Row Formatting

```python
headers = [
    'Inventory System', 'System Type', 'Asset Categories Stored', 
    'Primary/Secondary', 'Data Structure', 'Mandatory Attributes Coverage',
    'Missing Attributes', 'Access Controls', 'Update Mechanism',
    'Version Control', 'Backup Frequency', 'Backup Location',
    'Schema Documentation', 'Documentation Location', 'Responsible Party', 'Notes'
]

# Apply header styling
for col_num, header in enumerate(headers, start=1):
    cell = ws.cell(row=1, column=col_num, value=header)
    cell.font = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
    cell.fill = PatternFill(start_color='003366', end_color='003366', fill_type='solid')
    cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    cell.border = Border(
        left=Side(style='thin', color='000000'),
        right=Side(style='thin', color='000000'),
        top=Side(style='thin', color='000000'),
        bottom=Side(style='medium', color='000000')
    )

ws.row_dimensions[1].height = 50  # Taller for wrapped text
```

### Data Validation Rules

**Column B: System Type**

```python
system_types = [
    "CMDB",
    "Asset Management System",
    "Database",
    "Spreadsheet",
    "Document Repository",
    "Custom Application",
    "SaaS Platform"
]

dv_system_type = DataValidation(
    type="list",
    formula1=f'"{",".join(system_types)}"',
    allow_blank=False,
    showDropDown=True
)
dv_system_type.add('B3:B20')
ws.add_data_validation(dv_system_type)
```

**Column D: Primary/Secondary**

```python
primary_secondary = [
    "Primary (authoritative)",
    "Secondary (copy/cache)",
    "Reference Only"
]

dv_primary = DataValidation(
    type="list",
    formula1=f'"{",".join(primary_secondary)}"',
    allow_blank=False
)
dv_primary.add('D3:D20')
ws.add_data_validation(dv_primary)
```

**Column I: Update Mechanism**

```python
update_mechanisms = [
    "Manual Entry",
    "API Integration",
    "File Import",
    "Discovery Scan",
    "Multiple Methods"
]

dv_update_mech = DataValidation(
    type="list",
    formula1=f'"{",".join(update_mechanisms)}"',
    allow_blank=False
)
dv_update_mech.add('I3:I20')
ws.add_data_validation(dv_update_mech)
```

**Column J: Version Control**

```python
version_control = [
    "Full Audit Log",
    "Change Tracking",
    "Timestamps Only",
    "None"
]

dv_version = DataValidation(
    type="list",
    formula1=f'"{",".join(version_control)}"',
    allow_blank=False
)
dv_version.add('J3:J20')
ws.add_data_validation(dv_version)
```

**Column K: Backup Frequency**

```python
backup_frequencies = [
    "Real-time",
    "Hourly",
    "Daily",
    "Weekly",
    "Monthly",
    "None"
]

dv_backup = DataValidation(
    type="list",
    formula1=f'"{",".join(backup_frequencies)}"',
    allow_blank=False
)
dv_backup.add('K3:K20')
ws.add_data_validation(dv_backup)
```

**Column M: Schema Documentation**

```python
schema_doc = [
    "Yes - Comprehensive",
    "Yes - Basic",
    "No"
]

dv_schema = DataValidation(
    type="list",
    formula1=f'"{",".join(schema_doc)}"',
    allow_blank=False
)
dv_schema.add('M3:M20')
ws.add_data_validation(dv_schema)
```

### Conditional Formatting

**Column G: Missing Attributes - Alert if Not Empty**

```python
# Yellow fill if cell contains text (indicates missing attributes)
from openpyxl.formatting.rule import CellIsRule

missing_attr_rule = CellIsRule(
    operator='notEqual',
    formula=['""'],
    fill=PatternFill(start_color='FFEB9C', fill_type='solid'),
    font=Font(color='9C5700', bold=True)
)
ws.conditional_formatting.add('G3:G20', missing_attr_rule)
```

**Column K: Backup Frequency - Alert if "None"**

```python
from openpyxl.formatting.rule import ContainsText

no_backup_rule = ContainsText(
    text='None',
    fill=PatternFill(start_color='FFC7CE', fill_type='solid'),
    font=Font(color='9C0006', bold=True)
)
ws.conditional_formatting.add('K3:K20', no_backup_rule)
```

### Cell Styling

**Input Cells** (all columns are input cells in this sheet):

```python
input_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

for row in range(3, 21):  # Rows 3-20
    for col in input_columns:
        cell = ws[f'{col}{row}']
        cell.fill = PatternFill(start_color='FFFFFF', fill_type='solid')
        cell.border = Border(
            left=Side(style='thin', color='4F81BD'),
            right=Side(style='thin', color='4F81BD'),
            top=Side(style='thin', color='4F81BD'),
            bottom=Side(style='thin', color='4F81BD')
        )
        cell.alignment = Alignment(
            horizontal='left', 
            vertical='top', 
            wrap_text=True  # Important for long text fields
        )
        cell.protection = Protection(locked=False)
```

### Sheet Protection

```python
ws.protection.sheet = True
ws.protection.password = None
ws.protection.selectLockedCells = True
ws.protection.selectUnlockedCells = True
ws.protection.formatCells = False
ws.protection.sort = True
ws.protection.autoFilter = True
```

### Row Heights

```python
ws.row_dimensions[1].height = 50  # Header row (wrapped text)
for row in range(3, 21):
    ws.row_dimensions[row].height = 30  # Data rows (accommodate wrapped text)
```

---

## Sheet 3: Update Triggers & Workflows - Complete Specification

### Purpose

Document update triggers, procedures, and SLAs.

### Column Structure

**Total Columns: 15 (A through O)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Update Trigger | 35 | Text | None | None | No |
| B | Trigger Category | 20 | List | Dropdown | None | No |
| C | Asset Categories Affected | 30 | Text | None | None | No |
| D | Trigger Source | 25 | List | Dropdown | None | No |
| E | Update Method | 25 | List | Dropdown | None | No |
| F | Responsible Party | 25 | Text | None | None | No |
| G | Update Workflow | 50 | Text | None | None | No |
| H | SLA - Update Timeframe | 20 | List | Dropdown | None | No |
| I | SLA Achievement % | 12 | Number | 0-100 | None | No |
| J | Verification Method | 35 | Text | None | None | No |
| K | Failure Handling | 35 | Text | None | None | No |
| L | Evidence Location | 30 | Text | None | None | No |
| M | Integration Dependencies | 30 | Text | None | None | No |
| N | Last Review Date | 15 | Date | Date validation | None | No |
| O | Notes | 30 | Text | None | None | No |

### Data Validation Lists

**Column B: Trigger Category**

```python
trigger_categories = [
    "Asset Acquisition",
    "Asset Modification",
    "Asset Disposal",
    "Ownership Change",
    "Location Change",
    "Configuration Change",
    "Status Change",
    "Scheduled Review",
    "Discovery Finding"
]

dv_trigger_cat = DataValidation(
    type="list",
    formula1=f'"{",".join(trigger_categories)}"',
    allow_blank=False
)
dv_trigger_cat.add('B3:B30')
ws.add_data_validation(dv_trigger_cat)
```

**Column D: Trigger Source**

```python
trigger_sources = [
    "Change Management",
    "Service Request",
    "Procurement",
    "HR System",
    "Discovery Scan",
    "Owner Request",
    "Scheduled Process",
    "Manual Detection"
]

dv_trigger_source = DataValidation(
    type="list",
    formula1=f'"{",".join(trigger_sources)}"',
    allow_blank=False
)
dv_trigger_source.add('D3:D30')
ws.add_data_validation(dv_trigger_source)
```

**Column E: Update Method**

```python
update_methods = [
    "Automated (API/Integration)",
    "Semi-Automated (Form/Workflow)",
    "Manual Entry",
    "Discovery Scan Update"
]

dv_update_method = DataValidation(
    type="list",
    formula1=f'"{",".join(update_methods)}"',
    allow_blank=False
)
dv_update_method.add('E3:E30')
ws.add_data_validation(dv_update_method)
```

**Column H: SLA - Update Timeframe**

```python
sla_timeframes = [
    "Real-time",
    "Same Day",
    "Within 1 Day",
    "Within 3 Days",
    "Within 1 Week",
    "Within 1 Month"
]

dv_sla = DataValidation(
    type="list",
    formula1=f'"{",".join(sla_timeframes)}"',
    allow_blank=False
)
dv_sla.add('H3:H30')
ws.add_data_validation(dv_sla)
```

**Column I: SLA Achievement % - Numeric Validation**

```python
dv_sla_percent = DataValidation(
    type="whole",
    operator="between",
    formula1='0',
    formula2='100',
    allow_blank=True,
    showErrorMessage=True,
    errorTitle="Invalid Percentage",
    error="Enter a value between 0 and 100"
)
dv_sla_percent.add('I3:I30')
ws.add_data_validation(dv_sla_percent)
```

**Column N: Last Review Date - Date Validation**

```python
dv_date = DataValidation(
    type="date",
    operator="lessThanOrEqual",
    formula1=datetime.now().strftime('%Y-%m-%d'),
    allow_blank=True,
    showErrorMessage=True,
    errorTitle="Invalid Date",
    error="Date cannot be in the future"
)
dv_date.add('N3:N30')
ws.add_data_validation(dv_date)
```

### Conditional Formatting

**Column I: SLA Achievement % - Traffic Light**

```python
# Green: >= 95%
green_rule = CellIsRule(
    operator='greaterThanOrEqual',
    formula=['95'],
    fill=PatternFill(start_color='C6EFCE', fill_type='solid'),
    font=Font(color='006100', bold=True)
)
ws.conditional_formatting.add('I3:I30', green_rule)

# Yellow: 85-94%
yellow_rule = CellIsRule(
    operator='between',
    formula=['85', '94'],
    fill=PatternFill(start_color='FFEB9C', fill_type='solid'),
    font=Font(color='9C5700', bold=True)
)
ws.conditional_formatting.add('I3:I30', yellow_rule)

# Red: < 85%
red_rule = CellIsRule(
    operator='lessThan',
    formula=['85'],
    fill=PatternFill(start_color='FFC7CE', fill_type='solid'),
    font=Font(color='9C0006', bold=True)
)
ws.conditional_formatting.add('I3:I30', red_rule)
```

### Number Formatting

```python
# Column I: SLA Achievement %
for row in range(3, 31):
    ws[f'I{row}'].number_format = '0"%"'

# Column N: Last Review Date
for row in range(3, 31):
    ws[f'N{row}'].number_format = 'DD.MM.YYYY'
```

---

## Sheet 4: Integration Architecture - Complete Specification

### Purpose

Document system-to-system integrations.

### Column Structure

**Total Columns: 16 (A through P)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Integration Name | 30 | Text | None | None | No |
| B | Source System | 25 | Text | None | None | No |
| C | Target System | 25 | Text | None | None | No |
| D | Data Flow Direction | 25 | List | Dropdown | None | No |
| E | Integration Method | 25 | List | Dropdown | None | No |
| F | Data Elements Transferred | 45 | Text | None | None | No |
| G | Sync Frequency | 15 | List | Dropdown | None | No |
| H | Sync Schedule | 25 | Text | None | None | No |
| I | Last Successful Sync | 20 | DateTime | DateTime validation | None | No |
| J | Sync Success Rate % | 12 | Number | 0-100 | None | No |
| K | Failure Handling | 35 | Text | None | None | No |
| L | Reconciliation Procedure | 40 | Text | None | None | No |
| M | Reconciliation Frequency | 20 | List | Dropdown | None | No |
| N | Health Monitoring | 30 | Text | None | None | No |
| O | Responsible Party | 25 | Text | None | None | No |
| P | Notes | 30 | Text | None | None | No |

### Data Validation Lists

**Column D: Data Flow Direction**

```python
data_flows = [
    "Source → Target (one-way)",
    "Source ↔ Target (bi-directional)",
    "Target → Source (reverse one-way)"
]

dv_flow = DataValidation(
    type="list",
    formula1=f'"{",".join(data_flows)}"',
    allow_blank=False
)
dv_flow.add('D3:D25')
ws.add_data_validation(dv_flow)
```

**Column E: Integration Method**

```python
integration_methods = [
    "REST API",
    "SOAP API",
    "Database Sync",
    "File Transfer (CSV/XML)",
    "Message Queue",
    "Webhook",
    "Manual Export/Import"
]

dv_method = DataValidation(
    type="list",
    formula1=f'"{",".join(integration_methods)}"',
    allow_blank=False
)
dv_method.add('E3:E25')
ws.add_data_validation(dv_method)
```

**Column G: Sync Frequency**

```python
sync_frequencies = [
    "Real-time",
    "Every 15 minutes",
    "Hourly",
    "Daily",
    "Weekly",
    "Monthly",
    "On-Demand"
]

dv_sync_freq = DataValidation(
    type="list",
    formula1=f'"{",".join(sync_frequencies)}"',
    allow_blank=False
)
dv_sync_freq.add('G3:G25')
ws.add_data_validation(dv_sync_freq)
```

**Column J: Sync Success Rate % - Numeric Validation**

```python
dv_success_rate = DataValidation(
    type="whole",
    operator="between",
    formula1='0',
    formula2='100',
    allow_blank=True,
    showErrorMessage=True,
    errorTitle="Invalid Percentage",
    error="Enter a value between 0 and 100"
)
dv_success_rate.add('J3:J25')
ws.add_data_validation(dv_success_rate)
```

**Column M: Reconciliation Frequency**

```python
recon_frequencies = [
    "After Each Sync",
    "Daily",
    "Weekly",
    "Monthly",
    "Quarterly"
]

dv_recon_freq = DataValidation(
    type="list",
    formula1=f'"{",".join(recon_frequencies)}"',
    allow_blank=False
)
dv_recon_freq.add('M3:M25')
ws.add_data_validation(dv_recon_freq)
```

### Conditional Formatting

**Column J: Sync Success Rate % - Traffic Light**

```python
# Green: >= 98%
green_rule = CellIsRule(
    operator='greaterThanOrEqual',
    formula=['98'],
    fill=PatternFill(start_color='C6EFCE', fill_type='solid'),
    font=Font(color='006100', bold=True)
)
ws.conditional_formatting.add('J3:J25', green_rule)

# Yellow: 90-97%
yellow_rule = CellIsRule(
    operator='between',
    formula=['90', '97'],
    fill=PatternFill(start_color='FFEB9C', fill_type='solid'),
    font=Font(color='9C5700', bold=True)
)
ws.conditional_formatting.add('J3:J25', yellow_rule)

# Red: < 90%
red_rule = CellIsRule(
    operator='lessThan',
    formula=['90'],
    fill=PatternFill(start_color='FFC7CE', fill_type='solid'),
    font=Font(color='9C0006', bold=True)
)
ws.conditional_formatting.add('J3:J25', red_rule)
```

### Number Formatting

```python
# Column I: Last Successful Sync (DateTime)
for row in range(3, 26):
    ws[f'I{row}'].number_format = 'DD.MM.YYYY HH:MM'

# Column J: Sync Success Rate %
for row in range(3, 26):
    ws[f'J{row}'].number_format = '0"%"'
```

---

## Sheet 5: Data Quality Controls - Complete Specification

### Purpose

Document data quality validation, reviews, and controls.

### Column Structure

**Total Columns: 12 (A through L)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Quality Control Type | 25 | List | Dropdown | None | No |
| B | Control Description | 45 | Text | None | None | No |
| C | Applies To | 35 | Text | None | None | No |
| D | Implementation | 25 | List | Dropdown | None | No |
| E | Enforcement | 20 | List | Dropdown | None | No |
| F | Error Handling | 35 | Text | None | None | No |
| G | Responsible Party | 25 | Text | None | None | No |
| H | Effectiveness | 20 | List | Dropdown | None | No |
| I | Measurement Method | 35 | Text | None | None | No |
| J | Last Assessed | 15 | Date | Date validation | None | No |
| K | Evidence Location | 30 | Text | None | None | No |
| L | Notes | 30 | Text | None | None | No |

### Data Validation Lists

**Column A: Quality Control Type**

```python
quality_control_types = [
    "Data Validation Rule",
    "Mandatory Field",
    "Format Check",
    "Periodic Review",
    "Automated Check",
    "Owner Attestation",
    "Reconciliation",
    "Duplicate Detection"
]

dv_qc_type = DataValidation(
    type="list",
    formula1=f'"{",".join(quality_control_types)}"',
    allow_blank=False
)
dv_qc_type.add('A3:A30')
ws.add_data_validation(dv_qc_type)
```

**Column D: Implementation**

```python
implementations = [
    "System Validation",
    "Workflow Rule",
    "Scheduled Script",
    "Manual Process",
    "Database Constraint"
]

dv_implementation = DataValidation(
    type="list",
    formula1=f'"{",".join(implementations)}"',
    allow_blank=False
)
dv_implementation.add('D3:D30')
ws.add_data_validation(dv_implementation)
```

**Column E: Enforcement**

```python
enforcements = [
    "On Data Entry",
    "On Save",
    "On Submit",
    "Scheduled (periodic)",
    "On-Demand"
]

dv_enforcement = DataValidation(
    type="list",
    formula1=f'"{",".join(enforcements)}"',
    allow_blank=False
)
dv_enforcement.add('E3:E30')
ws.add_data_validation(dv_enforcement)
```

**Column H: Effectiveness**

```python
effectiveness = [
    "Effective",
    "Partially Effective",
    "Not Effective",
    "Not Yet Measured"
]

dv_effectiveness = DataValidation(
    type="list",
    formula1=f'"{",".join(effectiveness)}"',
    allow_blank=False
)
dv_effectiveness.add('H3:H30')
ws.add_data_validation(dv_effectiveness)
```

### Conditional Formatting

**Column H: Effectiveness - Color Coding**

```python
from openpyxl.formatting.rule import ContainsText

# Green: "Effective"
effective_rule = ContainsText(
    text='Effective',
    fill=PatternFill(start_color='C6EFCE', fill_type='solid'),
    font=Font(color='006100', bold=True)
)
ws.conditional_formatting.add('H3:H30', effective_rule)

# Yellow: "Partially Effective" or "Not Yet Measured"
partial_rule = ContainsText(
    text='Partially',
    fill=PatternFill(start_color='FFEB9C', fill_type='solid'),
    font=Font(color='9C5700', bold=True)
)
ws.conditional_formatting.add('H3:H30', partial_rule)

# Red: "Not Effective"
not_effective_rule = ContainsText(
    text='Not Effective',
    fill=PatternFill(start_color='FFC7CE', fill_type='solid'),
    font=Font(color='9C0006', bold=True)
)
ws.conditional_formatting.add('H3:H30', not_effective_rule)
```

### Number Formatting

```python
# Column J: Last Assessed (Date)
for row in range(3, 31):
    ws[f'J{row}'].number_format = 'DD.MM.YYYY'
```

---

## Sheet 6: Maintenance Metrics - Complete Specification

### Purpose

Auto-aggregate maintenance effectiveness metrics.

### Column Structure

**Total Columns: 11 (A through K)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Metric Category | 25 | Text | None | Fixed values | Yes |
| B | Metric Name | 35 | Text | None | Fixed values | Yes |
| C | Target Value | 15 | Text/Number | None | Fixed/Formula | Yes |
| D | Current Value | 15 | Number | None | Formula | Yes |
| E | Gap vs. Target | 15 | Number | None | Formula | Yes |
| F | Compliance Status | 20 | Text | None | Formula | Yes |
| G | Measurement Period | 20 | Text | None | None | No |
| H | Trend vs. Last Quarter | 20 | List | Dropdown | None | No |
| I | Remediation Actions | 40 | Text | None | None | No |
| J | Responsible Party | 25 | Text | None | None | No |
| K | Notes | 30 | Text | None | None | No |

### Pre-Populated Metrics

```python
metrics = [
    ("Update Timeliness", "Avg SLA Achievement %"),
    ("Update Timeliness", "% Updates Within 1 Day"),
    ("Update Timeliness", "% Updates Within 1 Week"),
    ("Integration Health", "Avg Sync Success Rate %"),
    ("Integration Health", "% Integrations Active"),
    ("Data Quality", "Mandatory Attribute Completeness %"),
    ("Data Quality", "Validation Rule Effectiveness %"),
    ("Data Quality", "Duplicate Detection Rate"),
    ("Review Compliance", "% Owner Attestations Complete"),
    ("Review Compliance", "Avg Review Timeliness"),
    ("System Health", "% Systems with Backup"),
    ("System Health", "% Systems with Version Control")
]

# Populate columns A-B (rows 3-14)
row_num = 3
for category, metric_name in metrics:
    ws[f'A{row_num}'] = category
    ws[f'B{row_num}'] = metric_name
    ws[f'A{row_num}'].protection = Protection(locked=True)
    ws[f'B{row_num}'].protection = Protection(locked=True)
    row_num += 1
```

### Formulas

**Column C: Target Value (mostly fixed, some calculated)**

```python
targets = {
    3: '95%',   # Avg SLA Achievement
    4: '95%',   # Within 1 Day
    5: '98%',   # Within 1 Week
    6: '98%',   # Avg Sync Success
    7: '100%',  # Integrations Active
    8: '100%',  # Mandatory Attributes
    9: '95%',   # Validation Effectiveness
    10: '<1%',  # Duplicate Rate (lower is better)
    11: '95%',  # Attestations Complete
    12: '100%', # Review Timeliness
    13: '100%', # Systems with Backup
    14: '100%'  # Systems with Version Control
}

for row, target in targets.items():
    ws[f'C{row}'] = target
    ws[f'C{row}'].protection = Protection(locked=True)
```

**Column D: Current Value (Formulas from other sheets)**

```python
# Row 3: Avg SLA Achievement %
ws['D3'] = '=IFERROR(AVERAGE(\'Update Triggers & Workflows\'!I:I),0)'
ws['D3'].number_format = '0"%"'

# Row 4: % Updates Within 1 Day
ws['D4'] = '=IFERROR(COUNTIFS(\'Update Triggers & Workflows\'!H:H,"Within 1 Day",\'Update Triggers & Workflows\'!I:I,">=95")/COUNTA(\'Update Triggers & Workflows\'!H3:H30)*100,0)'
ws['D4'].number_format = '0"%"'

# Row 5: % Updates Within 1 Week
ws['D5'] = '=IFERROR(COUNTIFS(\'Update Triggers & Workflows\'!H:H,"Within 1 Week",\'Update Triggers & Workflows\'!I:I,">=95")/COUNTA(\'Update Triggers & Workflows\'!H3:H30)*100,0)'
ws['D5'].number_format = '0"%"'

# Row 6: Avg Sync Success Rate %
ws['D6'] = '=IFERROR(AVERAGE(\'Integration Architecture\'!J:J),0)'
ws['D6'].number_format = '0"%"'

# Row 7: % Integrations Active
ws['D7'] = '=IFERROR(COUNTIF(\'Integration Architecture\'!E:E,"*API*")/COUNTA(\'Integration Architecture\'!E3:E25)*100,0)'
ws['D7'].number_format = '0"%"'

# Row 8: Mandatory Attribute Completeness %
# Calculate as: systems with no missing attributes / total systems
ws['D8'] = '=IFERROR((COUNTA(\'Inventory Structure\'!A3:A20)-COUNTIF(\'Inventory Structure\'!G:G,">0"))/COUNTA(\'Inventory Structure\'!A3:A20)*100,0)'
ws['D8'].number_format = '0"%"'

# Row 9: Validation Rule Effectiveness %
ws['D9'] = '=IFERROR(COUNTIF(\'Data Quality Controls\'!H:H,"Effective")/COUNTA(\'Data Quality Controls\'!H3:H30)*100,0)'
ws['D9'].number_format = '0"%"'

# Row 10: Duplicate Detection Rate (placeholder, needs manual input)
ws['D10'] = 0
ws['D10'].number_format = '0.0"%"'
ws['D10'].protection = Protection(locked=False)  # User enters this

# Row 11: % Owner Attestations Complete (placeholder, manual)
ws['D11'] = 0
ws['D11'].number_format = '0"%"'
ws['D11'].protection = Protection(locked=False)

# Row 12: Avg Review Timeliness (placeholder, manual)
ws['D12'] = 0
ws['D12'].number_format = '0"%"'
ws['D12'].protection = Protection(locked=False)

# Row 13: % Systems with Backup
ws['D13'] = '=IFERROR((COUNTA(\'Inventory Structure\'!K3:K20)-COUNTIF(\'Inventory Structure\'!K:K,"None"))/COUNTA(\'Inventory Structure\'!K3:K20)*100,0)'
ws['D13'].number_format = '0"%"'

# Row 14: % Systems with Version Control
ws['D14'] = '=IFERROR((COUNTA(\'Inventory Structure\'!J3:J20)-COUNTIF(\'Inventory Structure\'!J:J,"None"))/COUNTA(\'Inventory Structure\'!J3:J20)*100,0)'
ws['D14'].number_format = '0"%"'

# Lock all formula cells
for row in [3, 4, 5, 6, 7, 8, 9, 13, 14]:
    ws[f'D{row}'].protection = Protection(locked=True)
```

**Column E: Gap vs. Target**

```python
for row in range(3, 15):
    # Extract numeric value from target (remove %)
    formula = f'=D{row}-VALUE(LEFT(C{row},FIND("%",C{row})-1))'
    ws[f'E{row}'] = formula
    ws[f'E{row}'].number_format = '0.0"%"'
    ws[f'E{row}'].protection = Protection(locked=True)
```

**Column F: Compliance Status**

```python
for row in range(3, 15):
    formula = (
        f'=IF(D{row}>=VALUE(LEFT(C{row},FIND("%",C{row})-1)),"✅ Compliant",'
        f'IF(D{row}>=VALUE(LEFT(C{row},FIND("%",C{row})-1))-10,"⚠️ At Risk",'
        f'"❌ Non-Compliant"))'
    )
    ws[f'F{row}'] = formula
    ws[f'F{row}'].alignment = Alignment(horizontal='center', vertical='center')
    ws[f'F{row}'].protection = Protection(locked=True)
```

### Data Validation

**Column H: Trend vs. Last Quarter**

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
dv_trend.add('H3:H14')
ws.add_data_validation(dv_trend)
```

### Conditional Formatting

**Column F: Compliance Status - Color Coding**

```python
# Green: Contains "✅"
compliant_rule = ContainsText(
    text='✅',
    fill=PatternFill(start_color='C6EFCE', fill_type='solid')
)
ws.conditional_formatting.add('F3:F14', compliant_rule)

# Yellow: Contains "⚠️"
risk_rule = ContainsText(
    text='⚠️',
    fill=PatternFill(start_color='FFEB9C', fill_type='solid')
)
ws.conditional_formatting.add('F3:F14', risk_rule)

# Red: Contains "❌"
noncompliant_rule = ContainsText(
    text='❌',
    fill=PatternFill(start_color='FFC7CE', fill_type='solid')
)
ws.conditional_formatting.add('F3:F14', noncompliant_rule)
```

---

## Sheet 7: Evidence Register - Complete Specification

### Purpose

Document all evidence related to inventory maintenance.

### Column Structure

Same as IMP-A.5.9-1 Evidence Register with adjusted Related Domain dropdown:

**Total Columns: 14 (A through N)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Evidence ID | 15 | Text | Pattern MAINT-NNN | None | No |
| B | Evidence Type | 20 | List | Dropdown | None | No |
| C | Related Domain | 20 | List | Dropdown | None | No |
| D | Evidence Description | 40 | Text | None | None | No |
| E | Collection Date | 15 | Date | Date validation | None | No |
| F | Collected By | 20 | Text | None | None | No |
| G | File Name | 30 | Text | None | None | No |
| H | Storage Location | 35 | Text | None | None | No |
| I | Evidence Format | 15 | List | Dropdown | None | No |
| J | Retention Period | 15 | List | Dropdown | None | No |
| K | Access Restriction | 15 | List | Dropdown | None | No |
| L | Evidence Quality | 15 | List | Dropdown | None | No |
| M | Related Sheet | 20 | Text | None | None | No |
| N | Notes | 30 | Text | None | None | No |

### Data Validation Lists

**Column A: Evidence ID - Pattern Validation**

```python
dv_evidence_id = DataValidation(
    type="custom",
    formula1='=AND(LEN(A3)=8,LEFT(A3,6)="MAINT-",ISNUMBER(VALUE(RIGHT(A3,2))))',
    allow_blank=False,
    showErrorMessage=True,
    errorTitle="Invalid Evidence ID",
    error="Evidence ID must be in format MAINT-NN (e.g., MAINT-01, MAINT-02)"
)
dv_evidence_id.add('A3:A200')
ws.add_data_validation(dv_evidence_id)

dv_evidence_id.promptTitle = "Evidence ID Format"
dv_evidence_id.prompt = "Enter ID in format MAINT-01, MAINT-02, etc."
dv_evidence_id.showInputMessage = True
```

**Column B: Evidence Type**

```python
evidence_types = [
    "Procedure Document",
    "System Configuration",
    "Review Record",
    "Metrics Report",
    "Integration Config",
    "Workflow Diagram",
    "Meeting Minutes",
    "Screenshot",
    "Other"
]

dv_evidence_type = DataValidation(
    type="list",
    formula1=f'"{",".join(evidence_types)}"',
    allow_blank=False
)
dv_evidence_type.add('B3:B200')
ws.add_data_validation(dv_evidence_type)
```

**Column C: Related Domain**

```python
related_domains = [
    "Inventory Structure",
    "Update Procedures",
    "Integration",
    "Data Quality",
    "All Domains"
]

dv_related_domain = DataValidation(
    type="list",
    formula1=f'"{",".join(related_domains)}"',
    allow_blank=False
)
dv_related_domain.add('C3:C200')
ws.add_data_validation(dv_related_domain)
```

**Column E: Collection Date**

```python
dv_collection_date = DataValidation(
    type="date",
    operator="lessThanOrEqual",
    formula1=datetime.now().strftime('%Y-%m-%d'),
    allow_blank=False,
    showErrorMessage=True,
    errorTitle="Invalid Date",
    error="Collection date cannot be in the future"
)
dv_collection_date.add('E3:E200')
ws.add_data_validation(dv_collection_date)
```

**Column I: Evidence Format**

```python
evidence_formats = [
    "PDF",
    "Excel",
    "CSV",
    "JSON",
    "XML",
    "Screenshot",
    "Config File",
    "Text",
    "Other"
]

dv_evidence_format = DataValidation(
    type="list",
    formula1=f'"{",".join(evidence_formats)}"',
    allow_blank=False
)
dv_evidence_format.add('I3:I200')
ws.add_data_validation(dv_evidence_format)
```

**Columns J, K, L**: Same as IMP-A.5.9-1 (Retention Period, Access Restriction, Evidence Quality)

### Conditional Formatting

Same as IMP-A.5.9-1 Evidence Register:

- Access Restriction: Red for "Restricted", Orange for "Confidential"
- Evidence Quality: Green for "Complete", Yellow for "Partial", Red for "Insufficient"

---

## Python Script Template

```python
"""
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR CONTROL A.5.9-2

Inventory Maintenance Assessment Workbook Generator
ISO/IEC 27001:2022 Control A.5.9

This script generates the Excel workbook specified in ISMS-IMP-A.5.9.2.

IMPORTANT: This is a SAMPLE script. Customize for your organization:
1. Validation lists (adjust categories, methods per your context)
2. Formula references (verify sheet names, column positions)
3. Metric calculations (adjust based on your needs)
4. File paths and naming conventions

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
    'workbook_name': f'ISMS_A_5_9_Inventory_Maintenance_Assessment_{datetime.now().strftime("%Y%m%d")}.xlsx',
    'author': '[Organization] ISMS Implementation Team',
    'company': '[Organization]',
    
    # Color scheme (same as IMP-A.5.9-1)
    'colors': {
        'header_bg': '003366',
        'header_text': 'FFFFFF',
        'input_bg': 'FFFFFF',
        'formula_bg': 'F2F2F2',
        'input_border': '4F81BD',
        'formula_border': 'A6A6A6',
        'green_bg': 'C6EFCE',
        'green_text': '006100',
        'yellow_bg': 'FFEB9C',
        'yellow_text': '9C5700',
        'red_bg': 'FFC7CE',
        'red_text': '9C0006',
    },
    
    'sheets': [
        'Instructions',
        'Inventory Structure',
        'Update Triggers & Workflows',
        'Integration Architecture',
        'Data Quality Controls',
        'Maintenance Metrics',
        'Evidence Register'
    ]
}

# CUSTOMIZE: Validation lists
VALIDATION_LISTS = {
    # Sheet 2: Inventory Structure
    'system_types': [
        "CMDB", "Asset Management System", "Database", "Spreadsheet",
        "Document Repository", "Custom Application", "SaaS Platform"
    ],
    
    # Sheet 3: Update Triggers & Workflows
    'trigger_categories': [
        "Asset Acquisition", "Asset Modification", "Asset Disposal",
        "Ownership Change", "Location Change", "Configuration Change",
        "Status Change", "Scheduled Review", "Discovery Finding"
    ],
    
    # Sheet 4: Integration Architecture
    'integration_methods': [
        "REST API", "SOAP API", "Database Sync", "File Transfer (CSV/XML)",
        "Message Queue", "Webhook", "Manual Export/Import"
    ],
    
    # Sheet 5: Data Quality Controls
    'quality_control_types': [
        "Data Validation Rule", "Mandatory Field", "Format Check",
        "Periodic Review", "Automated Check", "Owner Attestation",
        "Reconciliation", "Duplicate Detection"
    ],
    
    # Sheet 7: Evidence Register
    'evidence_types': [
        "Procedure Document", "System Configuration", "Review Record",
        "Metrics Report", "Integration Config", "Workflow Diagram",
        "Meeting Minutes", "Screenshot", "Other"
    ],
    
    'related_domains': [
        "Inventory Structure", "Update Procedures", "Integration",
        "Data Quality", "All Domains"
    ]
}

def create_workbook():
    """Main function to create the assessment workbook"""
    
    print("=" * 60)
    print("ISMS A.5.9 Inventory Maintenance Assessment Generator")
    print("=" * 60)
    print()
    
    wb = openpyxl.Workbook()
    
    # Set properties
    wb.properties.title = "ISMS A.5.9 Inventory Maintenance Assessment"
    wb.properties.subject = "ISO/IEC 27001:2022 Control A.5.9 - Inventory Maintenance"
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
    create_inventory_structure_sheet(wb['Inventory Structure'])
    create_update_triggers_sheet(wb['Update Triggers & Workflows'])
    create_integration_sheet(wb['Integration Architecture'])
    create_quality_controls_sheet(wb['Data Quality Controls'])
    create_metrics_sheet(wb['Maintenance Metrics'])
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
    print(f"  Size: {os.path.getsize(output_path) / 1024:.1f} KB")
    print("=" * 60)
    
    return wb

def create_instructions_sheet(ws):
    """Create Instructions sheet"""
    print("  ✓ Instructions")
    # Implementation similar to IMP-A.5.9-1
    ws.protection.sheet = True

def create_inventory_structure_sheet(ws):
    """Create Inventory Structure sheet"""
    print("  ✓ Inventory Structure")
    
    headers = [
        'Inventory System', 'System Type', 'Asset Categories Stored',
        'Primary/Secondary', 'Data Structure', 'Mandatory Attributes Coverage',
        'Missing Attributes', 'Access Controls', 'Update Mechanism',
        'Version Control', 'Backup Frequency', 'Backup Location',
        'Schema Documentation', 'Documentation Location', 'Responsible Party', 'Notes'
    ]
    
    # Apply headers (styling same as IMP-A.5.9-1)
    # ... (implementation per specifications above)
    
    # Data validation
    # ... (implementation per specifications above)
    
    ws.protection.sheet = True
    ws.freeze_panes = 'A2'

def create_update_triggers_sheet(ws):
    """Create Update Triggers & Workflows sheet"""
    print("  ✓ Update Triggers & Workflows")
    # ... (implementation per specifications above)

def create_integration_sheet(ws):
    """Create Integration Architecture sheet"""
    print("  ✓ Integration Architecture")
    # ... (implementation per specifications above)

def create_quality_controls_sheet(ws):
    """Create Data Quality Controls sheet"""
    print("  ✓ Data Quality Controls")
    # ... (implementation per specifications above)

def create_metrics_sheet(ws):
    """Create Maintenance Metrics sheet"""
    print("  ✓ Maintenance Metrics")
    
    # Pre-populate metrics
    metrics = [
        ("Update Timeliness", "Avg SLA Achievement %"),
        ("Update Timeliness", "% Updates Within 1 Day"),
        # ... (all metrics per specifications)
    ]
    
    # ... (implementation per specifications above)

def create_evidence_sheet(ws):
    """Create Evidence Register sheet"""
    print("  ✓ Evidence Register")
    # ... (implementation per specifications above, similar to IMP-A.5.9-1)

if __name__ == '__main__':
    workbook = create_workbook()
    print("✓ Script execution complete")
```

---

## Integration with Dashboard

**CSV Export from Sheet 6 (Maintenance Metrics)**:

Required columns for dashboard consolidation:

- Metric Category
- Metric Name
- Current Value
- Compliance Status
- Trend

**Export procedure**:
1. Select rows 3-14 in Maintenance Metrics sheet
2. Export to CSV: `A59_2_Maintenance_Metrics_YYYYMMDD.csv`
3. UTF-8 encoding
4. Include headers

**File format**:
```csv
Metric Category,Metric Name,Current,Compliance Status,Trend
Update Timeliness,Avg SLA Achievement %,89%,⚠️ At Risk,Stable
Update Timeliness,% Updates Within 1 Day,94%,⚠️ At Risk,Improved
Integration Health,Avg Sync Success Rate %,96%,⚠️ At Risk,Improved
Data Quality,Mandatory Attribute Completeness %,94%,⚠️ At Risk,Improved
...
```

**Export filename**: `A59_2_Maintenance_Metrics_YYYYMMDD.csv`

---

**END OF SPECIFICATION**

---

*"Truth and clarity are complementary."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
