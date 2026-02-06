**ISMS-IMP-A.8.11.2-TG - Masking Technique Selection & Requirements**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.11: Data Masking


---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.11.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Masking Technique Selection & Implementation Requirements |
| **Related Policy** | ISMS-POL-A.8.11, Section 2.2 (Masking Technique Standards) |
| **Purpose** | Guide users through selecting appropriate masking techniques for different data types, use cases, and regulatory requirements |
| **Target Audience** | Data Protection Officers, Security Engineers, Database Administrators, Application Developers, Compliance Officers |
| **Assessment Type** | Technical & Operational Decision Framework |
| **Review Cycle** | Semi-Annual (every 6 months) or After Major System Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial user guide for masking technique selection assessment | ISMS Implementation Team |

---

# Technical Specification

---

# Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.11.2 |
| **Version** | 1.0 |
| **Assessment Area** | Masking Technique Selection & Implementation Requirements |
| **Related Policy** | ISMS-POL-A.8.11, Section 2.2 (Masking Technique Standards) |
| **Purpose** | Technical specification for Excel workbook documenting masking technique selection, implementation status, and validation results |
| **Target Audience** | Python Developers, Excel Power Users, ISMS Implementation Teams, Technical Auditors |
| **Specification Type** | Technical Implementation Blueprint |
| **Review Cycle** | Annual or When Python Generator Scripts Updated |
| **Date** | [Date] |

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial Excel workbook specification | ISMS Implementation Team |

---

# Overview

## Purpose of This Specification

This document provides the **complete technical blueprint** for generating the ISMS-IMP-A.8.11.2 Masking Technique Selection & Requirements Assessment Excel workbook using Python (openpyxl).

**What This Specification Defines:**

- Exact Excel workbook structure (12 sheets)
- Column headers, widths, data types, validation rules
- Cell formatting, conditional formatting, protection rules
- Formula specifications with cell references
- Data validation dropdown lists
- Styling standards (colors, fonts, borders)
- Python script integration requirements
- Quality assurance validation criteria

**Target Audience:**

- Python developers implementing the generator script
- Excel power users creating manual workbooks
- Quality assurance teams validating workbook structure
- Technical auditors verifying implementation accuracy

## Workbook Generation Approach

**Automated Generation (Recommended):**
```bash
python3 generate_a811_2_masking_techniques.py
# Output: ISMS-IMP-A.8.11.2_Masking_Techniques_20260120.xlsx
```

**Manual Creation (Not Recommended):**

- Create workbook structure manually following this specification
- Error-prone, time-consuming, difficult to maintain
- Use only if Python environment unavailable

## Key Design Principles

**Technique-Centric, Not Tool-Centric:**

- Focus on WHICH masking techniques are used and HOW configured
- Tool/product-agnostic (works with any masking solution or custom scripts)
- Technique selection decisions remain valid even if tools change

**Evidence-Based Assessment:**

- Every technique selection requires justification rationale
- Every implementation requires validation proof
- Every configuration requires approval
- Audit trail maintained throughout

**Scalability:**

- 50-100 row templates per sheet (expandable)
- Supports organizations with simple masking (1-2 techniques) or complex (all 8 techniques)
- Formula references use dynamic ranges where possible

---

# Workbook Structure Overview

## Sheet Summary

| Sheet # | Sheet Name | Primary Purpose | Row Count | User Input Cells |
|---------|------------|-----------------|-----------|------------------|
| 1 | **Instructions_Legend** | User guide, technique taxonomy reference | ~120 | 5 (metadata) |
| 2 | **Approved_Techniques** | Technique taxonomy (8 categories) | ~50 | 0 (reference only) |
| 3 | **Technique_Selection_Matrix** | Map data elements to techniques | ~120 | 100 data rows |
| 4 | **Static_Masking_SDM** | SDM implementation documentation | ~80 | 50 data rows |
| 5 | **Dynamic_Masking_DDM** | DDM implementation documentation | ~70 | 30 data rows |
| 6 | **Tokenization_Implementation** | Tokenization implementation (if used) | ~70 | 30 data rows |
| 7 | **Encryption_for_Masking** | Encryption implementation (if used) | ~60 | 20 data rows |
| 8 | **Masking_Tool_Inventory** | Tools/scripts used for masking | ~50 | 20 data rows |
| 9 | **Configuration_Standards** | Organization-specific configuration rules | ~60 | Variable |
| 10 | **Gap_Analysis** | Technique selection/implementation gaps | ~60 | 30 data rows |
| 11 | **Evidence_Register** | Compliance evidence tracking | ~60 | 40 data rows |
| 12 | **Summary_Dashboard** | Executive compliance summary | ~90 | 10 (sign-off) |

**Total Sheets:** 12  
**Total Template Capacity:** ~400 assessment data points

---

# Sheet 1: Instructions_Legend

## Purpose
Provide user guidance, technique taxonomy overview, use case guidance, status legends, and acceptable evidence examples.

## Sheet Structure

**Row Layout:**

- Rows 1-2: Document header (title, subtitle)
- Rows 3-11: Document metadata
- Rows 12-28: How to Use This Workbook
- Rows 29-42: Technique Taxonomy Quick Reference
- Rows 43-56: Use Case Guidance
- Rows 57-66: Status Legend
- Rows 67-90: Acceptable Evidence Examples
- Rows 91-110: Key Definitions

## Header Section (Rows 1-2)

**Row 1: Main Title**

- **Cell A1:** "ISMS-IMP-A.8.11.2 – Masking Technique Selection & Requirements"
- **Merge:** A1:Q1
- **Font:** Calibri 16pt Bold, White
- **Fill:** RGB(0, 51, 102) - Dark Blue (#003366)
- **Alignment:** Center, Vertical Center
- **Row Height:** 40px

**Row 2: Subtitle**

- **Cell A2:** "ISO/IEC 27001:2022 - Control A.8.11: Data Masking"
- **Merge:** A2:Q2
- **Font:** Calibri 12pt Regular, White
- **Fill:** RGB(68, 114, 196) - Medium Blue (#4472C4)
- **Alignment:** Center, Vertical Center
- **Row Height:** 25px

## Document Metadata (Rows 4-11)

**Table Format:**
| Row | Column A (Label) | Column B-C (Value) | Styling |
|-----|------------------|-------------------|---------|
| 4 | Document ID: | ISMS-IMP-A.8.11.2 | Label: Bold, Value: Normal |
| 5 | Assessment Area: | Masking Technique Selection & Implementation | |
| 6 | Related Policy: | ISMS-POL-A.8.11, Section 2.2 (Masking Technique Standards) | |
| 7 | Version: | 2.0 | |
| 8 | Assessment Date: | [USER INPUT] | Yellow fill (RGB 255,255,204) |
| 9 | Completed By: | [USER INPUT] | Yellow fill |
| 10 | Organization: | [USER INPUT] | Yellow fill |
| 11 | Review Cycle: | Semi-Annual (every 6 months) | |

**Cell Details:**

- **Column A Width:** 20
- **Column B-C Width:** 40 (merged)
- **Font:** Calibri 10pt
- **Border:** Thin border around each cell

## How to Use This Workbook (Rows 13-28)

**Row 13: Section Header**

- **Cell A13:** "How to Use This Workbook"
- **Merge:** A13:Q13
- **Font:** Calibri 12pt Bold
- **Fill:** RGB(217, 217, 217) - Light Gray (#D9D9D9)
- **Alignment:** Left

**Rows 14-28: Numbered Instructions**
```
1. Review Approved_Techniques sheet to understand technique taxonomy (8 categories)
2. Complete Technique_Selection_Matrix to map data elements to appropriate techniques
3. Document SDM implementations in Static_Masking_SDM sheet
4. Document DDM implementations in Dynamic_Masking_DDM sheet
5. If using tokenization, complete Tokenization_Implementation sheet
6. If using encryption for masking, complete Encryption_for_Masking sheet
7. Document masking tools/solutions in Masking_Tool_Inventory (generic names)
8. Define configuration standards in Configuration_Standards sheet
9. Identify gaps in Gap_Analysis sheet
10. Maintain evidence in Evidence_Register
11. Review summary metrics in Summary_Dashboard
12. Obtain required approvals (data owners, security team, CISO)
13. Archive completed workbook with assessment date in filename
14. Update semi-annually or when new techniques/tools deployed
15. Cross-reference with IMP-A.8.11.1 (Data Inventory) for data element list
```

**Format:**

- **Cell Range:** A14:Q28
- **Font:** Calibri 10pt
- **Wrap Text:** Enabled
- **Indentation:** 1 level

## Technique Taxonomy Quick Reference (Rows 30-42)

**Row 30: Section Header**

- **Cell A30:** "Approved Masking Technique Taxonomy (Quick Reference)"
- **Merge:** A30:F30
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray

**Rows 31-42: Taxonomy Table**

| Row | Technique ID | Technique Name | Reversible? | Format-Preserving? | Typical Use Case |
|-----|--------------|----------------|-------------|-------------------|------------------|
| 32 | TECH-SDM | Static Data Masking | No | Yes | Non-production environments |
| 33 | TECH-DDM | Dynamic Data Masking | Runtime only | Yes | Production role-based access |
| 34 | TECH-RED | Redaction/Nullification | No | No | Complete data removal |
| 35 | TECH-TOK | Tokenization | Yes (with vault) | Optional | Payment cards, reversible pseudonymization |
| 36 | TECH-SUB | Data Substitution (Synthetic) | No | Yes | Realistic test data |
| 37 | TECH-ENC | Encryption (for masking) | Yes (with key) | No | Reversible protection |
| 38 | TECH-SHF | Data Shuffling | No | Yes (values) | Analytics, ML training |
| 39 | TECH-HSH | Hashing (one-way) | No | No | Passwords, integrity checks |

**Column Specifications:**

- **Column A (Technique ID):** Width 12, Font Bold
- **Column B (Technique Name):** Width 25
- **Column C (Reversible?):** Width 15
- **Column D (Format-Preserving?):** Width 18
- **Column E (Typical Use Case):** Width 30, Wrap Text

**Conditional Formatting:**

- Reversible = "Yes" → Light blue fill (RGB 180, 199, 231)
- Reversible = "No" → Light green fill (RGB 198, 239, 206)

## Use Case Guidance (Rows 44-56)

**Row 44: Section Header**

- **Cell A44:** "Use Case to Technique Mapping Guide"
- **Merge:** A44:D44
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray

**Rows 45-56: Use Case Table**

| Use Case | Recommended Techniques | Notes |
|----------|----------------------|-------|
| Non-production testing | SDM, Data Substitution | Irreversible, format-preserving |
| Production role-based access | DDM | Real-time masking based on user role |
| External data sharing | Redaction, Tokenization | Complete obscuration or controlled de-masking |
| Analytics/ML training | Data Substitution, Data Shuffling | Maintain statistical properties |
| Payment processing (PCI-DSS) | Tokenization | Format-preserving, PCI-DSS compliant |
| Data at rest protection | Encryption | Reversible with proper key management |
| Password storage | Hashing (salted) | Irreversible verification |
| GDPR pseudonymization | SDM, Tokenization (vault segregated) | Prevent attribution without additional info |
| HIPAA de-identification | SDM, Redaction, Data Substitution | Safe Harbor compliance |
| Development/debugging | Data Substitution | Realistic but completely fake data |
| Archival/long-term storage | Encryption, Redaction | Based on data retention requirements |

**Column Widths:** A=25, B=30, C=40

## Status Legend (Rows 58-66)

**Row 58: Section Header**

- **Cell A58:** "Implementation Status Legend"
- **Merge:** A58:D58

**Rows 59-66: Status Symbols**

| Symbol | Status | Description | Color Code (RGB) |
|--------|--------|-------------|------------------|
| ✅ | Implemented | Technique fully implemented and validated | 198, 239, 206 (Green) |
| ⚠️ | Partial | Partial implementation (some environments/data) | 255, 235, 156 (Yellow) |
| ❌ | Not Implemented | Technique selected but not yet deployed | 255, 199, 206 (Red) |
| 📋 | Planned | Implementation planned with target date | 180, 199, 231 (Blue) |
| N/A | Not Applicable | Technique not required for this organization | 217, 217, 217 (Gray) |

## Acceptable Evidence (Rows 68-90)

**Row 68: Section Header**

- **Cell A68:** "Acceptable Evidence Examples"
- **Merge:** A68:D68

**Rows 69-90: Bulleted List**
```
✓ Masking tool configuration documentation (exports, screenshots)
✓ Masking scripts and procedures (source code with version control)
✓ Before/after masking sample data (sanitized examples only - no real data)
✓ Technique selection decision matrix with rationale
✓ Irreversibility test results (proof masked data cannot be reversed)
✓ Format preservation validation reports (e.g., Luhn check results)
✓ Referential integrity test results (cross-table consistency proofs)
✓ Performance impact assessments (overhead measurement reports)
✓ Token vault architecture documentation (if tokenization used)
✓ Key management procedures (if encryption used)
✓ Re-identification risk assessments (GDPR/HIPAA compliance)
✓ DDM rule configuration exports (policy definitions)
✓ Data owner approval emails/sign-offs
✓ QA functionality test results (application works with masked data)
✓ Compliance officer review documentation
✓ CISO approval for technique deployment
✓ Audit reports from external assessors (PCI, HIPAA, ISO 27001)
✓ Vendor security documentation (if third-party masking tools)
✓ Training materials for masking tool users
✓ Incident response records (if masking failures occurred)
```

**Format:**

- **Cell Range:** A69:D90
- **Font:** Calibri 10pt
- **Bullet Character:** ✓
- **Line Spacing:** 1.2

## Key Definitions (Rows 92-110)

**Row 92: Section Header**

- **Cell A92:** "Key Definitions & Terminology"
- **Merge:** A92:C92

**Rows 93-110: Definition Table**

| Term | Definition |
|------|------------|
| **Static Data Masking (SDM)** | Irreversible transformation of data in a database, creating a masked copy. Original data replaced with masked values. Commonly used for non-production environments. |
| **Dynamic Data Masking (DDM)** | Real-time masking of data based on user roles/policies. Original data remains unchanged; masking applied at query time. Used in production for role-based access control. |
| **Format Preservation** | Masked data maintains same format as original (e.g., credit card remains 16 digits, Luhn-valid). Critical for application functionality. |
| **Referential Integrity** | Same source value → same masked value across all tables. Ensures relationships between tables remain intact after masking. |
| **Irreversibility** | Masked data cannot be reversed to original value without "disproportionate effort" (GDPR term). Required for pseudonymization. |
| **Tokenization** | Replacement of sensitive data with non-sensitive tokens. Original data stored in secure vault. Reversible with vault access. |
| **Deterministic Masking** | Same input always produces same output. Enables referential integrity but may allow pattern analysis. |
| **Random Masking** | Same input produces different output each time. Prevents pattern analysis but breaks referential integrity. |
| **Luhn Algorithm** | Checksum formula for credit card validation. Format-preserving masking must maintain Luhn validity. |
| **Pseudonymization (GDPR)** | Processing personal data such that it can no longer be attributed to a specific data subject without additional information (kept separately). |
| **De-identification (HIPAA)** | Removing identifiers from data such that it is no longer individually identifiable health information. Safe Harbor = remove 18 identifiers. |
| **Token Vault** | Secure database storing mapping between tokens and original values. Critical security component for tokenization. |
| **Data Shuffling** | Randomizing values within a column, preserving statistical distribution but destroying individual relationships. |
| **Hashing** | One-way cryptographic function. Cannot reverse hash to original value. Used for passwords and integrity checks. |
| **Salt (cryptography)** | Random data added to input before hashing. Prevents rainbow table attacks on hashed passwords. |

**Column Widths:** A=25, B=60

---

# Sheet 2: Approved_Techniques

## Purpose
Comprehensive reference taxonomy for all approved masking techniques. **Read-only reference sheet** for users to understand technique capabilities and selection criteria.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "APPROVED MASKING TECHNIQUE TAXONOMY"
- **Merge:** A1:J1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Reference Guide - Use Technique IDs when documenting masking implementations (e.g., TECH-SDM for Static Data Masking)"
- **Merge:** A2:J2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Warning Note**

- **Cell A3:** "⚠️ This is a REFERENCE sheet. Do not modify. Use these Technique IDs in Technique_Selection_Matrix and implementation sheets."
- **Merge:** A3:J3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)
- **Border:** Thick border

## Column Headers (Row 5)

| Col | Header | Width | Description |
|-----|--------|-------|-------------|
| A | Technique ID | 12 | Unique identifier (TECH-XXX) |
| B | Technique Name | 25 | Human-readable name |
| C | Description | 40 | Detailed definition |
| D | Reversible? | 12 | Can data be un-masked? |
| E | Format-Preserving? | 15 | Maintains original format? |
| F | Typical Use Cases | 30 | When to use this technique |
| G | Pros | 30 | Advantages of this technique |
| H | Cons | 30 | Limitations/disadvantages |
| I | Regulatory Alignment | 25 | Which regulations accept this |
| J | Complexity | 12 | Implementation complexity (Low/Medium/High) |

**Header Row Formatting:**

- **Row Height:** 40px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 6

## Data Rows (Rows 6-13) - The 8 Approved Techniques

**Row 6: TECH-SDM (Static Data Masking)**
| Col | Value |
|-----|-------|
| A | TECH-SDM |
| B | Static Data Masking |
| C | Permanent, irreversible transformation of data creating masked database copy. Original data replaced with masked values. |
| D | No |
| E | Yes (configurable) |
| F | Non-production environments (Dev, Test, UAT), Data sharing with third parties, Archival datasets |
| G | Irreversible (cannot reverse to original), Format preservation possible, Referential integrity maintainable, No ongoing performance impact |
| H | One-time or periodic masking (not real-time), Requires data refresh process, Original data lost in masked copy |
| I | GDPR Art.32 (Pseudonymization), FADP Art.8, PCI-DSS Req.3.4, HIPAA Safe Harbor |
| J | Medium |

**Row 7: TECH-DDM (Dynamic Data Masking)**
| Col | Value |
|-----|-------|
| A | TECH-DDM |
| B | Dynamic Data Masking |
| C | Real-time masking based on user roles/policies. Original data unchanged; masking applied at query execution time. |
| D | Runtime only (original data accessible to authorized roles) |
| E | Yes |
| F | Production role-based access control, Customer service applications, Executive dashboards |
| G | Real-time (no data duplication), Role-based (different users see different masking), Original data preserved |
| H | Performance overhead (per-query masking), Requires DDM-capable infrastructure, Complexity in policy management |
| I | GDPR Art.32, SOC 2 CC6.1, ISO 27001 A.9.4.1 |
| J | High |

**Row 8: TECH-RED (Redaction/Nullification)**
| Col | Value |
|-----|-------|
| A | TECH-RED |
| B | Redaction / Nullification |
| C | Complete removal of data. Replace with NULL, blank, or fixed string (e.g., "REDACTED"). Data completely obscured. |
| D | No |
| E | No (original format lost) |
| F | GDPR Right to Erasure, Data minimization, Unneeded fields in datasets, Legal hold redaction |
| G | Simple to implement, Absolute data protection (no data = no risk), Clear compliance (data removed) |
| H | Data utility lost (cannot use for analytics), Not format-preserving, Application may break if field expected |
| I | GDPR Art.17 (Right to Erasure), CCPA, Data minimization principles |
| J | Low |

**Row 9: TECH-TOK (Tokenization)**
| Col | Value |
|-----|-------|
| A | TECH-TOK |
| B | Tokenization |
| C | Replace sensitive data with non-sensitive tokens. Original data stored in secure vault. De-tokenization possible with vault access. |
| D | Yes (with vault access) |
| E | Optional (format-preserving or random) |
| F | Payment cards (PCI-DSS), Reversible pseudonymization, Third-party processing requiring selective de-masking |
| G | Reversible (controlled de-tokenization), Format-preserving option (FPE), PCI-DSS compliant (tokens out-of-scope) |
| H | Vault infrastructure required, Vault is single point of failure, De-tokenization latency, Vault security critical |
| I | PCI-DSS Req.3.4, GDPR Art.32 (if vault segregated), FADP Art.8 |
| J | High |

**Row 10: TECH-SUB (Data Substitution)**
| Col | Value |
|-----|-------|
| A | TECH-SUB |
| B | Data Substitution (Synthetic) |
| C | Replace real data with synthetic but realistic data from lookup tables. Data looks real but is completely fabricated. |
| D | No |
| E | Yes |
| F | Demo environments, Third-party data sharing, Development with realistic data, Training datasets |
| G | Realistic data (looks authentic), Format-preserving, Referential integrity possible (deterministic substitution) |
| H | Requires lookup table maintenance, May not preserve statistical distribution, Synthetic data may not cover all edge cases |
| I | GDPR pseudonymization, HIPAA de-identification, FADP Art.8 |
| J | Medium |

**Row 11: TECH-ENC (Encryption for Masking)**
| Col | Value |
|-----|-------|
| A | TECH-ENC |
| B | Encryption (for masking) |
| C | Encrypt data with cryptographic key. Reversible with key access. NOT true masking (reversible) but used for data-at-rest protection. |
| D | Yes (with key) |
| E | No (ciphertext format different from plaintext) |
| F | Data-at-rest protection, Regulatory compliance (HIPAA), Reversible temporary masking, Backup encryption |
| G | Standard cryptographic controls (AES-256), Mature key management practices, Reversible for authorized use |
| H | NOT irreversible (key compromise = data exposure), Not format-preserving, Key management overhead, Performance impact |
| I | HIPAA 164.312, GDPR Art.32 (if key segregated), FADP Art.8, PCI-DSS Req.3.4 (with strong key management) |
| J | Medium |

**Row 12: TECH-SHF (Data Shuffling)**
| Col | Value |
|-----|-------|
| A | TECH-SHF |
| B | Data Shuffling |
| C | Randomize values within a column. Preserves statistical distribution but destroys individual relationships. |
| D | No |
| E | Yes (value format preserved) |
| F | Analytics datasets, Machine learning training, Statistical reporting, Research datasets |
| G | Preserves statistical properties (mean, variance, distribution), Format-preserving (values), Prevents individual re-identification |
| H | Destroys referential integrity (intentional), Cannot trace individual records, May enable correlation attacks if multiple datasets shuffled |
| I | GDPR research exemption, CCPA de-identification, Research use case exemptions |
| J | Low |

**Row 13: TECH-HSH (Hashing)**
| Col | Value |
|-----|-------|
| A | TECH-HSH |
| B | Hashing (One-Way) |
| C | One-way cryptographic transformation. Cannot reverse hash to original. Used for verification/authentication, not data utility. |
| D | No |
| E | No (hash output format different from input) |
| F | Password storage, Integrity verification, Unique identifier generation (non-reversible) |
| G | Irreversible (cannot derive original from hash), Fast computation, Standard cryptographic practice (bcrypt, SHA-256) |
| H | No data utility (cannot use hashed data), Vulnerable to rainbow tables (requires salt), Not format-preserving |
| I | NIST SP 800-63B (password hashing), GDPR Art.32, ISO 27001 A.9.4.3 |
| J | Low |

**Formatting for All Data Rows:**

- **Font:** Calibri 10pt Regular
- **Border:** Thin borders all cells
- **Wrap Text:** Enabled for columns C, F, G, H, I
- **Alignment:** Left for text, Center for Column A, D, E, J
- **Protection:** Locked (read-only reference)

## Technique Comparison Matrix (Rows 15-28)

**Row 15: Section Header**

- **Cell A15:** "TECHNIQUE COMPARISON MATRIX"
- **Merge:** A15:J15
- **Font:** Calibri 12pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Row 16: Comparison Table Headers**

| Criteria | SDM | DDM | Redaction | Tokenization | Substitution | Encryption | Shuffling | Hashing |
|----------|-----|-----|-----------|--------------|--------------|------------|-----------|---------|
| Irreversible? | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Format-Preserving? | ✅ | ✅ | ❌ | ✅/❌ | ✅ | ❌ | ✅ | ❌ |
| Maintains Data Utility? | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | Partial | ❌ |
| Real-Time Masking? | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Referential Integrity? | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ |
| PCI-DSS Compliant? | ✅ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| GDPR Pseudonymization? | ✅ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ |
| Implementation Complexity | Medium | High | Low | High | Medium | Medium | Low | Low |
| Performance Impact | Low (one-time) | Medium (per-query) | None | Medium (vault) | Low | Medium | Low | Low |
| Cost (Infrastructure) | Low | Medium | None | High | Low | Low | None | None |

**Legend:**

- ✅ = Yes / Supported
- ❌ = No / Not Supported
- ⚠️ = Conditional (depends on configuration)
- Partial = Limited support

**Conditional Formatting:**

- ✅ cells → Green fill (RGB 198, 239, 206)
- ❌ cells → Red fill (RGB 255, 199, 206)
- ⚠️ cells → Yellow fill (RGB 255, 235, 156)

---

# Sheet 3: Technique_Selection_Matrix

## Purpose
Map each sensitive data element to appropriate masking technique(s) with documented selection rationale and data owner approval.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "TECHNIQUE SELECTION MATRIX (Data Element to Technique Mapping)"
- **Merge:** A1:O1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "For each sensitive data element, select appropriate masking technique(s) with documented rationale (100 row template)"
- **Merge:** A2:O2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Has [Organization] completed technique selection for all sensitive data elements?"
- **Merge:** A3:K3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell L4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** L4:O4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Data Element ID | 15 | Lookup | Reference IMP-A.8.11.1 Sensitive_Data_Inventory!A:A |
| B | Field Name | 20 | Auto-populate | From IMP-A.8.11.1 |
| C | Data Category | 15 | Auto-populate | From IMP-A.8.11.1 |
| D | Sensitivity Level | 12 | Auto-populate | From IMP-A.8.11.1 Classification_Matrix |
| E | Primary Use Case | 20 | Dropdown | Non-Production Testing, Production Role-Based Access, Analytics/Reporting, Third-Party Data Sharing, Regulatory Compliance, Development/Debugging, Archival/Storage, Other |
| F | Functionality Requirements | 30 | Text | Specific requirements (Luhn check, referential integrity, etc.) |
| G | Reversible? | 15 | Dropdown | Never (Irreversible), Authorized Users Only (DDM), Specific Scenarios (Tokenization/Encryption), Emergency Only (Break-Glass) |
| H | Primary Technique | 20 | Dropdown | Static Data Masking (SDM), Dynamic Data Masking (DDM), Redaction/Nullification, Tokenization, Data Substitution (Synthetic), Encryption (for masking), Data Shuffling, Hashing (one-way) |
| I | Specific Method / Config | 30 | Text | HOW technique configured (format, algorithm, etc.) |
| J | Alternative Technique | 20 | Dropdown | Same options as Primary Technique, or "None" |
| K | Selection Rationale | 40 | Text | WHY this technique chosen (200-300 words) |
| L | Data Owner | 18 | Text | Name and role |
| M | Approval Status | 15 | Dropdown | ✅ Approved, ⚠️ Pending, ❌ Rejected, 📋 Under Review |
| N | Approval Date | 12 | Date | Date picker |
| O | Notes | 25 | Text | Additional context |

**Header Row Formatting:**

- **Row Height:** 40px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | DE-001 |
| B | credit_card_number |
| C | CAT-FIN |
| D | Critical |
| E | Non-Production Testing |
| F | Must pass Luhn check, maintain 16-digit format, support payment gateway integration testing, referential integrity across orders/payments/refunds tables |
| G | Specific Scenarios (Tokenization/Encryption) |
| H | Tokenization |
| I | Format-preserving tokenization (FF3-1 algorithm), 16-digit Luhn-valid tokens, deterministic (same card → same token), token vault with AES-256 encryption, de-tokenization requires 2FA |
| J | Static Data Masking (SDM) |
| K | Tokenization selected for credit card PAN based on: (1) PCI-DSS Req.3.4 explicitly allows tokenization, (2) Format-preserving tokens maintain 16-digit Luhn-valid format for application compatibility, (3) Reversibility required for authorized payment processor integration testing, (4) Token vault architecture segregates sensitive data, (5) Referential integrity maintained (deterministic tokenization). Alternative SDM rejected due to irreversibility (need de-tokenization for payment gateway testing). CFO approved as data owner (15.01.2026). |
| L | Jane Smith - Chief Financial Officer (CFO) |
| M | ✅ Approved |
| N | 15.01.2026 |
| O | Token vault HA architecture with DR failover. Performance tested: <20ms per token lookup. |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic

## Data Entry Rows (Rows 8-107)

**100 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked for E-O; Locked for A-D (auto-populate from IMP-A.8.11.1)

**Auto-populate Formulas:**

**Column B (Field Name):**
```excel
=IFERROR(VLOOKUP(A8,'[ISMS-IMP-A.8.11.1.xlsx]Sensitive_Data_Inventory'!$A:$F,6,FALSE),"")
```
Explanation: Lookup Data Element ID, return Field Name from IMP-A.8.11.1 workbook

**Column C (Data Category):**
```excel
=IFERROR(VLOOKUP(A8,'[ISMS-IMP-A.8.11.1.xlsx]Sensitive_Data_Inventory'!$A:$H,8,FALSE),"")
```

**Column D (Sensitivity Level):**
```excel
=IFERROR(VLOOKUP(A8,'[ISMS-IMP-A.8.11.1.xlsx]Classification_Matrix'!$A:$D,4,FALSE),"")
```

**Conditional Formatting (Column M - Approval Status):**

- ✅ Approved → Green fill (RGB 198, 239, 206)
- ⚠️ Pending → Yellow fill (RGB 255, 235, 156)
- ❌ Rejected → Red fill (RGB 255, 199, 206)
- 📋 Under Review → Blue fill (RGB 180, 199, 231)

**Data Validation (Column K - Selection Rationale):**
```excel
Custom: =LEN(K8)>=100
Error Alert: "Rationale too brief. Provide 200-300 word justification including regulatory, functional, and security reasons."
```

---

# Sheet 4: Static_Masking_SDM

## Purpose
Document all Static Data Masking (SDM) implementations across non-production and archival environments. Track masking configuration, validation status, and compliance.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "STATIC DATA MASKING (SDM) IMPLEMENTATION"
- **Merge:** A1:P1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Document SDM implementations across all non-production environments (50 row template)"
- **Merge:** A2:P2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Is Static Data Masking implemented and validated for all required environments and data elements?"
- **Merge:** A3:L3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell M4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** M4:P4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Environment Name | 15 | Dropdown | Dev, Test, UAT, Training, Analytics, DR/Backup, Archive, Other |
| B | Data Element ID | 15 | Lookup | Reference Technique_Selection_Matrix!A:A |
| C | Field Name | 20 | Auto-populate | From Technique_Selection_Matrix |
| D | Table/Schema Name | 20 | Text | Database.schema.table format |
| E | Masking Required? | 15 | Dropdown | Yes, No, Conditional, Under Review |
| F | Currently Masked? | 15 | Dropdown | Yes, No, Partial |
| G | Masking Technique Used | 20 | Dropdown | Format-Preserving Substitution, Random Substitution, Data Substitution (Lookup), Data Shuffling, Redaction (NULL/Blank), Fixed Value, Hashing, Other |
| H | Masking Tool/Script | 20 | Text | Tool name or script filename |
| I | Masking Configuration | 35 | Text | Detailed configuration (algorithm, format, etc.) |
| J | Referential Integrity? | 15 | Dropdown | Yes (Maintained), No (Broken), Partial, N/A |
| K | Last Masking Date | 12 | Date | Date picker |
| L | Masking Validated? | 15 | Dropdown | Yes, No, Partial, Pending |
| M | Validation Evidence | 25 | Text | File reference or test ID |
| N | Compliance Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, 📋 Under Review, N/A |
| O | Issues/Gaps | 25 | Text | Known problems or limitations |
| P | Notes | 25 | Text | Additional context |

**Header Row Formatting:**

- **Row Height:** 40px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | UAT |
| B | DE-001 |
| C | credit_card_number |
| D | payments_db.public.transactions |
| E | Yes |
| F | Yes |
| G | Format-Preserving Substitution |
| H | Delphix Data Masking Engine v6.0 |
| I | Algorithm: Format-preserving substitution preserving first 6 digits (BIN) + last 4, masking middle 6 with random digits. Luhn validity maintained. Deterministic masking (same card → same masked value) for referential integrity across transactions, orders, refunds tables. Masking seed: UAT-2026-Q1. |
| J | Yes (Maintained) |
| K | 15.01.2026 |
| L | Yes |
| M | Test report: /compliance/sdm-validation/UAT_CreditCard_20260115.pdf - 100% Luhn valid, 0% reversible |
| N | ✅ Compliant |
| O | [None] |
| P | Last refresh during quarterly UAT data refresh. Next refresh: 15.04.2026 |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic

## Data Entry Rows (Rows 8-57)

**50 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked for A, D-P; Locked for B-C (auto-populate)

**Auto-populate Formulas:**

**Column C (Field Name):**
```excel
=IFERROR(VLOOKUP(B8,Technique_Selection_Matrix!$A:$B,2,FALSE),"")
```

**Conditional Formatting (Column N - Compliance Status):**

- ✅ Compliant → Green fill (RGB 198, 239, 206)
- ⚠️ Partial → Yellow fill (RGB 255, 235, 156)
- ❌ Non-Compliant → Red fill (RGB 255, 199, 206)
- 📋 Under Review → Blue fill (RGB 180, 199, 231)
- N/A → Gray fill (RGB 217, 217, 217)

**Conditional Formatting (Column J - Referential Integrity):**

- Yes (Maintained) → Green fill (RGB 198, 239, 206)
- No (Broken) → Red fill (RGB 255, 199, 206)
- Partial → Yellow fill (RGB 255, 235, 156)
- N/A → Gray fill (RGB 217, 217, 217)

## SDM Implementation Checklist (Rows 59-72)

**Row 59: Section Header**

- **Cell A59:** "STATIC DATA MASKING CHECKLIST"
- **Merge:** A59:E59
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Row 60: Table Headers**

| Column | Header | Width |
|--------|--------|-------|
| A | # | 5 |
| B | Checklist Item | 50 |
| C | Status | 15 |
| D | Evidence | 25 |
| E | Notes | 25 |

**Rows 61-72: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is SDM implemented in all non-production environments? | [Dropdown] | [Text] | [Text] |
| 2 | Is masking configuration documented per environment? | [Dropdown] | [Text] | [Text] |
| 3 | Is referential integrity maintained across tables? | [Dropdown] | [Text] | [Text] |
| 4 | Is format preservation validated (e.g., Luhn check)? | [Dropdown] | [Text] | [Text] |
| 5 | Is irreversibility tested and validated? | [Dropdown] | [Text] | [Text] |
| 6 | Is application functionality tested with masked data? | [Dropdown] | [Text] | [Text] |
| 7 | Is masking refresh process automated? | [Dropdown] | [Text] | [Text] |
| 8 | Are masking scripts version-controlled? | [Dropdown] | [Text] | [Text] |
| 9 | Is masking performance acceptable (<8 hour window)? | [Dropdown] | [Text] | [Text] |
| 10 | Are data owners aware of masking in their domains? | [Dropdown] | [Text] | [Text] |
| 11 | Is masking validated after each data refresh? | [Dropdown] | [Text] | [Text] |
| 12 | Are backup/restore processes tested with masked data? | [Dropdown] | [Text] | [Text] |

**Data Validation (Column C):**

- Same status dropdown as other checklists
- Conditional formatting: Green/Yellow/Red based on status

## SDM Performance Metrics (Rows 74-82)

**Row 74: Section Header**

- **Cell A74:** "SDM PERFORMANCE METRICS"
- **Merge:** A74:E74
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray

**Rows 75-82: Metrics Table**

| Metric | Formula | Target | Status |
|--------|---------|--------|--------|
| Total Environments with SDM | `=COUNTA(A8:A57)-COUNTBLANK(A8:A57)` | All non-prod | Info |
| Data Elements Masked | `=COUNTIF(F8:F57,"Yes")` | 100% of required | Conditional |
| Referential Integrity Success Rate (%) | `=COUNTIF(J8:J57,"Yes (Maintained)")/COUNTA(J8:J57)*100` | 100% | Conditional |
| Validation Completion Rate (%) | `=COUNTIF(L8:L57,"Yes")/COUNTA(L8:L57)*100` | 100% | Conditional |
| Compliance Rate (%) | `=COUNTIF(N8:N57,"✅ Compliant")/COUNTA(N8:N57)*100` | ≥95% | Conditional |
| Last Masking Age (Avg Days) | `=AVERAGE(TODAY()-K8:K57)` | <90 days | Conditional |
| Open Issues | `=COUNTA(O8:O57)-COUNTBLANK(O8:O57)` | 0 | Conditional |

**Conditional Formatting (Status Column):**

- Green: Metric meets target
- Yellow: Metric within acceptable range
- Red: Metric below target

---

# Sheet 5: Dynamic_Masking_DDM

## Purpose
Document Dynamic Data Masking (DDM) implementations in production environments. Track role-based policies, performance impact, and audit logging.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "DYNAMIC DATA MASKING (DDM) IMPLEMENTATION"
- **Merge:** A1:N1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Document DDM implementations in production environments with role-based masking policies (30 row template)"
- **Merge:** A2:N2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Is Dynamic Data Masking implemented for all production systems requiring role-based access control?"
- **Merge:** A3:J3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell K4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** K4:N4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | System Name | 20 | Text | Production system identifier |
| B | Data Element ID | 15 | Lookup | Reference Technique_Selection_Matrix!A:A |
| C | Field Name | 20 | Auto-populate | From Technique_Selection_Matrix |
| D | DDM Policy Name | 20 | Text | Policy/rule identifier |
| E | Role/User Group | 20 | Text | Which role does this rule apply to? |
| F | Masking Rule | 35 | Text | Transformation applied (e.g., "SUBSTRING(ssn,1,3)+'-XX-XXXX'") |
| G | Masking Applied When? | 18 | Dropdown | SELECT Queries, Application UI, Reports, API Responses, All Access, Other |
| H | Exceptions/Bypass | 20 | Text | Conditions where masking bypassed |
| I | Performance Impact | 15 | Dropdown | Negligible (<5ms), Low (5-10ms), Moderate (10-50ms), High (>50ms), Not Measured |
| J | Performance Acceptable? | 15 | Dropdown | Yes, No, Needs Optimization |
| K | DDM Tested? | 15 | Dropdown | Yes, No, Partial, Pending |
| L | Audit Logging Enabled? | 15 | Dropdown | Yes, No, Partial |
| M | Compliance Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, 📋 Under Review |
| N | Notes | 25 | Text | Additional context |

**Header Row Formatting:**

- **Row Height:** 40px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | Customer CRM (Production) |
| B | DE-002 |
| C | customer_ssn |
| D | SSN_RoleBasedMasking_v1 |
| E | Customer_Service_Agents |
| F | CONCAT(SUBSTRING(ssn,1,3), '-XX-XXXX') - Show first 3 digits + masked remainder |
| G | SELECT Queries |
| H | Break-glass: Security team can bypass with 2FA + manager approval (logged) |
| I | Low (5-10ms) |
| J | Yes |
| K | Yes |
| L | Yes |
| M | ✅ Compliant |
| N | Policy tested with 500 concurrent users. Audit log retention: 7 years. |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic

## Data Entry Rows (Rows 8-37)

**30 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked for A, D-N; Locked for B-C (auto-populate)

**Auto-populate Formula:**

**Column C (Field Name):**
```excel
=IFERROR(VLOOKUP(B8,Technique_Selection_Matrix!$A:$B,2,FALSE),"")
```

**Conditional Formatting (Column I - Performance Impact):**

- Negligible (<5ms) → Green fill (RGB 198, 239, 206)
- Low (5-10ms) → Light green fill (RGB 226, 239, 218)
- Moderate (10-50ms) → Yellow fill (RGB 255, 235, 156)
- High (>50ms) → Red fill (RGB 255, 199, 206)
- Not Measured → Gray fill (RGB 217, 217, 217)

**Conditional Formatting (Column M - Compliance Status):**

- Same as SDM sheet (Green/Yellow/Red/Blue/Gray)

## DDM Role Matrix (Rows 39-52)

**Row 39: Section Header**

- **Cell A39:** "DDM ROLE-BASED MASKING MATRIX"
- **Merge:** A39:F39
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray

**Row 40: Column Headers**

| Role | SSN | Credit Card | Account Balance | Email | Phone |
|------|-----|-------------|-----------------|-------|-------|

**Rows 41-52: Role Masking Rules**

| Role | SSN | Credit Card | Account Balance | Email | Phone |
|------|-----|-------------|-----------------|-------|-------|
| **Customer Service Agent** | XXX-XX-1234 | XXXX-XXXX-XXXX-1234 | Rounded $100 | [user]@[HASH].com | XXX-XXX-1234 |
| **Customer Service Supervisor** | Full value | Full value | Full value | Full value | Full value |
| **Financial Analyst** | XXX-XX-XXXX (all masked) | XXXX-XXXX-XXXX-XXXX | Full value | [user]@[HASH].com | XXX-XXX-XXXX |
| **Marketing Analyst** | XXX-XX-XXXX | XXXX-XXXX-XXXX-XXXX | Rounded $1000 | Full value | XXX-XXX-1234 |
| **Executive Dashboard** | XXX-XX-XXXX | XXXX-XXXX-XXXX-XXXX | Aggregated only | N/A | N/A |
| **Database Administrator** | Full value | Full value | Full value | Full value | Full value |
| **Application Developer** | XXX-XX-XXXX | XXXX-XXXX-XXXX-XXXX | Rounded $100 | [user]@[HASH].com | XXX-XXX-1234 |
| **Security Team** | Full value (logged) | Full value (logged) | Full value (logged) | Full value (logged) | Full value (logged) |
| **Auditor** | Full value (logged) | Full value (logged) | Full value (logged) | Full value (logged) | Full value (logged) |
| **Public API** | XXX-XX-XXXX | XXXX-XXXX-XXXX-XXXX | Not exposed | Hashed | XXX-XXX-XXXX |

**Column Widths:** A=25, B=15, C=18, D=18, E=18, F=15

**Formatting:**

- "Full value" cells → Light blue fill (RGB 180, 199, 231)
- Masked values → Yellow fill (RGB 255, 235, 156)
- "Not exposed" / "N/A" → Gray fill (RGB 217, 217, 217)

## DDM Implementation Checklist (Rows 54-65)

**Row 54: Section Header**

- **Cell A54:** "DYNAMIC DATA MASKING CHECKLIST"
- **Merge:** A54:E54
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 55-65: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Are DDM policies defined for all sensitive fields in production? | [Dropdown] | [Text] | [Text] |
| 2 | Is role-based masking correctly configured per role? | [Dropdown] | [Text] | [Text] |
| 3 | Is DDM performance measured and acceptable (<10ms)? | [Dropdown] | [Text] | [Text] |
| 4 | Are DDM policies tested for each user role? | [Dropdown] | [Text] | [Text] |
| 5 | Is audit logging enabled for all DDM policy evaluations? | [Dropdown] | [Text] | [Text] |
| 6 | Are bypass/exception procedures documented and approved? | [Dropdown] | [Text] | [Text] |
| 7 | Is break-glass access logged and reviewed? | [Dropdown] | [Text] | [Text] |
| 8 | Are DDM policies version-controlled? | [Dropdown] | [Text] | [Text] |
| 9 | Is DDM failover tested (what happens if DDM fails)? | [Dropdown] | [Text] | [Text] |
| 10 | Are users trained on DDM (know they see masked data)? | [Dropdown] | [Text] | [Text] |

---

# Sheet 6: Tokenization_Implementation

## Purpose
Document tokenization implementations including token vault architecture, token format, and de-tokenization authorization processes.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "TOKENIZATION IMPLEMENTATION"
- **Merge:** A1:N1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Document tokenization implementations including vault architecture and de-tokenization procedures (30 row template). Mark N/A if tokenization not used."
- **Merge:** A2:N2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Is tokenization properly implemented with secure vault architecture and controlled de-tokenization?"
- **Merge:** A3:J3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell K4:** [Dropdown: Yes / No / Partial / Planned / N/A - Not Using Tokenization]
- **Merge:** K4:N4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Data Element ID | 15 | Lookup | Reference Technique_Selection_Matrix!A:A |
| B | Field Name | 20 | Auto-populate | From Technique_Selection_Matrix |
| C | Token Vault System | 25 | Text | Vault name/description |
| D | Token Format | 18 | Dropdown | Format-Preserving (FPE), Random (UUID/GUID), Custom Format, Other |
| E | Tokenization Algorithm | 20 | Text | Algorithm specification (e.g., FF3-1, AES-128) |
| F | Deterministic? | 15 | Dropdown | Yes (same input → same token), No (random each time) |
| G | Token Lifecycle | 20 | Text | When do tokens expire/rotate? |
| H | De-tokenization Authorization | 30 | Text | Who can de-tokenize and how? |
| I | Vault Encryption | 20 | Text | Vault data encryption method |
| J | Vault Access Controls | 25 | Text | Who/what can access vault? |
| K | Vault Backup/DR | 25 | Text | Backup and disaster recovery strategy |
| L | Performance (ms) | 12 | Number | Average token lookup time (milliseconds) |
| M | Compliance Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, 📋 Under Review, N/A |
| N | Notes | 25 | Text | Additional context |

**Header Row Formatting:**

- **Row Height:** 40px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | DE-001 |
| B | credit_card_number |
| C | Internal Token Vault (PostgreSQL cluster on dedicated infrastructure) |
| D | Format-Preserving (FPE) |
| E | FF3-1 (NIST SP 800-38G) with AES-128 |
| F | Yes (same card → same token) |
| G | Tokens expire on card expiration date. No automatic rotation. |
| H | Payment Gateway API with client certificate authentication (2FA). Manual de-tokenization requires CISO approval + audit trail. |
| I | AES-256 encryption at rest (transparent data encryption), TLS 1.3 in transit |
| J | Service accounts only (no human access). Vault admin console requires 2FA + IP whitelist. |
| K | Daily encrypted backups to offsite S3 bucket. DR site with async vault replica (RPO: 5 minutes). |
| L | 18 |
| M | ✅ Compliant |
| N | Vault architecture reviewed by PCI assessor (approved 10.01.2026). HA setup with 3-node cluster. |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic

## Data Entry Rows (Rows 8-37)

**30 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked for C-N; Locked for A-B (auto-populate)

**Auto-populate Formula:**

**Column B (Field Name):**
```excel
=IFERROR(VLOOKUP(A8,Technique_Selection_Matrix!$A:$B,2,FALSE),"")
```

**Conditional Formatting (Column L - Performance):**

- <20ms → Green fill (RGB 198, 239, 206)
- 20-50ms → Yellow fill (RGB 255, 235, 156)
- >50ms → Red fill (RGB 255, 199, 206)

**Conditional Formatting (Column M - Compliance Status):**

- Same as previous sheets (Green/Yellow/Red/Blue/Gray)

## Token Vault Architecture Diagram (Rows 39-55)

**Row 39: Section Header**

- **Cell A39:** "TOKEN VAULT ARCHITECTURE OVERVIEW"
- **Merge:** A39:F39
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray

**Rows 40-55: Architecture Description (Text Block)**
```
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                         │
│  - Payment Processing App                                    │
│  - Customer Service Portal                                   │
│  - Reporting/Analytics Systems                               │
└─────────────────────────────────────────────────────────────┘
                           │
                           │ TLS 1.3 Encrypted
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    TOKEN VAULT API                           │
│  - Tokenization Endpoint: /api/v1/tokenize                  │
│  - De-tokenization Endpoint: /api/v1/detokenize             │
│  - Authentication: Client certificate + JWT                  │
│  - Rate Limiting: 10,000 req/sec                            │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              TOKEN VAULT DATABASE CLUSTER                    │
│  - PostgreSQL 14 (3-node HA cluster)                        │
│  - Encryption: AES-256 at rest (TDE)                        │
│  - Replication: Synchronous (RPO: 0)                        │
│  - Backup: Daily to offsite encrypted S3                    │
│  - Access: Service accounts only (no human access)          │
└─────────────────────────────────────────────────────────────┘
                           │
                           │ Async Replication
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   DR SITE TOKEN VAULT                        │
│  - PostgreSQL replica (async replication)                   │
│  - RPO: 5 minutes, RTO: 1 hour                             │
│  - Tested quarterly (last test: 15.01.2026)                │
└─────────────────────────────────────────────────────────────┘

SECURITY CONTROLS:

- Network Segmentation: Token vault on isolated VLAN
- Firewall Rules: Only whitelisted IPs can access vault
- Audit Logging: All tokenization/de-tokenization logged
- Key Management: Vault encryption keys in HSM
- Access Review: Quarterly review of vault access permissions

```

**Format:** Monospace font (Courier New 9pt) to preserve ASCII art alignment

## Tokenization Checklist (Rows 57-68)

**Row 57: Section Header**

- **Cell A57:** "TOKENIZATION IMPLEMENTATION CHECKLIST"
- **Merge:** A57:E57
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 58-68: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is token vault on segregated infrastructure (not same as application DB)? | [Dropdown] | [Text] | [Text] |
| 2 | Is vault data encrypted at rest (AES-256 or stronger)? | [Dropdown] | [Text] | [Text] |
| 3 | Is vault access restricted to service accounts only (no human access)? | [Dropdown] | [Text] | [Text] |
| 4 | Is de-tokenization authorization process documented and enforced? | [Dropdown] | [Text] | [Text] |
| 5 | Is vault backup encrypted and stored offsite? | [Dropdown] | [Text] | [Text] |
| 6 | Is DR failover tested (vault recovery procedures)? | [Dropdown] | [Text] | [Text] |
| 7 | Is tokenization performance acceptable (<20ms per token)? | [Dropdown] | [Text] | [Text] |
| 8 | Are all tokenization/de-tokenization operations logged? | [Dropdown] | [Text] | [Text] |
| 9 | Is token format appropriate for use case (FPE vs random)? | [Dropdown] | [Text] | [Text] |
| 10 | Is PCI-DSS compliance validated (if payment cards tokenized)? | [Dropdown] | [Text] | [Text] |

---

# Sheet 7: Encryption_for_Masking

## Purpose
Document encryption implementations used for masking purposes (distinct from transport/storage encryption). Track key management and de-encryption procedures.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "ENCRYPTION FOR MASKING IMPLEMENTATION"
- **Merge:** A1:M1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Document encryption used for masking (reversible data protection). Mark N/A if encryption not used for masking. (20 row template)"
- **Merge:** A2:M2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Is encryption for masking properly implemented with secure key management and controlled de-encryption?"
- **Merge:** A3:I3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell J4:** [Dropdown: Yes / No / Partial / Planned / N/A - Not Using Encryption for Masking]
- **Merge:** J4:M4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Data Element ID | 15 | Lookup | Reference Technique_Selection_Matrix!A:A |
| B | Field Name | 20 | Auto-populate | From Technique_Selection_Matrix |
| C | Encryption Algorithm | 20 | Dropdown | AES-256-GCM, AES-128-GCM, RSA-2048, RSA-4096, ChaCha20-Poly1305, Other |
| D | Key Length (bits) | 12 | Dropdown | 128, 192, 256, 2048, 4096, Other |
| E | Key Storage | 25 | Dropdown | HSM (Hardware Security Module), Cloud KMS (AWS/Azure/GCP), Key Vault, Database (encrypted), File (encrypted), Other |
| F | Key Rotation Frequency | 18 | Dropdown | Monthly, Quarterly, Annually, On-Demand, Never, Other |
| G | Last Key Rotation | 12 | Date | Date picker |
| H | De-encryption Authorization | 30 | Text | Who can decrypt and how? |
| I | Key Access Controls | 25 | Text | Who/what can access encryption keys? |
| J | Key Backup/Escrow | 25 | Text | Key recovery procedures |
| K | Performance Impact | 15 | Dropdown | Negligible, Low, Moderate, High, Not Measured |
| L | Compliance Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, 📋 Under Review, N/A |
| M | Notes | 25 | Text | Additional context |

**Header Row Formatting:**

- **Row Height:** 40px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | DE-005 |
| B | patient_medical_records |
| C | AES-256-GCM |
| D | 256 |
| E | HSM (Hardware Security Module) - Thales Luna Network HSM |
| F | Quarterly |
| G | 15.01.2026 |
| H | HIPAA-authorized personnel only (Privacy Officer approval required). Decryption logged with audit trail. Break-glass for medical emergencies (logged, reviewed daily). |
| I | HSM access requires 2-factor authentication + IP whitelist. Master key never leaves HSM. Data encryption keys (DEKs) wrapped by master key. |
| J | Key backup: Master key split across 3 key custodians (3-of-3 quorum required for recovery). Annual key recovery test (last: 10.12.2025). |
| K | Low |
| L | ✅ Compliant |
| M | HIPAA compliance validated by external assessor (report dated 15.12.2025). Encryption meets NIST SP 800-175B requirements. |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic

## Data Entry Rows (Rows 8-27)

**20 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked for C-M; Locked for A-B (auto-populate)

**Auto-populate Formula:**

**Column B (Field Name):**
```excel
=IFERROR(VLOOKUP(A8,Technique_Selection_Matrix!$A:$B,2,FALSE),"")
```

**Conditional Formatting (Column L - Compliance Status):**

- Same as previous sheets (Green/Yellow/Red/Blue/Gray)

**Data Validation (Column G - Last Key Rotation):**
```excel
Custom: =G8>=TODAY()-365
Warning: "Key rotation older than 1 year. Consider rotating keys."
```

## Key Management Best Practices (Rows 29-45)

**Row 29: Section Header**

- **Cell A29:** "KEY MANAGEMENT BEST PRACTICES"
- **Merge:** A29:D29
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray

**Rows 30-45: Best Practices Table**

| Best Practice | Implementation Guidance | Compliance Reference |
|---------------|------------------------|---------------------|
| **Key Storage** | Store keys in HSM or cloud KMS. NEVER store keys in same database as encrypted data. | NIST SP 800-57, PCI-DSS Req.3.5/3.6 |
| **Key Rotation** | Rotate encryption keys annually minimum. Cryptoperiod: <2 years for AES-256. | NIST SP 800-57 Part 1 |
| **Key Access Control** | Principle of least privilege. Separate key custodians from data administrators. | ISO 27001 A.9.4.1 |
| **Key Backup** | Backup keys securely (encrypted, offsite). Test key recovery procedures annually. | ISO 27001 A.12.3.1 |
| **Key Destruction** | Securely destroy retired keys (overwrite, physical destruction for HSM). | NIST SP 800-88 |
| **Audit Logging** | Log all key access, encryption, decryption operations. Retain logs 7 years minimum. | SOC 2 CC6.1, GDPR Art.30 |
| **Separation of Duties** | Different roles for key generation, key storage, key usage. No single person has full access. | NIST SP 800-57 |
| **Algorithm Selection** | Use NIST-approved algorithms (AES-256, RSA-2048+, ECDSA). Avoid deprecated (DES, MD5, SHA-1). | NIST FIPS 140-2/140-3 |
| **Key Strength** | Symmetric: 256-bit minimum. Asymmetric: 2048-bit minimum (prefer 4096-bit). | NIST SP 800-175B |
| **Crypto Agility** | Design systems to support algorithm upgrades without full system rebuild. | Industry best practice |

**Column Widths:** A=25, B=40, C=25

## Encryption Implementation Checklist (Rows 47-58)

**Row 47: Section Header**

- **Cell A47:** "ENCRYPTION FOR MASKING CHECKLIST"
- **Merge:** A47:E47
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 48-58: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Are encryption keys stored separately from encrypted data? | [Dropdown] | [Text] | [Text] |
| 2 | Are NIST-approved algorithms used (AES-256, RSA-2048+)? | [Dropdown] | [Text] | [Text] |
| 3 | Is key rotation performed at least annually? | [Dropdown] | [Text] | [Text] |
| 4 | Is key access restricted to authorized personnel only? | [Dropdown] | [Text] | [Text] |
| 5 | Are encryption/decryption operations logged? | [Dropdown] | [Text] | [Text] |
| 6 | Is de-encryption authorization process documented? | [Dropdown] | [Text] | [Text] |
| 7 | Are encryption keys backed up securely? | [Dropdown] | [Text] | [Text] |
| 8 | Is key recovery tested (annually minimum)? | [Dropdown] | [Text] | [Text] |
| 9 | Is separation of duties enforced (key custodians vs data admins)? | [Dropdown] | [Text] | [Text] |
| 10 | Are deprecated algorithms avoided (DES, MD5, SHA-1)? | [Dropdown] | [Text] | [Text] |

---

# Sheet 8: Masking_Tool_Inventory

## Purpose
Inventory of all masking tools, scripts, and solutions used by [Organization]. Vendor-agnostic documentation focusing on what capabilities are used, not product marketing.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "MASKING TOOL & SOLUTION INVENTORY"
- **Merge:** A1:L1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Document all masking tools/scripts (commercial, open-source, custom). Focus on capabilities used, not product names. (20 row template)"
- **Merge:** A2:L2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Are all masking tools/scripts documented with version control and access controls?"
- **Merge:** A3:H3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell I4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** I4:L4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Tool/Script Name | 25 | Text | Generic descriptive name (not marketing name) |
| B | Type | 18 | Dropdown | Commercial Tool, Open-Source Tool, Custom Script, Cloud Service, Database Native, Other |
| C | Vendor/Source | 20 | Text | Vendor name or "Internal Development" |
| D | Version | 12 | Text | Version number or commit hash |
| E | Techniques Supported | 25 | Text | Which techniques does this tool support? (SDM, DDM, etc.) |
| F | Used For | 25 | Text | What data/environments is this tool used for? |
| G | Deployment Location | 20 | Dropdown | On-Premises, AWS, Azure, GCP, Hybrid, SaaS, Other |
| H | Access Control | 25 | Text | Who can access/execute this tool? |
| I | License/Cost | 15 | Text | License type or "Internal" |
| J | Last Updated | 12 | Date | Date picker |
| K | Support Contact | 20 | Text | Who maintains/supports this tool? |
| L | Notes | 25 | Text | Additional context |

**Header Row Formatting:**

- **Row Height:** 35px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | Database Data Masking Engine |
| B | Commercial Tool |
| C | Delphix Corporation |
| D | v6.0.12.0 |
| E | Static Data Masking (SDM), Format-Preserving Substitution, Data Substitution, Tokenization |
| F | Non-production database refreshes (UAT, Dev, Test). Credit cards, SSNs, customer names. |
| G | On-Premises (datacenter) |
| H | Database Administrators (3 personnel), Security Engineering Team (2 personnel). Access logged. |
| I | Enterprise License (annual subscription) |
| J | 15.12.2025 |
| K | Database Admin Team (dba@example.com), Vendor Support: support@vendor.example |
| L | Integrated with data refresh automation. Performance: <4 hours for 500GB database. |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic

## Data Entry Rows (Rows 8-27)

**20 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked (all user input)

## Tool Capabilities Matrix (Rows 29-42)

**Row 29: Section Header**

- **Cell A29:** "TOOL CAPABILITIES MATRIX"
- **Merge:** A29:J29
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray

**Row 30: Table Headers**

| Tool/Script Name | SDM | DDM | Tokenization | Encryption | Hashing | Data Substitution | Shuffling | Redaction |
|------------------|-----|-----|--------------|------------|---------|-------------------|-----------|-----------|

**Rows 31-42: Capability Mapping**

Use checkmarks (✓) to indicate which techniques each tool supports:

| Tool/Script Name | SDM | DDM | Tokenization | Encryption | Hashing | Data Substitution | Shuffling | Redaction |
|------------------|-----|-----|--------------|------------|---------|-------------------|-----------|-----------|
| Database Masking Engine | ✓ | ❌ | ✓ | ❌ | ❌ | ✓ | ✓ | ✓ |
| Database Native DDM | ❌ | ✓ | ❌ | ❌ | ❌ | ❌ | ❌ | ✓ |
| Token Vault Service | ❌ | ❌ | ✓ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Custom Python Scripts | ✓ | ❌ | ❌ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [Additional tools...] | | | | | | | | |

**Conditional Formatting:**

- ✓ cells → Green fill (RGB 198, 239, 206)
- ❌ cells → Light gray fill (RGB 217, 217, 217)

## Tool Inventory Checklist (Rows 44-52)

**Row 44: Section Header**

- **Cell A44:** "TOOL INVENTORY CHECKLIST"
- **Merge:** A44:E44
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 45-52: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Are all masking tools documented in inventory? | [Dropdown] | [Text] | [Text] |
| 2 | Are tool versions tracked and documented? | [Dropdown] | [Text] | [Text] |
| 3 | Are custom scripts version-controlled (Git, etc.)? | [Dropdown] | [Text] | [Text] |
| 4 | Is tool access restricted to authorized personnel? | [Dropdown] | [Text] | [Text] |
| 5 | Are commercial licenses current and compliant? | [Dropdown] | [Text] | [Text] |
| 6 | Is tool usage logged (who ran what, when)? | [Dropdown] | [Text] | [Text] |
| 7 | Are support contacts documented and current? | [Dropdown] | [Text] | [Text] |
| 8 | Are tool capabilities validated before use? | [Dropdown] | [Text] | [Text] |

---

# Sheet 9: Configuration_Standards

## Purpose
Organization-specific configuration standards for each masking technique. Defines "how we do masking" for consistency across implementations.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "MASKING CONFIGURATION STANDARDS"
- **Merge:** A1:F1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Define organization-specific configuration standards for each masking technique to ensure consistency (variable row count)"
- **Merge:** A2:F2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Are masking configuration standards documented and enforced across all implementations?"
- **Merge:** A3:D3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell E4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** E4:F4
- **Fill:** Light Yellow (#FFFFCC)

## Sheet Structure (Sections by Technique)

**This sheet uses a free-form structure with sections for each technique:**

---

## Section 1: Static Data Masking (SDM) Standards (Rows 6-25)

**Row 6: Section Header**

- **Cell A6:** "STATIC DATA MASKING (SDM) CONFIGURATION STANDARDS"
- **Merge:** A6:F6
- **Font:** Calibri 12pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 7-25: Standards Documentation (Free Text with Subsections)**
```markdown
**Format Preservation Requirements:**

When REQUIRED:

- Credit cards (PCI-DSS compliance, application validation)
- Phone numbers (international dialing compatibility)
- Email addresses (SMTP validation)
- Dates (application date calculations)
- Numeric fields with business logic (account numbers, etc.)

When ACCEPTABLE to change format:

- Free-text fields (names, addresses, comments)
- Internal identifiers with no validation logic
- Fields not displayed to end users

**Referential Integrity Standards:**

MANDATORY Referential Integrity:

- Customer ID → Customer Name (across all tables)
- Product ID → Product Name (across all tables)
- Account Number → Account Holder (across all tables)

Implementation Method:

- Use deterministic masking (same input → same output)
- Document masking seed per environment (ensures consistency)
- Test cross-table queries after masking

**Irreversibility Validation:**

Test Procedure:
1. Take sample of 1000 masked records
2. Attempt reverse engineering using:

   - Dictionary attack (common values)
   - Pattern analysis (identify substitution patterns)
   - Statistical analysis (frequency distribution)

3. Success Criteria: 0% reversal success rate

Evidence Required:

- Test results report showing 0 successful reversals
- Methodology documentation
- Sample dataset (sanitized)

**Data Substitution Source Standards:**

Names:

- Source: US Census Bureau name database (surnames + given names)
- Maintain gender consistency (male name → male name)
- Maintain cultural appropriateness where possible

Addresses:

- Source: USPS postal database (valid street addresses)
- Maintain country/region consistency
- Use realistic ZIP/postal codes

Email Addresses:

- Format: [firstname].[lastname]@example-masked.com
- Domain: Use organization-controlled test domain
- Uniqueness: Same email → same masked email

**Performance Standards:**

Masking Window:

- Standard: Complete within 8-hour overnight window
- Acceptable: Up to 12 hours for very large databases (>1TB)
- Unacceptable: >12 hours (requires optimization)

Throughput:

- Target: 50GB/hour minimum
- Acceptable: 25-50GB/hour
- Unacceptable: <25GB/hour

**Refresh Frequency:**

Production → Non-Production:

- UAT: Quarterly (or on-demand for major releases)
- Test: Monthly
- Dev: Bi-weekly or on-demand
- Training: Quarterly

Validation After Refresh:

- Run validation suite within 24 hours of refresh
- Fix any referential integrity breaks before environment release

```

**Formatting:**

- **Cell Range:** A7:F25
- **Font:** Calibri 10pt
- **Wrap Text:** Enabled
- **Borders:** Light borders around section

---

## Section 2: Dynamic Data Masking (DDM) Standards (Rows 27-42)

**Row 27: Section Header**

- **Cell A27:** "DYNAMIC DATA MASKING (DDM) CONFIGURATION STANDARDS"
- **Merge:** A27:F27
- **Font:** Calibri 12pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 28-42: Standards Documentation**
```markdown
**Role-Based Policy Standards:**

Policy Naming Convention:

- Format: [DataType]_[RoleType]_[MaskingLevel]_v[Version]
- Example: SSN_CustomerService_PartialMask_v1

Policy Structure:

- Default: DENY (mask everything unless explicitly allowed)
- Role-Specific: Define what each role can see
- Break-Glass: Emergency access with full logging

**Performance Standards:**

Acceptable Overhead:

- Per-Query Latency: <10ms (95th percentile)
- Overall System Impact: <5% CPU increase
- Concurrent Users: Support existing user base without degradation

Unacceptable Performance:

- Per-Query Latency: >50ms
- Overall System Impact: >15% CPU increase
- User complaints about system slowness

Optimization Strategies:

- Cache policy evaluation results (5-minute TTL)
- Index frequently queried masked columns
- Limit DDM to truly sensitive columns (not all columns)

**Audit Logging Standards:**

What to Log:

- User ID accessing masked data
- Timestamp of access
- Data element accessed
- Masking policy applied
- Whether data was masked or unmasked (role-based)
- Query executed (sanitized)

Log Retention:

- Minimum: 7 years (regulatory requirement)
- Storage: Secure log aggregation system (SIEM)
- Access: Audit team and Security team only

**Break-Glass Procedures:**

When Allowed:

- Medical emergency (HIPAA)
- Security incident investigation
- Regulatory audit (with proper authorization)
- Legal hold / litigation

Authorization Required:

- Manager approval (email or ticket)
- 2-Factor Authentication
- Justification documented
- Time-limited access (revoke after 24-48 hours)

Post-Access Review:

- Security team reviews all break-glass access monthly
- Unauthorized access triggers incident response
- Report to CISO and DPO

```

---

## Section 3: Tokenization Standards (Rows 44-58)

**Row 44: Section Header**

- **Cell A44:** "TOKENIZATION CONFIGURATION STANDARDS"
- **Merge:** A44:F44
- **Font:** Calibri 12pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 45-58: Standards Documentation**
```markdown
**Token Format Standards:**

Credit Cards (PCI-DSS):

- Format-Preserving: YES (16 digits, Luhn-valid)
- First 6 + Last 4: Preserve for BIN identification
- Middle 6: Tokenize
- Example: 4532-XXXX-XXXX-1234 (real) → 4532-7891-2345-1234 (token)

SSN/Tax ID:

- Format-Preserving: Optional
- Format: XXX-XX-XXXX maintained OR UUID
- Decision: Based on application validation requirements

Generic Identifiers:

- Format-Preserving: NOT required
- Use UUID/GUID for simplicity
- Example: 12345 → a1b2c3d4-e5f6-7890-abcd-ef1234567890

**Token Vault Security Standards:**

Infrastructure:

- Separate infrastructure from application databases
- Dedicated network segment (VLAN isolation)
- No direct internet access (internal only)

Encryption:

- At Rest: AES-256 (transparent data encryption)
- In Transit: TLS 1.3 minimum
- Master Key: HSM-managed (never in software)

Access Control:

- Human Access: None (service accounts only)
- Service Account: Client certificate authentication
- Admin Console: 2FA + IP whitelist
- Break-Glass: Requires 2-of-3 quorum (key custodians)

**De-tokenization Authorization Standards:**

Automated De-tokenization:

- Payment Gateway: Client certificate + API key
- Rate Limit: 10,000 de-tokenizations/minute
- Alert: >1,000 de-tokenizations/minute from single source

Manual De-tokenization:

- Requires: CISO or CFO approval (email or ticketing system)
- 2-Factor Authentication required
- Justification: Business case documented
- Audit: All manual de-tokenizations reviewed monthly

**Token Lifecycle Standards:**

Token Expiration:

- Payment Cards: Expire on card expiration date
- Permanent Identifiers (SSN): No expiration
- Temporary Identifiers: 90-day expiration

Token Rotation:

- Not Required (tokens are references, not keys)
- Exception: If tokenization algorithm changed, re-tokenize

Token Deletion:

- When Original Data Deleted: Delete token immediately
- Orphaned Tokens: Identify and purge quarterly

```

---

## Section 4: Additional Technique Standards (Rows 60-75)

**Row 60: Section Header**

- **Cell A60:** "OTHER TECHNIQUE CONFIGURATION STANDARDS"
- **Merge:** A60:F60
- **Font:** Calibri 12pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 61-75: Standards for Remaining Techniques**
```markdown
**Data Shuffling Standards:**

When Used:

- Analytics datasets (preserve distribution, destroy individual linkage)
- Machine learning training data
- Statistical reporting

Shuffle Scope:

- Within same column only (e.g., shuffle all salary values)
- Do NOT shuffle across columns (breaks data consistency)

Validation:

- Statistical properties preserved (mean, variance within 5%)
- Individual records cannot be reconstructed

**Hashing Standards:**

Password Hashing:

- Algorithm: bcrypt (work factor: 12) OR Argon2id
- NEVER: MD5, SHA-1, plain SHA-256 (not suitable for passwords)
- Salt: Unique per password (auto-generated by bcrypt/Argon2)

General Hashing:

- Algorithm: SHA-256 minimum (SHA-512 preferred)
- Salt: Required for all hashing (prevents rainbow tables)
- Use Case: Non-reversible identifiers, integrity checks

**Redaction Standards:**

NULL vs Blank vs Fixed String:

- NULL: When field can be nullable in database
- Blank (""): When field is NOT NULL in database
- Fixed String ("REDACTED"): When visual clarity needed (reports, UI)

Field-Level vs Record-Level:

- Field-Level: Redact specific fields only (preferred)
- Record-Level: Delete entire record (GDPR Right to Erasure)

**Encryption for Masking Standards:**

When Used (Encryption NOT Preferred for Masking):

- Only when reversibility absolutely required
- HIPAA compliance (specific regulatory requirement)
- Temporary masking (will be decrypted later)

Key Management:

- Keys stored in HSM or cloud KMS (never in database)
- Key rotation: Annually minimum
- Separate key custodians from data administrators

Algorithm:

- AES-256-GCM (authenticated encryption)
- Avoid: AES-ECB (not secure), DES, 3DES (deprecated)

```

---

# Sheet 10: Gap_Analysis

## Purpose
Document gaps between desired technique selections (from Technique_Selection_Matrix) and actual implementations. Track remediation plans.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "GAP ANALYSIS & REMEDIATION TRACKING"
- **Merge:** A1:N1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Document gaps between desired masking techniques and actual implementation (30 row template)"
- **Merge:** A2:N2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Are all technique selection/implementation gaps documented with remediation plans and target dates?"
- **Merge:** A3:J3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell K4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** K4:N4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Gap ID | 12 | Text | GAP-001, GAP-002, etc. |
| B | Gap Category | 18 | Dropdown | Technique Selection Gap, Implementation Gap, Validation Gap, Configuration Gap, Performance Gap, Compliance Gap, Tool Gap, Documentation Gap |
| C | Gap Description | 35 | Text | Detailed description |
| D | Affected Data/System | 20 | Text | Which data elements or systems |
| E | Current State | 25 | Text | What exists now? |
| F | Desired State | 25 | Text | What should exist? |
| G | Risk Level | 12 | Dropdown | Critical, High, Medium, Low |
| H | Business Impact | 25 | Text | Impact if not addressed |
| I | Remediation Plan | 30 | Text | Specific actions to close gap |
| J | Owner | 18 | Text | Person responsible |
| K | Target Date | 12 | Date | Date picker |
| L | Status | 15 | Dropdown | ✅ Closed, 🔄 In Progress, ❌ Open, 🚫 Blocked, 📋 Planned |
| M | Actual Closure Date | 12 | Date | Date picker |
| N | Notes | 25 | Text | Additional context |

**Header Row Formatting:**

- **Row Height:** 40px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | GAP-001 |
| B | Implementation Gap |
| C | Credit card tokenization selected but not yet implemented in UAT environment |
| D | DE-001 (credit_card_number) / UAT environment |
| E | Currently using Static Data Masking (SDM) with format-preserving substitution |
| F | Tokenization with format-preserving tokens (as per Technique_Selection_Matrix) |
| G | High |
| H | PCI-DSS assessor recommended tokenization for scope reduction. Current SDM meets compliance but tokenization preferred for long-term strategy. |
| I | (1) Procure token vault infrastructure, (2) Configure tokenization policies for credit cards, (3) Test tokenization with payment gateway integration, (4) Deploy to UAT during Q2 refresh, (5) Validate and obtain QA sign-off |
| J | Jane Doe (Security Engineering Lead) |
| K | 30.06.2026 |
| L | 🔄 In Progress |
| M | [blank] |
| N | Token vault procurement approved. Vendor selection in progress. Implementation dependent on infrastructure delivery (expected April 2026). |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic

## Data Entry Rows (Rows 8-37)

**30 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked

**Conditional Formatting (Column G - Risk Level):**

- Critical → Red fill (RGB 255, 199, 206)
- High → Orange fill (RGB 255, 235, 156)
- Medium → Yellow fill (RGB 255, 242, 204)
- Low → Light green (RGB 226, 239, 218)

**Conditional Formatting (Column L - Status):**

- ✅ Closed → Green fill (RGB 198, 239, 206)
- 🔄 In Progress → Blue fill (RGB 180, 199, 231)
- ❌ Open → Red fill (RGB 255, 199, 206)
- 🚫 Blocked → Dark red fill (RGB 192, 0, 0), White text
- 📋 Planned → Gray fill (RGB 217, 217, 217)

## Gap Summary Statistics (Rows 39-52)

**Row 39: Section Header**

- **Cell A39:** "GAP SUMMARY STATISTICS"
- **Merge:** A39:E39
- **Font:** Calibri 12pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 40-52: Statistics Table**

| Metric | Formula | Target | Status |
|--------|---------|--------|--------|
| Total Gaps Identified | `=COUNTA(A8:A37)-COUNTBLANK(A8:A37)` | N/A | Info |
| Critical Gaps | `=COUNTIF(G8:G37,"Critical")` | 0 | Conditional |
| High Risk Gaps | `=COUNTIF(G8:G37,"High")` | <3 | Conditional |
| Gaps Closed | `=COUNTIF(L8:L37,"✅ Closed")` | 100% | Conditional |
| Gaps In Progress | `=COUNTIF(L8:L37,"🔄 In Progress")` | N/A | Info |
| Gaps Open | `=COUNTIF(L8:L37,"❌ Open")` | 0 | Conditional |
| Gaps Blocked | `=COUNTIF(L8:L37,"🚫 Blocked")` | 0 | Conditional |
| Overdue Gaps | `=COUNTIFS(K8:K37,"<"&TODAY(),L8:L37,"<>✅ Closed")` | 0 | Conditional |
| Closure Rate (%) | `=COUNTIF(L8:L37,"✅ Closed")/COUNTA(L8:L37)*100` | 100% | Conditional |
| Avg Days to Close | `=AVERAGEIF(M8:M37,"<>"&"",M8:M37-K8:K37)` | <60 | Conditional |
| Critical Gaps Closed (%) | `=COUNTIFS(G8:G37,"Critical",L8:L37,"✅ Closed")/COUNTIF(G8:G37,"Critical")*100` | 100% | Conditional |

---

# Sheet 11: Evidence_Register

## Purpose
Central repository for all compliance evidence supporting technique selection, implementation, and validation.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "COMPLIANCE EVIDENCE REGISTER"
- **Merge:** A1:L1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center

**Row 2: Instructions**

- **Cell A2:** "Document all evidence supporting masking technique selection and implementation compliance (40 row template)"
- **Merge:** A2:L2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center

**Row 3: Assessment Question**

- **Cell A3:** "Is compliance evidence documented, stored securely, and retrievable for audit purposes?"
- **Merge:** A3:H3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)

**Row 4: Response**

- **Cell I4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** I4:L4
- **Fill:** Light Yellow (#FFFFCC)

## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Evidence ID | 12 | Formula | Auto-generate: EV-001, EV-002, etc. |
| B | Evidence Type | 20 | Dropdown | Technique Selection, Tool Configuration, Test Results, Approval Email, Screenshot, Script/Code, Policy Document, Training Material, Audit Report, Other |
| C | Description | 35 | Text | Brief description |
| D | Related Requirement | 20 | Text | Policy section or checklist item |
| E | Related Data/System | 20 | Text | Which data elements or systems |
| F | File Location | 30 | Text | File path or DMS reference |
| G | Created Date | 12 | Date | Date picker |
| H | Retention Period | 15 | Text | E.g., "7 years", "Indefinite" |
| I | Owner/Custodian | 18 | Text | Who maintains this evidence |
| J | Classification | 15 | Dropdown | Public, Internal, Confidential, Restricted |
| K | Last Verified | 12 | Date | Date picker |
| L | Notes | 25 | Text | Additional information |

**Header Row Formatting:**

- **Row Height:** 35px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7

## Example Row (Row 7)

| Col | Value |
|-----|-------|
| A | EV-001 |
| B | Technique Selection |
| C | Technique Selection Matrix with data owner approvals for financial data domain |
| D | ISMS-POL-A.8.11, Section 2.2 (Masking Technique Standards) |
| E | Credit cards, account numbers (CAT-FIN) |
| F | /compliance/data-masking/technique-selection/Finance_Domain_Approvals_20260115.pdf |
| G | 15.01.2026 |
| H | 7 years |
| I | Data Protection Officer |
| J | Confidential |
| K | 15.01.2026 |
| L | CFO sign-off obtained. Tokenization selected for credit cards, SDM for account numbers. |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic

## Data Entry Rows (Rows 8-47)

**40 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked for B-L; Locked for A (formula)

**Column A (Evidence ID) - Auto-Generate:**
```excel
="EV-"&TEXT(ROW()-7,"000")
```

**Conditional Formatting (Column J - Classification):**

- Restricted → Red fill (RGB 255, 199, 206)
- Confidential → Yellow fill (RGB 255, 235, 156)
- Internal → Light blue (RGB 180, 199, 231)
- Public → White (no fill)

## Evidence Type Distribution (Rows 49-60)

**Row 49: Section Header**

- **Cell A49:** "EVIDENCE TYPE DISTRIBUTION"
- **Merge:** A49:D49
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray

**Rows 50-60: Distribution Table**

| Evidence Type | Count | % of Total | Target % |
|---------------|-------|------------|----------|
| Technique Selection | `=COUNTIF(B8:B47,"Technique Selection")` | Formula | 25-30% |
| Tool Configuration | `=COUNTIF(B8:B47,"Tool Configuration")` | Formula | 20-25% |
| Test Results | `=COUNTIF(B8:B47,"Test Results")` | Formula | 25-30% |
| Approval Email | `=COUNTIF(B8:B47,"Approval Email")` | Formula | 10-15% |
| Other Types | Combined | Formula | <20% |

---

# Sheet 12: Summary_Dashboard

## Purpose
Executive summary consolidating all masking technique assessment data into actionable compliance metrics.

## Header Section (Rows 1-3)

**Row 1: Sheet Title**

- **Cell A1:** "EXECUTIVE SUMMARY DASHBOARD"
- **Merge:** A1:G1
- **Font:** Calibri 16pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center
- **Row Height:** 50px

**Row 2: Assessment Period**

- **Cell A2:** "Assessment Period:"
- **Cell B2:** [User Input - Date Range]
- **Merge:** B2:D2
- **Fill:** Light Yellow (#FFFFCC)

**Row 3: Last Updated**

- **Cell A3:** "Last Updated:"
- **Cell B3:** `=TODAY()`
- **Format:** DD.MM.YYYY

## Overall Compliance Summary (Rows 5-14)

**Row 5: Section Header**

- **Cell A5:** "OVERALL COMPLIANCE STATUS"
- **Merge:** A5:G5
- **Font:** Calibri 14pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 6-14: Key Metrics**

| Metric | Formula | Target | Status |
|--------|---------|--------|--------|
| **Technique Selection Complete (%)** | `=COUNTIF(Technique_Selection_Matrix!M:M,"✅ Approved")/COUNTA(Technique_Selection_Matrix!A8:A107)*100` | 100% | Conditional |
| **SDM Implementation (%)** | `=COUNTIF(Static_Masking_SDM!N:N,"✅ Compliant")/COUNTA(Static_Masking_SDM!A8:A57)*100` | 100% | Conditional |
| **DDM Implementation (%)** | `=COUNTIF(Dynamic_Masking_DDM!M:M,"✅ Compliant")/COUNTA(Dynamic_Masking_DDM!A8:A37)*100` | 100% | Conditional |
| **Tokenization Compliance (%)** | `=IF(COUNTA(Tokenization_Implementation!A8:A37)=0,"N/A",COUNTIF(Tokenization_Implementation!M:M,"✅ Compliant")/COUNTA(Tokenization_Implementation!A8:A37)*100)` | 100% or N/A | Conditional |
| **Critical Gaps Open** | `=COUNTIFS(Gap_Analysis!G:G,"Critical",Gap_Analysis!L:L,"<>✅ Closed")` | 0 | Conditional |
| **High Risk Gaps Open** | `=COUNTIFS(Gap_Analysis!G:G,"High",Gap_Analysis!L:L,"<>✅ Closed")` | <3 | Conditional |
| **Evidence Documents** | `=COUNTA(Evidence_Register!A8:A47)` | >20 | Conditional |
| **Overall Compliance Score** | `=AVERAGE(B6,B7,B8,B9)` | ≥95% | Conditional |

**Conditional Formatting (Status Column):**

- ≥95% or Target Met → Green fill (RGB 198, 239, 206)
- 80-94% → Yellow fill (RGB 255, 235, 156)
- <80% → Red fill (RGB 255, 199, 206)

## Technique Coverage Summary (Rows 16-27)

**Row 16: Section Header**

- **Cell A16:** "TECHNIQUE COVERAGE BY DATA CATEGORY"
- **Merge:** A16:G16
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray

**Rows 17-27: Technique Usage Table**

| Data Category | Data Elements | SDM | DDM | Tokenization | Encryption | Other | Technique Selection Rate |
|---------------|---------------|-----|-----|--------------|------------|-------|-------------------------|
| CAT-PII-D | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| CAT-FIN | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| CAT-HLT | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| CAT-CRD | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| [Other Categories] | | | | | | | |

## Implementation Status by Environment (Rows 29-38)

**Row 29: Section Header**

- **Cell A29:** "IMPLEMENTATION STATUS BY ENVIRONMENT"
- **Merge:** A29:G29
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray

**Rows 30-38: Environment Table**

| Environment | Data Elements | Masked | % Masked | Validated | Compliant | Status |
|-------------|---------------|--------|----------|-----------|-----------|--------|
| Production (DDM) | Formula | Formula | Formula | Formula | Formula | Conditional |
| UAT | Formula | Formula | Formula | Formula | Formula | Conditional |
| Test | Formula | Formula | Formula | Formula | Formula | Conditional |
| Dev | Formula | Formula | Formula | Formula | Formula | Conditional |
| Training | Formula | Formula | Formula | Formula | Formula | Conditional |
| Analytics | Formula | Formula | Formula | Formula | Formula | Conditional |

## Gap Analysis Summary (Rows 40-48)

**Row 40: Section Header**

- **Cell A40:** "GAP ANALYSIS SUMMARY"
- **Merge:** A40:G40
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray

**Rows 41-48: Gap Metrics**

| Gap Category | Total | Open | In Progress | Closed | % Closed | Overdue |
|--------------|-------|------|-------------|--------|----------|---------|
| Technique Selection Gap | Formula | Formula | Formula | Formula | Formula | Formula |
| Implementation Gap | Formula | Formula | Formula | Formula | Formula | Formula |
| Validation Gap | Formula | Formula | Formula | Formula | Formula | Formula |
| Configuration Gap | Formula | Formula | Formula | Formula | Formula | Formula |
| Other Gaps | Formula | Formula | Formula | Formula | Formula | Formula |

## Top 5 Gaps Requiring Attention (Rows 50-56)

**Row 50: Section Header**

- **Cell A50:** "TOP 5 GAPS REQUIRING IMMEDIATE ATTENTION"
- **Merge:** A50:G50
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray

**Rows 51-56: Gap List**

| Rank | Gap ID | Gap Description | Risk Level | Target Date | Owner | Status |
|------|--------|-----------------|------------|-------------|-------|--------|
| 1 | Lookup | Lookup | Lookup | Lookup | Lookup | Lookup |
| 2-5 | ... | ... | ... | ... | ... | ... |

## Assessment Sign-Off (Rows 58-66)

**Row 58: Section Header**

- **Cell A58:** "ASSESSMENT APPROVAL & SIGN-OFF"
- **Merge:** A58:E58
- **Font:** Calibri 12pt Bold
- **Fill:** Medium Blue (#4472C4), White Text

**Rows 59-66: Sign-Off Table**

| Role | Name | Signature | Date | Comments |
|------|------|-----------|------|----------|
| Data Owner (Finance) | [Text] | [Text] | [Date] | [Text] |
| Data Owner (HR) | [Text] | [Text] | [Date] | [Text] |
| Data Owner (Customer Data) | [Text] | [Text] | [Date] | [Text] |
| Security Team Lead | [Text] | [Text] | [Date] | [Text] |
| Compliance Officer | [Text] | [Text] | [Date] | [Text] |
| CISO | [Text] | [Text] | [Date] | [Text] |

**Fill:** Light Yellow (#FFFFCC) for all input cells  
**Protection:** Unlocked for user input

---

# Python Script Integration Notes

## Generator Script: `generate_a811_2_masking_techniques.py`

**CRITICAL: THIS IS A SAMPLE SCRIPT TEMPLATE**
```python
"""
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR CONTROL A.8.11

This script generates the ISMS-IMP-A.8.11.2 Masking Technique Selection &
Requirements Assessment Excel workbook.

CUSTOMIZATION REQUIRED:
1. Update technique taxonomy if organization adds custom techniques
2. Modify validation dropdowns for organization-specific values
3. Adjust formulas to reference correct external workbook (IMP-A.8.11.1)
4. Update data capacity (currently 20-100 rows per sheet)

DO NOT use without reviewing all sections marked "# CUSTOMIZE:"
"""

# Key Functions to Implement:
# - create_workbook(): Initialize workbook with 12 sheets
# - create_instructions_legend(): Sheet 1 with technique taxonomy
# - create_approved_techniques(): Sheet 2 (read-only reference)
# - create_technique_selection_matrix(): Sheet 3 with 100 row capacity
# - create_static_masking_sdm(): Sheet 4 with 50 row capacity
# - create_dynamic_masking_ddm(): Sheet 5 with 30 row capacity
# - create_tokenization_implementation(): Sheet 6 with 30 row capacity
# - create_encryption_for_masking(): Sheet 7 with 20 row capacity
# - create_masking_tool_inventory(): Sheet 8 with 20 row capacity
# - create_configuration_standards(): Sheet 9 (free-form sections)
# - create_gap_analysis(): Sheet 10 with 30 row capacity
# - create_evidence_register(): Sheet 11 with 40 row capacity
# - create_summary_dashboard(): Sheet 12 with consolidated formulas
# - setup_data_validation(): Apply all dropdown validations
# - setup_conditional_formatting(): Apply color-coding rules
# - setup_cell_protection(): Lock formula cells, unlock input cells
# - setup_external_links(): Link to IMP-A.8.11.1 workbook
```

## Key Customization Points

**1. Technique Taxonomy (Sheet 2):**
```python
# CUSTOMIZE: Modify if organization defines additional techniques
APPROVED_TECHNIQUES = [
    {"id": "TECH-SDM", "name": "Static Data Masking", "reversible": False},
    {"id": "TECH-DDM", "name": "Dynamic Data Masking", "reversible": True},
    {"id": "TECH-TOK", "name": "Tokenization", "reversible": True},
    # Add custom techniques here
]
```

**2. External Workbook Links (Sheet 3):**
```python
# CUSTOMIZE: Update path to IMP-A.8.11.1 workbook
EXTERNAL_WORKBOOK = "[ISMS-IMP-A.8.11.1.xlsx]"
EXTERNAL_SHEET_DATA_INVENTORY = "Sensitive_Data_Inventory"
EXTERNAL_SHEET_CLASSIFICATION = "Classification_Matrix"

# Formula template for auto-populate columns
def create_vlookup_formula(row, lookup_col, external_sheet, return_col):
    return f'=IFERROR(VLOOKUP(A{row},\'{EXTERNAL_WORKBOOK}{external_sheet}\'!$A:${chr(64+return_col)},{return_col},FALSE),"")'
```

**3. Validation Dropdowns:**
```python
# CUSTOMIZE: Modify dropdown options if needed
DROPDOWNS = {
    "technique": "Static Data Masking (SDM),Dynamic Data Masking (DDM),Redaction/Nullification,Tokenization,Data Substitution (Synthetic),Encryption (for masking),Data Shuffling,Hashing (one-way)",
    "environment": "Dev,Test,UAT,Training,Analytics,DR/Backup,Archive,Other",
    "status": "✅ Compliant,⚠️ Partial,❌ Non-Compliant,📋 Under Review,N/A",
    "approval": "✅ Approved,⚠️ Pending,❌ Rejected,📋 Under Review"
}
```

**4. Conditional Formatting Rules:**
```python
# CUSTOMIZE: Modify color thresholds if needed
COMPLIANCE_THRESHOLDS = {
    "green": 95,  # ≥95% = Green
    "yellow": 80,  # 80-94% = Yellow
    "red": 0       # <80% = Red
}

# Color definitions (RGB)
COLORS = {
    "green": "C6EFCE",     # Light Green
    "yellow": "FFEB9C",    # Light Yellow
    "red": "FFC7CE",       # Light Red
    "blue": "B4C7E7",      # Light Blue
    "gray": "D9D9D9"       # Light Gray
}
```

## Quality Assurance Script

**Script:** `validate_a811_2_structure.py`
```python
"""
Quality assurance script to validate generated workbook structure.

Validates:

- All 12 sheets present with correct names
- Column headers match specification
- Data validation rules applied correctly
- Conditional formatting ranges correct
- Formula accuracy (spot checks)
- External links to IMP-A.8.11.1 work correctly
- Cell protection properly configured

"""
```

---

# Styling & Formatting Standards

## Global Color Palette

| Element | RGB | Hex | Usage |
|---------|-----|-----|-------|
| Header (Main) | 0, 51, 102 | #003366 | Dark Blue - Main titles |
| Subheader | 68, 114, 196 | #4472C4 | Medium Blue - Section headers |
| Column Headers | 217, 217, 217 | #D9D9D9 | Light Gray - Table headers |
| Input Cells | 255, 255, 204 | #FFFFCC | Light Yellow - User input |
| Status - Compliant | 198, 239, 206 | #C6EFCE | Light Green |
| Status - Partial | 255, 235, 156 | #FFEB9C | Light Yellow |
| Status - Non-Compliant | 255, 199, 206 | #FFC7CE | Light Red |
| Status - Planned | 180, 199, 231 | #B4C7E7 | Light Blue |
| Example Rows | 231, 230, 230 | #E7E6E6 | Light Gray |

## Font Standards

- **Headers:** Calibri 14-16pt Bold
- **Subheaders:** Calibri 11-12pt Bold
- **Column Headers:** Calibri 10pt Bold
- **Data Cells:** Calibri 10pt Regular
- **Example Rows:** Calibri 10pt Italic
- **Monospace (ASCII art):** Courier New 9pt

## Border Standards

- **Outer borders:** Medium weight (2pt)
- **Inner borders:** Thin weight (1pt)
- **Header separator:** Thick bottom border (3pt)

## Cell Protection Strategy

**Protected (Locked):**

- All column headers
- All formula cells
- All reference/example rows
- Instructions and legend text
- Auto-populated cells (B-D in Technique_Selection_Matrix)

**Unprotected (Unlocked):**

- All yellow input cells
- All user data entry rows
- Sign-off fields
- Free-text configuration sections

---

# Workbook Metadata

**File Naming Convention:**  
`ISMS-IMP-A.8.11.2_Masking_Techniques_YYYYMMDD.xlsx`

**Example:**  
`ISMS-IMP-A.8.11.2_Masking_Techniques_20260120.xlsx`

**Excel Document Properties:**
```
Title: ISMS-IMP-A.8.11.2 - Masking Technique Selection & Requirements Assessment
Subject: ISO/IEC 27001:2022 Control A.8.11 Data Masking
Author: [Organization Name]
Company: [Organization Name]
Keywords: ISO 27001, Data Masking, Masking Techniques, SDM, DDM, Tokenization, A.8.11
Comments: Generated from ISMS policy framework. Do not modify structure without updating generator script. External links to ISMS-IMP-A.8.11.1.xlsx required.
```

---

# Requirements Traceability Matrix

This workbook assesses compliance with the following policy requirements:

| Policy Requirement | Description | Assessed In Sheet |
|--------------------|-------------|-------------------|
| REQ-TECH-001 | Select appropriate masking techniques per data type | Sheet 3 (Technique_Selection_Matrix) |
| REQ-TECH-002 | Document technique selection rationale | Sheet 3 (Selection Rationale column) |
| REQ-TECH-003 | Obtain data owner approval for techniques | Sheet 3 (Approval Status) |
| REQ-SDM-001 | Implement SDM in non-production environments | Sheet 4 (Static_Masking_SDM) |
| REQ-DDM-001 | Implement DDM for production role-based access | Sheet 5 (Dynamic_Masking_DDM) |
| REQ-TOK-001 | Implement tokenization with secure vault | Sheet 6 (Tokenization_Implementation) |
| REQ-CONF-001 | Define configuration standards per technique | Sheet 9 (Configuration_Standards) |
| REQ-VAL-001 | Validate masking effectiveness | Sheets 4, 5, 6 (Validation columns) |

---

# Quality Assurance Checklist

Before finalizing the workbook, verify:

**Structure:**

- [ ] All 12 sheets present with correct names
- [ ] Sheet order matches specification
- [ ] All column headers match specification exactly
- [ ] Row counts match template specifications

**Data Validation:**

- [ ] All dropdown lists applied correctly
- [ ] Custom validation rules working
- [ ] Error messages appropriate and helpful

**Formulas:**

- [ ] External links to IMP-A.8.11.1 workbook functional
- [ ] All VLOOKUP formulas reference correct sheets/columns
- [ ] Auto-calculation formulas (Evidence ID, dates) accurate
- [ ] Summary Dashboard formulas consolidate correctly

**Formatting:**

- [ ] Color palette consistent across all sheets
- [ ] Conditional formatting rules applied correctly
- [ ] Fonts and borders match standards
- [ ] Freeze panes set on all assessment sheets

**Protection:**

- [ ] Formula cells locked, input cells unlocked
- [ ] Sheet protection enabled (optional password)
- [ ] Allow filter and sort even when protected

**Content:**

- [ ] Technique taxonomy complete (8 techniques)
- [ ] Configuration standards documented
- [ ] Example rows present on assessment sheets
- [ ] Cell comments/notes on complex fields

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Final Notes for Implementation Team

**Critical Success Factors:**

1. **Technique-Centric Approach:** Focus on WHICH techniques and HOW configured, NOT which vendor products. This ensures framework longevity.

2. **External Workbook Integration:** This workbook depends on IMP-A.8.11.1 (Data Inventory). Ensure external links work correctly.

3. **Evidence-Based:** Every technique selection, every implementation, every validation must have documented evidence. No assumptions.

4. **Configuration Standards:** Sheet 9 is critical for consistency. Organizations must document HOW they configure each technique.

5. **Gap Tracking:** Honest gap identification drives continuous improvement. Don't hide gaps—remediate them.

**Next Steps:**

1. Generate Python script from this specification
2. Test external links to IMP-A.8.11.1 workbook
3. Execute script to create template workbook
4. Validate generated workbook against QA checklist
5. Test with sample organization data
6. Iterate based on usability feedback
7. Deploy to ISMS implementation teams

---

**Document Control:**

- **Version:** 1.0
- **Date:** [Date]
- **Status:** Approved for Implementation
- **Author:** ISMS Implementation Team
- **Approver:** CISO / Data Protection Officer
- **Review Cycle:** Annual or when Control A.8.11 requirements change

---

**END OF SPECIFICATION**

---

*"Insanity is doing the same thing over and over and expecting different results."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
