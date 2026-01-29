# ISMS-POL-A.8.12-S5.B
## Annex B: DLP Exception Request Template

**Document ID**: ISMS-POL-A.8.12-S5.B  
**Title**: Exception Request Template  
**Version**: 1.0  
**Date**: 2025-01-03  
**Classification**: Internal  
**Owner**: Information Security Officer  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-03 | ISO | Initial exception template |

**Review Cycle**: As needed (template updates based on process improvements)  
**Next Review Date**: 2026-01-03  
**Approvers**: ISO / Security Manager

**Distribution**: All employees (self-service exception requests)  
**Related Documents**: ISMS-POL-A.8.12-S4 (Policy Governance - Exception Management)

---

## DLP EXCEPTION REQUEST FORM

**Instructions:** Complete all sections. Incomplete requests will be returned. Submit to: [dlp-exceptions@company.com] or via [Self-Service Portal Link]

---

### SECTION 1: REQUESTOR INFORMATION

| Field | Response |
|-------|----------|
| **Your Name:** | |
| **Employee ID:** | |
| **Department:** | |
| **Manager Name:** | |
| **Manager Email:** | |
| **Request Date:** | [Auto-populated] |

---

### SECTION 2: EXCEPTION TYPE

**Select exception type (check one):**

☐ **User Exception** - I need to transfer data via a normally restricted channel  
☐ **Data Exception** - Specific data type needs different handling  
☐ **Channel Exception** - Specific channel needs temporary exception  
☐ **Technical Exception** - DLP rule causing false positives  

---

### SECTION 3: EXCEPTION DETAILS

| Field | Response |
|-------|----------|
| **What do you need to do?** (Be specific) | |
| **What data will be transferred?** (Classification level, type) | ☐ Public ☐ Internal ☐ Confidential ☐ Restricted<br><br>Data type: _________________ |
| **Which channel?** | ☐ Email ☐ Web/Cloud ☐ USB ☐ Network ☐ Application ☐ Mobile |
| **Destination** (Where is data going? IP, domain, recipient email, USB device) | |
| **Frequency** (How often will you transfer this data?) | ☐ One-time ☐ Weekly ☐ Daily ☐ Other: _______ |

---

### SECTION 4: BUSINESS JUSTIFICATION

| Field | Response |
|-------|----------|
| **Why is this exception needed?** (Business justification) | |
| **What is the business impact if exception is denied?** | |
| **Are there alternative secure methods?** (If yes, why not use them?) | ☐ Yes ☐ No<br><br>Explanation: _________________ |
| **Is this a recurring business need or one-time request?** | ☐ One-time ☐ Recurring |

---

### SECTION 5: RISK ASSESSMENT

| Field | Response |
|-------|----------|
| **Is the recipient/destination trusted?** (Existing business partner, approved vendor, etc.) | ☐ Yes ☐ No<br><br>Details: _________________ |
| **What are the risks if this data is mishandled?** | |
| **Proposed compensating controls** (Encryption, password protection, redaction, time limits, etc.) | |

---

### SECTION 6: DURATION

| Field | Response |
|-------|----------|
| **Exception start date:** | |
| **Exception end date (maximum 90 days):** | |
| **If permanent exception requested, provide justification:** | |

---

### SECTION 7: APPROVALS

#### Manager Approval (Required for all exceptions)

| Field | Response |
|-------|----------|
| **Manager Name:** | |
| **Manager Approval:** | ☐ Approved ☐ Denied |
| **Manager Comments:** | |
| **Manager Signature & Date:** | |

#### Security Team Review (Completed by ISO/Security Team)

| Field | Response |
|-------|----------|
| **Reviewer Name:** | |
| **Risk Level:** | ☐ Low ☐ Medium ☐ High |
| **Recommendation:** | ☐ Approve ☐ Approve with Conditions ☐ Deny |
| **Conditions/Compensating Controls:** | |
| **Reviewer Comments:** | |
| **Reviewer Signature & Date:** | |

#### CISO Approval (Required for Medium/High risk)

| Field | Response |
|-------|----------|
| **CISO Decision:** | ☐ Approved ☐ Approved with Conditions ☐ Denied |
| **CISO Comments:** | |
| **CISO Signature & Date:** | |

#### DPO Approval (Required for High risk involving personal data)

| Field | Response |
|-------|----------|
| **DPO Decision:** | ☐ Approved ☐ Approved with Conditions ☐ Denied |
| **DPO Comments:** | |
| **DPO Signature & Date:** | |

---

### SECTION 8: IMPLEMENTATION (Completed by IT Operations)

| Field | Response |
|-------|----------|
| **Exception implemented by:** | |
| **Implementation date:** | |
| **DLP rule ID / configuration:** | |
| **Monitoring/logging enabled:** | ☐ Yes ☐ No |
| **Exception expiration reminder set:** | ☐ Yes (30 days before expiration) |

---

### EXCEPTION REGISTER TRACKING

| Field | Auto-Populated |
|-------|----------------|
| **Exception ID:** | [AUTO] |
| **Status:** | ☐ Submitted ☐ Under Review ☐ Approved ☐ Implemented ☐ Expired ☐ Revoked |
| **Review Date (monthly/quarterly):** | [AUTO - based on risk level] |

---

## APPROVAL AUTHORITY MATRIX

| Risk Level | Criteria | Approval Required |
|------------|----------|-------------------|
| **Low** | Internal transfer, <30 days, non-sensitive data | Manager + ISO/Security Manager |
| **Medium** | Confidential data, approved partner, <90 days | Manager + CISO |
| **High** | Restricted data, unapproved destination, permanent | Manager + CISO + DPO + Data Owner |

---

## EMERGENCY EXCEPTION PROCESS

**For urgent business needs requiring immediate exception:**

1. **Contact Security Team:** Phone [XXX-XXX-XXXX] or Email [dlp-emergency@company.com]
2. **Verbal approval:** CISO (any risk) or Security Manager (Low/Medium risk only)
3. **Documentation:** Formal request submitted within 1 business day
4. **Formal approval:** Within 3 business days (validate emergency was legitimate)

**Invalid Emergency Scenarios:** Poor planning, convenience, personal preference

---

## POST-EXCEPTION REVIEW

**All exceptions are reviewed:**
- **Monthly:** Security Team reviews all active exceptions
- **Quarterly:** CISO reviews all Medium/High exceptions
- **Annually:** Full exception register audit

**Automatic Revocation:** Exceptions expire on stated end date unless renewed

---

**END OF DOCUMENT**

*"An exception without justification is a violation waiting to happen."* 📋