**ISMS-OP-POL-A.5.8 — Information Security in Project Management**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Security in Project Management |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.8 |
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

- ISO/IEC 27001:2022 Control A.5.8 — Information security in project management
- ISO/IEC 27002:2022 Section 5.8 — Implementation guidance
- ISO 21500:2021 — Project, programme and portfolio management
- Swiss nFADP (revDSG) Art. 22 — Data protection impact assessment
- NIST SP 800-53 Rev 5 SA-3 — System Development Life Cycle
- NIST SP 800-53 Rev 5 PL-2 — System Security and Privacy Plans

**Related Annex A Controls**:

| Control | Relationship to Information Security in Project Management |
|---------|-----------------------------------------------------------|
| A.5.1 Policies for information security | Overarching policy framework providing security requirements baseline for projects |
| A.5.7 Threat intelligence | Threat intelligence informs project-specific risk assessment and threat modelling |
| A.5.9 Inventory of information and other associated assets | Projects create new assets that shall be registered upon handover |
| A.5.12 Classification of information | Data classification drives project security classification and control selection |
| A.5.19 Information security in supplier relationships | Supplier security requirements apply to projects involving external vendors |
| A.5.34 Privacy and protection of PII | DPIA requirements for projects processing personal data |
| A.8.25 Secure development life cycle | Secure development requirements for software projects |
| A.8.26 Application security requirements | Security requirements identification for application projects |
| A.8.27 Secure system architecture and engineering principles | Architecture security for infrastructure and system projects |
| A.8.29 Security testing in development and acceptance | Security testing requirements integrated into project phase gates |
| A.8.32 Change management | Change control process for project-initiated changes to production |

**Related Internal Policies**:

- Information Classification and Handling Policy
- Supplier Relationship Security Policy
- Secure Development Lifecycle Policy
- Change Management Policy
- Privacy and PII Protection Policy
- Risk Management Policy

---

# Information Security in Project Management Policy

## Purpose

The purpose of this policy is to ensure that information security risks related to projects and project deliverables are systematically identified, assessed, and treated throughout the project lifecycle. Information security shall be integrated into project management so that it is part of every project — not an afterthought applied at the end.

Projects introduce change. Change introduces risk. Whether the project is a new software application, an infrastructure upgrade, a vendor procurement, or a business process redesign, each project creates opportunities for security controls to be weakened, bypassed, or omitted unless security is explicitly addressed at every phase.

This policy supports Swiss nFADP (revDSG) by implementing organisational measures appropriate to risk to protect personal data during project activities, including the requirement for data protection impact assessments (DPIA) under Art. 22 where processing is likely to result in high risk to individuals' personality or fundamental rights. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 25 (data protection by design and by default) and Art. 35 (DPIA) requirements also apply.

## Scope

All projects undertaken by the organisation, regardless of type, methodology, size, or duration. This includes:

- Software development projects (internal and outsourced).
- System implementation and integration projects.
- Infrastructure deployment and migration projects (on-premises and cloud).
- IT procurement projects (hardware, software, SaaS services).
- Business process redesign projects with information security implications.
- Compliance and regulatory implementation projects.
- Merger, acquisition, or divestiture projects involving IT assets or data.

**Out of scope**: Routine operational activities not constituting a project (business-as-usual maintenance and support); emergency incident response activities (covered under the Incident Management Policy); minor changes managed through the standard change control process (covered under the Change Management Policy). Where uncertainty exists about whether an activity constitutes a project, the CISO or Information Security Officer shall advise.

## Principle

Information security should be integrated into project management. Security requirements shall be identified early — at project initiation — and addressed proportionally throughout the project lifecycle based on the project's security risk classification. No project shall proceed to production deployment without appropriate security validation for its classification level.

All project security decisions shall be risk-based, considering the sensitivity and classification of data involved, the criticality of affected systems, the regulatory environment, and the potential for business impact if security is inadequate.

---

## Project Classification

All projects shall be classified by information security risk to determine proportional security requirements. Classification shall occur at project initiation and be documented in the project charter or equivalent initiation document.

### Classification Factors

Projects shall be classified based on the **highest applicable factor** across the following dimensions:

| Factor | High Risk | Medium Risk | Low Risk |
|--------|-----------|-------------|----------|
| **Data sensitivity** | Confidential or restricted data (PII, financial records, intellectual property, trade secrets) | Internal data (non-public business information, employee records) | Public data (marketing content, published documentation) |
| **System criticality** | Business-critical system (RTO < 4 hours); revenue-generating or customer-facing | Business-important system (RTO 4-24 hours); internal operational | Support system (RTO > 24 hours); non-critical tooling |
| **Regulatory scope** | nFADP high-risk processing, GDPR Art. 35 DPIA required, PCI DSS applicable | nFADP standard processing applicable | No regulated data processing |
| **External exposure** | Internet-facing or accessible to external parties (customers, partners, public) | Controlled external access (VPN, dedicated connection) | Internal-only access |
| **Third-party involvement** | Critical function outsourced (hosting, authentication, payment processing) | Vendor-managed components (SaaS integration, managed services) | Fully internal delivery |

**Classification rule**: If **any single factor** meets the High Risk criteria, the project shall be classified as **High Risk**. If any factor meets Medium Risk (and no factor is High Risk), classify as **Medium Risk**. Only if **all factors** are Low Risk shall the project be classified as **Low Risk**.

### Classification Examples

To support consistent classification decisions, the following examples illustrate typical project scenarios by classification level:

| Factor | High Risk Example | Medium Risk Example | Low Risk Example |
|--------|-------------------|---------------------|------------------|
| **Data sensitivity** | Customer credit card data, employee health records | Employee email addresses, internal financial reports | Marketing brochures, public documentation |
| **System criticality** | Payment processing system (RTO < 1 hour) | Internal CRM (RTO 8 hours) | Test environment, proof-of-concept system |
| **Regulatory scope** | GDPR Art. 35 DPIA required (profiling), PCI DSS Level 1 merchant | Swiss nFADP applies (standard personal data) | No regulated data |
| **External exposure** | Public website, customer-facing API | Partner extranet, VPN-only access | Internal LAN only |
| **Third-party involvement** | Cloud-hosted payment processor, authentication SaaS | AWS-hosted with organisation management, Office 365 | Fully internal, on-premises |

### Classification Approval

| Classification | Approval Authority |
|----------------|-------------------|
| **High Risk** | CISO approval required |
| **Medium Risk** | Information Security Officer approval |
| **Low Risk** | Project Manager self-classifies; Information Security Officer confirms |

Classification shall be reviewed at each phase gate. If project scope, data sensitivity, or external exposure changes materially, the classification shall be updated and re-approved.

### Security Budget Guidance

Project managers shall estimate security costs based on project classification when preparing project budgets:

| Classification | Typical Security Cost | Activities Included |
|----------------|----------------------|---------------------|
| **High Risk** | 8–12% of total project cost | Threat modelling, security architecture review, penetration testing, security code review, Information Security Officer time |
| **Medium Risk** | 4–6% of total project cost | Security requirements analysis, vulnerability scanning, functional security testing, Information Security Officer time |
| **Low Risk** | 1–2% of total project cost | Security checklist review, basic vulnerability scanning |

Security budget estimates shall be included in the project initiation documentation and approved as part of the project budget. Where actual security costs are expected to exceed the estimated range, the Project Manager shall notify the Information Security Officer and adjust the project budget accordingly.

---

## Security Requirements Identification

Security requirements for project deliverables shall be identified systematically during the planning phase based on the project's classification and the categories of assets and data involved.

### Requirement Categories

The Project Manager, with Information Security Officer support, shall assess each of the following requirement categories against project scope:

| Requirement Category | Applicable When | Source |
|---------------------|-----------------|--------|
| **Access control** | All projects (minimum baseline) | Identity and Access Management Policy |
| **Data protection and encryption** | Project involves confidential or restricted data | Use of Cryptography Policy, nFADP Art. 8 |
| **Application security** | Project includes software development or custom code | Secure Development Lifecycle Policy |
| **Infrastructure security** | Project deploys or modifies network infrastructure | Network Security Policy |
| **Supplier security** | Project involves external vendors or cloud services | Supplier Relationship Security Policy |
| **Privacy and PII** | Project processes personal data | Privacy and PII Protection Policy, nFADP Art. 22 |
| **Business continuity** | Project affects business-critical systems | Business Continuity and DR Policy |
| **Logging and monitoring** | Project deploys systems requiring security monitoring | Logging and Monitoring Policy |

### Requirement Source Mapping

The following reference table indicates which policy areas typically apply to common project types, to assist Project Managers in identifying applicable requirements:

| Project Type | Always Applicable | Often Applicable | Conditionally Applicable |
|-------------|-------------------|------------------|-------------------------|
| **Software Development** | Secure Development Lifecycle, Access Control, Logging | Application Security, Data Protection, Change Management | Privacy and PII (if personal data), Supplier Security (if outsourced) |
| **Infrastructure Deployment** | Access Control, Network Security, Logging | Configuration Management, Business Continuity | Supplier Security (if vendor-managed) |
| **SaaS Procurement** | Supplier Security, Access Control | Data Protection, Privacy and PII | Application Security (if custom integration) |

### Documentation

- **High and Medium Risk projects**: Security requirements shall be documented in a Security Requirements Register (or equivalent section in [Project Management Tool]) and tracked through to implementation and testing.
- **Low Risk projects**: Security requirements shall be documented as risk mitigation items in the project risk register with confirmation of applicable policy compliance.

### Approval

- **High Risk**: CISO approves security requirements before execution phase.
- **Medium Risk**: Information Security Officer approves before execution phase.
- **Low Risk**: Information Security Officer confirms requirement completeness.

---

## Phase Gate Security Reviews

Security reviews shall be integrated into project governance at the following phase gates. Projects shall not proceed to the next phase until security criteria for the current phase gate are satisfied or formally accepted by the appropriate authority.

### Phase Gate Requirements

| Phase Gate | Security Activities Required |
|------------|------------------------------|
| **Initiation / Project Approval** | Security risk classification determined and approved; initial security risks identified in project risk register; security budget and resource requirements estimated; DPIA screening completed (see DPIA Integration section) |
| **Planning / Design Approval** | Security requirements documented, reviewed, and approved; threat model completed for High Risk projects (recommended for Medium Risk); security architecture reviewed for High Risk projects; DPIA completed where screening indicated high risk |
| **Execution / Build Checkpoint** | Security testing conducted per classification requirements; security findings tracked and remediated per severity targets; security requirements traced to implementation evidence |
| **Deployment / Go-Live Approval** | All Critical findings remediated; High findings remediated per classification targets (see Security Testing section); security handover documentation complete and accepted by operations; residual risks formally documented and accepted by appropriate authority |
| **Closure** | Lessons learned captured (mandatory for High/Medium Risk); new assets registered in asset inventory; residual risks transferred to operational risk register; project security documentation archived per records management requirements |

### Escalation Timelines

Security concerns at phase gates shall be escalated within:

- **2 business days** for High Risk projects.
- **5 business days** for Medium Risk projects.

**Escalation path**: Project Manager -> Information Security Officer -> CISO -> Executive Management.

Projects shall not proceed to the next phase without resolving Critical security concerns. High security concerns may proceed with formal risk acceptance from the appropriate authority. Medium and Low concerns may proceed with a documented mitigation plan.

---

## Security Testing by Classification

All projects shall include security testing proportional to their classification level. Testing shall be completed before deployment and the results documented.

### Testing Requirements

| Requirement | High Risk | Medium Risk | Low Risk |
|-------------|-----------|-------------|----------|
| **External penetration test** | Mandatory (independent third party, OWASP methodology or equivalent) | Required if internet-facing or processing regulated data; otherwise recommended | Not required |
| **Automated vulnerability scan** | Mandatory (weekly during development + final pre-deployment) | Mandatory (final pre-deployment scan) | Recommended |
| **Security code review** | Mandatory for custom code (minimum: authentication, authorisation, data protection, cryptographic functions) | Recommended for custom code | Not required |
| **Functional security testing** | Mandatory (authentication, authorisation, input validation, error handling, session management) | Mandatory (authentication, authorisation, data validation, error handling) | Security validation against requirements checklist |

### Remediation Targets Before Deployment

| Finding Severity | High Risk Projects | Medium Risk Projects | Low Risk Projects |
|-----------------|-------------------|---------------------|-------------------|
| **Critical** | 100% remediated | 100% remediated | 100% remediated |
| **High** | >=80% remediated | >=70% remediated | Best effort; risk-accepted |
| **Medium** | Tracked; remediation plan | Tracked; remediation plan | Tracked |
| **Low** | Documented | Documented | Documented |

If remediation targets cannot be achieved before the deployment deadline, residual risk shall be formally accepted per the Exception Management section of this policy.

Testing evidence (scan reports, penetration test reports, code review findings) shall be archived per records management requirements.

---

## Security Handover and Acceptance

At project closure, security handover documentation shall be provided to the operational team and validated as complete before the project is formally closed. Incomplete security handover blocks project closure.

### Handover Documentation

The security handover package shall include:

1. **Security architecture documentation** — system security design, trust boundaries, authentication and authorisation model, encryption implementation, data flow diagrams with classification, network architecture and segmentation.

2. **Operational security procedures** — monitoring requirements (log sources, alert thresholds, [SIEM] integration), backup and recovery procedures, security patch management approach, incident response escalation paths.

3. **Accepted residual risks** — formal risk acceptance records with approval signatures, compensating controls where applicable, risk re-assessment timeline for time-limited acceptances.

4. **Security testing evidence** — final vulnerability scan report (dated within 7 days of deployment), penetration test report (if applicable), remediation records for Critical and High findings.

### Handover Acceptance

The operational owner shall confirm handover completeness via a signed Security Handover Checklist before the Project Manager requests project closure authorisation. For High Risk projects, the CISO shall additionally approve the handover.

Upon handover acceptance, the Project Manager shall ensure:
- New assets are registered in the asset inventory.
- Residual risks are transferred to the operational risk register.
- Security documentation is archived per records management requirements.

---

## Project Security Roles

### RACI Matrix

| Activity | Project Manager | InfoSec Officer | CISO | Business Owner | Technical Lead |
|----------|:-:|:-:|:-:|:-:|:-:|
| Project security classification | R | A | I | C | C |
| Security requirements identification | R | A | I | C | C |
| Security architecture design | C | C | I | I | R/A |
| Security testing execution | R | C | I | I | R |
| Residual risk acceptance | I | C | A (High) | A (Med/Low) | I |
| Security handover to operations | R | A | I | C | C |
| Lessons learned | R | C | I | C | C |

R = Responsible (does the work), A = Accountable (final decision), C = Consulted (input required), I = Informed (kept updated).

### Role Descriptions

| Role | Key Responsibilities |
|------|---------------------|
| **Executive Management** | Approve this policy; accept residual risks for critical projects; ensure resources for project security |
| **CISO** | Approve High Risk classifications; accept residual risks for High Risk projects; halt projects with unacceptable security risk; monitor project security metrics |
| **Information Security Officer** | Support project teams with risk assessment and requirements; approve Medium Risk classifications; review security testing adequacy; maintain security requirements templates |
| **Project Manager** | Classify project security risk; plan and budget security activities; execute security activities at each phase; maintain project security risk register; escalate security concerns |
| **Business Owner / Product Owner** | Define business security requirements; participate in risk assessment; accept residual risks for owned systems (Medium/Low Risk) |
| **Technical Lead / Solution Architect** | Design security controls into solution architecture; implement security requirements; support threat modelling; address security findings |
| **Third-Party Vendors** | Comply with contractual security requirements; participate in security assessments; report security incidents or vulnerabilities |

### Security Champions (Optional)

Organisations with 50 or more employees should consider appointing Security Champions within project teams to improve security integration and reduce bottlenecks on the Information Security Officer:

| Aspect | Description |
|--------|-------------|
| **Selection** | Trained team member (developer, business analyst, or project manager) who acts as security liaison within the project team |
| **Training** | Security Champions shall attend security training (minimum 8 hours per year) covering secure development practices, threat identification, and organisational security policies |
| **Responsibilities** | Help identify security requirements during planning; advocate for security within the project team; escalate security concerns to the Information Security Officer; support security testing coordination |
| **Benefits** | Reduces bottleneck on the Information Security Officer; builds security awareness across the organisation; creates security advocates embedded in project teams |

The Information Security Officer shall coordinate the Security Champion programme, including selection criteria, training content, and ongoing support.

---

## DPIA Integration

Where a project involves the processing of personal data, a Data Protection Impact Assessment (DPIA) screening shall be performed at project initiation to determine whether a full DPIA is required.

### DPIA Screening

A DPIA screening shall be completed for every project that processes personal data. The screening shall assess whether the planned processing is likely to result in high risk to individuals' personality or fundamental rights, as required by Swiss nFADP Art. 22.

**A DPIA is mandatory when the project involves any of the following:**

- Extensive processing of sensitive personal data (health data, biometric data, political opinions, religious beliefs, criminal records, or social assistance measures under nFADP Art. 5).
- Systematic and extensive monitoring of individuals (including profiling per nFADP Art. 5 lit. f).
- New technology deployment where the privacy impact is uncertain.
- Large-scale automated decision-making with significant effects on individuals.
- Combining or matching data sets from different sources in ways individuals would not reasonably expect.

### DPIA Timing

- **Screening**: Completed at project initiation (before Planning phase gate).
- **Full DPIA** (where required): Completed during the planning phase, before the execution phase gate.
- **DPIA update**: Required when project scope, data processing, or technology changes materially during execution.

### DPIA Approval

The completed DPIA shall be reviewed by the Data Protection Officer (or CISO where no DPO is appointed) and approved before the project proceeds to execution. Where the DPIA identifies residual high risks that cannot be mitigated, the organisation shall consult the Federal Data Protection and Information Commissioner (FDPIC) before proceeding, as required by nFADP Art. 23.

---

## Agile and Iterative Project Integration

For projects using Agile, Scrum, or other iterative methodologies, security shall be integrated into the iterative process rather than deferred to the end.

### Security in Iterative Development

| Agile Activity | Security Integration |
|---------------|---------------------|
| **Backlog refinement** | Security stories and security acceptance criteria added to user stories involving sensitive data, authentication, authorisation, or external interfaces |
| **Sprint planning** | Security tasks estimated and included in sprint capacity; security stories prioritised alongside business features |
| **Sprint execution** | Automated security testing (SAST, dependency scanning) integrated into CI/CD pipeline; security findings treated as defects and tracked in sprint backlog |
| **Sprint review** | Security status reported alongside feature progress; security debt tracked and prioritised |
| **Release planning** | Security testing requirements (penetration testing, vulnerability scanning) scheduled before production release per classification requirements |

### Security Checkpoints for Iterative Projects

Rather than single phase gates, iterative projects shall implement security checkpoints at the following points:

- **Project initiation**: Security classification, DPIA screening, and initial threat model (same as traditional projects).
- **Architecture sprint / Sprint 0**: Security architecture review; security requirements baseline established.
- **Each release candidate**: Automated security scan results reviewed; manual security testing for releases to production.
- **Production release**: Full security testing per classification requirements; security handover updated.
- **Project closure**: Final lessons learned; residual risks transferred to operations.

---

## Procurement Project Security

Projects involving procurement of IT systems, software, or services shall include information security requirements in the procurement process.

### Procurement Security Requirements

- **Vendor security assessment**: Vendors shall be assessed against the organisation's supplier security requirements (per the Supplier Relationship Security Policy) before contract award.
- **Security requirements in contracts**: Contracts shall include information security requirements, including data protection obligations, incident notification requirements, audit rights, and subcontractor controls.
- **Security acceptance criteria**: Procurement acceptance criteria shall include security validation (e.g., vulnerability scan of delivered system, security configuration review, access control verification).
- **Data processing agreements**: Where the vendor processes personal data on behalf of the organisation, a data processing agreement compliant with nFADP Art. 9 (and GDPR Art. 28 where applicable) shall be executed before data processing begins.

---

## Definitions

| Term | Definition |
|------|------------|
| **Project** | A temporary endeavour with defined start and end dates, undertaken to create a unique product, service, or result that involves information assets or information systems |
| **Phase gate** | A formal review point between project phases where security criteria must be satisfied before the project proceeds |
| **Security classification** | The categorisation of a project as High Risk, Medium Risk, or Low Risk based on information security impact factors |
| **Security Requirements Register** | A documented list of security requirements for a project, tracked through to implementation and testing |
| **DPIA (Data Protection Impact Assessment)** | A structured assessment of the impact of planned data processing on the protection of personal data, required by nFADP Art. 22 where processing is likely to result in high risk |
| **Threat model** | A structured analysis of potential threats to a system or application, identifying attack vectors, threat actors, and required countermeasures |
| **Residual risk** | The risk remaining after security controls have been implemented, which must be formally accepted by the appropriate authority |
| **Security handover** | The formal transfer of security documentation, responsibilities, and operational procedures from the project team to the operational team at project closure |
| **Security Champion** | A trained team member embedded in a project team who acts as a security liaison, helping identify security requirements and advocating for security best practices |

---

## Roles and Responsibilities

| Role | Information Security in Project Management Responsibilities |
|------|-------------------------------------------------------------|
| **Executive Management** | Approve this policy; ensure organisational resources for project security; accept residual risks for critical projects; review High Risk project security status in management reviews |
| **CISO** | Approve High Risk classifications and residual risk acceptance; halt or delay projects with unacceptable security risk; monitor project security metrics; approve exceptions to security requirements |
| **Information Security Officer** | Support project teams with security risk assessment and requirements identification; approve Medium Risk classifications; review security testing adequacy; maintain security templates and checklists |
| **Project Manager** | Classify project security risk (with InfoSec support); plan and budget security activities; execute security activities at each phase gate; maintain project security risk register; prepare security handover documentation |
| **Business Owner** | Define business security requirements; participate in security risk assessment; accept residual risks for Medium/Low Risk projects; approve security requirements as part of project scope |
| **Technical Lead** | Design security controls into solutions; implement security requirements; support threat modelling; address security findings from testing |
| **Data Protection Officer** | Review and approve DPIAs; advise on data protection requirements for projects; liaise with FDPIC where required by nFADP Art. 23 |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Project classification records** showing security risk classification determination and approval for each project | Project Manager | *Per project initiation; archived at project closure* |
| 2 | **Security requirements registers** (or risk register entries for Low Risk) documenting identified security requirements and implementation status | Project Manager | *Per project; updated throughout lifecycle* |
| 3 | **Phase gate approval records** with security criteria verification and sign-off | Project Manager | *Per phase gate; archived at project closure* |
| 4 | **Security testing reports** (penetration tests, vulnerability scans, code reviews) per classification requirements | InfoSec Officer | *Per project; final report within 7 days of deployment* |
| 5 | **Security finding remediation records** tracking findings to closure or risk acceptance | Project Manager | *Per project; updated until closure* |
| 6 | **Security handover documentation** packages accepted by operational teams | Project Manager | *Per project closure* |
| 7 | **Residual risk acceptance records** with appropriate approvals per classification | CISO / Business Owner | *Per project where residual risks exist* |
| 8 | **DPIA screening records** (and full DPIA where applicable) for projects processing personal data | DPO / CISO | *Per project involving personal data* |
| 9 | **Lessons learned documentation** for Medium and High Risk projects | Project Manager | *Per project closure* |
| 10 | **Security exception register** with approvals, compensating controls, and time limits | CISO | *Per exception; reviewed quarterly* |
| 11 | **Project security metrics dashboard** showing classification distribution, testing completion, and findings trends | CISO | *Monthly; reported quarterly to Executive Management* |
| 12 | **Training records** for project managers on security requirements integration | HR / InfoSec Officer | *Annual; completion tracked* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, project classification audits, phase gate compliance reviews, security testing completion verification, handover documentation reviews, internal and external audits, and feedback to the policy owner.

The following metrics shall be tracked and reported to the CISO quarterly:

| Metric | Target | Red Threshold |
|--------|--------|---------------|
| Projects classified within 5 business days of initiation | 100% | <80% |
| High/Medium Risk projects with completed security requirements register | 100% | <90% |
| Security testing completed before deployment | 100% | <90% |
| Critical security findings remediated before deployment | 100% | <100% (any Critical finding deployed = red) |
| Security handover documentation accepted before project closure | 100% | <80% |
| DPIA screening completed for projects processing personal data | 100% | <90% |
| Lessons learned captured for High/Medium Risk projects | 100% | <80% |

### Metrics Dashboard

The CISO shall maintain a project security metrics dashboard providing at-a-glance programme health visibility. The dashboard shall include:

- **Overall programme compliance score** — aggregate of the seven metrics above, calculated as the weighted average of target achievement.
- **Per-metric compliance bars** — each metric displayed with current percentage and status indicator (green >= target, amber >= red threshold, red < red threshold).
- **Active projects by classification** — count of active High, Medium, and Low Risk projects.
- **Attention items** — projects with overdue security activities or metrics breaching amber/red thresholds.

The dashboard shall be reviewed at the monthly CISO review and included in the quarterly Executive Management report to provide clear visibility of project security programme effectiveness.

**Reporting requirements**:
- **Monthly CISO dashboard**: Projects by classification and security status (on track / at risk / overdue); open security findings by severity and age; security exceptions granted.
- **Quarterly Executive Management report**: Total projects and High Risk project count; critical security findings and remediation status; DPIA completion rates; significant security incidents affecting projects.
- **Annual Management Review**: Full project security programme effectiveness; metrics trends; significant findings; improvement recommendations.

Metrics breaching red thresholds shall be escalated to the CISO for immediate attention and reported at the next Management Review.

## Exceptions

Any exception to this policy shall be approved and recorded by the CISO in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions to security testing or phase gate requirements for High Risk projects require joint CISO and Executive Management approval. Exceptions shall not exceed 90 calendar days without re-assessment and re-approval.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Projects deployed without required security testing or classification may be subject to immediate suspension until security requirements are met. Non-compliance shall be reported to the CISO and recorded in the ISMS nonconformity register.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to project management methodology, audit findings, regulatory changes (including nFADP amendments), security incidents related to projects, exception trends, lessons learned from project security reviews, and evolution of threat landscape. Nonconformities related to this policy shall be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Areas of the ISO 27001 Standard Addressed

Information Security in Project Management Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.3 Organisational roles, responsibilities and authorities | **5.8 Information security in project management** |
| Clause 6.1 Actions to address risks and opportunities | 5.7 Threat intelligence |
| Clause 6.2 Information security objectives and planning | 5.9 Inventory of information and other associated assets |
| Clause 7.4 Communication | 5.12 Classification of information |
| Clause 8.1 Operational planning and control | 5.19 Information security in supplier relationships |
| Clause 9.1 Monitoring, measurement, analysis and evaluation | 5.34 Privacy and protection of PII |
| Clause 10.2 Nonconformity and corrective action | 8.25 Secure development life cycle |
| | 8.26 Application security requirements |
| | 8.29 Security testing in development and acceptance |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 7 — Data protection by design and by default; Art. 8 — Technical and organisational measures; Art. 22 — DPIA for high-risk processing; Art. 23 — Consultation of FDPIC |
| Swiss DSV (Data Protection Ordinance) | Art. 1-3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 25 — Data protection by design and by default; Art. 32 — Security of processing; Art. 35 — Data protection impact assessment |
| ISO/IEC 27001:2022 | Annex A Control 5.8 — Information security in project management |
| ISO/IEC 27002:2022 | Section 5.8 — Implementation guidance for information security in project management |
| ISO 21500:2021 | Project, programme and portfolio management — Context and concepts |
| NIST SP 800-53 Rev 5 | SA-3 (System Development Life Cycle) — Security integration throughout system life cycle; PL-2 (System Security and Privacy Plans) — Security planning for systems |
| NIST CSF 2.0 | GV.RR — Roles, responsibilities, and authorities; ID.RA — Risk Assessment; PR.IP — Information Protection Processes and Procedures |
| CIS Controls v8 | Control 16 (Application Software Security) — Secure development lifecycle safeguards; Governance function — Policies and procedures for asset protection |

---

<!-- QA_VERIFIED: 2026-02-08 -->
