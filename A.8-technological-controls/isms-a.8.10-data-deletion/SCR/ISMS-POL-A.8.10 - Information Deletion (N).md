# ISMS-POL-A.8.10 — Information Deletion
## Comprehensive Policy & Implementation Framework

---

**Document ID**: ISMS-POL-A.8.10  
**Title**: Information Deletion Policy  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Information Security Manager | Initial policy framework |

**Review Cycle**: Annual (or upon significant regulatory/organizational changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Chief Information Security Officer (CISO)
- Data Protection Officer (DPO)
- Legal/Compliance Officer
- Chief Information Officer (CIO) or IT Director
- Executive Management / Board (for strategic approval)

**Distribution**: All employees, contractors, third-party service providers  
**Related Standards**: ISO/IEC 27001:2022 Control A.8.10, ISO/IEC 27002:2022 Control 8.10, NIST SP 800-88, Swiss FADP, EU GDPR

---

## Executive Summary

This policy establishes [Organization]'s requirements for information deletion controls to ensure systematic deletion of information when no longer required, in accordance with ISO/IEC 27001:2022 Control A.8.10.

**Scope**: This policy applies to all information assets regardless of storage location (on-premises, cloud, third-party), all storage media types (magnetic, solid-state, optical, paper, mobile devices), all systems and applications (including backup infrastructure), and all data categories (personal data, business records, technical data, logs) throughout their lifecycle.

**Purpose**: Define organizational requirements for information deletion control implementation and governance. This policy establishes WHAT deletion controls are required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8.10.1 through A.8.10.5.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss Federal Data Protection Act (FADP) for data minimization and right to erasure, EU GDPR Article 17 (Right to Erasure) where processing EU personal data, and ISO/IEC 27001:2022. NIST SP 800-88 Rev. 1 is referenced as informational guidance for media sanitization best practices, not mandatory compliance unless US federal contracts require it.

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.10

**ISO/IEC 27001:2022 Annex A.8.10 - Information Deletion**

> *Information stored in information systems, devices or in any other storage media should be deleted when no longer required.*

**Control Objective**: Establish organizational policy for information deletion controls ensuring systematic removal of data when retention requirements are met, supporting data minimization principles, regulatory compliance, and protection against unauthorized disclosure.

**This Policy Addresses**:
- Retention schedules and deletion triggers based on legal, regulatory, and business requirements
- Deletion methods appropriate to media types, data sensitivity, and regulatory requirements
- Verification and evidence requirements for demonstrating deletion occurred
- Third-party and cloud service provider deletion obligations and contractual requirements
- Integration with [Organization]'s data governance, privacy management, and risk assessment processes

### 1.2 What This Policy Does

This policy:
- **Defines** information deletion control requirements aligned with regulatory obligations and organizational risk appetite
- **Establishes** governance framework for deletion decision-making, exception management, and compliance monitoring
- **Specifies** roles and responsibilities for deletion control implementation and oversight
- **References** applicable regulatory requirements per ISMS-POL-00 (Regulatory Applicability Framework)
- **Integrates** with related controls including data classification (A.5.12), asset management (A.5.9), privacy protection (A.5.34), and secure disposal (A.7.14)

### 1.3 What This Policy Does NOT Do

This policy does NOT:
- **Specify technical deletion procedures** (see ISMS-IMP-A.8.10.2 Deletion Methods Assessment for media-specific procedures)
- **Define retention periods for specific data types** (see ISMS-IMP-A.8.10.1 Retention & Deletion Triggers Assessment)
- **Provide vendor-specific deletion instructions** (see ISMS-IMP-A.8.10.3 Third-Party & Cloud Deletion Assessment)
- **Select deletion technologies or tools** (technology selection based on [Organization]'s risk assessment and operational requirements)
- **Replace legal counsel** (legal retention requirements and data subject rights require DPO and legal review)
- **Mandate specific deletion standards** (NIST SP 800-88 used as informational reference unless contractually required)

**Rationale**: Separating policy requirements from implementation guidance enables:
- Policy stability despite evolving regulatory landscape and threat environment
- Technical agility for technology updates and infrastructure changes without policy revision
- Clear distinction between governance (WHAT/WHO in policy) and execution (HOW in implementation)
- Modular maintenance with independent versioning and targeted stakeholder reviews

### 1.4 Scope

**This policy applies to**:
- All information assets (electronic and physical) containing organizational or personal data
- All storage locations (on-premises data centers, cloud environments, third-party processors, backup systems, disaster recovery sites, archives)
- All storage media types (magnetic hard disk drives, solid-state drives, optical media, magnetic tape, paper records, mobile devices, removable media)
- All data categories (personal data subject to GDPR/FADP, business records, technical data, application logs, system metadata, email, documents)
- All lifecycle stages (operational systems, archived data, backup retention, end-of-life disposal)
- All personnel (employees, contractors, temporary staff, third-party processors, service providers)
- All organizational units ([Organization] entities, subsidiaries, branches as defined in scope)

**Out of Scope**:
- Active legal hold data (deletion suspended per litigation, investigation, or regulatory examination requirements; covered under separate legal hold procedures)
- Data required for ongoing regulatory examination (deletion deferred until examination completion; DPO approval required)
- Archival records with permanent retention mandates (deletion not applicable per regulatory or business requirements; documented in retention schedule)
- Third-party data where [Organization] acts as processor only (deletion executed per data controller instruction; not independent [Organization] decision)
- Public information intentionally published (deletion of published content follows separate content management procedures)

### 1.5 Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss FADP (nDSG)** | All Swiss operations | Art. 6 - Data minimization; Art. 12 - Right to erasure; Art. 30 - Adequate security measures |
| **EU GDPR** | When processing EU personal data | Art. 5(1)(e) - Storage limitation principle; Art. 17 - Right to erasure; Art. 32 - Security of processing |
| **ISO/IEC 27001:2022** | Certification scope | Control A.8.10 - Information deletion policy and procedures documented and implemented |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Information Deletion Requirements |
|-----------|-------------------|-----------------------------------|
| **PCI DSS v4.0** | Processing payment card data | Requirement 3.1 - Retain cardholder data only as long as needed; secure deletion when no longer required |
| **FINMA** | Swiss regulated financial institution | Record retention per FINMA Circular 2008/21; secure deletion after retention period |
| **HIPAA** | Processing US healthcare data | §164.310(d)(2) - Disposal of electronic protected health information |
| **SOX** | US publicly traded company | 7-year retention for audit records; secure deletion afterward |
| **CCPA** | Processing California residents' data | Right to deletion (§1798.105); business and service provider obligations |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- **NIST SP 800-88 Rev. 1** - Guidelines for Media Sanitization (Clear, Purge, Destroy)
- **ISO/IEC 27040** - Storage security including sanitization guidance
- **ISO/IEC 27555** - Guidelines on personally identifiable information deletion
- **ISO/IEC 27017** - Cloud services information security controls (deletion guidance)
- **DIN 66399** - Destruction of data media (German standard for paper/media destruction)
- **DoD 5220.22-M** - National Industrial Security Program (legacy, superseded by NIST SP 800-88)

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment coordinated by DPO and Legal/Compliance. The most stringent requirements apply where multiple regulations overlap.

---

## 2. Policy Documents

### 2.1 Policy Structure

The information deletion policy framework consists of the following modular documents:

| Document ID | Title | Purpose | Lines |
|-------------|-------|---------|-------|
| **ISMS-POL-A.8.10** | Master Framework | This document - index and overview | ~350 |
| **ISMS-POL-A.8.10-S1** | Purpose, Scope, Definitions | Foundation and terminology | ~350 |
| **ISMS-POL-A.8.10-S2** | Deletion Requirements | Requirements overview | ~200 |
| **ISMS-POL-A.8.10-S2.1** | Retention & Deletion Triggers | When deletion must occur | ~350 |
| **ISMS-POL-A.8.10-S2.2** | Deletion Methods by Media Type | How deletion is performed | ~350 |
| **ISMS-POL-A.8.10-S2.3** | Verification & Evidence Requirements | Proving deletion occurred | ~300 |
| **ISMS-POL-A.8.10-S2.4** | Third-Party & Cloud Deletion | External provider obligations | ~300 |
| **ISMS-POL-A.8.10-S3** | Roles & Responsibilities | RACI and accountability | ~250 |
| **ISMS-POL-A.8.10-S4** | Policy Governance | Review, exceptions, compliance | ~200 |
| **ISMS-POL-A.8.10-S5** | Annexes | Supporting materials | Variable |
| **ISMS-POL-A.8.10-S5.A** | Approved Deletion Methods Matrix | Technical reference | ~300 |
| **ISMS-POL-A.8.10-S5.B** | Data Subject Erasure Request Form | GDPR/FADP compliance | ~200 |
| **ISMS-POL-A.8.10-S5.C** | Deletion Verification Checklist | Quality assurance | ~200 |
| **ISMS-POL-A.8.10-S5.D** | Quick Reference Guide | Operational summary | ~150 |

**Total Policy Layer:** ~13 documents, approximately 3,500 lines

**Design Philosophy:** Each document is independently versionable (maximum 300-400 lines) to enable granular change management, targeted stakeholder reviews, and clear audit trails.

### 2.2 Document Hierarchy

```
ISMS-POL-A.8.10 (Master) ← You are here
├── ISMS-POL-A.8.10-S1 (Purpose, Scope, Definitions)
├── ISMS-POL-A.8.10-S2 (Requirements Overview)
│   ├── ISMS-POL-A.8.10-S2.1 (Retention & Deletion Triggers)
│   ├── ISMS-POL-A.8.10-S2.2 (Deletion Methods by Media Type)
│   ├── ISMS-POL-A.8.10-S2.3 (Verification & Evidence Requirements)
│   └── ISMS-POL-A.8.10-S2.4 (Third-Party & Cloud Deletion)
├── ISMS-POL-A.8.10-S3 (Roles & Responsibilities)
├── ISMS-POL-A.8.10-S4 (Policy Governance)
└── ISMS-POL-A.8.10-S5 (Annexes)
    ├── ISMS-POL-A.8.10-S5.A (Approved Deletion Methods Matrix)
    ├── ISMS-POL-A.8.10-S5.B (Data Subject Erasure Request Form)
    ├── ISMS-POL-A.8.10-S5.C (Deletion Verification Checklist)
    └── ISMS-POL-A.8.10-S5.D (Quick Reference Guide)

Implementation Layer (Separate Documents):
├── ISMS-IMP-A.8.10.1 (Retention & Deletion Triggers Assessment)
├── ISMS-IMP-A.8.10.2 (Deletion Methods Assessment)
├── ISMS-IMP-A.8.10.3 (Third-Party & Cloud Deletion Assessment)
├── ISMS-IMP-A.8.10.4 (Verification & Evidence Management)
└── ISMS-IMP-A.8.10.5 (Compliance Dashboard)
```

---

## 3. Assessment & Implementation Documents

### 3.1 Assessment Specifications (Markdown)

The framework includes **5 comprehensive assessment specifications** defining the structure and requirements for Excel workbook generation:

| Document ID | Title | Purpose | Sheets |
|-------------|-------|---------|--------|
| **ISMS-IMP-A.8.10.1** | Retention & Deletion Triggers | Map data to retention periods and deletion triggers | ~8 |
| **ISMS-IMP-A.8.10.2** | Deletion Methods Assessment | Assess deletion capabilities by media/platform | ~10 |
| **ISMS-IMP-A.8.10.3** | Third-Party & Cloud Deletion | Document provider deletion capabilities and SLAs | ~8 |
| **ISMS-IMP-A.8.10.4** | Verification & Evidence Management | Track deletion certificates, logs, and evidence | ~8 |
| **ISMS-IMP-A.8.10.5** | Compliance Dashboard | Consolidated metrics and gap analysis | ~6 |

### 3.2 Generated Excel Workbooks

When Python generators are executed, they produce:

| Workbook | Sheets | Purpose |
|----------|--------|---------|
| **ISMS-IMP-A.8.10.1_Retention_Triggers_YYYYMMDD.xlsx** | ~8 | Data categories, retention periods, triggers |
| **ISMS-IMP-A.8.10.2_Deletion_Methods_YYYYMMDD.xlsx** | ~10 | Media inventory, tools, physical destruction |
| **ISMS-IMP-A.8.10.3_Third_Party_Cloud_YYYYMMDD.xlsx** | ~8 | Provider inventory, SLAs, verification |
| **ISMS-IMP-A.8.10.4_Verification_Evidence_YYYYMMDD.xlsx** | ~8 | Certificates, logs, audit trail |
| **ISMS-IMP-A.8.10.5_Compliance_Dashboard_YYYYMMDD.xlsx** | ~6 | Executive summary, KPIs, gaps |

**Total Assessment Output:** ~40 sheets across 5 workbooks

### 3.3 Assessment Domains Explained

**Domain 1 - Retention & Deletion Triggers:**
- What data categories exist? (personal data, business records, logs, backups)
- What are the retention periods? (legal, regulatory, contractual, business)
- What triggers deletion? (expiry, data subject request, contract end, legal hold release)
- Are legal holds properly managed? (litigation, regulatory investigation)

**Domain 2 - Deletion Methods Assessment:**
- What storage media exists? (HDD, SSD, tape, cloud, paper, mobile)
- What deletion tools are available? (secure overwrite, cryptographic erasure, physical destruction)
- Are methods appropriate for media type? (NIST SP 800-88 alignment)
- Are deletion capabilities verified? (tool validation, certification)

**Domain 3 - Third-Party & Cloud Deletion:**
- Which providers store organizational data? (IaaS, PaaS, SaaS, BaaS)
- What deletion methods do providers offer? (API, portal, request-based)
- Are contractual deletion clauses in place? (DPA, SLA)
- How is deletion verified? (certificates, confirmations, audit logs)

**Domain 4 - Verification & Evidence Management:**
- How is deletion documented? (logs, certificates, chain of custody)
- Where is evidence stored? (audit trail, evidence register)
- How are data subject requests tracked? (request log, response SLA)
- Is evidence sufficient for audit? (completeness, retention)

**Domain 5 - Compliance Dashboard:**
- What is overall deletion compliance? (traffic light indicators)
- What gaps exist? (consolidated gap analysis)
- What risks are present? (residual risk from incomplete deletion)
- What is the remediation roadmap? (prioritized action plan)

### 3.4 Assessment Workflow

```
┌────────────────────────────────────────────────────────────┐
│ PHASE 1: GENERATION (Day 1)                                │
│ • Run 5 Python generator scripts                           │
│ • Output: 5 Excel workbooks with ~40 sheets total          │
│ • Validation: Run excel_sanity_check.py on each            │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ PHASE 2: ASSESSMENT (Weeks 1-3)                            │
│ • Data governance / IT / Legal teams complete workbooks    │
│ • Fill yellow cells, complete checklists, document gaps    │
│ • Provide evidence (deletion logs, certificates, contracts)│
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ PHASE 3: NORMALIZATION (Day 15)                            │
│ • Run normalize_assessment_files.py                        │
│ • Clean up filename variations from review process         │
│ • Create audit trail manifest                              │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ PHASE 4: DASHBOARD (Day 16)                                │
│ • Generate compliance summary dashboard                    │
│ • Link to normalized assessment files                      │
│ • Auto-populate compliance metrics                         │
│ • Complete consolidated gap/risk/remediation sections      │
└────────────────────────────────────────────────────────────┘
                            ↓
┌────────────────────────────────────────────────────────────┐
│ PHASE 5: EXECUTIVE REVIEW (Week 4)                         │
│ • CISO and DPO review dashboard                            │
│ • Approve remediation roadmap and budget                   │
│ • Sign off on assessment package                           │
│ • Deliver to auditors / regulators                         │
└────────────────────────────────────────────────────────────┘
```

---

## 4. Automation Scripts

### 4.1 Assessment Generator Scripts

| Script | Output | Purpose |
|--------|--------|---------|
| `generate_a810_1_retention_triggers.py` | ISMS-IMP-A.8.10.1 | Retention and triggers workbook |
| `generate_a810_2_deletion_methods.py` | ISMS-IMP-A.8.10.2 | Deletion methods workbook |
| `generate_a810_3_third_party_cloud.py` | ISMS-IMP-A.8.10.3 | Third-party/cloud workbook |
| `generate_a810_4_verification_evidence.py` | ISMS-IMP-A.8.10.4 | Evidence management workbook |
| `generate_a810_5_compliance_dashboard.py` | ISMS-IMP-A.8.10.5 | Executive dashboard |

### 4.2 Validation Scripts (Reused)

| Script | Purpose |
|--------|---------|
| `excel_sanity_check.py` | Generic workbook validator (structure, formulas, validation) |
| `style_object_checker.py` | Detect shared style objects causing Excel warnings |
| `style_object_patcher.py` | Auto-fix style issues in generated workbooks |
| `normalize_assessment_files.py` | Normalize filenames for audit readiness |

**Script Quality Standards:**
- PEP 8 compliant Python code
- Error handling and graceful failures
- Comprehensive commenting
- Modular functions for reusability
- Validation of inputs and outputs

---

## 5. Roles & Responsibilities

### 5.1 Executive Roles

| Role | Responsibilities |
|------|------------------|
| **CISO** | Overall accountability, policy approval, exception sign-off, budget approval |
| **DPO** | Data subject rights oversight, GDPR/FADP compliance, erasure request escalation |
| **CIO** | Technology infrastructure support, resource allocation |
| **Legal/Compliance** | Regulatory interpretation, retention requirements, litigation hold |
| **Executive Management** | Strategic approval, risk acceptance, remediation funding |

### 5.2 Operational Roles

| Role | Responsibilities |
|------|------------------|
| **Information Security Manager** | Policy ownership, enforcement, compliance monitoring |
| **Data Governance Team** | Data classification, retention schedules, deletion triggers |
| **IT Operations** | Technical deletion execution, tool management, media disposal |
| **System Owners** | Deletion implementation within their systems, evidence collection |
| **Database Administrators** | Database record deletion, backup purging |
| **Cloud/Vendor Management** | Third-party deletion verification, contract compliance |

### 5.3 Supporting Roles

| Role | Responsibilities |
|------|------------------|
| **Security Engineering** | Assessment tool development, generator scripts, validation |
| **Compliance & Audit** | Compliance verification, audit support, gap tracking |
| **Procurement** | Contract clauses for deletion, vendor selection criteria |
| **Physical Security** | Media destruction coordination, chain of custody |
| **HR** | Employee data deletion upon termination, awareness training |

### 5.4 User Responsibilities

| Role | Responsibilities |
|------|------------------|
| **All Users** | Report data for deletion, avoid unauthorized retention |
| **Data Owners** | Define retention requirements, approve deletion |
| **Records Managers** | Maintain retention schedules, coordinate destruction |

---

## 6. Assessment Methodology

### 6.1 System Engineering Approach

This framework employs **quantitative, evidence-based assessment** rather than checkbox compliance:

**Traditional Approach (Avoided):**
```
Auditor: "Do you delete data when no longer needed?"
Organization: "Yes"
Auditor: [checks box]
Reality: Unknown retention compliance, no deletion evidence, backup tapes from 2015 still in storage
```

**System Engineering Approach (Implemented):**
```
1. Run Python generator → produces standardized Excel workbook
2. Data governance/IT teams complete assessment with evidence
3. Validation scripts check for errors/issues
4. Normalization creates audit-ready filenames
5. Dashboard auto-aggregates compliance metrics
6. Quantitative results: "94.2% retention compliance, 847 deletion certificates collected,
   3 gaps identified (backup purge, legacy system, vendor X)"
```

### 6.2 Vendor-Agnostic Design

**Policy Layer** (ISMS-POL-A.8.10): Defines *what* deletion capabilities are required. No specific products, vendors, or cloud providers mentioned.

**Implementation Layer** (ISMS-IMP-A.8.10): Defines *how* requirements are met. Organizations document THEIR specific tools, providers, and processes.

**Provider Reference** (ISMS-REF-A.5.23): Pre-populated dropdown lists of common cloud/SaaS providers for consistent assessment without policy-level vendor lock-in.

### 6.3 Response Values

Assessment checklists use standardized response values:

| Value | Meaning | Action Required |
|-------|---------|-----------------|
| `Yes` | Fully implemented and documented | Maintain, provide evidence |
| `No` | Not implemented | Remediate or document exception |
| `Partial` | Partially implemented | Improvement plan required |
| `Planned` | Scheduled for implementation | Provide target date |
| `N/A` | Not applicable | Justify (e.g., media type not used) |

### 6.4 Assessment Cycle

**Frequency:** Quarterly (or upon significant change to data landscape, regulations, or provider relationships)

**Cycle:**
1. **Week 1:** Generate assessment workbooks, distribute to responsible teams
2. **Weeks 2-3:** Teams complete assessments, provide evidence
3. **Week 4:** Security/DPO reviews, validates, identifies gaps
4. **Week 5:** Dashboard generation, executive review, remediation planning
5. **Week 6:** Remediation initiation, tracking, sign-off

---

## 7. Integration with ISMS

### 7.1 Related Controls

Information deletion integrates with and supports multiple ISO 27001 controls:

| Control | Integration Point |
|---------|-------------------|
| **A.5.9** | Asset Inventory — Know what assets contain data requiring deletion |
| **A.5.10** | Acceptable Use — User responsibilities for data handling |
| **A.5.12** | Data Classification — Classification drives retention/deletion requirements |
| **A.5.13** | Labeling — Ensures data requiring deletion is identifiable |
| **A.5.33** | Protection of Records — Balance retention vs. deletion requirements |
| **A.5.34** | Privacy & PII Protection — GDPR/FADP deletion rights |
| **A.7.10** | Storage Media — Physical handling of media requiring deletion |
| **A.7.14** | Secure Disposal — Equipment disposal with data sanitization |
| **A.8.24** | Cryptography — Cryptographic erasure as deletion method |

### 7.2 Bidirectional Data Flows

**Information Deletion → Other Controls:**
- Deletion certificates → Audit & Compliance (evidence of disposal)
- Media destruction → Asset Management (asset decommissioning)
- Data subject requests → Privacy Management (GDPR compliance)
- Retention expiry → Records Management (lifecycle completion)

**Other Controls → Information Deletion:**
- Data Classification (A.5.12) → Retention periods based on classification
- Asset Inventory (A.5.9) → Identify systems/media requiring deletion
- Privacy Management (A.5.34) → Data subject erasure requests
- Legal Hold → Suspend deletion during litigation/investigation
- Contract Management → Contractual retention requirements

### 7.3 Risk Management Integration

**Risk Treatment:**
- Deletion controls as risk mitigation for data exposure
- Residual risks from incomplete deletion tracked in risk register
- Legal/regulatory risks from non-compliance with deletion obligations

**Risk Register:**
- Deletion risks documented in compliance dashboard (Domain 5)
- Risk scores drive remediation urgency
- Exception risks (extended retention) monitored and reported

---

## 8. Compliance & Audit

### 8.1 Audit Evidence Package

For internal and external audits, the following evidence is maintained:

| Evidence Type | Source | Location |
|---------------|--------|----------|
| Retention schedules | ISMS-IMP-A.8.10.1 | Data Governance |
| Deletion method documentation | ISMS-IMP-A.8.10.2 | IT Operations |
| Provider deletion SLAs | ISMS-IMP-A.8.10.3 | Vendor Management |
| Deletion certificates | ISMS-IMP-A.8.10.4 | Evidence Register |
| Data subject request log | ISMS-IMP-A.8.10.4 | DPO Office |
| Physical destruction certificates | ISMS-IMP-A.8.10.4 | Physical Security |
| Compliance dashboard | ISMS-IMP-A.8.10.5 | CISO Office |

### 8.2 Common Audit Findings (Prevention)

| Finding | Prevention Measure |
|---------|-------------------|
| "No documented retention policy" | ISMS-IMP-A.8.10.1 comprehensive retention matrix |
| "Cannot prove deletion occurred" | ISMS-IMP-A.8.10.4 evidence management |
| "Third-party deletion not verified" | ISMS-IMP-A.8.10.3 provider certificates |
| "Backup tapes never purged" | Include backups in media inventory |
| "Dev/test data not deleted" | Include non-production environments in scope |
| "Data subject requests not tracked" | Request log with SLA monitoring |

### 8.3 Regulatory Examination Readiness

**GDPR Article 17 (Right to Erasure):**
- Documented process for handling erasure requests
- Response within 30 days (with evidence)
- Notification to third parties who received data
- Exceptions documented (legal obligation, public interest, etc.)

**Swiss FADP:**
- Data minimization compliance
- Deletion upon purpose completion
- Data subject rights handling

---

## 9. Policy Governance

### 9.1 Policy Review

**Annual Review:** Full policy suite review by CISO, DPO, and Legal/Compliance

**Triggered Review:** Upon:
- Significant regulatory changes (GDPR amendments, new FADP guidance)
- Major organizational changes (M&A, new business lines)
- Significant incidents involving data retention/deletion
- Technology changes affecting deletion capabilities

### 9.2 Exception Management

Exceptions to deletion requirements require:
1. Written business justification
2. Risk assessment (data exposure, regulatory non-compliance)
3. Compensating controls (encryption, access restriction)
4. Approval by CISO and DPO
5. Time-limited approval with review date
6. Documentation in exception register

### 9.3 Non-Compliance Handling

Non-compliance with deletion policy may result in:
- Mandatory remediation with defined timeline
- Escalation to executive management
- Inclusion in risk register
- Disciplinary action (for willful non-compliance)
- Regulatory notification (if legally required)

---

## 10. Reference Documents

### 10.1 Internal Documents

**Policy Layer:**
- ISMS-POL-A.8.10 (this document) + Sections S1 through S5.D

**Assessment Layer:**
- ISMS-IMP-A.8.10.1 through A.8.10.5 (Markdown + Excel)

**Related ISMS Documents:**
- ISMS-POL-00 — Regulatory Applicability Framework
- ISMS-REF-A.5.23 — Cloud Service Provider Reference Registry
- ISMS-POL-A.5.12 — Classification of Information
- ISMS-POL-A.5.33 — Protection of Records
- ISMS-POL-A.5.34 — Privacy and PII Protection
- ISMS-POL-A.7.14 — Secure Disposal or Re-use of Equipment
- ISMS-POL-A.8.24 — Use of Cryptography

### 10.2 External Standards & Regulations

**International Standards:**
- ISO/IEC 27001:2022 — Information Security Management Systems
- ISO/IEC 27002:2022 — Information Security Controls (Control 8.10)
- ISO/IEC 27040 — Storage Security (sanitization guidance)
- ISO/IEC 27555 — Guidelines on PII Deletion
- ISO/IEC 27017 — Cloud Services Security (deletion guidance)

**Media Sanitization Standards:**
- NIST SP 800-88 Rev. 1 — Guidelines for Media Sanitization
- DoD 5220.22-M — National Industrial Security Program (legacy reference)
- DIN 66399 — Destruction of Data Media (paper, optical, magnetic)

**Regulatory:**
- Swiss Federal Act on Data Protection (FADP/nDSG)
- EU General Data Protection Regulation (GDPR) — Article 17
- Sector-specific regulations (as applicable)

---


## Appendix A: Implementation Principles

### A.1 Evidence-Based Verification

This framework emphasizes **substantive verification** over procedural documentation. Organizations must demonstrate operational effectiveness of deletion controls, not merely document policies and procedures.

**The assessment workbooks ensure specificity:**
- **What** data categories exist with defined retention periods?
- **When** does deletion trigger (expiry, request, contract end)?
- **How** is deletion performed per media type?
- **Whether** deletion occurred with verifiable evidence?

### A.2 Verification Requirements

Information deletion presents a unique compliance challenge: **demonstrating that information no longer exists**.

Traditional evidence: "Here is the data" ✓  
Deletion evidence: "Here is proof the data is gone" ✓✓ (requires systematic approach)

This framework addresses verification requirements through:
- Deletion certificates and logs
- Third-party destruction confirmations
- Cryptographic erasure verification
- Chain of custody documentation
- Audit trail of deletion activities

### A.3 Backup Infrastructure Scope

A critical consideration for deletion controls: **information persistence in backup systems**.

Organizations must address deletion across all data stores, including:
- Daily/weekly/monthly backup systems
- Disaster recovery replicas
- Cloud backup retention policies
- Database transaction logs
- System snapshots and archives

This framework explicitly includes backup infrastructure in the deletion scope to ensure comprehensive compliance.

---

**END OF MASTER POLICY**