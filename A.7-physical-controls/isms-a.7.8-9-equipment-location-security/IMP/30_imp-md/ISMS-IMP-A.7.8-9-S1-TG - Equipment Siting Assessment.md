**ISMS-IMP-A.7.8-9-S1-TG - Equipment Siting Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.8: Equipment Siting and Protection

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.8-9-S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Equipment Siting - Location Assessment, Environmental Protection, Security Measures |
| **Related Policy** | ISMS-POL-A.7.8-9, Section 2.1 (Equipment Siting Requirements) |
| **Purpose** | Document equipment siting locations, assess environmental risks, evaluate physical security measures, and identify gaps |
| **Target Audience** | Facilities Management, IT Operations, Security Operations, Data Centre Managers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Annual or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Equipment Siting assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.8-9-S1-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.8.S1_Equipment_Siting_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a78_1_equipment_siting.py)

**Sheet Count:** 9 worksheets

**Data Capacity:** 100 data rows per assessment sheet

**Styling:** Navy blue headers, yellow input cells, conditional formatting for compliance status (green/amber/red)

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Assessment metadata and status legend | Read-only Reference | ~30 rows |
| 2 | Equipment Locations | Location inventory with criticality and access | Data Entry | 100 data rows |
| 3 | Environmental Assessment | Temperature, humidity, flood, fire risks | Data Entry | 100 data rows |
| 4 | Physical Security | Access control, CCTV, locking, segregation | Data Entry | 100 data rows |
| 5 | Power Infrastructure | UPS, generator, surge, EPO | Data Entry | 100 data rows |
| 6 | Workstation Security | Screen positioning, privacy screens | Data Entry | 100 data rows |
| 7 | Evidence Register | Supporting evidence documentation | Data Entry | 100 data rows |
| 8 | Summary Dashboard | Automated compliance scoring and metrics | Formula-driven | ~40 rows |
| 9 | Approval Sign-Off | Four-level approval workflow | Data Entry | ~20 rows |

### Workbook Features

**Data Validation:**

- Dropdown lists for standardised input (Location Type, Criticality Tier, Access Control Type, etc.)
- Date validation (valid date format)
- Numeric validation (retention days, UPS runtime, workstation count)

**Conditional Formatting:**

- Compliance Status columns: Green fill (Compliant), Amber fill (Partial), Red fill (Non-Compliant)
- Summary Dashboard scores: Colour-coded thresholds (>90% green, 75-89% amber, <75% red)
- Overdue dates highlighted (inspection overdue, testing overdue)

**Formulas:**

- Summary Dashboard auto-calculates from Sheets 2-6
- Compliance Status formulas evaluate multiple criteria per row
- Aggregate metrics (totals, averages, percentages)

**Freeze Panes:**

- Row 1-3 frozen (header rows always visible)
- Column A frozen (location ID always visible when scrolling right)

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions & Legend

**Purpose:** Assessment metadata, status legend, and completion instructions

**Structure:**

**Row 1:** Header
- Merged cells A1:G1
- Text: "ISMS-IMP-A.7.8.S1 - Equipment Siting Assessment\nISO/IEC 27001:2022 - Control A.7.8: Equipment Siting and Protection"
- Style: Navy blue background, white bold text, 14pt, center-aligned

**Rows 3-11:** Document Information Table
- Column A: Labels
- Column B: Values (pre-filled for read-only, yellow for user input)

**Rows 13-17:** Status Legend
- Colour-coded status definitions

**Rows 19-30:** Completion Instructions

### Sheet 2: Equipment Locations

**Purpose:** Document all locations where information processing equipment is sited

**Header Row (Row 3):**
- Style: Gray background, bold text, center-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula |
|-----|------------|------|-------|------------|---------|
| A | Location ID | Text | 12 | None | No |
| B | Location Name | Text | 30 | None | No |
| C | Location Type | Dropdown | 18 | List | No |
| D | Building/Address | Text | 35 | None | No |
| E | Equipment Types | Text | 30 | None | No |
| F | Criticality Tier | Dropdown | 18 | List | No |
| G | Access Control Type | Dropdown | 20 | List | No |
| H | Environmental Monitoring | Dropdown | 22 | List | No |
| I | CCTV Coverage | Dropdown | 20 | List | No |
| J | UPS Protected | Dropdown | 18 | List | No |
| K | Last Physical Inspection | Date | 15 | Date | No |
| L | Compliance Status | Formula | 18 | None | Yes |
| M | Notes | Text | 50 | None | No |

**Compliance Status Formula (Column L):**
```excel
=IF(AND(OR(F2="Tier 3 - Non-Critical",AND(F2="Tier 2 - Standard",OR(G2="Badge Only",G2="Biometric + Badge"))),OR(F2="Tier 3 - Non-Critical",H2<>"No monitoring"),K2>TODAY()-365),"Compliant",IF(OR(AND(F2="Tier 1 - Critical",G2<>"Biometric + Badge"),H2="No monitoring",K2<TODAY()-547),"Non-Compliant","Partial"))
```

### Sheet 3: Environmental Assessment

**Header Row (Row 3):**
- Style: Gray background, bold text, center-aligned

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Location ID | Text | 12 | None |
| B | Location Name | Text | 30 | None |
| C | Temperature Range (C) | Text | 18 | None |
| D | Humidity Range (%RH) | Text | 18 | None |
| E | Temperature Monitoring | Dropdown | 22 | List |
| F | Flood Risk | Dropdown | 20 | List |
| G | Fire Suppression | Dropdown | 22 | List |
| H | Dust/Contamination | Dropdown | 20 | List |
| I | Vibration Exposure | Dropdown | 20 | List |
| J | Food/Drink Prohibited | Dropdown | 20 | List |
| K | Environmental Incidents (12 months) | Number | 15 | Integer |
| L | Compliance Status | Formula | 18 | Yes |
| M | Notes | Text | 50 | None |

### Sheet 4: Physical Security

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Location ID | Text | 12 | None |
| B | Location Name | Text | 30 | None |
| C | Access Control System | Text | 25 | None |
| D | Access Levels Defined | Text | 20 | None |
| E | Access Log Retention (Days) | Number | 18 | Integer |
| F | CCTV System | Text | 25 | None |
| G | CCTV Retention (Days) | Number | 18 | Integer |
| H | Equipment Locking | Dropdown | 22 | List |
| I | Cable Protection | Dropdown | 20 | List |
| J | Asset Labels | Dropdown | 18 | List |
| K | Segregation | Dropdown | 22 | List |
| L | Last Security Review | Date | 15 | Date |
| M | Compliance Status | Formula | 18 | Yes |
| N | Notes | Text | 50 | None |

### Sheet 5: Power Infrastructure

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Location ID | Text | 12 | None |
| B | Location Name | Text | 30 | None |
| C | UPS Coverage | Dropdown | 22 | List |
| D | UPS Runtime (minutes) | Number | 18 | Integer |
| E | Generator Backup | Dropdown | 22 | List |
| F | Surge Protection | Dropdown | 18 | List |
| G | Lightning Protection | Dropdown | 22 | List |
| H | EPO Switch | Dropdown | 20 | List |
| I | Power Redundancy | Dropdown | 22 | List |
| J | Last UPS Test | Date | 15 | Date |
| K | Last Generator Test | Date | 15 | Date |
| L | Power Incidents (12 months) | Number | 15 | Integer |
| M | Compliance Status | Formula | 18 | Yes |
| N | Notes | Text | 50 | None |

### Sheet 6: Workstation Security

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Area ID | Text | 12 | None |
| B | Area Name | Text | 30 | None |
| C | Workstation Count | Number | 15 | Integer |
| D | Data Sensitivity | Dropdown | 22 | List |
| E | Screen Positioning | Dropdown | 25 | List |
| F | Privacy Screens | Dropdown | 22 | List |
| G | Automatic Lock | Dropdown | 22 | List |
| H | Clear Desk Policy | Dropdown | 22 | List |
| I | Visitor Access | Dropdown | 20 | List |
| J | Shoulder Surfing Risk | Dropdown | 20 | List |
| K | Last Review | Date | 15 | Date |
| L | Compliance Status | Formula | 18 | Yes |
| M | Notes | Text | 50 | None |

### Sheet 7: Evidence Register

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Evidence ID | Text | 12 | None |
| B | Evidence Type | Dropdown | 18 | List |
| C | Description | Text | 40 | None |
| D | Related Sheet/Item | Text | 25 | None |
| E | File Name | Text | 35 | None |
| F | File Location | Text | 50 | None |
| G | Collection Date | Date | 15 | Date |
| H | Collected By | Text | 25 | None |
| I | Retention Period | Text | 18 | None |
| J | Notes | Text | 50 | None |

### Sheet 8: Summary Dashboard

**Purpose:** Automated compliance scoring and key performance indicators

**Structure:** Dashboard layout with metrics

**Rows 3-10:** Overall Compliance Score

**Rows 12-22:** Domain Scores
- Equipment Locations Compliance (%)
- Environmental Assessment Compliance (%)
- Physical Security Compliance (%)
- Power Infrastructure Compliance (%)
- Workstation Security Compliance (%)

**Rows 24-40:** Gap Summary

### Sheet 9: Approval Sign-Off

**Structure:**

**Row 1:** Header

**Rows 3-20:** Approval Table
- Level 1: Assessor
- Level 2: Facilities Manager
- Level 3: CISO
- Level 4: Compliance Officer

---

## Cell Styling Reference

### Colour Palette

**Headers:**
- Primary Header: #003366 (Navy blue), #FFFFFF (White text)
- Column Header: #D9D9D9 (Light gray), #000000 (Black text)

**Data Cells:**
- Input Cell: #FFFFCC (Light yellow)
- Formula Cell: #FFFFFF (White)

**Compliance Status:**
- Compliant: #C6EFCE (Light green)
- Partial: #FFEB9C (Light amber)
- Non-Compliant: #FFC7CE (Light red)

### Font Specifications

**Headers:**
- Font: Calibri
- Size: 14pt (primary), 10pt (column)
- Weight: Bold

**Data Cells:**
- Font: Calibri
- Size: 10pt
- Weight: Normal

---

## Integration Points

### Integration with Policy (ISMS-POL-A.7.8-9)

**Policy Section to Assessment Sheet Mapping:**

| Policy Section | Assessment Sheet | Assessment Focus |
|----------------|------------------|------------------|
| Section 2.1.1: Location Selection | Sheet 2: Equipment Locations | Location inventory, criticality, access control |
| Section 2.1.2: Environmental Considerations | Sheet 3: Environmental Assessment | Temperature, humidity, flood, fire, dust |
| Section 2.1.3: Security Measures | Sheet 4: Physical Security | Access control, CCTV, locking, segregation |
| Section 2.1.4: Power and Cabling Protection | Sheet 5: Power Infrastructure | UPS, surge, lightning, EPO |
| Section 2.1.5: Screen Positioning | Sheet 6: Workstation Security | Privacy screens, shoulder surfing prevention |

### Integration with Other Assessments

**Feeds into:**
- ISMS-IMP-A.7.8-9-S3 (Compliance Dashboard): Overall equipment siting and protection compliance
- ISMS-IMP-A.7.4-5-11 (Physical Infrastructure): Environmental and utility controls overlap

**Dependencies from:**
- Facility inventory: List of all locations requiring assessment
- Asset inventory: Equipment at each location

---

**END OF SPECIFICATION**

---

*"Security is mostly a superstition. Life is either a daring adventure or nothing."*
-- Helen Keller

<!-- QA_VERIFIED: 2026-02-06 -->
