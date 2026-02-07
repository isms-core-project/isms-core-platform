**ISMS-IMP-A.8.11.2-UG - Masking Technique Selection & Requirements**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.11.2-UG |
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

**Target Audience:** Data Protection Officers, Security Engineers, Database Administrators, Application Developers, Compliance Officers, Data Governance Teams

**Purpose of This Guide:** Enable autonomous selection of appropriate data masking techniques based on data type, use case, regulatory requirements, and technical constraints.

**What This Document Does:**

- Explains masking technique taxonomy (SDM, DDM, tokenization, encryption, etc.)
- Provides decision frameworks for technique selection
- Guides through assessment workbook completion
- Defines validation criteria for technique effectiveness
- Establishes evidence collection requirements

**What This Document Does NOT Do:**

- Recommend specific vendor products or tools (vendor-agnostic approach)
- Provide implementation tutorials for masking tools (see vendor documentation)
- Replace data inventory assessment (prerequisite: complete IMP-A.8.11.1 first)
- Define data classification (prerequisite: complete IMP-A.8.11.1 first)

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organization]'s **masking technique selection and implementation** to ensure:
1. Appropriate techniques are chosen for each data type and use case
2. Techniques are properly configured to achieve masking objectives
3. Irreversibility is validated where required
4. Format preservation maintains application functionality
5. Referential integrity is maintained across related datasets
6. Performance impact is acceptable for production systems

**Assessment Scope:** 8 technique categories + implementation validation:
1. **Static Data Masking (SDM)** - Permanent masking for non-production environments
2. **Dynamic Data Masking (DDM)** - Real-time masking based on user roles
3. **Redaction/Nullification** - Complete data removal or blanking
4. **Tokenization** - Reversible pseudonymization with secure vault
5. **Data Substitution (Synthetic)** - Replacement with realistic fake data
6. **Encryption for Masking** - Reversible cryptographic masking
7. **Data Shuffling** - Randomization within dataset
8. **Hashing (One-way)** - Irreversible cryptographic transformation

**Assessment Output:** Excel workbook documenting technique selection rationale, implementation status, validation results, and compliance evidence.

## Why This Matters

**ISO 27001:2022 Control A.8.11 Requirement:**
> *"Data masking should be used in accordance with the organization's topic-specific policy on access control and other related topic-specific policies, and business requirements, taking applicable legislation into consideration."*

**Key Success Criteria:**

- **Effectiveness:** Masked data cannot be reversed to original values (unless intentionally reversible)
- **Functionality:** Applications work correctly with masked data
- **Performance:** Masking overhead does not degrade system performance unacceptably
- **Compliance:** Technique selection meets regulatory requirements (GDPR, FADP, PCI-DSS, HIPAA)

**Business Impact:**

- **Data Breaches Prevented:** Properly masked non-production environments eliminate 80%+ of preventable data leaks
- **Regulatory Compliance:** GDPR Art.32, FADP Art.8, PCI-DSS Req.3.4 mandate masking
- **Development Velocity:** Realistic test data enables faster development without privacy risk
- **Third-Party Risk Reduction:** Masked data safe to share with vendors, contractors, offshore teams

## Who Should Complete This Assessment

**Primary Responsibility:** Security Engineers, Database Administrators, Application Developers with masking implementation authority

**Required Knowledge:**

- Understanding of [Organization]'s data classification scheme (from IMP-A.8.11.1)
- Familiarity with database structures and data relationships
- Knowledge of application functionality requirements
- Understanding of regulatory requirements (GDPR, FADP, PCI-DSS, HIPAA as applicable)
- Basic cryptography concepts (hashing, encryption, tokenization)

**Required Authority:**

- Ability to approve masking technique selection
- Authority to implement masking solutions
- Access to test/validate masking effectiveness

**Support Roles:**

- **Data Owners:** Approve masking techniques for their data domains
- **Application Teams:** Validate masked data maintains application functionality
- **Compliance Officers:** Verify regulatory compliance
- **Quality Assurance:** Test masking effectiveness and data integrity

## Time Estimate

**Total Assessment Time:** 6-10 hours (depending on data complexity)

**Breakdown:**

- **Technique Familiarization:** 1-2 hours (reading documentation, understanding options)
- **Technique Selection:** 2-3 hours (completing selection matrix)
- **Implementation Documentation:** 2-3 hours (documenting current implementations)
- **Validation Planning:** 1-2 hours (defining test criteria)
- **Evidence Collection:** 1 hour
- **Quality Review:** 30-60 minutes

**Pro Tip:** For organizations with multiple data domains (finance, HR, customer data, etc.), assign different team members to assess their respective domains in parallel, then consolidate results.

## Connection to Policy and Other Assessments

**Policy Hierarchy:**
```
ISMS-POL-A.8.11 (Data Masking Policy)
    │
    ├─► ISMS-POL-A.8.11, Section 2.1 (Data Classification and Identification) (Data Classification) ◄── Prerequisite
    ├─► ISMS-POL-A.8.11, Section 2.2 (Masking Technique Standards) (Masking Techniques) ◄── YOU ARE HERE
    ├─► ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) (Environment Requirements)
    └─► ISMS-POL-A.8.11, Section 2.4 (Testing and Validation) (Testing & Validation)
```

**Assessment Dependencies:**

**Prerequisites (MUST complete first):**

- ✅ **ISMS-IMP-A.8.11.1** (Data Inventory & Classification) - You must know WHAT data exists and its sensitivity level before selecting masking techniques

**Feeds Into (complete next):**

- ➡️ **ISMS-IMP-A.8.11.3** (Environment Coverage Assessment) - Uses technique selections to verify implementation across environments
- ➡️ **ISMS-IMP-A.8.11.4** (Testing & Validation Framework) - Tests effectiveness of selected techniques
- ➡️ **ISMS-IMP-A.8.11.5** (Compliance Dashboard) - Consolidates all assessment results

**Integration Point:** This assessment uses data inventory from IMP-A.8.11.1 to map data elements → masking techniques → implementation status.

## Critical Concept: Technique-Centric, NOT Tool-Centric

**⚠️ IMPORTANT - Vendor-Agnostic Approach:**

This assessment focuses on **WHICH masking techniques** are appropriate for your data and **HOW they should be configured**, NOT which vendor product to use.

**Good Approach (Technique-Centric):**
✅ "We use static data masking for credit card numbers in UAT, configured to preserve format (XXXX-XXXX-XXXX-1234), irreversible transformation, maintaining referential integrity across payment and order tables."

**Bad Approach (Tool-Centric):**
❌ "We use Delphix for masking." (Tells us nothing about technique selection, configuration, or validation)

**Why This Matters:**

- Techniques are transferable across tools (your decisions remain valid even if tools change)
- Audit focus is on technique effectiveness, not product branding
- Multiple tools may implement same technique differently
- Custom scripts can be as effective as commercial products if properly implemented

**Acceptable Tool References:**

- Document tool names in "Masking Tool Inventory" sheet for operational tracking
- Use generic descriptions in technique selection rationale
- Focus evidence on technique configuration, not product screenshots

---

# Prerequisites

## Completed Assessments (MANDATORY)

**Before starting this assessment, you MUST have completed:**

✅ **ISMS-IMP-A.8.11.1 (Data Inventory & Classification)**

- All sensitive data elements inventoried at field level
- Sensitivity classification assigned (Critical/High/Medium/Low)
- Data owners assigned
- Workbook available for reference

**Quality Check:** Open IMP-A.8.11.1 workbook and verify:

- Sensitive_Data_Inventory sheet populated (minimum 10 data elements)
- Classification_Matrix sheet shows approved classifications
- Data_Owner_Assignment sheet shows assigned owners

**If IMP-A.8.11.1 incomplete:** STOP. Complete data inventory first. You cannot select masking techniques without knowing what data exists and its sensitivity level.

## Access Required

**System Access:**

- [ ] Access to databases/systems containing sensitive data (read-only minimum)
- [ ] Access to masking tool configuration (if tools already deployed)
- [ ] Access to non-production environments (dev, test, UAT) for validation
- [ ] Access to data refresh/migration scripts (to understand current processes)

**Documentation Access:**

- [ ] Database schema documentation (ERD diagrams, data dictionaries)
- [ ] Application data flow diagrams
- [ ] Existing masking documentation (if any)
- [ ] Data retention and archival policies
- [ ] Regulatory compliance requirements (GDPR, FADP, PCI-DSS, HIPAA as applicable)

**Stakeholder Access:**

- [ ] Data owners (for technique approval)
- [ ] Application development teams (for functionality validation)
- [ ] Database administrators (for implementation planning)
- [ ] Compliance officers (for regulatory guidance)

## Knowledge Required

**Essential Understanding:**

**Data Masking Fundamentals:**

- Difference between static (SDM) and dynamic (DDM) masking
- Irreversibility vs. reversibility trade-offs
- Format preservation requirements
- Referential integrity concepts

**Data Relationships:**

- Primary keys and foreign keys
- Parent-child table relationships
- Cross-table data dependencies
- Application data validation rules

**Regulatory Context:**

- GDPR Art.32(1)(a) - Pseudonymization requirement
- FADP Art.8(2) - Technical security measures
- PCI-DSS Req.3.4 - Primary Account Number (PAN) masking
- HIPAA 164.514(b) - De-identification methods

**Technical Skills:**

- Ability to read database schemas
- Understanding of SQL joins and relationships
- Basic understanding of encryption vs. hashing vs. tokenization
- Ability to test data transformations

## Tools and Resources

**Decision Support Tools:**

- **Technique Selection Matrix:** Provided in this assessment workbook
- **Use Case Decision Tree:** See Section 4.2 of this guide
- **Regulatory Requirement Mapping:** Reference ISMS-POL-A.8.11, Section 2.2 (Masking Technique Standards)

**Testing Tools:**

- **SQL Query Tools:** For testing masked data, checking for reversibility
- **Data Profiling Tools:** To analyze masked data distribution (optional)
- **Application Test Environment:** To validate functionality with masked data

**Reference Materials:**

- **NIST SP 800-122:** Guide to Protecting the Confidentiality of PII
- **ISO/IEC 20889:2018:** Privacy Enhancing Data De-identification Terminology and Classification
- **ENISA Data Pseudonymisation Guide:** Advanced techniques and use cases

## Common Misconceptions to Avoid

**Misconception #1: "One technique fits all data"**
❌ Reality: Different data types require different techniques. Credit cards need format-preserving masking; passwords need hashing; analytics data needs data shuffling.

**Misconception #2: "Encryption = masking"**
❌ Reality: Encryption is reversible with key (not true masking). Use encryption only when reversibility is required AND key management is robust.

**Misconception #3: "Just randomize everything"**
❌ Reality: Random data breaks referential integrity, fails application validation, destroys analytics value. Technique must match use case.

**Misconception #4: "Production data doesn't need masking"**
❌ Reality: Dynamic Data Masking (DDM) applies to production for role-based access control. Some regulations require production masking too.

**Misconception #5: "Masking is one-time activity"**
❌ Reality: Masking is continuous. New data elements, schema changes, new environments all require technique selection and implementation.

---

# Assessment Workflow

## High-Level Process Flow
```
START
  │
  ├─► Step 1: Review Approved Techniques (30 min)
  │     └─► Understand technique taxonomy and capabilities
  │
  ├─► Step 2: Complete Technique Selection Matrix (2-3 hours)
  │     └─► Map each data element to appropriate technique(s)
  │
  ├─► Step 3: Document Current Implementations (2-3 hours)
  │     ├─► Static Data Masking (SDM) implementations
  │     ├─► Dynamic Data Masking (DDM) implementations
  │     ├─► Tokenization implementations
  │     └─► Other techniques in use
  │
  ├─► Step 4: Define Configuration Standards (1 hour)
  │     └─► Document technique-specific configuration requirements
  │
  ├─► Step 5: Identify Gaps (1 hour)
  │     └─► Compare desired techniques vs. actual implementation
  │
  ├─► Step 6: Collect Evidence (1 hour)
  │     └─► Document technique configurations, test results
  │
  ├─► Step 7: Quality Review (30 min)
  │     └─► Validate completeness, accuracy, approval status
  │
  └─► Step 8: Obtain Approvals
        └─► Data owners approve techniques for their domains
        
END → Feed results into IMP-A.8.11.3 (Environment Coverage)
```

## Detailed Step-by-Step Workflow

### Step 1: Review Approved Techniques (30 minutes)

**Action:** Read the "Approved_Techniques" sheet in the assessment workbook.

**What to Focus On:**

- Technique taxonomy (8 categories)
- Reversibility characteristics (irreversible vs. reversible)
- Format preservation capabilities (maintains original format vs. changes format)
- Typical use cases (when to use each technique)
- Regulatory alignment (which regulations require/prefer which techniques)

**Decision Point:** Familiarize yourself with ALL techniques before selecting. Don't prematurely narrow to one technique.

**Output:** Mental model of technique landscape and capabilities.

---

### Step 2: Complete Technique Selection Matrix (2-3 hours)

**Action:** For each sensitive data element from IMP-A.8.11.1, select appropriate masking technique(s).

**Sub-Steps:**

**2.1 Import Data Elements (15 minutes)**

- Copy data element list from IMP-A.8.11.1 (Sensitive_Data_Inventory sheet)
- OR manually list top 20-30 most critical sensitive data elements
- Include: Data Element ID, Field Name, Data Category, Sensitivity Level

**2.2 Analyze Use Cases (30 minutes)**
For each data element, identify:

- **Primary Use Case:** What is the masked data used for?
  - Non-production testing?
  - Production role-based access control?
  - Analytics/reporting?
  - Third-party data sharing?
  
- **Functionality Requirements:** What must work with masked data?
  - Application validation rules (e.g., Luhn algorithm for credit cards)?
  - Referential integrity (foreign key relationships)?
  - Sorting/searching capabilities?
  - Statistical properties (for analytics)?

- **Reversibility Requirements:** Must data be un-masked?
  - Never (irreversible)?
  - Authorized users only (DDM or tokenization)?
  - Specific scenarios (decryption with key)?

**2.3 Apply Selection Criteria (1-2 hours)**

Use the **Technique Selection Decision Tree** (Section 4.2) to select techniques.

**For each data element, document:**

- **Primary Technique:** The main masking approach (e.g., "Static Data Masking")
- **Specific Method:** Configuration details (e.g., "Format-preserving substitution with Luhn check")
- **Alternative Techniques:** Backup options if primary doesn't meet all requirements
- **Selection Rationale:** WHY this technique was chosen (3-5 sentences)

**Example Entry:**
```
Data Element: credit_card_number (CAT-FIN, Critical)
Primary Technique: Tokenization
Specific Method: Format-preserving tokenization (XXXX-XXXX-XXXX-1234), secure vault with encryption
Alternative Technique: Static Data Masking with format preservation
Selection Rationale: Tokenization chosen because:
  1. PCI-DSS Req.3.4 allows tokenization as masking method
  2. Reversibility required for authorized payment processors (with vault access)
  3. Format preservation required (16 digits, Luhn valid)
  4. Referential integrity maintained (same card → same token)
  5. Lower performance impact than encryption
```

**2.4 Obtain Data Owner Approval (30 minutes)**

- For each data domain (Finance, HR, Customer, etc.), review selections with data owner
- Document approval status in Technique_Selection_Matrix sheet
- Address any concerns or alternative suggestions

**Output:** Completed Technique_Selection_Matrix sheet with approved techniques for all critical data elements.

---

### Step 3: Document Current Implementations (2-3 hours)

**Action:** Document existing masking implementations across different techniques.

**Sub-Steps:**

**3.1 Static Data Masking (SDM) - 1 hour**

- Open "Static_Masking_SDM" sheet
- For each non-production environment (Dev, Test, UAT), document:
  - Which data elements are masked?
  - What technique is used? (substitution, shuffling, redaction, etc.)
  - What tool/script implements masking?
  - When was it last refreshed?
  - Is it working correctly? (validation status)

**3.2 Dynamic Data Masking (DDM) - 30 minutes**

- Open "Dynamic_Masking_DDM" sheet
- For production systems with role-based masking, document:
  - Which data elements have DDM policies?
  - What roles see masked data vs. clear data?
  - What masking method is applied? (partial masking, full masking, etc.)
  - What is the performance impact?

**3.3 Tokenization - 30 minutes** (if applicable)

- Open "Tokenization_Implementation" sheet
- Document:
  - Which data elements are tokenized?
  - Token vault architecture (external service, internal vault, etc.)
  - Token format (format-preserving or random?)
  - De-tokenization process and authorization

**3.4 Other Techniques - 30 minutes**

- Encryption for Masking: Document encrypted fields, key management
- Hashing: Document hashed fields (passwords, etc.), salt usage
- Redaction: Document nullified/blanked fields
- Data Shuffling: Document shuffled datasets (for analytics)

**Output:** Complete implementation documentation across all technique sheets.

---

### Step 4: Define Configuration Standards (1 hour)

**Action:** Open "Configuration_Standards" sheet and define organization-specific configuration rules.

**What to Document:**

**For Static Data Masking:**

- Format preservation requirements (when required vs. acceptable to change format)
- Referential integrity rules (how to maintain cross-table relationships)
- Data substitution sources (where to get realistic synthetic data)
- Irreversibility validation criteria (how to prove data cannot be reversed)

**For Dynamic Data Masking:**

- Role definitions (which roles see masked data)
- Masking policy templates (standard policies for common data types)
- Performance thresholds (maximum acceptable latency)
- Audit logging requirements (log DDM policy evaluations)

**For Tokenization:**

- Token format standards (format-preserving vs. random)
- Vault security requirements (encryption, access control, backup)
- De-tokenization authorization workflow
- Token lifecycle (expiration, rotation policies)

**Example Standard:**
```
Configuration Standard: Credit Card Masking (PCI-DSS)
Technique: Static Data Masking or Tokenization
Format: XXXX-XXXX-XXXX-1234 (first 6 + last 4 visible per PCI-DSS allowance)
Method: 

  - Option 1 (SDM): Replace middle 6 digits with fixed 'X', preserve first 6 (BIN) + last 4
  - Option 2 (Tokenization): Format-preserving token, maintain Luhn validity

Referential Integrity: Same card number → same masked value across all tables
Validation: Masked value must pass Luhn check, application accepts for processing
Irreversibility: Prove middle 6 digits cannot be derived from masked value (if SDM)
```

**Output:** Documented configuration standards for each technique in use.

---

### Step 5: Identify Gaps (1 hour)

**Action:** Open "Gap_Analysis" sheet and compare desired techniques (from Step 2) vs. actual implementations (from Step 3).

**Gap Types:**

**Implementation Gaps:**

- Technique selected but not yet implemented
- Example: "Selected tokenization for SSN, but currently using SDM"

**Coverage Gaps:**

- Technique implemented in some environments but not all
- Example: "Credit cards masked in Dev, but NOT masked in UAT"

**Configuration Gaps:**

- Technique implemented but incorrectly configured
- Example: "Masking breaks referential integrity between orders and payments tables"

**Validation Gaps:**

- Technique implemented but effectiveness not validated
- Example: "No test proving masked data is irreversible"

**For Each Gap, Document:**

- Gap Description
- Risk Level (Critical/High/Medium/Low)
- Remediation Plan
- Target Date
- Owner

**Output:** Complete Gap_Analysis sheet with prioritized remediation roadmap.

---

### Step 6: Collect Evidence (1 hour)

**Action:** Open "Evidence_Register" sheet and document all compliance evidence.

**Evidence to Collect:**

**Technique Selection Evidence:**

- Technique selection decision matrix (from this assessment)
- Data owner approval emails/sign-offs
- Regulatory requirement mapping

**Implementation Evidence:**

- Masking tool configuration exports
- Masking script source code (if custom scripts)
- Before/after masking sample data (sanitized examples only)
- DDM policy exports

**Validation Evidence:**

- Irreversibility test results (proof masked data cannot be reversed)
- Format preservation validation (masked data passes application validation)
- Referential integrity tests (cross-table relationships maintained)
- Performance test results (masking overhead acceptable)

**Approval Evidence:**

- Data owner approval records
- Security team sign-off
- Compliance officer approval

**Storage:** Store evidence files in secure location, document file path in Evidence_Register.

**Output:** Populated Evidence_Register with minimum 15-20 evidence items.

---

### Step 7: Quality Review (30 minutes)

**Action:** Use the Quality Checklist (Section 7) to validate assessment completeness.

**Key Validation Points:**

- All critical data elements have technique selections (no blanks)
- Selection rationale documented for each technique
- Data owner approvals obtained
- Current implementations documented accurately
- Gaps identified with remediation plans
- Evidence collected and registered

**Common Issues to Fix:**

- Missing rationale (WHY was this technique chosen?)
- Incomplete implementation documentation (which environments?)
- Generic gap descriptions (be specific about what's wrong)
- Missing evidence (cannot prove masking works)

**Output:** Quality-validated assessment ready for final approval.

---

### Step 8: Obtain Approvals (30 minutes)

**Action:** Open "Summary_Dashboard" sheet and complete Approval Sign-Off section.

**Required Approvals:**

| Role | Approves | Evidence Required |
|------|----------|------------------|
| **Data Owner(s)** | Technique selections for their data domain | Signed Technique_Selection_Matrix |
| **Security Team Lead** | Overall technique adequacy and security posture | Gap Analysis review |
| **Application Development Manager** | Masked data maintains application functionality | Functionality test results |
| **Compliance Officer** | Regulatory compliance (GDPR, FADP, PCI-DSS, HIPAA) | Regulatory mapping |
| **CISO** | Final approval for deployment | Complete assessment package |

**Approval Process:**
1. Share assessment workbook with approvers
2. Schedule review meeting (30-60 minutes)
3. Address questions/concerns
4. Obtain sign-offs in workbook
5. Archive approved workbook with signatures

**Output:** Approved assessment ready for implementation (IMP-A.8.11.3 Environment Coverage).

---

# Technique Selection Decision Framework

## Masking Technique Taxonomy (8 Categories)

**Quick Reference Table:**

| Technique | Reversible? | Format-Preserving? | Typical Use Case | Regulatory Alignment |
|-----------|-------------|-------------------|------------------|---------------------|
| **Static Data Masking (SDM)** | No | Yes | Non-production environments | GDPR Art.32, FADP Art.8 |
| **Dynamic Data Masking (DDM)** | Runtime only | Yes | Production role-based access | GDPR Art.32, SOC 2 |
| **Redaction/Nullification** | No | No | Complete data removal | GDPR Right to Erasure |
| **Tokenization** | Yes (with vault) | Optional | Payment cards, reversible pseudonymization | PCI-DSS Req.3.4, GDPR |
| **Data Substitution** | No | Yes | Realistic test data | GDPR, FADP |
| **Encryption (for masking)** | Yes (with key) | No | Reversible protection | HIPAA, GDPR Art.32 |
| **Data Shuffling** | No | Yes (values) | Analytics, ML training | GDPR, research exemptions |
| **Hashing (one-way)** | No | No | Passwords, integrity checks | NIST SP 800-63B, GDPR |

## Technique Selection Decision Tree

**START: For each data element from IMP-A.8.11.1, answer these questions:**

---

**Question 1: Must the data be reversible (un-maskable by authorized users)?**

➡️ **YES** → Continue to Question 2 (Reversible Techniques)  
➡️ **NO** → Continue to Question 3 (Irreversible Techniques)

---

**Question 2 (Reversible Path): How should de-masking be controlled?**

**Option A: Real-time, role-based de-masking in production**

- ✅ **Technique:** Dynamic Data Masking (DDM)
- **Use Case:** Customer service reps see masked SSN, supervisors see full SSN
- **Pros:** No data duplication, real-time access control
- **Cons:** Performance overhead, requires DDM-capable infrastructure

**Option B: Secure vault with tokenization**

- ✅ **Technique:** Tokenization
- **Use Case:** Payment cards, reversible for authorized payment processing
- **Pros:** PCI-DSS compliant, format-preserving optional
- **Cons:** Vault infrastructure required, vault is single point of failure

**Option C: Encryption with key management**

- ✅ **Technique:** Encryption for Masking
- **Use Case:** Data at rest protection, regulatory compliance (HIPAA)
- **Pros:** Standard cryptographic controls, mature key management
- **Cons:** Not format-preserving, key management overhead

**Decision Criteria:**

- Choose **DDM** if: Production system, role-based access control required
- Choose **Tokenization** if: Format preservation critical, PCI-DSS scope, limited authorized de-masking
- Choose **Encryption** if: Regulatory requirement (HIPAA), batch de-masking acceptable

➡️ **SELECTED TECHNIQUE** → Document in Technique_Selection_Matrix

---

**Question 3 (Irreversible Path): Must the masked data maintain format/structure?**

➡️ **YES** → Continue to Question 4 (Format-Preserving Irreversible)  
➡️ **NO** → Continue to Question 5 (Non-Format-Preserving Irreversible)

---

**Question 4 (Format-Preserving Irreversible): What is the primary use case?**

**Option A: Non-production testing (dev, test, UAT)**

- ✅ **Technique:** Static Data Masking (SDM)
- **Configuration:** Format-preserving substitution with referential integrity
- **Use Case:** Realistic test data for application testing
- **Validation:** Data passes application validation rules (e.g., Luhn check for credit cards)

**Option B: Analytics/reporting with statistical properties**

- ✅ **Technique:** Data Shuffling
- **Configuration:** Randomize values within dataset, preserve distribution
- **Use Case:** Analytics, machine learning training data
- **Validation:** Statistical properties preserved (mean, variance, distribution)

**Option C: Realistic synthetic data generation**

- ✅ **Technique:** Data Substitution (Synthetic)
- **Configuration:** Replace with fake but realistic data from lookup tables
- **Use Case:** Demo environments, third-party data sharing
- **Validation:** Data looks real but is completely fabricated

**Decision Criteria:**

- Choose **SDM** if: Need referential integrity across tables, application validation required
- Choose **Data Shuffling** if: Analytics/ML use case, statistical properties matter
- Choose **Data Substitution** if: Demo/external sharing, need realistic-looking fake data

➡️ **SELECTED TECHNIQUE** → Document in Technique_Selection_Matrix

---

**Question 5 (Non-Format-Preserving Irreversible): What is the security objective?**

**Option A: Complete data removal**

- ✅ **Technique:** Redaction/Nullification
- **Configuration:** Replace with NULL, blank, or fixed string (e.g., "REDACTED")
- **Use Case:** GDPR Right to Erasure, data minimization
- **Validation:** Original data cannot be recovered

**Option B: One-way transformation for verification**

- ✅ **Technique:** Hashing (one-way)
- **Configuration:** SHA-256 with salt, bcrypt for passwords
- **Use Case:** Password storage, integrity verification
- **Validation:** Cannot reverse hash to original value

**Decision Criteria:**

- Choose **Redaction** if: Data not needed at all, GDPR erasure requirement
- Choose **Hashing** if: Verification/authentication use case, password storage

➡️ **SELECTED TECHNIQUE** → Document in Technique_Selection_Matrix

---

## Use Case-Based Selection Guide

**Use Case 1: Non-Production Environments (Dev/Test/UAT)**

**Requirement:** Realistic test data without exposing sensitive information

**Recommended Techniques:**
1. **Primary:** Static Data Masking (SDM)

   - Format-preserving substitution for structured data (credit cards, SSNs)
   - Data substitution for free-text fields (names, addresses)
   - Referential integrity maintained across tables

2. **Alternative:** Data Shuffling

   - For analytics/reporting environments
   - Preserves statistical properties
   - Destroys individual-level relationships

**Configuration Standards:**

- Irreversible transformation (cannot reverse to production data)
- Format preservation (data passes application validation)
- Referential integrity (same customer ID → same masked name across tables)
- Refresh cycle: Quarterly or on-demand

**Validation Criteria:**

- ✅ Application functionality works with masked data
- ✅ Masked data is irreversible (prove via testing)
- ✅ No production data visible in logs, error messages, debugging output

---

**Use Case 2: Production Role-Based Access Control**

**Requirement:** Different users see different levels of data masking based on their role

**Recommended Technique:**

- **Primary:** Dynamic Data Masking (DDM)

**Configuration Standards:**

- Policy-based masking rules (define per role)
- Performance acceptable (<10ms overhead per query)
- Audit logging enabled (log who accessed what data)
- Fallback to "deny" if DDM service unavailable

**Example DDM Policies:**

| Role | Data Element | Masking Rule | Example |
|------|--------------|--------------|---------|
| Customer Service Agent | SSN | Show last 4 only | XXX-XX-1234 |
| Customer Service Supervisor | SSN | Show full value | 123-45-1234 |
| Financial Analyst | Account Balance | Round to nearest $100 | $12,300 (actual: $12,347.89) |
| Marketing Analyst | Email Address | Hash domain | abc123@xyz.example.com → abc123@[HASH].com |

**Validation Criteria:**

- ✅ Correct role sees correctly masked data
- ✅ Unauthorized role cannot bypass DDM
- ✅ Performance impact measured and acceptable
- ✅ Audit logs capture DDM policy evaluations

---

**Use Case 3: Payment Card Data (PCI-DSS Compliance)**

**Requirement:** PCI-DSS Req.3.4 - Mask Primary Account Number (PAN) in non-production

**Recommended Techniques:**
1. **Primary:** Tokenization (format-preserving)
2. **Alternative:** Static Data Masking with format preservation

**PCI-DSS Allowances:**

- First 6 digits (BIN - Bank Identification Number) + last 4 may be visible
- Example: 4532-XXXX-XXXX-1234

**Configuration Standards (Tokenization):**

- Format-preserving tokens (16 digits, Luhn-valid)
- Secure token vault (PCI-DSS compliant)
- De-tokenization only for authorized payment processing
- Token lifecycle: Expire tokens on card expiration date

**Configuration Standards (SDM Alternative):**

- Preserve first 6 + last 4, mask middle 6 with fixed 'X'
- Maintain Luhn validity (generates valid-looking but fake card)
- Referential integrity: Same card → same masked value
- Irreversible: Prove middle 6 cannot be derived

**Validation Criteria:**

- ✅ Masked PAN passes Luhn check
- ✅ Application accepts masked PAN for non-financial testing
- ✅ Referential integrity maintained across transactions
- ✅ PCI-DSS assessor approves masking method

---

**Use Case 4: Healthcare Data (HIPAA Compliance)**

**Requirement:** HIPAA 164.514(b) - De-identification of Protected Health Information (PHI)

**Recommended Techniques:**
1. **Primary:** Static Data Masking (SDM) for non-production
2. **Alternative:** Encryption for reversible production protection

**HIPAA De-Identification Methods:**

**Safe Harbor Method (18 identifiers must be removed/masked):**

- Names → Data substitution with fake names
- Geographic subdivisions smaller than state → Generalize to state level
- Dates (birth, admission, etc.) → Shift by random offset (±30 days)
- Phone numbers → Replace with fake but valid format
- Email addresses → Replace with fake domain
- SSN → Redact or static mask
- Medical record numbers → Tokenize with format preservation
- Account numbers → Tokenize
- Certificate/license numbers → Redact
- Device identifiers → Hash or tokenize
- URLs → Redact
- IP addresses → Replace with private IP range
- Biometric identifiers → Redact (cannot mask meaningfully)
- Photos → Redact faces or exclude
- Other unique identifiers → Assess case-by-case

**Expert Determination Method:**

- Statistical de-identification by qualified expert
- Risk of re-identification reduced to "very small"
- Document expert methodology and conclusions

**Validation Criteria:**

- ✅ All 18 HIPAA identifiers masked or removed
- ✅ Re-identification risk assessment performed
- ✅ Data utility maintained for research/analytics
- ✅ HIPAA Privacy Officer approves de-identification method

---

**Use Case 5: Analytics & Machine Learning Training Data**

**Requirement:** Realistic data distributions without exposing individual identities

**Recommended Techniques:**
1. **Primary:** Data Shuffling
2. **Alternative:** Synthetic Data Generation

**Configuration Standards (Data Shuffling):**

- Shuffle values within same column (destroys individual relationships)
- Preserve statistical properties (mean, variance, distribution)
- Maintain data type and format
- Document shuffle algorithm and seed (for reproducibility)

**Configuration Standards (Synthetic Data):**

- Generate synthetic data matching production distributions
- Use Generative Adversarial Networks (GANs) or statistical models
- Validate synthetic data resembles production statistically
- Ensure no individual production records can be reverse-engineered

**Validation Criteria:**

- ✅ Statistical properties match production (within 5% variance)
- ✅ ML model performance comparable to production data
- ✅ Individual-level re-identification impossible
- ✅ Data scientists confirm data utility maintained

---

**Use Case 6: Third-Party Data Sharing (Vendors, Partners)**

**Requirement:** Share data externally without exposing sensitive information

**Recommended Techniques:**
1. **Primary:** Redaction + Data Substitution
2. **Alternative:** Tokenization (if reversibility needed with authorized partner)

**Configuration Standards:**

- Data minimization: Share ONLY fields required by partner
- Sensitive fields: Redact (NULL/blank) or substitute with synthetic values
- Identifiers: Replace with pseudonyms (random IDs)
- Audit trail: Log what data was shared, when, with whom

**Example Sharing Scenarios:**

| Scenario | Data Shared | Masking Approach |
|----------|-------------|------------------|
| **Marketing Partner** | Customer preferences, NOT names/emails | Pseudonymize customer ID, redact PII, share preferences |
| **Analytics Vendor** | Behavioral data, NOT identities | Aggregate to anonymized cohorts, no individual records |
| **Cloud Service Provider** | Application data for processing | Tokenize sensitive fields, encrypt data-in-transit |
| **Offshore Development Team** | Test data for development | Static Data Masking with synthetic substitution |

**Validation Criteria:**

- ✅ Data sharing agreement (DPA) signed with partner
- ✅ Only necessary fields shared (data minimization)
- ✅ Sensitive fields masked or removed
- ✅ Legal/Compliance review approved data sharing

---

## Regulatory Requirement Mapping

**Technique Selection Based on Regulatory Requirements:**

| Regulation | Requirement | Recommended Techniques | Validation Evidence |
|------------|-------------|----------------------|---------------------|
| **GDPR Art.32(1)(a)** | Pseudonymization and encryption | SDM, Tokenization, Encryption | Irreversibility test results, technique documentation |
| **FADP Art.8(2)** | Appropriate technical measures | SDM, DDM, Encryption | Risk assessment, technique selection rationale |
| **PCI-DSS Req.3.4** | Mask PAN (display max first 6 + last 4) | Tokenization, SDM (format-preserving) | PCI assessor approval, masking validation tests |
| **HIPAA 164.514(b)** | De-identification (18 identifiers) | SDM, Redaction, Data Substitution | Safe Harbor checklist, expert determination report |
| **CCPA/CPRA** | De-identification for analytics | Data Shuffling, Synthetic Data | Re-identification risk assessment |
| **SOC 2 CC6.1** | Logical access controls | DDM (role-based), Access controls | DDM policy audit logs, access reviews |
| **ISO 27001 A.8.11** | Data masking per policy | All techniques (policy-driven) | Technique selection aligned to ISMS policy |

**Critical Compliance Notes:**

**GDPR Pseudonymization (Art.32):**

- Technique must prevent attribution to data subject without additional information
- Additional information (e.g., tokenization vault key) must be stored separately
- Re-identification must require "disproportionate effort"
- ✅ Compliant: Tokenization with vault, SDM with irreversibility
- ❌ Non-Compliant: Simple obfuscation (e.g., "XXX"), reversible encoding

**PCI-DSS Masking (Req.3.4):**

- Masking required in non-production AND for display purposes
- First 6 + last 4 may be displayed (for BIN identification)
- Truncation alone is NOT masking (must be irreversible or tokenized)
- ✅ Compliant: Format-preserving tokenization, SDM with irreversibility
- ❌ Non-Compliant: Simple truncation without irreversibility proof

**HIPAA De-Identification (164.514):**

- Safe Harbor: Remove all 18 identifiers (exhaustive list)
- Expert Determination: Statistical proof re-identification risk is "very small"
- De-identified data no longer PHI (relaxed controls)
- ✅ Compliant: Documented Safe Harbor compliance, expert determination letter
- ❌ Non-Compliant: Partial masking leaving some identifiers visible

---

# Sheet-by-Sheet Completion Guide

## Sheet: Approved_Techniques (Reference Sheet - Read Only)

**Purpose:** Reference guide for all approved masking techniques

**How to Use:**
1. **Read-only reference** - Do NOT modify this sheet
2. Use as reference when completing Technique_Selection_Matrix
3. Understand capabilities and limitations of each technique

**Key Information:**

- **Technique ID:** Unique identifier (TECH-SDM, TECH-DDM, etc.)
- **Technique Name:** Human-readable name
- **Reversible?:** Can data be un-masked?
- **Format-Preserving?:** Does masked data maintain original format?
- **Typical Use Cases:** When to use this technique
- **Regulatory Alignment:** Which regulations accept/prefer this technique

**Action Required:** None (reference only)

---

## Sheet: Technique_Selection_Matrix

**Purpose:** Map each sensitive data element to appropriate masking technique

**Time to Complete:** 2-3 hours

**Step-by-Step Instructions:**

**Step 1: Import Data Elements (15 minutes)**

**Column A-D (Auto-populated from IMP-A.8.11.1):**

- Data Element ID
- Field Name
- Data Category
- Sensitivity Level

**If NOT auto-populated:**
1. Open IMP-A.8.11.1 workbook
2. Copy from Sensitive_Data_Inventory sheet
3. Paste into rows 8-107 (100 row capacity)

**Quality Check:** Verify sensitivity levels are current (Critical/High/Medium/Low)

---

**Step 2: Identify Primary Use Case (30 minutes)**

**Column E: Primary Use Case**

- **Dropdown Options:**
  - Non-Production Testing
  - Production Role-Based Access
  - Analytics/Reporting
  - Third-Party Data Sharing
  - Regulatory Compliance (GDPR/HIPAA/PCI)
  - Development/Debugging
  - Archival/Long-Term Storage
  - Other (specify in notes)

**How to Select:**

- Ask: "What will the masked data primarily be used for?"
- If multiple use cases, select the most critical/restrictive
- Document secondary use cases in Notes column

**Example:**

- Credit card numbers → "Non-Production Testing" (dev/test/UAT environments)
- Customer SSN → "Production Role-Based Access" (customer service sees masked, supervisors see clear)
- Health records → "Regulatory Compliance (HIPAA)" (de-identification for research)

---

**Step 3: Define Functionality Requirements (30 minutes)**

**Column F: Functionality Requirements**

- **Free Text Field** - Document what must work with masked data

**What to Document:**

- Application validation rules (e.g., "Must pass Luhn check")
- Referential integrity (e.g., "Same customer ID must have same masked name across all tables")
- Sorting/searching requirements (e.g., "Must be sortable by masked value")
- Statistical properties (e.g., "Must preserve mean and variance for analytics")

**Examples:**

| Data Element | Functionality Requirements |
|--------------|---------------------------|
| credit_card_number | Must pass Luhn algorithm validation, maintain 16-digit format, support payment gateway integration (for testing) |
| customer_email | Must be valid email format (user@domain.tld), unique per customer, searchable in CRM system |
| patient_date_of_birth | Must maintain valid date format, age calculations accurate within ±30 days, chronological sorting |
| account_balance | Must maintain numeric precision, aggregate calculations accurate, no negative values |

**Common Mistake to Avoid:** Don't just write "must work" - be specific about WHAT functionality is required.

---

**Step 4: Determine Reversibility Requirements (15 minutes)**

**Column G: Reversible?**

- **Dropdown Options:**
  - Never (Irreversible)
  - Authorized Users Only (DDM)
  - Specific Scenarios (Tokenization/Encryption)
  - Emergency Only (Break-Glass)

**Decision Criteria:**

**Select "Never (Irreversible)" if:**

- Non-production testing (no need to see real data)
- Regulatory requirement (GDPR pseudonymization)
- Data minimization principle

**Select "Authorized Users Only (DDM)" if:**

- Production environment with role-based access
- Customer service needs conditional access
- Real-time business operations require selective unmasking

**Select "Specific Scenarios (Tokenization/Encryption)" if:**

- Payment processing (authorized payment gateway can de-tokenize)
- Compliance requirement (auditor needs access with proper authorization)
- Batch processing (decrypt for processing, re-encrypt after)

**Select "Emergency Only (Break-Glass)" if:**

- Incident response (security team needs access during investigation)
- Regulatory audit (provide access with full audit trail)
- Legal hold (litigation requires access to original data)

---

**Step 5: Select Primary Technique (1 hour)**

**Column H: Primary Technique**

- **Dropdown Options:**
  - Static Data Masking (SDM)
  - Dynamic Data Masking (DDM)
  - Redaction/Nullification
  - Tokenization
  - Data Substitution (Synthetic)
  - Encryption (for masking)
  - Data Shuffling
  - Hashing (one-way)

**Selection Process:**
1. Use Decision Tree (Section 4.2) to guide selection
2. Consider use case, functionality requirements, reversibility needs
3. Verify regulatory alignment (Section 4.4)
4. Select ONE primary technique (use Alternative Technique column for backups)

**Example Selections:**

| Data Type | Use Case | Reversibility | Primary Technique | Why? |
|-----------|----------|--------------|-------------------|------|
| Credit Card PAN | Non-prod testing | Never | Tokenization (format-preserving) | PCI-DSS compliant, maintains format, supports testing |
| Customer SSN | Prod role-based access | Authorized only | Dynamic Data Masking (DDM) | Real-time access control, no data duplication |
| Patient Names | HIPAA research | Never | Data Substitution (Synthetic) | Safe Harbor compliance, realistic for analytics |
| Passwords | Authentication | Never | Hashing (bcrypt) | Industry standard, irreversible, verification-only |
| Account Balances | Analytics | Never | Data Shuffling | Preserves distribution, anonymizes individuals |

---

**Step 6: Document Specific Method (30 minutes)**

**Column I: Specific Method / Configuration**

- **Free Text Field** - Document HOW the technique will be configured

**What to Document:**

- Masking algorithm (e.g., "Replace middle 6 digits with 'X', preserve first 6 + last 4")
- Format specifications (e.g., "Maintain 16-digit format, Luhn-valid")
- Referential integrity rules (e.g., "Same card → same token across all tables")
- Performance considerations (e.g., "Pre-compute tokens for batch load")

**Examples:**

| Primary Technique | Specific Method |
|------------------|-----------------|
| Static Data Masking | Format-preserving substitution: Replace each digit with random digit (0-9), maintain length and hyphens. Preserve Luhn validity for credit cards. Same input → same output (deterministic for referential integrity). |
| Dynamic Data Masking | Policy-based: IF user.role = 'agent' THEN CONCAT(SUBSTRING(ssn,1,3), '-XX-XXXX') ELSE ssn. Cache policy evaluation for 5 minutes to reduce overhead. |
| Tokenization | Format-preserving tokenization using AES-128 in FF3-1 mode. Token vault: PostgreSQL with AES-256 encryption at rest. Token format matches original (16 digits for cards, 11 for SSN). De-tokenization requires 2-factor auth. |
| Data Substitution | Lookup table replacement: names from US Census data, addresses from postal database, emails using [firstname].[lastname]@example-masked.com pattern. Maintain gender consistency (male name → male name). |

**Common Mistake:** Don't just repeat the technique name - provide configuration details.

---

**Step 7: Define Alternative Technique (15 minutes)**

**Column J: Alternative Technique**

- **Optional** - Document backup technique if primary doesn't meet all requirements

**When to Use:**

- Primary technique has performance issues → Document fallback
- Regulatory flexibility → Document acceptable alternatives
- Transitional period → Document current technique until primary implemented

**Example:**
```
Primary: Tokenization (format-preserving)
Alternative: Static Data Masking with format preservation
Rationale: If tokenization vault becomes unavailable or performance overhead too high, 
           fall back to SDM for non-production environments. Production continues with DDM.
```

---

**Step 8: Document Selection Rationale (1 hour)**

**Column K: Selection Rationale**

- **Free Text Field (200-300 words)** - Explain WHY this technique was chosen

**What to Include:**
1. **Regulatory Requirement:** Which regulation requires/prefers this technique?
2. **Functional Justification:** Why does this technique meet functionality requirements?
3. **Security Justification:** How does this technique protect the data?
4. **Alternatives Considered:** What other techniques were evaluated and why rejected?
5. **Trade-offs Accepted:** What limitations/risks are accepted with this choice?

**Example Rationale (Credit Card Tokenization):**
```
Tokenization selected for credit card PAN masking based on following criteria:

REGULATORY: PCI-DSS Req.3.4 explicitly allows tokenization as masking method. 
Tokens are out-of-scope for PCI audit, reducing compliance burden.

FUNCTIONAL: Format-preserving tokens maintain 16-digit format and Luhn validity, 
ensuring application payment processing logic works correctly in test environments. 
Referential integrity maintained (same card → same token across orders/payments/refunds tables).

SECURITY: Token vault provides additional security layer. Even if non-production database 
compromised, attacker only obtains tokens (useless without vault access). Vault segregated 
on separate infrastructure with strict access controls.

ALTERNATIVES CONSIDERED:

- Static Data Masking: Rejected because irreversible (cannot support payment gateway testing 

  requiring real card validation with partner processors)

- Encryption: Rejected because not format-preserving (would require application code changes)
- Dynamic Data Masking: Rejected for non-production (unnecessary overhead for static test data)

TRADE-OFFS ACCEPTED:

- Token vault is single point of failure (mitigated with HA architecture, backup vault)
- De-tokenization process adds latency (acceptable for infrequent authorized access)
- Vault infrastructure cost (justified by PCI scope reduction and security benefits)

APPROVAL: CFO approved as data owner for financial data category (approval email dated 15.01.2026)
```

**Quality Check:** If rationale is <5 sentences, it's too brief. Expand with justification details.

---

**Step 9: Obtain Data Owner Approval (30 minutes)**

**Column L: Data Owner**

- **Text Field** - Name and role of data owner

**Column M: Approval Status**

- **Dropdown:**
  - ✅ Approved
  - ⚠️ Pending
  - ❌ Rejected
  - 📋 Under Review

**Column N: Approval Date**

- **Date Field** - Date of approval

**Approval Process:**
1. For each data category (Finance, HR, Customer, etc.), identify data owner
2. Send technique selection summary to data owner for review
3. Schedule approval meeting (15-30 minutes per domain)
4. Address any concerns or change requests
5. Obtain sign-off (email approval acceptable)
6. Update Approval Status and Approval Date

**If Rejected:**

- Document reason in Notes column
- Re-evaluate technique selection
- Propose alternative technique
- Re-submit for approval

**Evidence:** Save approval emails/sign-offs in Evidence_Register sheet

---

**Step 10: Add Notes/Comments (ongoing)**

**Column O: Notes**

- **Free Text Field** - Any additional context, caveats, implementation notes

**What to Document:**

- Special considerations (e.g., "Performance testing required before production")
- Dependencies (e.g., "Requires token vault upgrade to v2.0")
- Timeline (e.g., "Implement by Q2 2026")
- Open questions (e.g., "Confirm with legal if anonymization level sufficient for GDPR")

---

## Sheet: Static_Masking_SDM

**Purpose:** Document all Static Data Masking implementations across non-production environments

**Time to Complete:** 1 hour

**Step-by-Step Instructions:**

**Column A-E: Environment & Data Element Identification**

**For each non-production environment (Dev, Test, UAT, Training, etc.):**

**Column A: Environment Name**

- **Text Field** - Which environment? (Dev, Test, UAT, Training, Analytics, DR)

**Column B: Data Element ID**

- **Lookup** - Reference from IMP-A.8.11.1 Sensitive_Data_Inventory

**Column C: Field Name**

- **Auto-populate** - From Data Element ID

**Column D: Masking Required?**

- **Dropdown:** Yes, No, Conditional, Under Review

**Column E: Currently Masked?**

- **Dropdown:** Yes, No, Partial

**Completion Guidance:**

- Start with Production-like environments first (UAT, Training)
- Then complete Test, Dev environments
- Document "Partial" if some instances masked but not all (e.g., masked in DB but not in logs)

---

**Column F-J: Masking Implementation Details**

**Column F: Masking Technique Used**

- **Dropdown:**
  - Format-Preserving Substitution
  - Random Substitution
  - Data Substitution (Lookup Table)
  - Data Shuffling
  - Redaction (NULL/Blank)
  - Fixed Value Replacement
  - Hashing
  - Other (specify in notes)

**Column G: Masking Tool/Script**

- **Text Field** - What implements the masking?
  - Tool name: "Delphix", "Informatica", "Oracle Data Masking Pack"
  - Script name: "mask_customer_data.py", "refresh_uat_masked.sql"
  - Manual: "Manual SQL UPDATE statements"

**IMPORTANT:** Document generic process, not product marketing names. Focus on WHAT is done, not which product does it.

**Column H: Masking Configuration**

- **Free Text** - Describe HOW masking is configured

**Example:**
```
Credit card PAN masking:

- Replace digits 7-12 with 'X' (preserve first 6 BIN + last 4)
- Maintain hyphen positions (XXXX-XXXX-XXXX-XXXX format)
- Deterministic: Same source card → same masked value (for referential integrity)
- Validate Luhn check digit maintained

```

**Column I: Referential Integrity Maintained?**

- **Dropdown:** Yes, No, Partial, N/A

**Referential Integrity Examples:**

**YES:**

- Customer ID 12345 has name "John Doe" in customers table
- Customer ID 12345 has name "John Doe" in orders table
- After masking: Both tables show "Jane Smith" (same masked name)

**NO:**

- Customer table masked: "Jane Smith"
- Orders table masked differently: "Bob Jones"
- Problem: Reports showing customer name from orders won't match customer master

**PARTIAL:**

- Referential integrity maintained within database
- BUT not maintained in log files, backup exports, etc.

**Column J: Last Masking Date**

- **Date Field** - When was data last masked/refreshed?

**Guidance:**

- For automated masking: Date of last data refresh
- For one-time masking: Date of initial masking
- If unknown: Document "Unknown - needs investigation"

---

**Column K-M: Validation & Compliance**

**Column K: Masking Validated?**

- **Dropdown:** Yes, No, Partial, Pending

**Validation Types:**

- **Irreversibility:** Confirmed masked data cannot be reversed to original
- **Functionality:** Application works correctly with masked data
- **Format:** Masked data passes validation rules

**Column L: Validation Evidence**

- **Text Field** - Reference to evidence files

**Examples:**

- "Test results in /compliance/sdm-validation-uat-20260115.pdf"
- "Screenshot of irreversibility test in Evidence_Register EV-042"
- "QA sign-off email dated 15.01.2026"

**Column M: Compliance Status**

- **Dropdown:**
  - ✅ Compliant
  - ⚠️ Partial
  - ❌ Non-Compliant
  - 📋 Under Review
  - N/A

**Determination:**

**✅ Compliant IF:**

- Masking technique properly configured
- Irreversibility validated
- Referential integrity maintained
- Functionality validated
- Evidence documented

**⚠️ Partial IF:**

- Masking works but minor issues (e.g., some referential integrity breaks)
- Validation incomplete (need more testing)

**❌ Non-Compliant IF:**

- Masking required but not implemented
- Masking reversible (can derive original data)
- Functionality broken (application errors with masked data)

---

**Column N-O: Notes & Issues**

**Column N: Issues/Gaps**

- **Text Field** - Document any problems

**Examples:**

- "Performance degradation during masking refresh (8 hours instead of expected 4)"
- "Referential integrity broken for customer_id in archived_orders table"
- "Masked data occasionally fails Luhn validation (1% of records)"

**Column O: Notes**

- **Free Text** - Additional context

---

## Sheet: Dynamic_Masking_DDM

**Purpose:** Document Dynamic Data Masking (DDM) implementations in production environments

**Time to Complete:** 30 minutes

**Step-by-Step Instructions:**

**Column A-D: Data Element & System Identification**

**Column A: System Name**

- **Text Field** - Which production system has DDM?

**Column B: Data Element ID**

- **Lookup** - Reference from IMP-A.8.11.1

**Column C: Field Name**

- **Auto-populate**

**Column D: DDM Policy Name**

- **Text Field** - Name of DDM policy/rule

**Example:** "SSN_Masking_Policy_v1", "CreditCard_RoleBasedMasking"

---

**Column E-H: Role-Based Masking Rules**

**Column E: Role/User Group**

- **Text Field** - Which role/group does this rule apply to?

**Examples:**

- "Customer_Service_Agents"
- "Finance_Analysts"
- "Database_Administrators"
- "Executive_Dashboards"

**Column F: Masking Rule**

- **Free Text** - Describe masking transformation for this role

**Examples:**

| Role | Data Element | Masking Rule |
|------|--------------|--------------|
| Customer Service Agent | SSN | Show XXX-XX-[last 4 digits] |
| Customer Service Supervisor | SSN | Show full value (no masking) |
| Financial Analyst | Account Balance | Round to nearest $100, hide cents |
| Marketing Analyst | Email Address | Show [username]@[HASH].com (hash domain) |

**Column G: Masking Applied When?**

- **Dropdown:**
  - SELECT Queries
  - Application UI
  - Reports
  - API Responses
  - All Access
  - Other (specify)

**Column H: Exceptions/Bypass**

- **Text Field** - Are there any bypass conditions?

**Examples:**

- "BREAK-GLASS: Security team can bypass with 2FA + manager approval"
- "AUDIT: Auditors see unmasked during annual audit (logged)"
- "NONE: No bypass allowed"

---

**Column I-L: Performance & Validation**

**Column I: Performance Impact**

- **Dropdown:**
  - Negligible (<5ms)
  - Low (5-10ms)
  - Moderate (10-50ms)
  - High (>50ms)
  - Not Measured

**Column J: Performance Acceptable?**

- **Dropdown:** Yes, No, Needs Optimization

**Column K: DDM Tested?**

- **Dropdown:** Yes, No, Partial, Pending

**Testing Validation:**

- ✅ **YES:** Confirmed each role sees correctly masked data
- ⚠️ **Partial:** Some roles tested, others not yet
- ❌ **NO:** Testing not performed

**Column L: Audit Logging Enabled?**

- **Dropdown:** Yes, No, Partial

**Why This Matters:** DDM policy evaluations should be logged (who accessed what data, when, which policy applied)

---

**Column M-N: Compliance & Notes**

**Column M: Compliance Status**

- **Dropdown:** ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, 📋 Under Review

**Column N: Notes**

- **Free Text**

---

## Sheet: Tokenization_Implementation

**Purpose:** Document tokenization implementations (if applicable to [Organization])

**Time to Complete:** 30 minutes (or skip if tokenization not used)

**⚠️ NOTE:** If [Organization] does NOT use tokenization, mark this sheet as "N/A - Not Applicable" and skip.

**Step-by-Step Instructions:**

**Column A-D: Data Element & Token Vault**

**Column A: Data Element ID**

- **Lookup** - Reference from IMP-A.8.11.1

**Column B: Field Name**

- **Auto-populate**

**Column C: Token Vault System**

- **Text Field** - Name/description of token vault

**Examples:**

- "Internal Token Vault (PostgreSQL + AES-256)"
- "Third-Party Service: [Provider Name]"
- "Hardware Security Module (HSM) - Model XYZ"

**Column D: Token Format**

- **Dropdown:**
  - Format-Preserving (FPE)
  - Random (UUID/GUID)
  - Custom Format
  - Other

**Format-Preserving Examples:**

- Credit card: 16 digits, Luhn-valid → Token: 16 digits, Luhn-valid
- SSN: XXX-XX-XXXX format → Token: XXX-XX-XXXX format

**Random Examples:**

- Token: 8a7f3c2e-9d41-4b1f-a5c3-1e8f6d9c2b4a (UUID)

---

**Column E-H: Tokenization Configuration**

**Column E: Tokenization Algorithm**

- **Text Field** - Which algorithm/method?

**Examples:**

- "FF3-1 (NIST SP 800-38G) with AES-128"
- "Deterministic encryption with key derivation"
- "Vault-based lookup table (random tokens)"

**Column F: Deterministic?**

- **Dropdown:** Yes (same input → same token), No (same input → different tokens)

**Deterministic = YES:**

- Same credit card "1234-5678-9012-3456" always maps to same token "4532-XXXX-XXXX-7890"
- **Benefit:** Referential integrity maintained
- **Risk:** Token collision possible (limited token space)

**Deterministic = NO:**

- Same credit card tokenized multiple times → different tokens each time
- **Benefit:** No token collision risk
- **Risk:** Referential integrity lost (same card → different tokens in different tables)

**Column G: Token Lifecycle**

- **Text Field** - When do tokens expire/rotate?

**Examples:**

- "Tokens expire on card expiration date"
- "Tokens rotated annually"
- "Indefinite (no expiration)"

**Column H: De-tokenization Authorization**

- **Text Field** - Who can de-tokenize and how?

**Examples:**

- "Payment Gateway API with client certificate authentication"
- "Database Administrators with 2FA + manager approval (logged)"
- "Automated payment processing (service account with HSM key)"

---

**Column I-L: Vault Security & Compliance**

**Column I: Vault Encryption**

- **Text Field** - How is vault data encrypted?

**Example:** "AES-256 encryption at rest, TLS 1.3 in transit, HSM-managed keys"

**Column J: Vault Access Controls**

- **Text Field** - Who/what can access vault?

**Example:** "Service accounts only, no human access. MFA required for vault admin console."

**Column K: Vault Backup/DR**

- **Text Field** - Backup strategy?

**Example:** "Daily encrypted backups to offsite storage. DR site with vault replica (async replication)."

**Column L: Compliance Status**

- **Dropdown:** ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant

---

# Common Pitfalls & How to Avoid Them

## Pitfall #1: Choosing Technique Before Understanding Requirements

**The Mistake:**
Jumping to a technique selection ("We'll use tokenization for everything!") before analyzing:

- What data types exist
- What use cases require masking
- What functionality must be preserved
- What regulatory requirements apply

**Why This Fails:**

- Tokenization may be overkill for simple non-production masking
- One technique doesn't fit all data types
- Over-engineering leads to complexity, cost, delays

**How to Avoid:**
✅ **ALWAYS start with requirements:**
1. Complete IMP-A.8.11.1 (know your data) FIRST
2. Identify use cases (non-prod? production DDM? third-party sharing?)
3. Document functionality requirements (format preservation? referential integrity?)
4. Map regulatory requirements (GDPR? PCI-DSS? HIPAA?)
5. THEN select appropriate technique using Decision Tree (Section 4.2)

**Good Example:**
```
Data: Credit card PAN
Use Case: Non-production testing for payment processing
Requirements: 

  - Format-preserving (16 digits, Luhn-valid)
  - Referential integrity (same card → same masked value)
  - Irreversible (never need to see real cards in test)
  - PCI-DSS compliant

Decision: Format-preserving tokenization OR static data masking with Luhn preservation
Rationale: Both meet requirements. Choose tokenization if future reversibility possible; 
          choose SDM if pure test data (no reversibility ever needed).
```

---

## Pitfall #2: Breaking Referential Integrity

**The Mistake:**
Masking tables independently without considering relationships.

**Example of Broken Referential Integrity:**

**BEFORE Masking (Production):**
```
customers table:
customer_id: 12345
name: "John Doe"
email: "john.doe@example.com"

orders table:
order_id: 98765
customer_id: 12345
customer_name: "John Doe"
```

**AFTER Masking (INCORRECT - No Referential Integrity):**
```
customers table:
customer_id: 12345
name: "Jane Smith"        ← Randomized independently
email: "alice.jones@example.com"   ← Randomized independently

orders table:
order_id: 98765
customer_id: 12345
customer_name: "Bob Williams"  ← Randomized independently (DIFFERENT!)
```

**Problem:** Customer name in orders table doesn't match customers table. Reports show wrong customer names.

**How to Avoid:**
✅ **Use deterministic masking:**

- Same input → same output (consistent transformation)
- Document parent-child table relationships
- Test cross-table queries after masking

**CORRECT Approach:**
```
Masking Rule: "John Doe" → "Jane Smith" (deterministic substitution)

customers table:
customer_id: 12345
name: "Jane Smith"        ← Deterministic
email: "masked_12345@example.com"  ← Based on customer_id (deterministic)

orders table:
order_id: 98765
customer_id: 12345
customer_name: "Jane Smith"  ← Same deterministic rule applied
```

**Testing Validation:**
```sql
-- Test referential integrity after masking
SELECT 
  c.customer_id,
  c.name AS customer_table_name,
  o.customer_name AS order_table_name,
  CASE WHEN c.name = o.customer_name THEN 'PASS' ELSE 'FAIL' END AS integrity_check
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE c.name != o.customer_name;

-- Should return 0 rows (all names match)
```

---

## Pitfall #3: Format Preservation Failures

**The Mistake:**
Masked data fails application validation rules, breaking functionality.

**Examples of Format Preservation Failures:**

**Example 1: Credit Cards (Luhn Check Failure)**
```
Original: 4532-1234-5678-9010 (Luhn-valid)
Bad Masking: 1111-1111-1111-1111 (Luhn-INVALID)
Problem: Application rejects card, payment processing fails in test
```

**Example 2: Email Addresses (Invalid Format)**
```
Original: john.doe@example.com
Bad Masking: XXXXXXXX (not a valid email format)
Problem: Application email validation fails, cannot send test emails
```

**Example 3: Phone Numbers (Wrong Length)**
```
Original: +41 79 123 45 67 (Swiss mobile)
Bad Masking: XXX-XXX-XXXX (US format)
Problem: International dialing code lost, SMS functionality breaks
```

**How to Avoid:**
✅ **Understand application validation rules:**

**For Credit Cards:**

- Must pass Luhn algorithm (checksum validation)
- Maintain BIN (first 6 digits) for card type identification
- Preserve IIN range (different for Visa, Mastercard, Amex)

**For Email Addresses:**

- Must match regex: `[username]@[domain].[tld]`
- Use masked domain: `masked_[hash]@example-test.com`
- Maintain uniqueness (same email → same masked email)

**For Phone Numbers:**

- Preserve country code format
- Maintain digit count per region
- Use valid area codes (avoid reserved ranges like 555-0100)

**For Dates:**

- Maintain valid calendar dates (no February 30th)
- Preserve date format (DD.MM.YYYY vs MM/DD/YYYY)
- Age calculations should remain reasonable (no 200-year-old patients)

**Testing Validation:**
```
1. Apply masking to test dataset
2. Run application validation logic against masked data
3. Check application logs for validation errors
4. Fix masking configuration if errors found
5. Re-test until 0 validation errors
```

---

## Pitfall #4: Reversibility When Irreversibility Required

**The Mistake:**
Using reversible techniques (encryption, tokenization) when irreversibility is required by regulation or policy.

**Example Scenario:**

**Requirement:** GDPR Art.32 pseudonymization for analytics (must be irreversible)

**Wrong Approach:**
```
Technique: AES-256 encryption
Configuration: Customer names encrypted with key stored in database
Problem: Encryption is REVERSIBLE (with key). Attacker who compromises database 
        gets both encrypted data AND key → can decrypt → NOT pseudonymized per GDPR
```

**Right Approach:**
```
Technique: Static Data Masking with one-way transformation
Configuration: Customer names replaced via deterministic hash-based lookup
            (hash input name → lookup synthetic name from table)
Validation: Prove original name cannot be derived from masked name
            (no key material, no reverse lookup table stored)
Result: GDPR-compliant pseudonymization (irreversible without "disproportionate effort")
```

**How to Avoid:**
✅ **Check regulatory requirements BEFORE selecting technique:**

| Regulation | Requirement | Reversible OK? | Recommended Technique |
|------------|-------------|----------------|----------------------|
| GDPR Art.32 Pseudonymization | Must prevent attribution without "additional info" | ⚠️ Yes, IF key/vault stored separately | Tokenization (vault segregated) OR SDM (irreversible) |
| PCI-DSS Req.3.4 Masking | Mask PAN in non-production | ✅ Yes (tokenization allowed) | Tokenization OR SDM |
| HIPAA Safe Harbor | Remove 18 identifiers | ❌ No (must be irreversible) | SDM, Redaction, Data Substitution |
| FADP Art.8 Security | Appropriate technical measures | ✅ Yes (context-dependent) | Any technique meeting risk assessment |

**Irreversibility Testing:**
```
Test: Can masked data be reversed to original without access to keys/vaults?

For SDM: 
  ✅ PASS if: No algorithm exists to reverse transformation
  ❌ FAIL if: Simple base64 encoding (easily reversed)

For Tokenization:
  ✅ PASS if: Vault access requires authentication + authorization (logged)
  ❌ FAIL if: Token-to-value mapping stored in same database as tokens

For Encryption:
  ✅ PASS if: Key stored in separate HSM, access logged and restricted
  ❌ FAIL if: Key stored alongside encrypted data
```

---

## Pitfall #5: Performance Impact Not Measured

**The Mistake:**
Implementing masking without testing performance impact, then discovering production degradation.

**Example Scenarios:**

**Scenario 1: Dynamic Data Masking (DDM) Overhead**
```
Implementation: DDM policies on production database
Impact: Every SELECT query evaluates masking policy
Result: Query latency increased from 50ms → 250ms (5x slower)
Problem: Application timeouts, user complaints, SLA breach
```

**Scenario 2: Tokenization Vault Bottleneck**
```
Implementation: Token vault for high-volume payment processing
Impact: 1000 transactions/second × 2 token lookups each = 2000 vault calls/sec
Result: Vault saturated, payment processing delayed
Problem: Revenue loss, customer complaints
```

**Scenario 3: Static Data Masking Refresh Time**
```
Implementation: Mask 500GB database for UAT environment refresh
Impact: Masking takes 12 hours (overnight window is 8 hours)
Result: UAT refresh fails, testing delayed
Problem: Release schedule impacted, business frustrated
```

**How to Avoid:**
✅ **ALWAYS performance test before production deployment:**

**Performance Testing Checklist:**

**For DDM:**

- [ ] Measure query latency before and after DDM policies
- [ ] Test with realistic query patterns (JOIN queries, complex WHERE clauses)
- [ ] Verify caching works correctly (policy evaluation results cached)
- [ ] Load test: Can system handle peak concurrent users with DDM?
- [ ] Set performance threshold: <10ms overhead acceptable, >50ms unacceptable

**For Tokenization:**

- [ ] Measure vault response time (round-trip latency)
- [ ] Load test vault: Concurrent tokenization/de-tokenization requests
- [ ] Test vault failover: Does failover work within SLA?
- [ ] Network latency: Vault in different datacenter/cloud region?
- [ ] Set performance threshold: <20ms per token lookup acceptable

**For SDM (Batch Masking):**

- [ ] Measure masking time for full dataset
- [ ] Test incremental masking (only mask changed records)
- [ ] Verify referential integrity maintained during masking
- [ ] Test parallel masking (can multiple tables be masked concurrently?)
- [ ] Set performance threshold: Masking completes within maintenance window

**Performance Acceptance Criteria:**
```
DDM: Query latency increase <10ms (95th percentile)
Tokenization: Vault response time <20ms (99th percentile)
SDM: Masking completes within 80% of available maintenance window
```

---

## Pitfall #6: No Validation of Masking Effectiveness

**The Mistake:**
Assuming masking works without testing irreversibility, format preservation, or functionality.

**Example:**
```
Implementation: Deployed SDM for credit cards in UAT environment
Assumption: "Masking script ran successfully, must be working"
Reality: 

  - 15% of cards failed Luhn validation (application rejects them)
  - Referential integrity broken (orders table has different masked values than payments)
  - Some cards not masked at all (masking script missed certain table columns)
  - Masked cards are reversible (simple substitution cipher, easily cracked)

Problem: Discovered during audit, resulted in non-compliance finding
```

**How to Avoid:**
✅ **Implement comprehensive validation testing:**

**Validation Test Suite:**

**Test 1: Irreversibility Test**
```
Objective: Prove masked data cannot be reversed to original

Method:
1. Take sample of 1000 masked records
2. Attempt to reverse using common techniques:

   - Dictionary attack (lookup common values)
   - Pattern analysis (identify substitution patterns)
   - Cryptanalysis (if encryption-based, test key recovery)

3. Document results: 0 records reversed = PASS

Evidence: Test report showing 0% reversibility success rate
```

**Test 2: Format Preservation Test**
```
Objective: Verify masked data passes application validation

Method:
1. Extract validation rules from application code
2. Apply validation to masked dataset
3. Calculate validation pass rate

Acceptance Criteria:

- Credit cards: 100% pass Luhn check
- Emails: 100% valid email format
- Phone numbers: 100% valid format per region
- Dates: 100% valid calendar dates

Evidence: Validation test results with 100% pass rate
```

**Test 3: Functionality Test**
```
Objective: Application works correctly with masked data

Method:
1. Deploy masked data to test environment
2. Execute end-to-end business process tests
3. Verify all functions work correctly

Test Cases:

- Create order with masked customer data → SUCCESS
- Process payment with masked card data → SUCCESS
- Generate report with masked data → SUCCESS
- Search for customer by masked name → SUCCESS

Evidence: QA test results with 0 functional defects
```

**Test 4: Referential Integrity Test**
```
Objective: Cross-table relationships maintained

Method:
SELECT 
  'customers-orders' AS relationship,
  COUNT(*) AS mismatches
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE c.customer_name != o.customer_name

UNION ALL

SELECT 
  'orders-payments' AS relationship,
  COUNT(*) AS mismatches
FROM orders o
JOIN payments p ON o.order_id = p.order_id
WHERE o.card_number != p.card_number;

Acceptance Criteria: 0 mismatches

Evidence: SQL query results showing 0 referential integrity violations
```

---

## Pitfall #7: Masking Production Data (When Not Intended)

**The Mistake:**
Accidentally applying masking to production database instead of non-production copy.

**Horror Story Example:**
```
Intended: Mask data in UAT environment (uat-db-server)
Actual: Ran masking script against production (prod-db-server)
Result: 2 million customer records permanently masked in production
Impact: Customer data lost, business disruption, regulatory breach
Root Cause: Connection string pointed to wrong database
```

**How to Avoid:**
✅ **Implement safety controls:**

**Safety Control 1: Database Connection Validation**
```python
# ALWAYS validate target database before masking
def validate_target_database(connection_string):
    if 'prod' in connection_string.lower():
        raise Exception("FATAL: Cannot mask production database!")
    if 'production' in connection_string.lower():
        raise Exception("FATAL: Cannot mask production database!")
    
    # Require explicit confirmation for safety
    db_name = extract_database_name(connection_string)
    print(f"Target database: {db_name}")
    confirmation = input("Type database name to confirm masking: ")
    
    if confirmation != db_name:
        raise Exception("Database name confirmation failed. Aborting.")
    
    return True
```

**Safety Control 2: Backup Before Masking**
```bash
# ALWAYS backup before masking (just in case)
backup_timestamp=$(date +%Y%m%d_%H%M%S)
pg_dump -h uat-db-server -d uat_database > backup_pre_masking_${backup_timestamp}.sql

# Verify backup completed successfully
if [ $? -eq 0 ]; then
    echo "Backup completed successfully"
    # Proceed with masking
else
    echo "Backup failed. ABORT masking."
    exit 1
fi
```

**Safety Control 3: Read-Only Production Credentials**
```
Best Practice: Masking scripts should NEVER have write access to production

Production database credentials:

  - SELECT only (read-only)
  - Used for: Extracting data to mask in non-production
  - Cannot accidentally modify production

Non-production database credentials:

  - Full write access
  - Used for: Applying masking transformations
  - Isolated from production

```

---

# Quality Checklist

## Pre-Submission Quality Check

**Before submitting assessment for approval, verify ALL items:**

### Section A: Technique Selection Matrix

- [ ] **All data elements covered:** Every sensitive data element from IMP-A.8.11.1 has technique selected
- [ ] **No blank rationales:** Every technique selection has 5+ sentence rationale
- [ ] **Use cases documented:** Primary use case identified for each data element
- [ ] **Functionality requirements clear:** Specific requirements documented (not just "must work")
- [ ] **Reversibility justified:** Reversibility choice matches use case and regulations
- [ ] **Data owner approval:** All technique selections approved by respective data owners
- [ ] **Regulatory alignment verified:** Technique selections comply with applicable regulations (GDPR, PCI-DSS, HIPAA, etc.)
- [ ] **Alternative techniques considered:** Documented what alternatives were evaluated and why rejected

**Quality Questions:**

- Can an auditor understand WHY each technique was chosen by reading the rationale?
- Would this technique selection still be valid if [Organization] changed masking tools?
- Are regulatory requirements explicitly referenced (not just "compliance required")?

---

### Section B: Implementation Documentation

**Static Data Masking (SDM):**

- [ ] All non-production environments documented (Dev, Test, UAT, Training, etc.)
- [ ] Masking configuration described in detail (not just "masked")
- [ ] Referential integrity status verified (tested, not assumed)
- [ ] Last masking date documented (<30 days old ideal)
- [ ] Validation status current (tested within last quarter)

**Dynamic Data Masking (DDM):**

- [ ] All DDM policies documented with role-based rules
- [ ] Performance impact measured (not "unknown")
- [ ] Audit logging enabled and verified
- [ ] DDM policies tested for each role

**Tokenization (if applicable):**

- [ ] Token vault architecture documented
- [ ] Token format specified (format-preserving or random)
- [ ] De-tokenization authorization process defined
- [ ] Vault security controls documented (encryption, access control, backup)

**Other Techniques:**

- [ ] Encryption key management documented
- [ ] Hashing algorithms specified (SHA-256, bcrypt, etc.)
- [ ] Redaction/nullification scope documented

**Quality Questions:**

- Can someone unfamiliar with the system understand how masking is implemented?
- Is enough detail provided to replicate the masking configuration?
- Are there any "TBD" or "Unknown" entries? (If yes, investigate before submission)

---

### Section C: Configuration Standards

- [ ] Configuration standards defined for each technique in use
- [ ] Format preservation requirements specified
- [ ] Referential integrity rules documented
- [ ] Irreversibility validation criteria defined
- [ ] Performance thresholds established

**Quality Questions:**

- Are standards specific enough to implement consistently?
- Would different teams implement masking the same way following these standards?

---

### Section D: Gap Analysis

- [ ] All gaps identified with clear descriptions
- [ ] Risk level assigned (Critical/High/Medium/Low)
- [ ] Remediation plan documented (not just "fix it")
- [ ] Target dates realistic and approved
- [ ] Gap ownership assigned to specific individuals

**Quality Questions:**

- Are gaps prioritized correctly (critical gaps have earliest target dates)?
- Are remediation plans actionable (specific steps, not vague intentions)?
- Are target dates achievable given resource constraints?

---

### Section E: Evidence Register

- [ ] Minimum 15-20 evidence items documented
- [ ] Evidence types diverse (not all one type)
- [ ] File locations accessible to auditors
- [ ] Evidence ownership assigned
- [ ] Evidence retention periods appropriate

**Evidence Type Distribution (Ideal):**

- 30% Technique selection evidence (decision matrices, approvals)
- 30% Implementation evidence (configurations, scripts, policies)
- 30% Validation evidence (test results, irreversibility proofs)
- 10% Approval evidence (sign-offs, emails)

**Quality Questions:**

- Can an auditor access each evidence item within 5 minutes?
- Is evidence storage secure and backed up?
- Does evidence actually prove what it claims to prove?

---

### Section F: Summary Dashboard

- [ ] Overall compliance metrics calculated correctly
- [ ] Technique coverage by data category summarized
- [ ] Gaps prioritized and visible
- [ ] Approval sign-off section complete

---

## Common Quality Issues and How to Fix Them

**Issue 1: Vague Technique Rationale**
```
❌ Bad: "We chose tokenization because it's secure and compliant."

✅ Good: "Tokenization selected for credit card PAN based on:
  1. PCI-DSS Req.3.4 explicitly allows tokenization
  2. Format-preserving tokens maintain 16-digit Luhn-valid format for application compatibility
  3. Reversibility required for authorized payment processor integration testing
  4. Token vault architecture segregates sensitive data from application database
  5. CFO approved as data owner for financial data (approval email 15.01.2026)
Alternatives considered: SDM rejected due to irreversibility (need de-tokenization for payment gateway testing)"
```

**How to Fix:** Use the 5-point rationale structure:
1. Regulatory requirement
2. Functional justification
3. Security justification
4. Alternatives considered
5. Approval documented

---

**Issue 2: Missing Implementation Details**
```
❌ Bad: "Credit cards are masked in UAT using our masking tool."

✅ Good: "Credit cards masked in UAT environment using Delphix Dynamic Data Engine v6.0.
Configuration: Format-preserving substitution algorithm, preserves first 6 digits (BIN) + last 4, 
masks middle 6 with random digits maintaining Luhn validity. Deterministic masking ensures 
referential integrity across customers, orders, payments, and refunds tables. Last masked: 15.01.2026 
during quarterly UAT refresh. Validation: 100% of masked cards pass Luhn check (validation report EV-034)."
```

**How to Fix:** Answer these questions in implementation documentation:

- WHAT is being masked? (data element)
- WHERE? (which environment/system)
- HOW? (technique and configuration)
- WHEN? (last masking date)
- VALIDATED? (proof it works)

---

**Issue 3: Unrealistic Gap Remediation Plans**
```
❌ Bad: 
Gap: "SSN not masked in Dev environment"
Remediation: "Implement masking"
Target Date: "Q2 2026"
Owner: "IT Team"

✅ Good:
Gap: "SSN field (employees.social_security_number) not masked in Dev environment (dev-db-01)"
Risk Level: Critical (regulatory breach if dev database compromised)
Remediation Plan:
  1. Update data refresh script (refresh_dev_db.sh) to include SSN masking
  2. Use format-preserving SDM: XXX-XX-[last 4 digits visible]
  3. Test masked data with HR application in dev
  4. Deploy to dev environment during next refresh (scheduled 01.02.2026)
  5. Validate 100% of SSN records masked post-deployment
Target Date: 01.02.2026
Owner: Jane Doe (Database Administrator), john.smith@example.com
```

**How to Fix:** Make remediation plans SMART:

- **S**pecific: Exactly what will be done
- **M**easurable: How to verify completion
- **A**chievable: Realistic given resources
- **R**elevant: Addresses root cause
- **T**ime-bound: Specific deadline

---

# Evidence Collection Guide

## Required Evidence Categories

**Category 1: Technique Selection Evidence**

**What to Collect:**

- Completed Technique_Selection_Matrix sheet
- Data owner approval emails/sign-offs
- Regulatory requirement analysis
- Alternatives evaluation documentation

**Storage Location:** `/compliance/data-masking/technique-selection/`

**Retention Period:** 7 years (regulatory audit retention requirement)

**Examples:**

- `Technique_Selection_Rationale_Finance_Domain_20260115.pdf` - Documented decision analysis for financial data
- `DataOwner_Approval_CFO_20260115.pdf` - CFO approval email for credit card tokenization
- `PCI_DSS_Compliance_Mapping_20260115.xlsx` - Mapping of PCI-DSS requirements to masking techniques

---

**Category 2: Implementation Evidence**

**What to Collect:**

- Masking tool configuration exports
- Masking script source code (if custom scripts)
- DDM policy exports
- Token vault architecture diagrams

**Storage Location:** `/compliance/data-masking/implementation/`

**Retention Period:** Current version + 2 prior versions

**Examples:**

- `SDM_Configuration_UAT_20260115.xml` - Delphix masking algorithm configuration export
- `DDM_Policies_Production_20260115.json` - Dynamic data masking policy export from database
- `TokenVault_Architecture_v2.pdf` - Token vault infrastructure diagram with security controls
- `mask_customer_data.py` - Custom Python masking script with version control history

---

**Category 3: Validation Evidence**

**What to Collect:**

- Irreversibility test results
- Format preservation validation reports
- Referential integrity test queries and results
- Functionality test results (QA sign-off)
- Performance test results

**Storage Location:** `/compliance/data-masking/validation/`

**Retention Period:** 3 years

**Examples:**

- `Irreversibility_Test_CreditCards_20260115.pdf` - Proof that masked cards cannot be reversed
- `Luhn_Validation_Test_Results_20260115.xlsx` - 100% of masked cards pass Luhn check
- `Referential_Integrity_Test_20260115.sql` - SQL queries proving cross-table consistency
- `QA_Signoff_UAT_Functionality_20260115.pdf` - QA team confirmation application works with masked data
- `Performance_Impact_DDM_20260115.pdf` - DDM overhead measurement (<10ms per query)

---

**Category 4: Approval Evidence**

**What to Collect:**

- Data owner approval records
- Security team sign-off
- Compliance officer approval
- CISO final approval

**Storage Location:** `/compliance/data-masking/approvals/`

**Retention Period:** 7 years

**Examples:**

- `DataOwner_Approvals_All_Domains_20260115.pdf` - Consolidated approval matrix
- `Security_Review_Signoff_20260115.pdf` - Security team approval of technique selections
- `Compliance_Officer_Review_20260115.pdf` - Compliance confirmation of regulatory alignment
- `CISO_Final_Approval_20260115.pdf` - CISO sign-off for deployment authorization

---

## Evidence Collection Workflow

**Step 1: Generate Evidence During Assessment (Ongoing)**

As you complete each assessment step, immediately collect corresponding evidence:

**While completing Technique Selection Matrix:**

- Save decision rationale documents
- Collect regulatory requirement mappings
- Document data owner review meetings (meeting minutes)

**While documenting implementations:**

- Export masking tool configurations
- Screenshot DDM policies
- Backup masking scripts with version control commit hash

**While validating masking:**

- Run validation tests and save results
- Capture test outputs (SQL query results, validation reports)
- Document QA sign-offs

---

**Step 2: Organize Evidence in Evidence_Register Sheet (1 hour)**

**For each evidence item:**

1. Generate Evidence ID (auto-numbered: EV-001, EV-002, etc.)
2. Select Evidence Type from dropdown
3. Write brief Description (1-2 sentences)
4. Reference Related Requirement (policy section or checklist item)
5. Document Related Data/System
6. Record File Location (full path or DMS reference)
7. Enter Created Date
8. Set Retention Period (7 years for audit evidence)
9. Assign Owner/Custodian
10. Set Classification (usually "Confidential" or "Internal")
11. Add Notes if needed

**Example Entry:**
```
Evidence ID: EV-023
Evidence Type: Test Results
Description: Irreversibility test for credit card masking - attempted reversal of 1000 masked cards, 0% success rate
Related Requirement: ISMS-POL-A.8.11, Section 2.4 (Testing and Validation) REQ-TEST-001 (Irreversibility validation)
Related Data/System: Credit card PAN (CAT-FIN) across all systems
File Location: /compliance/data-masking/validation/Irreversibility_Test_CreditCards_20260115.pdf
Created Date: 15.01.2026
Retention Period: 7 years
Owner/Custodian: Security Engineering Team (security@example.com)
Classification: Confidential
Last Verified: 15.01.2026
Notes: Test performed post-UAT refresh. Re-test quarterly with each refresh.
```

---

**Step 3: Verify Evidence Accessibility (15 minutes)**

**Before final submission:**

- [ ] Open Evidence_Register sheet
- [ ] Pick 5 random evidence items
- [ ] Attempt to access each evidence file using documented file location
- [ ] Verify files open correctly and content is as described
- [ ] If any files inaccessible, update file location or regenerate evidence

**Common Issues:**

- File moved → Update file location in Evidence_Register
- File deleted → Regenerate evidence or mark as "Missing - Needs Regeneration"
- Access denied → Verify permissions, add evidence owner to access list
- Wrong file → Correct file location reference

---

**Step 4: Evidence Quality Review (30 minutes)**

**Review each evidence item against quality criteria:**

**Quality Criteria:**

✅ **Relevance:** Evidence actually proves the claim it's supposed to prove

- Example: "Irreversibility test" should show attempted reversal attempts and 0% success rate
- Not just: "Masking completed successfully" (doesn't prove irreversibility)

✅ **Completeness:** Evidence includes all necessary context

- Who performed the test?
- When was it performed?
- What was the methodology?
- What were the results?

✅ **Authenticity:** Evidence is original and unaltered

- Avoid screenshots that could be easily faked (prefer system-generated reports)
- Include metadata (timestamps, author, version)
- Digital signatures if available

✅ **Accessibility:** Evidence can be retrieved within 5 minutes

- File path is correct
- Permissions allow access by auditors/compliance team
- Evidence not stored on personal devices (use shared repositories)

**Poor Quality Evidence Example:**
```
❌ Evidence Type: Screenshot
   Description: "Masking works"
   File Location: "On my desktop"
Problem: Vague description, inaccessible location, no context
```

**Good Quality Evidence Example:**
```
✅ Evidence Type: Test Results
   Description: "Referential integrity validation test for customer data across 5 tables (customers, orders, payments, refunds, support_tickets). SQL query confirmed 0 mismatches after masking."
   File Location: /compliance/data-masking/validation/Referential_Integrity_Test_20260115.sql (query) and results_20260115.xlsx (results showing 0 mismatches)
   Created Date: 15.01.2026
   Owner: Database Admin Team
```

---

## Evidence Storage Best Practices

**Storage Requirements:**

**Security:**

- Evidence contains sensitive information (masking configurations, test data samples)
- Store in access-controlled repository (not public file shares)
- Encryption at rest recommended (AES-256)
- Access logging enabled (who accessed what evidence when)

**Backup:**

- Evidence is required for audits (must not be lost)
- Daily backups to offsite storage
- Backup retention matches evidence retention period (7 years)
- Test restore process quarterly

**Organization:**
```
/compliance/data-masking/
  ├── technique-selection/
  │   ├── 2026/
  │   │   ├── Technique_Selection_Rationale_20260115.pdf
  │   │   ├── DataOwner_Approvals_20260115.pdf
  │   │   └── Regulatory_Mapping_20260115.xlsx
  │   └── 2025/ (prior year for comparison)
  │
  ├── implementation/
  │   ├── sdm/
  │   │   ├── configurations/
  │   │   └── scripts/
  │   ├── ddm/
  │   │   └── policies/
  │   └── tokenization/
  │       └── architecture/
  │
  ├── validation/
  │   ├── irreversibility/
  │   ├── format-preservation/
  │   ├── referential-integrity/
  │   └── functionality/
  │
  └── approvals/
      └── 2026/
```

---

# Review & Approval Process

## Internal Review (Before Formal Approval)

**Reviewer 1: Peer Review (Technical)**

- **Who:** Another security engineer or DBA familiar with masking
- **Focus:** Technical accuracy of technique selections and configurations
- **Checklist:**
  - [ ] Technique selections appropriate for data types
  - [ ] Configuration details technically sound
  - [ ] Referential integrity considerations addressed
  - [ ] Performance implications considered
  - [ ] Implementation details sufficient for deployment

**Reviewer 2: Data Owner Review (Business)**

- **Who:** Data owner for each data domain (Finance, HR, Customer, etc.)
- **Focus:** Business functionality preserved, regulatory requirements met
- **Checklist:**
  - [ ] Masked data will support business operations
  - [ ] Regulatory requirements addressed
  - [ ] Data utility maintained for intended use cases
  - [ ] Risks acceptable

**Reviewer 3: Compliance Officer Review (Regulatory)**

- **Who:** DPO, Compliance Officer, or Legal Counsel
- **Focus:** Regulatory compliance verification
- **Checklist:**
  - [ ] GDPR pseudonymization requirements met
  - [ ] PCI-DSS masking requirements met (if applicable)
  - [ ] HIPAA de-identification requirements met (if applicable)
  - [ ] Other applicable regulations addressed

---

## Formal Approval Sign-Off

**Approval Sequence:**

**Step 1: Data Owner Approval**

- **When:** After technique selection matrix complete
- **What:** Data owner approves techniques for their data domain
- **Evidence:** Approval email or signed Technique_Selection_Matrix sheet

**Step 2: Security Team Approval**

- **When:** After implementation documentation complete
- **What:** Security team confirms masking implementations adequate
- **Evidence:** Security review sign-off document

**Step 3: Compliance Officer Approval**

- **When:** After regulatory mapping verified
- **What:** Compliance confirms regulatory requirements met
- **Evidence:** Compliance approval memo

**Step 4: CISO Final Approval**

- **When:** After all above approvals obtained
- **What:** CISO authorizes deployment of masking implementations
- **Evidence:** CISO sign-off in Summary_Dashboard sheet

---

## Approval Documentation

**Open Summary_Dashboard sheet → Approval Sign-Off section**

**Complete the following:**

| Role | Name | Signature | Date | Comments |
|------|------|-----------|------|----------|
| Data Owner (Finance) | [Name] | [Signature/Email] | [Date] | "Approved tokenization for payment cards, SDM for account numbers" |
| Data Owner (HR) | [Name] | [Signature/Email] | [Date] | "Approved SDM for employee SSN, hashing for passwords" |
| Security Team Lead | [Name] | [Signature/Email] | [Date] | "All technique selections security-appropriate" |
| Compliance Officer | [Name] | [Signature/Email] | [Date] | "GDPR, PCI-DSS requirements addressed" |
| CISO | [Name] | [Signature/Email] | [Date] | "Approved for implementation. Proceed to IMP-A.8.11.3" |

**Approval Methods:**

- **In-person:** Signature in physical workbook printout
- **Electronic:** Email approval with reference to workbook version
- **Digital signature:** DocuSign or equivalent (if available)

**Store Approvals:** Save approval emails/documents in Evidence_Register

---

# Next Steps After Approval

## Handoff to Implementation Team

**After CISO approval, this assessment feeds into:**

➡️ **ISMS-IMP-A.8.11.3 (Environment Coverage Assessment)**

- Use technique selections from this assessment
- Verify implementation across all environments (Prod, Dev, Test, UAT, etc.)
- Document coverage gaps

➡️ **ISMS-IMP-A.8.11.4 (Testing & Validation Framework)**

- Use validation criteria from this assessment
- Implement comprehensive testing (irreversibility, functionality, performance)
- Document test results

➡️ **ISMS-IMP-A.8.11.5 (Compliance Dashboard)**

- Technique selection status feeds into overall compliance score
- Gap analysis feeds into remediation roadmap
- Evidence register consolidates with other assessments

---

## Assessment Maintenance

**This assessment is NOT one-time. Update when:**

**Triggers for Re-assessment:**

- [ ] New sensitive data elements identified (quarterly from IMP-A.8.11.1)
- [ ] New masking techniques available/approved
- [ ] Regulatory requirements change (new regulations, updated guidance)
- [ ] Masking tool/vendor changes
- [ ] Major system changes (new applications, database migrations)
- [ ] Gap remediation completed (update compliance status)

**Regular Review Cycle:**

- **Semi-Annual (every 6 months):** Review and update technique selections
- **Annual:** Full re-assessment with updated data inventory
- **After major changes:** Ad-hoc re-assessment

---

---

# Document Sign-Off

**Assessment Guide Prepared By:**

- Name: ISMS Implementation Team
- Date: [Date]

**Assessment Guide Reviewed By:**

- CISO: ___________________________ Date: __________
- Data Protection Officer: ___________________________ Date: __________
- Compliance Officer: ___________________________ Date: __________

**Assessment Guide Approved By:**

- CISO: ___________________________ Date: __________

**Next Review Date:** 20.07.2026 (6 months)

---

**END OF USER GUIDE**

---

*"The right masking technique is the one that protects data, maintains functionality, meets regulations, and can be validated. If you can't prove it works, it doesn't work."*
— Data Protection Maxim

<!-- QA_VERIFIED: 2026-02-06 -->
