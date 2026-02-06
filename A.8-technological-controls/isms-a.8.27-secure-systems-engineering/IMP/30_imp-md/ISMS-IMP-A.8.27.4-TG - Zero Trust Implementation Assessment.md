**ISMS-IMP-A.8.27.4-TG - Zero Trust Implementation Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Zero Trust Implementation Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.4-TG |
| **Assessment Domain** | Domain 4 - Zero Trust Architecture |
| **Related Policy** | ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Security Architect / Zero Trust Program Lead |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect | Initial Zero Trust assessment specification |

**Review Cycle**: Annual (or after significant ZTA changes)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles)
- ISMS-IMP-A.8.27.1 (Security Architecture Review Process)
- ISMS-IMP-A.8.27.2 (Threat Modelling Methodology)
- ISMS-IMP-A.8.27.3 (Secure Architecture Pattern Catalogue)
- ISMS-POL-A.5.15-16-18 (Identity and Access Management)
- ISMS-POL-A.8.20-22 (Network Security)
- ISO/IEC 27002:2022 Control A.8.27
- NIST SP 800-207 (Zero Trust Architecture)
- NIST SP 800-207A (Zero Trust for Cloud-Native Applications)
- CISA Zero Trust Maturity Model

---

# Technical Specification

# Excel Workbook Specification

## Workbook Overview

| Property | Value |
|----------|-------|
| **Filename** | ISMS-IMP-A.8.27.4_Zero_Trust_Implementation_Assessment_YYYYMMDD.xlsx |
| **Sheets** | 12 |
| **Purpose** | Zero Trust maturity assessment |
| **Generator** | generate_a827_4_zero_trust.py |

## Sheet Specifications

### Sheet 1: Instructions

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Instructions |
| **Purpose** | ZT overview and guidance |
| **Protection** | Read-only |

**Content:**

- Zero Trust overview
- NIST SP 800-207 summary
- CISA Maturity Model explanation
- Pillar definitions
- Rating scales

### Sheet 2: Strategy

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Strategy |
| **Purpose** | ZT strategy assessment |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Strat-ID | 10 | Auto | STRAT-001 |
| B | Element | 25 | Text | Required |
| C | Status | 15 | Dropdown | Implemented/Partial/Not Started |
| D | Evidence | 30 | Text | Required |
| E | Gap | 30 | Text | Optional |
| F | Owner | 20 | Text | Required |
| G | Notes | 25 | Text | Optional |

**Pre-populated Rows:** 12 strategy elements

### Sheets 3-7: Pillar Assessments (Identity, Device, Network, Workload, Data)

| Property | Specification |
|----------|---------------|
| **Sheet Names** | Identity, Device, Network, Workload, Data |
| **Purpose** | Pillar maturity assessment |

**Column Definitions (consistent across pillars):**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | [Pillar]-ID | 10 | Auto | ID-001, DEV-001, etc. |
| B | Capability | 30 | Text | Required |
| C | Traditional | 12 | Dropdown | 0/1/2/3 |
| D | Initial | 12 | Dropdown | 0/1/2/3 |
| E | Advanced | 12 | Dropdown | 0/1/2/3 |
| F | Optimal | 12 | Dropdown | 0/1/2/3 |
| G | Current | 12 | Formula | Calculated from C-F |
| H | Target | 12 | Dropdown | Traditional/Initial/Advanced/Optimal |
| I | Evidence | 30 | Text | Required |
| J | Gap | 30 | Text | If Current < Target |

**Pre-populated Capabilities per Pillar:**

- **Identity:** 10 capabilities (Authentication, Authorisation, Lifecycle, PAM, etc.)
- **Device:** 8 capabilities (Inventory, Compliance, Threat Protection, etc.)
- **Network:** 8 capabilities (Segmentation, Encryption, Access, Monitoring, etc.)
- **Workload:** 10 capabilities (Identity, Isolation, Security Testing, etc.)
- **Data:** 10 capabilities (Classification, Encryption, Access, DLP, etc.)

### Sheet 8: Visibility

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Visibility |
| **Purpose** | Visibility and analytics maturity |

**Same structure as pillar sheets with 8 visibility capabilities**

### Sheet 9: Automation

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Automation |
| **Purpose** | Automation and orchestration maturity |

**Same structure as pillar sheets with 8 automation capabilities**

### Sheet 10: Compliance

Standard compliance sheet with ZT-specific requirements from ISMS-POL-A.8.27

### Sheet 11: GapRegister

Standard gap register structure

### Sheet 12: Dashboard

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Dashboard |
| **Purpose** | ZT maturity summary |
| **Protection** | Read-only (formulas) |

**Dashboard Elements:**

1. **Maturity Radar Data Table:** Scores by pillar for radar chart
2. **Overall ZT Maturity Score:** Weighted average of pillars
3. **CISA Maturity Level:** Derived from scores (Traditional/Initial/Advanced/Optimal)
4. **Pillar Summary Table:** Current vs Target with gap indicator
5. **Gap Priority Matrix:** High/Medium/Low gaps by pillar
6. **Strategy Progress:** Roadmap milestone tracking
7. **Trend Indicators:** If baseline exists

## Maturity Scoring

**Pillar Score Calculation:**

Each capability scored 0-3 for each maturity level. Current level is the highest level where score ≥ 2.

```excel
# Current maturity level formula
=IF(F2>=2,"Optimal",IF(E2>=2,"Advanced",IF(D2>=2,"Initial","Traditional")))
```

**Overall ZT Score:**

Weighted average across pillars (Identity weighted higher per CISA model)

| Pillar | Weight |
|--------|--------|
| Identity | 20% |
| Device | 15% |
| Network | 15% |
| Workload | 15% |
| Data | 15% |
| Visibility | 10% |
| Automation | 10% |

## Styling Specifications

**CISA Maturity Level Colours:**

| Level | Colour Code |
|-------|-------------|
| Traditional | #FF6B6B (Red) |
| Initial | #FFE66D (Yellow) |
| Advanced | #4ECDC4 (Teal) |
| Optimal | #2ECC71 (Green) |

---

# Generator Script Reference

| Property | Value |
|----------|-------|
| **Script Name** | generate_a827_4_zero_trust.py |
| **Location** | 10-isms-scr-base/isms-a.8.27-secure-systems-engineering/10_generator-master/ |
| **Output** | ISMS-IMP-A.8.27.4_Zero_Trust_Implementation_Assessment_YYYYMMDD.xlsx |

---

**END OF SPECIFICATION**

---

*"The only way to do great work is to love what you do. The only way to do great security is to assume you're already breached."*
— Adaptation of Steve Jobs

<!-- QA_VERIFIED: [Date] -->
