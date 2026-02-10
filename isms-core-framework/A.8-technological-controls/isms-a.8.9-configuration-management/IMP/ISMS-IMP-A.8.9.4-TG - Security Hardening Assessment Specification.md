<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.9.4-TG:framework:TG:a.8.9.4 -->
**ISMS-IMP-A.8.9.4-TG - Security Hardening Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.9: Configuration Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.9.4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Security Hardening and Compliance - Hardening Standards Selection, Implementation, Compliance Verification, Gap Remediation |
| **Related Policy** | ISMS-POL-A.8.9, Section 2.5 (Security Hardening & Compliance) |
| **Purpose** | Assess implementation of security hardening standards (CIS Benchmarks, DISA STIGs, vendor guides), compliance verification processes, gap analysis, and remediation tracking across all asset types |
| **Target Audience** | Security Architect, Security Engineers, System Administrators, Configuration Manager, Compliance Officers, IT Operations, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Security Hardening assessment workbook | ISMS Implementation Team |

---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a89_4_hardening.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.9.4` |
| **Output Filename** | `ISMS-IMP-A.8.9.4_Hardening_YYYYMMDD.xlsx` |
| **Total Sheets** | 11 (11 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.9: Configuration Management |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #375623 | 375623 | Custom |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #70AD47 | 70AD47 | Medium Green (On Track) |
| #8B0000 | 8B0000 | Dark Red (Critical) |
| #C00000 | C00000 | Dark Red (Blocked) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D6EAF8 | D6EAF8 | Custom |
| #D8E4F8 | D8E4F8 | Pale Blue (Sub-section) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #ED7D31 | ED7D31 | Custom |
| #FCE4D6 | FCE4D6 | Peach (Warning Alt) |
| #FFC000 | FFC000 | Custom |
| #FFE6E6 | FFE6E6 | Custom |
| #FFF2CC | FFF2CC | Cream (Input Alt) |

## Sheet 1: Instructions

---

## Sheet 2: Hardening_Standard_Register

**Data Rows:** 30 (rows 2–31)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Standard_ID | 12 |
| B | Standard_Name | 35 |
| C | Standard_Category | 25 |
| D | Standard_Version | 15 |
| E | Issuing_Authority | 25 |
| F | Applicability_Scope | 30 |
| G | Compliance_Level | 15 |
| H | Mandatory_Optional | 18 |
| I | Regulatory_Driver | 25 |
| J | Control_Count | 14 |
| K | Implementation_Target | 18 |
| L | Review_Frequency | 18 |
| M | Last_Review_Date | 18 |
| N | Next_Review_Date | 18 |
| O | Standard_Owner | 25 |
| P | Documentation_Location | 30 |
| Q | Notes | 40 |
| R | Status | 12 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| N2:N31 | lessThan TODAY() |  |
| N2:N31 | between TODAY() |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{row}<>` |  |

---

## Sheet 3: Asset_Type_Hardening_Matrix

**Purpose:** This matrix maps hardening standards (columns) to asset types (rows),

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| N2:NN | equal  |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| NN | `=COUNTIF(B{row}:{get_column_letter(NUM_STANDARDS+1)}{row},` |  |
| NN | `={req_col}{row}+{rec_col}{row}` |  |
| NN | `=IF({req_col}{row}>5,` |  |

---

## Sheet 4: Asset_Hardening_Assessment

**Purpose:** This sheet documents hardening compliance status for individual assets.

**Data Rows:** 100 (rows 2–101)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Asset_ID | 12 |
| B | Asset_Name | 30 |
| C | Asset_Type | 25 |
| D | Asset_Tier | 12 |
| E | Asset_Owner | 25 |
| F | Location | 20 |
| G | Operating_System | 25 |
| H | Applicable_Standards | 25 |
| I | Standards_Count | 15 |
| J | Total_Controls | 14 |
| K | Implemented_Controls | 18 |
| L | Partial_Controls | 14 |
| M | Not_Implemented_Controls | 22 |
| N | Not_Applicable_Controls | 22 |
| O | Compliance_Percentage | 18 |
| P | High_Risk_Gaps | 14 |
| Q | Medium_Risk_Gaps | 16 |
| R | Low_Risk_Gaps | 14 |
| S | Active_Exceptions | 16 |
| T | Compensating_Controls | 22 |
| U | Compliance_Status | 20 |
| V | Last_Assessment_Date | 18 |
| W | Next_Assessment_Date | 18 |
| X | Assessor | 25 |
| Y | Evidence_Reference | 20 |
| Z | Remediation_Status | 18 |
| AA | Target_Compliance_Date | 20 |
| AB | Notes | 40 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| P2:P101 | greaterThan 0 |  |
| W2:W101 | lessThan TODAY() |  |
| W2:W101 | between TODAY() |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| ON | `=IF(AND(J{row}>0,(J{row}-N{row})>0), ` |  |
| WN | `=IF(V{row}<>` |  |

---

## Sheet 5: Control_Compliance_Detail

**Purpose:** This sheet provides control-level detail for hardening assessments.

**Data Rows:** 500 (rows 2–501)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Control_ID | 12 |
| B | Asset_ID | 12 |
| C | Asset_Name | 25 |
| D | Standard_ID | 12 |
| E | Standard_Name | 30 |
| F | Control_Number | 12 |
| G | Control_Title | 35 |
| H | Control_Description | 50 |
| I | Control_Category | 18 |
| J | Control_Severity | 15 |
| K | Implementation_Status | 18 |
| L | Implementation_Method | 18 |
| M | Implementation_Evidence | 40 |
| N | Configuration_Setting | 30 |
| O | Expected_Value | 25 |
| P | Actual_Value | 25 |
| Q | Compliance_Status | 16 |
| R | Gap_Description | 40 |
| S | Gap_Risk_Rating | 15 |
| T | Remediation_Required | 18 |
| U | Remediation_Plan | 40 |
| V | Remediation_Owner | 25 |
| W | Target_Remediation_Date | 20 |
| X | Exception_Status | 16 |
| Y | Exception_ID | 12 |
| Z | Compensating_Control | 40 |
| AA | Last_Verified_Date | 18 |
| AB | Verified_By | 25 |
| AC | Evidence_Reference | 20 |
| AD | Verification_Method | 20 |
| AE | Next_Verification_Date | 20 |
| AF | Notes | 40 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{row}<>` |  |
| AEN | `=IF(AA{row}<>` |  |

---

## Sheet 6: Exception_Management

**Purpose:** This sheet documents and tracks approved deviations from hardening requirements.

**Data Rows:** 50 (rows 2–51)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Exception_ID | 12 |
| B | Control_ID | 12 |
| C | Asset_ID | 12 |
| D | Asset_Name | 25 |
| E | Standard_ID | 12 |
| F | Control_Number | 12 |
| G | Control_Title | 30 |
| H | Control_Severity | 15 |
| I | Exception_Type | 20 |
| J | Exception_Reason | 40 |
| K | Business_Justification | 40 |
| L | Risk_Assessment | 40 |
| M | Residual_Risk_Rating | 18 |
| N | Compensating_Control_Required | 25 |
| O | Compensating_Control_Description | 40 |
| P | Compensating_Control_Effectiveness | 25 |
| Q | Requested_By | 25 |
| R | Request_Date | 15 |
| S | Reviewed_By | 25 |
| T | Review_Date | 15 |
| U | Approved_By | 25 |
| V | Approval_Date | 15 |
| W | Exception_Status | 18 |
| X | Exception_Duration | 18 |
| Y | Valid_From_Date | 15 |
| Z | Valid_Until_Date | 15 |
| AA | Days_Until_Expiry | 16 |
| AB | Review_Required | 18 |
| AC | Last_Review_Date | 15 |
| AD | Next_Review_Date | 15 |
| AE | Audit_Trail | 40 |
| AF | Monitoring_Required | 18 |
| AG | Monitoring_Description | 40 |
| AH | Re_Assessment_Trigger | 40 |
| AI | Exception_Closure_Plan | 40 |
| AJ | Documentation_Reference | 30 |
| AK | Notes | 40 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| AA2:AA51 | lessThan 0 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{row}<>` |  |
| AAN | `=IF(Z{row}<>` |  |

---

## Sheet 7: Remediation_Tracking

**Purpose:** This sheet tracks remediation activities for identified hardening gaps.

**Data Rows:** 100 (rows 2–101)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Remediation_ID | 12 |
| B | Gap_Type | 18 |
| C | Control_ID | 12 |
| D | Asset_ID | 12 |
| E | Asset_Name | 25 |
| F | Asset_Tier | 12 |
| G | Standard_ID | 12 |
| H | Control_Number | 12 |
| I | Control_Title | 30 |
| J | Control_Severity | 15 |
| K | Gap_Description | 40 |
| L | Gap_Risk_Rating | 15 |
| M | Impact_Assessment | 40 |
| N | Discovery_Date | 15 |
| O | Discovery_Method | 20 |
| P | Remediation_Required | 18 |
| Q | Remediation_Strategy | 20 |
| R | Remediation_Description | 40 |
| S | Remediation_Owner | 25 |
| T | Remediation_Team | 25 |
| U | Estimated_Effort | 15 |
| V | Estimated_Cost | 15 |
| W | Dependencies | 30 |
| X | Remediation_Priority | 18 |
| Y | Target_Start_Date | 15 |
| Z | Target_Completion_Date | 20 |
| AA | Actual_Start_Date | 15 |
| AB | Actual_Completion_Date | 20 |
| AC | Days_To_Remediate | 16 |
| AD | Days_Overdue | 14 |
| AE | Status | 18 |
| AF | Status_Notes | 40 |
| AG | Completion_Percentage | 18 |
| AH | Blocker_Description | 40 |
| AI | Verification_Required | 18 |
| AJ | Verification_Method | 20 |
| AK | Verified_By | 25 |
| AL | Verification_Date | 15 |
| AM | Verification_Result | 18 |
| AN | Re_Test_Required | 15 |
| AO | Change_Request_ID | 18 |
| AP | Risk_Acceptance_ID | 18 |
| AQ | Evidence_Reference | 20 |
| AR | Lessons_Learned | 40 |
| AS | Preventive_Action | 40 |
| AT | Closure_Date | 15 |
| AU | Approved_By | 25 |
| AV | Notes | 40 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| AD2:AD101 | greaterThan 0 |  |
| AD2:AD101 | greaterThan 7 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{row}<>` |  |
| ACN | `=IF(AND(AA{row}<>` |  |

---

## Sheet 8: Compliance_Dashboard

**Purpose:** This sheet provides executive-level summary of hardening posture.

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| B5 | between 0.90 |  |
| B5 | lessThan 0.90 |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=AVERAGE(Asset_Hardening_Assessment!O:O)` |  |
| BN | `=COUNTA(Asset_Hardening_Assessment!A:A)-1` |  |
| BN | `=COUNTIF(Asset_Hardening_Assessment!U:U,` |  |
| DN | `=B{row}/B{row-1}` |  |
| BN | `=SUM(Asset_Hardening_Assessment!J:J)` |  |
| BN | `=SUM(Asset_Hardening_Assessment!K:K)` |  |
| BN | `=SUM(Asset_Hardening_Assessment!M:M)` |  |
| BN | `=SUM(Asset_Hardening_Assessment!P:P)` |  |
| BN | `=COUNTIF(Exception_Management!W:W,` |  |
| DN | `=B{row-8}*0.05` | <5% of controls |
| BN | `=COUNTIFS(Remediation_Tracking!AE:AE,` |  |
| BN | `=COUNTIF(Asset_Hardening_Assessment!D:D,` |  |
| CN | `=AVERAGEIF(Asset_Hardening_Assessment!D:D,` |  |
| BN | `=COUNTA(Remediation_Tracking!A:A)-1` |  |
| BN | `=IF(B{row-2}>0, B{row-1}/B{row-2}, ` |  |
| BN | `=AVERAGE(Remediation_Tracking!AC:AC)` |  |
| BN | `=COUNTIF(Remediation_Tracking!AD:AD,` |  |
| BN | `=COUNTIF(Remediation_Tracking!AE:AE,` |  |
| BN | `=COUNTIFS(Remediation_Tracking!L:L,` |  |
| BN | `=COUNTIFS(Exception_Management!N:N,` |  |

---

## Sheet 9: Gap_Prioritization

**Purpose:** This sheet provides risk-based prioritization of all hardening gaps.

**Data Rows:** 100 (rows 2–101)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Priority_Rank | 12 |
| B | Remediation_ID | 14 |
| C | Asset_ID | 12 |
| D | Asset_Name | 25 |
| E | Asset_Tier | 12 |
| F | Control_ID | 12 |
| G | Control_Number | 14 |
| H | Control_Title | 30 |
| I | Standard_ID | 12 |
| J | Control_Severity | 15 |
| K | Gap_Risk_Rating | 15 |
| L | Gap_Description | 40 |
| M | Exploitation_Likelihood | 20 |
| N | Impact_Assessment | 35 |
| O | Risk_Score | 12 |
| P | Priority_Category | 18 |
| Q | Remediation_Owner | 25 |
| R | Estimated_Effort | 15 |
| S | Target_Completion_Date | 20 |
| T | Days_Until_Target | 16 |
| U | Status | 18 |
| V | Dependencies | 30 |
| W | Quick_Win | 15 |
| X | Related_Gaps | 25 |
| Y | Batch_Opportunity | 25 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| P2:P101 | equal  | Fill: #8B0000 (Dark Red (Critical)) |
| P2:P101 | equal  |  |
| P2:P101 | equal  |  |
| P2:P101 | equal  |  |
| T2:T101 | lessThan 0 |  |
| U2:U101 | equal  |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=Remediation_Tracking!A{row}` |  |
| CN | `=Remediation_Tracking!D{row}` |  |
| DN | `=Remediation_Tracking!E{row}` |  |
| EN | `=Remediation_Tracking!F{row}` |  |
| FN | `=Remediation_Tracking!C{row}` |  |
| GN | `=Remediation_Tracking!H{row}` |  |
| HN | `=Remediation_Tracking!I{row}` |  |
| IN | `=Remediation_Tracking!G{row}` |  |
| JN | `=Remediation_Tracking!J{row}` |  |
| KN | `=Remediation_Tracking!L{row}` |  |
| LN | `=Remediation_Tracking!K{row}` |  |
| NN | `=Remediation_Tracking!M{row}` |  |
| QN | `=Remediation_Tracking!S{row}` |  |
| RN | `=Remediation_Tracking!U{row}` |  |
| SN | `=Remediation_Tracking!Z{row}` |  |
| UN | `=Remediation_Tracking!AE{row}` |  |
| VN | `=Remediation_Tracking!W{row}` |  |
| TN | `=IF(S{row}<>` |  |
| AN | `=IF(B{row}<>` |  |

---

## Sheet 10: Evidence_Register

**Purpose:** This sheet provides centralized evidence management.

**Data Rows:** 100 (rows 2–101)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence_ID | 12 |
| B | Evidence_Type | 25 |
| C | Related_Control_ID | 14 |
| D | Related_Asset_ID | 14 |
| E | Related_Exception_ID | 14 |
| F | Evidence_Description | 50 |
| G | Evidence_Source | 20 |
| H | Collection_Method | 20 |
| I | Collection_Date | 15 |
| J | Collected_By | 25 |
| K | File_Name | 30 |
| L | File_Location | 40 |
| M | File_Hash | 65 |
| N | Evidence_Validity_Period | 20 |
| O | Evidence_Expiry_Date | 18 |
| P | Review_Required | 18 |
| Q | Evidence_Status | 15 |
| R | Verification_By | 25 |
| S | Verification_Date | 15 |
| T | Audit_Trail | 40 |
| U | Notes | 40 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| Q2:Q101 | equal  |  |
| Q2:Q101 | equal  |  |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{row}<>` |  |

---

## Sheet 11: Approval_Sign_Off

**Purpose:** This sheet documents formal approval of the assessment.

**Data Rows:** 8 (rows 6–13)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Asset_Hardening_Assessment!A:A)-1` | Number of Assets Assessed |
| — | `=COUNTA(Hardening_Standard_Register!A:A)-1` | Number of Standards Applied |

---

**END OF SPECIFICATION**

---

*"The more we study the major problems of our time, the more we come to realize that they cannot be understood in isolation."*
— Fritjof Capra

<!-- QA_VERIFIED: 2026-02-06 -->
