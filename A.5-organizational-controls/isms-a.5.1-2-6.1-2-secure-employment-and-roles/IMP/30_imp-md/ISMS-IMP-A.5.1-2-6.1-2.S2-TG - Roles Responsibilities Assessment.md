**ISMS-IMP-A.5.1-2-6.1-2.S2-TG - Roles & Responsibilities Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.2: Information Security Roles and Responsibilities

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Roles & Responsibilities Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.1-2-6.1-2.S2-TG |
| **Related Policy** | ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.2 (Information Security Roles and Responsibilities) |
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
- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) - Section 5 (Roles & Responsibilities Requirements)
- ISMS-IMP-A.5.1-2-6.1-2.S1 (Policy Framework Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S3 (Screening & Vetting Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S4 (Employment Contract Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S5 (Governance Compliance Dashboard)

**Note on Naming Convention**: The ".S" designation indicates this implementation is part of a **stacked control framework** (A.5.1 + A.5.2 + A.6.1 + A.6.2). Despite unified implementation, each control maintains distinct requirements for Statement of Applicability purposes.

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## 9. Workbook Technical Specification

### 9.1 Workbook Metadata

**File Name Convention**: `ISMS-IMP-A.5.1-2-6.1-2.S2_Roles_Responsibilities_YYYYMMDD.xlsx`  
**Example**: `ISMS-IMP-A.5.1-2-6.1-2.S2_Roles_Responsibilities_20260130.xlsx`

**Excel Version Requirements**:
- Microsoft Excel 2016 or later
- Excel for Microsoft 365
- Compatible with LibreOffice Calc 7.0+ (with minor formula adjustments)

**Workbook Properties**:
- **Title**: ISMS-IMP-A.5.1-2-6.1-2.S2 - Roles & Responsibilities Assessment
- **Author**: [Organization] Information Security Team
- **Subject**: ISO/IEC 27001:2022 Control A.5.2 Assessment
- **Keywords**: Roles, Responsibilities, RACI, ISMS, ISO27001, A.5.2
- **Comments**: Generated via Python script `generate_a5_1_2_6_1_2_s2_roles_responsibilities.py`

**Workbook Settings**:
- **Calculation**: Automatic
- **Iteration**: Enabled (Max 100 iterations, Max change 0.001)
- **Save AutoRecover**: Every 10 minutes
- **Sheet Protection**: Protect formulas, allow data entry in input cells

---

### 9.2 Sheet Structure Summary

| Sheet # | Sheet Name | Row Count | Input Cells | Formula Cells | Dropdowns |
|---------|------------|-----------|-------------|---------------|-----------|
| 1 | Dashboard | 100 | 6 | 40+ | 1 |
| 2 | Role_Inventory | 100 | 1,800+ | 200 | 6 |
| 3 | Role_Definition_Assessment | 90 | 800+ | 300 | 7 |
| 4 | RACI_Matrix_Assessment | 50 | 400 | 120 | 5 |
| 5 | Role_Assignment_Verification | 90 | 900+ | 200 | 8 |
| 6 | Training_Assessment | 90 | 900+ | 150 | 8 |
| 7 | Access_Alignment_Review | 90 | 700+ | 150 | 7 |
| 8 | Gap_Analysis | 80 | 640 | 160 | 3 |
| 9 | Evidence_Register | 80 | 640 | 80 | 2 |
| 10 | Approval_Sign_Off | 70 | 30 | 15 | 2 |

**Total Estimated Lines in Python Script**: ~900 lines (following A.8.23/A.8.24 quality standards)

---

### 9.3 Color Scheme & Styling

**Consistent with .S1 (Policy Framework Assessment)**:

- **User Input Cells**: Yellow fill (RGB 255, 255, 0), Arial 10pt
- **Auto-Calculated Cells**: Light Blue fill (RGB 220, 230, 241), Arial 10pt
- **Labels/Headers**: Gray fill (RGB 217, 217, 217), Arial 10pt Bold
- **Section Headers**: Dark Blue fill (RGB 0, 51, 102), White text, Arial 14pt Bold
- **Conditional Formatting**:
  - Compliant: Green (RGB 146, 208, 80)
  - Partial: Yellow (RGB 255, 255, 0)
  - Non-Compliant: Red (RGB 255, 0, 0)

---

### 9.4 Key Formula Patterns

**Role Assignment Status (Sheet 5)**:
```excel
=IF(B5="[VACANT]","Vacant",IF(B5="","Pending-Hire","Assigned"))
```

**RACI Compliance Rating (Sheet 4)**:
```excel
=IF(AND(C5="Yes",E5="Complete",F5="Clear",G5="Accurate",I5="Current"),"Compliant",
  IF(OR(C5="No",E5="Incomplete",F5="Ambiguous"),"Non-Compliant","Partial"))
```

**Training Status Auto-Calculate (Sheet 6)**:
```excel
=IF(I5="","N/A",IF(I5>=TODAY()-365,"Complete",IF(A5<90,"Incomplete","Overdue")))
```

**Overall Compliance Score (Dashboard)**:
```excel
=AVERAGE(B30,B31,B32,B33,B34,B35)
```
Where B30-B35 are domain compliance scores (25%, 25%, 20%, 15%, 10%, 5% weighted)

---

### 9.5 Data Validation Rules

**Role Tier (Sheet 2, Column C)**:
```
List: Tier-1-Leadership,Tier-2-Management,Tier-3-Operational
```

**Employment Type (Sheet 2, Column G)**:
```
List: Full-Time,Part-Time,Contractor,External-Consultant,Vacant
```

**Definition Type (Sheet 3, Column D)**:
```
List: Job-Description,Role-Charter,Policy-Section,Org-Chart-Only,None
```

**RACI Clarity (Sheet 4, Column F)**:
```
List: Clear,Partially-Clear,Ambiguous
```

**Assignment Status (Sheet 5, Column D)**:
```
List: Assigned,Vacant,Pending-Hire,Pending-Transition
```

**Training Frequency (Sheet 6, Column G)**:
```
List: Annual,Biennial,One-Time,As-Needed
```

**Access Review Frequency (Sheet 7, Column I)**:
```
List: Quarterly,Semi-Annual,Annual,Not-Defined
```

---

### 9.6 Named Ranges

**Workbook-level Named Ranges**:

| Named Range | Reference | Purpose |
|-------------|-----------|---------|
| `Role_ID_List` | Role_Inventory!$A$5:$A$104 | Validation list for Role ID dropdowns |
| `Role_Inventory_Data` | Role_Inventory!$A$5:$S$104 | Full role inventory data range |
| `Process_List` | RACI_Matrix_Assessment!$B$5:$B$24 | List of processes requiring RACI |

---

### 9.7 Sheet Protection Settings

**All Sheets**:
- Protect sheet: TRUE
- Password: [Optional - set during generation]
- Allow: Sort, AutoFilter
- Disallow: Delete rows, Modify formulas, Unprotect sheet

**Unlocked Cells** (user can edit):
- Yellow-filled input cells
- Date fields
- Dropdown selections
- Free text fields (Notes, Gap Descriptions, Evidence References)

---

### 9.8 Conditional Formatting Rules

**Sheet 2 (Role_Inventory), Column K (Next_Review_Date)**:
- If < TODAY(): Red fill, "Overdue"
- If between TODAY() and (TODAY()+30): Yellow fill, "Due Soon"
- If > (TODAY()+30): No fill

**Sheet 2 (Role_Inventory), Column R (Gap_Identified)**:
- No-Gap: Green fill
- Minor-Gap: Yellow fill
- Significant-Gap: Orange fill (RGB 255, 192, 0)
- Critical-Gap: Red fill

**Sheet 3 (Role_Definition_Assessment), Column L (Definition_Completeness_Rating)**:
- Complete: Green fill
- Partial: Yellow fill
- Incomplete: Red fill

**Sheet 4 (RACI_Matrix_Assessment), Column J (RACI_Compliance_Rating)**:
- Compliant: Green fill
- Partial: Yellow fill
- Non-Compliant: Red fill

**Sheet 5 (Role_Assignment_Verification), Column L (Assignment_Compliance_Rating)**:
- Compliant: Green fill
- Partial: Yellow fill
- Non-Compliant: Red fill

**Sheet 6 (Training_Assessment), Column L (Training_Compliance_Rating)**:
- Compliant: Green fill
- Partial: Yellow fill
- Non-Compliant: Red fill

**Sheet 7 (Access_Alignment_Review), Column J (Access_Compliance_Rating)**:
- Compliant: Green fill
- Partial: Yellow fill
- Non-Compliant: Red fill

**Sheet 8 (Gap_Analysis), Column F (Risk_Level)**:
- Critical: Red fill
- High: Orange fill (RGB 255, 192, 0)
- Medium: Yellow fill
- Low: No fill

---

### 9.9 Freeze Panes Configuration

- **Sheet 1 (Dashboard)**: No freeze (entire dashboard visible without scroll)
- **Sheets 2-9**: Freeze at A5 (keep column headers visible when scrolling)
- **Sheet 10 (Approval)**: Freeze at A3

---

### 9.10 Print Settings

**For all sheets**:
- Orientation: Landscape
- Fit to: 1 page wide by [auto] pages tall
- Margins: Narrow (0.5" all sides)
- Header: Sheet name + Date
- Footer: Page X of Y + File name
- Print titles: Repeat row 4 (column headers) on every page
- Print area: Data range only (exclude empty rows)

---

### 9.11 File Naming & Version Control

**File Naming Convention**:
```
ISMS-IMP-A.5.1-2-6.1-2.S2_Roles_Responsibilities_YYYYMMDD.xlsx
```

**Version Control**:
- Date in filename serves as version identifier
- Previous assessments archived with date suffix
- Repository: Store in version-controlled location (SharePoint, Git, DMS)

---

### 9.12 Integration with Python Script

**Generator Script**: `generate_a5_1_2_6_1_2_s2_roles_responsibilities.py`

**Script Responsibilities**:
1. Create workbook with 10 sheets
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
python generate_a5_1_2_6_1_2_s2_roles_responsibilities.py
```

**Output**:
```
ISMS-IMP-A.5.1-2-6.1-2.S2_Roles_Responsibilities_20260130.xlsx
```

---

**[END OF IMPLEMENTATION SPECIFICATION]**

---

**Document Summary**:
- **Part I: User Guide** (~900 lines) - How to complete assessment
- **Part II: Technical Specification** (~700 lines) - Excel workbook structure
- **Total**: ~1,600 lines
- **Complexity**: Moderate (10 sheets, RACI focus, role-centric assessment)

**Next Steps**: 
1. Review and approve this specification
2. Generate Python script: `generate_a5_1_2_6_1_2_s2_roles_responsibilities.py`
3. Test workbook generation
4. Proceed to next assessment: ISMS-IMP-A.5.1-2-6.1-2.S3 (Screening & Vetting)

---

**END OF SPECIFICATION**

---

*"The price of greatness is responsibility."*
— Winston Churchill

<!-- QA_VERIFIED: 2026-02-06 -->
