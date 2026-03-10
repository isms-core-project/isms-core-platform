<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.2.6-9-TG:privacy:TG:a.1.2.6-9 -->
**PRIV-IMP-A.1.2.6-9-TG — Privacy Governance and Records — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Privacy Governance and Records — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.1.2.6-9-TG |
| **Related Policy** | PRIV-POL-A.1.2.6-9 (Privacy Governance and Records) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial technical guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.1.2.6-9 (Privacy Governance and Records — the governing policy)
- PRIV-IMP-A.1.2.6-9-UG (Privacy Governance and Records — User Guide)
- PRIV-IMP-A.1.2.2-5-TG (Lawful Basis and Consent — RoPA lawful basis fields)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for DPIA, processor contracts, joint controller arrangements, and the RoPA. It covers:

- DPIA Screening Record template
- DPIA Register schema
- Full DPIA template
- RoPA schema (full field list)
- Processor Agreement Clause Checklist
- Processor Agreement Register schema
- Joint Controller Arrangement Register schema

**Audience**: DPO, Legal/Compliance.

---

## 1. DPIA Screening Record

```
DPIA SCREENING RECORD

Screening Reference: DPIAS-[YYYY]-[NNN]
Processing Activity: _____________________________________________
Data Owner: _____________________________________________
DPO Conducting Screening: _____________________________________________
Screening Date: _____________________________________________

DESCRIPTION OF PROPOSED PROCESSING
PII collected/used: _____________________________________________
Data subjects: _____________________________________________
Purpose: _____________________________________________
Technology / system: _____________________________________________
Recipients / processors: _____________________________________________

MANDATORY DPIA CRITERIA ASSESSMENT (GDPR Art. 35(3))
[ ] Systematic and extensive profiling with legal or significant effects
[ ] Large-scale processing of special category PII (Art. 9) or criminal data (Art. 10)
[ ] Systematic monitoring of publicly accessible areas
(One or more ticked: DPIA mandatory)

SUPERVISORY AUTHORITY DPIA-REQUIRED LIST
Does this processing appear on the lead DPA's mandatory DPIA list?
[ ] Yes — DPIA mandatory  [ ] No  [ ] Unknown — DPO to confirm

ADDITIONAL HIGH-RISK INDICATORS (EDPB criteria — 2 or more = DPIA recommended)
[ ] Evaluation or scoring of individuals
[ ] Automated decision-making with legal or significant effects
[ ] Systematic monitoring
[ ] Sensitive data or data of highly personal nature
[ ] Data processed at large scale
[ ] Matching or combining datasets
[ ] Data concerning vulnerable data subjects (children, employees)
[ ] Innovative use or application of new technologies
[ ] Prevents access to service or contract
Number of indicators ticked: ___

SCREENING OUTCOME
[ ] Full DPIA required — reason: _______________________________________________
[ ] Full DPIA not required at this time — rationale: _______________________________________________
[ ] Further information needed before screening can be completed

DPIA Register updated: [ ] Yes  Reference: _______________

DPO Signature: _________________________ Date: _____________
```

---

## 2. DPIA Register

### Schema

| Field | Type | Description |
|-------|------|-------------|
| DPIA Reference | Text | Unique ID (e.g., DPIA-2026-001) |
| Processing Activity | Text | Name of the processing activity |
| RoPA Reference | Text | Linked RoPA entry |
| Data Owner | Text | Business owner of the processing activity |
| DPIA Type | Enum | Screening Only / Full DPIA |
| Screening Date | Date | Date screening was completed |
| Full DPIA Start Date | Date | If full DPIA: date commenced |
| Full DPIA Completion Date | Date | Date full DPIA signed off |
| DPO Conducting | Text | DPO name |
| Residual Risk Level | Enum | Low / Medium / High / Not Assessed |
| Prior Consultation Required | Boolean | Yes / No |
| Prior Consultation Date | Date | If required: date submitted to DPA |
| DPA Reference | Text | DPA response reference number |
| Processing Status | Enum | Approved to Commence / On Hold (awaiting DPA) / Approved Pending Mitigation / Not Approved |
| Next Review Trigger | Text | Description of what triggers the next review |
| Next Review Date | Date | Latest date for next review (max 3 years for high-risk) |
| Notes | Text | Open items, DPA correspondence references |

---

## 3. Full DPIA Template

```
DATA PROTECTION IMPACT ASSESSMENT

DPIA Reference: DPIA-[YYYY]-[NNN]
Processing Activity: _____________________________________________
Data Owner: _____________________________________________
DPO: _____________________________________________
Version: 1.0
Date: _____________________________________________
Status: [ ] Draft  [ ] Under Review  [ ] Approved

SECTION 1 — DESCRIPTION OF PROCESSING

1.1 Purpose and context of the processing:
[Describe what the processing achieves and why it is being introduced or changed]

1.2 PII categories processed:
[ ] Ordinary PII (names, contact details, identifiers, employment)
[ ] Financial PII (bank, payment, salary)
[ ] Special category: [ ] Health [ ] Biometric [ ] Genetic [ ] Racial/ethnic
                       [ ] Religious [ ] Political [ ] Trade union [ ] Sex life/orientation
[ ] Sensitive: [ ] Children  [ ] National ID  [ ] Criminal records  [ ] Credentials

1.3 Data subjects:
[ ] Customers / users   [ ] Employees   [ ] Job applicants   [ ] Suppliers
[ ] Vulnerable individuals: [ ] Children  [ ] Medical patients  [ ] Other: ______
Approximate number: ___________

1.4 Processing operations: (collection, storage, access, transfer, deletion, etc.)
[Describe each operation]

1.5 Systems and processors involved:
[System names, internal processors, external processors]

1.6 International transfers: [ ] Yes — destinations: ___________  [ ] No

SECTION 2 — NECESSITY AND PROPORTIONALITY

2.1 Is this processing necessary for the stated purpose? [ ] Yes  [ ] No
2.2 Could the purpose be achieved with less PII? [ ] No  [ ] Yes — changes: ___________
2.3 Lawful basis: ___________
2.4 Compliance with data subject rights and purpose limitation: [Describe]
2.5 Retention period: ___________ Justification: ___________

SECTION 3 — RISK ASSESSMENT

| Risk | Likelihood (1-3) | Severity (1-3) | Risk Score | Mitigation Measures | Residual Risk |
|------|-----------------|---------------|------------|--------------------|-|
| Unauthorised access / data breach | | | | | |
| Excessive data collection | | | | | |
| Unlawful purpose or use | | | | | |
| Inaccurate data causing harm | | | | | |
| Discrimination / profiling effects | | | | | |
| Loss of data subjects' control | | | | | |
| [Other risk specific to this processing] | | | | | |

Scoring: Likelihood: 1=unlikely, 2=possible, 3=likely | Severity: 1=minor, 2=significant, 3=severe
Risk Score = Likelihood × Severity | Residual risk after mitigation

SECTION 4 — OUTCOME

Overall residual risk level: [ ] Low  [ ] Medium  [ ] High

[ ] Processing approved to proceed — risk is acceptable
[ ] Processing approved with mandatory risk-reduction measures — see above
[ ] Residual HIGH risk — prior consultation required before processing commences (Art. 36 / FADP Art. 23)
[ ] Processing not approved — risk cannot be reduced to acceptable level

SECTION 5 — SIGN-OFF

Data Owner: _________________________ Date: _____________
DPO: _________________________ Date: _____________
Executive Management (if residual high risk): _________________________ Date: _____________
```

---

## 4. RoPA Schema (Controller)

The RoPA is maintained by the DPO. One entry per processing activity. Fields required by GDPR Article 30(1) are marked (Art. 30).

| Field | Type | Description |
|-------|------|-------------|
| Activity ID | Text | Unique reference (e.g., ROPA-C-001) |
| Activity Name | Text | Descriptive name of the processing activity (Art. 30) |
| Department / Owner | Text | Business unit and Data Owner |
| Controller Contact | Text | [Organisation] legal name, address, DPO contact (Art. 30) |
| Processing Purpose | Text | Specific documented purpose (Art. 30) |
| Lawful Basis (Art. 6) | Enum | Consent / Contract / Legal obligation / Vital interests / Public task / Legitimate interests |
| Art. 9 Condition | Text | If special category: Art. 9(2) condition |
| LIA / Legal Provision Ref | Text | Reference to supporting evidence |
| Data Subject Categories | Text | Categories of data subjects (Art. 30) |
| PII Categories | Multi-select | Ordinary / Financial / Special Category / Sensitive |
| PII Fields | Text | Specific data fields processed |
| Recipients | Text | Categories of recipients — internal, processors, joint controllers (Art. 30) |
| Processor References | Text | Linked Processor Agreement Register entries |
| Joint Controller References | Text | Linked Joint Controller Arrangement references |
| International Transfers | Boolean | Yes / No |
| Transfer Destinations | Text | Countries to which PII is transferred (Art. 30) |
| Transfer Mechanism | Text | Adequacy decision / SCCs / BCRs / Derogation |
| Transfer Register Reference | Text | International Transfer Register entry |
| Retention Period | Text | Retention periods by PII category (Art. 30) |
| Security Measures Reference | Text | Reference to relevant PRIV-POL-A.3.23-31 controls |
| DPIA Reference | Text | Linked DPIA Register entry (if applicable) |
| Date Added to RoPA | Date | Date entry was created |
| Last Reviewed | Date | Date last reviewed for accuracy |
| Reviewed By | Text | DPO name |
| Next Review | Date | Scheduled next review |
| Status | Enum | Active / Discontinued |
| Discontinuation Date | Date | If discontinued: date processing ceased |
| Notes | Text | Open items, changes pending |

---

## 5. Processor Agreement Clause Checklist (GDPR Art. 28(3))

Use when reviewing a processor agreement for compliance with GDPR Article 28(3):

| Clause | Required | Present in Agreement? | Section Ref |
|--------|---------|----------------------|-------------|
| Process PII only on documented instructions from controller | Mandatory | Yes / No / Partial | |
| Inform controller if instructions infringe GDPR | Mandatory | Yes / No / Partial | |
| Ensure confidentiality obligations for all processing personnel | Mandatory | Yes / No / Partial | |
| Implement appropriate security measures (Art. 32) | Mandatory | Yes / No / Partial | |
| No sub-processor without prior written consent of controller | Mandatory | Yes / No / Partial | |
| Flow-down of equivalent obligations to sub-processors | Mandatory | Yes / No / Partial | |
| Assist controller with data subject rights obligations | Mandatory | Yes / No / Partial | |
| Assist with security, breach notification, DPIA, prior consultation | Mandatory | Yes / No / Partial | |
| Return or delete all PII at end of service (controller's choice) | Mandatory | Yes / No / Partial | |
| Provide information necessary to demonstrate compliance; support audits | Mandatory | Yes / No / Partial | |
| Reference to applicable ISO 27701 Table A.2 processor controls | Recommended | Yes / No | |
| Breach notification to controller (max 24 hours per agreement) | Recommended | Yes / No | |

**Overall adequacy**:
- [ ] Agreement is compliant with Art. 28(3) — approved
- [ ] Agreement requires amendment — items above marked No/Partial
- [ ] DPO sign-off: _________________ Date: _________

---

## 6. Processor Agreement Register

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Agreement ID | Text | Unique reference (e.g., PA-2026-001) |
| Processor Name | Text | Legal entity name |
| Processing Activities Covered | Text | What PII processing is covered by this agreement |
| Agreement Type | Enum | Full DPA (Art. 28) / Amended Standard Terms / DPA Addendum |
| Agreement Reference | Text | Contract document reference or location |
| Execution Date | Date | Date agreement was signed |
| Review / Expiry Date | Date | Next review date (annually for high-risk; every 3 years standard) |
| Risk Category | Enum | High / Standard |
| Art. 28(3) Clauses Complete | Enum | Yes / Partial — see notes / No |
| Sub-processors Disclosed | Text | Known sub-processors with PII access |
| International Transfers via Processor | Boolean | Yes / No |
| Status | Enum | In Force / Under Negotiation / Expired / Terminated |
| Last DPO Review | Date | Date DPO last confirmed adequacy |
| Notes | Text | Open items, amendment status |

---

## 7. Joint Controller Arrangement Register

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Arrangement ID | Text | Unique reference (e.g., JC-2026-001) |
| Joint Controller Name | Text | Legal entity name of the other controller |
| Processing Activity | Text | Description of the joint processing |
| [Organisation]'s Obligations | Text | Which GDPR obligations [Organisation] is responsible for under the arrangement |
| Other Controller's Obligations | Text | Which obligations the other controller is responsible for |
| Data Subject Contact | Text | Which controller data subjects should contact (and for what) |
| Essence Made Available to Data Subjects | Enum | Yes — in privacy notice / Yes — on request / No — action required |
| Arrangement Execution Date | Date | Date arrangement was signed |
| Review Date | Date | Next scheduled review |
| Status | Enum | Active / Terminated |
| Notes | Text | Open items |

---

<!-- QA_VERIFIED: [Date] -->
