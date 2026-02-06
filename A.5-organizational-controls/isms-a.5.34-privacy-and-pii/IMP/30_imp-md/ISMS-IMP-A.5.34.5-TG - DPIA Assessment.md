**ISMS-IMP-A.5.34.5-TG - Data Protection Impact Assessment (DPIA)**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.34.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Data Protection Impact Assessment (DPIA) for High-Risk Processing Activities |
| **Related Policy** | ISMS-POL-A.5.34, Section 2.5 (Data Protection Impact Assessment) |
| **Purpose** | Guide users through DPIA trigger assessment, systematic risk evaluation, and compliance with GDPR Article 35 requirements for high-risk processing activities |
| **Target Audience** | DPO/Privacy Officers, Legal Counsel, Business Owners, Product Managers, IT/Security Teams, Compliance Officers, Auditors |
| **Assessment Type** | Risk Assessment & Compliance |
| **Review Cycle** | Annual or upon introduction of new high-risk processing activities |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for DPIA assessment workbook | ISMS Implementation Team |

---

**Document Purpose**

This implementation guide specifies procedures for conducting Data Protection Impact Assessments (DPIAs) as required by GDPR Article 35. A DPIA is a systematic process to evaluate the necessity, proportionality, and risks of processing operations that are likely to result in high risk to individuals' rights and freedoms.

**Key Objectives:**
1. Identify processing activities requiring DPIA (trigger assessment)
2. Conduct systematic risk assessment for high-risk processing
3. Implement appropriate mitigation measures to reduce risks
4. Maintain comprehensive DPIA register for audit and compliance
5. Ensure stakeholder consultation (DPO, data subjects, supervisory authority)
6. Track DPIA lifecycle from initial assessment through annual reviews

**Regulatory Foundation:**

**GDPR Article 35(1):** "Where a type of processing in particular using new technologies, and taking into account the nature, scope, context and purposes of the processing, is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall, prior to the processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data."

**GDPR Article 35(3) - Mandatory DPIA Triggers:**

- (a) Systematic and extensive evaluation of personal aspects including profiling with legal/similarly significant effects
- (b) Large-scale processing of special category data (Art. 9) or criminal convictions (Art. 10)
- (c) Systematic monitoring of publicly accessible areas on a large scale (e.g., CCTV)

**Additional WP248 Triggers:**

- Innovative technologies or novel applications of existing technology
- Processing that prevents data subjects from exercising rights or using services
- Processing on a large scale
- Matching/combining datasets from different sources
- Processing vulnerable data subjects (children, employees, mentally ill)
- Processing involving cross-border data transfers outside EEA
- Decisions with potential to cause significant harm (automated decision-making)

**ISO/IEC 27001:2022 Control A.5.34 Requirement:** Organizations must implement privacy impact assessments when required by applicable privacy regulations.

---

# Technical Specification

**Target Audience:** Python Developers, System Administrators, Excel Power Users, Automation Engineers

**Purpose:** This section provides exact technical specifications for implementing the DPIA assessment workbook. All column definitions, data validation rules, conditional formatting, and Excel formulas are specified precisely to enable implementation without ambiguity.

---

### Global Workbook Settings

**File Format:** `.xlsx` (Excel 2007+ format)  
**Workbook Protection:** Structure locked (prevent sheet addition/deletion/reordering)  
**Default Font:** Calibri 11pt  
**Default Row Height:** 15 points  
**Default Column Width:** Auto-fit to content (minimum 10 characters)  
**Calculation Mode:** Automatic  
**Iteration:** Disabled (no circular references)

**Named Ranges (Workbook-Level):**

- `RiskLevels`: {"Low", "Medium", "High", "Critical"}
- `YesNoOptions`: {"Yes", "No"}
- `YesNoUncertain`: {"Yes", "No", "Uncertain"}
- `YesNoNA`: {"Yes", "No", "N/A"}
- `YesNoPartial`: {"Yes", "No", "Partial"}

---

### SHEET 1: Instructions & Legend

**Sheet Name:** `Instructions`  
**Tab Color:** RGB(68, 114, 196) - Blue  
**Protection:** Locked (read-only for users)  
**Print Settings:** Fit to 1 page wide, portrait orientation

**Content Structure:**

| Section | Rows | Content Type | Formatting |
|---------|------|--------------|------------|
| Header | 1-3 | Title block | Font: Arial 16pt Bold, Fill: RGB(68, 114, 196), Font Color: White |
| Overview | 4-15 | Instructional text | Font: Calibri 11pt, Wrap text enabled |
| Navigation Guide | 16-30 | Sheet descriptions | Font: Calibri 11pt, Bullet points |
| Terminology | 31-50 | Definitions | Font: Calibri 11pt, Two-column layout |
| Risk Methodology | 51-75 | Risk scoring logic | Font: Calibri 11pt, Tables with borders |
| Color Coding | 76-85 | Legend | Cells filled with actual colors used |
| Evidence | 86-100 | Requirements | Font: Calibri 11pt, Checklist format |
| Common Pitfalls | 101-120 | Warnings | Font: Calibri 11pt, Icons: ⚠️ |

**Cell Merging:**

- Title: A1:P3 (merged, centered)
- Section headers: Full row span (A:P)

**No Data Validation:** Sheet is pre-populated template, no user input

**No Formulas:** Static content only

**Implementation Notes:**

- Content from PART 1 Section "SHEET 1: Instructions & Legend" should be formatted as specified
- Use rich text formatting (bold, italic, underline) for emphasis
- Include hyperlinks to external resources (GDPR Article 35 official text, WP248 guidelines PDF)

---

### SHEET 2: DPIA Trigger Assessment

**Sheet Name:** `Trigger_Assessment`  
**Tab Color:** RGB(255, 192, 0) - Orange  
**Protection:** Unlocked cells: B2:O1000 (user input area), All other cells locked  
**Freeze Panes:** Row 1 (header row frozen)  
**Print Settings:** Fit to 1 page wide, landscape orientation, repeat header row on each page

#### Row 1: Column Headers

| Column | Header Text | Width | Format |
|--------|------------|-------|--------|
| A | Processing Activity ID | 20 | Bold, Fill: RGB(68, 114, 196), Font: White, Center-aligned |
| B | Processing Activity Name | 30 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| C | System/Application | 25 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| D | Trigger 1: Systematic Profiling | 18 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| E | Trigger 2: Large-Scale Special Categories | 18 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| F | Trigger 3: Systematic Monitoring | 18 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| G | Trigger 4: Innovative Technology | 18 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| H | Trigger 5: Denial of Service | 18 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| I | Trigger 6: Large Scale | 18 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| J | Trigger 7: Matching Datasets | 18 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| K | Trigger 8: Vulnerable Subjects | 18 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| L | Trigger 9: Cross-Border Transfer | 18 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| M | Total Triggers | 12 | Bold, Fill: RGB(68, 114, 196), Font: White, Center-aligned |
| N | DPIA Required? | 15 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| O | Notes | 40 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |

#### Data Rows (Rows 2-1000)

**Column A: Processing Activity ID**

- **Data Type:** Text
- **Validation:** List from external source

  ```
  Source: =ISMS_A5341_Sheet2!$A$2:$A$1000
  (Reference to A.5.34.1 PII Identification workbook, Sheet 2: System Inventory)
  ```
  Note: External reference assumes A.5.34.1 workbook is in same directory
  Fallback if workbook not found: Allow any text input (no validation)

- **Format:** Text, left-aligned
- **Required:** Yes (cannot be blank)
- **Example:** `PROC-001`

**Column B: Processing Activity Name**

- **Data Type:** Text
- **Validation:** 

  ```
  Type: Text length
  Minimum: 1 character
  Maximum: 100 characters
  Error message: "Processing name must be 1-100 characters"
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** Yes
- **Example:** `AI-powered resume screening system`

**Column C: System/Application**

- **Data Type:** Text
- **Validation:**

  ```
  Type: Text length
  Maximum: 100 characters
  Error message: "System name must be max 100 characters"
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** Yes
- **Example:** `Workday ATS + Custom ML Module`

**Column D: Trigger 1 - Systematic Profiling**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Yes,No"
  Error style: Stop
  Error message: "Select Yes or No"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Default:** `No`

**Column E: Trigger 2 - Large-Scale Special Categories**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Yes,No"
  Error style: Stop
  Error message: "Select Yes or No"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Default:** `No`

**Column F: Trigger 3 - Systematic Monitoring**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Yes,No"
  Error style: Stop
  Error message: "Select Yes or No"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Default:** `No`

**Column G: Trigger 4 - Innovative Technology**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Yes,No"
  Error style: Stop
  Error message: "Select Yes or No"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Default:** `No`

**Column H: Trigger 5 - Denial of Service**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Yes,No"
  Error style: Stop
  Error message: "Select Yes or No"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Default:** `No`

**Column I: Trigger 6 - Large Scale**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Yes,No"
  Error style: Stop
  Error message: "Select Yes or No"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Default:** `No`

**Column J: Trigger 7 - Matching Datasets**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Yes,No"
  Error style: Stop
  Error message: "Select Yes or No"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Default:** `No`

**Column K: Trigger 8 - Vulnerable Subjects**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Yes,No"
  Error style: Stop
  Error message: "Select Yes or No"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Default:** `No`

**Column L: Trigger 9 - Cross-Border Transfer**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Yes,No"
  Error style: Stop
  Error message: "Select Yes or No"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Default:** `No`

**Column M: Total Triggers**

- **Data Type:** Calculated (Integer)
- **Formula (Row 2):**

  ```excel
  =COUNTIF(D2:L2,"Yes")
  ```

- **Format:** Number, 0 decimal places, center-aligned
- **Conditional Formatting:**
  - Rule 1: `=M2=0` → Fill: RGB(146, 208, 80) - Light Green
  - Rule 2: `=M2=1` → Fill: RGB(255, 217, 102) - Yellow
  - Rule 3: `=M2>=2` → Fill: RGB(255, 102, 102) - Light Red
- **Auto-fill:** Copy formula to M2:M1000

**Column N: DPIA Required?**

- **Data Type:** Calculated (Text)
- **Formula (Row 2):**

  ```excel
  =IF(M2>=2,"Yes",IF(M2=1,"Uncertain","No"))
  ```

- **Format:** Text, center-aligned, bold
- **Conditional Formatting:**
  - Rule 1: `=N2="No"` → Fill: RGB(146, 208, 80) - Light Green, Font: RGB(0, 97, 0) - Dark Green
  - Rule 2: `=N2="Uncertain"` → Fill: RGB(255, 217, 102) - Yellow, Font: RGB(156, 87, 0) - Dark Orange
  - Rule 3: `=N2="Yes"` → Fill: RGB(255, 102, 102) - Light Red, Font: RGB(156, 0, 6) - Dark Red
- **Auto-fill:** Copy formula to N2:N1000

**Column O: Notes**

- **Data Type:** Text
- **Validation:**

  ```
  Type: Text length
  Maximum: 500 characters
  Error message: "Notes must be max 500 characters"
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** No (optional)
- **Example:** `DPO consulted 2024-03-15: Not large scale (<2,000 subjects), DPIA not required despite special category data`

#### Conditional Formatting (Entire Row)

**Rule 1: Highlight rows requiring DPIA**

- **Applies to:** $A$2:$O$1000
- **Condition:** `=$N2="Yes"`
- **Format:** Fill: RGB(255, 230, 230) - Very Light Red (row background)

**Rule 2: Highlight uncertain rows**

- **Applies to:** $A$2:$O$1000
- **Condition:** `=$N2="Uncertain"`
- **Format:** Fill: RGB(255, 243, 205) - Very Light Yellow (row background)

#### Data Validation Comments

**Columns D-L (All trigger columns):**

- Add comment (Note) to header cells with trigger definition:
  - D1: "Automated decision-making with legal/significant effects (Art. 35(3)(a))"
  - E1: "Large-scale processing of special category data (Art. 9) or criminal data (Art. 10)"
  - F1: "Systematic monitoring of public areas on large scale (e.g., CCTV)"
  - G1: "Novel technology or novel application of existing tech (AI, blockchain, IoT)"
  - H1: "Processing prevents data subjects from accessing services or exercising rights"
  - I1: "Large scale: >5,000 data subjects OR substantial proportion of population"
  - J1: "Combining datasets from different sources/controllers beyond original purpose"
  - K1: "Children <16, employees, refugees, elderly, mentally ill, prisoners"
  - L1: "Transfers outside EEA without adequacy decision (even with SCCs)"

#### Worksheet Protection

**Protected Elements:**

- Column headers (Row 1)
- Formula columns (M, N)
- Sheet structure

**Unprotected Elements (Allow Edit):**

- A2:L1000 (user input area for Processing Activity details and trigger assessment)
- O2:O1000 (Notes column)

**Protection Password:** Set by organization (recommended: complex password stored in password manager)

---

### SHEET 3: DPIA Register

**Sheet Name:** `DPIA_Register`  
**Tab Color:** RGB(112, 173, 71) - Green  
**Protection:** Unlocked cells: A2:R1000 (user input area for most columns), Column P locked (calculated field)  
**Freeze Panes:** Row 1 (header row frozen)  
**Print Settings:** Fit to 1 page wide, landscape orientation, repeat header row on each page

#### Row 1: Column Headers

| Column | Header Text | Width | Format |
|--------|------------|-------|--------|
| A | DPIA ID | 18 | Bold, Fill: RGB(112, 173, 71), Font: White, Center-aligned |
| B | Processing Activity ID | 20 | Bold, Fill: RGB(112, 173, 71), Font: White, Center-aligned |
| C | Processing Activity Name | 30 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| D | System/Application | 25 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| E | Business Owner | 20 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| F | DPO Assigned | 20 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| G | DPIA Start Date | 15 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| H | Target Completion Date | 15 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| I | Actual Completion Date | 15 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| J | DPIA Status | 15 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| K | Initial Risk Rating | 15 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| L | Residual Risk Rating | 15 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| M | Supervisory Authority Consulted? | 18 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| N | Authority Consultation Date | 15 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| O | Authority Reference Number | 20 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| P | Next Review Date | 15 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| Q | DPIA Document Location | 40 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| R | Notes | 40 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |

#### Data Rows (Rows 2-1000)

**Column A: DPIA ID**

- **Data Type:** Text
- **Format:** Text, center-aligned
- **Validation:**

  ```
  Type: Custom
  Formula: =AND(LEN(A2)>0, LEN(A2)<=20)
  Error message: "DPIA ID must be 1-20 characters (e.g., DPIA-2024-001)"
  ```

- **Required:** Yes
- **Naming Convention:** `DPIA-YYYY-NNN` (e.g., DPIA-2024-001)
- **Example:** `DPIA-2024-001`

**Column B: Processing Activity ID**

- **Data Type:** Text
- **Validation:**

  ```
  Type: List
  Source: =Trigger_Assessment!$A$2:$A$1000
  Error message: "Select from Trigger Assessment sheet"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Example:** `PROC-001`

**Column C: Processing Activity Name**

- **Data Type:** Calculated (Text)
- **Formula (Row 2):**

  ```excel
  =IF(ISBLANK(B2),"",IFERROR(VLOOKUP(B2,Trigger_Assessment!$A$2:$B$1000,2,FALSE),"Not Found"))
  ```

- **Format:** Text, left-aligned, wrap text
- **Auto-fill:** Copy formula to C2:C1000
- **Protected:** Yes (calculated field)

**Column D: System/Application**

- **Data Type:** Calculated (Text)
- **Formula (Row 2):**

  ```excel
  =IF(ISBLANK(B2),"",IFERROR(VLOOKUP(B2,Trigger_Assessment!$A$2:$C$1000,3,FALSE),"Not Found"))
  ```

- **Format:** Text, left-aligned, wrap text
- **Auto-fill:** Copy formula to D2:D1000
- **Protected:** Yes (calculated field)

**Column E: Business Owner**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="HR,IT,Marketing,Sales,Finance,Legal,Operations,Product,Engineering,Other"
  Error message: "Select department from list"
  ```

- **Format:** Text, left-aligned
- **Required:** Yes
- **Example:** `HR`

**Column F: DPO Assigned**

- **Data Type:** Text
- **Format:** Text, left-aligned
- **Validation:**

  ```
  Type: Text length
  Maximum: 100 characters
  Error message: "DPO name must be max 100 characters"
  ```

- **Required:** Yes
- **Example:** `Jane Smith (Internal DPO)`

**Column G: DPIA Start Date**

- **Data Type:** Date
- **Validation:**

  ```
  Type: Date
  Date: between 2020-01-01 and 2099-12-31
  Error message: "Enter valid date (YYYY-MM-DD)"
  ```

- **Format:** Date, `YYYY-MM-DD`
- **Required:** Yes
- **Example:** `2024-03-01`

**Column H: Target Completion Date**

- **Data Type:** Date
- **Validation:**

  ```
  Type: Date
  Date: between G2 and 2099-12-31 (must be >= Start Date)
  Error message: "Target date must be >= Start Date"
  ```

- **Format:** Date, `YYYY-MM-DD`
- **Required:** Yes
- **Example:** `2024-04-30`

**Column I: Actual Completion Date**

- **Data Type:** Date
- **Validation:**

  ```
  Type: Date
  Date: between G2 and 2099-12-31
  Error message: "Completion date must be >= Start Date"
  ```

- **Format:** Date, `YYYY-MM-DD`
- **Required:** No (blank until DPIA complete)
- **Example:** `2024-04-15`

**Column J: DPIA Status**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Planned,In Progress,Under Review,Complete,Overdue"
  Error message: "Select status from list"
  ```

- **Format:** Text, center-aligned, bold
- **Conditional Formatting:**
  - Rule 1: `=J2="Complete"` → Fill: RGB(146, 208, 80) - Light Green, Font: RGB(0, 97, 0) - Dark Green
  - Rule 2: `=J2="In Progress"` → Fill: RGB(255, 217, 102) - Yellow, Font: RGB(156, 87, 0) - Dark Orange
  - Rule 3: `=J2="Overdue"` → Fill: RGB(255, 102, 102) - Light Red, Font: RGB(156, 0, 6) - Dark Red
  - Rule 4: `=J2="Under Review"` → Fill: RGB(180, 198, 231) - Light Blue, Font: RGB(0, 32, 96) - Dark Blue
  - Rule 5: `=J2="Planned"` → Fill: RGB(217, 217, 217) - Light Gray, Font: Black
- **Required:** Yes
- **Example:** `In Progress`

**Column K: Initial Risk Rating**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Low,Medium,High,Critical"
  Error message: "Select risk level from list"
  ```

- **Format:** Text, center-aligned, bold
- **Conditional Formatting:**
  - Rule 1: `=K2="Low"` → Fill: RGB(146, 208, 80) - Light Green, Font: RGB(0, 97, 0) - Dark Green
  - Rule 2: `=K2="Medium"` → Fill: RGB(255, 217, 102) - Yellow, Font: RGB(156, 87, 0) - Dark Orange
  - Rule 3: `=K2="High"` → Fill: RGB(255, 165, 0) - Orange, Font: RGB(156, 0, 6) - Dark Red
  - Rule 4: `=K2="Critical"` → Fill: RGB(255, 102, 102) - Light Red, Font: RGB(156, 0, 6) - Dark Red, Bold
- **Required:** Yes (populate from Sheet 4 highest risk score)
- **Example:** `High`

**Column L: Residual Risk Rating**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Low,Medium,High,Critical"
  Error message: "Select risk level from list"
  ```

- **Format:** Text, center-aligned, bold
- **Conditional Formatting:** Same as Column K
- **Required:** No (blank until mitigation complete, populate from Sheet 7)
- **Example:** `Medium`

**Column M: Supervisory Authority Consulted?**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Yes,No,N/A"
  Error message: "Select from list"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Logic:** "Yes" if L (Residual Risk) = High or Critical
- **Example:** `No`

**Column N: Authority Consultation Date**

- **Data Type:** Date
- **Validation:**

  ```
  Type: Date
  Date: between 2020-01-01 and 2099-12-31
  Error message: "Enter valid date (YYYY-MM-DD)"
  ```

- **Format:** Date, `YYYY-MM-DD`
- **Required:** Only if M = "Yes"
- **Example:** `2024-05-01`

**Column O: Authority Reference Number**

- **Data Type:** Text
- **Format:** Text, left-aligned
- **Validation:**

  ```
  Type: Text length
  Maximum: 50 characters
  ```

- **Required:** Only if M = "Yes"
- **Example:** `ICO-DPIA-2024-12345`

**Column P: Next Review Date**

- **Data Type:** Calculated (Date)
- **Formula (Row 2):**

  ```excel
  =IF(ISBLANK(I2),"",DATE(YEAR(I2)+1,MONTH(I2),DAY(I2)))
  ```
  Alternative formula using EDATE (if available):
  ```excel
  =IF(ISBLANK(I2),"",EDATE(I2,12))
  ```

- **Format:** Date, `YYYY-MM-DD`
- **Auto-fill:** Copy formula to P2:P1000
- **Protected:** Yes (calculated field)
- **Conditional Formatting:**
  - Rule 1: `=AND(NOT(ISBLANK(P2)), P2<=TODAY()+30)` → Fill: RGB(255, 102, 102) - Light Red (review due soon/overdue)
  - Rule 2: `=AND(NOT(ISBLANK(P2)), P2<=TODAY()+90, P2>TODAY()+30)` → Fill: RGB(255, 217, 102) - Yellow (review upcoming)

**Column Q: DPIA Document Location**

- **Data Type:** Text (file path or URL)
- **Format:** Text, left-aligned, wrap text
- **Validation:**

  ```
  Type: Text length
  Maximum: 500 characters
  Error message: "File path must be max 500 characters"
  ```

- **Required:** Yes (once DPIA complete)
- **Example:** `/DPIAs/DPIA-2024-001/DPIA-Report-Final.pdf`

**Column R: Notes**

- **Data Type:** Text
- **Format:** Text, left-aligned, wrap text
- **Validation:**

  ```
  Type: Text length
  Maximum: 500 characters
  Error message: "Notes must be max 500 characters"
  ```

- **Required:** No
- **Example:** `Retroactive DPIA for legacy system - processing stopped pending mitigation implementation`

#### Conditional Formatting (Entire Row)

**Rule 1: Highlight overdue DPIAs**

- **Applies to:** $A$2:$R$1000
- **Condition:** `=AND($J2="Overdue", OR(NOT(ISBLANK($A2)), NOT(ISBLANK($B2))))`
- **Format:** Fill: RGB(255, 230, 230) - Very Light Red (row background), Font: Bold

**Rule 2: Highlight complete DPIAs**

- **Applies to:** $A$2:$R$1000
- **Condition:** `=$J2="Complete"`
- **Format:** Fill: RGB(235, 248, 233) - Very Light Green (row background)

**Rule 3: Highlight high/critical residual risk**

- **Applies to:** $A$2:$R$1000
- **Condition:** `=OR($L2="High", $L2="Critical")`
- **Format:** Fill: RGB(255, 242, 204) - Very Light Orange (row background), Left border: 4pt RGB(255, 0, 0) - Red

#### Worksheet Protection

**Protected Elements:**

- Column headers (Row 1)
- Calculated columns (C, D, P)
- Sheet structure

**Unprotected Elements:**

- A2:B1000, E2:O1000, Q2:R1000 (user input areas)

---

### SHEET 4: Risk Assessment Matrix

**Sheet Name:** `Risk_Assessment`  
**Tab Color:** RGB(255, 102, 102) - Red  
**Protection:** Unlocked cells: A2:G1000, J2:T1000 (user input), Columns H-I locked (calculated)  
**Freeze Panes:** Row 1 (header row frozen)  
**Print Settings:** Fit to 1 page wide, landscape orientation, repeat header row on each page

#### Row 1: Column Headers

| Column | Header Text | Width | Format |
|--------|------------|-------|--------|
| A | DPIA ID | 18 | Bold, Fill: RGB(192, 0, 0), Font: White, Center-aligned |
| B | Risk ID | 20 | Bold, Fill: RGB(192, 0, 0), Font: White, Center-aligned |
| C | Risk Category | 20 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| D | Risk Description | 50 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| E | Data Subject Impact | 40 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| F | Likelihood (Before Mitigation) | 15 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| G | Impact (Before Mitigation) | 15 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| H | Inherent Risk Score | 12 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| I | Inherent Risk Level | 15 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| J | Necessity Justified? | 15 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| K | Necessity Justification | 40 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| L | Proportionality Justified? | 15 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| M | Proportionality Justification | 40 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| N | Legal Basis | 20 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| O | Special Category Legal Basis | 20 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| P | Data Subject Rights Respected? | 15 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| Q | Rights Restrictions Documented | 40 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| R | Third-Party Recipients | 30 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| S | Cross-Border Transfers | 15 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |
| T | Transfer Safeguards | 30 | Bold, Fill: RGB(192, 0, 0), Font: White, Wrap text |

#### Data Rows (Rows 2-1000)

**Column A: DPIA ID**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: =DPIA_Register!$A$2:$A$1000
  Error message: "Select DPIA ID from register"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Example:** `DPIA-2024-001`

**Column B: Risk ID**

- **Data Type:** Calculated (Text)
- **Formula (Row 2):**

  ```excel
  =IF(ISBLANK(A2),"",A2&"-R"&TEXT(COUNTIF($A$2:A2,A2),"00"))
  ```
  This generates sequential risk IDs per DPIA: DPIA-2024-001-R01, DPIA-2024-001-R02, etc.

- **Format:** Text, center-aligned
- **Auto-fill:** Copy formula to B2:B1000
- **Protected:** Yes (calculated field)

**Column C: Risk Category**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Discrimination,Identity Theft/Fraud,Financial Loss,Reputational Damage,Physical Harm,Loss of Confidentiality,Loss of Control,Surveillance,Profiling with Significant Effects,Social Disadvantage,Psychological Harm,Loss of Rights/Freedoms"
  Error message: "Select risk category from list"
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** Yes
- **Example:** `Profiling with Significant Effects`

**Column D: Risk Description**

- **Data Type:** Text
- **Validation:**

  ```
  Type: Text length
  Minimum: 50 characters
  Maximum: 500 characters
  Error message: "Risk description must be 50-500 characters (be specific)"
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** Yes
- **Example:** `AI resume screening automatically rejects candidates based on keyword matching without human review. Algorithm may perpetuate historical hiring biases (e.g., rejecting candidates from certain universities or with career gaps), resulting in discriminatory outcomes prohibited under employment law.`

**Column E: Data Subject Impact**

- **Data Type:** Text
- **Validation:**

  ```
  Type: Text length
  Minimum: 30 characters
  Maximum: 300 characters
  Error message: "Impact description must be 30-300 characters"
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** Yes
- **Example:** `Qualified candidates unfairly rejected, losing employment opportunities. Disproportionate impact on protected classes (age, gender, race). Violation of right to fair consideration and non-discrimination.`

**Column F: Likelihood (Before Mitigation)**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="1 - Rare,2 - Unlikely,3 - Possible,4 - Likely,5 - Almost Certain"
  Error message: "Select likelihood from 1-5 scale"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Example:** `4 - Likely`

**Column G: Impact (Before Mitigation)**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="1 - Negligible,2 - Minor,3 - Moderate,4 - Major,5 - Severe"
  Error message: "Select impact from 1-5 scale"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Example:** `4 - Major`

**Column H: Inherent Risk Score**

- **Data Type:** Calculated (Integer)
- **Formula (Row 2):**

  ```excel
  =IF(OR(ISBLANK(F2),ISBLANK(G2)),"",VALUE(LEFT(F2,1))*VALUE(LEFT(G2,1)))
  ```
  This extracts the numeric value from likelihood/impact dropdowns and multiplies

- **Format:** Number, 0 decimal places, center-aligned, bold
- **Auto-fill:** Copy formula to H2:H1000
- **Protected:** Yes (calculated field)
- **Conditional Formatting:**
  - Rule 1: `=AND(H2>=1, H2<=6)` → Fill: RGB(146, 208, 80) - Light Green, Font: RGB(0, 97, 0) - Dark Green
  - Rule 2: `=AND(H2>=8, H2<=12)` → Fill: RGB(255, 217, 102) - Yellow, Font: RGB(156, 87, 0) - Dark Orange
  - Rule 3: `=AND(H2>=15, H2<=16)` → Fill: RGB(255, 165, 0) - Orange, Font: RGB(156, 0, 6) - Dark Red
  - Rule 4: `=H2>=20` → Fill: RGB(255, 102, 102) - Light Red, Font: RGB(156, 0, 6) - Dark Red, Bold

**Column I: Inherent Risk Level**

- **Data Type:** Calculated (Text)
- **Formula (Row 2):**

  ```excel
  =IF(ISBLANK(H2),"",IF(H2>=20,"Critical",IF(H2>=15,"High",IF(H2>=8,"Medium","Low"))))
  ```

- **Format:** Text, center-aligned, bold
- **Auto-fill:** Copy formula to I2:I1000
- **Protected:** Yes (calculated field)
- **Conditional Formatting:** Same as Column H

**Column J: Necessity Justified?**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Yes,No,Uncertain"
  Error message: "Select from list"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Example:** `Yes`

**Column K: Necessity Justification**

- **Data Type:** Text
- **Validation:**

  ```
  Type: Text length
  Minimum: 30 characters
  Maximum: 300 characters
  Error message: "Justification must be 30-300 characters"
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** Yes
- **Example:** `Automated screening necessary to handle volume (500+ applications per role). Manual review of all applications not feasible. However, human-in-the-loop review required before final rejection.`

**Column L: Proportionality Justified?**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Yes,No,Uncertain"
  Error message: "Select from list"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Example:** `Yes`

**Column M: Proportionality Justification**

- **Data Type:** Text
- **Validation:**

  ```
  Type: Text length
  Minimum: 30 characters
  Maximum: 300 characters
  Error message: "Justification must be 30-300 characters"
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** Yes
- **Example:** `Data minimization: System only processes resume text (skills, experience, education). Does NOT collect protected characteristics (age, gender, race) or social media profiles. Retention limited to 12 months post-hiring decision.`

**Column N: Legal Basis**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Consent (Art. 6(1)(a)),Contract (Art. 6(1)(b)),Legal Obligation (Art. 6(1)(c)),Vital Interests (Art. 6(1)(d)),Public Task (Art. 6(1)(e)),Legitimate Interests (Art. 6(1)(f))"
  Error message: "Select GDPR Article 6 legal basis"
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** Yes
- **Example:** `Legitimate Interests (Art. 6(1)(f))`

**Column O: Special Category Legal Basis**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="N/A,Explicit Consent (Art. 9(2)(a)),Employment Law (Art. 9(2)(b)),Vital Interests (Art. 9(2)(c)),Medical Purposes (Art. 9(2)(h)),Public Health (Art. 9(2)(i)),Archiving/Research (Art. 9(2)(j))"
  Error message: "Select GDPR Article 9 legal basis (or N/A)"
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** Yes
- **Example:** `N/A`

**Column P: Data Subject Rights Respected?**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Yes,No,Partial"
  Error message: "Select from list"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Example:** `Partial`

**Column Q: Rights Restrictions Documented**

- **Data Type:** Text
- **Validation:**

  ```
  Type: Text length
  Maximum: 300 characters
  Error message: "Restrictions must be max 300 characters"
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** If P = "No" or "Partial"
- **Example:** `Right to erasure restricted per Art. 17(3)(b) - legal obligation to retain hiring records for 12 months (employment law compliance). Right to object not applicable per Art. 21(1) - processing necessary for contract consideration.`

**Column R: Third-Party Recipients**

- **Data Type:** Text
- **Validation:**

  ```
  Type: Text length
  Maximum: 200 characters
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** No
- **Example:** `AWS (cloud infrastructure processor), HireVue (AI screening processor via DPA signed 2024-01-10)`

**Column S: Cross-Border Transfers**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Yes,No"
  Error message: "Select Yes or No"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes
- **Example:** `Yes`

**Column T: Transfer Safeguards**

- **Data Type:** Text
- **Validation:**

  ```
  Type: Text length
  Maximum: 200 characters
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** If S = "Yes"
- **Example:** `SCCs (Standard Contractual Clauses) executed with AWS on 2024-01-15. Data residency: EU-West-1 (Ireland) with replication to EU-Central-1 (Frankfurt).`

#### Conditional Formatting (Entire Row)

**Rule 1: Highlight Critical/High risks**

- **Applies to:** $A$2:$T$1000
- **Condition:** `=OR($I2="Critical", $I2="High")`
- **Format:** Fill: RGB(255, 230, 230) - Very Light Red (row background), Left border: 4pt RGB(192, 0, 0) - Dark Red

**Rule 2: Highlight necessity/proportionality failures**

- **Applies to:** $A$2:$T$1000
- **Condition:** `=OR($J2="No", $L2="No")`
- **Format:** Fill: RGB(255, 242, 204) - Very Light Orange (row background), Right border: 4pt RGB(255, 0, 0) - Red
- **Note:** These require processing redesign - CRITICAL flag

#### Worksheet Protection

**Protected Elements:**

- Column headers (Row 1)
- Calculated columns (B, H, I)
- Sheet structure

**Unprotected Elements:**

- A2:G1000, J2:T1000 (user input areas for risk assessment details)

---

**Target Audience:** Python Developers, System Administrators, Automation Engineers

**Purpose:** Complete technical specifications for mitigation tracking, stakeholder consultation, gap analysis, compliance dashboard, and Python workbook generation script.

---

### SHEET 5: Mitigation Measures

**Sheet Name:** `Mitigation_Measures`  
**Tab Color:** RGB(68, 114, 196) - Blue  
**Protection:** Unlocked cells: A2:K1000 (user input)  
**Freeze Panes:** Row 1 (header row frozen)  
**Print Settings:** Fit to 1 page wide, landscape orientation

#### Row 1: Column Headers

| Column | Header Text | Width | Format |
|--------|------------|-------|--------|
| A | Risk ID | 20 | Bold, Fill: RGB(68, 114, 196), Font: White, Center-aligned |
| B | Risk Description (Reference) | 50 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| C | Mitigation Control ID | 20 | Bold, Fill: RGB(68, 114, 196), Font: White, Center-aligned |
| D | Control Type | 20 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| E | Mitigation Description | 50 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| F | Implementation Status | 15 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| G | Owner | 20 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| H | Target Date | 15 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| I | Actual Date | 15 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| J | Effectiveness Rating | 15 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |
| K | Evidence Location | 40 | Bold, Fill: RGB(68, 114, 196), Font: White, Wrap text |

#### Column Specifications

**Column A: Risk ID**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: =Risk_Assessment!$B$2:$B$1000
  Error message: "Select Risk ID from Risk Assessment sheet"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes

**Column B: Risk Description (Reference)**

- **Data Type:** Calculated (Text)
- **Formula:**

  ```excel
  =IF(ISBLANK(A2),"",IFERROR(VLOOKUP(A2,Risk_Assessment!$B$2:$D$1000,2,FALSE),"Not Found"))
  ```

- **Format:** Text, left-aligned, wrap text, read-only
- **Auto-fill:** B2:B1000

**Column C: Mitigation Control ID**

- **Data Type:** Calculated (Text)
- **Formula:**

  ```excel
  =IF(ISBLANK(A2),"",A2&"-M"&TEXT(COUNTIF($A$2:A2,A2),"00"))
  ```
  Generates: DPIA-2024-001-R01-M01, DPIA-2024-001-R01-M02, etc.

- **Format:** Text, center-aligned
- **Auto-fill:** C2:C1000

**Column D: Control Type**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Technical,Organizational,Legal,Physical,Administrative"
  Error message: "Select control type"
  ```

- **Format:** Text, left-aligned
- **Required:** Yes

**Column E: Mitigation Description**

- **Data Type:** Text
- **Validation:**

  ```
  Type: Text length
  Minimum: 50 characters
  Maximum: 500 characters
  Error message: "Description must be 50-500 characters (be specific)"
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** Yes

**Column F: Implementation Status**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Planned,In Progress,Implemented,Validated,Rejected"
  Error message: "Select implementation status"
  ```

- **Format:** Text, center-aligned
- **Conditional Formatting:**
  - `=F2="Implemented"` → Fill: RGB(146, 208, 80), Font: RGB(0, 97, 0)
  - `=F2="Validated"` → Fill: RGB(146, 208, 80), Font: RGB(0, 97, 0), Bold
  - `=F2="In Progress"` → Fill: RGB(255, 217, 102), Font: RGB(156, 87, 0)
  - `=F2="Planned"` → Fill: RGB(217, 217, 217), Font: Black
  - `=F2="Rejected"` → Fill: RGB(255, 102, 102), Font: RGB(156, 0, 6)
- **Required:** Yes

**Column G: Owner**

- **Data Type:** Text
- **Format:** Text, left-aligned
- **Validation:**

  ```
  Type: Text length
  Maximum: 100 characters
  ```

- **Required:** Yes

**Column H: Target Date**

- **Data Type:** Date
- **Format:** Date, YYYY-MM-DD
- **Validation:**

  ```
  Type: Date
  Date: >= TODAY()
  Error message: "Target date must be in future"
  ```

- **Required:** Yes

**Column I: Actual Date**

- **Data Type:** Date
- **Format:** Date, YYYY-MM-DD
- **Validation:**

  ```
  Type: Date
  Date: >= H2
  Error message: "Actual date should be >= Target Date"
  ```

- **Required:** Only if Status = "Implemented" or "Validated"

**Column J: Effectiveness Rating**

- **Data Type:** Dropdown
- **Validation:**

  ```
  Type: List
  Source: ="Not Assessed,Ineffective,Partially Effective,Effective,Highly Effective"
  Error message: "Select effectiveness rating"
  ```

- **Format:** Text, center-aligned
- **Conditional Formatting:**
  - `=J2="Highly Effective"` → Fill: RGB(146, 208, 80), Font: RGB(0, 97, 0)
  - `=J2="Effective"` → Fill: RGB(146, 208, 80), Font: RGB(0, 97, 0)
  - `=J2="Partially Effective"` → Fill: RGB(255, 217, 102), Font: RGB(156, 87, 0)
  - `=J2="Ineffective"` → Fill: RGB(255, 102, 102), Font: RGB(156, 0, 6)
- **Required:** Only if Status = "Validated"

**Column K: Evidence Location**

- **Data Type:** Text
- **Format:** Text, left-aligned, wrap text
- **Validation:**

  ```
  Type: Text length
  Maximum: 500 characters
  ```

- **Required:** Only if Status = "Implemented" or "Validated"

#### Conditional Formatting (Row-Level)

**Rule: Highlight overdue mitigation**

- **Applies to:** $A$2:$K$1000
- **Condition:** `=AND(NOT(ISBLANK($H2)), $H2<TODAY(), OR($F2="Planned", $F2="In Progress"))`
- **Format:** Fill: RGB(255, 230, 230), Left border: 4pt RGB(192, 0, 0)

---

### SHEET 6: Stakeholder Consultation

**Sheet Name:** `Stakeholder_Consultation`  
**Tab Color:** RGB(112, 173, 71) - Green  
**Protection:** Unlocked cells: A2:I1000  
**Freeze Panes:** Row 1  
**Print Settings:** Portrait, fit to 1 page wide

#### Row 1: Column Headers

| Column | Header Text | Width | Format |
|--------|------------|-------|--------|
| A | DPIA ID | 18 | Bold, Fill: RGB(112, 173, 71), Font: White, Center-aligned |
| B | Stakeholder Type | 20 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| C | Stakeholder Name/Title | 25 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| D | Consultation Date | 15 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| E | Consultation Method | 20 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| F | Key Concerns Raised | 50 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| G | Recommendations | 50 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| H | Action Taken | 50 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |
| I | Evidence Location | 40 | Bold, Fill: RGB(112, 173, 71), Font: White, Wrap text |

#### Column Specifications

**Column A: DPIA ID**

- **Validation:**

  ```
  Type: List
  Source: =DPIA_Register!$A$2:$A$1000
  ```

- **Format:** Text, center-aligned
- **Required:** Yes

**Column B: Stakeholder Type**

- **Validation:**

  ```
  Type: List
  Source: ="DPO,Data Subjects,Supervisory Authority,Legal Counsel,IT/Security Team,Business Unit,External Consultant,Other"
  ```

- **Format:** Text, left-aligned
- **Required:** Yes

**Column C: Stakeholder Name/Title**

- **Data Type:** Text
- **Format:** Text, left-aligned
- **Validation:**

  ```
  Type: Text length
  Maximum: 100 characters
  ```

- **Required:** Yes

**Column D: Consultation Date**

- **Data Type:** Date
- **Format:** Date, YYYY-MM-DD
- **Validation:**

  ```
  Type: Date
  Date: between 2020-01-01 and TODAY()
  ```

- **Required:** Yes

**Column E: Consultation Method**

- **Validation:**

  ```
  Type: List
  Source: ="Meeting,Email,Survey,Workshop,Interview,Public Consultation,Other"
  ```

- **Format:** Text, left-aligned
- **Required:** Yes

**Column F: Key Concerns Raised**

- **Data Type:** Text
- **Format:** Text, left-aligned, wrap text
- **Validation:**

  ```
  Type: Text length
  Minimum: 20 characters
  Maximum: 500 characters
  ```

- **Required:** Yes

**Column G: Recommendations**

- **Data Type:** Text
- **Format:** Text, left-aligned, wrap text
- **Validation:**

  ```
  Type: Text length
  Maximum: 500 characters
  ```

- **Required:** No

**Column H: Action Taken**

- **Data Type:** Text
- **Format:** Text, left-aligned, wrap text
- **Validation:**

  ```
  Type: Text length
  Maximum: 500 characters
  ```

- **Required:** Yes

**Column I: Evidence Location**

- **Data Type:** Text
- **Format:** Text, left-aligned, wrap text
- **Validation:**

  ```
  Type: Text length
  Maximum: 500 characters
  ```

- **Required:** Yes

---

### SHEET 7: Gap Analysis

**Sheet Name:** `Gap_Analysis`  
**Tab Color:** RGB(255, 192, 0) - Orange  
**Protection:** Unlocked cells: A2:D1000, I2:K1000; Columns E-H locked (calculated)  
**Freeze Panes:** Row 1  
**Print Settings:** Landscape, fit to 1 page wide

#### Row 1: Column Headers

| Column | Header Text | Width | Format |
|--------|------------|-------|--------|
| A | Risk ID | 20 | Bold, Fill: RGB(237, 125, 49), Font: White, Center-aligned |
| B | Inherent Risk Score (Reference) | 15 | Bold, Fill: RGB(237, 125, 49), Font: White, Wrap text |
| C | Mitigation Implemented? | 15 | Bold, Fill: RGB(237, 125, 49), Font: White, Wrap text |
| D | Mitigation Effectiveness | 15 | Bold, Fill: RGB(237, 125, 49), Font: White, Wrap text |
| E | Risk Reduction Factor | 12 | Bold, Fill: RGB(237, 125, 49), Font: White, Wrap text |
| F | Residual Likelihood | 12 | Bold, Fill: RGB(237, 125, 49), Font: White, Wrap text |
| G | Residual Risk Score | 12 | Bold, Fill: RGB(237, 125, 49), Font: White, Wrap text |
| H | Residual Risk Level | 15 | Bold, Fill: RGB(237, 125, 49), Font: White, Wrap text |
| I | Gap Identified? | 12 | Bold, Fill: RGB(237, 125, 49), Font: White, Wrap text |
| J | Gap Description | 50 | Bold, Fill: RGB(237, 125, 49), Font: White, Wrap text |
| K | Remediation Plan | 50 | Bold, Fill: RGB(237, 125, 49), Font: White, Wrap text |

#### Column Specifications

**Column A: Risk ID**

- **Validation:**

  ```
  Type: List
  Source: =Risk_Assessment!$B$2:$B$1000
  ```

- **Format:** Text, center-aligned
- **Required:** Yes

**Column B: Inherent Risk Score (Reference)**

- **Formula:**

  ```excel
  =IF(ISBLANK(A2),"",IFERROR(VLOOKUP(A2,Risk_Assessment!$B$2:$H$1000,7,FALSE),"Not Found"))
  ```

- **Format:** Number, 0 decimal places, center-aligned
- **Auto-fill:** B2:B1000
- **Protected:** Yes

**Column C: Mitigation Implemented?**

- **Validation:**

  ```
  Type: List
  Source: ="Yes,No,Partial"
  ```

- **Format:** Text, center-aligned
- **Required:** Yes

**Column D: Mitigation Effectiveness**

- **Validation:**

  ```
  Type: List
  Source: ="N/A,Low (10% reduction),Medium (30% reduction),High (50% reduction),Very High (70% reduction)"
  ```

- **Format:** Text, left-aligned, wrap text
- **Required:** Yes

**Column E: Risk Reduction Factor**

- **Formula:**

  ```excel
  =IF(C2="No",1,IF(D2="N/A",1,IF(D2="Low (10% reduction)",0.9,IF(D2="Medium (30% reduction)",0.7,IF(D2="High (50% reduction)",0.5,IF(D2="Very High (70% reduction)",0.3,1))))))
  ```

- **Format:** Number, 2 decimal places, center-aligned
- **Auto-fill:** E2:E1000
- **Protected:** Yes

**Column F: Residual Likelihood**

- **Formula:**

  ```excel
  =IF(ISBLANK(B2),"",ROUNDUP(SQRT(B2)*E2,0))
  ```
  Approximates reduced likelihood assuming risk score = Likelihood × Impact

- **Format:** Number, 0 decimal places, center-aligned
- **Auto-fill:** F2:F1000
- **Protected:** Yes

**Column G: Residual Risk Score**

- **Formula:**

  ```excel
  =IF(ISBLANK(B2),"",ROUNDUP(B2*E2,0))
  ```

- **Format:** Number, 0 decimal places, center-aligned, bold
- **Auto-fill:** G2:G1000
- **Protected:** Yes
- **Conditional Formatting:** Same as Risk_Assessment!H (color by risk score)

**Column H: Residual Risk Level**

- **Formula:**

  ```excel
  =IF(ISBLANK(G2),"",IF(G2>=20,"Critical",IF(G2>=15,"High",IF(G2>=8,"Medium","Low"))))
  ```

- **Format:** Text, center-aligned, bold
- **Auto-fill:** H2:H1000
- **Protected:** Yes
- **Conditional Formatting:** Same as Risk_Assessment!I

**Column I: Gap Identified?**

- **Validation:**

  ```
  Type: List
  Source: ="Yes,No"
  ```

- **Format:** Text, center-aligned
- **Conditional Formatting:**
  - `=I2="Yes"` → Fill: RGB(255, 102, 102), Font: RGB(156, 0, 6)
- **Required:** Yes

**Column J: Gap Description**

- **Data Type:** Text
- **Format:** Text, left-aligned, wrap text
- **Validation:**

  ```
  Type: Text length
  Maximum: 500 characters
  ```

- **Required:** If I = "Yes"

**Column K: Remediation Plan**

- **Data Type:** Text
- **Format:** Text, left-aligned, wrap text
- **Validation:**

  ```
  Type: Text length
  Maximum: 500 characters
  ```

- **Required:** If I = "Yes"

#### Conditional Formatting (Row-Level)

**Rule: Highlight high/critical residual risk**

- **Applies to:** $A$2:$K$1000
- **Condition:** `=OR($H2="High", $H2="Critical")`
- **Format:** Fill: RGB(255, 230, 230), Left border: 4pt RGB(192, 0, 0)

---

### SHEET 8: Compliance Dashboard

**Sheet Name:** `Dashboard`  
**Tab Color:** RGB(0, 176, 240) - Cyan  
**Protection:** Entire sheet locked (all formulas)  
**Freeze Panes:** None  
**Print Settings:** Portrait, fit to 1 page

#### Dashboard Structure

**Section 1: DPIA Summary Metrics (Rows 1-10)**

| Cell | Metric | Formula |
|------|--------|---------|
| A1 | **DPIA Assessment Summary** | Text header (merged A1:D1) |
| A3 | Total DPIAs Registered | `=COUNTA(DPIA_Register!A2:A1000)` |
| A4 | DPIAs Complete | `=COUNTIF(DPIA_Register!J2:J1000,"Complete")` |
| A5 | DPIAs In Progress | `=COUNTIF(DPIA_Register!J2:J1000,"In Progress")` |
| A6 | DPIAs Overdue | `=COUNTIF(DPIA_Register!J2:J1000,"Overdue")` |
| A7 | Completion Rate | `=IF(A3=0,0,A4/A3)` (Format: Percentage, 0 decimal places) |
| A9 | Supervisory Authority Consultations | `=COUNTIF(DPIA_Register!M2:M1000,"Yes")` |

**Section 2: Risk Distribution (Rows 12-20)**

| Cell | Metric | Formula |
|------|--------|---------|
| A12 | **Risk Distribution** | Text header (merged A12:D12) |
| A14 | Total Risks Identified | `=COUNTA(Risk_Assessment!B2:B1000)` |
| A15 | Critical Risks | `=COUNTIF(Risk_Assessment!I2:I1000,"Critical")` |
| A16 | High Risks | `=COUNTIF(Risk_Assessment!I2:I1000,"High")` |
| A17 | Medium Risks | `=COUNTIF(Risk_Assessment!I2:I1000,"Medium")` |
| A18 | Low Risks | `=COUNTIF(Risk_Assessment!I2:I1000,"Low")` |

**Section 3: Mitigation Status (Rows 22-30)**

| Cell | Metric | Formula |
|------|--------|---------|
| A22 | **Mitigation Implementation** | Text header (merged A22:D22) |
| A24 | Total Mitigation Controls | `=COUNTA(Mitigation_Measures!C2:C1000)` |
| A25 | Controls Validated | `=COUNTIF(Mitigation_Measures!F2:F1000,"Validated")` |
| A26 | Controls Implemented | `=COUNTIF(Mitigation_Measures!F2:F1000,"Implemented")` |
| A27 | Controls In Progress | `=COUNTIF(Mitigation_Measures!F2:F1000,"In Progress")` |
| A28 | Mitigation Completion Rate | `=IF(A24=0,0,(A25+A26)/A24)` (Format: Percentage) |

**Section 4: Residual Risk Summary (Rows 32-40)**

| Cell | Metric | Formula |
|------|--------|---------|
| A32 | **Residual Risk After Mitigation** | Text header (merged A32:D32) |
| A34 | Total Assessed Risks | `=COUNTA(Gap_Analysis!A2:A1000)` |
| A35 | Residual Risk - Critical | `=COUNTIF(Gap_Analysis!H2:H1000,"Critical")` |
| A36 | Residual Risk - High | `=COUNTIF(Gap_Analysis!H2:H1000,"High")` |
| A37 | Residual Risk - Medium | `=COUNTIF(Gap_Analysis!H2:H1000,"Medium")` |
| A38 | Residual Risk - Low | `=COUNTIF(Gap_Analysis!H2:H1000,"Low")` |

**Section 5: Compliance Indicators (Rows 42-52)**

| Cell | Metric | Formula |
|------|--------|---------|
| A42 | **GDPR Article 35 Compliance** | Text header (merged A42:D42) |
| A44 | Necessity Justified (Yes) | `=COUNTIF(Risk_Assessment!J2:J1000,"Yes")` |
| A45 | Proportionality Justified (Yes) | `=COUNTIF(Risk_Assessment!L2:L1000,"Yes")` |
| A46 | Data Subject Rights Fully Respected | `=COUNTIF(Risk_Assessment!P2:P1000,"Yes")` |
| A47 | Stakeholder Consultations Conducted | `=COUNTA(Stakeholder_Consultation!A2:A1000)` |
| A49 | **Overall DPIA Compliance Score** | `=IF(A3=0,0,A7*0.4+A28*0.3+(1-A36/A34)*0.3)` |
| | | (Format: Percentage, weighted score) |

**Conditional Formatting for Dashboard Metrics:**

**A7 (Completion Rate):**

- `>=0.8` → Fill: RGB(146, 208, 80) - Green
- `>=0.5, <0.8` → Fill: RGB(255, 217, 102) - Yellow
- `<0.5` → Fill: RGB(255, 102, 102) - Red

**A28 (Mitigation Completion Rate):**

- `>=0.8` → Fill: RGB(146, 208, 80) - Green
- `>=0.5, <0.8` → Fill: RGB(255, 217, 102) - Yellow
- `<0.5` → Fill: RGB(255, 102, 102) - Red

**A49 (Overall DPIA Compliance Score):**

- `>=0.8` → Fill: RGB(146, 208, 80) - Green, Font: Bold
- `>=0.6, <0.8` → Fill: RGB(255, 217, 102) - Yellow, Font: Bold
- `<0.6` → Fill: RGB(255, 102, 102) - Red, Font: Bold

**Dashboard Chart Elements:**

**Chart 1: DPIA Status (Pie Chart)**

- Location: F3:K10
- Data Range: A4:A6 (Complete, In Progress, Overdue)
- Chart Title: "DPIA Status Distribution"

**Chart 2: Risk Distribution (Bar Chart)**

- Location: F14:K21
- Data Range: A15:A18 (Critical, High, Medium, Low)
- Chart Title: "Inherent Risk Distribution"

**Chart 3: Residual vs Inherent Risk (Stacked Bar)**

- Location: F25:K35
- Data Range: A15:A18 vs A35:A38
- Chart Title: "Risk Reduction Analysis"

---

## PYTHON IMPLEMENTATION ARCHITECTURE

### Script Overview

**Script Name:** `generate_a5345_dpia_assessment.py`

**Purpose:** Generate A.5.34.5 DPIA Assessment workbook with 8 pre-configured sheets, data validation, conditional formatting, formulas, and protection.

**Dependencies:**
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.chart import PieChart, BarChart, Reference
from datetime import datetime, date
```

### Key Implementation Patterns

**Pattern 1: Color Scheme (Consistent Across Sheets)**
```python
COLORS = {
    'header_blue': 'FF4472C4',      # Sheet 1, 5
    'header_orange': 'FFC00000',     # Sheet 2
    'header_green': 'FF70AD47',      # Sheet 3, 6
    'header_red': 'FFC00000',        # Sheet 4
    'header_gold': 'FFED7D31',       # Sheet 7
    'header_cyan': 'FF00B0F0',       # Sheet 8
    'white': 'FFFFFFFF',
    'light_green': 'FF92D050',
    'light_yellow': 'FFFFD966',
    'light_orange': 'FFFFA500',
    'light_red': 'FFFF6666',
    'very_light_red': 'FFFFE6E6',
    'very_light_yellow': 'FFFFF3CD',
    'very_light_green': 'FFEBF8E9',
    'very_light_orange': 'FFFFF2CC',
}
```

**Pattern 2: Header Styling Function**
```python
def style_header_row(ws, row_num, color_hex, columns):
    """Apply consistent header styling."""
    for col in columns:
        cell = ws.cell(row=row_num, column=col)
        cell.font = Font(name='Calibri', size=11, bold=True, color='FFFFFFFF')
        cell.fill = PatternFill(start_color=color_hex, end_color=color_hex, fill_type='solid')
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        cell.border = Border(
            left=Side(style='thin', color='FF000000'),
            right=Side(style='thin', color='FF000000'),
            top=Side(style='thin', color='FF000000'),
            bottom=Side(style='thin', color='FF000000')
        )
```

**Pattern 3: Dropdown Validation**
```python
def add_dropdown(ws, cell_range, options, error_msg):
    """Add dropdown data validation."""
    dv = DataValidation(type="list", formula1=f'"{options}"', allow_blank=False)
    dv.error = error_msg
    dv.errorStyle = 'stop'
    ws.add_data_validation(dv)
    dv.add(cell_range)
```

**Pattern 4: Conditional Formatting for Risk Levels**
```python
def add_risk_level_formatting(ws, column_letter, start_row, end_row):
    """Apply conditional formatting for risk levels (Low/Medium/High/Critical)."""
    # Low: Green
    ws.conditional_formatting.add(
        f'{column_letter}{start_row}:{column_letter}{end_row}',
        CellIsRule(operator='equal', formula=['"Low"'], 
                   fill=PatternFill(start_color='FF92D050', end_color='FF92D050', fill_type='solid'),
                   font=Font(color='FF006100'))
    )
    # Medium: Yellow
    ws.conditional_formatting.add(
        f'{column_letter}{start_row}:{column_letter}{end_row}',
        CellIsRule(operator='equal', formula=['"Medium"'], 
                   fill=PatternFill(start_color='FFFFD966', end_color='FFFFD966', fill_type='solid'),
                   font=Font(color='FF9C5700'))
    )
    # High: Orange
    ws.conditional_formatting.add(
        f'{column_letter}{start_row}:{column_letter}{end_row}',
        CellIsRule(operator='equal', formula=['"High"'], 
                   fill=PatternFill(start_color='FFFFA500', end_color='FFFFA500', fill_type='solid'),
                   font=Font(color='FF9C0006'))
    )
    # Critical: Red
    ws.conditional_formatting.add(
        f'{column_letter}{start_row}:{column_letter}{end_row}',
        CellIsRule(operator='equal', formula=['"Critical"'], 
                   fill=PatternFill(start_color='FFFF6666', end_color='FFFF6666', fill_type='solid'),
                   font=Font(color='FF9C0006', bold=True))
    )
```

**Pattern 5: Sheet Protection**
```python
def protect_sheet(ws, password=None):
    """Protect sheet with standard settings."""
    ws.protection.sheet = True
    ws.protection.password = password  # Optional password
    ws.protection.enable()
    # Allow specific actions:
    ws.protection.formatCells = False
    ws.protection.formatColumns = False
    ws.protection.formatRows = False
    ws.protection.insertColumns = False
    ws.protection.insertRows = False
    ws.protection.deleteColumns = False
    ws.protection.deleteRows = False
    ws.protection.sort = True
    ws.protection.autoFilter = True
    ws.protection.selectLockedCells = True
    ws.protection.selectUnlockedCells = True
```

### Script Structure (8 Sections)

**Section 1: Create Workbook and Global Settings**
```python
def main():
    wb = Workbook()
    wb.remove(wb.active)  # Remove default sheet
    
    # Create 8 sheets
    ws1 = wb.create_sheet("Instructions", 0)
    ws2 = wb.create_sheet("Trigger_Assessment", 1)
    ws3 = wb.create_sheet("DPIA_Register", 2)
    ws4 = wb.create_sheet("Risk_Assessment", 3)
    ws5 = wb.create_sheet("Mitigation_Measures", 4)
    ws6 = wb.create_sheet("Stakeholder_Consultation", 5)
    ws7 = wb.create_sheet("Gap_Analysis", 6)
    ws8 = wb.create_sheet("Dashboard", 7)
    
    # Apply tab colors
    ws1.sheet_properties.tabColor = "FF4472C4"  # Blue
    ws2.sheet_properties.tabColor = "FFC00000"  # Orange (actually red-orange)
    ws3.sheet_properties.tabColor = "FF70AD47"  # Green
    ws4.sheet_properties.tabColor = "FFFF6666"  # Red
    ws5.sheet_properties.tabColor = "FF4472C4"  # Blue
    ws6.sheet_properties.tabColor = "FF70AD47"  # Green
    ws7.sheet_properties.tabColor = "FFC00000"  # Orange
    ws8.sheet_properties.tabColor = "FF00B0F0"  # Cyan
```

**Section 2: Sheet 1 - Instructions (Pre-Populated Content)**
```python
def create_instructions_sheet(ws):
    """Populate Sheet 1 with instructional content."""
    # Title block (merged A1:P3)
    ws.merge_cells('A1:P3')
    title_cell = ws['A1']
    title_cell.value = "DPIA Assessment - Instructions & Legend"
    title_cell.font = Font(name='Arial', size=16, bold=True, color='FFFFFFFF')
    title_cell.fill = PatternFill(start_color='FF4472C4', end_color='FF4472C4', fill_type='solid')
    title_cell.alignment = Alignment(horizontal='center', vertical='center')
    
    # Add sections (from PART 1 content)
    # Overview section (rows 4-15)
    # Navigation guide (rows 16-30)
    # Terminology (rows 31-50)
    # Risk methodology (rows 51-75)
    # Color coding (rows 76-85)
    # Evidence requirements (rows 86-100)
    # Common pitfalls (rows 101-120)
    
    # Lock entire sheet
    for row in ws.iter_rows():
        for cell in row:
            cell.protection = Protection(locked=True)
    
    protect_sheet(ws)
```

**Section 3: Sheet 2 - DPIA Trigger Assessment**
```python
def create_trigger_assessment_sheet(ws):
    """Create Sheet 2 with trigger assessment logic."""
    # Column headers
    headers = [
        ("A1", "Processing Activity ID", 20),
        ("B1", "Processing Activity Name", 30),
        ("C1", "System/Application", 25),
        ("D1", "Trigger 1: Systematic Profiling", 18),
        # ... (all 15 columns)
    ]
    
    for cell_ref, header_text, width in headers:
        cell = ws[cell_ref]
        cell.value = header_text
        col_letter = cell_ref[0]
        ws.column_dimensions[col_letter].width = width
    
    style_header_row(ws, 1, COLORS['header_orange'], range(1, 16))
    
    # Data validation (Columns D-L: Yes/No dropdowns)
    for col in ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
        add_dropdown(ws, f'{col}2:{col}1000', 'Yes,No', 'Select Yes or No')
    
    # Formula columns
    # Column M: Total Triggers
    for row in range(2, 1001):
        ws[f'M{row}'] = f'=COUNTIF(D{row}:L{row},"Yes")'
        ws[f'M{row}'].number_format = '0'
    
    # Column N: DPIA Required?
    for row in range(2, 1001):
        ws[f'N{row}'] = f'=IF(M{row}>=2,"Yes",IF(M{row}=1,"Uncertain","No"))'
    
    # Conditional formatting
    # Total Triggers (Column M)
    ws.conditional_formatting.add('M2:M1000',
        CellIsRule(operator='equal', formula=['0'], 
                   fill=PatternFill(start_color='FF92D050', end_color='FF92D050', fill_type='solid')))
    ws.conditional_formatting.add('M2:M1000',
        CellIsRule(operator='equal', formula=['1'], 
                   fill=PatternFill(start_color='FFFFD966', end_color='FFFFD966', fill_type='solid')))
    ws.conditional_formatting.add('M2:M1000',
        CellIsRule(operator='greaterThanOrEqual', formula=['2'], 
                   fill=PatternFill(start_color='FFFF6666', end_color='FFFF6666', fill_type='solid')))
    
    # DPIA Required (Column N)
    ws.conditional_formatting.add('N2:N1000',
        CellIsRule(operator='equal', formula=['"No"'], 
                   fill=PatternFill(start_color='FF92D050', end_color='FF92D050', fill_type='solid'),
                   font=Font(color='FF006100')))
    # ... (add other conditional formatting rules)
    
    # Row-level highlighting
    ws.conditional_formatting.add('A2:O1000',
        FormulaRule(formula=['$N2="Yes"'], 
                    fill=PatternFill(start_color='FFFFE6E6', end_color='FFFFE6E6', fill_type='solid')))
    
    # Freeze panes
    ws.freeze_panes = 'A2'
    
    # Protection
    for row in ws.iter_rows(min_row=2, max_row=1000):
        for cell in row:
            if cell.column in range(1, 13) or cell.column == 15:  # A-L, O (user input)
                cell.protection = Protection(locked=False)
            else:  # M, N (formulas)
                cell.protection = Protection(locked=True)
    
    protect_sheet(ws)
```

**Section 4: Sheet 3 - DPIA Register**
```python
def create_dpia_register_sheet(ws):
    """Create Sheet 3 with DPIA tracking."""
    # Headers (18 columns A-R)
    # ... (header setup similar to Sheet 2)
    
    # Formulas for auto-populated columns
    # Column C: Processing Activity Name (VLOOKUP)
    for row in range(2, 1001):
        ws[f'C{row}'] = f'=IF(ISBLANK(B{row}),"",IFERROR(VLOOKUP(B{row},Trigger_Assessment!$A$2:$B$1000,2,FALSE),"Not Found"))'
    
    # Column D: System/Application (VLOOKUP)
    for row in range(2, 1001):
        ws[f'D{row}'] = f'=IF(ISBLANK(B{row}),"",IFERROR(VLOOKUP(B{row},Trigger_Assessment!$A$2:$C$1000,3,FALSE),"Not Found"))'
    
    # Column P: Next Review Date (DATE formula)
    for row in range(2, 1001):
        ws[f'P{row}'] = f'=IF(ISBLANK(I{row}),"",DATE(YEAR(I{row})+1,MONTH(I{row}),DAY(I{row})))'
        ws[f'P{row}'].number_format = 'YYYY-MM-DD'
    
    # Status dropdown (Column J)
    add_dropdown(ws, 'J2:J1000', 'Planned,In Progress,Under Review,Complete,Overdue', 'Select status')
    
    # Conditional formatting for status
    # ... (apply color coding per spec)
    
    # Risk level dropdowns and formatting (Columns K, L)
    add_dropdown(ws, 'K2:K1000', 'Low,Medium,High,Critical', 'Select risk level')
    add_dropdown(ws, 'L2:L1000', 'Low,Medium,High,Critical', 'Select risk level')
    add_risk_level_formatting(ws, 'K', 2, 1000)
    add_risk_level_formatting(ws, 'L', 2, 1000)
    
    # Freeze and protect
    ws.freeze_panes = 'A2'
    protect_sheet(ws)
```

**Section 5: Sheet 4 - Risk Assessment**
```python
def create_risk_assessment_sheet(ws):
    """Create Sheet 4 with risk scoring matrix."""
    # Headers (20 columns A-T)
    # ... (header setup)
    
    # Risk ID auto-generation (Column B)
    for row in range(2, 1001):
        ws[f'B{row}'] = f'=IF(ISBLANK(A{row}),"",A{row}&"-R"&TEXT(COUNTIF($A$2:A{row},A{row}),"00"))'
    
    # Likelihood/Impact dropdowns (Columns F, G)
    add_dropdown(ws, 'F2:F1000', '1 - Rare,2 - Unlikely,3 - Possible,4 - Likely,5 - Almost Certain', 
                 'Select likelihood')
    add_dropdown(ws, 'G2:G1000', '1 - Negligible,2 - Minor,3 - Moderate,4 - Major,5 - Severe', 
                 'Select impact')
    
    # Inherent Risk Score (Column H)
    for row in range(2, 1001):
        ws[f'H{row}'] = f'=IF(OR(ISBLANK(F{row}),ISBLANK(G{row})),"",VALUE(LEFT(F{row},1))*VALUE(LEFT(G{row},1)))'
        ws[f'H{row}'].number_format = '0'
    
    # Inherent Risk Level (Column I)
    for row in range(2, 1001):
        ws[f'I{row}'] = f'=IF(ISBLANK(H{row}),"",IF(H{row}>=20,"Critical",IF(H{row}>=15,"High",IF(H{row}>=8,"Medium","Low"))))'
    
    # Apply risk level conditional formatting
    add_risk_level_formatting(ws, 'H', 2, 1000)
    add_risk_level_formatting(ws, 'I', 2, 1000)
    
    # Legal basis dropdowns (Columns N, O)
    add_dropdown(ws, 'N2:N1000', 
                 'Consent (Art. 6(1)(a)),Contract (Art. 6(1)(b)),Legal Obligation (Art. 6(1)(c)),Vital Interests (Art. 6(1)(d)),Public Task (Art. 6(1)(e)),Legitimate Interests (Art. 6(1)(f))',
                 'Select GDPR Article 6 legal basis')
    
    # Row-level highlighting for Critical/High risks
    ws.conditional_formatting.add('A2:T1000',
        FormulaRule(formula=['OR($I2="Critical",$I2="High")'], 
                    fill=PatternFill(start_color='FFFFE6E6', end_color='FFFFE6E6', fill_type='solid'),
                    border=Border(left=Side(style='thick', color='FFC00000'))))
    
    ws.freeze_panes = 'A2'
    protect_sheet(ws)
```

**Section 6: Sheet 5 - Mitigation Measures**
```python
def create_mitigation_measures_sheet(ws):
    """Create Sheet 5 with mitigation tracking."""
    # Headers (11 columns A-K)
    # ... (header setup)
    
    # Column B: Risk Description reference (VLOOKUP)
    for row in range(2, 1001):
        ws[f'B{row}'] = f'=IF(ISBLANK(A{row}),"",IFERROR(VLOOKUP(A{row},Risk_Assessment!$B$2:$D$1000,2,FALSE),"Not Found"))'
    
    # Column C: Mitigation Control ID
    for row in range(2, 1001):
        ws[f'C{row}'] = f'=IF(ISBLANK(A{row}),"",A{row}&"-M"&TEXT(COUNTIF($A$2:A{row},A{row}),"00"))'
    
    # Implementation Status dropdown (Column F)
    add_dropdown(ws, 'F2:F1000', 'Planned,In Progress,Implemented,Validated,Rejected', 
                 'Select implementation status')
    
    # Status conditional formatting
    ws.conditional_formatting.add('F2:F1000',
        CellIsRule(operator='equal', formula=['"Validated"'], 
                   fill=PatternFill(start_color='FF92D050', end_color='FF92D050', fill_type='solid'),
                   font=Font(color='FF006100', bold=True)))
    # ... (other status colors)
    
    # Overdue mitigation highlighting
    ws.conditional_formatting.add('A2:K1000',
        FormulaRule(formula=['AND(NOT(ISBLANK($H2)),$H2<TODAY(),OR($F2="Planned",$F2="In Progress"))'], 
                    fill=PatternFill(start_color='FFFFE6E6', end_color='FFFFE6E6', fill_type='solid'),
                    border=Border(left=Side(style='thick', color='FFC00000'))))
    
    ws.freeze_panes = 'A2'
    protect_sheet(ws)
```

**Section 7: Sheet 6 - Stakeholder Consultation**
```python
def create_stakeholder_consultation_sheet(ws):
    """Create Sheet 6 for stakeholder consultation records."""
    # Headers (9 columns A-I)
    # ... (straightforward setup, all text/date fields)
    
    # Stakeholder Type dropdown (Column B)
    add_dropdown(ws, 'B2:B1000', 
                 'DPO,Data Subjects,Supervisory Authority,Legal Counsel,IT/Security Team,Business Unit,External Consultant,Other',
                 'Select stakeholder type')
    
    # Consultation Method dropdown (Column E)
    add_dropdown(ws, 'E2:E1000', 
                 'Meeting,Email,Survey,Workshop,Interview,Public Consultation,Other',
                 'Select consultation method')
    
    ws.freeze_panes = 'A2'
    protect_sheet(ws)
```

**Section 8: Sheet 7 - Gap Analysis**
```python
def create_gap_analysis_sheet(ws):
    """Create Sheet 7 with residual risk calculation."""
    # Headers (11 columns A-K)
    # ... (header setup)
    
    # Column B: Inherent Risk Score reference
    for row in range(2, 1001):
        ws[f'B{row}'] = f'=IF(ISBLANK(A{row}),"",IFERROR(VLOOKUP(A{row},Risk_Assessment!$B$2:$H$1000,7,FALSE),"Not Found"))'
    
    # Mitigation Effectiveness dropdown (Column D)
    add_dropdown(ws, 'D2:D1000', 
                 'N/A,Low (10% reduction),Medium (30% reduction),High (50% reduction),Very High (70% reduction)',
                 'Select effectiveness')
    
    # Column E: Risk Reduction Factor
    for row in range(2, 1001):
        formula = (
            f'=IF(C{row}="No",1,'
            f'IF(D{row}="N/A",1,'
            f'IF(D{row}="Low (10% reduction)",0.9,'
            f'IF(D{row}="Medium (30% reduction)",0.7,'
            f'IF(D{row}="High (50% reduction)",0.5,'
            f'IF(D{row}="Very High (70% reduction)",0.3,1))))))'
        )
        ws[f'E{row}'] = formula
        ws[f'E{row}'].number_format = '0.00'
    
    # Column G: Residual Risk Score
    for row in range(2, 1001):
        ws[f'G{row}'] = f'=IF(ISBLANK(B{row}),"",ROUNDUP(B{row}*E{row},0))'
        ws[f'G{row}'].number_format = '0'
    
    # Column H: Residual Risk Level
    for row in range(2, 1001):
        ws[f'H{row}'] = f'=IF(ISBLANK(G{row}),"",IF(G{row}>=20,"Critical",IF(G{row}>=15,"High",IF(G{row}>=8,"Medium","Low"))))'
    
    # Apply risk level formatting
    add_risk_level_formatting(ws, 'G', 2, 1000)
    add_risk_level_formatting(ws, 'H', 2, 1000)
    
    # Highlight High/Critical residual risks
    ws.conditional_formatting.add('A2:K1000',
        FormulaRule(formula=['OR($H2="High",$H2="Critical")'], 
                    fill=PatternFill(start_color='FFFFE6E6', end_color='FFFFE6E6', fill_type='solid'),
                    border=Border(left=Side(style='thick', color='FFC00000'))))
    
    ws.freeze_panes = 'A2'
    protect_sheet(ws)
```

**Section 9: Sheet 8 - Dashboard (All Formulas)**
```python
def create_dashboard_sheet(ws):
    """Create Sheet 8 with summary dashboard."""
    # Section 1: DPIA Summary Metrics
    ws.merge_cells('A1:D1')
    ws['A1'].value = "DPIA Assessment Summary"
    ws['A1'].font = Font(size=14, bold=True)
    
    metrics = [
        ("A3", "Total DPIAs Registered", "=COUNTA(DPIA_Register!A2:A1000)"),
        ("A4", "DPIAs Complete", '=COUNTIF(DPIA_Register!J2:J1000,"Complete")'),
        ("A5", "DPIAs In Progress", '=COUNTIF(DPIA_Register!J2:J1000,"In Progress")'),
        ("A6", "DPIAs Overdue", '=COUNTIF(DPIA_Register!J2:J1000,"Overdue")'),
        ("A7", "Completion Rate", "=IF(A3=0,0,A4/A3)"),
        ("A9", "Supervisory Authority Consultations", '=COUNTIF(DPIA_Register!M2:M1000,"Yes")'),
    ]
    
    for cell_ref, label, formula in metrics:
        ws[cell_ref].value = label
        ws[cell_ref].font = Font(bold=True)
        value_cell_ref = cell_ref.replace('A', 'C')
        ws[value_cell_ref] = formula
        if "Rate" in label:
            ws[value_cell_ref].number_format = '0%'
    
    # ... (continue with other sections: Risk Distribution, Mitigation Status, Residual Risk, Compliance)
    
    # Apply conditional formatting to key metrics
    ws.conditional_formatting.add('C7',
        CellIsRule(operator='greaterThanOrEqual', formula=['0.8'], 
                   fill=PatternFill(start_color='FF92D050', end_color='FF92D050', fill_type='solid')))
    ws.conditional_formatting.add('C7',
        CellIsRule(operator='between', formula=['0.5', '0.8'], 
                   fill=PatternFill(start_color='FFFFD966', end_color='FFFFD966', fill_type='solid')))
    ws.conditional_formatting.add('C7',
        CellIsRule(operator='lessThan', formula=['0.5'], 
                   fill=PatternFill(start_color='FFFF6666', end_color='FFFF6666', fill_type='solid')))
    
    # Add charts
    # Chart 1: DPIA Status Pie Chart
    pie = PieChart()
    pie.title = "DPIA Status Distribution"
    labels = Reference(ws, min_col=1, min_row=4, max_row=6)
    data = Reference(ws, min_col=3, min_row=3, max_row=6)
    pie.add_data(data, titles_from_data=True)
    pie.set_categories(labels)
    ws.add_chart(pie, "F3")
    
    # ... (add other charts)
    
    # Lock entire dashboard
    for row in ws.iter_rows():
        for cell in row:
            cell.protection = Protection(locked=True)
    
    protect_sheet(ws)
```

**Section 10: Save Workbook**
```python
    # Final workbook settings
    wb.properties.title = "A.5.34.5 DPIA Assessment"
    wb.properties.subject = "Data Protection Impact Assessment"
    wb.properties.creator = "ISMS Automation Script"
    wb.properties.created = datetime.now()
    
    # Save
    filename = f"ISMS-A.5.34.5-DPIA-Assessment-{datetime.now().strftime('%Y%m%d')}.xlsx"
    wb.save(filename)
    print(f"Workbook created: {filename}")

if __name__ == "__main__":
    main()
```

---

## INTEGRATION WITH A.5.34.7 BIG DASHBOARD

**Data Extraction Pattern (openpyxl):**

```python
# In A.5.34.7 Dashboard Generator Script
from openpyxl import load_workbook

def extract_a5345_metrics(workbook_path):
    """Extract DPIA metrics for BIG DASHBOARD consolidation."""
    wb = load_workbook(workbook_path, data_only=True)
    
    # Extract from Dashboard sheet (pre-calculated metrics)
    ws_dashboard = wb['Dashboard']
    
    metrics = {
        'total_dpias': ws_dashboard['C3'].value,
        'dpias_complete': ws_dashboard['C4'].value,
        'dpias_overdue': ws_dashboard['C6'].value,
        'completion_rate': ws_dashboard['C7'].value,
        'total_risks': ws_dashboard['C14'].value,
        'critical_risks': ws_dashboard['C15'].value,
        'high_risks': ws_dashboard['C16'].value,
        'mitigation_completion_rate': ws_dashboard['C28'].value,
        'residual_high_risks': ws_dashboard['C36'].value,
        'compliance_score': ws_dashboard['C49'].value,
    }
    
    wb.close()
    return metrics

# Usage in BIG DASHBOARD
a5345_metrics = extract_a5345_metrics('ISMS-A.5.34.5-DPIA-Assessment-20240330.xlsx')
```

---

**END OF SPECIFICATION**

---

*"Whenever we proceed from the known into the unknown we may hope to understand, but we may have to learn at the same time a new meaning of the word understanding."*
— Werner Heisenberg

<!-- QA_VERIFIED: 2026-02-06 -->
