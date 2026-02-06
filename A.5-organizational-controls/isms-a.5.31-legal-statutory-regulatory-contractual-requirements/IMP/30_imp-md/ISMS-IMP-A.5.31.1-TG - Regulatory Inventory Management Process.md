**ISMS-IMP-A.5.31.1-TG - Regulatory Inventory Management Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.31: Legal, Statutory, Regulatory and Contractual Requirements

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Regulatory Inventory Management Process |
| **Document Type** | Implementation Guide |
| **Document ID** | ISMS-IMP-A.5.31.1-TG |
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

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

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

- Tier 1 → Requirements Extraction (IMP-S3) within 30 days
- After extraction → Control Mapping (IMP-S4)
- After mapping → Evidence Collection (IMP-S5)

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

- ISMS-POL-A.5.31-S1: Executive Summary & Control Alignment
- ISMS-POL-A.5.31-S2: Regulatory Applicability Methodology
- ISMS-POL-00: Regulatory Applicability Framework

**Implementation Guides**:

- ISMS-IMP-A.5.31-S2: Regulatory Applicability Assessment Process
- ISMS-IMP-A.5.31-S3: Requirements Extraction Process
- ISMS-IMP-A.5.31-S4: Control Mapping Process
- ISMS-IMP-A.5.31-S5: Evidence Management Process

**Assessment Tools**:

- Assessment Workbook 1: Regulatory Inventory (this guide's output)
- Assessment Workbook 2: Applicability Matrix
- Assessment Workbook 6: Compliance Dashboard

---

**END OF SPECIFICATION**

---

*"The idea is to try to give all the information to help others to judge the value of your contribution; not just the information that leads to judgment in one particular direction or another."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
