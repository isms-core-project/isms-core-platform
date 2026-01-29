# Control A.8.24: Use of Cryptography
## APPENDIX B
## Exception Request Form Template

---

**Document ID**: ISMS-POL-A.8.24-S5.B  
**Title**: Use of Cryptography - Exception Request Form Template  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Risk Management Officer | Initial exception management framework |

**Review Cycle**: Annual (or upon exception process audit findings)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Risk: Risk Management Officer (for risk acceptance framework)
- Compliance: Legal/Compliance Officer (for regulatory exception boundaries)
- Business: Chief Information Officer (CIO) for business impact assessment

**Distribution**: IT Security Team, Risk Management, Compliance Officers, Project Managers, Architecture Review Board  
**Related Standards**: ISO/IEC 27001:2022 Clauses 6.1.3 (Risk Treatment), A.8.24, risk acceptance frameworks

---

## Purpose of This Form

This form is used to request an exception to the Cryptography Policy (ISMS-POL-A.8.24) when full compliance is not technically feasible or when business requirements necessitate a deviation from policy standards.

**Before submitting this form:**
1. Review the policy requirements thoroughly
2. Attempt to achieve compliance through standard means
3. Consult with Information Security team for guidance
4. Ensure you have documented business justification

**Submission Instructions:**
- Complete all sections of this form
- Attach supporting documentation (technical analysis, risk assessment, etc.)
- Submit to: Information Security Officer (ISO) or Security Team
- Submission method: [Email/Ticketing System/Portal]

---

## SECTION 1: REQUEST INFORMATION

### 1.1 Request Details

| Field | Information |
|-------|-------------|
| **Request ID** | *(Auto-assigned by ISO upon receipt)* |
| **Submission Date** | DD.MM.YYYY |
| **Requested By** | Name: ___________________________<br>Title: ___________________________<br>Department: ___________________________<br>Email: ___________________________<br>Phone: ___________________________ |
| **System Owner** | Name: ___________________________<br>Title: ___________________________<br>Email: ___________________________ |
| **Manager/Supervisor** | Name: ___________________________<br>Title: ___________________________<br>Email: ___________________________ |

---

## SECTION 2: SYSTEM/APPLICATION IDENTIFICATION

### 2.1 System Information

| Field | Information |
|-------|-------------|
| **System/Application Name** |  |
| **System Classification** | ☐ Production<br>☐ Development<br>☐ Testing<br>☐ Other: _________________ |
| **Data Classification** | ☐ Public<br>☐ Internal<br>☐ Confidential<br>☐ Restricted |
| **Environment** | ☐ On-premises<br>☐ Cloud (Provider: _________)<br>☐ Hybrid |
| **System Description** | Brief description of the system and its purpose:<br><br><br><br> |
| **Users/Stakeholders** | Number of users: _________<br>Key stakeholders: |

---

## SECTION 3: POLICY DEVIATION

### 3.1 Policy Requirement Unable to Comply With

**Refer to specific policy section(s):**

| Policy Section | Requirement Description |
|----------------|------------------------|
| **Section Number(s)** | Example: 2.1.2 (Approved Cryptographic Standards), 2.2.1 (HTTPS/TLS) |
| **Specific Requirement** | Copy the exact requirement from the policy that cannot be met:<br><br><br><br> |

### 3.2 Current Implementation State

**Describe the current cryptographic implementation:**

| Current State | Details |
|---------------|---------|
| **What is currently implemented?** | Example: TLS 1.1, 3DES encryption, password stored with bcrypt cost 10<br><br><br><br> |
| **How does this differ from policy?** | Example: Policy requires TLS 1.2+, AES-256, bcrypt cost ≥12<br><br><br><br> |

---

## SECTION 4: JUSTIFICATION

### 4.1 Technical Justification

**Why is compliance not technically feasible?**

☐ Legacy system with no cryptographic configuration options
☐ Third-party application with no control over cryptographic settings
☐ Hardware/firmware limitations
☐ Incompatibility with required systems/protocols
☐ Other (explain below)

**Detailed Technical Explanation:**
```
Provide technical details on why the policy requirement cannot be met.
Include:
- Technical constraints
- Vendor/product limitations
- System architecture dependencies
- Integration requirements








```

### 4.2 Business Justification

**Why is this system necessary despite non-compliance?**

☐ Critical business function with no alternative
☐ Regulatory or contractual requirement
☐ Customer-facing system with business impact if unavailable
☐ Legacy system scheduled for replacement (provide timeline)
☐ Cost of compliance grossly disproportionate to risk
☐ Other (explain below)

**Detailed Business Explanation:**
```
Explain the business impact if this exception is not granted.
Include:
- Business processes dependent on this system
- Financial impact of non-operation
- Customer/partner impact
- Timeline for remediation (if applicable)








```

---

## SECTION 5: RISK ASSESSMENT

### 5.1 Risk Analysis

**Likelihood of Security Incident:**
☐ Low (unlikely to occur)
☐ Medium (possible but not probable)
☐ High (likely to occur)
☐ Critical (very likely or already occurred)

**Impact if Security Incident Occurs:**
☐ Low (minimal impact, limited scope)
☐ Medium (moderate impact, some business disruption)
☐ High (significant impact, major business disruption)
☐ Critical (severe impact, regulatory breach, data exposure)

**Overall Risk Level:** *(Calculated by ISO)*
☐ Low
☐ Medium
☐ High
☐ Critical

### 5.2 Threat Description

**What could go wrong? What are the specific threats?**
```
Describe potential security incidents that could result from this non-compliance.
Examples:
- Man-in-the-middle attack due to weak TLS
- Password compromise due to weak hashing
- Data exposure due to lack of encryption









```

### 5.3 Impact Analysis

**If a security incident occurs, what would be the consequences?**

| Impact Category | Description |
|-----------------|-------------|
| **Confidentiality Impact** | ☐ None  ☐ Limited  ☐ Moderate  ☐ Severe<br>Details: |
| **Integrity Impact** | ☐ None  ☐ Limited  ☐ Moderate  ☐ Severe<br>Details: |
| **Availability Impact** | ☐ None  ☐ Limited  ☐ Moderate  ☐ Severe<br>Details: |
| **Regulatory/Legal Impact** | ☐ None  ☐ Limited  ☐ Moderate  ☐ Severe<br>Details: |
| **Reputational Impact** | ☐ None  ☐ Limited  ☐ Moderate  ☐ Severe<br>Details: |
| **Financial Impact** | Estimated: $____________ |

---

## SECTION 6: COMPENSATING CONTROLS

### 6.1 Compensating Controls Implemented or Proposed

**Compensating controls are alternative security measures that reduce risk to an acceptable level.**

**List all compensating controls:**

| Control # | Compensating Control Description | Implementation Status |
|-----------|----------------------------------|----------------------|
| **1** | Example: Network segmentation - system isolated on separate VLAN with firewall rules | ☐ Implemented  ☐ Planned |
| **2** | Example: Enhanced monitoring with 24/7 SOC alerting | ☐ Implemented  ☐ Planned |
| **3** | Example: Additional access controls - MFA required | ☐ Implemented  ☐ Planned |
| **4** |  | ☐ Implemented  ☐ Planned |
| **5** |  | ☐ Implemented  ☐ Planned |

### 6.2 Compensating Controls Effectiveness

**How do these compensating controls mitigate the identified risk?**
```
Explain how the compensating controls reduce the likelihood or impact of a security incident.








```

**Why are these compensating controls adequate?**
```
Justify that the combination of compensating controls provides risk reduction equivalent to policy compliance.








```

---

## SECTION 7: REMEDIATION PLAN

### 7.1 Remediation Strategy

**Is this exception temporary or permanent?**
☐ Temporary (remediation planned)
☐ Permanent (system cannot be brought into compliance)

### 7.2 Temporary Exception - Remediation Plan

*(Complete this section if temporary exception)*

**How will the system be brought into compliance?**
```
Describe the specific actions that will be taken to achieve compliance.
Example: Upgrade to new version of software that supports TLS 1.2+, migrate to new system








```

**Remediation Timeline:**

| Milestone | Target Date | Responsible Person |
|-----------|-------------|-------------------|
| **Planning/Design** | DD.MM.YYYY |  |
| **Budget Approval** | DD.MM.YYYY |  |
| **Procurement (if needed)** | DD.MM.YYYY |  |
| **Implementation** | DD.MM.YYYY |  |
| **Testing** | DD.MM.YYYY |  |
| **Deployment** | DD.MM.YYYY |  |
| **Full Compliance** | DD.MM.YYYY |  |

**Estimated Budget:** $_______________

**Dependencies/Blockers:**
```
List any dependencies or potential blockers to achieving compliance.





```

### 7.3 Permanent Exception - Justification

*(Complete this section if permanent exception)*

**Why can this system never be brought into compliance?**
```
Provide justification for permanent exception.
Example: Legacy system required by regulation, vendor no longer supports product, system scheduled for decommission








```

**System End-of-Life Date:** DD.MM.YYYY *(if applicable)*

**Replacement System Plan:**
```
If system will be replaced, describe replacement plans and timeline.





```

---

## SECTION 8: EXCEPTION DURATION

### 8.1 Requested Exception Period

**Exception Start Date:** DD.MM.YYYY

**Exception End Date:** DD.MM.YYYY

**Exception Duration:** _____ months

**Justification for Duration:**
```
Explain why this duration is necessary.
- For temporary exceptions: Must align with remediation timeline
- For permanent exceptions: Typically annual renewal required





```

### 8.2 Review Schedule

**How often should this exception be reviewed?**
☐ Quarterly
☐ Semi-annually
☐ Annually
☐ Other: _________________

---

## SECTION 9: DEPENDENCIES AND RELATED SYSTEMS

### 9.1 System Dependencies

**Does this system interact with other systems?**
☐ Yes ☐ No

**If yes, list dependent systems and potential impact:**

| Dependent System | Impact of This Exception |
|------------------|-------------------------|
| 1. |  |
| 2. |  |
| 3. |  |

---

## SECTION 10: MONITORING AND REPORTING

### 10.1 Monitoring Requirements

**How will this exception be monitored?**
```
Describe monitoring controls that will be in place.
Examples:
- Security event monitoring and alerting
- Monthly compliance reviews
- Automated scanning for vulnerabilities
- Access log review








```

**Monitoring Frequency:**
☐ Real-time/Continuous
☐ Daily
☐ Weekly
☐ Monthly
☐ Quarterly

**Responsible for Monitoring:** ___________________________

### 10.2 Incident Reporting

**If a security incident occurs related to this exception, who should be notified?**

1. Immediate notification: ___________________________
2. Security Team: ___________________________
3. Management: ___________________________

---

## SECTION 11: ATTACHMENTS AND SUPPORTING DOCUMENTATION

**Attach all relevant documentation:**

☐ Technical architecture diagram
☐ Vendor documentation (limitations, constraints)
☐ Risk assessment report
☐ Remediation project plan
☐ Cost-benefit analysis
☐ Regulatory/compliance requirement documentation
☐ Other: _________________________________

**List attachments:**
1. ___________________________
2. ___________________________
3. ___________________________

---

## SECTION 12: REQUESTOR CERTIFICATION

**I certify that:**
- The information provided in this exception request is accurate and complete
- I have attempted to achieve compliance through standard means
- I have consulted with relevant technical teams
- I understand the risks associated with this exception
- I commit to implementing and maintaining compensating controls
- I will adhere to the review schedule and report any changes in risk posture

**Requestor Signature:** ___________________________ **Date:** ___________

**System Owner Signature:** ___________________________ **Date:** ___________

**Manager/Supervisor Signature:** ___________________________ **Date:** ___________

---

## SECTION 13: SECURITY TEAM REVIEW

*(For completion by Information Security Officer or Security Team)*

**Reviewed By:** ___________________________

**Review Date:** DD.MM.YYYY

**Risk Assessment Validated:**
☐ Agree with requestor's risk assessment
☐ Adjust risk level to: _______________
☐ Additional risk analysis required

**Compensating Controls Assessment:**
☐ Adequate - risk reduced to acceptable level
☐ Inadequate - additional controls required (specify below)
☐ Not applicable

**Additional Controls Required:**
```




```

**Recommendation:**
☐ Approve as submitted
☐ Approve with conditions (specify below)
☐ Deny (provide reasons below)
☐ Return for revision (specify required changes below)

**Conditions/Required Changes:**
```




```

**ISO/Security Manager Signature:** ___________________________ **Date:** ___________

---

## SECTION 14: APPROVAL

*(Complete based on risk level and approval authority per Section 6.2.2 of Policy Governance)*

### Approval Authority

**Risk Level:** ☐ Low  ☐ Medium  ☐ High  ☐ Critical

**Required Approvals:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **IT Manager**<br>*(Required for Low risk)* |  |  |  |
| **Security Team Lead**<br>*(Required for Low risk)* |  |  |  |
| **CISO**<br>*(Required for Medium/High/Critical)* |  |  |  |
| **Senior Management (CIO/CTO)**<br>*(Required for High/Critical)* |  |  |  |
| **Executive Committee**<br>*(Required for Critical)* |  |  |  |

### Approval Conditions

**Exception Granted:** ☐ Yes  ☐ No  ☐ Conditional

**If conditional, specify conditions:**
```




```

**Approved Exception Period:**
- Start Date: DD.MM.YYYY
- End Date: DD.MM.YYYY
- Review Date: DD.MM.YYYY

**Exception ID:** *(Assigned by ISO)* EXC-A824-YYYY-####

---

## SECTION 15: TRACKING AND CLOSURE

*(For ISO/Compliance Team use)*

**Exception Register Entry:** ☐ Created  ☐ Updated

**Risk Register Entry:** ☐ Created  ☐ Updated

**Audit Log Entry:** ☐ Created

**Monitoring Setup:** ☐ Completed  ☐ Not Required

**Review Reminders Set:** ☐ Completed

**Stakeholders Notified:** ☐ Completed

### Exception Closure

**Exception Closed Date:** DD.MM.YYYY

**Closure Reason:**
☐ System came into compliance
☐ System decommissioned
☐ Exception expired (not renewed)
☐ Compensating controls deemed inadequate
☐ Risk level unacceptable
☐ Other: _________________________________

**Closed By:** ___________________________

**Closure Verification:** ___________________________ **Date:** ___________

---

## Instructions for Completing This Form

### General Guidelines
1. **Be thorough and specific** - Provide detailed information in all sections
2. **Attach supporting documentation** - Technical reports, vendor documentation, project plans
3. **Consult before submitting** - Speak with Security Team for guidance
4. **Allow processing time** - Typical processing: Low risk (5 days), Medium (10 days), High (15 days), Critical (20 days)

### Common Reasons for Rejection
- Insufficient justification
- Inadequate compensating controls
- No remediation plan for temporary exceptions
- Risk level deemed unacceptable
- Alternative compliant solutions available

### Tips for Successful Exception Requests
- **Start early** - Don't wait until the last minute
- **Be realistic** - Provide accurate timelines and cost estimates
- **Focus on compensating controls** - Strong compensating controls increase approval likelihood
- **Show commitment** - Demonstrate you're taking the exception seriously
- **Consider alternatives** - Have you truly exhausted all options for compliance?

### Need Help?
Contact the Information Security Team:
- **Email:** security@[organization].com
- **Phone:** [phone number]
- **Office Hours:** [hours]

---

**End of Appendix B - Exception Request Form Template**

*"Exceptions are like antibiotics: useful when necessary, dangerous when overused, and they create resistant strains when misapplied."*  
*— The Medical Model of Security Governance*