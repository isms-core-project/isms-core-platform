# ISMS Control Consolidation Guide v3.0

**Document Type**: Process Guide  
**Version**: 3.0  
**Date**: 24.01.2026  
**Purpose**: Instructions for consolidating multi-file ISMS control implementations into proper single-POL structure  
**Author**: ISMS Implementation Team  
**Status**: Active

---

## Table of Contents

1. [Critical Understanding](#1-critical-understanding)
2. [Phase 0: Discover Existing Content](#phase-0-discover-existing-content)
3. [Phase 1: Consolidation Planning](#phase-1-consolidation-planning)
4. [Phase 2: Consolidated POL Structure](#phase-2-consolidated-pol-structure)
5. [Phase 3: Consolidation Execution](#phase-3-consolidation-execution)
6. [Phase 4: CTX and REF Documents](#phase-4-ctx-and-ref-documents)
7. [Phase 5: Quality Assurance](#phase-5-quality-assurance)
8. [Phase 6: Delivery Process](#phase-6-delivery-process)
9. [Common Mistakes Reference](#common-mistakes-reference)
10. [Quick Start Checklist](#quick-start-checklist)

---

## 1. Critical Understanding

### 1.1 The Task Scope

**Common Misunderstanding:**
- ❌ Create new control implementation from scratch
- ❌ Design new structure based on ISO control text
- ❌ Ask user what structure they want

**Correct Understanding:**
- ✅ Consolidate EXISTING multi-file implementation
- ✅ Restructure EXISTING content into proper format
- ✅ Check project documentation FIRST to see what exists

### 1.2 Recognition Pattern

**If user says**: *"Rewrite current POLs into single POL"* or *"Did you check project docs?"*

**This means**:
1. Content already exists in project files
2. Structure is wrong (multiple files instead of one)
3. Task is consolidation, not creation from scratch
4. Reference implementations show correct target structure

### 1.3 Task Definition

**YOU ARE**: Restructuring existing content from improper format → proper format

**YOU ARE NOT**: Writing new policy content from ISO standards

---

## Phase 0: Discover Existing Content

### Step 0.1: Search Project Knowledge

**ALWAYS execute these searches FIRST:**

```
Search 1: "[Control Number] policy sections structure"
Search 2: "ISMS-POL-A.[X].[XX] all sections" 
Search 3: "ISMS-IMP-A.[X].[XX] implementation"
Search 4: "ISMS-POL-00 Regulatory Applicability"
Search 5: Reference controls (A.8.23, A.8.10, A.8.24, A.5.15-16-18, A.8.2-3-5)
```

### Step 0.2: Create Content Inventory

**Document what you find:**

| File Type | Document ID | Lines | Content | Decision |
|-----------|-------------|-------|---------|----------|
| Master | ISMS-POL-A.X.XX | ~400 | Overview | → Merge into consolidated POL |
| Section | ISMS-POL-A.X.XX-S1 | ~400 | Purpose/Scope | → Merge into Section 1 |
| Section | ISMS-POL-A.X.XX-S2 | ~300 | Requirements | → Merge into Section 2 |
| Section | ISMS-POL-A.X.XX-S2.1 | ~400 | Requirement domain 1 | → Merge into Section 2.1 |
| Section | ISMS-POL-A.X.XX-S2.2 | ~400 | Requirement domain 2 | → Merge into Section 2.2 |
| ... | ... | ... | ... | ... |
| Annex | ISMS-POL-A.X.XX-S5.A | ~400 | Landscape/guidelines | → Extract to CTX |
| Annex | ISMS-POL-A.X.XX-S5.B | ~400 | Technical checklist | → Extract to REF |
| Annex | ISMS-POL-A.X.XX-S5.C | ~400 | Procedures | → Keep as Annex A |
| Annex | ISMS-POL-A.X.XX-S5.D | ~300 | Quick reference | → Keep as Annex B |
| IMP | ISMS-IMP-A.X.XX.1 | - | Assessment spec | → NO CHANGES |
| IMP | ISMS-IMP-A.X.XX.2 | - | Assessment spec | → NO CHANGES |
| Scripts | generate_*.py | - | Generators | → NO CHANGES |

**Total existing content**: ___ files, ~_____ lines

### Step 0.3: Answer Key Questions

Before proceeding, answer:

1. **How many POL files exist?** ___
2. **Total line count across all POL files?** ___
3. **How many IMP specifications exist?** ___
4. **How many Python scripts exist?** ___
5. **Do CTX or REF documents already exist?** Yes / No
6. **What content needs extraction to CTX?** ___
7. **What content needs extraction to REF?** ___
8. **What annexes must stay in POL?** ___

---

## Phase 1: Consolidation Planning

### 1.1 Content Decision Framework

**For EACH annex/section, apply this decision tree:**

```
┌─ Is this BINDING policy (SHALL/SHOULD requirements)?
│
├─ YES → Keep in consolidated POL main body
│
└─ NO → Is it CRITICAL operational decision support?
    │
    ├─ YES (decision matrices, incident procedures, quick guides)
    │   └─→ Keep as POL Annex (max 2 annexes)
    │
    └─ NO → Is it detailed technical HOW-TO?
        │
        ├─ YES (methods, tools, checklists, procedures)
        │   └─→ Extract to REF document
        │
        └─ NO → Is it landscape/awareness/trends?
            │
            └─ YES → Extract to CTX document
```

### 1.2 Content Categorization Examples

| Content Type | Binding? | Critical Ops? | Technical? | Landscape? | Destination |
|--------------|----------|---------------|------------|------------|-------------|
| Policy requirements | ✅ | - | - | - | POL Section 2 |
| Roles & responsibilities | ✅ | - | - | - | POL Section 3 |
| Governance procedures | ✅ | - | - | - | POL Section 4 |
| Deletion decision matrix | ❌ | ✅ | - | - | POL Annex A |
| Vulnerability response | ❌ | ✅ | - | - | POL Annex A |
| Quick reference guide | ❌ | ✅ | - | - | POL Annex B |
| Exception request template | ❌ | ✅ | - | - | POL Annex B |
| Code review checklist | ❌ | ❌ | ✅ | - | REF document |
| Deletion methods detail | ❌ | ❌ | ✅ | - | REF document |
| Tool comparison matrices | ❌ | ❌ | ✅ | - | REF document |
| Language-specific patterns | ❌ | ❌ | ❌ | ✅ | CTX document |
| Cryptographic landscape | ❌ | ❌ | ❌ | ✅ | CTX document |
| Technology evolution | ❌ | ❌ | ❌ | ✅ | CTX document |

### 1.3 Target Document Structure

**After consolidation, you will have:**

1. **ISMS-POL-A.X.XX-[Name].md**
   - Length: ~1,500-2,000 lines
   - Content: All binding policy + 0-2 critical annexes

2. **ISMS-CTX-A.X.XX-[Topic].md** (if landscape content exists)
   - Length: ~400-500 lines
   - Content: Trends, awareness, evolution

3. **ISMS-REF-A.X.XX-[Topic].md** (if technical reference exists)
   - Length: ~400-700 lines
   - Content: Technical HOW-TO, methods, tools

4. **ISMS-IMP-A.X.XX.1 through .N** (unchanged)
   - Content: Assessment specifications
   - Action: NO MODIFICATIONS

5. **generate_*.py scripts** (unchanged)
   - Content: Assessment generators
   - Action: NO MODIFICATIONS (unless bug fixes requested)

### 1.4 Structure Plan Template

**Create this document and present to user for approval:**

```markdown
# A.X.XX Consolidation Structure Plan

## Current State
- X POL files totaling ~Y lines
- Z IMP specifications (unchanged)
- N Python scripts (unchanged)

## Proposed Consolidation

### ISMS-POL-A.X.XX-[Name].md (~1,800 lines)
**Consolidates:**
- Master document (ISMS-POL-A.X.XX)
- S1 (Purpose/Scope) → Section 1
- S2 (Requirements) → Section 2
- S2.1-2.N → Section 2 subsections
- S3 (Roles) → Section 3
- S4 (Governance) → Section 4

**Annexes (critical operational content only):**
- Annex A: [Name] (from S5.X) - WHY: [Decision support/procedures]
- Annex B: [Name] (from S5.Y) - WHY: [Quick reference/templates]

### ISMS-CTX-A.X.XX-[Topic].md (~400 lines)
**Extracts:**
- S5.A: [Landscape content] - WHY: Awareness, not binding

### ISMS-REF-A.X.XX-[Topic].md (~500 lines)
**Extracts:**
- S5.B: [Technical content] - WHY: Detailed HOW-TO, not binding

## What Stays Unchanged
- ISMS-IMP-A.X.XX.1 through .N (no modifications)
- All Python scripts (no modifications)

## Rationale
[Explain why content goes where it does]

## Approval Request
Please confirm this structure before I proceed with consolidation.
```

**WAIT FOR USER APPROVAL BEFORE PROCEEDING**

---

## Phase 2: Consolidated POL Structure

### 2.1 Standard Single-Control Structure

**Target length**: 1,500-2,000 lines (adjust for complexity)

**Mandatory structure** (follow exactly):

```markdown
# ISMS-POL-A.X.XX – [Control Name]

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | [Control Name] |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.X.XX |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | DD.MM.YYYY |
| **Version** | 1.0 |
| **Version Date** | DD.MM.YYYY |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | DD.MM.YYYY | CISO | Initial consolidated policy |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  
**Approval Chain**: CISO → CTO/VP Engineering → Legal/Compliance → Executive Management

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.X.XX.1 through .N (Implementation Specifications)
- ISMS-CTX-A.X.XX (if created)
- ISMS-REF-A.X.XX (if created)
- ISO/IEC 27001:2022 Control A.X.XX
- ISO/IEC 27002:2022 Control X.XX

---

## Executive Summary

[2-3 paragraphs consolidating from old Master + S1]

**Control Purpose**: [Why this control exists]

**Scope**: This policy applies to [scope statement]. It establishes organizational requirements for [control area], defining WHAT must be implemented and WHO is accountable. Technical implementation details (HOW) are documented in ISMS-IMP-A.X.XX specifications.

**Regulatory Context**: Per **ISMS-POL-00 (Regulatory Applicability Framework)**, [Organization] must comply with [key regulations]. This policy addresses requirements from ISO/IEC 27001:2022 Control A.X.XX and aligns with [relevant regulations].

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control A.X.XX

**ISO/IEC 27001:2022 Annex A.X.XX - [Control Name]**

> *[EXACT control text from ISO 27001:2022 standard]*

**Control Objective** (ISO/IEC 27002:2022): [Official objective from standard]

**This Control Addresses**:
- [Bullet list of what control prevents/protects]
- [Security objectives achieved]
- [Risks mitigated]

### 1.2 What This Policy Establishes

This policy defines:
- [Mandatory requirements (WHAT must be done)]
- [Governance framework (WHO is accountable)]
- [Compliance verification (HOW compliance is assessed)]
- [Exception management (WHEN deviations allowed)]

### 1.3 What This Policy Does NOT Establish

This policy does NOT include:
- Technical implementation procedures → See ISMS-IMP-A.X.XX specifications
- Tool selection and configuration → Risk-based organizational decisions
- Operational runbooks → Defined by operational teams
- [Other out-of-scope items]

**Rationale for Separation**:
- **Policy (POL)**: Stable governance requirements (annual review)
- **Implementation (IMP)**: Tactical procedures (quarterly updates)
- **Operations**: Dynamic operational details (continuous evolution)

This separation enables policy stability while allowing operational flexibility.

### 1.4 Scope

**This policy applies to**:
- [Organizational units]
- [Systems and services]
- [Data classifications]
- [Personnel roles]
- [Business processes]

**Out of Scope**:
- [Explicitly excluded items]
- [Boundary conditions]

**Applicability Notes**:
- [Risk-based tailoring guidance]
- [Organizational context considerations]

### 1.5 Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

#### Tier 1: Mandatory Compliance

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG** | All Swiss operations | [Specific requirements] |
| **EU GDPR** | Processing EU personal data | [Specific requirements] |
| **ISO/IEC 27001:2022** | ISMS certification | Control A.X.XX implementation |

#### Tier 2: Conditional Applicability

| Regulation | Trigger Condition | Requirements |
|------------|-------------------|--------------|
| [Regulation] | [When it applies] | [Requirements if triggered] |

#### Tier 3: Informational Reference

**Best practice alignment** (voluntary unless contractually required):
- [Framework 1]: [How it informs this control]
- [Framework 2]: [How it informs this control]

**For complete regulatory categorization, refer to ISMS-POL-00.**

---

## 2. Requirements Framework

[Consolidate S2, S2.1, S2.2, S2.3, S2.4 into logical requirement domains]

### 2.1 [Requirement Domain 1 - e.g., "Establishment Requirements"]

[Content consolidated from old sections, reorganized by theme]

**Requirements** (use SHALL/SHOULD/MAY):

1. **[Requirement 1]**: [Organization] SHALL [measurable requirement].
   - **Rationale**: [Why this requirement exists]
   - **Assessment**: [How compliance is verified]
   - **Evidence**: [What evidence demonstrates compliance]

2. **[Requirement 2]**: [Organization] SHOULD [recommended practice].
   - **Rationale**: [Why recommended]
   - **Exceptions**: [When deviation acceptable]

### 2.2 [Requirement Domain 2 - e.g., "Operational Requirements"]

[Continue pattern for all requirement domains]

### 2.3 [Requirement Domain 3 - e.g., "Verification Requirements"]

[Continue pattern]

---

## 3. Roles & Responsibilities

[Content from old S3, organized by role]

### 3.1 Governance Roles

#### 3.1.1 Executive Management

**Accountability**: Strategic oversight and resource allocation

**Responsibilities**:
- Policy approval and strategic direction
- Resource allocation for implementation
- Risk acceptance for exceptions
- Annual policy review participation

**RACI** (for key activities):

| Activity | Executive Mgmt | CISO | [Other Role] |
|----------|----------------|------|--------------|
| Policy approval | A | R | C |
| [Activity 2] | I | A | R |

#### 3.1.2 Chief Information Security Officer (CISO)

**Accountability**: Policy ownership and compliance oversight

**Responsibilities**:
- Policy framework ownership
- Compliance monitoring
- Exception approval
- Risk reporting to Executive Management

#### 3.1.3 [Other Governance Roles]

[Continue for all governance roles]

### 3.2 Operational Roles

#### 3.2.1 [Operational Role 1]

**Accountability**: [What they're accountable for]

**Responsibilities**:
- [Day-to-day duties]
- [Compliance obligations]
- [Escalation requirements]

#### 3.2.2 [Operational Role 2]

[Continue for all operational roles]

### 3.3 RACI Matrix (Comprehensive)

| Activity | Role 1 | Role 2 | Role 3 | Role 4 |
|----------|--------|--------|--------|--------|
| [Activity 1] | R | A | C | I |
| [Activity 2] | A | R | C | I |
| [Activity N] | R | A | I | C |

**Legend**:
- **R** (Responsible): Performs the work
- **A** (Accountable): Ultimately answerable (only one A per activity)
- **C** (Consulted): Provides input
- **I** (Informed): Kept updated

---

## 4. Policy Governance

[Content from old S4]

### 4.1 Policy Lifecycle

**Lifecycle Stages**:
1. **Creation**: Policy developed in response to [triggers]
2. **Review**: Stakeholder consultation and feedback integration
3. **Approval**: Formal approval per Section 4.3
4. **Publication**: Communication and distribution
5. **Implementation**: Deployment and training
6. **Monitoring**: Compliance verification and effectiveness measurement
7. **Review/Update**: Periodic or triggered review
8. **Retirement**: Archival when superseded

**Policy Owner**: Chief Information Security Officer (CISO)

### 4.2 Review and Updates

#### 4.2.1 Scheduled Reviews

**Annual Review** (mandatory):
- Full policy framework reviewed annually
- Scheduled: [Approval anniversary + 12 months]
- Participants: CISO, [stakeholders]
- Outcome: Approve as-is, update, or defer

**Quarterly Reviews** (targeted):
- Effectiveness metrics analysis
- Stakeholder feedback collection
- Threat landscape monitoring

#### 4.2.2 Triggered Reviews

Policy review SHALL be triggered by:
- Significant regulatory changes
- Major security incidents related to this control
- Risk assessment findings indicating gaps
- Technology changes affecting control applicability
- Organizational structure changes
- [Other triggers]

### 4.3 Approval Process

**Approval Authority**:

| Change Type | Approval Required | Review Required |
|-------------|-------------------|-----------------|
| Major update | CISO + CTO + Legal + Executive | All stakeholders |
| Minor update | CISO + Technical Lead | Affected stakeholders |
| Clarification | Technical Lead | CISO (informed) |

**Major Update**: Scope changes, new requirements, SLA modifications, role redefinitions  
**Minor Update**: Clarifications, examples, formatting, non-substantive changes  
**Clarification**: Typo fixes, cross-reference updates, editorial improvements

**Approval Process**:
1. Proposal submission with justification
2. Impact assessment
3. Stakeholder review (5-10 business days)
4. Approval authority decision
5. Version update and communication
6. Implementation tracking

### 4.4 Exception Management

[Exception process from old governance section]

#### 4.4.1 When Exceptions Are Permitted

Exceptions MAY be granted when:
- Technical impossibility demonstrated
- Business necessity with compensating controls
- Disproportionate cost relative to risk reduction
- Temporary during transition period

Exceptions SHALL NOT be granted for:
- Mandatory regulatory requirements (Tier 1)
- Controls protecting critical assets
- Requirements preventing high-severity risks

#### 4.4.2 Exception Request Process

1. **Submission**: [Who submits, what form]
2. **Assessment**: [Technical and risk evaluation]
3. **Approval**: [Who approves based on risk level]
4. **Documentation**: [What must be documented]
5. **Review**: [Periodic exception review frequency]

#### 4.4.3 Compensating Controls

When exceptions granted, compensating controls SHALL:
- Reduce risk to equivalent level
- Be documented and approved
- Be monitored for effectiveness
- Be reviewed periodically

### 4.5 Compliance Monitoring

[Compliance verification approach from old governance section]

#### 4.5.1 Monitoring Approach

**Methods**:
- Automated compliance checks (where feasible)
- Periodic assessments (frequency per risk)
- Audit reviews (internal and external)
- Self-assessments by control owners
- Evidence collection and validation

**Frequency**:

| Control Criticality | Assessment Frequency | Audit Frequency |
|---------------------|---------------------|-----------------|
| Critical | Quarterly | Annual |
| High | Semi-annual | Biennial |
| Medium | Annual | On-demand |
| Low | Biennial | On-demand |

#### 4.5.2 Non-Compliance Management

**Non-compliance handling**:
1. **Detection**: Identification through monitoring
2. **Assessment**: Impact and root cause analysis
3. **Remediation**: Corrective action plan with timeline
4. **Escalation**: Risk-based escalation to CISO/Executive
5. **Verification**: Validation of remediation effectiveness
6. **Tracking**: Non-compliance register maintenance

**Escalation Thresholds**:
- Critical findings → Immediate CISO notification
- High findings → CISO notification within 24 hours
- Medium findings → Monthly compliance report
- Low findings → Quarterly compliance report

### 4.6 Version Control

**Versioning Scheme**: Major.Minor (e.g., 1.0, 1.1, 2.0)

**Major Version (X.0)**:
- Scope changes
- New mandatory requirements
- Role redefinitions
- Requires full re-approval

**Minor Version (X.Y)**:
- Clarifications
- Example updates
- Non-substantive improvements
- Requires limited approval

**Change Tracking**:
- Version history table maintained
- Change rationale documented
- Previous versions archived
- Stakeholder notification process

---

## 5. Assessment & Verification

### 5.1 Assessment Approach

Compliance with this policy is assessed through:

**Implementation Assessments**:
- **ISMS-IMP-A.X.XX.1**: [Assessment 1 purpose]
- **ISMS-IMP-A.X.XX.2**: [Assessment 2 purpose]
- **ISMS-IMP-A.X.XX.N**: [Assessment N purpose]

**Assessment Methodology**:
1. Self-assessment by control owners
2. Evidence collection and documentation
3. Technical validation where applicable
4. Management review and approval
5. Gap identification and remediation planning

### 5.2 Evidence Requirements

**Required Evidence Types**:

| Requirement Area | Evidence Type | Examples |
|------------------|---------------|----------|
| [Area 1] | [Type] | [Specific examples] |
| [Area 2] | [Type] | [Specific examples] |

**Evidence Quality Standards**:
- Objective and verifiable
- Time-stamped and attributable
- Sufficient to demonstrate compliance
- Maintained per retention policy

### 5.3 Compliance Metrics

**Key Performance Indicators (KPIs)**:

| Metric | Target | Frequency | Owner |
|--------|--------|-----------|-------|
| [Metric 1] | [Target] | [Frequency] | [Owner] |
| [Metric 2] | [Target] | [Frequency] | [Owner] |

**Trend Analysis**:
- Quarterly compliance trending
- Year-over-year comparison
- Benchmark against industry standards

### 5.4 Audit Readiness

**Audit Support**:
- Consolidated evidence repository
- Assessment workbooks current (max 6 months old)
- Exception register up-to-date
- Compliance dashboard accessible
- Control owner interview preparation

**Audit Process**:
1. Provide policy and assessment documents
2. Present compliance dashboard
3. Demonstrate evidence for sampled requirements
4. Explain exceptions with compensating controls
5. Show continuous improvement initiatives

---

## 6. Related Documents

### 6.1 Internal ISMS Documents

**Foundational**:
- **ISMS-POL-00**: Regulatory Applicability Framework (mandatory reference)

**Implementation**:
- **ISMS-IMP-A.X.XX.1**: [Assessment 1 Name]
- **ISMS-IMP-A.X.XX.2**: [Assessment 2 Name]
- **ISMS-IMP-A.X.XX.N**: [Assessment N Name]

**Reference Materials** (if created):
- **ISMS-CTX-A.X.XX**: [Context Topic]
- **ISMS-REF-A.X.XX**: [Reference Topic]

**Related ISMS Policies**:
- **ISMS-POL-A.Y.YY**: [Related Control Policy]
- [Other related policies]

### 6.2 External Standards & Regulations

**International Standards**:
- **ISO/IEC 27001:2022**: Information Security Management Systems (Annex A.X.XX)
- **ISO/IEC 27002:2022**: Information Security Controls (Control X.XX)
- [Other relevant ISO standards]

**Regulatory**:
- **Swiss nDSG**: Federal Act on Data Protection
- **EU GDPR**: General Data Protection Regulation (where applicable)
- [Industry-specific regulations if applicable]

**Framework Alignment**:
- **[Framework 1]**: [How it relates]
- **[Framework 2]**: [How it relates]

**Technical References**:
- [Relevant technical standards]
- [Best practice guides]

---

## 7. Glossary

| Term | Definition |
|------|------------|
| **[Term 1]** | [Definition] |
| **[Term 2]** | [Definition] |
| **[Term N]** | [Definition] |
| **Assessment** | Systematic evaluation of control implementation and effectiveness |
| **Compensating Control** | Alternative control that reduces risk to acceptable level when primary control cannot be implemented |
| **Control Owner** | Individual accountable for control implementation and effectiveness |
| **Evidence** | Objective proof demonstrating control implementation and operation |
| **Exception** | Approved deviation from policy requirement with documented justification and compensating controls |
| **ISMS** | Information Security Management System |
| **Organization** | Generic placeholder - refers to the entity implementing this ISMS policy |
| **SHALL** | Mandatory requirement |
| **SHOULD** | Recommended practice (may have valid reasons for deviation) |
| **MAY** | Optional or permissible action |

---

## 8. Closing Statement

This policy establishes [Organization]'s commitment to [control objective]. It shall be maintained as a living document, subject to regular review and continuous improvement based on:

- Changing threat landscape
- Evolving regulatory requirements
- Organizational risk appetite
- Technological advancement
- Lessons learned from incidents
- Stakeholder feedback

**Continuous Improvement Philosophy**:

> *"The first principle is that you must not fool yourself—and you are the easiest person to fool."*  
> — Richard Feynman, Nobel Prize-winning physicist

[Organization] maintains this policy framework with intellectual honesty—ensuring controls genuinely reduce risk rather than creating security theater. Compliance is measured by effectiveness, not just existence.

**Policy Effectiveness Review**:
- Are controls actually preventing incidents?
- Do metrics show risk reduction?
- Are resources appropriately allocated?
- Is the control burden proportionate to risk?

The policy owner (CISO) is accountable for ensuring this policy achieves its intended security outcomes while enabling organizational objectives.

---

[IF CRITICAL ANNEXES EXIST - INSERT SECTION SEPARATOR]

---

## Annex A: [Critical Operational Content Name]

**Purpose**: [Why this annex is critical for operations]

**When to Use**: [Operational scenarios requiring this guidance]

[Content from extracted S5.X section - 100-200 lines]
[Examples: Decision matrix, incident procedures, approval framework]

---

## Annex B: [User Communication / Quick Reference Name]

**Purpose**: [Why this quick reference is critical]

**Audience**: [Primary users]

**When to Use**: [Daily operational context]

[Content from extracted S5.Y section - 100-150 lines]
[Examples: One-page summary, request template, quick decision guide]

---

**END OF ISMS-POL-A.X.XX**

*[Organization] maintains this policy as living documentation, reflecting the dynamic nature of information security while providing stable governance for risk management.*
```

### 2.2 Length Guidance by Complexity

| Control Complexity | Target Length | Annexes | Example Controls |
|--------------------|---------------|---------|------------------|
| Simple | 500-700 lines | 0 | A.8.23 (Web Filtering) |
| Moderate | 800-1,200 lines | 0-1 | A.8.11 (Data Masking) |
| Complex | 1,200-1,500 lines | 1-2 | A.8.10 (Deletion), A.8.24 (Crypto) |
| Stacked (3 controls) | 1,500-2,500 lines | 1-2 | A.8.2-3-5 (Auth/PAM/Access) |

**Note**: Length should be "just right" for control complexity—neither artificially padded nor arbitrarily truncated.

---

## Phase 3: Consolidation Execution

### 3.1 Content Consolidation Rules

#### Rule 1: Remove Redundancy

**REMOVE from consolidated POL:**
- ❌ Multiple document control headers (14 separate → 1 unified)
- ❌ Cross-references to now-merged sections ("see S2.1" → "see Section 2.1")
- ❌ References to "modular framework structure"
- ❌ Duplicate regulatory framework explanations
- ❌ Repeated definitions and glossary terms
- ❌ Multiple "Related Documents" sections

**KEEP in consolidated POL:**
- ✅ ALL substantive policy requirements
- ✅ ALL SHALL/SHOULD/MAY obligations
- ✅ ALL role definitions and RACI matrices
- ✅ ALL governance procedures
- ✅ ALL compliance and assessment requirements
- ✅ Critical operational annexes (max 2)

#### Rule 2: Reorganize Logically

**DON'T: Simple Concatenation**

```markdown
❌ WRONG APPROACH:

Section 2: Requirements Overview (from S2)
Section 2.1: Pre-Development Requirements (from S2.1)  
Section 2.2: Secure Coding Standards (from S2.2)
Section 2.3: Code Review Requirements (from S2.3)
Section 2.4: Third-Party Management (from S2.4)

[Just stacking old files in sequence with minor renumbering]
```

**DO: Logical Reorganization**

```markdown
✅ CORRECT APPROACH:

Section 2: Requirements Framework
  
  2.1 Pre-Development Requirements
      [Synthesize content from old S2 intro + S2.1]
      [Organize by: Planning → Design → Architecture → Training]
      [Remove redundant introductions from each old file]
  
  2.2 Development Requirements
      [Synthesize content from S2.2]
      [Organize by: Standards → Practices → Tools]
      [Integrate with other sections where overlap exists]
  
  2.3 Verification Requirements
      [Synthesize content from S2.3]
      [Organize by: Code Review → Testing → Validation]
      [Merge duplicate content on verification approaches]
  
  2.4 Supply Chain Requirements
      [Synthesize content from S2.4]
      [Organize by: Vendor → OSS → Dependencies]
      [Link to other sections where dependencies exist]

[Content flows logically by activity, not by old file structure]
```

#### Rule 3: Update Cross-References

**Systematically update all internal references:**

| Old Reference | New Reference |
|---------------|---------------|
| "ISMS-POL-A.X.XX-S2.1 Section 3" | "Section 2.1 Subsection 3" |
| "See S5.A for language guidelines" | "See ISMS-CTX-A.X.XX for language guidelines" |
| "Annex S5.C contains procedures" | "Annex A contains procedures" |
| "As defined in S1 Section 1.4" | "As defined in Section 1.4" |

#### Rule 4: Maintain Traceability

**For each requirement in consolidated POL:**

✅ **Clear Requirement ID**: Create unified numbering scheme
- Example: REQ-2.1.1, REQ-2.1.2, REQ-2.2.1...
- Map old IDs if they existed

✅ **Measurable Criteria**: Preserve SHALL/SHOULD/MAY language
- Maintain exact obligation level from original
- Don't weaken requirements during consolidation

✅ **Evidence Linkage**: Maintain connection to assessment
- Which IMP assessment addresses this requirement
- What evidence demonstrates compliance

✅ **Rationale Preservation**: Keep "why" explanations
- Business context for requirement
- Risk mitigation objective
- Regulatory driver if applicable

### 3.2 Consolidation Workflow

**Step-by-step process:**

1. **Create Master Document Shell**
   - Set up structure with all Section headers
   - Insert unified Document Control
   - Write consolidated Executive Summary

2. **Merge Section 1 (Control Alignment)**
   - Start with ISO control text (exact quote)
   - Consolidate scope from old S1 + Master
   - Integrate regulatory framework from old S1
   - Remove redundant introductions

3. **Merge Section 2 (Requirements)**
   - Map old S2, S2.1-2.N content to new structure
   - Eliminate duplicate content
   - Reorganize by logical flow
   - Update cross-references
   - Preserve all obligations

4. **Merge Section 3 (Roles)**
   - Consolidate from old S3
   - Update RACI matrices for new section numbers
   - Verify no roles lost

5. **Merge Section 4 (Governance)**
   - Consolidate from old S4
   - Update all procedural references
   - Verify exception and review processes complete

6. **Create Section 5 (Assessment)**
   - New section linking to IMP documents
   - Explain assessment approach
   - List evidence requirements

7. **Update Section 6 (Related Docs)**
   - Consolidate from all old reference sections
   - Add CTX/REF documents if created
   - Remove references to now-merged sections

8. **Consolidate Section 7 (Glossary)**
   - Merge all definitions from old sections
   - Remove duplicates
   - Alphabetize

9. **Create Section 8 (Closing)**
   - Write consolidated closing statement
   - Optional philosophy/methodology appendix

10. **Add Critical Annexes (if applicable)**
    - Maximum 2 annexes
    - Operational decision support only
    - Reference from main body

### 3.3 Quality Checks During Consolidation

**After each major section, verify:**

- [ ] No requirements lost from original content
- [ ] All cross-references updated
- [ ] No duplicate content
- [ ] Logical flow maintained
- [ ] Section numbering correct
- [ ] All SHALL/SHOULD/MAY obligations preserved
- [ ] Generic language maintained (no industry/size/tech assumptions)
- [ ] ISMS-POL-00 references correct

---

## Phase 4: CTX and REF Documents

### 4.1 CTX Document Structure

**Document Type**: ISMS-CTX-A.X.XX-[Topic].md

**Purpose**: Landscape, trends, awareness content NOT part of binding policy

**Length**: ~400-500 lines

**Template**:

```markdown
# ISMS-CTX-A.X.XX - [Context Topic]

**Document Type**: Internal - Technical Reference (Not ISMS)  
**Status**: Informational Only  
**Approval Authority**: Technical SME (no ISMS approval required)  
**Version**: 1.0  
**Date**: DD.MM.YYYY  
**Owner**: [Technical Lead Role]

---

## Disclaimer

**CRITICAL**: This is an informational reference document and is **NOT** part of the formal ISMS policy framework.

The information contained herein provides technical context, industry landscape awareness, and technology evolution trends but **does NOT establish mandatory requirements**.

**Binding policy requirements** are defined in **ISMS-POL-A.X.XX**.

**Purpose**: Support informed decision-making by providing awareness of:
- Industry trends and directions
- Technology evolution and maturity
- Best practice landscape
- Implementation options and considerations

**Usage**: Reference material for technical teams and decision-makers. Content may become outdated as industry evolves—check publication date.

---

## 1. Purpose & Scope

### 1.1 Context Objective

[Why this context document exists]
[What awareness it provides]
[How it supports decision-making]

### 1.2 Topics Covered

[List of major topics in this document]

### 1.3 Relationship to Policy

**ISMS-POL-A.X.XX establishes** (binding):
- [What the policy requires]

**This CTX document provides** (informational):
- [What context/landscape/awareness this adds]

---

## 2. [Landscape Topic 1]

### 2.1 Current State

[Where the industry/technology is today]
[Adoption rates, maturity levels]
[Common approaches]

### 2.2 Evolution & Trends

[How this is changing]
[Emerging practices]
[Direction of industry movement]

### 2.3 Considerations for [Organization]

[How to think about this landscape]
[Decision factors]
[Risk vs. maturity tradeoffs]

---

## 3. [Landscape Topic 2]

[Continue pattern for all landscape topics]

---

## 4. Technology & Standards Landscape

### 4.1 Relevant Standards

[External standards in this domain]
[Maturity and adoption]
[Alignment considerations]

### 4.2 Technology Options

[Available technologies/approaches]
[Maturity assessment]
[Adoption considerations]

---

## 5. Future Outlook

### 5.1 Emerging Developments

[What's on the horizon]
[Early-stage innovations]
[Potential disruptions]

### 5.2 Implications for [Organization]

[How to prepare for evolution]
[When to revisit decisions]
[Future-proofing considerations]

---

## 6. Document Maintenance

**Update Frequency**: Semi-annual or when significant landscape changes

**Owner**: [Technical Lead Role]

**Review Triggers**:
- Major industry standard updates
- Significant technology shifts
- New regulatory guidance
- Organizational strategy changes

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | DD.MM.YYYY | [Author] | Initial context document |

---

**END OF ISMS-CTX-A.X.XX**
```

**Example CTX Topics**:
- Language-specific secure coding landscapes (Python, Java, JS evolution)
- Cryptographic algorithm landscape and evolution
- Authentication technology landscape (passwords → passwordless)
- Cloud security service evolution

### 4.2 REF Document Structure

**Document Type**: ISMS-REF-A.X.XX-[Topic].md

**Purpose**: Detailed technical HOW-TO reference NOT part of binding policy

**Length**: ~400-700 lines

**Template**:

```markdown
# ISMS-REF-A.X.XX - [Reference Topic]

**Document Type**: Internal - Technical Reference (Not ISMS)  
**Status**: Informational Only  
**Approval Authority**: Technical SME (no ISMS approval required)  
**Version**: 1.0  
**Date**: DD.MM.YYYY  
**Owner**: [Technical Lead Role]

---

## Disclaimer

**CRITICAL**: This is an informational reference document and is **NOT** part of the formal ISMS policy framework.

The information contained herein provides technical guidance and methodological details but **does NOT establish mandatory requirements**.

**Binding policy requirements** are defined in **ISMS-POL-A.X.XX**.

**Purpose**: Support implementation by providing:
- Detailed technical procedures
- Method comparisons and selection guidance
- Tool landscape and evaluation criteria
- Implementation best practices

**Usage**: Technical reference for implementation teams. Content may require updates as technologies evolve—check publication date.

---

## 1. Purpose & Scope

### 1.1 Reference Objective

[What technical detail this provides]
[What implementation questions it answers]
[Who should use this reference]

### 1.2 Topics Covered

[List of technical topics]

### 1.3 Relationship to Policy

**ISMS-POL-A.X.XX requires** (binding):
- [What must be done per policy]

**This REF document explains** (informational):
- [HOW to do it - methods, tools, procedures]

---

## 2. [Technical Method 1]

### 2.1 Method Overview

[What this method is]
[When to use it]
[Prerequisites]

### 2.2 Procedure

**Step-by-step process**:

1. [Step 1 with details]
2. [Step 2 with details]
3. [Step N with details]

### 2.3 Tools & Technologies

[Tools that support this method]
[Selection criteria]
[Configuration considerations]

### 2.4 Validation

[How to verify method effectiveness]
[Testing procedures]
[Success criteria]

---

## 3. [Technical Method 2]

[Continue pattern for all methods]

---

## 4. Method Comparison & Selection

### 4.1 Comparison Matrix

| Method | Pros | Cons | Use When | Avoid When |
|--------|------|------|----------|------------|
| Method 1 | [Pros] | [Cons] | [Scenarios] | [Scenarios] |
| Method 2 | [Pros] | [Cons] | [Scenarios] | [Scenarios] |

### 4.2 Selection Decision Tree

[Flowchart or decision logic for method selection]

---

## 5. Tool Landscape

### 5.1 Tool Categories

[Types of tools for this technical domain]

### 5.2 Evaluation Criteria

[How to assess tool fitness]
[Key capabilities to verify]
[Vendor considerations]

### 5.3 Tool Comparison

[Vendor-agnostic comparison of capabilities]
[NOT specific product recommendations]

---

## 6. Implementation Best Practices

### 6.1 Common Pitfalls

[What typically goes wrong]
[How to avoid issues]

### 6.2 Lessons Learned

[Organizational experience]
[Industry best practices]

### 6.3 Optimization Opportunities

[How to improve effectiveness]
[Performance tuning]

---

## 7. Standards & Certifications

### 7.1 Relevant Standards

[Technical standards for this domain]
[Certification schemes]
[Compliance considerations]

### 7.2 Validation Methods

[How to validate against standards]
[Testing and certification procedures]

---

## 8. Document Maintenance

**Update Frequency**: Quarterly or when significant technical changes

**Owner**: [Technical Lead Role]

**Review Triggers**:
- New tool capabilities
- Method effectiveness findings
- Industry best practice evolution
- Organizational lessons learned

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | DD.MM.YYYY | [Author] | Initial reference document |

---

**END OF ISMS-REF-A.X.XX**
```

**Example REF Topics**:
- Data deletion methods technical reference
- Code review technical methodology
- Cryptographic implementation guide
- Masking technique details

---

## Phase 5: Quality Assurance

### 5.1 Pre-Delivery Checklist

**Before delivering consolidated POL, verify:**

#### Content Completeness
- [ ] All content from N separate files accounted for
- [ ] No substantive requirements lost
- [ ] All SHALL/SHOULD/MAY obligations preserved
- [ ] All role definitions included
- [ ] All governance procedures complete
- [ ] All assessment linkages maintained

#### Structure Correctness
- [ ] Follows standard POL structure (Sections 1-8)
- [ ] Document Control unified (not 14 separate headers)
- [ ] Only 0-2 critical annexes in POL
- [ ] CTX document created for landscape content
- [ ] REF document created for technical HOW-TO
- [ ] Length appropriate for complexity

#### Generic Language
- [ ] Uses "[Organization]" placeholder throughout
- [ ] NO industry assumptions (e.g., "for SaaS providers...")
- [ ] NO size assumptions (e.g., "for enterprises with 500+ staff...")
- [ ] NO technology assumptions (e.g., "for AWS users...")
- [ ] Technology-agnostic throughout
- [ ] Vendor-agnostic throughout

#### ISMS-POL-00 Integration
- [ ] Section 1.5 references ISMS-POL-00 explicitly
- [ ] Tier 1/2/3 framework used consistently
- [ ] NO custom regulatory classification invented
- [ ] Regulatory mapping complete and accurate

#### ISO 27001 Alignment
- [ ] Control text quoted EXACTLY from ISO 27001:2022
- [ ] Control number correct (A.X.XX)
- [ ] Control objective accurately stated
- [ ] Requirements traceable to control

#### Cross-References
- [ ] All internal section references updated
- [ ] References to old S-sections removed/updated
- [ ] IMP document references correct
- [ ] CTX/REF document references added if created
- [ ] Related ISMS policy references verified

#### Dates & Formatting
- [ ] All dates in DD.MM.YYYY format
- [ ] Markdown formatting correct
- [ ] Tables properly formatted
- [ ] Lists and bullets consistent
- [ ] No placeholder text like [TBD]

#### Evidence & Assessment
- [ ] Assessment approach section complete
- [ ] Evidence requirements clear
- [ ] IMP document linkage explicit
- [ ] Compliance metrics defined

### 5.2 CTX Document Quality Check

**If CTX document created, verify:**

- [ ] Disclaimer clearly states "Not part of ISMS"
- [ ] Approval authority = Technical SME (not ISMS approval)
- [ ] Contains landscape/trends/awareness only
- [ ] Does NOT contain binding requirements
- [ ] References binding POL for requirements
- [ ] Length ~400-500 lines
- [ ] Update frequency defined

### 5.3 REF Document Quality Check

**If REF document created, verify:**

- [ ] Disclaimer clearly states "Not part of ISMS"
- [ ] Approval authority = Technical SME (not ISMS approval)
- [ ] Contains technical HOW-TO only
- [ ] Does NOT contain binding requirements
- [ ] References binding POL for requirements
- [ ] Length ~400-700 lines
- [ ] Update frequency defined

### 5.4 Related Documents Check

**Verify unchanged documents:**

- [ ] IMP specifications NOT modified
- [ ] Python scripts NOT modified (unless bug fix requested)
- [ ] Existing REF/CTX documents reviewed (if applicable)
- [ ] All document IDs consistent

---

## Phase 6: Delivery Process

### 6.1 Delivery Sequence

**Deliver in this order (wait for approval between phases):**

#### Phase 6.1.1: Structure Plan (FIRST)

**Contents**:
1. Current state inventory
2. Consolidation decisions with rationale
3. Target document structure
4. Length estimates
5. Approval request

**Format**: Regular text (not in code block)

**Action**: WAIT FOR USER APPROVAL before proceeding

#### Phase 6.1.2: Consolidated POL (Second)

**Delivery approach**:
- Deliver in ~400-line sections
- Each section in markdown code block
- Wait for approval between sections
- Typical sequence:
  1. Document Control + Executive Summary + Section 1 (~400 lines)
  2. Section 2 (~400-600 lines, may split)
  3. Section 3 (~300-400 lines)
  4. Section 4 (~300-400 lines)
  5. Sections 5-6-7-8 (~300-400 lines)
  6. Annexes if applicable (~200-300 lines)

**Format for each delivery**:

````markdown
Here is Section [N] of the consolidated POL:

```markdown
[Content here in proper markdown]
```

**What's in this section:**
- [Brief summary]

**What's coming next:**
- [Preview of next section]

Shall I proceed with Section [N+1]?
````

#### Phase 6.1.3: CTX Document (Third, if created)

**Delivery approach**:
- Complete document in 1-2 chunks
- In markdown code block
- Explain what content was extracted and why

#### Phase 6.1.4: REF Document (Fourth, if created)

**Delivery approach**:
- Complete document in 1-2 chunks
- In markdown code block
- Explain what content was extracted and why

#### Phase 6.1.5: Summary Document (Final)

**Contents**:
1. What changed (before/after comparison)
2. What content moved where
3. Rationale for all decisions
4. File organization summary
5. Next steps (if any)

### 6.2 Delivery Format Requirements

**ALWAYS use markdown code blocks for policy content:**

````markdown
Correct example:

```markdown
# ISMS-POL-A.X.XX – Control Name

## Document Control
[content]
```
````

**NEVER deliver policy content as plain text:**

```
Wrong example:

# ISMS-POL-A.X.XX – Control Name

## Document Control
[content]

[This plain text format is INCORRECT for policy delivery]
```

**Why code blocks matter:**
- Preserves markdown formatting
- Enables direct copy-paste by user
- Prevents rendering issues
- Maintains consistent structure

### 6.3 Response Style During Delivery

**Between deliveries, keep responses concise:**

✅ **GOOD**:
```
Here is Section 2 of the consolidated POL:

[code block with content]

This section consolidates requirements from S2, S2.1-2.4 into 
logical domains. 

Ready for Section 3?
```

❌ **AVOID**:
```
Here is Section 2! I've worked really hard on this and I think 
you'll find it addresses all the requirements in a comprehensive 
way. I've reorganized the content from the original S2, S2.1, 
S2.2, S2.3, and S2.4 sections into a much more logical flow 
that I believe will be easier for readers to follow...

[300 words of explanation before showing actual content]

[code block with content]

[300 words of explanation after content]

Now let me know if you have any questions about this section 
or if you'd like me to explain any of my decisions in more detail...
```

**Delivery principle**: Let the work speak for itself. Provide brief context, deliver content, ask for approval to proceed.

---

## Common Mistakes Reference

### Mistake 1: Not Checking What Exists

**Symptom**: Starting to write new policy from scratch

**Root Cause**: Didn't search project knowledge first

**Consequence**: Wasted effort, incorrect deliverable, user frustration

**Prevention**:
- ALWAYS search project knowledge first
- Look for existing POL files (Master + S-sections)
- Inventory all content before planning
- Ask "What exists?" before "What should I create?"

### Mistake 2: Asking for Decisions Already Made

**Symptom**: Questions like "Should I create assessment workbooks?"

**Root Cause**: Not checking if IMP/scripts already exist

**Consequence**: Appears to not understand the task

**Prevention**:
- Search for ISMS-IMP-A.X.XX files
- Search for generate_*.py scripts
- Assume implementation layer exists if POL exists
- Only create IMP/scripts if explicitly requested

### Mistake 3: Simple File Concatenation

**Symptom**: POL reads like 14 separate documents stapled together

**Root Cause**: Copy-paste without reorganization

**Consequence**: Redundant content, poor flow, no consolidation value

**Prevention**:
- Remove all redundant headers
- Reorganize content by logical themes
- Eliminate duplicate content
- Update all cross-references
- Create unified flow

### Mistake 4: Losing Content During Consolidation

**Symptom**: Requirements missing from consolidated version

**Root Cause**: Deciding content "isn't important" without verification

**Consequence**: Non-compliant policy, user must identify gaps

**Prevention**:
- Track every requirement from source to destination
- Use checklist to verify all content placed
- When unsure, ask user rather than omit
- Create CTX/REF for content that doesn't fit POL

### Mistake 5: Too Many POL Annexes

**Symptom**: 4+ annexes in consolidated POL

**Root Cause**: Not applying decision framework correctly

**Consequence**: POL too long, content that should be CTX/REF

**Prevention**:
- Maximum 2 annexes in POL
- Only CRITICAL operational content as annexes
- Landscape content → CTX
- Technical HOW-TO → REF
- Apply decision tree strictly

### Mistake 6: Modifying IMP/Scripts Without Request

**Symptom**: "While consolidating, I also fixed the Python scripts..."

**Root Cause**: Scope creep, trying to be helpful

**Consequence**: Unexpected changes, potential bugs, scope confusion

**Prevention**:
- IMP specifications: NO MODIFICATIONS unless requested
- Python scripts: NO MODIFICATIONS unless bug fix requested
- Stay focused on consolidation task
- Suggest improvements separately

### Mistake 7: Non-Generic Language

**Symptom**: "For SaaS providers...", "Organizations with 500+ employees..."

**Root Cause**: Not maintaining generic language vigilance

**Consequence**: Policy not reusable, limited applicability

**Prevention**:
- Use "[Organization]" placeholder
- Avoid industry/size/technology assumptions
- Check every paragraph for assumptions
- Keep guidance universally applicable

### Mistake 8: Broken Cross-References

**Symptom**: "See Section S2.1" in consolidated document

**Root Cause**: Not systematically updating references

**Consequence**: Confusion, unprofessional output

**Prevention**:
- Search entire document for "S1", "S2", "S3", etc.
- Update all to new section numbers
- Verify references are correct
- Check before each delivery

### Mistake 9: Asking Instead of Showing

**Symptom**: "I think the structure should be... Do you agree?"

**Root Cause**: Lack of confidence in methodology

**Consequence**: Slows progress, creates uncertainty

**Prevention**:
- Follow methodology from this guide
- Present structure plan as recommendation
- Wait for approval before execution
- Trust the process, adjust based on feedback

### Mistake 10: Over-Explaining Deliveries

**Symptom**: 500 words of explanation before showing content

**Root Cause**: Nervousness, trying to pre-justify decisions

**Consequence**: User must scroll through explanation to find actual work

**Prevention**:
- Brief context (1-2 sentences)
- Show content in code block
- Ask if ready to proceed
- Let work speak for itself

---

## Quick Start Checklist

**Before starting ANY consolidation work:**

### Phase 0: Discovery
- [ ] Searched project knowledge for existing POL files
- [ ] Found and counted all POL files (Master + sections)
- [ ] Calculated total line count across all POL files
- [ ] Identified all IMP specifications
- [ ] Identified all Python scripts
- [ ] Checked if CTX or REF documents already exist
- [ ] Reviewed reference controls (A.8.23, A.8.10, etc.)
- [ ] Reviewed ISMS-POL-00 for regulatory framework

### Phase 1: Planning
- [ ] Created content inventory table
- [ ] Applied decision framework to each annex
- [ ] Determined what goes in POL vs CTX vs REF
- [ ] Outlined target POL structure
- [ ] Estimated lengths for each document
- [ ] Created structure plan document
- [ ] PRESENTED STRUCTURE PLAN TO USER
- [ ] RECEIVED APPROVAL TO PROCEED

### Phase 2: Execution Ready
- [ ] Understand this is CONSOLIDATION not creation
- [ ] Know what content goes where
- [ ] Have clear target structure
- [ ] Ready to deliver in ~400-line sections
- [ ] Will use markdown code blocks
- [ ] Will NOT modify IMP or scripts
- [ ] Will maintain generic language
- [ ] Will update all cross-references

### During Consolidation
- [ ] Removing redundant headers as I merge
- [ ] Reorganizing logically, not just concatenating
- [ ] Preserving all requirements
- [ ] Updating cross-references systematically
- [ ] Maintaining audit traceability
- [ ] Checking generic language in each section
- [ ] Verifying ISMS-POL-00 integration

### Before Each Delivery
- [ ] Content in markdown code block
- [ ] Cross-references updated
- [ ] Generic language verified
- [ ] Length appropriate (~400 lines)
- [ ] Brief summary provided
- [ ] Ready to wait for approval

---

## Success Criteria

**Consolidation is successfully complete when:**

1. ✅ **Structure**: N separate POL files → 1 consolidated POL
2. ✅ **Length**: ~1,500-2,000 lines (adjust for complexity)
3. ✅ **Annexes**: Maximum 2 critical operational annexes in POL
4. ✅ **CTX**: Created if landscape/awareness content existed
5. ✅ **REF**: Created if technical HOW-TO content existed
6. ✅ **IMP**: All specifications unchanged
7. ✅ **Scripts**: All Python files unchanged (unless bug fix)
8. ✅ **Content**: Nothing lost (everything went somewhere appropriate)
9. ✅ **Quality**: All quality checks passed
10. ✅ **Process**: User approved structure before execution
11. ✅ **Format**: All deliveries in markdown code blocks
12. ✅ **Language**: Generic throughout (no assumptions)
13. ✅ **Integration**: ISMS-POL-00 framework maintained
14. ✅ **Traceability**: Requirements traceable to ISO control
15. ✅ **References**: All cross-references updated

**User satisfaction indicators:**
- User approves structure plan quickly
- User approves sections with minimal changes
- User doesn't ask "did you check the project docs?"
- User doesn't point out missing content
- Consolidation process flows smoothly

---

## Appendix: Example Consolidation

### Before Consolidation (A.8.28 Example)

**Existing Structure**:
- 1 Master document (ISMS-POL-A.8.28.md) = 750 lines
- 13 Section files (S1 through S5.D) = 4,350 lines
- **Total**: 14 files, ~5,100 lines

### After Consolidation

**Target Structure**:
- **ISMS-POL-A.8.28-Secure-Coding.md** = ~1,800 lines
  - Consolidates: Master + S1 + S2 + S2.1-2.4 + S3 + S4
  - Annex A: Vulnerability Response (from S5.C) = ~200 lines
  - Annex B: Quick Reference (from S5.D) = ~150 lines
  
- **ISMS-CTX-A.8.28-Language-Guidelines.md** = ~400 lines
  - Extracts: S5.A (Language-specific patterns)
  
- **ISMS-REF-A.8.28-Code-Review-Reference.md** = ~400 lines
  - Extracts: S5.B (Code review checklist)

**Result**: 14 files → 3 files, improved organization, clearer purpose

---

**END OF ISMS CONTROL CONSOLIDATION GUIDE v3.0**

*"The first principle is that you must not fool yourself—and you are the easiest person to fool." — Richard Feynman*

**Remember**: Check what exists BEFORE planning what to create.