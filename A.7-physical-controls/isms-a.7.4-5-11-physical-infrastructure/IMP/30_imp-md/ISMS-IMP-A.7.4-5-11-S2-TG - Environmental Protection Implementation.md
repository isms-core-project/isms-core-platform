**ISMS-IMP-A.7.4-5-11-S2-TG - Environmental Protection Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.4: Physical Security Monitoring

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.4-5-11-S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Environmental Protection - Fire Detection/Suppression, Water Detection, Temperature/Humidity Monitoring |
| **Related Policy** | ISMS-POL-A.7.4-5-11, Section 3 (Environmental Protection Requirements) |
| **Purpose** | Document deployed environmental protection systems, assess capabilities against policy requirements, and identify gaps |
| **Target Audience** | Facilities Management, Fire/Life Safety Technicians, HVAC Technicians, Security Operations, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Environmental Protection assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.4-5-11-S2-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.4.2_Environmental_Protection_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a74_2_environmental_protection.py)

**Sheet Count:** 7 worksheets

**Data Capacity:** 100 data rows per assessment sheet (Sheets 2-4)

**Styling:** Navy blue headers, yellow input cells, conditional formatting for compliance status (green/amber/red)

### Sheet Organization

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Assessment metadata and status legend | Read-only Reference | ~30 rows |
| 2 | Fire Detection | Fire alarm systems, detectors, notification devices inventory | Data Entry | 100 data rows |
| 3 | Water Detection | Water detection systems, sensors, coverage assessment | Data Entry | 100 data rows |
| 4 | Temperature_Humidity | Environmental sensors, thresholds, excursion tracking | Data Entry | 100 data rows |
| 5 | Summary Dashboard | Automated compliance scoring and metrics | Formula-driven | ~40 rows |
| 6 | Evidence Register | Supporting evidence documentation | Data Entry | 100 data rows |
| 7 | Approval Sign-Off | Four-level approval workflow | Data Entry | ~20 rows |

### Workbook Features

**Data Validation:**

- Dropdown lists for standardized input (Panel Type, Monitoring Service, Alert Method, etc.)
- Date validation (valid date format)
- Numeric validation (detector count, sensor count, excursion count)
- Percentage validation (coverage percentage 0-100%)

**Conditional Formatting:**

- Compliance Status columns: Green fill (✅ Compliant), Amber fill (⚠️ Partial), Red fill (❌ Non-Compliant)
- Summary Dashboard scores: Color-coded thresholds (>90% green, 75-89% amber, 60-74% amber, <60% red)
- Overdue dates highlighted (testing overdue, inspection overdue)
- High excursion counts highlighted (>10 excursions in 90 days)

**Formulas:**

- Summary Dashboard auto-calculates from Sheets 2-4
- Compliance Status formulas evaluate multiple criteria per row
- Aggregate metrics (totals, averages, percentages)

**Freeze Panes:**

- Row 1-3 frozen (header rows always visible)
- Column A frozen (facility name always visible when scrolling right)

**Column Widths:**

- Optimized for readability (facility names 25 chars, descriptions 40 chars, notes 50 chars)

**Print Settings:**

- Page orientation: Landscape
- Fit to page: 1 page wide (scroll height)
- Print titles: Header rows repeat on each page

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions & Legend

**Purpose:** Assessment metadata, status legend, and completion instructions

**Structure:**

**Row 1:** Header

- Merged cells A1:G1
- Text: "ISMS-IMP-A.7.4.2 - Physical Environmental Protection Assessment\nISO/IEC 27001:2022 - Control A.7.5: Protecting Against Physical and Environmental Threats"
- Style: Navy blue background, white bold text, 14pt, center-aligned

**Rows 3-11:** Document Information Table

- Column A: Labels (Document ID, Assessment Area, Related Policy, Version, Assessment Date, Completed By, Organization, Review Cycle)
- Column B: Values (pre-filled for read-only fields, blank yellow for user input)
- User input fields (yellow): Assessment Date, Completed By, Organization

**Rows 13-17:** Status Legend

- Column A: Status labels (✅ Compliant, ⚠️ Partial Compliance, ❌ Non-Compliant)
- Column B: Definitions
- Style: Color-coded backgrounds matching compliance colors (green, amber, red)

**Rows 19-30:** Completion Instructions

- Brief workflow summary
- Reference to Part I User Guide for detailed instructions
- Contact information for assessment support

**Cell Styling:**

- Headers: Navy blue background (#003366), white bold text
- Labels: Bold text, gray background (#D9D9D9)
- Input cells: Yellow background (#FFFFCC)
- Read-only cells: White background

### Sheet 2: Fire Detection

**Purpose:** Document all fire alarm systems, detectors, notification devices, and assess compliance against policy requirements

**Header Row (Row 3):**

- Style: Gray background, bold text, center-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility or building name |
| B | Fire Alarm Panel | Text | 30 | None | No | Vendor and model (Simplex, Notifier, Edwards, etc.) |
| C | Panel Type | Dropdown | 15 | List | No | Addressable / Conventional / Hybrid |
| D | Smoke Detector Count | Number | 15 | Integer >0 | No | Total smoke detectors |
| E | Heat Detector Count | Number | 15 | Integer ≥0 | No | Total heat detectors (0 if none) |
| F | Detector Technology | Text | 25 | None | No | Photoelectric, Ionization, Dual-sensor, Aspirating |
| G | Notification Devices | Text | 25 | None | No | Horn/strobe count and type |
| H | Coverage Percentage | Number | 15 | Integer 0-100 | No | % of facility area covered |
| I | Monitoring Service | Dropdown | 25 | List | No | Yes - Professional / Yes - Self (BMS/SOC) / No |
| J | Backup Communication | Dropdown | 20 | List | No | Yes - Cellular / Yes - Dual path / No |
| K | Last Testing Date | Date | 15 | Date | No | Last annual fire alarm test date |
| L | Last Fire Marshal Inspection | Date | 18 | Date | No | Last fire marshal inspection date |
| M | Compliance Status | Formula | 18 | None | Yes | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant |
| N | Notes | Text | 50 | None | No | Additional context, gaps, remediation plans |

**Compliance Status Formula (Column M):**
```excel
=IF(AND(H2=100, I2<>"No", (TODAY()-K2)<=365, (TODAY()-L2)<=365), "✅ Compliant",
   IF(OR(H2<90, I2="No", (TODAY()-K2)>547, (TODAY()-L2)>547), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**

- ✅ Compliant IF: 100% coverage AND monitoring service active AND testing within 365 days AND fire marshal inspection within 365 days
- ❌ Non-Compliant IF: Coverage <90% OR no monitoring service OR testing >18 months overdue OR fire marshal inspection >18 months overdue
- ⚠️ Partial: Everything else (e.g., 95% coverage, testing slightly overdue)

**Conditional Formatting:**

- Column M: Green background if "✅ Compliant", Amber if "⚠️ Partial", Red if "❌ Non-Compliant"
- Column K: Red background if (TODAY()-K2)>365 (testing overdue)
- Column L: Red background if (TODAY()-L2)>365 (inspection overdue)

**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (facility name)

### Sheet 3: Water Detection

**Purpose:** Document all water detection systems, sensors, coverage areas, and assess compliance

**Header Row (Row 3):**

- Style: Gray background, bold text, center-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility or area name |
| B | Water Detection System | Text | 30 | None | No | Vendor and model |
| C | Sensor Count | Number | 12 | Integer >0 | No | Total water sensors |
| D | Sensor Type | Text | 25 | None | No | Spot, Cable, Wireless, Wired to BMS |
| E | Coverage Areas | Text | 30 | None | No | Areas protected |
| F | High-Risk Areas Covered | Dropdown | 20 | List | No | Yes - All covered / Partial - Some gaps / No - Missing coverage |
| G | Alert Method | Text | 25 | None | No | Email, SMS, BMS alarm, Alarm panel |
| H | Alert Recipients | Text | 30 | None | No | Who receives alerts |
| I | Response Procedure Documented | Dropdown | 20 | List | No | Yes / No |
| J | Last Testing Date | Date | 15 | Date | No | Last monthly water sensor test |
| K | Compliance Status | Formula | 18 | None | Yes | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant |
| L | Notes | Text | 50 | None | No | Additional context, gaps, remediation plans |

**Compliance Status Formula (Column K):**
```excel
=IF(AND(F2="Yes - All covered", G2<>"", I2="Yes", (TODAY()-J2)<=31), "✅ Compliant",
   IF(OR(F2="No - Missing coverage", G2="", I2="No", (TODAY()-J2)>60), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**

- ✅ Compliant IF: All high-risk areas covered AND alert method configured AND response procedure documented AND testing within 31 days
- ❌ Non-Compliant IF: No coverage in high-risk areas OR no alert method OR no response procedure OR testing >60 days overdue
- ⚠️ Partial: Everything else

**Conditional Formatting:**

- Column K: Green background if "✅ Compliant", Amber if "⚠️ Partial", Red if "❌ Non-Compliant"
- Column J: Red background if (TODAY()-J2)>31 (testing overdue)

**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (facility name)

### Sheet 4: Temperature_Humidity

**Purpose:** Document all temperature/humidity monitoring systems, sensors, thresholds, and assess compliance

**Header Row (Row 3):**

- Style: Gray background, bold text, center-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility or monitoring zone |
| B | Monitoring Platform | Text | 30 | None | No | Vendor and model |
| C | Sensor Count | Number | 12 | Integer >0 | No | Total environmental sensors |
| D | Sensor Locations | Text | 30 | None | No | Intake, exhaust, return air |
| E | Temperature Thresholds (°C) | Text | 25 | None | No | Warning and critical thresholds |
| F | Humidity Thresholds (%RH) | Text | 25 | None | No | Warning and critical thresholds |
| G | Alert Method | Text | 25 | None | No | Email, SMS, BMS alarm, Dashboard |
| H | Alert Recipients | Text | 30 | None | No | Who receives alerts |
| I | Data Retention (Months) | Number | 15 | Integer >0 | No | Months of data retained |
| J | Sensor Accuracy Verified | Dropdown | 20 | List | No | Yes - Within 6 months / Yes - Within 12 months / No / Unknown |
| K | Excursions Last 90 Days | Number | 18 | Integer ≥0 | No | Count of threshold exceedances |
| L | Compliance Status | Formula | 18 | None | Yes | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant |
| M | Notes | Text | 50 | None | No | Additional context, gaps, remediation plans |

**Compliance Status Formula (Column L):**
```excel
=IF(AND(E2<>"", F2<>"", G2<>"", I2>=12, K2<5), "✅ Compliant",
   IF(OR(E2="", G2="", I2<6, K2>10), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**

- ✅ Compliant IF: Temperature thresholds configured AND humidity thresholds configured AND alert method configured AND data retention ≥12 months AND excursions <5 in 90 days
- ❌ Non-Compliant IF: No temperature thresholds OR no alert method OR data retention <6 months OR excursions >10 in 90 days
- ⚠️ Partial: Everything else (e.g., moderate excursions 5-10, data retention 6-11 months)

**Conditional Formatting:**

- Column L: Green background if "✅ Compliant", Amber if "⚠️ Partial", Red if "❌ Non-Compliant"
- Column K: Red background if >10 (high excursions indicate HVAC issues)

**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (facility name)

### Sheet 5: Summary Dashboard

**Purpose:** Automated compliance scoring and key performance indicators

**Structure:** Dashboard layout with metrics and charts

**Row 1:** Header

- Merged cells A1:H1
- Text: "Environmental Protection - Summary Dashboard"
- Style: Navy blue background, white bold text, 14pt, center-aligned

**Rows 3-10:** Overall Compliance Score

- Row 3: "Overall Compliance Score" label
- Row 4: Formula calculating aggregate score from Sheets 2-4
- Row 5: Color-coded status (Green >90%, Amber 75-89%, Amber 60-74%, Red <60%)

**Overall Compliance Score Formula:**
```excel
=(COUNTIF('Fire Detection'!M:M,"✅ Compliant")/COUNTA('Fire Detection'!M:M)*0.4 +
  COUNTIF('Water Detection'!K:K,"✅ Compliant")/COUNTA('Water Detection'!K:K)*0.3 +
  COUNTIF(Temperature_Humidity!L:L,"✅ Compliant")/COUNTA(Temperature_Humidity!L:L)*0.3)*100
```

**Weighting:** Fire Detection 40%, Water Detection 30%, Temperature/Humidity 30%

**Rows 12-20:** Domain Scores

- Fire Detection Compliance Score (%)
- Water Detection Compliance Score (%)
- Temperature/Humidity Compliance Score (%)
- Each with formula, percentage display, color-coding

**Rows 22-30:** Environmental Incident Metrics

- Fire Alarm Events (last 12 months): Count of fire alarms (actual + false)
- Water Damage Incidents (last 12 months): Count of water detection events
- Temperature Excursions (last 90 days): Sum of excursions from Sheet 4
- Average Excursions per Facility: Average of Sheet 4, Column K

**Rows 32-50:** Gap Summary

- Auto-generated list of non-compliant items
- Formula scans Sheets 2-4 for "❌ Non-Compliant" status
- Lists facility name, system type, gap description
- Prioritized by severity

**Gap Summary Formula (example for row 32):**
```excel
=IF(COUNTIF('Fire Detection'!M:M,"❌ Non-Compliant")>0,
   INDEX('Fire Detection'!A:A, MATCH("❌ Non-Compliant",'Fire Detection'!M:M,0)) & " - Fire Detection Gap",
   IF(COUNTIF('Water Detection'!K:K,"❌ Non-Compliant")>0,
      INDEX('Water Detection'!A:A, MATCH("❌ Non-Compliant",'Water Detection'!K:K,0)) & " - Water Detection Gap",
      "No Critical Gaps Identified"))
```

**Charts:**

- Chart 1: Overall Compliance Score (gauge chart)
- Chart 2: Domain Scores (bar chart - Fire Detection, Water Detection, Temperature/Humidity)
- Chart 3: Temperature Excursion Trend (line chart - if historical data available)
- Chart 4: Gap Distribution (pie chart - compliant vs. partial vs. non-compliant)

**Conditional Formatting:**

- Compliance scores: Green >90%, Amber 75-89%, Red <60%
- Gap summary: Red highlight for critical gaps, amber for partial compliance

### Sheet 6: Evidence Register

**Purpose:** Document all supporting evidence with audit traceability

**Header Row (Row 3):**

- Style: Gray background, bold text, center-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Evidence ID | Text | 12 | None | No | Unique identifier (EVID-001, EVID-002, etc.) |
| B | Evidence Type | Dropdown | 18 | List | No | Screenshot / Config Export / Log Sample / Report / Document / Photo |
| C | Description | Text | 40 | None | No | What evidence shows |
| D | Related Sheet/Item | Text | 25 | None | No | Links to specific assessment row |
| E | File Name | Text | 35 | None | No | Evidence filename |
| F | File Location | Text | 50 | None | No | Path to evidence file |
| G | Collection Date | Date | 15 | Date | No | When evidence collected |
| H | Collected By | Text | 25 | None | No | Who collected evidence |
| I | Retention Period | Text | 18 | None | No | 3 years, Permanent, etc. |
| J | Notes | Text | 50 | None | No | Additional context |

**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (evidence ID)

**Conditional Formatting:**

- Column G: Red background if >30 days old (stale evidence warning)

### Sheet 7: Approval Sign-Off

**Purpose:** Four-level approval workflow documentation

**Structure:**

**Row 1:** Header

- Merged cells A1:E1
- Text: "Assessment Approval Workflow"
- Style: Navy blue background, white bold text, 14pt, center-aligned

**Rows 3-20:** Approval Table

| Approval Level | Role | Name | Date | Signature/Confirmation | Comments |
|----------------|------|------|------|------------------------|----------|
| Level 1 | Assessor | [Input] | [Input] | [Input] | |
| Level 2 | Facilities Manager | [Input] | [Input] | [Input] | [Input] |
| Level 3 | CISO | [Input] | [Input] | [Input] | [Input] |
| Level 4 | Compliance Officer | [Input] | [Input] | [Input] | [Input] |

**Cell Styling:**

- Level labels: Bold text, gray background
- Input cells: Yellow background (Name, Date, Signature, Comments)
- Instructions below table (rows 10-20): Workflow sequence, timeline expectations

---

## Cell Styling Reference

### Color Palette

**Headers:**

- Primary Header (Sheet titles, Row 1): #003366 (Navy blue background), #FFFFFF (White text)
- Subheader (Section titles): #4472C4 (Medium blue background), #FFFFFF (White text)
- Column Header (Row 3): #D9D9D9 (Light gray background), #000000 (Black text)

**Data Cells:**

- Input Cell (Yellow): #FFFFCC (Light yellow background) - indicates user should enter data
- Formula Cell (White): #FFFFFF (White background) - read-only, auto-calculated
- Read-Only Cell (Light gray): #F2F2F2 (Very light gray background) - pre-filled, do not edit

**Compliance Status:**

- Compliant: #C6EFCE (Light green background)
- Partial Compliance: #FFEB9C (Light amber/yellow background)
- Non-Compliant: #FFC7CE (Light red background)

**Alerts:**

- Warning (Amber): #FFEB9C (Light amber background)
- Critical (Red): #FFC7CE (Light red background)
- Success (Green): #C6EFCE (Light green background)

### Font Specifications

**Headers:**

- Font: Calibri
- Size: 14pt (primary header), 11pt (subheader), 10pt (column header)
- Weight: Bold
- Color: #FFFFFF (white) for primary/subheader, #000000 (black) for column header

**Data Cells:**

- Font: Calibri
- Size: 10pt
- Weight: Normal (regular for data, bold for labels)
- Color: #000000 (black)

**Status Text:**

- Font: Calibri
- Size: 10pt
- Weight: Bold
- Uses Unicode symbols: ✅ (U+2705), ⚠️ (U+26A0), ❌ (U+274C)

### Border Styles

**Table Borders:**

- Style: Thin solid line
- Color: #000000 (black)
- Applied to: All data table cells (Sheets 2-4, 6)

**Header Borders:**

- Style: Medium solid line (bottom border only)
- Color: #000000 (black)
- Applied to: Column header row (Row 3)

### Alignment

**Headers:**

- Horizontal: Center
- Vertical: Center
- Wrap text: Yes (for long header labels)

**Data Cells:**

- Text fields: Left-aligned, top-aligned
- Numeric fields: Right-aligned, top-aligned
- Date fields: Left-aligned, top-aligned
- Formula fields: Center-aligned (status indicators)

### Cell Protection

**Protected Cells (Formula cells):**

- Summary Dashboard (Sheet 5): All cells except approval override
- Compliance Status columns (Sheets 2-4): Formula-protected
- Header rows (Row 1-3 all sheets): Protected

**Unlocked Cells (Input cells):**

- All yellow background cells (user input required)
- Evidence Register (Sheet 6): All data cells
- Approval Sign-Off (Sheet 7): Name, Date, Signature, Comments cells

**Sheet Protection:**

- Password: [Organization-specific]
- Allow: Select unlocked cells, format cells (unlocked cells only)
- Disallow: Insert/delete rows, modify formulas, edit locked cells

---

## Integration Points

### Integration with Policy (ISMS-POL-A.7.4-5-11)

**Policy Section → Assessment Sheet Mapping:**

| Policy Section | Policy Reference | Assessment Sheet | Assessment Focus |
|----------------|------------------|------------------|------------------|
| Section 3.1: Environmental Threat Assessment | ISMS-POL-A.7.4-5-11, §3.1 | All Sheets | Geographic threats inform coverage requirements |
| Section 3.2: Fire Detection and Suppression | ISMS-POL-A.7.4-5-11, §3.2 | Sheet 2: Fire Detection | Fire alarm panels, detectors, notification devices, monitoring |
| Section 3.3: Flood and Water Damage Protection | ISMS-POL-A.7.4-5-11, §3.3 | Sheet 3: Water Detection | Water sensors, coverage, alerts, response procedures |
| Section 3.4: Temperature and Humidity Control | ISMS-POL-A.7.4-5-11, §3.4 | Sheet 4: Temperature_Humidity | Environmental sensors, thresholds, HVAC monitoring, excursions |
| Section 3.5: Structural Protection | ISMS-POL-A.7.4-5-11, §3.5 | Sheet 2 Notes | Structural protection noted where relevant (seismic, wind) |
| Section 3.6: Environmental Protection Plan | ISMS-POL-A.7.4-5-11, §3.6 | Sheet 3: Response Procedure | Response procedures documented |

**Assessment validates policy compliance by comparing deployed systems against policy requirements:**

- Policy states "100% coverage by smoke/heat detection" → Assessment verifies 100% in Sheet 2, Column H
- Policy states "Monthly water sensor testing" → Assessment verifies testing within 31 days in Sheet 3, Column J
- Policy states "Temperature monitoring with alerts" → Assessment verifies thresholds and alerts in Sheet 4, Columns E/F/G

### Integration with Other Assessments

**Feeds into:**

- ISMS-IMP-A.7.4-5-11-S4 (Compliance Dashboard): Overall compliance score, gap summary, environmental incident metrics
- ISMS-IMP-A.7.4-5-11-S3 (Utility Resilience): HVAC systems documented in both (environmental monitoring here, HVAC resilience in S3)

**Dependencies from:**

- Facility inventory: List of all facilities requiring assessment (if master facility list exists)
- Fire marshal inspection schedule: Annual inspections inform Sheet 2, Column L

**Shared evidence with:**

- Fire marshal inspection reports: Evidence for both environmental protection and facility compliance
- HVAC system documentation: Shared with utility resilience assessment (S3)

### Integration with Evidence Collection

**Evidence Register (Sheet 6) cross-references Assessment Sheets:**

- Evidence ID "EVID-003" → Related Sheet/Item: "Sheet 2, Row 4 (Building A Fire Detection)"
- File Name: "BuildingA_FireAlarm_Panel_Config_20260115.png"
- Assessment Sheet 2, Row 4, Column N (Notes): "Evidence: EVID-003"

**Evidence Traceability:**
```
Assessment Finding (Sheet 2, Row 4) ← Evidence (EVID-003) ← Evidence File (BuildingA_FireAlarm_Panel_Config_20260115.png)
```

**Audit Flow:**
1. Auditor reviews Sheet 2 (Fire Detection), identifies non-compliant item
2. Auditor checks Sheet 6 (Evidence Register) for supporting evidence ID
3. Auditor requests evidence file from File Location
4. Evidence file verifies or refutes assessment finding (fire marshal inspection report shows compliance)

### Integration with Audit Process

**Audit Deliverables:**
1. **Assessment Workbook:** ISMS-IMP-A.7.4.2_Environmental_Protection_YYYYMMDD_FINAL.xlsx (all sheets)
2. **Evidence Folder:** All files listed in Sheet 6 Evidence Register
3. **Approval Documentation:** Sheet 7 showing four-level approval workflow complete
4. **Gap Remediation Plan:** Derived from Sheet 5 Gap Summary (separate document or embedded in workbook)

**Auditor Review Process:**
1. Review Summary Dashboard (Sheet 5) for overall compliance score
2. Identify non-compliant areas (red status) in Sheets 2-4
3. Review Evidence Register (Sheet 6) for supporting evidence (especially fire marshal inspection reports)
4. Sample evidence files (verify 10-20% of evidence items, prioritize fire marshal reports and testing records)
5. Interview Facilities Manager (validate assessment accuracy, discuss remediation plans)
6. Physical facility inspection (spot-check fire detectors exist, water sensors placed correctly, temperature sensors functional)
7. Issue audit findings (if gaps identified) or confirm compliance

**Audit Questions Anticipated (Part I guides assessor to address proactively):**

- "How do you know fire detector count is accurate?" → Evidence: Fire alarm panel screenshot showing detector list
- "Is fire marshal inspection current?" → Evidence: Fire marshal inspection report within 12 months
- "Are water sensors tested monthly?" → Evidence: Testing logs showing monthly tests
- "What is temperature excursion frequency?" → Sheet 4, Column K documents excursion count, trend shown in Sheet 5
- "Are all high-risk areas covered by water detection?" → Sheet 3, Column F documents coverage status, facility maps show sensor placements

---

**END OF SPECIFICATION**

---

*"Both the man of science and the man of action live always at the edge of mystery, surrounded by it."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-02-06 -->
