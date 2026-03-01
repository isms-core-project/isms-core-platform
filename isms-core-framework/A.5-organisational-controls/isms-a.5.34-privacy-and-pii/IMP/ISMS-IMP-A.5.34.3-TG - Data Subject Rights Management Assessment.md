<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.34.3-TG:framework:TG:a.5.34.3 -->
**ISMS-IMP-A.5.34.3-TG - Data Subject Rights Management Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Data Subject Rights Management Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.34.3-TG |
| **Related Policy** | ISMS-POL-A.5.34 (Privacy and Pii) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.34 (Privacy and Protection of PII) |
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

- ISMS-POL-A.5.34 (Privacy and Pii)
- ISMS-IMP-A.5.34.1 (PII Identification and Classification Assessment)
- ISMS-IMP-A.5.34.2 (Legal Basis and Lawful Processing Assessment)
- ISMS-IMP-A.5.34.4 (Technical and Organisational Measures (TOMs) Assessment)
- ISMS-IMP-A.5.34.5 (DPIA Assessment)
- ISMS-IMP-A.5.34.6 (Cross Border Transfer Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a5343_dsr_management_assessment.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.34.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 2. DSR Request Inventory |
| 3 | 3. Request Process. Procedures |
| 4 | 4. SLA Compliance Tracking |
| 5 | 5. Exception & Reject. Tracking |
| 6 | 6. Rights-Specific Analysis |
| 7 | 7. Evidence Repository |
| 8 | Summary Dashboard |
| 9 | Approval Sign-Off |

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
| 1 | Status Legend |
| 2 | Request ID |
| 3 | Receipt Date |
| 4 | Request Channel |
| 5 | Right Type |
| 6 | Requester Name |
| 7 | Requester Contact |
| 8 | Request Description |
| 9 | Request Scope |
| 10 | Identity Verification Method |
| 11 | Verification Status |
| 12 | Verification Date |
| 13 | Response Date |
| 14 | Response Deadline |
| 15 | Days to Respond |
| 16 | SLA Status |
| 17 | Response Method |
| 18 | Response Description |
| 19 | Request Outcome |
| 20 | Rejection Reason |
| 21 | Extension Justification |
| 22 | Requester Satisfaction |
| 23 | Request Complexity |
| 24 | Effort (Hours) |
| 25 | Assigned To |
| 26 | Evidence Reference |
| 27 | Standard Response Time |
| 28 | Identity Verification Required |
| 29 | Typical Fulfillment Steps |
| 30 | Systems Involved |
| 31 | Quality Checklist |
| 32 | Common Exceptions |
| 33 | Escalation Criteria |
| 34 | Total |
| 35 | SLA Met |
| 36 | SLA Breached |
| 37 | Avg Response Time |
| 38 | Exception Legal Basis |
| 39 | Detailed Justification |
| 40 | Data Subject Notified |
| 41 | Appeal Rights Communicated |
| 42 | Alternative Measures Offered |
| 43 | DPO Review |
| 44 | Legal Counsel Review |
| 45 | Requester Response |
| 46 | Evidence ID |
| 47 | Request ID (Link) |
| 48 | Evidence Type |
| 49 | Description |
| 50 | File Location |
| 51 | Evidence Date |
| 52 | Retention Period (Years) |
| 53 | Notes |
| 54 | Assessment Area |
| 55 | Total Items |
| 56 | Compliant |
| 57 | Partial |
| 58 | Non-Compliant |
| 59 | N/A |
| 60 | Compliance % |
| 61 | Metric |
| 62 | Value |
| 63 | Category |
| 64 | Finding |
| 65 | Count |
| 66 | Severity |
| 67 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 67 columns, 8 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The existing scientific concepts cover always only a very limited part of reality, and the other part that has not yet been understood is infinite."*
— Werner Heisenberg

<!-- QA_VERIFIED: 2026-02-06 -->
