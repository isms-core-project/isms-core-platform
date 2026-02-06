**ISMS-IMP-A.7.12-13.S3-TG - Maintenance Schedule Tracking**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.13: Equipment Maintenance

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.12-13.S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Maintenance Schedule Tracking - Preventive Maintenance Planning, Schedule Compliance, Overdue Tracking |
| **Related Policy** | ISMS-POL-A.7.12-13, Section 2.2.1 (Maintenance Programme) |
| **Purpose** | Track preventive maintenance schedules, monitor compliance, identify overdue items, and ensure equipment reliability |
| **Target Audience** | IT Operations, Facilities Management, System Administrators, Asset Managers, Compliance Officers |
| **Assessment Type** | Operational Tracking |
| **Review Cycle** | Monthly Review, Quarterly Full Assessment |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Maintenance Schedule Tracking workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.12-13.S3-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.12-13.S3_Maintenance_Schedule_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a712_3_maintenance_schedule.py)

**Sheet Count:** 7 worksheets

**Styling:** Navy blue headers, yellow input cells, conditional formatting for status

**Protection:** Formula cells protected, input cells unlocked

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions | Configuration and instructions | Reference | ~50 rows |
| 2 | Equipment Schedule | Master maintenance schedule | Data Entry | 200 rows |
| 3 | Overdue Tracking | Overdue item management | Data Entry | 50 rows |
| 4 | Upcoming Maintenance | Forward planning | Formula-driven | ~100 rows |
| 5 | Dashboard | Compliance metrics | Formula-driven | ~60 rows |
| 6 | Maintenance Log | Completion history | Data Entry | 500 rows |
| 7 | Evidence Register | Supporting evidence | Data Entry | 100 rows |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions & Configuration

**Purpose:** Workbook configuration, thresholds, and user instructions

**Structure:**

| Row Range | Content | Type |
|-----------|---------|------|
| 1-3 | Title and version | Static |
| 5-15 | Configuration fields | Input |
| 17-25 | Alert thresholds | Input |
| 27-50 | User instructions | Static |

**Configuration Fields:**

| Cell | Field | Type | Default |
|------|-------|------|---------|
| B5 | Organisation Name | Text | [Enter] |
| B6 | Department | Text | IT Operations |
| B7 | Start Date | Date | [Today] |
| B8 | Update Frequency | Dropdown | Monthly |
| B9 | Primary Contact | Text | [Enter] |
| B10 | CMMS System | Text | ServiceNow |

**Alert Threshold Fields:**

| Cell | Field | Type | Default |
|------|-------|------|---------|
| B17 | Upcoming Warning (days) | Number | 30 |
| B18 | Due Soon Alert (days) | Number | 14 |
| B19 | Critical Escalation (days overdue) | Number | 7 |
| B20 | Tier 1 Escalation (days overdue) | Number | 3 |

### Sheet 2: Equipment Schedule

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Equipment ID | Text | 15 | None |
| B | Equipment Type | Dropdown | 18 | Server, Network Device, Storage, UPS, HVAC, Generator, Security System, Fire Suppression, Access Control, CCTV, Environmental Sensors, PDU, Cable Infrastructure, Other |
| C | Equipment Description | Text | 35 | None |
| D | Location | Text | 25 | None |
| E | Criticality | Dropdown | 18 | Tier 1 - Critical, Tier 2 - Standard, Tier 3 - Low |
| F | Maintenance Type | Dropdown | 20 | Firmware Update, Inspection, Battery Check, Filter Replacement, Calibration, Full Service, Cleaning, Testing, Component Replacement |
| G | Frequency | Dropdown | 15 | Weekly, Monthly, Quarterly, Semi-annually, Annually, Bi-annually |
| H | Responsible Party | Dropdown | 20 | Internal - IT, Internal - Facilities, Vendor, Manufacturer, Contractor |
| I | Last Completed | Date | 15 | Date |
| J | Next Due | Formula | 15 | =I2+VLOOKUP(G2,FrequencyTable,2,FALSE) |
| K | Status | Formula | 15 | See formula below |
| L | Days Until/Overdue | Formula | 15 | =J2-TODAY() |
| M | Maintenance Record Ref | Text | 20 | None |
| N | Warranty Status | Dropdown | 18 | In Warranty, Out of Warranty, Extended Warranty, N/A |
| O | Contract Reference | Text | 15 | None |
| P | Notes | Text | 40 | None |

**Frequency Lookup Table (Named Range: FrequencyTable):**

| Frequency | Days |
|-----------|------|
| Weekly | 7 |
| Monthly | 30 |
| Quarterly | 90 |
| Semi-annually | 180 |
| Annually | 365 |
| Bi-annually | 730 |

**Status Formula (Column K):**

```excel
=IF(J2="","",IF(J2>TODAY()+$B$17,"Current",IF(J2>TODAY(),"Due Soon","Overdue")))
```

**Where $B$17 is the Upcoming Warning threshold from Sheet 1**

**Conditional Formatting Rules (Column K):**

| Value | Background | Font |
|-------|------------|------|
| Current | #C6EFCE (Green) | Black |
| Due Soon | #FFEB9C (Amber) | Black |
| Overdue | #FFC7CE (Red) | Dark Red |

### Sheet 3: Overdue Tracking

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Equipment ID | Text | 15 | None |
| B | Equipment Description | Text | 30 | None |
| C | Criticality | Dropdown | 18 | Tier 1 - Critical, Tier 2 - Standard, Tier 3 - Low |
| D | Maintenance Type | Text | 20 | None |
| E | Original Due Date | Date | 15 | Date |
| F | Days Overdue | Formula | 12 | =TODAY()-E2 |
| G | Reason for Delay | Dropdown | 22 | Parts on Order, Vendor Scheduling, Resource Unavailable, Budget Hold, Awaiting Change Window, Equipment Access Issue, Dependency on Other Work, Other |
| H | Detailed Explanation | Text | 40 | None |
| I | Estimated Completion | Date | 15 | Date |
| J | Escalated | Dropdown | 10 | Yes, No |
| K | Escalated To | Text | 20 | None |
| L | Escalation Date | Date | 15 | Date |
| M | Compensating Control | Text | 35 | None |
| N | Risk Assessment | Dropdown | 12 | Low, Medium, High, Critical |
| O | Resolution Notes | Text | 40 | None |
| P | Actual Completion Date | Date | 15 | Date |

**Conditional Formatting (Column F - Days Overdue):**

| Days | Background |
|------|------------|
| 1-7 | #FFE4B5 (Light Orange) |
| 8-14 | #FFA500 (Orange) |
| 15-30 | #FFC7CE (Light Red) |
| >30 | #FF0000 (Red) |

**Conditional Formatting (Row - if Criticality = "Tier 1 - Critical" AND Escalated = "No" AND Days Overdue > 3):**
- Red border around entire row

### Sheet 4: Upcoming Maintenance

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Equipment ID | Text | 15 | None |
| B | Equipment Description | Text | 30 | None |
| C | Criticality | Text | 18 | None |
| D | Maintenance Type | Text | 20 | None |
| E | Due Date | Date | 15 | None |
| F | Days Until Due | Formula | 12 | =E2-TODAY() |
| G | Time Category | Formula | 15 | See formula |
| H | Scheduled Date | Date | 15 | Date |
| I | Assigned To | Text | 20 | None |
| J | Parts Required | Text | 30 | None |
| K | Vendor Booked | Dropdown | 12 | Yes, No, N/A |
| L | Change Request | Text | 15 | None |
| M | Maintenance Window | Text | 20 | None |
| N | Notes | Text | 35 | None |

**Time Category Formula (Column G):**

```excel
=IF(F2<=7,"1-Next 7 Days",IF(F2<=14,"2-8-14 Days",IF(F2<=30,"3-15-30 Days",IF(F2<=60,"4-31-60 Days","5-61-90 Days"))))
```

**Conditional Formatting (Column G):**

| Category | Background |
|----------|------------|
| 1-Next 7 Days | #FFC7CE (Light Red) |
| 2-8-14 Days | #FFE4B5 (Light Orange) |
| 3-15-30 Days | #FFEB9C (Light Amber) |
| 4-31-60 Days | #FFFFCC (Light Yellow) |
| 5-61-90 Days | #C6EFCE (Light Green) |

### Sheet 5: Dashboard

**Purpose:** Summary metrics and compliance status

**Layout:**

| Row Range | Content |
|-----------|---------|
| 1-5 | Title and report period |
| 7-18 | Overall compliance metrics |
| 20-35 | Compliance by type |
| 37-45 | Compliance by criticality |
| 47-60 | Overdue summary |
| 62-75 | Trend data (6 months) |
| 77-90 | Upcoming workload |

**Metrics Formulas:**

**Total Equipment:**
```excel
=COUNTA('Equipment Schedule'!A:A)-1
```

**Equipment Current (%):**
```excel
=COUNTIF('Equipment Schedule'!K:K,"Current")/B8*100
```

**Equipment Due Soon (%):**
```excel
=COUNTIF('Equipment Schedule'!K:K,"Due Soon")/B8*100
```

**Equipment Overdue:**
```excel
=COUNTIF('Equipment Schedule'!K:K,"Overdue")
```

**Critical Equipment Overdue:**
```excel
=COUNTIFS('Equipment Schedule'!K:K,"Overdue",'Equipment Schedule'!E:E,"Tier 1 - Critical")
```

**Average Days Overdue (for overdue items):**
```excel
=AVERAGEIF('Equipment Schedule'!K:K,"Overdue",'Equipment Schedule'!L:L)*-1
```

**Longest Overdue (days):**
```excel
=MIN('Equipment Schedule'!L:L)*-1
```

**Compliance by Type formulas:**

```excel
=COUNTIFS('Equipment Schedule'!B:B,"Server",'Equipment Schedule'!K:K,"Current")/COUNTIF('Equipment Schedule'!B:B,"Server")*100
```

**Compliance by Criticality formulas:**

```excel
=COUNTIFS('Equipment Schedule'!E:E,"Tier 1 - Critical",'Equipment Schedule'!K:K,"Current")/COUNTIF('Equipment Schedule'!E:E,"Tier 1 - Critical")*100
```

### Sheet 6: Maintenance Log

**Columns:**

| Col | Field Name | Type | Width |
|-----|------------|------|-------|
| A | Log ID | Auto-increment | 10 |
| B | Equipment ID | Text | 15 |
| C | Equipment Description | Text | 30 |
| D | Maintenance Type | Text | 20 |
| E | Scheduled Date | Date | 15 |
| F | Actual Completion Date | Date | 15 |
| G | Variance (Days) | Formula | 12 |
| H | Performed By | Text | 20 |
| I | Ticket Reference | Text | 15 |
| J | Findings/Notes | Text | 40 |
| K | Parts Replaced | Text | 25 |
| L | Cost (CHF) | Number | 12 |
| M | Follow-up Required | Dropdown | 12 |
| N | Follow-up Action | Text | 35 |
| O | Next Scheduled | Date | 15 |

**Variance Formula (Column G):**
```excel
=F2-E2
```

**Conditional Formatting (Column G - Variance):**

| Variance | Background |
|----------|------------|
| <0 (Early) | #C6EFCE (Light Green) |
| 0 (On Time) | White |
| 1-7 (Late) | #FFEB9C (Light Amber) |
| >7 (Very Late) | #FFC7CE (Light Red) |

### Sheet 7: Evidence Register

**Columns:**

| Col | Field Name | Type | Width |
|-----|------------|------|-------|
| A | Evidence ID | Text | 12 |
| B | Equipment ID | Text | 15 |
| C | Maintenance Date | Date | 15 |
| D | Evidence Type | Dropdown | 20 |
| E | Document Reference | Text | 30 |
| F | Storage Location | Text | 35 |
| G | File Path/URL | Text | 50 |
| H | Retention Period | Dropdown | 15 |
| I | Expiry Date | Formula | 15 |
| J | Last Verified | Date | 15 |
| K | Verified By | Text | 20 |
| L | Status | Dropdown | 12 |
| M | Notes | Text | 30 |

**Evidence Type Dropdown:**
- Maintenance Ticket
- Vendor Service Report
- Test Report
- Inspection Certificate
- Calibration Certificate
- Firmware Confirmation
- Photograph
- Sign-off Form
- Other

**Retention Period Dropdown:**
- 1 Year
- 3 Years
- 5 Years
- 7 Years
- Contract Term +3

**Expiry Date Formula:**
```excel
=IF(H2="1 Year",C2+365,IF(H2="3 Years",C2+1095,IF(H2="5 Years",C2+1825,IF(H2="7 Years",C2+2555,""))))
```

**Status Dropdown:**
- Active
- Archived
- Expired
- Missing

---

## Cell Styling Reference

### Colour Palette

- Primary Header: #003366 (Navy blue)
- Section Header: #4472C4 (Medium blue)
- Column Header: #D9D9D9 (Light grey)
- Input Cell: #FFFFCC (Light yellow)
- Formula Cell: #E6E6E6 (Very light grey)

### Status Colours

- Current: #C6EFCE (Light green)
- Due Soon: #FFEB9C (Light amber)
- Overdue: #FFC7CE (Light red)

### Priority Colours

- Critical: #FFC7CE (Light red)
- High: #FFE4B5 (Light orange)
- Medium: #FFEB9C (Light amber)
- Low: #FFFFCC (Light yellow)

### Font Standards

- Title: Calibri 16pt Bold
- Section Header: Calibri 14pt Bold
- Column Header: Calibri 11pt Bold
- Data: Calibri 11pt Regular
- Notes: Calibri 10pt Regular

---

## Formula Reference

### Named Ranges

| Name | Range | Purpose |
|------|-------|---------|
| FrequencyTable | Lookup!A2:B8 | Frequency to days conversion |
| UpcomingThreshold | Instructions!B17 | Days for upcoming warning |
| CriticalThreshold | Instructions!B20 | Days for Tier 1 escalation |
| EquipmentList | 'Equipment Schedule'!A:A | Equipment IDs |
| StatusList | 'Equipment Schedule'!K:K | Status values |

### Key Formulas

**Next Due Date:**
```excel
=IF(I2="","",I2+VLOOKUP(G2,FrequencyTable,2,FALSE))
```

**Status Determination:**
```excel
=IF(J2="","",IF(J2>TODAY()+UpcomingThreshold,"Current",IF(J2>TODAY(),"Due Soon","Overdue")))
```

**Days Calculation:**
```excel
=IF(J2="","",J2-TODAY())
```

**Compliance Percentage:**
```excel
=IFERROR(COUNTIF(StatusList,"Current")/COUNTA(EquipmentList)*100,0)
```

---

## Validation Rules

### Data Validation Settings

**Equipment ID (Column A):**
- No duplicates allowed
- Text length: 5-20 characters

**Date Fields:**
- Format: DD.MM.YYYY (Swiss)
- Future dates allowed for scheduled/estimated
- Past dates required for completed

**Dropdown Fields:**
- Source: Named range or list
- Error alert: Show error on invalid entry

### Error Handling

**Blank Dependencies:**
- If Last Completed blank, Next Due shows blank
- If Status blank, Days Until/Overdue shows blank

**Division Errors:**
- Dashboard percentages use IFERROR to handle division by zero

---

## Integration Points

### Integration with S2 (Equipment Maintenance)

- Equipment list should align with S2 equipment inventory
- Manufacturer frequencies from S2 populate S3 schedules
- S2 assessment informs maintenance programme scope

### Integration with S4 (Dashboard)

- S4 pulls compliance metrics from S3 Dashboard
- Overall maintenance compliance score feeds S4
- Overdue counts and critical items link to S4

### Integration with CMMS/ITSM

- Export equipment from CMMS for initial population
- Reconcile completion status with maintenance tickets
- Link maintenance records to ticket references
- Sync scheduled dates with CMMS calendar

### Integration with Change Management

- Maintenance windows align with change calendar
- Change requests required for system-impacting maintenance
- Change closure triggers maintenance completion

---

## Conditional Formatting Logic

### Status Column Formatting (Column K)

**Rule Configuration:**

| Rule Order | Condition | Format Applied |
|------------|-----------|----------------|
| 1 | Cell value = "Overdue" | Background: #FFC7CE (Light red), Font: #9C0006 (Dark red) |
| 2 | Cell value = "Due Soon" | Background: #FFEB9C (Light amber), Font: #9C6500 (Dark amber) |
| 3 | Cell value = "Current" | Background: #C6EFCE (Light green), Font: #006100 (Dark green) |

**Application Range:** K2:K201 (all data rows)

### Days Until/Overdue Formatting (Column L)

**Rule Configuration:**

| Rule Order | Condition | Format Applied |
|------------|-----------|----------------|
| 1 | Cell value < -14 | Background: #FF0000 (Red), Font: White, Bold |
| 2 | Cell value < -7 | Background: #FFC7CE (Light red), Font: Dark red |
| 3 | Cell value < 0 | Background: #FFE4B5 (Light orange), Font: Black |
| 4 | Cell value <= 7 | Background: #FFEB9C (Light amber), Font: Black |
| 5 | Cell value <= 30 | Background: #FFFFCC (Light yellow), Font: Black |
| 6 | Cell value > 30 | Background: #C6EFCE (Light green), Font: Black |

**Application Range:** L2:L201

### Criticality Row Highlighting

**Rule for Tier 1 Critical Equipment:**

```
Formula: =AND($E2="Tier 1 - Critical",$K2="Overdue")
Format: Bold font, Red border around row
```

**Rule for Tier 1 Overdue Without Escalation (Sheet 3):**

```
Formula: =AND($C2="Tier 1 - Critical",$J2="No",$F2>3)
Format: Red border, Bold text, Background: #FFC7CE
```

### Overdue Tracking Conditional Formats (Sheet 3)

**Days Overdue Column (F):**

| Days | Background Colour |
|------|-------------------|
| 1-3 | #FFFFCC (Light yellow) |
| 4-7 | #FFE4B5 (Light orange) |
| 8-14 | #FFA500 (Orange) |
| 15-30 | #FFC7CE (Light red) |
| >30 | #FF0000 (Red) with white text |

### Upcoming Maintenance Time Category (Sheet 4, Column G)

| Category | Background |
|----------|------------|
| 1-Next 7 Days | #FFC7CE (Light red) |
| 2-8-14 Days | #FFE4B5 (Light orange) |
| 3-15-30 Days | #FFEB9C (Light amber) |
| 4-31-60 Days | #FFFFCC (Light yellow) |
| 5-61-90 Days | #C6EFCE (Light green) |

---

## Validation Rule Details

### Equipment ID Validation (Column A)

**Validation Settings:**

```
Type: Custom
Formula: =AND(LEN(A2)>=5,LEN(A2)<=25,COUNTIF($A$2:$A$201,A2)=1)
Error Title: Invalid Equipment ID
Error Message: Equipment ID must be 5-25 characters and unique within the workbook.
```

### Date Field Validation

**Last Completed (Column I):**

```
Type: Date
Operator: Less than or equal to
Formula: =TODAY()
Error Title: Invalid Date
Error Message: Last Completed date cannot be in the future.
```

**Next Due (Column J):**

```
Type: Date
Operator: Greater than
Formula: =I2
Error Title: Invalid Date
Error Message: Next Due date must be after Last Completed date.
```

### Dropdown Validation Sources

**Equipment Type (Column B):**

```
Source: "Server,Network Device,Storage,UPS,HVAC,Generator,Security System,Fire Suppression,Access Control,CCTV,Environmental Sensors,PDU,Cable Infrastructure,Other"
Allow blank: No
Show input message: Yes
Input message: Select the equipment category from the list.
```

**Criticality (Column E):**

```
Source: "Tier 1 - Critical,Tier 2 - Standard,Tier 3 - Low"
Allow blank: No
Show input message: Yes
Input message: Select criticality based on business impact assessment.
```

**Frequency (Column G):**

```
Source: "Weekly,Monthly,Quarterly,Semi-annually,Annually,Bi-annually"
Allow blank: No
Show input message: Yes
Input message: Select maintenance frequency per manufacturer recommendation.
```

---

## Advanced Formula Reference

### Compliance Percentage Calculations (Dashboard)

**Overall Schedule Compliance:**

```excel
=IFERROR(COUNTIF('Equipment Schedule'!K:K,"Current")/(COUNTA('Equipment Schedule'!A:A)-1)*100,0)
```

**Compliance by Equipment Type:**

```excel
=IFERROR(COUNTIFS('Equipment Schedule'!B:B,"Server",'Equipment Schedule'!K:K,"Current")/COUNTIF('Equipment Schedule'!B:B,"Server")*100,0)
```

**Compliance by Criticality:**

```excel
=IFERROR(COUNTIFS('Equipment Schedule'!E:E,"Tier 1 - Critical",'Equipment Schedule'!K:K,"Current")/COUNTIF('Equipment Schedule'!E:E,"Tier 1 - Critical")*100,0)
```

### Overdue Analysis Formulas

**Total Overdue Count:**

```excel
=COUNTIF('Equipment Schedule'!K:K,"Overdue")
```

**Critical Equipment Overdue:**

```excel
=COUNTIFS('Equipment Schedule'!E:E,"Tier 1 - Critical",'Equipment Schedule'!K:K,"Overdue")
```

**Average Days Overdue:**

```excel
=IFERROR(ABS(AVERAGEIF('Equipment Schedule'!L:L,"<0",'Equipment Schedule'!L:L)),0)
```

**Maximum Days Overdue:**

```excel
=IFERROR(ABS(MIN('Equipment Schedule'!L:L)),0)
```

### Upcoming Workload Formulas

**Next 7 Days:**

```excel
=COUNTIFS('Equipment Schedule'!L:L,">=0",'Equipment Schedule'!L:L,"<=7")
```

**8-14 Days:**

```excel
=COUNTIFS('Equipment Schedule'!L:L,">7",'Equipment Schedule'!L:L,"<=14")
```

**15-30 Days:**

```excel
=COUNTIFS('Equipment Schedule'!L:L,">14",'Equipment Schedule'!L:L,"<=30")
```

### Trend Calculation Formulas

**Month-over-Month Change:**

```excel
=B3-B2
```
Where B3 is current month compliance and B2 is previous month.

**Rolling Average (3-month):**

```excel
=AVERAGE(B2:B4)
```

**Compliance Trend Direction:**

```excel
=IF(B3>B2,"↑ Improving",IF(B3<B2,"↓ Declining","→ Stable"))
```

---

## Error Handling and Edge Cases

### Handling Blank Cells

**Next Due Date Calculation:**

```excel
=IF(OR(I2="",G2=""),"",I2+VLOOKUP(G2,FrequencyTable,2,FALSE))
```
Returns blank if either Last Completed or Frequency is empty.

**Status Determination:**

```excel
=IF(J2="","",IF(J2>TODAY()+UpcomingThreshold,"Current",IF(J2>TODAY(),"Due Soon","Overdue")))
```
Returns blank if Next Due is empty.

### Division by Zero Prevention

**Percentage Calculations:**

```excel
=IFERROR(COUNTIF(range,"Current")/COUNTA(range)*100,0)
```
Returns 0 if division would fail.

### Circular Reference Prevention

Avoid referencing cells that reference back:
- Status (K) should not reference Dashboard metrics
- Days Until (L) references only Next Due (J) and TODAY()
- Compliance percentages calculated independently of source data formulas

### Large Dataset Performance

**For workbooks exceeding 500 equipment items:**

1. Consider splitting into multiple workbooks by location/type
2. Use SUMPRODUCT instead of COUNTIFS for large ranges
3. Disable automatic calculation during bulk updates
4. Use helper columns to pre-calculate intermediate values

---

**END OF SPECIFICATION**

---

*"An ounce of prevention is worth a pound of cure."*
— Benjamin Franklin

<!-- QA_VERIFIED: 2026-02-06 -->
