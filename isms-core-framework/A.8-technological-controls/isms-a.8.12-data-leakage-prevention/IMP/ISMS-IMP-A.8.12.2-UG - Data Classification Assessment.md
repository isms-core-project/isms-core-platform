<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.12.2-UG:framework:UG:a.8.12.2 -->
**ISMS-IMP-A.8.12.2-UG - Data Classification Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Data Classification Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.12.2-UG |
| **Related Policy** | ISMS-POL-A.8.12 (Data Leakage Prevention) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.12 (Data Leakage Prevention) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.8.12 (Data Leakage Prevention)
- ISMS-IMP-A.8.12.1 (DLP Infrastructure Assessment)
- ISMS-IMP-A.8.12.3 (Channel Coverage Assessment)
- ISMS-IMP-A.8.12.4 (Monitoring & Response Assessment)

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Classification Schema | Define and document data classification schema |
| 3 | Sensitive Data Inventory | Catalogue sensitive data assets requiring DLP protection |
| 4 | Data Location Mapping | Map sensitive data to storage and processing locations |
| 5 | Data Owner Assignment | Assign ownership and accountability for sensitive data |
| 6 | Regulatory Mapping | Map data assets to applicable regulatory requirements |
| 7 | Labelling Methods | Assess data labelling and tagging methods |
| 8 | Discovery Results | Record automated sensitive data discovery results |
| 9 | Gap Analysis | Identify classification and coverage gaps |
| 10 | Evidence Register | Store and reference evidence supporting assessments |
| 11 | Summary Dashboard | Compliance status and key metrics overview |
| 12 | Approval Sign-Off | Management review sign-off and certification |

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organisation]'s **data classification scheme and DLP detection capabilities** to ensure compliance with ISO/IEC 27001:2022 Control A.8.12 and applicable regulatory requirements.

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
- **Industry Standards:** PCI DSS v4.0.1 (Req. 3), HIPAA (§164.308), SOC 2 all require data discovery and classification

**Business Impact:**

- **Ineffective DLP:** Without classification, DLP either blocks everything (false positives → business disruption) or nothing (false negatives → data breaches)
- **Compliance Violations:** Regulators require demonstrating you know what data you have and where it is
- **Incident Response:** Data breach notification obligations depend on knowing what data was leaked
- **Risk Prioritization:** Can't assess data leakage risk without knowing data sensitivity

**Why Classification Assessment Matters:**

- **Accuracy Verification:** Are DLP patterns actually detecting the data they should?
- **Coverage Validation:** Have we identified ALL sensitive data types in the organisation?
- **Governance Check:** Do data owners understand their classification responsibilities?
- **False Positive Management:** Are classification rules too broad (everything flagged) or too narrow (nothing detected)?

## Who Should Complete This Assessment

**Primary Responsibility:** Data Classification Officer (if role exists), DLP Administrators, Information Security Officers

**Required Knowledge:**

- [Organisation]'s data classification policy and scheme (Public/Internal/Confidential/Restricted)
- Sensitive data types processed by [Organisation] (PII, financial, healthcare, IP, etc.)
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

**Pro Tip:** For organisations without formal data classification program, this assessment will take longer (8-10 hours) as you'll need to conduct discovery of sensitive data types during the assessment itself.

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

## Critical: Data Classification Maturity Model

**⚠️ IMPORTANT - Classification Maturity Determines DLP Effectiveness:**

Organisations fall into different data classification maturity levels. DLP effectiveness directly correlates with classification maturity.

**Maturity Levels:**

| Level | Characteristics | DLP Impact | Action Required |
|-------|----------------|------------|-----------------|
| **Level 0: Ad-Hoc** | No classification scheme, data discovery incomplete | DLP ineffective (too many false positives or false negatives) | **Establish classification scheme FIRST before deploying DLP** |
| **Level 1: Defined** | Classification scheme exists, manual labeling only | DLP partially effective (relies on users to label correctly) | Implement automated classification, regular audits |
| **Level 2: Managed** | Automated classification in key systems, pattern library maintained | DLP effective for structured data | Extend to unstructured data, tune patterns |
| **Level 3: Optimized** | ML-based classification, continuous pattern accuracy monitoring | DLP highly effective | Focus on edge cases, advanced threats |

**What This Means for Assessment:**

- **Level 0-1 organisations:** Will identify significant gaps in this assessment (expected, not a failure)
- **Level 2-3 organisations:** Assessment focuses on optimization and edge case detection
- **Honest assessment critical:** Don't inflate maturity level to "look good" - audit will expose gaps

**Common Issue:** Organisations implement DLP before establishing data classification. Result = DLP deployed but doesn't know what to protect = waste of money and creates false sense of security.

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

- [Organisation]'s data classification scheme (classification levels and definitions)
- Regulatory data protection requirements applicable to [Organisation]
- What constitutes PII, financial data, IP, credentials in [Organisation]'s context
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
3. Complete Organisation Metadata (yellow cells)

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
2. List all sensitive data categories processed by [Organisation]:

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
   - Check regulatory drivers (Swiss nDSG, GDPR, PCI DSS v4.0.1, etc.)

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

**Assessment Question:** *"Does your organisation have a formal data classification scheme with defined levels, handling requirements, and data owner accountability?"*

**How to Answer:**

- **"Yes":** If formal classification scheme exists, documented in policy, with defined levels (typically 3-4 levels: Public, Internal, Confidential, Restricted)
- **"Partial":** If classification scheme exists but incomplete (e.g., definitions unclear, no data ownership, not enforced)
- **"No":** If no formal classification scheme
- **"N/A":** Not applicable (rare - even smallest organisations need basic classification)

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
    - **Internal:** Organisation-only, no external sharing  
    - **Confidential:** Limited distribution, business impact if leaked  
    - **Restricted:** Highest sensitivity, severe impact if leaked, legal/regulatory constraints  

- [ ] **Clear definitions and data examples for each level**  

  *Problem if missing:* Users don't know how to classify data → inconsistent classification → DLP ineffective  
  *Quality check:* Show policy to random employee, ask "Is customer email addresses Confidential or Internal?" - can they answer correctly?  
  *Example definition (Confidential):* "Data that would cause significant financial, legal, or reputational harm to [Organisation] if disclosed to unauthorised parties. Examples: customer contracts, pricing information, non-public financial data, employee personal information."  

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

**Assessment Question:** *"Has your organisation identified and inventoried all sensitive data types requiring DLP protection?"*

**How to Answer:**

- **"Yes":** If comprehensive sensitive data inventory exists, covering all data categories listed in policy
- **"Partial":** If inventory exists but incomplete (some data types not inventoried, or inventory not maintained)
- **"No":** If no systematic data inventory, relying on ad-hoc knowledge
- **"N/A":** Not applicable (extremely rare - all organisations process some sensitive data)

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
| **Regulatory Driver** | Why sensitive | "Swiss nDSG Art. 5", "GDPR Art. 4", "PCI DSS v4.0.1 Req. 3" | Legal assessment, DPO input |
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

- Specific data category not applicable to organisation (e.g., healthcare data for non-healthcare organisation)

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

  *Why important:* Determines DLP requirements (GDPR has different requirements than PCI DSS v4.0.1)  
  *Common drivers:*  

    - Swiss nDSG Art. 5, 6 (personal data)  
    - EU GDPR Art. 4, 5, 32 (personal data)  
    - PCI DSS v4.0.1 Req. 3, 4 (payment card data)  
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

  *Frequency:* Annually minimum, quarterly for high-risk organisations  

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
**Statistics:** 80% of organisational data is unstructured, 90% of sensitive data breaches involve unstructured data  
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
- Inconsistent classification across organisation
- DLP rules complex, error-prone

**Solution:**
1. **Simplify to 3-4 levels maximum:**

   - **Public:** Can be publicly disclosed
   - **Internal:** Organisation-only, no external sharing (combine "Internal" and "Internal Only")
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

**END OF USER GUIDE**

---

*"What you do not classify, you cannot protect."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
