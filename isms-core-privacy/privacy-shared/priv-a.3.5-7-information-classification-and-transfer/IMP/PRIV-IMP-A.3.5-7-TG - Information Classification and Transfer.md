<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.5-7-TG:privacy:TG:a.3.5-7 -->
**PRIV-IMP-A.3.5-7-TG — Information Classification and Transfer — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Classification and Transfer — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.3.5-7-TG |
| **Related Policy** | PRIV-POL-A.3.5-7 (Information Classification and Transfer) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial technical guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant technical or regulatory change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.3.5-7 (Information Classification and Transfer — the governing policy)
- PRIV-IMP-A.3.5-7-UG (Information Classification and Transfer — User Guide)
- PRIV-POL-A.3.23-31 (Technical Security Controls for PII — cryptographic and transmission standards)
- ISMS-POL-A.5.12-13 (Information Classification and Labelling — ISMS framework)
- ISMS-POL-A.5.14 (Information Transfer — ISMS framework)

---

## Purpose of This Guide

This guide specifies the **technical structures, register schemas, label formats, and transfer control configurations** required to implement PRIV-POL-A.3.5-7. It covers:

- Classification Register structure
- Data Asset Register structure (system-level PII labelling)
- PII label format specifications for all media types
- Internal Transfer Log structure
- Transfer Agreement Register structure
- International Transfer Register structure
- Minimum technical standards for PII transfer channels

**Audience**: CISO, IT Security Team, System Owners, DPO (register ownership), Legal/Compliance (TIA sections).

---

## 1. Classification Register

The Classification Register records classification decisions for PII-containing datasets and information assets. It is owned by the DPO and maintained by Data Owners for their respective domains.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Asset ID | Text | Unique identifier for the information asset or dataset |
| Asset Name | Text | Descriptive name |
| Asset Owner | Text | Data Owner role and name |
| PII Present | Boolean | Yes / No |
| PII Categories | Multi-select | Ordinary / Financial / Special Category / Sensitive / Children's |
| Special Category Types | Text | If applicable: health, biometric, racial origin, etc. |
| Classification Level | Enum | PUBLIC / INTERNAL / CONFIDENTIAL / RESTRICTED |
| Classification Basis | Text | Reason for classification (PII floor, business requirement, combination) |
| Aggregation Rule Applied | Boolean | Yes / No — if Yes: document source datasets and derivation method |
| Aggregation Notes | Text | Source datasets combined; PII derivability assessment |
| Classification Authority | Text | Role that made the classification decision |
| DPO Approval (RESTRICTED) | Text | DPO name and date if RESTRICTED classification |
| Classification Date | Date | Date classification was assigned or last confirmed |
| Next Review Date | Date | Date of next scheduled classification review |
| Review Trigger | Text | Trigger event for last review (if trigger-based) |
| Notes | Text | Outstanding issues, pending review actions |

### Minimum Entries at First Certification

All information assets in the Record of Processing Activities (RoPA) must have a corresponding Classification Register entry. At minimum, the following must be registered:

- All databases and data stores containing PII
- All file repositories with PII-containing documents
- All third-party systems processing PII on behalf of the organisation
- All export/reporting datasets derived from PII systems

---

## 2. Data Asset Register (System-Level PII Labelling)

The Data Asset Register records PII status at the system, database, and repository level. It is the technical complement to the Classification Register (which records at dataset/asset level). It is owned by the CISO and updated by System Owners.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| System ID | Text | Unique system identifier (matches IT asset register) |
| System Name | Text | Descriptive system name |
| System Owner | Text | Role responsible for the system |
| System Type | Enum | Application / Database / File Store / Cloud Service / Integration / Other |
| PII Present | Boolean | Yes / No |
| PII Categories | Multi-select | Ordinary / Financial / Special Category / Sensitive |
| Special Category | Boolean | Yes / No |
| PII Volume (approx.) | Enum | <100 / 100–1,000 / 1,000–10,000 / 10,000–100,000 / >100,000 records |
| Jurisdictional Scope | Multi-select | EU/EEA / CH / UK / Other (specify) |
| Data Residency | Text | Country/region where data is stored at rest |
| Data Residency Verified | Boolean | Yes / No / Unknown |
| Encryption at Rest | Boolean | Yes / No / Partial |
| Encryption Standard | Text | AES-256 / AES-128 / Other |
| Access Control Mechanism | Text | RBAC / ABAC / ACL / Other |
| Classification Level | Enum | CONFIDENTIAL / RESTRICTED |
| DPIA Required | Boolean | Yes / No / Completed |
| DPIA Reference | Text | DPIA document reference if completed |
| Processor / Controller Role | Enum | Controller / Processor / Both |
| Last Updated | Date | Date of last register update |
| Notes | Text | Outstanding technical issues, pending actions |

### PII Metadata Field Standards for Technical Systems

For systems that support custom metadata fields (databases, document management platforms, cloud storage), implement the following standard fields:

| Metadata Field Name | Type | Values |
|--------------------|------|--------|
| `pii_present` | Boolean | true / false |
| `pii_category` | String | "ordinary" / "financial" / "special_category" / "sensitive" |
| `special_category` | Boolean | true / false |
| `classification` | String | "CONFIDENTIAL" / "RESTRICTED" |
| `jurisdictional_scope` | String | "EU" / "CH" / "UK" / comma-separated list |
| `data_owner` | String | Role identifier |
| `retention_expiry` | Date | ISO 8601 date |

---

## 3. PII Label Format Specifications

### Document Labels (Electronic — Word, PDF, PowerPoint)

**Header format** (appear on every page):
```
[CLASSIFICATION] — Contains Personal Data
```
Example: `CONFIDENTIAL — Contains Personal Data`
Example (special category): `RESTRICTED — Contains Special Category Personal Data`

**Footer format**:
```
[Document ID] | [CLASSIFICATION] | Contains Personal Data | © [Organisation] [Year]
```

Implementation:
- Word: Insert header/footer with automatic page numbering and classification text
- PDF export: Ensure headers/footers are included in PDF output settings; do not strip metadata
- PowerPoint: Apply to slide master so all slides carry the label

### Email Labels

Subject line prefix before the email subject:
- Ordinary PII: `[PD] `
- Special category PII: `[SPD] `

Examples:
- `[PD] Customer data extract — Q1 review`
- `[SPD] Medical assessment results — HR review`

Email footer (add to signature or as standard footer text):
```
CONFIDENTIAL — Contains Personal Data. This email and any attachments are intended solely
for the named recipient(s). If you have received this in error, please notify the sender
and delete immediately.
```

### File and Folder Naming Suffixes

Where naming conventions permit, apply these suffixes:
- `_PII` — file contains ordinary personal data (e.g., `customer_list_2026_PII.xlsx`)
- `_SPD` — file contains special category personal data (e.g., `health_records_2026_SPD.pdf`)

These suffixes are supplementary to document-level labels, not replacements for them.

### Physical Document Stamps

Use red ink stamps on cover page and all pages containing PII:

| Stamp Text | Usage |
|-----------|-------|
| `PERSONAL DATA — CONFIDENTIAL` | Ordinary personal data documents |
| `SPECIAL CATEGORY PERSONAL DATA — RESTRICTED` | Special category PII documents |

Physical stamp dimensions and ink colour: minimum 40mm × 10mm, red or dark blue ink.

---

## 4. Internal Transfer Log

Required for all RESTRICTED / special category PII transfers within the organisation.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Transfer ID | Text | Unique transfer reference |
| Date / Time | DateTime | ISO 8601 timestamp |
| Sender Name | Text | Full name of sender |
| Sender Role | Text | Role title |
| Sender System / Location | Text | Source system or location |
| Recipient Name | Text | Full name of recipient |
| Recipient Role | Text | Role title |
| Recipient System / Location | Text | Destination system or location |
| PII Categories Transferred | Multi-select | Categories of PII included in the transfer |
| Special Category | Boolean | Yes / No |
| Volume (approx.) | Text | Number of records or data subjects involved |
| Purpose of Transfer | Text | Documented business purpose |
| Authorisation Reference | Text | Data Owner approval reference (where required) |
| Transfer Method | Enum | Encrypted email / Secure platform / API / Physical / Other |
| Encryption Confirmed | Boolean | Yes / No |
| Notes | Text | Any anomalies, issues, or follow-up actions |

Retain internal transfer logs for 3 years.

---

## 5. Transfer Agreement Register

The Transfer Agreement Register is the authoritative record of all agreements governing external PII transfers. It is owned by the DPO.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Agreement ID | Text | Unique reference |
| Counterparty Name | Text | Legal name of the external party |
| Counterparty Type | Enum | PII Processor / Joint Controller / Recipient / Public Authority |
| Agreement Type | Enum | DPA (Art. 28) / Joint Controller (Art. 26) / Transfer Agreement / NDA |
| PII Categories Covered | Multi-select | Categories of PII covered by the agreement |
| Special Category | Boolean | Yes / No |
| Signed Date | Date | Date of execution |
| Effective Date | Date | Date transfer relationship commenced |
| Expiry / Review Date | Date | Renewal or review date |
| Status | Enum | Active / Expired / Terminated / Under Review |
| Cross-Border | Boolean | Yes / No |
| Destination Country | Text | If cross-border: destination country/region |
| Transfer Mechanism | Text | If cross-border: adequacy / EU SCCs / Swiss SCCs / BCRs / Art. 49 |
| International Transfer Register Ref | Text | Reference to TIA entry if applicable |
| Agreement Location | URL/Path | Document repository location |
| DPO Review Date | Date | Date DPO last reviewed the agreement |
| Notes | Text | Amendments, outstanding issues |

---

## 6. International Transfer Register

The International Transfer Register documents all cross-border PII transfers and the legal mechanisms supporting them. It is owned by the DPO with input from Legal/Compliance.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| Transfer ID | Text | Unique reference |
| Transfer Description | Text | Nature of the cross-border transfer |
| Originating Jurisdiction | Enum | EU/EEA / CH / UK / Other |
| Destination Country | Text | Country of PII destination |
| Recipient / Processor | Text | Name of the receiving entity |
| PII Categories | Multi-select | Categories of PII transferred |
| Special Category | Boolean | Yes / No |
| Transfer Mechanism | Enum | Adequacy Decision / EU SCCs (2021) / Swiss SCCs / BCRs / Art. 49 Derogation |
| Adequacy Decision Reference | Text | If adequacy: EU Commission / FDPIC decision reference and date |
| SCC Version | Text | If SCCs: version and module used (e.g., EU SCCs 2021, Module 2) |
| TIA Completed | Boolean | Yes / No |
| TIA Date | Date | Date TIA was completed |
| TIA Outcome | Enum | Adequate / Adequate with supplementary measures / Inadequate |
| Supplementary Measures | Text | If applicable: technical/contractual/organisational measures implemented |
| DPO Approval Date | Date | Date DPO approved the transfer |
| Transfer Agreement Ref | Text | Reference to entry in Transfer Agreement Register |
| Status | Enum | Active / Suspended / Terminated |
| Next Review Date | Date | Date for next TIA review |
| Notes | Text | Issues, pending adequacy changes, FDPIC watch items |

### Adequacy Status Reference (at time of publication)

Verify current status at eur-lex.europa.eu (EU adequacy decisions) and edoeb.admin.ch (Swiss adequacy list) before relying on adequacy as the transfer mechanism.

| Country | EU Adequacy | Swiss Adequacy |
|---------|-------------|----------------|
| Switzerland | ✓ (EU → CH) | N/A |
| EEA member states | N/A | ✓ |
| UK | ✓ (monitor renewal) | ✓ |
| Japan | ✓ | ✓ |
| Canada (PIPEDA organisations) | ✓ (partial) | ✓ |
| USA | EU–US Data Privacy Framework ✓ | ✓ (DPF signatories) |
| Other | Check eur-lex.europa.eu | Check edoeb.admin.ch |

---

## 7. Minimum Technical Standards for PII Transfer Channels

Per PRIV-POL-A.3.5-7 (A.3.7) and PRIV-POL-A.3.23-31:

| Transfer Type | Minimum Standard |
|--------------|-----------------|
| API / system-to-system | TLS 1.2 minimum; TLS 1.3 preferred; mutual TLS for RESTRICTED PII |
| Email (CONFIDENTIAL PII) | TLS transport encryption (STARTTLS); S/MIME or PGP where recipient supports it |
| Email (RESTRICTED / special category PII) | S/MIME or PGP end-to-end encryption required; plain TLS is not sufficient |
| Secure file transfer | SFTP (SSH-2) or HTTPS with TLS 1.2 minimum; no FTP or unencrypted HTTP |
| Cloud storage sharing | Recipient-authenticated share links with expiry; no public/anonymous links for PII |
| Physical media | AES-256 encryption on device; separate secure channel for decryption credentials |

Encryption configuration standards for systems handling PII are documented in PRIV-IMP-A.3.23-31-TG.

---

<!-- QA_VERIFIED: [Date] -->
