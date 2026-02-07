**ISMS-OP-POL-A.6.4-5 — Disciplinary Process and Employment Exit**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Disciplinary Process and Employment Exit |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.6.4-5 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Human Resources Officer (CHRO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / CHRO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.6.4 — Disciplinary process
- ISO/IEC 27001:2022 Control A.6.5 — Responsibilities after termination or change of employment
- ISO/IEC 27002:2022 Sections 6.4, 6.5 — Implementation guidance
- Swiss Code of Obligations Art. 328 (Duty of care), Art. 337 (Termination for cause), Art. 337d (Job abandonment)
- Swiss nFADP (revDSG) — Data subject rights and access revocation

**Related Annex A Controls**:

| Control | Relationship to Disciplinary Process and Employment Exit |
|---------|----------------------------------------------------------|
| A.5.1 Policies for information security | Policies that the disciplinary process enforces compliance with |
| A.5.10 Acceptable use of information and other associated assets | Violations of acceptable use trigger disciplinary actions |
| A.5.11 Return of assets | Asset return requirements at employment exit |
| A.5.15-16-18 Identity and access management | Access revocation execution for leavers and movers |
| A.5.24-28 Incident management lifecycle | Security violations may constitute incidents requiring parallel investigation |
| A.6.3 Information security awareness, education, and training | Training adequacy considered as mitigating factor in disciplinary decisions |
| A.6.6 Confidentiality and non-disclosure agreements | NDA obligations continue post-employment |
| A.6.7-8 Remote working and event reporting | Remote access revocation at exit; event reporting may trigger disciplinary |
| A.8.2-3-5 Authentication and privileged access | Privileged access revocation priority at termination |

**Related Internal Policies**:

- Access Control Policy
- Acceptable Use and Return of Assets Policy
- Incident Management Policy
- Information Classification and Handling Policy
- Confidentiality and Non-Disclosure Agreements Policy
- Privacy and Protection of PII Policy
- Pre-Employment Screening Policy (background check results referenced for repeat offenders or trust-sensitive roles)

---

# Disciplinary Process and Employment Exit Policy

## Purpose

The purpose of this policy is to establish the organisation's formal disciplinary process for information security policy violations and to define the requirements for secure termination or change of employment, including access revocation, asset recovery, and post-employment obligations.

This policy supports Swiss nFADP (revDSG) by implementing technical and organisational measures to ensure that personal data access is revoked promptly upon termination or change of employment, and that data protection obligations are communicated and enforced throughout and beyond the employment lifecycle. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

**Combined control approach**: Controls A.6.4 (Disciplinary Process) and A.6.5 (Responsibilities After Termination or Change of Employment) are implemented together because security-related disciplinary actions often precede termination, and both require coordinated HR-Security processes with shared access revocation, asset return, and documentation requirements.

## Scope

This policy applies to:

- All employees, contractors, temporary workers, and interns.
- All termination types: voluntary resignation, termination for cause, immediate dismissal, retirement, contract end, role change (mover), and job abandonment.
- All security violation types: policy breaches, acceptable use violations, data handling failures, and deliberate misconduct.
- All asset types: physical, logical, information, and intellectual property.

**Out of scope**:

- Pre-employment screening (see A.5.1-2-6.1-2 — ISMS Governance and Secure Employment).
- Ongoing security training requirements (see A.6.3 — Information Security Awareness and Training).
- Third-party or vendor termination procedures (see A.5.19-23 — Cloud Services and Supplier Security).

## Principle

The organisation shall maintain a formal, documented disciplinary process that is fair, proportionate, and aligned with Swiss employment law. The process shall deter information security violations, protect the rights of individuals, and ensure appropriate consequences for policy breaches. Upon termination or change of employment, the organisation shall revoke access promptly, recover assets, and communicate continuing obligations to departing personnel.

---

## Disciplinary Framework (A.6.4)

### ISO Control Reference

> *A disciplinary process should be formalised and communicated to take actions against personnel and other relevant interested parties who have committed an information security policy violation.*
> — ISO/IEC 27001:2022, Annex A Control 6.4

### Principles

The disciplinary process shall be:

- **Fair and consistent** — applied equally across all personnel regardless of seniority or role.
- **Proportionate** — the response shall match the severity of the violation and its consequences.
- **Aligned with employment law** — compliant with Swiss CO Art. 328 (employer's duty of care) and applicable cantonal employment regulations.
- **Documented** — all proceedings recorded with appropriate evidence and maintained confidentially.
- **Progressive** — graduated response where circumstances allow, from verbal warning through to dismissal.
- **Timely** — violations investigated and addressed without unreasonable delay.

The disciplinary process is both **preventive** (deterring negligence by communicating consequences) and **corrective** (addressing violations to prevent recurrence).

### Violation Categories

| Category | Examples | Typical Response |
|----------|----------|------------------|
| **Minor / Inadvertent** | Accidental policy breach (e.g., sending internal data to wrong recipient), first-time minor violation, failing to lock screen | Verbal warning, additional training, documented coaching |
| **Moderate** | Repeated minor violations after warning, negligent data handling, sharing credentials with a colleague, unapproved software installation | Written warning, mandatory remedial training, increased monitoring |
| **Serious** | Deliberate policy violation, significant data exposure, circumventing security controls, accessing data without authorisation | Final written warning, suspension pending investigation, termination |
| **Gross Misconduct** | Malicious data theft or exfiltration, sabotage of systems, selling confidential information, criminal activity | Immediate dismissal (Art. 337 CO), legal action, regulatory notification |

**Aggravating factors**: Deliberate intent, concealment of violation, abuse of privileged access, prior warnings on record, harm to data subjects.

**Mitigating factors**: Self-reporting, inadvertent error, insufficient training provided, unclear policy guidance, prompt corrective action by the individual.

**Role-based severity adjustment**:

For violations involving access abuse, data handling, or credential sharing, apply role risk multiplier:
- **Standard user**: Base severity.
- **Privileged user** (admin, developer, DB admin): +1 severity level (moderate becomes serious).
- **Executive/senior management**: +1 severity level (reputational risk).
- **Security team member**: +2 severity levels (violates trust foundation).

*Example*: Credential sharing by standard user = Moderate (written warning). Same by DB admin = Serious (final warning or termination).

**Self-reporting of violations**:

Employees who self-report policy violations before discovery by management/security team receive:
- Reduced severity classification (one level reduction: serious becomes moderate) where appropriate.
- Consideration for non-disciplinary remediation (training, process improvement) for first-time inadvertent violations.
- Documentation of good faith cooperation.

**Self-report procedure**: Report to manager, HR, or CISO (anonymous channel available via [Ethics Hotline]). Self-report must occur within 24 hours of violation discovery by employee.

**Exclusions**: Gross misconduct (data theft, sabotage) not eligible for severity reduction through self-reporting.

### Investigation Procedure

The following five-step procedure shall be followed for all information security violations:

**Step 1 — Report**: The violation is reported to HR and the Information Security Team. Reports may come from automated monitoring, management observation, colleague reporting, audit findings, or self-reporting.

**Step 2 — Preliminary Assessment**: HR and the Information Security Team jointly assess the severity of the reported violation. The assessment determines whether a formal investigation is warranted and whether interim measures (e.g., access suspension) are required.

**Preliminary assessment timeline by severity**:
- **Suspected gross misconduct** (data theft, sabotage, criminal activity): Immediate assessment (within 2 hours), access suspended pending investigation.
- **Serious violations**: Assessment within 4 business hours.
- **Moderate violations**: Assessment within 1 business day.
- **Minor violations**: Assessment within 2 business days.

Severity initially determined by reporter (manager, security team, HR). Over-triaging acceptable; under-triaging creates risk.

**Step 3 — Evidence Collection**: Relevant evidence is gathered and preserved, including:
- System logs, audit trails, and access records (from [SIEM] or [Identity Provider]).
- Email records and file access logs.
- Witness statements.
- Physical evidence (documents, devices).
- Previous warnings or disciplinary records.

Evidence shall be collected in a manner that respects the individual's rights under Swiss CO Art. 328 and nFADP. The chain of custody shall be documented.

**Step 4 — Investigation**: A formal investigation is conducted, including interviews with the individual concerned, witnesses, and relevant managers. The individual shall be informed of the nature of the allegations and given the opportunity to respond. For serious or gross misconduct cases, Legal Counsel shall be consulted.

**Step 5 — Findings Documented**: Investigation findings are documented, including the evidence reviewed, the individual's response, the conclusion reached, and the recommended disciplinary action. The investigation report is stored in the confidential HR case file with access restricted to authorised personnel.

### Decision and Action

Following the investigation:

1. **Severity determination** — The violation is categorised per the violation categories table above.
2. **Mitigating and aggravating factors** — All relevant circumstances are considered, including whether the individual received adequate training (per A.6.3), whether this is a first or repeat offence, and the individual's overall conduct record.
3. **Action selection** — The appropriate disciplinary action is selected from the range defined for the violation category.
4. **Communication** — The decision is communicated to the individual in writing, with clear explanation of the reasons and the right to appeal.
5. **Implementation** — The action is implemented, including any access restrictions, additional training, or employment changes.
6. **Follow-up** — Where the individual remains employed, follow-up monitoring is applied for a defined period to verify compliance.

### Due Process

The following due process requirements shall be observed in all disciplinary proceedings, in compliance with Swiss CO Art. 328 (employer's duty of care):

- The individual shall be **informed of the specific allegations** in writing before any disciplinary hearing.
- The individual shall be given a **reasonable opportunity to respond** to the allegations, including time to prepare.
- The individual shall have the **right to representation** at disciplinary meetings (e.g., a colleague, trade union representative, or legal advisor, as permitted under applicable employment law).
- An **appeals process** shall be available:
  - **Eligibility**: Moderate, Serious, or Gross Misconduct decisions (minor violations not appealable).
  - **Filing deadline**: 10 business days from receipt of written disciplinary decision.
  - **Appeal form**: Written appeal with grounds submitted to CHRO.
  - **Review body**: Panel of 2-3 persons not involved in original investigation (e.g., CHRO + external HR consultant, or Senior Manager + DPO).
  - **Timeline**: Appeal heard within 15 business days of filing; decision within 5 business days of hearing.
  - **Scope**: Review of process fairness, proportionality of action, consideration of new evidence.
  - **Outcome**: Uphold, reduce penalty, or overturn. Decision is final (no further internal appeal).
  - **Documentation**: Appeal decision documented and placed in HR file.
- All documentation shall be maintained **confidentially**, with access restricted to those with a legitimate need to know.
- The individual's **personal data** processed during the investigation shall be handled in accordance with nFADP and the organisation's Privacy and Protection of PII Policy.

### Security Team Involvement

The Information Security Team shall be involved in disciplinary matters when:

- The violation involves an information security policy breach or suspected data breach.
- Technical investigation is required (log analysis, forensic examination, access review).
- Access revocation, account suspension, or enhanced monitoring is recommended as an interim or final measure.
- There is potential for an ongoing security risk (e.g., insider threat indicators).
- Legal or regulatory notification may be required (e.g., personal data breach notification under nFADP Art. 24).

### Escalation and Notification

| Violation Severity | Internal Notification | External Notification |
|-------------------|----------------------|----------------------|
| **Minor** | Line Manager, HR | None |
| **Moderate** | HR, CISO | None typically |
| **Serious** | HR, CISO, Legal Counsel | Regulators if personal data breach (nFADP Art. 24) |
| **Gross Misconduct** | HR, CISO, Legal Counsel, Executive Management | Police (if criminal), regulators (nFADP Art. 24, GDPR Art. 33 where applicable) |

**Regulatory notification**: Where a disciplinary matter involves a confirmed or suspected personal data breach, the organisation shall assess notification obligations:

- **Risk assessment factors**: Volume of records affected, sensitivity of data (sensitive personal data per nFADP Art. 5(c) triggers higher urgency), whether data was encrypted, likelihood of harm to data subjects, whether the breach was contained.
- **nFADP Art. 24**: Notification to the FDPIC as soon as possible where the breach is likely to result in a high risk to the personality or fundamental rights of data subjects. No fixed deadline, but "as soon as possible" interpreted as within 72 hours by FDPIC guidance.
- **GDPR Art. 33** (where applicable): Notification to supervisory authority within 72 hours of becoming aware. Document reasons for delay if exceeded.
- **Data subject notification**: Required under nFADP Art. 24(4) where necessary for the protection of the data subject or requested by the FDPIC. Under GDPR Art. 34, required where high risk to rights and freedoms.
- **Notification thresholds**: Any breach involving 1+ records of sensitive personal data (health, biometric, racial/ethnic origin) or 100+ records of standard personal data triggers mandatory FDPIC assessment. CISO + DPO make determination within 24 hours of breach confirmation.

---

## Employment Exit (A.6.5)

### ISO Control Reference

> *Information security responsibilities and duties that remain valid after termination or change of employment should be defined, enforced and communicated to relevant personnel and other interested parties.*
> — ISO/IEC 27001:2022, Annex A Control 6.5

### Access Revocation Timeline

Access shall be revoked according to the following timelines based on termination type:

| Termination Type | Access Revocation Timing | Trigger |
|------------------|--------------------------|---------|
| **Immediate dismissal** (gross misconduct, Art. 337 CO) | Within **1 hour** of the dismissal decision | HR records termination in [HR System]; IT offboarding ticket raised immediately |
| **Termination for cause** | **Same business day**, before notification where possible | HR records termination; IT offboarding ticket raised |
| **Voluntary resignation** | **Last working day**, end of shift | HR records leave date; IT offboarding scheduled |
| **Retirement** | **Last working day** | HR records retirement date; IT offboarding scheduled |
| **Contract end** | **Contract end date** | HR records contract end; IT offboarding scheduled |
| **Role change — privilege escalation** (standard to admin) | New access granted within **2 business days** after approval | Manager notifies HR and IT of role change |
| **Role change — privilege reduction** (admin to standard) | Elevated access revoked **same business day** (within 4 hours) | Manager notifies HR and IT of role change |
| **Role change — lateral move** (same privilege level) | Access adjusted within **2 business days** | Manager notifies HR and IT of role change |
| **Role change — trust-impacted** (disciplinary, PIP, security concern) | Immediate revocation per "Immediate dismissal" timeline | HR and CISO notification |
| **Job abandonment** (Art. 337d CO) | Within **1 hour** of abandonment determination | HR determines abandonment; IT offboarding ticket raised |

### Immediate Dismissal Authorisation (Art. 337 CO)

Before executing immediate dismissal, the following procedural safeguards shall be observed:

- **Authorisation required**: CHRO + Legal Counsel (confirms good cause per CO Art. 337).
- **Timeline**: Decision and access revocation within same business day (delay undermines "immediate" requirement under Swiss law).
- **Documentation**: Written dismissal letter prepared before or immediately after notification, stating "immediate dismissal for good cause" (specific reasons provided upon employee request per CO Art. 337 para 2).
- **Access revocation**: Executed within 1 hour of authorisation, ideally before employee notification where feasible (reduces sabotage risk).
- **Post-revocation**: HR verifies written documentation complete within 2 hours.

**Good cause examples** (CO Art. 337): theft, fraud, serious breach of duty, violence, refusal to work, gross negligence causing significant damage. Minor violations not sufficient even if repeated.

**SLA trigger**: The access revocation timer starts when the termination decision is recorded in [HR System] and the IT offboarding request is submitted through [ITSM Tool].

**Termination notification protocol**:
- **HR System**: Termination recorded in [HR System] triggers automatic notification to IT Service Desk and IAM Team.
- **Email notification**: Automated email sent to [ITServiceDesk@], [IAM@], [CISO@] within 5 minutes of HR System entry.
- **Backup notification**: For immediate dismissals, HR phones IT Service Desk (emergency hotline: [number]) to initiate verbal notification before system entry.
- **Acknowledgment**: IT Service Desk acknowledges receipt and creates offboarding ticket within 15 minutes.

**Compensating controls when SLA cannot be met**: If full revocation across all systems cannot be completed within the SLA, the following compensating controls shall be applied **immediately** while full revocation is completed:

| Compensating Control | Action | Timeline |
|---------------------|--------|----------|
| **IdP disable** | User account disabled in [Identity Provider] (blocks SSO to all integrated applications) | Within 15 minutes |
| **VPN disable** | VPN access credential revoked | Within 15 minutes |
| **Badge disable** | Physical access badge deactivated | Within 30 minutes |
| **Email disable** | Email account suspended (incoming redirected to manager or shared mailbox) | Within 30 minutes |

A nonconformity or exception record shall be created for any SLA breach, with root cause analysis and remediation tracked to closure per the corrective action process.

### Job Abandonment Determination (Art. 337d CO)

**Abandonment criteria** (per Swiss CO Art. 337d):
- Employee absent without authorisation for 3+ consecutive working days.
- No response to manager contact attempts (phone, email, emergency contact).
- No acceptable explanation (medical emergency, force majeure excluded).

**Abandonment procedure**:
1. **Day 1-2 absence**: Manager attempts contact (3 attempts over 2 days, documented).
2. **Day 3**: HR notified; emergency contact attempted.
3. **Day 3 afternoon**: If no response, HR escalates to CHRO + Legal Counsel.
4. **Abandonment determination**: CHRO makes final determination with Legal review.
5. **Access revocation**: Immediate (per 1-hour SLA) upon determination.
6. **Written notification**: Registered letter sent to last known address confirming termination and asset return requirement.
7. **Compensation claim**: Finance initiates 1/4 monthly salary claim (30-day deadline per CO Art. 337d).

**False positive prevention**: Medical emergencies, accidents, and force majeure verified before abandonment determination finalised.

### Access Revocation Scope

All access types shall be addressed during the offboarding process:

| Access Type | Revocation Requirement |
|-------------|----------------------|
| **Physical access** | Badge disabled, keys returned, biometric enrolment removed. **Physical-logical coordination**: Physical access revocation shall be coordinated with logical access revocation to prevent scenarios where an individual retains badge access after logical accounts are disabled (or vice versa). Both revocation types shall be initiated from the same offboarding ticket and confirmed complete before sign-off. |
| **Logical access** | All accounts disabled: directory services, email, business applications, VPN, cloud platforms |
| **Remote access** | VPN credentials revoked, remote desktop sessions terminated, MDM profile removed |
| **Third-party access** | Vendor portal accounts disabled, partner system credentials revoked |
| **Delegated access** | Shared mailbox access removed, shared account passwords rotated, API keys revoked |
| **Data access** | File share permissions removed, database access revoked, cloud storage permissions removed |

**Privileged access revocation priority sequence**:

Where the departing individual holds privileged access, revocation shall follow this priority order:

| Priority | Access Type | Target Timeline | Rationale |
|----------|------------|-----------------|-----------|
| **P1 — Immediate** | Domain admin, root/sudo, cloud admin (AWS root, Azure Global Admin), database admin, security tool admin | Within 15 minutes of termination decision | Highest blast radius; can compromise entire infrastructure |
| **P2 — Urgent** | Application admin, CI/CD pipeline access, source code write access, backup system access | Within 1 hour | Can modify production systems or exfiltrate IP |
| **P3 — Standard** | Standard user accounts, email, VPN, badge, file shares | Per termination type SLA (see Access Revocation Timeline) | Standard access with limited blast radius |

For immediate dismissals and termination for cause: P1 and P2 revoked before or concurrent with employee notification where operationally feasible.

**Automated offboarding checklist process**:

1. **Checklist generation**: Upon termination recording in [HR System], the offboarding checklist is auto-generated from the authoritative application and service inventory, listing every system in which the departing individual holds an account.
2. **Assignment**: Checklist assigned to IT Operations via [ITSM Tool] with SLA based on termination type.
3. **Per-system verification**: Each system revocation is individually confirmed by the operator (checkbox + timestamp). Automated verification preferred where [Identity Provider] provides API-based account status check.
4. **Incomplete checklist escalation**: If any system remains unrevoked at SLA expiry, [ITSM Tool] auto-escalates to IAM Team Lead and CISO.
5. **Completion sign-off**: IT Operations Manager signs off completed checklist. Checklist retained as evidence (see Evidence table).
6. **Audit trail**: Checklist completion timestamp, operator name, and per-system revocation timestamps recorded in [ITSM Tool] for SOC 2 audit sampling.

### Asset Return

The organisation shall recover all organisational assets upon termination or change of employment.

**Physical assets to be returned**:

- Laptops, desktop computers, monitors, and peripherals.
- Mobile devices (phones, tablets).
- Storage media (USB drives, external hard drives).
- Access badges, office keys, security tokens, and smart cards.
- Printed documents, files, and any physical records.
- Company credit cards.

**Logical assets to be addressed**:

- Licensed software removed from personal devices (where BYOD was authorised).
- Organisational data on personal devices verified as deleted.
- Shared account passwords rotated per the following tiered timeline:
  - **Immediate dismissal / termination for cause**: All shared accounts the individual had knowledge of rotated within 1 hour (concurrent with individual account revocation).
  - **Voluntary resignation / retirement / contract end**: Shared account passwords rotated on last working day, after exit interview.
  - **Service accounts with shared credentials**: Rotated within 4 hours of termination decision for privileged service accounts; within 24 hours for standard service accounts.
  - **Shared environment credentials** (Wi-Fi PSK, door codes, alarm codes): Rotated within 24 hours for immediate dismissals; within 5 business days for planned departures.
  - All rotations documented in offboarding record with account name, rotation timestamp, and operator.
- Authentication tokens and software certificates revoked.

**Asset return process** (6-step):

1. **Inventory**: IT generates a list of all assets assigned to the departing individual from the asset register.
2. **Notification**: The departing individual is provided with the asset list and a return appointment date.
3. **Collection**: Assets are returned to IT at the scheduled appointment (or shipped with tracked delivery for remote workers).
4. **Verification**: IT verifies all returned assets against the inventory. Condition is documented.
5. **Gap resolution**: Missing or damaged assets are recorded. Missing assets are escalated to the line manager and HR. Where assets cannot be recovered, a write-off is processed per the exception process.
6. **Clearance**: IT and HR sign off the asset return form. Clearance is recorded in [HR System] and [ITSM Tool].

**Target**: Assets recovered within **5 business days** of the last working day (>95% recovery rate).

**Unreturned asset enforcement** (per Swiss CO Art. 339a):

Where assets are not returned within the 5-business-day target:

1. **Day 6**: IT Operations sends formal written reminder to the individual (email + registered letter) specifying outstanding items and 5-business-day deadline.
2. **Day 11**: HR escalates to line manager. Second written reminder sent with reference to contractual obligation and potential salary deduction.
3. **Day 16**: HR + Legal Counsel issue formal demand letter referencing CO Art. 339a (mutual return of property) with 10-day final deadline.
4. **Day 26**: If still outstanding, Legal Counsel assesses recovery options: salary offset against final payment (permitted under CO Art. 323b for agreed deductions), civil claim, or write-off with documented risk acceptance.
5. **Write-off**: CISO approves write-off only after confirming: remote wipe executed (if applicable), device encryption confirmed (if applicable), and residual risk documented in exception register.

**Remote worker asset return**: Shipped via tracked courier at organisation expense. Courier arranged by IT Operations with pre-paid shipping label sent to individual. If not shipped within 5 business days of receipt of shipping label, escalation follows steps 1-5 above.

### Post-Employment Obligations

Continuing obligations shall be communicated to the departing individual in writing before or on the last working day:

**Confidentiality**:

- NDA obligations continue per the terms of the signed agreement (see A.6.6 — Confidentiality and Non-Disclosure Agreements). NDA duration is risk-based by information classification:
  - **Trade secrets and proprietary algorithms**: Indefinite (per Swiss CO Art. 321a).
  - **Confidential information** (client data, financial data, security architecture): 24 months post-departure.
  - **Internal information** (internal processes, organisational data): 12 months post-departure.
  - **Client/contract-specific information**: Per client contract terms (may exceed standard periods).
- Trade secrets and proprietary information remain protected **indefinitely** under Swiss CO Art. 321a (duty of loyalty) and applicable trade secret law.
- Client and customer information remains confidential.
- Information classified as Confidential or Restricted at the time of departure remains subject to handling restrictions.

**Return and destruction of information**:

- All organisational information in the individual's possession shall be returned or certified as destroyed.
- Personal copies of organisational data are prohibited.
- The individual shall confirm in writing that no organisational data has been retained on personal devices, personal cloud storage, or personal email accounts.
- Verification of data return or deletion shall use the following lawful, risk-proportionate methods:
  - **Self-certification**: The individual completes a statutory declaration confirming deletion of all organisational data from personal devices, accounts, and storage. This is the baseline for all departures.
  - **Technical verification (company devices)**: IT performs automated scan of returned company devices to verify no organisational data remains. Results documented in offboarding record.
  - **Technical verification (BYOD with MDM)**: Where the individual used personal devices enrolled in [MDM], the organisation verifies MDM-initiated selective wipe completion before MDM disenrolment.
  - **Forensic verification**: Only where there is documented evidence of data exfiltration risk (e.g., DLP alerts, investigation findings). Requires Legal Counsel approval before initiation. Limited to company-owned devices and MDM-enrolled devices. Personal devices not subject to forensic inspection without the individual's written consent and Legal Counsel guidance.
  - **No forced inspection of personal devices**: The organisation shall not compel inspection of personal devices without the individual's consent. Where consent is refused and risk is assessed as high, Legal Counsel shall advise on available remedies under Swiss law.
- All work product created during employment belongs to the organisation.

**Non-compete and non-solicitation**: Where applicable, non-compete or non-solicitation clauses in the employment contract continue per their terms, subject to Swiss CO Art. 340-340c requirements (written form, reasonable scope, compensation where required).

### Exit Interview

A security-focused exit interview shall be conducted for all departing personnel. The interview shall cover:

1. **Reminder of continuing confidentiality obligations** — The individual is reminded of their NDA and any other post-employment obligations.
2. **Acknowledgment of NDA terms** — The individual confirms understanding and acceptance of continuing confidentiality requirements. Acknowledgment is documented and signed.
3. **Confirmation of data return or deletion** — The individual confirms all organisational data has been returned or deleted from personal devices and accounts.
4. **Identification of outstanding matters** — Any unresolved security concerns, access issues, or handover items are identified and assigned to the appropriate owner.
5. **Final documentation** — The exit interview form is completed and signed by both parties. A copy is retained in the HR file.

Exit interviews shall be conducted by HR with input from the Information Security Team where the departing individual had access to Confidential or Restricted data, held privileged system access, or is departing under disciplinary circumstances.

**Exit interview timing requirements**:

| Termination Type | Interview Timing | Notes |
|------------------|------------------|-------|
| **Voluntary resignation** | During notice period, minimum 3 business days before last day | Allows time to address outstanding items |
| **Termination for cause** | On last working day, before departure | Combined with asset return appointment |
| **Immediate dismissal** | Within 2 business days of dismissal, via phone/video if in-person not feasible | Individual may refuse; refusal documented |
| **Retirement** | During final month of employment | May include extended handover discussion |
| **Contract end** | Within 5 business days before contract end date | Scheduled at contract renewal decision point |
| **Job abandonment** | Written exit questionnaire sent via registered post | Individual unlikely to attend; documented as "not completed — abandonment" |

**Target**: Exit interviews completed for **100%** of departing personnel (excluding job abandonment where individual is uncontactable).

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|------------------|
| **CHRO / HR** | Disciplinary process ownership; exit process coordination; employment law compliance; exit interview conduct; documentation retention |
| **CISO** | Security violation assessment; access revocation verification; forensic support; regulatory notification assessment; policy ownership |
| **Legal Counsel** | Employment law compliance advice; disciplinary appeal support; NDA enforcement; regulatory notification guidance |
| **Line Managers** | Initiate disciplinary referrals; coordinate handover; verify asset return; confirm access removal for role changes |
| **IT Operations** | Access revocation execution; asset recovery and verification; technical offboarding checklist completion |
| **IAM Team** | Account disablement across all systems; access audit for completeness; orphaned account monitoring |
| **All Personnel** | Report violations; comply with exit procedures; return assets; honour post-employment obligations |

**Escalation path**:

- Disciplinary matters: Line Manager -> HR -> CISO (if security-related) -> Legal Counsel -> Executive Management.
- Exit process issues: HR -> IT Operations -> CISO.
- Overdue asset returns (>10 business days): IT Operations -> HR -> Legal Counsel.

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Disciplinary case records** (anonymised) showing investigation process, due process compliance, and outcomes. **Audit readiness**: Each case file shall contain a structured summary (case ID, violation category, investigation dates, due process steps completed, outcome, appeal status) suitable for SOC 2 / ISO 27001 audit sampling without requiring access to full confidential HR file. | HR | *Per case; retained per legal requirements; audited annually* |
| 2 | **Access revocation logs** with timestamps showing termination date vs. revocation date per system | IAM Team / IT Operations | *Per termination; reviewed monthly; target: 100% within SLA* |
| 3 | **Asset return records** with sign-off documentation and inventory reconciliation | IT Operations | *Per termination; reviewed quarterly; target: >95% within 5 days* |
| 4 | **Exit interview records** showing completion, NDA acknowledgment, and data return confirmation | HR | *Per termination; completion rate tracked monthly; target: 100%* |
| 5 | **Orphaned account reports** from periodic access reconciliation | IAM Team | *Monthly reconciliation; target: 0 orphaned accounts from leavers* |

**Monthly Orphaned Account Reconciliation**:

The IAM Team shall perform a monthly reconciliation to detect and remediate orphaned accounts:

1. **Source comparison**: Cross-reference active accounts in [Identity Provider] and all integrated applications against the HR active employee roster.
2. **Detection**: Any account belonging to an individual not on the active roster (terminated, contract ended, abandoned) is flagged as potentially orphaned.
3. **Verification**: IAM Team verifies flagged accounts against offboarding records. Accounts with completed offboarding but still active = confirmed orphan (remediate immediately). Accounts with no offboarding record = process failure (escalate to HR).
4. **Remediation**: Confirmed orphaned accounts disabled within 24 hours of detection. Root cause documented (e.g., system missed in offboarding checklist, manual process failure, new application not integrated with IdP).
5. **Reporting**: Monthly orphan count reported to CISO. Trend tracked quarter-over-quarter. Target: 0 orphaned accounts. Any orphan detected = nonconformity logged.
6. **Systemic remediation**: Where the same root cause produces orphans in consecutive months, corrective action required (e.g., add system to automated offboarding, integrate application with IdP).
| 6 | **Post-employment obligation acknowledgments** (signed NDA reminders, data return confirmations) | HR | *Per termination; retained for NDA duration + 2 years* |
| 7 | **Offboarding checklist completion records** (per-system verification of access revocation) | IT Operations | *Per termination; retained 3 years* |
| 8 | **Exception register entries** for SLA breaches, asset write-offs, and process deviations | CISO / HR | *Per exception; reviewed quarterly* |
| 9 | **Training records** for managers on disciplinary procedures and exit processes | HR | *Annual; target: 100% of people managers trained* |
| 10 | **Quarterly exit compliance audit** results (sample-based review of completed exits) | Internal Audit / HR | *Quarterly; presented at management review* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, access revocation timeliness metrics, asset recovery rates, exit interview completion rates, orphaned account monitoring, disciplinary case review, internal and external audits, and feedback to the policy owner.

**Governance metrics**:

| Metric | Target | Review Frequency |
|--------|--------|------------------|
| **Access revoked within SLA** (per termination type) | 100% | Monthly |
| **Assets recovered within 5 business days** | >95% | Quarterly |
| **Exit interviews completed** | 100% | Monthly |
| **Orphaned accounts from leavers** | 0 | Monthly |
| **Outstanding asset returns >30 days** | 0 | Monthly |
| **Disciplinary cases with documented due process** | 100% | Annually |
| **Post-employment NDA acknowledgments obtained** | 100% | Per termination |

Metrics shall be reported to the CISO monthly and to the Management Review Team quarterly.

## Exceptions

Any exception to this policy shall be approved and recorded by the CISO and CHRO jointly, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team.

**Permitted exceptions**:

- Accelerated exit with garden leave and immediate access revocation.
- Extended access for a documented business need (time-limited, maximum 10 business days, with compensating controls).
- Asset write-off for lost or damaged items after documented recovery attempts.

**Not permissible**:

- Permanent exceptions to access revocation timelines.
- Exceptions without compensating controls.
- Waiver of post-employment confidentiality obligations.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Managers who fail to follow the required exit procedures (e.g., delayed offboarding notification, incomplete asset recovery) may also be subject to disciplinary action.

Under Swiss CO Art. 337, gross misconduct involving information security violations (e.g., data theft, sabotage, deliberate breach of confidentiality) may constitute good cause for immediate dismissal without notice. Less serious but repeated violations may justify termination for cause following documented warnings per Art. 337 requirements.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to Swiss employment law, regulatory developments (nFADP, GDPR), lessons learned from disciplinary cases and exit process failures, audit findings, changes to the organisation's technology landscape affecting offboarding procedures, and industry best practices for secure personnel management.

Nonconformities related to this policy (e.g., delayed access revocation, unreturned assets, incomplete exit processes, orphaned accounts) shall be recorded and managed through the corrective action process (ISO 27001 Clause 10.2) with root cause analysis and tracked remediation.

---

# Areas of the ISO 27001 Standard Addressed

Disciplinary Process and Employment Exit Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 5.3 Organisational roles, responsibilities and authorities | 5.10 Acceptable use of information and other associated assets |
| Clause 7.3 Awareness | 5.11 Return of assets |
| Clause 8.1 Operational planning and control | 6.2 Terms and conditions of employment |
| Clause 10.2 Nonconformity and corrective action | **6.4 Disciplinary process** |
| | **6.5 Responsibilities after termination or change of employment** |
| | 6.6 Confidentiality or non-disclosure agreements |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss CO Art. 328 | Employer's duty of care — fair treatment in disciplinary proceedings, protection of employee personality rights |
| Swiss CO Art. 337 | Termination for cause (fristlose Kuendigung) — good cause requirement for immediate dismissal, written justification on request |
| Swiss CO Art. 337d | Job abandonment — employer's right to compensation (1/4 monthly salary), 30-day claim period |
| Swiss CO Art. 321a | Employee's duty of loyalty — obligation to protect trade secrets, continues post-employment |
| Swiss CO Art. 340-340c | Non-compete clauses — validity requirements, scope limitations, compensation |
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures (access revocation as security measure); Art. 24 — Data breach notification to FDPIC |
| EU GDPR (where applicable) | Art. 32 — Security of processing (access control measures at termination); Art. 33 — Breach notification within 72 hours |
| ISO/IEC 27001:2022 | Annex A Controls 6.4, 6.5 |
| ISO/IEC 27002:2022 | Sections 6.4, 6.5 — Implementation guidance |
| NIST SP 800-53 Rev 5 | PS-4 (Personnel Termination), PS-5 (Personnel Transfer), PS-8 (Personnel Sanctions) |
| CIS Controls v8 | Control 6 (Access Control Management — Safeguard 6.2: Establish an Access Revoking Process) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
