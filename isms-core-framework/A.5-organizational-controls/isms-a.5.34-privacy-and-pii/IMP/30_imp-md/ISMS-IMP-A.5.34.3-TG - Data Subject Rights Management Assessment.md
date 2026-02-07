**ISMS-IMP-A.5.34.3-TG - Data Subject Rights Management Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.34.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Data Subject Rights (DSR) Request Management and GDPR Articles 15-22 Compliance |
| **Related Policy** | ISMS-POL-A.5.34, Section 2.3 (Data Subject Rights Management) |
| **Purpose** | Guide users through DSR request tracking, SLA compliance monitoring (30-day deadline per Article 12), identity verification, and exception handling for GDPR Articles 15-22 rights |
| **Target Audience** | DPO/Privacy Officers, Privacy Team, Customer Service, Legal Counsel, IT Teams, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Monthly for SLA tracking, Annual for process assessment |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for DSR Management assessment workbook | ISMS Implementation Team |

---
# Technical Specification
**Audience:** Assessment Workbook Developers, Python Script Users, Technical Implementation Teams


> Auto-generated from `generate_a5343_dsr_management_assessment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.34.3` |
| **Output Filename** | `ISMS-IMP-A.5.34.3_Data_Subject_Rights_Management_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Data Subject Rights Management Assessment |
| **Total Sheets** | 10 (10 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | COLOR_HEADER | Dark Blue (Headers) |
| #C6EFCE | COLOR_SLA_MET | Light Green (Compliant/Pass) |
| #D6DCE4 | COLOR_INSTRUCTION | Silver (Neutral) |
| #F2F2F2 | COLOR_CALCULATED | Very Light Gray (Protected/Alternating) |
| #FFC7CE | COLOR_SLA_BREACHED | Light Red (Non-Compliant/Fail) |
| #FFD966 | COLOR_WARNING | Gold/Yellow (Highlight) |
| #FFEB9C | COLOR_PENDING | Light Yellow/Amber (Partial) |

## Sheet 1: Header_Row

---

## Sheet 2: 1. Instructions & Legend

---

## Sheet 3: 2. DSR Request Inventory

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Request ID | 15 |
| B | Receipt Date | 12 |
| C | Request Channel | 15 |
| D | Right Type | 20 |
| E | Requester Name | 25 |
| F | Requester Contact | 30 |
| G | Request Description | 50 |
| H | Request Scope | 40 |
| I | Identity Verification Method | 20 |
| J | Verification Status | 18 |
| K | Verification Date | 12 |
| L | Response Date | 12 |
| M | Response Deadline | 12 |
| N | Days to Respond | 12 |
| O | SLA Status | 12 |
| P | Response Method | 18 |
| Q | Response Description | 50 |
| R | Request Outcome | 20 |
| S | Rejection Reason | 40 |
| T | Extension Justification | 50 |
| U | Requester Satisfaction | 15 |
| V | Request Complexity | 15 |
| W | Effort (Hours) | 10 |
| X | Assigned To | 25 |
| Y | Evidence Reference | 15 |

---

## Sheet 4: 3. Request Processing Procedures

**Data Rows:** 7 (rows 2–8)

### Columns

| Col | Header |
|-----|--------|
| A | Right Type |
| B | Standard Response Time |
| C | Identity Verification Required |
| D | Typical Fulfillment Steps |
| E | Systems Involved |
| F | Quality Checklist |
| G | Common Exceptions |
| H | Escalation Criteria |

---

## Sheet 5: 4. SLA Compliance Tracking

---

## Sheet 6: 5. Exception & Rejection Tracking

### Columns

| Col | Header |
|-----|--------|
| A | Request ID |
| B | Right Type |
| C | Exception Legal Basis |
| D | Detailed Justification |
| E | Data Subject Notified |
| F | Appeal Rights Communicated |
| G | Alternative Measures Offered |
| H | DPO Review |
| I | Legal Counsel Review |
| J | Requester Response |

---

## Sheet 7: 6. Rights-Specific Analysis

---

## Sheet 8: 7. Evidence Repository

### Columns

| Col | Header |
|-----|--------|
| A | Evidence ID |
| B | Request ID (Link) |
| C | Evidence Type |
| D | Description |
| E | File Location |
| F | Evidence Date |
| G | Retention Period (Years) |
| H | Verification Status |
| I | Notes |

---

## Sheet 9: 8. Dashboard

---

## Sheet 10: 9. Approval & Sign-Off

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `APPROVAL_STATUS` | Approved, Approved with Conditions, Requires Revision, Rejected |
| `COMPLEXITY_LEVELS` | Low, Medium, High, Very High |
| `EVIDENCE_TYPES` | Request Email, Response Email, Data Export (Access/Portability), Deletion Certificate (Erasure), ... |
| `IDENTITY_VERIFICATION_METHODS` | Account Login, Email Confirmation, ID Document, Phone Verification, In-Person, Not Required |
| `REJECTION_REASONS` | Legal Obligation (Art. 17(3)(b) - Tax, Employment Law), Legal Claims (Art. 17(3)(e) - Litigation,... |
| `REQUESTER_RESPONSES` | Accepted, Appealed to Supervisory Authority, Disputed, No Response |
| `REQUEST_CHANNELS` | Email, Web Portal, Phone, Postal Mail, In-Person |
| `REQUEST_OUTCOMES` | Fulfilled, Partially Fulfilled, Rejected, Extended, Withdrawn |
| `RESPONSE_METHODS` | Email, Secure Portal, Postal Mail, In-Person, Download Link |
| `RIGHT_TYPES` | Access (Art. 15), Rectification (Art. 16), Erasure (Art. 17), Restriction (Art. 18), Data Portabi... |
| `SATISFACTION_LEVELS` | Satisfied, Neutral, Dissatisfied, No Feedback |
| `VERIFICATION_STATUS` | Verified, Verification Failed, Verification Pending, Not Required |
| `VERIFICATION_STATUS_EVIDENCE` | Complete, Incomplete, Under Review, Archived |
| `YES_NO` | Yes, No |
| `YES_NO_NA` | Yes, No, N/A |
| `YES_NO_PENDING` | Yes, No, Pending |

---

**END OF SPECIFICATION**

---

*"The existing scientific concepts cover always only a very limited part of reality, and the other part that has not yet been understood is infinite."*
— Werner Heisenberg

<!-- QA_VERIFIED: 2026-02-06 -->
