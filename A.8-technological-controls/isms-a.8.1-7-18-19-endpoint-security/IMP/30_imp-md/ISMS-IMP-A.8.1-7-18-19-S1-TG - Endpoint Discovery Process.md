**ISMS-IMP-A.8.1-7-18-19-S1-TG - Endpoint Discovery Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.1: User Endpoint Devices

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Endpoint Discovery and Inventory Management |
| **Related Policy** | ISMS-POL-A.8.1-7-18-19, Section 2.1.1 (Endpoint Inventory), Section 2.1.2 (Endpoint Classification) |
| **Purpose** | Document comprehensive endpoint discovery process, establish endpoint inventory, and classify endpoints to support all four endpoint security controls |
| **Target Audience** | Endpoint Administrators, Security Engineers, IT Operations, Asset Management, System Administrators, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Monthly (inventory updates), Quarterly (process review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guide for endpoint discovery and inventory | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.1-7-18-19-S1-UG.

---

# Technical Specification

## Instructions for Workbook Developers

This section provides detailed specifications for developers creating the `Endpoint_Inventory.xlsx` workbook (via Python script `generate_a817_1_endpoint_inventory.py` or manual creation).

### Workbook Overview

**Workbook Name:** `Endpoint_Inventory.xlsx`  
**Purpose:** Document comprehensive endpoint discovery and inventory  
**Target Users:** Endpoint Administrators, Security Engineers, IT Operations, Auditors  
**Creation Method:** Python script (`generate_a817_1_endpoint_inventory.py`) or manual Excel creation

### Sheet Structure

The workbook contains 10 worksheets:

1. **Instructions & Legend** - User guidance, status indicators, and thresholds
2. **Inventory** - Complete endpoint inventory with mandatory attributes
3. **Classification** - Endpoint classification by type, ownership, criticality
4. **Discovery_Methods** - Documentation of discovery methods and effectiveness
5. **Quality_Metrics** - Inventory quality metrics over time (coverage, accuracy, currency)
6. **Evidence** - Supporting documentation for inventory accuracy and audit trail
7. **Gaps** - Undiscovered endpoints and remediation plans
8. **Baseline_Compliance** - Baseline compliance status per endpoint (NEW)
9. **Encryption_Status** - Encryption verification and key escrow status (NEW)
10. **Management_Enrollment** - MDM/agent enrollment status (NEW)

---

## Common Column Structure

### Data Types Used Throughout

| Data Type | Description | Example | Validation |
|-----------|-------------|---------|------------|
| **Text** | Free-form text | "John Smith" | Max 255 chars |
| **Text (Constrained)** | Dropdown list | "Corporate-Owned" | Must be from approved list |
| **Date** | Date value | 2026-01-25 | ISO format YYYY-MM-DD |
| **DateTime** | Date and time | 2026-01-25 14:30:00 | ISO format YYYY-MM-DD HH:MM:SS |
| **Integer** | Whole number | 42 | No decimals |
| **Percentage** | Percentage value | 95% | 0-100, formatted as % |
| **Status** | Status indicator | 🟢 Green, 🟡 Yellow, 🔴 Red | Emoji-based visual status |

### Standard Column Patterns

#### Status Columns (Used in Multiple Sheets)

Status columns use emoji-based visual indicators with conditional formatting:

| Status Value | Emoji | Color | Meaning |
|--------------|-------|-------|---------|
| Green | 🟢 | Green fill (#C6EFCE), dark green text (#006100) | Compliant / Good |
| Yellow | 🟡 | Yellow fill (#FFEB9C), dark yellow text (#9C6500) | Partial / Warning |
| Red | 🔴 | Red fill (#FFC7CE), dark red text (#9C0006) | Non-Compliant / Critical |

**Excel Formula Example (Coverage_Status):**
```excel
=IF(Coverage_Rate>=95%,"🟢 Green",IF(Coverage_Rate>=80%,"🟡 Yellow","🔴 Red"))
```

**Conditional Formatting:**

- Green: Apply when cell contains "Green"
- Yellow: Apply when cell contains "Yellow"
- Red: Apply when cell contains "Red"

#### Priority Columns (Used in Gaps Sheet)

Priority columns use visual priority indicators:

| Priority | Emoji | Color | SLA |
|----------|-------|-------|-----|
| Critical | 🔴 | Red fill, white text | 24 hours |
| High | 🟡 | Yellow fill, black text | 7 days |
| Medium | 🟢 | Green fill, black text | 30 days |
| Low | ⚪ | No fill, gray text | 90 days |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Inventory

**Sheet Name:** `Inventory`  
**Purpose:** Complete endpoint inventory with mandatory attributes  
**Row Count:** Variable (one row per endpoint, typically 100-10,000+ rows)

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Device_ID | Text | 20 | Required, Unique | None | Serial number, UUID, asset tag |
| B: Hostname | Text | 25 | Required | None | Computer/device name |
| C: Device_Type | Text (Constrained) | 15 | Dropdown list | None | Laptop, Desktop, Smartphone, Tablet, IoT, VDI Client |
| D: Operating_System | Text | 20 | Required | None | OS and version (e.g., Windows 11 23H2) |
| E: OS_Version | Text | 15 | Optional | None | Detailed version (e.g., 10.0.22631.2861) |
| F: Owner | Text | 20 | Required | None | Assigned user or department |
| G: Ownership_Model | Text (Constrained) | 18 | Dropdown list | None | Corporate-Owned, BYOD, Contractor, Guest, Lab/Test |
| H: Location | Text (Constrained) | 15 | Dropdown list | None | Office, Remote, Mobile, Data Center, Branch Office |
| I: Network_Connection | Text (Constrained) | 18 | Dropdown list | None | Wired, Wireless, VPN, Direct Internet |
| J: IP_Address | Text | 15 | Optional | None | IPv4 or IPv6 address |
| K: MAC_Address | Text | 17 | Optional | None | MAC address format AA:BB:CC:DD:EE:FF |
| L: Criticality | Text (Constrained) | 12 | Dropdown list | None | Critical, High, Medium, Low |
| M: Last_Seen | DateTime | 18 | Required | None | Date/time of last successful connection |
| N: Discovery_Method | Text (Constrained) | 18 | Dropdown list | None | MDM, Network Scan, Manual Entry, AD Query, DHCP Lease |
| O: Discovery_Date | Date | 15 | Required | None | Date device first added to inventory |
| P: Management_Status | Text (Constrained) | 18 | Dropdown list | None | MDM Enrolled, Domain Joined, Unmanaged, Cloud Managed |
| Q: Notes | Text | 40 | Optional | None | Free-form notes |

#### Dropdown List Values

**Device_Type:** Laptop, Desktop, Smartphone, Tablet, IoT Device, VDI Client, Thin Client, Kiosk, Other  
**Ownership_Model:** Corporate-Owned, BYOD, Contractor, Guest, Lab/Test  
**Location:** Office, Remote, Mobile, Data Center, Branch Office, Customer Site, Other  
**Network_Connection:** Wired, Wireless, VPN, Direct Internet, Offline  
**Criticality:** Critical, High, Medium, Low  
**Discovery_Method:** MDM, Network Scan, Manual Entry, AD Query, DHCP Lease, User Survey, Cloud API  
**Management_Status:** MDM Enrolled, Domain Joined, Unmanaged, Cloud Managed, Hybrid

#### Conditional Formatting Rules

1. **Stale Endpoints (Last_Seen > 30 days):**

   - Condition: `=DAYS(TODAY(),M2)>30`
   - Format: Yellow fill (#FFEB9C), orange text (#9C5700)

2. **Very Stale Endpoints (Last_Seen > 90 days):**

   - Condition: `=DAYS(TODAY(),M2)>90`
   - Format: Red fill (#FFC7CE), dark red text (#9C0006)

3. **Critical Endpoints:**

   - Condition: `=L2="Critical"`
   - Format: Light red fill (#FFE6E6)

4. **Unmanaged Endpoints:**

   - Condition: `=P2="Unmanaged"`
   - Format: Light yellow fill (#FFF4CC)

#### Header Row Formatting

- **Font:** Calibri 11pt Bold
- **Fill:** Dark blue (#002060)
- **Text:** White
- **Alignment:** Center
- **Freeze Panes:** Row 2 (header row stays visible when scrolling)
- **AutoFilter:** Enabled on all columns

#### Data Validation

- All dropdown lists: `Data > Data Validation > List`
- Device_ID: Custom validation `=COUNTIF($A:$A,A2)=1` (ensure uniqueness)
- Last_Seen: Must be date ≤ TODAY()
- Discovery_Date: Must be date ≤ TODAY()

---

### Sheet 2: Classification

**Sheet Name:** `Classification`  
**Purpose:** Endpoint classification summary and rules  
**Row Count:** Variable (one row per unique classification combination)

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Device_Type | Text (Constrained) | 15 | Dropdown | None | From Inventory sheet |
| B: Ownership_Model | Text (Constrained) | 18 | Dropdown | None | From Inventory sheet |
| C: Criticality | Text (Constrained) | 12 | Dropdown | None | From Inventory sheet |
| D: Endpoint_Count | Integer | 15 | None | `=COUNTIFS(Inventory!$C:$C,A2,Inventory!$G:$G,B2,Inventory!$L:$L,C2)` | Count from Inventory |
| E: Percentage | Percentage | 12 | None | `=D2/SUM($D:$D)` | Percentage of total |
| F: Security_Baseline | Text | 20 | Optional | None | Applicable baseline (Windows, macOS, Linux, iOS, Android) |
| G: Encryption_Required | Text (Constrained) | 18 | Dropdown | None | Yes - FDE, Yes - Container, No, N/A |
| H: MDM_Required | Text (Constrained) | 15 | Dropdown | None | Yes - Full MDM, Yes - MAM Only, No |
| I: Notes | Text | 40 | Optional | None | Classification rationale |

#### Dropdown List Values

**Encryption_Required:** Yes - FDE (Full Disk Encryption), Yes - Container, No, N/A  
**MDM_Required:** Yes - Full MDM, Yes - MAM Only (Mobile App Management), No

#### Classification Rules (Populate in Sheet)

Example rules to include:

| Device_Type | Ownership_Model | Criticality | Security_Baseline | Encryption_Required | MDM_Required |
|-------------|-----------------|-------------|-------------------|---------------------|--------------|
| Laptop | Corporate-Owned | Critical | Windows/macOS/Linux Baseline | Yes - FDE | Yes - Full MDM |
| Desktop | Corporate-Owned | High | Windows/macOS/Linux Baseline | Yes - FDE | Yes - Full MDM |
| Smartphone | Corporate-Owned | High | iOS/Android Baseline | Yes - FDE | Yes - Full MDM |
| Smartphone | BYOD | Medium | iOS/Android Baseline | Yes - Container | Yes - MAM Only |
| Tablet | Corporate-Owned | Medium | iOS/Android Baseline | Yes - FDE | Yes - Full MDM |

#### Conditional Formatting

1. **High Endpoint Count (≥100):**

   - Condition: `=D2>=100`
   - Format: Light blue fill (#DDEBF7)

2. **Critical Classification:**

   - Condition: `=C2="Critical"`
   - Format: Light red fill (#FFE6E6)

---

### Sheet 3: Discovery_Methods

**Sheet Name:** `Discovery_Methods`  
**Purpose:** Document discovery methods used and effectiveness  
**Row Count:** Variable (one row per discovery method, typically 5-10 rows)

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Method_Name | Text | 20 | Required | None | MDM Export, AD Query, Network Scan, etc. |
| B: Technology | Text | 20 | Optional | None | Intune, Jamf, SCCM, Nmap, Active Directory, etc. |
| C: Coverage_Type | Text (Constrained) | 20 | Dropdown | None | Managed Devices, Domain-Joined, All Networked, DHCP Clients, Self-Reported |
| D: Endpoints_Discovered | Integer | 20 | Required | None | Count of endpoints discovered by this method |
| E: Discovery_Frequency | Text (Constrained) | 18 | Dropdown | None | Daily, Weekly, Monthly, Quarterly, One-Time |
| F: Automation_Status | Text (Constrained) | 18 | Dropdown | None | Fully Automated, Partially Automated, Manual |
| G: Data_Quality | Text (Constrained) | 15 | Dropdown | None | High, Medium, Low |
| H: Limitations | Text | 50 | Optional | None | What this method cannot discover |
| I: Notes | Text | 40 | Optional | None | Additional notes |

#### Dropdown List Values

**Coverage_Type:** Managed Devices, Domain-Joined, All Networked, DHCP Clients, Self-Reported, Cloud VMs, Other  
**Discovery_Frequency:** Real-Time, Daily, Weekly, Monthly, Quarterly, One-Time  
**Automation_Status:** Fully Automated, Partially Automated, Manual  
**Data_Quality:** High, Medium, Low

#### Conditional Formatting

1. **High Discovery Count (≥100):**

   - Condition: `=D2>=100`
   - Format: Light green fill (#E2EFDA)

2. **Manual Methods:**

   - Condition: `=F2="Manual"`
   - Format: Light yellow fill (#FFF4CC)

3. **Low Data Quality:**

   - Condition: `=G2="Low"`
   - Format: Light orange fill (#FDEADA)

---

### Sheet 4: Quality_Metrics

**Sheet Name:** `Quality_Metrics`  
**Purpose:** Track inventory quality metrics over time  
**Row Count:** Variable (one row per assessment period, typically monthly)

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Assessment_Date | Date | 18 | Required | None | Date of quality assessment |
| B: Total_Expected_Endpoints | Integer | 22 | Required | None | Estimated total endpoints |
| C: Total_Discovered_Endpoints | Integer | 25 | Required | `=COUNTA(Inventory!$A:$A)-1` | Count from Inventory (minus header) |
| D: Coverage_Rate | Percentage | 15 | None | `=C2/B2` | Discovered / Expected |
| E: Coverage_Status | Status | 18 | None | `=IF(D2>=0.95,"🟢 Green",IF(D2>=0.8,"🟡 Yellow","🔴 Red"))` | Green ≥95%, Yellow 80-94%, Red <80% |
| F: Spot_Check_Sample_Size | Integer | 22 | Optional | None | Number of endpoints manually verified |
| G: Spot_Check_Accuracy | Percentage | 20 | Optional | None | Percentage of sample verified as accurate |
| H: Accuracy_Status | Status | 18 | None | `=IF(G2>=0.95,"🟢 Green",IF(G2>=0.8,"🟡 Yellow","🔴 Red"))` | Green ≥95%, Yellow 80-94%, Red <80% |
| I: Stale_Endpoints_Count | Integer | 22 | None | `=COUNTIF(Inventory!$M:$M,"<"&TODAY()-30)` | Endpoints not seen >30 days |
| J: Stale_Endpoints_Percentage | Percentage | 25 | None | `=I2/C2` | Stale / Total |
| K: Currency_Status | Status | 18 | None | `=IF(J2<0.05,"🟢 Green",IF(J2<0.1,"🟡 Yellow","🔴 Red"))` | Green <5%, Yellow 5-10%, Red >10% |
| L: Duplicate_Records_Found | Integer | 22 | Optional | None | Count of duplicate records identified |
| M: Duplicate_Records_Merged | Integer | 25 | Optional | None | Count of duplicates resolved |
| N: Remaining_Duplicates | Integer | 20 | None | `=L2-M2` | Unresolved duplicates |
| O: Duplication_Rate | Percentage | 18 | None | `=N2/C2` | Remaining Duplicates / Total |
| P: Duplication_Status | Status | 18 | None | `=IF(O2<0.05,"🟢 Green",IF(O2<0.1,"🟡 Yellow","🔴 Red"))` | Green <5%, Yellow 5-10%, Red >10% |
| Q: Overall_Status | Status | 18 | None | `=IF(COUNTIF(E2:E2,"🔴 Red")+COUNTIF(H2:H2,"🔴 Red")+COUNTIF(K2:K2,"🔴 Red")+COUNTIF(P2:P2,"🔴 Red")>0,"🔴 Red",IF(COUNTIF(E2:E2,"🟡 Yellow")+COUNTIF(H2:H2,"🟡 Yellow")+COUNTIF(K2:K2,"🟡 Yellow")+COUNTIF(P2:P2,"🟡 Yellow")>0,"🟡 Yellow","🟢 Green"))` | Red if any metric red, Yellow if any yellow, else Green |

#### Conditional Formatting (All Status Columns)

Apply conditional formatting to columns E, H, K, P, Q:

1. **Green Status:**

   - Condition: Contains "Green"
   - Format: Green fill (#C6EFCE), dark green text (#006100)

2. **Yellow Status:**

   - Condition: Contains "Yellow"
   - Format: Yellow fill (#FFEB9C), dark yellow text (#9C6500)

3. **Red Status:**

   - Condition: Contains "Red"
   - Format: Red fill (#FFC7CE), dark red text (#9C0006)

#### Chart: Coverage Trend Over Time

Create line chart:

- **X-axis:** Assessment_Date (Column A)
- **Y-axis:** Coverage_Rate (Column D)
- **Title:** "Endpoint Discovery Coverage Trend"
- **Target Line:** Horizontal line at 95% (target coverage)

---

### Sheet 5: Evidence

**Sheet Name:** `Evidence`  
**Purpose:** Document supporting evidence for inventory accuracy  
**Row Count:** Variable (one row per evidence artifact, typically 5-20 rows)

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Evidence_Type | Text (Constrained) | 20 | Dropdown | None | MDM Export, AD Query Log, Network Scan Results, etc. |
| B: Evidence_Date | Date | 15 | Required | None | Date evidence collected |
| C: Evidence_File | Text | 40 | Optional | None | File name/path of evidence artifact |
| D: Evidence_Description | Text | 50 | Optional | None | Brief description of evidence content |
| E: Endpoints_Supported | Integer | 20 | Optional | None | Count of endpoints validated by this evidence |
| F: Evidence_Collector | Text | 20 | Optional | None | Person who collected evidence |
| G: Reviewed_By | Text | 20 | Optional | None | Person who reviewed evidence |
| H: Reviewed_Date | Date | 15 | Optional | None | Date evidence reviewed |
| I: Notes | Text | 40 | Optional | None | Additional notes |

#### Dropdown List Values

**Evidence_Type:** MDM Export, AD Query Log, Network Scan Results, DHCP Lease Report, User Survey Responses, Asset Database Report, Spot-Check Results, Reconciliation Report, Approval Workflow, Other

#### Evidence Naming Convention

Recommend consistent file naming: `Evidence_<Type>_<Date>.ext`

Examples:

- `Evidence_Intune_Export_2026-01-25.csv`
- `Evidence_AD_Query_2026-01-25.log`
- `Evidence_Nmap_Scan_2026-01-25.xml`
- `Evidence_Spot_Check_2026-01-25.xlsx`

---

### Sheet 6: Gaps

**Sheet Name:** `Gaps`  
**Purpose:** Identify undiscovered endpoints and remediation plans  
**Row Count:** Variable (one row per gap, typically 5-20 rows)

#### Column Specifications

| Column | Data Type | Width | Validation | Formula | Notes |
|--------|-----------|-------|------------|---------|-------|
| A: Gap_ID | Text | 10 | Required | None | Unique gap identifier (GAP-001, GAP-002, etc.) |
| B: Gap_Description | Text | 50 | Required | None | Description of gap |
| C: Gap_Type | Text (Constrained) | 20 | Dropdown | None | Discovery Method Gap, Coverage Gap, Classification Gap, Data Quality Gap |
| D: Affected_Endpoints | Integer | 20 | Optional | None | Estimate of how many endpoints affected |
| E: Impact | Text (Constrained) | 12 | Dropdown | None | Critical, High, Medium, Low |
| F: Priority | Status | 12 | None | `=IF(E2="Critical","🔴 Critical",IF(E2="High","🟡 High",IF(E2="Medium","🟢 Medium","⚪ Low")))` | Based on Impact |
| G: Root_Cause | Text | 50 | Optional | None | Why this gap exists |
| H: Remediation_Plan | Text | 60 | Required | None | Specific actions to close gap |
| I: Remediation_Owner | Text | 20 | Optional | None | Person/team responsible |
| J: Target_Date | Date | 15 | Optional | None | Target completion date |
| K: Remediation_Status | Text (Constrained) | 18 | Dropdown | None | Not Started, In Progress, Completed, Deferred |
| L: Status_Color | Status | 15 | None | `=IF(K2="Completed","🟢 Completed",IF(K2="In Progress","🟡 In Progress",IF(K2="Deferred","⚪ Deferred","🔴 Not Started")))` | Visual status indicator |
| M: Notes | Text | 40 | Optional | None | Additional notes |

#### Dropdown List Values

**Gap_Type:** Discovery Method Gap, Coverage Gap, Classification Gap, Data Quality Gap, Process Gap, Technology Gap  
**Impact:** Critical, High, Medium, Low  
**Remediation_Status:** Not Started, In Progress, Completed, Deferred

#### Conditional Formatting

1. **Critical Priority:**

   - Condition: `=E2="Critical"`
   - Format: Red fill (#FFC7CE), dark red text (#9C0006)

2. **High Priority:**

   - Condition: `=E2="High"`
   - Format: Yellow fill (#FFEB9C), dark yellow text (#9C6500)

3. **Overdue Remediation:**

   - Condition: `=AND(J2<TODAY(),K2<>"Completed")`
   - Format: Red fill (#FFC7CE), dark red text (#9C0006)

4. **Completed Remediation:**

   - Condition: `=K2="Completed"`
   - Format: Green fill (#C6EFCE), dark green text (#006100)

---

## Cell Styling Reference

### Standard Cell Formats

#### Text Cells

- **Font:** Calibri 11pt
- **Alignment:** Left (text), Center (dates/statuses), Right (numbers)
- **Wrap Text:** Enabled for description columns (>30 chars)

#### Number Cells

- **Format:** `#,##0` (thousands separator, no decimals)
- **Alignment:** Right

#### Percentage Cells

- **Format:** `0%` or `0.0%` (one decimal for precision)
- **Alignment:** Center

#### Date Cells

- **Format:** `YYYY-MM-DD` (ISO 8601)
- **Alignment:** Center

#### DateTime Cells

- **Format:** `YYYY-MM-DD HH:MM:SS`
- **Alignment:** Center

### Header Row Standard

- **Font:** Calibri 11pt Bold
- **Fill:** Dark blue (#002060)
- **Text Color:** White (#FFFFFF)
- **Alignment:** Center (horizontal), Middle (vertical)
- **Border:** Bottom border (thin, white)
- **Height:** 30 pixels
- **Freeze Panes:** Row 2 (header stays visible)
- **AutoFilter:** Enabled

### Alternating Row Colors

- **Even Rows:** No fill (white)
- **Odd Rows:** Light gray fill (#F2F2F2)

### Cell Borders

- **Header Row:** Bottom border (thin, white)
- **Data Rows:** No borders (alternating row colors provide visual separation)
- **Totals Row:** Top border (medium, black) if applicable

---

## Appendix: Technical Notes for Python Developers

### Script: `generate_a817_1_endpoint_inventory.py`

#### Script Purpose

Generate `Endpoint_Inventory.xlsx` workbook with all 6 worksheets, formulas, data validation, and conditional formatting pre-configured.

#### Required Python Libraries

```python
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils.dataframe import dataframe_to_sheet
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from datetime import datetime
```

#### Workbook Structure

```python
# Create workbook
wb = openpyxl.Workbook()

# Create sheets
ws_inventory = wb.active
ws_inventory.title = "Inventory"
ws_classification = wb.create_sheet("Classification")
ws_discovery = wb.create_sheet("Discovery_Methods")
ws_quality = wb.create_sheet("Quality_Metrics")
ws_evidence = wb.create_sheet("Evidence")
ws_gaps = wb.create_sheet("Gaps")
```

#### Sample Code Snippets

**Apply Header Formatting:**
```python
def format_header(ws, max_col):
    """Apply standard header formatting to worksheet"""
    header_fill = PatternFill(start_color="002060", end_color="002060", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF", size=11)
    header_alignment = Alignment(horizontal="center", vertical="center")
    
    for col in range(1, max_col + 1):
        cell = ws.cell(row=1, column=col)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = header_alignment
    
    ws.freeze_panes = "A2"  # Freeze header row
    ws.auto_filter.ref = ws.dimensions  # Enable autofilter
```

**Add Data Validation (Dropdown):**
```python
def add_dropdown(ws, column, start_row, end_row, options):
    """Add dropdown data validation to specified column range"""
    dv = DataValidation(type="list", formula1=f'"{",".join(options)}"', allow_blank=False)
    ws.add_data_validation(dv)
    dv.add(f'{column}{start_row}:{column}{end_row}')
```

**Add Conditional Formatting (Status Colors):**
```python
def add_status_formatting(ws, column, start_row, end_row):
    """Add conditional formatting for status indicators"""
    # Green status
    green_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    green_font = Font(color="006100")
    ws.conditional_formatting.add(
        f'{column}{start_row}:{column}{end_row}',
        CellIsRule(operator='containsText', formula=['"Green"'], fill=green_fill, font=green_font)
    )
    
    # Yellow status
    yellow_fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
    yellow_font = Font(color="9C6500")
    ws.conditional_formatting.add(
        f'{column}{start_row}:{column}{end_row}',
        CellIsRule(operator='containsText', formula=['"Yellow"'], fill=yellow_fill, font=yellow_font)
    )
    
    # Red status
    red_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
    red_font = Font(color="9C0006")
    ws.conditional_formatting.add(
        f'{column}{start_row}:{column}{end_row}',
        CellIsRule(operator='containsText', formula=['"Red"'], fill=red_fill, font=red_font)
    )
```

**Add Formula:**
```python
def add_formula(ws, cell_ref, formula):
    """Add formula to specified cell"""
    ws[cell_ref] = f'={formula}'
```

#### Dropdown List Values (Define Once, Reuse)

```python
DROPDOWN_VALUES = {
    'Device_Type': ['Laptop', 'Desktop', 'Smartphone', 'Tablet', 'IoT Device', 'VDI Client', 'Thin Client', 'Kiosk', 'Other'],
    'Ownership_Model': ['Corporate-Owned', 'BYOD', 'Contractor', 'Guest', 'Lab/Test'],
    'Location': ['Office', 'Remote', 'Mobile', 'Data Center', 'Branch Office', 'Customer Site', 'Other'],
    'Network_Connection': ['Wired', 'Wireless', 'VPN', 'Direct Internet', 'Offline'],
    'Criticality': ['Critical', 'High', 'Medium', 'Low'],
    'Discovery_Method': ['MDM', 'Network Scan', 'Manual Entry', 'AD Query', 'DHCP Lease', 'User Survey', 'Cloud API'],
    'Management_Status': ['MDM Enrolled', 'Domain Joined', 'Unmanaged', 'Cloud Managed', 'Hybrid'],
    # Add other dropdown lists as needed
}
```

#### Sample Data Generation (For Testing)

```python
def generate_sample_data(ws_inventory, num_rows=100):
    """Generate sample endpoint data for testing"""
    import random
    from datetime import datetime, timedelta
    
    for i in range(2, num_rows + 2):  # Start at row 2 (after header)
        ws_inventory[f'A{i}'] = f'SN-{str(i-1).zfill(6)}'  # Device_ID
        ws_inventory[f'B{i}'] = f'DEVICE-{str(i-1).zfill(4)}'  # Hostname
        ws_inventory[f'C{i}'] = random.choice(DROPDOWN_VALUES['Device_Type'])  # Device_Type
        ws_inventory[f'D{i}'] = 'Windows 11 23H2' if 'Desktop' in ws_inventory[f'C{i}'].value or 'Laptop' in ws_inventory[f'C{i}'].value else 'iOS 17.1'  # Operating_System
        ws_inventory[f'F{i}'] = f'User {i-1}'  # Owner
        ws_inventory[f'G{i}'] = random.choice(DROPDOWN_VALUES['Ownership_Model'])  # Ownership_Model
        ws_inventory[f'H{i}'] = random.choice(DROPDOWN_VALUES['Location'])  # Location
        ws_inventory[f'I{i}'] = random.choice(DROPDOWN_VALUES['Network_Connection'])  # Network_Connection
        ws_inventory[f'L{i}'] = random.choice(DROPDOWN_VALUES['Criticality'])  # Criticality
        ws_inventory[f'M{i}'] = datetime.now() - timedelta(days=random.randint(0, 60))  # Last_Seen
        ws_inventory[f'N{i}'] = random.choice(DROPDOWN_VALUES['Discovery_Method'])  # Discovery_Method
        ws_inventory[f'O{i}'] = datetime.now() - timedelta(days=random.randint(0, 365))  # Discovery_Date
        ws_inventory[f'P{i}'] = random.choice(DROPDOWN_VALUES['Management_Status'])  # Management_Status
```

#### Column Width Auto-Adjustment

```python
def auto_adjust_column_widths(ws):
    """Auto-adjust column widths based on content (up to max_width)"""
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        
        # Set column width (max 50 characters)
        adjusted_width = min(max_length + 2, 50)
        ws.column_dimensions[column_letter].width = adjusted_width
```

#### Save Workbook

```python
# Save workbook
output_path = "/mnt/user-data/outputs/Endpoint_Inventory.xlsx"
wb.save(output_path)
print(f"Workbook saved to: {output_path}")
```

---

**END OF SPECIFICATION**

---

*"Access to the Vedas is the greatest privilege this century may claim over all previous centuries."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-02-06 -->
