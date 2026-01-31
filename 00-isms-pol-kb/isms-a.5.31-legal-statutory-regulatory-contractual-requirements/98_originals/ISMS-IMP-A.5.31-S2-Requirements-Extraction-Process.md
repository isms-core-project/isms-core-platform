# ISMS-IMP-A.5.31-S2: Requirements Extraction Process
## SKELETON WITH WRITING INSTRUCTIONS

**Status**: SKELETON - Ready for content development  
**Target Length**: 8-10 pages  
**Purpose**: Step-by-step operational guide for extracting actionable requirements from regulations

**Related Policy**: ISMS-POL-A.5.31-S3 (Requirements Mapping Framework)

---

## SECTION 1: Process Overview

### WRITING INSTRUCTIONS:
Provide high-level overview of requirements extraction process.

### KEY CONTENT:
- **Purpose**: Translate regulatory text into actionable requirements that can be mapped to controls
- **When Used**: After regulation determined applicable (IMP-S1 complete)
- **Who Performs**: Compliance Officer, Legal, ISMS specialists working together
- **Output**: Requirements Register populated with extracted requirements

### INCLUDE:
- **Process Flowchart**:
  ```
  [Applicable Regulation (from IMP-S1)]
      ↓
  [Step 1: Parse Regulation Structure]
      ↓
  [Step 2: Identify Mandatory Requirements]
      ↓
  [Step 3: Extract & Rewrite in Actionable Form]
      ↓
  [Step 4: Categorize Requirements]
      ↓
  [Step 5: Register Entry]
      ↓
  [Step 6: Review & Validation]
      ↓
  [Requirements Register Updated]
  ```

- **Typical Timeline**: 
  - Simple regulation (10-20 requirements): 1-2 weeks
  - Complex regulation (50+ requirements): 4-6 weeks
  - Depends on regulation length and complexity

- **Key Artifacts**:
  - Requirements Register (master list)
  - Regulatory text (source document)
  - Extraction worksheets
  - Legal review notes

**Estimated Length**: 1-2 pages

---

## SECTION 2: Step 1 - Parse Regulation Structure

### WRITING INSTRUCTIONS:
Teach users how to read and understand regulatory structure systematically.

### KEY CONTENT:

#### 2.1 Understanding Regulatory Structure

**Regulations Typically Have:**
- **Articles/Sections**: Major divisions
- **Sub-sections/Paragraphs**: Subdivisions of articles
- **Clauses**: Specific provisions
- **Annexes/Schedules**: Supplementary details
- **Definitions**: Key terms (important for interpretation)
- **Scope/Applicability**: Who/what is covered
- **Obligations**: The "shall" statements
- **Guidance/Commentary**: Explanatory notes (not mandatory)

#### 2.2 Reading Systematically

**Process:**
1. **Read Definitions First**
   - Understand how regulation defines key terms
   - Example: What is "personal data"? "Security incident"? "Processing"?
   - Note: Definitions vary by regulation

2. **Read Scope/Applicability**
   - Who must comply (already assessed in IMP-S1, but reconfirm)
   - What activities are covered
   - Any exemptions or thresholds

3. **Read Articles in Order**
   - Don't jump around
   - Articles often build on each other
   - Note cross-references between articles

4. **Identify Structure**
   - Number of articles/sections
   - Which articles contain obligations vs. definitions vs. penalties
   - Create outline/table of contents if not provided

#### 2.3 Marking Up the Regulation

**Physical or Digital Markup:**
- **Highlight Mandatory Language**: "shall", "must", "is required to"
- **Underline Key Requirements**: Specific obligations
- **Bracket Definitions**: Important terms
- **Note Cross-References**: "As defined in Article X..."
- **Flag Unclear Sections**: May need legal interpretation

#### 2.4 Creating Extraction Worksheet

**For Each Article/Section, Note:**
- Article Number/Title
- Summary (1-2 sentences)
- Number of requirements identified
- Complexity (Simple/Moderate/Complex)
- Need for legal review? (Y/N)

**This worksheet guides the extraction work.**

**Estimated Length**: 2 pages

---

## SECTION 3: Step 2 - Identify Mandatory vs. Recommendatory Language

### WRITING INSTRUCTIONS:
Teach users to distinguish mandatory requirements from recommendations.

### KEY CONTENT:

#### 3.1 Mandatory Language

**Indicates OBLIGATION** - must extract as requirement:

- **"Shall"**: Strongest mandatory language
  - Example: "The organization shall implement encryption..."
  - Action: Extract as mandatory requirement

- **"Must"**: Also mandatory
  - Example: "Access controls must be in place..."
  - Action: Extract as mandatory requirement

- **"Is required to" / "Are required to"**
  - Example: "Organizations are required to conduct risk assessments..."
  - Action: Extract as mandatory requirement

- **"Will"** (in context of obligations)
  - Example: "The processor will notify the controller..."
  - Action: Extract as mandatory requirement

#### 3.2 Recommendatory Language

**Indicates GUIDANCE** - note but don't extract as mandatory requirement:

- **"Should"**: Recommended but not mandatory
  - Example: "Organizations should consider multi-factor authentication..."
  - Action: Note as best practice, not mandatory requirement

- **"May"**: Optional/permissive
  - Example: "Organizations may appoint a DPO..."
  - Action: Optional, note but don't extract unless context indicates obligation

- **"Is encouraged to" / "Is advised to"**: Guidance
  - Example: "Organizations are encouraged to adopt..."
  - Action: Note as guidance

- **"Recommended" / "Suggested"**
  - Action: Note as best practice

#### 3.3 Contextual Interpretation

**Some language requires context:**

- **"Should" in context of "should be" + detailed specification**
  - May actually be mandatory despite "should"
  - Example: "Password complexity should be: minimum 12 characters, upper/lower/number/symbol"
  - The detailed specification suggests mandatory
  - Action: Consult legal counsel, may extract as requirement

- **"Or"** - Alternatives
  - Example: "Encryption or pseudonymization"
  - Action: Extract as requirement with alternatives

- **Conditional Requirements**
  - "If X, then shall Y"
  - Action: Extract with condition noted

#### 3.4 When in Doubt

**If uncertain whether mandatory:**
- Err on side of caution: Extract it
- Flag for legal review
- Better to have and not need than need and not have

**Estimated Length**: 2 pages

---

## SECTION 4: Step 3 - Extract & Rewrite in Actionable Form

### WRITING INSTRUCTIONS:
This is the CORE skill - transforming legal text into actionable requirements.

### KEY CONTENT:

#### 4.1 Granularity Guidelines (Reference POL-S3)

**Too Coarse - NOT Actionable:**
- "Comply with Article 32"
- "Implement security measures"
- "Ensure data protection"

**Problem**: Too vague, can't map to specific controls

**Too Fine - TOO Prescriptive:**
- "Use AES-256 encryption with CBC mode and PKCS7 padding"
- "Configure firewall rule: deny TCP port 23"
- "Store logs for exactly 395 days"

**Problem**: Limits implementation flexibility, may become outdated

**Just Right - Actionable with Flexibility:**
- "Implement encryption for data at rest using industry-standard algorithms and key lengths appropriate to data sensitivity"
- "Restrict administrative access to necessary ports only, denying unnecessary services"
- "Retain security logs for a minimum of 12 months or as required by regulation"

**Goal**: Specific enough to implement, flexible enough to adapt

#### 4.2 Extraction Technique

**For Each Mandatory Provision:**

**Original Regulation Text Example:**
> "Article 32(1): The controller and processor shall implement appropriate technical and organizational measures to ensure a level of security appropriate to the risk, including inter alia as appropriate:
> (a) pseudonymization and encryption of personal data;
> (b) the ability to ensure ongoing confidentiality, integrity, availability and resilience of processing systems and services;"

**Extraction Process:**

1. **Identify Discrete Obligations**:
   - Obligation 1: Implement technical and organizational security measures
   - Obligation 2: Measures must be risk-appropriate
   - Obligation 3: Includes pseudonymization and encryption
   - Obligation 4: Ensure confidentiality, integrity, availability, resilience

2. **Rewrite Each in Actionable Form**:
   - REQ-1: "Implement technical and organizational security measures appropriate to the risk level of data processing activities"
   - REQ-2: "Implement pseudonymization or encryption controls for personal data to reduce risk"
   - REQ-3: "Implement controls to ensure ongoing confidentiality, integrity, availability, and resilience of information systems"

3. **Maintain Citation**:
   - Each requirement links back to Article 32(1)

#### 4.3 Writing Actionable Requirements

**Best Practices:**

**Use Active Voice:**
- Good: "Implement access controls..."
- Poor: "Access controls should be implemented..." (passive)

**Start with Action Verb:**
- Implement, Establish, Maintain, Conduct, Document, Ensure, Monitor, etc.

**Be Specific About WHAT, General About HOW:**
- Specific: "Implement authentication for system access"
- General HOW: "using passwords, biometrics, tokens, or other appropriate mechanisms"

**Include Context When Needed:**
- "Implement encryption for personal data in transit over untrusted networks"
- The context ("in transit over untrusted networks") scopes the requirement

**Avoid Duplication:**
- If regulation says same thing multiple times, extract once

**Avoid Over-Interpretation:**
- Don't add requirements not in the regulation
- Stick to what's written

#### 4.4 Handling Special Cases

**Conditional Requirements:**
- "If processing special categories of data, then implement additional safeguards"
- Extract: "Implement additional safeguards for special categories of data (when applicable)"

**Requirements with Alternatives:**
- "Encryption or pseudonymization"
- Extract: "Implement encryption or pseudonymization for personal data"

**Requirements with Examples ("Including but not limited to..."):**
- Examples are illustrative, not exhaustive
- Extract general requirement, note examples
- Extract: "Implement technical security measures (e.g., encryption, access control, network security)"

**Quantitative Requirements:**
- "Notify within 72 hours"
- Extract: "Notify [authority] within 72 hours of becoming aware of incident"
- Keep the specific number

**Estimated Length**: 2-3 pages

---

## SECTION 5: Step 4 - Categorize Requirements

### WRITING INSTRUCTIONS:
Teach users the categorization framework from POL-S3 Section 2.2.

### KEY CONTENT:

#### 5.1 Requirement Categories

**Technical Requirements:**
- Relate to systems, technology, security controls
- Examples:
  - "Implement encryption for data at rest"
  - "Configure firewalls to restrict unauthorized access"
  - "Deploy intrusion detection systems"
- **Why Categorize**: Maps to technical controls (A.8.x)

**Organizational Requirements:**
- Relate to policies, procedures, governance, roles
- Examples:
  - "Establish an information security policy"
  - "Assign a Data Protection Officer"
  - "Conduct annual security training"
- **Why Categorize**: Maps to organizational controls (A.5.x)

**Reporting Requirements:**
- Relate to notifications, submissions, disclosures
- Examples:
  - "Notify authority within 72 hours of breach"
  - "Submit annual compliance report"
  - "Disclose data processing activities to data subjects"
- **Why Categorize**: Maps to incident management and reporting controls (A.5.26-27)

**Operational Requirements:**
- Relate to ongoing operations, monitoring, maintenance
- Examples:
  - "Monitor security logs daily"
  - "Test incident response plan annually"
  - "Conduct regular vulnerability assessments"
- **Why Categorize**: Maps to operational controls (A.8.x)

#### 5.2 Assigning Categories

**For each extracted requirement:**
1. Read the requirement
2. Ask: What type of control will satisfy this?
3. Assign primary category (may have secondary)
4. Document in Requirements Register

**Multiple Categories Possible:**
- Some requirements span categories
- Example: "Establish and maintain incident response procedures and test them annually"
  - Organizational (establish procedures)
  - Operational (test them)
- Assign: Organizational (primary), Operational (secondary)

#### 5.3 Why Categorization Matters

- **Streamlines Control Mapping**: Know which Annex A sections to focus on
- **Assigns Responsibility**: Technical → IT, Organizational → Management, etc.
- **Prioritization**: Some categories may be more urgent than others

**Estimated Length**: 1-2 pages

---

## SECTION 6: Step 5 - Requirements Register Entry

### WRITING INSTRUCTIONS:
Define how to populate the Requirements Register (reference Assessment Workbook 3).

### KEY CONTENT:

#### 6.1 Requirements Register Structure

**The Register is the master list of all extracted requirements.**

**Fields to Complete for Each Requirement:**

1. **Requirement ID**: 
   - Format: REG-[RegCode]-[Article]-[Seq]
   - Example: REG-GDPR-32-001
   - Explanation: First requirement from GDPR Article 32

2. **Regulation ID**:
   - Link to ISMS-POL-00 entry
   - Example: REG-GDPR

3. **Regulation Name**:
   - Full name
   - Example: "General Data Protection Regulation (GDPR)"

4. **Citation**:
   - Specific article, section, paragraph
   - Example: "Article 32, Paragraph 1(a)"

5. **Original Requirement Text**:
   - Exact quote from regulation
   - Copy/paste from regulatory text

6. **Interpreted Requirement**:
   - Your actionable rewrite
   - Example: "Implement encryption for personal data at rest using industry-standard algorithms"

7. **Requirement Category**:
   - Technical / Organizational / Reporting / Operational
   - Select from dropdown (in Excel template)

8. **Priority**:
   - High / Medium / Low
   - Based on regulation tier and consequence of non-compliance

9. **Implementation Deadline**:
   - If regulation specifies deadline
   - If not specified: based on regulation effective date

10. **Implementation Status**:
    - Not Started / In Progress / Implemented / N/A
    - Initially "Not Started"

11. **Responsible Party**:
    - Who will implement this requirement
    - May be determined later during control mapping

12. **Notes**:
    - Additional context, clarifications, assumptions

13. **Extracted By / Date**:
    - Name of person who extracted requirement
    - Date of extraction

14. **Reviewed By / Date**:
    - Legal or compliance reviewer
    - Date of review

#### 6.2 Populating the Register

**Process:**
1. Open Requirements Register (Excel or database)
2. For each extracted requirement:
   - Create new row
   - Complete all fields
   - Save
3. Ensure no duplicate requirements (check before adding)
4. Maintain sequential requirement IDs per regulation

#### 6.3 Register Maintenance

**Version Control:**
- Register is version controlled
- Each time updated: increment version number
- Track changes in version history

**Access Control:**
- Who can add requirements: Compliance Officer, Legal
- Who can edit: Same
- Who can view: ISMS team, control owners (read-only)

**Estimated Length**: 2 pages

---

## SECTION 7: Step 6 - Review & Validation

### WRITING INSTRUCTIONS:
Define the quality assurance process for requirements extraction.

### KEY CONTENT:

#### 7.1 Completeness Check

**Ensure ALL mandatory requirements extracted:**
- Review regulation article-by-article
- Check: Any "shall" or "must" missed?
- Cross-reference against extraction worksheet
- Compare total extracted vs. initial estimate

#### 7.2 Accuracy Check

**Ensure requirements faithful to regulation:**
- Compare interpreted requirement to original text
- Check: Does interpretation match regulatory intent?
- Check: Any added requirements not in regulation? (Over-interpretation)
- Check: Any diluted requirements? (Under-interpretation)

**Red Flags:**
- Requirement more stringent than regulation says
- Requirement less stringent than regulation says
- Requirement introduces concepts not in regulation

#### 7.3 Granularity Check

**Ensure requirements are actionable but not too prescriptive:**
- Review against granularity guidelines (Section 4.1)
- Too coarse? Break down further
- Too fine? Generalize to allow implementation flexibility

#### 7.4 Consistency Check

**Ensure consistent style and format:**
- All requirements start with action verb?
- All requirements use active voice?
- All requirements scoped appropriately?
- All requirements have proper citations?

#### 7.5 Legal Review

**For Tier 1 regulations (mandatory compliance):**
- **Legal Counsel Reviews**:
  - Accuracy of extraction
  - Correct interpretation of legal language
  - Any legal ambiguities or uncertainties
- **Legal Counsel Approval**:
  - Signs off on requirements extraction
  - Documents any caveats or conditions
  - Identifies any areas needing external legal opinion

**For Tier 2/3 regulations:**
- Legal review may be optional
- ISMS Manager review sufficient

#### 7.6 Final Approval

**Approvers:**
- Compliance Officer (completeness and accuracy)
- Legal Counsel (legal interpretation) [Tier 1]
- ISMS Manager (ISMS implications)

**Approval Documented:**
- Signature/date in Requirements Register notes
- Or separate approval form

**Once Approved:**
- Requirements extraction complete
- Register locked (no further changes without new version)
- Ready for Control Mapping (IMP-S3)

**Estimated Length**: 2 pages

---

## SECTION 8: Example Requirements Extractions

### WRITING INSTRUCTIONS:
Provide 3-4 worked examples showing extraction in action.

Use **completely generic** examples.

### KEY CONTENT:

#### Example 1: Data Protection Obligation

**Original Regulation Text:**
> "Article X: Organizations shall implement appropriate technical and organizational measures to ensure the security of personal data, including protection against unauthorized or unlawful processing and against accidental loss, destruction, or damage. Such measures shall include, as appropriate, encryption and access controls."

**Extraction:**
1. **Identify Discrete Obligations**:
   - Implement technical and organizational security measures
   - Protect against unauthorized processing
   - Protect against accidental loss/destruction/damage
   - Implement encryption (as appropriate)
   - Implement access controls (as appropriate)

2. **Extract & Rewrite**:
   - **REQ-001**: "Implement technical and organizational measures to ensure the security of personal data"
   - **REQ-002**: "Implement controls to prevent unauthorized or unlawful processing of personal data"
   - **REQ-003**: "Implement controls to prevent accidental loss, destruction, or damage to personal data"
   - **REQ-004**: "Implement encryption for personal data where appropriate to risk"
   - **REQ-005**: "Implement access controls to restrict access to personal data to authorized personnel only"

3. **Categorize**:
   - REQ-001: Organizational (general security program)
   - REQ-002: Technical (access controls, monitoring)
   - REQ-003: Operational (backup, resilience)
   - REQ-004: Technical (encryption)
   - REQ-005: Technical (access management)

4. **Register Entry**:
   ```
   ID: REG-DPA-X-001
   Citation: Article X
   Original Text: [Full quote above]
   Interpreted: "Implement technical and organizational measures to ensure the security of personal data"
   Category: Organizational
   Priority: High
   Status: Not Started
   ```
   [Repeat for REQ-002 through REQ-005]

#### Example 2: Incident Reporting Obligation

**Original Regulation Text:**
> "Section Y: In the event of a security breach affecting personal data, the organization must notify the relevant authority without undue delay and, where feasible, no later than 72 hours after becoming aware of the breach, unless the breach is unlikely to result in a risk to individuals."

**Extraction:**
1. **Identify Obligation**:
   - Notify authority of security breach
   - Timeline: Within 72 hours (where feasible)
   - Condition: Unless unlikely to result in risk

2. **Extract & Rewrite**:
   - **REQ-001**: "Notify the relevant authority of security breaches affecting personal data within 72 hours of detection, unless the breach is unlikely to result in risk to individuals"

3. **Categorize**:
   - Category: Reporting

4. **Register Entry**:
   ```
   ID: REG-DPA-Y-001
   Citation: Section Y
   Original Text: [Full quote above]
   Interpreted: "Notify the relevant authority of security breaches affecting personal data within 72 hours of detection, unless the breach is unlikely to result in risk to individuals"
   Category: Reporting
   Priority: High
   Deadline: Within 72 hours of breach detection
   Status: Not Started
   Notes: Requires incident response procedures and authority contact information
   ```

#### Example 3: Organizational Requirement

**Original Regulation Text:**
> "Article Z: Organizations processing personal data shall designate a Data Protection Officer responsible for monitoring compliance with this regulation and serving as point of contact for data subjects and the supervisory authority."

**Extraction:**
1. **Identify Obligations**:
   - Designate a DPO
   - DPO responsibilities: Monitor compliance
   - DPO responsibilities: Serve as point of contact

2. **Extract & Rewrite**:
   - **REQ-001**: "Designate a Data Protection Officer responsible for monitoring data protection compliance"
   - **REQ-002**: "Ensure DPO serves as point of contact for data subjects and supervisory authority"

3. **Categorize**:
   - REQ-001: Organizational (role designation)
   - REQ-002: Organizational (governance)

4. **Register Entry**:
   ```
   ID: REG-DPA-Z-001
   Citation: Article Z
   Original Text: [Full quote above]
   Interpreted: "Designate a Data Protection Officer responsible for monitoring data protection compliance"
   Category: Organizational
   Priority: High
   Status: Not Started
   Notes: Check if organization meets threshold requiring DPO
   ```

#### Example 4: Operational Requirement

**Original Regulation Text:**
> "Section W: Organizations shall conduct regular testing and evaluation of the effectiveness of technical and organizational measures to ensure the security of processing."

**Extraction:**
1. **Identify Obligation**:
   - Conduct regular testing and evaluation
   - Focus: Effectiveness of security measures

2. **Extract & Rewrite**:
   - **REQ-001**: "Conduct regular testing and evaluation of the effectiveness of security controls"

3. **Categorize**:
   - Category: Operational

4. **Register Entry**:
   ```
   ID: REG-DPA-W-001
   Citation: Section W
   Original Text: [Full quote above]
   Interpreted: "Conduct regular testing and evaluation of the effectiveness of security controls"
   Category: Operational
   Priority: Medium
   Status: Not Started
   Notes: "Regular" not defined - recommend annual at minimum
   ```

**Estimated Length**: 2-3 pages

---

## SECTION 9: Templates & Tools

### WRITING INSTRUCTIONS:
Provide or reference templates for requirements extraction.

### KEY CONTENT:

#### 9.1 Requirements Register Template

**Reference**: Assessment Workbook 3 (Requirements Extraction) provides Excel template

**Template includes:**
- All fields listed in Section 6.1
- Data validation (dropdowns for categories, status, priority)
- Formulas for counts and summaries
- Filters for easy navigation

#### 9.2 Extraction Worksheet Template

**Purpose**: Working document while extracting requirements

**Structure:**
```
| Article | Summary | Mandatory? | Requirements Count | Notes | Legal Review Needed? |
```

**Use:**
- Track progress through regulation
- Estimate extraction effort
- Flag articles needing legal review

#### 9.3 Requirement Numbering Cheatsheet

**Convention**: REG-[RegCode]-[Article]-[Seq]

**Examples:**
- REG-GDPR-32-001: First requirement from GDPR Article 32
- REG-HIPAA-164-001: First requirement from HIPAA § 164
- REG-SOX-404-001: First requirement from SOX Section 404

**If Article Number Not Applicable:**
- Use Section number or title abbreviation
- Example: REG-PCI-3-001 (PCI DSS Requirement 3)

**Estimated Length**: 1 page

---

## SECTION 10: Quality Checks & Common Pitfalls

### WRITING INSTRUCTIONS:
Help users avoid common mistakes in requirements extraction.

### KEY CONTENT:

#### 10.1 Quality Checklist

Before finalizing extraction, verify:
- [ ] All articles reviewed (none skipped)
- [ ] All "shall" and "must" statements extracted
- [ ] Requirements rewritten in actionable form
- [ ] Requirements properly cited (article/section referenced)
- [ ] Requirements categorized
- [ ] Requirements prioritized
- [ ] No duplicate requirements
- [ ] No over-interpretation (only what's in regulation)
- [ ] No under-interpretation (all obligations captured)
- [ ] Legal review completed (for Tier 1)
- [ ] All approvals obtained
- [ ] Requirements Register updated and version controlled

#### 10.2 Common Pitfalls to Avoid

**Pitfall 1: Extracting Too Coarsely**
- "Comply with Article 32" is not a requirement
- Break down into specific obligations

**Pitfall 2: Extracting Too Finely**
- Don't specify implementation details regulation doesn't require
- Allow implementation flexibility

**Pitfall 3: Adding Requirements Not in Regulation**
- Over-interpretation
- Stick to what's written

**Pitfall 4: Missing Conditional Requirements**
- "If X, then Y" requirements are still requirements
- Extract with condition noted

**Pitfall 5: Ignoring Context**
- Definitions matter
- Cross-references matter
- Read regulation as a whole

**Pitfall 6: Inconsistent Categorization**
- Be consistent in how you categorize similar requirements
- Use guidelines, not arbitrary judgment

**Pitfall 7: Skipping Legal Review (for Tier 1)**
- Legal interpretation is critical for mandatory compliance
- Don't skip this step

**Estimated Length**: 1 page

---

## SECTION 11: Related Documents & References

### WRITING INSTRUCTIONS:
List all related documents.

### CONTENT:
- **Policy**: ISMS-POL-A.5.31-S3 (Requirements Mapping Framework) - defines methodology this guide implements
- **Implementation**: ISMS-IMP-A.5.31-S1 (Applicability Assessment) - precedes this step
- **Implementation**: ISMS-IMP-A.5.31-S3 (Control Mapping) - follows this step
- **Assessment Tool**: Assessment Workbook 3 (Requirements Extraction) - Excel template
- **Register**: Requirements Register (master list maintained via Workbook 3)
- **Standard**: ISO 27001:2022 Control A.5.31

**Estimated Length**: 0.5 page

---

## QUALITY CHECKS FOR IMP-S2

Before considering IMP-S2 complete, verify:

- [ ] Process steps are clear and actionable
- [ ] Parsing regulatory structure explained
- [ ] Mandatory vs. recommendatory language clearly distinguished
- [ ] Extraction technique thoroughly explained with granularity guidelines
- [ ] Categorization framework defined
- [ ] Requirements Register structure defined
- [ ] Review and validation process defined
- [ ] Examples are generic and illustrative
- [ ] Templates referenced
- [ ] Common pitfalls addressed
- [ ] Quality checklist included
- [ ] Total length: 8-10 pages

---

## READY FOR CONTENT DEVELOPMENT

This skeleton provides the structure for ISMS-IMP-A.5.31-S2.

**Next Steps After Completion:**
1. User reviews and approves IMP-S2
2. Proceed to IMP-S3 (Control Mapping Process)

---

END OF SKELETON
