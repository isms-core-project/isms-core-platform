**ISMS-IMP-A.5.31.2: Regulatory Applicability Assessment Process**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.31: Legal, Statutory, Regulatory and Contractual Requirements

**Document ID**: ISMS-IMP-A.5.31.2
**Title**: Regulatory Applicability Assessment Process  
**Version**: 1.0  
**Related Policy**: ISMS-POL-A.5.31.2 (Regulatory Applicability Methodology)  
**Purpose**: Operational guide for systematically identifying and assessing applicable regulations

---

# PART I: USER COMPLETION GUIDE
**Audience:** Security assessors, Control owners, Compliance officers

---

# Process Overview

## Purpose

This implementation guide operationalizes the regulatory applicability methodology defined in ISMS-POL-A.5.31.2. It provides step-by-step instructions for compliance personnel to systematically identify regulations that may apply to [Organization] and assess whether they are legally binding, conditionally applicable, or informational references.

**What This Guide Is**:

- Operational "how-to" for performing applicability assessments
- Structured process from identification through documentation
- Practical decision-making framework
- Quality assurance checklist


**What This Guide Is Not**:

- Legal advice (always consult legal counsel for interpretation)
- Comprehensive list of regulations (that's ISMS-POL-00)
- Requirements extraction methodology (that's IMP-5.31.2)


## When to Use This Process

**Trigger Events** (from POL-5.31.2 Section 2.1):

1. **New Geographic Market Entry**: [Organization] opens office, registers entity, or begins serving customers in new jurisdiction
2. **New Service Offering**: [Organization] launches new product/service that may trigger sector-specific regulations
3. **New Customer Contract**: Customer contract includes regulatory compliance requirements
4. **Periodic Review**: Annual comprehensive scan of regulatory landscape
5. **Regulatory Alert**: Legal counsel, database, or peer network alerts to new/changed regulation
6. **Business Model Change**: Mergers, acquisitions, restructuring, new data processing activities
7. **Threshold Crossing**: [Organization] grows beyond size/revenue thresholds that trigger regulations

## Who Performs This Process

**Primary Roles**:

- **Compliance Officer**: Leads assessment process, coordinates across functions
- **Legal Counsel**: Provides legal interpretation, reviews determinations, approves Tier 1 regulations
- **ISMS Manager**: Provides input on operational scope, approves additions to ISMS-POL-00


**Supporting Roles**:

- Business Unit Leaders: Provide information on operations, customers, data processing
- Finance: Provide threshold data (revenue, transaction volume, etc.)
- HR: Provide employee location and headcount data
- Sales/Marketing: Provide customer location and targeting data


## Process Flowchart

```
[Trigger Event: New jurisdiction, service, contract, alert, etc.]
         ↓
[STEP 1: Regulatory Identification]

- Search legal databases, regulatory sites, industry sources
- Document candidate regulations

         ↓
[STEP 2: Initial Screening]

- Relevance check (info security related?)
- Jurisdiction check (operate there?)
- Operational check (perform covered activities?)
- Threshold check (meet size requirements?)

         ↓
    Screening Outcome:

    - Not Applicable → Stop, document rationale
    - Uncertain → Proceed to detailed assessment
    - Applicable → Proceed to detailed assessment

         ↓
[STEP 3: Detailed Applicability Assessment]

- Geographic Scope (7 questions)
- Operational Scope (5 questions)
- Contractual Scope (4 questions)
- Score each dimension

         ↓
[STEP 4: Tier Categorization]

- Apply decision framework from POL-5.31.2
- Determine: Tier 1 (Mandatory) / Tier 2 (Conditional) / Tier 3 (Informational)

         ↓
[STEP 5: Documentation & Approval]

- Complete Applicability Assessment Form
- Attach supporting evidence
- Route for approval (workflow per tier)

         ↓
[STEP 6: Add to ISMS-POL-00]

- Create entry in regulatory register
- Assign regulation ID
- Document tier, rationale, next steps
- Communicate to stakeholders

         ↓
[Complete - Proceed to Requirements Extraction (IMP-5.31.2)]
```

## Timeline

**Simple Assessment** (straightforward geographic/operational scope):

- Steps 1-2: 1-2 days
- Step 3: 2-3 days (data gathering)
- Steps 4-6: 1-2 days (documentation, approval)
- **Total**: 1-2 weeks


**Complex Assessment** (requires legal opinion, ambiguous scope, multi-jurisdictional):

- Steps 1-2: 2-3 days
- Step 3: 1-2 weeks (data gathering, legal consultation)
- Steps 4-6: 1-2 weeks (legal review, executive approval for Tier 1)
- **Total**: 4-6 weeks


## Key Artifacts

**Inputs**:

- Trigger event documentation (market entry plan, new contract, regulatory alert)
- Business context (where we operate, what we do, who we serve)


**Process Artifacts**:

- Candidate Regulations List (working document during Step 1)
- Screening Checklist (completed during Step 2)
- Applicability Assessment Form (completed during Step 3-4)


**Outputs**:

- Completed Applicability Assessment (approved)
- Entry in ISMS-POL-00 (if applicable)
- Communication to stakeholders
- If not applicable: Documentation of rationale for future reference


---

# Step 1 - Regulatory Identification

## When to Perform Identification

Perform regulatory identification when any trigger event occurs (per Section 1.2). For periodic reviews, schedule annually in Q4 to inform next year's compliance planning.

## Where to Look for Regulations

Search systematically across multiple sources to ensure comprehensive coverage.

### Source 1: Legal Research Databases

**Commercial Platforms** (LexisNexis, Westlaw, Bloomberg Law, etc.):

**How to Access**:

- Subscription: Contact [Organization] Legal Department for credentials
- URL: [Internal Wiki link to access instructions]
- VPN may be required for off-site access


**Search Process**:
1. Navigate to "Regulatory Compliance" or "Laws & Regulations" section
2. Filter by **Jurisdiction**: Select target jurisdiction(s) (country, state/province, municipality)
3. Filter by **Topic/Practice Area**:

   - Information Security
   - Data Protection / Privacy
   - Cybersecurity
   - Telecommunications (if applicable)
   - Financial Services Regulation (if applicable)
   - Sector-specific as relevant

4. Filter by **Effective Date**: 

   - For new market entry: All active regulations
   - For periodic review: Last 12-24 months (recent changes)

5. Review results list:

   - Read official summaries first (quicker than full text)
   - Note regulation name, citation, effective date
   - Download full text for regulations that appear relevant


**Example Searches**:

- `"data protection" AND "cybersecurity" AND jurisdiction:EU`
- `"information security requirements" AND jurisdiction:"United States" AND topic:"Healthcare"`
- `"breach notification" AND jurisdiction:California AND effectivedate > 2023-01-01`


**Tips**:

- Set up automated alerts for ongoing monitoring (covered in IMP-5.31.4)
- Check both enacted laws AND proposed regulations (early awareness)
- Review regulatory agency interpretations and guidance documents
- Use citator tools to find amendments and related regulations


### Source 2: Government & Regulatory Authority Websites

**Direct from Source**:

**How to Access**:

- Identify regulatory authorities for target jurisdiction:
  - Data Protection Authorities (DPAs)
  - Cybersecurity agencies (e.g., CISA in US, ENISA in EU)
  - Sector regulators (financial, healthcare, telecom, etc.)
- Navigate to authority's official website
- Look for "Laws & Regulations", "Legal Framework", "Compliance" sections


**What to Look For**:

- Official legal texts (laws, regulations, directives, decrees)
- Regulatory guidance and FAQs
- Enforcement actions (reveal regulatory priorities and interpretations)
- Public consultation documents (proposed regulations)


**Example Process** (Data Protection Authority):
1. Visit DPA website for [Target Jurisdiction]
2. Navigate to "Legal Framework" section
3. Identify primary data protection law
4. Review associated regulations, implementing acts, guidance
5. Download official text and guidance documents
6. Note any sector-specific variations

**Tips**:

- Official sources are authoritative (use these to verify commercial database info)
- Subscribe to regulatory authority email lists for updates
- Check for official English translations if regulation in other language
- Note effective dates and any transition periods


### Source 3: Industry Associations & Trade Groups

**Sector-Specific Intelligence**:

**How to Access**:

- Identify industry associations for [Organization]'s sector
- Examples:
  - Technology: TechNet, CCIA, BSA | The Software Alliance
  - Financial Services: ABA, SIFMA, local banking associations
  - Healthcare: HIMSS, local healthcare associations
- Membership often required for full access to regulatory updates


**What to Look For**:

- Regulatory tracking reports (associations monitor regulations affecting members)
- Compliance guides (practical interpretation for sector)
- Advocacy positions (association's view on proposed regulations)
- Member briefings and webinars


**Example Process**:
1. Visit industry association website
2. Navigate to "Policy & Advocacy" or "Regulatory Affairs" section
3. Review recent regulatory updates
4. Download compliance guides for regulations in scope
5. Note association's recommended approach

**Tips**:

- Associations provide sector-specific context commercial databases lack
- Attend association conferences for early regulatory intelligence
- Participate in association working groups (if [Organization] is member)
- Cross-reference association info with official sources (verify)


### Source 4: Legal Counsel (In-House or External)

**Expert Guidance**:

**How to Access**:

- In-House Legal: Contact General Counsel or designated corporate attorney
- External Counsel: Engage law firm by jurisdiction or specialty (data privacy firm, regulatory compliance firm, etc.)


**What to Request**:

- "Regulatory landscape review for [Jurisdiction/Sector]"
- "Identify information security and data protection regulations applicable to [Organization's planned activities in Jurisdiction]"
- Proactive briefing on new or proposed regulations


**Process**:
1. Schedule consultation with legal counsel
2. Provide context:

   - [Organization]'s current and planned operations in jurisdiction
   - Services offered, customers served, data processed
   - Organizational characteristics (size, revenue, structure)

3. Legal counsel researches and briefs on applicable regulations
4. Document legal counsel's findings and recommendations

**Tips**:

- Legal counsel provides interpretation, not just identification
- Use legal counsel for complex or ambiguous regulations
- Document legal opinions for audit trail
- Consider cost (external counsel expensive; use strategically)


### Source 5: Peer Networks & Compliance Forums

**Practical Intelligence**:

**How to Access**:

- Professional networks: LinkedIn groups (Compliance Professionals, Privacy Officers, CISOs)
- Industry ISACs (Information Sharing and Analysis Centers)
- Compliance software communities (Vanta, Drata, etc. user groups)
- Conferences and webinars


**What to Look For**:

- Peer discussions on new regulations ("Has anyone assessed Regulation X for applicability?")
- Implementation experiences ("How are others in our industry handling Regulation Y?")
- Regulatory alerts shared by peers
- Conference presentations on emerging regulatory trends


**Example Process**:
1. Join relevant LinkedIn groups or professional associations
2. Monitor discussions for regulatory mentions
3. Post queries: "Has anyone assessed [Regulation] for [Organization Type]?"
4. Attend compliance-focused conferences and note regulatory sessions

**Tips**:

- Peers provide real-world context and implementation insights
- Always verify peer information against authoritative sources
- Use peers for awareness, not as sole source
- Reciprocate (share your knowledge to build network)


### Source 6: Regulatory Alerts from Subscriptions

**Automated Monitoring**:

**How to Set Up**:

- Legal database alerts (configured during Source 1 access)
- Regulatory authority mailing lists (subscribe during Source 2 research)
- Law firm client alerts (if using external counsel)
- RegTech platform alerts (if [Organization] uses compliance software)


**What to Monitor**:

- New regulations enacted
- Amendments to existing regulations
- Proposed regulations (public comment periods)
- Regulatory guidance issued
- Enforcement actions


**Process**:
1. Configure alerts with specific keywords and jurisdictions
2. Review alerts daily or weekly (depending on volume)
3. Triage: Relevant (add to candidate list) vs. Not Relevant (discard)
4. For relevant alerts, proceed to regulatory identification

**Tips**:

- Alert fatigue is real; configure narrowly (specific jurisdictions and topics)
- Use digest mode (daily/weekly summary) rather than individual alerts
- Designate specific person to monitor and triage alerts
- Integrate alerts into Step 1 workflow (don't let them pile up unreviewed)


## Documenting Candidate Regulations

As you identify potentially relevant regulations, document them in a **Candidate Regulations List** (working document, spreadsheet recommended).

**Columns**:

- **Candidate ID**: Sequential number (CAND-001, CAND-002, etc.)
- **Regulation Name**: Official name
- **Jurisdiction**: Country, state/province, municipality
- **Issuing Authority**: Which government body or regulator issued it
- **Citation**: Official citation (e.g., "Regulation (EU) 2016/679", "California Civil Code § 1798.100")
- **Effective Date**: When regulation became/becomes legally binding
- **Brief Description**: 1-2 sentence summary (what does it regulate?)
- **Source**: Where found (legal database, regulatory authority website, peer alert, etc.)
- **Trigger Event**: What prompted this identification (new market entry, periodic review, alert, etc.)
- **Identified By / Date**: Who identified it and when


**Example Entry**:

| Candidate ID | Regulation Name | Jurisdiction | Authority | Citation | Effective Date | Description | Source | Trigger | Identified By | Date |
|--------------|----------------|--------------|-----------|----------|----------------|-------------|--------|---------|---------------|------|
| CAND-042 | Data Protection Act 2025 | Country X | Data Protection Authority | DPA 2025 | 2025-01-01 | Comprehensive data protection law regulating personal data processing | Legal database (LexisNexis) | Market entry planning for Country X | Compliance Analyst | 2024-11-15 |

**Use This List For**:

- Tracking all candidates identified during Step 1
- Input to Step 2 (screening)
- Audit trail (shows comprehensive identification effort)


---

# Step 2 - Initial Screening

**Purpose**: Quickly filter candidate regulations to focus detailed assessment effort on truly relevant regulations.

## Screening Criteria

For each candidate regulation in the list, answer these screening questions:

### Question 1: Relevance Check

**Is this regulation related to information security, data protection, cybersecurity, or IT services?**

- **YES**: Regulation governs:
  - Information security practices
  - Data protection / privacy
  - Cybersecurity requirements
  - IT service delivery
  - Cloud computing
  - Network security
  - Incident response / breach notification
  - Related topics

- **NO**: Regulation governs unrelated topics:
  - Environmental regulations
  - Labor laws (unless specifically about data protection of employee data)
  - Tax laws
  - Product safety (unless IT products)
  - Unrelated sector regulations


**Decision**:

- If **NO** → **STOP**. Regulation not relevant to ISMS. Document screening outcome and stop.
- If **YES** → Continue to Question 2


### Question 2: Jurisdiction Check

**Does [Organization] have any connection to this jurisdiction?**

Check ALL that apply:

- ☐ [Organization] has physical operations (offices, facilities) in this jurisdiction
- ☐ [Organization] has employees located in this jurisdiction
- ☐ [Organization] serves customers located in this jurisdiction
- ☐ [Organization] processes data of individuals in this jurisdiction
- ☐ [Organization] targets this jurisdiction (website localization, marketing, sales efforts)
- ☐ Regulation claims extraterritorial reach (applies regardless of location if certain criteria met)


**Decision**:

- If **ALL unchecked (no connection)** → Likely **NOT APPLICABLE**. Document screening outcome. STOP unless regulation has extraterritorial provisions.
- If **ANY checked** → Continue to Question 3


### Question 3: Operational Check

**Does [Organization] perform activities or process data types covered by this regulation?**

Check relevant regulation text and compare to [Organization]'s operations:

- ☐ [Organization] provides services that regulation covers (e.g., cloud services, IT consulting, software development)
- ☐ [Organization] serves industry sectors that regulation targets (e.g., financial services, healthcare, government)
- ☐ [Organization] processes data types that regulation governs (e.g., personal data, health records, financial information, payment card data)
- ☐ [Organization] performs specific operations regulation addresses (e.g., e-commerce, telecommunications, payment processing)


**Decision**:

- If **NONE checked** → Likely **NOT APPLICABLE**. [Organization] does not perform activities regulation governs. Document and STOP.
- If **ANY checked** → Continue to Question 4


### Question 4: Threshold Check

**Does this regulation have size, revenue, volume, or other thresholds? If yes, does [Organization] meet them?**

**Common Thresholds**:

- Employee count (e.g., "applies to organizations with 250+ employees")
- Revenue (e.g., "applies to organizations with €10M+ annual revenue")
- Data volume (e.g., "applies if processing data of 50,000+ individuals annually")
- Transaction volume (e.g., "applies if processing 6M+ payment transactions annually")
- Organizational type (e.g., "applies to public companies only", "applies to critical infrastructure operators")


**Check Regulation for Thresholds**:
1. Review regulation text for scope limitations based on organizational characteristics
2. Compare [Organization]'s characteristics to thresholds
3. Document [Organization]'s current status vs. threshold

**Decision**:

- If regulation has **NO thresholds** → Continue to Screening Outcome (proceed to detailed assessment)
- If regulation has thresholds:
  - **[Organization] MEETS thresholds** → Continue to Screening Outcome (proceed)
  - **[Organization] DOES NOT MEET thresholds** → **NOT APPLICABLE currently**
    - Document that regulation not applicable due to threshold
    - **Important**: Monitor [Organization]'s growth; if threshold crossed in future, regulation may become applicable
    - Set reminder to reassess if [Organization] approaching threshold


## Screening Outcome

Based on screening questions:

**Outcome 1: PROCEED TO DETAILED ASSESSMENT**

- Passed all screening checks (relevant, jurisdiction connection, operational match, meets thresholds if any)
- OR: Borderline/uncertain on one or more questions
- **Action**: Move to Step 3 (Detailed Applicability Assessment)


**Outcome 2: NOT APPLICABLE**

- Failed one or more screening checks (not relevant, no jurisdiction connection, no operational match, does not meet thresholds)
- **Action**: 
  - Document screening outcome with rationale
  - File in "Reviewed but Not Applicable" folder
  - Do NOT proceed to detailed assessment
  - Retain documentation (demonstrates due diligence in identifying regulations)
  - Set reminder to reassess if [Organization]'s circumstances change


**Outcome 3: UNCERTAIN**

- Ambiguous language in regulation
- Borderline jurisdiction connection (e.g., small number of customers in jurisdiction)
- Unclear whether [Organization]'s activities match regulation's scope
- **Action**: 
  - Err on side of caution
  - Proceed to Step 3 (Detailed Applicability Assessment)
  - Engage legal counsel for interpretation during Step 3


## Documenting Screening

**Screening Checklist Template**:

For Regulation: [Regulation Name / Candidate ID: CAND-XXX]

| Screening Question | Answer (Y/N) | Evidence / Rationale |
|--------------------|--------------|----------------------|
| **Q1: Relevance** - Related to information security, data protection, cybersecurity, or IT services? | ☐ YES ☐ NO | |
| **Q2: Jurisdiction** - [Org] has connection to jurisdiction (operations, employees, customers, data subjects, targeting, extraterritorial)? | ☐ YES ☐ NO | |
| **Q3: Operational** - [Org] performs activities or processes data types covered by regulation? | ☐ YES ☐ NO | |
| **Q4: Threshold** - [Org] meets any size/revenue/volume thresholds (or regulation has no thresholds)? | ☐ YES ☐ NO ☐ N/A | |

**Screening Outcome**: ☐ Proceed to Detailed Assessment ☐ Not Applicable ☐ Uncertain (proceed to detailed)

**Rationale** (if Not Applicable):

**Next Steps**:

- If Proceed/Uncertain: Begin Step 3
- If Not Applicable: File documentation, update Candidate Regulations List status


**Screened By**: [Name/Role] **Date**: [Date]

---

# Step 3 - Detailed Applicability Assessment

**Purpose**: Systematically assess regulation across three dimensions (Geographic, Operational, Contractual) to determine applicability.

**Reference**: POL-5.31.2 Section 3 defines the methodology; this guide provides operational instructions.

## Geographic Scope Assessment

**Instructions**:
1. Review regulation text for geographic scope provisions (typically in early articles defining "scope" or "territorial application")
2. Gather evidence for [Organization]'s geographic footprint
3. Answer each question below with **YES** or **NO**
4. For each **YES**, document specific evidence
5. Calculate Geographic Applicability Score

**Question G1: Does [Organization] have physical operations in [Regulation's Jurisdiction]?**

- Physical operations: Offices, data centers, facilities, warehouses, storefronts
- **Evidence to Gather**:
  - Office location list (from HR or Facilities)
  - Legal entity registrations (from Legal/Finance)
  - Property leases or deeds
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "Office at 123 Main Street, City X, Country X - lease dated 2024-01-15"]


**Question G2: Does [Organization] have legal entities registered in [Regulation's Jurisdiction]?**

- Legal entities: Subsidiaries, branches, representative offices
- **Evidence to Gather**:
  - Corporate structure chart
  - Business registry records (Chamber of Commerce, Companies House, etc.)
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "[Organization] Country X GmbH, registration #12345678, registered 2024-02-01"]


**Question G3: Does [Organization] have employees located in [Regulation's Jurisdiction]?**

- Employees: Full-time, part-time, contractors physically located in jurisdiction
- **Evidence to Gather**:
  - Headcount report by location (from HR)
  - Payroll records showing local tax withholding
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "15 employees (10 FTE, 5 contractors) located in Country X per HR report dated 2024-11-01"]


**Question G4: Does [Organization] serve customers physically located in [Regulation's Jurisdiction]?**

- Customers: Individuals or organizations with primary location in jurisdiction
- **Evidence to Gather**:
  - Customer list filtered by location (from CRM)
  - Sales by region report (from Finance/Sales)
  - Customer contracts with address information
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "127 active customers with billing addresses in Country X, representing €1.2M annual revenue"]


**Question G5: Does [Organization] process data of individuals (data subjects) in [Regulation's Jurisdiction]?**

- Data subjects: Individuals whose personal data [Organization] processes, regardless of customer status
- Examples: Website visitors, app users, employee applicants, customer contacts
- **Evidence to Gather**:
  - Data processing records (from DPO or Privacy team)
  - Data subject location analysis (from data processing systems)
  - Web analytics (visitor geographic data)
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "Process personal data of ~50,000 website visitors from Country X monthly per Google Analytics"]


**Question G6: Does [Organization] target customers or users in [Regulation's Jurisdiction]?**

- Targeting indicators:
  - Website localized for jurisdiction (language, currency, local payment methods)
  - Marketing campaigns directed at jurisdiction
  - Social media advertising targeted to jurisdiction
  - Local domain name (e.g., .de for Germany, .fr for France)
  - Local phone numbers or support
- **Evidence to Gather**:
  - Website localization settings
  - Marketing campaign targeting data (from Marketing)
  - Domain registrations
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "Website available in Country X language, accepts local currency, Google Ads campaigns targeted to Country X"]


**Question G7: Does the regulation claim extraterritorial application?**

- Extraterritorial reach: Regulation applies regardless of [Organization]'s location if certain criteria met
- Common examples:
  - GDPR: Applies if offering goods/services to EU data subjects OR monitoring EU data subjects, even if organization not in EU
  - Some financial regulations: Apply if processing transactions in certain currencies, even if not in jurisdiction
- **Evidence to Gather**:
  - Regulation text analysis (read territorial scope provisions)
  - Legal counsel opinion on extraterritorial application
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "Regulation Article 3(2) states applies to processing of data subjects in Country X regardless of processor location"]


**Geographic Applicability Score**:

- Count **YES** answers: _____ / 7
- **Interpretation**:
  - **0-1 YES**: Low geographic applicability (minimal connection to jurisdiction)
  - **2-3 YES**: Moderate geographic applicability (some connection)
  - **4+ YES**: High geographic applicability (strong connection to jurisdiction)


**Document in**: Applicability Assessment Form - Section 2: Geographic Scope

## Operational Scope Assessment

**Instructions**:
1. Review regulation text for operational scope provisions (which activities, services, data types does it regulate?)
2. Gather evidence about [Organization]'s operations, services, customers, data processing
3. Answer each question below with **YES** or **NO**
4. For each **YES**, document specific evidence
5. Calculate Operational Applicability Score

**Question O1: Does [Organization] provide services that this regulation specifically addresses?**

- Identify service types regulation governs
- Compare to [Organization]'s service catalog
- **Common Service Types in Regulations**:
  - Cloud computing services (IaaS, PaaS, SaaS)
  - IT consulting and professional services
  - Software development
  - Managed security services
  - Data center hosting
  - Telecommunications
  - Payment processing
- **Evidence to Gather**:
  - Service catalog or product list
  - SOW (Statement of Work) examples from customer contracts
  - Marketing materials describing services
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "[Organization] provides SaaS platform and cloud infrastructure services, both explicitly covered by Regulation Section 4"]


**Question O2: Does [Organization] serve industry sectors that this regulation targets?**

- Sector-specific regulations (financial services, healthcare, government, energy, etc.)
- **Evidence to Gather**:
  - Customer list categorized by industry vertical (from CRM)
  - Revenue by sector (from Finance)
  - Customer contracts showing sector affiliation
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "35% of revenue from financial services customers; regulation specifically targets financial sector"]


**Question O3: Does [Organization] process data types that this regulation governs?**

- Data types commonly regulated:
  - Personal data / Personally Identifiable Information (PII)
  - Sensitive personal data (health, biometric, genetic, race, religion, etc.)
  - Financial data (account numbers, payment card data, transaction records)
  - Children's data
  - Government data / Classified information
  - Intellectual property
- **Evidence to Gather**:
  - Data inventory or data classification register
  - Data processing agreements with customers
  - Privacy notices or data protection impact assessments
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "Process personal data (names, emails, IP addresses) of EU data subjects; regulation governs personal data processing"]


**Question O4: Does [Organization]'s size, revenue, or other characteristics meet regulation's scope criteria?**

- Organizational characteristics that may trigger regulations:
  - **Size thresholds**: Number of employees (e.g., 50+, 250+, 1000+)
  - **Revenue thresholds**: Annual revenue (e.g., €10M+, $50M+)
  - **Data volume thresholds**: Number of data subjects (e.g., 10,000+, 50,000+)
  - **Transaction thresholds**: Payment volume (e.g., 6M+ card transactions annually)
  - **Organizational type**: Public company, private, non-profit, government contractor, critical infrastructure
- **Evidence to Gather**:
  - Financial reports (revenue, profit)
  - Headcount reports (from HR)
  - Data subject counts (from data processing systems)
  - Transaction volume (from payment processing systems)
  - Organizational structure (from Legal)
- **Answer**: ☐ YES ☐ NO ☐ N/A (regulation has no thresholds)
- **If YES or N/A, Evidence**: [e.g., "[Organization] has 350 employees, exceeds regulation's 250+ employee threshold per Article 5"]


**Question O5: Does [Organization] perform specific operations that regulation addresses?**

- Specific operational triggers:
  - E-commerce (selling goods/services online)
  - Cross-border data transfers
  - Automated decision-making / AI/ML
  - Profiling of individuals
  - Large-scale systematic monitoring
  - Telecommunications services
  - Payment services
  - Outsourcing / subprocessing
- **Evidence to Gather**:
  - Business model documentation
  - Data flow diagrams
  - Technology architecture (use of AI, automated systems)
  - Service descriptions
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "Platform uses automated recommendation algorithms qualifying as 'profiling' under regulation's definition (Article 22)"]


**Operational Applicability Score**:

- Count **YES** answers (exclude N/A): _____ / 5
- **Interpretation**:
  - **0-1 YES**: Low operational applicability (operations don't match regulation's scope)
  - **2-3 YES**: Moderate operational applicability (some operational alignment)
  - **4-5 YES**: High operational applicability (operations strongly align with regulation)


**Document in**: Applicability Assessment Form - Section 3: Operational Scope

## Contractual Scope Assessment

**Instructions**:
1. Review customer contracts, master service agreements, SLAs
2. Identify contractual obligations related to this regulation
3. Answer each question below with **YES** or **NO**
4. For each **YES**, document specific evidence
5. Calculate Contractual Applicability Score

**Question C1: Do customer contracts explicitly require compliance with this regulation?**

- Review contract clauses for specific regulatory references
- **Common Contract Language**:
  - "Supplier shall comply with [Regulation Name]"
  - "Supplier shall maintain compliance with all applicable data protection laws including [Regulation]"
  - "Supplier warrants compliance with [Regulation]"
- **Evidence to Gather**:
  - Customer contracts (review data protection, security, compliance clauses)
  - Master service agreements (MSAs)
  - Data processing agreements (DPAs)
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "15 customer contracts (23% of revenue) explicitly require [Regulation] compliance in Section 12 'Regulatory Compliance'"]


**Question C2: Do customer contracts require certifications or attestations related to this regulation?**

- Certifications evidencing regulatory compliance:
  - ISO 27001 (often required for European customers)
  - SOC 2 Type II
  - Specific regulatory certifications (e.g., HIPAA compliance attestation, PCI DSS certification)
- **Evidence to Gather**:
  - Contract requirements for certifications
  - RFP responses where certifications requested
  - Customer due diligence questionnaires
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "8 customer contracts require ISO 27001 certification; regulation is basis for many ISO 27001 control requirements"]


**Question C3: Do customer contracts grant audit rights that would examine compliance with this regulation?**

- Audit clauses allowing customer to verify compliance
- **Common Audit Rights**:
  - "Customer may audit Supplier's compliance with [Regulation] annually"
  - "Customer may request attestation of compliance"
  - "Customer may review security and compliance documentation"
- **Evidence to Gather**:
  - Customer contracts (review audit rights clauses)
  - Audit clause summaries
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "12 contracts grant customer right to audit [Organization]'s data protection practices, would include [Regulation] compliance"]


**Question C4: Is compliance with this regulation a competitive requirement or customer expectation in [Organization]'s market?**

- Market expectations even if not contractually mandated
- **Indicators**:
  - RFPs consistently ask about this regulation
  - Competitors advertise compliance with this regulation
  - Industry standards reference this regulation
  - Sales team reports customers asking about compliance
- **Evidence to Gather**:
  - RFP requirements analysis (from Sales)
  - Competitor websites and marketing materials
  - Sales team feedback (lost deals due to compliance gaps)
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "75% of RFPs in EU market request [Regulation] compliance confirmation; competitors prominently display compliance on websites"]


**Contractual Applicability Score**:

- Count **YES** answers: _____ / 4
- **Interpretation**:
  - **0 YES**: No contractual drivers (regulation not in contracts or market expectations)
  - **1-2 YES**: Moderate contractual drivers (some contracts or market pressure)
  - **3-4 YES**: High contractual drivers (strong contractual and market requirements)


**Document in**: Applicability Assessment Form - Section 4: Contractual Scope

## Overall Applicability Determination

**Combine the Three Dimensions**:

Review scores from Sections 4.1, 4.2, 4.3:

- Geographic Applicability Score: _____ / 7 → Low / Moderate / High
- Operational Applicability Score: _____ / 5 → Low / Moderate / High
- Contractual Applicability Score: _____ / 4 → None / Moderate / High


**Determination Framework** (from POL-5.31.2 Section 3.4):

**APPLICABLE if**:

- Geographic = Moderate or High AND Operational = Moderate or High
- OR: Geographic = High (strong jurisdictional connection) regardless of operational
- OR: Contractual = High (strong contractual obligation) regardless of geographic/operational


**CONDITIONALLY APPLICABLE if**:

- Geographic = Low but Operational = Moderate/High (could become applicable if enter jurisdiction)
- OR: Geographic = Moderate but Operational = Low (monitoring for business changes)
- OR: Contractual = Moderate (some contracts require, considering for broader adoption)


**NOT APPLICABLE if**:

- Geographic = Low AND Operational = Low AND Contractual = None/Low
- Clear mismatch (regulation addresses activities [Organization] does not perform)


**UNCERTAIN - Escalate to Legal Counsel if**:

- Borderline scores (e.g., Geographic = Moderate, Operational = Moderate, Contractual = Low)
- Ambiguous regulation language
- Novel regulatory approach with no precedent
- High legal or business risk if determination wrong


**Document Determination**:

- **Determination**: ☐ Applicable ☐ Conditionally Applicable ☐ Not Applicable ☐ Uncertain (legal review needed)
- **Rationale** (2-3 sentences explaining determination based on scores and evidence):


---

# Step 4 - Tier Categorization

**Purpose**: If regulation is Applicable or Conditionally Applicable, assign it to the appropriate tier in ISMS-POL-00.

**Reference**: POL-5.31.2 Section 4 defines tiers; this guide provides decision process.

## Tier Decision Framework

**For Regulations Determined APPLICABLE**:

**Assign Tier 1 (Mandatory Compliance) if ANY of**:
1. Legal obligation in jurisdiction where [Organization] operates (physical presence, legal entities, employees)
2. Required by law to serve customers in jurisdiction (e.g., GDPR for serving EU customers)
3. Required by contract with significant customers (>10% revenue, critical customers, government contracts)
4. Sector-specific regulation in sector where [Organization] operates (e.g., financial services reg, healthcare reg)

**Examples**:

- Data protection law in country where [Organization] has office → Tier 1
- Breach notification law for data processed by [Organization] → Tier 1
- PCI DSS because [Organization] processes payment cards → Tier 1 (contractual obligation with card brands)


**Assign Tier 2 (Conditional Applicability) if**:
1. Regulation WOULD apply IF [Organization] enters market, launches service, or crosses threshold
2. Not currently legally obligated but potential future obligation
3. Required by some customer contracts but not broadly (spot requirement)

**Examples**:

- Sector regulation for sector [Organization] considering entering → Tier 2
- Regulation with threshold [Organization] does not currently meet but may in future → Tier 2
- Regulation in jurisdiction where [Organization] may expand → Tier 2


**For Regulations Determined CONDITIONALLY APPLICABLE**:

- Assign **Tier 2** by default
- Monitor for condition triggering Tier 1 status


**For Informational References** (voluntary frameworks, not legal obligations):

**Assign Tier 3 if**:
1. Best practice framework [Organization] uses for guidance (NIST CSF, CIS Controls, etc.)
2. Industry standard [Organization] references for control design
3. Regulatory framework from other jurisdiction used for benchmarking

**Examples**:

- NIST Cybersecurity Framework (US) used by non-US organization for maturity assessment → Tier 3
- ISO 27002 guidance (not certification requirement itself) → Tier 3
- Foreign regulation used to inform control design but no legal obligation → Tier 3


## Documenting Tier Assignment

**In Applicability Assessment Form**:

- **Tier Assignment**: ☐ Tier 1 (Mandatory) ☐ Tier 2 (Conditional) ☐ Tier 3 (Informational)
- **Tier Rationale** (explain why this tier):


**Example Rationales**:

- **Tier 1**: "Legal obligation because [Organization] has office in Country X and regulation applies to all entities operating in Country X"
- **Tier 2**: "Conditional because [Organization] does not currently serve healthcare sector, but regulation would apply if healthcare services launched per 2025 strategic plan"
- **Tier 3**: "Informational because NIST CSF is voluntary framework used for maturity benchmarking, not legal requirement"


## Escalation for Tier 1

**Tier 1 assignments require heightened approval** (per POL-5.31.1 governance):

- Legal Counsel review (confirm legal obligation)
- Executive Management approval (significant compliance investment)


Before finalizing Tier 1:
1. Schedule legal counsel review
2. Present applicability assessment evidence
3. Obtain legal confirmation of Tier 1 status
4. Brief Executive Management (may require budget, resources for compliance)
5. Obtain executive approval for Tier 1 addition

**Tier 2 and Tier 3**:

- ISMS Manager or Compliance Officer approval sufficient


---

# Step 5 - Documentation & Approval

## Complete Applicability Assessment Form

**Use Template**: Assessment Workbook 2 (Applicability Matrix) provides Excel template.

**Form Sections** (summary of previous steps):

**Section 1: Regulation Identification**

- Regulation name, jurisdiction, authority, citation, effective date
- Brief description, source where identified, trigger event


**Section 2: Geographic Scope Assessment**

- Questions G1-G7 with YES/NO answers and evidence
- Geographic Score and interpretation


**Section 3: Operational Scope Assessment**

- Questions O1-O5 with YES/NO answers and evidence
- Operational Score and interpretation


**Section 4: Contractual Scope Assessment**

- Questions C1-C4 with YES/NO answers and evidence
- Contractual Score and interpretation


**Section 5: Overall Determination**

- Applicable / Conditionally Applicable / Not Applicable / Uncertain
- Rationale (2-3 sentences)


**Section 6: Tier Assignment** (if applicable)

- Tier 1 / Tier 2 / Tier 3
- Tier rationale


**Section 7: Supporting Evidence**

- Attach or link to all evidence documents
- Examples: Contracts, financial reports, regulation text, legal opinion


**Section 8: Approval Signatures**

- Prepared By / Date: [Compliance Analyst who performed assessment]
- Reviewed By / Date: [Compliance Officer or ISMS Manager]
- Legal Review / Date: [Legal Counsel, required for Tier 1]
- Approved By / Date: [Executive Management for Tier 1, ISMS Manager for Tier 2/3]


## Attach Supporting Evidence

Gather and attach all evidence documents:

- Office location lists, legal entity registrations
- Customer lists and revenue reports
- Data processing records
- Contracts excerpts (data protection clauses)
- Regulation text (official download or link)
- Legal counsel opinion (if obtained)


**Evidence Naming Convention**: `[Regulation-Name]_[Evidence-Type]_[Date]`

- Example: `CountryX-DPA_Customer-List_2024-11-15.xlsx`
- Example: `CountryX-DPA_Legal-Opinion_2024-11-20.pdf`


## Route for Approval

**Approval Workflow**:

**For Tier 1**:
1. Compliance Analyst completes assessment
2. Compliance Officer reviews (confirms methodology followed, evidence adequate)
3. Legal Counsel reviews (confirms legal obligation, tier assignment correct)
4. Present to Executive Management (briefing on regulation, implications, resource needs)
5. Executive approves
6. All signatures obtained on assessment form

**Timeline**: 2-4 weeks (allow time for legal review and executive scheduling)

**For Tier 2 or Tier 3**:
1. Compliance Analyst completes assessment
2. Compliance Officer or ISMS Manager reviews and approves
3. Signature obtained on assessment form

**Timeline**: 3-5 business days

**Approval Evidence**:

- Signed assessment form (physical or electronic signature)
- Email approvals (acceptable if signature not feasible)
- Meeting minutes (for executive approval of Tier 1)


---

# Step 6 - Add to ISMS-POL-00

**If Determination = Applicable or Conditionally Applicable**: Add to ISMS-POL-00 (Regulatory Applicability Framework).

**If Determination = Not Applicable**: Do NOT add to ISMS-POL-00. File assessment for reference.

## Create Entry in ISMS-POL-00

**Reference**: ISMS-POL-00 for current format and structure.

**Entry Fields**:

**Regulation ID**: Assign unique identifier

- Format: REG-[Jurisdiction-Code]-[Sequence]
- Examples: REG-EU-001, REG-US-CA-005, REG-CH-002
- Sequential within jurisdiction


**Regulation Name**: Official full name

**Short Name / Acronym**: Commonly used abbreviation (if exists)

- Examples: GDPR, CCPA, HIPAA, SOX, PCI DSS


**Jurisdiction**: Country, state/province, or multi-jurisdictional

**Issuing Authority**: Government body or regulator

**Citation**: Official citation

**Effective Date**: When regulation became binding

**Tier**: 1 (Mandatory) / 2 (Conditional) / 3 (Informational)

**Applicability Rationale**: 1-2 sentence summary (why this tier?)

- Reference applicability assessment ID for full details


**Key Requirements** (high-level summary): 2-3 bullet points

- Brief overview of main obligations
- Full requirements extraction in IMP-5.31.2 process


**Applicability Condition** (for Tier 2): What condition would trigger Tier 1 status?

- Example: "Applies if [Organization] processes payment cards" (for PCI DSS)
- Example: "Applies if [Organization] enters healthcare sector" (for healthcare regulation)


**Related Regulations**: Any overlapping or related regulations already in POL-00

- Cross-reference to show regulatory ecosystem


**Assessment Reference**: Link to completed Applicability Assessment Form

- Enables audit trail back to detailed analysis


**Next Review Date**: When to reassess applicability

- Tier 1: Annually
- Tier 2: Annually or when condition may be triggered
- Tier 3: Biennially


**Responsible Party**: Who monitors this regulation (typically Compliance Officer)

## Update ISMS-POL-00 Version

**Version Control**:

- Increment version number (e.g., v1.5 → v1.6 for minor addition)
- Update "Last Updated" date
- Add entry to POL-00 version history table


**Version History Entry**:
| Version | Date | Updated By | Changes |
|---------|------|------------|---------|
| 1.6 | 2024-11-30 | Compliance Officer | Added REG-EU-015: Country X Data Protection Act (Tier 1) |

## File Assessment Documentation

**Store Completed Assessment**:

- Central compliance repository (SharePoint, document management system, etc.)
- Folder structure: `/Regulatory-Assessments/[Year]/[Regulation-ID]_[Regulation-Name]/`
- Include:
  - Completed Applicability Assessment Form
  - All supporting evidence documents
  - Approval records (signed forms, email approvals, meeting minutes)


**Retention**: Indefinitely for Tier 1 regulations; 7 years for Tier 2/3 or Not Applicable determinations

## Communicate to Stakeholders

**Notification Template** (adapt based on tier and impact):

**Subject**: New Regulation Added to ISMS-POL-00: [Regulation Name] (Tier [1/2/3])

**To**: ISMS Team, Legal Counsel, Executive Management (Tier 1), Control Owners (if requirements identified)

**Body**:

```
Team,

A new regulation has been assessed and added to the Regulatory Applicability Framework (ISMS-POL-00):

REGULATION DETAILS:

- Name: [Full Regulation Name]
- Regulation ID: REG-XXX
- Jurisdiction: [Jurisdiction]
- Tier: [1 - Mandatory / 2 - Conditional / 3 - Informational]
- Effective Date: [Date]


APPLICABILITY RATIONALE:
[2-3 sentences explaining why this regulation applies and tier assignment]

KEY REQUIREMENTS (High-Level):

- [Requirement 1 summary]
- [Requirement 2 summary]
- [Requirement 3 summary]


NEXT STEPS:

- [For Tier 1]: Requirements extraction scheduled for [Date] (IMP-5.31.2 process)
- [For Tier 1]: Control mapping and gap analysis to follow (IMP-5.31.3 process)
- [For Tier 2]: Monitoring for [Condition that would trigger Tier 1]
- [For Tier 3]: Reference for control design and maturity assessment


DOCUMENTATION:

- Full assessment: [Link to assessment document]
- ISMS-POL-00 entry: [Section X.Y]


IMPACT:
[For Tier 1]: This is a mandatory compliance obligation. Implementation planning will begin immediately. Resource needs will be assessed and communicated.
[For Tier 2]: This regulation is conditionally applicable and monitored. No immediate action required.
[For Tier 3]: This is an informational reference. Use for benchmarking and best practices.

QUESTIONS:
Contact [Compliance Officer] at [email] with questions.

[Signature]
Compliance Officer
```

**Distribution**:

- **Tier 1**: Broad distribution (all stakeholders, executive team)
- **Tier 2**: Targeted distribution (compliance team, business unit planning specific condition)
- **Tier 3**: Minimal distribution (compliance team, relevant technical teams)


---

# Worked Examples

## Example 1: Data Protection Regulation in New Operating Jurisdiction

**Scenario**: [Organization] opens a sales office in Country X to better serve customers in that market. Country X has a comprehensive data protection law similar to GDPR.

**Trigger**: New jurisdiction entry (office opening)

**Step 1 - Identification**:

- Source: Legal database (LexisNexis) and Country X Data Protection Authority website
- Regulation Identified: Data Protection Act of Country X (DPA-CX)
- Candidate ID: CAND-042


**Step 2 - Screening**:

- Relevance: YES (data protection regulation, directly relevant to ISMS)
- Jurisdiction: YES ([Organization] now has office in Country X)
- Operational: YES ([Organization] processes personal data)
- Threshold: N/A (regulation applies to all data controllers/processors)
- **Outcome**: Proceed to detailed assessment


**Step 3 - Detailed Assessment**:

*Geographic Scope*:

- G1 (Physical operations): YES - Office at 456 Business Blvd, City X, Country X
- G2 (Legal entities): YES - [Organization] Country X LLC, registration #CX-987654
- G3 (Employees): YES - 8 employees (6 sales, 2 admin) in Country X office
- G4 (Customers located): YES - 45 customers with primary address in Country X
- G5 (Data subjects): YES - Process personal data of Country X customers and website visitors
- G6 (Targeting): YES - Website has Country X language version, local payment methods
- G7 (Extraterritorial): NO - Regulation applies based on territorial presence, not extraterritorial
- **Score**: 6/7 = **HIGH**


*Operational Scope*:

- O1 (Services): YES - [Organization] provides SaaS platform, regulation governs data processing services
- O2 (Sectors): YES - [Organization] serves financial services customers in Country X, regulation has financial sector provisions
- O3 (Data types): YES - Process personal data (names, emails, addresses, usage data)
- O4 (Thresholds): N/A - No thresholds, applies to all processors
- O5 (Specific operations): YES - Automated decision-making in platform falls under regulation's AI provisions
- **Score**: 4/5 = **HIGH**


*Contractual Scope*:

- C1 (Explicit contracts): YES - 12 Country X customer contracts require DPA-CX compliance
- C2 (Certifications): YES - 8 contracts require ISO 27001, which incorporates data protection requirements
- C3 (Audit rights): YES - 5 contracts grant customer audit rights for data protection practices
- C4 (Market expectations): YES - All RFPs from Country X customers ask for DPA-CX compliance confirmation
- **Score**: 4/4 = **HIGH**


**Determination**: **APPLICABLE**

- Rationale: High geographic (6/7), high operational (4/5), high contractual (4/4). [Organization] operates in Country X and is legally subject to DPA-CX.


**Step 4 - Tier Assignment**: **Tier 1 (Mandatory)**

- Rationale: Legal obligation due to physical presence (office, legal entity, employees) in Country X. Mandatory compliance required.


**Step 5 - Approval**:

- Legal Counsel reviewed: Confirmed Tier 1 (legal obligation)
- Executive Management briefed: Approved Tier 1 addition, authorized compliance budget
- Approvals obtained: 2024-11-25


**Step 6 - Add to POL-00**:

- Regulation ID: REG-CX-001
- Added to ISMS-POL-00 Tier 1 section
- Stakeholders notified: 2024-11-30


**Next Steps**:

- Requirements extraction scheduled: 2024-12-15 (IMP-5.31.2 process)
- Control mapping and gap analysis: 2025-01-15 (IMP-5.31.3 process)
- Target compliance: 2025-06-01


---

## Example 2: Sector-Specific Regulation (Potential Market Entry)

**Scenario**: [Organization] is evaluating entry into the healthcare sector. Strategic planning includes potential healthcare SaaS product launch in 2025 Q3. A healthcare-specific information security regulation exists.

**Trigger**: Strategic initiative (potential market entry)

**Step 1 - Identification**:

- Source: Industry association (Healthcare IT Association) + legal counsel briefing
- Regulation Identified: Healthcare Information Security Regulation (HISR)
- Candidate ID: CAND-058


**Step 2 - Screening**:

- Relevance: YES (information security regulation for healthcare sector)
- Jurisdiction: YES ([Organization] operates in jurisdictions where regulation applies)
- Operational: Partial (does NOT currently serve healthcare, but considering it)
- Threshold: N/A (applies to all healthcare service providers)
- **Outcome**: Proceed (uncertain on operational, assess for future)


**Step 3 - Detailed Assessment**:

*Geographic Scope*:

- G1-G7: All YES (existing [Organization] jurisdictional presence) = 7/7
- **Score**: 7/7 = **HIGH**


*Operational Scope*:

- O1 (Services): POTENTIAL - Would provide healthcare SaaS if market entered
- O2 (Sectors): NO - Does not currently serve healthcare sector
- O3 (Data types): POTENTIAL - Would process health data if market entered
- O4 (Thresholds): N/A
- O5 (Specific operations): POTENTIAL - Healthcare data processing would qualify
- **Score**: 0/5 currently = **LOW** (but POTENTIAL high if market entry occurs)


*Contractual Scope*:

- C1-C4: All NO (no current healthcare customers/contracts)
- **Score**: 0/4 = **NONE**


**Determination**: **CONDITIONALLY APPLICABLE**

- Rationale: Geographic presence exists (high), but operational scope is currently low (not in healthcare). WOULD become applicable if healthcare market entry occurs as planned.


**Step 4 - Tier Assignment**: **Tier 2 (Conditional)**

- Rationale: Regulation would apply IF [Organization] launches healthcare product and serves healthcare customers. Condition: Healthcare market entry.
- Applicability Condition: "Applies when [Organization] provides SaaS platform to healthcare providers or processes health data"


**Step 5 - Approval**:

- ISMS Manager reviewed and approved Tier 2 assignment
- Legal Counsel consulted: Confirmed conditional applicability based on market entry
- Approval: 2024-12-01


**Step 6 - Add to POL-00**:

- Regulation ID: REG-HC-001
- Added to ISMS-POL-00 Tier 2 section
- Note: "Monitor Q2 2025 for market entry decision; if launch confirmed, conduct gap analysis"


**Next Steps**:

- Monitor healthcare product launch planning
- If launch confirmed: Conduct pre-implementation gap analysis (Q2 2025)
- If launch occurs: Transition to Tier 1, requirements extraction, compliance implementation
- Annual review of market entry status


---

## Example 3: Industry Best Practice Framework

**Scenario**: [Organization] decides to use the NIST Cybersecurity Framework (CSF) for internal maturity assessment and continuous improvement benchmarking.

**Trigger**: Internal initiative (maturity assessment program)

**Step 1 - Identification**:

- Source: NIST website (nist.gov/cyberframework)
- Framework Identified: NIST Cybersecurity Framework (CSF) Version 2.0
- Candidate ID: CAND-072


**Step 2 - Screening**:

- Relevance: YES (cybersecurity framework for information security)
- Jurisdiction: N/A (voluntary framework, not jurisdiction-based)
- Operational: YES (framework applicable to any organization managing cyber risk)
- Threshold: N/A (voluntary, no thresholds)
- **Outcome**: Proceed (informational/best practice assessment)


**Step 3 - Detailed Assessment**:

*Geographic Scope*:

- G1-G7: N/A (not a jurisdiction-based regulation)
- **Score**: N/A (voluntary framework)


*Operational Scope*:

- O1 (Services): YES - Framework applicable to [Organization]'s services
- O2 (Sectors): YES - Cross-sector framework
- O3 (Data types): YES - Framework covers all data types
- O4 (Thresholds): N/A - Voluntary, scalable to any organization
- O5 (Specific operations): YES - Framework covers [Organization]'s operations
- **Score**: 4/5 = **HIGH** (operationally relevant)


*Contractual Scope*:

- C1 (Explicit requirement): NO - No contracts require NIST CSF specifically
- C2 (Certifications): NO - NIST CSF is framework, not certification
- C3 (Audit rights): NO
- C4 (Market expectations): PARTIAL - Some RFPs ask about use of frameworks but don't mandate NIST CSF
- **Score**: 0/4 = **NONE** to **LOW**


**Determination**: **INFORMATIONAL REFERENCE**

- Rationale: Voluntary framework, not legal obligation. [Organization] chooses to use for internal maturity assessment and benchmarking. High operational relevance but no compliance requirement.


**Step 4 - Tier Assignment**: **Tier 3 (Informational)**

- Rationale: Best practice framework used voluntarily for guidance, maturity assessment, and control design. Not legally mandated.


**Step 5 - Approval**:

- ISMS Manager approved Tier 3 addition
- No legal review required (not legal obligation)
- Approval: 2024-12-05


**Step 6 - Add to POL-00**:

- Regulation ID: REF-NIST-CSF-001
- Added to ISMS-POL-00 Tier 3 section
- Usage Note: "Used for annual maturity assessment and control design guidance. Supports ISO 27001 continuous improvement."


**Next Steps**:

- Map NIST CSF functions to ISO 27001 controls (informational mapping)
- Conduct annual maturity assessment using CSF
- Use CSF to inform control enhancements and roadmap


---

## Example 4: Not Applicable Regulation

**Scenario**: During periodic comprehensive regulatory scan, Compliance Analyst identifies a regulation specific to pharmaceutical manufacturing data integrity.

**Trigger**: Periodic review (annual regulatory landscape scan)

**Step 1 - Identification**:

- Source: Legal database comprehensive scan
- Regulation Identified: Pharmaceutical Manufacturing Data Integrity Regulation (PMDIR)
- Candidate ID: CAND-085


**Step 2 - Screening**:

- Relevance: PARTIAL (data integrity related to information security, but very sector-specific)
- Jurisdiction: YES ([Organization] operates in jurisdiction where regulation exists)
- Operational: **NO** - [Organization] does NOT manufacture pharmaceuticals, does NOT serve pharmaceutical manufacturing sector
- Threshold: N/A
- **Outcome**: **STOP** - Failed operational screening


**Screening Rationale**:
"Regulation applies exclusively to pharmaceutical manufacturing facilities and governs data integrity in drug production processes. [Organization] is SaaS platform provider, does not manufacture pharmaceuticals, and does not provide services to pharmaceutical manufacturing facilities. Regulation addresses sector [Organization] does not operate in."

**Determination**: **NOT APPLICABLE**

**Step 3, 4, 5**: Not performed (stopped at screening)

**Step 6 - Do NOT Add to POL-00**

**Documentation**:

- Completed screening checklist filed in "Reviewed but Not Applicable" folder
- Rationale documented: "[Organization] does not operate in pharmaceutical manufacturing sector. Regulation scope limited to pharmaceutical facilities. Not applicable to SaaS business model."
- Date: 2024-12-10
- Reviewed by: Compliance Officer


**Next Steps**:

- Retain screening documentation (demonstrates comprehensive regulatory review)
- No further action unless [Organization] business model changes to serve pharmaceutical sector
- Reassess if [Organization] acquires pharmaceutical sector customers or partners with pharmaceutical companies


---

# Templates & Tools

## Applicability Assessment Form Template

**Reference**: Assessment Workbook 2 (Applicability Matrix) provides complete Excel template with formulas and data validation.

**Template Sections**:
1. Regulation Identification (name, jurisdiction, authority, citation, effective date, brief description)
2. Geographic Scope Assessment (Questions G1-G7, scoring, interpretation)
3. Operational Scope Assessment (Questions O1-O5, scoring, interpretation)
4. Contractual Scope Assessment (Questions C1-C4, scoring, interpretation)
5. Overall Determination (Applicable / Conditionally Applicable / Not Applicable / Uncertain)
6. Tier Assignment (1 / 2 / 3 with rationale)
7. Evidence References (list of attached documents)
8. Approval Signatures (Prepared, Reviewed, Legal, Approved with dates)

## Screening Checklist Template

```
REGULATORY APPLICABILITY - INITIAL SCREENING CHECKLIST

Candidate Regulation: _________________________________
Candidate ID: CAND-______
Identified By: __________________ Date: __________

┌─────────────────────────────────────────────────────────────┐
│ SCREENING QUESTIONS                                         │
└─────────────────────────────────────────────────────────────┘

Q1: RELEVANCE CHECK
Is this regulation related to information security, data 
protection, cybersecurity, or IT services?

☐ YES - Continue to Q2
☐ NO - STOP, Not Relevant

Rationale: _____________________________________________

Q2: JURISDICTION CHECK
Does [Organization] have any connection to this jurisdiction?
(operations, employees, customers, data subjects, targeting, 
extraterritorial reach)

☐ YES - Continue to Q3
☐ NO - STOP, No Jurisdictional Connection

Evidence: ______________________________________________

Q3: OPERATIONAL CHECK
Does [Organization] perform activities or process data types 
covered by this regulation?

☐ YES - Continue to Q4
☐ NO - STOP, Not Operationally Applicable

Rationale: _____________________________________________

Q4: THRESHOLD CHECK
Does regulation have thresholds? If yes, does [Organization] 
meet them?

☐ YES, meets thresholds - Proceed to Detailed Assessment
☐ NO, does not meet thresholds - STOP, Below Threshold
☐ N/A, no thresholds - Proceed to Detailed Assessment

Evidence: ______________________________________________

┌─────────────────────────────────────────────────────────────┐
│ SCREENING OUTCOME                                           │
└─────────────────────────────────────────────────────────────┘

☐ PROCEED TO DETAILED ASSESSMENT (Step 3)
  Passed all screening checks or uncertain

☐ NOT APPLICABLE - STOP
  Failed screening check(s)
  
  Reason: __________________________________________
  
  Action: File in "Reviewed but Not Applicable" folder

☐ UNCERTAIN - PROCEED TO DETAILED ASSESSMENT
  Borderline case, err on side of caution

Screened By: _________________ Date: ___________
Reviewed By: _________________ Date: ___________
```

## Decision Tree for Tier Assignment

```
                     [Regulation Determined Applicable]
                                  |
                    Is there a legal obligation?
                    (law/regulation in jurisdiction
                     where [Org] operates)
                                  |
                    ┌─────────────┴─────────────┐
                   YES                         NO
                    |                           |
              ┌─────┴─────┐                    |
              |   TIER 1  |                    |
              | Mandatory |          Is it contractually
              └───────────┘          required (significant
                                     customers/revenue)?
                                              |
                                    ┌─────────┴─────────┐
                                   YES                 NO
                                    |                   |
                              ┌─────┴─────┐            |
                              |   TIER 1  |      Is it a market
                              | Mandatory |      expectation or
                              └───────────┘      competitive
                                                 requirement?
                                                        |
                                              ┌─────────┴─────────┐
                                             YES                 NO
                                              |                   |
                                        ┌─────┴─────┐            |
                                        |   TIER 2  |     Is it voluntary
                                        |Conditional|     framework for
                                        └───────────┘     best practices?
                                                                  |
                                                        ┌─────────┴─────────┐
                                                       YES                 NO
                                                        |                   |
                                                  ┌─────┴─────┐       Reassess -
                                                  |   TIER 3  |       May not
                                                  |Informatio |       be
                                                  └───────────┘       applicable


[Regulation Determined Conditionally Applicable]
                    |
              ┌─────┴─────┐
              |   TIER 2  |
              |Conditional|
              └───────────┘
        (Monitor for condition
         triggering Tier 1)
```

## Stakeholder Communication Template

*[Template provided in Section 7.4 above - Email notification template]*

---

# Quality Checks & Common Pitfalls

## Quality Checklist

Before finalizing and submitting applicability assessment for approval:

**Assessment Completeness**:

- ☐ All three dimensions assessed (Geographic, Operational, Contractual)
- ☐ All questions answered (no blank fields)
- ☐ Evidence provided for each YES answer (documents attached or cited)
- ☐ Scores calculated correctly
- ☐ Determination documented with rationale (2-3 sentences minimum)


**Tier Assignment** (if applicable):

- ☐ Tier assignment aligns with POL-5.31.2 definitions
- ☐ Tier rationale clearly explains why this tier
- ☐ Applicability condition specified (for Tier 2)


**Approvals**:

- ☐ All required approvals obtained per workflow
- ☐ Tier 1: Legal Counsel review AND Executive approval
- ☐ Tier 2/3: ISMS Manager or Compliance Officer approval
- ☐ Approval signatures/emails collected


**Documentation**:

- ☐ Supporting documents attached
- ☐ Evidence naming conventions followed
- ☐ Assessment form complete (no sections skipped)


**Integration**:

- ☐ If applicable: Entry prepared for ISMS-POL-00
- ☐ Regulation ID assigned
- ☐ Stakeholder communication drafted


**Quality**:

- ☐ No typos or grammatical errors
- ☐ Professional formatting
- ☐ Consistent terminology (use regulation's official name throughout)
- ☐ References to regulation articles/sections accurate


## Common Pitfalls to Avoid

**Pitfall 1: Assuming Applicability Without Assessment**

**Mistake**: "This is a data protection regulation and we process data, so it must apply to us."

**Why Wrong**: Not all data protection regulations apply to all data processors. Jurisdictional scope, thresholds, specific activities matter.

**Correct Approach**: Perform systematic assessment. Even if regulation seems obviously applicable, document the analysis showing why.

**Pitfall 2: Over-Interpreting Regulatory Scope**

**Mistake**: Reading regulation more broadly than written. Example: Regulation says "applies to telecommunications providers" and [Organization] interprets this as "any company using telecommunications networks" (i.e., all companies with internet).

**Why Wrong**: Misinterpretation leads to unnecessary compliance burden (implementing requirements that don't actually apply).

**Correct Approach**: Read regulation text carefully. When scope is ambiguous, consult legal counsel. Don't assume broad interpretation without legal basis.

**Pitfall 3: Ignoring Contractual Obligations**

**Mistake**: Determining regulation "Not Applicable" based on legal analysis alone, ignoring that customer contracts require compliance.

**Why Wrong**: Contractual obligations create compliance requirements even if no legal obligation exists.

**Correct Approach**: Always assess contractual dimension (Section 4.3). Review customer contracts for regulatory references. Contractual requirement = Tier 1 or Tier 2 depending on significance.

**Pitfall 4: Failing to Document Rationale**

**Mistake**: Completing assessment form with YES/NO answers but no rationale or evidence.

**Why Wrong**: Undocumented assessment is not auditable. If challenged (by auditors, regulators, customers), cannot demonstrate due diligence.

**Correct Approach**: For EVERY determination (Applicable, Not Applicable, Tier assignment), write clear rationale (2-3 sentences minimum). Attach evidence documents.

**Pitfall 5: Skipping Legal Review for Tier 1**

**Mistake**: Assigning Tier 1 (Mandatory) based on compliance team's interpretation without legal counsel confirmation.

**Why Wrong**: Legal obligations have significant consequences (penalties, liability). Non-lawyer interpretation may be incorrect. Legal review protects [Organization].

**Correct Approach**: ALWAYS engage legal counsel for Tier 1 determinations. Legal counsel confirms: (1) Regulation creates legal obligation, (2) Tier 1 assignment is correct. Document legal opinion.

**Pitfall 6: One-Time Assessment, No Review**

**Mistake**: Performing assessment once when regulation identified, never reassessing.

**Why Wrong**: Circumstances change:

- Regulation amended (scope expanded/contracted)
- [Organization] changes (new services, new markets, growth crosses thresholds)
- Business model evolves


**Correct Approach**: Set review date for each regulation (POL-00 includes "Next Review Date"). Annually reassess Tier 1, monitor Tier 2 for condition triggers, review Tier 3 biennially.

**Pitfall 7: Not Applicable Today = Not Applicable Forever**

**Mistake**: Determining regulation "Not Applicable" and never revisiting.

**Why Wrong**: Today's non-applicability may become tomorrow's obligation if [Organization] expands.

**Correct Approach**: For "Not Applicable" determinations, file documentation and note WHY not applicable (e.g., "Does not serve healthcare sector"). If that condition changes (e.g., [Organization] enters healthcare), reassess.

---

# Related Documents & References

**Policy Documents**:

- **ISMS-POL-A.5.31.2**: Regulatory Applicability Methodology
  - Defines the three-dimensional assessment methodology this guide operationalizes
- **ISMS-POL-00**: Regulatory Applicability Framework
  - The regulatory register populated by this process
- **ISMS-POL-A.5.31.1**: Executive Summary & Control Alignment
  - Defines governance, roles, and approval workflows referenced in this guide


**Implementation Guides** (Next Steps):

- **ISMS-IMP-A.5.31.3**: Requirements Extraction Process
  - Immediate next step: Extract specific requirements from applicable regulations
- **ISMS-IMP-A.5.31.4**: Control Mapping Process
  - Map extracted requirements to ISO 27001 controls
- **ISMS-IMP-A.5.31.5**: Evidence Management Process
  - Collect and manage evidence demonstrating compliance with mapped controls
- **ISMS-IMP-A.5.31.6**: Compliance Dashboard & Regulatory Monitoring Process
  - Ongoing monitoring of regulatory landscape for changes and compliance status tracking


**Assessment Tools**:

- **Assessment Workbook 1**: Regulatory Inventory
  - Master list of identified regulations
- **Assessment Workbook 2**: Applicability Matrix
  - Excel template for performing assessments (implements this guide)


**Standards**:

- **ISO 27001:2022**: Control A.5.31 - Legal, Statutory, Regulatory and Contractual Requirements
  - The ISO control this process supports


---

**END OF IMPLEMENTATION GUIDE**

---

*This operational guide provides step-by-step instructions for identifying and assessing applicable regulations, enabling [Organization] to systematically determine compliance obligations and populate the regulatory register (ISMS-POL-00) with audit-ready documentation.*

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

# Step 1 - Regulatory Identification

## When to Perform Identification

Perform regulatory identification when any trigger event occurs (per Section 1.2). For periodic reviews, schedule annually in Q4 to inform next year's compliance planning.

## Where to Look for Regulations

Search systematically across multiple sources to ensure comprehensive coverage.

### Source 1: Legal Research Databases

**Commercial Platforms** (LexisNexis, Westlaw, Bloomberg Law, etc.):

**How to Access**:

- Subscription: Contact [Organization] Legal Department for credentials
- URL: [Internal Wiki link to access instructions]
- VPN may be required for off-site access


**Search Process**:
1. Navigate to "Regulatory Compliance" or "Laws & Regulations" section
2. Filter by **Jurisdiction**: Select target jurisdiction(s) (country, state/province, municipality)
3. Filter by **Topic/Practice Area**:

   - Information Security
   - Data Protection / Privacy
   - Cybersecurity
   - Telecommunications (if applicable)
   - Financial Services Regulation (if applicable)
   - Sector-specific as relevant

4. Filter by **Effective Date**: 

   - For new market entry: All active regulations
   - For periodic review: Last 12-24 months (recent changes)

5. Review results list:

   - Read official summaries first (quicker than full text)
   - Note regulation name, citation, effective date
   - Download full text for regulations that appear relevant


**Example Searches**:

- `"data protection" AND "cybersecurity" AND jurisdiction:EU`
- `"information security requirements" AND jurisdiction:"United States" AND topic:"Healthcare"`
- `"breach notification" AND jurisdiction:California AND effectivedate > 2023-01-01`


**Tips**:

- Set up automated alerts for ongoing monitoring (covered in IMP-S4)
- Check both enacted laws AND proposed regulations (early awareness)
- Review regulatory agency interpretations and guidance documents
- Use citator tools to find amendments and related regulations


### Source 2: Government & Regulatory Authority Websites

**Direct from Source**:

**How to Access**:

- Identify regulatory authorities for target jurisdiction:
  - Data Protection Authorities (DPAs)
  - Cybersecurity agencies (e.g., CISA in US, ENISA in EU)
  - Sector regulators (financial, healthcare, telecom, etc.)
- Navigate to authority's official website
- Look for "Laws & Regulations", "Legal Framework", "Compliance" sections


**What to Look For**:

- Official legal texts (laws, regulations, directives, decrees)
- Regulatory guidance and FAQs
- Enforcement actions (reveal regulatory priorities and interpretations)
- Public consultation documents (proposed regulations)


**Example Process** (Data Protection Authority):
1. Visit DPA website for [Target Jurisdiction]
2. Navigate to "Legal Framework" section
3. Identify primary data protection law
4. Review associated regulations, implementing acts, guidance
5. Download official text and guidance documents
6. Note any sector-specific variations

**Tips**:

- Official sources are authoritative (use these to verify commercial database info)
- Subscribe to regulatory authority email lists for updates
- Check for official English translations if regulation in other language
- Note effective dates and any transition periods


### Source 3: Industry Associations & Trade Groups

**Sector-Specific Intelligence**:

**How to Access**:

- Identify industry associations for [Organization]'s sector
- Examples:
  - Technology: TechNet, CCIA, BSA | The Software Alliance
  - Financial Services: ABA, SIFMA, local banking associations
  - Healthcare: HIMSS, local healthcare associations
- Membership often required for full access to regulatory updates


**What to Look For**:

- Regulatory tracking reports (associations monitor regulations affecting members)
- Compliance guides (practical interpretation for sector)
- Advocacy positions (association's view on proposed regulations)
- Member briefings and webinars


**Example Process**:
1. Visit industry association website
2. Navigate to "Policy & Advocacy" or "Regulatory Affairs" section
3. Review recent regulatory updates
4. Download compliance guides for regulations in scope
5. Note association's recommended approach

**Tips**:

- Associations provide sector-specific context commercial databases lack
- Attend association conferences for early regulatory intelligence
- Participate in association working groups (if [Organization] is member)
- Cross-reference association info with official sources (verify)


### Source 4: Legal Counsel (In-House or External)

**Expert Guidance**:

**How to Access**:

- In-House Legal: Contact General Counsel or designated corporate attorney
- External Counsel: Engage law firm by jurisdiction or specialty (data privacy firm, regulatory compliance firm, etc.)


**What to Request**:

- "Regulatory landscape review for [Jurisdiction/Sector]"
- "Identify information security and data protection regulations applicable to [Organization's planned activities in Jurisdiction]"
- Proactive briefing on new or proposed regulations


**Process**:
1. Schedule consultation with legal counsel
2. Provide context:

   - [Organization]'s current and planned operations in jurisdiction
   - Services offered, customers served, data processed
   - Organizational characteristics (size, revenue, structure)

3. Legal counsel researches and briefs on applicable regulations
4. Document legal counsel's findings and recommendations

**Tips**:

- Legal counsel provides interpretation, not just identification
- Use legal counsel for complex or ambiguous regulations
- Document legal opinions for audit trail
- Consider cost (external counsel expensive; use strategically)


### Source 5: Peer Networks & Compliance Forums

**Practical Intelligence**:

**How to Access**:

- Professional networks: LinkedIn groups (Compliance Professionals, Privacy Officers, CISOs)
- Industry ISACs (Information Sharing and Analysis Centers)
- Compliance software communities (Vanta, Drata, etc. user groups)
- Conferences and webinars


**What to Look For**:

- Peer discussions on new regulations ("Has anyone assessed Regulation X for applicability?")
- Implementation experiences ("How are others in our industry handling Regulation Y?")
- Regulatory alerts shared by peers
- Conference presentations on emerging regulatory trends


**Example Process**:
1. Join relevant LinkedIn groups or professional associations
2. Monitor discussions for regulatory mentions
3. Post queries: "Has anyone assessed [Regulation] for [Organization Type]?"
4. Attend compliance-focused conferences and note regulatory sessions

**Tips**:

- Peers provide real-world context and implementation insights
- Always verify peer information against authoritative sources
- Use peers for awareness, not as sole source
- Reciprocate (share your knowledge to build network)


### Source 6: Regulatory Alerts from Subscriptions

**Automated Monitoring**:

**How to Set Up**:

- Legal database alerts (configured during Source 1 access)
- Regulatory authority mailing lists (subscribe during Source 2 research)
- Law firm client alerts (if using external counsel)
- RegTech platform alerts (if [Organization] uses compliance software)


**What to Monitor**:

- New regulations enacted
- Amendments to existing regulations
- Proposed regulations (public comment periods)
- Regulatory guidance issued
- Enforcement actions


**Process**:
1. Configure alerts with specific keywords and jurisdictions
2. Review alerts daily or weekly (depending on volume)
3. Triage: Relevant (add to candidate list) vs. Not Relevant (discard)
4. For relevant alerts, proceed to regulatory identification

**Tips**:

- Alert fatigue is real; configure narrowly (specific jurisdictions and topics)
- Use digest mode (daily/weekly summary) rather than individual alerts
- Designate specific person to monitor and triage alerts
- Integrate alerts into Step 1 workflow (don't let them pile up unreviewed)


## Documenting Candidate Regulations

As you identify potentially relevant regulations, document them in a **Candidate Regulations List** (working document, spreadsheet recommended).

**Columns**:

- **Candidate ID**: Sequential number (CAND-001, CAND-002, etc.)
- **Regulation Name**: Official name
- **Jurisdiction**: Country, state/province, municipality
- **Issuing Authority**: Which government body or regulator issued it
- **Citation**: Official citation (e.g., "Regulation (EU) 2016/679", "California Civil Code § 1798.100")
- **Effective Date**: When regulation became/becomes legally binding
- **Brief Description**: 1-2 sentence summary (what does it regulate?)
- **Source**: Where found (legal database, regulatory authority website, peer alert, etc.)
- **Trigger Event**: What prompted this identification (new market entry, periodic review, alert, etc.)
- **Identified By / Date**: Who identified it and when


**Example Entry**:

| Candidate ID | Regulation Name | Jurisdiction | Authority | Citation | Effective Date | Description | Source | Trigger | Identified By | Date |
|--------------|----------------|--------------|-----------|----------|----------------|-------------|--------|---------|---------------|------|
| CAND-042 | Data Protection Act 2025 | Country X | Data Protection Authority | DPA 2025 | 2025-01-01 | Comprehensive data protection law regulating personal data processing | Legal database (LexisNexis) | Market entry planning for Country X | Compliance Analyst | 2024-11-15 |

**Use This List For**:

- Tracking all candidates identified during Step 1
- Input to Step 2 (screening)
- Audit trail (shows comprehensive identification effort)


---

# Step 2 - Initial Screening

**Purpose**: Quickly filter candidate regulations to focus detailed assessment effort on truly relevant regulations.

## Screening Criteria

For each candidate regulation in the list, answer these screening questions:

### Question 1: Relevance Check

**Is this regulation related to information security, data protection, cybersecurity, or IT services?**

- **YES**: Regulation governs:
  - Information security practices
  - Data protection / privacy
  - Cybersecurity requirements
  - IT service delivery
  - Cloud computing
  - Network security
  - Incident response / breach notification
  - Related topics

- **NO**: Regulation governs unrelated topics:
  - Environmental regulations
  - Labor laws (unless specifically about data protection of employee data)
  - Tax laws
  - Product safety (unless IT products)
  - Unrelated sector regulations


**Decision**:

- If **NO** → **STOP**. Regulation not relevant to ISMS. Document screening outcome and stop.
- If **YES** → Continue to Question 2


### Question 2: Jurisdiction Check

**Does [Organization] have any connection to this jurisdiction?**

Check ALL that apply:

- ☐ [Organization] has physical operations (offices, facilities) in this jurisdiction
- ☐ [Organization] has employees located in this jurisdiction
- ☐ [Organization] serves customers located in this jurisdiction
- ☐ [Organization] processes data of individuals in this jurisdiction
- ☐ [Organization] targets this jurisdiction (website localization, marketing, sales efforts)
- ☐ Regulation claims extraterritorial reach (applies regardless of location if certain criteria met)


**Decision**:

- If **ALL unchecked (no connection)** → Likely **NOT APPLICABLE**. Document screening outcome. STOP unless regulation has extraterritorial provisions.
- If **ANY checked** → Continue to Question 3


### Question 3: Operational Check

**Does [Organization] perform activities or process data types covered by this regulation?**

Check relevant regulation text and compare to [Organization]'s operations:

- ☐ [Organization] provides services that regulation covers (e.g., cloud services, IT consulting, software development)
- ☐ [Organization] serves industry sectors that regulation targets (e.g., financial services, healthcare, government)
- ☐ [Organization] processes data types that regulation governs (e.g., personal data, health records, financial information, payment card data)
- ☐ [Organization] performs specific operations regulation addresses (e.g., e-commerce, telecommunications, payment processing)


**Decision**:

- If **NONE checked** → Likely **NOT APPLICABLE**. [Organization] does not perform activities regulation governs. Document and STOP.
- If **ANY checked** → Continue to Question 4


### Question 4: Threshold Check

**Does this regulation have size, revenue, volume, or other thresholds? If yes, does [Organization] meet them?**

**Common Thresholds**:

- Employee count (e.g., "applies to organizations with 250+ employees")
- Revenue (e.g., "applies to organizations with €10M+ annual revenue")
- Data volume (e.g., "applies if processing data of 50,000+ individuals annually")
- Transaction volume (e.g., "applies if processing 6M+ payment transactions annually")
- Organizational type (e.g., "applies to public companies only", "applies to critical infrastructure operators")


**Check Regulation for Thresholds**:
1. Review regulation text for scope limitations based on organizational characteristics
2. Compare [Organization]'s characteristics to thresholds
3. Document [Organization]'s current status vs. threshold

**Decision**:

- If regulation has **NO thresholds** → Continue to Screening Outcome (proceed to detailed assessment)
- If regulation has thresholds:
  - **[Organization] MEETS thresholds** → Continue to Screening Outcome (proceed)
  - **[Organization] DOES NOT MEET thresholds** → **NOT APPLICABLE currently**
    - Document that regulation not applicable due to threshold
    - **Important**: Monitor [Organization]'s growth; if threshold crossed in future, regulation may become applicable
    - Set reminder to reassess if [Organization] approaching threshold


## Screening Outcome

Based on screening questions:

**Outcome 1: PROCEED TO DETAILED ASSESSMENT**

- Passed all screening checks (relevant, jurisdiction connection, operational match, meets thresholds if any)
- OR: Borderline/uncertain on one or more questions
- **Action**: Move to Step 3 (Detailed Applicability Assessment)


**Outcome 2: NOT APPLICABLE**

- Failed one or more screening checks (not relevant, no jurisdiction connection, no operational match, does not meet thresholds)
- **Action**: 
  - Document screening outcome with rationale
  - File in "Reviewed but Not Applicable" folder
  - Do NOT proceed to detailed assessment
  - Retain documentation (demonstrates due diligence in identifying regulations)
  - Set reminder to reassess if [Organization]'s circumstances change


**Outcome 3: UNCERTAIN**

- Ambiguous language in regulation
- Borderline jurisdiction connection (e.g., small number of customers in jurisdiction)
- Unclear whether [Organization]'s activities match regulation's scope
- **Action**: 
  - Err on side of caution
  - Proceed to Step 3 (Detailed Applicability Assessment)
  - Engage legal counsel for interpretation during Step 3


## Documenting Screening

**Screening Checklist Template**:

For Regulation: [Regulation Name / Candidate ID: CAND-XXX]

| Screening Question | Answer (Y/N) | Evidence / Rationale |
|--------------------|--------------|----------------------|
| **Q1: Relevance** - Related to information security, data protection, cybersecurity, or IT services? | ☐ YES ☐ NO | |
| **Q2: Jurisdiction** - [Org] has connection to jurisdiction (operations, employees, customers, data subjects, targeting, extraterritorial)? | ☐ YES ☐ NO | |
| **Q3: Operational** - [Org] performs activities or processes data types covered by regulation? | ☐ YES ☐ NO | |
| **Q4: Threshold** - [Org] meets any size/revenue/volume thresholds (or regulation has no thresholds)? | ☐ YES ☐ NO ☐ N/A | |

**Screening Outcome**: ☐ Proceed to Detailed Assessment ☐ Not Applicable ☐ Uncertain (proceed to detailed)

**Rationale** (if Not Applicable):

**Next Steps**:

- If Proceed/Uncertain: Begin Step 3
- If Not Applicable: File documentation, update Candidate Regulations List status


**Screened By**: [Name/Role] **Date**: [Date]

---

# Step 3 - Detailed Applicability Assessment

**Purpose**: Systematically assess regulation across three dimensions (Geographic, Operational, Contractual) to determine applicability.

**Reference**: POL-S2 Section 3 defines the methodology; this guide provides operational instructions.

## Geographic Scope Assessment

**Instructions**:
1. Review regulation text for geographic scope provisions (typically in early articles defining "scope" or "territorial application")
2. Gather evidence for [Organization]'s geographic footprint
3. Answer each question below with **YES** or **NO**
4. For each **YES**, document specific evidence
5. Calculate Geographic Applicability Score

**Question G1: Does [Organization] have physical operations in [Regulation's Jurisdiction]?**

- Physical operations: Offices, data centers, facilities, warehouses, storefronts
- **Evidence to Gather**:
  - Office location list (from HR or Facilities)
  - Legal entity registrations (from Legal/Finance)
  - Property leases or deeds
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "Office at 123 Main Street, City X, Country X - lease dated 2024-01-15"]


**Question G2: Does [Organization] have legal entities registered in [Regulation's Jurisdiction]?**

- Legal entities: Subsidiaries, branches, representative offices
- **Evidence to Gather**:
  - Corporate structure chart
  - Business registry records (Chamber of Commerce, Companies House, etc.)
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "[Organization] Country X GmbH, registration #12345678, registered 2024-02-01"]


**Question G3: Does [Organization] have employees located in [Regulation's Jurisdiction]?**

- Employees: Full-time, part-time, contractors physically located in jurisdiction
- **Evidence to Gather**:
  - Headcount report by location (from HR)
  - Payroll records showing local tax withholding
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "15 employees (10 FTE, 5 contractors) located in Country X per HR report dated 2024-11-01"]


**Question G4: Does [Organization] serve customers physically located in [Regulation's Jurisdiction]?**

- Customers: Individuals or organizations with primary location in jurisdiction
- **Evidence to Gather**:
  - Customer list filtered by location (from CRM)
  - Sales by region report (from Finance/Sales)
  - Customer contracts with address information
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "127 active customers with billing addresses in Country X, representing €1.2M annual revenue"]


**Question G5: Does [Organization] process data of individuals (data subjects) in [Regulation's Jurisdiction]?**

- Data subjects: Individuals whose personal data [Organization] processes, regardless of customer status
- Examples: Website visitors, app users, employee applicants, customer contacts
- **Evidence to Gather**:
  - Data processing records (from DPO or Privacy team)
  - Data subject location analysis (from data processing systems)
  - Web analytics (visitor geographic data)
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "Process personal data of ~50,000 website visitors from Country X monthly per Google Analytics"]


**Question G6: Does [Organization] target customers or users in [Regulation's Jurisdiction]?**

- Targeting indicators:
  - Website localized for jurisdiction (language, currency, local payment methods)
  - Marketing campaigns directed at jurisdiction
  - Social media advertising targeted to jurisdiction
  - Local domain name (e.g., .de for Germany, .fr for France)
  - Local phone numbers or support
- **Evidence to Gather**:
  - Website localization settings
  - Marketing campaign targeting data (from Marketing)
  - Domain registrations
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "Website available in Country X language, accepts local currency, Google Ads campaigns targeted to Country X"]


**Question G7: Does the regulation claim extraterritorial application?**

- Extraterritorial reach: Regulation applies regardless of [Organization]'s location if certain criteria met
- Common examples:
  - GDPR: Applies if offering goods/services to EU data subjects OR monitoring EU data subjects, even if organization not in EU
  - Some financial regulations: Apply if processing transactions in certain currencies, even if not in jurisdiction
- **Evidence to Gather**:
  - Regulation text analysis (read territorial scope provisions)
  - Legal counsel opinion on extraterritorial application
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "Regulation Article 3(2) states applies to processing of data subjects in Country X regardless of processor location"]


**Geographic Applicability Score**:

- Count **YES** answers: _____ / 7
- **Interpretation**:
  - **0-1 YES**: Low geographic applicability (minimal connection to jurisdiction)
  - **2-3 YES**: Moderate geographic applicability (some connection)
  - **4+ YES**: High geographic applicability (strong connection to jurisdiction)


**Document in**: Applicability Assessment Form - Section 2: Geographic Scope

## Operational Scope Assessment

**Instructions**:
1. Review regulation text for operational scope provisions (which activities, services, data types does it regulate?)
2. Gather evidence about [Organization]'s operations, services, customers, data processing
3. Answer each question below with **YES** or **NO**
4. For each **YES**, document specific evidence
5. Calculate Operational Applicability Score

**Question O1: Does [Organization] provide services that this regulation specifically addresses?**

- Identify service types regulation governs
- Compare to [Organization]'s service catalog
- **Common Service Types in Regulations**:
  - Cloud computing services (IaaS, PaaS, SaaS)
  - IT consulting and professional services
  - Software development
  - Managed security services
  - Data center hosting
  - Telecommunications
  - Payment processing
- **Evidence to Gather**:
  - Service catalog or product list
  - SOW (Statement of Work) examples from customer contracts
  - Marketing materials describing services
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "[Organization] provides SaaS platform and cloud infrastructure services, both explicitly covered by Regulation Section 4"]


**Question O2: Does [Organization] serve industry sectors that this regulation targets?**

- Sector-specific regulations (financial services, healthcare, government, energy, etc.)
- **Evidence to Gather**:
  - Customer list categorized by industry vertical (from CRM)
  - Revenue by sector (from Finance)
  - Customer contracts showing sector affiliation
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "35% of revenue from financial services customers; regulation specifically targets financial sector"]


**Question O3: Does [Organization] process data types that this regulation governs?**

- Data types commonly regulated:
  - Personal data / Personally Identifiable Information (PII)
  - Sensitive personal data (health, biometric, genetic, race, religion, etc.)
  - Financial data (account numbers, payment card data, transaction records)
  - Children's data
  - Government data / Classified information
  - Intellectual property
- **Evidence to Gather**:
  - Data inventory or data classification register
  - Data processing agreements with customers
  - Privacy notices or data protection impact assessments
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "Process personal data (names, emails, IP addresses) of EU data subjects; regulation governs personal data processing"]


**Question O4: Does [Organization]'s size, revenue, or other characteristics meet regulation's scope criteria?**

- Organizational characteristics that may trigger regulations:
  - **Size thresholds**: Number of employees (e.g., 50+, 250+, 1000+)
  - **Revenue thresholds**: Annual revenue (e.g., €10M+, $50M+)
  - **Data volume thresholds**: Number of data subjects (e.g., 10,000+, 50,000+)
  - **Transaction thresholds**: Payment volume (e.g., 6M+ card transactions annually)
  - **Organizational type**: Public company, private, non-profit, government contractor, critical infrastructure
- **Evidence to Gather**:
  - Financial reports (revenue, profit)
  - Headcount reports (from HR)
  - Data subject counts (from data processing systems)
  - Transaction volume (from payment processing systems)
  - Organizational structure (from Legal)
- **Answer**: ☐ YES ☐ NO ☐ N/A (regulation has no thresholds)
- **If YES or N/A, Evidence**: [e.g., "[Organization] has 350 employees, exceeds regulation's 250+ employee threshold per Article 5"]


**Question O5: Does [Organization] perform specific operations that regulation addresses?**

- Specific operational triggers:
  - E-commerce (selling goods/services online)
  - Cross-border data transfers
  - Automated decision-making / AI/ML
  - Profiling of individuals
  - Large-scale systematic monitoring
  - Telecommunications services
  - Payment services
  - Outsourcing / subprocessing
- **Evidence to Gather**:
  - Business model documentation
  - Data flow diagrams
  - Technology architecture (use of AI, automated systems)
  - Service descriptions
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "Platform uses automated recommendation algorithms qualifying as 'profiling' under regulation's definition (Article 22)"]


**Operational Applicability Score**:

- Count **YES** answers (exclude N/A): _____ / 5
- **Interpretation**:
  - **0-1 YES**: Low operational applicability (operations don't match regulation's scope)
  - **2-3 YES**: Moderate operational applicability (some operational alignment)
  - **4-5 YES**: High operational applicability (operations strongly align with regulation)


**Document in**: Applicability Assessment Form - Section 3: Operational Scope

## Contractual Scope Assessment

**Instructions**:
1. Review customer contracts, master service agreements, SLAs
2. Identify contractual obligations related to this regulation
3. Answer each question below with **YES** or **NO**
4. For each **YES**, document specific evidence
5. Calculate Contractual Applicability Score

**Question C1: Do customer contracts explicitly require compliance with this regulation?**

- Review contract clauses for specific regulatory references
- **Common Contract Language**:
  - "Supplier shall comply with [Regulation Name]"
  - "Supplier shall maintain compliance with all applicable data protection laws including [Regulation]"
  - "Supplier warrants compliance with [Regulation]"
- **Evidence to Gather**:
  - Customer contracts (review data protection, security, compliance clauses)
  - Master service agreements (MSAs)
  - Data processing agreements (DPAs)
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "15 customer contracts (23% of revenue) explicitly require [Regulation] compliance in Section 12 'Regulatory Compliance'"]


**Question C2: Do customer contracts require certifications or attestations related to this regulation?**

- Certifications evidencing regulatory compliance:
  - ISO 27001 (often required for European customers)
  - SOC 2 Type II
  - Specific regulatory certifications (e.g., HIPAA compliance attestation, PCI DSS certification)
- **Evidence to Gather**:
  - Contract requirements for certifications
  - RFP responses where certifications requested
  - Customer due diligence questionnaires
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "8 customer contracts require ISO 27001 certification; regulation is basis for many ISO 27001 control requirements"]


**Question C3: Do customer contracts grant audit rights that would examine compliance with this regulation?**

- Audit clauses allowing customer to verify compliance
- **Common Audit Rights**:
  - "Customer may audit Supplier's compliance with [Regulation] annually"
  - "Customer may request attestation of compliance"
  - "Customer may review security and compliance documentation"
- **Evidence to Gather**:
  - Customer contracts (review audit rights clauses)
  - Audit clause summaries
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "12 contracts grant customer right to audit [Organization]'s data protection practices, would include [Regulation] compliance"]


**Question C4: Is compliance with this regulation a competitive requirement or customer expectation in [Organization]'s market?**

- Market expectations even if not contractually mandated
- **Indicators**:
  - RFPs consistently ask about this regulation
  - Competitors advertise compliance with this regulation
  - Industry standards reference this regulation
  - Sales team reports customers asking about compliance
- **Evidence to Gather**:
  - RFP requirements analysis (from Sales)
  - Competitor websites and marketing materials
  - Sales team feedback (lost deals due to compliance gaps)
- **Answer**: ☐ YES ☐ NO
- **If YES, Evidence**: [e.g., "75% of RFPs in EU market request [Regulation] compliance confirmation; competitors prominently display compliance on websites"]


**Contractual Applicability Score**:

- Count **YES** answers: _____ / 4
- **Interpretation**:
  - **0 YES**: No contractual drivers (regulation not in contracts or market expectations)
  - **1-2 YES**: Moderate contractual drivers (some contracts or market pressure)
  - **3-4 YES**: High contractual drivers (strong contractual and market requirements)


**Document in**: Applicability Assessment Form - Section 4: Contractual Scope

## Overall Applicability Determination

**Combine the Three Dimensions**:

Review scores from Sections 4.1, 4.2, 4.3:

- Geographic Applicability Score: _____ / 7 → Low / Moderate / High
- Operational Applicability Score: _____ / 5 → Low / Moderate / High
- Contractual Applicability Score: _____ / 4 → None / Moderate / High


**Determination Framework** (from POL-S2 Section 3.4):

**APPLICABLE if**:

- Geographic = Moderate or High AND Operational = Moderate or High
- OR: Geographic = High (strong jurisdictional connection) regardless of operational
- OR: Contractual = High (strong contractual obligation) regardless of geographic/operational


**CONDITIONALLY APPLICABLE if**:

- Geographic = Low but Operational = Moderate/High (could become applicable if enter jurisdiction)
- OR: Geographic = Moderate but Operational = Low (monitoring for business changes)
- OR: Contractual = Moderate (some contracts require, considering for broader adoption)


**NOT APPLICABLE if**:

- Geographic = Low AND Operational = Low AND Contractual = None/Low
- Clear mismatch (regulation addresses activities [Organization] does not perform)


**UNCERTAIN - Escalate to Legal Counsel if**:

- Borderline scores (e.g., Geographic = Moderate, Operational = Moderate, Contractual = Low)
- Ambiguous regulation language
- Novel regulatory approach with no precedent
- High legal or business risk if determination wrong


**Document Determination**:

- **Determination**: ☐ Applicable ☐ Conditionally Applicable ☐ Not Applicable ☐ Uncertain (legal review needed)
- **Rationale** (2-3 sentences explaining determination based on scores and evidence):


---

# Step 4 - Tier Categorization

**Purpose**: If regulation is Applicable or Conditionally Applicable, assign it to the appropriate tier in ISMS-POL-00.

**Reference**: POL-S2 Section 4 defines tiers; this guide provides decision process.

## Tier Decision Framework

**For Regulations Determined APPLICABLE**:

**Assign Tier 1 (Mandatory Compliance) if ANY of**:
1. Legal obligation in jurisdiction where [Organization] operates (physical presence, legal entities, employees)
2. Required by law to serve customers in jurisdiction (e.g., GDPR for serving EU customers)
3. Required by contract with significant customers (>10% revenue, critical customers, government contracts)
4. Sector-specific regulation in sector where [Organization] operates (e.g., financial services reg, healthcare reg)

**Examples**:

- Data protection law in country where [Organization] has office → Tier 1
- Breach notification law for data processed by [Organization] → Tier 1
- PCI DSS because [Organization] processes payment cards → Tier 1 (contractual obligation with card brands)


**Assign Tier 2 (Conditional Applicability) if**:
1. Regulation WOULD apply IF [Organization] enters market, launches service, or crosses threshold
2. Not currently legally obligated but potential future obligation
3. Required by some customer contracts but not broadly (spot requirement)

**Examples**:

- Sector regulation for sector [Organization] considering entering → Tier 2
- Regulation with threshold [Organization] does not currently meet but may in future → Tier 2
- Regulation in jurisdiction where [Organization] may expand → Tier 2


**For Regulations Determined CONDITIONALLY APPLICABLE**:

- Assign **Tier 2** by default
- Monitor for condition triggering Tier 1 status


**For Informational References** (voluntary frameworks, not legal obligations):

**Assign Tier 3 if**:
1. Best practice framework [Organization] uses for guidance (NIST CSF, CIS Controls, etc.)
2. Industry standard [Organization] references for control design
3. Regulatory framework from other jurisdiction used for benchmarking

**Examples**:

- NIST Cybersecurity Framework (US) used by non-US organization for maturity assessment → Tier 3
- ISO 27002 guidance (not certification requirement itself) → Tier 3
- Foreign regulation used to inform control design but no legal obligation → Tier 3


## Documenting Tier Assignment

**In Applicability Assessment Form**:

- **Tier Assignment**: ☐ Tier 1 (Mandatory) ☐ Tier 2 (Conditional) ☐ Tier 3 (Informational)
- **Tier Rationale** (explain why this tier):


**Example Rationales**:

- **Tier 1**: "Legal obligation because [Organization] has office in Country X and regulation applies to all entities operating in Country X"
- **Tier 2**: "Conditional because [Organization] does not currently serve healthcare sector, but regulation would apply if healthcare services launched per 2025 strategic plan"
- **Tier 3**: "Informational because NIST CSF is voluntary framework used for maturity benchmarking, not legal requirement"


## Escalation for Tier 1

**Tier 1 assignments require heightened approval** (per POL-S1 governance):

- Legal Counsel review (confirm legal obligation)
- Executive Management approval (significant compliance investment)


Before finalizing Tier 1:
1. Schedule legal counsel review
2. Present applicability assessment evidence
3. Obtain legal confirmation of Tier 1 status
4. Brief Executive Management (may require budget, resources for compliance)
5. Obtain executive approval for Tier 1 addition

**Tier 2 and Tier 3**:

- ISMS Manager or Compliance Officer approval sufficient


---

# Step 5 - Documentation & Approval

## Complete Applicability Assessment Form

**Use Template**: Assessment Workbook 2 (Applicability Matrix) provides Excel template.

**Form Sections** (summary of previous steps):

**Section 1: Regulation Identification**

- Regulation name, jurisdiction, authority, citation, effective date
- Brief description, source where identified, trigger event


**Section 2: Geographic Scope Assessment**

- Questions G1-G7 with YES/NO answers and evidence
- Geographic Score and interpretation


**Section 3: Operational Scope Assessment**

- Questions O1-O5 with YES/NO answers and evidence
- Operational Score and interpretation


**Section 4: Contractual Scope Assessment**

- Questions C1-C4 with YES/NO answers and evidence
- Contractual Score and interpretation


**Section 5: Overall Determination**

- Applicable / Conditionally Applicable / Not Applicable / Uncertain
- Rationale (2-3 sentences)


**Section 6: Tier Assignment** (if applicable)

- Tier 1 / Tier 2 / Tier 3
- Tier rationale


**Section 7: Supporting Evidence**

- Attach or link to all evidence documents
- Examples: Contracts, financial reports, regulation text, legal opinion


**Section 8: Approval Signatures**

- Prepared By / Date: [Compliance Analyst who performed assessment]
- Reviewed By / Date: [Compliance Officer or ISMS Manager]
- Legal Review / Date: [Legal Counsel, required for Tier 1]
- Approved By / Date: [Executive Management for Tier 1, ISMS Manager for Tier 2/3]


## Attach Supporting Evidence

Gather and attach all evidence documents:

- Office location lists, legal entity registrations
- Customer lists and revenue reports
- Data processing records
- Contracts excerpts (data protection clauses)
- Regulation text (official download or link)
- Legal counsel opinion (if obtained)


**Evidence Naming Convention**: `[Regulation-Name]_[Evidence-Type]_[Date]`

- Example: `CountryX-DPA_Customer-List_2024-11-15.xlsx`
- Example: `CountryX-DPA_Legal-Opinion_2024-11-20.pdf`


## Route for Approval

**Approval Workflow**:

**For Tier 1**:
1. Compliance Analyst completes assessment
2. Compliance Officer reviews (confirms methodology followed, evidence adequate)
3. Legal Counsel reviews (confirms legal obligation, tier assignment correct)
4. Present to Executive Management (briefing on regulation, implications, resource needs)
5. Executive approves
6. All signatures obtained on assessment form

**Timeline**: 2-4 weeks (allow time for legal review and executive scheduling)

**For Tier 2 or Tier 3**:
1. Compliance Analyst completes assessment
2. Compliance Officer or ISMS Manager reviews and approves
3. Signature obtained on assessment form

**Timeline**: 3-5 business days

**Approval Evidence**:

- Signed assessment form (physical or electronic signature)
- Email approvals (acceptable if signature not feasible)
- Meeting minutes (for executive approval of Tier 1)


---

# Step 6 - Add to ISMS-POL-00

**If Determination = Applicable or Conditionally Applicable**: Add to ISMS-POL-00 (Regulatory Applicability Framework).

**If Determination = Not Applicable**: Do NOT add to ISMS-POL-00. File assessment for reference.

## Create Entry in ISMS-POL-00

**Reference**: ISMS-POL-00 for current format and structure.

**Entry Fields**:

**Regulation ID**: Assign unique identifier

- Format: REG-[Jurisdiction-Code]-[Sequence]
- Examples: REG-EU-001, REG-US-CA-005, REG-CH-002
- Sequential within jurisdiction


**Regulation Name**: Official full name

**Short Name / Acronym**: Commonly used abbreviation (if exists)

- Examples: GDPR, CCPA, HIPAA, SOX, PCI DSS


**Jurisdiction**: Country, state/province, or multi-jurisdictional

**Issuing Authority**: Government body or regulator

**Citation**: Official citation

**Effective Date**: When regulation became binding

**Tier**: 1 (Mandatory) / 2 (Conditional) / 3 (Informational)

**Applicability Rationale**: 1-2 sentence summary (why this tier?)

- Reference applicability assessment ID for full details


**Key Requirements** (high-level summary): 2-3 bullet points

- Brief overview of main obligations
- Full requirements extraction in IMP-S2 process


**Applicability Condition** (for Tier 2): What condition would trigger Tier 1 status?

- Example: "Applies if [Organization] processes payment cards" (for PCI DSS)
- Example: "Applies if [Organization] enters healthcare sector" (for healthcare regulation)


**Related Regulations**: Any overlapping or related regulations already in POL-00

- Cross-reference to show regulatory ecosystem


**Assessment Reference**: Link to completed Applicability Assessment Form

- Enables audit trail back to detailed analysis


**Next Review Date**: When to reassess applicability

- Tier 1: Annually
- Tier 2: Annually or when condition may be triggered
- Tier 3: Biennially


**Responsible Party**: Who monitors this regulation (typically Compliance Officer)

## Update ISMS-POL-00 Version

**Version Control**:

- Increment version number (e.g., v1.5 → v1.6 for minor addition)
- Update "Last Updated" date
- Add entry to POL-00 version history table


**Version History Entry**:
| Version | Date | Updated By | Changes |
|---------|------|------------|---------|
| 1.6 | 2024-11-30 | Compliance Officer | Added REG-EU-015: Country X Data Protection Act (Tier 1) |

## File Assessment Documentation

**Store Completed Assessment**:

- Central compliance repository (SharePoint, document management system, etc.)
- Folder structure: `/Regulatory-Assessments/[Year]/[Regulation-ID]_[Regulation-Name]/`
- Include:
  - Completed Applicability Assessment Form
  - All supporting evidence documents
  - Approval records (signed forms, email approvals, meeting minutes)


**Retention**: Indefinitely for Tier 1 regulations; 7 years for Tier 2/3 or Not Applicable determinations

## Communicate to Stakeholders

**Notification Template** (adapt based on tier and impact):

**Subject**: New Regulation Added to ISMS-POL-00: [Regulation Name] (Tier [1/2/3])

**To**: ISMS Team, Legal Counsel, Executive Management (Tier 1), Control Owners (if requirements identified)

**Body**:

```
Team,

A new regulation has been assessed and added to the Regulatory Applicability Framework (ISMS-POL-00):

REGULATION DETAILS:

- Name: [Full Regulation Name]
- Regulation ID: REG-XXX
- Jurisdiction: [Jurisdiction]
- Tier: [1 - Mandatory / 2 - Conditional / 3 - Informational]
- Effective Date: [Date]


APPLICABILITY RATIONALE:
[2-3 sentences explaining why this regulation applies and tier assignment]

KEY REQUIREMENTS (High-Level):

- [Requirement 1 summary]
- [Requirement 2 summary]
- [Requirement 3 summary]


NEXT STEPS:

- [For Tier 1]: Requirements extraction scheduled for [Date] (IMP-S2 process)
- [For Tier 1]: Control mapping and gap analysis to follow (IMP-S3 process)
- [For Tier 2]: Monitoring for [Condition that would trigger Tier 1]
- [For Tier 3]: Reference for control design and maturity assessment


DOCUMENTATION:

- Full assessment: [Link to assessment document]
- ISMS-POL-00 entry: [Section X.Y]


IMPACT:
[For Tier 1]: This is a mandatory compliance obligation. Implementation planning will begin immediately. Resource needs will be assessed and communicated.
[For Tier 2]: This regulation is conditionally applicable and monitored. No immediate action required.
[For Tier 3]: This is an informational reference. Use for benchmarking and best practices.

QUESTIONS:
Contact [Compliance Officer] at [email] with questions.

[Signature]
Compliance Officer
```

**Distribution**:

- **Tier 1**: Broad distribution (all stakeholders, executive team)
- **Tier 2**: Targeted distribution (compliance team, business unit planning specific condition)
- **Tier 3**: Minimal distribution (compliance team, relevant technical teams)


---

# Worked Examples

## Example 1: Data Protection Regulation in New Operating Jurisdiction

**Scenario**: [Organization] opens a sales office in Country X to better serve customers in that market. Country X has a comprehensive data protection law similar to GDPR.

**Trigger**: New jurisdiction entry (office opening)

**Step 1 - Identification**:

- Source: Legal database (LexisNexis) and Country X Data Protection Authority website
- Regulation Identified: Data Protection Act of Country X (DPA-CX)
- Candidate ID: CAND-042


**Step 2 - Screening**:

- Relevance: YES (data protection regulation, directly relevant to ISMS)
- Jurisdiction: YES ([Organization] now has office in Country X)
- Operational: YES ([Organization] processes personal data)
- Threshold: N/A (regulation applies to all data controllers/processors)
- **Outcome**: Proceed to detailed assessment


**Step 3 - Detailed Assessment**:

*Geographic Scope*:

- G1 (Physical operations): YES - Office at 456 Business Blvd, City X, Country X
- G2 (Legal entities): YES - [Organization] Country X LLC, registration #CX-987654
- G3 (Employees): YES - 8 employees (6 sales, 2 admin) in Country X office
- G4 (Customers located): YES - 45 customers with primary address in Country X
- G5 (Data subjects): YES - Process personal data of Country X customers and website visitors
- G6 (Targeting): YES - Website has Country X language version, local payment methods
- G7 (Extraterritorial): NO - Regulation applies based on territorial presence, not extraterritorial
- **Score**: 6/7 = **HIGH**


*Operational Scope*:

- O1 (Services): YES - [Organization] provides SaaS platform, regulation governs data processing services
- O2 (Sectors): YES - [Organization] serves financial services customers in Country X, regulation has financial sector provisions
- O3 (Data types): YES - Process personal data (names, emails, addresses, usage data)
- O4 (Thresholds): N/A - No thresholds, applies to all processors
- O5 (Specific operations): YES - Automated decision-making in platform falls under regulation's AI provisions
- **Score**: 4/5 = **HIGH**


*Contractual Scope*:

- C1 (Explicit contracts): YES - 12 Country X customer contracts require DPA-CX compliance
- C2 (Certifications): YES - 8 contracts require ISO 27001, which incorporates data protection requirements
- C3 (Audit rights): YES - 5 contracts grant customer audit rights for data protection practices
- C4 (Market expectations): YES - All RFPs from Country X customers ask for DPA-CX compliance confirmation
- **Score**: 4/4 = **HIGH**


**Determination**: **APPLICABLE**

- Rationale: High geographic (6/7), high operational (4/5), high contractual (4/4). [Organization] operates in Country X and is legally subject to DPA-CX.


**Step 4 - Tier Assignment**: **Tier 1 (Mandatory)**

- Rationale: Legal obligation due to physical presence (office, legal entity, employees) in Country X. Mandatory compliance required.


**Step 5 - Approval**:

- Legal Counsel reviewed: Confirmed Tier 1 (legal obligation)
- Executive Management briefed: Approved Tier 1 addition, authorized compliance budget
- Approvals obtained: 2024-11-25


**Step 6 - Add to POL-00**:

- Regulation ID: REG-CX-001
- Added to ISMS-POL-00 Tier 1 section
- Stakeholders notified: 2024-11-30


**Next Steps**:

- Requirements extraction scheduled: 2024-12-15 (IMP-S2 process)
- Control mapping and gap analysis: 2025-01-15 (IMP-S3 process)
- Target compliance: 2025-06-01


---

## Example 2: Sector-Specific Regulation (Potential Market Entry)

**Scenario**: [Organization] is evaluating entry into the healthcare sector. Strategic planning includes potential healthcare SaaS product launch in 2025 Q3. A healthcare-specific information security regulation exists.

**Trigger**: Strategic initiative (potential market entry)

**Step 1 - Identification**:

- Source: Industry association (Healthcare IT Association) + legal counsel briefing
- Regulation Identified: Healthcare Information Security Regulation (HISR)
- Candidate ID: CAND-058


**Step 2 - Screening**:

- Relevance: YES (information security regulation for healthcare sector)
- Jurisdiction: YES ([Organization] operates in jurisdictions where regulation applies)
- Operational: Partial (does NOT currently serve healthcare, but considering it)
- Threshold: N/A (applies to all healthcare service providers)
- **Outcome**: Proceed (uncertain on operational, assess for future)


**Step 3 - Detailed Assessment**:

*Geographic Scope*:

- G1-G7: All YES (existing [Organization] jurisdictional presence) = 7/7
- **Score**: 7/7 = **HIGH**


*Operational Scope*:

- O1 (Services): POTENTIAL - Would provide healthcare SaaS if market entered
- O2 (Sectors): NO - Does not currently serve healthcare sector
- O3 (Data types): POTENTIAL - Would process health data if market entered
- O4 (Thresholds): N/A
- O5 (Specific operations): POTENTIAL - Healthcare data processing would qualify
- **Score**: 0/5 currently = **LOW** (but POTENTIAL high if market entry occurs)


*Contractual Scope*:

- C1-C4: All NO (no current healthcare customers/contracts)
- **Score**: 0/4 = **NONE**


**Determination**: **CONDITIONALLY APPLICABLE**

- Rationale: Geographic presence exists (high), but operational scope is currently low (not in healthcare). WOULD become applicable if healthcare market entry occurs as planned.


**Step 4 - Tier Assignment**: **Tier 2 (Conditional)**

- Rationale: Regulation would apply IF [Organization] launches healthcare product and serves healthcare customers. Condition: Healthcare market entry.
- Applicability Condition: "Applies when [Organization] provides SaaS platform to healthcare providers or processes health data"


**Step 5 - Approval**:

- ISMS Manager reviewed and approved Tier 2 assignment
- Legal Counsel consulted: Confirmed conditional applicability based on market entry
- Approval: 2024-12-01


**Step 6 - Add to POL-00**:

- Regulation ID: REG-HC-001
- Added to ISMS-POL-00 Tier 2 section
- Note: "Monitor Q2 2025 for market entry decision; if launch confirmed, conduct gap analysis"


**Next Steps**:

- Monitor healthcare product launch planning
- If launch confirmed: Conduct pre-implementation gap analysis (Q2 2025)
- If launch occurs: Transition to Tier 1, requirements extraction, compliance implementation
- Annual review of market entry status


---

## Example 3: Industry Best Practice Framework

**Scenario**: [Organization] decides to use the NIST Cybersecurity Framework (CSF) for internal maturity assessment and continuous improvement benchmarking.

**Trigger**: Internal initiative (maturity assessment program)

**Step 1 - Identification**:

- Source: NIST website (nist.gov/cyberframework)
- Framework Identified: NIST Cybersecurity Framework (CSF) Version 2.0
- Candidate ID: CAND-072


**Step 2 - Screening**:

- Relevance: YES (cybersecurity framework for information security)
- Jurisdiction: N/A (voluntary framework, not jurisdiction-based)
- Operational: YES (framework applicable to any organization managing cyber risk)
- Threshold: N/A (voluntary, no thresholds)
- **Outcome**: Proceed (informational/best practice assessment)


**Step 3 - Detailed Assessment**:

*Geographic Scope*:

- G1-G7: N/A (not a jurisdiction-based regulation)
- **Score**: N/A (voluntary framework)


*Operational Scope*:

- O1 (Services): YES - Framework applicable to [Organization]'s services
- O2 (Sectors): YES - Cross-sector framework
- O3 (Data types): YES - Framework covers all data types
- O4 (Thresholds): N/A - Voluntary, scalable to any organization
- O5 (Specific operations): YES - Framework covers [Organization]'s operations
- **Score**: 4/5 = **HIGH** (operationally relevant)


*Contractual Scope*:

- C1 (Explicit requirement): NO - No contracts require NIST CSF specifically
- C2 (Certifications): NO - NIST CSF is framework, not certification
- C3 (Audit rights): NO
- C4 (Market expectations): PARTIAL - Some RFPs ask about use of frameworks but don't mandate NIST CSF
- **Score**: 0/4 = **NONE** to **LOW**


**Determination**: **INFORMATIONAL REFERENCE**

- Rationale: Voluntary framework, not legal obligation. [Organization] chooses to use for internal maturity assessment and benchmarking. High operational relevance but no compliance requirement.


**Step 4 - Tier Assignment**: **Tier 3 (Informational)**

- Rationale: Best practice framework used voluntarily for guidance, maturity assessment, and control design. Not legally mandated.


**Step 5 - Approval**:

- ISMS Manager approved Tier 3 addition
- No legal review required (not legal obligation)
- Approval: 2024-12-05


**Step 6 - Add to POL-00**:

- Regulation ID: REF-NIST-CSF-001
- Added to ISMS-POL-00 Tier 3 section
- Usage Note: "Used for annual maturity assessment and control design guidance. Supports ISO 27001 continuous improvement."


**Next Steps**:

- Map NIST CSF functions to ISO 27001 controls (informational mapping)
- Conduct annual maturity assessment using CSF
- Use CSF to inform control enhancements and roadmap


---

## Example 4: Not Applicable Regulation

**Scenario**: During periodic comprehensive regulatory scan, Compliance Analyst identifies a regulation specific to pharmaceutical manufacturing data integrity.

**Trigger**: Periodic review (annual regulatory landscape scan)

**Step 1 - Identification**:

- Source: Legal database comprehensive scan
- Regulation Identified: Pharmaceutical Manufacturing Data Integrity Regulation (PMDIR)
- Candidate ID: CAND-085


**Step 2 - Screening**:

- Relevance: PARTIAL (data integrity related to information security, but very sector-specific)
- Jurisdiction: YES ([Organization] operates in jurisdiction where regulation exists)
- Operational: **NO** - [Organization] does NOT manufacture pharmaceuticals, does NOT serve pharmaceutical manufacturing sector
- Threshold: N/A
- **Outcome**: **STOP** - Failed operational screening


**Screening Rationale**:
"Regulation applies exclusively to pharmaceutical manufacturing facilities and governs data integrity in drug production processes. [Organization] is SaaS platform provider, does not manufacture pharmaceuticals, and does not provide services to pharmaceutical manufacturing facilities. Regulation addresses sector [Organization] does not operate in."

**Determination**: **NOT APPLICABLE**

**Step 3, 4, 5**: Not performed (stopped at screening)

**Step 6 - Do NOT Add to POL-00**

**Documentation**:

- Completed screening checklist filed in "Reviewed but Not Applicable" folder
- Rationale documented: "[Organization] does not operate in pharmaceutical manufacturing sector. Regulation scope limited to pharmaceutical facilities. Not applicable to SaaS business model."
- Date: 2024-12-10
- Reviewed by: Compliance Officer


**Next Steps**:

- Retain screening documentation (demonstrates comprehensive regulatory review)
- No further action unless [Organization] business model changes to serve pharmaceutical sector
- Reassess if [Organization] acquires pharmaceutical sector customers or partners with pharmaceutical companies


---

# Templates & Tools

## Applicability Assessment Form Template

**Reference**: Assessment Workbook 2 (Applicability Matrix) provides complete Excel template with formulas and data validation.

**Template Sections**:
1. Regulation Identification (name, jurisdiction, authority, citation, effective date, brief description)
2. Geographic Scope Assessment (Questions G1-G7, scoring, interpretation)
3. Operational Scope Assessment (Questions O1-O5, scoring, interpretation)
4. Contractual Scope Assessment (Questions C1-C4, scoring, interpretation)
5. Overall Determination (Applicable / Conditionally Applicable / Not Applicable / Uncertain)
6. Tier Assignment (1 / 2 / 3 with rationale)
7. Evidence References (list of attached documents)
8. Approval Signatures (Prepared, Reviewed, Legal, Approved with dates)

## Screening Checklist Template

```
REGULATORY APPLICABILITY - INITIAL SCREENING CHECKLIST

Candidate Regulation: _________________________________
Candidate ID: CAND-______
Identified By: __________________ Date: __________

┌─────────────────────────────────────────────────────────────┐
│ SCREENING QUESTIONS                                         │
└─────────────────────────────────────────────────────────────┘

Q1: RELEVANCE CHECK
Is this regulation related to information security, data 
protection, cybersecurity, or IT services?

☐ YES - Continue to Q2
☐ NO - STOP, Not Relevant

Rationale: _____________________________________________

Q2: JURISDICTION CHECK
Does [Organization] have any connection to this jurisdiction?
(operations, employees, customers, data subjects, targeting, 
extraterritorial reach)

☐ YES - Continue to Q3
☐ NO - STOP, No Jurisdictional Connection

Evidence: ______________________________________________

Q3: OPERATIONAL CHECK
Does [Organization] perform activities or process data types 
covered by this regulation?

☐ YES - Continue to Q4
☐ NO - STOP, Not Operationally Applicable

Rationale: _____________________________________________

Q4: THRESHOLD CHECK
Does regulation have thresholds? If yes, does [Organization] 
meet them?

☐ YES, meets thresholds - Proceed to Detailed Assessment
☐ NO, does not meet thresholds - STOP, Below Threshold
☐ N/A, no thresholds - Proceed to Detailed Assessment

Evidence: ______________________________________________

┌─────────────────────────────────────────────────────────────┐
│ SCREENING OUTCOME                                           │
└─────────────────────────────────────────────────────────────┘

☐ PROCEED TO DETAILED ASSESSMENT (Step 3)
  Passed all screening checks or uncertain

☐ NOT APPLICABLE - STOP
  Failed screening check(s)
  
  Reason: __________________________________________
  
  Action: File in "Reviewed but Not Applicable" folder

☐ UNCERTAIN - PROCEED TO DETAILED ASSESSMENT
  Borderline case, err on side of caution

Screened By: _________________ Date: ___________
Reviewed By: _________________ Date: ___________
```

## Decision Tree for Tier Assignment

```
                     [Regulation Determined Applicable]
                                  |
                    Is there a legal obligation?
                    (law/regulation in jurisdiction
                     where [Org] operates)
                                  |
                    ┌─────────────┴─────────────┐
                   YES                         NO
                    |                           |
              ┌─────┴─────┐                    |
              |   TIER 1  |                    |
              | Mandatory |          Is it contractually
              └───────────┘          required (significant
                                     customers/revenue)?
                                              |
                                    ┌─────────┴─────────┐
                                   YES                 NO
                                    |                   |
                              ┌─────┴─────┐            |
                              |   TIER 1  |      Is it a market
                              | Mandatory |      expectation or
                              └───────────┘      competitive
                                                 requirement?
                                                        |
                                              ┌─────────┴─────────┐
                                             YES                 NO
                                              |                   |
                                        ┌─────┴─────┐            |
                                        |   TIER 2  |     Is it voluntary
                                        |Conditional|     framework for
                                        └───────────┘     best practices?
                                                                  |
                                                        ┌─────────┴─────────┐
                                                       YES                 NO
                                                        |                   |
                                                  ┌─────┴─────┐       Reassess -
                                                  |   TIER 3  |       May not
                                                  |Informatio |       be
                                                  └───────────┘       applicable


[Regulation Determined Conditionally Applicable]
                    |
              ┌─────┴─────┐
              |   TIER 2  |
              |Conditional|
              └───────────┘
        (Monitor for condition
         triggering Tier 1)
```

## Stakeholder Communication Template

*[Template provided in Section 7.4 above - Email notification template]*

---

# Quality Checks & Common Pitfalls

## Quality Checklist

Before finalizing and submitting applicability assessment for approval:

**Assessment Completeness**:

- ☐ All three dimensions assessed (Geographic, Operational, Contractual)
- ☐ All questions answered (no blank fields)
- ☐ Evidence provided for each YES answer (documents attached or cited)
- ☐ Scores calculated correctly
- ☐ Determination documented with rationale (2-3 sentences minimum)


**Tier Assignment** (if applicable):

- ☐ Tier assignment aligns with POL-S2 definitions
- ☐ Tier rationale clearly explains why this tier
- ☐ Applicability condition specified (for Tier 2)


**Approvals**:

- ☐ All required approvals obtained per workflow
- ☐ Tier 1: Legal Counsel review AND Executive approval
- ☐ Tier 2/3: ISMS Manager or Compliance Officer approval
- ☐ Approval signatures/emails collected


**Documentation**:

- ☐ Supporting documents attached
- ☐ Evidence naming conventions followed
- ☐ Assessment form complete (no sections skipped)


**Integration**:

- ☐ If applicable: Entry prepared for ISMS-POL-00
- ☐ Regulation ID assigned
- ☐ Stakeholder communication drafted


**Quality**:

- ☐ No typos or grammatical errors
- ☐ Professional formatting
- ☐ Consistent terminology (use regulation's official name throughout)
- ☐ References to regulation articles/sections accurate


## Common Pitfalls to Avoid

**Pitfall 1: Assuming Applicability Without Assessment**

**Mistake**: "This is a data protection regulation and we process data, so it must apply to us."

**Why Wrong**: Not all data protection regulations apply to all data processors. Jurisdictional scope, thresholds, specific activities matter.

**Correct Approach**: Perform systematic assessment. Even if regulation seems obviously applicable, document the analysis showing why.

**Pitfall 2: Over-Interpreting Regulatory Scope**

**Mistake**: Reading regulation more broadly than written. Example: Regulation says "applies to telecommunications providers" and [Organization] interprets this as "any company using telecommunications networks" (i.e., all companies with internet).

**Why Wrong**: Misinterpretation leads to unnecessary compliance burden (implementing requirements that don't actually apply).

**Correct Approach**: Read regulation text carefully. When scope is ambiguous, consult legal counsel. Don't assume broad interpretation without legal basis.

**Pitfall 3: Ignoring Contractual Obligations**

**Mistake**: Determining regulation "Not Applicable" based on legal analysis alone, ignoring that customer contracts require compliance.

**Why Wrong**: Contractual obligations create compliance requirements even if no legal obligation exists.

**Correct Approach**: Always assess contractual dimension (Section 4.3). Review customer contracts for regulatory references. Contractual requirement = Tier 1 or Tier 2 depending on significance.

**Pitfall 4: Failing to Document Rationale**

**Mistake**: Completing assessment form with YES/NO answers but no rationale or evidence.

**Why Wrong**: Undocumented assessment is not auditable. If challenged (by auditors, regulators, customers), cannot demonstrate due diligence.

**Correct Approach**: For EVERY determination (Applicable, Not Applicable, Tier assignment), write clear rationale (2-3 sentences minimum). Attach evidence documents.

**Pitfall 5: Skipping Legal Review for Tier 1**

**Mistake**: Assigning Tier 1 (Mandatory) based on compliance team's interpretation without legal counsel confirmation.

**Why Wrong**: Legal obligations have significant consequences (penalties, liability). Non-lawyer interpretation may be incorrect. Legal review protects [Organization].

**Correct Approach**: ALWAYS engage legal counsel for Tier 1 determinations. Legal counsel confirms: (1) Regulation creates legal obligation, (2) Tier 1 assignment is correct. Document legal opinion.

**Pitfall 6: One-Time Assessment, No Review**

**Mistake**: Performing assessment once when regulation identified, never reassessing.

**Why Wrong**: Circumstances change:

- Regulation amended (scope expanded/contracted)
- [Organization] changes (new services, new markets, growth crosses thresholds)
- Business model evolves


**Correct Approach**: Set review date for each regulation (POL-00 includes "Next Review Date"). Annually reassess Tier 1, monitor Tier 2 for condition triggers, review Tier 3 biennially.

**Pitfall 7: Not Applicable Today = Not Applicable Forever**

**Mistake**: Determining regulation "Not Applicable" and never revisiting.

**Why Wrong**: Today's non-applicability may become tomorrow's obligation if [Organization] expands.

**Correct Approach**: For "Not Applicable" determinations, file documentation and note WHY not applicable (e.g., "Does not serve healthcare sector"). If that condition changes (e.g., [Organization] enters healthcare), reassess.

---

# Related Documents & References

**Policy Documents**:

- **ISMS-POL-A.5.31-S2**: Regulatory Applicability Methodology
  - Defines the three-dimensional assessment methodology this guide operationalizes
- **ISMS-POL-00**: Regulatory Applicability Framework
  - The regulatory register populated by this process
- **ISMS-POL-A.5.31-S1**: Executive Summary & Control Alignment
  - Defines governance, roles, and approval workflows referenced in this guide


**Implementation Guides** (Next Steps):

- **ISMS-IMP-A.5.31-S3**: Requirements Extraction Process
  - Immediate next step: Extract specific requirements from applicable regulations
- **ISMS-IMP-A.5.31-S4**: Control Mapping Process
  - Map extracted requirements to ISO 27001 controls
- **ISMS-IMP-A.5.31-S5**: Evidence Management Process
  - Collect and manage evidence demonstrating compliance with mapped controls
- **ISMS-IMP-A.5.31-S6**: Compliance Dashboard & Regulatory Monitoring Process
  - Ongoing monitoring of regulatory landscape for changes and compliance status tracking


**Assessment Tools**:

- **Assessment Workbook 1**: Regulatory Inventory
  - Master list of identified regulations
- **Assessment Workbook 2**: Applicability Matrix
  - Excel template for performing assessments (implements this guide)


**Standards**:

- **ISO 27001:2022**: Control A.5.31 - Legal, Statutory, Regulatory and Contractual Requirements
  - The ISO control this process supports


---

**END OF SPECIFICATION**

---

*"If you thought that science was certain — well, that is just an error on your part."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-01-31 -->
