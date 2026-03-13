<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.5-7:privacy:POL:a.3.5-7 -->
**PRIV-POL-A.3.5-7 — Information Classification and Transfer**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Classification and Transfer |
| **Document Type** | Policy |
| **Document ID** | PRIV-POL-A.3.5-7 |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial policy for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Data Protection Officer (DPO)
- Secondary: Chief Information Security Officer (CISO)
- Legal: Legal/Compliance Officer
- Final Authority: Executive Management

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- PRIV-POL-01 (Privacy Governance and Decision-Making Framework)
- PRIV-IMP-A.3.5-7-UG (Information Classification and Transfer — User Guide)
- PRIV-IMP-A.3.5-7-TG (Information Classification and Transfer — Technical Guide)
- ISMS-POL-A.5.12-13 (Information Classification and Labelling — ISMS parallel)
- ISMS-POL-A.5.14 (Information Transfer — ISMS parallel)
- ISO/IEC 27701:2025 Controls A.3.5, A.3.6, A.3.7
- ISO/IEC 27701:2025 Annex B (Implementation guidance B.3.5, B.3.6, B.3.7)
- GDPR Article 32 (Security of processing); Article 44–49 (International transfers)
- CH FADP Article 7 (Data security); Articles 16–17 (Cross-border disclosure)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for information classification, labelling, and transfer as they relate to the processing of Personally Identifiable Information (PII), in accordance with ISO/IEC 27701:2025 Controls A.3.5, A.3.6, and A.3.7.

**Scope**: All information containing or related to PII; all classification and labelling procedures applied to PII; all transfer of PII within [Organisation] and between [Organisation] and other parties.

**Purpose**: Define organisational requirements for:

- PII-informed classification of information (A.3.5)
- Labelling procedures that recognise PII status (A.3.6)
- Transfer rules, procedures, and agreements for PII processing (A.3.7)

This policy establishes **WHAT** classification criteria and transfer rules apply to PII, **WHO** holds responsibility for PII classification and transfer decisions, and **WHEN** reviews and updates occur. Implementation procedures (**HOW**) are documented in PRIV-IMP-A.3.5-7-UG and PRIV-IMP-A.3.5-7-TG.

**Role Applicability**: This policy applies to the organisation acting as **both PII Controller and PII Processor**. Controls A.3.5, A.3.6, and A.3.7 are shared controls (Table A.3) and apply regardless of processing role.

**Combined Control Rationale**: A.3.5 (classification), A.3.6 (labelling), and A.3.7 (transfer) form a cohesive PII data-flow protection triad. Classification informs the labelling applied; labelling drives the transfer method required. They are implemented together as an integrated PII protection layer that overlays and extends the ISMS classification framework.

---

# Scope and Applicability

## ISO/IEC 27701:2025 Control Statements

**Control A.3.5 — Classification of information**
> *Information shall be classified according to the information security needs of the organization, taking into consideration PII, based on confidentiality, integrity, availability and relevant interested party requirements.*

**Control A.3.6 — Labelling of information**
> *An appropriate set of procedures for information labelling that considers PII shall be developed and implemented in accordance with the information classification scheme adopted by the organization.*

**Control A.3.7 — Information transfer**
> *Information transfer rules, procedures, or agreements related to processing PII shall be in place for all types of transfer facilities within the organization and between the organization and other parties.*

## What This Policy Covers

**Information**:

- All datasets, records, files, databases, and communications containing PII
- Aggregated datasets where PII can be derived or inferred, even where no individual field is directly identifying
- Information containing special category PII (health, biometric, racial/ethnic origin, religious belief, etc.)
- Information about PII subjects held in any format (electronic, physical, verbal)

**Classification**:

- The classification scheme applied to information containing PII, including PII-specific classification criteria that extend the ISMS classification scheme
- Minimum classification floors for defined PII categories
- Aggregation rules where combined data elevates classification

**Labelling**:

- Label types and formats that identify PII-containing information
- Labelling requirements specific to PII sensitivity and category
- Labelling obligations for systems and repositories that process PII

**Transfer**:

- All movement of PII within [Organisation] (system-to-system, team-to-team, processing environment-to-processing environment)
- All transfer of PII to external parties (PII processors, joint controllers, recipients, public authorities)
- Cross-border and international transfer of PII, including cloud processing in different jurisdictions

## What This Policy Does NOT Cover

- Classification labelling templates, tools, and configuration procedures (see PRIV-IMP-A.3.5-7-TG)
- Transfer platform configurations and secure channel setup (see PRIV-IMP-A.3.5-7-TG)
- Data subject rights procedures for PII access and portability (see PRIV-POL-A.1.3.5-10 and PRIV-POL-A.1.4.6-10)
- Processor agreements and due diligence procedures (see PRIV-POL-A.2.2.2-7)
- Incident response for PII transfer breaches (see PRIV-POL-A.3.11-12)
- ISMS-wide classification and transfer requirements (see ISMS-POL-A.5.12-13 and ISMS-POL-A.5.14)

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 32 (appropriate security of processing, including protection during transfer); Article 44–49 (international transfer safeguards — SCCs, adequacy decisions, BCRs); Article 5(1)(f) (integrity and confidentiality principle)
- **CH FADP**: Article 7 (technical and organisational measures proportionate to sensitivity); Articles 16–17 (cross-border disclosure — equivalence, standard data protection clauses)
- **ISO/IEC 27701:2025**: Controls A.3.5, A.3.6, A.3.7 (normative)

**Tier 2: Conditional Applicability** (per PRIV-POL-00):

- **ISO/IEC 27018:2025**: Annex A — cloud PII transfer requirements where public cloud processing in scope

**Tier 3: Informational Reference** (per PRIV-POL-00):

- **ISO/IEC 27002:2022**: Implementation guidance for classification (5.12–5.13) and transfer (5.14)
- **ISO/IEC 27701:2025 Annex B**: Implementation guidance B.3.5 (classification with PII), B.3.6 (PII-aware labelling), B.3.7 (PII transfer rules)

For complete regulatory categorisation, refer to PRIV-POL-00.

---

# Policy Statements: PII-Informed Classification of Information (A.3.5)

## Classification Scheme Extension for PII

[Organisation]'s information classification scheme (as defined in ISMS-POL-A.5.12-13) SHALL be applied to all information. For information containing or related to PII, this policy establishes PII-specific criteria that extend and supplement the ISMS classification scheme.

### PII Minimum Classification Floors

The following minimum classification levels SHALL apply to information containing PII, regardless of other classification criteria:

| PII Category | Minimum Classification |
|-------------|------------------------|
| **Ordinary personal data** (name, address, contact details, employment record) | CONFIDENTIAL |
| **Financial personal data** (bank accounts, payment records, salary, credit information) | CONFIDENTIAL |
| **Special category PII** (health/medical, biometric, genetic, racial/ethnic origin, religious belief, political opinion, sexual life/orientation, trade union membership) | RESTRICTED |
| **Sensitive personal data** (children's data, criminal records, national ID numbers, authentication credentials) | RESTRICTED |
| **PII of high-risk individuals** (vulnerable persons, whistleblowers, data subjects under protective measures) | RESTRICTED |

### PII Aggregation Rule

Where information individually classified below CONFIDENTIAL is combined such that PII can be derived, identified, or inferred, the aggregated dataset SHALL be classified at minimum CONFIDENTIAL. Where the aggregated dataset contains or enables derivation of special category PII, it SHALL be classified RESTRICTED.

The Data Owner (or DPO where no Data Owner is assigned) SHALL make the aggregation classification determination and document it in the Classification Register.

### Classification Authority for PII

| Classification Level | Who May Classify PII | Who May Declassify |
|---------------------|---------------------|--------------------|
| CONFIDENTIAL (ordinary PII) | Data Owner, DPO | Data Owner with DPO notification |
| RESTRICTED (special category PII) | Data Owner with DPO approval | Data Owner with DPO and Executive Management approval |
| RESTRICTED (high-risk PII) | DPO with Executive Management approval | DPO with Executive Management approval |

### Classification Review for PII

In addition to the review triggers in ISMS-POL-A.5.12-13, PII classification SHALL be reviewed:

- When the purpose of processing changes, such that different PII categories are involved
- When the legal basis for processing changes, affecting the sensitivity level
- Following a Data Protection Impact Assessment (DPIA) that identifies a reclassification requirement
- Upon notification from a Data Protection Authority (DPA) or supervisory authority
- When new guidance or case law materially changes how a PII category is interpreted

---

# Policy Statements: PII-Aware Labelling of Information (A.3.6)

## Labelling Requirements for PII

[Organisation] SHALL develop and implement labelling procedures that identify PII-containing information as such. PII labelling procedures SHALL be consistent with and extend the ISMS labelling scheme (ISMS-POL-A.5.12-13).

### Mandatory PII Labelling

All information classified CONFIDENTIAL or RESTRICTED on the basis of PII content SHALL carry:

1. The applicable classification label (CONFIDENTIAL or RESTRICTED) per ISMS labelling standards
2. A PII indicator designating that the information contains personal data

**PII indicator formats** (defined in detail in PRIV-IMP-A.3.5-7-TG):

| Format | PII Indicator |
|--------|--------------|
| Electronic documents | "Contains Personal Data" notation in header/footer or document properties |
| Physical documents | "PERSONAL DATA" stamp or printed indicator on cover and first page |
| Databases and data stores | Classification metadata field: `pii_present = true`; PII category field populated |
| Email | Subject prefix addition where content contains PII: `[PD]` or `[SPD]` for special category |
| File/folder naming | Suffix `_PII` or `_SPD` where practical and consistent with system capabilities |

### Special Category PII Labelling

Information containing special category PII SHALL additionally carry a special category indicator to enable heightened handling. The specific format of this indicator is defined in PRIV-IMP-A.3.5-7-TG.

### System and Repository Labelling

Repositories, databases, systems, and processing environments that store or process PII SHALL be labelled at the system level with:

- Whether PII is present (yes/no)
- PII categories processed (ordinary, financial, special category, or list of applicable categories)
- Applicable jurisdictional scope (e.g., EU/EEA data subjects, CH data subjects)

System-level labelling is maintained in the Data Asset Register (see PRIV-IMP-A.3.5-7-TG for register structure).

### Labelling Consistency Obligation

Where the ISMS classification label and the PII labelling requirement conflict (e.g., an asset is classified INTERNAL by ISMS criteria but contains ordinary PII requiring CONFIDENTIAL classification), the higher classification SHALL prevail and the PII minimum floor SHALL apply.

---

# Policy Statements: PII Transfer Rules and Agreements (A.3.7)

## Transfer Requirements for PII

[Organisation] SHALL establish and maintain rules, procedures, and agreements covering all transfer of PII through all types of transfer facilities, whether internal or external, electronic or physical.

### Internal PII Transfer

**Within [Organisation]**:

- PII SHALL only be transferred to organisational roles and personnel with a legitimate processing purpose and appropriate access authorisation
- Internal transfer of RESTRICTED PII (special category) SHALL be logged and traceable
- System-to-system PII transfers SHALL use encrypted channels; transfer configurations are documented in PRIV-IMP-A.3.5-7-TG
- Internal transfer of PII to processing environments in different jurisdictions SHALL be treated as cross-border transfer for regulatory compliance purposes

### External PII Transfer

**To PII Processors (suppliers and service providers)**:

External transfers of PII to processors SHALL require a current and valid processor agreement (Article 28 GDPR; Article 9 CH FADP) in place before transfer commences. No PII transfer to an external processor shall occur without a signed processor agreement. The DPO maintains the Processor Agreement Register.

**To Joint Controllers**:

External transfers of PII to joint controllers SHALL require a joint controller arrangement (Article 26 GDPR) that documents respective responsibilities. The DPO must approve joint controller arrangements before PII transfer.

**To Recipients and Third Parties**:

External transfers of PII to recipients other than processors or joint controllers (including public authorities, professional advisors, auditors, and others) require:

- A documented legal basis for disclosure under GDPR Article 6 (and Article 9 for special category)
- DPO review where the disclosure is not routine
- A record of the transfer in the Record of Processing Activities (RoPA)

### Cross-Border and International PII Transfer

Transfers of PII to countries or international organisations outside the EEA (for GDPR) or outside Switzerland (for CH FADP) are subject to the following requirements:

**Legal Basis for Transfer**:

| Mechanism | Applicability |
|-----------|--------------|
| Adequacy decision (EU Commission / Swiss FDPIC) | Transfers to countries with recognised adequate protection — no additional measures required |
| Standard Contractual Clauses (SCCs) | Transfers to countries without adequacy — EU SCCs (2021) or Swiss SCCs as applicable |
| Binding Corporate Rules (BCRs) | Intra-group transfers where BCRs are approved by competent DPA |
| Article 49 derogations | Exceptional circumstances only (data subject consent, vital interests, important public interest, legal claims) — not for systematic transfers |

**Transfer Impact Assessment**:

Where SCCs or other contractual mechanisms are used, [Organisation] SHALL conduct a Transfer Impact Assessment (TIA) to evaluate whether the legal framework of the destination country provides essentially equivalent protection. The TIA, supplementary measures decision, and DPO approval SHALL be documented in the International Transfer Register.

**Prohibited Destinations**:

- Countries subject to international sanctions where transfer would be unlawful
- Jurisdictions where no adequate legal mechanism is available and no derogation applies

### Transfer Methods for PII

PII transfer method requirements are determined by classification level, consistent with ISMS-POL-A.5.14 and extended as follows:

| Transfer Type | CONFIDENTIAL PII | RESTRICTED / Special Category PII |
|--------------|------------------|------------------------------------|
| **Electronic — internal** | Encrypted channel (TLS minimum) | Encrypted channel + access log entry |
| **Electronic — external** | Encrypted email or secure file transfer platform | End-to-end encrypted platform; recipient identity verification required |
| **Physical — documents** | Sealed envelope, tracked delivery, recipient signature | Double-sealed, bonded courier, chain of custody documentation |
| **Physical — media** | Encrypted media, tracked delivery | Encrypted media, secure courier, delivery confirmation |
| **Cloud — processing** | Encrypted at rest and in transit; data residency verified | Encrypted at rest and in transit; data residency confirmed; DPA-approved processor |

### Transfer Agreements

All external transfers of PII under ongoing relationships SHALL be governed by a written agreement covering at minimum:

- Purposes for which the recipient may use the PII
- Retention limits and deletion/return obligations
- Security measures the recipient must maintain
- Sub-processor engagement restrictions (for processor relationships)
- Breach notification obligations and timeframes
- Audit rights (where applicable)
- Governing law and jurisdiction

The DPO maintains the Transfer Agreement Register. No ongoing external PII transfer shall be established without a current agreement in the register.

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Responsibilities for A.3.5–A.3.7 |
|------|-----------------------------------|
| **Data Protection Officer (DPO)** | Primary authority for PII classification floors and transfer rules; approves cross-border transfer mechanisms; maintains International Transfer Register and Transfer Agreement Register; reviews aggregation classification determinations |
| **Data Owner** | Classifies PII datasets within their domain; applies PII labels; authorises internal transfers; escalates cross-border transfers to DPO |
| **CISO** | Ensures ISMS classification scheme is extended consistently to PII per this policy; ensures transfer controls (encryption, logging) are implemented for PII; coordinates with DPO on technical transfer controls |
| **IT Security Team / System Owners** | Implement system-level PII labelling; configure encrypted transfer channels; maintain system classification metadata; provide audit logs for PII transfers |
| **Privacy Champions** | First-line support for PII classification questions; escalate reclassification triggers to Data Owner and DPO |
| **Legal/Compliance** | Advise on cross-border transfer mechanisms; review SCCs and DPA adequacy decisions; support TIA documentation |
| **All Personnel** | Apply classification and labelling to PII handled in their role; use only approved transfer methods for PII; report suspected misclassification or unauthorised transfer |

---

# Evidence Requirements

The following evidence demonstrates operation of this policy:

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Classification Register | Record of PII dataset classifications, including aggregation decisions and classification authority | 3 years |
| Data Asset Register | System-level PII labelling records (pii_present, pii_categories, jurisdictional scope) | Current + 3 years |
| International Transfer Register | TIA records, SCCs, adequacy decision references, DPO approvals for cross-border PII transfers | Duration of transfer activity + 3 years |
| Transfer Agreement Register | Signed processor agreements, joint controller arrangements, recipient agreements | Duration of agreement + 3 years |
| Internal Transfer Logs | Logs of RESTRICTED PII internal transfers, including purpose and authorisation | 3 years |
| Classification Review Records | Evidence of periodic classification review and trigger-based reviews | 3 years |

---

# Audit Considerations

Auditors verifying compliance with A.3.5, A.3.6, and A.3.7 should expect to find:

**For A.3.5 (Classification)**:
- Classification scheme documentation showing PII minimum classification floors
- Evidence that PII datasets are classified at or above the required minimum
- Aggregation classification determinations for relevant combined datasets
- Classification review records at planned intervals or upon trigger events

**For A.3.6 (Labelling)**:
- Labelling procedures covering PII-containing information across all formats
- Sample labelled documents and system metadata showing PII indicator fields
- Data Asset Register with PII fields populated for in-scope systems
- Evidence that CONFIDENTIAL/RESTRICTED classification and PII indicator are consistently applied together

**For A.3.7 (Transfer)**:
- Transfer rules and procedures covering internal and external PII transfer
- Signed processor agreements for all active processor relationships
- International Transfer Register with TIA documentation for cross-border transfers
- Evidence of appropriate transfer mechanisms (SCCs, adequacy decisions) for international transfers
- Transfer logs for RESTRICTED PII transfers

---

<!-- QA_VERIFIED: [Date] -->
