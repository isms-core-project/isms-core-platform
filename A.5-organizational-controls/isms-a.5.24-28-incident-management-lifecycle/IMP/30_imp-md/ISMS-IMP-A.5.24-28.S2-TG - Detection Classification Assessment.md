**ISMS-IMP-A.5.24-28.S2-TG - Incident Detection & Classification Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.24: Information Security Incident Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Incident Detection & Classification Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S2-TG |
| **Assessment Domain** | Domain 2 - Detection & Classification (A.5.25 Focus) |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Related Reference** | ISMS-REF-A.5.24-28 (Incident Response Reference Guide) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | SOC Manager / Detection Engineering Lead |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | SOC Manager | Initial detection & classification assessment specification |

**Review Cycle**: Annual (or after major detection capability changes)  
**Next Review Date**: [Effective Date + 12 months]  

**Related Documents**: 

- ISMS-POL-A.5.24-28 (Incident Management Lifecycle Policy)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide, Section 1: Incident Classification Taxonomy)
- ISMS-IMP-A.5.24-28.S1 (Framework & Governance Assessment)
- ISMS-IMP-A.5.24-28.S3 (Response Capabilities Assessment)
- ISMS-IMP-A.5.24-28.S4 (Forensic Evidence Assessment)
- ISMS-IMP-A.5.24-28.S5 (Learning & Improvement Assessment)
- ISMS-IMP-A.8.16 (Security Monitoring Assessment)
- ISO/IEC 27002:2022 Control A.5.25
- NIST SP 800-61 Rev. 2 Section 3.2 (Detection and Analysis)

---

# Technical Specification

# Workbook Structure

**Sheet 1: Instructions & Legend** - Assessment guidance
**Sheet 2: Detection Mechanisms** - 33 questions (SIEM, EDR, IDS/IPS, NDR, user reporting, coverage by category)
**Sheet 3: Alert Handling** - 25 questions (triage, playbooks, escalation, capacity)
**Sheet 4: Classification & Severity** - 25 questions (category assignment, severity criteria, consistency)
**Sheet 5: Detection Effectiveness** - 25 questions (MTTD, MTTT, false positives, coverage gaps)
**Sheet 6: Gap Analysis** - 40 gap capacity
**Sheet 7: Evidence Register** - 60 evidence capacity
**Sheet 8: Dashboard** - Detection effectiveness summary
**Sheet 9: Approval Sign-Off** - SOC Manager + CISO approval

---

# Python Script Specifications

**Total Questions:** 108 (33+25+25+25)
**Calculated Metrics:** MTTD, MTTT, False Positive Rate, Coverage %, Alert-to-Incident Ratio
**Conditional Formatting:** 

- Red: High false positive rate (>30%), Poor MTTD (>24h), Low coverage (<60%)
- Yellow: Medium thresholds
- Green: Good performance

**Data Validation:**

- Dropdowns for all categorical questions
- Date format validation
- Percentage validation (0-100%)
- Duration format guidance

---

**END OF SPECIFICATION**

---

*"The first principle is that you must not fool yourself — and you are the easiest person to fool."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
