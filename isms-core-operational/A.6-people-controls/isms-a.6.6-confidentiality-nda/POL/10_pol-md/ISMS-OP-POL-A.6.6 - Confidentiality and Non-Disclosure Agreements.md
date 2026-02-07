**ISMS-OP-POL-A.6.6 — Confidentiality and Non-Disclosure Agreements**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Confidentiality and Non-Disclosure Agreements |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.6.6 |
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

- ISO/IEC 27001:2022 Control A.6.6 — Confidentiality or non-disclosure agreements
- ISO/IEC 27002:2022 Section 6.6 — Implementation guidance
- Swiss Code of Obligations Art. 321a (Employee duty of care and loyalty)
- Swiss Code of Obligations Art. 340–340c (Non-compete agreements)
- Swiss nFADP (revDSG) — Art. 8 (Data security), Art. 24 (Breach notification)

**Related Annex A Controls**:

| Control | Relationship to Confidentiality and Non-Disclosure Agreements |
|---------|--------------------------------------------------------------|
| A.5.1 Policies for information security | Policies that NDAs support and reinforce |
| A.5.10 Acceptable use of information and other associated assets | NDA obligations complement acceptable use rules |
| A.5.12–13 Information classification and labelling | Classification scheme defines what information requires NDA protection |
| A.5.19–23 Cloud services and supplier security | Vendor and supplier NDAs required before data sharing |
| A.5.34 Privacy and protection of PII | NDAs include privacy-specific provisions for personal data handlers |
| A.6.2 Terms and conditions of employment | NDAs incorporated into or accompany employment contracts |
| A.6.4–5 Disciplinary process and employment exit | Post-employment NDA obligations communicated and tracked at exit |
| A.6.3 Information security awareness and training | NDA obligations reinforced through security awareness training |

**Related Internal Policies**:

- Identity and Access Management Policy
- Acceptable Use and Return of Assets Policy
- Information Classification and Handling Policy
- Cloud Services and Supplier Security Policy
- Privacy and Protection of PII Policy
- Disciplinary Process and Employment Exit Policy

---

# Confidentiality and Non-Disclosure Agreements Policy

## Purpose

The purpose of this policy is to establish the organisation's requirements for confidentiality and non-disclosure agreements (NDAs) to protect information accessible by personnel and external parties. NDAs inform signatories of their legal obligation to manage and safeguard confidential information responsibly, providing a legally enforceable mechanism to prevent unauthorised disclosure.

This policy supports Swiss nFADP (revDSG) by implementing organisational measures appropriate to risk to protect personal data, including ensuring that all parties with access to personal data are bound by confidentiality obligations (Art. 8 — data security through technical and organisational measures). The policy also aligns with the employee duty of loyalty and secrecy under Swiss CO Art. 321a, which requires employees to safeguard the employer's legitimate interests and not to exploit or reveal confidential information, including manufacturing or trade secrets, both during and after employment. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

## Scope

This policy applies to:

- All employees (permanent, temporary, part-time, interns).
- All contractors, consultants, and agency workers.
- Vendors and suppliers with access to confidential information or systems.
- Partners in joint ventures, strategic alliances, or collaborative arrangements.
- Board members, advisors, and external auditors.
- Customers receiving access to confidential product or technical information.
- Visitors with escorted access to sensitive areas (data centres, engineering areas, executive boardrooms).

**Out of scope**:

- Public information with no confidentiality requirement.
- Information explicitly excluded from confidentiality by Executive Management.
- Regulatory disclosures required by law (e.g., mandatory reporting under nFADP Art. 24).

## Principle

The organisation shall require confidentiality or non-disclosure agreements from all persons with access to confidential information before access is granted. Agreements shall be legally enforceable, regularly reviewed, and maintained for the duration of the confidentiality obligation. Post-employment and post-contract obligations shall be clearly communicated and tracked to completion.

---

## NDA Requirements

### ISO Control Reference

> *"Confidentiality or non-disclosure agreements reflecting the organisation's needs for the protection of information should be identified, documented, regularly reviewed and signed by personnel and other relevant interested parties."*
> — ISO/IEC 27001:2022, Annex A Control 6.6

### Mandatory Agreements Before Access

No person shall be granted access to the organisation's confidential information, systems, or facilities without a valid, signed confidentiality or non-disclosure agreement in place. NDAs shall be executed before access is granted — not retrospectively.

**Limited pre-NDA access (exception process)**:

Where negotiation, proposal, or initial assessment requires access to confidential information before full NDA execution:

- **Permitted**: Oral preliminary discussions, high-level requirements (Internal classification or lower), publicly available information.
- **Prohibited**: Detailed specifications, customer data, source code, financial information, trade secrets.

**Procedure**:

1. Executive sponsor approves pre-NDA access with scope limitation (in writing).
2. Watermarked "Preliminary — NDA Required" version of documents provided.
3. NDA must be executed within **10 business days** of first confidential information disclosure.
4. If NDA not executed within 10 days: access revoked, return/destruction of preliminary materials required.

Logged in NDA Exception Register. Target: <5% of new relationships require pre-NDA access.

**Coverage targets**: The organisation shall achieve and maintain the following NDA coverage rates:

| Stakeholder Category | Target Coverage | Measurement Frequency |
|---------------------|-----------------|----------------------|
| Employees | 100% | Monthly |
| Contractors / Consultants | 100% | Monthly |
| Vendors with data access | 100% | Quarterly |
| Partners (active agreements) | 100% | Quarterly |
| Board members / Advisors | 100% | Upon appointment |
| Visitors (sensitive areas) | 100% of registered visits | Per visit |

**Coverage calculation methodology**:

Coverage is calculated as (parties with valid, signed NDA / parties requiring NDA per this policy) x 100. A coverage rate below target triggers immediate gap remediation per the Gap Remediation section of this policy.

| Category | Numerator | Denominator | Exclusions |
|----------|-----------|-------------|------------|
| **Employees** | Employees with valid, signed NDA on file in [HR System] | All active employees (status = Active or On Leave, excluding Terminated) | Employees with start date >5 business days in future (pre-hire) |
| **Contractors / Consultants** | Contractors with valid, signed NDA on file in [Contract Management System] | All contractors with active access (SSO login within last 60 days OR physical badge with current access) | Contractors whose engagement ended (access revoked) |
| **Vendors** | Vendors with valid, signed NDA | Vendors with active data access (processed data in last 90 days OR hold active credentials) | Vendors with no data access (delivery-only, logistics) |

Measured monthly. Methodology documented in NDA Coverage Procedure.

### Timing Requirements

NDAs shall be executed according to the following timelines:

| Party Type | Timing Requirement |
|------------|-------------------|
| **Employees** | Before or on the first day of employment; incorporated into or accompanying the employment contract |
| **Contractors / Consultants** | Before access to any systems, information, or facilities |
| **Vendors / Suppliers** | Before contract execution or any data sharing commences |
| **Partners** | Before confidential discussions commence |
| **Board members / Advisors** | Upon appointment, before access to strategic or governance information |
| **Visitors** | Before entering sensitive areas (see Visitor NDA Requirements below) |

### Visitor NDA Requirements

Visitor NDAs are required based on the sensitivity of the area visited:

| Area / Context | NDA Requirement | Form |
|---------------|-----------------|------|
| Data centre or server rooms | Mandatory | Visitor NDA (full) |
| Development or engineering areas | Mandatory | Visitor NDA (full) |
| Executive boardrooms (during sensitive meetings) | Mandatory | Visitor NDA (full) |
| General office areas (escorted) | Acknowledgment only | Visitor Confidentiality Acknowledgment |
| Reception / public areas | Not required | N/A |

**Visitor NDA execution procedure**:

**Pre-arrival** (preferred):

1. Meeting organiser sends visitor NDA via [DocuSign] when visit is scheduled (minimum 2 business days before visit).
2. Visitor signs electronically before arrival.
3. Reception verifies signed NDA in system before badge issuance.

**At arrival** (backup):

1. If no pre-signed NDA: Visitor reviews and signs at reception using tablet or printed form.
2. Estimated time: 5–10 minutes (reception provides brief waiting area).
3. If visitor refuses: No badge issued; meeting held in non-sensitive area (e.g., conference room without confidential materials), or visit cancelled.

**Emergency access** (rare):

- Executive sponsor can authorise sensitive area access before NDA signature in genuine emergency (equipment failure requiring urgent vendor repair).
- Visitor escorted 100% of time; no unattended access.
- NDA must be executed within **4 hours** of arrival or access terminated.
- Logged as exception.

**Target**: 80% of sensitive-area visitor NDAs signed pre-arrival.

Visitor Confidentiality Acknowledgments may be incorporated into standard visitor sign-in procedures.

### Legal Enforceability

All NDAs shall be legally enforceable in the organisation's operating jurisdictions. Legal Counsel shall review and approve all NDA templates. NDAs shall reference:

- The applicable governing law (per selection criteria below).
- The jurisdiction for dispute resolution.
- The organisation's information classification scheme.
- Obligations specific to classification levels.

**Governing law and jurisdiction selection**:

| Party Location | Governing Law | Jurisdiction | Notes |
|----------------|---------------|--------------|-------|
| **Switzerland-based parties** (default) | Swiss law | Courts of [Canton], Switzerland (organisation's primary location) | Standard for all domestic NDAs |
| **EU/EEA parties** | Swiss law with GDPR compliance rider | Swiss courts OR EU party's jurisdiction (mutual recognition under Lugano Convention) | Legal Counsel determines most appropriate |
| **UK parties** | UK law may be more appropriate (post-Brexit legal divergence) | Legal Counsel determines | Consider enforceability in UK courts |
| **US parties** | US state law (e.g., Delaware, New York) may be more enforceable in US courts | Arbitration clause recommended | Legal Counsel assessment required |
| **Other jurisdictions** | Case-by-case Legal Counsel assessment | Legal Counsel determines | Consider local NDA enforceability |

Non-standard governing law requires Legal Counsel approval. Governing law selection rationale documented in contract file.

---

## Template Requirements

### Standardised Templates

The organisation shall maintain six standardised NDA templates, one for each stakeholder category:

| # | Template | Target Audience | Typical Use |
|---|----------|-----------------|-------------|
| 1 | **Employment NDA** | Employees | Incorporated into employment contract |
| 2 | **Contractor NDA** | Contractors, consultants, agency workers | Executed before engagement |
| 3 | **Vendor / Supplier NDA** | Third-party service providers | Accompanies service agreement |
| 4 | **Mutual NDA** | Partners, joint ventures | Reciprocal confidentiality |
| 5 | **Customer NDA** | Customers receiving confidential information (see use cases below) | Before disclosure |
| 6 | **Visitor NDA** | Visitors to sensitive facilities | At visitor registration |

**Customer NDA use cases**:

A Customer NDA is required when:

- **Pre-sales technical disclosure**: Detailed product architecture, security controls, or source code review required for customer's vendor assessment.
- **Proof of concept (POC)**: Customer deploying trial version with access to pre-release features or confidential technical documentation.
- **Technical partnership**: Customer participating in beta programme, providing product feedback, or co-developing features.
- **Strategic customer**: Customer receiving financial information, product roadmap, or M&A-related disclosures.

A Customer NDA is **not typically required** for:

- **Standard product use**: Customer uses product per standard terms and conditions (confidentiality provisions in Terms of Service sufficient).
- **Customer data**: Customer owns their data; organisation is data processor bound by DPA, not NDA.

**Approval authority**: Sales Director (standard Customer NDA), Legal Counsel (non-standard terms).

### Template Content Requirements

All NDA templates shall include the following elements:

| # | Required Element | Description |
|---|------------------|-------------|
| 1 | **Definition of confidential information** | Clear description of what constitutes confidential information, aligned with the organisation's classification scheme |
| 2 | **Obligations of receiving party** | Duty to protect, restrict access, use only for permitted purposes |
| 3 | **Permitted and prohibited uses** | Specific uses authorised under the agreement; prohibited actions |
| 4 | **Permitted disclosures** | Need-to-know basis; compelled disclosure by law or regulation |
| 5 | **Duration of confidentiality obligations** | Active period plus post-termination period |
| 6 | **Return or destruction of information** | Obligation to return or certify destruction upon termination |
| 7 | **Consequences of breach** | Remedies available, including injunctive relief and damages |
| 8 | **Governing law and jurisdiction** | Swiss law (default); jurisdiction for dispute resolution |
| 9 | **Post-termination obligations** | Continuing obligations after the relationship ends, with specified durations |

### Template Review

NDA templates shall be reviewed:

- **Annually** by Legal Counsel as part of the scheduled review cycle.
- **Within 30 business days** of any triggered review event.

**Triggered review events**:

| Trigger Event | Review Scope | Responsible Party |
|--------------|--------------|-------------------|
| New regulation enacted (e.g., privacy law amendment) | All templates | Legal Counsel |
| Court ruling affecting NDA enforceability | Affected templates | Legal Counsel |
| Expansion to new jurisdiction | All templates for that jurisdiction | Legal Counsel |
| Acquisition or merger | All templates | Legal Counsel + HR |
| Security incident involving confidential data | Root cause templates | CISO + Legal Counsel |
| Failed NDA enforcement attempt | Specific template used | Legal Counsel |

Upon a trigger event, Legal Counsel shall initiate review within 5 business days and record the review requirement in the NDA Template Register maintained in [Contract Management System].

---

## Stakeholder-Specific Requirements

### Employees

Employment NDAs shall:

- Be incorporated into or accompany the employment contract.
- Cover all information classifications (Confidential, Internal, and above).
- Include post-termination obligations: minimum **2 years** for Confidential information; **indefinite** for trade secrets (aligned with Swiss CO Art. 321a, para. 4).
- Be reinforced through security awareness training (per A.6.3).
- Reference the employee's statutory duty of loyalty and secrecy under Swiss CO Art. 321a.

**Swiss CO Art. 321a alignment**: Swiss law imposes a statutory duty of loyalty on employees. During employment, employees must not exploit or reveal confidential information such as manufacturing or trade secrets. This duty of confidentiality continues after the end of employment to the extent required to safeguard the employer's legitimate interests. The Employment NDA reinforces and extends these statutory obligations with specific terms.

### Contractors and Consultants

Contractor NDAs shall:

- Be executed before any access is granted (no retroactive NDAs).
- Specify the scope of permitted access and information types.
- Include provisions requiring the contractor to impose equivalent confidentiality obligations on any subcontractors.
- Require return or certified destruction of all information upon engagement end.
- Include post-engagement obligations: minimum **2 years**.

### Vendors and Suppliers

Vendor NDAs shall:

- Be part of or accompany service agreements.
- Include data protection provisions per nFADP (and GDPR where applicable) where personal data is involved.
- Require notification of security incidents affecting the organisation's information.
- Include audit rights for confidentiality compliance verification.
- Specify post-contract obligations: minimum **3 years**.

**Data Processing Agreement (DPA) requirements**: When a vendor will process personal data on behalf of the organisation, the Vendor NDA template shall include or reference a DPA covering the following elements (per nFADP Art. 9, GDPR Art. 28):

- Subject matter, duration, nature, and purpose of processing.
- Type of personal data and categories of data subjects.
- Vendor obligations: process only on documented instructions; ensure confidentiality of personnel; implement appropriate technical and organisational security measures.
- Sub-processor authorisation and notification requirements.
- Data subject rights assistance (access, deletion, correction requests).
- Data breach notification to controller (organisation) without undue delay.
- Deletion or return of personal data upon contract end.
- Audit rights and vendor cooperation.
- International data transfer safeguards (if applicable — e.g., Standard Contractual Clauses for EEA data).

DPA may be integrated into the Vendor NDA or attached as Annex. Legal Counsel approval required for all DPAs.

### Partners

Mutual NDAs for partners shall:

- Provide reciprocal protection for both parties' confidential information.
- Define procedures for handling shared confidential information.
- Include dispute resolution mechanisms.
- Specify duration aligned with partnership term plus a post-termination period.

**Mutual NDA approval authority**:

- **Authority required**: Legal Counsel approval required for all mutual NDAs before signature (no delegation).
- **Review criteria**:
  - Reciprocal confidentiality obligations acceptable and enforceable.
  - Post-termination periods symmetric and reasonable (maximum 3 years absent compelling justification).
  - Our obligations not broader than theirs (e.g., they get 5 years, we give 2 years = approve; they get 2 years, we give 5 years = reject or renegotiate).
  - No unusual indemnity, limitation of liability, or IP assignment clauses (these belong in the commercial contract, not the NDA).
- **Approval timeline**: Legal Counsel reviews within 3 business days of request. Template negotiation expedited where possible to avoid delaying partnership discussions.
- **One-way NDAs** (we receive confidentiality, we don't give): Department Manager can approve with Legal notification.

### Board Members and Advisors

Director/Advisor NDAs shall:

- Cover strategic, governance, and financial information.
- Include extended post-tenure obligations: minimum **3 years**.
- Address insider trading restrictions where applicable under FMIA (Financial Market Infrastructure Act).

**Conflict of interest provisions for Directors and Advisors**:

- **Acknowledgment of potential conflicts**: Director acknowledges they may serve on other boards or have advisory relationships that could create confidentiality conflicts.
- **Conflict disclosure**: Director agrees to disclose potential conflicts to the Chair before receiving confidential information that might conflict.
- **Abstention**: Where conflict exists, Director may abstain from discussions and recuse from receiving specific confidential materials.
- **Primary duty**: In event of irreconcilable conflict, Director's duty to this organisation takes precedence unless otherwise agreed in writing.
- **Insider trading**: Where the organisation is publicly traded or considering a public offering, Director acknowledges insider trading restrictions under FMIA (Financial Market Infrastructure Act).

Conflict assessment shall be performed at Director onboarding and annually thereafter (Chair + Legal Counsel).

### Visitors

Visitor NDAs shall:

- Be brief and clear, suitable for execution at reception.
- Cover information observed or disclosed during the visit.
- Specify that photographs, recordings, and copying are prohibited in sensitive areas unless explicitly authorised.
- Include a defined confidentiality period: minimum **1 year** from the date of visit.

---

## Execution and Storage

### Signature Requirements

NDAs shall be:

- Signed by authorised representatives of all parties.
- Dated with the effective date clearly specified.
- Witnessed or notarised where required by applicable law.
- Executed using approved signature methods per the tiered requirements below.

**Acceptable signature methods by agreement type**:

| Risk Level | Applicability | Accepted Methods |
|------------|---------------|------------------|
| **High-value or high-risk** (>CHF 100,000 value, trade secret access) | Executive NDAs, strategic partner NDAs, trade secret access | Wet signature (original) OR qualified electronic signature (QES per Swiss ZertES) |
| **Standard** (most NDAs) | Employment, contractor, vendor, customer NDAs | Wet signature, OR advanced electronic signature (AES) via [DocuSign / Adobe Sign] with identity verification (email + SMS), OR simple electronic signature (SES) with dual-factor identity confirmation |
| **Low-risk** (visitor NDAs, short-term access) | Visitor NDAs, conference room access | Any electronic signature method OR wet signature |

Method selection documented in NDA execution log. Audit trail retained per signature method requirements.

### Secure Storage

Executed NDAs shall be:

- Stored securely in the designated repository:
  - Employee NDAs: [HR System].
  - Third-party NDAs (contractors, vendors, partners, customers): [Contract Management System].
  - Visitor NDAs: [Reception / Facilities Management System].
- Protected against unauthorised access, modification, or deletion.
- Retained per the following retention calculation:

**NDA retention period calculation**:

Retention starts from the date of last obligation end (latest of contract end date + post-termination period).

| Framework | Retention Duration |
|-----------|-------------------|
| **Swiss default** | 10 years from end of business relationship (OR Art. 958f for accounting records; by analogy for NDAs supporting contracts) |
| **nFADP minimum** | Period necessary to demonstrate compliance with data protection obligations (typically 3–7 years post-obligation end) |
| **Policy minimum** | 7 years from last obligation end date |

**Example**: Employment NDA with 2-year post-termination period. Employee terminates 1 Jan 2025 → last obligation end 1 Jan 2027 → retention until 1 Jan 2034 (7 years after last obligation end) = 9 years from termination date.

**Exception**: Trade secret NDAs (indefinite confidentiality) retained 10 years from employment end as safe harbour, or indefinitely if active enforcement risk exists (Legal Counsel determination).
- Retrievable for audit purposes within **2 business days** of request.

### NDA Register

The organisation shall maintain a register of all active NDAs. The register shall include:

| Attribute | Description |
|-----------|-------------|
| **Signatory name** | Individual or entity name |
| **Party type** | Employee / Contractor / Vendor / Partner / Board / Visitor |
| **NDA type** | Template used (Employment, Contractor, Vendor, Mutual, Customer, Visitor) |
| **Signature date** | Date NDA was executed |
| **Effective date** | Date NDA became effective |
| **Expiration date** | Date NDA expires (if applicable) |
| **Post-termination end date** | Date post-termination obligations expire |
| **Status** | Active / Expired / Pending Renewal |
| **Storage location** | System and reference number |

The NDA Register shall be maintained in [Contract Management System] and reconciled quarterly against the personnel directory and active vendor/partner lists.

### NDA-Before-Access Verification (SOC 2 CC6.6)

For each access grant (system account, data access, facility badge):

1. Requesting manager confirms NDA on file before submitting access request.
2. IAM team / HR system automatically checks NDA status before provisioning access.
3. If no NDA: Access request rejected with reason "NDA required" and notification to requester.
4. Override: Requires CISO approval with compensating controls (see Gap Remediation section).

**Audit trail**: Access provisioning system logs NDA verification check with timestamp and result (pass/fail). Quarterly audit samples 10% of new access grants to verify NDA preceded access.

---

## Periodic Review and Gap Remediation

### Review Frequency

| Review Type | Frequency | Owner |
|-------------|-----------|-------|
| Template adequacy review (per checklist below) | Annual | Legal Counsel |
| Coverage analysis (who has / should have NDAs) | Quarterly | HR / Contracts Manager |
| Expiration monitoring | Monthly | Information Security Team |
| Triggered review (regulatory change, incident) | As required | Legal Counsel |

### Review Scope

Periodic reviews shall assess:

- Template adequacy for current regulatory requirements (nFADP, GDPR where applicable).
- Coverage completeness: all required parties have valid, signed NDAs.
- Currency of signed agreements: no expired NDAs for ongoing relationships.
- Appropriateness of template used for each party type.
- Storage security and accessibility of executed agreements.

### NDA Template Adequacy Review Checklist

Annual review by Legal Counsel shall assess each template against the following criteria:

**Regulatory compliance**:
- Current with Swiss CO Art. 321a (employee duty of loyalty)
- Current with Swiss CO Art. 340–340c (non-compete, if applicable)
- Current with nFADP (data security obligations)
- Current with GDPR (if applicable — data processor agreements)
- Current with any new applicable regulations (checked in last 12 months)

**Legal enforceability**:
- Governing law and jurisdiction clearly stated
- Confidential information definition aligned with current classification scheme
- Permitted/prohibited uses clearly defined
- Post-termination obligations clearly stated with durations
- Return/destruction obligations specified
- Remedy provisions (injunctive relief, damages) included
- Severability clause included (if one provision unenforceable, others remain)

**Operational effectiveness**:
- Template language clear and understandable (plain language where possible)
- No provisions that would delay execution (e.g., notarisation unless required)
- No provisions inconsistent with organisational practice
- Template usable without extensive modification for most signatories

Review documented in NDA Template Review Report. Template marked "Current — [Date]" upon passing review. Failed review triggers remediation within 30 days.

### NDA Relevance Review (SOC 2 CC1.4)

**Annual NDA relevance review** (sample-based):

**For active employment NDAs**:
- Review sample of employees (10% per year, rotating) to confirm:
  - NDA template used is appropriate for current role (e.g., employee promoted to executive role may need updated NDA with enhanced provisions).
  - Post-termination obligations align with current access level (e.g., former developer now in sales may have trade secret obligations no longer relevant).
- Action if misalignment: Offer supplemental NDA or updated terms (requires voluntary employee signature).

**For vendor NDAs**:
- Annual review of active vendors confirms:
  - NDA scope matches current data access (vendor scope reduced = confirm NDA still covers remaining access).
  - Post-contract obligations still appropriate (e.g., 3-year post-contract for vendor with 1-year contract = reasonable).

Documented in Annual NDA Relevance Review Report to CISO.

### Gap Remediation Timelines

| Gap Type | Remediation Timeline |
|----------|---------------------|
| Missing NDA — critical access (Confidential data, privileged systems) | **5 business days** |
| Missing NDA — standard access | **30 business days** |
| Expired NDA — ongoing relationship | **30 business days** |
| Template inadequacy identified | **60 business days** |

### Gap Remediation Escalation

When remediation timelines cannot be met, the following escalation shall apply:

| Escalation Trigger | Action Required | Authority |
|-------------------|-----------------|-----------|
| At 50% of timeline | Status report to responsible manager | Department Manager |
| At 100% of timeline (deadline) | Formal escalation with remediation plan | CISO notification |
| 10 business days past deadline | Access suspension decision required | CISO approval |
| 20 business days past deadline | Mandatory access suspension | Executive Management notification |

**Compensating controls**: If access cannot be immediately suspended pending NDA execution, documented compensating controls shall be implemented within **2 business days** of the deadline and reviewed weekly until the NDA is executed.

| Tier | Applicability | Compensating Controls |
|------|---------------|----------------------|
| **Tier 1 — High-risk access** (Confidential data, privileged systems) | Persons with access to Confidential or trade secret information | Revoke write/modify permissions, limit to read-only where feasible. Real-time alerts on all data downloads, exports, or transfers (threshold: >10 MB or any Confidential classification file). Manager or security team member reviews access logs daily; results documented. Maximum **10 business days**; reviewed weekly |
| **Tier 2 — Standard access** | Persons with access to Internal classification only | Weekly access log review by manager. Remove access to Confidential classification data. Maximum **20 business days** |

Documented in Exception Register. CISO reviews all Tier 1 compensating controls weekly.

---

## Post-Employment Obligations

### Continuing Obligations

Confidentiality obligations shall survive the termination of employment, contract, or business relationship. Post-termination obligations shall be communicated to the departing individual in writing before or on the last working day, as part of the exit process (per A.6.4–5).

### Post-Termination Periods

| Information Type | Minimum Post-Termination Period |
|------------------|--------------------------------|
| **Trade secrets** | Indefinite (aligned with Swiss CO Art. 321a, para. 4) |
| **Highly Confidential** | 5 years |
| **Confidential** | 2 years |
| **Internal** | 1 year |

### Post-Termination Tracking

The organisation shall maintain a Post-Termination Obligation Register for all departed personnel and ended third-party relationships. The register shall include:

| Tracking Element | Description |
|-----------------|-------------|
| Individual / entity name | Former employee, contractor, vendor, etc. |
| Former role | Position held or engagement type |
| Termination date | Date of departure or contract end |
| Information types accessed | Highest classification level accessed |
| Obligation end date(s) | By information type, per the post-termination periods above |
| Return / destruction confirmation | Date organisational information was returned or certified destroyed |
| Risk level | Based on access scope and classification level |

The register shall be:

- Updated upon each termination or contract end (owner: HR for employees; Contracts Manager for third parties).
- Monitored monthly for upcoming obligation expirations (owner: Information Security Team).
- Reviewed quarterly for high-risk individuals with broad access to Confidential or trade secret information (owner: CISO).
- Reviewed annually for trade secret holders, whose obligations are indefinite (owner: Legal Counsel).

Upon obligation expiration, the record shall be archived in historical compliance records, retained per document retention policy (minimum **7 years** from expiration), and removed from active monitoring.

### Post-Termination Obligation Monitoring

**Active monitoring** (obligations not yet expired):

| Risk Level | Monitoring Frequency | Monitoring Activities |
|------------|---------------------|---------------------|
| **High-risk individuals** (Confidential/trade secret access, privileged roles) | Quarterly | Check LinkedIn profile for competitor employment, public statements, patent filings. Action if concern: Legal Counsel assessment within 5 business days |
| **Standard risk** | Annual | Review on obligation anniversary |

**Expiration handling**:

- **30 days before expiration**: Legal Counsel reviews whether extension or legal hold is required.
- **Upon expiration**: Archive record (no notification to ex-employee — obligation ends by operation of NDA terms, not by company notification).
- **Trade secret obligations** (indefinite): Annual review indefinitely, or until trade secret becomes public knowledge.

**Suspected breach response** (immediate):

1. **Evidence preservation** (within 4 hours):
   - IT: Preserve suspect's access logs, email records (if still accessible), file download history.
   - Screenshots of public evidence (LinkedIn posts, competitor website, patent filings).
   - Witness statements from reporter.
   - Any physical evidence (documents, devices) secured.
2. **Initial assessment** (within 24 hours):
   - CISO + Legal Counsel review evidence.
   - Determine: credible breach (proceed) or insufficient evidence (monitor).
3. **Investigation** (if credible):
   - Legal Counsel leads investigation; external counsel engaged for litigation risk assessment.
   - Timeline: Investigation plan within 5 business days, completion within 30 days unless complexity requires extension.
4. **Enforcement decision**:
   - Legal Counsel recommends: cease-and-desist letter, negotiated resolution, or litigation.
   - Executive Management approves enforcement action.
   - If litigation: external litigation counsel engaged.

Chain of custody maintained for all evidence. Investigation documented in Confidentiality Breach Case File (attorney-client privileged where possible). Enforcement actions tracked in Confidentiality Breach Register.

### Non-Compete Agreements

Where applicable, non-compete clauses in employment contracts are governed by Swiss CO Art. 340–340c:

- **Art. 340** — Non-compete agreements must be in writing and are valid only where the employee had knowledge of the employer's clientele, manufacturing secrets, or business secrets, and the use of this knowledge could cause significant harm.
- **Art. 340a** — Non-compete clauses must be appropriately limited as to place, time, and type of business, so as not to unfairly jeopardise the employee's economic future. The maximum duration is 3 years except in special circumstances.
- **Art. 340b** — Employees who violate non-compete clauses are liable for damages; contractual penalties may be agreed but may be reduced by the court if excessive.
- **Art. 340c** — The non-compete clause lapses if the employer no longer has a substantial interest in maintaining it, or if the employer terminated the contract without the employee giving justified reason.

Non-compete agreements are separate from and additional to NDAs. An NDA governs confidentiality; a non-compete governs competitive activity. Both may apply concurrently.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|------------------|
| **Executive Management** | Approve policy; ensure resources for NDA programme; accept residual risks |
| **CISO** | Own policy; oversee NDA programme; approve exceptions; report compliance metrics |
| **Legal Counsel** | Review and approve all NDA templates; advise on legal requirements; support enforcement actions |
| **HR Manager** | Manage employee NDAs; ensure onboarding NDA completion; track post-employment obligations; conduct exit NDA reminders |
| **Contracts / Procurement Manager** | Manage vendor, supplier, and partner NDAs; ensure contract inclusion; track expirations and renewals |
| **Department Managers** | Ensure team compliance; identify NDA requirements for new relationships; escalate gaps |
| **Information Security Team** | Monitor compliance; conduct periodic coverage reviews; maintain NDA Register and tracking systems |
| **All Personnel** | Comply with NDA obligations; report potential breaches of confidentiality; protect confidential information |

### NDA Awareness and Communication (SOC 2 CC1.5)

**New hire onboarding**:

- HR conducts 15-minute NDA briefing covering: what confidential information is, examples (customer data, source code, financials), obligations during and after employment, consequences of breach.
- Briefing recorded in onboarding checklist.
- Employee acknowledges understanding (separate from NDA signature).

**Annual reinforcement**:

- Security awareness training includes confidentiality module (30 minutes) covering: NDA refresher, recent confidentiality incidents (anonymised case studies), reporting suspected breaches.
- Completion tracked in training system.

**Post-termination reminder**:

- Exit interview includes NDA reminder (see A.6.4–5 policy).
- Departing employee receives written summary of continuing obligations.

**Target**: 100% new hire NDA briefing completion within 5 business days of start date.

**Escalation path**:

- Missing employee NDA: HR Manager -> CISO -> Legal Counsel -> Executive Management.
- Missing third-party NDA: Contracts Manager -> CISO -> Legal Counsel -> Executive Management.
- Suspected NDA breach: CISO -> Legal Counsel -> Executive Management.
- Overdue gap remediation (>10 business days past deadline): CISO -> Executive Management.

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **NDA Template Register** showing all approved templates with legal review dates and version history | Legal Counsel | *Updated per review event; audited annually* |
| 2 | **Active NDA Register** with signatory tracking, dates, types, and status for all parties | HR / Contracts Manager | *Updated per event; reconciled quarterly against personnel and vendor lists* |
| 3 | **Employee NDA completion records** (100% target) correlated with onboarding dates | HR Manager | *Monthly; target: NDA signed before or on first day* |
| 4 | **Contractor and vendor NDA completion records** (100% target) correlated with access grant dates | Contracts Manager | *Monthly; target: NDA signed before access* |
| 5 | **Coverage analysis reports** showing NDA coverage rates by stakeholder category | Information Security Team | *Quarterly; presented at management review* |
| 6 | **Expiration monitoring reports** with renewal tracking and overdue items | Information Security Team | *Monthly; target: 0 expired NDAs for active relationships* |
| 7 | **Post-termination obligation register** with tracking of departed personnel and obligation end dates | HR / Contracts Manager | *Updated per termination; reviewed monthly* |
| 8 | **Gap remediation records** showing identified gaps, remediation actions, and closure dates | CISO | *Per gap; reviewed quarterly* |
| 9 | **Exception register** with documented justifications, approvals, and compensating controls | CISO | *Per exception; reported to Executive Management quarterly* |
| 10 | **Visitor NDA records** for sensitive area visits, correlated with visitor logs | Facilities Management | *Per visit; audited quarterly* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, NDA coverage rate monitoring, expiration tracking, onboarding and offboarding checklist audits, access review correlation (access granted vs. NDA on file), internal and external audits, and feedback to the policy owner.

**Governance metrics**:

| Metric | Target | Review Frequency |
|--------|--------|------------------|
| **Employee NDA coverage rate** | 100% | Monthly |
| **Contractor NDA coverage rate** | 100% | Monthly |
| **Vendor NDA coverage rate** | 100% | Quarterly |
| **NDAs expiring within 30 days** (active relationships) | <5% of active | Monthly |
| **Overdue NDA renewals** | 0 | Monthly |
| **Average time to execute NDA** (new employees) | <2 business days | Monthly |
| **Average time to execute NDA** (contractors) | <3 business days | Monthly |
| **Gap remediation within timeline** | >95% | Monthly |
| **Active exceptions** | Trending down | Quarterly |
| **Post-termination obligations tracked** | 100% of terminations | Monthly |
| **Template review currency** | 100% within 12 months | Quarterly |

Metrics shall be reported to the CISO monthly and to the Management Review Team quarterly.

## Exceptions

Any exception to this policy shall be approved and recorded by the CISO, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team quarterly.

**Exception types**:

- **Timing exception** — NDA executed after access is granted (e.g., urgent business need).
- **Template exception** — Non-standard NDA terms required (e.g., counterparty's template).
- **Coverage exception** — Party not required to sign (e.g., public information only).

**Exception authority**:

| Exception Type | Approval Authority |
|----------------|-------------------|
| Timing (< 5 days delay) | Department Manager with Legal notification |
| Timing (> 5 days delay) | CISO with Legal review |
| Template variation | Legal Counsel |
| Coverage exception | CISO with Legal review |

**Exception lifecycle**:

- **0–30 days**: Exception active with compensating controls; monthly review by approver.
- **30 days**: Mandatory status review by CISO + approver (renewed justification required; why not resolved?).
- **60 days**: Escalation to next approval level (Department Manager → CISO → Executive Management).
- **90 days**: Executive Management review required for continuation.
- **>90 days**: Automatic access suspension unless Executive Management grants explicit waiver (rare; documented in board-level exception register).
- All active exceptions reported to Executive Management quarterly.
- Expired exceptions without resolution escalated to the CISO within **5 business days**.

**Target**: 80% of exceptions resolved within 30 days. Exceptions >60 days reported in quarterly Management Review.

## Non-Compliance

Non-compliance with this policy may result in:

| Violation Type | Severity | Response |
|---------------|----------|----------|
| Missing NDA (new hire / contractor) | High | Access blocked until NDA executed; NDA required within 5 business days |
| Expired NDA (active relationship) | Medium | 30-day renewal window; access review at day 30 |
| Refused to sign NDA | Critical | Immediate access denial; relationship termination initiated |
| Suspected NDA breach | Critical | Immediate investigation; potential access suspension; Legal Counsel engaged |
| Wrong template used | Low | Correction within 15 business days; risk assessment by Legal Counsel |

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Managers who fail to ensure NDA compliance for their teams may also be subject to disciplinary action.

For third parties, non-compliance may result in contract termination and legal action for breach of confidentiality.

Under Swiss CO Art. 321a, employees who exploit or reveal confidential information — including manufacturing or trade secrets — during or after employment may be held liable for damages. In cases of deliberate or grossly negligent breach, immediate dismissal under Swiss CO Art. 337 may be warranted.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to Swiss employment and data protection law (nFADP, Swiss CO), GDPR developments where applicable, lessons learned from NDA enforcement actions or failures, audit findings, changes to the organisation's business relationships or jurisdictions, and industry best practices for confidentiality agreement management.

Nonconformities related to this policy (e.g., missing NDAs, expired agreements, gap remediation failures, enforcement difficulties) shall be recorded and managed through the corrective action process (ISO 27001 Clause 10.2) with root cause analysis and tracked remediation.

---

# Areas of the ISO 27001 Standard Addressed

Confidentiality and Non-Disclosure Agreements Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 7.5 Documented information | 5.10 Acceptable use of information and other associated assets |
| Clause 8.1 Operational planning and control | 5.12 Classification of information |
| Clause 10.2 Nonconformity and corrective action | 6.2 Terms and conditions of employment |
| | **6.6 Confidentiality or non-disclosure agreements** |
| | 6.5 Responsibilities after termination or change of employment |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss CO Art. 321a | Employee duty of care and loyalty — statutory obligation to protect trade secrets and confidential information during and after employment |
| Swiss CO Art. 340–340c | Non-compete agreements — validity requirements (written form, legitimate interest), scope limitations (place, time, business type), maximum 3 years, compensation, and lapse conditions |
| Swiss nFADP (revDSG) | Art. 8 — Data security through technical and organisational measures (NDAs as organisational measure); Art. 24 — Data breach notification to FDPIC |
| EU GDPR (where applicable) | Art. 28 — Processor agreements include confidentiality obligations; Art. 32 — Security of processing (confidentiality as security objective); Art. 38 — DPO bound by secrecy |
| ISO/IEC 27001:2022 | Annex A Control 6.6 |
| ISO/IEC 27002:2022 | Section 6.6 — Implementation guidance: agreement elements, review requirements, legal enforceability |
| NIST SP 800-53 Rev 5 | PS-6 (Access Agreements), PS-7 (External Personnel Security) |
| CIS Controls v8 | Control 6 (Access Control Management — Safeguard 6.1: Establish an Access Granting Process) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
