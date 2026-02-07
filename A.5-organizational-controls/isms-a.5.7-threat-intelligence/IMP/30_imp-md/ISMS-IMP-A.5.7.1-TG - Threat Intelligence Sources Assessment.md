**ISMS-IMP-A.5.7.1-TG - Threat Intelligence Sources Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Threat Intelligence Source Portfolio Management |
| **Related Policy** | ISMS-POL-A.5.7, Section 2.1 (Intelligence Collection Requirements), Section 2.7 (Effectiveness Measurement Requirements) |
| **Purpose** | Document threat intelligence source portfolio, assess source reliability using Admiralty Code, verify CVSS capability, and maintain audit evidence for quarterly validation |
| **Target Audience** | Threat Intelligence Analysts, Security Engineers, CISO, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial consolidated specification (15 sheets) | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a57_1_sources.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.7.1` |
| **Output Filename** | `ISMS-IMP-A.5.7.1_Threat_Intelligence_Sources_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Threat Intelligence Sources Assessment |
| **Total Sheets** | 31 (31 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | COLOR_BLUE_HEADER | Dark Blue (Headers) |
| #006100 | COLOR_GREEN_DARK | Dark Green (Pass) |
| #0066CC | 0066CC | Custom |
| #00B050 | COLOR_GREEN | Custom |
| #4472C4 | COLOR_BLUE_SUB | Medium Blue (Sub-headers) |
| #8FAADC | COLOR_BLUE_SECTION | Custom |
| #9C0006 | 9C0006 | Dark Red (Error) |
| #C65911 | C65911 | Brown/Orange (Overdue) |
| #C6EFCE | COLOR_GREEN_LIGHT | Light Green (Compliant/Pass) |
| #D5F5D5 | D5F5D5 | Custom |
| #D8E4F8 | COLOR_BLUE_PALE | Pale Blue (Sub-section) |
| #D9D9D9 | COLOR_GRAY | Light Gray (Column Headers) |
| #E7E6E6 | COLOR_GRAY_FORMULA | Light Gray (Example Rows) |
| #E7F4E4 | COLOR_GREEN_PALE | Custom |
| #FFC000 | FFC000 | Custom |
| #FFC7CE | COLOR_RED | Light Red (Non-Compliant/Fail) |
| #FFD966 | COLOR_ORANGE | Gold/Yellow (Highlight) |
| #FFEB9C | COLOR_YELLOW | Light Yellow/Amber (Partial) |
| #FFF4CC | COLOR_YELLOW_PALE | Custom |
| #FFFFCC | COLOR_YELLOW_INPUT | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Source_Inventory

---

## Sheet 3: Source_Evaluation

---

## Sheet 4: Coverage_Matrix

---

## Sheet 5: Cost_Analysis

---

## Sheet 6: Compliance_Check

---

## Sheet 7: Action_Items

---

## Sheet 8: Metadata

---

## Sheet 9: Integration_Points

---

## Sheet 10: Update_Frequency

---

## Sheet 11: Source_Contacts

---

## Sheet 12: Vendor_SLAs

---

## Sheet 13: API_Integration

---

## Sheet 14: Source_Performance_Validation

---

## Sheet 15: Business_Continuity_Plan

---

## Sheet 16: Data_Validations

**Purpose:** **UPDATED v1.0**: Added CVSS_Support, API health, role criticality, and validation status dropdowns.

---

## Sheet 17: Instructions

---

## Sheet 18: Source_Inventory

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Source_ID |
| B | Source_Name |
| C | Source_Type |
| D | Source_Category |
| E | Provider |
| F | Contact_Email |
| G | Contract_Start |
| H | Contract_End |
| I | Auto_Renew |
| J | Status |
| K | CVSS_Support |
| L | Primary_Owner |
| M | Backup_Owner |
| N | Last_Review_Date |
| O | Next_Review_Date |
| P | Notes |

---

## Sheet 19: Source_Evaluation

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Source_ID |
| B | Source_Name |
| C | Evaluation_Date |
| D | Evaluator |
| E | Reliability_Rating |
| F | Reliability_Justification |
| G | Credibility_Rating |
| H | Credibility_Justification |
| I | Timeliness_Score |
| J | Timeliness_Notes |
| K | Relevance_Score |
| L | Relevance_Notes |
| M | Actionability_Score |
| N | Actionability_Notes |
| O | Overall_Quality_Score |
| P | Quality_Rating |
| Q | False_Positive_Rate |
| R | CVSS_Accuracy_Rate |
| S | CVSS_Sample_Size |
| T | CVSS_Validation_Date |
| U | Evidence_Link |
| V | Recommendation |
| W | Next_Evaluation |

---

## Sheet 20: Coverage_Matrix

---

## Sheet 21: Cost_Analysis

---

## Sheet 22: Compliance_Check

---

## Sheet 23: Action_Items

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Action_ID |
| B | Source_ID |
| C | Issue_Type |
| D | Issue_Description |
| E | Detected_In_Sheet |
| F | Priority |
| G | Assigned_To |
| H | Due_Date |
| I | Status |
| J | Status_Notes |
| K | Resolution_Date |
| L | Evidence_Link |
| M | Created_Date |
| N | Created_By |
| O | Last_Updated |

---

## Sheet 24: Source_Performance_Validation

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Validation_ID |
| B | Source_ID |
| C | Source_Name |
| D | Validation_Quarter |
| E | Validation_Date |
| F | Validator |
| G | Validation_Method |
| H | Total_Sample_Size |
| I | IOC_Sample_Size |
| J | IOC_True_Positives |
| K | IOC_False_Positives |
| L | IOC_Accuracy |
| M | CVE_Sample_Size |
| N | CVE_Accurate |
| O | CVE_Inaccurate |
| P | CVE_Accuracy |
| Q | CVSS_Accurate_Count |
| R | CVSS_Inaccurate_Count |
| S | CVSS_Accuracy_Rate |
| T | CVSS_Accuracy_Method |
| U | Overall_Accuracy_Rate |
| V | Admiralty_Code_Source |
| W | Admiralty_Code_Info |
| X | Admiralty_Combined |
| Y | Validation_Pass |
| Z | Pass_Criteria_Met |
| AA | Action_Required |
| AB | Action_Notes |
| AC | Action_Item_Created |
| AD | Action_Item_ID |
| AE | Evidence_Location |
| AF | Reviewed_By |
| AG | Review_Date |
| AH | Next_Validation_Date |

---

## Sheet 25: Business_Continuity_Plan

**Data Rows:** 50 (rows 5–54)

### Columns

| Col | Header |
|-----|--------|
| A | Role_ID |
| B | Role_Name |
| C | Role_Description |
| D | Role_Category |
| E | Primary_Person_Name |
| F | Primary_Person_Email |
| G | Primary_Employment_Status |
| H | Primary_Training_Complete |
| I | Primary_Training_Date |
| J | Primary_Cert_Valid_Until |
| K | Backup_Person_Name |
| L | Backup_Person_Email |
| M | Backup_Employment_Status |
| N | Backup_Training_Complete |
| O | Backup_Training_Date |
| P | Backup_Cert_Valid_Until |
| Q | Backup_Ready_Percentage |
| R | Critical_Sources_Count |
| S | Critical_Sources_List |
| T | Access_Documented |
| U | Access_Documentation_Location |
| V | Access_Documentation_Format |
| W | Access_Last_Verified |
| X | Access_Next_Verification |
| Y | Last_Continuity_Test_Date |
| Z | Last_Test_Duration |
| AA | Last_Test_Scenario |
| AB | Last_Test_Result |
| AC | Last_Test_Issues |
| AD | Last_Test_Evidence |
| AE | Next_Test_Date |
| AF | Compliance_Status |
| AG | Non_Compliance_Reasons |
| AH | Remediation_Required |
| AI | Remediation_Action_ID |
| AJ | Last_Review_Date |
| AK | Next_Review_Date |
| AL | Reviewer |
| AM | Notes |

---

## Sheet 26: Integration_Points

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Source_ID |
| B | Source_Name |
| C | Integration_Type |
| D | Integration_Target_Type |
| E | Integration_Target_Name |
| F | API_Endpoint |
| G | Authentication_Method |
| H | Data_Format |
| I | CVSS_In_Feed |
| J | TLP_Support |
| K | IOC_Types_Supported |
| L | Bidirectional |
| M | Integration_Status |
| N | Last_Integration_Test |
| O | Next_Integration_Test |
| P | Integration_Owner |
| Q | Documentation_Link |
| R | Notes |

---

## Sheet 27: Update_Frequency

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Source_ID |
| B | Source_Name |
| C | Contractual_Frequency |
| D | Actual_Avg_Frequency |
| E | Last_Update_Received |
| F | Update_Count_Last_30_Days |
| G | Expected_Update_Count |
| H | Update_Variance |
| I | SLA_Met |
| J | SLA_Met_Justification |
| K | Outage_Count_Last_Quarter |
| L | Longest_Outage_Duration |
| M | Average_Outage_Duration |
| N | Timeliness_Score |
| O | Timeliness_Trend |
| P | Last_SLA_Review |
| Q | Next_SLA_Review |
| R | Notes |

---

## Sheet 28: Source_Contacts

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Source_ID |
| B | Source_Name |
| C | Contact_Type |
| D | Contact_Name |
| E | Contact_Title |
| F | Contact_Email |
| G | Contact_Phone |
| H | Contact_Region |
| I | Availability |
| J | Escalation_Path |
| K | Preferred_Contact_Method |
| L | Language_Supported |
| M | Last_Contact_Date |
| N | Last_Contact_Reason |
| O | Response_Quality |
| P | Response_Time |
| Q | Contact_Status |
| R | Replacement_Contact |
| S | Last_Verified |
| T | Next_Verification |
| U | Notes |

---

## Sheet 29: Vendor_Slas

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | SLA_Record_ID |
| B | Source_ID |
| C | Source_Name |
| D | SLA_Metric |
| E | Contractual_Target |
| F | Contractual_Target_Numeric |
| G | Actual_Performance |
| H | Actual_Performance_Numeric |
| I | Performance_Variance |
| J | Measurement_Period |
| K | Measurement_Start_Date |
| L | Measurement_End_Date |
| M | SLA_Status |
| N | SLA_Breach_Count |
| O | Penalty_Clause |
| P | Penalty_Amount |
| Q | Penalty_Applied |
| R | Penalty_Application_Date |
| S | Credit_Received |
| T | Escalated_To_Vendor |
| U | Escalation_Date |
| V | Vendor_Response |
| W | Last_Review_Date |
| X | Next_Review_Date |
| Y | Reviewer |
| Z | Notes |

---

## Sheet 30: Api_Integration

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Source_ID |
| B | Source_Name |
| C | API_Version |
| D | API_Endpoint_Base |
| E | API_Endpoint_Intel |
| F | API_Documentation_Link |
| G | API_Key_Location |
| H | API_Key_Rotation_Frequency |
| I | Last_Key_Rotation |
| J | Next_Key_Rotation |
| K | Authentication_Method |
| L | Authentication_Expiry |
| M | Authentication_Status |
| N | Rate_Limit_Calls |
| O | Rate_Limit_Data |
| P | Current_Usage_Calls |
| Q | Current_Usage_Percentage |
| R | Rate_Limit_Status |
| S | Rate_Limit_Breaches_Last_30_Days |
| T | Last_Successful_Call |
| U | Last_Failed_Call |
| V | Last_Failed_Reason |
| W | Error_Rate_Last_7_Days |
| X | Error_Rate_Last_30_Days |
| Y | Common_Error_Codes |
| Z | API_Health_Status |
| AA | Last_Health_Check |
| AB | Health_Check_Frequency |
| AC | Monitoring_Dashboard |
| AD | Alerting_Enabled |
| AE | Alert_Threshold_Error_Rate |
| AF | Alert_Contacts |
| AG | Retry_Policy |
| AH | Timeout_Setting |
| AI | Pagination_Limit |
| AJ | Max_Concurrent_Requests |
| AK | Integration_Health_Score |
| AL | Last_Integration_Review |
| AM | Next_Integration_Review |
| AN | Notes |

---

## Sheet 31: Metadata

---

**END OF SPECIFICATION**

---

*"An expert is a person who has made all the mistakes that can be made in a very narrow field."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
