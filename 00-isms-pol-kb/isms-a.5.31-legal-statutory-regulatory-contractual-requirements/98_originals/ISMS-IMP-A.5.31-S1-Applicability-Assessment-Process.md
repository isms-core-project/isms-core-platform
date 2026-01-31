# ISMS-IMP-A.5.31-S1: Regulatory Applicability Assessment Process
## SKELETON WITH WRITING INSTRUCTIONS

**Status**: SKELETON - Ready for content development  
**Target Length**: 8-10 pages  
**Purpose**: Step-by-step operational guide for identifying and assessing applicable regulations

**Related Policy**: ISMS-POL-A.5.31-S2 (Applicability Methodology)

---

## SECTION 1: Process Overview

### WRITING INSTRUCTIONS:
Provide high-level overview of the applicability assessment process.

### KEY CONTENT:
- **Purpose**: Operationalize the methodology defined in POL-S2
- **When Used**: When identifying potentially applicable regulations
- **Who Performs**: Compliance Officer, Legal, ISMS Manager (as defined in POL-S1 roles)
- **Output**: Completed applicability assessment, determination of tier, entry in ISMS-POL-00

### INCLUDE:
- **Process Flowchart**:
  ```
  [Trigger Event]
      ↓
  [Step 1: Regulatory Identification]
      ↓
  [Step 2: Initial Screening]
      ↓
  [Step 3: Detailed Applicability Assessment]
      ↓
  [Step 4: Tier Categorization]
      ↓
  [Step 5: Documentation & Approval]
      ↓
  [Step 6: Add to ISMS-POL-00]
  ```

- **Typical Timeline**: 
  - Simple assessment: 1-2 weeks
  - Complex assessment requiring legal opinion: 4-6 weeks

- **Key Artifacts**:
  - Applicability Assessment Form (template provided)
  - Supporting evidence documents
  - Approval records
  - ISMS-POL-00 entry

**Estimated Length**: 1-2 pages

---

## SECTION 2: Step 1 - Regulatory Identification

### WRITING INSTRUCTIONS:
Provide step-by-step instructions for identifying candidate regulations.

### KEY CONTENT:

#### 2.1 When to Perform Identification
List trigger events (reference POL-S2 Section 2.1):
- New jurisdiction entry
- New service offering
- New customer contract with requirements
- Periodic review schedule
- Regulatory alert received
- Etc.

#### 2.2 Where to Look (Sources)
Detailed guidance on each source (reference POL-S2 Section 2.2):

**For each source, provide:**
- **Source Name/Type**
- **How to Access**: URL, subscription info, contact
- **What to Search For**: Keywords, categories
- **Example Searches**: Concrete examples
- **Tips**: Best practices for using this source

**Example Structure for One Source:**
```
Legal Database: LexisNexis
- Access: [Organization] subscription at [URL]
- Search Process:
  1. Navigate to Regulatory Compliance section
  2. Filter by jurisdiction: [Target Jurisdiction]
  3. Filter by topic: Data Protection, Cybersecurity, Information Security
  4. Filter by effective date: Last 12 months (for periodic review)
- Example Search: "data protection regulation" AND "EU" AND "information security"
- Tips: 
  - Set up alerts for ongoing monitoring
  - Check both enacted and proposed regulations
  - Review official summaries before full text
```

#### 2.3 Documenting Candidate Regulations
As you identify potential regulations, document:
- Regulation name
- Jurisdiction
- Issuing authority
- Effective date
- Brief description
- Source (where found)
- Reason for consideration (which trigger event)

**Use: Candidate Regulations List (worksheet)**

**Estimated Length**: 2-3 pages

---

## SECTION 3: Step 2 - Initial Screening

### WRITING INSTRUCTIONS:
Define the quick filter process before detailed assessment.

### KEY CONTENT:

#### 3.1 Screening Criteria
Quick yes/no questions to filter candidate regulations:

**Relevance Check:**
- Does this regulation relate to information security, data protection, or IT services?
- If NO → Stop, do not proceed to detailed assessment
- If YES → Continue

**Jurisdiction Check:**
- Does [Organization] operate in this jurisdiction?
- Does [Organization] serve customers in this jurisdiction?
- Does this regulation claim extraterritorial reach?
- If ALL NO → Likely not applicable, document and stop
- If ANY YES → Continue

**Operational Check:**
- Does [Organization] perform activities covered by this regulation?
- Does [Organization] process data types covered by this regulation?
- If NO → Likely not applicable, document and stop
- If YES → Continue

**Threshold Check:**
- Does this regulation have size/revenue/volume thresholds?
- If YES: Does [Organization] meet them?
  - If NO → Not applicable (but monitor for future growth)
  - If YES → Continue
- If NO thresholds → Continue

#### 3.2 Screening Outcome
- **Proceed to Detailed Assessment**: Passed all screening checks
- **Not Applicable**: Failed screening, document rationale, do not proceed
- **Uncertain**: Borderline case, escalate to detailed assessment to be safe

#### 3.3 Documenting Screening
- Complete screening checklist for each candidate
- Document outcome and rationale
- If not proceeding: File in "Reviewed but Not Applicable" folder for future reference

**Estimated Length**: 1-2 pages

---

## SECTION 4: Step 3 - Detailed Applicability Assessment

### WRITING INSTRUCTIONS:
This is the CORE of the process - the three-dimensional assessment per POL-S2 Section 3.

### KEY CONTENT:

#### 4.1 Geographic Scope Assessment

**Instructions:**
1. Review regulation text for geographic scope provisions
2. Answer each question below with Yes/No and provide evidence
3. Document rationale

**Questions to Answer:**
- Does [Organization] have physical operations (offices, facilities) in [Jurisdiction]?
  - Evidence: Office locations, legal entity registrations
- Does [Organization] have legal entities registered in [Jurisdiction]?
  - Evidence: Corporate registry records
- Does [Organization] have employees located in [Jurisdiction]?
  - Evidence: Headcount reports, employee locations
- Does [Organization] serve customers physically located in [Jurisdiction]?
  - Evidence: Customer list, sales by region
- Does [Organization] process data of individuals in [Jurisdiction]?
  - Evidence: Data processing records, data subject locations
- Does [Organization] target customers in [Jurisdiction] (website, marketing)?
  - Evidence: Website localization, marketing campaigns
- Does the regulation claim extraterritorial application?
  - Evidence: Regulation text analysis

**Geographic Applicability Score:**
- Formula: Count of YES answers
- 0-1 YES: Low geographic applicability
- 2-3 YES: Moderate geographic applicability
- 4+ YES: High geographic applicability

**Document in: Applicability Assessment Form - Geographic Section**

#### 4.2 Operational Scope Assessment

**Instructions:**
1. Review regulation text for operational scope provisions
2. Answer each question below with Yes/No and provide evidence
3. Document rationale

**Questions to Answer:**
- Does [Organization] provide services that trigger this regulation?
  - Identify service types: Cloud services, IT consulting, software development, etc.
  - Match to regulation's scope
  - Evidence: Service catalog, SOW examples
- Does [Organization] serve industry sectors covered by this regulation?
  - Identify sectors: Financial services, healthcare, government, etc.
  - Match to regulation's applicability
  - Evidence: Customer contracts, vertical market analysis
- Does [Organization] process data types covered by this regulation?
  - Identify data types: Personal data, health data, financial data, etc.
  - Match to regulation's scope
  - Evidence: Data inventory, data classification
- Does [Organization]'s operational characteristics meet regulation's scope?
  - Size thresholds: Number of employees, revenue, data volume
  - Organizational type: Public/private, for-profit/non-profit
  - Evidence: Financial reports, organizational structure
- Does [Organization] perform specific operations covered by regulation?
  - Examples: E-commerce, telecommunications, payment processing
  - Evidence: Business model documentation

**Operational Applicability Score:**
- Formula: Count of YES answers
- 0-1 YES: Low operational applicability
- 2-3 YES: Moderate operational applicability
- 4+ YES: High operational applicability

**Document in: Applicability Assessment Form - Operational Section**

#### 4.3 Contractual Scope Assessment

**Instructions:**
1. Review customer contracts, supplier agreements, and certification requirements
2. Answer each question below with Yes/No and provide evidence
3. Document rationale

**Questions to Answer:**
- Do customer contracts require compliance with this regulation?
  - Review customer contracts for compliance clauses
  - Check if regulation explicitly named
  - Evidence: Contract excerpts
- Do supplier agreements create pass-through obligations?
  - Review agreements with [Organization]'s suppliers
  - Check for compliance requirements passed to [Organization]
  - Evidence: Supplier contract excerpts
- Is compliance required for certifications [Organization] holds or pursues?
  - ISO 27001, SOC 2, industry-specific certifications
  - Check certification body requirements
  - Evidence: Certification standards, audit requirements
- Has [Organization] made voluntary commitments to comply?
  - Public statements, privacy policies, commitments to customers
  - Evidence: Public documents, policies

**Contractual Applicability Score:**
- Formula: Count of YES answers
- 0 YES: No contractual applicability
- 1-2 YES: Moderate contractual applicability
- 3+ YES: High contractual applicability

**Document in: Applicability Assessment Form - Contractual Section**

#### 4.4 Overall Applicability Determination

**Combine the three assessments:**

**Decision Logic:**
- **Applicable (Tier 1)**: 
  - High score in any dimension (especially if legal obligation), OR
  - Moderate scores in multiple dimensions, OR
  - Explicit contractual requirement
  
- **Conditionally Applicable (Tier 2)**:
  - Moderate scores but no immediate legal obligation
  - Potential future applicability
  - Voluntary adoption for competitive advantage
  
- **Informational Reference (Tier 3)**:
  - Low scores across all dimensions
  - Used for guidance/best practices only
  - No compliance obligation
  
- **Not Applicable**:
  - Low/zero scores in all dimensions
  - No legal, operational, or contractual driver
  - Do not add to ISMS-POL-00

**Document: Final Determination with Rationale**

**Estimated Length**: 3-4 pages

---

## SECTION 5: Step 4 - Tier Categorization

### WRITING INSTRUCTIONS:
Apply the tier framework from POL-S2 Section 4 to assign the regulation to the correct tier.

### KEY CONTENT:

#### 5.1 Applying Tier Definitions

**Review POL-S2 Tier Definitions:**
- Tier 1: Mandatory Compliance (legal or contractual obligation)
- Tier 2: Conditional Applicability (potential or voluntary)
- Tier 3: Informational Reference (guidance only)

**Decision Tree:**
```
Is there a legal obligation?
  YES → Tier 1
  NO → Continue

Is there a contractual obligation with enforcement?
  YES → Tier 1
  NO → Continue

Is there potential future applicability?
  YES → Tier 2
  NO → Continue

Is this used for guidance/benchmarking?
  YES → Tier 3
  NO → Not Applicable (do not add to POL-00)
```

#### 5.2 Documenting Tier Assignment

**In Applicability Assessment Form:**
- Assigned Tier: [1/2/3]
- Rationale: [Explain why this tier based on assessment]
- Supporting Evidence: [Reference evidence documents]

#### 5.3 Examples of Tier Assignments (Generic)

**Example 1: Data Protection Law in Jurisdiction of Operation**
- Geographic: High (operations in jurisdiction)
- Operational: High (process personal data)
- Contractual: Moderate (customers expect compliance)
- Determination: Applicable
- Tier: 1 (Mandatory - legal obligation)

**Example 2: Industry Framework [Organization] Adopts Voluntarily**
- Geographic: N/A (not geographic-based)
- Operational: Moderate (industry best practice)
- Contractual: Low (some customers reference it)
- Determination: Conditionally Applicable
- Tier: 2 (Voluntary adoption for advantage)

**Example 3: Best Practice Framework for Reference**
- Geographic: N/A
- Operational: Low (guidance only)
- Contractual: None
- Determination: Informational
- Tier: 3 (Reference/benchmarking)

**Estimated Length**: 1 page

---

## SECTION 6: Step 5 - Documentation & Approval

### WRITING INSTRUCTIONS:
Define how to complete documentation and obtain approvals.

### KEY CONTENT:

#### 6.1 Completing the Applicability Assessment Form

**Form Sections to Complete:**
1. **Regulation Identification**:
   - Regulation name, jurisdiction, authority, effective date
2. **Assessment Summary**:
   - Geographic score and rationale
   - Operational score and rationale
   - Contractual score and rationale
3. **Overall Determination**:
   - Applicable / Not Applicable / Uncertain
4. **Tier Assignment** (if applicable):
   - Tier 1, 2, or 3
   - Rationale for tier
5. **Supporting Evidence**:
   - List attached documents
   - Links to evidence
6. **Assessor Information**:
   - Name, role, date of assessment

**Template: See Assessment Workbook 2 (Applicability Matrix) for form template**

#### 6.2 Gathering Supporting Evidence

**Evidence to Attach:**
- Regulatory text or official citation
- Legal opinion (if obtained)
- Jurisdictional analysis
- Contract excerpts (if contractual applicability)
- Any other supporting documentation

#### 6.3 Review & Approval Workflow

**Step 1: Peer Review**
- Another member of Compliance/Legal team reviews
- Checks: Completeness, logic, evidence
- May send back for revisions

**Step 2: Legal Review** (for Tier 1 determinations)
- Legal counsel reviews legal accuracy
- Validates interpretation of regulation
- Approves or requests changes

**Step 3: ISMS Manager Review**
- Reviews ISMS implications
- Considers resource/control impact
- Approves or escalates

**Step 4: Executive Approval** (for Tier 1, high-impact)
- Executive approval for Tier 1 (mandatory compliance)
- Acknowledges compliance obligation and resource commitment
- Approves or requests further analysis

**Step 5: Final Signature**
- All approvers sign/e-sign assessment form
- Date of approval recorded
- Assessment locked (no further changes without new version)

**Escalation:**
- If applicability is disputed or uncertain: Escalate to Executive Management
- May engage external legal counsel for opinion

**Estimated Length**: 1-2 pages

---

## SECTION 7: Step 6 - Adding to ISMS-POL-00

### WRITING INSTRUCTIONS:
Define the process for updating the regulatory register.

### KEY CONTENT:

#### 7.1 Updating ISMS-POL-00

**If Determination: Applicable (Tier 1, 2, or 3)**

**Steps:**
1. **Open ISMS-POL-00 (Regulatory Applicability Framework)**
2. **Add Entry to Appropriate Tier Section**:
   - Tier 1: Mandatory Compliance (if Tier 1)
   - Tier 2: Conditional Applicability (if Tier 2)
   - Tier 3: Informational Reference (if Tier 3)
3. **Complete All Fields**:
   - Regulation name
   - Jurisdiction
   - Issuing authority
   - Effective date
   - Applicability rationale (brief summary)
   - Reference to detailed assessment (file location)
   - Review date (1 year from assessment)
   - Responsible party
4. **Version Control**:
   - Increment version number of ISMS-POL-00
   - Update version history table
5. **Save and Distribute**:
   - Save updated POL-00
   - Distribute to stakeholders

**If Determination: Not Applicable**
- Do NOT add to ISMS-POL-00
- File completed assessment in "Reviewed but Not Applicable" folder
- May be revisited if circumstances change

#### 7.2 Communication

**Notify Stakeholders:**
- Email notification to:
  - ISMS Manager
  - Affected control owners (if requirements expected)
  - Management (for Tier 1 additions)
- Message includes:
  - Regulation added
  - Tier assigned
  - High-level implications
  - Next steps (requirements extraction)

#### 7.3 Triggering Next Steps

**For Tier 1 and Tier 2 regulations:**
- Next step: Requirements Extraction (IMP-S2)
- Schedule requirements extraction work
- Assign to appropriate personnel

**For Tier 3 regulations:**
- No immediate action required
- Available for reference when designing controls

**Estimated Length**: 1 page

---

## SECTION 8: Example Applicability Assessments

### WRITING INSTRUCTIONS:
Provide 3-4 worked examples showing the process in action.

Use **completely generic** examples - no real regulation names.

### KEY CONTENT:

#### Example 1: Data Protection Regulation in Operating Jurisdiction

**Scenario**: [Organization] opens office in [Country X]. [Country X] has a comprehensive data protection law.

**Assessment Process:**
- **Trigger**: New jurisdiction entry
- **Identification**: Data Protection Law of [Country X] identified via legal database
- **Screening**: Passes all screens (relevant, [Org] in jurisdiction, processes data)
- **Geographic Assessment**: High (6/7 YES - office, employees, customers in Country X)
- **Operational Assessment**: High (5/5 YES - processes personal data, serves customers)
- **Contractual Assessment**: Moderate (2/4 YES - customers expect compliance)
- **Determination**: Applicable
- **Tier**: Tier 1 (Mandatory - legal obligation in jurisdiction of operation)
- **Approval**: Legal reviewed, Executive approved
- **Added to POL-00**: Yes, Tier 1 section
- **Next Steps**: Requirements extraction scheduled

#### Example 2: Sector-Specific Regulation (Potential Market)

**Scenario**: [Organization] is considering entering the [Financial Services] sector. There is a sector-specific regulation for information security.

**Assessment Process:**
- **Trigger**: Strategic initiative (potential new market)
- **Identification**: [Financial Services] Information Security Regulation identified
- **Screening**: Passes (relevant, [Org] considering serving this sector)
- **Geographic Assessment**: Moderate ([Org] operates in jurisdictions where reg applies)
- **Operational Assessment**: Low (does NOT currently serve financial services)
- **Contractual Assessment**: Low (no current contractual requirement)
- **Determination**: Conditionally Applicable (potential future applicability)
- **Tier**: Tier 2 (Conditional - if/when [Org] enters market)
- **Approval**: ISMS Manager approved
- **Added to POL-00**: Yes, Tier 2 section
- **Next Steps**: Monitor market entry plans, gap analysis for preparedness

#### Example 3: Industry Best Practice Framework

**Scenario**: [Organization] wants to use [NIST Cybersecurity Framework] for maturity benchmarking.

**Assessment Process:**
- **Trigger**: Internal initiative (maturity assessment)
- **Identification**: NIST CSF identified as best practice
- **Screening**: Passes (relevant to information security)
- **Geographic Assessment**: N/A (not jurisdiction-based)
- **Operational Assessment**: Low (guidance, not obligation)
- **Contractual Assessment**: None
- **Determination**: Informational Reference
- **Tier**: Tier 3 (Reference/benchmarking only)
- **Approval**: ISMS Manager approved
- **Added to POL-00**: Yes, Tier 3 section
- **Next Steps**: Use for control design and maturity assessment, no compliance obligation

#### Example 4: Not Applicable Regulation

**Scenario**: [Organization] reviews a regulation specific to [Pharmaceutical Manufacturing] data.

**Assessment Process:**
- **Trigger**: Periodic review (comprehensive scan)
- **Identification**: [Pharmaceutical Manufacturing] Data Regulation identified
- **Screening**: Fails operational check ([Org] does NOT manufacture pharmaceuticals)
- **Geographic Assessment**: Not performed (failed screening)
- **Operational Assessment**: Not performed (failed screening)
- **Contractual Assessment**: Not performed (failed screening)
- **Determination**: Not Applicable
- **Tier**: N/A
- **Approval**: Compliance Officer documented rationale
- **Added to POL-00**: No (not applicable)
- **Next Steps**: File assessment, revisit if [Org] business changes

**Estimated Length**: 2-3 pages

---

## SECTION 9: Templates & Tools

### WRITING INSTRUCTIONS:
Provide or reference templates for performing assessments.

### KEY CONTENT:

#### 9.1 Applicability Assessment Form Template

**Reference**: Assessment Workbook 2 (Applicability Matrix) provides Excel template

**Sections:**
1. Regulation identification
2. Geographic scope assessment (questions + scores)
3. Operational scope assessment (questions + scores)
4. Contractual scope assessment (questions + scores)
5. Overall determination
6. Tier assignment
7. Rationale
8. Evidence references
9. Approval signatures

#### 9.2 Screening Checklist Template

**Simple checklist for Step 2:**
- [ ] Relevance: Related to information security? (Y/N)
- [ ] Jurisdiction: [Org] operates there? (Y/N)
- [ ] Operational: [Org] performs covered activities? (Y/N)
- [ ] Threshold: [Org] meets thresholds? (Y/N/NA)
- **Outcome**: Proceed / Stop / Uncertain

#### 9.3 Decision Tree Template

**Visual decision tree** to guide tier assignment (reference POL-S2 Section 4.4)

#### 9.4 Communication Template

**Email template for notifying stakeholders of new regulation:**
```
Subject: New Regulation Added to ISMS-POL-00: [Regulation Name]

[Stakeholder Name],

A new regulation has been assessed and added to our Regulatory Applicability Framework (ISMS-POL-00):

- Regulation: [Name]
- Jurisdiction: [Jurisdiction]
- Tier: [1/2/3]
- Rationale: [Brief summary]
- Implications: [High-level impact]

Next Steps:
- [e.g., Requirements extraction scheduled for [Date]]
- [e.g., Control mapping to follow]

Full assessment documentation: [Link]

Questions? Contact [Compliance Officer]

[Signature]
```

**Estimated Length**: 1 page

---

## SECTION 10: Quality Checks & Common Pitfalls

### WRITING INSTRUCTIONS:
Help users avoid common mistakes.

### KEY CONTENT:

#### 10.1 Quality Checklist

Before finalizing assessment, verify:
- [ ] All three dimensions assessed (geographic, operational, contractual)
- [ ] Evidence provided for each YES answer
- [ ] Rationale documented for determination
- [ ] Tier assignment aligns with POL-S2 definitions
- [ ] All approvals obtained per workflow
- [ ] Assessment form complete (no blank fields)
- [ ] Supporting documents attached
- [ ] If applicable: Entry added to ISMS-POL-00

#### 10.2 Common Pitfalls to Avoid

**Pitfall 1: Assuming Applicability Without Assessment**
- Don't assume regulation applies just because it exists
- Perform systematic assessment

**Pitfall 2: Over-Interpreting Scope**
- Don't read regulation more broadly than written
- When uncertain, seek legal opinion

**Pitfall 3: Ignoring Contractual Obligations**
- Even if no legal obligation, contract may require compliance
- Check customer contracts

**Pitfall 4: Failing to Document Rationale**
- Assessment without rationale is not auditable
- Always document WHY you reached your determination

**Pitfall 5: Skipping Approvals**
- Don't add to POL-00 without proper approvals
- Especially Tier 1 (executive approval required)

**Estimated Length**: 1 page

---

## SECTION 11: Related Documents & References

### WRITING INSTRUCTIONS:
List all related documents.

### CONTENT:
- **Policy**: ISMS-POL-A.5.31-S2 (Applicability Methodology) - defines the methodology this guide implements
- **Policy**: ISMS-POL-00 (Regulatory Applicability Framework) - the register updated by this process
- **Implementation**: ISMS-IMP-A.5.31-S2 (Requirements Extraction) - next step after applicability determined
- **Assessment Tool**: Assessment Workbook 2 (Applicability Matrix) - Excel template for assessments
- **Standard**: ISO 27001:2022 Control A.5.31

**Estimated Length**: 0.5 page

---

## QUALITY CHECKS FOR IMP-S1

Before considering IMP-S1 complete, verify:

- [ ] Process steps are clear and actionable
- [ ] Flowchart provided for visual understanding
- [ ] Each step has detailed instructions
- [ ] Examples are generic (not specific regulations)
- [ ] Templates referenced or provided
- [ ] Approval workflow is clear
- [ ] Integration with ISMS-POL-00 is explicit
- [ ] Common pitfalls addressed
- [ ] Quality checklist included
- [ ] Total length: 8-10 pages

---

## READY FOR CONTENT DEVELOPMENT

This skeleton provides the structure for ISMS-IMP-A.5.31-S1.

**Next Steps After Completion:**
1. User reviews and approves IMP-S1
2. Proceed to IMP-S2 (Requirements Extraction Process)

---

END OF SKELETON
