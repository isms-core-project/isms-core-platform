<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.2.2-5-TG:privacy:TG:a.1.2.2-5 -->
**PRIV-IMP-A.1.2.2-5-TG — Lawful Basis and Consent — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Lawful Basis and Consent — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.1.2.2-5-TG |
| **Related Policy** | PRIV-POL-A.1.2.2-5 (Lawful Basis and Consent) |
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

**Review Cycle**: Annual (or upon significant regulatory change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.1.2.2-5 (Lawful Basis and Consent — the governing policy)
- PRIV-IMP-A.1.2.2-5-UG (Lawful Basis and Consent — User Guide)
- PRIV-POL-A.1.2.6-9 (Privacy Governance and Records — RoPA schema)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for lawful basis determination and consent management. It covers:

- RoPA fields relevant to lawful basis documentation
- Legitimate Interests Assessment (LIA) template
- Consent Record schema
- Purpose Compatibility Assessment template
- Consent mechanism technical requirements

**Audience**: DPO, Legal/Compliance, Development/Product Teams.

---

## 1. RoPA Lawful Basis Fields

The fields below supplement the core RoPA schema (maintained in PRIV-IMP-A.1.2.6-9-TG). These fields must be completed per processing activity to evidence A.1.2.2 and A.1.2.3 compliance.

| Field | Type | Description |
|-------|------|-------------|
| Processing Purpose | Text | Specific, explicit purpose statement — not vague or generic |
| Purpose Category | Enum | Service Delivery / Contract Performance / Legal Compliance / Internal Operations / Marketing / Analytics / Research / Safety / Other |
| Lawful Basis (Art. 6) | Enum | Consent (a) / Contract (b) / Legal obligation (c) / Vital interests (d) / Public task (e) / Legitimate interests (f) |
| Art. 6 Basis Evidence Ref | Text | Reference to evidence document (LIA ref / legal provision / consent process ref) |
| Special Category Basis (Art. 9) | Enum | Not applicable / Explicit consent (a) / Employment law (b) / Vital interests (c) / Legitimate activities NGO (d) / Made public (e) / Legal claims (f) / Substantial public interest (g) / Health/social care (h) / Public health (i) / Archiving/research (j) |
| Art. 9 Evidence Ref | Text | Evidence reference for Art. 9 condition |
| CH FADP Lawful Basis | Enum | Consent / Legitimate interest / Legal obligation / Vital interest / Proportionate to purpose |
| LIA Reference | Text | If legitimate interests: LIA document reference |
| Legal Provision | Text | If legal obligation: specific legal provision (Act, Article) |
| Consent Process Reference | Text | If consent: consent process document reference |
| Compatible Secondary Uses | Text | Approved secondary uses with compatibility assessment references |
| Last Basis Review | Date | Date basis was last reviewed |
| Reviewed By | Text | DPO name |

---

## 2. Legitimate Interests Assessment (LIA) Template

```
LEGITIMATE INTERESTS ASSESSMENT

LIA Reference: LIA-[YYYY]-[NNN]
Processing Activity: _____________________________________________
DPO Conducting Assessment: _____________________________________________
Date: _____________________________________________

STEP 1 — PURPOSE TEST
Legitimate interest claimed: _____________________________________________

Is the interest real and specific (not generic)? [ ] Yes  [ ] No
Is the interest a legitimate one (not illegal or contrary to fundamental rights)? [ ] Yes  [ ] No
Is the interest the organisation's own, or a third party's? [ ] Own  [ ] Third party: ___________
Purpose test outcome: [ ] Pass — proceed  [ ] Fail — cannot rely on legitimate interests

STEP 2 — NECESSITY TEST
Is the processing necessary for the legitimate interest?
  Could the interest be achieved with less or no PII? [ ] Yes (use less/no PII)  [ ] No
  Is the processing actually necessary, not just useful or convenient? [ ] Yes  [ ] No

Necessity test outcome: [ ] Pass — proceed  [ ] Fail — cannot rely on legitimate interests

STEP 3 — BALANCING TEST
PII categories involved: _____________________________________________
Number of data subjects: _____________________________________________
Nature of PII: [ ] Ordinary  [ ] Financial  [ ] Special category  [ ] Sensitive
Data subjects' reasonable expectations (would they expect this use?): [ ] Yes  [ ] Unlikely  [ ] No

Factors favouring [Organisation]:
  [ ] PII subjects are customers/employees in an existing relationship
  [ ] Processing provides a clear benefit to the data subjects
  [ ] Processing is of low sensitivity
  [ ] Safeguards are in place (pseudonymisation, access restriction, etc.)

Factors favouring data subjects:
  [ ] Data subjects are vulnerable individuals
  [ ] Special category or sensitive PII is involved
  [ ] Processing could cause significant harm or distress
  [ ] Data subjects would not reasonably expect this use
  [ ] Children's data is involved

Balancing conclusion:
[ ] Organisation's interests prevail — safeguards: [describe compensating measures]
[ ] Data subjects' interests prevail — cannot rely on legitimate interests; assess alternative basis

SAFEGUARDS TO BE IMPLEMENTED (if legitimate interests confirmed):
- _____________________________________________
- _____________________________________________

Right to Object: Data subjects must be informed of right to object (Art. 21 GDPR) in privacy notice.

CONCLUSION
[ ] Legitimate interests basis is confirmed. Processing may proceed with safeguards.
[ ] Legitimate interests basis is not confirmed. Alternative basis required or processing must cease.

DPO Signature: _________________________ Date: _____________
Legal Review (if applicable): _________________________ Date: _____________
Next review trigger: [ ] Annual  [ ] On change to processing activity  [ ] On regulatory guidance update
```

---

## 3. Consent Record Schema

The consent record system must generate a record for each consent event. Maintained by the development team per DPO-approved schema.

| Field | Type | Description |
|-------|------|-------------|
| Consent Record ID | Text | Unique reference (e.g., CONS-2026-001) |
| Subject ID | Text | Internal identifier linking consent to the data subject's account or identity |
| Subject Reference | Text | External reference (e.g., anonymised hash linking consent to account, without raw PII in this register) |
| Consent Statement Version | Text | Version of the consent text/statement presented (e.g., "Privacy Notice v2.1 Consent Block") |
| Purposes Consented To | Multi-select | List of purposes covered by this consent event |
| Consent Method | Enum | Checkbox / Digital Signature / Verbal (recorded) / Paper Form / Email Confirmation |
| Consent Timestamp | DateTime | ISO 8601 timestamp of the consent event |
| IP Address / Session | Text | Technical evidence of the consent session (for digital consent) |
| Platform / Channel | Text | Where consent was collected (e.g., registration form, settings page, paper form reference) |
| Status | Enum | Active / Withdrawn / Expired |
| Withdrawal Timestamp | DateTime | If withdrawn: date and time of withdrawal |
| Withdrawal Channel | Text | How withdrawal was received (email, settings page, written, portal) |
| Processing Ceased Date | Date | Date on which processing based on this consent ceased following withdrawal |
| Notes | Text | Child consent parental reference; exception handling |

---

## 4. Purpose Compatibility Assessment Template

```
PURPOSE COMPATIBILITY ASSESSMENT

Assessment Reference: PCA-[YYYY]-[NNN]
Original Processing Activity (RoPA ref): _____________________________________________
Original Purpose: _____________________________________________
Proposed Secondary Purpose: _____________________________________________
DPO Conducting Assessment: _____________________________________________
Date: _____________________________________________

COMPATIBILITY FACTORS (GDPR Recital 50 / Art. 6(4))

1. Link between purposes:
   How similar is the proposed secondary purpose to the original purpose?
   [ ] Direct link (closely related)  [ ] Some link (same domain)  [ ] No link (different domain)
   Assessment: _______________________________________________

2. Context of collection:
   What was the context in which the PII was collected?
   Would data subjects reasonably expect this secondary use?
   [ ] Yes  [ ] Possibly  [ ] No
   Assessment: _______________________________________________

3. Nature of the PII:
   [ ] Ordinary personal data  [ ] Financial  [ ] Special category  [ ] Sensitive
   Special category or sensitive PII: [ ] Yes — high compatibility bar  [ ] No
   Assessment: _______________________________________________

4. Consequences for data subjects:
   What are the likely consequences of the secondary use?
   [ ] Positive or neutral  [ ] Minor impact  [ ] Significant impact  [ ] Harmful
   Assessment: _______________________________________________

5. Existence of safeguards:
   Are there safeguards in place for the secondary use?
   [ ] Pseudonymisation  [ ] Access restriction  [ ] Encryption  [ ] Aggregation  [ ] Other: ___
   Assessment: _______________________________________________

COMPATIBILITY CONCLUSION
[ ] Compatible — secondary use is compatible with original purpose; may proceed without fresh consent
    Rationale: _______________________________________________
[ ] Not compatible — secondary use requires fresh consent or a separate legal basis
    Action required: _______________________________________________

DPO Signature: _________________________ Date: _____________
```

---

## 5. Consent Mechanism Technical Requirements

### For Digital Consent (Web / App)

| Requirement | Technical Specification |
|-------------|------------------------|
| Opt-in mechanism | Unchecked checkbox (not pre-ticked) or explicit button action |
| Consent presentation | Consent statement presented before the consent action — not embedded in T&Cs scroll |
| Separate purposes | Separate consent control per distinct processing purpose |
| Withdrawal mechanism | Accessible from account settings or equivalent within 2 clicks; "unsubscribe" link in all consent-based marketing emails |
| Record generation | Consent record generated automatically on consent event: ID, timestamp, version, purpose, IP, channel |
| Consent version | Consent statement version-controlled; record links to version presented |
| Session evidence | Session token or IP logged as technical evidence of the consent event |

### For Paper / In-Person Consent

| Requirement | Technical Specification |
|-------------|------------------------|
| Form version control | All paper consent forms version-controlled with form ID and version date |
| Completion | Data subject name, date, signature required |
| Scope statement | Specific purpose(s) stated on the form — data subject should know what they consent to |
| Record entry | Paper consent entered into consent record system within 2 business days of collection |
| Original retention | Original signed form scanned and retained per consent record retention period |

---

<!-- QA_VERIFIED: [Date] -->
