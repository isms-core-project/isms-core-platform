<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.5.2-5-TG:privacy:TG:a.1.5.2-5 -->
**PRIV-IMP-A.1.5.2-5-TG — PII Transfer and Disclosure — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | PII Transfer and Disclosure — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.1.5.2-5-TG |
| **Related Policy** | PRIV-POL-A.1.5.2-5 (PII Transfer and Disclosure) |
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

- PRIV-POL-A.1.5.2-5 (PII Transfer and Disclosure — the governing policy)
- PRIV-IMP-A.1.5.2-5-UG (PII Transfer and Disclosure — User Guide)
- PRIV-IMP-A.1.2.6-9-TG (Privacy Governance and Records — RoPA schema with transfer fields)

---

## Purpose of This Guide

This guide provides the **technical structures, register schemas, and templates** for PII transfer and disclosure management. It covers:

- Transfer Country Register schema
- International Transfer Register schema (TIA records)
- Transfer Impact Assessment (TIA) template
- Transfer Record schema (ad-hoc transfers)
- Disclosure Register schema

**Audience**: DPO, Legal/Compliance, IT Security Team.

---

## 1. Transfer Country Register

Documents all countries and international organisations to which PII may be transferred, with the applicable transfer mechanism and PII scope. Maintained by the DPO as part of the PIMS documentation set.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Country ID | Text | Unique reference (e.g., TCR-001) |
| Country / Territory | Text | Name of destination country or international organisation |
| Transfer Mechanism | Enum | Adequacy Decision / SCCs (EU 2021) / SCCs (Swiss FDPIC) / BCRs / Art. 49 Derogation / Other |
| Adequacy Status (if applicable) | Enum | Adequate (EU) / Adequate (CH) / Both / Not Applicable |
| SCC Module (if applicable) | Enum | Module 1 (C2C) / Module 2 (C2P) / Module 3 (P2P) / Module 4 (P2C) |
| SCC Agreement Reference | Text | Reference to the signed SCC agreement |
| TIA Required | Boolean | Yes / No |
| TIA Reference | Text | Linked International Transfer Register entry |
| PII Categories Transferred | Text | Categories of PII that may be transferred to this destination |
| Processing Activities | Text | RoPA activity IDs involving transfers to this destination |
| Supplementary Measures | Text | Any supplementary technical or contractual measures in place |
| First Transfer Date | Date | Date on which first transfer to this destination occurred |
| Last Reviewed | Date | Date this entry was last reviewed |
| Status | Enum | Active / Suspended / Closed |
| Notes | Text | Adequacy history, pending changes, risk flags |

### Reference: Current Adequacy Decisions (at time of publication)

*Note: Adequacy status changes. DPO must verify current status from official supervisory authority sources before relying on this reference.*

| Country | EU Adequacy | Swiss Adequacy |
|---------|------------|----------------|
| United Kingdom | Yes (adequacy decision, subject to review) | Yes |
| Canada (PIPEDA commercial sector) | Yes | Yes |
| Japan | Yes | Yes |
| South Korea | Yes | Pending (check current status) |
| New Zealand | Yes | Yes |
| Israel | Yes | Yes |
| Switzerland | Yes (from EU perspective) | N/A (domestic) |
| United States | Partial — EU-US Data Privacy Framework (DPF) | Check FDPIC for CH-US |

---

## 2. International Transfer Register

Maintains the detailed record of each international transfer arrangement, including TIA documentation. One entry per transfer relationship. Maintained by DPO.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Transfer ID | Text | Unique reference (e.g., ITR-001) |
| Transfer Country Register Ref | Text | Linked TCR entry |
| Recipient Name | Text | Name of the receiving organisation |
| Recipient Jurisdiction | Text | Country/territory of recipient |
| Recipient Role | Enum | Processor / Joint Controller / Third Party Controller / Regulatory Authority |
| Transfer Mechanism | Enum | Adequacy / SCCs / BCRs / Derogation |
| Agreement Reference | Text | Reference to processor agreement or DPA containing the transfer mechanism |
| TIA Conducted | Boolean | Yes / No |
| TIA Date | Date | Date TIA was completed |
| TIA Outcome | Enum | Transfer proceeds / Transfer proceeds with supplementary measures / Transfer suspended |
| Supplementary Measures | Text | Measures applied (if any) |
| PII Categories | Text | PII categories included in this transfer |
| Processing Activities | Text | RoPA activity IDs |
| Transfer Frequency | Enum | Continuous / Daily / Weekly / Monthly / Ad-hoc |
| Transfer Volume (approx.) | Text | Approximate volume or record count |
| First Transfer Date | Date | Date of first transfer |
| Last Reviewed | Date | Last TIA review date |
| Status | Enum | Active / Suspended / Closed |
| Notes | Text | Open items, pending SCC renewals, supplementary measure reviews |

---

## 3. Transfer Impact Assessment Template

Completed by the DPO for each transfer relationship where SCCs or other contractual mechanisms are used.

```
TRANSFER IMPACT ASSESSMENT (TIA)

TIA Reference: TIA-[NNN]
Date: _____________
DPO: _____________

PART 1 — TRANSFER DETAILS

Recipient Organisation: _____________________________________________
Recipient Jurisdiction: _____________________________________________
Recipient Role: [ ] Processor  [ ] Joint Controller  [ ] Third Party Controller
Transfer Mechanism: [ ] SCCs (EU 2021 — Module ___) [ ] BCRs [ ] Other: _____________
Agreement Reference: _____________________________________________
PII Categories Involved: _____________________________________________
Processing Activities: _____________________________________________
Transfer Frequency: [ ] Continuous  [ ] Regular  [ ] Ad-hoc
Approximate Volume: _____________________________________________

PART 2 — DESTINATION COUNTRY LEGAL FRAMEWORK ASSESSMENT

2.1 Government access / surveillance laws
Describe any laws in the destination country that could require the recipient to
disclose PII to government authorities, including laws broader than comparable
EU/EFTA standards:
___________________________________________________________________
Risk assessment: [ ] Low (equivalent to EEA)  [ ] Medium  [ ] High
Source/reference: _____________________________________________

2.2 Data subject rights enforcement
Can data subjects in the destination country enforce rights effectively?
[ ] Yes — enforceable rights through independent authority or courts
[ ] Partial — limited enforcement mechanisms
[ ] No — no meaningful enforcement mechanism
Notes: _____________________________________________

2.3 Recipient compliance capability
Is the recipient able to fulfil its obligations under the SCC module?
[ ] Yes — no legal impediment identified
[ ] Potentially not — describe impediment: _____________________________________________

PART 3 — SUPPLEMENTARY MEASURES (if required)

If Part 2 identified gaps, the following supplementary measures are applied:

Technical measures:
[ ] Encryption in transit (TLS 1.2+) — keys held by [Organisation]
[ ] Encryption at rest — keys held by [Organisation], not accessible to recipient
[ ] Pseudonymisation before transfer
[ ] Other: _____________________________________________

Contractual measures:
[ ] Obligation to notify [Organisation] of any government access request
[ ] Prohibition on transfer to sub-processors in additional high-risk jurisdictions
[ ] Enhanced audit rights
[ ] Other: _____________________________________________

Organisational measures:
[ ] Transfer limited to minimum PII categories
[ ] Access by recipient limited to minimum personnel
[ ] Other: _____________________________________________

PART 4 — CONCLUSION

[ ] Transfer proceeds — no gap identified; SCCs provide adequate protection
[ ] Transfer proceeds with supplementary measures — measures documented above;
    effective protection achieved
[ ] Transfer cannot proceed — effective protection cannot be achieved;
    see escalation note below

Escalation (if applicable): _____________________________________________

DPO: _________________________ Date: _____________
Legal/Compliance Review: _________________________ Date: _____________
```

---

## 4. Transfer Record Schema (Ad-Hoc Transfers)

For one-time or irregular transfers not covered by an ongoing processor agreement. Maintained by the DPO.

| Field | Type | Description |
|-------|------|-------------|
| Transfer ID | Text | Unique reference (e.g., TRANS-2026-001) |
| Date | Date | Date of transfer |
| Initiating Role | Text | Who initiated the transfer |
| Recipient Name | Text | Receiving organisation or individual |
| Recipient Jurisdiction | Text | Country |
| Recipient Role | Enum | Processor / Joint Controller / Third Party Controller / Data Subject / Regulatory Authority |
| Governing Agreement | Text | Reference to DPA, processor agreement, or legal authority for the transfer |
| PII Categories Transferred | Text | Categories of PII included |
| Volume (approx.) | Text | Approximate record count or data volume |
| Transfer Method | Enum | Encrypted email / SFTP / API / Portal / Physical / Other |
| Transfer Mechanism (cross-border) | Text | Adequacy / SCCs / BCR / Derogation / N/A (same jurisdiction) |
| Purpose | Text | Why this transfer occurred |
| DPO Approval | Boolean | Yes / No |
| Approval Date | Date | Date DPO approved this transfer |
| Notes | Text | Circumstances, follow-up actions |

---

## 5. Disclosure Register

Records all disclosures of PII to third parties. Maintained by the DPO. Classified RESTRICTED.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Disclosure ID | Text | Unique reference (e.g., DISC-2026-001) |
| Date | Date | Date of disclosure |
| Recipient Name | Text | Name of the receiving third party |
| Recipient Type | Enum | Processor / Professional Advisor / Regulatory Authority / Law Enforcement / Other Controller / Other |
| PII Disclosed | Text | Categories of PII and approximate scope |
| Data Subjects Affected (approx.) | Text | Approximate number or description |
| Purpose of Disclosure | Text | Specific reason for the disclosure |
| Legal Basis for Disclosure | Text | Art. 6 basis or legal obligation reference |
| Cross-Border | Boolean | Yes / No |
| Transfer Mechanism (if cross-border) | Text | Mechanism reference |
| DPO Authorised | Boolean | Yes / No |
| Legal/Compliance Sign-Off (for legal obligation disclosures) | Boolean | Yes / No / Not Applicable |
| Data Subject Notified | Enum | Yes / No / Prohibited by law / Not Required |
| Notification Date | Date | If notified: date |
| Governing Agreement Reference | Text | Processor agreement, DPA, or order reference |
| Notes | Text | Legal hold status, restrictions on notification, follow-up actions |

---

<!-- QA_VERIFIED: [Date] -->
