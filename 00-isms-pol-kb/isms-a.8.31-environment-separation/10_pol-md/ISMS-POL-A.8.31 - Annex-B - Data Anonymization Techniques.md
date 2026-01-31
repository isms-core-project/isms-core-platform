# ISMS-POL-A.8.31-Annex-B
## Environment Separation - Data Anonymization Techniques

**Document ID**: ISMS-POL-A.8.31-Annex-B  
**Title**: Data Anonymization Techniques  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO) / Data Protection Officer (DPO)  
**Status**: Draft

---

## B.1 Purpose

This annex provides **practical techniques** for anonymizing production data for use in development/testing environments. These techniques support compliance with S2.3 (Data Handling Requirements) and GDPR/FADP data protection regulations.

**Key Principle**: Anonymized data cannot be reversed to identify individuals (irreversible anonymization, not pseudonymization).

---

## B.2 Anonymization vs. Pseudonymization vs. Encryption

### B.2.1 Definitions

**Anonymization** (GDPR Recital 26):
- Irreversible removal or modification of personal data
- Individuals cannot be re-identified (even with additional information)
- **Allowed for dev/test** (no longer personal data under GDPR)
- Example: "John Smith, 42, Sursee" → "Person A, Age 40-49, Central Switzerland"

**Pseudonymization** (GDPR Article 4(5)):
- Reversible replacement of identifiers with pseudonyms
- Can re-identify with additional information (e.g., lookup table)
- **NOT allowed for dev/test** (still personal data under GDPR, requires same protections)
- Example: "John Smith" → "ID-12345" (with lookup table: ID-12345 = John Smith)

**Encryption**:
- Reversible transformation using cryptographic keys
- **NOT anonymization** (can be decrypted)
- **NOT allowed for dev/test** (encrypted data is still personal data)

**For Dev/Test Use**: ONLY anonymization (irreversible) is permitted.

---

## B.3 Data Masking Techniques

### B.3.1 Full Masking (Complete Replacement)

**Technique**: Replace entire sensitive value with placeholder

**Examples**:
- Name: "Alice Anderson" → "XXXXX XXXXXXXX"
- Email: "alice.anderson@example.com" → "XXXXX.XXXXXXXX@example.com"
- Phone: "+41 79 123 4567" → "+41 XX XXX XXXX"
- Credit Card: "1234 5678 9012 3456" → "XXXX XXXX XXXX XXXX"

**Pros**:
- Simple to implement
- Clearly indicates masked data
- Prevents accidental exposure

**Cons**:
- Data not usable for realistic testing (lacks format/patterns)
- May break application logic (validation, parsing)

**Use Cases**:
- Highly sensitive data (SSN, credit cards, medical IDs)
- Data not needed for testing functionality
- Compliance demonstrations (show data is masked)

**Implementation (SQL)**:
```sql
UPDATE customers
SET 
  ssn = 'XXX-XX-XXXX',
  credit_card = 'XXXX-XXXX-XXXX-XXXX'
WHERE environment = 'test';
```

### B.3.2 Partial Masking

**Technique**: Mask part of value, preserve format

**Examples**:
- Email: "alice.anderson@example.com" → "a****@example.com"
- Phone: "+41 79 123 4567" → "+41 79 *** ****"
- Credit Card: "1234 5678 9012 3456" → "1234 **** **** 3456"
- Name: "Alice Anderson" → "A**** A*******"

**Pros**:
- Preserves data format (validation still works)
- Retains some usability
- Visually indicates real vs. masked data

**Cons**:
- May still allow re-identification (especially for unique values)
- DPO review required (ensure sufficient masking)

**Use Cases**:
- Testing validation logic (email format, phone format)
- Displaying partially masked data in UI
- Moderate sensitivity data

**Implementation (Python)**:
```python
def partial_mask_email(email):
    local, domain = email.split('@')
    masked_local = local[0] + '*' * (len(local) - 1)
    return f"{masked_local}@{domain}"

# Result: "alice.anderson@example.com" → "a************@example.com"
```

### B.3.3 Format-Preserving Masking

**Technique**: Replace value but preserve format/type

**Examples**:
- Phone: "+41 79 123 4567" → "+41 79 987 6543" (random but valid format)
- Date: "1985-03-15" → "1987-07-22" (random date, same format)
- Postal Code: "6210" → "8001" (random but valid Swiss postal code)
- Credit Card: "4111 1111 1111 1111" → "4532 8765 4321 9876" (random but valid Luhn)

**Pros**:
- Data remains realistic (testing works normally)
- Format validation works
- Database constraints satisfied (e.g., NOT NULL, format checks)

**Cons**:
- More complex to implement
- May require domain knowledge (valid formats, check digits)

**Use Cases**:
- Integration testing (realistic data needed)
- UI/UX testing (display formatting)
- Performance testing (realistic data volumes and types)

**Implementation (Faker library)**:
```python
from faker import Faker
fake = Faker('de_CH')  # Swiss locale

# Generate realistic but fake data
fake_name = fake.name()              # "Müller Hans"
fake_email = fake.email()            # "hans.mueller@example.com"
fake_phone = fake.phone_number()     # "+41 79 123 45 67"
fake_address = fake.address()        # "Bahnhofstrasse 1, 8001 Zürich"
```

---

## B.4 Tokenization

### B.4.1 One-Way Tokenization

**Technique**: Replace real values with random tokens (irreversible)

**Example**:
- Customer ID: "CUST-12345" → Token: "TKN-A7B9C2"
- Order ID: "ORD-2024-001" → Token: "TKN-X3Y8Z1"
- Invoice Number: "INV-2024-0315-001" → Token: "TKN-M4N2P9"

**Important**: **Consistent tokenization** (same real value always maps to same token)

**Implementation**:
```python
import hashlib

def tokenize(value, salt="random-salt-change-per-environment"):
    hash_obj = hashlib.sha256(f"{value}{salt}".encode())
    token_hash = hash_obj.hexdigest()[:8].upper()
    return f"TKN-{token_hash}"

# "CUST-12345" always → "TKN-A7B9C2" (same salt)
```

**Pros**:
- Referential integrity maintained (same ID across tables → same token)
- Reversibility impossible (one-way hash)
- Simple to implement

**Cons**:
- Tokens not human-readable
- Cannot derive meaning from token

**Use Cases**:
- Customer IDs, Order IDs, Transaction IDs
- Maintaining relationships across tables
- Anonymized analytics (track behavior without identity)

### B.4.2 Differential Privacy Tokens

**Technique**: Add noise to prevent re-identification even with auxiliary data

**Use Cases**:
- Aggregated analytics (counts, averages)
- Research datasets (epidemiological studies)
- High re-identification risk scenarios

**Advanced Technique**: Beyond scope of basic anonymization (consult privacy specialist)

---

## B.5 Generalization and Data Reduction

### B.5.1 Generalization (Reduce Precision)

**Technique**: Replace specific values with ranges or categories

**Examples**:
- Age: "42" → "40-49" (age range)
- Salary: "CHF 95,000" → "CHF 90,000-100,000" (salary band)
- Location: "Sursee, Lucerne" → "Central Switzerland" (region)
- Date: "2024-03-15" → "March 2024" (month/year only)
- Time: "14:37:22" → "14:00-15:00" (hour range)

**Pros**:
- Reduces re-identification risk (less specific)
- Retains statistical properties
- GDPR-compliant (sufficient generalization)

**Cons**:
- Loss of precision (may impact testing scenarios)
- Requires domain knowledge (appropriate ranges)

**Use Cases**:
- Demographic analysis (age groups, income bands)
- Geographic analysis (regions, not specific addresses)
- Temporal analysis (trends, not exact timestamps)

**Implementation**:
```python
def generalize_age(age):
    if age < 18:
        return "Under 18"
    elif age < 30:
        return "18-29"
    elif age < 50:
        return "30-49"
    elif age < 65:
        return "50-64"
    else:
        return "65+"

# age=42 → "30-49"
```

### B.5.2 Data Subsetting (Sampling)

**Technique**: Use small sample of production data (reduces risk through minimization)

**Approach**:
1. Extract 1-5% of production records (random sampling)
2. Anonymize the subset
3. Use subset for testing

**Example**:
- Production: 1,000,000 customer records → Test: 10,000 records (1%)

**Pros**:
- Smaller dataset = lower re-identification risk
- Faster testing (less data to process)
- Data minimization (GDPR principle)

**Cons**:
- May not represent full data diversity
- Performance testing less realistic (smaller volumes)

**Use Cases**:
- Functional testing (full dataset not needed)
- Integration testing
- Developer sandboxes

---

## B.6 Synthetic Data Generation

### B.6.1 Rule-Based Synthetic Data

**Technique**: Generate fake data following business rules

**Example (Customer Records)**:
```python
from faker import Faker
fake = Faker('de_CH')

for i in range(1000):
    customer = {
        'customer_id': f"CUST-{i+1:05d}",
        'name': fake.name(),
        'email': fake.email(),
        'phone': fake.phone_number(),
        'address': fake.address(),
        'registration_date': fake.date_between(start_date='-5y', end_date='today'),
        'loyalty_points': fake.random_int(min=0, max=10000),
        'segment': fake.random_element(['Bronze', 'Silver', 'Gold', 'Platinum'])
    }
    # Insert into test database
```

**Pros**:
- Zero re-identification risk (no real data)
- Unlimited volume (generate as needed)
- Customizable (business rules, edge cases)

**Cons**:
- May not capture real data patterns
- Requires effort to define realistic rules
- May miss rare edge cases from production

**Use Cases**:
- Functional testing
- Load testing (generate large volumes)
- Training environments

### B.6.2 Statistical Synthetic Data

**Technique**: Generate data matching statistical properties of production data

**Approach**:
1. Analyze production data (distributions, correlations, patterns)
2. Build statistical model
3. Generate synthetic data matching model

**Example**:
- Production: Customer ages follow normal distribution (mean=45, std=15)
- Synthetic: Generate ages from same distribution

**Tools**:
- **SDV (Synthetic Data Vault)**: Python library for generating synthetic data
- **Gretel.ai**: Cloud service for synthetic data generation
- **DataSynthesizer**: Research tool from University of Washington

**Pros**:
- Preserves statistical relationships
- Realistic data patterns
- Privacy-preserving (no real records)

**Cons**:
- Complex to implement
- May require ML expertise
- Potential for model memorization (advanced attack)

**Use Cases**:
- ML model training (privacy-preserving)
- Analytics testing (realistic distributions)
- Performance testing (realistic data patterns)

---

## B.7 Anonymization Validation (K-Anonymity, L-Diversity)

### B.7.1 K-Anonymity

**Definition**: Each record is indistinguishable from at least k-1 other records

**Example** (k=3):
Original data:
| Name | Age | Postal Code | Disease |
|------|-----|-------------|---------|
| Alice | 42 | 6210 | Diabetes |
| Bob | 43 | 6210 | Heart Disease |
| Charlie | 44 | 6210 | Diabetes |

Anonymized (k=3 - Age + Postal Code):
| Name | Age | Postal Code | Disease |
|------|-----|-------------|---------|
| * | 40-49 | 6210 | Diabetes |
| * | 40-49 | 6210 | Heart Disease |
| * | 40-49 | 6210 | Diabetes |

**Each person indistinguishable from at least 2 others** (k=3).

**Validation**:
```python
# Check if quasi-identifiers (Age, Postal Code) have at least k occurrences
min_k = 3
grouped = df.groupby(['Age_Range', 'Postal_Code']).size()
violations = grouped[grouped < min_k]
if len(violations) == 0:
    print(f"Dataset satisfies {min_k}-anonymity")
else:
    print(f"Violations: {violations}")
```

### B.7.2 L-Diversity

**Definition**: Each equivalence class (k-anonymity group) contains at least L "well-represented" sensitive values

**Example**:
- k-anonymity but all have same disease → Not l-diverse
- k-anonymity with diverse diseases → L-diverse

**Use Cases**:
- When k-anonymity alone insufficient (homogeneity attack)
- Sensitive attributes need diversity

---

## B.8 Re-Identification Risk Assessment

### B.8.1 Re-Identification Testing

**Process**:
1. Attempt to re-identify individuals from anonymized dataset
2. Use publicly available information (LinkedIn, company website, etc.)
3. Document re-identification attempts and results
4. If re-identification successful → Improve anonymization

**Example Test**:
- Anonymized dataset: "Manager, Age 40-49, Central Switzerland, Joined 2010"
- Public LinkedIn search: Find matching profile
- Result: If unique match found → re-identification possible → need stronger anonymization

### B.8.2 DPO Approval Checklist

Before using production-derived data in dev/test, DPO verifies:

☐ Anonymization technique appropriate for data sensitivity  
☐ Re-identification risk assessed (k-anonymity, manual testing)  
☐ Re-identification attempts failed (cannot link back to individuals)  
☐ Data minimization applied (only necessary data anonymized and used)  
☐ Anonymization irreversible (no reverse lookup possible)  
☐ Retention limited (anonymized data deleted after testing complete)  
☐ Access controls (anonymized data treated as confidential, not public)  
☐ Legal review (if cross-border transfer or contractual implications)

**DPO Signature**: ________________ **Date**: ________

---

## B.9 Tool Recommendations

### B.9.1 Open Source Tools

**Faker** (Synthetic Data Generation):
- Language: Python, JavaScript, Ruby, PHP, etc.
- Use: Generate realistic fake data (names, addresses, emails, etc.)
- URL: https://faker.readthedocs.io/

**ARX Data Anonymization Tool**:
- Language: Java (GUI application)
- Use: k-anonymity, l-diversity, differential privacy
- URL: https://arx.deidentifier.org/

**Gretel.ai Community Edition**:
- Language: Python
- Use: Statistical synthetic data generation
- URL: https://gretel.ai/

**SDV (Synthetic Data Vault)**:
- Language: Python
- Use: Generate synthetic data from real data models
- URL: https://sdv.dev/

### B.9.2 Commercial Tools

**Delphix** (Data Masking and Subsetting):
- Enterprise data masking for databases
- Integrated with CI/CD pipelines

**Informatica Persistent Data Masking**:
- Enterprise-scale data anonymization
- Policy-based masking rules

**IBM InfoSphere Optim Data Privacy**:
- Data masking, subsetting, test data generation
- Compliance reporting (GDPR, CCPA)

---

## B.10 Anonymization Workflow

### B.10.1 End-to-End Process

```
1. REQUEST
   Developer requests production-derived data for testing
   ↓
2. BUSINESS JUSTIFICATION
   Developer documents why production data needed (synthetic insufficient)
   ↓
3. DPO REVIEW
   DPO reviews request and proposes anonymization approach
   ↓
4. EXTRACTION
   Operations team extracts subset of production data (minimize volume)
   ↓
5. ANONYMIZATION
   Automated anonymization pipeline applies approved techniques
   ↓
6. VALIDATION
   DPO validates anonymization (k-anonymity check, re-identification attempts)
   ↓
7. APPROVAL
   DPO approves (signs checklist) + CISO approves
   ↓
8. TRANSFER
   Anonymized data provided to developer (in dev/test environment, not production)
   ↓
9. USAGE
   Developer uses anonymized data for testing (time-limited, purpose-limited)
   ↓
10. DELETION
    Anonymized data deleted after 30 days or project completion (whichever sooner)
```

### B.10.2 Automation Opportunities

**Anonymization Pipeline** (AWS Example):
```
Production RDS
  ↓ (AWS DMS - Database Migration Service)
Temporary anonymization database
  ↓ (AWS Lambda - Anonymization script)
Anonymized snapshot
  ↓ (Copy to Test environment)
Test RDS (anonymized data)
```

**CI/CD Integration**:
- Nightly refresh of test data (anonymization pipeline runs automatically)
- Developer self-service (request anonymized data via portal, automated approval for low-risk data)

---

## B.11 Common Pitfalls and Mistakes

### B.11.1 What NOT to Do

❌ **Pseudonymization instead of Anonymization**:
- "ID-12345" with lookup table → STILL personal data → NOT ALLOWED

❌ **Weak Masking**:
- "alice.anderson@example.com" → "a.a@example.com" → Too short, re-identifiable

❌ **Inconsistent Tokenization**:
- Customer ID "CUST-001" → Different tokens in different tables → Breaks referential integrity

❌ **No Re-Identification Testing**:
- Assume anonymization works → Don't test → Risk re-identification

❌ **Encrypting instead of Anonymizing**:
- Encrypt production data for dev/test → Can be decrypted → NOT anonymization

❌ **Production Data in Logs/Errors**:
- Anonymize database, but application logs contain real names/emails → Data leakage

### B.11.2 Best Practices

✅ Use established libraries (Faker, ARX) - don't reinvent the wheel  
✅ DPO approval BEFORE extraction (not after)  
✅ Minimize data volume (1-5% sample, not full dataset)  
✅ Delete after use (30-day maximum retention)  
✅ Test re-identification (attempt to find real people)  
✅ Document everything (anonymization technique, DPO approval, retention)  
✅ Prefer synthetic over production-derived (whenever possible)

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | [Name] | ________________ | [Date] |
| Data Protection Officer | [Name] | ________________ | [Date] |
| Legal/Compliance Officer | [Name] | ________________ | [Date] |

---

*End of Annex B - Data Anonymization Techniques*
