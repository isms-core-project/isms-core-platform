**ISMS-CTX-A.8.11 — Data Masking Technical Reference**
**Masking Techniques, Discovery Methods, and Implementation Patterns (Non-ISMS Technical Reference)**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Data Masking Technical Reference |
| **Document Type** | Internal - Technical Reference (Not ISMS) |
| **Document ID** | ISMS-CTX-A.8.11 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Living Document |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architecture Team | Initial technical reference for ISO 27001:2022 certification |

**Review Cycle**: As needed (technology and technique evolution)  
**Next Review Date**: [Date + 12 months]  
**Approvers**: Security Architecture / Data Protection SME (technical reference, no ISMS approval chain required)

**Distribution**: Security Engineering, Data Engineering, Development Teams, IT Operations (for awareness and implementation guidance)

---

⚠️ **IMPORTANT – NON-ISMS TECHNICAL SUPPORT DOCUMENT**

This document is provided for informational and awareness purposes only.

- This document is NOT part of the Information Security Management System (ISMS).
- This document does NOT define mandatory data masking controls.
- This document does NOT establish binding requirements, deadlines, KPIs, or SLAs.
- This document does NOT mandate the use, prohibition, or configuration of specific masking tools, vendors, algorithms, or platforms.
- This document does NOT override or extend any ISMS policy.

All binding data masking requirements, obligations, and governance decisions are defined exclusively in **ISMS-POL-A.8.11 (Data Masking Policy)** and other approved ISMS documentation.

This document serves solely as a technical reference to:

- Describe commonly encountered masking techniques and their implementations
- Provide data discovery methodology guidance for practitioners
- Support technical discussions and implementation planning
- Inform tool selection and architecture decisions (vendor-agnostic)
- Offer quick reference guides for operational masking activities
- **This document must not be used as audit evidence of implementation**

Use of this document does not imply implementation, compliance, or operational maturity. Implementation evidence is documented in ISMS-IMP-A.8.11 assessment workbooks.

**Critical Positioning Statement**:
This document intentionally exceeds the level of detail required for ISO/IEC 27001 policy documentation. Its purpose is technical awareness and practitioner guidance only. No auditor conclusions shall be drawn from the presence, absence, or classification of any technique, tool, algorithm, or parameter listed herein.

---

# Document Purpose and Scope

## Purpose

This document provides a technical deep-dive into data masking implementation patterns, techniques, and methodologies commonly encountered in modern information systems. It is intended to support:

- Technical awareness of masking implementation options
- Understanding of technique selection trade-offs
- Practical guidance for data discovery and classification
- Context for technology and tool evaluation (vendor-agnostic)
- Implementation planning for development and operations teams
- Troubleshooting and optimization of existing masking solutions

## What This Document Is NOT

This document does NOT:

- Define [Organization]'s approved or prohibited masking techniques (see ISMS-POL-A.8.11 Section 2.2 and Annex A)
- Establish mandatory implementation requirements (see ISMS-POL-A.8.11)
- Create compliance obligations or audit criteria (see ISMS-POL-A.8.11)
- Replace ISMS-POL-A.8.11 policy requirements
- Mandate specific tool vendors or products (technology selection based on [Organization]'s risk assessment)
- Establish data classification schemes (see [Organization]'s Information Classification Policy per A.5.12)
- Define roles and responsibilities (see ISMS-POL-A.8.11 Section 3.1)

## Relationship to ISMS

This document is a **non-binding technical reference**. All data masking control requirements and governance decisions are defined exclusively in ISMS-POL-A.8.11 (Data Masking Policy).

Implementation decisions are documented through ISMS-IMP-A.8.11 assessment workbooks based on risk assessment, operational context, data classification, and regulatory requirements.

## Content Organization

This reference organizes masking guidance by:

- **Section 2**: Detailed masking technique specifications (algorithms, parameters, configuration)
- **Section 3**: Data discovery methodologies (how to find sensitive data)
- **Section 4**: Masking tool landscape (vendor-agnostic capability comparison)
- **Section 5**: Implementation patterns (architectures and integration approaches)
- **Section 6**: Quick reference guides (decision trees, common scenarios, troubleshooting)

---

# Masking Technique Specifications

## Static Data Masking (SDM) Techniques

**Overview**: Static Data Masking permanently replaces sensitive data in non-production databases with realistic but fictitious data. Original data is irreversibly overwritten during a one-time masking process.

### Substitution (Replacement) Techniques

**Character-Level Substitution**:

```
Original: "John Smith"
Technique: Replace each character with random character of same type
Masked: "Kmpq Tnkui"

Configuration:

- Character class preservation: Letter→Letter, Digit→Digit, Special→Special
- Case preservation: Uppercase→Uppercase, Lowercase→Lowercase
- Length preservation: Same character count

```

**Word-Level Substitution**:

```
Original: "John Smith"
Technique: Replace with random name from name dictionary
Masked: "Michael Johnson"

Configuration:

- Dictionary source: Built-in name lists, external name databases
- Cultural context: Match origin (Western, Asian, Middle Eastern names)
- Gender preservation: Male→Male, Female→Female (if determinable)
- Consistency: Same input always produces same output (deterministic)

```

**Format-Preserving Substitution**:

```
Original Email: "john.smith@example.com"
Technique: Replace parts while preserving format
Masked: "michael.johnson@example.com"

Configuration:

- Preserve domain for deliverability testing
- Replace local part with realistic name
- Maintain "@" and "." positions

```

**Implementation Considerations**:

- **Referential Integrity**: Use deterministic algorithms (hash-based) to ensure same input produces same output across tables
- **Data Distribution**: Maintain statistical distribution for performance testing (e.g., name frequency distribution)
- **Uniqueness**: Ensure masked values remain unique where original data was unique (primary keys)
- **Performance**: Batch processing for large datasets, optimize for database operations

### Shuffling (Permutation) Techniques

**Column Shuffling**:

```
Original Table:
ID | Name          | Email

1  | John Smith    | john@example.com
2  | Alice Johnson | alice@example.com
3  | Bob Williams  | bob@example.com

After Column Shuffle (Email column):
ID | Name          | Email

1  | John Smith    | bob@example.com
2  | Alice Johnson | john@example.com
3  | Bob Williams  | alice@example.com

```

**Configuration**:

- Shuffle scope: Within single table only
- Random seed: Deterministic for repeatability
- Constraint preservation: Ensure no uniqueness constraint violations
- Foreign key handling: Shuffle only non-FK columns or coordinate across tables

**Use Cases**:

- Breaking person-to-attribute linkage while maintaining real data distribution
- Realistic test data with no direct individual identification
- Lower computational cost than substitution

**Limitations**:

- Not suitable for highly unique combinations (still potentially identifiable)
- Referential integrity complex across multiple tables
- May not meet regulatory de-identification standards (GDPR, HIPAA)

### Variance/Noise Addition (Numeric Data)

**Additive Noise**:

```
Original Salary: $75,000
Technique: Add random variance ±10%
Masked: $72,345 or $81,250

Configuration:

- Variance range: ±5% to ±20% typical
- Distribution: Uniform, Gaussian, or other
- Sign preservation: Keep positive/negative
- Bounds checking: Ensure result stays within valid range

```

**Multiplicative Noise**:

```
Original Age: 35
Technique: Multiply by random factor 0.9-1.1
Masked: 33 or 38

Configuration:

- Factor range: 0.8-1.2 typical for moderate masking
- Rounding: Round to integers for age, whole dollars for currency
- Range limits: Ensure age stays between 0-120, etc.

```

**Implementation Considerations**:

- **Statistical Validity**: Preserve mean, median, distribution shape for analytics
- **Outlier Handling**: Special handling for extreme values
- **Precision**: Maintain appropriate decimal places
- **Repeatability**: Use seeded random for consistency

**Use Cases**:

- Financial amounts where exact values not needed
- Age, height, weight for demographics
- Statistical analysis requiring realistic distributions

### Nulling/Deletion Techniques

**Complete Nulling**:

```
Original: "Confidential Internal Memo"
Masked: NULL

Configuration:

- Preserve column existence (NULL vs. drop column)
- Handle NOT NULL constraints (use placeholder)
- Foreign key impact assessment

```

**Partial Nulling with Placeholder**:

```
Original: "john.smith@example.com"
Masked: "masked@masked.com"

Configuration:

- Placeholder value: "MASKED", "REDACTED", empty string, or valid dummy
- Application compatibility: Ensure apps handle placeholder gracefully

```

**Use Cases**:

- Fields with no utility in test environments
- Highly sensitive data with no legitimate non-production use
- Simplest masking approach when data utility not required

### Date and Time Masking

**Date Shifting**:

```
Original Date: 2024-03-15
Technique: Add random offset ±180 days
Masked: 2024-01-22 or 2024-08-10

Configuration:

- Offset range: Days, weeks, or months
- Consistency: Same person gets same offset (deterministic based on ID)
- Sequence preservation: Event order maintained (DOB < enrollment < graduation)
- Weekday preservation: Optional - keep same day of week

```

**Date Generalization**:

```
Original: 2024-03-15 (March 15, 2024)
Masked: 2024-03-01 (March 2024, day removed)
Masked: 2024-Q1 (Q1 2024, month removed)
Masked: 2024 (Year only)

Configuration:

- Granularity: Day, month, quarter, year
- Null value handling: Missing dates remain missing
- Age calculation: Ensure derived age still accurate enough

```

**Implementation Considerations**:

- **Age calculations**: Maintain relative ages between dates
- **Event sequences**: Preserve chronological order (hire date < promotion date)
- **Leap years**: Handle February 29 appropriately
- **Time zones**: Consider if times are stored with timezone info

## Dynamic Data Masking (DDM) Techniques

**Overview**: Dynamic Data Masking applies masking rules in real-time at the point of data access based on user role or context. Original data remains unchanged in storage.

### Role-Based Masking

**Database-Level DDM**:

```sql
-- Example: PostgreSQL Row-Level Security with masking function

CREATE FUNCTION mask_email(email TEXT) RETURNS TEXT AS $$
BEGIN
  IF current_user_role() = 'admin' THEN
    RETURN email;  -- Admin sees full email
  ELSE
    RETURN REGEXP_REPLACE(email, '^(.{2}).*(@.*)$', '\1***\2');
    -- Regular users see: "jo***@example.com"
  END IF;
END;
$$ LANGUAGE plpgsql;

-- Apply to view
CREATE VIEW masked_customers AS
SELECT 
  customer_id,
  customer_name,
  mask_email(email) AS email,
  CASE 
    WHEN current_user_role() = 'admin' THEN phone
    ELSE '***-***-' || RIGHT(phone, 4)  -- Show last 4 digits only
  END AS phone
FROM customers;
```

**Configuration**:

- Role mapping: Define which roles see what level of masking
- Masking functions: Library of reusable masking functions
- Performance: Indexed columns may lose index benefit
- Logging: Log all access attempts and applied masking rules

**Application-Level DDM**:

```python
# Example: Application-layer masking based on user permissions

def get_customer_data(customer_id, user_role):
    customer = db.query(f"SELECT * FROM customers WHERE id={customer_id}")
    
    if user_role == 'admin':
        return customer  # Full unmasked data
    elif user_role == 'support':
        customer.email = mask_email(customer.email)
        customer.phone = mask_phone(customer.phone)
        return customer
    else:
        customer.email = "***@***"
        customer.phone = "***-***-****"
        customer.address = "[REDACTED]"
        return customer

def mask_email(email):
    parts = email.split('@')
    return f"{parts[0][:2]}***@{parts[1]}"

def mask_phone(phone):
    return f"***-***-{phone[-4:]}"
```

**Configuration**:

- Middleware implementation: Intercept data before presentation
- Caching considerations: Cache keyed by role + data
- Consistency: All API endpoints apply same masking rules
- Testing: Validate masking for each role

### Context-Based Masking

**Screen/Report-Based Masking**:

```
Context: Customer detail screen → Show partial credit card
Context: Financial report export → Show full credit card (authorized users)
Context: Email notification → Show masked credit card (all users)

Configuration:

- Context detection: Screen ID, report type, export format
- Rule precedence: Context rules override role-based rules
- Logging: Log context and applied masking rule

```

**Time-Based Masking**:

```
Condition: Current_time within business hours AND user_location = 'office'
Action: Show unmasked data

Condition: After hours OR user_location = 'remote'
Action: Apply additional masking layer

Configuration:

- Time windows: Business hours, maintenance windows
- Location detection: IP geolocation, VPN detection
- Multi-factor: Combine time + location + role

```

### Query-Level Masking

**Partial Result Masking**:

```sql
-- Example: Show only aggregated/summary data to unauthorized users

-- Authorized user query:
SELECT customer_name, salary FROM employees;
-- Returns: Individual salaries

-- Unauthorized user same query:
SELECT 'REDACTED' AS customer_name, 
       CASE 
         WHEN COUNT(*) < 10 THEN 'N/A'  -- Prevent small group identification
         ELSE ROUND(AVG(salary), -3)    -- Rounded average only
       END AS salary
FROM employees
GROUP BY department;
-- Returns: Aggregated data only
```

**Configuration**:

- Aggregation threshold: Minimum group size (k-anonymity)
- Rounding level: Precision reduction for de-identification
- NULL handling: Suppress results for insufficient data

## Tokenization Techniques

**Overview**: Tokenization replaces sensitive data with non-sensitive tokens while storing the original in a secure token vault. Tokens maintain format but have no intrinsic meaning.

### Format-Preserving Tokenization

**Credit Card Tokenization**:

```
Original PAN: 4532-1234-5678-9010
Token: 4532-7821-3456-1098

Configuration:

- BIN preservation: First 6 digits (Bank Identification Number) preserved
- Last 4 preservation: Last 4 digits preserved for customer reference
- Format preservation: Hyphens, length maintained
- Luhn check: Token passes Luhn algorithm validation
- Vault storage: Original PAN stored encrypted in token vault

```

**Implementation Pattern**:

```python
# Simplified tokenization example

class TokenVault:
    def __init__(self):
        self.token_to_value = {}  # Encrypted in real implementation
        self.value_to_token = {}  # For deterministic tokenization
    
    def tokenize(self, pan, preserve_bin=True, preserve_last4=True):
        # Check if already tokenized
        if pan in self.value_to_token:
            return self.value_to_token[pan]
        
        # Generate format-preserving token
        if preserve_bin and preserve_last4:
            bin = pan[:6]
            last4 = pan[-4:]
            middle = generate_random_digits(6)  # Random middle digits
            token = f"{bin}{middle}{last4}"
            token = adjust_for_luhn(token)  # Ensure passes Luhn check
        else:
            token = generate_random_pan()
        
        # Store bidirectional mapping (encrypted)
        self.token_to_value[token] = encrypt(pan)
        self.value_to_token[pan] = token
        
        return token
    
    def detokenize(self, token, requester_authorized=True):
        if not requester_authorized:
            raise PermissionError("Unauthorized detokenization")
        
        if token not in self.token_to_value:
            raise ValueError("Invalid token")
        
        # Log detokenization request
        audit_log(f"Detokenization: token={token}, user={current_user()}")
        
        return decrypt(self.token_to_value[token])
```

**Token Vault Security**:

- Encryption: Vault data encrypted with strong encryption (AES-256)
- Access control: Detokenization requires explicit authorization
- Audit logging: All tokenization and detokenization logged
- Key management: Vault encryption keys managed per A.8.24 Cryptography Policy
- Backup: Vault backed up separately with appropriate security
- High availability: Vault availability critical for operations

### Non-Format-Preserving Tokenization

**Random Token Generation**:

```
Original SSN: 123-45-6789
Token: 8f3d9a21-c8b4-4e7a-9d12-5c6f8a2e4b9d (UUID)

Configuration:

- Token format: UUID, random alphanumeric, or custom format
- Token length: Fixed or variable
- Character set: Alphanumeric, base64, hex
- Uniqueness guarantee: Cryptographic randomness or sequential with large namespace

```

**Use Cases**:

- Internal identifiers where format preservation not required
- API keys, session tokens
- Database foreign keys where format-independence acceptable

## Pseudonymization Techniques (GDPR Compliance)

**Overview**: Pseudonymization replaces direct identifiers with pseudonyms such that data cannot identify individuals without additional information (key or mapping) held separately. Meets GDPR requirements for reduced-risk processing.

### Cryptographic Pseudonymization

**HMAC-Based Pseudonymization**:

```python
import hmac
import hashlib

def pseudonymize(identifier, secret_key):
    """
    Generate pseudonym using HMAC-SHA256
    Deterministic: Same input + key = same pseudonym
    """
    pseudonym = hmac.new(
        key=secret_key.encode(),
        msg=identifier.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()
    
    return pseudonym

# Example
original_id = "john.smith@example.com"
secret_key = "organization-specific-secret-key"  # Stored separately, per A.8.24

pseudonym = pseudonymize(original_id, secret_key)
# Result: "8d3f9c2a1b4e5f6d7c8e9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c"
```

**Characteristics**:

- **Deterministic**: Same person always gets same pseudonym (enables linking across datasets)
- **Non-reversible** (without key): Computationally infeasible to recover original from pseudonym
- **Key management**: Secret key must be protected per cryptography policy
- **Format**: Typically hex string, base64, or truncated hash

**Key-Based Pseudonymization**:

```python
from cryptography.fernet import Fernet

def create_pseudonymization_key():
    """Generate pseudonymization key (store securely)"""
    return Fernet.generate_key()

def pseudonymize_reversible(identifier, key):
    """Pseudonymize with ability to re-identify (requires key)"""
    cipher = Fernet(key)
    pseudonym = cipher.encrypt(identifier.encode())
    return pseudonym.decode()

def de_pseudonymize(pseudonym, key):
    """Re-identify from pseudonym (requires key and authorization)"""
    cipher = Fernet(key)
    original = cipher.decrypt(pseudonym.encode())
    return original.decode()

# Example
key = create_pseudonymization_key()
original_name = "John Smith"

pseudonym = pseudonymize_reversible(original_name, key)
# Result: "gAAAAABh3f2k..." (Fernet token)

# Re-identification (when authorized)
recovered = de_pseudonymize(pseudonym, key)
# Result: "John Smith"
```

**GDPR Compliance Considerations**:

- Pseudonymization key stored separately from pseudonymized data (different system, access control)
- Re-identification requires explicit authorization beyond data access
- Key rotation: Plan for periodic key rotation (requires re-pseudonymization)
- Audit: Log all re-identification attempts

### Pseudonym Mapping Tables

**Separate Mapping Approach**:

```
Pseudonymized Dataset:
PseudonymID | Age | City     | Medical_Condition
PS001       | 45  | Zurich   | Diabetes
PS002       | 32  | Geneva   | Hypertension
PS003       | 58  | Basel    | None

Mapping Table (stored separately, restricted access):
PseudonymID | RealName
PS001       | John Smith
PS002       | Alice Johnson
PS003       | Bob Williams
```

**Configuration**:

- Storage separation: Mapping table in separate database/system
- Access control: Different permissions for pseudonymized data vs. mapping
- Encryption: Mapping table encrypted at rest
- Audit: All mapping table access logged

**Advantages**:

- Simple implementation
- Easy to manage mapping
- Clear separation of identified/de-identified data

**Disadvantages**:

- Mapping table is high-value target
- Backup complexity (must backup mapping separately)
- Scalability concerns for large datasets

### k-Anonymity and l-Diversity

**k-Anonymity**:

Ensure each combination of quasi-identifiers appears at least k times:

```
Original Data:
Age | ZIP   | Condition
25  | 8001  | Flu
26  | 8002  | Diabetes
27  | 8001  | Hypertension

k-Anonymity (k=2) Generalized:
Age Range | ZIP Area | Condition
20-30     | 8000-8099| Flu
20-30     | 8000-8099| Diabetes
20-30     | 8000-8099| Hypertension

Result: Each age range + ZIP area combination appears at least 2 times
```

**Generalization Techniques**:

- Age: Exact age → Age ranges (20-30, 30-40, etc.)
- ZIP: 5-digit ZIP → 3-digit ZIP prefix
- Date: Exact date → Month or Quarter
- Income: Exact amount → Income brackets

**l-Diversity**:

Extend k-anonymity to ensure sensitive attributes are diverse within each equivalence class:

```
k-Anonymity (k=3) but not l-Diverse:
Age Range | ZIP Area | Condition
20-30     | 8000-8099| Diabetes
20-30     | 8000-8099| Diabetes
20-30     | 8000-8099| Diabetes
Problem: All records have same sensitive attribute (Diabetes)

l-Diversity (l=2):
Age Range | ZIP Area | Condition
20-30     | 8000-8099| Diabetes
20-30     | 8000-8099| Flu
20-30     | 8000-8099| Hypertension
Solution: At least 2 different sensitive attributes in group
```

**Implementation Tool Examples** (vendor-agnostic):

- ARX Data Anonymization Tool (open source)
- Amnesia (open source)
- IBM InfoSphere Optim Data Privacy
- Microsoft Azure Data Catalog (data classification features)

## Anonymization Techniques (Irreversible)

**Overview**: Anonymization irreversibly removes identifying information such that re-identification is not possible even with additional data. Anonymized data is no longer personal data under GDPR.

### Aggregation and Statistical Disclosure Control

**Aggregation**:

```
Original Microdata (individual records):
Employee | Age | Salary
John     | 35  | 75000
Alice    | 42  | 82000
Bob      | 38  | 79000

Aggregated Data (anonymous):
Age Range | Employee Count | Average Salary
30-40     | 3              | 78667

Result: Individuals not identifiable, data utility preserved for analysis
```

**Minimum Group Size**:

```
Configuration:

- k-anonymity: Minimum 5-10 individuals per group (regulatory standard)
- Suppression: Groups smaller than k are suppressed or merged

```

**Rounding and Perturbation**:

```
Original Average: 78,666.67
Rounded: 79,000 (nearest 1,000)
Perturbed: 79,000 ± random noise

Configuration:

- Rounding level: 100s, 1,000s, 10,000s
- Noise distribution: Uniform, Gaussian
- Trade-off: More rounding/noise = less utility, higher privacy

```

### Data Suppression

**Cell Suppression**:

```
Original Data with rare combinations:
Age | City      | Condition
25  | Willisau  | Rare Disease X  ← Only 1 person, high re-identification risk

Suppressed:
Age | City      | Condition

*   | Willisau  | *                ← Suppressed to protect identity

```

**Configuration**:

- Suppression threshold: Typically k < 5 triggers suppression
- Primary suppression: Direct suppression of violating cells
- Secondary suppression: Additional cells to prevent inference

---

# Data Discovery Methodologies

## Automated Pattern Recognition

**Regular Expression Scanning**:

```python
# Example patterns for sensitive data detection

PATTERNS = {
    'credit_card': r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13})\b',
    'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'phone': r'\b(?:\+?\d{1,3}[-.]?)?\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b',
    'ip_address': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
    'iban': r'\b[A-Z]{2}\d{2}[A-Z0-9]{1,30}\b',
}

def scan_column_for_patterns(column_data, sample_size=1000):
    """Scan column data for sensitive data patterns"""
    results = {}
    sample = column_data.sample(min(sample_size, len(column_data)))
    
    for pattern_name, pattern in PATTERNS.items():
        matches = sample.str.contains(pattern, regex=True, na=False)
        match_percentage = (matches.sum() / len(sample)) * 100
        
        if match_percentage > 10:  # >10% matches suggests this data type
            results[pattern_name] = match_percentage
    
    return results
```

**Named Entity Recognition (NER)**:

```python
# Example using NLP for PII detection

import spacy

nlp = spacy.load("en_core_web_sm")

def detect_pii_entities(text_data):
    """Use NER to detect person names, organizations, locations"""
    doc = nlp(text_data)
    
    entities = {
        'PERSON': [],
        'ORG': [],
        'GPE': [],  # Geopolitical entities (countries, cities)
        'DATE': [],
    }
    
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)
    
    return entities
```

## Database Metadata Analysis

**Column Name Heuristics**:

```python
# Sensitive data indicators in column names

SENSITIVE_KEYWORDS = {
    'PII': ['name', 'firstname', 'lastname', 'email', 'phone', 'address', 
            'ssn', 'passport', 'license', 'dob', 'birth'],
    'Financial': ['card', 'account', 'iban', 'swift', 'routing', 'balance',
                  'salary', 'income', 'payment', 'credit'],
    'Health': ['medical', 'diagnosis', 'prescription', 'patient', 'health',
               'insurance', 'treatment', 'condition'],
    'Credentials': ['password', 'secret', 'token', 'key', 'credential',
                    'apikey', 'private'],
}

def classify_column_by_name(column_name):
    """Classify column based on name"""
    column_lower = column_name.lower()
    
    for category, keywords in SENSITIVE_KEYWORDS.items():
        if any(keyword in column_lower for keyword in keywords):
            return category
    
    return 'Unknown'
```

## Data Profiling and Statistical Analysis

**Distribution Analysis**:

```python
def profile_column(column_data):
    """Analyze column characteristics"""
    profile = {
        'row_count': len(column_data),
        'null_count': column_data.isnull().sum(),
        'unique_count': column_data.nunique(),
        'data_type': str(column_data.dtype),
        'uniqueness_ratio': column_data.nunique() / len(column_data),
    }
    
    # High uniqueness suggests identifiers or PII
    if profile['uniqueness_ratio'] > 0.95:
        profile['likely_identifier'] = True
    
    # Sample values (for manual review, never log actual values!)
    profile['sample_structure'] = [
        len(str(v)) for v in column_data.dropna().head(10)
    ]
    
    return profile
```

## Data Discovery Tools (Vendor-Agnostic Categories)

**Database Scanning Tools**:

- Cloud-native: Azure Purview, AWS Macie, Google DLP API
- On-premises: IBM InfoSphere, Informatica Data Privacy Management
- Open source: DataHub, Amundsen, Apache Atlas

**Application-Level Scanning**:

- API scanning: Inspect API responses for sensitive data
- Log file scanning: Search logs for inadvertent PII exposure
- Configuration scanning: Detect hardcoded credentials

---

# Masking Tool Landscape (Vendor-Agnostic)

## Tool Capability Matrix

| Capability | Database-Native | Dedicated Masking Tools | ETL Tools | Application-Level |
|-----------|-----------------|-------------------------|-----------|-------------------|
| **Static Data Masking** | Limited | Excellent | Good | Limited |
| **Dynamic Data Masking** | Good | Excellent | No | Excellent |
| **Format Preservation** | Limited | Excellent | Good | Limited |
| **Referential Integrity** | Good | Excellent | Excellent | Manual |
| **Performance** | Excellent | Good | Good | Varies |
| **Learning Curve** | Low | Medium | High | High |
| **Cost** | Low (included) | High | Medium | Low (dev effort) |

## Implementation Architectures

**Database-Native DDM**:

```
Architecture:
User → Application → Database (with DDM) → Masked Data Returned

Advantages:

- Centralized enforcement
- No application changes
- Performance optimized

Disadvantages:

- Database-specific implementation
- May impact query optimization
- Limited masking logic

```

**Proxy-Based Masking**:

```
Architecture:
User → Application → Masking Proxy → Database → Proxy applies masking

Advantages:

- Database-agnostic
- Centralized policy management
- Can mask multiple databases

Disadvantages:

- Additional infrastructure
- Performance overhead
- Single point of failure (if not HA)

```

---

# Quick Reference Guides

## Technique Selection Decision Tree

```
START: Need to mask sensitive data

Q1: Is data utility required in masked environment?
    NO → Use: Redaction/Nulling (simplest)
    YES → Continue

Q2: Must masking be reversible?
    YES → Q2a: Who needs to reverse?

        - Authorized users only → Use: Tokenization or Pseudonymization
        - Application needs referential integrity → Use: Tokenization

    NO → Continue

Q3: Is this for production access control?
    YES → Use: Dynamic Data Masking (DDM)
    NO → Continue (non-production use)

Q4: Must preserve referential integrity across tables?
    YES → Use: Deterministic Static Data Masking (SDM) with consistent algorithm
    NO → Use: Random Static Data Masking (SDM)

Q5: Regulatory requirement (GDPR, PCI DSS, HIPAA)?

    - GDPR pseudonymization → Use: Cryptographic Pseudonymization
    - PCI DSS masking → Use: Tokenization or Format-Preserving SDM
    - HIPAA de-identification → Use: Anonymization (Safe Harbor or Expert Determination)
    - None → Use: SDM with Substitution

```

## Common Masking Scenarios

**Scenario 1: Test Database from Production**

```
Problem: Need realistic test data without exposing PII

Solution:
1. Export production schema and data
2. Apply Static Data Masking (SDM):

   - Names: Substitute with fake names (deterministic for consistency)
   - Emails: Format-preserving substitution
   - Addresses: Replace with fake but valid addresses
   - Phone numbers: Format-preserving random digits
   - Dates: Shift by consistent random offset per person

3. Validate referential integrity
4. Load into test environment
5. Test masking effectiveness

Tools: Database export tools + SDM tool (commercial or custom scripts)
Timeline: 1-2 days for initial setup, automated thereafter
```

**Scenario 2: Analytics with PII Protection**

```
Problem: Business intelligence needs aggregate data without individual identification

Solution:
1. Pseudonymize identifiers (customer_id, email)
2. Generalize quasi-identifiers (age → age_range, ZIP → ZIP_prefix)
3. Aggregate sensitive metrics (individual_revenue → segment_revenue)
4. Implement k-anonymity (k=5 minimum)
5. Remove or suppress rare combinations

Tools: ETL tools with masking capabilities, Python/R scripts
Validation: Re-identification risk assessment
```

**Scenario 3: Production Access for Customer Support**

```
Problem: Support staff need customer data but not full PII

Solution:
1. Implement Dynamic Data Masking (DDM) in production database
2. Configure role-based rules:

   - Support: See partial email (jo***@example.com), last 4 of phone
   - Manager: See full email, full phone
   - Admin: See all unmasked

3. Log all access to sensitive fields
4. Monitor for bypass attempts

Tools: Database-native DDM or masking proxy
Compliance: GDPR access logging requirements
```

## Troubleshooting Guide

**Issue: Masked data breaks application logic**

```
Problem: Application validation fails on masked data
Cause: Masked data doesn't match expected format or constraints

Solutions:

- Use format-preserving masking techniques
- Update validation rules to accept masked formats
- Use realistic substitution data that passes validation
- Test masked data against application before deploying to test

```

**Issue: Referential integrity violations after masking**

```
Problem: Foreign keys point to non-existent records after masking
Cause: Non-deterministic masking or incomplete masking of related tables

Solutions:

- Use deterministic masking (same input → same output)
- Mask all related tables together
- Maintain FK relationship mapping during masking
- Validate referential integrity after masking

```

**Issue: Performance degradation with DDM**

```
Problem: Queries slow down significantly after enabling DDM
Cause: Masking functions prevent index usage, additional processing overhead

Solutions:

- Optimize masking functions (cached, indexed where possible)
- Review query execution plans
- Consider static masking for non-production instead
- Implement caching layer for frequently accessed masked data
- Use materialized views with pre-masked data

```

## Compliance Checklist

**PCI DSS Masking Requirements (Req. 3.4-3.5)**:

- [ ] Primary Account Number (PAN) masked when displayed (max 6 first + 4 last digits)
- [ ] PAN unreadable in non-production environments (masking, truncation, or tokenization)
- [ ] CVV2/CVC2 never stored (masking not applicable - must not store)
- [ ] Masking solution prevents unauthorized access to unmasked PAN
- [ ] Documented masking procedures and standards
- [ ] Annual validation of masking effectiveness

**GDPR Pseudonymization (Art. 32, 89)**:

- [ ] Pseudonymization key stored separately from pseudonymized data
- [ ] Re-identification requires additional information not available to data processor
- [ ] Technical and organizational measures prevent unauthorized re-identification
- [ ] Pseudonymization documented in data protection impact assessment (DPIA)
- [ ] Regular review of pseudonymization effectiveness
- [ ] Data subjects informed about pseudonymization where applicable

**HIPAA De-Identification (§164.514)**:

- [ ] Safe Harbor method: Remove all 18 HIPAA identifiers, OR
- [ ] Expert Determination: Statistical verification by qualified expert
- [ ] No actual knowledge of re-identification possibility
- [ ] Code of record for re-identification (if needed) stored separately
- [ ] Documentation of de-identification method and validation
- [ ] Periodic re-assessment of de-identification effectiveness

---

# Implementation Best Practices

## Masking Process Workflow

```
1. DISCOVER
   ├─ Inventory systems and databases
   ├─ Scan for sensitive data patterns
   ├─ Classify data by sensitivity
   └─ Identify regulatory requirements

2. DESIGN
   ├─ Select appropriate masking techniques
   ├─ Define masking rules per data element
   ├─ Plan referential integrity maintenance
   └─ Document masking specifications

3. DEVELOP/CONFIGURE
   ├─ Configure masking tool or develop scripts
   ├─ Implement masking algorithms
   ├─ Set up token vaults (if using tokenization)
   └─ Create masking execution workflows

4. TEST
   ├─ Validate masking effectiveness (original data not present)
   ├─ Test referential integrity (joins work correctly)
   ├─ Verify application compatibility (apps function with masked data)
   ├─ Performance testing (acceptable overhead)
   └─ Re-identification testing (cannot recover original)

5. DEPLOY
   ├─ Execute initial masking (SDM) or enable rules (DDM)
   ├─ Validate deployment success
   ├─ Monitor for errors and performance
   └─ Document deployment

6. MONITOR & MAINTAIN
   ├─ Periodic effectiveness testing
   ├─ Monitor for unmasked data exposure
   ├─ Update masking rules for new data types
   ├─ Annual compliance validation
   └─ Incident response for masking failures
```

## Common Pitfalls to Avoid

**Pitfall 1: Masking Only "Obvious" PII**

```
Mistake: Mask name, email, phone but ignore...

- Username (often same as email)
- Comments/notes fields (may contain PII in free text)
- Log files (may log sensitive data)
- Backup/archive systems (forgotten environments)

Solution: Comprehensive data discovery across ALL systems and formats
```

**Pitfall 2: Inconsistent Masking Across Environments**

```
Mistake: Dev environment masked, but QA environment has unmasked copy
Result: Sensitive data still exposed, compliance violation

Solution: Automated masking in data provisioning pipeline, no manual exceptions
```

**Pitfall 3: "Mask It Later" Mindset**

```
Mistake: Copy production to non-production, plan to mask "when we have time"
Result: Unmasked sensitive data in non-production for weeks/months

Solution: Masking as part of data copy process, no unmasked data in non-production
```

**Pitfall 4: Client-Side Masking Only**

```
Mistake: JavaScript masks data in UI, but backend returns full unmasked data
Result: Trivial to bypass by viewing network traffic

Solution: Enforce masking server-side (database or application layer)
```

---

# Glossary of Technical Terms

**Format-Preserving Encryption (FPE)**: Encryption that maintains the format of the original data (e.g., encrypted credit card number still looks like a credit card number).

**Luhn Algorithm**: Checksum formula for credit card validation. Format-preserving masking of credit cards should maintain Luhn validity.

**Quasi-Identifier**: Attribute that can identify individuals when combined with other attributes (age + ZIP code + gender).

**Re-identification Attack**: Attempt to recover original identity from masked, pseudonymized, or anonymized data through linking, inference, or statistical analysis.

**Salt (Cryptographic)**: Random data added to input before hashing/encryption to prevent rainbow table attacks and ensure unique outputs even for identical inputs.

**Token Vault**: Secure database storing mapping between tokens and original sensitive values in tokenization systems.

---

**END OF TECHNICAL REFERENCE**

**Document Status**: Living document - updated as masking technologies, techniques, and best practices evolve.

**Feedback**: Technical corrections, additions, or improvements should be submitted to Security Architecture team for review and incorporation.

**Reminder**: This document is NOT ISMS. Binding requirements are in ISMS-POL-A.8.11 (Data Masking Policy).

<!-- QA_VERIFIED: 2026-02-06 -->