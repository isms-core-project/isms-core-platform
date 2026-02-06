**ISMS-IMP-A.5.24-28.S4-UG - Forensic Evidence Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.28

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Forensic Evidence Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S4-UG |
| **Assessment Domain** | Domain 4 - Forensic Evidence Management (A.5.28 Focus) |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Related Reference** | ISMS-REF-A.5.24-28 (Incident Response Reference Guide, Section 3) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Digital Forensics Lead / Incident Response Manager |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Digital Forensics Lead | Initial forensic evidence assessment specification |

**Review Cycle**: Annual (or after major forensic investigation)  
**Next Review Date**: [Effective Date + 12 months]  

**Related Documents**:
- ISMS-POL-A.5.24-28 (Incident Management Lifecycle Policy)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide, Section 3: Forensic Collection Techniques Library)
- ISMS-IMP-A.5.24-28.S1 (Framework & Governance Assessment)
- ISMS-IMP-A.5.24-28.S2 (Detection & Classification Assessment)
- ISMS-IMP-A.5.24-28.S3 (Response Capabilities Assessment)
- ISMS-IMP-A.5.24-28.S5 (Learning & Improvement Assessment)
- ISO/IEC 27002:2022 Control A.5.28
- NIST SP 800-86 (Guide to Integrating Forensic Techniques into Incident Response)
- ISO/IEC 27037:2012 (Guidelines for the Identification, Collection, Acquisition and Preservation of Digital Evidence)

---

## 1. Assessment Overview

### 1.1 Purpose

This assessment evaluates [Organization]'s **digital forensic evidence management capabilities**, focusing on the collection, preservation, analysis, and legal admissibility of evidence throughout the incident lifecycle (A.5.28).

**What This Assessment Covers:**
- Evidence collection procedures and techniques
- Chain of custody management
- Evidence preservation and integrity protection
- Forensic analysis capabilities (tools, skills, processes)
- Evidence storage, retention, and disposal
- Legal readiness (court-admissible evidence, regulatory requirements)
- Integration of forensics with incident response
- Forensic capability maturity and training

**What This Assessment Does NOT Cover:**
- Incident management governance (see S1)
- Detection and classification (see S2)
- Response execution (see S3) — though evidence preservation during response is assessed here
- Post-incident learning (see S5)

**Assessment Output:**
- Excel workbook documenting forensic evidence maturity
- Evidence collection coverage assessment
- Chain of custody effectiveness evaluation
- Forensic analysis capability review
- Legal readiness assessment
- Storage and retention compliance check
- Gap analysis and capability improvement plan

### 1.2 Why This Matters

**ISO/IEC 27001:2022 Control A.5.28 Requirement:**
> *"The organisation should establish and implement procedures for the identification, collection, acquisition and preservation of evidence related to information security events."*

**ISO/IEC 27037:2012 Core Principles:**
> Digital evidence must be collected, preserved, and analysed in a manner that maintains its integrity and admissibility. The key principles are: identification, collection, acquisition, and preservation.

**Business Impact of Poor Forensic Capability:**
- **Failed Investigations:** Unable to determine root cause or attacker scope
- **Legal Liability:** Evidence not admissible in court (chain of custody broken)
- **Regulatory Penalties:** Cannot demonstrate due diligence in breach investigation
- **Recurring Incidents:** Without root cause analysis, incidents repeat
- **Insurance Claims:** Insurers require forensic evidence for claim processing
- **Reputational Damage:** Inability to provide credible investigation findings

**This Assessment Addresses:**
- Do we collect evidence effectively during incidents?
- Is chain of custody maintained throughout?
- Do we have forensic analysis capabilities?
- Is evidence stored securely and retained appropriately?
- Can evidence withstand legal challenge?
- Are forensics integrated into the incident response workflow?

### 1.3 Who Should Complete This Assessment

**Primary Responsibility:** Digital Forensics Lead, Incident Response Manager, or Senior Security Analyst with forensic experience

**Required Knowledge:**
- Digital forensics principles and methodologies
- [Organization]'s forensic tools and capabilities
- Chain of custody procedures
- Legal requirements for digital evidence
- Forensic analysis processes and techniques
- Integration with incident response workflow

**Support Roles:**
- **Forensic Analysts:** Tool usage, analysis techniques, evidence collection
- **Incident Responders:** Integration with response workflow, evidence preservation during containment
- **IT Operations:** System access for evidence collection, log preservation
- **Legal/Compliance:** Evidence admissibility requirements, retention obligations
- **CISO/Security Manager:** Resource allocation, capability decisions

**Collaboration Required:**
- Input from forensic analysts (hands-on experience)
- Review of recent forensic investigations
- Legal review of evidence procedures
- Validation of storage and retention compliance

### 1.4 Time Estimate

**Total Assessment Time:** 6-10 hours

**Breakdown:**
- **Information Gathering:** 2-3 hours
  - Review forensic procedures and tools
  - Review recent forensic investigations (evidence quality)
  - Collect chain of custody documentation
  - Review storage and retention policies
  
- **Assessment Completion:** 2-3 hours
  - Complete evidence collection assessment
  - Document preservation and chain of custody
  - Assess forensic analysis capabilities
  - Evaluate legal readiness
  
- **Gap Analysis:** 1-2 hours
  - Identify forensic capability gaps
  - Prioritize improvements
  - Develop capability enhancement plan

- **Quality Review:** 1 hour
  - Legal review of evidence procedures
  - Management review

**Complexity Factors:**
- **Simple (6 hours):** Mature forensics team, documented procedures, dedicated tools
- **Moderate (8 hours):** Some forensic capability, basic procedures
- **Complex (10+ hours):** Limited forensic capability, ad-hoc procedures, no dedicated tools

### 1.5 Connection to Policy

This assessment implements **ISMS-POL-A.5.24-28, Section 2.4 (Forensic Evidence Management)** which defines mandatory requirements for:

**Collection Requirements:**
- Evidence collected from all relevant sources (endpoints, network, logs, cloud, physical)
- Collection procedures documented per evidence type
- Forensic-grade collection (disk imaging, memory capture, log export)
- Metadata preservation (timestamps, file attributes, access logs)
- Integration with ISMS-REF-A.5.24-28 Section 3 (Forensic Collection Techniques Library)

**Preservation Requirements:**
- Chain of custody maintained from collection to disposal
- Evidence integrity verification (hash values: SHA-256 minimum)
- Tamper-evident storage
- Access control on evidence (restricted to authorized personnel)
- Backup copies of critical evidence

**Analysis Requirements:**
- Forensic analysis tools available (commercial and/or open-source)
- Qualified forensic analysts (certified or trained)
- Analysis on copies only (preserve original evidence)
- Documented analysis methodology
- Reproducible findings

**Storage & Retention Requirements:**
- Secure evidence storage (access controlled, monitored)
- Retention periods defined per incident severity and legal requirement
- Disposal procedures (secure deletion/destruction)
- Evidence catalog maintained

**Legal Readiness Requirements:**
- Evidence procedures validated by Legal
- Court-admissible evidence capabilities
- Regulatory evidence requirements met (GDPR, PCI DSS, etc.)
- Expert witness capability (if required)

**Policy Authority:** Chief Information Security Officer (CISO)  
**Compliance Status:** Mandatory for all [Organization] security incidents

### 1.6 Assessment Scope

**Included in This Assessment:**

✅ **Evidence Collection:** Collection procedures, coverage, techniques, metadata
✅ **Chain of Custody:** Documentation, integrity verification, access control
✅ **Forensic Analysis:** Tools, capabilities, methodology, qualified personnel
✅ **Storage & Retention:** Secure storage, retention periods, disposal
✅ **Legal Readiness:** Admissibility, regulatory compliance, expert witness

**Excluded:**

❌ Detection mechanisms (see S2)
❌ Response execution (see S3)
❌ Post-incident review (see S5)
❌ Detailed forensic tool configuration

### 1.7 Prerequisites

1. ✅ Read ISMS-REF-A.5.24-28 Section 3 (Forensic Collection Techniques Library)
2. ✅ Gather: Forensic procedures, chain of custody forms, tool inventory, recent investigation reports
3. ✅ Extract from last 10-15 incidents: Evidence collected, chain of custody completeness, analysis outcomes
4. ✅ Identify stakeholders: Forensic Lead, Incident Responders, Legal, IT Ops
5. ✅ Prepare evidence folder: `/Evidence/A.5.24-28/S4_Forensics/`

---

## 2. Assessment Workflow

### 2.1 High-Level Process

```
1. Evidence Collection Assessment (2 hours)
   ├── Review collection procedures by evidence type
   ├── Assess coverage (endpoints, network, logs, cloud, physical)
   ├── Evaluate collection techniques (imaging, memory, logs)
   └── Verify metadata preservation

2. Chain of Custody Assessment (1-2 hours)
   ├── Review CoC documentation procedures
   ├── Assess integrity verification (hashing)
   ├── Evaluate access control on evidence
   └── Review recent CoC records for completeness

3. Forensic Analysis Assessment (1-2 hours)
   ├── Inventory forensic tools
   ├── Assess analyst qualifications
   ├── Review analysis methodology
   └── Evaluate analysis quality from recent investigations

4. Storage & Retention Assessment (1 hour)
   ├── Review storage security
   ├── Assess retention policy compliance
   ├── Evaluate disposal procedures
   └── Check evidence catalog

5. Legal Readiness Assessment (1 hour)
   ├── Review admissibility procedures
   ├── Assess regulatory compliance
   └── Evaluate expert witness capability

6. Gap Analysis & Review (1 hour)
```

### 2.2 Assessment Sections Overview

**Sheet 1: Instructions & Legend**
**Sheet 2: Evidence Collection** — 25 questions
**Sheet 3: Chain of Custody** — 20 questions
**Sheet 4: Forensic Analysis** — 20 questions
**Sheet 5: Storage & Retention** — 15 questions
**Sheet 6: Legal & Regulatory Readiness** — 15 questions
**Sheet 7: Gap Analysis** — 40 capacity
**Sheet 8: Evidence Register** — 60 capacity
**Sheet 9: Dashboard**
**Sheet 10: Approval Sign-Off**

---

## 3. Section-by-Section Guidance

### 3.1 Sheet 2: Evidence Collection (25 Questions)

---

#### **Section A: Collection Procedures (Q1-Q8)**

**Q1: Collection_Procedures_Documented**
- **Question:** Are forensic evidence collection procedures documented?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No
- **Comprehensive:** Procedures per evidence type, step-by-step, tool-specific

**Q2: Collection_Integrated_With_IR**
- **Question:** Is evidence collection integrated into incident response procedures?
- **Dropdown:** Yes - Embedded in Playbooks / Yes - Separate Procedure / No
- **Best Practice:** Evidence collection steps embedded in response playbooks (collect before containment actions)

**Q3: Evidence_Types_Covered**
- **Question:** Which evidence types have collection procedures? (Select all: Disk Images/Memory Captures/Network Traffic/Log Files/Email Headers/Cloud Audit Logs/Physical Evidence/Mobile Device/IoT Device/Other)
- **Format:** Checkbox
- **Target:** Procedures for all applicable evidence types

**Q4: Collection_Priority_Defined**
- **Question:** Is evidence collection prioritised (volatile evidence first)?
- **Dropdown:** Yes - Documented Priority / Informal / No
- **Volatile Evidence Priority Order:**
  1. RAM / Memory (lost on power off)
  2. Network traffic (continuous flow)
  3. Running processes and connections
  4. Swap/temp files
  5. Event logs (may be overwritten)
  6. Disk contents (persistent, lowest priority)

**Q5: Pre_Collection_Checklist**
- **Question:** Is there a pre-collection checklist (verify tools, storage, hash baseline)?
- **Dropdown:** Yes / No

**Q6: Collection_Tool_Standardisation**
- **Question:** Are standard forensic collection tools defined and approved?
- **Dropdown:** Yes - Approved Tool List / Ad-Hoc Tool Selection / No
- **Importance:** Consistent, validated tools produce admissible evidence

**Q7: Collection_Training_Frequency**
- **Question:** How frequently do responders receive forensic collection training?
- **Dropdown:** Quarterly / Semi-Annually / Annually / Onboarding Only / Never
- **Best Practice:** Annually minimum, quarterly recommended

**Q8: Collection_Mistakes_Prevention**
- **Question:** Are common collection mistakes addressed in training? (e.g., not hashing before imaging, contaminating evidence)
- **Dropdown:** Yes / No

---

#### **Section B: Evidence by Source (Q9-Q18)**

For each evidence source, assess collection capability:

**Q9: Endpoint_Disk_Collection**
- **Category:** Endpoint Disk Image
- **Collection Capability:** Full Image / Targeted Collection / No Capability
- **Tool:** [Tool name]
- **Note:** Full disk image preferred (preserves deleted files, slack space)

**Q10: Endpoint_Memory_Collection**
- **Category:** Memory (RAM) Capture
- **Collection Capability:** Live Capture / Not Capable / No Process
- **Tool:** [Tool name]
- **Note:** Must be live capture (memory lost on shutdown)

**Q11: Network_Traffic_Capture**
- **Category:** Network Traffic (PCAP)
- **Collection Capability:** Real-Time Capture / Retrospective (from logs) / No Capability
- **Tool:** [Tool name]

**Q12: Log_Collection**
- **Category:** System/Application Logs
- **Collection Capability:** Centralised (SIEM) / Per-System Export / No
- **Retention:** How long are logs retained before overwrite?

**Q13: Email_Evidence_Collection**
- **Category:** Email Evidence (headers, attachments, routing)
- **Collection Capability:** Full Mailbox Export / Individual Message / No
- **Legal Note:** Email evidence often critical for phishing/BEC investigations

**Q14: Cloud_Evidence_Collection**
- **Category:** Cloud Audit Logs (AWS CloudTrail, Azure Activity Log, etc.)
- **Collection Capability:** Automated Export / Manual Export / No Cloud Logging
- **Note:** Cloud evidence has limited retention — collect promptly

**Q15: Mobile_Device_Collection**
- **Category:** Mobile Device Evidence
- **Collection Capability:** Forensic Acquisition / Logical Extraction Only / No Capability
- **Tools:** Cellebrite, Oxygen Forensic, etc.

**Q16: Physical_Evidence_Collection**
- **Category:** Physical Evidence (hardware, printed documents, USB drives)
- **Collection Capability:** Documented Procedure / Informal / No
- **Note:** Physical evidence requires different handling than digital

**Q17: Application_Evidence_Collection**
- **Category:** Application-Level Evidence (database records, transaction logs, API logs)
- **Collection Capability:** Automated / Manual with Developers / No
- **Coordination:** May require application team involvement

**Q18: IoT_OT_Evidence_Collection**
- **Category:** IoT/OT Device Evidence
- **Collection Capability:** Capable / Limited / No Capability / N/A (No IoT/OT)
- **Challenge:** IoT devices often lack forensic acquisition tools

---

#### **Section C: Collection Quality (Q19-Q25)**

**Q19: Collection_Completeness**
- **Question:** Based on recent investigations, was evidence collection complete? (Last 10 incidents)
- **Dropdown:** Yes - Consistently / Usually / Sometimes / No
- **Complete:** All relevant evidence types collected

**Q20: Volatile_Evidence_Captured**
- **Question:** Was volatile evidence captured before containment actions? (Last 10 incidents)
- **Dropdown:** Yes - Consistently / Usually / Sometimes / No
- **Critical:** Memory and network captures before endpoint isolation

**Q21: Evidence_Collection_Time**
- **Question:** Average time to begin evidence collection after incident declaration?
- **Format:** Duration
- **Target:** <30 minutes for Critical, <2 hours for High

**Q22: Collection_Documentation**
- **Question:** Is evidence collection documented during the process?
- **Dropdown:** Yes - Real-Time Documentation / Post-Incident Documentation / No
- **Content:** What was collected, when, from where, by whom, using what tool

**Q23: Collection_Coverage_Rate**
- **Question:** What percentage of incidents had adequate evidence collection? (Last 10 incidents)
- **Format:** Percentage
- **Target:** >85%
- **Gap if <70%:** HIGH - Insufficient evidence collection

**Q24: External_Forensics_Collection**
- **Question:** If external forensics engaged, is evidence collection coordinated?
- **Dropdown:** Yes - Before Engagement / During Engagement / No Coordination / N/A
- **Best Practice:** Collect initial evidence internally before engaging external firm

**Q25: Collection_Lessons_Learned**
- **Question:** Are evidence collection lessons learned captured and applied?
- **Dropdown:** Yes - Systematically / Sometimes / No

---

### 3.2 Sheet 3: Chain of Custody (20 Questions)

---

#### **Section A: CoC Documentation (Q26-Q32)**

**Q26: CoC_Procedure_Documented**
- **Question:** Is chain of custody procedure documented?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No
- **Content:** Transfer documentation, access logging, handling requirements

**Q27: CoC_Form_Used**
- **Question:** Are chain of custody forms completed for all evidence?
- **Dropdown:** Yes - Always / Usually / Sometimes / No
- **Form Content:** Evidence ID, description, collector, date/time, location, transfers

**Q28: CoC_Digital_vs_Paper**
- **Question:** How is chain of custody documented?
- **Dropdown:** Digital System / Paper Forms / Both / None
- **Best Practice:** Digital (tamper-evident, searchable) supplemented by paper backup

**Q29: CoC_Transfer_Documentation**
- **Question:** Is every evidence transfer documented (who transferred, to whom, when, why)?
- **Dropdown:** Yes - All Transfers / Most Transfers / Minimal / No

**Q30: CoC_Access_Logging**
- **Question:** Is access to stored evidence logged?
- **Dropdown:** Yes - All Access / Selected Access / No
- **Importance:** Any undocumented access can invalidate evidence in court

**Q31: CoC_Completeness**
- **Question:** Based on recent investigations, was CoC complete? (Last 10 incidents)
- **Dropdown:** Yes - Consistently / Usually / Sometimes / No
- **Complete:** Unbroken chain from collection to current storage

**Q32: CoC_Training**
- **Question:** Do all personnel handling evidence receive CoC training?
- **Dropdown:** Yes - All Personnel / Forensic Team Only / No
- **Risk:** IT Ops may handle evidence during containment without CoC awareness

---

#### **Section B: Integrity Verification (Q33-Q38)**

**Q33: Hash_Verification_Performed**
- **Question:** Are hash values calculated for all collected evidence?
- **Dropdown:** Yes - Always / Usually / Sometimes / No
- **Hash Algorithms:** SHA-256 minimum (MD5 no longer considered sufficient)

**Q34: Hash_Algorithm_Used**
- **Question:** What hash algorithm is used for evidence verification?
- **Dropdown:** SHA-256 / SHA-512 / MD5 (Legacy) / Multiple / None

**Q35: Dual_Hashing**
- **Question:** Is dual hashing used (two independent hash algorithms)?
- **Dropdown:** Yes / No
- **Best Practice:** SHA-256 + MD5 (legacy compatibility) or SHA-256 + SHA-512

**Q36: Hash_Verification_On_Copy**
- **Question:** Are hash values verified when evidence copies are made?
- **Dropdown:** Yes - Always / Sometimes / No
- **Purpose:** Confirm copy is identical to original (bit-for-bit)

**Q37: Hash_Storage**
- **Question:** Are hash values stored securely and separately from evidence?
- **Dropdown:** Yes - Separate Storage / Stored With Evidence / No

**Q38: Integrity_Check_Frequency**
- **Question:** How often is stored evidence integrity verified?
- **Dropdown:** On Each Access / Monthly / Quarterly / Annually / Never

---

#### **Section C: Access Control (Q39-Q45)**

**Q39: Evidence_Access_Restricted**
- **Question:** Is access to forensic evidence restricted to authorised personnel?
- **Dropdown:** Yes - Strictly Controlled / Yes - Role-Based / Limited Control / No

**Q40: Evidence_Access_List**
- **Question:** Is an authorised access list maintained for each evidence item?
- **Dropdown:** Yes / No

**Q41: Evidence_Read_Only_Access**
- **Question:** Is evidence accessible in read-only mode (analysis on copies)?
- **Dropdown:** Yes - Enforced / Yes - Policy / No
- **Critical:** Original evidence must never be modified

**Q42: Physical_Evidence_Security**
- **Question:** Is physical evidence stored in a secure, access-controlled location?
- **Dropdown:** Yes - Dedicated Evidence Room / Yes - Secure Location / No
- **Requirements:** Locked, logged access, environmental controls

**Q43: Unauthorised_Access_Detection**
- **Question:** Can unauthorised access to evidence be detected?
- **Dropdown:** Yes - Alerted / Yes - Logged / No
- **Monitoring:** File access alerts, storage system audit logs

**Q44: Evidence_Sharing_Controls**
- **Question:** Are controls in place for sharing evidence with external parties (law enforcement, forensic firms)?
- **Dropdown:** Yes - Documented Controls / Informal / No
- **Legal requirement:** Sharing must be authorised and documented

**Q45: Evidence_Handling_Gloves**
- **Question:** For physical evidence, are handling precautions followed (gloves, packaging)?
- **Dropdown:** Yes - Always / Sometimes / No / N/A (No Physical Evidence)

---

### 3.3 Sheet 4: Forensic Analysis (20 Questions)

---

#### **Section A: Analysis Tools (Q46-Q52)**

**Q46: Forensic_Tools_Available**
- **Question:** What forensic analysis tools are available? (Select all: Disk Analysis/Memory Analysis/Network Analysis/Malware Analysis/Mobile Analysis/Cloud Forensics/Log Analysis/Other)
- **Format:** Checkbox

**Q47: Commercial_vs_OpenSource_Tools**
- **Question:** What type of forensic tools are used?
- **Dropdown:** Commercial Only / Open-Source Only / Both / None

**Q48: Tool_Licensing**
- **Question:** Are forensic tools properly licensed and maintained?
- **Dropdown:** Yes - All Tools Licensed / Mostly / No
- **Unlicensed tools may produce inadmissible evidence**

**Q49: Tool_Validation**
- **Question:** Are forensic tools validated/tested before use in investigations?
- **Dropdown:** Yes - Regularly Validated / Yes - Initial Validation / No
- **Best Practice:** Tools tested against known evidence sets, results verified

**Q50: Tool_Updates**
- **Question:** Are forensic tools kept up-to-date?
- **Dropdown:** Yes - Monthly / Yes - Quarterly / Infrequently / Never
- **Importance:** Updated tools support latest file formats and techniques

**Q51: Dedicated_Forensic_Workstations**
- **Question:** Are dedicated forensic workstations available (isolated from production network)?
- **Dropdown:** Yes - Dedicated / Yes - Shared (Isolated When Used) / No
- **Isolation:** Prevents evidence contamination, blocks network access

**Q52: Malware_Analysis_Sandbox**
- **Question:** Is a malware analysis sandbox (isolated environment) available?
- **Dropdown:** Yes - Commercial (Any.run, Joe, etc.) / Yes - Internal / No
- **Purpose:** Safely execute suspicious samples for behaviour analysis

---

#### **Section B: Analyst Capabilities (Q53-Q60)**

**Q53: Forensic_Analyst_Count**
- **Question:** How many qualified forensic analysts does [Organisation] have?
- **Format:** Number
- **Benchmarking:** Minimum 1 FTE for forensic capability, 2+ for larger organisations

**Q54: Forensic_Certifications**
- **Question:** Do forensic analysts hold recognised certifications?
- **Dropdown:** Yes - DFCERT/GCFE/GCIH/EnCE / Yes - Other Certifications / No Certifications
- **Recognised:** SANS GCFE/GREM/GCIH, IACIS GCFE, (ISC)² CCFP, AccessData EnCE

**Q55: Forensic_Training_Frequency**
- **Question:** How frequently do forensic analysts receive training?
- **Dropdown:** Quarterly / Semi-Annually / Annually / Onboarding Only / Never

**Q56: Analysis_Methodology_Documented**
- **Question:** Is forensic analysis methodology documented?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No
- **Content:** Investigation approach, analysis steps, documentation requirements

**Q57: Analysis_On_Copies_Only**
- **Question:** Is forensic analysis always performed on copies (original preserved)?
- **Dropdown:** Yes - Always / Usually / Sometimes / No
- **Critical:** Modifying original evidence invalidates it

**Q58: Reproducibility**
- **Question:** Are forensic findings reproducible (another analyst can verify)?
- **Dropdown:** Yes - Documented for Reproducibility / Partial / No
- **Importance:** Court requirement — findings must be reproducible

**Q59: Analysis_Quality_Review**
- **Question:** Are forensic analysis reports reviewed by a second analyst?
- **Dropdown:** Yes - Always / Sometimes / No
- **Best Practice:** Independent review before report finalisation

**Q60: External_Forensics_Capability**
- **Question:** Can [Organisation] engage qualified external forensic services?
- **Dropdown:** Yes - Retainer / Yes - Ad-Hoc / No

---

#### **Section C: Analysis Outcomes (Q61-Q65)**

**Q61: Root_Cause_Identification_Rate**
- **Question:** What percentage of incidents had root cause identified through forensic analysis? (Last 10 incidents requiring forensics)
- **Format:** Percentage
- **Target:** >80%
- **Gap if <60%:** HIGH - Forensic analysis insufficient

**Q62: Attacker_Scope_Determination**
- **Question:** What percentage of breach incidents had full attacker scope determined?
- **Format:** Percentage
- **Target:** >75%
- **Scope:** All compromised systems, data accessed, lateral movement path

**Q63: IOC_Generation**
- **Question:** Are IOCs (Indicators of Compromise) generated from forensic analysis?
- **Dropdown:** Yes - Systematically / Sometimes / No
- **IOCs:** File hashes, IPs, domains, registry keys, YARA rules

**Q64: Analysis_Timeline_Accuracy**
- **Question:** Are incident timelines reconstructed accurately through forensic analysis?
- **Dropdown:** Yes - Comprehensive / Partial / No
- **Timeline:** When attacker entered, actions taken, data accessed, exfiltration

**Q65: Findings_Actionable**
- **Question:** Were forensic findings actionable (led to containment/remediation improvements)?
- **Dropdown:** Yes - Consistently / Usually / Sometimes / No

---

### 3.4 Sheet 5: Storage & Retention (15 Questions)

---

#### **Section A: Evidence Storage (Q66-Q72)**

**Q66: Evidence_Storage_Location**
- **Question:** Where is forensic evidence stored?
- **Dropdown:** Dedicated Evidence Server / Cloud Storage (Isolated) / General File Share / No Dedicated Storage

**Q67: Storage_Access_Control**
- **Question:** Is evidence storage access-controlled?
- **Dropdown:** Yes - Strict (Role-Based) / Yes - Basic / No

**Q68: Storage_Encryption**
- **Question:** Is stored evidence encrypted?
- **Dropdown:** Yes - At Rest and In Transit / Yes - At Rest Only / No

**Q69: Storage_Redundancy**
- **Question:** Are backup copies of critical evidence maintained?
- **Dropdown:** Yes - Multiple Copies / Yes - Single Backup / No

**Q70: Storage_Monitoring**
- **Question:** Is evidence storage monitored for access and changes?
- **Dropdown:** Yes - Real-Time Alerts / Yes - Periodic Review / No

**Q71: Evidence_Catalog**
- **Question:** Is an evidence catalog maintained (inventory of all stored evidence)?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No
- **Catalog Content:** Evidence ID, type, incident, date collected, location, status, retention date

**Q72: Storage_Capacity**
- **Question:** Is storage capacity sufficient for forensic evidence?
- **Dropdown:** Yes - Adequate / Yes - Near Capacity / No - Insufficient

---

#### **Section B: Retention & Disposal (Q73-Q80)**

**Q73: Retention_Policy_Defined**
- **Question:** Are retention periods defined for forensic evidence?
- **Dropdown:** Yes - By Severity / Yes - Uniform Period / No
- **Guidance:**
  - Critical (data breach): 3-7 years (legal/regulatory)
  - High: 2-3 years
  - Medium: 1-2 years
  - Low: 6-12 months

**Q74: Retention_Regulatory_Compliance**
- **Question:** Do retention periods meet regulatory requirements?
- **Dropdown:** Yes / No / Not Assessed
- **Regulations:** GDPR (as long as needed for investigation), PCI DSS (1 year minimum), national laws

**Q75: Retention_Legal_Hold**
- **Question:** Can evidence retention be extended via legal hold?
- **Dropdown:** Yes - Documented Process / Informal / No

**Q76: Evidence_Disposal_Procedure**
- **Question:** Are evidence disposal procedures documented?
- **Dropdown:** Yes / No
- **Disposal:** Secure deletion (DoD 5220.22-M or equivalent), physical destruction for hardware

**Q77: Disposal_Authorisation**
- **Question:** Is evidence disposal authorised before execution?
- **Dropdown:** Yes - Manager Approval / Yes - Legal Approval / No Authorisation Required

**Q78: Disposal_Verification**
- **Question:** Is evidence disposal verified (confirmation of deletion)?
- **Dropdown:** Yes / No

**Q79: Disposal_Records**
- **Question:** Are disposal records maintained?
- **Dropdown:** Yes / No
- **Record Content:** What was disposed, when, by whom, method, authorisation

**Q80: Automated_Disposal**
- **Question:** Is evidence disposal automated when retention period expires?
- **Dropdown:** Yes - Automated with Notification / Manual Process / No
- **Risk of Manual:** Evidence retained longer than needed (GDPR compliance risk)

---

### 3.5 Sheet 6: Legal & Regulatory Readiness (15 Questions)

---

#### **Section A: Legal Admissibility (Q81-Q88)**

**Q81: Legal_Review_Of_Procedures**
- **Question:** Have forensic evidence procedures been reviewed by Legal?
- **Dropdown:** Yes - Recently Reviewed / Yes - Initial Review Only / No
- **Target:** Annual legal review of evidence procedures

**Q82: Admissibility_Requirements_Known**
- **Question:** Are legal admissibility requirements known and documented?
- **Dropdown:** Yes - Jurisdiction-Specific / Yes - General / No
- **Requirements vary by jurisdiction (country, state)**

**Q83: Expert_Witness_Capability**
- **Question:** Can [Organisation] provide expert witnesses for legal proceedings?
- **Dropdown:** Yes - Internal Expert / Yes - External Expert Available / No

**Q84: Evidence_Report_Format**
- **Question:** Is forensic report format suitable for legal proceedings?
- **Dropdown:** Yes - Legal-Ready / Partially / No
- **Content:** Methodology, findings, conclusions, analyst credentials, reproducibility

**Q85: Cross_Examination_Preparation**
- **Question:** Are forensic analysts prepared for cross-examination?
- **Dropdown:** Yes - Trained / Partially / No / Not Yet Required

**Q86: Evidence_Integrity_Documentation**
- **Question:** Is evidence integrity fully documented (collection, transfers, storage, access)?
- **Dropdown:** Yes - Complete Trail / Mostly / No
- **Legal Requirement:** Unbroken chain of custody with integrity verification

**Q87: Photograph_Documentation**
- **Question:** Is physical evidence photographed in situ before collection?
- **Dropdown:** Yes - Always / Sometimes / No / N/A
- **Purpose:** Preserve scene context for reconstruction

**Q88: Witness_Statements**
- **Question:** Are witness statements collected during incidents?
- **Dropdown:** Yes - Systematically / Sometimes / No
- **Witnesses:** First responders, affected users, system administrators

---

#### **Section B: Regulatory Compliance (Q89-Q95)**

**Q89: GDPR_Evidence_Requirements**
- **Question:** Are forensic procedures compliant with GDPR evidence requirements?
- **Dropdown:** Yes / No / Not Applicable
- **GDPR:** Evidence needed for breach notification, data protection impact

**Q90: PCI_DSS_Evidence_Requirements**
- **Question:** Are forensic procedures compliant with PCI DSS requirements?
- **Dropdown:** Yes / No / Not Applicable
- **PCI DSS:** Requirement 12.10 — Forensic readiness for incident response

**Q91: Industry_Specific_Requirements**
- **Question:** Are industry-specific forensic requirements met (banking, healthcare, etc.)?
- **Dropdown:** Yes / No / Not Applicable
- **Examples:** Financial sector forensic requirements, healthcare breach notification

**Q92: Regulatory_Evidence_Submission**
- **Question:** Can forensic evidence be submitted to regulators in required format?
- **Dropdown:** Yes - Ready / Needs Preparation / No
- **Regulators:** Data protection authorities, financial regulators, sector-specific

**Q93: Law_Enforcement_Cooperation**
- **Question:** Can [Organisation] cooperate with law enforcement evidence requests?
- **Dropdown:** Yes - Documented Process / Informal / No
- **Legal:** Court orders, seizure requests, mutual legal assistance

**Q94: International_Evidence_Requirements**
- **Question:** Are international evidence requirements considered (if incidents cross borders)?
- **Dropdown:** Yes / No / Not Applicable
- **Complexity:** Different jurisdictions have different evidence rules

**Q95: Regulatory_Audit_Readiness**
- **Question:** Is forensic evidence available and accessible for regulatory audits?
- **Dropdown:** Yes - Readily Available / Needs Organisation / No

---

## 4. Metrics Calculation Guide

### 4.1 Evidence Collection Completeness
```
Completeness = (Incidents with Adequate Evidence / Total Incidents) × 100
Target: >85%
```

### 4.2 Chain of Custody Integrity Rate
```
CoC Integrity = (Incidents with Unbroken CoC / Total Incidents) × 100
Target: >95% (legal requirement)
```

### 4.3 Root Cause Identification Rate
```
RCI Rate = (Incidents with Root Cause Found / Incidents Requiring Forensics) × 100
Target: >80%
```

### 4.4 Forensic Analysis Cycle Time
```
Analysis Time = Σ(Analysis Complete - Evidence Received) / Number of Analyses
Target: <72 hours for Critical incidents
```

---

## 5. Common Mistakes to Avoid

**❌ Mistake:** Containment before evidence collection (volatile evidence lost)
**✅ Solution:** Collect RAM and network captures before isolating endpoints

**❌ Mistake:** Analysing original evidence (risk of modification)
**✅ Solution:** Always work on forensic copies, preserve originals untouched

**❌ Mistake:** Incomplete chain of custody documentation
**✅ Solution:** Document every transfer, access, and handling event

**❌ Mistake:** Using unvalidated forensic tools
**✅ Solution:** Validate tools against known test sets, maintain tool inventory

**❌ Mistake:** Storing evidence on shared file servers
**✅ Solution:** Dedicated, access-controlled evidence storage

---

## 6. Assessment Timeline

**Week 1:** Evidence Collection + Chain of Custody assessment (3-4 hours)
**Week 2:** Forensic Analysis + Storage/Retention assessment (3-4 hours)
**Week 3:** Legal Readiness + Gap Analysis + Review (2-3 hours)

**Total:** 2-3 weeks (part-time)

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
