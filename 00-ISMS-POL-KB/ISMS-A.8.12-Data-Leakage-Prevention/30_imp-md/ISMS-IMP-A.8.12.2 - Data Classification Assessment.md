# ISMS-IMP-A.8.12.2 - Data Classification Assessment

## DOC CONTROL

| **Attribute**           | **Details**                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Document ID**         | ISMS-IMP-A.8.12.2                                                          |
| **Document Title**      | Data Classification Assessment Workbook Specification                       |
| **Control Reference**   | ISO/IEC 27001:2022 - Control A.8.12 (Data Leakage Prevention)             |
| **Related Policy**      | ISMS-POL-A.8.12-S2.1 (Data Classification & Identification Requirements)   |
| **Document Type**       | Implementation Assessment Specification                                     |
| **Version**             | 1.0                                                                        |
| **Status**              | Draft                                                                      |
| **Effective Date**      | Approval Date                                                                 |
| **Review Cycle**        | Quarterly                                                                  |
| **Document Owner**      | Chief Information Security Officer (CISO)                                  |
| **Approved By**         | CISO, CIO, DPO                                                             |
| **Classification**      | Internal Use                                                               |

### Revision History

| **Version** | **Date**   | **Author**        | **Changes**                          |
|-------------|------------|-------------------|--------------------------------------|
| 1.0         | Approval Date | ISMS Project Team | Initial specification for Domain 2   |

### Related Documents

| **Document ID**              | **Title**                                      | **Relationship**        |
|------------------------------|------------------------------------------------|-------------------------|
| ISMS-POL-A.8.12              | Data Leakage Prevention Policy (Master)        | Parent Policy           |
| ISMS-POL-A.8.12-S2.1         | Data Classification & Identification Requirements | Direct Mapping       |
| ISMS-IMP-A.8.12.1            | DLP Infrastructure Assessment                  | Related Assessment      |
| ISMS-IMP-A.8.12.3            | Channel Coverage Assessment                    | Related Assessment      |
| ISMS-IMP-A.8.12.5            | Compliance Dashboard                           | Consolidation Target    |

---

## 1. PURPOSE & SCOPE

### 1.1 Purpose

This document specifies the structure and requirements for the **Data Classification Assessment Workbook**, which evaluates the organization's data classification schema, sensitive data inventory, data labeling methods, and regulatory compliance mapping.

**Assessment Focus:**
- Data classification schema (Public/Internal/Confidential/Restricted)
- Sensitive data categories (PII, financial data, IP, credentials, business confidential)
- Data location inventory (file servers, databases, endpoints, cloud storage)
- Data labeling and marking methods (manual, automated, metadata-based)
- Data ownership assignment (business owners, data stewards)
- Regulatory mapping (FADP, GDPR, PCI-DSS requirements)

### 1.2 Scope

**In Scope:**
- Organizational data classification schema (all classification levels)
- All sensitive data categories requiring DLP protection
- All data storage locations (on-premise, cloud, hybrid)
- Data labeling and classification tools
- Data discovery and scanning results
- Data owner assignments and accountability
- Regulatory data mapping (FADP Articles 4-5, GDPR Articles 4, 9)

**Out of Scope:**
- DLP technology implementation (covered in ISMS-IMP-A.8.12.1)
- Channel-specific DLP policies (covered in ISMS-IMP-A.8.12.3)
- Incident response procedures (covered in ISMS-IMP-A.8.12.4)
- Data retention policies (separate control)

### 1.3 Target Audience

- **Primary:** Data Protection Officer (DPO), Information Security Team, Data Owners
- **Secondary:** CISO, CIO, Compliance Team, Legal Department
- **Reviewers:** Internal Audit, External Auditors, Regulatory Authorities

---

## 2. ASSESSMENT METHODOLOGY

### 2.1 Assessment Approach

**Data-Centric Methodology:**
1. **Schema Definition** - Document organizational classification levels and criteria
2. **Data Discovery** - Identify and inventory all sensitive data types
3. **Location Mapping** - Map sensitive data to storage locations
4. **Ownership Assignment** - Assign data owners and stewards
5. **Regulatory Mapping** - Map data categories to legal requirements
6. **Labeling Assessment** - Evaluate classification marking methods
7. **Gap Identification** - Compare current state vs. policy requirements
8. **Evidence Collection** - Gather proof of data classification implementation

### 2.2 Assessment Frequency

- **Initial Assessment:** Complete baseline within 30 days of policy approval
- **Quarterly Review:** Update data inventory, reassess gaps, validate ownership
- **Ad-Hoc Assessment:** Upon data breach, regulatory audit, or major system changes

### 2.3 Response Values (Standard)

| **Value**   | **Meaning**                                          | **Visual**  |
|-------------|------------------------------------------------------|-------------|
| **Yes**     | Fully implemented, documented, evidence available    | ✅ Green    |
| **No**      | Not implemented, significant gap exists              | ❌ Red      |
| **Partial** | Partially implemented, some gaps remain              | ⚠️ Yellow   |
| **Planned** | Not yet implemented, scheduled with target date      | 📋 Blue     |
| **N/A**     | Not applicable to this organization (justification required) | ⚪ Gray |

**CRITICAL:** "Maybe" is **NOT** a valid response (Feynman says: measure or admit you don't know).

---

## 3. WORKBOOK STRUCTURE

### 3.1 Sheet Overview

| **#** | **Sheet Name**              | **Purpose**                                    | **Rows** |
|-------|-----------------------------|------------------------------------------------|----------|
| 1     | Instructions_Legend         | How to use workbook, legend, metadata         | 50       |
| 2     | Classification_Schema       | Organizational classification levels           | 10       |
| 3     | Sensitive_Data_Inventory    | All sensitive data categories                 | 30       |
| 4     | Data_Location_Mapping       | Where sensitive data resides                  | 40       |
| 5     | Data_Owner_Assignment       | Who owns each data category                   | 30       |
| 6     | Regulatory_Mapping          | FADP/GDPR/PCI-DSS data requirements           | 25       |
| 7     | Labeling_Methods            | Manual/automated classification tools         | 20       |
| 8     | Discovery_Results           | Data discovery scan results                   | 30       |
| 9     | Gap_Analysis                | Identified deficiencies and remediation plans | 40       |
| 10    | Evidence_Register           | Audit trail and evidence tracking             | 100      |
| 11    | Summary_Dashboard           | KPIs, compliance score, executive summary     | 25       |

**Total Assessment Items:** ~70 data classification checkpoints

---

## 4. SHEET SPECIFICATIONS

### 4.1 Sheet: Instructions_Legend

**Purpose:** Provide user guidance and assessment metadata.

**Content Sections:**
1. **Document Header**
   - Workbook ID: ISMS-IMP-A.8.12.2
   - Assessment Area: Data Classification
   - Related Policy: ISMS-POL-A.8.12-S2.1
   - Version: 1.0

2. **Organization Metadata** (Yellow input fields)
   - Assessment Date
   - Completed By
   - Organization Name
   - Review Cycle: Quarterly

3. **How to Use This Workbook**
   - Step-by-step instructions
   - Sheet completion order
   - Data classification principles
   - Evidence ID formatting (e.g., A812-2-CLS-001)

4. **Legend - Response Values**
   - Standard Yes/No/Partial/Planned/N/A legend

5. **Data Classification Levels**
   - Public: Information intended for public disclosure
   - Internal: Information for internal use only
   - Confidential: Sensitive information requiring protection
   - Restricted: Highly sensitive, strictly controlled access

**Layout:** Informational only, no data entry rows.

---

### 4.2 Sheet: Classification_Schema

**Purpose:** Document the organizational data classification schema.

**Columns:**

| **Col** | **Header**                  | **Type**     | **Validation**                     | **Width** |
|---------|-----------------------------|--------------|-------------------------------------|-----------|
| A       | Classification Level        | Text         | Pre-filled (Public/Internal/Confidential/Restricted) | 20 |
| B       | Definition                  | Text         | User input                          | 40        |
| C       | Examples                    | Text         | User input                          | 40        |
| D       | Handling Requirements       | Text         | User input                          | 35        |
| E       | Access Controls             | Text         | User input                          | 30        |
| F       | Encryption Required         | Dropdown     | Yes/No/Partial/N/A                  | 18        |
| G       | DLP Monitoring              | Dropdown     | Yes/No/Partial/Planned/N/A          | 18        |
| H       | Retention Period            | Text         | User input (e.g., 7 years)          | 18        |
| I       | Disposal Method             | Text         | User input                          | 25        |
| J       | Evidence ID                 | Text         | User input                          | 18        |

**Pre-Populated Rows:**

| **Level**      | **Definition**                                           |
|----------------|----------------------------------------------------------|
| Public         | Information approved for public disclosure               |
| Internal       | Information for internal use, no external sharing        |
| Confidential   | Sensitive information, limited internal access           |
| Restricted     | Highly sensitive, need-to-know basis, strict controls    |

**Data Rows:** 4 pre-filled classification levels + 6 blank rows for custom levels

---

### 4.3 Sheet: Sensitive_Data_Inventory

**Purpose:** Inventory all sensitive data categories requiring DLP protection.

**Columns:**

| **Col** | **Header**                  | **Type**     | **Validation**                     | **Width** |
|---------|-----------------------------|--------------|-------------------------------------|-----------|
| A       | Data Category               | Text         | User input                          | 30        |
| B       | Data Type                   | Dropdown     | PII/Financial/IP/Credentials/Business Confidential | 25 |
| C       | Classification Level        | Dropdown     | Public/Internal/Confidential/Restricted | 20    |
| D       | Regulatory Requirement      | Dropdown     | FADP/GDPR/PCI-DSS/Multiple/None     | 20        |
| E       | Data Examples               | Text         | User input                          | 35        |
| F       | Business Owner              | Text         | User input                          | 25        |
| G       | Data Steward                | Text         | User input                          | 25        |
| H       | Estimated Volume            | Text         | User input (records/GB)             | 18        |
| I       | Discovery Status            | Dropdown     | Discovered/In Progress/Not Started  | 18        |
| J       | DLP Protection              | Dropdown     | Yes/No/Partial/Planned/N/A          | 18        |
| K       | Evidence ID                 | Text         | User input                          | 18        |

**Pre-Populated Examples:**

| **Category**              | **Type**     | **Level**      | **Regulatory**  | **Examples**                          |
|---------------------------|--------------|----------------|-----------------|---------------------------------------|
| Personal Names            | PII          | Confidential   | FADP/GDPR       | First name, last name, full name      |
| Email Addresses           | PII          | Confidential   | FADP/GDPR       | john.doe@example.com                  |
| Swiss Social Security (AHV)| PII         | Restricted     | FADP            | 756.1234.5678.90                      |
| Credit Card Numbers       | Financial    | Restricted     | PCI-DSS         | 4111-1111-1111-1111                   |
| Bank Account (IBAN)       | Financial    | Restricted     | FADP/GDPR       | CH93 0076 2011 6238 5295 7           |
| API Keys                  | Credentials  | Restricted     | None            | sk_live_abcd1234efgh5678              |
| Source Code               | IP           | Confidential   | None            | Proprietary algorithms, trade secrets |
| Customer Lists            | Business Confidential | Confidential | FADP/GDPR | CRM exports, contact databases    |
| M&A Documents             | Business Confidential | Restricted | None        | Acquisition targets, financial models |
| Employee Health Records   | PII          | Restricted     | FADP/GDPR       | Medical diagnoses, disability status  |

**Data Rows:** 30 (10 examples + 20 blank)

---

### 4.4 Sheet: Data_Location_Mapping

**Purpose:** Map sensitive data categories to storage locations.

**Columns:**

| **Col** | **Header**                  | **Type**     | **Validation**                     | **Width** |
|---------|-----------------------------|--------------|-------------------------------------|-----------|
| A       | Data Category               | Text         | User input (or dropdown from Inventory) | 30    |
| B       | Storage Location Type       | Dropdown     | File Server/Database/Endpoint/Cloud/Email/Backup | 20 |
| C       | Specific Location           | Text         | User input (server name, DB, cloud service) | 30 |
| D       | Path/Schema                 | Text         | User input (file path, DB schema)   | 35        |
| E       | Estimated Records/Files     | Number       | User input                          | 18        |
| F       | Last Discovery Scan         | Date         | User input                          | 15        |
| G       | DLP Coverage                | Dropdown     | Yes/No/Partial/Planned/N/A          | 18        |
| H       | Encryption at Rest          | Dropdown     | Yes/No/Partial/N/A                  | 18        |
| I       | Access Controls             | Dropdown     | Yes/No/Partial/N/A                  | 18        |
| J       | Data Owner Notified         | Dropdown     | Yes/No/Pending                      | 18        |
| K       | Evidence ID                 | Text         | User input                          | 18        |

**Pre-Populated Examples:**

| **Category**        | **Location Type** | **Specific Location**     | **Path/Schema**         | **Records** |
|---------------------|-------------------|---------------------------|-------------------------|-------------|
| Credit Card Numbers | Database          | SQL-PROD-01               | dbo.Payments.CCNumber   | 250,000     |
| Customer PII        | File Server       | FS-HR-01                  | \\HR\PersonnelFiles\    | 5,000       |
| Source Code         | Cloud             | GitHub Enterprise         | /repos/proprietary/     | 150         |
| API Keys            | Endpoint          | Developer Workstations    | Various local configs   | Unknown     |
| Email Archives      | Email             | M365 Exchange Online      | All mailboxes           | 2,000,000   |

**Data Rows:** 40 (5 examples + 35 blank)

**Key Formula (Summary_Dashboard):**
```excel
Total_Data_Locations = COUNTA(Data_Location_Mapping!$A$6:$A$45) - 5
Locations_With_DLP = COUNTIF(Data_Location_Mapping!$G$6:$G$45,"Yes")
DLP_Coverage_Pct = (Locations_With_DLP / Total_Data_Locations) * 100
```

---

### 4.5 Sheet: Data_Owner_Assignment

**Purpose:** Assign data owners and stewards for accountability.

**Columns:**

| **Col** | **Header**                  | **Type**     | **Validation**                     | **Width** |
|---------|-----------------------------|--------------|-------------------------------------|-----------|
| A       | Data Category               | Text         | User input                          | 30        |
| B       | Business Owner Name         | Text         | User input                          | 25        |
| C       | Business Owner Department   | Text         | User input                          | 20        |
| D       | Business Owner Email        | Text         | User input                          | 30        |
| E       | Data Steward Name           | Text         | User input                          | 25        |
| F       | Data Steward Department     | Text         | User input (usually IT/Security)    | 20        |
| G       | Data Steward Email          | Text         | User input                          | 30        |
| H       | Ownership Documented        | Dropdown     | Yes/No/Pending                      | 18        |
| I       | Owner Training Complete     | Dropdown     | Yes/No/Partial/Planned/N/A          | 18        |
| J       | Last Review Date            | Date         | User input                          | 15        |
| K       | Evidence ID                 | Text         | User input                          | 18        |

**Pre-Populated Examples:**

| **Category**        | **Owner**       | **Dept**  | **Email**                 | **Steward**      |
|---------------------|-----------------|-----------|---------------------------|------------------|
| Customer PII        | Jane Smith      | Sales     | jane.smith@example.com    | John Security    |
| Financial Data      | Robert Johnson  | Finance   | robert.j@example.com      | Mary InfoSec     |
| Source Code         | Alice Developer | R&D       | alice.dev@example.com     | Bob CISO         |

**Data Rows:** 30 (3 examples + 27 blank)

---

### 4.6 Sheet: Regulatory_Mapping

**Purpose:** Map data categories to regulatory requirements.

**Columns:**

| **Col** | **Header**                  | **Type**     | **Validation**                     | **Width** |
|---------|-----------------------------|--------------|-------------------------------------|-----------|
| A       | Data Category               | Text         | User input                          | 30        |
| B       | Regulation                  | Dropdown     | FADP/GDPR/PCI-DSS/HIPAA/SOX/Other   | 20        |
| C       | Specific Article/Section    | Text         | User input (e.g., GDPR Art. 9)      | 25        |
| D       | Requirement Summary         | Text         | User input                          | 40        |
| E       | Compliance Status           | Dropdown     | Compliant/Non-Compliant/Partial/Planned | 18    |
| F       | DLP Controls Required       | Dropdown     | Yes/No/Partial/N/A                  | 18        |
| G       | Breach Notification Required| Dropdown     | Yes/No/N/A                          | 18        |
| H       | Data Subject Rights         | Text         | User input (access, deletion, portability) | 30 |
| I       | Evidence ID                 | Text         | User input                          | 18        |

**Pre-Populated Examples:**

| **Category**           | **Regulation** | **Article**      | **Requirement**                                  |
|------------------------|----------------|------------------|--------------------------------------------------|
| Personal Names         | FADP           | Article 4(1)     | Defined as personal data, requires protection    |
| Special Category PII   | GDPR           | Article 9        | Sensitive data (health, biometric), strict rules |
| Credit Card Numbers    | PCI-DSS        | Requirement 3    | Protect stored cardholder data                   |
| Swiss AHV Number       | FADP           | Article 5        | Special category, heightened protection          |
| Employee Health Data   | FADP/GDPR      | FADP Art 5, GDPR Art 9 | Health data, special category           |

**Data Rows:** 25 (5 examples + 20 blank)

---

### 4.7 Sheet: Labeling_Methods

**Purpose:** Assess data labeling and classification marking methods.

**Columns:**

| **Col** | **Header**                  | **Type**     | **Validation**                     | **Width** |
|---------|-----------------------------|--------------|-------------------------------------|-----------|
| A       | System/Application          | Text         | User input (Office 365, SharePoint) | 25        |
| B       | Labeling Method             | Dropdown     | Manual/Automated/Metadata/None      | 20        |
| C       | Classification Tool         | Text         | User input (AIP, Boldon James)      | 25        |
| D       | Supported Labels            | Text         | User input (Public, Internal, etc.) | 30        |
| E       | User Training Provided      | Dropdown     | Yes/No/Partial/Planned/N/A          | 18        |
| F       | Enforcement Capability      | Dropdown     | Yes/No/Partial/N/A                  | 18        |
| G       | DLP Integration             | Dropdown     | Yes/No/Partial/Planned/N/A          | 18        |
| H       | Adoption Rate %             | Number       | User input (0-100)                  | 15        |
| I       | Evidence ID                 | Text         | User input                          | 18        |

**Pre-Populated Examples:**

| **System**            | **Method**   | **Tool**                      | **Labels**                      | **Adoption %** |
|-----------------------|--------------|-------------------------------|---------------------------------|----------------|
| Microsoft 365         | Automated    | Microsoft Purview (AIP)       | Public, Internal, Confidential  | 85             |
| SharePoint            | Manual       | Built-in Classification       | Public, Internal, Restricted    | 60             |
| File Servers          | None         | None                          | None                            | 0              |
| Email (Outlook)       | Manual       | Azure Information Protection  | All 4 levels                    | 70             |

**Data Rows:** 20 (4 examples + 16 blank)

---

### 4.8 Sheet: Discovery_Results

**Purpose:** Document data discovery and scanning results.

**Columns:**

| **Col** | **Header**                  | **Type**     | **Validation**                     | **Width** |
|---------|-----------------------------|--------------|-------------------------------------|-----------|
| A       | Discovery Tool              | Text         | User input (Spirion, BigID, etc.)   | 25        |
| B       | Scan Target                 | Text         | User input (file server, database)  | 30        |
| C       | Scan Date                   | Date         | User input                          | 15        |
| D       | Data Categories Found       | Text         | User input (PII, Financial, etc.)   | 30        |
| E       | Total Findings              | Number       | User input                          | 15        |
| F       | Critical Findings           | Number       | User input                          | 15        |
| G       | False Positive Rate %       | Number       | User input (0-100)                  | 15        |
| H       | Remediation Status          | Dropdown     | Complete/In Progress/Planned/Not Started | 18   |
| I       | Data Owner Notified         | Dropdown     | Yes/No/Pending                      | 18        |
| J       | Evidence ID                 | Text         | User input                          | 18        |

**Pre-Populated Examples:**

| **Tool**    | **Target**          | **Date**     | **Categories**       | **Findings** | **Critical** | **FP %** |
|-------------|---------------------|--------------|----------------------|--------------|--------------|----------|
| Spirion     | FS-HR-01            | 2024-12-15   | PII, SSN             | 5,243        | 1,200        | 15       |
| BigID       | SQL-PROD-01         | 2024-12-10   | PII, CCN, IBAN       | 250,000      | 50,000       | 5        |
| Manual Audit| SharePoint          | 2024-11-20   | Business Confidential| 1,500        | 300          | 30       |

**Data Rows:** 30 (3 examples + 27 blank)

---

### 4.9 Sheet: Gap_Analysis

**Purpose:** Identify data classification gaps and remediation plans.

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Gap ID                    | Text         | Auto (GAP-A812-2-001)              | 18        |
| B       | Gap Description           | Text         | User input                         | 35        |
| C       | Affected Data Category    | Text         | User input                         | 25        |
| D       | Risk Level                | Dropdown     | Critical/High/Medium/Low           | 15        |
| E       | Business Impact           | Text         | User input                         | 30        |
| F       | Root Cause                | Text         | User input                         | 30        |
| G       | Remediation Plan          | Text         | User input                         | 35        |
| H       | Owner                     | Text         | User input                         | 20        |
| I       | Target Date               | Date         | User input                         | 15        |
| J       | Status                    | Dropdown     | Open/In Progress/Resolved/Closed   | 15        |
| K       | Evidence ID               | Text         | User input                         | 18        |

**Pre-Populated Example Gaps:**

| **Gap ID**        | **Description**                                    | **Risk**  | **Impact**                     |
|-------------------|----------------------------------------------------|-----------|--------------------------------|
| GAP-A812-2-001    | No data classification schema documented           | Critical  | Uncontrolled data handling     |
| GAP-A812-2-002    | PII found on file servers without DLP protection   | High      | Potential FADP/GDPR violation  |
| GAP-A812-2-003    | Data owners not assigned for 40% of data categories| High      | Lack of accountability         |

**Data Rows:** 40 (3 examples + 37 blank)

---

### 4.10 Sheet: Evidence_Register

**Purpose:** Track all evidence collected during assessment.

**Columns:** (Same as Domain 1 - standard across all workbooks)

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Evidence ID               | Text         | User input (A812-2-CLS-001)        | 18        |
| B       | Evidence Type             | Dropdown     | Screenshot/Config/Log/Report/Other | 20        |
| C       | Description               | Text         | User input                         | 35        |
| D       | Location/Link             | Text         | User input (file path/URL)         | 30        |
| E       | Date Collected            | Date         | User input                         | 15        |
| F       | Collected By              | Text         | User input                         | 20        |
| G       | Related Requirement       | Text         | User input (sheet reference)       | 25        |
| H       | Verification Status       | Dropdown     | Verified/Pending/Rejected          | 15        |

**Data Rows:** 100 blank rows

---

### 4.11 Sheet: Summary_Dashboard

**Purpose:** KPIs and compliance scoring for Domain 2.

**Sections:**

#### Section 1: Document Information
- Assessment Date
- Completed By
- DPO Approval Status
- Last Review Date

#### Section 2: Key Performance Indicators

| **KPI**                              | **Formula**                                    | **Target** | **Status** |
|--------------------------------------|------------------------------------------------|------------|------------|
| Classification Schema Documented     | =COUNTIF(Classification_Schema!F4:F10,"Yes")   | 4          | Auto       |
| Sensitive Data Categories Inventoried| =COUNTA(Sensitive_Data_Inventory!A4:A33)-10    | ≥20        | Auto       |
| Data Locations Mapped                | =COUNTA(Data_Location_Mapping!A6:A45)-5        | ≥30        | Auto       |
| Data Owners Assigned %               | =COUNTIF(Data_Owner_Assignment!H4:H33,"Yes")/Total*100 | ≥90% | Auto |
| DLP Protection Coverage %            | =COUNTIF(Sensitive_Data_Inventory!J4:J33,"Yes")/Total*100 | ≥80% | Auto |
| Regulatory Compliance %              | =COUNTIF(Regulatory_Mapping!E4:E28,"Compliant")/Total*100 | ≥90% | Auto |
| Labeling Tool Adoption %             | =AVERAGE(Labeling_Methods!H4:H23)              | ≥75%       | Auto       |
| Data Discovery Coverage %            | =COUNTIF(Discovery_Results!H4:H33,"Complete")/Total*100 | ≥80% | Auto |
| Total Gaps Identified                | =COUNTA(Gap_Analysis!A4:A43)-3                 | ≤10        | Auto       |
| Critical/High Gaps                   | =COUNTIFS(Gap_Analysis!D4:D43,"Critical")+COUNTIFS(Gap_Analysis!D4:D43,"High") | 0 | Auto |
| **Overall Classification Compliance**| =AVERAGE(B7:B16)                               | **≥85%**   | **Auto**   |

#### Section 3: Gap Summary by Risk Level
- Critical, High, Medium, Low counts

#### Section 4: Evidence Completeness
- Evidence items collected, verified, completeness %

#### Section 5: Approval Sign-Off
- DPO, CISO, Legal Counsel

---

## 5. ASSESSMENT CRITERIA & SCORING

### 5.1 Compliance Scoring Method

**Domain 2 Compliance Score** is calculated as:
```
Domain_2_Score = AVERAGE(
    Schema_Documentation_Score,
    Data_Inventory_Completeness,
    Location_Mapping_Coverage,
    Ownership_Assignment_Rate,
    DLP_Protection_Coverage,
    Regulatory_Compliance_Rate,
    Labeling_Adoption_Rate,
    Discovery_Coverage_Rate,
    Gap_Remediation_Rate
)
```

**Maturity Levels:**

| **Score** | **Level**       | **Description**                                |
|-----------|-----------------|------------------------------------------------|
| 90-100%   | Optimized       | Comprehensive classification, minimal gaps     |
| 80-89%    | Managed         | Strong classification, some improvements needed|
| 70-79%    | Defined         | Core classification present, notable gaps      |
| 60-69%    | Developing      | Partial classification, major gaps exist       |
| <60%      | Initial/Ad-Hoc  | Insufficient classification, urgent action     |

### 5.2 Pass/Fail Criteria

**PASS Criteria:**
- ✅ Overall Domain 2 Score ≥ 80%
- ✅ Classification schema documented (4 levels minimum)
- ✅ Data owners assigned ≥ 90%
- ✅ DLP protection coverage ≥ 80%
- ✅ Zero Critical gaps

**FAIL Criteria:**
- ❌ Overall Domain 2 Score < 70%
- ❌ No classification schema
- ❌ Data owners assigned < 70%
- ❌ Critical gaps > 0

---

## 6. COMPLIANCE MAPPING

### 6.1 ISO/IEC 27001:2022 Mapping

| **Control** | **Requirement**                              | **Evidence Location**        |
|-------------|----------------------------------------------|------------------------------|
| A.8.12      | Data leakage prevention (Master)             | All sheets                   |
| A.5.12      | Classification of information                | Classification_Schema        |
| A.5.13      | Labelling of information                     | Labeling_Methods             |
| A.5.14      | Information transfer                         | Data_Location_Mapping        |

### 6.2 Regulatory Mapping

| **Regulation** | **Requirement**                         | **Evidence Location**          |
|----------------|-----------------------------------------|--------------------------------|
| FADP Art. 4    | Definition of personal data             | Sensitive_Data_Inventory       |
| FADP Art. 5    | Special categories of personal data     | Regulatory_Mapping             |
| GDPR Art. 4(1) | Personal data definition                | Sensitive_Data_Inventory       |
| GDPR Art. 9    | Special categories                      | Regulatory_Mapping             |
| PCI-DSS Req 3  | Protect stored cardholder data          | Data_Location_Mapping          |

---

## 7. EVIDENCE REQUIREMENTS

### 7.1 Mandatory Evidence

For EACH data category:
1. **Classification Policy** - Documented schema with definitions
2. **Data Inventory Reports** - Discovery scan results
3. **Ownership Documentation** - Signed data owner assignments
4. **Regulatory Mapping** - Legal opinion or DPO assessment
5. **Labeling Screenshots** - Proof of classification marking
6. **DLP Policy Config** - DLP rules protecting each category

### 7.2 Evidence Naming Convention
```
A812-2-[CATEGORY]-[###]

Examples:
A812-2-CLS-001  (Classification - Schema document)
A812-2-INV-001  (Inventory - Data discovery report)
A812-2-OWN-001  (Ownership - Assignment matrix)
A812-2-REG-001  (Regulatory - FADP compliance mapping)
A812-2-LBL-001  (Labeling - AIP configuration)
```

---

## 8. APPROVAL & SIGN-OFF

### 8.1 Review and Approval Workflow

| **Role**           | **Responsibility**                          | **Timeline**   |
|--------------------|---------------------------------------------|----------------|
| Data Protection Officer | Review regulatory compliance, privacy impact | Week 1-2  |
| Information Security | Validate data classification, DLP coverage | Week 1-2       |
| Data Owners        | Confirm ownership, validate data categories | Week 2         |
| Legal Counsel      | Review regulatory mapping                   | Week 3         |
| CISO               | Approve gaps, remediation plans             | Week 3         |

### 8.2 Sign-Off Section (in Summary_Dashboard)

| **Approver**       | **Name** | **Signature** | **Date** | **Status**          |
|--------------------|----------|---------------|----------|---------------------|
| DPO                | [Input]  | [Input]       | [Auto]   | [Dropdown: Approved/Pending] |
| CISO               | [Input]  | [Input]       | [Auto]   | [Dropdown: Approved/Pending] |
| Legal Counsel      | [Input]  | [Input]       | [Auto]   | [Dropdown: Approved/Pending] |

---

**END OF SPECIFICATION: ISMS-IMP-A.8.12.2**

*"You can't protect what you can't see. You can't see what you haven't classified."*  
— Data Security Proverb (adapted by the Grand Guru)
