**ISMS-IMP-A.5.1-2-6.1-2.S4-TG - Employment Contract Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.2: Terms and Conditions of Employment

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Employment Contract Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.1-2-6.1-2.S4-TG |
| **Related Policy** | ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.6.2 (Terms and Conditions of Employment) |
| **Linked Control** | ISO/IEC 27001:2022 Annex A.6.5 (Responsibilities at Termination or Change of Employment) |
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
- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) — Section 7 (Employment Contract Requirements)
- ISMS-IMP-A.5.1-2-6.1-2.S1 (Policy Framework Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S2 (Roles & Responsibilities Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S3 (Screening & Vetting Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S5 (Governance Compliance Dashboard)
- Swiss Code of Obligations (OR) — Articles 328, 328b, 730a
- Swiss Federal Data Protection Act (FADP / nDSG) — Articles 6, 19
- ISMS-POL-A.8.12 (Data Leakage Prevention) — Annex A (monitoring transparency in employment contracts)

**Note on Linked Controls**: This assessment covers both A.6.2 (what security obligations are IN the contract) and A.6.5 (that post-employment obligations are specified and enforced). These are assessed together because A.6.5 obligations (confidentiality surviving termination, IP assignment, device return) must be contractually established by A.6.2.

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers

---

## 9. Workbook Technical Specification

### 9.1 Workbook Metadata

**File Name:** `ISMS-IMP-A.5.1-2-6.1-2.S4_Employment_Contract_YYYYMMDD.xlsx`

**Workbook Properties:**
- **Title**: ISMS-IMP-A.5.1-2-6.1-2.S4 — Employment Contract Assessment
- **Subject**: ISO/IEC 27001:2022 Controls A.6.2 & A.6.5 Assessment
- **Keywords**: Employment, Contract, NDA, Confidentiality, Post-Employment, ISMS, ISO27001, A.6.2, A.6.5
- **Comments**: Generated via `generate_a5_1_2_6_1_2_s4_employment_contract.py`

---

### 9.2 Sheet Structure Summary

| Sheet # | Sheet Name | Rows | Input | Formulas | Dropdowns |
|---------|------------|------|-------|----------|-----------|
| 1 | Dashboard | 80 | 6 | 35+ | 1 |
| 2 | Contract_Template_Assessment | 40 | 30+ | 8 | 10 |
| 3 | Required_Clause_Registry | 30 | 50+ | 0 | 8 |
| 4 | Personnel_Contract_Compliance | 154 | 900+ | 600 | 3 |
| 5 | Confidentiality_NDA_Tracking | 154 | 750+ | 450 | 5 |
| 6 | Post_Employment_Obligations | 110 | 600+ | 200 | 8 |
| 7 | Contractor_Agreement_Assessment | 64 | 900+ | 60 | 10 |
| 8 | Gap_Analysis | 84 | 640 | 80 | 5 |
| 9 | Evidence_Register | 84 | 640 | 80 | 2 |
| 10 | Approval_Sign_Off | 72 | 25 | 15 | 2 |

**Estimated Python Script Length:** ~900 lines

---

### 9.3 Color Scheme & Styling

**Consistent with .S1–.S3:**

| Element | Fill | Font |
|---------|------|------|
| User Input | Yellow (FFFF00) | Arial 10pt |
| Auto-Calculated | Light Blue (DCE6F1) | Arial 10pt |
| Labels | Gray (D9D9D9) | Arial 10pt Bold |
| Main Title | Dark Blue (003366) | Arial 18pt Bold White |
| Section Headers | Dark Blue (003366) | Arial 12pt White |

**Conditional Formatting — Status Fields:**

| Value | Fill | Font |
|-------|------|------|
| Compliant | Green (92D050) | Black |
| Partial | Yellow (FFFF00) | Black |
| Non-Compliant | Red (FF0000) | White |
| Yes (NDA) | Green (92D050) | Black |
| No (NDA — when required) | Red (FF0000) | White |
| Missing (NDA) | Red (FF0000) | White |
| Critical (Risk) | Red (FF0000) | White |
| High (Risk) | Orange (FFC000) | Black |
| Medium (Risk) | Yellow (FFFF00) | Black |
| Low (Risk) | Light Green (C6EFCE) | Black |

**Special Styling — NDA Column (Sheet 5, Col F):**
- "Missing" in NDA_Type column: Red fill with bold white text — draws immediate attention
- "Standalone-NDA": Light green fill — indicates NDA exists but is separate from contract (worth verifying)

---

### 9.4 Key Formula Patterns

**Contract Up-to-Date Check (Sheet 4, Col L):**
```excel
=IF(G5="","Unknown",IF(G5=H5,"Yes","No"))
```

**Contract Compliance Rating (Sheet 4, Col N):**
```excel
=IF(B5="","",IF(AND(F5<>"",G5<>"",L5="Yes",K5<>"No"),"Compliant",IF(OR(F5="",G5=""),"Non-Compliant","Partial")))
```

**NDA Required (Sheet 5, Col E):**
```excel
=IF(B5="","",IF(OR(D5="Confidential",D5="Restricted",C5="Tier-1-Leadership",C5="Tier-2-Management",C5="Tier-3-Operational"),"Yes","No"))
```

**NDA Compliance Rating (Sheet 5, Col L):**
```excel
=IF(B5="","",IF(E5="No","N/A",IF(AND(OR(F5="Embedded-in-Contract",F5="Standalone-NDA"),G5<>"",H5<>"No",J5="Yes"),"Compliant",IF(F5="Missing","Non-Compliant","Partial"))))
```

**Post-Employment Clause Rating — Current Employees (Sheet 6, Section A, Col J):**
```excel
=IF(B5="","",IF(AND(D5="Yes",F5="Yes",IF(OR(C5="Tier-1-Leadership",C5="Tier-2-Management",C5="Tier-3-Operational"),G5="Yes",TRUE)),"Compliant",IF(OR(D5="No",F5="No"),"Non-Compliant","Partial")))
```

**Post-Employment Tracking Rating — Former Employees (Sheet 6, Section B, Col M):**
```excel
=IF(B5="","",IF(AND(G5="Yes",F5<>"No",OR(I5="Yes",I5="Expired")),"Compliant",IF(OR(G5="No",F5="No"),"Non-Compliant","Partial")))
```

**Contractor Agreement Compliance (Sheet 7, Col Q):**
```excel
=IF(B5="","",IF(AND(E5="Yes",I5="Yes",J5="Yes",IF(L5="Yes",AND(M5="Yes",N5="Yes"),TRUE),O5="Yes",P5="Yes"),"Compliant",IF(OR(E5="No",I5="No",J5="No",AND(L5="Yes",M5="No")),"Non-Compliant","Partial")))
```

**Dashboard Overall Score:**
```excel
=B30*0.20 + B31*0.25 + B32*0.30 + B33*0.15 + B34*0.10
```

---

### 9.5 Data Validation Rules

**Sheet 2:**
- Template_In_Use: `List: Yes,No,Deprecated`
- Legal_Review_Status: `List: Current,Overdue-<6-Months,Overdue->6-Months`
- Clause_Present_in_Template: `List: Yes,No,Partial`
- Clause_Adequate: `List: Yes,No`

**Sheet 3:**
- Applies_To: `List: All-Employees,Tier1-3-Only,Tier1-Only,Contractors-Only,All`
- Required_in_TMPLxxx: `List: Yes,No`

**Sheet 4:**
- Employment_Type: `List: Full-Time,Part-Time,Fixed-Term,Contractor,Consultant`
- Contract_Signed_Before_Start: `List: Yes,No,Same-Day`

**Sheet 5:**
- Information_Access_Classification: `List: Internal,Confidential,Restricted`
- NDA_Type: `List: Embedded-in-Contract,Standalone-NDA,Not-Required,Missing`
- NDA_Signed_Before_Access: `List: Yes,No,Same-Day,N/A`
- NDA_Survival_Clause: `List: Yes,No,N/A`

**Sheet 6 (Section B):**
- Departure_Reason: `List: Resignation,Termination,Retirement,Contract-End,Restructuring`
- Exit_Interview_Completed: `List: Yes,No,N/A`
- Device_Return_Confirmed: `List: Yes,No,Partial,N/A`
- Access_Revoked: `List: Yes,No`
- Confidentiality_Obligation_Active: `List: Yes,No,Expired`
- Non_Solicitation_Active: `List: Yes,No,Expired,N/A`

**Sheet 7:**
- Party_Type: `List: Contractor,Consultant,Vendor`
- Agreement_Signed: `List: Yes,No`
- Security_Obligations_Clause: `List: Yes,No`
- NDA_In_Place: `List: Yes,No`
- DPA_Required: `List: Yes,No`
- DPA_In_Place: `List: Yes,No,N/A`
- DPA_Covers_Required_Elements: `List: Yes,Partial,No,N/A`
- Access_Scope_Documented: `List: Yes,No`
- Access_Revocation_on_End_Clause: `List: Yes,No`

**Sheet 8 (Gap_Analysis):**
- Source_Sheet: `List: Template,Clause-Registry,Personnel,NDA,Post-Employment,Contractor`
- Gap_Category: `List: Template-Gap,Clause-Gap,Contract-Gap,NDA-Gap,Post-Employment-Gap,Contractor-Gap`
- Risk_Level: `List: Critical,High,Medium,Low`
- Estimated_Effort: `List: <1hr,1-4hrs,1day,2-5days,>1week`
- Status: `List: Not-Started,In-Progress,Blocked,Completed,Accepted-Risk`

**Sheet 9 (Evidence_Register):**
- Evidence_Type: `List: Employment-Contract,Contract-Template,NDA-Agreement,DPA-Agreement,IP-Assignment-Agreement,Exit-Checklist,Access-Revocation-Record,Device-Return-Record,Legal-Review-Sign-Off,Template-Review-Record,Disciplinary-Policy,Acceptable-Use-Policy,Monitoring-Privacy-Notice,Post-Employment-Obligation-Letter,Other`
- Verification_Status: `List: Verified,Pending,Not-Verified,Expired`

---

### 9.6 Named Ranges

| Named Range | Reference | Purpose |
|-------------|-----------|---------|
| `Personnel_Contract_ID_List` | Personnel_Contract_Compliance!$A$5:$A$154 | Cross-sheet Personnel ID reference |
| `Template_ID_List` | Contract_Template_Assessment!$A$5:$A$10 | Template ID validation |
| `Clause_ID_List` | Required_Clause_Registry!$A$5:$A$29 | Clause ID validation |

---

### 9.7 Sheet Protection

**All sheets protected.** Unlocked: yellow input cells, date fields, dropdowns, free text fields.

**Special Note — Sheet 6 Section B (Former Employees):**
Access to former employee departure details should be restricted to HR, CISO, and Legal. Sheet protection enforces formula integrity; access to the workbook file should be controlled at the file-share level.

---

### 9.8 Conditional Formatting Rules

**Sheet 2, Col D (Clause_Present_in_Template):**
- Yes: Green fill
- No: Red fill
- Partial: Yellow fill

**Sheet 4, Col L (Contract_Up_to_Date):**
- Yes: Green fill
- No: Red fill
- Unknown: Orange fill

**Sheet 4, Col N (Contract_Compliance_Rating):**
- Compliant: Green / Partial: Yellow / Non-Compliant: Red

**Sheet 5, Col F (NDA_Type):**
- Embedded-in-Contract: Green fill
- Standalone-NDA: Light green fill
- Missing: Red fill, Bold white text
- Not-Required: No fill

**Sheet 5, Col L (NDA_Compliance_Rating):**
- Compliant: Green / Partial: Yellow / Non-Compliant: Red / N/A: No fill

**Sheet 6 Section B, Col G (Access_Revoked):**
- Yes: Green fill
- No: Red fill (critical — access should be revoked immediately on departure)

**Sheet 7, Col Q (Agreement_Compliance_Rating):**
- Compliant: Green / Partial: Yellow / Non-Compliant: Red

**Sheet 8, Col F (Risk_Level):**
- Critical: Red fill, White text / High: Orange / Medium: Yellow / Low: Light green

---

### 9.9 Freeze Panes

| Sheet | Freeze At | Rationale |
|-------|-----------|-----------|
| Dashboard | None | Full view |
| Contract_Template_Assessment | None | Two-section layout |
| Required_Clause_Registry | A5 | Keep headers visible |
| Personnel_Contract_Compliance | A5 | 150 rows — keep headers |
| Confidentiality_NDA_Tracking | A5 | 150 rows — keep headers |
| Post_Employment_Obligations | None | Two distinct sections |
| Contractor_Agreement_Assessment | A5 | Keep headers visible |
| Gap_Analysis | A5 | Keep headers visible |
| Evidence_Register | A5 | Keep headers visible |
| Approval_Sign_Off | A3 | Keep title visible |

---

### 9.10 Print Settings

All sheets: Landscape, fit 1 page wide × auto tall, narrow margins (0.5"), header (sheet name + date), footer (page X of Y + filename), repeat row 4 on every page for tabular sheets.

**Special:** Sheet 6 header includes "INTERNAL — CONTAINS HR AND DEPARTURE DATA"

---

### 9.11 Python Script Generation

**Script:** `generate_a5_1_2_6_1_2_s4_employment_contract.py`

**Execution:**
```bash
python generate_a5_1_2_6_1_2_s4_employment_contract.py
```

**Output:** `ISMS-IMP-A.5.1-2-6.1-2.S4_Employment_Contract_20260130.xlsx`

---

**[END OF PART II: TECHNICAL SPECIFICATION]**

---

**Document Summary:**
- **Part I: User Guide** (~900 lines)
- **Part II: Technical Specification** (~500 lines)
- **Total:** ~1,600 lines

**Key Differentiators from .S1–.S3:**
- **Linked control coverage**: Assesses both A.6.2 (contract content) and A.6.5 (post-termination obligations) — the only assessment in the stacked framework covering two distinct ISO controls
- **Template-first approach**: Starts at the template level before drilling to individual level — fixes at the template propagate to all future hires
- **Two-section Sheet 6**: Current employees (clause verification) and former employees (obligation enforcement) in one sheet — provides the complete lifecycle view
- **Contractor/vendor DPA assessment**: Sheet 7 bridges A.6.2 employment contracts with third-party processor obligations (FADP Art. 9)
- **NDA as audit focal point**: Explicit guidance that NDAs are the most auditable element — prioritizes evidence accessibility for this clause type

**Next Steps:**
1. Review and approve this specification
2. Proceed to: ISMS-IMP-A.5.1-2-6.1-2.S5 (Governance Compliance Dashboard)

---

**END OF SPECIFICATION**

---

*"A verbal contract isn't worth the paper it's written on."*
— Samuel Goldwyn

<!-- QA_VERIFIED: 2026-02-06 -->
