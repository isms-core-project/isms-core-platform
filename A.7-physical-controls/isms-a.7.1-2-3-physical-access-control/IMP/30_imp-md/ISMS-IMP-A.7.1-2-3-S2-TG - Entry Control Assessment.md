**ISMS-IMP-A.7.1-2-3-S2-TG - Entry Control Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.2: Physical Entry

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.1-2-3-S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Physical Entry Controls - Access Systems, Visitor Management, Contractor Access |
| **Related Policy** | ISMS-POL-A.7.1-2-3, Section 2.2 (Physical Entry Controls) |
| **Purpose** | Document entry control mechanisms, assess access control systems, verify visitor and contractor procedures |
| **Target Audience** | Facilities Management, Physical Security, Reception, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Access System Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Entry Control assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.1-2-3-S2-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.1.2_Entry_Control_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a71_2_entry_control.py)

**Sheet Count:** 8 worksheets

**Data Capacity:** 100 data rows per assessment sheet

**Styling:** Navy blue headers, yellow input cells, conditional formatting for compliance status (green/amber/red)

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Assessment metadata and legend | Read-only Reference | ~30 rows |
| 2 | Access Control Systems | Entry point access control inventory | Data Entry | 100 data rows |
| 3 | Visitor Management | Visitor procedure assessment | Data Entry | 100 data rows |
| 4 | Contractor Access | Contractor access control assessment | Data Entry | 100 data rows |
| 5 | After-Hours Access | After-hours access control assessment | Data Entry | 100 data rows |
| 6 | Summary Dashboard | Automated compliance scoring | Formula-driven | ~20 rows |
| 7 | Evidence Register | Supporting evidence documentation | Data Entry | 100 data rows |
| 8 | Approval Sign-Off | Four-level approval workflow | Data Entry | ~20 rows |

### Workbook Features

**Data Validation:**

- Dropdown lists for standardised input (Zone Types, Access System Types, Status)
- Date validation (valid date format)
- Number validation for log retention

**Conditional Formatting:**

- Compliance Status columns: Green (Compliant), Amber (Partial), Red (Non-Compliant)
- Summary Dashboard scores: Colour-coded thresholds
- Overdue dates highlighted in red

**Formulas:**

- Summary Dashboard auto-calculates from Sheets 2-5
- Compliance percentages calculated automatically
- Gap counts derived from status columns

**Freeze Panes:**

- Header rows frozen
- First column frozen for horizontal scrolling

---

## Sheet-by-Sheet Specifications

### Sheet 2: Access Control Systems

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Entry Point ID | Text | 15 | None |
| B | Location | Text | 25 | None |
| C | Security Zone | Dropdown | 18 | Controlled/Restricted/High-Security |
| D | Access System Type | Dropdown | 18 | Card/PIN/Biometric/Card+PIN/Multi-Factor |
| E | Authentication Method | Dropdown | 20 | Badge Only/Badge+PIN/Badge+Biometric/Dual-Person |
| F | Anti-Tailgating | Dropdown | 15 | Yes/No/Partial |
| G | Log Retention (Days) | Number | 15 | Integer |
| H | Last Review Date | Date | 15 | Date format |
| I | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| J | Notes | Text | 35 | None |

### Sheet 3: Visitor Management

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Procedure Element | Dropdown | 18 | Sign-In/ID Check/Badge/Escort/Sign-Out/After-Hours |
| B | Location/Facility | Text | 25 | None |
| C | Implemented | Dropdown | 15 | Yes/No/Partial/N/A |
| D | Sign-In Process | Dropdown | 15 | Yes/No/Partial/N/A |
| E | ID Verification | Dropdown | 15 | Yes/No/Partial/N/A |
| F | Badge Issued | Dropdown | 15 | Yes/No/Partial/N/A |
| G | Escort Required | Dropdown | 15 | Yes/No/Partial/N/A |
| H | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| I | Notes | Text | 35 | None |

### Sheet 4: Contractor Access

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Contractor Type | Dropdown | 18 | IT/Cleaning/Security/HVAC/Delivery/Construction/Other |
| B | Facility/Area | Text | 25 | None |
| C | Pre-Authorisation | Dropdown | 15 | Yes/No/Partial/N/A |
| D | Time-Limited Access | Dropdown | 15 | Yes/No/Partial/N/A |
| E | Access Logged | Dropdown | 15 | Yes/No/Partial/N/A |
| F | Escort Required | Dropdown | 15 | Yes/No/Partial/N/A |
| G | Supervision Level | Dropdown | 18 | Full Escort/Spot Checks/Self-Supervised/Not Required |
| H | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| I | Notes | Text | 35 | None |

### Sheet 5: After-Hours Access

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Facility/Entry Point | Text | 25 | None |
| B | Security Zone | Dropdown | 18 | Controlled/Restricted/High-Security |
| C | After-Hours Period | Text | 25 | None |
| D | Enhanced Auth | Dropdown | 15 | Yes/No/Partial/N/A |
| E | Alarm Integration | Dropdown | 15 | Yes/No/Partial/N/A |
| F | Security Response | Text | 25 | None |
| G | Access Logged | Dropdown | 15 | Yes/No/Partial/N/A |
| H | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| I | Notes | Text | 35 | None |

### Sheet 6: Summary Dashboard

**Structure:**

- Header with assessment title and period
- Control area compliance table
- Key metrics table
- Overall compliance score (highlighted)

**Calculated Fields:**

| Metric | Formula |
|--------|---------|
| Access Control Systems Score | COUNTIF(Status=Compliant) / COUNT(Status) * 100 |
| Visitor Management Score | COUNTIF(Status=Compliant) / COUNT(Status) * 100 |
| Contractor Access Score | COUNTIF(Status=Compliant) / COUNT(Status) * 100 |
| After-Hours Access Score | COUNTIF(Status=Compliant) / COUNT(Status) * 100 |
| Overall Score | Average of all area scores |

### Sheet 7: Evidence Register

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Evidence ID | Text | 12 | None |
| B | Evidence Type | Dropdown | 20 | Config Screenshot/Access Log/Visitor Log/Procedure/Form |
| C | Description | Text | 35 | None |
| D | Collection Date | Date | 15 | Date format |
| E | Collector | Text | 18 | None |
| F | Location/Link | Text | 40 | None |
| G | Status | Dropdown | 15 | Collected/Pending/Missing |

### Sheet 8: Approval Sign-Off

**Structure:**

| Row | Field | Description |
|-----|-------|-------------|
| Header | Assessment Info | Title, Document ID, Assessment Period |
| Approver 1 | Assessor | Name, Date, Status, Comments |
| Approver 2 | Facilities Manager | Name, Date, Status, Comments |
| Approver 3 | Physical Security Manager | Name, Date, Status, Comments |
| Approver 4 | CISO | Name, Date, Status, Comments |

---

## Cell Styling Reference

### Colour Palette

**Headers:**

- Primary Header: #003366 (Navy blue), White text
- Column Header: #D9D9D9 (Light grey), Black text

**Data Cells:**

- Input Cell: #FFFFCC (Light yellow)
- Read-Only: White
- Calculated: #E2EFDA (Light green)

**Compliance Status:**

- Compliant: #C6EFCE (Light green)
- Partial: #FFEB9C (Light amber)
- Non-Compliant: #FFC7CE (Light red)

**Dashboard Scores:**

- 90-100%: #C6EFCE (Green)
- 70-89%: #FFEB9C (Amber)
- Below 70%: #FFC7CE (Red)

---

## Integration Points

### Integration with Policy (ISMS-POL-A.7.1-2-3)

| Policy Section | Assessment Sheet | Focus |
|----------------|------------------|-------|
| 2.2.1 Entry Point Security | Sheet 2: Access Control Systems | Entry point inventory and controls |
| 2.2.2 Access Control Systems | Sheet 2: Access Control Systems | Authentication and logging |
| 2.2.3 Visitor Management | Sheet 3: Visitor Management | Visitor procedures |
| 2.2.4 Contractor Access | Sheet 4: Contractor Access | Contractor controls |
| 2.2.5 After-Hours Access | Sheet 5: After-Hours Access | Enhanced after-hours controls |

### Integration with Other Assessments

**Dependencies from:**

- ISMS-IMP-A.7.1-2-3-S1 (Perimeter Security) - Zone definitions, entry point identification

**Feeds into:**

- ISMS-IMP-A.7.1-2-3-S4 (Compliance Dashboard) - Entry control compliance score

### Integration with Related Controls

| Related Control | Integration Point |
|-----------------|-------------------|
| A.5.15-18 (Identity & Access) | Logical access aligned with physical access |
| A.6.1-2 (Screening) | Visitor ID verification procedures |
| A.6.6 (NDAs) | Contractor confidentiality agreements |
| A.8.1 (User Devices) | Device registration for visitors |

---

**END OF SPECIFICATION**

---

*"Security is not just about locks and keys; it's about ensuring only the right people pass through at the right time."*
--- Security Operations Principle

<!-- QA_VERIFIED: 2026-02-06 -->
