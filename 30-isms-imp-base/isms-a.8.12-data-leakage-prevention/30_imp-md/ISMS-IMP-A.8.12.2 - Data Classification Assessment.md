**ISMS-IMP-A.8.12.2 - Data Classification Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention

# PART I: USER COMPLETION GUIDE

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.12.2 |
| **Version** | 1.0 |
| **Assessment Area** | Data Classification and Identification for DLP |
| **Related Policy** | ISMS-POL-A.8.12 (Data Leakage Prevention Policy) - Section 2.1 |
| **Purpose** | Assess data classification scheme implementation, sensitive data identification methods, and DLP rule accuracy to ensure protection scope aligns with organizational risk appetite |
| **Target Audience** | Data Classification Officers, DLP Administrators, Data Owners, Security Engineers, Compliance Officers, CISO |
| **Assessment Type** | Operational & Governance Assessment |
| **Review Cycle** | Quarterly or After Data Classification Policy Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Data Classification assessment | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** Data Classification Officers, DLP Administrators, Data Owners, Security Engineers, Compliance Officers

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organization]'s **data classification scheme and DLP detection capabilities** to ensure compliance with ISO/IEC 27001:2022 Control A.8.12 and applicable regulatory requirements.

**Scope:** 5 assessment domains covering data identification and classification:
1. **Data Classification Scheme** - Classification levels, definitions, ownership, labeling standards
2. **Sensitive Data Inventory** - PII, financial data, IP, credentials, customer data
3. **DLP Detection Methods** - Content inspection, pattern matching, contextual analysis, ML/AI
4. **Classification Enforcement** - Document labeling, metadata tagging, automated classification
5. **Pattern Library Management** - Regex patterns, fingerprints, dictionaries, accuracy testing

**Assessment Output:** Excel workbook with ~60 data classification checkpoints documenting classification governance, sensitive data catalog, detection method effectiveness, and pattern accuracy metrics.

## Why This Matters

**ISO 27001:2022 Control A.8.12 Requirement:**
> *"Data leakage prevention measures should be applied to systems, networks and any other devices that process, store or transmit sensitive information."*

**Key Dependency:** DLP effectiveness depends entirely on **knowing what data to protect**. Without accurate data classification and identification, DLP controls are ineffective (false positives overwhelm security teams, false negatives allow data leakage).

**Regulatory Context:**

- **Swiss nDSG (Art. 5, 6):** Requires data controllers to know what personal data they process
- **EU GDPR (Art. 30):** Mandates records of processing activities (knowing data inventory)
- **Industry Standards:** PCI DSS (Req. 3), HIPAA (§164.308), SOC 2 all require data discovery and classification


**Business Impact:**

- **Ineffective DLP:** Without classification, DLP either blocks everything (false positives → business disruption) or nothing (false negatives → data breaches)
- **Compliance Violations:** Regulators require demonstrating you know what data you have and where it is
- **Incident Response:** Data breach notification obligations depend on knowing what data was leaked
- **Risk Prioritization:** Can't assess data leakage risk without knowing data sensitivity


**Why Classification Assessment Matters:**

- **Accuracy Verification:** Are DLP patterns actually detecting the data they should?
- **Coverage Validation:** Have we identified ALL sensitive data types in the organization?
- **Governance Check:** Do data owners understand their classification responsibilities?
- **False Positive Management:** Are classification rules too broad (everything flagged) or too narrow (nothing detected)?


## Who Should Complete This Assessment

**Primary Responsibility:** Data Classification Officer (if role exists), DLP Administrators, Information Security Officers

**Required Knowledge:**

- [Organization]'s data classification policy and scheme (Public/Internal/Confidential/Restricted)
- Sensitive data types processed by [Organization] (PII, financial, healthcare, IP, etc.)
- DLP detection methods in use (content inspection, labeling, fingerprinting)
- Data ownership structure (who owns which data categories)


**Support Roles:**

- **Data Owners:** Business leaders responsible for specific data categories (HR data, customer data, financial data)
- **Legal/Compliance:** Regulatory data protection requirements, data retention obligations
- **DPO (Data Protection Officer):** Personal data processing inventory, GDPR/nDSG compliance
- **DLP Administrators:** Technical pattern configuration, detection accuracy, false positive tuning
- **Application Owners:** Where sensitive data resides (databases, file shares, SaaS applications)


## Time Estimate

**Total Assessment Time:** 5-7 hours (depending on data classification maturity)

**Breakdown:**

- **Information Gathering:** 2-3 hours (inventory sensitive data types, review classification policy, collect data ownership records)
- **Assessment Completion:** 2-3 hours (complete all 5 domain sheets, verify detection accuracy)
- **Testing & Validation:** 1 hour (test DLP patterns against sample data, verify detection)
- **Evidence Collection:** 30-60 minutes (screenshots, policy exports, test results)
- **Quality Review:** 30 minutes (self-check using Section 7 quality checklist)


**Pro Tip:** For organizations without formal data classification program, this assessment will take longer (8-10 hours) as you'll need to conduct discovery of sensitive data types during the assessment itself.

## Connection to Policy

This assessment implements **ISMS-POL-A.8.12 (Data Leakage Prevention Policy)** Section 2.1 (Data Classification & Identification Requirements) which mandates:

**Policy Requirements Verified:**

- **Section 2.1 - Data Classification:** Classification-based DLP protection (Restricted = full DLP, Confidential = monitoring + blocking, Internal = monitoring)
- **Section 2.1 - Data Identification Methods:** Content inspection, document labeling, contextual analysis, ML/AI
- **Section 2.1 - Sensitive Data Categories:** PII, financial, healthcare, credentials, IP, customer data, employee data
- **Section 3.2 - Assessment & Verification:** Quarterly data classification review
- **Section 4.2 - Implementation Resources:** Structured assessment workbooks


**Policy Authority:** Chief Information Security Officer (CISO)  
**Compliance Status:** Mandatory for all DLP deployments

**Relationship to Other Assessments:**

- **A.8.12.1 (DLP Infrastructure):** Verifies DLP technology exists → THIS assessment verifies DLP knows WHAT to protect
- **A.8.12.3 (Channel Coverage):** Verifies DLP policies deployed → THIS assessment verifies policies detect correct data
- **A.8.12.4 (Monitoring & Response):** Assesses alert effectiveness → THIS assessment ensures alerts are for REAL sensitive data (not false positives)
- **A.8.12.5 (Compliance Dashboard):** Consolidates all assessments


## Critical: Data Classification Maturity Model

**⚠️ IMPORTANT - Classification Maturity Determines DLP Effectiveness:**

Organizations fall into different data classification maturity levels. DLP effectiveness directly correlates with classification maturity.

**Maturity Levels:**

| Level | Characteristics | DLP Impact | Action Required |
|-------|----------------|------------|-----------------|
| **Level 0: Ad-Hoc** | No classification scheme, data discovery incomplete | DLP ineffective (too many false positives or false negatives) | **Establish classification scheme FIRST before deploying DLP** |
| **Level 1: Defined** | Classification scheme exists, manual labeling only | DLP partially effective (relies on users to label correctly) | Implement automated classification, regular audits |
| **Level 2: Managed** | Automated classification in key systems, pattern library maintained | DLP effective for structured data | Extend to unstructured data, tune patterns |
| **Level 3: Optimized** | ML-based classification, continuous pattern accuracy monitoring | DLP highly effective | Focus on edge cases, advanced threats |

**What This Means for Assessment:**

- **Level 0-1 organizations:** Will identify significant gaps in this assessment (expected, not a failure)
- **Level 2-3 organizations:** Assessment focuses on optimization and edge case detection
- **Honest assessment critical:** Don't inflate maturity level to "look good" - audit will expose gaps


**Common Issue:** Organizations implement DLP before establishing data classification. Result = DLP deployed but doesn't know what to protect = waste of money and creates false sense of security.

**Best Practice:** If this assessment reveals Level 0-1 maturity, PAUSE DLP deployment, fix data classification FIRST, then resume DLP.

---

# Prerequisites

## Access Required

**Policy & Governance Documentation:**

- [ ] Data classification policy (current version with approval signatures)
- [ ] Data handling procedures and guidelines
- [ ] Data ownership register (RACI matrix for data categories)
- [ ] Information asset register (inventory of systems and data)


**Technical Documentation:**

- [ ] DLP pattern library (regex patterns, fingerprints, dictionaries)
- [ ] DLP rule configuration (content inspection rules, labeling rules)
- [ ] Data discovery scan results (if data discovery tools deployed)
- [ ] Classification automation configuration (if automated classification tools deployed)


**System Access:**

- [ ] DLP management console (to review patterns and test detection)
- [ ] Document management systems (SharePoint, Box, Google Drive - to check labeling implementation)
- [ ] Email system administration (to verify email classification labels)
- [ ] Database query access (to sample data for classification verification)
- [ ] File share access (to verify classification labels on documents)


**Stakeholder Access:**

- [ ] Data Owners (interviews/meetings to verify understanding of classification responsibilities)
- [ ] DPO/Legal (to review personal data inventory, regulatory obligations)
- [ ] Application Owners (to identify where sensitive data resides)


## Knowledge Required

**Essential Understanding:**

- [Organization]'s data classification scheme (classification levels and definitions)
- Regulatory data protection requirements applicable to [Organization]
- What constitutes PII, financial data, IP, credentials in [Organization]'s context
- Basic understanding of DLP detection methods (pattern matching, labeling, contextual)


**Technical Skills:**

- Ability to read and understand regex patterns (for pattern library review)
- Basic SQL queries (for data sampling and verification)
- Document metadata inspection (to verify classification labels)
- Understanding of false positive vs. false negative tradeoffs


**NOT Required:**

- DLP rule development expertise (covered in A.8.12.3 Channel Coverage)
- Advanced regex programming
- Machine learning algorithm expertise
- Data science or analytics skills


## Tools Needed

**Assessment Tools:**

- **DLP testing capability:** Ability to send test data through DLP and verify detection
- **Data sampling:** Access to sample real data for classification verification
- **Pattern testing:** Tools to test regex patterns against sample data


**Evidence Collection:**

- **Screenshot tool:** Classification policy, DLP pattern library, test results
- **Export capability:** Pattern library exports, classification statistics
- **Document access:** Sample classified documents for evidence


**Optional but Recommended:**

- **Data discovery tool:** Automated sensitive data discovery (Spirion, Varonis, BigID, etc.)
- **Classification automation:** Microsoft Purview Information Protection, Boldon James, etc.
- **Pattern testing tool:** Regex testing website (regex101.com) or DLP vendor testing tool


## Estimated Time Commitment

**Phase 1: Policy & Governance Review (1-2 hours)**

- Review data classification policy and definitions
- Interview data owners about classification understanding
- Review data ownership register
- Collect classification governance documentation


**Phase 2: Data Inventory Verification (2-3 hours)**

- Review sensitive data categories defined in policy
- Conduct gap analysis (are there data types NOT classified?)
- Verify data discovery completeness (do we know where sensitive data resides?)
- Sample data from key systems to verify classification accuracy


**Phase 3: DLP Pattern Assessment (1-2 hours)**

- Review DLP pattern library (regex, fingerprints, dictionaries)
- Test patterns against sample data (accuracy verification)
- Calculate false positive and false negative rates (if data available)
- Review pattern maintenance procedures


**Phase 4: Classification Enforcement Verification (30-60 minutes)**

- Check document labeling implementation (% of documents with classification labels)
- Verify automated classification coverage (which systems have auto-classification)
- Test classification workflows (create document, verify label applied)


**Phase 5: Assessment Completion & Evidence (1 hour)**

- Complete all 5 domain sheets
- Document gaps and create remediation plans
- Collect evidence files
- Populate Evidence Register
- Review Summary Dashboard


**Total:** 5-7 hours (Level 2-3 maturity), 8-10 hours (Level 0-1 maturity - significant discovery work)

---

# Assessment Workflow

## Recommended Completion Sequence

**STEP 1: Initial Setup (10 minutes)**
1. Open workbook: `ISMS-IMP-A.8.12.2_Data_Classification_YYYYMMDD.xlsx`
2. Review Instructions_Legend sheet
3. Complete Organization Metadata (yellow cells)

**STEP 2: Data Classification Scheme Assessment (45-60 minutes)**
1. Navigate to Classification_Scheme sheet
2. Review current data classification policy
3. Document classification levels (typically: Public, Internal, Confidential, Restricted)
4. For each level: definition, data examples, handling requirements
5. Verify data ownership structure exists
6. Check classification training completion rates
7. Status determination (see Section 4.1)
8. Collect evidence: classification policy PDF, data ownership register

**STEP 3: Sensitive Data Inventory (1-2 hours)**
1. Navigate to Sensitive_Data_Inventory sheet
2. List all sensitive data categories processed by [Organization]:

   - Personal Identifiable Information (PII)
   - Financial data (credit cards, bank accounts, payment data)
   - Healthcare data (if applicable)
   - Authentication credentials (passwords, API keys, certificates)
   - Intellectual Property (source code, designs, trade secrets)
   - Customer data (customer lists, contracts, pricing)
   - Employee data (HR records, payroll, performance reviews)

3. For each category:

   - Document data examples
   - Identify where data resides (systems, databases, file shares)
   - Verify DLP coverage (is this data type protected by DLP?)
   - Check regulatory drivers (Swiss nDSG, GDPR, PCI DSS, etc.)

4. Status determination (see Section 4.2)
5. Collect evidence: data inventory spreadsheet, data flow diagrams

**STEP 4: DLP Detection Methods Assessment (1-2 hours)**
1. Navigate to Detection_Methods sheet
2. For each detection method:

   - **Content Inspection:** Regex patterns, keyword detection
   - **Document Labeling:** Classification metadata in files
   - **Contextual Analysis:** Source system, user role, destination
   - **Machine Learning:** AI-based sensitive content detection
   - **Fingerprinting:** Hash-based document tracking

3. Test each method with sample data:

   - Content inspection: Send email with fake credit card number, verify detection
   - Document labeling: Create labeled document, verify DLP detects label
   - Contextual: Export from HR database, verify DLP recognizes HR data

4. Calculate detection accuracy (if test data available)
5. Status determination (see Section 4.3)
6. Collect evidence: DLP test results, pattern library export

**STEP 5: Classification Enforcement Verification (30-45 minutes)**
1. Navigate to Classification_Enforcement sheet
2. Check document labeling implementation:

   - What % of documents have classification labels?
   - Manual labeling vs. automated?
   - Label enforcement (users required to classify before saving)?

3. Verify automated classification:

   - Which systems have auto-classification enabled?
   - Classification accuracy (does auto-classification work correctly)?
   - Override capability (can users override auto-classification if wrong)?

4. Test classification workflow:

   - Create document in SharePoint/Google Drive
   - Verify classification prompt appears
   - Verify label is applied to document metadata

5. Status determination (see Section 4.4)
6. Collect evidence: classification workflow screenshots, label statistics

**STEP 6: Pattern Library Management (45-60 minutes)**
1. Navigate to Pattern_Library sheet
2. Document all DLP patterns:

   - PII patterns (SSN, credit card, passport, driver's license, etc.)
   - Financial patterns (IBAN, SWIFT, account numbers)
   - Credentials (API keys, passwords, certificates)
   - Custom patterns (product codes, internal IDs)

3. For each pattern:

   - Pattern definition (regex or description)
   - Accuracy (false positive rate, false negative rate)
   - Last tested date
   - Maintenance owner

4. Test critical patterns:

   - Credit card: Test with valid and invalid formats
   - SSN: Test with and without dashes
   - API keys: Test common formats (AWS, Azure, Google)

5. Status determination (see Section 4.5)
6. Collect evidence: pattern library export, test results spreadsheet

**STEP 7: Gap Analysis & Remediation Planning (30 minutes)**
1. Navigate to Gap_Analysis sheet
2. For each ❌ Non-Compliant or ⚠️ Partial item:

   - Describe gap (e.g., "No classification scheme for customer data")
   - Assess risk (Critical if Restricted data unclassified, High if Confidential, Medium if Internal)
   - Define remediation (e.g., "Create customer data classification definitions, implement DLP rules")
   - Assign owner (Data Owner + DLP Admin)
   - Set target date (Critical <30 days, High <90 days)

3. Prioritize based on data sensitivity and regulatory requirements

**STEP 8: Evidence Register & Final Review (15 minutes)**
1. Navigate to Evidence_Register sheet
2. Document all collected evidence
3. Review Summary_Dashboard for compliance percentage
4. Verify all mandatory fields completed

**STEP 9: Quality Check & Approval (15 minutes)**
1. Complete Quality Checklist (Section 7)
2. Navigate to Approval_Sign-Off sheet
3. Save with completion date in filename

---

# Sheet-by-Sheet Guidance

## Sheet: Classification_Scheme

**Assessment Question:** *"Does your organization have a formal data classification scheme with defined levels, handling requirements, and data owner accountability?"*

**How to Answer:**

- **"Yes":** If formal classification scheme exists, documented in policy, with defined levels (typically 3-4 levels: Public, Internal, Confidential, Restricted)
- **"Partial":** If classification scheme exists but incomplete (e.g., definitions unclear, no data ownership, not enforced)
- **"No":** If no formal classification scheme
- **"N/A":** Not applicable (rare - even smallest organizations need basic classification)


**Understanding the Requirement:**

**Policy (ISMS-POL-A.8.12 Section 2.1):**

- Classification scheme with minimum 3 levels (Public/Internal, Confidential, Restricted)
- Clear definitions and data examples for each level
- Data ownership accountability (named data owners for each category)
- Handling requirements per classification level
- User training on classification responsibilities


**Why Classification Scheme Matters:**

- **DLP foundation:** DLP protection requirements mapped to classification levels
- **Risk-based approach:** Apply strongest DLP controls to highest classification (Restricted), proportionate controls to lower levels
- **User understanding:** Users need clear guidance on what data is sensitive
- **Audit evidence:** Demonstrates systematic approach to data protection


**Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **Classification Level** | Official name | "Restricted", "Confidential", "Internal", "Public" | Data classification policy |
| **Definition** | Brief description | "Highly sensitive data with severe impact if leaked" | Classification policy Section X |
| **Data Examples** | Specific examples | "Credit card numbers, medical records, trade secrets" | Classification policy, data catalog |
| **Handling Requirements** | Security controls | "Encryption required, DLP blocking, MFA access" | Classification policy handling matrix |
| **DLP Protection Requirement** | DLP control level | "Full DLP monitoring + blocking all channels" | ISMS-POL-A.8.12 Section 2.1 table |
| **Data Owner Assigned** | Accountability | Yes/No (Is there a named data owner?) | Data ownership register, RACI matrix |
| **Owner Name/Role** | Who owns this data | "CFO (financial data)", "CISO (credentials)" | Data ownership register |
| **User Training Completed** | Training status | "Annual training - 85% completion" | LMS reports, HR training records |
| **Status** | Compliance status | ✅ / ⚠️ / ❌ / N/A | Based on checklist below |
| **Evidence ID** | Reference | A812-2-CLS-001 | Link to Evidence Register |

**Status Determination:**

**✅ Compliant:**

- Formal classification scheme documented in approved policy
- 3-4 classification levels with clear definitions and data examples
- Data owners assigned and accountable for each data category
- Handling requirements specified for each classification level
- DLP protection requirements aligned with classification levels (Restricted = full DLP, Confidential = selective DLP)
- User training provided annually with >80% completion rate
- Classification scheme reviewed annually and updated as needed


**⚠️ Partial:**

- Classification scheme exists but definitions unclear or incomplete
- Data ownership assigned but owners not actively engaged
- Handling requirements documented but not consistently enforced
- User training provided but low completion rate (<60%)
- Classification scheme outdated (>2 years since last review)
- Some data categories lack clear classification (e.g., customer data not clearly classified)


**❌ Non-Compliant:**

- No formal classification scheme
- Classification scheme exists in name only (not actually used)
- No data ownership accountability
- No user training on classification
- DLP deployed without alignment to classification scheme


**N/A:**

- Not applicable (extremely rare)


**Compliance Checklist:**

- [ ] **Formal classification policy approved by CISO/Executive Management**  

  *Critical:* Classification scheme must have executive sponsorship and approval  
  *How to verify:* Check policy approval signatures, board/management meeting minutes  
  *Evidence:* Classification policy PDF with signature block  

- [ ] **Minimum 3 classification levels defined (Public/Internal, Confidential, Restricted)**  

  *Rationale:* Fewer than 3 levels = insufficient granularity, more than 5 levels = too complex for users  
  *Common scheme:*  

    - **Public:** No restriction, can be publicly disclosed  
    - **Internal:** Organization-only, no external sharing  
    - **Confidential:** Limited distribution, business impact if leaked  
    - **Restricted:** Highest sensitivity, severe impact if leaked, legal/regulatory constraints  

- [ ] **Clear definitions and data examples for each level**  

  *Problem if missing:* Users don't know how to classify data → inconsistent classification → DLP ineffective  
  *Quality check:* Show policy to random employee, ask "Is customer email addresses Confidential or Internal?" - can they answer correctly?  
  *Example definition (Confidential):* "Data that would cause significant financial, legal, or reputational harm to [Organization] if disclosed to unauthorized parties. Examples: customer contracts, pricing information, non-public financial data, employee personal information."  

- [ ] **Data owners assigned and documented for each data category**  

  *Accountability model:*  

    - **Data Owner:** Business leader accountable for data (typically C-level or VP)  
    - **Data Custodian:** IT team maintaining systems where data resides  
    - **Data User:** Employees using data in daily work  

  *Evidence:* Data ownership register with names, roles, contact information  
  *Red flag:* "IT owns all data" → Wrong, business owns data, IT is custodian  

- [ ] **Handling requirements specified per classification level**  

  *Required specifications:*  

    - Storage requirements (encryption, access controls)  
    - Transmission requirements (encrypted channels, DLP)  
    - Disposal requirements (secure deletion, certificate of destruction for Restricted)  
    - Access requirements (who can access, authentication strength)  

  *Example:* Restricted data requires encryption at rest and in transit, MFA for access, DLP blocking, annual access review  

- [ ] **Classification scheme integrated with DLP policy**  

  *Verification:* ISMS-POL-A.8.12 Section 2.1 table shows DLP requirements per classification level  
  *Alignment check:*  

    - Restricted → Full DLP (monitoring + blocking all channels)  
    - Confidential → Selective DLP (monitoring + blocking high-risk channels)  
    - Internal → DLP monitoring (detection without blocking)  
    - Public → No DLP  

- [ ] **User training on classification provided annually**  

  *Training content:*  

    - What is data classification and why it matters  
    - Classification levels and definitions  
    - How to classify data (decision tree or examples)  
    - How to apply classification labels (technical procedure)  
    - Consequences of misclassification  

  *Target completion:* >80% of employees  
  *Evidence:* LMS completion reports, training attendance records  

- [ ] **Classification scheme reviewed and updated annually**  

  *Review triggers:*  

    - Annual review (calendar-based)  
    - New data types (new business lines, M&A, new products)  
    - Regulatory changes (GDPR, sector-specific regulations)  
    - Significant data breaches or near-misses  

  *Review participants:* CISO, DPO, Legal, Data Owners, Compliance  
  *Evidence:* Review meeting minutes, policy version history  

**Common Pitfalls:**

**Pitfall 1:** "We have a classification scheme but users never use it"  
**Problem:** Classification exists on paper only, not operationalized  
**Root causes:**  

- Too complex (5+ levels, unclear definitions)  
- Not integrated into workflows (users have to go out of their way to classify)  
- No consequences for non-compliance  
- No automated classification (100% manual = users ignore it)  

**Solution:**  

- Simplify scheme to 3 levels maximum  
- Integrate classification into document creation workflow (prompt users)  
- Implement automated classification where possible  
- Enforce through DLP (unclassified sensitive data = DLP alert)  


**Pitfall 2:** "Everything is marked Confidential to be safe"  
**Problem:** Over-classification makes DLP unusable (everything flagged = alert fatigue)  
**Root causes:**  

- Users don't understand definitions (when in doubt, mark highest)  
- Fear of consequences (better safe than sorry)  
- No review of classification accuracy  

**Solution:**  

- Clear definitions with specific examples  
- Regular audits of classification accuracy (sample documents, verify correctness)  
- Proportionate DLP controls (don't block Internal data transfers, users won't over-classify)  
- Data owner review of classification decisions for their data category  


**Pitfall 3:** "IT is the data owner for all data"  
**Problem:** Wrong accountability model, business disengaged from data protection  
**Correct model:**  

- **Data Owner = Business role** (CFO owns financial data, CHRO owns employee data, CMO owns customer data)  
- **Data Custodian = IT role** (IT maintains systems, implements technical controls)  
- **Data Protection Officer = Oversight** (ensures compliance, advises on obligations)  

**Solution:** Establish data ownership register with named business leaders as owners  

**Evidence Examples:**

- Data classification policy document: `EV-1-Scheme-20260121-Classification-Policy-v2.0.pdf`
- Classification level definitions: `EV-1-Scheme-20260121-Level-Definitions.xlsx`
- Data ownership register: `EV-1-Scheme-20260121-Data-Ownership-Register.xlsx`
- User training completion report: `EV-1-Scheme-20260121-Training-Completion-Q4-2025.pdf`
- Classification workflow diagram: `EV-1-Scheme-20260121-Workflow-Diagram.png`


---

## Sheet: Sensitive_Data_Inventory

**Assessment Question:** *"Has your organization identified and inventoried all sensitive data types requiring DLP protection?"*

**How to Answer:**

- **"Yes":** If comprehensive sensitive data inventory exists, covering all data categories listed in policy
- **"Partial":** If inventory exists but incomplete (some data types not inventoried, or inventory not maintained)
- **"No":** If no systematic data inventory, relying on ad-hoc knowledge
- **"N/A":** Not applicable (extremely rare - all organizations process some sensitive data)


**Understanding the Requirement:**

**Policy (ISMS-POL-A.8.12 Section 2.1 Table):**
Sensitive data categories requiring DLP protection:

- Personal Data (PII) - Names, addresses, national IDs, phone numbers, emails
- Financial Data - Bank accounts, credit cards, payment data
- Healthcare Data - Medical records, health information (if applicable)
- Authentication Credentials - Passwords, API keys, tokens, certificates, private keys
- Intellectual Property - Source code, designs, patents, trade secrets
- Customer Data - Customer lists, contracts, pricing, CRM data
- Employee Data - HR records, payroll, performance reviews


**Why Data Inventory Matters:**

- **DLP scope definition:** Can't protect data you don't know exists
- **Regulatory compliance:** GDPR Art. 30 requires records of processing activities (data inventory)
- **Risk assessment:** Need to know where sensitive data resides to assess leakage risk
- **Incident response:** Data breach notification requires knowing what data was exposed


**Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **Data Category** | Sensitive data type | "Personal Data (PII)", "Financial Data", "IP" | ISMS-POL-A.8.12 Section 2.1 |
| **Data Examples** | Specific data elements | "SSN, passport, driver's license, email addresses" | Data catalog, application documentation |
| **Systems/Locations** | Where data resides | "HR database, SharePoint, Email, Salesforce" | IT asset inventory, application portfolio |
| **Classification Level** | Per classification scheme | "Restricted", "Confidential", "Internal" | Data classification policy |
| **Volume (approx)** | Scale of data | "100K records", "50TB", "Millions of emails" | Database counts, storage reports |
| **Regulatory Driver** | Why sensitive | "Swiss nDSG Art. 5", "GDPR Art. 4", "PCI DSS Req. 3" | Legal assessment, DPO input |
| **DLP Coverage** | Is DLP protecting this? | Yes/No/Partial | Review DLP policies, test detection |
| **Data Discovery Method** | How identified | "Automated scan", "Manual inventory", "Application documentation" | Data discovery tool reports |
| **Data Owner** | Who owns this data | "CHRO (employee data)", "CFO (financial)" | Data ownership register |
| **Last Reviewed Date** | Inventory freshness | DD.MM.YYYY | Inventory documentation |
| **Status** | Compliance status | ✅ / ⚠️ / ❌ / N/A | Based on checklist below |
| **Evidence ID** | Reference | A812-2-INV-001 | Link to Evidence Register |

**Status Determination:**

**✅ Compliant:**

- Comprehensive data inventory covering all 7+ sensitive data categories from policy
- Data inventory documents: data type, location, classification, volume, regulatory driver
- Data discovery performed within last 12 months (automated or manual)
- All inventoried data types have DLP coverage (verified through testing)
- Data inventory maintained and reviewed quarterly
- Data owners assigned and engaged for each category


**⚠️ Partial:**

- Data inventory exists but incomplete (some categories missing)
- Inventory outdated (>12 months since last update)
- DLP coverage gaps (some inventoried data types not protected by DLP)
- Data discovery manual only (no automated scanning, likely incomplete)
- Data owners assigned but not actively maintaining inventory


**❌ Non-Compliant:**

- No systematic data inventory
- Data inventory ad-hoc (tribal knowledge, not documented)
- Major data categories not inventoried (e.g., customer data or IP not documented)
- No data discovery performed (unknown where sensitive data resides)
- DLP deployed without understanding what data to protect


**N/A:**

- Specific data category not applicable to organization (e.g., healthcare data for non-healthcare organization)


**Compliance Checklist:**

- [ ] **All 7 sensitive data categories from policy inventoried**  

  *Minimum categories:*  
    1. Personal Data (PII)  
    2. Financial Data  
    3. Authentication Credentials  
    4. Intellectual Property  
    5. Customer Data  
    6. Employee Data  
    7. Healthcare Data (if applicable) OR other sector-specific data  
  *How to verify:* Check inventory against policy Section 2.1 table, ensure all categories present  
  *Red flag:* "We only protect PII" → Incomplete, missing other sensitive categories  

- [ ] **Data inventory includes location (systems/applications where data resides)**  

  *Critical for DLP:* Need to know WHERE to deploy DLP controls  
  *Detail level:* Specific systems (not just "databases" but "Oracle HR database", "Salesforce production")  
  *Verification:* For each data category, can you name 3 specific systems where it resides?  
  *Tools:* Data discovery tools (Spirion, Varonis, BigID), application documentation, IT asset inventory  

- [ ] **Data inventory includes volume estimates**  

  *Purpose:*  

    - DLP capacity planning (millions of records require different architecture than thousands)  
    - Risk assessment (1M credit cards leaked >> 100 credit cards)  
    - Breach notification scoping (GDPR requires knowing how many data subjects affected)  

  *Accuracy:* Order of magnitude sufficient ("~100K records" acceptable, exact count not required)  
  *How to obtain:* Database SELECT COUNT(*), storage reports, application metrics  

- [ ] **Regulatory drivers documented for each data category**  

  *Why important:* Determines DLP requirements (GDPR has different requirements than PCI DSS)  
  *Common drivers:*  

    - Swiss nDSG Art. 5, 6 (personal data)  
    - EU GDPR Art. 4, 5, 32 (personal data)  
    - PCI DSS Req. 3, 4 (payment card data)  
    - HIPAA §164.308, §164.312 (healthcare data - US only)  

  *Source:* Legal team, DPO, compliance officer  

- [ ] **DLP coverage verified for all inventoried data types**  

  *Verification method:*  

    - Send test email with sample data (e.g., fake SSN: 123-45-6789)  
    - Verify DLP detects and blocks/alerts  
    - Repeat for each data category  

  *Coverage gap:* Data inventoried but DLP doesn't detect it = **Critical gap** (requires immediate remediation)  
  *Evidence:* DLP test results showing detection for each data category  

- [ ] **Data discovery performed (automated or manual) within last 12 months**  

  *Automated discovery:*  

    - Tools: Spirion, Varonis, BigID, Microsoft Purview, Google Cloud DLP  
    - Scans: File shares, databases, cloud storage, endpoints  
    - Output: Report of sensitive data locations  

  *Manual discovery:*  

    - Interviews with application owners  
    - Application documentation review  
    - Data flow mapping  

  *Frequency:* Annually minimum, quarterly for high-risk organizations  

- [ ] **Data inventory maintained and reviewed quarterly**  

  *Review activities:*  

    - Update for new applications/systems (M&A, new products, cloud migrations)  
    - Remove decommissioned systems  
    - Re-scan for new sensitive data types  
    - Verify DLP coverage still effective  

  *Evidence:* Quarterly review meeting minutes, inventory version history  

**Common Pitfalls:**

**Pitfall 1:** "We use data discovery tool, so we're compliant"  
**Problem:** Tool deployed but results not actioned  
**Reality check:**  

- Data discovery tool finds sensitive data in unexpected locations → Do you remediate (move data to protected location) or just document?  
- Discovery scan results in 10K+ findings → How do you prioritize? Are all findings reviewed?  
- Discovery tool last run 18 months ago → Inventory stale  

**Solution:**  

- Regular discovery scans (quarterly minimum)  
- Remediation process for findings (risk assessment, action plan, ownership)  
- Integration with DLP (discovery findings → DLP policy updates)  


**Pitfall 2:** "We only inventory structured data (databases)"  
**Problem:** Unstructured data (documents, emails, file shares) often contains more sensitive data than databases  
**Statistics:** 80% of organizational data is unstructured, 90% of sensitive data breaches involve unstructured data  
**Solution:**  

- Expand discovery to unstructured data stores (file shares, SharePoint, email archives, endpoints)  
- Use content-aware discovery (not just file name, but inspect file contents)  
- Prioritize high-risk locations (shared drives, contractor endpoints, personal cloud storage)  


**Pitfall 3:** "Data inventory is DPO's job, not DLP team's job"  
**Problem:** Siloed approach, inventory not used for DLP  
**Correct model:**  

- **DPO:** Maintains legal/compliance data inventory (GDPR Art. 30 Records of Processing Activities)  
- **DLP team:** Maintains technical data inventory (where data resides, how to detect it)  
- **Integration required:** DPO inventory + DLP technical inventory = comprehensive data protection  

**Solution:** Joint quarterly review meeting (DPO + CISO + DLP team) to align inventories  

**Evidence Examples:**

- Sensitive data inventory spreadsheet: `EV-2-Inventory-20260121-Sensitive-Data-Catalog.xlsx`
- Data discovery scan results: `EV-2-Inventory-20260121-Discovery-Scan-Report.pdf`
- Data flow diagram: `EV-2-Inventory-20260121-Data-Flow-Diagram.png`
- DLP coverage test results: `EV-2-Inventory-20260121-DLP-Detection-Tests.xlsx`
- Regulatory mapping table: `EV-2-Inventory-20260121-Regulatory-Requirements.pdf`


---

# Evidence Collection

## General Evidence Guidelines

**Evidence Naming Convention:**
```
EV-[Domain]-[Category]-[Date]-[Description].[ext]
```

**Domain Codes:**

- 1 = Classification Scheme
- 2 = Sensitive Data Inventory
- 3 = Detection Methods
- 4 = Classification Enforcement
- 5 = Pattern Library


**Examples:**

- `EV-1-Scheme-20260121-Classification-Policy-v2.0.pdf`
- `EV-2-Inventory-20260121-PII-Discovery-Scan.pdf`
- `EV-3-Detection-20260121-Content-Inspection-Test-Results.xlsx`
- `EV-4-Enforcement-20260121-Document-Labeling-Statistics.png`
- `EV-5-Patterns-20260121-Credit-Card-Pattern-Accuracy-Tests.xlsx`


**Storage Requirements:**

- **Location:** `ISMS/Controls/A.8.12_DLP/Assessments/Data_Classification/Evidence/`
- **Retention:** Audit cycle + 1 year (typically 2-3 years)
- **Sensitivity:** Internal (may contain sample data, sanitize if needed)
- **Access Control:** Security Team, DPO, Auditors


**Evidence Quality Criteria:**

- **Timestamped:** Screenshots include date/time
- **Complete:** Full policy documents, not excerpts
- **Attributable:** Clear which system/process documented
- **Verifiable:** Auditor can reproduce collection
- **Protected:** Sanitize sensitive data in evidence files


## Evidence Types by Domain

**1. Classification Scheme:**

- Data classification policy (approved, signed)
- Data ownership register
- User training materials and completion reports
- Classification workflow diagrams


**2. Sensitive Data Inventory:**

- Data inventory spreadsheet (all categories)
- Data discovery scan results
- Data flow diagrams
- Regulatory mapping documentation


**3. Detection Methods:**

- DLP detection test results (per method)
- Pattern accuracy test spreadsheets
- DLP console screenshots showing rules
- False positive/negative analysis


**4. Classification Enforcement:**

- Document labeling statistics
- Classification automation configuration
- Label application workflow screenshots
- Label accuracy audit results


**5. Pattern Library:**

- Pattern library export (all patterns)
- Pattern accuracy test results
- Pattern maintenance procedures
- Pattern testing tools/scripts


**Minimum Evidence Required:**

- Classification Scheme: 4 items (policy, ownership, training, workflow)
- Sensitive Data Inventory: 3 items (inventory, discovery scan, regulatory mapping)
- Detection Methods: 3 items (test results per method)
- Classification Enforcement: 2 items (labeling stats, automation config)
- Pattern Library: 3 items (library export, accuracy tests, procedures)


**Total Minimum:** 15 evidence items

---

# Common Pitfalls and How to Avoid Them

## "We classify everything as Confidential to be safe"

**Problem:** Over-classification renders DLP useless (everything flagged)  
**Impact:**  

- DLP alert fatigue (security team ignores alerts)  
- Business disruption (legitimate work blocked)  
- Wasted DLP investment (can't differentiate real threats from normal work)


**Root Cause:** Users don't understand classification or fear consequences of under-classification

**Solution:**
1. **Improve classification definitions** - Use clear, simple language with specific examples
2. **Proportionate controls** - Don't block Internal data (only Confidential/Restricted), users won't over-classify to avoid blocking
3. **Regular audits** - Sample classified documents, verify accuracy, provide feedback to users
4. **Automated classification** - Use ML to suggest classification, reduce user burden
5. **Data owner accountability** - Data owners review classification in their domain, correct over-classification

## "We have 100K+ DLP false positives per day"

**Problem:** DLP patterns too broad, detecting non-sensitive data as sensitive  
**Impact:**  

- Security team overwhelmed, can't review all alerts
- Real data leakage missed in noise
- Users lose trust in DLP, find workarounds


**Root Causes:**

- Overly broad regex (e.g., `\d{16}` matches ANY 16 digits, not just credit cards)
- No contextual analysis (credit card in test environment vs. production)
- No pattern accuracy testing before deployment


**Solution:**
1. **Baseline false positive rate** - Measure current FP rate (FP / Total Alerts × 100)
2. **Target <10% FP rate** - Industry best practice
3. **Tune patterns iteratively:**

   - Start with high-confidence patterns (Luhn algorithm for credit cards, not just 16 digits)
   - Add contextual checks (source system, user role, file type)
   - Test against real data samples before production deployment

4. **Implement ML-based detection** - ML better at context than regex
5. **User feedback loop** - Allow users to report false positives, incorporate into tuning

**Measurement:**
```
False Positive Rate = (False Positives / Total Alerts) × 100
Target: <10%
Critical threshold: >30% (DLP ineffective)
```

## "DLP doesn't detect our most sensitive data"

**Problem:** False negatives - DLP fails to detect actual sensitive data  
**Impact:**  

- Data leakage undetected
- Compliance violations (promised protection not delivered)
- False sense of security ("We have DLP, we're safe")


**Root Causes:**

- Incomplete data inventory (don't know all sensitive data types)
- Pattern gaps (missing detection logic for specific data formats)
- Evasion techniques (users/attackers obfuscate data to bypass DLP)


**Solution:**
1. **Comprehensive data inventory** - Discovery scans + manual review
2. **Test detection coverage:**

   - Create sample data for each category
   - Send via all channels (email, web, USB)
   - Verify DLP detects

3. **Red team testing** - Try to bypass DLP intentionally, find gaps
4. **Continuous pattern updates** - New data formats appear (new API key formats, new card types)
5. **Layered detection** - Use multiple methods (content inspection + labeling + contextual)

**Measurement:**
```
Detection Coverage = (Data Categories with DLP Coverage / Total Data Categories) × 100
Target: 100% for Restricted/Confidential data
```

## "Users ignore classification prompts (click through without reading)"

**Problem:** Classification automation prompts users but users always select same option  
**Impact:**  

- Incorrect classification
- DLP protecting wrong data or missing sensitive data


**Root Causes:**

- Too many prompts (prompt fatigue)
- Unclear options (users don't understand choices)
- No consequences (wrong classification = no impact on user)


**Solution:**
1. **Reduce prompt frequency:**

   - Auto-classify common file types (Excel in Finance folder = likely Confidential)
   - Only prompt for ambiguous cases

2. **Improve prompt design:**

   - Show examples: "Confidential examples: Customer contracts, pricing, financial reports"
   - Use simple language (avoid "PII", say "personal information like names and addresses")

3. **Enforce correctness:**

   - Periodic audits of user classifications
   - Feedback to users who consistently misclassify
   - DLP alerts on misclassified documents (unclassified sensitive data = alert)

4. **Default-deny for high-risk actions:**

   - Unclassified document upload to external site = blocked
   - User must classify before upload (forces engagement)


## "We don't have budget for data discovery tools"

**Problem:** Manual data inventory is incomplete and quickly outdated  
**Impact:**  

- Unknown sensitive data locations
- DLP coverage gaps
- Compliance risk (GDPR requires knowing what data you process)


**Solution (without expensive tools):**
1. **Use built-in capabilities:**

   - **Microsoft 365:** Microsoft Purview (included in E5), Content Search
   - **Google Workspace:** Cloud DLP API (limited free tier), Drive audit logs
   - **Windows Server:** File Server Resource Manager (FSRM) file screening

2. **Manual techniques:**

   - Application documentation review (what data does each app process?)
   - Data owner interviews (where is your sensitive data?)
   - Sampling: Manually review high-risk locations (shared drives, contractor endpoints)

3. **Prioritize high-risk locations:**

   - Start with most likely to contain sensitive data (HR systems, finance databases, customer CRM)
   - Expand coverage over time

4. **Scripted scanning:**

   - Simple grep/regex scripts to search for SSN patterns, credit cards, etc.
   - Not as sophisticated as commercial tools but free


**Free/Open Source Options:**

- **Maigret:** OSINT tool for finding data leakage
- **GitLeaks:** Find secrets in Git repos
- **TruffleHog:** Find credentials in code
- **PowerShell scripts:** Custom regex search scripts


## "Classification scheme is too complex (7 levels), nobody uses it correctly"

**Problem:** Over-engineering classification  
**Impact:**  

- Users confused, classify incorrectly
- Inconsistent classification across organization
- DLP rules complex, error-prone


**Solution:**
1. **Simplify to 3-4 levels maximum:**

   - **Public:** Can be publicly disclosed
   - **Internal:** Organization-only, no external sharing (combine "Internal" and "Internal Only")
   - **Confidential:** Limited distribution, business impact (combine "Confidential" and "Sensitive")
   - **Restricted:** Highest sensitivity, severe impact

2. **Clear decision tree:**
   ```
   Would public disclosure cause legal/regulatory violation? → Restricted
   Would disclosure cause significant business harm? → Confidential
   Is this for internal use only? → Internal
   Can this be publicly shared? → Public
   ```
3. **Retire unused levels:**

   - Review usage statistics (which levels actually used?)
   - Consolidate rarely-used levels
   - Migrate documents from retired levels


---

# Quality Checklist (Self-Review Before Submission)

**Completeness Check:**

- [ ] All 5 domain sheets completed (Classification Scheme, Sensitive Data Inventory, Detection Methods, Classification Enforcement, Pattern Library)
- [ ] No blank mandatory fields (Status, Evidence ID columns populated)
- [ ] All 7+ sensitive data categories from policy inventoried
- [ ] DLP detection coverage verified for each data category (test results documented)
- [ ] Gap Analysis completed for all ❌ Non-Compliant and ⚠️ Partial items
- [ ] Remediation plans include: Gap description, Risk level, Action, Owner, Target Date
- [ ] Summary Dashboard shows compliance percentage calculated


**Accuracy Check:**

- [ ] Classification scheme levels match current approved policy (not outdated version)
- [ ] Data inventory cross-referenced with DPO's GDPR Art. 30 records of processing
- [ ] Pattern accuracy test results based on actual testing (not assumptions)
- [ ] False positive rates calculated from real DLP alert data
- [ ] Data owner names verified (not "TBD" or generic roles)
- [ ] Regulatory drivers confirmed with Legal/DPO


**Evidence Quality:**

- [ ] Minimum 2-3 evidence items per domain (15 total minimum)
- [ ] Evidence files follow naming convention
- [ ] Classification policy includes approval signatures
- [ ] Test results include timestamps and methodology
- [ ] Sensitive data sanitized in evidence files (no real credit cards, SSNs, etc.)
- [ ] Evidence Register links verified (files actually exist at specified paths)


**Policy Alignment:**

- [ ] Assessment covers all data categories from ISMS-POL-A.8.12 Section 2.1 table
- [ ] DLP protection requirements per classification level verified
- [ ] Classification maturity level honestly assessed (don't inflate to look good)
- [ ] Gaps mapped to specific policy requirements


**Detection Verification:**

- [ ] DLP detection tested for each sensitive data category (not just assumed)
- [ ] Test methodology documented (what test data used, what channels tested)
- [ ] False positive and false negative rates measured (if data available)
- [ ] Pattern accuracy verified through testing (not just pattern existence)


**Stakeholder Engagement:**

- [ ] Data owners consulted for their data categories
- [ ] DPO reviewed personal data inventory alignment
- [ ] Legal reviewed regulatory drivers
- [ ] Users surveyed or interviewed about classification understanding


**Final Checks:**

- [ ] Workbook filename includes date: `ISMS-IMP-A.8.12.2_Data_Classification_20260121.xlsx`
- [ ] All formulas calculate correctly (no #REF, #DIV/0, #VALUE errors)
- [ ] Conditional formatting working (✅=Green, ⚠️=Yellow, ❌=Red)
- [ ] Sheet protection enabled (formula cells locked)


---

# Review & Approval Process

## Assessment Metadata

**Assessment Period:** From _______ to _______  
**Assessment Date:** _______  
**Assessment Type:**

- [ ] Initial Assessment
- [ ] Quarterly Review
- [ ] Ad-Hoc Assessment (trigger: _____)
- [ ] Post-Policy Update


## Completed By (Primary Assessor)

**Name:** _______________________  
**Role:** _______________________ (e.g., Data Classification Officer, DLP Administrator)  
**Email:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Assessment Declaration:**
I confirm that:

- All information is accurate based on available documentation and testing
- Evidence collected is authentic and verifiable
- Data owners consulted for their respective categories
- DLP detection tested, not assumed
- Classification maturity level honestly assessed


## Reviewed By (Information Security Manager / CISO)

**Name:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Review Comments:**
_________________________________________________________________

**Review Outcome:**

- [ ] Approved - Ready for deployment
- [ ] Approved with minor corrections: _______
- [ ] Requires revision: _______


## Consulted Stakeholders

**Data Protection Officer (DPO):**
**Name:** _______________________  
**Date:** _______________________  
**Comments:** Data inventory aligns with GDPR Art. 30 records: Yes / No / Partial  
_________________________________________________________________

**Legal/Compliance:**
**Name:** _______________________  
**Date:** _______________________  
**Comments:** Regulatory drivers confirmed: Yes / No / Needs revision  
_________________________________________________________________

## Approved By (CISO)

**Name:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Approval Decision:**

- [ ] Approved - Classification framework adequate for DLP
- [ ] Approved with conditions - Remediation required by: _______
- [ ] Rejected - Re-assessment required: _______


**Risk Acceptance:**
For documented gaps (classification maturity, pattern accuracy, coverage):

- [ ] Residual risk accepted with documented compensating controls
- [ ] Remediation required before DLP deployment
- [ ] Escalation to Executive Management required (Critical gaps)


**Budget Approval (if remediation requires funding):**
Estimated cost: _______

- [ ] Approved (data discovery tools, classification automation, consulting)
- [ ] Requires business case
- [ ] Deferred to next budget cycle


## Next Review Date

**Next Scheduled Assessment:** _______________________

**Review Cycle:** Quarterly or upon:

- Major policy changes (classification scheme updates)
- New sensitive data types identified (M&A, new products, new regulations)
- DLP detection accuracy issues (high false positive/negative rates)
- Data breaches involving DLP failures
- Regulatory changes (new data protection laws)


**Interim Monitoring:**

- Pattern accuracy: Monthly testing of critical patterns
- Classification compliance: Quarterly audits of document labeling
- Data inventory: Continuous updates as new systems deployed


## Distribution List

This assessment shall be distributed to:

- [ ] CISO
- [ ] Data Classification Officer (if role exists)
- [ ] DLP Administrators
- [ ] Data Protection Officer (DPO)
- [ ] Legal/Compliance
- [ ] Data Owners (executive summary only)
- [ ] Internal Audit
- [ ] IT Management


**Storage Location:**
`ISMS/Controls/A.8.12_DLP/Assessments/Data_Classification/ISMS-IMP-A.8.12.2_Data_Classification_[DATE]_APPROVED.xlsx`

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Python Developers, Excel Workbook Developers, Quality Assurance, ISMS Implementation Team

---

# Workbook Structure Overview

## Sheet List

**Total Sheets:** 11

| # | Sheet Name | Rows (approx) | Purpose | User Input |
|---|------------|---------------|---------|------------|
| 1 | Instructions_Legend | 45 | User guidance, metadata, legend | Metadata only (yellow cells) |
| 2 | Classification_Schema | 15 | Classification levels and definitions | Yes (classification details) |
| 3 | Sensitive_Data_Inventory | 25 | Sensitive data catalog | Yes (data categories) |
| 4 | Data_Location_Mapping | 25 | Data location and flow mapping | Yes (location details) |
| 5 | Data_Owner_Assignment | 20 | Data ownership accountability | Yes (owner assignments) |
| 6 | Regulatory_Mapping | 25 | Regulatory requirements mapping | Yes (regulatory alignment) |
| 7 | Labeling_Methods | 20 | Data labeling implementation status | Yes (labeling metrics) |
| 8 | Discovery_Results | 30 | Data discovery scan results | Yes (discovery findings) |
| 9 | Gap_Analysis | 40 | Gaps and remediation plans | Yes (gap details) |
| 10 | Evidence_Register | 100 | Evidence tracking | Yes (evidence entries) |
| 11 | Summary_Dashboard | 30 | KPIs, compliance metrics | No (automated formulas) |

**Total Assessment Items:** ~75 data classification checkpoints

---

# Detailed Sheet Specifications

## Sheet: Instructions_Legend

**Purpose:** User guidance, assessment metadata, response value legend

**Layout:**

- Rows 1-5: Document header (workbook title, ID, version)
- Rows 7-12: Organization metadata (yellow input cells)
- Rows 14-25: How to use this workbook (instructions)
- Rows 27-35: Legend - Response values
- Rows 37-45: Color coding guide


**Organization Metadata Fields:**

| Row | Field | Type | Example |
|-----|-------|------|---------|
| 7 | Assessment Date | Date | 21.01.2026 |
| 8 | Completed By | Text | John Smith |
| 9 | Role | Text | Data Classification Officer |
| 10 | Organization Name | Text | [Organization] |
| 11 | Review Cycle | Text | Quarterly |
| 12 | Next Review Date | Date | 21.04.2026 |

**Cell Formatting:**

- Organization metadata (B7:B12): Yellow fill, unlocked for user input
- All other cells: Locked, gray or white fill


**No Data Validation:** Informational sheet only

---

## Sheet: Classification_Scheme

**Purpose:** Document data classification scheme levels and governance

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Classification Level | Text | 18 | None | User input (e.g., "Restricted") |
| B | Definition | Text (wrap) | 40 | None | Brief description |
| C | Data Examples | Text (wrap) | 35 | None | Specific examples |
| D | Handling Requirements | Text (wrap) | 35 | None | Security controls |
| E | DLP Protection Requirement | Text | 20 | None | From ISMS-POL-A.8.12 |
| F | Data Owner Assigned | Dropdown | 15 | Yes/No/N/A | Yes if named owner |
| G | Owner Name/Role | Text | 25 | None | Specific person/role |
| H | User Training Completed | Text | 22 | None | E.g., "85% completion" |
| I | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance status |
| J | Evidence ID | Text | 15 | None | E.g., A812-2-CLS-001 |

**Pre-Populated Examples (Gray rows 6-9):**

| Level | Definition | Examples |
|-------|------------|----------|
| Restricted | Severe impact if leaked | Credit card numbers, medical records, trade secrets |
| Confidential | Significant business harm | Customer contracts, pricing, financial reports |
| Internal | Organization-only | Policies, procedures, internal communications |
| Public | Can be publicly disclosed | Marketing materials, public website content |

**Data Rows:** 15 total (4 examples + 11 blank)

**Data Validation:**

```python
# Column F: Data Owner Assigned
validation_owner = {
    'type': 'list',
    'formula1': '"Yes,No,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column I: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}
```

**Conditional Formatting:**

| Column | Condition | Format |
|--------|-----------|--------|
| I (Status) | ="✅ Compliant" | Green fill (RGB: 198, 239, 206) |
| I (Status) | ="⚠️ Partial" | Yellow fill (RGB: 255, 235, 156) |
| I (Status) | ="❌ Non-Compliant" | Red fill (RGB: 255, 199, 206) |

---

## Sheet: Sensitive_Data_Inventory

**Purpose:** Catalog all sensitive data types requiring DLP protection

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Data Category | Dropdown | 25 | Pre-defined list | PII, Financial, IP, etc. |
| B | Data Examples | Text (wrap) | 35 | None | Specific data elements |
| C | Systems/Locations | Text (wrap) | 30 | None | Where data resides |
| D | Classification Level | Dropdown | 18 | From sheet 2 | Restricted/Confidential/etc. |
| E | Volume (approx) | Text | 18 | None | "100K records", "50TB" |
| F | Regulatory Driver | Text | 25 | None | Swiss nDSG, GDPR, PCI DSS |
| G | DLP Coverage | Dropdown | 15 | Yes/No/Partial/N/A | Is DLP protecting? |
| H | Data Discovery Method | Dropdown | 22 | Pre-defined list | How identified |
| I | Data Owner | Text | 25 | None | Business owner |
| J | Last Reviewed Date | Date | 18 | None | DD.MM.YYYY |
| K | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance status |
| L | Evidence ID | Text | 15 | None | A812-2-INV-001 |

**Pre-Populated Examples (Gray rows 6-12):**

| Category | Examples | Systems | Classification |
|----------|----------|---------|----------------|
| Personal Data (PII) | SSN, passport, driver's license, email | HR database, SharePoint, Email | Restricted |
| Financial Data | Credit cards, bank accounts, payment data | Finance database, Payment gateway | Restricted |
| Healthcare Data | Medical records, health information | (If applicable) | Restricted |
| Authentication Credentials | Passwords, API keys, tokens, certificates | All systems | Restricted |
| Intellectual Property | Source code, designs, patents, trade secrets | Git repos, Engineering file shares | Confidential |
| Customer Data | Customer lists, contracts, pricing | Salesforce, CRM, Contract DB | Confidential |
| Employee Data | HR records, payroll, performance reviews | HR systems, Payroll | Confidential |

**Data Rows:** 25 total (7 examples + 18 blank)

**Data Validation:**

```python
# Column A: Data Category
validation_category = {
    'type': 'list',
    'formula1': '"Personal Data (PII),Financial Data,Healthcare Data,Authentication Credentials,Intellectual Property,Customer Data,Employee Data,Other"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column D: Classification Level
# Dynamic reference to Classification_Scheme sheet
validation_classification = {
    'type': 'list',
    'formula1': '=Classification_Scheme!$A$6:$A$15',  # Reference classification levels
    'allow_blank': False,
    'show_dropdown': True
}

# Column G: DLP Coverage
validation_coverage = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,Planned,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column H: Data Discovery Method
validation_discovery = {
    'type': 'list',
    'formula1': '"Automated Scan,Manual Inventory,Application Documentation,Data Owner Interview,None"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column K: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}
```

**Conditional Formatting:**

- Column K (Status): Same as Classification_Scheme (green/yellow/red)
- Column G (DLP Coverage):
  - "Yes" = Light green background
  - "No" = Light red background
  - "Partial" = Light yellow background


---

## Sheet: Detection_Methods

**Purpose:** Assess DLP detection method implementation and effectiveness

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Detection Method | Text | 25 | None | Pre-populated |
| B | Implementation Status | Dropdown | 20 | Deployed/Partial/Not Deployed | Current state |
| C | Capabilities | Text (wrap) | 35 | None | What it can do |
| D | Accuracy (%) | Number | 12 | 0-100 | If tested |
| E | False Positive Rate (%) | Number | 18 | 0-100 | FP / Total × 100 |
| F | False Negative Rate (%) | Number | 18 | 0-100 | FN / Total × 100 |
| G | Last Tested Date | Date | 18 | None | DD.MM.YYYY |
| H | Testing Methodology | Text (wrap) | 30 | None | How accuracy measured |
| I | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance status |
| J | Evidence ID | Text | 15 | None | A812-2-DET-001 |

**Pre-Populated Detection Methods (Rows 6-10):**

| Method | Description | Target Accuracy |
|--------|-------------|-----------------|
| Content Inspection | Pattern matching, regex, keyword detection | >90% |
| Document Labeling | Classification metadata embedded in files | >95% |
| Contextual Analysis | Source system, user role, destination | >85% |
| Machine Learning/AI | AI-based sensitive content detection | >90% |
| Fingerprinting | Hash-based document tracking | 100% (exact match) |

**Data Rows:** 20 total (5 pre-populated + 15 blank)

**Data Validation:**

```python
# Column B: Implementation Status
validation_implementation = {
    'type': 'list',
    'formula1': '"Fully Deployed,Partially Deployed,Not Deployed,Planned"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column D, E, F: Percentage validation
validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between'
}

# Column I: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}
```

**Conditional Formatting:**

- Column D (Accuracy):
  - ≥90% = Green
  - 75-89% = Yellow
  - <75% = Red
- Column E (False Positive Rate):
  - ≤10% = Green
  - 11-30% = Yellow
  - >30% = Red
- Column F (False Negative Rate):
  - ≤5% = Green
  - 6-15% = Yellow
  - >15% = Red


---

## Sheet: Classification_Enforcement

**Purpose:** Assess document labeling and automated classification implementation

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | System/Application | Text | 25 | None | SharePoint, Google Drive, etc. |
| B | Labeling Method | Dropdown | 22 | Manual/Automated/Hybrid | How labels applied |
| C | Labeling Coverage (%) | Number | 18 | 0-100 | % of docs with labels |
| D | Enforcement | Dropdown | 20 | Required/Optional/None | Label before save? |
| E | Auto-Classification Enabled | Dropdown | 22 | Yes/No/Partial | ML-based auto-classify |
| F | Auto-Classification Accuracy (%) | Number | 25 | 0-100 | If tested |
| G | User Override Allowed | Dropdown | 18 | Yes/No | Can users change label? |
| H | Integration with DLP | Dropdown | 18 | Yes/No/Partial | DLP reads labels |
| I | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance status |
| J | Evidence ID | Text | 15 | None | A812-2-ENF-001 |

**Pre-Populated Examples (Gray rows 6-9):**

| System | Method | Coverage | Enforcement |
|--------|--------|----------|-------------|
| SharePoint Online | Automated (Purview) | 85% | Required |
| Google Drive | Manual | 30% | Optional |
| Local File Shares | None | 0% | None |
| Email (M365) | Automated | 95% | Recommended |

**Data Rows:** 18 total (4 examples + 14 blank)

**Data Validation:**

```python
# Column B: Labeling Method
validation_method = {
    'type': 'list',
    'formula1': '"Manual,Automated,Hybrid,None"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column C, F: Percentage
validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between'
}

# Column D: Enforcement
validation_enforcement = {
    'type': 'list',
    'formula1': '"Required,Recommended,Optional,None"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column E, G, H: Yes/No/Partial
validation_yesnop = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column I: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}
```

**Conditional Formatting:**

- Column C (Labeling Coverage):
  - ≥80% = Green
  - 50-79% = Yellow
  - <50% = Red
- Column F (Auto-Classification Accuracy):
  - ≥85% = Green
  - 70-84% = Yellow
  - <70% = Red


---

## Sheet: Pattern_Library

**Purpose:** Document DLP patterns and their accuracy

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Pattern ID | Text | 15 | None | Unique identifier |
| B | Pattern Name | Text | 25 | None | Descriptive name |
| C | Data Type | Dropdown | 20 | Pre-defined list | What it detects |
| D | Pattern Definition | Text (wrap) | 40 | None | Regex or description |
| E | Detection Method | Dropdown | 20 | Regex/Keyword/ML/Fingerprint | How it works |
| F | Confidence Level | Dropdown | 18 | High/Medium/Low | Accuracy confidence |
| G | Accuracy (%) | Number | 12 | 0-100 | Tested accuracy |
| H | False Positive Rate (%) | Number | 18 | 0-100 | FP rate |
| I | Last Tested Date | Date | 18 | None | DD.MM.YYYY |
| J | Maintenance Owner | Text | 22 | None | Who maintains |
| K | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Pattern effectiveness |
| L | Evidence ID | Text | 15 | None | A812-2-PAT-001 |

**Pre-Populated Pattern Examples (Gray rows 6-15):**

| Pattern ID | Name | Data Type | Definition (simplified) |
|------------|------|-----------|-------------------------|
| PAT-001 | Credit Card (Luhn) | Financial | Regex with Luhn algorithm validation |
| PAT-002 | US SSN | PII | `\d{3}-\d{2}-\d{4}` or `\d{9}` |
| PAT-003 | IBAN | Financial | Country code + check digits + account |
| PAT-004 | Email Address | PII | Standard email regex |
| PAT-005 | API Key (AWS) | Credentials | `AKIA[0-9A-Z]{16}` |
| PAT-006 | Password Pattern | Credentials | Common password structures |
| PAT-007 | Swiss AHV Number | PII | `756.\d{4}.\d{4}.\d{2}` |
| PAT-008 | EU Passport | PII | Country-specific formats |
| PAT-009 | Medical Record Number | Healthcare | Site-specific format |
| PAT-010 | Source Code Fingerprint | IP | Hash of critical files |

**Data Rows:** 30 total (10 examples + 20 blank)

**Data Validation:**

```python
# Column C: Data Type
validation_datatype = {
    'type': 'list',
    'formula1': '"PII,Financial,Healthcare,Credentials,IP,Customer Data,Employee Data,Other"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column E: Detection Method
validation_detection = {
    'type': 'list',
    'formula1': '"Regex,Keyword,Machine Learning,Fingerprint,Hybrid"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column F: Confidence Level
validation_confidence = {
    'type': 'list',
    'formula1': '"High (>90%),Medium (75-90%),Low (<75%)"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column G, H: Percentage
validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between'
}

# Column K: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False,
    'show_dropdown': True
}
```

**Conditional Formatting:**

- Column G (Accuracy):
  - ≥90% = Green
  - 75-89% = Yellow
  - <75% = Red
- Column H (False Positive Rate):
  - ≤10% = Green
  - 11-30% = Yellow
  - >30% = Red
- Column F (Confidence Level):
  - "High" = Green
  - "Medium" = Yellow
  - "Low" = Red


---

## Sheet: Gap_Analysis

**Purpose:** Document identified gaps and remediation plans

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Gap ID | Text | 12 | Auto-generated: GAP-001 |
| B | Domain | Dropdown | 22 | Which assessment area |
| C | Gap Description | Text (wrap) | 40 | What's missing/inadequate |
| D | Current State | Text (wrap) | 25 | Current situation |
| E | Required State | Text (wrap) | 25 | What's needed |
| F | Risk Level | Dropdown | 15 | Critical/High/Medium/Low |
| G | Regulatory Impact | Text (wrap) | 25 | Which regulations affected |
| H | Remediation Action | Text (wrap) | 35 | What to do |
| I | Owner | Text | 20 | Who will fix |
| J | Target Date | Date | 15 | When to complete |
| K | Status | Dropdown | 15 | Open/In Progress/Resolved |
| L | Evidence ID | Text | 15 | A812-2-GAP-001 |

**Gap ID Auto-Generation:**
```python
# Formula in column A (starting row 6):
="GAP-"&TEXT(ROW()-5,"000")
# Results in: GAP-001, GAP-002, etc.
```

**Data Rows:** 40 (all blank, populated during assessment)

**Data Validation:**

```python
# Column B: Domain
validation_domain = {
    'type': 'list',
    'formula1': '"Classification Scheme,Sensitive Data Inventory,Detection Methods,Classification Enforcement,Pattern Library,General"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column F: Risk Level
validation_risk = {
    'type': 'list',
    'formula1': '"Critical,High,Medium,Low"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column K: Status
validation_status = {
    'type': 'list',
    'formula1': '"Open,In Progress,Resolved,Accepted (No Action)"',
    'allow_blank': False,
    'show_dropdown': True
}
```

**Conditional Formatting:**

- Column F (Risk Level):
  - "Critical" = Dark red fill
  - "High" = Red fill
  - "Medium" = Yellow fill
  - "Low" = Light yellow fill
- Column K (Status):
  - "Resolved" = Green fill
  - "In Progress" = Yellow fill
  - "Open" = Red fill
  - "Accepted" = Gray fill


---

## Sheet: Evidence_Register

**Purpose:** Track all evidence collected for audit

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Evidence ID | Text | 15 | Auto-generated: EV-001 |
| B | Domain | Dropdown | 20 | Which assessment area |
| C | Evidence Type | Dropdown | 20 | Screenshot/Doc/Test Result |
| D | Description | Text (wrap) | 45 | What evidence shows |
| E | File Name | Text | 35 | Actual filename |
| F | Collection Date | Date | 18 | DD.MM.YYYY |
| G | Collected By | Text | 20 | Person who collected |
| H | File Location | Text (wrap) | 40 | Path or URL |
| I | Sensitivity | Dropdown | 15 | Internal/Confidential |

**Evidence ID Auto-Generation:**
```python
# Formula in column A (starting row 6):
="EV-"&TEXT(ROW()-5,"000")
# Results in: EV-001, EV-002, etc.
```

**Pre-Populated Example (Gray row 6):**
| ID | Domain | Type | Description | File Name |
|----|--------|------|-------------|-----------|
| EV-001 | Classification Scheme | Policy Document | Data classification policy v2.0 with signatures | Classification-Policy-v2.0-Signed.pdf |

**Data Rows:** 100 total (1 example + 99 blank)

**Data Validation:**

```python
# Column B: Domain
validation_domain = {
    'type': 'list',
    'formula1': '"Classification Scheme,Sensitive Data Inventory,Detection Methods,Classification Enforcement,Pattern Library,Gap Analysis,General"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column C: Evidence Type
validation_type = {
    'type': 'list',
    'formula1': '"Screenshot,Configuration Export,Policy Document,Test Result,Data Discovery Report,Training Record,Audit Report,Other"',
    'allow_blank': False,
    'show_dropdown': True
}

# Column I: Sensitivity
validation_sensitivity = {
    'type': 'list',
    'formula1': '"Public,Internal,Confidential"',
    'allow_blank': False,
    'show_dropdown': True
}
```

---

## Sheet: Summary_Dashboard

**Purpose:** Executive summary with KPIs and compliance metrics

**Layout:**

**Rows 1-5: Header**

- Dashboard title, assessment date, organization


**Rows 7-15: Key Metrics (Large display)**

| Metric | Formula | Target |
|--------|---------|--------|
| Overall Compliance % | Weighted average of all domain compliance | ≥80% |
| Classification Scheme Maturity | Based on Classification_Scheme sheet | Level 2-3 |
| Sensitive Data Categories Inventoried | COUNT of categories in Sensitive_Data_Inventory | ≥7 |
| DLP Coverage % | Categories with DLP coverage / Total categories × 100 | 100% for Restricted/Confidential |
| Pattern Accuracy (avg) | AVERAGE of Pattern_Library accuracy column | ≥90% |
| False Positive Rate (avg) | AVERAGE of Detection_Methods FP rate | ≤10% |
| Critical Gaps | COUNT of Critical risk gaps in Gap_Analysis | 0 |
| High Gaps | COUNT of High risk gaps | ≤3 |

**Rows 17-25: Compliance by Domain**

| Domain | Compliance % | Status | Target |
|--------|--------------|--------|--------|
| Classification Scheme | Formula | ✅/⚠️/❌ | 100% |
| Sensitive Data Inventory | Formula | ✅/⚠️/❌ | 100% |
| Detection Methods | Formula | ✅/⚠️/❌ | ≥90% |
| Classification Enforcement | Formula | ✅/⚠️/❌ | ≥80% |
| Pattern Library | Formula | ✅/⚠️/❌ | ≥85% |

**Rows 27-35: Top 5 Critical Gaps (if any)**

- Dynamically pulled from Gap_Analysis sheet (filtered by "Critical" risk level)


**Key Formulas:**

```python
# Overall Compliance %
=ROUND(
  (COUNTIF(Classification_Scheme!I:I,"✅ Compliant") / COUNTA(Classification_Scheme!I6:I15) * 20) +
  (COUNTIF(Sensitive_Data_Inventory!K:K,"✅ Compliant") / COUNTA(Sensitive_Data_Inventory!K6:K25) * 25) +
  (COUNTIF(Detection_Methods!I:I,"✅ Compliant") / COUNTA(Detection_Methods!I6:I20) * 20) +
  (COUNTIF(Classification_Enforcement!I:I,"✅ Compliant") / COUNTA(Classification_Enforcement!I6:I18) * 15) +
  (COUNTIF(Pattern_Library!K:K,"✅ Compliant") / COUNTA(Pattern_Library!K6:K30) * 20),
  0
)

# Sensitive Data Categories Inventoried
=COUNTA(Sensitive_Data_Inventory!A6:A25) - COUNTBLANK(Sensitive_Data_Inventory!A6:A25)

# DLP Coverage %
=ROUND(
  COUNTIF(Sensitive_Data_Inventory!G6:G25,"Yes") / 
  COUNTA(Sensitive_Data_Inventory!G6:G25) * 100,
  0
)

# Pattern Accuracy (average)
=ROUND(AVERAGE(Pattern_Library!G6:G30), 0)

# False Positive Rate (average)
=ROUND(AVERAGE(Detection_Methods!E6:E20), 1)

# Critical Gaps
=COUNTIF(Gap_Analysis!F6:F45,"Critical")

# High Gaps
=COUNTIF(Gap_Analysis!F6:F45,"High")
```

**Conditional Formatting:**

- Overall Compliance %:
  - ≥90% = Dark green
  - 80-89% = Light green
  - 70-79% = Yellow
  - <70% = Red
- Critical Gaps:
  - 0 = Green
  - 1-2 = Yellow
  - ≥3 = Red


---

# Data Validation Rules (Consolidated)

**Standard Dropdown Values:**

```python
# Status (used in multiple sheets)
STATUS_VALUES = "✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"

# Yes/No/Partial
YES_NO_PARTIAL = "Yes,No,Partial,Planned,N/A"

# Risk Level
RISK_LEVEL = "Critical,High,Medium,Low"

# Data Categories
DATA_CATEGORIES = "Personal Data (PII),Financial Data,Healthcare Data,Authentication Credentials,Intellectual Property,Customer Data,Employee Data,Other"

# Detection Methods
DETECTION_METHODS = "Regex,Keyword,Machine Learning,Fingerprint,Hybrid"

# Implementation Status
IMPLEMENTATION_STATUS = "Fully Deployed,Partially Deployed,Not Deployed,Planned"
```

**Percentage Validation (0-100):**
```python
validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between',
    'error_title': 'Invalid Percentage',
    'error_message': 'Please enter a value between 0 and 100'
}
```

**Date Validation (DD.MM.YYYY):**
```python
validation_date = {
    'type': 'date',
    'formula1': '01.01.2020',  # Reasonable past date
    'formula2': '31.12.2030',  # Reasonable future date
    'allow_blank': True,
    'operator': 'between',
    'error_title': 'Invalid Date',
    'error_message': 'Please enter a valid date in DD.MM.YYYY format'
}
```

---

# Conditional Formatting Rules

**Standard Status Formatting:**
```python
status_formatting = {
    '✅ Compliant': {'fill': 'C6EFCE', 'font': '006100'},      # Green
    '⚠️ Partial': {'fill': 'FFEB9C', 'font': '9C6500'},        # Yellow
    '❌ Non-Compliant': {'fill': 'FFC7CE', 'font': '9C0006'},  # Red
    'N/A': {'fill': 'F2F2F2', 'font': '808080'}                # Gray
}
```

**Percentage Thresholds (Accuracy/Coverage):**
```python
# Green: ≥90%, Yellow: 75-89%, Red: <75%
accuracy_high_threshold = {
    'green': ('>=', 90),
    'yellow': ('and', [('>=', 75), ('<', 90)]),
    'red': ('<', 75)
}

# Green: ≥80%, Yellow: 50-79%, Red: <50%
coverage_threshold = {
    'green': ('>=', 80),
    'yellow': ('and', [('>=', 50), ('<', 80)]),
    'red': ('<', 50)
}

# False Positive Rate (Green: ≤10%, Yellow: 11-30%, Red: >30%)
fp_threshold = {
    'green': ('<=', 10),
    'yellow': ('and', [('>', 10), ('<=', 30)]),
    'red': ('>', 30)
}
```

**Risk Level Formatting:**
```python
risk_formatting = {
    'Critical': {'fill': '8B0000', 'font': 'FFFFFF'},  # Dark red, white text
    'High': {'fill': 'FF0000', 'font': 'FFFFFF'},      # Red, white text
    'Medium': {'fill': 'FFEB9C', 'font': '9C6500'},    # Yellow
    'Low': {'fill': 'FFF2CC', 'font': '9C6500'}        # Light yellow
}
```

---

# Cell Protection

**Protected Cells (Formula/Static):**

- All column headers (row 5 in each sheet)
- All formulas (Summary_Dashboard, auto-generated IDs)
- Instructions and legend text
- Pre-populated examples (gray rows)
- Summary_Dashboard calculations


**Unprotected Cells (User Input):**

- All yellow-highlighted fields (organization metadata)
- Data entry rows in assessment sheets (white cells)
- Status dropdown columns
- Additional Details / Comments fields
- Evidence Register descriptions
- Gap Analysis fields


**Sheet Protection Password:**

- Use organization-specific password
- Allow: Format cells, Insert rows, Sort, Filter
- Disallow: Delete rows, Modify formulas, Unprotect sheet


---

# Summary Dashboard Formulas (Detailed)

**Compliance Percentage Calculation (Weighted Average):**

Each domain has a weight based on importance:

- Classification Scheme: 20% (foundation)
- Sensitive Data Inventory: 25% (scope definition)
- Detection Methods: 20% (technical capability)
- Classification Enforcement: 15% (operational)
- Pattern Library: 20% (accuracy)


```python
overall_compliance = (
    (classification_scheme_compliance * 0.20) +
    (data_inventory_compliance * 0.25) +
    (detection_methods_compliance * 0.20) +
    (classification_enforcement_compliance * 0.15) +
    (pattern_library_compliance * 0.20)
)

# Where each domain_compliance =
# COUNTIF(domain_sheet!status_column, "✅ Compliant") / COUNTA(domain_sheet!status_column)
```

**Pattern Accuracy Average:**
```python
=IFERROR(
  ROUND(AVERAGE(Pattern_Library!G6:G30), 0),
  "N/A"
)
```

**DLP Coverage Percentage:**
```python
=IFERROR(
  ROUND(
    COUNTIF(Sensitive_Data_Inventory!G6:G25,"Yes") / 
    (COUNTA(Sensitive_Data_Inventory!G6:G25) - COUNTIF(Sensitive_Data_Inventory!G6:G25,"N/A")) * 100,
    0
  ),
  0
)
```

**Critical Gaps with Conditional Display:**
```python
=IF(COUNTIF(Gap_Analysis!F6:F45,"Critical")=0,
  "✅ No Critical Gaps",
  CONCATENATE("❌ ", COUNTIF(Gap_Analysis!F6:F45,"Critical"), " Critical Gaps - See Gap Analysis")
)
```

---

# Evidence Register Auto-Numbering

**Evidence ID Format:**
```python
# Column A formula (starting row 6):
=IF(ISBLANK(B6), "", "EV-"&TEXT(ROW()-5,"000"))

# Results in:
# EV-001, EV-002, EV-003, etc.
# Only generates ID if Domain column (B) is populated
```

**Date Auto-Fill for Collection Date:**
```python
# Column F formula (if collection date not manually entered):
=IF(AND(NOT(ISBLANK(B6)), ISBLANK(F6)), TODAY(), F6)

# Auto-fills today's date when evidence row created
# User can override with manual date entry
```

---

# APPENDIX: Technical Notes for Python Developers

## A.1 Python Script Integration Points

**Script Name:** `generate_a812_2_data_classification_assessment.py`

**Key Functions:**

```python
def create_workbook():
    """Initialize workbook with 9 sheets"""
    wb = Workbook()
    # Create sheets in order
    sheets = [
        'Instructions_Legend',
        'Classification_Scheme',
        'Sensitive_Data_Inventory',
        'Detection_Methods',
        'Classification_Enforcement',
        'Pattern_Library',
        'Gap_Analysis',
        'Evidence_Register',
        'Summary_Dashboard'
    ]
    return wb

def setup_styles():
    """Define reusable cell styles"""
    styles = {
        'header': {
            'font': Font(bold=True, size=11, color='FFFFFF'),
            'fill': PatternFill(start_color='366092', end_color='366092', fill_type='solid'),
            'alignment': Alignment(horizontal='center', vertical='center', wrap_text=True),
            'border': Border(...)
        },
        'yellow_input': {
            'fill': PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid'),
            'border': Border(...)
        },
        'gray_example': {
            'fill': PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid'),
            'font': Font(italic=True, color='808080')
        }
    }
    return styles

def apply_data_validation(sheet, cell_range, validation_type, formula):
    """Apply dropdown or range validation"""
    dv = DataValidation(...)
    sheet.add_data_validation(dv)
    dv.add(cell_range)

def apply_conditional_formatting(sheet, cell_range, rules):
    """Apply color coding based on values"""
    for rule in rules:
        sheet.conditional_formatting.add(cell_range, rule)

def create_summary_dashboard(wb):
    """Generate Summary_Dashboard with formulas"""
    # Implement weighted compliance calculation
    # Add KPI formulas
    # Link to other sheets
```

## A.2 Customization Guidelines

**For Each Implementation:**

1. **Review Pre-Populated Examples:**

   - Classification levels may differ (adjust Classification_Scheme examples)
   - Sensitive data categories may vary (add organization-specific categories)
   - Pattern library will be unique (replace examples with actual patterns)


2. **Adjust Validation Lists:**

   - Data categories: Add organization-specific categories
   - Systems/Applications: Replace generic examples with actual systems
   - Detection methods: Add any custom detection methods


3. **Tune Thresholds:**

   - Accuracy thresholds (90%, 75%) may need adjustment based on organization maturity
   - False positive targets (<10%) may be aspirational for immature programs
   - Coverage targets (80%, 100%) should align with policy requirements


4. **Customize Formulas:**

   - Weighted compliance calculation may need different weights
   - Summary dashboard KPIs may need additions/removals based on stakeholder needs


## A.3 Quality Assurance

**Validation Script:** `excel_sanity_check_a812_2.py`

```python
def validate_workbook(workbook_path):
    """Comprehensive workbook validation"""
    checks = [
        check_sheet_existence(),
        check_column_headers(),
        check_data_validation(),
        check_conditional_formatting(),
        check_formulas(),
        check_protection(),
        check_examples()
    ]
    return all(checks)

def check_formulas():
    """Verify all formulas calculate correctly"""
    # Open workbook
    # Trigger calculation
    # Check for #REF, #DIV/0, #VALUE errors
    # Verify formula logic matches specification
```

**Testing Checklist:**

- [ ] All 9 sheets created
- [ ] Column headers match specification
- [ ] Data validation dropdowns functional
- [ ] Conditional formatting rules applied
- [ ] Summary Dashboard formulas calculate correctly
- [ ] Evidence Register auto-numbering works
- [ ] Gap Analysis auto-numbering works
- [ ] Sheet protection enabled correctly
- [ ] No #REF or #VALUE errors
- [ ] File saves and reopens without errors


## A.4 Deployment Instructions

**Step 1: Generate Workbook**
```bash
python3 generate_a812_2_data_classification_assessment.py
```

**Expected Output:**
```
ISMS-IMP-A.8.12.2_Data_Classification_Assessment_YYYYMMDD.xlsx
```

**Step 2: Validate Workbook**
```bash
python3 excel_sanity_check_a812_2.py ISMS-IMP-A.8.12.2_Data_Classification_Assessment_20260121.xlsx
```

**Step 3: Manual QA**

- Open workbook in Excel/LibreOffice
- Verify dropdowns work (click, select value)
- Test formulas (enter sample data, verify calculations)
- Check conditional formatting (enter values triggering different colors)
- Verify sheet protection (try to modify locked cells - should fail)


**Step 4: Distribute to Assessment Team**

- Provide workbook + PART I User Completion Guide
- Conduct brief training session (30 min)
- Set completion deadline (typically 2-4 weeks)


**Step 5: Collect Completed Assessments**

- Review for completeness (no blank mandatory fields)
- Validate evidence exists (files referenced in Evidence Register)
- Approve or request corrections


---

**END OF PART II: TECHNICAL SPECIFICATION**

---

**Document Assembly:**

To create complete ISMS-IMP-A.8.12.2 specification:

1. **PART I:** User Completion Guide (separate file)
2. **PART II:** Technical Specification (this file)

**Python Script:** `generate_a812_2_data_classification_assessment.py`  
**Validation Script:** `excel_sanity_check_a812_2.py`  
**Output:** `ISMS-IMP-A.8.12.2_Data_Classification_Assessment_YYYYMMDD.xlsx`

**Dependencies:**

- openpyxl library (`pip install openpyxl`)
- Python 3.7+


---

**Status:** Technical Specification Complete  
**Next Action:** Implement Python workbook generator per specification  

---

**END OF SPECIFICATION**

---

*"The important thing is not to stop questioning. Curiosity has its own reason for existing."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-01-31 -->
