# ISMS-IMP-A.5.24-28.S4 — Forensic Evidence Assessment

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Forensic Evidence Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S4 |
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

# PART I: USER COMPLETION GUIDE

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

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

Workbook Structure (10 Sheets)

Instructions & Legend
Evidence Collection (25 Q)
Chain of Custody (20 Q)
Forensic Analysis (20 Q)
Storage & Retention (15 Q)
Legal & Regulatory Readiness (15 Q)
Gap Analysis (40 capacity)
Evidence Register (60 capacity)
Dashboard
Approval Sign-Off

Total Questions: 95
Key Metrics: Collection Completeness, CoC Integrity Rate, Root Cause ID Rate, Analysis Cycle Time

**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

## Document Overview

**Document ID:** ISMS-IMP-A.5.24-28.S4
**Assessment Area:** Forensic Evidence Management (Collection, Chain of Custody, Analysis, Storage, Legal Readiness)
**Related Policy:** ISMS-POL-A.5.24-28, Section 2.4 (A.5.28 – Collection of Evidence)
**Related Reference:** ISMS-REF-A.5.24-28, Section 3 (Forensic Collection Techniques Library)
**Purpose:** Evaluate the organisation's capability to collect, preserve, analyse, store, and present digital forensic evidence in a legally admissible manner throughout the incident lifecycle

**Key Principle:** This assessment is **evidence-integrity-driven**. The central question is not just whether forensic tools exist, but whether the chain of custody from collection through to analysis and storage is unbroken. Assessors review the last 10 incidents requiring forensic activity to validate real-world capability against documented procedures.

---

## Instructions for Completing This Assessment

### How to Use This Document

This technical specification defines the structure, validation rules, and formulas for the Forensic Evidence Assessment Excel workbook (`ISMS-IMP-A.5.24-28.S4_Forensic_Evidence_[DATE].xlsx`).

**Workbook Generation:** Python script `generate_a524_28_s4_forensic_evidence.py` creates the workbook based on this specification.

**Assessment Completion Process:**

1. **Read ISMS-REF-A.5.24-28 Section 3** (Forensic Collection Techniques Library) before starting — it defines the evidence types and collection methods this assessment validates against
2. **Pull data from last 10 incidents** that required forensic activity — note what evidence was collected, whether CoC was maintained, and analysis outcomes
3. **Complete Evidence Collection** — coverage across all 10 evidence source types
4. **Complete Chain of Custody** — documentation, integrity verification, access control
5. **Complete Forensic Analysis** — tools, analyst capability, outcomes
6. **Complete Storage & Retention** — security, retention periods, disposal
7. **Complete Legal & Regulatory Readiness** — admissibility, regulatory compliance
8. **Review the Dashboard** — the coverage matrix pulls live from the Collection sheet; verify it reflects reality
9. **Transfer gaps** to Gap Analysis, prioritise, assign owners
10. **Obtain approval** — Legal review is recommended before sign-off on this domain

### Status Legend

| Symbol | Meaning | Description |
|--------|---------|-------------|
| **✅** | **Compliant** | Capability fully operational, evidence integrity maintained |
| **⚠️** | **Partial** | Capability exists but gaps in coverage or integrity |
| **❌** | **Non-Compliant** | Capability missing or evidence integrity compromised |
| **N/A** | **Not Applicable** | Does not apply to this organisation's environment |

### Acceptable Evidence

- Forensic tool inventory and licence records
- Chain of custody forms (last 10 incidents)
- Hash verification logs
- Forensic analysis reports
- Evidence storage access logs
- Legal hold documentation
- Forensic analyst certification records
- Training completion records
- Incident investigation final reports
- Regulatory notification records referencing forensic evidence

### Evidence Source Types (10 Categories)

These are the 10 evidence source categories referenced throughout this assessment and displayed in the Dashboard coverage matrix:

| # | Source Type | Description |
|---|-------------|-------------|
| 1 | Disk | Hard drives / SSDs — full disk imaging |
| 2 | Memory | RAM capture (volatile) |
| 3 | Network | Packet captures, NetFlow, DNS |
| 4 | Logs | Application, OS, security event logs |
| 5 | Cloud | Cloud provider audit logs, API exports |
| 6 | SaaS | SaaS application audit logs (M365, etc.) |
| 7 | Mobile | Smartphone / tablet forensics |
| 8 | Email | Email header analysis, mailbox exports |
| 9 | Physical | Physical media, hardware |
| 10 | IoT | Internet of Things device logs / firmware |

---

## Sheet 1: Instructions & Legend

### Header Section
- **Title:** "ISMS-IMP-A.5.24-28.S4 — Forensic Evidence Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 – Control A.5.28: Collection of Evidence"
- **Styling:** Dark blue header (#003366), white text, centred, row height 30

### Document Information Block
```plaintext
Document ID:           ISMS-IMP-A.5.24-28.S4
Assessment Area:       Forensic Evidence Management
Related Policy:        ISMS-POL-A.5.24-28, Section 2.4
Related Reference:     ISMS-REF-A.5.24-28, Section 3
Version:               1.0
Assessment Date:       [USER INPUT – yellow cell]
Completed By:          [USER INPUT – yellow cell]
Organisation:          [USER INPUT – yellow cell]
Incidents Reviewed:    [USER INPUT – yellow cell, e.g. "Last 10 forensic incidents"]
Review Cycle:          Annual (or after major forensic investigation)
```

### How to Use This Workbook
1. Read ISMS-REF-A.5.24-28 Section 3 for forensic technique reference
2. Pull last 10 incidents requiring forensic activity from your ticketing system
3. Complete Evidence Collection — assess coverage across all 10 source types
4. Complete Chain of Custody — validate documentation and integrity procedures
5. Complete Forensic Analysis — inventory tools, assess analyst capability
6. Complete Storage & Retention — review security and retention compliance
7. Complete Legal & Regulatory Readiness — validate admissibility procedures
8. Review Dashboard — coverage matrix auto-populates from Collection sheet
9. Log gaps in Gap Analysis with severity and owners
10. Obtain approval (Legal review recommended before sign-off)

### Status Legend (rendered in workbook)

| Symbol | Status | Description | Colour Code |
|--------|--------|-------------|-------------|
| ✅ | Compliant | Evidence integrity maintained | Green (#C6EFCE) |
| ⚠️ | Partial | Gaps in coverage or integrity | Yellow (#FFEB9C) |
| ❌ | Non-Compliant | Capability missing or integrity compromised | Red (#FFC7CE) |
| N/A | Not Applicable | Not relevant to this environment | Grey (#D9D9D9) |

---

## Sheet 2: Evidence Collection (25 Questions)

### Purpose
Assess whether the organisation can collect forensic evidence from all relevant source types, using forensically sound methods that preserve integrity and metadata.

### Header
**Row 1:** "EVIDENCE COLLECTION"
**Row 2:** "Collection Procedures, Coverage, Techniques, Metadata Preservation (25 Questions)"

### Column Definitions

| Column | Header | Width | Type | Description |
|--------|--------|-------|------|-------------|
| A | Question_ID | 12 | Static | Q1–Q25, prefixed by section header rows |
| B | Section | 25 | Static | Collection Procedures / Coverage / Techniques / Metadata / External |
| C | Question | 60 | Static | Assessment question text (wrap text enabled) |
| D | Answer | 25 | **User Input** (yellow) | Dropdown or free-text per question type |
| E | Evidence_Reference | 30 | **User Input** (yellow) | Incident ticket IDs, tool names, document paths |
| F | Comments | 35 | **User Input** (yellow) | Free text — context, gaps, planned improvements |
| G | Gap_Identified | 12 | Formula (green) | Auto-calculated |

### Section Breakdown

**Collection Procedures (Q1–Q8):** Procedures documented, integration with IR playbooks, evidence type coverage (multi-select: Disk/Memory/Network/Logs/Cloud/SaaS/Mobile/Email/Physical/IoT), volatile evidence collection priority, collection before containment protocol, collection automation capability, collection procedure training frequency, collection procedure last review date.

**Coverage (Q9–Q15):** Disk imaging capability, memory capture capability, network traffic capture, log collection centralisation, cloud evidence export capability, mobile device forensic capability, percentage of evidence types with documented collection procedure.

**Techniques (Q16–Q20):** Disk imaging method (forensic vs logical), write blockers used for physical media, memory capture tool availability, network capture tool availability, collection tool validation status.

**Metadata (Q21–Q23):** File metadata preserved during collection, timestamp integrity maintained, collection context documented (who, what tool, when, from where).

**External (Q24–Q25):** External forensic engagement coordination, collection lessons learned captured.

### Compliance Checklist
```
☐ Collection procedures documented for all 10 evidence source types
☐ Volatile evidence collection prioritised (RAM before disk shutdown)
☐ Collection integrated into response playbooks (not a separate afterthought)
☐ Write blockers available for all physical media collection
☐ Forensic-grade imaging tools available (not ad-hoc copy)
☐ Collection procedure tested in at least one exercise per year
☐ Metadata preservation verified (timestamps, file attributes)
☐ Collection lessons learned feed back into procedure updates
```

---

## Sheet 3: Chain of Custody (20 Questions)

### Purpose
Assess whether evidence integrity is maintained from the moment of collection through storage — the single most critical requirement for legal admissibility.

### Header
**Row 1:** "CHAIN OF CUSTODY"
**Row 2:** "Documentation, Integrity Verification, Access Control (20 Questions)"

### Column Definitions
Identical to Sheet 2 (A–G, same widths and types).

### Section Breakdown

**CoC Documentation (Q26–Q32):** CoC procedure documented, CoC forms completed for all evidence, digital vs paper documentation method, transfer documentation completeness (who/to whom/when/why), access logging on stored evidence, CoC completeness in recent investigations (last 10), CoC training coverage.

**Integrity Verification (Q33–Q38):** Hash values calculated for all evidence, hash algorithm used (SHA-256 minimum), dual hashing practice, hash verification at each transfer point, hash mismatch response procedure, hash verification automation.

**Access Control (Q39–Q45):** Evidence storage access control model, access limited to authorised personnel only, evidence access logged with justification, tamper-evident storage measures, backup copies of critical evidence maintained, evidence handling physical security (if applicable), access control tested (attempted unauthorised access scenario).

### Compliance Checklist
```
☐ Chain of custody form completed for every piece of evidence collected
☐ SHA-256 (minimum) hash calculated at collection and verified at each transfer
☐ All evidence access logged — who, when, why, duration
☐ Dual hashing used (two independent algorithms)
☐ Tamper-evident storage confirmed (sealed containers or access-controlled digital storage)
☐ CoC procedure reviewed by Legal annually
☐ No undocumented access to evidence in last 12 months
☐ CoC training delivered to all IR team members who may handle evidence
```

---

## Sheet 4: Forensic Analysis (20 Questions)

### Purpose
Assess the organisation's forensic analysis capability — tools, qualified personnel, methodology, and the quality of analysis outcomes.

### Header
**Row 1:** "FORENSIC ANALYSIS"
**Row 2:** "Analysis Tools, Analyst Capabilities, Analysis Outcomes (20 Questions)"

### Column Definitions
Identical to Sheet 2 (A–G, same widths and types).

### Section Breakdown

**Analysis Tools (Q46–Q52):** Forensic tool availability (multi-select: Disk/Memory/Network/Malware/Mobile/Cloud/Log), commercial vs open-source mix, tool licensing compliance, tool validation against known test sets, tool update frequency, dedicated forensic workstations available (isolated from production), malware analysis sandbox availability.

**Analyst Capabilities (Q53–Q60):** Number of qualified forensic analysts, recognised certifications held (GCFE/GCIH/EnCE/CCFP), training frequency, analysis methodology documented, analysis always performed on copies (never originals), findings reproducible and documented, peer review of forensic reports, external forensic services engagement capability.

**Analysis Outcomes (Q61–Q65):** Percentage of incidents with root cause identified (last 10 requiring forensics), percentage of breach incidents with full attacker scope determined, IOCs systematically generated from forensic analysis, incident timelines accurately reconstructed, forensic findings actionable and fed into improvements.

### Compliance Checklist
```
☐ Forensic tools cover all evidence types collected (tool inventory matches collection capability)
☐ All forensic tools properly licensed and validated
☐ Analysis ALWAYS performed on forensic copies — originals never modified
☐ Peer review conducted on all forensic reports before finalisation
☐ At least 1 qualified forensic analyst available (2+ recommended)
☐ Analyst certifications current (renewed within validity period)
☐ External forensic retainer available if internal capacity exceeded
☐ IOCs generated from every forensic investigation and shared with detection team
```

---

## Sheet 5: Storage & Retention (15 Questions)

### Purpose
Assess the security, organisation, and lifecycle management of forensic evidence in storage — from secure placement through defined retention periods to secure disposal.

### Header
**Row 1:** "STORAGE & RETENTION"
**Row 2:** "Evidence Storage Security, Retention Policy, Disposal (15 Questions)"

### Column Definitions
Identical to Sheet 2 (A–G, same widths and types).

### Section Breakdown

**Evidence Storage (Q66–Q70):** Storage location type (dedicated server / cloud isolated / general share), access control model (strict role-based / basic / none), stored evidence encrypted, storage monitored for unauthorised access, evidence catalog maintained (searchable inventory).

**Retention Policy (Q71–Q75):** Retention periods defined per incident severity, retention periods comply with legal/regulatory requirements, retention policy documented and approved, retention periods reviewed annually, legal hold capability (suspend deletion on demand).

**Disposal (Q76–Q80):** Secure disposal procedure documented, disposal method appropriate per evidence type (cryptographic erasure / physical destruction), disposal authorisation required, disposal logged, disposal tested (verification that data is unrecoverable).

### Compliance Checklist
```
☐ Dedicated evidence storage (not co-located with production data)
☐ Access control: strict role-based, logged, justified
☐ All stored evidence encrypted at rest
☐ Retention periods defined, documented, and approved by Legal
☐ Legal hold capability tested (freeze + resume deletion)
☐ Secure disposal procedure tested — verified unrecoverable
☐ Disposal log maintained for audit trail
☐ Evidence catalog searchable by case, date, type, custodian
```

---

## Sheet 6: Legal & Regulatory Readiness (15 Questions)

### Purpose
Assess whether forensic evidence procedures meet legal admissibility standards and satisfy regulatory evidence requirements (GDPR breach notification, PCI DSS forensic investigation, etc.).

### Header
**Row 1:** "LEGAL & REGULATORY READINESS"
**Row 2:** "Admissibility, Regulatory Compliance, Expert Witness Capability (15 Questions)"

### Column Definitions
Identical to Sheet 2 (A–G, same widths and types).

### Section Breakdown

**Legal Readiness (Q81–Q87):** Evidence procedures reviewed by Legal, procedures meet court admissibility standards (jurisdiction-specific), expert witness capability available, forensic report template meets legal standards, legal hold integrated into evidence lifecycle, privilege protection considered during collection, cross-border evidence transfer procedures (if applicable).

**Regulatory Compliance (Q88–Q95):** GDPR Art. 33 evidence requirements met (breach notification within 72h), regulatory evidence retention periods documented, PCI DSS forensic investigation capability (if applicable), evidence provided to regulators within required timeframes, regulatory feedback on evidence quality tracked, multi-jurisdiction regulatory requirements mapped, evidence procedures aligned with applicable industry standards, regulatory evidence requirements reviewed annually.

### Compliance Checklist
```
☐ Evidence procedures reviewed and approved by Legal (within last 12 months)
☐ Procedures meet admissibility requirements for relevant jurisdiction(s)
☐ Expert witness capability available (internal or retained external)
☐ GDPR 72-hour breach notification timeline supported by evidence procedures
☐ Legal hold tested end-to-end (trigger → freeze → resume → dispose)
☐ Regulatory evidence requirements mapped for all applicable regulations
☐ Cross-border evidence transfer procedures documented (if multi-jurisdiction)
☐ Annual legal review of forensic evidence procedures scheduled
```

---

## Sheet 7: Gap Analysis (40 Capacity)

### Purpose
Consolidate all gaps flagged across Sheets 2–6. Prioritise by severity, assign owners, and track remediation.

### Header
**Row 1:** "GAP ANALYSIS"
**Row 2:** "Prioritised remediation tracking — transfer flagged gaps from assessment sheets"

### Column Definitions

| Column | Header | Width | Type | Description |
|--------|--------|-------|------|-------------|
| A | Gap_ID | 12 | Formula | Auto-numbered: `="GAP-"&TEXT(ROW()-6,"000")` |
| B | Source_Sheet | 28 | **User Input** (yellow) | Which sheet the gap originated from |
| C | Question_ID | 14 | **User Input** (yellow) | e.g. Q9, Q33 |
| D | Gap_Description | 55 | **User Input** (yellow) | Detailed description |
| E | Severity | 16 | **User Input** (yellow) | Dropdown: Critical / High / Medium / Low |
| F | Owner | 28 | **User Input** (yellow) | Name or role |
| G | Target_Date | 16 | **User Input** (yellow) | DD.MM.YYYY |
| H | Status | 18 | **User Input** (yellow) | Dropdown: Open / In Progress / Completed / Deferred |
| I | Remediation_Notes | 40 | **User Input** (yellow) | Free text |

### Summary Formulas (Rows 2–3, above headers)

```excel
Total Gaps:        =COUNTA(C7:C46)
Critical:          =COUNTIF(E7:E46,"Critical")
High:              =COUNTIF(E7:E46,"High")
Medium:            =COUNTIF(E7:E46,"Medium")
Open:              =COUNTIF(H7:H46,"Open")+COUNTIF(H7:H46,"In Progress")
Completed:         =COUNTIF(H7:H46,"Completed")
```

**Note:** S4 Gap Analysis includes the additional Medium count and Completed count compared to earlier domains — these are particularly relevant for forensic gaps where medium-severity items (e.g. tool validation gaps) accumulate and need tracking.

---

## Sheet 8: Evidence Register (60 Capacity)

### Purpose
Log all evidence collected to support this assessment and future audits.

### Header
**Row 1:** "EVIDENCE REGISTER"
**Row 2:** "Evidence supporting Forensic Evidence assessment"

### Column Definitions

| Column | Header | Width | Type | Description |
|--------|--------|-------|------|-------------|
| A | Evidence_ID | 14 | Formula | `="EV-"&TEXT(ROW()-4,"000")` |
| B | Related_Question | 18 | **User Input** (yellow) | Q-number(s) this evidence supports |
| C | Evidence_Type | 22 | **User Input** (yellow) | Dropdown: CoC Form / Forensic Report / Tool Licence / Hash Log / Training Record / Audit Log / Legal Review / Other |
| D | Description | 50 | **User Input** (yellow) | Free text — what the evidence contains |
| E | Source_Location | 40 | **User Input** (yellow) | File path, URL, or system reference |
| F | Collected_By | 22 | **User Input** (yellow) | Name |
| G | Collection_Date | 16 | **User Input** (yellow) | DD.MM.YYYY |
| H | Valid_Until | 16 | **User Input** (yellow) | DD.MM.YYYY (or "Ongoing") |

**Note:** Evidence_Type dropdown is S4-specific — CoC Form, Forensic Report, Hash Log are unique to this domain.

---

## Sheet 9: Dashboard

### Purpose
Three-panel automated summary: key forensic metrics, a live 10-source evidence coverage matrix, and gap counts.

### Header
**Row 1:** "FORENSIC EVIDENCE DASHBOARD"
**Row 2:** "ISMS-IMP-A.5.24-28.S4 — Coverage Matrix & Capability Summary"

### Panel 1: Key Forensic Metrics

| Metric | Source | Formula |
|--------|--------|---------|
| Collection Completeness % | Sheet 2, Q23 (% of types with procedures) | `='Evidence Collection'!D27` |
| CoC Completeness Rate % | Sheet 3, Q31 (CoC completeness in recent investigations) | `='Chain of Custody'!D35` |
| Root Cause ID Rate % | Sheet 4, Q61 (% with root cause identified) | `='Forensic Analysis'!D65` |
| Breach Scope Determination % | Sheet 4, Q62 | `='Forensic Analysis'!D66` |
| IOC Generation Rate | Sheet 4, Q63 | `='Forensic Analysis'!D67` |
| Analyst Count | Sheet 4, Q53 | `='Forensic Analysis'!D57` |
| Evidence Sources Covered | Calculated from Coverage Matrix | See Panel 2 formula |
| Gaps Logged | Sheet 7 | `=COUNTA('Gap Analysis'!C7:C46)` |

### Panel 2: Evidence Source Coverage Matrix

This is the signature feature of the S4 Dashboard. It pulls live from the Evidence Collection sheet (Q9–Q15 + coverage question) to show which of the 10 evidence source types have documented collection procedures, tested capability, and recent use.

**Matrix Structure:**

| Evidence Source | Procedure Exists | Capability Tested | Used in Last 12 Months | Coverage Status |
|----------------|-----------------|-------------------|------------------------|-----------------|
| 1. Disk | ✅/❌ | ✅/❌ | ✅/❌ | Green/Yellow/Red |
| 2. Memory | ✅/❌ | ✅/❌ | ✅/❌ | Green/Yellow/Red |
| 3. Network | ✅/❌ | ✅/❌ | ✅/❌ | Green/Yellow/Red |
| 4. Logs | ✅/❌ | ✅/❌ | ✅/❌ | Green/Yellow/Red |
| 5. Cloud | ✅/❌ | ✅/❌ | ✅/❌ | Green/Yellow/Red |
| 6. SaaS | ✅/❌ | ✅/❌ | ✅/❌ | Green/Yellow/Red |
| 7. Mobile | ✅/❌ | ✅/❌ | ✅/❌ | Green/Yellow/Red |
| 8. Email | ✅/❌ | ✅/❌ | ✅/❌ | Green/Yellow/Red |
| 9. Physical | ✅/❌ | ✅/❌ | ✅/❌ | Green/Yellow/Red |
| 10. IoT | ✅/❌ | ✅/❌ | ✅/❌ | Green/Yellow/Red |

**Coverage Status Logic:**
- **Green (Full Coverage):** Procedure exists AND capability tested AND used in last 12 months
- **Yellow (Partial):** Procedure exists but not tested OR not used recently
- **Red (Gap):** No procedure OR no capability

**Summary Formula:**
```excel
Sources Fully Covered:  =COUNTIF(CoverageStatusRange,"Full Coverage")
Sources Partially Covered: =COUNTIF(CoverageStatusRange,"Partial")
Sources Not Covered:    =COUNTIF(CoverageStatusRange,"Gap")
Overall Coverage %:     =Sources Fully Covered / 10 * 100
```

### Panel 3: Gap Summary

```excel
Total Gaps Flagged:     =COUNTIF('Evidence Collection'!G5:G29,"Yes")+COUNTIF('Chain of Custody'!G5:G24,"Yes")+COUNTIF('Forensic Analysis'!G5:G24,"Yes")+COUNTIF('Storage & Retention'!G5:G19,"Yes")+COUNTIF('Legal & Regulatory'!G5:G19,"Yes")
Critical Gaps:          =COUNTIF('Gap Analysis'!E7:E46,"Critical")
High Gaps:              =COUNTIF('Gap Analysis'!E7:E46,"High")
Gaps Requiring Action:  =[Total Gaps Flagged] - COUNTIF('Gap Analysis'!H7:H46,"Completed")
```

---

## Sheet 10: Approval Sign-Off

### Purpose
Formal review and approval workflow. **Legal review is recommended** before sign-off on this domain given the evidence admissibility implications.

### Structure

| Field | Type |
|-------|------|
| Assessment Reviewer Name | User Input (yellow) |
| Reviewer Role | User Input (yellow) |
| Review Date | User Input (yellow) |
| Legal Review Completed | Dropdown: Yes / No / Pending |
| Legal Reviewer Name (if Yes) | User Input (yellow) |
| Legal Review Date (if Yes) | User Input (yellow) |
| Review Comments | User Input (yellow, multi-line) |
| Approval Decision | Dropdown: Approved / Approved with conditions / Rejected |
| Next Review Date | User Input (yellow) |
| Next Review Responsible | User Input (yellow) |

**Note:** S4 Approval Sign-Off includes the Legal Review fields (Legal Review Completed, Legal Reviewer Name, Legal Review Date) which are unique to this domain — forensic evidence procedures have direct legal admissibility implications.

---

## Appendix A: Developer Technical Reference

### A.1 Workbook Structure Summary

| Sheet # | Name | Questions | Key Feature |
|---------|------|-----------|-------------|
| 1 | Instructions & Legend | — | Workflow guide, 10 evidence source types reference |
| 2 | Evidence Collection | 25 | Coverage across all 10 source types |
| 3 | Chain of Custody | 20 | Documentation, integrity (hashing), access control |
| 4 | Forensic Analysis | 20 | Tools, analysts, outcomes |
| 5 | Storage & Retention | 15 | Security, retention periods, disposal |
| 6 | Legal & Regulatory Readiness | 15 | Admissibility, regulatory compliance |
| 7 | Gap Analysis | 40 cap | Summary formulas at top (Total/Critical/High/Medium/Open/Completed) |
| 8 | Evidence Register | 60 cap | S4-specific evidence types (CoC forms, hash logs) |
| 9 | Dashboard | — | 3 panels: metrics, 10-source coverage matrix, gap summary |
| 10 | Approval Sign-Off | — | Includes Legal Review fields |

**Total Assessment Questions:** 95
**Freeze Panes:** Row 5 on all assessment sheets (headers stay visible)

### A.2 Data Validation Rules

**Answer Column (D) — Assessment Sheets:**

| Validation Set | Applied To | Values |
|----------------|-----------|--------|
| Procedure Quality | Q1, Q26, Q56, Q66, Q71, Q81 | Yes – Comprehensive / Yes – Basic / No |
| Integration | Q2 | Yes – Embedded in Playbooks / Yes – Separate Procedure / No |
| Multi-select (Evidence Types) | Q3 | Checkbox-style: Disk / Memory / Network / Logs / Cloud / SaaS / Mobile / Email / Physical / IoT |
| Yes/No | Q4, Q11, Q18, Q27, Q33, Q54, Q67, Q68, Q72, Q82 | Yes / No |
| Capability Level | Q6, Q9, Q10, Q12, Q16, Q32, Q46, Q47 | Capability-specific dropdowns (see sheet sections) |
| Duration | Q8 (collection procedure review cycle) | Quarterly / Semi-Annually / Annually / Never |
| Hash Algorithm | Q34 | SHA-256 / SHA-512 / MD5 (Legacy) / Multiple / None |
| Tool Type | Q47 | Commercial Only / Open-Source Only / Both / None |
| Certification | Q54 | GCFE/GCIH/EnCE/CCFP / Other Certs / No Certs |
| Percentage | Q23, Q61, Q62, Q90 | Free text number 0–100 |
| Number | Q53 (analyst count) | Free text number |
| Text | Q8 (review date), Q24 (engagement details) | Free text |

**Gap Analysis Sheet:**

| Column | Validation |
|--------|------------|
| E (Severity) | Critical / High / Medium / Low |
| H (Status) | Open / In Progress / Completed / Deferred |

**Evidence Register Sheet:**

| Column | Validation |
|--------|------------|
| C (Evidence_Type) | CoC Form / Forensic Report / Tool Licence / Hash Log / Training Record / Audit Log / Legal Review / Other |

**Approval Sign-Off:**

| Field | Validation |
|-------|------------|
| Legal Review Completed | Yes / No / Pending |
| Approval Decision | Approved / Approved with conditions / Rejected |

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

**Dashboard Coverage Matrix — Coverage Status Column:**
- Full Coverage → Green fill (#C6EFCE)
- Partial → Yellow fill (#FFEB9C)
- Gap → Red fill (#FFC7CE)

**Dashboard Key Metrics:**
- Collection Completeness ≥ 90% → Green; 70–89% → Yellow; < 70% → Red
- CoC Completeness ≥ 90% → Green; 70–89% → Yellow; < 70% → Red
- Root Cause ID Rate ≥ 85% → Green; 60–84% → Yellow; < 60% → Red

### A.4 Cell Protection

**Protected Cells (Formula / Static):**
- Column headers (row 4 on all assessment sheets)
- Question_ID (column A) and Question text (column C)
- Section labels (column B)
- Gap_Identified formulas (column G)
- Dashboard formulas, labels, and coverage matrix structure
- Gap Analysis ID formulas (column A) and summary formulas (rows 2–3)
- Evidence Register ID formulas (column A)

**Unprotected Cells (User Input — yellow fill):**
- Answer (column D), Evidence_Reference (column E), Comments (column F) on all assessment sheets
- All user-input columns on Gap Analysis and Evidence Register
- All fields on Approval Sign-Off
- Document information fields on Instructions & Legend
- Coverage matrix input fields on Dashboard (Procedure Exists / Capability Tested / Used in Last 12 Months)

**Sheet Protection:**
- Password: [Set during workbook generation]
- Allow: Format cells, Insert rows, Sort, Filter
- Disallow: Delete rows, Modify formulas, Unprotect sheet

### A.5 Gap_Identified Formula Logic

Applied to column G on every assessment sheet row:

```excel
=IF(OR(D5="No", D5="Limited", D5<80), "Yes", "No")
```

**Logic breakdown:**
- If Answer = "No" → gap flagged (capability absent)
- If Answer = "Limited" → gap flagged (insufficient capability)
- If Answer is a number < 80 → gap flagged (percentage below threshold — applies to Q23, Q61, Q62, Q90)
- All other answers → no gap

**Forensic-specific notes:**
- Hash algorithm = "MD5 (Legacy)" does NOT auto-flag as a gap via formula (MD5 is still a valid answer). However, assessors should manually note in Comments that MD5 is no longer considered sufficient for forensic integrity and flag for upgrade to SHA-256.
- Tool validation = "No" auto-flags. Unvalidated tools produce potentially inadmissible evidence — this is a Critical gap.

### A.6 Evidence Register Auto-Numbering

**Evidence ID Format:**
```excel
="EV-"&TEXT(ROW()-4,"000")
```
Produces: EV-001, EV-002, … EV-060

**Gap ID Format (Gap Analysis sheet — note offset differs from S3 due to summary rows):**
```excel
="GAP-"&TEXT(ROW()-6,"000")
```
Produces: GAP-001, GAP-002, … GAP-040

### A.7 Python Script Integration Points

**Workbook Generation Script:** `generate_a524_28_s4_forensic_evidence.py`

**Key Functions:**
- `create_workbook()`: Initialise workbook, create all 10 sheets
- `setup_styles()`: Define cell styles (header fill #003366, input fill #FFFFCC, calculated fill #E2EFDA, border)
- `create_assessment_sheet(ws, styles, title, subtitle, questions)`: Generic sheet generator — same pattern as S1–S3
- `create_evidence_collection(ws, styles)`: Sheet 2 — 25 questions across 5 sections
- `create_chain_of_custody(ws, styles)`: Sheet 3 — 20 questions across 3 sections
- `create_forensic_analysis(ws, styles)`: Sheet 4 — 20 questions across 3 sections
- `create_storage_retention(ws, styles)`: Sheet 5 — 15 questions across 3 sections
- `create_legal_regulatory(ws, styles)`: Sheet 6 — 15 questions across 2 sections
- `create_gap_analysis(ws, styles)`: Sheet 7 — 40-row capacity with 6 summary formulas at top
- `create_evidence_register(ws, styles)`: Sheet 8 — 60-row capacity, S4-specific evidence types
- `create_dashboard(ws, styles)`: Sheet 9 — 3 panels including 10-source coverage matrix
- `create_approval_signoff(ws, styles)`: Sheet 10 — includes Legal Review fields

**S4-Specific Enhancements vs S1–S3:**
- Gap Analysis sheet has summary formulas rendered above the header row (rows 2–3) — provides immediate visibility of total/critical/high/medium/open/completed counts without scrolling to Dashboard
- Dashboard coverage matrix is a 10×4 grid (10 evidence source types × Procedure/Tested/Used/Status) pulling live from Collection sheet responses
- Approval Sign-Off includes Legal Review fields (unique to S4)
- Evidence Register uses forensic-specific evidence types (CoC Form, Hash Log, Forensic Report)
- Gap ID formula offset is ROW()-6 (not ROW()-4) due to summary rows above the header

**Customisation Points (marked with `# CUSTOMIZE:` in script):**
- Evidence source types (if organisation uses different categorisation)
- Hash algorithm threshold (currently MD5 flagged as advisory, not auto-gap)
- Gap threshold value (currently 80 for percentage fields)
- Coverage matrix source type labels
- Legal review fields (can be removed if not applicable)
- Conditional formatting colour codes

**Quality Assurance:** After generation, verify:
- All 95 questions present across Sheets 2–6
- Coverage matrix on Dashboard correctly references Collection sheet cells
- Gap Analysis summary formulas at top return correct counts
- Gap ID formula produces GAP-001 starting from row 7 (not row 5)
- Legal Review fields present on Approval Sign-Off
- Evidence Register dropdown includes CoC Form, Hash Log, Forensic Report

### A.8 Version Control

**Workbook Versioning:**
- Filename format: `ISMS-IMP-A.5.24-28.S4_Forensic_Evidence_YYYYMMDD.xlsx`
- Version tracking in Instructions & Legend sheet
- Document Control section updated with each revision

**Change Log:**
- v1.0: Initial workbook structure — 10 sheets, 95 questions, 3-panel dashboard with coverage matrix

**Backward Compatibility:**
- v1.0 workbooks require Excel 2016+
- Previous assessments should be archived with date suffix before regenerating

---

## Document Assembly Instructions

**To create the complete ISMS-IMP-A.5.24-28.S4 v1.0 document:**

1. **Document Control** (from the S4 specification file header)
2. **PART I: USER COMPLETION GUIDE** (Assessment Overview through Assessment Timeline)
3. **PART II: TECHNICAL SPECIFICATION** (this section — Instructions through Appendix A.8)

**Final Document Structure:**
```
ISMS-IMP-A.5.24-28.S4 — Forensic Evidence Assessment v1.0

├── Document Control (Metadata, Version History, Related Documents)
│
├── PART I: USER COMPLETION GUIDE
│   ├── 1. Assessment Overview (Purpose, Scope, Prerequisites)
│   ├── 2. Assessment Workflow (High-Level Process, Timeline)
│   ├── 3. Section-by-Section Guidance (Q&A for all 95 questions)
│   ├── 4. Evidence Collection Guide
│   ├── 5. Common Mistakes to Avoid
│   └── 6. Assessment Timeline
│
└── PART II: TECHNICAL SPECIFICATION
    ├── Document Overview & Instructions
    ├── Sheet 1: Instructions & Legend
    ├── Sheet 2: Evidence Collection (25Q)
    ├── Sheet 3: Chain of Custody (20Q)
    ├── Sheet 4: Forensic Analysis (20Q)
    ├── Sheet 5: Storage & Retention (15Q)
    ├── Sheet 6: Legal & Regulatory Readiness (15Q)
    ├── Sheet 7: Gap Analysis (with summary formulas)
    ├── Sheet 8: Evidence Register (S4-specific types)
    ├── Sheet 9: Dashboard (3 panels + coverage matrix)
    ├── Sheet 10: Approval Sign-Off (with Legal Review fields)
    └── Appendix A (A.1–A.8: Developer Technical Reference)
```

**Quality Checks Before Finalising:**
- [ ] All 95 questions accounted for across sheet specifications
- [ ] Dashboard coverage matrix references correct Collection sheet cells
- [ ] Gap Analysis summary formulas reference correct row ranges (offset by summary rows)
- [ ] Gap ID formula uses ROW()-6 (not ROW()-4)
- [ ] Legal Review fields documented in Approval Sign-Off spec
- [ ] S4-specific Evidence Register types (CoC Form, Hash Log) included in validation rules
- [ ] MD5 advisory note documented in Gap formula logic section
- [ ] Cross-references to S1, S2, S3, S5 accurate
- [ ] ISMS-REF-A.5.24-28 Section 3 referenced throughout collection sections

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

**END OF DOCUMENT: ISMS-IMP-A.5.24-28.S4**

---

*"I would rather have questions that can't be answered than answers that can't be questioned."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-01 -->
