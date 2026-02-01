**ISMS-IMP-A.8.11.1 - Data Inventory & Classification Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.11: Data Masking

# PART I: USER COMPLETION GUIDE

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.11.1 |
| **Version** | 1.0 |
| **Assessment Area** | Sensitive Data Inventory & Classification |
| **Related Policy** | ISMS-POL-A.8.11, Section 2.1 (Data Classification and Identification) |
| **Purpose** | Assess organization's ability to identify, inventory, classify, and assign ownership to sensitive data requiring masking controls |
| **Target Audience** | Data Governance Teams, Data Protection Officers, Database Administrators, Application Owners, Compliance Officers, Auditors |
| **Assessment Type** | Data Discovery & Classification |
| **Review Cycle** | Quarterly (Inventory Updates) / Annual (Classification Review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial workbook layout specification only | ISMS Implementation Team |


---

# PART I: USER COMPLETION GUIDE
**Audience:** Data Governance Leads, Data Protection Officers, Database Administrators, Application Owners, Compliance Officers

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organization]'s **ability to identify, inventory, classify, and govern sensitive data** as the foundational prerequisite for implementing effective data masking controls under ISO/IEC 27001:2022 Control A.8.11.

**Core Principle:** *"You cannot mask what you do not know exists."*

**Scope:** Complete organizational data landscape including:
1. System Inventory (all databases, applications, file shares, SaaS platforms)
2. Data Category Taxonomy (10 sensitive data categories from PII to biometrics)
3. Sensitive Data Element Identification (table/field/column level)
4. Data Classification (Critical/High/Medium/Low sensitivity levels)
5. Data Ownership Assignment (who is accountable for each data category)
6. Regulatory Mapping (GDPR, FADP, HIPAA, PCI-DSS applicability)
7. Masking Priority Matrix (P1-P4 prioritization based on risk)
8. Gap Analysis (systems not inventoried, data not classified, ownership unassigned)

**Assessment Output:** Excel workbook with ~200-500 data points documenting comprehensive data inventory, classification decisions, ownership assignments, and masking priorities.

**Data-Centric Approach:** This assessment is **vendor-agnostic** and focuses on WHAT data exists, WHERE it resides, and WHO owns it — independent of specific masking tools or technologies.

## Why This Matters

**ISO 27001:2022 Control A.8.11 Requirement:**
> *"Data masking should be used in accordance with the organization's topic-specific policy on access control and other related topic-specific policies, and business requirements, taking applicable legislation into consideration."*

**The Foundational Problem:**
Data masking controls are meaningless without knowing:

- **WHAT** sensitive data exists in your environment
- **WHERE** this data is located (production, non-production, backups)
- **WHO** is accountable for protecting each data category
- **HOW SENSITIVE** the data is (drives masking requirements)
- **WHICH REGULATIONS** apply to each data category


**Regulatory Context:**

- **Swiss nFADP (Art. 6):** Requires data controllers to maintain processing inventories
- **EU GDPR (Art. 30):** Mandates records of processing activities (ROPA)
- **EU GDPR (Art. 32):** Data pseudonymization requirements depend on knowing what data exists
- **PCI-DSS v4.0 (Req. 3.3):** Primary Account Numbers (PAN) must be inventoried before masking
- **HIPAA (§164.514):** De-identification requires knowing which data elements constitute Protected Health Information (PHI)


**Business Impact:**

- **Data Breach Exposure:** Unknown sensitive data = unprotected data = regulatory fines
- **Audit Failures:** "How do you know you've masked everything?" → Need comprehensive inventory
- **Regulatory Penalties:** GDPR fines up to 4% of global revenue for inadequate data governance
- **Operational Risk:** Accidental disclosure of unclassified sensitive data (common root cause)
- **Resource Waste:** Masking non-sensitive data wastes effort; missing sensitive data creates risk


## Who Should Complete This Assessment

**Primary Responsibility:** Data Governance Lead, Chief Data Officer (CDO), or Data Protection Officer (DPO)

**Required Knowledge:**

- [Organization]'s information systems architecture (databases, applications, data flows)
- Data protection regulatory requirements applicable to [Organization]
- Data classification schemes and sensitivity criteria
- Business data ownership structures


**Required Skills:**

- Data discovery and profiling techniques
- Database schema analysis
- Risk assessment and prioritization
- Stakeholder engagement (extracting ownership assignments)


**Support Roles:**

- **Database Administrators (DBAs):** Database schema access, record counts, retention policies
- **Application Owners:** Business context, data criticality, regulatory scope
- **Information Security Team:** Classification criteria, risk scoring, masking requirements
- **Legal/Compliance:** Regulatory applicability, data retention requirements, cross-border restrictions
- **Privacy Team:** Personal data identification, DPIA (Data Protection Impact Assessment) linkage
- **IT Asset Management:** CMDB data, system inventory, hosting locations


## Time Estimate

**Total Assessment Time:** 12-20 hours (depending on data estate complexity and existing documentation)

**Breakdown:**

- **Initial System Inventory:** 2-4 hours (if CMDB exists: 1 hour; if manual: 4+ hours)
- **Data Discovery Execution:** 4-8 hours (automated tools: 4 hours; manual: 8+ hours)
- **Classification Decisions:** 3-5 hours (requires SME input, data owner consultation)
- **Ownership Assignment:** 2-3 hours (stakeholder outreach, RACI confirmation)
- **Regulatory Mapping:** 1-2 hours (legal/compliance team consultation)
- **Gap Analysis & Prioritization:** 1-2 hours
- **Evidence Collection:** 1-2 hours
- **Quality Review:** 1-2 hours


**Pro Tip for Large Organizations (>100 systems):**

- **Phase 1 (Week 1):** Crown jewel systems only (top 10-20 most critical)
- **Phase 2 (Week 2-3):** High-risk systems (regulatory scope, customer data)
- **Phase 3 (Month 2):** Medium-risk systems
- **Phase 4 (Ongoing):** Tail of low-risk systems, continuous inventory maintenance


## Connection to Policy

This assessment implements **ISMS-POL-A.8.11, Section 2.1 (Data Classification and Identification)** which defines mandatory requirements for:

**REQ-CLS-001:** Maintain comprehensive inventory of sensitive data categories  
**REQ-CLS-002:** Classify all sensitive data using organizational classification scheme  
**REQ-CLS-003:** Document all sensitive data locations (system, database, table, column/field)  
**REQ-CLS-010:** Perform initial data discovery (automated or manual)  
**REQ-CLS-020:** Maintain living inventory (quarterly updates minimum)  
**REQ-CLS-030:** Assign Data Owner per data category  
**REQ-CLS-031:** Data Owner SHALL approve masking decisions  
**REQ-CLS-032:** Annual classification review for all sensitive data categories

**Policy Authority:** Chief Information Security Officer (CISO), Chief Data Officer (CDO), or Data Protection Officer (DPO)  
**Compliance Status:** Mandatory for all systems processing Internal, Confidential, or Restricted data

## Critical Success Factors

**Assessment Quality Indicators:**

✅ **Comprehensive Coverage:**

- ALL production systems included (no "shadow IT" missing)
- Non-production environments documented (dev, test, UAT, analytics)
- SaaS/cloud systems included (not just on-premises)
- Backup/archive/DR systems included
- Decommissioned systems tracked (retention compliance)


✅ **Granular Classification:**

- Table/field level classification (not just "database contains PII")
- Specific data categories identified (not vague "sensitive data")
- Sensitivity levels assigned with clear rationale
- Regulatory applicability documented per data element


✅ **Clear Ownership:**

- Every data category has assigned Data Owner (named individual or role)
- Data Owners have acknowledged accountability
- Escalation path defined for ownership disputes


✅ **Risk-Based Prioritization:**

- Masking priority (P1-P4) assigned based on objective criteria
- High-risk data flagged for immediate attention
- Resources allocated proportional to risk


✅ **Audit-Ready Evidence:**

- Data discovery methodology documented
- Classification decisions traceable to policy criteria
- Ownership assignments formally acknowledged
- Review dates and next actions clearly defined


---

# Prerequisites

## Access Required

Before starting this assessment, ensure you have access to:

**Infrastructure Documentation:**

- [ ] Configuration Management Database (CMDB) or IT asset inventory
- [ ] Network architecture diagrams (showing system interconnections)
- [ ] Data flow diagrams (if available)
- [ ] Application portfolio catalog
- [ ] Database inventory (list of all databases, production and non-production)
- [ ] SaaS/cloud service inventory


**System Access:**

- [ ] Database administration consoles (Oracle, SQL Server, PostgreSQL, MySQL, MongoDB, etc.)
- [ ] Application administration interfaces
- [ ] Cloud provider consoles (AWS, Azure, GCP, etc.) if applicable
- [ ] File share access (for unstructured data assessment)
- [ ] Backup system access (to verify what's in backups)


**Documentation Systems:**

- [ ] Data governance policy repository
- [ ] Existing data classification schemes (if any)
- [ ] Regulatory compliance assessments (GDPR ROPA, PCI-DSS scope, etc.)
- [ ] Data Protection Impact Assessments (DPIAs)
- [ ] Privacy policy documentation
- [ ] Data retention schedules


**Stakeholder Access:**

- [ ] Data Owner contact information (business stakeholders)
- [ ] Application Owner contact list
- [ ] Legal/Compliance team availability (regulatory questions)
- [ ] DBA/Technical team availability (schema access)


## Knowledge Required

**Essential Understanding:**

- [Organization]'s data classification scheme (if exists; if not, use ISO 27001 framework)
- Regulatory landscape applicable to [Organization] (GDPR, FADP, HIPAA, PCI-DSS, etc.)
- Business context for major applications (CRM, ERP, HR, finance, etc.)
- Data residency and cross-border restrictions


**Technical Skills:**

- Basic database concepts (tables, columns, schemas)
- Understanding of structured vs. unstructured data
- Data discovery methodologies (automated scanning, manual review)
- Risk assessment fundamentals (likelihood × impact)


**NOT Required (but helpful):**

- Deep SQL expertise (DBAs handle technical queries)
- Privacy law expertise (legal team advises on regulatory applicability)
- Data science/statistics (for assessing re-identification risk)


## Tools Needed

**Data Discovery Tools (Optional but Recommended):**

**Automated Data Discovery Solutions:**

- **Commercial:** BigID, OneTrust, Collibra, Informatica Data Governance, Varonis, etc.
- **Open Source:** Amundsen (Lyft), DataHub (LinkedIn), Apache Atlas
- **Database-Specific:** Oracle Data Masking & Subsetting, Microsoft Data Classification
- **Cloud-Native:** AWS Macie, Azure Purview, GCP Cloud DLP


**Manual Discovery Tools (if automated tools unavailable):**

- **Database query tools:** SQL Developer, DBeaver, pgAdmin, MySQL Workbench
- **GREP/search utilities:** For searching configuration files, application code for sensitive data patterns
- **Spreadsheet software:** Excel or LibreOffice Calc for manual inventory tracking
- **Documentation tools:** For recording findings, classification decisions


**Evidence Collection:**

- **Screenshot tool:** For capturing data discovery outputs, classification evidence
- **Export capability:** Database schema exports, data dictionaries
- **Secure storage:** Evidence repository (some evidence contains metadata about sensitive data)


**Critical Tool Selection Note:**
This assessment is **tool-agnostic**. [Organization] may use any data discovery methodology (automated, manual, hybrid). The IMPORTANT part is documenting WHAT you found, not HOW you found it.

## Pre-Assessment Checklist

**Before You Begin (Mandatory Steps):**

✅ **Stakeholder Alignment:**

- [ ] CISO/CDO/DPO has approved assessment scope
- [ ] Data Owner identification process agreed (who assigns ownership?)
- [ ] Classification criteria approved (using policy definitions)
- [ ] Assessment timeline communicated to affected teams


✅ **Technical Preparation:**

- [ ] Read-only database access provisioned (for discovery)
- [ ] Data discovery tool access configured (if using automated tools)
- [ ] Assessment workbook downloaded and unprotected (if using Excel template)
- [ ] Evidence repository created (folder structure for screenshots, exports)


✅ **Coordination:**

- [ ] DBAs notified (performance impact from discovery scans)
- [ ] Application Owners notified (may need business context input)
- [ ] Change freeze awareness (avoid running during critical business periods)
- [ ] Escalation path defined (for ownership disputes, classification disagreements)


---

# Assessment Workflow

## High-Level Process Flow

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1: SYSTEM INVENTORY (Complete "System_Inventory" sheet)  │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 2: DATA DISCOVERY (Identify sensitive data elements)      │
│          Complete "Sensitive_Data_Inventory" sheet              │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 3: CLASSIFICATION (Apply sensitivity levels)              │
│          Complete "Classification_Matrix" sheet                 │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 4: REGULATORY MAPPING (Apply compliance requirements)     │
│          Complete "Regulatory_Mapping" sheet                    │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 5: OWNERSHIP (Assign Data Owners)                        │
│          Complete "Data_Owner_Assignment" sheet                 │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 6: PRIORITIZATION (Determine masking priority)           │
│          Complete "Masking_Priority_Matrix" sheet               │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 7: GAP ANALYSIS (Identify missing coverage)              │
│          Complete "Gap_Analysis" sheet                          │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 8: EVIDENCE & APPROVAL (Document & Sign-Off)             │
│          Complete "Evidence_Register" + "Summary_Dashboard"     │
└─────────────────────────────────────────────────────────────────┘
```

## Phase 1: System Inventory (2-4 hours)

**Objective:** Document ALL systems that store, process, or transmit data.

**Sheet:** `System_Inventory`

**Step-by-Step:**

1. **Extract from CMDB (if exists):**

   - Export all application and database entries
   - Include: System ID, Name, Type, Environment, Owner
   - Filter out network devices, purely infrastructure components


2. **Supplement with Manual Discovery:**

   - Interview Application Owners: "What systems do you manage?"
   - Review cloud provider consoles (AWS RDS, Azure SQL, GCP Cloud SQL, etc.)
   - Check SaaS subscriptions (Salesforce, Workday, ServiceNow, etc.)
   - Identify file shares (SharePoint, NAS, S3 buckets)
   - Don't forget: Backup systems, data warehouses, analytics platforms, DR sites


3. **Document in Excel (Rows 8-57, 50 row template):**

   - **System ID:** Internal identifier (e.g., SYS-001, APP-CRM-PROD)
   - **System Name:** Human-readable name
   - **System Type:** Database / Application / SaaS / File Share / Data Warehouse / Backup / Other
   - **Environment:** Production / Development / Test/QA / UAT / Training / Analytics / DR/Backup / Decommissioned
   - **Contains Sensitive Data?:** Yes / No / Unknown (if Unknown, requires discovery)
   - **Hosting Location:** On-Premises / AWS / Azure / GCP / Multi-Cloud / Hybrid / Third-Party
   - **Primary Data Owner:** Business stakeholder accountable for data
   - **System Owner/Admin:** Technical admin responsible for system


4. **Quality Checks:**

   - [ ] All production systems included (cross-reference with monitoring tools)
   - [ ] All environments represented (not just production)
   - [ ] SaaS/cloud systems included (common gap: forgetting Salesforce, Office 365, etc.)
   - [ ] Decommissioned systems noted (for retention compliance tracking)
   - [ ] "Unknown" sensitive data status flagged for Phase 2 discovery


**Common Mistakes to Avoid:**

- ❌ Only inventorying production (dev/test environments often have real data!)
- ❌ Forgetting SaaS applications (they contain sensitive data too)
- ❌ Assuming "small" databases are non-sensitive (size ≠ sensitivity)
- ❌ Skipping decommissioned systems (they may still have retention obligations)


## Phase 2: Data Discovery (4-8 hours)

**Objective:** Identify sensitive data elements at table/column/field level.

**Sheet:** `Sensitive_Data_Inventory`

**Discovery Methodologies:**

**Option A: Automated Data Discovery (Recommended for >20 systems)**
1. Deploy data discovery tool (BigID, OneTrust, AWS Macie, etc.)
2. Configure scanning for sensitive data patterns:

   - Personal Identifiers (SSN, passport, national ID patterns)
   - Financial Data (credit card, IBAN, account number patterns)
   - Health Data (diagnosis codes, prescription patterns)
   - Contact Information (email, phone, physical address patterns)

3. Review discovery results
4. Validate false positives (common: "customer_name" field contains company names, not people)
5. Document findings in Excel

**Option B: Manual Discovery (Small environments <20 systems)**
1. Export database schemas (table/column metadata)
2. Review column names for sensitive data indicators:

   - Keywords: `ssn`, `social_security`, `passport`, `credit_card`, `password`, `email`, `phone`, `dob`, `address`, `salary`, `diagnosis`, etc.

3. Sample data review (with appropriate authorization):

   - `SELECT column_name, COUNT(DISTINCT column_name) FROM table LIMIT 100;`
   - Look for PII patterns in actual data

4. Document findings in Excel

**Option C: Hybrid (Recommended for most organizations)**

- Automated scanning for known patterns (PII, financial data)
- Manual review for business-specific sensitive data (proprietary, trade secrets)
- Application Owner interviews for context


**Step-by-Step in Excel (Rows 8-207, 200 row template):**

For EACH sensitive data element found:
1. **Data Element ID:** Unique identifier (e.g., DATA-001)
2. **System Reference:** Link to System_Inventory (System ID)
3. **Database/Container:** Database name or file share path
4. **Table/File Name:** Specific table or filename
5. **Column/Field Name:** Exact column/field identifier
6. **Data Category:** Select from taxonomy (CAT-PII-D, CAT-FIN, CAT-HLT, etc.) - see reference sheet
7. **Sample Data Pattern:** Example (REDACTED): `XXX-XX-1234` (SSN), `user@domain.com` (email)
8. **Record Count (Approx):** Number of records in table (for volume assessment)
9. **Discovery Method:** Automated Scan / Manual Schema Review / Application Owner Interview / Data Sampling
10. **Discovery Date:** When this element was identified
11. **Verified By:** Who confirmed this is actually sensitive data

**Quality Checks:**

- [ ] All "Yes" systems from Phase 1 have corresponding data elements documented
- [ ] Data categories use standardized taxonomy (not free-text descriptions)
- [ ] Sample patterns provided (helps validate classification)
- [ ] Discovery method documented (audit trail)
- [ ] False positives eliminated (e.g., "customer_type" is NOT PII)


**Common Mistakes to Avoid:**

- ❌ Table-level classification only ("Customers table contains PII") → Too vague, need column-level
- ❌ Missing indirect identifiers (DOB+ZIP can re-identify individuals)
- ❌ Assuming encrypted data doesn't need classification (encryption ≠ masking)
- ❌ Not validating column names ("`email_opt_in`" column may NOT contain email addresses)


## Phase 3: Classification (3-5 hours)

**Objective:** Assign sensitivity levels (Critical/High/Medium/Low) to each data element.

**Sheet:** `Classification_Matrix`

**Classification Criteria (from Policy ISMS-POL-A.8.11, Section 2.1 (Data Classification and Identification)):**

| Sensitivity Level | Definition | Masking Requirement | Examples |
|-------------------|------------|---------------------|----------|
| **Critical** | Severe harm if exposed, guaranteed regulatory breach, criminal liability | SHALL mask in ALL non-production environments | SSN/AHV, Passport, Credit Card (full PAN), Health diagnoses, Genetic data |
| **High** | Substantial personal/business harm, privacy violation, regulatory risk | SHALL mask in non-production environments | Email, Phone, DOB, Full Name, IBAN, Salary, Location data |
| **Medium** | Moderate harm, business impact, reputational risk | SHOULD mask in non-production environments | Job Title+Department (indirect PII), IP addresses, Device IDs |
| **Low** | Minimal harm, low privacy risk | MAY mask based on risk assessment | Generalized demographics (age range, region) |
| **Public** | No confidentiality requirement | No masking needed | Public information, anonymized aggregates |

**Decision Tree for Classification:**

```
START: Is this data element subject to specific regulation?
  │
  ├─ YES, PCI-DSS (credit card) ────────────► CRITICAL
  ├─ YES, HIPAA (PHI) ──────────────────────► CRITICAL
  ├─ YES, GDPR Art. 9 (special categories) ─► CRITICAL
  │
  └─ NO ──► Can this data element identify an individual ALONE?
            │
            ├─ YES (direct identifier) ──────► HIGH
            │
            └─ NO ──► Can this data + 1 other field identify individual?
                      │
                      ├─ YES (indirect identifier) ► MEDIUM
                      │
                      └─ NO ───────────────────────► LOW or PUBLIC
```

**Step-by-Step in Excel (Rows 8-207):**

For EACH data element from Phase 2:
1. **Data Element ID:** Copy from Sensitive_Data_Inventory
2. **Data Category:** Copy from Sensitive_Data_Inventory
3. **Sensitivity Level:** Apply decision tree above → Critical/High/Medium/Low
4. **Classification Rationale:** Why this level? (e.g., "GDPR Art. 9 special category", "Direct PII per policy", "Indirect identifier + DOB")
5. **Regulatory Driver:** Which regulation applies? (GDPR / FADP / HIPAA / PCI-DSS / None / Multiple)
6. **Re-Identification Risk:** Very High / High / Medium / Low / Negligible
7. **Exposure Risk:** Very High (public internet) / High (internal network) / Medium (restricted network) / Low (encrypted, access-controlled) / Very Low (air-gapped)
8. **Classification Date:** When sensitivity assigned
9. **Classified By:** Data Owner or DPO
10. **Next Review Date:** Annual review date (12 months from classification)

**Quality Checks:**

- [ ] All Critical/High data elements have clear regulatory justification
- [ ] Classification rationale is objective (not subjective "feels sensitive")
- [ ] Re-identification risk assessed (especially for indirect identifiers)
- [ ] Exposure risk considers current controls (encryption, access controls)
- [ ] Data Owner has reviewed and approved classification (documented in notes)


**Common Mistakes to Avoid:**

- ❌ Over-classifying everything as Critical (creates resource burden, boy-who-cried-wolf effect)
- ❌ Under-classifying to avoid masking work (audit finding, potential breach)
- ❌ Inconsistent classification (same data type classified differently across systems)
- ❌ Ignoring context ("`email`" in support ticket = Medium; "`email`" in HR system = High)


## Phase 4: Regulatory Mapping (1-2 hours)

**Objective:** Document which regulations apply to each data category.

**Sheet:** `Regulatory_Mapping`

**Applicable Regulations (adjust for [Organization] context):**

**Mandatory (if processing personal data in scope):**

- **GDPR (EU General Data Protection Regulation):** Personal data of EU residents
- **Swiss nFADP (Federal Act on Data Protection):** Personal data of Swiss residents
- **UK GDPR:** Personal data of UK residents (if applicable)


**Conditional (if industry/contract requires):**

- **HIPAA (Health Insurance Portability and Accountability Act):** US healthcare entities only
- **PCI-DSS (Payment Card Industry Data Security Standard):** Entities processing payment cards
- **GLBA (Gramm-Leach-Bliley Act):** US financial institutions only
- **CCPA/CPRA (California Consumer Privacy Act):** US companies with California residents' data
- **FISMA (Federal Information Security Management Act):** US federal agencies and contractors


**Step-by-Step in Excel (Rows 8-57, 50 row template):**

For EACH data category (not individual fields):
1. **Data Category:** CAT-PII-D, CAT-FIN, CAT-HLT, etc.
2. **Category Description:** Human-readable (e.g., "Direct PII", "Financial Data")
3. **GDPR Applicable?:** Yes / No / Conditional
4. **GDPR Article Reference:** Art. 6 (lawful basis), Art. 9 (special categories), Art. 32 (security)
5. **FADP Applicable?:** Yes / No / Conditional
6. **FADP Article Reference:** Art. 6 (principles), Art. 8 (security measures)
7. **Other Regulations:** PCI-DSS / HIPAA / CCPA / None / Multiple
8. **Masking Requirement Source:** Which regulation mandates masking? (GDPR Art. 32 pseudonymization, PCI-DSS Req. 3.3, etc.)
9. **Cross-Border Restrictions:** Any data residency requirements? (EU data must stay in EU, etc.)
10. **Retention Period:** Regulatory minimum/maximum retention
11. **Deletion Requirements:** Right to erasure (GDPR Art. 17), destruction timelines

**Quality Checks:**

- [ ] All GDPR "special categories" (Art. 9) flagged: health, biometric, genetic, racial, political, religious, trade union, sexual orientation
- [ ] PCI-DSS scope clearly defined (only cardholder data environments)
- [ ] HIPAA applicability confirmed with legal team (US-specific, not global)
- [ ] Retention periods align with legal requirements (not arbitrary)
- [ ] Cross-border restrictions documented (impacts cloud hosting, masking tool selection)


**Common Mistakes to Avoid:**

- ❌ Assuming HIPAA applies globally (it's US-only)
- ❌ Confusing "personal data" with "sensitive personal data" (GDPR Art. 9 special categories)
- ❌ Not consulting legal team (don't guess regulatory applicability)
- ❌ Ignoring data residency (GDPR doesn't prohibit cross-border transfer, but requires safeguards)


## Phase 5: Data Ownership Assignment (2-3 hours)

**Objective:** Assign named Data Owners accountable for each data category.

**Sheet:** `Data_Owner_Assignment`

**Data Owner Definition (from Policy):**
> *"The business role or individual accountable for data quality, appropriate use, access control, and compliance with data protection requirements for a specific data category or dataset."*

**NOT the same as:**

- System Owner (technical accountability for infrastructure)
- Database Administrator (executes technical controls)
- Data Steward (tactical data management)


**Data Owner Responsibilities:**

- Approve data classification decisions
- Approve masking technique selections
- Define access control requirements
- Approve exceptions to masking policy
- Review and approve data retention/deletion
- Accountable for regulatory compliance for their data category


**Step-by-Step in Excel (Rows 8-57, 50 row template):**

For EACH data category:
1. **Data Category:** CAT-PII-D, CAT-FIN, etc.
2. **Category Description:** Human-readable
3. **Data Owner (Role):** Business role (e.g., "VP of HR", "Chief Marketing Officer", "Head of Finance")
4. **Data Owner (Individual):** Named person currently in role
5. **Data Owner Contact:** Email or phone
6. **Backup Data Owner:** Who covers when primary unavailable?
7. **Date Assigned:** When ownership assigned
8. **Acknowledgment Status:** Acknowledged / Pending Acknowledgment / Declined
9. **Acknowledgment Date:** When Data Owner confirmed acceptance
10. **Approval Authority:** What decisions can this Data Owner make? (Classification / Masking Technique / Access Control / All)
11. **Escalation Path:** Who resolves disputes or ownership gaps?

**Stakeholder Outreach Process:**

1. **Identify Candidate Data Owners:**

   - CAT-PII-D (Direct PII) → Chief Privacy Officer, DPO, or VP Legal
   - CAT-FIN (Financial Data) → CFO, Finance Director, or Controller
   - CAT-HLT (Health Data) → Chief Medical Officer (if applicable)
   - CAT-CRD (Credentials) → CISO, Security Director
   - CAT-PRP (Proprietary) → CTO, VP Product, or Business Unit Leader


2. **Send Ownership Assignment Email:**
   ```
   Subject: Data Ownership Assignment - [Data Category]
   
   Dear [Candidate Data Owner],
   
   As part of our ISO 27001 compliance initiative, we are formalizing Data 
   Ownership for sensitive data categories requiring masking controls.
   
   You have been identified as the appropriate Data Owner for:

   - Data Category: [CAT-XXX] - [Description]
   - Scope: [List of systems/tables containing this data]
   - Regulatory Context: [GDPR / FADP / Other]
   

   Data Owner responsibilities include:

   - Approving data classification and masking decisions
   - Defining access control requirements
   - Ensuring regulatory compliance
   

   Please confirm your acceptance by [Date]. If you believe another role 
   should own this data, please advise.
   
   Thank you,
   [Your Name], Data Governance Lead
   ```

3. **Document Acknowledgment:**

   - Positive response → Update "Acknowledgment Status" to "Acknowledged"
   - Declined → Escalate to CISO/CDO for alternative assignment
   - No response after 1 week → Follow up, escalate after 2 weeks


**Quality Checks:**

- [ ] All data categories have assigned Data Owners (no orphaned data)
- [ ] Data Owners are business stakeholders (not IT/security roles unless appropriate)
- [ ] Acknowledgment obtained in writing (email confirmation acceptable)
- [ ] Backup Data Owners identified (no single point of failure)
- [ ] Escalation path defined (for ownership disputes)


**Common Mistakes to Avoid:**

- ❌ Assigning CISO/DPO as Data Owner for everything (they're policy enforcers, not business owners)
- ❌ Assigning DBAs as Data Owners (they're technical implementers, not business accountable)
- ❌ Not getting written acknowledgment (undocumented = didn't happen for audit)
- ❌ Vague role definitions ("IT Manager" → which IT Manager? Be specific)


## Phase 6: Masking Priority Matrix (1-2 hours)

**Objective:** Prioritize masking implementation based on risk scoring.

**Sheet:** `Masking_Priority_Matrix`

**Priority Scoring Algorithm (from Policy):**

```
Priority Score = (Sensitivity Level × 3) + (Exposure Risk × 2) + (Regulatory Weight × 2) + (Volume Score × 1)

Where:

- Sensitivity Level: Critical=4, High=3, Medium=2, Low=1
- Exposure Risk: Very High=4, High=3, Medium=2, Low=1, Very Low=0
- Regulatory Weight: Multiple regulations=4, GDPR Art. 9=4, GDPR/FADP=3, Industry-specific=2, None=0
- Volume Score: >10M records=4, 1M-10M=3, 100K-1M=2, 10K-100K=1, <10K=0


Priority Bands:

- P1 (Critical): Score ≥30 → Mask within 30 days
- P2 (High): Score 20-29 → Mask within 90 days
- P3 (Medium): Score 10-19 → Mask within 180 days
- P4 (Low): Score <10 → Mask within 365 days or risk-accept

```

**Step-by-Step in Excel (Rows 8-207):**

For EACH data element (or grouped by data category if hundreds of fields):
1. **Data Element ID:** From Sensitive_Data_Inventory
2. **System Reference:** System ID
3. **Data Category:** CAT-XXX
4. **Sensitivity Level:** Critical/High/Medium/Low
5. **Sensitivity Score:** 4/3/2/1 (auto-calculated based on level)
6. **Exposure Risk:** Very High/High/Medium/Low/Very Low
7. **Exposure Score:** 4/3/2/1/0 (auto-calculated)
8. **Regulatory Applicability:** Multiple/GDPR Art. 9/GDPR or FADP/Industry/None
9. **Regulatory Weight:** 4/4/3/2/0 (auto-calculated)
10. **Record Count:** Approximate volume
11. **Volume Score:** 4/3/2/1/0 (auto-calculated based on thresholds)
12. **Total Priority Score:** =SUM(Sensitivity Score×3, Exposure Score×2, Regulatory Weight×2, Volume Score×1)
13. **Priority Band:** P1/P2/P3/P4 (auto-assigned based on score)
14. **Target Masking Date:** P1=30 days, P2=90 days, P3=180 days, P4=365 days from assessment
15. **Current Masking Status:** Not Started / In Progress / Complete / Blocked / Risk Accepted

**Quality Checks:**

- [ ] All Critical sensitivity data elements are P1 or P2 (if P3/P4, justification required)
- [ ] P1 items have defined implementation owners and timelines
- [ ] Blocked items have documented blockers and mitigation plans
- [ ] Risk-accepted items have formal risk acceptance from Data Owner + CISO


**Common Mistakes to Avoid:**

- ❌ Treating all data equally (everything becomes P1 → nothing gets done)
- ❌ Ignoring volume (1 record of sensitive data vs. 10M records = very different risk)
- ❌ Not updating status (Priority Matrix becomes stale if not maintained)
- ❌ No accountability for P1 items (assign explicit owners with deadlines)


## Phase 7: Gap Analysis (1-2 hours)

**Objective:** Identify missing inventory, classification, or ownership.

**Sheet:** `Gap_Analysis`

**Gap Types to Identify:**

**1. Inventory Gaps:**

- Systems not inventoried (discovered post-assessment)
- "Unknown" sensitive data status not resolved
- Missing environments (e.g., only production inventoried, not dev/test)


**2. Classification Gaps:**

- Sensitive data identified but not classified
- Classification rationale missing (can't audit decision)
- No Data Owner approval of classification


**3. Ownership Gaps:**

- Data categories without assigned Data Owners
- Data Owner acknowledgment pending (>2 weeks)
- No backup Data Owner assigned


**4. Regulatory Gaps:**

- Regulatory applicability unclear (needs legal review)
- Cross-border restrictions not assessed
- Retention period not defined


**5. Prioritization Gaps:**

- P1 items without assigned implementation owner
- Target masking dates passed without completion
- No risk acceptance for delayed P1/P2 items


**Step-by-Step in Excel (Rows 8-57, 50 row template):**

For EACH identified gap:
1. **Gap ID:** Unique identifier (GAP-001)
2. **Gap Type:** Inventory / Classification / Ownership / Regulatory / Prioritization / Other
3. **Gap Description:** Specific issue (e.g., "CRM database not inventoried", "Health data category has no Data Owner")
4. **Affected System(s):** Which systems impacted?
5. **Affected Data Category:** Which data category impacted?
6. **Risk Level:** Critical / High / Medium / Low (risk if gap not closed)
7. **Impact if Not Resolved:** Regulatory fine / Audit finding / Data breach risk / Operational inefficiency
8. **Target Resolution Date:** When must this be closed?
9. **Responsible Party:** Who will close this gap?
10. **Current Status:** Not Started / In Progress / Blocked / Resolved
11. **Resolution Notes:** What action taken?

**Quality Checks:**

- [ ] All "Unknown" systems from Phase 1 have gap entries (require discovery)
- [ ] All data categories without Data Owners have gap entries
- [ ] All P1 items without implementation plans have gap entries
- [ ] All Critical/High risk gaps have target dates within 30/90 days


**Common Mistakes to Avoid:**

- ❌ Not documenting gaps (sweep under rug → audit finding)
- ❌ No accountability (gaps without owners stay open forever)
- ❌ Unrealistic timelines (30 days to inventory 100 systems → won't happen)
- ❌ Not escalating blocked gaps (stuck gaps need management intervention)


---

# Question-by-Question Guidance

## System_Inventory Sheet

**Q1: Does your organization maintain a comprehensive inventory of all systems containing sensitive data?**

**How to Answer:**

- **Yes:** You have a CMDB or asset inventory covering >90% of systems, regularly updated
- **No:** No formal inventory exists, relying on tribal knowledge
- **Partial:** Inventory exists but incomplete (missing SaaS, or only production, or >6 months stale)
- **Planned:** Inventory project approved and funded, not yet executed
- **N/A:** Organization has no IT systems (highly unlikely)


**Evidence to Attach:**

- CMDB export showing all database and application assets
- Asset inventory documentation with review dates
- System inventory procedure (how inventory is maintained)


**Common Issues:**

- "We have an Excel list from 2 years ago" → Answer: **Partial** (needs updating)
- "We know what systems we have, just not documented" → Answer: **No** (if not documented, doesn't count for audit)


---

**Q2: Are all production systems documented in the inventory?**

**How to Answer:**

- **Yes:** All production databases, applications, SaaS platforms documented
- **No:** Known production systems missing (e.g., shadow IT discovered)
- **Partial:** Most documented, but some gaps (e.g., departmental Access databases, rogue Excel files on file shares)


**How to Verify:**

- Cross-reference inventory against:
  - Monitoring tools (APM, SIEM logs)
  - Network scans (port 3306=MySQL, 1433=SQL Server, 5432=PostgreSQL, etc.)
  - Billing records (cloud provider invoices show all running resources)
  - Backup job lists (what's being backed up?)


**Red Flags:**

- Systems in monitoring but not in inventory
- Database connections in application configs not in inventory
- SaaS subscriptions in expense reports not in inventory


---

**Q3: Are non-production environments included in the inventory?**

**Why This Matters:** **Non-production environments often contain real production data** (copied for testing). This is a CRITICAL masking use case.

**How to Answer:**

- **Yes:** Dev, Test, QA, UAT, Training, Analytics, DR all documented
- **No:** Only production inventoried
- **Partial:** Some non-prod environments documented (e.g., UAT yes, but dev/test unknown)


**How to Verify:**

- Ask developers: "Where do you test code changes?" (dev database)
- Ask QA: "Where do you run test scripts?" (test database)
- Ask analytics team: "Where do you query data for reports?" (data warehouse, may have masked or unmasked prod data)


**Common Discovery:**

- Developer workstations with production database exports (CRITICAL GAP)
- Cloud "dev" accounts with copies of production databases
- QA environments refreshed weekly from production (unmasked)


---

## Sensitive_Data_Inventory Sheet

**How to handle large datasets (thousands of tables/columns)?**

**Approach 1: Table-Level Aggregation (Acceptable for initial assessment)**

- Group by table (e.g., "Customers table contains: CAT-PII-D, CAT-FIN")
- Document most sensitive category per table
- Note: Auditors may ask for column-level detail in future


**Approach 2: Column-Level Detail (Best Practice)**

- One row per sensitive column
- Allows precise masking technique selection later
- More time-consuming but audit-proof


**Hybrid Recommendation:**

- Column-level for Critical/High sensitivity data
- Table-level for Medium/Low sensitivity data
- Note in assessment: "Low priority data documented at table-level, will expand to column-level before masking implementation"


---

**Q: How do I validate false positives from automated scanning?**

**Common False Positives:**

- "SSN" column contains something else (System Serial Number)
- "Email" column contains email domains, not full addresses
- "DOB" column contains "Date of Business" not "Date of Birth"
- "Account" column contains account types, not account numbers


**Validation Method:**
```sql
-- Sample data to verify (with appropriate authorization)
SELECT column_name, 
       COUNT(DISTINCT column_name) as unique_values,
       MIN(LENGTH(column_name)) as min_length,
       MAX(LENGTH(column_name)) as max_length
FROM table_name
LIMIT 100;
```

**Look for:**

- SSN: Exactly 9 digits (or 11 with dashes), unique per person
- Email: Contains '@' symbol, valid domain
- Phone: 10 digits (North America) or international format
- Credit Card: 15-16 digits, passes Luhn algorithm


**If False Positive Confirmed:**

- Remove from Sensitive_Data_Inventory
- Document in "Discovery Notes" why excluded (audit trail)


---

## Classification_Matrix Sheet

**Q: Data Owner disagrees with my classification. How to resolve?**

**Conflict Resolution Process:**

1. **Clarify Policy Criteria:**

   - Share classification decision tree from policy
   - Explain regulatory drivers (e.g., "GDPR Art. 9 special category = Critical, not negotiable")


2. **Seek Objective Evidence:**

   - Data Owner: "Why do you think it's lower sensitivity?"
   - Review: Is there encryption, access controls, or other mitigating factors?
   - Re-assessment: If controls reduce exposure risk, may affect priority but not sensitivity classification


3. **Escalate if Needed:**

   - If regulatory requirement: CISO/DPO decision overrides Data Owner
   - If business judgment: Data Owner decision (with documented rationale and CISO approval)
   - Document disagreement and resolution in "Classification Rationale" column


**Example Scenario:**

- **Data:** Employee salaries
- **Initial Classification:** High (substantial privacy harm if exposed)
- **Data Owner (VP HR):** "This should be Medium, we don't consider it that sensitive"
- **Resolution:** Check regulatory requirements → No specific regulation mandates High → Data Owner decision accepted IF documented rationale: "Business policy treats compensation as Medium sensitivity, access restricted to HR only, annual employee acknowledgment of confidentiality" → Requires CISO approval


---

**Q: How to classify data that's sensitive in combination but not individually?**

**Example:** ZIP code alone = Public. Date of Birth alone = Public. ZIP + DOB together = Medium (can re-identify individuals in small populations).

**Approach:**
1. **Classify Individual Fields:**

   - ZIP code: Public
   - DOB: Low (indirect identifier)


2. **Document Combination Risk:**

   - In "Re-Identification Risk" column: "High when combined with ZIP code"
   - In "Masking Requirements" notes: "SHALL mask DOB when ZIP code present in same dataset"


3. **Adjust Priority:**

   - Individual DOB field: P3 or P4
   - DOB in table with ZIP: P1 or P2 (elevated due to combination risk)


---

## Regulatory_Mapping Sheet

**Q: How do I know if GDPR applies to my organization?**

**GDPR Applicability Checklist:**

- [ ] Organization is established in EU (even if non-EU parent company)
- [ ] Organization processes personal data of EU residents (customers, employees, website visitors)
- [ ] Organization monitors behavior of EU residents (website tracking, profiling)


**If ANY of above is YES → GDPR applies**

**Common Misconceptions:**

- ❌ "We're a US company, GDPR doesn't apply" → WRONG if you have EU customers
- ❌ "We don't have a EU office, GDPR doesn't apply" → WRONG if you process EU personal data
- ❌ "We're B2B, not B2C, GDPR doesn't apply" → WRONG, B2B companies still process employee data, contact data


**When in Doubt:** Consult legal counsel. Regulatory fines for non-compliance = 4% of global annual revenue.

---

**Q: What if I don't know whether HIPAA applies?**

**HIPAA Applicability (US-Specific):**

- [ ] Organization is a "Covered Entity": Healthcare providers, health plans, healthcare clearinghouses
- [ ] Organization is a "Business Associate": Provides services to covered entities involving PHI (Protected Health Information)


**If NEITHER of above → HIPAA does NOT apply**

**If EITHER of above → HIPAA applies (consult HIPAA compliance officer or legal)**

**Important:** HIPAA is US federal law. If your organization is not US-based and does not provide services to US healthcare entities, HIPAA does NOT apply.

**When in Doubt:** Answer "Conditional" and flag for legal review.

---

## Data_Owner_Assignment Sheet

**Q: What if the ideal Data Owner refuses or is unresponsive?**

**Escalation Path:**

1. **Attempt 1: Direct Outreach** (email, meeting request)
2. **Attempt 2: Manager Escalation** (contact Data Owner's manager)
3. **Attempt 3: CISO/CDO Escalation** (executive intervention)
4. **Fallback:** If no resolution after 3 attempts:

   - **Temporary Assignment:** CISO or DPO becomes interim Data Owner
   - **Document:** "Ownership assignment pending, interim owner: [CISO]"
   - **Escalate to Executive Leadership:** Ownership vacuum = governance failure


**Never Leave Data Orphaned:**

- Every data category MUST have an accountable owner
- If business refuses ownership → Risk acceptance by executive leadership required
- Document in Gap_Analysis sheet


---

# Evidence Collection

## What Evidence to Collect

**For System Inventory:**

- [ ] CMDB export (all systems, databases, applications)
- [ ] Cloud provider resource inventory (AWS RDS list, Azure SQL list, etc.)
- [ ] SaaS subscription list (with data storage location)
- [ ] Backup system inventory (what's being backed up = what exists)
- [ ] Network scan results (discovered databases, open ports)


**For Data Discovery:**

- [ ] Automated scanning tool report (BigID, OneTrust, etc.) with findings summary
- [ ] Database schema exports (with column metadata)
- [ ] Sample data queries (REDACTED, only patterns visible)
- [ ] Data Owner interview notes (business context for sensitive data)
- [ ] Discovery methodology documentation (how discovery was performed)


**For Classification:**

- [ ] Classification decision matrix (criteria applied per data element)
- [ ] Data Owner approval emails (written acknowledgment of classification)
- [ ] Regulatory guidance references (GDPR Art. 9 list, PCI-DSS requirements, etc.)
- [ ] Re-identification risk assessment (for indirect identifiers)


**For Ownership:**

- [ ] Data Owner assignment emails (sent requests)
- [ ] Data Owner acknowledgment confirmations (replies accepting ownership)
- [ ] Escalation correspondence (if ownership disputes)
- [ ] RACI matrix (Responsible, Accountable, Consulted, Informed for data categories)


**For Regulatory Mapping:**

- [ ] Legal counsel memo on regulatory applicability
- [ ] GDPR Records of Processing Activities (ROPA)
- [ ] PCI-DSS scope validation documentation
- [ ] HIPAA Business Associate Agreements (if applicable)


## Evidence Storage & Organization

**Recommended Folder Structure:**
```
Evidence/
├── 01_System_Inventory/
│   ├── CMDB_Export_20260119.xlsx
│   ├── AWS_RDS_Inventory_20260119.csv
│   ├── SaaS_Subscriptions_20260119.pdf
│   └── Network_Scan_Results_20260119.pdf
│
├── 02_Data_Discovery/
│   ├── BigID_Discovery_Report_20260119.pdf
│   ├── Database_Schemas_Sanitized_20260119.zip
│   ├── Sample_Data_Patterns_REDACTED_20260119.xlsx
│   └── Discovery_Methodology_Documentation_20260119.docx
│
├── 03_Classification/
│   ├── Classification_Decision_Matrix_20260119.xlsx
│   ├── Data_Owner_Approvals_20260119.pdf (email compilation)
│   ├── GDPR_Art9_Reference_20260119.pdf
│   └── ReID_Risk_Assessment_20260119.xlsx
│
├── 04_Ownership/
│   ├── Data_Owner_Assignment_Emails_Sent_20260119.pdf
│   ├── Data_Owner_Acknowledgments_20260119.pdf
│   ├── Ownership_RACI_Matrix_20260119.xlsx
│   └── Escalation_Correspondence_20260119.pdf
│
└── 05_Regulatory/
    ├── Legal_Memo_Regulatory_Applicability_20260119.pdf
    ├── GDPR_ROPA_20260119.xlsx
    ├── PCI_DSS_Scope_Validation_20260119.pdf
    └── Data_Retention_Schedule_20260119.xlsx
```

**Evidence Register (in Excel):**
Document ALL evidence in the `Evidence_Register` sheet with:

- Evidence ID (EV-001, EV-002, etc.)
- Evidence Type (System Inventory / Data Discovery / Classification / etc.)
- Description (what this evidence proves)
- File Name/Location (path to evidence file)
- Collection Date
- Collected By (who gathered this evidence)
- Retention Period (how long to keep evidence)


---

# Common Pitfalls & Troubleshooting

## "We Have Too Much Data to Inventory Everything"

**Problem:** Organization has hundreds of systems, thousands of tables, millions of data elements.

**Solution: Risk-Based Phasing**

**Phase 1 (Week 1-2): Crown Jewels**

- Inventory top 10-20 most critical systems (customer data, financial systems, HR systems)
- Full column-level detail for these systems
- Target: 80% of sensitive data with 20% of effort (Pareto principle)


**Phase 2 (Week 3-4): High-Risk Tier**

- Inventory next 30-50 systems (regulatory scope, high data volume)
- Table-level detail acceptable (can expand later)
- Target: 95% of sensitive data covered


**Phase 3 (Month 2-3): Long Tail**

- Inventory remaining systems
- Automated discovery tools critical at this scale
- Table-level detail for low-priority systems


**Phase 4 (Ongoing): Continuous Discovery**

- New systems trigger inventory update
- Quarterly review for changes (new columns, new systems)
- Annual full re-validation


**Document Phasing in Assessment:**

- "Assessment Status: Phase 1 Complete (20 systems, 100% column-level). Phase 2 In Progress (50 systems, table-level). Phase 3 Planned (Q2 2026)."


---

## "Automated Discovery Tool Missed Sensitive Data"

**Problem:** Data discovery tool didn't flag known sensitive data.

**Root Causes:**
1. **Non-Standard Column Names:** "Cust_SSN" instead of "SSN", "Soc_Sec_Num" instead of "Social_Security_Number"
2. **Encrypted/Hashed Data:** Tool can't pattern-match encrypted data
3. **Custom Business Data:** Proprietary data types tool doesn't recognize (e.g., internal employee IDs that are sensitive in your context)
4. **Tool Configuration:** Pattern matching rules not tuned for your environment

**Solutions:**
1. **Supplement with Manual Review:**

   - DBAs review schemas for sensitive-sounding column names
   - Application Owners identify business-specific sensitive data


2. **Tune Discovery Tool:**

   - Add custom patterns (regex for your SSN format variations)
   - Add synonym lists ("Soc_Sec", "Social_Sec", "SocSec", etc.)
   - Adjust sensitivity thresholds (reduce false negatives)


3. **Decrypt Sample Data (With Authorization):**

   - For encrypted fields, decrypt a sample to verify contents
   - Re-classify based on plaintext contents
   - Document: "Field encrypted, sample decryption confirmed [Data Category]"


4. **Accept Tool Limitations:**

   - No tool is 100% accurate
   - Manual review is ALWAYS needed for validation
   - Document in "Discovery Method" column: "Automated scan + manual schema review"


---

## "Data Owner Says 'I Don't Have Time for This'"

**Problem:** Data Owner refuses to engage in classification or ownership acknowledgment.

**Response Strategy:**

**1. Executive Escalation Email:**
```
Subject: Data Ownership Required for ISO 27001 Compliance

Dear [Data Owner],

Our organization is required to implement ISO 27001 Control A.8.11 (Data Masking) 
for regulatory compliance (GDPR, FADP, [Other]).

As the business owner of [Data Category], your input is required to:
1. Approve data classification decisions (30 minutes)
2. Acknowledge data ownership accountability (5 minutes)

Failure to assign Data Ownership creates the following risks:

- Audit finding (ISO 27001 certification failure)
- Regulatory non-compliance (GDPR Art. 5 accountability principle)
- Data breach liability (no clear accountability)


CISO [Name] has been copied for escalation if we cannot resolve this week.

Can we schedule 30 minutes this week?

Thank you,
[Your Name]
```

**2. Provide Executive Summary (One-Pager):**

- What is Data Ownership? (2 sentences)
- What are you asking me to do? (bullet list, time estimates)
- What happens if I say no? (regulatory/audit/risk impact)
- Who can I escalate to? (CISO, CDO)


**3. Offer to Do the Work:**

- "I will draft the classification decisions based on policy criteria. You just need to review and approve (15 minutes)."
- "I will pre-fill the ownership acknowledgment form. You just need to sign (5 minutes)."


**4. If Still Unresponsive:**

- Escalate to CISO → CISO escalates to Data Owner's executive management
- Document in Gap_Analysis: "Data Owner [Name] unresponsive after 3 attempts, escalated to CISO on [Date]"
- Interim assignment: CISO becomes temporary Data Owner until resolution


**Never Accept "No Owner":**

- Someone must be accountable (even if interim)
- Document resistance for audit trail (shows due diligence)


---

## "We Found Sensitive Data Where It Shouldn't Be"

**Problem:** Discovered PII in analytics database, production data in dev environment, unencrypted backups, etc.

**Immediate Actions:**

**1. Document as Critical Gap:**

- Gap ID: GAP-XXX
- Description: "Production PII discovered in unmasked dev database [System Name]"
- Risk Level: **Critical** (active compliance violation)
- Impact: Regulatory breach, audit finding, potential data leak


**2. Implement Immediate Containment:**

- Access restriction: Limit who can access this system (emergency ACL change)
- Monitoring: Enable audit logging on this system (detect access)
- Communication: Notify CISO immediately (may trigger incident response)


**3. Plan Remediation:**

- Option A: Delete sensitive data if not needed (fastest)
- Option B: Mask sensitive data in place (if data needed for testing)
- Option C: Replace with synthetic data (best practice for dev/test)
- Option D: Risk-accept with compensating controls (if remediation infeasible short-term)


**4. Root Cause Analysis:**

- How did sensitive data get here? (data copy process, backup restore, etc.)
- Who approved this? (lack of approval = process gap)
- How do we prevent recurrence? (mandatory masking before copy, policy enforcement)


**5. Update Assessment:**

- Add to Sensitive_Data_Inventory (now you know it exists)
- Classify as Critical/High (drives priority)
- Assign P1 priority (immediate masking required)
- Document in Evidence_Register (proof of discovery and remediation)


**Important:** Finding sensitive data where it shouldn't be is **NORMAL** during first assessment. This is WHY you're doing the assessment. Document, remediate, prevent recurrence.

---

## "Classification Criteria Are Ambiguous"

**Problem:** Policy says "substantial harm" for High sensitivity, but what is "substantial"?

**Solution: Develop Organization-Specific Examples**

Work with CISO/DPO/Legal to create a reference table:

| Sensitivity | Example Data Elements | Harm if Exposed | Regulatory Consequence |
|-------------|----------------------|-----------------|------------------------|
| **Critical** | SSN/AHV, Passport #, Credit Card (full PAN), Medical diagnoses, Genetic data, Child data | Severe personal harm (identity theft, discrimination, blackmail), Criminal liability | Guaranteed regulatory fine (GDPR Art. 83), Mandatory breach notification, Criminal charges possible |
| **High** | Full Name, Email, Phone, DOB, Full Address, Salary, Bank Account (IBAN), Precise geolocation | Substantial privacy violation, Reputational damage, Financial loss | Regulatory investigation likely, Breach notification required, Civil liability |
| **Medium** | Job Title + Department (indirect PII), IP Address, Device ID, Generalized location (city-level), Transaction history (anonymized) | Moderate privacy concern, Re-identification risk when combined, Business confidentiality | Regulatory scrutiny possible, Internal policy violation, Reputational risk |
| **Low** | Aggregate demographics (age range 30-40, region), Publicly available info, Non-sensitive business data | Minimal privacy risk, Low business impact | No regulatory consequence, Minimal reputational impact |

**Document in Policy Annex:** "Classification Examples - [Organization] Context"

**Reference During Assessment:** When classifying ambiguous data, use these examples as benchmarks.

---

# Quality Checklist

**Before submitting assessment for approval, verify:**

## Completeness Checks

**System Inventory:**

- [ ] All production systems documented (verified against CMDB, monitoring tools, billing)
- [ ] All non-production environments documented (dev, test, UAT, training, analytics, DR)
- [ ] SaaS/cloud systems included (Salesforce, Workday, Office 365, etc.)
- [ ] Backup/archive systems included (what's in backups = what exists)
- [ ] Decommissioned systems tracked (retention compliance)
- [ ] System Inventory Checklist all items addressed (15 checklist items)
- [ ] No "Unknown" sensitive data status without gap entry


**Data Discovery:**

- [ ] All "Yes" systems from System Inventory have corresponding data elements
- [ ] Data categories use standardized taxonomy (CAT-PII-D, CAT-FIN, etc., not free text)
- [ ] Sample patterns documented (helps validate classification)
- [ ] Discovery method documented per element (audit trail)
- [ ] False positives eliminated (validation performed)
- [ ] Column-level detail for Critical/High data (minimum)


**Classification:**

- [ ] All discovered data elements classified (Critical/High/Medium/Low)
- [ ] Classification rationale documented (not subjective "feels sensitive")
- [ ] Regulatory drivers identified (GDPR, FADP, HIPAA, PCI-DSS, etc.)
- [ ] Re-identification risk assessed (especially for indirect identifiers)
- [ ] Exposure risk considers current controls (encryption, access controls)
- [ ] Data Owner reviewed classification (documented approval)


**Regulatory Mapping:**

- [ ] All data categories mapped to applicable regulations
- [ ] GDPR Art. 9 special categories flagged (health, biometric, genetic, etc.)
- [ ] PCI-DSS scope defined (only cardholder data, not all financial data)
- [ ] HIPAA applicability confirmed with legal (if US-related)
- [ ] Cross-border restrictions documented (data residency requirements)
- [ ] Retention periods aligned with legal requirements


**Data Ownership:**

- [ ] All data categories have assigned Data Owners (no orphans)
- [ ] Data Owners are business stakeholders (not IT/security unless appropriate)
- [ ] Written acknowledgment obtained (email confirmation documented)
- [ ] Backup Data Owners identified (no single point of failure)
- [ ] Escalation path defined for disputes


**Prioritization:**

- [ ] All data elements have priority score calculated (P1/P2/P3/P4)
- [ ] Priority scoring algorithm applied consistently
- [ ] P1 items have implementation owner and target date
- [ ] Risk-accepted items have formal approval (Data Owner + CISO)


**Gap Analysis:**

- [ ] All identified gaps documented (inventory/classification/ownership/regulatory)
- [ ] Gap risk levels assigned (Critical/High/Medium/Low)
- [ ] Gap owners assigned (who will close)
- [ ] Target resolution dates realistic (not aspirational)
- [ ] Critical/High gaps have resolution dates ≤30/90 days


## Evidence Checks

- [ ] Minimum 15 evidence items in Evidence_Register
- [ ] Evidence covers all phases (inventory, discovery, classification, ownership, regulatory)
- [ ] Evidence files referenced by name/location (not vague "we have documentation")
- [ ] Evidence collection dates documented
- [ ] Evidence retention period defined (align with records management policy)


## Approval Checks

- [ ] Assessment completed by qualified personnel (Data Governance Lead, DPO, or designee)
- [ ] Quality review performed by independent reviewer (CISO, CDO, or senior data governance)
- [ ] Data Owners have reviewed and approved classifications for their categories
- [ ] CISO or CDO has reviewed and approved overall assessment
- [ ] Sign-off sheet completed with signatures and dates
- [ ] Next review date scheduled (quarterly for inventory updates, annual for classification review)


---

# Review & Approval Process

## Review Workflow

```
┌──────────────────────────────────────────────────────────────┐
│ STEP 1: Self-Review                                         │
│ - Assessor completes quality checklist (Section 7)          │
│ - Verify all yellow cells filled (no blanks in critical fields) │
│ - Run formula checks (Summary_Dashboard calculates correctly) │
│ - Collect evidence files                                    │
│ Duration: 1-2 hours                                         │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│ STEP 2: Data Owner Review                                   │
│ - Send draft assessment to Data Owners                      │
│ - Data Owners review classification for their categories    │
│ - Data Owners approve or request changes                    │
│ - Document approvals in Evidence_Register                   │
│ Duration: 3-5 business days (stakeholder coordination)      │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│ STEP 3: Technical Review (DBA/Security)                     │
│ - DBAs verify system inventory accuracy                     │
│ - Security team verifies exposure risk assessments          │
│ - Validate priority scoring logic                           │
│ Duration: 1-2 business days                                 │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│ STEP 4: Legal/Compliance Review                             │
│ - Legal confirms regulatory applicability (GDPR, FADP, HIPAA) │
│ - Compliance validates retention periods, data residency     │
│ - Approve or request changes to regulatory mapping          │
│ Duration: 2-3 business days                                 │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│ STEP 5: Executive Approval (CISO/CDO/DPO)                   │
│ - Executive review of Summary_Dashboard                     │
│ - Review P1 gaps and remediation timeline                   │
│ - Approve resource allocation for masking implementation    │
│ - Sign approval sheet                                       │
│ Duration: 1 business day (executive calendar permitting)    │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│ STEP 6: Publish & Communicate                               │
│ - Save final approved version with date stamp               │
│ - Upload to ISMS document repository                        │
│ - Communicate P1 action items to implementation teams       │
│ - Schedule quarterly review meeting (3 months from approval) │
│ Duration: 1 hour                                            │
└──────────────────────────────────────────────────────────────┘
```

**Total Workflow Duration:** 2-3 weeks (from completion to approval)

## Approval Sign-Off Sheet

**Required Signatures (in Excel `Summary_Dashboard` sheet):**

| Role | Name | Signature | Date | Comments |
|------|------|-----------|------|----------|
| **Data Governance Lead** | [Name] | [Digital signature or "Approved via email [date]"] | DD.MM.YYYY | Assessment completed and self-reviewed |
| **Chief Data Officer (CDO)** or **Data Protection Officer (DPO)** | [Name] | [Signature] | DD.MM.YYYY | Data classification and ownership approved |
| **Chief Information Security Officer (CISO)** | [Name] | [Signature] | DD.MM.YYYY | Risk assessment and prioritization approved, resource allocation approved for P1 gaps |
| **Legal/Compliance Officer** | [Name] | [Signature] | DD.MM.YYYY | Regulatory mapping validated |

**Optional (depending on organization):**

- **CTO / VP Engineering:** If technical infrastructure changes required
- **CFO:** If significant budget required for masking tools
- **Privacy Officer:** If separate from DPO role


## Post-Approval Actions

**Immediate (Within 1 Week):**

- [ ] Communicate approved assessment to stakeholders
- [ ] Assign P1 gap owners and implementation timelines
- [ ] Schedule kickoff for masking technique selection (IMP-A.8.11.2)
- [ ] Add to ISMS audit evidence repository


**Short-Term (Within 1 Month):**

- [ ] Begin P1 gap remediation (Critical priority items)
- [ ] Initiate procurement for data discovery or masking tools (if needed)
- [ ] Develop masking implementation roadmap (feeds into IMP-A.8.11.2, 3, 4)


**Ongoing (Quarterly):**

- [ ] Update System_Inventory (new systems, decommissioned systems)
- [ ] Re-run data discovery for new systems
- [ ] Update classification if regulatory landscape changes
- [ ] Review and update Data Owner assignments (role changes)
- [ ] Track gap remediation progress


**Annual:**

- [ ] Full classification review (REQ-CLS-032 policy requirement)
- [ ] Re-validate regulatory applicability
- [ ] Audit previous year's changes to data inventory
- [ ] Update assessment and obtain re-approval


---

# Maintenance & Updates

## Quarterly Review Cycle

**Trigger Events for Quarterly Review:**

- New system deployments (new databases, applications, SaaS subscriptions)
- System decommissions (retention compliance)
- Regulatory changes (new laws, updated guidance)
- Data Owner role changes (personnel changes)
- Audit findings or incidents (discovered gaps)


**Quarterly Review Checklist:**

- [ ] Update System_Inventory (add/remove systems)
- [ ] Re-run data discovery for new systems (automated or manual)
- [ ] Update ownership assignments (if personnel changes)
- [ ] Review P1/P2 gap remediation progress
- [ ] Update Summary_Dashboard metrics


**Duration:** 2-4 hours per quarter (maintenance, not full re-assessment)

## Annual Full Re-Assessment

**Annual Review Triggers:**

- ISO 27001 policy requirement (annual review)
- Regulatory requirement (GDPR ROPA annual update)
- Significant organizational changes (M&A, new business lines, geographic expansion)


**Annual Review Checklist:**

- [ ] Full System_Inventory validation (verify all systems still exist, configurations accurate)
- [ ] Classification review for all data categories (REQ-CLS-032)
- [ ] Regulatory landscape review (new laws, updated guidance)
- [ ] Data Owner re-confirmation (ensure continued accountability)
- [ ] Gap analysis (compare current state to prior year)
- [ ] Evidence refresh (collect new evidence, retire outdated)
- [ ] Executive re-approval (CISO/CDO sign-off)


**Duration:** 8-12 hours (refresh, not full re-inventory)

## Change Management Integration

**Process: New System Deployment**
1. IT submits change request for new database/application
2. Change approval workflow includes: "Does this system contain sensitive data?"
3. If YES → Trigger mini-assessment:

   - Add to System_Inventory
   - Run data discovery (before go-live if possible)
   - Classify data
   - Assign Data Owner
   - Determine masking priority

4. Update IMP-A.8.11.1 workbook
5. If P1 priority → Implement masking before production deployment

**Process: System Decommission**
1. IT submits decommission request
2. Check System_Inventory: Does this system contain sensitive data?
3. If YES → Retention compliance check:

   - Legal hold? (litigation, regulatory investigation)
   - Retention period satisfied? (per Regulatory_Mapping sheet)
   - Backup data destruction plan?

4. Update System_Inventory status: "Decommissioned [Date]"
5. Schedule data destruction per retention policy

---

# Integration with Other Assessments

This assessment (IMP-A.8.11.1) feeds into:

**ISMS-IMP-A.8.11.2 (Masking Technique Selection):**

- Input: Data categories and sensitivity levels from Classification_Matrix
- Output: Approved masking techniques per data category


**ISMS-IMP-A.8.11.3 (Environment Coverage Assessment):**

- Input: System inventory from System_Inventory (all environments)
- Output: Masking coverage verification per environment


**ISMS-IMP-A.8.11.4 (Testing & Validation):**

- Input: Masking requirements from Masking_Priority_Matrix
- Output: Test evidence proving masking effectiveness


**ISMS-IMP-A.8.11.5 (Compliance Dashboard):**

- Input: All data from this assessment (inventory, classification, ownership, gaps)
- Output: Executive dashboard consolidating all A.8.11 assessments


**Workflow Sequence:**
```
IMP-A.8.11.1 (Data Inventory) 
    → YOU ARE HERE
    ↓
IMP-A.8.11.2 (Technique Selection)
    → "What masking techniques do we use?"
    ↓
IMP-A.8.11.3 (Environment Coverage)
    → "Where have we implemented masking?"
    ↓
IMP-A.8.11.4 (Testing & Validation)
    → "Does masking actually work?"
    ↓
IMP-A.8.11.5 (Compliance Dashboard)
    → "Overall compliance status?"
```

---

# Frequently Asked Questions (FAQ)

**Q1: How often do we need to update the data inventory?**

**A:** 

- **Minimum (Policy Requirement):** Quarterly updates for system inventory, annual for classification review
- **Recommended:** After any significant change (new system, new data category, M&A, regulatory change)
- **Best Practice:** Continuous discovery with automated tools, monthly reporting


---

**Q2: Can we use a tool other than Excel for this assessment?**

**A:** Yes. The Excel workbook is a template. Organizations may use:

- Commercial GRC platforms (ServiceNow GRC, RSA Archer, etc.)
- Data governance tools (Collibra, Alation, Informatica, etc.)
- Custom databases or applications


**IMPORTANT:** Whatever tool you use, ensure it can provide audit evidence in a format auditors can review (exportable, traceable, timestamped).

---

**Q3: What if we discover data we shouldn't have (e.g., GDPR data we have no legal basis for)?**

**A:** 
1. **Document as Critical Gap** (Gap_Analysis sheet)
2. **Immediate containment:** Restrict access, enable monitoring
3. **Legal consultation:** Determine if legal basis exists or data must be deleted
4. **If no legal basis:** Data deletion required (GDPR Art. 17 Right to Erasure)
5. **Notify DPO:** May trigger breach notification if retention was unlawful
6. **Root cause analysis:** How did we get this data? Prevent recurrence.

---

**Q4: Our organization has 500 databases. Do we really need to inventory ALL of them?**

**A:** Use risk-based phasing (see Section 6.1). Start with:

- Crown jewel systems (top 10-20)
- Regulatory scope systems (GDPR, PCI-DSS, HIPAA)
- High-volume systems (customer data, employee data)
- Then expand to long tail


Document phasing in assessment. Auditors will accept phased approach IF:

- High-risk systems covered first
- Low-risk systems have documented timeline for inclusion
- Methodology is risk-based (not arbitrary)


---

**Q5: What if Data Owners disagree on classification?**

**A:** 
1. **Regulatory requirement trumps business judgment:** If GDPR Art. 9 says "Critical", Data Owner cannot override
2. **Business judgment applies where regulation silent:** Data Owner decides if no regulatory mandate
3. **CISO/DPO arbitrates disputes:** Escalate classification disagreements
4. **Document all decisions:** Classification rationale column captures debate and resolution

---

**Q6: Do we need Data Owners for non-sensitive data?**

**A:** This assessment focuses on **sensitive data requiring masking**. 

For non-sensitive data:

- Data ownership is still good governance practice
- But not required for ISO 27001 Control A.8.11 compliance
- Consider separate data governance initiative for all data (beyond A.8.11 scope)


---

**Q7: Can we classify data as "Public" to avoid masking?**

**A:** **Only if truly public.** 

"Public" means:

- Data is published on public website
- Data is available in public records (government databases, court filings)
- Data has no confidentiality requirement


**NOT public:**

- Customer names (even if not secret, still PII under GDPR)
- Employee data (even if org chart published)
- Aggregated data (anonymized aggregates may be public, but underlying data is NOT)


**Auditor will challenge "Public" classification.** Be prepared to justify.

---

**Q8: What if we don't have budget for automated data discovery tools?**

**A:** Manual discovery is acceptable for smaller environments. See Section 3.3 "Option B: Manual Discovery."

**Cost-Effective Alternatives:**

- Open-source tools (Amundsen, DataHub, Apache Atlas)
- Database native tools (Oracle Data Masking, SQL Server Data Discovery)
- Cloud-native tools (AWS Macie, Azure Purview - often included in existing subscriptions)
- SQL scripts (custom queries to find sensitive column patterns)


**IMPORTANT:** Document discovery methodology. Manual discovery is valid IF:

- Systematic (not ad-hoc)
- Documented (evidence of process)
- Validated (DBAs confirm completeness)


---

# Success Criteria

**This assessment is complete and audit-ready when:**

✅ **Inventory Completeness:**

- 100% of production systems inventoried
- >90% of non-production systems inventoried (documented plan for remaining 10%)
- All SaaS/cloud systems included
- Decommissioned systems tracked


✅ **Classification Coverage:**

- All identified sensitive data elements classified (Critical/High/Medium/Low)
- Classification rationale documented and defensible
- Data Owner approval obtained for classifications


✅ **Ownership Accountability:**

- Every data category has assigned Data Owner
- Written acknowledgment from Data Owners
- No "TBD" or "Unknown" ownership gaps


✅ **Risk Prioritization:**

- Masking priority (P1/P2/P3/P4) assigned to all data elements
- P1 items have implementation plan and owner
- Critical gaps have resolution timeline ≤30 days


✅ **Evidence & Audit Trail:**

- Minimum 15 evidence items documented
- Discovery methodology traceable
- Classification decisions auditable
- Ownership acknowledgments provable


✅ **Executive Approval:**

- CISO/CDO/DPO sign-off obtained
- Legal/Compliance validation completed
- Resource allocation approved for P1 gaps
- Next review date scheduled


---

# Next Steps After Completion

**Upon approval of this assessment, proceed to:**

**1. ISMS-IMP-A.8.11.2 (Masking Technique Selection):**

- Select appropriate masking techniques per data category
- Document technique configuration requirements
- Identify gaps in masking tool capabilities


**2. Masking Tool Evaluation (if not already deployed):**

- RFI/RFP for data masking solutions
- Proof-of-concept testing
- Procurement and deployment


**3. Data Owner Engagement:**

- Present masking technique recommendations
- Obtain Data Owner approval for technique selections
- Define masking scope per environment


**4. Implementation Roadmap:**

- Develop project plan for P1 gap remediation
- Allocate resources (people, budget, tools)
- Establish governance cadence (weekly implementation sync)


---

**END OF PART I: USER COMPLETION GUIDE**

---

**Document Assembly Note:**
This is **PART I** of ISMS-IMP-A.8.11.1. 

**PART II (Technical Specification)** follows in the next deliverable and contains:

- Detailed Excel sheet structure (10 sheets)
- Column definitions and data types
- Data validation rules (dropdowns, formulas)
- Conditional formatting specifications
- Python script integration notes
- Formula examples and calculations
- Styling and formatting standards


**To create complete ISMS-IMP-A.8.11.1 v1.0 document:**
1. PART I: User Completion Guide (this file)
2. PART II: Technical Specification (next deliverable)

---

**Document Control:**

- **Version:** 1.0
- **Date:** [Date]
- **Status:** Draft for Review
- **Author:** ISMS Implementation Team
- **Approver:** CISO / CDO / DPO


---

*"You cannot protect what you do not know exists. Data inventory is the foundation of all data protection controls."*

# ISMS-IMP-A.8.11.1 - Data Inventory & Classification Assessment
# PART II: TECHNICAL SPECIFICATION

---

# Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.11.1 |
| **Version** | 1.0 |
| **Assessment Area** | Sensitive Data Inventory & Classification |
| **Related Policy** | ISMS-POL-A.8.11, Section 2.1 (Data Classification and Identification) |
| **Purpose** | Technical specification for Excel workbook documenting all systems containing sensitive data, data classification, ownership assignment, and masking requirements |
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

This document provides the **complete technical blueprint** for generating the ISMS-IMP-A.8.11.1 Data Inventory & Classification Assessment Excel workbook using Python (openpyxl).

**What This Specification Defines:**

- Exact Excel workbook structure (11 sheets)
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
python3 generate_a811_1_data_inventory.py
# Output: ISMS-IMP-A.8.11.1_Data_Inventory_Classification_20260119.xlsx
```

**Manual Creation (Not Recommended):**

- Create workbook structure manually following this specification
- Error-prone, time-consuming, difficult to maintain
- Use only if Python environment unavailable


## Key Design Principles

**Data-Centric, Not Tool-Centric:**

- Focus on WHAT data exists, WHERE it resides, WHO owns it
- Tool/product-agnostic (works with any masking solution or custom scripts)
- Platform-agnostic (cloud, on-premises, hybrid, SaaS)


**Evidence-Based Assessment:**

- Every classification requires justification
- Every ownership assignment requires approval
- Every masking requirement traced to data sensitivity
- Audit trail maintained throughout


**Scalability:**

- 50-row templates per sheet (expandable to 1,000+ with minimal modification)
- Supports organizations with 5 systems or 500 systems
- Formula references use dynamic ranges where possible


---

# Workbook Structure Overview

## Sheet Summary

| Sheet # | Sheet Name | Primary Purpose | Row Count | User Input Cells |
|---------|------------|-----------------|-----------|------------------|
| 1 | **Instructions_Legend** | User guide, taxonomy reference | ~100 | 5 (metadata) |
| 2 | **System_Inventory** | Master list of all systems/databases | ~70 | 50 data rows |
| 3 | **Data_Category_Reference** | Data category taxonomy definitions | ~40 | 0 (reference only) |
| 4 | **Sensitive_Data_Inventory** | Field-level sensitive data catalog | ~70 | 100 data rows |
| 5 | **Classification_Matrix** | Data sensitivity classification | ~70 | 100 data rows |
| 6 | **Regulatory_Mapping** | Map data to regulatory requirements | ~60 | 50 data rows |
| 7 | **Data_Owner_Assignment** | Assign ownership per data category | ~50 | 30 data rows |
| 8 | **Masking_Priority_Matrix** | Prioritize masking implementation | ~70 | 50 data rows |
| 9 | **Gap_Analysis** | Document classification/ownership gaps | ~50 | 30 data rows |
| 10 | **Evidence_Register** | Track compliance evidence | ~60 | 40 data rows |
| 11 | **Summary_Dashboard** | Executive compliance summary | ~80 | 10 (sign-off) |

**Total Sheets:** 11  
**Total Template Capacity:** ~500 assessment data points

---

# Sheet 1: Instructions_Legend

## Purpose
Provide user guidance, taxonomy reference, status legends, and acceptable evidence examples.

## Sheet Structure

**Row Layout:**

- Rows 1-2: Document header (title, subtitle)
- Rows 3-10: Document metadata (Document ID, Version, Date, etc.)
- Rows 11-25: How to Use This Workbook (numbered steps)
- Rows 26-40: Data Category Taxonomy (reference table)
- Rows 41-50: Sensitivity Classification Levels (reference table)
- Rows 51-60: Status Legend (symbol definitions)
- Rows 61-80: Acceptable Evidence Examples (bulleted list)


## Header Section (Rows 1-2)

**Row 1: Main Title**

- **Cell A1:** "ISMS-IMP-A.8.11.1 – Data Inventory & Classification Assessment"
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


## Document Metadata (Rows 4-10)

**Table Format:**
| Row | Column A (Label) | Column B-C (Value) | Styling |
|-----|------------------|-------------------|---------|
| 4 | Document ID: | ISMS-IMP-A.8.11.1 | Label: Bold, Value: Normal |
| 5 | Assessment Area: | Data Inventory & Classification | |
| 6 | Related Policy: | ISMS-POL-A.8.11, Section 2.1 (Data Classification and Identification) | |
| 7 | Version: | 2.0 | |
| 8 | Assessment Date: | [USER INPUT] | Yellow fill (RGB 255,255,204) |
| 9 | Completed By: | [USER INPUT] | Yellow fill |
| 10 | Organization: | [USER INPUT] | Yellow fill |
| 11 | Review Cycle: | Quarterly (Inventory) / Annual (Classification Review) | |

**Cell Details:**

- **Column A Width:** 20
- **Column B-C Width:** 40 (merged)
- **Font:** Calibri 10pt
- **Border:** Thin border around each cell


## How to Use This Workbook (Rows 13-25)

**Row 13: Section Header**

- **Cell A13:** "How to Use This Workbook"
- **Merge:** A13:Q13
- **Font:** Calibri 12pt Bold
- **Fill:** RGB(217, 217, 217) - Light Gray (#D9D9D9)
- **Alignment:** Left


**Rows 14-25: Numbered Instructions**
```
1. Start with System_Inventory – list ALL systems/databases that process data
2. Use Data_Category_Reference to understand sensitivity taxonomy
3. Complete Sensitive_Data_Inventory for each system (table/field level)
4. Apply classification using the Classification_Matrix sheet
5. Map data to regulatory requirements in Regulatory_Mapping
6. Assign data owners in Data_Owner_Assignment
7. Prioritize masking efforts in Masking_Priority_Matrix
8. Document gaps in Gap_Analysis
9. Maintain evidence in Evidence_Register
10. Review summary metrics in Summary_Dashboard
11. Obtain required approvals
12. Archive completed workbook with assessment date in filename
```

**Format:**

- **Cell Range:** A14:Q25
- **Font:** Calibri 10pt
- **Wrap Text:** Enabled
- **Indentation:** 1 level for sub-bullets


## Data Category Taxonomy (Rows 27-40)

**Row 27: Section Header**

- **Cell A27:** "Data Category Taxonomy (Quick Reference)"
- **Merge:** A27:E27
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray


**Rows 28-40: Taxonomy Table**

| Row | Cat ID | Category Name | Examples | Regulatory Scope |
|-----|--------|--------------|----------|------------------|
| 29 | CAT-PII-D | Direct PII | Name, SSN/AHV, Passport, Email, Phone | GDPR, FADP, CCPA |
| 30 | CAT-PII-I | Indirect PII | DOB+ZIP, Job Title+Department | GDPR, FADP |
| 31 | CAT-FIN | Financial Data | Credit Card (PAN), IBAN, Account Balance | PCI-DSS, FADP |
| 32 | CAT-HLT | Health Data | Diagnoses, Prescriptions, Medical Records | HIPAA, GDPR Art.9 |
| 33 | CAT-CRD | Credentials | Passwords, API Keys, Tokens, Private Keys | ISO 27001 A.9 |
| 34 | CAT-PRP | Proprietary Data | Trade Secrets, Pricing Models, IP | Contract, NDA |
| 35 | CAT-LOC | Location Data | GPS Coordinates, IP Address, Travel History | GDPR, CCPA |
| 36 | CAT-BIO | Biometric Data | Fingerprints, Facial Geometry, Voice Print | GDPR Art.9, BIPA |
| 37 | CAT-GEN | Genetic Data | DNA Sequences, Genetic Test Results | GDPR Art.9, GINA |
| 38 | CAT-CHD | Child Data | Data of minors (<16 GDPR / <18 COPPA) | GDPR, COPPA |
| 39 | CAT-LEG | Legal Data | Contracts, Legal Opinions, Litigation Records | Attorney-Client |
| 40 | CAT-ETH | Ethnicity/Race | Ethnic Origin, Religious Beliefs, Political Views | GDPR Art.9 |

**Column Specifications:**

- **Column A (Cat ID):** Width 12, Font Bold
- **Column B (Category Name):** Width 20
- **Column C (Examples):** Width 40, Wrap Text
- **Column D (Regulatory Scope):** Width 20, Wrap Text


## Sensitivity Classification Levels (Rows 42-50)

**Row 42: Section Header**

- **Cell A42:** "Sensitivity Classification Levels"
- **Merge:** A42:D42


**Rows 43-50: Classification Table**

| Row | Level | Definition | Masking Requirement | Breach Impact |
|-----|-------|------------|---------------------|---------------|
| 44 | **Critical** | Severe harm if exposed, regulatory breach guaranteed | SHALL mask in ALL non-production | Legal action, fines, reputational damage |
| 45 | **High** | Substantial harm, privacy violation, regulatory risk | SHALL mask in non-production | Regulatory investigation, customer loss |
| 46 | **Medium** | Moderate harm, business impact, competitive risk | SHOULD mask in non-production | Business disruption, competitive disadvantage |
| 47 | **Low** | Minimal harm, internal use only | MAY mask based on risk assessment | Minor operational impact |
| 48 | **Public** | No confidentiality requirement | N/A | No impact (publicly available) |

**Conditional Formatting:**

- **Critical row:** Red fill (RGB 255, 199, 206)
- **High row:** Orange fill (RGB 255, 235, 156)
- **Medium row:** Yellow fill (RGB 255, 242, 204)
- **Low row:** Light green (RGB 226, 239, 218)
- **Public row:** White (no fill)


## Status Legend (Rows 52-60)

**Row 52: Section Header**

- **Cell A52:** "Status Legend"
- **Merge:** A52:D52


**Rows 53-60: Status Symbols**

| Symbol | Status | Description | Color Code (RGB) |
|--------|--------|-------------|------------------|
| ✅ | Complete | Inventory complete, classified, owner assigned | 198, 239, 206 (Green) |
| ⚠️ | Partial | Partial inventory/classification in progress | 255, 235, 156 (Yellow) |
| ❌ | Missing | Not inventoried or classified | 255, 199, 206 (Red) |
| 📋 | Planned | Discovery/classification scheduled | 180, 199, 231 (Blue) |
| N/A | Not Applicable | System contains no sensitive data | 217, 217, 217 (Gray) |

## Acceptable Evidence (Rows 62-80)

**Row 62: Section Header**

- **Cell A62:** "Acceptable Evidence Examples"
- **Merge:** A62:D62


**Rows 63-80: Bulleted List**
```
✓ Database schema documentation (ERD diagrams, data dictionaries)
✓ Data discovery tool reports (BigID, Varonis, OneTrust, etc.)
✓ Data flow diagrams showing data movement across systems
✓ Data Processing Impact Assessments (DPIA) per GDPR
✓ System design documents with data element definitions
✓ Privacy policy documentation
✓ Data retention schedules
✓ Data owner assignment matrices (RACI charts)
✓ Classification review meeting minutes
✓ Regulatory compliance gap assessments
✓ Third-party data sharing agreements (DPAs)
✓ Screenshots of actual data samples (redacted/masked)
✓ SQL query results showing data structure
✓ API documentation showing data payloads
✓ Application configuration files (anonymized)
✓ Change management records for schema changes
✓ Data lineage documentation
✓ Metadata repository exports
```

**Format:**

- **Cell Range:** A63:D80
- **Font:** Calibri 10pt
- **Bullet Character:** ✓
- **Line Spacing:** 1.2


---

# Sheet 2: System_Inventory

## Purpose
Document all systems, applications, databases, and data repositories. Master list of WHERE sensitive data resides.

## Header Section (Rows 1-5)

**Row 1: Sheet Title**

- **Cell A1:** "SYSTEM & DATABASE INVENTORY"
- **Merge:** A1:Q1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center


**Row 2: Instructions**

- **Cell A2:** "List ALL systems that process, store, or transmit data (50 row template, expandable)"
- **Merge:** A2:Q2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4)
- **Alignment:** Center


**Row 3: Assessment Question**

- **Cell A3:** "Does [Organization] maintain a comprehensive inventory of all systems containing sensitive data?"
- **Merge:** A3:M3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)
- **Border:** Thick border


**Row 4: Response**

- **Cell N4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** N4:Q4
- **Fill:** Light Yellow (#FFFFCC)
- **Data Validation:** List = "Yes,No,Partial,Planned,N/A"


## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | System ID | 15 | Text | Free text (SYS-001, SYS-002, etc.) |
| B | System Name | 25 | Text | Free text |
| C | System Type | 18 | Dropdown | Database, Application, SaaS, File Share, API, Data Warehouse, Backup System, Archive, Other |
| D | Environment | 15 | Dropdown | Production, Development, Test/QA, UAT, Training, Analytics, DR/Backup, Decommissioned |
| E | Contains Sensitive Data? | 18 | Dropdown | Yes, No, Unknown |
| F | Data Categories Present | 25 | Text | Free text (comma-separated CAT-IDs) |
| G | Hosting Location | 20 | Dropdown | On-Premises, AWS, Azure, GCP, Multi-Cloud, Hybrid, Third-Party Hosted, Unknown |
| H | Primary Data Owner | 20 | Text | Free text (role or name) |
| I | System Owner/Admin | 20 | Text | Free text |
| J | Inventory Status | 18 | Dropdown | ✅ Complete, ⚠️ Partial, ❌ Missing, 📋 Planned, N/A |
| K | Last Inventory Date | 15 | Date | Date picker (DD.MM.YYYY) |
| L | Next Review Date | 15 | Date | Date picker (auto-calculate: Last Date + 90 days) |
| M | Record Count (Approx) | 15 | Number | Whole numbers only, allow commas |
| N | Retention Period | 15 | Text | Free text ("7 years", "Indefinite", etc.) |
| O | Regulatory Scope | 20 | Text | Free text (GDPR, FADP, HIPAA, etc.) |
| P | Decommission Date | 15 | Date | Date picker (optional) |
| Q | Notes/Comments | 30 | Text | Free text, wrap text enabled |

**Header Row Formatting:**

- **Row Height:** 30px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 7 (keep headers visible when scrolling)


## Example Row (Row 7)

**Purpose:** Show users a sample entry with realistic data

| Col | Value |
|-----|-------|
| A | SYS-001 |
| B | Customer Database |
| C | Database |
| D | Production |
| E | Yes |
| F | CAT-PII-D, CAT-FIN |
| G | On-Premises |
| H | Chief Data Officer |
| I | Database Admin Team |
| J | ✅ Complete |
| K | 15.01.2026 |
| L | 15.04.2026 |
| M | 1,250,000 |
| N | 7 years |
| O | GDPR, FADP |
| P | [blank] |
| Q | Primary CRM database, contains customer orders and payment info |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic
- **Border:** Thin borders
- **Note:** Add cell comment to Row 7: "This is an example row. Delete or replace with actual data."


## Data Entry Rows (Rows 8-57)

**50 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC) for all cells
- **Font:** Calibri 10pt Regular
- **Border:** Thin borders
- **Protection:** Unlocked (allow user input)
- **Auto-numbering:** Column A can auto-populate "SYS-{ROW-7}" if desired


**Formula in Column L (Next Review Date):**
```excel
=IF(ISBLANK(K8),"",DATE(YEAR(K8),MONTH(K8)+3,DAY(K8)))
```
Explanation: If Last Inventory Date exists, add 3 months (90 days)

---

**This completes Response 1. Shall I continue with Sheet 3 (Data_Category_Reference) and Sheet 4 (Sensitive_Data_Inventory) in Response 2?**

## System Inventory Checklist (Rows 59-75)

**Row 59: Section Header**

- **Cell A59:** "SYSTEM INVENTORY CHECKLIST"
- **Merge:** A59:E59
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center


**Row 60: Table Headers**

| Column | Header | Width |
|--------|--------|-------|
| A | # | 5 |
| B | Checklist Item | 50 |
| C | Status | 15 |
| D | Evidence | 25 |
| E | Notes | 25 |

**Rows 61-75: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is a comprehensive system inventory maintained? | [Dropdown] | [Text] | [Text] |
| 2 | Are all production systems documented? | [Dropdown] | [Text] | [Text] |
| 3 | Are non-production environments included? | [Dropdown] | [Text] | [Text] |
| 4 | Are SaaS/cloud systems included? | [Dropdown] | [Text] | [Text] |
| 5 | Are backup/archive systems included? | [Dropdown] | [Text] | [Text] |
| 6 | Are data warehouses/analytics systems included? | [Dropdown] | [Text] | [Text] |
| 7 | Is system type classified for each entry? | [Dropdown] | [Text] | [Text] |
| 8 | Is hosting location documented? | [Dropdown] | [Text] | [Text] |
| 9 | Are system owners assigned for each system? | [Dropdown] | [Text] | [Text] |
| 10 | Are data owners assigned for each system? | [Dropdown] | [Text] | [Text] |
| 11 | Is inventory reviewed quarterly? | [Dropdown] | [Text] | [Text] |
| 12 | Are decommissioned systems tracked? | [Dropdown] | [Text] | [Text] |
| 13 | Is approximate record count documented? | [Dropdown] | [Text] | [Text] |
| 14 | Is data retention period documented? | [Dropdown] | [Text] | [Text] |
| 15 | Are regulatory requirements mapped per system? | [Dropdown] | [Text] | [Text] |

**Data Validation (Column C - Status):**

- **Formula:** "✅ Complete,⚠️ Partial,❌ Missing,📋 Planned,N/A"
- **Allow Blank:** No
- **Error Message:** "Please select a valid status"


**Conditional Formatting (Column C):**

- ✅ Complete → Green fill (RGB 198, 239, 206)
- ⚠️ Partial → Yellow fill (RGB 255, 235, 156)
- ❌ Missing → Red fill (RGB 255, 199, 206)
- 📋 Planned → Blue fill (RGB 180, 199, 231)
- N/A → Gray fill (RGB 217, 217, 217)


## Reference Table: System Types (Rows 77-85)

**Row 77: Section Header**

- **Cell A77:** "SYSTEM TYPE DEFINITIONS"
- **Merge:** A77:C77
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray


**Rows 78-85: System Type Descriptions**

| System Type | Description | Examples |
|-------------|-------------|----------|
| Database | Relational or NoSQL databases | Oracle, PostgreSQL, MongoDB, SQL Server, MySQL |
| Application | Business applications | CRM, ERP, HR systems, Custom applications |
| SaaS | Cloud-based software services | Salesforce, Workday, ServiceNow, Office 365 |
| File Share | File storage systems | SharePoint, NAS, File servers, S3 buckets |
| API | API gateways and services | REST APIs, SOAP services, Integration platforms |
| Data Warehouse | Analytics and BI systems | Snowflake, Redshift, BigQuery, Tableau Server |
| Backup System | Backup and recovery systems | Veeam, Backup appliances, Cloud backup |
| Archive | Long-term archival storage | Tape libraries, Cold storage, Compliance archives |

**Formatting:**

- **Column Widths:** A=18, B=35, C=40
- **Font:** Calibri 10pt
- **Border:** All borders, thin weight


---

# Sheet 3: Data_Category_Reference

## Purpose
Comprehensive reference taxonomy for data sensitivity categories. **Read-only reference sheet** for users to understand classification scheme.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "DATA CATEGORY REFERENCE TAXONOMY"
- **Merge:** A1:H1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center


**Row 2: Instructions**

- **Cell A2:** "Reference Guide - Use Category IDs when documenting sensitive data (e.g., CAT-PII-D for Direct PII)"
- **Merge:** A2:H2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center


**Row 3: Warning Note**

- **Cell A3:** "⚠️ This is a REFERENCE sheet. Do not modify. Use these Category IDs in Sensitive_Data_Inventory and Classification_Matrix sheets."
- **Merge:** A3:H3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)
- **Border:** Thick border


## Column Headers (Row 5)

| Col | Header | Width | Description |
|-----|--------|-------|-------------|
| A | Category ID | 12 | Unique identifier (CAT-XXX-X) |
| B | Category Name | 20 | Human-readable name |
| C | Description | 35 | Detailed definition |
| D | Examples | 30 | Concrete field examples |
| E | Default Sensitivity | 15 | Recommended classification level |
| F | Regulatory Scope | 20 | Applicable regulations |
| G | Typical Location | 25 | Common system/table locations |
| H | Masking Priority | 12 | Default priority (P1/P2/P3/P4) |

**Header Row Formatting:**

- **Row Height:** 35px
- **Font:** Calibri 10pt Bold, Black
- **Fill:** Light Gray (#D9D9D9)
- **Alignment:** Center, Vertical Center, Wrap Text
- **Border:** All borders, medium weight
- **Freeze Panes:** Row 6


## Data Rows (Rows 6-30)

**Row 6: CAT-PII-D (Direct PII)**
| Col | Value |
|-----|-------|
| A | CAT-PII-D |
| B | Direct PII (Personally Identifiable Information) |
| C | Data that directly identifies an individual without requiring additional information |
| D | Full name, SSN, AHV number, Passport number, National ID, Email address, Phone number, Employee ID |
| E | High to Critical |
| F | GDPR Art.4(1), FADP Art.5, CCPA, LGPD |
| G | users.name, employees.email, customers.phone, accounts.ssn |
| H | P1 (Critical) |

**Row 7: CAT-PII-I (Indirect PII)**
| Col | Value |
|-----|-------|
| A | CAT-PII-I |
| B | Indirect PII (Quasi-Identifiers) |
| C | Data that can identify an individual when combined with other information |
| D | Date of Birth + ZIP code, Job title + Department, IP address + Timestamp, Device ID + Location |
| E | Medium to High |
| F | GDPR Art.4(1), FADP Art.5 |
| G | users.date_of_birth, employees.department, logs.ip_address |
| H | P2 (High) |

**Row 8: CAT-FIN (Financial Data)**
| Col | Value |
|-----|-------|
| A | CAT-FIN |
| B | Financial Data |
| C | Payment card information, bank account details, transaction data, financial statements |
| D | Credit card PAN, CVV, IBAN, Bank account number, Wire transfer details, Account balance, Salary |
| E | Critical |
| F | PCI-DSS v4.0, GDPR, FADP, GLBA |
| G | payments.card_number, transactions.iban, payroll.salary |
| H | P1 (Critical) |

**Row 9: CAT-HLT (Health Data)**
| Col | Value |
|-----|-------|
| A | CAT-HLT |
| B | Health/Medical Data |
| C | Protected health information (PHI), medical records, diagnoses, treatment information |
| D | Diagnoses (ICD codes), Prescriptions, Lab results, Medical imaging, Patient history, Insurance claims |
| E | Critical |
| F | HIPAA, GDPR Art.9 (Special Category), FADP Art.5(c) |
| G | patient_records.diagnosis, prescriptions.medication, lab_results.values |
| H | P1 (Critical) |

**Row 10: CAT-CRD (Credentials)**
| Col | Value |
|-----|-------|
| A | CAT-CRD |
| B | Authentication Credentials |
| C | Passwords, API keys, tokens, certificates, private keys, secrets |
| D | Password hashes, API keys, OAuth tokens, JWT tokens, SSH private keys, Certificate private keys |
| E | Critical |
| F | ISO 27001 A.9.4.3, NIST SP 800-63B, PCI-DSS Req.8 |
| G | users.password_hash, api_keys.secret, certificates.private_key |
| H | P1 (Critical) |

**Row 11: CAT-PRP (Proprietary Data)**
| Col | Value |
|-----|-------|
| A | CAT-PRP |
| B | Proprietary Business Data |
| C | Trade secrets, intellectual property, pricing models, strategic plans, confidential business information |
| D | Pricing algorithms, Customer lists, Contract terms, Product roadmaps, M&A documents, Source code |
| E | High to Critical |
| F | Trade Secret Law, NDA contracts, UTSA |
| G | pricing.algorithm, contracts.terms, products.roadmap |
| H | P2 (High) |

**Row 12: CAT-LOC (Location Data)**
| Col | Value |
|-----|-------|
| A | CAT-LOC |
| B | Location/Geolocation Data |
| C | Geographic location information that can track or identify individuals' whereabouts |
| D | GPS coordinates, IP addresses, WiFi/BLE beacon data, Cell tower triangulation, Travel history, Home/work addresses |
| E | High |
| F | GDPR Art.4(1), CCPA, ePrivacy Directive |
| G | tracking.gps_lat_long, users.ip_address, devices.location_history |
| H | P2 (High) |

**Row 13: CAT-BIO (Biometric Data)**
| Col | Value |
|-----|-------|
| A | CAT-BIO |
| B | Biometric Data |
| C | Unique physical/behavioral characteristics for authentication or identification |
| D | Fingerprints, Facial geometry, Iris scans, Voice prints, Keystroke dynamics, Gait analysis |
| E | Critical |
| F | GDPR Art.9 (Special Category), BIPA (Illinois), CCPA |
| G | biometric_auth.fingerprint_template, face_recognition.feature_vector |
| H | P1 (Critical) |

**Row 14: CAT-GEN (Genetic Data)**
| Col | Value |
|-----|-------|
| A | CAT-GEN |
| B | Genetic/Genomic Data |
| C | DNA sequences, genetic test results, hereditary disease information |
| D | DNA sequences, Genomic variants, Genetic test results, Family disease history, Pharmacogenomics data |
| E | Critical |
| F | GDPR Art.9 (Special Category), GINA (US), FADP Art.5(c) |
| G | genetic_tests.dna_sequence, health_records.hereditary_conditions |
| H | P1 (Critical) |

**Row 15: CAT-CHD (Child Data)**
| Col | Value |
|-----|-------|
| A | CAT-CHD |
| B | Child/Minor Data |
| C | Personal data of children/minors (age <16 GDPR / <13 COPPA / <18 jurisdiction-specific) |
| D | Any PII of minors: Names, Birthdates, School records, Parental consent records, Online activity |
| E | Critical |
| F | GDPR Art.8, COPPA (US), FADP (enhanced protection) |
| G | students.name, minors.birthdate, parental_consent.records |
| H | P1 (Critical) |

**Row 16: CAT-LEG (Legal Data)**
| Col | Value |
|-----|-------|
| A | CAT-LEG |
| B | Legal/Attorney-Client Data |
| C | Attorney-client privileged communications, legal opinions, litigation materials |
| D | Legal contracts, Court documents, Attorney communications, Settlement agreements, Legal opinions |
| E | High to Critical |
| F | Attorney-Client Privilege, Work Product Doctrine |
| G | legal_docs.contract, litigation.correspondence |
| H | P2 (High) |

**Row 17: CAT-ETH (Ethnicity/Race)**
| Col | Value |
|-----|-------|
| A | CAT-ETH |
| B | Ethnicity/Race/Religion/Politics |
| C | Special category data revealing ethnic origin, religious beliefs, political opinions, sexual orientation |
| D | Ethnic origin, Race, Religious affiliation, Political party membership, Sexual orientation, Trade union membership |
| E | Critical |
| F | GDPR Art.9 (Special Category), FADP Art.5(c) |
| G | surveys.ethnicity, employees.religion, members.political_affiliation |
| H | P1 (Critical) |

**Rows 18-25: Additional Categories (Organization-Specific)**

- **Purpose:** Allow organizations to define custom categories
- **Default:** Leave blank with instruction to add custom categories as needed
- **Format:** Same column structure as above


**Formatting for All Data Rows:**

- **Font:** Calibri 10pt Regular
- **Border:** Thin borders all cells
- **Wrap Text:** Enabled for columns C, D, G
- **Alignment:** Left for text, Center for Column A
- **Protection:** Locked (read-only reference)


## Category Summary Statistics (Rows 27-30)

**Row 27: Summary Header**

- **Cell A27:** "CATEGORY SUMMARY"
- **Merge:** A27:D27
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray


**Row 28-30: Statistics**

| Metric | Formula |
|--------|---------|
| Total Categories Defined | `=COUNTA(A6:A25)` |
| Critical Categories | `=COUNTIF(E6:E25,"Critical")` |
| High Categories | `=COUNTIF(E6:E25,"High")` |

---

# Sheet 4: Sensitive_Data_Inventory

## Purpose
Document **field-level** inventory of sensitive data elements. This is the detailed catalog of WHAT sensitive data exists and WHERE (down to table/column level).

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "SENSITIVE DATA INVENTORY (Field-Level)"
- **Merge:** A1:R1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center


**Row 2: Instructions**

- **Cell A2:** "Document all fields/columns containing sensitive data at table/field level (100 row template)"
- **Merge:** A2:R2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center


**Row 3: Assessment Question**

- **Cell A3:** "Has [Organization] completed a comprehensive field-level inventory of all sensitive data elements?"
- **Merge:** A3:N3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)


**Row 4: Response**

- **Cell O4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** O4:R4
- **Fill:** Light Yellow (#FFFFCC)


## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Data Element ID | 15 | Text | Free text (DE-001, DE-002, etc.) |
| B | System ID | 12 | Lookup | Reference System_Inventory!A:A |
| C | System Name | 20 | Lookup | Auto-populate from System_Inventory |
| D | Database/Schema | 18 | Text | Free text (schema name) |
| E | Table Name | 20 | Text | Free text (table name) |
| F | Column/Field Name | 20 | Text | Free text (column name) |
| G | Data Type | 15 | Text | Free text (VARCHAR, INT, DATE, etc.) |
| H | Data Category | 15 | Dropdown | Reference Data_Category_Reference!A:A |
| I | Sample Data (Masked) | 25 | Text | Examples ONLY (no real data) |
| J | Discovery Method | 18 | Dropdown | Manual Review, Data Discovery Tool, Schema Analysis, Application Audit, Other |
| K | Discovery Date | 12 | Date | Date picker |
| L | Populated Rows (Est.) | 15 | Number | Whole numbers |
| M | % Null Values | 10 | Number | 0-100% |
| N | Data Owner | 18 | Text | Reference Data_Owner_Assignment |
| O | Requires Masking? | 15 | Dropdown | Yes, No, Conditional, Under Review |
| P | Masking Status | 15 | Dropdown | ✅ Masked, ⚠️ Partial, ❌ Not Masked, 📋 Planned, N/A |
| Q | Last Verified Date | 12 | Date | Date picker |
| R | Notes | 30 | Text | Free text, wrap text |

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
| A | DE-001 |
| B | SYS-001 |
| C | Customer Database |
| D | public |
| E | customers |
| F | credit_card_number |
| G | VARCHAR(19) |
| H | CAT-FIN |
| I | 1234-XXXX-XXXX-5678 (example) |
| J | Data Discovery Tool |
| K | 10.01.2026 |
| L | 1,250,000 |
| M | 2% |
| N | Chief Data Officer |
| O | Yes |
| P | ✅ Masked |
| Q | 15.01.2026 |
| R | PCI-DSS scope. Masked in all non-prod environments using tokenization. |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic
- **Note:** Cell comment on Row 7: "Example row - replace with actual data"


## Data Entry Rows (Rows 8-107)

**100 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Border:** Thin borders
- **Protection:** Unlocked (user input enabled)


**Dependent Formulas:**

**Column C (System Name) - Auto-populate from System_Inventory:**
```excel
=IFERROR(VLOOKUP(B8,System_Inventory!$A:$B,2,FALSE),"")
```
Explanation: Lookup System ID from column B, return System Name from System_Inventory sheet

**Column M (% Null Values) - Validation:**
```excel
Data Validation: Whole number between 0 and 100
Error Alert: "Enter percentage between 0-100"
```

**Conditional Formatting (Column P - Masking Status):**

- ✅ Masked → Green fill (RGB 198, 239, 206)
- ⚠️ Partial → Yellow fill (RGB 255, 235, 156)
- ❌ Not Masked → Red fill (RGB 255, 199, 206)
- 📋 Planned → Blue fill (RGB 180, 199, 231)
- N/A → Gray fill (RGB 217, 217, 217)


## Data Inventory Checklist (Rows 109-125)

**Row 109: Section Header**

- **Cell A109:** "SENSITIVE DATA INVENTORY CHECKLIST"
- **Merge:** A109:E109
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text


**Row 110: Table Headers**

| Column | Header | Width |
|--------|--------|-------|
| A | # | 5 |
| B | Checklist Item | 50 |
| C | Status | 15 |
| D | Evidence | 25 |
| E | Notes | 25 |

**Rows 111-125: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is field-level inventory complete for all systems? | [Dropdown] | [Text] | [Text] |
| 2 | Are all sensitive data categories documented? | [Dropdown] | [Text] | [Text] |
| 3 | Is discovery method documented per field? | [Dropdown] | [Text] | [Text] |
| 4 | Are data owners assigned to each sensitive field? | [Dropdown] | [Text] | [Text] |
| 5 | Is approximate row count estimated per field? | [Dropdown] | [Text] | [Text] |
| 6 | Are null value percentages documented? | [Dropdown] | [Text] | [Text] |
| 7 | Is masking requirement defined per field? | [Dropdown] | [Text] | [Text] |
| 8 | Is masking status current (<30 days old)? | [Dropdown] | [Text] | [Text] |
| 9 | Are sample data examples provided (masked)? | [Dropdown] | [Text] | [Text] |
| 10 | Is inventory reviewed quarterly? | [Dropdown] | [Text] | [Text] |
| 11 | Are database schema changes tracked? | [Dropdown] | [Text] | [Text] |
| 12 | Are new sensitive fields flagged immediately? | [Dropdown] | [Text] | [Text] |
| 13 | Is data lineage documented (source → target)? | [Dropdown] | [Text] | [Text] |
| 14 | Are third-party data sources inventoried? | [Dropdown] | [Text] | [Text] |
| 15 | Is inventory synchronized with CMDB? | [Dropdown] | [Text] | [Text] |

**Data Validation (Column C):**

- Same status dropdown as System_Inventory checklist
- Same conditional formatting rules


---

# Sheet 5: Classification_Matrix

## Purpose
Apply sensitivity classification to each data element based on impact assessment. Links data elements to classification levels (Critical/High/Medium/Low/Public).

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "DATA SENSITIVITY CLASSIFICATION MATRIX"
- **Merge:** A1:P1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center


**Row 2: Instructions**

- **Cell A2:** "Classify each sensitive data element based on impact if exposed (100 row template)"
- **Merge:** A2:P2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center


**Row 3: Assessment Question**

- **Cell A3:** "Has [Organization] completed sensitivity classification for all sensitive data elements?"
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
| A | Data Element ID | 15 | Lookup | Reference Sensitive_Data_Inventory!A:A |
| B | Field Name | 20 | Auto-populate | From Sensitive_Data_Inventory |
| C | Data Category | 15 | Auto-populate | From Sensitive_Data_Inventory |
| D | Sensitivity Level | 15 | Dropdown | Critical, High, Medium, Low, Public |
| E | Confidentiality Impact | 15 | Dropdown | Severe, Substantial, Moderate, Minimal, None |
| F | Integrity Impact | 15 | Dropdown | Severe, Substantial, Moderate, Minimal, None |
| G | Availability Impact | 15 | Dropdown | Severe, Substantial, Moderate, Minimal, None |
| H | Regulatory Impact | 15 | Dropdown | Legal Breach, Violation, Non-Compliance, Minor, None |
| I | Reputational Impact | 15 | Dropdown | Severe, Substantial, Moderate, Minimal, None |
| J | Financial Impact (€) | 15 | Dropdown | >1M, 100K-1M, 10K-100K, <10K, None |
| K | Classification Rationale | 30 | Text | Explain why this classification |
| L | Classifier Name | 18 | Text | Person who classified |
| M | Classification Date | 12 | Date | Date picker |
| N | Review Date | 12 | Date | Auto-calc: Classification Date + 365 days |
| O | Approved By | 18 | Text | Data Owner or delegate |
| P | Approval Status | 15 | Dropdown | ✅ Approved, ⚠️ Pending, ❌ Rejected, 📋 Under Review |

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
| A | DE-001 |
| B | credit_card_number |
| C | CAT-FIN |
| D | Critical |
| E | Severe |
| F | Substantial |
| G | Moderate |
| H | Legal Breach |
| I | Severe |
| J | >1M |
| K | PCI-DSS cardholder data. Exposure would trigger mandatory breach notification and PCI non-compliance fines. |
| L | CISO |
| M | 10.01.2026 |
| N | 10.01.2027 |
| O | Chief Data Officer |
| P | ✅ Approved |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic


## Data Entry Rows (Rows 8-107)

**100 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked


**Auto-populate Formulas:**

**Column B (Field Name):**
```excel
=IFERROR(VLOOKUP(A8,Sensitive_Data_Inventory!$A:$F,6,FALSE),"")
```

**Column C (Data Category):**
```excel
=IFERROR(VLOOKUP(A8,Sensitive_Data_Inventory!$A:$H,8,FALSE),"")
```

**Column N (Review Date) - Auto-calculate:**
```excel
=IF(ISBLANK(M8),"",DATE(YEAR(M8)+1,MONTH(M8),DAY(M8)))
```
Explanation: Annual review (Classification Date + 365 days)

**Conditional Formatting (Column D - Sensitivity Level):**

- Critical → Red fill (RGB 255, 199, 206)
- High → Orange fill (RGB 255, 235, 156)
- Medium → Yellow fill (RGB 255, 242, 204)
- Low → Light green (RGB 226, 239, 218)
- Public → White (no fill)


**Conditional Formatting (Column P - Approval Status):**

- ✅ Approved → Green fill (RGB 198, 239, 206)
- ⚠️ Pending → Yellow fill (RGB 255, 235, 156)
- ❌ Rejected → Red fill (RGB 255, 199, 206)
- 📋 Under Review → Blue fill (RGB 180, 199, 231)


---

**This completes Response 2 (Sheets 3-5). Shall I continue with Sheet 6 (Regulatory_Mapping), Sheet 7 (Data_Owner_Assignment), and Sheet 8 (Masking_Priority_Matrix) in Response 3?**

## Classification Matrix Checklist (Rows 109-120)

**Row 109: Section Header**

- **Cell A109:** "CLASSIFICATION MATRIX CHECKLIST"
- **Merge:** A109:E109
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text


**Row 110: Table Headers**

| Column | Header | Width |
|--------|--------|-------|
| A | # | 5 |
| B | Checklist Item | 50 |
| C | Status | 15 |
| D | Evidence | 25 |
| E | Notes | 25 |

**Rows 111-120: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is sensitivity level assigned to all data elements? | [Dropdown] | [Text] | [Text] |
| 2 | Is CIA impact (Confidentiality, Integrity, Availability) assessed? | [Dropdown] | [Text] | [Text] |
| 3 | Is regulatory impact documented? | [Dropdown] | [Text] | [Text] |
| 4 | Is classification rationale documented? | [Dropdown] | [Text] | [Text] |
| 5 | Is data owner approval obtained for all classifications? | [Dropdown] | [Text] | [Text] |
| 6 | Are classifications reviewed annually? | [Dropdown] | [Text] | [Text] |
| 7 | Are Critical classifications justified with evidence? | [Dropdown] | [Text] | [Text] |
| 8 | Is classifier name documented per entry? | [Dropdown] | [Text] | [Text] |
| 9 | Are review dates tracked and monitored? | [Dropdown] | [Text] | [Text] |
| 10 | Is classification methodology consistent across all data? | [Dropdown] | [Text] | [Text] |

**Data Validation and Formatting:**

- Same as previous checklists (status dropdown with conditional formatting)


---

# Sheet 6: Regulatory_Mapping

## Purpose
Map sensitive data elements to applicable regulatory requirements (GDPR, FADP, HIPAA, PCI-DSS, etc.). Establishes compliance traceability from data → regulation → control requirement.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "REGULATORY REQUIREMENT MAPPING"
- **Merge:** A1:N1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center


**Row 2: Instructions**

- **Cell A2:** "Map each sensitive data element to applicable regulatory requirements and compliance obligations (50 row template)"
- **Merge:** A2:N2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center


**Row 3: Assessment Question**

- **Cell A3:** "Has [Organization] completed regulatory mapping for all sensitive data subject to compliance requirements?"
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
| A | Data Element ID | 15 | Lookup | Reference Sensitive_Data_Inventory!A:A |
| B | Field Name | 20 | Auto-populate | From Sensitive_Data_Inventory |
| C | Data Category | 15 | Auto-populate | From Sensitive_Data_Inventory |
| D | Applicable Regulations | 25 | Dropdown | GDPR, FADP, HIPAA, PCI-DSS, CCPA, LGPD, SOC 2, ISO 27001, Other (multiple select comma-separated) |
| E | Specific Articles/Requirements | 25 | Text | E.g., "GDPR Art.32, FADP Art.8, PCI-DSS Req.3.4" |
| F | Data Subject Rights Apply? | 15 | Dropdown | Yes (GDPR/FADP), Yes (CCPA), Yes (Other), No, N/A |
| G | Breach Notification Required? | 18 | Dropdown | Yes - Mandatory (72h), Yes - Risk-Based, No, N/A |
| H | Cross-Border Transfer Restrictions? | 20 | Dropdown | Yes - EU/EEA Only, Yes - Adequate Country Only, Yes - SCCs Required, No, N/A |
| I | Data Retention Requirement | 18 | Text | E.g., "7 years (tax law)", "Delete on request (GDPR)" |
| J | Masking Legally Required? | 15 | Dropdown | Yes - Production, Yes - Non-Production Only, No (Best Practice), N/A |
| K | Compliance Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, 📋 Under Review, N/A |
| L | Gap Description | 30 | Text | If non-compliant, describe gap |
| M | Compliance Owner | 18 | Text | Role responsible for compliance |
| N | Last Audit Date | 12 | Date | Date picker |

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
| D | PCI-DSS, GDPR, FADP |
| E | PCI-DSS v4.0 Req.3.4.1, GDPR Art.32(1)(a), FADP Art.8(2) |
| F | Yes (GDPR/FADP) |
| G | Yes - Mandatory (72h) |
| H | Yes - SCCs Required |
| I | Retain during active account + 7 years (audit) |
| J | Yes - Non-Production Only |
| K | ✅ Compliant |
| L | [blank] |
| M | Data Protection Officer |
| N | 10.01.2026 |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic


## Data Entry Rows (Rows 8-57)

**50 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked


**Auto-populate Formulas:**

**Column B (Field Name):**
```excel
=IFERROR(VLOOKUP(A8,Sensitive_Data_Inventory!$A:$F,6,FALSE),"")
```

**Column C (Data Category):**
```excel
=IFERROR(VLOOKUP(A8,Sensitive_Data_Inventory!$A:$H,8,FALSE),"")
```

**Conditional Formatting (Column K - Compliance Status):**

- ✅ Compliant → Green fill (RGB 198, 239, 206)
- ⚠️ Partial → Yellow fill (RGB 255, 235, 156)
- ❌ Non-Compliant → Red fill (RGB 255, 199, 206)
- 📋 Under Review → Blue fill (RGB 180, 199, 231)
- N/A → Gray fill (RGB 217, 217, 217)


## Regulatory Framework Reference (Rows 59-72)

**Row 59: Section Header**

- **Cell A59:** "REGULATORY FRAMEWORK REFERENCE"
- **Merge:** A59:D59
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray


**Rows 60-72: Framework Descriptions**

| Regulation | Jurisdiction | Data Protection Focus | Key Requirements |
|------------|--------------|----------------------|------------------|
| **GDPR** | EU/EEA | Personal data of EU residents | Art.32 security measures, Art.5 data minimization, Art.25 privacy by design |
| **FADP** | Switzerland | Personal data in Switzerland | Art.8 data security, Art.5 proportionality, Art.19 breach notification |
| **HIPAA** | USA | Protected Health Information (PHI) | 45 CFR 164.312(a)(2)(iv) encryption, 164.308 safeguards |
| **PCI-DSS** | Global | Payment card data | Req.3.4 masking PAN, Req.3.5 key management, Req.8 access control |
| **CCPA/CPRA** | California, USA | Personal information of CA residents | Right to deletion, right to opt-out, privacy by design |
| **LGPD** | Brazil | Personal data in Brazil | Art.46 security measures, Art.48 breach notification |
| **SOC 2** | Global | Service organization controls | CC6.1 logical access, CC6.6 encryption, CC6.7 data transmission |
| **ISO 27001** | Global | Information security management | A.8.11 data masking, A.8.24 cryptography, A.8.10 deletion |
| **PIPEDA** | Canada | Personal information in Canada | Safeguards principle, consent principle, accountability |
| **DPA 2018** | UK | Personal data in UK | Schedule 1 processing conditions, Part 2 security |
| **APPI** | Japan | Personal information in Japan | Art.20 security control, Art.23 anonymization |
| **PDPA** | Singapore | Personal data in Singapore | S.24 protection obligation, S.26 notification of breach |

**Column Widths:** A=15, B=15, C=30, D=40

## Regulatory Mapping Checklist (Rows 74-85)

**Row 74: Section Header**

- **Cell A74:** "REGULATORY MAPPING CHECKLIST"
- **Merge:** A74:E74
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text


**Row 75: Table Headers**

| Column | Header | Width |
|--------|--------|-------|
| A | # | 5 |
| B | Checklist Item | 50 |
| C | Status | 15 |
| D | Evidence | 25 |
| E | Notes | 25 |

**Rows 76-85: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Are all applicable regulations identified per data element? | [Dropdown] | [Text] | [Text] |
| 2 | Are specific regulatory articles/requirements documented? | [Dropdown] | [Text] | [Text] |
| 3 | Are data subject rights mapped (access, deletion, portability)? | [Dropdown] | [Text] | [Text] |
| 4 | Are breach notification requirements documented? | [Dropdown] | [Text] | [Text] |
| 5 | Are cross-border transfer restrictions identified? | [Dropdown] | [Text] | [Text] |
| 6 | Are data retention requirements compliance-based? | [Dropdown] | [Text] | [Text] |
| 7 | Is masking legally required or best practice only? | [Dropdown] | [Text] | [Text] |
| 8 | Is compliance status tracked per regulatory requirement? | [Dropdown] | [Text] | [Text] |
| 9 | Is compliance ownership assigned? | [Dropdown] | [Text] | [Text] |
| 10 | Are regulatory audits conducted and documented? | [Dropdown] | [Text] | [Text] |

---

# Sheet 7: Data_Owner_Assignment

## Purpose
Assign formal data ownership for each sensitive data category or element. Establishes accountability for classification decisions, masking approvals, and data governance.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "DATA OWNER ASSIGNMENT & APPROVAL"
- **Merge:** A1:M1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center


**Row 2: Instructions**

- **Cell A2:** "Assign data owners and obtain approval for data classification and masking decisions (30 row template)"
- **Merge:** A2:M2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center


**Row 3: Assessment Question**

- **Cell A3:** "Has [Organization] formally assigned data owners for all sensitive data categories?"
- **Merge:** A3:I3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)


**Row 4: Response**

- **Cell J4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** J4:M4
- **Fill:** Light Yellow (#FFFFCC)


## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Data Category | 15 | Dropdown | Reference Data_Category_Reference!A:A |
| B | Category Name | 20 | Auto-populate | From Data_Category_Reference |
| C | Primary Data Owner | 20 | Text | Name and title (e.g., "Jane Doe - CDO") |
| D | Data Owner Email | 25 | Text | Email validation format |
| E | Data Owner Department | 18 | Text | Free text |
| F | Backup Data Owner | 20 | Text | Name and title |
| G | Data Steward | 20 | Text | Operational contact (optional) |
| H | Assignment Date | 12 | Date | Date picker |
| I | Approval Status | 15 | Dropdown | ✅ Approved, ⚠️ Pending, ❌ Declined, 📋 Under Review |
| J | Classification Approved? | 15 | Dropdown | Yes, No, Pending, N/A |
| K | Masking Approved? | 15 | Dropdown | Yes, No, Pending, N/A |
| L | Last Review Date | 12 | Date | Date picker |
| M | Next Review Date | 12 | Date | Auto-calc: Last Review + 365 days |

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
| A | CAT-FIN |
| B | Financial Data |
| C | Jane Smith - Chief Financial Officer (CFO) |
| D | jane.smith@organization.example |
| E | Finance |
| F | John Doe - VP Finance |
| G | Mary Johnson - Finance Data Steward |
| H | 01.01.2026 |
| I | ✅ Approved |
| J | Yes |
| K | Yes |
| L | 15.01.2026 |
| M | 15.01.2027 |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic


## Data Entry Rows (Rows 8-37)

**30 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked


**Auto-populate Formula:**

**Column B (Category Name):**
```excel
=IFERROR(VLOOKUP(A8,Data_Category_Reference!$A:$B,2,FALSE),"")
```

**Column M (Next Review Date):**
```excel
=IF(ISBLANK(L8),"",DATE(YEAR(L8)+1,MONTH(L8),DAY(L8)))
```
Explanation: Annual review (Last Review + 365 days)

**Data Validation (Column D - Email):**
```excel
Custom formula: =AND(ISNUMBER(FIND("@",D8)),ISNUMBER(FIND(".",D8)))
Error Alert: "Please enter a valid email address"
```

**Conditional Formatting (Column I - Approval Status):**

- ✅ Approved → Green fill (RGB 198, 239, 206)
- ⚠️ Pending → Yellow fill (RGB 255, 235, 156)
- ❌ Declined → Red fill (RGB 255, 199, 206)
- 📋 Under Review → Blue fill (RGB 180, 199, 231)


**Conditional Formatting (Columns J, K - Yes/No/Pending):**

- Yes → Green fill (RGB 198, 239, 206)
- No → Red fill (RGB 255, 199, 206)
- Pending → Yellow fill (RGB 255, 235, 156)
- N/A → Gray fill (RGB 217, 217, 217)


## RACI Matrix (Rows 39-50)

**Row 39: Section Header**

- **Cell A39:** "DATA OWNERSHIP RACI MATRIX"
- **Merge:** A39:E39
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray


**Row 40: RACI Definition**

- **Cell A40:** "R=Responsible, A=Accountable, C=Consulted, I=Informed"
- **Merge:** A40:E40
- **Font:** Calibri 10pt Italic


**Rows 41-50: RACI Table**

| Activity | Data Owner | Data Steward | CISO/Security Team | DPO | IT Operations |
|----------|------------|--------------|-------------------|-----|---------------|
| Data Classification | A | R | C | C | I |
| Masking Decision | A | C | R | C | I |
| Access Control Policy | A | I | R | C | I |
| Data Retention Policy | A | R | C | C | I |
| Breach Response | C | C | R | A | R |
| Regulatory Compliance | A | C | C | A | I |
| Data Quality | A | R | I | I | C |
| Schema Changes | C | R | I | I | A |
| Annual Review | A | R | C | C | I |

**Column Widths:** A=25, B=12, C=12, D=15, E=10, F=12

**Formatting:**

- **Font:** Calibri 10pt
- **Alignment:** Center for RACI letters, Left for Activity column
- **Border:** All borders, thin weight


## Data Owner Assignment Checklist (Rows 52-62)

**Row 52: Section Header**

- **Cell A52:** "DATA OWNER ASSIGNMENT CHECKLIST"
- **Merge:** A52:E52
- **Font:** Calibri 11pt Bold
- **Fill:** Medium Blue (#4472C4), White Text


**Row 53: Table Headers**

| Column | Header | Width |
|--------|--------|-------|
| A | # | 5 |
| B | Checklist Item | 50 |
| C | Status | 15 |
| D | Evidence | 25 |
| E | Notes | 25 |

**Rows 54-62: Checklist Items**

| # | Checklist Item | Status | Evidence | Notes |
|---|----------------|--------|----------|-------|
| 1 | Is a primary data owner assigned for each data category? | [Dropdown] | [Text] | [Text] |
| 2 | Is a backup data owner assigned for each category? | [Dropdown] | [Text] | [Text] |
| 3 | Are data owner roles formally documented (job description)? | [Dropdown] | [Text] | [Text] |
| 4 | Have data owners acknowledged their responsibilities? | [Dropdown] | [Text] | [Text] |
| 5 | Is data owner approval obtained for classifications? | [Dropdown] | [Text] | [Text] |
| 6 | Is data owner approval obtained for masking decisions? | [Dropdown] | [Text] | [Text] |
| 7 | Are data stewards assigned for operational support? | [Dropdown] | [Text] | [Text] |
| 8 | Are data ownership assignments reviewed annually? | [Dropdown] | [Text] | [Text] |
| 9 | Is RACI matrix communicated to all stakeholders? | [Dropdown] | [Text] | [Text] |

---

# Sheet 8: Masking_Priority_Matrix

## Purpose
Prioritize masking implementation efforts based on data sensitivity, exposure risk, regulatory requirements, and business criticality. Generates a risk-weighted priority score (P1/P2/P3/P4).

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "MASKING PRIORITY MATRIX (Risk-Based)"
- **Merge:** A1:Q1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center


**Row 2: Instructions**

- **Cell A2:** "Calculate masking priority using risk-weighted scoring: Priority = (Sensitivity×3) + (Exposure×2) + (Regulatory×2) + (Volume×1) [50 row template]"
- **Merge:** A2:Q2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center


**Row 3: Assessment Question**

- **Cell A3:** "Has [Organization] completed risk-based prioritization for all masking requirements?"
- **Merge:** A3:M3
- **Font:** Calibri 10pt Bold
- **Fill:** Light Yellow (#FFFFCC)


**Row 4: Response**

- **Cell N4:** [Dropdown: Yes / No / Partial / Planned / N/A]
- **Merge:** N4:Q4
- **Fill:** Light Yellow (#FFFFCC)


## Column Headers (Row 6)

| Col | Header | Width | Data Type | Validation |
|-----|--------|-------|-----------|------------|
| A | Data Element ID | 15 | Lookup | Reference Sensitive_Data_Inventory!A:A |
| B | Field Name | 20 | Auto-populate | From Sensitive_Data_Inventory |
| C | Data Category | 15 | Auto-populate | From Sensitive_Data_Inventory |
| D | Sensitivity Level | 15 | Auto-populate | From Classification_Matrix |
| E | Sensitivity Score (1-5) | 12 | Dropdown | 5=Critical, 4=High, 3=Medium, 2=Low, 1=Public |
| F | Exposure Risk | 15 | Dropdown | Very High, High, Medium, Low, Very Low |
| G | Exposure Score (1-5) | 12 | Dropdown | 5=Very High, 4=High, 3=Medium, 2=Low, 1=Very Low |
| H | Regulatory Weight | 15 | Dropdown | Mandatory, High, Medium, Low, None |
| I | Regulatory Score (1-5) | 12 | Dropdown | 5=Mandatory, 4=High, 3=Medium, 2=Low, 1=None |
| J | Data Volume | 15 | Dropdown | Very Large (>1M), Large (100K-1M), Medium (10K-100K), Small (<10K) |
| K | Volume Score (1-4) | 12 | Dropdown | 4=Very Large, 3=Large, 2=Medium, 1=Small |
| L | **Total Priority Score** | 12 | Formula | `=(E×3)+(G×2)+(I×2)+(K×1)` Max=40 |
| M | **Priority Tier** | 12 | Formula | P1 (30-40), P2 (20-29), P3 (10-19), P4 (<10) |
| N | Implementation Status | 15 | Dropdown | ✅ Complete, 🔄 In Progress, ❌ Not Started, 🚫 Blocked |
| O | Target Completion Date | 15 | Date | Date picker |
| P | Assigned To | 18 | Text | Team/person responsible |
| Q | Notes | 25 | Text | Implementation notes |

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
| E | 5 |
| F | High |
| G | 4 |
| H | Mandatory |
| I | 5 |
| J | Very Large (>1M) |
| K | 4 |
| L | 33 |
| M | P1 |
| N | ✅ Complete |
| O | 15.12.2025 |
| P | Security Engineering Team |
| Q | Tokenization implemented in all non-prod environments |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic


## Data Entry Rows (Rows 8-57)

**50 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC) for user input columns
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked for E, G, I, K, N, O, P, Q; Locked for L, M (formulas)


**Auto-populate Formulas:**

**Column B (Field Name):**
```excel
=IFERROR(VLOOKUP(A8,Sensitive_Data_Inventory!$A:$F,6,FALSE),"")
```

**Column C (Data Category):**
```excel
=IFERROR(VLOOKUP(A8,Sensitive_Data_Inventory!$A:$H,8,FALSE),"")
```

**Column D (Sensitivity Level):**
```excel
=IFERROR(VLOOKUP(A8,Classification_Matrix!$A:$D,4,FALSE),"")
```

**Column L (Total Priority Score) - CRITICAL FORMULA:**
```excel
=IF(OR(ISBLANK(E8),ISBLANK(G8),ISBLANK(I8),ISBLANK(K8)),"",
   (E8*3)+(G8*2)+(I8*2)+(K8*1))
```
Explanation: Weighted sum = (Sensitivity×3) + (Exposure×2) + (Regulatory×2) + (Volume×1)
Maximum possible score: (5×3)+(5×2)+(5×2)+(4×1) = 15+10+10+4 = 39

**Column M (Priority Tier) - CRITICAL FORMULA:**
```excel
=IF(ISBLANK(L8),"",
   IF(L8>=30,"P1",
   IF(L8>=20,"P2",
   IF(L8>=10,"P3","P4"))))
```
Explanation:

- P1 (Critical): Score 30-40 → Immediate action required
- P2 (High): Score 20-29 → Implement within 90 days
- P3 (Medium): Score 10-19 → Implement within 180 days
- P4 (Low): Score <10 → Risk-based decision


**Conditional Formatting (Column L - Priority Score):**

- Score ≥30 → Red fill (RGB 255, 199, 206) - P1 Critical
- Score 20-29 → Orange fill (RGB 255, 235, 156) - P2 High
- Score 10-19 → Yellow fill (RGB 255, 242, 204) - P3 Medium
- Score <10 → Light green (RGB 226, 239, 218) - P4 Low


**Conditional Formatting (Column M - Priority Tier):**

- P1 → Red fill (RGB 255, 199, 206), Bold font
- P2 → Orange fill (RGB 255, 235, 156), Bold font
- P3 → Yellow fill (RGB 255, 242, 204)
- P4 → Light green (RGB 226, 239, 218)


**Conditional Formatting (Column N - Implementation Status):**

- ✅ Complete → Green fill (RGB 198, 239, 206)
- 🔄 In Progress → Blue fill (RGB 180, 199, 231)
- ❌ Not Started → Red fill (RGB 255, 199, 206)
- 🚫 Blocked → Dark red fill (RGB 192, 0, 0), White text


## Risk Scoring Guidance (Rows 59-75)

**Row 59: Section Header**

- **Cell A59:** "RISK SCORING GUIDANCE"
- **Merge:** A59:D59
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray


**Rows 60-75: Scoring Tables**

**Sensitivity Score (Rows 61-66):**

| Level | Score | Criteria |
|-------|-------|----------|
| Critical | 5 | Legal breach guaranteed if exposed, severe harm |
| High | 4 | Substantial harm, regulatory violation likely |
| Medium | 3 | Moderate harm, business impact |
| Low | 2 | Minimal harm, internal use only |
| Public | 1 | No confidentiality requirement |

**Exposure Risk Score (Rows 68-73):**

| Risk Level | Score | Criteria |
|------------|-------|----------|
| Very High | 5 | Internet-facing, no access controls, unencrypted |
| High | 4 | Internal network, limited access controls |
| Medium | 3 | Segmented network, access controls in place |
| Low | 2 | Isolated network, strong access controls |
| Very Low | 1 | Air-gapped, encrypted at rest, strict access |

**Regulatory Weight Score (Rows 75-80):**

| Weight | Score | Criteria |
|--------|-------|----------|
| Mandatory | 5 | Legal requirement (PCI-DSS, HIPAA, GDPR Art.32) |
| High | 4 | Regulatory expectation, audit scrutiny |
| Medium | 3 | Industry best practice, compliance framework |
| Low | 2 | Internal policy requirement |
| None | 1 | No regulatory mandate |

**Volume Score (Rows 82-86):**

| Volume | Score | Criteria |
|--------|-------|----------|
| Very Large | 4 | >1 million records |
| Large | 3 | 100,000 - 1 million records |
| Medium | 2 | 10,000 - 100,000 records |
| Small | 1 | <10,000 records |

## Priority Summary Dashboard (Rows 88-100)

**Row 88: Section Header**

- **Cell A88:** "MASKING PRIORITY SUMMARY"
- **Merge:** A88:F88
- **Font:** Calibri 12pt Bold
- **Fill:** Medium Blue (#4472C4), White Text


**Rows 89-100: Summary Statistics**

| Metric | Formula | Target | Status |
|--------|---------|--------|--------|
| **Total Data Elements Assessed** | `=COUNTA(A8:A57)-COUNTBLANK(A8:A57)` | N/A | Info |
| **P1 (Critical Priority) Count** | `=COUNTIF(M8:M57,"P1")` | 0 | Conditional |
| **P2 (High Priority) Count** | `=COUNTIF(M8:M57,"P2")` | <5 | Conditional |
| **P3 (Medium Priority) Count** | `=COUNTIF(M8:M57,"P3")` | <10 | Conditional |
| **P4 (Low Priority) Count** | `=COUNTIF(M8:M57,"P4")` | N/A | Info |
| **Implementation Complete (%)** | `=COUNTIF(N8:N57,"✅ Complete")/COUNTA(N8:N57)*100` | 100% | Conditional |
| **In Progress (%)** | `=COUNTIF(N8:N57,"🔄 In Progress")/COUNTA(N8:N57)*100` | N/A | Info |
| **Not Started (%)** | `=COUNTIF(N8:N57,"❌ Not Started")/COUNTA(N8:N57)*100` | 0% | Conditional |
| **Blocked Items** | `=COUNTIF(N8:N57,"🚫 Blocked")` | 0 | Conditional |
| **Overdue Items** | `=COUNTIFS(O8:O57,"<"&TODAY(),N8:N57,"<>✅ Complete")` | 0 | Conditional |
| **P1 Completion Rate (%)** | `=COUNTIFS(M8:M57,"P1",N8:N57,"✅ Complete")/COUNTIF(M8:M57,"P1")*100` | 100% | Conditional |

**Conditional Formatting (Status Column):**

- Green: Metric meets target
- Yellow: Metric within acceptable range
- Red: Metric below target, action required


---

**This completes Response 3 (Sheets 6-8). Shall I continue with Sheet 9 (Gap_Analysis), Sheet 10 (Evidence_Register), and Sheet 11 (Summary_Dashboard) plus Python script integration notes in Response 4 (final response)?**

# Sheet 9: Gap_Analysis

## Purpose
Document and track gaps in data inventory, classification, ownership assignment, and masking implementation. Provides action plan for remediation.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "GAP ANALYSIS & REMEDIATION TRACKING"
- **Merge:** A1:N1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center


**Row 2: Instructions**

- **Cell A2:** "Document gaps identified during inventory, classification, or ownership assessment (30 row template)"
- **Merge:** A2:N2
- **Font:** Calibri 10pt Italic
- **Fill:** Medium Blue (#4472C4), White Text
- **Alignment:** Center


**Row 3: Assessment Question**

- **Cell A3:** "Are all identified gaps documented with remediation plans and target dates?"
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
| B | Gap Category | 18 | Dropdown | Inventory Gap, Classification Gap, Ownership Gap, Masking Gap, Documentation Gap, Process Gap |
| C | Gap Description | 35 | Text | Detailed description of the gap |
| D | Affected Data/System | 20 | Text | Which data elements or systems are affected |
| E | Risk Level | 12 | Dropdown | Critical, High, Medium, Low |
| F | Business Impact | 25 | Text | Impact if gap not addressed |
| G | Root Cause | 25 | Text | Why does this gap exist? |
| H | Remediation Plan | 30 | Text | Actions to close the gap |
| I | Owner | 18 | Text | Person responsible for remediation |
| J | Target Date | 12 | Date | Date picker |
| K | Status | 15 | Dropdown | ✅ Closed, 🔄 In Progress, ❌ Open, 🚫 Blocked, 📋 Planned |
| L | Actual Closure Date | 12 | Date | Date picker |
| M | Verification Evidence | 25 | Text | How gap closure was verified |
| N | Notes | 25 | Text | Additional comments |

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
| A | GAP-001 |
| B | Masking Gap |
| C | Customer SSN field not masked in UAT environment |
| D | SYS-001 / customers.ssn |
| E | Critical |
| F | Regulatory breach (GDPR, FADP), potential fine, audit finding |
| G | UAT environment refresh process skips masking step |
| H | Update data refresh script to include masking, verify with test restore |
| I | Database Admin Team |
| J | 31.01.2026 |
| K | 🔄 In Progress |
| L | [blank] |
| M | [pending] |
| N | Temporary access restricted to authorized personnel only until resolved |

**Formatting:**

- **Fill:** Light Gray (#E7E6E6)
- **Font:** Calibri 10pt Italic


## Data Entry Rows (Rows 8-37)

**30 Template Rows:**

- **Fill:** Light Yellow (#FFFFCC)
- **Font:** Calibri 10pt Regular
- **Protection:** Unlocked


**Conditional Formatting (Column E - Risk Level):**

- Critical → Red fill (RGB 255, 199, 206)
- High → Orange fill (RGB 255, 235, 156)
- Medium → Yellow fill (RGB 255, 242, 204)
- Low → Light green (RGB 226, 239, 218)


**Conditional Formatting (Column K - Status):**

- ✅ Closed → Green fill (RGB 198, 239, 206)
- 🔄 In Progress → Blue fill (RGB 180, 199, 231)
- ❌ Open → Red fill (RGB 255, 199, 206)
- 🚫 Blocked → Dark red fill (RGB 192, 0, 0), White text
- 📋 Planned → Gray fill (RGB 217, 217, 217)


**Data Validation (Column J - Target Date):**
```excel
Custom: =J8>=TODAY()
Error Alert: "Target date should be in the future"
```

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
| Critical Gaps | `=COUNTIF(E8:E37,"Critical")` | 0 | Conditional |
| High Risk Gaps | `=COUNTIF(E8:E37,"High")` | <3 | Conditional |
| Gaps Closed | `=COUNTIF(K8:K37,"✅ Closed")` | 100% | Conditional |
| Gaps In Progress | `=COUNTIF(K8:K37,"🔄 In Progress")` | N/A | Info |
| Gaps Open | `=COUNTIF(K8:K37,"❌ Open")` | 0 | Conditional |
| Gaps Blocked | `=COUNTIF(K8:K37,"🚫 Blocked")` | 0 | Conditional |
| Overdue Gaps | `=COUNTIFS(J8:J37,"<"&TODAY(),K8:K37,"<>✅ Closed")` | 0 | Conditional |
| Closure Rate (%) | `=COUNTIF(K8:K37,"✅ Closed")/COUNTA(K8:K37)*100` | 100% | Conditional |
| Avg Days to Close | `=AVERAGEIF(L8:L37,"<>"&"",L8:L37-J8:J37)` | <30 | Conditional |
| Critical Gaps Closed (%) | `=COUNTIFS(E8:E37,"Critical",K8:K37,"✅ Closed")/COUNTIF(E8:E37,"Critical")*100` | 100% | Conditional |

---

# Sheet 10: Evidence_Register

## Purpose
Central repository for all compliance evidence supporting data inventory, classification, ownership, and masking implementation.

## Header Section (Rows 1-4)

**Row 1: Sheet Title**

- **Cell A1:** "COMPLIANCE EVIDENCE REGISTER"
- **Merge:** A1:L1
- **Font:** Calibri 14pt Bold, White
- **Fill:** Dark Blue (#003366)
- **Alignment:** Center


**Row 2: Instructions**

- **Cell A2:** "Document all evidence supporting compliance with data masking requirements (40 row template)"
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
| B | Evidence Type | 20 | Dropdown | Schema Documentation, Discovery Report, DPIA, Classification Review, Approval Email, Test Results, Screenshot, Configuration File, Meeting Minutes, Other |
| C | Description | 35 | Text | Brief description of evidence |
| D | Related Requirement | 20 | Text | Policy section or checklist item |
| E | Related Data/System | 20 | Text | Which data elements or systems |
| F | File Location | 30 | Text | File path or document management system reference |
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
| B | Discovery Report |
| C | BigID data discovery scan report for production database |
| D | ISMS-POL-A.8.11, Section 2.1 (Data Classification and Identification) REQ-CLS-010 |
| E | SYS-001 (Customer Database) |
| F | /compliance/data-masking/2026/BigID_Scan_20260110.pdf |
| G | 10.01.2026 |
| H | 7 years |
| I | Data Protection Officer |
| J | Confidential |
| K | 15.01.2026 |
| L | Quarterly scan, next due 10.04.2026 |

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
Explanation: Generates EV-001, EV-002, EV-003, etc. automatically

**Conditional Formatting (Column J - Classification):**

- Restricted → Red fill (RGB 255, 199, 206)
- Confidential → Yellow fill (RGB 255, 235, 156)
- Internal → Light blue (RGB 180, 199, 231)
- Public → White (no fill)


## Evidence Type Definitions (Rows 49-62)

**Row 49: Section Header**

- **Cell A49:** "EVIDENCE TYPE DEFINITIONS"
- **Merge:** A49:C49
- **Font:** Calibri 11pt Bold
- **Fill:** Light Gray


**Rows 50-62: Definitions Table**

| Evidence Type | Description | Examples |
|---------------|-------------|----------|
| Schema Documentation | Database schema, data dictionaries, ERD diagrams | DDL scripts, ER diagrams, data models |
| Discovery Report | Automated data discovery tool output | BigID, Varonis, OneTrust scan reports |
| DPIA | Data Protection Impact Assessment | GDPR Article 35 assessments |
| Classification Review | Classification decision documentation | Review meeting minutes, decision matrices |
| Approval Email | Email approvals from data owners | Classification approvals, masking approvals |
| Test Results | Masking effectiveness test results | Irreversibility tests, format validation |
| Screenshot | Visual evidence of configurations | Masking tool settings, access controls |
| Configuration File | System/tool configuration exports | Masking rules, DDM policies |
| Meeting Minutes | Governance meeting documentation | Data governance meetings, steering committee |
| Other | Any other relevant evidence | Audit reports, third-party assessments |

---

# Sheet 11: Summary_Dashboard

## Purpose
Executive summary consolidating all assessment data into actionable compliance metrics and KPIs.

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


## Overall Compliance Summary (Rows 5-12)

**Row 5: Section Header**

- **Cell A5:** "OVERALL COMPLIANCE STATUS"
- **Merge:** A5:G5
- **Font:** Calibri 14pt Bold
- **Fill:** Medium Blue (#4472C4), White Text


**Rows 6-12: Key Metrics**

| Metric | Formula | Target | Status |
|--------|---------|--------|--------|
| **Systems Inventoried (%)** | `=COUNTIF(System_Inventory!J:J,"✅ Complete")/COUNTA(System_Inventory!A8:A57)*100` | 100% | Conditional |
| **Sensitive Fields Classified (%)** | `=COUNTIF(Classification_Matrix!P:P,"✅ Approved")/COUNTA(Classification_Matrix!A8:A107)*100` | 100% | Conditional |
| **Data Owners Assigned (%)** | `=COUNTIF(Data_Owner_Assignment!I:I,"✅ Approved")/COUNTA(Data_Owner_Assignment!A8:A37)*100` | 100% | Conditional |
| **Masking Implementation (%)** | `=COUNTIF(Masking_Priority_Matrix!N:N,"✅ Complete")/COUNTA(Masking_Priority_Matrix!A8:A57)*100` | 100% | Conditional |
| **Critical Gaps Open** | `=COUNTIFS(Gap_Analysis!E:E,"Critical",Gap_Analysis!K:K,"<>✅ Closed")` | 0 | Conditional |
| **Evidence Documents** | `=COUNTA(Evidence_Register!A8:A47)` | >20 | Conditional |
| **Overall Compliance Score** | `=AVERAGE(B6,B7,B8,B9)` | ≥95% | Conditional |

**Conditional Formatting (Status Column):**

- ≥95% or Target Met → Green fill (RGB 198, 239, 206)
- 80-94% → Yellow fill (RGB 255, 235, 156)
- <80% → Red fill (RGB 255, 199, 206)


## Data Category Breakdown (Rows 14-26)

**Row 14: Section Header**

- **Cell A14:** "DATA CATEGORY COMPLIANCE"
- **Merge:** A14:G14
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray


**Rows 15-26: Category Summary**

| Data Category | Fields Inventoried | Classified | Owner Assigned | Masking Required | Masked | Compliance % |
|---------------|-------------------|------------|----------------|------------------|--------|--------------|
| CAT-PII-D | `=COUNTIF(...)` | `=COUNTIF(...)` | `=COUNTIF(...)` | `=COUNTIF(...)` | `=COUNTIF(...)` | `=Formula` |
| CAT-FIN | Formula | Formula | Formula | Formula | Formula | Formula |
| CAT-HLT | Formula | Formula | Formula | Formula | Formula | Formula |
| CAT-CRD | Formula | Formula | Formula | Formula | Formula | Formula |
| [Additional categories as needed] | | | | | | |

## Regulatory Compliance Summary (Rows 28-34)

**Row 28: Section Header**

- **Cell A28:** "REGULATORY COMPLIANCE STATUS"
- **Merge:** A28:G28
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray


**Rows 29-34: Regulatory Table**

| Regulation | Applicable? | Fields in Scope | Classified | Owner Assigned | Masking Required | Compliance % |
|------------|-------------|-----------------|------------|----------------|------------------|--------------|
| GDPR | `=COUNTIF(...)` | Formula | Formula | Formula | Formula | Formula |
| FADP | Formula | Formula | Formula | Formula | Formula | Formula |
| HIPAA | Formula | Formula | Formula | Formula | Formula | Formula |
| PCI-DSS | Formula | Formula | Formula | Formula | Formula | Formula |
| Other | Formula | Formula | Formula | Formula | Formula | Formula |

## Masking Priority Summary (Rows 36-42)

**Row 36: Section Header**

- **Cell A36:** "MASKING PRIORITY STATUS"
- **Merge:** A36:G36
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray


**Rows 37-42: Priority Table**

| Priority | Count | % Total | Complete | In Progress | Not Started | Blocked | On-Track? |
|----------|-------|---------|----------|-------------|-------------|---------|-----------|
| P1 (Critical) | `=COUNTIF(...)` | Formula | Formula | Formula | Formula | Formula | Formula |
| P2 (High) | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| P3 (Medium) | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| P4 (Low) | Formula | Formula | Formula | Formula | Formula | Formula | Formula |

## Top 10 Gaps (Rows 44-55)

**Row 44: Section Header**

- **Cell A44:** "TOP 10 GAPS REQUIRING ATTENTION"
- **Merge:** A44:G44
- **Font:** Calibri 12pt Bold
- **Fill:** Light Gray


**Rows 45-55: Gap List**

| Rank | Gap ID | Gap Description | Risk Level | Target Date | Owner | Status |
|------|--------|-----------------|------------|-------------|-------|--------|
| 1 | Lookup from Gap_Analysis | Lookup | Lookup | Lookup | Lookup | Lookup |
| 2 | ... | ... | ... | ... | ... | ... |

**Lookup Formula Example (Gap ID):**
```excel
=INDEX(Gap_Analysis!$A:$A,MATCH(LARGE(Gap_Analysis!$E:$E,ROW()-44),Gap_Analysis!$E:$E,0))
```
Explanation: Rank gaps by Risk Level, display top 10

## Key Performance Indicators (Rows 57-68)

**Row 57: Section Header**

- **Cell A57:** "KEY PERFORMANCE INDICATORS"
- **Merge:** A57:E57
- **Font:** Calibri 12pt Bold
- **Fill:** Medium Blue (#4472C4), White Text


**Rows 58-68: KPI Table**

| KPI | Current Value | Target | Status | Trend |
|-----|---------------|--------|--------|-------|
| % Systems Inventoried | Formula | 100% | Conditional | ↑ ↓ → |
| % Sensitive Fields Classified | Formula | 100% | Conditional | Trend |
| % Data Owners Assigned | Formula | 100% | Conditional | Trend |
| % Regulatory Mapping Complete | Formula | 100% | Conditional | Trend |
| % Masking Requirements Defined | Formula | 100% | Conditional | Trend |
| % P1 Items Complete | Formula | 100% | Conditional | Trend |
| Mean Time to Classify (days) | Number | <30 days | Conditional | Trend |
| Inventory Accuracy (last audit) | Number | >95% | Conditional | Trend |
| Open Critical Gaps | Formula | 0 | Conditional | Trend |

## Assessment Sign-Off (Rows 70-78)

**Row 70: Section Header**

- **Cell A70:** "ASSESSMENT APPROVAL & SIGN-OFF"
- **Merge:** A70:E70
- **Font:** Calibri 12pt Bold
- **Fill:** Medium Blue (#4472C4), White Text


**Rows 71-78: Sign-Off Table**

| Role | Name | Signature | Date | Comments |
|------|------|-----------|------|----------|
| Data Governance Lead | [Text] | [Text] | [Date] | [Text] |
| Chief Data Officer (CDO) | [Text] | [Text] | [Date] | [Text] |
| Data Protection Officer (DPO) | [Text] | [Text] | [Date] | [Text] |
| Chief Information Security Officer (CISO) | [Text] | [Text] | [Date] | [Text] |
| Legal/Compliance Officer | [Text] | [Text] | [Date] | [Text] |

**Fill:** Light Yellow (#FFFFCC) for all input cells  
**Protection:** Unlocked for user input

---

# Python Script Integration Notes

## Generator Script: `generate_a811_1_data_inventory.py`

**CRITICAL: THIS IS A SAMPLE SCRIPT TEMPLATE**
```python
"""
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR CONTROL A.8.11

This script generates the ISMS-IMP-A.8.11.1 Data Inventory & Classification 
Assessment Excel workbook.

CUSTOMIZATION REQUIRED:
1. Update sheet structures if taxonomy changes
2. Modify validation dropdowns for organization-specific values
3. Adjust formulas if scoring algorithms change
4. Update data capacity (currently 50-100 rows per sheet)

DO NOT use without reviewing all sections marked "# CUSTOMIZE:"
"""

# Key Functions to Implement:
# - create_workbook(): Initialize workbook with 11 sheets
# - create_instructions_legend(): Sheet 1 with taxonomy reference
# - create_system_inventory(): Sheet 2 with 50 row capacity
# - create_data_category_reference(): Sheet 3 (read-only reference)
# - create_sensitive_data_inventory(): Sheet 4 with 100 row capacity
# - create_classification_matrix(): Sheet 5 with 100 row capacity
# - create_regulatory_mapping(): Sheet 6 with 50 row capacity
# - create_data_owner_assignment(): Sheet 7 with 30 row capacity
# - create_masking_priority_matrix(): Sheet 8 with priority scoring formulas
# - create_gap_analysis(): Sheet 9 with 30 row capacity
# - create_evidence_register(): Sheet 10 with 40 row capacity
# - create_summary_dashboard(): Sheet 11 with consolidated formulas
# - setup_data_validation(): Apply all dropdown validations
# - setup_conditional_formatting(): Apply color-coding rules
# - setup_cell_protection(): Lock formula cells, unlock input cells
```

## Key Customization Points

**1. Data Category Taxonomy (Sheet 3):**
```python
# CUSTOMIZE: Add organization-specific data categories
DATA_CATEGORIES = [
    {"id": "CAT-PII-D", "name": "Direct PII", "sensitivity": "High"},
    {"id": "CAT-FIN", "name": "Financial Data", "sensitivity": "Critical"},
    # Add custom categories here
]
```

**2. Validation Dropdowns:**
```python
# CUSTOMIZE: Modify dropdown options if needed
DROPDOWNS = {
    "system_type": "Database,Application,SaaS,File Share,API,Data Warehouse,Backup System,Archive,Other",
    "environment": "Production,Development,Test/QA,UAT,Training,Analytics,DR/Backup,Decommissioned",
    "status": "✅ Complete,⚠️ Partial,❌ Missing,📋 Planned,N/A"
}
```

**3. Priority Scoring Formula:**
```python
# CUSTOMIZE: Adjust weights if risk model changes
# Current: (Sensitivity×3) + (Exposure×2) + (Regulatory×2) + (Volume×1)
def calculate_priority_score(sensitivity, exposure, regulatory, volume):
    return (sensitivity * 3) + (exposure * 2) + (regulatory * 2) + (volume * 1)
```

**4. Conditional Formatting Thresholds:**
```python
# CUSTOMIZE: Modify color thresholds if needed
COMPLIANCE_THRESHOLDS = {
    "green": 95,  # ≥95% = Green
    "yellow": 80,  # 80-94% = Yellow
    "red": 0       # <80% = Red
}
```

## Quality Assurance Script

**Script:** `validate_a811_1_structure.py`
```python
"""
Quality assurance script to validate generated workbook structure.

Validates:

- All 11 sheets present with correct names
- Column headers match specification
- Data validation rules applied correctly
- Conditional formatting ranges correct
- Formula accuracy (spot checks)
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
| Status - Complete | 198, 239, 206 | #C6EFCE | Light Green |
| Status - Partial | 255, 235, 156 | #FFEB9C | Light Yellow |
| Status - Missing | 255, 199, 206 | #FFC7CE | Light Red |
| Status - Planned | 180, 199, 231 | #B4C7E7 | Light Blue |
| Example Rows | 231, 230, 230 | #E7E6E6 | Light Gray |

## Font Standards

- **Headers:** Calibri 14-16pt Bold
- **Subheaders:** Calibri 11-12pt Bold
- **Column Headers:** Calibri 10pt Bold
- **Data Cells:** Calibri 10pt Regular
- **Example Rows:** Calibri 10pt Italic


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


**Unprotected (Unlocked):**

- All yellow input cells
- All user data entry rows
- Sign-off fields


---

# Workbook Metadata

**File Naming Convention:**  
`ISMS-IMP-A.8.11.1_Data_Inventory_Classification_YYYYMMDD.xlsx`

**Example:**  
`ISMS-IMP-A.8.11.1_Data_Inventory_Classification_20260119.xlsx`

**Excel Document Properties:**
```
Title: ISMS-IMP-A.8.11.1 - Data Inventory & Classification Assessment
Subject: ISO/IEC 27001:2022 Control A.8.11 Data Masking
Author: [Organization Name]
Company: [Organization Name]
Keywords: ISO 27001, Data Masking, Data Classification, Sensitive Data Inventory, A.8.11
Comments: Generated from ISMS policy framework. Do not modify structure without updating generator script.
```

---

# Requirements Traceability Matrix

This workbook assesses compliance with the following policy requirements:

| Policy Requirement | Description | Assessed In Sheet |
|--------------------|-------------|-------------------|
| REQ-CLS-001 | Maintain inventory of sensitive data categories | Sheet 4 (Sensitive_Data_Inventory) |
| REQ-CLS-002 | Classify data per organizational scheme | Sheet 5 (Classification_Matrix) |
| REQ-CLS-003 | Document sensitive data locations | Sheets 2, 4 |
| REQ-CLS-010 | Perform initial data discovery | Sheet 4 (Discovery Method column) |
| REQ-CLS-020 | Maintain living inventory | All sheets (Review Dates) |
| REQ-CLS-030 | Assign Data Owner per category | Sheet 7 (Data_Owner_Assignment) |
| REQ-CLS-031 | Data Owner approves masking | Sheet 7 (Approval Status) |
| REQ-CLS-032 | Annual classification review | Sheet 5 (Review Dates) |
| REQ-REG-001 | Map data to regulatory requirements | Sheet 6 (Regulatory_Mapping) |
| REQ-PRI-001 | Prioritize masking based on risk | Sheet 8 (Masking_Priority_Matrix) |

---

# Document Assembly Instructions

**To create the complete ISMS-IMP-A.8.11.1 document:**

1. **PART I: USER COMPLETION GUIDE** (separate document, ~500 lines)

   - Assessment Overview
   - Prerequisites
   - Assessment Workflow
   - Sheet-by-Sheet Completion Guide
   - Evidence Collection
   - Common Pitfalls
   - Quality Checklist


2. **PART II: TECHNICAL SPECIFICATION** (this document, ~1,500 lines)

   - Document Control
   - Workbook Structure Overview
   - 11 Sheet Specifications (detailed)
   - Python Script Integration Notes
   - Styling & Formatting Standards
   - Quality Assurance Requirements


**Final Combined Document Length:** ~2,000 lines (matching A.8.24 standard)

---

# Quality Assurance Checklist

Before finalizing the workbook, verify:

**Structure:**

- [ ] All 11 sheets present with correct names
- [ ] Sheet order matches specification
- [ ] All column headers match specification exactly
- [ ] Row counts match template specifications


**Data Validation:**

- [ ] All dropdown lists applied correctly
- [ ] Custom validation rules (email, dates) working
- [ ] Error messages appropriate and helpful


**Formulas:**

- [ ] All VLOOKUP formulas reference correct sheets
- [ ] Auto-calculation formulas (dates, scores) accurate
- [ ] Priority scoring formula tested with sample data
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


**Usability:**

- [ ] Example rows present on assessment sheets
- [ ] Cell comments/notes on complex fields
- [ ] Instructions clear and complete
- [ ] Navigation logical and intuitive


---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Final Notes for Implementation Team

**Critical Success Factors:**

1. **Data-Centric Approach:** This assessment focuses on WHAT data exists and WHERE it is, NOT on specific masking tools or products. Keep it vendor-agnostic.

2. **Evidence-Based:** Every classification, every ownership assignment, every masking decision must be documented with evidence. No checkbox compliance theater.

3. **Scalability:** The 50-100 row templates are starting points. Organizations with thousands of data elements should extend templates or create multiple workbooks.

4. **Automation:** The Python generator script is essential for consistency. Manual workbook creation is error-prone and not recommended.

5. **Integration:** This workbook feeds into IMP-A.8.11.2 (Masking Techniques), IMP-A.8.11.3 (Environment Coverage), and ultimately the Compliance Dashboard (IMP-A.8.11.5).

**Next Steps:**

1. Generate Python script from this specification
2. Execute script to create template workbook
3. Validate generated workbook against QA checklist
4. Test with sample organization data
5. Iterate based on usability feedback
6. Deploy to ISMS implementation teams

---

**Document Control:**

- **Version:** 1.0
- **Date:** [Date]
- **Status:** Approved for Implementation
- **Author:** ISMS Implementation Team
- **Approver:** CISO / Chief Data Officer
- **Review Cycle:** Annual or when Control A.8.11 requirements change


---

**END OF SPECIFICATION**

---

*"Quantum physics tells us that reality is far more interconnected than our everyday experience suggests."*
— Alain Aspect

<!-- QA_VERIFIED: 2026-01-31 -->
