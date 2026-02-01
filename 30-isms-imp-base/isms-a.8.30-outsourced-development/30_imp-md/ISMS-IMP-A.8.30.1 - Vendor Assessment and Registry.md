# ISMS-IMP-A.8.30.1 – Vendor Assessment and Registry

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.8.30.1 |
| **Document Title** | Vendor Assessment and Registry Workbook Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.30: Outsourced Development |
| **Parent Policy** | ISMS-POL-A.8.30 (Outsourced Development) |
| **Version** | 1.0 |
| **Classification** | Internal |

---

## 1. Workbook Purpose

This workbook captures vendor security assessment results and maintains the approved vendor registry for outsourced development engagements.

**Primary Use Cases**:
- Pre-engagement vendor security assessments
- Approved vendor registry management
- Annual vendor reassessment tracking
- Due diligence evidence for audits

---

## 2. Workbook Structure

### Sheet 1: Vendor Registry

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Vendor_ID | Unique vendor identifier | Text | VND-XXXX format |
| Vendor_Name | Legal entity name | Text | Required |
| Registry_Status | Approval status | Dropdown | Approved, Pending, Suspended, Removed |
| Risk_Tier | Vendor risk classification | Dropdown | Critical, High, Standard |
| Initial_Assessment_Date | Date of first assessment | Date | DD.MM.YYYY |
| Last_Assessment_Date | Most recent assessment date | Date | DD.MM.YYYY |
| Next_Assessment_Due | Reassessment due date | Date | DD.MM.YYYY |
| ISO_27001_Certified | Certification status | Dropdown | Yes, No, In Progress |
| SOC2_Type2 | SOC 2 Type II status | Dropdown | Yes, No, N/A |
| Primary_Contact | Vendor security contact | Text | Email format |
| Approved_Project_Types | Authorized project scopes | Multi-select | Critical, High, Standard |
| Approved_By | Approval authority | Text | Name + Role |
| Notes | Additional information | Text | Optional |

### Sheet 2: Security Assessment

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Assessment_ID | Unique assessment identifier | Text | ASM-XXXX format |
| Vendor_ID | Link to vendor registry | Reference | Valid Vendor_ID |
| Assessment_Date | Date assessment completed | Date | DD.MM.YYYY |
| Assessment_Type | Type of assessment | Dropdown | Initial, Annual, Triggered |
| Assessor | Person conducting assessment | Text | Name |
| Security_Certification | Valid security certification | Dropdown | ISO 27001, SOC 2, Both, None |
| Cert_Expiry_Date | Certification expiration | Date | DD.MM.YYYY |
| SDLC_Maturity | Secure development maturity | Dropdown | Mature, Developing, Basic, Unknown |
| Security_Incident_History | Major incidents in 24 months | Dropdown | None, Minor, Major |
| SAST_DAST_Tooling | Security testing tools in use | Text | Tool names |
| Personnel_Screening | Background check policy | Dropdown | Verified, Attested, Unknown |
| Dev_Environment_Security | Environment security status | Dropdown | Compliant, Partial, Non-Compliant |
| Overall_Risk_Rating | Combined risk assessment | Dropdown | Low, Medium, High, Critical |
| Recommendation | Assessment recommendation | Dropdown | Approve, Conditional, Reject |
| Conditions | Conditions for approval | Text | If conditional |
| Evidence_Location | Assessment evidence path | Text | File path/URL |

### Sheet 3: Due Diligence Checklist

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Vendor_ID | Link to vendor registry | Reference | Valid Vendor_ID |
| Check_Category | Due diligence category | Text | Category name |
| Check_Item | Specific check item | Text | Check description |
| Status | Completion status | Dropdown | Complete, Pending, N/A |
| Evidence_Type | Type of evidence collected | Dropdown | Certificate, Attestation, Document, Interview |
| Evidence_Reference | Evidence document reference | Text | File path/URL |
| Verified_By | Person who verified | Text | Name |
| Verified_Date | Date verified | Date | DD.MM.YYYY |
| Notes | Additional notes | Text | Optional |

**Standard Due Diligence Categories**:
1. Security Certification Verification
2. Secure Development Practices
3. Security Incident History
4. Technical Security Capabilities
5. Personnel Security
6. Physical Security (if on-site development)
7. Subcontractor Management
8. Business Continuity
9. Insurance Coverage
10. Reference Checks

### Sheet 4: Environment Security Assessment

| Column | Description | Data Type | Validation |
|--------|-------------|-----------|------------|
| Vendor_ID | Link to vendor registry | Reference | Valid Vendor_ID |
| Assessment_Date | Date of environment assessment | Date | DD.MM.YYYY |
| MFA_Enabled | MFA for all development access | Dropdown | Yes, Partial, No |
| Network_Isolation | Dev environment isolation | Dropdown | Isolated, Segmented, Shared |
| Endpoint_Security | Developer workstation security | Dropdown | Compliant, Partial, Non-Compliant |
| Code_Repository | Repository security status | Dropdown | Secure, Partial, Unsecure |
| Secret_Scanning | Secret scanning enabled | Dropdown | Yes, No |
| Branch_Protection | Branch protection configured | Dropdown | Yes, Partial, No |
| Data_Handling | Production data handling | Dropdown | No Prod Data, Masked, Raw (Non-Compliant) |
| Attestation_Received | Vendor security attestation | Dropdown | Yes, No |
| Attestation_Date | Date of attestation | Date | DD.MM.YYYY |
| Compliance_Status | Overall compliance | Dropdown | Compliant, Conditional, Non-Compliant |

---

## 3. Data Sources

| Data Element | Source System | Collection Method |
|--------------|---------------|-------------------|
| Vendor information | Vendor Management System / Procurement | Manual entry, import |
| Certification status | Vendor attestation, certification bodies | Document collection |
| Assessment responses | Security questionnaire | Vendor submission |
| Reference checks | Previous clients | Phone/email interviews |
| Environment security | Vendor attestation, audit | Assessment checklist |

---

## 4. Assessment Workflow

```
1. Vendor Identified for Engagement
         ↓
2. Risk Tier Classification (Critical/High/Standard)
         ↓
3. Security Questionnaire Sent
         ↓
4. Questionnaire Reviewed by IT Security
         ↓
5. Due Diligence Checks Completed
         ↓
6. Environment Security Assessed (for system access)
         ↓
7. Risk Rating Assigned
         ↓
8. Recommendation Made (Approve/Conditional/Reject)
         ↓
9. Approval by Appropriate Authority
         ↓
10. Added to Approved Vendor Registry
         ↓
11. Annual Reassessment Scheduled
```

---

## 5. Metrics and KPIs

| Metric | Target | Measurement |
|--------|--------|-------------|
| Vendor assessment completion rate | 100% before engagement | Assessments completed / New vendors |
| Assessment SLA compliance | 100% within 10 business days | On-time assessments / Total assessments |
| Approved vendor registry accuracy | 100% up-to-date | Vendors with current assessments / Total approved |
| Annual reassessment completion | 100% on schedule | On-time reassessments / Due reassessments |
| High-risk vendor monitoring | 100% quarterly review | Reviewed / High-risk vendors |

---

## 6. Automation Requirements

**Automated Alerts**:
- 60 days before certification expiration
- 30 days before reassessment due
- Immediately if vendor suspended or removed

**Data Validation**:
- Vendor_ID uniqueness enforced
- Date format validation (Swiss: DD.MM.YYYY)
- Required field completion checks
- Cross-reference validation (Vendor_ID exists in registry)

---

## 7. Evidence Package

For ISO 27001 audit, generate:
- Approved vendor registry export (current state)
- Assessment records for sampled vendors
- Due diligence checklists with evidence references
- Environment attestations
- Assessment trend analysis (12 months)

---

**END OF SPECIFICATION**

---

*"The strength of the team is each individual member. The strength of each member is the team."*
— Phil Jackson

<!-- QA_VERIFIED: 2026-02-01 -->
