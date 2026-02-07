**ISMS-IMP-A.5.7.2-TG - Intelligence Collection & Analysis Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Intelligence Collection, Analysis & Production Capabilities |
| **Related Policy** | ISMS-POL-A.5.7, Section 2.1 (Intelligence Collection Requirements), Section 2.2 (Intelligence Analysis and Production Requirements) |
| **Purpose** | Assess organizational capability to collect, analyze, and produce actionable threat intelligence including CVSS-integrated vulnerability-threat linkage |
| **Target Audience** | Threat Intelligence Analysts, SOC Team, Security Engineers, CISO, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial consolidated specification (14 sheets) | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a57_2_collection_analysis.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.7.2` |
| **Output Filename** | `ISMS-IMP-A.5.7.2_Intelligence_Collection_&_Analysis_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Intelligence Collection & Analysis Assessment |
| **Total Sheets** | 16 (16 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #8B0000 | 8B0000 | Dark Red (Critical) |
| #8FAADC | 8FAADC | Custom |
| #90EE90 | 90EE90 | Custom |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D3D3D3 | D3D3D3 | Custom |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #DC143C | DC143C | Custom |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FF8C00 | FF8C00 | Dark Orange (Severe) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFD700 | FFD700 | Custom |
| #FFD966 | FFD966 | Gold/Yellow (Highlight) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFF00 | FFFF00 | Yellow (Warning) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Intelligence_Requirements

---

## Sheet 3: Collection_Sources

---

## Sheet 4: Raw_Intelligence_Log

---

## Sheet 5: Intelligence_Production

---

## Sheet 6: MITRE_Mapping

---

## Sheet 7: Quality_Metrics

---

## Sheet 8: Vulnerability_Linked_Threats

---

## Sheet 9: Process_Maturity

---

## Sheet 10: Action_Items

---

## Sheet 11: Analysis_Tools

---

## Sheet 12: Threat_Actor_Profiles

---

## Sheet 13: Campaign_Tracking

---

## Sheet 14: Metadata

---

## Sheet 15: Mitre_Mapping

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Technique_ID |
| B | Tactic |
| C | Technique_Name |
| D | Sub_Technique |
| E | Priority_for_Org |
| F | Coverage_Level |
| G | Intelligence_Sources |
| H | Last_Intelligence_Update |
| I | Detection_Capability |
| J | Use_Cases_Identified |
| K | Gap_Analysis |
| L | Notes |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| F5:F104 | equal  | Fill: #C6EFCE (Light Green (Compliant/Pass)) |
| F5:F104 | equal  | Fill: #FFC7CE (Light Red (Non-Compliant/Fail)) |
| F5:F104 | equal  | Fill: #FFEB9C (Light Yellow/Amber (Partial)) |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(A5:A104)` | Total Techniques Tracked: |
| — | `=COUNTIF(E5:E104,` | Critical Priority: |
| — | `=COUNTIF(F5:F104,` | Full Coverage: |
| — | `=COUNTIF(I5:I104,` | With Detection Capability: |

---

## Sheet 16: Analyst_Capabilities

**Data Rows:** 20 (rows 5–24)

### Columns

| Col | Header |
|-----|--------|
| A | Analyst_ID |
| B | Analyst_Name |
| C | Email |
| D | Role |
| E | Team |
| F | Years_Experience_TI |
| G | Years_Experience_InfoSec |
| H | Primary_Focus_Area |
| I | Secondary_Focus_Area |
| J | Skill_OSINT |
| K | Skill_Malware_Analysis |
| L | Skill_MITRE_ATTACK |
| M | Skill_Scripting_Python |
| N | Skill_Threat_Modeling |
| O | Skill_Report_Writing |
| P | Skill_Briefing_Presentation |
| Q | Certifications |
| R | Training_Planned_2025 |
| S | Training_Budget_2025 |
| T | Last_Performance_Review |
| U | Capability_Gap_Identified |
| V | Notes |

---

**END OF SPECIFICATION**

---

*"How wonderful that we have met with a paradox. Now we have some hope of making progress."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
