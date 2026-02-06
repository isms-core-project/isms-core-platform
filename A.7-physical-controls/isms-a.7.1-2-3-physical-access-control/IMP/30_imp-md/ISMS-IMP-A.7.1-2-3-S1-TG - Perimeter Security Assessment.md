**ISMS-IMP-A.7.1-2-3-S1-TG - Perimeter Security Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.1: Physical Security Perimeters

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.1-2-3-S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Physical Security Perimeters - Zone Definition, Building Perimeter, Internal Perimeters |
| **Related Policy** | ISMS-POL-A.7.1-2-3, Section 2.1 (Physical Security Perimeters) |
| **Purpose** | Document security perimeter definitions, assess construction quality, verify monitoring coverage, and identify gaps |
| **Target Audience** | Facilities Management, Physical Security, Building Services, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Annual or After Major Facility Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Perimeter Security assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.1-2-3-S1-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.1.1_Perimeter_Security_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a71_1_perimeter_security.py)

**Sheet Count:** 8 worksheets

**Data Capacity:** 100 data rows per assessment sheet (Sheets 2-5)

**Styling:** Navy blue headers, yellow input cells, conditional formatting for compliance status (green/amber/red)

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Assessment metadata and status legend | Read-only Reference | ~30 rows |
| 2 | Security Zones | Security zone inventory and classification | Data Entry | 100 data rows |
| 3 | Building Perimeter | External perimeter construction assessment | Data Entry | 100 data rows |
| 4 | Internal Perimeters | Internal zone boundary assessment | Data Entry | 100 data rows |
| 5 | Perimeter Monitoring | CCTV and intrusion detection coverage | Data Entry | 100 data rows |
| 6 | Summary Dashboard | Automated compliance scoring | Formula-driven | ~20 rows |
| 7 | Evidence Register | Supporting evidence documentation | Data Entry | 100 data rows |
| 8 | Approval Sign-Off | Four-level approval workflow | Data Entry | ~20 rows |

### Workbook Features

**Data Validation:**

- Dropdown lists for standardised input (Zone Types, Perimeter Elements, Status)
- Date validation (valid date format)

**Conditional Formatting:**

- Compliance Status columns: Green (Compliant), Amber (Partial), Red (Non-Compliant)
- Summary Dashboard scores: Colour-coded thresholds

**Formulas:**

- Summary Dashboard auto-calculates from Sheets 2-5
- Compliance Status derived from entry data

**Freeze Panes:**

- Header rows frozen
- First column frozen for horizontal scrolling

---

## Sheet-by-Sheet Specifications

### Sheet 2: Security Zones

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Zone ID | Text | 12 | None |
| B | Zone Name | Text | 25 | None |
| C | Zone Type | Dropdown | 18 | Public/Controlled/Restricted/High-Security |
| D | Location/Building | Text | 25 | None |
| E | Classification | Dropdown | 18 | Tier 1/Tier 2/Tier 3 |
| F | Access Requirements | Text | 30 | None |
| G | Perimeter Defined | Dropdown | 15 | Yes/Partial/No |
| H | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| I | Notes | Text | 35 | None |

### Sheet 3: Building Perimeter

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Building/Facility | Text | 25 | None |
| B | Perimeter Element | Dropdown | 20 | Wall/Roof/Floor/Window/Door/Exit/Dock/Other |
| C | Construction Type | Text | 20 | None |
| D | Solid Construction | Dropdown | 15 | Yes/No/Partial |
| E | Gap/Breach Points | Text | 20 | None |
| F | Security Controls | Text | 25 | None |
| G | Last Inspection | Date | 15 | Date format |
| H | Inspector | Text | 18 | None |
| I | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| J | Notes | Text | 35 | None |

### Sheet 4: Internal Perimeters

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | From Zone | Text | 20 | None |
| B | To Zone | Text | 20 | None |
| C | Barrier Type | Dropdown | 20 | Wall/Glass/Partition/Cage/Other |
| D | Floor-to-Ceiling | Dropdown | 15 | Yes/No/N/A |
| E | Above Ceiling Check | Dropdown | 18 | Yes/No/N/A |
| F | Below Floor Check | Dropdown | 18 | Yes/No/N/A |
| G | Access Control | Text | 20 | None |
| H | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| I | Notes | Text | 35 | None |

### Sheet 5: Perimeter Monitoring

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Entry Point ID | Text | 15 | None |
| B | Location | Text | 25 | None |
| C | Entry Type | Dropdown | 20 | Entrance/Door/Exit/Window/Dock/Roof/Vent |
| D | CCTV Coverage | Dropdown | 15 | Yes/No/Partial |
| E | Intrusion Detection | Dropdown | 18 | Yes/No/Partial |
| F | Alert Response | Text | 20 | None |
| G | Last Tested | Date | 15 | Date format |
| H | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| I | Notes | Text | 35 | None |

---

## Cell Styling Reference

### Colour Palette

**Headers:**

- Primary Header: #003366 (Navy blue), White text
- Column Header: #D9D9D9 (Light grey), Black text

**Data Cells:**

- Input Cell: #FFFFCC (Light yellow)
- Read-Only: White

**Compliance Status:**

- Compliant: #C6EFCE (Light green)
- Partial: #FFEB9C (Light amber)
- Non-Compliant: #FFC7CE (Light red)

---

## Integration Points

### Integration with Policy (ISMS-POL-A.7.1-2-3)

| Policy Section | Assessment Sheet | Focus |
|----------------|------------------|-------|
| 2.1.1 Perimeter Definition | Sheet 2: Security Zones | Zone classification and definition |
| 2.1.2 Perimeter Construction | Sheet 3: Building Perimeter | External perimeter assessment |
| 2.1.2 Internal Perimeters | Sheet 4: Internal Perimeters | Zone boundary construction |
| 2.1.3 Perimeter Monitoring | Sheet 5: Perimeter Monitoring | CCTV and intrusion detection |

### Integration with Other Assessments

**Feeds into:**

- ISMS-IMP-A.7.1-2-3-S4 (Compliance Dashboard) - Perimeter compliance score

**Dependencies from:**

- None - this is the foundational assessment

---

**END OF SPECIFICATION**

---

*"The strength of a chain is determined by its weakest link; the security of a perimeter, by its least protected point."*
--- Bruce Schneier

<!-- QA_VERIFIED: 2026-02-06 -->
