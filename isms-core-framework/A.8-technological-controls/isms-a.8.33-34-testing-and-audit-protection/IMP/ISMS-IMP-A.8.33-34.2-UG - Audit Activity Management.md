<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.33-34.2-UG:framework:UG:a.8.33-34.2 -->
**ISMS-IMP-A.8.33-34.2-UG - Audit Activity Management Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Controls A.8.33: Test Information & A.8.34: Protection of Information Systems During Audit Testing

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Audit Activity Management |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.33-34.2-UG |
| **Related Policy** | ISMS-POL-A.8.33-34 (Testing and Audit Protection) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.33 (Test Information) & A.8.34 (Protection of Information Systems During Audit Testing) |
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

- ISMS-POL-A.8.33-34 (Testing and Audit Protection)
- ISMS-IMP-A.8.33-34.1 (Test Data Protection)

---

### ISO/IEC 27001:2022 Controls A.8.33: Test Information & A.8.34: Protection of Information Systems During Audit Testing

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.33-34.2-UG |
| **Version** | 1.0 |
| **Assessment Area** | Audit Activity Governance & System Protection |
| **Related Policy** | ISMS-POL-A.8.33-34, Section 2.2 (Audit Activity Management) |
| **Purpose** | Assess organisational compliance with audit testing governance including activity planning, tool authorisation, access control, disruption mitigation, and evidence protection |
| **Target Audience** | Internal Audit, External Auditors, IT Security, Penetration Testers, Compliance Officers, IT Operations, Risk Management, Legal |
| **Assessment Type** | Process & Operational Compliance |
| **Review Cycle** | Annual (minimum) or After Major Audits |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Audit Activity Management assessment workbook | ISMS Implementation Team |

---

**Audience:** Internal Audit, External Auditors, IT Security Managers, Penetration Testers, Compliance Officers

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Audit Activity Register | Registry of all planned and completed audit activities |
| 3 | Audit Tool Authorisation | Governance of audit tools and testing techniques |
| 4 | Audit Access Tracking | Track access granted during audit activities |
| 5 | Disruption Mitigation Plans | Plans to mitigate system disruption during audits |
| 6 | Audit Evidence Protection | Assess protection of audit evidence and findings |
| 7 | Evidence Register | Store and reference evidence supporting assessments |
| 8 | Summary Dashboard | Compliance status and key metrics overview |
| 9 | Approval Sign-Off | Management review sign-off and certification |

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organisation]'s implementation of **audit testing governance and system protection mechanisms** to ensure compliance with ISO/IEC 27001:2022 Control A.8.34 (Protection of Information Systems During Audit Testing) and related requirements for protecting operational systems during assurance activities.

**Scope:** Complete audit activity lifecycle management across 5 critical areas:

1. **Audit Activity Register** - Registry of all planned and completed audit activities
2. **Audit Tool Authorisation** - Governance of audit tools and testing techniques
3. **Audit Access Tracking** - Management of auditor access to systems and data
4. **Disruption Mitigation Plans** - Protection measures for production systems during testing
5. **Audit Evidence Protection** - Secure handling and retention of audit evidence

**Assessment Output:** Excel workbook with ~200-300 data points documenting current audit governance posture, tool authorisation status, access controls, system protection measures, and remediation plans for identified gaps.

## Why This Matters

**ISO 27001:2022 Control A.8.34 Requirement:**
> *"Audit tests and other assurance activities involving assessment of operational systems should be planned and agreed between the tester and appropriate management."*

**Key Control Objectives:**

- Prevent audit activities from disrupting business operations
- Ensure audit tools do not introduce security vulnerabilities
- Maintain confidentiality of sensitive information accessed during audits
- Protect audit evidence integrity
- Ensure proper authorisation for all testing activities

**Regulatory Context:**

- **ISO 27001:2022 (A.8.34):** Protection of information systems during audit testing
- **SOC 2 Type II:** Audit activity controls and evidence handling
- **PCI-DSS (11.3):** Penetration testing requirements and scope control
- **HIPAA Security Rule:** Audit controls and evidence protection
- **Industry Standards:** Penetration testing methodologies (PTES, OWASP, NIST)

**Business Impact:**

- **Operational Disruption:** Uncontrolled audit activities can cause outages
- **Security Exposure:** Audit tools can introduce vulnerabilities if not controlled
- **Data Breach Risk:** Audit access to sensitive data requires protection
- **Legal Liability:** Audit evidence mishandling can compromise legal proceedings
- **Audit Failures:** Poor audit governance is itself an audit finding

## Who Should Complete This Assessment

**Primary Responsibility:** Internal Audit Manager / IT Security Manager

**Required Knowledge:**

- [Organisation]'s complete audit program and schedule
- Penetration testing and vulnerability assessment practices
- Audit tool inventory and authorisation processes
- Access control mechanisms for audit activities
- Evidence handling and retention procedures

**Support Roles:**

- **External Audit Firms:** For third-party audit activity details
- **Penetration Testing Teams:** For technical testing details
- **IT Operations:** For system protection mechanisms
- **Legal Counsel:** For evidence protection requirements
- **Compliance Team:** For regulatory requirement mapping

## Time Estimate

**Total Assessment Time:** 8-12 hours (depending on audit program complexity)

**Breakdown:**

- **Audit Activity Register (2-3 hours):** Document all planned and completed audits
- **Tool Authorisation Review (2-3 hours):** Assess audit tool governance
- **Access Control Assessment (1-2 hours):** Document auditor access management
- **Disruption Mitigation (1-2 hours):** Review system protection measures
- **Evidence Protection (1-2 hours):** Assess evidence handling procedures
- **Quality Review (1 hour):** Final validation and approval preparation

## Connection to Policy

This assessment implements **ISMS-POL-A.8.33-34, Section 2.2 (Audit Activity Management)** which defines mandatory requirements for:

- **Audit Planning:** All audit activities must be planned and authorised
- **Tool Control:** Audit tools must be approved before use
- **Access Management:** Auditor access must be controlled and logged
- **System Protection:** Production systems must be protected during testing
- **Evidence Handling:** Audit evidence must be securely managed

**Policy Authority:** Chief Information Security Officer (CISO) / Chief Audit Executive (CAE)
**Compliance Status:** Mandatory for all audit and assurance activities

---

# Prerequisites

## Access Required

Before starting this assessment, ensure you have access to:

**Documentation:**

- [ ] Audit program and annual audit plan
- [ ] Penetration testing reports and scoping documents
- [ ] Audit tool inventory and approval records
- [ ] Auditor access request forms and logs
- [ ] Incident reports related to audit activities
- [ ] Evidence retention policies

**Systems:**

- [ ] Audit management platform
- [ ] Access control systems
- [ ] Security testing tools inventory
- [ ] Evidence repository
- [ ] Change management system (for audit-related changes)

**Subject Matter Experts:**

- [ ] Internal Audit Team (for audit program details)
- [ ] Penetration Testing Teams (for testing methodology)
- [ ] IT Operations (for system protection measures)
- [ ] Legal Counsel (for evidence handling requirements)

## Pre-Assessment Checklist

Complete these tasks before beginning the assessment:

- [ ] **Gather annual audit plan** and schedule
- [ ] **Collect penetration testing** scoping documents and reports
- [ ] **Review audit tool inventory** and authorisation records
- [ ] **Document auditor access** request and approval processes
- [ ] **Identify any audit-related incidents** in last 12 months
- [ ] **Review evidence retention** policies and storage
- [ ] **Collect disruption mitigation** plans for critical systems
- [ ] **Identify all third-party audit firms** engaged

---

# Assessment Workflow

## Workflow Overview

```
Step 1: Audit Activity Register (Sheet 2)
   |
Step 2: Audit Tool Authorisation (Sheet 3)
   |
Step 3: Audit Access Tracking (Sheet 4)
   |
Step 4: Disruption Mitigation Plans (Sheet 5)
   |
Step 5: Audit Evidence Protection (Sheet 6)
   |
Step 6: Evidence Collection (Sheet 8)
   |
Step 7: Review Summary Dashboard (Sheet 7)
   |
Step 8: Quality Check & Approval (Sheet 9)
```

## Step-by-Step Instructions

### Step 1: Audit Activity Register (Sheet 2)

**Objective:** Document all planned and completed audit activities

**Instructions:**
1. List all audit activities in Column A (e.g., "Annual IT Audit", "Q2 Penetration Test", "SOC 2 Type II")
2. Classify Audit Type in Column B (Internal, External, Regulatory, Penetration Test, Vulnerability Assessment)
3. Document Audit Scope in Column C (systems, processes, or areas covered)
4. Record Audit Firm/Team in Column D (who conducts the audit)
5. Specify Planned Start Date in Column E
6. Specify Planned End Date in Column F
7. Document Actual Start/End in Columns G-H
8. Assign Audit Status in Column I (Planned, In Progress, Completed, Cancelled)
9. Record Management Approval Status in Column J
10. Document Systems in Scope in Column K

**Audit Types to Include:**

- Internal IT audits and control assessments
- External financial audits (IT components)
- SOC 2 / SOC 1 audits
- Penetration testing (external, internal, web application)
- Vulnerability assessments
- Red team exercises
- Compliance audits (PCI-DSS, HIPAA, GDPR)
- Regulatory examinations

**Quality Check:**

- Are ALL planned audit activities documented?
- Is every audit authorised by management?
- Are audit scopes clearly defined?
- Are start/end dates accurate?

### Step 2: Audit Tool Authorisation (Sheet 3)

**Objective:** Track authorisation and control of audit testing tools

**Instructions:**
1. List all audit tools in Column A (e.g., "Nessus", "Burp Suite", "Nmap", "Metasploit")
2. Classify Tool Category in Column B (Vulnerability Scanner, Penetration Tool, Network Analyzer, Forensic Tool)
3. Document Tool Owner in Column C (who is responsible for the tool)
4. Record Authorisation Status in Column D (Authorised, Pending, Unauthorised, Prohibited)
5. Specify Authorised Use Cases in Column E (what the tool may be used for)
6. Document Version/Configuration in Column F
7. Record Last Security Review in Column G
8. Identify Risk Level in Column H (High, Medium, Low)
9. Document Required Approvals in Column I
10. Specify Storage Location in Column J

**Tool Categories:**

- **Vulnerability Scanners:** Nessus, Qualys, OpenVAS, Rapid7
- **Penetration Tools:** Burp Suite, Metasploit, Cobalt Strike, Kali Linux tools
- **Network Analyzers:** Wireshark, tcpdump, Nmap
- **Web Application Tools:** OWASP ZAP, SQLmap, Nikto
- **Forensic Tools:** EnCase, FTK, Autopsy
- **Credential Testing:** John the Ripper, Hashcat, Hydra

**Authorisation Requirements:**

- Tool purpose and use cases defined
- Security review of tool completed
- Approved storage and access controls
- Usage logging requirements defined
- Incident response procedures documented

**Quality Check:**

- Are ALL audit tools in use documented?
- Is every tool properly authorised?
- Are high-risk tools subject to additional controls?
- Are tool versions and configurations current?

### Step 3: Audit Access Tracking (Sheet 4)

**Objective:** Document and control auditor access to systems and data

**Instructions:**
1. List all auditor access grants in Column A (unique access ID)
2. Identify Auditor/Team in Column B
3. Document Associated Audit in Column C (reference to Audit Register)
4. Specify Access Type in Column D (Read-Only, Read-Write, Admin, Physical)
5. Document Systems Accessed in Column E
6. Record Data Classification Accessed in Column F
7. Specify Access Start Date in Column G
8. Specify Access End Date in Column H
9. Document Actual Access Revocation in Column I
10. Record Access Approval in Column J (who approved)
11. Document Access Logging Status in Column K
12. Verify NDA/Confidentiality in Column L

**Access Control Principles:**

- **Least Privilege:** Only access needed for audit scope
- **Time-Limited:** Access expires at audit completion
- **Logged:** All access activities recorded
- **Supervised:** Sensitive access may require escort
- **Revocable:** Access can be immediately terminated

**Access Types:**

- **Read-Only:** View data and configurations only
- **Read-Write:** Modify test data or configurations
- **Administrative:** Full system access (rare, high risk)
- **Physical:** On-site access to facilities/hardware
- **Temporary Admin:** Elevated privileges for specific tests

**Quality Check:**

- Is every auditor access grant documented?
- Are all access grants properly authorised?
- Is access revoked promptly after audit completion?
- Are access activities logged?

### Step 4: Disruption Mitigation Plans (Sheet 5)

**Objective:** Document protection measures for production systems during audit testing

**Instructions:**
1. List critical systems requiring protection in Column A
2. Document System Criticality in Column B (Critical, High, Medium, Low)
3. Identify Associated Audits in Column C (which audits may affect this system)
4. Specify Mitigation Strategy in Column D
5. Document Testing Restrictions in Column E (what cannot be tested)
6. Record Backup/Recovery Plan in Column F
7. Specify Testing Window in Column G (allowed times for testing)
8. Document Rollback Procedures in Column H
9. Assign Mitigation Owner in Column I
10. Record Last Mitigation Test in Column J
11. Document Escalation Contacts in Column K

**Mitigation Strategies:**

- **Staging Environment Testing:** Test in non-production first
- **Off-Hours Testing:** Test during maintenance windows
- **Rate Limiting:** Restrict testing intensity
- **Scope Exclusion:** Exclude from certain test types
- **Enhanced Monitoring:** Increased monitoring during testing
- **Standby Recovery:** Recovery team on standby
- **Read-Only Testing:** No modification allowed

**Testing Restrictions Examples:**

- No denial-of-service testing on production
- No data modification on financial systems
- No credential brute-forcing on authentication systems
- No social engineering against executives
- No physical intrusion testing without escort

**Quality Check:**

- Are ALL critical systems covered?
- Are mitigation strategies appropriate to criticality?
- Are testing windows defined?
- Are rollback procedures documented and tested?

### Step 5: Audit Evidence Protection (Sheet 6)

**Objective:** Document secure handling and retention of audit evidence

**Instructions:**
1. List evidence categories in Column A (e.g., "Penetration Test Reports", "Audit Workpapers")
2. Classify Evidence Sensitivity in Column B (Confidential, Restricted, Internal)
3. Document Storage Location in Column C
4. Specify Access Controls in Column D (who can access)
5. Record Encryption Status in Column E (Encrypted at Rest, In Transit, Both, None)
6. Document Retention Period in Column F
7. Specify Destruction Method in Column G
8. Record Chain of Custody Requirements in Column H
9. Document Legal Hold Status in Column I
10. Identify Evidence Owner in Column J

**Evidence Categories:**

- **Audit Reports:** Final audit findings and recommendations
- **Workpapers:** Supporting documentation for findings
- **Penetration Test Results:** Technical vulnerability data
- **System Configurations:** Captured during audit
- **Access Logs:** Records of auditor activity
- **Interview Notes:** Documented conversations
- **Screenshots/Recordings:** Visual evidence

**Protection Requirements:**

- **Confidentiality:** Encrypt sensitive evidence
- **Integrity:** Hash evidence for tamper detection
- **Availability:** Accessible for follow-up audits
- **Chain of Custody:** Track evidence handling
- **Legal Hold:** Preserve if litigation anticipated

**Quality Check:**

- Is ALL audit evidence categorized?
- Are sensitive materials encrypted?
- Are retention periods defined?
- Is destruction method appropriate?

### Step 6: Evidence Collection (Sheet 8)

**Objective:** Link supporting documentation to assessment findings

**Instructions:**
1. For each finding or control, create evidence entry
2. Evidence Register auto-generates Evidence ID (EV-001, EV-002, etc.)
3. Document Evidence Type, Location, Retention Period
4. Reference Evidence ID in assessment sheets

**Evidence Types:**

- **Policy Documents:** Audit policies, testing procedures
- **Authorisation Records:** Audit approvals, tool authorisations
- **Access Records:** Access request forms, access logs
- **Mitigation Plans:** System protection documentation
- **Audit Reports:** Completed audit deliverables
- **Incident Reports:** Any audit-related incidents

### Step 7: Review Summary Dashboard (Sheet 7)

**Objective:** Validate overall compliance metrics and identify critical gaps

**The Summary Dashboard auto-calculates:**

- Overall audit governance compliance percentage
- Count of authorised vs. unauthorised audits/tools
- Critical gaps requiring immediate attention
- Access control compliance status
- Evidence protection status
- Upcoming audit activities

### Step 8: Quality Check & Approval (Sheet 9)

**Objective:** Final validation and approval workflow

**Self-Check Before Submitting for Approval:**

- [ ] All audit activities documented
- [ ] All audit tools authorised
- [ ] All auditor access tracked
- [ ] Disruption mitigation plans in place
- [ ] Evidence protection measures documented
- [ ] Evidence register populated
- [ ] Status indicators accurate
- [ ] Gaps and remediation plans documented

**Approval Workflow:**
1. **Level 1: Technical** - IT Security Manager validates accuracy
2. **Level 2: Audit** - CAE/Internal Audit Manager approves
3. **Level 3: Executive** - CISO confirms overall governance

---

# Question-by-Question Guidance

## Audit Activity Register (Sheet 2)

**Q: Should we include informal security assessments?**
A: Yes, document any activity that involves testing production systems or accessing sensitive data for assurance purposes.

**Q: What about continuous monitoring vs. point-in-time audits?**
A: Document continuous monitoring programs as ongoing activities with annual review cycles.

**Q: How do we handle multi-phase audits?**
A: Document as single audit entry with overall scope, or separate entries for distinct phases if they have different scopes/teams.

## Audit Tool Authorisation (Sheet 3)

**Q: What about built-in OS tools like ping, traceroute?**
A: Document only tools that could cause harm or access sensitive data. Standard diagnostic tools typically don't need authorisation.

**Q: Who authorises audit tools?**
A: IT Security should authorise tools based on risk assessment. High-risk tools (exploitation frameworks) may require CISO approval.

**Q: What about auditor-provided tools?**
A: External auditors must submit tools for review before use. Document in authorisation register with "External Auditor" as requestor.

## Audit Access Tracking (Sheet 4)

**Q: How quickly should access be revoked after audit completion?**
A: Within 24-48 hours of audit completion. Critical/admin access should be revoked same day.

**Q: Should we track physical access separately?**
A: Yes, document physical facility access in the same register with access type "Physical."

**Q: What about remote access for external auditors?**
A: Document VPN/remote access grants with start/end dates, and ensure multi-factor authentication is required.

## Disruption Mitigation (Sheet 5)

**Q: What systems need mitigation plans?**
A: At minimum: all production systems classified as Critical or High, all systems processing sensitive data, and any systems with limited redundancy.

**Q: What if auditor causes an outage?**
A: Activate incident response, notify audit sponsor, implement rollback. Document in incident register and lessons learned.

---

# Evidence Collection

## What Evidence to Collect

**Audit Activity Register:**

- Annual audit plan and schedule
- Audit engagement letters
- Management authorisation emails
- Audit completion reports

**Tool Authorisation:**

- Tool authorisation request forms
- Tool security assessments
- Configuration documentation
- Usage policies

**Access Tracking:**

- Access request forms
- Approval records
- Access logs
- Access revocation confirmations

**Disruption Mitigation:**

- System criticality assessments
- Mitigation plan documents
- Testing window agreements
- Rollback procedure documents

**Evidence Protection:**

- Evidence handling procedures
- Encryption configurations
- Retention schedules
- Destruction certificates

## Audit-Readiness Tips

**What Auditors Will Look For:**
1. **Authorisation:** Is every audit activity authorised?
2. **Tool Control:** Are audit tools properly governed?
3. **Access Management:** Is auditor access controlled and logged?
4. **System Protection:** Are production systems protected during testing?
5. **Evidence Integrity:** Is audit evidence securely managed?

**Common Audit Findings (And How to Avoid Them):**

- "Unauthorised penetration testing" - Implement authorisation workflow
- "Audit tools not inventoried" - Complete tool authorisation register
- "Auditor access not revoked" - Implement automatic expiration
- "No disruption mitigation for critical systems" - Document protection plans
- "Audit evidence not encrypted" - Implement encryption requirements

---

**END OF USER GUIDE**

---

*"An audit is only as credible as the independence of those conducting it."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
