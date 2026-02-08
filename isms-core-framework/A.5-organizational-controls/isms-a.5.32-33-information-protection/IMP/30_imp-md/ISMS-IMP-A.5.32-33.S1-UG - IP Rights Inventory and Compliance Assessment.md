**ISMS-IMP-A.5.32-33.S1-UG - IP Rights Inventory and Compliance Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.32: Intellectual Property Rights

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.32-33.S1-UG |
| **Version** | 1.0 |
| **Assessment Area** | Intellectual Property Identification, Classification, Protection, and Compliance |
| **Related Policy** | ISMS-POL-A.5.32-33, Section 2.1 (IP Identification and Classification) |
| **Purpose** | Guide users through systematic IP discovery, classification, protection assessment, and third-party IP compliance verification |
| **Target Audience** | Legal Counsel, CISO, IP Owners, System Owners, IT Teams, Compliance Officers, Auditors, Workbook Developers |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Annual or After Significant IP Changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for IP Rights Inventory assessment workbook | ISMS Implementation Team |

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.32-33.S1-TG.

---

**Audience:** Legal Counsel, CISO, IP Owners, System Owners, IT Teams, Compliance Officers

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.32-33.S1 - IP Rights Inventory and Compliance Assessment

### ISO/IEC 27001:2022 Control Reference

**Control A.5.32 - Intellectual Property Rights:**

> *The organisation should implement appropriate procedures to protect intellectual property rights.*

This control ensures that organisations identify, protect, and manage intellectual property assets while also complying with third-party IP rights.

### What This Assessment Covers

This assessment documents the **WHAT** and **HOW** of IP protection - the foundational inventory that answers:

- What intellectual property does [Organisation] own or use?
- How is IP classified and categorised (trade secrets, patents, copyrights, trademarks)?
- What protection mechanisms are in place for each IP category?
- How does [Organisation] ensure compliance with third-party IP rights?
- What software licensing obligations exist and are they being met?
- What legal protections are registered (patents, trademarks)?

### Key Principle

This assessment is **organisation-specific and technology-independent**. You document YOUR specific intellectual property assets (whatever they are - proprietary software, trade secrets, methodologies, designs) and verify compliance against both internal protection requirements and external IP obligations.

### What You'll Document

- **Complete IP Asset Inventory** listing all organisational intellectual property
- **IP Classification** for each asset (trade secret, patent, copyright, trademark)
- **Protection Assessment** documenting controls per IP category
- **Ownership Documentation** with designated owners and custodians
- **Third-Party IP Register** for licensed software and content
- **Software License Compliance** verification and reconciliation
- **Legal Protection Status** (registered patents, trademarks)
- **Gap Analysis** identifying unprotected or non-compliant IP
- **Evidence Register** linking documentation to audit artefacts
- **Approved Assessment** with Legal Counsel and CISO sign-offs

### How This Relates to Other A.5.32-33 Assessments

| Assessment | Focus | Relationship to A.5.32-33.1 |
|------------|-------|--------------------------|
| **ISMS-IMP-A.5.32-33.S1** | **IP Rights Inventory** | **Foundation - WHAT IP exists** |
| ISMS-IMP-A.5.32-33.S2 | Records Protection | Requires IP classification for records containing IP |
| ISMS-IMP-A.5.32-33.S3 | Retention & Disposal | Requires IP inventory for retention requirements |
| ISMS-IMP-A.5.32-33.S4 | Compliance Dashboard | Aggregates metrics from all assessments |

**Context Note:** This assessment (A.5.32-33.1) should be completed first - it provides the foundational IP inventory that informs records protection and retention decisions.

## Who Should Complete This Assessment

### Primary Stakeholders

1. **Legal Counsel** - Leads assessment, validates legal protection status, ensures regulatory compliance
2. **Chief Information Security Officer (CISO)** - Provides technical IP protection assessment, validates security controls
3. **IP Owners / Business Unit Leaders** - Document IP assets they own, define protection requirements
4. **IT Operations** - Document software assets, provide licensing information
5. **Compliance Officer** - Validate third-party IP compliance, review license agreements

### Required Skills

- Understanding of intellectual property law (patents, copyrights, trademarks, trade secrets)
- Knowledge of [Organisation]'s proprietary assets and innovations
- Familiarity with software licensing models (commercial, open source, SaaS)
- Ability to interview business units and technical teams
- Technical understanding to assess protection mechanisms

### Time Commitment

- **Initial assessment:** 15-30 hours (depending on organisation size and IP portfolio)
  - Small organisation (limited IP, 1-50 employees): 8-15 hours
  - Medium organisation (moderate IP portfolio, 50-250 employees): 15-30 hours
  - Large organisation (extensive IP portfolio, 250+ employees): 30-60+ hours
- **Annual updates:** 4-8 hours (verify changes, update for new IP assets)

## Expected Outputs

Upon completion, you will have:

1. **Complete IP Asset Inventory** - All organisational IP with classifications
2. **IP Protection Assessment** - Controls documented per IP category
3. **Ownership Register** - Designated owners and custodians for all IP
4. **Third-Party IP Register** - Licensed software and content with compliance status
5. **Software License Reconciliation** - Usage vs entitlements verified
6. **Legal Protection Status** - Patents, trademarks, copyrights documented
7. **Gap Analysis** - Identified protection gaps with remediation plans
8. **Evidence Register** - Supporting documentation linked to audit artefacts
9. **Compliance Dashboard** - Executive summary with metrics
10. **Approved Assessment** - Legal Counsel and CISO sign-offs

---

# Prerequisites

## Information You'll Need

Before starting this assessment, gather:

### IP Asset Documentation

- Business unit innovation registers
- Research and development documentation
- Proprietary methodology descriptions
- Source code repositories list
- Design documentation and specifications
- Technical architecture documents
- Trade secret inventories (if existing)

### Legal Documentation

- Patent applications and grants
- Trademark registrations
- Copyright registrations
- IP assignment agreements (employee inventions)
- Non-disclosure agreements (NDA templates)
- Licensing agreements (inbound and outbound)
- Partnership/joint venture IP clauses

### Software Asset Information

- Software asset inventory (SAM tool exports)
- License entitlements and purchases
- SaaS subscription records
- Open source software usage
- Custom software development records
- Third-party component libraries

### Employment and Contractor Information

- Employment contract IP clauses
- Contractor agreement IP provisions
- Exit interview IP acknowledgments
- Confidentiality agreement templates

## Access Required

You will need access to:

**Systems:**

- [ ] Legal document management system
- [ ] Software asset management (SAM) tools
- [ ] Source code repositories (for inventory)
- [ ] Patent/trademark databases
- [ ] Contract management system

**Documents:**

- [ ] Employment contract templates (IP clauses)
- [ ] Vendor agreements with IP provisions
- [ ] Partnership agreements
- [ ] NDA templates and signed agreements
- [ ] Previous IP inventories (if existing)

**People:**

- [ ] Ability to interview business unit leaders
- [ ] Access to R&D and product development teams
- [ ] Coordination with Legal for regulatory interpretation
- [ ] Support from IT for software inventory

## Tools and Resources

**Assessment Workbook:** Excel workbook (generated by `generate_a532_33_1_ip_rights_inventory.py`) containing:

- Sheet 1: Instructions & Legend
- Sheet 2: IP Asset Inventory
- Sheet 3: IP Protection Assessment
- Sheet 4: Third-Party IP Register
- Sheet 5: Software License Compliance
- Sheet 6: Gap Analysis
- Sheet 7: Evidence Register
- Sheet 8: Approval & Sign-Off

**Supporting Tools** (optional but highly recommended):

- **Software Asset Management (SAM)** - Automated license tracking (e.g., Flexera, Snow Software, ServiceNow SAM)
- **Patent databases** - USPTO, EPO, WIPO, Swiss IGE
- **Trademark databases** - National and international registries
- **Contract management** - For license agreement tracking

**Reference Materials:**

- ISMS-POL-A.5.32-33 Section 2.1 (IP Classification Framework)
- Swiss Federal Act on Patents for Inventions (PatG)
- Swiss Federal Act on Copyright (URG)
- Berne Convention for the Protection of Literary and Artistic Works
- WIPO Copyright Treaty

---

# Assessment Workflow

## High-Level Process

```
1. PREPARE (Gather prerequisites, set up assessment team)
   |
2. DISCOVER IP ASSETS (Business unit interviews + technical inventory)
   |
3. CLASSIFY IP (Trade secrets, patents, copyrights, trademarks)
   |
4. ASSESS PROTECTION (Technical and administrative controls)
   |
5. VERIFY THIRD-PARTY COMPLIANCE (Software licenses, content rights)
   |
6. IDENTIFY GAPS (Unprotected IP, non-compliant usage)
   |
7. COLLECT EVIDENCE (Link to supporting documentation)
   |
8. REVIEW & APPROVE (Legal Counsel and CISO sign-off)
```

## Detailed Workflow

### Phase 1: Preparation (1-2 hours)

**Objective:** Set up assessment foundation

**Steps:**
1. Read this entire User Guide (PART I)
2. Gather all prerequisites (Section 2.1 above)
3. Review ISMS-POL-A.5.32-33 Section 2.1 for IP classification framework
4. Identify all IP owners and schedule interviews
5. Request SAM tool exports and license documentation
6. Create working folder for evidence collection

**Deliverable:** Assessment plan with IP owner interview schedule

### Phase 2: IP Asset Discovery (5-12 hours)

**Objective:** Identify ALL intellectual property assets

**Steps:**
1. **Business Unit Interviews:**

   - Interview R&D leadership for innovations and inventions
   - Interview product teams for proprietary methodologies
   - Interview marketing for brand assets and content
   - Interview IT for custom software and technical documentation

2. **Technical Discovery:**

   - Review source code repository inventory
   - Identify custom-developed software and tools
   - Document proprietary algorithms and processes
   - List technical documentation with trade secret content

3. **Legal Records Review:**

   - Pull patent application and grant records
   - Review trademark registration portfolio
   - Identify registered copyrights
   - Review IP assignment agreements

4. **Inventory Creation (Sheet 2):**

   - List EVERY IP asset with unique identifier
   - Document IP category (trade secret, patent, copyright, trademark)
   - Assign IP owner and custodian
   - Note protection status (registered, pending, unregistered)
   - Estimate business value (high, medium, low)

**Deliverable:** Complete Sheet 2 (IP Asset Inventory) with all assets listed

**Quality Check:**

- All business units interviewed for IP assets
- Technical documentation reviewed for trade secrets
- Legal records reconciled with inventory
- Source code and custom software captured
- Brand assets (logos, trademarks) documented

### Phase 3: IP Classification (2-4 hours)

**Objective:** Classify IP assets by type and protection requirements

**Steps:**
1. Review IP classification framework (ISMS-POL-A.5.32-33 Section 2.1):

   - **Trade Secrets:** Confidential business information providing competitive advantage
   - **Patents:** Inventions with formal legal protection (granted or pending)
   - **Copyrights:** Original works of authorship (software, documentation, content)
   - **Trademarks:** Brand identifiers (logos, names, slogans)

2. For EACH asset in Sheet 2, determine:

   - Primary IP category (trade secret, patent, copyright, trademark)
   - Legal protection status (registered, pending, unregistered, not applicable)
   - Information classification alignment (per ISMS-POL-A.5.12-13)
   - Required protection level based on business value

3. Apply classification decision tree:
```
Is this a registered patent or pending application?
  YES -> Classification: PATENT
  NO -> Continue...

Is this a registered trademark or service mark?
  YES -> Classification: TRADEMARK
  NO -> Continue...

Is this an original work (software, documentation, creative content)?
  YES -> Classification: COPYRIGHT
  NO -> Continue...

Is this confidential business information providing competitive advantage?
  YES -> Classification: TRADE SECRET
  NO -> May not qualify as IP (verify with Legal)
```

**Deliverable:** Sheet 2 complete with IP Classification column populated

**Common Mistakes to Avoid:**

- Forgetting that source code has both copyright and trade secret aspects
- Not recognising trade secrets in business processes and methodologies
- Assuming registered protection automatically means adequate protection
- Missing IP in contractor-developed works (ownership may be unclear)

### Phase 4: Protection Assessment (4-8 hours)

**Objective:** Document protection mechanisms for each IP category

**Steps:**
1. **For Trade Secrets:**

   - Access controls (need-to-know restriction)
   - Confidentiality agreements (NDAs with employees, contractors, partners)
   - Physical security (secure areas, locked storage)
   - Technical controls (encryption, DLP, access logging)
   - Documentation of reasonable protection measures (for legal defence)

2. **For Patents:**

   - Application/grant status and dates
   - Geographic coverage (countries where protected)
   - Maintenance fee payment status
   - Expiration tracking
   - Infringement monitoring

3. **For Copyrights:**

   - Copyright notices on protected works
   - Registration status (if applicable)
   - License terms for distribution
   - Open source component tracking

4. **For Trademarks:**

   - Registration status and classes
   - Geographic coverage
   - Renewal tracking
   - Brand usage guidelines
   - Monitoring for infringement

5. **Complete Sheet 3 (IP Protection Assessment):**

   - One row per IP asset
   - Document applicable controls per category
   - Rate control effectiveness (effective, partial, ineffective)
   - Identify protection gaps

**Deliverable:** Sheet 3 complete with protection assessment for all IP assets

### Phase 5: Third-Party IP Compliance (4-8 hours)

**Objective:** Verify compliance with third-party intellectual property rights

**Steps:**
1. **Software License Compliance:**

   - Export SAM tool inventory (deployed vs entitled)
   - Review commercial software licenses
   - Verify SaaS subscription compliance
   - Check open source license obligations

2. **For EACH Third-Party Software (Sheet 4):**

   - Software name and vendor
   - License type (perpetual, subscription, open source)
   - License count (entitled vs deployed)
   - Compliance status (compliant, over-deployed, under-utilised)
   - Renewal dates

3. **Open Source Compliance:**

   - Identify open source components in use
   - Document license types (GPL, Apache, MIT, BSD, etc.)
   - Verify license obligation compliance
   - Check for copyleft restrictions affecting proprietary code

4. **Third-Party Content:**

   - Stock photos, fonts, icons
   - Licensed data sets
   - Third-party APIs and services
   - Contracted creative work

5. **Complete Sheet 4 (Third-Party IP Register):**

   - All third-party IP assets listed
   - License compliance status documented
   - Risk rating for non-compliance
   - Remediation actions where needed

**Deliverable:** Sheets 4 and 5 complete with third-party IP documented

### Phase 6: Gap Analysis (2-4 hours)

**Objective:** Identify protection gaps and compliance issues

**Steps:**
1. Review IP Asset Inventory (Sheet 2) for:

   - Unregistered IP that should be registered
   - Missing ownership assignments
   - Inadequate protection controls
   - Expiring legal protections

2. Review Third-Party IP (Sheet 4) for:

   - Over-deployed software licenses
   - Open source license violations
   - Expired or expiring licenses
   - Missing license documentation

3. **Complete Sheet 6 (Gap Analysis):**

   - Gap description and category
   - Risk rating (high, medium, low)
   - Recommended remediation
   - Owner and due date
   - Status tracking

**Deliverable:** Sheet 6 complete with all gaps documented

### Phase 7: Evidence Collection (1-2 hours)

**Objective:** Document evidence supporting assessment findings

**Steps:**
1. Gather evidence for each IP asset:

   - Patent/trademark certificates
   - License agreements
   - NDA templates and samples
   - Access control configurations
   - SAM tool reports

2. **Complete Sheet 7 (Evidence Register):**

   - Evidence ID and description
   - Related IP asset or control
   - Storage location
   - Collection date
   - Verification status

**Deliverable:** Sheet 7 complete with evidence documented

### Phase 8: Review & Approval (1-2 hours)

**Objective:** Obtain formal sign-off on assessment

**Steps:**
1. Review assessment with Legal Counsel

   - Validate IP classifications
   - Confirm legal protection status
   - Review third-party compliance findings

2. Review assessment with CISO

   - Validate technical protection controls
   - Confirm information classification alignment
   - Review gap analysis and remediation plans

3. **Complete Sheet 8 (Approval & Sign-Off):**

   - Assessment summary
   - Approver signatures and dates
   - Conditions or limitations
   - Next review date

**Deliverable:** Approved assessment with sign-offs

---

# Sheet-by-Sheet Completion Guidance

## Sheet 1: Instructions & Legend

**Purpose:** Reference guide for completing the workbook

**User Actions:**
- Read classification definitions
- Understand colour coding and status indicators
- Reference control framework alignment

## Sheet 2: IP Asset Inventory

**Purpose:** Comprehensive register of all organisational IP

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| IP Asset ID | Unique identifier | IP-001 |
| IP Asset Name | Descriptive name | Customer Analytics Algorithm |
| IP Category | Trade Secret/Patent/Copyright/Trademark | Trade Secret |
| Description | Detailed description | Proprietary algorithm for customer churn prediction |
| IP Owner | Designated owner | Chief Data Officer |
| Custodian | Day-to-day responsible | Analytics Team Lead |
| Legal Protection Status | Registered/Pending/Unregistered | Unregistered |
| Business Value | High/Medium/Low | High |
| Classification | Per ISMS-POL-A.5.12-13 | Confidential |
| Creation Date | When IP was created | 2024-03-15 |
| Last Review | Last protection review | 2025-12-01 |

**Completion Tips:**
- Be comprehensive - include all IP regardless of formal registration
- Assign clear ownership for each asset
- Align classification with information security framework
- Document even "minor" IP - aggregated value may be significant

## Sheet 3: IP Protection Assessment

**Purpose:** Document protection controls for each IP asset

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| IP Asset ID | Reference to Sheet 2 | IP-001 |
| Access Control | How access is restricted | Role-based, need-to-know |
| Technical Controls | Encryption, DLP, etc. | AES-256 encryption, DLP monitoring |
| Administrative Controls | NDAs, policies, etc. | NDA required, confidentiality policy |
| Physical Controls | Secure storage, etc. | Restricted area access |
| Legal Protection | Registration, contracts | NDA clause in employment contracts |
| Control Effectiveness | Effective/Partial/Ineffective | Effective |
| Gap Description | Any protection gaps | No periodic access review |
| Remediation Needed | Required actions | Implement quarterly access review |

**Completion Tips:**
- Document all control layers (technical, administrative, physical, legal)
- Be honest about control effectiveness
- Identify gaps even if remediation is not immediately planned
- Link to evidence where controls are documented

## Sheet 4: Third-Party IP Register

**Purpose:** Track all third-party IP used by organisation

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Third-Party IP ID | Unique identifier | TP-001 |
| Software/Content Name | Name of product | Microsoft 365 |
| Vendor | Provider name | Microsoft |
| License Type | Perpetual/Subscription/Open Source | Subscription |
| License Quantity | Number entitled | 500 seats |
| Deployed Quantity | Number in use | 487 seats |
| Compliance Status | Compliant/Over-deployed/Under-utilised | Compliant |
| Contract Reference | Agreement number | MSA-2024-001 |
| Renewal Date | When license expires | 2026-06-30 |
| Open Source License | If applicable (GPL, MIT, etc.) | N/A |

**Completion Tips:**
- Include all software, not just major applications
- Track SaaS subscriptions as well as on-premises software
- Document open source components in development projects
- Flag over-deployment for immediate remediation

## Sheet 5: Software License Compliance

**Purpose:** Detailed license reconciliation

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Software Name | Application name | Adobe Creative Cloud |
| License Model | Named user/Device/Enterprise | Named User |
| Entitled | Licenses purchased | 50 |
| Deployed | Licenses in use | 52 |
| Variance | Over/Under | +2 |
| Compliance Risk | High/Medium/Low | High |
| Remediation Action | Required action | Purchase 2 additional licenses |
| Due Date | Action deadline | 2026-02-28 |
| Status | Open/In Progress/Complete | Open |

## Sheet 6: Gap Analysis

**Purpose:** Identify and track protection/compliance gaps

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Gap ID | Unique identifier | GAP-001 |
| Gap Category | Protection/Compliance/Documentation | Compliance |
| Description | Detailed gap description | 2 Adobe licenses over-deployed |
| Related IP | IP asset or third-party reference | TP-005 |
| Risk Rating | High/Medium/Low | High |
| Remediation Action | Required action | Purchase additional licenses |
| Owner | Responsible person | IT Procurement Manager |
| Due Date | Target completion | 2026-02-28 |
| Status | Open/In Progress/Complete | Open |

## Sheet 7: Evidence Register

**Purpose:** Link assessment to supporting documentation

**Required Fields:**
| Column | Description | Example |
|--------|-------------|---------|
| Evidence ID | Unique identifier | EV-001 |
| Description | What evidence shows | Software license agreement |
| Evidence Type | Document/Screenshot/Report | Document |
| Related Item | IP asset or control reference | TP-001 |
| Storage Location | Where evidence is stored | SharePoint/Legal/Contracts |
| Collected Date | When gathered | 2026-02-01 |
| Collected By | Who gathered | Legal Counsel |
| Verification Status | Verified/Pending/Expired | Verified |

## Sheet 8: Approval & Sign-Off

**Purpose:** Formal assessment approval record

**Required Fields:**
- Assessment Period
- Overall Compliance Status
- Summary of Findings
- Approver Signatures (Legal Counsel, CISO)
- Conditions or Limitations
- Next Review Date

---

# Evidence Collection

## Required Evidence

For each IP asset category, collect:

**Trade Secrets:**
- Confidentiality policy documentation
- NDA templates and signed examples
- Access control configurations
- DLP policy evidence
- Training records for IP handling

**Patents:**
- Patent certificates or application confirmations
- Maintenance fee payment records
- Geographic coverage documentation

**Copyrights:**
- Copyright notices on protected works
- Registration certificates (if applicable)
- Source code header samples

**Trademarks:**
- Registration certificates
- Renewal records
- Brand usage guidelines

**Third-Party IP:**
- License agreements
- SAM tool compliance reports
- Open source license documentation
- Vendor contracts

## Evidence Storage

Store all evidence in:
- **Primary Location:** ISMS Evidence Library (SharePoint/Confluence or equivalent)
- **Folder Structure:** `/ISMS/A.5.32-33/IP-Rights-Inventory/[Assessment-Date]/`
- **Naming Convention:** `EV-[ID]_[Description]_[Date].ext`

---

# Common Pitfalls

Avoid these common mistakes when completing the assessment:

**MISTAKE: Only documenting formally registered IP**
- Include trade secrets, proprietary processes, and unregistered copyrights
- Much valuable IP is protected without formal registration

**MISTAKE: Assuming all employee-created IP is owned by organisation**
- Review employment contracts for IP assignment clauses
- Contractor agreements may have different IP ownership terms

**MISTAKE: Ignoring open source license obligations**
- GPL and other copyleft licenses have distribution requirements
- Track open source components in all development projects

**MISTAKE: Not reconciling SAM data with actual deployments**
- Automated SAM tools may miss manual installations
- Cloud and SaaS usage may not be fully captured

**MISTAKE: Treating the assessment as one-time**
- IP portfolios change frequently
- Schedule regular reviews (at least annual)

**MISTAKE: Not involving Legal Counsel early**
- IP classification has legal implications
- Legal should validate protection status determinations

**MISTAKE: Forgetting about acquired IP**
- Merger and acquisition activities bring new IP
- Ensure acquired IP is properly integrated into inventory

**MISTAKE: Overlooking third-party content in marketing**
- Stock photos, fonts, music require proper licensing
- User-generated content has IP implications

**MISTAKE: Not documenting protection measures for trade secrets**
- Trade secret status requires "reasonable measures"
- Documentation is essential for legal defence

**MISTAKE: Missing IP in departing employee handovers**
- Exit procedures should include IP acknowledgment
- Knowledge transfer should capture undocumented IP

---

# Quality Checklist

Before submitting for approval, verify:

**IP Asset Inventory (Sheet 2):**
- [ ] All business units interviewed for IP assets
- [ ] All IP categories represented (trade secrets, patents, copyrights, trademarks)
- [ ] Each asset has designated owner and custodian
- [ ] Classification aligns with information security framework
- [ ] Business value assigned to prioritise protection

**IP Protection Assessment (Sheet 3):**
- [ ] All IP assets from Sheet 2 have protection assessment
- [ ] Control effectiveness honestly evaluated
- [ ] Gaps clearly identified
- [ ] Remediation actions assigned

**Third-Party IP Register (Sheet 4):**
- [ ] All commercial software documented
- [ ] SaaS subscriptions included
- [ ] Open source components tracked
- [ ] Third-party content (photos, fonts) documented

**Software License Compliance (Sheet 5):**
- [ ] SAM data reconciled with actual deployments
- [ ] Variances identified and explained
- [ ] Remediation actions for over-deployment

**Gap Analysis (Sheet 6):**
- [ ] All gaps from Sheets 3, 4, 5 consolidated
- [ ] Risk ratings assigned
- [ ] Remediation owners identified
- [ ] Due dates are realistic

**Evidence Register (Sheet 7):**
- [ ] Evidence collected for key findings
- [ ] Storage locations documented
- [ ] Evidence verification status current

**Approval (Sheet 8):**
- [ ] Legal Counsel review completed
- [ ] CISO review completed
- [ ] Any conditions documented
- [ ] Next review date scheduled

---

# Review & Approval

## Review Process

1. **Self-Review:** Complete quality checklist above
2. **Peer Review:** Another team member validates completeness
3. **Legal Counsel Review:** Validates IP classifications and legal protection status
4. **CISO Review:** Validates technical protection controls
5. **Final Approval:** Legal Counsel and CISO sign-off

## Approval Criteria

Assessment approved when:
- All IP assets documented with classifications
- Protection controls assessed for effectiveness
- Third-party IP compliance verified
- Gaps identified with remediation plans
- Evidence collected and verified

## Escalation Path

- Minor gaps (documentation): Remediate within 30 days
- Medium gaps (control weakness): Escalate to CISO for risk acceptance or remediation
- Major gaps (compliance violation): Immediate escalation to Legal Counsel and Executive Management

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
