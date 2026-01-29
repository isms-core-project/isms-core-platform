# ISMS-IMP-A.8.11.3 - Environment Coverage Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.11.3  
**Assessment Area:** Environment Coverage & Deployment Verification  
**Related Policy:** ISMS-POL-A.8.11-S2.3 - Environment Requirements  
**Purpose:** Assess WHERE data masking is deployed across all organizational environments

**Scope:** This assessment evaluates:
- Environment inventory and classification
- Production environment masking (DDM for role-based access)
- Non-production environment masking (SDM mandatory)
- Analytics and reporting platform masking
- Backup and archive masking requirements
- External data sharing controls
- Cloud environment masking coverage
- Data flow mapping and masking checkpoints

**Assessment Philosophy:**
- **Coverage-focused:** Track masking deployment across ALL environments
- **Vendor-agnostic:** Customers document THEIR environments and solutions
- **Evidence-based:** Link to Evidence Register for audit trail
- **Gap-driven:** Identify unmasked environments requiring remediation

---

## Workbook Structure

### Sheet Overview (12 Sheets)

1. **Instructions_Legend** - User guidance and color coding
2. **Environment_Inventory** - Complete catalog of all environments
3. **Production_Environment** - Production DDM assessment
4. **NonProduction_Environments** - Dev/Test/UAT/Sandbox SDM assessment
5. **Analytics_Reporting** - BI, data warehouse, ML/AI masking
6. **Backup_Archive** - Backup encryption and archive masking
7. **External_Sharing** - Vendor, auditor, customer data sharing
8. **Cloud_Environments** - Cloud-hosted environment masking
9. **Data_Flow_Mapping** - Data flows and masking checkpoints
10. **Gap_Analysis** - Coverage gaps and remediation plan
11. **Evidence_Register** - Supporting documentation (100 rows)
12. **Summary_Dashboard** - Executive overview and KPIs

---

## Standard Column Structure (Sheets 2-9)

### Base Columns (A-Q, 17 columns) - Used across assessment sheets

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| A | Environment Name | 25 | Text | Free text (customer fills in) |
| B | Environment Type | 20 | Dropdown | Production, Development, Testing, UAT, Staging, Training, Sandbox, Analytics, Cloud, Backup, Archive, External |
| C | Classification | 18 | Dropdown | Sensitive, Confidential, Internal, Public |
| D | Hosting Location | 18 | Dropdown | On-Premises, AWS, Azure, GCP, Hybrid, Other Cloud |
| E | Data Sensitivity | 18 | Dropdown | PII, Financial, Health, Credentials, Proprietary, Mixed, None |
| F | Masking Required? | 18 | Dropdown | ✅ Mandatory, ⚠️ Conditional, ❌ Not Required, N/A |
| G | Masking Deployed? | 18 | Dropdown | Yes, No, Partial, Planned, N/A |
| H | Masking Technique | 20 | Dropdown | SDM, DDM, Tokenization, Encryption, Redaction, Substitution, Anonymization, None |
| I | Masking Tool/Solution | 22 | Text | Free text (customer fills in) |
| J | Coverage % | 12 | Percentage | 0-100% |
| K | Last Verified Date | 15 | Date | Date picker |
| L | Environment Owner | 20 | Text | Free text |
| M | Data Owner | 20 | Text | Free text |
| N | Exception Approved? | 15 | Dropdown | Yes, No, N/A |
| O | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| P | Notes/Comments | 30 | Text | Free text |
| Q | Evidence ID | 15 | Text | Link to Evidence Register |

**Note:** Extended columns (R-X) added per sheet as needed for specific assessments.

---

## Cell Styling Reference

### Header Styles
- **Main Header:** Font: Calibri 14pt bold white, Fill: 003366 (dark blue), Centered
- **Subheader:** Font: Calibri 11pt bold white, Fill: 4472C4 (medium blue), Centered
- **Column Header:** Font: Calibri 10pt bold black, Fill: D9D9D9 (light gray), Centered, Wrapped

### Input Cell Styles
- **Fill:** FFFFCC (light yellow) - Indicates user must fill
- **Alignment:** Left for text, center for dropdowns, wrapped text
- **Border:** Thin black on all sides

### Status Color Coding
- **Compliant:** C6EFCE (light green)
- **Partial:** FFEB9C (light yellow)
- **Non-Compliant:** FFC7CE (light red)
- **Planned:** B4C7E7 (light blue)
- **N/A:** White (no fill)

---

## Sheet 1: Instructions_Legend

### Header Section
**Title:** "ISMS Control A.8.11.3 - Environment Coverage Assessment"  
**Subtitle:** "ISO/IEC 27001:2022 - Data Masking Policy Compliance"  
**Styling:** Dark blue header (003366), white text, centered, 40px height

### Document Information Block
```
Document ID:           ISMS-IMP-A.8.11.3
Assessment Area:       Environment Coverage & Deployment
Related Policy:        ISMS-POL-A.8.11-S2.3
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly
```

### How to Use This Workbook (10 instructions)
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

### Color Legend
- 🟨 **Yellow cells** = User input required
- 🟩 **Green status** = Compliant (masking deployed as required)
- 🟨 **Yellow status** = Partial compliance (some masking gaps)
- 🟥 **Red status** = Non-compliant (masking required but not deployed)
- 🟦 **Blue status** = Planned (remediation in progress)

### Environment Classification Reference (Table)

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

### Policy Requirements Summary (15 key points)
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

---

## Sheet 2: Environment_Inventory

### Header
**Title:** "ENVIRONMENT INVENTORY"  
**Policy Reference:** "All information processing environments must be cataloged and classified for masking applicability (ISMS-POL-A.8.11-S2.3 Section 2)"

### Assessment Question (Row 3)
**"Does your organization maintain a complete inventory of ALL environments where data is processed, stored, or transmitted?"**

Response: [Dropdown: Yes / No / Partial / In Progress] (yellow cell B3)

### Column Headers (Row 6) - Standard 17 columns A-Q
[Use standard column structure defined above]

### Data Entry Rows (8-57)
- **50 rows** for environment inventory
- All cells yellow-highlighted (user input)
- Example row (Row 7) in gray italic:
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
  - K7: "2026-01-01"
  - L7: "IT Operations Manager"
  - M7: "Customer Data Owner"
  - N7: "N/A"
  - O7: "✅ Compliant"
  - P7: "DDM applied for CS reps"
  - Q7: "EV-ENV-001"

### Compliance Checklist (Starting Row 60)

**ENVIRONMENT INVENTORY CHECKLIST** (15 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | All production environments documented | [Dropdown] | |
| ☐ | All non-production environments documented (Dev/Test/UAT/Sandbox) | [Dropdown] | |
| ☐ | All analytics/reporting environments documented | [Dropdown] | |
| ☐ | All cloud environments documented (AWS/Azure/GCP/Other) | [Dropdown] | |
| ☐ | All backup/archive systems documented | [Dropdown] | |
| ☐ | External data sharing destinations documented | [Dropdown] | |
| ☐ | Each environment classified (Sensitive/Confidential/Internal/Public) | [Dropdown] | |
| ☐ | Data sensitivity level assigned per environment | [Dropdown] | |
| ☐ | Masking requirement determined (Mandatory/Conditional/Not Required) | [Dropdown] | |
| ☐ | Environment owners assigned | [Dropdown] | |
| ☐ | Data owners assigned | [Dropdown] | |
| ☐ | Hosting location documented (On-Prem/Cloud) | [Dropdown] | |
| ☐ | Environment inventory reviewed in last 6 months | [Dropdown] | |
| ☐ | New environments added to inventory within 30 days of deployment | [Dropdown] | |
| ☐ | Decommissioned environments removed from inventory | [Dropdown] | |

**Status options:** ✅ Complete | ⚠️ Partial | ❌ Missing | N/A

### Reference Table 1: Environment Type Definitions (Starting Row 80)

| Environment Type | Primary Purpose | Typical Users | Data Refresh Frequency |
|-----------------|-----------------|---------------|----------------------|
| Production | Live business operations | End users, authorized staff | Real-time |
| Development | Software coding and development | Developers, DevOps | Weekly/Monthly |
| Testing/QA | Quality assurance testing | QA testers, developers | Weekly |
| UAT | Business user validation | Business analysts, end users | Monthly |
| Staging | Pre-production deployment testing | DevOps, release managers | Per release |
| Training | Employee training | Trainers, new employees | Quarterly |
| Sandbox | Experimental work, POCs | Data scientists, architects | Ad-hoc |
| Analytics | Business intelligence, reporting | Analysts, executives | Daily/Weekly |
| Cloud | Third-party hosted environments | Varies by cloud service | Varies |
| Backup | Disaster recovery, business continuity | Backup admins | Daily/Weekly |
| Archive | Long-term regulatory retention | Compliance officers | Annual |
| External | Data shared with vendors/partners | External parties | Per agreement |

---

## Sheet 3: Production_Environment

### Header
**Title:** "PRODUCTION ENVIRONMENT ASSESSMENT"  
**Policy Reference:** "Production environments may use Dynamic Data Masking (DDM) for role-based access. All access to unmasked data must be logged. (ISMS-POL-A.8.11-S2.3 Section 3.1)"

### Assessment Question (Row 3)
**"Does your organization implement role-based masking (DDM) in production environments to restrict access to sensitive data?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 24 columns (A-X)

Base columns A-Q (standard), plus extended columns:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | User Role/Group | 20 | Text | Free text |
| S | Masked Fields | 25 | Text | Free text (list of fields) |
| T | Unmasked Access Logged? | 15 | Dropdown | Yes, No, N/A |
| U | Access Control Method | 20 | Dropdown | RBAC, ABAC, ACL, Manual, None |
| V | Exception Justification | 30 | Text | Free text |
| W | Risk Level | 12 | Dropdown | High, Medium, Low, None |
| X | Remediation Target Date | 15 | Date | Date picker |

### Data Entry Rows (8-37)
- **30 rows** for production environment assessment
- Yellow-highlighted cells for user input
- Example row (Row 7): Production CRM with DDM for customer service reps

### Compliance Checklist (Starting Row 40)

**PRODUCTION ENVIRONMENT CHECKLIST** (18 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | DDM implemented for role-based access in production | [Dropdown] | |
| ☐ | Customer service representatives see masked customer data | [Dropdown] | |
| ☐ | Production reports mask data for non-privileged users | [Dropdown] | |
| ☐ | Audit logs containing sensitive data are masked/encrypted | [Dropdown] | |
| ☐ | Application outputs (invoices, statements) use partial redaction | [Dropdown] | |
| ☐ | Production data exports are masked before release | [Dropdown] | |
| ☐ | All access to unmasked production data is logged | [Dropdown] | |
| ☐ | Access logs reviewed monthly for anomalies | [Dropdown] | |
| ☐ | Privileged user access to unmasked data requires justification | [Dropdown] | |
| ☐ | Masking exceptions documented with business justification | [Dropdown] | |
| ☐ | Exception approvals obtained from Data Owner and ISO | [Dropdown] | |
| ☐ | Exceptions reviewed quarterly | [Dropdown] | |
| ☐ | DDM performance impact assessed (<10% degradation acceptable) | [Dropdown] | |
| ☐ | DDM rules tested before production deployment | [Dropdown] | |
| ☐ | DDM bypass mechanisms disabled or strictly controlled | [Dropdown] | |
| ☐ | Production masking coverage measured and tracked | [Dropdown] | |
| ☐ | Coverage target: ≥90% of sensitive fields masked for non-privileged users | [Dropdown] | |
| ☐ | Regulatory reporting requirements accommodate masking | [Dropdown] | |

### Reference Table 1: Production Masking Use Cases (Starting Row 65)

| Use Case | Masking Technique | Example |
|----------|-------------------|---------|
| Customer service rep viewing customer record | DDM | Show only last 4 digits of SSN/CC |
| Manager viewing employee salary report | DDM | Show salary ranges instead of exact amounts |
| Audit log entries with PII | Field-level encryption or redaction | Hash or redact usernames |
| Invoice generation for end customer | Partial redaction | Show full account number to customer |
| Internal invoice report | DDM | Mask account numbers for unauthorized viewers |
| Production database export for analysis | Static masking before export | Apply SDM before copying to analytics |

---

## Sheet 4: NonProduction_Environments

### Header
**Title:** "NON-PRODUCTION ENVIRONMENTS ASSESSMENT"  
**Policy Reference:** "ALL sensitive data SHALL be masked before deployment to non-production. NO production data SHALL be copied without masking. (ISMS-POL-A.8.11-S2.3 Section 3.2)"

### Assessment Question (Row 3)
**"Are ALL non-production environments (Dev/Test/UAT/Training/Sandbox/Staging) masked before receiving production data?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 24 columns (A-X)

Base columns A-Q, plus:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Data Refresh Frequency | 18 | Dropdown | Daily, Weekly, Monthly, Quarterly, Ad-hoc, Never |
| S | Masking Applied During Refresh? | 18 | Dropdown | Yes, No, N/A |
| T | Direct Prod Clone Prevented? | 18 | Dropdown | Yes, No, N/A |
| U | Masking Validation Method | 22 | Text | Free text |
| V | Last Data Refresh Date | 15 | Date | Date picker |
| W | Next Planned Refresh | 15 | Date | Date picker |
| X | Refresh Process Owner | 20 | Text | Free text |

### Data Entry Rows (8-37)
- **30 rows** for non-production environment assessment
- Yellow cells for user input

### Compliance Checklist (Starting Row 40)

**NON-PRODUCTION ENVIRONMENT CHECKLIST** (20 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | Development environments masked | [Dropdown] | |
| ☐ | Testing/QA environments masked | [Dropdown] | |
| ☐ | UAT environments masked | [Dropdown] | |
| ☐ | Training environments masked | [Dropdown] | |
| ☐ | Sandbox environments masked | [Dropdown] | |
| ☐ | Staging environments masked (unless prod-identical required) | [Dropdown] | |
| ☐ | Static Data Masking (SDM) applied during data refresh | [Dropdown] | |
| ☐ | Masking applied BEFORE data deployment (not "later") | [Dropdown] | |
| ☐ | Direct production database cloning prevented | [Dropdown] | |
| ☐ | Automated masking integrated into data refresh pipeline | [Dropdown] | |
| ☐ | Manual data copies prohibited without masking | [Dropdown] | |
| ☐ | Developer NDA reliance eliminated (NDAs not technical controls) | [Dropdown] | |
| ☐ | Non-production data refresh process documented | [Dropdown] | |
| ☐ | Masking validation performed after each refresh | [Dropdown] | |
| ☐ | Non-production exception count: ___ (Target: 0) | [Dropdown] | |
| ☐ | Exceptions approved by ISO and Data Owner | [Dropdown] | |
| ☐ | Compensating controls implemented for exceptions | [Dropdown] | |
| ☐ | Exception review conducted quarterly | [Dropdown] | |
| ☐ | Coverage target: 100% of non-prod environments masked | [Dropdown] | |
| ☐ | Non-compliance escalated to CISO | [Dropdown] | |

### Reference Table 1: Prohibited Practices (Starting Row 65)

| Prohibited Practice | Why It's Prohibited | Correct Approach |
|---------------------|---------------------|------------------|
| Direct prod DB clone without masking | Exposes real sensitive data in less secure environments | Apply SDM during clone/refresh process |
| "We'll mask it later" approach | Creates window of exposure; often forgotten | Mask BEFORE deployment to non-prod |
| "It's only test data" excuse | Test data is often production copy | Treat all non-prod data as requiring masking |
| Relying on developer NDAs | NDAs are legal, not technical controls | Implement technical masking controls |
| Manual masking processes | Error-prone, inconsistent, not auditable | Automate masking in data pipelines |
| Copying unmasked prod to laptop for testing | High risk of data loss/theft | Use centralized masked environments |

---

## Sheet 5: Analytics_Reporting

### Header
**Title:** "ANALYTICS & REPORTING ENVIRONMENTS ASSESSMENT"  
**Policy Reference:** "Individual-level PII SHALL be masked or aggregated. Synthetic data SHALL be used for ML/AI training. Re-identification risk SHALL be assessed. (ISMS-POL-A.8.11-S2.3 Section 3.3)"

### Assessment Question (Row 3)
**"Are analytics, BI, data warehouse, and ML/AI environments masked to prevent individual-level data exposure?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 24 columns (A-X)

Base columns A-Q, plus:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Analytics Platform Type | 22 | Dropdown | BI Tool, Data Warehouse, Data Lake, ML Platform, Reporting, Other |
| S | Aggregation Level | 18 | Dropdown | Individual, Group, Department, Organization, N/A |
| T | Re-ID Risk Assessed? | 15 | Dropdown | Yes, No, N/A |
| U | Re-ID Risk Level | 15 | Dropdown | High, Medium, Low, None |
| V | Synthetic Data Used? | 15 | Dropdown | Yes, No, N/A |
| W | Data Export Controls | 22 | Dropdown | Masked, Aggregated, Restricted, None |
| X | Self-Service BI Masking | 18 | Dropdown | Enforced, Not Enforced, N/A |

### Data Entry Rows (8-37)
- **30 rows** for analytics/reporting assessment

### Compliance Checklist (Starting Row 40)

**ANALYTICS & REPORTING CHECKLIST** (15 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | BI tool exports contain masked data | [Dropdown] | |
| ☐ | Data warehouse ETL includes masking steps | [Dropdown] | |
| ☐ | Individual-level reports use masked data | [Dropdown] | |
| ☐ | Aggregated reports assessed for re-identification risk | [Dropdown] | |
| ☐ | ML/AI training datasets use synthetic or masked data | [Dropdown] | |
| ☐ | PII removed or anonymized in training data | [Dropdown] | |
| ☐ | Ad-hoc query exports masked | [Dropdown] | |
| ☐ | Self-service BI tools enforce masking rules | [Dropdown] | |
| ☐ | CSV/Excel exports contain masked data | [Dropdown] | |
| ☐ | Analytics platform integrates masking at data ingestion | [Dropdown] | |
| ☐ | Data minimization applied (only export necessary fields) | [Dropdown] | |
| ☐ | Re-identification risk assessed before data release | [Dropdown] | |
| ☐ | Historical analytics data masked or aggregated | [Dropdown] | |
| ☐ | Analytics data retention period documented | [Dropdown] | |
| ☐ | Analytics environment access logged | [Dropdown] | |

---

## Sheet 6: Backup_Archive

### Header
**Title:** "BACKUP & ARCHIVE ENVIRONMENTS ASSESSMENT"  
**Policy Reference:** "Production backups may contain unmasked data if encrypted. Non-production backups SHALL contain only masked data. (ISMS-POL-A.8.11-S2.3 Section 3.4)"

### Assessment Question (Row 3)
**"Are backup and archive environments encrypted and access-controlled? Are non-production backups masked?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 24 columns (A-X)

Base columns A-Q, plus:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Backup Type | 18 | Dropdown | Full, Incremental, Differential, Snapshot, Archive |
| S | Encryption Enabled? | 15 | Dropdown | Yes, No, N/A |
| T | Encryption Method | 20 | Dropdown | AES-256, AES-128, Other, None |
| U | Access Control | 18 | Dropdown | RBAC, MFA Required, Logged, None |
| V | Restoration Process | 22 | Text | Free text |
| W | Masking on Restore? | 18 | Dropdown | Yes (if to non-prod), No, N/A |
| X | Backup Retention Period | 15 | Text | Free text (e.g., "90 days") |

### Data Entry Rows (8-37)
- **30 rows** for backup/archive assessment

### Compliance Checklist (Starting Row 40)

**BACKUP & ARCHIVE CHECKLIST** (12 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | Production backups encrypted at rest | [Dropdown] | |
| ☐ | Backup encryption uses strong algorithms (AES-256) | [Dropdown] | |
| ☐ | Backup access restricted to authorized administrators only | [Dropdown] | |
| ☐ | All backup access logged | [Dropdown] | |
| ☐ | Non-production backups contain only masked data | [Dropdown] | |
| ☐ | Backup restoration to non-prod triggers masking process | [Dropdown] | |
| ☐ | Archive data assessed for masking feasibility | [Dropdown] | |
| ☐ | If masking compromises compliance, encryption used instead | [Dropdown] | |
| ☐ | Archive access strictly controlled | [Dropdown] | |
| ☐ | Backup media stored securely (encrypted, access-controlled) | [Dropdown] | |
| ☐ | Backup retention policy documented | [Dropdown] | |
| ☐ | Backup testing includes masking validation | [Dropdown] | |

---

## Sheet 7: External_Sharing

### Header
**Title:** "EXTERNAL DATA SHARING ASSESSMENT"  
**Policy Reference:** "ALL data shared externally SHALL be masked unless contractually required. Data Processing Agreements SHALL specify masking. (ISMS-POL-A.8.11-S2.3 Section 3.5)"

### Assessment Question (Row 3)
**"Is data shared with vendors, partners, auditors, or customers masked unless contractually required to be unmasked?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 24 columns (A-X)

Base columns A-Q, plus:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Recipient Type | 20 | Dropdown | Vendor, Partner, Auditor, Customer, Regulator, Other |
| S | Data Sharing Purpose | 25 | Text | Free text |
| T | DPA in Place? | 15 | Dropdown | Yes, No, N/A |
| U | DPA Specifies Masking? | 18 | Dropdown | Yes, No, N/A |
| V | Contractual Exception? | 18 | Dropdown | Yes, No, N/A |
| W | Recipient Security Audit Date | 15 | Date | Date picker |
| X | Data Minimization Applied? | 18 | Dropdown | Yes, No, N/A |

### Data Entry Rows (8-37)
- **30 rows** for external sharing assessment

### Compliance Checklist (Starting Row 40)

**EXTERNAL SHARING CHECKLIST** (15 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | Vendor data shares masked unless contractually required | [Dropdown] | |
| ☐ | Data Processing Agreements (DPAs) in place | [Dropdown] | |
| ☐ | DPAs specify masking requirements | [Dropdown] | |
| ☐ | Vendor access to unmasked data logged and monitored | [Dropdown] | |
| ☐ | Vendor environments audited for security controls | [Dropdown] | |
| ☐ | Customer exports appropriately masked (not their own data) | [Dropdown] | |
| ☐ | Auditor data samples masked where possible | [Dropdown] | |
| ☐ | Auditors sign confidentiality agreements | [Dropdown] | |
| ☐ | Partner data sharing follows minimum necessary principle | [Dropdown] | |
| ☐ | Data minimization applied (only share necessary fields) | [Dropdown] | |
| ☐ | External sharing inventory maintained | [Dropdown] | |
| ☐ | Re-identification risk assessed before external release | [Dropdown] | |
| ☐ | External sharing reviewed annually | [Dropdown] | |
| ☐ | Data retention limits specified in agreements | [Dropdown] | |
| ☐ | Data deletion verified after contract termination | [Dropdown] | |

---

## Sheet 8: Cloud_Environments

### Header
**Title:** "CLOUD ENVIRONMENTS ASSESSMENT"  
**Policy Reference:** "Cloud environments SHALL follow same masking requirements as on-premises. Cloud-hosted non-prod SHALL be masked. (ISMS-POL-A.8.11-S2.3 Section 2.6)"

### Assessment Question (Row 3)
**"Are cloud-hosted environments (AWS/Azure/GCP/Other) masked according to the same requirements as on-premises environments?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 24 columns (A-X)

Base columns A-Q, plus:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Cloud Provider | 18 | Dropdown | AWS, Azure, GCP, Oracle Cloud, IBM Cloud, Other |
| S | Cloud Service Type | 20 | Dropdown | IaaS, PaaS, SaaS, DBaaS, Other |
| T | Region/Geography | 18 | Text | Free text (e.g., "EU-West-1") |
| U | Client-Side Masking? | 18 | Dropdown | Yes (before upload), No, N/A |
| V | Cloud-Native Masking Tool | 22 | Text | Free text |
| W | Multi-Tenancy Concerns? | 18 | Dropdown | Yes, No, N/A |
| X | Data Residency Compliance | 22 | Dropdown | Compliant, Non-Compliant, N/A |

### Data Entry Rows (8-37)
- **30 rows** for cloud environment assessment

### Compliance Checklist (Starting Row 40)

**CLOUD ENVIRONMENT CHECKLIST** (12 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | Cloud environments classified correctly (Prod/Non-Prod/Analytics) | [Dropdown] | |
| ☐ | Cloud-hosted production follows production masking rules | [Dropdown] | |
| ☐ | Cloud-hosted non-prod follows non-prod masking rules (mandatory) | [Dropdown] | |
| ☐ | Cloud analytics follows analytics masking rules | [Dropdown] | |
| ☐ | Client-side masking applied before cloud upload (where applicable) | [Dropdown] | |
| ☐ | Cloud provider security controls reviewed | [Dropdown] | |
| ☐ | Cloud provider SLAs reviewed for data protection | [Dropdown] | |
| ☐ | Multi-tenancy risks assessed and mitigated | [Dropdown] | |
| ☐ | Data residency requirements met | [Dropdown] | |
| ☐ | Cloud encryption enabled (at rest and in transit) | [Dropdown] | |
| ☐ | Cloud access controls configured (IAM, RBAC) | [Dropdown] | |
| ☐ | Cloud environment masking tested and validated | [Dropdown] | |

---

## Sheet 9: Data_Flow_Mapping

### Header
**Title:** "DATA FLOW MAPPING & MASKING CHECKPOINTS"  
**Policy Reference:** "Data flows SHALL be documented with masking checkpoints identified at each environment boundary. (ISMS-POL-A.8.11-S2.3 Section 3)"

### Assessment Question (Row 3)
**"Are data flows documented with masking checkpoints identified at each environment boundary?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 24 columns (A-X)

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| A | Data Flow Name | 25 | Text | Free text |
| B | Source Environment | 20 | Text | Free text |
| C | Destination Environment | 20 | Text | Free text |
| D | Data Type | 18 | Dropdown | PII, Financial, Health, Credentials, Proprietary, Mixed |
| E | Masking Checkpoint? | 18 | Dropdown | Yes, No, N/A |
| F | Masking Technique | 20 | Dropdown | SDM, DDM, Tokenization, Encryption, Redaction, None |
| G | Flow Frequency | 15 | Dropdown | Real-time, Hourly, Daily, Weekly, Monthly, Ad-hoc |
| H | Automated Masking? | 18 | Dropdown | Yes (automated), No (manual), N/A |
| I | Masking Tool/Script | 22 | Text | Free text |
| J | Masking Validation | 20 | Text | Free text (how validated) |
| K | Last Flow Date | 15 | Date | Date picker |
| L | Flow Owner | 20 | Text | Free text |
| M | Approval Required? | 15 | Dropdown | Yes, No, N/A |
| N | Approval Status | 18 | Dropdown | Approved, Pending, Denied, N/A |
| O | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| P | Risk Level | 12 | Dropdown | High, Medium, Low, None |
| Q | Notes/Comments | 30 | Text | Free text |
| R | Evidence ID | 15 | Text | Link to Evidence Register |

### Data Entry Rows (8-37)
- **30 rows** for data flow mapping

### Compliance Checklist (Starting Row 40)

**DATA FLOW MAPPING CHECKLIST** (10 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | All production → non-production flows documented | [Dropdown] | |
| ☐ | Masking checkpoints identified at environment boundaries | [Dropdown] | |
| ☐ | Data refresh processes documented | [Dropdown] | |
| ☐ | Automated masking integrated into data pipelines | [Dropdown] | |
| ☐ | Manual data transfers prohibited or strictly controlled | [Dropdown] | |
| ☐ | End-to-end masking verified for each flow | [Dropdown] | |
| ☐ | Data flow inventory reviewed quarterly | [Dropdown] | |
| ☐ | New data flows assessed for masking requirements | [Dropdown] | |
| ☐ | Data flow exceptions approved by ISO | [Dropdown] | |
| ☐ | High-risk flows (unmasked external sharing) escalated | [Dropdown] | |

---

## Sheet 10: Gap_Analysis

### Header
**Title:** "GAP ANALYSIS & REMEDIATION PLAN"  
**Policy Reference:** "All coverage gaps must be identified, risk-assessed, and remediated per organizational risk tolerance."

### Column Headers (Row 3)

| Column | Header | Width |
|--------|--------|-------|
| A | Gap ID | 12 |
| B | Environment/System | 25 |
| C | Gap Description | 35 |
| D | Current State | 25 |
| E | Target State | 25 |
| F | Risk Level | 12 |
| G | Impact | 25 |
| H | Remediation Action | 35 |
| I | Owner | 20 |
| J | Target Date | 15 |
| K | Status | 15 |
| L | Evidence ID | 15 |

### Data Entry Rows (5-44)
- **40 rows** for gap analysis
- Auto-populated from other sheets where Compliance Status = "Non-Compliant" or "Partial"

### Summary Metrics (Starting Row 50)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Environments Inventoried | [Formula] | N/A | |
| Environments Requiring Masking | [Formula] | | |
| Environments with Masking Deployed | [Formula] | | |
| Coverage Percentage | [Formula] | 100% | |
| Total Gaps Identified | [Formula] | 0 | |
| High-Risk Gaps | [Formula] | 0 | |
| Medium-Risk Gaps | [Formula] | | |
| Low-Risk Gaps | [Formula] | | |
| Gaps Remediated | [Formula] | | |
| Gaps In Progress | [Formula] | | |
| Gaps Not Started | [Formula] | | |
| Average Days to Remediation | [Formula] | ≤90 days | |

---

## Sheet 11: Evidence_Register

### Header
**Title:** "EVIDENCE REGISTER"  
**Subtitle:** "Supporting documentation for all environment coverage assessments"

### Column Headers (Row 3)

| Column | Header | Width |
|--------|--------|-------|
| A | Evidence ID | 15 |
| B | Evidence Type | 20 |
| C | Description | 35 |
| D | Related Environment | 25 |
| E | Document Name/Link | 30 |
| F | Date Created | 15 |
| G | Owner | 20 |
| H | Retention Period | 15 |
| I | Location | 25 |
| J | Notes | 30 |

### Data Entry Rows (5-104)
- **100 rows** for evidence documentation

### Evidence Type Reference (Row 110)

Common evidence types:
- Environment Inventory Report
- Masking Configuration Screenshot
- Masking Validation Report
- Data Refresh Procedure Document
- Access Control Policy
- Encryption Certificate
- DPA/Contract Excerpt
- Audit Log Sample
- Risk Assessment Document
- Exception Approval Form

---

## Sheet 12: Summary_Dashboard

### Header
**Title:** "ENVIRONMENT COVERAGE - EXECUTIVE SUMMARY DASHBOARD"

### Section 1: Compliance Summary Table (Rows 3-12)

| Assessment Area | Total Envs | Compliant | Partial | Non-Compliant | N/A | Coverage % |
|-----------------|-----------|-----------|---------|---------------|-----|------------|
| Production Environments | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| Non-Production Environments | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| Analytics & Reporting | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| Backup & Archive | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| External Sharing | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| Cloud Environments | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| Data Flow Mapping | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| **OVERALL TOTAL** | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |

### Section 2: Key Performance Indicators (Starting Row 16)

| KPI | Current Value | Target | Status |
|-----|---------------|--------|--------|
| Non-Production Masking Coverage | [Formula] | 100% | [Conditional Format] |
| Production DDM Coverage (role-based) | [Formula] | ≥90% | [Conditional Format] |
| Analytics Masking Coverage | [Formula] | 100% | [Conditional Format] |
| External Sharing Masking Coverage | [Formula] | 100% | [Conditional Format] |
| Cloud Environment Compliance | [Formula] | 100% | [Conditional Format] |
| Data Flow Mapping Completeness | [Formula] | 100% | [Conditional Format] |
| Exception Count (Total) | [Formula] | ≤5% of envs | [Conditional Format] |
| High-Risk Gaps | [Formula] | 0 | [Conditional Format] |
| Average Remediation Time (days) | [Formula] | ≤90 | [Conditional Format] |
| Evidence Documentation Rate | [Formula] | 100% | [Conditional Format] |

### Section 3: Critical Gaps (Starting Row 30)

| Priority | Environment | Gap Description | Risk Level | Owner | Target Date | Status |
|----------|-------------|-----------------|------------|-------|-------------|--------|
| P1 | [Auto from Gap Analysis] | [Auto] | [Auto] | [Auto] | [Auto] | [Auto] |
| P1 | [Auto] | [Auto] | [Auto] | [Auto] | [Auto] | [Auto] |
| ... | ... | ... | ... | ... | ... | ... |

(Top 10 gaps auto-populated)

### Section 4: Environment Type Breakdown (Starting Row 45)

| Environment Type | Count | Masked | Unmasked | Coverage % |
|-----------------|-------|--------|----------|------------|
| Production | [Formula] | [Formula] | [Formula] | [Formula] |
| Development | [Formula] | [Formula] | [Formula] | [Formula] |
| Testing | [Formula] | [Formula] | [Formula] | [Formula] |
| UAT | [Formula] | [Formula] | [Formula] | [Formula] |
| Analytics | [Formula] | [Formula] | [Formula] | [Formula] |
| Cloud | [Formula] | [Formula] | [Formula] | [Formula] |
| Backup | [Formula] | [Formula] | [Formula] | [Formula] |
| External | [Formula] | [Formula] | [Formula] | [Formula] |

### Section 5: Hosting Location Breakdown (Starting Row 58)

| Hosting Location | Count | Masked | Coverage % |
|-----------------|-------|--------|------------|
| On-Premises | [Formula] | [Formula] | [Formula] |
| AWS | [Formula] | [Formula] | [Formula] |
| Azure | [Formula] | [Formula] | [Formula] |
| GCP | [Formula] | [Formula] | [Formula] |
| Other Cloud | [Formula] | [Formula] | [Formula] |
| Hybrid | [Formula] | [Formula] | [Formula] |

### Section 6: Masking Technique Distribution (Starting Row 67)

| Masking Technique | Usage Count | % of Total |
|-------------------|-------------|------------|
| Static Data Masking (SDM) | [Formula] | [Formula] |
| Dynamic Data Masking (DDM) | [Formula] | [Formula] |
| Tokenization | [Formula] | [Formula] |
| Encryption | [Formula] | [Formula] |
| Redaction | [Formula] | [Formula] |
| Anonymization | [Formula] | [Formula] |
| None (Unmasked) | [Formula] | [Formula] |

### Section 7: Compliance Trend (Starting Row 78)

| Month | Total Envs | Compliant | Coverage % |
|-------|-----------|-----------|------------|
| [Manual entry] | [Manual] | [Manual] | [Manual] |
| [Manual entry] | [Manual] | [Manual] | [Manual] |
| ... | ... | ... | ... |

(6-month trend tracking)

### Section 8: Overall Security Score (Starting Row 90)

**Weighted Compliance Score:**
- Non-Production Coverage (30%): [Formula]
- Production DDM Coverage (20%): [Formula]
- Analytics Coverage (15%): [Formula]
- External Sharing Coverage (15%): [Formula]
- Cloud Coverage (10%): [Formula]
- Evidence Documentation (10%): [Formula]

**TOTAL SCORE: [Weighted Average Formula] / 100**

**Color Coding:**
- Green (≥90): Excellent compliance
- Yellow (70-89): Acceptable with gaps
- Red (<70): Significant gaps requiring immediate action

---

## Implementation Notes

### Python Generator Requirements

1. **Sheet Creation:** All 12 sheets with exact names
2. **Styling:** Consistent color scheme (dark blue headers, yellow input cells)
3. **Data Validation:** Dropdowns for all specified columns
4. **Formulas:** Summary Dashboard formulas linking to assessment sheets
5. **Freeze Panes:** Freeze at row 7 (assessment sheets), row 4 (dashboard)
6. **Pre-Population:**
   - Environment type reference tables
   - Example rows (gray italic)
   - Checklist items
   - Evidence types
7. **Row Counts:**
   - Environment Inventory: 50 rows
   - Production: 30 rows
   - Non-Production: 30 rows
   - Analytics: 30 rows
   - Backup: 30 rows
   - External Sharing: 30 rows
   - Cloud: 30 rows
   - Data Flow: 30 rows
   - Gap Analysis: 40 rows
   - Evidence Register: 100 rows

### Assessment Totals
- **Total checklist items:** ~117 items across all sheets
- **Total assessment rows:** 300+ environment assessment entries possible
- **Evidence capacity:** 100 evidence items

---

**END OF SPECIFICATION**