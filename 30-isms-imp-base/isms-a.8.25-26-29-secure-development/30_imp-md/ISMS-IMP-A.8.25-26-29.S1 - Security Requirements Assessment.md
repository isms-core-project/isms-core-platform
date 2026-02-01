**ISMS-IMP-A.8.25-26-29-S1**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.25: Secure Development Life Cycle

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.25-26-29-S1 |
| **Version** | 1.0 |
| **Assessment Area** | Security Requirements Compliance (A.8.26) |
| **Related Policy** | ISMS-POL-A.8.25-26-29 Section 2 (Application Security Requirements) |
| **Purpose** | Assessment workbook for evaluating application security requirements specification, threat modeling, and architecture review compliance |
| **Target Audience** | Security Architects, Product Managers, Application Owners, Compliance Officers |
| **Assessment Type** | Application-by-Application Security Requirements Verification |
| **Review Cycle** | Quarterly (High-Risk), Annually (Medium/Low-Risk) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guide format | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Question-by-Question Guidance
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Column Specifications
  - Formulas & Calculations
  - Data Validation Rules
  - Conditional Formatting
  - Technical Notes for Python Script Developers


---

# PART I: USER COMPLETION GUIDE

# Assessment Overview

## What This Assessment Does

**Assessment Name:** ISMS-IMP-A.8.25-26-29-S1 - Security Requirements Assessment

**Purpose:** 
This workbook assesses whether **application security requirements are properly specified, documented, and approved** before development begins. It verifies compliance with ISO/IEC 27001:2022 Control A.8.26 (Application Security Requirements).

**What Gets Assessed:**

- ✅ Application risk classification (High/Medium/Low)
- ✅ Security Requirements Specification (SRS) existence and completeness
- ✅ Threat modeling execution (for High/Medium-Risk applications)
- ✅ Security architecture review completion
- ✅ Requirements traceability to implementation and testing
- ✅ Security requirements approval documentation


**What This Assessment Is NOT:**

- ❌ Code-level security review (that's SAST in Workbook 3)
- ❌ Security testing results (that's Workbook 3 and 4)
- ❌ SDLC security activities (that's Workbook 2)
- ❌ General compliance audit (this is application-specific requirements)


## Who Should Use This Workbook

**Primary Users:**

- **Security Architects**: Assess requirements quality and completeness
- **Product Managers**: Verify their applications have documented security requirements
- **Application Owners**: Demonstrate compliance for their applications
- **Compliance Officers**: Collect evidence for audits


**Supporting Roles:**

- **Development Managers**: Understand security requirements for their teams
- **QA Managers**: Link requirements to security test cases
- **Auditors**: Verify ISO 27001 A.8.26 compliance


## Assessment Frequency

| Application Risk | Assessment Frequency | Trigger Events |
|-----------------|---------------------|----------------|
| **High-Risk** | Quarterly | + Major releases, architecture changes |
| **Medium-Risk** | Annually | + Major releases |
| **Low-Risk** | Annually | + Significant changes |

**Ad-Hoc Assessments Triggered By:**

- Security incidents affecting application
- Major functionality additions
- Technology stack changes
- Regulatory requirement changes
- Pre-audit preparation


## Expected Time Investment

| Activity | Time Required | Responsibility |
|----------|--------------|----------------|
| **Preparation** (evidence gathering) | 2-4 hours | Application Owner + Dev Team |
| **Workbook Completion** | 1-2 hours | Security Architect / Product Manager |
| **Review & Validation** | 30-60 min | Security Architect |
| **Remediation Planning** (if gaps found) | 1-3 hours | Application Owner + Security Architect |
| **Total per Application** | 4-10 hours | Varies |

**Efficiency Tips:**

- Batch assess similar applications together
- Reuse threat models for similar architectures
- Template security requirements for common application types
- Automate evidence collection where possible


---

# Prerequisites

## Before Starting Assessment

**CRITICAL - You MUST have:**

- [ ] **Application identified and scoped**
  - Application name, ID, and description documented
  - Application boundaries clearly defined
  - Integration points identified

- [ ] **Application risk classification completed**
  - Risk score calculated using policy criteria
  - Classification documented (High/Medium/Low)
  - Classification approved by Security Architect

- [ ] **Access to application documentation**
  - Architecture diagrams (if available)
  - Requirements documents (business + technical)
  - Design documents
  - Deployment documentation

- [ ] **Access to security documentation** (if exists):
  - Security Requirements Specification (SRS)
  - Threat model
  - Security architecture review report
  - Security sign-off records

- [ ] **Contact information for stakeholders**:
  - Product Manager / Application Owner
  - Lead Developer / Architect
  - Security Architect (reviewer)


**HELPFUL - Nice to have:**

- Previous assessment results (if reassessment)
- Security testing results
- Penetration testing reports
- Compliance audit findings


## Required Knowledge

**Assessor should understand:**

- Security requirements specification best practices
- Threat modeling methodologies (STRIDE, PASTA, etc.)
- Application security principles (OWASP Top 10, secure design)
- Organizational security policies and standards
- Relevant regulations (GDPR, PCI DSS, etc.)


**If you lack this knowledge:**

- Pair with experienced Security Architect
- Review ISMS-POL-A.8.25-26-29 Section 2 first
- Use provided question-by-question guidance (Section 4)


## Tools and Access Required

- **Excel 2016+** or compatible spreadsheet software
- **Read access** to document repository (SharePoint, Confluence, etc.)
- **Read access** to application inventory
- **Contact access** to application stakeholders (for clarifications)


---

# Assessment Workflow

## High-Level Process

```
Step 1: Preparation (30-60 min)
â"'
â"œâ"€> Identify application to assess
â"œâ"€> Gather application documentation
â"œâ"€> Confirm application risk classification
â""â"€> Collect security documentation (if exists)
     â"'
     â–¼
Step 2: Workbook Completion (1-2 hours)
â"'
â"œâ"€> Sheet 1: Application Profile
â"œâ"€> Sheet 2: Risk Classification
â"œâ"€> Sheet 3: Security Requirements Documentation
â"œâ"€> Sheet 4: Threat Modeling Status
â"œâ"€> Sheet 5: Architecture Review Status
â"œâ"€> Sheet 6: Requirements Traceability
â"œâ"€> Sheet 7: Compliance Checklist
â"œâ"€> Sheet 8: Gap Analysis & Action Plan
â"œâ"€> Sheet 9: Evidence Register
â""â"€> Sheet 10: Approval & Sign-Off
     â"'
     â–¼
Step 3: Review & Validation (30-60 min)
â"'
â"œâ"€> Self-review using quality checklist (Section 7)
â"œâ"€> Security Architect peer review
â"œâ"€> Evidence validation (spot-check)
â""â"€> Score calculation verification
     â"'
     â–¼
Step 4: Gap Remediation (if needed)
â"'
â"œâ"€> Prioritize gaps (critical first)
â"œâ"€> Create remediation plan
â"œâ"€> Assign responsibilities
â""â"€> Set target dates
     â"'
     â–¼
Step 5: Approval & Closeout (15-30 min)
â"'
â"œâ"€> Application Owner reviews findings
â"œâ"€> Security Architect approves assessment
â"œâ"€> File workbook in evidence repository
â""â"€> Schedule next assessment
```

## Detailed Step-by-Step

**Step 1: Preparation**

1. **Identify Application:**

   - Application name: _______________
   - Application ID (if assigned): APP-___
   - Assessment period: From _____ To _____


2. **Confirm Risk Classification:**

   - Check application inventory for existing classification
   - If not classified, complete risk scoring (see Section 4.2)
   - Verify classification is current (< 12 months old)


3. **Gather Documentation:**

   - Application overview document
   - Security Requirements Specification (SRS) - if exists
   - Threat model - if exists
   - Security architecture review report - if exists
   - Any previous assessment results


4. **Prepare Evidence Folder:**

   - Create folder: `Evidence/APP-XXX/A.8.26_Requirements/YYYYMMDD/`
   - Stage documents for reference during assessment


**Step 2: Workbook Completion**

Complete each sheet in order (Sheet 1 → Sheet 10). Use Section 4 (Question-by-Question Guidance) for detailed help on each question.

**Key principles:**

- Answer based on **evidence**, not assumptions
- Use **specific examples** (not "Yes, we have requirements" but "Yes, SRS v2.3 dated 2025-12-01")
- Document **evidence location** for each answer
- Mark **N/A** only when truly not applicable (with justification)
- Be **honest** about gaps - that's the point of assessment


**Step 3: Review & Validation**

1. **Self-Review:**

   - Use Quality Checklist (Section 7)
   - Verify all fields completed
   - Check evidence documented
   - Validate formulas calculated correctly


2. **Peer Review:**

   - Another Security Architect reviews workbook
   - Spot-check evidence claims
   - Challenge assumptions
   - Validate compliance scoring


3. **Stakeholder Confirmation:**

   - Application Owner reviews findings
   - Confirms assessment accuracy
   - Agrees with identified gaps


**Step 4: Gap Remediation (if gaps found)**

1. **Prioritize Gaps:**

   - Critical gaps (block deployment)
   - High gaps (address before next release)
   - Medium gaps (plan remediation)
   - Low gaps (track as technical debt)


2. **Create Action Plan:**

   - Document in Sheet 8 (Gap Analysis)
   - Assign responsibility
   - Set target dates
   - Define acceptance criteria


3. **Track Progress:**

   - Update Sheet 8 as gaps remediated
   - Collect evidence of remediation
   - Re-assess to verify closure


**Step 5: Approval & Closeout**

1. **Obtain Approvals:**

   - Application Owner signs (Sheet 10)
   - Security Architect approves (Sheet 10)
   - CISO approves for High-Risk apps (Sheet 10)


2. **File Workbook:**

   - Save as: `ISMS-A826-Requirements-APP-XXX-YYYYMMDD.xlsx`
   - Store in evidence repository
   - Link to application record


3. **Schedule Next Assessment:**

   - Set reminder for next assessment date
   - Note any special triggers (major release, etc.)


---

# Question-by-Question Guidance

This section provides detailed guidance for completing each assessment question in the workbook.

## Sheet 1: Application Profile

**Purpose:** Document basic application information for context.

### Question 1.1: Application Name
**Column B: Application Name**

*What to enter:* Official application name as it appears in organizational records.

*Examples:*

- ✅ Good: "Customer Portal v2.0"
- ✅ Good: "SAP ERP Production Instance"
- ❌ Avoid: "The app", "John's project"


*Where to find:*

- Application inventory
- CMDB (Configuration Management Database)
- Project documentation


**Column C: Application ID**

*What to enter:* Unique identifier (format: APP-XXX or organizational standard)

*Examples:*

- APP-001, APP-CUST-PORTAL, APP-HR-SYS


### Question 1.2: Application Owner
**Column B: Name**

*What to enter:* Person accountable for application (usually Product Manager or Business Owner)

**Column C: Department**

*What to enter:* Organizational unit owning the application

**Column D: Contact Email**

*What to enter:* How to reach the Application Owner

*Evidence:* Application inventory record, organizational chart

### Question 1.3: Application Description
**Column B: Business Purpose**

*What to enter:* What business function does this application serve? (2-3 sentences)

*Example:*
"Customer-facing portal allowing customers to view account balances, make payments, update profile information, and request support. Processes approximately 50,000 transactions daily. Critical for customer self-service strategy."

**Column C: User Base**

*What to enter:* Who uses this application?

*Examples:*

- "External customers (~10,000 active users)"
- "Internal HR staff (25 users)"
- "B2B partners (150 companies, ~500 users)"


**Column D: Technology Stack**

*What to enter:* Key technologies (keep it high-level)

*Example:*
"Frontend: React.js, Backend: Node.js + Express, Database: PostgreSQL, Infrastructure: AWS (EC2, RDS, S3)"

*Evidence:* Application documentation, architecture diagrams, technology inventory

### Question 1.4: Data Sensitivity
**Column B: Data Types Processed**

*What to enter:* Types of data the application handles (check all that apply from dropdown or list)

*Common data types:*

- Personal Identifiable Information (PII): names, emails, addresses, phone numbers
- Financial Data: payment card data, bank accounts, transactions
- Health Data (PHI): medical records, health status
- Authentication Credentials: passwords, API keys, certificates
- Business Sensitive: trade secrets, financial reports, strategic plans
- Public Information: marketing content, public product info


**Column C: Data Classification (Highest)**

*What to enter:* Highest data classification level processed (per organizational data classification policy)

*Typical classifications:*

- **Confidential/Restricted:** PII, PHI, payment data, credentials
- **Internal Use:** Business data, operational data
- **Public:** Marketing content, public documentation


*Where to find:*

- Data flow diagrams
- Privacy Impact Assessment (PIA)
- Data classification policy
- GDPR Article 30 Records of Processing


*Why this matters:*
Data classification drives security requirements. Confidential data requires encryption, access controls, audit logging, etc.

**Column D: Regulatory Scope**

*What to enter:* Applicable regulations (check all that apply)

*Common regulations:*

- GDPR (EU residents' personal data)
- FADP (Swiss personal data)
- PCI DSS (payment card data)
- HIPAA (US healthcare data)
- SOX (financial reporting)
- Industry-specific regulations


*Evidence:* Compliance register, legal analysis, privacy assessment

### Question 1.5: Deployment Environment
**Column B: Deployment Model**

*What to enter:* Where is the application deployed?

*Options:*

- On-Premises (organization's data center)
- Cloud (AWS, Azure, GCP, etc.)
- Hybrid (mix of on-prem and cloud)
- SaaS (vendor-hosted)


**Column C: Internet Accessibility**

*What to enter:* How is the application accessed?

*Options:*

- Public Internet (anyone can reach it)
- VPN Required (remote access via VPN)
- Internal Network Only (office network)
- Air-Gapped (isolated network)


*Why this matters:*
Internet-facing applications require stronger security controls (WAF, DDoS protection, public vulnerability management).

*Evidence:* Network diagrams, deployment documentation, infrastructure inventory

---

## Sheet 2: Risk Classification

**Purpose:** Document and validate application risk classification.

### Question 2.1: Risk Scoring Criteria

This sheet contains the risk scoring matrix from the policy. You'll score each criterion 0-5, and the weighted total determines risk classification.

**Data Sensitivity (Weight: 30%)**

*Score 0-5:*

- **5:** PII + financial + healthcare data (high sensitivity, regulated)
- **4:** Confidential business data, intellectual property
- **3:** Internal use data, moderate sensitivity
- **2:** Low-sensitivity internal data
- **1:** Public information only
- **0:** No data storage/processing


*How to score:*
Look at Question 1.4 (Data Types Processed). If processing PII, financial data, or PHI → score 5. If only internal business data → score 3-4. If public info → score 1.

*Example:*
Application processes customer payment card data and names/addresses.
→ Score: **5** (PCI DSS data + PII = highest sensitivity)

**User Base (Weight: 20%)**

*Score 0-5:*

- **5:** Public/anonymous users, customers (thousands)
- **4:** Business partners, contractors (hundreds)
- **3:** Mixed internal/external users
- **2:** Authenticated employees only (dozens)
- **1:** Restricted user group (<20 users)


*How to score:*
Look at Question 1.3 (User Base). More users = higher risk (larger attack surface, more credentials to manage).

*Example:*
Application used by 10,000 external customers.
→ Score: **5** (public user base)

**Internet Exposure (Weight: 25%)**

*Score 0-5:*

- **5:** Publicly accessible via internet (no VPN required)
- **4:** Internet-accessible with VPN/authentication
- **3:** Hybrid (some components internet-facing)
- **2:** Internal network with remote access (VPN)
- **1:** Isolated internal network (no remote access)
- **0:** Air-gapped/standalone


*How to score:*
Look at Question 1.5 (Internet Accessibility). Direct internet exposure = highest risk.

*Example:*
Customer portal accessible via https://portal.company.com (public URL).
→ Score: **5** (direct internet exposure)

**Business Criticality (Weight: 15%)**

*Score 0-5:*

- **5:** Critical (outage = business stoppage, revenue loss, regulatory breach)
- **4:** High impact (significant operational disruption)
- **3:** Moderate impact (workarounds available, inconvenient)
- **2:** Low impact (efficiency/convenience only)
- **1:** Minimal impact (nice-to-have)


*How to score:*
Ask: "What happens if this application is down for 4 hours? 1 day? 1 week?"
If answer is "business stops" or "major revenue loss" → score 5.
If answer is "minor inconvenience" → score 2-3.

*Example:*
E-commerce platform (primary revenue channel).
→ Score: **5** (revenue-critical)

**Regulatory Scope (Weight: 10%)**

*Score 0-5:*

- **5:** Multiple regulations (GDPR + PCI DSS + HIPAA, etc.)
- **4:** One major regulation (GDPR, PCI DSS, HIPAA, SOX)
- **3:** Industry standards (ISO 27001, SOC 2)
- **2:** Internal policies only
- **1:** Minimal requirements


*How to score:*
Look at Question 1.4 (Regulatory Scope). Count applicable regulations.

*Example:*
Application processes EU customer PII (GDPR) and payment cards (PCI DSS).
→ Score: **5** (two major regulations)

### Question 2.2: Risk Classification Result

**Automatic Calculation:**
The workbook automatically calculates:

- Weighted score for each criterion
- Total risk score (0-5 scale)
- Risk classification (High/Medium/Low)


**Classification Thresholds:**

- **High Risk:** Total score ≥ 3.5
- **Medium Risk:** Total score 2.0 - 3.4
- **Low Risk:** Total score < 2.0


**What if classification seems wrong?**

Sometimes the formula produces unexpected results. Common scenarios:

*Scenario 1: Low data sensitivity but high internet exposure*

- Example: Marketing website (public content, public internet)
- Formula may say "Medium Risk" due to internet exposure
- **Action:** Acceptable - internet exposure does increase risk even for low-sensitivity data


*Scenario 2: High data sensitivity but internal-only*

- Example: Payroll system (sensitive data, internal users only)
- Formula may say "Medium Risk"
- **Action:** Consider override to "High Risk" - sensitive data justifies higher classification
- **Document:** Override justification in Notes field


*Scenario 3: Borderline score (exactly 2.0 or 3.5)*

- **Action:** Use judgment - round up if concerned about specific threats
- **Document:** Rationale in Notes field


**Column D: Classification Approved By**

*What to enter:* Security Architect who reviewed and approved classification

**Column E: Approval Date**

*What to enter:* Date classification was approved

**Column F: Next Review Date**

*What to enter:* When to re-review classification (typically annual or on major changes)

*Evidence:* Risk scoring worksheet, email approval, classification meeting minutes

---

## Sheet 3: Security Requirements Documentation

**Purpose:** Assess whether security requirements are properly documented.

### Question 3.1: Does a Security Requirements Specification (SRS) exist?

**Column B: SRS Exists? (Yes/No/N/A)**

*Answer Yes if:*

- Formal document titled "Security Requirements Specification" or similar exists
- Security requirements documented in distinct section of requirements document
- Security requirements clearly identified and traceable


*Answer No if:*

- No security requirements documented anywhere
- Security mentioned only vaguely ("must be secure")
- Requirements mixed with functional requirements, not identifiable


*Answer N/A if:*

- Application is COTS with no customization (security requirements vendor responsibility)
- Application being decommissioned (no new requirements needed)


*Where to find:*

- Document repository (SharePoint, Confluence, etc.)
- Project folder for application
- Requirements management tool (Jira, Azure DevOps, etc.)


**Column C: Document Title & Location**

*What to enter:* Exact document title and where to find it

*Examples:*

- ✅ "Customer Portal Security Requirements Specification v2.1 - SharePoint > Projects > CUST-PORTAL > Requirements > SRS_v2.1.docx"
- ✅ "SAP ERP Security Configuration Guide - Confluence > IT > Security > SAP_Security_Config"
- ❌ "Somewhere in SharePoint" (too vague)
- ❌ "John has it" (not accessible)


**Column D: Document Version**

*What to enter:* Version number (shows document is under version control)

*Examples:*

- v2.1, v1.0, Rev 3, 2025-12-01 (date as version)


**Column E: Last Updated Date**

*What to enter:* When the security requirements were last reviewed/updated

*Why this matters:*
Requirements older than 12 months may be outdated (technology changes, new threats, regulatory changes).

**Status Determination:**

*✅ Compliant:*

- SRS exists
- Document title and location provided
- Version tracked
- Updated within last 12 months (or since last major release)


*⚠️ Partial:*

- SRS exists but outdated (>12 months)
- Security requirements exist but embedded in larger requirements doc (not dedicated SRS)
- Draft SRS exists but not finalized


*❌ Non-Compliant:*

- No SRS exists
- Security requirements not documented
- SRS location unknown / document lost


*N/A:*

- COTS application with no customization
- Application being decommissioned


### Question 3.2: SRS Completeness - Functional Security Requirements

**Column B: Authentication Requirements Specified? (Yes/No/N/A)**

*Answer Yes if:*
SRS includes requirements for:

- Authentication method (password, MFA, SSO, certificate-based, etc.)
- Password complexity requirements (if applicable)
- Account lockout policy
- Session timeout requirements
- MFA requirements for privileged users


*Example requirement:*
"The application SHALL implement multi-factor authentication for all administrative users. MFA SHALL use TOTP (RFC 6238) or push-notification method."

*Answer No if:*

- No authentication requirements documented
- Only vague statement ("must authenticate users")


*Answer N/A if:*

- Application has no authentication (public read-only content)
- Authentication handled by separate identity system (but should reference it)


**Column C: Authorization Requirements Specified? (Yes/No/N/A)**

*Answer Yes if:*
SRS includes requirements for:

- Authorization model (RBAC, ABAC, etc.)
- Role definitions
- Access control matrix (who can access what)
- Privilege escalation prevention
- Default deny (deny access unless explicitly granted)


*Example requirement:*
"The application SHALL implement role-based access control (RBAC) with minimum roles: User, Manager, Administrator. Access SHALL be denied by default unless explicitly granted."

*Answer No if:*

- No authorization requirements documented
- Only vague statement ("must control access")


*Answer N/A if:*

- Public application with no protected resources
- Authorization handled by separate system (but should reference it)


**Column D: Input Validation Requirements Specified? (Yes/No/N/A)**

*Answer Yes if:*
SRS includes requirements for:

- Input validation on all user input
- Whitelist approach (allow known-good, reject everything else)
- Validation type (data type, length, format, range)
- Output encoding based on context
- Protection against injection attacks (SQL, XSS, command injection)


*Example requirement:*
"The application SHALL validate all input from users and external systems using whitelist validation. All user input SHALL be validated for data type, length, format, and range. The application SHALL use parameterized queries for all database access to prevent SQL injection."

*Answer No if:*

- No input validation requirements
- Only vague statement ("must validate input")


*Answer N/A if:*

- No user input accepted (read-only static content)


**Column E: Cryptography Requirements Specified? (Yes/No/N/A)**

*Answer Yes if:*
SRS includes requirements for:

- Data in transit encryption (TLS 1.2+, strong cipher suites)
- Data at rest encryption (for sensitive data)
- Cryptographic algorithm specifications
- Key management requirements
- Certificate validation


*Example requirement:*
"The application SHALL encrypt all data in transit using TLS 1.3 or TLS 1.2 with approved cipher suites per ISMS-POL-A.8.24. Sensitive data (PII, payment card data) SHALL be encrypted at rest using AES-256."

*Answer No if:*

- No cryptography requirements
- Only vague statement ("must use encryption")


*Answer N/A if:*

- No sensitive data processed (public information only)
- No network communication (standalone application)


**Column F: Logging Requirements Specified? (Yes/No/N/A)**

*Answer Yes if:*
SRS includes requirements for:

- Security events to log (authentication, authorization, data access, configuration changes)
- Log content (who, what, when, where, result)
- Log retention period
- Log integrity protection
- Centralized logging (SIEM integration for High-Risk apps)


*Example requirement:*
"The application SHALL log all authentication attempts (successful and failed), authorization decisions (grants and denials), administrative actions, and data modifications. Logs SHALL include timestamp, user ID, source IP, action, and result. Logs SHALL be retained for 12 months and protected from tampering."

*Answer No if:*

- No logging requirements
- Only vague statement ("must log events")


*Answer N/A if:*

- Logging not applicable (static content with no user interaction)


**Column G: API Security Requirements Specified? (Yes/No/N/A)**

*Answer Yes if:*
SRS includes requirements for:

- API authentication (API keys, OAuth 2.0, JWT)
- API authorization (scope-based access control)
- API rate limiting
- API input validation
- API documentation (OpenAPI/Swagger)


*Example requirement:*
"The application API SHALL require OAuth 2.0 bearer tokens for authentication. API calls SHALL be rate-limited to 100 requests per minute per client. All API input SHALL be validated per input validation requirements."

*Answer No if:*

- Application has APIs but no security requirements documented
- Only vague statement ("APIs must be secure")


*Answer N/A if:*

- Application has no APIs
- APIs are internal-only (but should still have security requirements)


**Status for Section 3.2:**

*✅ Compliant:*

- All applicable functional security requirement categories addressed
- Requirements are specific and testable (not vague)
- Requirements reference standards/policies where applicable


*⚠️ Partial:*

- Some categories addressed, others missing
- Requirements exist but are vague ("must be secure" vs. "SHALL use TLS 1.2+")


*❌ Non-Compliant:*

- Most/all functional security requirements missing
- No detail beyond generic statements


### Question 3.3: SRS Completeness - Non-Functional Security Requirements

**Column B: Performance Requirements (Under Security Load)?**

*Answer Yes if:*
SRS includes requirements for:

- Acceptable performance with security controls enabled (authentication, encryption, validation)
- Performance under attack scenarios (brute force, DoS)
- Performance benchmarks for security operations


*Example:*
"Authentication response time SHALL be <500ms at p95. The application SHALL maintain 80% of normal throughput under simulated credential stuffing attack (100 login attempts/second)."

*Answer No if:*

- No security performance requirements
- Performance requirements exist but don't consider security overhead


**Column C: Resilience Requirements (Fail Secure)?**

*Answer Yes if:*
SRS includes requirements for:

- Fail-secure behavior (deny access on error)
- Graceful degradation under attack
- Circuit breaker patterns
- Resource exhaustion handling


*Example:*
"The application SHALL fail-closed on authorization errors (deny access if cannot determine authorization). The application SHALL implement rate limiting to prevent resource exhaustion attacks."

*Answer No if:*

- No resilience requirements
- No specification of fail-secure vs. fail-open behavior


**Column D: Secure Defaults?**

*Answer Yes if:*
SRS includes requirements for:

- Secure default configuration (no default passwords, secure cipher suites enabled by default)
- Principle of least privilege in defaults
- Unused features disabled by default
- Requirement for explicit security configuration changes


*Example:*
"The application SHALL ship with secure default configuration: TLS 1.2+ enabled, weak cipher suites disabled, all administrative interfaces requiring authentication, default accounts disabled."

*Answer No if:*

- No secure defaults requirements
- Insecure defaults allowed (e.g., HTTP allowed by default)


**Status for Section 3.3:**

*✅ Compliant:* All applicable non-functional security requirements addressed
*⚠️ Partial:* Some addressed, others missing
*❌ Non-Compliant:* Most/all missing

---

## Sheet 4: Threat Modeling Status

**Purpose:** Assess whether threat modeling was conducted (required for High-Risk, recommended for Medium-Risk).

### Question 4.1: Was threat modeling conducted?

**Column B: Threat Modeling Conducted? (Yes/No/N/A)**

*Answer Yes if:*

- Formal threat modeling workshop conducted
- Threat model document exists
- Threats identified and documented
- Countermeasures defined


*Answer No if:*

- No threat modeling conducted
- Only informal discussion (no documentation)


*Answer N/A if:*

- Low-Risk application (threat modeling not required per policy)
- COTS application with no customization


*Policy requirements:*

- **High-Risk applications:** Threat modeling MANDATORY
- **Medium-Risk applications:** Threat modeling RECOMMENDED
- **Low-Risk applications:** Threat modeling OPTIONAL


**Column C: Threat Model Document Title & Location**

*What to enter:* Document title and location

*Examples:*

- "Customer Portal Threat Model v1.2 - SharePoint > Security > Threat Models > CUST-PORTAL-TM-v1.2.pdf"
- "Payment Gateway STRIDE Analysis - Confluence > Security Architecture > Payment_Gateway_STRIDE"


**Column D: Methodology Used**

*What to enter:* Threat modeling methodology

*Common methodologies:*

- **STRIDE:** Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege
- **PASTA:** Process for Attack Simulation and Threat Analysis
- **LINDDUN:** Privacy threat modeling
- **Attack Trees:** Graphical threat representation
- **DREAD:** Damage, Reproducibility, Exploitability, Affected Users, Discoverability (deprecated but still used)


*Example:*
"STRIDE methodology applied to data flow diagrams"

**Column E: Last Updated Date**

*What to enter:* When threat model was last updated

*Why this matters:*
Threat models should be updated when:

- Application architecture changes significantly
- New threats emerge (Log4Shell, etc.)
- Major functionality added
- At least annually for High-Risk applications


**Column F: Threats Identified (Count)**

*What to enter:* Total number of threats identified

*Typical range:*

- Simple applications: 10-30 threats
- Complex applications: 50-150 threats
- Very complex (many integrations): 200+ threats


*Red flags:*

- Too few threats (<10) suggests incomplete analysis
- No threats identified = threat modeling not properly conducted


**Column G: Threats Mitigated**

*What to enter:* How many identified threats have countermeasures implemented?

*Typical breakdown:*

- Mitigated: Security control implemented (authentication, encryption, validation, etc.)
- Accepted: Risk accepted (documented why no mitigation)
- Transferred: Risk transferred (insurance, vendor responsibility)
- Outstanding: Not yet addressed (plan required)


*Example:*
"45 threats identified: 40 mitigated, 3 accepted risk (documented), 2 outstanding (planned for Q2)"

### Question 4.2: Threat Model Quality Assessment

**Column B: Architecture Diagrams Included? (Yes/No)**

*Answer Yes if:*

- Data flow diagrams (DFD) showing components, data flows, trust boundaries
- System context diagram showing external entities
- Deployment architecture diagram


*Answer No if:*

- No diagrams, only text description
- Diagrams too high-level to be useful


**Column C: Trust Boundaries Identified? (Yes/No)**

*Answer Yes if:*

- Trust boundaries clearly marked on diagrams
- Boundaries between components with different trust levels identified
- Internet/internal network boundary documented
- User/admin privilege boundaries identified


*Example trust boundaries:*

- Internet ↔ Web Application Firewall ↔ Application Server
- User Interface ↔ Application Logic ↔ Database
- User Role ↔ Admin Role


*Answer No if:*

- No trust boundaries identified
- Unclear where boundaries exist


**Column D: Countermeasures Documented? (Yes/No)**

*Answer Yes if:*

- Each threat has associated countermeasure
- Countermeasures specific (not "use encryption" but "use TLS 1.2+ for all client-server communication")
- Countermeasures mapped to security requirements


*Answer No if:*

- Threats identified but no countermeasures
- Countermeasures too vague to implement


**Column E: Residual Risks Documented? (Yes/No)**

*Answer Yes if:*

- Risks that remain after countermeasures are documented
- Risk acceptance decisions documented
- Risk owners assigned


*Answer No if:*

- No discussion of residual risk
- Assumption that all countermeasures eliminate all risk


**Status for Sheet 4:**

*✅ Compliant (for High-Risk apps):*

- Threat modeling conducted
- Document complete with diagrams, threats, countermeasures
- Updated within last 12 months (or since last major release)


*✅ Compliant (for Medium-Risk apps):*

- Threat modeling conducted (recommended but not required)
- OR documented decision not to conduct with justification


*⚠️ Partial:*

- Threat model exists but incomplete (missing diagrams, countermeasures, etc.)
- Threat model outdated (>12 months for High-Risk)


*❌ Non-Compliant:*

- High-Risk application with no threat model
- Threat model required but not conducted


*N/A:*

- Low-Risk application (threat modeling optional per policy)


**Evidence:**

- Threat model document
- Workshop attendance records
- Threat model review approval
- Residual risk acceptance documentation


---

## Sheet 5: Architecture Review Status

**Purpose:** Assess whether security architecture review was conducted.

### Question 5.1: Was security architecture review conducted?

**Column B: Architecture Review Conducted? (Yes/No/N/A)**

*Answer Yes if:*

- Formal security architecture review meeting held
- Security Architect reviewed architecture diagrams
- Security findings documented
- Review report exists


*Answer No if:*

- No architecture review conducted
- Only informal review (no documentation)


*Answer N/A if:*

- Low-Risk application (architecture review optional per policy)
- COTS application with no customization


*Policy requirements:*

- **High-Risk applications:** Architecture review MANDATORY
- **Medium-Risk applications:** Architecture review RECOMMENDED
- **Low-Risk applications:** Architecture review OPTIONAL


**Column C: Review Report Title & Location**

*What to enter:* Document title and location

*Example:*
"Customer Portal Security Architecture Review - 2025-11-15 - SharePoint > Security Reviews > CUST-PORTAL-ArchReview-20251115.pdf"

**Column D: Reviewer Name**

*What to enter:* Security Architect who conducted review

**Column E: Review Date**

*What to enter:* Date of architecture review meeting/completion

**Column F: Review Findings (Count)**

*What to enter:* Total number of security findings identified

*Typical range:*

- Well-designed architecture: 5-15 findings (mostly minor improvements)
- Needs improvement: 20-40 findings
- Major issues: 50+ findings


*Severity breakdown typical:*

- Critical: 0-3 (architecture flaws that block deployment)
- High: 5-15 (significant security issues)
- Medium: 10-30 (moderate concerns)
- Low: 10-40 (minor improvements)


**Column G: Critical/High Findings Remediated?**

*Answer:*

- "Yes - All remediated" (evidence: remediation records)
- "Partial - X of Y remediated" (remaining items in progress)
- "No - Outstanding" (requires justification)


*Policy requirement:*
Critical and High findings MUST be remediated before production deployment for High-Risk applications.

### Question 5.2: Architecture Review Quality Assessment

**Column B: Architecture Diagrams Reviewed? (Yes/No)**

*Answer Yes if:*

- System context diagram reviewed
- Component architecture diagram reviewed
- Deployment architecture diagram reviewed
- Network architecture diagram reviewed (if applicable)


**Column C: Security Controls Validated? (Yes/No)**

*Answer Yes if:*

- Authentication architecture validated
- Authorization model validated
- Data protection architecture validated (encryption, key management)
- API security architecture validated (if applicable)
- Logging architecture validated
- Network segmentation validated


*Answer No if:*

- Only high-level review, no security control deep-dive


**Column D: Integration Points Reviewed? (Yes/No)**

*Answer Yes if:*

- External system integrations identified
- API security for integrations reviewed
- Third-party component security reviewed
- Data flows to/from external systems validated


*Answer No if:*

- Integration security not explicitly reviewed


**Column E: Review Approval Obtained? (Yes/No)**

*Answer Yes if:*

- Security Architect signed off on architecture
- CISO approved for High-Risk applications
- Approval documented with date and signature


*Answer No if:*

- Review conducted but no formal approval
- Approval pending remediation of findings


**Status for Sheet 5:**

*✅ Compliant (for High-Risk apps):*

- Architecture review conducted
- Review report complete
- Critical/High findings remediated
- Approval obtained (Security Architect + CISO)


*✅ Compliant (for Medium-Risk apps):*

- Architecture review conducted (recommended)
- OR documented decision not to conduct with justification


*⚠️ Partial:*

- Review conducted but findings not fully remediated
- Review outdated (>12 months for changed architecture)


*❌ Non-Compliant:*

- High-Risk application with no architecture review
- Review required but not conducted
- Critical/High findings outstanding with no remediation plan


*N/A:*

- Low-Risk application (review optional per policy)


**Evidence:**

- Architecture review report
- Architecture diagrams (reviewed versions)
- Finding remediation records
- Approval sign-off


---

## Sheet 6: Requirements Traceability

**Purpose:** Assess whether security requirements are traceable from specification through implementation to testing.

### Question 6.1: Requirements Traceability Matrix Exists?

**Column B: Traceability Matrix Exists? (Yes/No)**

*Answer Yes if:*

- Document/system showing linkage: Security Requirement → Design Decision → Implementation → Test Case
- May be in spreadsheet, requirements management tool (Jira, Azure DevOps), or document


*Answer No if:*

- No traceability documentation
- Requirements exist but no linkage to implementation/testing


*Where to find:*

- Requirements management tool (Jira stories with linked test cases)
- Traceability matrix spreadsheet
- Security requirements document with traceability section


**Column C: Format/Location**

*What to enter:* Where traceability is documented

*Examples:*

- "Jira: Security requirements as Epics, implementation as Stories, tests as sub-tasks"
- "Excel Traceability Matrix - SharePoint > Requirements > Traceability_Matrix_v1.2.xlsx"
- "Security Requirements Specification Appendix B: Traceability Matrix"


### Question 6.2: Traceability Coverage

**Column B: % Requirements Traced to Design**

*What to enter:* Percentage of security requirements that have associated design decisions documented

*How to calculate:*
(Security Requirements with Design Documentation) / (Total Security Requirements) × 100%

*Examples:*

- 100%: Every requirement has design decision (optimal)
- 80-99%: Most requirements traced (acceptable)
- <80%: Significant gaps in traceability


*Where to find:*

- Architecture documents referencing requirements
- Design documents with requirements IDs
- Traceability matrix


**Column C: % Requirements Traced to Implementation**

*What to enter:* Percentage of security requirements that have associated code/configuration

*How to calculate:*
(Security Requirements with Implementation Evidence) / (Total Security Requirements) × 100%

*Examples:*

- 100%: Every requirement implemented and documented
- 80-99%: Most requirements implemented
- <80%: Significant implementation gaps


*Evidence:*

- Code commits referencing requirement IDs
- Configuration documentation
- Release notes showing implemented requirements


**Column D: % Requirements Traced to Test Cases**

*What to enter:* Percentage of security requirements that have associated test cases

*How to calculate:*
(Security Requirements with Test Cases) / (Total Security Requirements) × 100%

*Examples:*

- 100%: Every requirement has test case (optimal)
- 80-99%: Most requirements tested
- <80%: Significant testing gaps


*Evidence:*

- Test plan with requirements IDs
- Test management system (TestRail, Zephyr) showing requirement-to-test linkage
- Security testing results mapped to requirements


### Question 6.3: Traceability Tool

**Column B: Tool/System Used**

*What to enter:* Tool used to manage traceability

*Common tools:*

- Jira (requirements as Epics/Stories, tests as sub-tasks)
- Azure DevOps (Work Items with hierarchical linking)
- HP ALM / Micro Focus ALM
- IBM DOORS (enterprise requirements management)
- Excel/SharePoint (simple traceability matrices)
- Confluence (requirements documentation with links)


*Example:*
"Jira: SEC-REQ Epics → DEV Stories (implementation) → TEST sub-tasks"

**Column C: Last Updated**

*What to enter:* When traceability was last updated

*Why this matters:*
Traceability should be updated throughout development, not just at the end. Outdated traceability suggests it's not actively used.

**Status for Sheet 6:**

*✅ Compliant:*

- Traceability matrix exists
- >90% requirements traced to design, implementation, and testing
- Traceability current (updated within last 3 months)


*⚠️ Partial:*

- Traceability exists but incomplete (60-89% coverage)
- Traceability outdated (>6 months)


*❌ Non-Compliant:*

- No traceability matrix
- <60% requirements traced
- Traceability never updated


**Evidence:**

- Traceability matrix document/export
- Requirements management tool screenshots
- Test plan showing requirement linkage


---

## Sheet 7: Compliance Checklist

**Purpose:** Quick checklist of key policy requirements for A.8.26.

This sheet is auto-populated based on your answers in previous sheets. Review for accuracy.

**Checklist Items:**

- [ ] Application risk classified (High/Medium/Low)
- [ ] Risk classification approved by Security Architect
- [ ] Security Requirements Specification (SRS) exists
- [ ] SRS includes functional security requirements (authentication, authorization, input validation, crypto, logging)
- [ ] SRS includes non-functional security requirements (performance, resilience, secure defaults)
- [ ] SRS includes data protection requirements (encryption, retention, deletion, privacy)
- [ ] Threat modeling conducted (if High-Risk or Medium-Risk)
- [ ] Threat model includes architecture diagrams with trust boundaries
- [ ] Threat model includes threat enumeration and countermeasures
- [ ] Security architecture review conducted (if High-Risk or Medium-Risk)
- [ ] Architecture review findings documented
- [ ] Critical/High architecture findings remediated
- [ ] Requirements traceability matrix exists
- [ ] Requirements traced to design (>90%)
- [ ] Requirements traced to implementation (>90%)
- [ ] Requirements traced to test cases (>90%)
- [ ] Security requirements approved (Security Architect for Medium/High, CISO for High)
- [ ] All evidence documented and accessible


**Auto-Scoring:**

- Compliant items: Count of ✅
- Non-compliant items: Count of ❌
- Partial items: Count of ⚠️
- Overall compliance %: (Compliant Items / Total Applicable Items) × 100%


---

## Sheet 8: Gap Analysis & Action Plan

**Purpose:** Document identified gaps and remediation plan.

For each gap identified in the assessment:

**Column A: Gap ID**
*Auto-generated:* GAP-001, GAP-002, etc.

**Column B: Gap Description**
*What to enter:* Clear description of what's missing

*Examples:*

- "No threat model exists for Customer Portal (High-Risk application)"
- "SRS missing input validation requirements"
- "Architecture review conducted but 3 High findings not remediated"


**Column C: Sheet Reference**
*What to enter:* Which sheet identified this gap

*Example:* "Sheet 4 - Threat Modeling Status"

**Column D: Severity**
*What to enter:* How critical is this gap?

*Severity levels:*

- **Critical:** Blocks deployment (High-Risk app missing required controls)
- **High:** Must address before next release
- **Medium:** Address in next 90 days
- **Low:** Track as technical debt


**Column E: Policy Requirement**
*What to enter:* Which policy requirement is violated?

*Example:* "ISMS-POL-A.8.25-26-29 Section 2.8: Threat modeling MANDATORY for High-Risk applications"

**Column F: Remediation Action**
*What to enter:* Specific action to close gap

*Examples:*

- "Conduct threat modeling workshop using STRIDE methodology"
- "Update SRS Section 4.3 to add input validation requirements per policy"
- "Remediate 3 High architecture findings: implement API rate limiting, enable MFA for admins, configure TLS 1.2+"


**Column G: Responsible Party**
*What to enter:* Who will fix this?

*Examples:*

- Security Architect (for threat modeling)
- Product Manager (for requirements updates)
- Development Team (for implementation)
- DevOps (for configuration)


**Column H: Target Date**
*What to enter:* When will this be completed?

*SLA guidelines:*

- Critical gaps: 30 days
- High gaps: 90 days
- Medium gaps: 180 days
- Low gaps: Next major release


**Column I: Status**
*What to enter:* Current status

*Status options:*

- Open (not started)
- In Progress (work underway)
- Resolved (completed, evidence available)
- Risk Accepted (documented decision not to remediate)


**Column J: Completion Date**
*What to enter:* When was gap closed? (leave blank if still open)

**Column K: Evidence of Closure**
*What to enter:* What evidence shows gap is closed?

*Examples:*

- "Threat Model v1.0 dated 2026-01-20 - SharePoint link"
- "SRS v2.2 Section 4.3 updated - Confluence link"
- "Architecture findings remediation records - Jira tickets DEV-1234, DEV-1235, DEV-1236"


---

## Sheet 9: Evidence Register

**Purpose:** Centralized register of all evidence supporting this assessment.

For each piece of evidence:

**Column A: Evidence ID**
*Auto-generated:* EV-001, EV-002, etc.

**Column B: Evidence Type**
*What to enter:* Type of evidence

*Common types:*

- Document (SRS, threat model, architecture review report)
- Email (approval email, stakeholder confirmation)
- Screenshot (tool output, configuration settings)
- Meeting Minutes (threat modeling workshop, architecture review meeting)
- Report (security testing report, audit report)
- Spreadsheet (traceability matrix, risk scoring)


**Column C: Evidence Title**
*What to enter:* Descriptive title

*Examples:*

- "Customer Portal Security Requirements Specification v2.1"
- "Threat Modeling Workshop Minutes - 2025-11-08"
- "Architecture Review Report - Customer Portal - 2025-11-15"


**Column D: Evidence Location**
*What to enter:* Where can auditor/reviewer find this?

*Format:* `System > Folder > Subfolder > Filename`

*Examples:*

- "SharePoint > Projects > CUST-PORTAL > Requirements > SRS_v2.1.docx"
- "Confluence > Security Architecture > Threat Models > Customer_Portal_TM"
- "Jira > SEC-REQ-001 > Attachments > Traceability_Matrix.xlsx"


**Column E: Date**
*What to enter:* Evidence date (document date, not evidence collection date)

*Format:* DD.MM.YYYY

**Column F: Owner**
*What to enter:* Who created/maintains this evidence?

*Examples:*

- Product Manager (for SRS)
- Security Architect (for threat model, architecture review)
- Development Manager (for traceability matrix)


**Column G: Related Assessment Question**
*What to enter:* Which assessment question(s) does this evidence support?

*Format:* Sheet.Question

*Examples:*

- "3.1" (Sheet 3, Question 1 - SRS Exists)
- "4.1, 4.2" (Sheet 4, Questions 1 and 2 - Threat Modeling)
- "5.1" (Sheet 5, Question 1 - Architecture Review)


**Column H: Evidence Verified?**
*What to enter:* Has reviewer confirmed this evidence exists and is adequate?

*Options:*

- Yes (verified by reviewer)
- No (not yet verified)
- Issue (evidence missing, inadequate, or outdated)


**Column I: Verification Date**
*What to enter:* When was evidence verified?

**Column J: Verified By**
*What to enter:* Who verified evidence?

---

## Sheet 10: Approval & Sign-Off

**Purpose:** Document assessment completion and approval.

### Assessment Summary (Rows 1-10)

**Assessment Period:** [User input] *Example: Q4 2025 (October - December 2025)*

**Assessment Date:** [User input] *Example: 15.01.2026*

**Application Name:** [Auto-populated from Sheet 1]

**Application Risk:** [Auto-populated from Sheet 2]

**Overall Compliance Score:** [Auto-calculated from Sheet 7] *Example: 87% Compliant*

**Critical Gaps:** [Auto-counted from Sheet 8] *Example: 2 Critical, 5 High, 8 Medium, 3 Low*

**Assessment Status:** [Dropdown]

- Draft (work in progress)
- Final (ready for approval)
- Approved (signed off)
- Requires Remediation (gaps must be addressed)


### Assessment Completed By (Rows 12-20)

**Name:** [User input]  
**Role/Title:** [User input] *Example: Security Architect, Product Manager*  
**Department:** [User input]  
**Email:** [User input]  
**Date:** [User input - date picker]  
**Signature:** [User input] *Example: /s/ John Smith*

### Reviewed By - Security Architect (Rows 22-30)

**Name:** [User input]  
**Date:** [User input]  
**Review Notes:** [Text area - merged cells]

*Example review notes:*
"Reviewed application security requirements assessment for Customer Portal. Documentation is comprehensive. Two gaps identified: (1) Threat model needs update (>12 months old), (2) Three High architecture findings remain open. Recommend addressing before next major release."

**Recommendation:** [Dropdown]

- Approve (assessment complete, acceptable gaps)
- Approve with Conditions (minor gaps, must address by X date)
- Require Remediation (critical/high gaps must be addressed before approval)
- Reject (incomplete assessment, resubmit)


### Approved By - CISO (High-Risk Applications Only) (Rows 32-40)

**Name:** [User input]  
**Date:** [User input]  
**Approval Decision:** [Dropdown]

- Approved (for production deployment)
- Approved with Conditions (conditions documented below)
- Rejected (cannot deploy until gaps addressed)


**Conditions/Notes:** [Text area]

*Example:*
"Approved for production deployment contingent on remediation of 2 Critical gaps (threat model update, MFA implementation for admins) within 30 days. Re-assessment required after remediation."

### Next Review Details (Rows 42-46)

**Next Assessment Date:** [Date - auto-calculate based on risk classification]

- High-Risk: +3 months (quarterly)
- Medium-Risk: +12 months (annually)
- Low-Risk: +12 months (annually)


**Review Responsible:** [User input]

**Special Considerations:** [Text area]

*Example:*
"Next assessment should verify threat model update and MFA implementation completion. Major release planned for Q2 2026 - schedule assessment before release."

---

# Evidence Collection

## General Evidence Guidelines

**Evidence Naming Convention:**
```
EV-[SheetNumber]-[ApplicationID]-[DocumentType]-[Date].[ext]
```

**Examples:**

- `EV-3-APP-CUST-SRS-20260115.pdf` (SRS for Customer Portal app)
- `EV-4-APP-CUST-ThreatModel-20260115.pdf` (Threat Model)
- `EV-5-APP-CUST-ArchReview-20260115.pdf` (Architecture Review Report)
- `EV-6-APP-CUST-Traceability-20260115.xlsx` (Traceability Matrix)


**Storage Requirements:**

- **Location:** Centralized evidence repository
- **Folder Structure:** `Evidence/[AppID]/A.8.26_Requirements/[AssessmentDate]/`
- **Retention:** Audit cycle + 1 year minimum (typically 3 years)
- **Access Control:** Read access for auditors, compliance team, security team
- **Backup:** Included in standard backup procedures


**Evidence Quality Criteria:**

- **Timestamped:** Must show date/time of creation
- **Attributable:** Clear which application it documents
- **Complete:** Full document, not excerpts (unless noted)
- **Current:** Within validity period (< 12 months for High-Risk)
- **Verifiable:** Auditor can independently access and verify


## Evidence Types by Sheet

**Sheet 1: Application Profile**

- Application inventory record (screenshot or export)
- Application architecture diagram
- Data flow diagram
- Privacy Impact Assessment (if PII processed)


**Sheet 2: Risk Classification**

- Risk scoring worksheet
- Risk classification approval email
- Management meeting minutes (if classification discussed)


**Sheet 3: Security Requirements Documentation**

- Security Requirements Specification (SRS) document (full document)
- Requirements document excerpts (if SRS is section of larger document)
- Requirements management tool exports (Jira, Azure DevOps)


**Sheet 4: Threat Modeling**

- Threat model document (full document with diagrams)
- Threat modeling workshop attendance list
- Threat modeling tool exports (if tool used)
- Residual risk acceptance records


**Sheet 5: Architecture Review**

- Security architecture review report (full report)
- Architecture diagrams (reviewed versions)
- Architecture review meeting minutes
- Finding remediation records (Jira tickets, change records)
- Architecture approval sign-off


**Sheet 6: Requirements Traceability**

- Traceability matrix (spreadsheet or tool export)
- Requirements management tool screenshots
- Test plan showing requirement linkage
- Design documents referencing requirements


**Sheet 7: Compliance Checklist**

- (No separate evidence - checklist populated from other sheets)


**Sheet 8: Gap Analysis**

- Gap remediation plan (Sheet 8 itself serves as evidence)
- Remediation work tracking (Jira epics, project plans)
- Completed remediation evidence (updated SRS, completed threat model, etc.)


**Sheet 9: Evidence Register**

- (No separate evidence - register documents evidence locations)


**Sheet 10: Approval & Sign-Off**

- Signed approval emails
- Digital signatures (if used)
- Management meeting minutes (if presented)


## Evidence Collection Tips

**For Distributed Teams:**

- Use shared cloud storage (SharePoint, Google Drive)
- Standardize folder structures
- Use consistent naming conventions
- Set up automated reminders for evidence submissions


**For Large Application Portfolios:**

- Create evidence collection templates
- Automate exports from tools where possible
- Batch collect evidence (e.g., quarterly for all High-Risk apps)
- Consider evidence management tool (GRC platforms)


**For Auditors:**

- Provide evidence index (Sheet 9) first
- Offer remote access to evidence repository
- Prepare evidence package for major audits
- Maintain audit trails (who accessed what when)


---

# Common Pitfalls

**Pitfall 1: Treating Assessment as Checkbox Exercise**

**Symptom:** "Yes" answers everywhere with no supporting evidence

**Why it's bad:** Defeats purpose of assessment, provides false assurance, fails audit

**Solution:**

- Require evidence location for every "Yes"
- Spot-check evidence (don't just trust assessor)
- Make assessor accountable (sign-off with consequences for false claims)


**Example:**
❌ Bad: "SRS Exists? Yes" (no document title, no location, no version)
✅ Good: "SRS Exists? Yes - Customer Portal SRS v2.1 dated 2025-12-01 in SharePoint > Projects > CUST-PORTAL > Requirements > SRS_v2.1.docx"

---

**Pitfall 2: Confusing "Security Requirements" with "General Requirements"**

**Symptom:** Assessor thinks "We have requirements" = "We have security requirements"

**Why it's bad:** Business requirements ≠ security requirements. "Application shall allow users to update profile" is NOT a security requirement.

**Solution:**

- Look for SHALL statements about security controls
- Look for authentication, authorization, encryption, validation, logging requirements
- If requirements doc doesn't have a "Security" section, probably no security requirements


**Example:**
❌ Not Security Requirements: "The application shall allow customers to view their account balance"
✅ Security Requirements: "The application SHALL require multi-factor authentication for all users accessing account balance information. The application SHALL log all account balance access attempts with timestamp, user ID, and source IP address."

---

**Pitfall 3: Accepting Vague Requirements**

**Symptom:** SRS says "Application must be secure" or "Use encryption"

**Why it's bad:** Vague requirements = not testable = not implementable = security theater

**Solution:**

- Security requirements must be SPECIFIC and TESTABLE
- "Use encryption" → "Use TLS 1.2+ with cipher suites XYZ for all client-server communication"
- "Authenticate users" → "Implement OAuth 2.0 authentication with TOTP-based MFA for all administrative users"


**Example:**
❌ Vague: "The application shall use strong passwords"
✅ Specific: "The application SHALL enforce password policy: minimum 12 characters, uppercase + lowercase + digit + special character, no dictionary words, no reuse of last 12 passwords, password expires after 90 days"

---

**Pitfall 4: Skipping Threat Modeling for "Simple" High-Risk Apps**

**Symptom:** "This app is simple, we don't need threat modeling"

**Why it's bad:** Policy says threat modeling MANDATORY for High-Risk. "Simple" apps often have non-obvious threats.

**Solution:**

- Follow policy - High-Risk = threat modeling required, no exceptions
- If app truly simple, threat modeling will be quick (30-60 min workshop)
- Document all threat modeling, even for simple apps
- If you want exception, request formal exception from CISO with justification


**Example:**
❌ "Simple" High-Risk app: Marketing website (public content) → "No threat model needed, it's just a website"
✅ Correct approach: "Marketing website handles contact form submissions (potential injection), has CMS admin panel (needs strong auth), uses third-party analytics (data leakage risk). Conducted threat modeling workshop, identified 15 threats, documented countermeasures."

---

**Pitfall 5: Outdated Documentation (>12 Months)**

**Symptom:** All required documents exist, but all dated 2+ years ago

**Why it's bad:** Security requirements change (new threats, new regulations). Outdated docs don't reflect current state.

**Solution:**

- For High-Risk apps: SRS, threat model, architecture review should be <12 months old
- For Medium-Risk apps: <24 months acceptable
- Update documents when major changes occur (don't wait for scheduled review)
- Version control everything - show document is actively maintained


**Example:**
❌ "SRS exists, dated 2022-03-15" (almost 4 years old!) - app has had 3 major releases since then
✅ "SRS v4.2 dated 2025-11-20" (updated before latest major release)

---

**Pitfall 6: No Requirements Traceability**

**Symptom:** Requirements exist, code exists, tests exist, but no linkage

**Why it's bad:** Can't prove requirements are implemented. Can't prove tests validate requirements. Audit nightmare.

**Solution:**

- Use requirements management tool (Jira, Azure DevOps, etc.)
- Link requirements → implementation → tests
- Even simple traceability (spreadsheet) better than nothing
- Maintain traceability throughout development (not after the fact)


**Example:**
❌ "We have 50 security requirements in SRS, we have 500 test cases, but we don't know which tests validate which requirements"
✅ "Traceability matrix shows: SEC-REQ-001 (MFA requirement) → Story DEV-1234 (MFA implementation) → Test Cases TEST-401, TEST-402, TEST-403 (MFA validation tests)"

---

**Pitfall 7: Accepting "N/A" Without Justification**

**Symptom:** Many "N/A" answers with no explanation

**Why it's bad:** N/A often means "We didn't want to do this" not "This genuinely doesn't apply"

**Solution:**

- Every N/A requires brief justification
- "N/A - Application has no user authentication (public read-only content)" ✅
- "N/A" with no explanation ❌
- Challenge N/A during review - is it really not applicable?


**Example:**
❌ "Threat modeling? N/A" (no justification - is this really N/A or just not done?)
✅ "Threat modeling? N/A - Low-Risk application per policy (threat modeling optional for Low-Risk)"

---

**Pitfall 8: Architecture Review Findings Not Remediated**

**Symptom:** Architecture review identified 10 High findings, none addressed

**Why it's bad:** Policy requires Critical/High findings remediated before production deployment (High-Risk apps)

**Solution:**

- Track architecture findings like vulnerabilities
- Assign owners and due dates
- Verify remediation before deployment
- If can't remediate, document risk acceptance (CISO approval for High-Risk)


**Example:**
❌ "Architecture review conducted 6 months ago, identified 5 High findings, all still open, app deployed to production anyway"
✅ "Architecture review conducted, 5 High findings identified, 4 remediated (evidence: Jira tickets), 1 accepted risk (CISO approval on file, compensating controls documented)"

---

**Pitfall 9: One-Time Assessment (Never Updated)**

**Symptom:** First assessment done, filed away, never looked at again

**Why it's bad:** Applications change, threats change, requirements change. One-time assessment becomes obsolete.

**Solution:**

- Schedule recurring assessments (quarterly for High-Risk, annually for Medium/Low-Risk)
- Trigger assessments on major changes (architecture change, major release, security incident)
- Update assessment workbook (don't start from scratch each time)
- Track trends (is compliance improving or declining?)


**Example:**
❌ "Initial assessment done in 2023, app has had 5 major releases since, no reassessment"
✅ "Initial assessment Q1 2023, reassessed Q1 2024, Q1 2025, Q1 2026 - compliance improving over time (70% → 85% → 92% → 95%)"

---

**Pitfall 10: Assessor Not Qualified**

**Symptom:** Developer with no security background conducting assessment

**Why it's bad:** Assessor doesn't understand security requirements, accepts inadequate controls, misses gaps

**Solution:**

- Assessor should be Security Architect or someone with security training
- If Product Manager/Developer conducts assessment, Security Architect must review
- Provide training to assessors (how to assess security requirements)
- Use this guide (you're reading it!) to educate assessors


**Example:**
❌ "Junior developer filled out assessment - thought password length requirement is a 'security requirement' (it's a security control implementation detail, not a requirement)"
✅ "Security Architect conducted assessment with Product Manager - correctly identified requirements vs. controls, found gaps in authentication requirements"

---

# Quality Checklist

Use this checklist before submitting assessment for review.

## Completeness Checks

**Sheet 1: Application Profile**

- [ ] All application information fields completed (no blanks)
- [ ] Application Owner contact information current
- [ ] Data types and sensitivity accurately documented
- [ ] Deployment environment and internet accessibility specified


**Sheet 2: Risk Classification**

- [ ] All risk criteria scored (no blanks)
- [ ] Risk classification calculated correctly
- [ ] Classification justified and reasonable
- [ ] Classification approved by Security Architect (signature/email)


**Sheet 3: Security Requirements Documentation**

- [ ] SRS existence determined (Yes/No/N/A)
- [ ] If Yes: document title, location, version, date provided
- [ ] Functional security requirements assessed (all categories)
- [ ] Non-functional security requirements assessed
- [ ] Data protection requirements assessed
- [ ] Evidence documented for all "Yes" answers


**Sheet 4: Threat Modeling Status**

- [ ] Threat modeling status determined (Yes/No/N/A)
- [ ] If Yes: document title, location, methodology, date provided
- [ ] Threat count documented
- [ ] Mitigation status documented
- [ ] Quality criteria assessed (diagrams, trust boundaries, countermeasures, residual risks)
- [ ] Evidence documented


**Sheet 5: Architecture Review Status**

- [ ] Architecture review status determined (Yes/No/N/A)
- [ ] If Yes: review report title, location, reviewer, date provided
- [ ] Findings count documented
- [ ] Critical/High findings remediation status documented
- [ ] Quality criteria assessed (diagrams, controls, integrations, approval)
- [ ] Evidence documented


**Sheet 6: Requirements Traceability**

- [ ] Traceability matrix existence determined
- [ ] If Yes: format/location documented
- [ ] Traceability coverage percentages documented (design, implementation, testing)
- [ ] Tool/system used documented
- [ ] Evidence documented


**Sheet 7: Compliance Checklist**

- [ ] All checklist items auto-populated from previous sheets
- [ ] Compliance score calculated correctly
- [ ] No manual overrides without justification


**Sheet 8: Gap Analysis**

- [ ] All gaps from previous sheets documented
- [ ] Each gap has severity, remediation action, responsible party, target date
- [ ] Critical gaps have realistic remediation plans (<30 days)
- [ ] Gap prioritization makes sense (critical before low)


**Sheet 9: Evidence Register**

- [ ] Evidence registered for all "Yes" answers
- [ ] Evidence locations are specific (not "SharePoint" but "SharePoint > Projects > X > Y > file.doc")
- [ ] Evidence dates documented
- [ ] Evidence owners documented
- [ ] Evidence verified (spot-check at least 20%)


**Sheet 10: Approval & Sign-Off**

- [ ] Assessment summary completed
- [ ] Assessor information and signature provided
- [ ] Security Architect review and recommendation provided
- [ ] CISO approval provided (if High-Risk application)
- [ ] Next review date calculated and scheduled


## Quality Checks

**Overall Assessment Quality:**

- [ ] No "Yes" answers without evidence
- [ ] No "N/A" answers without justification
- [ ] Evidence locations are specific and accessible
- [ ] Formulas calculate correctly (spot-check)
- [ ] Conditional formatting applied correctly (status colors)
- [ ] No obvious errors (typos, incorrect dates, impossible values)


**Substantive Quality:**

- [ ] Risk classification matches application characteristics
- [ ] Security requirements are specific and testable (not vague)
- [ ] Threat modeling scope matches application complexity
- [ ] Architecture review findings severity matches descriptions
- [ ] Traceability coverage is realistic (not 100% if gaps exist)
- [ ] Gap remediation plans are realistic (not "30 days" for everything)


**Evidence Quality:**

- [ ] Evidence is current (<12 months for High-Risk)
- [ ] Evidence is complete (full documents, not excerpts unless noted)
- [ ] Evidence is attributable (clearly for this application)
- [ ] Evidence is verifiable (auditor can access)


## Pre-Submission Checklist

Before submitting assessment for approval:

- [ ] Self-review using this checklist completed
- [ ] All quality checks passed
- [ ] Evidence package prepared (all evidence in one folder)
- [ ] Application Owner has reviewed and confirmed accuracy
- [ ] Ready for Security Architect peer review
- [ ] Assessment status set to "Final" (not "Draft")


## Post-Approval Checklist

After assessment approved:

- [ ] Workbook saved with final name: `ISMS-A826-Requirements-APP-XXX-YYYYMMDD.xlsx`
- [ ] Workbook and evidence filed in evidence repository
- [ ] Link to assessment added to application inventory record
- [ ] Next assessment scheduled (calendar reminder)
- [ ] If gaps identified: Gap remediation tracking initiated (Sheet 8)
- [ ] Assessment summary communicated to stakeholders (Application Owner, Development Manager)


---

# Review & Approval Process

## Peer Review (Security Architect)

**Timing:** After assessor completes workbook, before final approval

**Reviewer:** Security Architect (not the person who conducted assessment)

**Review Focus:**
1. **Completeness:** All sheets completed, no blanks
2. **Evidence:** Spot-check evidence (verify 20% of evidence claims)
3. **Accuracy:** Challenge assumptions, validate risk classification
4. **Consistency:** Check for contradictions across sheets
5. **Compliance:** Verify policy requirements met

**Review Outputs:**

- Review notes documented in Sheet 10
- Recommendation: Approve / Approve with Conditions / Require Remediation / Reject
- Feedback provided to assessor (if revisions needed)


**Common Review Findings:**

- Missing evidence locations (assessor said "Yes" but no document specified)
- Risk classification questionable (needs re-scoring)
- Gaps underestimated (Low severity when should be High)
- Evidence outdated (documents >12 months old)
- Requirements too vague (not specific/testable)


## Application Owner Review

**Timing:** After Security Architect peer review, before final approval

**Reviewer:** Application Owner / Product Manager

**Review Focus:**
1. **Factual Accuracy:** Application description, data types, user base correct?
2. **Gap Acknowledgment:** Agree with identified gaps?
3. **Remediation Feasibility:** Remediation plans realistic given business constraints?
4. **Approval:** Ready to commit to remediation plan?

**Review Outputs:**

- Confirmation of factual accuracy
- Agreement with gap analysis
- Commitment to remediation (if gaps exist)
- Sign-off in Sheet 10


## CISO Approval (High-Risk Applications Only)

**Timing:** After Security Architect and Application Owner reviews

**Reviewer:** CISO

**Review Focus:**
1. **Risk Acceptance:** Comfortable with identified gaps and residual risk?
2. **Remediation Plans:** Adequate given application risk?
3. **Policy Compliance:** High-Risk requirements met?
4. **Strategic Alignment:** Fits organizational security strategy?

**Approval Outputs:**

- Approval decision: Approved / Approved with Conditions / Rejected
- Conditions documented (if conditional approval)
- Sign-off in Sheet 10


**Rejection Reasons:**

- Critical gaps not addressed (e.g., High-Risk app with no threat model)
- Remediation plans unrealistic or too slow
- Risk classification disputed (should be higher risk)
- Inadequate evidence quality


## Continuous Improvement

**After Each Assessment:**
1. **Lessons Learned:** What went well? What didn't?
2. **Process Improvements:** Update this guide based on feedback
3. **Template Updates:** Update SRS template, threat model template, etc.
4. **Training Needs:** Identify gaps in assessor knowledge
5. **Tool Enhancements:** Improve workbook formulas, validations, etc.

**Metrics to Track:**

- Time to complete assessment (efficiency)
- Assessment pass rate (first-time quality)
- Gap remediation rate (effectiveness)
- Repeat findings (are gaps being fixed or recurring?)


---

# Conclusion

This User Completion Guide provides comprehensive instructions for completing the Security Requirements Assessment Workbook (ISMS-IMP-A.8.25-26-29-S1).

**Key Takeaways:**

- Answer based on **evidence**, not assumptions
- Be **specific** (document titles, locations, dates)
- **Don't skip** required activities (threat modeling for High-Risk is mandatory)
- **Document gaps** honestly - that's the point of assessment
- **Follow up** on gaps - assessment without remediation is useless


**For Support:**

- Review ISMS-POL-A.8.25-26-29 Section 2 for policy requirements
- Contact Security Architecture team for technical questions
- Use this guide's question-by-question guidance (Section 4)
- Refer to example assessments (if available)


**Next Steps:**
1. Read this User Completion Guide thoroughly
2. Gather prerequisites (Section 2)
3. Complete workbook (Section 3-4)
4. Self-review using quality checklist (Section 7)
5. Submit for Security Architect peer review (Section 8)

Good luck with your assessment!

---

# PART II: TECHNICAL SPECIFICATION

[*Note: PART II will contain detailed Excel workbook structure, column definitions, formulas, data validation rules, and technical notes for Python script developers. This section is typically 400-800 lines and includes detailed specifications for generating the workbook programmatically.*]

[*Due to token constraints, PART II will be provided separately if needed. The structure follows the pattern established in A.8.24 and A.8.23 implementations, with detailed sheet-by-sheet column specifications, formula definitions, and Python script integration points.*]

---

**END OF PART I: USER COMPLETION GUIDE**

**Document Status:** ✅ READY FOR REVIEW (PART I Complete, PART II Pending)
# PART II: TECHNICAL SPECIFICATION

# Instructions for Workbook Development

This section provides detailed technical specifications for creating the Security Requirements Assessment Excel workbook, either manually or via Python script (`generate_a825_26_29_1_security_requirements.py`).

## Workbook Overview

**Filename Format:** `ISMS-A826-Requirements-[APP-ID]-[YYYYMMDD].xlsx`

**Example:** `ISMS-A826-Requirements-APP-CUST-20260123.xlsx`

**Total Sheets:** 10

**Excel Compatibility:** Excel 2016+ (Office 365 recommended for best formula support)

**File Size Estimate:** 500KB - 2MB depending on evidence attachments

---

# Common Structure Elements

## Standard Column Widths

| Column Type | Width (pixels) | Width (Excel units) |
|-------------|----------------|---------------------|
| ID Column (A) | 80 | 12 |
| Question/Description | 400 | 60 |
| Answer/Status | 150 | 22 |
| Evidence/Location | 300 | 45 |
| Date | 120 | 18 |
| Comments/Notes | 300 | 45 |

## Standard Colors (Fill)

**Headers:**

- Main Section Header: RGB(0, 51, 102) / #003366 (Dark Blue)
- Sub-Header: RGB(68, 114, 196) / #4472C4 (Blue)
- Column Header: RGB(217, 217, 217) / #D9D9D9 (Light Gray)


**Input Cells:**

- User Input Required: RGB(255, 255, 204) / #FFFFCC (Light Yellow)
- Auto-Calculated: RGB(217, 217, 217) / #D9D9D9 (Light Gray) - Protected


**Status Indicators:**

- Compliant (✅): RGB(198, 239, 206) / #C6EFCE (Light Green)
- Partial (⚠️): RGB(255, 235, 156) / #FFEB9C (Light Yellow)
- Non-Compliant (❌): RGB(255, 199, 206) / #FFC7CE (Light Red)
- N/A: RGB(237, 237, 237) / #EDEDED (Gray)


## Standard Fonts

- **Headers:** Calibri 14pt Bold, White text
- **Sub-Headers:** Calibri 11pt Bold, White text
- **Column Headers:** Calibri 10pt Bold, Black text
- **Body Text:** Calibri 10pt, Black text
- **Instructions:** Calibri 9pt, Italic, Gray text


## Data Validation Standards

**Yes/No Dropdowns:**
```
=Yes,No,N/A
```

**Status Dropdowns:**
```
=✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A
```

**Risk Classification:**
```
=High Risk,Medium Risk,Low Risk
```

**Approval Status:**
```
=Draft,Final,Approved,Requires Remediation
```

---

# Sheet 1: Application Profile

## Purpose
Document basic application information for assessment context.

## Sheet Structure

**Rows 1-2:** Header Section

- A1:G1 merged: "Application Profile" (Dark Blue header, white text, 14pt bold)
- A2:G2 merged: "Basic application information and characteristics" (Blue sub-header, white text, 11pt)


**Row 3:** Column Headers
| Column | Header | Width | Format |
|--------|--------|-------|--------|
| A | Field | 200px | Gray fill, bold, centered |
| B | Value | 300px | Gray fill, bold, centered |
| C | Evidence Location | 300px | Gray fill, bold, centered |
| D | Date | 120px | Gray fill, bold, centered |
| E | Status | 120px | Gray fill, bold, centered |
| F | Verified By | 150px | Gray fill, bold, centered |
| G | Notes | 250px | Gray fill, bold, centered |

**Rows 4-20:** Data Entry Section

### Row 4: Application Name

- A4: "Application Name" (bold)
- B4: [User Input] - Yellow fill
- C4: "Application Inventory - [Location]" - Yellow fill
- D4: [Date] - Yellow fill, Date format (DD.MM.YYYY)
- E4: Auto-status (if B4 not blank → "✅ Complete", else "❌ Incomplete")
- F4: [User Input] - Yellow fill
- G4: [User Input] - Yellow fill


### Row 5: Application ID

- A5: "Application ID" (bold)
- B5: [User Input - format: APP-XXX] - Yellow fill, Data validation: Text length 3-20
- C5-G5: Same structure as Row 4


### Row 6: Application Owner

- A6: "Application Owner" (bold)
- B6: [User Input - Name] - Yellow fill
- C6: "Organizational Chart / HR System" - Yellow fill
- D6-G6: Same structure as Row 4


### Row 7: Owner Department

- A7: "Owner Department" (bold)
- B7: [User Input] - Yellow fill


### Row 8: Owner Contact Email

- A8: "Owner Contact Email" (bold)
- B8: [User Input] - Yellow fill, Data validation: Email format check


### Row 9: Application Description - Business Purpose

- A9: "Business Purpose" (bold)
- B9: [User Input - Text area, merged B9:B11] - Yellow fill, Wrap text
- C9-G9: Evidence reference (merged C9:C11)


### Row 12: Application Description - User Base

- A12: "User Base" (bold)
- B12: [User Input] - Yellow fill
- **Example text in comments:** "External customers (~10,000 active users)"


### Row 13: Application Description - Technology Stack

- A13: "Technology Stack" (bold)
- B13: [User Input - Text area, merged B13:B14] - Yellow fill, Wrap text
- **Example text in comments:** "Frontend: React.js, Backend: Node.js, Database: PostgreSQL, Infrastructure: AWS"


### Row 15: Data Types Processed

- A15: "Data Types Processed" (bold)
- B15: [User Input - Multiline] - Yellow fill, Wrap text
- **Data validation dropdown:**

```
=PII (Names/Emails/Addresses),Financial Data,Health Data (PHI),Authentication Credentials,Business Sensitive,Public Information
```

- **Allow multiple selections via comment instruction:** "Check all that apply - separate with commas"


### Row 16: Data Classification (Highest)

- A16: "Data Classification (Highest)" (bold)
- B16: [Dropdown] - Yellow fill
- **Data validation:**

```
=Confidential/Restricted,Internal Use,Public
```

### Row 17: Regulatory Scope

- A17: "Regulatory Scope" (bold)
- B17: [User Input - Multiline] - Yellow fill, Wrap text
- **Data validation dropdown (multi-select via comments):**

```
=GDPR,FADP,PCI DSS,HIPAA,SOX,DORA,NIS2,Industry-Specific,None
```

### Row 18: Deployment Model

- A18: "Deployment Model" (bold)
- B18: [Dropdown] - Yellow fill
- **Data validation:**

```
=On-Premises,Cloud (AWS/Azure/GCP),Hybrid,SaaS (Vendor-Hosted)
```

### Row 19: Internet Accessibility

- A19: "Internet Accessibility" (bold)
- B19: [Dropdown] - Yellow fill
- **Data validation:**

```
=Public Internet,VPN Required,Internal Network Only,Air-Gapped
```

### Row 20: Assessment Period

- A20: "Assessment Period" (bold)
- B20: [User Input] - Yellow fill
- **Example text in comments:** "Q4 2025 (October - December 2025)"


## Formulas

**E4 (Status for Application Name):**
```excel
=IF(B4<>"","✅ Complete","❌ Incomplete")
```

**Apply same formula pattern to E5:E19** (adjust row reference)

**Conditional Formatting for Column E:**

- Rule 1: If cell contains "✅" → Green fill (RGB 198, 239, 206)
- Rule 2: If cell contains "❌" → Red fill (RGB 255, 199, 206)


## Sheet Protection

**Protect:** Column E (formulas), Headers (Rows 1-3)
**Unlock:** Columns B, C, D, F, G (user input areas)

---

# Sheet 2: Risk Classification

## Purpose
Document and validate application risk classification using policy criteria.

## Sheet Structure

**Rows 1-2:** Header Section

- A1:J1 merged: "Application Risk Classification" (Dark Blue header)
- A2:J2 merged: "Risk scoring based on ISMS-POL-A.8.25-26-29 Section 2 criteria" (Blue sub-header)


**Row 3:** Instructions

- A3:J3 merged: "Score each criterion 0-5 using the scoring guidelines. Weighted total determines risk classification: High Risk ≥3.5, Medium Risk 2.0-3.4, Low Risk <2.0" (Italic, gray text)


**Row 4:** Column Headers
| Column | Header | Width |
|--------|--------|-------|
| A | Risk Criterion | 200px |
| B | Weight | 80px |
| C | Score (0-5) | 80px |
| D | Weighted Score | 100px |
| E | Scoring Guidelines | 400px |
| F | Justification | 250px |
| G | Evidence | 250px |
| H | Verified | 100px |

**Rows 5-9:** Risk Scoring Criteria

### Row 5: Data Sensitivity

- A5: "Data Sensitivity" (bold)
- B5: "30%" (centered, gray fill, protected)
- C5: [User Input 0-5] - Yellow fill, Data validation: Whole number 0-5
- D5: `=B5*C5` (formula, gray fill, protected, number format: 0.00)
- E5: "5=PII+Financial+PHI, 4=Confidential Business, 3=Internal, 2=Low-Sensitivity, 1=Public Only, 0=No Data" (Wrap text)
- F5: [User Input] - Yellow fill, Wrap text
- G5: [User Input] - Yellow fill
- H5: [Dropdown: Yes/No] - Yellow fill


### Row 6: User Base

- A6: "User Base" (bold)
- B6: "20%" (centered, gray fill, protected)
- C6: [User Input 0-5] - Yellow fill, Data validation: Whole number 0-5
- D6: `=B6*C6` (formula, gray fill, protected, number format: 0.00)
- E6: "5=Public/Anonymous Users, 4=Partners/Contractors, 3=Mixed Internal/External, 2=Employees Only, 1=Restricted Group (<20)" (Wrap text)
- F6-H6: Same as Row 5


### Row 7: Internet Exposure

- A7: "Internet Exposure" (bold)
- B7: "25%" (centered, gray fill, protected)
- C7: [User Input 0-5] - Yellow fill, Data validation: Whole number 0-5
- D7: `=B7*C7` (formula)
- E7: "5=Public Internet, 4=Internet+VPN, 3=Hybrid, 2=Internal+Remote Access, 1=Isolated Internal, 0=Air-Gapped" (Wrap text)
- F7-H7: Same as Row 5


### Row 8: Business Criticality

- A8: "Business Criticality" (bold)
- B8: "15%" (centered, gray fill, protected)
- C8: [User Input 0-5] - Yellow fill, Data validation: Whole number 0-5
- D8: `=B8*C8` (formula)
- E8: "5=Critical (Outage=Business Stop), 4=High Impact, 3=Moderate Impact, 2=Low Impact, 1=Minimal Impact" (Wrap text)
- F8-H8: Same as Row 5


### Row 9: Regulatory Scope

- A9: "Regulatory Scope" (bold)
- B9: "10%" (centered, gray fill, protected)
- C9: [User Input 0-5] - Yellow fill, Data validation: Whole number 0-5
- D9: `=B9*C9` (formula)
- E9: "5=Multiple Regulations, 4=One Major Regulation, 3=Industry Standards, 2=Internal Policies Only, 1=Minimal" (Wrap text)
- F9-H9: Same as Row 5


**Row 10:** Totals Row

- A10: "TOTAL WEIGHTED SCORE" (bold, dark gray fill)
- B10: "100%" (centered, dark gray fill, protected)
- C10: [Auto-sum display] - Formula: `=SUM(C5:C9)/5` (show average score, gray fill, protected)
- D10: `=SUM(D5:D9)` (bold, dark gray fill, protected, number format: 0.00)
- **Conditional Formatting for D10:**
  - If ≥3.5 → Red fill (High Risk)
  - If 2.0-3.4 → Yellow fill (Medium Risk)
  - If <2.0 → Green fill (Low Risk)


**Row 12:** Risk Classification Result

- A12: "Risk Classification" (bold)
- B12: `=IF(D10>=3.5,"High Risk",IF(D10>=2.0,"Medium Risk","Low Risk"))` (formula, large font 14pt, bold)
- **Conditional Formatting for B12:**
  - If "High Risk" → Red fill, white text
  - If "Medium Risk" → Yellow fill, black text
  - If "Low Risk" → Green fill, white text


**Row 13:** Classification Approved By

- A13: "Classification Approved By" (bold)
- B13: [User Input - Name] - Yellow fill
- C13: "Approval Date" (bold)
- D13: [User Input - Date] - Yellow fill, Date format


**Row 14:** Next Review Date

- A14: "Next Review Date" (bold)
- B14: `=DATE(YEAR(D13)+1,MONTH(D13),DAY(D13))` (formula - 1 year from approval, gray fill, Date format)


**Row 15:** Override Justification (if needed)

- A15: "Override Justification (if applicable)" (bold)
- B15:H15 merged: [User Input - Text area] - Yellow fill, Wrap text
- **Instruction in comments:** "If you believe formula classification is incorrect, document justification here"


## Data Validation

**Score Columns (C5:C9):**
```
Type: Whole number
Data: Between 0 and 5
Error message: "Score must be between 0 and 5"
```

**Verified Column (H5:H9):**
```
=Yes,No
```

## Conditional Formatting

**D10 (Total Weighted Score):**
```
Rule 1: =$D$10>=3.5 → Fill: RGB(255,199,206), Font: Bold
Rule 2: =AND($D$10>=2.0,$D$10<3.5) → Fill: RGB(255,235,156), Font: Bold
Rule 3: =$D$10<2.0 → Fill: RGB(198,239,206), Font: Bold
```

**B12 (Risk Classification):**
```
Rule 1: =$B$12="High Risk" → Fill: RGB(255,0,0), Font: White, Bold, 14pt
Rule 2: =$B$12="Medium Risk" → Fill: RGB(255,192,0), Font: Black, Bold, 14pt
Rule 3: =$B$12="Low Risk" → Fill: RGB(0,176,80), Font: White, Bold, 14pt
```

---

# Sheet 3: Security Requirements Documentation

## Purpose
Assess completeness of Security Requirements Specification (SRS).

## Sheet Structure

**Rows 1-2:** Header Section

- A1:H1 merged: "Security Requirements Documentation Status" (Dark Blue header)
- A2:H2 merged: "Assessment of SRS existence, completeness, and currency" (Blue sub-header)


**Row 3:** Column Headers
| Column | Header | Width |
|--------|--------|-------|
| A | Requirement Category | 250px |
| B | Exists? (Y/N/NA) | 100px |
| C | Document Title & Location | 300px |
| D | Version | 80px |
| E | Last Updated | 100px |
| F | Status | 120px |
| G | Evidence | 250px |
| H | Notes | 250px |

**Row 4-5:** SRS Existence

### Row 4: SRS Exists?

- A4: "1.1 Security Requirements Specification (SRS) Exists?" (bold)
- B4: [Dropdown: Yes/No/N/A] - Yellow fill
- C4: [User Input - Document title and location] - Yellow fill, Wrap text
- D4: [User Input - Version] - Yellow fill
- E4: [User Input - Date] - Yellow fill, Date format
- F4: Formula (see below)
- G4: [User Input - Evidence link] - Yellow fill
- H4: [User Input - Notes] - Yellow fill, Wrap text


**F4 Formula (Status):**
```excel
=IF(B4="Yes",IF(E4<>"",IF((TODAY()-E4)<=365,"✅ Compliant","⚠️ Partial - Outdated"),"⚠️ Partial - No Date"),IF(B4="No","❌ Non-Compliant",IF(B4="N/A","N/A","")))
```

**Logic:**

- If Yes + Date < 12 months old → ✅ Compliant
- If Yes + Date > 12 months old → ⚠️ Partial - Outdated
- If Yes + No date → ⚠️ Partial - No Date
- If No → ❌ Non-Compliant
- If N/A → N/A


### Row 5: SRS Completeness Header

- A5:H5 merged: "1.2 Functional Security Requirements Coverage" (bold, gray fill)


**Rows 6-11:** Functional Security Requirements

### Row 6: Authentication Requirements

- A6: "Authentication Requirements Specified?" (indent with space or bullet)
- B6: [Dropdown: Yes/No/N/A] - Yellow fill
- C6: [User Input - Reference to section/page in SRS] - Yellow fill
- D6-E6: N/A (gray fill, protected)
- F6: Formula (simplified status: Yes=Compliant, No=Non-Compliant, N/A=N/A)
- G6-H6: [User Input] - Yellow fill


**F6 Formula:**
```excel
=IF(B6="Yes","✅ Compliant",IF(B6="No","❌ Non-Compliant",IF(B6="N/A","N/A","")))
```

### Row 7: Authorization Requirements

- Same structure as Row 6, adjust labels


### Row 8: Input Validation Requirements

- Same structure as Row 6


### Row 9: Cryptography Requirements

- Same structure as Row 6


### Row 10: Logging Requirements

- Same structure as Row 6


### Row 11: API Security Requirements

- Same structure as Row 6


### Row 12: Non-Functional Security Requirements Header

- A12:H12 merged: "1.3 Non-Functional Security Requirements Coverage" (bold, gray fill)


**Rows 13-15:** Non-Functional Requirements

### Row 13: Performance Requirements (Under Security Load)

- Same structure as Row 6


### Row 14: Resilience Requirements (Fail Secure)

- Same structure as Row 6


### Row 15: Secure Defaults

- Same structure as Row 6


### Row 16: Data Protection Requirements Header

- A16:H16 merged: "1.4 Data Protection Requirements Coverage" (bold, gray fill)


**Rows 17-20:** Data Protection Requirements

### Row 17: Data Classification Documented

- Same structure as Row 6


### Row 18: Encryption Requirements

- Same structure as Row 6


### Row 19: Retention Requirements

- Same structure as Row 6


### Row 20: Deletion Requirements

- Same structure as Row 6


### Row 21: Privacy Requirements (if applicable)

- Same structure as Row 6


**Row 23:** Overall SRS Completeness Score

- A23: "Overall SRS Completeness Score" (bold, dark gray fill)
- B23-E23: merged, blank
- F23: Formula (% compliant)
- G23-H23: merged, blank


**F23 Formula:**
```excel
=COUNTIF(F6:F21,"✅ Compliant")/(COUNTIF(B6:B21,"Yes")+COUNTIF(B6:B21,"No"))*100&"%"
```

**Logic:** Count compliant items / Count total applicable items (Yes or No, exclude N/A) × 100%

**Conditional Formatting for F23:**

- If ≥90% → Green fill
- If 70-89% → Yellow fill
- If <70% → Red fill


## Data Validation

**B4, B6:B21 (Yes/No/N/A dropdowns):**
```
=Yes,No,N/A
```

## Conditional Formatting

**Column F (Status) - Apply to F4:F21:**
```
Rule 1: Cell contains "✅" → Fill: RGB(198,239,206)
Rule 2: Cell contains "⚠️" → Fill: RGB(255,235,156)
Rule 3: Cell contains "❌" → Fill: RGB(255,199,206)
Rule 4: Cell contains "N/A" → Fill: RGB(237,237,237)
```

---

# Sheet 4: Threat Modeling Status

## Purpose
Assess threat modeling execution and quality.

## Sheet Structure

**Rows 1-2:** Header Section

- A1:I1 merged: "Threat Modeling Status" (Dark Blue header)
- A2:I2 merged: "Assessment of threat modeling execution for High/Medium-Risk applications" (Blue sub-header)


**Row 3:** Policy Requirement Reminder

- A3:I3 merged: "Policy Requirement: Threat modeling MANDATORY for High-Risk apps, RECOMMENDED for Medium-Risk apps, OPTIONAL for Low-Risk apps" (Bold, yellow fill, wrapped)


**Row 4:** Column Headers
| Column | Header | Width |
|--------|--------|-------|
| A | Assessment Question | 300px |
| B | Answer | 120px |
| C | Details | 300px |
| D | Date | 100px |
| E | Count/Metrics | 120px |
| F | Status | 120px |
| G | Evidence | 250px |
| H | Verified | 100px |
| I | Notes | 200px |

**Rows 5-6:** Threat Modeling Execution

### Row 5: Threat Modeling Conducted?

- A5: "2.1 Was threat modeling conducted?" (bold)
- B5: [Dropdown: Yes/No/N/A] - Yellow fill
- C5: [User Input - Document title & location] - Yellow fill, Wrap text
- D5: [User Input - Date] - Yellow fill, Date format
- E5: N/A (gray fill)
- F5: Formula (see below)
- G5: [User Input - Evidence link] - Yellow fill
- H5: [Dropdown: Yes/No] - Yellow fill
- I5: [User Input] - Yellow fill, Wrap text


**F5 Formula (Status):**
```excel
=IF(B5="Yes",IF(D5<>"",IF((TODAY()-D5)<=365,"✅ Compliant","⚠️ Partial - Outdated"),"⚠️ Partial - No Date"),IF(B5="No",IF('Sheet 2'!B12="High Risk","❌ Non-Compliant - REQUIRED","⚠️ Recommended"),IF(B5="N/A","N/A","")))
```

**Logic:**

- If Yes + Date < 12 months → ✅ Compliant
- If Yes + Date > 12 months → ⚠️ Partial - Outdated
- If No + High-Risk app → ❌ Non-Compliant - REQUIRED
- If No + Medium/Low-Risk → ⚠️ Recommended (not required)
- If N/A → N/A


### Row 6: Methodology Used

- A6: "Methodology Used" (indent)
- B6: [Dropdown] - Yellow fill
  - Data validation: `=STRIDE,PASTA,LINDDUN,Attack Trees,DREAD,Other`
- C6: [User Input - Description if "Other"] - Yellow fill
- D6-E6: N/A
- F6: Formula: `=IF(B6<>"","✅ Documented","❌ Not Documented")`
- G6-I6: [User Input] - Yellow fill


**Rows 7-10:** Threat Modeling Metrics

### Row 7: Threats Identified (Count)

- A7: "Threats Identified (Count)" (indent)
- B7: N/A
- C7: [User Input - Details] - Yellow fill
- D7: N/A
- E7: [User Input - Number] - Yellow fill, Number format
- F7: Formula: `=IF(E7>0,"✅ Threats Identified","❌ No Threats")`
- G7-I7: [User Input] - Yellow fill


### Row 8: Threats Mitigated (Count)

- A8: "Threats Mitigated (Count)" (indent)
- E8: [User Input - Number] - Yellow fill
- F8: Formula: `=IF(AND(E7>0,E8>0),TEXT(E8/E7,"0%")&" Mitigated","")`
- Other columns: [User Input] - Yellow fill


### Row 9: Threats Accepted Risk (Count)

- A9: "Threats Accepted Risk (Count)" (indent)
- E9: [User Input - Number] - Yellow fill
- Other columns: [User Input] - Yellow fill


### Row 10: Threats Outstanding (Count)

- A10: "Threats Outstanding (Count)" (indent)
- E10: Formula: `=IF(AND(E7>0,E8>=0,E9>=0),E7-E8-E9,"")` (auto-calculate)
- F10: Formula: `=IF(E10>0,"⚠️ Outstanding","✅ None Outstanding")`
- Other columns: [User Input] - Yellow fill


**Row 12:** Threat Model Quality Assessment Header

- A12:I12 merged: "2.2 Threat Model Quality Assessment" (bold, gray fill)


**Rows 13-16:** Quality Criteria

### Row 13: Architecture Diagrams Included?

- A13: "Architecture Diagrams Included?" (indent)
- B13: [Dropdown: Yes/No] - Yellow fill
- C13: [User Input - Types of diagrams] - Yellow fill
- F13: Formula: `=IF(B13="Yes","✅ Compliant","❌ Non-Compliant")`
- Other columns: [User Input] - Yellow fill


### Row 14: Trust Boundaries Identified?

- Same structure as Row 13


### Row 15: Countermeasures Documented?

- Same structure as Row 13


### Row 16: Residual Risks Documented?

- Same structure as Row 13


**Row 18:** Overall Threat Modeling Score

- A18: "Overall Threat Modeling Compliance Score" (bold, dark gray fill)
- F18: Formula (% compliant)


**F18 Formula:**
```excel
=COUNTIF(F5:F16,"✅*")/(COUNTIF(F5:F16,"✅*")+COUNTIF(F5:F16,"❌*")+COUNTIF(F5:F16,"⚠️*"))*100&"%"
```

## Conditional Formatting

**Column F (Status):**
```
Rule 1: Cell contains "✅" → Fill: RGB(198,239,206)
Rule 2: Cell contains "⚠️" → Fill: RGB(255,235,156)
Rule 3: Cell contains "❌" → Fill: RGB(255,199,206)
```

**E8 (Mitigation Percentage) - Color scale:**
```
Rule: If <50% → Red, 50-80% → Yellow, >80% → Green
```

---

# Sheet 5: Architecture Review Status

## Purpose
Assess security architecture review execution and findings remediation.

## Sheet Structure

**Similar structure to Sheet 4, adapted for architecture review.**

**Key Rows:**

- Row 5: Architecture Review Conducted? (Yes/No/N/A)
- Row 6: Review Report Title & Location
- Row 7: Reviewer Name (Security Architect)
- Row 8: Review Date
- Row 9: Findings Count (Total)
- Row 10: Critical Findings (Count)
- Row 11: High Findings (Count)
- Row 12: Medium Findings (Count)
- Row 13: Low Findings (Count)
- Row 15: Critical/High Findings Remediated? (Yes/Partial/No)
- Row 17-20: Quality Assessment (Diagrams Reviewed, Controls Validated, Integrations Reviewed, Approval Obtained)
- Row 22: Overall Architecture Review Compliance Score


**Key Formulas:**

**F5 (Architecture Review Status):**
```excel
=IF(B5="Yes",IF(D8<>"",IF((TODAY()-D8)<=365,"✅ Compliant","⚠️ Partial - Outdated"),"⚠️ Partial"),IF(B5="No",IF('Sheet 2'!B12="High Risk","❌ Non-Compliant - REQUIRED","⚠️ Recommended"),"N/A"))
```

**F15 (Critical/High Remediation Status):**
```excel
=IF(B15="Yes - All Remediated","✅ Compliant",IF(B15="Partial","⚠️ Partial",IF(B15="No - Outstanding","❌ Non-Compliant","N/A")))
```

---

# Sheet 6: Requirements Traceability

## Purpose
Assess requirements traceability from specification through implementation to testing.

## Sheet Structure

**Key Rows:**

- Row 5: Traceability Matrix Exists? (Yes/No)
- Row 6: Format/Location
- Row 7: Tool/System Used
- Row 8: Last Updated Date
- Row 10: % Requirements Traced to Design
- Row 11: % Requirements Traced to Implementation
- Row 12: % Requirements Traced to Test Cases
- Row 14: Overall Traceability Score


**Key Formulas:**

**F10-F12 (Traceability Coverage Status):**
```excel
=IF(E10>=90,"✅ Excellent",IF(E10>=80,"✅ Good",IF(E10>=60,"⚠️ Partial","❌ Inadequate")))
```

**F14 (Overall Traceability Score):**
```excel
=AVERAGE(E10,E11,E12)&"%"
```

**Conditional Formatting E10:E12:**
```
Rule 1: >=90 → Green
Rule 2: 80-89 → Light Green
Rule 3: 60-79 → Yellow
Rule 4: <60 → Red
```

---

# Sheet 7: Compliance Checklist

## Purpose
Auto-populated checklist summarizing compliance across all assessment areas.

## Sheet Structure

**Row 1-2:** Header

- A1:E1 merged: "Compliance Checklist - A.8.26 Security Requirements" (Dark Blue header)


**Row 3:** Column Headers
| Column | Header | Width |
|--------|--------|-------|
| A | Checklist Item | 400px |
| B | Compliant? | 120px |
| C | Source Sheet | 120px |
| D | Evidence | 300px |
| E | Notes | 250px |

**Rows 4-25:** Checklist Items (auto-populated from previous sheets)

### Row 4: Application Risk Classified

- A4: "1. Application risk classified (High/Medium/Low)" (with checkbox symbol ☐)
- B4: Formula: `=IF('Sheet 2'!B12<>"","☑ Yes","☐ No")`
- C4: "Sheet 2" (gray fill, protected)
- D4: Formula: `='Sheet 2'!G5` (pull evidence from Sheet 2)
- E4: [User Input] - Yellow fill


**Apply similar pattern for all checklist items:**

- Pull status from relevant sheet
- Convert to ☑ Yes / ☐ No format
- Reference source sheet
- Pull evidence automatically
- Allow notes


**Row 26:** Overall Compliance Score

- A26: "Overall Compliance Rate" (bold, dark gray fill)
- B26: Formula: `=COUNTIF(B4:B25,"☑ Yes")/COUNTA(B4:B25)*100&"%"`
- **Conditional Formatting:**
  - ≥90% → Green fill
  - 70-89% → Yellow fill
  - <70% → Red fill


**Row 27:** Compliance Status

- A27: "Compliance Status" (bold)
- B27: Formula: `=IF(VALUE(LEFT(B26,LEN(B26)-1))>=90,"✅ Compliant",IF(VALUE(LEFT(B26,LEN(B26)-1))>=70,"⚠️ Partial","❌ Non-Compliant"))`


---

# Sheet 8: Gap Analysis & Action Plan

## Purpose
Document identified gaps and remediation plan.

## Sheet Structure

**Row 1-2:** Header

- A1:K1 merged: "Gap Analysis & Remediation Action Plan" (Dark Blue header)


**Row 3:** Column Headers
| Column | Header | Width |
|--------|--------|-------|
| A | Gap ID | 80px |
| B | Gap Description | 300px |
| C | Sheet Reference | 120px |
| D | Severity | 100px |
| E | Policy Requirement | 200px |
| F | Remediation Action | 300px |
| G | Responsible Party | 150px |
| H | Target Date | 100px |
| I | Status | 120px |
| J | Completion Date | 100px |
| K | Evidence of Closure | 250px |

**Rows 4+:** Gap Entries

### Row 4: First Gap (Example)

- A4: "GAP-001" (auto-generate: `="GAP-"&TEXT(ROW()-3,"000")`)
- B4: [User Input - Gap description] - Yellow fill, Wrap text
- C4: [User Input - Sheet reference] - Yellow fill
- D4: [Dropdown] - Yellow fill
  - Data validation: `=Critical,High,Medium,Low`
- E4: [User Input - Policy section violated] - Yellow fill, Wrap text
- F4: [User Input - Remediation action] - Yellow fill, Wrap text
- G4: [User Input - Responsible party name] - Yellow fill
- H4: [User Input - Target date] - Yellow fill, Date format
- I4: [Dropdown] - Yellow fill
  - Data validation: `=Open,In Progress,Resolved,Risk Accepted`
- J4: [User Input - Completion date] - Yellow fill, Date format
- K4: [User Input - Evidence] - Yellow fill, Wrap text


**Conditional Formatting for Column D (Severity):**
```
Rule 1: ="Critical" → Red fill, White text, Bold
Rule 2: ="High" → Orange fill, Black text, Bold
Rule 3: ="Medium" → Yellow fill, Black text
Rule 4: ="Low" → Light blue fill, Black text
```

**Conditional Formatting for Column I (Status):**
```
Rule 1: ="Resolved" → Green fill
Rule 2: ="In Progress" → Yellow fill
Rule 3: ="Open" → White fill
Rule 4: ="Risk Accepted" → Light gray fill
```

**Conditional Formatting for Column H (Target Date) - Overdue Highlighting:**
```
Rule: =AND(H4<TODAY(),I4<>"Resolved",I4<>"Risk Accepted") → Red fill, Bold
```

**Row 100:** Gap Summary

- A100: "Gap Summary" (bold, dark gray fill)
- B100: `=COUNTA(A4:A99)&" Total Gaps"`
- C100: `=COUNTIF(D4:D99,"Critical")&" Critical"`
- D100: `=COUNTIF(D4:D99,"High")&" High"`
- E100: `=COUNTIF(D4:D99,"Medium")&" Medium"`
- F100: `=COUNTIF(D4:D99,"Low")&" Low"`
- I100: `=COUNTIF(I4:I99,"Resolved")&" Resolved, "&COUNTIF(I4:I99,"Open")&" Open"`


---

# Sheet 9: Evidence Register

## Purpose
Centralized register of all evidence supporting assessment.

## Sheet Structure

**Row 1-2:** Header

- A1:J1 merged: "Evidence Register" (Dark Blue header)


**Row 3:** Column Headers
| Column | Header | Width |
|--------|--------|-------|
| A | Evidence ID | 100px |
| B | Evidence Type | 120px |
| C | Evidence Title | 300px |
| D | Evidence Location | 350px |
| E | Date | 100px |
| F | Owner | 150px |
| G | Related Question(s) | 150px |
| H | Verified? | 100px |
| I | Verification Date | 120px |
| J | Verified By | 150px |

**Rows 4+:** Evidence Entries

### Row 4: First Evidence Entry

- A4: "EV-001" (auto-generate: `="EV-"&TEXT(ROW()-3,"000")`)
- B4: [Dropdown] - Yellow fill
  - Data validation: `=Document,Email,Screenshot,Meeting Minutes,Report,Spreadsheet,Tool Export,Other`
- C4: [User Input - Evidence title] - Yellow fill
- D4: [User Input - Location path] - Yellow fill, Wrap text
- E4: [User Input - Date] - Yellow fill, Date format
- F4: [User Input - Owner name] - Yellow fill
- G4: [User Input - Sheet.Question references] - Yellow fill
  - Example: "3.1, 4.1, 5.1"
- H4: [Dropdown: Yes/No/Issue] - Yellow fill
- I4: [User Input - Verification date] - Yellow fill, Date format
- J4: [User Input - Verifier name] - Yellow fill


**Conditional Formatting for Column H (Verified):**
```
Rule 1: ="Yes" → Green fill
Rule 2: ="No" → Yellow fill
Rule 3: ="Issue" → Red fill
```

**Row 100:** Evidence Summary

- A100: "Evidence Summary" (bold, dark gray fill)
- B100: `=COUNTA(A4:A99)&" Total Evidence Items"`
- H100: `=COUNTIF(H4:H99,"Yes")&" Verified, "&COUNTIF(H4:H99,"No")&" Pending, "&COUNTIF(H4:H99,"Issue")&" Issues"`


---

# Sheet 10: Approval & Sign-Off

## Purpose
Document assessment completion, review, and approval.

## Sheet Structure

**Rows 1-10:** Assessment Summary Section

### Row 1-2: Header

- A1:F1 merged: "Assessment Summary & Approval" (Dark Blue header, white text)


### Row 3: Assessment Period

- A3: "Assessment Period:" (bold)
- B3:F3 merged: [User Input] - Yellow fill


### Row 4: Assessment Date

- A4: "Assessment Date:" (bold)
- B4: [User Input - Date] - Yellow fill, Date format
- C4: "Application Name:" (bold)
- D4:F4 merged: Formula: `='Sheet 1'!B4` (auto-pull from Sheet 1)


### Row 5: Application Risk

- A5: "Application Risk:" (bold)
- B5: Formula: `='Sheet 2'!B12` (auto-pull from Sheet 2)
- **Conditional formatting:** Match risk classification colors from Sheet 2


### Row 6: Overall Compliance Score

- A6: "Overall Compliance Score:" (bold)
- B6: Formula: `='Sheet 7'!B26` (auto-pull from Sheet 7)
- **Conditional formatting:** Match compliance color scheme (Green/Yellow/Red)


### Row 7: Critical Gaps

- A7: "Critical Gaps:" (bold)
- B7: Formula: `='Sheet 8'!C100` (auto-pull Critical count from Sheet 8)
- **Conditional formatting:** If >0 → Red fill, Bold


### Row 8: Assessment Status

- A8: "Assessment Status:" (bold)
- B8: [Dropdown] - Yellow fill
  - Data validation: `=Draft,Final,Approved,Requires Remediation`
- **Conditional formatting:**
  - "Approved" → Green fill
  - "Final" → Blue fill
  - "Requires Remediation" → Red fill
  - "Draft" → Gray fill


**Rows 12-20:** Assessment Completed By

### Row 12: Section Header

- A12:F12 merged: "Assessment Completed By" (bold, gray fill)


### Row 13-19: Assessor Information

- A13: "Name:" | B13: [User Input] - Yellow fill
- A14: "Role/Title:" | B14: [User Input] - Yellow fill
- A15: "Department:" | B15: [User Input] - Yellow fill
- A16: "Email:" | B16: [User Input] - Yellow fill
- A17: "Date:" | B17: [User Input - Date] - Yellow fill, Date format
- A18: "Signature:" | B18: [User Input - /s/ Name] - Yellow fill
- A19: "Comments:" | B19:F19 merged: [User Input - Text area] - Yellow fill, Wrap text


**Rows 22-32:** Reviewed By - Security Architect

### Row 22: Section Header

- A22:F22 merged: "Reviewed By - Security Architect" (bold, gray fill)


### Row 23-28: Reviewer Information

- A23: "Name:" | B23: [User Input] - Yellow fill
- A24: "Date:" | B24: [User Input - Date] - Yellow fill, Date format
- A25: "Review Notes:" | B25:F28 merged: [User Input - Text area] - Yellow fill, Wrap text


### Row 29: Recommendation

- A29: "Recommendation:" (bold)
- B29:F29 merged: [Dropdown] - Yellow fill
  - Data validation: `=Approve,Approve with Conditions,Require Remediation,Reject`
- **Conditional formatting:**
  - "Approve" → Green fill
  - "Approve with Conditions" → Yellow fill
  - "Require Remediation" → Orange fill
  - "Reject" → Red fill


**Rows 34-45:** Approved By - CISO (High-Risk Apps Only)

### Row 34: Section Header

- A34:F34 merged: "Approved By - CISO (High-Risk Applications Only)" (bold, gray fill)


### Row 35-40: CISO Information

- A35: "Name:" | B35: [User Input] - Yellow fill
- A36: "Date:" | B36: [User Input - Date] - Yellow fill, Date format
- A37: "Approval Decision:" | B37:F37 merged: [Dropdown] - Yellow fill
  - Data validation: `=Approved,Approved with Conditions,Rejected`
- **Conditional formatting:** Same as Row 29
- A38: "Conditions/Notes:" | B38:F41 merged: [User Input - Text area] - Yellow fill, Wrap text


**Rows 43-48:** Next Review Details

### Row 43: Section Header

- A43:F43 merged: "Next Review Details" (bold, gray fill)


### Row 44-48: Next Review Information

- A44: "Next Assessment Date:" | B44: Formula (auto-calculate based on risk)
- A45: "Review Responsible:" | B45: [User Input] - Yellow fill
- A46: "Special Considerations:" | B46:F48 merged: [User Input - Text area] - Yellow fill, Wrap text


**B44 Formula (Next Assessment Date):**
```excel
=IF('Sheet 2'!B12="High Risk",DATE(YEAR(B17)+0,MONTH(B17)+3,DAY(B17)),DATE(YEAR(B17)+1,MONTH(B17),DAY(B17)))
```
**Logic:** High-Risk = +3 months (quarterly), Medium/Low-Risk = +12 months (annual)

---

# Python Script Integration Points

## Script Filename
`generate_a825_26_29_1_security_requirements.py`

## Key Functions

**1. create_workbook()**
```python
def create_workbook():
    """Initialize workbook with 10 sheets"""
    wb = openpyxl.Workbook()
    # Remove default sheet
    wb.remove(wb.active)
    # Create 10 sheets
    sheet_names = [
        "1. Application Profile",
        "2. Risk Classification",
        "3. Requirements Documentation",
        "4. Threat Modeling",
        "5. Architecture Review",
        "6. Requirements Traceability",
        "7. Compliance Checklist",
        "8. Gap Analysis",
        "9. Evidence Register",
        "10. Approval & Sign-Off"
    ]
    for name in sheet_names:
        wb.create_sheet(title=name)
    return wb
```

**2. setup_styles()**
```python
def setup_styles():
    """Define cell styles for consistent formatting"""
    # Header style
    header_style = NamedStyle(name="header")
    header_style.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    header_style.fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    header_style.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    
    # Similar definitions for sub_header, column_header, input_cell, formula_cell, status styles
    return styles_dict
```

**3. create_application_profile_sheet(ws, styles)**
```python
def create_application_profile_sheet(ws, styles):
    """Create Sheet 1: Application Profile"""
    # Set column widths
    ws.column_dimensions['A'].width = 30
    ws.column_dimensions['B'].width = 45
    # ... etc
    
    # Create headers
    ws.merge_cells('A1:G1')
    ws['A1'] = "Application Profile"
    ws['A1'].style = styles['header']
    
    # Create data rows
    # Row 4: Application Name
    ws['A4'] = "Application Name"
    ws['A4'].font = Font(bold=True)
    ws['B4'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
    
    # Add data validations
    dv = DataValidation(type="list", formula1='"High Risk,Medium Risk,Low Risk"', allow_blank=False)
    ws.add_data_validation(dv)
    dv.add(ws['B5'])  # Apply to specific cells
    
    # Add formulas
    ws['E4'] = '=IF(B4<>"","✅ Complete","❌ Incomplete")'
    
    # Add conditional formatting
    red_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
    rule = Rule(type="containsText", operator="containsText", text="❌", dxf=DifferentialStyle(fill=red_fill))
    ws.conditional_formatting.add('E4:E20', rule)
```

**4. create_risk_classification_sheet(ws, styles)**

- Similar structure for Sheet 2
- Focus on formula creation for weighted scoring
- Conditional formatting for risk thresholds


**5. create_requirements_documentation_sheet(ws, styles)**

- Similar structure for Sheet 3
- Multiple sections (SRS, Functional, Non-Functional, Data Protection)
- Status formulas for each section


**... Similar functions for Sheets 4-10**

**6. Main Execution**
```python
def main():
    # Create workbook
    wb = create_workbook()
    styles = setup_styles()
    
    # Create each sheet
    create_application_profile_sheet(wb['1. Application Profile'], styles)
    create_risk_classification_sheet(wb['2. Risk Classification'], styles)
    create_requirements_documentation_sheet(wb['3. Requirements Documentation'], styles)
    create_threat_modeling_sheet(wb['4. Threat Modeling'], styles)
    create_architecture_review_sheet(wb['5. Architecture Review'], styles)
    create_traceability_sheet(wb['6. Requirements Traceability'], styles)
    create_compliance_checklist_sheet(wb['7. Compliance Checklist'], styles)
    create_gap_analysis_sheet(wb['8. Gap Analysis'], styles)
    create_evidence_register_sheet(wb['9. Evidence Register'], styles)
    create_approval_signoff_sheet(wb['10. Approval & Sign-Off'], styles)
    
    # Save workbook
    filename = f"ISMS-A826-Requirements-Template-{datetime.now().strftime('%Y%m%d')}.xlsx"
    wb.save(filename)
    print(f"✅ Workbook created: {filename}")

if __name__ == "__main__":
    main()
```

## Script Testing Checklist

Before deploying script:

- [ ] All 10 sheets created
- [ ] Column widths correct
- [ ] Headers formatted correctly (colors, fonts, alignment)
- [ ] Data validations applied (dropdowns working)
- [ ] Formulas calculate correctly (test with sample data)
- [ ] Conditional formatting applies (colors appear correctly)
- [ ] Cell protection set (formulas protected, input cells unlocked)
- [ ] File saves without errors
- [ ] File opens in Excel 2016+ without warnings
- [ ] UTF-8 encoding correct (emojis display: ✅ ⚠️ ❌)


---

# Quality Assurance Script

**Script Filename:** `excel_sanity_check_a825_26_29_1.py`

**Purpose:** Validate generated workbook matches specification

**Key Checks:**
1. Verify 10 sheets exist with correct names
2. Validate column widths match specification
3. Check headers formatted correctly
4. Verify data validations present
5. Test formulas with sample data
6. Validate conditional formatting rules
7. Check cell protection settings
8. Verify UTF-8 encoding (emoji check)
9. Test file opens without errors
10. Generate validation report

**Example Validation Function:**
```python
def validate_sheet_structure(wb):
    """Validate sheet structure matches specification"""
    expected_sheets = [
        "1. Application Profile",
        "2. Risk Classification",
        # ... etc
    ]
    
    actual_sheets = wb.sheetnames
    
    if actual_sheets != expected_sheets:
        return False, f"Sheet mismatch: expected {expected_sheets}, got {actual_sheets}"
    
    return True, "✅ All sheets present and correctly named"
```

---

# Freeze Panes Configuration

**All Sheets:**

- Freeze at Row 4 (headers visible when scrolling down)
- Freeze at Column A (question column visible when scrolling right)


**Implementation:**
```python
ws.freeze_panes = 'B4'  # Freeze rows 1-3, column A
```

---

# Print Settings

**Page Setup for All Sheets:**

- Orientation: Landscape
- Paper Size: A4
- Fit to: 1 page wide, multiple pages tall
- Margins: Normal (0.75" left/right, 1" top/bottom)
- Headers: Print titles - Rows 1-3 repeat on each page
- Footers: Page X of Y (center), Date (right), Filename (left)


**Implementation:**
```python
ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
ws.page_setup.paperSize = ws.PAPERSIZE_A4
ws.page_setup.fitToWidth = 1
ws.page_setup.fitToHeight = 0  # Auto
ws.print_title_rows = '1:3'  # Repeat rows 1-3 on each page
```

---

# Version Control & Change Tracking

**Document Version Tracking:**

- Version documented in Document Control (Sheet 1, Row 1 or dedicated metadata)
- Version history maintained separately
- Filename includes date: `ISMS-A826-Requirements-APP-XXX-YYYYMMDD-v2.0.xlsx`


**Change Log Sheet (Optional):**

- Add hidden sheet "Change Log" documenting workbook modifications
- Track: Date, Version, Changes, Modified By


---

# File Size Optimization

**Tips to keep file size manageable:**
1. Don't embed large images (link instead)
2. Remove unused styles and formats
3. Clear formatting from unused cells
4. Don't save calculated formula results (recalc on open)
5. Use references instead of copying data

**Target File Size:** <2MB (typical: 500KB-1MB)

---

# Browser Compatibility (Office 365 Online)

**If workbook will be used in Excel Online:**

- Avoid VBA macros (not supported)
- Test all formulas (some advanced formulas may not work)
- Simplify conditional formatting (complex rules may not render)
- Limit data validation complexity
- Test on Office 365 before deployment


---

# Accessibility Considerations

**For users with disabilities:**

- Use high-contrast colors (current color scheme complies)
- Provide alt text for non-text content
- Use clear, simple language in instructions
- Ensure keyboard navigation works (tab order logical)
- Test with screen readers (JAWS, NVDA)


---

# Deployment Checklist

Before deploying workbook to users:

- [ ] All sheets tested with sample data
- [ ] Formulas calculate correctly
- [ ] Data validations work (dropdowns function)
- [ ] Conditional formatting displays correctly
- [ ] Colors and fonts match specification
- [ ] File opens in Excel 2016+ without errors
- [ ] File opens in Excel Online (if required)
- [ ] Print preview looks correct
- [ ] User guide (PART I) provided to users
- [ ] Training conducted (if needed)
- [ ] Support contact information provided
- [ ] Evidence repository folder structure created
- [ ] Assessment schedule established


---

# Maintenance & Updates

**When to update workbook template:**

- Policy changes (ISMS-POL-A.8.25-26-29 updates)
- User feedback (usability improvements)
- Formula errors discovered
- New requirements added
- Compliance scoring methodology changes


**Update Process:**
1. Document requested change
2. Update specification (this PART II)
3. Update Python script
4. Test updated workbook
5. Run QA script
6. Update version number
7. Deploy to users
8. Communicate changes

**Backward Compatibility:**

- Maintain compatibility with previous versions where possible
- Provide migration script if breaking changes
- Document migration process in version history


---

# Appendix: Technical Notes for Developers

## Excel Formula Best Practices

**Use Named Ranges:**
```
Define named range: RiskScore = 'Sheet 2'!D10
Reference in formulas: =IF(RiskScore>=3.5,"High Risk","Medium Risk")
```
**Benefit:** More readable formulas, easier maintenance

**Use INDIRECT() for Dynamic References:**
```excel
=INDIRECT("Sheet 2!B"&ROW())
```
**Use case:** When cell reference needs to be calculated

**Use IFERROR() for Robust Formulas:**
```excel
=IFERROR(E7/E8*100&" %","N/A")
```
**Benefit:** Prevents #DIV/0!, #VALUE! errors

## Python openpyxl Tips

**Merging Cells:**
```python
ws.merge_cells('A1:G1')
ws['A1'] = "Header Text"  # Only set value on first cell
```

**Data Validation:**
```python
from openpyxl.worksheet.datavalidation import DataValidation

dv = DataValidation(type="list", formula1='"Option1,Option2,Option3"')
ws.add_data_validation(dv)
dv.add('B5')  # Apply to cell B5
dv.add('B6:B10')  # Apply to range
```

**Conditional Formatting:**
```python
from openpyxl.formatting.rule import Rule, CellIsRule
from openpyxl.styles import PatternFill

green_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
rule = CellIsRule(operator="containsText", formula=['"✅"'], fill=green_fill)
ws.conditional_formatting.add('E4:E20', rule)
```

**Formula References:**
```python
# Absolute reference
ws['B5'] = '=$A$1 + $A$2'

# Relative reference
ws['B5'] = '=A1 + A2'

# Mixed reference
ws['B5'] = '=$A1 + A$2'
```

## Common Pitfalls to Avoid

**Pitfall 1: Excel Date Format**

- Python datetime → Excel serial date
- Use `ws.cell().number_format = 'DD.MM.YYYY'`


**Pitfall 2: UTF-8 Encoding**

- Emojis (✅ ⚠️ ❌) require UTF-8
- Use `wb.save(filename, encoding='utf-8')` (openpyxl handles automatically)


**Pitfall 3: Formula Calculation**

- Excel doesn't auto-calculate on open by default in scripts
- Set `wb.calculation.calcMode = 'auto'`


**Pitfall 4: Large Files**

- Conditional formatting on large ranges = slow performance
- Limit CF rules to necessary ranges only


**Pitfall 5: Protected Sheets**

- Set `ws.protection.password = None` (no password for user sheets)
- Lock formula cells, unlock input cells explicitly


---

**END OF SPECIFICATION**

---

*"I remember once going to see him when he was ill at Putney. I had ridden in taxi cab number 1729 and remarked that the number seemed to me rather a dull one."*
— G.H. Hardy, about Ramanujan

*Where bamboo antennas actually work.* 🎋
