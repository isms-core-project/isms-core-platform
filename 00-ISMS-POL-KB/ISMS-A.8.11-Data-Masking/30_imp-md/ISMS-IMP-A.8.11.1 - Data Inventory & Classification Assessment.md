# ISMS-IMP-A.8.11.1 - Data Inventory & Classification Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.11.1  
**Assessment Area:** Sensitive Data Inventory & Classification  
**Related Policy:** ISMS-POL-A.8.11-S2.1 (Data Classification & Identification)  
**Purpose:** Document all systems containing sensitive data, classify data elements, identify masking requirements, and establish data ownership in a vendor-agnostic manner

**Key Principle:** This assessment is **data-centric, not tool-centric**. Organizations identify WHAT data they have, WHERE it resides, and WHO owns it — independent of specific masking tools.

---

## Workbook Structure

### Sheet 1: Instructions_Legend

#### Header Section
- **Title:** "ISMS-IMP-A.8.11.1 — Data Inventory & Classification Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.11: Data Masking"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block
```
Document ID:           ISMS-IMP-A.8.11.1
Assessment Area:       Data Inventory & Classification
Related Policy:        ISMS-POL-A.8.11-S2.1
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly (Inventory) / Annual (Classification Review)
```

#### How to Use This Workbook
1. Start with System_Inventory — list ALL systems/databases that process data
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

#### Data Category Taxonomy (Quick Reference)
| Category ID | Category Name | Examples |
|-------------|---------------|----------|
| CAT-PII-D | Direct PII | Name, SSN/AHV, Passport, Email, Phone |
| CAT-PII-I | Indirect PII | DOB+ZIP, Job Title+Department |
| CAT-FIN | Financial Data | Credit Card (PAN), IBAN, Account Balance |
| CAT-HLT | Health Data | Diagnoses, Prescriptions, Medical Records |
| CAT-CRD | Credentials | Passwords, API Keys, Tokens |
| CAT-PRP | Proprietary | Trade Secrets, Pricing, IP |
| CAT-LOC | Location Data | GPS, IP Address, Travel History |
| CAT-BIO | Biometric | Fingerprints, Facial Geometry |
| CAT-GEN | Genetic Data | DNA, Genetic Test Results |
| CAT-CHD | Child Data | Data of minors (<16 GDPR / <18) |

#### Sensitivity Classification Levels
| Level | Definition | Masking Requirement |
|-------|------------|---------------------|
| **Critical** | Severe harm if exposed, regulatory breach | SHALL mask in ALL non-production |
| **High** | Substantial harm, privacy violation | SHALL mask in non-production |
| **Medium** | Moderate harm, business impact | SHOULD mask in non-production |
| **Low** | Minimal harm | MAY mask based on risk |
| **Public** | No confidentiality requirement | N/A |

#### Status Legend
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Complete | Inventory complete, classified | Green (C6EFCE) |
| ⚠️ | Partial | Partial inventory/classification | Yellow (FFEB9C) |
| ❌ | Missing | Not inventoried/classified | Red (FFC7CE) |
| 📋 | Planned | Discovery/classification planned | Blue (B4C7E7) |
| N/A | Not Applicable | System contains no sensitive data | Gray |

#### Acceptable Evidence (Examples)
- ✓ Database schema documentation
- ✓ Data dictionaries with field definitions
- ✓ Data discovery tool reports (e.g., BigID, OneTrust, etc.)
- ✓ Data flow diagrams
- ✓ Data Processing Impact Assessments (DPIA)
- ✓ System design documents
- ✓ Privacy policy documentation
- ✓ Data retention schedules
- ✓ Data owner assignment matrices (RACI)
- ✓ Classification review meeting minutes
- ✓ Regulatory compliance assessments
- ✓ Third-party data sharing agreements

---

## Sheet 2: System_Inventory

### Purpose
Document all systems, applications, databases, and data repositories. This is the master list of WHERE data resides.

### Header Section
**Row 1:** "SYSTEM & DATABASE INVENTORY"  
**Row 2:** "List ALL systems that process, store, or transmit data (50 row template)"

**Assessment Question (Row 3):**  
"Does your organization maintain a comprehensive inventory of all systems containing sensitive data?"

**Response Dropdown (Row 4):**  
Options: Yes / No / Partial / Planned / N/A

### Column Headers (Row 6)

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| A | System ID | 15 | Text | Free text (e.g., SYS-001) |
| B | System Name | 25 | Text | Free text |
| C | System Type | 18 | Dropdown | Database, Application, SaaS, File Share, API, Data Warehouse, Backup System, Archive, Other |
| D | Environment | 15 | Dropdown | Production, Development, Test/QA, UAT, Training, Analytics, DR/Backup, Decommissioned |
| E | Contains Sensitive Data? | 18 | Dropdown | Yes, No, Unknown |
| F | Data Categories Present | 25 | Text | Free text (e.g., CAT-PII-D, CAT-FIN) |
| G | Hosting Location | 20 | Dropdown | On-Premises, AWS, Azure, GCP, Multi-Cloud, Hybrid, Third-Party Hosted, Unknown |
| H | Primary Data Owner | 20 | Text | Free text (role or name) |
| I | System Owner/Admin | 20 | Text | Free text |
| J | Inventory Status | 18 | Dropdown | ✅ Complete, ⚠️ Partial, ❌ Missing, 📋 Planned, N/A |
| K | Last Inventory Date | 15 | Date | Date picker |
| L | Next Review Date | 15 | Date | Date picker |
| M | Record Count (Approx) | 15 | Number | Free number |
| N | Retention Period | 15 | Text | Free text (e.g., "7 years") |
| O | Regulatory Scope | 20 | Text | Free text (e.g., GDPR, FADP, HIPAA) |
| P | Decommission Date | 15 | Date | Date picker (if applicable) |
| Q | Notes/Comments | 30 | Text | Free text |

### Data Entry Rows
- **Rows 8-57:** 50 data entry rows (yellow highlighted)
- **Row 7:** Example row (gray, italic) with sample data

### System Inventory Checklist (Starting Row 59)
**Header:** "SYSTEM INVENTORY CHECKLIST"

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is a system inventory maintained? | Dropdown: ✅ / ⚠️ / ❌ / 📋 / N/A | Text | Text |
| 2 | Are all production systems documented? | Dropdown | Text | Text |
| 3 | Are non-production environments included? | Dropdown | Text | Text |
| 4 | Are SaaS/cloud systems included? | Dropdown | Text | Text |
| 5 | Are backup/archive systems included? | Dropdown | Text | Text |
| 6 | Are data warehouses/analytics systems included? | Dropdown | Text | Text |
| 7 | Is system type classified for each entry? | Dropdown | Text | Text |
| 8 | Is hosting location documented? | Dropdown | Text | Text |
| 9 | Are system owners assigned? | Dropdown | Text | Text |
| 10 | Are data owners assigned? | Dropdown | Text | Text |
| 11 | Is inventory reviewed quarterly? | Dropdown | Text | Text |
| 12 | Are decommissioned systems tracked? | Dropdown | Text | Text |
| 13 | Is record count estimated per system? | Dropdown | Text | Text |
| 14 | Is retention period documented? | Dropdown | Text | Text |
| 15 | Are regulatory requirements mapped? | Dropdown | Text | Text |

### Reference Table: System Types (Starting Row 76)
**Header:** "SYSTEM TYPE DEFINITIONS"

| System Type | Description | Examples |
|-------------|-------------|----------|
| Database | Relational or NoSQL databases | Oracle, PostgreSQL, MongoDB, SQL Server |
| Application | Business applications | CRM, ERP, HR systems, custom apps |
| SaaS | Cloud-based software services | Salesforce, Workday, ServiceNow |
| File Share | File storage systems | SharePoint, NAS, file servers |
| API | API gateways and services | REST APIs, integration platforms |
| Data Warehouse | Analytics and BI systems | Snowflake, Redshift, BigQuery |
| Backup System | Backup and recovery systems | Veeam, backup appliances |
| Archive | Long-term storage | Tape systems, cold storage |
| Other | Other system types | (Document in notes) |

---

## Sheet 3: Data_Category_Reference

### Purpose
Reference table defining the organization's sensitive data taxonomy. Read-only informational sheet.

### Header Section
**Row 1:** "SENSITIVE DATA CATEGORY REFERENCE"  
**Row 2:** "Reference taxonomy from ISMS-POL-A.8.11-S2.1"

### Data Category Table (Starting Row 4)

| Column | Header | Width |
|--------|--------|-------|
| A | Category ID | 15 |
| B | Category Name | 25 |
| C | Description | 40 |
| D | Examples | 50 |
| E | Sensitivity Level | 15 |
| F | Masking Priority | 18 |
| G | Regulatory Driver | 25 |

### Data Rows (Pre-populated from Policy S2.1)

**CAT-PII-D: Direct Personal Identifiers**
- Full Name, SSN/AHV, Passport, Driver's License, Email, Phone, Address, Photo, National ID
- Sensitivity: High / Critical
- Masking: Required
- Regulations: FADP, GDPR

**CAT-PII-I: Indirect Personal Identifiers**
- DOB+ZIP, Job Title+Department, Employee ID
- Sensitivity: Medium / High
- Masking: Required when combined

**CAT-FIN: Financial Data**
- PAN (Credit Card), CVV (never store), IBAN, Account Balance, Salary, Tax ID
- Sensitivity: Critical
- Masking: Required
- Regulations: PCI-DSS, FADP, GDPR

**CAT-HLT: Health Data**
- Medical Record Number, Diagnoses, Medications, Lab Results, Insurance ID, Mental Health Records
- Sensitivity: Critical
- Masking: Required
- Regulations: FADP, GDPR Article 9

**CAT-CRD: Credentials**
- Passwords, Password Hashes, API Keys, OAuth Tokens, Private Keys, DB Connection Strings
- Sensitivity: Critical
- Masking: Required (Never display/log)

**CAT-PRP: Proprietary Data**
- Trade Secrets, Pricing Models, Strategic Plans, Source Code
- Sensitivity: High
- Masking: Recommended

**CAT-LOC: Location Data**
- GPS Coordinates, IP Addresses, Travel History
- Sensitivity: Medium / High
- Masking: Recommended
- Regulations: GDPR (personal location)

**CAT-BIO: Biometric Data**
- Fingerprints, Facial Geometry, Voice Prints, Retina Scans
- Sensitivity: Critical
- Masking: Required
- Regulations: GDPR Article 9

**CAT-GEN: Genetic Data**
- DNA Sequences, Genetic Test Results, Hereditary Information
- Sensitivity: Critical
- Masking: Required
- Regulations: GDPR Article 9

**CAT-CHD: Child Data**
- Any PII of minors (<16 GDPR / <18 local)
- Sensitivity: Critical
- Masking: Required
- Regulations: GDPR Article 8, COPPA (US)

---

## Sheet 4: Sensitive_Data_Inventory

### Purpose
Field-level inventory of sensitive data elements. This is WHERE sensitive data exists (database, table, field level).

### Header Section
**Row 1:** "SENSITIVE DATA ELEMENT INVENTORY"  
**Row 2:** "Document sensitive data at the table/field level (100 row template)"

**Assessment Question (Row 3):**  
"Has your organization identified all sensitive data fields across systems?"

**Response Dropdown (Row 4):**  
Options: Yes / No / Partial / Planned / N/A

### Column Headers (Row 6)

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| A | Data Element ID | 15 | Text | Free text (e.g., DE-001) |
| B | System Name | 25 | Text | Lookup from System_Inventory |
| C | Database/Schema | 20 | Text | Free text |
| D | Table/Collection Name | 25 | Text | Free text |
| E | Field/Column Name | 25 | Text | Free text |
| F | Data Type | 15 | Dropdown | String, Integer, Date, Boolean, Binary, JSON, Other |
| G | Data Category | 15 | Dropdown | CAT-PII-D, CAT-PII-I, CAT-FIN, CAT-HLT, CAT-CRD, CAT-PRP, CAT-LOC, CAT-BIO, CAT-GEN, CAT-CHD |
| H | Specific PII Type | 20 | Dropdown | Name, SSN, Email, Phone, Address, DOB, PAN, Medical Record, Password, IP Address, Other |
| I | Sensitivity Level | 15 | Dropdown | Critical, High, Medium, Low, Public |
| J | Contains PII? | 12 | Dropdown | Yes, No |
| K | Regulatory Scope | 20 | Text | Free text (GDPR, FADP, HIPAA, PCI-DSS) |
| L | Masking Required? | 15 | Dropdown | Yes, No, Conditional, Unknown |
| M | Current Masking Status | 18 | Dropdown | Masked, Not Masked, Partially Masked, Encrypted, Planned |
| N | Record Count (Approx) | 15 | Number | Free number |
| O | Data Owner | 20 | Text | Free text |
| P | Discovery Method | 18 | Dropdown | Automated Scan, Schema Review, Manual Sample, Data Owner Interview, Unknown |
| Q | Discovery Date | 15 | Date | Date picker |
| R | Notes/Comments | 30 | Text | Free text |

### Data Entry Rows
- **Rows 8-107:** 100 data entry rows (yellow highlighted)
- **Row 7:** Example row (gray, italic)

### Sensitive Data Inventory Checklist (Starting Row 109)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is sensitive data identified at field level? | Dropdown: ✅ / ⚠️ / ❌ / 📋 / N/A | Text | Text |
| 2 | Are all production databases inventoried? | Dropdown | Text | Text |
| 3 | Are non-production environments inventoried? | Dropdown | Text | Text |
| 4 | Is PII specifically flagged? | Dropdown | Text | Text |
| 5 | Are special category data (GDPR Art.9) identified? | Dropdown | Text | Text |
| 6 | Is financial data (PCI scope) identified? | Dropdown | Text | Text |
| 7 | Are credentials/secrets identified? | Dropdown | Text | Text |
| 8 | Is data category assigned per field? | Dropdown | Text | Text |
| 9 | Is sensitivity level assigned? | Dropdown | Text | Text |
| 10 | Is masking requirement determined? | Dropdown | Text | Text |
| 11 | Is current masking status documented? | Dropdown | Text | Text |
| 12 | Are record counts estimated? | Dropdown | Text | Text |
| 13 | Is data ownership assigned? | Dropdown | Text | Text |
| 14 | Is discovery method documented? | Dropdown | Text | Text |
| 15 | Are regulatory requirements mapped? | Dropdown | Text | Text |
| 16 | Is inventory updated within 30 days of changes? | Dropdown | Text | Text |
| 17 | Is automated discovery used where feasible? | Dropdown | Text | Text |
| 18 | Are discovery results validated manually? | Dropdown | Text | Text |

---

## Sheet 5: Classification_Matrix

### Purpose
Map data elements to organizational classification levels and masking requirements.

### Header Section
**Row 1:** "DATA CLASSIFICATION MATRIX"  
**Row 2:** "Map data sensitivity to organizational classification scheme"

**Assessment Question (Row 3):**  
"Does your organization classify sensitive data according to an established taxonomy?"

**Response Dropdown (Row 4):**  
Options: Yes / No / Partial / Planned / N/A

### Classification Summary Table (Rows 6-12)

| Organizational Class | Typical Sensitivity | Data Categories | Masking Requirement | Count of Fields |
|---------------------|--------------------|-----------------|--------------------|-----------------|
| Restricted | Critical | CAT-HLT, CAT-BIO, CAT-GEN, CAT-FIN (PAN) | Mandatory in ALL non-prod | =COUNTIF() |
| Confidential | High | CAT-PII-D, CAT-FIN, CAT-CRD | Mandatory in non-prod | =COUNTIF() |
| Internal | Medium | CAT-PII-I, CAT-PRP, CAT-LOC | Risk-based masking | =COUNTIF() |
| Public | Low/None | Non-sensitive data | No masking required | =COUNTIF() |

### Classification Assignment Table (Starting Row 14)

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Data Element ID | 15 | Lookup from Sensitive_Data_Inventory |
| B | System Name | 25 | Auto-populate |
| C | Field Name | 25 | Auto-populate |
| D | Data Category | 15 | Auto-populate |
| E | Sensitivity Level | 15 | Auto-populate |
| F | Organizational Classification | 20 | Dropdown: Restricted / Confidential / Internal / Public |
| G | Masking Requirement | 18 | Auto-calculate based on classification |
| H | Classification Rationale | 30 | Text |
| I | Classified By | 20 | Text |
| J | Classification Date | 15 | Date |
| K | Last Review Date | 15 | Date |
| L | Next Review Date | 15 | Auto-calculate (+365 days) |

**Rows 15-114:** 100 classification rows

### Classification Checklist (Starting Row 116)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is organizational classification scheme defined? | Dropdown: ✅ / ⚠️ / ❌ / 📋 / N/A | Text | Text |
| 2 | Are all sensitive fields classified? | Dropdown | Text | Text |
| 3 | Is classification aligned with data categories? | Dropdown | Text | Text |
| 4 | Are masking requirements derived from classification? | Dropdown | Text | Text |
| 5 | Is classification rationale documented? | Dropdown | Text | Text |
| 6 | Are classifiers identified per field? | Dropdown | Text | Text |
| 7 | Is classification reviewed annually? | Dropdown | Text | Text |
| 8 | Are regulatory overrides documented? | Dropdown | Text | Text |
| 9 | Is reclassification process defined? | Dropdown | Text | Text |
| 10 | Are classification changes tracked? | Dropdown | Text | Text |

---

## Sheet 6: Regulatory_Mapping

### Purpose
Map data elements to applicable regulatory requirements (GDPR, FADP, HIPAA, PCI-DSS, etc.).

### Header Section
**Row 1:** "REGULATORY REQUIREMENT MAPPING"  
**Row 2:** "Map data to applicable privacy and security regulations"

**Assessment Question (Row 3):**  
"Has your organization identified which data is subject to specific regulatory requirements?"

**Response Dropdown (Row 4):**  
Options: Yes / No / Partial / Planned / N/A

### Regulatory Summary Table (Rows 6-13)

| Regulation | Applicability | Data Categories in Scope | Field Count | Masking Mandated? |
|------------|---------------|-------------------------|-------------|-------------------|
| GDPR (EU) | Dropdown: Yes/No/Conditional | Auto-populate | =COUNTIF() | Yes (Art. 32) |
| FADP (Switzerland) | Dropdown: Yes/No/Conditional | Auto-populate | =COUNTIF() | Yes |
| HIPAA (US - if applicable) | Dropdown: Yes/No/N/A | Auto-populate | =COUNTIF() | Yes |
| PCI-DSS (if processing cards) | Dropdown: Yes/No/N/A | CAT-FIN (PAN) | =COUNTIF() | Yes (Req 3.4) |
| CCPA/CPRA (California) | Dropdown: Yes/No/N/A | Auto-populate | =COUNTIF() | Recommended |
| Other (specify) | Text | Text | Number | Dropdown |

### Detailed Mapping Table (Starting Row 15)

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Data Element ID | 15 | Lookup |
| B | System Name | 25 | Auto-populate |
| C | Field Name | 25 | Auto-populate |
| D | Data Category | 15 | Auto-populate |
| E | GDPR Applicable? | 15 | Dropdown: Yes / No / Unknown |
| F | GDPR Article | 15 | Dropdown: Art. 4 (PII) / Art. 9 (Special) / Art. 32 (Security) / N/A |
| G | FADP Applicable? | 15 | Dropdown: Yes / No / Unknown |
| H | HIPAA Applicable? | 15 | Dropdown: Yes / No / N/A |
| I | PCI-DSS Applicable? | 15 | Dropdown: Yes / No / N/A |
| J | Other Regulations | 20 | Text |
| K | Masking Mandated by Reg? | 18 | Dropdown: Yes / No / Recommended |
| L | Regulatory Reference | 25 | Text (e.g., "GDPR Art.32(1)(a)") |
| M | Compliance Deadline | 15 | Date |
| N | Notes | 30 | Text |

**Rows 16-115:** 100 mapping rows

### Regulatory Compliance Checklist (Starting Row 117)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Are applicable regulations identified? | Dropdown: ✅ / ⚠️ / ❌ / 📋 / N/A | Text | Text |
| 2 | Is GDPR applicability determined? | Dropdown | Text | Text |
| 3 | Is FADP applicability determined? | Dropdown | Text | Text |
| 4 | Is HIPAA applicability determined (if US)? | Dropdown | Text | Text |
| 5 | Is PCI-DSS applicability determined? | Dropdown | Text | Text |
| 6 | Are GDPR special categories (Art.9) identified? | Dropdown | Text | Text |
| 7 | Is PCI-DSS PAN data identified? | Dropdown | Text | Text |
| 8 | Are masking requirements per regulation documented? | Dropdown | Text | Text |
| 9 | Are regulatory references cited? | Dropdown | Text | Text |
| 10 | Are compliance deadlines tracked? | Dropdown | Text | Text |
| 11 | Is DPO consulted for GDPR scope? | Dropdown | Text | Text |
| 12 | Are cross-border data transfers considered? | Dropdown | Text | Text |

---

## Sheet 7: Data_Owner_Assignment

### Purpose
Assign data ownership and accountability for classification and masking decisions.

### Header Section
**Row 1:** "DATA OWNERSHIP ASSIGNMENT"  
**Row 2:** "Assign data owners per system and data category (ISMS-POL-A.8.11-S3)"

**Assessment Question (Row 3):**  
"Has your organization assigned data owners for all sensitive data categories?"

**Response Dropdown (Row 4):**  
Options: Yes / No / Partial / Planned / N/A

### Ownership Summary by Category (Rows 6-17)

| Data Category | Data Owner (Role) | Data Owner (Name) | Backup Owner | Assignment Date | Last Review |
|---------------|-------------------|-------------------|--------------|-----------------|-------------|
| CAT-PII-D (Direct PII) | Text | Text | Text | Date | Date |
| CAT-PII-I (Indirect PII) | Text | Text | Text | Date | Date |
| CAT-FIN (Financial) | Text | Text | Text | Date | Date |
| CAT-HLT (Health) | Text | Text | Text | Date | Date |
| CAT-CRD (Credentials) | Text | Text | Text | Date | Date |
| CAT-PRP (Proprietary) | Text | Text | Text | Date | Date |
| CAT-LOC (Location) | Text | Text | Text | Date | Date |
| CAT-BIO (Biometric) | Text | Text | Text | Date | Date |
| CAT-GEN (Genetic) | Text | Text | Text | Date | Date |
| CAT-CHD (Child Data) | Text | Text | Text | Date | Date |

### Ownership by System (Starting Row 19)

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | System Name | 25 | Lookup from System_Inventory |
| B | System Owner | 20 | Text |
| C | Primary Data Owner | 20 | Text (responsible for data classification) |
| D | Data Steward | 20 | Text (maintains data quality) |
| E | Business Owner | 20 | Text (business process owner) |
| F | Data Categories in System | 25 | Auto-populate from inventory |
| G | Ownership Documented? | 15 | Dropdown: Yes / No / Partial |
| H | RACI Matrix Reference | 20 | Text (link to RACI doc) |
| I | Assignment Date | 15 | Date |
| J | Last Review Date | 15 | Date |
| K | Next Review Date | 15 | Auto-calculate (+365 days) |
| L | Approval Status | 15 | Dropdown: Approved / Pending / N/A |
| M | Approver | 20 | Text |
| N | Notes | 30 | Text |

**Rows 20-69:** 50 system ownership rows

### Data Owner Responsibilities Table (Starting Row 71)

**Header:** "DATA OWNER RESPONSIBILITIES (Reference)"

| Responsibility | Requirement Level | Policy Reference |
|----------------|-------------------|------------------|
| Approve data classification | SHALL | REQ-CLS-031 |
| Approve masking techniques for their data | SHALL | REQ-CLS-031 |
| Review classification annually | SHALL | REQ-CLS-032 |
| Approve access to unmasked data | SHALL | REQ-ENV-041 |
| Review masking effectiveness | SHOULD | REQ-TST-020 |
| Participate in risk assessments | SHOULD | REQ-GOV-010 |

### Ownership Checklist (Starting Row 79)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Are data owners assigned per category? | Dropdown: ✅ / ⚠️ / ❌ / 📋 / N/A | Text | Text |
| 2 | Are data owners assigned per system? | Dropdown | Text | Text |
| 3 | Are data stewards identified? | Dropdown | Text | Text |
| 4 | Are backup owners assigned? | Dropdown | Text | Text |
| 5 | Is ownership documented in RACI matrix? | Dropdown | Text | Text |
| 6 | Have data owners acknowledged responsibilities? | Dropdown | Text | Text |
| 7 | Are ownership changes tracked? | Dropdown | Text | Text |
| 8 | Is ownership reviewed annually? | Dropdown | Text | Text |
| 9 | Are data owners trained on masking requirements? | Dropdown | Text | Text |
| 10 | Do data owners approve masking techniques? | Dropdown | Text | Text |

---

## Sheet 8: Masking_Priority_Matrix

### Purpose
Risk-based prioritization of masking implementation efforts.

### Header Section
**Row 1:** "MASKING PRIORITY & RISK ASSESSMENT"  
**Row 2:** "Prioritize masking efforts based on risk, compliance, and business impact"

**Assessment Question (Row 3):**  
"Has your organization prioritized masking implementation based on risk assessment?"

**Response Dropdown (Row 4):**  
Options: Yes / No / Partial / Planned / N/A

### Priority Calculation Formula (Rows 6-10)
**Priority Score = (Sensitivity × 3) + (Exposure Risk × 2) + (Regulatory Weight × 2) + (Volume Factor × 1)**

| Factor | Weight | Scoring |
|--------|--------|---------|
| Sensitivity Level | 3x | Critical=5, High=4, Medium=3, Low=2, Public=1 |
| Exposure Risk | 2x | Very High=5, High=4, Medium=3, Low=2, Very Low=1 |
| Regulatory Mandate | 2x | Mandatory=5, Recommended=3, Optional=1 |
| Data Volume | 1x | >1M records=5, 100K-1M=4, 10K-100K=3, 1K-10K=2, <1K=1 |

**Priority Tiers:**
- **P1 (Critical):** Score ≥ 35 — Immediate action required
- **P2 (High):** Score 25-34 — Implement within 3 months
- **P3 (Medium):** Score 15-24 — Implement within 6 months
- **P4 (Low):** Score < 15 — Risk-based timeline

### Priority Assessment Table (Starting Row 12)

| Column | Header | Width | Type | Formula/Validation |
|--------|--------|-------|------|--------------------|
| A | Data Element ID | 15 | Lookup | From Sensitive_Data_Inventory |
| B | System Name | 25 | Auto-populate | |
| C | Field Name | 25 | Auto-populate | |
| D | Data Category | 15 | Auto-populate | |
| E | Sensitivity Score (1-5) | 12 | Auto-populate | Critical=5, High=4, etc. |
| F | Exposure Risk (1-5) | 15 | Dropdown | Very High / High / Medium / Low / Very Low |
| G | Regulatory Score (1-5) | 15 | Auto-calculate | Mandatory=5, Recommended=3, Optional=1 |
| H | Volume Score (1-5) | 12 | Auto-calculate | Based on record count |
| I | **Total Priority Score** | 15 | Formula | =(E×3)+(F×2)+(G×2)+(H×1) |
| J | **Priority Tier** | 12 | Formula | =IF(I≥35,"P1",IF(I≥25,"P2",IF(I≥15,"P3","P4"))) |
| K | Current Masking Status | 18 | Auto-populate | From inventory |
| L | Target Implementation Date | 18 | Date | User input |
| M | Assigned To | 20 | Text | User input |
| N | Implementation Status | 18 | Dropdown | Not Started / In Progress / Complete / Blocked |
| O | Blocking Issues | 25 | Text | If status = Blocked |
| P | Notes | 30 | Text | |

**Rows 13-112:** 100 priority assessment rows

### Priority Summary Dashboard (Starting Row 114)

**Header:** "PRIORITY TIER SUMMARY"

| Priority Tier | Count | % of Total | Avg Score | Complete | In Progress | Not Started |
|---------------|-------|-----------|-----------|----------|-------------|-------------|
| P1 (Critical) | =COUNTIF() | =Formula | =AVERAGEIF() | =COUNTIFS() | =COUNTIFS() | =COUNTIFS() |
| P2 (High) | =COUNTIF() | =Formula | =AVERAGEIF() | =COUNTIFS() | =COUNTIFS() | =COUNTIFS() |
| P3 (Medium) | =COUNTIF() | =Formula | =AVERAGEIF() | =COUNTIFS() | =COUNTIFS() | =COUNTIFS() |
| P4 (Low) | =COUNTIF() | =Formula | =AVERAGEIF() | =COUNTIFS() | =COUNTIFS() | =COUNTIFS() |
| **TOTAL** | =SUM() | 100% | =AVERAGE() | =SUM() | =SUM() | =SUM() |

### Priority Checklist (Starting Row 121)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is risk-based prioritization performed? | Dropdown: ✅ / ⚠️ / ❌ / 📋 / N/A | Text | Text |
| 2 | Are sensitivity levels factored into priority? | Dropdown | Text | Text |
| 3 | Is exposure risk assessed per field? | Dropdown | Text | Text |
| 4 | Are regulatory mandates weighted? | Dropdown | Text | Text |
| 5 | Is data volume considered? | Dropdown | Text | Text |
| 6 | Are P1 items addressed immediately? | Dropdown | Text | Text |
| 7 | Are target dates assigned per priority? | Dropdown | Text | Text |
| 8 | Are responsible parties assigned? | Dropdown | Text | Text |
| 9 | Is implementation status tracked? | Dropdown | Text | Text |
| 10 | Are blocking issues documented? | Dropdown | Text | Text |

---

## Sheet 9: Gap_Analysis

### Purpose
Identify systems/data without proper inventory, classification, or masking.

### Header Section
**Row 1:** "DATA INVENTORY & CLASSIFICATION GAP ANALYSIS"  
**Row 2:** "Identify missing inventory, classification, ownership, or masking"

### Gap Summary Table (Rows 4-12)

| Gap Category | Count | % of Total | Risk Level | Remediation Owner | Target Date |
|--------------|-------|-----------|------------|-------------------|-------------|
| Systems not inventoried | =COUNTIF() | Formula | Dropdown: Critical/High/Medium/Low | Text | Date |
| Systems with unknown sensitive data | =COUNTIF() | Formula | Dropdown | Text | Date |
| Fields not classified | =COUNTIF() | Formula | Dropdown | Text | Date |
| Fields without data owner | =COUNTIF() | Formula | Dropdown | Text | Date |
| Regulatory mapping incomplete | =COUNTIF() | Formula | Dropdown | Text | Date |
| Masking required but not implemented | =COUNTIF() | Formula | Dropdown | Text | Date |
| Masking status unknown | =COUNTIF() | Formula | Dropdown | Text | Date |

### Detailed Gap Register (Starting Row 14)

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Gap ID | 12 | Text (e.g., GAP-001) |
| B | Gap Category | 20 | Dropdown: Inventory Missing / Classification Missing / Ownership Missing / Masking Missing / Regulatory Unknown / Other |
| C | System Name | 25 | Text |
| D | Field/Data Element | 25 | Text (if applicable) |
| E | Gap Description | 35 | Text |
| F | Risk Level | 12 | Dropdown: Critical / High / Medium / Low |
| G | Impact if Not Remediated | 30 | Text |
| H | Root Cause | 25 | Text |
| I | Remediation Action | 30 | Text |
| J | Remediation Owner | 20 | Text |
| K | Target Completion Date | 15 | Date |
| L | Status | 15 | Dropdown: Open / In Progress / Complete / Accepted Risk |
| M | Actual Completion Date | 15 | Date |
| N | Verification Method | 20 | Text |
| O | Notes | 30 | Text |

**Rows 15-74:** 60 gap register rows

### Gap Analysis Checklist (Starting Row 76)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is gap analysis performed quarterly? | Dropdown: ✅ / ⚠️ / ❌ / 📋 / N/A | Text | Text |
| 2 | Are missing inventories identified? | Dropdown | Text | Text |
| 3 | Are unclassified systems identified? | Dropdown | Text | Text |
| 4 | Are fields without owners identified? | Dropdown | Text | Text |
| 5 | Are regulatory gaps documented? | Dropdown | Text | Text |
| 6 | Are masking gaps prioritized? | Dropdown | Text | Text |
| 7 | Are root causes analyzed? | Dropdown | Text | Text |
| 8 | Are remediation actions defined? | Dropdown | Text | Text |
| 9 | Are remediation owners assigned? | Dropdown | Text | Text |
| 10 | Are target dates realistic? | Dropdown | Text | Text |
| 11 | Is gap closure tracked? | Dropdown | Text | Text |
| 12 | Are accepted risks documented? | Dropdown | Text | Text |

---

## Sheet 10: Evidence_Register

### Purpose
Central repository of evidence supporting inventory, classification, and masking decisions.

### Header Section
**Row 1:** "EVIDENCE REGISTER"  
**Row 2:** "Audit trail of supporting documentation (100 entry template)"

### Column Headers (Row 4)

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Evidence ID | 12 | Text (EVD-001) |
| B | Evidence Type | 20 | Dropdown: Data Discovery Report / Schema Documentation / DPIA / Data Flow Diagram / Classification Review / RACI Matrix / Meeting Minutes / Approval Email / Tool Report / Other |
| C | Evidence Title | 30 | Text |
| D | Related System(s) | 25 | Text |
| E | Related Requirement(s) | 20 | Text (REQ-CLS-xxx) |
| F | Related Sheet/Assessment | 20 | Text |
| G | Evidence Location | 30 | Text (file path, URL, document ID) |
| H | Evidence Date | 15 | Date |
| I | Evidence Owner | 20 | Text |
| J | Retention Period | 15 | Text |
| K | Review Frequency | 15 | Dropdown: Annual / Semi-Annual / Quarterly / As-Needed / N/A |
| L | Last Reviewed Date | 15 | Date |
| M | Next Review Date | 15 | Auto-calculate |
| N | Confidentiality Level | 15 | Dropdown: Public / Internal / Confidential / Restricted |
| O | Access Restrictions | 25 | Text |
| P | Notes | 30 | Text |

**Rows 5-104:** 100 evidence rows (yellow highlighted)

### Evidence Types Reference (Starting Row 106)

| Evidence Type | Description | Typical Retention |
|---------------|-------------|-------------------|
| Data Discovery Report | Automated or manual data discovery results | 3 years |
| Schema Documentation | Database schemas, data dictionaries | Current + 1 year |
| DPIA | Data Protection Impact Assessments | 3 years post-processing |
| Data Flow Diagram | How data moves between systems | Current + 2 years |
| Classification Review | Annual classification review records | 3 years |
| RACI Matrix | Responsibility assignments | Current + 1 year |
| Meeting Minutes | Classification meetings, approvals | 3 years |
| Approval Email | Data owner approvals, sign-offs | 3 years |
| Tool Report | Reports from discovery/masking tools | 1 year |

---

## Sheet 11: Summary_Dashboard

### Purpose
Executive summary with KPIs, coverage metrics, and compliance status.

### Header Section
**Row 1:** "DATA INVENTORY & CLASSIFICATION DASHBOARD"  
**Row 2:** "Executive summary with key metrics and compliance status"

### Completion Status Section (Rows 4-9)

| Assessment Area | Total Items | Complete | Partial | Missing | Planned | % Complete |
|-----------------|-------------|----------|---------|---------|---------|------------|
| Systems Inventoried | =COUNTA() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =Formula |
| Sensitive Data Fields | =COUNTA() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =Formula |
| Classification Applied | =COUNTA() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =Formula |
| Regulatory Mapping | =COUNTA() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =Formula |
| Data Ownership | =COUNTA() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =Formula |

### Data Category Coverage (Rows 11-23)

| Data Category | Fields Identified | % of Total | Classified | Owner Assigned | Masking Required | Masking Implemented |
|---------------|-------------------|-----------|------------|----------------|------------------|---------------------|
| CAT-PII-D | =COUNTIF() | =Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() |
| CAT-PII-I | =COUNTIF() | =Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() |
| CAT-FIN | =COUNTIF() | =Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() |
| CAT-HLT | =COUNTIF() | =Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() |
| CAT-CRD | =COUNTIF() | =Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() |
| CAT-PRP | =COUNTIF() | =Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() |
| CAT-LOC | =COUNTIF() | =Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() |
| CAT-BIO | =COUNTIF() | =Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() |
| CAT-GEN | =COUNTIF() | =Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() |
| CAT-CHD | =COUNTIF() | =Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() |
| **TOTAL** | =SUM() | 100% | =SUM() | =SUM() | =SUM() | =SUM() |

### Regulatory Compliance Summary (Rows 25-31)

| Regulation | Applicable? | Fields in Scope | Classified | Owner Assigned | Masking Required | Compliance % |
|------------|-------------|-----------------|------------|----------------|------------------|--------------|
| GDPR | Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =Formula |
| FADP | Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =Formula |
| HIPAA | Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =Formula |
| PCI-DSS | Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =Formula |
| Other | Formula | =COUNTIF() | =COUNTIF() | =COUNTIF() | =COUNTIF() | =Formula |

### Masking Priority Summary (Rows 33-39)

| Priority | Count | % Total | Complete | In Progress | Not Started | Blocked | On-Track? |
|----------|-------|---------|----------|-------------|-------------|---------|-----------|
| P1 (Critical) | =COUNTIF() | =Formula | =COUNTIFS() | =COUNTIFS() | =COUNTIFS() | =COUNTIFS() | Formula |
| P2 (High) | =COUNTIF() | =Formula | =COUNTIFS() | =COUNTIFS() | =COUNTIFS() | =COUNTIFS() | Formula |
| P3 (Medium) | =COUNTIF() | =Formula | =COUNTIFS() | =COUNTIFS() | =COUNTIFS() | =COUNTIFS() | Formula |
| P4 (Low) | =COUNTIF() | =Formula | =COUNTIFS() | =COUNTIFS() | =COUNTIFS() | =COUNTIFS() | Formula |

### Top 10 Gaps (Rows 41-52)

| Rank | Gap ID | Gap Description | Risk Level | Target Date | Owner | Status |
|------|--------|-----------------|------------|-------------|-------|--------|
| 1 | Lookup | Lookup | Lookup | Lookup | Lookup | Lookup |
| ... | | | | | | |

### Key Performance Indicators (Rows 54-65)

| KPI | Current Value | Target | Status | Trend |
|-----|---------------|--------|--------|-------|
| % Systems Inventoried | =Formula | 100% | Conditional: ✅/⚠️/❌ | Text |
| % Sensitive Fields Classified | =Formula | 100% | Conditional | Text |
| % Data Owners Assigned | =Formula | 100% | Conditional | Text |
| % Regulatory Mapping Complete | =Formula | 100% | Conditional | Text |
| % Masking Requirements Defined | =Formula | 100% | Conditional | Text |
| % P1 Items Complete | =Formula | 100% | Conditional | Text |
| Mean Time to Classify (days) | Number | <30 days | Conditional | Text |
| Inventory Accuracy (last audit) | Number | >95% | Conditional | Text |
| Open Critical Gaps | =COUNTIFS() | 0 | Conditional | Text |

### Assessment Sign-Off (Rows 67-75)

| Role | Name | Signature | Date | Comments |
|------|------|-----------|------|----------|
| Data Governance Lead | Text | Text | Date | Text |
| Chief Data Officer (CDO) | Text | Text | Date | Text |
| Data Protection Officer (DPO) | Text | Text | Date | Text |
| Chief Information Security Officer (CISO) | Text | Text | Date | Text |
| Legal/Compliance Officer | Text | Text | Date | Text |

---

## Styling & Formatting Standards

### Color Palette
- **Header (Main):** RGB 0,51,102 (#003366) - Dark Blue, White Text
- **Subheader:** RGB 68,114,196 (#4472C4) - Medium Blue, White Text
- **Column Headers:** RGB 217,217,217 (#D9D9D9) - Light Gray, Black Text
- **Input Cells:** RGB 255,255,204 (#FFFFCC) - Light Yellow
- **Status - Complete/Pass:** RGB 198,239,206 (#C6EFCE) - Light Green
- **Status - Partial/Warning:** RGB 255,235,156 (#FFEB9C) - Light Yellow
- **Status - Missing/Fail:** RGB 255,199,206 (#FFC7CE) - Light Red
- **Status - Planned:** RGB 180,199,231 (#B4C7E7) - Light Blue
- **Info/Example Rows:** RGB 231,230,230 (#E7E6E6) - Light Gray, Italic

### Font Standards
- **Headers:** Calibri 14pt Bold
- **Subheaders:** Calibri 11pt Bold
- **Column Headers:** Calibri 10pt Bold
- **Data Cells:** Calibri 10pt Regular
- **Example Rows:** Calibri 10pt Italic

### Cell Protection
- Lock all cells EXCEPT yellow input cells
- Protect worksheets with password (optional, user configurable)
- Allow filtering and sorting even when protected

### Freeze Panes
- All assessment sheets: Freeze at Row 7 (keep headers visible)
- Summary Dashboard: Freeze at Row 4

---

## Data Validation & Formulas

### Standard Dropdowns
- **Yes/No:** `Yes, No`
- **Yes/No/Partial:** `Yes, No, Partial`
- **Yes/No/Partial/Planned/N/A:** `Yes, No, Partial, Planned, N/A`
- **Yes/No/Unknown:** `Yes, No, Unknown`
- **Status (✅/⚠️/❌/📋/N/A):** `✅ Complete, ⚠️ Partial, ❌ Missing, 📋 Planned, N/A`
- **Risk Level:** `Critical, High, Medium, Low`
- **Priority:** `P1, P2, P3, P4`

### Auto-Calculations
- Percentage formulas: `=ROUND((numerator/denominator)*100,1)`
- Conditional status: `=IF(value>=target,"✅",IF(value>=threshold,"⚠️","❌"))`
- Next review date: `=DATE(YEAR(last_review)+1,MONTH(last_review),DAY(last_review))`
- Priority score: `=(Sensitivity*3)+(ExposureRisk*2)+(RegulatoryWeight*2)+(VolumeScore*1)`

---

## Cell Comments & Help Text

### Key Cells with Comments (Alt Text)
- **System Type:** "Select the primary type. Choose 'Other' if none fit and explain in Notes."
- **Contains Sensitive Data?:** "Select 'Unknown' if data discovery not yet performed."
- **Data Category:** "Use taxonomy from Data_Category_Reference sheet. Multiple categories can be comma-separated."
- **Masking Required?:** "'Conditional' = depends on environment (e.g., required in non-prod, not in prod)."
- **Sensitivity Level:** "Critical = regulatory breach if exposed. See Classification_Matrix for details."
- **Exposure Risk:** "Very High = publicly accessible, no access controls. Very Low = encrypted at rest, strict access."

---

## Workbook Metadata

**File Naming Convention:**  
`ISMS-IMP-A.8.11.1_Data_Inventory_Classification_YYYYMMDD.xlsx`

**Example:**  
`ISMS-IMP-A.8.11.1_Data_Inventory_Classification_20260104.xlsx`

**Excel Properties:**
- **Title:** ISMS-IMP-A.8.11.1 - Data Inventory & Classification Assessment
- **Subject:** ISO/IEC 27001:2022 Control A.8.11 Data Masking
- **Author:** [Organization Name]
- **Company:** [Organization Name]
- **Comments:** Generated from ISMS policy framework. Do not modify structure without updating generator script.

---

## Requirements Traceability

This workbook implements and assesses compliance with:

| Policy Req | Requirement | Assessed In Sheet |
|------------|-------------|-------------------|
| REQ-CLS-001 | Maintain inventory of sensitive data categories | Sensitive_Data_Inventory |
| REQ-CLS-002 | Classify data per organizational scheme | Classification_Matrix |
| REQ-CLS-003 | Document sensitive data locations | System_Inventory, Sensitive_Data_Inventory |
| REQ-CLS-010 | Perform initial data discovery | Sensitive_Data_Inventory (Discovery Method) |
| REQ-CLS-020 | Maintain living inventory | All sheets (Review Dates) |
| REQ-CLS-030 | Assign Data Owner per category | Data_Owner_Assignment |
| REQ-CLS-031 | Data Owner approves masking | Data_Owner_Assignment (Approval Status) |
| REQ-CLS-032 | Annual classification review | Classification_Matrix (Review Dates) |

---

**END OF SPECIFICATION**

*This specification defines the complete structure for workbook ISMS-IMP-A.8.11.1. The Python generator script `generate_a811_1_data_inventory.py` will implement this specification programmatically.*

**Next Steps:**
1. Generate Python script from this specification
2. Execute generator to create Excel workbook
3. Validate generated workbook structure
4. Test with sample data
5. Iterate based on usability feedback

---

**Document Control:**
- **Version:** 1.0
- **Date:** Approval Date
- **Status:** Draft for Implementation
- **Author:** ISMS Implementation Team
- **Approver:** CISO / CDO

---

*"You can't mask what you don't know exists. Start with knowing."*