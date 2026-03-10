<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.3.2-4-TG:privacy:TG:a.1.3.2-4 -->
**PRIV-IMP-A.1.3.2-4-TG — Transparency and Information Provision — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Transparency and Information Provision — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.1.3.2-4-TG |
| **Related Policy** | PRIV-POL-A.1.3.2-4 (Transparency and Information Provision) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial technical guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.1.3.2-4 (Transparency and Information Provision — the governing policy)
- PRIV-IMP-A.1.3.2-4-UG (Transparency and Information Provision — User Guide)
- PRIV-POL-A.1.2.6-9 (Privacy Governance and Records — RoPA schema)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for privacy notice management and transparency obligations. It covers:

- PII Principal Obligations Register schema
- Privacy Notice Version Register schema
- Full Privacy Notice structural template (Article 13)
- Layered (short) Notice template
- Indirect Collection Notification template
- Collection Point Audit Record template

**Audience**: DPO, Legal/Compliance, Marketing/Communications.

---

## 1. PII Principal Obligations Register

Maps each applicable transparency and other obligation to the processing activities it affects. Maintained by the DPO as part of the broader PLRR (per PRIV-POL-A.3.13-16).

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Obligation ID | Text | Unique reference (e.g., OBL-GDPR-ART13-001) |
| Legal Source | Text | GDPR Art. 13 / GDPR Art. 14 / CH FADP Art. 19 / CH FADP Art. 20 / Other |
| Obligation Description | Text | Plain-language description of the obligation |
| Applicable Processing Activities | Text | RoPA activity IDs this obligation applies to |
| Collection Method | Enum | Direct / Indirect / Both |
| Timing Requirement | Text | e.g., "At or before point of collection" / "Within 1 month of obtaining PII" |
| Fulfilment Mechanism | Text | How the obligation is met (e.g., website privacy notice v2.1; employee notice; inline notice) |
| Current Status | Enum | Fulfilled / Partially Fulfilled / Not Yet Fulfilled / Under Review |
| Last Reviewed | Date | Date obligation was last confirmed as met |
| Reviewed By | Text | DPO name |
| Notes | Text | Open items, jurisdiction-specific considerations |

---

## 2. Privacy Notice Version Register

All versions of privacy notices are retained and tracked. Maintained by the DPO.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Notice ID | Text | Unique reference (e.g., PN-EXT-001) |
| Notice Name | Text | Descriptive name (e.g., "Website Privacy Notice", "Employee Privacy Notice") |
| Audience | Text | Who this notice is for |
| Version | Text | e.g., 1.0, 1.1, 2.0 |
| Effective Date | Date | Date this version became effective |
| Retired Date | Date | Date this version was replaced (blank if current) |
| Author | Text | Name of drafter |
| DPO Approval Date | Date | Date DPO approved this version |
| Legal Review Date | Date | Date Legal reviewed this version |
| Key Changes from Prior Version | Text | Summary of material changes |
| Published Location | Text | URL or document reference |
| Processing Activities Covered | Text | RoPA activity IDs covered by this notice |
| Status | Enum | Current / Retired / Draft |

---

## 3. Full Privacy Notice Structural Template (Article 13)

The template below provides the required structure for a GDPR Article 13-compliant privacy notice. All bold labels should appear as section headings or clearly labelled fields in the published notice.

```
PRIVACY NOTICE
[Organisation Legal Name]
Version: [X.X] | Effective: [Date] | Last Updated: [Date]

---

1. WHO WE ARE

[Organisation Legal Name] ("[Organisation]") is the data controller for the
personal data described in this notice.

Registered address: [Address]
Privacy enquiries: privacy@[domain] | Data Protection Officer: [DPO Name]

---

2. WHAT PERSONAL DATA WE COLLECT AND WHY

We process your personal data for the following purposes:

| Purpose | Data Collected | Legal Basis | Retention |
|---------|---------------|-------------|-----------|
| [Purpose 1 — specific] | [PII categories] | [Art. 6 basis] | [Period] |
| [Purpose 2 — specific] | [PII categories] | [Art. 6 basis] | [Period] |
| [Purpose 3 — ...] | ... | ... | ... |

[Where legitimate interests is the basis, include a brief explanation of the
interest and state that data subjects have the right to object — see Section 7.]

[Where special category data is processed, include the Art. 9(2) condition.]

---

3. WHO WE SHARE YOUR DATA WITH

We may share your personal data with:
- [Internal teams / functions — brief description]
- [Service providers acting as processors — category description, not exhaustive list]
- [Regulatory or legal authorities where required by law]
- [Joint controllers — identified if applicable]

We do not sell your personal data to third parties.

---

4. INTERNATIONAL TRANSFERS

[If applicable:]
We transfer personal data to [country/countries]. This transfer is safeguarded by:
- [Adequacy decision / Standard Contractual Clauses (SCCs) / Binding Corporate Rules]

[If not applicable: We do not transfer your personal data outside [jurisdiction].]

---

5. HOW LONG WE KEEP YOUR DATA

We retain your personal data for:
[List retention periods by purpose or data category. Where an exact period cannot
be given, state the criteria used to determine it.]

---

6. YOUR RIGHTS

You have the following rights regarding your personal data:
- **Access**: Request a copy of the personal data we hold about you (Art. 15)
- **Rectification**: Ask us to correct inaccurate data (Art. 16)
- **Erasure**: Request deletion of your personal data (Art. 17)
- **Restriction**: Ask us to restrict processing in certain circumstances (Art. 18)
- **Portability**: Receive your data in a machine-readable format (Art. 20)
- **Objection**: Object to processing based on legitimate interests or for direct marketing (Art. 21)
- **Withdraw consent**: Where we process on the basis of consent, you can withdraw at any time — this does not affect processing before withdrawal

To exercise any of these rights, contact: privacy@[domain]
We will respond within 30 days. We may ask for identity verification.

---

7. RIGHT TO OBJECT

Where we process your personal data on the basis of our legitimate interests,
you have the right to object to this processing. We will stop processing unless
we can demonstrate compelling legitimate grounds that override your rights.

For direct marketing: you have an unconditional right to object at any time.

---

8. RIGHT TO COMPLAIN

You have the right to lodge a complaint with the supervisory data protection authority:
[Supervisory authority name, URL, contact]

We would appreciate the opportunity to address your concern before you contact
the supervisory authority.

---

9. AUTOMATED DECISION-MAKING

[If applicable:]
We use automated decision-making [including profiling] in the following contexts:
[Description — logic involved, significance, envisaged consequences]
You have the right to request human review of automated decisions that significantly affect you.

[If not applicable: We do not use automated decision-making or profiling that
produces legal or similarly significant effects.]

---

10. HOW THIS NOTICE MAY CHANGE

We may update this notice to reflect changes in our processing or legal requirements.
Material changes will be communicated [by email / via in-app notification / on our website].
Previous versions are available on request.
```

---

## 4. Layered (Short) Notice Template

For use at collection points — directs data subjects to the full notice.

```
YOUR PRIVACY

[Organisation] will use the information you provide [here / to register / in this form]
to [specific purpose in 1 sentence, e.g., "process your order and send you order updates"].

Legal basis: [Contract / Legitimate interests / Your consent]
Retention: [Period or criteria]

We may share your information with [categories of recipients — brief].

For full details of your rights and how we handle your data:
→ [Full Privacy Notice URL]

[If legitimate interests: You can object to this processing at any time — see our full notice.]
[If consent: You can withdraw consent at any time — see our full notice.]
```

---

## 5. Indirect Collection Notification Template

For use when PII is obtained from a source other than the data subject directly.

```
SUBJECT: Important Privacy Information from [Organisation]

Dear [Name / "Sir or Madam" if names not available],

We are writing because we have obtained your personal data from [source description,
e.g., "our partner [Name]" or "publicly available sources"] and we are processing
it in connection with [specific purpose].

WHAT DATA WE HOLD
[Categories of PII received]

Source of your data: [Source description]
[State: Is it from publicly available sources? Yes / No]

WHY WE PROCESS IT
Purpose: [Specific purpose]
Legal basis: [Art. 6 basis]

HOW LONG WE KEEP IT
[Retention period or criteria]

YOUR RIGHTS
You have the right to access, correct, erase, restrict, or object to this processing.
To exercise your rights: privacy@[domain]

FULL PRIVACY NOTICE
For complete information: [URL]

[If legitimate interests: You may object to this processing by contacting us at the address above.]

[Organisation Legal Name] | [Address] | [Date]
```

---

## 6. Collection Point Audit Record

Maintained by the DPO — records where and how privacy notices are provided at each PII collection point. Reviewed annually.

| Collection Point ID | Description | Processing Activity (RoPA ref) | Notice Type Provided | Notice Version | Where Published / How Delivered | Last Audited | Adequate? |
|--------------------|-------------|-------------------------------|---------------------|----------------|-------------------------------|-------------|-----------|
| CP-001 | Website registration form | ROPA-C-001 | Inline short notice + link to full | PN-EXT v2.1 | Footer of registration form; link to privacy notice | [Date] | Yes |
| CP-002 | App account creation | ROPA-C-002 | Inline notice + link | PN-APP v1.0 | Before submit button | [Date] | Yes |
| CP-003 | Employee onboarding | ROPA-C-010 | Employee privacy notice | PN-EMP v1.1 | Onboarding pack; acknowledgment signed | [Date] | Yes |
| ... | | | | | | | |

---

<!-- QA_VERIFIED: [Date] -->
