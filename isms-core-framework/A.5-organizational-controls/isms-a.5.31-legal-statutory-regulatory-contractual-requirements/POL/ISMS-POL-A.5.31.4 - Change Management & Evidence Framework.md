<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.31.4:framework:GOV-POL:a.5.31.4 -->
**ISMS-POL-A.5.31.4: Change Management & Evidence Framework**
**Legal, Statutory, Regulatory and Contractual Requirements**

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Change Management & Evidence Framework |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.31.4 |
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

# Introduction & Relationship to 5.31.1/5.31.2/5.31.3

## Purpose of This Policy Section

This policy section establishes [Organization]'s systematic framework for maintaining the regulatory compliance framework over time and demonstrating compliance through systematic evidence management. It defines the processes by which regulatory changes are detected, assessed, and incorporated into the compliance framework, and how evidence of compliance is collected, managed, and presented for audits.

**This is the "steady-state operation"** of the regulatory compliance framework—the processes that keep the framework current, accurate, and audit-ready as regulations evolve and [Organization] implements controls.

## Framework Lifecycle: Setup → Maintain → Demonstrate

The regulatory compliance framework operates in a continuous lifecycle:

**ISMS-POL-A.5.31.1** (Executive Summary & Control Alignment) established the framework foundation, governance structure, roles, and integration with ISMS-POL-00. It defined the "what" and "why" of the regulatory compliance architecture.

**ISMS-POL-A.5.31.2** (Regulatory Applicability Methodology) defined how [Organization] determines WHICH regulations apply based on geographic, operational, and contractual criteria. It provides the systematic process for populating and maintaining the regulatory register (ISMS-POL-00).

**ISMS-POL-A.5.31.3** (Requirements Extraction & Control Mapping Framework) defined how [Organization] extracts specific requirements from applicable regulations, maps them to ISO 27001 controls, identifies gaps, and maintains traceability. It provides the "translation layer" from legal language to security controls.

**ISMS-POL-A.5.31.4** (this document) defines how [Organization] maintains the framework over time and proves compliance through evidence:

- **Regulatory monitoring**: How [Organization] detects changes to applicable regulations
- **Impact assessment**: How [Organization] evaluates regulatory changes for impact on compliance framework
- **Framework updates**: How [Organization] maintains Requirements Register, Control Mapping Matrix, and related documents
- **Evidence management**: How [Organization] systematically collects, stores, verifies, and presents evidence of compliance
- **Compliance reporting**: How [Organization] communicates compliance status internally and externally
- **Records retention**: How [Organization] manages compliance records lifecycle

Together, these four policy sections (5.31.1-5.31.4) provide comprehensive governance for regulatory compliance within the ISMS.

## The Ongoing Challenge

The regulatory compliance framework is not "set and forget." Multiple forces drive continuous maintenance:

**Regulatory Landscape Evolution**:

- Legislators enact new laws and regulations
- Regulators amend existing requirements (updates, clarifications, expansions)
- Regulations are repealed or superseded
- Regulatory guidance and interpretations evolve
- Enforcement priorities shift
- **Challenge**: Framework must stay current with legal landscape

**Organizational Changes**:

- Business expansion (new markets, new services, new customers)
- Mergers and acquisitions
- Technology changes (cloud migration, new systems)
- Process changes
- Staffing changes
- **Challenge**: Framework must reflect current organizational reality

**Control Implementation Evolution**:

- Controls are implemented (gaps closed)
- Controls are enhanced (partial coverage → full coverage)
- Controls are retired or replaced
- Evidence accumulates
- **Challenge**: Framework must reflect actual control state, not just planned state

**Audit Requirements**:

- External auditors require current, accurate evidence
- Regulatory audits and inspections
- Customer audits
- Certification body surveillance audits
- **Challenge**: Evidence must be current, complete, accessible, and verifiable

**This policy section addresses all four challenges** through systematic monitoring, assessment, maintenance, and evidence management processes.

## Document Scope

This policy section applies to:

- **All regulations** maintained in ISMS-POL-00 (Tier 1 Mandatory, Tier 2 Conditional, and relevant Tier 3 Informational)
- **All compliance framework documents** (Requirements Register, Control Mapping Matrix, Gap Register, Evidence Register)
- **All personnel** involved in regulatory monitoring, compliance assessment, control implementation, and audit preparation
- **All evidence** demonstrating compliance with applicable regulations

This document does NOT:

- Define initial applicability determination (covered in 5.31.2)
- Define requirements extraction methodology (covered in 5.31.3)
- Provide operational step-by-step procedures (covered in IMP-5.31.4 and IMP-5.31.5)
- Address non-regulatory information security risks (covered in ISMS risk management processes)

---

# Regulatory Change Monitoring

Regulatory change monitoring is the systematic, ongoing process of detecting changes to the regulatory landscape that may affect [Organization]'s compliance obligations.

## Monitoring Sources

[Organization] SHALL monitor multiple sources for regulatory changes to ensure comprehensive coverage of the regulatory landscape.

### Legal Databases & Subscription Services

**Commercial Legal Research Platforms**:

- Services such as LexisNexis, Westlaw, Bloomberg Law, or equivalent provide comprehensive regulatory databases with change tracking
- Coverage: Laws, regulations, administrative rules, regulatory guidance, enforcement actions
- Features:
  - **Change alerts**: Automated notifications when tracked regulations are amended
  - **Legislative tracking**: Monitor bills/proposals before they become law
  - **Citator services**: Track subsequent amendments and related materials
  - **Jurisdiction coverage**: Multi-jurisdiction monitoring (domestic and international)

**Regulatory Technology (RegTech) Platforms**:

- Specialized compliance platforms (Compliance.ai, Ascent, ComplyAdvantage, or equivalent)
- Purpose-built for regulatory change monitoring
- Features:
  - AI/ML-powered change detection
  - Impact analysis capabilities
  - Regulatory mapping to business operations
  - Obligation extraction and tracking

**Jurisdiction-Specific Legal Databases**:

- National or regional legal databases (e.g., EUR-Lex for EU, Federal Register for US, SR for Switzerland)
- Official government legal information systems
- Often free or lower-cost than commercial platforms
- Authoritative source for official regulatory text

**Usage**: Subscribe to relevant platforms based on jurisdictions where [Organization] operates and is regulated. Configure alerts for regulations in ISMS-POL-00.

### Government & Regulatory Authority Notifications

**Direct Regulatory Authority Sources**:

- Monitor websites of regulatory authorities directly (e.g., Data Protection Authority, Financial Regulator, Sector Regulator)
- Official channels provide earliest and most authoritative information
- Sources:
  - **Email subscription lists**: Regulatory bulletins, enforcement alerts
  - **RSS feeds**: Automated update feeds
  - **Agency newsletters**: Periodic publications
  - **Press releases**: Major regulatory changes announced

**Official Gazettes and Registers**:

- Official publications where new laws and regulations are published (e.g., Official Journal of the European Union, Federal Register in US)
- Legal requirement in many jurisdictions for public notice
- Subscription or monitoring services available

**Public Comment Periods**:

- Proposed regulations often open for public comment before finalization
- Monitoring proposals enables early awareness and preparation
- Opportunity to participate in regulatory development (submit comments)
- Advance warning (typically months before regulation becomes effective)

**Final Rule Publications**:

- Monitor when proposed regulations become final
- Effective dates, transition periods, compliance deadlines published
- Preambles often provide regulatory intent and interpretation guidance

**Usage**: Identify applicable regulatory authorities from ISMS-POL-00 (by regulation). Subscribe to direct notifications from each authority. Designate responsible party to monitor these sources.

### Industry Associations & Working Groups

**Sector-Specific Associations**:

- Trade associations for [Organization]'s industry sector
- Examples: Financial services associations, technology industry groups, healthcare associations
- Services:
  - Regulatory updates tailored to sector
  - Interpretation guidance for complex regulations
  - Best practice sharing for compliance
  - Industry position papers and advocacy

**Cross-Industry Compliance Groups**:

- Broad compliance and regulatory professional associations
- Examples: International Compliance Association (ICA), Society of Corporate Compliance & Ethics (SCCE)
- Focus on compliance methodology and trends across sectors

**Working Groups & Task Forces**:

- Industry-regulator collaborative groups
- Standards development organizations (ISO, NIST, etc.)
- Regulatory sandbox participants
- Information sharing and analysis centers (ISACs) for sector-specific threats and regulatory intelligence

**Participation Benefits**:

- Early awareness of regulatory developments
- Peer learning and best practice sharing
- Collective interpretation of ambiguous requirements
- Influence on regulatory development through industry voice

**Usage**: Join relevant industry associations. Participate in regulatory working groups where applicable. Assign staff to monitor association communications and attend relevant events.

### Legal Counsel Updates

**In-House Legal Team**:

- If [Organization] has in-house legal counsel, establish regular regulatory briefings
- Legal counsel monitors regulatory developments relevant to [Organization]'s operations
- Quarterly (minimum) briefings to Compliance Officer and ISMS Manager
- Ad-hoc briefings for urgent regulatory changes

**External Legal Advisors**:

- Retained law firms by jurisdiction or specialty
- Subscription to client alerts and legal bulletins
- Examples: Data privacy law firm alerts on privacy regulations, employment law updates, sector-specific regulatory counsel
- Periodic consultations (quarterly or semi-annual) for comprehensive regulatory landscape review

**Legal Bulletins & Client Alerts**:

- Law firms publish alerts on significant regulatory changes
- Often free subscription for clients and prospects
- Timely, expert interpretation of new regulations
- Practical implications highlighted

**Proactive Legal Counsel Engagement**:

- Request legal counsel to proactively monitor specific regulations (Tier 1 Mandatory from ISMS-POL-00)
- Legal counsel may attend regulatory proceedings, read proposed rules, track legislative calendars
- Higher cost but highest quality regulatory intelligence

**Usage**: Establish clear scope with legal counsel for regulatory monitoring. Designate primary legal contact for compliance matters. Review legal counsel alerts promptly and assess relevance to [Organization].

### Peer Networks & Forums

**Compliance Professional Networks**:

- Informal and formal networks of compliance professionals
- Peer sharing of regulatory intelligence
- Examples: LinkedIn compliance groups, Slack channels, professional association forums
- Value: Real-world interpretation, implementation challenges, auditor expectations

**Information Sharing Groups**:

- Sector-specific Information Sharing and Analysis Centers (ISACs)
- Cybersecurity and compliance intelligence sharing
- Often non-profit, member-driven
- Focus on threats, incidents, and regulatory developments affecting sector

**Conferences & Webinars**:

- Industry conferences often feature regulatory update sessions
- Regulator speakers provide insights into enforcement priorities and interpretations
- Networking opportunities with peers facing similar compliance challenges
- Continuing professional education

**Professional Discussion Forums**:

- Online communities (Reddit r/compliance, specialized forums, LinkedIn groups)
- Moderated discussions on regulatory changes and interpretations
- Caution: Verify information from authoritative sources; forums are discussion not gospel

**Usage**: Participate in 2-3 high-quality peer networks relevant to [Organization]'s sector and regulatory exposure. Attend at least one annual conference focused on regulatory compliance. Share learnings internally.

### Professional Services

**Audit Firm Regulatory Alerts**:

- Big 4 and other audit firms publish regulatory alerts for clients
- Expertise in interpreting regulatory impact on financial reporting, controls, compliance
- Often sector-specific alerts (e.g., "DORA implications for financial services")
- Subscription typically included for audit clients

**Compliance Consultants**:

- Specialized consultancies focused on regulatory compliance
- Proactive monitoring and advisory services
- Costly but high-touch, tailored to [Organization]'s needs
- May provide gap analysis, remediation planning, implementation support

**Specialized Regulatory Advisors**:

- Boutique firms specializing in specific regulations (GDPR specialists, HIPAA consultants, PCI DSS v4.0.1 QSAs)
- Deep expertise in narrow domain
- Valuable for complex, high-stakes regulatory requirements

**Usage**: Leverage professional services strategically for complex or high-risk regulations. For routine monitoring, rely on lower-cost sources (databases, direct regulatory notifications). Engage consultants for interpretation and implementation support when needed.

### News & Media (With Verification)

**Industry Press**:

- Trade publications for [Organization]'s industry
- Examples: Compliance Week, Risk.net, SC Magazine, PrivacyTech
- Timely reporting on regulatory developments
- Interviews with regulators, analysis of trends

**Legal News Services**:

- Specialized legal news (Law360, Legal Dive, JDSupra)
- Regulatory enforcement actions and court decisions
- Emerging regulatory trends and proposals

**General Business News**:

- Major regulatory changes covered by mainstream business media
- Bloomberg, Reuters, Wall Street Journal, Financial Times
- High-level awareness of significant developments

**Verification Requirement**:

- News media is SECONDARY source
- Always verify regulatory changes through authoritative primary sources
  - Primary sources: Regulatory authority website, official gazette, legal database
- News provides awareness; official sources provide certainty
- Do NOT base compliance decisions on media reports alone

**Usage**: Monitor news media for awareness of potential regulatory changes. When media reports significant development, immediately verify through primary source. Use news as trigger for deeper investigation, not as authoritative source itself.

## Monitoring Frequency

Monitoring frequency SHALL be risk-based, with higher-risk regulations monitored more frequently.

### Continuous Monitoring (High-Priority)

**Tier 1 Regulations** (Mandatory Compliance from ISMS-POL-00):

- Set up real-time or daily alerts
- Any change to mandatory compliance regulation requires immediate awareness
- Rationale: Non-compliance has direct legal, financial, or contractual consequences

**Regulations with History of Frequent Change**:

- Some regulations are amended frequently (e.g., tax law, sector regulations in rapidly evolving industries)
- Continuous monitoring prevents surprises
- Historical analysis: Review past 3-5 years of amendments to identify "high-change" regulations

**Regulations with Upcoming Effective Dates**:

- Regulations recently enacted but not yet effective
- Transition period may have milestones or preparatory requirements
- Monitor for guidance, FAQs, enforcement policies during transition
- Example: DORA effective January 2025 → continuous monitoring through transition period

**Implementation**:

- Configure automated alerts in legal databases for Tier 1 regulations
- Email subscriptions to regulatory authorities governing Tier 1 regulations
- Designate Compliance Analyst to review alerts daily
- Escalate significant changes immediately to Compliance Officer

### Periodic Review (Lower Priority)

**Tier 2 Regulations** (Conditional Applicability from ISMS-POL-00):

- Monthly or quarterly monitoring
- If condition triggering applicability met, these become Tier 1 and move to continuous monitoring
- Until then, periodic check sufficient
- Example: PCI DSS v4.0.1 if [Organization] does not currently process payment cards but may in future

**Tier 3 Regulations** (Informational Reference from ISMS-POL-00):

- Quarterly or semi-annual monitoring
- These are best practices and guidance, not legal mandates
- Monitor for potential transition to Tier 2/1 (e.g., voluntary framework becomes regulatory requirement)
- Monitor for useful updates to inform control implementation

**Scheduled Calendar Approach**:

- Create monitoring calendar with scheduled review dates
- Assign specific regulations to specific review dates (distribute workload)
- Calendar reminders/tasks in project management or compliance software
- Example: "Review Tier 2 regulations 1-10: First week of January, April, July, October"

### Alert-Based Monitoring

**Legal Database Alerts**:

- Configure saved searches/alerts in commercial legal platforms
- Alert criteria:
  - Specific regulation cited (e.g., "GDPR Article 32")
  - Specific regulatory authority (e.g., "European Data Protection Board")
  - Specific keywords (e.g., "cybersecurity requirements" + "financial services")
- Alerts delivered via email, dashboard, RSS feed

**Email Notifications from Authorities**:

- Subscribe to regulatory authority mailing lists
- Automatic delivery of new guidance, proposed rules, enforcement actions
- Typically free and authoritative

**RSS Feed Subscriptions**:

- Many regulatory authorities publish RSS feeds
- Aggregate multiple RSS feeds in reader (Feedly, Inoreader, or equivalent)
- Efficient way to monitor multiple sources in single location

**Automated Monitoring Tools**:

- RegTech platforms with automated change detection
- AI-powered monitoring flags relevant changes based on [Organization]'s profile
- Reduces manual effort, increases coverage

**Alert Management**:

- Designate primary recipient for alerts (Compliance Analyst or Compliance Officer)
- Review alerts within 24-48 hours
- Triage: Relevant (log in Change Register) vs. Not Relevant (discard)
- Escalate relevant changes for impact assessment

### Adaptive Frequency

**Increase Monitoring Frequency**:

- During legislative sessions (when legislature is in session, more laws enacted)
- When regulatory review or reform is expected (e.g., government announced comprehensive regulatory review)
- When regulatory change is proposed (monitor through public comment, finalization, implementation)
- Industry events suggesting regulatory attention (major breach, scandal, enforcement action in sector)

**Decrease Monitoring Frequency**:

- Mature, stable regulations with long history of no changes
- Regulations in jurisdictions [Organization] is exiting
- Regulations that may transition from Tier 2 to Tier 3 (condition no longer likely to be met)

**Continuous Adjustment**:

- Review monitoring frequency quarterly
- Adjust based on regulatory activity patterns observed
- Document rationale for frequency changes

## Change Logging

All detected regulatory changes SHALL be systematically logged in a Regulatory Change Register for tracking and assessment.

### Regulatory Change Register

**Purpose**: Centralized log of all detected regulatory changes affecting or potentially affecting [Organization].

**Register Fields**:

- **Change ID**: Unique identifier
  - Format: CHG-[Year]-[Sequence]
  - Example: CHG-2025-001 (first change detected in 2025)

- **Regulation ID**: Link to entry in ISMS-POL-00
  - Cross-reference to ensure consistency
  - Enables filtering/reporting by regulation

- **Regulation Name**: Full regulation name for human readability

- **Type of Change**: Categorization (see Section 2.3.2)
  - New Regulation, Amendment, Repeal, Guidance, Enforcement Action

- **Change Description**: Brief summary of change
  - 2-3 sentences summarizing what changed
  - Example: "Article 32 amended to require post-quantum cryptography within 2 years of effective date"

- **Effective Date**: When change becomes legally binding
  - Critical for implementation planning
  - May differ from publication date
  - Example: "January 17, 2025"

- **Transition Period**: Time allowed for compliance
  - Some regulations provide transition/grace period
  - Calculate deadline: Effective Date + Transition Period
  - Example: "24 months from effective date (deadline: January 17, 2027)"

- **Source**: Where change was detected
  - URL, citation, legal database reference
  - Enables verification and detailed review
  - Example: "EUR-Lex CELEX:32024R9999, detected via GDPR alert on LexisNexis"

- **Detected By / Date**: Who detected change and when
  - Accountability and traceability
  - Example: "Compliance Analyst / 2025-01-15"

- **Status**: Tracking through lifecycle
  - **Detected**: Change logged, not yet assessed
  - **Under Assessment**: Impact assessment in progress (per Section 3)
  - **Implemented**: Framework updated, gaps remediated, change integrated
  - **Closed**: Change fully integrated, no further action needed
  - **Not Applicable**: Assessed as not affecting [Organization]

- **Impact Assessment ID** (if applicable): Link to impact assessment document
  - Cross-reference to detailed assessment (Section 3)
  - Empty if assessment determines "Not Applicable"

- **Notes**: Additional context
  - Free text for important details
  - Links to related changes
  - Regulatory guidance or FAQs

### Change Types

**New Regulation**:

- Entirely new law or regulation enacted
- Creates new compliance obligations
- Example: New data localization law enacted requiring data to be stored in-country
- Impact: Triggers full applicability assessment per 5.31.2 methodology

**Amendment**:

- Changes to existing regulation
- Most common type of change
- Subcategories:
  - **New requirements added**: Regulation expanded (new articles, new obligations)
  - **Existing requirements modified**: Changes to scope, specificity, timelines, thresholds
  - **Requirements removed**: Obligations eliminated (rare but possible)
  - **Technical corrections**: Typos, cross-reference fixes (usually no compliance impact)
- Impact: Requires requirement extraction review per 5.31.3 methodology

**Repeal**:

- Regulation retired or superseded by new regulation
- Compliance obligations end (as of effective date)
- Example: Old data protection law repealed when new data protection law takes effect
- Impact: Archive requirements and mappings; retain records per retention policy (Section 7)

**Guidance**:

- Official interpretation, FAQ, or implementation guidance published by regulatory authority
- Not law itself but authoritative interpretation
- Examples: Regulatory authority publishes guidance on applying regulation to cloud services
- Impact: May clarify ambiguous requirements, inform requirement interpretation updates

**Enforcement Action**:

- Regulatory action against another organization
- Reveals regulatory interpretation and enforcement priorities
- Examples: Regulator fines company for specific practice, clarifying what regulator considers non-compliant
- Impact: Informational (understand enforcement priorities); may inform risk assessment

### Change Log Maintenance

**Updating the Register**:

- Changes logged within 2 business days of detection
- Compliance Analyst or designated monitor logs changes
- Initial status: "Detected"

**Status Progression**:

- Detected → Under Assessment (when impact assessment begins per Section 3)
- Under Assessment → Implemented (when framework updates complete)
- Implemented → Closed (when verification complete, ongoing operation integrated)
- OR: Detected → Not Applicable (if assessment determines no impact on [Organization])

**Historical Record**:

- NEVER delete entries from Regulatory Change Register
- All changes retained indefinitely
- Provides audit trail of regulatory landscape evolution
- Demonstrates proactive monitoring and diligence

**Integration with Compliance Dashboard**:

- Change Register feeds Regulatory Compliance Dashboard (Assessment Workbook 6)
- Metrics: Changes detected this period, changes under assessment, changes pending implementation
- Executive visibility into regulatory landscape volatility

**Quarterly Review**:

- Compliance Officer reviews Change Register quarterly
- Identify changes stuck in "Under Assessment" (escalate or close)
- Identify changes with approaching effective dates (prioritize)
- Report to management on regulatory change trends

---

# Impact Assessment Process

Impact assessment is the systematic evaluation of how a detected regulatory change affects [Organization]'s compliance obligations and control framework.

## Assessment Triggers

Not every detected regulatory change requires full impact assessment. Clear triggers determine when assessment is needed.

### Automatic Triggers

**ANY Change to Tier 1 Regulation**:

- Tier 1 = Mandatory Compliance (from ISMS-POL-00)
- Assumption: Changes to mandatory regulations ALWAYS require assessment
- Rationale: Legal obligation to comply; cannot risk missing relevant changes
- Action: Trigger impact assessment immediately upon detection

**Change to Tier 2 Regulation with Potential Impact**:

- Tier 2 = Conditional Applicability
- If change affects condition triggering applicability, assess
- Example: PCI DSS v4.0.1 is Tier 2 (applies only if processing cards); if PCI DSS v4.0.1 changes and [Organization] is considering accepting cards, assess impact
- Action: Compliance Officer evaluates whether Tier 2 change is relevant given business context

**New Regulation in [Organization] Jurisdiction**:

- Any new regulation enacted in jurisdiction where [Organization] operates or has customers
- Unknown applicability until assessed
- Action: Trigger applicability assessment per 5.31.2 methodology to determine if regulation is Tier 1, 2, or 3

### Threshold Triggers

**Material Change** (Not Minor/Technical):

- Exclude purely technical corrections (typos, formatting, cross-reference fixes)
- Include substantive changes (new requirements, modified scope, changed timelines)
- Judgment call by Compliance Analyst; when in doubt, assess

**Change Affecting ISO 27001 Scope**:

- If regulatory change affects controls within ISO 27001 certification scope
- Example: Regulation now requires specific control that [Organization] previously excluded from scope
- Action: Assess impact on certification and Statement of Applicability

**Change with Compliance Deadline**:

- If regulatory change includes specific implementation deadline
- Deadline creates urgency regardless of content
- Action: Assess feasibility of meeting deadline, resource requirements

## Impact Assessment Steps

[Organization] SHALL follow a six-step impact assessment process for each triggered regulatory change.

### Step 1: Applicability Check

**Question**: Does this regulatory change affect [Organization]?

**Process**:

- Review change against 5.31.2 applicability criteria:
  - **Geographic**: Does change affect jurisdictions where [Organization] operates or has customers?
  - **Operational**: Does change affect services [Organization] provides or data [Organization] processes?
  - **Contractual**: Does change affect contractual obligations [Organization] has?
  
- **Possible Outcomes**:

  1. **Affects [Organization]**: Change applies; proceed to Step 2
  2. **Does Not Affect [Organization]**: Change does not apply (e.g., regulation specific to industry [Organization] is not in)
  3. **Uncertain**: Unclear whether change applies; obtain legal counsel interpretation

**Documentation**:

- Document applicability determination in Impact Assessment Template (Section 3.3)
- If "Does Not Affect", update Regulatory Change Register status to "Not Applicable - Closed"
- If "Uncertain", engage legal counsel before proceeding

**Example**:

- Change: New healthcare data regulation enacted in Country X
- [Organization] Assessment: [Organization] does not operate in Country X, does not have customers in Country X, does not process healthcare data
- Outcome: Does Not Affect [Organization]
- Action: Log as "Not Applicable" and close

### Step 2: Requirement Extraction (If Applicable)

**Condition**: Only if Step 1 determined "Affects [Organization]"

**Process**:

- Apply 5.31.3 requirements extraction methodology to new or modified regulatory text
- Identify:
  - **NEW requirements** introduced by change (extract per 5.31.3 Section 2)
  - **MODIFIED requirements** (compare old vs. new regulatory text; update interpreted requirement in Requirements Register)
  - **REMOVED requirements** (if regulatory change deletes obligations)
  
- **Actions**:
  - Add new requirements to Requirements Register with new Requirement IDs
  - Update existing requirements in Requirements Register if regulatory text changed
  - Archive removed requirements (mark as "Repealed - [Date]" in Requirements Register)

**Traceability**:

- Link new/modified requirements to Regulatory Change ID
- Document in Requirements Register Notes field: "Created/Modified by CHG-2025-XXX"
- Maintains audit trail from regulatory change through to requirements

**Example**:

- Change: Data Protection Regulation Article 32 amended to add "implement post-quantum cryptography within 24 months"
- Existing Requirement: REG-DP01-32-001 "Implement encryption for personal data at rest and in transit"
- Modified Requirement: REG-DP01-32-001 updated Interpreted Requirement to "Implement encryption (transitioning to post-quantum cryptography by [deadline]) for personal data at rest and in transit"
- OR: New Requirement: REG-DP01-32-005 "Transition to post-quantum cryptographic algorithms for personal data encryption within 24 months of amendment effective date"

### Step 3: Control Impact Analysis

**Question**: Which existing controls are affected by new/modified requirements?

**Process**:

- Review Control Mapping Matrix (from 5.31.3)
- For each new/modified requirement from Step 2:
  - Identify controls currently mapped (if modifying existing requirement)
  - Assess whether existing controls still satisfy modified requirement
  - Identify controls that may need enhancement
  - Identify controls that may become obsolete (if requirement removed)

**Possible Outcomes**:

- **Existing controls sufficient**: No control changes needed (best case)
- **Existing controls need enhancement**: Controls exist but must be upgraded
- **New controls needed**: No existing control satisfies new requirement (creates gap)
- **Controls can be retired**: Requirement removed, control no longer needed (if control served only that requirement)

**Documentation**:

- List affected controls in Impact Assessment Template
- Note type of impact: Enhancement Needed, New Control Needed, Retirement Candidate

**Example**:

- Modified Requirement: REG-DP01-32-001 now requires post-quantum cryptography
- Existing Control: A.8.24 Use of Cryptography (currently implements classical cryptography - AES, RSA)
- Impact Analysis: A.8.24 requires enhancement (migrate to post-quantum algorithms)
- Other Affected Controls: A.8.11 Data masking (if masked data encrypted, also needs post-quantum migration)

### Step 4: Gap Analysis

**Question**: Do new or modified requirements create gaps in compliance?

**Process**:

- Apply 5.31.3 gap analysis methodology (Section 4) to new/modified requirements
- Identify:
  - **Complete gaps**: New requirement with no control mapping (no existing control satisfies it)
  - **Partial gaps**: Existing control partially satisfies modified requirement but enhancement needed
  - **Implementation gaps**: Control exists and is mapped but not fully implemented

**Gap Documentation**:

- Add gaps to Gap Register (from 5.31.3 Section 4.4)
- Link gaps to Regulatory Change ID (traceability)
- Prioritize gaps per 5.31.3 Section 4.2 prioritization framework
  - Consider regulatory tier, legal consequence, compliance deadline

**Example**:

- New Requirement: REG-DP01-33-006 "Conduct automated testing of breach detection capabilities quarterly"
- Control Mapping Review: No existing Annex A control specifically addresses automated breach detection testing
- Gap Identified: GAP-2025-015 - Complete gap for quarterly automated breach detection testing
- Priority: HIGH (Tier 1 regulation, specific deadline, testable requirement)

### Step 5: Implementation Effort Assessment

**Question**: What resources are required to implement changes needed to comply?

**Process**:
Estimate resources across multiple dimensions:

**People**:

- Which teams involved? (IT, Security, Compliance, Legal, Business Units)
- How many person-hours/days required?
- Internal resources sufficient or external consultants/vendors needed?
- Availability of required expertise?

**Time**:

- Implementation timeline estimate (realistic)
- Dependencies on other projects/initiatives
- Parallel vs. sequential activities
- Buffer for testing, validation, approval

**Budget**:

- Technology costs (new systems, software licenses, hardware)
- Consulting/professional services costs
- Training costs
- Opportunity cost (resources diverted from other priorities)

**Systems**:

- Which systems require changes? (applications, infrastructure, cloud services)
- Scope of changes (configuration vs. code changes vs. replacement)
- Testing requirements (dev, staging, production)
- Downtime or maintenance windows needed?

**Policies/Procedures**:

- Which documents need updates?
- Who must approve changes?
- Training and communication needed for new/updated procedures?

**Training**:

- Who needs training? (all employees, specific roles, control owners)
- Training content development effort
- Delivery method (online, in-person, documentation)
- Verification (testing, attestation)

**Timeline Estimate Format**:

- Optimistic / Realistic / Pessimistic timeline
- Example: "3 months (optimistic) / 6 months (realistic) / 9 months (pessimistic)"
- Account for unknowns, dependencies, resource contention

**Documentation**:

- Detailed breakdown in Impact Assessment Template
- Executive summary: "X person-months, $Y budget, Z months timeline"

**Example**:

- Gap: Need to implement post-quantum cryptography
- People: Crypto team (2 FTEs), IT Ops (1 FTE), Vendor engagement (external)
- Time: 12-18 months (algorithm selection, vendor evaluation, pilot, staged rollout, testing, migration)
- Budget: $500K (new key management system, consulting, testing)
- Systems: All systems encrypting personal data (databases, backup systems, application-level encryption)
- Policies: Update Encryption Policy, Key Management Procedures
- Training: Security team training on post-quantum algorithms, Operations training on new KMS

### Step 6: Risk Assessment (If Not Implemented)

**Question**: What is the risk if [Organization] does NOT comply with this regulatory change?

**Process**:
Assess risk across multiple factors:

**Legal Penalties**:

- What are statutory penalties for non-compliance?
- Examples: Fines, criminal liability, regulatory sanctions
- Review regulation text for penalty provisions
- Research enforcement history (has regulator fined others for similar non-compliance?)
- Magnitude: Minor (warnings, small fines) vs. Major (% of revenue, criminal prosecution)

**Contractual Consequences**:

- If regulation flows from customer contract, what are contract breach consequences?
- Examples: Contract termination, financial penalties, loss of business
- Review contract terms for remedies and termination rights

**Reputational Risk**:

- Public disclosure of non-compliance (regulatory enforcement actions often public)
- Customer trust impact
- Competitive disadvantage (competitors compliant, [Organization] not)
- Media coverage risk

**Business Impact**:

- Loss of ability to operate (e.g., data localization requirement not met → cannot serve customers in that jurisdiction)
- Loss of certification (e.g., non-compliance affects ISO 27001 certification)
- Litigation risk (class action lawsuits for data breaches tied to non-compliance)

**Likelihood of Enforcement**:

- How active is regulator in enforcement?
- Recent enforcement trends (increasing or decreasing)
- Regulatory priorities (is this a focus area?)
- [Organization]'s profile (high-profile vs. under-the-radar)

**Risk Rating**:

- Combine likelihood and impact:
  - **High Risk**: High likelihood of enforcement AND severe consequences
  - **Medium Risk**: Moderate likelihood OR moderate consequences
  - **Low Risk**: Low likelihood AND minor consequences

**Documentation**:

- Document risk assessment in Impact Assessment Template
- Include rationale (why this risk rating)
- Cite sources (enforcement actions, regulatory guidance, legal counsel opinion)

**Example**:

- Regulatory Change: Breach notification deadline changed from 72 hours to 24 hours
- Legal Penalty: Fines up to €10M or 2% of revenue for late notification (GDPR)
- Contractual: Customer contracts incorporate regulatory breach notification requirements
- Reputational: Public disclosure of breach AND late notification compounds reputation damage
- Business: Potential loss of customer trust, competitive disadvantage
- Likelihood: HIGH (regulator actively enforces breach notification timelines, recent enforcement actions in sector)
- **Risk Rating: HIGH**

## Assessment Documentation

All impact assessments SHALL be documented in a standardized Impact Assessment Template for consistency, completeness, and auditability.

### Impact Assessment Template

**Template Structure**:

**Header**:

- Impact Assessment ID: IA-[Year]-[Sequence] (e.g., IA-2025-001)
- Regulatory Change ID: CHG-YYYY-XXX (link to Change Register)
- Regulation Name: [Full regulation name]
- Change Description: [Brief summary from Change Register]
- Assessment Date: [Date]
- Assessor: [Name/Role]

**Section 1: Applicability Determination** (Step 1):

- Does this change affect [Organization]? ☐ Yes  ☐ No  ☐ Uncertain
- Geographic Scope: [Analysis]
- Operational Scope: [Analysis]
- Contractual Scope: [Analysis]
- Applicability Rationale: [Detailed explanation]
- If "Uncertain": Legal counsel consulted? ☐ Yes  ☐ No  Legal opinion attached: ☐ Yes  ☐ No

**Section 2: Requirements Impact** (Step 2):

- New Requirements Identified:
  - List of new Requirement IDs created in Requirements Register
- Modified Requirements:
  - List of Requirement IDs updated in Requirements Register
  - Summary of changes to each
- Removed Requirements:
  - List of Requirement IDs archived
- Requirements Register Updated: ☐ Yes  ☐ N/A

**Section 3: Control Impact** (Step 3):

- Affected Controls:

  | Control ID | Control Name | Impact Type | Notes |
  |------------|--------------|-------------|-------|
  | A.X.Y | [Name] | Enhancement Needed / New Control / Retirement | [Details] |

- Control Mapping Matrix Review Complete: ☐ Yes  ☐ N/A

**Section 4: Gap Analysis** (Step 4):

- New Gaps Identified:

  | Gap ID | Requirement ID | Gap Type | Priority | Notes |
  |--------|---------------|----------|----------|-------|
  | GAP-YYYY-XXX | REG-XX-XX-XXX | Complete / Partial / Implementation | H/M/L | [Details] |

- Gap Register Updated: ☐ Yes  ☐ No Gaps

**Section 5: Implementation Effort** (Step 5):

- People: [FTEs, roles, availability]
- Time: Optimistic: [X months] / Realistic: [Y months] / Pessimistic: [Z months]
- Budget: $[Amount] (breakdown: [Technology $X, Consulting $Y, Training $Z, Other $W])
- Systems Affected: [List]
- Policies/Procedures to Update: [List]
- Training Required: [Scope and audience]
- Dependencies: [Other projects, vendor deliveries, etc.]

**Section 6: Risk Assessment** (Step 6):

- Legal Penalties: [Description and magnitude]
- Contractual Consequences: [Description]
- Reputational Risk: [Description]
- Business Impact: [Description]
- Likelihood of Enforcement: ☐ High  ☐ Medium  ☐ Low (rationale: [Text])
- **Overall Risk Rating**: ☐ High  ☐ Medium  ☐ Low
- Risk Rationale: [Detailed explanation]

**Section 7: Recommended Action**:

- ☐ Implement (close gaps, update controls, comply fully)
- ☐ Defer (delay implementation; state timeline and rationale)
- ☐ Accept Risk (do not implement; document risk acceptance)
- ☐ No Action Required (change does not affect [Organization])
- Recommendation Rationale: [Detailed explanation]
- If Defer: Revisit Date: [Date]
- If Accept Risk: Requires Executive Approval: ☐ Yes (obtained) ☐ Pending

**Attachments**:

- Legal counsel opinion (if obtained)
- Detailed resource plan (if Implement recommended)
- Risk acceptance documentation (if Accept Risk recommended)
- Supporting regulatory text, guidance, or analysis

### Decision Record

Impact Assessment provides recommendation. Decision Record documents management decision.

**Decision Record Fields**:

- Impact Assessment ID: [Reference]
- Decision Date: [Date]
- Decision Maker: [Name/Role] (typically ISMS Manager, Compliance Officer, or Executive Management)
- Decision: ☐ Approved as Recommended  ☐ Modified (specify)  ☐ Rejected (specify alternative)
- Modified/Alternative Action: [If decision differs from recommendation]
- Decision Rationale: [Why this decision was made]
- If Deferred:
  - Defer Until: [Date]
  - Revisit Trigger: [Condition or date]
  - Interim Risk Mitigation: [Any temporary measures]
- If Risk Accepted:
  - Executive Approval Signature: [Name/Date]
  - Risk Acceptance Duration: [Until when risk acceptance valid]
  - Risk Review Date: [When to reassess]
- If Implemented:
  - Implementation Owner: [Name/Role]
  - Implementation Deadline: [Date]
  - Implementation Plan Reference: [Link to detailed plan]

**Storage**:

- Decision Record attached to Impact Assessment Template
- Both stored in centralized compliance repository
- Linked from Regulatory Change Register (Impact Assessment ID field)

## Escalation Criteria

Certain regulatory changes require executive management involvement due to significance, risk, or resource requirements.

### Escalation Triggers

**Significant New Compliance Obligation**:

- Regulatory change creates major new compliance requirement
- Examples:
  - New regulation requiring significant operational changes (data localization, mandatory breach notification infrastructure)
  - Amendment expanding scope dramatically (applies to more data, more systems, more jurisdictions)
- Criterion: Fundamental change to compliance posture

**High Risk if Not Implemented**:

- Step 6 risk assessment yields "High Risk" rating
- Potential for severe legal penalties, business disruption, or reputational damage
- Executive decision required: Accept this risk or allocate resources to mitigate?

**Major Control Changes Required**:

- Organization-wide control implementation needed
- Examples:
  - All systems must implement new encryption standard
  - All employees must receive training on new data handling requirements
- Impacts multiple business units, requires coordination
- Criterion: Scope beyond single team or control owner

**Significant Budget/Resource Requirements**:

- Implementation effort assessment (Step 5) exceeds delegated authority thresholds
- Example thresholds:
  - Budget >$100K: Escalate to Executive Management
  - Person-months >10 FTEs: Escalate to Executive Management
  - Timeline >12 months: Escalate to Executive Management
- Requires budget approval and resource allocation decisions

**Short Implementation Deadline (Urgent)**:

- Regulatory change effective date is near-term (e.g., <6 months)
- Insufficient time for normal implementation planning and execution
- May require emergency measures, expedited procurement, temporary workarounds
- Executive decision needed on priorities and trade-offs

**Legal Uncertainty**:

- Interpretation of regulatory change is unclear
- Legal counsel unable to provide definitive guidance (law is ambiguous, no enforcement precedent)
- Different interpretations have significantly different implementation implications
- Executive decision required on interpretation approach (conservative vs. liberal) and risk tolerance

### Escalation Process

**Step 1: Prepare Executive Briefing**

- Concise summary (1-2 pages maximum)
- Content:
  - **What Changed**: Summary of regulatory change
  - **Why It Matters**: Impact on [Organization] (requirements, controls, operations)
  - **Options**: Typically 2-3 options (e.g., Full Compliance, Partial Compliance with Risk Acceptance, Defer)
  - **Recommendation**: Preferred option with rationale
  - **Decision Needed**: Specific decision requested from executive
  - **Timeline**: When decision needed
- Attach full Impact Assessment Template as appendix

**Step 2: Present to Executive Management**

- Compliance Officer and/or ISMS Manager present briefing
- Legal Counsel attends (if legal uncertainty or high risk)
- Q&A session
- Discussion of options, trade-offs, risk tolerance

**Step 3: Obtain Executive Decision**

- Executive provides decision
- Document decision in Decision Record (Section 3.3.2)
- If risk acceptance, obtain executive signature on risk acceptance documentation

**Step 4: Communicate Decision**

- Communicate decision to affected stakeholders (control owners, implementation teams, business units)
- Provide context and rationale
- Clarify roles, responsibilities, and timelines

**Step 5: Track Implementation**

- If decision is to implement, track via project/program management
- Regular status updates to executive management
- Escalate again if challenges arise (timeline slippage, cost overruns, unforeseen dependencies)

### Escalation Examples

**Example 1: Data Localization Requirement**

- **Change**: New regulation requires personal data of Country X citizens to be stored exclusively in Country X
- **Impact**: [Organization] currently uses global cloud provider with data centers outside Country X; would require new cloud region or data center in Country X
- **Risk**: High (cannot serve Country X customers if non-compliant)
- **Effort**: $2M budget, 18-month implementation (new data center, data migration)
- **Escalation Trigger**: Significant budget/resource + high risk + major control change
- **Decision Needed**: Proceed with Country X data center OR exit Country X market
- **Outcome**: Executive approves $2M for data center; strategic decision to maintain Country X presence

**Example 2: Breach Notification Timeline Change**

- **Change**: Breach notification deadline reduced from 72 hours to 24 hours
- **Impact**: Current incident response procedures assume 72-hour timeline; need faster detection, assessment, decision-making, and notification
- **Risk**: High (regulator actively enforces notification deadlines; severe fines for late notification)
- **Effort**: $150K (automated detection tools, revised procedures, training), 4 months implementation
- **Escalation Trigger**: High risk + tight timeline
- **Decision Needed**: Approve budget and prioritize implementation OR accept risk of non-compliance
- **Outcome**: Executive approves budget; directs Security team to prioritize over other projects

**Example 3: Ambiguous Cryptography Requirement**

- **Change**: Regulation requires "quantum-resistant cryptography" but does not specify standards or timeline
- **Impact**: Uncertain; post-quantum cryptography standards still evolving (NIST standardization ongoing)
- **Risk**: Medium-High (if interpreted strictly, massive cryptography migration; if interpreted flexibly, may defer until standards mature)
- **Effort**: Depends on interpretation; could range from $0 (defer) to $1M+ (immediate migration)
- **Escalation Trigger**: Legal uncertainty + significant budget variation based on interpretation
- **Decision Needed**: Conservative interpretation (begin planning now) OR liberal interpretation (wait for regulatory guidance and mature standards)
- **Outcome**: Executive approves conservative approach (begin planning and pilot projects) while monitoring for regulatory guidance

---

# Control Mapping Updates

When regulatory changes result in new or modified requirements, or when controls are implemented/changed, the compliance framework documents must be updated to maintain accuracy and traceability.

## Update Triggers

### Regulatory Change with Impact

**Trigger**: Impact assessment (Section 3) concludes regulatory change affects [Organization]

**Updates Needed**:

- **ISMS-POL-00** (if applicability changed):
  - New regulation added
  - Existing regulation tier changed (e.g., Tier 2 → Tier 1 because condition now met)
  - Regulation archived (if repealed)
  
- **Requirements Register** (per Step 2 of impact assessment):
  - New requirements added
  - Existing requirements modified
  - Obsolete requirements archived
  
- **Control Mapping Matrix** (per Step 3 of impact assessment):
  - New requirements mapped to controls
  - Modified requirements re-mapped (mappings may change)
  - Obsolete requirement mappings removed
  
- **Gap Register** (per Step 4 of impact assessment):
  - New gaps added
  - Existing gaps updated if priority/status changed
  - Gaps closed if regulatory change eliminates requirement creating gap

### New Control Implemented

**Trigger**: [Organization] implements new ISO 27001 Annex A control or creates new organization-specific control (per 5.31.3 Section 3.5)

**Updates Needed**:

- **Control Mapping Matrix**:
  - Add column for new control (if Annex A control not previously in scope)
  - Review ALL requirements in Requirements Register to identify mappings to new control
  - Populate mappings (P, S, Su) for relevant requirements
  
- **Gap Register**:
  - If new control closes gaps, update Gap Status to "Closed"
  - Document in gap closure notes: "Closed by implementation of Control X.Y.Z"
  
- **Evidence Register**:
  - Add evidence requirements for new control
  - Begin evidence collection

**Rationale**: New control may satisfy requirements previously identified as gaps or partially satisfied. Comprehensive mapping review ensures control is credited for all requirements it satisfies.

### Control Retired or Changed

**Trigger**: [Organization] retires control (no longer implemented) or significantly changes control scope/implementation

**Updates Needed**:

- **Control Mapping Matrix**:
  - If control retired: Review all requirements mapped to that control
    - Identify alternative controls satisfying those requirements
    - If no alternative, create gaps
    - Update mappings
  - If control changed:
    - Re-assess mapping type (may change: P → S if control weakened; S → P if control enhanced)
    - Update notes in matrix explaining change
  
- **Gap Register**:
  - If control retirement creates gaps, add new gaps
  - If control enhancement closes gaps, update Gap Status
  
- **Evidence Register**:
  - Archive evidence for retired control (per retention policy Section 7)
  - Update evidence requirements if control changed

**Caution**: Retiring or weakening controls may create compliance gaps. Use reverse traceability (5.31.3 Section 5.2) to identify all affected requirements before retiring controls.

### Gap Remediation Completed

**Trigger**: Implementation of new or enhanced control specifically to close compliance gap

**Updates Needed**:

- **Control Mapping Matrix**:
  - Add mapping between requirement (from gap) and new/enhanced control
  - Mapping type typically Primary (P) since control was implemented to satisfy requirement
  
- **Gap Register**:
  - Update Gap Status: "Closed"
  - Gap Closure Date: [Date]
  - Gap Closure Method: [New control / Enhanced control / Compensating control / Risk accepted]
  - Verification: [Who verified closure and when]
  
- **Evidence Register**:
  - Add evidence for new/enhanced control
  - Link evidence to requirement that gap addressed

**Verification Required**: Gap closure must be VERIFIED (not just claimed). Verification methods:

- Control Owner confirms control implemented and operational
- Evidence collected and reviewed
- Internal audit validates control effectiveness
- Testing demonstrates control satisfies requirement

## Update Process

### Step 1: Review Affected Documents

**Question**: Which compliance framework documents require updates based on trigger?

**Process**:

- Review trigger (regulatory change, new control, control change, gap remediation)
- Identify affected documents from list:
  - **ISMS-POL-00**: Regulatory register (if applicability changed)
  - **Requirements Register**: Requirement entries (if requirements added/modified/removed)
  - **Control Mapping Matrix**: Requirement-control mappings (if requirements or controls changed)
  - **Gap Register**: Gap entries (if gaps created or closed)
  - **Evidence Register**: Evidence requirements and collection (if controls changed)
  - **Organizational Controls Register**: Organization-specific controls (if custom control created)

**Output**: List of documents requiring updates with specific changes needed

### Step 2: Make Updates

**Process**:
For each document requiring update:

1. **Retrieve Current Version**:

   - Access centralized repository
   - Confirm working with latest version (avoid overwriting concurrent edits)

2. **Make Changes**:

   - Follow document-specific update procedures
   - Maintain data integrity (correct formats, valid values, complete fields)
   - Use change tracking if document format supports (e.g., Track Changes in Word, version control in Git)

3. **Document What Changed**:

   - Update "Last Updated" and "Updated By" fields (if present in document)
   - Add entry to document's change log or version history
   - Describe change: "Added Requirement REG-DP01-32-006 per CHG-2025-015"

4. **Increment Version**:

   - Apply versioning scheme (Section 4.3.1)
   - Update document version number
   - Update "Version History" table in document

5. **Quality Check**:

   - Review changes for accuracy
   - Verify all fields populated
   - Check for consistency with related documents
   - Verify traceability maintained (IDs link correctly)

**Tools**:

- Use Assessment Workbooks (standardized templates with data validation)
- Use version control systems (Git, SharePoint, document management system)
- Automate where possible (scripts to update dashboards from underlying registers)

### Step 3: Update Traceability

**Importance**: Traceability is foundation of audit readiness (per 5.31.3 Section 5). Updates must maintain complete traceability.

**Forward Traceability Check** (Regulation → Requirement → Control → Evidence):

- Start with regulation in ISMS-POL-00
- Verify all extracted requirements in Requirements Register link to that regulation (Regulation ID field)
- Verify all requirements mapped to controls in Control Mapping Matrix
- Verify all controls have evidence in Evidence Register
- **Result**: Can trace from regulation to evidence through requirements and controls

**Reverse Traceability Check** (Evidence → Control → Requirement → Regulation):

- Start with evidence in Evidence Register
- Verify evidence linked to control(s) (Control ID field)
- Verify control(s) mapped to requirement(s) in Control Mapping Matrix
- Verify requirement(s) linked to regulation(s) in Requirements Register
- **Result**: Can trace from evidence back to regulation that mandated it

**Change Traceability Update** (per 5.31.3 Section 5.3):

- Document in change logs WHY changes were made
- Link changes to triggering event:
  - Regulatory Change ID (if triggered by regulatory change)
  - Gap ID (if triggered by gap remediation)
  - Control change notification (if triggered by control change)
- Maintain audit trail showing evolution of framework over time

**Automated Traceability Checks** (if using compliance management software):

- Run validation reports checking:
  - Requirements without control mappings (gaps)
  - Controls without evidence (evidence gaps)
  - Orphaned records (requirements referencing non-existent regulations)
- Resolve validation errors before finalizing updates

### Step 4: Communicate Changes

**Who Needs to Know?**

- **Control Owners**: If their controls affected (new mappings, changed requirements, gap closures)
- **Compliance Team**: Awareness of framework changes
- **ISMS Manager**: Oversight of framework integrity
- **Legal Counsel**: Awareness of new regulatory requirements
- **Executive Management**: If material changes (significant new requirements, major gaps)
- **Auditors**: If changes affect certification scope or audit approach

**Communication Methods**:

- **Email Notification**: Brief summary of changes, links to updated documents
- **Compliance Dashboard Update**: Metrics reflect new state of framework
- **Team Meeting**: If changes are significant, brief relevant teams
- **Training**: If new requirements create new procedures, train affected personnel
- **Documentation**: Update README, change log, or user guide for framework documents

**Communication Content**:

- What changed (brief summary)
- Why it changed (regulatory change, gap remediation, control update)
- Who is affected (which teams, which controls)
- What actions are needed (if any)
- Where to find updated documents (links)
- Who to contact with questions

**Timing**:

- Communicate within 1 week of finalizing updates
- Urgent changes (e.g., approaching compliance deadline): Immediate communication

**Example Communication**:
```
Subject: Regulatory Compliance Framework Update - CHG-2025-015

Team,

The Regulatory Compliance Framework has been updated to reflect regulatory change CHG-2025-015 (Data Protection Regulation Article 32 amendment requiring post-quantum cryptography).

CHANGES:

- Added Requirement REG-DP01-32-006 to Requirements Register
- Mapped requirement to Control A.8.24 (Use of Cryptography) - Enhancement Needed
- Created GAP-2025-020 (High Priority) for post-quantum crypto migration
- Target remediation: Q4 2026

AFFECTED TEAMS:

- Security Engineering (Control Owner for A.8.24)
- IT Operations (encryption systems)
- Compliance Team (gap tracking)

NEXT STEPS:

- Security Engineering to develop post-quantum migration plan by [Date]
- Status updates in monthly compliance review meetings

UPDATED DOCUMENTS:

- Requirements Register v2.3
- Control Mapping Matrix v2.1  
- Gap Register v1.8

Questions? Contact Compliance Team at compliance@[organization].

[Signature]
Compliance Officer
```

## Version Control

### Versioning Scheme

**Format**: Major.Minor (e.g., 1.0, 1.1, 2.0)

**Major Version** (increment first number, reset second to 0):

- **Triggers**:
  - New regulation added to ISMS-POL-00 (significant expansion of regulatory scope)
  - Major control changes (organization-wide control implementation)
  - Structural changes to framework (new registers, new processes)
  - Multiple significant changes accumulated over time
- **Examples**:
  - v1.5 → v2.0 when new major regulation (e.g., AI Act) becomes applicable
  - v2.3 → v3.0 when framework restructured

**Minor Version** (increment second number):

- **Triggers**:
  - Individual requirement added/modified/removed
  - Individual control mapping added/changed
  - Gap created/closed
  - Clarifications or corrections
  - Evidence updates
- **Examples**:
  - v1.0 → v1.1 when adding 3 new requirements from regulatory amendment
  - v2.5 → v2.6 when closing 5 gaps through control enhancements

**Initial Version**: 1.0 (when framework document first approved and published)

**Application**:

- Each framework document (Requirements Register, Control Mapping Matrix, Gap Register, Evidence Register, ISMS-POL-00) versioned independently
- Policy documents (POL-5.31.1 through 5.31.4) versioned independently
- Implementation guides (IMP-5.31.1 through 5.31.5) versioned independently

### Version History

**Version History Table** (in each document):

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| 1.0 | 2025-01-15 | Compliance Officer | Initial release |

**Details in Change Log**:

- For complex changes, version history table provides summary only
- Detailed change log (separate section or separate document) provides:
  - Requirement ID, old value, new value, rationale
  - Gap ID, closure method, verification
  - Mapping changes, justification

**Previous Version Retention**:

- ALL previous versions retained (never delete)
- Storage: Archive folder or version control system (Git, SharePoint version history)
- Naming convention: Document-Name_v1.1.xlsx, Document-Name_v1.2.xlsx
- Purpose: Audit trail, historical reference, ability to revert if needed

### Approval for Changes

**Minor Changes** (incremental requirements, mappings, gap updates):

- **Approver**: ISMS Manager OR Compliance Officer
- **Process**: 
  - Compliance Analyst prepares updates
  - ISMS Manager/Compliance Officer reviews and approves
  - Approval documented in version history ("Approved by: ISMS Manager, 2025-03-10")
- **Timeline**: Approval within 1 week of update completion

**Major Changes** (new regulations, framework restructure, significant scope changes):

- **Approver**: Executive Management
- **Process**:
  - Compliance Officer prepares briefing (similar to escalation briefing Section 3.4.2)
  - Present to Executive Management (context, changes, implications, resource needs)
  - Obtain executive approval (documented decision)
  - Approval documented in version history and formal approval record
- **Timeline**: Varies; schedule executive review within 2 weeks if possible

**Emergency Changes** (urgent regulatory compliance deadline):

- **Process**:
  - Compliance Officer makes urgent updates
  - Document as "Emergency Change - Awaiting Retroactive Approval"
  - Brief Executive Management at earliest opportunity (within 1 week)
  - Obtain retroactive approval and document
  - If Executive does not approve retroactively, revert change and address through normal process
- **Rare**: Used only for genuine emergencies (imminent compliance deadline, critical regulatory change)

**Approval Documentation**:

- Email approval from approver (retained in compliance repository)
- Approval recorded in version history table
- For Executive approvals: Formal approval document or meeting minutes

---

# Evidence Management Framework

Evidence is the tangible proof that [Organization] complies with regulatory requirements through implemented controls. Systematic evidence management is essential for audit readiness and regulatory inquiries.

## Evidence Requirements Per Regulation Type

Different types of regulations demand different forms of evidence.

### Legal/Statutory Regulations

**Evidence Types**:

- **Policy Documents**:
  - Approved policies addressing regulatory requirements
  - Executive approval signatures
  - Distribution records (who received policy, when)
  - Acknowledgment of receipt (if required)

- **Implementation Records**:
  - System configurations (screenshots, configuration files, audit exports)
  - Technical settings (encryption enabled, access controls configured, logging active)
  - Deployment records (when implemented, by whom)

- **Operational Evidence**:
  - Logs demonstrating ongoing compliance (access logs, audit logs, security event logs)
  - Periodic execution records (quarterly reviews, annual testing, monthly reports)
  - Incident response records (if breach notification required)

- **Periodic Reports** (if regulation requires):
  - Compliance attestations
  - Risk assessment reports
  - Audit findings and remediation
  - Submitted to regulatory authority with proof of submission (certified mail receipt, electronic filing confirmation)

- **Audit Reports**:
  - Internal audit findings on regulatory compliance
  - External audit reports (if applicable)
  - Management responses to findings
  - Corrective action plans and completion evidence

**Example** (Data Protection Regulation):

- Policy: Data Protection Policy (approved by DPO and Executive)
- Implementation: DPIA for high-risk processing, processor agreements with vendors, encryption configurations
- Operational: Data subject request fulfillment logs, breach notification records (if applicable)
- Periodic: Annual compliance report to supervisory authority (if required)
- Audit: Internal audit of GDPR compliance (findings and remediation)

### Contractual Requirements

**Evidence Types**:

- **Attestations**:
  - Signed compliance statements provided to customer
  - Declarations of compliance with contract terms
  - Examples: "We attest that we comply with security requirements in Section 12 of the Service Agreement"

- **Audit Reports**:
  - SOC 2 Type II report (if contract requires)
  - ISO 27001 certificate (if contract requires)
  - Customer-conducted audit reports (if customer exercised audit rights)
  - Third-party assessment reports

- **Specific Evidence Per Contract Terms**:
  - Contracts may specify exact evidence required
  - Examples:
    - "Provide quarterly vulnerability scan reports"
    - "Provide annual penetration test executive summary"
    - "Provide evidence of background checks for personnel with access to customer data"
  - Collect and provide exact evidence contract specifies

- **Regular Reporting to Customer**:
  - Monthly security metrics dashboard (if contract requires)
  - Quarterly compliance status reports
  - Incident notifications (as specified in contract SLA)

**Example** (Customer Contract with Security Exhibit):

- Attestation: Annual signed compliance statement
- Audit Report: SOC 2 Type II report provided to customer
- Specific Evidence: Quarterly vulnerability scan summaries, evidence of employee background checks
- Regular Reporting: Monthly uptime and security metrics dashboard

### Certification Requirements

**Evidence Types**:

- **Evidence Package Per Certification Body Requirements**:
  - ISO 27001: Statement of Applicability (SoA), risk assessment and treatment plan, policies, procedures, records
  - SOC 2: System description, control descriptions, evidence of control operation, management assertions
  - PCI DSS v4.0.1: Attestation of Compliance (AOC), Self-Assessment Questionnaire (SAQ), vulnerability scan reports
  - Each certification standard specifies required evidence

- **Policies & Procedures**:
  - All documented policies addressing certification control requirements
  - Procedures implementing policies
  - Work instructions, templates, forms

- **Records**:
  - Evidence of policy/procedure execution
  - Training records, access reviews, incident logs, change management tickets
  - Sampling: Auditor selects sample period; must have records for that period

- **Testing & Validation Evidence**:
  - Penetration test reports
  - Vulnerability scan results
  - Business continuity test results
  - Security awareness training effectiveness testing

- **Surveillance Audit Evidence** (for ongoing certification):
  - Between certification audits (e.g., annual surveillance for ISO 27001), provide evidence of continued compliance
  - Similar evidence types as initial certification but focused on changes and improvements

**Example** (ISO 27001 Certification):

- Evidence Package: SoA mapping Annex A controls to requirements, ISMS policies (POL-5.31.1 through 5.31.4), risk register, control implementation evidence
- Policies: All ISMS policies approved and in force
- Procedures: Implementation guides (IMP-5.31.1 through 5.31.5), control-specific procedures
- Records: Access review logs (quarterly), training completion records (annual), incident response records, change management logs
- Testing: Annual penetration test report, quarterly vulnerability scans, business continuity test results

## Evidence Requirements Per Control Type

Different types of controls generate different evidence.

### Policy Controls

**Evidence**:

- **Policy Document**:
  - Approved version of policy
  - Approval signatures (electronic or physical)
  - Effective date

- **Distribution Record**:
  - Who received policy (all employees, specific roles)
  - When distributed (email timestamp, portal publication date)
  - Access log (if policy on portal, who accessed)

- **Acknowledgment** (if required):
  - Employee acknowledgment of receipt and understanding
  - Attestation (e.g., "I have read and agree to comply with this policy")

**Refresh**: 

- Annual or upon change
- Evidence refresh: When policy updated, collect new approval and distribution evidence

**Example** (A.5.1 Policies for Information Security):

- Evidence: Information Security Policy v3.0 (approved by CISO and Executive Management on 2025-01-15)
- Distribution: Email to all employees 2025-01-20, published on policy portal
- Acknowledgment: 98% of employees acknowledged within 30 days (tracking spreadsheet)

### Process Controls

**Evidence**:

- **Procedure Documents**:
  - Documented procedures, work instructions, process flows
  - Approval records

- **Execution Logs**:
  - Records of procedure execution
  - Examples:
    - Access request/approval workflow tickets
    - Change management tickets
    - Incident response case records
    - User provisioning/deprovisioning logs

- **Periodic Execution** (if process is periodic):
  - Quarterly access reviews: Quarterly review completion reports
  - Annual risk assessments: Risk assessment report dated annually

**Refresh**: 

- Ongoing as process executes
- Evidence accumulates over time (continuous logs, periodic reports)

**Example** (A.5.18 Access Rights):

- Evidence Procedure: Access Rights Provisioning Procedure v2.0
- Evidence Execution: Access request tickets in ticketing system (ServiceNow, Jira, etc.) showing request, approval, provisioning, verification
- Evidence Periodic: Quarterly access rights review reports (reviewed by Control Owner, approved by ISMS Manager)

### Technical Controls

**Evidence**:

- **Configuration Files**:
  - System configuration exports
  - Firewall rules, access control lists, encryption settings
  - Screenshots of configuration screens (dated and annotated)

- **System Settings**:
  - Active Directory group policy objects (GPOs)
  - Cloud security posture (AWS Config, Azure Policy, GCP Security Command Center)
  - Network device configurations

- **Scan Reports**:
  - Vulnerability scan reports (Nessus, Qualys, Rapid7, etc.)
  - Compliance scans (CIS Benchmark scans, STIG compliance)
  - Dated and containing scan scope and results

**Refresh**:

- **Point-in-Time**: Configuration snapshots (collected for audits, quarterly, annually)
- **Ongoing Monitoring**: Continuous compliance monitoring tools provide ongoing evidence

**Example** (A.8.24 Use of Cryptography):

- Evidence Configuration: Encryption configuration for database (TDE enabled, AES-256, key rotation quarterly) - screenshot dated 2025-01-15
- Evidence Settings: TLS configuration for web services (TLS 1.3 enforced, cipher suites restricted) - configuration file export
- Evidence Scan: SSL Labs scan report for public-facing services (A+ rating, no weak ciphers) - dated 2025-01-10

### Testing Controls

**Evidence**:

- **Test Plans**:
  - Document describing test scope, methodology, schedule, participants
  - Approved test plan before execution

- **Test Results**:
  - Detailed test execution results
  - Pass/fail status for each test case
  - Issues identified during testing

- **Penetration Test Reports**:
  - Executive summary and detailed findings from penetration testers
  - Vulnerability severity ratings
  - Remediation recommendations
  - Dated and signed by testing firm

- **Validation Records**:
  - Business continuity test: Test scenario, participants, outcomes, lessons learned
  - Disaster recovery test: Restore time objective (RTO) achieved, data loss verified within recovery point objective (RPO)

**Refresh**:

- Periodic based on control requirement
  - Annual penetration testing: Evidence collected annually
  - Quarterly vulnerability scanning: Evidence collected quarterly
  - Semi-annual disaster recovery testing: Evidence collected semi-annually

**Example** (A.8.8 Management of Technical Vulnerabilities):

- Evidence Test Plan: Q1 2025 Vulnerability Assessment Plan (scope: all production systems, methodology: automated scanning + manual validation)
- Evidence Test Results: Nessus scan report dated 2025-01-15 (127 systems scanned, 5 high-severity findings, 23 medium, 89 low)
- Evidence Validation: Remediation validation scan dated 2025-02-01 (all high and medium vulnerabilities remediated and verified)

### Training Controls

**Evidence**:

- **Training Materials**:
  - Course content, slide decks, videos, e-learning modules
  - Version-controlled training materials (ensure using current version)

- **Completion Records**:
  - Training attendance sheets (for in-person training)
  - Learning management system (LMS) completion reports (for e-learning)
  - Certificates of completion

- **Test Scores** (if training includes assessment):
  - Quiz results, exam scores
  - Passing threshold (e.g., 80%)
  - Remediation for failures (retake training)

- **Attestations**:
  - Employee attestations of understanding
  - Acknowledgment of information security responsibilities

**Refresh**:

- Ongoing as training occurs
- Annual refresh: If training is annual, collect evidence annually
- New hire training: Collect evidence for each new hire cohort

**Example** (A.6.3 Information Security Awareness, Education and Training):

- Evidence Materials: Information Security Awareness Training 2025 (e-learning module, 45 minutes, covers phishing, passwords, data handling, incident reporting)
- Evidence Completion: LMS report showing 452 of 460 employees completed training (98% completion rate) as of 2025-02-15
- Evidence Scores: Average quiz score 94%, all employees scored >80% (passing threshold)

## Evidence Storage & Retrieval

### Centralized Evidence Repository

**Requirement**: All compliance evidence SHALL be stored in a centralized, organized, access-controlled repository.

**Repository Types**:

- **Document Management System**: SharePoint, Google Drive, Box, OneDrive
- **Compliance Management Platform**: Specialized software (Vanta, Drata, Secureframe, AuditBoard)
- **File Shares**: Network drives (if properly secured and backed up)
- **Hybrid**: Combination (policies in DMS, logs in SIEM, configurations in infrastructure-as-code repository)

**Key Requirements**:

- **Single Source of Truth**: All stakeholders access same repository (no shadow evidence in personal drives)
- **Searchable**: Metadata, naming conventions, folder structure enable quick retrieval
- **Backed Up**: Evidence repository is backed up per organizational backup policy
- **Versioned**: Previous versions of evidence retained (version control)
- **Indexed**: Compliance evidence catalog or index maintained for quick navigation

### Folder Structure

**Recommended Structure Option 1: By Regulation**
```
/Evidence_Repository/
  /REG-DP01_Data_Protection_Regulation/
    /Policies/

      - Data_Protection_Policy_v2.1.pdf
      - Data_Processing_Agreement_Template_v1.0.docx

    /Procedures/

      - DPIA_Procedure_v1.5.pdf
      - Data_Subject_Request_Workflow_v1.2.pdf

    /Technical_Configurations/

      - Encryption_Configuration_Database_2025-01-15.pdf
      - TLS_Configuration_Web_Services_2025-01-15.json

    /Logs/

      - Data_Subject_Requests_Log_Q1_2025.xlsx
      - Breach_Notification_Log_2024.xlsx

    /Audit_Reports/

      - Internal_Audit_GDPR_Compliance_2024.pdf
      - DPO_Annual_Report_2024.pdf

  /REG-FIN05_Financial_Regulation/
    /...
  /REG-ISO27001_Certification/
    /...
```

**Recommended Structure Option 2: By Control**
```
/Evidence_Repository/
  /ISO_27001_Controls/
    /A.5.1_Policies/

      - Information_Security_Policy_v3.0.pdf (evidence for multiple regulations)

    /A.5.15_Access_Control/

      - Access_Control_Policy_v2.5.pdf
      - Access_Request_Logs_Q1_2025.xlsx
      - Quarterly_Access_Review_2025-Q1.pdf

    /A.8.24_Use_of_Cryptography/

      - Encryption_Policy_v2.1.pdf
      - Cryptographic_Key_Management_Procedure_v1.8.pdf
      - Encryption_Configuration_Evidence_2025-01-15.zip

    /...
```

**Hybrid Structure** (Recommended for Large Organizations):

- Top level: By regulation (facilitates audit preparation by regulation)
- Within each regulation: By control (organizes evidence by what control provides it)
- Cross-references: Evidence that satisfies multiple regulations stored once, referenced from multiple locations (shortcuts, links, or tags)

**Choosing Structure**:

- **By Regulation**: Better for organizations with distinct regulatory audits (GDPR audit, SOC 2 audit occur separately)
- **By Control**: Better for organizations with integrated ISMS approach (one control framework serves multiple regulations)
- **Hybrid**: Best for complex environments with multiple regulations and many controls

### Access Controls

**Role-Based Access Control (RBAC)**:

- **Read Access (View Evidence)**:
  - All ISMS stakeholders
  - Control Owners (for their controls)
  - Compliance Team
  - Internal Audit Team
  - Management
  - External Auditors (temporary, read-only, during audit period)

- **Write Access (Upload/Edit Evidence)**:
  - Control Owners (for their controls' evidence only)
  - Compliance Team (for all evidence)
  - Designated Evidence Custodians

- **Delete Access** (Restricted):
  - Compliance Officer only (and only per retention policy)
  - Secure deletion, not ad-hoc deletion

- **Administrative Access**:
  - ISMS Manager
  - IT Security Administrator (for repository infrastructure)

**Least Privilege Principle**:

- Grant minimum access necessary for role
- Example: Control Owner for A.8.24 can upload evidence for A.8.24, cannot access evidence for A.5.1 (unless also owner of A.5.1)

**Audit Trail of Access**:

- Evidence repository SHOULD log:
  - Who accessed what evidence
  - When accessed (date/time)
  - What action (view, upload, edit, download, delete)
- Purpose: Detect unauthorized access, support forensic investigations

**Auditor Access**:

- External auditors granted temporary read-only access during audit
- Access limited to audit period (e.g., 2-week audit window)
- Access provisioned by Compliance Officer with audit firm contact information
- Access revoked immediately after audit completion
- Separate "auditor" account or role (not shared credentials)

### Retrieval Procedures

**Search Capabilities**:

- Search by: Regulation ID, Control ID, Evidence Type, Date Range, Keyword
- Examples:
  - "Find all evidence for REG-DP01 from 2024"
  - "Find penetration test reports from last 2 years"
  - "Find evidence for A.8.24 (Use of Cryptography)"

**Quick Retrieval for Audit Requests**:

- Auditor requests specific evidence (e.g., "Provide evidence of quarterly access reviews for 2024")
- Compliance Team retrieves from repository using search/folder structure
- Typical retrieval time target: <1 hour for specific evidence request, <1 day for comprehensive evidence package

**Evidence Packages Pre-Assembled**:

- For frequent audits (ISO 27001 surveillance, SOC 2 annual), pre-assemble evidence packages
- Evidence Package = Folder containing all typical evidence for that audit
- Updated quarterly or semi-annually
- Reduces audit preparation time (package ready, just need to verify currency)

**Designated Evidence Custodian During Audits**:

- Appoint Evidence Custodian role during audit period
- Responsibilities:
  - Interface with auditors for evidence requests
  - Retrieve evidence from repository
  - Track evidence provided to auditors (avoid providing same evidence multiple times)
  - Answer questions about evidence format, vintage, scope
- Typically: Compliance Analyst or Compliance Officer

## Evidence Lifecycle Management

Evidence is not static; it has a lifecycle from creation through disposal.

### Creation & Initial Verification

**Creation**:

- Evidence created during control implementation and operation
- Examples:
  - Policy approved → Policy PDF is evidence
  - Access review completed → Access review report is evidence
  - Vulnerability scan executed → Scan report is evidence

**Initial Verification** (by Control Owner):

- Control Owner verifies evidence is:
  - **Authentic**: Evidence is genuine (not fabricated, from authoritative source)
  - **Complete**: Evidence contains all required information
  - **Current**: Evidence is from correct time period (not outdated)
  - **Accessible**: Evidence is stored in correct location with correct permissions

**Upload to Repository**:

- Control Owner uploads verified evidence to Evidence Repository
- Follows naming convention (see below)
- Populates metadata (tags, description, related controls/requirements)

**Naming Convention Example**:
Format: [Control-ID]\_[Evidence-Type]\_[Date]\_[Version].[ext]

- A.8.24_Encryption_Policy_2025-01-15_v2.1.pdf
- A.5.18_Access_Review_Report_Q1-2025_v1.0.xlsx
- A.8.8_Penetration_Test_Report_2024_Annual_v1.0.pdf

### Periodic Refresh (For Time-Sensitive Evidence)

**Time-Sensitive Evidence**:

- Evidence that expires or becomes stale
- Examples:
  - Audit reports (typically valid 12 months)
  - Certifications (expire per certification body rules - ISO 27001 certificate valid 3 years, SOC 2 Type II valid 12 months)
  - Vulnerability scans (require quarterly refresh per many regulations)
  - Penetration tests (annual refresh common)

**Refresh Schedule**:

- Control Owner maintains refresh calendar
- Alerts configured for approaching expiration
- Example:
  - SOC 2 Type II valid through 2025-06-30 → Alert on 2025-05-15 (45 days before expiration) to begin next audit
  - Quarterly vulnerability scans due → Alert on first day of quarter to schedule scan

**Re-Collection Process**:
1. Alert triggers (evidence expiring soon)
2. Control Owner initiates evidence collection activity (conduct new scan, request new audit, execute new test)
3. New evidence created and verified
4. New evidence uploaded to repository
5. Old evidence archived (not deleted, moved to "Historical_Evidence" folder per retention policy)
6. Evidence Register updated with new evidence details

**Avoiding Evidence Gaps**:

- Evidence gaps occur when time-sensitive evidence expires before refresh collected
- Gap = Auditor requests evidence, but current evidence not available
- Prevention: Proactive calendar management, early alerts (60-90 days before expiration), buffer time for evidence collection

### Verification & Validation

**Control Owner Verification** (Primary):

- Frequency: At evidence creation and annually for static evidence (policies)
- Verification Criteria:
  - **Authenticity**: Evidence is from legitimate source
  - **Completeness**: All required fields/sections populated
  - **Currency**: Evidence is current and not outdated
  - **Accessibility**: Evidence is retrievable and usable
- Documentation: Control Owner signs off on evidence verification (checklist, attestation)

**Compliance Function Spot-Checks** (Secondary):

- Frequency: Quarterly spot-checks (sample 10% of evidence)
- Purpose: Independent verification that Control Owners are performing verification properly
- Process:
  - Compliance Analyst selects random sample of evidence
  - Reviews evidence against criteria
  - Confirms evidence is appropriate and current
  - Escalates issues to Compliance Officer

**Internal Audit Validation** (Tertiary):

- Frequency: Annual internal audits of ISMS
- Scope: Internal Audit team validates evidence for sampled controls
- Process:
  - Internal Audit selects sample of controls
  - Requests evidence for those controls
  - Validates evidence quality and adequacy
  - Reports findings (adequate evidence vs. gaps)
  - Management addresses findings

**Verification Records**:

- Evidence Register (Assessment Workbook 5) includes verification fields:
  - Last Verified By: [Name/Role]
  - Last Verified Date: [Date]
  - Verification Outcome: Pass / Issues Identified
  - Issues: [Description if applicable]
  - Next Verification Date: [Scheduled]

### Retention

**Retention Periods**:

- Defined by regulation, contract, or organizational policy (see Section 7)
- Typical: 3-7 years after event or evidence creation
- Examples:
  - GDPR often requires 3-7 years
  - Financial regulations may require longer (7-10 years)
  - Contractual: Per contract terms (often contract duration + 3-5 years)

**Retention Management**:

- Evidence Repository includes "Retention Date" metadata field
- Automated reports of evidence approaching retention expiration
- Review before disposal (confirm no legal hold, no ongoing audit, retention period truly expired)

**Evidence for Superseded Regulations**:

- If regulation is repealed or [Organization] exits jurisdiction, evidence still retained
- Purpose: Demonstrate historical compliance (defend against retroactive inquiries, investigations, litigation)
- Retention: Typically 7 years after regulation ceased to apply

### Secure Disposal

**When to Dispose**:

- Retention period expired
- No legal hold in effect (Section 7.3)
- No ongoing audit or investigation
- Compliance Officer approval obtained

**Disposal Method**:

- **Electronic Evidence**:
  - Secure deletion (data sanitization, overwrite, cryptographic erasure if encrypted at rest)
  - Not just "recycle bin delete" – must be unrecoverable
  - Tools: DBAN, Eraser, shred utilities, or built-in secure erase features
  
- **Physical Evidence** (paper documents):
  - Shredding (cross-cut shredder minimum)
  - For sensitive evidence: Industrial shredding or incineration
  - Certificate of destruction for highly sensitive material

- **Cloud-Based Evidence**:
  - Delete from cloud storage
  - Verify deletion propagated (not just soft-delete with retention)
  - If using immutable storage (compliance mode), wait for retention period to expire

**Disposal Logging**:

- Evidence Disposal Log maintained
- Fields:
  - Evidence ID or Description
  - Disposal Date
  - Disposed By (name/role)
  - Disposal Method (secure deletion, shredding, etc.)
  - Approval (Compliance Officer signature)
  - Rationale (retention period expired, legal hold cleared)

**Audit of Disposal**:

- Internal Audit periodically reviews Disposal Log
- Confirms disposals were authorized and appropriate
- Verifies secure disposal methods used

## Evidence Gaps & Remediation

### Identifying Evidence Gaps

**Evidence Gap**: Requirement or control for which evidence is missing, expired, or inadequate.

**Gap Types**:

- **Missing Evidence**: Control is mapped to requirement, but no evidence exists
  - Example: A.8.8 mapped to vulnerability management requirement, but no vulnerability scan reports in repository
  
- **Expired Evidence**: Evidence exists but is outdated
  - Example: Penetration test report is from 2022, but annual testing required (2024 and 2025 reports missing)
  
- **Inadequate Evidence**: Evidence exists but does not fully demonstrate compliance
  - Example: Policy exists but no evidence of policy distribution or employee acknowledgment

**Detection Methods**:

- **Manual Review**: Compliance Team reviews Evidence Register against Control Mapping Matrix
  - For each requirement → control mapping, verify evidence exists
  
- **Automated Checks** (if using compliance management software):
  - Software flags controls without evidence links
  - Software flags evidence with expiration dates in past
  - Reports generated weekly or monthly
  
- **Audit Preparation Reviews**: Pre-audit evidence review identifies gaps before auditor does
  - Typically 4-6 weeks before audit, comprehensive evidence review
  
- **Internal Audits**: Internal auditors request evidence, gaps identified if evidence cannot be provided

### Evidence Gap Register

**Purpose**: Track all identified evidence gaps and remediation efforts.

**Register Fields**:

- **Gap ID**: EG-[Year]-[Sequence] (EG-2025-001)
- **Control ID**: Which control lacks evidence
- **Requirement ID(s)**: Which requirement(s) control is mapped to
- **Gap Type**: Missing / Expired / Inadequate
- **Gap Description**: What evidence is missing or inadequate
- **Identified Date**: When gap detected
- **Identified By**: Who detected gap (Compliance Analyst, Internal Auditor, etc.)
- **Priority**: Based on regulation tier and audit risk
  - **Critical**: Tier 1 regulation, audit imminent
  - **High**: Tier 1 regulation, audit not imminent
  - **Medium**: Tier 2 regulation or Tier 1 but compensating evidence exists
  - **Low**: Tier 3 or informational
- **Remediation Plan**: How gap will be closed
- **Responsible Party**: Control Owner (typically)
- **Target Closure Date**: When evidence will be collected
- **Status**: Open / In Progress / Closed
- **Actual Closure Date**: When gap actually closed
- **Verification**: How closure verified (evidence reviewed by Compliance Officer, Internal Audit validated)

### Remediation

**Remediation Actions**:

**Collect Missing Evidence**:

- Control Owner collects evidence that should exist
- Examples:
  - Conduct missing vulnerability scan
  - Document existing configuration (if implemented but not documented)
  - Retrieve logs from systems
  - Recreate documentation if original lost (but note that recreation may not be as strong as contemporaneous evidence)

**Refresh Expired Evidence**:

- Re-execute activity to create current evidence
- Examples:
  - Conduct new penetration test (if previous expired)
  - Run new vulnerability scan (if previous too old)
  - Obtain new certification (if certificate expired)

**Enhance Inadequate Evidence**:

- Supplement existing evidence with additional evidence
- Examples:
  - Policy exists but no distribution record → Add distribution email or portal publication evidence
  - Configuration exists but no explanation → Add narrative explaining what configuration demonstrates

**Prioritization**:

- Close **Critical** gaps immediately (within 1 week)
- Close **High** gaps within 1 month
- Close **Medium** gaps within 1 quarter
- Close **Low** gaps opportunistically (when resources available, before next audit)

**Pre-Audit Evidence Remediation**:

- 4-6 weeks before audit, conduct comprehensive evidence gap review
- Close all **Critical** and **High** gaps before audit begins
- Provide status of **Medium** gaps to auditor (in progress)
- **Low** gaps may remain open if resources insufficient (accept risk of potential audit finding)

**Verification of Closure**:

- Compliance Officer or Internal Audit verifies gap closure
- Reviews new/refreshed evidence
- Confirms evidence is adequate
- Updates Evidence Gap Register status to "Closed"

---

# Compliance Reporting

Compliance reporting provides visibility into regulatory compliance status for internal stakeholders and external parties.

## Internal Reporting

### Compliance Status Dashboard

**Purpose**: Real-time or near-real-time view of regulatory compliance posture for management and ISMS stakeholders.

**Implementation**: Assessment Workbook 6 (Regulatory Compliance Dashboard) provides template; may be automated via compliance management software.

**Key Metrics**:

**Regulatory Landscape**:

- Number of applicable regulations (by tier):
  - Tier 1 Mandatory: [X]
  - Tier 2 Conditional: [Y]
  - Tier 3 Informational: [Z]
- Recent regulatory changes (last 30/90 days): [Count]
- Regulations under assessment: [Count]

**Requirements Coverage**:

- Total requirements extracted: [X]
- Requirements with Primary control mapping: [Y] ([Y/X]%)
- Requirements with gaps (no Primary mapping): [Z] ([Z/X]%)
- Gap trend: ↑ Increasing / → Stable / ↓ Decreasing

**Gap Status**:

- Open gaps by priority:
  - Critical: [X]
  - High: [Y]
  - Medium: [Z]
  - Low: [W]
- Gaps remediated this period: [Count]
- Average gap age: [Days]
- Overdue gaps (past target closure date): [Count]

**Evidence Coverage**:

- Requirements with evidence: [X] ([X/Total]%)
- Evidence gaps: [Y]
- Evidence approaching expiration (next 30 days): [Z]
- Evidence expired: [W]

**Regulatory Changes**:

- Changes detected this quarter: [X]
- Changes under assessment: [Y]
- Changes implemented: [Z]

**Visualization**:

- **Charts**: Pie chart (regulations by tier), bar chart (gaps by priority), trend line (gap count over time)
- **Heat Map**: Regulation × Requirements showing compliance status (green = full compliance, yellow = partial, red = gap)
- **Gauges**: Overall compliance percentage (requirements satisfied / total requirements)

**Access**:

- Executive Management: High-level dashboard with summary metrics
- ISMS Manager / Compliance Officer: Detailed dashboard with drill-down capabilities
- Control Owners: Filtered view showing their controls only

**Update Frequency**:

- Automated dashboards: Real-time (updates as underlying data changes)
- Manual dashboards: Weekly refresh

### Management Reporting

**Purpose**: Periodic briefings to Executive Management on compliance status, significant changes, and resource needs.

**Frequency**: 

- **Routine**: Quarterly
- **Triggered**: Upon significant regulatory change, major gap identification, or audit findings

**Report Structure**:

**Executive Summary** (1 page):

- Overall compliance status (compliant / minor gaps / significant gaps / non-compliant)
- Summary of significant developments this period
  - New regulations applicable
  - Major regulatory changes
  - High-priority gaps identified or closed
- Key risks and issues
- Resource requests (if needed)
- Recommendations for executive action

**Detailed Sections** (3-5 pages):
1. **Regulatory Landscape Update**:

   - New regulations identified (applicability determination)
   - Regulatory changes detected and assessed
   - Regulations added/removed from ISMS-POL-00
   
2. **Compliance Status**:

   - Compliance metrics (requirements satisfied, gaps, evidence coverage)
   - Trend analysis (improving or degrading)
   - Per-regulation compliance summary (for Tier 1 regulations)
   
3. **Gap Analysis & Remediation**:

   - High-priority gaps and remediation status
   - Gaps closed this period
   - Overdue gaps requiring escalation
   
4. **Evidence & Audit Readiness**:

   - Evidence collection status
   - Upcoming audits (preparation status)
   - Audit findings from previous period (remediation status)
   
5. **Resource Needs**:

   - Budget requests (for control implementation, consulting, technology)
   - Staffing needs (if compliance workload exceeds capacity)
   - Training requirements

**Appendices**:

- Detailed gap register (all open gaps)
- Regulatory change log (all changes detected this period)
- Compliance dashboard screenshots
- Risk register (regulatory compliance risks)

**Distribution**:

- CEO, CFO, CIO, CISO
- General Counsel
- Board of Directors (summary only, annually or upon request)

### Control Owner Reporting

**Purpose**: Provide individual Control Owners with targeted information about their controls and responsibilities.

**Frequency**: Monthly or quarterly

**Report Content** (Personalized per Control Owner):

- **Your Controls**: List of controls you own (e.g., Control Owner for A.8.24 sees A.8.24-specific report)
- **Requirements Mapped to Your Controls**: Which regulatory requirements your controls satisfy
- **Evidence Status**:
  - Evidence required for your controls
  - Evidence collected (current, complete)
  - Evidence gaps (missing, expired, inadequate)
- **Action Items**:
  - Evidence collection tasks (what evidence to collect by when)
  - Gap remediation tasks (if your controls have gaps)
  - Upcoming verification/validation activities
- **Support Requests**: Option to request support from Compliance Team

**Delivery**: Email report or dashboard portal (personalized login shows Control Owner's data only)

**Benefits**:

- Control Owners see their specific responsibilities
- Reduces noise (don't see irrelevant controls)
- Actionable (clear tasks with deadlines)
- Accountability (Control Owner knows they're being tracked)

## External Reporting

### Regulatory Submissions & Filings

**Purpose**: Satisfy regulatory requirements for periodic submissions, notifications, or filings.

**Examples**:

- **Breach Notifications**:
  - Notify supervisory authority within [X] hours of becoming aware of personal data breach (e.g., GDPR 72 hours)
  - Format: Prescribed by regulation (often online form or structured email)
  - Evidence: Submission confirmation (screenshot, email receipt)
  
- **Annual Compliance Reports**:
  - Some regulations require annual attestation of compliance
  - Format: Regulatory authority may provide template
  - Content: Compliance status, material changes, incidents (if any)
  - Evidence: Filed report and submission proof
  
- **Certifications**:
  - Some sectors require periodic certification to regulatory authority (e.g., financial services)
  - Evidence: Certification issued by authority

**Process**:
1. Identify required submission (from regulation text or regulatory authority notification)
2. Prepare submission content (Compliance Officer, with input from Legal, Control Owners, ISMS Manager)
3. Legal Counsel reviews submission for accuracy and legal implications
4. Executive Management approves submission (for significant filings)
5. Submit via required method (online portal, certified mail, email)
6. Retain proof of submission (confirmation number, receipt, timestamp)
7. Store copy of submission in Evidence Repository

**Timeliness Critical**: Regulatory submissions often have strict deadlines (e.g., 72 hours for breach notification). Late submission may be separate violation.

### Customer Compliance Attestations

**Purpose**: Customers may request attestations or confirmations of compliance with contractual security requirements.

**Trigger**: Customer request (often annual or semi-annual per contract terms)

**Process**:
1. **Receive Request**: Customer sends compliance questionnaire or requests attestation
2. **Review Requirements**: Compliance Officer reviews what customer is asking for
3. **Gather Evidence**: Compile evidence demonstrating compliance

   - Reference Evidence Repository
   - May need to collect specific evidence customer requests

4. **Prepare Attestation**: Draft compliance statement or complete questionnaire

   - Example: "We attest that we comply with security requirements in Section 12 of the Service Agreement dated [Date], including [list key requirements]"

5. **Attach Supporting Evidence** (if customer requests):

   - SOC 2 report
   - ISO 27001 certificate
   - Specific evidence (vulnerability scan summaries, policy documents, audit reports)

6. **Legal Review**: Legal Counsel reviews attestation for accuracy and liability
7. **Executive Approval**: CISO or Executive Management signs attestation
8. **Submit to Customer**: Deliver via secure method (encrypted email, secure portal)
9. **Retain Copy**: Store in Evidence Repository and contract file

**Attestation Content**:

- Statement of compliance (affirmative declaration)
- Scope of attestation (which requirements, which time period)
- Supporting evidence (attached or referenced)
- Limitations/caveats (if any - e.g., "except as disclosed in attached report")
- Signature of authorized representative (CISO, Legal, Executive)
- Date

### Audit Responses

**Purpose**: Respond to external auditor requests for evidence and information.

**Audit Types**:

- **Certification Audits**: ISO 27001, SOC 2, PCI DSS v4.0.1 QSA, etc.
- **Customer Audits**: Customer exercising contractual audit rights
- **Regulatory Audits**: Regulator conducting examination or inspection

**Process**:
1. **Pre-Audit Preparation** (4-6 weeks before audit):

   - Comprehensive evidence gap review (Section 5.5)
   - Close critical and high gaps
   - Pre-assemble evidence packages
   - Designate Evidence Custodian for audit period
   
2. **Audit Kick-Off**:

   - Understand auditor's scope, methodology, sample selections
   - Clarify audit timeline and deliverables
   - Confirm Evidence Custodian as primary contact for evidence requests
   
3. **Evidence Provision**:

   - Auditor requests specific evidence
   - Evidence Custodian retrieves from Evidence Repository
   - Provide evidence to auditor via secure method (portal, encrypted files)
   - Track what evidence provided (avoid duplication, ensure completeness)
   
4. **Auditor Findings**:

   - Auditor identifies findings (non-conformities, observations, opportunities for improvement)
   - Compliance Team and Control Owners review findings
   - Clarify with auditor if misunderstanding (provide additional evidence if needed)
   
5. **Corrective Action Plans**:

   - For findings requiring correction, develop corrective action plan
   - Address root cause (not just symptom)
   - Timeline for remediation
   - Submit to auditor for acceptance
   
6. **Post-Audit Follow-Up**:

   - Implement corrective actions
   - Provide evidence of remediation to auditor (for closing findings)
   - Update compliance framework (if audit revealed framework gaps)
   - Lessons learned (improve for next audit)

**Evidence Package Assembly**:

- For recurring audits (ISO 27001 surveillance), maintain pre-assembled evidence package
- Update package quarterly (add new evidence, remove obsolete)
- Package includes:
  - Policies (all applicable)
  - Procedures (key procedures auditor typically requests)
  - Recent evidence (logs, reports, test results from last 12 months)
  - Previous audit reports and corrective action completion evidence

### Certification Body Submissions

**Purpose**: Submit evidence and information to certification bodies (ISO 27001, SOC 2 auditors, etc.) for initial certification and ongoing surveillance.

**Certification Cycle**:

- **Initial Certification**: Comprehensive evidence package, Stage 1 (documentation review) and Stage 2 (implementation audit)
- **Surveillance Audits**: Annual audits (typically lighter, focus on changes and sampling)
- **Recertification**: Every 3 years (comprehensive like initial certification)

**Submission Requirements** (Specific to Certification Standard):

- **ISO 27001**:
  - Statement of Applicability (SoA) mapping requirements to controls
  - Risk Assessment and Risk Treatment Plan
  - ISMS policies (POL-5.31.1 through 5.31.4 for A.5.31)
  - Control implementation evidence (for all controls in SoA)
  - Internal audit reports
  - Management review minutes
  
- **SOC 2**:
  - System description (what systems and processes are in scope)
  - Control descriptions (matrix of controls and how implemented)
  - Evidence of control operation (logs, reports, configurations)
  - Management assertions (management's statement of control effectiveness)
  
- **PCI DSS v4.0.1**:
  - Self-Assessment Questionnaire (SAQ) or Report on Compliance (ROC)
  - Attestation of Compliance (AOC)
  - Quarterly vulnerability scans (by Approved Scanning Vendor)
  - Compensating controls documentation (if any)

**Preparation Timeline**:

- Begin preparation 2-3 months before certification audit
- Conduct internal readiness assessment
- Close evidence gaps
- Internal audit of ISMS (for ISO 27001 - required before certification audit)
- Management review (for ISO 27001 - required before certification audit)

**Submission & Audit**:

- Submit evidence package to certification body
- Certification auditor reviews documentation (desk review)
- On-site or remote audit (interviews, evidence validation, observations)
- Findings issued (non-conformities must be addressed before certificate issued)
- Certificate issued (if compliant)

**Ongoing Maintenance**:

- Address surveillance audit findings
- Maintain evidence collection between audits (continuous, not just pre-audit scramble)
- Track certification expiration dates, plan recertification in advance

## Reporting Frequency

### Continuous

**Compliance Dashboard**: 

- Always current (updated as underlying data changes)
- Accessible on-demand by stakeholders
- No scheduled delivery (stakeholders access when needed)

**Automated Alerts**:

- Gap creation: Alert when new gap identified (immediate email to Compliance Officer, ISMS Manager)
- Evidence expiration: Alert when evidence approaching expiration (30 days prior, 7 days prior)
- Regulatory change detection: Alert when regulatory change detected (immediate or daily digest)

### Periodic

**Quarterly Management Reports**:

- Executive briefing on compliance status
- Delivered within 2 weeks of quarter end
- Scheduled presentation to Executive Management

**Annual Comprehensive Compliance Review**:

- Deep dive into compliance posture
- Review of all applicable regulations (reconfirm applicability)
- Comprehensive evidence review
- Gap analysis and prioritization
- Resource planning for next year
- Delivered Q4 or Q1 (annual planning cycle)

**Bi-Annual Control Effectiveness Reviews**:

- Control Owners assess effectiveness of their controls
- Twice per year (mid-year and year-end)
- Feeds into compliance reporting and internal audit planning

### Event-Driven

**Significant Regulatory Change Detected**:

- Impact assessment completed → Impact Report to Executive Management
- Timeline: Within 2 weeks of completing impact assessment
- Content: Change summary, impact on [Organization], recommended action, resource needs

**Major Gap Identified**:

- High or Critical priority gap → Escalation Report
- Timeline: Within 48 hours of gap identification
- Content: Gap description, affected requirements/regulations, risk, remediation plan

**Regulatory Inquiry Received**:

- Regulator requests information or initiates investigation
- Timeline: Immediate notification to Executive Management and Legal Counsel
- Content: Nature of inquiry, required response, timeline, preparation plan

**Audit Scheduled**:

- Audit scheduled → Readiness Report
- Timeline: 4-6 weeks before audit
- Content: Audit scope, evidence gaps, remediation plan, resource needs, readiness status

### On-Demand

**Auditor Requests**: 

- Ad-hoc evidence requests during audit
- Response timeline: Per auditor's request (typically within 24-48 hours)

**Customer Inquiries**:

- Customer requests compliance information
- Response timeline: Per customer SLA (typically within 1-2 weeks)

**Executive Queries**:

- Executive Management requests specific compliance information
- Response timeline: Within 24 hours (summary) to 1 week (comprehensive)

**Board Requests**:

- Board of Directors requests compliance briefing
- Response timeline: Per Board meeting schedule (typically 2-4 weeks for preparation)

---

# Records Retention

Compliance records must be retained for specified periods to support audits, regulatory inquiries, and legal defense.

## Retention Periods Per Regulation Type

### Legal/Statutory Requirements

**Regulation-Specified Retention**:

- Many regulations explicitly state retention periods
- Examples:
  - GDPR: Not explicit, but data protection authorities commonly require 3-7 years for compliance records
  - Financial regulations: Often 7-10 years for financial transaction records
  - Tax regulations: Varies by jurisdiction (typically 5-7 years)
- **Approach**: Review each applicable regulation for retention requirements; comply with specified period

**Common Retention Periods** (When Regulation Specifies):

- **3 years**: Some data protection and privacy regulations
- **5 years**: Common for business records, contracts
- **7 years**: Common baseline for compliance and audit records
- **10 years**: Some financial and tax regulations

**Calculating Retention Period**:

- Typically measured from: Event date, end of fiscal year, or end of regulatory applicability
- Example: "Retain incident response records for 7 years from incident closure date"

### Contractual Requirements

**Contract Terms Govern**:

- Customer contracts may specify retention periods for compliance records
- Often: Contract duration + X years
- Example: "Supplier shall retain security compliance records for the duration of the contract plus 5 years thereafter"

**Audit Rights Alignment**:

- Contract may grant customer audit rights for X years after contract ends
- Retention period must cover audit rights period
- Example: Customer can audit for 3 years post-contract → Must retain evidence for at least 3 years post-contract

**Longest Period Wins**:

- If regulation requires 7 years AND contract requires 5 years → Retain for 7 years
- If contract requires 10 years AND regulation requires 7 years → Retain for 10 years
- Apply most stringent retention requirement

### Organizational Policy

**Default Retention** (When Regulation/Contract Silent):

- [Organization] establishes default retention period
- Common practice: **7 years**
- Rationale:
  - Aligns with many common regulatory and legal retention periods
  - Statute of limitations in many jurisdictions is 5-7 years
  - Provides reasonable defense against retroactive inquiries

**Longer for Critical Compliance Records**:

- For critical compliance records (e.g., major incident response, significant audit findings, regulatory submissions), consider longer retention
- Example: 10 years for records related to significant data breaches or regulatory investigations
- Rationale: Potential for long-tail liability or inquiries

**Organizational Policy Documentation**:

- Document default retention periods in Records Retention Policy
- Specify exceptions (longer retention for specific record types)
- Approval by Legal Counsel and Executive Management

## Retention for Framework Documents

### Active Regulations

**Indefinite Retention** (While Regulation Applicable):

- All framework documents for active regulations retained indefinitely
- Includes:
  - ISMS-POL-00 entry
  - Requirements Register entries
  - Control Mapping Matrix mappings
  - Gap Register (open and closed gaps)
  - Evidence Register (current and historical evidence)
- Rationale: Ongoing compliance obligation; historical audit trail valuable

**Version Retention** (All Versions):

- Retain ALL versions of framework documents
- Purpose:
  - Audit trail showing framework evolution
  - Demonstrate proactive framework maintenance
  - Support retroactive inquiries ("How did you interpret this requirement in 2023?")
- Storage: Archive folder or version control system

### Superseded/Repealed Regulations

**Post-Repeal Retention**:

- When regulation repealed or [Organization] exits jurisdiction, framework documents not immediately deleted
- Retention period: **7 years after regulation ceases to apply** (or longer per legal counsel guidance)
- Rationale:
  - Demonstrate historical compliance (if retroactive inquiry or investigation)
  - Statute of limitations defense
  - Contract claims or litigation may arise years later

**Archival Process**:
1. Regulation repealed or [Organization] determines regulation no longer applicable
2. Mark regulation as "Repealed - [Date]" or "No Longer Applicable - [Date]" in ISMS-POL-00
3. Archive framework documents (move to "Historical_Compliance" folder)
4. Calculate disposal date: Repeal Date + 7 years
5. Set reminder for disposal date
6. At disposal date: Legal review (confirm no legal hold, no ongoing litigation) → Secure disposal per Section 7.4

**Example**:

- Old Data Protection Law repealed 2025-01-01 when new law took effect
- Framework documents for Old Law archived 2025-01-01
- Disposal date: 2032-01-01 (7 years later)
- 2032: Legal review → Confirm no legal hold → Securely dispose

## Legal Hold Procedures

### What is Legal Hold

**Definition**: Legal hold (litigation hold, preservation order) is suspension of normal records retention/disposal procedures when litigation, investigation, or regulatory inquiry is reasonably anticipated or active.

**Purpose**: Preserve records that may be relevant to legal proceedings or investigations.

**Scope**: All records potentially relevant to the matter (broad scope to avoid inadvertent destruction of relevant evidence).

**Overrides**: Legal hold overrides normal retention policies (even if retention period expired, records on legal hold are NOT disposed).

### Legal Hold Process

**Trigger Events**:

- **Litigation**: Lawsuit filed against [Organization] or [Organization] filing lawsuit
- **Regulatory Investigation**: Regulatory authority initiates investigation or inquiry
- **Regulatory Inquiry**: Regulator requests information (may be precursor to investigation)
- **Internal Investigation**: Internal investigation that may lead to litigation or regulatory action
- **Threatened Litigation**: Credible threat of lawsuit (demand letter received)

**Legal Hold Process**:

**Step 1: Legal Counsel Declaration**:

- General Counsel or external legal advisor assesses situation
- Determines whether legal hold is warranted
- If yes, issues Legal Hold Notice

**Step 2: Identify Affected Records**:

- Legal Counsel works with Compliance Officer, ISMS Manager, IT to identify:
  - Types of records potentially relevant (emails, compliance records, incident reports, etc.)
  - Custodians (people or systems holding relevant records)
  - Time period (from what date to what date)
- Broad scope to ensure preservation of all potentially relevant evidence

**Step 3: Issue Legal Hold Notices**:

- Legal Counsel issues written Legal Hold Notice to:
  - Record custodians (employees with relevant records)
  - IT Department (for systems containing relevant data)
  - Compliance Officer (for compliance framework records)
- Notice instructs:
  - DO NOT delete, modify, or destroy any records related to [matter]
  - Preserve records in original form
  - Notify Legal Counsel if unclear whether record is covered
  - Consequences of violation (disciplinary action, legal sanctions)

**Step 4: Preserve Records**:

- Custodians and IT halt normal disposal processes for affected records
- Records segregated (if possible) or flagged (in systems)
- Backups preserved (if records on backup systems)
- Compliance evidence repository: Mark affected evidence as "Legal Hold - Do Not Dispose"

**Step 5: Monitor Compliance**:

- Legal Counsel periodically verifies hold is being followed
- Reminders sent to custodians (quarterly or as needed)
- Hold remains in effect until Legal Counsel releases it

**Step 6: Release of Legal Hold**:

- When litigation/investigation concludes or Legal Counsel determines hold no longer necessary
- Legal Counsel issues Legal Hold Release Notice
- Records return to normal retention schedule
- Disposal may now occur if retention period expired (subject to legal review)

**Documentation**:

- Legal Hold Notice (written directive from Legal Counsel)
- Custodian Acknowledgments (confirmation of receipt and understanding)
- Legal Hold Log (centralized list of all active legal holds)
- Release Notices (when holds lifted)

**Training**:

- Employees trained on legal hold obligations
- Emphasize: Deliberate destruction of records under legal hold is spoliation (serious legal consequences)

## Secure Disposal

### When to Dispose

**Criteria** (ALL must be met):

- ☑ Retention period expired (per Section 7.1)
- ☑ No legal hold in effect (per Section 7.3)
- ☑ No ongoing audit or investigation requiring records
- ☑ Legal Counsel approval obtained (for sensitive or significant records)
- ☑ Compliance Officer approval obtained

**Review Before Disposal**:

- Compliance Officer reviews disposal candidates quarterly
- Legal Counsel consulted if records potentially sensitive
- Executive approval for disposal of records related to significant events (major incidents, investigations, litigation)

### Disposal Method

**Electronic Evidence**:

- **Secure Deletion** (Data Sanitization):
  - Overwrite data multiple times (DoD 5220.22-M standard: 3-pass overwrite minimum)
  - Cryptographic erasure (if data encrypted at rest, destroy encryption keys)
  - Tools: DBAN (Darik's Boot and Nuke), Eraser, shred utilities (Linux/Unix), BitLocker cryptographic erasure (Windows)
- **NOT Sufficient**: Recycle bin deletion, simple file deletion (data recoverable)
- **Verification**: Confirm deletion successful (attempt recovery to verify unrecoverable)

**Cloud-Based Evidence**:

- Delete from cloud storage (5.31.3, Azure Blob, Google Cloud Storage)
- Verify deletion propagated (not soft-delete with retention period)
- If using compliance/legal hold features in cloud (AWS 5.31.3 Object Lock, Azure Immutable Blob Storage), wait for retention period to expire before deletion possible

**Physical Evidence** (Paper Documents, Physical Media):

- **Shredding** (Paper):
  - Cross-cut shredder minimum (strip-cut not secure)
  - Particle size: <5mm x <50mm recommended
  - For highly sensitive: Industrial shredding or pulverization
- **Physical Destruction** (Hard Drives, USB Drives, CDs):
  - Degaussing (for magnetic media like hard drives)
  - Physical destruction (drill, shredder, hammer, incineration)
  - Certified destruction by vendor (Certificate of Destruction provided)
- **Certificate of Destruction**:
  - For highly sensitive material, obtain Certificate of Destruction from destruction vendor
  - Certificate documents: What was destroyed, when, method, vendor signature

### Disposal Logging

**Evidence Disposal Log** (Maintained by Compliance Officer):

**Log Fields**:

- **Disposal ID**: Unique identifier (DISP-[Year]-[Seq])
- **Evidence ID or Description**: What was disposed
- **Record Type**: Compliance evidence, policy, log, report, etc.
- **Regulation/Control**: Which regulation or control it related to (if applicable)
- **Retention Period End Date**: When retention period expired
- **Disposal Date**: Actual disposal date
- **Disposed By**: Name/role of person authorizing and executing disposal
- **Disposal Method**: Secure deletion, shredding, physical destruction, etc.
- **Verification**: How disposal verified (e.g., "Attempted recovery failed - data unrecoverable")
- **Approval**: Compliance Officer and Legal Counsel approval (signatures or email confirmations)
- **Rationale**: Why disposed (retention expired, legal hold cleared, no ongoing need)

**Disposal Log Review**:

- Internal Audit reviews Disposal Log annually
- Confirms disposals were authorized
- Verifies disposal methods were secure
- Checks for unauthorized disposals (records disposed before retention period expired or during legal hold)

**Audit of Disposal Process**:

- Periodically audit disposal process (annual or bi-annual)
- Test sample of disposed records (attempt recovery to verify secure disposal)
- Verify disposal log completeness and accuracy

---

# Document Control & Related Documents

## Document Information

**Document ID**: ISMS-POL-A.5.31.4  
**Title**: Change Management & Evidence Framework  
**Version**: 1.0  
**Effective Date**: [TBD upon approval]  
**Classification**: Internal  
**Owner**: Compliance Officer / ISMS Manager  

**Review Frequency**: Annually or upon:

- Significant changes to regulatory monitoring processes
- Major updates to evidence management systems
- Organizational changes affecting compliance operations
- Process improvements identified

**Next Review Date**: [Effective Date + 12 months]

## Related Documents

**ISMS Policy Framework**:

- **ISMS-POL-A.5.31.1**: Executive Summary & Control Alignment
  - Provides framework foundation and governance
  - Defines roles referenced in this document
- **ISMS-POL-A.5.31.2**: Regulatory Applicability Methodology
  - Determines which regulations apply (input to monitoring)
  - Maintains ISMS-POL-00
- **ISMS-POL-A.5.31.3**: Requirements Extraction & Control Mapping Framework
  - Defines requirements extraction and control mapping (used in impact assessment)
  - Establishes traceability framework (maintained through updates)
- **ISMS-POL-00**: Regulatory Applicability Framework
  - Master regulatory register (updated per Section 4)

**Implementation Guides**:

- **ISMS-IMP-A.5.31.4-UG/TG**: Regulatory Monitoring Process
  - Step-by-step operational guide for regulatory monitoring (implements Section 2)
- **ISMS-IMP-A.5.31.5-UG/TG**: Evidence Management Process
  - Step-by-step operational guide for evidence management (implements Section 5)

**Assessment Workbooks**:

- **Regulatory Change Register**: Template for logging regulatory changes (Section 2.3)
- **Impact Assessment Template**: Template for impact assessments (Section 3.3)
- **Assessment Workbook 5**: Compliance Evidence Register (Section 5)
- **Assessment Workbook 6**: Regulatory Compliance Dashboard (Section 6.1.1)

**Standards & External References**:

- **ISO/IEC 27001:2022**: Information Security Management Systems - Requirements
  - Clause 9.3: Management Review (compliance reporting integration)
  - Clause 7.5: Documented Information (records retention)

## Definitions

**Evidence**: Tangible proof that [Organization] complies with regulatory requirements through implemented controls.

**Evidence Gap**: Regulatory requirement or control for which evidence is missing, expired, or inadequate.

**Legal Hold**: Suspension of normal retention/disposal when litigation or investigation is anticipated or active.

**Regulatory Change**: Modification to regulation (amendment, new regulation, repeal, guidance, enforcement action).

**Retention Period**: Time duration for which compliance records must be preserved before authorized disposal.

**Traceability**: Ability to trace from regulation through requirements and controls to evidence (forward) and reverse (evidence back to regulation).

---

**END OF DOCUMENT**

---

*This policy establishes [Organization]'s systematic approach to maintaining the regulatory compliance framework and demonstrating compliance through evidence, enabling audit readiness and regulatory confidence.*
<!-- QA_VERIFIED: 2026-02-01 -->
