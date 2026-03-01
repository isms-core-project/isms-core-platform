<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.31.3-UG:framework:UG:a.5.31.3 -->
**ISMS-IMP-A.5.31.3-UG - Requirements Extraction Process**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.31: Legal, Statutory, Regulatory and Contractual Requirements

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Requirements Extraction Process |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.31.3-UG |
| **Related Policy** | ISMS-POL-A.5.31 (Legal Statutory Regulatory Contractual Requirements) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.31 (Legal, Statutory, Regulatory and Contractual Requirements) |
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

- ISMS-POL-A.5.31 (Legal Statutory Regulatory Contractual Requirements)
- ISMS-IMP-A.5.31.1 (Regulatory Inventory Management Process)
- ISMS-IMP-A.5.31.2 (Regulatory Applicability Assessment Process)
- ISMS-IMP-A.5.31.4 (Control Mapping Process)
- ISMS-IMP-A.5.31.5 (Evidence Management Process)

---

### Workbook at a Glance

This workbook contains the following 5 sheets:

| Sheet | Purpose |
|-------|---------|
| **Instructions & Legend** | Assessment guidance, rating definitions, and field descriptions |
| **Requirements Register** | Extracted regulatory requirements with control mappings |
| **Summary Dashboard** | Compliance overview auto-populated from your input data |
| **Approval Sign-Off** | Stakeholder sign-off and approval workflow |
| **Extraction Worksheet** | Working template for systematic requirements extraction |

---

# Process Overview

## Purpose

This implementation guide operationalizes the requirements extraction methodology defined in ISMS-POL-A.5.31.3 Section 2. It provides step-by-step instructions for transforming regulatory text into specific, actionable requirements that can be mapped to ISO 27001 controls and implemented by [Organisation].

**The Translation Challenge**:
Regulations are written in legal language for legal purposes. Security controls are implemented in technical and organisational terms. Requirements extraction is the "translation layer" that bridges this gap.

**Example**:

- Legal Language: "Organisations shall implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk..."
- Translation: Three specific requirements: (1) Implement risk assessment process, (2) Implement technical security controls appropriate to identified risks, (3) Implement organisational security controls appropriate to identified risks
- Implementation: Maps to specific ISO 27001 controls (A.5.7 Threat Intelligence, A.8.8 Technical Vulnerability Management, etc.)

## When to Use This Process

**Trigger**: Regulation determined applicable (IMP-5.31.1 process complete, regulation added to ISMS-POL-00 as Tier 1 or Tier 2)

**Input**: 

- Regulation text (official legal text)
- ISMS-POL-00 entry for regulation
- Applicability Assessment (from IMP-5.31.1)

**Output**:

- Requirements Register populated with extracted requirements
- Each requirement ready for control mapping (IMP-5.31.3 next step)

## Who Performs This Process

**Primary Roles**:

- **Compliance Officer**: Leads extraction, coordinates team, ensures completeness
- **Legal Counsel**: Provides legal interpretation, reviews extraction for accuracy (especially Tier 1)
- **ISMS Specialist**: Ensures requirements are actionable for control implementation

**Collaborative Process**:
Requirements extraction is NOT a solo activity. Best results come from team:

- Compliance Officer extracts requirements based on regulatory reading
- Legal Counsel reviews for legal accuracy
- ISMS Specialist reviews for implementability
- Iterate until all three are satisfied

## Process Flowchart

```
[Applicable Regulation - Tier 1 or Tier 2 from IMP-5.31.1]
              ↓
[STEP 1: Parse Regulation Structure]

- Read definitions, scope, articles systematically
- Create extraction worksheet (article-by-article plan)
- Identify complex sections needing legal review

              ↓
[STEP 2: Identify Mandatory vs. Recommendatory Language]

- Highlight "shall", "must", "is required to"
- Distinguish from "should", "may", "is encouraged to"
- Flag ambiguous language for legal review

              ↓
[STEP 3: Extract & Rewrite in Actionable Form]

- For each mandatory provision:
  - Identify discrete obligations
  - Rewrite in active voice, action verb
  - Apply granularity guidelines (not too coarse, not too fine)
  - Maintain citation to regulation

              ↓
[STEP 4: Categorize Requirements]

- Assign category: Technical, Organisational, Reporting, Operational
- Streamlines control mapping (know which Annex A sections relevant)

              ↓
[STEP 5: Requirements Register Entry]

- Populate register with all fields
- Assign Requirement ID (REG-[Code]-[Article]-[Seq])
- Link to Regulation ID in ISMS-POL-00
- Complete metadata (priority, status, responsible party)

              ↓
[STEP 6: Review & Validation]

- Completeness check (all obligations extracted?)
- Accuracy check (faithful to regulation?)
- Granularity check (actionable?)
- Legal review (Tier 1 mandatory)
- Final approval (Compliance Officer, Legal, ISMS Manager)

              ↓
[Requirements Register Updated & Approved]
              ↓
[Proceed to Control Mapping (IMP-5.31.3)]
```

## Timeline

**Simple Regulation** (10-20 requirements, clear language, well-defined scope):

- Step 1 (Parse): 1-2 days
- Step 2-3 (Extract): 2-3 days
- Step 4-5 (Categorize & Register): 1 day
- Step 6 (Review): 2-3 days
- **Total**: 1-2 weeks

**Complex Regulation** (50+ requirements, ambiguous language, complex structure, novel regulatory approach):

- Step 1 (Parse): 3-5 days
- Step 2-3 (Extract): 1-2 weeks (legal consultation, interpretation iterations)
- Step 4-5 (Categorize & Register): 2-3 days
- Step 6 (Review): 1-2 weeks (legal review, executive review for Tier 1)
- **Total**: 4-6 weeks

**Factors Increasing Complexity**:

- Regulation length (longer = more requirements)
- Legal ambiguity (unclear language requires interpretation)
- Novel regulatory concepts (no precedent to guide extraction)
- Cross-references to other regulations
- Conditional requirements (many "if X then Y" provisions)

## Key Artifacts

**Inputs**:

- Regulation text (PDF, official website, legal database)
- ISMS-POL-00 entry (regulation metadata)
- Applicability Assessment (from IMP-5.31.1, provides context)

**Working Documents**:

- Extraction Worksheet (article-by-article tracking during process)
- Markup of regulation text (highlighted, annotated)
- Legal review notes (interpretations, clarifications)

**Outputs**:

- Requirements Register (Assessment Workbook 3) - populated with extracted requirements
- Approval documentation (legal sign-off, compliance approval)

---

# Step 1 - Parse Regulation Structure

**Purpose**: Understand the regulation systematically before extracting requirements. Rushing into extraction without understanding structure leads to missed requirements and misinterpretations.

## Understanding Regulatory Structure

Regulations typically follow structured formats, though specific formats vary by jurisdiction and regulatory authority.

**Common Structural Elements**:

**Articles / Sections / Clauses**:

- Major divisions of regulation
- Typically numbered sequentially (Article 1, Article 2, etc. OR Section 1, Section 2, etc.)
- Each article addresses a distinct topic or obligation
- Example: "Article 32: Security of Processing"

**Sub-sections / Paragraphs**:

- Subdivisions within articles
- Provide detail or enumerate specific requirements
- Example: "Article 32(1)(a): Pseudonymization and encryption of personal data"

**Annexes / Schedules / Appendices**:

- Supplementary material attached to main regulation text
- May contain technical specifications, lists, forms, templates
- Example: "Annex A: Technical and Organisational Security Measures"

**Definitions**:

- Section defining key terms used throughout regulation
- Critical for interpretation (terms may have specific legal meanings different from common usage)
- Example: Definition of "personal data", "processing", "controller", "processor"
- Typically at beginning of regulation

**Scope / Applicability**:

- Defines who/what regulation applies to
- May include thresholds, exemptions, territorial scope
- Already reviewed during IMP-5.31.1, but reconfirm during extraction

**Obligations** (the requirements):

- Articles containing "shall", "must", "is required to"
- These are the sections to extract requirements from
- May be interspersed throughout or concentrated in specific sections

**Guidance / Commentary / Recitals**:

- Explanatory notes, intent, background
- Helpful for understanding context but NOT legally binding
- Don't extract requirements from guidance (only from binding provisions)

**Penalties / Enforcement**:

- Articles defining consequences of non-compliance
- Informs priority but don't extract as requirements
- Example: "Violations may result in fines up to €10M or 2% of revenue"

## Reading Systematically

**Step-by-Step Reading Process**:

**Step 2.2.1: Read Definitions FIRST**

Before reading any obligations, understand how regulation defines key terms.

**Why This Matters**:

- Same word may have different meanings in different regulations
- Example: "Personal data" definition varies (GDPR vs. CCPA vs. other laws)
- Obligations reference defined terms; misunderstanding definition = misunderstanding requirement

**What to Do**:

- Locate definitions section (often Article 1 or Article 4)
- Read all definitions
- Note definitions that differ from [Organisation]'s current understanding or common usage
- Create glossary for reference during extraction

**Example**:

- Regulation defines "Processing" as "any operation performed on personal data, including collection, storage, use, transmission, deletion"
- Extracted requirement references "processing" → Applies to all those activities, not just one

**Step 2.2.2: Read Scope / Applicability**

Reconfirm what regulation applies to (already assessed in IMP-5.31.1, but re-read for extraction context).

**Why This Matters**:

- Some requirements may only apply to subset of [Organisation]'s activities
- Example: Regulation applies to "high-risk processing" → Requirements only apply to those specific processes

**What to Do**:

- Identify scope provisions (typically early articles)
- Note any limitations (applies only to X, exempt if Y, threshold of Z)
- Flag conditional applicability (applies if certain criteria met)
- This scoping informs requirement extraction (some requirements conditional)

**Step 2.2.3: Read Articles in Sequential Order**

Don't skip around. Regulations are structured deliberately.

**Why Sequential Reading**:

- Articles often build on each other
- Later articles reference earlier articles
- Understanding flow prevents misinterpretation

**How to Read**:

- Start at Article 1 (or first substantive article after definitions)
- Read each article completely before moving to next
- Note cross-references ("as defined in Article X", "subject to Article Y")
- Don't jump to "interesting" articles first (tempting but risky)

**Step 2.2.4: Identify Overall Structure**

As you read, map the regulation's architecture.

**Create Simple Outline**:
```
Example Regulation Structure:

Articles 1-5: Definitions and Scope
Articles 6-15: Data Protection Principles and Lawful Basis
Articles 16-23: Data Subject Rights
Articles 24-40: Controller and Processor Obligations
Articles 41-50: Transfers and International Data Flows
Articles 51-59: Supervisory Authorities
Articles 60-76: Remedies, Liability, Penalties
Articles 77-91: Final Provisions
```

**This Outline**:

- Shows which sections contain obligations (Articles 24-40 in example)
- Helps estimate extraction effort
- Guides prioritization (start with obligation-heavy sections)

## Marking Up the Regulation

Physical or digital markup makes extraction more efficient and accurate.

**Tools**:

- **Physical Document**: Highlighters, pens, sticky notes
- **Digital Document (PDF)**: PDF annotation tools (Adobe Acrobat, Preview, web browser PDF viewers)
- **Digital Document (Word/Text)**: Comments, highlight, track changes

**Markup Strategy**:

**Highlight Mandatory Language** (Color: Yellow):

- "shall"
- "must"
- "is required to"
- "will" (in obligatory context)
- These are requirement indicators

**Underline Key Requirements** (or Second Color: Orange):

- Specific obligations within mandatory articles
- Example: In "shall implement encryption", underline "encryption"

**Bracket Definitions** (or Third Color: Green):

- Terms defined in definitions section when they appear in obligations
- Example: When "personal [data]" appears in Article 32, bracket it
- Reminder to apply regulatory definition

**Note Cross-References** (Margin Notes):

- When article references another article, note in margin
- Example: Margin note "See Art. 5 for principles" when Art. 32 says "consistent with Article 5"
- Follow up cross-references during extraction

**Flag Unclear Sections** (or Fourth Color: Red):

- Ambiguous language
- Complex conditional requirements
- Legal terms unfamiliar to you
- Mark for legal review

**Example Marked-Up Article**:

> Article 32: Security of Processing
> 
> The controller and processor **shall** implement appropriate [technical] and [organisational measures] to ensure a level of security appropriate to the risk, including inter alia as appropriate:
> 
> (a) **pseudonymization** and **encryption** of [personal data];
> 
> (b) the ability to ensure the ongoing **confidentiality**, **integrity**, **availability** and **resilience** of [processing systems] and services;
>
> *[Margin note: "Appropriate to risk" - see Art. 5 risk-based approach]*
> 
> *[Red flag: "inter alia as appropriate" - non-exhaustive list, how comprehensive must implementation be? Legal review.]*

## Creating Extraction Worksheet

Before extracting requirements, create a worksheet to track progress and plan extraction.

**Worksheet Purpose**:

- Article-by-article inventory
- Effort estimation
- Progress tracking
- Legal review planning

**Worksheet Structure** (Spreadsheet Recommended):

| Article # | Article Title | Summary (1-2 sentences) | Contains Obligations? (Y/N) | Est. # Requirements | Complexity (S/M/C) | Legal Review Needed? (Y/N) | Status | Notes |
|-----------|---------------|-------------------------|-----------------------------|--------------------|-------------------|---------------------------|--------|-------|
| Article 4 | Definitions | Defines key terms | N | 0 | S | N | Complete | Referenced during extraction |
| Article 32 | Security of Processing | Security measures required | Y | 4-5 | M | Y | In Progress | Ambiguous scope of "appropriate" |
| Article 33 | Breach Notification | Notification to authority | Y | 2-3 | C | Y | Not Started | Complex timeline and conditions |

**How to Use Worksheet**:

1. **First Pass Through Regulation**:

   - Create row for each article
   - Complete Article #, Title, Summary columns
   - Mark Y/N for "Contains Obligations"
   - Leave other columns for second pass

2. **Second Pass (For Articles with Obligations)**:

   - Estimate number of requirements (rough count of "shall"/"must")
   - Assess complexity:
     - **Simple (S)**: Clear language, straightforward obligation
     - **Moderate (M)**: Some ambiguity, multiple sub-requirements
     - **Complex (C)**: Highly ambiguous, conditional, cross-referenced, novel concept
   - Determine if legal review needed (typically Y for Moderate/Complex)

3. **During Extraction**:

   - Update Status: Not Started → In Progress → Complete
   - Add Notes as you extract (issues, questions, decisions)

4. **After Extraction**:

   - Worksheet becomes audit trail showing systematic approach
   - File with extracted requirements documentation

**Worksheet Benefits**:

- Prevents skipping articles
- Estimates effort realistically
- Prioritizes legal review where needed
- Tracks progress (manager can see % complete)

---

# Step 2 - Identify Mandatory vs. Recommendatory Language

**Purpose**: Distinguish legal obligations (must extract) from guidance/recommendations (note but don't extract as requirements).

## Mandatory Language

**These words/phrases indicate OBLIGATION** → Extract as requirement:

**"Shall"** (Strongest Mandatory):

- Legal drafting convention: "shall" = mandatory obligation
- Example: "Organisations shall implement access controls"
- Action: Extract as mandatory requirement
- Frequency: Very common in regulations

**"Must"**:

- Equally mandatory as "shall"
- Example: "Data processors must maintain records of processing activities"
- Action: Extract as mandatory requirement
- Frequency: Common, especially in non-legal-drafting contexts (regulations translated from other languages)

**"Is required to" / "Are required to"**:

- Explicit obligation language
- Example: "Controllers are required to conduct Data Protection Impact Assessments for high-risk processing"
- Action: Extract as mandatory requirement

**"Will"** (In Obligatory Context):

- When used to express obligation (not future tense description)
- Example: "The processor will notify the controller within 24 hours of any breach"
- Context: This is obligation, not prediction
- Action: Extract as mandatory requirement
- Caution: "Will" can be ambiguous; consider context

**"Has/Have obligation to"**:

- Example: "Organisations have an obligation to ensure data accuracy"
- Action: Extract as mandatory requirement

**Implicit Obligations** (No Modal Verb):

- Some regulations state obligations directly without "shall"/"must"
- Example: "Organisations implement technical safeguards" (present tense used as obligation)
- Context: Check if this is obligation or description; when in doubt, consult legal counsel
- Action: If obligation, extract

## Recommendatory Language

**These words/phrases indicate GUIDANCE** → Note as best practice, do NOT extract as mandatory requirement:

**"Should"**:

- Recommended but not mandatory
- Example: "Organisations should consider implementing multi-factor authentication for privileged accounts"
- Action: Note as best practice; do not create mandatory requirement
- Frequency: Common in guidance documents, less common in binding regulations

**"May"**:

- Optional / Permissive
- Example: "Organisations may appoint a Data Protection Officer"
- Action: Note as option; not mandatory unless contract or other regulation makes it mandatory
- Exception: If contract requires DPO, "may" in regulation becomes "shall" contractually

**"Is encouraged to" / "Is advised to"**:

- Guidance language
- Example: "Controllers are encouraged to adopt Privacy by Design principles"
- Action: Note as guidance; informational only

**"Recommended" / "Suggested"**:

- Best practice, not obligation
- Example: "It is recommended that organisations conduct annual penetration testing"
- Action: Note as best practice

**"Could" / "Can"**:

- Possibility, not obligation
- Example: "Organisations could implement anonymization to reduce risk"
- Action: Note as option

## Contextual Interpretation

Some language requires careful contextual analysis.

**"Should" with Detailed Specification**:

**Example**:
> "Password complexity should be: minimum 12 characters, including uppercase, lowercase, numbers, and symbols; passwords should be changed every 90 days."

**Analysis**:

- Uses "should" (normally recommendatory)
- BUT: Provides very specific, detailed requirements (12 chars, complexity rules, 90-day rotation)
- Detailed specification suggests this is more than guidance
- Context: In some regulations (especially technical standards), "should" is used for mandatory requirements

**Action**:

- Flag for legal review
- Legal counsel determines if this is mandatory despite "should"
- If legal counsel confirms mandatory: Extract as requirement
- If legal counsel confirms recommendatory: Note as guidance

**"Or" - Alternatives**:

**Example**:
> "Organisations shall implement encryption or pseudonymization for personal data"

**Analysis**:

- "Shall" = Mandatory
- "Or" = Alternatives (organisation can choose)

**Extraction**:

- Single requirement: "Implement encryption or pseudonymization for personal data"
- OR: Two alternative requirements: (1) "Implement encryption for personal data" OR (2) "Implement pseudonymization for personal data"
- Recommended: Single requirement with "or" (preserves implementation flexibility)

**Conditional Requirements ("If X, then shall Y")**:

**Example**:
> "If processing special categories of personal data, organisations shall implement additional safeguards"

**Analysis**:

- Condition: "If processing special categories..."
- Obligation: "...shall implement additional safeguards"
- Obligation is mandatory IF condition met

**Extraction**:

- Extract with condition noted
- Requirement: "Implement additional safeguards for special categories of personal data (when processing such data)"
- OR: "If processing special categories of personal data, implement additional safeguards"
- During control mapping: Assess if [Organisation] meets condition (if yes, requirement applies)

**"Unless"**:

**Example**:
> "Organisations shall notify the supervisory authority within 72 hours of becoming aware of a breach, unless the breach is unlikely to result in risk to individuals"

**Analysis**:

- Default obligation: Notify within 72 hours
- Exception: Unless unlikely to result in risk

**Extraction**:

- Single requirement including exception: "Notify supervisory authority within 72 hours of becoming aware of breach, unless breach is unlikely to result in risk to individuals"
- Preserves full obligation including exception

## When in Doubt

**General Principle**: If uncertain whether language is mandatory, err on side of caution.

**Decision Framework**:
1. **Is there mandatory language present** ("shall", "must", "required")? → Likely mandatory
2. **Is there recommendatory language** ("should", "may", "encouraged")? → Likely guidance
3. **Is language ambiguous** (could be interpreted either way)? → Flag for legal review
4. **Would failure to comply violate the regulation**? → If yes, mandatory; if no, guidance

**When to Engage Legal Counsel**:

- Ambiguous language (could be interpreted multiple ways)
- Novel regulatory concept (no precedent)
- High-stakes obligation (significant penalty if wrong)
- Tier 1 regulation (mandatory compliance, legal review required anyway)

**Better to Extract and Discard than Miss and Face Non-Compliance**:

- If borderline, extract as requirement and flag for review
- Legal counsel can confirm: "Yes, this is mandatory" or "No, this is guidance only"
- Easy to remove non-mandatory item during review
- Hard to identify missing mandatory requirement after extraction complete

---

# Step 3 - Extract & Rewrite in Actionable Form

**Purpose**: Transform legal language into clear, implementable requirements that control owners can act on.

## Granularity Guidelines

Requirements must be "just right" - specific enough to implement, general enough to remain flexible.

**Too Coarse - NOT Actionable**:

**Examples**:

- "Comply with Article 32"
- "Implement security measures"
- "Ensure data protection"
- "Maintain compliance"

**Problems**:

- Vague (what specific actions required?)
- Cannot map to controls (which controls satisfy "security measures"?)
- Not measurable (how to verify compliance?)
- Not implementable (control owner doesn't know what to do)

**Too Fine - TOO Prescriptive**:

**Examples**:

- "Use AES-256 encryption in CBC mode with PKCS#7 padding and 128-bit keys rotated every 90 days"
- "Configure firewall to deny TCP port 23, UDP port 69, TCP port 21, and allow only TCP port 443 on egress"
- "Store security logs for exactly 395 days in ISO 27001 certified data center in Switzerland with triple redundancy"

**Problems**:

- Over-specifies implementation (regulation usually doesn't mandate specific algorithms, ports, durations this precisely)
- Limits flexibility (what if better encryption algorithm available in 2 years?)
- May become obsolete (algorithm deprecated, port requirements change)
- Adds requirements not in regulation (over-interpretation)

**Just Right - Actionable with Flexibility**:

**Examples**:

- "Implement encryption for data at rest using industry-standard algorithms appropriate to data sensitivity"
  - Specific: Encryption, data at rest
  - Flexible: "Industry-standard algorithms" allows AES-256 today, post-quantum tomorrow
  
- "Restrict administrative access by blocking unnecessary services and allowing only required ports"
  - Specific: Block unnecessary, allow required
  - Flexible: [Organisation] determines which ports necessary based on services used
  
- "Retain security logs for minimum 12 months or longer as required by applicable regulations"
  - Specific: Minimum 12 months
  - Flexible: Allows longer retention if needed; "or longer" accommodates future regulation changes

**How to Achieve "Just Right"**:
1. Extract the WHAT (what must be done) specifically
2. Keep the HOW (how to do it) general
3. Include context when it limits scope (e.g., "for personal data", "over untrusted networks")
4. Allow implementation options when regulation allows them

## Extraction Technique

**Process for Each Mandatory Provision**:

**Example Original Regulation Text**:
> "Article 32(1): The controller and processor shall implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk, including inter alia as appropriate:
> 
> (a) the pseudonymization and encryption of personal data;
> 
> (b) the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services;
> 
> (c) the ability to restore the availability and access to personal data in a timely manner in the event of a physical or technical incident;
> 
> (d) a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing."

**Step 4.2.1: Identify Discrete Obligations**

Break down complex article into individual obligations:

- **Obligation 1**: Implement technical and organisational security measures
- **Obligation 2**: Measures must be appropriate to risk
- **Obligation 3**: Include pseudonymization and encryption (example)
- **Obligation 4**: Ensure confidentiality, integrity, availability, resilience (CIA+R)
- **Obligation 5**: Restore availability and access after incidents (business continuity/disaster recovery)
- **Obligation 6**: Regularly test, assess, evaluate effectiveness (ongoing assurance)

**Step 4.2.2: Rewrite Each in Actionable Form**

Transform each obligation into requirement:

**REQ-001**: "Implement technical and organisational security measures appropriate to the risk level of data processing activities"

- Action verb: "Implement"
- What: "technical and organisational security measures"
- Context: "appropriate to risk level"
- Result: Clear, actionable

**REQ-002**: "Implement pseudonymization or encryption controls for personal data to reduce processing risk"

- Action verb: "Implement"
- What: "pseudonymization or encryption"
- Scope: "for personal data"
- Purpose: "to reduce risk"
- Note: "or" preserves flexibility

**REQ-003**: "Implement controls to ensure ongoing confidentiality, integrity, availability, and resilience of information processing systems"

- Action verb: "Implement controls"
- What: "ensure C-I-A-R" (common security triad plus resilience)
- Scope: "information processing systems"
- "Ongoing" implies continuous operation, not one-time

**REQ-004**: "Establish business continuity and disaster recovery capabilities to restore data availability and access in timely manner following incidents"

- Action verb: "Establish"
- What: "BC/DR capabilities"
- Purpose: "restore availability and access"
- Context: "following incidents"
- "Timely manner" (from regulation) preserved

**REQ-005**: "Conduct regular testing, assessment, and evaluation of the effectiveness of security controls"

- Action verb: "Conduct"
- What: "testing, assessment, evaluation"
- Focus: "effectiveness of security controls"
- Frequency: "regular" (will define in implementation; regulation doesn't specify)

**Step 4.2.3: Maintain Citation**

Each extracted requirement links back to source:

- Citation: Article 32(1) for all five requirements
- Enables traceability (requirement → regulation article)
- If regulation changes Article 32(1), know which requirements affected

## Writing Actionable Requirements

**Best Practices for Clear Requirements**:

**Practice 1: Use Active Voice**

✅ **Good**: "Implement access controls for information systems"
❌ **Poor**: "Access controls should be implemented for information systems" (passive)

Why: Active voice is clearer, more direct, easier to understand and implement.

**Practice 2: Start with Action Verb**

**Common Action Verbs**:

- **Implement**: For technical/organisational controls
- **Establish**: For policies, procedures, governance structures
- **Maintain**: For ongoing activities (keep current, update as needed)
- **Conduct**: For assessments, tests, reviews
- **Document**: For documentation requirements
- **Ensure**: For outcomes that must be achieved
- **Monitor**: For ongoing observation/surveillance
- **Review**: For periodic examination
- **Report**: For notification/disclosure requirements

**Examples**:

- "Implement encryption for sensitive data"
- "Establish incident response procedures"
- "Maintain current inventory of information assets"
- "Conduct annual security awareness training"
- "Document all security exceptions and approvals"
- "Ensure vendor contracts include data protection clauses"
- "Monitor security logs for anomalous activity"
- "Review access rights quarterly"
- "Report security breaches to authority within 72 hours"

**Practice 3: Be Specific About WHAT, General About HOW**

✅ **Good**: "Implement authentication for system access using passwords, biometrics, tokens, or other appropriate mechanisms"

- Specific WHAT: Authentication for system access
- General HOW: Multiple options listed, plus "other appropriate mechanisms"

❌ **Poor**: "Implement authentication" (too vague - authentication for what?)
❌ **Poor**: "Require 12-character passwords with uppercase, lowercase, numbers, symbols, rotated every 60 days" (over-prescriptive - regulation likely doesn't specify this detail)

**Practice 4: Include Context When It Limits Scope**

**Examples with Context**:

- "Implement encryption for personal data **in transit over public networks**" (context: when/where encryption required)
- "Conduct background checks for employees **with access to sensitive data**" (context: which employees)
- "Require multi-factor authentication for **administrative access**" (context: which type of access)

**Without Context** (if regulation doesn't limit scope):

- "Implement encryption for personal data" (applies to all personal data, all contexts)

**Practice 5: Avoid Duplication**

If regulation says same thing multiple times (common in laws with cross-references), extract requirement once and note multiple citations.

**Example**:

- Article 5 says: "Personal data shall be processed securely"
- Article 32 says: "Implement security measures for personal data processing"
- Both saying same thing

**Action**: Extract as single requirement, cite both articles:

- Requirement: "Implement security measures for personal data processing"
- Citation: Articles 5(1)(f), 32(1)

**Practice 6: Avoid Over-Interpretation**

**Over-Interpretation Example**:

- Regulation: "Organisations shall implement access controls"
- ❌ Over-Interpreted Requirement: "Implement role-based access control with least privilege, separation of duties, and quarterly access reviews"
- Why wrong: Regulation says "access controls" (general), not "role-based with least privilege and quarterly reviews" (specific). You added requirements.

**Correct Extraction**:

- ✅ Requirement: "Implement access controls to restrict information access to authorised individuals"
- Why correct: Captures obligation ("implement access controls") without adding specificity regulation doesn't require

**When to Add Detail**:

- Only if regulation provides that detail
- If regulation says "quarterly access reviews", include "quarterly"
- If regulation doesn't specify, don't add specificity

## Handling Special Cases

**Case 1: Conditional Requirements**

**Regulation Example**:
> "If processing special categories of personal data, organisations shall implement additional safeguards"

**Extraction**:

- **Option A**: "Implement additional safeguards for special categories of personal data (when processing such data)"
- **Option B**: "IF processing special categories of personal data, THEN implement additional safeguards"

**Recommended**: Option A (cleaner)

**Notes Field**: "Conditional requirement - applies only if [Organisation] processes special categories (e.g., health, biometric, genetic data). Assess during control mapping."

**Case 2: Requirements with Alternatives**

**Regulation Example**:
> "Organisations shall implement encryption or pseudonymization for personal data"

**Extraction**:

- ✅ "Implement encryption or pseudonymization for personal data"

**Preserves Choice**: [Organisation] can choose encryption, pseudonymization, or both. Don't arbitrarily choose one.

**Case 3: Requirements with Examples ("Including but not limited to...")**

**Regulation Example**:
> "Technical measures shall include, but are not limited to, encryption, access control, and network security"

**Analysis**:

- Examples provided: encryption, access control, network security
- "Including but not limited to" = examples are illustrative, not exhaustive

**Extraction**:

- "Implement technical security measures (examples include encryption, access control, network security)"

**Notes Field**: "Regulation provides examples but is non-exhaustive. [Organisation] should implement comprehensive technical measures appropriate to risk."

**Case 4: Quantitative Requirements**

**Regulation Example**:
> "Organisations must notify the supervisory authority within 72 hours of becoming aware of a personal data breach"

**Extraction**:

- ✅ "Notify supervisory authority within 72 hours of becoming aware of personal data breach"

**Preserve Specific Numbers**: When regulation specifies timeline, threshold, frequency, or quantity, include it exactly.

**More Examples**:

- "Retain logs for minimum 12 months" (if regulation says 12 months)
- "Conduct penetration testing annually" (if regulation says annual)
- "Applies to organisations processing data of 50,000+ individuals" (threshold)

**Case 5: Requirements Referencing Other Articles**

**Regulation Example**:
> "Data processing shall comply with the principles set forth in Article 5"

**Extraction Approach**:

- Don't extract as "Comply with Article 5" (too coarse)
- Instead: Extract specific principles from Article 5
- Each principle becomes separate requirement
- Cross-reference back to both the referencing article and Article 5

**Case 6: Requirements in Annexes/Schedules**

Some regulations have obligations in annexes (not just main articles).

**Action**: Review all annexes for mandatory language ("shall", "must")

**Extraction**: Same process as main articles

- Requirement ID format: REG-[Code]-ANNEX[X]-[Seq]
- Example: REG-GDPR-ANNEX1-001

---

# Step 4 - Categorize Requirements

**Purpose**: Categorize each requirement by type to streamline control mapping and assign responsibilities.

## Requirement Categories

**Category 1: Technical Requirements**

**Definition**: Requirements that relate to information systems, technology, technical security controls.

**Characteristics**:

- Implemented through technology
- Involve configuration, deployment, technical architecture
- Often require IT/Security Engineering resources

**Examples**:

- "Implement encryption for data at rest"
- "Configure firewalls to restrict unauthorised network access"
- "Deploy intrusion detection and prevention systems"
- "Implement automated malware detection on endpoints"
- "Enable multi-factor authentication for system access"

**Maps To**: ISO 27001 Annex A Section 8 (Technology Controls)

**Category 2: Organisational Requirements**

**Definition**: Requirements that relate to policies, procedures, governance, roles, management structures.

**Characteristics**:

- Implemented through documentation, processes, organisational structures
- Involve policy development, role definition, governance
- Often require Management/HR/Legal resources

**Examples**:

- "Establish an information security policy approved by management"
- "Assign a Data Protection Officer responsible for monitoring compliance"
- "Conduct annual security awareness training for all employees"
- "Define roles and responsibilities for information security"
- "Establish information security governance structure"

**Maps To**: ISO 27001 Annex A Section 5 (Organisational Controls)

**Category 3: Reporting Requirements**

**Definition**: Requirements that relate to notifications, submissions, disclosures, external reporting.

**Characteristics**:

- Require communication to external parties (regulators, customers, data subjects)
- Often time-sensitive (e.g., notify within X hours)
- Involve compliance reporting, transparency

**Examples**:

- "Notify supervisory authority within 72 hours of data breach"
- "Submit annual compliance report to regulator"
- "Disclose data processing activities to data subjects in privacy notice"
- "Report security incidents to affected customers"
- "Notify data subjects of breaches affecting their rights"

**Maps To**: ISO 27001 Annex A Section 5.26 (Response to Information Security Incidents), 5.27 (Learning from Information Security Incidents)

**Category 4: Operational Requirements**

**Definition**: Requirements that relate to ongoing operations, monitoring, maintenance, testing, review activities.

**Characteristics**:

- Recurring activities (daily, monthly, quarterly, annually)
- Involve monitoring, testing, validation, continuous operations
- Often require Security Operations/IT Operations resources

**Examples**:

- "Monitor security logs daily for suspicious activity"
- "Test incident response plan annually"
- "Conduct regular vulnerability assessments"
- "Review and update risk assessments quarterly"
- "Perform regular backups and test restoration procedures"

**Maps To**: ISO 27001 Annex A Sections 5 and 8 (various operational controls like 5.37 Documented Operating Procedures, 8.8 Management of Technical Vulnerabilities)

## Assigning Categories

**For Each Extracted Requirement**:

**Step 1**: Read the requirement

**Step 2**: Ask: "What type of control will satisfy this requirement?"

- If answer is "technical control" → Technical
- If answer is "policy/procedure/governance" → Organisational
- If answer is "notification/report" → Reporting
- If answer is "ongoing activity/monitoring" → Operational

**Step 3**: Assign primary category

**Step 4**: If requirement spans multiple categories, assign secondary category

**Examples**:

| Requirement | Analysis | Primary Category | Secondary Category |
|-------------|----------|------------------|--------------------|
| "Implement encryption for data at rest" | Technical control (encryption technology) | Technical | - |
| "Establish incident response procedures" | Policy/procedure | Organisational | - |
| "Notify authority within 72 hours of breach" | External reporting | Reporting | - |
| "Test incident response plan annually" | Recurring testing activity | Operational | - |
| "Establish and test business continuity plan annually" | Establish (create plan) + Test (recurring activity) | Organisational | Operational |
| "Implement access controls and review access rights quarterly" | Technical (implement) + Operational (quarterly review) | Technical | Operational |

**Multiple Categories**:
Some requirements inherently span categories.

**Example**: "Establish incident response procedures and test them annually"

- Organisational (establish procedures = create documented process)
- Operational (test annually = recurring activity)
- **Assign**: Organisational (primary), Operational (secondary)

**Why Both Matter**:

- During control mapping, map to both organisational control (policy) and operational control (testing)
- Organisational control = ISMS-POL-5.26 Incident Response Policy
- Operational control = Annual incident response tabletop exercise

## Why Categorization Matters

**Benefit 1: Streamlines Control Mapping**

Knowing category narrows which Annex A controls to consider.

**Example**:

- Requirement Category: Technical
- Immediately focus on Annex A Section 8 (Technology Controls)
- Don't waste time reviewing Section 5 Organisational Controls (less likely to map)

**Benefit 2: Assigns Responsibility**

Categories correlate to organisational responsibilities.

| Category | Typical Responsible Party |
|----------|---------------------------|
| Technical | IT/Security Engineering |
| Organisational | ISMS Manager / Management / HR / Legal |
| Reporting | Compliance Officer / Legal / PR (for customer comms) |
| Operational | Security Operations / IT Operations |

**During implementation planning**: Use categories to assign owners.

**Benefit 3: Prioritization**

Some categories may be more urgent.

**Example Scenario**:

- Regulation effective in 6 months
- Reporting requirements (Category 3) may need immediate implementation (breach notification can't wait)
- Organisational requirements (policies, procedures) needed next (foundation for technical controls)
- Technical requirements follow (time to procure, deploy, configure)
- Operational requirements last (need controls implemented before you can test them)

**Benefit 4: Resource Planning**

Categories inform resource needs.

**Example**:

- 40 Technical requirements → Need Security Engineering capacity
- 15 Organisational requirements → Need Policy Development capacity (Compliance Officer, Legal)
- 5 Reporting requirements → Need Compliance Officer + Communications support
- 10 Operational requirements → Need Security Operations capacity

---

# Step 5 - Requirements Register Entry

**Purpose**: Populate the Requirements Register (master list) with all extracted requirements in structured format.

## Requirements Register Structure

**The Requirements Register** (Assessment Workbook 3) is the authoritative list of all regulatory requirements extracted from all applicable regulations.

**Register Fields** (Complete for Each Requirement):

**1. Requirement ID**:

- **Format**: REG-[RegCode]-[Article]-[Seq]
- **RegCode**: Short code for regulation (from ISMS-POL-00)
- **Article**: Article/Section number from regulation
- **Seq**: Sequential number (001, 002, 003...)
- **Examples**:
  - REG-GDPR-32-001 (First requirement from GDPR Article 32)
  - REG-HIPAA-164-001 (First requirement from HIPAA 45 CFR § 164)
  - REG-PCI-3-001 (First requirement from PCI DSS v4.0.1 Requirement 3)

**2. Regulation ID**:

- Link to entry in ISMS-POL-00
- **Example**: REG-GDPR (ID from POL-00)
- Enables filtering (show all requirements for one regulation)

**3. Regulation Name**:

- Full name for human readability
- **Example**: "General Data Protection Regulation (GDPR)"

**4. Citation**:

- Specific article, section, paragraph from regulation
- **Examples**:
  - "Article 32, Paragraph 1(a)"
  - "45 CFR § 164.308(a)(1)(i)"
  - "PCI DSS v4.0.1 Requirement 3.4"
- Enables looking up source text

**5. Original Requirement Text**:

- **Exact quote** from regulation (copy/paste)
- Preserves original legal language
- **Example**: "The controller and processor shall implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk..."
- Use quotation marks or italics to indicate this is verbatim quote

**6. Interpreted Requirement**:

- Your actionable rewrite (from Step 3)
- **Example**: "Implement technical and organisational security measures appropriate to the risk level of data processing activities"
- This is what [Organisation] will implement

**7. Requirement Category**:

- Technical / Organisational / Reporting / Operational (from Step 4)
- **Excel Implementation**: Dropdown list (data validation)

**8. Priority**:

- High / Medium / Low
- **Criteria**:
  - **High**: Tier 1 regulation + severe penalty for non-compliance + explicit deadline
  - **Medium**: Tier 1 but less severe consequence, or Tier 2 with potential near-term applicability
  - **Low**: Tier 2 or Tier 3, no imminent deadline
- **Excel Implementation**: Dropdown list

**9. Implementation Deadline**:

- Date by which requirement must be implemented
- **Sources**:
  - Regulation specifies deadline (e.g., "within 6 months of effective date")
  - Regulation effective date (if no specific deadline, assume effective date)
  - Risk-based deadline (if no regulatory deadline, [Organisation] determines based on risk)
- **Format**: YYYY-MM-DD
- **Example**: 2025-06-01

**10. Implementation Status**:

- Not Started / In Progress / Implemented / N/A
- **Initially**: "Not Started" for all extracted requirements
- **Updated**: As control mapping and implementation progress
- **Excel Implementation**: Dropdown list

**11. Mapped Controls**:

- ISO 27001 Annex A control(s) that satisfy this requirement
- **Initially**: Blank (populated during IMP-5.31.3 Control Mapping process)
- **Examples**: "A.8.24", "A.5.1, A.5.15", "A.8.16, A.8.17"
- Multiple controls possible (comma-separated)

**12. Gap Status**:

- Complete Gap / Partial Gap / No Gap / TBD
- **Initially**: "TBD" (determined during control mapping and gap analysis)
- **Updated**: During IMP-5.31.3
- **Excel Implementation**: Dropdown list

**13. Responsible Party**:

- Person/role who will implement this requirement
- **May be determined later** during control mapping (when know which control satisfies requirement, know who owns that control)
- **Examples**: "CISO", "IT Security Manager", "Compliance Officer", "HR Director"

**14. Notes**:

- Additional context, clarifications, assumptions, conditions
- **Examples**:
  - "Conditional requirement - applies only if processing special categories of data"
  - "Legal counsel confirmed this is mandatory despite 'should' language"
  - "Regulation doesn't define 'regular' - recommend quarterly at minimum"
- **Use for**: Capturing nuance that doesn't fit in other fields

**15. Extracted By / Date**:

- Name of person who extracted requirement
- Date of extraction
- **Example**: "Compliance Analyst / 2024-12-01"
- Accountability and audit trail

**16. Reviewed By / Date**:

- Legal or compliance reviewer
- Date of review
- **Example**: "Legal Counsel / 2024-12-05"
- Blank until review (Step 6)

**17. Approved By / Date**:

- Final approver (Compliance Officer, ISMS Manager)
- Date of approval
- Blank until final approval (Step 6)

## Populating the Register

**Process**:

**Before Starting**:

- Open Requirements Register (Excel template: Assessment Workbook 3)
- Save with version number (e.g., "Requirements-Register-v1.0-[RegCode].xlsx" for single regulation, or use master register for all regulations)

**For Each Extracted Requirement** (from Step 3):

1. **Create New Row** in register

2. **Assign Requirement ID**:

   - Check last requirement ID for this regulation
   - Increment sequence number
   - Example: Last was REG-GDPR-32-003, next is REG-GDPR-32-004

3. **Complete All Fields**:

   - Fill in Regulation ID, Regulation Name (copy from template or ISMS-POL-00)
   - Enter Citation (article/section from regulation)
   - Copy/paste Original Requirement Text (from regulation)
   - Enter Interpreted Requirement (your actionable rewrite)
   - Select Requirement Category (dropdown: Technical/Organisational/Reporting/Operational)
   - Assign Priority (dropdown: High/Medium/Low)
   - Enter Implementation Deadline (if known)
   - Set Implementation Status to "Not Started"
   - Leave Mapped Controls, Gap Status, Responsible Party blank (populated later)
   - Add Notes (if needed)
   - Enter "Extracted By" and "Date"

4. **Save** after each requirement (or after each article's requirements)

**Check for Duplicates**:

- Before adding requirement, check if similar requirement already exists
- Use Excel's Find function (Ctrl+F) to search for keywords
- If similar requirement exists:
  - **Same requirement from same article**: Don't duplicate; verify existing entry is correct
  - **Same requirement from different article**: Add cross-reference in Notes ("See also REG-GDPR-5-002 for related principle")

**Maintain Sequential IDs**:

- Within each article, number sequentially (001, 002, 003...)
- If inserting requirement later, use next available number (don't renumber existing; breaks references)
- Example: Article 32 has REQ-001 through REQ-005; later add REQ-006 (not REQ-003.5)

## Register Maintenance

**Version Control**:

**Initial Version**: 1.0 (when first created and approved)

**Minor Updates** (1.0 → 1.1 → 1.2):

- Add new requirements from same regulation
- Correct typos or minor clarifications
- Update status fields (In Progress, Implemented)

**Major Updates** (1.x → 2.0):

- Add requirements from new regulation
- Significant restructuring
- Major interpretation changes

**Version History Table** (in Excel, separate tab):

| Version | Date | Updated By | Changes |
|---------|------|------------|---------|
| 1.0 | 2024-12-10 | Compliance Officer | Initial extraction: GDPR Articles 5-50 (87 requirements) |
| 1.1 | 2024-12-15 | Compliance Analyst | Added GDPR Articles 51-59 (12 requirements); Legal review complete |
| 2.0 | 2025-01-15 | Compliance Officer | Added new regulation: CCPA (45 requirements) |

**Access Control**:

**Who Can Add/Edit Requirements**:

- Compliance Officer (full access)
- Legal Counsel (full access)
- Compliance Analysts (add/edit with Compliance Officer approval)

**Who Can View** (Read-Only):

- ISMS team
- Control owners (need to see requirements they'll implement)
- Auditors (demonstrate systematic extraction)
- Management

**Excel Implementation**:

- Store in SharePoint or shared drive with permissions
- OR: Use "Protect Sheet" feature with password (Edit access requires password)
- Track changes (Excel "Track Changes" or version control in SharePoint)

**Backup**:

- Requirements Register is critical document
- Backup daily (auto-backup if in SharePoint)
- Retain all versions (never delete old versions)

---

# Step 6 - Review & Validation

**Purpose**: Quality assurance before finalizing requirements extraction.

## Completeness Check

**Question**: Have we extracted ALL mandatory requirements from the regulation?

**Process**:

**Step 7.1.1**: Review regulation article-by-article against extraction worksheet

- For each article marked "Contains Obligations? Y", check corresponding requirements in register
- Confirm expected number of requirements extracted

**Step 7.1.2**: Search regulation for missed mandatory language

- Use PDF/document search: Find all instances of "shall", "must", "is required to"
- For each instance, verify corresponding requirement in register
- If "shall" found but no requirement extracted: Either (a) missed requirement, OR (b) in non-binding section (definitions, guidance) - verify

**Step 7.1.3**: Cross-check against extraction worksheet

- Extraction worksheet estimated # requirements per article
- Compare actual extracted count to estimate
- Significant variance (estimated 5, extracted 2)? → Review article again

**Step 7.1.4**: Peer Review

- Second person (Compliance Analyst or Legal) reviews extraction
- Fresh eyes catch missed requirements

**Red Flags**:

- Total requirements seems low compared to regulation length
- Entire articles skipped
- Complex article has only 1-2 requirements (may have missed nuance)

## Accuracy Check

**Question**: Are the extracted requirements faithful to the regulation?

**Process**:

**Step 7.2.1**: Compare interpreted requirement to original text

- For sample of requirements (10-20% of total, random selection):
  - Read original requirement text (from Register field 5)
  - Read interpreted requirement (from Register field 6)
  - Ask: Does interpreted requirement capture obligation from original?
  - Ask: Does interpreted requirement add anything not in original? (over-interpretation)
  - Ask: Does interpreted requirement omit anything from original? (under-interpretation)

**Step 7.2.2**: Check for over-interpretation

- **Red Flag Patterns**:
  - Interpreted requirement specifies technology not in regulation (e.g., regulation says "encryption", interpreted says "AES-256")
  - Interpreted requirement specifies frequency not in regulation (e.g., regulation says "regular", interpreted says "quarterly")
  - Interpreted requirement adds constraints (e.g., regulation says "access controls", interpreted says "role-based access control with separation of duties")

**If Over-Interpretation Found**:

- Revise interpreted requirement to remove added specificity
- Retain flexibility regulation provides

**Step 7.2.3**: Check for under-interpretation

- **Red Flag Patterns**:
  - Interpreted requirement less specific than regulation (e.g., regulation says "within 72 hours", interpreted says "promptly")
  - Interpreted requirement omits conditions (e.g., regulation says "unless unlikely to result in risk", interpreted omits exception)
  - Interpreted requirement generalizes where regulation is specific

**If Under-Interpretation Found**:

- Revise interpreted requirement to restore regulatory specificity
- Preserve all conditions, exceptions, qualifiers from regulation

**Step 7.2.4**: Verify consistent terminology

- Regulation uses specific terms (defined in definitions section)
- Interpreted requirements should use same terms consistently
- Example: If regulation defines "personal data", use "personal data" in requirements (not "PII", "personal information", "customer data")

## Granularity Check

**Question**: Are requirements actionable but not over-prescriptive?

**Review Against Guidelines** (from Section 4.1):

- Not too coarse: Can control owner understand what to do?
- Not too fine: Does requirement allow implementation flexibility?
- Just right: Specific WHAT, general HOW?

**Spot Check Method**:

- Select 5-10 requirements randomly
- For each, ask: "If I'm a control owner, can I implement this?"
- If answer is "No, too vague": Break down further (too coarse)
- If answer is "Yes, but I'm locked into very specific technology/process": Generalize (too fine)
- If answer is "Yes, I know what to do and have options for how": Just right ✓

**Common Fixes**:

**Too Coarse → Add Specificity**:

- Before: "Implement security controls"
- After: "Implement access controls to restrict information access to authorised individuals"

**Too Fine → Add Flexibility**:

- Before: "Implement AES-256 encryption in GCM mode with 256-bit keys"
- After: "Implement encryption using industry-standard algorithms appropriate to data sensitivity"

## Consistency Check

**Question**: Are all requirements written in consistent style and format?

**Checklist**:

☐ **All requirements start with action verb**:

- Review first word of each interpreted requirement
- Should be: Implement, Establish, Maintain, Conduct, Document, Ensure, Monitor, Review, Report
- Should NOT be: "The organisation shall...", "Organisations must...", "It is required that..."
- Fix: Revise to start with verb

☐ **All requirements use active voice**:

- ✅ "Implement encryption"
- ❌ "Encryption shall be implemented"
- Fix: Convert passive to active

☐ **All requirements properly scoped**:

- Check for context (where needed)
- "Implement encryption" → Too broad
- "Implement encryption for personal data in transit" → Properly scoped

☐ **All requirements have proper citations**:

- Every requirement links to article/section
- Citation format consistent
- Fix: Add missing citations, standardize format

☐ **Consistent terminology**:

- Same concept referred to same way across all requirements
- Example: Don't mix "personal data" (regulation term) with "PII" (US term) or "customer data" (colloquial)
- Fix: Standardize on regulatory terminology

☐ **Consistent priority logic**:

- All Tier 1 + severe penalty = High priority
- Check for inconsistencies (one Tier 1 requirement is Low while similar one is High)
- Fix: Align priority assignments

## Legal Review

**For Tier 1 Regulations** (Mandatory Compliance): Legal review is MANDATORY.

**Legal Counsel Responsibilities**:

**Review 1: Accuracy of Extraction**

- Verify all mandatory provisions extracted
- Confirm no provisions missed
- Check extraction worksheet completeness

**Review 2: Correct Interpretation**

- Verify interpreted requirements match regulatory intent
- Identify any misinterpretations
- Confirm granularity appropriate (not too specific, not too vague)

**Review 3: Legal Ambiguities**

- Flag any ambiguous provisions
- Provide interpretation guidance
- Recommend whether external legal opinion needed (e.g., novel regulatory concept, high stakes, unclear scope)

**Review 4: Categorization Accuracy**

- Verify Technical/Organisational/Reporting/Operational categories make sense
- Some requirements may be debatable (is "establish policy" Organisational or also Operational?)

**Review 5: Conditions and Exceptions**

- Verify conditional requirements properly extracted (if X, then Y)
- Verify exceptions properly noted (unless Z)
- Confirm no mandatory exceptions omitted

**Legal Approval**:

- Legal Counsel signs off on extraction
- Documented in Register: "Reviewed By" field
- OR: Separate Legal Review Memo attached to extraction

**Legal Caveats**:

- Legal Counsel may note: "Requirement X interpretation is [Legal Counsel]'s best judgment but regulation is ambiguous; recommend monitoring regulatory guidance"
- Document caveats in Requirements Register Notes field

**For Tier 2/3 Regulations**: Legal review may be optional

- ISMS Manager review may suffice
- Engage Legal if ambiguity or complexity warrants it

## Final Approval

**Approvers**:

**Compliance Officer**:

- Reviews for: Completeness, accuracy, consistency
- Confirms: All quality checks performed (Sections 7.1-7.4)
- Signs off: "Approved By" in Register

**Legal Counsel** (Tier 1):

- Reviews for: Legal accuracy, correct interpretation
- Signs off: "Reviewed By" in Register (already done in Section 7.5)

**ISMS Manager**:

- Reviews for: ISMS implications, implementability, control mapping readiness
- Signs off: Concurs with Compliance Officer approval

**Approval Documentation**:

**Option 1: Signatures in Requirements Register**

- "Reviewed By / Date" field: Legal Counsel signature and date
- "Approved By / Date" field: Compliance Officer signature and date
- Electronic signature acceptable (typed name + date)

**Option 2: Separate Approval Form**
```
REQUIREMENTS EXTRACTION APPROVAL

Regulation: [Regulation Name]
Regulation ID: [REG-XXX]
Requirements Extracted: [Count]

APPROVALS:
Extracted By: [Name] - [Date]
Reviewed By (Legal Counsel): [Name] - [Date] - Signature: _______
Approved By (Compliance Officer): [Name] - [Date] - Signature: _______
Concurrence (ISMS Manager): [Name] - [Date] - Signature: _______

Comments/Caveats: [If any]
```

**Once Approved**:

1. **Lock Requirements Register** (version control):

   - This becomes the approved baseline version
   - Example: Requirements-Register-v1.0-Approved-2024-12-10.xlsx
   - No further edits without creating new version

2. **Communicate Completion**:

   - Email to ISMS team: "Requirements extraction complete for [Regulation Name]; [X] requirements identified; proceeding to control mapping"

3. **Proceed to Next Step**:

   - Requirements extraction complete
   - Ready for IMP-5.31.3: Control Mapping Process

---

# Example Requirements Extractions

## Example 1: Data Protection Obligation

**Original Regulation Text** (Generic Example):
> "Article X: Organisations shall implement appropriate technical and organisational measures to ensure the security of personal data, including protection against unauthorised or unlawful processing and against accidental loss, destruction, or damage. Such measures shall include, as appropriate, encryption and access controls."

**Extraction Process**:

**Step 1: Identify Discrete Obligations**:

- Implement technical and organisational measures for data security
- Protect against unauthorised/unlawful processing
- Protect against accidental loss, destruction, damage
- Include encryption (as appropriate)
- Include access controls (as appropriate)

**Step 2: Extract & Rewrite**:

**REQ-001**: "Implement technical and organisational security measures to ensure the security of personal data"

- Action: Implement
- What: Technical and organisational measures
- Purpose: Security of personal data

**REQ-002**: "Implement controls to protect personal data against unauthorised or unlawful processing"

- Action: Implement controls
- Purpose: Prevent unauthorised/unlawful processing
- Context: Personal data

**REQ-003**: "Implement controls to protect personal data against accidental loss, destruction, or damage"

- Action: Implement controls
- Purpose: Prevent accidental loss/destruction/damage
- Context: Personal data

**REQ-004**: "Implement encryption for personal data where appropriate to reduce processing risk"

- Action: Implement encryption
- Context: Personal data
- Qualifier: "where appropriate" (from regulation - allows risk-based decision)

**REQ-005**: "Implement access controls to restrict personal data access to authorised individuals"

- Action: Implement access controls
- Purpose: Restrict access to authorised only
- Context: Personal data

**Step 3: Categorize**:

- REQ-001: Organisational (high-level security program)
- REQ-002: Technical (controls to prevent unauthorised processing)
- REQ-003: Technical (controls for availability/integrity)
- REQ-004: Technical (encryption)
- REQ-005: Technical (access management)

**Step 4: Register Entry** (Sample for REQ-001):

| Attribute | Value |
|-------|-------|
| Requirement ID | REG-DPA-X-001 |
| Regulation ID | REG-DPA |
| Regulation Name | Data Protection Act |
| Citation | Article X |
| Original Text | "Organisations shall implement appropriate technical and organisational measures to ensure the security of personal data, including protection against unauthorised or unlawful processing and against accidental loss, destruction, or damage. Such measures shall include, as appropriate, encryption and access controls." |
| Interpreted Requirement | Implement technical and organisational security measures to ensure the security of personal data |
| Category | Organisational |
| Priority | High |
| Implementation Deadline | 2025-06-01 |
| Implementation Status | Not Started |
| Mapped Controls | [TBD - during IMP-5.31.3] |
| Gap Status | TBD |
| Responsible Party | CISO |
| Notes | Foundational requirement; specific measures detailed in REQ-002 through REQ-005 |
| Extracted By / Date | Compliance Analyst / 2024-12-01 |
| Reviewed By / Date | Legal Counsel / 2024-12-05 |
| Approved By / Date | Compliance Officer / 2024-12-10 |

[Repeat structure for REQ-002 through REQ-005]

---

## Example 2: Incident Reporting Obligation

**Original Regulation Text** (Generic Example):
> "Section Y: In the event of a security breach affecting personal data, the organisation must notify the relevant supervisory authority without undue delay and, where feasible, no later than 72 hours after becoming aware of the breach, unless the breach is unlikely to result in a risk to the rights and freedoms of individuals."

**Extraction Process**:

**Step 1: Identify Obligation**:

- Notify supervisory authority of security breach
- Timeline: "Without undue delay" AND "no later than 72 hours" (where feasible)
- Scope: Breaches affecting personal data
- Exception: Unless breach unlikely to result in risk to individuals

**Step 2: Extract & Rewrite**:

**REQ-001**: "Notify the relevant supervisory authority of security breaches affecting personal data within 72 hours of becoming aware of the breach, unless the breach is unlikely to result in risk to the rights and freedoms of individuals"

- Action: Notify
- Who: Supervisory authority
- What: Security breaches affecting personal data
- When: Within 72 hours of awareness
- Exception: Unless unlikely to result in risk
- Note: Preserves all elements of obligation including timeline and exception

**Step 3: Categorize**:

- Category: **Reporting** (external notification requirement)

**Step 4: Register Entry**:

| Attribute | Value |
|-------|-------|
| Requirement ID | REG-DPA-Y-001 |
| Regulation ID | REG-DPA |
| Regulation Name | Data Protection Act |
| Citation | Section Y |
| Original Text | "In the event of a security breach affecting personal data, the organisation must notify the relevant supervisory authority without undue delay and, where feasible, no later than 72 hours after becoming aware of the breach, unless the breach is unlikely to result in a risk to the rights and freedoms of individuals." |
| Interpreted Requirement | Notify the relevant supervisory authority of security breaches affecting personal data within 72 hours of becoming aware of the breach, unless the breach is unlikely to result in risk to the rights and freedoms of individuals |
| Category | Reporting |
| Priority | High |
| Implementation Deadline | 2025-06-01 (regulation effective date) |
| Implementation Status | Not Started |
| Mapped Controls | [TBD - likely A.5.26 Response to Information Security Incidents] |
| Gap Status | TBD |
| Responsible Party | Compliance Officer / Incident Response Manager |
| Notes | Requires: (1) Incident detection capability to "become aware", (2) Incident response procedures including breach assessment (to determine if "unlikely to result in risk"), (3) Authority contact information, (4) Notification templates. Timeline is critical (72 hours). |
| Extracted By / Date | Compliance Analyst / 2024-12-01 |
| Reviewed By / Date | Legal Counsel / 2024-12-05 |
| Approved By / Date | Compliance Officer / 2024-12-10 |

---

## Example 3: Organisational Requirement

**Original Regulation Text** (Generic Example):
> "Article Z: Organisations processing personal data shall designate a Data Protection Officer responsible for monitoring compliance with this regulation, advising on data protection matters, and serving as the point of contact for data subjects and the supervisory authority regarding processing activities."

**Extraction Process**:

**Step 1: Identify Obligations**:

- Designate a Data Protection Officer (DPO)
- DPO responsibility 1: Monitor compliance with regulation
- DPO responsibility 2: Advise on data protection matters
- DPO responsibility 3: Serve as point of contact for data subjects
- DPO responsibility 4: Serve as point of contact for supervisory authority

**Step 2: Extract & Rewrite**:

**REQ-001**: "Designate a Data Protection Officer responsible for monitoring compliance with data protection regulation"

- Action: Designate
- Role: Data Protection Officer
- Responsibility: Monitor compliance

**REQ-002**: "Ensure DPO advises the organisation on data protection matters"

- Action: Ensure
- Who: DPO
- Responsibility: Advise on data protection

**REQ-003**: "Ensure DPO serves as point of contact for data subjects and supervisory authority regarding data processing activities"

- Action: Ensure
- Who: DPO
- Responsibility: Point of contact
- For whom: Data subjects and supervisory authority
- Regarding: Processing activities

**Step 3: Categorize**:

- REQ-001: **Organisational** (role designation)
- REQ-002: **Organisational** (governance function)
- REQ-003: **Organisational** (communication/interface role)

**Step 4: Register Entry** (Sample for REQ-001):

| Attribute | Value |
|-------|-------|
| Requirement ID | REG-DPA-Z-001 |
| Regulation ID | REG-DPA |
| Regulation Name | Data Protection Act |
| Citation | Article Z |
| Original Text | "Organisations processing personal data shall designate a Data Protection Officer responsible for monitoring compliance with this regulation, advising on data protection matters, and serving as the point of contact for data subjects and the supervisory authority regarding processing activities." |
| Interpreted Requirement | Designate a Data Protection Officer responsible for monitoring compliance with data protection regulation |
| Category | Organisational |
| Priority | High |
| Implementation Deadline | 2025-06-01 |
| Implementation Status | Not Started |
| Mapped Controls | [TBD - likely new org-specific control or adapted from A.5.2 Information Security Roles and Responsibilities] |
| Gap Status | TBD |
| Responsible Party | Executive Management (designates DPO) |
| Notes | Check if organisation meets threshold requiring DPO designation. If required, DPO must have appropriate expertise and independence. Consider whether internal or external DPO. REQ-002 and REQ-003 define DPO responsibilities. |
| Extracted By / Date | Compliance Analyst / 2024-12-01 |
| Reviewed By / Date | Legal Counsel / 2024-12-05 |
| Approved By / Date | Compliance Officer / 2024-12-10 |

[REQ-002 and REQ-003 would have similar entries]

---

## Example 4: Operational Requirement

**Original Regulation Text** (Generic Example):
> "Section W: Organisations shall conduct regular testing and evaluation of the effectiveness of technical and organisational measures implemented to ensure the security of data processing."

**Extraction Process**:

**Step 1: Identify Obligation**:

- Conduct regular testing and evaluation
- Focus: Effectiveness of security measures
- Scope: Technical and organisational measures

**Step 2: Extract & Rewrite**:

**REQ-001**: "Conduct regular testing and evaluation of the effectiveness of security controls for data processing"

- Action: Conduct
- What: Testing and evaluation
- Of what: Effectiveness of security controls
- Frequency: "Regular" (regulation doesn't define; [Organisation] will determine)
- Scope: Data processing security

**Step 3: Categorize**:

- Category: **Operational** (recurring testing activity)

**Step 4: Register Entry**:

| Attribute | Value |
|-------|-------|
| Requirement ID | REG-DPA-W-001 |
| Regulation ID | REG-DPA |
| Regulation Name | Data Protection Act |
| Citation | Section W |
| Original Text | "Organisations shall conduct regular testing and evaluation of the effectiveness of technical and organisational measures implemented to ensure the security of data processing." |
| Interpreted Requirement | Conduct regular testing and evaluation of the effectiveness of security controls for data processing |
| Category | Operational |
| Priority | Medium |
| Implementation Deadline | 2025-06-01 (initial implementation); ongoing thereafter |
| Implementation Status | Not Started |
| Mapped Controls | [TBD - likely A.5.37 Documented Operating Procedures, A.8.8 Management of Technical Vulnerabilities] |
| Gap Status | TBD |
| Responsible Party | CISO / Security Operations Manager |
| Notes | "Regular" not defined by regulation. Recommend: (1) Annual penetration testing, (2) Quarterly vulnerability scanning, (3) Annual controls testing (internal audit), (4) Continuous monitoring via security operations. Frequency to be defined in implementation procedures based on risk. |
| Extracted By / Date | Compliance Analyst / 2024-12-01 |
| Reviewed By / Date | Legal Counsel / 2024-12-05 |
| Approved By / Date | Compliance Officer / 2024-12-10 |

---

# Templates & Tools

## Requirements Register Template

**Reference**: Assessment Workbook 3 (Requirements Extraction) provides complete Excel template.

**Template Features**:

- All 17 fields (per Section 6.1)
- Data validation (dropdowns for Category, Priority, Status, Gap Status)
- Conditional formatting (color-code by Priority: Red = High, Yellow = Medium, Green = Low)
- Filter controls (filter by Regulation, Category, Priority, Status)
- Summary formulas:
  - Total requirements count
  - Count by Category
  - Count by Priority
  - Count by Status
  - Count by Gap Status
- Version control tab
- Instructions tab

## Extraction Worksheet Template

**Purpose**: Working document to track extraction progress article-by-article.

**Template** (Spreadsheet):

| Article # | Article Title | Summary | Contains Obligations? | Est. # Reqs | Complexity | Legal Review? | Status | Notes |
|-----------|---------------|---------|----------------------|-------------|------------|--------------|--------|-------|
| [Number] | [Title] | [1-2 sentence summary] | Y / N | [#] | S / M / C | Y / N | Not Started / In Progress / Complete | [Notes] |

**Instructions**:
1. Create row for each article/section in regulation
2. First pass: Complete Article #, Title, Summary, Contains Obligations
3. Second pass: For articles with obligations, estimate # requirements, assess complexity, determine if legal review needed
4. During extraction: Update Status as you work through articles
5. Use Notes for questions, issues, decisions

**Usage**: Working document during extraction (Steps 1-5); filed with final extraction documentation as audit trail

## Requirement ID Numbering Cheatsheet

**Standard Convention**: REG-[RegCode]-[Article]-[Seq]

**Component Breakdown**:

- **REG**: Prefix indicating "Requirement from Regulation"
- **RegCode**: Short code for regulation (from ISMS-POL-00)
  - Examples: GDPR, CCPA, HIPAA, SOX, PCI, ISO27001, NIST
  - Keep short (3-8 characters)
- **Article**: Article, Section, or Requirement number from regulation
  - Use regulation's numbering
  - If regulation uses decimal notation (e.g., 3.4.1), replace periods with hyphens (3-4-1)
- **Seq**: Sequential number (001, 002, 003...)
  - Always 3 digits (leading zeros)
  - Unique within Article

**Examples**:

| Regulation | Article/Section | Requirement ID | Notes |
|------------|----------------|----------------|-------|
| GDPR | Article 32 | REG-GDPR-32-001 | First requirement from GDPR Article 32 |
| HIPAA | 45 CFR § 164.308 | REG-HIPAA-164-001 | Use just "164" (section number) |
| PCI DSS v4.0.1 | Requirement 3.4 | REG-PCI-3-4-001 | Decimal becomes hyphen |
| SOX | Section 404 | REG-SOX-404-001 | Section 404 |
| NIST CSF 2.0 | Function: Protect | REG-NIST-PR-001 | Use function abbreviation |

**If Regulation Doesn't Have Article Numbers**:

- Use section titles abbreviated
- OR: Number sequentially by order in document
- Consistency matters more than specific convention

**If Requirement from Annex/Schedule**:

- Format: REG-[RegCode]-ANNEX[X]-[Seq]
- Example: REG-GDPR-ANNEXA-001

---

# Quality Checks & Common Pitfalls

## Quality Checklist

Before submitting for final approval (Step 6), perform these checks:

**Completeness**:

- ☐ All articles/sections reviewed (checked against extraction worksheet)
- ☐ All "shall" and "must" statements extracted
- ☐ No obvious gaps (compare estimated vs. actual requirement count)

**Accuracy**:

- ☐ Interpreted requirements faithful to original text (spot-checked per Section 7.2)
- ☐ No over-interpretation (no added requirements)
- ☐ No under-interpretation (no omitted obligations)
- ☐ Proper citations (every requirement links to article/section)

**Actionability**:

- ☐ Requirements rewritten in actionable form (action verb, active voice)
- ☐ Granularity appropriate (not too coarse, not too fine - spot-checked per Section 7.3)
- ☐ Implementable by control owners

**Consistency**:

- ☐ Requirements categorized (Technical/Organisational/Reporting/Operational)
- ☐ Requirements prioritized (High/Medium/Low)
- ☐ Consistent terminology (regulatory terms used consistently)
- ☐ Consistent formatting (all start with action verb, etc.)

**Documentation**:

- ☐ All Requirements Register fields completed
- ☐ Requirement IDs sequential and correct
- ☐ No duplicate requirements
- ☐ Extraction worksheet filed

**Review & Approval**:

- ☐ Legal review completed (for Tier 1) and documented
- ☐ Compliance Officer approval obtained
- ☐ ISMS Manager concurrence obtained
- ☐ Approval signatures/dates in Register

**Readiness for Next Step**:

- ☐ Requirements Register version controlled and locked
- ☐ Ready to proceed to Control Mapping (IMP-5.31.3)

## Common Pitfalls to Avoid

**Pitfall 1: Extracting Too Coarsely**

**Mistake**: "Comply with Article 32" is not a requirement.

**Why Wrong**: Doesn't tell control owner what to do. Can't map to specific control. Not measurable.

**Correct Approach**: Break Article 32 into specific obligations:

- Implement technical security measures
- Implement organisational security measures
- Implement encryption (where appropriate)
- Ensure CIA+R of systems
- Etc.

**Pitfall 2: Extracting Too Finely (Over-Specifying)**

**Mistake**: Regulation says "implement encryption", extracted requirement says "implement AES-256 encryption in GCM mode with SHA-384 HMAC and 256-bit keys rotated quarterly".

**Why Wrong**: Regulation doesn't require that level of specificity. Locks [Organisation] into specific technology that may become obsolete. Limits flexibility.

**Correct Approach**: "Implement encryption for data at rest using industry-standard algorithms appropriate to data sensitivity" - Preserves obligation, allows implementation flexibility.

**Pitfall 3: Adding Requirements Not in Regulation**

**Mistake**: Regulation requires "access controls". Extracted requirements include "role-based access control", "separation of duties", "quarterly access reviews", "least privilege" - none of which are in regulation.

**Why Wrong**: Over-interpretation. Adding obligations regulation doesn't impose.

**Correct Approach**: Extract what regulation says: "Implement access controls to restrict information access to authorised individuals". If [Organisation] chooses to implement RBAC, SoD, quarterly reviews - that's implementation decision during control mapping, not regulatory requirement.

**When in Doubt**: Ask "Did the regulation say this, or did I infer it?" If inferred, don't extract.

**Pitfall 4: Missing Conditional Requirements**

**Mistake**: Regulation says "If processing special categories of data, implement additional safeguards". Extraction skips it thinking "we don't process special categories, so not applicable".

**Why Wrong**: [Organisation] may process special categories in future. OR: [Organisation] does process them but extractor didn't realise. Conditional requirements are still requirements.

**Correct Approach**: Extract as "Implement additional safeguards for special categories of personal data (when processing such data)". Note condition in Notes field. During control mapping, assess if condition met.

**Pitfall 5: Ignoring Regulatory Context**

**Mistake**: Extracting requirements in isolation without reading definitions, scope, or related articles.

**Example**: Regulation defines "processing" as "collection, storage, use, transmission, deletion". Extractor reads Article 25 "Organisations shall implement security for processing" and extracts requirement as "Implement security for data storage".

**Why Wrong**: "Processing" includes more than storage (also collection, use, transmission, deletion). Requirement should cover all processing operations per regulatory definition.

**Correct Approach**: Read definitions first. Use regulatory terminology. Extract as "Implement security controls for all personal data processing operations (collection, storage, use, transmission, deletion)".

**Pitfall 6: Inconsistent Categorization**

**Mistake**: Similar requirements categorized differently.

- "Establish incident response policy" → Organisational
- "Establish access control policy" → Technical

**Why Wrong**: Both are "establish policy" (organisational activity). Inconsistency creates confusion during control mapping.

**Correct Approach**: Apply categorization guidelines consistently.

- "Establish incident response policy" → Organisational
- "Establish access control policy" → Organisational
- "Implement access controls" → Technical (implementation distinct from policy)

**Pitfall 7: Skipping Legal Review for Tier 1 Regulations**

**Mistake**: Compliance team extracts requirements from Tier 1 mandatory regulation and proceeds to control mapping without legal review.

**Why Wrong**: Legal interpretation critical. Misinterpretation of mandatory regulation creates compliance risk. Non-lawyers may miss legal nuance.

**Correct Approach**: ALWAYS engage legal counsel for Tier 1 extraction. Legal reviews accuracy, confirms interpretation, signs off. Non-negotiable.

---

# Related Documents & References

**Policy Documents**:

- **ISMS-POL-A.5.31.3**: Requirements Extraction & Control Mapping Framework
  - Defines the extraction methodology this guide operationalizes
  - Section 2: Requirements Extraction Process (methodology)
- **ISMS-POL-00**: Regulatory Applicability Framework
  - Source of applicable regulations (input to this process)

**Implementation Guides** (Process Sequence):

- **ISMS-IMP-A.5.31.2**: Applicability Assessment Process
  - PRECEDES this step (determines which regulations apply)
- **ISMS-IMP-A.5.31.4**: Control Mapping Process
  - FOLLOWS this step (maps extracted requirements to ISO 27001 controls)

**Assessment Tools**:

- **Assessment Workbook 3**: Requirements Extraction (Excel template)
  - Requirements Register template (implements Section 6)
  - Pre-configured with fields, dropdowns, formulas
  - Used to populate master Requirements Register

**Standards**:

- **ISO 27001:2022**: Control A.5.31 - Legal, Statutory, Regulatory and Contractual Requirements
  - The ISO control this process supports

---

**END OF IMPLEMENTATION GUIDE**

---

*This operational guide provides step-by-step instructions for extracting actionable requirements from regulatory text, enabling [Organisation] to systematically translate legal obligations into implementable security controls with full traceability and audit readiness.*

---

**END OF USER GUIDE**

---

*"The difference between something good and something great is attention to detail."*
— Charles R. Swindoll

<!-- QA_VERIFIED: 2026-03-01 -->
