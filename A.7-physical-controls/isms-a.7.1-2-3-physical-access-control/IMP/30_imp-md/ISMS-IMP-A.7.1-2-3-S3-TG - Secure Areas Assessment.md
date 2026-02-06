**ISMS-IMP-A.7.1-2-3-S3-TG - Secure Areas Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.3: Securing Offices, Rooms and Facilities

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.1-2-3-S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Securing Offices, Rooms and Facilities - Office Security, Server Rooms, Meeting Rooms |
| **Related Policy** | ISMS-POL-A.7.1-2-3, Section 2.3 (Securing Offices, Rooms and Facilities) |
| **Purpose** | Document secure area controls, assess office security, verify server room protection, evaluate meeting room procedures |
| **Target Audience** | Facilities Management, IT Operations, Physical Security, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Annual or After Facility Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Secure Areas assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.1-2-3-S3-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.1.3_Secure_Areas_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a71_3_secure_areas.py)

**Sheet Count:** 8 worksheets

**Data Capacity:** 100 data rows per assessment sheet

**Styling:** Navy blue headers, yellow input cells, conditional formatting for compliance status (green/amber/red)

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Assessment metadata and legend | Read-only Reference | ~30 rows |
| 2 | Office Security | Office security assessment | Data Entry | 100 data rows |
| 3 | Server Rooms | Server room and datacenter security | Data Entry | 100 data rows |
| 4 | Meeting Rooms | Meeting room security procedures | Data Entry | 100 data rows |
| 5 | Shared Facilities | Shared building security arrangements | Data Entry | 100 data rows |
| 6 | Summary Dashboard | Automated compliance scoring | Formula-driven | ~20 rows |
| 7 | Evidence Register | Supporting evidence documentation | Data Entry | 100 data rows |
| 8 | Approval Sign-Off | Four-level approval workflow | Data Entry | ~20 rows |

### Workbook Features

**Data Validation:**

- Dropdown lists for standardised input (Zone Types, Room Types, Status)
- Date validation (valid date format)

**Conditional Formatting:**

- Compliance Status columns: Green (Compliant), Amber (Partial), Red (Non-Compliant)
- Summary Dashboard scores: Colour-coded thresholds

**Formulas:**

- Summary Dashboard auto-calculates from Sheets 2-5
- Compliance percentages calculated automatically
- Gap counts derived from status columns

**Freeze Panes:**

- Header rows frozen
- First column frozen for horizontal scrolling

---

## Sheet-by-Sheet Specifications

### Sheet 2: Office Security

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Office/Area ID | Text | 15 | None |
| B | Location | Text | 25 | None |
| C | Security Zone | Dropdown | 18 | Controlled/Restricted/High-Security |
| D | Classification | Dropdown | 20 | Public/Internal/Confidential/Highly Confidential |
| E | Lock When Unoccupied | Dropdown | 15 | Yes/No/Partial/N/A |
| F | Clean Desk Enforced | Dropdown | 15 | Yes/No/Partial/N/A |
| G | Screen Privacy | Dropdown | 15 | Yes/No/Partial/N/A |
| H | Secure Storage | Dropdown | 15 | Yes/No/Partial/N/A |
| I | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| J | Notes | Text | 35 | None |

### Sheet 3: Server Rooms

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Room ID | Text | 12 | None |
| B | Location | Text | 25 | None |
| C | Room Type | Dropdown | 18 | Server Room/Datacenter/Network Closet/Comms Room/UPS Room |
| D | MFA Access | Dropdown | 15 | Yes/No/Partial/N/A |
| E | No Windows | Dropdown | 15 | Yes/No/Partial/N/A |
| F | Reinforced Walls | Dropdown | 15 | Yes/No/Partial/N/A |
| G | CCTV Coverage | Dropdown | 15 | Yes/No/Partial/N/A |
| H | Access Logging | Dropdown | 15 | Yes/No/Partial/N/A |
| I | Env. Monitoring | Dropdown | 15 | Yes/No/Partial/N/A |
| J | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| K | Notes | Text | 35 | None |

### Sheet 4: Meeting Rooms

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Room ID | Text | 12 | None |
| B | Location | Text | 25 | None |
| C | Room Classification | Dropdown | 18 | Standard/Boardroom/Secure/Interview |
| D | Recording Check | Dropdown | 15 | Yes/No/Partial/N/A |
| E | Whiteboard Clear | Dropdown | 15 | Yes/No/Partial/N/A |
| F | Document Clear | Dropdown | 15 | Yes/No/Partial/N/A |
| G | VC Equipment Secured | Dropdown | 15 | Yes/No/Partial/N/A |
| H | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| I | Notes | Text | 35 | None |

### Sheet 5: Shared Facilities

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Facility/Building | Text | 25 | None |
| B | Sharing Arrangement | Dropdown | 18 | Multi-Tenant/Co-Working/Shared Floor/Colocation/Sole Occupant |
| C | Perimeter Defined | Dropdown | 15 | Yes/No/Partial/N/A |
| D | Own Access Control | Dropdown | 15 | Yes/No/Partial/N/A |
| E | Building Mgmt Access | Dropdown | 20 | Controlled and Logged/Controlled Only/Uncontrolled/N/A |
| F | Shared Infrastructure | Text | 30 | None |
| G | Key Management | Text | 25 | None |
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
| Office Security Score | COUNTIF(Status=Compliant) / COUNT(Status) * 100 |
| Server Rooms Score | COUNTIF(Status=Compliant) / COUNT(Status) * 100 |
| Meeting Rooms Score | COUNTIF(Status=Compliant) / COUNT(Status) * 100 |
| Shared Facilities Score | COUNTIF(Status=Compliant) / COUNT(Status) * 100 |
| Overall Score | Average of all area scores |

### Sheet 7: Evidence Register

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Evidence ID | Text | 12 | None |
| B | Evidence Type | Dropdown | 20 | Photograph/Audit Report/Configuration/Log Sample/Procedure |
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
| Approver 3 | IT Operations Manager | Name, Date, Status, Comments |
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
| 2.3.1 General Offices | Sheet 2: Office Security | Office locking, clean desk |
| 2.3.2 Sensitive Areas | Sheet 2: Office Security (Classification: Confidential+) | Enhanced controls |
| 2.3.3 Server Rooms | Sheet 3: Server Rooms | Technical space security |
| 2.3.4 Meeting Rooms | Sheet 4: Meeting Rooms | Meeting room procedures |
| 2.3.5 Shared Facilities | Sheet 5: Shared Facilities | Multi-tenant arrangements |

### Integration with Other Assessments

**Dependencies from:**

- ISMS-IMP-A.7.1-2-3-S1 (Perimeter Security) - Zone inventory
- ISMS-IMP-A.7.1-2-3-S2 (Entry Control) - Access control configuration

**Feeds into:**

- ISMS-IMP-A.7.1-2-3-S4 (Compliance Dashboard) - Secure areas compliance score

### Integration with Related Controls

| Related Control | Integration Point |
|-----------------|-------------------|
| A.5.10 (Acceptable Use) | Clean desk policy alignment |
| A.5.12 (Classification) | Information classification in secure areas |
| A.7.7-9 (Working in Secure Areas) | Secure area operational controls |
| A.7.10 (Storage Media) | Secure storage for media |
| A.8.1 (User Devices) | Device security in offices |

---

**END OF SPECIFICATION**

---

*"The security of a place lies not just in its walls, but in the practices of those within."*
--- Physical Security Principle

<!-- QA_VERIFIED: 2026-02-06 -->
