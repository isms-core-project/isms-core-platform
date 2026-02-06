**ISMS-IMP-A.8.25-26-29.S1-TG - Security Requirements Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.25: Secure Development Life Cycle

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.25-26-29-S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Security Requirements Compliance (A.8.26) |
| **Related Policy** | ISMS-POL-A.8.25-26-29 Section 2 (Application Security Requirements) |
| **Purpose** | Assessment workbook for evaluating application security requirements specification, threat modeling, and architecture review compliance |
| **Target Audience** | Security Architects, Product Managers, Application Owners, Compliance Officers |
| **Assessment Type** | Application-by-Application Security Requirements Verification |
| **Review Cycle** | Quarterly (High-Risk), Annually (Medium/Low-Risk) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guide format | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.25-26-29.S1-UG.

---

# Technical Specification

[*Note: PART II will contain detailed Excel workbook structure, column definitions, formulas, data validation rules, and technical notes for Python script developers. This section is typically 400-800 lines and includes detailed specifications for generating the workbook programmatically.*]

[*Due to token constraints, PART II will be provided separately if needed. The structure follows the pattern established in A.8.24 and A.8.23 implementations, with detailed sheet-by-sheet column specifications, formula definitions, and Python script integration points.*]

---

**END OF PART I: USER COMPLETION GUIDE**

**Document Status:** ✅ READY FOR REVIEW (PART I Complete, PART II Pending)
# PART II: TECHNICAL SPECIFICATION

# Instructions for Workbook Development

This section provides detailed technical specifications for creating the Security Requirements Assessment Excel workbook, either manually or via Python script (`generate_a825_26_29_1_security_requirements.py`).

## Workbook Overview

**Filename Format:** `ISMS-A826-Requirements-[APP-ID]-[YYYYMMDD].xlsx`

**Example:** `ISMS-A826-Requirements-APP-CUST-20260123.xlsx`

**Total Sheets:** 10

**Excel Compatibility:** Excel 2016+ (Office 365 recommended for best formula support)

**File Size Estimate:** 500KB - 2MB depending on evidence attachments

---

# Common Structure Elements

## Standard Column Widths

| Column Type | Width (pixels) | Width (Excel units) |
|-------------|----------------|---------------------|
| ID Column (A) | 80 | 12 |
| Question/Description | 400 | 60 |
| Answer/Status | 150 | 22 |
| Evidence/Location | 300 | 45 |
| Date | 120 | 18 |
| Comments/Notes | 300 | 45 |

## Standard Colors (Fill)

**Headers:**

- Main Section Header: RGB(0, 51, 102) / #003366 (Dark Blue)
- Sub-Header: RGB(68, 114, 196) / #4472C4 (Blue)
- Column Header: RGB(217, 217, 217) / #D9D9D9 (Light Gray)

**Input Cells:**

- User Input Required: RGB(255, 255, 204) / #FFFFCC (Light Yellow)
- Auto-Calculated: RGB(217, 217, 217) / #D9D9D9 (Light Gray) - Protected

**Status Indicators:**

- Compliant (✅): RGB(198, 239, 206) / #C6EFCE (Light Green)
- Partial (⚠️): RGB(255, 235, 156) / #FFEB9C (Light Yellow)
- Non-Compliant (❌): RGB(255, 199, 206) / #FFC7CE (Light Red)
- N/A: RGB(237, 237, 237) / #EDEDED (Gray)

## Standard Fonts

- **Headers:** Calibri 14pt Bold, White text
- **Sub-Headers:** Calibri 11pt Bold, White text
- **Column Headers:** Calibri 10pt Bold, Black text
- **Body Text:** Calibri 10pt, Black text
- **Instructions:** Calibri 9pt, Italic, Gray text

## Data Validation Standards

**Yes/No Dropdowns:**
```
=Yes,No,N/A
```

**Status Dropdowns:**
```
=✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A
```

**Risk Classification:**
```
=High Risk,Medium Risk,Low Risk
```

**Approval Status:**
```
=Draft,Final,Approved,Requires Remediation
```

---

# Sheet 1: Application Profile

## Purpose
Document basic application information for assessment context.

## Sheet Structure

**Rows 1-2:** Header Section

- A1:G1 merged: "Application Profile" (Dark Blue header, white text, 14pt bold)
- A2:G2 merged: "Basic application information and characteristics" (Blue sub-header, white text, 11pt)

**Row 3:** Column Headers
| Column | Header | Width | Format |
|--------|--------|-------|--------|
| A | Field | 200px | Gray fill, bold, centered |
| B | Value | 300px | Gray fill, bold, centered |
| C | Evidence Location | 300px | Gray fill, bold, centered |
| D | Date | 120px | Gray fill, bold, centered |
| E | Status | 120px | Gray fill, bold, centered |
| F | Verified By | 150px | Gray fill, bold, centered |
| G | Notes | 250px | Gray fill, bold, centered |

**Rows 4-20:** Data Entry Section

### Row 4: Application Name

- A4: "Application Name" (bold)
- B4: [User Input] - Yellow fill
- C4: "Application Inventory - [Location]" - Yellow fill
- D4: [Date] - Yellow fill, Date format (DD.MM.YYYY)
- E4: Auto-status (if B4 not blank → "✅ Complete", else "❌ Incomplete")
- F4: [User Input] - Yellow fill
- G4: [User Input] - Yellow fill

### Row 5: Application ID

- A5: "Application ID" (bold)
- B5: [User Input - format: APP-XXX] - Yellow fill, Data validation: Text length 3-20
- C5-G5: Same structure as Row 4

### Row 6: Application Owner

- A6: "Application Owner" (bold)
- B6: [User Input - Name] - Yellow fill
- C6: "Organizational Chart / HR System" - Yellow fill
- D6-G6: Same structure as Row 4

### Row 7: Owner Department

- A7: "Owner Department" (bold)
- B7: [User Input] - Yellow fill

### Row 8: Owner Contact Email

- A8: "Owner Contact Email" (bold)
- B8: [User Input] - Yellow fill, Data validation: Email format check

### Row 9: Application Description - Business Purpose

- A9: "Business Purpose" (bold)
- B9: [User Input - Text area, merged B9:B11] - Yellow fill, Wrap text
- C9-G9: Evidence reference (merged C9:C11)

### Row 12: Application Description - User Base

- A12: "User Base" (bold)
- B12: [User Input] - Yellow fill
- **Example text in comments:** "External customers (~10,000 active users)"

### Row 13: Application Description - Technology Stack

- A13: "Technology Stack" (bold)
- B13: [User Input - Text area, merged B13:B14] - Yellow fill, Wrap text
- **Example text in comments:** "Frontend: React.js, Backend: Node.js, Database: PostgreSQL, Infrastructure: AWS"

### Row 15: Data Types Processed

- A15: "Data Types Processed" (bold)
- B15: [User Input - Multiline] - Yellow fill, Wrap text
- **Data validation dropdown:**

```
=PII (Names/Emails/Addresses),Financial Data,Health Data (PHI),Authentication Credentials,Business Sensitive,Public Information
```

- **Allow multiple selections via comment instruction:** "Check all that apply - separate with commas"

### Row 16: Data Classification (Highest)

- A16: "Data Classification (Highest)" (bold)
- B16: [Dropdown] - Yellow fill
- **Data validation:**

```
=Confidential/Restricted,Internal Use,Public
```

### Row 17: Regulatory Scope

- A17: "Regulatory Scope" (bold)
- B17: [User Input - Multiline] - Yellow fill, Wrap text
- **Data validation dropdown (multi-select via comments):**

```
=GDPR,FADP,PCI DSS,HIPAA,SOX,DORA,NIS2,Industry-Specific,None
```

### Row 18: Deployment Model

- A18: "Deployment Model" (bold)
- B18: [Dropdown] - Yellow fill
- **Data validation:**

```
=On-Premises,Cloud (AWS/Azure/GCP),Hybrid,SaaS (Vendor-Hosted)
```

### Row 19: Internet Accessibility

- A19: "Internet Accessibility" (bold)
- B19: [Dropdown] - Yellow fill
- **Data validation:**

```
=Public Internet,VPN Required,Internal Network Only,Air-Gapped
```

### Row 20: Assessment Period

- A20: "Assessment Period" (bold)
- B20: [User Input] - Yellow fill
- **Example text in comments:** "Q4 2025 (October - December 2025)"

## Formulas

**E4 (Status for Application Name):**
```excel
=IF(B4<>"","✅ Complete","❌ Incomplete")
```

**Apply same formula pattern to E5:E19** (adjust row reference)

**Conditional Formatting for Column E:**

- Rule 1: If cell contains "✅" → Green fill (RGB 198, 239, 206)
- Rule 2: If cell contains "❌" → Red fill (RGB 255, 199, 206)

## Sheet Protection

**Protect:** Column E (formulas), Headers (Rows 1-3)
**Unlock:** Columns B, C, D, F, G (user input areas)

---

# Sheet 2: Risk Classification

## Purpose
Document and validate application risk classification using policy criteria.

## Sheet Structure

**Rows 1-2:** Header Section

- A1:J1 merged: "Application Risk Classification" (Dark Blue header)
- A2:J2 merged: "Risk scoring based on ISMS-POL-A.8.25-26-29 Section 2 criteria" (Blue sub-header)

**Row 3:** Instructions

- A3:J3 merged: "Score each criterion 0-5 using the scoring guidelines. Weighted total determines risk classification: High Risk ≥3.5, Medium Risk 2.0-3.4, Low Risk <2.0" (Italic, gray text)

**Row 4:** Column Headers
| Column | Header | Width |
|--------|--------|-------|
| A | Risk Criterion | 200px |
| B | Weight | 80px |
| C | Score (0-5) | 80px |
| D | Weighted Score | 100px |
| E | Scoring Guidelines | 400px |
| F | Justification | 250px |
| G | Evidence | 250px |
| H | Verified | 100px |

**Rows 5-9:** Risk Scoring Criteria

### Row 5: Data Sensitivity

- A5: "Data Sensitivity" (bold)
- B5: "30%" (centered, gray fill, protected)
- C5: [User Input 0-5] - Yellow fill, Data validation: Whole number 0-5
- D5: `=B5*C5` (formula, gray fill, protected, number format: 0.00)
- E5: "5=PII+Financial+PHI, 4=Confidential Business, 3=Internal, 2=Low-Sensitivity, 1=Public Only, 0=No Data" (Wrap text)
- F5: [User Input] - Yellow fill, Wrap text
- G5: [User Input] - Yellow fill
- H5: [Dropdown: Yes/No] - Yellow fill

### Row 6: User Base

- A6: "User Base" (bold)
- B6: "20%" (centered, gray fill, protected)
- C6: [User Input 0-5] - Yellow fill, Data validation: Whole number 0-5
- D6: `=B6*C6` (formula, gray fill, protected, number format: 0.00)
- E6: "5=Public/Anonymous Users, 4=Partners/Contractors, 3=Mixed Internal/External, 2=Employees Only, 1=Restricted Group (<20)" (Wrap text)
- F6-H6: Same as Row 5

### Row 7: Internet Exposure

- A7: "Internet Exposure" (bold)
- B7: "25%" (centered, gray fill, protected)
- C7: [User Input 0-5] - Yellow fill, Data validation: Whole number 0-5
- D7: `=B7*C7` (formula)
- E7: "5=Public Internet, 4=Internet+VPN, 3=Hybrid, 2=Internal+Remote Access, 1=Isolated Internal, 0=Air-Gapped" (Wrap text)
- F7-H7: Same as Row 5

### Row 8: Business Criticality

- A8: "Business Criticality" (bold)
- B8: "15%" (centered, gray fill, protected)
- C8: [User Input 0-5] - Yellow fill, Data validation: Whole number 0-5
- D8: `=B8*C8` (formula)
- E8: "5=Critical (Outage=Business Stop), 4=High Impact, 3=Moderate Impact, 2=Low Impact, 1=Minimal Impact" (Wrap text)
- F8-H8: Same as Row 5

### Row 9: Regulatory Scope

- A9: "Regulatory Scope" (bold)
- B9: "10%" (centered, gray fill, protected)
- C9: [User Input 0-5] - Yellow fill, Data validation: Whole number 0-5
- D9: `=B9*C9` (formula)
- E9: "5=Multiple Regulations, 4=One Major Regulation, 3=Industry Standards, 2=Internal Policies Only, 1=Minimal" (Wrap text)
- F9-H9: Same as Row 5

**Row 10:** Totals Row

- A10: "TOTAL WEIGHTED SCORE" (bold, dark gray fill)
- B10: "100%" (centered, dark gray fill, protected)
- C10: [Auto-sum display] - Formula: `=SUM(C5:C9)/5` (show average score, gray fill, protected)
- D10: `=SUM(D5:D9)` (bold, dark gray fill, protected, number format: 0.00)
- **Conditional Formatting for D10:**
  - If ≥3.5 → Red fill (High Risk)
  - If 2.0-3.4 → Yellow fill (Medium Risk)
  - If <2.0 → Green fill (Low Risk)

**Row 12:** Risk Classification Result

- A12: "Risk Classification" (bold)
- B12: `=IF(D10>=3.5,"High Risk",IF(D10>=2.0,"Medium Risk","Low Risk"))` (formula, large font 14pt, bold)
- **Conditional Formatting for B12:**
  - If "High Risk" → Red fill, white text
  - If "Medium Risk" → Yellow fill, black text
  - If "Low Risk" → Green fill, white text

**Row 13:** Classification Approved By

- A13: "Classification Approved By" (bold)
- B13: [User Input - Name] - Yellow fill
- C13: "Approval Date" (bold)
- D13: [User Input - Date] - Yellow fill, Date format

**Row 14:** Next Review Date

- A14: "Next Review Date" (bold)
- B14: `=DATE(YEAR(D13)+1,MONTH(D13),DAY(D13))` (formula - 1 year from approval, gray fill, Date format)

**Row 15:** Override Justification (if needed)

- A15: "Override Justification (if applicable)" (bold)
- B15:H15 merged: [User Input - Text area] - Yellow fill, Wrap text
- **Instruction in comments:** "If you believe formula classification is incorrect, document justification here"

## Data Validation

**Score Columns (C5:C9):**
```
Type: Whole number
Data: Between 0 and 5
Error message: "Score must be between 0 and 5"
```

**Verified Column (H5:H9):**
```
=Yes,No
```

## Conditional Formatting

**D10 (Total Weighted Score):**
```
Rule 1: =$D$10>=3.5 → Fill: RGB(255,199,206), Font: Bold
Rule 2: =AND($D$10>=2.0,$D$10<3.5) → Fill: RGB(255,235,156), Font: Bold
Rule 3: =$D$10<2.0 → Fill: RGB(198,239,206), Font: Bold
```

**B12 (Risk Classification):**
```
Rule 1: =$B$12="High Risk" → Fill: RGB(255,0,0), Font: White, Bold, 14pt
Rule 2: =$B$12="Medium Risk" → Fill: RGB(255,192,0), Font: Black, Bold, 14pt
Rule 3: =$B$12="Low Risk" → Fill: RGB(0,176,80), Font: White, Bold, 14pt
```

---

# Sheet 3: Security Requirements Documentation

## Purpose
Assess completeness of Security Requirements Specification (SRS).

## Sheet Structure

**Rows 1-2:** Header Section

- A1:H1 merged: "Security Requirements Documentation Status" (Dark Blue header)
- A2:H2 merged: "Assessment of SRS existence, completeness, and currency" (Blue sub-header)

**Row 3:** Column Headers
| Column | Header | Width |
|--------|--------|-------|
| A | Requirement Category | 250px |
| B | Exists? (Y/N/NA) | 100px |
| C | Document Title & Location | 300px |
| D | Version | 80px |
| E | Last Updated | 100px |
| F | Status | 120px |
| G | Evidence | 250px |
| H | Notes | 250px |

**Row 4-5:** SRS Existence

### Row 4: SRS Exists?

- A4: "1.1 Security Requirements Specification (SRS) Exists?" (bold)
- B4: [Dropdown: Yes/No/N/A] - Yellow fill
- C4: [User Input - Document title and location] - Yellow fill, Wrap text
- D4: [User Input - Version] - Yellow fill
- E4: [User Input - Date] - Yellow fill, Date format
- F4: Formula (see below)
- G4: [User Input - Evidence link] - Yellow fill
- H4: [User Input - Notes] - Yellow fill, Wrap text

**F4 Formula (Status):**
```excel
=IF(B4="Yes",IF(E4<>"",IF((TODAY()-E4)<=365,"✅ Compliant","⚠️ Partial - Outdated"),"⚠️ Partial - No Date"),IF(B4="No","❌ Non-Compliant",IF(B4="N/A","N/A","")))
```

**Logic:**

- If Yes + Date < 12 months old → ✅ Compliant
- If Yes + Date > 12 months old → ⚠️ Partial - Outdated
- If Yes + No date → ⚠️ Partial - No Date
- If No → ❌ Non-Compliant
- If N/A → N/A

### Row 5: SRS Completeness Header

- A5:H5 merged: "1.2 Functional Security Requirements Coverage" (bold, gray fill)

**Rows 6-11:** Functional Security Requirements

### Row 6: Authentication Requirements

- A6: "Authentication Requirements Specified?" (indent with space or bullet)
- B6: [Dropdown: Yes/No/N/A] - Yellow fill
- C6: [User Input - Reference to section/page in SRS] - Yellow fill
- D6-E6: N/A (gray fill, protected)
- F6: Formula (simplified status: Yes=Compliant, No=Non-Compliant, N/A=N/A)
- G6-H6: [User Input] - Yellow fill

**F6 Formula:**
```excel
=IF(B6="Yes","✅ Compliant",IF(B6="No","❌ Non-Compliant",IF(B6="N/A","N/A","")))
```

### Row 7: Authorization Requirements

- Same structure as Row 6, adjust labels

### Row 8: Input Validation Requirements

- Same structure as Row 6

### Row 9: Cryptography Requirements

- Same structure as Row 6

### Row 10: Logging Requirements

- Same structure as Row 6

### Row 11: API Security Requirements

- Same structure as Row 6

### Row 12: Non-Functional Security Requirements Header

- A12:H12 merged: "1.3 Non-Functional Security Requirements Coverage" (bold, gray fill)

**Rows 13-15:** Non-Functional Requirements

### Row 13: Performance Requirements (Under Security Load)

- Same structure as Row 6

### Row 14: Resilience Requirements (Fail Secure)

- Same structure as Row 6

### Row 15: Secure Defaults

- Same structure as Row 6

### Row 16: Data Protection Requirements Header

- A16:H16 merged: "1.4 Data Protection Requirements Coverage" (bold, gray fill)

**Rows 17-20:** Data Protection Requirements

### Row 17: Data Classification Documented

- Same structure as Row 6

### Row 18: Encryption Requirements

- Same structure as Row 6

### Row 19: Retention Requirements

- Same structure as Row 6

### Row 20: Deletion Requirements

- Same structure as Row 6

### Row 21: Privacy Requirements (if applicable)

- Same structure as Row 6

**Row 23:** Overall SRS Completeness Score

- A23: "Overall SRS Completeness Score" (bold, dark gray fill)
- B23-E23: merged, blank
- F23: Formula (% compliant)
- G23-H23: merged, blank

**F23 Formula:**
```excel
=COUNTIF(F6:F21,"✅ Compliant")/(COUNTIF(B6:B21,"Yes")+COUNTIF(B6:B21,"No"))*100&"%"
```

**Logic:** Count compliant items / Count total applicable items (Yes or No, exclude N/A) × 100%

**Conditional Formatting for F23:**

- If ≥90% → Green fill
- If 70-89% → Yellow fill
- If <70% → Red fill

## Data Validation

**B4, B6:B21 (Yes/No/N/A dropdowns):**
```
=Yes,No,N/A
```

## Conditional Formatting

**Column F (Status) - Apply to F4:F21:**
```
Rule 1: Cell contains "✅" → Fill: RGB(198,239,206)
Rule 2: Cell contains "⚠️" → Fill: RGB(255,235,156)
Rule 3: Cell contains "❌" → Fill: RGB(255,199,206)
Rule 4: Cell contains "N/A" → Fill: RGB(237,237,237)
```

---

# Sheet 4: Threat Modeling Status

## Purpose
Assess threat modeling execution and quality.

## Sheet Structure

**Rows 1-2:** Header Section

- A1:I1 merged: "Threat Modeling Status" (Dark Blue header)
- A2:I2 merged: "Assessment of threat modeling execution for High/Medium-Risk applications" (Blue sub-header)

**Row 3:** Policy Requirement Reminder

- A3:I3 merged: "Policy Requirement: Threat modeling MANDATORY for High-Risk apps, RECOMMENDED for Medium-Risk apps, OPTIONAL for Low-Risk apps" (Bold, yellow fill, wrapped)

**Row 4:** Column Headers
| Column | Header | Width |
|--------|--------|-------|
| A | Assessment Question | 300px |
| B | Answer | 120px |
| C | Details | 300px |
| D | Date | 100px |
| E | Count/Metrics | 120px |
| F | Status | 120px |
| G | Evidence | 250px |
| H | Verified | 100px |
| I | Notes | 200px |

**Rows 5-6:** Threat Modeling Execution

### Row 5: Threat Modeling Conducted?

- A5: "2.1 Was threat modeling conducted?" (bold)
- B5: [Dropdown: Yes/No/N/A] - Yellow fill
- C5: [User Input - Document title & location] - Yellow fill, Wrap text
- D5: [User Input - Date] - Yellow fill, Date format
- E5: N/A (gray fill)
- F5: Formula (see below)
- G5: [User Input - Evidence link] - Yellow fill
- H5: [Dropdown: Yes/No] - Yellow fill
- I5: [User Input] - Yellow fill, Wrap text

**F5 Formula (Status):**
```excel
=IF(B5="Yes",IF(D5<>"",IF((TODAY()-D5)<=365,"✅ Compliant","⚠️ Partial - Outdated"),"⚠️ Partial - No Date"),IF(B5="No",IF('Sheet 2'!B12="High Risk","❌ Non-Compliant - REQUIRED","⚠️ Recommended"),IF(B5="N/A","N/A","")))
```

**Logic:**

- If Yes + Date < 12 months → ✅ Compliant
- If Yes + Date > 12 months → ⚠️ Partial - Outdated
- If No + High-Risk app → ❌ Non-Compliant - REQUIRED
- If No + Medium/Low-Risk → ⚠️ Recommended (not required)
- If N/A → N/A

### Row 6: Methodology Used

- A6: "Methodology Used" (indent)
- B6: [Dropdown] - Yellow fill
  - Data validation: `=STRIDE,PASTA,LINDDUN,Attack Trees,DREAD,Other`
- C6: [User Input - Description if "Other"] - Yellow fill
- D6-E6: N/A
- F6: Formula: `=IF(B6<>"","✅ Documented","❌ Not Documented")`
- G6-I6: [User Input] - Yellow fill

**Rows 7-10:** Threat Modeling Metrics

### Row 7: Threats Identified (Count)

- A7: "Threats Identified (Count)" (indent)
- B7: N/A
- C7: [User Input - Details] - Yellow fill
- D7: N/A
- E7: [User Input - Number] - Yellow fill, Number format
- F7: Formula: `=IF(E7>0,"✅ Threats Identified","❌ No Threats")`
- G7-I7: [User Input] - Yellow fill

### Row 8: Threats Mitigated (Count)

- A8: "Threats Mitigated (Count)" (indent)
- E8: [User Input - Number] - Yellow fill
- F8: Formula: `=IF(AND(E7>0,E8>0),TEXT(E8/E7,"0%")&" Mitigated","")`
- Other columns: [User Input] - Yellow fill

### Row 9: Threats Accepted Risk (Count)

- A9: "Threats Accepted Risk (Count)" (indent)
- E9: [User Input - Number] - Yellow fill
- Other columns: [User Input] - Yellow fill

### Row 10: Threats Outstanding (Count)

- A10: "Threats Outstanding (Count)" (indent)
- E10: Formula: `=IF(AND(E7>0,E8>=0,E9>=0),E7-E8-E9,"")` (auto-calculate)
- F10: Formula: `=IF(E10>0,"⚠️ Outstanding","✅ None Outstanding")`
- Other columns: [User Input] - Yellow fill

**Row 12:** Threat Model Quality Assessment Header

- A12:I12 merged: "2.2 Threat Model Quality Assessment" (bold, gray fill)

**Rows 13-16:** Quality Criteria

### Row 13: Architecture Diagrams Included?

- A13: "Architecture Diagrams Included?" (indent)
- B13: [Dropdown: Yes/No] - Yellow fill
- C13: [User Input - Types of diagrams] - Yellow fill
- F13: Formula: `=IF(B13="Yes","✅ Compliant","❌ Non-Compliant")`
- Other columns: [User Input] - Yellow fill

### Row 14: Trust Boundaries Identified?

- Same structure as Row 13

### Row 15: Countermeasures Documented?

- Same structure as Row 13

### Row 16: Residual Risks Documented?

- Same structure as Row 13

**Row 18:** Overall Threat Modeling Score

- A18: "Overall Threat Modeling Compliance Score" (bold, dark gray fill)
- F18: Formula (% compliant)

**F18 Formula:**
```excel
=COUNTIF(F5:F16,"✅*")/(COUNTIF(F5:F16,"✅*")+COUNTIF(F5:F16,"❌*")+COUNTIF(F5:F16,"⚠️*"))*100&"%"
```

## Conditional Formatting

**Column F (Status):**
```
Rule 1: Cell contains "✅" → Fill: RGB(198,239,206)
Rule 2: Cell contains "⚠️" → Fill: RGB(255,235,156)
Rule 3: Cell contains "❌" → Fill: RGB(255,199,206)
```

**E8 (Mitigation Percentage) - Color scale:**
```
Rule: If <50% → Red, 50-80% → Yellow, >80% → Green
```

---

# Sheet 5: Architecture Review Status

## Purpose
Assess security architecture review execution and findings remediation.

## Sheet Structure

**Similar structure to Sheet 4, adapted for architecture review.**

**Key Rows:**

- Row 5: Architecture Review Conducted? (Yes/No/N/A)
- Row 6: Review Report Title & Location
- Row 7: Reviewer Name (Security Architect)
- Row 8: Review Date
- Row 9: Findings Count (Total)
- Row 10: Critical Findings (Count)
- Row 11: High Findings (Count)
- Row 12: Medium Findings (Count)
- Row 13: Low Findings (Count)
- Row 15: Critical/High Findings Remediated? (Yes/Partial/No)
- Row 17-20: Quality Assessment (Diagrams Reviewed, Controls Validated, Integrations Reviewed, Approval Obtained)
- Row 22: Overall Architecture Review Compliance Score

**Key Formulas:**

**F5 (Architecture Review Status):**
```excel
=IF(B5="Yes",IF(D8<>"",IF((TODAY()-D8)<=365,"✅ Compliant","⚠️ Partial - Outdated"),"⚠️ Partial"),IF(B5="No",IF('Sheet 2'!B12="High Risk","❌ Non-Compliant - REQUIRED","⚠️ Recommended"),"N/A"))
```

**F15 (Critical/High Remediation Status):**
```excel
=IF(B15="Yes - All Remediated","✅ Compliant",IF(B15="Partial","⚠️ Partial",IF(B15="No - Outstanding","❌ Non-Compliant","N/A")))
```

---

# Sheet 6: Requirements Traceability

## Purpose
Assess requirements traceability from specification through implementation to testing.

## Sheet Structure

**Key Rows:**

- Row 5: Traceability Matrix Exists? (Yes/No)
- Row 6: Format/Location
- Row 7: Tool/System Used
- Row 8: Last Updated Date
- Row 10: % Requirements Traced to Design
- Row 11: % Requirements Traced to Implementation
- Row 12: % Requirements Traced to Test Cases
- Row 14: Overall Traceability Score

**Key Formulas:**

**F10-F12 (Traceability Coverage Status):**
```excel
=IF(E10>=90,"✅ Excellent",IF(E10>=80,"✅ Good",IF(E10>=60,"⚠️ Partial","❌ Inadequate")))
```

**F14 (Overall Traceability Score):**
```excel
=AVERAGE(E10,E11,E12)&"%"
```

**Conditional Formatting E10:E12:**
```
Rule 1: >=90 → Green
Rule 2: 80-89 → Light Green
Rule 3: 60-79 → Yellow
Rule 4: <60 → Red
```

---

# Sheet 7: Compliance Checklist

## Purpose
Auto-populated checklist summarizing compliance across all assessment areas.

## Sheet Structure

**Row 1-2:** Header

- A1:E1 merged: "Compliance Checklist - A.8.26 Security Requirements" (Dark Blue header)

**Row 3:** Column Headers
| Column | Header | Width |
|--------|--------|-------|
| A | Checklist Item | 400px |
| B | Compliant? | 120px |
| C | Source Sheet | 120px |
| D | Evidence | 300px |
| E | Notes | 250px |

**Rows 4-25:** Checklist Items (auto-populated from previous sheets)

### Row 4: Application Risk Classified

- A4: "1. Application risk classified (High/Medium/Low)" (with checkbox symbol ☐)
- B4: Formula: `=IF('Sheet 2'!B12<>"","☑ Yes","☐ No")`
- C4: "Sheet 2" (gray fill, protected)
- D4: Formula: `='Sheet 2'!G5` (pull evidence from Sheet 2)
- E4: [User Input] - Yellow fill

**Apply similar pattern for all checklist items:**

- Pull status from relevant sheet
- Convert to ☑ Yes / ☐ No format
- Reference source sheet
- Pull evidence automatically
- Allow notes

**Row 26:** Overall Compliance Score

- A26: "Overall Compliance Rate" (bold, dark gray fill)
- B26: Formula: `=COUNTIF(B4:B25,"☑ Yes")/COUNTA(B4:B25)*100&"%"`
- **Conditional Formatting:**
  - ≥90% → Green fill
  - 70-89% → Yellow fill
  - <70% → Red fill

**Row 27:** Compliance Status

- A27: "Compliance Status" (bold)
- B27: Formula: `=IF(VALUE(LEFT(B26,LEN(B26)-1))>=90,"✅ Compliant",IF(VALUE(LEFT(B26,LEN(B26)-1))>=70,"⚠️ Partial","❌ Non-Compliant"))`

---

# Sheet 8: Gap Analysis & Action Plan

## Purpose
Document identified gaps and remediation plan.

## Sheet Structure

**Row 1-2:** Header

- A1:K1 merged: "Gap Analysis & Remediation Action Plan" (Dark Blue header)

**Row 3:** Column Headers
| Column | Header | Width |
|--------|--------|-------|
| A | Gap ID | 80px |
| B | Gap Description | 300px |
| C | Sheet Reference | 120px |
| D | Severity | 100px |
| E | Policy Requirement | 200px |
| F | Remediation Action | 300px |
| G | Responsible Party | 150px |
| H | Target Date | 100px |
| I | Status | 120px |
| J | Completion Date | 100px |
| K | Evidence of Closure | 250px |

**Rows 4+:** Gap Entries

### Row 4: First Gap (Example)

- A4: "GAP-001" (auto-generate: `="GAP-"&TEXT(ROW()-3,"000")`)
- B4: [User Input - Gap description] - Yellow fill, Wrap text
- C4: [User Input - Sheet reference] - Yellow fill
- D4: [Dropdown] - Yellow fill
  - Data validation: `=Critical,High,Medium,Low`
- E4: [User Input - Policy section violated] - Yellow fill, Wrap text
- F4: [User Input - Remediation action] - Yellow fill, Wrap text
- G4: [User Input - Responsible party name] - Yellow fill
- H4: [User Input - Target date] - Yellow fill, Date format
- I4: [Dropdown] - Yellow fill
  - Data validation: `=Open,In Progress,Resolved,Risk Accepted`
- J4: [User Input - Completion date] - Yellow fill, Date format
- K4: [User Input - Evidence] - Yellow fill, Wrap text

**Conditional Formatting for Column D (Severity):**
```
Rule 1: ="Critical" → Red fill, White text, Bold
Rule 2: ="High" → Orange fill, Black text, Bold
Rule 3: ="Medium" → Yellow fill, Black text
Rule 4: ="Low" → Light blue fill, Black text
```

**Conditional Formatting for Column I (Status):**
```
Rule 1: ="Resolved" → Green fill
Rule 2: ="In Progress" → Yellow fill
Rule 3: ="Open" → White fill
Rule 4: ="Risk Accepted" → Light gray fill
```

**Conditional Formatting for Column H (Target Date) - Overdue Highlighting:**
```
Rule: =AND(H4<TODAY(),I4<>"Resolved",I4<>"Risk Accepted") → Red fill, Bold
```

**Row 100:** Gap Summary

- A100: "Gap Summary" (bold, dark gray fill)
- B100: `=COUNTA(A4:A99)&" Total Gaps"`
- C100: `=COUNTIF(D4:D99,"Critical")&" Critical"`
- D100: `=COUNTIF(D4:D99,"High")&" High"`
- E100: `=COUNTIF(D4:D99,"Medium")&" Medium"`
- F100: `=COUNTIF(D4:D99,"Low")&" Low"`
- I100: `=COUNTIF(I4:I99,"Resolved")&" Resolved, "&COUNTIF(I4:I99,"Open")&" Open"`

---

# Sheet 9: Evidence Register

## Purpose
Centralized register of all evidence supporting assessment.

## Sheet Structure

**Row 1-2:** Header

- A1:J1 merged: "Evidence Register" (Dark Blue header)

**Row 3:** Column Headers
| Column | Header | Width |
|--------|--------|-------|
| A | Evidence ID | 100px |
| B | Evidence Type | 120px |
| C | Evidence Title | 300px |
| D | Evidence Location | 350px |
| E | Date | 100px |
| F | Owner | 150px |
| G | Related Question(s) | 150px |
| H | Verified? | 100px |
| I | Verification Date | 120px |
| J | Verified By | 150px |

**Rows 4+:** Evidence Entries

### Row 4: First Evidence Entry

- A4: "EV-001" (auto-generate: `="EV-"&TEXT(ROW()-3,"000")`)
- B4: [Dropdown] - Yellow fill
  - Data validation: `=Document,Email,Screenshot,Meeting Minutes,Report,Spreadsheet,Tool Export,Other`
- C4: [User Input - Evidence title] - Yellow fill
- D4: [User Input - Location path] - Yellow fill, Wrap text
- E4: [User Input - Date] - Yellow fill, Date format
- F4: [User Input - Owner name] - Yellow fill
- G4: [User Input - Sheet.Question references] - Yellow fill
  - Example: "3.1, 4.1, 5.1"
- H4: [Dropdown: Yes/No/Issue] - Yellow fill
- I4: [User Input - Verification date] - Yellow fill, Date format
- J4: [User Input - Verifier name] - Yellow fill

**Conditional Formatting for Column H (Verified):**
```
Rule 1: ="Yes" → Green fill
Rule 2: ="No" → Yellow fill
Rule 3: ="Issue" → Red fill
```

**Row 100:** Evidence Summary

- A100: "Evidence Summary" (bold, dark gray fill)
- B100: `=COUNTA(A4:A99)&" Total Evidence Items"`
- H100: `=COUNTIF(H4:H99,"Yes")&" Verified, "&COUNTIF(H4:H99,"No")&" Pending, "&COUNTIF(H4:H99,"Issue")&" Issues"`

---

# Sheet 10: Approval & Sign-Off

## Purpose
Document assessment completion, review, and approval.

## Sheet Structure

**Rows 1-10:** Assessment Summary Section

### Row 1-2: Header

- A1:F1 merged: "Assessment Summary & Approval" (Dark Blue header, white text)

### Row 3: Assessment Period

- A3: "Assessment Period:" (bold)
- B3:F3 merged: [User Input] - Yellow fill

### Row 4: Assessment Date

- A4: "Assessment Date:" (bold)
- B4: [User Input - Date] - Yellow fill, Date format
- C4: "Application Name:" (bold)
- D4:F4 merged: Formula: `='Sheet 1'!B4` (auto-pull from Sheet 1)

### Row 5: Application Risk

- A5: "Application Risk:" (bold)
- B5: Formula: `='Sheet 2'!B12` (auto-pull from Sheet 2)
- **Conditional formatting:** Match risk classification colors from Sheet 2

### Row 6: Overall Compliance Score

- A6: "Overall Compliance Score:" (bold)
- B6: Formula: `='Sheet 7'!B26` (auto-pull from Sheet 7)
- **Conditional formatting:** Match compliance color scheme (Green/Yellow/Red)

### Row 7: Critical Gaps

- A7: "Critical Gaps:" (bold)
- B7: Formula: `='Sheet 8'!C100` (auto-pull Critical count from Sheet 8)
- **Conditional formatting:** If >0 → Red fill, Bold

### Row 8: Assessment Status

- A8: "Assessment Status:" (bold)
- B8: [Dropdown] - Yellow fill
  - Data validation: `=Draft,Final,Approved,Requires Remediation`
- **Conditional formatting:**
  - "Approved" → Green fill
  - "Final" → Blue fill
  - "Requires Remediation" → Red fill
  - "Draft" → Gray fill

**Rows 12-20:** Assessment Completed By

### Row 12: Section Header

- A12:F12 merged: "Assessment Completed By" (bold, gray fill)

### Row 13-19: Assessor Information

- A13: "Name:" | B13: [User Input] - Yellow fill
- A14: "Role/Title:" | B14: [User Input] - Yellow fill
- A15: "Department:" | B15: [User Input] - Yellow fill
- A16: "Email:" | B16: [User Input] - Yellow fill
- A17: "Date:" | B17: [User Input - Date] - Yellow fill, Date format
- A18: "Signature:" | B18: [User Input - /s/ Name] - Yellow fill
- A19: "Comments:" | B19:F19 merged: [User Input - Text area] - Yellow fill, Wrap text

**Rows 22-32:** Reviewed By - Security Architect

### Row 22: Section Header

- A22:F22 merged: "Reviewed By - Security Architect" (bold, gray fill)

### Row 23-28: Reviewer Information

- A23: "Name:" | B23: [User Input] - Yellow fill
- A24: "Date:" | B24: [User Input - Date] - Yellow fill, Date format
- A25: "Review Notes:" | B25:F28 merged: [User Input - Text area] - Yellow fill, Wrap text

### Row 29: Recommendation

- A29: "Recommendation:" (bold)
- B29:F29 merged: [Dropdown] - Yellow fill
  - Data validation: `=Approve,Approve with Conditions,Require Remediation,Reject`
- **Conditional formatting:**
  - "Approve" → Green fill
  - "Approve with Conditions" → Yellow fill
  - "Require Remediation" → Orange fill
  - "Reject" → Red fill

**Rows 34-45:** Approved By - CISO (High-Risk Apps Only)

### Row 34: Section Header

- A34:F34 merged: "Approved By - CISO (High-Risk Applications Only)" (bold, gray fill)

### Row 35-40: CISO Information

- A35: "Name:" | B35: [User Input] - Yellow fill
- A36: "Date:" | B36: [User Input - Date] - Yellow fill, Date format
- A37: "Approval Decision:" | B37:F37 merged: [Dropdown] - Yellow fill
  - Data validation: `=Approved,Approved with Conditions,Rejected`
- **Conditional formatting:** Same as Row 29
- A38: "Conditions/Notes:" | B38:F41 merged: [User Input - Text area] - Yellow fill, Wrap text

**Rows 43-48:** Next Review Details

### Row 43: Section Header

- A43:F43 merged: "Next Review Details" (bold, gray fill)

### Row 44-48: Next Review Information

- A44: "Next Assessment Date:" | B44: Formula (auto-calculate based on risk)
- A45: "Review Responsible:" | B45: [User Input] - Yellow fill
- A46: "Special Considerations:" | B46:F48 merged: [User Input - Text area] - Yellow fill, Wrap text

**B44 Formula (Next Assessment Date):**
```excel
=IF('Sheet 2'!B12="High Risk",DATE(YEAR(B17)+0,MONTH(B17)+3,DAY(B17)),DATE(YEAR(B17)+1,MONTH(B17),DAY(B17)))
```
**Logic:** High-Risk = +3 months (quarterly), Medium/Low-Risk = +12 months (annual)

---

# Python Script Integration Points

## Script Filename
`generate_a825_26_29_1_security_requirements.py`

## Key Functions

**1. create_workbook()**
```python
def create_workbook():
    """Initialize workbook with 10 sheets"""
    wb = openpyxl.Workbook()
    # Remove default sheet
    wb.remove(wb.active)
    # Create 10 sheets
    sheet_names = [
        "1. Application Profile",
        "2. Risk Classification",
        "3. Requirements Documentation",
        "4. Threat Modeling",
        "5. Architecture Review",
        "6. Requirements Traceability",
        "7. Compliance Checklist",
        "8. Gap Analysis",
        "9. Evidence Register",
        "10. Approval & Sign-Off"
    ]
    for name in sheet_names:
        wb.create_sheet(title=name)
    return wb
```

**2. setup_styles()**
```python
def setup_styles():
    """Define cell styles for consistent formatting"""
    # Header style
    header_style = NamedStyle(name="header")
    header_style.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    header_style.fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    header_style.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    
    # Similar definitions for sub_header, column_header, input_cell, formula_cell, status styles
    return styles_dict
```

**3. create_application_profile_sheet(ws, styles)**
```python
def create_application_profile_sheet(ws, styles):
    """Create Sheet 1: Application Profile"""
    # Set column widths
    ws.column_dimensions['A'].width = 30
    ws.column_dimensions['B'].width = 45
    # ... etc
    
    # Create headers
    ws.merge_cells('A1:G1')
    ws['A1'] = "Application Profile"
    ws['A1'].style = styles['header']
    
    # Create data rows
    # Row 4: Application Name
    ws['A4'] = "Application Name"
    ws['A4'].font = Font(bold=True)
    ws['B4'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
    
    # Add data validations
    dv = DataValidation(type="list", formula1='"High Risk,Medium Risk,Low Risk"', allow_blank=False)
    ws.add_data_validation(dv)
    dv.add(ws['B5'])  # Apply to specific cells
    
    # Add formulas
    ws['E4'] = '=IF(B4<>"","✅ Complete","❌ Incomplete")'
    
    # Add conditional formatting
    red_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
    rule = Rule(type="containsText", operator="containsText", text="❌", dxf=DifferentialStyle(fill=red_fill))
    ws.conditional_formatting.add('E4:E20', rule)
```

**4. create_risk_classification_sheet(ws, styles)**

- Similar structure for Sheet 2
- Focus on formula creation for weighted scoring
- Conditional formatting for risk thresholds

**5. create_requirements_documentation_sheet(ws, styles)**

- Similar structure for Sheet 3
- Multiple sections (SRS, Functional, Non-Functional, Data Protection)
- Status formulas for each section

**... Similar functions for Sheets 4-10**

**6. Main Execution**
```python
def main():
    # Create workbook
    wb = create_workbook()
    styles = setup_styles()
    
    # Create each sheet
    create_application_profile_sheet(wb['1. Application Profile'], styles)
    create_risk_classification_sheet(wb['2. Risk Classification'], styles)
    create_requirements_documentation_sheet(wb['3. Requirements Documentation'], styles)
    create_threat_modeling_sheet(wb['4. Threat Modeling'], styles)
    create_architecture_review_sheet(wb['5. Architecture Review'], styles)
    create_traceability_sheet(wb['6. Requirements Traceability'], styles)
    create_compliance_checklist_sheet(wb['7. Compliance Checklist'], styles)
    create_gap_analysis_sheet(wb['8. Gap Analysis'], styles)
    create_evidence_register_sheet(wb['9. Evidence Register'], styles)
    create_approval_signoff_sheet(wb['10. Approval & Sign-Off'], styles)
    
    # Save workbook
    filename = f"ISMS-A826-Requirements-Template-{datetime.now().strftime('%Y%m%d')}.xlsx"
    wb.save(filename)
    print(f"✅ Workbook created: {filename}")

if __name__ == "__main__":
    main()
```

## Script Testing Checklist

Before deploying script:

- [ ] All 10 sheets created
- [ ] Column widths correct
- [ ] Headers formatted correctly (colors, fonts, alignment)
- [ ] Data validations applied (dropdowns working)
- [ ] Formulas calculate correctly (test with sample data)
- [ ] Conditional formatting applies (colors appear correctly)
- [ ] Cell protection set (formulas protected, input cells unlocked)
- [ ] File saves without errors
- [ ] File opens in Excel 2016+ without warnings
- [ ] UTF-8 encoding correct (emojis display: ✅ ⚠️ ❌)

---

# Quality Assurance Script

**Script Filename:** `excel_sanity_check_a825_26_29_1.py`

**Purpose:** Validate generated workbook matches specification

**Key Checks:**
1. Verify 10 sheets exist with correct names
2. Validate column widths match specification
3. Check headers formatted correctly
4. Verify data validations present
5. Test formulas with sample data
6. Validate conditional formatting rules
7. Check cell protection settings
8. Verify UTF-8 encoding (emoji check)
9. Test file opens without errors
10. Generate validation report

**Example Validation Function:**
```python
def validate_sheet_structure(wb):
    """Validate sheet structure matches specification"""
    expected_sheets = [
        "1. Application Profile",
        "2. Risk Classification",
        # ... etc
    ]
    
    actual_sheets = wb.sheetnames
    
    if actual_sheets != expected_sheets:
        return False, f"Sheet mismatch: expected {expected_sheets}, got {actual_sheets}"
    
    return True, "✅ All sheets present and correctly named"
```

---

# Freeze Panes Configuration

**All Sheets:**

- Freeze at Row 4 (headers visible when scrolling down)
- Freeze at Column A (question column visible when scrolling right)

**Implementation:**
```python
ws.freeze_panes = 'B4'  # Freeze rows 1-3, column A
```

---

# Print Settings

**Page Setup for All Sheets:**

- Orientation: Landscape
- Paper Size: A4
- Fit to: 1 page wide, multiple pages tall
- Margins: Normal (0.75" left/right, 1" top/bottom)
- Headers: Print titles - Rows 1-3 repeat on each page
- Footers: Page X of Y (center), Date (right), Filename (left)

**Implementation:**
```python
ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
ws.page_setup.paperSize = ws.PAPERSIZE_A4
ws.page_setup.fitToWidth = 1
ws.page_setup.fitToHeight = 0  # Auto
ws.print_title_rows = '1:3'  # Repeat rows 1-3 on each page
```

---

# Version Control & Change Tracking

**Document Version Tracking:**

- Version documented in Document Control (Sheet 1, Row 1 or dedicated metadata)
- Version history maintained separately
- Filename includes date: `ISMS-A826-Requirements-APP-XXX-YYYYMMDD-v2.0.xlsx`

**Change Log Sheet (Optional):**

- Add hidden sheet "Change Log" documenting workbook modifications
- Track: Date, Version, Changes, Modified By

---

# File Size Optimization

**Tips to keep file size manageable:**
1. Don't embed large images (link instead)
2. Remove unused styles and formats
3. Clear formatting from unused cells
4. Don't save calculated formula results (recalc on open)
5. Use references instead of copying data

**Target File Size:** <2MB (typical: 500KB-1MB)

---

# Browser Compatibility (Office 365 Online)

**If workbook will be used in Excel Online:**

- Avoid VBA macros (not supported)
- Test all formulas (some advanced formulas may not work)
- Simplify conditional formatting (complex rules may not render)
- Limit data validation complexity
- Test on Office 365 before deployment

---

# Accessibility Considerations

**For users with disabilities:**

- Use high-contrast colors (current color scheme complies)
- Provide alt text for non-text content
- Use clear, simple language in instructions
- Ensure keyboard navigation works (tab order logical)
- Test with screen readers (JAWS, NVDA)

---

# Deployment Checklist

Before deploying workbook to users:

- [ ] All sheets tested with sample data
- [ ] Formulas calculate correctly
- [ ] Data validations work (dropdowns function)
- [ ] Conditional formatting displays correctly
- [ ] Colors and fonts match specification
- [ ] File opens in Excel 2016+ without errors
- [ ] File opens in Excel Online (if required)
- [ ] Print preview looks correct
- [ ] User guide (PART I) provided to users
- [ ] Training conducted (if needed)
- [ ] Support contact information provided
- [ ] Evidence repository folder structure created
- [ ] Assessment schedule established

---

# Maintenance & Updates

**When to update workbook template:**

- Policy changes (ISMS-POL-A.8.25-26-29 updates)
- User feedback (usability improvements)
- Formula errors discovered
- New requirements added
- Compliance scoring methodology changes

**Update Process:**
1. Document requested change
2. Update specification (this PART II)
3. Update Python script
4. Test updated workbook
5. Run QA script
6. Update version number
7. Deploy to users
8. Communicate changes

**Backward Compatibility:**

- Maintain compatibility with previous versions where possible
- Provide migration script if breaking changes
- Document migration process in version history

---

# Appendix: Technical Notes for Developers

## Excel Formula Best Practices

**Use Named Ranges:**
```
Define named range: RiskScore = 'Sheet 2'!D10
Reference in formulas: =IF(RiskScore>=3.5,"High Risk","Medium Risk")
```
**Benefit:** More readable formulas, easier maintenance

**Use INDIRECT() for Dynamic References:**
```excel
=INDIRECT("Sheet 2!B"&ROW())
```
**Use case:** When cell reference needs to be calculated

**Use IFERROR() for Robust Formulas:**
```excel
=IFERROR(E7/E8*100&" %","N/A")
```
**Benefit:** Prevents #DIV/0!, #VALUE! errors

## Python openpyxl Tips

**Merging Cells:**
```python
ws.merge_cells('A1:G1')
ws['A1'] = "Header Text"  # Only set value on first cell
```

**Data Validation:**
```python
from openpyxl.worksheet.datavalidation import DataValidation

dv = DataValidation(type="list", formula1='"Option1,Option2,Option3"')
ws.add_data_validation(dv)
dv.add('B5')  # Apply to cell B5
dv.add('B6:B10')  # Apply to range
```

**Conditional Formatting:**
```python
from openpyxl.formatting.rule import Rule, CellIsRule
from openpyxl.styles import PatternFill

green_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
rule = CellIsRule(operator="containsText", formula=['"✅"'], fill=green_fill)
ws.conditional_formatting.add('E4:E20', rule)
```

**Formula References:**
```python
# Absolute reference
ws['B5'] = '=$A$1 + $A$2'

# Relative reference
ws['B5'] = '=A1 + A2'

# Mixed reference
ws['B5'] = '=$A1 + A$2'
```

## Common Pitfalls to Avoid

**Pitfall 1: Excel Date Format**

- Python datetime → Excel serial date
- Use `ws.cell().number_format = 'DD.MM.YYYY'`

**Pitfall 2: UTF-8 Encoding**

- Emojis (✅ ⚠️ ❌) require UTF-8
- Use `wb.save(filename, encoding='utf-8')` (openpyxl handles automatically)

**Pitfall 3: Formula Calculation**

- Excel doesn't auto-calculate on open by default in scripts
- Set `wb.calculation.calcMode = 'auto'`

**Pitfall 4: Large Files**

- Conditional formatting on large ranges = slow performance
- Limit CF rules to necessary ranges only

**Pitfall 5: Protected Sheets**

- Set `ws.protection.password = None` (no password for user sheets)
- Lock formula cells, unlock input cells explicitly

---

**END OF SPECIFICATION**

---

*"I remember once going to see him when he was ill at Putney. I had ridden in taxi cab number 1729 and remarked that the number seemed to me rather a dull one."*
— G.H. Hardy, about Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->
