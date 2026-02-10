<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.31:operational:OP-POL:a.5.31 -->
**ISMS-OP-POL-A.5.31 — Legal, Statutory, Regulatory and Contractual Requirements**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Legal, Statutory, Regulatory and Contractual Requirements |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.31 |
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

- ISO/IEC 27001:2022 Control A.5.31 — Legal, statutory, regulatory and contractual requirements
- ISO/IEC 27002:2022 Section 5.31 — Implementation guidance

**Related Annex A Controls**:

| Control | Relationship to Legal and Regulatory Compliance |
|---------|--------------------------------------------------|
| A.5.1 Policies for information security | Top-level policy framework reflecting legal obligations |
| A.5.9 Inventory of information and assets | Asset inventory supports identification of regulated data |
| A.5.12-13 Classification and labelling | Classification scheme reflects regulatory sensitivity levels |
| A.5.19-23 Supplier relationships | Supplier contracts include regulatory pass-through obligations |
| A.5.24-28 Incident management | Breach notification obligations under nFADP and GDPR |
| A.5.32-33 Information protection and records | Intellectual property and records retention obligations |
| A.5.34 Privacy and PII | Data protection requirements under nFADP and GDPR |
| A.5.35-36 Independent review and compliance | Compliance review and audit against legal requirements |
| A.8.24 Use of cryptography | Cryptographic controls aligned with regulatory requirements |

**Related Internal Policies**:

- Privacy and Protection of PII Policy (ISMS-OP-POL-A.5.34)
- Information Protection and Records Management Policy (ISMS-OP-POL-A.5.32-33)
- Incident Management Policy (ISMS-OP-POL-A.5.24-28)
- Independent Review and Compliance Policy (ISMS-OP-POL-A.5.35-36)
- Cloud Services and Supplier Security Policy (ISMS-OP-POL-A.5.19-23)

---

# Legal, Statutory, Regulatory and Contractual Requirements Policy

## Purpose

The purpose of this policy is to ensure that the organisation identifies, documents, and maintains compliance with all legal, statutory, regulatory, and contractual requirements relevant to information security.

This policy supports Swiss nFADP (revDSG) by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data). Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply. Other laws may apply depending on operations (e.g., Swiss Code of Obligations, industry-specific regulations).

This policy implements ISO 27001:2022 Annex A Control A.5.31:

> **Control A.5.31**: Legal, statutory, regulatory and contractual requirements relevant to information security and the organisation's approach to meet these requirements should be identified, documented and kept up to date.

## Scope

This policy applies to:

- All employees, contractors, and third-party users.
- All information systems, data processing activities, and business operations.
- All legal, statutory, regulatory, and contractual requirements related to information security, data protection, and privacy.
- All jurisdictions in which the organisation operates, stores data, or serves customers.

## Principle

The organisation shall take a proactive, systematic approach to identifying and complying with applicable laws and regulations. Compliance shall not be left to ad-hoc awareness or individual judgement. A documented regulatory register shall be maintained as the authoritative record of all applicable requirements, and compliance shall be monitored, reviewed, and demonstrated through evidence.

---

## Regulatory Identification and Applicability

### Identifying Applicable Requirements

The organisation shall maintain a systematic process for identifying legal, statutory, regulatory, and contractual requirements relevant to information security. This process shall be initiated:

**Periodically:**

- **Annual comprehensive review** — full scan of the regulatory landscape and validation of all entries in the Regulatory Register. Performed in Q4 (October–November) to align with the annual Management Review cycle and allow remediation planning for the following year. The review completion date shall be documented in the Regulatory Register.
- **Quarterly environmental scan** (recommended) — focused review of regulatory developments in key jurisdictions and accumulation of monitoring alerts.

**Upon trigger events:**

- Entry into a new geographic market or jurisdiction.
- Launch of new services or products, or processing of new data categories.
- Acquisition of customers in regulated industries (e.g., financial services, healthcare).
- Mergers, acquisitions, or organisational restructuring.
- Execution of new customer or supplier contracts containing compliance requirements.
- Pursuit of new certifications (e.g., ISO 27001, SOC 2).
- Enactment of new laws or regulations in jurisdictions where the organisation operates.
- Receipt of regulatory inquiries or enforcement actions in the organisation's sector.
- Internal risk assessments identifying potential regulatory exposure.

### Sources for Regulatory Intelligence

The organisation shall utilise the following sources to identify potentially applicable regulations, listed in order of authority:

**Source hierarchy (highest authority first):**

1. **Primary legislation** — Federal and cantonal laws (nFADP, CO, GDPR where applicable).
2. **Implementing ordinances** — Regulations and ordinances providing detailed requirements (DSV).
3. **Regulatory authority guidance** — FDPIC guidance, EU supervisory authority opinions, FINMA circulars.
4. **Contractual obligations** — Customer and supplier compliance requirements.
5. **Certification standards** — ISO 27001, SOC 2, PCI DSS.
6. **Industry best practice frameworks** — NIST CSF, CIS Controls, ISO 27002 (informational).

Where sources conflict, higher-authority sources take precedence. Conflicts between equal-level sources (e.g., nFADP vs. GDPR) shall be resolved by legal counsel.

**Specific sources:

- **Government legal databases** — Official repositories (e.g., Fedlex for Swiss federal law, EUR-Lex for EU law).
- **Legal counsel** — In-house or external legal advisors, with jurisdiction-specific expertise where required.
- **Industry associations** — Trade groups, IAPP, ISACA, and sector-specific bodies that publish regulatory updates.
- **Customer and supplier channels** — Compliance clauses in contracts, security questionnaires, and audit findings.
- **Professional services** — Audit firms, compliance consultants, and regulatory monitoring services.
- **Peer networks** — Compliance officer forums, information sharing groups, and professional communities.

### Applicability Assessment

For each potentially applicable regulation, the organisation shall assess applicability across three dimensions:

**Geographic scope** — Does the organisation have a presence, customers, data subjects, or data processing activities in the jurisdiction? Does the regulation have extraterritorial application?

**Operational scope** — Do the organisation's services, industry sectors, data types, or operational activities fall within the regulation's scope?

**Contractual scope** — Do customer contracts, supplier agreements, or certification requirements mandate compliance?

If a regulation is clearly relevant across any dimension, or if applicability is uncertain, it shall be added to the Regulatory Register with an appropriate tier classification.

### Three-Tier Classification

Each applicable regulation shall be classified into one of three tiers:

| Tier | Definition | Treatment |
|------|------------|-----------|
| **Tier 1 — Mandatory** | Legal obligation, enforceable contractual requirement, or certification requirement. Non-compliance results in fines, sanctions, or loss of business. | Full compliance required. Inclusion approved by CISO (or Compliance Officer with CISO endorsement); escalated to Executive Management where the regulation imposes material financial risk or requires significant resource commitment. Annual review minimum. Continuous evidence collection. |
| **Tier 2 — Conditional** | Potential future applicability (e.g., market expansion plans), voluntary adoption for strategic advantage, or uncertain applicability pending legal clarification. | Monitoring and readiness. Gap analysis to understand compliance effort. Annual or biennial review. |
| **Tier 3 — Informational** | No compliance obligation. Used for guidance, benchmarking, or best practice reference. | Reference for control design. No formal compliance reporting. Biennial review or as needed. |

**Tier mobility:** Regulations may move between tiers as circumstances change (e.g., Tier 2 becomes Tier 1 when the organisation enters a new jurisdiction). Tier changes require reassessment and appropriate approval.

**Default position:** Where applicability is uncertain after assessment, the organisation shall default to a higher tier (Tier 1 over Tier 2, Tier 2 over Tier 3) to reduce the risk of non-compliance.

### Regulatory Register

The organisation shall maintain a Regulatory Register documenting all applicable requirements. This register is the authoritative source for regulatory compliance obligations.

**Minimum fields per entry:**

| Field | Description |
|-------|-------------|
| **Register ID** | Unique identifier (e.g., REG-001) |
| **Regulation name** | Full name and common abbreviation |
| **Jurisdiction** | Country, canton, or multi-jurisdictional |
| **Issuing authority** | Legislative body or regulatory agency |
| **Effective date** | Date from which the regulation applies |
| **Tier** | 1 (Mandatory), 2 (Conditional), or 3 (Informational) |
| **Applicability rationale** | Brief justification for inclusion and tier assignment |
| **Key requirements summary** | High-level summary of obligations relevant to the organisation |
| **Responsible party** | Role accountable for monitoring compliance |
| **Last review date** | Date of most recent review |
| **Next review date** | Scheduled next review |

**Example entries:**

| ID | Regulation | Jurisdiction | Tier | Responsible |
|----|------------|--------------|------|-------------|
| REG-001 | Swiss nFADP (revDSG) | Switzerland | 1 | Compliance Officer |
| REG-002 | Swiss DSV (Data Protection Ordinance) | Switzerland | 1 | Compliance Officer |
| REG-003 | Swiss CO Art. 328/328b (Employee Data) | Switzerland | 1 | HR / Legal |
| REG-004 | Swiss CO Art. 957–958f (Record-Keeping) | Switzerland | 1 | Finance / Legal |
| REG-005 | EU GDPR | EU/EEA | 1* | Compliance Officer |
| REG-006 | ISO/IEC 27001:2022 | International | 1 | ISMS Manager |
| REG-007 | FINMA Circular (if applicable) | Switzerland | 2** | Compliance Officer |
| REG-008 | PCI DSS v4.0 (if applicable) | International | 2** | ISMS Manager |
| REG-009 | NIST Cybersecurity Framework 2.0 | International | 3 | ISMS Manager |
| REG-010 | CIS Controls v8 | International | 3 | ISMS Manager |

\* Tier 1 where the organisation processes data of EU/EEA individuals; otherwise Tier 2.
\** Tier 2 unless contractual or operational requirements elevate to Tier 1.

---

## Swiss Regulatory Requirements

### Swiss Federal Act on Data Protection (nFADP / revDSG)

The Swiss nFADP, effective 1 September 2023, is the primary data protection legislation governing the organisation's processing of personal data. The organisation shall comply with the following key requirements:

#### Data Protection Principles (Art. 6 nFADP)

Personal data shall be:

- **Processed lawfully and in good faith** — Processing shall be conducted transparently, with a clear and documented purpose.
- **Collected for specified purposes** — Data shall be collected for specific, stated purposes and shall not be further processed in a manner incompatible with those purposes.
- **Proportionate** — Only data that is adequate, relevant, and limited to what is necessary for the stated purpose shall be collected and processed.
- **Accurate** — Personal data shall be accurate, and every reasonable step shall be taken to ensure that inaccurate data is rectified or erased without delay.
- **Not retained longer than necessary** — Data shall be retained only for as long as necessary for the processing purpose, or as required by law. It shall then be destroyed or anonymised.
- **Processed securely** — Appropriate technical and organisational measures shall be implemented to protect personal data against unauthorised processing, accidental loss, or destruction (Art. 8 nFADP).

#### Legal Basis for Processing

Under Swiss nFADP, personal data may be processed provided that data protection principles are respected (Art. 6 nFADP). Unlike GDPR, a specific legal basis is not required for each processing activity unless processing involves sensitive personal data, high-risk profiling, or where consent is otherwise required by law.

Where the organisation also processes data of EU/EEA individuals, a valid legal basis under GDPR Article 6 shall be identified and documented for each processing activity.

#### Sensitive Personal Data (Art. 5(c) nFADP)

The nFADP defines sensitive personal data as requiring particular protection. This includes:

- Religious, philosophical, political, or trade union opinions or activities.
- Health data and data on the intimate sphere.
- Racial or ethnic origin data.
- Genetic data.
- Biometric data for unique identification of a natural person.
- Data on administrative and criminal proceedings or sanctions.
- Data on social security measures.

Processing of sensitive personal data requires explicit consent (Art. 6(7) nFADP) unless another legal justification applies.

#### Duty to Inform (Art. 19 nFADP)

The organisation shall inform data subjects at the time of data collection. Privacy notices shall include: the identity and contact details of the controller, purposes of processing, categories of data processed, recipients or categories of recipients, whether data is transferred abroad and applicable safeguards, the retention period, and the rights of data subjects.

#### Data Subject Rights

Under the nFADP, data subjects have the following rights:

| Right | nFADP Reference | Response Timeline |
|-------|-----------------|-------------------|
| **Right of access** | Art. 25 | Within 30 days, free of charge. May be extended by a further 30 days with notification to the data subject. |
| **Right to rectification** | Art. 32(2)(a) | Within 30 days. |
| **Right to erasure** | Art. 32(2)(c) | Where no legal justification for continued retention. |
| **Right to data portability** | Art. 28 | Personal data provided in a commonly used electronic format, or direct transfer to another controller. |
| **Right to object** | Art. 30(2)(b) | Absolute right for direct marketing; otherwise subject to legitimate grounds. |
| **Right regarding automated decisions** | Art. 21 | Right to be informed of and request human review of decisions made solely by automated means. |

The organisation shall maintain a Data Subject Rights Request Register documenting all requests, responses, and timelines. SLA tracking shall include:

- **Receipt date** — Date the request was received and acknowledged (acknowledgement within 5 business days).
- **Response deadline** — Calculated deadline (30 days from receipt; extended deadline where applicable, with notification to the data subject).
- **Actual response date** — Date the substantive response was provided.
- **SLA compliance** — Whether the response met the deadline (on-time / late / extended with justification).
- **Quarterly SLA reporting** — Aggregate statistics on DSR volumes, response times, compliance rates, and escalations, reported to the CISO and included in the Management Review.

#### Breach Notification (Art. 24 nFADP)

Data security breaches shall be reported to the Federal Data Protection and Information Commissioner (FDPIC) as soon as possible where the breach is likely to result in a high risk to the personality or fundamental rights of data subjects. Data subjects shall also be informed where necessary for their protection or where the FDPIC requires it.

**Tiered notification timelines:**

| Severity | Timeline | Notification |
|----------|----------|-------------|
| **Critical** — Confirmed breach involving sensitive personal data, large-scale exposure, or active exploitation | Within 24 hours of confirmation | FDPIC notification; affected data subjects; executive management; legal counsel |
| **High** — Breach involving personal data likely to result in high risk to individuals | Within 72 hours of confirmation | FDPIC notification; affected data subjects where required; CISO and executive management |
| **Standard** — Breach involving personal data with low risk to individuals | Within 72 hours (assessment); notification if risk threshold met | Internal documentation; FDPIC notification only if high-risk threshold is met upon assessment |

**Note:** The nFADP requires notification "as soon as possible" without a fixed deadline. The 24/72-hour targets are the organisation's internal standard, aligned with GDPR Art. 33 (72-hour requirement where applicable) and best practice.

All breaches shall be documented in the breach register regardless of the notification threshold. Upon discovery of any potential breach, an immediate assessment shall be performed within 4 hours to determine:

- Whether personal data is affected and, if so, categories and approximate volume.
- Whether the breach is likely to result in a high risk to data subjects.
- Which notification obligations are triggered (nFADP, GDPR, contractual).
- Whether data subjects need to be informed for their protection.

The immediate assessment outcome shall be recorded in the breach register entry and approved by the CISO or Compliance Officer.

#### Record of Processing Activities (Art. 12 nFADP / DSV Art. 4-5)

The organisation shall maintain a Record of Processing Activities (ROPA) documenting all processing operations.

**SME exemption (DSV Art. 4):** Organisations with fewer than 250 employees are exempted from maintaining a ROPA unless their processing presents a high risk of violating personality or fundamental rights (e.g., large-scale processing of sensitive data, high-risk profiling). The organisation shall document its assessment of whether the exemption applies, including:

- Current employee headcount and date of assessment.
- Whether the organisation processes sensitive personal data at scale.
- Whether high-risk profiling is conducted.
- Conclusion: exemption applicable / not applicable.
- Approval by: Compliance Officer / DPO.

**Best practice recommendation:** Even where the SME exemption applies, maintaining a simplified ROPA is strongly recommended as it supports accountability, incident response, and audit readiness. The organisation shall reassess the exemption annually and whenever employee headcount approaches 250 or processing activities materially change.

### Swiss Data Protection Ordinance (DSV)

The DSV provides implementing provisions for the nFADP:

- **Art. 1-3 — Data security measures**: The controller and processor shall implement technical and organisational measures appropriate to the risk. The adequacy of measures depends on the purpose, nature, and extent of data processing and the risk to data subjects. Measures shall be reviewed regularly.
- **Art. 4 — Logging of automated processing**: Processing of personal data in automated systems shall be logged to enable retrospective verification that data has not been lost, deleted, destroyed, modified, or disclosed without authorisation. Logs shall be retained for at least one year.
- **Art. 8 — Duty to inform on cross-border transfers**: Where personal data is transferred abroad, the organisation shall disclose the destination country and applicable safeguards.
- **Art. 14 — DPIA retention**: Data Protection Impact Assessment documentation shall be retained for at least 2 years after processing ends.

**Data Protection Impact Assessments (Art. 22 nFADP):** The organisation shall conduct a DPIA before commencing any processing that is likely to result in a high risk to the personality or fundamental rights of data subjects. High-risk processing includes:

- Large-scale processing of sensitive personal data.
- Systematic and extensive profiling with significant effects on individuals.
- Systematic monitoring of publicly accessible areas.
- Use of new technologies where the impact on data subjects is not yet fully understood.

The DPIA shall assess the necessity and proportionality of processing, evaluate risks to data subjects, and identify measures to mitigate those risks. Where the DPIA concludes that high risk remains despite mitigation measures, the FDPIC shall be consulted prior to processing (Art. 23 nFADP).
- **Annex 1 — Adequacy list**: Countries determined by the Swiss Federal Council to provide adequate data protection for the purposes of cross-border data transfers. The organisation shall maintain a current copy of the DSV Annex 1 adequacy list and verify the adequacy status of each destination country before initiating cross-border transfers. Note: The Swiss and EU adequacy lists differ — a country may be adequate under one framework but not the other (e.g., the US is adequate under the Swiss-U.S. Data Privacy Framework but subject to specific conditions).

### Swiss Code of Obligations (CO)

The following provisions of the CO are relevant to information security:

- **Art. 328 — Employer duty of care**: The employer shall protect and respect the personality rights of employees, including the protection of their personal data and privacy.
- **Art. 328b — Data processing in employment**: The employer may process employee data only to the extent that such data concerns the employee's suitability for the job or is necessary for the performance of the employment contract. This provision cannot be waived, even with the employee's consent.
- **Art. 957-958f — Record-keeping obligations**: Legal entities and sole proprietorships with turnover of at least CHF 500,000 shall maintain commercial books and records. Business books, accounting vouchers, business reports, and audit reports shall be retained for 10 years from the end of the business year (Art. 958f CO). Records may be kept on paper, electronically, or in a comparable format provided they can be read at any time.

### EU General Data Protection Regulation (GDPR)

Where the organisation processes personal data of individuals located in the EU/EEA — whether through offering goods or services, monitoring behaviour, or as a processor for EU-based controllers — GDPR shall apply in addition to the nFADP.

Key GDPR-specific obligations include:

- **Legal basis required** — A valid legal basis under Art. 6 GDPR shall be documented for each processing activity (consent, contract, legal obligation, vital interests, public interest, or legitimate interests). The legal basis shall be recorded in the ROPA and, where consent is relied upon, consent records shall be maintained in [GRC Tool / Privacy Management Platform] with evidence of when and how consent was obtained.
- **Breach notification** — Within 72 hours to the competent supervisory authority (Art. 33 GDPR) for breaches likely to result in a risk to rights and freedoms.
- **Data Protection Officer** — Mandatory appointment under Art. 37 GDPR where the organisation's core activities involve large-scale processing of special categories or systematic monitoring.
- **Cross-border transfer mechanisms** — European Commission adequacy decisions, Standard Contractual Clauses, Binding Corporate Rules, or derogations under Art. 44-49 GDPR.

The organisation shall maintain clear documentation of which processing activities fall under nFADP only, which fall under GDPR, and which fall under both.

### Cross-Border Data Transfers

The organisation shall not transfer personal data to countries outside Switzerland unless adequate safeguards are in place:

| Mechanism | Swiss nFADP | EU GDPR (where applicable) |
|-----------|-------------|----------------------------|
| **Adequacy decision** | Swiss Federal Council adequacy determination (Art. 16(1) nFADP, Annex 1 DSV) | European Commission adequacy decision (Art. 45 GDPR) |
| **Standard Contractual Clauses** | SCCs adapted for Swiss law (Art. 16(2)(b) nFADP) | EU-approved SCCs (Art. 46(2)(c) GDPR) |
| **Binding Corporate Rules** | Approved by the FDPIC (Art. 16(2)(a) nFADP) | Approved by competent supervisory authority (Art. 47 GDPR) |
| **Derogations** | Explicit consent, contract performance, vital interests, or other exceptions (Art. 17 nFADP) | Art. 49 GDPR derogations |

**Transfer Impact Assessments (TIAs)** shall be conducted where the adequacy of the destination country is uncertain or where legal frameworks are subject to change. The TIA methodology shall include:

1. **Identify the transfer** — Data categories, volume, recipients, and destination country.
2. **Assess legal framework** — Evaluate the destination country's data protection legislation, government access powers, rule of law, and independent supervisory authority.
3. **Evaluate risks** — Assess the probability and severity of government access to transferred data, considering the specific circumstances of the transfer (data type, industry sector, encryption in transit and at rest).
4. **Identify supplementary measures** — Where the legal framework is insufficient, document additional safeguards (encryption, pseudonymisation, contractual restrictions on onward transfer).
5. **Document and approve** — Record the assessment, conclusion, and approval. TIAs for Tier 1 transfers shall be approved by the Compliance Officer with legal counsel input.
6. **Reassess periodically** — Review TIAs annually and upon material changes to the destination country's legal framework (e.g., court rulings, new legislation, adequacy decision changes).

### Penalties and Enforcement

The organisation shall be aware of the enforcement mechanisms and potential penalties under applicable regulations:

| Regulation | Maximum Penalty | Enforcement Authority |
|------------|-----------------|----------------------|
| Swiss nFADP — Duty to inform (Art. 60) | CHF 250,000 (individual) | FDPIC |
| Swiss nFADP — Minimum data security (Art. 61) | CHF 250,000 (individual) | FDPIC |
| Swiss nFADP — Cross-border transfer violations (Art. 61) | CHF 250,000 (individual) | FDPIC |
| Swiss nFADP — DPO obligations (Art. 62) | CHF 250,000 (individual) | FDPIC |
| Swiss nFADP — Professional secrecy (Art. 62) | CHF 250,000 (individual) | FDPIC |
| EU GDPR | EUR 20 million or 4% of global annual turnover (whichever is higher) | Competent EU supervisory authority |
| Swiss CO | Civil liability under Art. 41ff CO (damages) | Swiss courts |
| PCI DSS (if applicable) | Card brand fines, increased transaction fees, loss of processing ability | PCI SSC / card brands |

**Note:** Under Swiss nFADP, fines are imposed on responsible individuals (not the organisation), making personal accountability a critical compliance driver.

---

## Contractual Requirements

### Customer Compliance Obligations

The organisation shall systematically review all customer contracts for compliance requirements related to information security. This includes:

- **Compliance clauses** in Master Service Agreements (MSAs) and Statements of Work (SOWs).
- **Data Processing Agreements (DPAs)** specifying security and privacy obligations.
- **Security questionnaires** (e.g., SIG, CAIQ) implying conformance expectations.
- **Right-to-audit clauses** requiring the organisation to demonstrate compliance.
- **Certification requirements** (e.g., ISO 27001, SOC 2) mandated by contract.

Contractual compliance requirements shall be assessed and added to the Regulatory Register with the appropriate tier classification. Where a customer contract explicitly requires compliance with a specific regulation and includes enforcement mechanisms (penalties, termination rights), the requirement shall be classified as Tier 1.

**Contract compliance review process:**

1. **Pre-signature review** — Business Development shall flag all compliance clauses to the Compliance Officer before contract execution.
2. **Compliance assessment** — Compliance Officer evaluates whether the organisation can meet each requirement with existing controls or identifies gaps requiring remediation.
3. **Gap notification** — Where gaps exist, Business Development shall be informed of the remediation timeline before contract execution. Contracts shall not be signed where Tier 1 compliance gaps cannot be remediated within the contract start date.
4. **Post-execution tracking** — Contractual requirements added to the Regulatory Register within 10 business days of contract execution.
5. **Renewal review** — Compliance clauses shall be reviewed at each contract renewal for changes or new requirements.

### Supplier Pass-Through Obligations

The organisation shall review supplier and subprocessor agreements for obligations that flow through to the organisation. This includes:

- **Data Processing Agreements** where the organisation acts as subprocessor.
- **Supply chain compliance requirements** passed down from prime contractors.
- **Flow-down clauses** requiring the organisation to meet standards the supplier must meet.
- **Certification requirements** imposed by technology or platform partners.

Pass-through obligations shall be documented in the Regulatory Register alongside directly applicable regulations.

### Certification Requirements

Where the organisation holds or pursues certifications, the compliance requirements associated with those certifications shall be treated as Tier 1 obligations:

- **ISO/IEC 27001:2022** — ISMS requirements including Annex A controls.
- **SOC 2 Type II** (if applicable) — Trust Services Criteria.
- **PCI DSS** (if applicable) — Payment card industry requirements, gated to specific processing activities.

Certification requirements shall be reviewed upon any of the following triggers:

- Publication of a new version of the standard (e.g., ISO 27001:2022 replacing ISO 27001:2013).
- Certification body issuance of new guidance, interpretations, or mandatory transition timelines.
- Surveillance or recertification audit findings requiring corrective action.
- Organisational changes that affect certification scope (new services, locations, or data types).
- Contract execution requiring a new certification not currently held.

### Cryptographic Controls

The organisation shall comply with applicable laws and regulations regarding the use of cryptography, including:

- Import/export restrictions on cryptographic hardware or software.
- Regulations requiring authorities to access encrypted information.
- Legal admissibility of digital signatures and electronic documents.

These requirements shall be documented in the Regulatory Register and reflected in the Use of Cryptography Policy (ISMS-OP-POL-A.8.24).

---

## Compliance Monitoring and Review

### Annual Regulatory Review

The organisation shall conduct a comprehensive annual review of all entries in the Regulatory Register:

1. Confirm the organisation's circumstances have not changed in ways affecting applicability.
2. Confirm each regulation has not been amended in ways affecting applicability or requirements.
3. Validate that the tier assignment for each entry remains appropriate.
4. Identify any new regulations that should be added.
5. Remove or reclassify regulations that are no longer applicable.
6. Document the review date, outcome, and any changes.
7. Update "Last Review Date" and "Next Review Date" fields.

The annual review shall be performed by the Compliance Officer (or equivalent), with ISMS Manager approval of the review summary.

### Trigger Events for Reassessment

In addition to the annual review, the Regulatory Register shall be revisited when triggered by:

| Trigger Category | Examples |
|------------------|----------|
| **Organisational changes** | Geographic expansion or contraction, new service offerings, entry into new industry sectors, mergers and acquisitions, crossing regulatory thresholds (employee count, revenue, data volume). |
| **Regulatory changes** | New laws enacted, existing regulations amended or repealed, new regulatory guidance or court interpretations, changes to adequacy decisions for cross-border transfers. |
| **Contractual changes** | New customer contracts with compliance clauses, contract renewals adding compliance requirements, contract expiration where the contract was the sole driver of applicability, new supplier agreements with pass-through obligations. |
| **Certification changes** | Pursuit of new certifications, updates to certification standards, certification body guidance changes. |

Reassessments triggered by events shall be completed within 30 days of the trigger event (within 60 days for mergers and acquisitions due to complexity).

### Gap Remediation

Where a compliance gap is identified (a requirement exists but the organisation does not fully meet it):

1. **Document the gap** — Record the regulation, requirement, current state, and the nature of the gap.
2. **Assess risk** — Determine the risk of non-compliance (regulatory fines, contractual penalties, reputational harm).
3. **Assign an owner** — Designate a responsible party with authority to remediate.
4. **Define remediation plan** — Specify actions, resources, timeline, and success criteria.
5. **Track to closure** — Monitor progress. Gaps overdue by more than 30 days shall be escalated to the ISMS Manager; gaps overdue by more than 60 days shall be escalated to executive management.
6. **Verify closure** — Confirm remediation is complete, evidence is collected, and the gap is closed.

Where full remediation is not feasible within the required timeframe, the organisation shall implement compensating controls and document a formal risk acceptance signed by executive management.

**External dependency gaps:** Where remediation depends on a third party (e.g., vendor software update, supplier contract amendment, cloud provider feature), the gap owner shall:

- Document the external dependency and the expected resolution timeline from the third party.
- Implement interim compensating controls to reduce risk while awaiting third-party resolution.
- Establish a monitoring cadence (minimum monthly) to track third-party progress.
- Escalate to procurement/vendor management if the third party fails to meet committed timelines.
- Record the external dependency in the gap tracker alongside the internal remediation plan.

---

## Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Executive Management** | Approve Tier 1 regulatory obligations; commit resources for compliance; accept residual compliance risks. |
| **CISO / ISMS Manager** | Maintain the Regulatory Register; coordinate compliance activities; approve annual review summary; ensure ISMS controls align with regulatory requirements. |
| **Compliance Officer** | Conduct regulatory identification and applicability assessments; monitor regulatory changes; perform annual and event-driven reviews; track gap remediation. |
| **Legal Counsel** | Provide legal interpretation of regulations; validate applicability determinations for Tier 1 regulations; review contractual compliance obligations; advise on dispute resolution. |
| **HR** | Ensure compliance with employment-related regulations (CO Art. 328/328b); coordinate employee data protection obligations. |
| **Finance** | Ensure compliance with record-keeping obligations (CO Art. 957-958f); maintain financial records for the statutory retention period. |
| **Business Development** | Identify contractual compliance requirements during pre-contract due diligence; communicate new customer compliance obligations to Compliance Officer. |
| **All Employees** | Report potential regulatory requirements or compliance concerns to line management; comply with policies implementing regulatory obligations. |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence Item | Review Cycle |
|---|---------------|--------------|
| 1 | **Regulatory Register** — maintained and up to date, with tier classification and review dates per entry | Annually (comprehensive); event-driven as required |
| 2 | **Applicability assessment records** — documented rationale for each regulation's inclusion, tier, or exclusion | Per assessment; retained for duration of applicability + 7 years |
| 3 | **Annual regulatory review summary** — scope, findings, changes, approval | Annually in Q4 |
| 4 | **nFADP compliance documentation** — privacy notices, ROPA, DPIA records, consent records | Annually; updated upon changes to processing |
| 5 | **Data subject rights request register** — requests logged with response timelines and outcomes | Quarterly review of register; responses within 30 days |
| 6 | **Breach register** — all breaches documented with notification decisions and rationale | Per incident; register reviewed quarterly |
| 7 | **Contractual compliance matrix** — customer and supplier contracts mapped to regulatory obligations | Upon contract execution; reviewed at renewal |
| 8 | **Gap remediation tracker** — identified gaps with owner, remediation plan, status, and closure evidence | Monthly review until closure |
| 9 | **Regulatory change log** — changes detected, impact assessed, actions taken | Ongoing; reviewed quarterly |
| 10 | **Cross-border data transfer assessments** — Transfer Impact Assessments, safeguard documentation (SCCs, adequacy determinations) | Annually or upon legal changes |
| 11 | **Training records** — employees trained on regulatory obligations relevant to their role | Annually; completion tracked |
| 12 | **Legal counsel opinions** — documented legal advice on applicability determinations (Tier 1) | Per determination; retained with assessment record |
| 13 | **Regulatory change communication records** — notifications to affected teams, acknowledgement receipts, implementation tracking (SOC 2: CC2.3) | Per regulatory change; retained 3 years |
| 14 | **Legal counsel review evidence** — confirmation of legal review for Tier 1 applicability, contractual compliance opinions, dispute resolution advice (SOC 2: CC3.2) | Per Tier 1 determination; retained with assessment |
| 15 | **Compliance testing evidence** — results of periodic compliance testing against Tier 1 requirements, test procedures, findings, and remediation (SOC 2: CC4.1) | Semi-annually for Tier 1; annually for Tier 2 |

---

# Definitions

| Term | Definition |
|------|------------|
| **Applicable regulation** | Any law, statute, regulation, directive, contractual clause, or standard that the organisation is legally, contractually, or voluntarily required to comply with in relation to information security. |
| **Contractual obligation** | A compliance requirement imposed by a customer contract, supplier agreement, or partnership agreement that creates an enforceable obligation on the organisation. |
| **FDPIC** | Federal Data Protection and Information Commissioner (*Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter, EDÖB*) — the Swiss supervisory authority for data protection. |
| **nFADP (revDSG)** | The revised Swiss Federal Act on Data Protection (*Bundesgesetz über den Datenschutz*), effective 1 September 2023. Also referred to as FADP or revFADP. |
| **DSV** | Swiss Data Protection Ordinance (*Verordnung über den Datenschutz*), the implementing ordinance to the nFADP. |
| **Personal data** | Any information relating to an identified or identifiable natural person. Under the revised nFADP, legal persons are no longer covered. |
| **Sensitive personal data** | Personal data requiring particular protection under nFADP Art. 5(c), including health data, genetic and biometric data, racial or ethnic origin data, political, religious, or trade union opinions or activities, data on criminal or administrative proceedings, and social security measures data. |
| **Regulatory Register** | The authoritative, maintained record of all legal, statutory, regulatory, and contractual requirements applicable to the organisation's information security programme. |
| **Tier 1 (Mandatory)** | Regulations with legal obligation, enforceable contractual requirement, or certification requirement. Full compliance required. |
| **Tier 2 (Conditional)** | Regulations with potential future applicability or voluntarily adopted for strategic reasons. Monitoring and readiness required. |
| **Tier 3 (Informational)** | Frameworks used for guidance, benchmarking, or best practice reference. No compliance obligation. |
| **ROPA** | Record of Processing Activities — a documented inventory of all personal data processing operations, required under Art. 12 nFADP (subject to SME exemption under DSV Art. 4). |
| **DPIA** | Data Protection Impact Assessment — a structured assessment of high-risk processing activities, required under Art. 22 nFADP. |
| **Transfer Impact Assessment** | An evaluation of the legal framework of a destination country to determine whether personal data can be transferred with adequate protection. |

---

# Policy Compliance

## Compliance Measurement

The information security management team shall verify compliance with this policy through various methods, including but not limited to: Regulatory Register audits, compliance gap analysis, internal and external audits, regulatory review records, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to executive management.

Exceptions shall not be granted for mandatory regulatory requirements (Tier 1 obligations) unless supported by legal counsel opinion and formal executive risk acceptance.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

Under Swiss nFADP, individuals responsible for wilful data protection violations may be subject to criminal fines of up to CHF 250,000. Under GDPR (where applicable), organisational fines may reach EUR 20 million or 4% of global annual turnover.

Non-compliance with contractual requirements may result in contractual penalties, termination of business relationships, or loss of certifications.

## Regulatory Change Communication (SOC 2: CC2.3)

When regulatory changes are identified that affect the organisation's compliance obligations:

1. **Assessment** — Compliance Officer assesses the impact and identifies affected teams, systems, and processes within 10 business days of change identification.
2. **Communication** — Affected teams are notified via [email / internal communication platform] with a summary of the change, impact assessment, and required actions.
3. **Acknowledgement** — Team leads shall acknowledge receipt and confirm understanding within 5 business days.
4. **Implementation tracking** — Required changes are tracked in the gap remediation tracker with assigned owners and deadlines.
5. **Verification** — Compliance Officer verifies implementation of required changes before the regulation's effective date (or within 90 days for already-effective changes).

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to applicable legislation, supervisory authority guidance, regulatory enforcement trends, contractual landscape changes, emerging regulatory risks, and lessons learned from audits and compliance reviews.

---

# Areas of the ISO 27001 Standard Addressed

Legal, Statutory, Regulatory and Contractual Requirements Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 4.2 Understanding the needs and expectations of interested parties | 5.31 Legal, statutory, regulatory and contractual requirements |
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.1.3 Information security risk treatment | 5.36 Compliance with policies, rules, and standards |
| Clause 9.1 Monitoring, measurement, analysis and evaluation | 5.35 Independent review of information security |
| | **5.31 Legal, statutory, regulatory and contractual requirements** |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 6 — Data protection principles; Art. 8 — Data security; Art. 12 — ROPA; Art. 19 — Duty to inform; Art. 21 — Automated decisions; Art. 24 — Breach notification; Art. 25-32 — Data subject rights |
| Swiss DSV (Data Protection Ordinance) | Art. 1-3 — Minimum data security measures; Art. 4 — Logging of automated processing; Art. 8 — Cross-border transfer disclosure; Art. 14 — DPIA retention; Annex 1 — Adequacy list |
| Swiss Code of Obligations (CO) | Art. 328/328b — Employer data protection duties; Art. 957-958f — Record-keeping obligations (10-year retention) |
| EU GDPR (where applicable) | Art. 5-6 — Principles and legal basis; Art. 12-22 — Data subject rights; Art. 32-34 — Security and breach notification; Art. 37 — DPO appointment; Art. 44-49 — International transfers |
| ISO/IEC 27001:2022 | Annex A Control 5.31 — Legal, statutory, regulatory and contractual requirements |
| ISO/IEC 27002:2022 | Section 5.31 — Implementation guidance |
| NIST Cybersecurity Framework 2.0 | GV.OC — Organisational Context (legal and regulatory requirements) |
| NIST SP 800-53 Rev 5 | SA-9 — External Information System Services; PM-8 — Critical Infrastructure Plan |
| CIS Controls v8 | Control 15 — Service Provider Management (contractual security requirements) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
