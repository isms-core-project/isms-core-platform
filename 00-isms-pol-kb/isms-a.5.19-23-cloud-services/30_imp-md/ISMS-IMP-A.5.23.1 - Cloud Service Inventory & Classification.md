# ISMS-IMP-A.5.23.1 - Cloud Service Inventory & Classification
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.5.23: Information security for use of cloud services

---

## Document Overview

**Document ID:** ISMS-IMP-A.5.23.1  
**Assessment Area:** Cloud Service Inventory & Classification  
**Related Policy:** ISMS-POL-A.5.19-23-S5, ISMS-POL-A.5.19-23-S6  
**Purpose:** Maintain authoritative inventory of all cloud services with data classification, criticality assessment, and exit feasibility analysis

---

## Workbook Structure

### Sheet 1: Instructions & Legend

#### Header Section
- **Title:** "ISMS-IMP-A.5.23.1 – Cloud Service Inventory & Classification"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.5.23: Information security for use of cloud services"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block
```
Document ID:           ISMS-IMP-A.5.23.1
Assessment Area:       Cloud Service Inventory & Classification
Related Policy:        ISMS-POL-A.5.19-23-S5
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly
```

#### How to Use This Workbook
1. Complete each worksheet tab (2–7) for all cloud services in use
2. Use dropdown menus for standardized entries (Service Type, Criticality, Status, etc.)
3. Fill in yellow-highlighted cells with your information
4. If Status = Partial or Non-Compliant, complete the Gap Description and Remediation sections
5. Document all cloud services including SaaS, IaaS, PaaS, security services, and storage
6. Provide evidence location/path for each service entry
7. Summary Dashboard auto-calculates compliance statistics per service category
8. Maintain the Evidence Register for audit traceability
9. Obtain final approval and sign-off in the Approval Sign-Off sheet

#### Status Legend
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Compliant | Fully meets inventory & classification requirements | Green (C6EFCE) |
| ⚠️ | Partial | Some requirements met, gaps exist | Yellow (FFEB9C) |
| ❌ | Non-Compliant | Does not meet policy requirements | Red (FFC7CE) |
| N/A | Not Applicable | Requirement does not apply to this service | Gray |

#### Acceptable Evidence (Examples)
- ✓ Procurement records (purchase orders, invoices)
- ✓ Contract documents (MSA, SOW, SLA)
- ✓ Service catalog entries
- ✓ Configuration management database (CMDB) exports
- ✓ Asset inventory reports
- ✓ Financial system exports (monthly costs, annual spend)
- ✓ User license reports
- ✓ Data flow diagrams
- ✓ Data classification matrices
- ✓ Criticality assessment worksheets
- ✓ Business impact analysis (BIA) reports
- ✓ Exit feasibility studies
- ✓ Alternative vendor analysis

---

## Assessment Sheets (2-7) - Standard Column Layout

### Common Column Structure for Cloud Service Inventory

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| A | Cloud Service Name | 30 | Text | Free text |
| B | Service Type | 22 | Dropdown | SaaS, IaaS, PaaS, Security Service, Cloud Storage, Collaboration, Other |
| C | Vendor Name | 25 | Text | Free text (e.g., Microsoft, AWS, Google, CrowdStrike) |
| D | Service Criticality | 20 | Dropdown | Critical, High, Medium, Low |
| E | Data Classification | 22 | Dropdown | Public, Internal, Confidential, Restricted, Mixed, N/A |
| F | Data Residency Region | 22 | Dropdown | Switzerland, EU, USA, Global/Multi-Region, Unknown |
| G | Contract Status | 20 | Dropdown | Active, Renewal Due (≤90 days), Expired, Under Negotiation, Trial |
| H | Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| I | Evidence Location | 30 | Text | Free text (file path, SharePoint link, CMDB ID) |
| J | Gap Description | 35 | Text | Free text |
| K | Remediation Needed | 16 | Dropdown | Yes, No |
| L | Exception ID | 14 | Text | Free text (links to exception register) |
| M | Risk ID | 14 | Text | Free text (links to risk register) |
| N | Compensating Controls | 35 | Text | Free text |
| O | Service Owner | 22 | Text | Free text (person responsible) |
| P | Target Remediation Date | 18 | Date | Date picker |
| Q | Budget Impact | 18 | Dropdown | High (>$50K), Medium ($10K-$50K), Low (<$10K), None |

### Extended Columns for Inventory (R-X)

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Monthly Cost (CHF) | 18 | Number | Numeric validation (≥0) |
| S | Annual Contract Value | 20 | Formula | =R*12 (auto-calculated) |
| T | Number of Licensed Users | 18 | Number | Numeric validation (≥0) |
| U | Integration Count | 16 | Number | Numeric validation (≥0) |
| V | Backup Service Available | 20 | Dropdown | Yes, No, Planned, Unknown |
| W | Exit Feasibility | 18 | Dropdown | Easy (≤30 days), Medium (31-90 days), Hard (>90 days), Unknown |
| X | Last Inventory Review | 18 | Date | Date picker |

---

## Sheet 2: SaaS Services

### Row 1: Section Header
- **Merged cells A1:X1**
- **Content:** "SAAS SERVICES INVENTORY\nPolicy Requirement: All SaaS applications must be documented in CMDB with data classification (Policy S5 Section 2.1)"
- **Styling:** Dark blue background (003366), white bold text, centered, 40px height

### Row 3: Assessment Question
- **Merged cells A3:X3**
- **Content:** "Does your organization use Software-as-a-Service (SaaS) applications for business operations?"
- **Styling:** Bold, 11pt, left-aligned, wrap text, 30px height

### Row 4: Response Dropdown
- **Cell A4:** "Response:"
- **Cell B4:** Dropdown with validation: Yes, No, Partial, Under Review
- **Styling:** Yellow background for B4 (user input)

### Row 6: Column Headers
- **Columns A-X** as defined in Common Column Structure above
- **Styling:** Gray background (D9D9D9), bold, centered, borders, wrap text

### Rows 8-50: Data Entry Area
- **43 rows** for SaaS service entries
- **Yellow cells** in columns requiring user input (A, B, C, D, E, F, G, I, J, O, P, R, T, U, V, W, X)
- **Formula cells** in column S (Annual Contract Value = Monthly Cost * 12)
- **Status column H** with conditional formatting:
  - ✅ Compliant → Green fill
  - ⚠️ Partial → Yellow fill
  - ❌ Non-Compliant → Red fill
  - N/A → Gray fill

### Example Pre-Populated Row (Row 8 - Example)
| Column | Value |
|--------|-------|
| A | Microsoft 365 (Office 365) |
| B | SaaS |
| C | Microsoft Corporation |
| D | Critical |
| E | Confidential |
| F | EU |
| G | Active |
| H | ✅ Compliant |
| I | CMDB-ID-12345, Contract-MS-2024 |
| J | (empty - compliant) |
| K | No |
| L | (empty) |
| M | RISK-CLOUD-001 |
| N | (empty) |
| O | John Smith (IT Manager) |
| P | (empty - no remediation needed) |
| Q | High (>$50K) |
| R | 8500 |
| S | =R8*12 (102,000) |
| T | 150 |
| U | 5 |
| V | Yes |
| W | Medium (31-90 days) |
| X | 2025-12-15 |

### Checklist Section (Below Data Entry)

**Row 52:** Header "SAAS SERVICES COMPLIANCE CHECKLIST" (merged A52:X52, bold, blue background)

**Rows 54-65:** Checklist items

| Item | Requirement | Status | Evidence |
|------|-------------|--------|----------|
| ☐ | All SaaS applications documented in CMDB | ✅/⚠️/❌ | CMDB export, asset report |
| ☐ | Data classification assigned to each service | ✅/⚠️/❌ | Data classification matrix |
| ☐ | Service criticality assessed (BIA performed) | ✅/⚠️/❌ | Business impact analysis |
| ☐ | Service owner identified and documented | ✅/⚠️/❌ | RACI matrix, org chart |
| ☐ | Contract status tracked (renewal dates) | ✅/⚠️/❌ | Contract management system |
| ☐ | Monthly costs documented | ✅/⚠️/❌ | Finance system, invoices |
| ☐ | User license count verified | ✅/⚠️/❌ | License management report |
| ☐ | Integration dependencies mapped | ✅/⚠️/❌ | Architecture diagram, CMDB |
| ☐ | Backup/redundancy strategy defined | ✅/⚠️/❌ | BC/DR plan |
| ☐ | Exit feasibility evaluated | ✅/⚠️/❌ | Exit strategy document |
| ☐ | Data residency requirements verified | ✅/⚠️/❌ | Vendor documentation, DPA |
| ☐ | Last inventory review date recorded | ✅/⚠️/❌ | Audit log, review calendar |

---

## Sheet 3: IaaS/PaaS Services

### Section Header
"IAAS/PAAS SERVICES INVENTORY\nPolicy Requirement: All infrastructure and platform services must maintain security baselines and configuration management (Policy S5 Section 2.2)"

### Assessment Question
"Does your organization use Infrastructure-as-a-Service (IaaS) or Platform-as-a-Service (PaaS) offerings?"

### Column Structure
Same as Sheet 2 (Columns A-X with identical definitions)

### Example Services
- Amazon Web Services (AWS) - EC2, S3, RDS
- Microsoft Azure - Virtual Machines, Azure SQL
- Google Cloud Platform (GCP) - Compute Engine, Cloud Storage
- Oracle Cloud Infrastructure (OCI)
- IBM Cloud
- DigitalOcean
- Heroku (PaaS)
- Red Hat OpenShift (PaaS)

### Checklist Items (IaaS/PaaS Specific)
| Item | Requirement |
|------|-------------|
| ☐ | Infrastructure inventory maintained with configuration baselines |
| ☐ | Security groups/firewalls documented |
| ☐ | Auto-scaling policies reviewed for cost control |
| ☐ | Reserved instances vs. on-demand tracked |
| ☐ | API access keys rotated quarterly |
| ☐ | Infrastructure-as-Code (IaC) templates stored in version control |
| ☐ | Disaster recovery region configured |
| ☐ | Compute/storage resources tagged for cost allocation |
| ☐ | Compliance requirements (GDPR, HIPAA) mapped to services |

---

## Sheet 4: Cloud Security Services

### Section Header
"CLOUD SECURITY SERVICES INVENTORY\nPolicy Requirement: Security tools must be integrated with SOC and provide centralized logging (Policy S5 Section 2.3)"

### Assessment Question
"Does your organization use cloud-based security services (XDR, SIEM, DLP, CASB, etc.)?"

### Column Structure
Same as Sheet 2 (Columns A-X)

### Example Services
- CrowdStrike Falcon (XDR/EDR)
- Microsoft Defender for Cloud
- Zscaler Internet Access (ZTNA)
- Cloudflare (DDoS protection, WAF)
- Palo Alto Prisma Cloud (CSPM)
- Proofpoint (Email security)
- Splunk Cloud (SIEM)
- Netskope (CASB)

### Checklist Items (Security Services Specific)
| Item | Requirement |
|------|-------------|
| ☐ | Security tools integrated with SOC/SIEM |
| ☐ | Alert thresholds configured and tested |
| ☐ | Incident response playbooks documented |
| ☐ | Log retention meets compliance requirements (≥1 year) |
| ☐ | Threat intelligence feeds enabled |
| ☐ | Security dashboard accessible to CISO |
| ☐ | License coverage matches endpoint count |
| ☐ | API integrations secured with MFA |

---

## Sheet 5: Cloud Storage Services

### Section Header
"CLOUD STORAGE SERVICES INVENTORY\nPolicy Requirement: All cloud storage must enforce encryption at rest and access controls (Policy S5 Section 2.4)"

### Assessment Question
"Does your organization use cloud storage services for file sharing, backup, or archival?"

### Column Structure
Same as Sheet 2 (Columns A-X)

### Example Services
- Dropbox Business
- Box
- Google Drive (Workspace)
- Microsoft OneDrive/SharePoint
- AWS S3 (as file storage)
- Backblaze B2
- Wasabi Hot Cloud Storage
- Egnyte

### Checklist Items (Cloud Storage Specific)
| Item | Requirement |
|------|-------------|
| ☐ | Encryption at rest verified (AES-256 minimum) |
| ☐ | Encryption in transit enforced (TLS 1.2+) |
| ☐ | Access controls based on data classification |
| ☐ | Shared link expiration policies configured |
| ☐ | Data loss prevention (DLP) rules active |
| ☐ | Version history enabled (minimum 30 days) |
| ☐ | Geographic replication configured |
| ☐ | Storage quotas set per user/department |
| ☐ | Audit logging enabled and reviewed quarterly |

---

## Sheet 6: Data Classification Mapping

### Section Header
"DATA CLASSIFICATION MAPPING\nPolicy Requirement: All cloud services must be mapped to data classification levels (Policy S5 Section 3.1)"

### Purpose
Cross-reference cloud services with the types of data they process to ensure appropriate security controls.

### Table Structure

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Cloud Service Name | 30 | Dropdown (from Sheets 2-5) |
| B | Data Type Processed | 30 | Text (e.g., PII, Financial, Health, Trade Secrets) |
| C | Data Classification | 20 | Dropdown (Restricted, Confidential, Internal, Public) |
| D | Volume (Records/GB) | 18 | Text |
| E | Data Residency Requirement | 25 | Dropdown (Switzerland Only, EU Only, USA Allowed, Global OK) |
| F | Encryption Required | 18 | Dropdown (Yes - At Rest, Yes - In Transit, Yes - Both, N/A) |
| G | Access Control Model | 22 | Dropdown (RBAC, ABAC, Need-to-Know, Public) |
| H | Retention Period | 18 | Dropdown (7 years, 5 years, 3 years, 1 year, 90 days, Other) |
| I | Compliance Framework | 25 | Text (e.g., GDPR, HIPAA, PCI-DSS, SOX, nFADP) |
| J | Status | 15 | Dropdown (✅ Mapped, ⚠️ Review Needed, ❌ Unmapped) |

### Example Entries

| Service | Data Type | Classification | Volume | Residency | Encryption | Access | Retention | Compliance | Status |
|---------|-----------|----------------|--------|-----------|------------|--------|-----------|------------|--------|
| Microsoft 365 | Email, Files, Contacts | Confidential | 500K emails | EU | Yes - Both | RBAC | 7 years | GDPR, nFADP | ✅ Mapped |
| Salesforce | Customer CRM Data | Confidential | 50K records | USA Allowed | Yes - Both | RBAC | 5 years | GDPR | ✅ Mapped |
| Dropbox | Project Files | Internal | 2 TB | Global OK | Yes - Both | Need-to-Know | 3 years | None | ✅ Mapped |

### Checklist (Data Classification)
| Item | Requirement |
|------|-------------|
| ☐ | All cloud services mapped to data types |
| ☐ | Data classification levels assigned |
| ☐ | Data volume estimated for capacity planning |
| ☐ | Residency requirements verified with vendor |
| ☐ | Encryption controls match data sensitivity |
| ☐ | Access control models documented |
| ☐ | Retention policies aligned with legal/regulatory |
| ☐ | Compliance frameworks identified |

---

## Sheet 7: Service Criticality Assessment

### Section Header
"SERVICE CRITICALITY ASSESSMENT\nPolicy Requirement: Business impact analysis must be performed for all cloud services (Policy S5 Section 3.2)"

### Purpose
Assess the criticality of each cloud service based on business impact, availability requirements, and recovery objectives.

### Table Structure

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Cloud Service Name | 30 | Dropdown (from Sheets 2-5) |
| B | Business Process Supported | 30 | Text |
| C | Criticality Level | 18 | Dropdown (Critical, High, Medium, Low) |
| D | RTO (Recovery Time Objective) | 20 | Dropdown (< 1 hour, 1-4 hours, 4-24 hours, 24-72 hours, > 72 hours) |
| E | RPO (Recovery Point Objective) | 20 | Dropdown (< 15 min, 15 min - 1 hour, 1-4 hours, 4-24 hours, > 24 hours) |
| F | Availability Requirement | 20 | Dropdown (99.99% (52 min/yr), 99.9% (8.7 hrs/yr), 99.5% (43 hrs/yr), 99% (87 hrs/yr)) |
| G | Peak Usage Time | 20 | Dropdown (24/7, Business Hours Only, Month-End, Ad-Hoc) |
| H | Downtime Impact | 25 | Dropdown (Severe ($100K+/hr), High ($10K-$100K/hr), Medium ($1K-$10K/hr), Low (<$1K/hr)) |
| I | Alternative Solution Exists | 20 | Dropdown (Yes - Active, Yes - Manual, No) |
| J | Status | 15 | Dropdown (✅ Assessed, ⚠️ Review, ❌ Not Assessed) |

### Criticality Calculation Matrix

**Automatic Criticality Assignment (Formula-Driven):**
```
IF Downtime Impact = "Severe" AND RTO < 1 hour → Critical
IF Downtime Impact = "Severe" OR RTO < 4 hours → High  
IF Downtime Impact = "Medium" → Medium
ELSE → Low
```

### Checklist (Criticality Assessment)
| Item | Requirement |
|------|-------------|
| ☐ | Business processes mapped to cloud services |
| ☐ | Criticality level assigned based on impact |
| ☐ | RTO/RPO defined and documented |
| ☐ | Availability requirements verified with vendor SLA |
| ☐ | Peak usage patterns identified |
| ☐ | Financial impact of downtime calculated |
| ☐ | Alternative solutions evaluated |
| ☐ | Business continuity plan updated |

---

## Sheet 8: Summary Dashboard

### Section Header
"CLOUD SERVICE INVENTORY - COMPLIANCE SUMMARY DASHBOARD"

### Dashboard Tables

#### Table 1: Compliance Summary by Service Category

| Service Category | Total Services | ✅ Compliant | ⚠️ Partial | ❌ Non-Compliant | N/A | Compliance % |
|------------------|----------------|--------------|------------|------------------|-----|--------------|
| SaaS Services | =COUNTA('2. SaaS Services'!A8:A50) | =COUNTIF('2. SaaS Services'!H8:H50,"✅*") | =COUNTIF(...) | =COUNTIF(...) | =COUNTIF(...) | =ROUND(C/(B-F)*100,1)&"%" |
| IaaS/PaaS | (formula) | (formula) | (formula) | (formula) | (formula) | (formula) |
| Security Services | (formula) | (formula) | (formula) | (formula) | (formula) | (formula) |
| Cloud Storage | (formula) | (formula) | (formula) | (formula) | (formula) | (formula) |
| **TOTAL** | =SUM(B4:B7) | =SUM(C4:C7) | =SUM(D4:D7) | =SUM(E4:E7) | =SUM(F4:F7) | =ROUND(C8/(B8-F8)*100,1)&"%" |

#### Table 2: Cost Analysis

| Metric | Value |
|--------|-------|
| Total Monthly Cloud Spend | =SUM('2. SaaS Services'!R8:R50, '3. IaaS/PaaS'!R8:R50, ...) |
| Total Annual Cloud Spend | =B12*12 |
| Average Cost per Service | =B12/[Total Service Count] |
| Highest Cost Service | =INDEX(A8:A50, MATCH(MAX(R8:R50), R8:R50, 0)) |
| Services >$10K/month | =COUNTIF(R8:R50,">10000") |

#### Table 3: Risk Indicators

| Risk Area | Count | Remediation Required |
|-----------|-------|---------------------|
| Services with Restricted data in non-EU regions | =COUNTIFS(E:E,"Restricted",F:F,"<>EU") | Yes |
| Critical services without backup | =COUNTIFS(D:D,"Critical",V:V,"No") | Yes |
| Services with Hard exit feasibility | =COUNTIF(W:W,"Hard*") | Review |
| Expired contracts | =COUNTIF(G:G,"Expired") | Urgent |
| Services lacking data classification | =COUNTIF(E:E,"") | Yes |

#### Table 4: Action Items Summary

| Priority | Count | Target Completion |
|----------|-------|-------------------|
| Critical (Non-Compliant + Critical Service) | =COUNTIFS(H:H,"❌*",D:D,"Critical") | Within 30 days |
| High (Non-Compliant + High Service) | =COUNTIFS(H:H,"❌*",D:D,"High") | Within 60 days |
| Medium (Partial Compliance) | =COUNTIF(H:H,"⚠️*") | Within 90 days |
| Low (Documentation gaps) | =COUNTIF(H:H,"⚠️*",D:D,"Low") | Next quarter |

---

## Sheet 9: Evidence Register

### Section Header
"EVIDENCE REGISTER - CLOUD SERVICE INVENTORY"

### Evidence Table

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Evidence ID | 18 | Text (Auto: EV-INV-001, EV-INV-002, ...) |
| B | Cloud Service Name | 30 | Dropdown (from all services) |
| C | Evidence Type | 25 | Dropdown (Contract, Invoice, CMDB Export, Asset Report, Screenshot, Data Flow Diagram, BIA Report, Other) |
| D | Description | 40 | Text |
| E | File Location | 40 | Text (SharePoint URL, file path) |
| F | Collection Date | 18 | Date |
| G | Collected By | 20 | Text |
| H | Retention Period | 18 | Dropdown (Permanent, 7 years, 5 years, 3 years, 1 year) |
| I | Status | 15 | Dropdown (Current, Expired, Pending Update) |

### Evidence Checklist
- ☐ All contracts uploaded to evidence repository
- ☐ Monthly invoices collected for cost verification
- ☐ CMDB export includes all services
- ☐ Data classification matrix approved by DPO
- ☐ Business impact analysis signed off by business owners
- ☐ Exit feasibility studies documented

---

## Sheet 10: Approval Sign-Off

### Section Header
"APPROVAL SIGN-OFF - CLOUD SERVICE INVENTORY ASSESSMENT"

### Approval Fields

| Field | Value |
|-------|-------|
| **Assessment Completed By:** | [USER INPUT - yellow] |
| **Completion Date:** | [USER INPUT - yellow] |
| **Total Services Inventoried:** | =SUM('8. Summary Dashboard'!B4:B7) |
| **Overall Compliance %:** | ='8. Summary Dashboard'!G8 |
| **Critical Issues Identified:** | [USER INPUT - yellow] |
| **Remediation Plan Attached:** | [Dropdown: Yes / No / In Progress] |

### Reviewer Approval

| Field | Value |
|-------|-------|
| **Reviewed By (ISO):** | [USER INPUT - yellow] |
| **Review Date:** | [USER INPUT - yellow] |
| **Review Comments:** | [USER INPUT - yellow, multiline] |
| **Approval Status:** | [Dropdown: Approved / Approved with Conditions / Rejected] |

### CISO Approval

| Field | Value |
|-------|-------|
| **Approved By (CISO):** | [USER INPUT - yellow] |
| **[Approval Date]:** | [USER INPUT - yellow] |
| **Executive Comments:** | [USER INPUT - yellow, multiline] |
| **Approval Decision:** | [Dropdown: Approved / Approved with Conditions / Rejected] |

### Next Review Details

| Field | Value |
|-------|-------|
| **Next Review Date:** | [USER INPUT - yellow, default: +90 days] |
| **Review Responsible:** | [USER INPUT - yellow] |
| **Special Considerations:** | [USER INPUT - yellow, multiline] |

---

## Integration Points

### Related Documents
- ISMS-POL-A.5.19-23-S5: Cloud Services Security Policy
- ISMS-POL-A.5.19-23-S6: Assessment Methodology (this framework)
- ISMS-IMP-A.5.23.2: Vendor Due Diligence Assessment (pulls service list from this workbook)
- ISMS-IMP-A.5.23.3: Secure Configuration Assessment (pulls service list from this workbook)
- Risk Register: Link Risk IDs to cloud service risks
- Asset Management Database (CMDB)
- Contract Management System

### External Workbook Links
The Summary Dashboard (Sheet 8) will be linked to by:
- ISMS-IMP-A.5.23.5 (Compliance Dashboard) - pulls inventory metrics
- ISMS-IMP-A.5.23.2 (Vendor DD) - references service names
- ISMS-IMP-A.5.23.3 (Configuration) - references service names

---

**END OF SPECIFICATION**

**Document Status:** Ready for Python generator script development  
**Estimated Workbook Size:** ~65 KB (10 sheets, 200+ formula cells)  
**Target Generation Time:** < 3 seconds

--------------------------------------------------------------------------------------------------

---

## 6. Example Data Row (Updated)

### Row 8 Example — Microsoft 365

| Column | Value |
|--------|-------|
| A | Microsoft 365 (Office 365) |
| B | SaaS |
| C | Microsoft Corporation |
| D | Critical |
| E | Confidential |
| F | EU |
| G | Active |
| H | ✅ Compliant |
| ... | (columns I-X as before) |
| Y | United States |
| Z | Mitigated (EU Data Boundary) |
| AA | EU, Switzerland (EU Data Boundary) |
| AB | Yes |
| AC | Yes |
| AD | Yes |
| AE | Not Applicable |
| AF | High (Few alternatives) |
| AG | Partial |

---

## 7. Checklist Updates

Add to each assessment sheet checklist (Sheets 2-5):

| Item | Requirement | Status | Evidence |
|------|-------------|--------|----------|
| ☐ | Provider HQ jurisdiction documented | ✅/⚠️/❌ | Vendor documentation |
| ☐ | CLOUD Act exposure assessed | ✅/⚠️/❌ | Risk assessment |
| ☐ | Data processing locations verified | ✅/⚠️/❌ | DPA, vendor statement |
| ☐ | DORA applicability determined | ✅/⚠️/❌ | Regulatory review |
| ☐ | NIS2 applicability determined | ✅/⚠️/❌ | Regulatory review |
| ☐ | AI system classification assessed | ✅/⚠️/❌ | AI inventory |
| ☐ | Concentration risk evaluated | ✅/⚠️/❌ | Risk assessment |
| ☐ | Alternative providers identified | ✅/⚠️/❌ | Market analysis |

---

## 8. Updated Sheet Structure Summary

### Before (v1.0) — 10 Sheets

| Sheet | Name |
|-------|------|
| 1 | Instructions & Legend |
| 2 | SaaS Services |
| 3 | IaaS Services |
| 4 | PaaS Services |
| 5 | Cloud Storage |
| 6 | Service Criticality Matrix |
| 7 | Data Classification Map |
| 8 | Summary Dashboard |
| 9 | Evidence Register |
| 10 | Approval Sign-Off |

### After (v2.0) — 10 Sheets

| Sheet | Name | Change |
|-------|------|--------|
| 1 | Instructions & Legend | UPDATED (regulatory guidance added) |
| 2 | SaaS Services | +9 columns (Y-AG), +8 checklist items |
| 3 | IaaS Services | +9 columns (Y-AG), +8 checklist items |
| 4 | PaaS Services | +9 columns (Y-AG), +8 checklist items |
| 5 | Cloud Storage | +9 columns (Y-AG), +8 checklist items |
| 6 | Service Criticality Matrix | Unchanged |
| 7 | Data Classification Map | Unchanged |
| 8 | Summary Dashboard | +7 regulatory metrics |
| 9 | Evidence Register | +5 evidence types |
| 10 | Approval Sign-Off | Unchanged |

---

## 9. Validation Requirements (Updated)

**Pre-Distribution Checks:**

- [ ] ✅ All **10 sheets** present
- [ ] ✅ Base 17 columns (A-Q) configured on assessment sheets
- [ ] ✅ Extended columns (R-X) present per sheet type
- [ ] ✅ **NEW: Regulatory columns (Y-AG) present on assessment sheets (2-5)**
- [ ] ✅ Dropdowns configured (22+ validation types) — was 17
- [ ] ✅ **NEW: 5 regulatory dropdowns configured**
- [ ] ✅ Dashboard formulas link to assessment sheets
- [ ] ✅ **NEW: Regulatory dashboard metrics table added**
- [ ] ✅ Evidence Register has auto-generated IDs (EV-INV-XXX)
- [ ] ✅ **NEW: Evidence Register includes regulatory evidence types**
- [ ] ✅ Approval Sign-Off links to dashboard metrics
- [ ] ✅ No Excel repair warnings (run style_object_checker.py)

---

## 10. Generator Script Impact

**File:** `generate_a523_1_inventory.py`

**Changes Required:**

1. Add 5 new dropdown list constants (PROVIDER_HQ_JURISDICTION, etc.)
2. Update `get_extended_columns_inventory()` — add Y-AG columns
3. Apply dropdowns to new columns in assessment sheets 2-5
4. Update `create_8_summary_dashboard()` — add regulatory metrics table
5. Update `create_9_evidence_register()` — add regulatory evidence types
6. Update column count constant: 24 → 33
7. Update `create_1_instructions()` — add regulatory guidance section
8. Update `main()` — version 2.0

---

## 11. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author Name] | Initial workbook specification |

---

**END OF REGULATORY UPDATE SPECIFICATION**

*"The CLOUD Act giveth access, and encryption taketh away." — Every compliance officer, probably*