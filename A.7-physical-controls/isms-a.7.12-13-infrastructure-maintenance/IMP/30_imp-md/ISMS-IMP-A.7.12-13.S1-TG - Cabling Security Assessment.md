**ISMS-IMP-A.7.12-13.S1-TG - Cabling Security Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.12: Cabling Security

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.12-13.S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Cabling Security - Power and Data Cable Protection, Segregation, Documentation |
| **Related Policy** | ISMS-POL-A.7.12-13, Section 2.1 (Cabling Security) |
| **Purpose** | Document cabling infrastructure, assess protection measures against policy requirements, and identify gaps |
| **Target Audience** | Facilities Management, Network Engineers, IT Operations, Data Centre Managers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Annual or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Cabling Security assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.12-13.S1-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.12-13.S1_Cabling_Security_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a712_1_cabling_security.py)

**Sheet Count:** 8 worksheets

**Data Capacity:** 100 data rows per assessment sheet

**Styling:** Navy blue headers, yellow input cells, conditional formatting for compliance status

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Assessment metadata and status legend | Read-only Reference | ~30 rows |
| 2 | Cable Pathways | Cable pathway inventory and compliance | Data Entry | 100 data rows |
| 3 | Physical Protection | Physical and environmental protection | Data Entry | 100 data rows |
| 4 | Access Controls | Infrastructure access control assessment | Data Entry | 100 data rows |
| 5 | Documentation | Cable documentation compliance | Data Entry | 50 data rows |
| 6 | Summary Dashboard | Automated compliance scoring | Formula-driven | ~40 rows |
| 7 | Evidence Register | Supporting evidence documentation | Data Entry | 100 data rows |
| 8 | Approval Sign-Off | Four-level approval workflow | Data Entry | ~20 rows |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions & Legend

**Purpose:** Assessment metadata and status legend

**Structure:**

**Row 1:** Header
- Merged cells A1:G1
- Text: "ISMS-IMP-A.7.12-13.S1 - Cabling Security Assessment\nISO/IEC 27001:2022 - Control A.7.12: Cabling Security"
- Style: Navy blue background (#003366), white bold text, 14pt

**Rows 3-11:** Document Information Table
- Labels in Column A, Values in Column B
- User input fields (yellow): Assessment Date, Completed By, Organisation

**Rows 13-17:** Status Legend
- Colour-coded status definitions

### Sheet 2: Cable Pathways

**Purpose:** Document all cable pathways and assess protection status

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Pathway ID | Text | 12 | None |
| B | Facility/Building | Text | 25 | None |
| C | Pathway Type | Dropdown | 18 | List: Conduit, Cable Tray, Raised Floor, Underground, Ceiling Void, Wall Chase |
| D | Start Location | Text | 25 | None |
| E | End Location | Text | 25 | None |
| F | Cable Types | Text | 20 | None |
| G | Protection Type | Dropdown | 18 | List: Enclosed - Metal, Enclosed - Plastic, Open Tray, Armoured, None |
| H | Length (metres) | Number | 12 | Integer >0 |
| I | Segregation Compliant | Dropdown | 15 | List: Yes, No, N/A |
| J | Documentation Current | Dropdown | 15 | List: Yes, Partial, No |
| K | Last Inspection | Date | 15 | Date format |
| L | Compliance Status | Formula | 18 | Auto-calculated |
| M | Notes | Text | 40 | None |

**Compliance Status Formula:**
```excel
=IF(AND(G2<>"None", I2<>"No", J2<>"No"), "✅ Compliant",
   IF(OR(G2="None", I2="No"), "❌ Non-Compliant",
   "⚠️ Partial"))
```

### Sheet 3: Physical Protection

**Purpose:** Assess physical and environmental protection measures

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Area ID | Text | 12 | None |
| B | Facility/Building | Text | 25 | None |
| C | Area Name | Text | 25 | None |
| D | EMI Protection | Dropdown | 15 | List: Yes - Shielded, Partial, No, N/A |
| E | Physical Damage Protection | Dropdown | 20 | List: Yes - Armoured, Yes - Enclosed, Partial, No |
| F | Water Protection | Dropdown | 15 | List: Yes, Partial, No, N/A |
| G | Heat Protection | Dropdown | 15 | List: Yes, Partial, No, N/A |
| H | Cable Route Risk Level | Dropdown | 15 | List: Low, Medium, High |
| I | Fibre Used for High Security | Dropdown | 15 | List: Yes, No, N/A |
| J | Compliance Status | Formula | 18 | Auto-calculated |
| K | Notes | Text | 40 | None |

### Sheet 4: Access Controls

**Purpose:** Document access controls for cabling infrastructure

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Location ID | Text | 12 | None |
| B | Facility/Building | Text | 25 | None |
| C | Infrastructure Type | Dropdown | 18 | List: Wiring Closet, Patch Panel, Distribution Frame, Manhole, Duct Access |
| D | Location Description | Text | 30 | None |
| E | Lock Type | Dropdown | 20 | List: Electronic Access Card, Keyed Lock, Combination Lock, No Lock, Cage/Enclosure |
| F | Access Restricted | Dropdown | 25 | List: Yes - IT Only, Yes - Facilities Only, Yes - Authorised Personnel, No |
| G | Access Logged | Dropdown | 15 | List: Yes - Electronic, Yes - Manual, No |
| H | Occupied Monitoring | Dropdown | 15 | List: Yes - CCTV, Yes - Guards, No |
| I | Last Access Review | Date | 15 | Date format |
| J | Compliance Status | Formula | 18 | Auto-calculated |
| K | Notes | Text | 40 | None |

### Sheet 5: Documentation

**Purpose:** Audit cable documentation compliance

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Document Type | Dropdown | 20 | List: Cable Schedule, Network Diagram, Labelling Standard, Change Log, Audit Report |
| B | Document Name | Text | 35 | None |
| C | Document Location | Text | 40 | None |
| D | Owner | Text | 25 | None |
| E | Last Updated | Date | 15 | Date format |
| F | Review Cycle | Dropdown | 15 | List: Annual, Quarterly, On Change |
| G | Current | Dropdown | 10 | List: Yes, No |
| H | Accessible | Dropdown | 15 | List: Yes - Online, Yes - Restricted, No |
| I | Compliance Status | Formula | 18 | Auto-calculated |
| J | Notes | Text | 40 | None |

### Sheet 6: Summary Dashboard

**Purpose:** Automated compliance scoring and metrics

**Structure:**
- Overall Compliance Score (weighted average)
- Domain Scores (Pathways, Protection, Access, Documentation)
- Gap Summary (auto-generated from non-compliant items)

**Weighting:**
- Cable Pathways: 30%
- Physical Protection: 25%
- Access Controls: 25%
- Documentation: 20%

### Sheet 7: Evidence Register

**Purpose:** Document supporting evidence for audit

**Columns:**
- Evidence ID, Evidence Type, Description, Related Sheet/Item
- File Name, File Location, Collection Date, Collected By
- Retention Period, Notes

### Sheet 8: Approval Sign-Off

**Purpose:** Four-level approval workflow

**Structure:**
- Assessment summary section
- Approval table (Role, Name, Signature, Date, Comments)

---

## Cell Styling Reference

### Colour Palette

**Headers:**
- Primary Header: #003366 (Navy blue), white text
- Column Header: #D9D9D9 (Light grey), black text

**Data Cells:**
- Input Cell: #FFFFCC (Light yellow)
- Formula Cell: #FFFFFF (White)

**Compliance Status:**
- Compliant: #C6EFCE (Light green)
- Partial: #FFEB9C (Light amber)
- Non-Compliant: #FFC7CE (Light red)

### Font Specifications

- Headers: Calibri, 14pt (primary), 10pt (column), Bold
- Data Cells: Calibri, 10pt, Regular

---

## Integration Points

### Integration with Policy

**Policy Section → Assessment Sheet Mapping:**

| Policy Section | Assessment Sheet | Focus |
|----------------|------------------|-------|
| Section 2.1.1: Cable Protection | Sheet 2, Sheet 3 | Pathways and protection measures |
| Section 2.1.2: Access Control | Sheet 4 | Infrastructure access controls |
| Section 2.1.3: Segregation Requirements | Sheet 2, Sheet 3 | Power/data segregation, fibre for security |
| Section 2.1.4: Documentation | Sheet 5 | Cable schedules, diagrams, labelling |
| Section 2.1.5: Inspection and Maintenance | Sheet 2 | Last inspection dates |

### Integration with Other Assessments

**Feeds into:**
- ISMS-IMP-A.7.12-13.S4 (Compliance Dashboard)
- Network security assessments

**Dependencies from:**
- Facility inventory
- Network documentation

---

**END OF SPECIFICATION**

---

*"The strength of the chain is the strength of the weakest link."*
— Thomas Reid

<!-- QA_VERIFIED: 2026-02-06 -->
