<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.23.S2-UG:framework:UG:a.5.23 -->
**ISMS-IMP-A.5.23.S2-UG - Vendor Due Diligence & Contracts**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S2-UG |
| **Version** | 1.0 |
| **Assessment Area** | Vendor Due Diligence & Contracts |
| **Related Policy** | ISMS-POL-A.5.19-23-S2 (Supplier Agreement Requirements), ISMS-POL-A.5.19-23-S5 (Cloud Services Security) |
| **Purpose** | Assess vendor security posture, contract adequacy, SLA compliance, data sovereignty, audit rights, and jurisdictional risks for all cloud service providers |
| **Target Audience** | Legal, Procurement, Security Teams, Compliance Officers, Risk Managers |
| **Assessment Type** | Vendor Due Diligence & Contract Analysis |
| **Review Cycle** | Quarterly (with annual comprehensive review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial Excel workbook specification | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.23.S2-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.23.S2 - Vendor Due Diligence & Contracts

#### What This Assessment Covers

This assessment evaluates the **security and contractual posture** of ALL cloud service providers identified in your cloud service inventory (ISMS-IMP-A.5.23.1). This is where you verify that vendor claims match reality and that contracts protect [Organization]'s interests.

**Core Principle:**

**"Trust, but verify - every vendor relationship requires documented due diligence backed by objective evidence."**

This is NOT about:

- ❌ Accepting vendor marketing materials at face value
- ❌ Checkbox compliance ("they have ISO 27001, we're good")
- ❌ Assuming contracts protect you without reading them
- ❌ Skipping verification of vendor security claims

This IS about:

- ✅ Verifying vendor certifications are current and scoped correctly
- ✅ Ensuring contracts include required security clauses
- ✅ Monitoring SLA compliance with objective data
- ✅ Validating data residency and sovereignty requirements
- ✅ Confirming audit rights are exercisable, not just written
- ✅ Assessing jurisdictional risks (US CLOUD Act exposure)

#### What You'll Document

For EACH cloud service provider:

**Vendor Security Posture (Sheet 2):**

- Security certifications (ISO 27001, SOC 2 Type II, etc.)
- Certification validity and scope verification
- Penetration testing and security audit results
- Incident history and breach notifications

**Contract Adequacy (Sheet 3):**

- Contract type and key clauses
- Security requirements in agreements
- Data processing agreements (DPA) status
- Liability and indemnification terms
- Subprocessor authorization and notification
- Exit and data portability clauses

**SLA Compliance (Sheet 4):**

- Availability commitments and actual uptime
- Performance metrics and actuals
- Support response times
- SLA credits claimed vs. received
- Breach notification timing

**Data Sovereignty (Sheet 5):**

- Data storage and processing locations
- Cross-border transfer mechanisms (SCCs, BCRs)
- Encryption and key management
- Government access risks (CLOUD Act, FISA)

**Audit Rights (Sheet 6):**

- Contractual audit rights
- SOC 2/ISO reports availability
- On-site audit feasibility
- Security questionnaire completion
- Incident investigation cooperation

**Jurisdictional Risk (Sheet 7):**

- Vendor headquarters and ownership structure
- US CLOUD Act exposure assessment
- Transfer Impact Assessment (TIA) results
- Risk mitigation measures
- Residual risk acceptance

#### How This Relates to Other A.5.23 Assessments

```
┌────────────────────────────────────────────────────────────────┐
│                 A.5.19-23 FRAMEWORK FLOW                       │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    │
│  │ IMP-5.23.1   │ →  │ IMP-5.23.2   │ →  │ IMP-5.23.3   │    │
│  │ INVENTORY    │    │  THIS DOC    │    │ CONFIG       │    │
│  │ "What?"      │    │ "Who/Terms?" │    │ "How?"       │    │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘    │
│         │                   │                   │             │
│         └───────────────────┼───────────────────┘             │
│                             ▼                                 │
│                   ┌──────────────────┐                        │
│                   │  IMP-5.23.4      │                        │
│                   │  GOVERNANCE      │                        │
│                   │  "Ongoing?"      │                        │
│                   └────────┬─────────┘                        │
│                            │                                  │
│                            ▼                                  │
│                   ┌──────────────────┐                        │
│                   │  IMP-5.23.5      │                        │
│                   │  DASHBOARD       │                        │
│                   │  "Reporting"     │                        │
│                   └──────────────────┘                        │
└────────────────────────────────────────────────────────────────┘
```

**Upstream Dependency:** IMP-5.23.1 (Cloud Service Inventory)

- Provides list of vendors to assess
- Provides criticality and data classification
- Base columns (A-E) populated from inventory

**Downstream Consumers:**

- IMP-5.23.3 (Secure Configuration) - uses vendor certification data
- IMP-5.23.4 (Governance) - uses SLA and contract renewal data
- IMP-5.23.5 (Dashboard) - aggregates compliance metrics

### Who Should Complete This Assessment

#### Primary Stakeholders

| Role | Responsibility | Time Commitment |
|------|---------------|-----------------|
| **Legal / Procurement Lead** | Complete Sheets 3, 6 (contract analysis) | 8-12 hours |
| **Security / Compliance Officer** | Complete Sheets 2, 5, 7 (security posture, data sovereignty, jurisdictional risk) | 12-16 hours |
| **IT Operations / Service Owner** | Complete Sheet 4 (SLA compliance tracking) | 4-6 hours |
| **ISMS Coordinator** | Coordinate assessment, review results, manage approvals | 6-8 hours |

#### Required Skills

**Legal/Procurement:**

- Contract review and interpretation
- Negotiation experience with cloud vendors
- Understanding of SLA structures and remedies

**Security/Compliance:**

- ISO 27001, SOC 2, and common security frameworks
- Data protection regulations (GDPR, FADP, NIS2, DORA)
- Risk assessment methodologies

**IT Operations:**

- Vendor portal access and monitoring tools
- Performance metrics collection
- Incident tracking systems

#### Time Commitment

**Initial Assessment (First Time):**

- Data collection: 2-3 weeks
- Vendor engagement: 1-2 weeks (parallel)
- Evidence validation: 1 week
- Review and approval: 1 week
- **Total:** 4-6 weeks

**Quarterly Updates:**

- Review changes: 3-5 days
- Update evidence: 2-3 days
- Approval: 1-2 days
- **Total:** 1-2 weeks

**Assumptions:**

- ~15-25 cloud vendors to assess
- Vendors generally cooperative
- Contracts and certifications are accessible

#### Collaboration Model

**Week 1-2: Data Collection**

- Legal: Gather contracts, identify missing clauses
- Security: Collect certifications, verify validity
- IT Ops: Pull SLA performance data from monitoring

**Week 3-4: Vendor Engagement**

- Request missing certifications
- Request SOC 2 reports under NDA
- Clarify contract ambiguities
- Verify data residency claims

**Week 5: Gap Analysis**

- Identify missing certifications
- Identify inadequate contract terms
- Identify SLA breaches
- Risk assessment for gaps

**Week 6: Review & Approval**

- ISMS Coordinator consolidates findings
- Legal, Security, IT Ops review
- CISO approval
- Risk exceptions documented

### Expected Outputs

**Primary Deliverable:**

- **ISMS-IMP-A.5.23.S2_VendorDD_YYYYMMDD.xlsx** (10-sheet workbook)

**Workbook Contents:**

| Sheet | Title | Rows (Typical) | Purpose |
|-------|-------|----------------|---------|
| 1 | Instructions & Legend | N/A | How to use this workbook |
| 2 | 2. Security Certifications | 15-25 | ISO 27001, SOC 2, penetration tests |
| 3 | 3. Contract Terms | 15-25 | DPA, liability, exit clauses |
| 4 | 4. SLA Performance | 15-25 | Uptime, support, SLA credits |
| 5 | 5. Data Sovereignty | 15-25 | Residency, encryption, transfers |
| 6 | 6. Forensics & Audit | 15-25 | Audit clauses, SOC 2 access |
| 7 | 7. Jurisdictional Risk | 15-25 | CLOUD Act, TIA, risk mitigation |
| 8 | 8. Summary Dashboard | Auto-calc | Executive summary, metrics |
| 9 | 9. Evidence Register | 50-100 | Links to all evidence files |
| 10 | 10. Approval Sign-Of | N/A | Legal, Security, CISO approvals |

**Supporting Deliverables:**

- Evidence repository (contracts, certs, SLA reports)
- Gap analysis with remediation plan
- Risk register entries for accepted exceptions

### Assessment Success Criteria

**Completeness:**

- ✅ All vendors from IMP-5.23.1 assessed (no gaps)
- ✅ All required evidence collected and linked
- ✅ All status flags set (✅/⚠️/❌/N/A)
- ✅ All gaps identified with remediation plans
- ✅ All approvals obtained

**Quality:**

- ✅ Certifications verified directly with issuing bodies
- ✅ Contracts reviewed by qualified legal personnel
- ✅ SLA data from objective monitoring (not vendor self-reporting)
- ✅ Data residency verified (not assumed from marketing)
- ✅ Jurisdictional risks assessed with Transfer Impact Assessment

**Compliance:**

- ✅ All Critical services: ISO 27001 or SOC 2 Type II
- ✅ All contracts: DPA, security clauses, audit rights
- ✅ All EU data: Valid transfer mechanism (SCCs/BCRs/Adequacy)
- ✅ DORA/NIS2 requirements met for in-scope services
- ✅ Residual risks formally accepted by CISO

**Traceability:**

- ✅ Every "Compliant" status → Evidence file exists
- ✅ Every gap → Remediation plan or risk exception
- ✅ Every vendor → Linked to IMP-5.23.1 inventory
- ✅ Evidence register → All links work, files accessible

### Common Use Cases

**Use Case 1: New Vendor Onboarding**
*A business unit wants to adopt Notion for project management.*

**Assessment Flow:**
1. Add to IMP-5.23.1 inventory first
2. Complete IMP-5.23.2 assessment:

   - Request ISO 27001 certificate from Notion
   - Review contract for DPA, security clauses
   - Verify data residency (Notion uses AWS)
   - Assess CLOUD Act exposure (US company)
   - Complete Transfer Impact Assessment

3. Identify gaps (e.g., missing SOC 2 Type II)
4. Risk decision: Accept with compensating controls OR reject
5. If approved → proceed to IMP-5.23.3 (secure configuration)

**Use Case 2: Contract Renewal**
*Microsoft 365 contract expires in 90 days.*

**Assessment Flow:**
1. Pull existing IMP-5.23.2 assessment
2. Update Sheet 4 (SLA compliance) with last 12 months data
3. Review Sheet 3 (contract terms) - are there gaps to negotiate?
4. Check Sheet 2 (certifications) - are they current?
5. Legal uses assessment as negotiation input
6. Update assessment post-renewal with new terms

**Use Case 3: Audit Preparation**
*External ISO 27001 auditor is coming in 30 days.*

**Assessment Flow:**
1. Verify all assessments complete and current (<90 days old)
2. Check all evidence links work
3. Validate all "Compliant" status flags are justified
4. Ensure all gaps have documented risk exceptions
5. Generate summary report from Sheet 8 (Dashboard)
6. Prepare Sheet 10 (Approval Sign-Off) for auditor review

**Use Case 4: Regulatory Change Response**
*DORA Article 28.6 now requires annual exit strategy testing.*

**Assessment Flow:**
1. Identify all Critical ICT providers (DORA scope)
2. Review Sheet 7 for existing exit strategy documentation
3. Add new column: "PoC Test Date" and "PoC Test Result"
4. Plan annual proof-of-concept migration tests
5. Update assessment quarterly with test results
6. Report to risk committee on exit feasibility

---

## Prerequisites & Preparation

### Required Inputs

**From IMP-5.23.1 (Cloud Service Inventory):**

- ✅ Complete and approved inventory
- ✅ Vendor list with criticality ratings
- ✅ Data classification for each service
- ✅ Service owner assignments
- ✅ Contract owner identification

**Internal Systems Access:**

- ✅ Contract management system (SharePoint, DocuSign, etc.)
- ✅ Procurement system (vendor records, PO history)
- ✅ Monitoring/ITSM (SLA performance data)
- ✅ Evidence repository (file share or document management)

**Vendor Access/Credentials:**

- ✅ Vendor admin portals (to verify configurations)
- ✅ Trust centers (AWS Artifact, Microsoft Trust Center, etc.)
- ✅ Support portals (to request certifications under NDA)

### Required Materials

**From Vendors (Request if Missing):**

| Material | Purpose | How to Obtain |
|----------|---------|---------------|
| **ISO 27001 Certificate** | Verify security management system | Vendor website, trust center, or request from vendor account manager |
| **SOC 2 Type II Report** | Verify controls over 12 months | Request under NDA from vendor (sales or compliance contact) |
| **Penetration Test Summary** | Verify external security testing | Request from vendor security team (may be redacted) |
| **DPA (Data Processing Agreement)** | GDPR/FADP compliance | Should be annexed to contract; if missing, request from legal |
| **Subprocessor List** | Supply chain transparency | Vendor trust center or privacy documentation |
| **SLA Performance Reports** | Validate uptime claims | Vendor status page, support portal, or admin dashboard |
| **Data Residency Documentation** | Verify storage/processing locations | Admin console settings, DPA, or vendor documentation |

**Internal Documents:**

| Document | Purpose | Location |
|----------|---------|----------|
| **Contracts (MSA, DPA, Order Forms)** | Contract terms analysis | Procurement, Legal department, contract management system |
| **Vendor Invoices** | Validate spend, contract terms | Finance system, procurement records |
| **SLA Breach Records** | Quantify vendor performance | ITSM system (incident tickets), monitoring dashboards |
| **Incident Reports** | Vendor-caused incidents | Incident management system, security team records |
| **Previous Audits / Assessments** | Baseline for comparison | ISMS repository, audit files |

### Stakeholder Coordination

**Before Starting:**

1. **Schedule Kickoff Meeting** (90 minutes)

   - Legal, Procurement, Security, IT Ops, Service Owners
   - Present assessment scope and timeline
   - Assign sheets to responsible parties
   - Establish communication channel (Slack, Teams)

2. **Establish Evidence Repository**

   - Create folder structure: `/ISMS/Evidence/A.5.23.2/[Vendor_Name]/`
   - Set permissions (Legal, Security, Auditors)
   - Document naming convention: `[Vendor]_[DocType]_YYYYMMDD.pdf`

3. **Prepare Vendor Communication**

   - Draft template email requesting certifications
   - Identify vendor contacts (account manager, compliance, legal)
   - Set expectations: 2-week response time for requests

### Tool Requirements

**Software:**

- Excel 2016+ or Google Sheets
- PDF reader (for contracts, certifications)
- Screenshot tool (Snipping Tool, Greenshot, Snagit)

**Access:**

- Vendor admin consoles (Service Owners)
- Contract management system (Legal, Procurement)
- Monitoring dashboards (IT Ops)
- ITSM/ticketing system (IT Ops)

---

## Understanding the Assessment Sheets

### Base Columns (A-Q) - Standard Across All Sheets

**All data collection sheets (2-7) share these base columns:**

| Column | Header | Source | Purpose |
|--------|--------|--------|---------|
| **A** | Cloud Service Name | IMP-5.23.1 | Service as YOU know it (not vendor's product name) |
| **B** | Vendor Name | IMP-5.23.1 | Provider's legal name (for contract matching) |
| **C** | Service Type | IMP-5.23.1 | SaaS, IaaS, PaaS, Security Service, etc. |
| **D** | Service Criticality | IMP-5.23.1 | Critical, High, Medium, Low (from inventory) |
| **E** | Data Classification | IMP-5.23.1 | Restricted, Confidential, Internal, Public |
| **F** | Contract Type | Contract | MSA+DPA, Subscription, Enterprise Agreement |
| **G** | Contract Start Date | Contract | When contract became effective |
| **H** | Status | Assessment | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant / N/A |
| **I** | Evidence Location | Sheet 9 | Link/reference to evidence files |
| **J** | Gap Description | Assessment | What's missing or inadequate (if status ≠ ✅) |
| **K** | Remediation Needed | Assessment | Yes/No (gaps requiring action) |
| **L** | Exception ID | Risk Register | If gap accepted: reference to risk exception |
| **M** | Risk ID | Risk Register | Reference to risk register entry |
| **N** | Compensating Controls | Security | Mitigating measures for gaps |
| **O** | Vendor Contact (Legal) | Contract/Portal | Vendor legal/compliance contact email |
| **P** | Target Remediation Date | Remediation Plan | When gap will be closed |
| **Q** | Contract Owner | Procurement | Internal person responsible for vendor relationship |

**Important:**

- Columns A-E are **copied from IMP-5.23.1** (maintain consistency)
- Do NOT re-assess criticality or data classification here
- Status (Column H) is **sheet-specific** (varies by assessment focus)
- Evidence Location (Column I) references **Sheet 9** (centralized evidence tracking)

### Extended Columns (R+) - Sheet-Specific

Each data collection sheet has **extended columns** specific to its assessment focus:

| Sheet | Extended Columns | Focus Area |
|-------|------------------|------------|
| **Sheet 2** | R-Y | Certification types, validity dates, scope verification |
| **Sheet 3** | R-Z | Contract clauses (DPA, liability, exit, subprocessors) |
| **Sheet 4** | R-X | SLA commitments, actuals, breach counts, credits |
| **Sheet 5** | R-Y | Data residency, encryption, transfer mechanisms |
| **Sheet 6** | R-W | Audit rights, SOC 2 access, forensics support |
| **Sheet 7** | R-AA | Jurisdictional risk, CLOUD Act, TIA results |

**See Part II (Technical Specification) for complete column definitions.**

### Data Flow & Dependencies

**Input Flow:**
```
IMP-5.23.1 Inventory (Columns A-E)
        ↓
    Sheets 2-7 (Base + Extended columns)
        ↓
    Sheet 8 (Dashboard - auto-calculated)
        ↓
    Sheet 9 (Evidence Register)
        ↓
    Sheet 10 (Approvals)
```

**Cross-Sheet Integration:**

- Sheet 9 (Evidence Register) ← All evidence links from Sheets 2-7
- Sheet 8 (Dashboard) ← Compliance metrics from Sheets 2-7
- Sheet 10 (Approvals) ← Triggered after Sheets 2-9 complete

### Status Flag Meanings

**Consistent across all sheets:**

| Status | Symbol | Meaning | When to Use |
|--------|--------|---------|-------------|
| **Compliant** | ✅ | Requirement fully met with evidence | All required elements present, verified, and documented |
| **Partial** | ⚠️ | Requirement partially met | Some elements present but gaps exist |
| **Non-Compliant** | ❌ | Requirement not met | Significant gaps, missing controls, or no evidence |
| **N/A** | N/A | Not applicable to this service | Requirement doesn't apply (document why in Gap Description) |

**Key Principle:** Every status requires justification:

- ✅ → Evidence file must exist (Sheet 9)
- ⚠️ → Gap description required (Column J)
- ❌ → Gap + remediation plan required (Columns J, K, P)
- N/A → Rationale documented (Column J)

### Sheet Completion Order

**Recommended Sequence:**

1. **Sheet 2 (Security Certifications)** - Start here (fastest to complete)
2. **Sheet 3 (Contract Terms)** - Requires legal review
3. **Sheet 5 (Data Sovereignty)** - Often linked to Sheet 3 (DPA)
4. **Sheet 6 (Audit Rights)** - Linked to Sheet 3 (contract clauses)
5. **Sheet 7 (Jurisdictional Risk)** - Requires Sheet 5 data
6. **Sheet 4 (SLA Performance)** - Can be parallel (IT Ops)
7. **Sheet 9 (Evidence Register)** - As you complete Sheets 2-7
8. **Sheet 8 (Dashboard)** - Auto-calculated (verify formulas)
9. **Sheet 10 (Approvals)** - After all sheets complete

**Rationale:** Build from foundational data (certifications) to dependent assessments (risk).

### Regulatory Applicability Guide

**Which sheets apply to which regulations:**

| Regulation | Applicable Sheets | Key Requirements |
|------------|-------------------|------------------|
| **GDPR / FADP** | Sheets 3, 5, 7 | DPA required, data residency, transfer mechanisms, TIA |
| **DORA** | Sheets 2, 3, 4, 6 | ICT provider certifications, contract clauses, SLA monitoring, audit rights |
| **NIS2** | Sheets 2, 3, 4 | Security certifications, incident notification clauses, supply chain security |
| **EU AI Act** | Sheets 2, 3 | If using AI services: provider certifications, liability clauses |
| **US CLOUD Act** | Sheet 7 | Jurisdictional risk assessment for US-based providers |

**See ISMS-POL-00 (Regulatory Applicability Framework) for detailed requirements.**

---

## Completing Each Sheet - Detailed Guidance

### Overview

This section provides step-by-step guidance for completing each data collection sheet (Sheets 2-7).

**Structure for each sheet:**
1. Purpose - Why this sheet matters
2. What to Document - Key data points
3. How to Complete - Step-by-step with tables
4. Common Mistakes - Key gotchas
5. Example Entry - One good example

**Base Columns (A-Q):** See previous section. These are standard across all sheets.

**Extended Columns (R+):** Sheet-specific, documented below.

---

## Sheet 2: Vendor Security Certifications

### Purpose

Verify that vendors hold current, valid security certifications appropriate for the criticality and data classification of services they provide. Certifications provide independent assurance of vendor security controls.

**Success Criterion:** All Critical and High services are provided by vendors with current ISO 27001 or SOC 2 Type II certification, verified directly with issuing bodies.

### What to Document

For each vendor:

- ISO 27001 certification (certificate, accreditation body, expiry, scope)
- SOC 2 Type II report (auditor, period, opinion, scope)
- Penetration testing (frequency, scope, critical findings)
- Incident history (breaches in last 24 months, notification compliance)
- Other relevant certifications (PCI-DSS, HIPAA, FedRAMP, etc.)

### How to Complete

**Step 1: Request Certifications from Vendor**

| Certification | How to Request | Expected Response Time |
|---------------|----------------|------------------------|
| ISO 27001 Certificate | Public (vendor website, trust center) | Immediate |
| SOC 2 Type II Report | Request under NDA (vendor compliance team) | 5-10 business days |
| Penetration Test Summary | Request from vendor security (may be redacted) | 10-15 business days |
| Incident Reports | Public status page, or request from vendor support | Varies |

**Template Email:**
```
Subject: Security Certification Request - [Your Organization]

Dear [Vendor Compliance Contact],

As part of our vendor risk management program (ISO 27001:2022 Control A.5.23), 
we require the following security documentation for [Service Name]:

1. Current ISO 27001 certificate (with scope)
2. Most recent SOC 2 Type II report (under NDA if required)
3. Summary of latest penetration testing results
4. Any security incidents in the last 24 months

Please provide by [Date + 10 business days].

Thank you,
[Your Name], [Title]
```

**Step 2: Verify Certification Validity**

**ISO 27001:**

- Check certificate against IAF accreditation database
- Verify certification body is accredited (UKAS, DAkkS, ANAB, etc.)
- Confirm service is within certification scope
- Check expiry date (≥3 months remaining)

**SOC 2 Type II:**

- Verify auditor is reputable (Big 4, recognized regional firm)
- Check audit period (must be ≥12 months for Type II)
- Review opinion (unqualified/clean opinion required)
- Check scope covers relevant Trust Service Criteria

**Step 3: Complete Extended Columns**

| Column | Field | How to Complete | Evidence |
|--------|-------|-----------------|----------|
| R | ISO 27001 Status | Yes/No/Expired/In Progress | Certificate PDF |
| S | ISO 27001 Cert Number | Certificate ID from cert body | Certificate PDF |
| T | ISO 27001 Expiry Date | Expiry date from certificate | Certificate PDF |
| U | ISO 27001 Scope Verified | Service in scope? Yes/No/Partial | Certificate scope statement |
| V | SOC 2 Type II Status | Yes/No/Type I Only/Expired | SOC 2 report cover page |
| W | SOC 2 Audit Period | Start - End dates | SOC 2 report |
| X | SOC 2 Opinion | Unqualified/Qualified/Adverse | SOC 2 auditor opinion |
| Y | Penetration Testing | Annual/Semi-Annual/None | Pen test summary or cert |

**Step 4: Set Status Flag**

| Scenario | Status | Gap Description (if ≠ ✅) |
|----------|--------|---------------------------|
| ISO 27001 valid + SOC 2 Type II valid + service in scope | ✅ | - |
| ISO 27001 valid + SOC 2 Type I only | ⚠️ | "SOC 2 Type I only (point-in-time, not 12-month)" |
| ISO 27001 valid + No SOC 2 | ⚠️ | "No SOC 2 report available" |
| No ISO 27001 + No SOC 2 | ❌ | "No recognized security certification" |
| ISO 27001 expired | ❌ | "ISO 27001 expired [Date]" |
| Service not in ISO scope | ❌ | "Service not covered by ISO 27001 certification scope" |
| Low criticality + No certs | N/A | "Certification not required for Low criticality services" |

### Common Mistakes

❌ **Accepting marketing claims** - "ISO 27001 certified" on website without verifying certificate  
❌ **Not checking scope** - Certificate exists but doesn't cover your specific service  
❌ **SOC 2 Type I vs Type II** - Type I is point-in-time; Type II is 12-month operational effectiveness  
❌ **Expired certifications** - Certificate was valid at contract signing but expired since  
❌ **Unaccredited certifiers** - "ISO 27001" from non-accredited certification body  
❌ **Not requesting under NDA** - Vendor refuses to share SOC 2 because you didn't sign NDA  

### Example Entry

**Good Example:**

| A | B | C | D | E | F | G | H | I | R | S | T | U | V | W | X | Y |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Microsoft 365 | Microsoft Corp. | SaaS | Critical | Confidential | MSA+DPA | 01.01.2024 | ✅ | /evidence/msft/iso27001.pdf | Yes | IS 123456 | 30.06.2026 | Yes | Yes | 01.04.2024-31.03.2025 | Unqualified | Annual |

---

## Sheet 3: Contract Terms Analysis

### Purpose

Ensure contracts include required security clauses to protect [Organization]'s interests. This includes data processing agreements, liability terms, exit clauses, and subprocessor controls.

**Success Criterion:** All contracts include DPA, security requirements, audit rights, liability caps ≥€1M, and data portability clauses.

### What to Document

For each contract:

- Contract type and structure (MSA, DPA, Order Forms)
- Data Processing Agreement (DPA) presence and adequacy
- Security requirements and SLAs in contract
- Liability and indemnification terms
- Subprocessor notification and approval
- Exit and data portability clauses
- Contract renewal dates and auto-renewal terms

### How to Complete

**Step 1: Gather Contract Documents**

**Typical Cloud Contract Structure:**
```
Master Services Agreement (MSA)
    ├── Data Processing Agreement (DPA) - GDPR/FADP compliance
    ├── Service Level Agreement (SLA) - Availability commitments
    ├── Security Exhibit - Technical/organizational measures
    └── Order Forms / Statements of Work
```

**Where to Find:**

- Contract management system (SharePoint, DocuSign, Concord)
- Procurement records (PO references)
- Vendor portal (signed agreements often downloadable)
- Legal department files

**Step 2: Review Contract Clauses**

| Clause Category | Required Elements | Where to Find |
|-----------------|-------------------|---------------|
| **Data Processing Agreement** | Processor obligations, sub-processors, data subject rights, SCCs/BCRs | Annex or standalone DPA |
| **Security Requirements** | Encryption, access controls, logging, incident notification | Security exhibit or MSA |
| **Liability** | Liability cap (€€€), indemnification for breaches, exclusions | MSA general terms |
| **Audit Rights** | Right to audit, third-party audits (SOC 2), frequency | MSA or DPA |
| **Exit / Termination** | Data export format, deletion timelines, assistance obligations | MSA termination clause |
| **Subprocessors** | Notification requirement, approval process, liability chain | DPA section 4-5 |

**Step 3: Complete Extended Columns**

| Column | Field | How to Assess | Evidence |
|--------|-------|---------------|----------|
| R | DPA Status | Present/Absent/Under Negotiation | DPA document or MSA annex |
| S | DPA Adequate? | Yes/No/Partial (missing elements) | Legal review notes |
| T | Security Reqs in Contract | Yes/No/Generic | MSA security exhibit |
| U | Liability Cap (€) | Amount (e.g., €5M, Unlimited, None) | MSA liability clause |
| V | Liability Adequate? | Yes (≥€1M) / No (<€1M) / None | Legal assessment |
| W | Subprocessor Notification | Prior Notice/Post-Notice/None | DPA clause X.Y |
| X | Subprocessor Approval | Opt-Out Right/No Control | DPA clause X.Z |
| Y | Exit Clause Present | Yes/No | MSA termination section |
| Z | Data Portability Guaranteed | Yes/No/On Request | MSA or DPA exit terms |

**Step 4: Set Status Flag**

| Scenario | Status | Gap Description |
|----------|--------|-----------------|
| DPA + Security Reqs + Liability ≥€1M + Exit clause | ✅ | - |
| DPA present but missing SCCs/BCRs | ⚠️ | "DPA missing Standard Contractual Clauses" |
| No DPA for service processing personal data | ❌ | "No DPA - GDPR/FADP violation" |
| Liability cap <€1M for Critical service | ⚠️ | "Liability cap €[X] insufficient for criticality" |
| No exit/portability clause | ⚠️ | "No contractual data portability guarantee" |
| Free/trial service (no contract) | ❌ | "No formal contract - shadow IT" |

### Common Mistakes

❌ **Assuming DPA exists** - "It's a cloud service, they must have a DPA" (verify!)  
❌ **Not reading liability exclusions** - Cap exists but excludes IP infringement, data breaches  
❌ **Accepting "reasonable efforts"** - Vague language instead of firm commitments  
❌ **Ignoring auto-renewal** - Contract auto-renews without price cap or exit opportunity  
❌ **Not checking subprocessor list** - DPA allows subprocessors but vendor doesn't publish list  
❌ **Accepting vendor standard terms** - "This is our standard contract, non-negotiable" (negotiate!)  

### Example Entry

| A | B | C | D | E | H | I | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Salesforce CRM | Salesforce Inc. | SaaS | Critical | Confidential | ✅ | /evidence/sfdc/contract.pdf | Present | Yes (SCCs included) | Yes | €5M | Yes | Prior Notice (30 days) | Opt-Out Right | Yes | Yes |

---

## Sheet 4: SLA Requirements & Performance

### Purpose

Monitor vendor compliance with Service Level Agreements and quantify service quality. This provides objective data for vendor performance evaluation and contract renewal negotiations.

**Success Criterion:** All Critical services meet SLA commitments with <1% breach rate. All SLA credits owed are claimed and received.

### What to Document

For each service:

- Availability commitments (uptime %, allowed downtime)
- Actual availability achieved (from monitoring)
- Performance metrics (response time, throughput)
- Support response times (ticket resolution SLAs)
- SLA breach events (count, duration, impact)
- SLA credits (owed vs. claimed vs. received)

### How to Complete

**Step 1: Identify SLA Commitments**

**Where to Find SLA Terms:**

- Contract Annex B (Service Level Agreement)
- Vendor service description document
- Public SLA page (AWS, Azure, GCP publish SLAs)

**Common SLA Types:**

| SLA Type | Typical Commitment | Measurement Method |
|----------|--------------------|--------------------|
| **Availability / Uptime** | 99.9% monthly uptime | Service availability monitoring |
| **Performance** | API response <200ms (P95) | Application Performance Monitoring |
| **Support Response** | P1: 1 hour, P2: 4 hours, P3: 24 hours | Ticket system timestamps |
| **Incident Resolution** | P1: 4 hours, P2: 24 hours, P3: 5 days | Ticket close timestamps |
| **Data Recovery** | RTO: 4 hours, RPO: 1 hour | DR test results |

**Step 2: Collect Performance Data**

**Data Sources:**

| Metric | Source | Frequency |
|--------|--------|-----------|
| Uptime % | Vendor status page, own monitoring (Pingdom, Datadog) | Monthly |
| Incident count | Vendor status page, ITSM tickets | Monthly |
| Support ticket SLA | ITSM system reports | Quarterly |
| Performance metrics | APM tools (New Relic, Dynatrace) | Real-time |

**Important:** Use YOUR monitoring data, not vendor self-reporting (trust but verify).

**Step 3: Calculate SLA Compliance**

**Formula:**
```
SLA Compliance % = (Actual Uptime % / Committed Uptime %) × 100

Example:
Committed: 99.9% (43.2 minutes downtime allowed per month)
Actual: 99.95% (21.6 minutes downtime)
Compliance: (99.95 / 99.9) × 100 = 100.05% → PASS
```

**SLA Breach:**
```
If Actual < Committed → Breach

Example:
Committed: 99.9%
Actual: 99.7% (129.6 minutes downtime)
Breach: YES (86.4 minutes excess downtime)
```

**Step 4: Complete Extended Columns**

| Column | Field | How to Calculate | Evidence |
|--------|-------|------------------|----------|
| R | SLA Uptime Commitment | From contract (e.g., 99.9%) | SLA document |
| S | Actual Uptime (Last Quarter) | From monitoring | Monitoring dashboard export |
| T | SLA Breaches (Count) | Number of months below SLA | Incident log |
| U | Total Downtime (Minutes) | Sum of all outages | Monitoring data |
| V | SLA Credits Owed (€) | Per contract credit formula | Contract + breach data |
| W | SLA Credits Claimed (€) | What you've requested | Support tickets |
| X | SLA Credits Received (€) | What vendor paid | Finance records, invoices |

**Step 5: Set Status Flag**

| Scenario | Status | Gap Description |
|----------|--------|-----------------|
| Actual ≥ SLA commitment + No missed credits | ✅ | - |
| Actual ≥ SLA but credits not claimed | ⚠️ | "€[X] in SLA credits owed but not claimed" |
| 1-2 breaches in 12 months, credits received | ⚠️ | "[N] breaches in last 12 months" |
| Persistent breaches (≥3 in 12 months) | ❌ | "Chronic SLA violations - consider vendor review" |
| No SLA in contract | ❌ | "No formal SLA commitments" |
| Monitoring not configured | ❌ | "No objective SLA measurement in place" |

### Common Mistakes

❌ **Trusting vendor status page** - Vendor reports 99.99%, your monitoring shows 99.7%  
❌ **Not claiming credits** - "It's only €100, not worth the paperwork" (claim ALL credits!)  
❌ **Accepting excuses** - "Outage was DDoS, excluded from SLA" (verify exclusion clause)  
❌ **Not tracking partial outages** - 50% degraded performance = 50% downtime for SLA  
❌ **Manual SLA tracking** - Use automation (monitoring tools, dashboards)  
❌ **No SLA for Critical services** - "Free tier doesn't have SLA" (unacceptable for Critical!)  

### Example Entry

| A | B | C | D | E | H | I | R | S | T | U | V | W | X |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AWS EC2 | Amazon Web Services | IaaS | Critical | Confidential | ⚠️ | /evidence/aws/sla_report.pdf | 99.99% | 99.97% | 1 | 13 min | €250 | €250 | €0 |

**Gap:** "€250 in SLA credits claimed but not yet received (pending vendor processing)"

---

## Sheet 5: Data Sovereignty Compliance

### Purpose

Verify data storage and processing locations comply with regulatory requirements (GDPR, FADP, NIS2, DORA). Ensure cross-border data transfers have valid legal mechanisms (SCCs, BCRs, Adequacy Decisions).

**Success Criterion:** All Restricted/Confidential data has verified residency in approved jurisdictions with valid transfer mechanisms for any cross-border flows.

### What to Document

For each service:

- Data storage location(s) - where data is stored at rest
- Data processing location(s) - where data is computed/analyzed
- Cross-border transfers (if any)
- Transfer mechanism (SCCs, BCRs, Adequacy Decision)
- Encryption status (at-rest, in-transit, key management)
- Data residency controls (ability to restrict to specific regions)

### How to Complete

**Step 1: Verify Data Storage Location**

**How to Determine:**

| Method | Reliability | How to Use |
|--------|-------------|------------|
| **Admin Console** | HIGH | Check service settings (AWS: region selector, Azure: resource location) |
| **DPA Schedule** | HIGH | Data Processing Addendum typically lists data center locations |
| **Vendor Documentation** | MEDIUM | Trust center, privacy policy (verify against admin console) |
| **Ask Vendor** | LOW | Request written confirmation (verify claims) |

**Common Cloud Regions:**

| Region Code | Location | GDPR/FADP Status |
|-------------|----------|------------------|
| eu-central-1 | Frankfurt, Germany | ✅ EU/EEA |
| eu-west-1 | Ireland | ✅ EU/EEA |
| eu-west-2 | London, UK | ⚠️ Adequate (post-Brexit) |
| us-east-1 | Virginia, USA | ❌ Non-adequate (requires SCCs) |
| us-west-2 | Oregon, USA | ❌ Non-adequate (requires SCCs) |
| ap-southeast-1 | Singapore | ❌ Non-adequate (requires SCCs) |

**Step 2: Identify Cross-Border Transfers**

**Transfer Occurs When:**

- Data stored in EU/EEA but processed in USA (e.g., support staff in USA access data)
- Backups replicated to non-EU region
- Vendor uses subprocessors in non-adequate countries
- CDN caches data globally

**Example Scenarios:**

**Scenario 1: Salesforce (EU Instance)**

- Primary: Germany (eu-central-1)
- Backup: Netherlands (eu-west-1)
- Processing: Germany
- Support Access: USA (if EU data boundary NOT enabled)
- **Transfer:** YES (if US support access enabled)
- **Mechanism Required:** SCCs

**Scenario 2: AWS S3 (EU-Only)**

- Bucket region: eu-west-1 (Ireland)
- Replication: NONE (single region)
- Processing: eu-west-1 only
- **Transfer:** NO
- **Mechanism Required:** N/A

**Step 3: Verify Transfer Mechanism**

**Valid Transfer Mechanisms (GDPR Article 46):**

| Mechanism | Description | When to Use | Verification |
|-----------|-------------|-------------|--------------|
| **SCCs** | Standard Contractual Clauses (EU Commission approved) | Most common for cloud services | Check DPA includes SCCs (Module 2: Controller-Processor) |
| **BCRs** | Binding Corporate Rules | Large enterprises with intra-group transfers | Verify BCR approval from EU DPA |
| **Adequacy Decision** | EU Commission adequacy finding | UK, Switzerland, Canada, Japan, etc. | Check EU Commission adequacy list |
| **TIA Required** | Transfer Impact Assessment | For transfers to USA under SCCs (post-Schrems II) | Legal/DPO assessment document |

**Post-Schrems II Requirements (US Transfers):**

- SCCs alone are NOT sufficient
- Requires Transfer Impact Assessment (TIA)
- Must assess US surveillance law risk (FISA 702, EO 12333)
- Additional safeguards may be required (encryption + key control)

**Step 4: Assess Encryption & Key Management**

| Encryption Type | Purpose | Verification |
|-----------------|---------|--------------|
| **At-Rest** | Protects stored data | Vendor docs, admin console (e.g., AWS S3 encryption) |
| **In-Transit** | Protects data during transmission | TLS 1.2+ enforced, check connection |
| **Key Management** | Who controls encryption keys? | Vendor-managed (default) OR customer-managed (BYOK, HYOK) |

**Customer-Managed Keys (CMK) Benefits:**

- Vendor cannot decrypt data without your key
- Mitigates some US CLOUD Act risks
- Adds complexity (key rotation, backup)

**Step 5: Complete Extended Columns**

| Column | Field | How to Verify | Evidence |
|--------|-------|---------------|----------|
| R | Data Storage Location | Admin console or DPA | Screenshot or DPA schedule |
| S | Data Processing Location | Same or different from storage | Vendor documentation |
| T | Cross-Border Transfer | Yes/No | Analysis of storage + processing + support |
| U | Transfer Mechanism | SCCs/BCRs/Adequacy/None | DPA Annex, contract |
| V | SCCs Present in DPA | Yes/No/N/A | DPA document (search for "Standard Contractual Clauses") |
| W | TIA Completed (if US transfer) | Yes/No/N/A | DPO assessment document |
| X | Encryption At-Rest | Yes/No/Partial | Vendor docs, admin console |
| Y | Encryption In-Transit | Yes (TLS 1.2+)/No | Connection test, vendor docs |
| Z | Key Management | Vendor/Customer (BYOK)/Hybrid | Admin console, key management service |

**Step 6: Set Status Flag**

| Scenario | Status | Gap Description |
|----------|--------|-----------------|
| EU-only storage + No transfer + Encryption | ✅ | - |
| US storage + SCCs + TIA + Encryption | ✅ | "US transfer with valid SCCs, TIA approved" |
| US storage + SCCs + No TIA | ⚠️ | "TIA required for US transfer (post-Schrems II)" |
| US storage + No SCCs | ❌ | "Cross-border transfer without legal mechanism" |
| No encryption at rest | ⚠️ | "No encryption at rest" |
| Unknown data location | ❌ | "Data residency not verified" |

### Common Mistakes

❌ **Assuming EU vendor = EU data** - Vendor HQ in EU but uses US cloud infrastructure  
❌ **Trusting marketing** - "GDPR compliant" doesn't mean EU-only data residency  
❌ **Ignoring backups** - Primary in EU, backups replicate to USA → transfer occurs  
❌ **Forgetting support access** - US support staff access EU data → transfer occurs  
❌ **SCCs without TIA** - Post-Schrems II requires TIA for US transfers (not just SCCs)  
❌ **Not enabling EU data boundary** - Service supports it but not enabled by default  

### Example Entry

| A | B | C | D | E | H | I | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Microsoft 365 | Microsoft Corp. | SaaS | Critical | Confidential | ✅ | /evidence/msft/dpa.pdf | EU Multi-Geo (DE, NL) | EU-only | No | N/A | N/A | N/A | Yes (AES-256) | Yes (TLS 1.3) | Vendor |

---

## Sheet 6: Forensics & Audit Rights

### Purpose

Verify contractual audit rights are exercisable and that vendor provides adequate support for security investigations, forensics, and compliance audits.

**Success Criterion:** All Critical/High services have contractual audit rights AND vendor provides annual SOC 2 Type II reports.

### What to Document

For each service:

- Contractual audit rights (right to audit clause)
- SOC 2 report availability (can you access it?)
- On-site audit feasibility (vendor allows physical visits?)
- Security questionnaire completion
- Incident investigation cooperation
- Forensics data availability (logs, access records)

### How to Complete

**Step 1: Review Contract Audit Clauses**

**Common Audit Right Patterns:**

| Clause Type | Description | Assessment |
|-------------|-------------|------------|
| **Right to Audit** | Customer can conduct audit with [X] days notice | ✅ GOOD (verify frequency limit) |
| **SOC 2 in Lieu** | Vendor provides SOC 2, customer waives audit right | ⚠️ ACCEPTABLE if SOC 2 Type II |
| **No Audit Rights** | Contract silent or explicitly prohibits audits | ❌ UNACCEPTABLE for Critical services |
| **Vendor Discretion** | "Vendor may permit audits at its discretion" | ❌ Not a right if discretionary |

**Key Audit Right Elements:**

| Element | Requirement | Where to Find |
|---------|-------------|---------------|
| **Frequency** | At least annually (or on reasonable cause) | Audit clause section |
| **Notice Period** | 30-60 days advance notice | Audit clause |
| **Scope** | Can audit security controls, data handling | Audit clause |
| **Cost** | Who pays? (Ideally vendor, or split) | Audit clause |
| **Third-Party** | Can use independent auditor | Audit clause |

**Step 2: Verify SOC 2 Report Availability**

**Process:**
1. Request SOC 2 Type II report from vendor
2. Sign NDA if required
3. Receive report (PDF, typically 50-150 pages)
4. Verify:

   - Report is Type II (12-month, not Type I point-in-time)
   - Audit period is recent (<18 months old)
   - Opinion is unqualified (clean)
   - Scope covers relevant Trust Service Criteria

**Trust Service Criteria (SOC 2):**

- **Security** (required for all SOC 2)
- **Availability** (uptime, performance)
- **Confidentiality** (data protection)
- **Processing Integrity** (data accuracy)
- **Privacy** (personal data handling)

**Step 3: Assess Incident Investigation Support**

**Key Questions:**

| Question | Good Answer | Red Flag |
|----------|-------------|----------|
| Can vendor provide logs for forensics? | Yes, within 24 hours | No, or >1 week delay |
| Do logs include user actions? | Yes, comprehensive audit trail | Basic system logs only |
| Can vendor freeze environment for investigation? | Yes, with legal process | No capability |
| Does vendor cooperate with law enforcement? | Yes, with customer notification | Yes, without notification |
| Are logs retained long enough? | 12+ months | <90 days |

**Step 4: Complete Extended Columns**

| Column | Field | How to Assess | Evidence |
|--------|-------|---------------|----------|
| R | Audit Rights in Contract | Yes/Limited/No | Contract audit clause |
| S | Audit Frequency Allowed | Annual/On-Cause/None | Contract |
| T | SOC 2 Type II Available | Yes/Type I Only/No | SOC 2 report |
| U | SOC 2 Report Date | Most recent report period end | SOC 2 cover page |
| V | On-Site Audit Feasible | Yes/Virtual Only/No | Vendor facilities policy |
| W | Incident Investigation Support | Strong/Adequate/Weak/None | Vendor security policy, DPA |
| X | Log Retention Period | Days/months | Vendor documentation |

**Step 5: Set Status Flag**

| Scenario | Status | Gap Description |
|----------|--------|-----------------|
| Audit rights + SOC 2 Type II + Good investigation support | ✅ | - |
| SOC 2 Type II only (no audit rights) | ⚠️ | "No direct audit rights (SOC 2 in lieu)" |
| Audit rights but no SOC 2 available | ⚠️ | "Must exercise audit rights (no SOC 2 alternative)" |
| No audit rights + No SOC 2 | ❌ | "No audit visibility into vendor controls" |
| Poor incident investigation support | ⚠️ | "Limited forensics capability" |

### Common Mistakes

❌ **Not requesting SOC 2** - "It's a big vendor, they must be secure" (verify!)  
❌ **Accepting SOC 2 Type I** - Type I is point-in-time, not 12-month operational effectiveness  
❌ **Not reading audit restrictions** - Clause allows audit but only of physical DC, not cloud environment  
❌ **Assuming logs are available** - Many SaaS providers don't retain detailed logs long-term  
❌ **Not testing incident response** - Contract says "support", but never tested in practice  

### Example Entry

| A | B | C | D | E | H | I | R | S | T | U | V | W | X |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zoom | Zoom Video Communications | SaaS | High | Confidential | ✅ | /evidence/zoom/soc2.pdf | Yes | Annual | Yes | 31.12.2024 | Virtual Only | Adequate | 12 months |

---

## Sheet 7: Jurisdictional Risk Assessment

### Purpose

Assess legal and jurisdictional risks, particularly US CLOUD Act exposure for vendors subject to US jurisdiction. Evaluate Transfer Impact Assessment (TIA) results and risk mitigation measures.

**Success Criterion:** All Restricted/Confidential data transfers to US-jurisdiction vendors have completed TIA with documented risk acceptance or mitigation.

### What to Document

For each vendor:

- Vendor headquarters and legal jurisdiction
- Parent company ownership (especially US ownership)
- US CLOUD Act exposure assessment
- Transfer Impact Assessment (TIA) results (if applicable)
- Risk mitigation measures (encryption, data residency controls)
- Residual risk acceptance

### How to Complete

**Step 1: Determine Vendor Jurisdiction**

**Key Factors:**

| Factor | Why It Matters | How to Verify |
|--------|----------------|---------------|
| **HQ Location** | Primary legal jurisdiction | Vendor website (About Us, Legal Notices) |
| **Parent Company** | Ultimate owner's jurisdiction | Corporate structure, investor relations |
| **Data Center Location** | Where data is physically stored | Admin console, DPA |
| **Subsidiary Structure** | EU subsidiary vs. US parent | Company registry (EU Transparency Register) |

**Examples:**

| Vendor | HQ | Parent | Data Storage | US CLOUD Act Exposure |
|--------|-------|--------|--------------|----------------------|
| Microsoft Ireland | Ireland (EU) | Microsoft Corp. (USA) | EU | YES (US parent) |
| AWS Europe | Luxembourg (EU) | Amazon Inc. (USA) | EU | YES (US parent) |
| OVHcloud | France (EU) | OVHcloud (FR) | EU | NO (EU-only) |
| Proton Mail | Switzerland | Proton AG (CH) | Switzerland | NO (CH-only) |

**Step 2: Assess US CLOUD Act Exposure**

**US CLOUD Act (18 USC §2713) Applies To:**

- Any company incorporated in USA
- Any company with substantial US presence
- Foreign subsidiaries of US companies (Microsoft Ireland, AWS Europe, Google Ireland)

**Risk:**

- US government can demand data from US companies
- Includes data stored outside USA (extraterritorial reach)
- Conflicts with GDPR prohibition on transfers without legal basis
- Vendor must comply with US law (even if violates GDPR)

**Step 3: Conduct Transfer Impact Assessment (TIA)**

**When Required:**

- Transfer to USA or US-owned company
- Using SCCs as transfer mechanism
- Processing personal data (GDPR/FADP scope)

**TIA Process (see EDPB Recommendations 01/2020):**

1. **Map Transfer:** Identify all transfer points (primary, backup, support, subprocessors)
2. **Assess Laws:** Evaluate US surveillance laws (FISA 702, EO 12333, CLOUD Act)
3. **Evaluate Safeguards:** Do SCCs + technical measures overcome legal risks?
4. **Document:** DPO/Legal assessment with risk conclusion

**TIA Outcomes:**

| Outcome | Description | Next Steps |
|---------|-------------|------------|
| **Low Risk** | US access unlikely (non-critical data, encryption + BYOK) | Proceed with transfer |
| **Medium Risk** | Some risk but mitigated (SCCs + encryption) | Accept risk with controls |
| **High Risk** | Likely US access, inadequate safeguards | Reject transfer OR add controls |

**Step 4: Identify Risk Mitigation Measures**

**Effective Mitigations:**

| Mitigation | Description | Effectiveness |
|------------|-------------|---------------|
| **EU Data Residency** | Enable EU-only data boundary (Microsoft EU Boundary, AWS EU Regions) | HIGH (but check support access) |
| **Customer-Managed Keys** | BYOK/HYOK - vendor cannot decrypt without your key | HIGH (if properly implemented) |
| **End-to-End Encryption** | Client-side encryption before upload | VERY HIGH |
| **Contractual Protections** | Vendor agrees to challenge US requests, notify customer | LOW (cannot override US law) |

**Ineffective Mitigations:**

- ❌ "We'll anonymize data" (re-identification risk)
- ❌ "Vendor promises not to give US data" (cannot override CLOUD Act)
- ❌ "Data is encrypted" (if vendor holds keys, US can compel disclosure)

**Step 5: Complete Extended Columns**

| Column | Field | How to Assess | Evidence |
|--------|-------|---------------|----------|
| R | Vendor HQ Jurisdiction | From vendor website, company registry | Website screenshot, Dun & Bradstreet |
| S | Parent Company | Ultimate owner | Corporate structure chart |
| T | US CLOUD Act Exposure | Yes/No/Unclear | Legal assessment |
| U | TIA Completed | Yes/No/N/A (no US transfer) | DPO assessment document |
| V | TIA Risk Level | Low/Medium/High/N/A | TIA conclusion |
| W | EU Data Residency Enabled | Yes/No/N/A | Admin console screenshot |
| X | Customer-Managed Keys | Yes/No/N/A | Key management config |
| Y | Residual Risk Accepted By | CISO, Legal, DPO (name + date) | Risk acceptance form |
| Z | Risk Exception ID | Link to risk register | Risk register entry |
| AA | Mitigation Review Date | Next TIA review date (annual) | Calendar entry |

**Step 6: Set Status Flag**

| Scenario | Status | Gap Description |
|----------|--------|-----------------|
| No US exposure (EU-only vendor) | ✅ | - |
| US exposure + TIA Low Risk + Mitigations | ✅ | "US CLOUD Act risk mitigated" |
| US exposure + TIA Medium Risk + Accepted | ⚠️ | "Residual US CLOUD Act risk accepted by [Role]" |
| US exposure + TIA High Risk | ❌ | "High US jurisdiction risk - recommend EU alternative" |
| US exposure + No TIA | ❌ | "TIA required but not completed" |

### Common Mistakes

❌ **Assuming EU subsidiary = safe** - Microsoft Ireland is still subject to US CLOUD Act  
❌ **Ignoring parent company** - Vendor HQ in EU but owned by US parent  
❌ **Skipping TIA** - "We have SCCs, we're compliant" (post-Schrems II requires TIA)  
❌ **Weak mitigations** - Relying on vendor promises instead of technical controls  
❌ **Not reviewing annually** - TIA is not one-time; legal landscape changes  
❌ **Confusing encryption types** - Vendor-managed keys ≠ customer-managed keys  

### Example Entry

| A | B | C | D | E | H | I | R | S | T | U | V | W | X | Y | Z | AA |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GitHub | GitHub Inc. | SaaS | High | Confidential | ⚠️ | /evidence/github/tia.pdf | USA | Microsoft Corp. (USA) | Yes | Yes | Medium | No | No | Dr. Maria Weber, DPO (15.01.2026) | RISK-2026-015 | 15.01.2027 |

**Gap:** "US CLOUD Act exposure; Medium risk accepted with mitigations (code encryption, no personal data in repos)"

---

## Evidence Collection Guide

### Evidence Principles

**Core Requirement:** Every ✅ (Compliant) status MUST link to verifiable evidence.

**Evidence Quality Standards:**

- **Authentic:** From official source (not screenshots of screenshots)
- **Current:** Within validity period, not expired
- **Complete:** Shows all required information
- **Attributable:** Clear which vendor/service it applies to
- **Accessible:** Reviewable by auditors (proper permissions)

### Evidence Repository Structure

**Folder Organization:**
```
/ISMS/Evidence/A.5.23.2/
    ├── Amazon_Web_Services/
    │   ├── AWS_ISO27001_Certificate_2024.pdf
    │   ├── AWS_SOC2_TypeII_2024.pdf
    │   ├── AWS_MSA_Signed_2024.pdf
    │   └── AWS_SLA_Performance_Q4_2025.xlsx
    ├── Microsoft_Corporation/
    │   ├── MSFT_ISO27001_Certificate_2025.pdf
    │   ├── MSFT_DPA_SCCs_2024.pdf
    │   └── MSFT_TIA_Assessment_2025.pdf
    └── [Vendor_Name]/
        └── [Evidence_Files]
```

**Naming Convention:** `[Vendor]_[DocType]_[Date/Year].[ext]`

### Evidence Types by Sheet

| Sheet | Evidence Type | Example Filename | How to Obtain |
|-------|---------------|------------------|---------------|
| **Sheet 2** | ISO 27001 Certificate | `Vendor_ISO27001_Cert_2025.pdf` | Vendor trust center, request from vendor |
| **Sheet 2** | SOC 2 Type II Report | `Vendor_SOC2_TypeII_2024.pdf` | Request under NDA from vendor compliance |
| **Sheet 3** | Contract (MSA) | `Vendor_MSA_Signed_2024.pdf` | Contract management system, legal files |
| **Sheet 3** | DPA with SCCs | `Vendor_DPA_SCCs_2024.pdf` | Contract annex or standalone agreement |
| **Sheet 4** | SLA Performance Report | `Vendor_SLA_Report_Q4_2025.xlsx` | Monitoring tool export, vendor portal |
| **Sheet 5** | Data Residency Config | `Vendor_DataResidency_Screenshot_20260120.png` | Admin console screenshot |
| **Sheet 6** | SOC 2 Report Access | `Vendor_SOC2_TypeII_2024.pdf` | Same as Sheet 2 (link to same file) |
| **Sheet 7** | TIA Document | `Vendor_TIA_Assessment_2025.pdf` | DPO/Legal assessment memo |
| **All** | Email Correspondence | `Vendor_Email_CertRequest_20260115.pdf` | Print email to PDF |

### Screenshot Guidelines

**When to Screenshot:**

- Admin console settings (data residency, encryption, MFA status)
- Vendor status pages (historical uptime data)
- Vendor trust center (publicly available certifications)
- Support portal (SLA credit requests)

**Required Elements in Screenshot:**

- Full URL visible (top of browser)
- Timestamp/date visible (bottom right corner overlay OR system clock)
- Service name visible
- Relevant setting/configuration clearly shown
- Your organization's account context visible (if applicable)

**Tools:**

- Windows: Snipping Tool (Win+Shift+S), Snagit
- Mac: Screenshot (Cmd+Shift+4), CleanShot
- Browser: Full-page screenshot extensions

### Document Collection Checklist

**For Each Vendor, Gather:**

```
☐ Sheet 2 - Security Certifications
    ☐ ISO 27001 certificate (PDF)
    ☐ SOC 2 Type II report (PDF, under NDA)
    ☐ Penetration test summary (PDF, may be redacted)
    ☐ Incident breach notifications (email, PDF)

☐ Sheet 3 - Contracts
    ☐ Master Services Agreement (PDF, signed)
    ☐ Data Processing Agreement (PDF, signed)
    ☐ Order forms / Statements of Work (PDF)
    ☐ SLA schedule (if separate from MSA)

☐ Sheet 4 - SLA Performance
    ☐ Monitoring dashboard export (PDF, Excel)
    ☐ Vendor status page history (screenshot, PDF)
    ☐ SLA credit requests (email, support tickets)
    ☐ Incident records (ITSM export)

☐ Sheet 5 - Data Sovereignty
    ☐ Admin console region settings (screenshot)
    ☐ DPA data location schedule (PDF)
    ☐ Encryption settings (screenshot)
    ☐ Subprocessor list (vendor website, PDF)

☐ Sheet 6 - Audit Rights
    ☐ Contract audit clause (highlight in MSA PDF)
    ☐ SOC 2 Type II report (same as Sheet 2)
    ☐ Vendor audit policy (PDF from vendor)

☐ Sheet 7 - Jurisdictional Risk
    ☐ TIA document (DPO/Legal assessment)
    ☐ Vendor corporate structure (Dun & Bradstreet, website)
    ☐ Risk acceptance form (if applicable)
    ☐ EU data boundary settings (screenshot)
```

### Evidence Quality Validation

**Before Marking ✅, Verify:**

| Evidence Type | Validation Check | Red Flag |
|---------------|------------------|----------|
| **ISO 27001** | Certificate number valid, accreditation body recognized, service in scope | Generic "management system" cert not covering cloud service |
| **SOC 2** | Type II (not Type I), <18 months old, unqualified opinion | Type I, qualified opinion, or ancient report |
| **Contracts** | Signed by authorized parties, dates valid, all annexes present | Unsigned draft, missing DPA, expired |
| **SLA Data** | From YOUR monitoring (not vendor self-report), timestamp visible | "Vendor told us 99.9%" with no proof |
| **Screenshots** | URL visible, timestamp clear, relevant setting shown | Cropped image, no context, unclear source |

### Evidence Register (Sheet 9) Workflow

**As You Complete Sheets 2-7:**

1. Collect evidence file
2. Save to repository: `/ISMS/Evidence/A.5.23.2/[Vendor]/[File]`
3. Add entry to Sheet 9:

   - Evidence ID (auto-increment: EV-001, EV-002...)
   - Vendor Name
   - Evidence Type
   - File Location (full path or hyperlink)
   - Collection Date
   - Expiry Date (for certs)

4. Reference Evidence ID in Sheet 2-7 Column I

**Benefit:** Centralized evidence tracking, easy audit trail, no duplicate files.

---

## Common Pitfalls & How to Avoid Them

### Top 10 Critical Mistakes

**1. Trusting Vendor Marketing Without Verification**

- ❌ Problem: "Vendor website says ISO 27001 certified" → assumed compliant
- ✅ Solution: Request actual certificate, verify with certification body database

**2. Accepting Expired Certifications**

- ❌ Problem: ISO 27001 was valid at contract signing 3 years ago, now expired
- ✅ Solution: Check expiry dates, set calendar reminders for renewal verification

**3. Not Checking Certification Scope**

- ❌ Problem: Vendor has ISO 27001 for "IT infrastructure" but cloud service not in scope
- ✅ Solution: Read certificate scope statement carefully, request clarification if unclear

**4. SOC 2 Type I vs Type II Confusion**

- ❌ Problem: Accepted SOC 2 Type I (point-in-time) for Critical service
- ✅ Solution: Require Type II (12-month operational effectiveness) for Critical/High services

**5. Missing or Inadequate DPA**

- ❌ Problem: Contract has generic "data protection" clause but no formal DPA
- ✅ Solution: Request standalone DPA with Standard Contractual Clauses (EU transfers)

**6. Assuming EU Vendor = EU Data**

- ❌ Problem: Vendor HQ in Germany but uses AWS us-east-1 for data storage
- ✅ Solution: Verify actual data location in admin console, don't trust vendor location

**7. Not Completing Transfer Impact Assessment (TIA)**

- ❌ Problem: Using SCCs for US transfer without TIA (post-Schrems II requirement)
- ✅ Solution: Engage DPO/Legal to conduct TIA for all US-jurisdiction vendors

**8. Relying on Vendor SLA Self-Reporting**

- ❌ Problem: "Vendor says 99.99% uptime" but no independent monitoring
- ✅ Solution: Implement YOUR monitoring (Pingdom, Datadog, etc.), track objectively

**9. Not Claiming SLA Credits**

- ❌ Problem: Vendor breaches SLA, credits owed but not claimed ("too much paperwork")
- ✅ Solution: Claim ALL credits (principle of accountability + budget recovery)

**10. Shadow IT / Undocumented Services**

- ❌ Problem: Business unit adopted Notion without IT approval, no assessment
- ✅ Solution: Regular discovery scans (CASB, egress monitoring), add to inventory → assess

### Sheet-Specific Gotchas

**Sheet 2 (Certifications):**

- ⚠️ Certificate is for parent company, not the specific cloud service entity
- ⚠️ Penetration test report is 3 years old (should be annual)
- ⚠️ SOC 2 report doesn't include "Confidentiality" criteria (only "Security")

**Sheet 3 (Contracts):**

- ⚠️ DPA allows subprocessors without notification requirement
- ⚠️ Liability cap is €100K but service handles €10M in revenue (inadequate)
- ⚠️ Exit clause requires 12-month notice (unacceptably long)
- ⚠️ Auto-renewal with 90-day notice (easy to miss renewal deadline)

**Sheet 4 (SLA):**

- ⚠️ SLA commitment is "reasonable efforts" not specific percentage
- ⚠️ SLA excludes "third-party issues" (but vendor uses third-party CDN)
- ⚠️ Credits are capped at 1 month service fee (even for 100% downtime)

**Sheet 5 (Data Sovereignty):**

- ⚠️ Backup replication to US region not disclosed in DPA
- ⚠️ Support staff in US/India can access EU data
- ⚠️ SCCs present but Transfer Impact Assessment not conducted
- ⚠️ Encryption enabled but vendor manages keys (CLOUD Act risk)

**Sheet 6 (Audit Rights):**

- ⚠️ Audit clause allows audit "at vendor's discretion" (not a right)
- ⚠️ SOC 2 available but only via vendor portal (expires annually, must re-request)
- ⚠️ On-site audit prohibited, only virtual/questionnaire allowed

**Sheet 7 (Jurisdictional Risk):**

- ⚠️ Vendor is EU subsidiary but parent company is US (CLOUD Act applies)
- ⚠️ TIA not updated after US-EU Data Privacy Framework adoption
- ⚠️ Risk acceptance expired (was accepted for 1 year, now past date)

### Data Quality Issues

**Incomplete Data:**

- Problem: Missing values in base columns (Criticality, Data Classification)
- Fix: Cross-reference IMP-5.23.1 inventory, populate ALL base columns

**Inconsistent Data:**

- Problem: Service marked "Critical" in IMP-5.23.1 but "Medium" in IMP-5.23.2
- Fix: Base columns should be READ-ONLY from IMP-5.23.1 (copy, don't edit)

**Stale Data:**

- Problem: Assessment completed Q1 2025, now Q4 2025, certifications expired
- Fix: Quarterly reviews, calendar reminders for cert expiry dates

---

## Quality Checklist

### Pre-Submission Checklist

**Before Submitting for Approval, Verify:**

```
☐ COMPLETENESS
    ☐ All vendors from IMP-5.23.1 inventory assessed (cross-check)
    ☐ All data collection sheets (2-7) completed
    ☐ All base columns (A-Q) populated (no blanks unless N/A)
    ☐ All extended columns (R+) completed for each sheet
    ☐ All status flags set (✅/⚠️/❌/N/A)

☐ EVIDENCE QUALITY
    ☐ Every ✅ status links to evidence (Sheet 9)
    ☐ All evidence files exist and accessible
    ☐ All evidence is current (not expired)
    ☐ Screenshots show URL + timestamp
    ☐ Contracts are signed (not drafts)
    ☐ Certifications verified (not just vendor claims)

☐ GAP ANALYSIS
    ☐ Every ⚠️/❌ has Gap Description (Column J)
    ☐ Every gap has Remediation Needed (Yes/No in Column K)
    ☐ If remediation needed, Target Date populated (Column P)
    ☐ If gap accepted, Exception ID populated (Column L)
    ☐ All exceptions documented in risk register

☐ CONSISTENCY
    ☐ Base columns match IMP-5.23.1 (A-E)
    ☐ Vendor names consistent across sheets
    ☐ Contract dates consistent (Sheet 3 vs Sheet 4)
    ☐ Data residency consistent (Sheet 5 vs Sheet 7)

☐ REGULATORY COMPLIANCE
    ☐ All Restricted/Confidential data: DPA present (Sheet 3)
    ☐ All EU data transfers: SCCs or Adequacy (Sheet 5)
    ☐ All US transfers: TIA completed (Sheet 7)
    ☐ All Critical services: ISO 27001 or SOC 2 (Sheet 2)
    ☐ DORA in-scope services: All requirements met

☐ DASHBOARD VALIDATION
    ☐ Sheet 8 formulas calculate correctly
    ☐ Overall compliance % reasonable (cross-check manually)
    ☐ Risk distribution makes sense (not all green or all red)
    ☐ Top gaps list matches actual data in Sheets 2-7

☐ EVIDENCE REGISTER
    ☐ All evidence files linked in Sheet 9
    ☐ All hyperlinks work (click each one)
    ☐ File naming follows convention
    ☐ Folder permissions correct (auditors can access)

☐ APPROVAL READINESS
    ☐ Sheet 10 blank and ready for approvers
    ☐ All prerequisite approvals obtained (if any)
    ☐ Assessment summary prepared for CISO
    ☐ Remediation plan ready (if gaps exist)
```

### Sheet-Specific Quality Checks

**Sheet 2 (Security Certifications):**

- ☐ ISO 27001 certificate numbers verified against accreditation body
- ☐ SOC 2 Type II (not Type I) for all Critical/High services
- ☐ Certification expiry dates ≥3 months in future
- ☐ Service explicitly listed in certification scope

**Sheet 3 (Contract Terms):**

- ☐ All Confidential/Restricted services have DPA
- ☐ Liability caps appropriate for service criticality
- ☐ Exit clauses present with data portability
- ☐ Subprocessor notification requirements documented

**Sheet 4 (SLA Performance):**

- ☐ SLA data from YOUR monitoring (not vendor claims)
- ☐ Breach counts reconcile with incident records
- ☐ All SLA credits claimed (none outstanding)
- ☐ SLA commitments match contract (Sheet 3)

**Sheet 5 (Data Sovereignty):**

- ☐ Data locations verified in admin console
- ☐ Cross-border transfers identified correctly
- ☐ SCCs/BCRs present for all non-adequate country transfers
- ☐ Encryption status verified (not assumed)

**Sheet 6 (Audit Rights):**

- ☐ Audit rights exist in contract (not discretionary)
- ☐ SOC 2 reports current (<18 months old)
- ☐ Incident investigation support verified (not assumed)

**Sheet 7 (Jurisdictional Risk):**

- ☐ US CLOUD Act exposure correctly identified
- ☐ TIA completed for all US transfers
- ☐ Risk acceptance signed by appropriate authority
- ☐ Mitigation measures actually implemented (not just planned)

### Approval Workflow Quality Gate

**Legal Review:**

- ☐ All contract terms reviewed and approved
- ☐ DPAs adequate for data protection compliance
- ☐ Liability and indemnification terms acceptable
- ☐ Exit clauses protect organization interests

**Security Review:**

- ☐ All certifications verified authentic
- ☐ Security gaps documented and acceptable
- ☐ Compensating controls adequate (if gaps exist)
- ☐ Vendor security posture matches criticality

**Compliance Review:**

- ☐ GDPR/FADP compliance verified (DPA, SCCs, TIA)
- ☐ DORA/NIS2 requirements met (if applicable)
- ☐ All residual risks formally accepted
- ☐ Evidence audit-ready

**CISO Approval:**

- ☐ Overall risk profile acceptable
- ☐ Critical gaps remediated or accepted
- ☐ Assessment methodology followed
- ☐ Ready for external audit

---

## Review & Approval Process

### Approval Workflow

**Standard Approval Chain:**

```
Step 1: ISMS Coordinator Review (Quality Check)
          ↓
Step 2: Legal Review (Contract Terms, DPA, Liability)
          ↓
Step 3: Security Review (Certifications, Technical Controls)
          ↓
Step 4: Compliance Review (GDPR, DORA, NIS2, Regulatory)
          ↓
Step 5: CISO Approval (Final Risk Acceptance)
          ↓
Step 6: Archive & Publish (Evidence repository, ISMS folder)
```

**Timeline:** 5-10 business days from submission to final approval

### Approval Roles & Responsibilities

| Role | Responsibility | Focus Areas | Timeline |
|------|---------------|-------------|----------|
| **ISMS Coordinator** | Quality check completeness | All sheets complete, evidence linked, no blanks | 1-2 days |
| **Legal** | Contract review | DPA adequacy, liability terms, exit clauses | 2-3 days |
| **Security / CISO** | Security posture review | Certifications, risk gaps, compensating controls | 2-3 days |
| **DPO / Compliance** | Regulatory review | GDPR/FADP compliance, TIA, jurisdictional risk | 2-3 days |
| **CISO** | Final approval | Overall risk acceptance, budget for remediation | 1-2 days |

### Approval Criteria

**ISMS Coordinator (Quality Gate 1):**

- ✅ All vendors assessed (cross-check with IMP-5.23.1)
- ✅ All evidence files linked and accessible
- ✅ All status flags justified (✅ has evidence, ❌ has gap description)
- ✅ Dashboard formulas calculate correctly
- ❌ Reject if: Missing evidence, incomplete sheets, broken links

**Legal (Quality Gate 2):**

- ✅ All Confidential/Restricted services have DPA
- ✅ Liability terms adequate for service criticality
- ✅ Exit clauses protect organization
- ✅ Subprocessor controls documented
- ❌ Reject if: No DPA for personal data, inadequate liability, missing critical clauses

**Security / CISO (Quality Gate 3):**

- ✅ All Critical services: ISO 27001 or SOC 2 Type II
- ✅ Security gaps acceptable or remediation planned
- ✅ Compensating controls adequate (if gaps exist)
- ✅ Vendor security posture matches risk tolerance
- ❌ Reject if: Critical service without certification, unacceptable risk gap, no remediation plan

**Compliance / DPO (Quality Gate 4):**

- ✅ All EU personal data: DPA with SCCs or Adequacy
- ✅ All US transfers: TIA completed with risk assessment
- ✅ DORA/NIS2 requirements met (if applicable)
- ✅ All residual risks documented and justified
- ❌ Reject if: GDPR violation, missing TIA, regulatory non-compliance

**CISO (Final Approval):**

- ✅ Overall risk profile acceptable
- ✅ Budget approved for remediation actions
- ✅ Critical gaps remediated or formally accepted
- ✅ Assessment ready for external audit

### Approval Documentation (Sheet 10)

**Required Sign-Offs:**

| Approver | Approval Date | Decision | Comments | Evidence |
|----------|---------------|----------|----------|----------|
| ISMS Coordinator | [Date] | Approved / Rejected | Quality issues, if any | Checklist completed |
| Legal | [Date] | Approved / Conditionally Approved / Rejected | Contract concerns | Legal review memo |
| Security / CISO | [Date] | Approved / Conditionally Approved / Rejected | Security gaps | Gap analysis |
| DPO / Compliance | [Date] | Approved / Conditionally Approved / Rejected | Regulatory issues | Compliance checklist |
| CISO | [Date] | Approved / Approved with Conditions / Rejected | Final decision | Risk acceptance form |

**Conditional Approval Example:**
"Approved with condition: Complete TIA for AWS by 28.02.2026. If TIA identifies high risk, re-submit for review."

### Remediation Planning (If Gaps Identified)

**For Each Gap (⚠️ or ❌):**

1. **Prioritize:** Critical > High > Medium > Low (based on service criticality + risk)
2. **Assign Owner:** Who will remediate? (Legal, Security, Vendor Manager)
3. **Set Target Date:** Realistic timeline (30/60/90 days)
4. **Define Success Criteria:** What does "fixed" look like?
5. **Track Progress:** Monthly review in governance meetings

**Remediation Plan Template:**

| Gap ID | Vendor | Issue | Owner | Target Date | Status | Notes |
|--------|--------|-------|-------|-------------|--------|-------|
| GAP-001 | Zoom | No SOC 2 Type II | Security | 28.02.2026 | In Progress | Requested from vendor |
| GAP-002 | Notion | Missing DPA | Legal | 15.03.2026 | Blocked | Vendor slow to respond |

### Escalation Process

**When to Escalate:**

- Vendor refuses to provide required documentation (ISO cert, SOC 2, DPA)
- Critical gaps cannot be remediated (e.g., vendor won't sign DPA)
- Budget needed for remediation exceeds approval authority
- Risk acceptance required above CISO level (Board approval)

**Escalation Path:**
1. ISMS Coordinator → CISO (initial escalation)
2. CISO → Risk Committee (if risk acceptance needed)
3. Risk Committee → Board (if strategic decision or high financial impact)

---

## Integration & Maintenance

### Integration with Other ISMS Documents

**Upstream Dependencies:**

| Document | Relationship | Integration Point |
|----------|--------------|-------------------|
| **IMP-5.23.1 (Inventory)** | Provides vendor list | Base columns A-E copied from inventory |
| **ISMS-POL-A.5.19-23** | Policy requirements | Assessment criteria derived from policy |
| **Risk Register** | Risk tracking | Exception IDs (Column L), Risk IDs (Column M) |
| **Contract Management System** | Contract repository | Evidence files sourced from contracts |

**Downstream Consumers:**

| Document | What It Needs | How It Gets It |
|----------|---------------|----------------|
| **IMP-5.23.3 (Secure Config)** | Vendor certifications, data residency | Sheet 2, Sheet 5 data |
| **IMP-5.23.4 (Governance)** | SLA performance, contract renewal dates | Sheet 4, Sheet 3 data |
| **IMP-5.23.5 (Dashboard)** | Compliance metrics | Sheet 8 summary dashboard |
| **Risk Register** | Identified vendor risks | Sheet 8 top gaps, exception tracking |
| **Audit Reports** | Evidence of compliance | Sheet 9 evidence register |

### Quarterly Review Process

**Every Quarter (Within 30 Days of Quarter-End):**

**Week 1: Data Collection**

- Pull updated SLA performance data (Sheet 4)
- Check for certification renewals (Sheet 2)
- Verify contracts still current (Sheet 3)
- Review any new subprocessors (Sheet 3)

**Week 2: Assessment Updates**

- Update changed data in Sheets 2-7
- Re-verify evidence files still accessible
- Update status flags if changes
- Document new gaps or closed gaps

**Week 3: Review & Approval**

- ISMS Coordinator quality check
- Stakeholder review (if significant changes)
- CISO approval (if new risks identified)

**Week 4: Reporting**

- Update IMP-5.23.5 dashboard
- Report to risk committee (if material changes)
- Archive previous quarter version

**Triggers for Out-of-Cycle Review:**

- New vendor onboarding (IMP-5.23.1 inventory updated)
- Contract renewal or major amendment
- Vendor security incident or breach
- Regulatory change (new DORA standards, etc.)
- Certification expiry or suspension
- Vendor acquisition / change of ownership

### Annual Comprehensive Review

**Once per Year (Aligned with ISO 27001 Audit):**

**Extended Scope:**

- Request updated SOC 2 reports (annual cycle)
- Re-verify ALL certifications (even if not expired)
- Full contract review (identify renewal opportunities)
- Re-conduct TIA for all US transfers (legal landscape changes)
- Review risk acceptances (re-approve or remediate)
- Update evidence repository (purge old files)

**Deliverables:**

- Updated IMP-5.23.2 workbook (new version)
- Risk committee annual report
- Remediation plan for year ahead
- Vendor performance scorecards

### Data Retention

**Workbook Versions:**

- Retain: Last 3 years of quarterly assessments
- Archive: Older versions to long-term storage
- Reason: Audit trail, trend analysis, contract disputes

**Evidence Files:**

- Retain: Current + 1 expired version (e.g., 2024 + 2023 ISO cert)
- Archive: After 3 years post-expiry
- Reason: Audit evidence, legal defense

**Approval Records:**

- Retain: Indefinitely (part of ISMS audit trail)
- Archive: After 7 years (legal retention)

### System Integration Points

**Automated Data Flows (If Available):**

| Source System | Data | Target Sheet | Frequency |
|---------------|------|--------------|-----------|
| **ITSM (ServiceNow)** | Incident tickets, SLA breaches | Sheet 4 | Monthly export |
| **Monitoring (Datadog)** | Uptime %, performance metrics | Sheet 4 | Monthly export |
| **Contract Mgmt** | Contract renewal dates | Sheet 3 | Quarterly sync |
| **Procurement** | Vendor spend, PO data | Base columns | Quarterly sync |
| **CMDB** | Service-vendor mapping | Base columns | Weekly sync |

**Manual Workflows:**

- Vendor certification requests (email + NDA)
- SOC 2 report collection (vendor portal)
- TIA completion (DPO/Legal assessment)
- Risk exception approvals (risk committee meetings)

---

## Appendix

### Glossary (IMP-Specific Terms)

| Term | Definition |
|------|------------|
| **Base Columns (A-Q)** | Standard columns shared across all data collection sheets (2-7) |
| **DPA** | Data Processing Agreement - GDPR-required contract for processor relationships |
| **Extended Columns (R+)** | Sheet-specific columns beyond the standard base columns |
| **SCCs** | Standard Contractual Clauses - EU-approved contract templates for data transfers |
| **SOC 2 Type II** | Service Organization Control audit report covering 12 months of operational effectiveness |
| **TIA** | Transfer Impact Assessment - Required for transfers to non-adequate countries (post-Schrems II) |
| **US CLOUD Act** | Clarifying Lawful Overseas Use of Data Act - US law requiring US companies to provide data to US government, even if stored abroad |

### Regulatory References

**For detailed regulatory requirements, see:**

- **ISMS-POL-00:** Regulatory Applicability Framework (master regulatory mapping)
- **ISMS-POL-A.5.19-23:** Supplier and Cloud Services Security Policy (policy requirements)

**Key Regulations:**

- **GDPR** (EU Regulation 2016/679): General Data Protection Regulation
- **FADP** (Swiss Federal Data Protection Act): Swiss data protection law
- **DORA** (EU Regulation 2022/2554): Digital Operational Resilience Act (financial sector)
- **NIS2** (EU Directive 2022/2555): Network and Information Security Directive
- **US CLOUD Act** (18 USC §2713): US extraterritorial data access law

### Certification Verification Resources

**ISO 27001 Certificate Verification:**

- **IAF CertSearch:** https://www.iafcertsearch.org/ (international accreditation database)
- **UKAS Directory:** https://www.ukas.com/find-an-organisation/ (UK accreditation)
- **DAkkS:** https://www.dakks.de/ (German accreditation)
- **ANAB:** https://anab.ansi.org/accreditation/ (US accreditation)

**SOC 2 Auditor Verification:**

- **AICPA Firm Search:** https://us.aicpa.org/forthepublic/findacpa (verify auditor licensed)
- Big 4: Deloitte, PwC, EY, KPMG
- Reputable Regional: Moss Adams, BDO, RSM, Grant Thornton

**Vendor Trust Centers:**

- **AWS:** https://aws.amazon.com/compliance/programs/
- **Azure:** https://servicetrust.microsoft.com/
- **Google Cloud:** https://cloud.google.com/security/compliance
- **Salesforce:** https://trust.salesforce.com/

### Assessment Completion Checklist (Quick Reference)

```
☐ Prerequisites Complete
    ☐ IMP-5.23.1 inventory complete and approved
    ☐ Evidence repository created
    ☐ Stakeholders assigned to sheets
    ☐ Kickoff meeting held

☐ Data Collection (Weeks 1-4)
    ☐ Sheet 2: Security Certifications (request from vendors)
    ☐ Sheet 3: Contract Terms (gather from Legal)
    ☐ Sheet 4: SLA Performance (export from monitoring)
    ☐ Sheet 5: Data Sovereignty (verify in admin consoles)
    ☐ Sheet 6: Audit Rights (review contracts, request SOC 2)
    ☐ Sheet 7: Jurisdictional Risk (conduct TIA if needed)

☐ Evidence Collection (Ongoing)
    ☐ All evidence files collected
    ☐ Files saved to repository
    ☐ Sheet 9 (Evidence Register) populated
    ☐ All hyperlinks tested

☐ Quality Assurance (Week 5)
    ☐ Quality checklist completed
    ☐ All status flags justified
    ☐ Dashboard formulas validated
    ☐ Cross-sheet consistency verified

☐ Review & Approval (Week 6)
    ☐ ISMS Coordinator quality check
    ☐ Legal review and approval
    ☐ Security review and approval
    ☐ Compliance review and approval
    ☐ CISO final approval

☐ Post-Approval
    ☐ Archive approved version
    ☐ Update IMP-5.23.5 dashboard
    ☐ Remediation plan created (if gaps)
    ☐ Next quarterly review scheduled
```

### Vendor Communication Templates

**Template 1: Certification Request**
```
Subject: Security Certification Request - [Your Organization]

Dear [Vendor Contact],

As part of our vendor risk management program (ISO 27001:2022 Control A.5.23), 
we require the following security documentation for [Service Name]:

1. Current ISO 27001 certificate (with scope statement)
2. Most recent SOC 2 Type II audit report (we will sign NDA if required)
3. Summary of latest penetration testing results
4. List of authorized subprocessors

Please provide these documents by [Date + 10 business days].

If you have a vendor trust center or security portal, please provide access 
credentials.

Thank you for your cooperation.

Best regards,
[Name], [Title]
[Organization]
```

**Template 2: SLA Credit Request**
```
Subject: SLA Credit Request - Service Outage [Date]

Dear [Vendor Support],

Our records show that [Service Name] experienced downtime on [Date] from 
[Start Time] to [End Time] ([Duration] minutes).

Per our Service Level Agreement (Section X.Y), this outage exceeds the 
allowed monthly downtime and qualifies for SLA credits.

Calculation:

- Monthly commitment: 99.9% uptime (43.2 minutes allowed downtime)
- Actual downtime this month: [X] minutes
- Excess downtime: [X - 43.2] minutes
- Credit amount: €[Amount] per contract formula

Please process this SLA credit and confirm receipt.

Incident reference: [Ticket #]
Monitoring evidence: [Attached]

Thank you,
[Name], [Title]
```

### Document History

**Major Changes in v2.1 (Refactor):**

- Reduced from 13,357 → 4,500 lines (66% reduction)
- Section 4: Table-based sheet guidance (replaced paragraph explanations)
- Section 5: Streamlined evidence guide (removed screenshot tutorials)
- Section 6: Top 10 pitfalls only (removed exhaustive lists)
- Section 10: IMP-specific content only (removed regulatory duplication)
- All regulatory references now point to POL-00 (eliminated duplication)

**Alignment with IMP-5.23.1 Quality Standard:**

- Consistent structure across all A.5.23 assessments
- Table-heavy presentation for scannability
- ONE example per sheet (not multiple good/bad comparisons)
- Concise, actionable guidance (not encyclopedia)

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
