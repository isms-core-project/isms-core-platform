**ISMS-IMP-A.5.34.4-UG - Technical and Organizational Measures (TOMs) Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.34.4-UG |
| **Version** | 1.0 |
| **Assessment Area** | Technical and Organizational Measures (TOMs) Assessment per GDPR Article 32 |
| **Related Policy** | ISMS-POL-A.5.34, Section 2.4 (Technical and Organizational Measures) |
| **Purpose** | Guide users through systematic evaluation of 20 GDPR Article 32 security measures, calculate compliance scoring, and identify gaps in pseudonymization, encryption, availability, and resilience controls |
| **Target Audience** | DPO/Privacy Officers, CISO, IT Security Teams, System Administrators, Cloud Architects, Compliance Officers, Auditors |
| **Assessment Type** | Technical Security Assessment |
| **Review Cycle** | Quarterly or after security architecture changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for TOMs assessment workbook | ISMS Implementation Team |

---

### Document Structure

This document consists of three parts:

- **PART 1: DOCUMENT CONTROL + USER COMPLETION GUIDE** (This file)
  - Document Control & Version History
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Sheet-by-Sheet Completion Guidance
  - Evidence Collection
  - Common Pitfalls (10 mistakes)
  - Quality Checklist (80+ items)
  - Review & Approval

- **PART 2: TECHNICAL SPECIFICATION (Sheets 1-4)** (Second file)
  - Workbook Structure & File Naming
  - Cell Styling Reference (comprehensive)
  - Sheet 1: Instructions & Legend (complete spec)
  - Sheet 2: TOM Control Inventory (20 TOMs, exact columns A-N)
  - Sheet 3: Technical Measures Deep-Dive (T1-T10 detailed layout)
  - Sheet 4: Organizational Measures Deep-Dive (O1-O10 detailed layout)

- **PART 3: TECHNICAL SPECIFICATION (Sheets 5-8 + Python)** (Third file)
  - Sheet 5: Evidence Repository (exact columns A-I, auto-numbering)
  - Sheet 6: Gap Analysis & Risk Assessment (exact columns A-J, risk formulas)
  - Sheet 7: Remediation Action Plan (exact columns A-J, SLA tracking)
  - Sheet 8: Compliance Dashboard (exact metrics, formulas, charts)
  - Python Script Architecture (complete implementation pattern)
  - Integration with A.5.34.7 Dashboard
  - Testing & Validation

**Target Audiences:**

- **Part 1:** Assessment users (CISO, DPO, Security Team, Compliance Officers)
- **Parts 2-3:** Workbook developers (Python/Excel script maintainers)

---

**Audience:** CISO, DPO, Security Architects, Compliance Officers

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates **Technical and Organizational Measures (TOMs)** protecting PII processing to ensure compliance with:

- **GDPR Article 32** - Security of Processing
- **Swiss FADP Article 8** - Data Security  
- **ISO/IEC 27001:2022 Control A.5.34** - Privacy and Protection of PII

**The 20 TOM Categories:**

**Technical Measures (T1-T10):**
1. **T1 - Encryption:** Data encryption in transit and at rest
2. **T2 - Access Control:** Role-based access control (RBAC), least privilege
3. **T3 - Pseudonymization/Anonymization:** Data minimization techniques
4. **T4 - Data Minimization:** Collection limitation, purpose limitation
5. **T5 - Security Monitoring & Logging:** SIEM, audit trails, anomaly detection
6. **T6 - Network Security:** Firewalls, segmentation, intrusion detection
7. **T7 - Application Security:** Secure coding, input validation, WAF
8. **T8 - Endpoint Security:** EDR, anti-malware, device management
9. **T9 - Backup & Recovery:** Business continuity, disaster recovery
10. **T10 - Physical Security:** Data center security, device disposal

**Organizational Measures (O1-O10):**
1. **O1 - Policies & Procedures:** Written security policies, procedures
2. **O2 - Staff Training & Awareness:** Privacy training, phishing awareness
3. **O3 - Incident Response & Breach Notification:** IR plan, 72-hour notification
4. **O4 - Vendor Management:** Third-party risk management, DPAs
5. **O5 - Data Protection by Design/Default:** Privacy-first architecture
6. **O6 - Accountability & Governance:** DPO appointment, data ownership
7. **O7 - Risk Management:** Privacy risk assessments, DPIAs
8. **O8 - Compliance Monitoring & Audit:** Internal audits, control testing
9. **O9 - Documentation & Records:** ROPA, consent logs, DSR logs
10. **O10 - Business Continuity:** BC/DR plans, resilience

**Assessment Output:** 8-sheet Excel workbook documenting:

- Implementation status of all 20 TOMs
- Detailed technical/organizational descriptions
- Evidence of implementation
- Gap analysis with risk ratings
- Remediation action plans
- Executive compliance dashboard

## Why This Matters

**ISO 27001:2022 Control A.5.34 Requirement:**
> *"Rules for the privacy and protection of PII should be established and implemented in accordance with applicable laws and regulations."*

**GDPR Article 32 Requirement:**
> *"Taking into account the state of the art, the costs of implementation and the nature, scope, context and purposes of processing as well as the risk of varying likelihood and severity for the rights and freedoms of natural persons, the controller and the processor shall implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk."*

**Swiss FADP Article 8 Requirement:**
> *"The controller and the processor must ensure the security of personal data through appropriate technical and organisational measures."*

**Why Auditors Care:**

- TOMs are the **foundation** of privacy compliance - without them, you're just documenting paper policies
- Auditors will test control effectiveness, not just existence
- GDPR fines can reach €20M or 4% of global annual turnover for Article 32 violations
- Swiss FADP fines up to CHF 250,000 for inadequate security measures
- ISO 27001 certification requires demonstrable control implementation

**Business Impact:**

- Data breaches cost organizations an average of $4.45M (IBM 2023)
- 60% of SMBs go out of business within 6 months of a major breach
- Customer trust and brand reputation are irreplaceable
- Regulatory investigations are costly and time-consuming

## What You'll Document

Upon completion, you will have:

1. ✅ **TOM Implementation Status** - Complete inventory of all 20 TOMs with implementation ratings (Implemented/Partially Implemented/Planned/Not Implemented)
2. ✅ **Technical Measure Details** - Deep-dive documentation of T1-T10: technologies deployed, configurations, coverage percentages, exceptions
3. ✅ **Organizational Measure Details** - Deep-dive documentation of O1-O10: policies, training programs, governance structures, monitoring methods
4. ✅ **Evidence Repository** - Centralized documentation of all evidence proving TOM effectiveness (policies, configs, audit reports, test results)
5. ✅ **Gap Analysis** - Identification of all TOM gaps with risk ratings (Critical/High/Medium/Low) using likelihood × impact matrix
6. ✅ **Remediation Roadmap** - Prioritized action plans for closing gaps with owners, timelines, budgets, and progress tracking
7. ✅ **Compliance Dashboard** - Executive metrics showing implementation rate, effectiveness rate, gap distribution, and GDPR Art. 32 compliance score
8. ✅ **Audit-Ready Documentation** - Complete assessment workbook suitable for ISO 27001, GDPR, FADP audits and supervisory authority inspections

## How This Relates to Other A.5.34 Assessments

| Assessment | Focus | Relationship to A.5.34.4 |
|------------|-------|--------------------------|
| **ISMS-IMP-A.5.34.1** | **PII Identification & Classification** | **Prerequisites:** A.5.34.1 identifies WHAT PII you process. A.5.34.4 documents HOW you protect it. |
| ISMS-IMP-A.5.34.2 | Legal Basis & Lawful Processing | Provides legal context for processing - A.5.34.4 ensures technical/organizational controls match legal obligations |
| ISMS-IMP-A.5.34.3 | Data Subject Rights Management | A.5.34.4's TOMs enable DSR fulfillment (e.g., T3 pseudonymization enables right to object, O3 incident response enables breach notification) |
| ISMS-IMP-A.5.34.5 | Data Protection Impact Assessment (DPIA) | DPIA identifies risks - A.5.34.4 documents mitigating controls |
| ISMS-IMP-A.5.34.6 | Cross-Border Transfer Assessment | International transfers require TOMs adequacy - A.5.34.4 proves your controls meet GDPR Chapter V requirements |
| ISMS-IMP-A.5.34.7 | Privacy Compliance Dashboard | A.5.34.4 feeds TOM metrics into consolidated dashboard |

**Critical Dependency:** Complete A.5.34.1 (PII Identification) BEFORE starting A.5.34.4. You cannot assess protection measures without knowing what PII you're protecting.

---

# Prerequisites

## Information You'll Need

Before starting this assessment, gather:

### PII Inventory & Classification (from A.5.34.1)

- List of all PII categories processed
- Data classification (Restricted/Confidential/Internal/Public)
- PII locations (systems, databases, file shares)
- Data flow maps

### Security Architecture Documentation

- Network architecture diagrams
- System architecture diagrams
- Data flow diagrams
- Integration maps

### Technical Security Controls Documentation

- Encryption configurations (TLS, at-rest encryption)
- Access control configurations (AD groups, IAM roles, RBAC)
- Security monitoring configurations (SIEM rules, alerts)
- Network security configurations (firewall rules, segmentation)
- Application security controls (WAF, input validation)
- Endpoint security deployments (EDR, anti-malware)
- Backup & DR configurations
- Physical security controls

### Organizational Security Documentation

- Information security policies (ISMS policy suite)
- Privacy-specific policies (privacy policy, data retention policy)
- Procedures and work instructions
- Training materials and completion records
- Incident response plan
- Vendor management documentation (DPAs, vendor assessments)
- Risk assessment documentation
- Audit reports (internal/external)
- ROPA (Record of Processing Activities)
- Business continuity plan

### Evidence & Proof of Implementation

- Configuration screenshots
- Audit logs showing control operation
- Test results (penetration tests, vulnerability scans)
- Training completion reports
- Incident response exercise reports
- Vendor due diligence reports
- ISO 27001 audit reports
- Supervisory authority correspondence (if any)

## Access Required

You will need access to:

**Technical Systems:**

- Security information and event management (SIEM) system
- Identity and access management (IAM) console
- Cloud platform management consoles (AWS, Azure, GCP)
- Endpoint management console (Intune, JAMF, etc.)
- Network security management (firewall, IDS/IPS consoles)
- Backup management console
- Vulnerability management system
- Data loss prevention (DLP) console (if deployed)

**Administrative Systems:**

- Policy management system / SharePoint
- Training management system (LMS)
- Incident management system (ServiceNow, Jira Service Management)
- Vendor management system
- Risk management system
- Audit management system
- HR system (for training records)
- Physical access control system (if applicable)

**Documentation Repositories:**

- Security documentation library
- Privacy documentation library
- Audit evidence repository
- Policy repository
- Procedure repository

## Who Should Complete This Assessment

### Primary Stakeholders

1. **Chief Information Security Officer (CISO)** - Overall responsibility, strategic decisions, gap prioritization, executive reporting
2. **Data Protection Officer (DPO)** - Regulatory interpretation, GDPR/FADP compliance verification, risk assessment
3. **Security Architect** - Technical measure documentation (T1-T10), architecture decisions, control effectiveness assessment
4. **IT Operations Manager** - Operational measure documentation, implementation details, evidence collection
5. **Compliance Officer** - Organizational measure documentation (O1-O10), policy verification, audit readiness
6. **Internal Auditor** - Independent verification, evidence validation, gap identification

### Required Skills

- **Privacy Regulation Knowledge:** Understanding of GDPR Articles 5, 25, 32-36; Swiss FADP Articles 6-8
- **Security Controls Expertise:** Familiarity with NIST CSF, ISO 27001 Annex A, CIS Controls
- **Risk Assessment:** Ability to assess likelihood and impact of security risks
- **Technical Security:** Understanding of encryption, access control, network security, application security
- **Compliance Auditing:** Experience with control testing and evidence evaluation
- **Documentation Skills:** Ability to write clear, audit-ready documentation

### Time Commitment

- **Initial assessment:** 40-60 hours total across all stakeholders
  - CISO/DPO: 8-12 hours (strategic decisions, review)
  - Security Architect: 16-24 hours (technical measures T1-T10)
  - IT Ops Manager: 12-16 hours (implementation details, evidence)
  - Compliance Officer: 12-16 hours (organizational measures O1-O10)
  - Internal Auditor: 8-12 hours (verification, gap analysis)

- **Annual updates:** 16-24 hours (review changes, update evidence, remediation progress)
- **Quarterly reviews:** 4-8 hours (spot checks, dashboard updates, remediation tracking)

## Expected Outputs

Upon completion, you will have:

1. ✅ **8-Sheet Excel Workbook** - Complete TOM assessment with all fields populated
2. ✅ **Implementation Status Matrix** - 20 TOMs rated (Implemented/Partially/Planned/Not Implemented)
3. ✅ **Technical Measure Documentation** - Detailed descriptions of T1-T10 with coverage percentages
4. ✅ **Organizational Measure Documentation** - Detailed descriptions of O1-O10 with governance structures
5. ✅ **Evidence Repository** - 100+ evidence entries documenting control effectiveness
6. ✅ **Gap Analysis Report** - All identified gaps with risk ratings
7. ✅ **Remediation Roadmap** - Prioritized action plans with owners, timelines, budgets
8. ✅ **Executive Dashboard** - Compliance metrics suitable for board reporting
9. ✅ **GDPR Art. 32 Compliance Score** - Calculated compliance percentage
10. ✅ **Audit Evidence Package** - Documentation suitable for ISO 27001, GDPR, FADP audits

---

# Assessment Workflow

## Overview of Assessment Process

Complete the assessment in **4 phases**:

**PHASE 1: INVENTORY (Sheets 2-4)** - Document all 20 TOMs

- Assess implementation status
- Identify gaps
- Rate effectiveness
- Link to evidence

**PHASE 2: EVIDENCE (Sheet 5)** - Collect proof of implementation

- Gather technical evidence (configs, logs, tests)
- Gather organizational evidence (policies, training, audits)
- Document evidence locations
- Verify evidence adequacy

**PHASE 3: ANALYSIS (Sheets 6-7)** - Assess gaps and plan remediation

- Conduct gap analysis
- Assess risks (likelihood × impact)
- Prioritize remediation
- Assign ownership and timelines

**PHASE 4: REPORTING (Sheet 8)** - Generate compliance metrics

- Calculate implementation rate
- Calculate effectiveness rate
- Calculate GDPR Art. 32 compliance score
- Prepare executive summary

## Step-by-Step Completion Sequence

**Step 1: Read Sheet 1 (Instructions & Legend)** [15 minutes]

- Understand the 20 TOM categories
- Review status definitions
- Review effectiveness ratings
- Review risk rating methodology

**Step 2: Complete Sheet 2 (TOM Control Inventory)** [8-12 hours]

- For EACH of the 20 TOMs (Rows 2-21):
  - Rate implementation status (Implemented/Partially/Planned/Not Implemented)
  - Enter implementation date
  - Write detailed description (3-5 paragraphs)
  - Reference evidence in Sheet 5
  - Rate effectiveness (Effective/Partially Effective/Ineffective/Not Tested)
  - Document last test date
  - Identify gaps
  - Assess risk level (Critical/High/Medium/Low)
  - Note remediation plan
  - Assign remediation owner
  - Set target completion date

**Step 3: Complete Sheets 3-4 (Deep-Dive Analysis)** [12-16 hours]

- **Sheet 3 (Technical Measures):** For each T1-T10:
  - List technologies deployed
  - Document configuration details
  - Calculate coverage percentage
  - Note exceptions
  - Describe system integrations

- **Sheet 4 (Organizational Measures):** For each O1-O10:
  - List policies in place
  - Describe training/communication
  - Document governance structure
  - Explain monitoring methods
  - Describe improvement processes

**Step 4: Complete Sheet 5 (Evidence Repository)** [8-12 hours]

- For EACH TOM, document evidence:
  - Evidence ID (auto-generated)
  - Evidence type
  - Description
  - File location
  - Evidence date
  - Verification status
  - Verifier
  - Notes

**Step 5: Complete Sheet 6 (Gap Analysis)** [4-6 hours]

- For EACH identified gap:
  - Generate Gap ID
  - Link to TOM ID
  - Describe gap
  - Assess likelihood (High/Medium/Low)
  - Assess impact (Critical/High/Medium/Low)
  - Calculate overall risk (formula-based)
  - Assign remediation priority
  - Document residual risk (post-remediation)
  - Justify risk acceptance (if applicable)

**Step 6: Complete Sheet 7 (Remediation Action Plan)** [4-6 hours]

- For EACH gap requiring remediation:
  - Generate Action ID
  - Link to TOM ID and Gap
  - Describe proposed solution
  - Assign owner
  - Set start date and target date
  - Track status (Not Started/In Progress/Blocked/Complete/Cancelled)
  - Update % complete
  - Record completion date

**Step 7: Review Sheet 8 (Compliance Dashboard)** [1-2 hours]

- Verify auto-calculated metrics
- Review implementation rate (target: ≥90%)
- Review effectiveness rate (target: ≥95%)
- Review gap distribution
- Review remediation progress
- Review GDPR Art. 32 compliance score
- Identify areas for improvement

**Step 8: Quality Review** [2-4 hours]

- Use Quality Checklist (Section 7)
- Verify all required fields completed
- Validate evidence adequacy
- Check calculations
- Review narrative descriptions
- Verify evidence links
- Test formulas

**Step 9: Approval & Sign-Off** [1-2 hours]

- Security review (CISO)
- Privacy review (DPO)
- Compliance review (Compliance Officer)
- Executive approval (as required)
- Document approval in workbook
- Set next review date

## Phase-by-Phase Dependencies

**PHASE 1 Dependencies:**

- Must complete A.5.34.1 (PII Identification) first
- Requires access to all technical systems
- Requires access to all policy documentation

**PHASE 2 Dependencies:**

- Cannot complete Sheet 5 until TOMs are documented in Sheet 2
- Evidence collection requires system access
- Evidence validation requires technical expertise

**PHASE 3 Dependencies:**

- Gap analysis requires completed TOM inventory
- Risk assessment requires gap identification
- Remediation planning requires gap risk ratings

**PHASE 4 Dependencies:**

- Dashboard requires all sheets completed
- Compliance score calculation requires evidence verification
- Executive reporting requires DPO/CISO review

---

# Sheet-by-Sheet Completion Guidance

## Sheet 1: Instructions & Legend

**Purpose:** Reference guide embedded in workbook

**What to Do:**
1. Read this sheet first to understand TOM framework
2. Review the 20 TOM categories (T1-T10 Technical, O1-O10 Organizational)
3. Understand implementation status definitions:

   - **Implemented:** Control fully deployed (90-100% coverage)
   - **Partially Implemented:** Control exists with gaps (50-89% coverage)
   - **Planned:** Control approved but not deployed (<50% with plan)
   - **Not Implemented:** Control not in place (<50% with no plan)

4. Understand effectiveness ratings:

   - **Effective:** Control operating as intended, validated through testing
   - **Partially Effective:** Control operating but with known limitations
   - **Ineffective:** Control failing to meet objectives
   - **Not Tested:** Control existence not verified through testing

5. Understand risk rating methodology (likelihood × impact matrix)
6. Note evidence requirements for each TOM category

**No data entry required on this sheet.**

---

## Sheet 2: TOM Control Inventory

**Purpose:** Document implementation status of all 20 TOM categories

**Pre-Populated Content:**

- **Rows 2-11:** T1-T10 (Technical Measures) - pre-filled in Columns A-B
- **Rows 12-21:** O1-O10 (Organizational Measures) - pre-filled in Columns A-B
- **Columns A-B:** TOM ID and TOM Category (locked - do not edit)

**For EACH TOM (Rows 2-21), Complete Columns C-N:**

### Column C - TOM Type
**Pre-filled:** Technical or Organizational (locked)

### Column D - Implementation Status
**Dropdown Options:** Implemented, Partially Implemented, Planned, Not Implemented

**Decision Criteria:**

- **Implemented (✅):** 90-100% coverage across all in-scope systems/processes
- **Partially Implemented (⚠️):** 50-89% coverage, functional but with gaps
- **Planned (📄):** <50% coverage, approved project in flight
- **Not Implemented (❌):** <50% coverage, no approved plan

**Example Decision Tree (T1 - Encryption):**
```
Question 1: Is data encrypted in transit (HTTPS/TLS)?
→ Yes (100% of web services) → +50 points
→ Partial (80% of web services) → +40 points  
→ No (<50%) → +0 points

Question 2: Is data encrypted at rest (database, file storage)?
→ Yes (100% of databases) → +50 points
→ Partial (80% of databases) → +40 points
→ No (<50%) → +0 points

TOTAL SCORE:

- 90-100 points → Implemented ✅
- 50-89 points → Partially Implemented ⚠️
- 1-49 points → Planned 📄 (if project exists) or Not Implemented ❌

```

**Real-World Examples:**

**Example 1: T1 - Encryption (Partially Implemented)**
```
Implementation Status: ⚠️ Partially Implemented

Rationale:
✅ ENCRYPTION IN TRANSIT (95% coverage):

- TLS 1.3 deployed on all external web services (100%)
- TLS 1.2 deployed on internal web services (100%)
- SFTP used for all file transfers (100%)
- Email encryption (TLS opportunistic) for external email (90%)
- VPN encryption (AES-256) for remote access (100%)

⚠️ ENCRYPTION AT REST (70% coverage):

- Database TDE enabled on 14/20 production databases (70%)

  → 6 legacy Oracle databases pending upgrade

- Full-disk encryption on 95% of laptops (FDE via BitLocker)
- Cloud storage encrypted (S3 default encryption, Azure Storage SSE)
- Backup encryption via Veeam (100%)
- File share encryption: Only confidential/restricted shares encrypted (50%)

OVERALL COVERAGE: (95% + 70%) / 2 = 82.5% → Partially Implemented ⚠️

Gap: 6 legacy databases, 50% of file shares not encrypted
Risk: Medium (legacy databases contain limited PII, file shares mostly internal data)
```

**Example 2: O2 - Staff Training (Implemented)**
```
Implementation Status: ✅ Implemented

Rationale:
✅ ANNUAL PRIVACY TRAINING (100% completion):

- Platform: KnowBe4 online learning management system
- GDPR/FADP module: 60 minutes, mandatory for all staff (1,250 employees)
- 2025 completion rate: 98.4% (1,230/1,250)

  → 20 incomplete due to recent hires (grace period 30 days from hire date)

- Quiz requirement: 80% passing score, unlimited retakes allowed
- Certificate issued upon completion

✅ ROLE-SPECIFIC TRAINING (100% of PII handlers):

- Deep-dive training: 90 minutes, mandatory for PII handlers (350 employees)
- Topics: Data minimization, pseudonymization, DSR handling, breach response
- 2025 completion rate: 100% (350/350)
- Includes practical exercises (mock DSR requests)

✅ PHISHING AWARENESS (quarterly):

- Simulated phishing campaigns: Quarterly via KnowBe4
- Q1 2025: 12% click rate → Q4 2025: 3% click rate (75% improvement)
- Clickers receive immediate micro-training (5 minutes)

✅ DPO CERTIFICATION:

- DPO certified: CIPP/E (Certified Information Privacy Professional/Europe)
- Recertification: Annual CPE requirements met

COVERAGE: 100% of staff trained, 98.4% completion rate → Implemented ✅
```

**Example 3: O4 - Vendor Management (Not Implemented)**
```
Implementation Status: ❌ Not Implemented

Rationale:
❌ NO FORMAL VENDOR RISK ASSESSMENT PROCESS:

- No vendor privacy risk assessment questionnaire
- No DPA template or review process
- No vendor onboarding checklist
- Procurement lacks privacy review step

⚠️ AD-HOC DPA COLLECTION (30% coverage):

- DPAs executed with 6/20 processors (30%)

  → Only major vendors (Salesforce, AWS, Microsoft, Google Workspace, HubSpot, Zoom)

- 14 processors lack DPAs (email marketing tools, analytics providers, payment processors)
- DPAs not centrally tracked or monitored

❌ NO VENDOR AUDIT RIGHTS EXERCISED:

- No vendor audits conducted (internal or external)
- No SOC 2 reports requested or reviewed
- No vendor security assessments

❌ NO PROCESSOR INVENTORY:

- No comprehensive list of processors
- Marketing and IT maintain separate (incomplete) vendor lists
- No classification of processors vs. controllers vs. sub-processors

COVERAGE: 30% DPA coverage, 0% formal risk assessment → Not Implemented ❌

Gap: Entire vendor management lifecycle needs implementation
Risk: HIGH - Material GDPR non-compliance (Art. 28), regulatory risk, vendor breach risk
```

### Column E - Implementation Date
**Format:** YYYY-MM-DD
**Guidance:** When was control first deployed?

- If phased deployment, use date of initial rollout
- If enhanced over time, use original deployment date
- If not yet implemented, leave blank

**Examples:**

- T1 Encryption: 2020-03-15 (when first TLS deployment completed)
- O2 Training: 2021-06-01 (when first annual training launched)
- O4 Vendor Mgmt: [blank] (not implemented)

### Column F - Description of Implementation
**Length:** 3-5 paragraphs (400-800 words)
**Required Elements:**
1. **WHAT:** List specific controls implemented
2. **HOW:** Explain how controls function technically/operationally
3. **WHERE:** Specify systems, locations, environments where deployed
4. **WHO:** Identify responsible team/owner
5. **COVERAGE:** Quantify coverage percentage with numerator/denominator

**Quality Standards:**

- ✅ **GOOD:** Specific, measurable, verifiable (e.g., "TLS 1.3 on 95/100 web services")
- ❌ **BAD:** Vague, generic, unverifiable (e.g., "We use encryption")

**Example (T2 - Access Control):**
```
WHAT: Role-Based Access Control (RBAC) implemented across all PII-handling systems using Azure Active Directory (Entra ID) as centralized identity provider (IdP). 18 security groups defined based on job functions: Customer_Service_Agent, Data_Analyst, System_Administrator, HR_Specialist, Finance_Team, Marketing_User, Legal_Team, Executive_Management, IT_Support, Network_Admin, Database_Admin, Security_Team, Audit_Team, Contractor_Limited, Temporary_Worker, External_Partner, API_Service_Account, System_Service_Account. Multi-Factor Authentication (MFA) mandatory for all human users via Microsoft Authenticator push notification or FIDO2 security key. Privileged Access Management (PAM) deployed via CyberArk for administrative accounts.

HOW: Users authenticate via Entra ID single sign-on (SSO) with MFA as second factor. Access requests submitted via ServiceNow ticketing system with automated routing to manager for approval. Just-in-Time (JIT) access granted for temporary elevated privileges (valid 4-8 hours, auto-expires). Privileged sessions recorded via CyberArk session monitoring. Password policy enforced: 14 characters minimum, complexity enabled, 90-day expiration, 24-password history. Conditional Access policies enforce MFA from untrusted networks, block legacy authentication protocols (POP3, IMAP, SMTP AUTH).

WHERE: Entra ID integrated with: Salesforce (CRM), Microsoft 365 (email/SharePoint), AWS (cloud infrastructure via SAML federation), Azure SQL Database, SAP (ERP), HubSpot (marketing automation), Zoom (video conferencing), GitHub (source code), Confluence/Jira (documentation), VPN (Cisco AnyConnect with RADIUS integration). On-premises Active Directory synchronized via Entra ID Connect. 95% of applications integrated with Entra ID (95/100 apps). 5 legacy applications (AS/400 mainframe, 2 custom .NET apps, vendor portal, building access system) use local authentication (planned migration to Entra ID in 2027).

WHO: Identity and Access Management (IAM) team (3 FTEs) manages Entra ID, group membership, access reviews. Security Operations Center (SOC) monitors access logs via Splunk SIEM. IT Service Desk handles access requests. Information Security (InfoSec) team defines RBAC roles and conducts quarterly access reviews.

COVERAGE: 95/100 applications integrated with Entra ID (95%). 1,250 users enabled for MFA (100% human users). 14 privileged accounts managed via CyberArk (100% of privileged accounts). Access reviews conducted quarterly covering 18 security groups (100% review coverage). 5 legacy applications represent gap (5% of applications, contain minimal PII, scheduled for retirement or SSO integration by Q2 2027).
```

**Example (O3 - Incident Response & Breach Notification):**
```
WHAT: Incident Response Plan (IRP-2024-v2.1) approved by CISO 2024-08-15, defines 6-phase incident response process: (1) Preparation, (2) Detection & Analysis, (3) Containment, (4) Eradication, (5) Recovery, (6) Post-Incident Review. Breach notification procedure (BNP-2024-v1.2) approved by DPO 2024-09-01, implements GDPR Article 33 (notification to supervisory authority) and Article 34 (communication to data subjects) requirements. Incident response team: 12 members (CISO, DPO, IT Director, Security Architect, SOC Manager, Network Engineer, Database Admin, Legal Counsel, HR Director, Communications Director, External Counsel on-call, Forensics Consultant on-call).

HOW: Security incidents detected via: (1) SIEM alerts (Splunk Enterprise Security), (2) EDR alerts (CrowdStrike Falcon), (3) User reports (security@company.com), (4) Vulnerability scan findings (Qualys), (5) Third-party notifications (vendors, partners). Severity classification: P1-Critical (active breach, data exfiltration), P2-High (contained breach, suspected data access), P3-Medium (vulnerability exploitation attempt), P4-Low (policy violation, minor anomaly). Breach assessment criteria: (1) Confidentiality breach? (2) PII involved? (3) Risk to data subject rights? (4) GDPR Article 33 threshold met? Notification timeline: 72 hours from breach awareness to supervisory authority (Swiss FDPIC or EU DPA), without undue delay to data subjects (if high risk). Incident communication: Secure incident channel (Microsoft Teams private channel), escalation matrix, stakeholder notification templates, PR crisis communication plan.

WHERE: Incident response managed via: ServiceNow Security Incident Response (SIRT) module for case tracking, Splunk for log analysis, CyberArk for evidence collection (privileged session recordings), Microsoft Sentinel for threat intelligence correlation, SharePoint (secure library) for evidence storage, External forensics provider (CyberForensics Inc.) on retainer for P1/P2 incidents. Breach notification templates stored in DPO SharePoint library: FDPIC notification template (German/French), EDPS notification template (English), Data subject notification letter template (6 languages), Media statement template, Internal communication template.

WHO: Security Operations Center (SOC) performs initial triage (24/7). Incident Commander (IC) appointed based on severity: P1/P2 = CISO, P3 = Security Architect, P4 = SOC Manager. DPO assesses breach notification requirements and drafts notifications. Legal Counsel reviews external communications. Communications Director handles media relations. Forensics Consultant (CyberForensics Inc.) performs deep forensics for P1/P2 incidents.

COVERAGE: Incident response process operational 24/7/365. 12/12 incident response team members trained (2024-11-15 tabletop exercise: ransomware scenario). 100% of security incidents logged in ServiceNow SIRT (Q4 2025: 142 incidents, P1=2, P2=5, P3=48, P4=87). 2 P1 breaches in 2025: (1) Phishing compromise of 1 account (72-hour notification met, 0 PII exposed, no GDPR notification required), (2) Misconfigured S3 bucket (public exposure 4 days, 12 records exposed, FDPIC notified within 72 hours, affected data subjects notified within 7 days, incident closed with no enforcement action). Breach notification templates tested and pre-approved by Legal/DPO. Post-incident reviews conducted for 100% of P1/P2 incidents.
```

### Column G - Evidence Reference
**Format:** EV-[TOM ID]-### (e.g., EV-T1-001, EV-T2-003)
**Guidance:** Link to Sheet 5 (Evidence Repository) entries
**Examples:**

- T1 Encryption: EV-T1-001, EV-T1-002, EV-T1-003 (TLS configs, TDE configs, FDE reports)
- O2 Training: EV-O2-001, EV-O2-002 (training completion report, quiz results)

### Column H - Effectiveness Rating
**Dropdown Options:** Effective, Partially Effective, Ineffective, Not Tested

**Decision Criteria:**

- **Effective (✅):** Control operating as intended, validated through testing, no known failures
- **Partially Effective (⚠️):** Control operating but with limitations, some failures identified
- **Ineffective (❌):** Control failing to meet objectives, significant failures, needs replacement
- **Not Tested (🔍):** Control existence not verified through testing (testing required)

**Testing Methods by TOM:**

- **T1 Encryption:** TLS test (SSL Labs), TDE verification (database query), FDE verification (device sample)
- **T2 Access Control:** Access review (user permissions), penetration test (privilege escalation), SOC 2 audit
- **T3 Pseudonymization:** Data inspection (verify PII masked), query test (cannot reverse pseudonymization)
- **T4 Data Minimization:** Privacy audit (compare collected vs. required data fields)
- **T5 Security Monitoring:** SIEM test (inject test event, verify alert), alert tuning validation
- **T6 Network Security:** Firewall rule review, network scan (Nmap), penetration test
- **T7 Application Security:** SAST/DAST scan results, penetration test, bug bounty findings
- **T8 Endpoint Security:** EDR test (inject malware sample), anti-malware effectiveness rate
- **T9 Backup & Recovery:** Backup restoration test (quarterly), RTO/RPO validation
- **T10 Physical Security:** Physical security audit, access log review
- **O1 Policies:** Document review (policy up-to-date, approved, published)
- **O2 Training:** Training completion report, quiz results, phishing simulation results
- **O3 Incident Response:** Tabletop exercise, breach simulation, post-incident review
- **O4 Vendor Management:** Vendor assessment report, DPA review, SOC 2 report review
- **O5 Privacy by Design:** DPIA review, privacy architecture review
- **O6 Accountability:** DPO appointment verification, data ownership matrix review
- **O7 Risk Management:** Risk assessment report review, DPIA completion verification
- **O8 Compliance Monitoring:** Internal audit report, ISO 27001 surveillance audit report
- **O9 Documentation:** ROPA completeness check, consent log audit, DSR log review
- **O10 Business Continuity:** BC/DR test (annual), RTO/RPO validation

**Examples:**
```
T5 - Security Monitoring: EFFECTIVE ✅
Last Test: 2025-12-01 (SIEM validation test)
Test Results: Injected 10 test events (failed login, privilege escalation, data export), 10/10 generated alerts within SLA (5 minutes). Alert accuracy: 95% (minimal false positives). SOC response time: 100% of alerts triaged within 15 minutes.

O3 - Incident Response: PARTIALLY EFFECTIVE ⚠️
Last Test: 2025-11-15 (ransomware tabletop exercise)  
Test Results: Incident response team activated within 30 minutes (✅). Communication with DPO delayed 90 minutes (❌ target 30 minutes). 72-hour breach notification process understood by 10/12 participants (⚠️ 2 participants unclear on GDPR thresholds). Forensics provider engaged within 2 hours (✅). Lessons learned: Need to improve DPO notification process, provide refresher training on GDPR notification requirements.
```

### Column I - Last Test Date
**Format:** YYYY-MM-DD
**Guidance:** When was control effectiveness last validated?
**Testing Frequency Standards:**

- **Technical controls (T1-T10):** Quarterly or after major changes
- **Organizational controls (O1-O10):** Annually or after major changes
- **Critical controls (T1, T2, T5, O3):** Quarterly minimum

**Examples:**

- T1 Encryption: 2025-12-15 (TLS test via SSL Labs)
- O2 Training: 2025-11-01 (training completion report generated)

### Column J - Gaps Identified
**Format:** Narrative description (2-5 paragraphs)
**Content:** Describe any deficiencies, exceptions, or areas where control falls short of full implementation

**Examples:**
```
T1 - Encryption GAPS:
1. 6/20 production databases lack TDE (Transparent Data Encryption). These are legacy Oracle 11g databases that require upgrade to Oracle 12c+ to support TDE. Databases contain: customer contact info (3 databases), HR records (1 database), financial transactions (2 databases). Risk: MEDIUM - Databases protected by network segmentation and access controls, but lack defense-in-depth.

2. 50% of file shares not encrypted at rest. Only shares classified as Confidential/Restricted encrypted. Internal-classified shares not encrypted. File shares contain: project documents (mostly non-PII), internal communications (some PII in email exports). Risk: LOW - File shares access-controlled via AD groups, limited PII exposure.

3. Email encryption opportunistic (TLS) not mandatory. External email uses opportunistic TLS (fallback to unencrypted if recipient doesn't support TLS). 10% of external email sent unencrypted (Q4 2025 analysis). Risk: LOW - Sensitive data sent via S/MIME or password-protected PDF as policy requires, but policy compliance not enforced technically.

Total Gap Impact: MEDIUM - Primary concern is unencrypted databases. File share and email gaps are lower priority.

O4 - Vendor Management GAPS:
1. No formal vendor privacy risk assessment process. Procurement lacks privacy review checkpoint. Result: Vendors onboarded without privacy due diligence. Risk: HIGH - Material GDPR non-compliance (Art. 28 requires adequate safeguards before engaging processor).

2. DPA coverage 30% (6/20 processors). 14 processors lack executed DPAs: email marketing (4 vendors), analytics (3 vendors), payment processing (2 vendors), HR tech (2 vendors), facility management (1 vendor), benefits administration (1 vendor), travel booking (1 vendor). Risk: HIGH - GDPR Article 28 requires written DPA with all processors before processing begins. Current state is material non-compliance.

3. No vendor audit rights exercised. Zero vendor audits conducted. Zero SOC 2 reports requested/reviewed. Zero vendor security assessments. Risk: MEDIUM - Cannot verify processor compliance with GDPR Article 28 obligations. Blind trust model.

4. No comprehensive processor inventory. Marketing and IT maintain separate incomplete lists. True number of processors unknown (estimated 30-50). Sub-processor identification not performed. Risk: MEDIUM - Cannot assess true vendor risk exposure. Cannot fulfill supervisory authority information requests.

Total Gap Impact: HIGH - Entire vendor management lifecycle needs urgent implementation. Material GDPR non-compliance.
```

### Column K - Risk Level
**Dropdown Options:** Critical, High, Medium, Low, N/A

**Risk Matrix (Likelihood × Impact):**
```
                    IMPACT
                Low     Medium  High    Critical
LIKELIHOOD  
High        Medium  High    Critical Critical
Medium      Low     Medium  High     Critical  
Low         Low     Low     Medium   High
```

**Likelihood Assessment:**

- **High:** Gap likely to be exploited or control failure likely within 12 months
- **Medium:** Gap may be exploited or control failure possible within 12-24 months  
- **Low:** Gap unlikely to be exploited or control failure unlikely within 24+ months

**Impact Assessment:**

- **Critical:** Massive PII breach (>100,000 records), material regulatory enforcement, business-ending event
- **High:** Large PII breach (10,000-100,000 records), regulatory investigation, significant financial/reputational harm
- **Medium:** Moderate PII breach (1,000-10,000 records), supervisory authority inquiry, manageable financial/reputational harm
- **Low:** Small PII breach (<1,000 records), minor supervisory authority concern, minimal financial/reputational harm

**Examples:**
```
T1 - Encryption Gap (6 unencrypted databases): MEDIUM RISK
→ Likelihood: LOW (databases network-segmented, access-controlled, monitored)
→ Impact: HIGH (if breached, 50,000+ customer records exposed)
→ Overall Risk: MEDIUM

O4 - Vendor Management Gap (no DPAs, no risk assessment): HIGH RISK  
→ Likelihood: MEDIUM (vendor breach risk increasing, regulatory scrutiny increasing)
→ Impact: HIGH (20 processors, unknown risk, material GDPR non-compliance, potential enforcement action)
→ Overall Risk: HIGH
```

### Column L - Remediation Plan
**Format:** 1-3 paragraphs describing proposed solution
**Content:** HOW will gap be closed? WHEN? WHO owns it? WHAT resources needed?

**Examples:**
```
T1 - Encryption Remediation Plan:
Phase 1 (Q1 2026): Upgrade 3 highest-priority databases (customer contact databases) to Oracle 19c, enable TDE. Owner: Database Admin team. Budget: $45,000 (licensing + migration). Phase 2 (Q2 2026): Upgrade 2 financial transaction databases to Oracle 19c, enable TDE. Owner: Database Admin team. Budget: $30,000. Phase 3 (Q3 2026): Upgrade HR database to Oracle 19c, enable TDE. Owner: Database Admin team. Budget: $15,000. Total budget: $90,000. Alternative considered: Migrate to Azure SQL Database (cloud) with automatic TDE, estimated cost $120,000, longer timeline (12 months), decided to upgrade in-place for faster resolution. File share encryption (lower priority): Implement Microsoft Purview Information Protection automatic encryption for Internal-classified shares. Timeline: Q4 2026. Owner: IT Infrastructure team. Budget: Included in existing M365 E5 licensing. Email encryption (lowest priority): Enforce mandatory TLS via Exchange transport rule (reject non-TLS external email). Timeline: Q4 2026. Owner: Email Admin team. Budget: $0 (configuration change only). Requires business approval due to potential delivery failures.

O4 - Vendor Management Remediation Plan:
Phase 1 (Q1 2026): Implement vendor privacy risk assessment process. Tasks: (1) Create vendor risk assessment questionnaire (DPO + Legal), (2) Integrate questionnaire into procurement workflow (Procurement + IT), (3) Define risk scoring methodology (DPO + CISO), (4) Train procurement team (DPO). Owner: DPO. Budget: $20,000 (consulting support for questionnaire development). Phase 2 (Q2 2026): Backfill DPAs with existing processors. Tasks: (1) Send DPA template to all 14 processors lacking DPAs, (2) Negotiate and execute DPAs, (3) Centralize DPA storage in SharePoint library, (4) Track DPA expiration dates. Owner: Legal Counsel. Budget: $50,000 (legal time, contract negotiation). Phase 3 (Q3 2026): Conduct initial vendor audits. Tasks: (1) Request SOC 2 Type II reports from top 10 processors, (2) Review reports and document findings, (3) Conduct on-site audits of 3 highest-risk processors, (4) Document audit results and remediation requirements. Owner: Internal Audit team. Budget: $30,000 (external audit support). Phase 4 (Q4 2026): Create comprehensive processor inventory. Tasks: (1) Survey all departments for processor lists, (2) Consolidate into master inventory, (3) Classify processors by risk level, (4) Map processors to processing activities in ROPA, (5) Identify sub-processors. Owner: Compliance Officer. Budget: $15,000 (data classification consulting). Total budget: $115,000. Ongoing annual cost: $25,000 (annual vendor risk assessments, SOC 2 report reviews, periodic audits).
```

### Column M - Remediation Owner
**Format:** Full name and role
**Examples:**

- "Jane Smith, Database Administrator"
- "John Doe, Data Protection Officer"  
- "Alice Johnson, CISO"

### Column N - Target Completion Date
**Format:** YYYY-MM-DD
**Guidance:** When should gap be closed?
**Prioritization:**

- **Critical risk gaps:** 30-60 days
- **High risk gaps:** 90-180 days
- **Medium risk gaps:** 6-12 months
- **Low risk gaps:** 12-24 months

---

## Sheet 3: Technical Measures Deep-Dive

**Purpose:** Detailed technical documentation of T1-T10 implementation

**Structure:** One section per TOM (T1-T10), each section contains 5 fields

**For EACH Technical Measure (T1-T10), Document:**

### Technologies Deployed
**Length:** 1-2 paragraphs
**Content:** List specific products, vendors, versions
**Example (T1 - Encryption):**
```
TECHNOLOGIES DEPLOYED:

ENCRYPTION IN TRANSIT:

- Web servers: nginx 1.24.0 with TLS 1.3, TLS 1.2 fallback, cipher suite: TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256, TLS_AES_128_GCM_SHA256
- Load balancers: AWS Application Load Balancer (ALB) with TLS termination, enforced HTTPS redirect, HSTS header (max-age=31536000)
- Email: Microsoft Exchange Online with mandatory TLS 1.2 for external email, TLS 1.2 opportunistic with MTA-STS for inbound
- File transfer: SFTP (OpenSSH 8.9p1), AWS S3 Transfer Acceleration (TLS 1.2), Azure Files (SMB 3.1.1 with AES-256-GCM encryption)
- VPN: Cisco AnyConnect with IKEv2, AES-256-GCM, SHA-384 HMAC, DH Group 20 (ECDH 384-bit)
- Database connections: TLS 1.2 enforced for all database connections (SQL Server, Oracle, PostgreSQL)

ENCRYPTION AT REST:

- Databases: SQL Server TDE (AES-256), Oracle TDE (AES-192), PostgreSQL (pgcrypto AES-256)
- Cloud storage: AWS S3 default encryption (SSE-S3 AES-256), Azure Blob Storage (AES-256), Google Cloud Storage (AES-256)
- File servers: Windows Server 2022 BitLocker (AES-256-XTS), Linux dm-crypt with LUKS (AES-256-XTS)
- Laptops: Windows 10/11 BitLocker (AES-256-XTS, TPM 2.0), macOS FileVault 2 (AES-256-XTS)
- Backup: Veeam Backup & Replication v12 with AES-256 encryption, backup repository with immutability (air-gapped backup storage)

```

### Configuration Details
**Length:** 2-3 paragraphs  
**Content:** Technical configuration specifics, settings, parameters
**Example (T2 - Access Control):**
```
CONFIGURATION DETAILS:

AZURE AD CONFIGURATION:

- Tenant ID: 12345678-90ab-cdef-1234-567890abcdef
- Licenses: Entra ID Premium P2 (1,250 licenses), Microsoft 365 E5 (1,250 licenses)
- Custom domain: sso.company.com (federated with Entra ID)
- Password policy: 14-character minimum, complexity enabled (uppercase, lowercase, numbers, symbols), 90-day expiration, 24-password history, account lockout after 5 failed attempts (15-minute lockout duration)
- MFA enforcement: Enabled for all users, registration required within 14 days of account creation, authentication methods: Microsoft Authenticator (primary), FIDO2 security key (backup), SMS (emergency only)
- Conditional Access policies: 12 policies configured

  → Policy 1: Require MFA for all cloud apps (All users, All cloud apps, Grant: Require MFA)
  → Policy 2: Block legacy authentication (All users, Exchange ActiveSync/Other clients, Block)
  → Policy 3: Require compliant device for Confidential data (All users, Confidential-classified apps, Grant: Require device compliance)
  → Policy 4: Require hybrid Entra ID joined device for on-prem apps (All users, On-premises apps, Grant: Require hybrid Entra ID joined device)
  → Policy 5: Block access from non-corporate networks to admin portals (Admin users, Azure portal, Grant: Require location: Corporate Network)
  → Policy 6-12: (additional policies for guest access, service accounts, external collaboration, risk-based access, app protection policies)

RBAC CONFIGURATION:

- 18 security groups: Customer_Service_Agent (250 members), Data_Analyst (45 members), System_Administrator (12 members), HR_Specialist (8 members), Finance_Team (25 members), Marketing_User (60 members), Legal_Team (5 members), Executive_Management (8 members), IT_Support (18 members), Network_Admin (5 members), Database_Admin (3 members), Security_Team (6 members), Audit_Team (4 members), Contractor_Limited (50 members), Temporary_Worker (20 members), External_Partner (15 members), API_Service_Account (25 service accounts), System_Service_Account (50 service accounts)
- Group membership: Managed via HR system integration (Workday), automatic provisioning/deprovisioning, manual approval for privileged groups (System_Administrator, Database_Admin, Network_Admin)
- Application permissions: Salesforce (12 permission sets mapped to 6 security groups), AWS (8 IAM roles mapped via SAML federation), Azure (15 Azure RBAC roles via Entra ID groups), SAP (6 SAP roles mapped to 4 security groups)

PAM (CyberArk) CONFIGURATION:

- CyberArk version: Privileged Access Security 13.2
- Vaults: Production Vault (12 privileged accounts), Non-Production Vault (8 privileged accounts)
- Platforms: Windows Domain Admin, Linux root, SQL Server SA, Oracle SYS, AWS IAM admin, Azure Global Admin
- Access workflow: Self-service request via CyberArk web portal, JIT access (4-8 hour sessions), password rotation after each session, session recording (100% of privileged sessions), dual control for production database access (2-person approval)

```

### Coverage Percentage
**Format:** X% (numerator/denominator)
**Content:** Quantify scope of implementation
**Example (T6 - Network Security):**
```
COVERAGE PERCENTAGE:

FIREWALL COVERAGE:

- Network segments: 18/20 segments protected by next-generation firewall (90%)

  → Protected: Corporate LAN (5 VLANs), Corporate WLAN (3 SSIDs), VPN (2 concentrators), DMZ (2 zones), Branch offices (4 sites), Cloud VPCs (2 AWS VPCs)
  → Unprotected: Legacy OT network (air-gapped, isolated, no internet access), Guest WLAN (internet-only access, no internal resources)

- Firewall vendors: Palo Alto Networks PA-5260 (primary datacenter), Palo Alto Networks PA-3260 (secondary datacenter), Palo Alto Networks PA-440 (branch offices), AWS Network Firewall (cloud VPCs)

INTRUSION DETECTION COVERAGE:

- Network IDS: Sensors deployed at 12/15 critical network locations (80%)

  → Covered: DMZ ingress/egress (4 sensors), Datacenter core switches (2 sensors), Branch office WAN links (4 sensors), Cloud VPC traffic mirroring (2 sensors)
  → Not covered: Guest WLAN (low-risk, internet-only), Legacy OT network (air-gapped), Internal LAN inter-VLAN traffic (future deployment)

- IDS vendor: Cisco Secure IDS (formerly Cisco FireSIGHT)

NETWORK SEGMENTATION COVERAGE:

- Network segmentation: 15/18 segments properly segmented with firewall rules (83%)

  → Segmented: Production network (VLAN 10-15), Corporate office (VLAN 20-25), DMZ (VLAN 30-31), VPN (VLAN 40), Branch offices (VLAN 50-54), Cloud VPCs (VPC-PROD, VPC-DEV)
  → Flat network (to be segmented): Legacy LAN (VLAN 100, mixed-use, scheduled for re-architecture Q2 2026), Dev/Test (VLAN 200, shared access, scheduled for micro-segmentation Q3 2026)

Overall Network Security Coverage: (90% + 80% + 83%) / 3 = 84%
```

### Exceptions
**Format:** Bulleted list or paragraph
**Content:** Systems, processes, or scenarios where control doesn't apply
**Example (T8 - Endpoint Security):**
```
EXCEPTIONS:

ENDPOINT SECURITY EXCLUSIONS:
1. **5 legacy Windows Server 2008 R2 systems** (end-of-life, no longer supported by CrowdStrike EDR agent)

   - Systems: AS/400 terminal server (1), Crystal Reports server (1), legacy .NET app servers (3)
   - Justification: Servers scheduled for decommissioning Q2 2026, isolated network VLAN, compensating controls (network IDS, firewall rules, manual patching)
   - Risk: MEDIUM - Servers contain minimal PII, limited internet access, monitored via SIEM

2. **Industrial control systems (ICS/SCADA)** - air-gapped OT network (8 systems)

   - Systems: Building management system (BMS), HVAC controllers (3), Physical access control system (PACS), Video surveillance system (2), Fire alarm system (1)
   - Justification: OT systems incompatible with EDR agent (vendor certification requirements, real-time performance constraints), air-gapped from corporate network
   - Risk: LOW - No PII on OT systems, physical access required for exploitation, monitored via ICS-specific monitoring (Nozomi Networks)

3. **50 contractor laptops** (managed by contractor employer, not by [Organization])

   - Systems: Contractor-owned devices, VPN access only, no access to internal network
   - Justification: Contractors prohibited from installing company software on personal devices per contractor agreement
   - Risk: LOW - Contractors access only cloud apps via VPN (Salesforce, Microsoft 365), no local PII storage, conditional access enforces device compliance checks (managed by contractor employer)

4. **15 mobile hotspots** (cellular routers for remote/field workers)

   - Systems: Netgear Nighthawk M6 mobile routers, used by field technicians
   - Justification: Routers are IoT devices, no EDR support, provide internet connectivity only
   - Risk: LOW - Routers provide internet only, no PII storage, VPN required for corporate access, firewall enforced

Total Exceptions: 78 devices excluded from EDR coverage (78/1,400 endpoints = 5.6% exception rate)
```

### Integration Notes
**Format:** 1-2 paragraphs
**Content:** How control integrates with other systems, dependencies
**Example (T5 - Security Monitoring & Logging):**
```
INTEGRATION NOTES:

SIEM DATA SOURCES (42 log sources integrated with Splunk Enterprise Security):

- Windows: Active Directory (authentication logs), Exchange (email logs), Windows Servers (event logs via Universal Forwarder)
- Linux: Syslog forwarding from 85 Linux servers (auth logs, audit logs, application logs)
- Network: Palo Alto firewalls (traffic logs, threat logs), Cisco switches (NetFlow), Cisco IDS (alerts)
- Cloud: AWS CloudTrail (API calls, resource changes), Azure Activity Log (Azure resource changes), Microsoft 365 Unified Audit Log (user activity, admin changes, mailbox access)
- Applications: Salesforce Event Monitoring (user login, data export, API calls), SAP Security Audit Log (transaction logs, authorization changes), GitHub Audit Log (code commits, access changes)
- Security tools: CrowdStrike Falcon EDR (endpoint detections, process execution, file modifications), CyberArk (privileged session logs, password retrieval), Okta (authentication events via SIEM integration)

ALERT WORKFLOWS:

- Splunk ES generates 150-200 notable events per day (automated enrichment via Splunk SOAR)
- Notable events triaged by SOC analysts via Splunk Mission Control dashboard
- P1/P2 incidents escalated via PagerDuty (on-call rotation: SOC Manager → Security Architect → CISO)
- Incident cases created in ServiceNow SIRT module (bidirectional sync with Splunk ES)
- Threat intelligence enrichment via MISP (Malware Information Sharing Platform), integration with Splunk Threat Intelligence Management

RETENTION & COMPLIANCE:

- Splunk indexes: 90-day hot storage (SSD), 12-month warm storage (spinning disk), 7-year cold storage (AWS S3 Glacier)
- GDPR/FADP compliance: Right to be forgotten implemented via Splunk data deletion command, retention aligned with legal requirements (7 years for financial logs, 5 years for security logs per Swiss banking regulations)
- Archive compression: ~30% of original size via Splunk SmartStore
- Backup: Splunk configuration backed up daily, indexes backed up weekly via Veeam

```

---

## Sheet 4: Organizational Measures Deep-Dive

**Purpose:** Detailed organizational documentation of O1-O10 implementation

**Structure:** One section per TOM (O1-O10), each section contains 5 fields

**For EACH Organizational Measure (O1-O10), Document:**

### Policies in Place
**Length:** 1-2 paragraphs
**Content:** List specific policy documents, approval dates, versions
**Example (O1 - Policies & Procedures):**
```
POLICIES IN PLACE:

PRIVACY-SPECIFIC POLICIES (8 policies):
1. Privacy Policy (external-facing) - v3.2, approved 2025-06-15, published company.com/privacy, last reviewed 2025-12-01
2. Data Protection Policy (internal) - v2.1, approved 2024-09-01, published intranet/policies/data-protection, last reviewed 2025-12-01
3. Data Retention and Disposal Policy - v1.5, approved 2024-03-15, defines retention periods for 25 data categories, last reviewed 2025-09-01
4. Consent Management Policy - v1.2, approved 2024-07-01, implements GDPR Art. 7 requirements, last reviewed 2025-12-01
5. Data Subject Rights Policy - v1.3, approved 2024-08-01, implements GDPR Art. 15-22 & FADP Art. 25-28, last reviewed 2025-12-01
6. Data Breach Response Policy - v2.0, approved 2024-09-01, implements GDPR Art. 33-34 72-hour notification, last reviewed 2025-12-01
7. International Data Transfer Policy - v1.1, approved 2024-06-01, implements GDPR Chapter V (SCCs, adequacy decisions), last reviewed 2025-12-01
8. Privacy by Design and Default Policy - v1.0, approved 2024-05-01, implements GDPR Art. 25, last reviewed 2025-12-01

INFORMATION SECURITY POLICIES (15 policies):
1. Information Security Policy (master policy) - v4.0, approved 2023-12-01, last reviewed 2025-12-01
2. Acceptable Use Policy - v3.1, approved 2024-01-15, covers email, internet, mobile device use
3. Access Control Policy - v2.3, approved 2024-02-01, implements RBAC, least privilege, JIT access
4. Encryption Policy - v2.0, approved 2024-03-01, mandates TLS 1.2+ and AES-256 for PII
5. Password Policy - v3.2, approved 2024-04-01, 14-character minimum, 90-day expiration
6. Incident Response Policy - v2.5, approved 2024-09-01, 6-phase IR process
7. Vulnerability Management Policy - v2.0, approved 2024-06-01, defines scan frequency, patching SLAs
8. Vendor Management Policy - v1.8, approved 2024-07-01, third-party risk assessment requirements
9. Mobile Device Policy - v2.2, approved 2024-05-01, BYOD and corporate-owned devices
10. Remote Access Policy - v2.0, approved 2024-04-01, VPN mandatory, MFA required
11. Network Security Policy - v2.1, approved 2024-03-01, firewall, segmentation, IDS requirements
12. Application Security Policy - v1.5, approved 2024-06-01, secure SDLC, code review, SAST/DAST
13. Backup and Recovery Policy - v2.3, approved 2024-02-01, RTO 24 hours, RPO 1 hour
14. Physical Security Policy - v2.0, approved 2024-01-01, datacenter access, device disposal
15. Security Awareness and Training Policy - v2.1, approved 2024-08-01, annual training mandatory

PROCEDURES (25 procedures):

- Data classification procedure, Data subject rights request procedure, Consent collection procedure, Cookie management procedure, Data deletion procedure, Data breach notification procedure, DPIA procedure, Privacy impact assessment procedure, Vendor onboarding procedure, Vulnerability scanning procedure, Patch management procedure, Incident response procedure, Access request procedure, Password reset procedure, Account provisioning/deprovisioning procedure, Log review procedure, Security monitoring procedure, Firewall change procedure, Network access procedure, Application deployment procedure, Code review procedure, Penetration testing procedure, Backup restoration procedure, Disaster recovery procedure, Physical access procedure

All policies reviewed annually, approved by CISO/DPO, published on company intranet, version-controlled in SharePoint.
```

### Training/Communication
**Length:** 1-2 paragraphs
**Content:** Describe training programs, communication methods, completion rates
**Example (O2 - Staff Training & Awareness):**
```
TRAINING/COMMUNICATION:

ANNUAL MANDATORY PRIVACY TRAINING:

- Platform: KnowBe4 Security Awareness Training
- Module: "GDPR & Swiss FADP Compliance for [Organization] Employees"  
- Duration: 60 minutes (self-paced online)
- Content: PII definition, lawful basis for processing, data minimization, purpose limitation, data subject rights, consent requirements, breach notification, international transfers, employee responsibilities
- Quiz: 20 questions, 80% passing score, unlimited retakes, certificate upon completion
- 2025 Completion: 1,230/1,250 employees (98.4%)

  → 20 incomplete: 15 new hires (grace period 30 days from hire date), 5 on long-term leave

- Reminder cadence: Email reminder at 7 days, 3 days, 1 day before deadline, escalation to manager if not completed within 30 days
- Training deadline: January 31 annually (Q4 prior year for new hires)
- Recordkeeping: Completion tracked in KnowBe4, certificate stored in employee record (HR system), audit report generated quarterly

ROLE-SPECIFIC DEEP-DIVE TRAINING:

- Target audience: PII handlers (350 employees: Customer Service, Marketing, HR, Finance, Legal, IT)
- Module: "Advanced Privacy Practices for PII Handlers"
- Duration: 90 minutes (self-paced online) + 30-minute live Q&A with DPO (optional)
- Content: Data minimization techniques, pseudonymization, anonymization, encryption, access control, secure data transfer, data retention, secure disposal, DSR handling, consent management, breach response, vendor management, DPIA requirements
- Practical exercises: Mock DSR requests (access request, erasure request, portability request), mock breach assessment, mock DPIA scoping
- 2025 Completion: 350/350 (100%)
- Delivery: Q2 annually (April-June), mandatory for new PII handlers within 60 days of role assignment

PHISHING AWARENESS PROGRAM:

- Platform: KnowBe4 Phishing Security Tests
- Frequency: Monthly simulated phishing campaigns (12 campaigns per year)
- Campaigns: Varied difficulty (easy, medium, hard), varied tactics (credential harvesting, malicious attachment, malicious link, CEO fraud, invoice scam, COVID-19 phishing)
- Immediate training: Clickers receive immediate micro-training (5-minute module), "Think Before You Click" landing page
- 2025 Results:

  → Q1: 12% click rate (baseline)
  → Q2: 8% click rate (33% improvement)
  → Q3: 5% click rate (58% improvement)
  → Q4: 3% click rate (75% improvement)
  → Top clickers (>3 clicks in 12 months): 45 employees → targeted remedial training (15-minute 1-on-1 with Security Awareness Manager)

- Leaderboard: Monthly leaderboard published (department-level, no individual shaming), recognition for top-performing departments

DPO CERTIFICATION & CONTINUING EDUCATION:

- DPO: Jane Doe (Data Protection Officer)
- Certification: CIPP/E (Certified Information Privacy Professional/Europe) - IAPP certification, obtained 2020-11-15, recertified 2024-11-15
- Continuing education: 20 CPE credits annually (conferences, webinars, self-study)

  → 2025 CPE: 22 credits (IAPP Europe Data Protection Congress 10 credits, IAPP webinars 6 credits, self-study 6 credits)

- Professional membership: IAPP (International Association of Privacy Professionals), Swiss Privacy Officers Association

COMMUNICATION CHANNELS:

- Privacy newsletter: Monthly newsletter via email ("Privacy Matters" newsletter), covers: regulatory updates (GDPR guidance, EDPB decisions, FDPIC guidance), privacy tips, breach case studies, DSR statistics, upcoming training
- Intranet: Privacy Hub on company intranet, contains: Policies, procedures, training materials, DSR request form, DPO contact info, privacy FAQ, breach reporting form
- Privacy awareness campaigns: Quarterly campaigns (Data Privacy Day, GDPR anniversary, Cybersecurity Awareness Month, Privacy Awareness Week), posters, desk drops, screensavers, lunch & learns
- DPO office hours: Weekly office hours (Thursdays 2-4pm), drop-in Q&A, privacy consultations
- Management briefings: Quarterly privacy updates to executive management (Board of Directors receives annual privacy report)

```

### Governance Structure
**Format:** 1-2 paragraphs
**Content:** Who is responsible, reporting lines, oversight mechanisms
**Example (O6 - Accountability & Governance):**
```
GOVERNANCE STRUCTURE:

PRIVACY GOVERNANCE ROLES:

- **Chief Executive Officer (CEO):** Ultimate accountability for privacy compliance, signs off on annual privacy report to Board of Directors
- **Data Protection Officer (DPO):** Jane Doe, dedicated full-time role (100% FTE), reports directly to General Counsel (dotted line to CEO), independent from business operations per GDPR Art. 38, budget authority for privacy initiatives, authority to escalate to Board of Directors
- **Chief Information Security Officer (CISO):** John Smith, owns technical security controls (TOMs T1-T10), reports to CEO, collaborates with DPO on privacy-security alignment
- **General Counsel:** Owns legal compliance, reviews all privacy notices, DPAs, contracts, advises DPO on legal interpretation
- **Chief Information Officer (CIO):** Owns IT systems and data infrastructure, implements DPO's technical requirements, allocates resources for privacy projects
- **Chief Human Resources Officer (CHRO):** Owns employee data processing, implements HR-specific privacy controls, manages employee consent, handles employee DSRs

PRIVACY COMMITTEE (cross-functional governance):

- **Members (10):** DPO (Chair), CISO, General Counsel, CIO, CHRO, CFO, Chief Marketing Officer (CMO), Chief Product Officer (CPO), Head of Internal Audit, Chief Risk Officer (CRO)
- **Meeting frequency:** Monthly (second Wednesday), 90-minute meetings, mandatory attendance
- **Charter:** Review privacy risks, approve major privacy initiatives (new processing activities, high-risk DPIAs, international transfers), review breach incidents, review DSR trends, review regulatory updates, escalate to Board of Directors as needed
- **Quorum:** 6/10 members required for voting, DPO has tie-breaking vote
- **Minutes:** Recorded by DPO's office, stored in SharePoint (retained 7 years), reviewed/approved at next meeting
- **Escalation:** Critical issues escalated to Board of Directors within 48 hours (data breaches, supervisory authority inquiries, high-risk processing without mitigations)

BOARD OF DIRECTORS OVERSIGHT:

- **Audit Committee:** Receives annual privacy report (presented by DPO), reviews privacy risks in enterprise risk register, approves privacy budget
- **Privacy report content:** Compliance status (GDPR, FADP, ISO 27001), DSR metrics, breach incidents, supervisory authority interactions, privacy risk landscape, remediation status, budget requests
- **Meeting frequency:** Quarterly Audit Committee meetings include privacy update (15-minute DPO presentation), annual deep-dive (60-minute session)

DATA OWNERSHIP FRAMEWORK:

- **Data Owners (12):** Executive-level owners assigned to each major processing activity

  → Customer data: CMO (Chief Marketing Officer)
  → Employee data: CHRO (Chief Human Resources Officer)
  → Financial data: CFO (Chief Financial Officer)
  → Product data: CPO (Chief Product Officer)
  → Vendor data: Chief Procurement Officer
  → Patient data: Chief Medical Officer (healthcare vertical)
  → Clinical trial data: Head of Clinical Operations (healthcare vertical)
  → Claims data: Chief Claims Officer (insurance vertical)
  → Underwriting data: Chief Underwriting Officer (insurance vertical)
  → Sales data: Chief Revenue Officer
  → IT systems data: CIO (Chief Information Officer)
  → Security logs: CISO (Chief Information Security Officer)

- **Accountability:** Data Owners accountable for: Lawfulness of processing, Data quality, Data minimization, Retention compliance, Vendor management (processors), DPIA approval, DSR handling, Breach reporting
- **RACI Matrix:** Documented in ISMS-IMP-A.5.34.1 (PII Identification Assessment), updated quarterly, reviewed by Privacy Committee

INTERNAL AUDIT FUNCTION:

- **Internal Audit team:** 4 FTEs (Head of Internal Audit + 3 auditors), reports to Audit Committee (Board of Directors), independent from operational management
- **Privacy audit scope:** Annual privacy audit (comprehensive), quarterly spot checks (DSR handling, consent management, vendor DPAs), ad-hoc audits (breach response, high-risk processing)
- **Audit findings:** Documented in audit reports, shared with DPO, CISO, General Counsel, escalated to Audit Committee if material findings
- **Remediation tracking:** Internal Audit tracks remediation of findings, validates closure, reports status to Audit Committee quarterly

```

### Monitoring Method
**Format:** 1-2 paragraphs
**Content:** How is effectiveness monitored, KPIs tracked
**Example (O8 - Compliance Monitoring & Audit):**
```
MONITORING METHOD:

INTERNAL PRIVACY AUDITS:

- **Annual comprehensive privacy audit:** Conducted by Internal Audit team, scope: All 20 TOMs, GDPR/FADP compliance verification, control effectiveness testing, evidence review, gap identification
- **2025 Audit results:** 95% compliance score, 12 findings (2 High, 6 Medium, 4 Low), all findings remediated within SLA (High: 60 days, Medium: 90 days, Low: 180 days)
- **Audit methodology:** ISO 27001 audit approach, evidence-based testing, sample-based for large populations (e.g., 30 DSR requests tested from 250 total), 100% testing for critical controls (e.g., all DPAs reviewed)
- **Audit report:** Shared with DPO, CISO, General Counsel, Privacy Committee, Audit Committee (Board of Directors), documented recommendations and management responses

QUARTERLY COMPLIANCE MONITORING:

- **DSR compliance monitoring (quarterly):**

  → Sample 20 DSR requests per quarter, verify: (1) SLA compliance (30-day response), (2) Completeness of response, (3) Evidence of verification, (4) Proper redaction/minimization, (5) Documentation in DSR log
  → 2025 Q4 Results: 20/20 DSR requests compliant (100% compliance rate)

- **Consent audit (quarterly):**

  → Sample 50 consent records per quarter, verify: (1) Freely given, (2) Specific, (3) Informed, (4) Unambiguous indication, (5) Withdrawal mechanism present, (6) Documentation in consent log
  → 2025 Q4 Results: 48/50 consent records compliant (96% compliance rate, 2 findings: insufficient granularity in 2 cookie consent mechanisms → remediated)

- **Vendor DPA audit (quarterly):**

  → Review all processors onboarded in quarter, verify: (1) DPA executed before processing begins, (2) DPA contains GDPR Art. 28 mandatory clauses, (3) DPA stored centrally, (4) Sub-processors identified
  → 2025 Q4 Results: 3 new processors onboarded, 3/3 DPAs executed (100% compliance), 1 finding: Sub-processor list incomplete for 1 vendor → remediated

COMPLIANCE DASHBOARD (ISMS-IMP-A.5.34.7):

- **Privacy Compliance Dashboard:** Consolidated view of all privacy metrics
- **KPIs tracked:**

  → TOM implementation rate (target: ≥90%, current: 87%)
  → TOM effectiveness rate (target: ≥95%, current: 92%)
  → DSR SLA compliance rate (target: ≥95%, current: 98%)
  → Consent audit pass rate (target: ≥95%, current: 96%)
  → DPA coverage rate (target: 100%, current: 30% → in remediation)
  → Breach notification SLA compliance (target: 100%, current: 100%)
  → Training completion rate (target: ≥95%, current: 98.4%)
  → DPIA completion rate for high-risk processing (target: 100%, current: 85% → 3 DPIAs in progress)

- **Dashboard frequency:** Updated monthly, reviewed by Privacy Committee, quarterly Board reporting
- **Trend analysis:** YoY comparison, quarterly trend charts, red/yellow/green status indicators

EXTERNAL AUDITS & CERTIFICATIONS:

- **ISO 27001:2022 certification:** Certified since 2020, surveillance audits annually, recertification every 3 years

  → 2025 Surveillance Audit (September): Zero non-conformities, 3 observations (opportunities for improvement), certificate valid until 2027
  → Auditor: TÜV SÜD (accredited certification body)

- **SOC 2 Type II audit:** Annual audit, scope: Security, Confidentiality, Privacy (TSC + CC sections)

  → 2025 SOC 2 Report: Unqualified opinion, zero exceptions, control effectiveness validated
  → Auditor: Deloitte & Touche LLP
  → Report period: October 1, 2024 - September 30, 2025
  → Report issuance: November 15, 2025

- **GDPR adequacy assessment:** Independent third-party assessment by privacy consultancy

  → 2025 Assessment: 92% GDPR compliance score, 8 recommendations for improvement (all in remediation)
  → Assessor: OneTrust Professional Services

REGULATORY INTERACTIONS:

- **Supervisory authority:** Swiss Federal Data Protection and Information Commissioner (FDPIC)
- **2025 Interactions:** Zero enforcement actions, 1 inquiry (routine questionnaire on AI processing → responded within 30 days, no follow-up)
- **Complaint handling:** 2 data subject complaints filed with FDPIC in 2025:

  → Complaint 1: DSR response time (claimed 45-day response, actual: 28 days, complaint dismissed)
  → Complaint 2: Marketing opt-out not honored (investigation confirmed bug in email platform, remediated within 7 days, complaint closed with warning)

- **Proactive reporting:** 1 breach notified to FDPIC in 2025 (misconfigured S3 bucket, 12 records exposed 4 days, notification within 72 hours, no enforcement action)

```

### Improvement Process
**Format:** 1-2 paragraphs
**Content:** How is measure continuously improved
**Example (O2 - Staff Training & Awareness):**
```
IMPROVEMENT PROCESS:

TRAINING CONTENT UPDATES (annual):

- **Regulatory changes:** Training content updated annually based on:

  → GDPR guidance updates (EDPB guidelines, CJEU case law, national DPA guidance)
  → Swiss FADP amendments (FDPIC guidance, Federal Council ordinances)
  → Supervisory authority enforcement actions (case studies from EDPB, FDPIC, ICO, CNIL)
  → Example: 2025 updates included EDPB Guidelines 05/2022 on consent (dark patterns), CJEU Schrems II decision impacts, FDPIC guidance on AI processing

- **Incident trends:** Training content adjusted based on internal incident data:

  → 2025 phishing click rate analysis: Healthcare-themed phishing most successful (15% click rate) → added healthcare phishing module to 2026 training
  → 2025 DSR errors: 5% of DSRs had incomplete responses → added DSR response checklist to role-specific training

- **Staff feedback:** Post-training surveys administered:

  → 2025 Survey Results: 4.2/5.0 average satisfaction score, 85% found content relevant, 15% requested more practical examples → 2026 training will include more case studies and practical exercises

- **Audit findings:** Internal audit findings drive training updates:

  → 2025 Audit Finding: Consent collection inconsistencies → added consent management module to 2026 training, added consent audit procedure to compliance monitoring

PHISHING SIMULATION EVOLUTION:

- **Difficulty progression:** Phishing campaign difficulty increased based on prior performance:

  → 2025 Q1: Easy campaigns (obvious phishing indicators) → 12% click rate
  → 2025 Q4: Hard campaigns (sophisticated social engineering, no obvious indicators) → 3% click rate
  → Continuous improvement: As users become more aware, campaigns become more challenging to maintain training effectiveness

- **Campaign variety:** Phishing tactics varied monthly to expose users to diverse threats:

  → Credential harvesting (fake login pages)
  → Malicious attachments (fake invoices, COVID-19 updates)
  → Malicious links (URL shorteners, typosquatting)
  → CEO fraud (fake urgent requests from executives)
  → Invoice scams (fake vendor payment requests)
  → QR code phishing (fake parking tickets, package delivery)

- **Targeted remediation:** High clickers (>3 clicks in 12 months) receive personalized remedial training:

  → 2025: 45 high clickers identified → 100% completed remedial training (15-minute 1-on-1 with Security Awareness Manager)
  → Post-remediation results: High clickers' subsequent click rate dropped from 25% to 5% (80% improvement)

LEARNING MANAGEMENT SYSTEM (LMS) ANALYTICS:

- **KnowBe4 analytics dashboard:** Tracks completion rates, quiz scores, time spent, module engagement
- **2025 Analytics insights:**

  → Privacy training: Average quiz score 88% (target: 80%), average time spent 65 minutes (target: 60 minutes), 98.4% completion rate
  → Role-specific training: Average quiz score 92%, average time spent 95 minutes (target: 90 minutes), 100% completion rate
  → Top-performing departments: IT (100% completion, 95% quiz average), Legal (100% completion, 98% quiz average), Finance (100% completion, 92% quiz average)
  → Lowest-performing departments: Operations (95% completion, 85% quiz average) → targeted outreach to Operations management

- **Continuous improvement:** LMS analytics inform 2026 training improvements:

  → Modules with low engagement scores (<4.0/5.0) redesigned
  → Modules with high drop-off rates (>10%) shortened or split into smaller modules
  → Quiz questions with <70% pass rate reviewed for clarity or content gaps

DPO CONTINUING EDUCATION:

- **Professional development plan:** DPO maintains annual professional development plan:

  → 2025 Plan: IAPP Europe Data Protection Congress (Prague), IAPP webinar series (AI regulation, international transfers, cookie compliance), self-study (EDPB guidelines, CJEU case law), Swiss Privacy Officers Association quarterly meetings
  → 2025 Actual: 22 CPE credits earned (target: 20 credits)

- **Knowledge sharing:** DPO shares learnings with organization:

  → Quarterly privacy newsletter includes regulatory updates from DPO continuing education
  → Monthly Privacy Committee meetings include DPO briefing on regulatory developments
  → Annual all-staff privacy training includes latest regulatory guidance from DPO learning
```

---

## Sheet 5: Evidence Repository

**Purpose:** Centralized storage of all evidence proving TOM implementation and effectiveness

**Complete Evidence Repository for ALL 20 TOMs (T1-T10, O1-O10)**

**For EACH TOM, Store Multiple Evidence Items:**

### Column A - Evidence ID
**Format:** EV-[TOM ID]-### (auto-generated)
**Examples:**

- EV-T1-001 (first evidence item for T1 Encryption)
- EV-T1-002 (second evidence item for T1 Encryption)
- EV-O2-001 (first evidence item for O2 Training)

### Column B - TOM ID
**Format:** T1, T2, ..., T10, O1, O2, ..., O10
**Purpose:** Links evidence to specific TOM in Sheet 2

### Column C - Evidence Type
**Dropdown Options:**

- Configuration Screenshot
- Policy Document
- Training Report
- Audit Report
- Test Results
- Vendor Assessment
- Incident Response Test
- System Log Extract
- Certificate (ISO 27001, SOC 2, etc.)
- DPA (Data Processing Agreement)
- Risk Assessment
- DPIA (Data Protection Impact Assessment)
- Penetration Test Report
- Vulnerability Scan Report
- Business Continuity Test
- Disaster Recovery Test
- Other

**Examples:**

- T1 Encryption → Evidence Type: Configuration Screenshot (TLS settings)
- O2 Training → Evidence Type: Training Report (completion statistics)

### Column D - Description
**Length:** 1-3 sentences
**Content:** Brief summary of evidence
**Examples:**
```
EV-T1-001: TLS 1.3 configuration screenshot from nginx web server (prod-web-01), showing enforced TLS 1.3, cipher suite TLS_AES_256_GCM_SHA384, HSTS enabled (max-age=31536000), captured 2025-12-15.

EV-O2-001: 2025 Annual Privacy Training completion report from KnowBe4 platform, showing 1,230/1,250 employees completed (98.4%), average quiz score 88%, average time spent 65 minutes, report generated 2026-01-05.

EV-T2-005: Entra ID Conditional Access policy configuration screenshot, showing Policy CA002 "Block Legacy Authentication" enabled for all users, blocking Exchange ActiveSync and Other clients, captured 2025-12-10.

EV-O4-003: Salesforce Data Processing Agreement (DPA) v3.1 executed 2023-06-15, contains GDPR Article 28 mandatory clauses, sub-processor list attached (Annex A), stored in SharePoint /Legal/Contracts/Vendors/Salesforce/.
```

### Column E - File Location / System
**Format:** Full path to evidence file or system where evidence resides
**Examples:**
```
SharePoint: /Privacy/Evidence/2025/TLS_Config_Screenshot_20251215.png

KnowBe4 Platform: Dashboard > Reports > Annual Training Completion Report 2025

Azure Portal: Azure Active Directory > Security > Conditional Access > Policies > CA002

SharePoint: /Legal/Contracts/Vendors/Salesforce/Salesforce_DPA_v3.1_20230615.pdf

Splunk Enterprise Security: Dashboard "MFA Enrollment Report" > Saved Search "MFA_Enrollment_Status"

CrowdStrike Falcon: Dashboards > Endpoint Security Dashboard > Widget "EDR Agent Deployment Status"

CyberArk: Reports > Privileged Sessions > Report "Privileged Sessions December 2025"

Veeam Backup & Replication: Jobs > Job "Production Database Backup" > Session Details > Restore Test 2025-12-20

TÜV SÜD: ISO 27001 Surveillance Audit Report 2025-09-30 (PDF, stored SharePoint /Compliance/ISO27001/Audits/2025/)

Deloitte: SOC 2 Type II Report October 2024 - September 2025 (PDF, stored SharePoint /Compliance/SOC2/Reports/2025/)
```

### Column F - Evidence Date
**Format:** YYYY-MM-DD
**Content:** When was evidence created or captured
**Examples:**

- Configuration screenshot: Date screenshot was taken
- Audit report: Date audit was completed / report issued
- Training report: Date report was generated
- Test results: Date test was conducted

### Column G - Verification Status
**Dropdown Options:** Verified, Pending Verification, Invalid, Expired

**Decision Criteria:**

- **Verified (✅):** Evidence reviewed and confirmed adequate by DPO, CISO, or Internal Auditor
- **Pending Verification (⏳):** Evidence collected but not yet reviewed for adequacy
- **Invalid (❌):** Evidence inadequate (poor quality screenshot, incomplete report, outdated information)
- **Expired (⏳):** Evidence no longer current (stale screenshot, expired certificate, outdated audit report)

**Examples:**
```
EV-T1-001 (TLS config screenshot from 2025-12-15): VERIFIED ✅ (reviewed by Security Architect 2025-12-20, confirms TLS 1.3 properly configured)

EV-O2-001 (Training completion report): VERIFIED ✅ (reviewed by DPO 2026-01-08, confirms 98.4% completion meets target)

EV-T2-008 (Entra ID access review report from 2024-06-01): EXPIRED ⏳ (report >6 months old, quarterly access review required, new report pending)

EV-O4-007 (Vendor risk assessment for new processor XYZ Corp): PENDING VERIFICATION ⏳ (assessment completed 2025-12-20, awaiting DPO review)

EV-T7-003 (Application penetration test report from external consultant): INVALID ❌ (report incomplete, missing risk ratings and remediation recommendations, consultant re-engagement required)
```

### Column H - Verified By
**Format:** Full name and role of verifier
**Examples:**

- "Jane Doe, Data Protection Officer"
- "John Smith, Chief Information Security Officer"
- "Alice Johnson, Security Architect"
- "Bob Williams, Internal Audit Manager"

### Column I - Notes
**Format:** Additional context, caveats, follow-up actions
**Examples:**
```
Evidence EV-T1-005 (Database TDE config): TDE enabled on 14/20 production databases. 6 databases pending upgrade to Oracle 12c+ to support TDE (remediation project in Sheet 7, Action ID ACT-T1-001, target Q2 2026).

Evidence EV-O4-010 (Vendor DPA with ABC Corp): DPA executed 2025-11-01. Note: Sub-processor list in Annex A is incomplete (vendor confirmed 3 additional sub-processors not listed). Amended DPA requested 2025-12-15, pending vendor signature.

Evidence EV-T5-002 (SIEM alert tuning validation): False positive rate reduced from 25% (Q1 2025) to 5% (Q4 2025) through iterative rule tuning. SOC Manager recommends quarterly tuning reviews to maintain effectiveness.

Evidence EV-O3-001 (Incident response tabletop exercise): Exercise identified 2 gaps: (1) DPO notification delayed 90 minutes (target 30 minutes), (2) GDPR breach notification threshold unclear to 2/12 participants. Remediation: Update IR plan to include DPO notification checklist, provide refresher training on GDPR notification requirements (action item added to Sheet 7).
```

**Evidence Repository Best Practices:**

- **Comprehensiveness:** Aim for 5-10 evidence items per TOM
- **Variety:** Include different evidence types (technical configs, policies, audit reports, test results)
- **Currency:** Update evidence regularly (technical configs quarterly, audit reports annually)
- **Accessibility:** Store evidence in centralized, access-controlled repository (SharePoint recommended)
- **Auditability:** Ensure evidence can be easily retrieved for audits (clear file naming, logical folder structure)

---

## Sheet 6: Gap Analysis & Risk Assessment

**Purpose:** Document all identified gaps with risk ratings

**For EACH Gap Identified (from Sheet 2 Column J), Complete:**

### Column A - Gap ID
**Format:** GAP-[TOM ID]-### (e.g., GAP-T1-001, GAP-O4-001)

### Column B - TOM ID
**Format:** Link to TOM in Sheet 2 (e.g., T1, O4)

### Column C - Gap Description
**Length:** 1-3 paragraphs
**Content:** Detailed description of the gap
**Example:**
```
GAP-T1-001: Unencrypted Databases (6/20 production databases lack TDE)

6 production databases do not have Transparent Data Encryption (TDE) enabled. These are legacy Oracle 11g databases that require upgrade to Oracle 12c or higher to support TDE. The 6 databases contain:
- 3 databases: Customer contact information (name, email, phone, address) for 50,000 customers
- 1 database: Employee records (name, SSN, salary, performance reviews) for 1,200 employees
- 2 databases: Financial transaction history (credit card tokens, transaction amounts, merchant names) for 100,000 transactions

Current compensating controls:

- Network segmentation (databases in isolated VLAN, firewall rules restrict access)
- Access control (database access via AD groups, least privilege, privileged accounts in CyberArk)
- Encryption in transit (TLS 1.2 for all database connections)
- Security monitoring (database audit logs forwarded to Splunk SIEM)

Gap impact: If database server is compromised (OS-level access gained), attacker could read database files directly (bypassing database access controls), exposing PII in cleartext. This violates GDPR Article 32 requirement for encryption of personal data.
```

### Column D - Likelihood
**Dropdown Options:** High, Medium, Low

**Assessment Criteria:**

- **High:** Vulnerability actively exploited, significant attack surface, known threat actor interest, weak compensating controls
- **Medium:** Vulnerability known but not actively exploited, moderate attack surface, some compensating controls
- **Low:** Vulnerability theoretical, small attack surface, strong compensating controls

**Example Decision:**
```
GAP-T1-001 (Unencrypted databases) Likelihood: LOW

Rationale:

- Databases network-segmented in isolated VLAN (attacker needs to breach perimeter first)
- Database servers patched monthly (vulnerability window small)
- OS access restricted to 3 database administrators (small attack surface)
- Privileged accounts in CyberArk (session recording, JIT access)
- No known exploits targeting Oracle 11g database servers in recent 12 months
- SOC monitoring for unusual database access patterns (SIEM alerts configured)
- Compensating controls significantly reduce likelihood of successful exploitation

Conclusion: While gap exists, likelihood of exploitation is LOW due to defense-in-depth architecture.
```

### Column E - Impact
**Dropdown Options:** Critical, High, Medium, Low

**Assessment Criteria:**

- **Critical:** >100,000 PII records exposed, material regulatory enforcement (€20M or 4% global revenue fine), business-ending reputational harm
- **High:** 10,000-100,000 PII records exposed, significant regulatory investigation, major financial/reputational harm
- **Medium:** 1,000-10,000 PII records exposed, supervisory authority inquiry, manageable financial/reputational harm
- **Low:** <1,000 PII records exposed, minor supervisory authority concern, minimal financial/reputational harm

**Example Decision:**
```
GAP-T1-001 (Unencrypted databases) Impact: HIGH

Rationale:

- 6 databases contain 50,000 customer records + 1,200 employee records + 100,000 financial transactions = 151,200 PII records total
- PII categories: Names, SSNs, salaries, credit card tokens, contact details (high sensitivity)
- GDPR breach notification required (Article 33: supervisory authority within 72 hours, Article 34: data subjects without undue delay)
- Potential GDPR fine: Up to €20M or 4% of global revenue per Article 83
- Potential Swiss FADP fine: Up to CHF 250,000 per Article 60
- Reputational harm: Customer trust erosion, media coverage, competitor advantage
- Financial harm: Breach response costs ($500K-$1M estimated), legal fees, regulatory fines, customer compensation, business interruption

Conclusion: Impact is HIGH due to large number of PII records and significant financial/regulatory/reputational consequences.
```

### Column F - Overall Risk
**Formula:** `=IF(AND(D2="High", OR(E2="High", E2="Critical")), "Critical", IF(AND(D2="Medium", E2="Critical"), "Critical", IF(OR(AND(D2="High", E2="Medium"), AND(D2="Medium", E2="High")), "High", IF(OR(AND(D2="Low", E2="High"), AND(D2="Medium", E2="Medium")), "Medium", "Low"))))`

**Risk Matrix:**
```
                    IMPACT
                Low     Medium  High    Critical
LIKELIHOOD  
High        Medium  High    Critical Critical
Medium      Low     Medium  High     Critical  
Low         Low     Low     Medium   High
```

**Example:**
```
GAP-T1-001: Likelihood=LOW, Impact=HIGH → Overall Risk=MEDIUM
```

### Column G - Risk Score
**Formula:** `=IF(F2="Critical", 4, IF(F2="High", 3, IF(F2="Medium", 2, IF(F2="Low", 1, 0))))`

**Scoring:**

- Critical = 4
- High = 3
- Medium = 2
- Low = 1

**Purpose:** Enables sorting and prioritization (sort by risk score descending to prioritize remediation)

### Column H - Remediation Priority
**Formula:** `=IF(G2=4, "URGENT (30 days)", IF(G2=3, "HIGH (90 days)", IF(G2=2, "MEDIUM (6 months)", "LOW (12 months)")))`

**Priorities:**

- Critical risk → URGENT (30-60 days)
- High risk → HIGH (90-180 days)
- Medium risk → MEDIUM (6-12 months)
- Low risk → LOW (12-24 months)

### Column I - Residual Risk (Post-Remediation)
**Dropdown Options:** Critical, High, Medium, Low, N/A

**Content:** What will the risk level be after remediation is complete?

**Example:**
```
GAP-T1-001 (Unencrypted databases) Residual Risk: LOW

Rationale:
After remediation (database upgrade to Oracle 19c + TDE enabled):

- Database files encrypted with AES-256
- Encryption keys managed by Oracle TDE
- Even if OS-level access gained, database files unreadable without TDE keys
- TDE keys protected by database master key (stored in HSM or OS keystore with restrictive permissions)
- Defense-in-depth: Encryption at rest + network segmentation + access control + monitoring

Post-remediation risk: LOW (encryption eliminates primary risk vector)
```

### Column J - Acceptance Justification
**Format:** 1-2 paragraphs (only if risk accepted without remediation)

**Content:** Why is risk accepted? Who approved? What are compensating controls?

**Example (Risk Acceptance Scenario):**
```
GAP-O4-002: No vendor audits conducted (LOW RISK)

RISK ACCEPTANCE JUSTIFICATION:
Risk accepted by Privacy Committee 2025-12-15 for following reasons:

1. Cost-benefit analysis: Conducting on-site vendor audits for 20 processors estimated cost $200,000 annually (external audit firms). Benefit: Increased assurance of vendor compliance, but SOC 2 reports provide similar assurance at zero additional cost.

2. Compensating control: Requesting SOC 2 Type II reports from all processors in lieu of on-site audits. SOC 2 reports provide independent third-party verification of controls (security, confidentiality, privacy). 15/20 processors have current SOC 2 reports (75% coverage). 5 processors without SOC 2 reports are low-risk (low PII volume, limited processing scope).

3. Risk level: Overall risk rated LOW. Likelihood of vendor breach is MEDIUM (general threat landscape), Impact if breach occurs is LOW (due to limited PII volume in these 5 vendors, ~5,000 records total). Overall Risk: LOW.

4. Alternative approach: Implement vendor risk assessment questionnaire (GAP-O4-001 remediation) to identify high-risk vendors. High-risk vendors (>10,000 PII records, high-risk processing) will be required to provide SOC 2 reports or undergo on-site audits. Low-risk vendors can be managed via questionnaire + contractual DPA requirements.

5. Review: Risk acceptance reviewed annually by Privacy Committee. If risk landscape changes (e.g., vendor breach occurs, regulatory guidance requires audits, supervisor authority inquiry), risk acceptance will be re-evaluated.

Approved by: Privacy Committee (DPO, CISO, General Counsel, CIO) 2025-12-15
Next review: 2026-12-15
```

**Note:** Risk acceptance without remediation should be rare. Most gaps should have remediation plans in Sheet 7.

---

## Sheet 7: Remediation Action Plan

**Purpose:** Track remediation actions for closing gaps

**For EACH Gap Requiring Remediation (from Sheet 6), Complete:**

### Column A - Action ID
**Format:** ACT-[TOM ID]-### (e.g., ACT-T1-001, ACT-O4-001)

### Column B - TOM ID
**Format:** Link to TOM in Sheet 2 (e.g., T1, O4)

### Column C - Gap Description
**Content:** Copy from Sheet 6 Column C (or abbreviated version)
**Example:** "6/20 production databases lack TDE encryption"

### Column D - Proposed Solution
**Length:** 2-5 paragraphs
**Content:** Detailed action plan - HOW will gap be closed?

**Example:**
```
PROPOSED SOLUTION for ACT-T1-001 (Unencrypted Databases):

PHASE 1 - DATABASE ASSESSMENT (January 2026, 2 weeks):

- Inventory all 6 unencrypted databases (names, versions, data volumes, dependencies)
- Identify application dependencies (which applications connect to each database?)
- Assess upgrade complexity (downtime requirements, testing scope, rollback procedures)
- Calculate storage impact (TDE increases database size ~5-10%, ensure sufficient disk space)
- Prioritize databases by PII sensitivity and business criticality

PHASE 2 - PILOT UPGRADE (February 2026, 4 weeks):

- Select 1 low-risk database for pilot (non-production database or lowest-criticality production database)
- Perform Oracle 11g → Oracle 19c upgrade in non-production environment
- Enable TDE on upgraded database
- Conduct functional testing (application connectivity, query performance, backup/restore)
- Document lessons learned and refine procedure

PHASE 3 - PRODUCTION ROLLOUT (March-August 2026, 24 weeks):

- Batch 1 (March 2026): Upgrade 2 customer contact databases (highest priority, customer-facing data)

  → Schedule maintenance window (Saturday 2AM-6AM, 4-hour window)
  → Communicate to application teams (2-week advance notice)
  → Upgrade database, enable TDE, validate functionality
  → Monitor for 1 week post-upgrade (performance metrics, error logs, application stability)

- Batch 2 (May 2026): Upgrade 2 financial transaction databases

  → Same procedure as Batch 1
  → Additional testing: Payment processing validation, transaction integrity checks

- Batch 3 (August 2026): Upgrade 1 HR database

  → Same procedure as Batch 1
  → Additional coordination with HR team (payroll processing schedule)
  → Upgrade 1 remaining database (lowest priority)

PHASE 4 - VALIDATION & DOCUMENTATION (September 2026, 2 weeks):

- Validate TDE enabled on all 6 databases (query sys.encrypted_tablespaces view)
- Capture evidence screenshots (TLS configs, TDE status queries)
- Update evidence repository (Sheet 5)
- Update ISMS documentation (ISMS-POL-A.8.24 Cryptography Policy)
- Conduct post-implementation review (lessons learned, process improvements)
- Close remediation action (mark Status=Complete in Column H)

BUDGET:

- Oracle 19c licenses: $90,000 (6 databases × $15,000 license)
- DBA contractor support: $25,000 (200 hours × $125/hour for upgrade assistance)
- Disk storage expansion: $10,000 (TDE overhead ~10% × 2TB total data)
- Testing environment: $5,000 (temporary cloud infrastructure for pilot testing)
- Total: $130,000

RISKS & MITIGATION:

- Risk 1: Application incompatibility with Oracle 19c

  → Mitigation: Pilot upgrade + comprehensive testing in non-production environment

- Risk 2: Downtime exceeds 4-hour maintenance window

  → Mitigation: Rehearse upgrade procedure in test environment, have rollback plan ready

- Risk 3: Performance degradation with TDE

  → Mitigation: Monitor database performance pre/post-upgrade, tune as needed (TDE CPU overhead typically <5%)

ALTERNATIVE CONSIDERED:

- Cloud migration to Azure SQL Database (automatic TDE)

  → Estimated cost: $200,000 + $50,000 annual cloud costs
  → Timeline: 12 months (longer than in-place upgrade)
  → Complexity: Higher (application re-architecture required for cloud)
  → Decision: In-place upgrade preferred (faster, lower cost, lower risk)
```

### Column E - Owner
**Format:** Full name and role
**Example:** "Bob Williams, Database Administrator"

**Ownership Guidelines:**

- **Technical measures (T1-T10):** IT/Security teams (Database Admin, Security Architect, Network Engineer)
- **Organizational measures (O1-O10):** Compliance/Legal teams (DPO, Compliance Officer, Legal Counsel)
- **Cross-functional measures:** Collaboration required (e.g., O4 Vendor Management requires Legal + Procurement + DPO)

### Column F - Start Date
**Format:** YYYY-MM-DD
**Guidance:** When will remediation begin?

**Examples:**

- ACT-T1-001 (Database upgrade): 2026-01-15 (Phase 1 assessment starts)
- ACT-O4-001 (Vendor risk assessment process): 2026-02-01 (Project kickoff)

### Column G - Target Date
**Format:** YYYY-MM-DD
**Guidance:** When should remediation be complete? Based on risk priority:

**Prioritization:**

- **Critical risk gaps:** 30-60 days from start
- **High risk gaps:** 90-180 days from start
- **Medium risk gaps:** 6-12 months from start
- **Low risk gaps:** 12-24 months from start

**Examples:**

- ACT-T1-001 (MEDIUM risk): Start 2026-01-15 → Target 2026-09-01 (8 months)
- ACT-O4-001 (HIGH risk): Start 2026-02-01 → Target 2026-08-01 (6 months)

### Column H - Status
**Dropdown Options:** Not Started, In Progress, Blocked, Complete, Cancelled

**Status Definitions:**

- **Not Started:** Project not yet begun (future start date)
- **In Progress:** Active work underway
- **Blocked:** Impediment preventing progress (e.g., budget approval pending, vendor unresponsive, technical blocker)
- **Complete:** Remediation finished and validated (evidence in Sheet 5, status updated in Sheet 2)
- **Cancelled:** Action cancelled (e.g., risk accepted, alternative solution implemented, requirements changed)

### Column I - % Complete
**Format:** 0-100%
**Guidance:** Estimated progress

**Examples:**

- 0%: Not Started
- 25%: Phase 1 complete (assessment done)
- 50%: Phase 2 complete (pilot upgrade done)
- 75%: Phase 3 in progress (2/3 batches complete)
- 100%: Complete (all phases finished, validated)

**Update Frequency:** Monthly (or more frequently for urgent/high-priority actions)

### Column J - Completion Date
**Format:** YYYY-MM-DD (blank if not complete)
**Guidance:** Actual completion date when Status=Complete

**Validation:** Completion date should align with evidence update in Sheet 5

**Example:**

- ACT-T1-001: Start 2026-01-15, Target 2026-09-01, Completion 2026-08-20 (11 days early)

---

## Sheet 8: Compliance Dashboard

**Purpose:** Executive summary of TOM compliance (auto-calculated metrics)

**NO DATA ENTRY REQUIRED - All Metrics Auto-Calculated from Sheets 2-7**

**Dashboard Sections:**

### Section 1: Implementation Status (Rows 5-12)

- **Total TOMs:** 20 (constant)
- **Implemented:** `=COUNTIF('2. TOM Control Inventory'!D2:D21,"Implemented")`
- **Partially Implemented:** `=COUNTIF('2. TOM Control Inventory'!D2:D21,"Partially Implemented")`
- **Planned:** `=COUNTIF('2. TOM Control Inventory'!D2:D21,"Planned")`
- **Not Implemented:** `=COUNTIF('2. TOM Control Inventory'!D2:D21,"Not Implemented")`
- **Implementation Rate:** `=('2. TOM Control Inventory'!Implemented + 'Partially Implemented'*0.5) / 20`
  - Formula explanation: Full implementations count 100%, partial implementations count 50%
  - **Target:** ≥90%
  - **Conditional formatting:** Green if ≥90%, Yellow if 80-89%, Red if <80%

### Section 2: Technical vs. Organizational (Rows 14-21)

- **Technical Measures Implemented:** `=COUNTIFS('2. TOM Control Inventory'!C2:C21,"Technical",'2. TOM Control Inventory'!D2:D21,"Implemented")`
- **Technical Measures Total:** 10
- **Technical Implementation Rate:** `=Technical Implemented / 10`
- **Organizational Measures Implemented:** `=COUNTIFS('2. TOM Control Inventory'!C2:C21,"Organizational",'2. TOM Control Inventory'!D2:D21,"Implemented")`
- **Organizational Measures Total:** 10
- **Organizational Implementation Rate:** `=Organizational Implemented / 10`
- **Analysis:** Technical measures typically easier to implement (buy tools/deploy technology), organizational measures require culture change and sustained effort

### Section 3: Control Effectiveness (Rows 23-30)

- **Effective Controls:** `=COUNTIF('2. TOM Control Inventory'!H2:H21,"Effective")`
- **Partially Effective Controls:** `=COUNTIF('2. TOM Control Inventory'!H2:H21,"Partially Effective")`
- **Ineffective Controls:** `=COUNTIF('2. TOM Control Inventory'!H2:H21,"Ineffective")`
- **Not Tested Controls:** `=COUNTIF('2. TOM Control Inventory'!H2:H21,"Not Tested")`
- **Effectiveness Rate:** `=Effective / (Total Implemented)`
  - Formula explanation: Only implemented controls can be tested for effectiveness
  - **Target:** ≥95% (of implemented controls should be effective)
  - **Conditional formatting:** Green if ≥95%, Yellow if 85-94%, Red if <85%
- **Testing Coverage:** `=(Effective + Partially Effective + Ineffective) / Total Implemented`
  - Formula explanation: Percentage of implemented controls that have been tested
  - **Target:** 100% (all implemented controls should be tested)

### Section 4: Gap Analysis (Rows 32-40)

- **Critical Gaps:** `=COUNTIF('6. Gap Analysis'!F2:F100,"Critical")`
- **High Gaps:** `=COUNTIF('6. Gap Analysis'!F2:F100,"High")`
- **Medium Gaps:** `=COUNTIF('6. Gap Analysis'!F2:F100,"Medium")`
- **Low Gaps:** `=COUNTIF('6. Gap Analysis'!F2:F100,"Low")`
- **Total Gaps:** `=COUNTA('6. Gap Analysis'!A2:A100)-1` (exclude header)
- **Average Risk Score:** `=AVERAGE('6. Gap Analysis'!G2:G100)`
  - Risk scores: Critical=4, High=3, Medium=2, Low=1
  - **Target:** ≤2.0 (average risk should be Medium or below)
- **Conditional formatting:** 
  - Critical Gaps: Red background, bold
  - High Gaps: Orange background
  - Medium/Low Gaps: No special formatting

### Section 5: Remediation Progress (Rows 42-50)

- **Total Actions:** `=COUNTA('7. Remediation Action Plan'!A2:A100)-1`
- **Not Started:** `=COUNTIF('7. Remediation Action Plan'!H2:H100,"Not Started")`
- **In Progress:** `=COUNTIF('7. Remediation Action Plan'!H2:H100,"In Progress")`
- **Blocked:** `=COUNTIF('7. Remediation Action Plan'!H2:H100,"Blocked")`
- **Complete:** `=COUNTIF('7. Remediation Action Plan'!H2:H100,"Complete")`
- **Cancelled:** `=COUNTIF('7. Remediation Action Plan'!H2:H100,"Cancelled")`
- **Overdue Actions:** `=COUNTIFS('7. Remediation Action Plan'!H2:H100,"In Progress",'7. Remediation Action Plan'!G2:G100,"<"&TODAY())`
- **Remediation Progress:** `=Complete / (Total Actions - Cancelled)`
  - Formula explanation: Cancelled actions excluded from denominator
  - **Target:** ≥80% (most actions should be complete)
  - **Conditional formatting:** Green if ≥80%, Yellow if 60-79%, Red if <60%
- **Average % Complete:** `=AVERAGE('7. Remediation Action Plan'!I2:I100)` (for In Progress actions only)

### Section 6: GDPR Art. 32 Compliance Score (Rows 52-60)

**Formula:**
```
=AVERAGE(
  Implementation_Rate * 0.40,      // 40% weight - Are TOMs implemented?
  Effectiveness_Rate * 0.30,       // 30% weight - Do TOMs work effectively?
  (1 - Critical_Gaps/20) * 0.20,   // 20% weight - Are critical gaps addressed?
  Remediation_Progress * 0.10      // 10% weight - Are gaps being fixed?
)
```

**Example Calculation:**
```
Implementation Rate: 85% (17/20 TOMs implemented)
Effectiveness Rate: 90% (16/18 implemented TOMs tested effective)
Critical Gaps: 1 (out of 20 TOMs)
Remediation Progress: 75% (15/20 actions complete)

GDPR Art. 32 Compliance Score:
= (0.85 * 0.40) + (0.90 * 0.30) + ((1 - 1/20) * 0.20) + (0.75 * 0.10)
= 0.34 + 0.27 + 0.19 + 0.075
= 0.875
= 87.5%
```

**Interpretation:**

- **90-100%:** Excellent compliance (best-in-class, minimal risk)
- **80-89%:** Good compliance (acceptable, minor improvements needed)
- **70-79%:** Fair compliance (significant improvements required)
- **60-69%:** Poor compliance (major gaps, urgent action required)
- **<60%:** Critical non-compliance (material GDPR violation risk)

**Conditional Formatting:**

- ≥90%: Dark green background (#006400), white bold text
- 80-89%: Light green background (#C6EFCE)
- 70-79%: Yellow background (#FFEB9C)
- 60-69%: Orange background (#FFA500)
- <60%: Red background (#C00000), white bold text

### Section 7: Evidence Summary (Rows 62-68)

- **Total Evidence Items:** `=COUNTA('5. Evidence Repository'!A2:A1000)-1`
- **Evidence by Type:** Count of each evidence type (Configuration Screenshot, Policy Document, Audit Report, etc.)
- **Verified Evidence:** `=COUNTIF('5. Evidence Repository'!G2:G1000,"Verified")`
- **Pending Verification:** `=COUNTIF('5. Evidence Repository'!G2:G1000,"Pending Verification")`
- **Expired Evidence:** `=COUNTIF('5. Evidence Repository'!G2:G1000,"Expired")`
- **Evidence Verification Rate:** `=Verified / Total Evidence Items`
  - **Target:** ≥95%

**Dashboard Charts (inserted manually after workbook generation):**
1. **TOM Implementation Status** (Pie Chart):

   - Data: Implemented, Partially Implemented, Planned, Not Implemented
   - Colors: Green, Yellow, Blue, Red

2. **Gap Risk Distribution** (Bar Chart):

   - Data: Critical, High, Medium, Low gap counts
   - Colors: Red, Orange, Yellow, Green

3. **Remediation Progress** (Bar Chart):

   - Data: Not Started, In Progress, Blocked, Complete, Cancelled
   - Colors: Gray, Blue, Red, Green, Black

---

# Evidence Collection

## What Evidence to Gather

**For Technical Measures (T1-T10), Gather:**

**T1 - Encryption:**

- ✅ TLS configuration screenshots (web servers, load balancers, email servers)
- ✅ Database TDE status queries (proof of encryption at rest)
- ✅ Full-disk encryption reports (BitLocker deployment report, FileVault report)
- ✅ Backup encryption configuration (Veeam encryption settings)
- ✅ VPN encryption configuration (Cisco AnyConnect settings)
- ✅ Cloud storage encryption configuration (AWS S3 default encryption, Azure SSE)
- ✅ SSL Labs test results (A+ rating for public-facing web services)

**T2 - Access Control:**

- ✅ Entra ID user/group report (user list, group memberships, role assignments)
- ✅ Conditional Access policy configurations (screenshots of all 12 policies)
- ✅ MFA enrollment report (percentage of users with MFA enabled)
- ✅ Password policy configuration (Entra ID password settings)
- ✅ CyberArk privileged account inventory (list of privileged accounts, access workflow)
- ✅ Access review results (quarterly access review reports)
- ✅ Least privilege validation (sample privilege escalation tests)

**T3 - Pseudonymization/Anonymization:**

- ✅ Data masking configuration (database masking rules, application-level masking)
- ✅ Anonymization procedure documentation
- ✅ Test results (query results showing PII properly masked)
- ✅ Code review (application code implementing masking)

**T4 - Data Minimization:**

- ✅ Privacy audit report (data collection vs. required fields analysis)
- ✅ Data retention policy (approved policy document)
- ✅ Automated deletion logs (scheduled deletion jobs, records deleted)
- ✅ Form/application review (web forms, mobile apps - data collection limited to necessary fields)

**T5 - Security Monitoring & Logging:**

- ✅ SIEM dashboard screenshots (Splunk Enterprise Security dashboards)
- ✅ Alert rule configurations (SIEM detection rules)
- ✅ Alert validation test results (test event injection, alert generation)
- ✅ SOC metrics (alert volume, triage time, false positive rate)
- ✅ Log retention configuration (Splunk retention policies)
- ✅ SIEM data source inventory (list of 42 log sources)

**T6 - Network Security:**

- ✅ Firewall rule exports (Palo Alto firewall rule base)
- ✅ Network segmentation diagram (VLAN architecture)
- ✅ IDS alert log samples (Cisco Secure IDS detections)
- ✅ Network scan results (Nmap scan, vulnerability scan)
- ✅ Penetration test report (external pen test results)

**T7 - Application Security:**

- ✅ SAST/DAST scan results (static/dynamic application security testing)
- ✅ Secure code review reports
- ✅ Penetration test results (web application pen test)
- ✅ WAF configuration (web application firewall rules)
- ✅ Bug bounty findings (if applicable)

**T8 - Endpoint Security:**

- ✅ EDR deployment report (CrowdStrike agent deployment status)
- ✅ Anti-malware scan logs (detection logs, quarantine logs)
- ✅ Endpoint compliance report (device compliance status)
- ✅ Mobile device management report (Intune/JAMF device inventory)

**T9 - Backup & Recovery:**

- ✅ Backup job configurations (Veeam backup jobs)
- ✅ Backup restoration test logs (quarterly DR tests)
- ✅ RTO/RPO documentation (documented recovery objectives)
- ✅ Disaster recovery plan (approved BC/DR plan)

**T10 - Physical Security:**

- ✅ Datacenter access logs (physical access control system logs)
- ✅ Video surveillance documentation (camera locations, retention periods)
- ✅ Equipment disposal certificates (certificate of destruction for decommissioned hardware)
- ✅ Physical security policy (approved policy document)

**For Organizational Measures (O1-O10), Gather:**

**O1 - Policies:**

- ✅ All privacy policy documents (8 privacy-specific policies)
- ✅ All information security policies (15 InfoSec policies)
- ✅ Policy approval records (signature pages, approval emails)
- ✅ Policy review logs (annual review documentation)
- ✅ Policy version history (document control)

**O2 - Training:**

- ✅ Training completion reports (KnowBe4 completion statistics)
- ✅ Training materials (course content, quizzes)
- ✅ Quiz results (individual and aggregate quiz scores)
- ✅ Phishing simulation results (click rates, trends)
- ✅ DPO certification (CIPP/E certificate, CPE records)
- ✅ Training records (employee training history)

**O3 - Incident Response:**

- ✅ Incident response plan (approved IRP document)
- ✅ Tabletop exercise reports (exercise documentation, lessons learned)
- ✅ Breach register (log of all security incidents)
- ✅ 72-hour notification templates (GDPR Art. 33/34 templates)
- ✅ Incident response team roster (contact list, roles)

**O4 - Vendor Management:**

- ✅ Executed DPAs (all Data Processing Agreements)
- ✅ Vendor risk assessment reports (questionnaires, scoring)
- ✅ Vendor audit reports (on-site audit reports, SOC 2 reports)
- ✅ Processor inventory (list of all processors, sub-processors)
- ✅ Vendor due diligence documentation

**O5 - Privacy by Design:**

- ✅ DPIA documentation (completed DPIAs for high-risk processing)
- ✅ Privacy requirements in project documentation (requirements docs, design docs)
- ✅ Privacy architecture review checklists
- ✅ Privacy by default configuration proof (system settings)

**O6 - Accountability:**

- ✅ DPO appointment letter (formal DPO appointment documentation)
- ✅ Data ownership matrix (RACI matrix)
- ✅ Privacy Committee meeting minutes (monthly meeting records)
- ✅ Board reporting materials (annual privacy report to Board)

**O7 - Risk Management:**

- ✅ Privacy risk assessment reports (risk registers)
- ✅ DPIA documentation (high-risk processing assessments)
- ✅ Privacy risk register (centralized risk tracking)
- ✅ Risk acceptance sign-offs (risk acceptance documentation)

**O8 - Compliance Monitoring:**

- ✅ Internal audit reports (annual privacy audit report)
- ✅ Control test results (control effectiveness testing)
- ✅ Compliance dashboard (ISMS-IMP-A.5.34.7 dashboard)
- ✅ ISO 27001 certificate (current certification, audit reports)
- ✅ SOC 2 report (SOC 2 Type II report)

**O9 - Documentation:**

- ✅ ROPA (Record of Processing Activities from A.5.34.1)
- ✅ Legal basis documentation (lawful basis records from A.5.34.2)
- ✅ DSR logs (data subject request logs from A.5.34.3)
- ✅ Consent logs (consent management records)

**O10 - Business Continuity:**

- ✅ Business continuity plan (approved BC plan)
- ✅ Disaster recovery plan (approved DR plan)
- ✅ BC/DR test reports (annual test documentation)
- ✅ RTO/RPO documentation (recovery objectives)

## Where to Find Evidence

**Technical Systems:**

- **SIEM (Splunk):** Dashboards > Reports > Saved Searches
- **Entra ID:** Azure portal > Azure Active Directory > Reports > Sign-ins/Audit logs
- **CrowdStrike:** Dashboards > Host Management > Agent Status
- **CyberArk:** Reports > Privileged Sessions
- **Veeam:** Jobs > Backup Jobs > Session Details
- **Palo Alto:** Monitor > Logs > Traffic/Threat logs
- **AWS:** CloudTrail > Event history, S3 > Bucket properties
- **Azure:** Activity Log, Storage > Encryption settings

**Administrative Systems:**

- **SharePoint:** Policy library, Evidence repository, Audit reports folder
- **KnowBe4:** Dashboard > Reports > Training Completion
- **ServiceNow:** Incident Management > SIRT module
- **HR System:** Employee training records

**Physical Documents:**

- **Policies:** Intranet/SharePoint policy library
- **Contracts/DPAs:** Legal SharePoint library /Legal/Contracts/
- **Audit Reports:** Compliance SharePoint library /Compliance/Audits/
- **Certificates:** Compliance SharePoint library /Compliance/Certifications/

## How to Document Evidence

**Best Practices:**

- **Screenshot best practices:**
  - Include URL/title bar (proves source)
  - Include timestamp (proves currency)
  - Annotate if necessary (highlight relevant sections)
  - High resolution (readable text)
  - PNG format preferred (no JPEG compression artifacts)
- **Document naming conventions:**
  - Format: `YYYYMMDD_[System]_[Description]_[Version].ext`
  - Example: `20251215_nginx_TLS_Config_v1.0.png`
- **Centralized storage:**
  - Store all evidence in SharePoint folder `/Privacy/Evidence/2025/`
  - Subfolders by TOM (e.g., `/T1_Encryption/`, `/O2_Training/`)
  - Version control enabled
  - Access restricted (Privacy team, CISO, Internal Audit)
- **Evidence metadata:**
  - Document in Sheet 5 (Evidence Repository)
  - Include: Description, date, source system, file path, verification status

---

# Common Pitfalls

## Pitfall 1: Confusing "Implemented" with "Effective"
**Issue:** Marking a TOM as "Implemented" without testing effectiveness.

**Assessment:** Implementation status (Column D) ≠ Effectiveness rating (Column H)

- **Implemented:** Control is deployed (e.g., EDR agent installed on all laptops)
- **Effective:** Control is working as intended (e.g., EDR agent detecting and blocking malware)

**Gap:** Many organizations deploy controls but never test them. Result: False sense of security.

**Remediation:** 

- Establish testing program for all implemented controls (quarterly technical controls, annually organizational controls)
- Document test results in Sheet 5 (Evidence Repository)
- Update Column H (Effectiveness Rating) based on test results
- Example: T8 Endpoint Security → Implemented (EDR deployed) → Test effectiveness (inject malware sample, verify detection/blocking) → Update rating (Effective if 100% detection, Partially Effective if 80-99%, Ineffective if <80%)

---

## Pitfall 2: Inadequate Evidence Documentation
**Issue:** Claiming control implementation without supporting evidence.

**Assessment:** Every implemented TOM must have evidence in Sheet 5.

**Gap:** Auditors will reject claims without proof. Result: Control considered "not implemented" by auditor.

**Remediation:**

- Minimum 3-5 evidence items per TOM
- Variety of evidence types (technical configs, policies, audit reports, test results)
- Current evidence (configs from last 3 months, audit reports from last 12 months)
- Example: T1 Encryption → Evidence should include: (1) TLS config screenshot, (2) Database TDE query, (3) FDE deployment report, (4) SSL Labs test result, (5) Backup encryption config

---

## Pitfall 3: Overestimating Implementation Coverage
**Issue:** Rating control as "Implemented (✅)" when coverage is actually 80% (should be "Partially Implemented ⚠️").

**Assessment:** Implemented = 90-100% coverage. 80% = Partially Implemented.

**Gap:** Organizations round up coverage percentages. Result: Gaps hidden, auditor finds discrepancies.

**Remediation:**

- Be honest about coverage percentages
- Document exceptions/exclusions explicitly (Column F in Sheet 2)
- If 80% coverage, rate as "Partially Implemented" and document gap in Column J
- Example: T2 Access Control → 95/100 applications integrated with Entra ID (95%) → "Implemented ✅". If only 85/100 (85%) → "Partially Implemented ⚠️" with gap documentation for 15 non-integrated applications.

---

## Pitfall 4: Missing Gap Risk Assessment
**Issue:** Identifying gap but not assessing risk (likelihood × impact).

**Assessment:** All gaps in Column J (Sheet 2) must have corresponding entry in Sheet 6 (Gap Analysis).

**Gap:** Without risk assessment, gaps cannot be prioritized for remediation.

**Remediation:**

- For EVERY gap in Sheet 2 Column J, create entry in Sheet 6
- Assess likelihood (High/Medium/Low)
- Assess impact (Critical/High/Medium/Low)
- Calculate overall risk using matrix
- Prioritize remediation based on risk score
- Example: T1 Encryption gap (6 unencrypted databases) → Sheet 6 entry: Likelihood=LOW (strong compensating controls), Impact=HIGH (150K PII records), Overall Risk=MEDIUM, Remediation Priority=6 months

---

## Pitfall 5: Remediation Plans Lack Detail
**Issue:** Vague remediation plans (e.g., "Implement TDE on databases" with no phases, timeline, budget, or ownership).

**Assessment:** Column D in Sheet 7 (Proposed Solution) must be actionable.

**Gap:** Vague plan = plan won't get executed. Result: Gaps remain open, auditor finds same gaps on next audit.

**Remediation:**

- Break remediation into phases (assessment, pilot, rollout, validation)
- Assign ownership to specific person (full name, role)
- Define timeline with start/target dates
- Document budget (licensing, consulting, staffing)
- Identify risks and mitigation strategies
- Define success criteria (how will you know when gap is closed?)
- Example: ACT-T1-001 (Database TDE) → 4 phases, 8-month timeline, $130K budget, owner: Database Admin, success criteria: TDE enabled on all 6 databases + evidence in Sheet 5

---

## Pitfall 6: Treating All Gaps as Equal Priority
**Issue:** Attempting to remediate all gaps simultaneously regardless of risk level.

**Assessment:** Prioritize gaps based on risk score (Column G in Sheet 6).

**Gap:** Resource constraints mean not all gaps can be closed immediately. Treating all gaps equally spreads resources thin.

**Remediation:**

- Focus on Critical/High risk gaps first (30-180 day timeline)
- Medium risk gaps next (6-12 months)
- Low risk gaps last (12-24 months)
- Accept low-risk gaps if remediation cost exceeds risk (risk acceptance in Column J)
- Example: Critical risk gap (public S3 bucket with PII) → Immediate remediation (24-48 hours). Low risk gap (no vendor audits) → Risk accepted with compensating controls (SOC 2 reports)

---

## Pitfall 7: No Evidence Verification Process
**Issue:** Evidence collected but never reviewed for adequacy (Column G in Sheet 5 remains "Pending Verification").

**Assessment:** Evidence Verification Rate (Sheet 8) should be ≥95%.

**Gap:** Unverified evidence may be inadequate for audit. Result: Auditor rejects evidence, control deemed "not implemented".

**Remediation:**

- Assign evidence verification responsibilities (DPO verifies privacy evidence, CISO verifies security evidence)
- Establish verification criteria (screenshot readable? Document approved? Test result conclusive?)
- Document verification in Column G (Verified) and Column H (Verified By)
- Reject inadequate evidence (mark "Invalid" in Column G), request replacement evidence
- Example: EV-T1-001 (TLS config screenshot) → DPO reviews screenshot → Verifies TLS 1.3 enabled, HSTS header present, cipher suite strong → Marks "Verified" → Documents verifier "Jane Doe, DPO"

---

## Pitfall 8: Confusing Policy Existence with Control Implementation
**Issue:** Believing that having a policy equals control implementation (O1 Policies rated "Implemented" but actual controls in T1-T10 not deployed).

**Assessment:** O1 Policies documents the EXISTENCE of policies. T1-T10, O2-O10 document IMPLEMENTATION of controls specified in policies.

**Gap:** "Paper compliance" - policies written but not followed. Result: Auditor finds policy-practice gap, material non-compliance.

**Remediation:**

- Rate O1 Policies based on policy documentation (policies written, approved, published)
- Rate T1-T10, O2-O10 based on actual control implementation (policies FOLLOWED, controls DEPLOYED)
- Example: ISMS-POL-A.8.24 Cryptography Policy (O1) states "TLS 1.3 shall be used" → Rate O1="Implemented" (policy exists) → T1 Encryption implementation checks if TLS 1.3 actually deployed → If yes, T1="Implemented"; if no, T1="Not Implemented" + gap documented

---

## Pitfall 9: Ignoring Organizational Measures (O1-O10)
**Issue:** Focusing solely on technical controls (T1-T10) while neglecting organizational controls (O1-O10).

**Assessment:** Organizational measures are equally important for GDPR Art. 32 compliance.

**Gap:** Technical controls without organizational support fail. Example: Encryption (T1) deployed but no training (O2) → users store PII in unencrypted file shares.

**Remediation:**

- Give equal attention to O1-O10
- Ensure organizational measures support technical measures
- Example: T2 Access Control requires O2 Training (users must understand least privilege), O6 Accountability (data ownership), O8 Compliance Monitoring (access reviews)

---

## Pitfall 10: Treating Assessment as "Point-in-Time" Activity
**Issue:** Completing assessment once, never updating.

**Assessment:** TOMs are dynamic - controls change, new systems deploy, risks evolve.

**Gap:** Stale assessment provides no value. Result: Auditor finds documented status doesn't match actual state.

**Remediation:**

- Update assessment annually (full review)
- Update assessment quarterly (spot checks: new systems, major changes, remediation progress)
- Update Sheet 8 (Dashboard) monthly (KPI tracking, remediation status)
- Update after major incidents (data breach, audit finding, regulatory inquiry)
- Example: New cloud application deployed in Q2 2026 → Update Sheet 2 (assess TOMs for new application), update Sheet 3/4 (describe how TOMs apply to new application), update Sheet 5 (collect evidence), update Sheet 6 (identify new gaps), update Sheet 7 (remediation for new gaps)

---

# Quality Checklist

## Sheet 1: Instructions & Legend

- [ ] Sheet reviewed and understood by all assessment participants
- [ ] All 20 TOM categories clearly defined
- [ ] Implementation status definitions understood (Implemented/Partially/Planned/Not Implemented)
- [ ] Effectiveness rating definitions understood (Effective/Partially Effective/Ineffective/Not Tested)
- [ ] Risk rating methodology understood (likelihood × impact matrix)

## Sheet 2: TOM Control Inventory

**Completeness:**

- [ ] All 20 TOM rows completed (no blank rows)
- [ ] Column D (Implementation Status) selected for all 20 TOMs
- [ ] Column E (Implementation Date) filled for all Implemented/Partially Implemented TOMs
- [ ] Column F (Description) completed for all 20 TOMs (minimum 3 paragraphs each)
- [ ] Column G (Evidence Reference) populated for all Implemented/Partially Implemented TOMs
- [ ] Column H (Effectiveness Rating) selected for all Implemented/Partially Implemented TOMs
- [ ] Column I (Last Test Date) filled for all Effective/Partially Effective/Ineffective TOMs
- [ ] Column J (Gaps Identified) completed where gaps exist
- [ ] Column K (Risk Level) assessed for all gaps
- [ ] Column L (Remediation Plan) outlined for all gaps requiring remediation
- [ ] Column M (Remediation Owner) assigned for all gaps requiring remediation
- [ ] Column N (Target Completion Date) set for all gaps requiring remediation

**Quality:**

- [ ] Implementation status decisions justified with coverage percentages
- [ ] Descriptions are specific (vendor names, versions, configurations) not generic
- [ ] Descriptions quantify coverage (numerator/denominator)
- [ ] Descriptions identify responsible teams/owners
- [ ] Evidence references valid (evidence actually exists in Sheet 5)
- [ ] Effectiveness ratings based on actual testing, not assumptions
- [ ] Test dates within expected frequency (quarterly for tech, annually for org)
- [ ] Gaps described in detail (what's missing, impact, affected systems)
- [ ] Risk assessments justified (likelihood and impact rationale documented)
- [ ] Remediation plans actionable (phases, timelines, budgets)

## Sheet 3: Technical Measures Deep-Dive

**Completeness:**

- [ ] All 10 technical measures (T1-T10) documented
- [ ] "Technologies Deployed" completed for all T1-T10
- [ ] "Configuration Details" completed for all T1-T10
- [ ] "Coverage Percentage" calculated for all T1-T10
- [ ] "Exceptions" documented where applicable
- [ ] "Integration Notes" completed for all T1-T10

**Quality:**

- [ ] Technologies: Specific product names, vendors, versions listed
- [ ] Configuration: Technical parameters, settings, thresholds documented
- [ ] Coverage: Percentages calculated with numerators/denominators
- [ ] Exceptions: Justified (business reason, compensating controls, remediation plan)
- [ ] Integration: Dependencies and data flows clearly described

## Sheet 4: Organizational Measures Deep-Dive

**Completeness:**

- [ ] All 10 organizational measures (O1-O10) documented
- [ ] "Policies in Place" completed for all O1-O10
- [ ] "Training/Communication" completed for all O1-O10
- [ ] "Governance Structure" completed for all O1-O10
- [ ] "Monitoring Method" completed for all O1-O10
- [ ] "Improvement Process" completed for all O1-O10

**Quality:**

- [ ] Policies: Specific policy names, versions, approval dates listed
- [ ] Training: Completion rates, quiz scores, certification details documented
- [ ] Governance: Organizational chart, reporting lines, meeting frequency clear
- [ ] Monitoring: KPIs defined, measurement methods described
- [ ] Improvement: Continuous improvement process documented

## Sheet 5: Evidence Repository

**Completeness:**

- [ ] Minimum 5 evidence items per TOM (total 100+ evidence items for 20 TOMs)
- [ ] Column A (Evidence ID) auto-generated for all entries
- [ ] Column B (TOM ID) linked to Sheet 2 for all entries
- [ ] Column C (Evidence Type) selected for all entries
- [ ] Column D (Description) completed for all entries
- [ ] Column E (File Location) documented for all entries
- [ ] Column F (Evidence Date) filled for all entries
- [ ] Column G (Verification Status) selected for all entries
- [ ] Column H (Verified By) filled for all "Verified" entries
- [ ] Column I (Notes) completed where additional context needed

**Quality:**

- [ ] Evidence variety (mix of configs, policies, audits, tests for each TOM)
- [ ] Evidence currency (technical evidence <3 months, organizational evidence <12 months)
- [ ] Evidence accessibility (file paths valid, files retrievable)
- [ ] Evidence adequacy verified by DPO/CISO/Internal Auditor
- [ ] Verification rate ≥95% (minimal "Pending Verification" entries)
- [ ] Expired evidence replaced or refreshed

## Sheet 6: Gap Analysis & Risk Assessment

**Completeness:**

- [ ] All gaps from Sheet 2 Column J have corresponding entries in Sheet 6
- [ ] Column A (Gap ID) formatted correctly (GAP-[TOM]-###)
- [ ] Column B (TOM ID) linked to Sheet 2
- [ ] Column C (Gap Description) completed for all gaps
- [ ] Column D (Likelihood) assessed for all gaps
- [ ] Column E (Impact) assessed for all gaps
- [ ] Column F (Overall Risk) auto-calculated for all gaps
- [ ] Column G (Risk Score) auto-calculated for all gaps
- [ ] Column H (Remediation Priority) auto-calculated for all gaps
- [ ] Column I (Residual Risk) documented for remediation-planned gaps
- [ ] Column J (Acceptance Justification) completed for risk-accepted gaps

**Quality:**

- [ ] Gap descriptions detailed (what's missing, impact, affected systems)
- [ ] Likelihood assessments justified (threat analysis, attack surface, compensating controls)
- [ ] Impact assessments justified (PII volume, sensitivity, regulatory consequences)
- [ ] Risk calculations verified (formula correct, manual check of 10% sample)
- [ ] Residual risk realistic (post-remediation risk should be LOW for most gaps)
- [ ] Risk acceptances properly justified and approved by management

## Sheet 7: Remediation Action Plan

**Completeness:**

- [ ] All Medium/High/Critical gaps have remediation actions in Sheet 7
- [ ] Low-risk gaps either remediated or risk-accepted in Sheet 6
- [ ] Column A (Action ID) formatted correctly (ACT-[TOM]-###)
- [ ] Column B (TOM ID) linked to Sheet 2
- [ ] Column C (Gap Description) copied from Sheet 6
- [ ] Column D (Proposed Solution) detailed for all actions
- [ ] Column E (Owner) assigned for all actions
- [ ] Column F (Start Date) set for all actions
- [ ] Column G (Target Date) set for all actions (risk-based prioritization)
- [ ] Column H (Status) selected for all actions
- [ ] Column I (% Complete) estimated for all In Progress actions
- [ ] Column J (Completion Date) filled for all Complete actions

**Quality:**

- [ ] Proposed solutions detailed (phases, steps, deliverables)
- [ ] Solutions include timeline estimates (realistic, phased approach)
- [ ] Solutions include budget estimates (licensing, consulting, staffing)
- [ ] Solutions address root cause (not just symptoms)
- [ ] Ownership clear (full name, role, contact info)
- [ ] Target dates aligned with risk priority (Critical: 30-60 days, High: 90-180 days, Medium: 6-12 months)
- [ ] Status updates current (monthly updates minimum)
- [ ] Completion dates validated (evidence updated in Sheet 5)

## Sheet 8: Compliance Dashboard

**Verification:**

- [ ] All formulas calculate correctly (manual spot-check 10% of formulas)
- [ ] Implementation Rate ≥90% (target met or gap explanation documented)
- [ ] Effectiveness Rate ≥95% (target met or gap explanation documented)
- [ ] Critical Gaps ≤1 (ideally 0)
- [ ] High Risk Gaps ≤3 (ideally 0)
- [ ] Remediation Progress ≥80% (most actions complete)
- [ ] GDPR Art. 32 Compliance Score ≥80% (good compliance)
- [ ] Evidence Verification Rate ≥95% (minimal pending verification)
- [ ] Dashboard charts inserted (Pie chart: TOM status, Bar charts: Gap risk, Remediation progress)

**Conditional Formatting:**

- [ ] Implementation Rate: Green if ≥90%, Yellow if 80-89%, Red if <80%
- [ ] Effectiveness Rate: Green if ≥95%, Yellow if 85-94%, Red if <85%
- [ ] GDPR Compliance Score: Green if ≥90%, Light green if 80-89%, Yellow if 70-79%, Orange if 60-69%, Red if <60%
- [ ] Gap counts: Critical Gaps in red bold, High Gaps in orange

## General Quality Checks

**Consistency:**

- [ ] Status values consistent across sheets (Sheet 2 Column D matches Sheet 7 Column H after remediation complete)
- [ ] Evidence references valid (Sheet 2 Column G matches Sheet 5 Column A)
- [ ] Gap IDs consistent (Sheet 2 Column J gaps match Sheet 6 entries)
- [ ] Action IDs consistent (Sheet 6 gaps match Sheet 7 actions)
- [ ] Dates logical (Implementation Date < Last Test Date < Evidence Date < Current Date)

**Completeness:**

- [ ] No blank required fields (all mandatory columns completed)
- [ ] No "TODO" or placeholder text
- [ ] All 20 TOMs documented
- [ ] All gaps risk-assessed
- [ ] All Medium/High/Critical gaps remediated or risk-accepted

**Evidence:**

- [ ] Minimum 100 evidence items (5 per TOM)
- [ ] Evidence covers all Implemented/Partially Implemented TOMs
- [ ] Evidence types varied (not just policies or screenshots)
- [ ] Evidence current (technical: <3 months, organizational: <12 months)
- [ ] Evidence verified (≥95% verification rate)

**Realism:**

- [ ] Coverage percentages realistic (not inflated)
- [ ] Risk assessments honest (not downplayed)
- [ ] Remediation timelines achievable (not overly optimistic)
- [ ] Budget estimates realistic (not under-estimated)
- [ ] Ownership assignments appropriate (owners have authority/capacity)

**Auditability:**

- [ ] Descriptions specific and verifiable
- [ ] Evidence retrievable (file paths valid)
- [ ] Justifications clear and documented
- [ ] Decisions traceable (who, what, when, why)
- [ ] Document version-controlled and date-stamped

---

# Review & Approval

## Internal Review Process

**Step 1: Self-Review (Assessment Owner)**

- **Who:** Assessment owner (typically Security Architect or DPO)
- **When:** Before submitting for review
- **Duration:** 2-4 hours
- **Checklist:**
  - [ ] Quality Checklist (Section 7) completed
  - [ ] All 20 TOMs documented
  - [ ] All gaps identified and risk-assessed
  - [ ] Evidence adequate (100+ items, verified)
  - [ ] Dashboard metrics calculated
  - [ ] No obvious errors or omissions

**Step 2: Peer Review (Security Team)**

- **Who:** Security Architect, Security Engineer, SOC Manager (peers)
- **When:** After self-review
- **Duration:** 4-6 hours
- **Focus:**
  - Technical accuracy (configurations, coverage percentages)
  - Evidence adequacy (screenshots readable, configs current)
  - Gap identification (any missed gaps?)
  - Risk assessments (likelihood and impact reasonable?)

**Step 3: DPO Review (Privacy Perspective)**

- **Who:** Data Protection Officer
- **When:** After peer review
- **Duration:** 6-8 hours
- **Focus:**
  - GDPR/FADP compliance (Art. 32 TOMs adequately addressed?)
  - Organizational measures (O1-O10 sufficient?)
  - Evidence sufficiency (audit-ready?)
  - Gap prioritization (Critical/High risks addressed?)
  - Regulatory risk (any material non-compliance?)

**Step 4: CISO Review (Security Posture)**

- **Who:** Chief Information Security Officer
- **When:** After DPO review
- **Duration:** 4-6 hours
- **Focus:**
  - Technical controls (T1-T10 effective?)
  - Control effectiveness (testing adequate?)
  - Remediation plans (realistic timelines, budgets?)
  - Resource allocation (owners assigned appropriately?)
  - Executive summary (Dashboard metrics acceptable?)

**Step 5: Internal Audit Verification (Independent Check)**

- **Who:** Internal Audit team
- **When:** After CISO review (before final approval)
- **Duration:** 8-12 hours
- **Focus:**
  - Evidence validation (sample 20% of evidence items, verify adequacy)
  - Control testing (sample 10% of controls, re-test effectiveness)
  - Consistency checks (status values match across sheets?)
  - Formula validation (spot-check calculations)
  - Audit readiness (will external auditors accept this?)

## Approval Workflow

**Approval Level 1: CISO (Security Approval)**

- **Who:** Chief Information Security Officer
- **Approval criteria:**
  - [ ] Technical controls (T1-T10) adequately documented
  - [ ] Control effectiveness validated
  - [ ] Remediation plans realistic and resourced
  - [ ] Critical/High risk gaps addressed or remediation in flight
  - [ ] Dashboard metrics acceptable (Implementation Rate ≥80%, Effectiveness Rate ≥85%)

**Approval Level 2: DPO (Privacy Approval)**

- **Who:** Data Protection Officer
- **Approval criteria:**
  - [ ] GDPR/FADP compliance requirements met
  - [ ] Organizational measures (O1-O10) sufficient
  - [ ] Evidence audit-ready
  - [ ] Privacy risks identified and remediated/accepted
  - [ ] GDPR Art. 32 Compliance Score ≥80%

**Approval Level 3: Compliance Officer (Regulatory Approval)**

- **Who:** Compliance Officer (if separate from DPO)
- **Approval criteria:**
  - [ ] Regulatory alignment (GDPR, FADP, ISO 27001)
  - [ ] Audit readiness (suitable for ISO 27001, SOC 2, GDPR audits)
  - [ ] Documentation completeness
  - [ ] Risk acceptance properly documented and justified

**Approval Level 4: Executive Management (Budget/Resource Approval)**

- **Who:** CEO or CFO (for remediation budget >$100K)
- **Approval criteria:**
  - [ ] Remediation budget justified (cost-benefit analysis)
  - [ ] Resource allocation reasonable (staffing, external consultants)
  - [ ] Timeline achievable
  - [ ] Business impact acceptable (downtime, user impact)

**Approval Level 5: Audit Committee / Board (Governance Oversight)**

- **Who:** Audit Committee (Board of Directors subcommittee)
- **When:** Annual privacy report to Board (includes TOM assessment summary)
- **Approval criteria:**
  - [ ] Privacy risk landscape understood
  - [ ] Material privacy risks identified and addressed
  - [ ] Compliance status acceptable
  - [ ] Budget allocation approved
  - [ ] Regulatory exposure acceptable

## Sign-Off Documentation

**Final approval documented in workbook:**

- Sheet 2 (or dedicated Approval sheet): Signature section with:
  - [ ] Assessment completed by: [Name, Role, Date, Signature]
  - [ ] Reviewed by CISO: [Name, Date, Signature]
  - [ ] Reviewed by DPO: [Name, Date, Signature]
  - [ ] Approved by Compliance Officer: [Name, Date, Signature]
  - [ ] Budget approved by CFO: [Name, Date, Signature] (if >$100K)
  - [ ] Presented to Audit Committee: [Date, Signature]

**Next review scheduled:**

- [ ] Next annual review: [Date] (12 months from completion)
- [ ] Next quarterly update: [Date] (3 months from completion)
- [ ] Remediation progress review: [Date] (monthly during active remediation)

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
