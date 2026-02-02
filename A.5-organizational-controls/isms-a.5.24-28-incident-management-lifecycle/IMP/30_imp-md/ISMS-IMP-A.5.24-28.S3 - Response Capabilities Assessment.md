# ISMS-IMP-A.5.24-28.S3 — Incident Response Capabilities Assessment

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Incident Response Capabilities Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S3 |
| **Assessment Domain** | Domain 3 - Response Capabilities (A.5.26 Focus) |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Related Reference** | ISMS-REF-A.5.24-28 (Incident Response Reference Guide) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | CSIRT Manager / Incident Response Lead |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CSIRT Manager | Initial response capabilities assessment specification |

**Review Cycle**: Annual (or after major incident response activities)  
**Next Review Date**: [Effective Date + 12 months]  

**Related Documents**: 
- ISMS-POL-A.5.24-28 (Incident Management Lifecycle Policy)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide)
- ISMS-IMP-A.5.24-28.S1 (Framework & Governance Assessment)
- ISMS-IMP-A.5.24-28.S2 (Detection & Classification Assessment)
- ISMS-IMP-A.5.24-28.S4 (Forensic Evidence Assessment)
- ISMS-IMP-A.5.24-28.S5 (Learning & Improvement Assessment)
- ISMS-IMP-A.5.29-30 (BC/DR Framework)
- ISO/IEC 27002:2022 Control A.5.26
- NIST SP 800-61 Rev. 2 Section 3.3 (Containment, Eradication, and Recovery)

---

# PART I: USER COMPLETION GUIDE

## 1. Assessment Overview

### 1.1 Purpose

This assessment evaluates [Organization]'s **incident response execution capabilities**, focusing on the **response and recovery** phase of incident management (A.5.26).

**What This Assessment Covers:**
- Containment procedures and technical capabilities
- Eradication and remediation processes
- Recovery and restoration procedures
- Communication during active incidents
- Coordination with internal/external parties
- Response time metrics and SLA compliance
- Resource availability (people, tools, authority)
- Response playbook execution effectiveness

**What This Assessment Does NOT Cover:**
- Incident management governance (see S1 - Framework Assessment)
- Detection and classification (see S2 - Detection Assessment)
- Forensic evidence collection procedures (see S4 - Forensic Assessment)
- Post-incident learning (see S5 - Learning Assessment)

**Assessment Output:**
- Excel workbook documenting response capability maturity
- Containment effectiveness assessment
- Recovery time metrics (MTTR, MTTT, MTTC)
- Communication effectiveness evaluation
- Response playbook quality assessment
- Resource adequacy analysis
- Gap analysis and capability improvements

### 1.2 Why This Matters

**ISO/IEC 27001:2022 Control A.5.26 Requirement:**
> *"Information security incidents should be responded to in accordance with documented procedures."*

**NIST SP 800-61 Guidance:**
> *"Containment, Eradication, and Recovery: During this phase, the incident is contained, the threat is eradicated from the environment, and affected systems are recovered to normal operations."*

**Business Impact of Poor Response:**
- **Extended Dwell Time:** Slow containment allows attackers to persist and spread
- **Data Loss:** Incomplete eradication enables continued exfiltration
- **Business Disruption:** Ineffective recovery prolongs downtime
- **Reputational Damage:** Poor crisis communication erodes stakeholder trust
- **Regulatory Penalties:** Delayed response fails to meet notification deadlines
- **Recurring Incidents:** Incomplete remediation causes incident recurrence

**This Assessment Addresses:**
- Can we contain incidents quickly and effectively?
- Do we have procedures for eradication and recovery?
- Can we communicate effectively during crisis?
- Do we have adequate resources for response?
- Are our response playbooks effective?
- Do we meet response time SLAs?

### 1.3 Who Should Complete This Assessment

**Primary Responsibility:** CSIRT Manager, Incident Response Lead, or Senior Incident Responder

**Required Knowledge:**
- [Organization]'s incident response procedures (containment, eradication, recovery)
- Response playbook execution and effectiveness
- Communication protocols during incidents
- Resource availability (staffing, tools, authority)
- Response time metrics and SLA tracking
- Coordination with IT Operations, Legal, Management

**Support Roles:**
- **CSIRT Members:** Hands-on response experience, playbook execution
- **IT Operations:** System isolation, patching, recovery capabilities
- **Network Team:** Network segmentation, traffic blocking, isolation
- **Legal/Compliance:** Communication approval, regulatory notification
- **Management:** Authority for business decisions, resource allocation
- **External Partners:** Incident response retainers, MSSPs, forensic firms

**Collaboration Required:**
- This is NOT a solo assessment
- Requires input from responders (frontline experience)
- Requires metrics data (MTTR, MTTC, response times)
- Review sessions with CSIRT and IT Operations

### 1.4 Time Estimate

**Total Assessment Time:** 8-12 hours (depending on incident response maturity)

**Breakdown:**
- **Information Gathering:** 2-3 hours
  - Review response procedures and playbooks
  - Extract response metrics (MTTR, MTTC, response times)
  - Collect incident tickets (recent 6 months for case studies)
  - Interview CSIRT members on response effectiveness
  
- **Assessment Completion:** 3-4 hours
  - Complete containment capability assessment
  - Document eradication and recovery processes
  - Assess communication effectiveness
  - Evaluate resource adequacy
  
- **Playbook Review:** 2-3 hours
  - Review playbook completeness
  - Assess playbook execution quality
  - Identify playbook gaps
  
- **Gap Analysis:** 1-2 hours
  - Identify response capability gaps
  - Prioritize improvements
  - Develop remediation recommendations

**Complexity Factors:**
- **Simple (8 hours):** Mature CSIRT, documented playbooks, good metrics
- **Moderate (10 hours):** Growing capability, some playbook gaps, basic metrics
- **Complex (12+ hours):** Immature response, limited playbooks, poor metrics tracking

### 1.5 Connection to Policy

This assessment implements **ISMS-POL-A.5.24-28, Section 2.3 (Incident Response & Recovery)** which defines mandatory requirements for:

**Containment Requirements:**
- Documented containment procedures for each incident category
- Technical capabilities for isolation (network, endpoint, account)
- Maximum containment time SLAs (15 min Critical, 1 hour High, 4 hours Medium)
- Coordination with IT Operations for containment actions
- Authority matrix for containment decisions (who can authorize system shutdown, network segmentation)

**Eradication Requirements:**
- Malware removal and system cleaning procedures
- Vulnerability remediation processes
- Account and credential rotation procedures
- Threat actor expulsion verification
- Re-infection prevention measures

**Recovery Requirements:**
- System restoration and validation procedures
- Data recovery from backups (if needed)
- Service resumption processes
- Post-recovery monitoring (detection of reinfection)
- Integration with BC/DR plans (A.5.29-30)

**Communication Requirements:**
- Internal communication protocols (management, affected users, IT teams)
- External communication procedures (customers, regulators, media)
- Communication approval workflows (Legal, PR)
- Crisis communication templates
- Communication timeliness SLAs

**Resource Requirements:**
- 24/7 CSIRT availability (on-call rotation minimum)
- Access to containment/remediation tools
- Authority to make emergency decisions
- Budget for incident response (external support, forensics)

**Policy Authority:** Chief Information Security Officer (CISO)  
**Compliance Status:** Mandatory for all [Organization] security incidents

### 1.6 Assessment Scope

**Included in This Assessment:**

✅ **Containment Capabilities:**
- Network isolation procedures (VLAN, firewall rules, routing)
- Endpoint isolation (EDR, network quarantine)
- Account suspension/disablement
- Application/service shutdown
- Containment decision authority
- Containment time metrics (MTTC)

✅ **Eradication & Remediation:**
- Malware removal procedures
- Vulnerability patching processes
- Credential rotation workflows
- Threat actor expulsion verification
- Root cause remediation

✅ **Recovery & Restoration:**
- System restoration procedures
- Backup recovery processes
- Service resumption validation
- Post-recovery monitoring
- Recovery time metrics (MTTR)

✅ **Communication:**
- Internal communication effectiveness
- External communication preparedness
- Communication timeliness
- Stakeholder satisfaction with communication

✅ **Resource Availability:**
- CSIRT availability (coverage, on-call)
- Tool access and capabilities
- Authority for emergency decisions
- Budget for incident response

**Excluded from This Assessment:**

❌ CSIRT organizational structure (see S1)
❌ Detection and triage (see S2)
❌ Forensic evidence collection (see S4)
❌ Post-incident review (see S5)

### 1.7 Prerequisites

**Before Starting This Assessment:**

1. ✅ **Read Related Documents:**
   - ISMS-POL-A.5.24-28 Section 2.3 (Response & Recovery Requirements)
   - ISMS-REF-A.5.24-28 Section 3 (Forensic Collection - for evidence preservation during response)

2. ✅ **Gather Documentation:**
   - Containment procedures by incident type
   - Eradication and remediation playbooks
   - Recovery and restoration procedures
   - Communication templates and workflows
   - Authority matrix (who can authorize containment actions)

3. ✅ **Extract Metrics (Last 6 Months):**
   - Mean Time to Contain (MTTC)
   - Mean Time to Remediate (MTTR)
   - Response SLA compliance rates
   - Incidents by response outcome (contained, escalated, recurring)
   - Communication timeliness metrics

4. ✅ **Identify Stakeholders:**
   - CSIRT Manager (primary assessor)
   - Incident Responders (hands-on experience)
   - IT Operations (containment execution)
   - Network Team (network isolation)
   - Legal/Compliance (communication approval)

5. ✅ **Prepare Evidence Folder:**
   - Create folder: `/Evidence/A.5.24-28/S3_Response/`
   - Collect: Response playbooks, containment evidence, communication examples, metrics reports

---

## 2. Assessment Workflow

### 2.1 High-Level Process

```
1. Containment Assessment (2-3 hours)
   ├── Review containment procedures
   ├── Assess technical capabilities
   ├── Evaluate containment authority
   └── Analyze containment time metrics

2. Eradication & Remediation Assessment (2 hours)
   ├── Review eradication procedures
   ├── Assess vulnerability remediation processes
   ├── Evaluate credential rotation workflows
   └── Assess re-infection prevention

3. Recovery Assessment (2 hours)
   ├── Review recovery procedures
   ├── Assess backup/restore capabilities
   ├── Evaluate service resumption processes
   └── Analyze recovery time metrics

4. Communication Assessment (1-2 hours)
   ├── Review communication protocols
   ├── Assess communication timeliness
   ├── Evaluate stakeholder satisfaction
   └── Review communication templates

5. Resource Assessment (1 hour)
   ├── Assess CSIRT availability
   ├── Evaluate tool access
   ├── Review decision authority
   └── Assess budget adequacy

6. Gap Analysis (1 hour)
   ├── Identify capability gaps
   ├── Prioritize improvements
   └── Develop recommendations
```

### 2.2 Assessment Sections Overview

**Sheet 1: Instructions & Legend**
**Sheet 2: Containment Capabilities** (30 questions)
**Sheet 3: Eradication & Remediation** (20 questions)
**Sheet 4: Recovery & Restoration** (20 questions)
**Sheet 5: Communication** (20 questions)
**Sheet 6: Resources & Authority** (20 questions)
**Sheet 7: Playbook Effectiveness** (15 questions)
**Sheet 8: Gap Analysis** (40 gap capacity)
**Sheet 9: Evidence Register** (60 evidence capacity)
**Sheet 10: Dashboard** (Response effectiveness summary)
**Sheet 11: Approval Sign-Off**

---

## 3. Section-by-Section Guidance

### 3.1 Sheet 2: Containment Capabilities (30 Questions)

**Purpose:** Assess ability to contain incidents quickly and effectively

---

#### **Section A: Network Containment (Q1-Q8)**

**Q1: Network_Isolation_Capability**
- **Question:** Can [Organization] isolate network segments to contain incidents?
- **Dropdown:** Yes - Automated / Yes - Manual / Limited / No
- **Automated:** SOAR or network automation (VLAN changes, firewall rules)
- **Manual:** Network engineer executes changes
- **Evidence:** Network segmentation diagram, isolation procedure

**Q2: Firewall_Rule_Emergency_Changes**
- **Question:** Can firewall rules be changed on emergency basis to block threats?
- **Dropdown:** Yes - 24/7 / Yes - Business Hours Only / No
- **Best Practice:** 24/7 capability for Critical/High incidents
- **Authority:** Who can authorize emergency firewall changes?

**Q3: Internet_Egress_Blocking**
- **Question:** Can internet egress be blocked for infected systems?
- **Dropdown:** Yes - Per System / Yes - Per Subnet / No
- **Use Case:** Block C2 communication, prevent exfiltration

**Q4: VLAN_Quarantine**
- **Question:** Is there a quarantine VLAN for isolated systems?
- **Dropdown:** Yes / No
- **Purpose:** Move infected systems to isolated VLAN (no production access, monitored)

**Q5: Network_Containment_Time**
- **Question:** What is average time to execute network containment? (MTTC - Network)
- **Format:** Duration (e.g., "15 minutes", "1 hour")
- **Target:** <15 min for Critical, <1 hour for High
- **Evidence:** Incident tickets with containment timestamps

**Q6: Network_Containment_Authority**
- **Question:** Who has authority to order network containment (e.g., block IP, isolate segment)?
- **Format:** Free text (Role/Title)
- **Examples:** CSIRT Manager, SOC Lead, Network Manager, CISO
- **Risk if Unclear:** Delays during incident while seeking approval

**Q7: Network_Containment_Procedure**
- **Question:** Are network containment procedures documented?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No
- **Comprehensive:** Step-by-step procedures, decision trees, contact lists

**Q8: Network_Team_Availability**
- **Question:** Is network team available 24/7 for emergency containment?
- **Dropdown:** Yes - 24/7 / On-Call / Business Hours Only / No
- **Gap if "Business Hours Only":** MEDIUM - After-hours incidents delayed

---

#### **Section B: Endpoint Containment (Q9-Q15)**

**Q9: EDR_Isolation_Capability**
- **Question:** Can endpoints be isolated remotely via EDR/XDR?
- **Dropdown:** Yes - Automated / Yes - Manual / No EDR / No
- **Automated:** SOAR triggers EDR isolation
- **Manual:** Analyst clicks "Isolate" in EDR console

**Q10: EDR_Isolation_Speed**
- **Question:** How quickly can endpoint isolation be executed?
- **Format:** Duration
- **Target:** <5 minutes (near-instant via EDR)
- **Evidence:** EDR isolation logs, timestamps

**Q11: Network_Quarantine_Non_EDR**
- **Question:** Can endpoints without EDR be isolated (e.g., via 802.1X, DHCP, switch port disable)?
- **Dropdown:** Yes / No
- **Use Case:** Legacy systems, IoT devices without EDR agent

**Q12: Endpoint_Containment_Scope**
- **Question:** What percentage of endpoints can be remotely isolated?
- **Format:** Percentage (0-100%)
- **Target:** >95%
- **Gap if <90%:** HIGH - Incomplete containment capability

**Q13: Laptop_Remote_Isolation**
- **Question:** Can remote laptops (VPN, off-network) be isolated?
- **Dropdown:** Yes - EDR / Yes - VPN Disconnect / Limited / No
- **Challenge:** Laptops not on corporate network

**Q14: Server_Containment**
- **Question:** Can production servers be isolated during incidents?
- **Dropdown:** Yes - With Business Approval / Yes - Emergency Authority / No
- **Trade-off:** Server isolation causes service disruption

**Q15: Endpoint_Containment_Reversal**
- **Question:** Is there a documented process for reversing endpoint isolation (un-quarantine)?
- **Dropdown:** Yes / No
- **Risk if "No":** Systems stuck in isolation after remediation

---

#### **Section C: Account & Identity Containment (Q16-Q22)**

**Q16: Account_Suspension_Capability**
- **Question:** Can compromised accounts be suspended/disabled immediately?
- **Dropdown:** Yes - Automated / Yes - Manual (Minutes) / Manual (Hours) / No
- **Automated:** SOAR → Active Directory API → Disable account
- **Manual:** AD admin disables account

**Q17: Account_Suspension_Authority**
- **Question:** Who has authority to suspend user accounts during incidents?
- **Format:** Free text
- **Examples:** CSIRT Manager, Security Analyst, IT Manager, CISO
- **Best Practice:** CSIRT can suspend, revoke later if false positive

**Q18: MFA_Token_Revocation**
- **Question:** Can MFA tokens/sessions be revoked for compromised accounts?
- **Dropdown:** Yes / No
- **Purpose:** Force re-authentication even if password unchanged

**Q19: Service_Account_Rotation**
- **Question:** Can service account credentials be rotated during incidents?
- **Dropdown:** Yes - Automated / Yes - Manual / No
- **Challenge:** Service accounts often hard-coded in applications

**Q20: Password_Force_Reset**
- **Question:** Can [Organization] force password reset for affected users?
- **Dropdown:** Yes - Immediate / Yes - Next Login / No
- **Use Case:** Credential compromise incidents

**Q21: Privileged_Access_Revocation**
- **Question:** Can privileged access (admin rights) be revoked during incidents?
- **Dropdown:** Yes - Immediately / Yes - Delayed / No

**Q22: Account_Containment_Time**
- **Question:** What is average time to suspend compromised account? (MTTC - Account)
- **Format:** Duration
- **Target:** <15 minutes

---

#### **Section D: Application & Service Containment (Q23-Q27)**

**Q23: Application_Shutdown_Authority**
- **Question:** Who has authority to shut down applications/services during incidents?
- **Format:** Free text
- **Trade-off:** Service shutdown causes business disruption vs. risk of continued compromise

**Q24: Service_Isolation_Capability**
- **Question:** Can individual services be isolated without full shutdown?
- **Dropdown:** Yes / Limited / No
- **Example:** Disable specific API endpoint, block specific URL path

**Q25: Database_Connection_Blocking**
- **Question:** Can database connections be blocked during SQL injection incidents?
- **Dropdown:** Yes - Per Application / Yes - Global / No

**Q26: Web_Application_Firewall**
- **Question:** Can WAF rules be deployed on emergency basis to block attacks?
- **Dropdown:** Yes - Automated / Yes - Manual / No WAF

**Q27: Cloud_Service_Containment**
- **Question:** Can cloud services (SaaS, IaaS) be isolated during incidents?
- **Dropdown:** Yes / Limited / No Cloud / No
- **Examples:** Revoke API keys, disable cloud app access, isolate cloud VMs

---

#### **Section E: Containment Metrics (Q28-Q30)**

**Q28: MTTC_Overall**
- **Question:** What is Mean Time to Contain (MTTC) overall? (Last 6 months)
- **Format:** Duration
- **Benchmark:**
  - <1 hour: Excellent
  - 1-4 hours: Good
  - 4-24 hours: Fair
  - >24 hours: Poor
- **Evidence:** Incident tickets (containment timestamp - incident start)

**Q29: MTTC_Critical**
- **Question:** What is MTTC for Critical severity incidents?
- **Format:** Duration
- **Target:** <15 minutes (per ISMS-POL-A.5.24-28 SLA)

**Q30: Containment_SLA_Compliance**
- **Question:** What percentage of incidents meet containment SLA? (Last 6 months)
- **Format:** Percentage
- **Target:** >90%
- **Gap if <80%:** HIGH

---

### 3.2 Sheet 3: Eradication & Remediation (20 Questions)

**Purpose:** Assess eradication and root cause remediation

---

#### **Section A: Malware Eradication (Q31-Q36)**

**Q31: Malware_Removal_Procedure**
- **Question:** Are malware removal procedures documented?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No

**Q32: EDR_Malware_Removal**
- **Question:** Can EDR perform automated malware removal?
- **Dropdown:** Yes - Automated / Yes - Manual / No

**Q33: Reimaging_Capability**
- **Question:** Can compromised systems be reimaged quickly?
- **Dropdown:** Yes - Automated / Yes - Manual (Same Day) / Yes - Manual (Days) / No

**Q34: Malware_Persistence_Check**
- **Question:** Are persistence mechanisms checked and removed (registry, scheduled tasks, startup items)?
- **Dropdown:** Yes - Systematically / Sometimes / No

**Q35: Network_Share_Malware_Scan**
- **Question:** Are network shares scanned for malware after incidents?
- **Dropdown:** Yes - Automatically / Yes - Manually / No

**Q36: Malware_Sample_Collection**
- **Question:** Are malware samples collected for analysis before removal?
- **Dropdown:** Yes - Always / Sometimes / No
- **Purpose:** Threat intelligence, IOC generation

---

#### **Section B: Vulnerability Remediation (Q37-Q42)**

**Q37: Emergency_Patching_Capability**
- **Question:** Can critical patches be deployed on emergency basis?
- **Dropdown:** Yes - Same Day / Yes - Within Week / No

**Q38: Vulnerability_Remediation_Time**
- **Question:** What is average time to remediate vulnerabilities exploited in incidents?
- **Format:** Duration
- **Target:** <24 hours for Critical, <7 days for High

**Q39: Patch_Testing_Waiver**
- **Question:** Can patch testing be waived for emergency security patches?
- **Dropdown:** Yes - With Approval / No - Always Test

**Q40: Configuration_Hardening**
- **Question:** Are configuration weaknesses remediated after incidents?
- **Dropdown:** Yes - Systematically / Sometimes / No

**Q41: Code_Fix_Deployment**
- **Question:** (For web app vulnerabilities) Can code fixes be deployed on emergency basis?
- **Dropdown:** Yes - Same Day / Yes - Days / No / N/A

**Q42: Workaround_Implementation**
- **Question:** Can workarounds (WAF rules, firewall blocks) be implemented while patching?
- **Dropdown:** Yes / No

---

#### **Section C: Credential & Access Remediation (Q43-Q47)**

**Q43: Credential_Rotation_Procedure**
- **Question:** Are credential rotation procedures documented?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No

**Q44: Bulk_Password_Reset**
- **Question:** Can [Organization] perform bulk password reset for affected users?
- **Dropdown:** Yes / No

**Q45: Certificate_Revocation**
- **Question:** Can certificates be revoked and reissued after compromise?
- **Dropdown:** Yes / No

**Q46: API_Key_Rotation**
- **Question:** Can API keys be rotated after exposure?
- **Dropdown:** Yes - Automated / Yes - Manual / No

**Q47: Privileged_Account_Review**
- **Question:** Are privileged accounts reviewed and cleaned up after incidents?
- **Dropdown:** Yes - Systematically / Sometimes / No

---

#### **Section D: Threat Actor Expulsion (Q48-Q50)**

**Q48: Attacker_Expulsion_Verification**
- **Question:** Is threat actor expulsion verified before declaring incident resolved?
- **Dropdown:** Yes - Systematically / Sometimes / No
- **Verification:** No more C2 beaconing, no unauthorized access, no persistence

**Q49: Backdoor_Search**
- **Question:** Are backdoors searched for and removed?
- **Dropdown:** Yes - Comprehensive / Limited / No

**Q50: Re_infection_Prevention**
- **Question:** Are measures taken to prevent re-infection (blocking C2 IPs, monitoring for IOCs)?
- **Dropdown:** Yes / No

---

### 3.3 Sheet 4: Recovery & Restoration (20 Questions)

**Purpose:** Assess recovery and service restoration

---

#### **Section A: System Restoration (Q51-Q57)**

**Q51: Restoration_Procedure**
- **Question:** Are system restoration procedures documented?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No

**Q52: Backup_Availability**
- **Question:** Are backups available for critical systems?
- **Dropdown:** Yes - All Systems / Yes - Most / Limited / No
- **Cross-Reference:** ISMS-IMP-A.5.29-30 (BC/DR Assessment)

**Q53: Backup_Restoration_Time**
- **Question:** What is average time to restore system from backup?
- **Format:** Duration
- **Target:** <4 hours for Critical systems

**Q54: Backup_Integrity_Verification**
- **Question:** Are backups verified for integrity before restoration?
- **Dropdown:** Yes - Always / Sometimes / No
- **Risk if "No":** Restore corrupted/infected backup

**Q55: Clean_Rebuild_Capability**
- **Question:** Can systems be rebuilt from clean images?
- **Dropdown:** Yes / Limited / No

**Q56: Configuration_Restoration**
- **Question:** Are system configurations backed up and restorable?
- **Dropdown:** Yes / Partial / No

**Q57: Data_Recovery_Testing**
- **Question:** Is data recovery tested regularly (not just during incidents)?
- **Dropdown:** Yes - Quarterly / Yes - Annually / No
- **Best Practice:** Annual minimum

---

#### **Section B: Service Resumption (Q58-Q64)**

**Q58: Service_Resumption_Procedure**
- **Question:** Are service resumption procedures documented?
- **Dropdown:** Yes / No

**Q59: Post_Recovery_Validation**
- **Question:** Are services validated before declaring full recovery?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No
- **Validation:** Functionality testing, performance check, security scan

**Q60: Staged_Recovery**
- **Question:** Is staged recovery used (restore critical services first, then others)?
- **Dropdown:** Yes / No

**Q61: User_Communication_During_Recovery**
- **Question:** Are users informed during recovery process?
- **Dropdown:** Yes - Proactively / Yes - On Request / No

**Q62: Service_Degradation_Acceptable**
- **Question:** Can services run in degraded mode during recovery?
- **Dropdown:** Yes - Documented / Limited / No
- **Example:** Read-only mode, reduced capacity

**Q63: Recovery_Time_Objective**
- **Question:** Are Recovery Time Objectives (RTOs) defined for critical services?
- **Dropdown:** Yes / No
- **Cross-Reference:** ISMS-POL-A.5.29-30 (BC/DR)

**Q64: RTO_Compliance**
- **Question:** What percentage of incidents meet RTO? (Last 6 months)
- **Format:** Percentage
- **Target:** >90%

---

#### **Section C: Post-Recovery Monitoring (Q65-Q70)**

**Q65: Post_Recovery_Monitoring_Period**
- **Question:** Is there enhanced monitoring after recovery?
- **Dropdown:** Yes - 7+ Days / Yes - 1-3 Days / No

**Q66: Reinfection_Detection**
- **Question:** Is reinfection actively monitored for after recovery?
- **Dropdown:** Yes / No

**Q67: IOC_Monitoring**
- **Question:** Are IOCs from incident monitored after recovery?
- **Dropdown:** Yes / No

**Q68: MTTR_Overall**
- **Question:** What is Mean Time to Recover (MTTR) overall? (Last 6 months)
- **Format:** Duration
- **Benchmark:** <24 hours for most incidents

**Q69: MTTR_Critical**
- **Question:** What is MTTR for Critical incidents?
- **Format:** Duration
- **Target:** <4 hours

**Q70: Recovery_Success_Rate**
- **Question:** What percentage of incidents recover without recurrence? (Last 6 months)
- **Format:** Percentage
- **Target:** >95% (no reinfection/recurrence)

---

### 3.4 Sheet 5: Communication (20 Questions)

**Purpose:** Assess communication during incidents

---

#### **Section A: Internal Communication (Q71-Q77)**

**Q71: Internal_Communication_Protocol**
- **Question:** Is internal communication protocol documented?
- **Dropdown:** Yes / No

**Q72: Management_Notification_Timeliness**
- **Question:** Are management notifications sent within SLA? (Critical: 15 min, High: 1 hour)
- **Dropdown:** Yes - Always / Usually / No

**Q73: Affected_User_Notification**
- **Question:** Are affected users notified during incidents?
- **Dropdown:** Yes - Proactively / Yes - On Request / No

**Q74: IT_Ops_Coordination**
- **Question:** How is communication coordinated with IT Operations during incidents?
- **Dropdown:** Dedicated Channel / Email / Phone / Informal / No Process

**Q75: Communication_Templates**
- **Question:** Are communication templates available (management briefing, user notification)?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No

**Q76: Communication_Approval**
- **Question:** Is there an approval process for incident communications?
- **Dropdown:** Yes - Required / Optional / No

**Q77: Communication_Log**
- **Question:** Is all incident communication logged?
- **Dropdown:** Yes / No
- **Purpose:** Audit trail, post-incident review

---

#### **Section B: External Communication (Q78-Q84)**

**Q78: External_Communication_Procedure**
- **Question:** Are external communication procedures documented?
- **Dropdown:** Yes / No

**Q79: Customer_Notification_Capability**
- **Question:** Can customers be notified of incidents affecting them?
- **Dropdown:** Yes - Automated / Yes - Manual / No

**Q80: Regulatory_Notification_Preparedness**
- **Question:** Are regulatory notification templates ready (GDPR, PCI DSS, etc.)?
- **Dropdown:** Yes / No

**Q81: Media_Inquiry_Handling**
- **Question:** Is there a process for handling media inquiries during incidents?
- **Dropdown:** Yes - PR Team / Yes - Ad-Hoc / No

**Q82: Third_Party_Communication**
- **Question:** Are third parties (vendors, partners) notified when incidents affect them?
- **Dropdown:** Yes / No

**Q83: Legal_Review_Communication**
- **Question:** Does Legal review external communications before release?
- **Dropdown:** Yes - Always / Sometimes / No

**Q84: Communication_Timeliness_External**
- **Question:** Are external communications sent within required timelines (e.g., GDPR 72h)?
- **Dropdown:** Yes - Always / Usually / No

---

#### **Section C: Crisis Communication (Q85-Q90)**

**Q85: Crisis_Communication_Plan**
- **Question:** Is there a crisis communication plan?
- **Dropdown:** Yes / No

**Q86: Spokesperson_Designated**
- **Question:** Are designated spokespersons identified?
- **Dropdown:** Yes / No
- **Typical:** CISO (technical), CEO (business impact), PR (media)

**Q87: Communication_Frequency**
- **Question:** Is communication frequency defined during major incidents?
- **Dropdown:** Yes (e.g., hourly updates) / No

**Q88: Stakeholder_Satisfaction**
- **Question:** Are stakeholders generally satisfied with incident communication? (Based on feedback)
- **Dropdown:** Yes / Mixed / No / Not Measured

**Q89: Communication_Lessons_Learned**
- **Question:** Are communication lessons learned captured after incidents?
- **Dropdown:** Yes / No

**Q90: Communication_Training**
- **Question:** Do CSIRT members receive communication training?
- **Dropdown:** Yes / No

---

### 3.5 Sheet 6: Resources & Authority (20 Questions)

**Purpose:** Assess resource availability and decision authority

---

#### **Section A: CSIRT Availability (Q91-Q95)**

**Q91: CSIRT_24_7_Coverage**
- **Question:** Is CSIRT available 24/7 for incident response?
- **Dropdown:** Yes - Dedicated Staff / Yes - On-Call / Business Hours Only

**Q92: On_Call_Response_Time**
- **Question:** What is the on-call response SLA?
- **Format:** Duration (e.g., "15 minutes", "1 hour")
- **Target:** <15 min for Critical

**Q93: On_Call_Escalation**
- **Question:** Is there an on-call escalation process if primary responder unavailable?
- **Dropdown:** Yes / No

**Q94: Weekend_Holiday_Coverage**
- **Question:** Is CSIRT coverage maintained on weekends/holidays?
- **Dropdown:** Yes / Limited / No

**Q95: Surge_Capacity**
- **Question:** Can [Organization] scale response for multiple simultaneous incidents?
- **Dropdown:** Yes - External Support / Limited - Internal Only / No

---

#### **Section B: Tool Access (Q96-Q100)**

**Q96: After_Hours_Tool_Access**
- **Question:** Can CSIRT access all necessary tools after hours?
- **Dropdown:** Yes / Limited / No

**Q97: Remote_Response_Capability**
- **Question:** Can CSIRT respond to incidents remotely (from home)?
- **Dropdown:** Yes - Full Capability / Yes - Limited / No

**Q98: Emergency_System_Access**
- **Question:** Can CSIRT obtain emergency access to systems during incidents?
- **Dropdown:** Yes - Break-Glass / Yes - With Approval / No

**Q99: Third_Party_Tool_Access**
- **Question:** Do external partners (MSSP, forensics) have necessary tool access?
- **Dropdown:** Yes / Limited / No / N/A

**Q100: VPN_Capacity**
- **Question:** Is VPN capacity sufficient for mass remote work during incidents?
- **Dropdown:** Yes / Limited / No

---

#### **Section C: Decision Authority (Q101-Q105)**

**Q101: Emergency_Authority_Matrix**
- **Question:** Is emergency decision authority documented?
- **Dropdown:** Yes / No
- **Examples:** Who can shut down production, who can authorize emergency patching

**Q102: Business_Impact_Decisions**
- **Question:** Can CSIRT make business impact decisions (e.g., accept downtime for containment)?
- **Dropdown:** Yes - Full Authority / Yes - With Approval / No

**Q103: After_Hours_Authority**
- **Question:** Do on-call responders have authority to make critical decisions after hours?
- **Dropdown:** Yes / Limited / Must Escalate

**Q104: Spending_Authority**
- **Question:** Does CSIRT have spending authority for incident response (e.g., engage forensics)?
- **Dropdown:** Yes - Up to $X / Yes - With Approval / No

**Q105: Legal_Hold_Authority**
- **Question:** Can CSIRT initiate legal hold on systems/data?
- **Dropdown:** Yes / Yes - With Legal / No

---

#### **Section D: Budget & External Support (Q106-Q110)**

**Q106: IR_Budget_Allocated**
- **Question:** Is budget allocated for incident response?
- **Dropdown:** Yes - Dedicated / Yes - Part of IT Security / No

**Q107: External_IR_Retainer**
- **Question:** Does [Organization] have an incident response retainer (external firm)?
- **Dropdown:** Yes / No

**Q108: Forensic_Services_Available**
- **Question:** Can [Organization] engage forensic services on short notice?
- **Dropdown:** Yes - Retainer / Yes - Ad-Hoc / No

**Q109: Legal_Support_Available**
- **Question:** Is legal support available 24/7 for incident response?
- **Dropdown:** Yes / Business Hours Only / No

**Q110: Insurance_Cyber_Coverage**
- **Question:** Does [Organization] have cyber insurance covering incident response costs?
- **Dropdown:** Yes / No

---

### 3.6 Sheet 7: Playbook Effectiveness (15 Questions)

**Purpose:** Assess quality and effectiveness of response playbooks

---

**Q111: Playbook_Usage_Rate**
- **Question:** What percentage of incidents use documented playbooks?
- **Format:** Percentage
- **Target:** >80%

**Q112: Playbook_Completeness**
- **Question:** Are playbooks comprehensive (all steps documented)?
- **Dropdown:** Yes - Comprehensive / Partial / No

**Q113: Playbook_Accuracy**
- **Question:** Are playbooks accurate (steps work as documented)?
- **Dropdown:** Yes / Mostly / No

**Q114: Playbook_Update_After_Incident**
- **Question:** Are playbooks updated after incidents reveal gaps?
- **Dropdown:** Yes - Always / Sometimes / No

**Q115: Playbook_Accessibility**
- **Question:** Can responders easily access playbooks during incidents?
- **Dropdown:** Yes - Easily / With Difficulty / No

**Q116-Q120:** **Playbook Quality by Category (Top 5 incident types)**

For each:
- **Playbook Exists:** Yes / No
- **Playbook Quality:** Excellent / Good / Fair / Poor
- **Responder Feedback:** Helpful / Needs Improvement / Not Used

**Q121: Playbook_Training**
- **Question:** Are responders trained on playbook usage?
- **Dropdown:** Yes / No

**Q122: Playbook_Testing**
- **Question:** Are playbooks tested during exercises?
- **Dropdown:** Yes - Regularly / Occasionally / No

**Q123: Playbook_Automation**
- **Question:** What percentage of playbook steps are automated (SOAR)?
- **Format:** Percentage

**Q124: Playbook_Deviation_Tracking**
- **Question:** Are deviations from playbooks tracked and reviewed?
- **Dropdown:** Yes / No

**Q125: Playbook_Improvement_Process**
- **Question:** Is there a process for continuous playbook improvement?
- **Dropdown:** Yes / No

---

### 3.7 Sheets 8-11: Gap Analysis, Evidence, Dashboard, Approval

**(Similar structure to S1 and S2, adapted for response capabilities)**

---

## 4. Metrics Calculation Guide

### 4.1 Mean Time to Contain (MTTC)

**Formula:**
```
MTTC = Σ(Containment Timestamp - Incident Start Timestamp) / Number of Incidents
```

**Best Practice:** Track separately by severity (Critical, High, Medium, Low)

---

### 4.2 Mean Time to Remediate/Recover (MTTR)

**Formula:**
```
MTTR = Σ(Recovery Complete Timestamp - Incident Start Timestamp) / Number of Incidents
```

---

### 4.3 Response SLA Compliance

**Formula:**
```
SLA Compliance = (Incidents Meeting SLA / Total Incidents) × 100
```

---

## 5. Common Mistakes to Avoid

**❌ Mistake:** Focusing on documentation without validating actual capability
**✅ Solution:** Test containment capabilities through exercises

**❌ Mistake:** Assuming IT Ops will execute containment without clear authority
**✅ Solution:** Document emergency authority matrix, train IT Ops

**❌ Mistake:** No playbook updates after incidents
**✅ Solution:** Mandatory playbook review in post-incident process

**❌ Mistake:** Communication templates not approved in advance
**✅ Solution:** Pre-approve templates with Legal/PR before incidents

---

## 6. Assessment Timeline

**Week 1:** Containment + Eradication assessment (4-5 hours)
**Week 2:** Recovery + Communication assessment (4-5 hours)
**Week 3:** Resources + Playbooks + Gap analysis (4 hours)
**Week 4:** Evidence collection, quality review, approval (2-3 hours)

**Total:** 2-4 weeks (part-time)

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

Workbook Structure (11 Sheets)

Instructions & Legend
Containment Capabilities (30 Q)
Eradication & Remediation (20 Q)
Recovery & Restoration (20 Q)
Communication (20 Q)
Resources & Authority (20 Q)
Playbook Effectiveness (15 Q)
Gap Analysis (40 capacity)
Evidence Register (60 capacity)
Dashboard
Approval Sign-Off

Total Questions: 125
Key Metrics: MTTC, MTTR, SLA Compliance %, Playbook Usage Rate

**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

## Document Overview

**Document ID:** ISMS-IMP-A.5.24-28.S3
**Assessment Area:** Incident Response Capabilities (Containment, Eradication, Recovery, Communication, Resources, Playbooks)
**Related Policy:** ISMS-POL-A.5.24-28, Section 2.3 (A.5.26 – Response to Information Security Incidents)
**Purpose:** Evaluate operational readiness and execution effectiveness across all response phases, using metrics extracted from recent incidents and capability assessments per response domain

**Key Principle:** This assessment is **metric-driven**. Where possible, assessors extract MTTC, MTTE, and MTTR from the last 6 months of incident tickets rather than self-reporting estimates. Capability questions validate that the procedures and tools backing those metrics actually exist.

---

## Instructions for Completing This Assessment

### How to Use This Document

This technical specification defines the structure, validation rules, and formulas for the Response Capabilities Assessment Excel workbook (`ISMS-IMP-A.5.24-28.S3_Response_Capabilities_[DATE].xlsx`).

**Workbook Generation:** Python script `generate_a524_28_s3_response_capabilities.py` creates the workbook based on this specification.

**Assessment Completion Process:**

1. **Extract metrics first** — pull MTTC, MTTE, MTTR from your ticketing/SIEM system for the last 6 months before completing any assessment sheet
2. **Work through each section** — Containment → Eradication → Recovery → Communication → Resources → Playbooks
3. **Select the answer from each dropdown** that most accurately reflects current capability
4. **Enter durations** in the unit shown (minutes or hours as labelled)
5. **Enter percentages** as whole numbers (e.g., 85 for 85%)
6. **Provide evidence references** — ticket IDs, runbook locations, tool names, documentation paths
7. **Review the Gap_Identified column** — formulas flag gaps automatically; add detail in Comments where needed
8. **Complete Gap Analysis** — transfer flagged items, prioritise, assign owners
9. **Obtain approval** via the Approval Sign-Off sheet

### Status Legend

| Symbol | Meaning | Description |
|--------|---------|-------------|
| **✅** | **Compliant** | Capability fully operational, metrics within SLA |
| **⚠️** | **Partial** | Capability exists but gaps or SLA breaches present |
| **❌** | **Non-Compliant** | Capability missing or metrics significantly outside SLA |
| **N/A** | **Not Applicable** | Does not apply to this organisation's environment |

### Acceptable Evidence

- Incident ticket exports (last 6 months)
- Response playbook documents and version history
- EDR/SIEM tool configuration screenshots
- Network architecture diagrams showing segmentation
- Authority/escalation matrix documents
- Communication templates and approval records
- Tabletop or live exercise reports
- After-action / post-incident review reports
- Training completion records

---

## Sheet 1: Instructions & Legend

### Header Section
- **Title:** "ISMS-IMP-A.5.24-28.S3 — Incident Response Capabilities Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 – Control A.5.26: Response to Information Security Incidents"
- **Styling:** Dark blue header (#003366), white text, centred, row height 30

### Document Information Block
```plaintext
Document ID:           ISMS-IMP-A.5.24-28.S3
Assessment Area:       Response Capabilities
Related Policy:        ISMS-POL-A.5.24-28, Section 2.3
Version:               1.0
Assessment Date:       [USER INPUT – yellow cell]
Completed By:          [USER INPUT – yellow cell]
Organisation:          [USER INPUT – yellow cell]
Metrics Period:        [USER INPUT – yellow cell, e.g. "01.07.2025 – 31.12.2025"]
Review Cycle:          Annual (or after major incident)
```

### How to Use This Workbook
1. Extract response metrics from your ticketing system (6-month window) before starting
2. Complete Containment Capabilities sheet — network, endpoint, account, application layers
3. Complete Eradication & Remediation — malware removal, patching, root-cause identification
4. Complete Recovery & Restoration — backup restoration, service resumption, post-recovery monitoring
5. Complete Communication — internal coordination, external/customer notification, regulatory reporting
6. Complete Resources & Authority — budget, staffing, decision authority matrix
7. Complete Playbook Effectiveness — coverage, usage rates, update cadence
8. Review Dashboard for automated metric calculations and maturity scoring
9. Transfer gaps to Gap Analysis, prioritise, assign owners
10. Obtain approval via Approval Sign-Off

### Status Legend (rendered in workbook)

| Symbol | Status | Description | Colour Code |
|--------|--------|-------------|-------------|
| ✅ | Compliant | Capability operational, within SLA | Green (#C6EFCE) |
| ⚠️ | Partial | Capability exists, gaps present | Yellow (#FFEB9C) |
| ❌ | Non-Compliant | Capability missing or severely degraded | Red (#FFC7CE) |
| N/A | Not Applicable | Not relevant to this environment | Grey (#D9D9D9) |

---

## Sheet 2: Containment Capabilities (30 Questions)

### Purpose
Assess the organisation's ability to stop an active threat from spreading — network isolation, endpoint control, account suspension, and application-layer containment.

### Header
**Row 1:** "CONTAINMENT CAPABILITIES"
**Row 2:** "Network, Endpoint, Account, Application Containment (30 Questions)"

### Column Definitions

| Column | Header | Width | Type | Description |
|--------|--------|-------|------|-------------|
| A | Question_ID | 12 | Static | Q1–Q30, prefixed by section header rows |
| B | Section | 25 | Static | Network / Endpoint / Account / Application / Metrics |
| C | Question | 60 | Static | Assessment question text (wrap text enabled) |
| D | Answer | 25 | **User Input** (yellow) | Dropdown or free-text per question type |
| E | Evidence_Reference | 30 | **User Input** (yellow) | Ticket ID, tool name, document path |
| F | Comments | 35 | **User Input** (yellow) | Free text — context, caveats, planned improvements |
| G | Gap_Identified | 12 | Formula (green) | Auto-calculated — see formula below |

### Section Breakdown

**Network (Q1–Q8):** Network segment isolation, emergency firewall rules, internet egress blocking, quarantine VLAN, containment authority, 24/7 availability, average network containment time.

**Endpoint (Q9–Q15):** EDR-based remote isolation, isolation speed, non-EDR fallback, percentage of endpoints isolatable, laptop remote isolation, production server isolation authority, isolation reversal procedure.

**Account (Q16–Q22):** Compromised account suspension speed, suspension authority, MFA/session revocation, service account credential rotation, forced password reset, privileged access revocation, average account suspension time.

**Application (Q23–Q27):** Application shutdown authority, individual service isolation, database connection blocking, emergency WAF rule deployment, cloud service containment.

**Metrics (Q28–Q30):** Mean Time to Contain (MTTC) overall (6-month window), MTTC for Critical-severity incidents, percentage of incidents meeting containment SLA.

### Answer Type Reference (Sheet 2)

| Q-Range | Answer Types Used |
|---------|-------------------|
| Q1 | Dropdown: Automated / Manual / Limited / No |
| Q2 | Dropdown: 24/7 / Business Hours / No |
| Q3 | Dropdown: Per System / Per Subnet / No |
| Q4 | Dropdown: Yes / No |
| Q5 | Duration (minutes) — free text number |
| Q6 | Text — name/role of authority holder |
| Q7 | Dropdown: Comprehensive / Basic / No |
| Q8 | Dropdown: 24/7 / On-Call / Business Hours / No |
| Q9 | Dropdown: Automated / Manual / No EDR / No |
| Q10 | Duration (minutes) — free text number |
| Q11–Q15 | Yes/No or capability-specific dropdowns |
| Q16 | Dropdown: Automated / Manual (Min) / Manual (Hours) / No |
| Q17 | Text — name/role |
| Q18–Q21 | Yes / No or capability-specific |
| Q22 | Duration (minutes) |
| Q23 | Text — name/role |
| Q24–Q27 | Capability-specific dropdowns |
| Q28–Q29 | Duration (hours) — free text number |
| Q30 | Percentage (0–100) — free text number |

### Compliance Checklist
```
☐ Network isolation capability verified (live or exercise)
☐ Quarantine VLAN documented and tested
☐ EDR endpoint isolation tested within last 90 days
☐ Account suspension procedure tested (tabletop or live)
☐ Containment authority matrix approved by management
☐ MTTC targets defined per severity level
☐ All containment procedures documented in playbooks
☐ 24/7 containment capability confirmed (or on-call SLA documented)
```

---

## Sheet 3: Eradication & Remediation (20 Questions)

### Purpose
Assess the organisation's ability to remove threats and restore a clean state — malware removal, vulnerability remediation, and root-cause identification.

### Header
**Row 1:** "ERADICATION & REMEDIATION"
**Row 2:** "Malware Removal, Vulnerability Patching, Root Cause Identification (20 Questions)"

### Column Definitions
Identical to Sheet 2 (A–G, same widths and types).

### Section Breakdown

**Malware (Q31–Q37):** Malware removal procedure documentation, EDR automated removal capability, system reimaging capability and speed, lateral movement containment during eradication, backup verification before restoration, eradication confirmation method, average time to eradicate.

**Vulnerability (Q38–Q43):** Emergency patching capability, patch deployment speed for critical CVEs, configuration hardening procedures, vulnerability scanning post-eradication, compensating control deployment for unpatched systems, patch rollback capability.

**Root Cause (Q44–Q46):** Root cause analysis capability, percentage of incidents with documented RCA (last 10), RCA integration into control improvements.

**Metrics (Q47–Q50):** Mean Time to Eradicate (MTTE) overall (6-month), MTTE for Critical incidents, eradication success rate (no recurrence within 30 days), percentage of incidents where root cause was identified before eradication declared complete.

### Compliance Checklist
```
☐ Malware removal procedures tested (EICAR/live exercise)
☐ Reimaging capability confirmed — target time documented
☐ Emergency patch process activated and tested within last 12 months
☐ Backup integrity verified before any restoration action (procedure exists)
☐ Root cause analysis mandatory for all Critical and High incidents
☐ MTTE targets defined and tracked
☐ Eradication confirmation criteria documented (not just symptom removal)
```

---

## Sheet 4: Recovery & Restoration (20 Questions)

### Purpose
Assess restoration procedures, service resumption capability, and post-recovery monitoring controls.

### Header
**Row 1:** "RECOVERY & RESTORATION"
**Row 2:** "System Restoration, Service Resumption, Post-Recovery Monitoring (20 Questions)"

### Column Definitions
Identical to Sheet 2 (A–G, same widths and types).

### Section Breakdown

**Restoration (Q51–Q57):** System restoration procedure documentation, backup availability for critical systems, average backup restoration time, backup integrity verification before restoration, clean rebuild capability, configuration restoration capability, data recovery testing frequency.

**Resumption (Q58–Q64):** Service resumption procedures, post-recovery validation scope, staged recovery capability, user communication during recovery, service degradation mode capability, RTOs defined for critical services, percentage of incidents meeting RTO (6-month).

**Monitoring (Q65–Q70):** Enhanced monitoring period after recovery (duration), active reinfection monitoring, IOC-based monitoring post-recovery, Mean Time to Recover (MTTR) overall (6-month), MTTR for Critical incidents, recovery success rate (no recurrence within 30 days).

### Compliance Checklist
```
☐ Backup restoration tested within last 12 months (critical systems)
☐ RTOs defined and approved for all critical services
☐ Staged recovery procedure documented
☐ Enhanced monitoring period (minimum 7 days) defined in playbooks
☐ IOC watchlists maintained and updated post-incident
☐ MTTR targets defined per severity level
☐ Post-recovery validation checklist exists and is mandatory
```

---

## Sheet 5: Communication (20 Questions)

### Purpose
Assess internal coordination, external stakeholder notification, and regulatory reporting capability during active incidents.

### Header
**Row 1:** "COMMUNICATION"
**Row 2:** "Internal Coordination, External Notification, Regulatory Reporting (20 Questions)"

### Column Definitions
Identical to Sheet 2 (A–G, same widths and types).

### Section Breakdown

**Internal (Q71–Q77):** Internal communication protocol documentation, management notification SLA compliance, affected user notification approach, IT Operations coordination channel, pre-approved communication templates, communication approval process, incident communication logging.

**External (Q78–Q84):** External communication procedure documentation, customer notification capability, regulatory notification templates readiness, media/press response procedure, third-party/supplier notification, legal counsel involvement timing, post-incident customer communication.

**Regulatory (Q85–Q90):** Regulatory notification timeline compliance (last 5 breaches), breach notification procedure documented, authority contacts maintained, notification drafting speed (hours from decision to submission), regulatory feedback incorporation, multi-jurisdiction notification handling.

### Compliance Checklist
```
☐ Internal communication templates pre-approved by Legal
☐ Management notification SLA defined (Critical: <1 hour)
☐ Regulatory notification procedure reviewed by Legal annually
☐ Authority contact list maintained and tested
☐ All incident communications logged (who, what, when, to whom)
☐ External communication approval chain documented
☐ Multi-jurisdiction breach notification matrix maintained (if applicable)
```

---

## Sheet 6: Resources & Authority (20 Questions)

### Purpose
Assess budget allocation, staffing adequacy, tool availability, and the decision-authority matrix that enables rapid response execution.

### Header
**Row 1:** "RESOURCES & AUTHORITY"
**Row 2:** "Budget, Staffing, Tools, Decision Authority (20 Questions)"

### Column Definitions
Identical to Sheet 2 (A–G, same widths and types).

### Section Breakdown

**Budget & Staffing:** Dedicated IR budget existence, budget adequacy (self-assessment), CSIRT staffing model (dedicated/on-call/hybrid), 24/7 coverage capability, external IR retainer existence, IR personnel training budget.

**Tools:** IR ticketing system, SIEM availability, EDR coverage percentage, forensic tooling availability, communication/war-room capability, automation/SOAR availability.

**Authority:** Emergency change authority matrix, containment authority without management approval, budget authority during active incidents, authority matrix tested (tabletop or live), authority gaps identified, authority documentation currency.

### Compliance Checklist
```
☐ IR budget line item exists and is reviewed annually
☐ CSIRT staffing model documented and approved
☐ Authority matrix approved by executive management
☐ Authority matrix exercised in at least one tabletop per year
☐ External IR retainer (if used) contracts reviewed annually
☐ Tool availability confirmed for all IR phases
```

---

## Sheet 7: Playbook Effectiveness (15 Questions)

### Purpose
Assess whether response playbooks exist for all critical incident categories, are actively used during incidents, and are kept current.

### Header
**Row 1:** "PLAYBOOK EFFECTIVENESS"
**Row 2:** "Coverage, Usage, Maintenance (15 Questions)"

### Column Definitions
Identical to Sheet 2 (A–G, same widths and types).

### Section Breakdown

**Coverage (Q106–Q110):** Playbooks exist for all primary incident categories, coverage percentage across categories, playbooks include containment + eradication + recovery steps, playbooks reference forensic evidence collection, playbooks include communication/notification steps.

**Usage (Q111–Q115):** Playbooks consulted during last 5 incidents, percentage of incidents where playbook was followed, playbook deviation documented when occurred, playbook feedback captured post-incident, playbook accessibility during active incidents (mobile/offline).

**Maintenance (Q116–Q120):** Playbook review frequency, last review date within cycle, lessons learned incorporated, playbook owner assigned and accountable, playbook version controlled.

### Compliance Checklist
```
☐ Playbooks exist for all incident categories identified in S2 taxonomy
☐ Playbooks reviewed and updated after every Critical incident
☐ Playbooks accessible offline (printed/cached) during network outages
☐ Playbook owners assigned and accountable for annual review
☐ Playbook usage tracked per incident for effectiveness measurement
```

---

## Sheet 8: Gap Analysis (40 Capacity)

### Purpose
Consolidate all gaps flagged by the Gap_Identified formula across Sheets 2–7. Prioritise, assign owners, and track remediation.

### Header
**Row 1:** "GAP ANALYSIS"
**Row 2:** "Prioritised remediation tracking — auto-populated from assessment sheets"

### Column Definitions

| Column | Header | Width | Type | Description |
|--------|--------|-------|------|-------------|
| A | Gap_ID | 12 | Formula | Auto-numbered: `="GAP-"&TEXT(ROW()-4,"000")` |
| B | Source_Sheet | 28 | **User Input** (yellow) | Which sheet the gap originated from |
| C | Question_ID | 14 | **User Input** (yellow) | e.g. Q5, Q28 |
| D | Gap_Description | 55 | **User Input** (yellow) | Detailed description of the gap |
| E | Severity | 16 | **User Input** (yellow) | Dropdown: Critical / High / Medium / Low |
| F | Owner | 28 | **User Input** (yellow) | Name or role responsible |
| G | Target_Date | 16 | **User Input** (yellow) | DD.MM.YYYY |
| H | Status | 18 | **User Input** (yellow) | Dropdown: Open / In Progress / Completed / Deferred |
| I | Remediation_Notes | 40 | **User Input** (yellow) | Free text |

### Summary Formulas (Row 2, above headers)

```excel
Total Gaps:        =COUNTA(C5:C44)
Critical:          =COUNTIF(E5:E44,"Critical")
High:              =COUNTIF(E5:E44,"High")
Open:              =COUNTIF(H5:H44,"Open")+COUNTIF(H5:H44,"In Progress")
```

---

## Sheet 9: Evidence Register (60 Capacity)

### Purpose
Log all evidence collected to support this assessment and future audits.

### Header
**Row 1:** "EVIDENCE REGISTER"
**Row 2:** "Evidence supporting Response Capabilities assessment"

### Column Definitions

| Column | Header | Width | Type | Description |
|--------|--------|-------|------|-------------|
| A | Evidence_ID | 14 | Formula | `="EV-"&TEXT(ROW()-4,"000")` |
| B | Related_Question | 18 | **User Input** (yellow) | Q-number(s) this evidence supports |
| C | Evidence_Type | 22 | **User Input** (yellow) | Dropdown: Ticket Export / Playbook / Tool Config / Exercise Report / Training Record / Other |
| D | Description | 50 | **User Input** (yellow) | Free text — what the evidence contains |
| E | Source_Location | 40 | **User Input** (yellow) | File path, URL, or system reference |
| F | Collected_By | 22 | **User Input** (yellow) | Name |
| G | Collection_Date | 16 | **User Input** (yellow) | DD.MM.YYYY |
| H | Valid_Until | 16 | **User Input** (yellow) | DD.MM.YYYY (or "Ongoing") |

---

## Sheet 10: Dashboard

### Purpose
Automated summary of response capability maturity across all six assessment domains, plus key SLA metrics.

### Header
**Row 1:** "RESPONSE CAPABILITIES DASHBOARD"
**Row 2:** "ISMS-IMP-A.5.24-28.S3 — Automated Maturity & Metrics Summary"

### Panel 1: Key Response Metrics

| Metric | Source | Formula |
|--------|--------|---------|
| MTTC (Overall) | Sheet 2, Q28 | `='Containment Capabilities'!D32` |
| MTTC (Critical) | Sheet 2, Q29 | `='Containment Capabilities'!D33` |
| MTTE (Overall) | Sheet 3, Q47 | `='Eradication & Remediation'!D51` |
| MTTE (Critical) | Sheet 3, Q48 | `='Eradication & Remediation'!D52` |
| MTTR (Overall) | Sheet 4, Q68 | `='Recovery & Restoration'!D72` |
| MTTR (Critical) | Sheet 4, Q69 | `='Recovery & Restoration'!D73` |
| Containment SLA % | Sheet 2, Q30 | `='Containment Capabilities'!D34` |
| Recovery Success Rate | Sheet 4, Q70 | `='Recovery & Restoration'!D74` |

### Panel 2: Domain Maturity Scores

Each domain scored 0–100 based on the ratio of non-gap answers to total questions:

```excel
Containment Score:  =COUNTIF('Containment Capabilities'!G5:G34,"No")/30*100
Eradication Score:  =COUNTIF('Eradication & Remediation'!G5:G24,"No")/20*100
Recovery Score:     =COUNTIF('Recovery & Restoration'!G5:G24,"No")/20*100
Communication Score:=COUNTIF(Communication!G5:G24,"No")/20*100
Resources Score:    =COUNTIF('Resources & Authority'!G5:G24,"No")/20*100
Playbook Score:     =COUNTIF('Playbook Effectiveness'!G5:G19,"No")/15*100
```

**Maturity Level Mapping:**

| Score Range | Maturity Level | Colour |
|-------------|----------------|--------|
| 90–100 | Level 5 – Optimised | Green (#C6EFCE) |
| 70–89 | Level 4 – Managed | Light Green (#E2EFDA) |
| 50–69 | Level 3 – Defined | Yellow (#FFEB9C) |
| 30–49 | Level 2 – Developing | Orange (#FCE4D6) |
| 0–29 | Level 1 – Initial | Red (#FFC7CE) |

### Panel 3: Gap Summary

```excel
Total Gaps Flagged:  =COUNTIF('Containment Capabilities'!G5:G34,"Yes")+COUNTIF('Eradication & Remediation'!G5:G24,"Yes")+COUNTIF('Recovery & Restoration'!G5:G24,"Yes")+COUNTIF(Communication!G5:G24,"Yes")+COUNTIF('Resources & Authority'!G5:G24,"Yes")+COUNTIF('Playbook Effectiveness'!G5:G19,"Yes")
Gaps Logged in Gap Analysis: =COUNTA('Gap Analysis'!C5:C44)
Gaps Requiring Attention:    =[Total Gaps Flagged] - [Gaps Logged]
```

---

## Sheet 11: Approval Sign-Off

### Purpose
Formal review and approval workflow for the completed assessment.

### Structure

| Field | Type |
|-------|------|
| Assessment Reviewer Name | User Input (yellow) |
| Reviewer Role | User Input (yellow) |
| Review Date | User Input (yellow) |
| Review Comments | User Input (yellow, multi-line) |
| Approval Decision | Dropdown: Approved / Approved with conditions / Rejected |
| Next Review Date | User Input (yellow) |
| Next Review Responsible | User Input (yellow) |

---

## Appendix A: Developer Technical Reference

### A.1 Workbook Structure Summary

| Sheet # | Name | Questions | Key Feature |
|---------|------|-----------|-------------|
| 1 | Instructions & Legend | — | Workflow guide, status legend, evidence types |
| 2 | Containment Capabilities | 30 | Network/Endpoint/Account/Application layers |
| 3 | Eradication & Remediation | 20 | Malware removal, patching, RCA |
| 4 | Recovery & Restoration | 20 | Backup restoration, RTOs, post-recovery monitoring |
| 5 | Communication | 20 | Internal/External/Regulatory notification |
| 6 | Resources & Authority | 20 | Budget, staffing, authority matrix |
| 7 | Playbook Effectiveness | 15 | Coverage, usage, maintenance |
| 8 | Gap Analysis | 40 cap | Prioritised remediation tracking |
| 9 | Evidence Register | 60 cap | Audit evidence log |
| 10 | Dashboard | — | Metrics, maturity scores, gap summary |
| 11 | Approval Sign-Off | — | Formal approval workflow |

**Total Assessment Questions:** 125
**Freeze Panes:** Row 5 on all assessment sheets (headers stay visible)

### A.2 Data Validation Rules

**Answer Column (D) — Assessment Sheets:**

Each question defines its own dropdown or input type. The most common validation sets:

| Validation Set | Applied To | Values |
|----------------|-----------|--------|
| Capability Level | Q1, Q7, Q9, Q16, Q31, Q32, etc. | Automated / Manual / Limited / No |
| Availability | Q2, Q8 | 24/7 / Business Hours / No |
| Yes/No | Q4, Q11, Q18, Q71, Q78, etc. | Yes / No |
| Duration | Q5, Q10, Q22, Q28, Q29, Q53, Q68, Q69 | Free text number (unit shown in question) |
| Percentage | Q12, Q30, Q64, Q70, Q90 | Free text number 0–100 |
| Text | Q6, Q17, Q23 | Free text (authority holder name/role) |
| Completeness | Q7, Q31, Q51, Q75 | Comprehensive / Basic / No |

**Gap Analysis Sheet:**

| Column | Validation |
|--------|------------|
| E (Severity) | Critical / High / Medium / Low |
| H (Status) | Open / In Progress / Completed / Deferred |

**Evidence Register Sheet:**

| Column | Validation |
|--------|------------|
| C (Evidence_Type) | Ticket Export / Playbook / Tool Config / Exercise Report / Training Record / Other |

### A.3 Conditional Formatting

**Gap_Identified Column (G) — All Assessment Sheets:**
- "Yes" → Red fill (#FFC7CE), bold text
- "No" → Green fill (#C6EFCE)

**Gap Analysis Severity (Column E):**
- Critical → Red fill (#FFC7CE)
- High → Orange fill (#FCE4D6)
- Medium → Yellow fill (#FFEB9C)
- Low → Light blue fill (#B4C7E7)

**Gap Analysis Status (Column H):**
- Open → Red fill (#FFC7CE)
- In Progress → Yellow fill (#FFEB9C)
- Completed → Green fill (#C6EFCE)
- Deferred → Grey fill (#D9D9D9)

**Dashboard Maturity Scores:**
- 90–100 (Level 5) → Green (#C6EFCE)
- 70–89 (Level 4) → Light Green (#E2EFDA)
- 50–69 (Level 3) → Yellow (#FFEB9C)
- 30–49 (Level 2) → Orange (#FCE4D6)
- 0–29 (Level 1) → Red (#FFC7CE)

**Dashboard Key Metrics — SLA Thresholds:**
- MTTC ≤ target → Green
- MTTC > target but ≤ 2× target → Yellow
- MTTC > 2× target → Red
- Same logic applies to MTTE and MTTR

### A.4 Cell Protection

**Protected Cells (Formula / Static):**
- Column headers (row 4 on all assessment sheets)
- Question_ID (column A) and Question text (column C)
- Section labels (column B)
- Gap_Identified formulas (column G)
- Dashboard formulas and labels
- Gap Analysis ID formulas (column A)
- Evidence Register ID formulas (column A)

**Unprotected Cells (User Input — yellow fill):**
- Answer (column D), Evidence_Reference (column E), Comments (column F) on all assessment sheets
- All user-input columns on Gap Analysis and Evidence Register
- All fields on Approval Sign-Off
- Document information fields on Instructions & Legend

**Sheet Protection:**
- Password: [Set during workbook generation]
- Allow: Format cells, Insert rows, Sort, Filter
- Disallow: Delete rows, Modify formulas, Unprotect sheet

### A.5 Gap_Identified Formula Logic

Applied to column G on every assessment sheet row (rows 5 through end of questions):

```excel
=IF(OR(D5="No", D5="Limited", D5<80), "Yes", "No")
```

**Logic breakdown:**
- If Answer = "No" → gap flagged (capability absent)
- If Answer = "Limited" → gap flagged (insufficient capability)
- If Answer is a number < 80 → gap flagged (metric below threshold — applies to percentage and duration fields where lower = worse)
- All other answers → no gap

**Note for duration fields (Q5, Q10, Q22, Q28, Q29, Q53, Q68, Q69):** The formula flags values < 80 which is appropriate for percentage fields. Duration fields will not trigger this numeric check unless the value happens to be < 80 in the unit shown. Assessors should manually flag duration gaps in the Comments column if the value exceeds the organisation's SLA target.

### A.6 Evidence Register Auto-Numbering

**Evidence ID Format:**
```excel
="EV-"&TEXT(ROW()-4,"000")
```
Produces: EV-001, EV-002, … EV-060

**Gap ID Format (Gap Analysis sheet):**
```excel
="GAP-"&TEXT(ROW()-4,"000")
```
Produces: GAP-001, GAP-002, … GAP-040

### A.7 Python Script Integration Points

**Workbook Generation Script:** `generate_a524_28_s3_response_capabilities.py`

**Key Functions:**
- `create_workbook()`: Initialise workbook, create all 11 sheets
- `setup_styles()`: Define cell styles (header fill #003366, input fill #FFFFCC, calculated fill #E2EFDA, border)
- `create_assessment_sheet(ws, styles, title, subtitle, questions)`: Generic sheet generator — applies headers, populates questions, sets column widths, adds data validation per question type, applies Gap_Identified formula, freezes panes
- `create_containment_capabilities(ws, styles)`: Sheet 2 — 30 questions across 5 sections
- `create_eradication_remediation(ws, styles)`: Sheet 3 — 20 questions across 4 sections
- `create_recovery_restoration(ws, styles)`: Sheet 4 — 20 questions across 3 sections
- `create_communication(ws, styles)`: Sheet 5 — 20 questions across 3 sections
- `create_resources_authority(ws, styles)`: Sheet 6 — 20 questions across 3 sections
- `create_playbook_effectiveness(ws, styles)`: Sheet 7 — 15 questions across 3 sections
- `create_gap_analysis(ws, styles)`: Sheet 8 — 40-row capacity with summary formulas
- `create_evidence_register(ws, styles)`: Sheet 9 — 60-row capacity
- `create_dashboard(ws, styles)`: Sheet 10 — 3 panels (metrics, maturity, gaps)
- `create_approval_signoff(ws, styles)`: Sheet 11 — approval workflow

**Customisation Points (marked with `# CUSTOMIZE:` in script):**
- Sheet names (if organisational naming differs)
- Question text (if wording needs adjustment for local context)
- Gap threshold value (currently 80 — adjust if organisation uses different SLA benchmarks)
- Maturity level boundaries (currently 90/70/50/30)
- Conditional formatting colour codes
- Gap Analysis and Evidence Register row capacity

**Quality Assurance:** After generation, verify:
- All 125 questions present across Sheets 2–7
- Gap_Identified formula returns "Yes" or "No" for every row
- Dashboard metrics pull from correct cell references
- Data validation dropdowns active on all Answer cells

### A.8 Version Control

**Workbook Versioning:**
- Filename format: `ISMS-IMP-A.5.24-28.S3_Response_Capabilities_YYYYMMDD.xlsx`
- Version tracking in Instructions & Legend sheet
- Document Control section updated with each revision

**Change Log:**
- v1.0: Initial workbook structure — 11 sheets, 125 questions, 3-panel dashboard

**Backward Compatibility:**
- v1.0 workbooks require Excel 2016+ (for dynamic array formulas in Dashboard)
- Previous assessments should be archived with date suffix before regenerating

---

## Document Assembly Instructions

**To create the complete ISMS-IMP-A.5.24-28.S3 v1.0 document:**

1. **Document Control** (from the S3 specification file header)
2. **PART I: USER COMPLETION GUIDE** (Assessment Overview through Assessment Timeline)
3. **PART II: TECHNICAL SPECIFICATION** (this section — Instructions through Appendix A.8)

**Final Document Structure:**
```
ISMS-IMP-A.5.24-28.S3 — Incident Response Capabilities Assessment v1.0

├── Document Control (Metadata, Version History, Related Documents)
│
├── PART I: USER COMPLETION GUIDE
│   ├── 1. Assessment Overview (Purpose, Scope, Prerequisites)
│   ├── 2. Assessment Workflow (High-Level Process, Timeline)
│   ├── 3. Section-by-Section Guidance (Q&A for all 125 questions)
│   ├── 4. Evidence Collection Guide
│   ├── 5. Common Mistakes to Avoid
│   └── 6. Assessment Timeline
│
└── PART II: TECHNICAL SPECIFICATION
    ├── Document Overview & Instructions
    ├── Sheet 1: Instructions & Legend
    ├── Sheet 2: Containment Capabilities (30Q)
    ├── Sheet 3: Eradication & Remediation (20Q)
    ├── Sheet 4: Recovery & Restoration (20Q)
    ├── Sheet 5: Communication (20Q)
    ├── Sheet 6: Resources & Authority (20Q)
    ├── Sheet 7: Playbook Effectiveness (15Q)
    ├── Sheet 8: Gap Analysis
    ├── Sheet 9: Evidence Register
    ├── Sheet 10: Dashboard
    ├── Sheet 11: Approval Sign-Off
    └── Appendix A (A.1–A.8: Developer Technical Reference)
```

**Quality Checks Before Finalising:**
- [ ] All 125 questions accounted for across sheet specifications
- [ ] Dashboard formulas reference correct sheet names and cell addresses
- [ ] Gap_Identified formula documented and matches script implementation
- [ ] Data validation rules match all dropdown options in script
- [ ] Conditional formatting colour codes match script implementation
- [ ] Python script function names match this specification
- [ ] Version Control section updated
- [ ] Cross-references to S1, S2, S4, S5 accurate

---

**END OF SPECIFICATION**

---

*"Study hard what interests you the most in the most undisciplined, irreverent and original manner possible."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-02 -->
