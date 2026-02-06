**ISMS-IMP-A.8.27.2-TG - Threat Modelling Methodology**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Threat Modelling Methodology |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.2-TG |
| **Assessment Domain** | Domain 2 - Threat Analysis and Modelling |
| **Related Policy** | ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Security Architect / Threat Modelling Lead |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect | Initial threat modelling assessment specification |

**Review Cycle**: Annual (or after methodology changes)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles)
- ISMS-IMP-A.8.27.1 (Security Architecture Review Process)
- ISMS-IMP-A.8.27.3 (Secure Architecture Pattern Catalogue)
- ISMS-IMP-A.8.27.4 (Zero Trust Implementation Assessment)
- ISMS-POL-A.5.7 (Threat Intelligence)
- ISO/IEC 27002:2022 Control A.8.27
- MITRE ATT&CK Framework
- STRIDE Methodology (Microsoft)
- PASTA Threat Modelling Framework

---

# Technical Specification

# Excel Workbook Specification

## Workbook Overview

| Property | Value |
|----------|-------|
| **Filename** | ISMS-IMP-A.8.27.2_Threat_Modelling_Methodology_YYYYMMDD.xlsx |
| **Sheets** | 10 |
| **Purpose** | Threat modelling methodology assessment |
| **Generator** | generate_a827_2_threat_modelling.py |

## Sheet Specifications

### Sheet 1: Instructions

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Instructions |
| **Purpose** | User guidance and methodology overview |
| **Protection** | Read-only (protected) |

**Content Sections:**

1. Document header with ISMS branding
2. Assessment purpose
3. STRIDE methodology overview
4. PASTA methodology overview
5. MITRE ATT&CK primer
6. Rating scales
7. Evidence requirements

### Sheet 2: Methodology

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Methodology |
| **Purpose** | Methodology adoption assessment |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Meth-ID | 10 | Auto | METH-001 format |
| B | Category | 25 | Dropdown | See list below |
| C | Requirement | 40 | Text | Required |
| D | Adopted | 10 | Dropdown | Yes/Partial/No |
| E | Documented | 12 | Dropdown | Yes/Partial/No |
| F | Effective | 12 | Dropdown | 1/2/3/4/5 |
| G | Evidence | 30 | Text | Required |
| H | Gaps | 30 | Text | Optional |

**Category Dropdown:**
Selection, Scope, Assets, Threats, AttackSurface, TrustBoundaries, DataFlows, Prioritisation, Countermeasures, Documentation, Review, Maintenance

**Pre-populated Rows:** 20 methodology requirements

### Sheet 3: MITRE_ATT&CK

| Property | Specification |
|----------|---------------|
| **Sheet Name** | MITRE_ATT&CK |
| **Purpose** | ATT&CK framework coverage assessment |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | ATT-ID | 10 | Text | T#### format |
| B | Tactic | 20 | Dropdown | ATT&CK tactics |
| C | Technique | 35 | Text | Technique name |
| D | Relevance | 12 | Dropdown | High/Medium/Low/N/A |
| E | Covered | 10 | Dropdown | Yes/Partial/No |
| F | DetectionMap | 35 | Text | Detection capabilities |
| G | Gap | 30 | Text | Coverage gaps |

**Pre-populated Rows:** 50 key ATT&CK techniques

### Sheet 4: ThreatCatalogue

| Property | Specification |
|----------|---------------|
| **Sheet Name** | ThreatCatalogue |
| **Purpose** | Organisational threat catalogue |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Threat-ID | 10 | Auto | THR-001 format |
| B | Category | 20 | Dropdown | Threat actor categories |
| C | ThreatActor | 25 | Text | Actor description |
| D | Motivation | 20 | Dropdown | Financial/Espionage/Disruption/Ideology/Revenge |
| E | Capability | 15 | Dropdown | Low/Moderate/High/Nation-State |
| F | ATT&CK_Ref | 25 | Text | ATT&CK technique IDs |
| G | Likelihood | 12 | Dropdown | Rare/Unlikely/Possible/Likely/Almost Certain |
| H | Countermeasures | 35 | Text | Primary controls |

**Pre-populated Rows:** 15 standard threat actors

### Sheet 5: Tools

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Tools |
| **Purpose** | Threat modelling tools assessment |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Tool-ID | 10 | Auto | TOOL-001 format |
| B | Tool | 30 | Text | Tool name |
| C | Purpose | 35 | Text | Primary use case |
| D | Licensed | 10 | Dropdown | Yes/No/OSS |
| E | Users | 10 | Number | Integer |
| F | Integration | 25 | Text | Integrated systems |
| G | Effectiveness | 12 | Dropdown | 1/2/3/4/5 |
| H | Gaps | 30 | Text | Limitations |

**Pre-populated Rows:** 8 common tools

### Sheet 6: Competency

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Competency |
| **Purpose** | Team competency assessment |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Comp-ID | 10 | Auto | COMP-001 format |
| B | Role | 25 | Text | Role title |
| C | Competency | 30 | Text | Required competency |
| D | Required | 10 | Dropdown | Mandatory/Recommended |
| E | Training | 10 | Dropdown | Yes/Partial/No |
| F | Certified | 10 | Number | Count |
| G | Target | 10 | Number | Target count |
| H | Gap | 25 | Text | Competency gap |

**Pre-populated Rows:** 12 competency requirements

### Sheet 7: Samples

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Samples |
| **Purpose** | Sample threat model quality review |
| **Protection** | Data entry enabled |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Sample-ID | 10 | Auto | SAMP-001 format |
| B | System | 25 | Text | System name |
| C | Date | 12 | Date | Threat model date |
| D | Author | 20 | Text | Author name |
| E | Methodology | 15 | Dropdown | STRIDE/PASTA/OCTAVE/Other |
| F | Completeness | 12 | Dropdown | 1/2/3/4/5 |
| G | Quality | 12 | Dropdown | 1/2/3/4/5 |
| H | ATT&CK_Mapped | 12 | Dropdown | Yes/Partial/No |
| I | Findings | 10 | Number | Count |
| J | Mitigated | 10 | Number | Count |

### Sheet 8: Compliance

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Compliance |
| **Purpose** | Policy compliance scoring |
| **Protection** | Data entry enabled |

**Standard compliance sheet structure with 15 requirements**

### Sheet 9: GapRegister

| Property | Specification |
|----------|---------------|
| **Sheet Name** | GapRegister |
| **Purpose** | Gap tracking and remediation |
| **Protection** | Data entry enabled |

**Standard gap register structure**

### Sheet 10: Dashboard

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Dashboard |
| **Purpose** | Summary view and ATT&CK heatmap |
| **Protection** | Read-only (formulas only) |

**Dashboard Elements:**

1. Overall methodology maturity score
2. MITRE ATT&CK coverage percentage by tactic
3. Threat catalogue completeness
4. Tool effectiveness summary
5. Competency gap chart
6. Sample quality metrics
7. ATT&CK coverage heatmap (simplified)

## Styling Specifications

**Use standard ISMS colour palette as per ISMS-IMP-A.8.27.1**

## Pre-populated Data

**Methodology Requirements (20 rows):**

STRIDE components, PASTA phases, documentation standards

**ATT&CK Techniques (50 rows):**

Top 50 enterprise techniques by prevalence, organised by tactic

**Threat Actors (15 rows):**

Standard threat actor categories with examples

**Tools (8 rows):**

Common threat modelling tools

**Competencies (12 rows):**

Role-based competency requirements

---

# Generator Script Reference

## Script Information

| Property | Value |
|----------|-------|
| **Script Name** | generate_a827_2_threat_modelling.py |
| **Location** | 10-isms-scr-base/isms-a.8.27-secure-systems-engineering/10_generator-master/ |
| **Output** | ISMS-IMP-A.8.27.2_Threat_Modelling_Methodology_YYYYMMDD.xlsx |

---

**END OF SPECIFICATION**

---

*"If you know the enemy and know yourself, you need not fear the result of a hundred battles."*
— Sun Tzu, The Art of War

<!-- QA_VERIFIED: [Date] -->
