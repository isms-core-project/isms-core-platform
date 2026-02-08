**ISMS-IMP-A.5.31.4-UG - Control Mapping Process**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.31: Legal, Statutory, Regulatory and Contractual Requirements

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Control Mapping Process |
| **Document Type** | Implementation Guide |
| **Document ID** | ISMS-IMP-A.5.31.4-UG |
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
| 1.0 | [Date] | CISO/ISO | Initial implementation guide for ISO 27001:2022 first certification |

---

**Audience:** Security assessors, Control owners, Compliance officers

---

# Process Overview

## Purpose

This implementation guide operationalizes the control mapping framework defined in ISMS-POL-A.5.31.3. It provides step-by-step instructions for compliance and security personnel to systematically map regulatory requirements to ISO 27001:2022 Annex A controls, identify gaps, and develop remediation plans.

**What This Guide Is**:

- Operational "how-to" for performing control mapping exercises
- Structured process from requirement analysis through gap remediation
- Practical decision-making framework for determining mapping types
- Quality assurance and validation methodology

**What This Guide Is Not**:

- Control implementation guide (that's control-specific documentation)
- Requirements extraction methodology (that's IMP-5.31.3)
- Evidence collection process (that's IMP-5.31.5)

## When to Use This Process

**Trigger Events**:

1. **New Requirements Extracted**: Requirements extracted from newly applicable regulation (via IMP-5.31.3)
2. **Regulatory Amendment**: Existing regulation updated, new requirements added
3. **ISMS Evolution**: New ISO 27001 controls implemented, need to map to existing requirements
4. **Periodic Review**: Annual comprehensive review of all mappings
5. **Gap Analysis**: Systematic assessment of control coverage
6. **Audit Preparation**: Pre-audit validation of control mappings and evidence
7. **Compliance Demonstration**: External stakeholder (customer, regulator, certifier) requests proof of compliance

## Who Performs This Process

**Primary Roles**:

- **ISMS Manager**: Leads mapping process, coordinates between compliance and technical teams, approves mappings
- **Compliance Officer**: Provides regulatory interpretation, validates that mappings satisfy requirements
- **Control Owners**: Confirm controls can satisfy mapped requirements, provide implementation details

**Supporting Roles**:

- Legal Counsel: Interpret complex regulatory language, validate legal sufficiency of mappings
- Information Security Team: Technical assessment of control capabilities
- Internal Audit: Independent validation of mapping accuracy

## Process Flowchart

```
[Input: Requirements Register from IMP-5.31.3]
         ↓
[STEP 1: Preparation]

- Review extracted requirements
- Prepare Control Mapping Matrix
- Identify ISO 27001 controls available

         ↓
[STEP 2: Requirement-by-Requirement Analysis]
For each requirement:

  - Understand requirement objective
  - Identify candidate controls
  - Assess control-to-requirement fit

         ↓
[STEP 3: Mapping Assignment]
For each requirement-control pair:

  - Assign mapping type (Primary, Secondary, Supporting, N/A)
  - Document rationale
  - Note any limitations

         ↓
[STEP 4: Gap Identification]
For each requirement:

  - Has Primary mapping? → No Gap
  - Only Secondary/Supporting? → Partial Gap
  - No mappings? → Complete Gap

         ↓
[STEP 5: Gap Analysis & Prioritization]

- Categorize gaps (Complete, Partial, Implementation)
- Prioritize by regulatory tier, deadline, severity
- Consult stakeholders (legal, control owners)

         ↓
[STEP 6: Remediation Planning]
For each gap:

  - Determine remediation approach
  - Develop remediation plan
  - Assign responsibility and timeline

         ↓
[STEP 7: Documentation & Approval]

- Complete Control Mapping Matrix
- Generate Gap Register
- Route for approval

         ↓
[STEP 8: Integration]

- Update Requirements Register with control mappings
- Add gaps to remediation tracking
- Communicate to stakeholders

         ↓
[Complete - Proceed to Evidence Management (IMP-5.31.5)]
```

## Timeline

**Small Regulation** (5-15 requirements):

- Preparation: 1-2 hours
- Mapping Analysis: 4-8 hours
- Gap Analysis: 2-4 hours
- Documentation: 2-3 hours
- **Total**: 1-2 days

**Medium Regulation** (15-50 requirements):

- Preparation: 2-4 hours
- Mapping Analysis: 1-2 days
- Gap Analysis: 4-8 hours
- Documentation: 4-6 hours
- **Total**: 3-5 days

**Large Regulation** (50+ requirements):

- Preparation: 1 day
- Mapping Analysis: 3-5 days
- Gap Analysis: 1-2 days
- Documentation: 1 day
- **Total**: 1-2 weeks

**Comprehensive ISMS Review** (all regulations):

- **Total**: 2-4 weeks (depending on regulatory scope)

## Prerequisites

**Before Beginning Control Mapping**:

✅ Requirements extracted and documented in Requirements Register (IMP-5.31.3 complete)  
✅ Requirements approved by Legal Counsel and Compliance Officer  
✅ ISO 27001:2022 Annex A controls inventory available  
✅ Statement of Applicability (SoA) current (know which controls are implemented)  
✅ Control Owners identified and available for consultation  
✅ Control Mapping Matrix template prepared (Workbook 4)

---

# Detailed Process Steps

## Step 1: Preparation

### Review Requirements Register

**Actions**:
1. **Access Requirements Register** (Workbook 3 from IMP-5.31.3)
2. **Filter to regulation** being mapped (if mapping one regulation at a time)
3. **Review each requirement**:

   - Read Interpreted Requirement (actionable version)
   - Understand Category (Technical, Organizational, Reporting, Operational)
   - Note Priority (High, Medium, Low)
   - Identify any dependencies between requirements

**Output**: Clear understanding of requirements scope and complexity

### Prepare Control Mapping Matrix

**Actions**:
1. **Open Control Mapping Matrix** (Workbook 4)
2. **Import requirements** from Requirements Register:

   - Requirement ID
   - Interpreted Requirement (brief version)
   - Category
   - Priority

3. **Verify ISO 27001 controls** listed (all 93 Annex A controls as columns)
4. **Set up workspace**: Large screen or dual monitors recommended (wide matrix)

**Output**: Control Mapping Matrix ready for population

### Review ISO 27001 Controls Inventory

**Actions**:
1. **Access ISO 27001 Controls Reference** (Workbook 4, Sheet 2)
2. **Review control categories**:

   - Section 5: Organizational Controls (37 controls)
   - Section 6: People Controls (8 controls)
   - Section 7: Physical Controls (14 controls)
   - Section 8: Technological Controls (34 controls)

3. **Review Statement of Applicability** to know:

   - Which controls are implemented (can map to these)
   - Which controls are excluded (generally cannot map to these unless reconsidering exclusion)
   - Implementation status of each control

**Output**: Understanding of available controls and their implementation status

### Assemble Stakeholders

**Actions**:
1. **Schedule mapping sessions** (if collaborative):

   - ISMS Manager (facilitator)
   - Compliance Officer (regulatory expertise)
   - 2-3 Control Owners (technical/operational expertise)

2. **Prepare materials**:

   - Requirements Register printout or shared screen
   - Control Mapping Matrix (collaborative editing if possible)
   - ISO 27001 standard text (for control descriptions)

**Output**: Team ready to conduct mapping exercise

---

## Step 2: Requirement-by-Requirement Analysis

For each requirement in the Requirements Register, perform this analysis:

### Understand Requirement Objective

**Question**: What security outcome does this requirement mandate?

**Actions**:
1. **Read Interpreted Requirement** (actionable version from IMP-5.31.3)
2. **Identify security objective**:

   - Confidentiality protection?
   - Integrity assurance?
   - Availability guarantee?
   - Accountability/audit trail?
   - Risk management?
   - Compliance demonstration?

3. **Understand regulatory intent**: Why does regulator mandate this? What harm are they preventing?
4. **Note any specific technical or organizational mandates**: Does regulation prescribe HOW (e.g., "shall use encryption") or just WHAT (e.g., "shall protect data")?

**Example**:
```
Requirement ID: REQ-GDPR-32-001
Interpreted Requirement: "Implement encryption for personal data at rest and in transit"

Security Objective: Confidentiality protection for personal data
Regulatory Intent: Prevent unauthorized access if data is stolen or intercepted
Specific Mandate: YES - explicitly requires encryption (not just "appropriate security")

→ Need controls that implement encryption specifically
```

### Identify Candidate Controls

**Question**: Which ISO 27001 controls could potentially satisfy this requirement?

**Strategy**: Think broad initially, narrow later.

**Approach A: Category-Based** (for Technical requirements)

- If requirement is Technical → Focus on Section 8 (Technological Controls)
- If requirement is Organizational → Focus on Section 5 (Organizational Controls)
- If requirement is People-related → Focus on Section 6 (People Controls)
- If requirement is Physical → Focus on Section 7 (Physical Controls)

**Approach B: Keyword Search** (for complex requirements)

- Search ISO 27001 control names/descriptions for keywords from requirement
- Example: Requirement mentions "access control" → Look at A.5.15 through A.5.18

**Approach C: Objective-Based** (for outcome-focused requirements)

- If requirement mandates confidentiality → Consider A.5.10, A.5.13, A.5.14, A.8.24
- If requirement mandates logging → Consider A.8.15, A.8.16
- If requirement mandates testing → Consider A.8.8, A.8.29

**Typical Candidates by Requirement Type**:

| Requirement Type | Likely Candidate Controls | Examples |
|------------------|---------------------------|----------|
| **Encryption** | A.8.24 (Cryptography) | Personal data encryption, transmission security |
| **Access Control** | A.5.15-A.5.18, A.8.3 | User access management, authentication, authorization |
| **Logging/Monitoring** | A.8.15-A.8.16 | Security event logging, audit trails |
| **Incident Response** | A.5.24-A.5.28 | Breach notification, incident management |
| **Vendor/Supplier** | A.5.19-A.5.23 | Third-party risk, cloud security, supply chain |
| **Data Protection** | A.5.10, A.5.34, A.8.10-A.8.12 | Data classification, retention, deletion |
| **Security Testing** | A.8.8, A.8.29 | Vulnerability management, penetration testing |
| **Training/Awareness** | A.6.3 | Security awareness and training |
| **Physical Security** | A.7.1-A.7.14 | Physical access, environmental controls |
| **Business Continuity** | A.5.29-A.5.30 | Disaster recovery, continuity planning |
| **Policy/Governance** | A.5.1-A.5.7 | Information security policies, roles, responsibilities |

**Actions**:
1. Based on requirement objective and type, identify 3-10 candidate controls
2. List candidates in working notes (not yet in matrix)
3. If unsure, err on side of including more candidates (will narrow in next step)

**Example**:
```
Requirement: "Implement breach notification process to notify data subjects within 72 hours"

Candidate Controls:

- A.5.24 (Information Security Incident Management Planning)
- A.5.25 (Assessment and Decision on Information Security Events)
- A.5.26 (Response to Information Security Incidents)
- A.5.27 (Learning from Information Security Incidents)
- A.5.28 (Collection of Evidence)
- Possibly A.5.6 (Contact with Authorities) - for notification to regulators

→ 6 candidates identified for further analysis
```

### Assess Control-to-Requirement Fit

For each candidate control, assess HOW WELL it satisfies the requirement.

**Assessment Framework**:

**Primary Mapping (P)**: Control directly and substantially satisfies requirement

- **Criteria**:
  - Control's objective aligns with requirement's objective
  - Control's implementation, if complete, would satisfy requirement
  - This is the "go-to" control for auditors to examine
  - Requirement would be considered "met" if this control is implemented
- **Test**: "If auditor asked how we satisfy Requirement X, would we primarily point to this control?"

**Secondary Mapping (S)**: Control partially satisfies requirement

- **Criteria**:
  - Control addresses PART of the requirement but not all
  - Control contributes to satisfaction but additional controls needed
  - Control is relevant but not sufficient alone
- **Test**: "Does this control help satisfy the requirement but is incomplete on its own?"

**Supporting Mapping (Su)**: Control indirectly supports requirement

- **Criteria**:
  - Control doesn't directly satisfy requirement but enables/supports other controls that do
  - Control provides context, foundation, or complementary capability
  - Requirement could be met without this control, but this control makes it easier/better
- **Test**: "Does this control make satisfaction easier but isn't directly responsible for satisfaction?"

**No Mapping (Blank)**: Control not applicable to requirement

- **Criteria**:
  - Control has no relationship to requirement
  - Control addresses completely different security objective
  - Mapping would be a stretch or misleading
- **Test**: "Would including this control in a compliance discussion confuse rather than clarify?"

**Assessment Questions**:

For each candidate control → requirement pair, ask:

1. **Scope**: Does control's scope cover what requirement mandates?

   - Example: Requirement = "Protect customer data" / Control = A.8.24 Cryptography
   - If A.8.24 is scoped to encrypt customer data → Good fit
   - If A.8.24 only encrypts internal secrets, not customer data → Poor fit

2. **Completeness**: Does control fully address requirement, or only part?

   - Example: Requirement = "Implement access controls including authentication, authorization, and logging"
   - A.5.15 Access Control Policy → Secondary (policy, not implementation)
   - A.5.16 Identity Management → Secondary (partial - authentication only)
   - A.5.17 Authentication Information → Secondary (partial - authentication only)
   - A.5.18 Access Rights → Secondary (partial - authorization only)
   - A.8.15 Logging → Secondary (partial - logging only)
   - Combination of A.5.16 + A.5.17 + A.5.18 + A.8.15 → Primary (all together)

3. **Directness**: Is control directly responsible, or does it support other controls?

   - Example: Requirement = "Conduct annual penetration testing"
   - A.8.8 Vulnerability Management → Primary (includes penetration testing)
   - A.8.29 Security Testing → Primary (testing controls)
   - A.5.1 Policies → Supporting (policies mandate testing but don't implement it)

4. **Implementation Status**: Is control actually implemented?

   - If control is excluded from SoA → Generally cannot map (unless reconsidering exclusion)
   - If control is planned but not implemented → Note as "Gap" (mapping exists conceptually but implementation gap)

**Decision Matrix**:

| Control Fit Assessment | Mapping Type | Notes |
|------------------------|--------------|-------|
| Directly satisfies entire requirement | **Primary (P)** | This is the main control for this requirement |
| Satisfies major part of requirement, minor gaps | **Primary (P)** | Document minor gap, may need small enhancement |
| Satisfies significant part, but substantial part missing | **Secondary (S)** | Need additional controls for full satisfaction |
| Contributes meaningfully but incomplete alone | **Secondary (S)** | Part of a control set |
| Provides foundation or enabler for other controls | **Supporting (Su)** | Indirect contribution |
| Tangentially related but not really relevant | **Blank** | Don't map - misleading |
| Completely unrelated | **Blank** | Don't map |

**Example Analysis**:
```
Requirement: "Implement encryption for personal data at rest and in transit"

Candidate Control: A.8.24 Use of Cryptography

Assessment:

- Scope: A.8.24 covers cryptography policy and key management
- Completeness: If A.8.24 implementation includes encrypting personal data at rest and in transit → Complete
- Directness: Directly responsible for encryption
- Implementation Status: Check SoA - if implemented, can map

Decision: PRIMARY (P)
Rationale: A.8.24 directly addresses encryption requirement, and if implemented for personal data, fully satisfies requirement.

---

Candidate Control: A.8.10 Information Deletion

Assessment:

- Scope: A.8.10 covers secure deletion, not encryption
- Completeness: Doesn't address encryption requirement
- Directness: N/A
- Implementation Status: N/A

Decision: BLANK (No mapping)
Rationale: Completely different security objective (deletion vs encryption). Including would be misleading.

---

Candidate Control: A.5.10 Acceptable Use of Information

Assessment:

- Scope: A.5.10 covers policies on how users should handle information
- Completeness: Might mandate users use encrypted channels, but doesn't implement encryption
- Directness: Indirect - policy supports, but doesn't implement
- Implementation Status: Check SoA

Decision: SUPPORTING (Su)
Rationale: Policy may require encrypted transmission, which supports requirement, but actual encryption is implemented by A.8.24.
```

---

## Step 3: Mapping Assignment

### Populate Control Mapping Matrix

**Actions**:
1. **For each requirement** (row in matrix):
2. **For each assessed control** (column in matrix):
3. **Enter mapping type** in cell:

   - **P** = Primary
   - **S** = Secondary
   - **Su** = Supporting
   - **Blank** = No mapping

**Data Entry**:

- Use dropdown data validation (prevents typos)
- Consistency is critical (always use "P", not "Primary" or "p")
- Most cells will be blank (requirements typically map to 1-5 controls)

**Example Matrix**:
```
| Req ID | Requirement | A.5.1 | A.5.15 | A.5.16 | A.8.15 | A.8.24 | ... |
|--------|-------------|-------|--------|--------|--------|--------|-----|
| REQ-001| Encryption  |       |        |        |        | P      | ... |
| REQ-002| Access Ctrl |       | S      | P      | S      |        | ... |
| REQ-003| Logging     |       |        |        | P      |        | ... |
```

### Document Mapping Rationale

**For Primary Mappings**:

- Brief note on WHY this control primarily satisfies requirement
- Document in separate "Mapping Notes" sheet or comments

**For Complex Mappings** (multiple Primary, or unusual mappings):

- Detailed rationale explaining how controls work together
- If requirement needs 3+ Primary controls, explain why each is necessary

**For Gaps** (requirements with no Primary):

- Note explicitly that gap exists (will be documented in Step 4)

**Example Rationale**:
```
Requirement REQ-GDPR-32-001: Encryption for personal data at rest and in transit

Primary Mapping: A.8.24 Use of Cryptography
Rationale: A.8.24 implements AES-256 encryption for all personal data at rest (database encryption) and TLS 1.3 for data in transit (API communications). This directly satisfies GDPR Article 32(1)(a) encryption requirement.

Supporting Mapping: A.5.10 Acceptable Use of Information
Rationale: A.5.10 policy requires employees to use encrypted channels when transmitting personal data. Supports A.8.24 implementation by mandating compliant behavior.
```

### Handle Multi-Control Requirements

**Scenario**: Requirement needs MULTIPLE controls working together (no single control sufficient)

**Approach**:
1. **Identify all controls needed** for complete satisfaction
2. **Mark each as Primary (P)** if each is essential
3. **Document how they work together** in mapping notes

**Example**:
```
Requirement REQ-SEC-05: "Implement comprehensive access management including identity lifecycle, authentication, authorization, and access reviews"

Mappings:

- A.5.16 Identity Management → P (identity lifecycle)
- A.5.17 Authentication Information → P (authentication)
- A.5.18 Access Rights → P (authorization and reviews)
- A.8.3 Information Access Restriction → P (technical enforcement)

Rationale: This requirement mandates a complete access management system. Each control addresses one component:

- A.5.16: Creating, modifying, revoking identities
- A.5.17: Password/MFA management
- A.5.18: Granting, reviewing, revoking access rights
- A.8.3: Technical controls enforcing access restrictions

All four are PRIMARY because requirement cannot be satisfied without any of them.
```

### Handle One-to-Many Control Mappings

**Scenario**: One control satisfies MULTIPLE requirements

**Approach**:
1. **Map control to each applicable requirement** (control reuse is good!)
2. **Specify which aspect of control** satisfies each requirement (may be different aspects)
3. **Collect evidence once** (one control, one evidence set) but reference in multiple requirement contexts

**Example**:
```
Control A.8.15 Logging:

Maps to:

- REQ-GDPR-30: "Maintain records of processing activities" → P
- REQ-PCI-10: "Track and monitor all access to network resources and cardholder data" → P
- REQ-SOX-404: "Log changes to financial systems" → S (partial - need additional controls for SOX)
- REQ-HIPAA-164.312(b): "Implement hardware, software, and procedural mechanisms that record and examine activity" → P

Rationale: Single logging implementation (centralized SIEM) satisfies multiple regulatory logging requirements. Same logs, same evidence, multiple regulatory contexts.
```

---

## Step 4: Gap Identification

### Automated Gap Detection

**Process**: Review Control Mapping Matrix row-by-row

**For each requirement row**:

**Test 1: Count Primary Mappings**
```
IF count(P in row) = 0:
  → FLAG: Potential gap (no primary control)
ELSE:
  → No gap at mapping level
```

**Test 2: Count Any Mappings**
```
IF count(P, S, Su in row) = 0:
  → FLAG: Complete gap (no controls at all)
ELSE IF count(P) = 0 AND count(S or Su) > 0:
  → FLAG: Partial gap (secondary/supporting only, no primary)
ELSE:
  → Continue
```

**Output**: List of requirements with gaps

### Gap Categorization

**Complete Gap**: Requirement has NO control mappings (not even Secondary or Supporting)

- **Meaning**: Requirement is not addressed AT ALL by current ISMS
- **Risk**: High - complete non-compliance
- **Action Needed**: Implement new control(s)

**Partial Gap**: Requirement has Secondary or Supporting mappings but NO Primary mapping

- **Meaning**: Requirement is partially addressed but not fully satisfied
- **Risk**: Medium - partial compliance but insufficient for audit
- **Action Needed**: Enhance existing controls or add additional controls

**Implementation Gap**: Requirement has Primary mapping but control not yet implemented

- **Meaning**: Conceptual mapping exists, but control is "planned" or "in progress" in SoA
- **Risk**: Medium - know what to do, but haven't done it yet
- **Action Needed**: Complete control implementation

**Example Gap Analysis**:
```
Requirements with Gaps (Sample):

REQ-GDPR-35: "Conduct Data Protection Impact Assessments (DPIA) for high-risk processing"

- Mappings: None (blank row)
- Gap Type: Complete Gap
- Risk: High - GDPR mandates DPIAs, we have no process

REQ-PCI-11.3: "Implement penetration testing at least annually"

- Mappings: A.8.8 Vulnerability Management (S), A.8.29 Security Testing (S)
- Gap Type: Partial Gap
- Risk: Medium - have vulnerability scanning (A.8.8) and some testing (A.8.29), but no formal annual penetration test
- Action: Enhance A.8.29 to explicitly include annual penetration testing

REQ-SOX-404: "Automated logging of all financial system changes"

- Mappings: A.8.15 Logging (P)
- Implementation Status: A.8.15 is "Planned" in SoA (not yet implemented)
- Gap Type: Implementation Gap
- Risk: Medium - know what control needed, but not deployed yet
- Action: Accelerate A.8.15 implementation for financial systems

```

### Document Gaps in Gap Register

**Gap Register** (from Control Mapping Matrix, Sheet 4: Gap Summary):

For each identified gap, document:

| Field | Description | Example |
|-------|-------------|---------|
| **Gap ID** | Unique identifier | GAP-2025-001 |
| **Requirement ID** | Which requirement has gap | REQ-GDPR-35 |
| **Requirement Text** | Brief description | DPIA for high-risk processing |
| **Regulation** | Source regulation | GDPR Article 35 |
| **Gap Type** | Complete / Partial / Implementation | Complete |
| **Gap Description** | What is missing | No DPIA process exists |
| **Current State** | What controls exist (if partial gap) | N/A (complete gap) |
| **Risk/Impact** | Consequence of non-compliance | GDPR enforcement action, fines up to 4% revenue |
| **Priority** | Critical / High / Medium / Low | High |
| **Remediation Approach** | How gap will be closed | Implement new organizational control CTRL-ORG-005 "DPIA Process" |
| **Responsible Party** | Who will remediate | Privacy Officer |
| **Target Date** | When gap will be closed | 2025-06-30 |
| **Status** | Open / In Progress / Closed | Open |
| **Notes** | Additional context | Legal counsel reviewing DPIA template |

**Gap Documentation Example**:
```
Gap ID: GAP-2025-001
Requirement ID: REQ-GDPR-35
Requirement Text: Conduct Data Protection Impact Assessments (DPIA) for high-risk processing activities
Regulation: GDPR Article 35
Gap Type: Complete Gap
Gap Description: [Organization] has no formal DPIA process. No procedure, no template, no assessment history. When launching new products/services involving personal data, no systematic risk assessment is performed.
Current State: N/A (gap is complete)
Risk/Impact: 

  - Legal: GDPR Article 83(4) - fines up to €10M or 2% global annual turnover
  - Operational: May deploy high-risk processing without appropriate safeguards
  - Reputational: Privacy incidents due to inadequate risk assessment

Priority: HIGH (Tier 1 regulation, mandatory requirement, significant penalty)
Remediation Approach: Implement new organizational control "CTRL-ORG-005: Data Protection Impact Assessment Process"

  - Develop DPIA procedure
  - Create DPIA template (aligned with ICO/CNIL guidance)
  - Train privacy team and key stakeholders
  - Conduct DPIAs for existing high-risk processing (backlog)
  - Integrate DPIA into product/service launch workflow

Responsible Party: Privacy Officer (lead), supported by Legal Counsel and ISMS Manager
Target Date: 2025-06-30 (Q2 2025)
Status: Open
Assigned Date: 2025-01-10
Notes: Legal counsel reviewing DPIA template for legal sufficiency. Benchmarking against peer organizations' DPIA processes.
```

---

## Step 5: Gap Analysis & Prioritization

### Gap Prioritization Framework

Not all gaps are equally urgent. Use this framework to prioritize remediation:

**Factor 1: Regulatory Tier** (from ISMS-POL-00)

- **Tier 1 Mandatory**: Highest priority (legal obligation)
- **Tier 2 Conditional**: High priority IF condition applies
- **Tier 3 Informational**: Lower priority (best practice)

**Factor 2: Legal Consequence Severity**

- **Criminal Liability / Severe Fines**: Highest priority
  - Example: GDPR up to 4% revenue, PCI DSS v4.0.1 loss of card processing
- **Civil Penalties / Moderate Fines**: High priority
- **Reputational Damage**: Medium-High priority
- **Minor Penalties / Warnings**: Lower priority

**Factor 3: Compliance Deadline**

- **Overdue** (deadline passed): CRITICAL - already non-compliant
- **Imminent** (<30 days): CRITICAL - urgent action required
- **Near-term** (30-90 days): HIGH - plan immediate remediation
- **Medium-term** (90 days - 1 year): MEDIUM - planned remediation
- **Long-term** (>1 year): LOWER - strategic planning

**Factor 4: Implementation Complexity**

- **Quick Wins** (low complexity, high impact): Prioritize for fast closure
- **Complex, High-Impact**: Prioritize but plan carefully (phased approach)
- **Simple, Low-Impact**: Batch with similar gaps
- **Complex, Low-Impact**: Defer or accept risk

**Factor 5: Business Impact**

- **Revenue-Critical**: Highest priority (blocks business if non-compliant)
- **Customer-Facing**: High priority (SLA, customer trust)
- **Internal Operations**: Medium priority
- **Non-Critical**: Lower priority

**Prioritization Decision Matrix**:

| Priority Level | Criteria | Action Timeline |
|----------------|----------|-----------------|
| **CRITICAL** | Tier 1 + Deadline passed or <30 days + Severe consequence + Revenue-critical | Immediate (1-30 days) |
| **HIGH** | Tier 1 + Deadline 30-90 days + Significant consequence + Customer-facing | Urgent (1-3 months) |
| **MEDIUM** | Tier 1 Partial Gap OR Tier 2 Complete Gap (if applicable) + Deadline 90 days - 1 year | Planned (3-12 months) |
| **LOW** | Tier 3 OR Implementation Gap + Deadline >1 year + Minor consequence | Strategic (12+ months or accept risk) |

**Example Prioritization**:

| Gap | Regulation | Tier | Deadline | Consequence | Complexity | Business Impact | **Priority** |
|-----|------------|------|----------|-------------|------------|-----------------|--------------|
| No breach notification process | GDPR | 1 | Immediate (72hr legal requirement) | Major fines | Low | Customer-facing | **CRITICAL** |
| No DPIA process | GDPR | 1 | No specific deadline | Major fines | Medium | Product launch | **HIGH** |
| Partial encryption (data at rest only) | PCI DSS v4.0.1 | 2 (applies if processing cards) | 90 days (next audit) | Lose card processing | Medium | Revenue-critical | **HIGH** |
| Annual penetration test missing | Industry best practice | 3 | None | Reputational | High | Internal | **LOW** |

### Stakeholder Consultation

**Before finalizing gap analysis**, consult key stakeholders:

**Legal Counsel**:

- Confirm gap interpretation is legally accurate
- Validate consequence severity assessment
- Confirm whether gap is true non-compliance or acceptable alternative approach

**Control Owners**:

- For Partial Gaps: Can existing control be enhanced to close gap?
- Confirm whether control CANNOT satisfy requirement (vs. not currently configured to satisfy)
- Estimate effort/cost to enhance existing control vs. implement new control

**Executive Management** (for CRITICAL/HIGH gaps):

- Communicate gap existence and risk
- Obtain buy-in for remediation resources (budget, staff, timeline)
- If risk acceptance considered, obtain formal approval

**Example Stakeholder Consultation**:
```
Gap: No annual penetration testing (mapped to A.8.29 Security Testing - Secondary only)

Consultation with Control Owner (CISO):
Q: "A.8.29 currently includes vulnerability scanning but not penetration testing. Can A.8.29 be enhanced to include annual penetration tests?"
A: "Yes - we can expand A.8.29 scope to include annual penetration test, either performed internally or by external firm. Estimated cost: €20K/year for external pentest, or hire penetration tester (€90K/year salary)."

Consultation with Legal Counsel:
Q: "Regulation requires 'penetration testing at least annually.' Does our current vulnerability scanning satisfy this, or is dedicated penetration test required?"
A: "Vulnerability scanning (automated) is distinct from penetration testing (manual exploitation). Regulation explicitly requires penetration testing. Current scanning does not satisfy. We have a gap."

Decision: Enhance A.8.29 to include annual external penetration test. Budget €20K/year. Upgrade mapping from S → P once implemented.
```

---

## Step 6: Remediation Planning

For each identified gap, develop remediation plan.

### Remediation Approaches

**Option 1: Implement New Control**

- **When**: Complete gap, no existing control addresses requirement
- **Process**:

  1. Define new control (may be organization-specific, beyond Annex A)
  2. Assign Control Owner
  3. Develop implementation plan (technical, organizational, procedural)
  4. Implement control
  5. Collect evidence
  6. Update Control Mapping Matrix (add new control, mark as Primary)
  7. Close gap in Gap Register

**Option 2: Enhance Existing Control**

- **When**: Partial gap, existing control is close but incomplete
- **Process**:

  1. Identify control needing enhancement
  2. Define enhancements (scope expansion, capability addition, better implementation)
  3. Control Owner implements enhancements
  4. Update control documentation
  5. Update evidence
  6. Update Control Mapping Matrix (potentially upgrade S → P)
  7. Close gap in Gap Register

**Option 3: Implement Combination of Controls**

- **When**: Complex requirement needs multiple controls together
- **Process**:

  1. Identify all controls needed (mix of Annex A and organizational)
  2. Assign owners (may be different for different controls)
  3. Coordinate implementation (controls must integrate)
  4. Document how combination satisfies requirement
  5. Collect evidence from each control
  6. Update Control Mapping Matrix (multiple Primary mappings)
  7. Close gap in Gap Register

**Option 4: Implement Compensating Control**

- **When**: Ideal control infeasible (technical, cost, operational constraints) but alternative achieves same objective
- **Process**:

  1. Document why ideal control cannot be implemented
  2. Identify compensating control achieving same security outcome
  3. Document compensating control rationale
  4. Obtain Legal Counsel and Management approval
  5. Implement compensating control
  6. Document as compensating in Control Mapping Matrix
  7. Close gap in Gap Register (with notation)

**Option 5: Accept Risk**

- **When**: Gap exists but cost exceeds risk, OR Low priority gap with resource constraints
- **Process**:

  1. Conduct risk assessment (likelihood and impact of non-compliance)
  2. Document rationale for accepting risk
  3. Obtain Executive Management approval (risk acceptance is executive decision)
  4. Document in Risk Register
  5. Monitor (reassess if circumstances change)
  6. Update Gap Register (gap remains Open but risk accepted)

- **Restrictions**:
  - CANNOT accept risk for Tier 1 Mandatory (legal obligation)
  - SHOULD NOT accept risk for High/Critical priority
  - MUST revisit if regulation changes or enforcement increases

### Develop Remediation Plan

**For each gap** (especially CRITICAL and HIGH priority):

**Remediation Plan Template**:

```markdown
# Remediation Plan: [Gap ID] - [Brief Description]

## Gap Summary

- **Gap ID**: GAP-2025-XXX
- **Requirement**: REQ-XXX - [Brief requirement description]
- **Regulation**: [Regulation name, citation]
- **Gap Type**: Complete / Partial / Implementation
- **Priority**: Critical / High / Medium / Low
- **Risk**: [Brief risk description]

## Remediation Approach
**Chosen Approach**: [New Control / Enhance Control / Combination / Compensating / Accept Risk]

**Rationale**: [Why this approach chosen]

## Implementation Plan

**Objective**: [What will be achieved - how requirement will be satisfied]

**Scope**:

- What will be implemented (technical, procedural, organizational)
- What is explicitly OUT of scope

**Activities**:
1. [Activity 1] - [Responsible party] - [Timeline]
2. [Activity 2] - [Responsible party] - [Timeline]
3. [Activity N] - [Responsible party] - [Timeline]

**Dependencies**:

- [Dependency 1 - what is needed before this can proceed]
- [Dependency 2]

**Resources Required**:

- Budget: [€X for software, consulting, etc.]
- Staff: [X FTE, roles needed]
- Technology: [Infrastructure, software licenses, etc.]
- Vendor: [If external vendor needed]

**Timeline**:

- Start Date: [YYYY-MM-DD]
- Milestone 1: [Description] - [Date]
- Milestone 2: [Description] - [Date]
- Completion Date: [YYYY-MM-DD]

## Success Criteria
How will we know remediation is complete?

- [ ] [Criterion 1 - specific, measurable]
- [ ] [Criterion 2]
- [ ] [Criterion 3]
- [ ] Evidence collected and documented
- [ ] Control Mapping Matrix updated
- [ ] Gap Register marked "Closed"

## Validation

- **Control Testing**: [How control will be tested]
- **Evidence Collection**: [What evidence will demonstrate control effectiveness]
- **Approval**: [Who must approve completion]

## Post-Implementation

- **Maintenance**: [Ongoing activities to maintain control]
- **Review Frequency**: [How often control reviewed]
- **Metrics**: [How control effectiveness measured]

## Approval

- [ ] Remediation Plan Approved by: [Control Owner] - Date: ______
- [ ] Budget Approved by: [Finance/Management] - Date: ______
- [ ] Implementation Approved by: [ISMS Manager] - Date: ______

```

**Example Remediation Plan**:
```markdown
# Remediation Plan: GAP-2025-001 - Data Protection Impact Assessment Process

## Gap Summary

- **Gap ID**: GAP-2025-001
- **Requirement**: REQ-GDPR-35 - Conduct Data Protection Impact Assessments (DPIA) for high-risk processing
- **Regulation**: GDPR Article 35
- **Gap Type**: Complete Gap
- **Priority**: HIGH
- **Risk**: GDPR enforcement (fines up to 2% revenue), privacy incidents, reputational damage

## Remediation Approach
**Chosen Approach**: Implement New Organizational Control (CTRL-ORG-005: DPIA Process)

**Rationale**: No existing control addresses DPIA requirement. This is a specialized privacy process mandated by GDPR. Must create dedicated control.

## Implementation Plan

**Objective**: Establish systematic DPIA process that identifies and mitigates privacy risks for high-risk processing activities, satisfying GDPR Article 35 requirements.

**Scope**:

- DPIA procedure document
- DPIA template/form
- Integration with product development lifecycle
- Training for privacy team and key stakeholders
- Conduct DPIAs for existing high-risk processing (backlog: 3 identified)
- OUT OF SCOPE: Transfer Impact Assessments (different requirement), algorithm audits (separate initiative)

**Activities**:
1. Research and Benchmarking (Week 1-2)

   - Review ICO, CNIL, EDPB DPIA guidance
   - Benchmark peer organization DPIA processes
   - Identify DPIA triggers specific to [Organization]
   - Responsible: Privacy Officer
   
2. Develop DPIA Procedure (Week 3-4)

   - Draft DPIA procedure document (when required, who performs, escalation)
   - Define DPIA triggers (thresholds for "high risk")
   - Create DPIA template/assessment form
   - Responsible: Privacy Officer, with Legal Counsel review
   
3. Stakeholder Review & Approval (Week 5)

   - Legal Counsel review for legal sufficiency
   - ISMS Manager review for integration with ISMS
   - Executive approval of DPIA procedure
   - Responsible: Privacy Officer (coordination)
   
4. Training (Week 6)

   - Train privacy team on DPIA execution
   - Brief product managers on DPIA requirements
   - Integrate DPIA into product launch checklist
   - Responsible: Privacy Officer (deliver training)
   
5. Backlog DPIAs (Week 7-10)

   - Conduct DPIA for Existing Processing #1 (Customer Analytics Platform)
   - Conduct DPIA for Existing Processing #2 (Automated Decision System)
   - Conduct DPIA for Existing Processing #3 (Biometric Authentication Pilot)
   - Document findings, mitigations, approvals
   - Responsible: Privacy Officer (lead), Data Protection Officer (approve)
   
6. Evidence Collection (Week 11)

   - Collect evidence: DPIA procedure document, completed DPIAs, training records
   - Upload to Evidence Register
   - Link to REQ-GDPR-35
   - Responsible: Compliance Officer
   
7. Control Mapping Update (Week 11)

   - Add CTRL-ORG-005 to Control Mapping Matrix as new control
   - Map REQ-GDPR-35 to CTRL-ORG-005 as Primary (P)
   - Update Gap Register: GAP-2025-001 → Closed
   - Responsible: ISMS Manager

**Dependencies**:

- Legal Counsel availability for template review (confirmed: available Week 3-4)
- Executive approval of DPIA procedure (scheduled: Week 5)
- Product team availability for training (confirmed: Week 6)

**Resources Required**:

- Budget: €5K (external privacy consultant for template review, training materials)
- Staff: Privacy Officer (0.5 FTE for 11 weeks), Legal Counsel (0.1 FTE), Compliance Officer (0.1 FTE)
- Technology: None (document-based process initially; may automate later)
- Vendor: Privacy consultant (€5K, 2-day engagement for template review and training support)

**Timeline**:

- Start Date: 2025-01-15
- Milestone 1: DPIA procedure approved - 2025-02-15
- Milestone 2: Training complete - 2025-02-28
- Milestone 3: All backlog DPIAs complete - 2025-03-31
- Completion Date: 2025-03-31 (11 weeks)

## Success Criteria
How will we know remediation is complete?

- [x] DPIA procedure document approved by Legal Counsel and Executive Management
- [x] DPIA template validated against GDPR Article 35 and EDPB guidance
- [x] Privacy team trained (attendance records, competency assessment)
- [x] All 3 backlog DPIAs completed and approved by DPO
- [x] DPIA integrated into product development process (launch checklist updated)
- [x] Evidence collected: procedure doc, 3 completed DPIAs, training records
- [x] Control Mapping Matrix updated: CTRL-ORG-005 added, REQ-GDPR-35 mapped Primary
- [x] Gap Register updated: GAP-2025-001 closed

## Validation

- **Control Testing**: Simulate DPIA for hypothetical new processing activity, verify DPIA procedure is followed correctly
- **Evidence Collection**: 
  - CTRL-ORG-005 Procedure Document v1.0 (approved, signed)
  - Completed DPIA #1: Customer Analytics Platform
  - Completed DPIA #2: Automated Decision System
  - Completed DPIA #3: Biometric Authentication Pilot
  - Training records (attendance, materials)
  - Product launch checklist (updated with DPIA requirement)
- **Approval**: DPO approves each completed DPIA, ISMS Manager approves control implementation

## Post-Implementation

- **Maintenance**: 
  - Review and update DPIA template annually (or when GDPR guidance evolves)
  - Conduct DPIAs for all new high-risk processing activities
  - Refresh training for new privacy team members
- **Review Frequency**: DPIA procedure reviewed annually, individual DPIAs reviewed when processing changes
- **Metrics**: 
  - Number of DPIAs conducted per year
  - % of high-risk processing activities with completed DPIA
  - Time from DPIA initiation to completion (target: <30 days)

## Approval

- [x] Remediation Plan Approved by: Privacy Officer - Date: 2025-01-10
- [x] Budget Approved by: CFO - Date: 2025-01-12
- [x] Implementation Approved by: ISMS Manager - Date: 2025-01-13

```

---

## Step 7: Documentation & Approval

### Finalize Control Mapping Matrix

**Actions**:
1. **Review all mappings**: Ensure no blank cells where mapping should exist
2. **Verify mapping consistency**: Similar requirements mapped similarly?
3. **Check for orphaned requirements**: Any requirement with NO mappings at all?
4. **Validate against requirements**: Do all requirements from Requirements Register appear in matrix?
5. **Add metadata**:

   - Mapping Version: 1.0
   - Mapping Date: [Date completed]
   - Mapped By: [Name]
   - Approved By: [To be filled after approval]

**Quality Checks**:

- [ ] All requirements from Requirements Register included
- [ ] Mapping types (P/S/Su) used correctly
- [ ] Gaps identified and documented
- [ ] Mapping rationale documented for complex cases
- [ ] Matrix formatted professionally (freeze panes, colors, etc.)

### Finalize Gap Register

**Actions**:
1. **Review all documented gaps**: Ensure all gaps from matrix appear in Gap Register
2. **Complete gap descriptions**: Every gap has description, risk, remediation approach
3. **Assign priorities**: Every gap has priority assigned (using framework from 2.5.1)
4. **Assign owners**: Every gap has responsible party
5. **Set target dates**: Every gap has target remediation date (realistic, approved)

**Quality Checks**:

- [ ] All gaps from Control Mapping Matrix documented
- [ ] Gap categorization (Complete/Partial/Implementation) accurate
- [ ] Priorities assigned using framework
- [ ] Remediation approaches defined
- [ ] Responsible parties assigned
- [ ] Target dates realistic and approved

### Prepare Approval Package

**Package Contents**:
1. **Control Mapping Matrix** (Workbook 4, main sheet)
2. **Gap Register** (Workbook 4, Gap Summary sheet)
3. **Mapping Summary**:

   - Total requirements mapped: [#]
   - Requirements with Primary mappings: [#] ([%])
   - Requirements with gaps: [#] ([%])
   - Gap breakdown: Complete [#], Partial [#], Implementation [#]
   - Priority breakdown: Critical [#], High [#], Medium [#], Low [#]

4. **Executive Summary** (1-2 pages):

   - What was mapped (which regulation)
   - Key findings (major gaps, strengths)
   - Recommendations (priority remediations)
   - Resource requirements (budget, staff, timeline)

**Example Executive Summary**:
```markdown
# Control Mapping Executive Summary
# GDPR Compliance Assessment - January 2025

## Overview
Completed control mapping for 42 requirements extracted from GDPR Articles 5, 24, 25, 28, 30, 32, 33, 34, 35, and 44.

## Key Findings

**Strengths**:

- 32 of 42 requirements (76%) have Primary control mappings
- Strong technical controls (encryption, access control, logging)
- Solid organizational governance (policies, procedures, roles)

**Gaps Identified**: 10 gaps requiring remediation

- **Complete Gaps** (5): 
  - No DPIA process (REQ-GDPR-35)
  - No international transfer safeguards (REQ-GDPR-44)
  - No data retention schedule (REQ-GDPR-05)
  - No DPO function (REQ-GDPR-37)
  - No breach notification process (REQ-GDPR-33)
  
- **Partial Gaps** (3):
  - Consent management incomplete (REQ-GDPR-07)
  - Records of processing activities informal (REQ-GDPR-30)
  - Data subject rights partially implemented (REQ-GDPR-12-22)
  
- **Implementation Gaps** (2):
  - Privacy by Design not fully operationalized (REQ-GDPR-25)
  - Data minimization policy exists but not enforced (REQ-GDPR-05)

## Priority Remediation

**CRITICAL** (2 gaps - immediate action required):
1. Breach Notification Process (€60K, 6 weeks)
2. DPO Function (€120K/year, 8 weeks to hire)

**HIGH** (5 gaps - Q1-Q2 2025):
3. DPIA Process (€5K, 11 weeks) - detailed plan attached
4. International Transfer Safeguards (€10K, 8 weeks)
5. Data Retention Schedule (€15K, 12 weeks)
6. Consent Management Enhancement (€25K, 10 weeks)
7. Records of Processing Activities (€8K, 6 weeks)

**MEDIUM** (3 gaps - Q2-Q3 2025):
8. Privacy by Design implementation (€40K, 16 weeks)
9. Data Subject Rights full implementation (€50K, 20 weeks)
10. Data Minimization enforcement (€12K, 8 weeks)

## Resource Requirements

- **Budget**: €345K total (€180K for CRITICAL+HIGH, €102K for MEDIUM, €63K contingency)
- **Staff**: Privacy Officer 1.0 FTE (new hire - DPO), Compliance Officer 0.3 FTE, Legal 0.2 FTE
- **Timeline**: Q1 2025 (CRITICAL) → Q2-Q3 2025 (HIGH+MEDIUM) → Q4 2025 (validation and audit prep)

## Recommendations
1. **Immediate**: Approve CRITICAL gap remediation budgets and authorize DPO hire
2. **Q1 2025**: Execute CRITICAL remediations (breach notification, DPO hire)
3. **Q1 2025**: Develop detailed plans for HIGH priority gaps
4. **Q2 2025**: Begin HIGH priority implementations
5. **Q4 2025**: Conduct gap validation audit (internal or external)
6. **2026**: Maintain, monitor, and improve

## Risk Statement
If CRITICAL gaps not remediated by Q1 2025, [Organization] is non-compliant with GDPR mandatory requirements (Articles 33, 37) and vulnerable to enforcement action. Immediate action required.

Prepared by: [ISMS Manager]
Date: 2025-01-15
```

### Approval Workflow

**Routing**:
1. **Control Owners** (affected by new mappings): Review and confirm controls can satisfy mapped requirements
2. **Compliance Officer**: Review for regulatory accuracy, approve gap categorization
3. **Legal Counsel**: Review for legal sufficiency, approve CRITICAL/HIGH gap remediation plans
4. **ISMS Manager**: Overall approval of mapping and gap register
5. **Executive Management** (for significant gaps/budgets): Approve resource allocation for remediation

**Approval Criteria**:

- [ ] Mappings accurate and defensible to auditor
- [ ] Gaps correctly identified and categorized
- [ ] Remediation plans realistic and resourced
- [ ] Priorities aligned with regulatory risk
- [ ] Budget approved for CRITICAL and HIGH priority gaps

**Timeline**: Allow 1-2 weeks for approval routing

---

## Step 8: Integration & Communication

### Update Requirements Register

**Actions**:
1. **Add Control Mapping column** to Requirements Register (if not already present)
2. **For each requirement**, populate with:

   - Primary controls (list all controls marked "P")
   - Example: "A.8.24, A.5.10" for requirement with 2 Primary mappings

3. **Add Gap Status column**:

   - "✅ No Gap" (has Primary mapping)
   - "⚠️ Partial Gap" (Secondary/Supporting only)
   - "❌ Complete Gap" (no mappings)
   - "🔧 Remediation In Progress" (gap being closed)

4. **Link to Gap ID** if gap exists

**Output**: Requirements Register now shows control mappings and gap status at a glance

### Update Control Documentation

**For controls with NEW mappings** (especially if previously excluded or low-priority):
1. **Update control description** to note regulatory requirements satisfied
2. **Adjust implementation priority** if control is critical for regulatory compliance
3. **Enhance evidence collection** if control now supports regulatory requirement

**Example**:
```
Control: A.8.24 Use of Cryptography

Previous Description: "Implement encryption for sensitive data."

Updated Description: "Implement encryption for sensitive data. Primary control for:

- GDPR Article 32(1)(a) - Personal data encryption
- PCI DSS v4.0.1 Requirement 3.4 - Cardholder data encryption at rest
- PCI DSS v4.0.1 Requirement 4.1 - Cardholder data encryption in transit

Regulatory compliance CRITICAL. Implementation status: Implemented. Evidence: Encryption policy, key management procedure, system configuration exports."
```

### Communicate to Stakeholders

**Who Needs to Know**:

- **Control Owners**: Inform of new mappings, especially if affects their control priority/scope
- **Compliance Team**: Share gap register, coordinate remediation efforts
- **Executive Management**: Brief on critical gaps and resource needs
- **Legal Counsel**: Share for awareness of compliance status
- **Internal Audit**: Provide mapping for audit planning

**Communication Modes**:

- **Email Summary**: Brief stakeholder update with link to Control Mapping Matrix
- **Meeting**: For CRITICAL gaps or significant findings, schedule stakeholder meeting
- **Dashboard**: Update Compliance Dashboard (Workbook 6) with new mapping data

**Example Email**:
```
To: [Stakeholders]
Subject: GDPR Control Mapping Complete - Action Required

Team,

We have completed the ISO 27001 control mapping for GDPR requirements. Key findings:

✅ STRENGTHS:

- 76% of requirements have primary control mappings
- Strong technical and organizational controls in place

⚠️ GAPS IDENTIFIED:

- 10 gaps requiring remediation (5 Complete, 3 Partial, 2 Implementation)
- 2 CRITICAL gaps require immediate action:

  1. Breach notification process (must implement by Q1 2025)
  2. DPO function (hiring in progress)

📊 RESOURCES:

- Full mapping matrix: [Link to Workbook 4]
- Gap register: [Link to Gap Summary]
- Executive summary: [Attachment]

🎯 NEXT STEPS:

- Control Owners: Review new mappings for your controls (details in mapping matrix)
- Compliance Team: Begin CRITICAL gap remediation planning
- All: Please review and provide feedback by [Date]

Meeting scheduled: [Date/Time] to discuss remediation prioritization.

[ISMS Manager]
```

---

# Tools & Templates

## Control Mapping Matrix (Workbook 4)

**Purpose**: Primary tool for documenting requirement-to-control mappings

**Structure**: See detailed specification in Assessment Workbook handoff document

**Usage**:

- One row per requirement
- One column per ISO 27001 control (93 columns)
- Cell values: P (Primary), S (Secondary), Su (Supporting), or blank
- Automated gap detection via formulas

## Gap Register Template

**Integrated into Workbook 4, Sheet 4: Gap Summary**

**Fields**: See Section 2.4.3 for complete field list

**Usage**:

- Auto-populated from Control Mapping Matrix (requirements with no "P")
- Manual population of remediation fields (approach, responsible party, dates)
- Status tracking (Open → In Progress → Closed)

## Mapping Rationale Document (Optional)

**When Needed**: Complex mappings requiring extensive justification

**Template**:
```markdown
# Mapping Rationale: [Regulation Name]
# [Requirement ID]: [Requirement Text]

## Requirement Analysis
**Objective**: [What requirement mandates]
**Scope**: [What is covered]
**Specific Mandates**: [Any prescribed implementation]

## Candidate Controls Considered
1. [Control ID] - [Why considered]
2. [Control ID] - [Why considered]
3. [Control ID] - [Why considered]

## Mapping Decision

**Primary Mapping**: [Control ID]
**Rationale**: [Why this control is primary - how it satisfies requirement]
**Evidence**: [What evidence demonstrates satisfaction]

**Secondary Mappings** (if any):

- [Control ID]: [Rationale]
- [Control ID]: [Rationale]

**Supporting Mappings** (if any):

- [Control ID]: [Rationale]

## Implementation Status

- Control Status: [Implemented / Planned / In Progress]
- Evidence Available: [Yes / No / Partial]
- Gap Assessment: [No Gap / Partial Gap / Implementation Gap]

## Stakeholder Approvals

- Compliance Officer: [Name] - [Date]
- Control Owner: [Name] - [Date]
- Legal Counsel (if required): [Name] - [Date]

```

## Remediation Plan Template

See Section 2.6.2 for complete template

---

# Quality Assurance

## Mapping Quality Checklist

**Before finalizing mappings**, verify:

**Completeness**:

- [ ] All requirements from Requirements Register included in matrix
- [ ] All 93 ISO 27001 Annex A controls included as columns
- [ ] No requirements accidentally omitted

**Accuracy**:

- [ ] Mapping types (P/S/Su) used correctly per definitions
- [ ] Similar requirements mapped consistently (pattern consistency)
- [ ] Complex requirements with multiple Primary mappings have rationale documented
- [ ] No obvious mis-mappings (control clearly doesn't address requirement)

**Stakeholder Validation**:

- [ ] Control Owners consulted for Primary mappings (confirm controls can satisfy)
- [ ] Compliance Officer reviewed for regulatory accuracy
- [ ] Legal Counsel reviewed CRITICAL/HIGH priority gaps
- [ ] Mapping rationale documented for auditor scrutiny

**Gap Identification**:

- [ ] All requirements with no Primary mapping flagged as gap
- [ ] Gap type (Complete/Partial/Implementation) correctly assigned
- [ ] Gap priority follows framework (Section 2.5.1)
- [ ] Gaps entered in Gap Register

**Documentation**:

- [ ] Mapping Matrix professionally formatted (headers, colors, freeze panes)
- [ ] Gap Register complete (all fields populated)
- [ ] Executive Summary prepared
- [ ] Approval signatures obtained

## Common Mapping Errors to Avoid

**Error 1: Over-Mapping** (mapping controls that don't really address requirement)

- **Symptom**: Every requirement has 10+ Primary mappings
- **Problem**: Dilutes responsibility, confuses auditors, creates false confidence
- **Fix**: Be strict with "Primary" designation - only controls that DIRECTLY satisfy

**Error 2: Under-Mapping** (being too conservative, marking real Primary as Secondary)

- **Symptom**: Requirement clearly satisfied by control, but marked "S" instead of "P"
- **Problem**: Creates artificial gaps, wastes remediation resources
- **Fix**: If control substantially satisfies requirement, mark "P" confidently

**Error 3: Ignoring Implementation Status**

- **Symptom**: Mapping control as Primary even though it's "Excluded" in SoA
- **Problem**: Mapping is theoretical, not actual - creates false compliance claims
- **Fix**: Only map to implemented or planned controls; if excluded, either reconsider exclusion or accept gap

**Error 4: Inconsistent Mapping Across Similar Requirements**

- **Symptom**: Requirement A maps to Control X, but nearly-identical Requirement B doesn't
- **Problem**: Inconsistency suggests error, raises auditor questions
- **Fix**: Review similar requirements together, ensure consistent approach

**Error 5: Missing Rationale for Complex Mappings**

- **Symptom**: Requirement has 5 Primary controls, no explanation
- **Problem**: Auditor will question why so many controls needed, unclear which to examine
- **Fix**: Document why multiple controls needed, what each contributes

**Error 6: Gaps Not Prioritized**

- **Symptom**: All gaps marked "High" priority
- **Problem**: No clear remediation sequence, resource allocation unclear
- **Fix**: Use prioritization framework rigorously (Section 2.5.1)

**Error 7: Gaps Without Remediation Plans**

- **Symptom**: Gap Register shows gaps but no remediation approach or target date
- **Problem**: Gaps will never close, compliance will not improve
- **Fix**: Every gap needs plan, owner, date - no exceptions for CRITICAL/HIGH

## Validation Methods

**Self-Review**:
1. **Requirement Walkthrough**: For each requirement, verbally explain to yourself why each mapping is correct
2. **Control Walkthrough**: For each control with mappings, verify control actually addresses those requirements
3. **Gap Logic Check**: For each gap, confirm no control exists that could satisfy requirement

**Peer Review**:
1. **Second Mapper**: Have different person independently map 10-20% of requirements, compare results
2. **Discussion**: Where mappings differ, discuss rationale, converge on correct mapping
3. **Lessons Learned**: Apply insights from peer review to remaining mappings

**Stakeholder Review**:
1. **Control Owner Validation**: Each Control Owner reviews mappings to their control, confirms accuracy
2. **Compliance Officer Validation**: Reviews entire mapping for regulatory accuracy
3. **Legal Counsel Validation**: Reviews CRITICAL/HIGH gaps for legal sufficiency

**Audit Simulation**:
1. **Mock Audit**: Pretend to be auditor, ask "How do you satisfy Requirement X?"
2. **Evidence Check**: For each Primary mapping, verify evidence exists (or can be collected)
3. **Red Flag Test**: Would this mapping survive auditor scrutiny? If doubt exists, reconsider.

---

# Integration with Other Processes

## Prerequisites (Input from Other Processes)

**From IMP-5.31.2 (Requirements Extraction)**:

- Requirements Register with all extracted requirements
- Requirements categorized and approved
- Requirements prioritized

**From IMP-5.31.3 (Applicability Assessment)**:

- Regulatory Inventory (which regulations apply)
- Tier categorization (Mandatory, Conditional, Informational)

**From ISMS Implementation**:

- Statement of Applicability (which controls implemented)
- Control descriptions and implementation details
- Control Owner assignments

## Outputs (Feed into Other Processes)

**To IMP-5.31.5 (Evidence Management)**:

- Control mappings inform what evidence needed
- For each Primary mapping, evidence must demonstrate control satisfies requirement
- Gap remediation creates new evidence collection needs

**To Control Implementation**:

- Gap remediation drives new control implementations or enhancements
- Remediation plans feed into ISMS improvement projects

**To Risk Management**:

- Gaps represent compliance risks
- Gap priority informs risk treatment decisions
- Risk acceptance for Low priority gaps

**To Compliance Dashboard (Assessment Workbook 6)**:

- Mapping statistics (% requirements with Primary mappings)
- Gap counts and trends
- Remediation progress tracking

**To Audit Preparation**:

- Mapping matrix is key audit artifact
- Pre-identifies what auditors will examine (Primary mappings)
- Gap register shows areas needing improvement before audit

---

# Continuous Improvement

## Mapping Maintenance

**When to Update Mappings**:

1. **Regulatory Changes**: Regulation amended, new requirements added → Re-extract (IMP-5.31.3), re-map
2. **Control Changes**: New control implemented, control enhanced → Update mappings, potentially close gaps
3. **Control Removed**: Control excluded from SoA → Remove mappings, create gaps
4. **Periodic Review**: Annual comprehensive review → Validate all mappings still accurate

**Maintenance Process**:
1. Identify trigger (regulatory change, control change, scheduled review)
2. Update Control Mapping Matrix
3. Identify new gaps or closed gaps
4. Update Gap Register
5. Update Compliance Dashboard
6. Communicate changes to stakeholders

## Metrics & Monitoring

**Key Performance Indicators**:

**Mapping Coverage**:

- % Requirements with Primary mappings (target: >90%)
- % Requirements with any mappings (target: 100%)
- Average number of Primary mappings per requirement (target: 1-2)

**Gap Metrics**:

- Total gaps (trend: decreasing over time)
- Gaps by priority (CRITICAL/HIGH: target = 0)
- Average gap age (time from identification to closure)
- Gap closure rate (# gaps closed per quarter)

**Remediation Progress**:

- % Gaps with remediation plans (target: 100% for CRITICAL/HIGH)
- % Gaps on track (target date not passed)
- % Gaps overdue (target: <10%)

**Control Utilization**:

- Most-mapped controls (which controls satisfy most requirements)
- Least-mapped controls (which controls rarely used - candidate for exclusion?)
- Controls with no mappings (definitely candidates for exclusion)

## Lessons Learned

**After Each Mapping Exercise**:
1. **What Worked Well**: Document effective approaches, reuse in future mappings
2. **What Was Difficult**: Identify challenging requirement types, develop guidance
3. **Process Improvements**: Refine this IMP guide based on experience
4. **Tool Enhancements**: Improve Control Mapping Matrix template, automation

**Example Lessons Learned**:
```markdown
# Lessons Learned: GDPR Mapping (January 2025)

## What Worked Well

- Pre-mapping session with Legal Counsel helped clarify ambiguous requirements
- Using Control Reference sheet during mapping saved time (quick control lookup)
- Peer review caught 3 mapping errors before finalization

## Challenges

- GDPR Article 6 (lawful basis) difficult to map to ISO controls - legal concept, not technical
- Multiple requirements needing same control combination (A.5.16+A.5.17+A.5.18) - repetitive
- Differentiating Primary vs Secondary for A.5.24-A.5.28 (incident management) - all seemed important

## Process Improvements for Next Mapping

- Create "mapping decision tree" for common requirement patterns (access control, encryption, etc.)
- Pre-identify control combinations that frequently appear together
- Develop clearer Primary vs Secondary criteria for closely-related controls

## Tool Enhancements

- Add "control combination templates" to matrix (pre-populate common patterns)
- Create separate sheet for Legal/Organizational requirements that don't map cleanly to technical controls
- Improve gap prioritization automation (auto-calculate based on fields)

```

---

# Roles & Responsibilities Summary

| Role | Responsibilities in Control Mapping Process |
|------|---------------------------------------------|
| **ISMS Manager** | - Lead mapping process<br>- Coordinate stakeholders<br>- Approve final mappings<br>- Oversee gap remediation |
| **Compliance Officer** | - Validate regulatory accuracy of mappings<br>- Approve gap categorization<br>- Prioritize gaps based on regulatory risk |
| **Control Owners** | - Confirm controls can satisfy mapped requirements<br>- Provide implementation details<br>- Execute gap remediation for their controls |
| **Legal Counsel** | - Interpret complex requirements<br>- Validate legal sufficiency of mappings<br>- Approve CRITICAL/HIGH gap remediation approaches |
| **Information Security Team** | - Technical assessment of control capabilities<br>- Implement technical controls for gap remediation |
| **Internal Audit** | - Independent validation of mapping accuracy<br>- Audit simulation and pre-audit review |
| **Executive Management** | - Approve resource allocation for gap remediation<br>- Risk acceptance decisions for Low priority gaps |

---

# Common Scenarios & Examples

## Scenario 1: Straightforward Encryption Requirement

**Requirement**: "Implement encryption for personal data at rest"

**Analysis**:

- Objective: Confidentiality protection
- Specific mandate: Yes - explicitly requires encryption
- Category: Technical

**Candidate Controls**:

- A.8.24 Use of Cryptography ← Primary candidate

**Mapping Decision**:

- **A.8.24 → Primary (P)**
- Rationale: A.8.24 directly implements encryption. If A.8.24 includes personal data at rest encryption, requirement fully satisfied.
- Check: Review A.8.24 implementation - does it cover personal data? If yes → P. If no → gap.

**Outcome**: Simple, clear mapping. Single Primary control.

---

## Scenario 2: Complex Access Control Requirement

**Requirement**: "Implement comprehensive access management including identity lifecycle, multi-factor authentication, least privilege authorization, and quarterly access reviews"

**Analysis**:

- Objective: Access control across entire lifecycle
- Specific mandates: MFA, least privilege, quarterly reviews
- Category: Technical + Organizational

**Candidate Controls**:

- A.5.15 Access Control (policy)
- A.5.16 Identity Management (identity lifecycle)
- A.5.17 Authentication Information (MFA)
- A.5.18 Access Rights (authorization, reviews)
- A.8.3 Information Access Restriction (technical enforcement)

**Mapping Decision**:

- **A.5.16 → Primary (P)** - Identity lifecycle
- **A.5.17 → Primary (P)** - MFA
- **A.5.18 → Primary (P)** - Authorization + reviews
- **A.8.3 → Primary (P)** - Technical enforcement
- **A.5.15 → Supporting (Su)** - Policy foundation
- Rationale: Requirement is comprehensive, needs multiple controls working together. Each Primary control addresses one component. All are essential (cannot satisfy without any one).

**Outcome**: Multiple Primary mappings, documented rationale for combination.

---

## Scenario 3: Organizational Requirement with No Direct Control

**Requirement**: "Appoint a Data Protection Officer (DPO) with appropriate qualifications and independence"

**Analysis**:

- Objective: Governance, regulatory role
- Specific mandate: DPO role with specific characteristics
- Category: Organizational

**Candidate Controls**:

- A.5.2 Information Security Roles and Responsibilities ← Closest match

**Mapping Decision**:

- **A.5.2 → Secondary (S)** - A.5.2 defines roles but doesn't specifically mandate DPO
- **Gap: Complete** - ISO 27001 doesn't have "DPO" control
- Remediation: Create organization-specific control "CTRL-ORG-004: Data Protection Officer"

**Outcome**: Partial mapping to A.5.2, but gap identified. New organizational control needed.

---

## Scenario 4: Reporting Requirement

**Requirement**: "Notify supervisory authority within 72 hours of personal data breach"

**Analysis**:

- Objective: Regulatory reporting / incident response
- Specific mandate: 72-hour timeline, specific recipient
- Category: Operational + Reporting

**Candidate Controls**:

- A.5.24 Information Security Incident Management Planning
- A.5.25 Assessment and Decision on Information Security Events
- A.5.26 Response to Information Security Incidents
- A.5.6 Contact with Authorities

**Mapping Decision**:

- **A.5.26 → Primary (P)** - Incident response includes breach notification
- **A.5.6 → Supporting (Su)** - Establishes authority contact framework
- **A.5.24, A.5.25 → Supporting (Su)** - Incident management foundation
- Check: Does A.5.26 implementation include 72-hour breach notification? If yes → P. If no → enhancement needed (Partial Gap).

**Outcome**: If A.5.26 fully implements breach notification, Primary mapping. If not, enhance A.5.26 to include 72-hour process.

---

## Scenario 5: Testing Requirement with Partial Implementation

**Requirement**: "Conduct annual penetration testing of all external-facing systems"

**Analysis**:

- Objective: Security validation / testing
- Specific mandate: Penetration testing (not just vulnerability scanning), annual frequency
- Category: Operational

**Candidate Controls**:

- A.8.8 Management of Technical Vulnerabilities
- A.8.29 Security Testing in Development and Acceptance

**Current Implementation Check**:

- A.8.8: Includes vulnerability scanning (quarterly) but not penetration testing
- A.8.29: Includes security testing in dev/test environments, not production

**Mapping Decision**:

- **A.8.8 → Secondary (S)** - Vulnerability scanning ≠ penetration testing (related but distinct)
- **A.8.29 → Secondary (S)** - Security testing but not production penetration test
- **Gap: Partial** - Have related controls but not the specific mandated activity

**Remediation**: Enhance A.8.8 or A.8.29 (or both) to include annual external penetration test.

**Outcome**: Partial gap, enhancement needed to upgrade S → P.

---

# Reference Materials

## ISO 27001:2022 Annex A Controls

**93 Controls** across 4 sections:

- **Section 5: Organizational Controls** (A.5.1 - A.5.37): 37 controls
- **Section 6: People Controls** (A.6.1 - A.6.8): 8 controls
- **Section 7: Physical Controls** (A.7.1 - A.7.14): 14 controls
- **Section 8: Technological Controls** (A.8.1 - A.8.34): 34 controls

**Full list available in**: Assessment Workbook 4, Sheet 2: ISO 27001 Controls Reference

## Related Policy Documents

- **ISMS-POL-A.5.31.1**: Executive Summary & Control Alignment
- **ISMS-POL-A.5.31.2**: Regulatory Applicability Methodology (tier framework)
- **ISMS-POL-A.5.31.3**: Requirements Extraction & Control Mapping Framework (mapping definitions)
- **ISMS-POL-A.5.31.4**: Change Management & Evidence Framework (evidence requirements)

## Related Implementation Guides

- **ISMS-IMP-A.5.31.2**: Regulatory Applicability Assessment Process (determines which regulations apply)
- **ISMS-IMP-A.5.31.3**: Requirements Extraction Process (creates Requirements Register)
- **ISMS-IMP-A.5.31.5**: Evidence Management Process (collects evidence for mapped controls)
- **ISMS-IMP-A.5.31.6**: Compliance Dashboard & Regulatory Monitoring (tracks compliance status)

---

# Appendices

## Appendix A: Mapping Decision Flowchart

```
Start: Review Requirement X and Candidate Control Y
         ↓
[Q1: Does Control Y's objective align with Requirement X's objective?]
  No → [Skip to next control]
  Yes → [Continue]
         ↓
[Q2: If Control Y is fully implemented, would Requirement X be substantially satisfied?]
  No → [Continue to Q3]
  Yes → [PRIMARY (P) - Document rationale]
         ↓
[Q3: Does Control Y address a significant part of Requirement X?]
  No → [Continue to Q4]
  Yes → [SECONDARY (S) - Document which part + what's missing]
         ↓
[Q4: Does Control Y provide foundation/support for other controls that satisfy X?]
  No → [NO MAPPING (Blank)]
  Yes → [SUPPORTING (Su) - Document how it supports]
         ↓
[Document mapping in Control Mapping Matrix]
         ↓
[Next control]
```

## Appendix B: Glossary

**Primary Mapping (P)**: Control directly and substantially satisfies requirement; auditor would primarily examine this control for compliance

**Secondary Mapping (S)**: Control partially satisfies requirement; contributes meaningfully but additional controls needed

**Supporting Mapping (Su)**: Control indirectly supports requirement; provides foundation or enabler but not directly responsible

**Complete Gap**: Requirement has no control mappings at all (not even Secondary or Supporting)

**Partial Gap**: Requirement has Secondary or Supporting mappings but no Primary mapping (partially addressed but insufficient)

**Implementation Gap**: Requirement has Primary mapping but control not yet implemented (conceptual mapping exists, implementation pending)

**Control Owner**: Individual or role responsible for implementing and maintaining a specific control

**Compensating Control**: Alternative control that achieves same security objective when ideal control cannot be implemented

**Risk Acceptance**: Formal decision to not remediate a gap due to low priority or cost exceeding risk

## Appendix C: Acronyms

- **CISO**: Chief Information Security Officer
- **DPO**: Data Protection Officer
- **DPIA**: Data Protection Impact Assessment
- **GDPR**: General Data Protection Regulation
- **IMP**: Implementation Guide
- **ISMS**: Information Security Management System
- **PCI DSS v4.0.1**: Payment Card Industry Data Security Standard
- **POL**: Policy
- **SoA**: Statement of Applicability

---

**Document Control**:

- **Last Updated**: 2025-01-11
- **Next Review**: [Date] (annual)
- **Change History**:
  - v1.0 (2025-01-11): Initial release

---

END OF DOCUMENT

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
