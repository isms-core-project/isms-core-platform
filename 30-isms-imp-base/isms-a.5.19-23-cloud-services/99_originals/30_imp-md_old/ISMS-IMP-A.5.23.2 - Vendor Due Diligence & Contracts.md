# ISMS-IMP-A.5.23.S2 - Vendor Due Diligence & Contracts
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.5.23: Information security for use of cloud services

---

## Document Overview

**Document ID:** ISMS-IMP-A.5.23.S2  
**Assessment Area:** Vendor Due Diligence & Contracts  
**Related Policy:** ISMS-POL-A.5.19-23-S2, ISMS-POL-A.5.19-23-S5, ISMS-POL-A.5.19-23-S6  
**Purpose:** Assess vendor security posture, contract terms, SLAs, data sovereignty compliance, and audit rights for all cloud service providers

---

## Workbook Structure

### Sheet 1: Instructions & Legend

#### Header Section
- **Title:** "ISMS-IMP-A.5.23.S2 – Vendor Due Diligence & Contracts"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.5.23: Information security for use of cloud services"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block
```
Document ID:           ISMS-IMP-A.5.23.S2
Assessment Area:       Vendor Due Diligence & Contracts
Related Policy:        ISMS-POL-A.5.19-23-S2, S5
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly
```

#### How to Use This Workbook
1. Complete each worksheet tab (2–6) for all cloud service vendors
2. Use dropdown menus for standardized entries (Cert Status, SLA Tier, etc.)
3. Fill in yellow-highlighted cells with your vendor-specific information
4. Attach evidence: contracts (MSA, DPA, SLA), security certifications, audit reports
5. Document SLA performance metrics and track contract renewal dates
6. Update vendor security posture assessments annually or upon significant changes
7. Summary Dashboard auto-calculates vendor compliance statistics
8. Maintain the Evidence Register with all contract documents and certifications
9. Obtain final approval and sign-off from Legal, Procurement, and CISO

#### Status Legend
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Compliant | Vendor meets all security and contractual requirements | Green (C6EFCE) |
| ⚠️ | Partial | Some requirements met, gaps exist (e.g., cert pending) | Yellow (FFEB9C) |
| ❌ | Non-Compliant | Vendor does not meet minimum requirements | Red (FFC7CE) |
| N/A | Not Applicable | Requirement does not apply to this vendor/service | Gray |

#### Acceptable Evidence (Examples)
- ✓ Master Service Agreement (MSA)
- ✓ Data Processing Agreement (DPA) / Addendum
- ✓ Service Level Agreement (SLA)
- ✓ ISO 27001 certificate (current, not expired)
- ✓ SOC 2 Type II report (within last 12 months)
- ✓ FedRAMP authorization letter
- ✓ GDPR compliance attestation
- ✓ Vendor security questionnaire (completed)
- ✓ Penetration test results (if available)
- ✓ Incident response plan documentation
- ✓ Business continuity/disaster recovery plan
- ✓ Insurance certificates (cyber liability)
- ✓ Right to audit clause (contract section reference)
- ✓ Data sovereignty documentation (data center locations)

---

## Assessment Sheets (2-6) - Standard Column Layout

### Common Column Structure for Vendor Due Diligence

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| A | Cloud Service Name | 30 | Text | Free text (or dropdown from Inventory) |
| B | Vendor Name | 25 | Text | Free text |
| C | Service Type | 22 | Dropdown | SaaS, IaaS, PaaS, Security Service, Cloud Storage, Other |
| D | Service Criticality | 20 | Dropdown | Critical, High, Medium, Low |
| E | Data Classification | 22 | Dropdown | Public, Internal, Confidential, Restricted, Mixed |
| F | Contract Type | 22 | Dropdown | MSA + DPA, Subscription Agreement, Pay-As-You-Go, Trial, Custom |
| G | Contract Start Date | 18 | Date | Date picker |
| H | Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| I | Evidence Location | 30 | Text | Free text (SharePoint link, contract management system ID) |
| J | Gap Description | 35 | Text | Free text |
| K | Remediation Needed | 16 | Dropdown | Yes, No |
| L | Exception ID | 14 | Text | Free text |
| M | Risk ID | 14 | Text | Free text (links to risk register) |
| N | Compensating Controls | 35 | Text | Free text |
| O | Vendor Contact (Legal) | 25 | Text | Free text (email/phone) |
| P | Target Remediation Date | 18 | Date | Date picker |
| Q | Contract Owner | 22 | Text | Free text (internal person responsible) |

### Extended Columns for Vendor Due Diligence (R-X)

**NOTE:** Extended columns vary by sheet to capture domain-specific vendor data.

---

## Sheet 2: Vendor Security Certifications

### Section Header
"VENDOR SECURITY CERTIFICATIONS\nPolicy Requirement: All cloud vendors must maintain ISO 27001 or equivalent security certification (Policy S2 Section 3.1)"

### Assessment Question
"Do your cloud service vendors hold current security certifications (ISO 27001, SOC 2, FedRAMP, etc.)?"

### Extended Columns (R-X) for Security Certifications

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | ISO 27001 Certified | 18 | Dropdown | Yes (Current), Yes (Expired), No, Unknown |
| S | ISO 27001 Cert Number | 22 | Text | Free text (e.g., ISO27001-12345) |
| T | ISO 27001 Expiry Date | 18 | Date | Date picker |
| U | SOC 2 Type II Report | 20 | Dropdown | Yes (< 6 months), Yes (6-12 months), No, Unknown |
| V | SOC 2 Report Date | 18 | Date | Date picker |
| W | FedRAMP Authorized | 18 | Dropdown | Yes (High), Yes (Moderate), Yes (Low), No, N/A |
| X | Other Certifications | 30 | Text | Free text (e.g., PCI-DSS, HIPAA, CSA STAR) |

### Example Entry (Row 8)

| A | B | C | D | E | F | G | H | I | R | S | T | U | V | W | X |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Microsoft 365 | Microsoft Corp | SaaS | Critical | Confidential | MSA + DPA | 2024-01-01 | ✅ Compliant | \\contracts\ms\M365-cert.pdf | Yes (Current) | ISO27001-MS-2023 | 2026-06-30 | Yes (< 6 months) | 2025-11-15 | Yes (High) | SOC 3, CSA STAR Level 2 |

### Checklist Items (Security Certifications)

| Item | Requirement | Evidence |
|------|-------------|----------|
| ☐ | All critical/high services have ISO 27001 or SOC 2 Type II | Certification register |
| ☐ | Certificates verified as current (not expired) | Certificate expiry tracking |
| ☐ | SOC 2 reports obtained within last 12 months | Vendor portal, NDA required |
| ☐ | Certificate scope covers services in use | Certificate scope statement |
| ☐ | Certificate issuing body is accredited (e.g., UKAS, ANAB) | Issuer verification |
| ☐ | FedRAMP authorization verified for US government workloads | FedRAMP marketplace |
| ☐ | Industry-specific certs documented (PCI-DSS, HIPAA, etc.) | Compliance attestations |
| ☐ | Certificate renewal dates tracked in contract management system | CMS reports |

---

## Sheet 3: Contract Terms Analysis

### Section Header
"CONTRACT TERMS ANALYSIS\nPolicy Requirement: All cloud service contracts must include security clauses, data protection terms, and termination rights (Policy S2 Section 3.2)"

### Assessment Question
"Have all cloud service contracts been reviewed for security and data protection clauses?"

### Extended Columns (R-X) for Contract Terms

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Data Protection Clause | 20 | Dropdown | Yes (Adequate), Yes (Weak), No, Under Negotiation |
| S | Subprocessor Disclosure | 20 | Dropdown | Yes (List Provided), Yes (Generic), No |
| T | Liability Cap (CHF) | 20 | Text | Free text (e.g., "$1M annual fees") |
| U | Indemnification Clause | 18 | Dropdown | Yes (Favorable), Yes (Limited), No |
| V | Termination Notice Period | 20 | Dropdown | ≤30 days, 31-60 days, 61-90 days, >90 days |
| W | Data Return on Termination | 20 | Dropdown | Yes (30 days), Yes (60 days), Yes (90 days), No |
| X | Auto-Renewal Clause | 18 | Dropdown | Yes (Opt-Out), Yes (Opt-In), No |

### Example Entry

| A | B | R | S | T | U | V | W | X |
|---|---|---|---|---|---|---|---|---|
| Salesforce CRM | Salesforce.com | Yes (Adequate) | Yes (List Provided) | $5M or 12 months fees (greater) | Yes (Favorable) | 61-90 days | Yes (30 days) | Yes (Opt-Out) |

### Checklist Items (Contract Terms)

| Item | Requirement |
|------|-------------|
| ☐ | Data protection clause references GDPR/nFADP compliance |
| ☐ | Subprocessor list reviewed and approved by Legal |
| ☐ | Liability cap is reasonable for service criticality |
| ☐ | Indemnification covers data breaches and IP infringement |
| ☐ | Termination notice period ≤90 days for non-critical services |
| ☐ | Data return process documented (format, timeline, deletion proof) |
| ☐ | Auto-renewal tracked 90+ days before renewal date |
| ☐ | Price increase caps negotiated (e.g., max 5% annually) |

---

## Sheet 4: SLA Requirements & Performance

### Section Header
"SLA REQUIREMENTS & PERFORMANCE TRACKING\nPolicy Requirement: SLAs must define availability, support response times, and performance penalties (Policy S2 Section 3.3)"

### Assessment Question
"Do all cloud services have documented SLAs with performance commitments?"

### Extended Columns (R-X) for SLA Performance

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | SLA Availability % | 18 | Dropdown | 99.99% (4-nines), 99.9% (3-nines), 99.5%, 99%, <99%, None |
| S | Actual Availability Q4 | 20 | Number | Numeric (e.g., 99.97) |
| T | SLA Credits Claimed | 18 | Dropdown | Yes (Received), Yes (Pending), No, N/A |
| U | Support Response Time | 22 | Dropdown | <1 hour, 1-4 hours, 4-24 hours, >24 hours, Best Effort |
| V | Incident Count Q4 | 16 | Number | Numeric (count of incidents) |
| W | Mean Time to Resolve | 18 | Text | Free text (e.g., "2.5 hours avg") |
| X | SLA Review Date | 18 | Date | Date picker |

### Example Entry

| A | B | R | S | T | U | V | W | X |
|---|---|---|---|---|---|---|---|---|
| AWS EC2 Production | Amazon Web Services | 99.99% (4-nines) | 99.98 | No | <1 hour | 2 | 1.8 hours avg | 2025-12-15 |

### Checklist Items (SLA Performance)

| Item | Requirement |
|------|-------------|
| ☐ | SLA commitments documented for all critical/high services |
| ☐ | Actual availability tracked monthly and compared to SLA |
| ☐ | SLA breaches identified and credits claimed |
| ☐ | Support response times verified against SLA commitments |
| ☐ | Incident trends analyzed (increasing/decreasing) |
| ☐ | Mean time to resolve (MTTR) benchmarked against industry |
| ☐ | SLA performance reviewed quarterly with vendor |
| ☐ | Service degradations tracked (not just full outages) |

---

## Sheet 5: Data Sovereignty & Compliance

### Section Header
"DATA SOVEREIGNTY & COMPLIANCE\nPolicy Requirement: Vendor data processing locations must comply with organizational data residency requirements (Policy S2 Section 3.4)"

### Assessment Question
"Do vendors comply with data sovereignty and regulatory requirements for your data?"

### Extended Columns (R-X) for Data Sovereignty

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Data Processing Region | 22 | Dropdown | Switzerland, EU/EEA, USA, Asia-Pacific, Global, Unknown |
| S | Data Residency Verified | 20 | Dropdown | Yes (Contractual), Yes (Technical), No, Unknown |
| T | Standard Contractual Clauses | 22 | Dropdown | Yes (EU SCC), Yes (Swiss SCC), Yes (Other), No, N/A |
| U | Data Transfer Mechanism | 22 | Dropdown | Adequacy Decision, SCC, BCR, Derogations, None |
| V | GDPR Compliance | 18 | Dropdown | Yes (Certified), Yes (Self-Assessed), No, N/A |
| W | Swiss nFADP Compliance | 20 | Dropdown | Yes (Certified), Yes (Self-Assessed), No, N/A |
| X | Regulatory Framework | 30 | Text | Free text (e.g., HIPAA, PCI-DSS, SOX) |

### Example Entry

| A | B | R | S | T | U | V | W | X |
|---|---|---|---|---|---|---|---|---|
| Microsoft 365 | Microsoft Corp | EU/EEA | Yes (Contractual) | Yes (EU SCC) | Adequacy Decision | Yes (Certified) | Yes (Certified) | GDPR, nFADP, SOX |

### Checklist Items (Data Sovereignty)

| Item | Requirement |
|------|-------------|
| ☐ | Data processing regions verified for restricted/confidential data |
| ☐ | Data residency requirements met (Switzerland-only for restricted) |
| ☐ | Standard Contractual Clauses (SCC) in place for EU/Swiss transfers |
| ☐ | Data transfer mechanisms comply with GDPR Article 44-50 |
| ☐ | Vendor GDPR compliance verified (certification or assessment) |
| ☐ | Swiss nFADP requirements addressed (effective Sept 2023) |
| ☐ | Subprocessor locations disclosed and approved |
| ☐ | Data localization laws considered (China, Russia, India, etc.) |

---

## Sheet 6: Forensics, Audit Rights & Incident Response

### Section Header
"FORENSICS, AUDIT RIGHTS & INCIDENT RESPONSE\nPolicy Requirement: Vendors must support forensic investigations and grant audit rights (Policy S2 Section 3.5)"

### Assessment Question
"Do vendors provide forensic capabilities, audit rights, and incident response support?"

### Extended Columns (R-X) for Forensics & Audit

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Forensics Support | 20 | Dropdown | Yes (Full), Yes (Limited), No, Unknown |
| S | Forensics SLA | 20 | Text | Free text (e.g., "24-hour response") |
| T | Right to Audit | 18 | Dropdown | Yes (Unrestricted), Yes (With Notice), No |
| U | Audit Notice Period | 18 | Dropdown | No Notice, ≤7 days, 8-30 days, >30 days, N/A |
| V | Incident Notification SLA | 22 | Dropdown | <1 hour, 1-4 hours, 4-24 hours, >24 hours, None |
| W | Breach Notification | 20 | Dropdown | Yes (72 hours), Yes (Custom), No, Unknown |
| X | IR Playbook Provided | 18 | Dropdown | Yes, No, Upon Request |

### Example Entry

| A | B | R | S | T | U | V | W | X |
|---|---|---|---|---|---|---|---|---|
| CrowdStrike Falcon | CrowdStrike | Yes (Full) | 24-hour response | Yes (Unrestricted) | ≤7 days | <1 hour | Yes (72 hours) | Yes |

### Checklist Items (Forensics & Audit)

| Item | Requirement |
|------|-------------|
| ☐ | Forensics support verified for critical/high services |
| ☐ | Forensics SLA documented (log retention, data export, analysis support) |
| ☐ | Right to audit clause in contract (SOC 2 audit rights alternative accepted) |
| ☐ | Audit notice period ≤30 days for critical services |
| ☐ | Incident notification SLA ≤24 hours for security incidents |
| ☐ | Breach notification meets GDPR 72-hour requirement |
| ☐ | Incident response playbook obtained and reviewed |
| ☐ | Vendor participates in tabletop exercises (if critical service) |

---

## Sheet 7: Summary Dashboard

### Section Header
"VENDOR DUE DILIGENCE - COMPLIANCE SUMMARY DASHBOARD"

### Dashboard Tables

#### Table 1: Compliance Summary by Assessment Area

| Assessment Area | Total Vendors | ✅ Compliant | ⚠️ Partial | ❌ Non-Compliant | N/A | Compliance % |
|-----------------|---------------|--------------|------------|------------------|-----|--------------|
| Security Certifications | =COUNTA('2. Certifications'!A8:A50) | =COUNTIF('2. Certifications'!H8:H50,"✅*") | =COUNTIF(...) | =COUNTIF(...) | =COUNTIF(...) | =ROUND(C/(B-F)*100,1)&"%" |
| Contract Terms | (formula) | (formula) | (formula) | (formula) | (formula) | (formula) |
| SLA Performance | (formula) | (formula) | (formula) | (formula) | (formula) | (formula) |
| Data Sovereignty | (formula) | (formula) | (formula) | (formula) | (formula) | (formula) |
| Forensics & Audit | (formula) | (formula) | (formula) | (formula) | (formula) | (formula) |
| **TOTAL** | =SUM(B4:B8) | =SUM(C4:C8) | =SUM(D4:D8) | =SUM(E4:E8) | =SUM(F4:F8) | =ROUND(C9/(B9-F9)*100,1)&"%" |

#### Table 2: Certification Status Summary

| Certification Type | Vendors Certified | Vendors Pending | Vendors Without |
|--------------------|-------------------|-----------------|-----------------|
| ISO 27001 | =COUNTIF('2. Certifications'!R8:R50,"Yes (Current)") | =COUNTIF(...,"Yes (Expired)") | =COUNTIF(...,"No") |
| SOC 2 Type II | =COUNTIF('2. Certifications'!U8:U50,"Yes*") | 0 | =COUNTIF(...,"No") |
| FedRAMP | =COUNTIF('2. Certifications'!W8:W50,"Yes*") | 0 | =COUNTIF(...,"No") |

#### Table 3: Contract Renewal Tracker

| Timeframe | Contracts Expiring | Action Required |
|-----------|-------------------|-----------------|
| Next 30 days | =COUNTIFS('3. Contract Terms'!G8:G50,">="&TODAY(),'3. Contract Terms'!G8:G50,"<="&TODAY()+30) | Urgent Renewal |
| 31-90 days | =COUNTIFS(...) | Plan Renewal |
| 91-180 days | =COUNTIFS(...) | Monitor |
| >180 days | =COUNTIFS(...) | OK |

#### Table 4: SLA Performance Issues

| Issue Type | Count | Severity |
|------------|-------|----------|
| Availability < SLA Commitment | =COUNTIF('4. SLA Performance'!S8:S50,"<R8:R50") | High |
| SLA Credits Not Claimed | =COUNTIF('4. SLA Performance'!T8:T50,"Yes (Pending)") | Medium |
| >5 Incidents in Quarter | =COUNTIF('4. SLA Performance'!V8:V50,">5") | Medium |

#### Table 5: Data Sovereignty Risks

| Risk | Count | Remediation |
|------|-------|-------------|
| Restricted Data Outside Switzerland | =COUNTIFS('5. Data Sovereignty'!E8:E50,"Restricted",'5. Data Sovereignty'!R8:R50,"<>Switzerland") | Critical |
| Confidential Data Without SCC | =COUNTIFS('5. Data Sovereignty'!E8:E50,"Confidential",'5. Data Sovereignty'!T8:T50,"No") | High |
| GDPR Compliance Not Verified | =COUNTIF('5. Data Sovereignty'!V8:V50,"No") | High |

---

## Sheet 8: Evidence Register

### Section Header
"EVIDENCE REGISTER - VENDOR DUE DILIGENCE & CONTRACTS"

### Evidence Table

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| A | Evidence ID | 18 | Formula | =CONCATENATE("EV-VDD-",TEXT(ROW()-3,"000")) |
| B | Vendor Name | 25 | Text | Free text |
| C | Evidence Type | 25 | Dropdown | Contract (MSA), Contract (DPA), Contract (SLA), ISO 27001 Cert, SOC 2 Report, FedRAMP Letter, Vendor Questionnaire, Audit Report, Insurance Cert, Other |
| D | Description | 40 | Text | Free text |
| E | File Location | 40 | Text | Free text (SharePoint URL, contract mgmt system ID) |
| F | Document Date | 18 | Date | Date picker |
| G | Expiry/Renewal Date | 18 | Date | Date picker |
| H | Document Owner | 20 | Text | Free text (Legal, Procurement, ISO) |
| I | Status | 15 | Dropdown | Current, Expired, Pending Renewal, Superseded |

### Evidence Checklist
- ☐ All MSAs uploaded to contract management system
- ☐ DPAs reviewed by Legal and Data Protection Officer
- ☐ SLAs attached to vendor records
- ☐ Current ISO 27001/SOC 2 reports on file (<12 months old)
- ☐ FedRAMP authorization letters archived
- ☐ Vendor security questionnaires completed annually
- ☐ Cyber insurance certificates verified (>$1M coverage)

---

## Sheet 9: Approval Sign-Off

### Section Header
"APPROVAL SIGN-OFF - VENDOR DUE DILIGENCE ASSESSMENT"

### Approval Fields

**Assessment Completion:**
- Assessment Completed By: [USER INPUT - yellow]
- Completion Date: [USER INPUT - yellow]
- Total Vendors Assessed: ='7. Summary Dashboard'!B9
- Overall Compliance %: ='7. Summary Dashboard'!G9
- Critical Issues Identified: [USER INPUT - yellow]
- Remediation Plan Attached: [Dropdown: Yes / No / In Progress]

**Legal Review:**
- Reviewed By (Legal Counsel): [USER INPUT - yellow]
- Review Date: [USER INPUT - yellow]
- Contract Compliance Status: [Dropdown: Approved / Requires Negotiation / Non-Compliant]
- Legal Comments: [USER INPUT - yellow, multiline]

**Procurement Approval:**
- Reviewed By (Procurement): [USER INPUT - yellow]
- Review Date: [USER INPUT - yellow]
- Commercial Terms Status: [Dropdown: Approved / Under Negotiation / Rejected]
- Procurement Comments: [USER INPUT - yellow, multiline]

**CISO Approval:**
- Approved By (CISO): [USER INPUT - yellow]
- Approval Date: [USER INPUT - yellow]
- Security Risk Acceptance: [Dropdown: Approved / Approved with Conditions / Rejected]
- Executive Comments: [USER INPUT - yellow, multiline]

**Next Review Details:**
- Next Review Date: [USER INPUT - yellow, default: +90 days]
- Review Responsible: [USER INPUT - yellow]
- Special Considerations: [USER INPUT - yellow, multiline]

---

## Integration Points

### Related Documents
- ISMS-POL-A.5.19-23-S2: Supplier Agreement Requirements
- ISMS-POL-A.5.19-23-S5: Cloud Services Security Policy
- ISMS-IMP-A.5.23.S1: Cloud Service Inventory (pulls service list)
- Risk Register: Link Risk IDs to vendor risks
- Contract Management System: Link to contract records
- Legal document repository

### External Workbook Links
This workbook links to:
- ISMS-IMP-A.5.23.S1 (Inventory) - imports service names and criticality
- ISMS-IMP-A.5.23.S5 (Compliance Dashboard) - exports vendor compliance metrics

---

## Validation Requirements

**Pre-Distribution Checks:**
- [ ] ✅ All 9 sheets present
- [ ] ✅ Base 17 columns (A-Q) configured on assessment sheets
- [ ] ✅ Extended columns (R-X) present per sheet type
- [ ] ✅ Dropdowns configured (12+ validation types)
- [ ] ✅ Dashboard formulas link to assessment sheets
- [ ] ✅ Evidence Register has auto-generated IDs
- [ ] ✅ Approval Sign-Off links to dashboard metrics
- [ ] ✅ No Excel repair warnings (run style_object_checker.py)

---

**END OF SPECIFICATION**

**Document Status:** Ready for Python generator script development  
**Estimated Workbook Size:** ~70 KB (9 sheets, 250+ formula cells)  
**Target Generation Time:** < 3 seconds  
**Stakeholders:** Legal, Procurement, Compliance, CISO

--------------------------------------------------------------------------------------------------

# ISMS-IMP-A.5.23.S2 - Vendor Due Diligence & Contracts
## Regulatory Update — DORA, NIS2, AI Act, CLOUD Act Enhancements

---

## Change Summary

| Change Type | Description |
|-------------|-------------|
| **Sheet Added** | NEW Sheet 7: Jurisdictional Risk Assessment (20 columns) |
| **Columns Added** | 2 new columns (Y-Z) on Contract Terms sheet for DORA/NIS2 |
| **Checklists Updated** | +7 DORA Art.30 items, +3 NIS2 items, +9 Evaluation criteria |
| **Dashboard Updated** | +7 jurisdictional risk metrics |
| **Approval Updated** | +1 DPO sign-off section |
| **Instructions Updated** | Regulatory applicability guidance added |
| **Sheet Count** | 9 → 10 sheets |

---

## 1. New Dropdown Definitions

Add to Instructions & Legend sheet (after existing dropdown definitions):

### Regulatory Dropdown Lists
```
PROVIDER_HQ_JURISDICTION:
- Switzerland
- EU/EEA
- United Kingdom
- United States
- Other Adequate Country
- Non-Adequate Country

CLOUD_ACT_EXPOSURE:
- No Exposure
- Potential Exposure (US HQ)
- Mitigated (EU Data Boundary)
- Mitigated (Encryption + Key Control)
- Accepted Risk (Documented)
- Under Assessment

TRANSFER_MECHANISM:
- SCCs
- BCRs
- Adequacy Decision
- None
- N/A

RISK_LEVEL:
- Low
- Medium
- High
- Critical

YES_NO_PARTIAL_UNKNOWN:
- Yes
- No
- Partial
- Unknown

YES_NO_PLANNED:
- Yes
- No
- Planned
```

---

## 2. NEW Sheet: Jurisdictional Risk Assessment (Sheet 7)

**Insert as Sheet 7** — Existing sheets 7-9 become 8-10.

### Sheet Header
- **Title:** "JURISDICTIONAL RISK ASSESSMENT"
- **Subtitle:** "CLOUD Act, Data Sovereignty, and Cross-Border Transfer Analysis"
- **Warning text:** "⚠️ US-headquartered providers may be compelled to disclose data under CLOUD Act regardless of data location."

### Column Structure (A-T)

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Assessment_ID | 14 | Text | Auto: JRA-001 |
| B | Cloud_Service_Name | 25 | Text | From Inventory |
| C | Provider_Name | 22 | Text | Free text |
| D | Provider_HQ_Country | 18 | Text | Free text |
| E | Provider_HQ_Jurisdiction | 20 | Dropdown | PROVIDER_HQ_JURISDICTION |
| F | US_Parent_Company | 14 | Dropdown | Yes/No/Unknown |
| G | CLOUD_Act_Applicability | 20 | Dropdown | CLOUD_ACT_EXPOSURE |
| H | Data_Processing_Locations | 25 | Text | Free text (list countries) |
| I | EU_Data_Boundary_Available | 18 | Dropdown | YES_NO_PLANNED |
| J | Customer_Managed_Keys | 16 | Dropdown | YES_NO_PLANNED |
| K | Legal_Challenge_Commitment | 18 | Dropdown | YES_NO_PARTIAL_UNKNOWN |
| L | Adequacy_Decision_Status | 18 | Text | Free text |
| M | Transfer_Mechanism | 16 | Dropdown | TRANSFER_MECHANISM |
| N | Risk_Level | 14 | Dropdown | RISK_LEVEL |
| O | Risk_Accepted_By | 18 | Text | Free text |
| P | Risk_Acceptance_Date | 16 | Date | Date picker |
| Q | Compensating_Controls | 28 | Text | Free text |
| R | Review_Date | 14 | Date | Date picker |
| S | Evidence_Reference | 20 | Text | EV-JRA-XXX |
| T | Notes | 30 | Text | Free text |

**Total Columns: 20 (A-T)**
**Data Rows: 7-30 (24 entries)**

### Example Row (Row 7 — Microsoft 365)

| Column | Value |
|--------|-------|
| A | JRA-001 |
| B | Microsoft 365 |
| C | Microsoft Corporation |
| D | United States |
| E | United States |
| F | No |
| G | Mitigated (EU Data Boundary) |
| H | EU, Switzerland (EU Data Boundary enabled) |
| I | Yes |
| J | Yes |
| K | Yes |
| L | Adequacy Decision (Swiss-US DPF) |
| M | SCCs |
| N | Medium |
| O | CISO |
| P | 2025-01-15 |
| Q | EU Data Boundary + Customer Lockbox |
| R | 2025-07-01 |
| S | EV-JRA-001 |
| T | Example entry - delete or overwrite |

### Jurisdictional Risk Checklist

| Item | Requirement | Status | Evidence |
|------|-------------|--------|----------|
| ☐ | Provider HQ jurisdiction identified and documented | ✅/⚠️/❌ | Vendor documentation |
| ☐ | US parent company status verified | ✅/⚠️/❌ | Corporate structure review |
| ☐ | CLOUD Act exposure assessed for US-nexus providers | ✅/⚠️/❌ | Legal review |
| ☐ | Data processing locations documented in DPA | ✅/⚠️/❌ | DPA review |
| ☐ | EU Data Boundary availability checked | ✅/⚠️/❌ | Vendor announcement/docs |
| ☐ | Customer-managed encryption keys option evaluated | ✅/⚠️/❌ | Technical documentation |
| ☐ | Legal challenge commitment verified | ✅/⚠️/❌ | Contract/Public statement |
| ☐ | Transfer mechanism documented (SCCs, BCRs, etc.) | ✅/⚠️/❌ | DPA |
| ☐ | Risk acceptance recorded if residual risk remains | ✅/⚠️/❌ | Risk register |
| ☐ | Compensating controls documented for high-risk providers | ✅/⚠️/❌ | Control documentation |

### CLOUD Act Mitigation Strategies (Reference Section)

| Category | Strategies |
|----------|------------|
| Technical | EU Data Boundary, Customer-managed encryption keys, Confidential Computing |
| Contractual | Legal challenge commitment, Data disclosure notification, SCCs with supplementary measures |
| Organizational | Risk acceptance by CISO/DPO, Documented risk assessment, Regular review cycle |
| Alternative | Consider EU-headquartered alternatives for highest-risk data categories |

---

## 3. Contract Terms Sheet Updates (Sheet 3)

### New Columns (Y-Z) — Add After Existing Column X

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| Y | DORA_Art30_Compliance | 20 | Dropdown | Yes (Full)/Yes (Partial)/No/N/A (Not in scope) |
| Z | NIS2_Supply_Chain_Clause | 20 | Dropdown | Yes/No/N/A |

### Updated Contract Checklist — Add DORA/NIS2 Items

**Existing items remain unchanged. ADD the following:**

#### DORA Article 30 Contract Clauses (CON-DORA-01 to CON-DORA-07)

| Clause_ID | Requirement | DORA_Mandatory | NIS2_Mandatory |
|-----------|-------------|----------------|----------------|
| CON-DORA-01 | Clear service descriptions | Yes | No |
| CON-DORA-02 | Data processing locations specified | Yes | Yes |
| CON-DORA-03 | Subcontracting conditions defined | Yes | Yes |
| CON-DORA-04 | Full access and audit rights | Yes | No |
| CON-DORA-05 | Cooperation with regulators | Yes | Yes |
| CON-DORA-06 | Exit strategy provisions | Yes | No |
| CON-DORA-07 | Termination rights defined | Yes | No |

#### NIS2 Supply Chain Clauses (CON-NIS2-01 to CON-NIS2-03)

| Clause_ID | Requirement | DORA_Mandatory | NIS2_Mandatory |
|-----------|-------------|----------------|----------------|
| CON-NIS2-01 | Supply chain security requirements | No | Yes |
| CON-NIS2-02 | Incident notification ≤24h to customer | No | Yes |
| CON-NIS2-03 | Vulnerability handling process defined | No | Yes |

---

## 4. Evaluation Criteria Updates

### Add to Existing Evaluation Criteria (All Assessment Sheets)

#### Regulatory Evaluation Criteria (EVAL-REG-01 to EVAL-REG-06)

| Criteria_ID | Category | Requirement |
|-------------|----------|-------------|
| EVAL-REG-01 | Regulatory | Provider discloses HQ jurisdiction and legal entity structure |
| EVAL-REG-02 | Regulatory | Provider discloses all data processing locations |
| EVAL-REG-03 | Regulatory | Provider offers EU Data Boundary or regional commitment |
| EVAL-REG-04 | Regulatory | Provider supports customer-managed encryption keys |
| EVAL-REG-05 | Regulatory | Provider commits to challenge government data requests |
| EVAL-REG-06 | Regulatory | Provider discloses sub-processor jurisdictions |

#### AI Act Evaluation Criteria (EVAL-AI-01 to EVAL-AI-03)

| Criteria_ID | Category | Requirement |
|-------------|----------|-------------|
| EVAL-AI-01 | AI Act | AI system risk classification documented |
| EVAL-AI-02 | AI Act | High-risk AI system has conformity assessment |
| EVAL-AI-03 | AI Act | AI transparency requirements met |

---

## 5. Dashboard Updates (Sheet 8 — Previously Sheet 7)

### Add: Table 2 — Jurisdictional & CLOUD Act Risk Summary

Insert after Table 1 (Compliance by Assessment Area):

| Row | Metric | Formula | Status Formula |
|-----|--------|---------|----------------|
| Header | JURISDICTIONAL & CLOUD ACT RISK SUMMARY | (merged, dark blue) | |
| 1 | US-HQ Providers (CLOUD Act Scope) | `=COUNTIF('7. Jurisdictional Risk'!E7:E30,"United States")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 2 | Providers with US Parent Company | `=COUNTIF('7. Jurisdictional Risk'!F7:F30,"Yes")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 3 | CLOUD Act Potential Exposure (Unmitigated) | `=COUNTIF('7. Jurisdictional Risk'!G7:G30,"Potential*")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 4 | CLOUD Act Mitigated | `=COUNTIF('7. Jurisdictional Risk'!G7:G30,"Mitigated*")` | Info |
| 5 | High/Critical Jurisdictional Risk | `=COUNTIF('7. Jurisdictional Risk'!N7:N30,"High")+COUNTIF('7. Jurisdictional Risk'!N7:N30,"Critical")` | `=IF(B>0,"❌ Action","✅ OK")` |
| 6 | Providers Without EU Data Boundary | `=COUNTIF('7. Jurisdictional Risk'!I7:I30,"No")` | `=IF(B>0,"⚠️ Review","✅ OK")` |
| 7 | Providers Without Customer-Managed Keys | `=COUNTIF('7. Jurisdictional Risk'!J7:J30,"No")` | `=IF(B>0,"⚠️ Review","✅ OK")` |

### Update: Table 1 — Add Jurisdictional Risk Row

Add new row to Compliance by Assessment Area table:

| Assessment Area | Sheet Reference | Status Column |
|-----------------|-----------------|---------------|
| Jurisdictional Risk | '7. Jurisdictional Risk' | N (Risk_Level) |

**Note:** For Jurisdictional Risk, compliance logic differs:
- ✅ Compliant = Low + Medium risk
- ⚠️ Partial = High risk
- ❌ Non-Compliant = Critical risk

---

## 6. Instructions Sheet Updates

### Add: Regulatory Applicability Section

Insert after "Acceptable Evidence" section:
```
REGULATORY COMPLIANCE

This workbook includes updated requirements for:
- DORA (Digital Operational Resilience Act) - Art.30 contract clauses
- NIS2 (Network and Information Security Directive 2) - Supply chain security
- EU AI Act - AI service provider evaluation criteria
- US CLOUD Act - Jurisdictional risk assessment (NEW Sheet 7)

REGULATORY APPLICABILITY GUIDANCE

| If You Are...                        | Complete These Fields              |
|--------------------------------------|------------------------------------|
| EU Financial Entity (DORA scope)     | All DORA fields (mandatory)        |
| EU Essential/Important Entity (NIS2) | All NIS2 fields (mandatory)        |
| Using AI Systems from cloud vendors  | All AI Act evaluation criteria     |
| Using US-HQ Providers                | Sheet 7 Jurisdictional Risk (all)  |
| None of the Above                    | Mark as "N/A" or "Not Applicable"  |

CLOUD ACT CONSIDERATIONS

For providers headquartered in the United States, assess potential
exposure to US CLOUD Act data requests. Document:
- Whether EU Data Boundary commitment exists
- Whether customer-managed encryption keys are available  
- Risk acceptance if exposure is accepted
- Compensating controls implemented
```

### Update: How to Use This Workbook

Change instruction count from 9 to 10 and update text:
```
5. Complete Jurisdictional Risk sheet (7) for all US-nexus providers (NEW)
```

### Update: Acceptable Evidence

Add new items:
```
✓ Jurisdictional risk assessment (for US-nexus providers)
✓ Risk acceptance form (signed by CISO/DPO)
✓ EU Data Boundary confirmation (vendor documentation)
✓ Customer-managed key configuration evidence
```

---

## 7. Approval Sign-Off Updates (Sheet 10 — Previously Sheet 9)

### Add: Data Protection Officer Review Section

Insert between Procurement Review and CISO Approval:

| Field | Type |
|-------|------|
| **DATA PROTECTION OFFICER REVIEW** | Section header (blue) |
| Reviewed By (DPO): | Yellow input |
| Review Date: | Yellow input |
| Data Protection Compliance: | Dropdown: Compliant/Partially Compliant/Non-Compliant |
| Cross-Border Transfer Status: | Dropdown: Approved/Approved with SCCs/Requires TIA/Rejected |
| DPO Comments: | Yellow input |

### Update: Assessment Summary

Add new field:

| Field | Formula/Value |
|-------|---------------|
| Jurisdictional Risks Identified: | `='8. Summary Dashboard'!B20` |

---

## 8. Updated Sheet Structure Summary

### Before (v1.0) — 9 Sheets

| Sheet | Name |
|-------|------|
| 1 | Instructions & Legend |
| 2 | Security Certifications |
| 3 | Contract Terms |
| 4 | SLA Performance |
| 5 | Data Sovereignty |
| 6 | Forensics & Audit |
| 7 | Summary Dashboard |
| 8 | Evidence Register |
| 9 | Approval Sign-Off |

### After— 10 Sheets

| Sheet | Name | Change |
|-------|------|--------|
| 1 | Instructions & Legend | UPDATED |
| 2 | Security Certifications | Unchanged |
| 3 | Contract Terms | +2 columns (Y-Z), +10 checklist items |
| 4 | SLA Performance | Unchanged |
| 5 | Data Sovereignty | Unchanged |
| 6 | Forensics & Audit | Unchanged |
| 7 | **Jurisdictional Risk** | **NEW** |
| 8 | Summary Dashboard | +7 metrics, renumbered |
| 9 | Evidence Register | +2 evidence types, renumbered |
| 10 | Approval Sign-Off | +DPO section, renumbered |

---

## 9. Validation Requirements (Updated)

**Pre-Distribution Checks:**

- [ ] ✅ All **10 sheets** present (was 9)
- [ ] ✅ Base 17 columns (A-Q) configured on assessment sheets
- [ ] ✅ Extended columns present per sheet type
- [ ] ✅ **NEW: Jurisdictional Risk sheet has 20 columns (A-T)**
- [ ] ✅ **NEW: Contract Terms has columns Y-Z (DORA/NIS2)**
- [ ] ✅ Dropdowns configured (22+ validation types) — was 17
- [ ] ✅ **NEW: 6 regulatory dropdowns configured**
- [ ] ✅ Dashboard formulas link to assessment sheets
- [ ] ✅ **NEW: Dashboard includes jurisdictional metrics table**
- [ ] ✅ Evidence Register has auto-generated IDs (EV-VDD-XXX)
- [ ] ✅ **NEW: Evidence Register includes Jurisdictional Assessment type**
- [ ] ✅ Approval Sign-Off links to dashboard metrics
- [ ] ✅ **NEW: DPO sign-off section present**
- [ ] ✅ No Excel repair warnings (run style_object_checker.py)

---

## 10. Generator Script Impact

**File:** `generate_a523_2_vendor_dd.py`

**Changes Required:**

1. Add 6 new dropdown list constants (PROVIDER_HQ_JURISDICTION, CLOUD_ACT_EXPOSURE, etc.)
2. Update `create_workbook()` — add "7. Jurisdictional Risk" sheet, renumber 8-10
3. Add new function `create_7_jurisdictional_risk()`
4. Add `get_jurisdictional_columns()` — 20 columns
5. Add `create_jurisdictional_validations()` — 7 validation types
6. Add `get_checklist_jurisdictional()` — 10 items
7. Update `get_extended_columns_contracts()` — add Y-Z
8. Update `get_checklist_contracts()` — add DORA/NIS2 items
9. Update `create_8_summary_dashboard()` — add jurisdictional metrics table
10. Update `create_9_evidence_register()` — add evidence types
11. Add `create_10_approval_signoff()` — add DPO section
12. Update `main()` — 10 sheets, version 2.0

---

## 11. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author Name] | Initial workbook specification |

---

**END OF REGULATORY UPDATE SPECIFICATION**

*"The CLOUD Act giveth access, and encryption taketh away." — Every compliance officer, probably*