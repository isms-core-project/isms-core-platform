**ISMS-IMP-A.5.7.3-TG - Intelligence Integration & Distribution Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Intelligence Integration into Security Operations & Distribution to Stakeholders |
| **Related Policy** | ISMS-POL-A.5.7, Section 2.3 (Intelligence Dissemination Requirements), Section 2.4 (Risk Assessment Integration Requirements), Section 2.5 (Incident Management Integration Requirements), Section 2.7 (Effectiveness Measurement Requirements) |
| **Purpose** | Assess effectiveness of threat intelligence integration with security tools, dissemination to stakeholders, and measurement of operational impact including prevention tracking |
| **Target Audience** | Security Operations Manager, SOC Team, Incident Response, Network Security, Threat Intelligence Team, Risk Management, CISO, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial consolidated specification (17 sheets) | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a57_3_integration.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.7.3` |
| **Output Filename** | `ISMS-IMP-A.5.7.3_Intelligence_Integration_&_Distribution_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Intelligence Integration & Distribution Assessment |
| **Total Sheets** | 19 (19 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #006100 | 006100 | Dark Green (Pass) |
| #0066CC | 0066CC | Custom |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #8FAADC | 8FAADC | Custom |
| #9C0006 | 9C0006 | Dark Red (Error) |
| #C65911 | C65911 | Brown/Orange (Overdue) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D5F5D5 | D5F5D5 | Custom |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FFC000 | FFC000 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Tool_Integration_Matrix

---

## Sheet 3: IOC_Deployment

---

## Sheet 4: Dissemination_Channels

---

## Sheet 5: Stakeholder_Registry

---

## Sheet 6: Distribution_Tracking

---

## Sheet 7: Prevention_Tracking

---

## Sheet 8: Feedback_Collection

---

## Sheet 9: Integration_Metrics

---

## Sheet 10: SIEM_Integration_Details

---

## Sheet 11: EDR_Integration_Details

---

## Sheet 12: Threat_Hunting_Campaigns

---

## Sheet 13: Risk_Assessment_Updates

---

## Sheet 14: Incident_TI_Integration

---

## Sheet 15: Intelligence_Driven_Decisions

---

## Sheet 16: Action_Items

---

## Sheet 17: Metadata

---

## Sheet 18: Tool_Integration

**Data Rows:** 30 (rows 5–34) | **Frozen Panes:** C5

### Columns

| Col | Header |
|-----|--------|
| A | Tool_ID |
| B | Tool_Category |
| C | Tool_Name |
| D | Vendor |
| E | Version |
| F | Primary_Owner |
| G | Integration_Status |
| H | Integration_Method |
| I | Integration_Direction |
| J | Data_Types_Integrated |
| K | Automation_Level |
| L | Update_Frequency |
| M | IOC_Types_Supported |
| N | Last_Successful_Sync |
| O | Sync_Errors_Last_30_Days |
| P | Effectiveness_Rating |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=COUNTA(C5:C34)` |  |
| BN | `=COUNTIF(G5:G34,` |  |

---

## Sheet 19: Ioc_Deployment

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** D5

### Columns

| Col | Header |
|-----|--------|
| A | IOC_ID |
| B | IOC_Type |
| C | IOC_Value |
| D | Intelligence_Source |
| E | Threat_Actor |
| F | Associated_Malware |
| G | Confidence_Level |
| H | Severity |
| I | TLP_Classification |
| J | Deployment_Date |
| K | Deployed_To_Tools |
| L | Deployment_Method |
| M | Expiration_Date |
| N | Status |
| O | Hits_Last_7_Days |
| P | Hits_Last_30_Days |
| Q | Hits_Total |
| R | Last_Hit_Date |
| S | False_Positive |
| T | Effectiveness_Rating |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| TN | `=IF(AND(Q{row}>0,S{row}=` |  |
| BN | `=COUNTA(C5:C104)` |  |
| BN | `=COUNTIF(N5:N104,` |  |
| BN | `=COUNTIF(O5:O104,` |  |
| BN | `=COUNTIF(S5:S104,` |  |
| BN | `=COUNTIF(T5:T104,` |  |

---

**END OF SPECIFICATION**

---

*"The opposite of a correct statement is a false statement. But the opposite of a profound truth may well be another profound truth."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
