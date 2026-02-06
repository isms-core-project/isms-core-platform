**ISMS-IMP-A.8.11.1-UG - Data Inventory & Classification Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.11.1-UG |
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

**END OF USER GUIDE**

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

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
