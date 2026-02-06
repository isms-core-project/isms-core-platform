**ISMS-IMP-A.7.6-7-14-S2-TG - Clear Desk and Clear Screen Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.7: Clear Desk and Clear Screen

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.6-7-14-S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Clear Desk and Clear Screen - Workspace Information Protection |
| **Related Policy** | ISMS-POL-A.7.6-7-14, Section 2.2 (Clear Desk and Clear Screen) |
| **Purpose** | Document clear desk/screen requirements, assess workspace compliance, track audit results and enforcement |
| **Target Audience** | Facilities Management, IT Operations, Line Managers, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Procedural |
| **Review Cycle** | Monthly (Audits) / Quarterly (Full Assessment) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Clear Desk/Screen Compliance assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.6-7-14-S2-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.7.S2_Clear_Desk_Screen_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a76_2_clear_desk_screen.py)

**Sheet Count:** 8 worksheets

**Data Capacity:** 100 data rows per assessment sheet

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type |
|---------|------------|---------|------|
| 1 | Instructions & Legend | Assessment metadata | Read-only Reference |
| 2 | Requirements Matrix | Classification requirements | Data Entry |
| 3 | Screen Lock Configuration | Technical control verification | Data Entry |
| 4 | Audit Results | Clear desk audit tracking | Data Entry |
| 5 | Workspace Assessment | Area compliance infrastructure | Data Entry |
| 6 | Summary Dashboard | Automated compliance scoring | Formula-driven |
| 7 | Evidence Register | Audit evidence documentation | Data Entry |
| 8 | Approval Sign-Off | Approval workflow | Data Entry |

---

## Sheet-by-Sheet Specifications

### Sheet 2: Requirements Matrix

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Classification Level | Dropdown | 18 | CONFIDENTIAL / INTERNAL / PUBLIC |
| B | Clear Desk - Work Hours | Text | 25 | None |
| C | Clear Desk - End of Day | Text | 25 | None |
| D | Storage Requirement | Text | 25 | None |
| E | Screen Lock Timeout | Number | 15 | Integer |
| F | Privacy Screen Required | Dropdown | 20 | Required / Recommended / Not Required |
| G | Implementation Status | Dropdown | 20 | Implemented / Partial / Not Implemented |
| H | Notes | Text | 50 | None |

### Sheet 3: Screen Lock Configuration

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Device Type | Text | 20 | None |
| B | Policy Name | Text | 30 | None |
| C | Configured Timeout (min) | Number | 18 | Integer |
| D | Required Timeout (min) | Number | 18 | Integer |
| E | Compliant | Formula | 12 | Auto |
| F | Enforcement Method | Dropdown | 20 | Group Policy / MDM / Manual |
| G | Device Count | Number | 15 | Integer |
| H | Last Verified | Date | 15 | Date |
| I | Evidence | Text | 30 | None |
| J | Notes | Text | 40 | None |

### Sheet 4: Audit Results

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Audit Date | Date | 15 | Date |
| B | Audit Type | Dropdown | 20 | Scheduled / Random / Post-Incident |
| C | Location/Area | Text | 25 | None |
| D | Workstations Audited | Number | 18 | Integer |
| E | Compliant | Number | 12 | Integer |
| F | Non-Compliant | Number | 15 | Integer |
| G | Compliance Rate | Formula | 15 | Percentage |
| H | Common Issues | Text | 35 | None |
| I | Follow-Up Actions | Text | 35 | None |
| J | Auditor | Text | 20 | None |

### Sheet 5: Workspace Assessment

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Area ID | Text | 12 | None |
| B | Location | Text | 30 | None |
| C | Workspace Type | Dropdown | 20 | Open Plan / Private / Meeting Room / Shared / Home |
| D | Workstation Count | Number | 15 | Integer |
| E | Lockable Storage | Dropdown | 18 | Yes - All / Yes - Partial / No |
| F | Shredder Access | Dropdown | 18 | Yes - On Floor / Yes - Central / No |
| G | Confidential Bins | Dropdown | 15 | Yes / No |
| H | Privacy Screens | Dropdown | 18 | Yes - All / Yes - Partial / No / N/A |
| I | Avg Audit Compliance | Text | 18 | Percentage |
| J | Compliance Status | Formula | 18 | Auto |
| K | Notes | Text | 40 | None |

---

## Cell Styling Reference

### Colour Palette

**Headers:**
- Primary: #003366 (Navy blue), #FFFFFF (White text)
- Column: #D9D9D9 (Grey), #000000 (Black text)

**Data Cells:**
- Input: #FFFFCC (Yellow)
- Formula: #FFFFFF (White)

**Status:**
- Compliant: #C6EFCE (Green)
- Partial: #FFEB9C (Amber)
- Non-Compliant: #FFC7CE (Red)

---

## Integration Points

### Policy Integration

| Policy Section | Assessment Sheet |
|----------------|------------------|
| Section 2.2: Clear Desk Requirements | Sheet 2, Sheet 5 |
| Section 2.2: Clear Screen Requirements | Sheet 2, Sheet 3 |
| Section 2.2: Enforcement | Sheet 4 |

### Dashboard Integration

Feeds into ISMS-IMP-A.7.6-7-14-S4 Compliance Dashboard:
- Screen lock compliance percentage
- Audit compliance trend
- Workspace infrastructure score

---

**END OF SPECIFICATION**

---

*"The best defence against data leakage is a culture of security, not just a policy document."*
— Unknown

<!-- QA_VERIFIED: 2026-02-06 -->
