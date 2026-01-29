# ISMS-POL-A.5.31-S3: Requirements Extraction & Control Mapping Framework
## SKELETON WITH WRITING INSTRUCTIONS

**Status**: SKELETON - Ready for content development  
**Target Length**: 10-12 pages  
**Purpose**: Define methodology for translating regulations into actionable controls with traceability

---

## SECTION 1: Introduction & Relationship to S1/S2

### WRITING INSTRUCTIONS:
- Brief introduction explaining purpose of this section
- Reference S1 (framework foundation) and S2 (applicability determination)
- Explain that THIS section covers translating regulations into action

### KEY POINTS:
- S2 determined WHICH regulations apply
- S3 determines WHAT those regulations require and HOW we comply
- The translation layer: Regulatory text → Actionable requirements → ISO controls
- Foundation for demonstrating compliance

### STRUCTURE:
```
1.1 Purpose of This Policy Section
1.2 Progression: Applicability → Requirements → Controls
1.3 The Translation Challenge
1.4 Document Scope
```

**Estimated Length**: 1 page

---

## SECTION 2: Requirements Extraction Process

### WRITING INSTRUCTIONS:
Define the systematic process for parsing regulatory text into actionable requirements.

This is a CRITICAL section - regulations are often vague, lawyers' text, hard to operationalize.
The extraction process must be systematic and repeatable.

### KEY CONTENT:

#### 2.1 Requirements Extraction Methodology

**Write about:**
- **Reading Regulatory Text Systematically**:
  - Regulations have structure (articles, sections, annexes, schedules)
  - Each article/section may contain multiple requirements
  - Requirements may be nested or interdependent
  - Some text is definitions, some is obligations
  
- **Identifying Mandatory vs. Recommendatory Language**:
  - **Mandatory**: "shall", "must", "is required to", "will"
  - **Recommendatory**: "should", "may", "is encouraged to"
  - **Optional**: "can", "recommended", "suggested"
  - Only mandatory requirements are extracted (recommendatory noted for context)
  
- **Granularity Guidelines**:
  - **Too Coarse**: "Comply with Article 32" → Not actionable
  - **Too Fine**: "Use AES-256 encryption" → Too prescriptive, limits flexibility
  - **Just Right**: "Implement encryption for data at rest using industry-standard algorithms and key lengths"
  - Goal: Actionable requirement that maps to controls but allows implementation flexibility

#### 2.2 Requirements Categorization

Once extracted, requirements must be categorized for mapping:

**Write about:**
- **Technical Requirements**:
  - System configurations
  - Security measures (encryption, access controls, etc.)
  - Technical safeguards
  - Technology-specific requirements
  
- **Organizational Requirements**:
  - Policies and procedures
  - Roles and responsibilities
  - Training and awareness
  - Governance structures
  
- **Reporting Requirements**:
  - Notifications to authorities
  - Periodic submissions
  - Breach disclosures
  - Audit reports
  
- **Operational Requirements**:
  - Incident response procedures
  - Business continuity
  - Monitoring and logging
  - Testing and validation
  
- **Purpose**: Categorization helps with control mapping (technical → technical controls, etc.)

#### 2.3 Requirements Register Structure

The register is the authoritative list of all extracted requirements:

**Write about:**
- **Register Fields**:
  - **Requirement ID**: Unique identifier (format: REG-[RegCode]-[Article]-[Seq])
    - Example: REG-GDPR-32-001 (first requirement from GDPR Article 32)
  - **Regulation ID**: Link to ISMS-POL-00 entry
  - **Regulation Name**: Full name
  - **Citation**: Specific article, section, paragraph
  - **Original Requirement Text**: Exact quote from regulation
  - **Interpreted Requirement**: Rewritten in actionable form
  - **Requirement Category**: Technical/Organizational/Reporting/Operational
  - **Priority**: High/Medium/Low (based on legal consequence)
  - **Implementation Deadline**: If specified in regulation
  - **Implementation Status**: Not Started/In Progress/Implemented/N/A
  - **Responsible Party**: Who implements
  - **Notes**: Additional context
  - **Extracted By / Date**: Traceability
  - **Reviewed By / Date**: Quality control
  
- **Register Maintenance**:
  - Central repository (likely spreadsheet or database)
  - Version control
  - Access control (who can add/edit)
  - Audit trail

#### 2.4 Extraction Principles

**Write about:**
- **Completeness**: Extract ALL mandatory requirements (don't cherry-pick)
- **Accuracy**: Faithful to regulatory intent (legal review recommended)
- **Clarity**: Written to be understandable by implementers
- **Traceability**: Always cite source (article, paragraph)
- **Consistency**: Similar requirements extracted similarly across regulations
- **No Interpretation Creep**: Don't add requirements not in regulation
- **Legal Review**: Legal counsel should review extractions for accuracy

### STRUCTURE:
```
2.1 Requirements Extraction Methodology
    2.1.1 Reading Regulatory Text Systematically
    2.1.2 Identifying Mandatory vs. Recommendatory Language
    2.1.3 Granularity Guidelines
2.2 Requirements Categorization
    2.2.1 Technical Requirements
    2.2.2 Organizational Requirements
    2.2.3 Reporting Requirements
    2.2.4 Operational Requirements
    2.2.5 Purpose of Categorization
2.3 Requirements Register Structure
    2.3.1 Register Fields (detailed)
    2.3.2 Register Maintenance
2.4 Extraction Principles
```

**Estimated Length**: 3-4 pages

---

## SECTION 3: Control Mapping Methodology

### WRITING INSTRUCTIONS:
Define the systematic process for mapping requirements to ISO 27001 Annex A controls.

This is the CORE of demonstrating compliance - showing HOW requirements are satisfied.

### KEY CONTENT:

#### 3.1 Mapping Approach

**Write about:**
- **The Mapping Challenge**:
  - Regulations written in legal language
  - ISO 27001 controls written in security language
  - Must translate between the two
  - Not always one-to-one correspondence
  
- **The Mapping Question**:
  - For each requirement: "Which ISO 27001 control(s) satisfy this requirement?"
  - May be multiple controls needed
  - May be one control satisfying multiple requirements
  
- **Mapping Philosophy**:
  - Map to EXISTING controls first (leverage Annex A)
  - Only create new controls if no Annex A control fits
  - Prefer multiple controls working together over partial mappings

#### 3.2 Mapping Types

Define the classification system for mappings:

**Write about:**
- **Primary (P)**: Control DIRECTLY satisfies the requirement
  - Example: Requirement "implement access controls" → A.5.15 (Access Control)
  - This is the main control for compliance
  
- **Secondary (S)**: Control PARTIALLY satisfies or SUPPORTS the requirement
  - Example: Requirement "secure software development" → A.8.25 (Primary) + A.8.8 (Secondary for testing)
  - Contributes to compliance but not complete by itself
  
- **Supporting (Su)**: Control contributes INDIRECTLY
  - Example: Requirement "protect data" → A.5.10 (Acceptable Use) supports by defining proper data handling
  - Background support, not direct implementation
  
- **Not Applicable (N/A)**: Control has no relationship to requirement
  - Most controls will be N/A for most requirements
  - Only map when there IS a relationship

#### 3.3 Mapping Matrix Structure

The matrix is the visual representation of mappings:

**Write about:**
- **Matrix Layout**:
  - **Rows**: Requirements (from Requirements Register)
  - **Columns**: ISO 27001 Annex A controls (A.5.1 through A.8.34 = 93 controls)
  - **Cells**: Mapping type (P, S, Su, or blank for N/A)
  
- **Matrix Benefits**:
  - Visual overview of coverage
  - Easy to spot gaps (row with no P/S/Su)
  - Easy to see control reuse (column with many mappings)
  - Supports analysis and reporting
  
- **Matrix Maintenance**:
  - Updated when new requirements added
  - Updated when controls change
  - Version controlled
  - Approved changes only

#### 3.4 One-to-Many and Many-to-One Mappings

**Write about:**
- **One Requirement → Multiple Controls (One-to-Many)**:
  - Common scenario
  - Complex requirements need multiple controls
  - Example: "Implement comprehensive access management" might map to:
    - A.5.15 (Access Control) - Primary
    - A.5.16 (Identity Management) - Primary
    - A.5.17 (Authentication) - Primary
    - A.5.18 (Access Rights) - Primary
    - A.8.2 (Privileged Access) - Secondary
    - A.8.3 (Information Access Restriction) - Secondary
  - All controls work together to satisfy requirement
  
- **Multiple Requirements → One Control (Many-to-One)**:
  - Also common
  - One control may satisfy obligations from multiple regulations
  - Example: A.8.24 (Cryptography) might satisfy:
    - GDPR Article 32: Encryption requirement
    - PCI DSS 3.4: Encryption of cardholder data
    - HIPAA: Encryption of ePHI
    - Customer Contract: Encryption mandate
  - Control implementation provides evidence for multiple requirements
  - Efficiency: Implement once, satisfy many

#### 3.5 Beyond Annex A Controls

What if no Annex A control fits?

**Write about:**
- **When Annex A Isn't Enough**:
  - Highly specific regulatory requirements
  - Industry-specific obligations
  - Jurisdiction-specific mandates
  - Novel requirements (new technologies, new threats)
  
- **Creating Organization-Specific Controls**:
  - When no suitable Annex A control exists
  - Create new control aligned with requirement
  - Numbering convention: CTRL-ORG-[Sequence]
  - Example: CTRL-ORG-001: "Biometric Data Protection"
  - Document rationale for new control
  
- **Control Documentation**:
  - Control objective
  - Control statement
  - Implementation guidance
  - Evidence requirements
  - Responsible party
  - Add to control catalog
  
- **Integration with ISMS**:
  - New controls integrated into ISMS
  - Risk assessment updated
  - Statement of Applicability updated
  - Control effectiveness monitored

### STRUCTURE:
```
3.1 Mapping Approach
    3.1.1 The Mapping Challenge
    3.1.2 The Mapping Question
    3.1.3 Mapping Philosophy
3.2 Mapping Types
    3.2.1 Primary (P)
    3.2.2 Secondary (S)
    3.2.3 Supporting (Su)
    3.2.4 Not Applicable (N/A)
3.3 Mapping Matrix Structure
    3.3.1 Matrix Layout
    3.3.2 Matrix Benefits
    3.3.3 Matrix Maintenance
3.4 One-to-Many and Many-to-One Mappings
    3.4.1 One Requirement → Multiple Controls
    3.4.2 Multiple Requirements → One Control
3.5 Beyond Annex A Controls
    3.5.1 When Annex A Isn't Enough
    3.5.2 Creating Organization-Specific Controls
    3.5.3 Control Documentation
    3.5.4 Integration with ISMS
```

**Estimated Length**: 3-4 pages

---

## SECTION 4: Gap Analysis Process

### WRITING INSTRUCTIONS:
Define how gaps are identified and managed.

A "gap" is a requirement with no control satisfying it - a compliance risk.

### KEY CONTENT:

#### 4.1 Gap Identification

**Write about:**
- **What is a Gap?**:
  - Requirement with NO Primary, Secondary, or Supporting control mapping
  - Or requirement with only partial coverage (e.g., only Su, no P)
  - Or control exists but not implemented
  
- **Types of Gaps**:
  - **Complete Gap**: No control at all for requirement
  - **Partial Gap**: Some controls but incomplete coverage
  - **Implementation Gap**: Control defined but not implemented
  - **Evidence Gap**: Control implemented but no evidence
  
- **Gap Detection**:
  - Review mapping matrix: any row with no P/S/Su = gap
  - Review requirements with only Su: likely partial gap
  - Compare control implementation status to requirements

#### 4.2 Gap Prioritization

Not all gaps are equal - prioritize for remediation:

**Write about:**
- **Prioritization Factors**:
  - **Legal Obligation Level**: Tier 1 regulations (mandatory) → highest priority
  - **Risk Severity**: What's the risk if not compliant? (fines, sanctions, reputational damage)
  - **Implementation Complexity**: How hard/expensive to remediate?
  - **Timeline**: Is there a regulatory deadline?
  
- **Priority Levels**:
  - **High**: Tier 1 regulation, high risk, deadline approaching
  - **Medium**: Tier 2 regulation, moderate risk, or no immediate deadline
  - **Low**: Tier 3 or low risk, no deadline
  
- **Prioritization Matrix**:
  - Consider using Risk × Legal Obligation matrix
  - High risk + Tier 1 = Highest priority
  - Low risk + Tier 3 = Lowest priority

#### 4.3 Gap Remediation Approaches

How to close gaps:

**Write about:**
- **Add New Control**:
  - Create organization-specific control (see 3.5)
  - Most comprehensive approach
  - Highest effort
  
- **Enhance Existing Control**:
  - Expand scope of existing control to cover requirement
  - Less effort than new control
  - Update control documentation
  
- **Implement Compensating Control**:
  - Alternative control that achieves same outcome
  - When primary control not feasible
  - Document equivalence
  
- **Risk Acceptance**:
  - Document decision NOT to implement control
  - Requires executive approval
  - Justify with risk/benefit analysis
  - Document potential consequences
  - Time-bound (re-evaluate periodically)
  
- **Roadmap for Remediation**:
  - Timeline for gap closure
  - Milestones
  - Resource requirements
  - Responsible parties
  - Progress tracking

#### 4.4 Gap Tracking and Reporting

**Write about:**
- **Gap Register**:
  - List of all identified gaps
  - Priority, remediation approach, timeline, owner
  - Status tracking (open, in progress, closed)
  
- **Reporting**:
  - Regular gap status reports to management
  - Highlight high-priority gaps
  - Track remediation progress
  - Escalate stalled remediations
  
- **Integration**:
  - Gaps feed into risk register
  - Gaps inform compliance dashboard
  - Gaps considered in management reviews

### STRUCTURE:
```
4.1 Gap Identification
    4.1.1 What is a Gap?
    4.1.2 Types of Gaps
    4.1.3 Gap Detection
4.2 Gap Prioritization
    4.2.1 Prioritization Factors
    4.2.2 Priority Levels
    4.2.3 Prioritization Matrix
4.3 Gap Remediation Approaches
    4.3.1 Add New Control
    4.3.2 Enhance Existing Control
    4.3.3 Implement Compensating Control
    4.3.4 Risk Acceptance
    4.3.5 Roadmap for Remediation
4.4 Gap Tracking and Reporting
    4.4.1 Gap Register
    4.4.2 Reporting
    4.4.3 Integration
```

**Estimated Length**: 2-3 pages

---

## SECTION 5: Traceability Requirements

### WRITING INSTRUCTIONS:
Define how traceability is maintained throughout the framework.

Traceability = ability to trace from regulation → requirement → control → evidence and reverse.

### KEY CONTENT:

#### 5.1 Forward Traceability

From regulation to evidence:

**Write about:**
- **Traceability Chain**:
  ```
  Regulation (ISMS-POL-00)
      ↓ [extracted via S2 process]
  Requirement (Requirements Register)
      ↓ [mapped via S3 process]
  ISO 27001 Control (Control Mapping Matrix)
      ↓ [implemented via control owner]
  Control Implementation (policies, procedures, systems)
      ↓ [demonstrated via evidence]
  Compliance Evidence (Evidence Register)
  ```
  
- **Why Forward Traceability Matters**:
  - Shows HOW regulation is satisfied
  - Demonstrates completeness (all requirements covered)
  - Supports compliance reporting
  - Prepares for audits

#### 5.2 Reverse Traceability

From evidence back to regulation:

**Write about:**
- **Reverse Chain**:
  ```
  Compliance Evidence
      ↑ [proves implementation of]
  Control Implementation
      ↑ [which satisfies]
  ISO 27001 Control
      ↑ [which is mapped to]
  Requirement
      ↑ [which was extracted from]
  Regulation
  ```
  
- **Why Reverse Traceability Matters**:
  - Shows WHY a control exists (regulatory driver)
  - Supports change impact analysis (if regulation changes, what's affected?)
  - Identifies redundancy (controls no longer needed)
  - Demonstrates value of controls to business

#### 5.3 Change Traceability

When something changes, trace the impact:

**Write about:**
- **Regulation Changes**:
  - Identify affected requirements (Requirements Register)
  - Identify affected controls (Control Mapping Matrix)
  - Assess control implementation impact
  - Update evidence as needed
  
- **Control Changes**:
  - Identify which requirements are affected
  - Verify continued satisfaction of requirements
  - Update mapping if needed
  - Update evidence
  
- **Organizational Changes**:
  - If [Organization] changes (new jurisdiction, new services)
  - May trigger new applicability (S2)
  - May create new requirements
  - May require new controls

#### 5.4 Audit Trail

Every change must be logged:

**Write about:**
- **What to Log**:
  - Who made the change
  - When change was made
  - What was changed (before/after)
  - Why change was made (rationale)
  - Who approved change
  
- **Where Logs Are Maintained**:
  - Requirements Register: version history
  - Control Mapping Matrix: version history
  - Evidence Register: verification records
  - All changes centrally logged
  
- **Audit Trail Uses**:
  - Demonstrates framework is actively maintained
  - Shows due diligence
  - Supports compliance audits
  - Enables forensic review if needed

### STRUCTURE:
```
5.1 Forward Traceability
    5.1.1 Traceability Chain
    5.1.2 Why Forward Traceability Matters
5.2 Reverse Traceability
    5.2.1 Reverse Chain
    5.2.2 Why Reverse Traceability Matters
5.3 Change Traceability
    5.3.1 Regulation Changes
    5.3.2 Control Changes
    5.3.3 Organizational Changes
5.4 Audit Trail
    5.4.1 What to Log
    5.4.2 Where Logs Are Maintained
    5.4.3 Audit Trail Uses
```

**Estimated Length**: 2 pages

---

## SECTION 6: Handling Overlapping Requirements

### WRITING INSTRUCTIONS:
Define how to handle situation where multiple regulations require the same thing.

### KEY CONTENT:

#### 6.1 Identifying Overlapping Requirements

**Write about:**
- **Common Scenario**:
  - Multiple regulations may require similar controls
  - Example: GDPR, CCPA, and HIPAA all require encryption
  - Don't need to implement encryption three times
  
- **Overlap Detection**:
  - During requirements extraction, note similarities
  - During control mapping, multiple requirements map to same control
  - Control Mapping Matrix shows this visually (one column with many rows)

#### 6.2 Identifying the Most Stringent Requirement

When requirements overlap, comply with the most stringent:

**Write about:**
- **Why Most Stringent?**:
  - Satisfying the highest bar satisfies all lower bars
  - Efficiency: implement once to highest standard
  
- **Stringency Comparison**:
  - Compare technical specifications (AES-128 vs. AES-256 → 256 is more stringent)
  - Compare process requirements (annual review vs. quarterly → quarterly more stringent)
  - Compare documentation requirements (policy vs. policy + procedure → latter more stringent)
  
- **Documentation**:
  - Document which requirement is most stringent
  - Document that implementation satisfies all overlapping requirements

#### 6.3 Demonstrating Compliance with All Applicable Regulations

**Write about:**
- **Compliance Documentation**:
  - One control implementation
  - Evidence shows it satisfies all relevant requirements
  - Mapping matrix shows all requirements satisfied by control
  
- **Audit Preparation**:
  - Auditor for Regulation A: show evidence for Requirement from Reg A
  - Auditor for Regulation B: show SAME evidence for Requirement from Reg B
  - Efficiency: collect evidence once, use multiple times
  
- **Reporting**:
  - Compliance dashboard shows compliance across all regulations
  - Leveraging overlapping controls

#### 6.4 Evidence Optimization

**Write about:**
- **One Evidence Source, Multiple Requirements**:
  - Encryption policy satisfies GDPR, CCPA, HIPAA requirements
  - Access control logs satisfy multiple regulations
  - Don't duplicate evidence unnecessarily
  
- **Evidence Tagging**:
  - Tag evidence with all requirements it satisfies
  - Easy retrieval for audits
  - Shows efficiency

### STRUCTURE:
```
6.1 Identifying Overlapping Requirements
    6.1.1 Common Scenario
    6.1.2 Overlap Detection
6.2 Identifying the Most Stringent Requirement
    6.2.1 Why Most Stringent?
    6.2.2 Stringency Comparison
    6.2.3 Documentation
6.3 Demonstrating Compliance with All Applicable Regulations
    6.3.1 Compliance Documentation
    6.3.2 Audit Preparation
    6.3.3 Reporting
6.4 Evidence Optimization
    6.4.1 One Evidence Source, Multiple Requirements
    6.4.2 Evidence Tagging
```

**Estimated Length**: 1-2 pages

---

## SECTION 7: Document Control & Related Documents

### WRITING INSTRUCTIONS:
Standard document control section.

### CONTENT:
1. **Document Information**:
   - Document ID: ISMS-POL-A.5.31-S3
   - Version: 1.0
   - Effective Date: [Date]
   - Review Frequency: Annually or upon significant change
   - Next Review Date: [Date]

2. **Approval**:
   ```
   | Role | Name | Signature | Date |
   | ISMS Manager | | | |
   | Compliance Officer | | | |
   | Control Owners (Representative) | | | |
   | Executive Management | | | |
   ```

3. **Version History**:
   ```
   | Version | Date | Author | Changes |
   | 1.0 | [Date] | [Name] | Initial release |
   ```

4. **Related Documents**:
   - ISMS-POL-A.5.31-S1: Executive Summary & Control Alignment
   - ISMS-POL-A.5.31-S2: Regulatory Applicability Methodology
   - ISMS-POL-00: Regulatory Applicability Framework
   - ISMS-POL-A.5.31-S4: Change Management & Evidence (coming next)
   - ISMS-IMP-A.5.31-S2: Requirements Extraction Process (step-by-step)
   - ISMS-IMP-A.5.31-S3: Control Mapping Process (step-by-step)
   - Assessment Workbook 3: Requirements Extraction
   - Assessment Workbook 4: Control Mapping Matrix
   - ISO 27001:2022 Annex A (list of 93 controls)

**Estimated Length**: 0.5-1 page

---

## QUALITY CHECKS FOR S3

Before considering S3 complete, verify:

- [ ] Requirements extraction process is systematic and repeatable
- [ ] Granularity guidelines are clear
- [ ] Categorization framework is defined
- [ ] Requirements Register structure is comprehensive
- [ ] Mapping methodology is clear and systematic
- [ ] Mapping types (P/S/Su/N/A) are well-defined
- [ ] Mapping matrix structure is explained
- [ ] One-to-many and many-to-one scenarios addressed
- [ ] Beyond Annex A approach (new controls) is defined
- [ ] Gap analysis process is comprehensive
- [ ] Gap prioritization is risk-based
- [ ] Gap remediation options are clear
- [ ] Traceability (forward, reverse, change) is defined
- [ ] Audit trail requirements are specified
- [ ] Overlapping requirements approach is clear
- [ ] Evidence optimization is addressed
- [ ] Generic and industry-agnostic (no specific regulations)
- [ ] Integration with S2 (applicability) and S4 (evidence) is clear
- [ ] Total length: 10-12 pages

---

## WRITING SEQUENCE NOTES

**When writing this document:**
1. Introduction and context (builds on S2)
2. Requirements extraction (the translation process)
3. Control mapping (the core methodology)
4. Gap analysis (identifying and managing compliance risks)
5. Traceability (the thread connecting everything)
6. Overlapping requirements (efficiency)
7. Document control (standard)

**Voice and Tone:**
- Systematic and methodical
- Bridge between legal and technical language
- Emphasize traceability and auditability
- Process-oriented with clear steps

**Integration Points to Emphasize:**
- S2 output (applicable regulations) is input to this process
- Requirements Register is key artifact
- Control Mapping Matrix is key artifact
- S4 will cover evidence management (reference forward)
- IMP-S2 and IMP-S3 provide operational details
- Assessment Workbooks 3 and 4 are the tools

---

## READY FOR CONTENT DEVELOPMENT

This skeleton provides the structure for ISMS-POL-A.5.31-S3.

**Next Steps After Completion:**
1. User reviews and approves S3
2. Proceed to S4 (Change Management & Evidence)

---

END OF SKELETON
