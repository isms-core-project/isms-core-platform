<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.31.2:framework:POL:a.5.31.2 -->
**ISMS-POL-A.5.31.2 — Regulatory Applicability Methodology**
**Legal, Statutory, Regulatory and Contractual Requirements**

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Legal, Statutory, Regulatory and Contractual Requirements: Regulatory Applicability Methodology |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.31.2 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO/ISO | Initial policy framework for ISO 27001:2022 first certification |

---

# Introduction and Framework Context

## Purpose of This Policy Section

This policy section establishes the systematic methodology by which [Organisation] identifies, assesses, and categorizes legal, statutory, regulatory, and contractual requirements applicable to its information security program. 

The methodology defined herein transforms regulatory compliance from a reactive, ad-hoc activity into a systematic, repeatable process that produces consistent, defensible determinations of regulatory applicability.

## Relationship to the Compliance Framework

ISMS-POL-A.5.31.1 (Executive Summary & Control Alignment) established the overall regulatory compliance framework and governance structure. This policy section (5.31.2) provides the **first operational methodology** within that framework: the process for determining **which regulations apply** to [Organisation].

The outputs of this methodology directly populate and maintain **ISMS-POL-00 (Regulatory Applicability Framework)**—the authoritative registry of applicable regulations.

**Framework Flow:**
```
ISO 27001:2022 Control A.5.31
         ↓
POL-5.31.1: Framework Foundation & Governance
         ↓
POL-5.31.2: Applicability Methodology ← YOU ARE HERE
         ↓ (produces entries for)
ISMS-POL-00: Regulatory Register
         ↓ (feeds into)
POL-5.31.3: Requirements Extraction & Control Mapping
         ↓
POL-5.31.4: Change Management & Evidence
```

## The Systematic vs. Ad-Hoc Approach

**Traditional Ad-Hoc Approach:**

- "We operate in Country X, so we probably need to comply with Country X's data protection law"
- "Customer Y mentioned regulation Z in their RFP, so I guess that applies"
- "I heard at a conference that regulation ABC is important"
- No documented rationale for determinations
- Inconsistent criteria applied across different regulations
- No systematic review process

**This Framework's Systematic Approach:**

- Defined trigger events initiate applicability assessments
- Multiple sources systematically scanned for potentially applicable regulations
- Structured assessment using consistent three-dimensional criteria
- Documented rationale with supporting evidence
- Formal approval workflow
- Periodic review and validation
- Complete audit trail

The systematic approach ensures that:

- Different evaluators reach the same conclusions (repeatability)
- Decisions are defensible to auditors and regulators
- Applicability determinations are traceable and reversible
- Changes in circumstances trigger re-evaluation
- Nothing falls through the cracks

## Integration with ISMS-POL-00

ISMS-POL-00 serves as the **authoritative regulatory register** for [Organisation]. This policy defines the **processes by which regulations enter, are categorized within, and exit POL-00**.

**Key Relationship:**

- **This Policy (POL-5.31.2)** defines the methodology for applicability assessment
- **POL-00** contains the results of applying that methodology (the list of applicable regulations)
- **IMP-5.31.1** (Applicability Assessment Process) provides step-by-step operational procedures for executing this methodology
- **Assessment Workbook 2** (Applicability Matrix) provides structured tools for documentation

## Document Scope

This policy section covers:

- **Trigger events** that initiate applicability assessments (Section 2.1)
- **Sources** for identifying potentially applicable regulations (Section 2.2)
- **Initial screening** to filter candidates (Section 2.3)
- **Three-dimensional applicability assessment** methodology (Section 3)
- **Three-tier categorization** framework (Section 4)
- **Documentation and approval** requirements (Section 5)
- **Review frequency and triggers** for re-assessment (Section 6)

This policy does NOT cover:

- Extracting requirements from applicable regulations (covered in POL-5.31.3)
- Mapping requirements to controls (covered in POL-5.31.3)
- Monitoring for regulatory changes (covered in POL-5.31.4)
- Evidence management (covered in POL-5.31.4)

---

# Regulatory Identification Process

## Trigger Events for Regulatory Identification

[Organisation] shall initiate regulatory identification and applicability assessments when triggered by the following events:

### Periodic Review Triggers

**Annual Comprehensive Review** (Mandatory):

- Complete scan of regulatory landscape
- Review of all entries in ISMS-POL-00 for continued applicability
- Validation that no applicable regulations have been missed
- Performed in Q4 of each calendar year (or as defined by ISMS calendar)
- Responsibility: Compliance Officer in coordination with Legal Function

**Quarterly Environmental Scan** (Recommended):

- Focused scan of regulatory developments in key jurisdictions
- Review of regulatory monitoring alerts accumulated during quarter
- Identification of new or proposed regulations requiring attention
- Performed at end of each quarter
- Responsibility: Compliance Officer

### Expansion Triggers

Applicability assessment shall be initiated when [Organisation]:

**Enters New Geographic Market:**

- Establishes legal entity in new jurisdiction
- Opens office or operational facility in new location
- Begins marketing or selling services in new country or region
- Process data of individuals in new jurisdiction

**Offers New Services or Products:**

- Launches new service offering (e.g., cloud services, managed security, consulting)
- Enters new vertical market (e.g., healthcare, financial services, government)
- Begins processing new categories of data (e.g., health data, financial data, biometric data)
- Adopts new technologies with regulatory implications (e.g., AI, blockchain)

**Acquires Customers in Regulated Industries:**

- Contracts with customer in highly regulated sector (finance, healthcare, energy, etc.)
- Relationship involves access to customer's regulated data or systems
- Customer operates in jurisdiction new to [Organisation]

**Mergers and Acquisitions:**

- [Organisation] acquires another entity (inherit their regulatory obligations)
- [Organisation] is acquired (may trigger new obligations from parent company)
- Triggers comprehensive review of combined regulatory landscape

### Contractual Triggers

**New Customer Contracts:**

- Customer contract includes specific compliance requirements
- Customer conducts compliance due diligence questionnaire
- RFP/RFI includes regulatory or certification requirements
- Master Service Agreement includes regulatory compliance clauses

**New Supplier Agreements:**

- Supplier agreement includes pass-through compliance obligations
- [Organisation] is designated as subprocessor or service provider with inherited obligations
- Supplier certifications require [Organisation] to meet specific standards

**Partnership and Reseller Agreements:**

- Joint offering requiring compliance with partner's obligations
- Technology partner requires specific compliance posture
- Reseller agreement includes compliance commitments

### Certification and Accreditation Triggers

**Pursuing New Certifications:**

- Decision to pursue ISO 27001, SOC 2, PCI DSS v4.0.1, or other certification
- Certification body specifies regulatory requirements as part of certification
- Industry-specific accreditations with compliance components

**Certification Maintenance:**

- Surveillance audit identifies new regulatory requirements
- Certification standard updated with new compliance references
- Certification body issues new guidance on regulatory expectations

### Internal Triggers

**Strategic Initiatives:**

- Business strategy calls for entering regulated markets
- Digital transformation initiative involves regulated technologies
- New product development with regulatory implications

**Risk Assessment Findings:**

- Information security risk assessment identifies regulatory exposure
- Privacy impact assessment reveals potential regulatory applicability
- Threat intelligence indicates regulatory enforcement in [Organisation]'s domain

**Compliance Gap Identification:**

- Internal audit identifies potential applicable regulation not in POL-00
- Employee raises awareness of potentially applicable regulation
- Compliance self-assessment reveals knowledge gap

### External Triggers

**Regulatory Enactment:**

- New law or regulation enacted in jurisdiction where [Organisation] operates
- Regulatory authority issues new rules or guidance
- International treaty or agreement with compliance implications

**Industry Developments:**

- Industry association publishes new standards or guidance
- Peer organisations receive regulatory enforcement actions
- Industry working group recommends adoption of specific framework

**Regulatory Inquiry:**

- Regulatory authority contacts [Organisation] directly
- Industry survey from regulatory body
- Regulatory investigation or enforcement action in [Organisation]'s sector

## Sources for Regulatory Intelligence

[Organisation] shall utilize the following sources to identify potentially applicable regulations:

### Legal Databases and Research Services

**Commercial Legal Research Platforms:**

- Subscription-based services (e.g., LexisNexis, Westlaw, Bloomberg Law)
- Access to statutes, regulations, administrative codes across jurisdictions
- Alerting functionality for regulatory changes
- Searchable by jurisdiction, topic, industry, effective date

**Government Legal Databases:**

- Official government repositories (e.g., EUR-Lex for EU, Federal Register for U.S.)
- National legislative databases
- Regulatory authority websites
- Free but may lack advanced search and alerting

**Regulatory Technology (RegTech) Platforms:**

- Specialized compliance monitoring services (e.g., Compliance.ai, RegHub)
- AI-powered regulatory change detection
- Industry-specific regulatory tracking
- Often includes interpretation and impact analysis

**Usage Guidelines:**

- Maintain current subscriptions to primary legal research platform
- Configure alerts for key jurisdictions and topics
- Regular training for compliance staff on effective database usage
- Document search queries and results for audit trail

### Industry Associations and Standards Bodies

**Sector-Specific Associations:**

- Industry trade associations in sectors [Organisation] serves
- Associations publish regulatory updates, compliance guides, and best practices
- Examples: Financial services associations, healthcare industry groups, technology consortiums

**Cross-Industry Organisations:**

- Information security and privacy professional associations (e.g., IAPP, (ISC)², ISACA)
- Quality and compliance organisations (e.g., ISO national bodies)
- Regional business organisations

**Standards Development Organisations:**

- ISO (International Organisation for Standardization)
- NIST (National Institute of Standards and Technology)
- CIS (Center for Internet Security)
- Industry-specific standards bodies

**Usage Guidelines:**

- Maintain memberships in relevant associations
- Subscribe to regulatory update newsletters and alerts
- Participate in industry working groups on regulatory topics
- Attend conferences and webinars on regulatory developments

### Legal Counsel

**In-House Legal Team:**

- Primary source for legal interpretation of regulations
- Monitors legal developments relevant to [Organisation]
- Provides ongoing legal advice on compliance matters
- Coordinates with external counsel as needed

**External Legal Advisors:**

- Jurisdiction-specific counsel (for international operations)
- Specialized regulatory counsel (e.g., data protection, financial regulation)
- Engaged for specific matters or ongoing regulatory monitoring

**Specialized Regulatory Counsel:**

- Deep expertise in specific regulatory domains
- Retained for complex compliance questions
- Provides opinions on regulatory applicability and interpretation

**Usage Guidelines:**

- Regular (at least quarterly) legal briefings on regulatory landscape
- Standing agenda item in Legal/Compliance meetings
- Legal review of all Tier 1 applicability determinations
- External counsel engaged for jurisdictions where [Organisation] lacks in-house expertise

### Peer Networks and Professional Communities

**Industry Forums:**

- Compliance and legal forums within industry
- Information sharing and analysis centers (ISACs)
- Peer discussion groups on regulatory topics

**Professional Associations:**

- Compliance officers networks
- Data protection officers communities
- Information security professional groups

**Compliance Communities of Practice:**

- Cross-company compliance collaboration
- Benchmarking and best practice sharing
- Regulatory interpretation discussions

**Usage Guidelines:**

- Active participation in at least one relevant peer network
- Designated representatives attend regular meetings
- Share learnings while respecting confidentiality
- Verify peer information through authoritative sources before acting

### Professional Services Firms

**Audit Firms:**

- Big 4 and regional audit firms publish regulatory updates
- Industry-specific regulatory alerts
- Compliance advisory services
- Often provide complimentary regulatory briefings to clients

**Compliance Consultants:**

- Specialized regulatory compliance advisory
- Regulatory program assessments
- Compliance gap analysis services

**Regulatory Monitoring Services:**

- Third-party regulatory change monitoring
- Curated alerts and summaries
- Impact assessments and recommendations

**Usage Guidelines:**

- Subscribe to regulatory update services from audit firm or consultant
- Attend client briefings and webinars
- Leverage professional service providers for complex assessments
- Maintain relationships for ad-hoc consultations

### Customer and Supplier Channels

**Customer Requirements:**

- Compliance clauses in Master Service Agreements
- Security and compliance questionnaires (e.g., SIG, CAIQ)
- RFP/RFI compliance requirements
- Customer compliance audits and assessments

**Supplier Obligations:**

- Data Processing Agreements (DPAs) with inherited obligations
- Subprocessor agreements
- Supply chain compliance requirements
- Vendor assessment questionnaires

**Usage Guidelines:**

- Systematic review of all customer contracts for compliance clauses
- Legal review of supplier agreements for pass-through obligations
- Maintain database of contractual compliance requirements
- Feed contractual requirements into applicability assessment process

## Initial Screening Criteria

Before conducting full applicability assessment, [Organisation] shall apply initial screening to filter the universe of regulations to a manageable candidate set:

### Relevance Screening

**Question**: Does this regulation relate to information security, data protection, IT services, or [Organisation]'s information assets?

**Apply**:

- Regulations governing data protection, privacy, cybersecurity
- Regulations governing IT services, cloud services, managed services
- Regulations governing specific types of data [Organisation] processes
- Regulations governing information systems and technology infrastructure
- Regulations with information security provisions (even if broader scope)

**Exclude**:

- Purely operational regulations unrelated to information/IT (e.g., workplace safety, environmental)
- Financial reporting regulations without information security components
- Product safety regulations for physical products [Organisation] doesn't produce
- Regulations clearly outside [Organisation]'s domain

**Outcome**: If regulation is NOT relevant to information security or IT, **STOP** - do not proceed to full assessment. Document rationale and file in "Screened Out - Not Relevant" category.

### Jurisdictional Screening

**Question**: Does [Organisation] have any connection to the jurisdiction where this regulation applies?

**Connections Include**:

- Physical presence (office, facility, employees) in jurisdiction
- Legal entity registered in jurisdiction
- Customers or data subjects located in jurisdiction
- Providing services into jurisdiction (even without physical presence)
- Processing data subject to jurisdiction's laws
- Regulation claims extraterritorial reach affecting [Organisation]

**Outcome**: If [Organisation] has ZERO connection to jurisdiction and regulation makes NO extraterritorial claim, likely not applicable. However, proceed to full assessment if:

- Uncertainty about extraterritorial reach
- Potential future expansion to jurisdiction
- Indirect connection through customers or suppliers

### Operational Screening

**Question**: Does [Organisation]'s current or planned operations fall within this regulation's scope?

**Check**:

- Types of services [Organisation] provides vs. regulation's scope
- Industries [Organisation] serves vs. regulation's applicability
- Types of data [Organisation] processes vs. regulation's scope
- [Organisation]'s size, revenue, or other thresholds vs. regulation's applicability criteria

**Outcome**: If regulation clearly does NOT apply to [Organisation]'s operations (e.g., healthcare regulation when [Organisation] doesn't serve healthcare or process health data), likely not applicable. Proceed to full assessment if:

- Uncertainty about scope
- Potential future operations could trigger applicability
- Partial overlap with current operations

### Screening Decision Matrix

| Relevance | Jurisdiction | Operations | Decision |
|-----------|--------------|------------|----------|
| NOT Relevant | Any | Any | **STOP** - Screened Out |
| Relevant | NO Connection | NOT Applicable | **STOP** - Likely Not Applicable (document) |
| Relevant | NO Connection | Potentially Applicable | **PROCEED** - Full Assessment (potential future) |
| Relevant | Connection | NOT Applicable | **PROCEED** - Full Assessment (verify not applicable) |
| Relevant | Connection | Potentially Applicable | **PROCEED** - Full Assessment |
| Relevant | Connection | Clearly Applicable | **PROCEED** - Full Assessment (likely applicable) |

### Screening Documentation

For each regulation screened:

- Document regulation name, jurisdiction, brief description
- Record screening decision (Proceed to Full Assessment / Screened Out)
- Provide rationale for decision
- Reference source where identified
- Date and assessor name

Regulations screened out shall be retained in a "Reviewed but Not Applicable" file for potential future reference if circumstances change.

---

# Applicability Criteria Framework

For regulations that pass initial screening, [Organisation] shall conduct a structured applicability assessment using a **three-dimensional framework**:

1. **Geographic Scope**: Applicability based on WHERE [Organisation] operates
2. **Operational Scope**: Applicability based on WHAT [Organisation] does
3. **Contractual Scope**: Applicability based on AGREEMENTS [Organisation] has entered

Each dimension is evaluated independently, then combined for an overall applicability determination.

## Geographic Scope Assessment

### Geographic Applicability Criteria

**Criterion G1: Operations in Jurisdiction**

Question: Does [Organisation] conduct operations in the jurisdiction where this regulation applies?

Consider:

- Physical offices, facilities, or data centers in jurisdiction
- Employees working from jurisdiction
- Legal entities incorporated or registered in jurisdiction
- Business licenses or permits in jurisdiction

Evidence: Corporate registry records, office lease agreements, employment records, business license registrations

**Criterion G2: Customers or Data Subjects in Jurisdiction**

Question: Does [Organisation] serve customers physically located in the jurisdiction, or process data of individuals in the jurisdiction?

Consider:

- Customer contracts with parties located in jurisdiction
- End users accessing [Organisation]'s services from jurisdiction
- Data subjects whose personal data is protected by jurisdiction's laws
- Marketing or sales activities targeting jurisdiction

Evidence: Customer contracts, sales records, website analytics, data processing records

**Criterion G3: Targeting Jurisdiction**

Question: Does [Organisation] actively target individuals or entities in the jurisdiction?

Consider:

- Website available in jurisdiction's language(s)
- Prices displayed in jurisdiction's currency
- Marketing campaigns directed at jurisdiction
- Local payment methods accepted
- Compliance with jurisdiction's consumer protection laws

Evidence: Website content, marketing materials, payment gateway configurations

**Criterion G4: Data Processing in Jurisdiction**

Question: Does [Organisation] process data in the jurisdiction, even if [Organisation] has no other presence?

Consider:

- Servers or infrastructure located in jurisdiction
- Third-party service providers in jurisdiction processing data on [Organisation]'s behalf
- Data in transit through jurisdiction
- Backup or disaster recovery sites in jurisdiction

Evidence: Infrastructure diagrams, vendor agreements, data flow documentation

**Criterion G5: Extraterritorial Application**

Question: Does the regulation explicitly claim to apply beyond its jurisdiction's borders?

Consider:

- Regulation applies to organisations outside jurisdiction if they serve residents
- Regulation applies based on data subject location regardless of organisation location
- Examples: GDPR (EU), CCPA (California), LGPD (Brazil) all have extraterritorial provisions

Evidence: Regulatory text, legal analysis of extraterritorial provisions

### Geographic Scope Scoring

For each criterion G1-G5:

- **YES** = 1 point
- **NO** = 0 points
- **UNCERTAIN** = 0.5 points (triggers legal review)

**Geographic Applicability Score** = Sum of G1 through G5 (range: 0 to 5)

**Interpretation**:

- 0-1 points: Low geographic applicability
- 2-3 points: Moderate geographic applicability  
- 4-5 points: High geographic applicability

High score indicates strong geographic connection suggesting applicability. However, score alone does NOT determine final applicability—must consider all three dimensions.

## Operational Scope Assessment

### Operational Applicability Criteria

**Criterion O1: Service Type Alignment**

Question: Does [Organisation] provide types of services that fall within the regulation's scope?

Consider:

- Cloud services, hosting, SaaS (may trigger cloud/IT service regulations)
- Payment processing (may trigger financial services regulations)
- Healthcare services or health data processing (may trigger healthcare regulations)
- Telecommunications services (may trigger telecom regulations)
- Critical infrastructure services (may trigger CI protection regulations)

Evidence: Service catalog, service descriptions, SOWs, marketing materials

**Criterion O2: Industry Sector Alignment**

Question: Does [Organisation] serve industry sectors that are regulated by this regulation?

Consider:

- Financial services sector (banks, investment firms, insurance)
- Healthcare sector (providers, payers, health tech)
- Government sector (public sector, defense)
- Critical infrastructure sectors (energy, water, transportation)
- Regulation may apply to service providers TO these sectors even if not in sector directly

Evidence: Customer list, vertical market analysis, industry-specific contracts

**Criterion O3: Data Type Alignment**

Question: Does [Organisation] process types of data that are protected or regulated by this regulation?

Consider:

- Personal data / Personally Identifiable Information (PII)
- Special categories of personal data (health, biometric, genetic, race/ethnicity, etc.)
- Financial data (payment card data, banking data, financial account info)
- Government data (classified, controlled unclassified, law enforcement data)
- Trade secrets or confidential business information
- Children's data

Evidence: Data inventory, data classification register, data flow diagrams, data processing records

**Criterion O4: Organisational Characteristics**

Question: Does [Organisation] meet the regulation's applicability thresholds based on size, revenue, or other characteristics?

Consider:

- Number of employees (some regulations apply only above threshold)
- Annual revenue or turnover (financial thresholds)
- Volume of data processed (e.g., number of data subjects)
- Public vs. private entity
- For-profit vs. non-profit
- Organisational structure (subsidiary of regulated parent company)

Evidence: Financial statements, employee headcount reports, data processing volume metrics, corporate structure documents

**Criterion O5: Specific Operations Covered**

Question: Does [Organisation] perform specific operations or activities explicitly covered by the regulation?

Consider:

- E-commerce operations (may trigger consumer protection/e-commerce regulations)
- Cross-border data transfers (may trigger data transfer regulations)
- Automated decision-making or profiling (may trigger AI/algorithmic regulations)
- Marketing/advertising using personal data (may trigger marketing regulations)
- Biometric authentication/identification (may trigger biometric regulations)

Evidence: Operational documentation, technology documentation, process descriptions

### Operational Scope Scoring

For each criterion O1-O5:

- **YES** = 1 point
- **NO** = 0 points
- **UNCERTAIN** = 0.5 points (triggers further analysis)

**Operational Applicability Score** = Sum of O1 through O5 (range: 0 to 5)

**Interpretation**:

- 0-1 points: Low operational applicability
- 2-3 points: Moderate operational applicability
- 4-5 points: High operational applicability

## Contractual Scope Assessment

### Contractual Applicability Criteria

**Criterion C1: Customer Contractual Requirements**

Question: Do [Organisation]'s customer contracts explicitly require compliance with this regulation?

Consider:

- Master Service Agreements with compliance clauses
- Data Processing Agreements requiring processor compliance
- Statements of Work with specific regulatory requirements
- Customer compliance questionnaires expecting conformance
- Right to audit clauses covering regulatory compliance

Evidence: Executed customer contracts, compliance requirement matrices, customer audit reports

**Criterion C2: Supplier Pass-Through Obligations**

Question: Do [Organisation]'s agreements with suppliers create obligations on [Organisation] to comply with this regulation?

Consider:

- [Organisation] as subprocessor with obligations from primary processor
- Supply chain compliance requirements
- Supplier requiring [Organisation] to meet standards supplier must meet
- Flow-down clauses from prime contractor

Evidence: Supplier agreements, subprocessor agreements, supply chain contracts

**Criterion C3: Certification Requirements**

Question: Is compliance with this regulation required for certifications [Organisation] holds or pursues?

Consider:

- ISO 27001 may reference specific regulatory requirements
- SOC 2 Type II may include regulatory compliance in criteria
- Industry-specific certifications requiring regulatory compliance
- Certification body explicitly requiring conformance with regulation

Evidence: Certification standards, certification body requirements, audit reports, assessor guidance

**Criterion C4: Voluntary Commitments**

Question: Has [Organisation] made public commitments or voluntary pledges to comply with this regulation or framework?

Consider:

- Privacy policies stating compliance with specific regulations
- Marketing materials claiming certifications or compliance
- Public commitments to frameworks (e.g., Privacy Shield - historical example)
- Codes of conduct or industry pledges

Evidence: Published privacy policies, website statements, marketing materials, press releases

### Contractual Scope Scoring

For each criterion C1-C4:

- **YES** = 1 point
- **NO** = 0 points
- **UNCERTAIN** = 0.5 points

**Contractual Applicability Score** = Sum of C1 through C4 (range: 0 to 4)

**Interpretation**:

- 0 points: No contractual applicability
- 1-2 points: Moderate contractual applicability
- 3-4 points: High contractual applicability

## Combined Applicability Determination

### Dimension Weighting

All three dimensions carry equal weight in the determination. A regulation may be applicable based on strong showing in one dimension OR moderate showing across multiple dimensions.

### Applicability Decision Logic

**APPLICABLE** (Add to ISMS-POL-00):

- High score (4-5) in ANY dimension, OR
- Moderate scores (2-3) in TWO OR MORE dimensions, OR
- Explicit contractual requirement (C1 or C2 = YES), OR
- Legal opinion confirms applicability

**CONDITIONALLY APPLICABLE** (Add to ISMS-POL-00 as Tier 2):

- Moderate score (2-3) in ONE dimension only
- Potential future applicability (expansion plans)
- Voluntary adoption for competitive advantage

**NOT APPLICABLE** (Do not add to ISMS-POL-00):

- Low scores (0-1) across ALL dimensions
- Regulation explicitly excludes [Organisation]'s operations
- Legal opinion confirms non-applicability

### Special Cases

**Uncertain Determinations:**
If applicability is uncertain after assessment:

- Escalate to legal counsel for interpretation
- Consider engaging external regulatory counsel
- Document uncertainty and decision to include/exclude
- Monitor for clarifying guidance from regulatory authority
- Default to "Conditionally Applicable" (Tier 2) if doubt remains

**Conflicting Indicators:**
If some criteria suggest applicable and others suggest not:

- Legal counsel makes final determination
- Weight given to contractual requirements (C1, C2) as they create obligations regardless of legal applicability
- Document the conflict and rationale for final decision

---

# Three-Tier Categorization Framework

Regulations determined to be applicable shall be categorized into one of three tiers within ISMS-POL-00:

## Tier 1: Mandatory Compliance

### Definition

Regulations in Tier 1 are those with **LEGAL OBLIGATION** or **ENFORCEABLE CONTRACTUAL REQUIREMENT**.

Non-compliance results in concrete legal or contractual consequences: regulatory fines, sanctions, license revocation, contractual penalties, or loss of business relationships.

### Assignment Criteria

A regulation SHALL be classified as Tier 1 if it meets ANY of the following:

**Legal Obligation:**

- Statute, law, or regulation legally binding on [Organisation] in jurisdictions where [Organisation] operates
- High Geographic Applicability Score (4-5) AND regulation contains mandatory requirements ("shall", "must")
- Regulatory authority has jurisdiction over [Organisation] and enforcement power
- Non-compliance can result in fines, sanctions, or other legal penalties

**Contractual Enforceability:**

- Customer contract explicitly requires compliance and includes enforcement mechanisms (penalties, termination rights)
- Supplier agreement creates enforceable pass-through obligation
- Contractual commitment with material financial or business consequences if breached

**Certification Requirement:**

- Conformance required for certification [Organisation] holds (e.g., ISO 27001, SOC 2)
- Certification body audits compliance with regulation
- Loss of certification would have material business impact

### Treatment of Tier 1 Regulations

Tier 1 regulations receive highest priority:

- **Full compliance required** - no exceptions without documented risk acceptance
- **Executive approval required** for inclusion in Tier 1 (resource commitment)
- **Mandatory requirements extraction** (POL-5.31.3, IMP-5.31.2)
- **Mandatory control mapping** (POL-5.31.3, IMP-5.31.3)
- **High-priority gap remediation** - gaps must be addressed or formally accepted
- **Regular compliance audits** (internal and potentially external)
- **Continuous evidence collection** and maintenance
- **Annual review minimum** - more frequent if regulation is actively changing

### Examples of Tier 1 Classifications (Generic)

- Data protection law in jurisdiction where [Organisation] has operations and processes personal data
- Financial services regulation where [Organisation] provides IT services to financial institutions and is designated as service provider
- Customer contract with Fortune 500 client requiring SOC 2 compliance with contractual penalties for non-compliance
- ISO 27001 standard (if [Organisation] is certified)

## Tier 2: Conditional Applicability

### Definition

Regulations in Tier 2 are those that **MAY BECOME APPLICABLE** in the future or are **VOLUNTARILY ADOPTED** for strategic reasons.

These are not currently legally binding, but [Organisation] monitors them due to potential future applicability or because voluntary adoption provides competitive or strategic advantage.

### Assignment Criteria

A regulation SHALL be classified as Tier 2 if it meets ANY of the following:

**Potential Future Applicability:**

- [Organisation] is considering expansion into jurisdiction where regulation applies
- [Organisation] is planning to offer services that would trigger applicability
- [Organisation] may enter industry sector covered by regulation
- Proposed or draft regulation likely to be enacted and affect [Organisation]
- Thresholds not currently met but may be met with growth

**Voluntary Adoption:**

- Industry best practice framework [Organisation] chooses to adopt
- Competitive differentiator (compliance exceeds requirements)
- Customer expectations or market demands (even without contractual obligation)
- Regulatory safe harbor or preferred approach
- Strategic positioning for future opportunities

**Regulatory Uncertainty:**

- Applicability assessment is uncertain (moderate scores, unclear scope)
- Extraterritorial reach is ambiguous
- Awaiting legal clarification or regulatory guidance
- Default to Tier 2 pending clarity

### Treatment of Tier 2 Regulations

Tier 2 regulations receive moderate priority:

- **Monitoring and readiness** - stay informed of changes
- **Gap analysis** to understand compliance effort if/when triggered
- **Partial implementation** may occur if strategically valuable
- **Requirements extraction** optional (recommended for high-probability future applicability)
- **Annual or biennial review** - assess if circumstances have changed triggering move to Tier 1
- **Document strategic rationale** for voluntary adoption if applicable

### Examples of Tier 2 Classifications (Generic)

- Data protection regulation in jurisdiction [Organisation] is considering expanding to
- Industry-specific regulation for vertical market [Organisation] may enter
- Emerging regulation (draft/proposed) likely to affect [Organisation] once enacted
- NIST Cybersecurity Framework (CSF) 2.0 adopted voluntarily for maturity assessment

## Tier 3: Informational Reference

### Definition

Regulations and frameworks in Tier 3 are used for **GUIDANCE**, **BENCHMARKING**, or **BEST PRACTICES** only.

There is NO compliance obligation (legal or contractual), but these frameworks inform [Organisation]'s control design and provide reference points for maturity assessment.

### Assignment Criteria

A regulation or framework SHALL be classified as Tier 3 if:

**No Compliance Obligation:**

- Low applicability scores across all three dimensions
- No legal requirement to comply
- No contractual requirement to comply
- Not required for any certification [Organisation] holds

**Valuable for Reference:**

- Industry-recognized best practice
- Used by peers for benchmarking
- Provides useful guidance for control design
- Referenced by other applicable regulations
- Supports maturity assessment and improvement efforts

### Treatment of Tier 3 Regulations

Tier 3 regulations receive minimal formal treatment:

- **Reference for control design** - consulted when implementing or enhancing controls
- **Benchmarking** against industry standards
- **No evidence requirements** - no obligation to demonstrate conformance
- **Periodic review** (biennial or as needed) - assess if still useful reference
- **May inform but not require** - controls may be inspired by Tier 3 frameworks but no obligation

### Examples of Tier 3 Classifications (Generic)

- CIS Controls (Center for Internet Security Critical Security Controls)
- NIST Cybersecurity Framework (if not voluntarily adopted per Tier 2)
- OWASP guidelines (Open Web Application Security Project)
- Industry-specific best practice guides with no regulatory force

## Tier Assignment Decision Tree

```
START: Regulation passed initial screening
    ↓
Is there a LEGAL obligation?
(Regulation is law in jurisdiction where [Org] operates
 AND applies to [Org]'s operations)
    ├─ YES → TIER 1 (Mandatory Compliance)
    └─ NO → Continue
        ↓
Is there an ENFORCEABLE contractual requirement?
(Customer/supplier contract requires compliance
 WITH enforcement mechanism)
    ├─ YES → TIER 1 (Mandatory Compliance)
    └─ NO → Continue
        ↓
Is compliance REQUIRED for certification [Org] holds?
(ISO 27001, SOC 2, etc. requires this)
    ├─ YES → TIER 1 (Mandatory Compliance)
    └─ NO → Continue
        ↓
Is there POTENTIAL FUTURE applicability?
(Expansion plans, growth trajectory, proposed regulation)
    ├─ YES → TIER 2 (Conditional Applicability)
    └─ NO → Continue
        ↓
Is [Org] VOLUNTARILY adopting for strategic reasons?
(Competitive advantage, customer expectations)
    ├─ YES → TIER 2 (Conditional Applicability)
    └─ NO → Continue
        ↓
Is this useful as GUIDANCE/BENCHMARKING?
(Industry best practice, maturity reference)
    ├─ YES → TIER 3 (Informational Reference)
    └─ NO → DO NOT ADD TO POL-00
              (Not applicable, file in "Screened Out")
```

## Tier Mobility

Regulations may move between tiers as circumstances change:

**Tier 2 → Tier 1:**

- [Organisation] expands into jurisdiction (potential becomes actual)
- Proposed regulation is enacted
- Customer contract added requiring compliance
- [Organisation] meets threshold that triggers applicability

**Tier 1 → Tier 2:**

- [Organisation] exits jurisdiction or discontinues relevant operations
- Regulation is repealed or substantially amended to exclude [Organisation]
- Contract expires without renewal

**Tier 3 → Tier 2:**

- [Organisation] decides to voluntarily adopt framework for strategic reasons

**Any Tier → Removed:**

- Regulation is repealed entirely
- [Organisation] definitively determines non-applicability after initial classification
- Framework is superseded or no longer useful

Tier changes require re-assessment using full applicability methodology and appropriate approval (see Section 5).

---

# Documentation and Approval Requirements

## Applicability Assessment Documentation

For each regulation assessed (whether determined applicable or not), [Organisation] shall create and maintain comprehensive documentation:

### Required Documentation Elements

**Regulation Identification:**

- Full regulation name and common abbreviation
- Jurisdiction (country, state/province, multi-jurisdictional)
- Issuing authority (legislative body, regulatory agency)
- Effective date and any transition periods
- Source where identified (database, counsel, customer, etc.)

**Assessment Summary:**

- **Geographic Scope Assessment:**
  - Response to each criterion G1-G5 (Yes/No/Uncertain)
  - Geographic Applicability Score
  - Supporting rationale and evidence
- **Operational Scope Assessment:**
  - Response to each criterion O1-O5 (Yes/No/Uncertain)
  - Operational Applicability Score
  - Supporting rationale and evidence
- **Contractual Scope Assessment:**
  - Response to each criterion C1-C4 (Yes/No/Uncertain)
  - Contractual Applicability Score
  - Supporting rationale and evidence

**Overall Determination:**

- Applicability conclusion (Applicable / Conditionally Applicable / Not Applicable)
- Tier assignment (1, 2, 3, or N/A)
- Detailed rationale synthesizing three-dimensional assessment
- Any special considerations or edge cases
- Dissenting views or areas of uncertainty

**Supporting Evidence:**

- Links to or copies of regulatory text
- Legal opinions or memoranda
- Contract excerpts (if contractually driven)
- Jurisdictional analysis
- Precedent from similar regulations or peer organisations

**Assessment Metadata:**

- Assessor name and role
- Assessment date
- Reviewer name and role (if peer reviewed)
- Approver(s) and approval date(s)
- Next review date

### Documentation Templates

**Assessment Workbook 2: Applicability Matrix** provides standardized template for documentation. All assessments shall be documented using this template to ensure consistency.

Template includes:

- Structured form for three-dimensional assessment
- Scoring formulas
- Decision tree for tier assignment
- Approval signature blocks
- Version control

### Evidence Retention

Supporting evidence shall be attached to or referenced in the applicability assessment documentation and retained according to records retention policy (minimum: duration of applicability + 7 years, or as required by regulation).

## Approval Workflow

### Assessment and Review Stages

**Stage 1: Initial Assessment**

- Performed by: Compliance Officer or designated Legal/Compliance personnel
- Activities: Complete three-dimensional assessment, draft determination
- Output: Draft applicability assessment document
- Timeline: Within 10 business days of trigger event (or per IMP-5.31.1 schedule)

**Stage 2: Peer Review** (Recommended for all; Mandatory for Tier 1)

- Performed by: Second Compliance/Legal professional
- Activities: Review assessment for completeness, logic, evidence quality
- Output: Peer review comments, recommendation to proceed or revise
- Timeline: Within 5 business days of initial assessment

**Stage 3: Legal Review** (Mandatory for Tier 1; Optional for Tier 2/3)

- Performed by: In-house Legal Counsel (or external counsel for jurisdictions without in-house expertise)
- Activities: Validate legal interpretation, confirm applicability determination
- Output: Legal approval or request for revision, may include legal opinion
- Timeline: Within 10 business days of peer review

**Stage 4: ISMS Manager Review** (All Tiers)

- Performed by: ISMS Manager
- Activities: Review ISMS implications, consider integration with existing framework
- Output: ISMS Manager approval or concerns
- Timeline: Within 5 business days of legal review (or Stage 2 if no legal review)

**Stage 5: Executive Approval** (Mandatory for Tier 1; Not required for Tier 2/3)

- Performed by: Executive Management (as defined in POL-5.31.1 roles)
- Activities: Acknowledge compliance obligation, commit resources, approve inclusion in Tier 1
- Output: Executive approval signature
- Timeline: Within 10 business days of ISMS Manager review
- Note: Executive approval signifies organisational commitment to comply

### Approval Authority Matrix

| Tier | Compliance Officer | Legal Counsel | ISMS Manager | Executive Mgmt |
|------|-------------------|---------------|--------------|----------------|
| **Tier 1** | Assesses (R) | Reviews & Approves (A) | Reviews & Approves (A) | **Approves** (A) |
| **Tier 2** | Assesses (R) | Reviews (C) | **Approves** (A) | Informed (I) |
| **Tier 3** | Assesses (R) | Optional (C) | **Approves** (A) | Informed (I) |

R=Responsible, A=Accountable/Approves, C=Consulted, I=Informed

### Expedited Approval Process

In urgent situations (e.g., customer contract closing contingent on compliance commitment, imminent regulatory deadline), an expedited approval process may be used:

- Compress timelines to 2-3 business days per stage
- Concurrent review stages where possible
- Verbal approvals acceptable with documented follow-up signatures within 5 business days
- Escalation to highest available authority if designated approver unavailable
- **All expedited approvals subject to post-approval audit** within 30 days to validate process integrity

Expedited process requires ISMS Manager authorisation and documentation of urgency rationale.

### Disputed Determinations

If assessors, reviewers, or approvers disagree on applicability or tier:

**Internal Resolution:**

- Compliance Officer and ISMS Manager discuss, attempt consensus
- Legal Counsel provides definitive interpretation on legal matters
- If consensus cannot be reached internally, escalate to Executive Management

**External Resolution:**

- For complex legal questions: Engage external legal counsel for opinion
- For regulatory interpretation: Consider direct inquiry to regulatory authority (with legal counsel guidance)
- Document dispute, resolution process, and final decision with supporting rationale

**Default Position:**

- If doubt remains after resolution efforts: Default to "Applicable" and higher tier (Tier 1 over Tier 2, Tier 2 over Tier 3)
- Rationale: Conservative approach reduces risk of non-compliance
- Re-assess when additional clarity becomes available

## Adding to ISMS-POL-00

Upon final approval of applicability determination:

### POL-00 Entry

ISMS Manager shall add regulation to ISMS-POL-00 (Regulatory Applicability Framework) in the appropriate tier section with the following information:

- Regulation ID (assigned systematically, e.g., REG-001, REG-002)
- Regulation name
- Jurisdiction
- Issuing authority
- Effective date
- Tier (1, 2, or 3)
- Applicability status (Applicable, Conditionally Applicable)
- Brief applicability rationale (1-2 sentences)
- Link to full applicability assessment documentation
- Last review date
- Next review date (annual for Tier 1, biennial for Tier 2/3, or as determined)
- Responsible party (typically Compliance Officer)

### Version Control

- Increment POL-00 version number
- Update version history table with date, author, and summary of change ("Added REG-XXX [Regulation Name] to Tier [X]")
- Distribute updated POL-00 to stakeholders per distribution list

### Communication

Compliance Officer or ISMS Manager shall notify relevant stakeholders:

**For Tier 1 additions:**

- Executive Management (formal notification)
- All Control Owners (broad awareness)
- Affected business units (if regulation impacts specific operations)
- Internal Audit (for audit planning)
- Customer-facing teams (if customer-driven requirement)

**For Tier 2/3 additions:**

- ISMS Manager
- Affected Control Owners (targeted notification)
- Compliance team

**Communication content:**

- Regulation added and tier
- High-level implications
- Next steps (e.g., requirements extraction scheduled)
- Point of contact for questions

### Triggering Downstream Processes

Adding regulation to POL-00 Tier 1 or 2 triggers:

- **Requirements Extraction** (POL-5.31.3, IMP-5.31.2): Schedule extraction of specific requirements from regulation
- **Control Mapping** (POL-5.31.3, IMP-5.31.3): Following requirements extraction, map to controls
- **Gap Analysis**: Identify any compliance gaps
- **Evidence Planning** (POL-5.31.4, IMP-5.31.5): Determine evidence requirements

ISMS Manager coordinates these downstream activities.

---

# Review Frequency and Update Triggers

Applicability determinations are not static. [Organisation] shall review and, where appropriate, update applicability assessments according to the following schedule and triggers:

## Periodic Review Schedule

### Annual Comprehensive Review (Mandatory)

**Scope**: ALL regulations in ISMS-POL-00 (Tiers 1, 2, and 3)

**Timing**: Q4 of each calendar year (or alternative schedule defined in ISMS management review cycle)

**Process**:
1. Compliance Officer reviews each regulation in POL-00
2. Confirm [Organisation]'s circumstances have not changed affecting applicability
3. Confirm regulation itself has not been amended in ways affecting applicability
4. Validate tier assignment remains appropriate
5. Document review date and outcome ("No change", "Tier modified", "Removed", etc.)
6. Update "Last Review Date" and "Next Review Date" fields in POL-00

**Documentation**: Annual review summary report documenting scope, findings, and any changes

**Approval**: ISMS Manager approval of annual review summary

### Tier-Specific Review Frequency

**Tier 1 Regulations**:

- Minimum: Annual review (per 6.1.1)
- Recommended: Semi-annual review for rapidly evolving regulations
- Mandatory: Event-driven review (Section 6.2) takes precedence over scheduled reviews

**Tier 2 Regulations**:

- Minimum: Annual review (per 6.1.1)
- Alternative: Biennial review acceptable for stable frameworks with low probability of change

**Tier 3 Regulations**:

- Minimum: Biennial review
- May review "as needed" based on [Organisation]'s use of framework for reference

## Event-Driven Review Triggers

Applicability assessment shall be revisited (outside of scheduled reviews) when triggered by:

### Organisational Changes

**Geographic Expansion or Contraction:**

- [Organisation] enters new jurisdiction → Review regulations in that jurisdiction
- [Organisation] exits jurisdiction → Review regulations dependent on presence there
- Trigger: Within 30 days of expansion/contraction decision or event

**Operational Changes:**

- New service offerings → Review regulations covering those services
- Entry into new industry vertical → Review sector-specific regulations
- New data types processed → Review data-specific regulations
- Discontinuation of services → Review if regulations remain applicable
- Trigger: During planning phase (before launch) and within 30 days of operational change

**Organisational Restructuring:**

- Merger or acquisition → Comprehensive review of combined entity's obligations
- Divestiture → Review if obligations remain post-divestiture
- Change in parent company → Review if new obligations flow down
- Trigger: As part of merger/acquisition due diligence; within 60 days of transaction close

**Threshold Changes:**

- [Organisation] crosses regulatory threshold (e.g., number of employees, revenue, data volume)
- Trigger: Continuous monitoring; formal review when threshold crossed

### Regulatory Changes

**Regulation Amended:**

- Amendments may change scope, applicability criteria, or requirements
- Trigger: Regulatory change monitoring process (POL-5.31.4, IMP-5.31.4) detects amendment
- Action: Impact assessment includes re-assessment of applicability if scope changed

**New Regulation Enacted:**

- Already covered by identification process (Section 2)
- Trigger: Multiple sources (per Section 2.2)

**Regulation Repealed or Superseded:**

- Regulation in POL-00 is repealed, rescinded, or superseded by newer regulation
- Trigger: Regulatory change monitoring
- Action: Mark as "Superseded" in POL-00, conduct applicability assessment for replacement regulation

**Regulatory Guidance or Interpretation Issued:**

- Regulatory authority issues guidance clarifying scope or applicability
- Court decision interprets regulation in way affecting applicability
- Trigger: Regulatory monitoring or legal counsel alert
- Action: Review applicability determination in light of new interpretation

### Contractual Changes

**New Customer Contract:**

- Contract includes compliance requirements → Applicability assessment for those requirements
- Trigger: Contract execution or during pre-contract due diligence
- Action: Assess contractually-mandated regulations (may be Tier 1 if enforceable)

**Contract Renewal or Amendment:**

- Customer adds compliance requirements during renewal
- Compliance obligations modified
- Trigger: Contract renewal process
- Action: Review applicability based on updated contract terms

**Contract Expiration:**

- Major customer contract expires without renewal
- Contract was sole driver of applicability (Criterion C1)
- Trigger: Contract expiration date
- Action: Assess if regulation still applicable without contract (may drop from Tier 1 to Tier 2 or remove)

**New Supplier Agreement:**

- Agreement creates pass-through obligations
- Trigger: Supplier contract execution
- Action: Applicability assessment for passed-through requirements

### Certification Changes

**New Certification Pursued:**

- [Organisation] decides to pursue new certification (e.g., SOC 2, PCI DSS v4.0.1)
- Trigger: Certification decision
- Action: Review certification requirements for applicable regulations

**Certification Standard Updated:**

- Standard revised with new regulatory references
- Trigger: Certification body notification or standards body publication
- Action: Review updated standard for new applicability

## Escalation for Applicability Disputes

If applicability determination is disputed (internal disagreement or challenge from external party):

### Internal Disputes

**Typical Scenarios:**

- Business unit claims regulation doesn't apply; Compliance claims it does
- Control owner disputes tier assignment (e.g., requests Tier 2 instead of Tier 1 due to implementation burden)
- Legal and Compliance disagree on interpretation

**Resolution Process:**
1. **Discussion**: Disputing parties meet to understand positions and evidence
2. **Compliance Officer Decision**: If dispute at operational level, Compliance Officer makes determination
3. **Legal Counsel Review**: For legal interpretation disputes, Legal Counsel has final say on legal matters
4. **Executive Escalation**: For disputes involving resource commitments or risk acceptance, escalate to Executive Management
5. **External Counsel**: For complex legal questions, engage external counsel for independent opinion

**Documentation**: Dispute must be documented including positions, evidence, resolution process, and final decision with rationale

**Timeline**: Disputes should be resolved within 30 days of identification; interim position of "Applicable" maintained until resolved

### External Challenges

**Scenarios:**

- Regulatory authority asserts regulation applies; [Organisation] believes it does not
- Customer disputes [Organisation]'s position on applicability
- Auditor questions applicability determination

**Response:**
1. **Gather Evidence**: Compile applicability assessment documentation and supporting evidence
2. **Legal Counsel Review**: Engage legal counsel to review position and external assertion
3. **External Legal Opinion**: Consider obtaining independent legal opinion
4. **Direct Regulatory Inquiry**: With counsel guidance, consider direct inquiry to regulatory authority
5. **Resolve**: Based on analysis and legal advice, confirm or revise determination
6. **Document**: Thoroughly document external challenge and resolution

**Interim Position**: During dispute resolution, unless legal counsel advises otherwise, maintain original determination or adopt more conservative position (treat as applicable) to reduce compliance risk.

## Review Documentation

All reviews (periodic and event-driven) shall be documented:

**Review Record:**

- Regulation reviewed
- Type of review (Annual, Event-Driven, Dispute Resolution)
- Date of review
- Reviewer name
- Outcome (No Change, Tier Changed, Removed from POL-00, Added to POL-00)
- Rationale for outcome (if changed)
- Approver and date (if determination changed)

**Review Log**: Maintain centralized review log recording all reviews. Supports demonstration of diligent ongoing management of regulatory landscape.

---

# Document Control and Related Documents

## Document Information

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-POL-A.5.31.2 |
| **Document Title** | Legal, Statutory, Regulatory and Contractual Requirements: Regulatory Applicability Methodology |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal Use |
| **Owner** | Compliance Officer |
| **Author** | [Name] |
| **Effective Date** | [To Be Determined upon approval] |
| **Review Frequency** | Annually, or upon significant change to methodology or applicability framework |
| **Next Review Date** | [12 months from Effective Date] |

## Approval

This policy requires approval from the following roles:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Compliance Officer** | [Name] | ___________________ | __________ |
| **Legal Counsel** | [Name] | ___________________ | __________ |
| **ISMS Manager** | [Name] | ___________________ | __________ |
| **Executive Management** | [Name] | ___________________ | __________ |

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [Date] | [Name] | Initial draft for review |
| 1.0 | [Date] | [Name] | Initial approved release |

## Related Documents

**Prerequisite Documents:**

- **ISMS-POL-A.5.31.1**: Executive Summary & Control Alignment (framework foundation)

**Coordinating Documents:**

- **ISMS-POL-00**: Regulatory Applicability Framework (regulatory register maintained using this methodology)

**Downstream Documents:**

- **ISMS-POL-A.5.31.3**: Requirements Extraction & Control Mapping Framework (next phase after applicability determined)
- **ISMS-POL-A.5.31.4**: Change Management & Evidence Framework (ongoing management including regulatory change monitoring)

**Implementation Guides:**

- **ISMS-IMP-A.5.31.2-UG/TG**: Regulatory Applicability Assessment Process (step-by-step procedures for executing this methodology)

**Assessment Tools:**

- **Assessment Workbook 1**: Regulatory Inventory (comprehensive list of regulations)
- **Assessment Workbook 2**: Applicability Matrix (structured assessment template)

**Standards:**

- ISO/IEC 27001:2022 - Information Security Management Systems - Requirements (Control A.5.31)
- ISO/IEC 27002:2022 - Information Security Controls (Section 5.31)

## Distribution and Access

**Distribution List:**

- Executive Management Team
- Compliance Officer / Legal Function
- ISMS Manager
- Business Development (for new contracts/customers)
- Operations Leadership (for operational changes triggering reviews)
- Internal Audit Team

**Access Level**: Internal Use

**Document Location**: [Organisation]'s Document Management System: [Path/URL]

---

# Definitions

**Applicability**: Determination that a regulation applies to [Organisation] based on geographic, operational, or contractual criteria.

**Contractual Obligation**: Requirement imposed by contract (customer, supplier, partner) that creates enforceable compliance obligation.

**Geographic Scope**: Applicability based on where [Organisation] operates, where customers are located, or extraterritorial provisions.

**Legal Obligation**: Requirement imposed by statute, law, or regulation that is legally binding and enforceable.

**Operational Scope**: Applicability based on what services [Organisation] provides, what data it processes, or what operations it conducts.

**Regulation**: General term encompassing laws, statutes, regulations, directives, contractual requirements, and standards (regulatory requirements).

**Three-Tier Framework**: Categorization system classifying regulations as Tier 1 (Mandatory), Tier 2 (Conditional), or Tier 3 (Informational).

**Trigger Event**: Circumstance initiating regulatory identification or re-assessment of applicability.

---

**END OF DOCUMENT**

---

*This policy establishes [Organisation]'s systematic methodology for regulatory applicability determination, feeding into ISMS-POL-00 and enabling downstream requirements extraction and control mapping.*
<!-- QA_VERIFIED: 2026-03-01 -->
