**ISMS-IMP-A.5.1-2-6.1-2.S3-TG - Screening & Vetting Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.1: Screening

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Screening & Vetting Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.1-2-6.1-2.S3-TG |
| **Related Policy** | ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.6.1 (Screening) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO / Chief Human Resources Officer (CHRO) — joint ownership |
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
- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) — Section 6 (Screening & Vetting Requirements)
- ISMS-IMP-A.5.1-2-6.1-2.S1 (Policy Framework Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S2 (Roles & Responsibilities Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S4 (Employment Contract Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S5 (Governance Compliance Dashboard)
- Swiss Federal Data Protection Act (FADP / nDSG) — Articles 4, 6, 7, 22, 25
- Swiss Code of Obligations (OR) — Article 328b

**Note on Naming Convention**: The ".S" designation indicates this implementation is part of a **stacked control framework** (A.5.1 + A.5.2 + A.6.1 + A.6.2). Despite unified implementation, each control maintains distinct requirements for Statement of Applicability purposes.

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## 9. Workbook Technical Specification

### 9.1 Workbook Metadata

**File Name Convention:** `ISMS-IMP-A.5.1-2-6.1-2.S3_Screening_Vetting_YYYYMMDD.xlsx`
**Example:** `ISMS-IMP-A.5.1-2-6.1-2.S3_Screening_Vetting_20260130.xlsx`

**Excel Version Requirements:**
- Microsoft Excel 2016 or later
- Excel for Microsoft 365
- Compatible with LibreOffice Calc 7.0+

**Workbook Properties:**
- **Title**: ISMS-IMP-A.5.1-2-6.1-2.S3 — Screening & Vetting Assessment
- **Author**: [Organization] Information Security Team
- **Subject**: ISO/IEC 27001:2022 Control A.6.1 Assessment
- **Keywords**: Screening, Vetting, Personnel, Pre-Employment, FADP, ISMS, ISO27001, A.6.1
- **Comments**: Generated via Python script `generate_a5_1_2_6_1_2_s3_screening_vetting.py`

**Workbook Settings:**
- Calculation: Automatic
- Sheet Protection: Protect formulas, allow data entry in input cells
- Save AutoRecover: Every 10 minutes

---

### 9.2 Sheet Structure Summary

| Sheet # | Sheet Name | Row Count | Input Cells | Formula Cells | Dropdowns |
|---------|------------|-----------|-------------|---------------|-----------|
| 1 | Dashboard | 80 | 6 | 35+ | 1 |
| 2 | Screening_Process_Assessment | 30 | 18 | 3 | 18 |
| 3 | Screening_Level_Matrix | 60 | 40+ | 15 | 8 |
| 4 | Personnel_Screening_Registry | 154 | 1,200+ | 450 | 7 |
| 5 | Screening_Compliance_Verification | 154 | 150 | 1,200+ | 0 |
| 6 | Continuous_Screening_Assessment | 154 | 600+ | 450 | 5 |
| 7 | Legal_Compliance_Review | 35 | 22 | 3 | 22 |
| 8 | Gap_Analysis | 84 | 640 | 80 | 5 |
| 9 | Evidence_Register | 84 | 640 | 80 | 2 |
| 10 | Approval_Sign_Off | 72 | 25 | 15 | 2 |

**Total Estimated Lines in Python Script:** ~950 lines

---

### 9.3 Color Scheme & Styling

**Consistent with .S1 and .S2:**

| Element | Fill Color | Font | Notes |
|---------|-----------|------|-------|
| User Input Cells | Yellow (FFFF00) | Arial 10pt | Editable by user |
| Auto-Calculated Cells | Light Blue (DCE6F1) | Arial 10pt | Formula cells — protected |
| Labels / Headers | Gray (D9D9D9) | Arial 10pt Bold | Static labels |
| Main Title | Dark Blue (003366) | Arial 18pt Bold White | Sheet header |
| Sub-Header | Dark Blue (003366) | Arial 12pt White | Section headers |
| Column Headers | Gray (D9D9D9) | Arial 10pt Bold | Table column headers |

**Conditional Formatting — Status Fields:**
| Value | Fill Color | Font Color |
|-------|-----------|------------|
| Compliant | Green (92D050) | Black |
| Partial | Yellow (FFFF00) | Black |
| Non-Compliant | Red (FF0000) | White |
| Current | Green (92D050) | Black |
| Due-Soon | Yellow (FFFF00) | Black |
| Overdue-<90-Days | Orange (FFC000) | Black |
| Overdue->90-Days | Red (FF0000) | White |
| Critical (Risk) | Red (FF0000) | White |
| High (Risk) | Orange (FFC000) | Black |
| Medium (Risk) | Yellow (FFFF00) | Black |
| Low (Risk) | Light Green (C6EFCE) | Black |

**Special Styling — Criminal Check Data Cells:**
- Criminal_Check_Completed column (Sheet 4, Col O): Light purple fill (E2D4F0) to visually distinguish sensitive data fields
- This draws assessor attention to the consent requirement

---

### 9.4 Key Formula Patterns

**Required Screening Level from Level Matrix with Override Check (Sheet 4, Col I):**
```excel
=IF(A5="","",IF(COUNTIF(Screening_Level_Matrix!$B$24:$B$53,C5)>0,
  INDEX(Screening_Level_Matrix!$F$24:$F$53,MATCH(C5,Screening_Level_Matrix!$B$24:$B$53,0)),
  INDEX(Screening_Level_Matrix!$C$5:$C$10,MATCH(E5,Screening_Level_Matrix!$A$5:$A$10,0))))
```
Logic: If the Role_ID has an override in Section C of the Level Matrix, use the override level. Otherwise, look up the standard level for the role's tier.

**Screening Compliance Rating (Sheet 4, Col Q):**
```excel
=IF(B5="","",IF(AND(M5="Yes",P5="Yes",
  IF(OR(I5="Level-2-Standard",I5="Level-3-Enhanced",I5="Level-4-Comprehensive"),N5="Yes",TRUE),
  IF(OR(I5="Level-3-Enhanced",I5="Level-4-Comprehensive"),O5="Yes",TRUE),
  L5="Yes"),
"Compliant",
  IF(OR(M5="No",P5="No",
    AND(OR(I5="Level-3-Enhanced",I5="Level-4-Comprehensive"),O5="No")),
  "Non-Compliant","Partial")))
```

**References Required (Sheet 5, Col F):**
```excel
=IF(C5="","",IF(OR(C5="Level-2-Standard",C5="Level-3-Enhanced",C5="Level-4-Comprehensive"),"Yes","N/A"))
```

**Criminal Required (Sheet 5, Col H):**
```excel
=IF(C5="","",IF(OR(C5="Level-3-Enhanced",C5="Level-4-Comprehensive"),"Yes","N/A"))
```

**Missing Checks (Sheet 5, Col M):**
```excel
=IF(B5="","",IF(AND(E5="Yes",IF(F5="Yes",G5="Yes",TRUE),IF(H5="Yes",I5="Yes",TRUE),K5="Yes"),"None","Missing: "&IF(E5<>"Yes","Identity ","")&IF(AND(F5="Yes",G5<>"Yes"),"References ","")&IF(AND(H5="Yes",I5<>"Yes"),"Criminal ","")&IF(K5<>"Yes","CV ","")))
```

**Next Re-Screening Due (Sheet 6, Col G):**
```excel
=IF(F5="","",IF(E5="Annual",EDATE(F5,12),IF(E5="Biennial",EDATE(F5,24),"")))
```

**Re-Screening Status (Sheet 6, Col H):**
```excel
=IF(G5="","N/A",IF(G5>=TODAY(),"Current",IF(G5>=TODAY()-30,"Due-Soon",IF(G5>=TODAY()-90,"Overdue-<90-Days","Overdue->90-Days"))))
```

**Process Compliance Rating (Sheet 2, Q23):**
```excel
=IF(AND(B5="Yes",B9="Yes",B10="Yes",B14="Yes",B17="Yes",B19="Yes",B20="Yes",B21="Yes",B22="Yes"),"Compliant",IF(OR(B5="No",B17="No",B19="No",B20="No",B21="No"),"Non-Compliant","Partial"))
```

**Legal Compliance Rating (Sheet 7, Q29):**
```excel
=IF(AND(B1="Yes",B2="Yes",B4<>"No",B6="Yes",B8="Yes",B18="Yes",B19="Yes"),"Compliant",IF(OR(AND(B4="No",B19<>"N/A"),B6="No",B8="No",B18="No",B19="No"),"Non-Compliant","Partial"))
```

**Dashboard Overall Score:**
```excel
=B30*0.20 + B31*0.15 + B32*0.30 + B33*0.20 + B34*0.15
```
Where B30–B34 are the five domain compliance scores (0–100 scale).

---

### 9.5 Data Validation Rules

**Sheet 2 (Screening_Process_Assessment):**
- All Yes/No questions: `List: Yes,No`
- Process_Review_Status: `List: Current,Overdue-<6-Months,Overdue->6-Months`
- Integration_with_Recruitment: `List: Yes,Partial,No`
- Screening_Results_Retention: `List: Yes,No,Unknown`

**Sheet 3 (Screening_Level_Matrix):**
- Screening_Level_Justified: `List: Yes,No,Requires-Review`
- Override_Level: `List: Level-1-Basic,Level-2-Standard,Level-3-Enhanced,Level-4-Comprehensive`
- Override_Compliance: `List: Compliant,Non-Compliant`

**Sheet 4 (Personnel_Screening_Registry):**
- Employment_Type: `List: Full-Time,Part-Time,Contractor,Consultant`
- Screening_Completed: `List: Yes,Partial,No`
- Screening_Before_Start: `List: Yes,No,Grace-Period`
- Identity_Verified: `List: Yes,No`
- References_Completed: `List: Yes,No,N/A`
- Criminal_Check_Completed: `List: Yes,No,N/A,Consent-Pending`
- CV_Verified: `List: Yes,No`

**Sheet 6 (Continuous_Screening_Assessment):**
- Re_Screening_Required: `List: Yes,No`
- Re_Screening_Frequency: `List: Annual,Biennial,Role-Change-Only,Not-Required`
- Event_Trigger_Required: `List: Yes,No`
- Event_Triggers_Occurred: `List: Yes,No,N/A`
- Event_Triggered_Re_Screening_Done: `List: Yes,No,N/A`

**Sheet 7 (Legal_Compliance_Review):**
- All Yes/No/N/A questions: `List: Yes,No,N/A` (where N/A applies)
- Consent_Voluntary: `List: Yes,Unclear,No`
- Notice_Covers_Required_Elements: `List: Yes,Partial,No`

**Sheet 8 (Gap_Analysis):**
- Source_Sheet: `List: Process,Level-Matrix,Registry,Compliance,Continuous,Legal`
- Gap_Category: `List: Process-Gap,Level-Gap,Screening-Gap,Re-Screening-Gap,Legal-Gap`
- Risk_Level: `List: Critical,High,Medium,Low`
- Estimated_Effort: `List: <1hr,1-4hrs,1day,2-5days,>1week`
- Status: `List: Not-Started,In-Progress,Blocked,Completed,Accepted-Risk`

**Sheet 9 (Evidence_Register):**
- Evidence_Type: `List: Screening-Process-Document,Consent-Form,Privacy-Notice,Criminal-Check-Report,Reference-Check-Report,Identity-Verification-Document,CV-Verification-Record,Re-Screening-Record,DPIA-Document,DPO-Sign-Off,Screening-Provider-Contract,Screening-Provider-DPA,Access-Control-Report,Audit-Log,Screening-Exemption-Approval,Other`
- Verification_Status: `List: Verified,Pending,Not-Verified,Expired`

**Sheet 10 (Approval_Sign_Off):**
- Assessment_Status: `List: Draft,Under-Review,Approved,Audit-Ready`

---

### 9.6 Named Ranges

| Named Range | Reference | Purpose |
|-------------|-----------|---------|
| `Personnel_ID_List` | Personnel_Screening_Registry!$A$5:$A$154 | Validation for Personnel ID references |
| `Screening_Level_Overrides` | Screening_Level_Matrix!$B$24:$F$53 | Override lookup range |
| `Role_Tier_Levels` | Screening_Level_Matrix!$A$5:$C$10 | Standard tier-to-level mapping |

---

### 9.7 Sheet Protection Settings

**All Sheets:**
- Protect sheet: TRUE
- Allow: Sort, AutoFilter
- Disallow: Delete rows, Modify formulas, Unprotect sheet

**Unlocked Cells (user can edit):**
- All yellow-filled input cells
- Date fields
- Dropdown selections
- Free text fields (Notes, Gap Descriptions, Evidence References, Justification fields)

**Special Protection Note — Sheet 7 (Legal_Compliance_Review):**
This sheet contains legally sensitive assessment findings. Sheet protection is enforced. Access to the completed workbook should be restricted to authorized personnel (CISO, CHRO, DPO, Legal, Internal Audit).

---

### 9.8 Conditional Formatting Rules

**Sheet 3 (Screening_Level_Matrix), Column E (Screening_Level_Justified):**
- Yes: Green fill
- No: Red fill
- Requires-Review: Orange fill

**Sheet 4 (Personnel_Screening_Registry), Column Q (Screening_Compliance_Rating):**
- Compliant: Green fill
- Partial: Yellow fill
- Non-Compliant: Red fill

**Sheet 4 (Personnel_Screening_Registry), Column O (Criminal_Check_Completed):**
- Yes: Green fill
- No: Red fill
- N/A: No fill
- Consent-Pending: Orange fill (FFC000) — draws attention to pending consent

**Sheet 5 (Screening_Compliance_Verification), Column N (Compliance_Rating):**
- Compliant: Green fill
- Partial: Yellow fill
- Non-Compliant: Red fill

**Sheet 6 (Continuous_Screening_Assessment), Column H (Re_Screening_Status):**
- Current: Green fill
- Due-Soon: Yellow fill
- Overdue-<90-Days: Orange fill
- Overdue->90-Days: Red fill

**Sheet 6 (Continuous_Screening_Assessment), Column L (Continuous_Screening_Rating):**
- Compliant: Green fill
- Partial: Yellow fill
- Non-Compliant: Red fill

**Sheet 8 (Gap_Analysis), Column F (Risk_Level):**
- Critical: Red fill, White text
- High: Orange fill
- Medium: Yellow fill
- Low: Light Green fill

---

### 9.9 Freeze Panes Configuration

| Sheet | Freeze At | Rationale |
|-------|-----------|-----------|
| Dashboard | None | Full dashboard visible |
| Screening_Process_Assessment | None | Single-column Q&A format |
| Screening_Level_Matrix | A14 | Keep Section A visible when scrolling Section C |
| Personnel_Screening_Registry | A5 | Keep column headers visible (150 rows) |
| Screening_Compliance_Verification | A5 | Keep column headers visible |
| Continuous_Screening_Assessment | A5 | Keep column headers visible |
| Legal_Compliance_Review | None | Single-column Q&A format |
| Gap_Analysis | A5 | Keep column headers visible |
| Evidence_Register | A5 | Keep column headers visible |
| Approval_Sign_Off | A3 | Keep title visible |

---

### 9.10 Column Widths

**Sheet 2 (Screening_Process_Assessment):** A=55, B=45
**Sheet 3 (Screening_Level_Matrix):** A=25, B=30, C=22, D=28, E=22, F=35, G=16, H=22, I=22
**Sheet 4 (Personnel_Screening_Registry):** A=15, B=25, C=12, D=28, E=22, F=20, G=15, H=14, I=24, J=18, K=20, L=22, M=22, N=22, O=24, P=14, Q=24, R=30
**Sheet 5 (Screening_Compliance_Verification):** A=15, B=25, C=24, D=18, E=18, F=20, G=18, H=20, I=18, J=14, K=14, L=22, M=40, N=22, O=35, P=20
**Sheet 6 (Continuous_Screening_Assessment):** A=15, B=25, C=24, D=22, E=24, F=18, G=22, H=24, I=22, J=24, K=32, L=26, M=40, N=20
**Sheet 7 (Legal_Compliance_Review):** A=65, B=45
**Sheet 8 (Gap_Analysis):** A=12, B=18, C=15, D=20, E=40, F=12, G=30, H=25, I=40, J=22, K=18, L=14, M=25, N=18, O=30, P=30
**Sheet 9 (Evidence_Register):** A=12, B=32, C=35, D=20, E=28, F=40, G=16, H=22, I=18, J=30
**Sheet 10 (Approval_Sign_Off):** A=35, B=50, C=25, D=25

---

### 9.11 Print Settings

**All Sheets:**
- Orientation: Landscape
- Fit to: 1 page wide × auto pages tall
- Margins: Narrow (0.5" all sides)
- Header: Sheet name + Date
- Footer: Page X of Y + File name
- Print Titles: Repeat row 4 (column headers) on every page (tabular sheets)
- Print Area: Data range only

**Special Print Note — Sheet 7 (Legal_Compliance_Review):**
- Header includes classification marking: "INTERNAL — CONTAINS LEGAL ASSESSMENT DATA"
- Print area restricted; do not print to shared printers

---

### 9.12 Integration with Python Script

**Generator Script:** `generate_a5_1_2_6_1_2_s3_screening_vetting.py`

**Script Responsibilities:**
1. Create workbook with 10 sheets
2. Apply all formatting (colors, fonts, borders, special purple highlight for criminal check fields)
3. Write all headers, labels, and reference tables (Section B of Sheet 3)
4. Create all data validation rules
5. Write all formulas (including complex override-aware screening level lookup)
6. Apply conditional formatting (including Consent-Pending orange highlighting)
7. Create named ranges
8. Set freeze panes and column widths
9. Protect sheets
10. Save workbook with correct filename

**Script Execution:**
```bash
python generate_a5_1_2_6_1_2_s3_screening_vetting.py
```

**Output:**
```
ISMS-IMP-A.5.1-2-6.1-2.S3_Screening_Vetting_20260130.xlsx
```

---

**[END OF PART II: TECHNICAL SPECIFICATION]**

---

**Document Summary:**
- **Part I: User Guide** (~950 lines) — How to complete the screening assessment
- **Part II: Technical Specification** (~650 lines) — Excel workbook technical structure
- **Total:** ~1,600 lines
- **Complexity:** High (legal compliance dimension adds significant depth; FADP consent and sensitive data handling requirements drive unique validation logic)

**Key Differentiators from .S1 and .S2:**
- **Legal compliance sheet (Sheet 7)** is unique to .S3 — screening is the only stacked control that directly processes sensitive personal data under FADP Art. 4(c)(5)
- **Consent management** is a first-class concern — criminal checks require explicit consent that must be voluntary and separate from employment offer acceptance
- **DPIA requirement** — processing criminal records at scale triggers FADP Art. 22 DPIA obligation
- **Purple-highlighted criminal check fields** — visual distinction for sensitive data fields throughout the workbook
- **Override-aware screening level lookup** — the screening level formula checks for role-specific overrides before falling back to the standard tier mapping

**Next Steps:**
1. Review and approve this specification
2. Generate Python script: `generate_a5_1_2_6_1_2_s3_screening_vetting.py`
3. Test workbook generation
4. Proceed to: ISMS-IMP-A.5.1-2-6.1-2.S4 (Employment Contract Assessment)

---

**END OF SPECIFICATION**

---

*"Trust is earned through verification."*
— Security Maxim

<!-- QA_VERIFIED: 2026-02-06 -->
