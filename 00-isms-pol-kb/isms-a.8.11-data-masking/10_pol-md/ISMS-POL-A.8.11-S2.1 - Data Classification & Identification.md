# ISMS-POL-A.8.11-S2.1 — Data Classification & Identification
## What Data Needs Masking?

---

**Document ID**: ISMS-POL-A.8.11-S2.1  
**Title**: Data Classification & Identification Requirements  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Information Security Officer (ISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Data Governance Team / Information Security Manager | Initial section document |

**Review Cycle**: Annual (synchronized with Master Policy review), or upon:
- Introduction of new data types or processing activities
- Changes to data classification scheme
- Regulatory updates affecting data categories  

**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Data Governance: Chief Data Officer (CDO) or Data Governance Manager
- Privacy/Legal: Data Protection Officer (DPO)
- Compliance: Legal/Compliance Officer

**Distribution**: Data owners, data stewards, information security team, development teams  
**Parent Document**: ISMS-POL-A.8.11-S2 - Data Masking Requirements  
**Related Standards**: ISO/IEC 27001:2022 Control A.8.11, GDPR Article 9 (Special Categories), ISO 27701

---

## 1. Purpose

This document defines requirements for identifying and classifying data that requires masking. It answers the fundamental question: **"WHAT data needs masking?"**

Before implementing masking techniques, organizations must know:
- What sensitive data categories exist
- Where sensitive data resides
- Who owns the data
- What regulatory requirements apply

> "You cannot mask what you cannot find, and you cannot protect what you do not know exists."

---

## 2. Sensitive Data Categories

### 2.1 Category Taxonomy

The organization SHALL classify data requiring masking into the following categories:

| Category ID | Category Name | Description | Examples |
|-------------|---------------|-------------|----------|
| **CAT-PII-D** | Direct PII | Data that directly identifies an individual | Name, SSN/AHV, passport number, photo |
| **CAT-PII-I** | Indirect PII | Data that can identify when combined | DOB + ZIP, job title + department |
| **CAT-FIN** | Financial Data | Payment and financial account data | Credit card (PAN), IBAN, account balance |
| **CAT-HLT** | Health Data | Medical and health information | Diagnoses, prescriptions, insurance ID |
| **CAT-CRD** | Credentials | Authentication and access data | Passwords, API keys, tokens, certificates |
| **CAT-PRP** | Proprietary | Business-sensitive information | Trade secrets, pricing, strategies |
| **CAT-LOC** | Location Data | Geographic and tracking data | GPS coordinates, IP addresses, travel history |
| **CAT-BIO** | Biometric Data | Physical/behavioral identifiers | Fingerprints, facial geometry, voice prints |
| **CAT-GEN** | Genetic Data | DNA and genetic information | Genetic test results, hereditary data |
| **CAT-CHD** | Child Data | Data relating to minors | Any PII of persons under 16 (GDPR) / 18 |

### 2.2 Detailed Data Elements

#### CAT-PII-D: Direct Personal Identifiers

| Data Element | Sensitivity | Masking Priority | Regulatory Driver |
|--------------|-------------|------------------|-------------------|
| Full Name | High | Required | FADP, GDPR |
| Social Security / AHV Number | Critical | Required | FADP, GDPR |
| Passport / ID Number | Critical | Required | FADP, GDPR |
| Driver's License Number | High | Required | FADP, GDPR |
| Email Address (personal) | High | Required | FADP, GDPR |
| Phone Number (personal) | High | Required | FADP, GDPR |
| Physical Address | High | Required | FADP, GDPR |
| Photograph / Image | High | Required | FADP, GDPR |
| National ID Numbers | Critical | Required | FADP, GDPR |

#### CAT-FIN: Financial Data

| Data Element | Sensitivity | Masking Priority | Regulatory Driver |
|--------------|-------------|------------------|-------------------|
| Primary Account Number (PAN) | Critical | Required | PCI-DSS 3.4 |
| Card Verification Value (CVV) | Critical | Never Store | PCI-DSS 3.2 |
| Card Expiration Date | High | Required | PCI-DSS |
| PIN / PIN Block | Critical | Never Store | PCI-DSS 3.2 |
| Bank Account Number (IBAN) | High | Required | FADP, GDPR |
| Account Balance | High | Recommended | FADP |
| Transaction History | High | Recommended | FADP |
| Salary / Compensation | High | Required | FADP, GDPR |
| Tax Identification Number | Critical | Required | FADP |

#### CAT-HLT: Health Data

| Data Element | Sensitivity | Masking Priority | Regulatory Driver |
|--------------|-------------|------------------|-------------------|
| Medical Record Number | Critical | Required | FADP, GDPR Art.9 |
| Diagnoses / Conditions | Critical | Required | FADP, GDPR Art.9 |
| Medications / Prescriptions | Critical | Required | FADP, GDPR Art.9 |
| Lab Results | Critical | Required | FADP, GDPR Art.9 |
| Health Insurance ID | High | Required | FADP, GDPR |
| Treatment History | Critical | Required | FADP, GDPR Art.9 |
| Mental Health Records | Critical | Required | FADP, GDPR Art.9 |
| Disability Status | Critical | Required | FADP, GDPR Art.9 |

#### CAT-CRD: Credentials

| Data Element | Sensitivity | Masking Priority | Regulatory Driver |
|--------------|-------------|------------------|-------------------|
| Passwords (any form) | Critical | Never display | Best Practice |
| Password Hashes | Critical | Required | Best Practice |
| API Keys / Secrets | Critical | Required | Best Practice |
| OAuth Tokens | Critical | Required | Best Practice |
| Session Tokens | High | Required | Best Practice |
| Private Keys | Critical | Never expose | Best Practice |
| Database Connection Strings | Critical | Required | Best Practice |
| Service Account Credentials | Critical | Required | Best Practice |

### 2.3 Sensitivity Classification Matrix

| Classification | Definition | Masking Requirement |
|----------------|------------|---------------------|
| **Critical** | Exposure causes severe harm, regulatory breach, or significant financial loss | SHALL be masked in ALL non-production environments |
| **High** | Exposure causes substantial harm or privacy violation | SHALL be masked in non-production; SHOULD be masked where operationally feasible |
| **Medium** | Exposure causes moderate harm or business impact | SHOULD be masked in non-production |
| **Low** | Exposure causes minimal harm | MAY be masked based on risk assessment |
| **Public** | No confidentiality requirement | N/A — no masking required |

---

## 3. Classification Alignment

### 3.1 Organizational Classification Scheme

Data masking requirements SHALL align with the organization's information classification policy (ISMS-POL-A.5.12).

| Org Classification | Typical Sensitivity | Default Masking Requirement |
|--------------------|--------------------|-----------------------------|
| **Restricted** | Critical | Mandatory masking |
| **Confidential** | High | Mandatory masking |
| **Internal** | Medium | Risk-based masking |
| **Public** | Low/None | No masking required |

### 3.2 Regulatory Classification Override

Regulatory requirements MAY override organizational classification:

| Scenario | Action |
|----------|--------|
| Data classified "Internal" but contains PII | Treat as Confidential for masking |
| Data classified "Confidential" but is PAN | Treat as Restricted (PCI-DSS) |
| Data aggregated/anonymized from Restricted | MAY be reclassified if re-identification risk eliminated |

---

## 4. Data Discovery Requirements

### 4.1 Discovery Process

| Req ID | Requirement | Level |
|--------|-------------|-------|
| REQ-CLS-010 | Organization SHALL perform initial data discovery across all systems | SHALL |
| REQ-CLS-011 | Data discovery SHALL identify sensitive data locations | SHALL |
| REQ-CLS-012 | Discovery SHOULD use automated scanning tools where feasible | SHOULD |
| REQ-CLS-013 | Manual discovery SHALL be performed for systems not supporting automation | SHALL |
| REQ-CLS-014 | Discovery results SHALL be documented in data inventory | SHALL |

### 4.2 Discovery Methods

| Method | Description | When to Use |
|--------|-------------|-------------|
| **Automated Scanning** | Tools scan databases, files, logs for patterns (SSN, PAN, email) | Structured data, databases |
| **Metadata Analysis** | Review schema, column names, data dictionaries | Database systems |
| **Data Sampling** | Manual review of representative data samples | Unstructured data, legacy systems |
| **Interview/Survey** | Ask data owners about data handled | New systems, shadow IT discovery |
| **Network Traffic Analysis** | Monitor data flows between systems | Integration points, APIs |

### 4.3 Discovery Frequency

| Trigger | Action |
|---------|--------|
| **Annual** | Full discovery scan of all known systems |
| **Quarterly** | Review and update inventory for changes |
| **New System** | Discovery before production deployment |
| **M&A Activity** | Discovery of acquired systems within 90 days |
| **Incident** | Discovery if data exposure suspected |

---

## 5. Data Inventory Requirements

### 5.1 Inventory Content

The sensitive data inventory SHALL include:

| Field | Description | Required |
|-------|-------------|----------|
| Data Category | From taxonomy (CAT-PII-D, CAT-FIN, etc.) | YES |
| Data Elements | Specific fields/attributes | YES |
| System/Application | Where data resides | YES |
| Database/Table/File | Specific location | YES |
| Data Owner | Accountable individual/role | YES |
| Classification | Organizational classification level | YES |
| Regulatory Scope | Applicable regulations | YES |
| Volume Estimate | Approximate record count | RECOMMENDED |
| Retention Period | How long data is kept | YES |
| Masking Status | Current masking implementation | YES |

### 5.2 Inventory Maintenance

| Req ID | Requirement | Level |
|--------|-------------|-------|
| REQ-CLS-020 | Data inventory SHALL be maintained as a living document | SHALL |
| REQ-CLS-021 | Inventory SHALL be updated within 30 days of system changes | SHALL |
| REQ-CLS-022 | Inventory accuracy SHALL be verified quarterly | SHALL |
| REQ-CLS-023 | Inventory SHOULD be stored in a controlled repository | SHOULD |

---

## 6. Data Ownership & Accountability

### 6.1 Roles

| Role | Responsibility |
|------|----------------|
| **Data Owner** | Accountable for classification and masking decisions for their data |
| **Data Steward** | Maintains data quality and inventory accuracy |
| **System Owner** | Implements masking within their systems |
| **DPO** | Advises on regulatory requirements, validates PII handling |

### 6.2 Ownership Requirements

| Req ID | Requirement | Level |
|--------|-------------|-------|
| REQ-CLS-030 | Every sensitive data category SHALL have an assigned Data Owner | SHALL |
| REQ-CLS-031 | Data Owners SHALL approve masking techniques for their data | SHALL |
| REQ-CLS-032 | Data Owners SHALL review classification annually | SHALL |
| REQ-CLS-033 | Ownership changes SHALL be documented and communicated | SHALL |

---

## 7. Requirements Summary

### 7.1 Complete Requirements List

| Req ID | Requirement | Level | Evidence |
|--------|-------------|-------|----------|
| REQ-CLS-001 | Maintain inventory of sensitive data categories | SHALL | Data inventory |
| REQ-CLS-002 | Classify data according to organizational scheme | SHALL | Classification records |
| REQ-CLS-003 | Document sensitive data locations | SHALL | System mapping |
| REQ-CLS-004 | Perform data discovery at least annually | SHOULD | Discovery reports |
| REQ-CLS-005 | Classify new systems before go-live | SHALL | Go-live checklist |
| REQ-CLS-010 | Perform initial discovery across all systems | SHALL | Discovery report |
| REQ-CLS-011 | Identify sensitive data locations | SHALL | Location inventory |
| REQ-CLS-012 | Use automated scanning where feasible | SHOULD | Tool deployment |
| REQ-CLS-013 | Manual discovery for non-automated systems | SHALL | Manual review records |
| REQ-CLS-014 | Document discovery results | SHALL | Inventory updates |
| REQ-CLS-020 | Maintain living inventory | SHALL | Version history |
| REQ-CLS-021 | Update inventory within 30 days of changes | SHALL | Change records |
| REQ-CLS-022 | Verify inventory accuracy quarterly | SHALL | Review records |
| REQ-CLS-023 | Store inventory in controlled repository | SHOULD | Repository access |
| REQ-CLS-030 | Assign Data Owner per category | SHALL | RACI matrix |
| REQ-CLS-031 | Data Owner approves masking techniques | SHALL | Approval records |
| REQ-CLS-032 | Annual classification review by owner | SHALL | Review records |
| REQ-CLS-033 | Document ownership changes | SHALL | Change log |

---

## 8. Assessment Linkage

### 8.1 Related Assessment Workbook

**ISMS-IMP-A.8.11.1 — Sensitive Data Inventory Assessment**

| Sheet | Content | Requirements Covered |
|-------|---------|---------------------|
| Data_Category_Inventory | List all sensitive data categories | REQ-CLS-001, 002 |
| System_Data_Mapping | Map data to systems/locations | REQ-CLS-003, 011 |
| Discovery_Log | Record discovery activities | REQ-CLS-010, 012, 013 |
| Data_Owner_Register | Document ownership assignments | REQ-CLS-030, 033 |
| Classification_Review | Track classification reviews | REQ-CLS-032 |
| Gap_Analysis | Identify missing coverage | All |
| Evidence_Register | Link to supporting evidence | All |

---

**END OF DOCUMENT**