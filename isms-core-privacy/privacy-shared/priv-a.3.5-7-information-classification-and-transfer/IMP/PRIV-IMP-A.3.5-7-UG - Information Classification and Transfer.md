<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.5-7-UG:privacy:UG:a.3.5-7 -->
**PRIV-IMP-A.3.5-7-UG — Information Classification and Transfer — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Classification and Transfer — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.3.5-7-UG |
| **Related Policy** | PRIV-POL-A.3.5-7 (Information Classification and Transfer) |
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

- PRIV-POL-A.3.5-7 (Information Classification and Transfer — the governing policy)
- PRIV-IMP-A.3.5-7-TG (Information Classification and Transfer — Technical Guide)
- ISMS-POL-A.5.12-13 (Information Classification and Labelling — ISMS framework parallel)
- ISMS-POL-A.5.14 (Information Transfer — ISMS framework parallel)
- PRIV-POL-A.3.11-12 (Privacy Incident Management — for transfer breach response)

---

## Purpose of This Guide

This guide explains **how to implement** the classification, labelling, and transfer requirements of PRIV-POL-A.3.5-7 from an operational perspective. It covers:

- How to classify PII-containing information correctly, including when to apply minimum floors and aggregation rules
- How to label PII-containing documents, emails, files, and systems
- How to transfer PII internally and externally, including cross-border transfers
- How to set up and maintain transfer agreements and the International Transfer Register

**Who this guide is for**: Data Owners, Privacy Champions, DPO, all personnel who handle PII in any format, Legal/Compliance (for cross-border transfer sections).

---

## Part 1 — Classifying PII-Containing Information (A.3.5)

### 1.1 Quick Classification Decision Guide

When you create, receive, or work with information that may contain PII, use this sequence:

**Step 1 — Does it contain PII?**
Does the information directly identify, or could it reasonably be used to identify, a living natural person? If yes → PII present. If unsure → treat as PII and escalate to your Privacy Champion or Data Owner.

**Step 2 — What category of PII?**

| If the information contains... | Category |
|-------------------------------|----------|
| Name, address, phone, email, employment record, professional profile | Ordinary personal data |
| Bank account, salary, payment history, credit record | Financial personal data |
| Health/medical data, biometric data, genetic data, racial or ethnic origin, religious or philosophical belief, political opinion, trade union membership, sex life or sexual orientation | Special category PII |
| Children's data (under 16), national ID numbers, criminal convictions, authentication credentials, data about vulnerable persons | Sensitive personal data |

**Step 3 — Apply the minimum floor**

| PII Category | Minimum Classification |
|-------------|----------------------|
| Ordinary personal data | CONFIDENTIAL (never below) |
| Financial personal data | CONFIDENTIAL (never below) |
| Special category PII | RESTRICTED (never below) |
| Sensitive personal data | RESTRICTED (never below) |

If the existing ISMS classification is already higher than the PII minimum floor, keep the higher classification. The PII floor can only push the classification up, never down.

**Step 4 — Check the aggregation rule**
If you are combining datasets (e.g., linking a name list to a pseudonymised dataset, or joining tables from different sources) and the combined result allows identification of individuals — classify the combined dataset at minimum CONFIDENTIAL, or RESTRICTED if special category PII can be derived.

**Step 5 — Record the classification**
Record the classification decision in the Classification Register (see PRIV-IMP-A.3.5-7-TG for register template). For RESTRICTED datasets, note the Data Owner and DPO approval.

### 1.2 When to Escalate Classification Questions

Escalate to your Privacy Champion or Data Owner when:
- You are unsure whether information qualifies as PII
- An aggregation rule may apply and you need a determination
- You believe an existing dataset is misclassified
- A new processing activity or system is being introduced that will handle PII

Escalate directly to the DPO when:
- You believe RESTRICTED (special category) PII is involved
- A classification review trigger has been identified (e.g., processing purpose has changed)
- A supervisory authority has provided guidance that may require reclassification

### 1.3 Classification Reviews

Data Owners review PII classification at minimum annually and on the following triggers:
- Processing purpose has changed
- Legal basis for processing has changed
- A DPIA has been completed that identifies reclassification needs
- DPA guidance or case law materially changes how a PII category is interpreted

Review outcome: confirm existing classification is correct, or initiate reclassification and update the Classification Register.

---

## Part 2 — Labelling PII-Containing Information (A.3.6)

### 2.1 What to Label and How

Every item of information classified CONFIDENTIAL or RESTRICTED due to PII content must carry:
1. The classification label (CONFIDENTIAL or RESTRICTED)
2. A PII indicator

Apply labels consistently across all formats:

**Documents (Word, PDF, presentations)**:
- Classification label in the header or footer on every page (per ISMS-POL-A.5.12-13 standard)
- "Contains Personal Data" in the document header or in document properties metadata
- For special category PII: add "Contains Special Category Personal Data" or use the `[SPD]` indicator

**Emails**:
- Add `[PD]` to the subject line when the email body or attachment contains ordinary PII
- Add `[SPD]` to the subject line when the email body or attachment contains special category PII
- Classification label in the email footer (consistent with ISMS labelling policy)

**Spreadsheets and databases**:
- Sheet-level or table-level label where the structure allows
- If the system cannot apply visual labels, ensure the Data Asset Register records the PII status (see Part 3)
- For exports from PII databases: apply document labels to the exported file

**Physical documents**:
- "PERSONAL DATA" stamp or printed indicator on the cover and first page
- Special category documents: "SPECIAL CATEGORY PERSONAL DATA" stamp

**File and folder names**:
Where system conventions allow and it is consistent with existing naming standards, use the suffixes `_PII` (ordinary PII) or `_SPD` (special category PII) in file or folder names for PII-containing materials.

### 2.2 Unlabelled PII — What to Do

If you encounter PII-containing information that is not labelled (e.g., a legacy document, an inherited dataset, a file received from a third party):

1. Apply the appropriate PII label immediately if you are the document owner or custodian
2. If you are not the document owner, notify the Data Owner or Privacy Champion
3. Record the unlabelled PII finding in the Classification Register for follow-up

Do not transfer, forward, or share unlabelled PII-containing information before labelling is applied.

### 2.3 System-Level PII Labelling

Systems, databases, and repositories that process PII must be registered in the Data Asset Register with PII metadata. This is a responsibility of the System Owner, supported by the DPO:

- `pii_present`: yes/no
- `pii_categories`: list of applicable PII categories
- `special_category`: yes/no
- `jurisdictional_scope`: which data subjects (EU, CH, UK, etc.)

System Owners update the Data Asset Register when a system is introduced, when its processing activities change, or when a DPIA is completed. See PRIV-IMP-A.3.5-7-TG for the Data Asset Register structure.

---

## Part 3 — Transferring PII (A.3.7)

### 3.1 Before You Transfer PII — Checklist

Before transferring any PII (internal or external), confirm:

- [ ] **Purpose**: Does the recipient have a documented legitimate need for this specific PII?
- [ ] **Authorisation**: Are you authorised to transfer this PII? (Check with your Data Owner or the DPO if unsure)
- [ ] **Agreement**: For external transfers — is there a current signed agreement (processor agreement, joint controller arrangement, or other transfer agreement) in the Transfer Agreement Register?
- [ ] **Method**: Is the transfer method appropriate for the classification level? (See table in PRIV-POL-A.3.5-7 Section A.3.7)
- [ ] **Cross-border**: If the transfer is to a different country — has a cross-border transfer mechanism (adequacy, SCCs, BCRs) been confirmed and documented in the International Transfer Register?

If any box cannot be checked: stop and contact the DPO before proceeding.

### 3.2 Internal Transfers

Internal transfers are transfers of PII between teams, departments, systems, or processing environments within the organisation.

**For CONFIDENTIAL PII**:
- Transfer using encrypted channels (encrypted email, approved internal platform, TLS-secured system API)
- No need to log individual transfers unless the system generates logs automatically

**For RESTRICTED / special category PII**:
- Transfer using encrypted channels — same requirement as above
- Create a transfer log entry: date, sender, recipient, purpose, PII categories transferred (see PRIV-IMP-A.3.5-7-TG for log template)
- If transferring to a processing environment in a different jurisdiction: treat as cross-border transfer (see 3.4)

### 3.3 External Transfers — Setting Up an Agreement

Before establishing any ongoing external relationship that involves transfer of PII, the DPO must be notified and the following completed:

**For processor relationships** (supplier processes PII on your behalf):
1. Confirm the supplier requires access to PII to provide their service
2. DPO categorises the supplier as PII Processor
3. Execute a processor agreement (Data Processing Agreement / DPA) per GDPR Article 28 before any PII transfer
4. Register the agreement in the Transfer Agreement Register
5. Transfer may commence only after the signed agreement is on file

**For joint controller arrangements**:
1. DPO assesses whether joint controllership applies (both parties determine processing purposes)
2. DPO drafts joint controller arrangement per GDPR Article 26
3. Arrangement signed by Executive Management on both sides
4. Register the arrangement in the Transfer Agreement Register

**For ad hoc disclosures** (one-time transfers to recipients, public authorities, auditors, etc.):
1. Confirm the legal basis for disclosure (instruction from customer, legal obligation, legitimate interest, etc.)
2. Document the disclosure in the Record of Processing Activities (RoPA)
3. For non-routine disclosures: DPO reviews before the transfer occurs
4. Retain a record of the disclosure

### 3.4 Cross-Border / International Transfers

Any transfer of PII to a country or organisation outside the EEA (for EU GDPR) or outside Switzerland (for CH FADP) requires a valid transfer mechanism. The DPO is responsible for confirming and documenting the mechanism.

**Process for new cross-border transfer destinations**:

1. Data Owner or Privacy Champion identifies a new cross-border transfer (new supplier, new system, new processing location)
2. Notify the DPO immediately — do not commence the transfer until approved
3. DPO checks whether the destination country has an adequacy decision (EU Commission or Swiss FDPIC)
4. If adequacy exists: document adequacy basis in the International Transfer Register → transfer may proceed
5. If no adequacy: DPO initiates Transfer Impact Assessment (TIA) to evaluate whether SCCs or BCRs can be used with or without supplementary measures
6. DPO selects transfer mechanism, documents supplementary measures if required, and approves the transfer
7. International Transfer Register is updated before transfer commences

**Cloud services**: If a new cloud service processes PII in data centres outside the EEA/Switzerland, this is a cross-border transfer and must go through the same process. Confirm data residency with the cloud provider before onboarding.

### 3.5 Physical PII Transfer

For physical transfer of PII-containing documents or media:

| Classification | Method |
|---------------|--------|
| CONFIDENTIAL PII | Sealed envelope, tracked delivery, recipient signature required |
| RESTRICTED / Special category | Double-sealed envelope, bonded courier or hand delivery, chain of custody documentation |

Chain of custody documentation includes: sender, despatch date, courier/carrier, recipient name and signature, delivery date. Retain chain of custody records per Evidence Requirements.

### 3.6 Refusing a Transfer Request

Decline a PII transfer request and notify the DPO where:
- No agreement exists for an external recipient
- The purpose does not align with the documented legal basis for processing
- The transfer would be cross-border to a destination without an approved mechanism
- The requester cannot demonstrate a legitimate processing need

Document declined transfer requests (date, requestor, PII involved, reason for refusal). Retain for 3 years.

---

## Evidence Checklist

Use this checklist when preparing for a PIMS audit covering A.3.5, A.3.6, and A.3.7:

**A.3.5 — Classification:**
- [ ] Classification scheme document with PII minimum floors
- [ ] Classification Register — PII datasets classified, decisions recorded
- [ ] Aggregation determinations documented where applicable
- [ ] Classification review records for past 12 months

**A.3.6 — Labelling:**
- [ ] Labelling procedure documentation (format specifications for each media type)
- [ ] Data Asset Register with PII metadata fields populated for in-scope systems
- [ ] Sample labelled documents / system screenshots showing PII indicators

**A.3.7 — Transfer:**
- [ ] Transfer Agreement Register — signed agreements for all active external PII relationships
- [ ] International Transfer Register — TIA and mechanism documentation for cross-border transfers
- [ ] Internal transfer logs for RESTRICTED PII transfers
- [ ] Records of declined transfer requests where applicable

---

<!-- QA_VERIFIED: [Date] -->
