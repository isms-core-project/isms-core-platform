**ISMS-IMP-A.8.11.3-TG - Environment Coverage Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.11: Data Masking


---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.11.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Environment Coverage & Deployment Verification |
| **Related Policy** | ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) |
| **Purpose** | Guide users through assessing WHERE data masking is deployed across all organizational environments to ensure comprehensive coverage |
| **Target Audience** | IT Operations Managers, Database Administrators, Cloud Architects, DevOps Engineers, Security Engineers, Compliance Officers, Auditors |
| **Assessment Type** | Environment Coverage & Gap Analysis |
| **Review Cycle** | Quarterly (Environment Inventory Updates) / After Major System Deployments |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial workbook layout specification only | ISMS Implementation Team |

---

# Technical Specification

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.11.3 - Part II |
| **Version** | 1.0 |
| **Document Type** | Excel Workbook Layout Specification |
| **Related Policy** | ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) |
| **Purpose** | Define complete technical specification for Environment Coverage Assessment Excel workbook generation |
| **Target Audience** | Python Developers, ISMS Implementation Teams, Automation Engineers |
| **Assessment Type** | Technical Specification for Automated Workbook Generation |
| **Date** | [Date] |

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial workbook layout specification | ISMS Implementation Team |

---

# PART II: TECHNICAL SPECIFICATION

**Purpose:** This document provides the complete technical specification for generating the ISMS-IMP-A.8.11.3 Environment Coverage Assessment Excel workbook using Python (openpyxl library).

**Target Audience:** Python developers implementing the `generate_assessment_3_environment_coverage.py` script.

**What This Document Provides:**

- Complete workbook structure (12 sheets with exact specifications)
- Column definitions with data types and validation rules
- Styling and formatting standards (colors, fonts, borders)
- Formula definitions for automated calculations
- Data validation dropdown lists
- Cell protection strategies
- Quality assurance requirements

**Implementation Note:** This specification is designed for openpyxl-based generation. All sheet names, column headers, cell references, and formulas must match exactly for dashboard consolidation scripts to work correctly.

---

# Workbook Structure Overview

## Sheet Summary (12 Sheets)

| Sheet # | Sheet Name | Purpose | Row Count | Assessment Focus |
|---------|------------|---------|-----------|------------------|
| 1 | Instructions_Legend | User guidance, color legend, policy requirements | ~120 | Documentation |
| 2 | Environment_Inventory | Complete catalog of ALL environments | 50 data rows | Environment discovery |
| 3 | Production_Environment | Production DDM assessment, role-based masking | 30 data rows | Production compliance |
| 4 | NonProduction_Environments | Dev/Test/UAT/Staging masking (100% coverage) | 30 data rows | **CRITICAL** Non-prod coverage |
| 5 | Analytics_Reporting | BI, data warehouse, ML platform masking | 30 data rows | Analytics compliance |
| 6 | Backup_Archive | Backup encryption, archive masking | 30 data rows | Backup/DR controls |
| 7 | External_Sharing | Vendor, auditor, customer data sharing | 30 data rows | Third-party risk |
| 8 | Cloud_Environments | AWS, Azure, GCP, SaaS platform masking | 30 data rows | Cloud compliance |
| 9 | Data_Flow_Mapping | ETL pipelines, data movement, masking checkpoints | 30 data rows | Data flow analysis |
| 10 | Gap_Analysis | Consolidated gaps, remediation roadmap | 40 data rows | Gap tracking |
| 11 | Evidence_Register | Supporting documentation, audit trail | 100 data rows | Evidence management |
| 12 | Summary_Dashboard | Executive KPIs, compliance metrics | ~100 rows | Executive reporting |

**Total Data Capacity:** 400+ environment assessments, 100 evidence items, 40 gaps

**File Naming Convention:**  
`ISMS-IMP-A.8.11.3_Environment_Coverage_Assessment_YYYYMMDD.xlsx`

**Example:**  
`ISMS-IMP-A.8.11.3_Environment_Coverage_Assessment_20260120.xlsx`

---

# Standard Column Structure (Used Across Sheets 2-9)

## Base Columns (A-Q, 17 columns)

These standard columns appear on assessment sheets 2-9 with consistent definitions:

| Column | Header | Width | Type | Validation Options | Notes |
|--------|--------|-------|------|-------------------|-------|
| A | Environment Name | 25 | Text | Free text | User-defined environment identifier |
| B | Environment Type | 20 | Dropdown | Production, Development, Testing, UAT, Staging, Training, Sandbox, Analytics, Cloud, Backup, Archive, External | Standardized environment classification |
| C | Classification | 18 | Dropdown | Sensitive, Confidential, Internal, Public | Data classification level |
| D | Hosting Location | 18 | Dropdown | On-Premises, AWS, Azure, GCP, Hybrid, Other Cloud | Infrastructure location |
| E | Data Sensitivity | 18 | Dropdown | PII, Financial, Health, Credentials, Proprietary, Mixed, None | Type of sensitive data |
| F | Masking Required? | 18 | Dropdown | ✅ Mandatory, ⚠️ Conditional, ❌ Not Required, N/A | Policy-driven requirement |
| G | Masking Deployed? | 18 | Dropdown | Yes, No, Partial, Planned, N/A | Current deployment status |
| H | Masking Technique | 20 | Dropdown | SDM, DDM, Tokenization, Encryption, Redaction, Substitution, Anonymization, None | Technique from IMP-A.8.11.2 |
| I | Masking Tool/Solution | 22 | Text | Free text | Tool name if deployed |
| J | Coverage % | 12 | Percentage | 0-100% | Numeric percentage |
| K | Last Verified Date | 15 | Date | Date picker (dd.mm.yyyy) | Last masking verification |
| L | Environment Owner | 20 | Text | Free text | IT Operations contact |
| M | Data Owner | 20 | Text | Free text | Business contact from IMP-A.8.11.1 |
| N | Exception Approved? | 15 | Dropdown | Yes, No, N/A | Formal exception approval |
| O | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Overall status |
| P | Notes/Comments | 30 | Text | Free text, wrapped | Additional context |
| Q | Evidence ID | 15 | Text | Free text (e.g., EV-ENV-001) | Link to Evidence_Register |

**Extended Columns (R-X):** Added per sheet for specific assessment needs (varies by sheet).

---

# Global Styling Standards

## Color Palette

| Element | RGB | Hex | Usage |
|---------|-----|-----|-------|
| Header (Main) | 0, 51, 102 | #003366 | Dark Blue - Main sheet titles |
| Subheader | 68, 114, 196 | #4472C4 | Medium Blue - Section headers |
| Column Headers | 217, 217, 217 | #D9D9D9 | Light Gray - Table headers |
| Input Cells | 255, 255, 204 | #FFFFCC | Light Yellow - User input required |
| Status - Compliant | 198, 239, 206 | #C6EFCE | Light Green - ✅ |
| Status - Partial | 255, 235, 156 | #FFEB9C | Light Yellow - ⚠️ |
| Status - Non-Compliant | 255, 199, 206 | #FFC7CE | Light Red - ❌ |
| Status - Planned | 180, 199, 231 | #B4C7E7 | Light Blue - Planned |
| Example Rows | 231, 230, 230 | #E7E6E6 | Light Gray - Example data |

## Font Standards

- **Main Headers:** Calibri 14-16pt Bold, White text on #003366 background
- **Subheaders:** Calibri 11-12pt Bold, White text on #4472C4 background
- **Column Headers:** Calibri 10pt Bold, Black text on #D9D9D9 background
- **Data Cells:** Calibri 10pt Regular, Black text
- **Example Rows:** Calibri 10pt Italic, Gray text on #E7E6E6 background

## Border Standards

- **Outer borders:** Medium weight (2pt), black
- **Inner borders:** Thin weight (1pt), black
- **Header separator:** Thick bottom border (3pt), black

## Cell Protection Strategy

**Protected (Locked):**

- All column headers
- All formula cells
- All reference tables and legends
- All instructions and example rows

**Unprotected (Unlocked):**

- All yellow input cells (#FFFFCC background)
- All user data entry rows
- Sign-off fields in Summary_Dashboard

---

# Sheet 1: Instructions_Legend

## Header Section (Rows 1-2)

**Row 1 - Main Title:**

- **Merge:** A1:Q1
- **Text:** "ISMS Control A.8.11.3 - Environment Coverage Assessment"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Alignment:** Center, Vertical Center
- **Row Height:** 40px

**Row 2 - Subtitle:**

- **Merge:** A2:Q2
- **Text:** "ISO/IEC 27001:2022 - Data Masking Policy Compliance"
- **Font:** Calibri 11pt Bold, White
- **Fill:** #4472C4 (Medium Blue)
- **Alignment:** Center, Vertical Center
- **Row Height:** 25px

## Document Information Block (Rows 4-12)

**Two-column layout:**

| Row | Column A (Label) | Column B-D (Value - Yellow Input) |
|-----|------------------|-----------------------------------|
| 4 | Document ID: | ISMS-IMP-A.8.11.3 |
| 5 | Assessment Area: | Environment Coverage & Deployment |
| 6 | Related Policy: | ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) |
| 7 | Version: | 1.0 |
| 8 | Assessment Date: | [USER INPUT - yellow cell] |
| 9 | Completed By: | [USER INPUT - yellow cell] |
| 10 | Organization: | [USER INPUT - yellow cell] |
| 11 | Review Cycle: | Quarterly |

**Column A Styling:**

- Font: Calibri 10pt Bold
- Alignment: Right-aligned

**Columns B-D Styling:**

- Font: Calibri 10pt Regular
- Fill: #FFFFCC (Yellow) for input rows 8-10
- Fill: White for static values
- Borders: Thin all sides

## How to Use This Workbook Section (Rows 14-25)

**Row 14 - Section Header:**

- **Merge:** A14:Q14
- **Text:** "HOW TO USE THIS WORKBOOK"
- **Font:** Calibri 12pt Bold
- **Fill:** #4472C4 (Medium Blue), White text
- **Row Height:** 30px

**Rows 16-25 - Instructions (Numbered List):**

1. Complete each worksheet tab in sequence (Environment Inventory → Production → Non-Production → etc.)
2. Fill ALL yellow-highlighted cells with your organization's specific information
3. Use dropdown menus where provided (do not type free-form text in dropdown cells)
4. Document ALL environments in your organization (include cloud, on-premises, hybrid)
5. For each environment, specify masking requirement (Mandatory/Conditional/Not Required) per policy S2.3
6. Verify masking deployment status (Yes/No/Partial/Planned)
7. Calculate coverage percentage (% of sensitive fields masked)
8. Link all assessments to Evidence Register with unique Evidence IDs
9. Complete Gap Analysis sheet to identify remediation needs
10. Review Summary Dashboard for executive-level compliance status

**Formatting:**

- Column A: Numbers (1-10)
- Columns B-Q: Instruction text (wrapped)
- Font: Calibri 10pt Regular
- Row Height: Auto (wrapped text)

## Color Legend Section (Rows 27-32)

**Row 27 - Section Header:**

- **Text:** "COLOR LEGEND"
- **Styling:** Same as Row 14

**Rows 29-32 - Legend Items:**

| Row | Color Sample (Col A) | Description (Cols B-Q) |
|-----|----------------------|------------------------|
| 29 | #FFFFCC (Yellow fill) | Yellow cells = User input required |
| 30 | #C6EFCE (Green fill) | Green status = Compliant (masking deployed as required) |
| 31 | #FFEB9C (Yellow fill) | Yellow status = Partial compliance (some masking gaps) |
| 32 | #FFC7CE (Red fill) | Red status = Non-compliant (masking required but not deployed) |
| 33 | #B4C7E7 (Blue fill) | Blue status = Planned (remediation in progress) |

**Column A:** Fill with corresponding color, no border
**Columns B-Q:** Description text, Calibri 10pt Regular

## Environment Classification Reference Table (Rows 35-49)

**Row 35 - Table Header:**

- **Text:** "ENVIRONMENT CLASSIFICATION REFERENCE"
- **Styling:** #4472C4 header

**Row 37 - Column Headers:**

| Column | Header | Width |
|--------|--------|-------|
| A | Environment Type | 20 |
| B | Definition | 35 |
| C | Masking Requirement | 25 |
| D | Typical Technique | 20 |

**Styling:** #D9D9D9 background, Calibri 10pt Bold, centered

**Rows 38-49 - Reference Data:**

| Environment Type | Definition | Masking Requirement | Typical Technique |
|-----------------|------------|---------------------|-------------------|
| Production | Live operational systems | ⚠️ Conditional (DDM for role-based) | DDM, Field-level encryption |
| Development | Software development | ✅ Mandatory | SDM |
| Testing/QA | Quality assurance | ✅ Mandatory | SDM |
| UAT | User acceptance testing | ✅ Mandatory | SDM |
| Staging | Pre-production validation | ✅ Mandatory (unless prod-identical) | SDM or DDM |
| Training | Employee training systems | ✅ Mandatory | SDM + Substitution |
| Sandbox | Experimental/POC work | ✅ Mandatory | SDM |
| Analytics | BI, reporting, data warehouse | ✅ Mandatory | Aggregation, Anonymization |
| Cloud | Third-party hosted (AWS/Azure/GCP) | ✅ Follows same rules as on-prem | Varies by cloud env type |
| Backup | Disaster recovery backups | ⚠️ Conditional (encryption required) | Encryption at rest |
| Archive | Long-term retention | ⚠️ Conditional (assess feasibility) | Encryption or masking |
| External | Data shared outside org | ✅ Mandatory (unless contractual) | Redaction, Aggregation |

**Cell Styling:**

- Column A: Text, left-aligned
- Columns B-D: Text, wrapped, left-aligned
- All cells: Thin borders
- Alternating row shading (optional): Light gray on even rows

## Policy Requirements Summary (Rows 51-67)

**Row 51 - Section Header:**

- **Text:** "POLICY REQUIREMENTS SUMMARY - KEY POINTS"
- **Styling:** #4472C4 header

**Rows 53-67 - Requirements (Numbered List with Icons):**

1. ✅ ALL non-production environments SHALL be masked (Policy S2.3 Section 3.2)
2. ✅ Production data SHALL NOT be copied to non-prod without masking
3. ✅ Analytics and reporting environments SHALL mask individual-level PII
4. ✅ External data sharing SHALL be masked unless contractually required
5. ✅ Cloud environments SHALL follow same masking rules as on-premises
6. ⚠️ Production environments MAY use DDM for role-based access control
7. ⚠️ Backup environments MAY contain unmasked data if encrypted and access-controlled
8. ❌ Direct production database cloning without masking is PROHIBITED
9. ❌ "We'll mask it later" approach is NOT acceptable
10. ❌ NDAs are NOT a substitute for technical masking controls
11. 📊 Coverage target: 100% of non-production environments masked
12. 📊 Exception limit: ≤5% of environments may have approved exceptions
13. 📋 All exceptions require ISO and Data Owner approval
14. 📋 Exceptions must be reviewed quarterly
15. 🔍 Masking effectiveness must be validated (see A.8.11.4 Testing)

**Formatting:**

- Icons as Unicode characters (✅ ⚠️ ❌ 📊 📋 🔍)
- Font: Calibri 10pt Regular
- Column A: Number + Icon
- Columns B-Q: Requirement text (wrapped)
- Important requirements (1-5) in Bold

---

# Sheet 2: Environment_Inventory

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:Q1
- **Text:** "ENVIRONMENT INVENTORY"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Alignment:** Center, Vertical Center
- **Row Height:** 35px

**Row 2 - Policy Reference:**

- **Merge:** A2:Q2
- **Text:** "All information processing environments must be cataloged and classified for masking applicability (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 2)"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Alignment:** Center, Vertical Center, Wrapped
- **Row Height:** Auto (wrapped)

## Assessment Question (Rows 4-5)

**Row 4 - Question:**

- **Merge:** A4:O4
- **Text:** "Does your organization maintain a complete inventory of ALL environments where data is processed, stored, or transmitted?"
- **Font:** Calibri 10pt Bold
- **Alignment:** Left, Vertical Center, Wrapped

**Cell P4 - Response:**

- **Data Validation:** Dropdown list: "Yes, No, Partial, In Progress"
- **Fill:** #FFFFCC (Yellow)
- **Font:** Calibri 10pt Regular
- **Alignment:** Center

**Cell Q4 - Label:**

- **Text:** "Response:"
- **Font:** Calibri 10pt Bold
- **Alignment:** Right

## Column Headers (Row 6)

**Standard 17 columns (A-Q) as defined in Standard Column Structure section above.**

**Row 6 Styling:**

- **Fill:** #D9D9D9 (Light Gray)
- **Font:** Calibri 10pt Bold, Black
- **Alignment:** Center, Vertical Center, Wrapped
- **Border:** Thick bottom border (3pt)
- **Row Height:** 40px (to accommodate wrapped text)

## Example Row (Row 7) - Gray Italic

**Purpose:** Provide example data to guide users

**Row 7 Data:**

- A7: "Production CRM Database"
- B7: "Production"
- C7: "Sensitive"
- D7: "On-Premises"
- E7: "PII"
- F7: "⚠️ Conditional"
- G7: "Yes"
- H7: "DDM"
- I7: "[Your masking tool name]"
- J7: "95%"
- K7: "01.01.2026"
- L7: "IT Operations Manager"
- M7: "Customer Data Owner"
- N7: "N/A"
- O7: "✅ Compliant"
- P7: "DDM applied for customer service reps"
- Q7: "EV-ENV-001"

**Row 7 Styling:**

- **Fill:** #E7E6E6 (Light Gray)
- **Font:** Calibri 10pt Italic, Gray text (#808080)
- **Border:** Thin all sides
- **Cell Protection:** Locked (user cannot edit example)

## Data Entry Rows (8-57)

**50 rows for environment inventory**

**Row 8-57 Styling:**

- **Fill:** #FFFFCC (Light Yellow) - All cells
- **Font:** Calibri 10pt Regular, Black
- **Border:** Thin all sides
- **Cell Protection:** Unlocked (user input)
- **Row Height:** 20px (standard)

**Data Validation per Column:**

**Column A (Environment Name):** Text, no validation
**Column B (Environment Type):** Dropdown list:
```
Production, Development, Testing, UAT, Staging, Training, Sandbox, Analytics, Cloud, Backup, Archive, External
```

**Column C (Classification):** Dropdown list:
```
Sensitive, Confidential, Internal, Public
```

**Column D (Hosting Location):** Dropdown list:
```
On-Premises, AWS, Azure, GCP, Hybrid, Other Cloud
```

**Column E (Data Sensitivity):** Dropdown list:
```
PII, Financial, Health, Credentials, Proprietary, Mixed, None
```

**Column F (Masking Required?):** Dropdown list:
```
✅ Mandatory, ⚠️ Conditional, ❌ Not Required, N/A
```

**Column G (Masking Deployed?):** Dropdown list:
```
Yes, No, Partial, Planned, N/A
```

**Column H (Masking Technique):** Dropdown list:
```
SDM, DDM, Tokenization, Encryption, Redaction, Substitution, Anonymization, None
```

**Column I (Masking Tool/Solution):** Text, no validation

**Column J (Coverage %):** Number validation:

- Type: Whole number
- Minimum: 0
- Maximum: 100
- Format: "0%"

**Column K (Last Verified Date):** Date validation:

- Type: Date
- Format: "dd.mm.yyyy"
- Allow blank: Yes

**Columns L-M (Owners):** Text, no validation

**Column N (Exception Approved?):** Dropdown list:
```
Yes, No, N/A
```

**Column O (Compliance Status):** Dropdown list:
```
✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A
```

**Conditional Formatting for Column O:**

- If "✅ Compliant" → Fill #C6EFCE (Green)
- If "⚠️ Partial" → Fill #FFEB9C (Yellow)
- If "❌ Non-Compliant" → Fill #FFC7CE (Red)
- If "N/A" → No fill (white)

**Columns P-Q:** Text, no validation

## Compliance Checklist (Rows 60-76)

**Row 60 - Section Header:**

- **Merge:** A60:Q60
- **Text:** "ENVIRONMENT INVENTORY CHECKLIST"
- **Font:** Calibri 12pt Bold
- **Fill:** #4472C4 (Medium Blue), White text
- **Row Height:** 30px

**Row 62 - Checklist Column Headers:**

| Column | Header | Width |
|--------|--------|-------|
| A | ☐ | 5 |
| B | Requirement | 50 |
| C | Status | 15 |
| D | Notes | 30 |

**Styling:** #D9D9D9 background, Calibri 10pt Bold

**Rows 63-76 - Checklist Items (15 items):**

| Item | Requirement | Status Dropdown | Notes |
|------|-------------|-----------------|-------|
| ☐ | All production environments documented | [Dropdown] | [Text input] |
| ☐ | All non-production environments documented (Dev/Test/UAT/Sandbox) | [Dropdown] | [Text input] |
| ☐ | All analytics/reporting environments documented | [Dropdown] | [Text input] |
| ☐ | All cloud environments documented (AWS/Azure/GCP/Other) | [Dropdown] | [Text input] |
| ☐ | All backup/archive systems documented | [Dropdown] | [Text input] |
| ☐ | External data sharing destinations documented | [Dropdown] | [Text input] |
| ☐ | Each environment classified (Sensitive/Confidential/Internal/Public) | [Dropdown] | [Text input] |
| ☐ | Data sensitivity level assigned per environment | [Dropdown] | [Text input] |
| ☐ | Masking requirement determined (Mandatory/Conditional/Not Required) | [Dropdown] | [Text input] |
| ☐ | Environment owners assigned | [Dropdown] | [Text input] |
| ☐ | Data owners assigned | [Dropdown] | [Text input] |
| ☐ | Hosting location documented (On-Prem/Cloud) | [Dropdown] | [Text input] |
| ☐ | Environment inventory reviewed in last 6 months | [Dropdown] | [Text input] |
| ☐ | New environments added to inventory within 30 days of deployment | [Dropdown] | [Text input] |
| ☐ | Decommissioned environments removed from inventory | [Dropdown] | [Text input] |

**Status Column Dropdown:**
```
✅ Complete, ⚠️ Partial, ❌ Missing, N/A
```

**Conditional Formatting for Status:**

- ✅ Complete → Fill #C6EFCE (Green)
- ⚠️ Partial → Fill #FFEB9C (Yellow)
- ❌ Missing → Fill #FFC7CE (Red)
- N/A → No fill

---

# Sheet 3: Production_Environment

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:X1 (Note: Extended to X for additional columns)
- **Text:** "PRODUCTION ENVIRONMENT ASSESSMENT"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px

**Row 2 - Policy Reference:**

- **Merge:** A2:X2
- **Text:** "Production environments may use Dynamic Data Masking (DDM) for role-based access. All access to unmasked data must be logged. (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 3.1)"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Row Height:** Auto (wrapped)

## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:U4
- **Text:** "Does your organization implement role-based masking (DDM) in production environments to restrict access to sensitive data?"
- **Font:** Calibri 10pt Bold

**Cell V4 - Response:**

- **Data Validation:** Dropdown: "Yes, No, Partial, Planned"
- **Fill:** #FFFFCC (Yellow)

**Cell W4-X4 - Label:**

- **Merge:** W4:X4
- **Text:** "Response:"
- **Alignment:** Right

## Column Headers (Row 6)

**Standard Columns A-Q** (as defined in Standard Column Structure)

**PLUS Extended Columns R-X:**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | User Role/Group | 20 | Text | Free text |
| S | Masked Fields | 25 | Text | Free text (comma-separated list) |
| T | Unmasked Access Logged? | 15 | Dropdown | Yes, No, N/A |
| U | Access Control Method | 20 | Dropdown | RBAC, ABAC, ACL, Manual, None |
| V | Exception Justification | 30 | Text | Free text, wrapped |
| W | Risk Level | 12 | Dropdown | High, Medium, Low, None |
| X | Remediation Target Date | 15 | Date | Date picker (dd.mm.yyyy) |

**Row 6 Styling:** Same as Sheet 2 (Environment_Inventory)

## Example Row (Row 7)

**Sample Production Environment with DDM:**

- A7: "Production CRM Database"
- B7: "Production"
- C7: "Sensitive"
- D7: "On-Premises"
- E7: "PII"
- F7: "⚠️ Conditional"
- G7: "Yes"
- H7: "DDM"
- I7: "Oracle Data Masking"
- J7: "95%"
- K7: "15.01.2026"
- L7: "DB Admin Team Lead"
- M7: "Customer Data Owner"
- N7: "N/A"
- O7: "✅ Compliant"
- P7: "DDM for customer service reps, helpdesk"
- Q7: "EV-PROD-001"
- R7: "Customer Service Representative"
- S7: "credit_card_number, ssn, date_of_birth"
- T7: "Yes"
- U7: "RBAC"
- V7: "N/A"
- W7: "Low"
- X7: "N/A"

**Styling:** Same gray italic example row format as Sheet 2

## Data Entry Rows (8-37)

**30 rows for production environment assessment**

**Styling:** Yellow input cells, same as Sheet 2

**Additional Validation for Extended Columns:**

**Column T (Unmasked Access Logged?):** Dropdown:
```
Yes, No, N/A
```

**Column U (Access Control Method):** Dropdown:
```
RBAC, ABAC, ACL, Manual, None
```

**Column W (Risk Level):** Dropdown:
```
High, Medium, Low, None
```

**Conditional Formatting for Column W:**

- High → Fill #FFC7CE (Red)
- Medium → Fill #FFEB9C (Yellow)
- Low → Fill #C6EFCE (Green)
- None → No fill

**Column X (Remediation Target Date):** Date format "dd.mm.yyyy"

## Compliance Checklist (Rows 40-59)

**Row 40 - Section Header:**

- **Text:** "PRODUCTION ENVIRONMENT CHECKLIST"
- **Styling:** #4472C4 header

**Rows 42-59 - Checklist Items (18 items):**

1. DDM implemented for role-based access in production
2. Customer service representatives see masked customer data
3. Production reports mask data for non-privileged users
4. Audit logs containing sensitive data are masked/encrypted
5. Application outputs (invoices, statements) use partial redaction
6. Production data exports are masked before release
7. All access to unmasked production data is logged
8. Access logs reviewed monthly for anomalies
9. Privileged user access to unmasked data requires justification
10. Masking exceptions documented with business justification
11. Exception approvals obtained from Data Owner and ISO
12. Exceptions reviewed quarterly
13. Production DDM configuration tested after schema changes
14. Role definitions documented (who sees what)
15. DDM bypass controls prevent unauthorized unmasked access
16. Production monitoring alerts on DDM failures
17. Incident response plan includes DDM failure scenarios
18. Annual DDM effectiveness review performed

**Status Dropdown:** Same as Sheet 2 (✅ Complete, ⚠️ Partial, ❌ Missing, N/A)

---

**END OF PART II - SECTION 1**

**Next Sections:**

---

# Sheet 4: NonProduction_Environments

**⚠️ CRITICAL SHEET:** This sheet assesses the MANDATORY 100% masking coverage requirement for ALL non-production environments. Policy compliance depends on this assessment.

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:X1
- **Text:** "NON-PRODUCTION ENVIRONMENTS - CRITICAL COMPLIANCE ASSESSMENT"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px

**Row 2 - Policy Reference:**

- **Merge:** A2:X2
- **Text:** "ALL non-production environments SHALL be masked (100% coverage). Production data SHALL NOT be copied to non-production without masking. (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 3.2) - MANDATORY REQUIREMENT"
- **Font:** Calibri 10pt Bold Italic, Red text (#FF0000)
- **Fill:** #FFEB9C (Light Yellow - Warning color)
- **Alignment:** Center, Vertical Center, Wrapped
- **Row Height:** Auto (wrapped)

## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:U4
- **Text:** "Are ALL non-production environments (Dev/Test/UAT/Staging/Training/Sandbox) masked at 100% coverage?"
- **Font:** Calibri 10pt Bold, Red text

**Cell V4 - Response:**

- **Data Validation:** Dropdown: "Yes (100%), No (<100%), Partial, In Progress"
- **Fill:** #FFFFCC (Yellow)
- **Font:** Calibri 10pt Regular

**Cell W4-X4 - Label:**

- **Merge:** W4:X4
- **Text:** "Response:"
- **Alignment:** Right

**Row 5 - Warning:**

- **Merge:** A5:X5
- **Text:** "⚠️ WARNING: Any environment with <100% coverage is a CRITICAL GAP requiring immediate remediation (≤30 day SLA)"
- **Font:** Calibri 9pt Bold, Red text
- **Fill:** #FFC7CE (Light Red)
- **Alignment:** Center

## Column Headers (Row 7)

**Standard Columns A-Q** (as defined in Standard Column Structure)

**PLUS Extended Columns R-X:**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Data Refresh Frequency | 18 | Dropdown | Daily, Weekly, Monthly, Ad-hoc, Never |
| S | Refresh Process | 15 | Dropdown | Automated, Manual, Hybrid |
| T | Masking in Refresh Script? | 18 | Dropdown | Yes, No, N/A |
| U | Last Data Refresh Date | 15 | Date | Date picker (dd.mm.yyyy) |
| V | Next Refresh Date | 15 | Date | Date picker (dd.mm.yyyy) |
| W | Developer Access Count | 12 | Number | Whole number |
| X | Contractor Access? | 15 | Dropdown | Yes, No, N/A |

**Row 7 Styling:**

- **Fill:** #D9D9D9 (Light Gray)
- **Font:** Calibri 10pt Bold, Black
- **Alignment:** Center, Vertical Center, Wrapped
- **Border:** Thick bottom border (3pt)
- **Row Height:** 50px (more wrapped text due to longer headers)

## Example Row (Row 8)

**Sample Non-Production Environment:**

- A8: "Development Customer DB"
- B8: "Development"
- C8: "Sensitive"
- D8: "On-Premises"
- E8: "PII"
- F8: "✅ Mandatory"
- G8: "Yes"
- H8: "SDM"
- I8: "Informatica Data Masking"
- J8: "100%"
- K8: "18.01.2026"
- L8: "Dev Team Lead"
- M8: "Customer Data Owner"
- N8: "N/A"
- O8: "✅ Compliant"
- P8: "Weekly refresh with automated masking"
- Q8: "EV-NONPROD-001"
- R8: "Weekly"
- S8: "Automated"
- T8: "Yes"
- U8: "13.01.2026"
- V8: "20.01.2026"
- W8: "15"
- X8: "No"

**Styling:** Gray italic example row format (same as previous sheets)

## Data Entry Rows (9-38)

**30 rows for non-production environment assessment**

**Row 9-38 Styling:**

- **Fill:** #FFFFCC (Light Yellow) - All cells
- **Font:** Calibri 10pt Regular, Black
- **Border:** Thin all sides
- **Cell Protection:** Unlocked (user input)

**Data Validation for Extended Columns:**

**Column R (Data Refresh Frequency):** Dropdown:
```
Daily, Weekly, Monthly, Ad-hoc, Never
```

**Column S (Refresh Process):** Dropdown:
```
Automated, Manual, Hybrid
```

**Column T (Masking in Refresh Script?):** Dropdown:
```
Yes, No, N/A
```

**Conditional Formatting for Column T:**

- If "Yes" → Fill #C6EFCE (Green)
- If "No" → Fill #FFC7CE (Red) + Bold Red text
- If "N/A" → No fill

**Columns U-V (Dates):** Date format "dd.mm.yyyy"

**Column W (Developer Access Count):** Number validation:

- Type: Whole number
- Minimum: 0
- Maximum: 1000

**Column X (Contractor Access?):** Dropdown:
```
Yes, No, N/A
```

**Conditional Formatting for Column X:**

- If "Yes" → Fill #FFEB9C (Yellow) - Warning, third-party risk

**CRITICAL: Conditional Formatting for Column J (Coverage %):**

- If <100% → Fill #FFC7CE (Red) + Bold Red text + Red border (thick 3pt)
- If =100% → Fill #C6EFCE (Green)
- This visual indicator is CRITICAL for identifying gaps

**Conditional Formatting for Column O (Compliance Status):**

- Enhanced for this sheet:
- If "❌ Non-Compliant" → Fill #FFC7CE (Red) + Bold + Red border (thick 3pt all sides)

## Compliance Checklist (Rows 41-62)

**Row 41 - Section Header:**

- **Merge:** A41:X41
- **Text:** "NON-PRODUCTION ENVIRONMENT CHECKLIST - 100% COVERAGE REQUIRED"
- **Font:** Calibri 12pt Bold
- **Fill:** #FF0000 (Red), White text
- **Row Height:** 30px

**Rows 43-62 - Checklist Items (20 items):**

1. ✅ ALL non-production environments inventoried (Dev/Test/UAT/Staging/Training/Sandbox)
2. ✅ 100% masking coverage verified for ALL environments with production data
3. ✅ Data refresh scripts include automated masking step (not manual)
4. ✅ Direct production database cloning prohibited (policy enforced)
5. ✅ Developer workstations with local DB copies inventoried and masked
6. ✅ Ephemeral CI/CD test environments masked (automated in pipeline)
7. ✅ Contractor/offshore access restricted to masked environments only
8. ✅ Data refresh process documented (who, what, when, how)
9. ✅ Masking verification performed after each data refresh
10. ✅ Schema changes trigger re-masking (automated or documented process)
11. ❌ No environments with <100% coverage (if any exist, document as CRITICAL gap)
12. ❌ No "we'll mask it later" environments (policy prohibits deferral)
13. ⚠️ Training environments use synthetic/substitution data (preferred over masked production)
14. ⚠️ Sandbox/POC environments deleted after project completion (data minimization)
15. ⚠️ Non-production data retention limited (30-90 days typical, not indefinite)
16. 📋 Exception process: If <100% coverage, MUST have Data Owner + CISO approval
17. 📋 Exceptions documented in Gap_Analysis sheet with remediation plan
18. 📋 Exceptions reviewed quarterly (auto-expire after 90 days)
19. 🔍 Spot checks performed monthly (random non-prod environment verification)
20. 🔍 Annual comprehensive re-validation (all non-prod environments tested)

**Status Dropdown:** Same as previous sheets (✅ Complete, ⚠️ Partial, ❌ Missing, N/A)

**Notes Column:** Text input for explanations/exceptions

---

# Sheet 5: Analytics_Reporting

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:W1
- **Text:** "ANALYTICS & REPORTING ENVIRONMENT ASSESSMENT"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px

**Row 2 - Policy Reference:**

- **Merge:** A2:W2
- **Text:** "Analytics and reporting environments SHALL mask individual-level PII. Aggregation and anonymization preferred over row-level masking. (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 3.3)"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Row Height:** Auto (wrapped)

## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:T4
- **Text:** "Are analytics and reporting environments configured to mask or aggregate individual-level PII?"
- **Font:** Calibri 10pt Bold

**Cell U4 - Response:**

- **Data Validation:** Dropdown: "Yes (Masked), Yes (Aggregated), Partial, No"
- **Fill:** #FFFFCC (Yellow)

**Cell V4-W4 - Label:**

- **Merge:** V4:W4
- **Text:** "Response:"
- **Alignment:** Right

## Column Headers (Row 6)

**Standard Columns A-Q** (as defined in Standard Column Structure)

**PLUS Extended Columns R-W:**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Platform Type | 20 | Dropdown | BI Tool, Data Warehouse, Data Lake, ML Platform, Reporting, Other |
| S | Data Granularity | 18 | Dropdown | Individual-level, Aggregated, Anonymized, Mixed |
| T | Analyst Access Count | 12 | Number | Whole number |
| U | External Access? | 15 | Dropdown | Yes (Vendors/Consultants), No, N/A |
| V | PII Visible? | 15 | Dropdown | Yes, No, Partial |
| W | Aggregation Level | 18 | Dropdown | Row-level, k≥5, k≥10, k≥20, Fully Aggregated, N/A |

**Row 6 Styling:** Same as previous sheets

## Example Row (Row 7)

**Sample Analytics Environment:**

- A7: "Snowflake Data Warehouse"
- B7: "Analytics"
- C7: "Confidential"
- D7: "AWS"
- E7: "PII"
- F7: "✅ Mandatory"
- G7: "Yes"
- H7: "Anonymization"
- I7: "Snowflake Dynamic Data Masking"
- J7: "100%"
- K7: "15.01.2026"
- L7: "Analytics Platform Manager"
- M7: "Customer Data Owner"
- N7: "N/A"
- O7: "✅ Compliant"
- P7: "k-anonymity ≥10 for all customer reports"
- Q7: "EV-ANALYTICS-001"
- R7: "Data Warehouse"
- S7: "Aggregated"
- T7: "25"
- U7: "Yes (Vendors/Consultants)"
- V7: "No"
- W7: "k≥10"

**Styling:** Gray italic example row

## Data Entry Rows (8-37)

**30 rows for analytics/reporting environment assessment**

**Styling:** Yellow input cells, standard format

**Data Validation for Extended Columns:**

**Column R (Platform Type):** Dropdown:
```
BI Tool, Data Warehouse, Data Lake, ML Platform, Reporting, Other
```

**Column S (Data Granularity):** Dropdown:
```
Individual-level, Aggregated, Anonymized, Mixed
```

**Conditional Formatting for Column S:**

- If "Individual-level" AND Column V="Yes" (PII Visible) → Fill #FFC7CE (Red) + Bold
- If "Aggregated" OR "Anonymized" → Fill #C6EFCE (Green)

**Column T (Analyst Access Count):** Number validation:

- Type: Whole number
- Minimum: 0
- Maximum: 1000

**Column U (External Access?):** Dropdown:
```
Yes (Vendors/Consultants), No, N/A
```

**Conditional Formatting for Column U:**

- If "Yes (Vendors/Consultants)" → Fill #FFEB9C (Yellow) - Warning flag

**Column V (PII Visible?):** Dropdown:
```
Yes, No, Partial
```

**Conditional Formatting for Column V:**

- If "Yes" → Fill #FFC7CE (Red) + Bold Red text
- If "No" → Fill #C6EFCE (Green)
- If "Partial" → Fill #FFEB9C (Yellow)

**Column W (Aggregation Level):** Dropdown:
```
Row-level, k≥5, k≥10, k≥20, Fully Aggregated, N/A
```

**Note:** k-anonymity means each record is indistinguishable from at least k-1 other records

## Compliance Checklist (Rows 40-56)

**Row 40 - Section Header:**

- **Text:** "ANALYTICS & REPORTING CHECKLIST"
- **Styling:** #4472C4 header

**Rows 42-56 - Checklist Items (15 items):**

1. All BI tools, data warehouses, data lakes inventoried
2. ML/AI platforms and training datasets inventoried
3. Individual-level PII masked or aggregated (no raw customer records)
4. BI dashboards query masked views (verified by analyst login)
5. Data warehouse ETL includes masking/aggregation step
6. Reporting platforms use aggregated data (minimum k≥5)
7. ML training datasets anonymized (models don't leak PII)
8. Export functionality restricted (analysts cannot export raw PII)
9. Ad-hoc query tools (SQL clients) access masked views only
10. Personal Excel/CSV exports prohibited (or automatically masked)
11. External consultant access limited to aggregated data
12. Vendor-hosted analytics (SaaS BI) have DPAs and masking
13. Data retention in analytics limited (not indefinite historical storage)
14. Analytics platform access logged and reviewed
15. Annual re-validation of aggregation effectiveness

**Status Dropdown:** Same as previous sheets

---

# Sheet 6: Backup_Archive

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:X1
- **Text:** "BACKUP & ARCHIVE ASSESSMENT"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px

**Row 2 - Policy Reference:**

- **Merge:** A2:X2
- **Text:** "Backup environments MAY contain unmasked data IF encrypted (AES-256 minimum) and access-controlled. Masking required where technically feasible. Archive systems follow retention policies. (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 3.4)"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Row Height:** Auto (wrapped)

## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:U4
- **Text:** "Are all backups containing sensitive data encrypted at rest? Is masking applied where technically feasible?"
- **Font:** Calibri 10pt Bold

**Cell V4 - Response (Encryption):**

- **Data Validation:** Dropdown: "Yes (All Encrypted), Partial, No"
- **Fill:** #FFFFCC (Yellow)

**Cell W4 - Label:**

- **Text:** "Encryption:"
- **Alignment:** Right

**Row 5:**

- **Merge:** A5:U5
- **Text:** "Secondary question: Are export backups for testing purposes masked before distribution?"
- **Font:** Calibri 10pt Italic

**Cell V5 - Response (Masking):**

- **Data Validation:** Dropdown: "Yes, Partial, No, N/A (No exports)"
- **Fill:** #FFFFCC (Yellow)

**Cell W5 - Label:**

- **Text:** "Masking:"
- **Alignment:** Right

## Column Headers (Row 7)

**Standard Columns A-Q** (as defined in Standard Column Structure)

**PLUS Extended Columns R-X:**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Backup Type | 18 | Dropdown | Full, Incremental, Differential, Transaction Log, Snapshot, Archive |
| S | Backup Frequency | 15 | Dropdown | Hourly, Daily, Weekly, Monthly, Yearly |
| T | Retention Period | 15 | Dropdown | 7 days, 30 days, 90 days, 1 year, 3 years, 7 years, >7 years |
| U | Encryption Method | 18 | Dropdown | AES-256, TDE, Disk Encryption, None |
| V | Encryption at Rest? | 15 | Dropdown | Yes, No, Partial |
| W | Encryption in Transit? | 15 | Dropdown | Yes, No, N/A |
| X | Key Management | 18 | Dropdown | KMS, HSM, Manual, N/A |

**Additional Columns (Continue if needed):**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| Y | Restore Access Control | 20 | Dropdown | Restricted (≤3 people), General (>3 people), None |
| Z | Masking Feasible? | 15 | Dropdown | Yes, No, Conditional |
| AA | Masking Applied? | 15 | Dropdown | Yes, No, N/A |

**Note:** Columns Y-AA extend beyond standard Q, requiring column width adjustments

**Row 7 Styling:** Same as previous sheets (may need to extend merge for title rows)

## Example Row (Row 8)

**Sample Backup System:**

- A8: "Production DB Daily Backup"
- B8: "Backup"
- C8: "Sensitive"
- D8: "On-Premises"
- E8: "PII"
- F8: "⚠️ Conditional"
- G8: "No (Encrypted instead)"
- H8: "Encryption"
- I8: "Veeam Backup"
- J8: "N/A"
- K8: "19.01.2026"
- L8: "Backup Administrator"
- M8: "IT Operations Manager"
- N8: "Yes (CISO approved)"
- O8: "✅ Compliant"
- P8: "Full backup encrypted AES-256, restore restricted to 2 admins"
- Q8: "EV-BACKUP-001"
- R8: "Full"
- S8: "Daily"
- T8: "30 days"
- U8: "AES-256"
- V8: "Yes"
- W8: "Yes"
- X8: "KMS"
- Y8: "Restricted (≤3 people)"
- Z8: "No"
- AA8: "N/A"

**Styling:** Gray italic example row

## Data Entry Rows (9-38)

**30 rows for backup/archive assessment**

**Styling:** Yellow input cells, standard format

**Data Validation for Extended Columns:**

**Column R (Backup Type):** Dropdown:
```
Full, Incremental, Differential, Transaction Log, Snapshot, Archive
```

**Column S (Backup Frequency):** Dropdown:
```
Hourly, Daily, Weekly, Monthly, Yearly
```

**Column T (Retention Period):** Dropdown:
```

7 days, 30 days, 90 days, 1 year, 3 years, 7 years, >7 years

```

**Column U (Encryption Method):** Dropdown:
```
AES-256, TDE, Disk Encryption, None
```

**Conditional Formatting for Column U:**

- If "None" AND Column E ≠ "None" (has sensitive data) → Fill #FFC7CE (Red) + Bold
- If "AES-256" OR "TDE" → Fill #C6EFCE (Green)
- If "Disk Encryption" → Fill #FFEB9C (Yellow) - Less secure than application-level

**Column V (Encryption at Rest?):** Dropdown:
```
Yes, No, Partial
```

**Conditional Formatting for Column V:**

- If "No" → Fill #FFC7CE (Red) + Bold Red text
- If "Yes" → Fill #C6EFCE (Green)

**Column W (Encryption in Transit?):** Dropdown:
```
Yes, No, N/A
```

**Column X (Key Management):** Dropdown:
```
KMS, HSM, Manual, N/A
```

**Column Y (Restore Access Control):** Dropdown:
```
Restricted (≤3 people), General (>3 people), None
```

**Conditional Formatting for Column Y:**

- If "None" → Fill #FFC7CE (Red)
- If "Restricted (≤3 people)" → Fill #C6EFCE (Green)
- If "General (>3 people)" → Fill #FFEB9C (Yellow)

**Column Z (Masking Feasible?):** Dropdown:
```
Yes, No, Conditional
```

**Column AA (Masking Applied?):** Dropdown:
```
Yes, No, N/A
```

**Conditional Logic for Columns Z-AA:**

- If Z="Yes" (feasible) AND AA="No" (not applied) → Red flag, potential gap
- If Z="No" (not feasible) AND V="Yes" (encrypted) → Acceptable (compensating control)

## Compliance Checklist (Rows 41-54)

**Row 41 - Section Header:**

- **Text:** "BACKUP & ARCHIVE CHECKLIST"
- **Styling:** #4472C4 header

**Rows 43-54 - Checklist Items (12 items):**

1. All backup systems inventoried (production, DR, archive)
2. Encryption verified for all backups containing sensitive data (AES-256 minimum)
3. Encryption at rest enabled (storage-level encryption)
4. Encryption in transit enabled (TLS 1.2+ for network backups)
5. Key management properly configured (KMS or HSM, not manual)
6. Key rotation policy in place (annual minimum)
7. Restore access restricted (principle of least privilege, ≤3 backup admins)
8. Restore operations logged (audit trail)
9. Masking applied where technically feasible (export backups for testing)
10. Backup retention periods align with legal requirements (documented in policy)
11. Offline/tape backups encrypted (physical media protection)
12. Annual restore test performed (validates encryption doesn't break recovery)

**Status Dropdown:** Same as previous sheets

## Reference Tables (Starting Row 58)

**Backup Encryption Best Practices Table:**

| Backup Type | Masking Feasible? | Recommended Approach | Rationale |
|-------------|-------------------|---------------------|-----------|
| Full Database Backup | No | Encryption only (AES-256) | Byte-for-byte restore required |
| Transaction Log Backup | No | Encryption only | Point-in-time recovery breaks if masked |
| DR Hot Standby | No | Encryption + replication | Must be exact replica for failover |
| Incremental Backup | No | Encryption only | Delta changes, masking breaks chain |
| Export for Testing | Yes | Mask BEFORE backup | Separate use case from disaster recovery |
| Archive (Compliance) | Conditional | Assess if restore needed | If no restore needed, can mask |
| File-level Backup | Yes | Mask files BEFORE backup | Especially for reports, exports |

**Retention Period Reference Table:**

| Data Category | Legal Minimum | Legal Maximum | Typical Retention |
|---------------|---------------|---------------|------------------|
| Financial Records | 7 years | N/A | 7 years |
| Tax Documents | 7 years | N/A | 7 years |
| Employee Records | 3 years (after termination) | N/A | 10 years |
| Customer Data | None (GDPR deletion) | N/A | 3-5 years (business need) |
| Health Data (HIPAA) | 6 years | N/A | 6 years |
| Audit Logs | 1 year (ISO 27001) | N/A | 2-3 years |

---

**END OF PART II - SECTION 2**

**Completed Sheets:**

- Sheet 1: Instructions_Legend ✅
- Sheet 2: Environment_Inventory ✅
- Sheet 3: Production_Environment ✅
- Sheet 4: NonProduction_Environments ✅
- Sheet 5: Analytics_Reporting ✅
- Sheet 6: Backup_Archive ✅

---

# Sheet 7: External_Sharing

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:Y1
- **Text:** "EXTERNAL DATA SHARING ASSESSMENT"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px

**Row 2 - Policy Reference:**

- **Merge:** A2:Y2
- **Text:** "External data sharing SHALL be masked unless contractually required and formally risk-accepted by Data Owner + CISO. All external sharing requires DPA (GDPR Art. 28). (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 3.5)"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Row Height:** Auto (wrapped)

## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:V4
- **Text:** "Is all external data sharing (vendors, auditors, customers, partners) properly masked or formally approved as exception?"
- **Font:** Calibri 10pt Bold

**Cell W4 - Response:**

- **Data Validation:** Dropdown: "Yes (All Masked), Yes (Approved Exceptions), Partial, No"
- **Fill:** #FFFFCC (Yellow)

**Cell X4-Y4 - Label:**

- **Merge:** X4:Y4
- **Text:** "Response:"
- **Alignment:** Right

**Row 5 - Reminder:**

- **Merge:** A5:Y5
- **Text:** "⚠️ REMINDER: Data Processing Agreements (DPAs) required for ALL external processors per GDPR Art. 28"
- **Font:** Calibri 9pt Bold, Blue text (#003366)
- **Fill:** #B4C7E7 (Light Blue)
- **Alignment:** Center

## Column Headers (Row 7)

**Standard Columns A-Q** (as defined in Standard Column Structure)

**PLUS Extended Columns R-Y:**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | External Party Name | 25 | Text | Free text (company/organization name) |
| S | External Party Type | 18 | Dropdown | Vendor, Partner, Auditor, Regulator, Customer, Offshore Team, Other |
| T | Purpose of Sharing | 25 | Text | Free text, wrapped |
| U | Contractual Requirement? | 18 | Dropdown | Yes (Unmasked Required), No (Can Be Masked), Conditional |
| V | DPA in Place? | 12 | Dropdown | Yes, No, N/A |
| W | Data Transfer Method | 18 | Dropdown | SFTP, API, Email (encrypted), Physical Media, Portal, Other |
| X | Transfer Frequency | 15 | Dropdown | One-time, Daily, Weekly, Monthly, On-demand |
| Y | Access Duration | 18 | Dropdown | Permanent, Temporary (specify end date in notes) |

**Additional Columns (if space permits):**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| Z | Data Volume | 15 | Text | Number of records or file size |
| AA | Risk Assessment Done? | 15 | Dropdown | Yes, No, N/A |
| AB | CISO Approval Date | 15 | Date | Date picker (dd.mm.yyyy) |

**Row 7 Styling:** Same as previous sheets, extended merge for title rows

## Example Row (Row 8)

**Sample External Sharing Arrangement:**

- A8: "Vendor Support Portal"
- B8: "External"
- C8: "Confidential"
- D8: "Vendor SaaS"
- E8: "PII"
- F8: "✅ Mandatory"
- G8: "Yes"
- H8: "Redaction"
- I8: "Manual masking process"
- J8: "100%"
- K8: "10.01.2026"
- L8: "IT Operations Manager"
- M8: "Customer Data Owner"
- N8: "N/A"
- O8: "✅ Compliant"
- P8: "Support tickets with redacted customer details"
- Q8: "EV-EXT-001"
- R8: "TechSupport Inc."
- S8: "Vendor"
- T8: "Technical support and troubleshooting"
- U8: "No (Can Be Masked)"
- V8: "Yes"
- W8: "Portal"
- X8: "On-demand"
- Y8: "Permanent"
- Z8: "~50 tickets/month"
- AA8: "Yes"
- AB8: "05.12.2025"

**Styling:** Gray italic example row

## Data Entry Rows (9-38)

**30 rows for external sharing assessment**

**Styling:** Yellow input cells, standard format

**Data Validation for Extended Columns:**

**Column S (External Party Type):** Dropdown:
```
Vendor, Partner, Auditor, Regulator, Customer, Offshore Team, Other
```

**Conditional Formatting for Column S:**

- If "Offshore Team" → Fill #FFEB9C (Yellow) - Cross-border risk flag
- If "Regulator" → Fill #B4C7E7 (Blue) - Special handling

**Column U (Contractual Requirement?):** Dropdown:
```
Yes (Unmasked Required), No (Can Be Masked), Conditional
```

**Conditional Formatting for Column U:**

- If "Yes (Unmasked Required)" → Fill #FFEB9C (Yellow) - Requires exception approval
- If "No (Can Be Masked)" AND Column G="No" → Fill #FFC7CE (Red) - Should be masked

**Column V (DPA in Place?):** Dropdown:
```
Yes, No, N/A
```

**Conditional Formatting for Column V:**

- If "No" AND Column S = "Vendor" OR "Partner" OR "Offshore Team" → Fill #FFC7CE (Red) + Bold
  - **Rationale:** GDPR Art. 28 violation
- If "Yes" → Fill #C6EFCE (Green)

**Column W (Data Transfer Method):** Dropdown:
```
SFTP, API, Email (encrypted), Physical Media, Portal, Other
```

**Conditional Formatting for Column W:**

- If contains "Email" AND NOT "encrypted" → Flag as potential risk (note: requires text parsing)

**Column X (Transfer Frequency):** Dropdown:
```
One-time, Daily, Weekly, Monthly, On-demand
```

**Column Y (Access Duration):** Dropdown:
```
Permanent, Temporary (specify end date in notes)
```

**Conditional Formatting for Column Y:**

- If "Temporary" → Fill #B4C7E7 (Blue) - Ensure end date in notes

**Column AA (Risk Assessment Done?):** Dropdown:
```
Yes, No, N/A
```

**Conditional Formatting for Column AA:**

- If "No" AND Column U = "Yes (Unmasked Required)" → Fill #FFC7CE (Red)
  - **Rationale:** Unmasked sharing without risk assessment = policy violation

**Column AB (CISO Approval Date):** Date format "dd.mm.yyyy"

**Validation Logic Across Columns:**

- If Column G (Masking Deployed?) = "No" (unmasked)
  - THEN Column N (Exception Approved?) MUST = "Yes"
  - AND Column AA (Risk Assessment Done?) MUST = "Yes"
  - AND Column AB (CISO Approval Date) MUST NOT be blank
  - **Otherwise:** Red flag for gap analysis

## Compliance Checklist (Rows 41-57)

**Row 41 - Section Header:**

- **Text:** "EXTERNAL SHARING CHECKLIST"
- **Styling:** #4472C4 header

**Rows 43-57 - Checklist Items (15 items):**

1. All external data sharing arrangements documented (vendors, auditors, customers, partners)
2. DPAs in place for ALL data processors (GDPR Art. 28 mandatory)
3. Unmasked sharing has formal risk acceptance (Data Owner + CISO approval)
4. Risk assessments completed for all unmasked sharing
5. Data transfer methods secure (encrypted in transit - SFTP, TLS, encrypted email)
6. No unencrypted email attachments with sensitive data
7. Access is time-limited where feasible (revoke after project completion)
8. Quarterly access review (who still has access, is it still needed?)
9. Vendor contracts include data protection clauses
10. Offshore data transfers comply with GDPR/FADP cross-border requirements
11. Customer data exports limited to their data only (no over-sharing)
12. Auditor access documented and time-limited (delete data after audit)
13. Physical media transfers encrypted (USB drives, tapes)
14. Portal/API access logged (audit trail for external access)
15. Annual DPA review (contracts still valid, clauses current?)

**Status Dropdown:** Same as previous sheets

## Reference Table: Cross-Border Data Transfer Requirements (Starting Row 61)

**GDPR/FADP Cross-Border Transfer Mechanisms:**

| Mechanism | When Applicable | Requirements | Masking Impact |
|-----------|----------------|--------------|----------------|
| EU Adequacy Decision | Transfer to "adequate" countries (UK, Switzerland, Japan, etc.) | None (adequacy assumed) | Masking still required per purpose limitation |
| Standard Contractual Clauses (SCCs) | Transfer to non-adequate countries | Sign EU SCCs or Swiss TCC | Masking recommended, not waived by SCCs |
| Binding Corporate Rules (BCRs) | Intra-group transfers (multinational corporations) | BCR approval by DPA | Masking policy should be in BCRs |
| Consent | Individual consent for each transfer | Explicit, informed consent | Masking still best practice |
| Derogations | Limited, case-by-case transfers | Specific legal grounds (contract performance, legal claim, etc.) | Case-specific assessment |

**Note:** Masking requirements are independent of cross-border transfer mechanisms. Even with SCCs, data minimization (masking) is best practice.

---

# Sheet 8: Cloud_Environments

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:X1
- **Text:** "CLOUD ENVIRONMENT ASSESSMENT"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px

**Row 2 - Policy Reference:**

- **Merge:** A2:X2
- **Text:** "Cloud environments SHALL follow same masking rules as on-premises. Cloud hosting does NOT exempt from masking requirements. (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 3.6)"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Row Height:** Auto (wrapped)

## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:U4
- **Text:** "Are cloud-hosted environments (AWS, Azure, GCP, SaaS) classified and masked according to same requirements as on-premises?"
- **Font:** Calibri 10pt Bold

**Cell V4 - Response:**

- **Data Validation:** Dropdown: "Yes (Same Rules), Partial, No"
- **Fill:** #FFFFCC (Yellow)

**Cell W4-X4 - Label:**

- **Merge:** W4:X4
- **Text:** "Response:"
- **Alignment:** Right

**Row 5 - Reminder:**

- **Merge:** A5:X5
- **Text:** "⚠️ CLOUD REMINDER: Production cloud = same as on-prem production. Non-prod cloud = 100% masking (same as on-prem non-prod)"
- **Font:** Calibri 9pt Bold
- **Fill:** #B4C7E7 (Light Blue)
- **Alignment:** Center

## Column Headers (Row 7)

**Standard Columns A-Q** (as defined in Standard Column Structure)

**PLUS Extended Columns R-X:**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Cloud Provider | 18 | Dropdown | AWS, Azure, GCP, Multi-Cloud, SaaS, Other |
| S | Cloud Service | 22 | Text | Free text (e.g., RDS, SQL Database, BigQuery, Salesforce) |
| T | Region/Location | 18 | Text | Free text (e.g., us-east-1, eu-central-1, Switzerland) |
| U | Account/Subscription ID | 20 | Text | Free text (for cloud resource tracking) |
| V | Multi-Tenant? | 12 | Dropdown | Yes (SaaS), No (Dedicated), N/A |
| W | Data Residency Compliant? | 18 | Dropdown | Yes, No, N/A |
| X | Cloud-Specific Controls | 25 | Text | Free text, wrapped (e.g., AWS Macie, Azure Purview) |

**Row 7 Styling:** Same as previous sheets

## Example Row (Row 8)

**Sample Cloud Environment:**

- A8: "AWS RDS Production Customer DB"
- B8: "Production"
- C8: "Sensitive"
- D8: "AWS"
- E8: "PII"
- F8: "⚠️ Conditional"
- G8: "Yes"
- H8: "DDM"
- I8: "AWS RDS Native Masking"
- J8: "90%"
- K8: "18.01.2026"
- L8: "Cloud Infrastructure Manager"
- M8: "Customer Data Owner"
- N8: "N/A"
- O8: "✅ Compliant"
- P8: "DDM for API access, encryption at rest"
- Q8: "EV-CLOUD-001"
- R8: "AWS"
- S8: "RDS PostgreSQL"
- T8: "eu-central-1 (Frankfurt)"
- U8: "123456789012/prod-db-cluster"
- V8: "No (Dedicated)"
- W8: "Yes"
- X8: "RDS encryption, IAM policies, CloudTrail logging"

**Styling:** Gray italic example row

## Data Entry Rows (9-38)

**30 rows for cloud environment assessment**

**Styling:** Yellow input cells, standard format

**Data Validation for Extended Columns:**

**Column R (Cloud Provider):** Dropdown:
```
AWS, Azure, GCP, Multi-Cloud, SaaS, Other
```

**Column V (Multi-Tenant?):** Dropdown:
```
Yes (SaaS), No (Dedicated), N/A
```

**Conditional Formatting for Column V:**

- If "Yes (SaaS)" → Fill #FFEB9C (Yellow) - Vendor-managed risk

**Column W (Data Residency Compliant?):** Dropdown:
```
Yes, No, N/A
```

**Conditional Formatting for Column W:**

- If "No" → Fill #FFC7CE (Red) - GDPR/FADP data residency violation

## Compliance Checklist (Rows 41-60)

**Row 41 - Section Header:**

- **Text:** "CLOUD ENVIRONMENT CHECKLIST"
- **Styling:** #4472C4 header

**Rows 43-60 - Checklist Items (18 items):**

1. All cloud accounts/subscriptions inventoried (AWS, Azure, GCP, multi-cloud)
2. Cloud resources tagged (Owner, Environment, Project, Data Classification)
3. Cloud production environments follow on-prem production rules (DDM conditional)
4. Cloud non-production environments 100% masked (same as on-prem non-prod)
5. SaaS platforms data protection verified (vendor questionnaires, certifications)
6. IaaS/PaaS databases classified (same as on-prem databases)
7. Cloud dev/test databases masked (no "it's just cloud dev" exemption)
8. Cloud sandbox accounts governed (approval required, auto-expire)
9. Cloud storage buckets (S3, Blob, GCS) containing sensitive data encrypted
10. Cloud-native masking tools configured (AWS Macie, Azure Purview, GCP DLP)
11. Data residency requirements met (GDPR/FADP compliant regions)
12. Cross-region replication masked (if replicating to non-compliant regions)
13. Cloud backup/snapshot encryption enabled (same as on-prem backup requirements)
14. Cloud access logged (CloudTrail, Activity Log, Cloud Audit Logs)
15. Multi-cloud environments consistent (no cloud provider exemptions)
16. SaaS vendor DPAs in place (GDPR Art. 28)
17. Cloud cost alerts configured (detect forgotten resources)
18. Quarterly cloud inventory reconciliation (billing vs. documented resources)

**Status Dropdown:** Same as previous sheets

## Cloud Provider-Specific Reference Table (Starting Row 64)

**Cloud-Native Masking & Data Protection Tools:**

| Cloud Provider | Data Discovery | Masking/Encryption | Access Control | Monitoring |
|----------------|----------------|-------------------|----------------|------------|
| **AWS** | Macie (PII discovery) | RDS encryption, S3 encryption, KMS | IAM policies, SCPs | CloudTrail, GuardDuty |
| **Azure** | Purview (data catalog) | SQL TDE, Disk encryption, Key Vault | RBAC, Entra ID | Activity Log, Sentinel |
| **GCP** | Cloud DLP (sensitive data) | Cloud SQL encryption, Cloud KMS | IAM, VPC Service Controls | Cloud Audit Logs, SCC |
| **Multi-Cloud** | Third-party tools (BigID, Collibra) | Cross-cloud masking tools | Centralized IAM (Okta, etc.) | SIEM aggregation |

**SaaS Platform Data Protection Checklist:**

| SaaS Platform | PII Storage? | DPA Required? | Data Residency Control? | Masking Available? |
|---------------|--------------|---------------|------------------------|-------------------|
| Salesforce | Yes (CRM data) | Yes | Yes (region selection) | Field-level encryption, Shield |
| Workday | Yes (HR data) | Yes | Yes (regional datacenters) | Limited (vendor manages) |
| ServiceNow | Yes (tickets) | Yes | Yes (instance location) | Field-level encryption |
| Office 365 | Yes (emails, files) | Yes | Yes (geo selection) | Sensitivity labels, DLP |
| Google Workspace | Yes (emails, Drive) | Yes | Yes (region preference) | DLP, encryption at rest |

---

# Sheet 9: Data_Flow_Mapping

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:Z1
- **Text:** "DATA FLOW MAPPING & MASKING CHECKPOINTS"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px

**Row 2 - Policy Reference:**

- **Merge:** A2:Z2
- **Text:** "Data flows between environments SHALL have documented masking checkpoints. Production → Non-Production flows MUST include masking step. (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 3.7)"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Row Height:** Auto (wrapped)

## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:W4
- **Text:** "Are all data flows mapped with masking checkpoints identified and validated?"
- **Font:** Calibri 10pt Bold

**Cell X4 - Response:**

- **Data Validation:** Dropdown: "Yes (All Flows), Partial, No"
- **Fill:** #FFFFCC (Yellow)

**Cell Y4-Z4 - Label:**

- **Merge:** Y4:Z4
- **Text:** "Response:"
- **Alignment:** Right

**Row 5 - Critical Reminder:**

- **Merge:** A5:Z5
- **Text:** "🚨 CRITICAL: Production → Non-Production flows WITHOUT masking checkpoint = POLICY VIOLATION (automatic P1 gap)"
- **Font:** Calibri 9pt Bold, Red text
- **Fill:** #FFC7CE (Light Red)
- **Alignment:** Center

## Column Headers (Row 7)

**Custom Column Structure for Data Flow Mapping:**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| A | Flow ID | 12 | Text | Free text (e.g., FLOW-001) |
| B | Source Environment | 25 | Text | Free text (from Environment_Inventory) |
| C | Destination Environment | 25 | Text | Free text (from Environment_Inventory) |
| D | Flow Description | 30 | Text | Free text, wrapped |
| E | Flow Frequency | 15 | Dropdown | Real-time, Hourly, Daily, Weekly, Monthly, On-demand |
| F | Flow Mechanism | 20 | Dropdown | ETL, Replication, API, File Transfer, Manual |
| G | Sensitive Data Transferred? | 15 | Dropdown | Yes, No, Unknown |
| H | Masking Checkpoint Exists? | 15 | Dropdown | Yes, No, N/A |
| I | Checkpoint Location | 18 | Dropdown | At Source, In Pipeline, At Destination, None |
| J | Masking Technique Used | 20 | Dropdown | SDM, DDM, Tokenization, Redaction, Aggregation, None |
| K | Checkpoint Automated? | 15 | Dropdown | Yes, Manual, N/A |
| L | Checkpoint Validation | 25 | Text | Free text (how masking is verified) |
| M | Failure Handling | 20 | Dropdown | Stop Flow, Alert Only, Continue (Non-Compliant), N/A |
| N | Last Verified Date | 15 | Date | Date picker (dd.mm.yyyy) |
| O | Flow Owner | 20 | Text | Free text (responsible for flow) |
| P | Compliance Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| Q | Notes/Comments | 30 | Text | Free text, wrapped |
| R | Evidence ID | 15 | Text | Link to Evidence_Register |

**Row 7 Styling:**

- **Fill:** #D9D9D9 (Light Gray)
- **Font:** Calibri 9pt Bold (smaller font due to many columns)
- **Alignment:** Center, Vertical Center, Wrapped
- **Border:** Thick bottom border (3pt)
- **Row Height:** 60px (accommodate wrapped text)

## Example Row (Row 8)

**Sample Data Flow:**

- A8: "FLOW-001"
- B8: "Production CRM Database"
- C8: "Development CRM Database"
- D8: "Weekly data refresh for dev testing"
- E8: "Weekly"
- F8: "ETL"
- G8: "Yes"
- H8: "Yes"
- I8: "In Pipeline"
- J8: "SDM"
- K8: "Yes"
- L8: "Automated validation script checks 100% coverage post-masking"
- M8: "Stop Flow"
- N8: "13.01.2026"
- O8: "Database Administrator"
- P8: "✅ Compliant"
- Q8: "Informatica ETL job includes masking transformation step"
- R8: "EV-FLOW-001"

**Styling:** Gray italic example row

## Data Entry Rows (9-38)

**30 rows for data flow mapping**

**Styling:** Yellow input cells, standard format

**Data Validation for Columns:**

**Column E (Flow Frequency):** Dropdown:
```
Real-time, Hourly, Daily, Weekly, Monthly, On-demand
```

**Column F (Flow Mechanism):** Dropdown:
```
ETL, Replication, API, File Transfer, Manual
```

**Column G (Sensitive Data Transferred?):** Dropdown:
```
Yes, No, Unknown
```

**Conditional Formatting for Column G:**

- If "Unknown" → Fill #FFEB9C (Yellow) - Requires investigation

**Column H (Masking Checkpoint Exists?):** Dropdown:
```
Yes, No, N/A
```

**CRITICAL Conditional Formatting for Column H:**

- If "No" AND Column G="Yes" (sensitive data) AND Destination is non-production → Fill #FFC7CE (Red) + Bold Red text + Thick red border
  - **Rationale:** Production → Non-Production flow WITHOUT masking = P1 GAP

**Column I (Checkpoint Location):** Dropdown:
```
At Source, In Pipeline, At Destination, None
```

**Column J (Masking Technique Used):** Dropdown:
```
SDM, DDM, Tokenization, Redaction, Aggregation, None
```

**Column K (Checkpoint Automated?):** Dropdown:
```
Yes, Manual, N/A
```

**Conditional Formatting for Column K:**

- If "Manual" → Fill #FFEB9C (Yellow) - Manual process = error risk

**Column M (Failure Handling):** Dropdown:
```
Stop Flow, Alert Only, Continue (Non-Compliant), N/A
```

**Conditional Formatting for Column M:**

- If "Continue (Non-Compliant)" → Fill #FFC7CE (Red) - Unmasked data could leak
- If "Stop Flow" → Fill #C6EFCE (Green) - Best practice

**Column P (Compliance Status):** Dropdown:
```
✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A
```

**Standard conditional formatting** for status column

## Compliance Checklist (Rows 41-54)

**Row 41 - Section Header:**

- **Text:** "DATA FLOW MAPPING CHECKLIST"
- **Styling:** #4472C4 header

**Rows 43-54 - Checklist Items (12 items):**

1. All major data flows mapped (production → non-prod, analytics, external)
2. Masking checkpoints identified for ALL flows with sensitive data
3. Production → Non-Production flows have masking checkpoint (100% required)
4. Checkpoint implementation verified (not just documented)
5. Checkpoint automation preferred (manual processes documented with mitigation)
6. Failure handling defined (masking fails → flow stops, not continues)
7. Bypass controls prevent skipping masking step
8. ETL/pipeline configurations reviewed (masking step present)
9. Real-time replication includes masking (or destination-side masking)
10. API integrations return masked data (application layer masking)
11. Data flow diagrams maintained (Visio, Lucidchart, etc.)
12. Annual data flow re-mapping (detect new flows, retired flows)

**Status Dropdown:** Same as previous sheets

## Data Flow Patterns Reference Table (Starting Row 58)

**Common Data Flow Patterns & Masking Checkpoints:**

| Flow Pattern | Example | Masking Checkpoint | Risk if No Checkpoint |
|--------------|---------|-------------------|----------------------|
| **Prod → Dev** | Weekly data refresh | In ETL pipeline (pre-load) | P1 GAP: Unmasked prod data in dev |
| **Prod → Analytics** | Nightly ETL to warehouse | At source (masked views) | Individual-level PII in reports |
| **Prod → Backup** | Daily backup job | N/A (encryption instead) | Acceptable if encrypted |
| **Prod → Vendor** | API integration | Application layer masking | Third-party sees real PII |
| **Analytics → Export** | BI dashboard export | Aggregation at source | Users export raw PII |
| **Dev → Staging** | Pre-production promotion | N/A (dev already masked) | Low risk (both non-prod) |
| **Staging → Prod** | Production deployment | ⚠️ Should NOT include data | Code only, no data flow |

**ETL Tool Masking Integration Examples:**

| ETL Tool | Masking Integration Method | Validation Approach |
|----------|---------------------------|---------------------|
| Informatica PowerCenter | Masking transformation component | Test mode preview, row counts |
| Talend | tMask component or custom Java | Unit tests on sample data |
| Apache Airflow | Custom Python masking operator | DAG task dependencies, assertions |
| AWS Glue | PySpark masking transforms | Glue Data Quality rules |
| Azure Data Factory | Data flow masking activity | Pipeline validation, monitoring |
| Google Dataflow | Apache Beam masking DoFn | Pipeline monitoring, assertions |

---

**END OF PART II - SECTION 3**

**Completed Assessment Sheets:**

- Sheet 1: Instructions_Legend ✅
- Sheet 2: Environment_Inventory ✅
- Sheet 3: Production_Environment ✅
- Sheet 4: NonProduction_Environments ✅
- Sheet 5: Analytics_Reporting ✅
- Sheet 6: Backup_Archive ✅
- Sheet 7: External_Sharing ✅
- Sheet 8: Cloud_Environments ✅
- Sheet 9: Data_Flow_Mapping ✅

**Next Section 4 (FINAL Technical Spec Section):**

- Sheet 10: Gap_Analysis
- Sheet 11: Evidence_Register
- Sheet 12: Summary_Dashboard
- Python Script Integration Notes
- Quality Assurance Requirements

**Shall the Grand ISMS Guru continue to enlighten you with the final sacred section? 🙏**

# ISMS-IMP-A.8.11.3 - Environment Coverage Assessment
# PART II: TECHNICAL SPECIFICATION - SECTION 4 (FINAL)

---

# Sheet 10: Gap_Analysis

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:O1
- **Text:** "GAP ANALYSIS & REMEDIATION ROADMAP"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px

**Row 2 - Policy Reference:**

- **Merge:** A2:O2
- **Text:** "All gaps (unmasked environments, missing checkpoints, policy exceptions) SHALL be documented, prioritized (P1-P4), assigned to owners, and remediated within SLA: P1≤30 days, P2≤90 days, P3≤180 days, P4≤365 days"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Row Height:** Auto (wrapped)

## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:L4
- **Text:** "Have ALL gaps from all assessment sheets been consolidated and assigned to owners with remediation plans?"
- **Font:** Calibri 10pt Bold

**Cell M4 - Response:**

- **Data Validation:** Dropdown: "Yes (All Documented), Partial, No"
- **Fill:** #FFFFCC (Yellow)

**Cell N4-O4 - Label:**

- **Merge:** N4:O4
- **Text:** "Response:"
- **Alignment:** Right

## Column Headers (Row 6)

**Gap Analysis Columns:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gap ID | 12 | Text | Free text (GAP-001, etc.) |
| B | Gap Category | 20 | Dropdown | Environment Inventory, Production, Non-Production, Analytics, Cloud, Backup, External, Data Flow |
| C | Gap Description | 40 | Text | Free text, wrapped |
| D | Environment(s) Affected | 25 | Text | Free text |
| E | Priority | 8 | Dropdown | P1, P2, P3, P4 |
| F | Risk Level | 12 | Dropdown | Critical, High, Medium, Low |
| G | Gap Owner | 20 | Text | Named individual |
| H | Supporting Teams | 22 | Text | DBAs, Cloud, Security, etc. |
| I | Remediation Action | 35 | Text | Specific steps |
| J | Target Date | 15 | Date | dd.mm.yyyy |
| K | Current Status | 15 | Dropdown | Not Started, In Progress, Blocked, Completed |
| L | Completion Date | 15 | Date | dd.mm.yyyy |
| M | Verification Method | 25 | Text | How closure verified |
| N | Evidence ID | 15 | Text | Link to Evidence_Register |
| O | Notes | 30 | Text | Wrapped |

**Row 6 Styling:**

- Fill: #D9D9D9, Font: Calibri 10pt Bold
- Border: Thick bottom (3pt)
- Row Height: 50px

## Data Entry Rows (7-46)

**40 rows for gaps**

**Conditional Formatting:**

**Column E (Priority):**

- P1 → #FFC7CE (Red) + Bold
- P2 → #FFEB9C (Yellow)
- P3 → #E7E6E6 (Light Gray)
- P4 → White

**Column K (Status):**

- Completed → #C6EFCE (Green) + Strikethrough
- Blocked → #FFC7CE (Red) + Bold
- In Progress → #B4C7E7 (Blue)
- Not Started → #FFEB9C (Yellow)

## Reference Tables (Starting Row 50)

**Priority SLA Matrix (Rows 50-56):**

| Priority | SLA | Examples |
|----------|-----|----------|
| P1 | ≤30 days | Unmasked non-prod, no DPA |
| P2 | ≤90 days | Missing DDM, analytics PII |
| P3 | ≤180 days | Manual processes, 90-99% coverage |
| P4 | ≤365 days | Documentation gaps |

---

# Sheet 11: Evidence_Register

## Header (Rows 1-2)

**Row 1:**

- Merge: A1:J1
- Text: "EVIDENCE REGISTER"
- Styling: #003366 header

**Row 2:**

- Merge: A2:J2
- Text: "Complete audit trail - Supporting documentation for all assessments"
- Styling: #E7E6E6 italic

## Columns (Row 4)

| Column | Header | Width |
|--------|--------|-------|
| A | Evidence ID | 15 |
| B | Evidence Type | 22 |
| C | Description | 40 |
| D | Related Environment | 25 |
| E | Document Name/Link | 35 |
| F | Date Created | 15 |
| G | Owner | 20 |
| H | Retention Period | 15 |
| I | Location | 30 |
| J | Notes | 30 |

## Data Entry Rows (5-104)

**100 rows for evidence**

**Evidence Type Examples:**

- Configuration, Screenshot, Log, Agreement, Script, Report, Audit Trail

---

# Sheet 12: Summary_Dashboard

## Complete Dashboard Structure

**Section 1: Overall Compliance (Rows 4-12)**

**Key Metrics with Formulas:**

| Metric | Formula | Target |
|--------|---------|--------|
| Overall Score | Weighted average | ≥90% |
| Non-Prod Masking | `=COUNTIF(NonProduction_Environments!O:O,"✅ Compliant")/COUNTA(NonProduction_Environments!A7:A37)*100` | 100% |
| Production DDM | `=COUNTIF(Production_Environment!O:O,"✅ Compliant")/COUNTA(Production_Environment!A7:A37)*100` | ≥90% |
| Cloud Coverage | `=COUNTIF(Cloud_Environments!O:O,"✅ Compliant")/COUNTA(Cloud_Environments!A7:A37)*100` | 100% |
| Critical Gaps | `=COUNTIF(Gap_Analysis!E:E,"P1")` | 0 |

**Weighted Average Formula:**
```
=(NonProd*0.35 + Production*0.20 + Cloud*0.15 + Analytics*0.15 + DataFlow*0.10 + Inventory*0.05)
```

**Section 2: Environment Breakdown (Rows 14-24)**

Counts by environment type with coverage percentages.

**Section 3: Critical Gaps (Rows 26-36)**

Top 10 P1/P2 gaps auto-populated from Gap_Analysis sheet.

**Section 4: Sign-Off (Rows 50-58)**

Executive approval table (IT Ops Manager, CISO, DPO, Legal).

---

# Python Script Integration

## Script Template Structure

```python
"""
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR A.8.11.3

Key customization areas:
1. Sheet structures (12 sheets, varying columns)
2. Dashboard formulas (references to 9 assessment sheets)
3. Conditional formatting (environment-specific)
4. Data validation (environment types, priorities)
"""

import openpyxl
from openpyxl.styles import *
from openpyxl.worksheet.datavalidation import DataValidation
from datetime import datetime

# Color palette
COLORS = {
    'header_main': '003366',
    'header_sub': '4472C4',
    'input': 'FFFFCC',
    'status_compliant': 'C6EFCE',
    'status_partial': 'FFEB9C',
    'status_noncompliant': 'FFC7CE'
}

def create_workbook():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    
    # Create all 12 sheets
    create_instructions_legend(wb)
    create_environment_inventory(wb)
    create_production_environment(wb)
    create_nonproduction_environments(wb)
    create_analytics_reporting(wb)
    create_backup_archive(wb)
    create_external_sharing(wb)
    create_cloud_environments(wb)
    create_data_flow_mapping(wb)
    create_gap_analysis(wb)
    create_evidence_register(wb)
    create_summary_dashboard(wb)  # LAST - references others
    
    filename = f"ISMS-IMP-A.8.11.3_Environment_Coverage_{datetime.now():%Y%m%d}.xlsx"
    wb.save(filename)
    return wb

# Implement each create_* function per specification
```

## Critical Implementation Notes

**Dashboard Formula Validation:**

- MUST verify all sheet names exist
- Test formulas with sample data
- Handle division by zero (empty sheets)

**Conditional Formatting:**

- Non-Production <100% → Red + Bold + Thick border
- Missing DPAs → Red + Bold
- P1 gaps → Red highlighting

**Cell Protection:**

- Lock all formula cells
- Unlock yellow input cells
- Enable sheet protection

---

# Quality Assurance Checklist

## Pre-Deployment

**Structure:**

- [ ] All 12 sheets present
- [ ] Sheet names exact
- [ ] Column headers match spec
- [ ] Row counts correct

**Formulas:**

- [ ] Dashboard calculates correctly
- [ ] No #REF! errors
- [ ] No #DIV/0! errors
- [ ] Conditional formulas trigger

**Formatting:**

- [ ] Colors consistent
- [ ] Fonts correct
- [ ] Borders applied
- [ ] Protection set

**Data Validation:**

- [ ] All dropdowns work
- [ ] Date formats correct
- [ ] No typos in options

## Post-Deployment

**Functional Testing:**
1. Fill 10 sample environments
2. Verify dropdowns
3. Check conditional formatting
4. Test Dashboard formulas

**User Acceptance:**
1. Pilot with test user
2. Collect feedback
3. Iterate

---

# Requirements Traceability

| Requirement | Sheet | How Assessed |
|-------------|-------|--------------|
| Complete inventory | Environment_Inventory | All systems documented |
| Non-prod 100% masked | NonProduction_Environments | Coverage % column |
| Production DDM | Production_Environment | Role-based masking |
| Cloud compliance | Cloud_Environments | Same rules as on-prem |
| External sharing | External_Sharing | DPAs + masking |
| Data flow checkpoints | Data_Flow_Mapping | Checkpoint tracking |
| Gap remediation | Gap_Analysis | SLA tracking |

---

**END OF PART II - TECHNICAL SPECIFICATION**

**Complete IMP-A.8.11.3 Package:**

- Part I: ~1,800 lines (User Guide)
- Part II: ~2,500 lines (Technical Spec)
- Total: ~4,300 lines

**Status:** APPROVED FOR IMPLEMENTATION

**Next Steps:**
1. Generate Python script
2. Create Excel template
3. Test with sample data
4. Deploy to teams

---

**END OF SPECIFICATION**

---

*"In the middle of difficulty lies opportunity."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
