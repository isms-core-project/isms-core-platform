**ISMS-IMP-A.7.4-5-11-S1-TG - Physical Monitoring Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.4: Physical Security Monitoring

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.4-5-11-S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Physical Security Monitoring - Access Control, CCTV, Intrusion Detection |
| **Related Policy** | ISMS-POL-A.7.4-5-11, Section 2 (Physical Security Monitoring) |
| **Purpose** | Document deployed physical security monitoring systems, assess capabilities against policy requirements, and identify gaps |
| **Target Audience** | Security Operations, Facilities Management, IT Operations, Security Engineers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Physical Monitoring assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.4-5-11-S1-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.4.1_Access_Monitoring_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a74_1_access_monitoring.py)

**Sheet Count:** 8 worksheets

**Data Capacity:** 100 data rows per assessment sheet (Sheets 2-5)

**Styling:** Navy blue headers, yellow input cells, conditional formatting for compliance status (green/amber/red)

### Sheet Organization

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Assessment metadata and status legend | Read-only Reference | ~30 rows |
| 2 | Access Control | Access control system inventory and compliance | Data Entry | 100 data rows |
| 3 | CCTV | CCTV system inventory and coverage assessment | Data Entry | 100 data rows |
| 4 | Intrusion Detection | Intrusion detection system inventory and testing | Data Entry | 100 data rows |
| 5 | Incidents | Physical security incident log (last 12 months) | Data Entry | 100 data rows |
| 6 | Summary Dashboard | Automated compliance scoring and metrics | Formula-driven | ~40 rows |
| 7 | Evidence Register | Supporting evidence documentation | Data Entry | 100 data rows |
| 8 | Approval Sign-Off | Four-level approval workflow | Data Entry | ~20 rows |

### Workbook Features

**Data Validation:**

- Dropdown lists for standardized input (Yes/No, Compliant/Partial/Non-Compliant, etc.)
- Date validation (valid date format)
- Numeric validation (retention days, camera count, etc.)

**Conditional Formatting:**

- Compliance Status columns: Green fill (✅ Compliant), Amber fill (⚠️ Partial), Red fill (❌ Non-Compliant)
- Summary Dashboard scores: Color-coded thresholds (>90% green, 75-89% amber, 60-74% amber, <60% red)
- Overdue dates highlighted (testing overdue, access review overdue)

**Formulas:**

- Summary Dashboard auto-calculates from Sheets 2-5
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
- Text: "ISMS-IMP-A.7.4.1 - Physical Access Monitoring Assessment\nISO/IEC 27001:2022 - Control A.7.4: Physical Security Monitoring"
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

### Sheet 2: Access Control

**Purpose:** Document all access control systems and assess compliance against policy requirements

**Header Row (Row 3):**

- Style: Gray background, bold text, center-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility or building name |
| B | Access Control System | Text | 30 | None | No | Vendor and model (HID, Lenel, Verkada, etc.) |
| C | Controller Count | Number | 12 | Integer >0 | No | Number of access control panels/controllers |
| D | Reader Count | Number | 12 | Integer >0 | No | Number of badge readers (doors) |
| E | Badge Technology | Text | 25 | None | No | Reader technology (HID Prox, iCLASS, Mobile, Biometric) |
| F | User Count | Number | 12 | Integer >0 | No | Total users in system |
| G | Access Levels Defined | Number | 12 | Integer >0 | No | Number of access levels configured |
| H | HR Integration | Dropdown | 18 | List | No | Yes - Automated / Partial - Manual / No |
| I | SIEM Integration | Dropdown | 18 | List | No | Yes - Real-time / Partial - Batch / No |
| J | Anti-Passback | Dropdown | 15 | List | No | Yes / No / N/A |
| K | Access Log Retention (Days) | Number | 15 | Integer >0 | No | Days of logs retained |
| L | Last Access Review | Date | 15 | Date | No | Date of last quarterly access review |
| M | Compliance Status | Formula | 18 | None | Yes | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant |
| N | Notes | Text | 50 | None | No | Additional context, gaps, remediation plans |

**Compliance Status Formula (Column M):**
```excel
=IF(AND(H2="Yes - Automated", I2="Yes - Real-time", K2>=90, (TODAY()-L2)<=90), "✅ Compliant",
   IF(OR(H2="No", I2="No", K2<30, (TODAY()-L2)>180), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**

- ✅ Compliant IF: HR integration automated AND SIEM integration real-time AND retention ≥90 days AND access review within 90 days
- ❌ Non-Compliant IF: HR integration "No" OR SIEM integration "No" OR retention <30 days OR access review >180 days overdue
- ⚠️ Partial: Everything else (meets some but not all requirements)

**Conditional Formatting:**

- Column M: Green background if "✅ Compliant", Amber if "⚠️ Partial", Red if "❌ Non-Compliant"

**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (facility name)

### Sheet 3: CCTV

**Purpose:** Document all CCTV systems and assess coverage and retention compliance

**Header Row (Row 3):**

- Style: Gray background, bold text, center-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility or NVR/VMS name |
| B | NVR/VMS System | Text | 30 | None | No | Vendor and model (Milestone, Genetec, Verkada, etc.) |
| C | Camera Count | Number | 12 | Integer >0 | No | Total cameras on this NVR/VMS |
| D | Camera Types | Text | 25 | None | No | Fixed, PTZ, Fisheye, Mix |
| E | Resolution | Text | 15 | None | No | 720p, 1080p, 4K, Mix |
| F | Recording Mode | Dropdown | 18 | List | No | Continuous 24/7 / Motion-triggered / Scheduled / Mix |
| G | Retention Period (Days) | Number | 15 | Integer >0 | No | Days of footage retained |
| H | Storage Capacity (TB) | Number | 15 | Float >0 | No | Total storage capacity |
| I | Storage Utilization (%) | Number | 15 | Integer 0-100 | No | Current storage usage percentage |
| J | Coverage Areas | Text | 30 | None | No | Areas covered (entrances, server rooms, parking, etc.) |
| K | Blind Spots | Text | 30 | None | No | Areas not covered but should be |
| L | Low-Light Capable | Dropdown | 18 | List | No | Yes - IR / Yes - Low-light sensor / No |
| M | Redundant Storage | Dropdown | 18 | List | No | Yes - RAID / Yes - Cloud backup / No |
| N | Compliance Status | Formula | 18 | None | Yes | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant |
| O | Notes | Text | 50 | None | No | Additional context, gaps, remediation plans |

**Compliance Status Formula (Column N):**
```excel
=IF(AND(G2>=30, I2<90, K2="None identified", L2<>"No"), "✅ Compliant",
   IF(OR(G2<14, I2>95, ISNUMBER(SEARCH("no coverage",K2))), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**

- ✅ Compliant IF: Retention ≥30 days AND storage utilization <90% AND no blind spots AND low-light capable
- ❌ Non-Compliant IF: Retention <14 days OR storage utilization >95% OR critical area no coverage
- ⚠️ Partial: Everything else

**Conditional Formatting:**

- Column N: Green background if "✅ Compliant", Amber if "⚠️ Partial", Red if "❌ Non-Compliant"
- Column I: Red background if >90% (storage critically full)

**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (facility name)

### Sheet 4: Intrusion Detection

**Purpose:** Document all intrusion detection systems and assess coverage, arming, and testing compliance

**Header Row (Row 3):**

- Style: Gray background, bold text, center-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility or alarm panel name |
| B | Alarm Panel System | Text | 30 | None | No | Vendor and model (Honeywell, DSC, Bosch, etc.) |
| C | Sensor Count | Number | 12 | Integer >0 | No | Total sensors (motion, door/window, glass break) |
| D | Sensor Types | Text | 30 | None | No | Breakdown by type (Motion: 15, Door/Window: 30, etc.) |
| E | Zone Count | Number | 12 | Integer >0 | No | Number of arming zones |
| F | Coverage Areas | Text | 30 | None | No | Areas protected (perimeter, server rooms, etc.) |
| G | Arming Schedule | Text | 25 | None | No | 24/7, After hours, Manual |
| H | Monitoring Service | Dropdown | 25 | List | No | Yes - Professional / Yes - Self (SOC) / No |
| I | Backup Communication | Dropdown | 20 | List | No | Yes - Cellular / Yes - Dual path / No |
| J | False Alarm Rate (/month) | Number | 15 | Integer ≥0 | No | Average false alarms per month |
| K | Last Testing Date | Date | 15 | Date | No | Date of last monthly testing |
| L | Compliance Status | Formula | 18 | None | Yes | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant |
| M | Notes | Text | 50 | None | No | Additional context, gaps, remediation plans |

**Compliance Status Formula (Column L):**
```excel
=IF(AND(H2<>"No", J2<=5, (TODAY()-K2)<=31), "✅ Compliant",
   IF(OR(H2="No", J2>10, (TODAY()-K2)>60), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**

- ✅ Compliant IF: Monitoring service active AND false alarm rate ≤5/month AND testing within 31 days
- ❌ Non-Compliant IF: No monitoring service OR false alarm rate >10/month OR testing >60 days overdue
- ⚠️ Partial: Everything else

**Conditional Formatting:**

- Column L: Green background if "✅ Compliant", Amber if "⚠️ Partial", Red if "❌ Non-Compliant"
- Column J: Red background if >10 (excessive false alarms)
- Column K: Red background if (TODAY()-K2)>31 (testing overdue)

**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (facility name)

### Sheet 5: Incidents

**Purpose:** Log all physical security incidents from last 12 months for trend analysis and response time tracking

**Header Row (Row 3):**

- Style: Gray background, bold text, center-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Incident ID | Text | 18 | None | No | Unique incident identifier |
| B | Incident Date | Date | 15 | Date | No | Date incident occurred |
| C | Incident Type | Dropdown | 20 | List | No | Unauthorized Access / Intrusion Alarm / Tailgating / Lost Badge / System Failure / Other |
| D | Facility/Location | Text | 25 | None | No | Where incident occurred |
| E | Severity | Dropdown | 12 | List | No | Critical / High / Medium / Low |
| F | Description | Text | 40 | None | No | Brief incident description |
| G | Detection Method | Text | 25 | None | No | How detected (Access control alarm, CCTV, Guard patrol, etc.) |
| H | Response Time (Min) | Number | 15 | Integer ≥0 | No | Minutes from detection to response |
| I | Resolution Status | Dropdown | 15 | List | No | Resolved / In Progress / Escalated |
| J | Root Cause | Text | 30 | None | No | Identified cause |
| K | Corrective Action | Text | 40 | None | No | Actions taken to prevent recurrence |
| L | Notes | Text | 50 | None | No | Additional context |

**Conditional Formatting:**

- Column E: Red background if "Critical", Orange if "High", Yellow if "Medium", White if "Low"
- Column H: Red background if >15 minutes (response time target exceeded for standard facilities)

**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (incident ID)

**Summary Metrics (Auto-calculated in Sheet 6):**

- Total incidents (last 12 months)
- Critical/High incident count
- Average response time
- Most common incident types
- Facilities with highest incident count

### Sheet 6: Summary Dashboard

**Purpose:** Automated compliance scoring and key performance indicators

**Structure:** Dashboard layout with metrics and charts

**Row 1:** Header

- Merged cells A1:H1
- Text: "Physical Security Monitoring - Summary Dashboard"
- Style: Navy blue background, white bold text, 14pt, center-aligned

**Rows 3-10:** Overall Compliance Score

- Row 3: "Overall Compliance Score" label
- Row 4: Formula calculating aggregate score from Sheets 2-4
- Row 5: Color-coded status (Green >90%, Amber 75-89%, Amber 60-74%, Red <60%)

**Overall Compliance Score Formula:**
```excel
=(COUNTIF('Access Control'!M:M,"✅ Compliant")/COUNTA('Access Control'!M:M)*0.4 +
  COUNTIF(CCTV!N:N,"✅ Compliant")/COUNTA(CCTV!N:N)*0.3 +
  COUNTIF('Intrusion Detection'!L:L,"✅ Compliant")/COUNTA('Intrusion Detection'!L:L)*0.3)*100
```

**Weighting:** Access Control 40%, CCTV 30%, Intrusion Detection 30%

**Rows 12-20:** Domain Scores

- Access Control Compliance Score (%)
- CCTV Compliance Score (%)
- Intrusion Detection Compliance Score (%)
- Each with formula, percentage display, color-coding

**Rows 22-30:** Incident Metrics

- Total Incidents (last 12 months): `=COUNTA(Incidents!A:A)-1`
- Critical/High Incidents: `=COUNTIF(Incidents!E:E,"Critical")+COUNTIF(Incidents!E:E,"High")`
- Average Response Time (min): `=AVERAGE(Incidents!H:H)`
- Response Time Compliance (%): `=COUNTIF(Incidents!H:H,"<=15")/COUNTA(Incidents!H:H)*100`

**Rows 32-50:** Gap Summary

- Auto-generated list of non-compliant items
- Formula scans Sheets 2-4 for "❌ Non-Compliant" status
- Lists facility name, system type, gap description
- Prioritized by severity (Critical → High → Medium → Low)

**Gap Summary Formula (example for row 32):**
```excel
=IF(COUNTIF('Access Control'!M:M,"❌ Non-Compliant")>0,
   INDEX('Access Control'!A:A, MATCH("❌ Non-Compliant",'Access Control'!M:M,0)) & " - Access Control Gap",
   IF(COUNTIF(CCTV!N:N,"❌ Non-Compliant")>0,
      INDEX(CCTV!A:A, MATCH("❌ Non-Compliant",CCTV!N:N,0)) & " - CCTV Gap",
      "No Critical Gaps Identified"))
```

**Charts:**

- Chart 1: Overall Compliance Score (gauge chart)
- Chart 2: Domain Scores (bar chart - Access Control, CCTV, Intrusion Detection)
- Chart 3: Incident Trend (line chart - incidents per month, last 12 months)
- Chart 4: Incident Severity Distribution (pie chart - Critical, High, Medium, Low)

**Conditional Formatting:**

- Compliance scores: Green >90%, Amber 75-89%, Red <60%
- Gap summary: Red highlight for critical gaps, amber for high/medium gaps

### Sheet 7: Evidence Register

**Purpose:** Document all supporting evidence with audit traceability

**Header Row (Row 3):**

- Style: Gray background, bold text, center-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Evidence ID | Text | 12 | None | No | Unique identifier (EVID-001, EVID-002, etc.) |
| B | Evidence Type | Dropdown | 18 | List | No | Screenshot / Config Export / Log Sample / Report / Document / Photo |
| C | Description | Text | 40 | None | No | What evidence shows |
| D | Related Sheet/Item | Text | 25 | None | No | Links to specific assessment row (Sheet 2, Row 5) |
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

### Sheet 8: Approval Sign-Off

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
| Level 2 | Security Operations Manager | [Input] | [Input] | [Input] | [Input] |
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
- Applied to: All data table cells (Sheets 2-5, 7)

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

- Summary Dashboard (Sheet 6): All cells except approval override
- Compliance Status columns (Sheets 2-5): Formula-protected
- Header rows (Row 1-3 all sheets): Protected

**Unlocked Cells (Input cells):**

- All yellow background cells (user input required)
- Evidence Register (Sheet 7): All data cells
- Approval Sign-Off (Sheet 8): Name, Date, Signature, Comments cells

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
| Section 2.1: Access Control and Monitoring | ISMS-POL-A.7.4-5-11, §2.1 | Sheet 2: Access Control | Badge readers, access levels, HR/SIEM integration, log retention, access review |
| Section 2.3: Video Surveillance (CCTV) | ISMS-POL-A.7.4-5-11, §2.3 | Sheet 3: CCTV | Camera coverage, recording capabilities, retention, storage capacity, blind spots |
| Section 2.2: Physical Intrusion Detection | ISMS-POL-A.7.4-5-11, §2.2 | Sheet 4: Intrusion Detection | Sensors, alarm panels, arming schedules, monitoring service, false alarms, testing |
| Section 2.4: Security Personnel | ISMS-POL-A.7.4-5-11, §2.4 | Sheet 5: Incidents | Security guard logs reflected in incident documentation |
| Section 2.5: Integration | ISMS-POL-A.7.4-5-11, §2.5 | Sheets 2-4: Integration columns | SIEM integration, dashboard deployments, alerting configurations |
| Section 5.4: Incident Response | ISMS-POL-A.7.4-5-11, §5.4 | Sheet 5: Incidents | Incident classification, response times, resolution status |

**Assessment validates policy compliance by comparing deployed systems against policy requirements:**

- Policy states "SIEM integration SHALL be implemented" → Assessment verifies "Yes - Real-time" in Sheet 2, Column I
- Policy states "Retention 90 days minimum (Tier 1)" → Assessment verifies ≥90 days in Sheet 2, Column K
- Policy states "Response time <5 min (Tier 1)" → Assessment tracks actual response times in Sheet 5, Column H

### Integration with Other Assessments

**Feeds into:**

- ISMS-IMP-A.7.4-5-11-S4 (Compliance Dashboard): Overall compliance score, gap summary, incident metrics
- SIEM assessment (if separate): Physical security log integration status verified
- BC/DR assessment: Physical security incident data informs business continuity scenarios

**Dependencies from:**

- Facility inventory: List of all facilities requiring assessment (if master facility list exists)
- Network inventory: Network infrastructure supporting physical security systems (access control network, CCTV network)
- HR system inventory: Confirms HR system integration feasibility

**Shared evidence with:**

- Access Control assessment (if separate from physical monitoring): Badge reader deployments, access control logs
- Network security assessment: Network diagrams showing security system VLANs
- Incident management assessment: Physical security incidents cross-referenced

### Integration with Evidence Collection

**Evidence Register (Sheet 7) cross-references Assessment Sheets:**

- Evidence ID "EVID-005" → Related Sheet/Item: "Sheet 2, Row 5 (Building A Access Control)"
- File Name: "BuildingA_AccessControl_Config_20260115.png"
- Assessment Sheet 2, Row 5, Column N (Notes): "Evidence: EVID-005"

**Evidence Traceability:**
```
Assessment Finding (Sheet 2, Row 5) ← Evidence (EVID-005) ← Evidence File (BuildingA_AccessControl_Config_20260115.png)
```

**Audit Flow:**
1. Auditor reviews Sheet 2 (Access Control), identifies non-compliant item
2. Auditor checks Sheet 7 (Evidence Register) for supporting evidence ID
3. Auditor requests evidence file from File Location
4. Evidence file verifies or refutes assessment finding

### Integration with Audit Process

**Audit Deliverables:**
1. **Assessment Workbook:** ISMS-IMP-A.7.4.1_Access_Monitoring_YYYYMMDD_FINAL.xlsx (all sheets)
2. **Evidence Folder:** All files listed in Sheet 7 Evidence Register
3. **Approval Documentation:** Sheet 8 showing four-level approval workflow complete
4. **Gap Remediation Plan:** Derived from Sheet 6 Gap Summary (separate document or embedded in workbook)

**Auditor Review Process:**
1. Review Summary Dashboard (Sheet 6) for overall compliance score
2. Identify non-compliant areas (red status) in Sheets 2-4
3. Review Evidence Register (Sheet 7) for supporting evidence
4. Sample evidence files (verify 10-20% of evidence items)
5. Interview Security Operations Manager and Facilities Manager (validate assessment accuracy)
6. Test integration (trigger access control event, verify appears in SIEM)
7. Review physical facility (spot-check badge readers, cameras, sensors exist as documented)
8. Issue audit findings (if gaps identified) or confirm compliance

**Audit Questions Anticipated (Part I guides assessor to address proactively):**

- "How do you know camera count is accurate?" → Evidence: NVR screenshot showing camera list
- "How do you verify SIEM integration works?" → Evidence: SIEM screenshot showing access control events
- "What is your false alarm rate trend?" → Sheet 5 incidents include false alarms, trend shown in Sheet 6
- "Are all facilities documented?" → Sheet 2/3/4 comprehensive, or explicit "N/A" if facility truly has no systems

---

**END OF SPECIFICATION**

---

*"There must be no barriers to freedom of inquiry. There is no place for dogma in science."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-02-06 -->
