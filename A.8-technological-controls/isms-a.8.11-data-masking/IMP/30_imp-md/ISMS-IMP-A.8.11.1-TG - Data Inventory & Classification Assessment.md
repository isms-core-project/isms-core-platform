**ISMS-IMP-A.8.11.1-TG - Data Inventory & Classification Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.11: Data Masking


---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.11.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Sensitive Data Inventory & Classification |
| **Related Policy** | ISMS-POL-A.8.11, Section 2.1 (Data Classification and Identification) |
| **Purpose** | Assess organization's ability to identify, inventory, classify, and assign ownership to sensitive data requiring masking controls |
| **Target Audience** | Data Governance Teams, Data Protection Officers, Database Administrators, Application Owners, Compliance Officers, Auditors |
| **Assessment Type** | Data Discovery & Classification |
| **Review Cycle** | Quarterly (Inventory Updates) / Annual (Classification Review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial workbook layout specification only | ISMS Implementation Team |

---

# Technical Specification

---

# Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.11.1 |
| **Version** | 1.0 |
| **Assessment Area** | Sensitive Data Inventory & Classification |
| **Related Policy** | ISMS-POL-A.8.11, Section 2.1 (Data Classification and Identification) |
| **Purpose** | Technical specification for Excel workbook documenting all systems containing sensitive data, data classification, ownership assignment, and masking requirements |
| **Target Audience** | Python Developers, Excel Power Users, ISMS Implementation Teams, Technical Auditors |
| **Specification Type** | Technical Implementation Blueprint |
| **Review Cycle** | Annual or When Python Generator Scripts Updated |
| **Date** | [Date] |

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial Excel workbook specification | ISMS Implementation Team |

---

# Overview

## Purpose of This Specification

This document provides the **complete technical blueprint** for generating the ISMS-IMP-A.8.11.1 Data Inventory & Classification Assessment Excel workbook using Python (openpyxl).

**What This Specification Defines:**

- Exact Excel workbook structure (11 sheets)
- Column headers, widths, data types, validation rules
- Cell formatting, conditional formatting, protection rules
- Formula specifications with cell references
- Data validation dropdown lists
- Styling standards (colors, fonts, borders)
- Python script integration requirements
- Quality assurance validation criteria

**Target Audience:**

- Python developers implementing the generator script
- Excel power users creating manual workbooks
- Quality assurance teams validating workbook structure
- Technical auditors verifying implementation accuracy

## Workbook Generation Approach

**Automated Generation (Recommended):**
```bash
python3 generate_a811_1_data_inventory.py
# Output: ISMS-IMP-A.8.11.1_Data_Inventory_Classification_20260119.xlsx
```

**Manual Creation (Not Recommended):**

- Create workbook structure manually following this specification
- Error-prone, time-consuming, difficult to maintain
- Use only if Python environment unavailable

## Key Design Principles

**Data-Centric, Not Tool-Centric:**

- Focus on WHAT data exists, WHERE it resides, WHO owns it
- Tool/product-agnostic (works with any masking solution or custom scripts)
- Platform-agnostic (cloud, on-premises, hybrid, SaaS)

**Evidence-Based Assessment:**

- Every classification requires justification
- Every ownership assignment requires approval
- Every masking requirement traced to data sensitivity
- Audit trail maintained throughout

**Scalability:**

- 50-row templates per sheet (expandable to 1,000+ with minimal modification)
- Supports organizations with 5 systems or 500 systems
- Formula references use dynamic ranges where possible

---

# Workbook Structure Overview

## Sheet Summary

| Sheet # | Sheet Name | Primary Purpose | Row Count | User Input Cells |
|---------|------------|-----------------|-----------|------------------|
| 1 | **Instructions_Legend** | User guide, taxonomy reference | ~100 | 5 (metadata) |
| 2 | **System_Inventory** | Master list of all systems/databases | ~70 | 50 data rows |
| 3 | **Data_Category_Reference** | Data category taxonomy definitions | ~40 | 0 (reference only) |
| 4 | **Sensitive_Data_Inventory** | Field-level sensitive data catalog | ~70 | 100 data rows |
| 5 | **Classification_Matrix** | Data sensitivity classification | ~70 | 100 data rows |
| 6 | **Regulatory_Mapping** | Map data to regulatory requirements | ~60 | 50 data rows |
| 7 | **Data_Owner_Assignment** | Assign ownership per data category | ~50 | 30 data rows |
| 8 | **Masking_Priority_Matrix** | Prioritize masking implementation | ~70 | 50 data rows |
| 9 | **Gap_Analysis** | Document classification/ownership gaps | ~50 | 30 data rows |
| 10 | **Evidence_Register** | Track compliance evidence | ~60 | 40 data rows |
| 11 | **Summary_Dashboard** | Executive compliance summary | ~80 | 10 (sign-off) |

**Total Sheets:** 11  
**Total Template Capacity:** ~500 assessment data points

---

# Sheet 1: Instructions_Legend

## Purpose
Provide user guidance, taxonomy reference, status legends, and acceptable evidence examples.

## Sheet Structure

**Row Layout:**

- Rows 1-2: Document header (title, subtitle)
- Rows 3-10: Document metadata (Document ID, Version, Date, etc.)
- Rows 11-25: How to Use This Workbook (numbered steps)
- Rows 26-40: Data Category Taxonomy (reference table)
- Rows 41-50: Sensitivity Classification Levels (reference table)
- Rows 51-60: Status Legend (symbol definitions)
- Rows 61-80: Acceptable Evidence Examples (bulleted list)

## Header Section (Rows 1-2)

**Row 1: Main Title**

- **Cell A1:** "ISMS-IMP-A.8.11.1 – Data Inventory & Classification Assessment"
- **Merge:** A1:Q1
- **Font:** Calibri 16pt Bold, White
- **Fill:** RGB(0, 51, 102) - Dark Blue (#003366)
- **Alignment:** Center, Vertical Center
- **Row Height:** 40px

**Row 2: Subtitle**

- **Cell A2:** "ISO/IEC 27001:2022 - Control A.8.11: Data Masking"
- **Merge:** A2:Q2
- **Font:** Calibri 12pt Regular, White
- **Fill:** RGB(68, 114, 196) - Medium Blue (#4472C4)
- **Alignment:** Center, Vertical Center
- **Row Height:** 25px

## Document Metadata (Rows 4-10)

**Table Format:**
| Row | Column A (Label) | Column B-C (Value) | Styling |
|-----|------------------|-------------------|---------|
| 4 | Document ID: | ISMS-IMP-A.8.11.1 | Label: Bold, Value: Normal |
| 5 | Assessment Area: | Data Inventory & Classification | |
| 6 | Related Policy: | ISMS-POL-A.8.11, Section 2.1 (Data Classification and Identification) | |
| 7 | Version: | 2.0 | |
| 8 | Assessment Date: | [USER INPUT] | Yellow fill (RGB 255,255,204) |
| 9 | Completed By: | [USER INPUT] | Yellow fill |
| 10 | Organization: | [USER INPUT] | Yellow fill |
| 11 | Review Cycle: | Quarterly (Inventory) / Annual (Classification Review) | |

**Cell Details:**

- **Column A Width:** 20
- **Column B-C Width:** 40 (merged)
- **Font:** Calibri 10pt
- **Border:** Thin border around each cell

## How to Use This Workbook (Rows 13-25)

**Row 13: Section Header**

- **Cell A13:** "How to Use This Workbook"
- **Merge:** A13:Q13
- **Font:** Calibri 12pt Bold
- **Fill:** RGB(217, 217, 217) - Light Gray (#D9D9D9)
- **Alignment:** Left

**Rows 14-25: Numbered Instructions**
```
1. Start with System_Inventory – list ALL systems/databases that process data
2. Use Data_Category_Reference to understand sensitivity taxonomy
3. Complete Sensitive_Data_Inventory for each system (table/field level)
4. Apply classification using the Classification_Matrix sheet
5. Map data to regulatory requirements in Regulatory_Mapping
6. Assign data owners in Data_Owner_Assignment
7. Prioritize masking efforts in Masking_Priority_Matrix
8. Document gaps in Gap_Analysis
9. Maintain evidence in Evidence_Register
10. Review summary metrics in Summary_Dashboard
11. Obtain required approvals
12. Archive completed workbook with assessment date in filename
```

**Format:**

- **Cell Range:** A14:Q25
- **Font:** Calibri 10pt
- **Wrap Text:** Enabled
- **Indentation:** 1 level for sub-bullets

## Data Category Taxonomy (Rows 27-40)

**Row 27: Section Header**

- **Cell A27:** "Data Category Taxonomy (Quick Reference)"
- **Merge:** A27:E27
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray

**Rows 28-40: Taxonomy Table**

| Row | Cat ID | Category Name | Examples | Regulatory Scope |
|-----|--------|--------------|----------|------------------|
| 29 | CAT-PII-D | Direct PII | Name, SSN/AHV, Passport, Email, Phone | GDPR, FADP, CCPA |
| 30 | CAT-PII-I | Indirect PII | DOB+ZIP, Job Title+Department | GDPR, FADP |
| 31 | CAT-FIN | Financial Data | Credit Card (PAN), IBAN, Account Balance | PCI-DSS, FADP |
| 32 | CAT-HLT | Health Data | Diagnoses, Prescriptions, Medical Records | HIPAA, GDPR Art.9 |
| 33 | CAT-CRD | Credentials | Passwords, API Keys, Tokens, Private Keys | ISO 27001 A.9 |
| 34 | CAT-PRP | Proprietary Data | Trade Secrets, Pricing Models, IP | Contract, NDA |
| 35 | CAT-LOC | Location Data | GPS Coordinates, IP Address, Travel History | GDPR, CCPA |
| 36 | CAT-BIO | Biometric Data | Fingerprints, Facial Geometry, Voice Print | GDPR Art.9, BIPA |
| 37 | CAT-GEN | Genetic Data | DNA Sequences, Genetic Test Results | GDPR Art.9, GINA |
| 38 | CAT-CHD | Child Data | Data of minors (<16 GDPR / <18 COPPA) | GDPR, COPPA |
| 39 | CAT-LEG | Legal Data | Contracts, Legal Opinions, Litigation Records | Attorney-Client |
| 40 | CAT-ETH | Ethnicity/Race | Ethnic Origin, Religious Beliefs, Political Views | GDPR Art.9 |

**Column Specifications:**

- **Column A (Cat ID):** Width 12, Font Bold
- **Column B (Category Name):** Width 20
- **Column C (Examples):** Width 40, Wrap Text
- **Column D (Regulatory Scope):** Width 20, Wrap Text

## Sensitivity Classification Levels (Rows 42-50)

**Row 42: Section Header**

- **Cell A42:** "Sensitivity Classification Levels"
- **Merge:** A42:D42

**Rows 43-50: Classification Table**

| Row | Level | Definition | Masking Requirement | Breach Impact |
|-----|-------|------------|---------------------|---------------|
| 44 | **Critical** | Severe harm if exposed, regulatory breach guaranteed | SHALL mask in ALL non-production | Legal action, fines, reputational damage |
| 45 | **High** | Substantial harm, privacy violation, regulatory risk | SHALL mask in non-production | Regulatory investigation, customer loss |
| 46 | **Medium** | Moderate harm, business impact, competitive risk | SHOULD mask in non-production | Business disruption, competitive disadvantage |
| 47 | **Low** | Minimal harm, internal use only | MAY mask based on risk assessment | Minor operational impact |
| 48 | **Public** | No confidentiality requirement | N/A | No impact (publicly available) |

**Conditional Formatting:**

- **Critical row:** Red fill (RGB 255, 199, 206)
- **High row:** Orange fill (RGB 255, 235, 156)
- **Medium row:** Yellow fill (RGB 255, 242, 204)
- **Low row:** Light green (RGB 226, 239, 218)
- **Public row:** White (no fill)

## Status Legend (Rows 52-60)

**Row 52: Section Header**

- **Cell A52:** "Status Legend"
- **Merge:** A52:D52

**Rows 53-60: Status Symbols**

| Symbol | Status | Description | Color Code (RGB) |
|--------|--------|-------------|------------------|
| ✅ | Complete | Inventory complete, classified, owner assigned | 198, 239, 206 (Green) |
| ⚠️ | Partial | Partial inventory/classification in progress | 255, 235, 156 (Yellow) |
| ❌ | Missing | Not inventoried or classified | 255, 199, 206 (Red) |
| 📋 | Planned | Discovery/classification scheduled | 180, 199, 231 (Blue) |
| N/A | Not Applicable | System contains no sensitive data | 217, 217, 217 (Gray) |

## Acceptable Evidence (Rows 62-80)

**Row 62: Section Header**

- **Cell A62:** "Acceptable Evidence Examples"
- **Merge:** A62:D62

**Rows 63-80: Bulleted List**
```
✓ Database schema documentation (ERD diagrams, data dictionaries)
✓ Data discovery tool reports (BigID, Varonis, OneTrust, etc.)
✓ Data flow diagrams showing data movement across systems
✓ Data Processing Impact Assessments (DPIA) per GDPR
✓ System design documents with data element definitions
✓ Privacy policy documentation
✓ Data retention schedules
✓ Data owner assignment matrices (RACI charts)
✓ Classification review meeting minutes
✓ Regulatory compliance gap assessments
✓ Third-party data sharing agreements (DPAs)
✓ Screenshots of actual data samples (redacted/masked)
✓ SQL query results showing data structure
✓ API documentation showing data payloads
✓ Application configuration files (anonymized)
✓ Change management records for schema changes
✓ Data lineage documentation
✓ Metadata repository exports
```

**Format:**

- **Cell Range:** A63:D80
- **Font:** Calibri 10pt
- **Bullet Character:** ✓
- **Line Spacing:** 1.2

---

# Sheet 2: System_Inventory

## Purpose
Document all systems, applications, databases, and data repositories. Master list of WHERE sensitive data resides.

## Header Section (Rows 1-5)

**Row 1: Sheet Title**

- **Cell A1:** "SYSTEM & DATABASE INVENTORY"
- **Merge:** A1:Q1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "List ALL systems that process, store, or transmit data (50 row template, expandable)"
- **Merge:** A2:Q2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4)
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Does [Organization] maintain a comprehensive inventory of all systems containing sensitive data?"
- **Merge:** A3:M3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)
- **Border:** Thick border

**Row 4: Response**

- **Cell N4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** N4:Q4
- **Fill:** Light Yellow (#FFFFCC)
- **Data Validation:** List = "Yes,No,Partial,Planned,N/A"

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | System ID | 15 | Text | Free text (SYS-001, SYS-002, etc.) |
| B | System Name | 25 | Text | Free text |
| C | System Type | 18 | Dropdown | Database, Application, SaaS, File Share, API, Data Warehouse, Backup System, Archive, Other |
| D | Environment | 15 | Dropdown | Production, Development, Test/QA, UAT, Training, Analytics, DR/Backup, Decommissioned |
| E | Contains Sensitive Data? | 18 | Dropdown | Yes, No, Unknown |
| F | Data Categories Present | 25 | Text | Free text (comma-separated CAT-IDs) |
| G | Hosting Location | 20 | Dropdown | On-Premises, AWS, Azure, GCP, Multi-Cloud, Hybrid, Third-Party Hosted, Unknown |
| H | Primary Data Owner | 20 | Text | Free text (role or name) |
| I | System Owner/Admin | 20 | Text | Free text |
| J | Inventory Status | 18 | Dropdown | ✅ Complete, ⚠️ Partial, ❌ Missing, 📋 Planned, N/A |
| K | Last Inventory Date | 15 | Date | Date picker (DD.MM.YYYY) |
| L | Next Review Date | 15 | Date | Date picker (auto-calculate: Last Date + 90 days) |
| M | Record Count (Approx) | 15 | Number | Whole numbers only, allow commas |
| N | Retention Period | 15 | Text | Free text ("7 years", "Indefinite", etc.) |
| O | Regulatory Scope | 20 | Text | Free text (GDPR, FADP, HIPAA, etc.) |
| P | Decommission Date | 15 | Date | Date picker (optional) |
| Q | Notes/Comments | 30 | Text | Free text, wrap text enabled |

**Header Row Formatting:**

- **Row Height:** 30px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7 (keep headers visible when scrolling)

## Example Row (Row 7)

**Purpose:** Show users a sample entry with realistic data

| Col | Value |
|-----|-------|
| A | SYS-001 |
| B | Customer Database |
| C | Database |
| D | Production |
| E | Yes |
| F | CAT-PII-D, CAT-FIN |
| G | On-Premises |
| H | Chief Data Officer |
| I | Database Admin Team |
| J | ✅ Complete |
| K | 15.01.2026 |
| L | 15.04.2026 |
| M | 1,250,000 |
| N | 7 years |
| O | GDPR, FADP |
| P | [blank] |
| Q | Primary CRM database, contains customer orders and payment info |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic
- **Border:** Thin borders
- **Note:** Add cell comment to Row 7: "This is an example row. Delete or replace with actual data."

## Data Entry Rows (Rows 8-57)

**50 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC) for all cells
- **Font:** Calibri 10pt Regular
- **Border:** Thin borders
- **Protection:** Unlocked (allow user input)
- **Auto-numbering:** Column A can auto-populate "SYS-{ROW-7}" if desired

**Formula in Column L (Next Review Date):**
```excel
=IF(ISBLANK(K8),"",DATE(YEAR(K8),MONTH(K8)+3,DAY(K8)))
```
Explanation: If Last Inventory Date exists, add 3 months (90 days)

---

## System Inventory Checklist (Rows 59-75)

**Row 59: Section Header**

- **Cell A59:** "SYSTEM INVENTORY CHECKLIST"
- **Merge:** A59:E59
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 60: Table Headers**

| Column | Header | Width |
|--------|--------|-------|
| A | # | 5 |
| B | Checklist Item | 50 |
| C | Status | 15 |
| D | Evidence | 25 |
| E | Notes | 25 |

**Rows 61-75: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is a comprehensive system inventory maintained? | [Dropdown] | [Text] | [Text] |
| 2 | Are all production systems documented? | [Dropdown] | [Text] | [Text] |
| 3 | Are non-production environments included? | [Dropdown] | [Text] | [Text] |
| 4 | Are SaaS/cloud systems included? | [Dropdown] | [Text] | [Text] |
| 5 | Are backup/archive systems included? | [Dropdown] | [Text] | [Text] |
| 6 | Are data warehouses/analytics systems included? | [Dropdown] | [Text] | [Text] |
| 7 | Is system type classified for each entry? | [Dropdown] | [Text] | [Text] |
| 8 | Is hosting location documented? | [Dropdown] | [Text] | [Text] |
| 9 | Are system owners assigned for each system? | [Dropdown] | [Text] | [Text] |
| 10 | Are data owners assigned for each system? | [Dropdown] | [Text] | [Text] |
| 11 | Is inventory reviewed quarterly? | [Dropdown] | [Text] | [Text] |
| 12 | Are decommissioned systems tracked? | [Dropdown] | [Text] | [Text] |
| 13 | Is approximate record count documented? | [Dropdown] | [Text] | [Text] |
| 14 | Is data retention period documented? | [Dropdown] | [Text] | [Text] |
| 15 | Are regulatory requirements mapped per system? | [Dropdown] | [Text] | [Text] |

**Data Validation (Column C - Status):**

- **Formula:** "✅ Complete,⚠️ Partial,❌ Missing,📋 Planned,N/A"
- **Allow Blank:** No
- **Error Message:** "Please select a valid status"

**Conditional Formatting (Column C):**

- ✅ Complete → Green fill (RGB 198, 239, 206)
- ⚠️ Partial → Yellow fill (RGB 255, 235, 156)
- ❌ Missing → Red fill (RGB 255, 199, 206)
- 📋 Planned → Blue fill (RGB 180, 199, 231)
- N/A → Gray fill (RGB 217, 217, 217)

## Reference Table: System Types (Rows 77-85)

**Row 77: Section Header**

- **Cell A77:** "SYSTEM TYPE DEFINITIONS"
- **Merge:** A77:C77
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray

**Rows 78-85: System Type Descriptions**

| System Type | Description | Examples |
|-------------|-------------|----------|
| Database | Relational or NoSQL databases | Oracle, PostgreSQL, MongoDB, SQL Server, MySQL |
| Application | Business applications | CRM, ERP, HR systems, Custom applications |
| SaaS | Cloud-based software services | Salesforce, Workday, ServiceNow, Office 365 |
| File Share | File storage systems | SharePoint, NAS, File servers, S3 buckets |
| API | API gateways and services | REST APIs, SOAP services, Integration platforms |
| Data Warehouse | Analytics and BI systems | Snowflake, Redshift, BigQuery, Tableau Server |
| Backup System | Backup and recovery systems | Veeam, Backup appliances, Cloud backup |
| Archive | Long-term archival storage | Tape libraries, Cold storage, Compliance archives |

**Formatting:**

- **Column Widths:** A=18, B=35, C=40
- **Font:** Calibri 10pt
- **Border:** All borders, thin weight

---

# Sheet 3: Data_Category_Reference

## Purpose
Comprehensive reference taxonomy for data sensitivity categories. **Read-only reference sheet** for users to understand classification scheme.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "DATA CATEGORY REFERENCE TAXONOMY"
- **Merge:** A1:H1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Reference Guide - Use Category IDs when documenting sensitive data (e.g., CAT-PII-D for Direct PII)"
- **Merge:** A2:H2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Warning Note**

- **Cell A3:** "⚠️ This is a REFERENCE sheet. Do not modify. Use these Category IDs in Sensitive_Data_Inventory and Classification_Matrix sheets."
- **Merge:** A3:H3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)
- **Border:** Thick border

## Column Headers (Row 5)

| Col | Header | Width | Description |
|-----|--------|-------|-------------|
| A | Category ID | 12 | Unique identifier (CAT-XXX-X) |
| B | Category Name | 20 | Human-readable name |
| C | Description | 35 | Detailed definition |
| D | Examples | 30 | Concrete field examples |
| E | Default Sensitivity | 15 | Recommended classification level |
| F | Regulatory Scope | 20 | Applicable regulations |
| G | Typical Location | 25 | Common system/table locations |
| H | Masking Priority | 12 | Default priority (P1/P2/P3/P4) |

**Header Row Formatting:**

- **Row Height:** 35px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 6

## Data Rows (Rows 6-30)

**Row 6: CAT-PII-D (Direct PII)**
| Col | Value |
|-----|-------|
| A | CAT-PII-D |
| B | Direct PII (Personally Identifiable Information) |
| C | Data that directly identifies an individual without requiring additional information |
| D | Full name, SSN, AHV number, Passport number, National ID, Email address, Phone number, Employee ID |
| E | High to Critical |
| F | GDPR Art.4(1), FADP Art.5, CCPA, LGPD |
| G | users.name, employees.email, customers.phone, accounts.ssn |
| H | P1 (Critical) |

**Row 7: CAT-PII-I (Indirect PII)**
| Col | Value |
|-----|-------|
| A | CAT-PII-I |
| B | Indirect PII (Quasi-Identifiers) |
| C | Data that can identify an individual when combined with other information |
| D | Date of Birth + ZIP code, Job title + Department, IP address + Timestamp, Device ID + Location |
| E | Medium to High |
| F | GDPR Art.4(1), FADP Art.5 |
| G | users.date_of_birth, employees.department, logs.ip_address |
| H | P2 (High) |

**Row 8: CAT-FIN (Financial Data)**
| Col | Value |
|-----|-------|
| A | CAT-FIN |
| B | Financial Data |
| C | Payment card information, bank account details, transaction data, financial statements |
| D | Credit card PAN, CVV, IBAN, Bank account number, Wire transfer details, Account balance, Salary |
| E | Critical |
| F | PCI-DSS v4.0, GDPR, FADP, GLBA |
| G | payments.card_number, transactions.iban, payroll.salary |
| H | P1 (Critical) |

**Row 9: CAT-HLT (Health Data)**
| Col | Value |
|-----|-------|
| A | CAT-HLT |
| B | Health/Medical Data |
| C | Protected health information (PHI), medical records, diagnoses, treatment information |
| D | Diagnoses (ICD codes), Prescriptions, Lab results, Medical imaging, Patient history, Insurance claims |
| E | Critical |
| F | HIPAA, GDPR Art.9 (Special Category), FADP Art.5(c) |
| G | patient_records.diagnosis, prescriptions.medication, lab_results.values |
| H | P1 (Critical) |

**Row 10: CAT-CRD (Credentials)**
| Col | Value |
|-----|-------|
| A | CAT-CRD |
| B | Authentication Credentials |
| C | Passwords, API keys, tokens, certificates, private keys, secrets |
| D | Password hashes, API keys, OAuth tokens, JWT tokens, SSH private keys, Certificate private keys |
| E | Critical |
| F | ISO 27001 A.9.4.3, NIST SP 800-63B, PCI-DSS Req.8 |
| G | users.password_hash, api_keys.secret, certificates.private_key |
| H | P1 (Critical) |

**Row 11: CAT-PRP (Proprietary Data)**
| Col | Value |
|-----|-------|
| A | CAT-PRP |
| B | Proprietary Business Data |
| C | Trade secrets, intellectual property, pricing models, strategic plans, confidential business information |
| D | Pricing algorithms, Customer lists, Contract terms, Product roadmaps, M&A documents, Source code |
| E | High to Critical |
| F | Trade Secret Law, NDA contracts, UTSA |
| G | pricing.algorithm, contracts.terms, products.roadmap |
| H | P2 (High) |

**Row 12: CAT-LOC (Location Data)**
| Col | Value |
|-----|-------|
| A | CAT-LOC |
| B | Location/Geolocation Data |
| C | Geographic location information that can track or identify individuals' whereabouts |
| D | GPS coordinates, IP addresses, WiFi/BLE beacon data, Cell tower triangulation, Travel history, Home/work addresses |
| E | High |
| F | GDPR Art.4(1), CCPA, ePrivacy Directive |
| G | tracking.gps_lat_long, users.ip_address, devices.location_history |
| H | P2 (High) |

**Row 13: CAT-BIO (Biometric Data)**
| Col | Value |
|-----|-------|
| A | CAT-BIO |
| B | Biometric Data |
| C | Unique physical/behavioral characteristics for authentication or identification |
| D | Fingerprints, Facial geometry, Iris scans, Voice prints, Keystroke dynamics, Gait analysis |
| E | Critical |
| F | GDPR Art.9 (Special Category), BIPA (Illinois), CCPA |
| G | biometric_auth.fingerprint_template, face_recognition.feature_vector |
| H | P1 (Critical) |

**Row 14: CAT-GEN (Genetic Data)**
| Col | Value |
|-----|-------|
| A | CAT-GEN |
| B | Genetic/Genomic Data |
| C | DNA sequences, genetic test results, hereditary disease information |
| D | DNA sequences, Genomic variants, Genetic test results, Family disease history, Pharmacogenomics data |
| E | Critical |
| F | GDPR Art.9 (Special Category), GINA (US), FADP Art.5(c) |
| G | genetic_tests.dna_sequence, health_records.hereditary_conditions |
| H | P1 (Critical) |

**Row 15: CAT-CHD (Child Data)**
| Col | Value |
|-----|-------|
| A | CAT-CHD |
| B | Child/Minor Data |
| C | Personal data of children/minors (age <16 GDPR / <13 COPPA / <18 jurisdiction-specific) |
| D | Any PII of minors: Names, Birthdates, School records, Parental consent records, Online activity |
| E | Critical |
| F | GDPR Art.8, COPPA (US), FADP (enhanced protection) |
| G | students.name, minors.birthdate, parental_consent.records |
| H | P1 (Critical) |

**Row 16: CAT-LEG (Legal Data)**
| Col | Value |
|-----|-------|
| A | CAT-LEG |
| B | Legal/Attorney-Client Data |
| C | Attorney-client privileged communications, legal opinions, litigation materials |
| D | Legal contracts, Court documents, Attorney communications, Settlement agreements, Legal opinions |
| E | High to Critical |
| F | Attorney-Client Privilege, Work Product Doctrine |
| G | legal_docs.contract, litigation.correspondence |
| H | P2 (High) |

**Row 17: CAT-ETH (Ethnicity/Race)**
| Col | Value |
|-----|-------|
| A | CAT-ETH |
| B | Ethnicity/Race/Religion/Politics |
| C | Special category data revealing ethnic origin, religious beliefs, political opinions, sexual orientation |
| D | Ethnic origin, Race, Religious affiliation, Political party membership, Sexual orientation, Trade union membership |
| E | Critical |
| F | GDPR Art.9 (Special Category), FADP Art.5(c) |
| G | surveys.ethnicity, employees.religion, members.political_affiliation |
| H | P1 (Critical) |

**Rows 18-25: Additional Categories (Organization-Specific)**

- **Purpose:** Allow organizations to define custom categories
- **Default:** Leave blank with instruction to add custom categories as needed
- **Format:** Same column structure as above

**Formatting for All Data Rows:**

- **Font:** Calibri 10pt Regular
- **Border:** Thin borders all cells
- **Wrap Text:** Enabled for columns C, D, G
- **Alignment:** Left for text, Center for Column A
- **Protection:** Locked (read-only reference)

## Category Summary Statistics (Rows 27-30)

**Row 27: Summary Header**

- **Cell A27:** "CATEGORY SUMMARY"
- **Merge:** A27:D27
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray

**Row 28-30: Statistics**

| Metric | Formula |
|--------|---------|
| Total Categories Defined | `=COUNTA(A6:A25)` |
| Critical Categories | `=COUNTIF(E6:E25,"Critical")` |
| High Categories | `=COUNTIF(E6:E25,"High")` |

---

# Sheet 4: Sensitive_Data_Inventory

## Purpose
Document **field-level** inventory of sensitive data elements. This is the detailed catalog of WHAT sensitive data exists and WHERE (down to table/column level).

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "SENSITIVE DATA INVENTORY (Field-Level)"
- **Merge:** A1:R1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Document all fields/columns containing sensitive data at table/field level (100 row template)"
- **Merge:** A2:R2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Has [Organization] completed a comprehensive field-level inventory of all sensitive data elements?"
- **Merge:** A3:N3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell O4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** O4:R4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Data Element ID | 15 | Text | Free text (DE-001, DE-002, etc.) |
| B | System ID | 12 | Lookup | Reference System_Inventory!A:A |
| C | System Name | 20 | Lookup | Auto-populate from System_Inventory |
| D | Database/Schema | 18 | Text | Free text (schema name) |
| E | Table Name | 20 | Text | Free text (table name) |
| F | Column/Field Name | 20 | Text | Free text (column name) |
| G | Data Type | 15 | Text | Free text (VARCHAR, INT, DATE, etc.) |
| H | Data Category | 15 | Dropdown | Reference Data_Category_Reference!A:A |
| I | Sample Data (Masked) | 25 | Text | Examples ONLY (no real data) |
| J | Discovery Method | 18 | Dropdown | Manual Review, Data Discovery Tool, Schema Analysis, Application Audit, Other |
| K | Discovery Date | 12 | Date | Date picker |
| L | Populated Rows (Est.) | 15 | Number | Whole numbers |
| M | % Null Values | 10 | Number | 0-100% |
| N | Data Owner | 18 | Text | Reference Data_Owner_Assignment |
| O | Requires Masking? | 15 | Dropdown | Yes, No, Conditional, Under Review |
| P | Masking Status | 15 | Dropdown | ✅ Masked, ⚠️ Partial, ❌ Not Masked, 📋 Planned, N/A |
| Q | Last Verified Date | 12 | Date | Date picker |
| R | Notes | 30 | Text | Free text, wrap text |

**Header Row Formatting:**

- **Row Height:** 35px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | DE-001 |
| B | SYS-001 |
| C | Customer Database |
| D | public |
| E | customers |
| F | credit_card_number |
| G | VARCHAR(19) |
| H | CAT-FIN |
| I | 1234-XXXX-XXXX-5678 (example) |
| J | Data Discovery Tool |
| K | 10.01.2026 |
| L | 1,250,000 |
| M | 2% |
| N | Chief Data Officer |
| O | Yes |
| P | ✅ Masked |
| Q | 15.01.2026 |
| R | PCI-DSS scope. Masked in all non-prod environments using tokenization. |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic
- **Note:** Cell comment on Row 7: "Example row - replace with actual data"

## Data Entry Rows (Rows 8-107)

**100 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Border:** Thin borders
- **Protection:** Unlocked (user input enabled)

**Dependent Formulas:**

**Column C (System Name) - Auto-populate from System_Inventory:**
```excel
=IFERROR(VLOOKUP(B8,System_Inventory!$A:$B,2,FALSE),"")
```
Explanation: Lookup System ID from column B, return System Name from System_Inventory sheet

**Column M (% Null Values) - Validation:**
```excel
Data Validation: Whole number between 0 and 100
Error Alert: "Enter percentage between 0-100"
```

**Conditional Formatting (Column P - Masking Status):**

- ✅ Masked → Green fill (RGB 198, 239, 206)
- ⚠️ Partial → Yellow fill (RGB 255, 235, 156)
- ❌ Not Masked → Red fill (RGB 255, 199, 206)
- 📋 Planned → Blue fill (RGB 180, 199, 231)
- N/A → Gray fill (RGB 217, 217, 217)

## Data Inventory Checklist (Rows 109-125)

**Row 109: Section Header**

- **Cell A109:** "SENSITIVE DATA INVENTORY CHECKLIST"
- **Merge:** A109:E109
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Row 110: Table Headers**

| Column | Header | Width |
|--------|--------|-------|
| A | # | 5 |
| B | Checklist Item | 50 |
| C | Status | 15 |
| D | Evidence | 25 |
| E | Notes | 25 |

**Rows 111-125: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is field-level inventory complete for all systems? | [Dropdown] | [Text] | [Text] |
| 2 | Are all sensitive data categories documented? | [Dropdown] | [Text] | [Text] |
| 3 | Is discovery method documented per field? | [Dropdown] | [Text] | [Text] |
| 4 | Are data owners assigned to each sensitive field? | [Dropdown] | [Text] | [Text] |
| 5 | Is approximate row count estimated per field? | [Dropdown] | [Text] | [Text] |
| 6 | Are null value percentages documented? | [Dropdown] | [Text] | [Text] |
| 7 | Is masking requirement defined per field? | [Dropdown] | [Text] | [Text] |
| 8 | Is masking status current (<30 days old)? | [Dropdown] | [Text] | [Text] |
| 9 | Are sample data examples provided (masked)? | [Dropdown] | [Text] | [Text] |
| 10 | Is inventory reviewed quarterly? | [Dropdown] | [Text] | [Text] |
| 11 | Are database schema changes tracked? | [Dropdown] | [Text] | [Text] |
| 12 | Are new sensitive fields flagged immediately? | [Dropdown] | [Text] | [Text] |
| 13 | Is data lineage documented (source → target)? | [Dropdown] | [Text] | [Text] |
| 14 | Are third-party data sources inventoried? | [Dropdown] | [Text] | [Text] |
| 15 | Is inventory synchronized with CMDB? | [Dropdown] | [Text] | [Text] |

**Data Validation (Column C):**

- Same status dropdown as System_Inventory checklist
- Same conditional formatting rules

---

# Sheet 5: Classification_Matrix

## Purpose
Apply sensitivity classification to each data element based on impact assessment. Links data elements to classification levels (Critical/High/Medium/Low/Public).

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "DATA SENSITIVITY CLASSIFICATION MATRIX"
- **Merge:** A1:P1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Classify each sensitive data element based on impact if exposed (100 row template)"
- **Merge:** A2:P2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Has [Organization] completed sensitivity classification for all sensitive data elements?"
- **Merge:** A3:L3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell M4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** M4:P4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Data Element ID | 15 | Lookup | Reference Sensitive_Data_Inventory!A:A |
| B | Field Name | 20 | Auto-populate | From Sensitive_Data_Inventory |
| C | Data Category | 15 | Auto-populate | From Sensitive_Data_Inventory |
| D | Sensitivity Level | 15 | Dropdown | Critical, High, Medium, Low, Public |
| E | Confidentiality Impact | 15 | Dropdown | Severe, Substantial, Moderate, Minimal, None |
| F | Integrity Impact | 15 | Dropdown | Severe, Substantial, Moderate, Minimal, None |
| G | Availability Impact | 15 | Dropdown | Severe, Substantial, Moderate, Minimal, None |
| H | Regulatory Impact | 15 | Dropdown | Legal Breach, Violation, Non-Compliance, Minor, None |
| I | Reputational Impact | 15 | Dropdown | Severe, Substantial, Moderate, Minimal, None |
| J | Financial Impact (€) | 15 | Dropdown | >1M, 100K-1M, 10K-100K, <10K, None |
| K | Classification Rationale | 30 | Text | Explain why this classification |
| L | Classifier Name | 18 | Text | Person who classified |
| M | Classification Date | 12 | Date | Date picker |
| N | Review Date | 12 | Date | Auto-calc: Classification Date + 365 days |
| O | Approved By | 18 | Text | Data Owner or delegate |
| P | Approval Status | 15 | Dropdown | ✅ Approved, ⚠️ Pending, ❌ Rejected, 📋 Under Review |

**Header Row Formatting:**

- **Row Height:** 35px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | DE-001 |
| B | credit_card_number |
| C | CAT-FIN |
| D | Critical |
| E | Severe |
| F | Substantial |
| G | Moderate |
| H | Legal Breach |
| I | Severe |
| J | >1M |
| K | PCI-DSS cardholder data. Exposure would trigger mandatory breach notification and PCI non-compliance fines. |
| L | CISO |
| M | 10.01.2026 |
| N | 10.01.2027 |
| O | Chief Data Officer |
| P | ✅ Approved |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic

## Data Entry Rows (Rows 8-107)

**100 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked

**Auto-populate Formulas:**

**Column B (Field Name):**
```excel
=IFERROR(VLOOKUP(A8,Sensitive_Data_Inventory!$A:$F,6,FALSE),"")
```

**Column C (Data Category):**
```excel
=IFERROR(VLOOKUP(A8,Sensitive_Data_Inventory!$A:$H,8,FALSE),"")
```

**Column N (Review Date) - Auto-calculate:**
```excel
=IF(ISBLANK(M8),"",DATE(YEAR(M8)+1,MONTH(M8),DAY(M8)))
```
Explanation: Annual review (Classification Date + 365 days)

**Conditional Formatting (Column D - Sensitivity Level):**

- Critical → Red fill (RGB 255, 199, 206)
- High → Orange fill (RGB 255, 235, 156)
- Medium → Yellow fill (RGB 255, 242, 204)
- Low → Light green (RGB 226, 239, 218)
- Public → White (no fill)

**Conditional Formatting (Column P - Approval Status):**

- ✅ Approved → Green fill (RGB 198, 239, 206)
- ⚠️ Pending → Yellow fill (RGB 255, 235, 156)
- ❌ Rejected → Red fill (RGB 255, 199, 206)
- 📋 Under Review → Blue fill (RGB 180, 199, 231)

---

## Classification Matrix Checklist (Rows 109-120)

**Row 109: Section Header**

- **Cell A109:** "CLASSIFICATION MATRIX CHECKLIST"
- **Merge:** A109:E109
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Row 110: Table Headers**

| Column | Header | Width |
|--------|--------|-------|
| A | # | 5 |
| B | Checklist Item | 50 |
| C | Status | 15 |
| D | Evidence | 25 |
| E | Notes | 25 |

**Rows 111-120: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is sensitivity level assigned to all data elements? | [Dropdown] | [Text] | [Text] |
| 2 | Is CIA impact (Confidentiality, Integrity, Availability) assessed? | [Dropdown] | [Text] | [Text] |
| 3 | Is regulatory impact documented? | [Dropdown] | [Text] | [Text] |
| 4 | Is classification rationale documented? | [Dropdown] | [Text] | [Text] |
| 5 | Is data owner approval obtained for all classifications? | [Dropdown] | [Text] | [Text] |
| 6 | Are classifications reviewed annually? | [Dropdown] | [Text] | [Text] |
| 7 | Are Critical classifications justified with evidence? | [Dropdown] | [Text] | [Text] |
| 8 | Is classifier name documented per entry? | [Dropdown] | [Text] | [Text] |
| 9 | Are review dates tracked and monitored? | [Dropdown] | [Text] | [Text] |
| 10 | Is classification methodology consistent across all data? | [Dropdown] | [Text] | [Text] |

**Data Validation and Formatting:**

- Same as previous checklists (status dropdown with conditional formatting)

---

# Sheet 6: Regulatory_Mapping

## Purpose
Map sensitive data elements to applicable regulatory requirements (GDPR, FADP, HIPAA, PCI-DSS, etc.). Establishes compliance traceability from data → regulation → control requirement.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "REGULATORY REQUIREMENT MAPPING"
- **Merge:** A1:N1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Map each sensitive data element to applicable regulatory requirements and compliance obligations (50 row template)"
- **Merge:** A2:N2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Has [Organization] completed regulatory mapping for all sensitive data subject to compliance requirements?"
- **Merge:** A3:J3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell K4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** K4:N4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Data Element ID | 15 | Lookup | Reference Sensitive_Data_Inventory!A:A |
| B | Field Name | 20 | Auto-populate | From Sensitive_Data_Inventory |
| C | Data Category | 15 | Auto-populate | From Sensitive_Data_Inventory |
| D | Applicable Regulations | 25 | Dropdown | GDPR, FADP, HIPAA, PCI-DSS, CCPA, LGPD, SOC 2, ISO 27001, Other (multiple select comma-separated) |
| E | Specific Articles/Requirements | 25 | Text | E.g., "GDPR Art.32, FADP Art.8, PCI-DSS Req.3.4" |
| F | Data Subject Rights Apply? | 15 | Dropdown | Yes (GDPR/FADP), Yes (CCPA), Yes (Other), No, N/A |
| G | Breach Notification Required? | 18 | Dropdown | Yes - Mandatory (72h), Yes - Risk-Based, No, N/A |
| H | Cross-Border Transfer Restrictions? | 20 | Dropdown | Yes - EU/EEA Only, Yes - Adequate Country Only, Yes - SCCs Required, No, N/A |
| I | Data Retention Requirement | 18 | Text | E.g., "7 years (tax law)", "Delete on request (GDPR)" |
| J | Masking Legally Required? | 15 | Dropdown | Yes - Production, Yes - Non-Production Only, No (Best Practice), N/A |
| K | Compliance Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, 📋 Under Review, N/A |
| L | Gap Description | 30 | Text | If non-compliant, describe gap |
| M | Compliance Owner | 18 | Text | Role responsible for compliance |
| N | Last Audit Date | 12 | Date | Date picker |

**Header Row Formatting:**

- **Row Height:** 40px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | DE-001 |
| B | credit_card_number |
| C | CAT-FIN |
| D | PCI-DSS, GDPR, FADP |
| E | PCI-DSS v4.0 Req.3.4.1, GDPR Art.32(1)(a), FADP Art.8(2) |
| F | Yes (GDPR/FADP) |
| G | Yes - Mandatory (72h) |
| H | Yes - SCCs Required |
| I | Retain during active account + 7 years (audit) |
| J | Yes - Non-Production Only |
| K | ✅ Compliant |
| L | [blank] |
| M | Data Protection Officer |
| N | 10.01.2026 |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic

## Data Entry Rows (Rows 8-57)

**50 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked

**Auto-populate Formulas:**

**Column B (Field Name):**
```excel
=IFERROR(VLOOKUP(A8,Sensitive_Data_Inventory!$A:$F,6,FALSE),"")
```

**Column C (Data Category):**
```excel
=IFERROR(VLOOKUP(A8,Sensitive_Data_Inventory!$A:$H,8,FALSE),"")
```

**Conditional Formatting (Column K - Compliance Status):**

- ✅ Compliant → Green fill (RGB 198, 239, 206)
- ⚠️ Partial → Yellow fill (RGB 255, 235, 156)
- ❌ Non-Compliant → Red fill (RGB 255, 199, 206)
- 📋 Under Review → Blue fill (RGB 180, 199, 231)
- N/A → Gray fill (RGB 217, 217, 217)

## Regulatory Framework Reference (Rows 59-72)

**Row 59: Section Header**

- **Cell A59:** "REGULATORY FRAMEWORK REFERENCE"
- **Merge:** A59:D59
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray

**Rows 60-72: Framework Descriptions**

| Regulation | Jurisdiction | Data Protection Focus | Key Requirements |
|------------|--------------|----------------------|------------------|
| **GDPR** | EU/EEA | Personal data of EU residents | Art.32 security measures, Art.5 data minimization, Art.25 privacy by design |
| **FADP** | Switzerland | Personal data in Switzerland | Art.8 data security, Art.5 proportionality, Art.19 breach notification |
| **HIPAA** | USA | Protected Health Information (PHI) | 45 CFR 164.312(a)(2)(iv) encryption, 164.308 safeguards |
| **PCI-DSS** | Global | Payment card data | Req.3.4 masking PAN, Req.3.5 key management, Req.8 access control |
| **CCPA/CPRA** | California, USA | Personal information of CA residents | Right to deletion, right to opt-out, privacy by design |
| **LGPD** | Brazil | Personal data in Brazil | Art.46 security measures, Art.48 breach notification |
| **SOC 2** | Global | Service organization controls | CC6.1 logical access, CC6.6 encryption, CC6.7 data transmission |
| **ISO 27001** | Global | Information security management | A.8.11 data masking, A.8.24 cryptography, A.8.10 deletion |
| **PIPEDA** | Canada | Personal information in Canada | Safeguards principle, consent principle, accountability |
| **DPA 2018** | UK | Personal data in UK | Schedule 1 processing conditions, Part 2 security |
| **APPI** | Japan | Personal information in Japan | Art.20 security control, Art.23 anonymization |
| **PDPA** | Singapore | Personal data in Singapore | S.24 protection obligation, S.26 notification of breach |

**Column Widths:** A=15, B=15, C=30, D=40

## Regulatory Mapping Checklist (Rows 74-85)

**Row 74: Section Header**

- **Cell A74:** "REGULATORY MAPPING CHECKLIST"
- **Merge:** A74:E74
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Row 75: Table Headers**

| Column | Header | Width |
|--------|--------|-------|
| A | # | 5 |
| B | Checklist Item | 50 |
| C | Status | 15 |
| D | Evidence | 25 |
| E | Notes | 25 |

**Rows 76-85: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Are all applicable regulations identified per data element? | [Dropdown] | [Text] | [Text] |
| 2 | Are specific regulatory articles/requirements documented? | [Dropdown] | [Text] | [Text] |
| 3 | Are data subject rights mapped (access, deletion, portability)? | [Dropdown] | [Text] | [Text] |
| 4 | Are breach notification requirements documented? | [Dropdown] | [Text] | [Text] |
| 5 | Are cross-border transfer restrictions identified? | [Dropdown] | [Text] | [Text] |
| 6 | Are data retention requirements compliance-based? | [Dropdown] | [Text] | [Text] |
| 7 | Is masking legally required or best practice only? | [Dropdown] | [Text] | [Text] |
| 8 | Is compliance status tracked per regulatory requirement? | [Dropdown] | [Text] | [Text] |
| 9 | Is compliance ownership assigned? | [Dropdown] | [Text] | [Text] |
| 10 | Are regulatory audits conducted and documented? | [Dropdown] | [Text] | [Text] |

---

# Sheet 7: Data_Owner_Assignment

## Purpose
Assign formal data ownership for each sensitive data category or element. Establishes accountability for classification decisions, masking approvals, and data governance.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "DATA OWNER ASSIGNMENT & APPROVAL"
- **Merge:** A1:M1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Assign data owners and obtain approval for data classification and masking decisions (30 row template)"
- **Merge:** A2:M2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Has [Organization] formally assigned data owners for all sensitive data categories?"
- **Merge:** A3:I3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell J4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** J4:M4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Data Category | 15 | Dropdown | Reference Data_Category_Reference!A:A |
| B | Category Name | 20 | Auto-populate | From Data_Category_Reference |
| C | Primary Data Owner | 20 | Text | Name and title (e.g., "Jane Doe - CDO") |
| D | Data Owner Email | 25 | Text | Email validation format |
| E | Data Owner Department | 18 | Text | Free text |
| F | Backup Data Owner | 20 | Text | Name and title |
| G | Data Steward | 20 | Text | Operational contact (optional) |
| H | Assignment Date | 12 | Date | Date picker |
| I | Approval Status | 15 | Dropdown | ✅ Approved, ⚠️ Pending, ❌ Declined, 📋 Under Review |
| J | Classification Approved? | 15 | Dropdown | Yes, No, Pending, N/A |
| K | Masking Approved? | 15 | Dropdown | Yes, No, Pending, N/A |
| L | Last Review Date | 12 | Date | Date picker |
| M | Next Review Date | 12 | Date | Auto-calc: Last Review + 365 days |

**Header Row Formatting:**

- **Row Height:** 35px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | CAT-FIN |
| B | Financial Data |
| C | Jane Smith - Chief Financial Officer (CFO) |
| D | jane.smith@organization.example |
| E | Finance |
| F | John Doe - VP Finance |
| G | Mary Johnson - Finance Data Steward |
| H | 01.01.2026 |
| I | ✅ Approved |
| J | Yes |
| K | Yes |
| L | 15.01.2026 |
| M | 15.01.2027 |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic

## Data Entry Rows (Rows 8-37)

**30 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked

**Auto-populate Formula:**

**Column B (Category Name):**
```excel
=IFERROR(VLOOKUP(A8,Data_Category_Reference!$A:$B,2,FALSE),"")
```

**Column M (Next Review Date):**
```excel
=IF(ISBLANK(L8),"",DATE(YEAR(L8)+1,MONTH(L8),DAY(L8)))
```
Explanation: Annual review (Last Review + 365 days)

**Data Validation (Column D - Email):**
```excel
Custom formula: =AND(ISNUMBER(FIND("@",D8)),ISNUMBER(FIND(".",D8)))
Error Alert: "Please enter a valid email address"
```

**Conditional Formatting (Column I - Approval Status):**

- ✅ Approved → Green fill (RGB 198, 239, 206)
- ⚠️ Pending → Yellow fill (RGB 255, 235, 156)
- ❌ Declined → Red fill (RGB 255, 199, 206)
- 📋 Under Review → Blue fill (RGB 180, 199, 231)

**Conditional Formatting (Columns J, K - Yes/No/Pending):**

- Yes → Green fill (RGB 198, 239, 206)
- No → Red fill (RGB 255, 199, 206)
- Pending → Yellow fill (RGB 255, 235, 156)
- N/A → Gray fill (RGB 217, 217, 217)

## RACI Matrix (Rows 39-50)

**Row 39: Section Header**

- **Cell A39:** "DATA OWNERSHIP RACI MATRIX"
- **Merge:** A39:E39
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray

**Row 40: RACI Definition**

- **Cell A40:** "R=Responsible, A=Accountable, C=Consulted, I=Informed"
- **Merge:** A40:E40
- **Font:** Calibri 10pt Italic

**Rows 41-50: RACI Table**

| Activity | Data Owner | Data Steward | CISO/Security Team | DPO | IT Operations |
|----------|------------|--------------|-------------------|-----|---------------|
| Data Classification | A | R | C | C | I |
| Masking Decision | A | C | R | C | I |
| Access Control Policy | A | I | R | C | I |
| Data Retention Policy | A | R | C | C | I |
| Breach Response | C | C | R | A | R |
| Regulatory Compliance | A | C | C | A | I |
| Data Quality | A | R | I | I | C |
| Schema Changes | C | R | I | I | A |
| Annual Review | A | R | C | C | I |

**Column Widths:** A=25, B=12, C=12, D=15, E=10, F=12

**Formatting:**

- **Font:** Calibri 10pt
- **Alignment:** Center for RACI letters, Left for Activity column
- **Border:** All borders, thin weight

## Data Owner Assignment Checklist (Rows 52-62)

**Row 52: Section Header**

- **Cell A52:** "DATA OWNER ASSIGNMENT CHECKLIST"
- **Merge:** A52:E52
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Row 53: Table Headers**

| Column | Header | Width |
|--------|--------|-------|
| A | # | 5 |
| B | Checklist Item | 50 |
| C | Status | 15 |
| D | Evidence | 25 |
| E | Notes | 25 |

**Rows 54-62: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is a primary data owner assigned for each data category? | [Dropdown] | [Text] | [Text] |
| 2 | Is a backup data owner assigned for each category? | [Dropdown] | [Text] | [Text] |
| 3 | Are data owner roles formally documented (job description)? | [Dropdown] | [Text] | [Text] |
| 4 | Have data owners acknowledged their responsibilities? | [Dropdown] | [Text] | [Text] |
| 5 | Is data owner approval obtained for classifications? | [Dropdown] | [Text] | [Text] |
| 6 | Is data owner approval obtained for masking decisions? | [Dropdown] | [Text] | [Text] |
| 7 | Are data stewards assigned for operational support? | [Dropdown] | [Text] | [Text] |
| 8 | Are data ownership assignments reviewed annually? | [Dropdown] | [Text] | [Text] |
| 9 | Is RACI matrix communicated to all stakeholders? | [Dropdown] | [Text] | [Text] |

---

# Sheet 8: Masking_Priority_Matrix

## Purpose
Prioritize masking implementation efforts based on data sensitivity, exposure risk, regulatory requirements, and business criticality. Generates a risk-weighted priority score (P1/P2/P3/P4).

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "MASKING PRIORITY MATRIX (Risk-Based)"
- **Merge:** A1:Q1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Calculate masking priority using risk-weighted scoring: Priority = (Sensitivity×3) + (Exposure×2) + (Regulatory×2) + (Volume×1) [50 row template]"
- **Merge:** A2:Q2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Has [Organization] completed risk-based prioritization for all masking requirements?"
- **Merge:** A3:M3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell N4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** N4:Q4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Data Element ID | 15 | Lookup | Reference Sensitive_Data_Inventory!A:A |
| B | Field Name | 20 | Auto-populate | From Sensitive_Data_Inventory |
| C | Data Category | 15 | Auto-populate | From Sensitive_Data_Inventory |
| D | Sensitivity Level | 15 | Auto-populate | From Classification_Matrix |
| E | Sensitivity Score (1-5) | 12 | Dropdown | 5=Critical, 4=High, 3=Medium, 2=Low, 1=Public |
| F | Exposure Risk | 15 | Dropdown | Very High, High, Medium, Low, Very Low |
| G | Exposure Score (1-5) | 12 | Dropdown | 5=Very High, 4=High, 3=Medium, 2=Low, 1=Very Low |
| H | Regulatory Weight | 15 | Dropdown | Mandatory, High, Medium, Low, None |
| I | Regulatory Score (1-5) | 12 | Dropdown | 5=Mandatory, 4=High, 3=Medium, 2=Low, 1=None |
| J | Data Volume | 15 | Dropdown | Very Large (>1M), Large (100K-1M), Medium (10K-100K), Small (<10K) |
| K | Volume Score (1-4) | 12 | Dropdown | 4=Very Large, 3=Large, 2=Medium, 1=Small |
| L | **Total Priority Score** | 12 | Formula | `=(E×3)+(G×2)+(I×2)+(K×1)` Max=40 |
| M | **Priority Tier** | 12 | Formula | P1 (30-40), P2 (20-29), P3 (10-19), P4 (<10) |
| N | Implementation Status | 15 | Dropdown | ✅ Complete, 🔄 In Progress, ❌ Not Started, 🚫 Blocked |
| O | Target Completion Date | 15 | Date | Date picker |
| P | Assigned To | 18 | Text | Team/person responsible |
| Q | Notes | 25 | Text | Implementation notes |

**Header Row Formatting:**

- **Row Height:** 40px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | DE-001 |
| B | credit_card_number |
| C | CAT-FIN |
| D | Critical |
| E | 5 |
| F | High |
| G | 4 |
| H | Mandatory |
| I | 5 |
| J | Very Large (>1M) |
| K | 4 |
| L | 33 |
| M | P1 |
| N | ✅ Complete |
| O | 15.12.2025 |
| P | Security Engineering Team |
| Q | Tokenization implemented in all non-prod environments |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic

## Data Entry Rows (Rows 8-57)

**50 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC) for user input columns
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked for E, G, I, K, N, O, P, Q; Locked for L, M (formulas)

**Auto-populate Formulas:**

**Column B (Field Name):**
```excel
=IFERROR(VLOOKUP(A8,Sensitive_Data_Inventory!$A:$F,6,FALSE),"")
```

**Column C (Data Category):**
```excel
=IFERROR(VLOOKUP(A8,Sensitive_Data_Inventory!$A:$H,8,FALSE),"")
```

**Column D (Sensitivity Level):**
```excel
=IFERROR(VLOOKUP(A8,Classification_Matrix!$A:$D,4,FALSE),"")
```

**Column L (Total Priority Score) - CRITICAL FORMULA:**
```excel
=IF(OR(ISBLANK(E8),ISBLANK(G8),ISBLANK(I8),ISBLANK(K8)),"",
   (E8*3)+(G8*2)+(I8*2)+(K8*1))
```
Explanation: Weighted sum = (Sensitivity×3) + (Exposure×2) + (Regulatory×2) + (Volume×1)
Maximum possible score: (5×3)+(5×2)+(5×2)+(4×1) = 15+10+10+4 = 39

**Column M (Priority Tier) - CRITICAL FORMULA:**
```excel
=IF(ISBLANK(L8),"",
   IF(L8>=30,"P1",
   IF(L8>=20,"P2",
   IF(L8>=10,"P3","P4"))))
```
Explanation:

- P1 (Critical): Score 30-40 → Immediate action required
- P2 (High): Score 20-29 → Implement within 90 days
- P3 (Medium): Score 10-19 → Implement within 180 days
- P4 (Low): Score <10 → Risk-based decision

**Conditional Formatting (Column L - Priority Score):**

- Score ≥30 → Red fill (RGB 255, 199, 206) - P1 Critical
- Score 20-29 → Orange fill (RGB 255, 235, 156) - P2 High
- Score 10-19 → Yellow fill (RGB 255, 242, 204) - P3 Medium
- Score <10 → Light green (RGB 226, 239, 218) - P4 Low

**Conditional Formatting (Column M - Priority Tier):**

- P1 → Red fill (RGB 255, 199, 206), Bold font
- P2 → Orange fill (RGB 255, 235, 156), Bold font
- P3 → Yellow fill (RGB 255, 242, 204)
- P4 → Light green (RGB 226, 239, 218)

**Conditional Formatting (Column N - Implementation Status):**

- ✅ Complete → Green fill (RGB 198, 239, 206)
- 🔄 In Progress → Blue fill (RGB 180, 199, 231)
- ❌ Not Started → Red fill (RGB 255, 199, 206)
- 🚫 Blocked → Dark red fill (RGB 192, 0, 0), White text

## Risk Scoring Guidance (Rows 59-75)

**Row 59: Section Header**

- **Cell A59:** "RISK SCORING GUIDANCE"
- **Merge:** A59:D59
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray

**Rows 60-75: Scoring Tables**

**Sensitivity Score (Rows 61-66):**

| Level | Score | Criteria |
|-------|-------|----------|
| Critical | 5 | Legal breach guaranteed if exposed, severe harm |
| High | 4 | Substantial harm, regulatory violation likely |
| Medium | 3 | Moderate harm, business impact |
| Low | 2 | Minimal harm, internal use only |
| Public | 1 | No confidentiality requirement |

**Exposure Risk Score (Rows 68-73):**

| Risk Level | Score | Criteria |
|------------|-------|----------|
| Very High | 5 | Internet-facing, no access controls, unencrypted |
| High | 4 | Internal network, limited access controls |
| Medium | 3 | Segmented network, access controls in place |
| Low | 2 | Isolated network, strong access controls |
| Very Low | 1 | Air-gapped, encrypted at rest, strict access |

**Regulatory Weight Score (Rows 75-80):**

| Weight | Score | Criteria |
|--------|-------|----------|
| Mandatory | 5 | Legal requirement (PCI-DSS, HIPAA, GDPR Art.32) |
| High | 4 | Regulatory expectation, audit scrutiny |
| Medium | 3 | Industry best practice, compliance framework |
| Low | 2 | Internal policy requirement |
| None | 1 | No regulatory mandate |

**Volume Score (Rows 82-86):**

| Volume | Score | Criteria |
|--------|-------|----------|
| Very Large | 4 | >1 million records |
| Large | 3 | 100,000 - 1 million records |
| Medium | 2 | 10,000 - 100,000 records |
| Small | 1 | <10,000 records |

## Priority Summary Dashboard (Rows 88-100)

**Row 88: Section Header**

- **Cell A88:** "MASKING PRIORITY SUMMARY"
- **Merge:** A88:F88
- **Font:** Calibri 12pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 89-100: Summary Statistics**

| Metric | Formula | Target | Status |
|--------|---------|--------|--------|
| **Total Data Elements Assessed** | `=COUNTA(A8:A57)-COUNTBLANK(A8:A57)` | N/A | Info |
| **P1 (Critical Priority) Count** | `=COUNTIF(M8:M57,"P1")` | 0 | Conditional |
| **P2 (High Priority) Count** | `=COUNTIF(M8:M57,"P2")` | <5 | Conditional |
| **P3 (Medium Priority) Count** | `=COUNTIF(M8:M57,"P3")` | <10 | Conditional |
| **P4 (Low Priority) Count** | `=COUNTIF(M8:M57,"P4")` | N/A | Info |
| **Implementation Complete (%)** | `=COUNTIF(N8:N57,"✅ Complete")/COUNTA(N8:N57)*100` | 100% | Conditional |
| **In Progress (%)** | `=COUNTIF(N8:N57,"🔄 In Progress")/COUNTA(N8:N57)*100` | N/A | Info |
| **Not Started (%)** | `=COUNTIF(N8:N57,"❌ Not Started")/COUNTA(N8:N57)*100` | 0% | Conditional |
| **Blocked Items** | `=COUNTIF(N8:N57,"🚫 Blocked")` | 0 | Conditional |
| **Overdue Items** | `=COUNTIFS(O8:O57,"<"&TODAY(),N8:N57,"<>✅ Complete")` | 0 | Conditional |
| **P1 Completion Rate (%)** | `=COUNTIFS(M8:M57,"P1",N8:N57,"✅ Complete")/COUNTIF(M8:M57,"P1")*100` | 100% | Conditional |

**Conditional Formatting (Status Column):**

- Green: Metric meets target
- Yellow: Metric within acceptable range
- Red: Metric below target, action required

---

# Sheet 9: Gap_Analysis

## Purpose
Document and track gaps in data inventory, classification, ownership assignment, and masking implementation. Provides action plan for remediation.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "GAP ANALYSIS & REMEDIATION TRACKING"
- **Merge:** A1:N1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Document gaps identified during inventory, classification, or ownership assessment (30 row template)"
- **Merge:** A2:N2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Are all identified gaps documented with remediation plans and target dates?"
- **Merge:** A3:J3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell K4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** K4:N4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Gap ID | 12 | Text | GAP-001, GAP-002, etc. |
| B | Gap Category | 18 | Dropdown | Inventory Gap, Classification Gap, Ownership Gap, Masking Gap, Documentation Gap, Process Gap |
| C | Gap Description | 35 | Text | Detailed description of the gap |
| D | Affected Data/System | 20 | Text | Which data elements or systems are affected |
| E | Risk Level | 12 | Dropdown | Critical, High, Medium, Low |
| F | Business Impact | 25 | Text | Impact if gap not addressed |
| G | Root Cause | 25 | Text | Why does this gap exist? |
| H | Remediation Plan | 30 | Text | Actions to close the gap |
| I | Owner | 18 | Text | Person responsible for remediation |
| J | Target Date | 12 | Date | Date picker |
| K | Status | 15 | Dropdown | ✅ Closed, 🔄 In Progress, ❌ Open, 🚫 Blocked, 📋 Planned |
| L | Actual Closure Date | 12 | Date | Date picker |
| M | Verification Evidence | 25 | Text | How gap closure was verified |
| N | Notes | 25 | Text | Additional comments |

**Header Row Formatting:**

- **Row Height:** 35px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | GAP-001 |
| B | Masking Gap |
| C | Customer SSN field not masked in UAT environment |
| D | SYS-001 / customers.ssn |
| E | Critical |
| F | Regulatory breach (GDPR, FADP), potential fine, audit finding |
| G | UAT environment refresh process skips masking step |
| H | Update data refresh script to include masking, verify with test restore |
| I | Database Admin Team |
| J | 31.01.2026 |
| K | 🔄 In Progress |
| L | [blank] |
| M | [pending] |
| N | Temporary access restricted to authorized personnel only until resolved |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic

## Data Entry Rows (Rows 8-37)

**30 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked

**Conditional Formatting (Column E - Risk Level):**

- Critical → Red fill (RGB 255, 199, 206)
- High → Orange fill (RGB 255, 235, 156)
- Medium → Yellow fill (RGB 255, 242, 204)
- Low → Light green (RGB 226, 239, 218)

**Conditional Formatting (Column K - Status):**

- ✅ Closed → Green fill (RGB 198, 239, 206)
- 🔄 In Progress → Blue fill (RGB 180, 199, 231)
- ❌ Open → Red fill (RGB 255, 199, 206)
- 🚫 Blocked → Dark red fill (RGB 192, 0, 0), White text
- 📋 Planned → Gray fill (RGB 217, 217, 217)

**Data Validation (Column J - Target Date):**
```excel
Custom: =J8>=TODAY()
Error Alert: "Target date should be in the future"
```

## Gap Summary Statistics (Rows 39-52)

**Row 39: Section Header**

- **Cell A39:** "GAP SUMMARY STATISTICS"
- **Merge:** A39:E39
- **Font:** Calibri 12pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 40-52: Statistics Table**

| Metric | Formula | Target | Status |
|--------|---------|--------|--------|
| Total Gaps Identified | `=COUNTA(A8:A37)-COUNTBLANK(A8:A37)` | N/A | Info |
| Critical Gaps | `=COUNTIF(E8:E37,"Critical")` | 0 | Conditional |
| High Risk Gaps | `=COUNTIF(E8:E37,"High")` | <3 | Conditional |
| Gaps Closed | `=COUNTIF(K8:K37,"✅ Closed")` | 100% | Conditional |
| Gaps In Progress | `=COUNTIF(K8:K37,"🔄 In Progress")` | N/A | Info |
| Gaps Open | `=COUNTIF(K8:K37,"❌ Open")` | 0 | Conditional |
| Gaps Blocked | `=COUNTIF(K8:K37,"🚫 Blocked")` | 0 | Conditional |
| Overdue Gaps | `=COUNTIFS(J8:J37,"<"&TODAY(),K8:K37,"<>✅ Closed")` | 0 | Conditional |
| Closure Rate (%) | `=COUNTIF(K8:K37,"✅ Closed")/COUNTA(K8:K37)*100` | 100% | Conditional |
| Avg Days to Close | `=AVERAGEIF(L8:L37,"<>"&"",L8:L37-J8:J37)` | <30 | Conditional |
| Critical Gaps Closed (%) | `=COUNTIFS(E8:E37,"Critical",K8:K37,"✅ Closed")/COUNTIF(E8:E37,"Critical")*100` | 100% | Conditional |

---

# Sheet 10: Evidence_Register

## Purpose
Central repository for all compliance evidence supporting data inventory, classification, ownership, and masking implementation.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "COMPLIANCE EVIDENCE REGISTER"
- **Merge:** A1:L1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Document all evidence supporting compliance with data masking requirements (40 row template)"
- **Merge:** A2:L2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Is compliance evidence documented, stored securely, and retrievable for audit purposes?"
- **Merge:** A3:H3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell I4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** I4:L4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Evidence ID | 12 | Formula | Auto-generate: EV-001, EV-002, etc. |
| B | Evidence Type | 20 | Dropdown | Schema Documentation, Discovery Report, DPIA, Classification Review, Approval Email, Test Results, Screenshot, Configuration File, Meeting Minutes, Other |
| C | Description | 35 | Text | Brief description of evidence |
| D | Related Requirement | 20 | Text | Policy section or checklist item |
| E | Related Data/System | 20 | Text | Which data elements or systems |
| F | File Location | 30 | Text | File path or document management system reference |
| G | Created Date | 12 | Date | Date picker |
| H | Retention Period | 15 | Text | E.g., "7 years", "Indefinite" |
| I | Owner/Custodian | 18 | Text | Who maintains this evidence |
| J | Classification | 15 | Dropdown | Public, Internal, Confidential, Restricted |
| K | Last Verified | 12 | Date | Date picker |
| L | Notes | 25 | Text | Additional information |

**Header Row Formatting:**

- **Row Height:** 35px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | EV-001 |
| B | Discovery Report |
| C | BigID data discovery scan report for production database |
| D | ISMS-POL-A.8.11, Section 2.1 (Data Classification and Identification) REQ-CLS-010 |
| E | SYS-001 (Customer Database) |
| F | /compliance/data-masking/2026/BigID_Scan_20260110.pdf |
| G | 10.01.2026 |
| H | 7 years |
| I | Data Protection Officer |
| J | Confidential |
| K | 15.01.2026 |
| L | Quarterly scan, next due 10.04.2026 |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic

## Data Entry Rows (Rows 8-47)

**40 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked for B-L; Locked for A (formula)

**Column A (Evidence ID) - Auto-Generate:**
```excel
="EV-"&TEXT(ROW()-7,"000")
```
Explanation: Generates EV-001, EV-002, EV-003, etc. automatically

**Conditional Formatting (Column J - Classification):**

- Restricted → Red fill (RGB 255, 199, 206)
- Confidential → Yellow fill (RGB 255, 235, 156)
- Internal → Light blue (RGB 180, 199, 231)
- Public → White (no fill)

## Evidence Type Definitions (Rows 49-62)

**Row 49: Section Header**

- **Cell A49:** "EVIDENCE TYPE DEFINITIONS"
- **Merge:** A49:C49
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray

**Rows 50-62: Definitions Table**

| Evidence Type | Description | Examples |
|---------------|-------------|----------|
| Schema Documentation | Database schema, data dictionaries, ERD diagrams | DDL scripts, ER diagrams, data models |
| Discovery Report | Automated data discovery tool output | BigID, Varonis, OneTrust scan reports |
| DPIA | Data Protection Impact Assessment | GDPR Article 35 assessments |
| Classification Review | Classification decision documentation | Review meeting minutes, decision matrices |
| Approval Email | Email approvals from data owners | Classification approvals, masking approvals |
| Test Results | Masking effectiveness test results | Irreversibility tests, format validation |
| Screenshot | Visual evidence of configurations | Masking tool settings, access controls |
| Configuration File | System/tool configuration exports | Masking rules, DDM policies |
| Meeting Minutes | Governance meeting documentation | Data governance meetings, steering committee |
| Other | Any other relevant evidence | Audit reports, third-party assessments |

---

# Sheet 11: Summary_Dashboard

## Purpose
Executive summary consolidating all assessment data into actionable compliance metrics and KPIs.

## Header Section (Rows 1-3)

**Row 1: Sheet Title**

- **Cell A1:** "EXECUTIVE SUMMARY DASHBOARD"
- **Merge:** A1:G1
- **Font:** Calibri 16pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center
- **Row Height:** 50px

**Row 2: Assessment Period**

- **Cell A2:** "Assessment Period:"
- **Cell B2:** [User Input - Date Range]
- **Merge:** B2:D2
- **Fill:** Light Yellow (#FFFFCC)

**Row 3: Last Updated**

- **Cell A3:** "Last Updated:"
- **Cell B3:** `=TODAY()`
- **Format:** DD.MM.YYYY

## Overall Compliance Summary (Rows 5-12)

**Row 5: Section Header**

- **Cell A5:** "OVERALL COMPLIANCE STATUS"
- **Merge:** A5:G5
- **Font:** Calibri 14pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 6-12: Key Metrics**

| Metric | Formula | Target | Status |
|--------|---------|--------|--------|
| **Systems Inventoried (%)** | `=COUNTIF(System_Inventory!J:J,"✅ Complete")/COUNTA(System_Inventory!A8:A57)*100` | 100% | Conditional |
| **Sensitive Fields Classified (%)** | `=COUNTIF(Classification_Matrix!P:P,"✅ Approved")/COUNTA(Classification_Matrix!A8:A107)*100` | 100% | Conditional |
| **Data Owners Assigned (%)** | `=COUNTIF(Data_Owner_Assignment!I:I,"✅ Approved")/COUNTA(Data_Owner_Assignment!A8:A37)*100` | 100% | Conditional |
| **Masking Implementation (%)** | `=COUNTIF(Masking_Priority_Matrix!N:N,"✅ Complete")/COUNTA(Masking_Priority_Matrix!A8:A57)*100` | 100% | Conditional |
| **Critical Gaps Open** | `=COUNTIFS(Gap_Analysis!E:E,"Critical",Gap_Analysis!K:K,"<>✅ Closed")` | 0 | Conditional |
| **Evidence Documents** | `=COUNTA(Evidence_Register!A8:A47)` | >20 | Conditional |
| **Overall Compliance Score** | `=AVERAGE(B6,B7,B8,B9)` | ≥95% | Conditional |

**Conditional Formatting (Status Column):**

- ≥95% or Target Met → Green fill (RGB 198, 239, 206)
- 80-94% → Yellow fill (RGB 255, 235, 156)
- <80% → Red fill (RGB 255, 199, 206)

## Data Category Breakdown (Rows 14-26)

**Row 14: Section Header**

- **Cell A14:** "DATA CATEGORY COMPLIANCE"
- **Merge:** A14:G14
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray

**Rows 15-26: Category Summary**

| Data Category | Fields Inventoried | Classified | Owner Assigned | Masking Required | Masked | Compliance % |
|---------------|-------------------|------------|----------------|------------------|--------|--------------|
| CAT-PII-D | `=COUNTIF(...)` | `=COUNTIF(...)` | `=COUNTIF(...)` | `=COUNTIF(...)` | `=COUNTIF(...)` | `=Formula` |
| CAT-FIN | Formula | Formula | Formula | Formula | Formula | Formula |
| CAT-HLT | Formula | Formula | Formula | Formula | Formula | Formula |
| CAT-CRD | Formula | Formula | Formula | Formula | Formula | Formula |
| [Additional categories as needed] | | | | | | |

## Regulatory Compliance Summary (Rows 28-34)

**Row 28: Section Header**

- **Cell A28:** "REGULATORY COMPLIANCE STATUS"
- **Merge:** A28:G28
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray

**Rows 29-34: Regulatory Table**

| Regulation | Applicable? | Fields in Scope | Classified | Owner Assigned | Masking Required | Compliance % |
|------------|-------------|-----------------|------------|----------------|------------------|--------------|
| GDPR | `=COUNTIF(...)` | Formula | Formula | Formula | Formula | Formula |
| FADP | Formula | Formula | Formula | Formula | Formula | Formula |
| HIPAA | Formula | Formula | Formula | Formula | Formula | Formula |
| PCI-DSS | Formula | Formula | Formula | Formula | Formula | Formula |
| Other | Formula | Formula | Formula | Formula | Formula | Formula |

## Masking Priority Summary (Rows 36-42)

**Row 36: Section Header**

- **Cell A36:** "MASKING PRIORITY STATUS"
- **Merge:** A36:G36
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray

**Rows 37-42: Priority Table**

| Priority | Count | % Total | Complete | In Progress | Not Started | Blocked | On-Track? |
|----------|-------|---------|----------|-------------|-------------|---------|-----------|
| P1 (Critical) | `=COUNTIF(...)` | Formula | Formula | Formula | Formula | Formula | Formula |
| P2 (High) | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| P3 (Medium) | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| P4 (Low) | Formula | Formula | Formula | Formula | Formula | Formula | Formula |

## Top 10 Gaps (Rows 44-55)

**Row 44: Section Header**

- **Cell A44:** "TOP 10 GAPS REQUIRING ATTENTION"
- **Merge:** A44:G44
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray

**Rows 45-55: Gap List**

| Rank | Gap ID | Gap Description | Risk Level | Target Date | Owner | Status |
|------|--------|-----------------|------------|-------------|-------|--------|
| 1 | Lookup from Gap_Analysis | Lookup | Lookup | Lookup | Lookup | Lookup |
| 2 | ... | ... | ... | ... | ... | ... |

**Lookup Formula Example (Gap ID):**
```excel
=INDEX(Gap_Analysis!$A:$A,MATCH(LARGE(Gap_Analysis!$E:$E,ROW()-44),Gap_Analysis!$E:$E,0))
```
Explanation: Rank gaps by Risk Level, display top 10

## Key Performance Indicators (Rows 57-68)

**Row 57: Section Header**

- **Cell A57:** "KEY PERFORMANCE INDICATORS"
- **Merge:** A57:E57
- **Font:** Calibri 12pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 58-68: KPI Table**

| KPI | Current Value | Target | Status | Trend |
|-----|---------------|--------|--------|-------|
| % Systems Inventoried | Formula | 100% | Conditional | ↑ ↓ → |
| % Sensitive Fields Classified | Formula | 100% | Conditional | Trend |
| % Data Owners Assigned | Formula | 100% | Conditional | Trend |
| % Regulatory Mapping Complete | Formula | 100% | Conditional | Trend |
| % Masking Requirements Defined | Formula | 100% | Conditional | Trend |
| % P1 Items Complete | Formula | 100% | Conditional | Trend |
| Mean Time to Classify (days) | Number | <30 days | Conditional | Trend |
| Inventory Accuracy (last audit) | Number | >95% | Conditional | Trend |
| Open Critical Gaps | Formula | 0 | Conditional | Trend |

## Assessment Sign-Off (Rows 70-78)

**Row 70: Section Header**

- **Cell A70:** "ASSESSMENT APPROVAL & SIGN-OFF"
- **Merge:** A70:E70
- **Font:** Calibri 12pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 71-78: Sign-Off Table**

| Role | Name | Signature | Date | Comments |
|------|------|-----------|------|----------|
| Data Governance Lead | [Text] | [Text] | [Date] | [Text] |
| Chief Data Officer (CDO) | [Text] | [Text] | [Date] | [Text] |
| Data Protection Officer (DPO) | [Text] | [Text] | [Date] | [Text] |
| Chief Information Security Officer (CISO) | [Text] | [Text] | [Date] | [Text] |
| Legal/Compliance Officer | [Text] | [Text] | [Date] | [Text] |

**Fill:** Light Yellow (#FFFFCC) for all input cells  
**Protection:** Unlocked for user input

---

# Python Script Integration Notes

## Generator Script: `generate_a811_1_data_inventory.py`

**CRITICAL: THIS IS A SAMPLE SCRIPT TEMPLATE**
```python
"""
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR CONTROL A.8.11

This script generates the ISMS-IMP-A.8.11.1 Data Inventory & Classification 
Assessment Excel workbook.

CUSTOMIZATION REQUIRED:
1. Update sheet structures if taxonomy changes
2. Modify validation dropdowns for organization-specific values
3. Adjust formulas if scoring algorithms change
4. Update data capacity (currently 50-100 rows per sheet)

DO NOT use without reviewing all sections marked "# CUSTOMIZE:"
"""

# Key Functions to Implement:
# - create_workbook(): Initialize workbook with 11 sheets
# - create_instructions_legend(): Sheet 1 with taxonomy reference
# - create_system_inventory(): Sheet 2 with 50 row capacity
# - create_data_category_reference(): Sheet 3 (read-only reference)
# - create_sensitive_data_inventory(): Sheet 4 with 100 row capacity
# - create_classification_matrix(): Sheet 5 with 100 row capacity
# - create_regulatory_mapping(): Sheet 6 with 50 row capacity
# - create_data_owner_assignment(): Sheet 7 with 30 row capacity
# - create_masking_priority_matrix(): Sheet 8 with priority scoring formulas
# - create_gap_analysis(): Sheet 9 with 30 row capacity
# - create_evidence_register(): Sheet 10 with 40 row capacity
# - create_summary_dashboard(): Sheet 11 with consolidated formulas
# - setup_data_validation(): Apply all dropdown validations
# - setup_conditional_formatting(): Apply color-coding rules
# - setup_cell_protection(): Lock formula cells, unlock input cells
```

## Key Customization Points

**1. Data Category Taxonomy (Sheet 3):**
```python
# CUSTOMIZE: Add organization-specific data categories
DATA_CATEGORIES = [
    {"id": "CAT-PII-D", "name": "Direct PII", "sensitivity": "High"},
    {"id": "CAT-FIN", "name": "Financial Data", "sensitivity": "Critical"},
    # Add custom categories here
]
```

**2. Validation Dropdowns:**
```python
# CUSTOMIZE: Modify dropdown options if needed
DROPDOWNS = {
    "system_type": "Database,Application,SaaS,File Share,API,Data Warehouse,Backup System,Archive,Other",
    "environment": "Production,Development,Test/QA,UAT,Training,Analytics,DR/Backup,Decommissioned",
    "status": "✅ Complete,⚠️ Partial,❌ Missing,📋 Planned,N/A"
}
```

**3. Priority Scoring Formula:**
```python
# CUSTOMIZE: Adjust weights if risk model changes
# Current: (Sensitivity×3) + (Exposure×2) + (Regulatory×2) + (Volume×1)
def calculate_priority_score(sensitivity, exposure, regulatory, volume):
    return (sensitivity * 3) + (exposure * 2) + (regulatory * 2) + (volume * 1)
```

**4. Conditional Formatting Thresholds:**
```python
# CUSTOMIZE: Modify color thresholds if needed
COMPLIANCE_THRESHOLDS = {
    "green": 95,  # ≥95% = Green
    "yellow": 80,  # 80-94% = Yellow
    "red": 0       # <80% = Red
}
```

## Quality Assurance Script

**Script:** `validate_a811_1_structure.py`
```python
"""
Quality assurance script to validate generated workbook structure.

Validates:

- All 11 sheets present with correct names
- Column headers match specification
- Data validation rules applied correctly
- Conditional formatting ranges correct
- Formula accuracy (spot checks)
- Cell protection properly configured

"""
```

---

# Styling & Formatting Standards

## Global Color Palette

| Element | RGB | Hex | Usage |
|---------|-----|-----|-------|
| Header (Main) | 0, 51, 102 | #003366 | Dark Blue - Main titles |
| Subheader | 68, 114, 196 | #4472C4 | Medium Blue - Section headers |
| Column Headers | 217, 217, 217 | #D9D9D9 | Light Gray - Table headers |
| Input Cells | 255, 255, 204 | #FFFFCC | Light Yellow - User input |
| Status - Complete | 198, 239, 206 | #C6EFCE | Light Green |
| Status - Partial | 255, 235, 156 | #FFEB9C | Light Yellow |
| Status - Missing | 255, 199, 206 | #FFC7CE | Light Red |
| Status - Planned | 180, 199, 231 | #B4C7E7 | Light Blue |
| Example Rows | 231, 230, 230 | #E7E6E6 | Light Gray |

## Font Standards

- **Headers:** Calibri 14-16pt Bold
- **Subheaders:** Calibri 11-12pt Bold
- **Column Headers:** Calibri 10pt Bold
- **Data Cells:** Calibri 10pt Regular
- **Example Rows:** Calibri 10pt Italic

## Border Standards

- **Outer borders:** Medium weight (2pt)
- **Inner borders:** Thin weight (1pt)
- **Header separator:** Thick bottom border (3pt)

## Cell Protection Strategy

**Protected (Locked):**

- All column headers
- All formula cells
- All reference/example rows
- Instructions and legend text

**Unprotected (Unlocked):**

- All yellow input cells
- All user data entry rows
- Sign-off fields

---

# Workbook Metadata

**File Naming Convention:**  
`ISMS-IMP-A.8.11.1_Data_Inventory_Classification_YYYYMMDD.xlsx`

**Example:**  
`ISMS-IMP-A.8.11.1_Data_Inventory_Classification_20260119.xlsx`

**Excel Document Properties:**
```
Title: ISMS-IMP-A.8.11.1 - Data Inventory & Classification Assessment
Subject: ISO/IEC 27001:2022 Control A.8.11 Data Masking
Author: [Organization Name]
Company: [Organization Name]
Keywords: ISO 27001, Data Masking, Data Classification, Sensitive Data Inventory, A.8.11
Comments: Generated from ISMS policy framework. Do not modify structure without updating generator script.
```

---

# Requirements Traceability Matrix

This workbook assesses compliance with the following policy requirements:

| Policy Requirement | Description | Assessed In Sheet |
|--------------------|-------------|-------------------|
| REQ-CLS-001 | Maintain inventory of sensitive data categories | Sheet 4 (Sensitive_Data_Inventory) |
| REQ-CLS-002 | Classify data per organizational scheme | Sheet 5 (Classification_Matrix) |
| REQ-CLS-003 | Document sensitive data locations | Sheets 2, 4 |
| REQ-CLS-010 | Perform initial data discovery | Sheet 4 (Discovery Method column) |
| REQ-CLS-020 | Maintain living inventory | All sheets (Review Dates) |
| REQ-CLS-030 | Assign Data Owner per category | Sheet 7 (Data_Owner_Assignment) |
| REQ-CLS-031 | Data Owner approves masking | Sheet 7 (Approval Status) |
| REQ-CLS-032 | Annual classification review | Sheet 5 (Review Dates) |
| REQ-REG-001 | Map data to regulatory requirements | Sheet 6 (Regulatory_Mapping) |
| REQ-PRI-001 | Prioritize masking based on risk | Sheet 8 (Masking_Priority_Matrix) |

---

# Document Assembly Instructions

**To create the complete ISMS-IMP-A.8.11.1 document:**

1. **PART I: USER COMPLETION GUIDE** (separate document, ~500 lines)

   - Assessment Overview
   - Prerequisites
   - Assessment Workflow
   - Sheet-by-Sheet Completion Guide
   - Evidence Collection
   - Common Pitfalls
   - Quality Checklist

2. **PART II: TECHNICAL SPECIFICATION** (this document, ~1,500 lines)

   - Document Control
   - Workbook Structure Overview
   - 11 Sheet Specifications (detailed)
   - Python Script Integration Notes
   - Styling & Formatting Standards
   - Quality Assurance Requirements

**Final Combined Document Length:** ~2,000 lines (matching A.8.24 standard)

---

# Quality Assurance Checklist

Before finalizing the workbook, verify:

**Structure:**

- [ ] All 11 sheets present with correct names
- [ ] Sheet order matches specification
- [ ] All column headers match specification exactly
- [ ] Row counts match template specifications

**Data Validation:**

- [ ] All dropdown lists applied correctly
- [ ] Custom validation rules (email, dates) working
- [ ] Error messages appropriate and helpful

**Formulas:**

- [ ] All VLOOKUP formulas reference correct sheets
- [ ] Auto-calculation formulas (dates, scores) accurate
- [ ] Priority scoring formula tested with sample data
- [ ] Summary Dashboard formulas consolidate correctly

**Formatting:**

- [ ] Color palette consistent across all sheets
- [ ] Conditional formatting rules applied correctly
- [ ] Fonts and borders match standards
- [ ] Freeze panes set on all assessment sheets

**Protection:**

- [ ] Formula cells locked, input cells unlocked
- [ ] Sheet protection enabled (optional password)
- [ ] Allow filter and sort even when protected

**Usability:**

- [ ] Example rows present on assessment sheets
- [ ] Cell comments/notes on complex fields
- [ ] Instructions clear and complete
- [ ] Navigation logical and intuitive

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Final Notes for Implementation Team

**Critical Success Factors:**

1. **Data-Centric Approach:** This assessment focuses on WHAT data exists and WHERE it is, NOT on specific masking tools or products. Keep it vendor-agnostic.

2. **Evidence-Based:** Every classification, every ownership assignment, every masking decision must be documented with evidence. No checkbox compliance theater.

3. **Scalability:** The 50-100 row templates are starting points. Organizations with thousands of data elements should extend templates or create multiple workbooks.

4. **Automation:** The Python generator script is essential for consistency. Manual workbook creation is error-prone and not recommended.

5. **Integration:** This workbook feeds into IMP-A.8.11.2 (Masking Techniques), IMP-A.8.11.3 (Environment Coverage), and ultimately the Compliance Dashboard (IMP-A.8.11.5).

**Next Steps:**

1. Generate Python script from this specification
2. Execute script to create template workbook
3. Validate generated workbook against QA checklist
4. Test with sample organization data
5. Iterate based on usability feedback
6. Deploy to ISMS implementation teams

---

**Document Control:**

- **Version:** 1.0
- **Date:** [Date]
- **Status:** Approved for Implementation
- **Author:** ISMS Implementation Team
- **Approver:** CISO / Chief Data Officer
- **Review Cycle:** Annual or when Control A.8.11 requirements change

---

**END OF SPECIFICATION**

---

*"Quantum physics tells us that reality is far more interconnected than our everyday experience suggests."*
— Alain Aspect

<!-- QA_VERIFIED: 2026-02-06 -->
