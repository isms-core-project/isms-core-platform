<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.34.2-TG:framework:TG:a.5.34.2 -->
**ISMS-IMP-A.5.34.2-TG - Legal Basis and Lawful Processing Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.34.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Legal Basis Assessment, Legitimate Interest Assessments (LIAs), and Consent Management |
| **Related Policy** | ISMS-POL-A.5.34, Section 2.2 (Legal Basis and Lawful Processing) |
| **Purpose** | Guide users through GDPR Article 6 legal basis documentation, Legitimate Interest Assessments (LIAs), consent validity evaluation, and special category data safeguards (Article 9) |
| **Target Audience** | DPO/Privacy Officers, Legal Counsel, Business Owners, Marketing Teams, Compliance Officers, Auditors |
| **Assessment Type** | Legal & Compliance |
| **Review Cycle** | Annual or upon new processing activities |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Legal Basis assessment workbook | ISMS Implementation Team |

---


---
# Technical Specification
**Audience:** Workbook developers (Python/Excel script maintainers), Technical implementation teams


> Auto-generated from `generate_a5342_legal_basis_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.34.2` |
| **Output Filename** | `ISMS-IMP-A.5.34.2_Legal_Basis_and_Lawful_Processing_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Legal Basis and Lawful Processing Assessment |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | COLOR_HEADER | Dark Blue (Headers) |
| #9BC2E6 | COLOR_LOW | Custom |
| #C00000 | COLOR_CRITICAL | Dark Red (Blocked) |
| #C6EFCE | COLOR_COMPLIANT | Light Green (Compliant/Pass) |
| #D6DCE4 | COLOR_INSTRUCTION | Silver (Neutral) |
| #F2F2F2 | COLOR_CALCULATED | Very Light Gray (Protected/Alternating) |
| #FF6600 | COLOR_HIGH | Custom |
| #FFC7CE | COLOR_GAP | Light Red (Non-Compliant/Fail) |
| #FFD966 | COLOR_MEDIUM | Gold/Yellow (Highlight) |
| #FFEB9C | COLOR_REVIEW | Light Yellow/Amber (Partial) |

## Sheet 1: Header_Row

---

## Sheet 2: 1. Instructions & Legend

---

## Sheet 3: 2. Legal Basis Inventory

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Activity ID | 15 |
| B | Processing Activity | 40 |
| C | Processing Purpose | 50 |
| D | Legal Basis (GDPR Art. 6) | 30 |
| E | Legal Basis Justification | 60 |
| F | Data Subject Information | 30 |
| G | Special Category Data? | 15 |
| H | GDPR Art. 9 Legal Basis | 30 |
| I | Consent Status | 20 |
| J | Consent Mechanism | 30 |
| K | LIA Required? | 15 |
| L | LIA Reference | 20 |
| M | Legal Basis Evidence | 50 |
| N | Compliance Status | 20 |
| O | Remediation Plan | 60 |

---

## Sheet 4: 3. Legitimate Interest Assessments

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | LIA ID | 15 |
| B | Activity ID
(from Sheet 2) | 15 |
| C | Legitimate Interest | 50 |
| D | Beneficiary | 20 |
| E | Legitimacy Assessment | 20 |
| F | Necessity Assessment | 50 |
| G | Alternative Methods Considered | 50 |
| H | Necessity Conclusion | 20 |
| I | Data Subject's Interests | 50 |
| J | Data Subject Expectations | 20 |
| K | Impact Assessment | 20 |
| L | Safeguards Implemented | 50 |
| M | Balancing Test Result | 30 |
| N | Assessor Name | 25 |
| O | Assessment Date | 15 |
| P | DPO Approval | 15 |
| Q | Approval Date | 15 |

---

## Sheet 5: 4. Consent Management

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Consent ID | 15 |
| B | Activity ID
(from Sheet 2) | 15 |
| C | Consent Purpose | 40 |
| D | Consent Date | 15 |
| E | Consent Mechanism | 30 |
| F | Freely Given? | 15 |
| G | Specific? | 15 |
| H | Informed? | 15 |
| I | Unambiguous? | 15 |
| J | Documented? | 15 |
| K | Consent Validity | 25 |
| L | Withdrawal Mechanism Available? | 15 |
| M | Withdrawal Mechanism Description | 50 |
| N | Withdrawal Processing Time | 20 |
| O | Consent Records Location | 40 |
| P | Audit Trail Available? | 15 |
| Q | Evidence Reference | 20 |

---

## Sheet 6: 5. Legal Basis Gaps

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Activity ID | 15 |
| B | Processing Activity | 40 |
| C | Current Legal Basis | 30 |
| D | Gap Type | 30 |
| E | Risk Level | 15 |
| F | Remediation Priority | 15 |
| G | Remediation Action | 60 |
| H | Remediation Owner | 25 |
| I | Target Date | 15 |
| J | Status | 15 |
| K | Completion Date | 15 |
| L | Verification Notes | 50 |

---

## Sheet 7: 6. Evidence Repository

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 15 |
| B | Evidence Type | 30 |
| C | Description | 50 |
| D | File Location | 60 |
| E | Linked Activity IDs | 30 |
| F | Verified By | 25 |
| G | Verification Date | 15 |
| H | Verification Status | 20 |
| I | Notes | 50 |

---

## Sheet 8: 7. Dashboard

---

## Sheet 9: 8. Approval & Sign-Off

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `APPROVAL_STATUS` | Approved, Approved with Conditions, Requires Revision, Rejected |
| `COMPLIANCE_STATUS` | Compliant, Requires Review, Gap - No Legal Basis, Gap - Invalid Consent, Gap - Missing LIA |
| `CONSENT_MECHANISMS` | Website Form (Opt-In Checkbox), Double Opt-In (Email Confirmation), Written Signature, Verbal Con... |
| `CONSENT_STATUS` | Valid, Invalid - Not Freely Given, Invalid - Not Specific, Invalid - Not Informed, Invalid - Ambi... |
| `DS_INFORMATION_CHANNELS` | Privacy Notice (Website), Privacy Notice (Contract), Consent Form, Employee Handbook, Terms of Se... |
| `EVIDENCE_TYPES` | Consent Records, Customer Contract, Employment Contract, Processor Agreement (DPA), Legal Obligat... |
| `LEGAL_BASIS_ART6` | Consent (GDPR Art. 6(1)(a)), Contract (GDPR Art. 6(1)(b)), Legal Obligation (GDPR Art. 6(1)(c)), ... |
| `LEGAL_BASIS_ART9` | Explicit Consent (Art. 9(2)(a)), Employment Law (Art. 9(2)(b)), Vital Interests (Art. 9(2)(c)), L... |
| `LIA_BENEFICIARY` | Controller, Data Subject, Third Party, Multiple Parties |
| `LIA_EXPECTATIONS` | Reasonable Expectation, Unexpected, Surprising |
| `LIA_IMPACT` | Minimal Impact, Limited Impact, Significant Impact, High Impact |
| `LIA_LEGITIMACY` | Legitimate, Questionable, Not Legitimate |
| `LIA_NECESSITY` | Necessary, Questionable, Not Necessary |
| `LIA_RESULT` | Pass - Legitimate Interest Prevails, Pass with Conditions, Fail - Data Subject's Rights Prevail |
| `REMEDIATION_STATUS` | Not Started, In Progress, Complete, Blocked |
| `RISK_LEVELS` | Critical, High, Medium, Low |
| `VERIFICATION_STATUS` | Valid, Expired, Requires Update, Under Review |
| `YES_NO` | Yes, No |
| `YES_NO_PENDING` | Yes, No, Pending |
| `YES_NO_UNCERTAIN` | Yes, No, Uncertain |

---

**END OF SPECIFICATION**

---

*"The right to be let alone is indeed the beginning of all freedom."*
— William O. Douglas

<!-- QA_VERIFIED: 2026-02-06 -->
