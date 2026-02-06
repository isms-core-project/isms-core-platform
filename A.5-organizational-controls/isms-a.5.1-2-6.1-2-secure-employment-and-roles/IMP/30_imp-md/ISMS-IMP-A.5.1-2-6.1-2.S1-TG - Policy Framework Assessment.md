**ISMS-IMP-A.5.1-2-6.1-2.S1-TG - Policy Framework Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.1: Policies for Information Security

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Policy Framework Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.1-2-6.1-2.S1-TG |
| **Related Policy** | ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.1 (Policies for Information Security) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) - Section 4 (Policy Framework Requirements)
- ISMS-IMP-A.5.1-2-6.1-2.S2 (Roles & Responsibilities Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S3 (Screening & Vetting Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S4 (Employment Contract Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S5 (Governance Compliance Dashboard)

**Note on Naming Convention**: The ".S" designation indicates this implementation is part of a **stacked control framework** (A.5.1 + A.5.2 + A.6.1 + A.6.2). Despite unified implementation, each control maintains distinct requirements for Statement of Applicability purposes.

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

# Workbook Technical Specification

## Workbook Metadata

**File Name Convention**: `ISMS-IMP-A.5.1-2-6.1-2.S1_Policy_Framework_YYYYMMDD.xlsx`  
**Example**: `ISMS-IMP-A.5.1-2-6.1-2.S1_Policy_Framework_20260130.xlsx`

**Excel Version Requirements**:

- Microsoft Excel 2016 or later
- Excel for Microsoft 365
- Compatible with LibreOffice Calc 7.0+ (with minor formula adjustments)

**Workbook Properties**:

- **Title**: ISMS-IMP-A.5.1-2-6.1-2.S1 - Policy Framework Assessment
- **Author**: [Organization] Information Security Team
- **Subject**: ISO/IEC 27001:2022 Control A.5.1 Assessment
- **Keywords**: Policy, Governance, ISMS, ISO27001, A.5.1
- **Comments**: Generated via Python script `generate_a5_1_2_6_1_2_s1_policy_framework.py`

**Workbook Settings**:

- **Calculation**: Automatic
- **Iteration**: Enabled (Max 100 iterations, Max change 0.001)
- **Save AutoRecover**: Every 10 minutes
- **Sheet Protection**: Protect formulas, allow data entry in input cells

---

## Sheet 1: Dashboard

**Purpose**: Executive summary dashboard (read-only, auto-calculated)

**Layout**:

**Header Section** (Rows 1-15):

- **Row 1**: Title (A1:K1 merged) "ISMS-IMP-A.5.1-2-6.1-2.S1 — Policy Framework Assessment Dashboard"
  - Font: Arial 18pt Bold, White text, Dark Blue fill (RGB 0, 51, 102)
- **Row 2**: Subtitle (A2:K2 merged) "ISO/IEC 27001:2022 Control A.5.1 - Policies for Information Security"
  - Font: Arial 12pt, White text, Dark Blue fill
- **Rows 4-15**: Document Information Block
  - Labels in Column A (Bold, Gray fill RGB 217, 217, 217)
  - Values in Columns B-C (merged)
  - **Row 4**: Document ID - "ISMS-IMP-A.5.1-2-6.1-2.S1"
  - **Row 5**: Related Policy - "ISMS-POL-A.5.1-2-6.1-2, Section 4"
  - **Row 6**: ISO Control - "A.5.1 (Policies for Information Security)"
  - **Row 7**: Assessment Period - User input (Yellow fill RGB 255, 255, 0)
  - **Row 8**: Assessment Date - `=TODAY()` (auto-updates daily)
  - **Row 9**: Assessor Name - User input (Yellow)
  - **Row 10**: Assessor Role - User input (Yellow)
  - **Row 11**: Organization - User input (Yellow)
  - **Row 12**: Review Cycle - "Quarterly"
  - **Row 13**: Last Updated - `=NOW()` (updates on workbook open/edit)
  - **Row 14**: Assessment Status - Dropdown: Draft / Under-Review / Approved / Audit-Ready (Yellow)
  - **Row 15**: Next Review Date - User input (Yellow)

**Overall Compliance Summary** (Rows 17-30):

- **Row 17**: Section header (A17:K17 merged) "OVERALL POLICY FRAMEWORK COMPLIANCE"
  - Font: Arial 14pt Bold, White text, Dark Blue fill

**Compliance Scorecard** (Rows 19-26):

| Row | Label (Column A) | Value (Column B) | Target (Column C) | Status (Column D) |
|-----|------------------|------------------|-------------------|-------------------|
| 19 | Overall Compliance Score | `=AVERAGE(B32,B33,B34,B35,B36,B37)` | 90% | Conditional formatting |
| 20 | Policies Assessed | `=COUNTA(Policy_Inventory!A:A)-1` | N/A | N/A |
| 21 | Policies Compliant | `=COUNTIF(Lifecycle_Compliance!L:L,"Compliant")` | 100% | Conditional |
| 22 | Policies with Gaps | `=B20-B21` | 0 | Conditional |
| 23 | Critical Gaps | `=COUNTIF(Gap_Analysis!F:F,"Critical")` | 0 | Conditional |
| 24 | High Priority Gaps | `=COUNTIF(Gap_Analysis!F:F,"High")` | 0 | Conditional |
| 25 | Medium Priority Gaps | `=COUNTIF(Gap_Analysis!F:F,"Medium")` | N/A | N/A |
| 26 | Low Priority Gaps | `=COUNTIF(Gap_Analysis!F:F,"Low")` | N/A | N/A |

**Conditional Formatting for Column D (Status)**:

- If B >= C: Green fill (RGB 146, 208, 80), "✓ On Target"
- If B between (C-10%) and C: Yellow fill (RGB 255, 255, 0), "⚠ Close"
- If B < (C-10%): Red fill (RGB 255, 0, 0), "✗ Below Target"

**Domain Compliance Breakdown** (Rows 32-38):

| Row | Domain | Weight | Score (%) | Weighted Score | Status |
|-----|--------|--------|-----------|----------------|--------|
| 32 | Policy Inventory Completeness | 25% | `=COUNTIF(Policy_Inventory!S:S,"No-Gap")/COUNTA(Policy_Inventory!A:A)*100` | `=B32*0.25` | Conditional |
| 33 | Policy Lifecycle Compliance | 25% | `=COUNTIF(Lifecycle_Compliance!L:L,"Compliant")/COUNTA(Lifecycle_Compliance!A:A)*100` | `=B33*0.25` | Conditional |
| 34 | Policy Governance | 20% | `=COUNTIF(Governance_Assessment!M:M,"Compliant")/COUNTA(Governance_Assessment!A:A)*100` | `=B34*0.20` | Conditional |
| 35 | Policy Classification | 10% | `=COUNTIF(Classification_Review!J:J,"Compliant")/COUNTA(Classification_Review!A:A)*100` | `=B35*0.10` | Conditional |
| 36 | Policy Communication | 15% | `=COUNTIF(Communication_Tracking!N:N,"Compliant")/COUNTA(Communication_Tracking!A:A)*100` | `=B36*0.15` | Conditional |
| 37 | Policy Repository | 5% | `=IF(Repository_Assessment!P16="Compliant",100,IF(Repository_Assessment!P16="Partial",50,0))` | `=B37*0.05` | Conditional |
| 38 | **TOTAL WEIGHTED SCORE** | **100%** | **`=SUM(C32:C37)`** | **`=B19`** | **Bold** |

**Key Findings** (Rows 40-60):

**Row 40**: Section header "KEY FINDINGS & PRIORITIES"

**Critical Issues** (Rows 42-47):

- **Row 42**: "Critical Issues (Immediate Action Required):"
- **Rows 43-47**: Top 5 critical gaps (auto-populate from Gap_Analysis sheet, filter Risk_Level="Critical")
  - Formula: `=IFERROR(INDEX(Gap_Analysis!E:E,SMALL(IF(Gap_Analysis!F:F="Critical",ROW(Gap_Analysis!F:F)),ROW(A1))),"None")`
  - Array formula (Ctrl+Shift+Enter in older Excel)

**High Priority Issues** (Rows 49-54):

- **Row 49**: "High Priority Issues (Address Within 60 Days):"
- **Rows 50-54**: Top 5 high-priority gaps (auto-populate, filter Risk_Level="High")

**Overdue Policies** (Rows 56-60):

- **Row 56**: "Policies Overdue for Review:"
- **Rows 57-60**: List policies where Next_Review_Date < TODAY()
  - Formula: `=IFERROR(INDEX(Policy_Inventory!B:B,SMALL(IF(Policy_Inventory!K:K<TODAY(),ROW(Policy_Inventory!K:K)),ROW(A1))),"None")`

**Action Items Summary** (Rows 62-70):

| Row | Label | Value |
|-----|-------|-------|
| 63 | Total Action Items | `=COUNTA(Action_Items!A:A)-1` |
| 64 | Not Started | `=COUNTIF(Action_Items!G:G,"Not-Started")` |
| 65 | In Progress | `=COUNTIF(Action_Items!G:G,"In-Progress")` |
| 66 | Blocked | `=COUNTIF(Action_Items!G:G,"Blocked")` |
| 67 | Completed | `=COUNTIF(Action_Items!G:G,"Completed")` |
| 68 | Accepted Risk | `=COUNTIF(Action_Items!G:G,"Accepted-Risk")` |
| 69 | Overdue Actions (past target date) | `=SUMPRODUCT((Action_Items!F:F<TODAY())*(Action_Items!G:G<>"Completed")*(Action_Items!G:G<>"Accepted-Risk"))` |

**Evidence & Approval Status** (Rows 72-80):

| Row | Label | Value |
|-----|-------|-------|
| 73 | Total Evidence Items | `=COUNTA(Evidence_Register!A:A)-1` |
| 74 | Evidence Verified | `=COUNTIF(Evidence_Register!I:I,"Verified")` |
| 75 | Evidence Pending Verification | `=COUNTIF(Evidence_Register!I:I,"Pending")` |
| 76 | Level 1 Approval (Prepared) | `=IF(Approval_Sign_Off!C5<>"","Complete","Pending")` |
| 77 | Level 2 Approval (Reviewed) | `=IF(Approval_Sign_Off!C15<>"","Complete","Pending")` |
| 78 | Level 3 Approval (CISO Approved) | `=IF(Approval_Sign_Off!C27<>"","Complete","Pending")` |
| 79 | Audit Readiness | `=IF(AND(B19>=90,B23=0,B76="Complete",B77="Complete",B78="Complete"),"Audit Ready","Not Ready")` |

**Column Widths**:

- Column A: 40 (labels)
- Column B: 15 (values)
- Column C: 15 (targets)
- Column D: 15 (status)
- Columns E-K: 5 (spacing)

**Row Heights**:

- Header rows (1-2): 40
- Section headers: 30
- Data rows: 20

**Borders**: Thin black borders around all data blocks

**Sheet Protection**:

- Protect sheet, allow AutoFilter, allow Sorting
- Unlock only user input cells (Yellow highlighted)

---

## Sheet 2: Policy_Inventory

**Purpose**: Master policy inventory with full metadata

**Header** (Rows 1-3):

- **Row 1**: Title (A1:T1 merged) "POLICY INVENTORY"
- **Row 2**: Subtitle (A2:T2 merged) "Master list of all information security policies with metadata"

**Column Headers** (Row 4):

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Policy_ID | 20 | Text | None |
| B | Policy_Title | 35 | Text | None |
| C | Policy_Hierarchy_Tier | 15 | Dropdown | Tier-1-Master / Tier-2-Domain / Tier-3-Topic |
| D | ISO_Control_Mapping | 20 | Text | None |
| E | Policy_Owner | 25 | Text | None |
| F | Policy_Approver | 25 | Text | None |
| G | Current_Version | 12 | Numeric | Format: 0.0 |
| H | Version_Date | 12 | Date | Format: DD.MM.YYYY |
| I | Approval_Date | 12 | Date | Format: DD.MM.YYYY |
| J | Last_Review_Date | 12 | Date | Format: DD.MM.YYYY |
| K | Next_Review_Date | 12 | Date | Format: DD.MM.YYYY |
| L | Review_Frequency | 15 | Dropdown | Annual / Biennial / Quarterly / Triggered-Only |
| M | Policy_Status | 15 | Dropdown | Active / Draft / Under-Review / Retired / Superseded |
| N | Policy_Classification | 15 | Dropdown | Internal / Confidential / Public |
| O | Acknowledgment_Required | 15 | Dropdown | Yes / No / Role-Specific |
| P | Acknowledgment_Rate | 12 | Percentage | Format: 0% (0-100) |
| Q | Repository_Location | 40 | Text | None |
| R | Related_Documents | 30 | Text | None |
| S | Gap_Identified | 15 | Dropdown | No-Gap / Minor-Gap / Significant-Gap / Critical-Gap |
| T | Notes | 40 | Text | None |

**Data Rows**: 5-154 (150 rows for policies)

**Conditional Formatting**:

- **Column K (Next_Review_Date)**:
  - If < TODAY(): Red fill, "Overdue"
  - If between TODAY() and (TODAY()+30): Yellow fill, "Due Soon"
  - If > (TODAY()+30): No fill

- **Column S (Gap_Identified)**:
  - No-Gap: Green fill (RGB 146, 208, 80)
  - Minor-Gap: Yellow fill (RGB 255, 255, 0)
  - Significant-Gap: Orange fill (RGB 255, 192, 0)
  - Critical-Gap: Red fill (RGB 255, 0, 0)

**Data Validation**:

- All dropdown columns: List validation with error alert
- Dates: Date validation, must be valid date
- Acknowledgment_Rate: Integer between 0-100

**Named Ranges**:

- `Policy_ID_List` = Policy_Inventory!$A$5:$A$154 (for cross-sheet references)
- `Policy_Inventory_Data` = Policy_Inventory!$A$5:$T$154

**Formula Cells** (none in this sheet - all manual entry except auto-populated from other sheets)

**Sheet Protection**: Protect, allow data entry, allow AutoFilter, allow Sorting

**Freeze Panes**: Freeze at A5 (keep headers visible)

---

## Sheet 3: Lifecycle_Compliance

**Purpose**: Verify policy lifecycle stage completion

**Header** (Rows 1-3):

- **Row 1**: Title "LIFECYCLE COMPLIANCE ASSESSMENT"
- **Row 2**: Subtitle "Verification of policy creation, approval, publication, review, and update processes"

**Column Headers** (Row 4):

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Policy_ID | 20 | Auto-populate | From Policy_Inventory |
| B | Policy_Title | 35 | Auto-populate | From Policy_Inventory |
| C | Creation_Process_Followed | 20 | Dropdown | Yes / Partial / No / Unknown |
| D | Approval_Valid | 15 | Dropdown | Yes / Partial / No / Expired |
| E | Approval_Documentation | 20 | Dropdown | Complete / Incomplete / Missing |
| F | Publication_Status | 20 | Dropdown | Published / Not-Published / Partially-Accessible |
| G | Review_Schedule_Defined | 20 | Dropdown | Yes / No |
| H | Review_Status | 20 | Formula | Auto-calculate from Next_Review_Date |
| I | Last_Review_Evidence | 20 | Dropdown | Yes / Partial / No |
| J | Version_Control_Practice | 15 | Dropdown | Excellent / Good / Adequate / Poor |
| K | Sunset_Process | 15 | Dropdown | N/A / Yes / No |
| L | Lifecycle_Compliance_Rating | 20 | Formula | Auto-calculate based on C-K |
| M | Gap_Description | 40 | Text | Required if L ≠ "Compliant" |
| N | Evidence_Reference | 30 | Text | None |

**Data Rows**: 5-154 (auto-populate Policy_ID and Policy_Title from Sheet 2)

**Formula: Column A (Policy_ID)**:
```excel
=IF(ROW()-4<=COUNTA(Policy_Inventory!$A:$A)-1,INDEX(Policy_Inventory!$A:$A,ROW()-3),"")
```

**Formula: Column B (Policy_Title)**:
```excel
=IF(A5<>"",VLOOKUP(A5,Policy_Inventory!$A:$B,2,FALSE),"")
```

**Formula: Column H (Review_Status)**:
```excel
=IF(B5="","",
  IF(VLOOKUP(A5,Policy_Inventory!$A:$K,11,FALSE)>=TODAY(),"Current",
    IF(VLOOKUP(A5,Policy_Inventory!$A:$K,11,FALSE)>=TODAY()-30,"Overdue-<30-Days",
      IF(VLOOKUP(A5,Policy_Inventory!$A:$K,11,FALSE)>=TODAY()-90,"Overdue-30-90-Days",
        "Overdue->90-Days"))))
```

**Formula: Column L (Lifecycle_Compliance_Rating)**:
```excel
=IF(B5="","",
  IF(AND(D5="Yes",E5="Complete",F5="Published",OR(H5="Current",H5="Overdue-<30-Days"),I5="Yes",J5<>"Poor"),"Compliant",
    IF(OR(D5="No",D5="Expired",E5="Missing",F5="Not-Published",H5="Overdue->90-Days"),"Non-Compliant",
      "Partial")))
```

**Conditional Formatting**:

- **Column H (Review_Status)**:
  - Current: Green
  - Overdue-<30-Days: Yellow
  - Overdue-30-90-Days: Orange
  - Overdue->90-Days: Red

- **Column L (Lifecycle_Compliance_Rating)**:
  - Compliant: Green
  - Partial: Yellow
  - Non-Compliant: Red

**Sheet Protection**: Protect, unlock manual entry columns (C-G, I-K, M-N)

**Freeze Panes**: A5

---

## Sheet 4: Governance_Assessment

**Header** (Rows 1-3):

- **Row 1**: Title "GOVERNANCE ASSESSMENT"
- **Row 2**: Subtitle "Ownership, accountability, approval authority, and RACI verification"

**Column Headers** (Row 4):

| Col | Header | Width | Data Type | Validation/Formula |
|-----|--------|-------|-----------|-------------------|
| A | Policy_ID | 20 | Auto-populate | From Policy_Inventory |
| B | Policy_Title | 35 | Auto-populate | From Policy_Inventory |
| C | Policy_Hierarchy_Tier | 15 | Auto-populate | From Policy_Inventory |
| D | Owner_Assigned | 15 | Formula | Auto-check if Policy_Owner populated |
| E | Owner_Name_Role | 25 | Auto-populate | From Policy_Inventory |
| F | Owner_Accountability_Clear | 15 | Dropdown | Yes / Unclear / No |
| G | Approver_Assigned | 15 | Formula | Auto-check if Policy_Approver populated |
| H | Approver_Name_Role | 25 | Auto-populate | From Policy_Inventory |
| I | Approval_Authority_Appropriate | 20 | Dropdown | Yes / No / Elevated-Unnecessarily / Insufficient |
| J | RACI_Defined | 15 | Dropdown | Yes / Partial / No / N/A |
| K | Governance_Documentation | 20 | Dropdown | Complete / Partial / Missing |
| L | Escalation_Path_Clear | 15 | Dropdown | Yes / Unclear / No |
| M | Governance_Compliance_Rating | 20 | Formula | Auto-calculate |
| N | Gap_Description | 40 | Text | Required if M ≠ "Compliant" |
| O | Evidence_Reference | 30 | Text | None |

**Formulas**:

**Column D (Owner_Assigned)**:
```excel
=IF(A5="","",IF(VLOOKUP(A5,Policy_Inventory!$A:$E,5,FALSE)<>"","Yes","No"))
```

**Column G (Approver_Assigned)**:
```excel
=IF(A5="","",IF(VLOOKUP(A5,Policy_Inventory!$A:$F,6,FALSE)<>"","Yes","No"))
```

**Column M (Governance_Compliance_Rating)**:
```excel
=IF(B5="","",
  IF(AND(D5="Yes",G5="Yes",I5="Yes",K5="Complete",L5="Yes"),"Compliant",
    IF(OR(D5="No",G5="No",I5="Insufficient",K5="Missing"),"Non-Compliant",
      "Partial")))
```

**Conditional Formatting**:

- Column M (Governance_Compliance_Rating): Green/Yellow/Red

**Sheet Protection**: Protect, unlock manual entry columns (F, I-L, N-O)

**Freeze Panes**: A5

---

## Sheet 5: Classification_Review

**Header** (Rows 1-3):

- **Row 1**: Title "CLASSIFICATION REVIEW"
- **Row 2**: Subtitle "Policy classification appropriateness and access control verification"

**Column Headers** (Row 4):

| Col | Header | Width | Data Type | Validation/Formula |
|-----|--------|-------|-----------|-------------------|
| A | Policy_ID | 20 | Auto-populate | From Policy_Inventory |
| B | Policy_Title | 35 | Auto-populate | From Policy_Inventory |
| C | Current_Classification | 15 | Auto-populate | From Policy_Inventory |
| D | Classification_Appropriate | 20 | Dropdown | Yes / No / Should-Be-Higher / Should-Be-Lower |
| E | Content_Sensitivity_Assessment | 15 | Dropdown | None / Low / Medium / High |
| F | Access_Controls_Implemented | 20 | Dropdown | Yes / Partial / No / Unknown |
| G | Distribution_Restrictions | 20 | Dropdown | Yes / Partial / No / N/A |
| H | Classification_Marking | 15 | Dropdown | Yes / No / Inconsistent |
| I | Classification_Review_Date | 15 | Date | DD.MM.YYYY |
| J | Classification_Compliance_Rating | 20 | Formula | Auto-calculate |
| K | Gap_Description | 40 | Text | Required if J ≠ "Compliant" |
| L | Evidence_Reference | 30 | Text | None |

**Formula: Column J (Classification_Compliance_Rating)**:
```excel
=IF(B5="","",
  IF(AND(D5="Yes",F5="Yes",H5="Yes"),"Compliant",
    IF(OR(D5="No",F5="No",H5="No"),"Non-Compliant",
      "Partial")))
```

**Conditional Formatting**:

- Column J: Green/Yellow/Red

**Sheet Protection**: Protect, unlock manual entry columns (D-I, K-L)

**Freeze Panes**: A5

---

## Sheet 6: Communication_Tracking

**Header** (Rows 1-3):

- **Row 1**: Title "COMMUNICATION TRACKING"
- **Row 2**: Subtitle "Policy publication, acknowledgment, and training integration verification"

**Column Headers** (Row 4):

| Col | Header | Width | Data Type | Validation/Formula |
|-----|--------|-------|-----------|-------------------|
| A | Policy_ID | 20 | Auto-populate | From Policy_Inventory |
| B | Policy_Title | 35 | Auto-populate | From Policy_Inventory |
| C | Acknowledgment_Required | 15 | Auto-populate | From Policy_Inventory |
| D | Target_Audience | 20 | Text | Multiple selection allowed |
| E | Publication_Date | 12 | Date | DD.MM.YYYY |
| F | Publication_Method | 30 | Text | Multiple methods (checkboxes in description) |
| G | Accessibility_Verified | 15 | Dropdown | Yes / Partial / No |
| H | Acknowledgment_Mechanism | 20 | Dropdown | N/A / LMS / Email / E-Signature / Form / Training |
| I | Acknowledgment_Rate | 12 | Auto-populate | From Policy_Inventory (formula) |
| J | Acknowledgment_Timeframe | 15 | Dropdown | N/A / Immediate / 30-Days / 60-Days / 90-Days / Annual |
| K | Non_Acknowledgment_Follow_Up | 20 | Dropdown | Yes / Partial / No / N/A |
| L | Training_Integration | 15 | Dropdown | Yes / Partial / No / N/A |
| M | User_Feedback_Mechanism | 15 | Dropdown | Yes / No |
| N | Communication_Compliance_Rating | 20 | Formula | Auto-calculate |
| O | Gap_Description | 40 | Text | Required if N ≠ "Compliant" |
| P | Evidence_Reference | 30 | Text | None |

**Formula: Column I (Acknowledgment_Rate)**:
```excel
=IF(A5="","",VLOOKUP(A5,Policy_Inventory!$A:$P,16,FALSE))
```

**Formula: Column N (Communication_Compliance_Rating)**:
```excel
=IF(B5="","",
  IF(AND(G5="Yes",OR(C5="No",AND(C5<>"No",I5>=90)),L5<>"No"),"Compliant",
    IF(OR(G5="No",AND(C5<>"No",I5<70)),"Non-Compliant",
      "Partial")))
```

**Conditional Formatting**:

- Column I (Acknowledgment_Rate): 
  - ≥90%: Green
  - 70-89%: Yellow
  - <70%: Red
- Column N: Green/Yellow/Red

**Sheet Protection**: Protect, unlock manual entry (D-H, J-M, O-P)

**Freeze Panes**: A5

---

## Sheet 7: Repository_Assessment

**Purpose**: Assess policy repository as a whole

**Note**: This sheet assesses repository-level attributes, not individual policies

**Header** (Rows 1-3):

- **Row 1**: Title "REPOSITORY ASSESSMENT"
- **Row 2**: Subtitle "Policy repository structure, organization, access, and performance"

**Assessment Questions** (Rows 5-60):

Structure similar to previous sheets but **single assessment** (not per-policy):

| Row | Question | Answer Column | Type |
|-----|----------|---------------|------|
| 5 | Repository_Type | B5 | Dropdown |
| 6 | Repository_URL_Path | B6 | Text |
| 7 | Repository_Organization | B7 | Dropdown |
| 8 | Navigation_Ease | B8 | Dropdown |
| 9 | Search_Functionality | B9 | Dropdown |
| 10 | Version_Control | B10 | Dropdown |
| 11 | Previous_Versions_Accessible | B11 | Dropdown |
| 12 | Access_Control_Implementation | B12 | Dropdown |
| 13 | Access_Logging | B13 | Dropdown |
| 14 | Mobile_Accessibility | B14 | Dropdown |
| 15 | Offline_Access | B15 | Dropdown |
| 16 | Repository_Backup | B16 | Dropdown |
| 17 | Repository_Disaster_Recovery | B17 | Dropdown |
| 18 | Repository_Performance | B18 | Dropdown |
| 19 | Repository_Uptime | B19 | Dropdown |
| 20 | Repository_Compliance_Rating | B20 | Formula |
| 21 | Gap_Description | B21 | Text |
| 22 | Evidence_Reference | B22 | Text |

**Formula: B20 (Repository_Compliance_Rating)**:
```excel
=IF(AND(B7<>"Unorganized",B8<>"Poor",B9<>"None",B10<>"No-Versioning",B12="Yes",B16="Yes"),"Compliant",
  IF(OR(B7="Unorganized",B8="Poor",B10="No-Versioning",B12="No",B16="No"),"Non-Compliant",
    "Partial"))
```

**Conditional Formatting**: B20 (Green/Yellow/Red)

**Sheet Protection**: Protect, unlock manual entry cells (B5-B19, B21-B22)

---

## Sheet 8: Gap_Analysis

**Header** (Rows 1-3):

- **Row 1**: Title "GAP ANALYSIS"
- **Row 2**: Subtitle "Consolidated gaps from all assessment domains with risk levels and remediation plans"

**Column Headers** (Row 4):

| Col | Header | Width | Data Type | Formula/Validation |
|-----|--------|-------|-----------|-------------------|
| A | Gap_ID | 12 | Formula | Auto-generate (GAP-001, GAP-002...) |
| B | Policy_ID | 20 | Auto-populate | From assessment sheets |
| C | Policy_Title | 35 | Auto-populate | Lookup from Policy_Inventory |
| D | Gap_Category | 15 | Auto-populate | Inventory/Lifecycle/Governance/Classification/Communication/Repository |
| E | Gap_Description | 40 | Auto-populate | From assessment sheets |
| F | Risk_Level | 15 | Dropdown | Critical / High / Medium / Low |
| G | Impact_Assessment | 35 | Text | Manual entry |
| H | Affected_Stakeholders | 25 | Text | Manual entry |
| I | Remediation_Action | 40 | Text | Manual entry |
| J | Responsible_Party | 25 | Text | Manual entry |
| K | Target_Completion_Date | 15 | Date | DD.MM.YYYY |
| L | Estimated_Effort | 15 | Dropdown | <1hr / 1-4hrs / 1day / 2-5days / >1week |
| M | Dependencies | 30 | Text | Manual entry |
| N | Status | 15 | Dropdown | Not-Started / In-Progress / Blocked / Completed / Accepted-Risk |
| O | Completion_Evidence | 30 | Text | Required if Status="Completed" |
| P | Risk_Acceptance | 40 | Text | Required if Status="Accepted-Risk" |

**Gap Auto-Population Logic**:

Gaps are pulled from assessment sheets where compliance rating ≠ "Compliant":

- Sheet 2 (Inventory): Column S = "Minor-Gap" or "Significant-Gap" or "Critical-Gap"
- Sheet 3 (Lifecycle): Column L ≠ "Compliant"
- Sheet 4 (Governance): Column M ≠ "Compliant"
- Sheet 5 (Classification): Column J ≠ "Compliant"
- Sheet 6 (Communication): Column N ≠ "Compliant"
- Sheet 7 (Repository): B20 ≠ "Compliant"

**Formula: Column A (Gap_ID)**:
```excel
=IF(ROW()<=4,"",TEXT(ROW()-4,"GAP-000"))
```

**Formula: Column C (Policy_Title)**:
```excel
=IF(B5="","",IF(B5="Repository","Repository-Wide",VLOOKUP(B5,Policy_Inventory!$A:$B,2,FALSE)))
```

**Conditional Formatting**:

- Column F (Risk_Level):
  - Critical: Red fill
  - High: Orange fill
  - Medium: Yellow fill
  - Low: No fill

**Sheet Protection**: Protect, unlock manual entry (F-P)

**Freeze Panes**: A5

---

## Sheet 9: Evidence_Register

**Header** (Rows 1-3):

- **Row 1**: Title "EVIDENCE REGISTER"
- **Row 2**: Subtitle "Documentation of all supporting evidence for policy framework assessment"

**Column Headers** (Row 4):

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Evidence_ID | 12 | Pre-filled | EVD-001 to EVD-100 |
| B | Evidence_Type | 20 | Dropdown | Policy-Document / Approval-Email / Approval-Signature / Meeting-Minutes / Review-Checklist / Repository-Screenshot / Access-Control-Config / Acknowledgment-Report / Training-Records / Version-History / Organizational-Chart / Other |
| C | Description | 40 | Text | None |
| D | Related_Policy_ID | 20 | Text | None (or "All") |
| E | Related_Assessment_Sheet | 20 | Text | None |
| F | File_Location | 40 | Text | None |
| G | Date_Collected | 12 | Date | DD.MM.YYYY |
| H | Collected_By | 25 | Text | None |
| I | Verification_Status | 15 | Dropdown | Verified / Pending / Not-Verified / Expired |
| J | Notes | 40 | Text | None |

**Data Rows**: 5-104 (100 evidence items)

**Formula: Column A (Evidence_ID)**:
```excel
=IF(ROW()<=4,"",TEXT(ROW()-4,"EVD-000"))
```

**Conditional Formatting**:

- Column I (Verification_Status):
  - Verified: Green
  - Pending: Yellow
  - Not-Verified: Orange
  - Expired: Red

**Sheet Protection**: Protect, unlock manual entry (B-J)

**Freeze Panes**: A5

---

## Sheet 10: Action_Items

**Header** (Rows 1-3):

- **Row 1**: Title "ACTION ITEMS"
- **Row 2**: Subtitle "Remediation tracking for identified gaps"

**Column Headers** (Row 4):

| Col | Header | Width | Data Type | Formula/Validation |
|-----|--------|-------|-----------|-------------------|
| A | Action_ID | 12 | Auto-generate | From Gap_ID |
| B | Related_Gap_ID | 12 | Auto-populate | From Gap_Analysis |
| C | Action_Description | 40 | Auto-populate | From Gap_Analysis (Remediation_Action) |
| D | Priority | 15 | Auto-populate | From Gap_Analysis (Risk_Level) |
| E | Owner | 25 | Auto-populate | From Gap_Analysis (Responsible_Party) |
| F | Target_Date | 15 | Auto-populate | From Gap_Analysis (Target_Completion_Date) |
| G | Status | 15 | Auto-populate | From Gap_Analysis (Status) |
| H | Progress_% | 12 | Manual entry | Percentage 0-100% |
| I | Last_Update_Date | 12 | Date | DD.MM.YYYY |
| J | Last_Update_Notes | 35 | Text | None |
| K | Blocking_Issues | 35 | Text | Required if Status="Blocked" |
| L | Escalation_Required | 15 | Dropdown | Yes / No |
| M | Escalation_To | 25 | Text | Required if L="Yes" |

**Data Rows**: Auto-populate from Gap_Analysis sheet

**Formula: Column A (Action_ID)**:
```excel
=IF(Gap_Analysis!A5="","",SUBSTITUTE(Gap_Analysis!A5,"GAP","ACT"))
```

**Conditional Formatting**:

- Column D (Priority): Red/Orange/Yellow (matching risk levels)
- Column F (Target_Date):
  - If < TODAY() AND Status ≠ "Completed": Red (overdue)
  - If between TODAY() and TODAY()+14 AND Status ≠ "Completed": Yellow (due soon)
- Column H (Progress_%):
  - 0-30%: Red
  - 31-70%: Yellow
  - 71-99%: Light green
  - 100%: Dark green

**Sheet Protection**: Protect, unlock manual entry (H-M)

**Freeze Panes**: A5

---

## Sheet 11: Approval_Sign_Off

**Purpose**: Three-level approval workflow

**Layout**:

**Assessment Summary** (Rows 1-20):

- **Row 1**: Title "APPROVAL & SIGN-OFF"
- **Rows 3-20**: Auto-calculated summary metrics
  - Document: ISMS-IMP-A.5.1-2-6.1-2.S1
  - Assessment Period: (from Dashboard)
  - Overall Compliance Score: `=Dashboard!B19`
  - Total Policies: `=Dashboard!B20`
  - Compliant Policies: `=Dashboard!B21`
  - Policies with Gaps: `=Dashboard!B22`
  - Critical Gaps: `=Dashboard!B23`
  - High Priority Gaps: `=Dashboard!B24`
  - Repository Compliance: `=Repository_Assessment!B20`

**Level 1 Approval** (Rows 22-30):

- **Row 22**: Section header "LEVEL 1: PREPARED BY"
- **Row 23**: Name (user input, Yellow)
- **Row 24**: Role (user input, Yellow)
- **Row 25**: Date (user input, Yellow, Date format)
- **Row 26**: Signature (user input, Yellow)
- **Row 27**: Certification checkbox: "I certify this assessment is complete and accurate"
- **Row 28-30**: Comments (user input, text area)

**Level 2 Approval** (Rows 32-45):

- **Row 32**: Section header "LEVEL 2: REVIEWED BY"
- **Row 33**: Name (user input, Yellow)
- **Row 34**: Role (user input, Yellow)
- **Row 35**: Date (user input, Yellow)
- **Row 36**: Signature (user input, Yellow)
- **Rows 37-44**: Review checklist (checkboxes):
  - [ ] Policy inventory complete
  - [ ] Lifecycle compliance verified
  - [ ] Governance gaps identified
  - [ ] Communication assessment thorough
  - [ ] Repository assessment complete
  - [ ] Gap risk levels appropriate
  - [ ] Evidence sufficient
  - [ ] Action items tracked
- **Row 45**: Comments (user input, text area)

**Level 3 Approval** (Rows 47-60):

- **Row 47**: Section header "LEVEL 3: APPROVED BY (CISO)"
- **Row 48**: Name (user input, Yellow)
- **Row 49**: Role (user input, Yellow)
- **Row 50**: Date (user input, Yellow)
- **Row 51**: Signature (user input, Yellow)
- **Row 52**: Final approval statement: "I approve this assessment as accurate"
- **Row 53**: Risk acceptance (if applicable): "I accept residual risk for: [list]"
- **Rows 54-57**: Comments (user input, text area)

**Assessment Metadata** (Rows 59-65):

- **Row 59**: Next Review Date (user input, Yellow, Date)
- **Row 60**: Assessment Status (dropdown: Draft / Under-Review / Approved / Audit-Ready)
- **Row 61-65**: Audit Readiness Checklist (checkboxes):
  - [ ] All three approvals complete
  - [ ] Evidence 100% verified
  - [ ] All critical gaps have remediation plans
  - [ ] Repository compliance verified
  - [ ] Assessment audit-ready

**Sheet Protection**: Protect, unlock approval cells (Yellow highlighted)

---

# Cell Styling Standards

**Consistent across all sheets:**

**User Input Cells**:

- Fill: Yellow (RGB 255, 255, 0)
- Font: Arial 10pt
- Border: Thin black

**Auto-Calculated Cells**:

- Fill: Light Blue (RGB 220, 230, 241)
- Font: Arial 10pt
- Border: Thin black
- Number format: As appropriate (percentage, date, text)

**Labels / Headers**:

- Fill: Gray (RGB 217, 217, 217)
- Font: Arial 10pt Bold
- Border: Thin black

**Section Headers**:

- Fill: Dark Blue (RGB 0, 51, 102)
- Font: Arial 14pt Bold, White text
- Border: None
- Merge cells across full width

**Conditional Formatting Colors**:

- **Green** (Compliant / On Target): RGB 146, 208, 80
- **Yellow** (Partial / Warning): RGB 255, 255, 0
- **Orange** (Moderate Issue): RGB 255, 192, 0
- **Red** (Non-Compliant / Critical): RGB 255, 0, 0

**Borders**:

- Header rows: Medium border bottom
- Data blocks: Thin border around entire block
- Individual cells: Thin border all sides

---

# Freeze Panes & Print Settings

**Freeze Panes**:

- All assessment sheets: Freeze at A5 (keep column headers visible when scrolling)
- Dashboard: No freeze (entire dashboard visible without scroll)

**Print Settings** (for all sheets):

- Orientation: Landscape
- Fit to: 1 page wide by [auto] pages tall
- Margins: Narrow (0.5" all sides)
- Header: Sheet name + Date
- Footer: Page X of Y + File name
- Print titles: Repeat row 4 (column headers) on every page
- Print area: Data range only (exclude empty rows)

---

# Named Ranges Summary

**Workbook-level Named Ranges** (accessible from any sheet):

| Named Range | Reference | Purpose |
|-------------|-----------|---------|
| `Policy_ID_List` | Policy_Inventory!$A$5:$A$154 | Validation list for Policy ID dropdowns |
| `Policy_Inventory_Data` | Policy_Inventory!$A$5:$T$154 | Full policy inventory data range |
| `Gap_List` | Gap_Analysis!$A$5:$P$104 | Full gap analysis data range |
| `Evidence_List` | Evidence_Register!$A$5:$J$104 | Full evidence register data range |
| `Action_Items_List` | Action_Items!$A$5:$M$54 | Full action items data range |

**Usage**: Named ranges used in VLOOKUP, COUNTIF, SUMIF formulas for cleaner syntax

---

# Macro / VBA (Optional)

**Note**: This workbook is designed to function WITHOUT macros for maximum compatibility and security.

**Optional VBA Enhancements** (if organization allows macros):

1. **Auto-Populate Gaps**: Macro to scan assessment sheets and auto-populate Gap_Analysis sheet
2. **Evidence Link Checker**: Macro to verify all evidence file paths are accessible
3. **Dashboard Refresh**: Macro to force dashboard recalculation
4. **Export to PDF**: Macro to export Dashboard and Approval sheets to PDF for distribution

**Macro Naming Convention**: `ISMS_PolicyFramework_[MacroName]`

**Macro Security**: All macros digitally signed by organization

---

# File Naming & Version Control

**File Naming Convention**:
```
ISMS-IMP-A.5.1-2-6.1-2.S1_Policy_Framework_YYYYMMDD.xlsx
```

**Components**:

- `ISMS-IMP`: Implementation specification
- `A.5.1-2-6.1-2`: Stacked controls (A.5.1 + A.5.2 + A.6.1 + A.6.2)
- `.S1`: First assessment in stacked control suite
- `Policy_Framework`: Assessment domain
- `YYYYMMDD`: Assessment date (e.g., 20260130)
- `.xlsx`: Excel file extension

**Version Control**:

- Date in filename serves as version identifier
- Previous assessments archived with date suffix
- Repository: Store in version-controlled location (SharePoint, Git, DMS)

**Example File History**:
```
ISMS-IMP-A.5.1-2-6.1-2.S1_Policy_Framework_20260130.xlsx (current)
ISMS-IMP-A.5.1-2-6.1-2.S1_Policy_Framework_20251031.xlsx (Q4 2025)
ISMS-IMP-A.5.1-2-6.1-2.S1_Policy_Framework_20250731.xlsx (Q3 2025)
```

---

# Integration with Python Script

**Generator Script**: `generate_a5_1_2_6_1_2_s1_policy_framework.py`

**Script Responsibilities**:
1. Create workbook with 11 sheets
2. Apply all formatting (colors, fonts, borders)
3. Write all headers and labels
4. Create all data validation rules
5. Write all formulas
6. Apply conditional formatting
7. Create named ranges
8. Set print settings
9. Protect sheets
10. Set freeze panes
11. Save workbook with correct filename

**Script does NOT**:

- Populate data (user's responsibility)
- Create macros (optional enhancement)
- Require external dependencies beyond `openpyxl`

**Script Execution**:
```bash
python generate_a5_1_2_6_1_2_s1_policy_framework.py
```

**Output**:
```
ISMS-IMP-A.5.1-2-6.1-2.S1_Policy_Framework_20260130.xlsx
```

---

# Quality Assurance Checklist

**For Script Developers / Reviewers**:

## Workbook Structure

- [ ] 11 sheets created with correct names
- [ ] Sheet tab colors assigned (if applicable)
- [ ] Sheet order correct (Dashboard first, Approval last)

## Formatting

- [ ] All headers formatted (Dark Blue background, White text, Bold)
- [ ] User input cells highlighted (Yellow fill)
- [ ] Auto-calculated cells highlighted (Light Blue fill)
- [ ] Labels formatted (Gray fill, Bold)
- [ ] Borders applied consistently

## Data Validation

- [ ] All dropdown fields have validation lists
- [ ] Date fields have date validation
- [ ] Percentage fields have numeric validation (0-100)
- [ ] Error alerts configured for invalid entries

## Formulas

- [ ] All auto-calculate fields have correct formulas
- [ ] VLOOKUP formulas reference correct ranges
- [ ] Conditional formulas (IF, AND, OR) logic correct
- [ ] Dashboard metrics formulas accurate
- [ ] No #REF!, #VALUE!, #DIV/0! errors in empty workbook

## Conditional Formatting

- [ ] Compliance rating cells (Green/Yellow/Red)
- [ ] Date-based formatting (overdue dates)
- [ ] Risk level formatting (Critical/High/Medium/Low)
- [ ] Percentage thresholds correct

## Named Ranges

- [ ] All named ranges created
- [ ] Named range references correct
- [ ] Named ranges used in formulas where appropriate

## Sheet Protection

- [ ] All sheets protected
- [ ] User input cells unlocked
- [ ] AutoFilter and Sorting allowed
- [ ] Protection password set (if required)

## Freeze Panes

- [ ] Dashboard: No freeze
- [ ] All other sheets: Freeze at A5

## Print Settings

- [ ] Orientation: Landscape
- [ ] Fit to 1 page wide
- [ ] Headers/footers configured
- [ ] Print titles set (row 4 repeat)

## File Properties

- [ ] Workbook title set
- [ ] Author set to organization
- [ ] Subject and keywords populated
- [ ] Comments include generator script name

## Testing

- [ ] Open workbook - no errors
- [ ] Enter sample data - formulas calculate correctly
- [ ] Test data validation - invalid entries rejected
- [ ] Test conditional formatting - colors apply correctly
- [ ] Test freeze panes - headers stay visible
- [ ] Test print preview - layout correct

---

# Maintenance & Updates

**When to Update This Specification**:

- ISMS-POL-A.5.1-2-6.1-2 policy updated (new requirements)
- ISO 27001 standard revised
- Assessment methodology improved based on lessons learned
- User feedback identifies confusing sections
- Excel best practices evolve

**Version Control for This Document**:

- Document version: 1.0 (Initial)
- Update version number when substantive changes made
- Document changes in Version History table

**Backward Compatibility**:

- Major version changes (2.0): May break compatibility with old assessments
- Minor version changes (1.1): Maintain backward compatibility
- Migration guide provided for major version changes

---

**END OF SPECIFICATION**

---

*"Policy is the architecture of accountability."*
— Anonymous

<!-- QA_VERIFIED: 2026-02-06 -->
