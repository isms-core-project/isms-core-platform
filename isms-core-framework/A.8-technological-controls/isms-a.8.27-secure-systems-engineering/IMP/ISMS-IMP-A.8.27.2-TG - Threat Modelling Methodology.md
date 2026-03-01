<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.27.2-TG:framework:TG:a.8.27.2 -->
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
| **Related Policy** | ISMS-POL-A.8.27 (Secure Systems Engineering) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.27 (Secure System Architecture and Engineering Principles) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.8.27 (Secure Systems Engineering)
- ISMS-IMP-A.8.27.1 (Security Architecture Review Process)
- ISMS-IMP-A.8.27.3 (Secure Architecture Pattern Catalogue)
- ISMS-IMP-A.8.27.4 (Zero Trust Implementation Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a827_2_threat_modelling.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.27.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Methodology Assessment |
| 2 | Methodology |
| 3 | D |
| 4 | MITRE ATT&CK Coverage |
| 5 | MITRE ATT&CK |
| 6 | E |
| 7 | Licensed |
| 8 | Competency Assessment |
| 9 | Competency |
| 10 | Sample Quality Review |
| 11 | Samples |
| 12 | H |
| 13 | Policy Compliance |
| 14 | Compliance |
| 15 | Instructions & Legend |
| 16 | ThreatCatalogue |
| 17 | Tools |
| 18 | Evidence Register |
| 19 | Summary Dashboard |
| 20 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #C00000 | Dark Red (Blocked) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | APT Groups |
| 2 | Security Architect |
| 3 | STRIDE Methodology |
| 4 | Authentication Service |
| 5 | Security Team Lead |
| 6 | Overall Compliance Score: |
| 7 | What This Shows |
| 8 | Critical Finding Type |
| 9 | Filter Instructions |
| 10 | Meth-ID |
| 11 | Category |
| 12 | Requirement |
| 13 | Adopted |
| 14 | Documented |
| 15 | Effective |
| 16 | Evidence |
| 17 | Gaps |
| 18 | ATT-ID |
| 19 | Tactic |
| 20 | Technique |
| 21 | Relevance |
| 22 | Covered |
| 23 | DetectionMap |
| 24 | Gap |
| 25 | Threat-ID |
| 26 | ThreatActor |
| 27 | Motivation |
| 28 | Capability |
| 29 | ATT&CK Ref |
| 30 | Likelihood |
| 31 | Countermeasures |
| 32 | Tool-ID |
| 33 | Tool |
| 34 | Purpose |
| 35 | Licensed |
| 36 | Users |
| 37 | Integration |
| 38 | Effectiveness |
| 39 | Comp-ID |
| 40 | Role |
| 41 | Competency |
| 42 | Required |
| 43 | Training |
| 44 | Certified |
| 45 | Target |
| 46 | Sample-ID |
| 47 | System |
| 48 | Date |
| 49 | Author |
| 50 | Methodology |
| 51 | Completeness |
| 52 | Quality |
| 53 | ATT&CK Mapped |
| 54 | Findings |
| 55 | Mitigated |
| 56 | Source |
| 57 | Compliant |
| 58 | Score |
| 59 | Notes |
| 60 | Evidence ID |
| 61 | Assessment Area |
| 62 | Evidence Type |
| 63 | Description |
| 64 | Location / Path |
| 65 | Date Collected |
| 66 | Collected By |
| 67 | Verification Status |
| 68 | Total Items |
| 69 | Partial |
| 70 | Non-Compliant |
| 71 | N/A |
| 72 | Compliance % |

### Data Validation Values

All dropdown/list values used across sheets:

```
✅ Yes, ⚠️ Partial, ❌ No, 1, 2, 3, 4, 5, High, Medium, Low, N/A, Financial
Espionage, Disruption, Ideology, Revenge, Moderate, Nation-State, Rare
Unlikely, Possible, Likely, Almost Certain, Yes, No, OSS, Mandatory
Recommended, STRIDE, PASTA, OCTAVE, Other, Policy Document, Process Record
System Screenshot, Configuration Export, Audit Log, Training Record
Test Result, Risk Assessment, Meeting Minutes, ✅ Verified, ⚠️ Pending
❌ Not Verified, Draft, Final, Requires remediation, Re-assessment required
Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 20 sheets, 72 columns, 53 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"If you know the enemy and know yourself, you need not fear the result of a hundred battles."*
— Sun Tzu, The Art of War

<!-- QA_VERIFIED: [Date] -->
