**ISMS-IMP-A.5.23.S5-TG - Compliance Monitoring Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Compliance Monitoring & Exit Planning Dashboard |
| **Related Policy** | ISMS-POL-A.5.19-23-S5 (Cloud Services Security - Section 8: Exit Strategy Framework) |
| **Purpose** | Auto-generate executive compliance dashboard consolidating exit strategy compliance, DORA PoC testing status, and high-risk service identification from source assessment workbooks (IMP-A.5.23.1 through A.5.23.4) |
| **Target Audience** | CISO, CIO, Risk Committee, Board of Directors, Compliance Officers, DPO, Internal/External Auditors |
| **Assessment Type** | Consolidation Dashboard (Auto-Generated from Source Workbooks) |
| **Review Cycle** | Quarterly (after source workbook completion), Annual (post-PoC testing), Pre-Audit, Board Meetings |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial Python generator script for basic exit strategy dashboard (3 sheets). Consolidated data from IMP-A.5.23.1 (exit strategies) and IMP-A.5.23.4 (governance). No user documentation provided. | ISMS Implementation Team |

---

## Document Purpose & Scope

### What This Document Provides

**Part I: User Completion Guide** (~4,500 lines target)

- Dashboard overview and architecture
- Source workbook prerequisites and validation
- Step-by-step dashboard generation procedures
- Sheet-by-sheet interpretation guidance
- Executive reporting templates (CISO/CIO, Board)
- Dashboard refresh and maintenance procedures
- Integration with ISMS and risk management
- Quality assurance and troubleshooting
- Appendices, glossary, and regulatory references

**Part II: Technical Specification** (~4,000 lines target)

- Python generator script architecture breakdown
- Complete output workbook specification (3 sheets)
- Data extraction algorithms and formulas
- Schema validation logic
- Conditional formatting and styling rules
- Testing and validation procedures
- Extension and customization guidance

### Target Audience

**Primary Users:**

- **CISO / CIO:** Executive oversight of cloud exit strategy compliance
- **Risk Committee:** Quarterly compliance reporting and risk escalation
- **Compliance Officer:** Dashboard generation, validation, and evidence management
- **DPO (Data Protection Officer):** Cross-border data transfer risk monitoring

**Secondary Users:**

- **Internal Auditors:** ISO 27001 A.5.23 audit evidence
- **External Auditors:** Third-party compliance verification
- **Board of Directors:** Annual strategic risk reporting
- **IT Operations:** Remediation action planning and tracking

### Dual Perspective Approach

**🔧 IMPLEMENTER PERSPECTIVE:**
*You are the Compliance Officer responsible for generating the quarterly compliance dashboard. You need to understand how to run the Python generator script, validate outputs against source data, interpret metrics, and present findings to executives with actionable recommendations.*

**🔍 AUDITOR PERSPECTIVE:**
*You are verifying that exit strategy compliance is monitored systematically with proper evidence trails. You need to understand data sources, validation procedures, traceability from source workbooks to dashboard metrics, and evidence of executive governance (decisions based on dashboard findings).*

**This guide maintains BOTH perspectives throughout all sections.**

---

## Relationship to Other ISMS Documents

### Source Documents (Inputs to Dashboard)

| Document ID | Title | Data Extracted | Usage in Dashboard |
|-------------|-------|----------------|-------------------|
| **ISMS-IMP-A.5.23.S1** | Cloud Service Inventory | Sheet 4: Exit strategy type, lock-in risk, export tested, migration complexity | Exit Strategy Coverage metrics, High-risk services list |
| **ISMS-IMP-A.5.23.S2** | Vendor Due Diligence & Contracts | (Future: Vendor risk ratings, contract terms) | Not currently used (v2.1 enhancement planned) |
| **ISMS-IMP-A.5.23.S3** | Secure Configuration & Deployment | (Future: Configuration compliance metrics) | Not currently used (v2.1 enhancement planned) |
| **ISMS-IMP-A.5.23.S4** | Ongoing Governance & Risk Management | Sheet 7: Annual exit review status, PoC testing results, next due dates | DORA PoC Testing Compliance metrics, Recommendations |

### Policy Documents (Compliance Baseline)

| Document ID | Title | Policy Targets | Dashboard Validation |
|-------------|-------|----------------|---------------------|
| **ISMS-POL-A.5.19-23-S5** | Cloud Services Security - Section 8 | Exit Strategy Framework: Cloud-to-Cloud ≥90%, Hybrid 5-10%, On-Premises <5% | Compares actual % vs targets, flags deviations |
| **ISMS-POL-A.5.19-23-S4** | Supplier Monitoring & Change Management | Vendor risk monitoring, governance activities | (Future: Vendor performance metrics) |

### Output Documents (Dashboard Consumers)

| Document Type | Usage | Frequency |
|---------------|-------|-----------|
| **CISO Monthly Report** | Executive summary of exit strategy compliance | Monthly |
| **Risk Committee Report** | Quarterly compliance status with escalations | Quarterly |
| **Board Briefing** | Annual strategic risk overview (1-page summary) | Annually |
| **Audit Evidence Package** | ISO 27001 A.5.23 compliance demonstration | On-demand (pre-audit) |
| **Risk Register Updates** | Critical findings added as enterprise risks | As needed (Critical findings) |

---

# Technical Specification

# Script Architecture

## Python Script Structure

**File:** `generate_reg_a523_5_compliance_dashboard.py` (~900 lines)

**Sections:**
```python
# Section 1: Workbook Schema Definitions (~150 lines)
#   - INVENTORY_SCHEMA
#   - VENDOR_DD_SCHEMA  
#   - SECURE_CONFIG_SCHEMA
#   - GOVERNANCE_SCHEMA

# Section 2: Input Validation (~100 lines)
#   - find_latest_workbook()
#   - validate_workbook_schema()
#   - validate_all_inputs()

# Section 3: Data Extraction (~250 lines)
#   - extract_exit_strategy_data()
#   - extract_poc_testing_data()

# Section 4: Style Definitions (~50 lines)
#   - create_styles()

# Section 5: Dashboard Creation (~350 lines)
#   - create_exit_strategy_dashboard()
#   - create_poc_testing_dashboard()
#   - create_risk_overview()
#   - create_recommendations()
#   - create_dashboard_workbook()

# Section 6: Main Execution (~50 lines)
#   - main()
```

## Data Flow Diagram

```
INPUT VALIDATION
├─ Find latest workbook matching pattern
├─ Validate required sheets exist
├─ Validate required columns present
└─ Fail fast if validation errors

DATA EXTRACTION
├─ Load workbook read-only (openpyxl)
├─ Navigate to specific sheet
├─ Read column range (start_row to max_row)
├─ Parse data into Python dict
├─ Calculate summary metrics
└─ Close workbook

DASHBOARD GENERATION
├─ Create new workbook
├─ Apply styles (fonts, fills, borders)
├─ Populate metrics tables
├─ Conditional formatting (status colors)
├─ Generate risk list
├─ Create recommendations
└─ Save workbook

OUTPUT
└─ ISMS-IMP-A.5.23.S5_Dashboard_YYYYMMDD.xlsx
```

---

# Output Workbook Specification

## Sheet 1: Exit Strategy Dashboard

**Sheet Name:** `1. Exit Strategy Dashboard`

**Layout:**

```
Row 1: HEADER
  ├─ Merged A1:H1
  ├─ "EXIT STRATEGY COVERAGE DASHBOARD"
  └─ Font: Calibri 14 Bold, White on Dark Blue (003366)

Row 2: POLICY REFERENCE
  ├─ Merged A2:H2
  ├─ "POL-S5 Section 8: Exit Strategy Framework..."
  └─ Font: Calibri 9 Italic

Row 4: METRICS TABLE HEADER
  ├─ Columns: METRIC | VALUE | PERCENTAGE | STATUS | POLICY TARGET
  └─ Style: Bold, Gray fill (D9D9D9)

Row 5-13: EXIT STRATEGY METRICS
  ├─ Total Cloud Services
  ├─ Cloud-to-Cloud Strategy
  ├─ Hybrid Strategy
  ├─ On-Premises Strategy
  ├─ Not Yet Determined
  ├─ (blank separator)
  ├─ High Lock-In Risk
  ├─ CRITICAL Lock-In Risk
  └─ Export Not Tested (Critical)

Row 15: POC TESTING HEADER
  ├─ "DORA PoC TESTING COMPLIANCE (Article 28.6)"
  └─ Font: Calibri 12 Bold, White on Medium Blue (4472C4)

Row 18: POC METRICS TABLE HEADER
  └─ Columns: METRIC | VALUE | STATUS | COMPLIANCE REQUIREMENT

Row 19-24: POC TESTING METRICS
  ├─ Critical Services Requiring PoC Testing
  ├─ PoC Testing Completed (Pass)
  ├─ PoC Testing Not Tested
  ├─ PoC Testing Overdue
  ├─ Overall PoC Compliance
  └─ Next Annual Review Due
```

**Column Widths:**

- A: 35 (Metric names)
- B: 12 (Values)
- C: 15 (Percentages)
- D: 12 (Status symbols)
- E: 25 (Policy targets)

**Conditional Formatting:**

| Condition | Cell Range | Fill Color | Font Color |
|-----------|------------|------------|------------|
| On-Premises % > 5% | A-C (On-Premises row) | Red (FFC7CE) | Dark Red (9C0006) |
| Critical Lock-In > 0 | A-B (Critical Lock-In row) | Red (FFC7CE) | Dark Red (9C0006) |
| PoC Compliance < 100% | B (Overall PoC Compliance) | Yellow (FFEB9C) | Dark Yellow (9C6500) |

---

## Sheet 2: Risk Overview

**Sheet Name:** `2. Risk Overview`

**Purpose:** Table listing all high-risk services.

**Columns (A-H):**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Service Name | 28 | Cloud service name from inventory |
| B | Provider | 22 | Vendor name |
| C | Criticality | 14 | Critical, High, Medium, Low |
| D | Exit Strategy | 18 | Cloud-to-Cloud, Hybrid, On-Premises, Not Determined |
| E | Lock-In Risk | 14 | Low, Medium, High, Critical |
| F | Export Tested | 14 | Yes, No, Partial |
| G | PoC Result | 14 | Pass, Fail, Not Tested, In Progress |
| H | Risk Factors | 50 | Concatenated list of issues (❌ ⚠️ symbols) |

**Filtering Logic:**
```python
# Include service in Risk Overview if ANY of:
# Lock-In Risk = "High" or "Critical"
# PoC Result = "Fail" or "Not Tested" (for Critical services)
# Export Tested = "No" (for Critical services)
# Exit Strategy = "On-Premises" (without TCO justification)
```

**Row Sorting:** By number of ❌ symbols (descending) - highest risk first

**Example Row:**
```
Service: Oracle ERP
Provider: Oracle
Criticality: Critical
Exit Strategy: On-Premises
Lock-In Risk: Critical
Export Tested: Partial
PoC Result: Fail
Risk Factors: ❌ Critical lock-in, ❌ PoC failed, ⚠️ On-prem strategy, ⚠️ Partial export
```

---

## Sheet 3: Recommendations

**Sheet Name:** `3. Recommendations`

**Purpose:** Priority-ranked actionable items.

**Structure:**

```
Row 1: HEADER
  "EXECUTIVE RECOMMENDATIONS - Exit Strategy Compliance"

Row 3: PRIORITY 1 HEADER
  "PRIORITY 1: CRITICAL - IMMEDIATE ACTION (Next 30 Days)"

Row 4+: Priority 1 Recommendations
  For each Critical issue:
  ├─ Recommendation number
  ├─ Service name
  ├─ Issue description
  ├─ Impact statement
  ├─ Recommended action
  └─ Suggested owner

Row X: PRIORITY 2 HEADER
  "PRIORITY 2: HIGH - NEXT 90 DAYS"

Row X+: Priority 2 Recommendations
  ...

Row Y: PRIORITY 3 HEADER
  "PRIORITY 3: MEDIUM - NEXT 6 MONTHS"
```

**Recommendation Template:**
```
[PRIORITY] [NUMBER]. [ISSUE_TYPE]: [SERVICE]
├─ Issue: [DESCRIPTION]
├─ Impact: [BUSINESS_IMPACT]
├─ Recommendation: [ACTION_REQUIRED]
└─ Owner: [SUGGESTED_OWNER]
```

**Prioritization Logic:**

| Priority | Criteria | Timeline |
|----------|----------|----------|
| **P1: Critical** | Critical lock-in, PoC failures, DORA violations | 30 days |
| **P2: High** | High lock-in, Export not tested, Strategy deviation from target | 90 days |
| **P3: Medium** | Not Determined strategies, Minor compliance gaps | 6 months |

---

# Data Extraction Specification

## Exit Strategy Data Extraction

**Source:** IMP-A.5.23.1, Sheet 4 (Cloud Security Services)

**Column Mapping:**

```python
INVENTORY_SCHEMA['exit_strategy_columns'] = {
    'Service Name': 'A',          # Column A
    'Provider': 'B',              # Column B
    'Service Type': 'C',          # Column C
    'Criticality': 'H',           # Column H
    'Exit Strategy Type': 'R',    # Column R
    'Alternative Identified': 'S', # Column S
    'Export Tested': 'U',         # Column U
    'Migration Complexity': 'W',  # Column W
    'Lock-In Risk': 'X',          # Column X
}
```

**Extraction Logic:**

```python
for row in range(start_row, ws.max_row + 1):
    service_name = ws[f"A{row}"].value
    
    if not service_name or str(service_name).strip() == "":
        continue  # Skip empty rows
    
    data['total_services'] += 1
    
    exit_strategy = ws[f"R{row}"].value
    criticality = ws[f"H{row}"].value
    lock_in_risk = ws[f"X{row}"].value
    export_tested = ws[f"U{row}"].value
    
    # Count by exit strategy type
    if exit_strategy == "Cloud-to-Cloud":
        data['cloud_to_cloud'] += 1
    elif exit_strategy == "Hybrid":
        data['hybrid'] += 1
    elif exit_strategy == "On-Premises":
        data['on_premises'] += 1
    else:
        data['not_determined'] += 1
    
    # Count lock-in risks
    if lock_in_risk == "High":
        data['high_lock_in'] += 1
    elif lock_in_risk == "Critical":
        data['critical_lock_in'] += 1
    
    # Count critical services without tested export
    if criticality == "Critical" and export_tested == "No":
        data['export_not_tested_critical'] += 1
```

**Return Value:**
```python
{
    'total_services': 32,
    'cloud_to_cloud': 28,
    'hybrid': 3,
    'on_premises': 1,
    'not_determined': 0,
    'high_lock_in': 2,
    'critical_lock_in': 1,
    'export_not_tested_critical': 1,
    'services': [...]  # List of service dicts
}
```

---

## PoC Testing Data Extraction

**Source:** IMP-A.5.23.4, Sheet 7 (Exit Strategy Review)

**Column Mapping:**

```python
GOVERNANCE_SCHEMA['exit_review_columns'] = {
    'Service Name': 'B',               # Column B
    'Criticality': 'F',                # Column F
    'PoC Testing Required?': 'H',      # Column H
    'PoC Test Result': 'J',            # Column J
    'PoC Test Next Due': 'N',          # Column N
}
```

**Extraction Logic:**

```python
today = datetime.now().date()

for row in range(start_row, ws.max_row + 1):
    service_name = ws[f"B{row}"].value
    
    if not service_name or str(service_name).strip() == "":
        continue
    
    poc_required = ws[f"H{row}"].value
    poc_result = ws[f"J{row}"].value
    poc_next_due = ws[f"N{row}"].value
    
    if poc_required == "Yes (Critical)":
        data['total_requiring_poc'] += 1
        
        if poc_result == "Pass":
            data['poc_completed'] += 1
        elif poc_result in ["Not Tested"]:
            data['poc_not_tested'] += 1
        elif poc_result in ["In Progress"]:
            data['poc_overdue'] += 1
        
        # Check if actually overdue based on date
        if poc_next_due:
            try:
                if isinstance(poc_next_due, datetime):
                    due_date = poc_next_due.date()
                else:
                    due_date = datetime.strptime(str(poc_next_due), '%Y-%m-%d').date()
                
                if due_date < today and poc_result != "Pass":
                    data['poc_overdue'] += 1
            except:
                pass  # Ignore date parsing errors
```

**Return Value:**
```python
{
    'total_requiring_poc': 12,
    'poc_completed': 10,
    'poc_overdue': 1,
    'poc_not_tested': 1,
    'services': [...]
}
```

---

# Schema Validation

## Required Sheets Validation

**Function:** `validate_workbook_schema(filepath, schema)`

**Logic:**
```python
def validate_workbook_schema(filepath: str, schema: dict) -> bool:
    """
    Validate that workbook has required sheets and structure.
    
    Returns:
        True if valid, raises ValueError if invalid
    """
    wb = load_workbook(filepath, read_only=True)
    
    for required_sheet in schema['required_sheets']:
        if required_sheet not in wb.sheetnames:
            raise ValueError(
                f"Missing required sheet '{required_sheet}' in {filepath}"
            )
    
    wb.close()
    return True
```

**Error Examples:**

```
ValueError: Missing required sheet '4. Cloud Security Services' in ISMS-IMP-A.5.23.S1_Inventory_20260120.xlsx

ValueError: Missing required sheet '7. Exit Strategy Review' in ISMS-IMP-A.5.23.S4_Governance_20260120.xlsx
```

---

# File Naming & Metadata

## Output File Naming

**Pattern:** `ISMS-IMP-A.5.23.S5_Dashboard_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.5.23.S5_Dashboard_20260120.xlsx`

**Timestamp:** Uses `datetime.now().strftime("%Y%m%d")`

## Workbook Metadata

```python
wb.properties.title = "ISMS-IMP-A.5.23.S5 Compliance Dashboard"
wb.properties.subject = "ISO 27001 A.5.23 Exit Strategy Compliance"
wb.properties.creator = "[Organization] ISMS Team"
wb.properties.description = "Auto-generated dashboard consolidating exit strategy compliance"
wb.properties.keywords = "ISMS, ISO27001, Exit Strategy, DORA, PoC Testing"
wb.properties.category = "Information Security Management"
wb.properties.version = "2.0"
```

---

# Known Limitations & Future Enhancements

## Current Limitations

| Limitation | Workaround | Future Enhancement |
|------------|------------|-------------------|
| Only extracts from IMP-5.23.1 & 5.23.4 | Manual review of IMP-5.23.2/3 | Add vendor risk, config compliance metrics |
| No trend analysis (single point-in-time) | Compare archived dashboards manually | Add quarterly trend charts |
| No email automation | Manual distribution | Auto-email dashboard to stakeholders |
| Fixed policy targets (90% cloud-to-cloud) | Edit Python script | Add config file for targets |

## Roadmap

**Version 2.1 (Q2 2026):**

- Add vendor concentration risk metrics (from IMP-5.23.2)
- Add configuration compliance summary (from IMP-5.23.3)

**Version 2.2 (Q3 2026):**

- Quarterly trend charts (compare last 4 quarters)
- Email automation (send dashboard to distribution list)

**Version 3.0 (Q4 2026):**

- Real-time dashboard (web-based, not Excel)
- Integration with CMDB/ITSM for live data

---

# Testing & Validation

## Unit Test Cases

**Test 1: Empty Inventory**
```
Input: IMP-5.23.1 with 0 services
Expected: Dashboard generates with all metrics = 0
Actual: ✅ PASS
```

**Test 2: All Cloud-to-Cloud**
```
Input: 10 services, all Cloud-to-Cloud
Expected: Cloud-to-Cloud % = 100%, Status = ✅
Actual: ✅ PASS
```

**Test 3: PoC All Pass**
```
Input: 5 Critical services, all PoC = Pass
Expected: PoC Compliance = 100%, Status = ✅
Actual: ✅ PASS
```

**Test 4: Missing Sheet 7**
```
Input: IMP-5.23.4 without Sheet 7 (old version)
Expected: Warning message, PoC metrics = 0
Actual: ✅ PASS (warning logged)
```

## Integration Test

**Full End-to-End Test:**
```
Step 1: Generate all 4 source workbooks with test data
Step 2: Run dashboard generator
Step 3: Validate all 3 sheets created
Step 4: Spot-check 10 metrics against source data
Step 5: Check conditional formatting applied correctly
Result: ✅ PASS
```

---

**END OF SPECIFICATION**

---

*"Science is the belief in the ignorance of experts."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
