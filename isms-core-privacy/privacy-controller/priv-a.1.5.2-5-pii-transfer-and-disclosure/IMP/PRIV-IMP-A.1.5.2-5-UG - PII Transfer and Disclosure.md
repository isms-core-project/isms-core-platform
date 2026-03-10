<!-- ISMS-CORE:IMP:PRIV-IMP-A.1.5.2-5-UG:privacy:UG:a.1.5.2-5 -->
**PRIV-IMP-A.1.5.2-5-UG — PII Transfer and Disclosure — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | PII Transfer and Disclosure — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.1.5.2-5-UG |
| **Related Policy** | PRIV-POL-A.1.5.2-5 (PII Transfer and Disclosure) |
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
| 1.0 | [Date to be set] | DPO | Initial user guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.1.5.2-5 (PII Transfer and Disclosure — the governing policy)
- PRIV-IMP-A.1.5.2-5-TG (PII Transfer and Disclosure — Technical Guide)
- PRIV-IMP-A.1.2.6-9-UG (Privacy Governance and Records — processor agreement engagement)
- PRIV-IMP-A.1.3.5-10-UG (Data Subject Rights — disclosures relevant to SAR responses)

---

## Purpose of This Guide

This guide explains **how to implement** the PII transfer and disclosure obligations of PRIV-POL-A.1.5.2-5. It covers how to identify the legal basis for cross-border transfers, how to maintain the Transfer Country Register, how to conduct a Transfer Impact Assessment, and how to record transfers and disclosures.

**Who this guide is for**: DPO, Legal/Compliance, Procurement, IT Security Team.

**Controller-only**: This guide applies only to processing activities where [Organisation] acts as PII Controller.

---

## Part 1 — Identifying the Basis for Cross-Border Transfers (A.1.5.2)

### 1.1 What Constitutes a Cross-Border PII Transfer

A cross-border transfer occurs when PII is sent to, or accessed from, a recipient in a country outside the controller's jurisdiction. This includes:

- Sending data files to a supplier or partner located in another country
- Using a cloud service or SaaS platform where data is processed in data centres outside the EEA or Switzerland
- Enabling remote access to PII systems by personnel in other countries
- Forwarding emails containing PII to recipients outside the jurisdiction

**Note on cloud services**: If a cloud provider processes PII in data centres located outside the EEA or Switzerland, this is a cross-border transfer even if the contractual relationship is with a local entity. The DPO must confirm data centre location before any cloud service agreement is signed.

### 1.2 Transfer Mechanism Selection

When a new cross-border transfer is identified, the DPO selects the appropriate transfer mechanism:

**Step 1 — Adequacy check**
Check whether the destination country has an adequacy decision from the EU Commission (for GDPR) or adequate protection status from the Swiss FDPIC (for FADP). Adequate countries require no additional safeguards. Current adequacy lists are maintained by the DPO from supervisory authority sources.

**Step 2 — Standard Contractual Clauses (SCCs)**
Where no adequacy decision exists, the primary mechanism is SCCs:
- **EU transfers**: Use the EU Commission SCCs (2021 Implementing Decision) — the correct module depends on the relationship (controller-to-controller, controller-to-processor)
- **Swiss transfers**: Use the Swiss SCCs approved by the FDPIC
- SCCs must be incorporated into the supplier/processor agreement — they are not signed separately in most cases; they are embedded or referenced with a signed acknowledgment

**Step 3 — Transfer Impact Assessment (TIA)**
Where SCCs are used, the DPO conducts a TIA (see Section 1.3) to assess whether the legal framework in the destination country provides essentially equivalent protection. The TIA is documented before the transfer commences.

**Step 4 — Art. 49 derogations (last resort)**
Derogations are available for isolated, specific circumstances (explicit consent for the specific transfer, vital interests, legal claims, public register data). They are NOT appropriate for systematic or routine transfers. If a derogation appears to be the only available basis, the DPO escalates to Legal/Compliance before relying on it.

### 1.3 Conducting a Transfer Impact Assessment (TIA)

A TIA is required when relying on SCCs or other contractual mechanisms for a cross-border transfer. The DPO (with Legal/Compliance input) conducts the TIA:

**TIA assessment steps:**

1. **Identify the transfer**: Document the transfer — parties, countries involved, PII categories, purpose, volume
2. **Verify the transfer mechanism**: Confirm the correct SCC module is in place
3. **Assess the destination country's legal framework**: Review whether laws in the destination country (particularly surveillance, government access, or data disclosure laws) would prevent the recipient from meeting SCC obligations — standard resources include DPA guidance on specific third countries
4. **Identify supplementary measures if needed**: If the legal framework creates a gap, identify and document supplementary measures that close the gap:
   - Technical: encryption in transit and at rest (with keys held by [Organisation], not the recipient); pseudonymisation before transfer
   - Contractual: enhanced confidentiality obligations; obligation to notify [Organisation] of government access requests
   - Organisational: access limited to minimum personnel; minimum transfer scope
5. **Record the outcome**: Document the conclusion (transfer proceeds / transfer proceeds with supplementary measures / transfer cannot proceed)

If the TIA concludes that effective protection cannot be achieved despite supplementary measures, the transfer must not proceed. The DPO escalates to Executive Management and Legal/Compliance.

---

## Part 2 — Maintaining the Transfer Country Register (A.1.5.3)

### 2.1 Building the Initial Register

At PIMS implementation, the DPO maps all existing cross-border transfers from the RoPA (each processing activity includes a transfer destination field). From this, the Transfer Country Register is built, listing:

- All countries where PII is transferred or processed on [Organisation]'s behalf
- The transfer mechanism for each country
- The categories of PII that may be transferred there
- The processing activities involved

### 2.2 Ongoing Register Maintenance

The Transfer Country Register is a living document. It must be updated:

- When a new supplier or service in a new country is onboarded (Procurement triggers DPO review before contract signature)
- When a supplier moves its data centre to a new country (requires re-assessment)
- When adequacy status for a destination country changes (DPO monitors supervisory authority announcements)
- Annually as part of the general RoPA review

**Procurement gate**: No supplier agreement involving PII processing in a new country may be signed without DPO confirmation of the transfer mechanism. Procurement includes a "transfer country review" step in the supplier onboarding process.

### 2.3 Responding to Adequacy Status Changes

If the EU Commission withdraws an adequacy decision for a country where [Organisation] has active transfers, the DPO must:

1. Within 5 business days of the decision: identify all affected transfers from the Transfer Country Register
2. Within 15 business days: put SCCs in place for each affected transfer, conduct TIAs, implement supplementary measures as required
3. Notify affected suppliers of the change and obtain SCC signatures
4. Update the Transfer Country Register and inform Legal/Compliance
5. Update the privacy notice if the change is material

---

## Part 3 — Recording Transfers (A.1.5.4)

### 3.1 What Must Be Recorded

Every transfer of PII to or from a third party must be recorded. A transfer is any movement of PII to a party outside [Organisation]'s direct operational control — including to processors, joint controllers, third-party controllers, and regulators.

For routine ongoing transfers (e.g., a SaaS platform that regularly processes PII under a processor agreement), the transfer is documented at the activity level in the RoPA rather than as individual transaction-level records, unless specific log records are required.

For one-time or ad-hoc transfers (e.g., sharing a specific dataset with a new party, responding to a regulator request), a specific Transfer Record is created.

### 3.2 Supporting Data Subject Rights via Transfer Records

Transfer records directly support data subject rights:

- **Subject access requests**: Data subjects are entitled to know the recipients (or categories of recipients) of their PII — transfer records enable this response
- **Erasure requests**: When PII is erased, all third parties who received the PII must be notified — transfer records identify who to notify
- **Rectification requests**: Similarly, rectification must be propagated to recipients

Data Owners and the DPO consult transfer records when processing these DSR types.

---

## Part 4 — Recording Disclosures (A.1.5.5)

### 4.1 What Is a Disclosure

A disclosure is any communication of PII to a third party. All disclosures must be recorded:

| Disclosure Type | Examples |
|----------------|---------|
| **Routine processor disclosures** | PII sent to payroll provider, email platform, cloud hosting provider |
| **Professional advisor disclosures** | Sharing PII with legal counsel, auditors, consultants for a specific engagement |
| **Regulatory / law enforcement disclosures** | Responding to a court order, tax authority request, law enforcement access request |
| **One-time business disclosures** | Sharing customer data with an acquirer during M&A due diligence |
| **Emergency disclosures** | Sharing PII where vital interests require disclosure |

### 4.2 Recording a Disclosure

When a disclosure is about to occur or has just occurred:

1. The person making the disclosure notifies the DPO and Data Owner (or DPO logs the disclosure where it originates from the DPO's own functions)
2. The DPO creates a Disclosure Register entry (see PRIV-IMP-A.1.5.2-5-TG for schema)
3. For mandatory disclosures (legal obligation), Legal/Compliance confirms the legal obligation reference and whether [Organisation] may or must notify the data subject
4. For discretionary disclosures (e.g., professional advisor), the DPO confirms the lawful basis for disclosure and whether a data processing agreement is needed

### 4.3 Legal Obligation Disclosures

When [Organisation] receives a request for PII from a law enforcement authority, regulator, or court:

1. The request is forwarded to the DPO and Legal/Compliance immediately
2. Legal/Compliance confirms the legal authority for the request (court order, statutory power, voluntary cooperation)
3. The minimum necessary scope of disclosure is confirmed — only PII required by the order/request is shared
4. Whether [Organisation] is legally permitted to notify the data subject of the disclosure is confirmed (some orders include a prohibition on notification)
5. Disclosure is executed and logged in the Disclosure Register

No PII is disclosed under a legal obligation request without Legal/Compliance sign-off.

---

## Evidence Checklist

- [ ] Transfer Country Register — all cross-border transfer destinations documented with mechanism and PII categories
- [ ] TIA records — documented for all SCC-based transfers
- [ ] SCC agreements — executed and filed for all non-adequate country transfers
- [ ] RoPA transfer section — destinations and safeguards recorded per processing activity
- [ ] Transfer Records — ad-hoc and one-time transfers logged
- [ ] Disclosure Register — all disclosures to third parties recorded
- [ ] Procurement gate records — DPO review completed before new international supplier engagement
- [ ] Annual register review — Transfer Country Register reviewed and updated

---

<!-- QA_VERIFIED: [Date] -->
