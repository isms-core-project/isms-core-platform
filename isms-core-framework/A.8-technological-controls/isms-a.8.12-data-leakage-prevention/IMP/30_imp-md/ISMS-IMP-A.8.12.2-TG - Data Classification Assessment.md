**ISMS-IMP-A.8.12.2-TG - Data Classification Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention


---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.12.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Data Classification and Identification for DLP |
| **Related Policy** | ISMS-POL-A.8.12 (Data Leakage Prevention Policy) - Section 2.1 |
| **Purpose** | Assess data classification scheme implementation, sensitive data identification methods, and DLP rule accuracy to ensure protection scope aligns with organizational risk appetite |
| **Target Audience** | Data Classification Officers, DLP Administrators, Data Owners, Security Engineers, Compliance Officers, CISO |
| **Assessment Type** | Operational & Governance Assessment |
| **Review Cycle** | Quarterly or After Data Classification Policy Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Data Classification assessment | ISMS Implementation Team |

---

# Technical Specification
**Audience:** Python Developers, Excel Workbook Developers, Quality Assurance, ISMS Implementation Team

---

# Workbook Structure Overview

## Sheet List

**Total Sheets:** 11

| # | Sheet Name | Rows (approx) | Purpose | User Input |
|---|------------|---------------|---------|------------|
| 1 | Instructions_Legend | 45 | User guidance, metadata, legend | Metadata only (yellow cells) |
| 2 | Classification_Schema | 15 | Classification levels and definitions | Yes (classification details) |
| 3 | Sensitive_Data_Inventory | 25 | Sensitive data catalog | Yes (data categories) |
| 4 | Data_Location_Mapping | 25 | Data location and flow mapping | Yes (location details) |
| 5 | Data_Owner_Assignment | 20 | Data ownership accountability | Yes (owner assignments) |
| 6 | Regulatory_Mapping | 25 | Regulatory requirements mapping | Yes (regulatory alignment) |
| 7 | Labeling_Methods | 20 | Data labeling implementation status | Yes (labeling metrics) |
| 8 | Discovery_Results | 30 | Data discovery scan results | Yes (discovery findings) |
| 9 | Gap_Analysis | 40 | Gaps and remediation plans | Yes (gap details) |
| 10 | Evidence_Register | 100 | Evidence tracking | Yes (evidence entries) |
| 11 | Summary_Dashboard | 30 | KPIs, compliance metrics | No (automated formulas) |

**Total Assessment Items:** ~75 data classification checkpoints

---

# Detailed Sheet Specifications

## Sheet: Instructions_Legend

**Purpose:** User guidance, assessment metadata, response value legend

**Layout:**

- Rows 1-5: Document header (workbook title, ID, version)
- Rows 7-12: Organization metadata (yellow input cells)
- Rows 14-25: How to use this workbook (instructions)
- Rows 27-35: Legend - Response values
- Rows 37-45: Color coding guide

**Organization Metadata Fields:**

| Row | Field | Type | Example |
|-----|-------|------|---------|
| 7 | Assessment Date | Date | 21.01.2026 |
| 8 | Completed By | Text | John Smith |
| 9 | Role | Text | Data Classification Officer |
| 10 | Organization Name | Text | [Organization] |
| 11 | Review Cycle | Text | Quarterly |
| 12 | Next Review Date | Date | 21.04.2026 |

**Cell Formatting:**

- Organization metadata (B7:B12): Yellow fill, unlocked for user input
- All other cells: Locked, gray or white fill

**No Data Validation:** Informational sheet only

---

## Sheet: Classification_Scheme

**Purpose:** Document data classification scheme levels and governance

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Classification Level | Text | 18 | None | User input (e.g., "Restricted") |
| B | Definition | Text (wrap) | 40 | None | Brief description |
| C | Data Examples | Text (wrap) | 35 | None | Specific examples |
| D | Handling Requirements | Text (wrap) | 35 | None | Security controls |
| E | DLP Protection Requirement | Text | 20 | None | From ISMS-POL-A.8.12 |
| F | Data Owner Assigned | Dropdown | 15 | Yes/No/N/A | Yes if named owner |
| G | Owner Name/Role | Text | 25 | None | Specific person/role |
| H | User Training Completed | Text | 22 | None | E.g., "85% completion" |
| I | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance status |
| J | Evidence ID | Text | 15 | None | E.g., A812-2-CLS-001 |

**Pre-Populated Examples (Gray rows 6-9):**

| Level | Definition | Examples |
|-------|------------|----------|
| Restricted | Severe impact if leaked | Credit card numbers, medical records, trade secrets |
| Confidential | Significant business harm | Customer contracts, pricing, financial reports |
| Internal | Organization-only | Policies, procedures, internal communications |
| Public | Can be publicly disclosed | Marketing materials, public website content |

**Data Rows:** 15 total (4 examples + 11 blank)

**Data Validation:**

```python
# Column F: Data Owner Assigned
validation_owner = {
    'type': 'list',
    'formula1': '"Yes,No,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column I: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}
```

**Conditional Formatting:**

| Column | Condition | Format |
|--------|-----------|--------|
| I (Status) | ="✅ Compliant" | Green fill (RGB: 198, 239, 206) |
| I (Status) | ="⚠️ Partial" | Yellow fill (RGB: 255, 235, 156) |
| I (Status) | ="❌ Non-Compliant" | Red fill (RGB: 255, 199, 206) |

---

## Sheet: Sensitive_Data_Inventory

**Purpose:** Catalog all sensitive data types requiring DLP protection

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Data Category | Dropdown | 25 | Pre-defined list | PII, Financial, IP, etc. |
| B | Data Examples | Text (wrap) | 35 | None | Specific data elements |
| C | Systems/Locations | Text (wrap) | 30 | None | Where data resides |
| D | Classification Level | Dropdown | 18 | From sheet 2 | Restricted/Confidential/etc. |
| E | Volume (approx) | Text | 18 | None | "100K records", "50TB" |
| F | Regulatory Driver | Text | 25 | None | Swiss nDSG, GDPR, PCI DSS |
| G | DLP Coverage | Dropdown | 15 | Yes/No/Partial/N/A | Is DLP protecting? |
| H | Data Discovery Method | Dropdown | 22 | Pre-defined list | How identified |
| I | Data Owner | Text | 25 | None | Business owner |
| J | Last Reviewed Date | Date | 18 | None | DD.MM.YYYY |
| K | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance status |
| L | Evidence ID | Text | 15 | None | A812-2-INV-001 |

**Pre-Populated Examples (Gray rows 6-12):**

| Category | Examples | Systems | Classification |
|----------|----------|---------|----------------|
| Personal Data (PII) | SSN, passport, driver's license, email | HR database, SharePoint, Email | Restricted |
| Financial Data | Credit cards, bank accounts, payment data | Finance database, Payment gateway | Restricted |
| Healthcare Data | Medical records, health information | (If applicable) | Restricted |
| Authentication Credentials | Passwords, API keys, tokens, certificates | All systems | Restricted |
| Intellectual Property | Source code, designs, patents, trade secrets | Git repos, Engineering file shares | Confidential |
| Customer Data | Customer lists, contracts, pricing | Salesforce, CRM, Contract DB | Confidential |
| Employee Data | HR records, payroll, performance reviews | HR systems, Payroll | Confidential |

**Data Rows:** 25 total (7 examples + 18 blank)

**Data Validation:**

```python
# Column A: Data Category
validation_category = {
    'type': 'list',
    'formula1': '"Personal Data (PII),Financial Data,Healthcare Data,Authentication Credentials,Intellectual Property,Customer Data,Employee Data,Other"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column D: Classification Level
# Dynamic reference to Classification_Scheme sheet
validation_classification = {
    'type': 'list',
    'formula1': '=Classification_Scheme!$A$6:$A$15',  # Reference classification levels
    'allow_blank': False,
    'show_dropdown': True
}

# Column G: DLP Coverage
validation_coverage = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,Planned,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column H: Data Discovery Method
validation_discovery = {
    'type': 'list',
    'formula1': '"Automated Scan,Manual Inventory,Application Documentation,Data Owner Interview,None"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column K: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}
```

**Conditional Formatting:**

- Column K (Status): Same as Classification_Scheme (green/yellow/red)
- Column G (DLP Coverage):
  - "Yes" = Light green background
  - "No" = Light red background
  - "Partial" = Light yellow background

---

## Sheet: Detection_Methods

**Purpose:** Assess DLP detection method implementation and effectiveness

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Detection Method | Text | 25 | None | Pre-populated |
| B | Implementation Status | Dropdown | 20 | Deployed/Partial/Not Deployed | Current state |
| C | Capabilities | Text (wrap) | 35 | None | What it can do |
| D | Accuracy (%) | Number | 12 | 0-100 | If tested |
| E | False Positive Rate (%) | Number | 18 | 0-100 | FP / Total × 100 |
| F | False Negative Rate (%) | Number | 18 | 0-100 | FN / Total × 100 |
| G | Last Tested Date | Date | 18 | None | DD.MM.YYYY |
| H | Testing Methodology | Text (wrap) | 30 | None | How accuracy measured |
| I | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance status |
| J | Evidence ID | Text | 15 | None | A812-2-DET-001 |

**Pre-Populated Detection Methods (Rows 6-10):**

| Method | Description | Target Accuracy |
|--------|-------------|-----------------|
| Content Inspection | Pattern matching, regex, keyword detection | >90% |
| Document Labeling | Classification metadata embedded in files | >95% |
| Contextual Analysis | Source system, user role, destination | >85% |
| Machine Learning/AI | AI-based sensitive content detection | >90% |
| Fingerprinting | Hash-based document tracking | 100% (exact match) |

**Data Rows:** 20 total (5 pre-populated + 15 blank)

**Data Validation:**

```python
# Column B: Implementation Status
validation_implementation = {
    'type': 'list',
    'formula1': '"Fully Deployed,Partially Deployed,Not Deployed,Planned"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column D, E, F: Percentage validation
validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between'
}

# Column I: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}
```

**Conditional Formatting:**

- Column D (Accuracy):
  - ≥90% = Green
  - 75-89% = Yellow
  - <75% = Red
- Column E (False Positive Rate):
  - ≤10% = Green
  - 11-30% = Yellow
  - >30% = Red
- Column F (False Negative Rate):
  - ≤5% = Green
  - 6-15% = Yellow
  - >15% = Red

---

## Sheet: Classification_Enforcement

**Purpose:** Assess document labeling and automated classification implementation

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | System/Application | Text | 25 | None | SharePoint, Google Drive, etc. |
| B | Labeling Method | Dropdown | 22 | Manual/Automated/Hybrid | How labels applied |
| C | Labeling Coverage (%) | Number | 18 | 0-100 | % of docs with labels |
| D | Enforcement | Dropdown | 20 | Required/Optional/None | Label before save? |
| E | Auto-Classification Enabled | Dropdown | 22 | Yes/No/Partial | ML-based auto-classify |
| F | Auto-Classification Accuracy (%) | Number | 25 | 0-100 | If tested |
| G | User Override Allowed | Dropdown | 18 | Yes/No | Can users change label? |
| H | Integration with DLP | Dropdown | 18 | Yes/No/Partial | DLP reads labels |
| I | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance status |
| J | Evidence ID | Text | 15 | None | A812-2-ENF-001 |

**Pre-Populated Examples (Gray rows 6-9):**

| System | Method | Coverage | Enforcement |
|--------|--------|----------|-------------|
| SharePoint Online | Automated (Purview) | 85% | Required |
| Google Drive | Manual | 30% | Optional |
| Local File Shares | None | 0% | None |
| Email (M365) | Automated | 95% | Recommended |

**Data Rows:** 18 total (4 examples + 14 blank)

**Data Validation:**

```python
# Column B: Labeling Method
validation_method = {
    'type': 'list',
    'formula1': '"Manual,Automated,Hybrid,None"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column C, F: Percentage
validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between'
}

# Column D: Enforcement
validation_enforcement = {
    'type': 'list',
    'formula1': '"Required,Recommended,Optional,None"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column E, G, H: Yes/No/Partial
validation_yesnop = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column I: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}
```

**Conditional Formatting:**

- Column C (Labeling Coverage):
  - ≥80% = Green
  - 50-79% = Yellow
  - <50% = Red
- Column F (Auto-Classification Accuracy):
  - ≥85% = Green
  - 70-84% = Yellow
  - <70% = Red

---

## Sheet: Pattern_Library

**Purpose:** Document DLP patterns and their accuracy

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Pattern ID | Text | 15 | None | Unique identifier |
| B | Pattern Name | Text | 25 | None | Descriptive name |
| C | Data Type | Dropdown | 20 | Pre-defined list | What it detects |
| D | Pattern Definition | Text (wrap) | 40 | None | Regex or description |
| E | Detection Method | Dropdown | 20 | Regex/Keyword/ML/Fingerprint | How it works |
| F | Confidence Level | Dropdown | 18 | High/Medium/Low | Accuracy confidence |
| G | Accuracy (%) | Number | 12 | 0-100 | Tested accuracy |
| H | False Positive Rate (%) | Number | 18 | 0-100 | FP rate |
| I | Last Tested Date | Date | 18 | None | DD.MM.YYYY |
| J | Maintenance Owner | Text | 22 | None | Who maintains |
| K | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Pattern effectiveness |
| L | Evidence ID | Text | 15 | None | A812-2-PAT-001 |

**Pre-Populated Pattern Examples (Gray rows 6-15):**

| Pattern ID | Name | Data Type | Definition (simplified) |
|------------|------|-----------|-------------------------|
| PAT-001 | Credit Card (Luhn) | Financial | Regex with Luhn algorithm validation |
| PAT-002 | US SSN | PII | `\d{3}-\d{2}-\d{4}` or `\d{9}` |
| PAT-003 | IBAN | Financial | Country code + check digits + account |
| PAT-004 | Email Address | PII | Standard email regex |
| PAT-005 | API Key (AWS) | Credentials | `AKIA[0-9A-Z]{16}` |
| PAT-006 | Password Pattern | Credentials | Common password structures |
| PAT-007 | Swiss AHV Number | PII | `756.\d{4}.\d{4}.\d{2}` |
| PAT-008 | EU Passport | PII | Country-specific formats |
| PAT-009 | Medical Record Number | Healthcare | Site-specific format |
| PAT-010 | Source Code Fingerprint | IP | Hash of critical files |

**Data Rows:** 30 total (10 examples + 20 blank)

**Data Validation:**

```python
# Column C: Data Type
validation_datatype = {
    'type': 'list',
    'formula1': '"PII,Financial,Healthcare,Credentials,IP,Customer Data,Employee Data,Other"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column E: Detection Method
validation_detection = {
    'type': 'list',
    'formula1': '"Regex,Keyword,Machine Learning,Fingerprint,Hybrid"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column F: Confidence Level
validation_confidence = {
    'type': 'list',
    'formula1': '"High (>90%),Medium (75-90%),Low (<75%)"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column G, H: Percentage
validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between'
}

# Column K: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}
```

**Conditional Formatting:**

- Column G (Accuracy):
  - ≥90% = Green
  - 75-89% = Yellow
  - <75% = Red
- Column H (False Positive Rate):
  - ≤10% = Green
  - 11-30% = Yellow
  - >30% = Red
- Column F (Confidence Level):
  - "High" = Green
  - "Medium" = Yellow
  - "Low" = Red

---

## Sheet: Gap_Analysis

**Purpose:** Document identified gaps and remediation plans

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Gap ID | Text | 12 | Auto-generated: GAP-001 |
| B | Domain | Dropdown | 22 | Which assessment area |
| C | Gap Description | Text (wrap) | 40 | What's missing/inadequate |
| D | Current State | Text (wrap) | 25 | Current situation |
| E | Required State | Text (wrap) | 25 | What's needed |
| F | Risk Level | Dropdown | 15 | Critical/High/Medium/Low |
| G | Regulatory Impact | Text (wrap) | 25 | Which regulations affected |
| H | Remediation Action | Text (wrap) | 35 | What to do |
| I | Owner | Text | 20 | Who will fix |
| J | Target Date | Date | 15 | When to complete |
| K | Status | Dropdown | 15 | Open/In Progress/Resolved |
| L | Evidence ID | Text | 15 | A812-2-GAP-001 |

**Gap ID Auto-Generation:**
```python
# Formula in column A (starting row 6):
="GAP-"&TEXT(ROW()-5,"000")
# Results in: GAP-001, GAP-002, etc.
```

**Data Rows:** 40 (all blank, populated during assessment)

**Data Validation:**

```python
# Column B: Domain
validation_domain = {
    'type': 'list',
    'formula1': '"Classification Scheme,Sensitive Data Inventory,Detection Methods,Classification Enforcement,Pattern Library,General"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column F: Risk Level
validation_risk = {
    'type': 'list',
    'formula1': '"Critical,High,Medium,Low"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column K: Status
validation_status = {
    'type': 'list',
    'formula1': '"Open,In Progress,Resolved,Accepted (No Action)"',
    'allow_blank': False,
    'show_dropdown': True
}
```

**Conditional Formatting:**

- Column F (Risk Level):
  - "Critical" = Dark red fill
  - "High" = Red fill
  - "Medium" = Yellow fill
  - "Low" = Light yellow fill
- Column K (Status):
  - "Resolved" = Green fill
  - "In Progress" = Yellow fill
  - "Open" = Red fill
  - "Accepted" = Gray fill

---

## Sheet: Evidence_Register

**Purpose:** Track all evidence collected for audit

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Evidence ID | Text | 15 | Auto-generated: EV-001 |
| B | Domain | Dropdown | 20 | Which assessment area |
| C | Evidence Type | Dropdown | 20 | Screenshot/Doc/Test Result |
| D | Description | Text (wrap) | 45 | What evidence shows |
| E | File Name | Text | 35 | Actual filename |
| F | Collection Date | Date | 18 | DD.MM.YYYY |
| G | Collected By | Text | 20 | Person who collected |
| H | File Location | Text (wrap) | 40 | Path or URL |
| I | Sensitivity | Dropdown | 15 | Internal/Confidential |

**Evidence ID Auto-Generation:**
```python
# Formula in column A (starting row 6):
="EV-"&TEXT(ROW()-5,"000")
# Results in: EV-001, EV-002, etc.
```

**Pre-Populated Example (Gray row 6):**
| ID | Domain | Type | Description | File Name |
|----|--------|------|-------------|-----------|
| EV-001 | Classification Scheme | Policy Document | Data classification policy v2.0 with signatures | Classification-Policy-v2.0-Signed.pdf |

**Data Rows:** 100 total (1 example + 99 blank)

**Data Validation:**

```python
# Column B: Domain
validation_domain = {
    'type': 'list',
    'formula1': '"Classification Scheme,Sensitive Data Inventory,Detection Methods,Classification Enforcement,Pattern Library,Gap Analysis,General"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column C: Evidence Type
validation_type = {
    'type': 'list',
    'formula1': '"Screenshot,Configuration Export,Policy Document,Test Result,Data Discovery Report,Training Record,Audit Report,Other"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column I: Sensitivity
validation_sensitivity = {
    'type': 'list',
    'formula1': '"Public,Internal,Confidential"',
    'allow_blank': False,
    'show_dropdown': True
}
```

---

## Sheet: Summary_Dashboard

**Purpose:** Executive summary with KPIs and compliance metrics

**Layout:**

**Rows 1-5: Header**

- Dashboard title, assessment date, organization

**Rows 7-15: Key Metrics (Large display)**

| Metric | Formula | Target |
|--------|---------|--------|
| Overall Compliance % | Weighted average of all domain compliance | ≥80% |
| Classification Scheme Maturity | Based on Classification_Scheme sheet | Level 2-3 |
| Sensitive Data Categories Inventoried | COUNT of categories in Sensitive_Data_Inventory | ≥7 |
| DLP Coverage % | Categories with DLP coverage / Total categories × 100 | 100% for Restricted/Confidential |
| Pattern Accuracy (avg) | AVERAGE of Pattern_Library accuracy column | ≥90% |
| False Positive Rate (avg) | AVERAGE of Detection_Methods FP rate | ≤10% |
| Critical Gaps | COUNT of Critical risk gaps in Gap_Analysis | 0 |
| High Gaps | COUNT of High risk gaps | ≤3 |

**Rows 17-25: Compliance by Domain**

| Domain | Compliance % | Status | Target |
|--------|--------------|--------|--------|
| Classification Scheme | Formula | ✅/⚠️/❌ | 100% |
| Sensitive Data Inventory | Formula | ✅/⚠️/❌ | 100% |
| Detection Methods | Formula | ✅/⚠️/❌ | ≥90% |
| Classification Enforcement | Formula | ✅/⚠️/❌ | ≥80% |
| Pattern Library | Formula | ✅/⚠️/❌ | ≥85% |

**Rows 27-35: Top 5 Critical Gaps (if any)**

- Dynamically pulled from Gap_Analysis sheet (filtered by "Critical" risk level)

**Key Formulas:**

```python
# Overall Compliance %
=ROUND(
  (COUNTIF(Classification_Scheme!I:I,"✅ Compliant") / COUNTA(Classification_Scheme!I6:I15) * 20) +
  (COUNTIF(Sensitive_Data_Inventory!K:K,"✅ Compliant") / COUNTA(Sensitive_Data_Inventory!K6:K25) * 25) +
  (COUNTIF(Detection_Methods!I:I,"✅ Compliant") / COUNTA(Detection_Methods!I6:I20) * 20) +
  (COUNTIF(Classification_Enforcement!I:I,"✅ Compliant") / COUNTA(Classification_Enforcement!I6:I18) * 15) +
  (COUNTIF(Pattern_Library!K:K,"✅ Compliant") / COUNTA(Pattern_Library!K6:K30) * 20),
  0
)

# Sensitive Data Categories Inventoried
=COUNTA(Sensitive_Data_Inventory!A6:A25) - COUNTBLANK(Sensitive_Data_Inventory!A6:A25)

# DLP Coverage %
=ROUND(
  COUNTIF(Sensitive_Data_Inventory!G6:G25,"Yes") / 
  COUNTA(Sensitive_Data_Inventory!G6:G25) * 100,
  0
)

# Pattern Accuracy (average)
=ROUND(AVERAGE(Pattern_Library!G6:G30), 0)

# False Positive Rate (average)
=ROUND(AVERAGE(Detection_Methods!E6:E20), 1)

# Critical Gaps
=COUNTIF(Gap_Analysis!F6:F45,"Critical")

# High Gaps
=COUNTIF(Gap_Analysis!F6:F45,"High")
```

**Conditional Formatting:**

- Overall Compliance %:
  - ≥90% = Dark green
  - 80-89% = Light green
  - 70-79% = Yellow
  - <70% = Red
- Critical Gaps:
  - 0 = Green
  - 1-2 = Yellow
  - ≥3 = Red

---

# Data Validation Rules (Consolidated)

**Standard Dropdown Values:**

```python
# Status (used in multiple sheets)
STATUS_VALUES = "✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"

# Yes/No/Partial
YES_NO_PARTIAL = "Yes,No,Partial,Planned,N/A"

# Risk Level
RISK_LEVEL = "Critical,High,Medium,Low"

# Data Categories
DATA_CATEGORIES = "Personal Data (PII),Financial Data,Healthcare Data,Authentication Credentials,Intellectual Property,Customer Data,Employee Data,Other"

# Detection Methods
DETECTION_METHODS = "Regex,Keyword,Machine Learning,Fingerprint,Hybrid"

# Implementation Status
IMPLEMENTATION_STATUS = "Fully Deployed,Partially Deployed,Not Deployed,Planned"
```

**Percentage Validation (0-100):**
```python
validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between',
    'error_title': 'Invalid Percentage',
    'error_message': 'Please enter a value between 0 and 100'
}
```

**Date Validation (DD.MM.YYYY):**
```python
validation_date = {
    'type': 'date',
    'formula1': '01.01.2020',  # Reasonable past date
    'formula2': '31.12.2030',  # Reasonable future date
    'allow_blank': True,
    'operator': 'between',
    'error_title': 'Invalid Date',
    'error_message': 'Please enter a valid date in DD.MM.YYYY format'
}
```

---

# Conditional Formatting Rules

**Standard Status Formatting:**
```python
status_formatting = {
    '✅ Compliant': {'fill': 'C6EFCE', 'font': '006100'},      # Green
    '⚠️ Partial': {'fill': 'FFEB9C', 'font': '9C6500'},        # Yellow
    '❌ Non-Compliant': {'fill': 'FFC7CE', 'font': '9C0006'},  # Red
    'N/A': {'fill': 'F2F2F2', 'font': '808080'}                # Gray
}
```

**Percentage Thresholds (Accuracy/Coverage):**
```python
# Green: ≥90%, Yellow: 75-89%, Red: <75%
accuracy_high_threshold = {
    'green': ('>=', 90),
    'yellow': ('and', [('>=', 75), ('<', 90)]),
    'red': ('<', 75)
}

# Green: ≥80%, Yellow: 50-79%, Red: <50%
coverage_threshold = {
    'green': ('>=', 80),
    'yellow': ('and', [('>=', 50), ('<', 80)]),
    'red': ('<', 50)
}

# False Positive Rate (Green: ≤10%, Yellow: 11-30%, Red: >30%)
fp_threshold = {
    'green': ('<=', 10),
    'yellow': ('and', [('>', 10), ('<=', 30)]),
    'red': ('>', 30)
}
```

**Risk Level Formatting:**
```python
risk_formatting = {
    'Critical': {'fill': '8B0000', 'font': 'FFFFFF'},  # Dark red, white text
    'High': {'fill': 'FF0000', 'font': 'FFFFFF'},      # Red, white text
    'Medium': {'fill': 'FFEB9C', 'font': '9C6500'},    # Yellow
    'Low': {'fill': 'FFF2CC', 'font': '9C6500'}        # Light yellow
}
```

---

# Cell Protection

**Protected Cells (Formula/Static):**

- All column headers (row 5 in each sheet)
- All formulas (Summary_Dashboard, auto-generated IDs)
- Instructions and legend text
- Pre-populated examples (gray rows)
- Summary_Dashboard calculations

**Unprotected Cells (User Input):**

- All yellow-highlighted fields (organization metadata)
- Data entry rows in assessment sheets (white cells)
- Status dropdown columns
- Additional Details / Comments fields
- Evidence Register descriptions
- Gap Analysis fields

**Sheet Protection Password:**

- Use organization-specific password
- Allow: Format cells, Insert rows, Sort, Filter
- Disallow: Delete rows, Modify formulas, Unprotect sheet

---

# Summary Dashboard Formulas (Detailed)

**Compliance Percentage Calculation (Weighted Average):**

Each domain has a weight based on importance:

- Classification Scheme: 20% (foundation)
- Sensitive Data Inventory: 25% (scope definition)
- Detection Methods: 20% (technical capability)
- Classification Enforcement: 15% (operational)
- Pattern Library: 20% (accuracy)

```python
overall_compliance = (
    (classification_scheme_compliance * 0.20) +
    (data_inventory_compliance * 0.25) +
    (detection_methods_compliance * 0.20) +
    (classification_enforcement_compliance * 0.15) +
    (pattern_library_compliance * 0.20)
)

# Where each domain_compliance =
# COUNTIF(domain_sheet!status_column, "✅ Compliant") / COUNTA(domain_sheet!status_column)
```

**Pattern Accuracy Average:**
```python
=IFERROR(
  ROUND(AVERAGE(Pattern_Library!G6:G30), 0),
  "N/A"
)
```

**DLP Coverage Percentage:**
```python
=IFERROR(
  ROUND(
    COUNTIF(Sensitive_Data_Inventory!G6:G25,"Yes") / 
    (COUNTA(Sensitive_Data_Inventory!G6:G25) - COUNTIF(Sensitive_Data_Inventory!G6:G25,"N/A")) * 100,
    0
  ),
  0
)
```

**Critical Gaps with Conditional Display:**
```python
=IF(COUNTIF(Gap_Analysis!F6:F45,"Critical")=0,
  "✅ No Critical Gaps",
  CONCATENATE("❌ ", COUNTIF(Gap_Analysis!F6:F45,"Critical"), " Critical Gaps - See Gap Analysis")
)
```

---

# Evidence Register Auto-Numbering

**Evidence ID Format:**
```python
# Column A formula (starting row 6):
=IF(ISBLANK(B6), "", "EV-"&TEXT(ROW()-5,"000"))

# Results in:
# EV-001, EV-002, EV-003, etc.
# Only generates ID if Domain column (B) is populated
```

**Date Auto-Fill for Collection Date:**
```python
# Column F formula (if collection date not manually entered):
=IF(AND(NOT(ISBLANK(B6)), ISBLANK(F6)), TODAY(), F6)

# Auto-fills today's date when evidence row created
# User can override with manual date entry
```

---

# APPENDIX: Technical Notes for Python Developers

## A.1 Python Script Integration Points

**Script Name:** `generate_a812_2_data_classification_assessment.py`

**Key Functions:**

```python
def create_workbook():
    """Initialize workbook with 9 sheets"""
    wb = Workbook()
    # Create sheets in order
    sheets = [
        'Instructions_Legend',
        'Classification_Scheme',
        'Sensitive_Data_Inventory',
        'Detection_Methods',
        'Classification_Enforcement',
        'Pattern_Library',
        'Gap_Analysis',
        'Evidence_Register',
        'Summary_Dashboard'
    ]
    return wb

def setup_styles():
    """Define reusable cell styles"""
    styles = {
        'header': {
            'font': Font(bold=True, size=11, color='FFFFFF'),
            'fill': PatternFill(start_color='366092', end_color='366092', fill_type='solid'),
            'alignment': Alignment(horizontal='center', vertical='center', wrap_text=True),
            'border': Border(...)
        },
        'yellow_input': {
            'fill': PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid'),
            'border': Border(...)
        },
        'gray_example': {
            'fill': PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid'),
            'font': Font(italic=True, color='808080')
        }
    }
    return styles

def apply_data_validation(sheet, cell_range, validation_type, formula):
    """Apply dropdown or range validation"""
    dv = DataValidation(...)
    sheet.add_data_validation(dv)
    dv.add(cell_range)

def apply_conditional_formatting(sheet, cell_range, rules):
    """Apply color coding based on values"""
    for rule in rules:
        sheet.conditional_formatting.add(cell_range, rule)

def create_summary_dashboard(wb):
    """Generate Summary_Dashboard with formulas"""
    # Implement weighted compliance calculation
    # Add KPI formulas
    # Link to other sheets
```

## A.2 Customization Guidelines

**For Each Implementation:**

1. **Review Pre-Populated Examples:**

   - Classification levels may differ (adjust Classification_Scheme examples)
   - Sensitive data categories may vary (add organization-specific categories)
   - Pattern library will be unique (replace examples with actual patterns)

2. **Adjust Validation Lists:**

   - Data categories: Add organization-specific categories
   - Systems/Applications: Replace generic examples with actual systems
   - Detection methods: Add any custom detection methods

3. **Tune Thresholds:**

   - Accuracy thresholds (90%, 75%) may need adjustment based on organization maturity
   - False positive targets (<10%) may be aspirational for immature programs
   - Coverage targets (80%, 100%) should align with policy requirements

4. **Customize Formulas:**

   - Weighted compliance calculation may need different weights
   - Summary dashboard KPIs may need additions/removals based on stakeholder needs

## A.3 Quality Assurance

**Validation Script:** `excel_sanity_check_a812_2.py`

```python
def validate_workbook(workbook_path):
    """Comprehensive workbook validation"""
    checks = [
        check_sheet_existence(),
        check_column_headers(),
        check_data_validation(),
        check_conditional_formatting(),
        check_formulas(),
        check_protection(),
        check_examples()
    ]
    return all(checks)

def check_formulas():
    """Verify all formulas calculate correctly"""
    # Open workbook
    # Trigger calculation
    # Check for #REF, #DIV/0, #VALUE errors
    # Verify formula logic matches specification
```

**Testing Checklist:**

- [ ] All 9 sheets created
- [ ] Column headers match specification
- [ ] Data validation dropdowns functional
- [ ] Conditional formatting rules applied
- [ ] Summary Dashboard formulas calculate correctly
- [ ] Evidence Register auto-numbering works
- [ ] Gap Analysis auto-numbering works
- [ ] Sheet protection enabled correctly
- [ ] No #REF or #VALUE errors
- [ ] File saves and reopens without errors

## A.4 Deployment Instructions

**Step 1: Generate Workbook**
```bash
python3 generate_a812_2_data_classification_assessment.py
```

**Expected Output:**
```
ISMS-IMP-A.8.12.2_Data_Classification_Assessment_YYYYMMDD.xlsx
```

**Step 2: Validate Workbook**
```bash
python3 excel_sanity_check_a812_2.py ISMS-IMP-A.8.12.2_Data_Classification_Assessment_20260121.xlsx
```

**Step 3: Manual QA**

- Open workbook in Excel/LibreOffice
- Verify dropdowns work (click, select value)
- Test formulas (enter sample data, verify calculations)
- Check conditional formatting (enter values triggering different colors)
- Verify sheet protection (try to modify locked cells - should fail)

**Step 4: Distribute to Assessment Team**

- Provide workbook + PART I User Completion Guide
- Conduct brief training session (30 min)
- Set completion deadline (typically 2-4 weeks)

**Step 5: Collect Completed Assessments**

- Review for completeness (no blank mandatory fields)
- Validate evidence exists (files referenced in Evidence Register)
- Approve or request corrections

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

**Document Assembly:**

To create complete ISMS-IMP-A.8.12.2 specification:

1. **PART I:** User Completion Guide (separate file)
2. **PART II:** Technical Specification (this file)

**Python Script:** `generate_a812_2_data_classification_assessment.py`  
**Validation Script:** `excel_sanity_check_a812_2.py`  
**Output:** `ISMS-IMP-A.8.12.2_Data_Classification_Assessment_YYYYMMDD.xlsx`

**Dependencies:**

- openpyxl library (`pip install openpyxl`)
- Python 3.7+

---

**Status:** Technical Specification Complete  
**Next Action:** Implement Python workbook generator per specification  

---

**END OF SPECIFICATION**

---

*"The important thing is not to stop questioning. Curiosity has its own reason for existing."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
