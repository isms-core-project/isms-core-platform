<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.6-7-14-S3-UG:framework:UG:a.7.6-7-14-s3 -->
**ISMS-IMP-A.7.6-7-14-S3-UG - Secure Equipment Disposal Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.14: Secure Disposal or Re-Use of Equipment

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Equipment Disposal Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.6-7-14-S3-UG |
| **Related Policy** | ISMS-POL-A.7.6-7-14-S3 (Information Media Handling) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.14 (Secure Disposal or Re-Use of Equipment) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.7.6-7-14-S3 (Information Media Handling)
- ISMS-IMP-A.7.6-7-14-S1 (Secure Areas Working Assessment)
- ISMS-IMP-A.7.6-7-14-S2 (Clear Desk Screen Compliance)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.7.6-7-14-S3-TG.

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Disposal Requirements | Define approved disposal methods by equipment type |
| 3 | Disposal Tools | Assess data destruction tools and their effectiveness |
| 4 | Service Providers | Manage approved third-party disposal vendors |
| 5 | Disposal Log | Record all equipment disposal activities and certificates |
| 6 | Evidence Register | Store and reference evidence supporting assessments |
| 7 | Summary Dashboard | Compliance status and key metrics overview |
| 8 | Approval Sign-Off | Management review sign-off and certification |

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.7.6-7-14-S3 - Secure Equipment Disposal Assessment

#### What This Assessment Covers

This assessment documents the secure disposal and re-use procedures for equipment containing storage media, and evaluates compliance with data sanitisation requirements. It answers:

- What equipment types require secure disposal procedures?
- What disposal methods are defined for each data classification level?
- What tools and processes are used for data sanitisation?
- How are disposal service providers managed?
- What disposal records and certificates are maintained?
- What equipment has been disposed of or re-used (tracking)?

#### ISO 27001:2022 Control Reference

> *Items of equipment containing storage media should be verified to ensure that any sensitive data and licensed software has been removed or securely overwritten prior to disposal or re-use.*
>
> — ISO/IEC 27001:2022 Annex A, Control A.7.14

**Control Objective:** Prevent leakage of information from equipment being disposed of or re-used.

#### Key Principle

This assessment covers the ENTIRE equipment lifecycle end-point - from identification of equipment for disposal through data sanitisation, physical destruction (where required), and documentation. It applies to ALL equipment containing storage media: computers, servers, mobile devices, printers, network equipment, and removable media.

#### What You'll Document

**Disposal Requirements:**

- Equipment types requiring disposal procedures
- Disposal methods by data classification (physical destruction, secure overwrite, standard deletion)
- Tools and software approved for data sanitisation
- Verification requirements per method

**Disposal Service Providers:**

- Approved disposal vendors
- Contract and SLA requirements
- Destruction certificate requirements
- On-site vs. off-site destruction options

**Re-Use Requirements:**

- Internal re-assignment procedures
- External re-use (donation/sale) restrictions
- Licensed software handling
- Organisation identifier removal

**Disposal Tracking:**

- Equipment disposal log (last 12-24 months)
- Destruction certificates collected
- Verification evidence maintained
- Asset management record updates

#### How This Relates to Other A.7.6-7-14 Assessments

| Assessment | Focus | Relationship to S3 |
|------------|-------|-------------------|
| ISMS-IMP-A.7.6-7-14-S1 | Secure Areas Working | Equipment storage in secure areas before disposal |
| ISMS-IMP-A.7.6-7-14-S2 | Clear Desk/Screen Compliance | Removable media handling links to disposal |
| **ISMS-IMP-A.7.6-7-14-S3** | **Equipment Disposal Assessment** | **HOW equipment is securely disposed of or re-used** |


#### Related Controls

- **A.5.10-11** - Asset lifecycle including disposal
- **A.7.10** - Storage media management
- **A.8.10** - Information deletion requirements

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **IT Operations Manager** - Equipment disposal execution, data sanitisation
2. **Asset Manager** - Equipment inventory, disposal tracking
3. **Procurement** - Disposal vendor management
4. **Compliance Officers** - Certificate collection, audit evidence

#### Required Skills

- Understanding of data classification levels
- Knowledge of data sanitisation methods (overwrite, degaussing, physical destruction)
- Familiarity with equipment asset management
- Access to disposal records and vendor contracts

#### Time Commitment

- **Initial assessment:** 8-12 hours
- **Semi-annual updates:** 3-4 hours
- **Post-disposal event updates:** 1-2 hours

### Expected Outputs

Upon completion, you will have:

1. **Complete disposal requirements documentation** - Methods by equipment type and classification
2. **Disposal tools assessment** - Approved sanitisation tools and verification
3. **Service provider evaluation** - Vendor compliance and certificate management
4. **Disposal log** - All equipment disposed in assessment period
5. **Re-use tracking** - Equipment re-assigned or externally disposed
6. **Gap analysis** - Identified gaps in disposal procedures
7. **Evidence register** - Certificates and verification evidence
8. **Approved assessment** - Four-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Policy Documentation

- Secure disposal policy (ISMS-POL-A.7.6-7-14, Section 2.3)
- Information classification policy
- Asset management policy

#### 2. Disposal Procedures

- Data sanitisation procedures
- Physical destruction procedures
- Re-use/re-assignment procedures
- Vendor management procedures for disposal services

#### 3. Tool Documentation

- Approved data sanitisation tools (DBAN, Blancco, BitRaser, etc.)
- Tool configuration standards
- Verification procedures

#### 4. Vendor Information

- Disposal service provider contracts
- SLAs and destruction certificate requirements
- Approved vendor list

#### 5. Disposal Records

- Equipment disposal log (last 12-24 months)
- Destruction certificates (collected from vendors)
- Sanitisation verification reports
- Asset management records (disposed equipment)

### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Access to asset management system
- Access to disposal records and certificates
- Screen capture tools (for evidence)

### Dependencies

This assessment should be conducted after:
- Equipment inventory is current in asset management system
- Disposal records are consolidated from all sources

---

## Workflow

### High-Level Process

```
1. PREPARE
   |
2. DOCUMENT REQUIREMENTS (Sheet 2: Disposal Requirements)
   |
3. ASSESS TOOLS & METHODS (Sheet 3: Disposal Tools)
   |
4. EVALUATE SERVICE PROVIDERS (Sheet 4: Service Providers)
   |
5. REVIEW DISPOSAL LOG (Sheet 5: Disposal Log)
   |
6. COLLECT EVIDENCE (Sheet 7: Evidence Register)
   |
7. REVIEW SUMMARY (Sheet 6: Summary Dashboard)
   |
8. QUALITY CHECK
   |
9. OBTAIN APPROVALS (Sheet 8: Approval Sign-Off)
   |
10. SUBMIT FOR AUDIT
```

---

## Completing Each Sheet

### Sheet 1: Instructions & Legend

**Purpose:** Assessment metadata and status legend

**What to Complete:**

- Assessment Date, Completed By, Organisation
- Review status legend

**Time Required:** 5 minutes

### Sheet 2: Disposal Requirements

**Purpose:** Document disposal methods by equipment type and classification

**What to Document:**

**Disposal Methods Matrix:**

| Equipment Type | CONFIDENTIAL | INTERNAL | PUBLIC |
|----------------|--------------|----------|--------|
| Hard Drives (HDD) | Physical destruction | 3-pass overwrite or destruction | Format |
| Solid State Drives (SSD) | Physical destruction | Cryptographic erase or destruction | Secure erase |
| Mobile Devices | Physical destruction | Factory reset + verification | Factory reset |
| USB/Removable Media | Physical destruction | Secure overwrite or destruction | Format |
| Printers/Copiers | HDD removal + destruction | HDD removal + secure wipe | Clear memory |
| Network Equipment | N/A (config wipe) | Config wipe + verification | Config reset |

**Column Structure:**

| Col | Field | Description |
|-----|-------|-------------|
| A | Equipment Type | Category of equipment |
| B | Storage Type | HDD / SSD / Flash / Memory / Config |
| C | CONFIDENTIAL Method | Required disposal method |
| D | INTERNAL Method | Required disposal method |
| E | PUBLIC Method | Required disposal method |
| F | Verification Required | Yes / No |
| G | Certificate Required | Yes / No |
| H | Implementation Status | Implemented / Partial / Not Implemented |
| I | Notes | Additional context |

**Time Required:** 1-2 hours

### Sheet 3: Disposal Tools

**Purpose:** Document approved sanitisation tools and methods

**What to Document (Per Tool/Method):**

**Column A - Tool/Method Name:**

- "DBAN (Darik's Boot and Nuke)", "Blancco Drive Eraser", "Physical Shredder", "Degausser"

**Column B - Tool Type:**

- Dropdown: "Software - Overwrite", "Software - Crypto Erase", "Hardware - Degausser", "Hardware - Shredder"

**Column C - Applicable Equipment:**

- "HDD", "SSD", "All Magnetic Media", "All Storage Media"

**Column D - Standard/Method:**

- "DoD 5220.22-M (3-pass)", "NIST 800-88 Rev. 2 Clear", "NIST 800-88 Rev. 2 Purge", "Physical Destruction"

**Column E - Verification Method:**

- "Software verification report", "Visual inspection", "Certificate from vendor"

**Column F - Approved Version:**

- Current approved version: "DBAN 2.3.0", "Blancco 7.5"

**Column G - Last Tested:**

- Date tool was last tested: "15.12.2025"

**Column H - Compliant with Policy:**

- "Yes", "Partial", "No"

**Column I - Notes:**

- Configuration requirements, limitations

**Time Required:** 1-2 hours

### Sheet 4: Service Providers

**Purpose:** Document and evaluate disposal service providers

**What to Document (Per Provider):**

**Column A - Provider Name:**

- Company name: "SecureIT Disposal Ltd", "Data Destruction Services Inc"

**Column B - Service Type:**

- "On-site destruction", "Off-site destruction", "Recycling with destruction", "Certificate only"

**Column C - Contract Status:**

- "Active", "Expired", "Under Review"

**Column D - Contract Expiry:**

- Contract end date

**Column E - Destruction Certificate Provided:**

- "Yes - Per Item", "Yes - Per Batch", "No"

**Column F - On-Site Option:**

- "Yes", "No"

**Column G - Chain of Custody:**

- "Documented", "Partial", "Not Documented"

**Column H - Last Audit/Review:**

- Date of last provider review

**Column I - Compliance Status:**

- Formula or dropdown

**Column J - Notes:**

- Service limitations, preferred for specific equipment

**Time Required:** 1-2 hours

### Sheet 5: Disposal Log

**Purpose:** Track all equipment disposals in assessment period

**What to Document (Per Disposal Event):**

**Column A - Disposal ID:**

- Unique identifier: "DISP-2025-001"

**Column B - Date:**

- Disposal date: "15.12.2025"

**Column C - Asset Tag:**

- Equipment asset tag from asset management system

**Column D - Equipment Type:**

- "Laptop", "Desktop", "Server", "Mobile", "Printer", "Other"

**Column E - Make/Model:**

- Equipment make and model

**Column F - Serial Number:**

- Equipment serial number

**Column G - Data Classification:**

- Maximum classification stored: "CONFIDENTIAL", "INTERNAL", "PUBLIC", "Unknown"

**Column H - Disposal Method:**

- Actual method used: "Physical Destruction", "Secure Overwrite", "Factory Reset"

**Column I - Disposal Destination:**

- "Vendor Destruction", "Internal Re-Use", "Donation", "Sale", "Recycling"

**Column J - Certificate Obtained:**

- "Yes", "No", "N/A"

**Column K - Certificate Reference:**

- Certificate number or reference

**Column L - Verified By:**

- Name of person who verified sanitisation

**Column M - Asset Record Updated:**

- "Yes", "No"

**Column N - Compliant:**

- Formula: Checks method matches classification requirement

**Column O - Notes:**

- Additional context

**Time Required:** 2-4 hours (depending on disposal volume)

### Sheet 6: Summary Dashboard

**Purpose:** Automated compliance scoring and metrics

**What to Review:**

- Overall Disposal Compliance Score
- Disposal by Method (pie chart)
- Certificate Collection Rate
- Equipment Types Disposed
- Gap Summary

**Time Required:** 15-30 minutes

### Sheet 7: Evidence Register

**Purpose:** Document all supporting evidence

**Common Evidence to Collect:**

1. Disposal policy document
2. Approved tools list with configurations
3. Vendor contracts (redacted if sensitive)
4. Sample destruction certificates
5. Sanitisation verification reports
6. Asset management disposal records
7. Training records (disposal procedures)

**Time Required:** 2-3 hours

### Sheet 8: Approval Sign-Off

**Purpose:** Four-level approval workflow

**Approval Levels:**

- Level 1: Assessor
- Level 2: IT Operations Manager
- Level 3: CISO
- Level 4: Compliance Officer

**Time Required:** 5 minutes for Level 1

---

## Evidence Collection

### What Evidence to Collect

**1. Policy and Procedure Evidence**

- Secure disposal policy
- Data sanitisation procedures
- Vendor management procedures

**2. Tool Evidence**

- Approved tools list
- Tool configuration documentation
- Sample sanitisation verification reports

**3. Vendor Evidence**

- Vendor contracts (redacted)
- Service level agreements
- Sample destruction certificates

**4. Disposal Records**

- Disposal log export from asset management
- Destruction certificates (sample or all)
- Chain of custody documentation

**5. Training Evidence**

- Training materials
- Training completion records

### Evidence Storage

**Location:** SharePoint > ISMS > Assessments > A.7.6-7-14 > S3_Equipment_Disposal > Evidence

**Certificates Sub-folder:** Evidence > Certificates > [Year] > [Certificate files]

**Retention:** 7 years (per policy requirement for disposal records)

---

## Common Pitfalls

### Pitfall 1: Unknown Data Classification

**Problem:** Equipment disposed without knowing maximum data classification stored

**Impact:** Inappropriate disposal method used, potential data leakage

**How to Avoid:**

- Default to CONFIDENTIAL if classification unknown
- Implement pre-disposal classification assessment
- Document "Unknown" classification and treatment

### Pitfall 2: Missing Destruction Certificates

**Problem:** Vendor destruction completed but certificates not collected

**Impact:** Cannot evidence secure destruction to auditors

**How to Avoid:**

- Include certificate requirement in vendor contracts
- Track certificate receipt for each disposal batch
- Follow up on missing certificates within 30 days

### Pitfall 3: SSD Disposal Using HDD Methods

**Problem:** Using overwrite methods for SSDs which may not fully sanitise

**Impact:** Data potentially recoverable from SSDs

**How to Avoid:**

- Use cryptographic erase or physical destruction for SSDs
- Document SSD-specific procedures
- Verify tool supports SSD sanitisation correctly

### Pitfall 4: Internal Re-Use Without Sanitisation

**Problem:** Equipment re-assigned internally without data sanitisation

**Impact:** Previous user's data accessible to new user

**How to Avoid:**

- Include internal re-use in disposal procedures
- Sanitise before re-assignment regardless of destination
- Verify sanitisation before handover

### Pitfall 5: Printer/Copier Hard Drives Overlooked

**Problem:** Printers and copiers disposed without addressing internal storage

**Impact:** Print job history and scanned documents potentially recoverable

**How to Avoid:**

- Include printers/copiers in equipment inventory
- Remove and destroy hard drives before disposal
- Verify with vendor if hard drive present

### Pitfall 6: Removable Media Not Tracked

**Problem:** USB drives, external drives disposed without tracking

**Impact:** Incomplete disposal records, potential data leakage

**How to Avoid:**

- Include removable media in disposal procedures
- Provide secure disposal bins for small media
- Track batch destructions of removable media

### Pitfall 7: Asset Records Not Updated

**Problem:** Equipment disposed but asset management not updated

**Impact:** Audit discrepancy between inventory and physical assets

**How to Avoid:**

- Include asset record update in disposal checklist
- Verify asset status change after disposal
- Reconcile disposal log with asset management quarterly

### Pitfall 8: Licensed Software Not Addressed

**Problem:** Equipment disposed with licensed software still installed

**Impact:** License compliance issues, potential waste of licenses

**How to Avoid:**

- Include license deactivation in disposal procedure
- Coordinate with software asset management
- Document license handling for each disposal

---

## Quality Checklist

### Sheet 2: Disposal Requirements

- [ ] All equipment types documented
- [ ] Disposal methods defined for CONFIDENTIAL, INTERNAL, PUBLIC
- [ ] Verification requirements defined
- [ ] Certificate requirements defined
- [ ] Implementation status accurate

### Sheet 3: Disposal Tools

- [ ] All approved tools documented
- [ ] Standards/methods specified (DoD, NIST)
- [ ] Verification methods defined
- [ ] Last tested dates current (within 12 months)

### Sheet 4: Service Providers

- [ ] All disposal vendors documented
- [ ] Contract status current
- [ ] Certificate provision confirmed
- [ ] Last audit/review within 12 months

### Sheet 5: Disposal Log

- [ ] All disposals in period documented
- [ ] Data classification documented (or "Unknown" noted)
- [ ] Disposal methods appropriate for classification
- [ ] Certificates obtained where required
- [ ] Asset records updated

### Sheet 7: Evidence Register

- [ ] Policy documents referenced
- [ ] Tool documentation collected
- [ ] Sample certificates collected
- [ ] All evidence files exist

---

**END OF USER GUIDE**

---

*"Disposing of equipment without disposing of its data is not disposal at all."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
