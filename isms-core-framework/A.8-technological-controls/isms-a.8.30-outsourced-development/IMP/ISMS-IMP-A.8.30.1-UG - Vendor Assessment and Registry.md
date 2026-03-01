<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.30.1-UG:framework:UG:a.8.30.1 -->
**ISMS-IMP-A.8.30.1-UG - Vendor Assessment and Registry**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.30: Outsourced Development

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Vendor Assessment and Registry |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.30.1-UG |
| **Related Policy** | ISMS-POL-A.8.30 (Outsourced Development) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.30 (Outsourced Development) |
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

- ISMS-POL-A.8.30 (Outsourced Development)
- ISMS-IMP-A.8.30.2 (Contract Compliance)
- ISMS-IMP-A.8.30.3 (Security Testing and Acceptance)

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Vendor Registry | Central registry of all outsourced development vendors |
| 3 | Security Assessment | Vendor security posture assessment and scoring |
| 4 | Due Diligence | Due diligence records and evidence for each vendor |
| 5 | Environment Security | Assessment of vendor development environment security |
| 6 | Evidence Register | Store and reference evidence supporting assessments |
| 7 | Summary Dashboard | Compliance status and key metrics overview |
| 8 | Approval Sign-Off | Management review sign-off and certification |

---

## Assessment Overview

### Purpose

The Vendor Assessment and Registry workbook serves as the central control point for managing outsourced development security. It captures vendor security posture, tracks approval status, maintains due diligence records, and provides the evidentiary foundation for demonstrating A.8.30 compliance.

ISO/IEC 27001:2022 Control A.8.30 states:

> *"The organisation should direct, monitor and review the activities related to outsourced system development."*

This control ensures that when development activities are outsourced, appropriate security requirements are established, communicated, and verified with external development partners.

### Scope and Applicability

**This workbook applies to:**

| Vendor Category | Assessment Required | Risk Tier |
|-----------------|---------------------|-----------|
| Custom software development firms | Full assessment | Critical or High |
| System integrators with development scope | Full assessment | Critical or High |
| Managed service providers with code access | Full assessment | High or Standard |
| Freelance developers (individual contractors) | Full assessment | Based on access level |
| Offshore development centers | Full assessment + enhanced due diligence | Critical |
| Platform/SaaS vendors with customisation work | Conditional assessment | Based on scope |
| Open source maintainers (commercial support) | Risk-based assessment | Based on criticality |

**This workbook does NOT apply to:**

- Pure SaaS vendors with no customisation (use Supplier Assessment A.5.21-22)
- Off-the-shelf software procurement (use standard procurement process)
- Internal development teams (covered by A.8.25-29)
- Staff augmentation where developers work under organisation's direct supervision and processes

### Business Context

**Why Vendor Assessment Matters:**

Outsourced development introduces significant security risks that must be systematically managed:

1. **Code Quality Risks**: External developers may not follow secure coding standards
2. **Access Risks**: Vendors require access to development environments, repositories, and potentially production data
3. **Intellectual Property Risks**: Code ownership and confidentiality must be protected
4. **Supply Chain Risks**: Vendor compromises can propagate to organisation systems
5. **Compliance Risks**: Regulatory requirements (GDPR, FADP) apply regardless of who writes the code
6. **Continuity Risks**: Vendor failure or termination must not impact operations

**Regulatory Context:**

| Regulation | Relevant Requirements |
|------------|----------------------|
| ISO 27001:2022 A.8.30 | Outsourced development security controls |
| Swiss FADP/nDSG | Data processor requirements, cross-border transfers |
| GDPR Article 28 | Processor obligations, sub-processor controls |
| FINMA | Third-party risk management for financial services |

### Assessment Outputs

Upon completion, this workbook provides:

| Output | Purpose | Audience |
|--------|---------|----------|
| Approved Vendor Registry | Authoritative list of approved development partners | Project Managers, Procurement |
| Risk Tier Classifications | Risk-based engagement requirements | IT Security, Project Leads |
| Due Diligence Records | Audit evidence of vendor evaluation | Internal/External Auditors |
| Assessment Recommendations | Approval/conditional/rejection decisions | Management, Procurement |
| Summary Dashboard Data | Metrics for security monitoring | CISO, Management |
| Evidence Package | ISO 27001 audit documentation | External Auditors |

---

## Prerequisites

### Required Inputs

Before beginning vendor assessment, ensure you have collected:

| Input | Source | Required For |
|-------|--------|--------------|
| Vendor legal entity information | Procurement/Contract | Sheet 1: Vendor Registry |
| Scope of work description | Project Manager | Risk tier determination |
| Vendor security questionnaire responses | Vendor | Sheet 2: Security Assessment |
| Security certifications (ISO 27001, SOC 2) | Vendor | Sheet 2, Sheet 3 |
| Development environment documentation | Vendor | Sheet 4: Environment Security |
| Reference contacts | Vendor | Sheet 3: Due Diligence |
| Previous engagement history (if applicable) | Internal records | Risk assessment |
| Data classification of systems accessed | Data Owner | Risk tier determination |

### Required Approvals Before Assessment

| Approval Type | Approver | Purpose |
|---------------|----------|---------|
| Engagement Intent | Project Sponsor | Confirms business need for outsourcing |
| Budget Approval | Finance | Confirms funds available |
| Data Sharing Approval | Data Owner | Authorises data access for vendor |
| Security Assessment Initiation | IT Security Lead | Confirms assessment resources available |

### Required Knowledge

Assessment personnel should understand:

- ISO 27001:2022 control requirements, particularly A.8.25-30
- Secure software development lifecycle (SSDLC) concepts
- Common security frameworks (OWASP, NIST CSF 2.0, CIS Controls)
- Vendor risk assessment methodologies
- Organisation's security policies and standards
- Regulatory requirements applicable to the development scope

### Tool Requirements

| Tool | Purpose | Access Required |
|------|---------|-----------------|
| Excel or equivalent spreadsheet | Workbook completion | Standard user |
| Document management system | Evidence storage | Write access to vendor folders |
| Security questionnaire platform | Questionnaire distribution | Admin or assessor role |
| Certificate validation services | Certification verification | Web access |
| Video conferencing | Vendor interviews | Standard access |

---

## Completion Walkthrough

### Sheet 1: Vendor Registry – Completion Guide

**Purpose**: Maintain the authoritative list of development vendors with their approval status, risk tier, and assessment dates.

**Step-by-Step Completion:**

**Step 1: Generate Vendor ID**

Create a unique identifier using the format `VND-XXXX`:

| Component | Format | Example |
|-----------|--------|---------|
| Prefix | VND- | VND- |
| Sequential Number | 4 digits, zero-padded | 0042 |
| Full ID | VND-XXXX | VND-0042 |

**Step 2: Enter Vendor Legal Name**

- Use the exact legal entity name from contract documents
- Include legal suffix (AG, GmbH, Ltd, Inc., etc.)
- Do NOT use trading names or abbreviations

| Correct | Incorrect |
|---------|-----------|
| Acme Software Development AG | Acme Software |
| TechPartners GmbH | Tech Partners |
| CodeCraft Solutions Ltd. | CodeCraft |

**Step 3: Set Initial Registry Status**

For new vendors, always set initial status to "Pending":

| Status | When Used | Next Action |
|--------|-----------|-------------|
| Pending | New vendor, assessment not complete | Complete assessment |
| Approved | Assessment passed, approval granted | Schedule annual review |
| Suspended | Issues identified, access revoked | Remediation required |
| Removed | Relationship terminated | Archive records |

**Step 4: Assign Risk Tier**

Determine risk tier based on data access and system criticality:

| Risk Tier | Criteria | Assessment Depth | Review Frequency |
|-----------|----------|------------------|------------------|
| Critical | Access to production systems, personal data, or financial data | Full assessment + enhanced due diligence | Quarterly |
| High | Access to development environments, non-production data | Full assessment | Semi-annual |
| Standard | Limited access, isolated development | Standard assessment | Annual |

**Risk Tier Decision Matrix:**

| Data/System Access | Production Systems | Non-Production | Isolated Environment |
|--------------------|-------------------|----------------|---------------------|
| Personal Data (PII) | Critical | High | High |
| Financial Data | Critical | High | High |
| Business Critical | Critical | High | Standard |
| Internal Only | High | Standard | Standard |
| Public Data | High | Standard | Standard |

**Step 5: Record Assessment Dates**

Enter dates in Swiss format (DD.MM.YYYY):

| Field | Description | Example |
|-------|-------------|---------|
| Initial_Assessment_Date | Date of first approved assessment | 15.01.2026 |
| Last_Assessment_Date | Most recent assessment completion | 15.01.2026 |
| Next_Assessment_Due | Calculated based on risk tier | 15.01.2027 |

**Step 6: Document Certifications**

Record vendor security certifications:

| Certification | Values | Evidence Required |
|---------------|--------|-------------------|
| ISO_27001_Certified | Yes, No, In Progress | Current certificate, scope document |
| SOC2_Type2 | Yes, No, N/A | Current SOC 2 Type II report |

**Certification Validation:**
- Verify certificate authenticity via certification body website
- Confirm certificate is current (not expired)
- Ensure scope covers relevant services
- Document expiration dates for renewal tracking

**Step 7: Enter Contact and Approval Information**

| Field | Guidance |
|-------|----------|
| Primary_Contact | Vendor's designated security contact email |
| Approved_Project_Types | Select all applicable: Critical, High, Standard |
| Approved_By | Full name and role of approver |
| Notes | Any restrictions, conditions, or special considerations |

### Sheet 2: Security Assessment – Completion Guide

**Purpose**: Document detailed security assessment findings for each vendor evaluation.

**Step-by-Step Completion:**

**Step 1: Generate Assessment ID**

Create unique identifier using format `ASM-XXXX`:

| Component | Format | Example |
|-----------|--------|---------|
| Prefix | ASM- | ASM- |
| Sequential Number | 4 digits | 0156 |
| Full ID | ASM-XXXX | ASM-0156 |

**Step 2: Link to Vendor Registry**

Enter the Vendor_ID from Sheet 1. Ensure the ID exists in the registry before proceeding.

**Step 3: Select Assessment Type**

| Type | When Used | Scope |
|------|-----------|-------|
| Initial | First-time vendor assessment | Full assessment |
| Annual | Scheduled reassessment | Full assessment |
| Triggered | Event-based reassessment | Focused on trigger area |

**Triggered Assessment Triggers:**
- Security incident involving vendor
- Major contract scope change
- Vendor acquisition or merger
- Certification lapse
- New regulatory requirements
- Negative security news about vendor

**Step 4: Evaluate Security Certification Status**

| Field | Assessment Guidance |
|-------|---------------------|
| Security_Certification | Current certification status |
| Cert_Expiry_Date | When certification expires |

**Certification Assessment:**

| Certification | Verification Method | Weight in Assessment |
|---------------|---------------------|---------------------|
| ISO 27001 | Certification body registry lookup | High |
| SOC 2 Type II | Review actual report | High |
| SOC 2 Type I | Review report (limited assurance) | Medium |
| Self-attested | Questionnaire review only | Low |
| None | No third-party verification | Risk factor |

**Step 5: Assess SDLC Maturity**

Evaluate the vendor's secure development lifecycle:

| Maturity Level | Characteristics | Evidence |
|----------------|-----------------|----------|
| Mature | Documented SSDLC, integrated security testing, trained developers | SSDLC documentation, training records |
| Developing | SSDLC in progress, some security testing | Improvement roadmap, partial implementation |
| Basic | Ad-hoc security practices, minimal documentation | Limited formal processes |
| Unknown | Insufficient information provided | Requires additional investigation |

**Assessment Questions:**
- Does vendor have documented secure coding standards?
- Is security training mandatory for developers?
- Are threat modelling/security reviews performed?
- Is security integrated into CI/CD pipelines?
- How are security findings tracked and remediated?

**Step 6: Review Security Incident History**

| Rating | Definition |
|--------|------------|
| None | No known security incidents in past 24 months |
| Minor | Incidents with no customer data impact |
| Major | Incidents involving data breach, prolonged outage, or regulatory notification |

**Investigation Sources:**
- Direct vendor disclosure (required in questionnaire)
- Public breach databases
- News/media searches
- Regulatory disclosure databases

**Step 7: Evaluate Security Tooling**

Document tools used by vendor for security testing:

| Tool Category | Examples | Minimum Expectation |
|---------------|----------|---------------------|
| SAST | SonarQube, Checkmarx, Fortify, Snyk Code | Required for Critical/High |
| DAST | OWASP ZAP, Burp Suite, Acunetix | Required for Critical/High |
| SCA | Snyk, WhiteSource, Dependabot | Required for all tiers |
| Secret Scanning | GitLeaks, TruffleHog, GitHub Secret Scanning | Required for all tiers |

**Step 8: Assess Personnel Security**

| Rating | Definition | Verification |
|--------|------------|--------------|
| Verified | Background checks conducted, evidence provided | Attestation + sample records |
| Attested | Vendor attests to background check policy | Signed attestation |
| Unknown | No information on personnel screening | Risk factor |

**Step 9: Evaluate Development Environment**

| Rating | Definition |
|--------|------------|
| Compliant | Meets all security requirements |
| Partial | Meets most requirements with documented exceptions |
| Non-Compliant | Significant security gaps identified |

**Step 10: Calculate Overall Risk Rating**

| Rating | Criteria |
|--------|----------|
| Low | Certified, mature SDLC, no incidents, compliant environment |
| Medium | Certified or mature SDLC, minor gaps, acceptable remediation |
| High | Some certifications, developing SDLC, gaps requiring attention |
| Critical | No certification, basic SDLC, significant gaps, or major incidents |

**Step 11: Document Recommendation**

| Recommendation | When Appropriate | Required Actions |
|----------------|------------------|------------------|
| Approve | Low/Medium risk, all critical requirements met | Add to registry |
| Conditional | Acceptable risk with specific conditions | Document conditions, set review date |
| Reject | High/Critical risk, critical requirements not met | Document rationale, suggest alternatives |

### Sheet 3: Due Diligence Checklist – Completion Guide

**Purpose**: Track completion of all due diligence verification items with evidence references.

**Step-by-Step Completion:**

**Step 1: Link to Vendor**

Enter the Vendor_ID from Sheet 1.

**Step 2: Complete Each Due Diligence Category**

Work through each of the 10 standard categories:

**Category 1: Security Certification Verification**

| Check Item | Verification Method | Evidence Type |
|------------|---------------------|---------------|
| ISO 27001 certificate authenticity | Certification body registry | Certificate copy |
| Certificate scope covers services | Review certificate scope statement | Scope document |
| Certificate current (not expired) | Check validity dates | Certificate copy |
| SOC 2 Type II report validity | Review report date | SOC 2 report |
| SOC 2 scope covers development | Review service description | SOC 2 report section |

**Category 2: Secure Development Practices**

| Check Item | Verification Method | Evidence Type |
|------------|---------------------|---------------|
| Documented SSDLC process | Request documentation | SSDLC document |
| Secure coding standards | Request standards | Coding standards |
| Code review process | Interview/documentation | Process document |
| Security testing integration | Review CI/CD configuration | Pipeline documentation |
| Security training program | Request training records | Training records sample |

**Category 3: Security Incident History**

| Check Item | Verification Method | Evidence Type |
|------------|---------------------|---------------|
| Vendor incident disclosure | Questionnaire response | Signed questionnaire |
| Public breach database search | HaveIBeenPwned, breach databases | Search results |
| Regulatory action search | Regulatory body websites | Search results |
| News/media search | Google News search | Search results |

**Category 4: Technical Security Capabilities**

| Check Item | Verification Method | Evidence Type |
|------------|---------------------|---------------|
| SAST tools implemented | Demo/configuration review | Tool configuration |
| DAST capabilities | Demo/test results | Scan reports |
| Vulnerability management | Process documentation | Policy/process docs |
| Penetration testing practice | Test reports (sanitised) | Summary report |

**Category 5: Personnel Security**

| Check Item | Verification Method | Evidence Type |
|------------|---------------------|---------------|
| Background check policy | Request policy | Policy document |
| Check verification | Attestation of compliance | Signed attestation |
| Security clearance (if required) | Clearance documentation | Clearance letter |
| Security awareness training | Training records | Completion records |

**Category 6: Physical Security (If On-Site Development)**

| Check Item | Verification Method | Evidence Type |
|------------|---------------------|---------------|
| Physical access controls | Site assessment/attestation | Attestation/photos |
| Visitor management | Policy review | Policy document |
| Secure development areas | Site assessment | Assessment report |
| Clean desk policy | Policy review | Policy document |

**Category 7: Subcontractor Management**

| Check Item | Verification Method | Evidence Type |
|------------|---------------------|---------------|
| Subcontractor disclosure | Questionnaire response | Questionnaire |
| Subcontractor assessment process | Policy documentation | Policy document |
| Flow-down of security requirements | Contract review | Contract clauses |
| Right to audit subcontractors | Contract review | Contract clause |

**Category 8: Business Continuity**

| Check Item | Verification Method | Evidence Type |
|------------|---------------------|---------------|
| BCP documentation | Request plan summary | BCP summary |
| DR capabilities | Documentation review | DR plan summary |
| Backup procedures | Documentation | Backup policy |
| Recovery testing | Test records | Test results summary |

**Category 9: Insurance Coverage**

| Check Item | Verification Method | Evidence Type |
|------------|---------------------|---------------|
| Cyber liability insurance | Insurance certificate | Certificate |
| Professional indemnity | Insurance certificate | Certificate |
| Coverage adequacy | Review limits | Certificate review |

**Category 10: Reference Checks**

| Check Item | Verification Method | Evidence Type |
|------------|---------------------|---------------|
| Reference contacts provided | Vendor submission | Contact list |
| Reference interviews conducted | Phone/video calls | Interview notes |
| Reference feedback documented | Written summary | Summary document |

**Step 3: Document Evidence References**

For each completed check, record:
- Evidence type (Certificate, Attestation, Document, Interview)
- Evidence reference (file path or document ID)
- Verifier name and date

### Sheet 4: Environment Security Assessment – Completion Guide

**Purpose**: Evaluate the security of the vendor's development environment, particularly when they will have access to organisation systems or data.

**Step-by-Step Completion:**

**Step 1: Link to Vendor and Date Assessment**

Enter Vendor_ID and current date.

**Step 2: Assess Multi-Factor Authentication**

| Rating | Definition | Evidence |
|--------|------------|----------|
| Yes | MFA enforced for all development access | Policy + technical configuration |
| Partial | MFA for some access, gaps identified | Documentation of coverage |
| No | MFA not implemented or not enforced | Requires remediation |

**Step 3: Evaluate Network Isolation**

| Rating | Definition | Risk Level |
|--------|------------|------------|
| Isolated | Separate network for development, no production connectivity | Low |
| Segmented | Network segments with controlled access | Medium |
| Shared | Development on same network as other operations | High |

**Step 4: Assess Endpoint Security**

| Rating | Definition | Verification |
|--------|------------|--------------|
| Compliant | EDR, encryption, patch management enforced | Configuration evidence |
| Partial | Some controls in place, gaps identified | Gap documentation |
| Non-Compliant | Significant endpoint security gaps | Remediation required |

**Step 5: Evaluate Code Repository Security**

| Rating | Definition | Requirements |
|--------|------------|--------------|
| Secure | Access controls, audit logging, secret scanning | All controls verified |
| Partial | Some controls, gaps identified | Document gaps |
| Unsecure | Significant security gaps | Remediation required |

**Step 6: Verify Secret Scanning**

| Rating | Definition |
|--------|------------|
| Yes | Automated secret scanning in place and active |
| No | No secret scanning implemented |

**Step 7: Check Branch Protection**

| Rating | Definition |
|--------|------------|
| Yes | Branch protection rules configured on main branches |
| Partial | Some protection, not comprehensive |
| No | No branch protection |

**Step 8: Assess Data Handling Practices**

| Rating | Definition | Risk Level |
|--------|------------|------------|
| No Prod Data | No production data in development | Low |
| Masked | Production data used but properly masked/anonymised | Medium |
| Raw (Non-Compliant) | Unmasked production data in development | Critical - Reject |

**Step 9: Document Attestation**

| Field | Guidance |
|-------|----------|
| Attestation_Received | Whether vendor has signed security attestation |
| Attestation_Date | Date attestation was signed |

**Step 10: Determine Compliance Status**

| Status | Criteria |
|--------|----------|
| Compliant | All requirements met |
| Conditional | Minor gaps with documented remediation plan |
| Non-Compliant | Significant gaps requiring remediation before engagement |

---

## Evidence Collection

### Evidence Requirements

Evidence must be collected and stored for all assessment activities:

| Evidence Category | Retention Period | Storage Location |
|-------------------|------------------|------------------|
| Assessment records | 7 years | ISMS Evidence Library: Vendor Assessments |
| Certifications | Duration of validity + 1 year | Vendor folder |
| Due diligence documents | 7 years | Vendor folder |
| Attestations | Duration of engagement + 3 years | Vendor folder |
| Interview notes | 3 years | Assessment folder |
| Approval records | 7 years | Approval folder |

### Evidence Folder Structure

```
ISMS-Evidence-Library/
└── Vendor-Assessments/
    └── A.8.30-Outsourced-Development/
        └── [Vendor_ID]-[Vendor_Name]/
            ├── Assessments/
            │   ├── [ASM-XXXX]-[Date]-Initial/
            │   │   ├── Questionnaire-Response.pdf
            │   │   ├── Assessment-Workbook.xlsx
            │   │   └── Recommendation-Memo.pdf
            │   └── [ASM-XXXX]-[Date]-Annual/
            ├── Certifications/
            │   ├── ISO27001-Certificate-[Expiry].pdf
            │   └── SOC2-TypeII-Report-[Date].pdf
            ├── Attestations/
            │   └── Security-Attestation-[Date].pdf
            ├── Due-Diligence/
            │   ├── Reference-Check-Notes.pdf
            │   └── Background-Check-Attestation.pdf
            └── Contracts/
                └── Security-Schedule-[Date].pdf
```

### Evidence Quality Requirements

All evidence must be:

| Quality Attribute | Requirement |
|-------------------|-------------|
| Authentic | From verified sources |
| Complete | Covers all required areas |
| Current | Within validity period |
| Legible | Readable format |
| Attributable | Author/source identified |
| Dated | Clear date of creation |

### Evidence for Audit

During ISO 27001 audit, be prepared to demonstrate:

| Auditor Request | Evidence to Provide |
|-----------------|---------------------|
| "Show me your approved vendor list" | Sheet 1: Vendor Registry export |
| "How do you assess new vendors?" | Assessment procedure + sample assessment |
| "What due diligence do you perform?" | Sheet 3 + supporting evidence |
| "How do you verify certifications?" | Certification validation process |
| "Show me a sample vendor file" | Complete vendor evidence folder |
| "How often do you reassess vendors?" | Registry showing reassessment dates |
| "What happens if a vendor fails assessment?" | Rejection records, remediation tracking |

---

## Common Pitfalls

### Assessment Errors

❌ **MISTAKE: Accepting vendor self-attestation without verification**
Vendors claiming ISO 27001 certification must provide certificate copy with verification via certification body registry.

❌ **MISTAKE: Not verifying certification scope covers relevant services**
A vendor may be ISO 27001 certified for one business unit but not for the development services you're engaging. Always verify scope.

❌ **MISTAKE: Using outdated assessment for new engagement**
Each engagement requires current assessment. Assessments older than 12 months require refresh.

❌ **MISTAKE: Accepting SOC 2 Type I as equivalent to Type II**
Type I is point-in-time; Type II covers operational effectiveness over a period. Type II provides significantly more assurance.

❌ **MISTAKE: Not documenting conditional approval conditions**
When approving with conditions, failing to document specific conditions and review dates leads to gaps in follow-up.

### Registry Management Errors

❌ **MISTAKE: Not updating registry when vendor status changes**
Vendor certifications expiring, acquisitions, or incidents must trigger immediate registry review.

❌ **MISTAKE: Allowing engagement before assessment completes**
"Pending" status vendors must not begin work until assessment completes and approval is granted.

❌ **MISTAKE: Not tracking reassessment due dates**
Critical and High tier vendors require more frequent reassessment. Missing these dates creates compliance gaps.

### Due Diligence Errors

❌ **MISTAKE: Skipping reference checks for "known" vendors**
Prior experience doesn't replace current reference checks. Vendor quality can change over time.

❌ **MISTAKE: Not verifying personnel assigned to your project**
Assessment covers vendor organisation, but specific personnel should meet security requirements, especially for elevated access.

❌ **MISTAKE: Not checking for subcontractor usage**
Vendors using subcontractors extend your supply chain risk. Must be disclosed and assessed.

### Environment Assessment Errors

❌ **MISTAKE: Accepting "yes" responses without evidence**
Environment security responses must be verified through configuration evidence or attestation, not just questionnaire answers.

❌ **MISTAKE: Not assessing data handling for production data scenarios**
If vendor will access production data for testing/support, data handling practices become critical.

---

## Quality Checklist

### Pre-Submission Checklist

Before submitting assessment for approval, verify:

**Sheet 1: Vendor Registry**
- [ ] Vendor_ID follows VND-XXXX format
- [ ] Legal entity name matches contract exactly
- [ ] Risk tier assignment documented with rationale
- [ ] All date fields in DD.MM.YYYY format
- [ ] Certification status verified (not just attested)
- [ ] Appropriate approver identified for risk tier

**Sheet 2: Security Assessment**
- [ ] Assessment_ID follows ASM-XXXX format
- [ ] Valid Vendor_ID reference
- [ ] All assessment fields completed
- [ ] Certification expiry dates recorded
- [ ] SDLC maturity rating justified
- [ ] Incident history search documented
- [ ] Overall risk rating consistent with findings
- [ ] Recommendation aligned with risk rating
- [ ] Conditions documented (if conditional)
- [ ] Evidence location valid and accessible

**Sheet 3: Due Diligence Checklist**
- [ ] All 10 categories addressed
- [ ] N/A items justified
- [ ] Evidence references valid
- [ ] Verification dates recorded
- [ ] Verifier names documented

**Sheet 4: Environment Security**
- [ ] All environment fields completed
- [ ] Non-compliant items have remediation notes
- [ ] Attestation received (if required)
- [ ] Compliance status justified

### Evidence Completeness Check

- [ ] All referenced evidence files exist in repository
- [ ] Evidence is current (within validity periods)
- [ ] Sensitive evidence appropriately classified
- [ ] Evidence naming follows convention
- [ ] Evidence organised in proper folder structure

### Approval Readiness Check

- [ ] Assessment workbook complete
- [ ] All critical fields populated
- [ ] Evidence package complete
- [ ] Recommendation memo prepared
- [ ] Appropriate approver identified
- [ ] No blocking issues unresolved

---

## Review and Approval

### Approval Authority Matrix

| Vendor Risk Tier | Approval Authority | Escalation |
|------------------|-------------------|------------|
| Critical | CISO + Executive Management | Board Risk Committee |
| High | CISO | Executive Management |
| Standard | IT Security Manager | CISO |

### Approval Workflow

```
Assessor Completes Assessment
         ↓
Assessment Peer Review (IT Security Team)
         ↓
Evidence Package Verification
         ↓
Recommendation Memo Prepared
         ↓
Submit to Approval Authority
         ↓
[Approval Authority Review]
         ↓
    ├── Approved → Update Registry, Notify Procurement
    ├── Conditional → Document Conditions, Set Review Date
    └── Rejected → Document Rationale, Notify Requestor
```

### Review Timeline

| Risk Tier | Assessment SLA | Approval SLA | Total SLA |
|-----------|---------------|--------------|-----------|
| Critical | 15 business days | 5 business days | 20 business days |
| High | 10 business days | 3 business days | 13 business days |
| Standard | 7 business days | 2 business days | 9 business days |

### Post-Approval Actions

| Action | Responsibility | Timeline |
|--------|----------------|----------|
| Update Vendor Registry | IT Security | Same day as approval |
| Notify Procurement | IT Security | Same day |
| Configure system access (if approved) | IT Operations | Per access request SLA |
| Schedule reassessment | IT Security | Immediately |
| Archive evidence | IT Security | Within 5 days |

---

**END OF USER GUIDE**

---

*"You cannot outsource accountability."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
