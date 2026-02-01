# ISMS-IMP-A.6.6.2 — NDA Execution and Tracking

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.6.2 |
| **Title** | NDA Execution and Tracking |
| **Control Reference** | ISO/IEC 27001:2022 A.6.6 |
| **Control Name** | Confidentiality or Non-Disclosure Agreements |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

## PART I: USER COMPLETION GUIDE

### Assessment Overview

**Purpose**

This workbook tracks all executed (signed) NDAs, individual signatories, expiration dates, and renewal requirements to ensure complete coverage of confidentiality protection.

**Scope**

- All signed confidentiality and non-disclosure agreements
- Individual signatory tracking by stakeholder category
- Expiration monitoring and alerts
- Renewal management and tracking

**Control Requirements**

ISO 27001:2022 Control A.6.6 requires NDAs be "signed by personnel and other relevant interested parties."

### Prerequisites

- [ ] Access to signed NDA repository
- [ ] HR records for employee NDAs
- [ ] Contract management system for vendor NDAs
- [ ] Signatory contact information

### Workbook Structure

| Sheet | Purpose | Key Actions |
|-------|---------|-------------|
| Instructions | Guidance | Review before starting |
| Active_NDAs | Current NDAs | Register all active NDAs |
| Signatory_Register | Individual tracking | Track each signatory |
| Expiration_Monitor | Expiration tracking | Monitor upcoming expirations |
| Renewal_Tracking | Renewal management | Track renewal process |
| Evidence_Register | Evidence tracking | Link evidence |
| Approval_SignOff | Authorisation | Obtain approvals |

### Completion Walkthrough

**Step 1: Active_NDAs Sheet**

Register all active NDAs:

1. **NDA_ID** - Unique identifier
2. **Template_Ref** - Link to template registry
3. **NDA_Title** - Agreement title
4. **Counterparty** - Other party name
5. **Counterparty_Type** - Employee/Contractor/Vendor/etc.
6. **Execution_Date** - When signed
7. **Effective_Date** - When becomes effective
8. **Expiration_Date** - When expires (or "Indefinite")
9. **Post_Term_Period** - Duration after termination
10. **Post_Term_Expiry** - When post-term ends
11. **Signatories_Count** - Number of signatories
12. **Storage_Location** - Where original stored
13. **Status** - Active/Expired/Terminated/Renewed

**Step 2: Signatory_Register Sheet**

Track individual signatories:

1. **Signatory_ID** - Unique identifier
2. **NDA_Ref** - Link to Active_NDAs
3. **Signatory_Name** - Full name
4. **Signatory_Type** - Role category
5. **Organisation** - Their employer
6. **Role_Title** - Job title
7. **Email** - Contact email
8. **Signature_Date** - When they signed
9. **Signature_Method** - Wet/Digital/Electronic
10. **Termination_Date** - If relationship ended
11. **Status** - Active/Terminated

**Step 3: Expiration_Monitor Sheet**

Monitor upcoming expirations:

1. **NDA_ID** - Link to Active_NDAs
2. **Counterparty** - Party name
3. **Expiration_Date** - When expires
4. **Days_Until_Expiry** - Calculated days remaining
5. **Alert_Status** - Green/Amber/Red/Expired
6. **Renewal_Required** - Yes/No/Under Review
7. **Renewal_Owner** - Who manages renewal
8. **Action_Required** - Next steps

**Alert Thresholds**:

| Alert | Condition |
|-------|-----------|
| Green | >90 days to expiry |
| Amber | 30-90 days to expiry |
| Red | <30 days to expiry |
| Expired | Past expiration date |

**Step 4: Renewal_Tracking Sheet**

Track renewal process:

1. **Renewal_ID** - Unique identifier
2. **Original_NDA** - Link to expiring NDA
3. **Counterparty** - Party name
4. **Original_Expiry** - Original expiration
5. **Renewal_Initiated** - When process started
6. **New_Terms_Required** - Yes/No
7. **Legal_Review** - Yes/No/Pending
8. **Counterparty_Agreed** - Yes/No/Pending
9. **New_NDA_ID** - Link to new NDA
10. **New_Expiry** - New expiration date
11. **Status** - Not Started/In Progress/Completed

### Evidence Collection

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Signed NDAs | Original executed agreements | HR/Contracts repository |
| Signature Certificates | DocuSign/Adobe Sign certificates | ISMS Evidence Library |
| Renewal Records | Renewal correspondence | ISMS Evidence Library |

### Common Pitfalls

❌ **MISTAKE**: NDAs stored in personal folders
✅ **CORRECT**: Centralised, secure storage with backup

❌ **MISTAKE**: No tracking of individual signatories
✅ **CORRECT**: Track each person who signed

❌ **MISTAKE**: Expiration dates not monitored
✅ **CORRECT**: Monthly expiration monitoring with alerts

❌ **MISTAKE**: Renewed NDAs not linked to originals
✅ **CORRECT**: Maintain chain of renewal history

❌ **MISTAKE**: Post-termination obligations not tracked
✅ **CORRECT**: Track when post-term period ends

❌ **MISTAKE**: Missing signature date records
✅ **CORRECT**: Record exact signature date for each party

❌ **MISTAKE**: Terminated employees still showing as active
✅ **CORRECT**: Update status when relationship ends

❌ **MISTAKE**: No renewal process initiation
✅ **CORRECT**: Start renewal 90 days before expiry

### Quality Checklist

- [ ] All active NDAs registered
- [ ] All signatories tracked individually
- [ ] Expiration monitoring current
- [ ] Renewal process initiated for expiring NDAs
- [ ] Storage locations verified
- [ ] Approval sign-offs obtained

---

## PART II: TECHNICAL SPECIFICATION

### Workbook Architecture

**File Details**:

- Filename: `ISMS-IMP-A.6.6.2_NDA_Execution_and_Tracking_YYYYMMDD.xlsx`
- Format: Microsoft Excel (.xlsx)
- Sheets: 7

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Counterparty_Type | Employee, Contractor, Consultant, Vendor, Supplier, Partner, Customer, Board Member, Visitor, Other |
| NDA_Status | Active, Expired, Terminated, Renewed, Superseded |
| Signatory_Type | Employee, Contractor, Consultant, Vendor Rep, Partner Rep, Customer Rep, Board Member, Visitor, Witness, Authorised Signatory |
| Signature_Method | Wet Signature, Digital Signature, Electronic Signature, DocuSign, Adobe Sign, Other |
| Alert_Status | Green (>90 days), Amber (30-90 days), Red (<30 days), Expired |
| Renewal_Status | Not Started, In Progress, Legal Review, Awaiting Signature, Completed, Cancelled |

### Generator Reference

**Script**: `generate_a66_2_nda_execution_tracking.py`

**Location**: `10-isms-scr-base/isms-a.6.6-confidentiality-nda/10_generator-master/`

---

**END OF SPECIFICATION**

---

*"A verbal contract isn't worth the paper it's written on."*
— Samuel Goldwyn

<!-- QA_VERIFIED: 2026-02-01 -->
