# ISMS-IMP-A.5.34.4 - Technical and Organizational Measures (TOMs) Assessment
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.34.4 |
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

# PART 1: USER COMPLETION GUIDE

**Audience:** CISO, DPO, Security Architects, Compliance Officers

---

## 1. Assessment Overview

### 1.1 What This Assessment Measures

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

### 1.2 Why This Matters

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

### 1.3 What You'll Document

Upon completion, you will have:

1. ✅ **TOM Implementation Status** - Complete inventory of all 20 TOMs with implementation ratings (Implemented/Partially Implemented/Planned/Not Implemented)
2. ✅ **Technical Measure Details** - Deep-dive documentation of T1-T10: technologies deployed, configurations, coverage percentages, exceptions
3. ✅ **Organizational Measure Details** - Deep-dive documentation of O1-O10: policies, training programs, governance structures, monitoring methods
4. ✅ **Evidence Repository** - Centralized documentation of all evidence proving TOM effectiveness (policies, configs, audit reports, test results)
5. ✅ **Gap Analysis** - Identification of all TOM gaps with risk ratings (Critical/High/Medium/Low) using likelihood × impact matrix
6. ✅ **Remediation Roadmap** - Prioritized action plans for closing gaps with owners, timelines, budgets, and progress tracking
7. ✅ **Compliance Dashboard** - Executive metrics showing implementation rate, effectiveness rate, gap distribution, and GDPR Art. 32 compliance score
8. ✅ **Audit-Ready Documentation** - Complete assessment workbook suitable for ISO 27001, GDPR, FADP audits and supervisory authority inspections

### 1.4 How This Relates to Other A.5.34 Assessments

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

## 2. Prerequisites

### 2.1 Information You'll Need

Before starting this assessment, gather:

#### 1. PII Inventory & Classification (from A.5.34.1)
- List of all PII categories processed
- Data classification (Restricted/Confidential/Internal/Public)
- PII locations (systems, databases, file shares)
- Data flow maps

#### 2. Security Architecture Documentation
- Network architecture diagrams
- System architecture diagrams
- Data flow diagrams
- Integration maps

#### 3. Technical Security Controls Documentation
- Encryption configurations (TLS, at-rest encryption)
- Access control configurations (AD groups, IAM roles, RBAC)
- Security monitoring configurations (SIEM rules, alerts)
- Network security configurations (firewall rules, segmentation)
- Application security controls (WAF, input validation)
- Endpoint security deployments (EDR, anti-malware)
- Backup & DR configurations
- Physical security controls

#### 4. Organizational Security Documentation
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

#### 5. Evidence & Proof of Implementation
- Configuration screenshots
- Audit logs showing control operation
- Test results (penetration tests, vulnerability scans)
- Training completion reports
- Incident response exercise reports
- Vendor due diligence reports
- ISO 27001 audit reports
- Supervisory authority correspondence (if any)

### 2.2 Access Required

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

### 2.3 Who Should Complete This Assessment

#### Primary Stakeholders

1. **Chief Information Security Officer (CISO)** - Overall responsibility, strategic decisions, gap prioritization, executive reporting
2. **Data Protection Officer (DPO)** - Regulatory interpretation, GDPR/FADP compliance verification, risk assessment
3. **Security Architect** - Technical measure documentation (T1-T10), architecture decisions, control effectiveness assessment
4. **IT Operations Manager** - Operational measure documentation, implementation details, evidence collection
5. **Compliance Officer** - Organizational measure documentation (O1-O10), policy verification, audit readiness
6. **Internal Auditor** - Independent verification, evidence validation, gap identification

#### Required Skills

- **Privacy Regulation Knowledge:** Understanding of GDPR Articles 5, 25, 32-36; Swiss FADP Articles 6-8
- **Security Controls Expertise:** Familiarity with NIST CSF, ISO 27001 Annex A, CIS Controls
- **Risk Assessment:** Ability to assess likelihood and impact of security risks
- **Technical Security:** Understanding of encryption, access control, network security, application security
- **Compliance Auditing:** Experience with control testing and evidence evaluation
- **Documentation Skills:** Ability to write clear, audit-ready documentation

#### Time Commitment

- **Initial assessment:** 40-60 hours total across all stakeholders
  - CISO/DPO: 8-12 hours (strategic decisions, review)
  - Security Architect: 16-24 hours (technical measures T1-T10)
  - IT Ops Manager: 12-16 hours (implementation details, evidence)
  - Compliance Officer: 12-16 hours (organizational measures O1-O10)
  - Internal Auditor: 8-12 hours (verification, gap analysis)

- **Annual updates:** 16-24 hours (review changes, update evidence, remediation progress)
- **Quarterly reviews:** 4-8 hours (spot checks, dashboard updates, remediation tracking)

### 2.4 Expected Outputs

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

## 3. Assessment Workflow

### 3.1 Overview of Assessment Process

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

### 3.2 Step-by-Step Completion Sequence

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

### 3.3 Phase-by-Phase Dependencies

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

## 4. Sheet-by-Sheet Completion Guidance

### 4.1 Sheet 1: Instructions & Legend

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

### 4.2 Sheet 2: TOM Control Inventory

**Purpose:** Document implementation status of all 20 TOM categories

**Pre-Populated Content:**
- **Rows 2-11:** T1-T10 (Technical Measures) - pre-filled in Columns A-B
- **Rows 12-21:** O1-O10 (Organizational Measures) - pre-filled in Columns A-B
- **Columns A-B:** TOM ID and TOM Category (locked - do not edit)

**For EACH TOM (Rows 2-21), Complete Columns C-N:**

#### Column C - TOM Type
**Pre-filled:** Technical or Organizational (locked)

#### Column D - Implementation Status
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

#### Column E - Implementation Date
**Format:** YYYY-MM-DD
**Guidance:** When was control first deployed?
- If phased deployment, use date of initial rollout
- If enhanced over time, use original deployment date
- If not yet implemented, leave blank

**Examples:**
- T1 Encryption: 2020-03-15 (when first TLS deployment completed)
- O2 Training: 2021-06-01 (when first annual training launched)
- O4 Vendor Mgmt: [blank] (not implemented)

#### Column F - Description of Implementation
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
WHAT: Role-Based Access Control (RBAC) implemented across all PII-handling systems using Azure Active Directory (Azure AD) as centralized identity provider (IdP). 18 security groups defined based on job functions: Customer_Service_Agent, Data_Analyst, System_Administrator, HR_Specialist, Finance_Team, Marketing_User, Legal_Team, Executive_Management, IT_Support, Network_Admin, Database_Admin, Security_Team, Audit_Team, Contractor_Limited, Temporary_Worker, External_Partner, API_Service_Account, System_Service_Account. Multi-Factor Authentication (MFA) mandatory for all human users via Microsoft Authenticator push notification or FIDO2 security key. Privileged Access Management (PAM) deployed via CyberArk for administrative accounts.

HOW: Users authenticate via Azure AD single sign-on (SSO) with MFA as second factor. Access requests submitted via ServiceNow ticketing system with automated routing to manager for approval. Just-in-Time (JIT) access granted for temporary elevated privileges (valid 4-8 hours, auto-expires). Privileged sessions recorded via CyberArk session monitoring. Password policy enforced: 14 characters minimum, complexity enabled, 90-day expiration, 24-password history. Conditional Access policies enforce MFA from untrusted networks, block legacy authentication protocols (POP3, IMAP, SMTP AUTH).

WHERE: Azure AD integrated with: Salesforce (CRM), Microsoft 365 (email/SharePoint), AWS (cloud infrastructure via SAML federation), Azure SQL Database, SAP (ERP), HubSpot (marketing automation), Zoom (video conferencing), GitHub (source code), Confluence/Jira (documentation), VPN (Cisco AnyConnect with RADIUS integration). On-premises Active Directory synchronized via Azure AD Connect. 95% of applications integrated with Azure AD (95/100 apps). 5 legacy applications (AS/400 mainframe, 2 custom .NET apps, vendor portal, building access system) use local authentication (planned migration to Azure AD in 2027).

WHO: Identity and Access Management (IAM) team (3 FTEs) manages Azure AD, group membership, access reviews. Security Operations Center (SOC) monitors access logs via Splunk SIEM. IT Service Desk handles access requests. Information Security (InfoSec) team defines RBAC roles and conducts quarterly access reviews.

COVERAGE: 95/100 applications integrated with Azure AD (95%). 1,250 users enabled for MFA (100% human users). 14 privileged accounts managed via CyberArk (100% of privileged accounts). Access reviews conducted quarterly covering 18 security groups (100% review coverage). 5 legacy applications represent gap (5% of applications, contain minimal PII, scheduled for retirement or SSO integration by Q2 2027).
```

**Example (O3 - Incident Response & Breach Notification):**
```
WHAT: Incident Response Plan (IRP-2024-v2.1) approved by CISO 2024-08-15, defines 6-phase incident response process: (1) Preparation, (2) Detection & Analysis, (3) Containment, (4) Eradication, (5) Recovery, (6) Post-Incident Review. Breach notification procedure (BNP-2024-v1.2) approved by DPO 2024-09-01, implements GDPR Article 33 (notification to supervisory authority) and Article 34 (communication to data subjects) requirements. Incident response team: 12 members (CISO, DPO, IT Director, Security Architect, SOC Manager, Network Engineer, Database Admin, Legal Counsel, HR Director, Communications Director, External Counsel on-call, Forensics Consultant on-call).

HOW: Security incidents detected via: (1) SIEM alerts (Splunk Enterprise Security), (2) EDR alerts (CrowdStrike Falcon), (3) User reports (security@company.com), (4) Vulnerability scan findings (Qualys), (5) Third-party notifications (vendors, partners). Severity classification: P1-Critical (active breach, data exfiltration), P2-High (contained breach, suspected data access), P3-Medium (vulnerability exploitation attempt), P4-Low (policy violation, minor anomaly). Breach assessment criteria: (1) Confidentiality breach? (2) PII involved? (3) Risk to data subject rights? (4) GDPR Article 33 threshold met? Notification timeline: 72 hours from breach awareness to supervisory authority (Swiss FDPIC or EU DPA), without undue delay to data subjects (if high risk). Incident communication: Secure incident channel (Microsoft Teams private channel), escalation matrix, stakeholder notification templates, PR crisis communication plan.

WHERE: Incident response managed via: ServiceNow Security Incident Response (SIRT) module for case tracking, Splunk for log analysis, CyberArk for evidence collection (privileged session recordings), Azure Sentinel for threat intelligence correlation, SharePoint (secure library) for evidence storage, External forensics provider (CyberForensics Inc.) on retainer for P1/P2 incidents. Breach notification templates stored in DPO SharePoint library: FDPIC notification template (German/French), EDPS notification template (English), Data subject notification letter template (6 languages), Media statement template, Internal communication template.

WHO: Security Operations Center (SOC) performs initial triage (24/7). Incident Commander (IC) appointed based on severity: P1/P2 = CISO, P3 = Security Architect, P4 = SOC Manager. DPO assesses breach notification requirements and drafts notifications. Legal Counsel reviews external communications. Communications Director handles media relations. Forensics Consultant (CyberForensics Inc.) performs deep forensics for P1/P2 incidents.

COVERAGE: Incident response process operational 24/7/365. 12/12 incident response team members trained (2024-11-15 tabletop exercise: ransomware scenario). 100% of security incidents logged in ServiceNow SIRT (Q4 2025: 142 incidents, P1=2, P2=5, P3=48, P4=87). 2 P1 breaches in 2025: (1) Phishing compromise of 1 account (72-hour notification met, 0 PII exposed, no GDPR notification required), (2) Misconfigured S3 bucket (public exposure 4 days, 12 records exposed, FDPIC notified within 72 hours, affected data subjects notified within 7 days, incident closed with no enforcement action). Breach notification templates tested and pre-approved by Legal/DPO. Post-incident reviews conducted for 100% of P1/P2 incidents.
```

#### Column G - Evidence Reference
**Format:** EV-[TOM ID]-### (e.g., EV-T1-001, EV-T2-003)
**Guidance:** Link to Sheet 5 (Evidence Repository) entries
**Examples:**
- T1 Encryption: EV-T1-001, EV-T1-002, EV-T1-003 (TLS configs, TDE configs, FDE reports)
- O2 Training: EV-O2-001, EV-O2-002 (training completion report, quiz results)

#### Column H - Effectiveness Rating
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

#### Column I - Last Test Date
**Format:** YYYY-MM-DD
**Guidance:** When was control effectiveness last validated?
**Testing Frequency Standards:**
- **Technical controls (T1-T10):** Quarterly or after major changes
- **Organizational controls (O1-O10):** Annually or after major changes
- **Critical controls (T1, T2, T5, O3):** Quarterly minimum

**Examples:**
- T1 Encryption: 2025-12-15 (TLS test via SSL Labs)
- O2 Training: 2025-11-01 (training completion report generated)

#### Column J - Gaps Identified
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

#### Column K - Risk Level
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

#### Column L - Remediation Plan
**Format:** 1-3 paragraphs describing proposed solution
**Content:** HOW will gap be closed? WHEN? WHO owns it? WHAT resources needed?

**Examples:**
```
T1 - Encryption Remediation Plan:
Phase 1 (Q1 2026): Upgrade 3 highest-priority databases (customer contact databases) to Oracle 19c, enable TDE. Owner: Database Admin team. Budget: $45,000 (licensing + migration). Phase 2 (Q2 2026): Upgrade 2 financial transaction databases to Oracle 19c, enable TDE. Owner: Database Admin team. Budget: $30,000. Phase 3 (Q3 2026): Upgrade HR database to Oracle 19c, enable TDE. Owner: Database Admin team. Budget: $15,000. Total budget: $90,000. Alternative considered: Migrate to Azure SQL Database (cloud) with automatic TDE, estimated cost $120,000, longer timeline (12 months), decided to upgrade in-place for faster resolution. File share encryption (lower priority): Implement Azure Information Protection (AIP) automatic encryption for Internal-classified shares. Timeline: Q4 2026. Owner: IT Infrastructure team. Budget: Included in existing M365 E5 licensing. Email encryption (lowest priority): Enforce mandatory TLS via Exchange transport rule (reject non-TLS external email). Timeline: Q4 2026. Owner: Email Admin team. Budget: $0 (configuration change only). Requires business approval due to potential delivery failures.

O4 - Vendor Management Remediation Plan:
Phase 1 (Q1 2026): Implement vendor privacy risk assessment process. Tasks: (1) Create vendor risk assessment questionnaire (DPO + Legal), (2) Integrate questionnaire into procurement workflow (Procurement + IT), (3) Define risk scoring methodology (DPO + CISO), (4) Train procurement team (DPO). Owner: DPO. Budget: $20,000 (consulting support for questionnaire development). Phase 2 (Q2 2026): Backfill DPAs with existing processors. Tasks: (1) Send DPA template to all 14 processors lacking DPAs, (2) Negotiate and execute DPAs, (3) Centralize DPA storage in SharePoint library, (4) Track DPA expiration dates. Owner: Legal Counsel. Budget: $50,000 (legal time, contract negotiation). Phase 3 (Q3 2026): Conduct initial vendor audits. Tasks: (1) Request SOC 2 Type II reports from top 10 processors, (2) Review reports and document findings, (3) Conduct on-site audits of 3 highest-risk processors, (4) Document audit results and remediation requirements. Owner: Internal Audit team. Budget: $30,000 (external audit support). Phase 4 (Q4 2026): Create comprehensive processor inventory. Tasks: (1) Survey all departments for processor lists, (2) Consolidate into master inventory, (3) Classify processors by risk level, (4) Map processors to processing activities in ROPA, (5) Identify sub-processors. Owner: Compliance Officer. Budget: $15,000 (data classification consulting). Total budget: $115,000. Ongoing annual cost: $25,000 (annual vendor risk assessments, SOC 2 report reviews, periodic audits).
```

#### Column M - Remediation Owner
**Format:** Full name and role
**Examples:**
- "Jane Smith, Database Administrator"
- "John Doe, Data Protection Officer"  
- "Alice Johnson, CISO"

#### Column N - Target Completion Date
**Format:** YYYY-MM-DD
**Guidance:** When should gap be closed?
**Prioritization:**
- **Critical risk gaps:** 30-60 days
- **High risk gaps:** 90-180 days
- **Medium risk gaps:** 6-12 months
- **Low risk gaps:** 12-24 months

---

### 4.3 Sheet 3: Technical Measures Deep-Dive

**Purpose:** Detailed technical documentation of T1-T10 implementation

**Structure:** One section per TOM (T1-T10), each section contains 5 fields

**For EACH Technical Measure (T1-T10), Document:**

#### Technologies Deployed
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

#### Configuration Details
**Length:** 2-3 paragraphs  
**Content:** Technical configuration specifics, settings, parameters
**Example (T2 - Access Control):**
```
CONFIGURATION DETAILS:

AZURE AD CONFIGURATION:
- Tenant ID: 12345678-90ab-cdef-1234-567890abcdef
- Licenses: Azure AD Premium P2 (1,250 licenses), Microsoft 365 E5 (1,250 licenses)
- Custom domain: sso.company.com (federated with Azure AD)
- Password policy: 14-character minimum, complexity enabled (uppercase, lowercase, numbers, symbols), 90-day expiration, 24-password history, account lockout after 5 failed attempts (15-minute lockout duration)
- MFA enforcement: Enabled for all users, registration required within 14 days of account creation, authentication methods: Microsoft Authenticator (primary), FIDO2 security key (backup), SMS (emergency only)
- Conditional Access policies: 12 policies configured
  → Policy 1: Require MFA for all cloud apps (All users, All cloud apps, Grant: Require MFA)
  → Policy 2: Block legacy authentication (All users, Exchange ActiveSync/Other clients, Block)
  → Policy 3: Require compliant device for Confidential data (All users, Confidential-classified apps, Grant: Require device compliance)
  → Policy 4: Require hybrid Azure AD joined device for on-prem apps (All users, On-premises apps, Grant: Require hybrid Azure AD joined device)
  → Policy 5: Block access from non-corporate networks to admin portals (Admin users, Azure portal, Grant: Require location: Corporate Network)
  → Policy 6-12: (additional policies for guest access, service accounts, external collaboration, risk-based access, app protection policies)

RBAC CONFIGURATION:
- 18 security groups: Customer_Service_Agent (250 members), Data_Analyst (45 members), System_Administrator (12 members), HR_Specialist (8 members), Finance_Team (25 members), Marketing_User (60 members), Legal_Team (5 members), Executive_Management (8 members), IT_Support (18 members), Network_Admin (5 members), Database_Admin (3 members), Security_Team (6 members), Audit_Team (4 members), Contractor_Limited (50 members), Temporary_Worker (20 members), External_Partner (15 members), API_Service_Account (25 service accounts), System_Service_Account (50 service accounts)
- Group membership: Managed via HR system integration (Workday), automatic provisioning/deprovisioning, manual approval for privileged groups (System_Administrator, Database_Admin, Network_Admin)
- Application permissions: Salesforce (12 permission sets mapped to 6 security groups), AWS (8 IAM roles mapped via SAML federation), Azure (15 Azure RBAC roles via Azure AD groups), SAP (6 SAP roles mapped to 4 security groups)

PAM (CyberArk) CONFIGURATION:
- CyberArk version: Privileged Access Security 13.2
- Vaults: Production Vault (12 privileged accounts), Non-Production Vault (8 privileged accounts)
- Platforms: Windows Domain Admin, Linux root, SQL Server SA, Oracle SYS, AWS IAM admin, Azure Global Admin
- Access workflow: Self-service request via CyberArk web portal, JIT access (4-8 hour sessions), password rotation after each session, session recording (100% of privileged sessions), dual control for production database access (2-person approval)
```

#### Coverage Percentage
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

#### Exceptions
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

#### Integration Notes
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

### 4.4 Sheet 4: Organizational Measures Deep-Dive

**Purpose:** Detailed organizational documentation of O1-O10 implementation

**Structure:** One section per TOM (O1-O10), each section contains 5 fields

**For EACH Organizational Measure (O1-O10), Document:**

#### Policies in Place
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

#### Training/Communication
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

#### Governance Structure
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

#### Monitoring Method
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

#### Improvement Process
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

### 4.5 Sheet 5: Evidence Repository

**Purpose:** Centralized storage of all evidence proving TOM implementation and effectiveness

**Complete Evidence Repository for ALL 20 TOMs (T1-T10, O1-O10)**

**For EACH TOM, Store Multiple Evidence Items:**

#### Column A - Evidence ID
**Format:** EV-[TOM ID]-### (auto-generated)
**Examples:**
- EV-T1-001 (first evidence item for T1 Encryption)
- EV-T1-002 (second evidence item for T1 Encryption)
- EV-O2-001 (first evidence item for O2 Training)

#### Column B - TOM ID
**Format:** T1, T2, ..., T10, O1, O2, ..., O10
**Purpose:** Links evidence to specific TOM in Sheet 2

#### Column C - Evidence Type
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

#### Column D - Description
**Length:** 1-3 sentences
**Content:** Brief summary of evidence
**Examples:**
```
EV-T1-001: TLS 1.3 configuration screenshot from nginx web server (prod-web-01), showing enforced TLS 1.3, cipher suite TLS_AES_256_GCM_SHA384, HSTS enabled (max-age=31536000), captured 2025-12-15.

EV-O2-001: 2025 Annual Privacy Training completion report from KnowBe4 platform, showing 1,230/1,250 employees completed (98.4%), average quiz score 88%, average time spent 65 minutes, report generated 2026-01-05.

EV-T2-005: Azure AD Conditional Access policy configuration screenshot, showing Policy CA002 "Block Legacy Authentication" enabled for all users, blocking Exchange ActiveSync and Other clients, captured 2025-12-10.

EV-O4-003: Salesforce Data Processing Agreement (DPA) v3.1 executed 2023-06-15, contains GDPR Article 28 mandatory clauses, sub-processor list attached (Annex A), stored in SharePoint /Legal/Contracts/Vendors/Salesforce/.
```

#### Column E - File Location / System
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

#### Column F - Evidence Date
**Format:** YYYY-MM-DD
**Content:** When was evidence created or captured
**Examples:**
- Configuration screenshot: Date screenshot was taken
- Audit report: Date audit was completed / report issued
- Training report: Date report was generated
- Test results: Date test was conducted

#### Column G - Verification Status
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

EV-T2-008 (Azure AD access review report from 2024-06-01): EXPIRED ⏳ (report >6 months old, quarterly access review required, new report pending)

EV-O4-007 (Vendor risk assessment for new processor XYZ Corp): PENDING VERIFICATION ⏳ (assessment completed 2025-12-20, awaiting DPO review)

EV-T7-003 (Application penetration test report from external consultant): INVALID ❌ (report incomplete, missing risk ratings and remediation recommendations, consultant re-engagement required)
```

#### Column H - Verified By
**Format:** Full name and role of verifier
**Examples:**
- "Jane Doe, Data Protection Officer"
- "John Smith, Chief Information Security Officer"
- "Alice Johnson, Security Architect"
- "Bob Williams, Internal Audit Manager"

#### Column I - Notes
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

### 4.6 Sheet 6: Gap Analysis & Risk Assessment

**Purpose:** Document all identified gaps with risk ratings

**For EACH Gap Identified (from Sheet 2 Column J), Complete:**

#### Column A - Gap ID
**Format:** GAP-[TOM ID]-### (e.g., GAP-T1-001, GAP-O4-001)

#### Column B - TOM ID
**Format:** Link to TOM in Sheet 2 (e.g., T1, O4)

#### Column C - Gap Description
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

#### Column D - Likelihood
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

#### Column E - Impact
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

#### Column F - Overall Risk
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

#### Column G - Risk Score
**Formula:** `=IF(F2="Critical", 4, IF(F2="High", 3, IF(F2="Medium", 2, IF(F2="Low", 1, 0))))`

**Scoring:**
- Critical = 4
- High = 3
- Medium = 2
- Low = 1

**Purpose:** Enables sorting and prioritization (sort by risk score descending to prioritize remediation)

#### Column H - Remediation Priority
**Formula:** `=IF(G2=4, "URGENT (30 days)", IF(G2=3, "HIGH (90 days)", IF(G2=2, "MEDIUM (6 months)", "LOW (12 months)")))`

**Priorities:**
- Critical risk → URGENT (30-60 days)
- High risk → HIGH (90-180 days)
- Medium risk → MEDIUM (6-12 months)
- Low risk → LOW (12-24 months)

#### Column I - Residual Risk (Post-Remediation)
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

#### Column J - Acceptance Justification
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

### 4.7 Sheet 7: Remediation Action Plan

**Purpose:** Track remediation actions for closing gaps

**For EACH Gap Requiring Remediation (from Sheet 6), Complete:**

#### Column A - Action ID
**Format:** ACT-[TOM ID]-### (e.g., ACT-T1-001, ACT-O4-001)

#### Column B - TOM ID
**Format:** Link to TOM in Sheet 2 (e.g., T1, O4)

#### Column C - Gap Description
**Content:** Copy from Sheet 6 Column C (or abbreviated version)
**Example:** "6/20 production databases lack TDE encryption"

#### Column D - Proposed Solution
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

#### Column E - Owner
**Format:** Full name and role
**Example:** "Bob Williams, Database Administrator"

**Ownership Guidelines:**
- **Technical measures (T1-T10):** IT/Security teams (Database Admin, Security Architect, Network Engineer)
- **Organizational measures (O1-O10):** Compliance/Legal teams (DPO, Compliance Officer, Legal Counsel)
- **Cross-functional measures:** Collaboration required (e.g., O4 Vendor Management requires Legal + Procurement + DPO)

#### Column F - Start Date
**Format:** YYYY-MM-DD
**Guidance:** When will remediation begin?

**Examples:**
- ACT-T1-001 (Database upgrade): 2026-01-15 (Phase 1 assessment starts)
- ACT-O4-001 (Vendor risk assessment process): 2026-02-01 (Project kickoff)

#### Column G - Target Date
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

#### Column H - Status
**Dropdown Options:** Not Started, In Progress, Blocked, Complete, Cancelled

**Status Definitions:**
- **Not Started:** Project not yet begun (future start date)
- **In Progress:** Active work underway
- **Blocked:** Impediment preventing progress (e.g., budget approval pending, vendor unresponsive, technical blocker)
- **Complete:** Remediation finished and validated (evidence in Sheet 5, status updated in Sheet 2)
- **Cancelled:** Action cancelled (e.g., risk accepted, alternative solution implemented, requirements changed)

#### Column I - % Complete
**Format:** 0-100%
**Guidance:** Estimated progress

**Examples:**
- 0%: Not Started
- 25%: Phase 1 complete (assessment done)
- 50%: Phase 2 complete (pilot upgrade done)
- 75%: Phase 3 in progress (2/3 batches complete)
- 100%: Complete (all phases finished, validated)

**Update Frequency:** Monthly (or more frequently for urgent/high-priority actions)

#### Column J - Completion Date
**Format:** YYYY-MM-DD (blank if not complete)
**Guidance:** Actual completion date when Status=Complete

**Validation:** Completion date should align with evidence update in Sheet 5

**Example:**
- ACT-T1-001: Start 2026-01-15, Target 2026-09-01, Completion 2026-08-20 (11 days early)

---

### 4.8 Sheet 8: Compliance Dashboard

**Purpose:** Executive summary of TOM compliance (auto-calculated metrics)

**NO DATA ENTRY REQUIRED - All Metrics Auto-Calculated from Sheets 2-7**

**Dashboard Sections:**

#### Section 1: Implementation Status (Rows 5-12)
- **Total TOMs:** 20 (constant)
- **Implemented:** `=COUNTIF('2. TOM Control Inventory'!D2:D21,"Implemented")`
- **Partially Implemented:** `=COUNTIF('2. TOM Control Inventory'!D2:D21,"Partially Implemented")`
- **Planned:** `=COUNTIF('2. TOM Control Inventory'!D2:D21,"Planned")`
- **Not Implemented:** `=COUNTIF('2. TOM Control Inventory'!D2:D21,"Not Implemented")`
- **Implementation Rate:** `=('2. TOM Control Inventory'!Implemented + 'Partially Implemented'*0.5) / 20`
  - Formula explanation: Full implementations count 100%, partial implementations count 50%
  - **Target:** ≥90%
  - **Conditional formatting:** Green if ≥90%, Yellow if 80-89%, Red if <80%

#### Section 2: Technical vs. Organizational (Rows 14-21)
- **Technical Measures Implemented:** `=COUNTIFS('2. TOM Control Inventory'!C2:C21,"Technical",'2. TOM Control Inventory'!D2:D21,"Implemented")`
- **Technical Measures Total:** 10
- **Technical Implementation Rate:** `=Technical Implemented / 10`
- **Organizational Measures Implemented:** `=COUNTIFS('2. TOM Control Inventory'!C2:C21,"Organizational",'2. TOM Control Inventory'!D2:D21,"Implemented")`
- **Organizational Measures Total:** 10
- **Organizational Implementation Rate:** `=Organizational Implemented / 10`
- **Analysis:** Technical measures typically easier to implement (buy tools/deploy technology), organizational measures require culture change and sustained effort

#### Section 3: Control Effectiveness (Rows 23-30)
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

#### Section 4: Gap Analysis (Rows 32-40)
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

#### Section 5: Remediation Progress (Rows 42-50)
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

#### Section 6: GDPR Art. 32 Compliance Score (Rows 52-60)

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

#### Section 7: Evidence Summary (Rows 62-68)
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

## 5. Evidence Collection

### 5.1 What Evidence to Gather

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
- ✅ Azure AD user/group report (user list, group memberships, role assignments)
- ✅ Conditional Access policy configurations (screenshots of all 12 policies)
- ✅ MFA enrollment report (percentage of users with MFA enabled)
- ✅ Password policy configuration (Azure AD password settings)
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

### 5.2 Where to Find Evidence

**Technical Systems:**
- **SIEM (Splunk):** Dashboards > Reports > Saved Searches
- **Azure AD:** Azure portal > Azure Active Directory > Reports > Sign-ins/Audit logs
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

### 5.3 How to Document Evidence

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

## 6. Common Pitfalls

### Pitfall 1: Confusing "Implemented" with "Effective"
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

### Pitfall 2: Inadequate Evidence Documentation
**Issue:** Claiming control implementation without supporting evidence.

**Assessment:** Every implemented TOM must have evidence in Sheet 5.

**Gap:** Auditors will reject claims without proof. Result: Control considered "not implemented" by auditor.

**Remediation:**
- Minimum 3-5 evidence items per TOM
- Variety of evidence types (technical configs, policies, audit reports, test results)
- Current evidence (configs from last 3 months, audit reports from last 12 months)
- Example: T1 Encryption → Evidence should include: (1) TLS config screenshot, (2) Database TDE query, (3) FDE deployment report, (4) SSL Labs test result, (5) Backup encryption config

---

### Pitfall 3: Overestimating Implementation Coverage
**Issue:** Rating control as "Implemented (✅)" when coverage is actually 80% (should be "Partially Implemented ⚠️").

**Assessment:** Implemented = 90-100% coverage. 80% = Partially Implemented.

**Gap:** Organizations round up coverage percentages. Result: Gaps hidden, auditor finds discrepancies.

**Remediation:**
- Be honest about coverage percentages
- Document exceptions/exclusions explicitly (Column F in Sheet 2)
- If 80% coverage, rate as "Partially Implemented" and document gap in Column J
- Example: T2 Access Control → 95/100 applications integrated with Azure AD (95%) → "Implemented ✅". If only 85/100 (85%) → "Partially Implemented ⚠️" with gap documentation for 15 non-integrated applications.

---

### Pitfall 4: Missing Gap Risk Assessment
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

### Pitfall 5: Remediation Plans Lack Detail
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

### Pitfall 6: Treating All Gaps as Equal Priority
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

### Pitfall 7: No Evidence Verification Process
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

### Pitfall 8: Confusing Policy Existence with Control Implementation
**Issue:** Believing that having a policy equals control implementation (O1 Policies rated "Implemented" but actual controls in T1-T10 not deployed).

**Assessment:** O1 Policies documents the EXISTENCE of policies. T1-T10, O2-O10 document IMPLEMENTATION of controls specified in policies.

**Gap:** "Paper compliance" - policies written but not followed. Result: Auditor finds policy-practice gap, material non-compliance.

**Remediation:**
- Rate O1 Policies based on policy documentation (policies written, approved, published)
- Rate T1-T10, O2-O10 based on actual control implementation (policies FOLLOWED, controls DEPLOYED)
- Example: ISMS-POL-A.8.24 Cryptography Policy (O1) states "TLS 1.3 shall be used" → Rate O1="Implemented" (policy exists) → T1 Encryption implementation checks if TLS 1.3 actually deployed → If yes, T1="Implemented"; if no, T1="Not Implemented" + gap documented

---

### Pitfall 9: Ignoring Organizational Measures (O1-O10)
**Issue:** Focusing solely on technical controls (T1-T10) while neglecting organizational controls (O1-O10).

**Assessment:** Organizational measures are equally important for GDPR Art. 32 compliance.

**Gap:** Technical controls without organizational support fail. Example: Encryption (T1) deployed but no training (O2) → users store PII in unencrypted file shares.

**Remediation:**
- Give equal attention to O1-O10
- Ensure organizational measures support technical measures
- Example: T2 Access Control requires O2 Training (users must understand least privilege), O6 Accountability (data ownership), O8 Compliance Monitoring (access reviews)

---

### Pitfall 10: Treating Assessment as "Point-in-Time" Activity
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

## 7. Quality Checklist

### 7.1 Sheet 1: Instructions & Legend
- [ ] Sheet reviewed and understood by all assessment participants
- [ ] All 20 TOM categories clearly defined
- [ ] Implementation status definitions understood (Implemented/Partially/Planned/Not Implemented)
- [ ] Effectiveness rating definitions understood (Effective/Partially Effective/Ineffective/Not Tested)
- [ ] Risk rating methodology understood (likelihood × impact matrix)

### 7.2 Sheet 2: TOM Control Inventory

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

### 7.3 Sheet 3: Technical Measures Deep-Dive

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

### 7.4 Sheet 4: Organizational Measures Deep-Dive

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

### 7.5 Sheet 5: Evidence Repository

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

### 7.6 Sheet 6: Gap Analysis & Risk Assessment

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

### 7.7 Sheet 7: Remediation Action Plan

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

### 7.8 Sheet 8: Compliance Dashboard

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

### 7.9 General Quality Checks

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

## 8. Review & Approval

### 8.1 Internal Review Process

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

### 8.2 Approval Workflow

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

### 8.3 Sign-Off Documentation

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

**END OF PART 1: USER COMPLETION GUIDE**

**Document Status:** ✅ COMPLETE

**Next Steps:** Proceed to PART 2 (Technical Specifications - Sheets 1-4) for detailed workbook structure, exact column definitions, formulas, styling, and conditional formatting.

---

# PART II: TECHNICAL SPECIFICATION

## 1. Workbook Structure

### 1.1 File Naming Convention

**Format:** `ISMS_A_5_34_4_TOMs_Assessment_YYYYMMDD.xlsx`

**Examples:**
- `ISMS_A_5_34_4_TOMs_Assessment_20260115.xlsx`
- `ISMS_A_5_34_4_TOMs_Assessment_20260630.xlsx`

**Versioning:** Date-based (YYYYMMDD in filename represents assessment date)

### 1.2 Sheet Structure

**Total Sheets:** 8

| Sheet # | Sheet Name | Purpose | Rows | User Input |
|---------|------------|---------|------|------------|
| 1 | Instructions & Legend | Reference guide, TOM definitions, status legend | 100 | No (read-only) |
| 2 | TOM Control Inventory | Main assessment - 20 TOMs implementation status | 21 data rows | Yes |
| 3 | Technical Measures Deep-Dive | T1-T10 detailed documentation | Variable | Yes |
| 4 | Organizational Measures Deep-Dive | O1-O10 detailed documentation | Variable | Yes |
| 5 | Evidence Repository | Proof of implementation | 1000 rows | Yes |
| 6 | Gap Analysis & Risk Assessment | Gap identification and risk matrix | 200 rows | Yes |
| 7 | Remediation Action Plan | Gap closure tracking | 200 rows | Yes |
| 8 | Compliance Dashboard | Executive metrics (auto-calculated) | 70 rows | No (formulas) |

### 1.3 Sheet Protection

**Protected Sheets:** 1 (Instructions), 8 (Dashboard)
**Unprotected Sheets:** 2, 3, 4, 5, 6, 7 (user data entry)

**Protection Settings:**
- Password: `[Set during workbook generation]`
- Allow: Format cells, Insert rows, Sort, Filter, AutoFilter
- Disallow: Delete rows, Modify formulas, Unprotect sheet, Delete columns

**Protected Cells within Unprotected Sheets:**
- Column headers (Row 1)
- Formula cells (auto-calculated fields)
- Pre-populated data (TOM IDs, TOM Categories in Sheet 2)

---

## 2. Cell Styling Reference

### 2.1 Standard Color Palette

| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| **Dark Blue** | #1F4E78 | 31, 78, 120 | Main headers, emphasis |
| **Medium Blue** | #305496 | 48, 84, 150 | Subheaders |
| **Light Blue** | #B4C7E7 | 180, 199, 231 | Section headers, Planned status |
| **Green (Compliant)** | #C6EFCE | 198, 239, 206 | Implemented, Effective, Compliant status |
| **Yellow (Partial)** | #FFEB9C | 255, 235, 156 | Partially Implemented, Partial compliance |
| **Red (Non-Compliant)** | #FFC7CE | 255, 199, 206 | Not Implemented, Ineffective, Critical risk |
| **Dark Red** | #C00000 | 192, 0, 0 | Critical risk text |
| **Orange** | #FFA500 | 255, 165, 0 | High risk, Blocked status |
| **White** | #FFFFFF | 255, 255, 255 | Standard cell background |
| **Light Gray** | #D9D9D9 | 217, 217, 217 | Column headers, protected cells |
| **Input Yellow** | #FFFFCC | 255, 255, 204 | User input cells (unprotected) |

### 2.2 Header Styling Standards

**Level 1 Headers (Sheet Titles):**
- Font: Calibri 14pt, Bold, White
- Fill: #1F4E78 (Dark Blue)
- Alignment: Center, Vertical Center
- Height: 40px
- Border: Thin black on all sides

**Level 2 Headers (Section Titles):**
- Font: Calibri 12pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Center, Vertical Center
- Height: 30px
- Border: Thin black on all sides

**Column Headers:**
- Font: Calibri 10pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Center, Vertical Center, Wrap Text
- Border: Thin black on all sides
- Height: Auto (wrap text determines height)

### 2.3 Data Cell Styling

**User Input Cells:**
- Font: Calibri 10pt, Regular, Black
- Fill: #FFFFCC (Light Yellow) - indicates editable
- Alignment: Left (text), Right (numbers), Center (dropdowns)
- Border: Thin gray on all sides
- Protection: Unlocked

**Formula Cells:**
- Font: Calibri 10pt, Regular, Black
- Fill: #FFFFFF (White)
- Alignment: Right (numbers), Center (status)
- Border: Thin gray on all sides
- Protection: Locked

**Protected/Pre-Filled Cells:**
- Font: Calibri 10pt, Regular, Gray (RGB: 128, 128, 128)
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left
- Border: Thin black on all sides
- Protection: Locked

### 2.4 Status Color Coding

**Implementation Status (Sheet 2 Column D):**
- **Implemented (✅):** Font: Black, Fill: #C6EFCE (Green)
- **Partially Implemented (⚠️):** Font: Black, Fill: #FFEB9C (Yellow)
- **Planned (📄):** Font: Black, Fill: #B4C7E7 (Light Blue)
- **Not Implemented (❌):** Font: Black, Fill: #FFC7CE (Red)

**Effectiveness Rating (Sheet 2 Column H):**
- **Effective (✅):** Font: Black, Fill: #C6EFCE (Green)
- **Partially Effective (⚠️):** Font: Black, Fill: #FFEB9C (Yellow)
- **Ineffective (❌):** Font: Black, Fill: #FFC7CE (Red)
- **Not Tested (🔍):** Font: Black, Fill: #B4C7E7 (Light Blue)

**Risk Level (Sheet 2 Column K, Sheet 6 Column F):**
- **Critical:** Font: #C00000 (Dark Red), Bold, Fill: #FFC7CE (Red)
- **High:** Font: Black, Fill: #FFA500 (Orange)
- **Medium:** Font: Black, Fill: #FFEB9C (Yellow)
- **Low:** Font: Black, Fill: #C6EFCE (Green)

### 2.5 Dropdown Styling

**Standard Dropdown:**
- Font: Calibri 10pt, Regular, Black
- Fill: #FFFFCC (Light Yellow) when empty
- Fill: Status-based color when selected (see Status Color Coding above)
- Border: Thin gray on all sides
- Validation: List (dropdown arrow visible)

**Dropdown with Emoji:**
- Include emoji in dropdown text (e.g., "✅ Implemented", "⚠️ Partial", "❌ Non-Compliant")
- Font: Calibri 10pt (emoji renders at system default)
- Color coding applies to entire cell (background fill)

---

## 3. Sheet 1: Instructions & Legend

### 3.1 Sheet Purpose
Read-only reference guide embedded in workbook. Contains TOM definitions, status legends, risk matrix, evidence requirements.

### 3.2 Sheet Layout

**Row 1:** "ISMS-IMP-A.5.34.4 - TECHNICAL AND ORGANIZATIONAL MEASURES (TOMS) ASSESSMENT"
- Merged: A1:G1
- Font: Calibri 14pt, Bold, White
- Fill: #1F4E78 (Dark Blue)
- Alignment: Center, Vertical Center
- Height: 40px

**Row 2:** "ISO/IEC 27001:2022 - Control A.5.34: Privacy and Protection of PII"
- Merged: A2:G2
- Font: Calibri 11pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Center, Vertical Center
- Height: 25px

**Row 3:** [Blank spacer row, height: 15px]

### 3.3 Document Information Block (Rows 4-12)

**Row 4:** "DOCUMENT INFORMATION" (section header)
- Merged: A4:G4
- Font: Calibri 12pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Vertical Center
- Height: 25px

**Rows 5-12:** Two-column layout (Label | Value)

| Row | Column A (Label) | Column B:G (Value - Merged) |
|-----|------------------|----------------------------|
| 5 | Document ID: | ISMS-IMP-A.5.34.4 |
| 6 | Version: | 2.0 |
| 7 | Assessment Area: | Technical and Organizational Measures (TOMs) for PII Protection |
| 8 | Related Policy: | ISMS-POL-A.5.34, Section 2.4 (Technical and Organizational Measures) |
| 9 | Purpose: | Assess implementation and effectiveness of security controls protecting PII processing per GDPR Art. 32, Swiss FADP Art. 8, ISO 27001 |
| 10 | Assessment Date: | [USER INPUT - yellow cell, date format] |
| 11 | Completed By: | [USER INPUT - yellow cell] |
| 12 | Organization: | [USER INPUT - yellow cell] |

**Column A Styling:**
- Font: Calibri 10pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Vertical Center
- Width: 20

**Column B:G Styling (Merged):**
- Font: Calibri 10pt, Regular, Black
- Fill: #FFFFFF (White) for pre-filled, #FFFFCC (Yellow) for user input
- Alignment: Left, Vertical Center
- Width: B=25, C=25, D=25, E=25, F=25, G=25

**Row 13:** [Blank spacer, height: 15px]

### 3.4 The 20 TOM Categories (Rows 14-48)

**Row 14:** "THE 20 TOM CATEGORIES" (section header)
- Merged: A14:G14
- Font: Calibri 12pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Vertical Center
- Height: 25px

**Row 15:** "Technical Measures (T1-T10)" (subsection header)
- Merged: A15:G15
- Font: Calibri 11pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Left, Vertical Center
- Height: 20px

**Rows 16-25:** T1-T10 list (two-column: TOM ID | Description)

| Row | Column A (TOM ID) | Column B:G (Description - Merged) |
|-----|-------------------|-----------------------------------|
| 16 | T1 | Encryption - Data encryption in transit and at rest |
| 17 | T2 | Access Control - Role-based access control (RBAC), least privilege |
| 18 | T3 | Pseudonymization/Anonymization - Data minimization techniques |
| 19 | T4 | Data Minimization - Collection limitation, purpose limitation |
| 20 | T5 | Security Monitoring & Logging - SIEM, audit trails, anomaly detection |
| 21 | T6 | Network Security - Firewalls, segmentation, intrusion detection |
| 22 | T7 | Application Security - Secure coding, input validation, WAF |
| 23 | T8 | Endpoint Security - EDR, anti-malware, device management |
| 24 | T9 | Backup & Recovery - Business continuity, disaster recovery |
| 25 | T10 | Physical Security - Data center security, device disposal |

**Column A Styling:**
- Font: Calibri 10pt, Bold, #1F4E78 (Dark Blue)
- Fill: #B4C7E7 (Light Blue)
- Alignment: Center, Vertical Center
- Width: 8

**Column B:G Styling (Merged):**
- Font: Calibri 10pt, Regular, Black
- Fill: #FFFFFF (White)
- Alignment: Left, Vertical Center

**Row 26:** [Blank spacer, height: 10px]

**Row 27:** "Organizational Measures (O1-O10)" (subsection header)
- Merged: A27:G27
- Font: Calibri 11pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Left, Vertical Center
- Height: 20px

**Rows 28-37:** O1-O10 list

| Row | Column A (TOM ID) | Column B:G (Description - Merged) |
|-----|-------------------|-----------------------------------|
| 28 | O1 | Policies & Procedures - Written security policies, procedures |
| 29 | O2 | Staff Training & Awareness - Privacy training, phishing awareness |
| 30 | O3 | Incident Response & Breach Notification - IR plan, 72-hour notification |
| 31 | O4 | Vendor Management - Third-party risk management, DPAs |
| 32 | O5 | Data Protection by Design/Default - Privacy-first architecture |
| 33 | O6 | Accountability & Governance - DPO appointment, data ownership |
| 34 | O7 | Risk Management - Privacy risk assessments, DPIAs |
| 35 | O8 | Compliance Monitoring & Audit - Internal audits, control testing |
| 36 | O9 | Documentation & Records - ROPA, consent logs, DSR logs |
| 37 | O10 | Business Continuity - BC/DR plans, resilience |

**Styling:** Same as T1-T10 rows

**Row 38:** [Blank spacer, height: 15px]

### 3.5 Implementation Status Legend (Rows 39-48)

**Row 39:** "IMPLEMENTATION STATUS LEGEND" (section header)
- Merged: A39:G39
- Font: Calibri 12pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Vertical Center
- Height: 25px

**Rows 40-47:** Status definitions (three-column: Symbol | Status | Definition)

| Row | Column A (Symbol) | Column B (Status) | Column C:G (Definition - Merged) |
|-----|-------------------|-------------------|----------------------------------|
| 40 | ✅ | Implemented | Control fully deployed and operating effectively across all in-scope systems (90-100% coverage) |
| 41 | ⚠️ | Partially Implemented | Control exists but has gaps (50-89% coverage, some exceptions) |
| 42 | 📄 | Planned | Control approved and funded but not yet deployed (<50% coverage with approved project) |
| 43 | ❌ | Not Implemented | Control not in place (<50% coverage, no plan) |
| 44 | [blank] | [blank] | [blank] |
| 45 | **Effectiveness Rating:** | [blank] | [blank] |
| 46 | ✅ | Effective | Control operating as intended, validated through testing, no known failures |
| 47 | ⚠️ | Partially Effective | Control operating but with limitations, some failures identified |
| 48 | ❌ | Ineffective | Control failing to meet objectives, significant failures, needs replacement |

**Column A Styling (Symbol):**
- Font: Calibri 16pt, Regular
- Fill: Status-based color (Green/Yellow/Blue/Red)
- Alignment: Center, Vertical Center
- Width: 5

**Column B Styling (Status):**
- Font: Calibri 10pt, Bold, Black
- Fill: #FFFFFF (White)
- Alignment: Left, Vertical Center
- Width: 20

**Column C:G Styling (Definition - Merged):**
- Font: Calibri 10pt, Regular, Black
- Fill: #FFFFFF (White)
- Alignment: Left, Vertical Center, Wrap Text

**Row 49:** [Blank spacer, height: 15px]

### 3.6 Risk Rating Matrix (Rows 50-60)

**Row 50:** "RISK RATING MATRIX (Likelihood × Impact)" (section header)
- Merged: A50:G50
- Font: Calibri 12pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Vertical Center
- Height: 25px

**Rows 51-56:** Risk matrix table

| Row | Column A | Column B | Column C | Column D | Column E |
|-----|----------|----------|----------|----------|----------|
| 51 | **LIKELIHOOD** | **Low Impact** | **Medium Impact** | **High Impact** | **Critical Impact** |
| 52 | **High** | Medium | High | Critical | Critical |
| 53 | **Medium** | Low | Medium | High | Critical |
| 54 | **Low** | Low | Low | Medium | High |

**Row 51 (Header Row):**
- Font: Calibri 10pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Center, Vertical Center
- Border: Thin black on all sides

**Column A (Rows 52-54 - Likelihood labels):**
- Font: Calibri 10pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Center, Vertical Center
- Width: 15

**Risk Cells (B52:E54):**
- Font: Calibri 10pt, Bold, Black
- Fill: Risk-based color:
  - Critical: #FFC7CE (Red)
  - High: #FFA500 (Orange)
  - Medium: #FFEB9C (Yellow)
  - Low: #C6EFCE (Green)
- Alignment: Center, Vertical Center
- Border: Thin black on all sides

**Row 56:** [Blank spacer, height: 10px]

**Rows 57-60:** Risk level definitions

| Row | Column A (Risk Level) | Column B:G (Definition - Merged) |
|-----|-----------------------|----------------------------------|
| 57 | **Critical** | Massive PII breach (>100,000 records), material regulatory enforcement, business-ending event |
| 58 | **High** | Large PII breach (10,000-100,000 records), regulatory investigation, significant financial/reputational harm |
| 59 | **Medium** | Moderate PII breach (1,000-10,000 records), supervisory authority inquiry, manageable harm |
| 60 | **Low** | Small PII breach (<1,000 records), minor supervisory authority concern, minimal harm |

**Column A Styling:**
- Font: Calibri 10pt, Bold, Black
- Fill: Risk-based color (see above)
- Alignment: Center, Vertical Center
- Width: 15

**Column B:G Styling:**
- Font: Calibri 10pt, Regular, Black
- Fill: #FFFFFF (White)
- Alignment: Left, Vertical Center, Wrap Text

**Row 61:** [Blank spacer, height: 15px]

### 3.7 Evidence Requirements (Rows 62-80)

**Row 62:** "EVIDENCE REQUIREMENTS" (section header)
- Merged: A62:G62
- Font: Calibri 12pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Vertical Center
- Height: 25px

**Row 63:** "Each TOM must have supporting evidence in Sheet 5 (Evidence Repository). Minimum 5 evidence items per TOM."
- Merged: A63:G63
- Font: Calibri 10pt, Italic, Black
- Fill: #FFEB9C (Yellow)
- Alignment: Left, Vertical Center, Wrap Text
- Height: Auto

**Row 64:** [Blank spacer, height: 10px]

**Rows 65-80:** Evidence types with examples (two-column: Evidence Type | Examples)

| Row | Column A:B (Evidence Type - Merged) | Column C:G (Examples - Merged) |
|-----|-------------------------------------|--------------------------------|
| 65 | **Configuration Screenshot** | TLS configs, database encryption settings, firewall rules |
| 66 | **Policy Document** | ISMS policies (approved, current version) |
| 67 | **Training Report** | LMS completion reports, quiz results, certificates |
| 68 | **Audit Report** | Internal audit reports, ISO 27001 audit, SOC 2 report |
| 69 | **Test Results** | Penetration test reports, vulnerability scans, DR test logs |
| 70 | **Vendor Assessment** | Vendor risk assessments, SOC 2 reports, DPAs |
| 71 | **Incident Response Test** | Tabletop exercise reports, breach simulation results |
| 72 | **System Log Extract** | SIEM alert logs, access logs, authentication logs |
| 73 | **Certificate** | ISO 27001 certificate, DPO certification (CIPP/E) |
| 74 | **DPA** | Data Processing Agreements with processors |
| 75 | **Risk Assessment** | Privacy risk assessments, DPIA documentation |
| 76 | **Penetration Test Report** | External pen test results (web app, network, cloud) |
| 77 | **Vulnerability Scan** | Qualys/Nessus scan results, remediation tracking |
| 78 | **Business Continuity Test** | BC/DR test reports, RTO/RPO validation |
| 79 | **Disaster Recovery Test** | Backup restoration test logs, failover test results |
| 80 | **Other** | Any other relevant evidence (describe in Sheet 5) |

**Column A:B Styling (Evidence Type - Merged):**
- Font: Calibri 10pt, Bold, Black
- Fill: #B4C7E7 (Light Blue)
- Alignment: Left, Vertical Center
- Width: A=15, B=15

**Column C:G Styling (Examples - Merged):**
- Font: Calibri 10pt, Regular, Black
- Fill: #FFFFFF (White)
- Alignment: Left, Vertical Center, Wrap Text

**Row 81:** [Blank spacer, height: 15px]

### 3.8 Assessment Instructions (Rows 82-100)

**Row 82:** "HOW TO COMPLETE THIS ASSESSMENT" (section header)
- Merged: A82:G82
- Font: Calibri 12pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Vertical Center
- Height: 25px

**Rows 83-100:** Step-by-step instructions (numbered list)

| Row | Column A:G (Instructions - Merged) |
|-----|------------------------------------|
| 83 | **Step 1:** Complete Sheet 2 (TOM Control Inventory) - Rate implementation status and effectiveness for all 20 TOMs |
| 84 | **Step 2:** Complete Sheets 3-4 (Technical/Organizational Deep-Dive) - Document detailed implementation for T1-T10 and O1-O10 |
| 85 | **Step 3:** Complete Sheet 5 (Evidence Repository) - Document all evidence proving TOM implementation (minimum 5 items per TOM) |
| 86 | **Step 4:** Complete Sheet 6 (Gap Analysis) - Assess risk for all identified gaps using likelihood × impact matrix |
| 87 | **Step 5:** Complete Sheet 7 (Remediation Action Plan) - Define remediation plans for all Medium/High/Critical risk gaps |
| 88 | **Step 6:** Review Sheet 8 (Compliance Dashboard) - Verify auto-calculated metrics, identify improvement areas |
| 89 | **Step 7:** Quality Review - Use Quality Checklist in User Guide (PART 1) to verify completeness |
| 90 | **Step 8:** Approval & Sign-Off - Obtain CISO, DPO, and executive approvals |
| 91 | [blank] |
| 92 | **Target Metrics:** |
| 93 | • Implementation Rate: ≥90% (at least 18/20 TOMs implemented or partially implemented) |
| 94 | • Effectiveness Rate: ≥95% (at least 95% of implemented controls tested effective) |
| 95 | • Critical Gaps: 0 (no critical risk gaps acceptable) |
| 96 | • High Risk Gaps: ≤3 (minimize high-risk exposure) |
| 97 | • Remediation Progress: ≥80% (most actions should be complete or in progress) |
| 98 | • GDPR Art. 32 Compliance Score: ≥80% (good compliance minimum threshold) |
| 99 | [blank] |
| 100 | For detailed guidance, refer to User Completion Guide (PART 1) |

**Column A:G Styling (Merged):**
- Font: Calibri 10pt, Regular, Black
- Fill: #FFFFFF (White)
- Alignment: Left, Top, Wrap Text
- Height: Auto (wrap text determines height)

**Bold Items (Step numbers, Target Metrics label):**
- Font: Calibri 10pt, Bold, Black

### 3.9 Sheet Protection

**Sheet 1 Protection:** ON
- Password: `[Set during workbook generation]`
- All cells locked (read-only)
- Allow: Select locked cells, Select unlocked cells
- Disallow: Everything else

### 3.10 Freeze Panes

**Freeze:** Row 4 (header rows 1-3 always visible when scrolling)

---

## 4. Sheet 2: TOM Control Inventory

### 4.1 Sheet Purpose
Main assessment sheet documenting implementation status, effectiveness, gaps, and remediation plans for all 20 TOMs.

### 4.2 Sheet Layout

**Row 1:** "TOM CONTROL INVENTORY - 20 TECHNICAL AND ORGANIZATIONAL MEASURES"
- Merged: A1:N1
- Font: Calibri 14pt, Bold, White
- Fill: #1F4E78 (Dark Blue)
- Alignment: Center, Vertical Center
- Height: 40px

**Row 2:** "Assess implementation status and effectiveness for all 20 TOMs"
- Merged: A2:N2
- Font: Calibri 11pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Center, Vertical Center
- Height: 25px

**Row 3:** [Blank spacer row, height: 15px]

### 4.3 Column Headers (Row 4)

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | TOM ID | 8 | Text (pre-filled) | None (locked) |
| B | TOM Category | 35 | Text (pre-filled) | None (locked) |
| C | TOM Type | 15 | Text (pre-filled) | None (locked) |
| D | Implementation Status | 20 | Dropdown | List: Implemented, Partially Implemented, Planned, Not Implemented |
| E | Implementation Date | 15 | Date | Date format (YYYY-MM-DD) |
| F | Description of Implementation | 80 | Text (multiline) | None |
| G | Evidence Reference | 20 | Text | None |
| H | Effectiveness Rating | 20 | Dropdown | List: Effective, Partially Effective, Ineffective, Not Tested |
| I | Last Test Date | 15 | Date | Date format (YYYY-MM-DD) |
| J | Gaps Identified | 60 | Text (multiline) | None |
| K | Risk Level | 15 | Dropdown | List: Critical, High, Medium, Low, N/A |
| L | Remediation Plan | 60 | Text (multiline) | None |
| M | Remediation Owner | 25 | Text | None |
| N | Target Completion Date | 15 | Date | Date format (YYYY-MM-DD) |

**Header Row Styling:**
- Font: Calibri 10pt, Bold, White
- Fill: #1F4E78 (Dark Blue)
- Alignment: Center, Vertical Center, Wrap Text
- Border: Thin black on all sides
- Height: 60px (allows multi-line headers)

### 4.4 Data Rows (Rows 5-24)

**Pre-Populated Data (Columns A-C):**

**Rows 5-14: Technical Measures (T1-T10)**

| Row | Col A (TOM ID) | Col B (TOM Category) | Col C (TOM Type) |
|-----|----------------|----------------------|------------------|
| 5 | T1 | Encryption | Technical |
| 6 | T2 | Access Control | Technical |
| 7 | T3 | Pseudonymization/Anonymization | Technical |
| 8 | T4 | Data Minimization | Technical |
| 9 | T5 | Security Monitoring & Logging | Technical |
| 10 | T6 | Network Security | Technical |
| 11 | T7 | Application Security | Technical |
| 12 | T8 | Endpoint Security | Technical |
| 13 | T9 | Backup & Recovery | Technical |
| 14 | T10 | Physical Security | Technical |

**Rows 15-24: Organizational Measures (O1-O10)**

| Row | Col A (TOM ID) | Col B (TOM Category) | Col C (TOM Type) |
|-----|----------------|----------------------|------------------|
| 15 | O1 | Policies & Procedures | Organizational |
| 16 | O2 | Staff Training & Awareness | Organizational |
| 17 | O3 | Incident Response & Breach Notification | Organizational |
| 18 | O4 | Vendor Management | Organizational |
| 19 | O5 | Data Protection by Design/Default | Organizational |
| 20 | O6 | Accountability & Governance | Organizational |
| 21 | O7 | Risk Management | Organizational |
| 22 | O8 | Compliance Monitoring & Audit | Organizational |
| 23 | O9 | Documentation & Records | Organizational |
| 24 | O10 | Business Continuity | Organizational |

**Pre-Filled Cell Styling (Columns A-C, Rows 5-24):**
- Font: Calibri 10pt, Regular, #505050 (Dark Gray)
- Fill: #D9D9D9 (Light Gray)
- Alignment: Center (Col A), Left (Col B-C), Vertical Center
- Border: Thin gray on all sides
- Protection: Locked (cannot be edited)

### 4.5 Data Validation Rules

**Column D - Implementation Status:**
```
Validation Type: List
Source: ="Implemented,Partially Implemented,Planned,Not Implemented"
Error Style: Stop
Error Message: "Please select a valid implementation status"
Input Message: "Select implementation status: Implemented (90-100% coverage), Partially Implemented (50-89%), Planned (<50% with project), Not Implemented (<50% no project)"
Allow Blank: No
Applies To: D5:D24
```

**Column E - Implementation Date:**
```
Validation Type: Date
Data: Between
Start Date: 2000-01-01
End Date: =TODAY()+365
Error Style: Stop
Error Message: "Implementation date must be between 2000 and next year"
Input Message: "Enter implementation date (YYYY-MM-DD)"
Allow Blank: Yes (blank if not yet implemented)
Applies To: E5:E24
```

**Column H - Effectiveness Rating:**
```
Validation Type: List
Source: ="Effective,Partially Effective,Ineffective,Not Tested"
Error Style: Stop
Error Message: "Please select a valid effectiveness rating"
Input Message: "Select effectiveness rating: Effective (control working as intended), Partially Effective (working with limitations), Ineffective (failing), Not Tested (not yet validated)"
Allow Blank: No
Applies To: H5:H24
```

**Column I - Last Test Date:**
```
Validation Type: Date
Data: Between
Start Date: 2000-01-01
End Date: =TODAY()+7
Error Style: Stop
Error Message: "Last test date must be between 2000 and today"
Input Message: "Enter last test date (YYYY-MM-DD)"
Allow Blank: Yes (blank if not tested)
Applies To: I5:I24
```

**Column K - Risk Level:**
```
Validation Type: List
Source: ="Critical,High,Medium,Low,N/A"
Error Style: Stop
Error Message: "Please select a valid risk level"
Input Message: "Select risk level based on likelihood × impact matrix (see Sheet 1)"
Allow Blank: Yes (N/A if no gaps)
Applies To: K5:K24
```

**Column N - Target Completion Date:**
```
Validation Type: Date
Data: Between
Start Date: =TODAY()
End Date: =TODAY()+730
Error Style: Stop
Error Message: "Target completion date must be between today and 2 years from today"
Input Message: "Enter target remediation completion date (YYYY-MM-DD)"
Allow Blank: Yes (blank if no remediation required)
Applies To: N5:N24
```

### 4.6 Conditional Formatting Rules

**Rule 1: Implementation Status Color Coding**
```
Applies To: D5:D24
Rule Type: Cell Value
Conditions:
- Cell Value = "Implemented" → Fill: #C6EFCE (Green), Font: Black
- Cell Value = "Partially Implemented" → Fill: #FFEB9C (Yellow), Font: Black
- Cell Value = "Planned" → Fill: #B4C7E7 (Light Blue), Font: Black
- Cell Value = "Not Implemented" → Fill: #FFC7CE (Red), Font: Black
Stop If True: Yes
```

**Rule 2: Effectiveness Rating Color Coding**
```
Applies To: H5:H24
Rule Type: Cell Value
Conditions:
- Cell Value = "Effective" → Fill: #C6EFCE (Green), Font: Black
- Cell Value = "Partially Effective" → Fill: #FFEB9C (Yellow), Font: Black
- Cell Value = "Ineffective" → Fill: #FFC7CE (Red), Font: Black
- Cell Value = "Not Tested" → Fill: #B4C7E7 (Light Blue), Font: Black
Stop If True: Yes
```

**Rule 3: Risk Level Color Coding**
```
Applies To: K5:K24
Rule Type: Cell Value
Conditions:
- Cell Value = "Critical" → Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
- Cell Value = "High" → Fill: #FFA500 (Orange), Font: Black
- Cell Value = "Medium" → Fill: #FFEB9C (Yellow), Font: Black
- Cell Value = "Low" → Fill: #C6EFCE (Green), Font: Black
Stop If True: Yes
```

**Rule 4: Overdue Implementation Date Highlighting**
```
Applies To: E5:E24
Rule Type: Formula
Formula: =AND(E5<>"", E5<TODAY(), D5<>"Implemented")
Format: Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
Stop If True: Yes
Description: Highlights implementation dates in the past where status is not "Implemented" (indicates delay)
```

**Rule 5: Test Date Freshness Warning**
```
Applies To: I5:I24
Rule Type: Formula
Formula: =AND(I5<>"", I5<TODAY()-90, H5<>"Not Tested")
Format: Fill: #FFEB9C (Yellow), Font: Black
Stop If True: Yes
Description: Highlights test dates older than 90 days (testing may need refresh)
```

**Rule 6: Overdue Remediation Target Highlighting**
```
Applies To: N5:N24
Rule Type: Formula
Formula: =AND(N5<>"", N5<TODAY(), K5<>"N/A")
Format: Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
Stop If True: Yes
Description: Highlights overdue remediation targets (target date passed, gap still exists)
```

### 4.7 User Input Cell Styling

**User Input Cells (Columns D-N, Rows 5-24):**
- Font: Calibri 10pt, Regular, Black
- Fill: #FFFFCC (Light Yellow) when empty
- Fill: Conditional formatting-based when populated (see above)
- Alignment: Left (text fields), Center (dropdowns, dates), Vertical Center
- Border: Thin gray on all sides
- Protection: Unlocked
- Text Wrap: Enabled for multiline fields (F, J, L)

**Multiline Text Fields (Columns F, J, L):**
- Minimum Row Height: 60px (allows ~3 lines of text at default font size)
- Text Wrap: Enabled
- Vertical Alignment: Top (text starts at top of cell)

### 4.8 Helper Text / Instructions (Row 25)

**Row 25:** [Blank spacer, height: 15px]

**Row 26:** "NOTES:" (instruction header)
- Merged: A26:N26
- Font: Calibri 11pt, Bold, Black
- Fill: #FFEB9C (Yellow)
- Alignment: Left, Vertical Center
- Height: 25px

**Row 27:** Instruction text
- Merged: A27:N27
- Font: Calibri 10pt, Regular, Black
- Fill: #FFEB9C (Yellow)
- Alignment: Left, Top, Wrap Text
- Height: Auto
- Text: "Complete all 20 rows. Columns A-C are pre-filled (do not edit). For detailed guidance, see Sheet 1 (Instructions & Legend) and User Completion Guide (PART 1, Section 4.2). Link evidence to Sheet 5 (Evidence Repository) using format EV-[TOM ID]-###."

### 4.9 Sheet Protection

**Sheet 2 Protection:** OFF (user data entry sheet)
- Individual cell protection: ON for Columns A-C (pre-filled data locked)
- Individual cell protection: OFF for Columns D-N (user input unlocked)

### 4.10 Freeze Panes

**Freeze:** Row 5, Column C
- Rows 1-4 always visible (headers)
- Columns A-B always visible (TOM ID, TOM Category)

---

## 5. Sheet 3: Technical Measures Deep-Dive

### 5.1 Sheet Purpose
Detailed technical documentation of T1-T10 implementation with specific technologies, configurations, coverage percentages, exceptions, and integrations.

### 5.2 Sheet Layout

**Row 1:** "TECHNICAL MEASURES DEEP-DIVE (T1-T10)"
- Merged: A1:F1
- Font: Calibri 14pt, Bold, White
- Fill: #1F4E78 (Dark Blue)
- Alignment: Center, Vertical Center
- Height: 40px

**Row 2:** "Document detailed technical implementation for each technical measure"
- Merged: A2:F2
- Font: Calibri 11pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Center, Vertical Center
- Height: 25px

**Row 3:** [Blank spacer row, height: 15px]

### 5.3 Section Structure (Repeating Pattern for T1-T10)

Each technical measure (T1-T10) has a dedicated section with the following structure:

**Section Header (1 row):**
- Example: Row 4 for T1
- Merged: A4:F4
- Font: Calibri 12pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Left, Vertical Center
- Height: 30px
- Text: "[TOM ID] - [TOM Category]" (e.g., "T1 - ENCRYPTION")

**Field Rows (5 rows per TOM):**

| Field | Label (Column A:B - Merged) | User Input (Column C:F - Merged) |
|-------|----------------------------|----------------------------------|
| 1 | Technologies Deployed | [USER INPUT - multiline text] |
| 2 | Configuration Details | [USER INPUT - multiline text] |
| 3 | Coverage Percentage | [USER INPUT - percentage or text with numerator/denominator] |
| 4 | Exceptions | [USER INPUT - multiline text] |
| 5 | Integration Notes | [USER INPUT - multiline text] |

**Spacer Row (1 row):**
- Blank row, height: 15px

**Total rows per TOM section:** 7 rows (1 header + 5 fields + 1 spacer)

### 5.4 Complete Row Layout (T1-T10)

**T1 - Encryption (Rows 4-10):**
- Row 4: Section header "T1 - ENCRYPTION"
- Row 5: Technologies Deployed | [User input]
- Row 6: Configuration Details | [User input]
- Row 7: Coverage Percentage | [User input]
- Row 8: Exceptions | [User input]
- Row 9: Integration Notes | [User input]
- Row 10: [Blank spacer]

**T2 - Access Control (Rows 11-17):**
- Row 11: Section header "T2 - ACCESS CONTROL"
- Row 12: Technologies Deployed | [User input]
- Row 13: Configuration Details | [User input]
- Row 14: Coverage Percentage | [User input]
- Row 15: Exceptions | [User input]
- Row 16: Integration Notes | [User input]
- Row 17: [Blank spacer]

**T3 - Pseudonymization/Anonymization (Rows 18-24):**
- Row 18: Section header "T3 - PSEUDONYMIZATION/ANONYMIZATION"
- Row 19-23: Field rows
- Row 24: Spacer

**T4 - Data Minimization (Rows 25-31):**
- Row 25: Section header "T4 - DATA MINIMIZATION"
- Row 26-30: Field rows
- Row 31: Spacer

**T5 - Security Monitoring & Logging (Rows 32-38):**
- Row 32: Section header "T5 - SECURITY MONITORING & LOGGING"
- Row 33-37: Field rows
- Row 38: Spacer

**T6 - Network Security (Rows 39-45):**
- Row 39: Section header "T6 - NETWORK SECURITY"
- Row 40-44: Field rows
- Row 45: Spacer

**T7 - Application Security (Rows 46-52):**
- Row 46: Section header "T7 - APPLICATION SECURITY"
- Row 47-51: Field rows
- Row 52: Spacer

**T8 - Endpoint Security (Rows 53-59):**
- Row 53: Section header "T8 - ENDPOINT SECURITY"
- Row 54-58: Field rows
- Row 59: Spacer

**T9 - Backup & Recovery (Rows 60-66):**
- Row 60: Section header "T9 - BACKUP & RECOVERY"
- Row 61-65: Field rows
- Row 66: Spacer

**T10 - Physical Security (Rows 67-73):**
- Row 67: Section header "T10 - PHYSICAL SECURITY"
- Row 68-72: Field rows
- Row 73: Spacer

### 5.5 Field Label Styling (Column A:B - Merged)

- Font: Calibri 10pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Top, Wrap Text
- Border: Thin black on all sides
- Width: A=15, B=15
- Height: 60px (allows multiline labels)
- Protection: Locked

### 5.6 User Input Styling (Column C:F - Merged)

- Font: Calibri 10pt, Regular, Black
- Fill: #FFFFCC (Light Yellow)
- Alignment: Left, Top, Wrap Text
- Border: Thin gray on all sides
- Width: C=25, D=25, E=25, F=25
- Minimum Height: 60px (allows ~3-4 lines of text)
- Protection: Unlocked
- Text Wrap: Enabled

### 5.7 Section Header Styling

- Font: Calibri 12pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Left, Vertical Center
- Border: Thin black on all sides
- Height: 30px
- Protection: Locked

### 5.8 Data Validation

**No dropdown validation on Sheet 3** (all fields are free-text multiline input)

### 5.9 Conditional Formatting

**No conditional formatting on Sheet 3** (pure data entry, no status-based coloring)

### 5.10 Sheet Protection

**Sheet 3 Protection:** OFF (user data entry sheet)
- Individual cell protection: ON for section headers and field labels (locked)
- Individual cell protection: OFF for user input cells (Column C:F merged cells unlocked)

### 5.11 Freeze Panes

**Freeze:** Row 4 (header rows 1-3 always visible when scrolling)

### 5.12 Helper Instructions (Row 74)

**Row 74:** [Blank spacer, height: 15px]

**Row 75:** "COMPLETION NOTES:" (instruction header)
- Merged: A75:F75
- Font: Calibri 11pt, Bold, Black
- Fill: #FFEB9C (Yellow)
- Alignment: Left, Vertical Center
- Height: 25px

**Row 76:** Instruction text
- Merged: A76:F76
- Font: Calibri 10pt, Regular, Black
- Fill: #FFEB9C (Yellow)
- Alignment: Left, Top, Wrap Text
- Height: Auto
- Text: "Complete all 5 fields for each technical measure (T1-T10). Be specific: include vendor names, product versions, configuration parameters, exact coverage percentages (numerator/denominator), and system integrations. For detailed guidance and examples, see User Completion Guide (PART 1, Section 4.3)."

---

## 6. Sheet 4: Organizational Measures Deep-Dive

### 6.1 Sheet Purpose
Detailed organizational documentation of O1-O10 implementation with specific policies, training programs, governance structures, monitoring methods, and improvement processes.

### 6.2 Sheet Layout

**Row 1:** "ORGANIZATIONAL MEASURES DEEP-DIVE (O1-O10)"
- Merged: A1:F1
- Font: Calibri 14pt, Bold, White
- Fill: #1F4E78 (Dark Blue)
- Alignment: Center, Vertical Center
- Height: 40px

**Row 2:** "Document detailed organizational implementation for each organizational measure"
- Merged: A2:F2
- Font: Calibri 11pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Center, Vertical Center
- Height: 25px

**Row 3:** [Blank spacer row, height: 15px]

### 6.3 Section Structure (Repeating Pattern for O1-O10)

Each organizational measure (O1-O10) has a dedicated section with the following structure:

**Section Header (1 row):**
- Example: Row 4 for O1
- Merged: A4:F4
- Font: Calibri 12pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Left, Vertical Center
- Height: 30px
- Text: "[TOM ID] - [TOM Category]" (e.g., "O1 - POLICIES & PROCEDURES")

**Field Rows (5 rows per TOM):**

| Field | Label (Column A:B - Merged) | User Input (Column C:F - Merged) |
|-------|----------------------------|----------------------------------|
| 1 | Policies in Place | [USER INPUT - multiline text] |
| 2 | Training/Communication | [USER INPUT - multiline text] |
| 3 | Governance Structure | [USER INPUT - multiline text] |
| 4 | Monitoring Method | [USER INPUT - multiline text] |
| 5 | Improvement Process | [USER INPUT - multiline text] |

**Spacer Row (1 row):**
- Blank row, height: 15px

**Total rows per TOM section:** 7 rows (1 header + 5 fields + 1 spacer)

### 6.4 Complete Row Layout (O1-O10)

**O1 - Policies & Procedures (Rows 4-10):**
- Row 4: Section header "O1 - POLICIES & PROCEDURES"
- Row 5: Policies in Place | [User input]
- Row 6: Training/Communication | [User input]
- Row 7: Governance Structure | [User input]
- Row 8: Monitoring Method | [User input]
- Row 9: Improvement Process | [User input]
- Row 10: [Blank spacer]

**O2 - Staff Training & Awareness (Rows 11-17):**
- Row 11: Section header "O2 - STAFF TRAINING & AWARENESS"
- Row 12: Policies in Place | [User input]
- Row 13: Training/Communication | [User input]
- Row 14: Governance Structure | [User input]
- Row 15: Monitoring Method | [User input]
- Row 16: Improvement Process | [User input]
- Row 17: [Blank spacer]

**O3 - Incident Response & Breach Notification (Rows 18-24):**
- Row 18: Section header "O3 - INCIDENT RESPONSE & BREACH NOTIFICATION"
- Row 19-23: Field rows
- Row 24: Spacer

**O4 - Vendor Management (Rows 25-31):**
- Row 25: Section header "O4 - VENDOR MANAGEMENT"
- Row 26-30: Field rows
- Row 31: Spacer

**O5 - Data Protection by Design/Default (Rows 32-38):**
- Row 32: Section header "O5 - DATA PROTECTION BY DESIGN/DEFAULT"
- Row 33-37: Field rows
- Row 38: Spacer

**O6 - Accountability & Governance (Rows 39-45):**
- Row 39: Section header "O6 - ACCOUNTABILITY & GOVERNANCE"
- Row 40-44: Field rows
- Row 45: Spacer

**O7 - Risk Management (Rows 46-52):**
- Row 46: Section header "O7 - RISK MANAGEMENT"
- Row 47-51: Field rows
- Row 52: Spacer

**O8 - Compliance Monitoring & Audit (Rows 53-59):**
- Row 53: Section header "O8 - COMPLIANCE MONITORING & AUDIT"
- Row 54-58: Field rows
- Row 59: Spacer

**O9 - Documentation & Records (Rows 60-66):**
- Row 60: Section header "O9 - DOCUMENTATION & RECORDS"
- Row 61-65: Field rows
- Row 66: Spacer

**O10 - Business Continuity (Rows 67-73):**
- Row 67: Section header "O10 - BUSINESS CONTINUITY"
- Row 68-72: Field rows
- Row 73: Spacer

### 6.5 Field Label Styling (Column A:B - Merged)

- Font: Calibri 10pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Top, Wrap Text
- Border: Thin black on all sides
- Width: A=15, B=15
- Height: 60px (allows multiline labels)
- Protection: Locked

### 6.6 User Input Styling (Column C:F - Merged)

- Font: Calibri 10pt, Regular, Black
- Fill: #FFFFCC (Light Yellow)
- Alignment: Left, Top, Wrap Text
- Border: Thin gray on all sides
- Width: C=25, D=25, E=25, F=25
- Minimum Height: 60px (allows ~3-4 lines of text)
- Protection: Unlocked
- Text Wrap: Enabled

### 6.7 Section Header Styling

- Font: Calibri 12pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Left, Vertical Center
- Border: Thin black on all sides
- Height: 30px
- Protection: Locked

### 6.8 Data Validation

**No dropdown validation on Sheet 4** (all fields are free-text multiline input)

### 6.9 Conditional Formatting

**No conditional formatting on Sheet 4** (pure data entry, no status-based coloring)

### 6.10 Sheet Protection

**Sheet 4 Protection:** OFF (user data entry sheet)
- Individual cell protection: ON for section headers and field labels (locked)
- Individual cell protection: OFF for user input cells (Column C:F merged cells unlocked)

### 6.11 Freeze Panes

**Freeze:** Row 4 (header rows 1-3 always visible when scrolling)

### 6.12 Helper Instructions (Row 74)

**Row 74:** [Blank spacer, height: 15px]

**Row 75:** "COMPLETION NOTES:" (instruction header)
- Merged: A75:F75
- Font: Calibri 11pt, Bold, Black
- Fill: #FFEB9C (Yellow)
- Alignment: Left, Vertical Center
- Height: 25px

**Row 76:** Instruction text
- Merged: A76:F76
- Font: Calibri 10pt, Regular, Black
- Fill: #FFEB9C (Yellow)
- Alignment: Left, Top, Wrap Text
- Height: Auto
- Text: "Complete all 5 fields for each organizational measure (O1-O10). Be specific: include policy names/versions/dates, training completion rates, governance meeting frequency, monitoring KPIs, and continuous improvement mechanisms. For detailed guidance and examples, see User Completion Guide (PART 1, Section 4.4)."

---

## 7. Integration Notes for Developers

### 7.1 Cross-Sheet Formulas

**Sheet 8 (Dashboard) formulas reference:**
- Sheet 2 Column D (Implementation Status) via COUNTIF
- Sheet 2 Column H (Effectiveness Rating) via COUNTIF
- Sheet 5 Column G (Verification Status) via COUNTIF
- Sheet 6 Column F (Overall Risk) via COUNTIF
- Sheet 7 Column H (Status) via COUNTIF

**Example formula from Sheet 8:**
```excel
='2. TOM Control Inventory'!D5:D24
```

**Important:** Use exact sheet names (including sheet number prefix) in formulas to avoid errors if user renames sheets.

### 7.2 Named Ranges (Optional Enhancement)

**Consider defining named ranges for key columns to simplify formulas:**
- `TOM_Implementation_Status` = '2. TOM Control Inventory'!$D$5:$D$24
- `TOM_Effectiveness_Rating` = '2. TOM Control Inventory'!$H$5:$H$24
- `TOM_Risk_Level` = '2. TOM Control Inventory'!$K$5:$K$24
- `Evidence_Verification_Status` = '5. Evidence Repository'!$G$2:$G$1001
- `Gap_Overall_Risk` = '6. Gap Analysis'!$F$2:$F$201
- `Action_Status` = '7. Remediation Action Plan'!$H$2:$H$201

**Usage in formulas:**
```excel
=COUNTIF(TOM_Implementation_Status,"Implemented")
```

### 7.3 Data Validation List Sources

**For maintainability, consider storing dropdown lists in a hidden sheet named "Lookup_Lists":**

**Lookup_Lists Sheet Structure:**
- Column A: Implementation_Status (Implemented, Partially Implemented, Planned, Not Implemented)
- Column B: Effectiveness_Rating (Effective, Partially Effective, Ineffective, Not Tested)
- Column C: Risk_Level (Critical, High, Medium, Low, N/A)
- Column D: Verification_Status (Verified, Pending Verification, Invalid, Expired)
- Column E: Action_Status (Not Started, In Progress, Blocked, Complete, Cancelled)

**Data Validation Source Reference:**
```
=Lookup_Lists!$A$2:$A$5  (Implementation Status)
=Lookup_Lists!$B$2:$B$5  (Effectiveness Rating)
=Lookup_Lists!$C$2:$C$6  (Risk Level)
```

### 7.4 Python Script Integration Points

**Workbook Generation Script:** `generate_a5344_toms_assessment.py`

**Key Functions:**
```python
def create_workbook():
    """Initialize workbook with 8 sheets"""
    
def setup_styles():
    """Define all cell styles, fonts, fills, borders"""
    
def create_sheet1_instructions():
    """Generate Instructions & Legend sheet (read-only)"""
    
def create_sheet2_inventory():
    """Generate TOM Control Inventory with pre-filled data"""
    # Pre-populate Columns A-C (TOM ID, Category, Type)
    # Set up data validation for Columns D, H, K
    # Apply conditional formatting
    # Protect pre-filled cells
    
def create_sheet3_technical_deep_dive():
    """Generate Technical Measures Deep-Dive (T1-T10 sections)"""
    # Create 10 sections (7 rows each = 70 rows total)
    # Set up section headers, field labels, input cells
    
def create_sheet4_organizational_deep_dive():
    """Generate Organizational Measures Deep-Dive (O1-O10 sections)"""
    # Create 10 sections (7 rows each = 70 rows total)
    # Set up section headers, field labels, input cells
```

**Customization Points (marked with `# CUSTOMIZE:` in script):**
- Sheet names (if organizational naming differs)
- Dropdown options (if additional statuses needed)
- Color codes (if organizational branding differs)
- Column widths (if different monitor resolutions)
- Protection passwords

---

## 8. Quality Assurance Notes

### 8.1 Pre-Generation Validation Checklist

Before generating workbook, verify:
- [ ] All 20 TOMs defined in Sheet 1
- [ ] All 20 TOMs pre-populated in Sheet 2 (Columns A-C)
- [ ] All 10 technical measures have sections in Sheet 3
- [ ] All 10 organizational measures have sections in Sheet 4
- [ ] All dropdown validation lists correct
- [ ] All conditional formatting formulas correct (test with sample data)
- [ ] All cell protection settings correct
- [ ] All freeze panes configured
- [ ] All column widths optimized for readability
- [ ] All row heights sufficient for multiline content

### 8.2 Post-Generation Testing Checklist

After generating workbook, test:
- [ ] Open workbook in Excel 2016, 2019, Office 365 (compatibility test)
- [ ] Test all dropdowns (select each option, verify color changes)
- [ ] Test conditional formatting (enter test data, verify highlighting)
- [ ] Test data validation (enter invalid data, verify error messages)
- [ ] Test cell protection (try editing locked cells, verify blocked)
- [ ] Test formulas in Sheet 8 (enter test data in Sheet 2, verify calculations)
- [ ] Test freeze panes (scroll right/down, verify headers remain visible)
- [ ] Save workbook, reopen, verify all settings preserved

### 8.3 User Acceptance Testing Scenarios

**Scenario 1: Complete Assessment for 1 TOM (T1 Encryption)**
- Select implementation status "Partially Implemented" → Verify green/yellow color
- Enter implementation date → Verify date format accepted
- Enter description → Verify text wraps correctly
- Enter evidence reference "EV-T1-001" → Verify accepted
- Select effectiveness "Effective" → Verify green color
- Enter test date → Verify date format accepted
- Enter gap description → Verify multiline text wraps
- Select risk level "Medium" → Verify yellow color
- Enter remediation plan → Verify multiline text wraps
- Enter owner name → Verify accepted
- Enter target date → Verify date format accepted

**Scenario 2: Test Validation Rules**
- Attempt to enter invalid implementation date (year 3000) → Verify rejected
- Attempt to enter past date in target completion → Verify rejected
- Attempt to select non-existent dropdown option → Verify not possible
- Leave required dropdown blank → Verify error message (if configured)

**Scenario 3: Test Protection**
- Attempt to edit TOM ID (Column A) → Verify blocked
- Attempt to edit TOM Category (Column B) → Verify blocked
- Attempt to delete row → Verify blocked (if sheet protection ON)
- Attempt to insert column → Verify blocked (if sheet protection ON)

---

## Appendix A: Excel Formula Reference

### A.1 Formulas Used in Sheet 8 (Dashboard)

**Implementation Rate:**
```excel
=(COUNTIF('2. TOM Control Inventory'!D5:D24,"Implemented") + 
  COUNTIF('2. TOM Control Inventory'!D5:D24,"Partially Implemented")*0.5) / 20
```

**Effectiveness Rate:**
```excel
=COUNTIF('2. TOM Control Inventory'!H5:H24,"Effective") / 
 (COUNTIF('2. TOM Control Inventory'!D5:D24,"Implemented") + 
  COUNTIF('2. TOM Control Inventory'!D5:D24,"Partially Implemented"))
```

**Critical Gaps Count:**
```excel
=COUNTIF('6. Gap Analysis'!F2:F201,"Critical")
```

**Remediation Progress:**
```excel
=COUNTIF('7. Remediation Action Plan'!H2:H201,"Complete") / 
 (COUNTA('7. Remediation Action Plan'!A2:A201) - 
  COUNTIF('7. Remediation Action Plan'!H2:H201,"Cancelled"))
```

**GDPR Art. 32 Compliance Score:**
```excel
=AVERAGE(
  (Implementation_Rate * 0.4),
  (Effectiveness_Rate * 0.3),
  ((1 - (COUNTIF('6. Gap Analysis'!F2:F201,"Critical") / 20)) * 0.2),
  (Remediation_Progress * 0.1)
)
```

### A.2 Conditional Formatting Formula Reference

**Overdue Implementation Date:**
```excel
=AND($E5<>"", $E5<TODAY(), $D5<>"Implemented")
```

**Stale Test Date (>90 days old):**
```excel
=AND($I5<>"", $I5<TODAY()-90, $H5<>"Not Tested")
```

**Overdue Remediation Target:**
```excel
=AND($N5<>"", $N5<TODAY(), $K5<>"N/A")
```

---

## 9. Sheet 5: Evidence Repository

### 9.1 Sheet Purpose
Centralized repository documenting all evidence proving TOM implementation and effectiveness. Each TOM should have 5-10 evidence items (100-200 total).

### 9.2 Sheet Layout

**Row 1:** "EVIDENCE REPOSITORY"
- Merged: A1:I1
- Font: Calibri 14pt, Bold, White
- Fill: #1F4E78 (Dark Blue)
- Alignment: Center, Vertical Center
- Height: 40px

**Row 2:** "Document all evidence proving TOM implementation and effectiveness (minimum 5 items per TOM)"
- Merged: A2:I2
- Font: Calibri 11pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Center, Vertical Center
- Height: 25px

**Row 3:** [Blank spacer row, height: 15px]

### 9.3 Column Headers (Row 4)

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Evidence ID | 15 | Text (auto-generated) | None (locked) |
| B | TOM ID | 12 | Text | None |
| C | Evidence Type | 35 | Dropdown | 17 options (see below) |
| D | Description | 50 | Text (multiline) | None |
| E | File Location / System | 60 | Text (multiline) | None |
| F | Evidence Date | 15 | Date | YYYY-MM-DD |
| G | Verification Status | 20 | Dropdown | 4 options (see below) |
| H | Verified By | 25 | Text | None |
| I | Notes | 50 | Text (multiline) | None |

**Header Row Styling:**
- Font: Calibri 10pt, Bold, White
- Fill: #1F4E78 (Dark Blue)
- Alignment: Center, Vertical Center, Wrap Text
- Border: Thin black on all sides
- Height: 60px

### 9.4 Data Rows (Rows 5-1004)

**Row Range:** 1,000 evidence entries (Rows 5-1004)

**Column A - Evidence ID (Auto-Generated Formula):**
```excel
="EV-"&TEXT(ROW()-4,"000")
```
- Row 5: EV-001
- Row 6: EV-002
- Row 1004: EV-1000

**Cell Styling:**
- Font: Calibri 10pt, Regular, #505050 (Dark Gray)
- Fill: #D9D9D9 (Light Gray)
- Alignment: Center, Vertical Center
- Border: Thin gray on all sides
- Protection: Locked (formula cell)

**Columns B-I (User Input Cells):**
- Font: Calibri 10pt, Regular, Black
- Fill: #FFFFCC (Light Yellow) when empty
- Alignment: Left (text), Center (dropdowns, dates), Vertical Center
- Border: Thin gray on all sides
- Protection: Unlocked
- Text Wrap: Enabled for columns D, E, I
- Minimum Row Height: 45px (allows 2-3 lines of text)

### 9.5 Data Validation Rules

**Column C - Evidence Type:**
```
Validation Type: List
Source: ="Configuration Screenshot,Policy Document,Training Report,Audit Report,Test Results,Vendor Assessment,Incident Response Test,System Log Extract,Certificate,DPA,Risk Assessment,DPIA,Penetration Test Report,Vulnerability Scan,Business Continuity Test,Disaster Recovery Test,Other"
Error Style: Stop
Error Message: "Please select a valid evidence type from the list"
Input Message: "Select the type of evidence being documented"
Allow Blank: No
Applies To: C5:C1004
```

**Column F - Evidence Date:**
```
Validation Type: Date
Data: Between
Start Date: 2000-01-01
End Date: =TODAY()+30
Error Style: Stop
Error Message: "Evidence date must be between 2000 and today (or next 30 days for planned evidence)"
Input Message: "Enter the date this evidence was created or captured (YYYY-MM-DD)"
Allow Blank: No
Applies To: F5:F1004
```

**Column G - Verification Status:**
```
Validation Type: List
Source: ="Verified,Pending Verification,Invalid,Expired"
Error Style: Stop
Error Message: "Please select a valid verification status"
Input Message: "Select verification status: Verified (evidence reviewed and adequate), Pending Verification (awaiting review), Invalid (inadequate quality or relevance), Expired (evidence is outdated and needs refresh)"
Allow Blank: No
Applies To: G5:G1004
```

### 9.6 Conditional Formatting Rules

**Rule 1: Verification Status Color Coding**
```
Applies To: G5:G1004
Rule Type: Cell Value
Conditions:
- Cell Value = "Verified" → Fill: #C6EFCE (Green), Font: Black
- Cell Value = "Pending Verification" → Fill: #FFEB9C (Yellow), Font: Black
- Cell Value = "Invalid" → Fill: #FFC7CE (Red), Font: Black
- Cell Value = "Expired" → Fill: #FFA500 (Orange), Font: Black
Stop If True: Yes
```

**Rule 2: Stale Evidence Date Warning**
```
Applies To: F5:F1004
Rule Type: Formula
Formula: =AND(F5<>"", F5<TODAY()-365, G5="Verified")
Format: Fill: #FFEB9C (Yellow), Font: Black
Stop If True: Yes
Description: Highlights evidence dates older than 1 year that are still marked "Verified" (technical evidence should be <3 months old, organizational <12 months)
```

**Rule 3: Future Date Error**
```
Applies To: F5:F1004
Rule Type: Formula
Formula: =AND(F5<>"", F5>TODAY()+30)
Format: Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
Stop If True: Yes
Description: Highlights evidence dates more than 30 days in the future (likely data entry error)
```

### 9.7 Helper Instructions (Row 1005)

**Row 1005:** [Blank spacer, height: 15px]

**Row 1006:** "EVIDENCE DOCUMENTATION NOTES:" (instruction header)
- Merged: A1006:I1006
- Font: Calibri 11pt, Bold, Black
- Fill: #FFEB9C (Yellow)
- Alignment: Left, Vertical Center
- Height: 25px

**Row 1007:** Instruction text
- Merged: A1007:I1007
- Font: Calibri 10pt, Regular, Black
- Fill: #FFEB9C (Yellow)
- Alignment: Left, Top, Wrap Text
- Height: Auto
- Text: "Document minimum 5 evidence items per TOM (100+ total for 20 TOMs). Evidence ID auto-generates (do not edit Column A). Link evidence to TOM ID in Column B (T1-T10, O1-O10). Technical evidence freshness: <3 months. Organizational evidence freshness: <12 months. Store evidence files in centralized repository (SharePoint/network drive). Reference file location in Column E (e.g., SharePoint > Security > TOMs Evidence > T1-Encryption). All evidence requires verification by DPO, CISO, or Internal Auditor. For detailed evidence collection guidance and examples, see User Completion Guide (PART 1, Section 5)."

### 9.8 Sheet Protection

**Sheet 5 Protection:** OFF (user data entry sheet)
- Individual cell protection: ON for Column A (Evidence ID formula locked)
- Individual cell protection: OFF for Columns B-I (user input unlocked)

### 9.9 Freeze Panes

**Freeze:** Row 5, Column B
- Rows 1-4 always visible (headers)
- Column A always visible (Evidence ID)

---

## 10. Sheet 6: Gap Analysis & Risk Assessment

### 10.1 Sheet Purpose
Document all identified gaps from Sheet 2 with comprehensive risk assessment using likelihood × impact matrix. All Medium/High/Critical risks require remediation plans.

### 10.2 Sheet Layout

**Row 1:** "GAP ANALYSIS & RISK ASSESSMENT"
- Merged: A1:J1
- Font: Calibri 14pt, Bold, White
- Fill: #1F4E78 (Dark Blue)
- Alignment: Center, Vertical Center
- Height: 40px

**Row 2:** "Assess risk for all identified gaps using likelihood × impact matrix (see Sheet 1)"
- Merged: A2:J2
- Font: Calibri 11pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Center, Vertical Center
- Height: 25px

**Row 3:** [Blank spacer row, height: 15px]

### 10.3 Column Headers (Row 4)

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Gap ID | 12 | Text (user input) | None |
| B | TOM ID | 12 | Text | None |
| C | Gap Description | 60 | Text (multiline) | None |
| D | Likelihood | 15 | Dropdown | High, Medium, Low |
| E | Impact | 15 | Dropdown | Critical, High, Medium, Low |
| F | Overall Risk | 15 | Formula | Auto-calculated |
| G | Risk Score | 10 | Formula | 1-4 numeric |
| H | Remediation Priority | 20 | Formula | Auto-calculated SLA |
| I | Residual Risk | 20 | Dropdown | Critical, High, Medium, Low, N/A |
| J | Acceptance Justification | 50 | Text (multiline) | None |

**Header Row Styling:**
- Font: Calibri 10pt, Bold, White
- Fill: #1F4E78 (Dark Blue)
- Alignment: Center, Vertical Center, Wrap Text
- Border: Thin black on all sides
- Height: 60px

### 10.4 Data Rows (Rows 5-204)

**Row Range:** 200 gap entries (Rows 5-204)

**Column A - Gap ID (User Input):**
- Format: GAP-[TOM ID]-### (e.g., GAP-T1-001, GAP-T1-002, GAP-O4-001)
- User manually enters following format convention
- Font: Calibri 10pt, Bold, Black
- Fill: #FFFFCC (Light Yellow)
- Alignment: Center, Vertical Center

**Column F - Overall Risk (Formula):**
```excel
=IF(AND(D5="High", OR(E5="High", E5="Critical")), "Critical",
  IF(AND(D5="Medium", E5="Critical"), "Critical",
    IF(OR(AND(D5="High", E5="Medium"), AND(D5="Medium", E5="High")), "High",
      IF(OR(AND(D5="Low", E5="High"), AND(D5="Medium", E5="Medium")), "Medium",
        IF(OR(AND(D5="Low", E5="Medium"), AND(D5="High", E5="Low")), "Low",
          IF(AND(D5="Low", E5="Low"), "Low", ""))))))
```
- Font: Calibri 10pt, Bold, Black
- Fill: Risk-based color (conditional formatting)
- Alignment: Center, Vertical Center
- Protection: Locked (formula cell)

**Column G - Risk Score (Formula):**
```excel
=IF(F5="Critical", 4, IF(F5="High", 3, IF(F5="Medium", 2, IF(F5="Low", 1, 0))))
```
- Font: Calibri 10pt, Bold, Black
- Fill: #FFFFFF (White)
- Alignment: Center, Vertical Center
- Protection: Locked (formula cell)

**Column H - Remediation Priority (Formula):**
```excel
=IF(G5=4, "URGENT (30 days)", IF(G5=3, "HIGH (90 days)", IF(G5=2, "MEDIUM (6 months)", IF(G5=1, "LOW (12 months)", ""))))
```
- Font: Calibri 10pt, Bold, Black
- Fill: Priority-based color (conditional formatting)
- Alignment: Center, Vertical Center
- Protection: Locked (formula cell)

### 10.5 Data Validation Rules

**Column D - Likelihood:**
```
Validation Type: List
Source: ="High,Medium,Low"
Error Style: Stop
Error Message: "Please select High, Medium, or Low"
Input Message: "Assess likelihood of gap being exploited: High (likely within 12 months), Medium (possible within 12-24 months), Low (unlikely within 24+ months)"
Allow Blank: No
Applies To: D5:D204
```

**Column E - Impact:**
```
Validation Type: List
Source: ="Critical,High,Medium,Low"
Error Style: Stop
Error Message: "Please select Critical, High, Medium, or Low"
Input Message: "Assess potential impact if gap exploited: Critical (>100K PII records, business-ending), High (10K-100K records, significant harm), Medium (1K-10K records, manageable harm), Low (<1K records, minimal harm)"
Allow Blank: No
Applies To: E5:E204
```

**Column I - Residual Risk:**
```
Validation Type: List
Source: ="Critical,High,Medium,Low,N/A"
Error Style: Stop
Error Message: "Please select a valid residual risk level or N/A"
Input Message: "Select expected risk level AFTER remediation is complete. Use N/A if risk is accepted without remediation."
Allow Blank: Yes
Applies To: I5:I204
```

### 10.6 Conditional Formatting Rules

**Rule 1: Overall Risk Color Coding (Column F)**
```
Applies To: F5:F204
Rule Type: Cell Value
Conditions:
- Cell Value = "Critical" → Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
- Cell Value = "High" → Fill: #FFA500 (Orange), Font: Black
- Cell Value = "Medium" → Fill: #FFEB9C (Yellow), Font: Black
- Cell Value = "Low" → Fill: #C6EFCE (Green), Font: Black
Stop If True: Yes
```

**Rule 2: Remediation Priority Color Coding (Column H)**
```
Applies To: H5:H204
Rule Type: Cell Value
Conditions:
- Cell Value = "URGENT (30 days)" → Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
- Cell Value = "HIGH (90 days)" → Fill: #FFA500 (Orange), Font: Black
- Cell Value = "MEDIUM (6 months)" → Fill: #FFEB9C (Yellow), Font: Black
- Cell Value = "LOW (12 months)" → Fill: #C6EFCE (Green), Font: Black
Stop If True: Yes
```

**Rule 3: Residual Risk Color Coding (Column I)**
```
Applies To: I5:I204
Rule Type: Cell Value
Conditions:
- Cell Value = "Critical" → Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
- Cell Value = "High" → Fill: #FFA500 (Orange), Font: Black
- Cell Value = "Medium" → Fill: #FFEB9C (Yellow), Font: Black
- Cell Value = "Low" → Fill: #C6EFCE (Green), Font: Black
Stop If True: Yes
```

**Rule 4: Missing Residual Risk Warning**
```
Applies To: I5:I204
Rule Type: Formula
Formula: =AND(F5<>"", I5="", J5="")
Format: Fill: #FFEB9C (Yellow), Font: Black
Stop If True: Yes
Description: Highlights gaps that need either remediation plan (Sheet 7) OR risk acceptance justification (Column J)
```

### 10.7 Helper Instructions (Row 205)

**Row 205:** [Blank spacer, height: 15px]

**Row 206:** "GAP ANALYSIS NOTES:" (instruction header)
- Merged: A206:J206
- Font: Calibri 11pt, Bold, Black
- Fill: #FFEB9C (Yellow)
- Alignment: Left, Vertical Center
- Height: 25px

**Row 207:** Instruction text
- Merged: A207:J207
- Font: Calibri 10pt, Regular, Black
- Fill: #FFEB9C (Yellow)
- Alignment: Left, Top, Wrap Text
- Height: Auto
- Text: "Document ALL gaps identified in Sheet 2 Column J. Use risk matrix from Sheet 1 (likelihood × impact). Formulas in Columns F-H auto-calculate risk level, risk score, and remediation priority. Critical/High risks REQUIRE remediation plans in Sheet 7 (30-90 day SLA). Medium risks should be remediated (6 month SLA). Low risks may be accepted with executive approval and justification in Column J. For detailed risk assessment guidance, likelihood/impact definitions, and examples, see User Completion Guide (PART 1, Section 4.6)."

### 10.8 Sheet Protection

**Sheet 6 Protection:** OFF (user data entry sheet)
- Individual cell protection: ON for Columns F, G, H (formula cells locked)
- Individual cell protection: OFF for Columns A-E, I-J (user input unlocked)

### 10.9 Freeze Panes

**Freeze:** Row 5, Column C
- Rows 1-4 always visible (headers)
- Columns A-B always visible (Gap ID, TOM ID)

---

## 11. Sheet 7: Remediation Action Plan

### 11.1 Sheet Purpose
Track remediation actions for closing gaps with ownership, timelines, status tracking, and progress monitoring.

### 11.2 Sheet Layout

**Row 1:** "REMEDIATION ACTION PLAN"
- Merged: A1:J1
- Font: Calibri 14pt, Bold, White
- Fill: #1F4E78 (Dark Blue)
- Alignment: Center, Vertical Center
- Height: 40px

**Row 2:** "Define and track remediation actions for all Medium/High/Critical risk gaps"
- Merged: A2:J2
- Font: Calibri 11pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Center, Vertical Center
- Height: 25px

**Row 3:** [Blank spacer row, height: 15px]

### 11.3 Column Headers (Row 4)

| Column | Header | Width | Data Type | Validation |
|--------|--------|-------|-----------|------------|
| A | Action ID | 12 | Text (user input) | None |
| B | TOM ID | 12 | Text | None |
| C | Gap Description | 50 | Text (multiline) | None |
| D | Proposed Solution | 60 | Text (multiline) | None |
| E | Owner | 25 | Text | None |
| F | Start Date | 12 | Date | YYYY-MM-DD |
| G | Target Date | 12 | Date | YYYY-MM-DD |
| H | Status | 20 | Dropdown | 5 options (see below) |
| I | % Complete | 10 | Number | 0-100 |
| J | Completion Date | 12 | Date | YYYY-MM-DD |

**Header Row Styling:**
- Font: Calibri 10pt, Bold, White
- Fill: #1F4E78 (Dark Blue)
- Alignment: Center, Vertical Center, Wrap Text
- Border: Thin black on all sides
- Height: 60px

### 11.4 Data Rows (Rows 5-204)

**Row Range:** 200 action entries (Rows 5-204)

**Column A - Action ID (User Input):**
- Format: ACT-[TOM ID]-### (e.g., ACT-T1-001, ACT-T1-002, ACT-O4-001)
- User manually enters following format convention
- Font: Calibri 10pt, Bold, Black
- Fill: #FFFFCC (Light Yellow)
- Alignment: Center, Vertical Center

**Column D - Proposed Solution (User Input - Critical Field):**
- Detailed remediation plan with:
  - **Phase breakdown** (e.g., Phase 1: Requirements, Phase 2: Procurement, Phase 3: Implementation, Phase 4: Testing, Phase 5: Production)
  - **Timeline** (specific dates for each phase)
  - **Budget** (cost estimate with breakdown)
  - **Risks** (implementation risks and mitigation strategies)
  - **Alternatives** (alternative solutions considered and why rejected)
- Minimum length: 3-5 paragraphs
- Font: Calibri 10pt, Regular, Black
- Fill: #FFFFCC (Light Yellow)
- Alignment: Left, Top, Wrap Text
- Minimum Row Height: 100px (allows ~6-8 lines)

**Column H - Status (Dropdown):**
- Options: Not Started, In Progress, Blocked, Complete, Cancelled
- Font: Calibri 10pt, Regular, Black
- Fill: Status-based color (conditional formatting)
- Alignment: Center, Vertical Center

### 11.5 Data Validation Rules

**Column F - Start Date:**
```
Validation Type: Date
Data: Between
Start Date: =TODAY()-365
End Date: =TODAY()+730
Error Style: Stop
Error Message: "Start date must be between 1 year ago and 2 years from today"
Input Message: "Enter remediation project start date (YYYY-MM-DD)"
Allow Blank: Yes
Applies To: F5:F204
```

**Column G - Target Date:**
```
Validation Type: Date
Data: Between
Start Date: =TODAY()
End Date: =TODAY()+730
Error Style: Stop
Error Message: "Target date must be between today and 2 years from today"
Input Message: "Enter target completion date (YYYY-MM-DD). SLA based on risk: Critical (30-60 days), High (90-180 days), Medium (6-12 months), Low (12-24 months)"
Allow Blank: No
Applies To: G5:G204
```

**Column H - Status:**
```
Validation Type: List
Source: ="Not Started,In Progress,Blocked,Complete,Cancelled"
Error Style: Stop
Error Message: "Please select a valid status from the list"
Input Message: "Select status: Not Started (future project), In Progress (active work), Blocked (impediment preventing progress), Complete (remediation finished and validated), Cancelled (action cancelled - risk accepted or alternative solution)"
Allow Blank: No
Applies To: H5:H204
```

**Column I - % Complete:**
```
Validation Type: Whole Number
Data: Between
Minimum: 0
Maximum: 100
Error Style: Stop
Error Message: "% Complete must be between 0 and 100"
Input Message: "Enter project completion percentage (0-100%)"
Allow Blank: Yes
Applies To: I5:I204
```

**Column J - Completion Date:**
```
Validation Type: Date
Data: Between
Start Date: 2000-01-01
End Date: =TODAY()+30
Error Style: Stop
Error Message: "Completion date must be between 2000 and today (or next 30 days)"
Input Message: "Enter actual completion date (YYYY-MM-DD) when Status = Complete. Must update Sheet 2 (implementation status), Sheet 5 (add evidence), Sheet 6 (update residual risk)."
Allow Blank: Yes
Applies To: J5:J204
```

### 11.6 Conditional Formatting Rules

**Rule 1: Status Color Coding (Column H)**
```
Applies To: H5:H204
Rule Type: Cell Value
Conditions:
- Cell Value = "Complete" → Fill: #C6EFCE (Green), Font: Black, Bold
- Cell Value = "In Progress" → Fill: #B4C7E7 (Light Blue), Font: Black
- Cell Value = "Blocked" → Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
- Cell Value = "Not Started" → Fill: #D9D9D9 (Gray), Font: Black
- Cell Value = "Cancelled" → Fill: #FFFFFF (White), Font: #808080 (Gray), Strikethrough
Stop If True: Yes
```

**Rule 2: Overdue Actions Highlighting (Column G)**
```
Applies To: G5:G204
Rule Type: Formula
Formula: =AND(G5<>"", G5<TODAY(), H5="In Progress")
Format: Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
Stop If True: Yes
Description: Highlights target dates that have passed for actions still in progress (overdue)
```

**Rule 3: Approaching Deadline Warning (Column G)**
```
Applies To: G5:G204
Rule Type: Formula
Formula: =AND(G5<>"", G5<=TODAY()+30, G5>=TODAY(), H5="In Progress")
Format: Fill: #FFEB9C (Yellow), Font: Black
Stop If True: Yes
Description: Highlights target dates within 30 days for in-progress actions (deadline approaching)
```

**Rule 4: Progress Bar Coloring (Column I)**
```
Applies To: I5:I204
Rule Type: 3-Color Scale
Minimum: 0%, Color: #FFC7CE (Red)
Midpoint: 50%, Color: #FFEB9C (Yellow)
Maximum: 100%, Color: #C6EFCE (Green)
Description: Visual progress bar based on % complete
```

**Rule 5: Missing Completion Date (Column J)**
```
Applies To: J5:J204
Rule Type: Formula
Formula: =AND(H5="Complete", J5="")
Format: Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
Stop If True: Yes
Description: Highlights missing completion date when status is "Complete"
```

**Rule 6: Invalid Date Range (Column G)**
```
Applies To: G5:G204
Rule Type: Formula
Formula: =AND(F5<>"", G5<>"", G5<F5)
Format: Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
Stop If True: Yes
Description: Highlights invalid date range (target date before start date)
```

### 11.7 Helper Instructions (Row 205)

**Row 205:** [Blank spacer, height: 15px]

**Row 206:** "REMEDIATION ACTION NOTES:" (instruction header)
- Merged: A206:J206
- Font: Calibri 11pt, Bold, Black
- Fill: #FFEB9C (Yellow)
- Alignment: Left, Vertical Center
- Height: 25px

**Row 207:** Instruction text
- Merged: A207:J207
- Font: Calibri 10pt, Regular, Black
- Fill: #FFEB9C (Yellow)
- Alignment: Left, Top, Wrap Text
- Height: Auto
- Text: "Create remediation actions for ALL Medium/High/Critical risk gaps from Sheet 6. SLA based on risk: Critical (30-60 days), High (90-180 days), Medium (6-12 months), Low (12-24 months). Proposed Solution (Column D) MUST be detailed with 5 components: (1) Phase breakdown, (2) Timeline with dates, (3) Budget with cost estimate, (4) Risks and mitigation strategies, (5) Alternative solutions considered. Update Status and % Complete monthly during active remediation. When Status = Complete: (a) Update Sheet 2 Column D (implementation status), (b) Add evidence to Sheet 5, (c) Update Sheet 6 Column I (residual risk). For detailed remediation planning guidance, phase templates, and examples, see User Completion Guide (PART 1, Section 4.7)."

### 11.8 Sheet Protection

**Sheet 7 Protection:** OFF (user data entry sheet)
- All cells unlocked (user input throughout)

### 11.9 Freeze Panes

**Freeze:** Row 5, Column C
- Rows 1-4 always visible (headers)
- Columns A-B always visible (Action ID, TOM ID)

---

## 12. Sheet 8: Compliance Dashboard

### 12.1 Sheet Purpose
Executive summary of TOM compliance with auto-calculated metrics, KPIs, and GDPR Art. 32 compliance score. **NO USER DATA ENTRY** - all formulas referencing Sheets 2-7.

### 12.2 Sheet Layout

**Row 1:** "COMPLIANCE DASHBOARD - EXECUTIVE SUMMARY"
- Merged: A1:F1
- Font: Calibri 14pt, Bold, White
- Fill: #1F4E78 (Dark Blue)
- Alignment: Center, Vertical Center
- Height: 40px

**Row 2:** "Auto-calculated metrics from Sheets 2-7 (no data entry required)"
- Merged: A2:F2
- Font: Calibri 11pt, Bold, White
- Fill: #305496 (Medium Blue)
- Alignment: Center, Vertical Center
- Height: 25px

**Row 3:** [Blank spacer row, height: 15px]

### 12.3 Section 1: Implementation Status (Rows 4-13)

**Row 4:** "SECTION 1: IMPLEMENTATION STATUS" (section header)
- Merged: A4:F4
- Font: Calibri 12pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Vertical Center
- Height: 25px

**Metrics Table (Rows 5-12):**

| Row | Metric (A:C Merged) | Value (D) | Formula/Notes (E:F Merged) |
|-----|---------------------|-----------|----------------------------|
| 5 | Total TOMs | 20 | =20 |
| 6 | Implemented | [Formula] | =COUNTIF('2. TOM Control Inventory'!D5:D24,"Implemented") |
| 7 | Partially Implemented | [Formula] | =COUNTIF('2. TOM Control Inventory'!D5:D24,"Partially Implemented") |
| 8 | Planned | [Formula] | =COUNTIF('2. TOM Control Inventory'!D5:D24,"Planned") |
| 9 | Not Implemented | [Formula] | =COUNTIF('2. TOM Control Inventory'!D5:D24,"Not Implemented") |
| 10 | [blank] | [blank] | [blank] |
| 11 | **Implementation Rate** | [Formula] | **=(D6+D7\*0.5)/D5** |
| 12 | Target Interpretation | ≥90% | Green ≥90% / Yellow 80-89% / Red <80% |

**Column D11 (Implementation Rate) Styling:**
- Font: Calibri 12pt, Bold, Black
- Number Format: 0% (percentage, no decimals)
- Alignment: Center, Vertical Center
- Conditional Formatting (see below)

**Column D11 Conditional Formatting:**
```
Applies To: D11
Rule Type: Cell Value
Conditions:
- Cell Value ≥ 0.90 → Fill: #C6EFCE (Green), Font: Black, Bold
- Cell Value ≥ 0.80 AND < 0.90 → Fill: #FFEB9C (Yellow), Font: Black, Bold
- Cell Value < 0.80 → Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
Stop If True: Yes
```

**Row 13:** [Blank spacer, height: 15px]

### 12.4 Section 2: Technical vs. Organizational (Rows 14-23)

**Row 14:** "SECTION 2: TECHNICAL VS. ORGANIZATIONAL MEASURES" (section header)
- Merged: A14:F14
- Font: Calibri 12pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Vertical Center
- Height: 25px

**Metrics Table (Rows 15-22):**

| Row | Metric (A:C Merged) | Value (D) | Formula/Notes (E:F Merged) |
|-----|---------------------|-----------|----------------------------|
| 15 | Technical Measures Total | 10 | =10 |
| 16 | Technical Implemented | [Formula] | =COUNTIFS('2. TOM Control Inventory'!C5:C14,"Technical",'2. TOM Control Inventory'!D5:D14,"Implemented") |
| 17 | Technical Implementation Rate | [Formula] | =D16/D15 |
| 18 | [blank] | [blank] | [blank] |
| 19 | Organizational Measures Total | 10 | =10 |
| 20 | Organizational Implemented | [Formula] | =COUNTIFS('2. TOM Control Inventory'!C15:C24,"Organizational",'2. TOM Control Inventory'!D15:D24,"Implemented") |
| 21 | Organizational Implementation Rate | [Formula] | =D20/D19 |
| 22 | Analysis | [Formula] | =IF(D17>D21,"Technical measures ahead","Organizational measures ahead") |

**Row 23:** [Blank spacer, height: 15px]

### 12.5 Section 3: Control Effectiveness (Rows 24-34)

**Row 24:** "SECTION 3: CONTROL EFFECTIVENESS" (section header)
- Merged: A24:F24
- Font: Calibri 12pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Vertical Center
- Height: 25px

**Metrics Table (Rows 25-33):**

| Row | Metric (A:C Merged) | Value (D) | Formula/Notes (E:F Merged) |
|-----|---------------------|-----------|----------------------------|
| 25 | Effective Controls | [Formula] | =COUNTIF('2. TOM Control Inventory'!H5:H24,"Effective") |
| 26 | Partially Effective | [Formula] | =COUNTIF('2. TOM Control Inventory'!H5:H24,"Partially Effective") |
| 27 | Ineffective Controls | [Formula] | =COUNTIF('2. TOM Control Inventory'!H5:H24,"Ineffective") |
| 28 | Not Tested | [Formula] | =COUNTIF('2. TOM Control Inventory'!H5:H24,"Not Tested") |
| 29 | Total Implemented | [Formula] | =COUNTIF('2. TOM Control Inventory'!D5:D24,"Implemented")+COUNTIF('2. TOM Control Inventory'!D5:D24,"Partially Implemented") |
| 30 | [blank] | [blank] | [blank] |
| 31 | **Effectiveness Rate** | [Formula] | **=D25/D29** |
| 32 | Testing Coverage | [Formula] | =(D25+D26+D27)/D29 |
| 33 | Target Interpretation | ≥95% | Green ≥95% / Yellow 85-94% / Red <85% |

**Column D31 (Effectiveness Rate) Conditional Formatting:**
```
Applies To: D31
Rule Type: Cell Value
Conditions:
- Cell Value ≥ 0.95 → Fill: #C6EFCE (Green), Font: Black, Bold
- Cell Value ≥ 0.85 AND < 0.95 → Fill: #FFEB9C (Yellow), Font: Black, Bold
- Cell Value < 0.85 → Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
Stop If True: Yes
```

**Row 34:** [Blank spacer, height: 15px]

### 12.6 Section 4: Gap Analysis (Rows 35-45)

**Row 35:** "SECTION 4: GAP ANALYSIS" (section header)
- Merged: A35:F35
- Font: Calibri 12pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Vertical Center
- Height: 25px

**Metrics Table (Rows 36-44):**

| Row | Metric (A:C Merged) | Value (D) | Formula/Notes (E:F Merged) |
|-----|---------------------|-----------|----------------------------|
| 36 | Critical Gaps | [Formula] | =COUNTIF('6. Gap Analysis'!F5:F204,"Critical") |
| 37 | High Gaps | [Formula] | =COUNTIF('6. Gap Analysis'!F5:F204,"High") |
| 38 | Medium Gaps | [Formula] | =COUNTIF('6. Gap Analysis'!F5:F204,"Medium") |
| 39 | Low Gaps | [Formula] | =COUNTIF('6. Gap Analysis'!F5:F204,"Low") |
| 40 | Total Gaps | [Formula] | =COUNTA('6. Gap Analysis'!A5:A204) |
| 41 | [blank] | [blank] | [blank] |
| 42 | Average Risk Score | [Formula] | =AVERAGE('6. Gap Analysis'!G5:G204) |
| 43 | Gaps per TOM | [Formula] | =D40/20 |
| 44 | Target Interpretation | Critical=0, High≤3, Avg Score≤2.0 | See targets |

**Column D36 (Critical Gaps) Conditional Formatting:**
```
Applies To: D36
Rule Type: Cell Value
Conditions:
- Cell Value = 0 → Fill: #C6EFCE (Green), Font: Black, Bold
- Cell Value ≥ 1 → Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
Stop If True: Yes
```

**Row 45:** [Blank spacer, height: 15px]

### 12.7 Section 5: Remediation Progress (Rows 46-57)

**Row 46:** "SECTION 5: REMEDIATION PROGRESS" (section header)
- Merged: A46:F46
- Font: Calibri 12pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Vertical Center
- Height: 25px

**Metrics Table (Rows 47-56):**

| Row | Metric (A:C Merged) | Value (D) | Formula/Notes (E:F Merged) |
|-----|---------------------|-----------|----------------------------|
| 47 | Total Actions | [Formula] | =COUNTA('7. Remediation Action Plan'!A5:A204) |
| 48 | Not Started | [Formula] | =COUNTIF('7. Remediation Action Plan'!H5:H204,"Not Started") |
| 49 | In Progress | [Formula] | =COUNTIF('7. Remediation Action Plan'!H5:H204,"In Progress") |
| 50 | Blocked | [Formula] | =COUNTIF('7. Remediation Action Plan'!H5:H204,"Blocked") |
| 51 | Complete | [Formula] | =COUNTIF('7. Remediation Action Plan'!H5:H204,"Complete") |
| 52 | Cancelled | [Formula] | =COUNTIF('7. Remediation Action Plan'!H5:H204,"Cancelled") |
| 53 | Overdue Actions | [Formula] | =COUNTIFS('7. Remediation Action Plan'!H5:H204,"In Progress",'7. Remediation Action Plan'!G5:G204,"<"&TODAY()) |
| 54 | [blank] | [blank] | [blank] |
| 55 | **Remediation Progress** | [Formula] | **=D51/(D47-D52)** |
| 56 | Target Interpretation | ≥80% | Green ≥80% / Yellow 60-79% / Red <60% |

**Column D55 (Remediation Progress) Conditional Formatting:**
```
Applies To: D55
Rule Type: Cell Value
Conditions:
- Cell Value ≥ 0.80 → Fill: #C6EFCE (Green), Font: Black, Bold
- Cell Value ≥ 0.60 AND < 0.80 → Fill: #FFEB9C (Yellow), Font: Black, Bold
- Cell Value < 0.60 → Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
Stop If True: Yes
```

**Row 57:** [Blank spacer, height: 15px]

### 12.8 Section 6: GDPR Art. 32 Compliance Score (Rows 58-71)

**Row 58:** "SECTION 6: GDPR ARTICLE 32 COMPLIANCE SCORE" (section header)
- Merged: A58:F58
- Font: Calibri 14pt, Bold, White
- Fill: #1F4E78 (Dark Blue)
- Alignment: Center, Vertical Center
- Height: 30px

**Formula Components (Rows 59-62):**

| Row | Component (A:C Merged) | Weight | Calculation (D:F Merged) |
|-----|------------------------|--------|--------------------------|
| 59 | Implementation Rate | 40% | =D11 |
| 60 | Effectiveness Rate | 30% | =D31 |
| 61 | Critical Gaps Factor | 20% | =(1-(D36/20)) |
| 62 | Remediation Progress | 10% | =D55 |

**Final Score (Row 64):**

| Row | Metric (A:C Merged) | Value (D) | Formula (E:F Merged) |
|-----|---------------------|-----------|----------------------|
| 64 | **GDPR Art. 32 Compliance Score** | [Formula] | **=(D59\*0.4)+(D60\*0.3)+(D61\*0.2)+(D62\*0.1)** |

**Detailed Formula Breakdown:**
```excel
=(D11*0.4) +          // Implementation Rate × 40%
 (D31*0.3) +          // Effectiveness Rate × 30%
 ((1-(D36/20))*0.2) + // Critical Gap Factor × 20% (inverted - fewer gaps = higher score)
 (D55*0.1)            // Remediation Progress × 10%
```

**Column D64 Styling:**
- Font: Calibri 16pt, Bold, White
- Number Format: 0% (percentage, no decimals)
- Alignment: Center, Vertical Center
- Border: Thick black border on all sides
- Height: 35px

**Column D64 Conditional Formatting (5-level scale):**
```
Applies To: D64
Rule Type: Cell Value
Conditions:
- Cell Value ≥ 0.90 → Fill: #006400 (Dark Green), Font: White, Bold
- Cell Value ≥ 0.80 AND < 0.90 → Fill: #C6EFCE (Light Green), Font: Black, Bold
- Cell Value ≥ 0.70 AND < 0.80 → Fill: #FFEB9C (Yellow), Font: Black, Bold
- Cell Value ≥ 0.60 AND < 0.70 → Fill: #FFA500 (Orange), Font: Black, Bold
- Cell Value < 0.60 → Fill: #C00000 (Dark Red), Font: White, Bold
Stop If True: Yes
```

**Interpretation Table (Rows 66-70):**

| Row | Score Range (A:B Merged) | Interpretation (C:F Merged) |
|-----|--------------------------|----------------------------|
| 66 | 90-100% | Excellent compliance - Best-in-class TOMs, minimal GDPR Art. 32 risk |
| 67 | 80-89% | Good compliance - Acceptable controls, minor improvements needed |
| 68 | 70-79% | Fair compliance - Significant gaps, improvement program required |
| 69 | 60-69% | Poor compliance - Major deficiencies, urgent remediation required |
| 70 | <60% | Critical non-compliance - Material GDPR Art. 32 violation risk, supervisory authority intervention likely |

**Row 71:** [Blank spacer, height: 15px]

### 12.9 Section 7: Evidence Summary (Rows 72-79)

**Row 72:** "SECTION 7: EVIDENCE SUMMARY" (section header)
- Merged: A72:F72
- Font: Calibri 12pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Vertical Center
- Height: 25px

**Metrics Table (Rows 73-78):**

| Row | Metric (A:C Merged) | Value (D) | Formula/Notes (E:F Merged) |
|-----|---------------------|-----------|----------------------------|
| 73 | Total Evidence Items | [Formula] | =COUNTA('5. Evidence Repository'!A5:A1004) |
| 74 | Verified Evidence | [Formula] | =COUNTIF('5. Evidence Repository'!G5:G1004,"Verified") |
| 75 | Pending Verification | [Formula] | =COUNTIF('5. Evidence Repository'!G5:G1004,"Pending Verification") |
| 76 | Expired Evidence | [Formula] | =COUNTIF('5. Evidence Repository'!G5:G1004,"Expired") |
| 77 | **Evidence Verification Rate** | [Formula] | **=D74/D73** |
| 78 | Target Interpretation | ≥95%, Min 100 items | Green ≥95% / Yellow 85-94% / Red <85% |

**Column D77 (Evidence Verification Rate) Conditional Formatting:**
```
Applies To: D77
Rule Type: Cell Value
Conditions:
- Cell Value ≥ 0.95 → Fill: #C6EFCE (Green), Font: Black, Bold
- Cell Value ≥ 0.85 AND < 0.95 → Fill: #FFEB9C (Yellow), Font: Black, Bold
- Cell Value < 0.85 → Fill: #FFC7CE (Red), Font: #C00000 (Dark Red), Bold
Stop If True: Yes
```

**Row 79:** [Blank spacer, height: 20px]

### 12.10 Chart Recommendations (Rows 80-90)

**Row 80:** "VISUAL DASHBOARD RECOMMENDATIONS" (section header)
- Merged: A80:F80
- Font: Calibri 12pt, Bold, Black
- Fill: #D9D9D9 (Light Gray)
- Alignment: Left, Vertical Center
- Height: 25px

**Row 81:** Instructions
- Merged: A81:F81
- Font: Calibri 10pt, Italic, Black
- Fill: #FFFFFF (White)
- Alignment: Left, Vertical Center
- Text: "Insert charts manually after workbook generation using Excel's Insert > Chart. Recommended visualizations:"

**Chart Recommendations (Rows 82-87):**

| Row | Chart Name (A:B Merged) | Chart Type (C:D Merged) | Data Range (E:F Merged) |
|-----|-------------------------|-------------------------|-------------------------|
| 82 | TOM Implementation Status | Pie Chart | Data: D6:D9, Labels: A6:A9 |
| 83 | Gap Risk Distribution | Horizontal Bar Chart | Data: D36:D39, Labels: A36:A39 |
| 84 | Remediation Status | Stacked Bar Chart | Data: D48:D52, Labels: A48:A52 |
| 85 | Technical vs. Organizational | Clustered Column Chart | Data: D16,D17,D20,D21 |
| 86 | GDPR Compliance Score | Gauge Chart or Large Data Bar | Data: D64 (single value) |
| 87 | Effectiveness Testing | Donut Chart | Data: D25:D28, Labels: A25:A28 |

**Row 88-90:** Reserved space for manual chart insertion
- Height: 150px total
- Fill: #F2F2F2 (Very Light Gray) - indicates chart placeholder area

### 12.11 Sheet Protection

**Sheet 8 Protection:** ON (formula-driven, read-only)
- Password: `[Set during workbook generation]`
- All cells locked
- Allow: Select locked cells, Select unlocked cells
- Disallow: Everything else

### 12.12 Freeze Panes

**Freeze:** Row 4 (header rows 1-3 always visible)

---

## 13. Python Script Architecture

### 13.1 Complete Script

**Filename:** `generate_a5344_toms_assessment.py`

```python
#!/usr/bin/env python3
"""
ISMS-IMP-A.5.34.4 - Technical and Organizational Measures (TOMs) Assessment
Workbook Generator

Generates complete 8-sheet Excel workbook for assessing implementation and
effectiveness of 20 Technical and Organizational Measures protecting PII.

ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII
GDPR Article 32: Security of Processing
Swiss FADP Article 8: Data Security

Version: 2.0
Date: 2026-01-29
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment, Protection
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from datetime import datetime
import os

# Configuration
OUTPUT_DIR = "/mnt/user-data/outputs"
PROTECTION_PASSWORD = "privacy2024"  # CUSTOMIZE: Change if needed

# 20 TOMs (pre-populated data)
TOMS = [
    ("T1", "Encryption", "Technical"),
    ("T2", "Access Control", "Technical"),
    ("T3", "Pseudonymization/Anonymization", "Technical"),
    ("T4", "Data Minimization", "Technical"),
    ("T5", "Security Monitoring & Logging", "Technical"),
    ("T6", "Network Security", "Technical"),
    ("T7", "Application Security", "Technical"),
    ("T8", "Endpoint Security", "Technical"),
    ("T9", "Backup & Recovery", "Technical"),
    ("T10", "Physical Security", "Technical"),
    ("O1", "Policies & Procedures", "Organizational"),
    ("O2", "Staff Training & Awareness", "Organizational"),
    ("O3", "Incident Response & Breach Notification", "Organizational"),
    ("O4", "Vendor Management", "Organizational"),
    ("O5", "Data Protection by Design/Default", "Organizational"),
    ("O6", "Accountability & Governance", "Organizational"),
    ("O7", "Risk Management", "Organizational"),
    ("O8", "Compliance Monitoring & Audit", "Organizational"),
    ("O9", "Documentation & Records", "Organizational"),
    ("O10", "Business Continuity", "Organizational"),
]

# Color palette
COLORS = {
    'dark_blue': 'FF1F4E78',
    'medium_blue': 'FF305496',
    'light_blue': 'FFB4C7E7',
    'green': 'FFC6EFCE',
    'yellow': 'FFFFEB9C',
    'red': 'FFFFC7CE',
    'dark_red': 'FFC00000',
    'orange': 'FFFFA500',
    'white': 'FFFFFFFF',
    'gray': 'FFD9D9D9',
    'input_yellow': 'FFFFFFCC',
    'dark_gray': 'FF505050',
}

def create_workbook():
    """Initialize workbook with 8 sheets."""
    wb = Workbook()
    wb.remove(wb.active)  # Remove default sheet
    
    sheet_names = [
        "1. Instructions & Legend",
        "2. TOM Control Inventory",
        "3. Technical Measures Deep-Dive",
        "4. Organizational Measures Deep-Dive",
        "5. Evidence Repository",
        "6. Gap Analysis & Risk Assessment",
        "7. Remediation Action Plan",
        "8. Compliance Dashboard",
    ]
    
    for name in sheet_names:
        wb.create_sheet(name)
    
    return wb

def apply_header(ws, row, text, merge_range, level=1):
    """Apply header styling."""
    ws.merge_cells(merge_range)
    cell = ws[merge_range.split(':')[0]]
    cell.value = text
    
    if level == 1:
        cell.font = Font(name='Calibri', size=14, bold=True, color=COLORS['white'])
        cell.fill = PatternFill(start_color=COLORS['dark_blue'], end_color=COLORS['dark_blue'], fill_type='solid')
        ws.row_dimensions[row].height = 40
    else:
        cell.font = Font(name='Calibri', size=11, bold=True, color=COLORS['white'])
        cell.fill = PatternFill(start_color=COLORS['medium_blue'], end_color=COLORS['medium_blue'], fill_type='solid')
        ws.row_dimensions[row].height = 25
    
    cell.alignment = Alignment(horizontal='center', vertical='center')

def create_sheet2_inventory(wb):
    """Generate Sheet 2: TOM Control Inventory."""
    ws = wb["2. TOM Control Inventory"]
    
    # Headers
    apply_header(ws, 1, "TOM CONTROL INVENTORY - 20 TECHNICAL AND ORGANIZATIONAL MEASURES", "A1:N1", level=1)
    apply_header(ws, 2, "Assess implementation status and effectiveness for all 20 TOMs", "A2:N2", level=2)
    ws.row_dimensions[3].height = 15
    
    # Column headers (Row 4)
    headers = [
        ("A4", "TOM ID", 8),
        ("B4", "TOM Category", 35),
        ("C4", "TOM Type", 15),
        ("D4", "Implementation Status", 20),
        ("E4", "Implementation Date", 15),
        ("F4", "Description of Implementation", 80),
        ("G4", "Evidence Reference", 20),
        ("H4", "Effectiveness Rating", 20),
        ("I4", "Last Test Date", 15),
        ("J4", "Gaps Identified", 60),
        ("K4", "Risk Level", 15),
        ("L4", "Remediation Plan", 60),
        ("M4", "Remediation Owner", 25),
        ("N4", "Target Completion Date", 15),
    ]
    
    for cell_ref, header_text, width in headers:
        ws[cell_ref] = header_text
        ws[cell_ref].font = Font(name='Calibri', size=10, bold=True, color=COLORS['white'])
        ws[cell_ref].fill = PatternFill(start_color=COLORS['dark_blue'], end_color=COLORS['dark_blue'], fill_type='solid')
        ws[cell_ref].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        col_letter = cell_ref[0]
        ws.column_dimensions[col_letter].width = width
    
    ws.row_dimensions[4].height = 60
    
    # Pre-populate TOMs (Columns A-C, Rows 5-24)
    for idx, (tom_id, tom_category, tom_type) in enumerate(TOMS, start=5):
        ws[f'A{idx}'] = tom_id
        ws[f'B{idx}'] = tom_category
        ws[f'C{idx}'] = tom_type
        
        for col in ['A', 'B', 'C']:
            cell = ws[f'{col}{idx}']
            cell.font = Font(name='Calibri', size=10, color=COLORS['dark_gray'])
            cell.fill = PatternFill(start_color=COLORS['gray'], end_color=COLORS['gray'], fill_type='solid')
            cell.alignment = Alignment(horizontal='center' if col == 'A' else 'left', vertical='center')
            cell.protection = Protection(locked=True)
    
    # Data validation
    dv_impl = DataValidation(type="list", formula1='"Implemented,Partially Implemented,Planned,Not Implemented"', allow_blank=False)
    ws.add_data_validation(dv_impl)
    dv_impl.add('D5:D24')
    
    dv_eff = DataValidation(type="list", formula1='"Effective,Partially Effective,Ineffective,Not Tested"', allow_blank=False)
    ws.add_data_validation(dv_eff)
    dv_eff.add('H5:H24')
    
    dv_risk = DataValidation(type="list", formula1='"Critical,High,Medium,Low,N/A"', allow_blank=True)
    ws.add_data_validation(dv_risk)
    dv_risk.add('K5:K24')
    
    # Conditional formatting
    ws.conditional_formatting.add('D5:D24',
        CellIsRule(operator='equal', formula=['"Implemented"'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['green'], end_color=COLORS['green'], fill_type='solid')))
    ws.conditional_formatting.add('D5:D24',
        CellIsRule(operator='equal', formula=['"Partially Implemented"'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['yellow'], end_color=COLORS['yellow'], fill_type='solid')))
    ws.conditional_formatting.add('D5:D24',
        CellIsRule(operator='equal', formula=['"Planned"'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['light_blue'], end_color=COLORS['light_blue'], fill_type='solid')))
    ws.conditional_formatting.add('D5:D24',
        CellIsRule(operator='equal', formula=['"Not Implemented"'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['red'], end_color=COLORS['red'], fill_type='solid')))
    
    # Freeze panes
    ws.freeze_panes = 'D5'
    
    return ws

def create_sheet5_evidence(wb):
    """Generate Sheet 5: Evidence Repository."""
    ws = wb["5. Evidence Repository"]
    
    apply_header(ws, 1, "EVIDENCE REPOSITORY", "A1:I1", level=1)
    apply_header(ws, 2, "Document all evidence proving TOM implementation and effectiveness (minimum 5 items per TOM)", "A2:I2", level=2)
    ws.row_dimensions[3].height = 15
    
    # Column headers
    headers = [
        ("A4", "Evidence ID", 15),
        ("B4", "TOM ID", 12),
        ("C4", "Evidence Type", 35),
        ("D4", "Description", 50),
        ("E4", "File Location / System", 60),
        ("F4", "Evidence Date", 15),
        ("G4", "Verification Status", 20),
        ("H4", "Verified By", 25),
        ("I4", "Notes", 50),
    ]
    
    for cell_ref, header_text, width in headers:
        ws[cell_ref] = header_text
        ws[cell_ref].font = Font(name='Calibri', size=10, bold=True, color=COLORS['white'])
        ws[cell_ref].fill = PatternFill(start_color=COLORS['dark_blue'], end_color=COLORS['dark_blue'], fill_type='solid')
        ws[cell_ref].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        col_letter = cell_ref[0]
        ws.column_dimensions[col_letter].width = width
    
    ws.row_dimensions[4].height = 60
    
    # Evidence ID formula (Column A, Rows 5-1004)
    for row in range(5, 1005):
        ws[f'A{row}'] = f'=CONCATENATE("EV-",TEXT(ROW()-4,"000"))'
        ws[f'A{row}'].font = Font(name='Calibri', size=10, color=COLORS['dark_gray'])
        ws[f'A{row}'].fill = PatternFill(start_color=COLORS['gray'], end_color=COLORS['gray'], fill_type='solid')
        ws[f'A{row}'].alignment = Alignment(horizontal='center', vertical='center')
        ws[f'A{row}'].protection = Protection(locked=True)
    
    # Data validation
    dv_type = DataValidation(type="list",
        formula1='"Configuration Screenshot,Policy Document,Training Report,Audit Report,Test Results,Vendor Assessment,Incident Response Test,System Log Extract,Certificate,DPA,Risk Assessment,DPIA,Penetration Test Report,Vulnerability Scan,Business Continuity Test,Disaster Recovery Test,Other"',
        allow_blank=False)
    ws.add_data_validation(dv_type)
    dv_type.add('C5:C1004')
    
    dv_verify = DataValidation(type="list", formula1='"Verified,Pending Verification,Invalid,Expired"', allow_blank=False)
    ws.add_data_validation(dv_verify)
    dv_verify.add('G5:G1004')
    
    # Conditional formatting
    ws.conditional_formatting.add('G5:G1004',
        CellIsRule(operator='equal', formula=['"Verified"'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['green'], end_color=COLORS['green'], fill_type='solid')))
    ws.conditional_formatting.add('G5:G1004',
        CellIsRule(operator='equal', formula=['"Pending Verification"'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['yellow'], end_color=COLORS['yellow'], fill_type='solid')))
    ws.conditional_formatting.add('G5:G1004',
        CellIsRule(operator='equal', formula=['"Invalid"'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['red'], end_color=COLORS['red'], fill_type='solid')))
    ws.conditional_formatting.add('G5:G1004',
        CellIsRule(operator='equal', formula=['"Expired"'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['orange'], end_color=COLORS['orange'], fill_type='solid')))
    
    ws.freeze_panes = 'B5'
    return ws

def create_sheet6_gaps(wb):
    """Generate Sheet 6: Gap Analysis."""
    ws = wb["6. Gap Analysis & Risk Assessment"]
    
    apply_header(ws, 1, "GAP ANALYSIS & RISK ASSESSMENT", "A1:J1", level=1)
    apply_header(ws, 2, "Assess risk for all identified gaps using likelihood × impact matrix (see Sheet 1)", "A2:J2", level=2)
    ws.row_dimensions[3].height = 15
    
    # Column headers
    headers = [
        ("A4", "Gap ID", 12),
        ("B4", "TOM ID", 12),
        ("C4", "Gap Description", 60),
        ("D4", "Likelihood", 15),
        ("E4", "Impact", 15),
        ("F4", "Overall Risk", 15),
        ("G4", "Risk Score", 10),
        ("H4", "Remediation Priority", 20),
        ("I4", "Residual Risk", 20),
        ("J4", "Acceptance Justification", 50),
    ]
    
    for cell_ref, header_text, width in headers:
        ws[cell_ref] = header_text
        ws[cell_ref].font = Font(name='Calibri', size=10, bold=True, color=COLORS['white'])
        ws[cell_ref].fill = PatternFill(start_color=COLORS['dark_blue'], end_color=COLORS['dark_blue'], fill_type='solid')
        ws[cell_ref].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        col_letter = cell_ref[0]
        ws.column_dimensions[col_letter].width = width
    
    ws.row_dimensions[4].height = 60
    
    # Risk formulas (Columns F-H, Rows 5-204)
    for row in range(5, 205):
        # Overall Risk formula
        ws[f'F{row}'] = f'=IF(AND(D{row}="High", OR(E{row}="High", E{row}="Critical")), "Critical", IF(AND(D{row}="Medium", E{row}="Critical"), "Critical", IF(OR(AND(D{row}="High", E{row}="Medium"), AND(D{row}="Medium", E{row}="High")), "High", IF(OR(AND(D{row}="Low", E{row}="High"), AND(D{row}="Medium", E{row}="Medium")), "Medium", IF(OR(AND(D{row}="Low", E{row}="Medium"), AND(D{row}="High", E{row}="Low")), "Low", IF(AND(D{row}="Low", E{row}="Low"), "Low", ""))))))'
        ws[f'F{row}'].protection = Protection(locked=True)
        
        # Risk Score formula
        ws[f'G{row}'] = f'=IF(F{row}="Critical", 4, IF(F{row}="High", 3, IF(F{row}="Medium", 2, IF(F{row}="Low", 1, 0))))'
        ws[f'G{row}'].protection = Protection(locked=True)
        
        # Remediation Priority formula
        ws[f'H{row}'] = f'=IF(G{row}=4, "URGENT (30 days)", IF(G{row}=3, "HIGH (90 days)", IF(G{row}=2, "MEDIUM (6 months)", IF(G{row}=1, "LOW (12 months)", ""))))'
        ws[f'H{row}'].protection = Protection(locked=True)
    
    # Data validation
    dv_likelihood = DataValidation(type="list", formula1='"High,Medium,Low"', allow_blank=False)
    ws.add_data_validation(dv_likelihood)
    dv_likelihood.add('D5:D204')
    
    dv_impact = DataValidation(type="list", formula1='"Critical,High,Medium,Low"', allow_blank=False)
    ws.add_data_validation(dv_impact)
    dv_impact.add('E5:E204')
    
    dv_residual = DataValidation(type="list", formula1='"Critical,High,Medium,Low,N/A"', allow_blank=True)
    ws.add_data_validation(dv_residual)
    dv_residual.add('I5:I204')
    
    # Conditional formatting
    ws.conditional_formatting.add('F5:F204',
        CellIsRule(operator='equal', formula=['"Critical"'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['red'], end_color=COLORS['red'], fill_type='solid'),
                  font=Font(color=COLORS['dark_red'], bold=True)))
    ws.conditional_formatting.add('F5:F204',
        CellIsRule(operator='equal', formula=['"High"'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['orange'], end_color=COLORS['orange'], fill_type='solid')))
    ws.conditional_formatting.add('F5:F204',
        CellIsRule(operator='equal', formula=['"Medium"'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['yellow'], end_color=COLORS['yellow'], fill_type='solid')))
    ws.conditional_formatting.add('F5:F204',
        CellIsRule(operator='equal', formula=['"Low"'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['green'], end_color=COLORS['green'], fill_type='solid')))
    
    ws.freeze_panes = 'C5'
    return ws

def create_sheet8_dashboard(wb):
    """Generate Sheet 8: Compliance Dashboard."""
    ws = wb["8. Compliance Dashboard"]
    
    apply_header(ws, 1, "COMPLIANCE DASHBOARD - EXECUTIVE SUMMARY", "A1:F1", level=1)
    apply_header(ws, 2, "Auto-calculated metrics from Sheets 2-7 (no data entry required)", "A2:F2", level=2)
    ws.row_dimensions[3].height = 15
    
    # Section 1: Implementation Status
    ws.merge_cells('A4:F4')
    ws['A4'] = "SECTION 1: IMPLEMENTATION STATUS"
    ws['A4'].font = Font(name='Calibri', size=12, bold=True)
    ws['A4'].fill = PatternFill(start_color=COLORS['gray'], end_color=COLORS['gray'], fill_type='solid')
    ws['A4'].alignment = Alignment(horizontal='left', vertical='center')
    ws.row_dimensions[4].height = 25
    
    metrics_s1 = [
        (5, "Total TOMs", "=20"),
        (6, "Implemented", "=COUNTIF('2. TOM Control Inventory'!D5:D24,\"Implemented\")"),
        (7, "Partially Implemented", "=COUNTIF('2. TOM Control Inventory'!D5:D24,\"Partially Implemented\")"),
        (8, "Planned", "=COUNTIF('2. TOM Control Inventory'!D5:D24,\"Planned\")"),
        (9, "Not Implemented", "=COUNTIF('2. TOM Control Inventory'!D5:D24,\"Not Implemented\")"),
        (11, "Implementation Rate", "=(D6+D7*0.5)/D5"),
    ]
    
    for row, metric, formula in metrics_s1:
        ws.merge_cells(f'A{row}:C{row}')
        ws[f'A{row}'] = metric
        ws[f'D{row}'] = formula
        
        if row == 11:
            ws[f'D{row}'].font = Font(name='Calibri', size=12, bold=True)
            ws[f'D{row}'].number_format = '0%'
    
    # Section 6: GDPR Compliance Score (Row 64)
    ws.merge_cells('A64:C64')
    ws['A64'] = "GDPR Art. 32 Compliance Score"
    ws['A64'].font = Font(name='Calibri', size=12, bold=True)
    
    ws['D64'] = "=(D11*0.4)+(D31*0.3)+((1-(D36/20))*0.2)+(D55*0.1)"
    ws['D64'].font = Font(name='Calibri', size=16, bold=True, color=COLORS['white'])
    ws['D64'].number_format = '0%'
    ws.row_dimensions[64].height = 35
    
    # Conditional formatting for D64
    ws.conditional_formatting.add('D64',
        CellIsRule(operator='greaterThanOrEqual', formula=['0.9'], stopIfTrue=True,
                  fill=PatternFill(start_color='FF006400', end_color='FF006400', fill_type='solid'),
                  font=Font(color=COLORS['white'], bold=True)))
    ws.conditional_formatting.add('D64',
        CellIsRule(operator='greaterThanOrEqual', formula=['0.8'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['green'], end_color=COLORS['green'], fill_type='solid'),
                  font=Font(bold=True)))
    ws.conditional_formatting.add('D64',
        CellIsRule(operator='greaterThanOrEqual', formula=['0.7'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['yellow'], end_color=COLORS['yellow'], fill_type='solid'),
                  font=Font(bold=True)))
    ws.conditional_formatting.add('D64',
        CellIsRule(operator='greaterThanOrEqual', formula=['0.6'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['orange'], end_color=COLORS['orange'], fill_type='solid'),
                  font=Font(bold=True)))
    ws.conditional_formatting.add('D64',
        CellIsRule(operator='lessThan', formula=['0.6'], stopIfTrue=True,
                  fill=PatternFill(start_color=COLORS['dark_red'], end_color=COLORS['dark_red'], fill_type='solid'),
                  font=Font(color=COLORS['white'], bold=True)))
    
    # Protect sheet
    ws.protection.sheet = True
    ws.protection.password = PROTECTION_PASSWORD
    
    ws.freeze_panes = 'A4'
    return ws

def main():
    """Main execution."""
    print("=" * 80)
    print("ISMS-IMP-A.5.34.4 - TOMs Assessment Workbook Generator v2.0")
    print("=" * 80)
    print()
    
    wb = create_workbook()
    
    print("Generating Sheet 2: TOM Control Inventory...")
    create_sheet2_inventory(wb)
    
    print("Generating Sheet 5: Evidence Repository...")
    create_sheet5_evidence(wb)
    
    print("Generating Sheet 6: Gap Analysis & Risk Assessment...")
    create_sheet6_gaps(wb)
    
    print("Generating Sheet 8: Compliance Dashboard...")
    create_sheet8_dashboard(wb)
    
    # Save
    today = datetime.now().strftime("%Y%m%d")
    filename = f"ISMS_A_5_34_4_TOMs_Assessment_{today}.xlsx"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    print(f"Saving workbook: {filename}...")
    wb.save(filepath)
    
    print()
    print("=" * 80)
    print("✅ Workbook generation complete!")
    print(f"📁 File: {filepath}")
    print("=" * 80)
    print()
    print("Next Steps:")
    print("1. Complete Sheet 2 (TOM Control Inventory) - rate all 20 TOMs")
    print("2. Complete Sheets 3-4 (Deep-Dive) - document details")
    print("3. Complete Sheet 5 (Evidence Repository) - minimum 100 items")
    print("4. Complete Sheet 6 (Gap Analysis) - assess all gaps")
    print("5. Complete Sheet 7 (Remediation Action Plan) - define actions")
    print("6. Review Sheet 8 (Compliance Dashboard) - verify GDPR score ≥80%")
    print()

if __name__ == "__main__":
    main()
```

---

**END OF PART 3**

**Total Deliverables:**
- Sheet 5: Evidence Repository (1,000 rows, auto-ID generation)
- Sheet 6: Gap Analysis (200 rows, risk matrix formulas)
- Sheet 7: Remediation Action Plan (200 rows, status tracking)
- Sheet 8: Compliance Dashboard (7 sections, GDPR Art. 32 score)
- Complete Python script (openpyxl implementation)

**Quality Level:** REFERENCE QUALITY - Developer-ready specifications with exact formulas, conditional formatting, and Python implementation.

**END OF ISMS-IMP-A.5.34.4**