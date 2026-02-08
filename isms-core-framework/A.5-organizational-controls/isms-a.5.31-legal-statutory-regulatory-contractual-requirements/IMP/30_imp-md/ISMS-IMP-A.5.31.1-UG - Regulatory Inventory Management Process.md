**ISMS-IMP-A.5.31.1-UG - Regulatory Inventory Management Process**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.31: Legal, Statutory, Regulatory and Contractual Requirements

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Regulatory Inventory Management Process |
| **Document Type** | Implementation Guide |
| **Document ID** | ISMS-IMP-A.5.31.1-UG |
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

This implementation guide provides step-by-step instructions for establishing and maintaining [Organization]'s master regulatory inventory—the definitive list of all regulations, standards, and frameworks relevant to information security compliance obligations.

**What This Guide Is**:

- Operational procedures for inventory creation and maintenance
- Data quality standards for regulatory entries  
- Review and update processes
- Integration with applicability assessments (IMP-5.31.2)

**What This Guide Is Not**:

- How to assess applicability (that's IMP-5.31.2)
- How to extract requirements (that's IMP-5.31.3)
- Legal interpretation guidance (consult legal counsel)

## The Regulatory Inventory Explained

**Definition**: The Regulatory Inventory is a structured database (Assessment Workbook 1) containing all regulations, statutes, standards, frameworks, and contractual obligations related to information security.

**Coverage**:

- **Tier 1 (Mandatory)**: Regulations that legally apply
- **Tier 2 (Conditional)**: Regulations that would apply if conditions met
- **Tier 3 (Informational)**: Voluntary frameworks for guidance

## Who Manages This Process

**Primary Roles**:

- **Compliance Officer**: Owns inventory, ensures accuracy
- **ISMS Manager**: Approves changes affecting ISMS scope
- **Legal Counsel**: Reviews Tier 1 regulations, validates citations

## Process Flowchart

```
[Trigger: New regulation, business change, periodic review]
         ↓
[STEP 1: Initial Registration]

- Create entry, assign ID, status = "Under Assessment"

         ↓
[STEP 2: Data Collection]

- Research details, citation, requirements summary

         ↓
[STEP 3: Applicability Assessment]

- Perform IMP-5.31.2 assessment, determine Tier

         ↓
[STEP 4: Inventory Entry Completion]

- Update with assessment results, set review date

         ↓
[STEP 5: Quality Review & Approval]

- Verify accuracy, obtain approvals per tier

         ↓
[STEP 6: Integration]

- Add to ISMS-POL-00, trigger downstream processes

         ↓
[Ongoing Maintenance: Monitor, Review, Update]
```

---

# Regulation ID Assignment

**Format**: `REG-[Jurisdiction]-[Sequence]`

**Jurisdiction Codes**:

- EU = European Union
- CH = Switzerland  
- US = United States
- UK = United Kingdom
- INT = International (ISO)
- CUST = Customer contractual
- VOL = Voluntary frameworks

**Examples**:

- `REG-EU-001`: GDPR
- `REG-CH-001`: Swiss FADP
- `REG-INT-003`: ISO 27001

---

# Inventory Fields

**Required Fields**:

- Regulation ID, Name, Short Name/Acronym
- Jurisdiction, Issuing Authority, Citation
- Effective Date
- Tier (1-Mandatory / 2-Conditional / 3-Informational)
- Applicability Status (Applicable / Conditional / Not Applicable / Under Assessment)
- Applicability Rationale
- Key Requirements Summary (2-4 bullets)
- Assessment Reference (link to Workbook 2)
- Next Review Date
- Responsible Party, Notes, Last Updated

---

# Review Schedule

| Tier | Frequency | Rationale |
|------|-----------|-----------|
| Tier 1 | Annually | Ensure ongoing applicability |
| Tier 2 | Quarterly | Monitor condition triggers |
| Tier 3 | Biennially | Frameworks evolve slowly |
| Not Applicable | Upon business change | Reassess only if operations change |

---

# Approval Workflow

**Tier 3 or Not Applicable**: Compliance Officer (1 day)

**Tier 2**: Compliance Officer + ISMS Manager (2-3 days)

**Tier 1**: Compliance Officer + Legal Counsel + ISMS Manager + Executive Management (1-2 weeks)

---

# Integration with ISMS-POL-00

Tier 1 and Tier 2 regulations must be added to ISMS-POL-00 (master regulatory framework).

**Triggers downstream processes**:

- Tier 1 → Requirements Extraction (IMP-5.31.3) within 30 days
- After extraction → Control Mapping (IMP-5.31.4)
- After mapping → Evidence Collection (IMP-5.31.5)

---

# Ongoing Maintenance

**Annual Comprehensive Review** (Q4):

- Review all entries
- Identify new regulations
- Clean up stale/repealed entries

**Continuous Monitoring**:

- Regulatory changes (amendments, new regs)
- Business changes (new markets, services, thresholds)
- Tier 2 condition triggers (quarterly check)

**Amendment Management**:

- Assess impact of amendments
- Update inventory fields
- Trigger re-extraction if requirements changed

**Archiving**:

- Archive (don't delete) regulations no longer applicable
- Status → "Archived - [Reason]"
- Preserves audit trail

---

# Common Pitfalls

1. **"Set and Forget"**: Inventory created once, never updated
2. **Inconsistent IDs**: Random assignment, IDs reused
3. **Skipping Assessment**: Adding without formal applicability assessment
4. **Vague Rationale**: "Applicable because we operate in EU" (too general)
5. **No POL-00 Integration**: Inventory and POL-00 out of sync
6. **Poor Version Control**: Overwriting files, no change log
7. **Duplicate Entries**: Same regulation listed multiple times
8. **Ignoring Tier 2**: Conditional regs documented but never monitored
9. **No Legal Review**: Tier 1 determined without legal counsel
10. **Incomplete Summaries**: Key requirements field blank or vague

---

# Related Documents

**Policies**:

- ISMS-POL-A.5.31.1: Executive Summary & Control Alignment
- ISMS-POL-A.5.31.2: Regulatory Applicability Methodology
- ISMS-POL-00: Regulatory Applicability Framework

**Implementation Guides**:

- ISMS-IMP-A.5.31.2: Regulatory Applicability Assessment Process
- ISMS-IMP-A.5.31.3: Requirements Extraction Process
- ISMS-IMP-A.5.31.4: Control Mapping Process
- ISMS-IMP-A.5.31.5: Evidence Management Process

**Assessment Tools**:

- Assessment Workbook 1: Regulatory Inventory (this guide's output)
- Assessment Workbook 2: Applicability Matrix
- Assessment Workbook 6: Compliance Dashboard

---

**END OF IMPLEMENTATION GUIDE**

---

*This guide provides systematic procedures for creating and maintaining [Organization]'s master regulatory inventory, ensuring all information security compliance obligations are identified, categorized, and tracked.*

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
