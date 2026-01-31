# ISMS-POL-A.8.11-S2.2 – Data Masking Techniques
## ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

**Document ID**: ISMS-POL-A.8.11-S2.2  
**Title**: Masking Technique Requirements  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Information Security Officer (ISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager / Technical Security Architect | Initial section document |

**Review Cycle**: Semi-annual (every 6 months), or upon:
- Discovery of vulnerabilities in masking techniques
- Introduction of new masking technologies or methods
- Audit findings or security incidents
- Changes to threat landscape  

**Next Review Date**: [Approval Date + 6 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical: Chief Technology Officer (CTO) or Technical Security Architect
- Privacy/Legal: Data Protection Officer (DPO)
- Quality Assurance: QA/Test Manager (for non-production environments)

**Distribution**: Technical teams, database administrators, developers, DevOps teams  
**Parent Document**: ISMS-POL-A.8.11-S2 - Data Masking Requirements  
**Related Standards**: ISO/IEC 27002:2022 Control 8.11, NIST SP 800-122, GDPR Article 32

---

## 1. Purpose

This section defines the **APPROVED masking techniques** that the organization 
SHALL use to protect sensitive data. These techniques are technology-agnostic 
and apply across all data processing environments.

**What this section covers:**
- Approved masking methods (generic techniques)
- Selection criteria for choosing appropriate techniques
- Irreversibility requirements
- Format preservation considerations
- Technique-specific implementation requirements

**What this section does NOT cover:**
- Specific vendor tools (see implementation guides)
- Detailed WHERE to apply masking (see S2.3 Environment Requirements)
- Specific data field mappings (see implementation workbooks)

---

## 2. Approved Masking Techniques

The organization SHALL use one or more of the following approved masking 
techniques based on data sensitivity and use case requirements:

### 2.1 Static Data Masking (SDM)

**Definition:** Permanent replacement of sensitive data with realistic but 
fictitious data in non-production databases.

**Characteristics:**
- Original data is **irreversibly replaced**
- Masked data maintains referential integrity
- Format and data type preserved
- One-time masking operation

**When to use:**
- Non-production environments (Dev, Test, QA)
- Training databases
- Analytics datasets (where real values not required)
- External data sharing scenarios

**Generic Requirements:**
- SDM SHALL be applied before data leaves production environments
- SDM SHALL maintain data relationships across tables (referential integrity)
- SDM SHALL preserve data format and validation rules
- SDM processes SHALL be repeatable and consistent
- Original data SHALL NOT be recoverable from masked data

**Example Use Cases** (generic):
- Customer names in test database → Realistic fake names
- Credit card numbers → Valid format but fake numbers
- Email addresses → Fake but deliverable-format addresses

**Audit Evidence Requirements:**
- Masking process documentation
- Before/after data samples (sanitized)
- Validation test results
- Referential integrity verification

---

### 2.2 Dynamic Data Masking (DDM)

**Definition:** Real-time masking of data at the point of access based on 
user privileges and context.

**Characteristics:**
- Original data **remains unchanged** in database
- Masking applied at query/retrieval time
- User role-based masking rules
- No performance-critical data modification

**When to use:**
- Production environments with role-based access
- Applications where some users need real data, others don't
- Compliance scenarios requiring audit trails of data access
- Scenarios requiring different masking for different user groups

**Generic Requirements:**
- DDM SHALL be enforced at the database or application layer
- DDM rules SHALL be based on documented user roles and privileges
- DDM SHALL NOT be bypassable by users lacking appropriate authorization
- DDM implementation SHALL log all access to sensitive fields
- DDM performance impact SHALL be assessed and acceptable

**Example Use Cases** (generic):
- Customer service reps see "****1234" for card numbers
- Managers see full unmasked data
- External auditors see partially masked data
- Reports show masked data for unauthorized users

**Audit Evidence Requirements:**
- DDM rule configuration documentation
- User role mapping to masking rules
- Access logs showing masking enforcement
- Bypass attempt logs (if applicable)

---

### 2.3 Redaction / Nullification

**Definition:** Complete removal or replacement of sensitive data with 
placeholder characters.

**Characteristics:**
- Data is **completely obscured**
- No realistic substitute data
- Minimal processing overhead
- Irreversible

**When to use:**
- Data export for external parties
- Reports and screenshots
- Scenarios where data utility is not required
- High-sensitivity data with no legitimate non-production use

**Generic Requirements:**
- Redaction SHALL completely obscure original data
- Placeholder characters SHALL be consistent (e.g., "*", "XXXX", "[REDACTED]")
- Redaction SHALL be applied consistently across all output formats
- Redacted data SHALL maintain field presence (not deleted, just masked)

**Redaction Methods:**
- **Full Redaction:** Entire field replaced → "John Smith" → "**********"
- **Partial Redaction:** Partial data shown → "+41791234567" → "+4179*******"
- **Nullification:** Field set to null/empty → "Confidential Memo" → NULL

**Example Use Cases** (generic):
- PII in publicly shared reports
- Sensitive comments in screenshots
- Legal documents with confidential sections
- Compliance reports for external auditors

**Audit Evidence Requirements:**
- Redaction policy documentation
- Sample redacted outputs
- Validation that redaction cannot be reversed

---

### 2.4 Data Tokenization

**Definition:** Replacement of sensitive data with non-sensitive tokens 
(surrogate values) with a secure mapping table.

**Characteristics:**
- Original data stored in **secure token vault**
- Token has no mathematical relationship to original
- Reversible (if authorized and vault accessible)
- Format-preserving or format-independent

**When to use:**
- Payment processing systems (credit cards)
- Scenarios requiring potential de-tokenization
- High-security environments with centralized token management
- Cross-system data references without exposing sensitive data

**Generic Requirements:**
- Token vault SHALL be cryptographically secured
- Token generation SHALL be unpredictable and non-reversible without vault
- Access to token vault SHALL be strictly controlled and logged
- Tokenization system SHALL support token lifecycle management (expiry, revocation)
- Token format MAY be preserved (e.g., 16-digit token for 16-digit card number)

**Tokenization Types:**
- **Format-Preserving Tokenization:** Token matches original format
- **Non-Format-Preserving Tokenization:** Token is arbitrary (e.g., UUID)

**Example Use Cases** (generic):
- Credit card tokenization for recurring payments
- PII tokenization for data analytics
- Cross-border data transfer compliance
- Third-party integrations requiring data references

**Audit Evidence Requirements:**
- Token vault architecture documentation
- Access control policies for vault
- Token generation algorithm documentation (if applicable)
- Token lifecycle management procedures

---

### 2.5 Data Substitution (Synthetic Data Generation)

**Definition:** Replacement of sensitive data with **realistic but entirely 
fictional data** generated algorithmically.

**Characteristics:**
- Maintains statistical properties of original dataset
- No relationship to real individuals
- Format and data type preserved
- Referential integrity maintained

**When to use:**
- AI/ML training datasets
- Performance testing with realistic data volumes
- Third-party analytics sharing
- Public data releases for research

**Generic Requirements:**
- Substitution algorithm SHALL produce statistically similar data
- Substituted data SHALL NOT be traceable to original individuals
- Substitution SHALL maintain referential integrity across tables
- Substitution SHALL preserve data format and validation rules
- Re-identification risk SHALL be assessed and minimized

**Substitution Methods:**
- **Deterministic Substitution:** Same input always produces same output (repeatable)
- **Random Substitution:** Different output each time (non-repeatable)
- **Algorithmic Substitution:** Uses statistical models to generate realistic data

**Example Use Cases** (generic):
- Customer demographics for ML model training
- Transaction data for performance benchmarking
- Medical records for research (anonymized)
- Employee data for HR analytics

**Audit Evidence Requirements:**
- Substitution algorithm documentation
- Re-identification risk assessment results
- Sample substituted datasets
- Validation that substituted data maintains utility

---

### 2.6 Data Encryption (for Masking Purposes)

**Definition:** Cryptographic transformation of sensitive data rendering it 
unreadable without decryption key.

**Characteristics:**
- **Reversible** (if key is available)
- Requires key management
- Strong cryptographic protection
- Format typically NOT preserved

**When to use:**
- Data at rest requiring protection but potential authorized access
- Data in transit requiring confidentiality
- Long-term data archival
- Scenarios where de-masking may be legitimately required

**Generic Requirements:**
- Encryption algorithm SHALL be industry-standard (AES-256, RSA, etc.)
- Encryption keys SHALL be managed per ISMS-POL-A.8.24 (Cryptography Control)
- Encrypted data SHALL be protected from unauthorized decryption attempts
- Key access SHALL be strictly controlled and logged
- Encryption SHALL be applied at appropriate layer (field, record, file, database)

**Encryption vs. Masking:**
- Encryption is **reversible** → Use when authorized users may need original data
- Masking is **irreversible** → Use when original data should never be recovered

**Example Use Cases** (generic):
- Sensitive fields in production databases (field-level encryption)
- Backup media containing PII
- Data exports to secure third parties
- Audit logs containing sensitive data

**Audit Evidence Requirements:**
- Encryption algorithm and key strength documentation
- Key management procedures (reference ISMS-POL-A.8.24)
- Encryption implementation configuration
- Access logs for decryption operations

---

### 2.7 Data Shuffling / Permutation

**Definition:** Rearrangement of data values within a column or dataset such 
that values are redistributed among records.

**Characteristics:**
- Individual values remain **real** but are **disassociated** from original records
- Statistical distribution preserved
- Irreversible (without original mapping)
- Referential integrity broken by design

**When to use:**
- Analytics requiring realistic value distribution
- Scenarios where individual record accuracy is not required
- Breaking linkability between data fields
- Scenarios where aggregate statistics must be preserved

**Generic Requirements:**
- Shuffling SHALL randomly redistribute values within the dataset
- Shuffling SHALL NOT create unrealistic data combinations
- Shuffling SHALL be applied consistently across related fields (if required)
- Shuffling process SHALL be documented and repeatable

**Example Use Cases** (generic):
- Salaries shuffled among employees (preserves salary distribution, breaks individual linkage)
- Diagnoses shuffled among patients (preserves disease prevalence, breaks patient linkage)
- IP addresses shuffled among log entries (preserves traffic patterns, breaks source identification)

**Audit Evidence Requirements:**
- Shuffling algorithm documentation
- Validation that shuffled data maintains statistical properties
- Assessment that shuffled data does not create inappropriate associations

---

### 2.8 Hashing (One-Way Cryptographic Hash)

**Definition:** Transformation of data into fixed-length hash values using 
cryptographic hash functions.

**Characteristics:**
- **Irreversible** (one-way function)
- Deterministic (same input → same hash)
- Collision-resistant
- Format NOT preserved

**When to use:**
- Data matching/deduplication without exposing original data
- Verification scenarios (e.g., password verification)
- Data anonymization where matching is required
- Scenarios where data utility is comparison, not retrieval

**Generic Requirements:**
- Hashing algorithm SHALL be cryptographically secure (SHA-256, SHA-3, etc.)
- Hashing SHALL use salt values to prevent rainbow table attacks (if applicable)
- Hashing SHALL NOT use weak algorithms (MD5, SHA-1)
- Hash outputs SHALL be protected from brute-force attacks

**Hashing Methods:**
- **Salted Hashing:** Hash(data + random salt) → Prevents rainbow tables
- **Keyed Hashing (HMAC):** Hash(data + secret key) → Adds authentication

**Example Use Cases** (generic):
- Password storage (salted hashes)
- Email address matching without exposing emails
- Record deduplication without exposing PII
- Data integrity verification

**Audit Evidence Requirements:**
- Hashing algorithm selection justification
- Salt generation and management procedures (if applicable)
- Validation that hashing is irreversible
- Assessment of brute-force attack resistance

---

## 3. Technique Selection Criteria

The organization SHALL select masking techniques based on the following criteria:

| Criterion | Consideration |
|-----------|---------------|
| **Data Sensitivity** | Higher sensitivity → Stronger masking (redaction, encryption) |
| **Use Case Requirements** | Need for data utility → Format-preserving techniques (substitution, tokenization) |
| **Reversibility Needs** | Need for de-masking → Encryption, tokenization<br>No de-masking → Redaction, hashing, substitution |
| **Performance Impact** | Real-time masking → Dynamic masking, encryption<br>Batch processing → Static masking, substitution |
| **Regulatory Requirements** | GDPR, HIPAA, PCI-DSS → May mandate specific techniques |
| **Referential Integrity** | Cross-table relationships → Deterministic techniques (tokenization, deterministic substitution) |
| **Re-identification Risk** | High risk → Redaction, hashing, strong substitution |
| **Data Format Preservation** | Must preserve format → Tokenization, format-preserving encryption, substitution |

---

## 4. Irreversibility Requirements

For masking techniques intended to be **irreversible**, the organization SHALL:

1. **Verify Irreversibility:**
   - Conduct re-identification risk assessments
   - Test that original data cannot be recovered from masked data
   - Document irreversibility validation results

2. **Prevent Reverse Engineering:**
   - Use cryptographically secure algorithms (where applicable)
   - Avoid predictable patterns in masked data
   - Do not store original data alongside masked data

3. **Audit Irreversible Masking:**
   - Require evidence that masking cannot be reversed
   - Validate that no "unmasking" function exists in production
   - Verify that masked data cannot be correlated back to original

---

## 5. Format Preservation Considerations

When **data format must be preserved** (e.g., for application compatibility):

1. **Use Format-Preserving Techniques:**
   - Tokenization (format-preserving mode)
   - Format-preserving encryption (FPE)
   - Substitution with format validation

2. **Validate Format Compliance:**
   - Masked data SHALL pass same validation rules as original
   - Masked data SHALL maintain data type compatibility
   - Masked data SHALL not break application functionality

3. **Document Format Requirements:**
   - Specify required format constraints
   - Validate masked data against format requirements
   - Test application compatibility with masked data

---

## 6. Technique-Specific Implementation Requirements

### 6.1 Static Data Masking (SDM)

- **Automation:** SDM SHALL be automated (scripted, tool-based)
- **Repeatability:** SDM SHALL produce consistent results on repeated execution
- **Validation:** SDM SHALL include post-masking validation checks
- **Backup:** Original production data SHALL be backed up before masking

### 6.2 Dynamic Data Masking (DDM)

- **Performance:** DDM SHALL NOT degrade application performance beyond acceptable limits
- **Logging:** DDM SHALL log all masking decisions and access attempts
- **Bypass Prevention:** DDM SHALL prevent SQL injection or direct database access bypasses
- **Testing:** DDM rules SHALL be tested against all user roles

### 6.3 Tokenization

- **Vault Security:** Token vault SHALL be cryptographically secured
- **Key Management:** Token vault encryption keys SHALL follow ISMS-POL-A.8.24
- **Availability:** Token vault SHALL have appropriate availability/redundancy
- **Lifecycle:** Tokens SHALL have defined lifecycle (creation, expiry, revocation)

### 6.4 Encryption

- **Algorithm Selection:** SHALL use approved algorithms (ISMS-POL-A.8.24-S2.1)
- **Key Management:** SHALL follow key lifecycle procedures (ISMS-POL-A.8.24-S2.2)
- **Access Control:** Decryption keys SHALL be strictly access-controlled
- **Logging:** Decryption operations SHALL be logged

### 6.5 Hashing

- **Salt Generation:** SHALL use cryptographically random salts (if applicable)
- **Salt Storage:** Salts SHALL be stored securely
- **Algorithm Selection:** SHALL use SHA-256 or stronger
- **Brute-Force Protection:** SHALL implement rate limiting (if applicable)

---

## 7. Combining Techniques

The organization MAY combine multiple masking techniques for defense-in-depth:

**Example Combinations:**
- **Encryption + Tokenization:** Encrypt sensitive data, then tokenize encrypted values
- **Hashing + Salting:** Hash data with unique salts to prevent rainbow tables
- **Redaction + Shuffling:** Redact high-sensitivity fields, shuffle moderate-sensitivity fields

**Requirements for Combined Techniques:**
- Document the combination and rationale
- Validate that combined techniques do not introduce vulnerabilities
- Test re-identification resistance of combined approach

---

## 8. Prohibited Techniques

The organization SHALL NOT use the following techniques as masking:

| Prohibited Technique | Reason |
|----------------------|--------|
| **Weak Encryption (DES, RC4)** | Cryptographically broken |
| **Weak Hashing (MD5, SHA-1)** | Collision vulnerabilities |
| **Simple Character Replacement** | Easily reversible (e.g., ROT13) |
| **Predictable Substitution** | Re-identification risk (e.g., John → Person1, Jane → Person2) |
| **Truncation Only** | Insufficient protection (e.g., "12345678" → "1234****") |

---

## 9. Technique Documentation Requirements

For each masking technique deployed, the organization SHALL document:

1. **Technique Name and Type** (e.g., "Static Data Masking - Substitution")
2. **Use Case / Data Types** (e.g., "Customer names in test database")
3. **Implementation Method** (e.g., "Automated script using X library")
4. **Irreversibility Confirmation** (Yes/No, with justification)
5. **Format Preservation** (Yes/No, with details)
6. **Re-identification Risk Assessment** (Low/Medium/High, with mitigation)
7. **Validation Results** (e.g., "Passed referential integrity tests")
8. **Responsible Role** (e.g., "Database Administrator")

---

## 10. Compliance and Audit

### 10.1 Audit Evidence

Auditors SHALL be provided with:
- Masking technique selection justifications
- Technique-specific implementation documentation
- Validation and testing results
- Re-identification risk assessments

### 10.2 Regulatory Alignment

Masking techniques SHALL align with:
- **GDPR:** Pseudonymization and anonymization requirements
- **HIPAA:** De-identification standards (Safe Harbor, Expert Determination)
- **PCI-DSS:** Cardholder data protection (masking, tokenization)
- **CCPA/CPRA:** Consumer data protection requirements

---

## 11. Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| **ISO** | Approve masking techniques, maintain this policy |
| **Data Owner** | Select appropriate techniques for their data |
| **System Owner** | Implement and validate masking techniques |
| **Database Administrator** | Configure and operate masking tools |
| **Security Architect** | Design masking architecture |
| **Compliance Officer** | Validate regulatory alignment |

---

## 12. Review and Updates

This section SHALL be reviewed:
- **Annually** as part of policy review cycle
- Upon **regulatory changes** affecting masking requirements
- Upon **technology changes** (new masking tools, deprecated algorithms)
- Upon **audit findings** recommending technique updates

---

## 13. References

- **ISMS-POL-A.8.11-S1:** Purpose, Scope, Definitions
- **ISMS-POL-A.8.11-S2.1:** Data Identification Requirements
- **ISMS-POL-A.8.11-S2.3:** Environment Requirements (WHERE to mask)
- **ISMS-POL-A.8.11-S2.4:** Testing & Validation
- **ISMS-POL-A.8.24:** Use of Cryptography Policy
- **ISO/IEC 27001:2022 Control A.8.11**
- **ISO/IEC 27002:2022 Guidance for A.8.11**

---

**END OF SECTION S2.2**