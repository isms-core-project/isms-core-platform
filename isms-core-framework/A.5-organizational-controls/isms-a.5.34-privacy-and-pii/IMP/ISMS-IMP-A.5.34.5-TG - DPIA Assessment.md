<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.34.5-TG:framework:TG:a.5.34.5 -->
**ISMS-IMP-A.5.34.5-TG - Data Protection Impact Assessment (DPIA)**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.34.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Data Protection Impact Assessment (DPIA) for High-Risk Processing Activities |
| **Related Policy** | ISMS-POL-A.5.34, Section 2.5 (Data Protection Impact Assessment) |
| **Purpose** | Guide users through DPIA trigger assessment, systematic risk evaluation, and compliance with GDPR Article 35 requirements for high-risk processing activities |
| **Target Audience** | DPO/Privacy Officers, Legal Counsel, Business Owners, Product Managers, IT/Security Teams, Compliance Officers, Auditors |
| **Assessment Type** | Risk Assessment & Compliance |
| **Review Cycle** | Annual or upon introduction of new high-risk processing activities |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for DPIA assessment workbook | ISMS Implementation Team |

---

**Document Purpose**

This implementation guide specifies procedures for conducting Data Protection Impact Assessments (DPIAs) as required by GDPR Article 35. A DPIA is a systematic process to evaluate the necessity, proportionality, and risks of processing operations that are likely to result in high risk to individuals' rights and freedoms.

**Key Objectives:**
1. Identify processing activities requiring DPIA (trigger assessment)
2. Conduct systematic risk assessment for high-risk processing
3. Implement appropriate mitigation measures to reduce risks
4. Maintain comprehensive DPIA register for audit and compliance
5. Ensure stakeholder consultation (DPO, data subjects, supervisory authority)
6. Track DPIA lifecycle from initial assessment through annual reviews

**Regulatory Foundation:**

**GDPR Article 35(1):** "Where a type of processing in particular using new technologies, and taking into account the nature, scope, context and purposes of the processing, is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall, prior to the processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data."

**GDPR Article 35(3) - Mandatory DPIA Triggers:**

- (a) Systematic and extensive evaluation of personal aspects including profiling with legal/similarly significant effects
- (b) Large-scale processing of special category data (Art. 9) or criminal convictions (Art. 10)
- (c) Systematic monitoring of publicly accessible areas on a large scale (e.g., CCTV)

**Additional WP248 Triggers:**

- Innovative technologies or novel applications of existing technology
- Processing that prevents data subjects from exercising rights or using services
- Processing on a large scale
- Matching/combining datasets from different sources
- Processing vulnerable data subjects (children, employees, mentally ill)
- Processing involving cross-border data transfers outside EEA
- Decisions with potential to cause significant harm (automated decision-making)

**ISO/IEC 27001:2022 Control A.5.34 Requirement:** Organizations must implement privacy impact assessments when required by applicable privacy regulations.

---
# Technical Specification


> Auto-generated from `generate_a5345_dpia_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.34.5` |
| **Output Filename** | `ISMS-IMP-A.5.34.5_Data_Protection_Impact_Assessment_(DPIA)_YYYYMMDD.xlsx` |
| **Workbook Title** | Data Protection Impact Assessment (DPIA) |
| **Total Sheets** | 8 (8 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Sheet 1: Instructions

**Data Rows:** 16 (rows 1–16)

---

## Sheet 2: Trigger_Assessment

**Data Rows:** 999 (rows 2–1000) | **Frozen Panes:** A2

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Processing Activity ID | 20 |
| B | Processing Activity Name | 30 |
| C | System/Application | 25 |
| D | Trigger 1: Systematic Profiling | 18 |
| E | Trigger 2: Large-Scale Special Categories | 18 |
| F | Trigger 3: Systematic Monitoring | 18 |
| G | Trigger 4: Innovative Technology | 18 |
| H | Trigger 5: Denial of Service | 18 |
| I | Trigger 6: Large Scale | 18 |
| J | Trigger 7: Matching Datasets | 18 |
| K | Trigger 8: Vulnerable Subjects | 18 |
| L | Trigger 9: Cross-Border Transfer | 18 |
| M | Total Triggers | 12 |
| N | DPIA Required? | 15 |
| O | Notes | 40 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| M2:M1000 | equal 0 | Fill: light_green |
| M2:M1000 | equal 1 | Fill: light_yellow |
| M2:M1000 | greaterThanOrEqual 2 | Fill: light_red |
| N2:N1000 | equal  | Fill: light_green |
| N2:N1000 | equal  | Fill: light_yellow |
| N2:N1000 | equal  | Fill: light_red |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| MN | `=COUNTIF(D{row}:L{row},` |  |
| NN | `=IF(M{row}>=2,` |  |

---

## Sheet 3: Dpia_Register

**Data Rows:** 999 (rows 2–1000) | **Frozen Panes:** A2

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | DPIA ID | 18 |
| B | Processing Activity ID | 20 |
| C | Processing Activity Name | 30 |
| D | System/Application | 25 |
| E | Business Owner | 20 |
| F | DPO Assigned | 20 |
| G | DPIA Start Date | 15 |
| H | Target Completion Date | 15 |
| I | Actual Completion Date | 15 |
| J | DPIA Status | 15 |
| K | Initial Risk Rating | 15 |
| L | Residual Risk Rating | 15 |
| M | Supervisory Authority Consulted? | 18 |
| N | Authority Consultation Date | 15 |
| O | Authority Reference Number | 20 |
| P | Next Review Date | 15 |
| Q | DPIA Document Location | 40 |
| R | Notes | 40 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| J2:J1000 | equal  | Fill: light_green |
| J2:J1000 | equal  | Fill: light_yellow |
| J2:J1000 | equal  | Fill: light_red |
| J2:J1000 | equal  | Fill: light_blue |
| J2:J1000 | equal  | Fill: light_gray |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| CN | `=IFERROR(VLOOKUP(B{row},Trigger_Assessment!$A$2:$B$1000,2,FALSE),` |  |
| PN | `=IF(ISBLANK(I{row}),` |  |

---

## Sheet 4: Risk_Assessment

**Data Rows:** 999 (rows 2–1000) | **Frozen Panes:** A2

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | DPIA ID | 18 |
| B | Risk ID | 20 |
| C | Risk Category | 20 |
| D | Risk Description | 50 |
| E | Data Subject Impact | 40 |
| F | Likelihood (Before Mitigation) | 15 |
| G | Impact (Before Mitigation) | 15 |
| H | Inherent Risk Score | 12 |
| I | Inherent Risk Level | 15 |
| J | Necessity Justified? | 15 |
| K | Necessity Justification | 40 |
| L | Proportionality Justified? | 15 |
| M | Proportionality Justification | 40 |
| N | Legal Basis | 20 |
| O | Special Category Legal Basis | 20 |
| P | Data Subject Rights Respected? | 15 |
| Q | Rights Restrictions Documented | 40 |
| R | Third-Party Recipients | 30 |
| S | Cross-Border Transfers | 15 |
| T | Transfer Safeguards | 30 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| H2:H1000 | between 1 | Fill: light_green |
| H2:H1000 | between 8 | Fill: light_yellow |
| H2:H1000 | between 15 | Fill: light_orange |
| H2:H1000 | greaterThanOrEqual 20 | Fill: light_red |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=IF(ISBLANK(A{row}),` |  |
| HN | `=IF(OR(ISBLANK(F{row}),ISBLANK(G{row})),` |  |
| IN | `=IF(ISBLANK(H{row}),` |  |

---

## Sheet 5: Mitigation_Measures

**Data Rows:** 999 (rows 2–1000) | **Frozen Panes:** A2

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Risk ID | 20 |
| B | Risk Description (Reference) | 50 |
| C | Mitigation Control ID | 20 |
| D | Control Type | 20 |
| E | Mitigation Description | 50 |
| F | Implementation Status | 15 |
| G | Owner | 20 |
| H | Target Date | 15 |
| I | Actual Date | 15 |
| J | Effectiveness Rating | 15 |
| K | Evidence Location | 40 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| F2:F1000 | equal  | Fill: light_green |
| F2:F1000 | equal  | Fill: light_green |
| F2:F1000 | equal  | Fill: light_yellow |
| F2:F1000 | equal  | Fill: light_gray |
| F2:F1000 | equal  | Fill: light_red |
| J2:J1000 | equal  | Fill: light_green |
| J2:J1000 | equal  | Fill: light_green |
| J2:J1000 | equal  | Fill: light_yellow |
| J2:J1000 | equal  | Fill: light_red |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=IFERROR(VLOOKUP(A{row},Risk_Assessment!$B$2:$D$1000,2,FALSE),` |  |
| CN | `=IF(ISBLANK(A{row}),` |  |

---

## Sheet 6: Stakeholder_Consultation

**Data Rows:** 999 (rows 2–1000) | **Frozen Panes:** A2

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | DPIA ID | 18 |
| B | Stakeholder Type | 20 |
| C | Stakeholder Name/Title | 25 |
| D | Consultation Date | 15 |
| E | Consultation Method | 20 |
| F | Key Concerns Raised | 50 |
| G | Recommendations | 50 |
| H | Action Taken | 50 |
| I | Evidence Location | 40 |

---

## Sheet 7: Gap_Analysis

**Data Rows:** 999 (rows 2–1000) | **Frozen Panes:** A2

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Risk ID | 20 |
| B | Inherent Risk Score (Reference) | 15 |
| C | Mitigation Implemented? | 15 |
| D | Mitigation Effectiveness | 15 |
| E | Risk Reduction Factor | 12 |
| F | Residual Likelihood | 12 |
| G | Residual Risk Score | 12 |
| H | Residual Risk Level | 15 |
| I | Gap Identified? | 12 |
| J | Gap Description | 50 |
| K | Remediation Plan | 50 |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| I2:I1000 | equal  | Fill: light_red |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=IFERROR(VLOOKUP(A{row},Risk_Assessment!$B$2:$H$1000,7,FALSE),` |  |
| FN | `=IF(ISBLANK(B{row}),` |  |
| HN | `=IF(ISBLANK(G{row}),` |  |

---

## Sheet 8: Dashboard

**Data Rows:** 999 (rows 2–1000)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(DPIA_Register!A2:A1000)` | Total DPIAs Registered |
| — | `=COUNTIF(DPIA_Register!J2:J1000,` | DPIAs Complete |
| — | `=IF(C3=0,0,C4/C3)` | Completion Rate |
| — | `=COUNTIF(DPIA_Register!M2:M1000,` | Supervisory Authority Consultations |
| — | `=COUNTA(Risk_Assessment!B2:B1000)` | Total Risks Identified |
| — | `=COUNTIF(Risk_Assessment!I2:I1000,` | Critical Risks |
| — | `=COUNTA(Mitigation_Measures!C2:C1000)` | Total Mitigation Controls |
| — | `=COUNTIF(Mitigation_Measures!F2:F1000,` | Controls Validated |
| — | `=IF(C24=0,0,(C25+C26)/C24)` | Mitigation Completion Rate |
| — | `=COUNTA(Gap_Analysis!A2:A1000)` | Total Assessed Risks |
| — | `=COUNTIF(Gap_Analysis!H2:H1000,` | Residual Risk - Critical |
| — | `=COUNTIF(Risk_Assessment!J2:J1000,` | Necessity Justified (Yes) |
| — | `=COUNTIF(Risk_Assessment!L2:L1000,` | Proportionality Justified (Yes) |
| — | `=COUNTIF(Risk_Assessment!P2:P1000,` | Data Subject Rights Fully Respected |
| — | `=COUNTA(Stakeholder_Consultation!A2:A1000)` | Stakeholder Consultations Conducted |
| — | `=IF(C3=0,0,C7*0.4+C28*0.3+IF(C34=0,0,(1-C36/C34)*0.3))` | Overall DPIA Compliance Score |

---

**END OF SPECIFICATION**

---

*"Whenever we proceed from the known into the unknown we may hope to understand, but we may have to learn at the same time a new meaning of the word understanding."*
— Werner Heisenberg

<!-- QA_VERIFIED: 2026-02-06 -->
