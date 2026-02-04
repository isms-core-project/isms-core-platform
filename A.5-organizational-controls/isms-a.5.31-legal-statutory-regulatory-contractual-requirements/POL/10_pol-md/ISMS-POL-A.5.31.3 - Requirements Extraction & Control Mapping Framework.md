**ISMS-POL-A.5.31.3: Requirements Extraction & Control Mapping Framework**
**Legal, Statutory, Regulatory and Contractual Requirements**

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Requirements Extraction & Control Mapping Framework |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.31.3 |
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

# Introduction & Relationship to 5.31.1/5.31.2

## Purpose of This Policy Section

This policy section establishes [Organization]'s systematic framework for translating regulatory obligations into actionable security controls with complete traceability. It defines the processes by which legal and regulatory text is transformed into implementable requirements, mapped to ISO 27001 controls, and tracked through to evidence.

**This is the "translation layer"** of the regulatory compliance framework—the critical link between identifying applicable regulations and demonstrating compliance through implemented controls.

## Progression: Applicability → Requirements → Controls

The regulatory compliance framework operates in a logical progression:

**ISMS-POL-A.5.31.1** established the overall framework architecture, governance model, and integration with ISMS-POL-00 (Regulatory Applicability Framework). It defined the "why" and the structural foundation.

**ISMS-POL-A.5.31.2** defined the systematic methodology for determining WHICH regulations apply to [Organization] based on geographic, operational, and contractual criteria. It answers the question: "What laws govern us?"

**ISMS-POL-A.5.31.3** (this document) defines the systematic methodology for determining WHAT those applicable regulations require and HOW [Organization] complies through ISO 27001 controls. It answers the questions:

- "What specific obligations do these regulations impose?"
- "Which security controls satisfy these obligations?"
- "Where are the gaps in our current control implementation?"
- "How do we prove compliance through evidence?"

**ISMS-POL-A.5.31.4** (subsequent) will define how [Organization] monitors regulatory changes, manages framework updates, and maintains audit-ready evidence.

## The Translation Challenge

Regulations are written in legal language by legislators and regulators. Security controls are written in technical and organizational language by security professionals. These two domains speak different languages:

**Legal Language**:

- "The controller shall implement appropriate technical and organizational measures to ensure a level of security appropriate to the risk..."
- Written for legal compliance and enforcement
- Often principle-based rather than prescriptive
- May reference technical concepts without specific implementation guidance

**Security Control Language**:

- "A.5.15 Access Control: Information and other associated assets shall be made accessible to authorized users only."
- Written for security practitioners
- Focused on what to implement, not legal compliance
- Specific enough to guide implementation

**The Translation Challenge**: How do we systematically and repeatably extract specific, actionable requirements from regulatory text and map them to existing security controls?

The methodology defined in this document solves this challenge through:
1. **Systematic requirements extraction** - parsing regulatory text into discrete, actionable requirements
2. **Requirements categorization** - organizing requirements by nature (technical, organizational, reporting, operational)
3. **Control mapping** - identifying which ISO 27001 Annex A controls satisfy each requirement
4. **Gap analysis** - identifying where requirements exist without corresponding controls
5. **Traceability** - maintaining complete audit trail from regulation through requirement to control to evidence

## Document Scope

This policy section applies to:

- **All regulations** identified as applicable in ISMS-POL-00 (Tier 1 Mandatory and Tier 2 Conditional regulations)
- **All ISO 27001:2022 Annex A controls** (93 controls across organizational, people, physical, and technological domains)
- **Organization-specific controls** created when no Annex A control satisfies a requirement
- **All personnel** involved in regulatory compliance, control implementation, and evidence management

This document does NOT:

- Provide legal interpretations of specific regulations (legal counsel required)
- Specify which regulations apply to [Organization] (covered in 5.31.2)
- Define operational procedures for extraction and mapping (covered in IMP-5.31.2 and IMP-5.31.3)
- Define evidence management processes (covered in 5.31.4)

---

# Requirements Extraction Process

## Requirements Extraction Methodology

Requirements extraction is the systematic process of parsing regulatory text to identify specific, mandatory obligations that [Organization] must satisfy. This process transforms verbose, principle-based legal text into discrete, actionable requirements suitable for control mapping.

### Reading Regulatory Text Systematically

Regulations have structure, though it varies by jurisdiction and type:

- **Statutes and Acts**: Typically organized into chapters, sections, subsections, paragraphs
- **Regulations and Directives**: Organized into articles, sections, annexes, schedules
- **Standards**: Organized into clauses, subclauses, requirements, recommendations
- **Contracts**: Organized into sections, clauses, exhibits, service level agreements

Each structural element may contain:

- **Definitions** - establishing meaning of terms (extract for glossary, not as requirements)
- **Principles** - high-level objectives (may generate requirements when made mandatory)
- **Obligations** - specific things [Organization] must do (THESE are requirements)
- **Prohibitions** - things [Organization] must NOT do (requirements stated negatively)
- **Procedures** - how to comply with obligations (may generate operational requirements)
- **Reporting requirements** - what to submit and when
- **Penalties** - consequences of non-compliance (inform prioritization, not extracted as requirements)

**Systematic Reading Process**:

1. **Review entire regulation** to understand overall intent and scope
2. **Identify structural boundaries** (where one requirement ends, another begins)
3. **Parse each section/article** for discrete obligations
4. **Distinguish** between mandatory obligations, recommendations, and contextual information
5. **Extract** each mandatory obligation as a separate requirement
6. **Note interdependencies** where requirements reference or depend on others

**Common Pitfalls**:

- **Over-aggregation**: Extracting entire article as single requirement when it contains multiple distinct obligations
- **Under-extraction**: Missing requirements embedded in definitional or procedural text
- **Interpretation creep**: Adding obligations not explicitly stated in regulation
- **Ignoring context**: Extracting requirements without understanding their broader regulatory purpose

### Identifying Mandatory vs. Recommendatory Language

Regulations use specific language to indicate obligation level. [Organization] extracts MANDATORY requirements for compliance and notes recommendatory language for context and best practice guidance.

**Mandatory Language** (SHALL/MUST extract):

- **"shall"** - primary indicator of legal obligation
- **"must"** - equivalent to "shall", mandatory requirement
- **"is required to"** - explicit requirement
- **"will"** - when used prescriptively (e.g., "the organization will implement...")
- **"has a duty to"** - imposes obligation
- **"is obligated to"** - explicit obligation

**Recommendatory Language** (MAY extract as optional/best practice):

- **"should"** - recommendation, not mandatory
- **"is encouraged to"** - voluntary action
- **"may"** - permissive, optional
- **"can"** - possibility, not requirement
- **"it is recommended"** - best practice guidance

**Conditional Language** (extract WITH conditions):

- **"shall, where applicable"** - mandatory when condition met
- **"must, if [condition]"** - mandatory when specific circumstance exists
- **"is required to, in cases where..."** - conditional obligation

**Context Matters**: Language alone is insufficient. Legal counsel should review extractions to confirm whether seemingly recommendatory language creates enforceable obligations in specific regulatory contexts.

**Example Extraction Decisions**:

| Regulatory Text | Mandatory? | Extraction Decision |
|----------------|------------|---------------------|
| "Organizations shall implement encryption for data at rest" | Yes (shall) | Extract: "Implement encryption for data at rest" |
| "Organizations should consider multi-factor authentication" | No (should) | Note as best practice, do not extract as requirement |
| "Organizations must conduct annual risk assessments" | Yes (must) | Extract: "Conduct risk assessments annually" |
| "Organizations may use industry-standard frameworks" | No (may) | Note as option, do not extract as requirement |
| "Where personal data is processed, organizations shall obtain consent" | Conditional (shall, where...) | Extract: "Obtain consent when processing personal data" |

### Granularity Guidelines

Requirements must be extracted at the right level of detail—specific enough to be actionable, but not so prescriptive that they eliminate implementation flexibility.

**Too Coarse** (Not Actionable):

- ❌ "Comply with Article 32"
  - Problem: No guidance on WHAT to do to comply
  - Cannot map to specific controls
  - Not implementable

- ❌ "Implement appropriate security measures"
  - Problem: "Appropriate" is undefined
  - Too vague to verify compliance
  - Leaves implementers guessing

**Too Fine** (Over-Prescriptive):

- ❌ "Use AES-256-GCM encryption with PBKDF2 key derivation using 10,000 iterations and SHA-256 hashing for all data at rest"
  - Problem: Eliminates flexibility in implementation
  - Technology evolves, overly specific requirements become obsolete
  - May conflict with other regulations allowing equivalent controls

- ❌ "Conduct penetration testing on the second Tuesday of March each year"
  - Problem: Unnecessarily specific timing
  - Regulation likely just requires "annual" testing
  - Creates rigid process that may not align with business needs

**Just Right** (Actionable with Flexibility):

- ✅ "Implement encryption for data at rest using industry-standard algorithms and key lengths appropriate to the sensitivity of the data"
  - Actionable: Clear WHAT (encrypt data at rest)
  - Flexible: Implementation choice of algorithm (AES-256, ChaCha20, etc.)
  - Guidance: "Industry-standard" and "appropriate to sensitivity" provide boundaries
  - Mappable: Can map to ISO 27001 controls on encryption

- ✅ "Conduct vulnerability assessments of all internet-facing systems at least quarterly"
  - Actionable: Clear WHAT (vulnerability assessments), WHICH (internet-facing), WHEN (quarterly minimum)
  - Flexible: Choice of scanning tools, methodology details
  - Verifiable: Can demonstrate quarterly scans occurred
  - Mappable: Can map to ISO 27001 controls on vulnerability management

**Granularity Decision Framework**:

Ask these questions when determining extraction granularity:
1. **Can someone implement this without guessing?** (If no → too coarse)
2. **Does this allow reasonable implementation choices?** (If no → too fine)
3. **Can we map this to one or more controls?** (If no → adjust granularity)
4. **Can we collect evidence to prove compliance?** (If no → too vague)
5. **Will this requirement remain valid as technology evolves?** (If no → too prescriptive)

**General Principle**: Extract requirements at the level where the regulation ACTUALLY mandates specificity. If regulation says "encryption", don't add "AES-256". If regulation says "AES-256", don't generalize to "encryption".

## Requirements Categorization

Once extracted, requirements are categorized by their nature to facilitate control mapping and implementation assignment. Each requirement may fall into one or more categories.

### Technical Requirements

Requirements that mandate specific technical security measures, system configurations, or technology implementations.

**Characteristics**:

- Require technical implementation (code, configuration, systems)
- Often implemented by IT, Security Engineering, Development teams
- Can be technically verified (scans, audits, tests)

**Examples** (generic):

- "Implement network segmentation to isolate sensitive systems"
- "Deploy anti-malware protection on all endpoints"
- "Enable encryption for data in transit using TLS 1.2 or higher"
- "Configure systems to enforce password complexity requirements"
- "Implement automated log collection and centralized storage"

**Typical Control Mappings**: Technical requirements typically map to ISO 27001 controls in domains:

- **Domain 8 (Technological controls)**: A.8.1 through A.8.34
- Some organizational controls with technical elements (e.g., A.5.15 Access Control)

### Organizational Requirements

Requirements that mandate policies, procedures, governance structures, roles, training, or organizational processes.

**Characteristics**:

- Require policy/procedure documentation
- Often implemented by Legal, Compliance, HR, Management
- Verified through document review and interviews

**Examples** (generic):

- "Establish and maintain an information security policy approved by executive management"
- "Define roles and responsibilities for data protection"
- "Conduct background checks for personnel with access to sensitive information"
- "Provide security awareness training to all employees annually"
- "Establish incident response procedures including escalation paths"

**Typical Control Mappings**: Organizational requirements typically map to ISO 27001 controls in domains:

- **Domain 5 (Organisational controls)**: A.5.1 through A.5.37
- **Domain 6 (People controls)**: A.6.1 through A.6.8

### Reporting Requirements

Requirements that mandate submissions, notifications, disclosures, or reports to regulatory authorities, data subjects, or other external parties.

**Characteristics**:

- Time-sensitive (specific deadlines)
- External-facing (submitted to authorities or third parties)
- Often have prescribed formats or templates
- Non-compliance directly visible to regulators

**Examples** (generic):

- "Notify the supervisory authority of personal data breaches within 72 hours of becoming aware"
- "Submit annual compliance attestation to regulatory body by March 31"
- "Notify affected individuals of security incidents involving their personal information without undue delay"
- "Maintain public register of data processing activities accessible via website"
- "Report significant cybersecurity events to sector regulator within 24 hours"

**Typical Control Mappings**: Reporting requirements often map to:

- Incident management controls (A.5.24 through A.5.28)
- Compliance monitoring controls (A.5.31, A.5.36)
- Often require CUSTOM processes beyond Annex A

**Special Considerations**: 

- Reporting requirements often have the strictest deadlines
- Failure to report is typically a separate violation
- Require robust processes and clear responsibility assignment

### Operational Requirements

Requirements that mandate specific operational procedures, business continuity measures, testing, monitoring, or ongoing operational activities.

**Characteristics**:

- Require ongoing execution (not one-time implementation)
- Often cyclic (daily, monthly, annual activities)
- Implemented by Operations, IT, Security Operations teams
- Verified through activity logs and evidence of execution

**Examples** (generic):

- "Test business continuity plans annually with documented results"
- "Monitor security event logs continuously for indicators of compromise"
- "Conduct tabletop exercises for incident response procedures semi-annually"
- "Review and update risk assessments quarterly"
- "Perform vulnerability scans of production systems monthly"

**Typical Control Mappings**: Operational requirements typically map to:

- Testing and monitoring controls (A.8.7 Protection against malware, A.8.15 Logging, A.8.16 Monitoring activities)
- Business continuity controls (A.5.29 Information security during disruption, A.5.30 ICT readiness for business continuity)
- Compliance and audit controls (A.5.36 Compliance with policies, A.5.37 Documented operating procedures)

### Purpose of Categorization

Categorization serves multiple purposes:

**Control Mapping Efficiency**: 

- Technical requirements → focus on Domain 8 controls first
- Organizational requirements → focus on Domains 5 & 6 controls first
- Saves time by narrowing search space

**Implementation Assignment**:

- Technical requirements → IT/Security Engineering teams
- Organizational requirements → Compliance/Legal/HR teams
- Reporting requirements → Compliance/Communications teams
- Operational requirements → Operations/SOC teams

**Evidence Planning**:

- Technical requirements → configuration audits, scan results, system logs
- Organizational requirements → policy documents, training records, meeting minutes
- Reporting requirements → submission confirmations, notification logs
- Operational requirements → activity logs, test results, monitoring dashboards

**Gap Analysis**:

- Categories help identify WHERE gaps exist (technical gaps vs. process gaps)
- Informs remediation approach (technical fix vs. policy creation)

**Note**: Requirements may span multiple categories. Example: "Implement and maintain multi-factor authentication for all privileged accounts" is both Technical (MFA implementation) and Organizational (policy requiring it).

## Requirements Register Structure

The Requirements Register is the authoritative, centralized repository of all extracted requirements from applicable regulations. It provides the structured foundation for control mapping, gap analysis, and compliance reporting.

### Register Fields

Each requirement entry in the register SHALL contain the following fields:

**Requirement ID** (Unique Identifier)

- **Format**: REG-[RegulationCode]-[Article/Section]-[Sequence]
- **Purpose**: Unique, stable identifier for each requirement that remains constant even if requirement text is updated
- **Examples**:
  - REG-DP01-32-001 (first requirement extracted from Data Protection Regulation Article 32)
  - REG-DP01-32-002 (second requirement from same article)
  - REG-SEC15-4.2-001 (first requirement from Security Standard Section 4.2)
- **RegulationCode**: Short code from ISMS-POL-00 regulatory register (e.g., DP01 for primary data protection law, SEC15 for security standard)

**Regulation ID** (Link to ISMS-POL-00)

- **Purpose**: Links requirement to parent regulation in regulatory register
- **Content**: Same RegulationCode used in Requirement ID
- **Use**: Enables filtering/reporting by regulation, enables cascading updates when regulation changes

**Regulation Name** (Full Regulation Name)

- **Purpose**: Human-readable identification of source regulation
- **Content**: Full official name of regulation
- **Examples**:
  - "Data Protection Act 2025"
  - "Cybersecurity Regulation (EU) 2024/1234"
  - "Payment Card Industry Data Security Standard v4.0"

**Citation** (Specific Source Location)

- **Purpose**: Precise reference to WHERE in regulation this requirement appears
- **Content**: Article, section, subsection, paragraph, clause as applicable
- **Examples**:
  - "Article 32, Paragraph 1(a)"
  - "Section 4.2.1"
  - "Requirement 8.3.2"
  - "Schedule A, Clause 12"
- **Importance**: Enables legal review, verification, and citation in compliance documentation

**Original Requirement Text** (Verbatim Quote)

- **Purpose**: Exact regulatory language as written in source regulation
- **Content**: Direct quote, no paraphrasing
- **Examples**:
  - "The controller shall implement appropriate technical and organizational measures to ensure a level of security appropriate to the risk, including inter alia as appropriate: (a) the pseudonymisation and encryption of personal data"
- **Importance**: Legal accuracy, enables verification that interpretation is faithful to source

**Interpreted Requirement** (Actionable Translation)

- **Purpose**: Requirement rewritten in clear, actionable language suitable for implementation
- **Content**: What [Organization] must DO to comply, written at appropriate granularity (per Section 2.1.3)
- **Examples**:
  - From original above: "Implement encryption and pseudonymization for personal data appropriate to assessed risk level"
- **Guidance**: Should be understandable by implementers without legal background

**Requirement Category** (Classification)

- **Purpose**: Type of requirement per Section 2.2
- **Content**: One or more of: Technical / Organizational / Reporting / Operational
- **Format**: Can be multi-select (e.g., "Technical, Organizational" for requirements spanning both)

**Priority** (Implementation Urgency)

- **Purpose**: Relative importance for implementation and gap remediation
- **Values**: 
  - **High**: Significant legal consequence for non-compliance, or compliance deadline imminent, or Tier 1 regulation
  - **Medium**: Moderate legal consequence, or reasonable timeline for compliance
  - **Low**: Minor consequence or aspirational requirement
- **Basis**: Informed by legal counsel, regulatory tier (Tier 1 vs. Tier 2), enforcement history

**Implementation Deadline** (Compliance Date)

- **Purpose**: When this requirement must be implemented/compliant
- **Content**: Specific date if regulation specifies, otherwise organizational target date
- **Examples**:
  - "2025-01-17" (regulation effective date)
  - "Within 6 months of regulation entry into force"
  - "TBD - organizational priority" (for ongoing requirements)
- **Use**: Drives implementation planning, gap remediation scheduling

**Implementation Status** (Current State)

- **Purpose**: Track implementation progress
- **Values**:
  - **Not Started**: No implementation activity yet
  - **In Progress**: Implementation underway, not yet complete
  - **Implemented**: Fully implemented and operational
  - **Verified**: Implemented and compliance verified (evidence exists)
  - **N/A**: Requirement does not apply to [Organization] based on scope/context
- **Updated By**: Control Owner responsible for implementation

**Responsible Party** (Owner)

- **Purpose**: Who is accountable for implementing this requirement
- **Content**: Role or named individual
- **Examples**:
  - "Chief Information Security Officer"
  - "IT Security Manager"
  - "Data Protection Officer"
  - "Control Owner A.8.24" (links to control ownership)

**Mapped Controls** (ISO 27001 Controls)

- **Purpose**: Which controls satisfy this requirement
- **Content**: List of control IDs with mapping type
- **Format**: "A.5.15 (P), A.5.16 (S), A.8.2 (Su)"
  - P = Primary, S = Secondary, Su = Supporting (per Section 3.2)
- **Use**: Links requirements to controls, enables gap identification (requirements with no mappings)

**Gap Status** (Compliance Gap)

- **Purpose**: Whether requirement is fully satisfied by existing controls
- **Values**:
  - **No Gap**: Requirement fully satisfied by mapped controls
  - **Partial Gap**: Mapped controls provide partial satisfaction, enhancements needed
  - **Complete Gap**: No controls satisfy this requirement, new control(s) needed
- **Drives**: Gap remediation activities (Section 4)

**Notes** (Additional Context)

- **Purpose**: Capture important context, legal nuances, implementation considerations
- **Content**: Free text field for:
  - Legal counsel interpretation notes
  - Dependencies on other requirements
  - Implementation challenges or considerations
  - Clarifications from regulatory guidance
  - Links to regulatory FAQ or enforcement actions

**Extracted By / Date** (Traceability)

- **Purpose**: Who performed extraction and when
- **Content**: Name/role and date
- **Example**: "Compliance Analyst / 2025-01-15"
- **Use**: Quality control, accountability, contact for questions

**Reviewed By / Date** (Quality Control)

- **Purpose**: Who reviewed extraction for accuracy and when
- **Content**: Name/role and date (typically Legal Counsel or senior compliance)
- **Example**: "Legal Counsel / 2025-01-20"
- **Use**: Ensures legal accuracy, secondary verification

**Last Updated / Updated By** (Change Tracking)

- **Purpose**: When requirement entry was last modified and by whom
- **Content**: Date and name/role
- **Use**: Audit trail, version control, identifies stale entries needing review

### Register Maintenance

**Centralized Repository**:
The Requirements Register SHOULD be maintained in a structured, searchable format:

- **Preferred**: Database (enables complex queries, reporting, traceability)
- **Acceptable**: Structured spreadsheet (Excel/LibreOffice with data validation, protected sheets)
- **Location**: Centralized location accessible to all stakeholders with appropriate permissions
- **Tool**: Assessment Workbook 3 provides standardized template

**Access Control**:

- **Read Access**: All ISMS stakeholders, control owners, auditors
- **Write Access (Add/Edit)**: Compliance Officer, Legal Counsel, designated Requirements Analysts
- **Approval Authority**: ISMS Manager, Legal Counsel (for new requirements or changes to Interpreted Requirement field)
- **Administrative Access**: ISMS Manager (for structure changes, archiving)

**Version Control**:

- **Register Version**: Entire register versioned (e.g., v1.0, v1.1, v2.0)
- **Requirement-Level Tracking**: Each requirement tracks its own modification history (Last Updated field)
- **Change Log**: Separate log captures what changed, when, why
  - Example: "v1.1 - 2025-02-15 - Added 12 requirements from amended Data Protection Regulation"
- **Archival**: Previous register versions retained for minimum [X years per retention policy]

**Audit Trail**:
All changes to the register SHALL be logged:

- Date/time of change
- User making change
- Field(s) modified
- Old value → New value
- Reason for change (from Notes or separate change justification)

**Quality Control Process**:
1. **Extraction**: Requirements Analyst extracts requirements per Section 2.1
2. **Legal Review**: Legal Counsel reviews Original Text → Interpreted Requirement translation for accuracy
3. **Approval**: ISMS Manager or Compliance Officer approves addition to register
4. **Publication**: Requirement added to register with "Reviewed By" populated
5. **Periodic Review**: All requirements reviewed annually or when source regulation changes

**Maintenance Triggers**:
Requirements Register SHALL be updated when:

- New regulation identified as applicable (from 5.31.2 process)
- Existing regulation amended (from 5.31.4 regulatory monitoring)
- Regulation repealed or sunsets (requirements archived)
- Organizational scope changes (new requirements become applicable)
- Implementation status changes (requirements move through lifecycle)
- Gap remediation completed (Gap Status updated)
- Control mappings change (Mapped Controls updated)

## Extraction Principles

These principles govern the requirements extraction process to ensure consistency, accuracy, and legal defensibility.

**Principle 1: Completeness**

- Extract ALL mandatory requirements from applicable regulations
- Do not cherry-pick requirements based on ease of implementation
- If requirement exists in regulation, it must exist in register
- Rationale: Regulatory auditors will review entire regulation; gaps in extraction are compliance failures

**Principle 2: Accuracy**

- Interpreted Requirement must be faithful to Original Requirement Text
- Do not add obligations not present in regulatory language
- Do not weaken obligations through interpretation
- Do not change scope or applicability through paraphrasing
- Rationale: Legal defensibility requires faithful representation of regulatory intent

**Principle 3: Clarity**

- Write Interpreted Requirements in clear, jargon-free language
- Target audience: Technical implementers and control owners, not lawyers
- Avoid ambiguous terms ("reasonable", "appropriate" without context)
- Make requirements actionable (specific enough to implement and verify)
- Rationale: Implementers must understand what is required without legal background

**Principle 4: Traceability**

- Every requirement MUST cite source (Regulation ID, Citation)
- Every interpretation MUST preserve original text (Original Requirement Text field)
- Maintain audit trail of extraction and review (Extracted By, Reviewed By)
- Enable reverse lookup (given a control, find all requirements it satisfies)
- Rationale: Auditors will demand proof that extracted requirements match regulatory source

**Principle 5: Consistency**

- Use consistent language across requirements from different regulations
  - Example: If "data at rest" is term used in Requirement 1, use same term in Requirement 2, not "stored data"
- Apply same granularity guidelines across all extractions
- Use same categorization logic for similar requirements
- Rationale: Inconsistency creates confusion, complicates control mapping, appears unprofessional to auditors

**Principle 6: No Interpretation Creep**

- Do not add requirements beyond what regulation mandates
- Example: If regulation says "annual review", do not extract "quarterly review" even if that's better practice
- Separate compliance requirements from organizational best practices
- If [Organization] chooses to exceed regulatory requirements, document separately as organizational policy
- Rationale: Compliance framework must reflect actual obligations, not aspirations

**Principle 7: Legal Review**

- All extractions SHOULD be reviewed by qualified legal counsel
- Legal review confirms:
  - Interpretation is legally accurate
  - No mandatory requirements overlooked
  - No obligations added through interpretation
  - Categorization aligns with regulatory intent
- Document legal review (Reviewed By field)
- Rationale: Requirements extraction has legal implications; legal expertise is essential for accuracy

**Principle 8: Regulatory Context**

- Consider regulation in its entirety, not article-by-article in isolation
- Requirements may reference definitions, exceptions, or procedures elsewhere in regulation
- Interpret requirements in light of regulatory purpose and enforcement guidance
- Consult regulatory FAQ, guidance documents, enforcement actions for clarification
- Rationale: Regulations are holistic instruments; context matters for accurate interpretation

**Principle 9: Update When Regulations Change**

- When regulation is amended, review ALL extracted requirements from that regulation
- Update Interpreted Requirements if regulatory language changed
- Add new requirements if amendments create new obligations
- Archive requirements if provisions repealed
- Rationale: Regulatory landscape evolves; compliance framework must stay current

**Principle 10: Avoid Technology Lock-In**

- Do not extract requirements more prescriptively than regulation mandates
- If regulation says "encryption", do not specify algorithm unless regulation does
- If regulation says "industry-standard", preserve that flexibility
- Allow for technology evolution
- Rationale: Technology changes faster than regulations; overly specific requirements become obsolete

---

# Control Mapping Methodology

## Mapping Approach

Control mapping is the systematic process of identifying which ISO 27001 Annex A controls satisfy extracted regulatory requirements. It establishes the critical link between what regulations require and how [Organization] implements those requirements through security controls.

### The Mapping Challenge

Mapping regulatory requirements to ISO 27001 controls presents several challenges:

**Language Mismatch**:

- Regulations use legal language focused on obligations and penalties
- ISO 27001 uses security management language focused on risk and controls
- Same concept described differently (regulation: "unauthorized access prevention" vs. ISO: "access control")

**Abstraction Level Differences**:

- Regulations may be very specific ("notify within 72 hours") or very general ("appropriate security measures")
- ISO controls are consistently mid-level abstractions (what to do, not specifically how)
- Mapping must bridge these abstraction gaps

**Many-to-Many Relationships**:

- One requirement may need multiple controls to fully satisfy it
- One control may satisfy (partially or fully) multiple requirements
- Overlap and interdependencies between controls

**Lack of Perfect Alignment**:

- ISO 27001 is a general-purpose ISMS standard
- Regulations are specific to jurisdiction, sector, or data type
- Some regulatory requirements may have no direct ISO control equivalent

### The Mapping Question

For each requirement in the Requirements Register, systematically answer:

**"Which ISO 27001 Annex A control(s), when properly implemented, satisfy this requirement?"**

This question has several possible answers:

- **Single primary control**: One control fully satisfies requirement
- **Multiple controls**: Several controls work together to satisfy requirement
- **Partial controls**: Existing controls partially satisfy, gaps remain
- **No existing controls**: Requirement has no Annex A control mapping (requires new organizational control)

### Mapping Philosophy

**Principle: Leverage Existing Controls First**

- Start with ISO 27001 Annex A (93 controls across 4 domains)
- Map requirements to existing controls wherever possible
- Prefer combination of existing controls over creating new controls
- Only create organization-specific controls when no Annex A control(s) fit

**Rationale**:

- ISO 27001 controls are well-defined, industry-standard, auditor-familiar
- Implementing standard controls is easier than designing custom controls
- Leveraging existing controls reduces complexity
- Certification audits focus on Annex A; custom controls require additional justification

**Principle: Accept Many-to-Many Mappings**

- Complex requirements SHOULD map to multiple controls (comprehensive coverage)
- Simple controls SHOULD satisfy multiple requirements (efficiency)
- Do not force one-to-one mappings where many-to-many is more accurate

**Rationale**:

- Security is layered; multiple controls provide defense-in-depth
- Regulations often require comprehensive approaches that single controls cannot satisfy
- Efficient compliance leverages overlap (one control, multiple requirements satisfied)

**Principle: Document Partial Mappings**

- If control partially satisfies requirement, document it as Secondary or Supporting
- Do not claim full satisfaction when gaps exist
- Partial mappings inform gap analysis and remediation

**Rationale**:

- Honesty in mapping enables accurate gap identification
- Partial mappings show progress toward full compliance
- Auditors respect transparency about gaps

## Mapping Types

[Organization] uses a four-level classification system to characterize the relationship between a requirement and a control.

### Primary (P): Direct, Substantial Satisfaction

**Definition**: Control DIRECTLY and SUBSTANTIALLY satisfies the requirement. If this control is properly implemented, the majority of the requirement's obligation is met.

**Characteristics**:

- Control's stated purpose aligns with requirement's intent
- Implementing control achieves compliance with requirement
- Control is the "main" way [Organization] satisfies this requirement
- Evidence of control implementation serves as evidence of requirement compliance

**Example Mappings**:

| Requirement (Interpreted) | Primary Control | Rationale |
|--------------------------|-----------------|-----------|
| "Implement access controls to restrict information access to authorized personnel only" | A.5.15 Access Control | Control directly mandates access restrictions |
| "Encrypt sensitive data at rest" | A.8.24 Use of cryptography | Control specifically addresses cryptographic protection including encryption |
| "Conduct background checks on employees with access to sensitive information" | A.6.1 Screening | Control mandates pre-employment and ongoing screening |
| "Maintain inventory of information assets" | A.5.9 Inventory of information and other associated assets | Control directly requires asset inventory |

**Usage Guidance**:

- Each requirement SHOULD have at least one Primary control (if no Primary, likely a gap)
- Complex requirements may have multiple Primary controls working together
- Primary mappings drive evidence collection (evidence of Primary control = evidence of compliance)

### Secondary (S): Partial or Supporting Satisfaction

**Definition**: Control PARTIALLY satisfies the requirement or SUPPORTS satisfaction but does not fully achieve compliance on its own. Secondary controls work alongside Primary controls to provide comprehensive coverage.

**Characteristics**:

- Control contributes to compliance but is insufficient by itself
- Control addresses one aspect of a multi-faceted requirement
- Control provides technical or procedural support to Primary control
- Multiple Secondary controls may combine with Primary to achieve full compliance

**Example Mappings**:

| Requirement (Interpreted) | Primary Control(s) | Secondary Control(s) | Rationale |
|--------------------------|-------------------|---------------------|-----------|
| "Implement comprehensive security awareness program for all personnel" | A.6.3 Information security awareness, education and training | A.5.2 Information security roles and responsibilities, A.6.2 Terms and conditions of employment | Primary is the awareness program; Secondary controls define who is trained and employment terms requiring training |
| "Ensure secure software development practices" | A.8.25 Secure development lifecycle | A.8.8 Management of technical vulnerabilities, A.8.29 Security testing in development and acceptance | Primary is SDLC; Secondary controls address testing and vulnerability management aspects |
| "Protect against malware across all systems" | A.8.7 Protection against malware | A.8.5 Secure authentication, A.8.19 Installation of software on operational systems | Primary is anti-malware; Secondary controls reduce attack surface that malware exploits |

**Usage Guidance**:

- Secondary mappings show comprehensive approach to complex requirements
- Secondary controls may share implementation burden (different teams implement different controls)
- Evidence from Secondary controls supplements evidence from Primary controls

### Supporting (Su): Indirect Contribution

**Definition**: Control contributes INDIRECTLY to satisfaction of the requirement. Supporting controls create the organizational, procedural, or technical foundation that enables Primary and Secondary controls to function effectively.

**Characteristics**:

- Control is not directly related to requirement's specific mandate
- Control provides background capability, foundation, or enabler
- Absence of Supporting control would not immediately create compliance gap, but would weaken overall security posture related to requirement

**Example Mappings**:

| Requirement (Interpreted) | Primary Control | Secondary Control(s) | Supporting Control(s) | Rationale |
|--------------------------|----------------|---------------------|---------------------|-----------|
| "Implement logging and monitoring of security events" | A.8.15 Logging, A.8.16 Monitoring activities | A.8.11 Data masking | A.5.24 Information security event management, A.5.37 Documented operating procedures | Primary controls log/monitor; Secondary masks sensitive data in logs; Supporting controls govern how incidents are managed and procedures documented |
| "Establish incident response capabilities" | A.5.24 through A.5.28 (Incident Management series) | A.6.8 Information security event reporting | A.5.1 Policies for information security, A.7.7 Clear desk and clear screen | Primaries are incident response; Secondary is reporting; Supporting are foundational policies and physical security |

**Usage Guidance**:

- Supporting mappings are optional (use judgment on whether relationship is meaningful)
- Supporting mappings show holistic approach to compliance
- May be valuable in demonstrating "defense in depth" to auditors
- Do not overuse (risk cluttering mapping matrix with tenuous relationships)

### Not Applicable (N/A): No Relationship

**Definition**: Control has no meaningful relationship to the requirement. The control and requirement address entirely different security objectives.

**Characteristics**:

- Control does not contribute to satisfying requirement
- Implementing control does not advance compliance with requirement
- No logical or technical connection between control and requirement

**Representation in Mapping Matrix**:

- N/A is represented by BLANK cell (cell is empty, no marking)
- Majority of cells in mapping matrix will be blank (93 controls × typically dozens of requirements = thousands of cells, most blank)

**Example Non-Mappings**:

| Requirement | Control That Is N/A | Why N/A |
|-------------|-------------------|---------|
| "Encrypt data at rest" | A.7.2 Physical entry | Physical security does not contribute to encryption requirement |
| "Conduct penetration testing annually" | A.6.4 Disciplinary process | Disciplinary processes unrelated to penetration testing |
| "Notify breaches within 72 hours" | A.5.12 Classification of information | Classification does not help with notification timing |

**Usage Guidance**:

- Do NOT mark every non-relationship as "N/A" in matrix (clutters matrix, default is blank)
- Blank cell = N/A (implicit)
- Focus mapping effort on P, S, Su relationships

## Control Mapping Matrix Structure

The Control Mapping Matrix is the visual representation of requirement-to-control relationships. It provides at-a-glance view of compliance coverage and enables gap identification.

### Matrix Layout

**Rows**: Requirements

- Each row represents one requirement from Requirements Register
- Row identifier: Requirement ID (e.g., REG-DP01-32-001)
- Row label: Interpreted Requirement (abbreviated if needed for space)
- Rows may be grouped by Regulation or by Category for readability

**Columns**: ISO 27001 Annex A Controls

- Each column represents one of 93 Annex A controls
- Column identifier: Control ID (e.g., A.5.1, A.8.24)
- Column label: Control name (abbreviated)
- Columns organized by domain (A.5.x Organizational, A.6.x People, A.7.x Physical, A.8.x Technological)

**Cells**: Mapping Type

- Cell at intersection of Requirement row and Control column contains mapping type
- **Values**: P, S, Su, or blank
  - P = Primary mapping
  - S = Secondary mapping
  - Su = Supporting mapping
  - blank = Not Applicable (no relationship)
- **Formatting** (optional but recommended):
  - P cells highlighted (e.g., bold, colored background)
  - S cells differentiated (e.g., italic)
  - Su cells minimally marked
  - Makes Primary mappings immediately visible

**Example Matrix Snippet**:

| Requirement ID | Requirement | A.5.15 Access Control | A.5.16 Identity Mgmt | A.8.2 Privileged Access | A.8.3 Info Access Restriction | A.8.5 Secure Auth | ... |
|----------------|-------------|----------------------|---------------------|------------------------|------------------------------|------------------|-----|
| REG-DP01-32-001 | Encrypt data at rest | | | | | | ... |
| REG-DP01-32-002 | Implement access controls | **P** | **P** | S | S | S | ... |
| REG-SEC15-4.2-001 | Multi-factor authentication for privileged accounts | | S | **P** | | **P** | ... |

(Note: "**P**" shown in bold to indicate primary mapping emphasis)

### Matrix Benefits

**Visual Gap Identification**:

- Row with no P/S/Su markings = requirement with no control coverage (COMPLETE GAP)
- Row with only S or Su (no P) = requirement with partial coverage (PARTIAL GAP)
- Immediate visual identification of compliance risks

**Control Reuse Analysis**:

- Column with many P/S/Su markings = control satisfies many requirements
- Identifies "high-value" controls for prioritization
- Shows efficiency of control framework

**Regulatory Coverage**:

- Group rows by regulation to see coverage per regulation
- Identify regulations with high gap counts (prioritization)
- Support compliance reporting per regulation

**Change Impact Analysis**:

- If control changes (implementation, scope, removal), scan column to see all affected requirements
- If requirement changes (regulatory amendment), scan row to see all affected controls
- Enables systematic impact assessment (per Section 5.3)

**Audit Support**:

- Provide matrix to auditors as visual representation of compliance approach
- Walk through specific requirements and their control mappings
- Demonstrate systematic, comprehensive approach

### Matrix Maintenance

**Tool**: Assessment Workbook 4 provides standardized Control Mapping Matrix template with:

- Pre-populated 93 Annex A control columns
- Data validation (only P, S, Su, blank allowed)
- Conditional formatting for visual highlighting
- Formulas for gap detection (rows with no Primary)

**Version Control**:

- Matrix versioned alongside Requirements Register
- Changes logged (date, user, cell changed, old value → new value, reason)
- Previous versions archived

**Update Triggers**:
Matrix SHALL be updated when:

- New requirement added to Requirements Register (new row, mappings populated)
- Requirement interpretation changes (review mappings for continued accuracy)
- Control implementation changes (mapping type may change: S → P if control enhanced)
- New control added to ISMS (new column, review all requirements for potential mappings)
- Control removed or deprecated (remove column, identify affected requirements, remap)
- Gap remediation completed (blank → P/S/Su)

**Quality Control**:

- **Completeness Check**: Every requirement has at least one mapping (preferably Primary)
- **Consistency Check**: Similar requirements have similar mapping patterns
- **Accuracy Review**: Legal/Compliance reviews mappings quarterly for continued validity
- **Stakeholder Validation**: Control Owners confirm their controls satisfy mapped requirements

## One-to-Many and Many-to-One Mappings

Real-world compliance scenarios frequently involve complex relationships between requirements and controls. The mapping methodology accommodates these scenarios explicitly.

### One Requirement → Multiple Controls (One-to-Many)

**Scenario**: Single regulatory requirement mandates comprehensive security approach that no single control can satisfy. Multiple controls must work together to achieve compliance.

**When This Occurs**:

- Requirement is complex or multi-faceted
- Requirement spans technical, organizational, and operational domains
- Comprehensive security approach needed

**Example 1: Comprehensive Access Management**

**Requirement** (REG-DP01-32-003): "Implement comprehensive access management ensuring only authorized personnel access sensitive information based on business need, with authentication, authorization, and audit capabilities"

**Control Mappings**:

- **A.5.15 Access Control** (Primary) - Establishes access control policy
- **A.5.16 Identity Management** (Primary) - Manages user identities
- **A.5.17 Authentication Information** (Primary) - Manages credentials
- **A.5.18 Access Rights** (Primary) - Manages authorization
- **A.8.2 Privileged Access Rights** (Secondary) - Manages privileged accounts
- **A.8.3 Information Access Restriction** (Secondary) - Technical access restrictions
- **A.8.5 Secure Authentication** (Secondary) - Authentication mechanisms
- **A.8.15 Logging** (Supporting) - Audit trail of access

**Interpretation**:

- No single control satisfies entire requirement
- All Primary controls must be implemented for full compliance
- Secondary controls enhance access management
- Supporting controls provide audit capability
- Evidence needed from ALL mapped controls

**Example 2: Secure Development Lifecycle**

**Requirement** (REG-SEC15-8.1-002): "Implement secure software development practices including secure coding, testing, vulnerability management, and change control"

**Control Mappings**:

- **A.8.25 Secure Development Lifecycle** (Primary) - SDLC policy and process
- **A.8.28 Secure Coding** (Primary) - Coding standards
- **A.8.29 Security Testing** (Primary) - Testing requirements
- **A.8.8 Management of Technical Vulnerabilities** (Secondary) - Vulnerability remediation
- **A.8.32 Change Management** (Secondary) - Change control
- **A.5.37 Documented Operating Procedures** (Supporting) - Procedures documentation

**Complexity Handling**:

- When requirement maps to many controls (>5), consider:
  - Is requirement too coarse? (Should it be broken into multiple requirements?)
  - Are all mappings truly necessary? (Avoid mapping everything remotely related)
  - Can mappings be grouped? (e.g., all A.8.x technical controls as "primary", all A.5.x organizational as "secondary")

### Multiple Requirements → One Control (Many-to-One)

**Scenario**: Single control, when implemented, satisfies multiple regulatory requirements simultaneously. This is efficiency in action—implement once, comply with multiple regulations.

**When This Occurs**:

- Different regulations require similar security measures
- Control is foundational (many requirements depend on it)
- Overlapping regulatory mandates

**Example 1: Encryption Control**

**Control**: A.8.24 Use of Cryptography

**Satisfies Requirements**:

- REG-DP01-32-001: "Encrypt personal data at rest" (Primary)
- REG-DP01-32-002: "Encrypt personal data in transit" (Primary)
- REG-FIN05-15-003: "Protect payment card data using encryption" (Primary)
- REG-HEALTH-12-001: "Encrypt electronic health records" (Primary)
- REG-SEC15-4.4-002: "Use industry-standard encryption for sensitive data" (Primary)

**Interpretation**:

- One encryption control implementation
- Satisfies requirements from 5 different regulations
- Evidence of encryption implementation (encryption policy, key management procedures, encryption-at-rest configuration, TLS configuration) serves as evidence for all 5 requirements
- Efficiency: Single control, multiple compliance benefits

**Example 2: Logging and Monitoring**

**Control**: A.8.15 Logging

**Satisfies Requirements**:

- REG-DP01-33-001: "Log access to personal data" (Primary)
- REG-FIN05-10-002: "Maintain audit trails of financial transactions" (Primary)
- REG-SEC15-5.2-001: "Log security events for incident detection" (Primary)
- REG-CYBER-Article4-002: "Monitor system activities for anomalies" (Secondary - monitoring uses logs)
- REG-CONTRACT-SLA-003: "Provide access logs to customer upon request" (Primary)

**Interpretation**:

- Centralized logging infrastructure
- Satisfies logging requirements across data protection, financial, security, and contractual regulations
- Comprehensive logging approach benefits multiple compliance needs
- Evidence efficiency (log samples satisfy multiple auditors)

**Benefits of Many-to-One Mappings**:

- **Implementation Efficiency**: Build control once, satisfy multiple requirements
- **Evidence Efficiency**: Collect evidence once, present to multiple audits
- **Maintenance Efficiency**: Update one control, maintain compliance with multiple regulations
- **Cost Efficiency**: Avoid duplicative implementations
- **Consistency**: Same control for similar requirements ensures consistent security posture

**Leveraging Overlaps**:
Section 6 (Handling Overlapping Requirements) provides detailed guidance on identifying and leveraging many-to-one mappings for efficiency.

## Beyond Annex A: Organization-Specific Controls

### When No Annex A Control Fits

Despite 93 controls covering comprehensive ISMS scope, regulatory requirements occasionally demand capabilities not addressed by any Annex A control.

**Situations Requiring Organization-Specific Controls**:

**Sector-Specific Technical Requirements**:

- Financial services: "Implement transaction monitoring for fraud detection"
  - No direct Annex A control for fraud detection systems
  - A.8.16 Monitoring activities is related but not specific to fraud
- Healthcare: "Implement break-the-glass access for medical emergencies"
  - Emergency access override is sector-specific
  - A.5.18 Access rights covers access but not emergency override

**Jurisdiction-Specific Reporting**:

- "File annual cybersecurity attestation with Regulator X by March 31"
  - Annex A has no control for regulatory filing processes
  - This is pure compliance process, not security control

**Contractual Obligations**:

- "Provide customer with monthly security metrics dashboard per SLA Section 12"
  - Customer-specific reporting is contractual, not covered by Annex A
  - A.5.31 addresses regulatory requirements generally but not specific customer reporting

**Emerging Threats/Technologies**:

- "Implement AI model bias testing and monitoring"
  - AI-specific controls not in ISO 27001:2022
  - Emerging regulatory requirements may outpace standard updates

### Creating Organization-Specific Controls

When gap analysis (Section 4) identifies requirements with no Annex A mapping, [Organization] SHALL create organization-specific controls following this methodology:

**Step 1: Verify Gap**

- Confirm that NO Annex A control, even partially, addresses requirement
- Consult with ISMS Manager, Control Owners, Legal to verify
- Document justification for new control (why Annex A insufficient)

**Step 2: Define Control**

- **Control ID**: CTRL-ORG-[Domain]-[Sequence]
  - Domain: ORG (Organizational), PEO (People), PHY (Physical), TEC (Technological)
  - Sequence: 001, 002, 003, etc.
  - Example: CTRL-ORG-TEC-001 (first organizational technological control)
- **Control Name**: Clear, concise description
  - Example: "Fraud Detection and Transaction Monitoring"
- **Control Objective**: Why this control exists
  - Example: "Detect and prevent fraudulent financial transactions in real-time"
- **Control Description**: What the control does
  - Example: "Implement automated transaction monitoring system that analyzes financial transactions against fraud indicators, alerts on suspicious activity, and enables investigation and response"

**Step 3: Specify Implementation**

- **Implementation Guidance**: How to implement control
  - Technical specifications
  - Organizational procedures
  - Roles and responsibilities
- **Evidence Requirements**: How to demonstrate control effectiveness
  - Documentation required
  - Logs, reports, configurations
  - Audit/review frequency

**Step 4: Assign Ownership**

- **Control Owner**: Who implements and maintains control
- **Approval**: Executive Management approval for new control (adds to ISMS scope and cost)

**Step 5: Integrate with ISMS**

- Add to Statement of Applicability (SoA) if pursuing certification
  - Document in SoA that this is organization-specific control beyond Annex A
  - Provide justification (regulatory requirement XYZ mandates this)
- Add to Control Mapping Matrix (new column for CTRL-ORG-TEC-001)
- Map requirement(s) to new control (Primary mapping)
- Include in Internal Audit scope
- Include in Management Review

**Step 6: Document in Organizational Controls Register**

- Maintain separate register of organization-specific controls
- Link to regulatory requirements driving creation
- Track implementation status, evidence, audits

**Example: Organization-Specific Control**

**Requirement**: REG-FIN05-23-005: "Implement real-time fraud detection for all payment card transactions with automated alerts for suspicious patterns"

**Gap Analysis**: 

- A.8.16 Monitoring activities is too general
- A.8.7 Protection against malware addresses different threat
- No Annex A control specifically addresses fraud detection
- **Gap Type**: Complete gap, new control needed

**Organization-Specific Control Created**:

- **Control ID**: CTRL-ORG-TEC-001
- **Control Name**: Fraud Detection and Transaction Monitoring
- **Control Objective**: Detect and prevent payment card fraud in real-time to protect customers and satisfy regulatory requirements
- **Control Description**: 
  - Deploy real-time transaction monitoring system analyzing all payment card transactions
  - System compares transactions against fraud indicators (unusual amounts, geographic anomalies, velocity patterns, device fingerprinting)
  - Automated alerts generated for high-risk transactions (>threshold score)
  - Security Operations team investigates alerts within 15 minutes
  - Fraudulent transactions blocked, cardholders notified
- **Implementation Guidance**:
  - Procurement: Select fraud detection platform meeting requirements
  - Configuration: Define fraud rules, thresholds, alert routing
  - Integration: API integration with payment processing systems
  - Training: SOC analysts trained on fraud alert triage
  - Procedures: Document investigation and response procedures
- **Evidence Requirements**:
  - Fraud detection system configuration documentation
  - Monitoring dashboard showing transaction analysis
  - Alert logs (date, time, transaction, risk score, analyst action)
  - Monthly fraud detection metrics (transactions analyzed, alerts generated, fraud prevented)
  - Annual testing of fraud detection rules
- **Control Owner**: Chief Information Security Officer
- **Mapped Requirements**: REG-FIN05-23-005 (Primary)

### Governance of Organization-Specific Controls

**Approval Process**:

- New organization-specific controls require Executive Management approval
- Justification documented (regulatory requirement, business need, risk mitigation)
- Cost-benefit analysis (implementation cost vs. regulatory penalty/risk)

**Review Cycle**:

- Organization-specific controls reviewed annually
- Verify continued need (has regulation changed? has Annex A added relevant control in newer version?)
- Assess effectiveness (is control achieving objective?)
- Update or retire controls as needed

**Integration with Certification**:

- ISO 27001 certification audits will review organization-specific controls
- Auditor will assess:
  - Is control necessary? (justified by regulatory requirement or risk assessment)
  - Is control properly designed? (effective at achieving objective)
  - Is control implemented? (evidence of operation)
  - Is control maintained? (ongoing operation, not one-time)
- Document in Statement of Applicability with clear justification

**Limitation**:

- Avoid proliferation of organization-specific controls
- Prefer enhancement of Annex A controls over creating new controls
- Only create when truly necessary
- Too many organization-specific controls suggests:
  - Misunderstanding of Annex A (controls are flexible, can be tailored)
  - Over-interpretation of requirements (extracting too prescriptively)
  - Opportunity to influence standard bodies (propose new controls for future ISO versions)

---

# Gap Analysis Process

Gap analysis is the systematic identification of regulatory requirements that are not fully satisfied by existing or planned controls. It is the critical "reality check" that answers: "Where are we non-compliant?"

## Gap Identification

### Types of Gaps

**Complete Gaps**:

- **Definition**: Requirement has NO control mapped to it (no P, S, or Su mappings in Control Mapping Matrix)
- **Severity**: Critical - represents total non-compliance with requirement
- **Identification**: Requirement row in matrix is completely blank (no markings in any control column)
- **Example**:
  - Requirement: "Notify supervisory authority of data breaches within 72 hours"
  - Current Controls: [Organization] has incident response procedures (A.5.24-A.5.28) but no specific breach notification process for regulatory authority
  - Gap: No control governs 72-hour notification requirement
  - Remediation Needed: Create notification procedure as part of incident management

**Partial Gaps**:

- **Definition**: Requirement has Secondary or Supporting mappings but NO Primary mapping, OR Primary mapping exists but control only partially implements requirement
- **Severity**: High - partial compliance, but significant gaps remain
- **Identification**: 
  - Matrix row has S or Su markings but no P marking, OR
  - Control Owner assessment indicates control doesn't fully satisfy requirement
- **Example 1** (No Primary):
  - Requirement: "Conduct penetration testing of all internet-facing systems annually"
  - Current Controls: A.8.8 Management of Technical Vulnerabilities (Secondary - vulnerability scanning, not pen testing)
  - Gap: No control mandates penetration testing specifically
  - Remediation Needed: Enhance A.8.8 to include penetration testing or create new organizational procedure
- **Example 2** (Incomplete Primary):
  - Requirement: "Encrypt all sensitive data at rest and in transit"
  - Current Control: A.8.24 Use of Cryptography (Primary)
  - Current State: Encryption at rest implemented, encryption in transit partial (some legacy systems use unencrypted protocols)
  - Gap: Partial implementation of control
  - Remediation Needed: Complete implementation (upgrade legacy systems to use TLS)

**Implementation Gaps**:

- **Definition**: Requirement is mapped to appropriate control (Primary mapping exists), but control is not yet implemented or is implemented inadequately
- **Severity**: Varies (High if deadline approaching, Medium otherwise)
- **Identification**: 
  - Requirements Register shows Implementation Status = "Not Started" or "In Progress"
  - Control Maturity Assessment indicates control is immature (Level 0-1 on maturity scale)
  - Recent audit findings indicate control deficiencies
- **Example**:
  - Requirement: "Conduct security awareness training for all employees annually"
  - Mapped Control: A.6.3 Information security awareness, education and training (Primary)
  - Current State: Policy exists but training not delivered consistently, no tracking
  - Gap: Control defined but not effectively implemented
  - Remediation Needed: Implement training program, establish tracking, ensure annual delivery

### Gap Identification Process

**Step 1: Control Mapping Matrix Analysis**

- Review completed Control Mapping Matrix
- Identify rows (requirements) with no Primary mappings → Complete or Partial gaps
- For each requirement, assess:
  - Does it have Primary mapping? (If no → gap)
  - Do Secondary/Supporting mappings partially cover? (If yes → partial gap; if no → complete gap)
  - Is mapping accurate? (Sometimes gap is mismapping, not actual lack of control)

**Step 2: Control Implementation Review**

- For requirements with Primary mappings, verify control implementation status
- Sources:
  - Requirements Register "Implementation Status" field
  - Internal audit reports
  - Control effectiveness assessments
  - Control Owner confirmations
- Identify Implementation gaps (mapped but not implemented or implemented inadequately)

**Step 3: Evidence Verification**

- For requirements marked "Implemented", verify evidence exists
- Can [Organization] demonstrate compliance through documentation, logs, reports?
- If evidence is lacking or inadequate → Evidence gap (related to implementation gap)

**Step 4: Stakeholder Consultation**

- **Legal Counsel**: Confirm gap interpretation is legally accurate
  - "We believe Requirement X is not satisfied by Control Y - do you concur?"
- **Control Owners**: Confirm controls cannot satisfy requirement
  - "Your control A.8.15 is mapped to Requirement Z - does your control fully satisfy this requirement?"
- **Compliance Officer**: Prioritize gaps based on regulatory risk

**Step 5: Gap Documentation**

- Document ALL identified gaps in Gap Register
- Gap Register fields:
  - Gap ID (unique identifier)
  - Requirement ID (which requirement is not satisfied)
  - Gap Type (Complete, Partial, Implementation)
  - Gap Description (what is missing)
  - Risk/Impact (consequence of non-compliance)
  - Priority (High/Medium/Low per Section 4.2)
  - Remediation Plan (how gap will be closed)
  - Responsible Party (who will remediate)
  - Target Date (when gap will be closed)
  - Status (Open, In Progress, Closed)

## Gap Prioritization

Not all gaps are equally urgent. Prioritization ensures [Organization] addresses highest-risk gaps first with limited resources.

### Prioritization Factors

**Factor 1: Regulatory Tier** (from ISMS-POL-00)

- **Tier 1 Mandatory**: Highest priority (legal obligation, direct enforcement)
- **Tier 2 Conditional**: High priority if condition met (e.g., if processing payment cards, PCI DSS gaps are high priority)
- **Tier 3 Informational**: Lower priority (best practice, not legally mandated)

**Factor 2: Legal Consequence Severity**

- **Criminal/Severe Fines**: Highest priority
  - Example: GDPR breaches can result in fines up to 4% of global turnover or €20M
- **Civil Penalties/Moderate Fines**: High priority
- **Reputational Damage**: Medium-High priority (customer trust, brand impact)
- **Minor Penalties/Warnings**: Lower priority

**Factor 3: Compliance Deadline**

- **Immediate** (deadline passed or <30 days): Highest priority (already non-compliant)
- **Near-term** (30-90 days): High priority (urgent remediation needed)
- **Medium-term** (90 days - 1 year): Medium priority (planned remediation)
- **Long-term** (>1 year): Lower priority (strategic planning)

**Factor 4: Implementation Complexity**

- **Quick Wins** (low complexity, high impact): Prioritize for immediate action
- **Complex, High-Impact**: Prioritize but plan carefully (may need phased approach)
- **Simple, Low-Impact**: Batch with other similar gaps
- **Complex, Low-Impact**: Defer or accept risk

**Factor 5: Business Impact**

- **Customer-Facing**: Higher priority (SLA commitments, customer trust)
- **Internal**: May be lower priority
- **Revenue-Critical**: Highest priority (blocks business if non-compliant)
- **Non-Critical**: Lower priority

### Prioritization Matrix

Combine factors into prioritization decision:

**Priority: CRITICAL** (Immediate Action Required)

- Complete or Partial gap in Tier 1 regulation
- Deadline passed or <30 days away
- Severe legal consequence (criminal liability, major fines)
- Affects revenue-critical business operations

**Priority: HIGH** (Urgent, Plan Remediation)

- Complete or Partial gap in Tier 1 regulation
- Deadline 30-90 days
- Significant legal consequence (civil penalties, moderate fines)
- Customer-facing or contractually committed

**Priority: MEDIUM** (Plan and Execute)

- Partial gap in Tier 1, or Complete gap in Tier 2 (if applicable)
- Deadline 90 days - 1 year
- Moderate legal consequence or reputational risk
- Internal operations

**Priority: LOW** (Strategic Planning)

- Implementation gap only (control defined, implementation in progress)
- Gap in Tier 3 (informational/best practice)
- Deadline >1 year
- Minor or no legal consequence
- Non-critical operations

**Example Prioritizations**:

| Gap Description | Reg Tier | Deadline | Consequence | Complexity | Priority | Rationale |
|-----------------|----------|----------|-------------|------------|----------|-----------|
| No breach notification process for 72hr requirement | Tier 1 | 30 days | Major fines (GDPR) | Low | CRITICAL | Tier 1, imminent deadline, severe penalty |
| Partial encryption implementation (data at rest only) | Tier 1 | 90 days | Moderate fines | Medium | HIGH | Tier 1, partial gap, medium-term deadline |
| No penetration testing program | Tier 2 (PCI DSS applies) | 6 months | Lose ability to process cards | High | HIGH | Tier 2 but business-critical, sufficient time to plan |
| Security awareness training inconsistent | Tier 1 | No specific deadline | Minor (policy violation) | Low | MEDIUM | Implementation gap, low complexity, no deadline pressure |
| No AI bias testing procedure | Tier 3 (NIST AI guidance) | None | Reputational | High | LOW | Informational only, complex, no legal mandate yet |

## Gap Remediation Approaches

For each identified gap, [Organization] SHALL determine and execute an appropriate remediation approach.

### Remediation Options

**Option 1: Implement New Control**

- **When**: Complete gap, no existing control addresses requirement
- **Action**: Create and implement organization-specific control (per Section 3.5)
- **Process**:

  1. Define new control (control ID, name, description, objective)
  2. Assign Control Owner
  3. Implement control (technical, organizational, procedural)
  4. Document implementation
  5. Collect evidence
  6. Update Control Mapping Matrix (add column for new control, mark requirement as Primary)
  7. Update Gap Register (gap closed)

- **Example**: No control for breach notification → Create CTRL-ORG-ORG-003 "Regulatory Breach Notification Process"

**Option 2: Enhance Existing Control**

- **When**: Partial gap, existing control is close but incomplete
- **Action**: Expand scope, add capabilities, or improve implementation of existing control
- **Process**:

  1. Identify control needing enhancement
  2. Define what enhancements needed (additional procedures, technical capabilities, scope expansion)
  3. Control Owner implements enhancements
  4. Document enhancements in control description
  5. Update evidence to reflect enhanced control
  6. Update Control Mapping Matrix (potentially upgrade Secondary → Primary if enhancement addresses gap)
  7. Update Gap Register (gap closed)

- **Example**: A.8.8 Management of Technical Vulnerabilities includes scanning but not penetration testing → Enhance A.8.8 to include annual penetration testing requirement

**Option 3: Implement Combination of Controls**

- **When**: Complex requirement needs multiple controls working together
- **Action**: Implement several controls (existing Annex A or new organizational) that collectively satisfy requirement
- **Process**:

  1. Identify which controls needed (may be mix of Annex A and organizational)
  2. Assign owners (may be different owners for different controls)
  3. Coordinate implementation (controls must work together)
  4. Document how combination satisfies requirement
  5. Collect evidence from each control
  6. Update Control Mapping Matrix (multiple Primary or Secondary mappings)
  7. Update Gap Register (gap closed)

- **Example**: "Comprehensive access management" requires A.5.15 + A.5.16 + A.5.17 + A.5.18 working together

**Option 4: Implement Compensating Control**

- **When**: Ideal control cannot be implemented (technical, cost, operational constraints) but alternative approach achieves same objective
- **Action**: Implement different control that compensates for gap
- **Process**:

  1. Document why ideal control cannot be implemented (justification)
  2. Identify compensating control that achieves same security objective
  3. Document compensating control rationale (how it achieves requirement)
  4. Obtain Legal Counsel and Management approval (compensating controls are risk decisions)
  5. Implement compensating control
  6. Document in Control Mapping Matrix with annotation (e.g., "A.8.X (P) - Compensating control for Requirement Y")
  7. Update Gap Register (gap closed with compensating control)

- **Example**: Requirement mandates biometric authentication, but biometric system cost-prohibitive → Compensate with MFA using hardware tokens + behavioral analytics
- **Caution**: Regulators/auditors may challenge compensating controls; strong justification and evidence of effectiveness required

**Option 5: Accept Risk**

- **When**: Gap exists but implementation cost/complexity exceeds risk, OR gap is Low priority and resources limited
- **Action**: Formally accept risk, document rationale, obtain management approval
- **Process**:

  1. Conduct risk assessment (likelihood and impact of non-compliance)
  2. Document rationale for accepting risk (cost, technical infeasibility, low priority)
  3. Obtain Executive Management approval (risk acceptance is executive decision)
  4. Document in Risk Register
  5. Monitor for changes (if regulatory enforcement increases, reassess)
  6. Update Gap Register (gap remains open but risk accepted)

- **Example**: Tier 3 informational best practice, cost to implement exceeds benefit, executive approves risk acceptance
- **Restrictions**: 
  - CANNOT accept risk for Tier 1 Mandatory requirements (legal obligation)
  - SHOULD NOT accept risk for High priority gaps
  - MUST revisit risk acceptance if circumstances change (regulation amended, business changes, enforcement increases)

### Remediation Planning

For each gap remediation:

**Develop Remediation Plan**:

- Gap ID and description
- Chosen remediation approach (New Control, Enhancement, Combination, Compensating, Accept Risk)
- Detailed implementation steps
- Responsible party (Control Owner or project team)
- Resources required (budget, staff, technology)
- Timeline (start date, milestones, completion date)
- Dependencies (on other projects, vendor delivery, etc.)
- Success criteria (how will we know remediation is complete?)

**Obtain Approval**:

- Control Owner approves remediation plan
- ISMS Manager/Compliance Officer approves
- Executive Management approves (for significant investments or risk acceptances)

**Execute Plan**:

- Implement according to plan
- Track progress (milestones, status updates)
- Adjust as needed (plans may need revision based on implementation realities)

**Verify Closure**:

- Test implemented control (does it work as intended?)
- Collect evidence (can we demonstrate control effectiveness?)
- Re-assess requirement (is it now satisfied?)
- Update Control Mapping Matrix (add or update mappings)
- Update Gap Register (status: Closed)
- Internal audit validation (independent verification)

## Gap Tracking

### Gap Register

[Organization] SHALL maintain a Gap Register documenting all identified compliance gaps and their remediation status.

**Gap Register Fields**:

- **Gap ID**: Unique identifier (GAP-YYYY-###)
- **Identification Date**: When gap identified
- **Requirement ID**: Which requirement not satisfied
- **Regulation Name**: Parent regulation
- **Gap Type**: Complete, Partial, Implementation
- **Gap Description**: What is missing (clear, specific)
- **Current Control(s)**: Existing controls (if partial gap)
- **Risk/Impact**: Consequence of non-compliance
- **Priority**: Critical/High/Medium/Low (per Section 4.2)
- **Remediation Approach**: New Control, Enhancement, Combination, Compensating, Accept Risk
- **Remediation Plan**: Summary or link to detailed plan
- **Responsible Party**: Who owns remediation
- **Target Closure Date**: When gap will be closed
- **Status**: Open, In Progress, Pending Approval, Closed, Risk Accepted
- **Actual Closure Date**: When gap actually closed (blank if open)
- **Verification**: How closure verified (audit, test, evidence review)
- **Notes**: Additional context

**Tool**: Maintained in centralized register (spreadsheet or compliance management system)

### Gap Management Process

**Quarterly Gap Review**:

- ISMS Manager, Compliance Officer, Legal Counsel review Gap Register
- Assess progress on remediation plans
- Re-prioritize gaps if circumstances changed
- Identify overdue remediations, escalate as needed
- Report gap status to Executive Management

**Management Review Integration**:

- Gap metrics reported in ISO 27001 Management Review (Clause 9.3)
- Metrics: Total gaps, gaps by priority, gaps closed this period, overdue gaps
- Trends: Increasing/decreasing gap counts, aging gaps
- Executive decisions on resource allocation, risk acceptances

**Gap Metrics and KPIs**:

- **Total Open Gaps** (count by priority)
- **Mean Time to Close Gaps** (by priority)
- **Gap Aging** (gaps open >90 days, >180 days, >1 year)
- **Gap Closure Rate** (gaps closed per month/quarter)
- **Percentage of Requirements Satisfied** (requirements with Primary mapping / total requirements)

**Continuous Improvement**:

- Root cause analysis: Why did gap exist? (new regulation, oversight in initial implementation, requirement creep)
- Process improvement: How can we prevent similar gaps? (better initial gap analysis, earlier regulatory monitoring, more frequent assessments)

---

# Traceability Requirements

Traceability is the ability to trace relationships between regulations, requirements, controls, and evidence in both forward and reverse directions. It is fundamental to audit readiness and compliance demonstration.

## Forward Traceability

### The Forward Traceability Chain

**Definition**: Forward traceability is the ability to start with a regulation and trace through to the evidence that demonstrates compliance.

**The Forward Chain**:
```
Regulation (in ISMS-POL-00)
    ↓
Extracted Requirements (in Requirements Register)
    ↓
Mapped Controls (in Control Mapping Matrix)
    ↓
Implemented Controls (in control documentation, policies, procedures)
    ↓
Collected Evidence (in Evidence Register and repository)
```

**Example Forward Trace**:

**Starting Point**: Data Protection Regulation Article 32 ("Security of Processing")

**Step 1**: Identify in ISMS-POL-00

- Regulation ID: REG-DP01
- Tier: 1 - Mandatory
- Status: Applicable

**Step 2**: Find Extracted Requirements in Requirements Register

- REG-DP01-32-001: "Implement encryption for personal data at rest and in transit"
- REG-DP01-32-002: "Implement access controls to restrict personal data access to authorized personnel"
- REG-DP01-32-003: "Conduct regular testing and evaluation of security measures"
- [... additional requirements from Article 32]

**Step 3**: Identify Mapped Controls in Control Mapping Matrix

- REG-DP01-32-001 maps to:
  - A.8.24 Use of Cryptography (Primary)
- REG-DP01-32-002 maps to:
  - A.5.15 Access Control (Primary)
  - A.5.16 Identity Management (Primary)
  - A.5.18 Access Rights (Primary)
- REG-DP01-32-003 maps to:
  - A.5.36 Compliance with policies, rules and standards (Primary)
  - A.8.8 Management of Technical Vulnerabilities (Secondary - for technical testing)

**Step 4**: Review Implemented Controls

- A.8.24: Encryption Policy v2.1, Key Management Procedures
- A.5.15: Access Control Policy v3.0
- A.5.16: Identity Management Standard
- A.5.18: Access Rights Provisioning Procedure
- A.5.36: Compliance Monitoring Procedure
- A.8.8: Vulnerability Management Policy, Penetration Testing Standard

**Step 5**: Locate Evidence

- A.8.24 Evidence:
  - Encryption-at-rest configuration (database encryption enabled, full-disk encryption)
  - TLS configuration (TLS 1.3 enforced on all web services)
  - Key management audit logs (key rotation quarterly)
- A.5.15/16/18 Evidence:
  - Access control matrix (roles and permissions)
  - Access request/approval logs
  - Quarterly access review reports
- A.5.36/A.8.8 Evidence:
  - Annual penetration test report
  - Quarterly vulnerability scan results
  - Remediation tracking for identified vulnerabilities

**Outcome**: Can demonstrate to auditor: "Here's the regulation, here are the requirements we extracted, here are the controls we implemented, and here is the evidence proving they're working."

### Why Forward Traceability Matters

**Audit Readiness**:

- Auditor asks: "Show me how you comply with Regulation Article 32"
- [Organization] provides the forward trace above
- Demonstrates systematic approach, not ad-hoc compliance

**Regulatory Inquiries**:

- Regulator requests compliance demonstration
- Forward trace provides complete answer
- Shows comprehensive approach

**Executive Reporting**:

- Management asks: "Are we compliant with Data Protection Regulation?"
- Follow forward trace for ALL requirements from that regulation
- Report compliance status (% satisfied, gaps, evidence available)

**Gap Identification**:

- Forward trace breaks if requirement has no control mapping (gap)
- Forward trace incomplete if control implemented but no evidence (implementation or evidence gap)

## Reverse Traceability

### The Reverse Traceability Chain

**Definition**: Reverse traceability is the ability to start with evidence (or a control) and trace back to the regulation(s) it satisfies.

**The Reverse Chain**:
```
Evidence (in Evidence Register and repository)
    ↓
Implemented Control (documented in policies, procedures)
    ↓
Mapped Requirements (in Control Mapping Matrix)
    ↓
Source Regulation (in ISMS-POL-00)
```

**Example Reverse Trace**:

**Starting Point**: Encryption Policy document (v2.1)

**Step 1**: Identify as Evidence for Control

- Control: A.8.24 Use of Cryptography
- Evidence Type: Policy document
- Evidence Location: Policy Repository / Encryption Policy v2.1.pdf

**Step 2**: Find Control in Control Mapping Matrix

- A.8.24 column in matrix shows mappings to multiple requirements:
  - REG-DP01-32-001 (Primary) - Data Protection Regulation
  - REG-FIN05-15-003 (Primary) - Financial Regulation
  - REG-HEALTH-12-001 (Primary) - Healthcare Regulation
  - REG-SEC15-4.4-002 (Primary) - Security Standard

**Step 3**: Trace Requirements Back to Regulations

- REG-DP01-32-001 → Data Protection Regulation Article 32
- REG-FIN05-15-003 → Financial Regulation Section 15
- REG-HEALTH-12-001 → Healthcare Data Security Law Article 12
- REG-SEC15-4.4-002 → Security Standard Section 4.4

**Outcome**: Single encryption policy satisfies requirements from FOUR different regulations. Efficiency through reuse.

### Why Reverse Traceability Matters

**Evidence Efficiency**:

- Know which evidence satisfies which requirements
- Avoid collecting duplicate evidence for overlapping requirements
- One evidence artifact, multiple compliance uses

**Control Justification**:

- Explain WHY control exists (which regulations mandate it)
- Defend security investments (these controls are legally required, not optional)
- Prioritize control improvements (controls satisfying multiple Tier 1 regulations are high priority)

**Impact Analysis for Control Changes**:

- If control is modified or removed, immediately identify affected requirements
- Assess regulatory impact before making changes
- Prevent accidental non-compliance

**Audit Efficiency**:

- When auditor reviews evidence, quickly identify all regulations it satisfies
- Present evidence once, satisfy multiple audit needs
- Demonstrate comprehensive approach (this evidence serves X, Y, Z regulations)

## Change Traceability

### Types of Changes Requiring Traceability

**Regulation Changes**:

- Regulation amended (new articles added, existing articles modified, articles repealed)
- New regulation becomes applicable
- Regulation repealed or sunsets

**Control Changes**:

- Control implementation modified (technical changes, scope changes)
- Control enhanced or expanded
- Control deprecated or removed
- New control added

**Organizational Changes**:

- Business expansion (new services, new geographic markets, new customer types)
- Mergers and acquisitions
- Outsourcing or insourcing of services
- Technology changes (cloud migration, new platforms)

### Change Impact Analysis Using Traceability

**When Regulation Changes**:

**Process**:
1. Identify changed regulation in ISMS-POL-00
2. Use forward traceability to find all requirements extracted from that regulation (Requirements Register)
3. Review changed regulatory text

   - Are existing requirements still accurate? (Update interpreted requirement if needed)
   - Are new requirements created? (Extract and add to register)
   - Are existing requirements obsolete? (Archive if article repealed)

4. Re-assess control mappings for affected requirements

   - Do current mappings still satisfy updated requirements?
   - Are new controls needed for new requirements?

5. Update evidence if requirement or control mappings changed
6. Communicate changes to stakeholders (per Section 5.31.4 - covered in Change Management policy)

**Example**:

- Data Protection Regulation Article 32 amended to require "encryption using post-quantum cryptographic algorithms within 2 years"
- Forward trace finds REG-DP01-32-001 ("Implement encryption for personal data")
- Update interpreted requirement to include post-quantum requirement
- Assess A.8.24 (Use of Cryptography): Current implementation uses classical algorithms (AES, RSA)
- Identify gap: Need to plan migration to post-quantum algorithms
- Add to Gap Register with 2-year deadline
- Update roadmap for post-quantum crypto implementation

**When Control Changes**:

**Process**:
1. Identify control being changed (Control ID)
2. Use reverse traceability to find all requirements that map to this control (Control Mapping Matrix column)
3. Assess impact of change on each mapped requirement:

   - Does change improve satisfaction? (Partial gap → no gap)
   - Does change reduce satisfaction? (Previously satisfied → now gap)
   - Does change not affect requirement satisfaction?

4. Update Control Mapping Matrix if mapping types change
5. Update Gap Register if gaps created or closed
6. Update evidence if control change affects evidence type or collection
7. Communicate to stakeholders, especially if gaps created

**Example**:

- A.8.15 (Logging) implementation changed: Reduced log retention from 2 years to 6 months due to storage costs
- Reverse trace finds requirements mapped to A.8.15:
  - REG-DP01-33-001: "Retain logs for 1 year minimum" (Primary mapping)
  - REG-FIN05-10-002: "Retain financial transaction logs for 7 years" (Primary mapping)
- Impact assessment:
  - REG-DP01-33-001: 6 months retention does NOT satisfy 1-year requirement → GAP CREATED
  - REG-FIN05-10-002: 6 months retention does NOT satisfy 7-year requirement → GAP CREATED
- Decision: REVERT control change (cannot reduce retention) OR implement differential retention (financial logs kept 7 years, other logs 6 months)
- Demonstrates value of change traceability: prevented non-compliance

**When Organization Changes**:

**Process**:
1. Identify nature of change (new service, new market, acquisition, etc.)
2. Trigger applicability re-assessment (per 5.31.2 methodology)

   - New regulations may become applicable
   - Existing regulations may no longer apply

3. If new regulations applicable:

   - Extract requirements (per Section 2)
   - Map to controls (per Section 3)
   - Identify gaps (per Section 4)
   - Plan remediation

4. If regulations no longer applicable:

   - Archive requirements from those regulations
   - Retain controls if they serve other purposes (other regulations, business risk management)
   - Update Control Mapping Matrix

5. Communicate regulatory landscape changes to stakeholders

**Example**:

- [Organization] acquires company that processes payment cards → PCI DSS now applicable (Tier 2 Conditional → Tier 1 Mandatory because condition met)
- Trigger applicability re-assessment: PCI DSS is now Tier 1
- Extract PCI DSS requirements (all 12 requirement categories → dozens of specific requirements)
- Map to existing controls: Some controls already satisfy (encryption, access control), many gaps identified
- Prioritize PCI gaps as HIGH (now mandatory, customer card processing depends on compliance)
- Develop PCI remediation roadmap

### Tools for Change Traceability

**Requirements Register Linking**:

- Regulation ID field links to ISMS-POL-00
- When POL-00 updated (regulation changed), Requirements Register flagged for review

**Control Mapping Matrix Bidirectionality**:

- Matrix enables both forward (requirement → controls) and reverse (control → requirements) trace
- Any cell change propagates impact in both directions

**Change Log Integration**:

- Requirements Register tracks changes (Last Updated field)
- Control Mapping Matrix tracks changes (version history)
- Cross-reference change logs to identify related changes
  - Example: If Regulation X amended on 2025-03-15, Requirements Register should show updates around same date

**Automated Alerts** (if using compliance management software):

- Alert when regulation in POL-00 marked as "Under Review" or "Changed" → Trigger requirements review
- Alert when control implementation status changes → Trigger mapping review
- Alert when requirement Implementation Deadline approaching → Trigger gap remediation

## Audit Trail

Every change in the regulatory compliance framework SHALL be logged to create a complete, auditable history.

### What to Log

**Requirements Register Changes**:

- New requirement added (who, when, from which regulation)
- Requirement interpretation modified (old interpretation → new interpretation, who, when, why)
- Requirement status changed (implementation status, gap status)
- Requirement archived (which requirement, when, why no longer applicable)

**Control Mapping Matrix Changes**:

- New mapping created (requirement X → control Y, mapping type P/S/Su, who, when)
- Mapping type changed (S → P because control enhanced, who, when)
- Mapping removed (requirement no longer maps to control, who, when, why)

**Gap Register Changes**:

- Gap identified (gap ID, description, priority, who identified, when)
- Gap priority changed (re-prioritization rationale)
- Gap remediation plan updated (plan changes, timeline adjustments)
- Gap status changed (Open → In Progress → Closed)
- Gap closure (how closed, verification method, who verified, when)

**Evidence Changes**:

- New evidence collected (what evidence, for which control/requirement)
- Evidence updated (evidence refresh, new version)
- Evidence verification (who verified, when, verification outcome)

### Where Logs Are Maintained

**Within Documents/Registers**:

- **Requirements Register**: 
  - "Last Updated" and "Updated By" fields per requirement
  - Register-level version history table
  - Change log tab/section documenting all changes
- **Control Mapping Matrix**:
  - Matrix-level version history
  - Cell change tracking (if using software with change tracking)
  - Separate change log documenting mapping changes
- **Gap Register**:
  - Status history per gap (Open → In Progress → Closed with dates)
  - Notes field capturing decisions and rationale
- **Evidence Register**:
  - Evidence verification dates and verifiers
  - Evidence refresh/update history

**Centralized Compliance Log** (Optional but Recommended):

- Single log capturing ALL compliance framework changes
- Chronological record across all documents
- Useful for management review, audits, forensic analysis
- Fields:
  - Date/Time
  - Document/Register affected
  - Change type (Add, Modify, Delete, Status Change)
  - Change description
  - User making change
  - Approval (if applicable)
  - Rationale

**Example Centralized Log Entries**:

| Date | Document | Change Type | Description | User | Rationale |
|------|----------|-------------|-------------|------|-----------|
| 2025-01-15 | Requirements Register | Add | Added REG-DP01-32-004 (DPIA requirement) | Compliance Analyst | New requirement from DP Regulation guidance |
| 2025-01-20 | Mapping Matrix | Modify | REG-FIN05-23-005 mapping to CTRL-ORG-TEC-001 changed S → P | ISMS Manager | Fraud detection system fully implemented |
| 2025-02-01 | Gap Register | Status Change | GAP-2025-003 status changed Open → Closed | CISO | Penetration testing program implemented and verified |
| 2025-02-10 | ISMS-POL-00 | Modify | REG-CYBER updated to v2.0 (Cybersecurity Regulation amended) | Legal Counsel | Regulation amendment published 2025-02-01 |

### Audit Trail Uses

**Demonstrates Active Management**:

- Shows compliance framework is not static "set and forget"
- Framework actively maintained, updated, improved
- Proves ongoing diligence

**Supports Internal/External Audits**:

- Auditors can review change history
- Verify that regulatory changes were identified and addressed
- Confirm that gaps were systematically remediated
- Audit trail shows compliance framework is working as designed

**Enables Forensic Review**:

- If compliance issue arises, trace back through audit trail
- Understand when and why decisions were made
- Identify process improvements to prevent recurrence

**Regulatory Defense**:

- If regulator questions compliance, audit trail demonstrates good faith effort
- Shows systematic approach, not negligence
- May mitigate penalties (demonstrated due diligence)

**Management Oversight**:

- Executive management can review audit trail in Management Review
- Confirm compliance activities occurring as planned
- Identify resource needs (high volume of changes may indicate need for more compliance staff)

---

# Handling Overlapping Requirements

Multiple regulations frequently mandate similar or identical security controls. Rather than duplicate implementations, [Organization] identifies overlaps and implements to the most stringent standard, achieving compliance with multiple regulations simultaneously.

## Identifying Overlapping Requirements

### Common Overlap Scenarios

**Data Protection Regulations**:

- GDPR (EU), CCPA (California), FADP (Switzerland), LGPD (Brazil) all require:
  - Encryption of personal data
  - Access controls
  - Breach notification
  - Data minimization
  - Similar requirements, different jurisdictions

**Sector-Specific Regulations**:

- Financial services: Multiple regulators (SEC, FINRA, Federal Reserve, state regulators) with overlapping cybersecurity requirements
- Healthcare: HIPAA, HITECH, state health information laws overlap

**Framework Harmonization**:

- Many regulations reference or align with ISO 27001, NIST Cybersecurity Framework, CIS Controls
- Implementing ISO 27001 often satisfies multiple regulatory requirements

### Overlap Detection Methods

**During Requirements Extraction**:

- When extracting requirements from new regulation, compare to existing requirements in Register
- Flag similar requirements (similar language, similar intent)
- Example: Extracting from CCPA, encounter "Implement reasonable security measures" → Similar to existing GDPR requirement "Implement appropriate technical and organizational measures"

**During Control Mapping**:

- Control Mapping Matrix visually shows overlaps
- When populating matrix, if control column already has many Primary mappings, this indicates control satisfies many requirements (likely overlap)
- Example: A.8.24 (Encryption) column has Primary mappings for REG-DP01-32-001 (GDPR), REG-CCPA-15-002 (CCPA), REG-FADP-08-001 (Swiss FADP) → Clear overlap

**Quarterly Overlap Analysis**:

- Periodically review Requirements Register and Mapping Matrix
- Identify requirements with similar interpreted text
- Identify controls mapped as Primary to 5+ requirements (high-overlap controls)
- Document overlaps in Requirements Register Notes field
  - Example: REG-DP01-32-001 Notes: "Overlaps with REG-CCPA-15-002, REG-FADP-08-001; implement to most stringent standard"

## Identifying the Most Stringent Requirement

When overlapping requirements exist, [Organization] SHALL implement to the MOST STRINGENT standard, ensuring all overlapping requirements are satisfied.

### Why Implement to Most Stringent Standard?

**Efficiency**:

- Implement once, satisfy multiple requirements
- Avoid multiple parallel implementations of similar controls
- Reduce complexity (one encryption standard, not different standards per regulation)

**Risk Mitigation**:

- Highest standard provides best security
- Satisfies all regulations simultaneously
- No risk of partial compliance

**Audit Simplification**:

- One implementation to audit, not multiple
- Same evidence serves multiple audits
- Consistent approach across organization

### Stringency Comparison Framework

**Technical Specifications**:
Compare technical parameters; higher/stronger is more stringent:

| Requirement | Technical Spec | Stringency Comparison |
|-------------|---------------|----------------------|
| REG-DP01: "Use industry-standard encryption" | Not specified | Less stringent (vague) |
| REG-FIN05: "Use AES-128 or higher encryption" | AES-128 minimum | Moderately stringent (specific but lower) |
| REG-SEC15: "Use AES-256 encryption for data at rest" | AES-256 required | **Most stringent** (highest standard) |

**Implementation**: Use AES-256 (satisfies all three requirements)

**Process Frequencies**:
Compare how often activities must occur; more frequent is more stringent:

| Requirement | Frequency | Stringency Comparison |
|-------------|-----------|----------------------|
| REG-DP01: "Review access rights periodically" | Not specified | Less stringent (vague) |
| REG-FIN05: "Review access rights annually" | Annual | Moderately stringent |
| REG-PCI: "Review access rights quarterly" | Quarterly | **Most stringent** (most frequent) |

**Implementation**: Quarterly access reviews (satisfies all three requirements)

**Documentation Requirements**:
Compare what documentation must be created; more comprehensive is more stringent:

| Requirement | Documentation | Stringency Comparison |
|-------------|--------------|----------------------|
| REG-DP01: "Establish access control policy" | Policy only | Less stringent |
| REG-FIN05: "Establish access control policy and procedures" | Policy + Procedures | Moderately stringent |
| REG-SEC15: "Establish policy, procedures, and technical standards for access control with annual review" | Policy + Procedures + Standards + Review | **Most stringent** (most comprehensive) |

**Implementation**: Policy + Procedures + Technical Standards + Annual Review (satisfies all three)

**Timelines and Deadlines**:
Compare timelines; shorter timeline is more stringent:

| Requirement | Timeline | Stringency Comparison |
|-------------|----------|----------------------|
| REG-DP01: "Notify data subjects of breaches without undue delay" | Unspecified | Less stringent (vague) |
| REG-CCPA: "Notify data subjects of breaches within reasonable timeframe" | Unspecified | Less stringent (vague) |
| REG-GDPR: "Notify data subjects of breaches within 72 hours unless low risk" | 72 hours | **Most stringent** (specific, short deadline) |

**Implementation**: 72-hour notification process (satisfies all three)

**Scope and Coverage**:
Compare what must be covered; broader scope is more stringent:

| Requirement | Scope | Stringency Comparison |
|-------------|-------|----------------------|
| REG-DP01: "Encrypt personal data during transmission over public networks" | Public networks only | Less stringent (limited scope) |
| REG-FIN05: "Encrypt sensitive data in transit" | All transmission | Moderately stringent (broader) |
| REG-SEC15: "Encrypt all data at rest and in transit using TLS 1.3 or higher" | At rest + in transit, specific protocol | **Most stringent** (broadest scope, specific) |

**Implementation**: Encrypt all data at rest and in transit using TLS 1.3+ (satisfies all three)

### Documentation of Most Stringent Determination

For each overlapping requirement set:

**Document in Requirements Register**:

- In "Notes" field for each requirement in overlap set:
  - "Overlaps with [list other requirement IDs]"
  - "Most stringent requirement: [Requirement ID]"
  - "Implementation follows most stringent standard"
- Example:
  - REG-DP01-32-001 Notes: "Overlaps with REG-FIN05-15-003, REG-SEC15-4.4-002; Most stringent: REG-SEC15-4.4-002 (requires AES-256); Implementation uses AES-256"

**Document in Control Implementation**:

- Control description or implementation guidance references most stringent requirement
- Example: A.8.24 (Use of Cryptography) implementation guidance states: "Encryption for data at rest uses AES-256 to satisfy REG-SEC15-4.4-002 (most stringent among overlapping encryption requirements)"

**Maintain Overlap Register** (Optional):

- Separate register documenting overlap sets
- Fields:
  - Overlap Set ID
  - Requirement IDs in overlap (list)
  - Most Stringent Requirement (ID)
  - Stringency Rationale (why this one is most stringent)
  - Implemented Standard (how implemented to most stringent)
  - Evidence (common evidence for all requirements in set)

## Demonstrating Compliance with All Applicable Regulations

### Mapping Matrix Shows Multi-Regulation Satisfaction

**Example Mapping Matrix (Partial)**:

| Requirement ID | Requirement | A.8.24 Cryptography | A.8.15 Logging | ... |
|----------------|-------------|---------------------|----------------|-----|
| REG-DP01-32-001 | Encrypt personal data | **P** | | |
| REG-FIN05-15-003 | Encrypt financial data | **P** | | |
| REG-HEALTH-12-001 | Encrypt health records | **P** | | |
| REG-SEC15-4.4-002 | Use AES-256 encryption | **P** | | |

**Interpretation**: A.8.24 (Use of Cryptography) control, when implemented to REG-SEC15-4.4-002 standard (AES-256), satisfies FOUR regulatory requirements from FOUR different regulations.

**One implementation**, **one set of evidence**, **four regulations compliant**.

### Evidence Serves Multiple Requirements

**Single Evidence Artifact, Multiple Uses**:

Example: Encryption Policy v2.1

- **Content**: Requires AES-256 for data at rest, TLS 1.3 for data in transit, quarterly key rotation
- **Control**: Evidence for A.8.24 (Use of Cryptography)
- **Satisfies Requirements**:
  - REG-DP01-32-001 (GDPR Article 32 encryption requirement)
  - REG-FIN05-15-003 (Financial regulation encryption requirement)
  - REG-HEALTH-12-001 (Healthcare data encryption requirement)
  - REG-SEC15-4.4-002 (Security standard encryption requirement)

**Audit Scenario**:

- **GDPR Auditor** asks: "Show me how you comply with Article 32 encryption requirement"
  - [Organization] provides: Encryption Policy v2.1, encryption configuration documentation, key management logs
  - Auditor confirms compliance
- **Financial Auditor** asks: "Show me how you protect financial data"
  - [Organization] provides: **SAME** Encryption Policy v2.1, configuration documentation, logs
  - Auditor confirms compliance
- **Healthcare Auditor** asks: "Show me health record protection"
  - [Organization] provides: **SAME** evidence again
  - Auditor confirms compliance

**Result**: One policy, three audits satisfied. Evidence efficiency in action.

### Compliance Reporting Per Regulation

Despite leveraging overlaps, [Organization] can still report compliance status per regulation:

**Regulatory Compliance Dashboard** (Assessment Workbook 6) shows:

| Regulation | Total Reqs | Satisfied | Gaps | Compliance % |
|-----------|-----------|-----------|------|--------------|
| Data Protection Regulation (REG-DP01) | 45 | 42 | 3 | 93% |
| Financial Regulation (REG-FIN05) | 38 | 38 | 0 | 100% |
| Healthcare Law (REG-HEALTH) | 22 | 20 | 2 | 91% |
| Security Standard (REG-SEC15) | 67 | 63 | 4 | 94% |

**How This Works Despite Overlaps**:

- Requirements Register has entries for EACH requirement from EACH regulation (even if overlapping)
- Control Mapping Matrix maps EACH requirement to appropriate controls
- Even though many requirements map to same control (overlap), each requirement tracked individually
- Compliance % calculated per regulation (satisfied requirements / total requirements for that regulation)

**Reporting Flexibility**:

- Can report compliance by regulation (for regulatory audits)
- Can report compliance by control (for ISO 27001 certification audit)
- Can report compliance by tier (Tier 1 vs. Tier 2 status)
- Can report control efficiency (controls satisfying most requirements = high ROI controls)

## Evidence Optimization

### Tagging Evidence with Multiple Requirements

**Evidence Register** includes field: "Satisfies Requirements"

- Multi-select field listing ALL requirement IDs satisfied by this evidence
- Example:
  - **Evidence**: Encryption Policy v2.1
  - **Satisfies Requirements**: REG-DP01-32-001, REG-FIN05-15-003, REG-HEALTH-12-001, REG-SEC15-4.4-002

**Benefits**:

- Easy retrieval for audits (search by requirement ID, find all relevant evidence)
- Shows efficiency (one evidence item, multiple requirements satisfied)
- Ensures evidence not duplicated (search before collecting new evidence to see if existing evidence suffices)

### Avoiding Evidence Duplication

**Before Collecting New Evidence**:
1. Check if requirement is in overlap set (Requirements Register Notes field)
2. If yes, check Control Mapping Matrix to see which control satisfies it
3. Check Evidence Register for existing evidence for that control
4. If existing evidence satisfies most stringent requirement in overlap set, it satisfies ALL requirements in set
5. Tag existing evidence with new requirement ID (add to "Satisfies Requirements" field)
6. Do NOT collect new evidence

**Example**:

- New regulation REG-NEWREG identified as applicable
- Extract requirement REG-NEWREG-10-001: "Encrypt data using industry-standard algorithms"
- During mapping, identify overlap with REG-DP01-32-001, REG-FIN05-15-003 (all encryption requirements)
- Most stringent is REG-SEC15-4.4-002 (requires AES-256)
- Check Evidence Register: Encryption Policy v2.1 already satisfies REG-SEC15-4.4-002
- **Action**: Tag Encryption Policy v2.1 with additional requirement REG-NEWREG-10-001
- **Do NOT** create separate encryption policy for REG-NEWREG

**Result**: Evidence efficiency maintained, no duplication.

### Evidence Collection Strategy for Overlapping Requirements

**Collect Once, Tag Many**:

- Identify high-overlap controls (controls satisfying many requirements)
- Prioritize evidence collection for these controls (high ROI)
- Comprehensively tag evidence with all satisfied requirements
- Maintain evidence to highest standard (satisfies most stringent requirement in any overlap set)

**Periodic Evidence Review**:

- Quarterly: Review Evidence Register for each high-overlap control
- Ensure evidence still satisfies most stringent requirement (regulations may change)
- Update evidence tags if new requirements added to overlap set
- Identify evidence gaps (requirements without evidence)

**Audit Preparation Efficiency**:

- Pre-audit: Generate evidence packages per regulation
- Evidence packages may reuse same artifacts (tagged with multiple requirement IDs)
- Auditors understand overlaps, do not view reuse negatively (demonstrates efficiency and consistency)

---

# Document Control & Related Documents

## Document Information

**Document ID**: ISMS-POL-A.5.31.3  
**Title**: Requirements Extraction & Control Mapping Framework  
**Version**: 1.0  
**Effective Date**: [TBD upon approval]  
**Classification**: Internal  
**Owner**: ISMS Manager / Compliance Officer  

**Review Frequency**: Annually or upon:

- Significant regulatory changes affecting multiple regulations
- Major changes to ISO 27001 standard
- Organizational changes affecting compliance scope
- Methodology improvements identified through use

**Next Review Date**: [Effective Date + 12 months]

## Related Documents

**ISMS Policy Framework**:

- **ISMS-POL-A.5.31.1**: Executive Summary & Control Alignment
  - Provides framework foundation and governance structure
  - Defines roles referenced in this document
- **ISMS-POL-A.5.31.2**: Regulatory Applicability Methodology
  - Determines WHICH regulations apply (input to this document)
  - Maintains ISMS-POL-00 regulatory register
- **ISMS-POL-00**: Regulatory Applicability Framework
  - Master list of applicable regulations
  - Source for regulations from which requirements are extracted
- **ISMS-POL-A.5.31.4**: Change Management & Evidence Framework (subsequent)
  - Defines regulatory monitoring and evidence management processes
  - Builds on control mappings defined in this document

**Implementation Guides**:

- **ISMS-IMP-A.5.31.3**: Requirements Extraction Process
  - Step-by-step operational guide for extracting requirements
  - Implements requirements extraction methodology (Section 2)
- **ISMS-IMP-A.5.31.3**: Control Mapping Process
  - Step-by-step operational guide for mapping requirements to controls
  - Implements control mapping methodology (Section 3)
- **ISMS-IMP-A.5.31.5**: Evidence Management Process (subsequent)
  - Operational guide for collecting and managing evidence
  - Uses traceability framework defined in Section 5

**Assessment Workbooks**:

- **Assessment Workbook 3**: Requirements Extraction Register
  - Template for maintaining Requirements Register (Section 2.3)
  - Standardized format with data validation
- **Assessment Workbook 4**: Control Mapping Matrix
  - Template for maintaining Control Mapping Matrix (Section 3.3)
  - Pre-populated with 93 Annex A controls
  - Conditional formatting for gap visualization
- **Assessment Workbook 5**: Compliance Evidence Register (subsequent)
  - Template for tracking evidence linked to controls and requirements
  - Supports traceability framework (Section 5)

**Standards and External References**:

- **ISO/IEC 27001:2022**: Information Security Management Systems - Requirements
  - Annex A: Controls catalog (93 controls referenced throughout this document)
- **ISO/IEC 27002:2022**: Information Security Controls
  - Implementation guidance for Annex A controls
  - Reference for understanding control capabilities when mapping

## Definitions

**Control Mapping**: Process of linking regulatory requirements to ISO 27001 controls that satisfy those requirements.

**Gap**: Regulatory requirement for which no control exists or existing controls are inadequate.

**Primary Control (P)**: Control that directly and substantially satisfies a regulatory requirement.

**Requirements Register**: Authoritative repository of all extracted requirements from applicable regulations.

**Secondary Control (S)**: Control that partially satisfies or supports satisfaction of a regulatory requirement.

**Supporting Control (Su)**: Control that contributes indirectly to satisfaction of a regulatory requirement.

**Traceability**: Ability to trace forward (regulation → evidence) and backward (evidence → regulation) through requirements and controls.

---

**END OF DOCUMENT**

---

*This policy establishes the translation methodology from regulatory text to actionable controls, enabling [Organization] to demonstrate HOW it satisfies regulatory requirements through systematic control implementation.*
<!-- QA_VERIFIED: 2026-02-01 -->
