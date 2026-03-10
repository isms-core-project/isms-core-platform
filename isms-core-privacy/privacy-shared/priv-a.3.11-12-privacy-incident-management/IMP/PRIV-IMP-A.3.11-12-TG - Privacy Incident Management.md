<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.11-12-TG:privacy:TG:a.3.11-12 -->
**PRIV-IMP-A.3.11-12-TG — Privacy Incident Management — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Privacy Incident Management — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.3.11-12-TG |
| **Related Policy** | PRIV-POL-A.3.11-12 (Privacy Incident Management) |
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

**Review Cycle**: Annual (or after any significant incident)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.3.11-12 (Privacy Incident Management — the governing policy)
- PRIV-IMP-A.3.11-12-UG (Privacy Incident Management — User Guide)
- ISMS-POL-A.5.24-28 (Incident Management Lifecycle)

---

## Purpose of This Guide

This guide provides the **technical structures, register schemas, assessment forms, and notification templates** for privacy incident management. It covers:

- Privacy Breach Register schema
- Personal Data Breach Assessment Form template
- Supervisory Authority Notification templates (GDPR Art. 33; FADP Art. 24)
- Data Subject Notification template (GDPR Art. 34)
- Customer (Controller) Notification template (processor role)
- Log collection and preservation specifications for PII incidents

**Audience**: DPO, Legal/Compliance, CISO, IT Security Team.

---

## 1. Privacy Breach Register

The Privacy Breach Register is owned by the DPO. It is a confidential document — access restricted to DPO, Legal/Compliance, and Executive Management.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Incident ID | Text | Unique reference (e.g., PB-2026-001) |
| Date Discovered | DateTime | When the incident was first detected or reported |
| Date DPO Notified | DateTime | When the DPO became aware |
| Reported By | Text | Name and role of person who reported |
| Incident Description | Text | Nature of the security event |
| Affected System(s) | Text | Systems or data stores involved |
| PII Categories Affected | Multi-select | Ordinary / Financial / Special Category / Sensitive / Unknown |
| Special Category Types | Text | If applicable: health, biometric, etc. |
| Approximate Data Subjects Affected | Text | Number or range |
| Approximate Records Affected | Text | Number or range |
| Breach Type | Multi-select | Confidentiality breach / Integrity breach / Availability breach |
| Role (Controller / Processor) | Enum | Controller / Processor / Both |
| Risk Assessment Outcome | Enum | No risk / Risk / High risk / Under assessment |
| Risk Rationale | Text | Basis for risk level determination |
| Regulatory Notification Required (GDPR Art. 33) | Boolean | Yes / No / Under assessment |
| GDPR Notification Date | DateTime | Date and time notification submitted to DPA |
| DPA Reference Number | Text | Reference number from supervisory authority |
| Data Subject Notification Required (GDPR Art. 34) | Boolean | Yes / No |
| Data Subject Notification Date | Date | Date communication sent to data subjects |
| FADP Notification Required | Boolean | Yes / No |
| FADP Notification Date | DateTime | Date notification submitted to FDPIC |
| Customer Notification Required (processor role) | Boolean | Yes / No / N/A |
| Customer Notification Date | DateTime | If applicable |
| Containment Date | Date | Date breach was contained |
| Resolution Date | Date | Date incident was fully resolved |
| Post-Incident Review Date | Date | Date of post-incident review completion |
| Post-Incident Review Ref | Text | Reference to review report document |
| Root Cause Category | Enum | Human error / Malicious external / Malicious internal / Technical failure / Supplier / Process gap / Unknown |
| Remediation Summary | Text | Key actions taken |
| Outstanding Actions | Text | Actions not yet completed |
| Status | Enum | Under investigation / Contained / Resolved / Closed |

---

## 2. Personal Data Breach Assessment Form

Complete for every incident where PII may have been involved. File in the breach record. Use this form to determine regulatory notification obligations.

```
PERSONAL DATA BREACH ASSESSMENT FORM

Incident ID: _____________
Date of Assessment: _____________
Assessed By (DPO or delegate): _____________

SECTION A — BREACH CHARACTERISATION

1. Nature of the incident:
   [ ] Unauthorised access by external party
   [ ] Unauthorised access by internal party
   [ ] Accidental disclosure (wrong recipient)
   [ ] Loss or theft of device / media / documents
   [ ] System compromise (malware / ransomware)
   [ ] Accidental deletion or corruption
   [ ] Supplier / processor notification
   [ ] Other: ________________________________

2. Was PII definitely accessed, disclosed, altered, lost, or destroyed without authorisation?
   [ ] Yes — confirmed
   [ ] Likely — under investigation
   [ ] Possible — cannot confirm or deny
   [ ] No — PII not affected (document rationale below)

3. If "No": rationale for no PII impact:
   _______________________________________________

SECTION B — SCOPE

4. PII categories involved (tick all that apply):
   [ ] Ordinary personal data (name, address, contact, employment)
   [ ] Financial personal data (bank, payment, salary)
   [ ] Special category: [ ] Health [ ] Biometric [ ] Genetic [ ] Racial/Ethnic origin
                         [ ] Religious/philosophical belief [ ] Political opinion
                         [ ] Trade union membership [ ] Sex life / sexual orientation
   [ ] Sensitive: [ ] Children's data [ ] National ID / SSN [ ] Criminal records
                  [ ] Authentication credentials
   [ ] Unknown — investigation ongoing

5. Approximate number of data subjects affected: _______________
6. Approximate number of records involved: _______________
7. Are affected data subjects identifiable? [ ] Yes [ ] No [ ] Partially

SECTION C — RISK ASSESSMENT

8. For each category below, assess the likely impact on affected data subjects:

| Risk Factor | Assessment | Notes |
|-------------|-----------|-------|
| Financial loss (fraud, identity theft) | Low / Medium / High | |
| Discrimination or reputational damage | Low / Medium / High | |
| Physical harm or distress | Low / Medium / High | |
| Loss of control over personal data | Low / Medium / High | |
| Special category PII exposure | Yes / No | Automatically elevates risk |
| Vulnerable individuals affected | Yes / No / Unknown | Automatically elevates risk |
| Large scale (>1,000 data subjects) | Yes / No | Consider elevating |

9. Overall risk level:
   [ ] No risk — breach is unlikely to result in any risk to data subjects
   [ ] Risk — breach is likely to result in some risk to rights and freedoms
   [ ] High Risk — breach is likely to result in HIGH risk to rights and freedoms

SECTION D — NOTIFICATION DECISIONS

10. GDPR supervisory authority notification (Art. 33):
    [ ] Required — risk or high risk identified; notify within 72 hours
    [ ] Not required — no risk to rights and freedoms (document rationale in Q3/Q8)
    [ ] Delayed notification — partial notification submitted within 72 hours; supplementary notification to follow
    Target notification time: _____________  Actual notification time: _____________
    Hours from awareness to notification: _______ (target: ≤ 72 hours)

11. GDPR data subject communication (Art. 34):
    [ ] Required — HIGH risk identified; notify without undue delay
    [ ] Not required — not high risk (or appropriate safeguard in place per Art. 34(3))
    [ ] Law enforcement consideration — coordinate with Legal before notifying
    Target communication date: _____________

12. FADP FDPIC notification (Art. 24):
    [ ] Required — likely high risk to personality or fundamental rights
    [ ] Not required
    Target notification date: _____________

13. Customer notification (processor role only):
    [ ] Required — notify customer without undue delay (max 24 hours per agreement)
    [ ] Not applicable — acting as controller only

ASSESSMENT CONCLUSION AND SIGN-OFF

DPO Signature: _________________________ Date: _____________
Legal/Compliance Review: _________________________ Date: _____________
```

---

## 3. GDPR Article 33 Supervisory Authority Notification Template

```
PERSONAL DATA BREACH NOTIFICATION
Under GDPR Article 33

To: [Name of Lead Supervisory Authority / DPA]
Date: [Date]
Time: [Time and timezone]
Hours since awareness: [Number]

Organisation: [Organisation Legal Name]
Address: [Registered address]
Country: [Country of main establishment]

Data Protection Officer Contact:
  Name: [DPO Name]
  Email: [DPO Email]
  Phone: [DPO Phone]

ARTICLE 33(3)(a) — NATURE OF THE BREACH
[Describe: type of breach (confidentiality / integrity / availability); source / cause;
systems involved; how it was discovered; date and time of breach (if known).]

ARTICLE 33(3)(b) — CATEGORIES AND APPROXIMATE NUMBER OF DATA SUBJECTS
[Categories of data subjects affected (e.g., customers, employees, users).
Approximate number of individuals affected: [Number or range].]

ARTICLE 33(3)(b) — CATEGORIES AND APPROXIMATE NUMBER OF RECORDS
[Categories of personal data involved (e.g., name, email, health data).
Approximate number of records: [Number or range].]

ARTICLE 33(3)(c) — LIKELY CONSEQUENCES
[Describe the likely consequences of the breach for data subjects, including:
risk of identity theft, fraud, financial loss, discrimination, distress, reputational damage,
loss of confidentiality, or other significant adverse effects.]

ARTICLE 33(3)(d) — MEASURES TAKEN OR PROPOSED
[Describe: containment actions taken; remediation measures in progress or planned;
measures to address adverse consequences for data subjects.]

SUPPLEMENTARY INFORMATION TO FOLLOW
[ ] Yes — additional information will be provided as investigation continues
[ ] No — all available information is included in this notification

This notification is submitted in accordance with GDPR Article 33.
[Organisation Legal Name] | [DPO Name] | [Date]
```

---

## 4. GDPR Article 34 Data Subject Communication Template

```
NOTICE OF PERSONAL DATA BREACH

Dear [Data Subject Name / "Valued Customer" if names unavailable],

We are writing to inform you of a security incident that may affect your personal data.

WHAT HAPPENED
[Clear, plain-language description of the incident. Avoid technical jargon.
Date and approximate time of the incident if known.]

WHAT PERSONAL DATA WAS INVOLVED
[List the categories of personal data that may have been accessed or disclosed.
Be specific but avoid unnecessary alarm. Example: your name, email address, and account number.]

WHAT WE ARE DOING
[Describe the steps already taken to contain and address the incident.
Describe any measures you are taking to prevent recurrence.]

WHAT YOU CAN DO
[Practical advice relevant to this breach. Examples:
- Change your password if account credentials were involved
- Monitor your bank account for unusual activity if financial data was involved
- Be alert for phishing communications if contact data was involved
- Contact [helpline / email] if you have questions]

FOR FURTHER INFORMATION
[Organisation's Data Protection Officer contact:
Name: [DPO Name] | Email: [DPO Email] | Phone: [DPO Phone]

You also have the right to contact your data protection supervisory authority if you have concerns:
[Supervisory authority name and contact]]

We sincerely apologise for any concern or inconvenience this may cause.
[Organisation Name]
[Date]
```

---

## 5. Processor-to-Controller Breach Notification Template

For use when [Organisation] acts as PII Processor and must notify the customer (controller):

```
PERSONAL DATA BREACH NOTIFICATION — PROCESSOR TO CONTROLLER
CONFIDENTIAL

To: [Customer DPO / Privacy Contact Name]
Organisation: [Customer Legal Name]
Date and Time: [ISO 8601 timestamp]

From: [Organisation Legal Name]
Contact: [DPO Name] | [DPO Email] | [DPO Phone]

Pursuant to our Data Processing Agreement (ref: [Agreement reference], clause [X]),
we are notifying you of a security incident affecting your personal data.

INCIDENT SUMMARY
Date/Time Detected: [Timestamp]
Date/Time [Organisation] Became Aware: [Timestamp]
Hours to Notification: [Number] (contractual requirement: max 24 hours)

Nature of Incident: [Brief description]

YOUR DATA AFFECTED
PII Categories: [List]
Approximate Data Subjects: [Number]
Approximate Records: [Number]

CURRENT STATUS
[ ] Under active investigation
[ ] Contained — investigation continuing
[ ] Contained and resolved

ACTIONS TAKEN
[List containment and remediation actions taken to date.]

ACTIONS IN PROGRESS
[List ongoing actions.]

TO SUPPORT YOUR REGULATORY OBLIGATIONS
We are prepared to provide further information to support your Article 33 assessment
and, if required, your Article 34 notifications to data subjects.

Next update will be provided by: [Timestamp]

[DPO Signature]
[Organisation Legal Name] | [Date]
```

---

## 6. Log Collection Specification for PII Incidents

When a PII incident is triggered, IT Security Team must collect and preserve the following log types:

| Log Type | Minimum Retention Period | Priority |
|----------|-------------------------|----------|
| Authentication logs (login / logout / failed login) for affected systems | Preserve immediately; retain 5 years | Critical |
| Database query logs for affected PII data stores | Preserve immediately; retain 5 years | Critical |
| File access logs for affected PII repositories | Preserve immediately; retain 5 years | Critical |
| Network traffic logs (ingress/egress for affected systems) | Preserve immediately; retain 3 years | High |
| Email server logs (relevant date range) | Preserve immediately; retain 3 years | High |
| Privileged access session logs | Preserve immediately; retain 5 years | Critical |
| Application logs for PII processing pipelines | Preserve immediately; retain 3 years | High |
| Cloud provider activity logs (CloudTrail, Azure Monitor, etc.) | Preserve immediately; retain 3 years | High |
| SIEM alerts and correlation events for incident window | Preserve immediately; retain 3 years | High |

**Preservation method**: Export and archive to write-protected storage before any remediation activity that may overwrite logs. Hash exported logs and retain hash values with the incident record to demonstrate integrity.

---

<!-- QA_VERIFIED: [Date] -->
