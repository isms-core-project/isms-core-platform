**ISMS-OP-POL-A.5.1-2-6.1-2 — ISMS Governance and Secure Employment**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | ISMS Governance and Secure Employment |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.1-2-6.1-2 |
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

- ISO/IEC 27001:2022 Control A.5.1 — Policies for information security
- ISO/IEC 27001:2022 Control A.5.2 — Information security roles and responsibilities
- ISO/IEC 27001:2022 Control A.6.1 — Screening
- ISO/IEC 27001:2022 Control A.6.2 — Terms and conditions of employment
- Swiss Code of Obligations (OR) Art. 328, 328b
- Swiss Federal Data Protection Act (nFADP/revDSG)

**Related Annex A Controls**:

| Control | Relationship to ISMS Governance and Secure Employment |
|---------|-------------------------------------------------------|
| A.5.3 Segregation of duties | Roles must enforce segregation between policy creation, execution, and oversight |
| A.5.4 Management responsibilities | Management support underpins policy governance and personnel security |
| A.5.10 Acceptable use of information | AUP is a key policy requiring acknowledgment under A.6.2 |
| A.5.24–28 Incident management | Incident reporting obligations included in employment terms |
| A.5.35–36 Independent review and compliance | Policies are the baseline against which compliance is measured |
| A.6.3 Awareness, education, and training | Training obligations established through employment terms |
| A.6.4 Disciplinary process | Policy violation handling and consequences |
| A.6.5 Responsibilities after termination | Post-employment obligations originate in A.6.2 contract clauses |
| A.8.2 Privileged access rights | Elevated screening requirements for privileged roles |

**Related Internal Policies**:

- Acceptable Use Policy
- Information Classification and Handling Policy
- Incident Management Policy
- Access Control Policy
- Privacy and Protection of PII Policy
- Information Security Awareness and Training Policy

---

# ISMS Governance and Secure Employment Policy

## Purpose

The purpose of this policy is to establish the organisation's information security policy framework, define security roles and responsibilities, set personnel screening requirements, and specify the information security obligations within employment contracts.

This policy supports Swiss nFADP (revDSG) by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data) throughout the employment lifecycle. Swiss Code of Obligations (OR) Art. 328 (employer duty of care) and Art. 328b (employee data processing) apply to all screening and employment activities. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

## Scope

All employees (full-time, part-time, temporary), contractors, consultants, interns, apprentices, and third-party personnel with access to the organisation's information assets, systems, or facilities.

All information security policies, security-related roles, pre-employment and during-employment screening activities, and employment-related contracts and agreements.

## Principle

Information security is managed based on risk, legal and regulatory requirements, and business need. The organisation shall maintain a structured policy framework, assign clear security roles and responsibilities, verify the suitability of personnel before granting access, and contractually bind all personnel to information security obligations.

---

## Chief Executive's Statement of Commitment

"As an organisation, information processing is fundamental to our success and the protection, availability, and security of that information is a board-level priority. Whether it is employee information, customer information, or intellectual property, we take our obligations under Swiss law and international standards seriously. We have provided the resources to develop, implement, and continually improve the information security management system and to ensure all personnel understand and fulfil their security responsibilities."

[Chief Executive Officer — Name, Date, and Signature]

---

## Information Security Defined

Information security is defined as preserving:

| Property | Definition |
|----------|------------|
| **Confidentiality** | Access to information is restricted to those with appropriate authority — the right people with the right access |
| **Integrity** | Information is complete, accurate, and protected from unauthorised modification — the right data |
| **Availability** | Information is accessible when it is needed by authorised users — at the right time |

---

## Information Security Policy Framework (A.5.1)

### Policy Hierarchy

The information security management system is built upon a hierarchical policy framework:

| Tier | Type | Approval Authority | Review Frequency |
|------|------|-------------------|------------------|
| 1 | Master Information Security Policy | Executive Management (CEO/Board) | Annual |
| 2 | Topic-Specific Policies (Annex A) | CISO | Annual |
| 3 | Standards and Guidelines | Information Security Manager | As needed |
| 4 | Procedures and Work Instructions | Process Owner | As needed |

Higher-tier policies set requirements; lower-tier documents provide operational detail. Lower-tier documents shall not contradict higher-tier policies.

### Policy Lifecycle

Information security policies shall be managed through defined lifecycle stages:

**Creation**: Policies shall be developed using the organisational template, with input from stakeholders including Legal, HR, IT, and affected business units.

**Approval**: Policies shall be approved by the appropriate authority per tier before publication. Policy approval shall be performed by a different individual than the policy author. Tier 2 policies authored by the Security Team shall be approved by the CISO. The Master Policy authored by the CISO shall be approved by the CEO.

**Publication**: Approved policies shall be published to the organisational policy repository (e.g., SharePoint, Confluence, or equivalent) with version control.

**Communication**: Policies shall be communicated to all affected personnel. Supplemental training shall be provided when: (a) >30% of users are affected, (b) a new technical control requires user action (e.g., MFA enrolment), or (c) a regulatory deadline is <90 days. Training formats: webinar, e-learning module, or annotated policy guide.

**Acknowledgment**: Critical policies (Master Information Security Policy, Acceptable Use Policy, Code of Conduct) shall require formal acknowledgment from all personnel annually. Acknowledgments shall be collected via [electronic signature portal / HR system attestation] and tracked in the Personnel Training and Acknowledgment Register maintained by HR.

**Review**: Policies shall be reviewed at planned intervals (minimum annually) and upon:

- Significant regulatory change (new applicable regulation, material amendment, enforcement action).
- Major security incident (Severity 1–2 per incident management policy).
- Organisational change (merger, acquisition, significant restructure).
- Failed audit finding requiring policy amendment.

**Change management**: Policy changes shall follow the change management process: change request logged in [GRC Tool / Change Management System], impact assessment performed (affected systems, users, controls), approval obtained per policy tier, change communicated to affected personnel, change implementation tracked (old version archived, new version published), and post-implementation review within 30 days to verify acknowledgments collected and no unintended impacts.

**Retirement**: Retired policies shall be archived with audit trail retained for a minimum of 3 years.

### Policy Content Requirements

All topic-specific policies (Tier 2) shall include:

- Document control (ID, version, approval, dates).
- Purpose and scope.
- Control alignment (ISO 27001:2022 controls addressed).
- Requirements framework (what is required, who is accountable, when it applies).
- Roles and responsibilities.
- Regulatory framework reference.

### Policy Exceptions

Exceptions to any information security policy shall be:

- Documented with business justification and risk assessment.
- Approved by CISO (medium risk) or Executive Management (high risk).
- Time-limited: medium risk = 6 months (renewable once), high risk = 3 months (renewable with Executive approval). Critical controls = no exception without Board approval.
- Include compensating controls to mitigate residual risk.
- Tracked in the Policy and Control Exception Register maintained by the CISO in [GRC Tool / controlled shared drive].

The exception register shall record: exception ID, affected control or policy, description, requestor, business justification, risk assessment, compensating controls, approval authority, approval date, expiry date, and review status.

Exceptions shall be reviewed quarterly by the ISMS Committee and reported in Management Review. Expired exceptions shall be re-assessed or closed within 30 days.

### Policy Violation Handling

Policy violations shall be classified by severity:

| Severity | Criteria | Investigation | Response |
|----------|----------|---------------|----------|
| **Critical** | Intentional misconduct, data breach, regulatory violation | Executive Management investigation within 24 hours | Disciplinary action up to termination; legal/regulatory reporting if required |
| **High** | Repeated violations, deliberate circumvention of controls | CISO investigation within 3 business days | Formal written warning; mandatory retraining; 90-day monitoring |
| **Medium** | Unintentional non-compliance, isolated incident | Manager investigation within 5 business days | Documented coaching; corrective action; 30-day follow-up |
| **Low** | Procedural error, no security impact, first occurrence | Manager-led discussion | Policy clarification; no formal disciplinary action unless recurring |

All violations (Critical, High, Medium) shall be logged in the Security Incident Register with investigation findings, remediation actions, and closure date. Violations shall be analysed quarterly for trends and policy effectiveness improvement.

---

## Information Security Roles and Responsibilities (A.5.2)

### Organisational Security Structure

The organisation shall establish a clear security organisational structure with:

- **Clear accountability**: Every security responsibility assigned to a specific role.
- **Segregation of duties**: Separation between policy definition, execution, and oversight.
- **CISO independence**: The CISO shall report to executive level (CEO, COO, or CTO).
- **Adequate resources**: Security roles provided with budget, tools, personnel, and training commensurate with organisational size, complexity, and risk profile.
- **Commensurate authority**: Security roles granted authority matching their responsibilities.

### Key Security Roles

The organisation shall define and assign the following security roles:

**Executive Management (CEO/Board)**:

- Ultimate accountability for the ISMS and regulatory compliance.
- Approves the Master Information Security Policy and risk appetite.
- Allocates resources for the information security programme.
- Reviews ISMS performance quarterly via Management Review meetings. Receives incident summary, control effectiveness metrics, and risk changes.

**Chief Information Security Officer (CISO)**:

- Accountable for ISMS design, implementation, and continuous improvement.
- Approves topic-specific policies (Tier 2).
- Oversees the security team, incident response, and compliance activities.
- Reports ISMS performance to Executive Management.

**Data Protection Officer (DPO)**:

- Accountable for nFADP and GDPR compliance (where applicable).
- Reviews policies and screening practices for data protection compliance.
- Independent reporting to Executive Management.
- Contact point for data subjects and the Federal Data Protection and Information Commissioner (FDPIC).

**Information Security Team**:

- Operational implementation of security controls.
- Security monitoring, incident response, and assessments.
- Security awareness training delivery.
- Audit support and evidence collection.

### Competence Requirements for Security Roles

| Role | Minimum Qualifications | Verification |
|------|----------------------|-------------|
| **CISO** | CISSP, CISM, or equivalent; minimum 5 years security management experience; demonstrated knowledge of ISO 27001 and relevant frameworks | Verified at hire; reviewed annually |
| **Information Security Team** | Security+, CEH, or equivalent; relevant technical certifications for assigned domains (e.g., AWS Security Specialty for cloud security) | Verified at hire; reviewed annually |
| **DPO** | CIPP/E, CIPM, or equivalent data protection qualification; knowledge of nFADP and GDPR | Verified at hire; reviewed annually |

Competence shall be verified at hire and reviewed annually. Where gaps are identified, a training plan shall be developed within 30 days with target completion within 6 months.

**System Owners**:

- Accountable for security of assigned systems.
- Implement controls, maintain compliance, and conduct access reviews.
- Report incidents affecting assigned systems.

**Data Owners**:

- Accountable for classification and protection of assigned data.
- Define and approve access requirements.
- Conduct data access reviews.

**Line Managers**:

- Ensure direct reports complete training and comply with policies.
- Initiate joiner/mover/leaver processes.
- Approve access requests with business justification.
- Include security responsibilities in annual performance reviews for direct reports with security accountabilities (System Owners, Data Owners). Assess compliance with training, access review, and incident reporting obligations.

**All Personnel**:

- Comply with policies, complete training, and protect organisational assets.
- Report security incidents immediately.
- Maintain confidentiality of organisational information.

### Role Documentation

All security-related roles shall be documented with: role title and purpose, key responsibilities (typically 5–10 items), required qualifications, authority and decision rights, reporting structure, performance metrics, and annual review date.

**[GRC Tool]** is the authoritative source for all security role descriptions. Read-only copies are published to [HR System] and the policy appendix. Synchronisation occurs monthly.

Role descriptions shall be reviewed annually by the role holder's manager in coordination with the CISO. Updates shall be version-controlled and communicated to affected personnel.

### Third-Party Security Responsibilities

Third-party security responsibilities shall be:

- Defined in service agreements and contracts.
- Proportional to access granted.
- Subject to periodic review (at minimum annually).
- Managed by the contract owner in coordination with the information security team.

Third-party compliance shall be spot-checked annually, verifying screening completion, security training completion, and contract clause acknowledgment:

| Vendor Size | Sample Size |
|-------------|------------|
| **Critical vendors (>20 personnel)** | 10% sample, minimum 3 individuals |
| **Medium vendors (5–20 personnel)** | 20% sample, minimum 2 individuals |
| **Small vendors (<5 personnel)** | 100% verification |

Non-compliance shall trigger vendor escalation and remediation within 30 days.

### Succession Planning

Key security roles (CISO, Information Security Manager, DPO) shall have documented succession plans to ensure continuity during unplanned absences or planned transitions. Succession plans shall be reviewed annually and include: designated interim successor(s), notification procedure, knowledge transfer checklist (critical systems, ongoing projects, key contacts), and cross-training schedule.

---

## Personnel Screening (A.6.1)

### Screening Principles

The organisation shall conduct background verification checks based on:

**Proportionality**: Screening intensity shall be proportional to the sensitivity of information accessed, the criticality of the role, the level of system access and privileges, and regulatory requirements.

**Legality**: All screening shall comply with Swiss Code of Obligations (OR) Art. 328 and 328b, Swiss nFADP (revDSG), and local employment law. Under Swiss law, employers may only collect information relevant to the role. Written consent from the candidate shall be obtained before conducting background checks. Criminal record checks may cover up to seven years in Switzerland.

**Fairness**: Screening shall be conducted transparently. Candidates shall be informed before screening is conducted, consent shall be obtained where required, criteria shall be non-discriminatory and job-relevant, and candidates shall have the opportunity to clarify adverse findings.

**Confidentiality**: Screening results shall be accessed only by HR and authorised hiring personnel, stored securely in [HR System] with access controls, retained for the duration of employment plus 2 years (for defence of employment decisions), and securely destroyed per the data deletion procedure thereafter.

### Screening Levels

The organisation shall classify roles by sensitivity and apply appropriate screening:

| Level | Applicable To | Verification Required |
|-------|--------------|----------------------|
| **Level 1: Basic** | All personnel | Identity verification, right to work, most recent employer reference, education verification |
| **Level 2: Standard** | Roles with Internal/Confidential data or system access | Level 1 + extended employment history (5 years), professional references |
| **Level 3: Enhanced** | Privileged access, Restricted data, Security Team, Finance | Level 2 + criminal record excerpt (Strafregisterauszug — standard excerpt, voluntary, requires explicit candidate consent; Sonderprivatauszug where legally required, e.g., FINMA-regulated roles, roles involving children/vulnerable persons), credit check (only for roles with direct financial authority: CFO, Finance Director, Treasury, Accounts Payable Manager, or roles with access to payment systems — candidate must provide written consent and be informed of check scope, e.g., insolvency record, debt enforcement register), adverse media screening (limited to: criminal convictions, regulatory sanctions, professional misconduct findings published by authorities — social media content, unverified allegations, and political opinions excluded) |
| **Level 4: Security Clearance** | CISO, highest-sensitivity roles | Level 3 + extended background investigation, character references |

The role-to-screening-level mapping shall be documented and maintained by HR in consultation with the CISO. Assignments shall be reviewed annually and upon organisational restructure. Changes require CISO approval and HR execution.

### Screening Timing

**Pre-employment**: Screening shall be completed before granting organisational access.

**Interim access exception**: Emergency access before screening completion requires:

- Manager and CISO approval.
- Compensating controls (close supervision, limited access scope).
- Maximum 15 business days duration.
- Documented business justification.
- Interim access not permitted for Level 3 or Level 4 roles.

**Ongoing screening**:

Re-screening shall be conducted only where: (a) contractually agreed in employment terms, (b) required by regulation (e.g., FINMA for financial sector roles), or (c) triggered by security incident or role change requiring elevated access.

- Level 4 roles: Re-screening every 2–3 years (contractual basis).
- Privileged access roles: Re-screening every 5 years or upon significant role change.
- All roles: Right-to-work verification upon permit renewals.

### Adverse Findings

Adverse findings shall be discussed with the candidate to allow clarification, assessed for relevance, recency, and severity, documented with a decision rationale, and handled consistently and non-discriminatorily.

### Third-Party Personnel Screening

Third-party personnel screening shall be specified in contracts (minimum screening requirements equivalent to the access granted), attested by the vendor, and spot-checked by the organisation (sample verification per the third-party spot-checking process).

Before granting third-party personnel access, conduct a vendor risk assessment:

| Factor | Assessment |
|--------|-----------|
| **Data sensitivity** | What data will vendor access (Public / Internal / Confidential / Restricted)? |
| **Access level** | Read-only, write, privileged/admin? |
| **Duration** | Short-term (<30 days), medium-term (30–180 days), long-term (>180 days)? |

Based on risk assessment, require screening equivalent to organisational roles with similar access (per Screening Levels table). Document risk assessment and screening requirement in vendor contract.

---

## Terms and Conditions of Employment (A.6.2)

### Contractual Security Obligations

Information security obligations shall be included in all employment-related contracts:

- Employment contracts (employees).
- Contractor and consulting agreements.
- Vendor agreements (for on-site or access-holding personnel).
- Internship and apprenticeship agreements.

### Mandatory Contract Clauses

All employment contracts shall include the following information security clauses:

**Confidentiality and data protection**:

- Obligation to maintain confidentiality of organisational information.
- Compliance with data protection policies and applicable laws (nFADP, GDPR where applicable).
- Confidentiality obligations for trade secrets continue indefinitely per Swiss CO Art. 321a. Confidentiality for non-trade-secret Internal/Confidential information continues for 2 years post-termination.

**Acceptable use acknowledgment**:

- Agreement to comply with the Acceptable Use Policy.
- Acknowledgment of the organisation's right to monitor use of information systems per the Monitoring Activities Policy, which defines: what is monitored (e.g., system logs, network traffic — not content of private communications), why (security, compliance), limits (no monitoring of private device use), and employee notification procedure.
- Understanding of prohibited activities.

**Security training obligation**:

- Requirement to complete mandatory information security awareness training.
- Timeline: within 5 business days of start date and annually thereafter.
- New hire training shall cover: Acceptable Use Policy key requirements (authorised use, prohibited activities), information classification and handling rules, incident identification and reporting procedure, password and authentication requirements, physical security (badge use, visitor management, clean desk), and data protection obligations (confidentiality, nFADP/GDPR basics). Training delivered via [LMS platform] with completion tracked by HR. Certification required to provision system access.

**Incident reporting obligation**:

- Requirement to report security incidents and suspected breaches immediately.
- Obligation to cooperate with security investigations.

**Access rights and termination**:

- Access granted at the organisation's discretion and revocable at any time.
- Return of all organisational assets upon termination.
- Post-termination access prohibition.

**Disciplinary action**:

- Security policy violations are subject to disciplinary action per the severity framework.
- Serious violations may result in immediate termination and legal action.

### Additional Clauses for Sensitive Roles

**Privileged access roles**: Enhanced background check consent, conflict of interest declaration, ongoing monitoring acknowledgment.

**Roles with restricted data**: Special handling requirements, elevated breach notification obligations, regulatory awareness acknowledgment.

**Executive Management**: Leadership commitment statement, governance accountability, resource allocation responsibility.

### Access Revocation Upon Termination

Upon employee termination (voluntary or involuntary), the Line Manager shall initiate the termination workflow in [HR System] immediately. HR notifies IT Service Desk on the same business day. IT Service Desk:

- Disables all system accounts (Active Directory, SaaS applications, VPN) within 4 business hours of notification.
- Revokes physical access (badge, keys) immediately.
- Retrieves organisational assets (laptop, mobile, access cards) within 5 business days.

Termination checklist completed and filed in [HR System]. IT logs access revocation in [Ticketing System].

### Contract Execution Timing

Contracts shall be signed before access is granted:

- Employment contract (includes NDA clause) signed before the first day of work.
- Standalone NDA signed for contractors/consultants before system access or confidential data access.
- System access provisioning requests require evidence of signed NDA (verified by IT Service Desk via [HR System] before account creation).
- Acceptable Use Policy acknowledged before system access is provisioned.

### Acknowledgment Tracking

All acknowledgments (NDA, AUP, training completion) shall be collected with signature (physical or electronic), tracked in [HR System], and re-collected annually for critical policies. Acknowledgment compliance shall be reported quarterly to the ISMS Committee. Personnel who do not acknowledge critical policies within 30 days of communication shall have system access suspended until acknowledgment is completed. Line managers shall be notified at 21 days.

---

## Monitoring

Compliance with the policies and procedures of the information security management system shall be monitored via the Management Review Team, together with independent reviews by both internal and external audit on a periodic basis.

---

## Legal and Regulatory Obligations

The organisation takes its legal and regulatory obligations seriously. Requirements arising from Swiss nFADP (revDSG), the Swiss Code of Obligations, and other applicable regulations are recorded in the Legal and Contractual Requirements Register. This register shall be reviewed at least annually and updated when new regulations apply or existing regulations change materially.

---

## Training and Awareness

Policies shall be made readily and easily available to all employees and third-party users. A training and communication plan shall be in place to communicate the policies, processes, and concepts of information security. Training needs shall be identified per role, and relevant training requirements captured in the competency matrix.

---

## Continual Improvement of the Management System

The information security management system shall be continually improved. The organisation shall maintain a continual improvement process informed by audit findings, incident lessons learned, risk assessment outcomes, regulatory changes, and Management Review decisions.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Executive Management** | Ultimate accountability for policy framework and personnel security; approve Master Policy and risk appetite; allocate resources; review ISMS performance quarterly via Management Review |
| **CISO** | Policy framework maintenance; security role definition; screening requirements; contract security clauses; exception approval (medium risk); quarterly reporting to ISMS Committee |
| **DPO** | Review policies and screening for data protection compliance; independent reporting to Executive Management; contact point for FDPIC |
| **HR Manager** | Employment contract execution; screening operations; acknowledgment tracking; training record maintenance; joiner/mover/leaver process integration |
| **Legal/Compliance** | Review policies for legal compliance; contract clause enforceability; regulatory change monitoring |
| **Line Managers** | Ensure direct reports comply with policies; initiate joiner/mover/leaver processes; approve access requests; escalate non-completion |
| **All Personnel** | Comply with policies; complete training; maintain confidentiality; report security incidents immediately |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Policy inventory** listing all ISMS policies with ID, version, approval date, review date, and status | CISO | *Maintained continuously; reviewed annually; target: 100% currency* |
| 2 | **Policy acknowledgment records** (Master Policy, AUP, Code of Conduct) with signatures and dates | HR | *Annually; target: 95% acknowledgment rate within 30 days* |
| 3 | **Policy exception register** with business justification, compensating controls, and approval chain | CISO | *Maintained continuously; reviewed quarterly by ISMS Committee* |
| 4 | **Security role descriptions** documenting responsibilities, authority, qualifications, and performance metrics | HR / CISO | *Reviewed annually; retained for duration of role assignment + 3 years* |
| 5 | **RACI matrix** mapping ISO 27001 Annex A controls to security roles | CISO | *Reviewed annually; updated upon organisational change* |
| 6 | **Screening completion records** with: (a) screening request date, (b) screening completion date, (c) access provisioning date, (d) evidence that access was granted only after screening cleared. Consent forms and verification results retained. | HR | *Per event; retained for employment + 2 years; target: 100% access date ≥ screening completion date* |
| 7 | **Employment contracts** with information security clauses (NDA, AUP, training obligation, incident reporting) | HR / Legal | *Per hire; retained for employment duration + statutory retention period* |
| 8 | **Succession plans** for key security roles (CISO, Information Security Manager, DPO) | CISO | *Reviewed annually; tested annually via tabletop exercise or during planned leave (minimum 1-week CISO absence per year)* |
| 9 | **Policy violation log** with investigation findings, severity classification, and remediation actions | CISO / Security Team | *Per event; analysed quarterly for trends; retained 3 years* |
| 10 | **Third-party spot-check records** verifying vendor personnel screening and training compliance | CISO / Procurement | *Annually per critical vendor; retained 3 years* |
| 11 | **Quarterly Management Review meeting minutes** with ISMS performance, incident summary, risk changes, and executive decisions | CISO | *Quarterly* |
| 12 | **Competence verification records** for security roles (certifications, training, experience) at hire and annually | HR / CISO | *Per hire + annual review* |
| 13 | **New hire training completion records** with training content covered, completion date, and certification | HR | *Per hire; target: 100% within 5 business days* |
| 14 | **Termination access revocation logs** showing: (a) termination date, (b) HR notification timestamp, (c) account disable timestamp, (d) asset return confirmation | IT / HR | *Per termination; target: 100% accounts disabled within 4 hours* |
| 15 | **NDA execution records** with signature date and evidence of signature before access granted | HR / Legal | *Per hire; target: 100% signed before access granted* |
| 16 | **Vendor risk assessments** documenting data access, access level, duration, and screening requirements | Procurement / CISO | *Per vendor onboarding; reviewed annually* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, policy inventory reviews, acknowledgment tracking reports, screening completion audits, contract clause verification, role documentation currency checks, internal and external audits, and feedback to the policy owner.

Key metrics:

| Metric | Target |
|--------|--------|
| Policy review currency (% reviewed within cycle) | 95% |
| Policy acknowledgment rate (critical policies) | 95% |
| Screening completion before access granted | 100% |
| Contract execution before first day of access | 100% |
| NDA signing rate | 100% |
| Security training completion (within 30 days) | 95% |
| Role documentation reviewed within annual cycle | 100% |

## Exceptions

Any exception to this policy shall be approved and recorded per the Policy Exceptions process defined above (medium risk: 6 months renewable once; high risk: 3 months renewable with Executive approval). Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Violations shall be handled per the severity framework defined in this policy.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to employment law and data protection regulation (nFADP, GDPR), organisational structure changes, screening service provider capabilities, audit findings, lessons learned from personnel security incidents, and industry best practice developments.

---

# Areas of the ISO 27001 Standard Addressed

ISMS Governance and Secure Employment Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | **5.1 Policies for information security** |
| Clause 5.2 Policy | **5.2 Information security roles and responsibilities** |
| Clause 5.3 Organisational roles, responsibilities and authorities | 5.3 Segregation of duties |
| Clause 6.2 Information security objectives | 5.4 Management responsibilities |
| Clause 7.3 Awareness | 5.36 Compliance with policies, rules, and standards |
| Clause 7.5.3 Control of documented information | **6.1 Screening** |
| | **6.2 Terms and conditions of employment** |
| | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures for data security; Art. 6 — Proportionality and purpose limitation in data processing (applies to screening data) |
| Swiss CO (Code of Obligations) | Art. 328 — Employer's duty of care; Art. 328b — Employee data processing limited to suitability and necessity for employment; Art. 321a — Employee loyalty obligations |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 5, 32 — Security of processing; Art. 88 — Employment processing safeguards |
| ISO/IEC 27001:2022 | Annex A Controls 5.1, 5.2, 6.1, 6.2 |
| ISO/IEC 27002:2022 | Sections 5.1, 5.2, 6.1, 6.2 — Implementation guidance |
| NIST SP 800-53 Rev 5 | PS-1 (Policy and Procedures), PS-2 (Position Risk Designation), PS-3 (Personnel Screening), PS-6 (Access Agreements), PS-7 (External Personnel Security) |
| CIS Controls v8 | Control 14 (Security Awareness and Skills Training — personnel security baseline) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
