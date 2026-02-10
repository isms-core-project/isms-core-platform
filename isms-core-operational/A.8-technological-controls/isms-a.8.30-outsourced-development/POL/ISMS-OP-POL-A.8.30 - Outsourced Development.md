<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.30:operational:OP-POL:a.8.30 -->
**ISMS-OP-POL-A.8.30 — Outsourced Development**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Outsourced Development |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.30 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.8.30 — Outsourced development
- ISO/IEC 27002:2022 Section 8.30 — Implementation guidance for outsourced development
- NIST SP 800-53 Rev 5 — SA-4 (Acquisition Process), SA-9 (External System Services)
- OWASP Secure Software Contract Annex
- OWASP Top 10:2025 — A03 Software Supply Chain Failures
- CIS Controls v8 — Safeguard 16.4 (Third-Party Software Component Inventory)

**Related Annex A Controls**:

| Control | Relationship to Outsourced Development |
|---------|----------------------------------------|
| A.5.19–23 Supplier and cloud service security | Supplier assessment framework; cloud-hosted development platforms |
| A.5.31 Legal, statutory, regulatory, and contractual requirements | Regulatory obligations in outsourcing contracts |
| A.5.34 Privacy and protection of PII | Data protection requirements for vendor access to personal data |
| A.8.4 Access to source code | Vendor access to organisational repositories |
| A.8.25–26–29 Secure development lifecycle | Secure coding, testing, and SDLC requirements applied to outsourced work |
| A.8.28 Secure coding | Coding standards extended to third-party developers |
| A.8.31 Separation of environments | Environment segregation for outsourced development |
| A.8.32 Change management | Change control for outsourced code promotion |

**Related Internal Policies**:

- Secure Development Lifecycle Policy
- Supplier and Cloud Services Security Policy
- Access to Source Code Policy
- Change Management Policy
- Information Classification and Handling Policy
- Privacy and PII Protection Policy

---

# Outsourced Development Policy

## Purpose

The purpose of this policy is to ensure that the organisation directs, monitors, and reviews all activities related to outsourced system and software development so that externally developed code meets the organisation's information security requirements before acceptance and deployment.

This policy supports Swiss nFADP (revDSG) Art. 9 by establishing contractual requirements for data processors involved in software development, ensuring that outsourced development activities handle personal data only in the manner the organisation itself is permitted to process it. Art. 8 requirements for technical and organisational measures apply equally to outsourced components. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 28 (processor obligations) and Art. 32 (security of processing) requirements also apply.

## Scope

All system and software development activities performed by external parties on behalf of the organisation, including:

- Bespoke software development by contracted development firms.
- Offshore and nearshore development teams.
- Individual freelance developers and contractors.
- Development partnerships and co-development arrangements.
- Customisation and extension of acquired software by third parties.
- Third-party maintenance and enhancement of existing organisational systems.

All employees responsible for procuring, managing, or accepting outsourced development work.

**Out of scope**: Commercial off-the-shelf (COTS) software purchased without customisation (covered under A.5.19–23); internal development activities (covered under A.8.25-26-29); cloud platform services where no custom code is developed; open-source software used as dependencies (covered under SCA requirements in the Secure Development Lifecycle Policy).

## Principle

The organisation retains accountability for the security of outsourced code regardless of where or by whom it is developed. Outsourced development shall be subject to security requirements, contractual controls, and verification activities that are equivalent to — or stricter than — those applied to internal development.

No outsourced code shall be deployed to production without the organisation's independent security validation and formal acceptance.

---

## Vendor Security Assessment

Before engaging an external development partner, the organisation shall conduct a security assessment to confirm the vendor's ability to meet information security requirements.

**Pre-Engagement Assessment Criteria**:

| Assessment Area | Minimum Requirements |
|-----------------|----------------------|
| **Security certifications** | Evidence of ISO 27001 certification, SOC 2 Type II report, or equivalent; or completion of the organisation's vendor security questionnaire |
| **Secure development practices** | Documented SDLC with security activities; use of SAST, SCA, and code review processes |
| **Personnel security** | Background checks for developers accessing organisational data; NDA signed by all individuals with access |
| **Data protection** | Data processing agreement (DPA) compliant with Swiss nFADP Art. 9; data residency and transfer assessment completed |
| **Incident response** | Documented security incident response capability; ability to notify the organisation within 24 hours of a security event |
| **Business continuity** | Evidence of business continuity planning; source code escrow or equivalent continuity arrangement where appropriate |
| **References** | Verifiable references from comparable engagements |

**Assessment Tiers**:

| Vendor Tier | Criteria | Assessment Depth |
|-------------|----------|------------------|
| **Tier 1 — High-Risk** | Vendor develops High-Risk applications; accesses production data or PII; develops internet-facing systems | Full security assessment + on-site or remote audit + annual reassessment |
| **Tier 2 — Medium-Risk** | Vendor develops internal tools; limited data access; no direct production access | Security questionnaire + evidence review + biennial reassessment |
| **Tier 3 — Low-Risk** | Vendor develops non-critical utilities; no access to sensitive data | Security questionnaire + self-attestation + reassessment at contract renewal |

**Vendor Tier Determination**:

Vendors shall be classified based on the highest risk factor present:

**Tier 1 triggers** (any one qualifies):
- Develops applications processing Confidential or Restricted data
- Direct access to production environments or databases
- Develops internet-facing systems with user authentication
- Processes personal data of >1,000 individuals
- Customises payment processing or financial systems
- Access to source code repositories containing proprietary algorithms

**Tier 2 triggers** (none of Tier 1, any of these):
- Develops internal-only applications
- Read-only access to non-production data
- Processes personal data of <1,000 individuals
- Integration work with third-party APIs
- Reporting and analytics tool development

**Tier 3** (default):
- Utility development (scripts, CLI tools, non-critical automation)
- Static website development with no user data collection
- Documentation and UI/UX design (no code access)
- Prototype/proof-of-concept work with synthetic data only

Tier determination shall be documented in the vendor security assessment record and reviewed upon scope changes.

Assessment results shall be documented and retained for the duration of the vendor relationship plus 3 years.

Vendors that fail the security assessment shall not be engaged until identified deficiencies are remediated and verified.

### Vendor Security Red Flags

During vendor assessment, the following are disqualifying findings unless remediated:

| Red Flag | Risk | Remediation Required |
|----------|------|----------------------|
| **No formal SDLC** | Unstructured development; inconsistent security practices | Document SDLC with security gates; demonstrate 3+ months consistent application |
| **No SAST/SCA tooling** | Vulnerabilities not detected before delivery | Implement automated security scanning; demonstrate ≥3 scans with remediation |
| **Vendor refuses audit rights clause** | Inability to verify security claims | Accept audit rights or provide SOC 2 Type II / ISO 27001 certification |
| **Outsources to undisclosed subcontractors** | Unknown security posture in supply chain | Full transparency on subcontractors; flow-down security requirements; assessment of each |
| **No incident response capability** | Unable to detect or respond to compromise | Document IR plan; provide 24hr notification commitment; demonstrate IR testing |
| **Previous significant breach (unresolved)** | Pattern of poor security | Demonstrate post-incident improvements; third-party validation of remediation |
| **Lack of background checks** | Insider threat risk | Implement background checks for personnel with data access |
| **Uses personal email for work** | No separation of corporate/personal data | Provide corporate email; document acceptable use policy |

**During engagement, these are escalation triggers**:
- Vendor provides false information in security assessment
- Unauthorised data exfiltration detected
- Vendor refuses vulnerability remediation
- Security testing results withheld or falsified

---

## Contractual Security Requirements

All outsourced development agreements shall include security requirements as contractual obligations.

**Mandatory Contract Clauses**:

| Clause | Requirement |
|--------|-------------|
| **Secure development standards** | Vendor shall comply with the organisation's secure coding standards and the Secure Development Lifecycle Policy, or demonstrate equivalent standards approved by the CISO |
| **Security testing** | Vendor shall perform SAST and SCA on all deliverables; DAST for web applications and APIs; results shall be shared with the organisation before acceptance |
| **Vulnerability remediation** | Critical vulnerabilities: 7 days; High: 30 days; Medium: 90 days; Low: 180 days — aligned with the organisation's remediation SLAs |
| **Security incident notification** | Vendor shall notify the organisation within 24 hours of discovering a security incident affecting the engagement, including suspected data breaches, code compromise, or unauthorised access |
| **Audit rights** | The organisation reserves the right to audit vendor security practices, development environments, and processes upon 30 calendar days' written notice |
| **Code review rights** | The organisation shall have the right to review, test, and inspect all source code, build scripts, and configuration files delivered under the agreement |
| **Subcontracting** | Vendor shall not subcontract development work without the organisation's prior written approval; subcontractors shall meet equivalent security requirements |
| **Data protection** | Data processing agreement per Swiss nFADP Art. 9; personal data processed only as instructed by the organisation; cross-border transfers subject to transfer assessment |
| **Confidentiality** | NDA covering all proprietary information, source code, system architecture, and data accessed during the engagement |
| **Termination provisions** | Secure return or destruction of all organisational data, source code, credentials, and access upon contract termination; verification within 30 days |

**Recommended Contract Clauses** (based on engagement risk):

| Clause | Applicability |
|--------|---------------|
| **Penetration testing** | Required for Tier 1 vendors; the organisation or a qualified third party shall conduct penetration testing before production acceptance |
| **Background checks** | Required for Tier 1 vendor personnel accessing PII, financial data, or production environments |
| **Security training** | Vendor personnel shall complete the organisation's security awareness briefing or demonstrate equivalent training |
| **Liability and indemnification** | Vendor liability for security breaches caused by non-compliance with contractual security requirements |
| **Insurance** | Professional indemnity and cyber liability insurance appropriate to engagement value and risk |

**Subcontractor Approval Process**:

When a vendor requests subcontracting approval:
1. **Notification**: Vendor submits written request ≥30 days before subcontractor engagement, including:
   - Subcontractor name and location
   - Scope of work to be subcontracted
   - Data access required by subcontractor
   - Subcontractor security assessment results
   - Flow-down of contractual security requirements confirmation

2. **Assessment**: Organisation reviews subcontractor against same security criteria as primary vendor (tier-appropriate assessment)

3. **Approval**:
   - Tier 1 vendors: CISO approval required
   - Tier 2/3 vendors: Development Manager approval with CISO notification

4. **Documentation**: Approved subcontractors added to vendor security assessment record; same monitoring and access management requirements apply

Unapproved subcontracting is a material breach and grounds for contract termination.

---

## Secure Development Requirements for Vendors

The organisation's secure development standards shall be communicated to vendors at the start of every engagement.

**Vendor Development Standards Package**:

The organisation shall provide each vendor with:

- Secure coding standards applicable to the technology stack in use.
- Security requirements specification for the project.
- Threat model (where one exists for the application).
- Approved cryptographic standards and libraries.
- Logging and error handling requirements.
- API security standards (where applicable).
- Input validation and output encoding requirements.

**Vendor Development Environment Requirements**:

| Requirement | Detail |
|-------------|--------|
| **Environment segregation** | Development, test, and production environments shall be separated; vendor development environments shall not have direct access to the organisation's production systems |
| **Access control** | Vendor access to organisational repositories and systems shall follow the principle of least privilege; access shall be time-bound and tied to contract duration |
| **Credential management** | No hardcoded credentials in source code; secrets managed via approved secrets management tools |
| **Version control** | All code shall be maintained in an approved version control system with full commit history and attribution |
| **Dependency management** | Vendors shall maintain a Software Bill of Materials (SBOM) for all deliverables; third-party dependencies shall be sourced from approved registries and scanned for known vulnerabilities |

**Supply Chain Security**:

Vendors shall implement controls to mitigate software supply chain risks in accordance with OWASP Top 10:2025 A03 (Software Supply Chain Failures):

- All third-party dependencies shall be inventoried and tracked in an SBOM (CycloneDX or SPDX format).
- Dependencies shall be pinned to specific versions and sourced from trusted registries.
- Transitive dependencies shall be included in vulnerability scanning.
- Vendors shall monitor dependencies against vulnerability databases (NVD, OSV, GitHub Advisory Database) and remediate identified vulnerabilities within the agreed SLAs.
- Use of unmaintained or end-of-life components shall require documented risk acceptance from the organisation.

**SBOM Requirements Detail**:
- **Format**: CycloneDX 1.4+ (preferred) or SPDX 2.3+
- **Depth**: Include transitive dependencies (not just direct dependencies)
- **Contents**: Component name, version, licence, supplier, cryptographic hash
- **Delivery**: SBOM provided with each release and updated for any dependency changes
- **Tool**: Generated via automated SBOM tool (CycloneDX CLI, Syft, SPDX tools, or equivalent) — not manually created spreadsheets
- **Validation**: Organisation verifies SBOM completeness using SCA tool before acceptance

## Typical Vendor Development Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ ENGAGEMENT PHASE                                                 │
├─────────────────────────────────────────────────────────────────┤
│ 1. Vendor Security Assessment (CISO) ──────────────────────────┐│
│ 2. Contract with Security Clauses (Legal + CISO) ─────────────┐││
│ 3. DPA Execution (DPO) ────────────────────────────────────────┘││
│ 4. Secure Development Package Delivery (Dev Manager) ──────────┘│
│ 5. Vendor Access Provisioning (IT Ops) ─────────────────────────│
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ DEVELOPMENT PHASE (iterative)                                    │
├─────────────────────────────────────────────────────────────────┤
│ 6. Vendor Development + Security Testing (Vendor) ──────────────│
│    - SAST/SCA per build                                          │
│    - Security test results shared with Org                       │
│ 7. Milestone Delivery (Vendor → Dev Manager) ───────────────────│
│ 8. Organisation Code Review (Security Team) ────────────────────│
│ 9. Vulnerability Remediation (Vendor) ──────────────────────────│
│    ↺ Repeat until acceptance criteria met                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ ACCEPTANCE PHASE                                                 │
├─────────────────────────────────────────────────────────────────┤
│ 10. Independent Security Testing (Org / Third Party) ───────────│
│     - SAST/SCA/DAST                                              │
│     - Penetration testing (Tier 1)                              │
│ 11. SBOM Delivery and Review (Dev Manager) ─────────────────────│
│ 12. Acceptance Checklist Completion (Dev Manager) ──────────────│
│ 13. Sign-Off (Risk-based: CISO/Dev Manager/App Owner) ─────────│
│ 14. Code Escrow Deposit (if applicable) ────────────────────────│
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ POST-DEPLOYMENT PHASE                                            │
├─────────────────────────────────────────────────────────────────┤
│ 15. Vendor Access Deprovisioning (IT Ops) ──────────────────────│
│ 16. Data Return/Destruction Verification (DPO) ─────────────────│
│ 17. Ongoing Support Contract (if applicable) ───────────────────│
│ 18. Annual Security Reassessment (Tier 1) ──────────────────────│
└─────────────────────────────────────────────────────────────────┘
```

---

## Code Review and Security Testing

All outsourced code shall undergo independent security validation by the organisation before acceptance.

**Vendor-Side Testing** (performed by vendor, results provided to organisation):

| Test Type | Requirement | Timing |
|-----------|-------------|--------|
| **SAST** | Scan all source code for security vulnerabilities using [SAST Tool] (examples: SonarQube, Semgrep, Checkmarx, Veracode, or CISO-approved equivalent) | Per build or at minimum weekly during active development |
| **SCA** | Scan all dependencies for known vulnerabilities and licence compliance | Per build or at minimum weekly during active development |
| **Unit/integration tests** | Demonstrate security control effectiveness (authentication, authorisation, input validation) | Continuous |
| **Secret scanning** | Verify no credentials, API keys, or tokens in source code or configuration | Pre-commit and per build |

Vendor-side test results shall be shared with the organisation at agreed intervals (minimum: per milestone or sprint delivery).

**Organisation-Side Testing** (performed by organisation or appointed third party):

| Test Type | Requirement | Timing |
|-----------|-------------|--------|
| **Independent code review** | Internal developer or Security Champion reviews vendor code against secure coding checklist | Before acceptance of each deliverable |
| **Independent SAST/SCA** | Organisation runs its own SAST and SCA scans against delivered code | Before acceptance |
| **DAST** | Dynamic testing of running application (e.g., OWASP ZAP, Burp Suite, or equivalent) | Before production deployment |
| **Penetration testing** | External specialist penetration test for High-Risk applications | Before initial production deployment; annually thereafter |

**Minimum testing baseline**: All security testing shall, at a minimum, cover the OWASP Top 10:2025 categories.

All penetration testing shall be conducted by an independent external specialist company meeting at least one of:
- CREST certification (CREST Registered Penetration Tester or higher)
- Team members holding OSCP, GPEN, or CEH certifications
- Demonstrated experience with ≥5 comparable penetration tests in the past 2 years with verifiable references
- ISO 27001 certified pentesting firm with public client portfolio

Penetration test provider shall not be the same entity as the development vendor to ensure independence.

Vulnerabilities identified during testing shall be remediated by the vendor at the vendor's cost before the organisation accepts the deliverable. Critical and High vulnerabilities shall block acceptance.

### Vulnerability Remediation Management

All vulnerabilities identified in vendor deliverables shall be tracked through resolution:

**Tracking Process**:
1. **Discovery**: Vulnerability identified via SAST/SCA/DAST/pentest
2. **Assignment**: Vulnerability assigned to vendor with remediation SLA
3. **Verification**: Vendor provides fix + re-test results
4. **Validation**: Organisation validates fix effectiveness
5. **Closure**: Documented closure with test evidence

**Remediation SLA Tracking**:

| Severity | SLA | SLA Breach Response |
|----------|-----|---------------------|
| **Critical** | 7 days | Immediate CISO escalation; block acceptance; vendor performance review |
| **High** | 30 days | Development Manager escalation; acceptance conditional on remediation plan |
| **Medium** | 90 days | Track in weekly status meetings; may accept with documented risk acceptance and remediation commitment |
| **Low** | 180 days | Track in project backlog; may accept with planned future sprint for remediation |

**SLA Clock**:
- Starts from vulnerability disclosure to vendor
- Pauses for reasonable vendor clarification requests (<5 business days)
- Resets upon vendor request for SLA extension with justification (CISO approval)

**SLA Compliance Reporting**:
Tracked per vendor, per engagement. <70% compliance triggers vendor performance review.

---

## Acceptance Criteria

Outsourced deliverables shall not be accepted or deployed to production until all acceptance criteria are satisfied.

**Security Acceptance Checklist**:

| # | Criterion | Verified By |
|---|-----------|-------------|
| 1 | All contractually required security testing completed and results provided | Development Manager |
| 2 | No unresolved Critical or High vulnerabilities in SAST, SCA, DAST, or penetration test results | CISO / Security Team |
| 3 | Organisation's independent code review completed with no blocking findings | Development Manager |
| 4 | SBOM provided in CycloneDX or SPDX format; no components with unpatched Critical or High vulnerabilities where patches are available; vulnerabilities without patches require documented risk acceptance and compensating controls | Development Manager |
| 5 | No hardcoded secrets, credentials, or test data present in delivered code | Security Team |
| 6 | Code meets the organisation's secure coding standards | Security Champion / Senior Developer |
| 7 | All documentation delivered (architecture, API specifications, deployment guides, configuration) | Development Manager |
| 8 | Source code and all artifacts delivered to the organisation's repository or escrow agent | Development Manager |
| 9 | Data protection requirements met; no unauthorised personal data retained by vendor | Data Protection Officer / CISO |
| 10 | Licensing and intellectual property ownership confirmed per contract | Legal / Procurement |

*Blocking findings include:*
- Hardcoded credentials, API keys, or secrets
- SQL injection vulnerabilities (any severity)
- Authentication bypass vulnerabilities
- Authorisation flaws allowing privilege escalation
- Use of cryptographically broken algorithms (MD5, SHA-1 for security, DES, RC4)
- Exposure of sensitive data in logs or error messages
- Missing input validation on user-supplied data
- Critical or High severity findings from SAST/DAST unaddressed

**Acceptance sign-off**:

| Application Risk | Required Sign-Off |
|------------------|-------------------|
| High-Risk | CISO + Development Manager + Application Owner |
| Medium-Risk | Development Manager + Application Owner |
| Low-Risk | Development Manager |

Acceptance records shall be retained for the duration of the application lifecycle plus 3 years.

---

## Intellectual Property and Code Escrow

**Code Ownership**:

The development agreement shall clearly define ownership of all work products, including source code, documentation, designs, and related intellectual property.

Where the organisation commissions bespoke development, the default position shall be that the organisation owns all intellectual property rights in the deliverables upon final payment or upon delivery if payment-on-delivery, whichever occurs first. Any deviation from full ownership shall be documented, approved by Legal and the CISO, and justified by business need.

**Licensing**:

Where full ownership transfer is not possible (e.g., vendor retains rights to pre-existing components or frameworks), the agreement shall specify:

- A perpetual, irrevocable licence for the organisation to use, modify, and maintain the delivered software.
- Clear identification of vendor-owned components versus organisation-owned components.
- Licence terms for all third-party and open-source components included in the deliverable.

**Code Escrow**:

For Tier 1 vendor engagements where the organisation does not hold the source code directly, the organisation shall establish a code escrow arrangement with an independent escrow agent (e.g., Escode, Codekeeper, or equivalent).

**Escrow arrangement requirements**:

| Requirement | Detail |
|-------------|--------|
| **Deposit frequency** | Source code deposited at each major release, or at minimum quarterly |
| **Deposit contents** | Complete source code, build scripts, build environment specifications, documentation, dependencies, and deployment instructions sufficient to build and deploy the software independently |
| **Release conditions** | Vendor insolvency, cessation of business, material breach of maintenance obligations, or failure to provide contracted services |
| **Verification** | Escrow deposits verified annually by the escrow agent (build verification — confirming the deposited code compiles and produces a working build) |

**Escrow Deposit Verification Criteria**:
- Source code compiles without errors using documented build instructions
- All dependencies resolvable from public or documented private repositories
- Build environment specifications include all required tools, SDKs, and versions
- Resulting build artifact (executable, container image, deployable package) can be deployed to a test environment
- Basic smoke test passes (application starts, health check endpoint responds)
- No proprietary vendor-only tools required for build process

Verification performed by escrow agent annually. Failed verification requires vendor to correct deposit within 30 days.

Where the organisation holds source code directly in its own repositories, code escrow is not required, but the organisation shall maintain its own verified backups.

---

## Ongoing Monitoring

The organisation shall continuously monitor outsourced development activities throughout the engagement lifecycle.

**Monitoring Activities**:

| Activity | Frequency | Responsible |
|----------|-----------|-------------|
| **Security testing report review** | Per milestone or sprint delivery | Development Manager |
| **Progress and quality review** | Every 2 weeks or per sprint (for agile engagements) | Development Manager / Project Manager |
| **Vendor security posture review** | Annually (Tier 1); biennially (Tier 2); at renewal (Tier 3) | CISO / Information Security Manager |
| **Access review** | Quarterly — verify vendor personnel with active access still require it | IT Operations / Development Manager |
| **Compliance spot check** | Semi-annually — verify vendor adherence to secure coding standards | Security Team |
| **Incident and near-miss review** | Per occurrence | CISO |

Vendor performance scorecard shall be maintained quarterly, tracking: security testing compliance, SLA adherence, incident count, and audit findings. Results shall be reported to management annually.

**Escalation triggers**:

| Trigger | Action |
|---------|--------|
| Vendor fails to provide security test results within agreed timeframe | Escalate to Development Manager; hold acceptance |
| Critical vulnerability identified in vendor-delivered code | Escalate to CISO; vendor remediation within 7 days |
| Vendor security incident affecting the organisation's data or systems | Activate incident management process (A.5.24-28); notify CISO within 1 hour |
| Vendor fails annual security reassessment | Suspend new work assignments; remediation plan within 30 days; contract review |
| Evidence of unauthorised subcontracting | Escalate to CISO and Legal; contract review |

---

## Vendor Security Incident Response

When a vendor experiences a security incident affecting the organisation's engagement:

**Vendor Notification Obligation**:
- **Within 24 hours**: Initial notification of incident occurrence, nature, and potential impact
- **Within 72 hours**: Detailed incident report including scope, root cause analysis (preliminary), affected systems/data, and remediation actions

**Organisation Response**:

| Incident Type | Response Action |
|---------------|-----------------|
| **Vendor code repository compromise** | 1. Suspend vendor access to org systems 2. Forensic review of all vendor-delivered code 3. Full security re-testing before any further acceptance 4. Consider code re-write if malicious code suspected |
| **Vendor personnel credential theft** | 1. Revoke all vendor access credentials immediately 2. Review access logs for unauthorised activity 3. Re-issue credentials after vendor confirms compromise remediated 4. MFA mandatory for re-access |
| **Vendor data breach (org data exposed)** | 1. Activate org incident response process 2. Assess data protection authority notification requirements 3. Joint incident investigation 4. Contract review for liability and remediation costs |
| **Vendor supply chain compromise** | 1. Suspend acceptance of any deliverables using affected component 2. Review SBOM for affected dependency across all vendor work 3. Require vendor to remove/replace compromised component 4. Independent security re-testing |

CISO shall notify Executive Management within 24 hours of any vendor incident affecting organisational data or systems.

**Post-Incident Actions**:
- Vendor must provide post-incident report within 30 days
- Organisation conducts vendor security reassessment
- Contract continuation contingent on satisfactory remediation
- Significant incidents may trigger contract termination clause

---

## Data Protection Requirements

Where outsourced development involves access to personal data or systems processing personal data, additional data protection requirements shall apply.

**Data Processing Agreement (DPA)**:

In accordance with Swiss nFADP Art. 9, the organisation shall execute a DPA with the development vendor that addresses:

- Categories and types of personal data accessed.
- Purpose and duration of processing.
- Obligation to process data only as instructed by the organisation.
- Confidentiality obligations for vendor personnel.
- Technical and organisational security measures implemented by the vendor.
- Subprocessor notification and approval requirements.
- Data subject rights assistance obligations.
- Data return and deletion upon contract termination.
- Audit and inspection rights.

**Cross-Border Transfers**:

Where vendor development occurs outside Switzerland:

- A transfer impact assessment shall be completed per Swiss nFADP requirements.
- Appropriate safeguards shall be in place (e.g., Standard Contractual Clauses, adequacy decisions by the Federal Council, or binding corporate rules).
- Where the vendor processes data of EU/EEA individuals, GDPR Chapter V transfer requirements shall also be met.

**Data Minimisation for Development**:

- Vendors shall not receive production personal data for development or testing purposes.
- Where realistic data is required, sanitised, anonymised, or pseudonymised data shall be used.
- Synthetic data (artificially generated) is the preferred approach.
- Any use of transformed personal data shall be documented and approved by the Data Protection Officer or CISO.

**Synthetic Data Generation Approaches**:
- **Faker libraries**: Realistic but fake data (names, addresses, emails) — suitable for UI testing, reporting development
- **Data masking tools**: Retain data structure and referential integrity while obscuring values — suitable for complex schema testing
- **Rule-based generation**: Generate data matching production patterns and distributions — suitable for performance testing
- **AI-generated data**: ML models trained on production data to generate statistically similar synthetic datasets — suitable for analytics development

Tool examples: Faker (Python/JavaScript), Mockaroo (web-based), Tonic.ai, Gretel.ai (enterprise)

Where absolutely necessary to use production data (complex data relationships, rare edge cases), data shall be:
1. Subset to minimum records required (not full production dump)
2. Anonymised or pseudonymised per nFADP Art. 5
3. Approved by Data Protection Officer with documented justification
4. Encrypted at rest and in transit to vendor environment
5. Deleted from vendor systems within 30 days of development completion

**Swiss Federal Data Protection and Information Commissioner (FDPIC) Notification**:

Where a vendor security incident results in high risk to data subjects (nFADP Art. 24), the organisation shall notify the FDPIC without undue delay. High risk indicators include:
- Unauthorised access to special categories of personal data (Art. 5 para. 2)
- Data breach affecting >500 Swiss residents
- Compromise of sensitive personal data (health, financial, biometric)
- Incident involving systematic profiling or automated decision-making data

Vendor DPA shall require vendor to provide all information necessary for FDPIC notification within 48 hours of incident discovery.

---

## Definitions

| Term | Definition |
|------|------------|
| **Acceptance testing** | Formal verification that a deliverable meets specified requirements before deployment |
| **Code escrow** | Arrangement where source code is deposited with an independent third party for release to the organisation under specified conditions |
| **DAST** | Dynamic Application Security Testing — analyses running applications for security vulnerabilities |
| **DPA** | Data Processing Agreement — contract governing how a processor handles personal data on behalf of a controller |
| **SAST** | Static Application Security Testing — analyses source code for security vulnerabilities without executing the code |
| **SBOM** | Software Bill of Materials — inventory of all software components, dependencies, and their versions |
| **SCA** | Software Composition Analysis — identifies vulnerabilities and licence issues in third-party and open-source dependencies |
| **Subprocessor** | Third party engaged by the data processor (vendor) to process personal data on behalf of the controller (organisation) |
| **Supply chain attack** | Compromise of a software component, dependency, or development tool to inject malicious code or vulnerabilities into downstream systems |
| **Tier 1/2/3 vendor** | Vendor risk classification based on the sensitivity of systems developed and data accessed |

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; Tier 1 vendor security assessment approval; acceptance sign-off for High-Risk applications; exception approval; escalation authority; annual policy review |
| **Development Manager** | Vendor engagement coordination; security requirements communication; code review and acceptance management; monitoring of vendor deliverables; compliance reporting |
| **Information Security Manager** | Vendor security questionnaire management; compliance spot checks; monitoring of vendor security posture; incident investigation coordination |
| **Project Manager** | Day-to-day vendor relationship management; delivery milestone tracking; escalation of security concerns to Development Manager |
| **Data Protection Officer / CISO** | DPA review and approval; cross-border transfer assessments; data minimisation verification; data subject rights coordination |
| **Legal / Procurement** | Contract drafting and review; IP and licensing terms; NDA management; insurance verification; escrow arrangement coordination |
| **Security Team** | Independent security testing of vendor deliverables; penetration testing coordination; SAST/DAST/SCA execution; vulnerability triage |
| **IT Operations** | Vendor access provisioning and deprovisioning; access review support; environment segregation for vendor access |
| **Application Owner** | Security requirements initiation; acceptance sign-off; exception requests; budget for security testing |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency | Retention |
|---|----------|-------|-----------|-----------|
| 1 | **Vendor security assessment records** (questionnaires, audit reports, certification evidence, assessment decisions) | CISO / Information Security Manager | Per engagement + annual reassessment (Tier 1) | Vendor relationship duration + 3 years |
| 2 | **Development contracts with security clauses** (signed agreements, DPAs, NDAs, escrow arrangements) | Legal / Procurement | Per engagement | Contract duration + 7 years |
| 3 | **Vendor security testing reports** (SAST, SCA, DAST results provided by vendor per milestone) | Development Manager | Per milestone or sprint delivery | Application lifecycle + 3 years |
| 4 | **Organisation independent test results** (internal code review, independent SAST/SCA/DAST, penetration test reports) | Security Team / CISO | Per acceptance | Application lifecycle + 3 years |
| 5 | **Acceptance sign-off records** (security acceptance checklist, sign-off with date, approver, conditions) | Development Manager | Per deliverable | Application lifecycle + 3 years |
| 6 | **Vendor access records** (access grants, quarterly reviews, deprovisioning confirmations) | IT Operations / Development Manager | Per access event; quarterly reviews | Vendor relationship duration + 3 years |
| 7 | **SBOM records** (Software Bill of Materials for each accepted deliverable) | Development Manager | Per deliverable | Application lifecycle + 3 years |
| 8 | **Code escrow deposit and verification records** (deposit confirmations, annual build verification results) | Legal / Development Manager | Per deposit + annual verification | Contract duration + 3 years |
| 9 | **Vulnerability remediation tracking** (vendor remediation records, SLA compliance, closure evidence) | Development Manager / Security Team | Per vulnerability | 3 years |
| 10 | **Vendor monitoring records** (progress reviews, compliance spot checks, escalation records) | Development Manager / CISO | Per review cycle | Vendor relationship duration + 3 years |
| 11 | **Data protection records** (DPAs, transfer impact assessments, data minimisation approvals) | Data Protection Officer / CISO | Per engagement | Contract duration + 10 years (nFADP) |
| 12 | **Exception register** (exception requests, approvals, compensating controls, quarterly reviews) | Information Security Manager | Per exception; reviewed quarterly | Exception duration + 3 years |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, vendor security assessment records, contract clause audits, security testing reports, acceptance records, access reviews, internal and external audits, and feedback to the policy owner.

**Compliance Metrics**:

| Metric | Target | Measurement Frequency |
|--------|--------|-----------------------|
| Vendor engagements with completed security assessment before contract signature | 100% | Per engagement |
| Development contracts containing all mandatory security clauses | 100% | Per engagement |
| Outsourced deliverables with organisation-side independent security testing before acceptance | 100% | Per deliverable |
| Vendor-reported vulnerabilities remediated within SLA | >= 90% | Quarterly |
| Vendor access reviews completed on schedule | 100% | Quarterly |
| Tier 1 vendors with current security reassessment (within 12 months) | 100% | Annually |
| Code escrow deposits current (within agreed frequency) | 100% | Per deposit schedule |

**Non-Compliance Handling**: Below 70% on any metric requires immediate CISO escalation and a remediation plan. 70-89% requires Information Security Manager oversight with monthly review until restored. 90% and above follows standard quarterly monitoring.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date (maximum 12 months). Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Vendor non-compliance shall be addressed through contractual remedies, including contract suspension or termination for material security breaches.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to outsourcing industry practices and supply chain threat landscape, emerging software supply chain attack techniques (dependency confusion, typosquatting, CI/CD pipeline compromise), regulatory changes affecting data processing agreements and cross-border transfers, vendor management framework updates, audit findings, and lessons learned from security incidents involving outsourced development.

---

## Implementation Checklist (For Organisations New to Outsourcing)

**Before Engaging First Vendor**:
- [ ] Vendor security assessment questionnaire template created
- [ ] Standard outsourced development contract template with security clauses drafted (Legal review)
- [ ] DPA template compliant with nFADP Art. 9 prepared (DPO review)
- [ ] Secure coding standards documented and published
- [ ] SAST/SCA/DAST tooling selected and operational
- [ ] Security acceptance checklist template created
- [ ] Vendor access provisioning process documented
- [ ] Code escrow agent selected (if applicable for Tier 1)

**Per Engagement**:
- [ ] Vendor tier determined and documented
- [ ] Security assessment completed and approved
- [ ] Contract with security clauses signed
- [ ] DPA executed (if vendor accesses personal data)
- [ ] Secure development package delivered to vendor
- [ ] Vendor personnel background checks verified (Tier 1)
- [ ] Vendor access provisioned with least privilege
- [ ] Security testing cadence scheduled (milestone/sprint reviews)
- [ ] Acceptance criteria communicated to vendor
- [ ] Code repository or escrow arrangement established

---

# Areas of the ISO 27001 Standard Addressed

Outsourced Development Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.19 Information security in supplier relationships |
| Clause 7.3 Awareness | 5.20 Addressing information security within supplier agreements |
| | 5.21 Managing information security in the ICT supply chain |
| | 5.22 Monitoring, review, and change management of supplier services |
| | 5.36 Compliance with policies, rules, and standards |
| | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | 8.4 Access to source code |
| | 8.25 Secure development lifecycle |
| | 8.26 Application security requirements |
| | 8.28 Secure coding |
| | 8.29 Security testing in development and acceptance |
| | **8.30 Outsourced development** |
| | 8.31 Separation of development, test, and production environments |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures for data protection; Art. 9 — Data processing by third parties (processor agreements) |
| Swiss DSV (Data Protection Ordinance) | Art. 1-3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 28 — Processor obligations; Art. 32 — Security of processing; Chapter V — Cross-border data transfers |
| ISO/IEC 27001:2022 | Annex A Control 8.30 — Outsourced development |
| ISO/IEC 27002:2022 | Section 8.30 — Implementation guidance for outsourced development |
| NIST SP 800-53 Rev 5 | SA-4 (Acquisition Process), SA-9 (External System Services) |
| OWASP Top 10:2025 | A03 — Software Supply Chain Failures |
| CIS Controls v8 | 16.4 (Third-Party Software Component Inventory), 16.6 (Severity Rating for Application Vulnerabilities) |

---

<!-- QA_VERIFIED: 2026-02-08 -->
