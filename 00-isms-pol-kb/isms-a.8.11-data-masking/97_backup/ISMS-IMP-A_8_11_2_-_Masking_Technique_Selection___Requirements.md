# ISMS-IMP-A.8.11.2 - Masking Technique Selection & Requirements
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.11.2  
**Assessment Area:** Masking Technique Selection & Implementation  
**Related Policy:** ISMS-POL-A.8.11-S2.2 (Masking Technique Requirements)  
**Purpose:** Document approved masking techniques, assess technique selection against requirements, identify implementation gaps, and verify technique effectiveness in a vendor-agnostic manner

**Key Principle:** This assessment is **technique-centric, not tool-centric**. Organizations document WHICH masking techniques they use and HOW they're configured – independent of specific vendor products.

---

## Workbook Structure

### Sheet 1: Instructions_Legend

#### Header Section
- **Title:** "ISMS-IMP-A.8.11.2 – Masking Technique Selection & Requirements"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.11: Data Masking"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block
```
Document ID:           ISMS-IMP-A.8.11.2
Assessment Area:       Masking Technique Selection
Related Policy:        ISMS-POL-A.8.11-S2.2
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Semi-Annual (every 6 months)
```

#### How to Use This Workbook
1. Review Approved_Techniques to understand organization's approved masking methods
2. Complete Technique_Selection_Matrix to map data types to appropriate techniques
3. Document SDM implementations in Static_Masking_SDM sheet
4. Document DDM implementations in Dynamic_Masking_DDM sheet
5. If using tokenization, complete Tokenization_Implementation sheet
6. If using encryption for masking, complete Encryption_for_Masking sheet
7. Document any masking tools/solutions in Masking_Tool_Inventory (generic names only)
8. Define configuration standards in Configuration_Standards sheet
9. Identify gaps in Gap_Analysis
10. Maintain evidence in Evidence_Register
11. Review summary metrics in Summary_Dashboard
12. Obtain required approvals

#### Approved Masking Technique Taxonomy (Quick Reference)
| Technique ID | Technique Name | Reversible? | Format-Preserving? |
|--------------|----------------|-------------|-------------------|
| TECH-SDM | Static Data Masking | No | Yes |
| TECH-DDM | Dynamic Data Masking | N/A (runtime) | Yes |
| TECH-RED | Redaction/Nullification | No | No |
| TECH-TOK | Tokenization | Yes (with vault) | Optional |
| TECH-SUB | Data Substitution (Synthetic) | No | Yes |
| TECH-ENC | Encryption (for masking) | Yes (with key) | No |
| TECH-SHF | Data Shuffling | No | Yes (values) |
| TECH-HSH | Hashing (One-way) | No | No |

#### Use Case Guidance
| Use Case | Recommended Techniques | Notes |
|----------|----------------------|-------|
| Non-production environments | SDM, Substitution | Irreversible, format-preserving |
| Production role-based access | DDM | Real-time masking based on user role |
| External data sharing | Redaction, Tokenization | Complete obscuration or controlled de-masking |
| Analytics/ML training | Substitution, Shuffling | Maintain statistical properties |
| Payment processing | Tokenization | PCI-DSS compliance |
| Data at rest protection | Encryption | Reversible with proper key management |
| Password storage | Hashing (salted) | Irreversible verification |

#### Status Legend
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Implemented | Technique fully implemented | Green (C6EFCE) |
| ⚠️ | Partial | Partial implementation | Yellow (FFEB9C) |
| ❌ | Not Implemented | Technique not deployed | Red (FFC7CE) |
| 📋 | Planned | Implementation planned | Blue (B4C7E7) |
| N/A | Not Applicable | Not required for organization | Gray |

#### Acceptable Evidence (Examples)
- ✓ Masking tool configuration documentation
- ✓ Masking scripts and procedures
- ✓ Before/after masking sample data (sanitized)
- ✓ Technique selection decision matrix
- ✓ Irreversibility test results
- ✓ Format preservation validation reports
- ✓ Referential integrity test results
- ✓ Performance impact assessments
- ✓ Token vault architecture documentation (if applicable)
- ✓ Key management procedures (if encryption used)
- ✓ Re-identification risk assessments
- ✓ DDM rule configuration exports

---

## Sheet 2: Approved_Techniques

### Purpose
Document the organization's approved masking techniques per policy S2.2. Read-only reference sheet.

### Header Section
**Row 1:** "APPROVED MASKING TECHNIQUES"  
**Row 2:** "Organization-approved techniques from ISMS-POL-A.8.11-S2.2"

**Assessment Question (Row 3):**  
"Has your organization formally approved and documented the masking techniques to be used?"

**Response Dropdown (Row 4):**  
Options: Yes / No / Partial / Planned / N/A

### Column Headers (Row 6)

| Column | Header | Width |
|--------|--------|-------|
| A | Technique ID | 15 |
| B | Technique Name | 25 |
| C | Description | 45 |
| D | Reversible? | 12 |
| E | Format-Preserving? | 18 |
| F | Primary Use Cases | 40 |
| G | Approved for Use? | 15 |
| H | Policy Reference | 20 |
| I | Implementation Status | 18 |

### Pre-Populated Technique Definitions (Rows 7-16)

**TECH-SDM: Static Data Masking**
- Description: Permanent replacement of sensitive data with realistic but fictitious data
- Reversible: No
- Format-Preserving: Yes
- Use Cases: Non-production environments, training databases, external sharing
- Policy Ref: ISMS-POL-A.8.11-S2.2, Section 2.1

**TECH-DDM: Dynamic Data Masking**
- Description: Real-time masking at point of access based on user privileges
- Reversible: N/A (runtime only)
- Format-Preserving: Yes
- Use Cases: Production role-based access, compliance audit trails
- Policy Ref: ISMS-POL-A.8.11-S2.2, Section 2.2

**TECH-RED: Redaction/Nullification**
- Description: Complete removal or replacement with placeholder characters
- Reversible: No
- Format-Preserving: No
- Use Cases: External reports, screenshots, high-sensitivity data
- Policy Ref: ISMS-POL-A.8.11-S2.2, Section 2.3

**TECH-TOK: Tokenization**
- Description: Replacement with non-sensitive tokens, mapping in secure vault
- Reversible: Yes (with vault access)
- Format-Preserving: Optional
- Use Cases: Payment processing, cross-system references
- Policy Ref: ISMS-POL-A.8.11-S2.2, Section 2.4

**TECH-SUB: Data Substitution (Synthetic)**
- Description: Replacement with realistic but entirely fictional data
- Reversible: No
- Format-Preserving: Yes
- Use Cases: AI/ML training, performance testing, analytics
- Policy Ref: ISMS-POL-A.8.11-S2.2, Section 2.5

**TECH-ENC: Encryption (for Masking)**
- Description: Cryptographic transformation rendering data unreadable
- Reversible: Yes (with key)
- Format-Preserving: No (typically)
- Use Cases: Data at rest, backups, authorized de-masking scenarios
- Policy Ref: ISMS-POL-A.8.11-S2.2, Section 2.6

**TECH-SHF: Data Shuffling**
- Description: Rearrangement of values within dataset, breaking associations
- Reversible: No
- Format-Preserving: Yes (value distribution)
- Use Cases: Analytics preserving statistics, breaking linkability
- Policy Ref: ISMS-POL-A.8.11-S2.2, Section 2.7

**TECH-HSH: Hashing (One-Way)**
- Description: Cryptographic one-way transformation to fixed-length hash
- Reversible: No
- Format-Preserving: No
- Use Cases: Password storage, data matching, deduplication
- Policy Ref: ISMS-POL-A.8.11-S2.2, Section 2.8

### Technique Approval Checklist (Starting Row 18)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Are approved techniques formally documented? | Dropdown: ✅/⚠️/❌/📋/N/A | Text | Text |
| 2 | Are technique selection criteria defined? | Dropdown | Text | Text |
| 3 | Are techniques approved by CISO? | Dropdown | Text | Text |
| 4 | Is DPO consulted on technique selection? | Dropdown | Text | Text |
| 5 | Are irreversibility requirements documented? | Dropdown | Text | Text |
| 6 | Are format preservation requirements documented? | Dropdown | Text | Text |
| 7 | Are prohibited techniques clearly identified? | Dropdown | Text | Text |
| 8 | Is technique review cycle established? | Dropdown | Text | Text |

---

## Sheet 3: Technique_Selection_Matrix

### Purpose
Map data types and categories to appropriate masking techniques.

### Header Section
**Row 1:** "TECHNIQUE SELECTION MATRIX"  
**Row 2:** "Map data types/categories to appropriate masking techniques"

**Assessment Question (Row 3):**  
"Has your organization mapped data types to appropriate masking techniques?"

**Response Dropdown (Row 4):**  
Options: Yes / No / Partial / Planned / N/A

### Column Headers (Row 6)

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Data Category | 20 | Text | From A.8.11.1 taxonomy |
| B | Data Type Example | 30 | Text | Free text |
| C | Sensitivity Level | 15 | Dropdown | Critical/High/Medium/Low |
| D | Primary Technique | 20 | Dropdown | TECH-SDM/DDM/RED/TOK/SUB/ENC/SHF/HSH |
| E | Secondary Technique | 20 | Dropdown | Same as D (or N/A) |
| F | Format Must Preserve? | 15 | Dropdown | Yes/No/Conditional |
| G | Reversibility Required? | 15 | Dropdown | Yes/No/Conditional |
| H | Environment(s) | 25 | Text | Prod/Non-Prod/Both |
| I | Selection Rationale | 35 | Text | Free text |
| J | Regulatory Driver | 20 | Text | GDPR/FADP/HIPAA/PCI-DSS |
| K | Implementation Status | 18 | Dropdown | ✅/⚠️/❌/📋/N/A |
| L | Notes | 30 | Text | Free text |

### Pre-Populated Example Rows (Rows 7-9 - gray italic)

| Data Category | Data Type Example | Sensitivity | Primary Tech | Secondary | Format? | Reverse? | Env | Rationale |
|--------------|-------------------|-------------|--------------|-----------|---------|----------|-----|-----------|
| CAT-PII-D | Full Name | High | TECH-SUB | N/A | Yes | No | Non-Prod | Substitution maintains realistic names |
| CAT-FIN | Credit Card (PAN) | Critical | TECH-TOK | TECH-RED | Yes | Yes | Prod + Non-Prod | Tokenization for prod, redaction for reports |
| CAT-CRD | Passwords | Critical | TECH-HSH | N/A | No | No | All | Salted hashing per best practice |

### Data Entry Rows (10-59: 50 rows)
Yellow-highlighted input cells with dropdowns

### Selection Criteria Reference Table (Starting Row 61)

**Header:** "TECHNIQUE SELECTION CRITERIA (Reference)"

| Criterion | Consideration | Recommended Techniques |
|-----------|---------------|----------------------|
| High Sensitivity + No Reversibility | Complete obscuration required | Redaction, Hashing |
| High Sensitivity + Format Preservation | Realistic data needed | Substitution, Format-Preserving Tokenization |
| Reversibility Required | Authorized users may need original | Encryption, Tokenization |
| Production Role-Based Access | Different views per role | Dynamic Data Masking (DDM) |
| Analytics/ML Use Case | Statistical properties must preserve | Substitution, Shuffling |
| Payment Processing | PCI-DSS compliance | Tokenization |
| Referential Integrity Required | Cross-table relationships | Deterministic Substitution, Tokenization |

### Technique Selection Checklist (Starting Row 70)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is technique selection based on documented criteria? | Dropdown | Text | Text |
| 2 | Are data types mapped to techniques? | Dropdown | Text | Text |
| 3 | Is sensitivity level considered in selection? | Dropdown | Text | Text |
| 4 | Is reversibility requirement evaluated? | Dropdown | Text | Text |
| 5 | Is format preservation requirement evaluated? | Dropdown | Text | Text |
| 6 | Are regulatory requirements considered? | Dropdown | Text | Text |
| 7 | Is referential integrity requirement assessed? | Dropdown | Text | Text |
| 8 | Are performance requirements considered? | Dropdown | Text | Text |
| 9 | Is re-identification risk assessed? | Dropdown | Text | Text |
| 10 | Are technique combinations evaluated (if needed)? | Dropdown | Text | Text |

---

## Sheet 4: Static_Masking_SDM

### Purpose
Document Static Data Masking (SDM) implementations for non-production environments.

### Header Section
**Row 1:** "STATIC DATA MASKING (SDM) IMPLEMENTATION"  
**Row 2:** "Document SDM implementations for non-production environments (40 rows)"

**Assessment Question (Row 3):**  
"Is Static Data Masking (SDM) implemented for non-production environments?"

**Response Dropdown (Row 4):**  
Options: Yes / No / Partial / Planned / N/A

### Column Headers (Row 6)

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | SDM Implementation ID | 15 | Text | Free text (SDM-001) |
| B | Source System | 25 | Text | From A.8.11.1 inventory |
| C | Target Environment | 20 | Dropdown | Development/Test/QA/UAT/Training/Analytics |
| D | Data Category Masked | 20 | Text | CAT-PII-D, CAT-FIN, etc. |
| E | Masking Method | 20 | Dropdown | Substitution/Redaction/Shuffling/Hashing/Other |
| F | Automated? | 12 | Dropdown | Yes/No/Partial |
| G | Masking Tool/Script | 25 | Text | Generic name (e.g., "Python masking script") |
| H | Masking Frequency | 15 | Dropdown | On-Demand/Weekly/Monthly/Quarterly |
| I | Last Masking Date | 15 | Date | Date picker |
| J | Format Preserved? | 15 | Dropdown | Yes/No/Partial |
| K | Referential Integrity? | 18 | Dropdown | Maintained/Not Required/Broken |
| L | Irreversibility Validated? | 18 | Dropdown | Yes/No/Not Tested |
| M | Performance Impact | 15 | Dropdown | Negligible/Low/Medium/High |
| N | Implementation Status | 18 | Dropdown | ✅/⚠️/❌/📋/N/A |
| O | Evidence Reference | 20 | Text | Link to Evidence_Register |
| P | Notes | 30 | Text | Free text |

### Data Entry Rows (7-46: 40 rows)

### SDM Requirements Checklist (Starting Row 48)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is SDM applied before data leaves production? | Dropdown | Text | Text |
| 2 | Is SDM automated (scripted/tool-based)? | Dropdown | Text | Text |
| 3 | Is SDM process repeatable and consistent? | Dropdown | Text | Text |
| 4 | Does SDM maintain referential integrity? | Dropdown | Text | Text |
| 5 | Does SDM preserve data format? | Dropdown | Text | Text |
| 6 | Is original data backed up before masking? | Dropdown | Text | Text |
| 7 | Is post-masking validation performed? | Dropdown | Text | Text |
| 8 | Is irreversibility validated? | Dropdown | Text | Text |
| 9 | Are masking rules documented? | Dropdown | Text | Text |
| 10 | Is SDM process tested before production deployment? | Dropdown | Text | Text |
| 11 | Are SDM failures logged and alerted? | Dropdown | Text | Text |
| 12 | Is SDM coverage verified (all sensitive fields masked)? | Dropdown | Text | Text |

---

## Sheet 5: Dynamic_Masking_DDM

### Purpose
Document Dynamic Data Masking (DDM) implementations for production role-based access.

### Header Section
**Row 1:** "DYNAMIC DATA MASKING (DDM) IMPLEMENTATION"  
**Row 2:** "Document DDM implementations for production role-based access (30 rows)"

**Assessment Question (Row 3):**  
"Is Dynamic Data Masking (DDM) implemented for production role-based data access?"

**Response Dropdown (Row 4):**  
Options: Yes / No / Partial / Planned / N/A

### Column Headers (Row 6)

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | DDM Rule ID | 15 | Text | Free text (DDM-001) |
| B | System/Database | 25 | Text | From A.8.11.1 inventory |
| C | Table/View | 25 | Text | Free text |
| D | Field(s) Masked | 25 | Text | Comma-separated field names |
| E | Data Category | 20 | Text | CAT-PII-D, CAT-FIN, etc. |
| F | User Role (Masked) | 25 | Text | Role that sees masked data |
| G | User Role (Unmasked) | 25 | Text | Role that sees original data |
| H | Masking Pattern | 25 | Text | e.g., "****1234", "XXX@XXX.com" |
| I | DDM Layer | 15 | Dropdown | Database/Application/Both |
| J | Bypass Prevention | 15 | Dropdown | Yes/No/Partial |
| K | Access Logging | 15 | Dropdown | Yes/No/Partial |
| L | Performance Impact | 15 | Dropdown | Negligible/Low/Medium/High |
| M | Implementation Status | 18 | Dropdown | ✅/⚠️/❌/📋/N/A |
| N | Evidence Reference | 20 | Text | Link to Evidence_Register |
| O | Notes | 30 | Text | Free text |

### Data Entry Rows (7-36: 30 rows)

### DDM Requirements Checklist (Starting Row 38)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is DDM enforced at database or application layer? | Dropdown | Text | Text |
| 2 | Are DDM rules based on documented user roles? | Dropdown | Text | Text |
| 3 | Is DDM bypass prevention implemented? | Dropdown | Text | Text |
| 4 | Does DDM log all access to sensitive fields? | Dropdown | Text | Text |
| 5 | Is DDM performance impact acceptable? | Dropdown | Text | Text |
| 6 | Are DDM rules tested for all user roles? | Dropdown | Text | Text |
| 7 | Can DDM rules be updated without application downtime? | Dropdown | Text | Text |
| 8 | Is DDM configuration backed up? | Dropdown | Text | Text |
| 9 | Are DDM failures alerted to security team? | Dropdown | Text | Text |
| 10 | Is DDM coverage verified (all sensitive fields covered)? | Dropdown | Text | Text |
| 11 | Are SQL injection bypasses prevented? | Dropdown | Text | Text |
| 12 | Is direct database access (non-application) also masked? | Dropdown | Text | Text |

---

## Sheet 6: Tokenization_Implementation

### Purpose
Document tokenization implementations (if applicable).

### Header Section
**Row 1:** "TOKENIZATION IMPLEMENTATION"  
**Row 2:** "Document tokenization deployments and token vault details (20 rows)"

**Assessment Question (Row 3):**  
"Does your organization use tokenization for data masking?"

**Response Dropdown (Row 4):**  
Options: Yes / No / Planned / N/A

### Column Headers (Row 6)

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Tokenization ID | 15 | Text | Free text (TOK-001) |
| B | Use Case | 30 | Text | e.g., "Payment processing", "PII de-identification" |
| C | Data Category Tokenized | 20 | Text | CAT-FIN, CAT-PII-D, etc. |
| D | Format-Preserving? | 15 | Dropdown | Yes/No |
| E | Token Vault Solution | 25 | Text | Generic name (e.g., "Token vault A") |
| F | Vault Encryption | 15 | Dropdown | AES-256/AES-128/Other |
| G | Vault Access Control | 20 | Text | Role-based/API-key/Certificate |
| H | Token Lifecycle Mgmt | 15 | Dropdown | Yes/No/Partial |
| I | Token Expiry Configured? | 18 | Dropdown | Yes/No/N/A |
| J | De-tokenization Logging? | 18 | Dropdown | Yes/No |
| K | Vault Availability | 15 | Dropdown | HA Configured/Single Instance |
| L | Key Management | 20 | Text | Reference to ISMS-POL-A.8.24 |
| M | Implementation Status | 18 | Dropdown | ✅/⚠️/❌/📋/N/A |
| N | Evidence Reference | 20 | Text | Link to Evidence_Register |
| O | Notes | 30 | Text | Free text |

### Data Entry Rows (7-26: 20 rows)

### Tokenization Requirements Checklist (Starting Row 28)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is token vault cryptographically secured? | Dropdown | Text | Text |
| 2 | Is token generation unpredictable? | Dropdown | Text | Text |
| 3 | Is access to token vault strictly controlled? | Dropdown | Text | Text |
| 4 | Is token vault access logged? | Dropdown | Text | Text |
| 5 | Is token lifecycle management implemented? | Dropdown | Text | Text |
| 6 | Are expired tokens revoked? | Dropdown | Text | Text |
| 7 | Is token vault backed up? | Dropdown | Text | Text |
| 8 | Is token vault availability ensured (HA/DR)? | Dropdown | Text | Text |
| 9 | Are vault encryption keys managed per ISMS-POL-A.8.24? | Dropdown | Text | Text |
| 10 | Is de-tokenization audited? | Dropdown | Text | Text |

---

## Sheet 7: Encryption_for_Masking

### Purpose
Document use of encryption as a masking technique (if applicable).

### Header Section
**Row 1:** "ENCRYPTION FOR MASKING"  
**Row 2:** "Document encryption used for data masking purposes (20 rows)"

**Assessment Question (Row 3):**  
"Does your organization use encryption as a masking technique?"

**Response Dropdown (Row 4):**  
Options: Yes / No / Planned / N/A

### Column Headers (Row 6)

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Encryption ID | 15 | Text | Free text (ENC-001) |
| B | System/Database | 25 | Text | From A.8.11.1 inventory |
| C | Data Category Encrypted | 20 | Text | CAT-PII-D, CAT-FIN, etc. |
| D | Encryption Algorithm | 18 | Dropdown | AES-256/AES-128/RSA/Other |
| E | Encryption Layer | 15 | Dropdown | Field-Level/File-Level/Database-Level |
| F | Key Length | 12 | Text | e.g., "256-bit" |
| G | Key Management | 20 | Text | Reference to ISMS-POL-A.8.24 |
| H | Key Storage | 20 | Dropdown | HSM/KMS/File-Based/Other |
| I | Decryption Access Control | 25 | Text | Role-based/Certificate-based |
| J | Decryption Logging? | 15 | Dropdown | Yes/No |
| K | Format-Preserving Encryption? | 18 | Dropdown | Yes/No |
| L | Performance Impact | 15 | Dropdown | Negligible/Low/Medium/High |
| M | Implementation Status | 18 | Dropdown | ✅/⚠️/❌/📋/N/A |
| N | Evidence Reference | 20 | Text | Link to Evidence_Register |
| O | Notes | 30 | Text | Free text |

### Data Entry Rows (7-26: 20 rows)

### Encryption for Masking Checklist (Starting Row 28)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is encryption algorithm industry-standard? | Dropdown | Text | Text |
| 2 | Are encryption keys managed per ISMS-POL-A.8.24? | Dropdown | Text | Text |
| 3 | Is key access strictly controlled? | Dropdown | Text | Text |
| 4 | Are decryption operations logged? | Dropdown | Text | Text |
| 5 | Is encryption applied at appropriate layer? | Dropdown | Text | Text |
| 6 | Are encryption keys rotated regularly? | Dropdown | Text | Text |
| 7 | Is key backup and recovery tested? | Dropdown | Text | Text |
| 8 | Is performance impact acceptable? | Dropdown | Text | Text |
| 9 | Is encrypted data protected from unauthorized decryption? | Dropdown | Text | Text |
| 10 | Is encryption vs. masking use case justified? | Dropdown | Text | Text |

---

## Sheet 8: Masking_Tool_Inventory

### Purpose
Document masking tools/solutions deployed (vendor-agnostic).

### Header Section
**Row 1:** "MASKING TOOL/SOLUTION INVENTORY"  
**Row 2:** "Document masking tools deployed (30 rows - generic names only)"

**Assessment Question (Row 3):**  
"Does your organization use dedicated masking tools or solutions?"

**Response Dropdown (Row 4):**  
Options: Yes / No / Planned / N/A

### Column Headers (Row 6)

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Tool ID | 12 | Text | Free text (TOOL-001) |
| B | Tool Name (Generic) | 25 | Text | e.g., "Masking Tool A", "Python Script X" |
| C | Vendor/Provider | 25 | Text | Customer fills in vendor name |
| D | Tool Type | 20 | Dropdown | Commercial/Open Source/Custom Script/Cloud Service |
| E | Techniques Supported | 30 | Text | SDM/DDM/Tokenization/etc. (comma-separated) |
| F | Systems Covered | 25 | Text | Which systems does this tool mask? |
| G | Deployment Model | 18 | Dropdown | On-Premises/Cloud/SaaS/Hybrid |
| H | License Type | 15 | Dropdown | Perpetual/Subscription/Open Source |
| I | License Expiry | 15 | Date | Date picker (if applicable) |
| J | Support Contract Active? | 18 | Dropdown | Yes/No/N/A |
| K | Last Update/Patch | 15 | Date | Date picker |
| L | Integration Points | 25 | Text | What systems integrate with this tool? |
| M | Implementation Status | 18 | Dropdown | ✅/⚠️/❌/📋/N/A |
| N | Evidence Reference | 20 | Text | Link to Evidence_Register |
| O | Notes | 30 | Text | Free text |

### Data Entry Rows (7-36: 30 rows)

### Tool Inventory Checklist (Starting Row 38)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Are all masking tools inventoried? | Dropdown | Text | Text |
| 2 | Are tool capabilities documented? | Dropdown | Text | Text |
| 3 | Are licenses current and valid? | Dropdown | Text | Text |
| 4 | Are support contracts active? | Dropdown | Text | Text |
| 5 | Are tools updated regularly? | Dropdown | Text | Text |
| 6 | Is tool configuration backed up? | Dropdown | Text | Text |
| 7 | Is tool access controlled? | Dropdown | Text | Text |
| 8 | Are tool operations logged? | Dropdown | Text | Text |
| 9 | Is tool redundancy/HA configured? | Dropdown | Text | Text |
| 10 | Are tools integrated with CI/CD pipelines (if applicable)? | Dropdown | Text | Text |

---

## Sheet 9: Configuration_Standards

### Purpose
Document masking configuration standards and rules.

### Header Section
**Row 1:** "MASKING CONFIGURATION STANDARDS"  
**Row 2:** "Document masking rules, standards, and referential integrity requirements (40 rows)"

**Assessment Question (Row 3):**  
"Are masking configuration standards documented and enforced?"

**Response Dropdown (Row 4):**  
Options: Yes / No / Partial / Planned / N/A

### Column Headers (Row 6)

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Standard ID | 15 | Text | Free text (STD-001) |
| B | Standard Category | 20 | Dropdown | Format Preservation/Referential Integrity/Irreversibility/Performance/Other |
| C | Standard Description | 40 | Text | Free text |
| D | Applies To | 25 | Text | Which techniques/systems? |
| E | Requirement Level | 15 | Dropdown | SHALL/SHOULD/MAY |
| F | Validation Method | 25 | Text | How is this standard verified? |
| G | Validation Frequency | 18 | Dropdown | Pre-Masking/Post-Masking/Quarterly/Annual |
| H | Compliance Status | 18 | Dropdown | ✅/⚠️/❌/📋/N/A |
| I | Non-Compliance Impact | 25 | Text | What happens if violated? |
| J | Responsible Role | 20 | Text | Who enforces this standard? |
| K | Evidence Reference | 20 | Text | Link to Evidence_Register |
| L | Notes | 30 | Text | Free text |

### Pre-Populated Example Standards (Rows 7-11 - gray italic)

| Standard ID | Category | Description | Applies To | Requirement |
|-------------|----------|-------------|------------|-------------|
| STD-001 | Format Preservation | Masked data SHALL pass same validation rules as original | SDM, Substitution | SHALL |
| STD-002 | Referential Integrity | Foreign key relationships SHALL be maintained post-masking | SDM | SHALL |
| STD-003 | Irreversibility | Masked data SHALL NOT be reversible to original | SDM, Redaction, Hashing | SHALL |
| STD-004 | Performance | Masking SHALL NOT degrade performance beyond 10% | DDM | SHOULD |
| STD-005 | Consistency | Same input SHALL produce same masked output (if deterministic) | Tokenization, Substitution | SHOULD |

### Data Entry Rows (12-51: 40 rows)

### Configuration Standards Checklist (Starting Row 53)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Are configuration standards documented? | Dropdown | Text | Text |
| 2 | Are format preservation rules defined? | Dropdown | Text | Text |
| 3 | Are referential integrity requirements specified? | Dropdown | Text | Text |
| 4 | Are irreversibility requirements validated? | Dropdown | Text | Text |
| 5 | Are performance impact limits defined? | Dropdown | Text | Text |
| 6 | Are configuration standards enforced? | Dropdown | Text | Text |
| 7 | Is standard compliance verified? | Dropdown | Text | Text |
| 8 | Are exceptions to standards documented? | Dropdown | Text | Text |
| 9 | Are configuration changes reviewed? | Dropdown | Text | Text |
| 10 | Is configuration documentation maintained? | Dropdown | Text | Text |

---

## Sheet 10: Gap_Analysis

### Purpose
Identify gaps in masking technique implementation.

### Header Section
**Row 1:** "MASKING TECHNIQUE IMPLEMENTATION GAP ANALYSIS"  
**Row 2:** "Identify missing techniques, incomplete implementations, or coverage gaps"

### Gap Summary Table (Rows 4-12)

| Gap Category | Count | % of Total | Risk Level | Remediation Owner | Target Date |
|--------------|-------|------------|------------|-------------------|-------------|
| Required technique not implemented | =COUNTIF() | Formula | Dropdown: Critical/High/Medium/Low | Text | Date |
| SDM not covering all non-prod environments | =COUNTIF() | Formula | Dropdown | Text | Date |
| DDM not implemented for production | =COUNTIF() | Formula | Dropdown | Text | Date |
| Format preservation failures | =COUNTIF() | Formula | Dropdown | Text | Date |
| Referential integrity broken | =COUNTIF() | Formula | Dropdown | Text | Date |
| Irreversibility not validated | =COUNTIF() | Formula | Dropdown | Text | Date |
| Configuration standards not enforced | =COUNTIF() | Formula | Dropdown | Text | Date |

### Detailed Gap Register (Starting Row 14)

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Gap ID | 12 | Text (GAP-001) |
| B | Gap Category | 25 | Dropdown: Technique Missing/Coverage Incomplete/Standard Violation/Validation Missing/Other |
| C | Affected System/Data | 25 | Text |
| D | Gap Description | 35 | Text |
| E | Risk Level | 12 | Dropdown: Critical/High/Medium/Low |
| F | Impact if Not Remediated | 30 | Text |
| G | Root Cause | 25 | Text |
| H | Remediation Action | 30 | Text |
| I | Remediation Owner | 20 | Text |
| J | Target Completion Date | 15 | Date |
| K | Status | 15 | Dropdown: Open/In Progress/Complete/Accepted Risk |
| L | Actual Completion Date | 15 | Date |
| M | Verification Method | 20 | Text |
| N | Notes | 30 | Text |

**Rows 15-64:** 50 gap register rows

### Gap Analysis Checklist (Starting Row 66)

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is gap analysis performed semi-annually? | Dropdown | Text | Text |
| 2 | Are missing technique implementations identified? | Dropdown | Text | Text |
| 3 | Are coverage gaps documented? | Dropdown | Text | Text |
| 4 | Are standard violations identified? | Dropdown | Text | Text |
| 5 | Are validation gaps documented? | Dropdown | Text | Text |
| 6 | Are gaps prioritized by risk? | Dropdown | Text | Text |
| 7 | Are remediation actions defined? | Dropdown | Text | Text |
| 8 | Are remediation owners assigned? | Dropdown | Text | Text |
| 9 | Is gap closure tracked? | Dropdown | Text | Text |
| 10 | Are accepted risks documented and approved? | Dropdown | Text | Text |

---

## Sheet 11: Evidence_Register

### Purpose
Central repository of masking technique implementation evidence.

### Header Section
**Row 1:** "EVIDENCE REGISTER"  
**Row 2:** "Audit trail of masking technique documentation (100 entry template)"

### Column Headers (Row 4)

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Evidence ID | 12 | Text (EVD-001) |
| B | Evidence Type | 25 | Dropdown: Config File/Masking Script/Test Report/Validation Report/Tool Documentation/Screenshot/Approval Email/Other |
| C | Evidence Title | 30 | Text |
| D | Related Technique(s) | 20 | Text (TECH-SDM, TECH-DDM, etc.) |
| E | Related System(s) | 25 | Text |
| F | Related Requirement(s) | 20 | Text (REQ-xxx) |
| G | Evidence Location | 30 | Text (file path, URL, document ID) |
| H | Evidence Date | 15 | Date |
| I | Evidence Owner | 20 | Text |
| J | Retention Period | 15 | Text |
| K | Review Frequency | 15 | Dropdown: Annual/Semi-Annual/Quarterly/As-Needed/N/A |
| L | Last Reviewed Date | 15 | Date |
| M | Next Review Date | 15 | Auto-calculate |
| N | Confidentiality Level | 15 | Dropdown: Public/Internal/Confidential/Restricted |
| O | Notes | 30 | Text |

**Rows 5-104:** 100 evidence rows (yellow highlighted)

---

## Sheet 12: Summary_Dashboard

### Purpose
Executive summary with KPIs and technique coverage metrics.

### Header Section
**Row 1:** "MASKING TECHNIQUE IMPLEMENTATION DASHBOARD"  
**Row 2:** "Executive summary with technique coverage and compliance status"

### Technique Implementation Summary (Rows 4-13)

| Technique | Approved? | Implemented? | Systems Covered | Data Categories Covered | Compliance % |
|-----------|-----------|--------------|-----------------|------------------------|--------------|
| TECH-SDM | Dropdown | Dropdown | =COUNTIF() | Text | =Formula |
| TECH-DDM | Dropdown | Dropdown | =COUNTIF() | Text | =Formula |
| TECH-RED | Dropdown | Dropdown | =COUNTIF() | Text | =Formula |
| TECH-TOK | Dropdown | Dropdown | =COUNTIF() | Text | =Formula |
| TECH-SUB | Dropdown | Dropdown | =COUNTIF() | Text | =Formula |
| TECH-ENC | Dropdown | Dropdown | =COUNTIF() | Text | =Formula |
| TECH-SHF | Dropdown | Dropdown | =COUNTIF() | Text | =Formula |
| TECH-HSH | Dropdown | Dropdown | =COUNTIF() | Text | =Formula |

### Key Performance Indicators (Rows 15-26)

| KPI | Current Value | Target | Status | Trend |
|-----|---------------|--------|--------|-------|
| % Data Categories with Technique Assigned | =Formula | 100% | Conditional | Text |
| % Non-Prod Environments with SDM | =Formula | 100% | Conditional | Text |
| % Prod Systems with DDM (if applicable) | =Formula | 100% | Conditional | Text |
| % Techniques with Irreversibility Validated | =Formula | 100% | Conditional | Text |
| % Techniques with Format Preservation Validated | =Formula | 100% | Conditional | Text |
| % Configuration Standards Compliant | =Formula | >95% | Conditional | Text |
| Open Critical Gaps | =COUNTIFS() | 0 | Conditional | Text |
| Masking Tool License Compliance | =Formula | 100% | Conditional | Text |
| Evidence Completeness | =Formula | >90% | Conditional | Text |

### Assessment Sign-Off (Rows 28-34)

| Role | Name | Signature | Date | Comments |
|------|------|-----------|------|----------|
| Technical Security Architect | Text | Text | Date | Text |
| Chief Technology Officer (CTO) | Text | Text | Date | Text |
| Chief Information Security Officer (CISO) | Text | Text | Date | Text |
| Data Protection Officer (DPO) | Text | Text | Date | Text |
| QA/Test Manager | Text | Text | Date | Text |

---

## Styling & Formatting Standards

### Color Palette
(Same as A.8.11.1)

### Font Standards
(Same as A.8.11.1)

### Cell Protection
(Same as A.8.11.1)

### Freeze Panes
- All assessment sheets: Freeze at Row 7
- Summary Dashboard: Freeze at Row 4

---

## Data Validation & Formulas

### Standard Dropdowns
(Same as A.8.11.1 plus technique-specific)

---

## Workbook Metadata

**File Naming Convention:**  
`ISMS-IMP-A.8.11.2_Masking_Technique_Selection_YYYYMMDD.xlsx`

**Example:**  
`ISMS-IMP-A.8.11.2_Masking_Technique_Selection_20260104.xlsx`

---

## Requirements Traceability

| Policy Req | Requirement | Assessed In Sheet |
|------------|-------------|-------------------|
| Section 2.1 | Static Data Masking (SDM) | Static_Masking_SDM |
| Section 2.2 | Dynamic Data Masking (DDM) | Dynamic_Masking_DDM |
| Section 2.4 | Tokenization | Tokenization_Implementation |
| Section 2.6 | Encryption | Encryption_for_Masking |
| Section 3 | Technique Selection Criteria | Technique_Selection_Matrix |
| Section 4 | Irreversibility Requirements | Configuration_Standards |
| Section 5 | Format Preservation | Configuration_Standards |

---

**END OF SPECIFICATION**

*"Don't just implement masking. Implement the RIGHT masking technique for the RIGHT data in the RIGHT environment."*