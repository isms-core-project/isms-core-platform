<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.24-28.S3-UG:framework:UG:a.5.24-28 -->
**ISMS-IMP-A.5.24-28.S3-UG - Incident Response Capabilities Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.26

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Response Capabilities Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S3-UG |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.26) |
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

- ISMS-POL-A.5.24-28 (Incident Management Lifecycle)
- ISMS-IMP-A.5.24-28.S1 (Incident Management Framework Assessment)
- ISMS-IMP-A.5.24-28.S2 (Detection Classification Assessment)
- ISMS-IMP-A.5.24-28.S4 (Forensic Evidence Assessment)
- ISMS-IMP-A.5.24-28.S5 (Learning & Continuous Improvement Assessment)

---

### Workbook at a Glance

This workbook contains the following 11 sheets:

| Sheet | Purpose |
|-------|---------|
| **Instructions & Legend** | Assessment guidance, rating definitions, and field descriptions |
| **Containment Capabilities** | Containment strategies, tools, and execution capability assessment |
| **Eradication & Remediation** | Eradication procedures and root cause remediation capabilities |
| **Recovery & Restoration** | System recovery, data restoration, and return-to-service capabilities |
| **Communication** | Internal and external communication procedures during incidents |
| **Resources & Authority** | Resource allocation, escalation authority, and crisis management |
| **Playbook Effectiveness** | Incident response playbook coverage and effectiveness assessment |
| **Gap Analysis** | Identified gaps and remediation action tracking |
| **Evidence Register** | Tracking of supporting evidence for audit purposes |
| **Summary Dashboard** | Compliance overview auto-populated from your input data |
| **Approval Sign-Off** | Stakeholder sign-off and approval workflow |

---

## Assessment Overview

### Purpose

This assessment evaluates [Organisation]'s **incident response execution capabilities**, focusing on the **response and recovery** phase of incident management (A.5.26).

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

### Why This Matters

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

### Who Should Complete This Assessment

**Primary Responsibility:** CSIRT Manager, Incident Response Lead, or Senior Incident Responder

**Required Knowledge:**
- [Organisation]'s incident response procedures (containment, eradication, recovery)
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

### Time Estimate

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

### Connection to Policy

This assessment implements **ISMS-POL-A.5.24-28, Section 2.3 (Incident Response & Recovery)** which defines mandatory requirements for:

**Containment Requirements:**
- Documented containment procedures for each incident category
- Technical capabilities for isolation (network, endpoint, account)
- Maximum containment time SLAs (15 min Critical, 1 hour High, 4 hours Medium)
- Coordination with IT Operations for containment actions
- Authority matrix for containment decisions (who can authorise system shutdown, network segmentation)

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
**Compliance Status:** Mandatory for all [Organisation] security incidents

### Assessment Scope

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

❌ CSIRT organisational structure (see S1)
❌ Detection and triage (see S2)
❌ Forensic evidence collection (see S4)
❌ Post-incident review (see S5)

### Prerequisites

**Before Starting This Assessment:**

1. ✅ **Read Related Documents:**
   - ISMS-POL-A.5.24-28 Section 2.3 (Response & Recovery Requirements)
   - ISMS-REF-A.5.24-28 Section 3 (Forensic Collection - for evidence preservation during response)

2. ✅ **Gather Documentation:**
   - Containment procedures by incident type
   - Eradication and remediation playbooks
   - Recovery and restoration procedures
   - Communication templates and workflows
   - Authority matrix (who can authorise containment actions)

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

## Assessment Workflow

### High-Level Process

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

### Assessment Sections Overview

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

## Section-by-Section Guidance

### Sheet 2: Containment Capabilities (30 Questions)

**Purpose:** Assess ability to contain incidents quickly and effectively

---

#### **Section A: Network Containment (Q1-Q8)**

**Q1: Network_Isolation_Capability**
- **Question:** Can [Organisation] isolate network segments to contain incidents?
- **Dropdown:** Yes - Automated / Yes - Manual / Limited / No
- **Automated:** SOAR or network automation (VLAN changes, firewall rules)
- **Manual:** Network engineer executes changes
- **Evidence:** Network segmentation diagram, isolation procedure

**Q2: Firewall_Rule_Emergency_Changes**
- **Question:** Can firewall rules be changed on emergency basis to block threats?
- **Dropdown:** Yes - 24/7 / Yes - Business Hours Only / No
- **Best Practice:** 24/7 capability for Critical/High incidents
- **Authority:** Who can authorise emergency firewall changes?

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
- **Question:** Can [Organisation] force password reset for affected users?
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

### Sheet 3: Eradication & Remediation (20 Questions)

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
- **Question:** Can [Organisation] perform bulk password reset for affected users?
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
- **Verification:** No more C2 beaconing, no unauthorised access, no persistence

**Q49: Backdoor_Search**
- **Question:** Are backdoors searched for and removed?
- **Dropdown:** Yes - Comprehensive / Limited / No

**Q50: Re_infection_Prevention**
- **Question:** Are measures taken to prevent re-infection (blocking C2 IPs, monitoring for IOCs)?
- **Dropdown:** Yes / No

---

### Sheet 4: Recovery & Restoration (20 Questions)

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

### Sheet 5: Communication (20 Questions)

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
- **Question:** Are regulatory notification templates ready (GDPR, PCI DSS v4.0.1, etc.)?
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

### Sheet 6: Resources & Authority (20 Questions)

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
- **Question:** Can [Organisation] scale response for multiple simultaneous incidents?
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
- **Examples:** Who can shut down production, who can authorise emergency patching

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
- **Question:** Does [Organisation] have an incident response retainer (external firm)?
- **Dropdown:** Yes / No

**Q108: Forensic_Services_Available**
- **Question:** Can [Organisation] engage forensic services on short notice?
- **Dropdown:** Yes - Retainer / Yes - Ad-Hoc / No

**Q109: Legal_Support_Available**
- **Question:** Is legal support available 24/7 for incident response?
- **Dropdown:** Yes / Business Hours Only / No

**Q110: Insurance_Cyber_Coverage**
- **Question:** Does [Organisation] have cyber insurance covering incident response costs?
- **Dropdown:** Yes / No

---

### Sheet 7: Playbook Effectiveness (15 Questions)

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

### Sheets 8-11: Gap Analysis, Evidence, Dashboard, Approval

**(Similar structure to S1 and S2, adapted for response capabilities)**

---

## Metrics Calculation Guide

### Mean Time to Contain (MTTC)

**Formula:**
```
MTTC = Σ(Containment Timestamp - Incident Start Timestamp) / Number of Incidents
```

**Best Practice:** Track separately by severity (Critical, High, Medium, Low)

---

### Mean Time to Remediate/Recover (MTTR)

**Formula:**
```
MTTR = Σ(Recovery Complete Timestamp - Incident Start Timestamp) / Number of Incidents
```

---

### Response SLA Compliance

**Formula:**
```
SLA Compliance = (Incidents Meeting SLA / Total Incidents) × 100
```

---

## Common Mistakes to Avoid

**❌ Mistake:** Focusing on documentation without validating actual capability
**✅ Solution:** Test containment capabilities through exercises

**❌ Mistake:** Assuming IT Ops will execute containment without clear authority
**✅ Solution:** Document emergency authority matrix, train IT Ops

**❌ Mistake:** No playbook updates after incidents
**✅ Solution:** Mandatory playbook review in post-incident process

**❌ Mistake:** Communication templates not approved in advance
**✅ Solution:** Pre-approve templates with Legal/PR before incidents

---

## Assessment Timeline

**Week 1:** Containment + Eradication assessment (4-5 hours)
**Week 2:** Recovery + Communication assessment (4-5 hours)
**Week 3:** Resources + Playbooks + Gap analysis (4 hours)
**Week 4:** Evidence collection, quality review, approval (2-3 hours)

**Total:** 2-4 weeks (part-time)

---

**END OF USER GUIDE**

---

*"Speed is the essence of war."*
— Sun Tzu

<!-- QA_VERIFIED: 2026-03-01 -->
