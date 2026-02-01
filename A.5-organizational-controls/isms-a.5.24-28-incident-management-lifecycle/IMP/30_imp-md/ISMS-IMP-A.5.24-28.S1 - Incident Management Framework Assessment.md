**ISMS-IMP-A.5.24-28.S1 — Incident Management Framework Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.24: Information Security Incident Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Incident Management Framework Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S1 |
| **Assessment Domain** | Domain 1 - Framework & Governance (A.5.24 Focus) |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Related Reference** | ISMS-REF-A.5.24-28 (Incident Response Reference Guide) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Incident Response Team Lead / CSIRT Manager |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CSIRT Manager | Initial framework assessment specification |

**Review Cycle**: Annual (or after major incident management changes)  
**Next Review Date**: [Effective Date + 12 months]  

**Related Documents**: 

- ISMS-POL-A.5.24-28 (Incident Management Lifecycle Policy)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide)
- ISMS-IMP-A.5.24-28.S2 (Detection & Classification Assessment)
- ISMS-IMP-A.5.24-28.S3 (Response Capabilities Assessment)
- ISMS-IMP-A.5.24-28.S4 (Forensic Evidence Assessment)
- ISMS-IMP-A.5.24-28.S5 (Learning & Improvement Assessment)
- ISO/IEC 27002:2022 Control A.5.24
- NIST SP 800-61 Rev. 2 (Computer Security Incident Handling Guide)


---

# PART I: USER COMPLETION GUIDE

# Assessment Overview

## Purpose

This assessment evaluates [Organization]'s **incident management framework and governance structure**, focusing on the **planning and preparation** phase of incident management (A.5.24).

**What This Assessment Covers:**

- Incident management governance (policies, procedures, authority)
- CSIRT/SOC organizational structure and staffing
- Role definitions, responsibilities, and RACI clarity
- Training and competency programs
- Tools and technology capabilities
- Integration with monitoring, logging, and other controls


**What This Assessment Does NOT Cover:**

- Incident classification and triage procedures (see ISMS-IMP-A.5.24-28.S2)
- Response execution and effectiveness (see ISMS-IMP-A.5.24-28.S3)
- Forensic evidence procedures (see ISMS-IMP-A.5.24-28.S4)
- Post-incident learning processes (see ISMS-IMP-A.5.24-28.S5)


**Assessment Output:**

- Excel workbook documenting incident management framework maturity
- Governance structure clarity assessment
- Training effectiveness evaluation
- Technology capability gaps
- Compliance scoring and gap analysis


## Why This Matters

**ISO/IEC 27001:2022 Control A.5.24 Requirement:**
> *"The organisation should plan and prepare for managing information security incidents by defining, establishing and communicating information security incident management processes, roles and responsibilities."*

**NIST SP 800-61 Guidance:**
> *"Establishing an incident response capability should include the following actions: creating an incident response policy and plan, developing procedures for performing incident handling and reporting, setting guidelines for communicating with outside parties regarding incidents, selecting a team structure and staffing model, and establishing relationships and lines of communication."*

**Business Impact of Poor Planning:**

- **Delayed Response:** Unclear roles delay incident containment (every minute counts)
- **Regulatory Violations:** GDPR 72-hour notification missed due to unclear procedures
- **Ineffective Response:** Untrained staff make mistakes, evidence destroyed
- **Legal Liability:** Poor forensic procedures render evidence inadmissible
- **Reputational Damage:** Public incidents handled poorly due to lack of preparation


**This Assessment Addresses:**

- Do we have clear, documented incident management procedures?
- Is our CSIRT/SOC properly structured and staffed?
- Are roles and responsibilities unambiguous?
- Is our team trained and competent?
- Do we have the tools needed for effective incident response?


## Who Should Complete This Assessment

**Primary Responsibility:** CSIRT Manager, SOC Manager, or Incident Response Team Lead

**Required Knowledge:**

- [Organization]'s incident management policies and procedures
- CSIRT/SOC team structure and staffing model
- Incident response training programs
- Incident response tools and technologies in use
- Integration points with monitoring (A.8.16), logging (A.8.15), and other controls


**Support Roles:**

- **CISO:** Governance framework, policy approval, budget authority
- **HR:** Staffing models, job descriptions, training records
- **IT Operations:** Tool integration, system access, escalation procedures
- **Legal/Compliance:** Regulatory requirements, breach notification procedures
- **External Partners:** Managed security service providers (MSSPs), incident response retainers


**Collaboration Required:**

- This is NOT a solo assessment
- Requires input from multiple stakeholders
- Review sessions with CSIRT, Legal, IT Ops, Management


## Time Estimate

**Total Assessment Time:** 8-12 hours (depending on organization size and complexity)

**Breakdown:**

- **Information Gathering:** 3-4 hours
  - Review incident management policy and procedures
  - Collect organizational charts, job descriptions, RACI matrices
  - Gather training records, exercise logs
  - Inventory incident response tools and integrations
  
- **Assessment Completion:** 3-4 hours
  - Complete governance assessment (policy, procedures, authority)
  - Document organizational structure and staffing
  - Assess training effectiveness
  - Evaluate tool capabilities
  - Complete integration assessment
  
- **Evidence Collection:** 1-2 hours
  - Screenshots of CSIRT charter, procedures
  - Organizational charts
  - Training records and certificates
  - Tool inventory and integration diagrams
  
- **Quality Review:** 1-2 hours
  - Gap analysis
  - Remediation planning
  - Management review and approval


**Complexity Factors:**

- **Simple (8 hours):** Small organization, dedicated CSIRT, well-documented procedures, mature tools
- **Moderate (10 hours):** Mid-size organization, part-time incident response, some documentation gaps
- **Complex (12+ hours):** Large organization, distributed teams, multiple locations, outsourced SOC, compliance complexity


## Connection to Policy

This assessment implements **ISMS-POL-A.5.24-28, Section 2.1 (Incident Management Planning & Preparation)** which defines mandatory requirements for:

**Governance Framework:**

- Incident management policy documented and approved
- Incident response procedures established
- Authority levels defined (escalation matrix)
- Exception management process
- Policy review and update cycle


**Organizational Structure:**

- CSIRT/SOC team established (dedicated, part-time, or outsourced)
- Roles and responsibilities clearly defined
- RACI matrix for incident lifecycle phases
- On-call rotation and escalation paths
- Integration with business units and management


**Training & Competency:**

- Annual incident response training for all staff
- Specialized training for CSIRT members
- Tabletop exercises conducted (minimum annually)
- Competency assessment and certification tracking
- New hire onboarding (incident reporting awareness)


**Tools & Technology:**

- Incident ticketing/tracking system
- SIEM integration for event detection
- Forensic tools and capabilities
- Communication platforms (internal, external)
- Threat intelligence integration


**Integration Points:**

- Logging (A.8.15): Incident investigations require comprehensive logs
- Monitoring (A.8.16): Event detection feeds incident pipeline
- Event Reporting (A.6.8): User reporting mechanism
- BC/DR (A.5.29-30): Major incidents trigger BC/DR activation
- Third-Party Management (A.5.19-23): Supplier incidents escalated appropriately


**Policy Authority:** Chief Information Security Officer (CISO)  
**Compliance Status:** Mandatory for all [Organization] information security incidents

## Assessment Scope

**Included in This Assessment:**

✅ **Governance:**

- Incident management policy existence and approval
- Procedure documentation completeness
- Authority matrix clarity
- Review and update frequency


✅ **Organizational Structure:**

- CSIRT/SOC team model (dedicated, virtual, outsourced)
- Staffing levels and coverage (24/7, business hours, on-call)
- Role definitions (Incident Manager, Analyst, Forensic Specialist, etc.)
- RACI matrix completeness


✅ **Training & Exercises:**

- Training program existence and delivery frequency
- Training content relevance (aligned with threat landscape)
- Tabletop exercise frequency and quality
- Competency tracking and certification


✅ **Tools & Technology:**

- Incident ticketing system capabilities
- SIEM integration status
- Forensic tool availability
- Communication platform readiness


✅ **Integration Assessment:**

- Integration with A.8.15 (Logging), A.8.16 (Monitoring)
- Integration with A.6.8 (User Event Reporting)
- Integration with A.5.29-30 (BC/DR)
- Third-party coordination (MSSPs, vendors)


**Excluded from This Assessment:**

❌ Incident detection and classification procedures (see S2)
❌ Response execution and effectiveness (see S3)
❌ Forensic evidence collection procedures (see S4)
❌ Post-incident review quality (see S5)
❌ Individual incident investigations (historical incident data analyzed in S3)

## Prerequisites

**Before Starting This Assessment:**

1. ✅ **Read Related Policy:**

   - ISMS-POL-A.5.24-28 Section 2.1 (Planning & Preparation Requirements)
   - Understand mandatory vs. recommended practices


2. ✅ **Gather Documentation:**

   - Incident management policy document
   - Incident response procedures/runbooks
   - CSIRT charter or SOC operating procedures
   - Organizational charts showing CSIRT reporting structure
   - Job descriptions for incident response roles
   - RACI matrix (if exists)
   - Training records (courses, exercises, certifications)
   - Tool inventory (ticketing system, SIEM, forensic tools)


3. ✅ **Identify Stakeholders:**

   - CSIRT/SOC Manager (primary assessor)
   - CISO (governance, budget, authority)
   - HR (staffing, training records)
   - IT Ops (tool integration, on-call rotation)
   - Legal/Compliance (regulatory requirements, breach notification)


4. ✅ **Schedule Review Sessions:**

   - CSIRT team review (validate structure, roles)
   - Management review (governance, budget, staffing)
   - Legal review (regulatory compliance, notification procedures)


5. ✅ **Prepare Evidence Folder:**

   - Create folder: `/Evidence/A.5.24-28/S1_Framework/`
   - Collect documents, screenshots, training records
   - Organize by assessment section (Governance, Structure, Training, Tools)


---

# Assessment Workflow

## High-Level Process

**Step-by-Step Assessment Flow:**

```
1. Information Gathering (3-4 hours)
   ├── Review incident management policy and procedures
   ├── Collect organizational charts and role definitions
   ├── Gather training records and exercise logs
   └── Inventory tools and integrations

2. Assessment Completion (3-4 hours)
   ├── Section A: Governance Assessment (policy, procedures, authority)
   ├── Section B: Organizational Structure (CSIRT model, staffing, roles)
   ├── Section C: Training & Competency (programs, exercises, tracking)
   ├── Section D: Tools & Technology (capabilities, integrations)
   └── Section E: Integration Assessment (logging, monitoring, BC/DR)

3. Gap Analysis (1 hour)
   ├── Identify missing or incomplete elements
   ├── Prioritize gaps by risk
   └── Develop remediation recommendations

4. Evidence Collection (1-2 hours)
   ├── Screenshots and document exports
   ├── Training records and certificates
   └── Tool configuration evidence

5. Quality Review (1-2 hours)
   ├── Self-assessment against policy requirements
   ├── Peer review (CSIRT team)
   └── Management review

6. Approval Workflow (1 week)
   ├── CSIRT Manager approval
   ├── CISO review and approval
   └── Document filing and next review scheduling
```

## Assessment Sections Overview

**The workbook contains the following sections:**

**Sheet 1: Instructions & Legend**

- Assessment overview
- How to complete the workbook
- Color coding and validation rules
- Evidence reference system


**Sheet 2: Governance Assessment**

- Incident management policy documentation
- Procedure completeness
- Authority matrix and escalation
- Policy review frequency
- Regulatory compliance alignment


**Sheet 3: Organizational Structure**

- CSIRT/SOC team model (dedicated, virtual, hybrid, outsourced)
- Staffing levels and coverage (24/7, business hours, on-call)
- Role definitions (15-20 common incident response roles)
- RACI matrix assessment
- Reporting structure and management visibility


**Sheet 4: Training & Competency**

- Training program existence and content
- Training delivery frequency and format
- Tabletop exercise schedule and quality
- Competency tracking and certifications
- New hire onboarding (incident reporting awareness)


**Sheet 5: Tools & Technology**

- Incident ticketing/tracking system assessment
- SIEM integration status
- Forensic tool availability
- Communication platforms
- Threat intelligence integration
- Automation capabilities (playbooks, SOAR)


**Sheet 6: Integration Assessment**

- Integration with logging (A.8.15)
- Integration with monitoring (A.8.16)
- Integration with user event reporting (A.6.8)
- Integration with BC/DR (A.5.29-30)
- Third-party coordination (suppliers, MSSPs)


**Sheet 7: Gap Analysis**

- Framework maturity scoring
- Gap prioritization (Critical, High, Medium, Low)
- Remediation recommendations
- Timeline and ownership


**Sheet 8: Evidence Register**

- Evidence inventory (100 items capacity)
- Evidence types (policy documents, org charts, training records, tool screenshots)
- Storage locations
- Verification status


**Sheet 9: Dashboard**

- Overall framework maturity score
- Governance compliance percentage
- Staffing adequacy assessment
- Training effectiveness score
- Tool capability score
- Integration completeness
- Top 10 gaps summary


**Sheet 10: Approval Sign-Off**

- Assessment summary
- CSIRT Manager approval
- CISO approval
- Next review date


---

# Section-by-Section Guidance

## Sheet 2: Governance Assessment

**Purpose:** Document and assess incident management governance framework

**Assessment Questions (25 questions):**

---

### **Section A: Policy Documentation**

**Q1: Policy_Exists**

- **Question:** Does [Organization] have a documented incident management policy?
- **Dropdown:** Yes / No / In Draft
- **Evidence Expected:**
  - ISMS-POL-A.5.24-28 (or equivalent incident management policy document)
  - Policy approval record
  - Version and effective date
- **Auditor Will Verify:**
  - Policy document exists and is approved
  - Policy covers all 5 incident lifecycle phases (Planning, Assessment, Response, Learning, Evidence)
  - Policy is accessible to relevant staff
- **If "No" or "In Draft":**
  - **Gap:** CRITICAL - No approved incident management policy
  - **Remediation:** Develop and approve ISMS-POL-A.5.24-28 immediately
  - **Timeline:** High priority (within 30 days)


**Q2: Policy_Approval_Date**

- **Question:** When was the current incident management policy approved?
- **Format:** Date (DD.MM.YYYY)
- **Acceptance Criteria:**
  - Policy approved within last 12 months (preferred)
  - Policy approved within last 24 months (acceptable)
  - Policy >24 months old → DUE FOR REVIEW
- **Evidence:** Policy approval record (signature page, approval email, board minutes)


**Q3: Policy_Owner**

- **Question:** Who is the designated owner of the incident management policy?
- **Format:** Free text (Name, Title)
- **Best Practice:** Chief Information Security Officer (CISO)
- **Auditor Expects:** Policy owner has authority to:
  - Approve policy updates
  - Allocate resources (budget, staffing)
  - Enforce compliance
- **Evidence:** Policy document header, job description, organizational chart


**Q4: Policy_Review_Frequency**

- **Question:** How often is the incident management policy reviewed?
- **Dropdown:** Annually / Bi-Annually / Quarterly / Ad-Hoc / Not Defined
- **Requirement (ISMS-POL-A.5.24-28):** Annual minimum
- **Best Practice:** Annual scheduled + triggered reviews (major incidents, regulatory changes)
- **If "Ad-Hoc" or "Not Defined":**
  - **Gap:** Policy review not systematic
  - **Risk:** Policy becomes outdated, non-compliance with regulations
  - **Remediation:** Establish annual review schedule


**Q5: Last_Policy_Review_Date**

- **Question:** When was the policy last reviewed?
- **Format:** Date (DD.MM.YYYY)
- **Cross-Check:** Should align with Q2 (Approval Date) or more recent
- **Red Flag:** Last review >12 months ago → OVERDUE
- **Evidence:** Review meeting minutes, policy change log, version history


---

### **Section B: Procedure Documentation**

**Q6: Procedures_Documented**

- **Question:** Are incident response procedures documented?
- **Dropdown:** Yes - Comprehensive / Yes - Partial / No / In Development
- **Comprehensive Means:**
  - Procedures cover all incident lifecycle phases
  - Procedures include step-by-step instructions
  - Procedures reference tools, contacts, escalation paths
  - Procedures regularly updated
- **Evidence Expected:**
  - Incident response runbooks/playbooks
  - Procedures for common incident types (malware, data breach, DoS, unauthorized access)
  - Escalation procedures
  - Communication procedures (internal, external, regulatory)
  - Evidence collection procedures


**Q7: Procedure_Format**

- **Question:** In what format are incident response procedures documented?
- **Checkbox (multiple selections allowed):**
  - ☐ Written procedures (Word, PDF, Wiki)
  - ☐ Flowcharts / process diagrams
  - ☐ Automated playbooks (SOAR, runbook automation)
  - ☐ Tabletop exercise scenarios
  - ☐ Other (specify)
- **Best Practice:** Multiple formats for different audiences:
  - Written procedures for reference
  - Flowcharts for quick decision-making during incident
  - Automated playbooks for common responses


**Q8: Procedure_Accessibility**

- **Question:** Where are incident response procedures stored and how are they accessed?
- **Format:** Free text
- **Examples:**
  - "SharePoint site: /CSIRT/Procedures/ (access restricted to CSIRT members)"
  - "Confluence wiki: https://wiki.example.com/incident-response"
  - "SOAR platform: Integrated playbooks"
  - "Physical binder in SOC + digital copy on shared drive"
- **Auditor Will Verify:**
  - Procedures accessible during incident (even if primary systems down)
  - Access controls appropriate (need-to-know basis)
  - Version control maintained


**Q9: Procedures_Include_Contacts**

- **Question:** Do procedures include up-to-date contact information (CSIRT, management, legal, external partners)?
- **Dropdown:** Yes - Current / Yes - Outdated / No
- **Critical for:**
  - Escalation during incidents
  - Regulatory breach notification (Legal, DPO)
  - Third-party coordination (MSSP, incident response retainer, law enforcement)
- **If "Outdated" or "No":**
  - **Gap:** HIGH - Communication delays during incident
  - **Remediation:** Update contact list quarterly, verify before each exercise


**Q10: Procedures_Last_Updated**

- **Question:** When were incident response procedures last updated?
- **Format:** Date (DD.MM.YYYY)
- **Best Practice:** Updated annually + after major incidents (lessons learned)
- **Red Flag:** Procedures >12 months old without review
- **Evidence:** Procedure version history, change log


---

### **Section C: Authority & Escalation**

**Q11: Incident_Declaration_Authority**

- **Question:** Who has authority to declare a security incident?
- **Format:** Free text (role/title)
- **Common Models:**
  - **Model 1 (Empowered CSIRT):** Any CSIRT member can declare incident → Fast response
  - **Model 2 (SOC Lead):** SOC Manager or senior analyst declares → Quality control
  - **Model 3 (Management Approval):** CISO or IT Director approves → Slower but risk-averse
- **Best Practice:** Empower CSIRT to declare incidents; management informed via escalation
- **Auditor Expects:** Clear authority documented in policy/procedures


**Q12: Escalation_Matrix_Exists**

- **Question:** Is there a documented escalation matrix defining when and to whom incidents are escalated?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No
- **Comprehensive Escalation Matrix Includes:**
  - Severity levels (Critical, High, Medium, Low)
  - Escalation triggers (severity, impact, regulatory breach)
  - Escalation paths (SOC Analyst → SOC Manager → CISO → CIO → CEO/Board)
  - Timeframes (immediate, 1 hour, 4 hours, 24 hours)
  - Notification methods (phone, email, SMS, incident platform)
- **Evidence:** Escalation matrix document, decision tree, flowchart


**Q13: Management_Notification_Criteria**

- **Question:** What criteria trigger executive management notification?
- **Format:** Free text
- **Common Triggers:**
  - **Critical severity incidents:** Ransomware, data breach (Restricted/Confidential data), major system outage
  - **Regulatory breach notification required:** GDPR, Swiss nDSG, PCI DSS, sector-specific
  - **Potential legal action:** Law enforcement involvement, subpoena
  - **Media/public attention:** Reputational risk
  - **Financial impact:** Revenue loss, fines, remediation costs >$X threshold
- **Best Practice:** Defined thresholds prevent over-escalation (alert fatigue) and under-escalation (management surprised)


**Q14: Board_Notification_Criteria**

- **Question:** What criteria trigger Board of Directors notification?
- **Format:** Free text
- **Typical Triggers:**
  - Material incidents (significant financial, operational, or reputational impact)
  - Regulatory breach with potential fines or enforcement action
  - Systemic failure or control breakdown
  - Major data breach (>10,000 records, sensitive data)
- **Note:** Many organizations include Board notification in BC/DR activation criteria


**Q15: External_Notification_Procedures**

- **Question:** Are procedures defined for external notifications (regulators, law enforcement, customers, media)?
- **Dropdown:** Yes - Documented / Partially Documented / No
- **External Parties:**
  - **Regulators:** GDPR supervisory authority, Swiss FDPIC, PCI DSS payment brands, sector-specific (FINMA, NIS2 CSIRT)
  - **Law Enforcement:** Cybercrime units, FBI (if US presence), Europol
  - **Customers/Partners:** Breach notification if customer data affected
  - **Media:** Public relations, press releases (if material breach)
- **Evidence:** External communication procedures, notification templates, contact lists
- **Legal Review:** External communications often require Legal/PR approval


---

### **Section D: Regulatory Compliance Alignment**

**Q16: Regulatory_Requirements_Identified**

- **Question:** Have applicable regulatory incident notification requirements been identified?
- **Dropdown:** Yes - Documented / Partially / No
- **Regulations to Consider (per ISMS-POL-00):**
  - **Tier 1 Mandatory:** GDPR, Swiss nDSG, ISO 27001
  - **Tier 2 Conditional:** PCI DSS, FINMA, DORA, NIS2, HIPAA (if applicable)
- **Reference:** ISMS-POL-A.5.24-28 Section 1.5, ISMS-REF-A.5.24-28 Section 2
- **Evidence:** Regulatory requirements matrix, notification timelines documented


**Q17: GDPR_Breach_Notification_Procedure**

- **Question:** (If GDPR applies) Is GDPR 72-hour breach notification procedure documented?
- **Dropdown:** Yes / No / N/A (GDPR not applicable)
- **GDPR Requirements:**
  - 72-hour notification to supervisory authority (Art. 33)
  - Data subject notification if high risk (Art. 34)
  - Breach register maintained (Art. 33(5))
- **Evidence:**
  - GDPR breach notification procedure
  - Breach assessment decision tree
  - Notification templates (supervisory authority, data subjects)
  - DPO contact information
- **Auditor Will Verify:** Procedure includes all GDPR-required information (nature, categories, consequences, measures)


**Q18: Swiss_nDSG_Breach_Notification_Procedure**

- **Question:** (If Swiss nDSG applies) Is Swiss nDSG breach notification procedure documented?
- **Dropdown:** Yes / No / N/A (nDSG not applicable)
- **nDSG Requirements:**
  - Notification to FDPIC "as soon as possible" if high risk (Art. 24)
  - High risk = threat to personality or fundamental rights
- **Evidence:**
  - nDSG breach notification procedure
  - Risk assessment criteria (high risk determination)
  - FDPIC contact information
  - Notification template


**Q19: PCI_DSS_Incident_Reporting_Procedure**

- **Question:** (If PCI DSS applies) Is PCI DSS incident reporting procedure documented?
- **Dropdown:** Yes / No / N/A (PCI DSS not applicable)
- **PCI DSS Requirements:**
  - Immediate notification to payment brands and acquiring bank
  - PFI (PCI Forensic Investigator) engagement if account data compromise suspected
  - Forensic investigation and remediation
- **Evidence:**
  - PCI DSS incident reporting procedure
  - Payment brand contact information (Visa, Mastercard, Amex)
  - Acquiring bank contact
  - PFI list and engagement procedure


**Q20: Sector_Specific_Requirements**

- **Question:** Are sector-specific incident reporting requirements documented (FINMA, DORA, NIS2, HIPAA, etc.)?
- **Dropdown:** Yes / No / N/A (no sector-specific requirements)
- **Sector-Specific Examples:**
  - **FINMA (Swiss financial):** Significant operational incident reporting
  - **DORA (EU financial):** Major ICT incident reporting (4h/72h/1 month)
  - **NIS2 (EU critical infrastructure):** Significant incident reporting (24h/72h/1 month)
  - **HIPAA (US healthcare):** Breach notification (60 days)
- **Reference:** ISMS-POL-00 Tier 2 conditional regulations
- **Evidence:** Sector-specific notification procedures, authority contacts


---

### **Section E: Exception Management**

**Q21: Exception_Process_Defined**

- **Question:** Is there a process for exceptions to incident management requirements?
- **Dropdown:** Yes / No
- **Exception Examples:**
  - Certain low-risk systems excluded from 24/7 monitoring
  - Specific incident types escalated differently (business justification)
  - Third-party managed services with different procedures
- **Exception Process Should Include:**
  - Exception request and justification
  - Risk assessment
  - Approval authority (typically CISO)
  - Documentation and review
  - Expiration/renewal


**Q22: Exceptions_Documented**

- **Question:** Are current exceptions documented and approved?
- **Dropdown:** Yes / No / N/A (no exceptions)
- **Evidence:** Exception register, approval records
- **Auditor Will Verify:**
  - Exceptions have valid business justification
  - Risk assessed and accepted
  - Approved by appropriate authority
  - Reviewed periodically


---

### **Section F: Policy Governance**

**Q23: Policy_Communication**

- **Question:** How is the incident management policy communicated to staff?
- **Checkbox (multiple selections):**
  - ☐ Published in ISMS document repository
  - ☐ Included in new hire onboarding
  - ☐ Annual security awareness training
  - ☐ CSIRT-specific training
  - ☐ Email announcement to all staff
  - ☐ Manager briefings
  - ☐ Other (specify)
- **Best Practice:** Multi-channel communication ensuring all staff know:
  - How to report security incidents (A.6.8 integration)
  - What constitutes a security incident
  - Expectation to report promptly


**Q24: Policy_Accessible_to_Staff**

- **Question:** Can relevant staff easily access the incident management policy?
- **Dropdown:** Yes - Widely Accessible / Yes - Restricted Access / No - Difficult to Access
- **Accessibility Considerations:**
  - Published on intranet or document portal
  - Searchable by keyword
  - No unnecessary access restrictions (balance security with usability)
  - Available offline (for major incidents affecting primary systems)


**Q25: Next_Policy_Review_Date**

- **Question:** When is the next scheduled policy review?
- **Format:** Date (DD.MM.YYYY)
- **Calculation:** Last review date + 12 months
- **Action:** Set calendar reminder 30 days before review date
- **Evidence:** Policy review schedule, meeting invitations


---

## Sheet 3: Organizational Structure

**Purpose:** Document CSIRT/SOC structure, staffing, roles, and responsibilities

**Assessment Questions (30 questions):**

---

### **Section A: CSIRT/SOC Model**

**Q26: Incident_Response_Model**

- **Question:** What incident response organizational model does [Organization] use?
- **Dropdown:**
  - Dedicated CSIRT (full-time incident response team)
  - Virtual CSIRT (part-time, members from different departments)
  - Hybrid (core dedicated staff + virtual team members)
  - Outsourced SOC/MSSP (Managed Security Service Provider)
  - Coordinated (decentralized, regional teams)
- **Model Characteristics:**
  

  **Dedicated CSIRT:**

  - Full-time incident response professionals
  - 24/7 coverage (shifts or on-call)
  - Deep expertise, fast response
  - Higher cost
  - Best for: Large organizations, high incident volume, regulated industries
  

  **Virtual CSIRT:**

  - IT, Security, Legal, HR members activated during incidents
  - Day jobs + incident response duties
  - Cost-effective but slower response
  - Best for: Small/mid-size organizations, low incident volume
  

  **Hybrid:**

  - Core SOC team (detection, triage) + CSIRT (investigation, remediation)
  - Balances cost and capability
  - Best for: Mid-large organizations
  

  **Outsourced SOC/MSSP:**

  - Third-party provides monitoring, detection, initial response
  - Internal team handles escalation, remediation, communication
  - Cost-effective for 24/7 coverage
  - Best for: Organizations without resources for full SOC
  

  **Coordinated:**

  - Multiple regional/business unit teams
  - Central coordination (CISO office)
  - Best for: Global organizations, decentralized IT


**Q27: CSIRT_Establishment_Date**

- **Question:** When was the CSIRT/SOC team established?
- **Format:** Date (MM.YYYY) or "Not formally established"
- **Maturity Indicator:**
  - <1 year: New team, likely building processes
  - 1-3 years: Maturing, refining procedures
  - 3-5 years: Established, optimizing
  - >5 years: Mature, industry-leading (if continuously improved)


**Q28: CSIRT_Coverage**

- **Question:** What coverage does the CSIRT/SOC provide?
- **Dropdown:**
  - 24/7/365 (round-the-clock coverage)
  - Business hours only (e.g., 08:00-18:00 Mon-Fri)
  - Extended hours (e.g., 06:00-22:00 Mon-Fri)
  - On-call rotation (business hours + on-call after hours)
- **Requirement:** Dependent on risk assessment, regulatory requirements, business criticality
- **Best Practice:**
  - Critical systems, regulated industries → 24/7 coverage
  - Small organizations, low risk → Business hours + on-call acceptable
- **Auditor Will Verify:** Coverage aligns with risk assessment and business requirements


**Q29: CSIRT_Staffing_Level**

- **Question:** How many full-time equivalent (FTE) staff are dedicated to incident response?
- **Format:** Number (FTE count)
- **Benchmarking (rough guidance):**
  - **Small org (<500 employees):** 1-2 FTE (virtual team acceptable)
  - **Mid-size (500-5000):** 3-5 FTE (hybrid model)
  - **Large (5000+):** 5-20+ FTE (dedicated CSIRT + SOC)
- **Note:** FTE = full-time equivalent. Part-time staff counted proportionally (e.g., 2 people at 50% = 1 FTE)
- **Cross-Check:** Does staffing support stated coverage (Q28)?
  - 24/7 coverage typically requires 4-5 FTE per role (to cover shifts, vacation, training)


**Q30: CSIRT_Reporting_Structure**

- **Question:** To whom does the CSIRT/SOC team report?
- **Format:** Free text (Title/Department)
- **Common Structures:**
  - **Reports to CISO:** Most common, direct security authority
  - **Reports to CIO/IT Director:** Risk if security priorities conflict with IT operations
  - **Reports to COO/CRO:** Enterprise risk management alignment
  - **Independent (reports to CEO/Board):** Rare, maximum independence
- **Best Practice:** Report to CISO for security autonomy
- **Auditor Consideration:** Independence from IT operations (separation of duties)


---

### **Section B: Role Definitions**

**Q31-Q45: Role Definition Assessment (15 Common Roles)**

For each role, document:

- **Role_Exists:** Yes / No
- **Role_Definition:** Brief description or reference to job description
- **Assigned_To:** Name(s) or "Vacant"
- **RACI_Clarity:** Clear / Unclear / Not Documented


**Q31: Incident_Manager**

- **Description:** Leads incident response, coordinates teams, communicates with management
- **Typical Responsibilities:**
  - Declare incidents (or approve declaration)
  - Coordinate response activities
  - Manage escalation and communication
  - Approve incident closure
- **RACI:** Responsible for incident lifecycle management
- **Common Mistakes:** Incident Manager also performing technical investigation (role conflict)


**Q32: SOC_Analyst_Tier_1**

- **Description:** First-line event monitoring, triage, initial classification
- **Typical Responsibilities:**
  - Monitor SIEM alerts
  - Perform initial triage (event vs. incident)
  - Create incident tickets
  - Escalate to Tier 2 or CSIRT
- **RACI:** Responsible for event detection and initial assessment
- **Skill Level:** Junior to mid-level, broad security knowledge


**Q33: SOC_Analyst_Tier_2**

- **Description:** Incident investigation, deeper analysis, threat hunting
- **Typical Responsibilities:**
  - Investigate escalated incidents
  - Perform log analysis, PCAP review
  - Identify IOCs (Indicators of Compromise)
  - Recommend containment actions
- **RACI:** Responsible for incident investigation
- **Skill Level:** Mid to senior, specialized security skills


**Q34: Forensic_Specialist**

- **Description:** Digital forensics, evidence collection and preservation
- **Typical Responsibilities:**
  - Collect forensic evidence (disk, memory, network)
  - Maintain chain of custody
  - Perform forensic analysis
  - Prepare forensic reports for legal
- **RACI:** Responsible for evidence collection (A.5.28)
- **Skill Level:** Senior, specialized forensic training/certification
- **Note:** May be outsourced (forensic retainer, law enforcement)


**Q35: Malware_Analyst**

- **Description:** Malware reverse engineering and analysis
- **Typical Responsibilities:**
  - Analyze malware samples
  - Identify malware capabilities (C2, exfiltration, persistence)
  - Develop detection signatures (YARA, IDS)
  - Recommend remediation
- **RACI:** Responsible for malware analysis
- **Skill Level:** Senior, specialized reverse engineering skills
- **Note:** Often outsourced or shared resource


**Q36: Threat_Intelligence_Analyst**

- **Description:** Threat intelligence collection, analysis, and dissemination
- **Typical Responsibilities:**
  - Monitor threat intelligence feeds
  - Analyze threat actor TTPs (Tactics, Techniques, Procedures)
  - Provide context for incidents (attribution, campaign)
  - Update detection rules based on emerging threats
- **RACI:** Consulted for threat context during incidents
- **Skill Level:** Mid to senior, intelligence analysis background helpful


**Q37: Communication_Coordinator**

- **Description:** Manages internal and external communications during incidents
- **Typical Responsibilities:**
  - Draft management briefings
  - Coordinate with Legal, PR, HR
  - Prepare regulatory notifications (GDPR, PCI DSS)
  - Manage customer communications
- **RACI:** Responsible for incident communications
- **Skill Level:** Mid-level, strong writing and stakeholder management
- **Note:** Often filled by CISO, Legal, or PR (depending on incident severity)


**Q38: Legal_Representative**

- **Description:** Provides legal guidance during incidents (privilege, breach notification, law enforcement)
- **Typical Responsibilities:**
  - Advise on regulatory notification requirements
  - Coordinate with law enforcement
  - Manage legal hold and evidence preservation
  - Assess litigation risk
- **RACI:** Consulted for legal matters, Accountable for breach notifications
- **Skill Level:** Legal counsel (in-house or external)
- **Note:** May be Data Protection Officer (DPO) for GDPR matters


**Q39: HR_Representative**

- **Description:** HR liaison for insider threat, employee termination, personnel matters
- **Typical Responsibilities:**
  - Coordinate employee terminations (disable access)
  - Support insider threat investigations (employee interviews)
  - Manage disciplinary actions
  - Provide HR policy guidance
- **RACI:** Consulted for personnel-related incidents
- **Note:** Particularly important for insider threat (A.5.15-16-18 integration)


**Q40: IT_Operations_Liaison**

- **Description:** IT Ops representative for system access, configuration, recovery
- **Typical Responsibilities:**
  - Provide system access for investigation
  - Execute containment actions (isolate systems, block IPs)
  - Perform system restoration and patching
  - Coordinate change management during incident
- **RACI:** Responsible for operational response actions
- **Note:** CSIRT identifies what needs to be done; IT Ops executes


**Q41: Business_Unit_Liaison**

- **Description:** Business representative for impact assessment, communication, continuity
- **Typical Responsibilities:**
  - Assess business impact of incident
  - Communicate with affected business users
  - Coordinate workarounds or alternative processes
  - Support BC/DR activation if needed
- **RACI:** Consulted for business impact, Informed of incident status
- **Note:** Critical for business-impacting incidents (ransomware, outages)


**Q42: Third_Party_Coordinator**

- **Description:** Manages third-party involvement (vendors, suppliers, MSSP)
- **Typical Responsibilities:**
  - Coordinate with MSSPs or outsourced SOC
  - Engage incident response retainers (if contracted)
  - Manage vendor notifications (if supplier incident affects [Organization])
  - Track vendor SLAs for incident support
- **RACI:** Responsible for third-party coordination
- **Note:** May be Procurement, Vendor Management, or CISO office


**Q43: Executive_Sponsor**

- **Description:** Executive-level sponsor for CSIRT (budget, authority, escalation)
- **Typical Role:** CISO, CIO, CRO (Chief Risk Officer)
- **Typical Responsibilities:**
  - Provide CSIRT budget and resources
  - Remove organizational blockers
  - Escalation point for critical incidents
  - Board reporting for material incidents
- **RACI:** Accountable for incident management capability
- **Note:** Executive sponsor ≠ involved in every incident (only escalated incidents)


**Q44: On_Call_Engineer**

- **Description:** After-hours on-call rotation for incident response
- **Typical Responsibilities:**
  - Respond to after-hours alerts
  - Perform initial triage and escalation
  - Coordinate emergency response (if Critical incident)
- **RACI:** Responsible for after-hours coverage
- **Note:** Should have documented on-call procedures, escalation contacts, runbooks


**Q45: Other_Roles**

- **Question:** Are there additional incident response roles specific to [Organization]?
- **Format:** Free text (list roles)
- **Examples:**
  - Cloud Security Specialist (for cloud-native incidents)
  - OT/ICS Security Engineer (for operational technology/SCADA incidents)
  - Regulatory Compliance Officer (for highly regulated industries)
  - Customer Support Liaison (for customer-facing incidents)


---

### **Section C: RACI Matrix Assessment**

**Q46: RACI_Matrix_Exists**

- **Question:** Is there a documented RACI matrix for incident management roles?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No
- **RACI Matrix Purpose:**
  - **R** = Responsible (does the work)
  - **A** = Accountable (decision authority, approves)
  - **C** = Consulted (provides input)
  - **I** = Informed (kept updated)
- **Comprehensive RACI Matrix Covers:**
  - All incident lifecycle phases (Detection, Classification, Response, Evidence, Learning)
  - All key roles (15-20 roles documented)
  - Clear assignment (one "A" per activity, one or more "R")
- **Evidence:** RACI matrix document, table, or flowchart


**Q47: RACI_Clarity_Assessment**

- **Question:** Overall, are roles and responsibilities clear and unambiguous?
- **Dropdown:** Yes - Very Clear / Mostly Clear / Some Ambiguity / Significant Confusion
- **Indicators of Clarity:**
  - Staff can explain their responsibilities without referring to documents
  - No "that's not my job" disputes during incidents
  - Clear escalation path (everyone knows who to contact)
- **Indicators of Ambiguity:**
  - Overlapping responsibilities (multiple people think they're Accountable)
  - Gaps (activities with no Responsible party)
  - Role confusion during tabletop exercises


**Q48: RACI_Last_Updated**

- **Question:** When was the RACI matrix last reviewed/updated?
- **Format:** Date (DD.MM.YYYY) or "Never updated"
- **Best Practice:** Review annually + after organizational changes
- **Trigger Events for RACI Update:**
  - Staffing changes (new hires, departures, reorganization)
  - Process changes (new tools, procedures)
  - Major incidents revealing role confusion


---

### **Section D: Staffing Adequacy**

**Q49: Staffing_Adequate_for_Coverage**

- **Question:** Is current staffing adequate to support stated coverage (Q28)?
- **Dropdown:** Yes / No / Barely Adequate
- **Assessment Criteria:**
  - 24/7 coverage: Typically requires 4-5 FTE per shift role (covering shifts, vacation, sick leave, training)
  - On-call rotation: Reasonable frequency (not same person on-call 24/7/365)
  - Incident surge capacity: Can team handle multiple simultaneous incidents?
- **If "No" or "Barely Adequate":**
  - **Gap:** Staffing inadequacy risks burnout, slow response, missed incidents
  - **Remediation:** Increase FTE, adjust coverage model, or engage MSSP


**Q50: Turnover_Rate**

- **Question:** What is the CSIRT/SOC annual turnover rate?
- **Format:** Percentage (e.g., 20%)
- **Calculation:** (Departures in last 12 months / Average team size) × 100
- **Benchmarking:**
  - <10%: Excellent retention
  - 10-20%: Industry average for security roles
  - 20-30%: High turnover, investigate causes
  - >30%: Critical issue (burnout, compensation, culture)
- **High Turnover Impacts:**
  - Loss of institutional knowledge
  - Training costs for replacements
  - Reduced incident response effectiveness
  - Morale issues


**Q51: Succession_Planning**

- **Question:** Is there succession planning for key incident response roles?
- **Dropdown:** Yes / Informal / No
- **Succession Planning Elements:**
  - Backup personnel identified for critical roles (Incident Manager, Forensic Specialist)
  - Cross-training programs
  - Documentation to enable knowledge transfer
  - Onboarding plans for new hires
- **Risk:** Key person dependency (single person with critical skill; departure causes capability gap)


**Q52: Skills_Gaps_Identified**

- **Question:** Have skill gaps in the incident response team been identified?
- **Dropdown:** Yes - Documented / Informally Identified / No
- **Common Skill Gaps:**
  - Cloud security (AWS/Azure/GCP incident response)
  - Forensics (specialized training needed)
  - Malware reverse engineering
  - Threat intelligence analysis
  - Regulatory compliance (GDPR, PCI DSS procedures)
- **Evidence:** Skills assessment matrix, training needs analysis
- **Remediation:** Training, hiring, or external augmentation (retainers, MSSPs)


---

### **Section E: Management Visibility**

**Q53: Management_Reporting_Frequency**

- **Question:** How frequently does CSIRT report to management (CISO, CIO, or Executive)?
- **Dropdown:** Weekly / Monthly / Quarterly / Ad-Hoc (only during incidents) / Never
- **Best Practice:**
  - Monthly metrics reports (incident volume, trends, SLA compliance)
  - Quarterly strategic reviews (capability improvements, training, budget)
  - Ad-hoc for Critical/High severity incidents
- **Management Reporting Should Include:**
  - Incident statistics (count by category, severity)
  - Mean Time to Detect (MTTD), Mean Time to Respond (MTTR)
  - Open/closed incident trends
  - Training and exercise completion
  - Budget and resource needs


**Q54: CSIRT_Performance_Metrics**

- **Question:** Are incident management performance metrics defined and tracked?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No
- **Comprehensive Metrics Include:**
  - **Volume:** Number of incidents (by severity, category, month)
  - **Detection:** Mean Time to Detect (MTTD)
  - **Response:** Mean Time to Respond (MTTR), Mean Time to Contain (MTTC)
  - **SLA Compliance:** % incidents meeting response SLA
  - **False Positives:** % events classified as incidents but determined false
  - **Training:** % staff trained, % exercises completed
  - **Improvements:** Number of lessons learned implemented
- **Evidence:** Metrics dashboard, monthly reports


**Q55: Board_Briefing_Protocol**

- **Question:** Is there a protocol for briefing the Board of Directors on material incidents?
- **Dropdown:** Yes / Informal / No / N/A (no board)
- **Board Briefing Should Include:**
  - Incident summary (what happened, impact)
  - Root cause and contributing factors
  - Response actions and containment
  - Business impact (financial, operational, reputational)
  - Lessons learned and improvements
- **Typical Triggers:** Material incidents (per Q14 criteria)
- **Evidence:** Board briefing template, past briefing materials


---

## Sheet 4: Training & Competency

**Purpose:** Assess training programs, exercises, and competency tracking

**Assessment Questions (25 questions):**

---

### **Section A: Training Program**

**Q56: Training_Program_Exists**

- **Question:** Does [Organization] have a documented incident response training program?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No
- **Comprehensive Program Includes:**
  - Training curriculum (awareness, role-specific, specialized)
  - Delivery methods (classroom, online, tabletop, simulation)
  - Frequency requirements (annual for all, quarterly for CSIRT)
  - Competency assessment
  - Training records and tracking
- **Evidence:** Training program document, curriculum, training calendar


**Q57: Annual_Awareness_Training**

- **Question:** Do all staff receive annual security awareness training including incident reporting?
- **Dropdown:** Yes / Partial (some staff) / No
- **Requirement:** ISMS-POL-A.5.24-28 Section 2.1.3 - Annual training for all staff
- **Awareness Training Should Cover:**
  - What is a security incident (examples)
  - How to recognize security incidents
  - How to report incidents (A.6.8 integration - reporting mechanism)
  - Importance of timely reporting
  - Personal accountability
- **Evidence:** Training completion records, course materials


**Q58: Awareness_Training_Completion_Rate**

- **Question:** What percentage of staff completed incident reporting awareness training in the last 12 months?
- **Format:** Percentage (e.g., 95%)
- **Target:** >95% compliance
- **Calculation:** (Staff trained / Total staff) × 100
- **Evidence:** Training management system reports, HR records


**Q59: CSIRT_Specialized_Training**

- **Question:** Do CSIRT members receive specialized incident response training?
- **Dropdown:** Yes - Regular / Yes - Occasional / No
- **Specialized Training Topics:**
  - Incident handling methodologies (NIST, SANS)
  - Digital forensics
  - Malware analysis
  - Threat intelligence
  - Regulatory compliance (GDPR breach notification, PCI DSS forensics)
  - Tools (SIEM, forensic tools, SOAR)
- **Best Practice:** CSIRT members receive at least 40 hours specialized training annually
- **Evidence:** Training records, certifications, course materials


**Q60: External_Training_Budget**

- **Question:** Is there a dedicated budget for incident response training (courses, certifications, conferences)?
- **Dropdown:** Yes - Adequate / Yes - Limited / No
- **Common Training Investments:**
  - SANS FOR500, FOR508, FOR572 courses ($5,000-$8,000 each)
  - Certifications (GCIH, GCFA, GCFE) (exam fees ~$2,000)
  - Conferences (Black Hat, RSA, FIRST) ($1,500-$3,000 per person)
- **Budgeting Rule of Thumb:** $5,000-$10,000 per CSIRT member annually for external training
- **ROI:** Trained staff = faster, more effective incident response


---

### **Section B: Tabletop Exercises**

**Q61: Tabletop_Exercise_Frequency**

- **Question:** How often does [Organization] conduct incident response tabletop exercises?
- **Dropdown:** Quarterly / Semi-Annually / Annually / Bi-Annually / Never
- **Requirement:** ISMS-POL-A.5.24-28 Section 2.1.3 - Minimum annually
- **Best Practice:** Quarterly for CSIRT, annually for broader organization (including Legal, HR, Management)
- **Tabletop Exercise Purpose:**
  - Test procedures without actual incident
  - Identify gaps in response (roles, communication, tools)
  - Build muscle memory and coordination
  - Low-cost, high-value training method


**Q62: Last_Tabletop_Date**

- **Question:** When was the most recent tabletop exercise conducted?
- **Format:** Date (DD.MM.YYYY) or "Never conducted"
- **Red Flag:** >12 months since last exercise
- **Evidence:** Exercise report, participant list, lessons learned


**Q63: Tabletop_Scenario_Variety**

- **Question:** Do tabletop exercises cover a variety of incident types?
- **Dropdown:** Yes - Diverse Scenarios / Limited Variety / Single Scenario Type
- **Recommended Scenario Variety:**
  - Ransomware attack
  - Data breach (personal data exfiltration)
  - Insider threat (malicious employee)
  - DDoS attack (availability incident)
  - Supply chain compromise (third-party incident)
  - Business Email Compromise (BEC/CEO fraud)
- **Rationale:** Different incident types test different procedures, roles, and decisions


**Q64: Tabletop_Participants**

- **Question:** Who typically participates in tabletop exercises?
- **Checkbox (multiple selections):**
  - ☐ CSIRT members
  - ☐ IT Operations
  - ☐ Legal/Compliance
  - ☐ HR
  - ☐ Management (CISO, CIO)
  - ☐ Executive Leadership (CEO, COO)
  - ☐ Board of Directors
  - ☐ External Partners (MSSP, legal retainer)
- **Best Practice:** Scale participation to scenario:
  - Operational exercises: CSIRT + IT Ops
  - Strategic exercises: Include Legal, Management, Executive
  - Board exercises: Focus on decision-making, communication, business impact


**Q65: Tabletop_Lessons_Learned**

- **Question:** Are lessons learned from tabletop exercises documented and acted upon?
- **Dropdown:** Yes - Systematically / Yes - Informally / No
- **Lessons Learned Process:**

  1. **During Exercise:** Facilitator notes gaps, issues, confusion
  2. **Post-Exercise Debrief:** Participants discuss what went well, what didn't
  3. **Documentation:** Formal after-action report (AAR)
  4. **Action Items:** Specific remediation tasks assigned with owners and deadlines
  5. **Tracking:** Action items tracked to completion
  6. **Follow-Up:** Next exercise tests whether gaps were closed

- **Evidence:** Exercise after-action reports, action item tracking


---

### **Section C: Simulation & Testing**

**Q66: Full_Scale_Exercises**

- **Question:** Does [Organization] conduct full-scale incident response exercises (beyond tabletop)?
- **Dropdown:** Yes - Regularly / Yes - Occasionally / No
- **Full-Scale Exercise Types:**
  - **Red Team / Blue Team:** Simulated attack, CSIRT defends
  - **Purple Team:** Collaborative exercise (red team + blue team)
  - **Cyber Range:** Simulated environment for safe testing
  - **Breach Simulation:** Third-party simulates breach (e.g., ransomware deployment in isolated environment)
- **Benefit:** More realistic than tabletop, identifies operational gaps
- **Challenge:** Resource-intensive, requires isolated test environment


**Q67: Breach_Simulation_Tools**

- **Question:** Does [Organization] use breach simulation or attack simulation tools?
- **Dropdown:** Yes / No
- **Tools Examples:**
  - **Breach and Attack Simulation (BAS):** Automated attack simulation (SafeBreach, AttackIQ)
  - **Red Team Frameworks:** Cobalt Strike, Metasploit, custom tools
  - **Ransomware Simulation:** Controlled ransomware deployment (test environment only!)
- **Use Case:** Validate detection and response capabilities continuously
- **Evidence:** BAS platform reports, red team reports


**Q68: Regulatory_Drills**

- **Question:** Are drills conducted specifically for regulatory breach notification (GDPR 72-hour, PCI DSS, etc.)?
- **Dropdown:** Yes / No
- **Regulatory Drill Purpose:**
  - Test notification procedures
  - Verify contact information current
  - Practice decision-making (does breach meet notification threshold?)
  - Time the process (can we meet 72-hour GDPR deadline?)
- **Best Practice:** Annual GDPR breach notification drill (tabletop minimum, full-scale ideal)
- **Evidence:** Drill scenarios, timeline logs, notification drafts


---

### **Section D: Competency & Certification**

**Q69: Competency_Requirements_Defined**

- **Question:** Are competency requirements defined for incident response roles?
- **Dropdown:** Yes / No
- **Competency Framework Should Define:**
  - Technical skills (forensics, malware analysis, log analysis, networking)
  - Soft skills (communication, decision-making under pressure, teamwork)
  - Certifications (GCIH, GCFA, GCFE, CISSP, CEH)
  - Experience (years in security, incident response)
- **Evidence:** Competency matrix, job descriptions, hiring criteria


**Q70: Certification_Tracking**

- **Question:** Does [Organization] track security certifications for CSIRT members?
- **Dropdown:** Yes / Informal / No
- **Common Incident Response Certifications:**
  - **GIAC (SANS):** GCIH, GCFA, GCFE, GREM
  - **(ISC)²:** CISSP, CCSP
  - **EC-Council:** CEH, CHFI
  - **Vendor-Specific:** EnCE (EnCase), ACE (AccessData)
- **Tracking Benefits:**
  - Identify skill gaps
  - Support professional development
  - Demonstrate team capability to auditors, management
- **Evidence:** Certification register, copies of certificates


**Q71: Certification_Currency**

- **Question:** Are certifications current (not expired)?
- **Dropdown:** Yes - All Current / Some Expired / Not Tracked
- **Note:** Most security certifications require continuing education (CPEs) and renewal every 3 years
- **Risk:** Expired certifications may indicate lack of ongoing training
- **Evidence:** Certification expiration dates, CPE tracking


**Q72: New_Hire_Onboarding**

- **Question:** Is there a documented onboarding process for new CSIRT members?
- **Dropdown:** Yes - Formal Program / Informal / No
- **Onboarding Should Include:**
  - Introduction to incident management policy and procedures
  - Tool training (SIEM, ticketing, forensics)
  - Shadowing experienced team members
  - Escalation and communication procedures
  - Regulatory requirements (GDPR, PCI DSS, sector-specific)
  - First 30/60/90 day milestones
- **Duration:** Typical onboarding 30-90 days depending on role complexity
- **Evidence:** Onboarding checklist, training records


---

### **Section E: Training Effectiveness**

**Q73: Training_Effectiveness_Measured**

- **Question:** Is training effectiveness measured (beyond completion tracking)?
- **Dropdown:** Yes / No
- **Effectiveness Measures:**
  - **Knowledge Assessment:** Pre/post-training quizzes, certifications
  - **Behavioral Change:** Incident reporting rates increased after awareness training?
  - **Performance Improvement:** Response time improved after specialized training?
  - **Exercise Performance:** Tabletop performance improved over time?
- **Best Practice:** Combine multiple measures (Kirkpatrick Model - Reaction, Learning, Behavior, Results)


**Q74: Training_Feedback_Collected**

- **Question:** Is feedback collected from training participants?
- **Dropdown:** Yes - Systematically / Occasionally / No
- **Feedback Mechanisms:**
  - Post-training surveys (course content, instructor, relevance)
  - Exercise debriefs (what went well, what to improve)
  - Annual training needs assessment
- **Use of Feedback:** Improve training content, adjust delivery methods, identify new topics


**Q75: Training_Gaps_Identified**

- **Question:** Have training gaps been identified through exercises or actual incidents?
- **Dropdown:** Yes - Documented / Informally Identified / No
- **Gap Identification Methods:**
  - Tabletop exercises reveal knowledge gaps (e.g., no one knew GDPR 72-hour requirement)
  - Actual incidents reveal skill gaps (e.g., malware analysis took too long, outsourced)
  - Staff surveys (self-assessment of confidence and competence)
- **Evidence:** Exercise after-action reports, post-incident reviews, training needs analysis


---

## Sheet 5: Tools & Technology

**Purpose:** Assess incident response tools and technology capabilities

**Assessment Questions (30 questions):**

---

### **Section A: Incident Ticketing & Tracking**

**Q76: Ticketing_System_Exists**

- **Question:** Does [Organization] have a dedicated incident ticketing/tracking system?
- **Dropdown:** Yes - Dedicated IR Platform / Yes - General IT Ticketing / No
- **Platform Examples:**
  - **Dedicated IR:** TheHive, Cortex, RTIR (Request Tracker for Incident Response), Resilient (IBM)
  - **General IT Ticketing Adapted:** ServiceNow Security Incident Module, Jira Service Management
  - **SOAR Platforms (Advanced):** Splunk Phantom, Palo Alto Cortex XSOAR, Swimlane
- **Dedicated IR Platform Benefits:**
  - Purpose-built for incident workflows
  - Integration with security tools (SIEM, threat intel)
  - Playbook automation
  - Evidence tracking and chain of custody


**Q77: Ticketing_System_Features**

- **Question:** What features does the incident ticketing system provide?
- **Checkbox (multiple selections):**
  - ☐ Incident creation and assignment
  - ☐ Severity and categorization
  - ☐ Timeline/chronology tracking
  - ☐ Evidence attachment and storage
  - ☐ Task management (subtasks, workflows)
  - ☐ Communication/collaboration (comments, notes)
  - ☐ Escalation and notification
  - ☐ Integration with other tools (SIEM, email, Slack)
  - ☐ Reporting and dashboards
  - ☐ Playbook/runbook integration
- **Critical Features:** At minimum, system should support creation, assignment, severity, timeline, and reporting


**Q78: Ticket_Retention**

- **Question:** How long are incident tickets retained?
- **Dropdown:** 1 year / 3 years / 5 years / 7+ years / Indefinitely / Not Defined
- **Requirements:**
  - **Regulatory:** GDPR breach records must be kept (Art. 33(5))
  - **Legal:** Potential litigation evidence (7+ years typical)
  - **Best Practice:** 7 years minimum, indefinitely for material/regulatory incidents
- **Evidence:** Ticketing system retention policy, archive procedures


**Q79: Ticket_Access_Control**

- **Question:** Are access controls implemented for incident tickets (need-to-know basis)?
- **Dropdown:** Yes - Strict / Yes - Moderate / No - Open Access
- **Access Control Considerations:**
  - Sensitive incidents (insider threat, exec compromise) should be restricted
  - Most incidents accessible to CSIRT members
  - Management/Legal granted access as needed
  - Auditors granted read-only access
- **Compliance:** Confidentiality of investigation, attorney-client privilege (for legally sensitive incidents)


---

### **Section B: SIEM Integration**

**Q80: SIEM_Deployed**

- **Question:** Does [Organization] have a Security Information and Event Management (SIEM) system?
- **Dropdown:** Yes - Fully Operational / Yes - Partial Deployment / No
- **SIEM Purpose:**
  - Aggregate logs from multiple sources
  - Correlate events to detect incidents
  - Provide centralized investigation platform
  - Generate alerts for CSIRT
- **Common SIEM Platforms:** Splunk, QRadar (IBM), Sentinel (Microsoft), ArcSight (Micro Focus), ELK Stack (open source)


**Q81: SIEM_Log_Sources**

- **Question:** How many log sources feed into the SIEM?
- **Format:** Number (count) or "Not applicable (no SIEM)"
- **Log Source Categories:**
  - Network devices (firewalls, routers, switches, IDS/IPS)
  - Endpoints (Windows event logs, Mac logs, Linux syslog)
  - Applications (web servers, databases, email, authentication)
  - Security tools (antivirus, EDR, DLP, web proxy)
  - Cloud services (AWS CloudTrail, Azure logs, O365 audit logs)
- **Benchmark:** Comprehensive SIEM ingests 50-500+ log sources depending on org size


**Q82: SIEM_Integration_with_Ticketing**

- **Question:** Is the SIEM integrated with the incident ticketing system (automatic ticket creation)?
- **Dropdown:** Yes - Fully Automated / Yes - Semi-Automated / Manual / N/A (no SIEM)
- **Integration Benefits:**
  - SIEM alert → Automatically creates incident ticket
  - Reduces response time (no manual ticket creation)
  - Ensures all alerts are logged and tracked
- **Example:** Splunk alert fires → Creates ServiceNow incident via API → Assigns to SOC


**Q83: SIEM_Playbook_Automation**

- **Question:** Does the SIEM/SOAR platform support automated playbooks for common incident types?
- **Dropdown:** Yes - Extensive / Yes - Limited / No / N/A
- **Playbook Examples:**
  - Malware detected → Isolate endpoint + Collect forensic evidence + Create ticket
  - Brute force attack → Block IP + Alert SOC + Create ticket
  - Data exfiltration alert → Block egress + Alert Legal + Escalate to CISO
- **SOAR (Security Orchestration, Automation, Response) Platforms:**
  - Splunk Phantom
  - Palo Alto Cortex XSOAR
  - Swimlane
  - Demisto (acquired by Palo Alto)


---

### **Section C: Forensic Tools**

**Q84: Forensic_Tools_Available**

- **Question:** What digital forensic tools are available to the incident response team?
- **Checkbox (multiple selections):**
  - ☐ Disk imaging (FTK Imager, EnCase, dd)
  - ☐ Memory acquisition (FTK Imager, WinPmem, LiME)
  - ☐ Memory analysis (Volatility, Rekall)
  - ☐ Network forensics (Wireshark, tcpdump, NetworkMiner)
  - ☐ Log analysis (grep, Splunk, ELK)
  - ☐ Malware analysis (Cuckoo Sandbox, Joe Sandbox, ANY.RUN)
  - ☐ Mobile forensics (Cellebrite, Magnet AXIOM)
  - ☐ Cloud forensics (AWS forensics tools, Azure logging)
  - ☐ Commercial forensic suites (EnCase, X-Ways, Magnet AXIOM)
  - ☐ None / Not applicable
- **Note:** Combination of open-source and commercial tools typical


**Q85: Forensic_Tool_Training**

- **Question:** Are CSIRT members trained in the use of forensic tools?
- **Dropdown:** Yes - All Members / Yes - Specialized Roles Only / Limited / No
- **Training Requirements:**
  - Tool-specific training (e.g., EnCase certification)
  - Forensic methodology (NIST, SANS FOR500/572)
  - Legal considerations (chain of custody, admissibility)
- **Risk:** Tools without training → Evidence mishandled, inadmissible in court


**Q86: Forensic_Workstation**

- **Question:** Does [Organization] have a dedicated forensic workstation or lab?
- **Dropdown:** Yes - Dedicated Lab / Yes - Virtual Environment / No
- **Forensic Workstation Requirements:**
  - Write blockers (hardware or software)
  - Large storage (for forensic images)
  - Forensic software licenses
  - Isolated network (avoid contamination)
  - Documented chain of custody procedures
- **Alternative:** Cloud-based forensic environment (AWS forensics instance)


**Q87: Evidence_Storage**

- **Question:** Is there secure storage for forensic evidence?
- **Dropdown:** Yes - Dedicated Storage / Yes - General Storage / No
- **Storage Requirements:**
  - Sufficient capacity (disk images are large - 500GB-2TB per device)
  - Access control (evidence integrity)
  - Encryption at rest
  - Retention policy (7+ years for material incidents)
  - Chain of custody log (who accessed when)
- **Evidence Types:** Disk images, memory dumps, PCAPs, log exports, malware samples


---

### **Section D: Communication Platforms**

**Q88: Internal_Communication_Tools**

- **Question:** What tools are used for internal incident response communication?
- **Checkbox (multiple selections):**
  - ☐ Email
  - ☐ Phone/Mobile
  - ☐ Instant Messaging (Slack, Microsoft Teams, etc.)
  - ☐ Video Conferencing (Zoom, Teams, WebEx)
  - ☐ Incident War Room (physical or virtual)
  - ☐ Dedicated IR Communication Platform (e.g., PagerDuty, VictorOps)
  - ☐ Encrypted Communication (Signal, WhatsApp, PGP)
- **Best Practice:**
  - Primary: Incident ticketing system (timeline, evidence)
  - Secondary: Real-time chat (Slack channel for active incident)
  - Escalation: Phone/SMS (for urgency)
  - Sensitive: Encrypted channels (insider threat, legal matters)


**Q89: External_Communication_Secure_Channel**

- **Question:** Is there a secure channel for external communications (legal, law enforcement, regulators)?
- **Dropdown:** Yes / No
- **Secure Channels:**
  - Encrypted email (PGP, S/MIME)
  - Secure file sharing (password-protected, encrypted)
  - Dedicated portal (for regulators, law enforcement)
- **Use Cases:**
  - Sharing forensic evidence with law enforcement
  - Breach notification to supervisory authority
  - Attorney-client privileged communications (encrypted)


**Q90: On_Call_Alerting**

- **Question:** How are on-call incident responders alerted?
- **Dropdown:** PagerDuty / VictorOps / Phone Call / SMS / Email / No On-Call System
- **On-Call System Requirements:**
  - Reliable alerting (multiple channels - push notification + SMS + phone call)
  - Escalation (if no response, alert backup)
  - Alert acknowledgment (confirm on-call received alert)
  - Integration with monitoring/SIEM (automated alerts)
- **Best Practice:** Dedicated on-call platform (PagerDuty, VictorOps, Opsgenie) over email alone


---

### **Section E: Threat Intelligence Integration**

**Q91: Threat_Intel_Feeds**

- **Question:** Does [Organization] subscribe to threat intelligence feeds?
- **Dropdown:** Yes - Multiple Feeds / Yes - Single Feed / No
- **Threat Intel Feed Types:**
  - **Commercial:** Recorded Future, CrowdStrike, Mandiant, ThreatConnect
  - **Open Source:** AlienVault OTX, MISP, Abuse.ch
  - **ISAC/ISAO:** Industry-specific (FS-ISAC, H-ISAC, etc.)
  - **Government:** CISA, NCSC, national CERTs
- **Use Cases:**
  - IOC enrichment (is this IP/domain known malicious?)
  - Proactive threat hunting
  - Alert prioritization (known APT group TTPs)


**Q92: Threat_Intel_Integration_SIEM**

- **Question:** Is threat intelligence integrated into SIEM for alerting?
- **Dropdown:** Yes - Automated / Yes - Manual Lookups / No / N/A (no threat intel)
- **Integration:**
  - IOC feed → SIEM correlation rule → Alert if match
  - Example: SIEM detects connection to IP listed in threat feed → Generate alert
- **Benefit:** Proactive detection of known threats


**Q93: Threat_Intel_Analyst_Role**

- **Question:** Is there a dedicated threat intelligence analyst role?
- **Dropdown:** Yes - Dedicated Role / Yes - Part-Time / No - CSIRT Handles
- **Threat Intel Analyst Responsibilities:**
  - Monitor threat landscape
  - Analyze threat actor TTPs
  - Provide incident context (attribution, campaign)
  - Update detection rules based on emerging threats
- **Small Orgs:** CSIRT members perform threat intel as part of duties (no dedicated analyst)


---

### **Section F: Automation Capabilities**

**Q94: Incident_Response_Automation**

- **Question:** What level of incident response automation exists?
- **Dropdown:** High (SOAR Platform) / Moderate (Some Playbooks) / Low (Mostly Manual) / None
- **Automation Examples:**
  - **High (SOAR):**
    - Automated playbooks for 10+ incident types
    - Orchestration across multiple tools (SIEM, EDR, firewall, ticketing)
    - Human-in-the-loop for critical decisions
  - **Moderate:**
    - SIEM automated ticket creation
    - Automated endpoint isolation (EDR)
    - Automated IOC enrichment (threat intel lookup)
  - **Low:**
    - Scripts for common tasks (e.g., block IP via firewall API)
    - Manual execution of most response actions


**Q95: Playbook_Count**

- **Question:** How many documented/automated playbooks exist?
- **Format:** Number (count) or "None"
- **Common Playbooks:**
  - Malware incident response
  - Ransomware response
  - Data breach response
  - Phishing response
  - DDoS mitigation
  - Insider threat investigation
  - BEC/CEO fraud response
- **Benchmark:** 10-20 playbooks for comprehensive coverage


**Q96: Playbook_Maintenance**

- **Question:** Are playbooks regularly reviewed and updated?
- **Dropdown:** Yes - Annually / Yes - After Incidents / No / N/A (no playbooks)
- **Playbook Update Triggers:**
  - Annual review
  - After major incident (lessons learned)
  - Tool changes (new SIEM, EDR, etc.)
  - Regulatory changes (new notification requirements)
- **Risk:** Outdated playbooks reference deprecated tools, wrong contacts, obsolete procedures


---

### **Section G: Tool Gap Analysis**

**Q97: Critical_Tool_Gaps**

- **Question:** Are there critical tool gaps preventing effective incident response?
- **Dropdown:** Yes - Multiple Gaps / Yes - Some Gaps / No
- **Common Tool Gaps:**
  - No SIEM → Blind to correlated attacks
  - No EDR → Cannot isolate compromised endpoints remotely
  - No forensic tools → Must outsource forensics (slow, expensive)
  - No ticketing system → Incidents tracked in email (no accountability)
  - No threat intel → Cannot identify known threats
- **Impact:** Tool gaps = longer response times, missed incidents, higher costs


**Q98: Tool_Procurement_Planned**

- **Question:** Are tool gaps being addressed (budget approved, procurement in progress)?
- **Dropdown:** Yes - Funded / Proposed (Budget Request) / No
- **Procurement Timeline:**
  - Budget approval (annual cycle or emergency request)
  - Vendor selection and POC (1-3 months)
  - Procurement and deployment (2-6 months)
  - Training and operationalization (1-3 months)
- **Evidence:** Budget documents, procurement plans, project timelines


**Q99: Tool_Integration_Challenges**

- **Question:** Are there challenges integrating incident response tools?
- **Dropdown:** Yes - Significant / Yes - Moderate / No / N/A (few tools)
- **Integration Challenges:**
  - Legacy tools lack APIs (manual data export/import)
  - Vendor silos (tools don't communicate)
  - Data format inconsistencies (CSV vs. JSON vs. proprietary)
  - Complexity (too many tools, integration sprawl)
- **Remediation:** SOAR platforms can bridge integration gaps


---

## Sheet 6: Integration Assessment

**Purpose:** Assess integration with related ISMS controls

**Assessment Questions (25 questions):**

---

### **Section A: Logging Integration (A.8.15)**

**Q100: Logging_Integration_Exists**

- **Question:** Is incident management integrated with logging infrastructure (A.8.15)?
- **Dropdown:** Yes - Fully Integrated / Partially Integrated / No
- **Integration Points:**
  - Incident investigations require access to comprehensive logs
  - Logging scope covers systems relevant to incident response
  - Log retention supports forensic investigation (ISMS-POL-A.8.15 retention requirements)
- **Evidence:** Cross-reference ISMS-IMP-A.8.15 (Logging Assessment)


**Q101: Log_Availability_During_Incidents**

- **Question:** Are logs readily available to CSIRT during incidents?
- **Dropdown:** Yes - Immediate Access / Yes - Delayed Access / No
- **Access Methods:**
  - SIEM centralized logs (ideal - search and correlate)
  - Direct system access (SSH, RDP to log locations)
  - Request to IT Ops (slower, dependency)
- **Best Practice:** CSIRT has direct access to SIEM or centralized logging platform


**Q102: Log_Retention_Adequate**

- **Question:** Is log retention adequate for incident investigation?
- **Dropdown:** Yes / Insufficient for Some Systems / No
- **Retention Requirements:**
  - Minimum: 90 days (ISMS-POL-A.8.15 baseline)
  - Best Practice: 12 months (enables historical analysis, detection of long-dwell-time threats)
  - Regulatory: GDPR breach investigation may require access to logs >90 days prior
- **Risk:** Short retention → Cannot investigate incidents discovered late (e.g., breach discovered 6 months after occurrence)


---

### **Section B: Monitoring Integration (A.8.16)**

**Q103: Monitoring_Integration_Exists**

- **Question:** Is incident management integrated with security monitoring (A.8.16)?
- **Dropdown:** Yes - Fully Integrated / Partially Integrated / No
- **Integration Points:**
  - SIEM/SOC monitoring detects events → Triggers incident classification (A.5.25)
  - Monitoring alerts automatically create incident tickets
  - Monitoring data feeds incident investigation
- **Evidence:** Cross-reference ISMS-IMP-A.8.16 (Monitoring Assessment)


**Q104: Alert_to_Incident_Workflow**

- **Question:** Is there a defined workflow from security alert to incident declaration?
- **Dropdown:** Yes - Documented / Informal / No
- **Workflow:**

  1. Monitoring system generates alert (SIEM rule, IDS, EDR)
  2. SOC Analyst reviews alert (triage)
  3. Analyst classifies as Event (false positive) or Incident (true positive)
  4. If Incident → Create ticket, assign severity, escalate per procedures

- **Evidence:** Workflow diagram, SOC procedures, SIEM integration documentation


**Q105: False_Positive_Rate_Tracking**

- **Question:** Is the false positive rate from monitoring tracked?
- **Dropdown:** Yes / No
- **False Positive Rate = (False Positive Alerts / Total Alerts) × 100**
- **Target:** <1% for high-fidelity alerts, <10% for experimental rules
- **High FP Rate Problems:**
  - Alert fatigue (SOC ignores alerts)
  - Wasted investigation time
  - True incidents missed in noise
- **Remediation:** Tune SIEM rules, improve detection logic, add context/enrichment


---

### **Section C: User Event Reporting Integration (A.6.8)**

**Q106: User_Reporting_Mechanism_Exists**

- **Question:** Is there a mechanism for users to report security events (A.6.8 integration)?
- **Dropdown:** Yes - Dedicated / Yes - General IT Helpdesk / No
- **Reporting Mechanisms:**
  - Dedicated security email (security@example.com)
  - IT helpdesk (ServiceNow, Jira)
  - Phishing button (email client plugin)
  - Security hotline (phone)
  - Web form or internal portal
- **Best Practice:** Multiple channels (email + helpdesk) for accessibility


**Q107: User_Reports_Integrated_Ticketing**

- **Question:** Are user-reported events integrated into incident ticketing system?
- **Dropdown:** Yes - Automatically / Yes - Manually / No
- **Integration:**
  - User reports phishing email → Email to security@example.com → Creates ticket automatically → Assigned to SOC
  - Alternative: Helpdesk ticket → Triaged by helpdesk → Escalated to CSIRT if security incident
- **Risk:** Manual handoff = delays, missed reports


**Q108: User_Reporting_Awareness**

- **Question:** Do users know how to report security incidents?
- **Dropdown:** Yes - Well Communicated / Somewhat / No
- **Communication Methods:**
  - Annual security awareness training (Q57 integration)
  - Phishing simulations (remind users to report phishing)
  - Posters, intranet, email signatures
  - New hire onboarding
- **Metric:** User reporting rate (# user reports per month)
- **Goal:** Increase user reporting (users are the "human IDS")


---

### **Section D: BC/DR Integration (A.5.29-30)**

**Q109: BCDR_Integration_Defined**

- **Question:** Is incident management integrated with Business Continuity / Disaster Recovery (A.5.29-30)?
- **Dropdown:** Yes - Documented / Informal / No
- **Integration Points:**
  - Major incidents (ransomware, outages) trigger BC/DR activation
  - BC/DR plan references incident management procedures
  - CSIRT involved in BC/DR exercises
- **Evidence:** Cross-reference ISMS-POL-A.5.29-30, BC/DR plan


**Q110: Incident_BCDR_Trigger_Criteria**

- **Question:** Are criteria defined for when an incident triggers BC/DR activation?
- **Dropdown:** Yes / No
- **Trigger Examples:**
  - Ransomware encrypts critical production systems
  - Data center outage (natural disaster, power failure)
  - Prolonged service unavailability (>4 hours for critical systems)
- **Evidence:** BC/DR activation criteria document, escalation matrix


**Q111: CSIRT_Role_in_BCDR**

- **Question:** Is CSIRT's role defined in BC/DR plans?
- **Dropdown:** Yes - Documented / Informal / No
- **CSIRT Responsibilities During BC/DR:**
  - Incident containment and eradication (stop the attack)
  - Forensic investigation (why did this happen?)
  - Communication with stakeholders (technical status updates)
  - Support recovery (ensure systems restored securely, not re-infected)
- **BC/DR Team Focus:** Business continuity, service restoration, customer communication
- **Collaboration:** CSIRT (technical security) + BC/DR Team (business continuity)


---

### **Section E: Third-Party Coordination**

**Q112: Third_Party_Incident_Procedures**

- **Question:** Are procedures defined for incidents involving third parties (suppliers, MSSPs)?
- **Dropdown:** Yes - Documented / Informal / No
- **Third-Party Incident Scenarios:**
  - Supplier breach affecting [Organization] (e.g., cloud provider incident)
  - MSSP-detected incident (outsourced SOC escalates to [Organization])
  - Vendor software vulnerability requiring patch/mitigation
- **Procedures Should Cover:**
  - Notification from third party
  - Escalation to [Organization] CSIRT
  - Coordination and communication
  - Evidence collection (if third party provides logs, forensics)


**Q113: MSSP_SLA_Defined**

- **Question:** (If MSSP/outsourced SOC) Are SLAs defined for incident detection and escalation?
- **Dropdown:** Yes / No / N/A (no MSSP)
- **MSSP SLAs Should Include:**
  - Detection time (mean time to detect)
  - Escalation time (how quickly MSSP notifies [Organization])
  - Severity thresholds (what gets escalated immediately vs. daily report)
  - Communication protocols (phone, email, portal)
- **Evidence:** MSSP contract, SLA document


**Q114: Supplier_Incident_Notification_Process**

- **Question:** Do suppliers know how to report security incidents to [Organization]?
- **Dropdown:** Yes - Defined in Contracts / Informal / No
- **Supplier Contract Language (A.5.19-20 integration):**
  - Supplier must notify [Organization] of security incidents affecting [Organization] data or services
  - Notification timeline (within 24 hours)
  - Contact: [Organization] Security Team (security@example.com)
- **Evidence:** Supplier contracts, supplier security requirements


---

### **Section F: Legal & Regulatory Coordination**

**Q115: Legal_Integration_Defined**

- **Question:** Is Legal/Compliance involvement in incident management clearly defined?
- **Dropdown:** Yes - Documented / Informal / No
- **Legal Involvement Triggers:**
  - Data breach (personal data, Restricted/Confidential)
  - Regulatory breach notification required
  - Law enforcement involvement
  - Potential litigation (employee termination, external threat actor)
  - Attorney-client privilege (sensitive investigations)
- **Procedures:**
  - When to notify Legal (severity threshold, incident type)
  - How to notify Legal (immediate phone call for Critical, email for lower severity)
  - Legal's role (breach notification decision, communication approval, evidence handling)


**Q116: DPO_Integration**

- **Question:** (If GDPR applicable) Is the Data Protection Officer (DPO) integrated into incident management?
- **Dropdown:** Yes / No / N/A (GDPR not applicable)
- **DPO Involvement:**
  - Consulted for all incidents involving personal data
  - Makes breach notification decision (Art. 33 assessment)
  - Coordinates with supervisory authority
- **Evidence:** DPO role description, incident procedures referencing DPO


**Q117: Law_Enforcement_Coordination**

- **Question:** Are procedures defined for coordinating with law enforcement?
- **Dropdown:** Yes - Documented / Informal / No
- **Law Enforcement Coordination:**
  - When to involve (major breach, nation-state attack, criminal activity)
  - How to contact (cybercrime unit contacts)
  - What to share (evidence, forensics, IOCs)
  - Legal considerations (jurisdiction, evidence admissibility)
- **Best Practice:** Establish relationship with law enforcement proactively (before incident)
- **Evidence:** Law enforcement contact list, coordination procedures


---

## Sheet 7: Gap Analysis

**Purpose:** Consolidate gaps from all assessment sections and prioritize remediation

**Gap Register Format:**

| Gap_ID | Assessment_Section | Gap_Description | Risk_Level | Current_State | Target_State | Remediation_Action | Owner | Target_Date | Status |
|--------|-------------------|-----------------|-----------|---------------|--------------|-------------------|-------|-------------|--------|
| GAP-001 | Governance | No RACI matrix documented | High | Roles informally understood | RACI matrix created and approved | Document RACI matrix, review with CSIRT, approve | CSIRT Manager | [Date + 30 days] | Open |
| GAP-002 | Training | <50% tabletop exercise completion | Medium | Last exercise 18 months ago | Quarterly exercises | Schedule Q1 exercise, appoint facilitator | CSIRT Manager | [Date + 60 days] | Open |
| [etc.] | | | | | | | | | |

**Risk Levels:**

- **Critical:** Immediate security risk, regulatory violation, or operational impact
- **High:** Significant gap, should remediate within 3 months
- **Medium:** Moderate gap, remediate within 6-12 months
- **Low:** Minor gap, address when feasible


**Prioritization Criteria:**
1. **Regulatory Compliance:** GDPR, PCI DSS, sector-specific requirements
2. **Operational Impact:** Does gap prevent effective incident response?
3. **Risk Exposure:** Does gap leave organization vulnerable?
4. **Effort/Cost:** Quick wins vs. major projects

---

## Sheet 8: Evidence Register

**Purpose:** Document all evidence supporting the framework assessment

**Evidence Register Format:**

| Evidence_ID | Evidence_Type | Description | Related_Section | Storage_Location | Date_Collected | Collected_By | Verification_Status |
|-------------|---------------|-------------|-----------------|------------------|----------------|--------------|-------------------|
| EV-001 | Policy Document | ISMS-POL-A.5.24-28 | Governance | SharePoint:/Policies/ | [Date] | CSIRT Manager | Verified |
| EV-002 | Org Chart | CSIRT Organizational Chart | Structure | /Evidence/S1/org_chart.pdf | [Date] | HR | Verified |
| EV-003 | Training Records | 2025 Security Awareness Training Completion | Training | HR System Report | [Date] | HR | Verified |
| [etc.] | | | | | | | |

**Evidence Types:**

- Policy Document
- Procedure/Runbook
- Organizational Chart
- Job Description
- RACI Matrix
- Training Record
- Exercise Report
- Tool Screenshot
- Contract/SLA
- Metrics Report
- Other


---

## Sheet 9: Dashboard

**Purpose:** Executive summary of framework assessment results

**Dashboard Sections:**

**A. Overall Framework Maturity Score**

- **Calculation:** Weighted average of Governance, Structure, Training, Tools, Integration
- **Maturity Levels:**
  - **Level 1 (Initial):** Ad-hoc, reactive, minimal documentation (0-40%)
  - **Level 2 (Developing):** Some processes defined, inconsistent implementation (41-60%)
  - **Level 3 (Defined):** Documented, standardized, repeatable processes (61-75%)
  - **Level 4 (Managed):** Measured, monitored, data-driven decisions (76-90%)
  - **Level 5 (Optimizing):** Continuous improvement, industry-leading (91-100%)


**B. Domain Scores**

- Governance Compliance: [%]
- Organizational Structure: [%]
- Training Effectiveness: [%]
- Tool Capabilities: [%]
- Integration Completeness: [%]


**C. Key Metrics**

- CSIRT Staffing (FTE): [#]
- Coverage Model: [24/7 / Business Hours / On-Call]
- Training Completion Rate: [%]
- Tabletop Exercise Frequency: [Quarterly / Annually / etc.]
- Tool Count: [#]
- Critical Gaps: [#]


**D. Top 10 Gaps**

- Gap prioritization table (from Gap Analysis sheet)


---

## Sheet 10: Approval Sign-Off

**Assessment Summary:**

```
Assessment Period: [Start Date] - [End Date]
Completed By: [Name, Title]
Assessment Status: [Draft / Under Review / Approved]
```

**Overall Maturity Level:** [Level 1-5]

**Key Findings:**

- [Summary of strengths]
- [Summary of critical gaps]
- [Remediation priority]


**Approval Workflow:**

| Role | Name | Date | Signature | Status |
|------|------|------|-----------|--------|
| **Assessor (CSIRT Manager)** | [Name] | [Date] | [Signature] | [ ] Submitted for review |
| **Reviewer (CISO)** | [Name] | [Date] | [Signature] | [ ] Approved / [ ] Revisions Required |
| **Next Review Date** | - | [Date + 12 months] | - | - |

---

# Evidence Collection Tips

## Governance Evidence

**Policy Documentation:**

- Screenshot policy approval page (signatures, date)
- Export policy version history
- Policy review meeting minutes


**Regulatory Procedures:**

- GDPR breach notification template (screenshot)
- PCI DSS incident reporting procedure (export)
- Contact lists (redact personal info if needed)


## Organizational Structure Evidence

**Org Charts:**

- Export from HR system or create diagram
- Show CSIRT reporting line to CISO
- Annotate with names and roles


**Job Descriptions:**

- Collect for key incident response roles
- Highlight incident response responsibilities


**RACI Matrix:**

- Export or screenshot
- Verify with stakeholders before submitting


## Training Evidence

**Training Records:**

- HR system export showing completion rates
- Certificates (e.g., SANS certifications)
- Exercise reports (tabletop after-action reports)


**Exercise Scenarios:**

- Tabletop scenario documents
- Participant lists
- Lessons learned documentation


## Tools Evidence

**Tool Inventory:**

- List of incident response tools (name, version, purpose)
- Tool integration diagram (how tools connect)


**Tool Screenshots:**

- Incident ticketing system (ticket example, dashboard)
- SIEM (alert rule example, log search)
- Forensic workstation (tool installation, write blocker)


**Configuration Evidence:**

- SIEM log source count (screenshot)
- Playbook list (SOAR platform)
- Threat intel feed configuration


## Integration Evidence

**Cross-Control References:**

- ISMS-IMP-A.8.15 assessment results (logging)
- ISMS-IMP-A.8.16 assessment results (monitoring)
- BC/DR plan excerpts showing CSIRT integration


**SLA Documents:**

- MSSP contract excerpts (SLA pages)
- Supplier security requirements (incident notification clause)


---

# Common Mistakes to Avoid

## Assessment Mistakes

**❌ Mistake:** Solo assessment (CSIRT Manager completes alone without input)
**✅ Solution:** Collaborative assessment (interview HR, Legal, IT Ops, Management)

**❌ Mistake:** Overstating capability ("Yes" for everything to look good)
**✅ Solution:** Honest self-assessment (auditors will verify, gaps are opportunities to improve)

**❌ Mistake:** Ignoring "soft" elements (culture, communication) and focusing only on tools
**✅ Solution:** Balance technical and organizational aspects (procedures, training, roles are as important as tools)

**❌ Mistake:** No evidence collected (claims without proof)
**✅ Solution:** Systematic evidence collection (for every "Yes," have supporting evidence)

**❌ Mistake:** Generic assessment (copy-paste from templates without customization)
**✅ Solution:** Organization-specific assessment (reflect actual state, not aspirational state)

## Gap Analysis Mistakes

**❌ Mistake:** All gaps marked "Critical" (lack of prioritization)
**✅ Solution:** Risk-based prioritization (use criteria: regulatory, operational, risk, effort)

**❌ Mistake:** Vague remediation ("Improve training")
**✅ Solution:** Specific actions ("Conduct tabletop exercise by Q2, 20 participants, ransomware scenario")

**❌ Mistake:** No ownership (gaps listed but no one responsible)
**✅ Solution:** Assign owner and deadline for every gap

**❌ Mistake:** Unrealistic timelines (all gaps remediated in 1 month)
**✅ Solution:** Realistic phasing (quick wins first, major projects over 6-12 months)

## Evidence Mistakes

**❌ Mistake:** No evidence folder organization (random files, unclear naming)
**✅ Solution:** Structured folder (/Evidence/S1_Framework/ with subfolders)

**❌ Mistake:** Evidence without context (screenshot with no explanation)
**✅ Solution:** Evidence with metadata (filename: "CSIRT_Org_Chart_2026-01-30.pdf", Evidence Register entry)

**❌ Mistake:** Sensitive data in evidence (personal info, credentials)
**✅ Solution:** Redact sensitive data, use anonymized examples

---

# Assessment Timeline

**Week 1:**

- Day 1-2: Information gathering (policies, docs, records)
- Day 3-4: Stakeholder interviews (CSIRT, Legal, HR, IT Ops)
- Day 5: Evidence collection (screenshots, exports)


**Week 2:**

- Day 6-8: Assessment completion (Sheets 2-6)
- Day 9: Gap analysis (Sheet 7)
- Day 10: Evidence register (Sheet 8)


**Week 3:**

- Day 11: Dashboard and summary (Sheets 9-10)
- Day 12-13: Quality review (self-assessment, peer review)
- Day 14: Submit for CISO approval


**Week 4:**

- Day 15-18: CISO review and feedback
- Day 19: Revisions (if needed)
- Day 20: Final approval and filing


**Total:** 4 weeks (part-time effort) or 2 weeks (dedicated full-time effort)

---

# After Assessment Completion

## Review & Approval

**Step 1: Self-Review**

- Review assessment against ISMS-POL-A.5.24-28 requirements
- Verify evidence completeness
- Check calculations (scoring, percentages)


**Step 2: Peer Review (CSIRT Team)**

- Present findings to CSIRT team
- Validate accuracy (do they agree with assessment?)
- Refine gap priorities based on team input


**Step 3: Management Review (CISO)**

- Submit assessment to CISO
- Brief CISO on findings (strengths, gaps, recommendations)
- Request approval and remediation budget (if needed)


**Step 4: Final Approval & Documentation**

- CISO signs approval
- File assessment in ISMS document repository
- Schedule next review (12 months from approval date)


## Gap Remediation Planning

**Create Remediation Project Plan:**

- List all gaps (from Gap Analysis sheet)
- Prioritize (Critical → High → Medium → Low)
- Assign owners
- Set deadlines
- Allocate budget/resources
- Track progress (project management tool, monthly reviews)


**Quick Wins (0-3 months):**

- Document RACI matrix
- Update contact lists
- Schedule next tabletop exercise
- Fix tool integration issues


**Medium-Term (3-6 months):**

- Develop missing procedures/playbooks
- Conduct training for new tools
- Implement SIEM integration
- Hire additional CSIRT staff (if budget approved)


**Long-Term (6-12 months):**

- Deploy SOAR platform
- Establish forensic lab
- Achieve certifications (CSIRT members)
- Mature to next maturity level


## Continuous Improvement

**Triggers for Re-Assessment:**

- Annual review (scheduled)
- Major organizational change (merger, acquisition, restructuring)
- Major incident (lessons learned trigger assessment update)
- Audit findings (ISO 27001 audit identifies gaps)
- Regulatory changes (new requirements)


**Continuous Monitoring:**

- Track CSIRT performance metrics monthly
- Review gap remediation progress quarterly
- Update assessment as improvements implemented
- Celebrate wins (maturity level increases, gaps closed)


---

**END OF PART I: USER COMPLETION GUIDE**

---
---

# PART II: TECHNICAL SPECIFICATION

# Workbook Structure & Technical Details

**Audience:** Workbook developers, Python script maintainers

**This section provides technical specifications for workbook generation and automation.**

---

# Sheet 1: Instructions & Legend

## Header Section

**Title Block (Rows 1-3):**

- Row 1: Document Title - "ISMS-IMP-A.5.24-28.S1 — Incident Management Framework Assessment"
- Row 2: Subtitle - "ISO/IEC 27001:2022 - Control A.5.24: Planning and Preparation"
- Row 3: Empty (spacing)


**Styling:**

- Background: Dark blue (RGB 0, 51, 102 or #003366)
- Font: White, Bold, 18pt (Title), 14pt (Subtitle)
- Alignment: Center, Middle
- Row Height: 40px (Title), 30px (Subtitle)


## Document Information Block (Rows 5-15)

```
Row 5:  Document ID:          ISMS-IMP-A.5.24-28.S1
Row 6:  Assessment Area:      Incident Management Framework & Governance (Domain 1)
Row 7:  Related Policy:       ISMS-POL-A.5.24-28, Section 2.1
Row 8:  Version:              1.0
Row 9:  Assessment Date:      [USER INPUT - yellow cell]
Row 10: Completed By:         [USER INPUT - yellow cell]
Row 11: Organization:         [USER INPUT - yellow cell]
Row 12: Review Cycle:         Annual
Row 13: Next Review Date:     [AUTO-CALCULATE: Assessment Date + 12 months]
```

**Column Widths:**

- Column A: 25 (label)
- Column B: 50 (value)


## Assessment Scope (Rows 17-30)

**Section Title (Row 17):** "Assessment Scope"

- Font: Bold, 14pt
- Background: Light blue (RGB 200, 220, 240)


**Scope Description (Rows 18-30):**

- Multi-line text explaining what's included/excluded in this assessment
- Wrap text enabled
- Bullet points for included items (✅) and excluded items (❌)


## Color Legend (Rows 32-40)

**Legend Title (Row 32):** "Color Legend"

| Color | Meaning | RGB | Usage |
|-------|---------|-----|-------|
| Yellow | User Input Required | 255, 255, 200 | Input cells |
| Light Green | Calculated/Auto-filled | 200, 240, 200 | Formula cells |
| White | Read-Only Information | 255, 255, 255 | Instructions, labels |
| Light Gray | Optional/Not Applicable | 220, 220, 220 | Optional fields |
| Light Red | Gap/Issue Identified | 255, 200, 200 | Risk highlighting |
| Light Blue | Section Header | 200, 220, 240 | Section titles |

## Dropdown Options Reference (Rows 42-60)

**Common Dropdowns:**

- Yes / No / Partial / N/A
- Yes - Comprehensive / Yes - Basic / No
- Critical / High / Medium / Low
- Implemented / Partial / Not Implemented
- [Role-specific dropdowns listed]


## Freeze Panes

**Set freeze at Row 5, Column B** so headers remain visible during scrolling.

---

# Sheet 2: Governance Assessment

## Header Row (Row 4)

| Column | Header | Width |
|--------|--------|-------|
| A | Question_ID | 12 |
| B | Section | 15 |
| C | Question | 50 |
| D | Answer | 20 |
| E | Evidence_Reference | 25 |
| F | Comments | 30 |
| G | Gap_Identified | 10 |

**Header Styling:**

- Background: Dark blue (#003366)
- Font: White, Bold, 11pt
- Borders: All borders, white lines
- Alignment: Center, Middle
- Text wrap: Enabled


## Data Rows (Rows 5-29, 25 questions)

**Question Data Validation:**

Q1 (Policy_Exists): Dropdown

- List: Yes, No, In Draft
- Cell: D5
- Input Message: "Does a documented incident management policy exist?"
- Error Alert: "Please select from dropdown list"


Q2 (Policy_Approval_Date): Date

- Cell: D6
- Format: DD.MM.YYYY
- Data Validation: Date, ≤ TODAY()
- Conditional Formatting: If >730 days old (2 years), background light red


Q3 (Policy_Owner): Text

- Cell: D7
- Input Message: "Name and title of policy owner (typically CISO)"


Q4 (Policy_Review_Frequency): Dropdown

- List: Annually, Bi-Annually, Quarterly, Ad-Hoc, Not Defined
- Cell: D8


Q5 (Last_Policy_Review_Date): Date

- Cell: D9
- Format: DD.MM.YYYY
- Conditional Formatting: If > 365 days old, background light red


[Continue pattern for Q6-Q25]

**Conditional Formatting Rules:**

**Rule 1: Highlight "No" Answers (High Risk)**

- Applies to: Column D (Answer cells)
- Condition: Cell Value = "No"
- Format: Background light red (255, 200, 200)


**Rule 2: Highlight "Partial" Answers (Medium Risk)**

- Condition: Cell Value = "Partial" OR "Yes - Partial" OR "Informal"
- Format: Background light yellow (255, 255, 200)


**Rule 3: Highlight Overdue Dates**

- Applies to: Date cells (Policy Review, Training dates, etc.)
- Condition: Value < TODAY() - 365
- Format: Background light red + Bold red text


**Gap_Identified Column (Column G):**

- Formula: `=IF(OR(D5="No", D5="Partial", D5="Informal"), "Yes", "No")`
- Conditional Formatting: If "Yes", background light red


## Section Headers (Within Rows)

Insert blank rows with section headers:

- Row 5: "Section A: Policy Documentation" (merged A5:G5, light blue background, bold)
- Row 11: "Section B: Procedure Documentation"
- Row 17: "Section C: Authority & Escalation"
- Row 22: "Section D: Regulatory Compliance"
- Row 27: "Section E: Exception Management"
- Row 29: "Section F: Policy Governance"


---

# Sheet 3: Organizational Structure

## Header Row (Row 4)

Same structure as Sheet 2 (Question_ID, Section, Question, Answer, Evidence, Comments, Gap)

## Data Rows (Rows 5-60, 30 questions + role definitions)

**Section A: CSIRT/SOC Model (Q26-Q30)**

Q26 (Incident_Response_Model): Dropdown

- List: Dedicated CSIRT, Virtual CSIRT, Hybrid, Outsourced SOC/MSSP, Coordinated
- Cell: D5


Q27 (CSIRT_Establishment_Date): Date

- Format: MM.YYYY
- Conditional Formatting: Calculate age, color-code maturity


Q28 (CSIRT_Coverage): Dropdown

- List: 24/7/365, Business Hours Only, Extended Hours, On-Call Rotation


Q29 (CSIRT_Staffing_Level): Number

- Data Validation: Whole number, ≥0
- Conditional Formatting: 
  - <2 FTE: Red (understaffed)
  - 2-5 FTE: Yellow (adequate for small org)
  - >5 FTE: Green (well-staffed)


Q30 (CSIRT_Reporting_Structure): Text

- Input Message: "Title/Department (e.g., CISO, CIO, COO)"


**Section B: Role Definitions (Q31-Q45, 15 roles)**

For each role (4 columns per role):

- Role_Exists: Yes/No dropdown
- Role_Definition: Text (brief description)
- Assigned_To: Text (Name or "Vacant")
- RACI_Clarity: Dropdown (Clear, Unclear, Not Documented)


Example for Q31 (Incident_Manager):

- D11 (Role_Exists): Dropdown (Yes / No)
- E11 (Role_Definition): Text
- F11 (Assigned_To): Text
- G11 (RACI_Clarity): Dropdown


[Repeat for 15 roles: Q31-Q45]

**Section C: RACI Matrix (Q46-Q48)**

Q46 (RACI_Matrix_Exists): Dropdown (Yes - Comprehensive, Yes - Basic, No)
Q47 (RACI_Clarity_Assessment): Dropdown (Very Clear, Mostly Clear, Some Ambiguity, Significant Confusion)
Q48 (RACI_Last_Updated): Date

**Section D: Staffing Adequacy (Q49-Q52)**

Q49 (Staffing_Adequate): Dropdown (Yes, No, Barely Adequate)
Q50 (Turnover_Rate): Percentage (Data Validation: 0-100%)
Q51 (Succession_Planning): Dropdown (Yes, Informal, No)
Q52 (Skills_Gaps_Identified): Dropdown (Yes - Documented, Informally Identified, No)

**Section E: Management Visibility (Q53-Q55)**

Q53 (Management_Reporting_Frequency): Dropdown (Weekly, Monthly, Quarterly, Ad-Hoc, Never)
Q54 (CSIRT_Performance_Metrics): Dropdown (Yes - Comprehensive, Yes - Basic, No)
Q55 (Board_Briefing_Protocol): Dropdown (Yes, Informal, No, N/A)

---

# Sheet 4: Training & Competency

## Header Row (Row 4)

Same structure: Question_ID, Section, Question, Answer, Evidence, Comments, Gap

## Data Rows (Rows 5-35, 25 questions)

**Section A: Training Program (Q56-Q60)**

Q56 (Training_Program_Exists): Dropdown (Yes - Comprehensive, Yes - Basic, No)
Q57 (Annual_Awareness_Training): Dropdown (Yes, Partial, No)
Q58 (Awareness_Training_Completion_Rate): Percentage

  - Conditional Formatting: <95% red, 95-99% yellow, ≥99% green

Q59 (CSIRT_Specialized_Training): Dropdown (Yes - Regular, Yes - Occasional, No)
Q60 (External_Training_Budget): Dropdown (Yes - Adequate, Yes - Limited, No)

**Section B: Tabletop Exercises (Q61-Q65)**

Q61 (Tabletop_Exercise_Frequency): Dropdown (Quarterly, Semi-Annually, Annually, Bi-Annually, Never)
Q62 (Last_Tabletop_Date): Date

  - Conditional Formatting: >365 days = Red

Q63 (Tabletop_Scenario_Variety): Dropdown (Yes - Diverse, Limited Variety, Single Scenario Type)
Q64 (Tabletop_Participants): Checkbox (Multiple)

  - CSIRT, IT Ops, Legal, HR, Management, Executive, Board, External Partners

Q65 (Tabletop_Lessons_Learned): Dropdown (Yes - Systematically, Yes - Informally, No)

**Section C: Simulation & Testing (Q66-Q68)**

Q66 (Full_Scale_Exercises): Dropdown (Yes - Regularly, Yes - Occasionally, No)
Q67 (Breach_Simulation_Tools): Dropdown (Yes, No)
Q68 (Regulatory_Drills): Dropdown (Yes, No)

**Section D: Competency & Certification (Q69-Q72)**

Q69 (Competency_Requirements_Defined): Dropdown (Yes, No)
Q70 (Certification_Tracking): Dropdown (Yes, Informal, No)
Q71 (Certification_Currency): Dropdown (Yes - All Current, Some Expired, Not Tracked)
Q72 (New_Hire_Onboarding): Dropdown (Yes - Formal Program, Informal, No)

**Section E: Training Effectiveness (Q73-Q75)**

Q73 (Training_Effectiveness_Measured): Dropdown (Yes, No)
Q74 (Training_Feedback_Collected): Dropdown (Yes - Systematically, Occasionally, No)
Q75 (Training_Gaps_Identified): Dropdown (Yes - Documented, Informally Identified, No)

---

# Sheet 5: Tools & Technology

## Header Row (Row 4)

Same structure.

## Data Rows (Rows 5-50, 30 questions)

**Section A: Ticketing (Q76-Q79)**

Q76 (Ticketing_System_Exists): Dropdown (Yes - Dedicated IR, Yes - General IT, No)
Q77 (Ticketing_System_Features): Checkbox (Multiple selections)

  - Incident creation, Severity, Timeline, Evidence, Tasks, Collaboration, Escalation, Integration, Reporting, Playbooks

Q78 (Ticket_Retention): Dropdown (1 year, 3 years, 5 years, 7+ years, Indefinitely, Not Defined)
Q79 (Ticket_Access_Control): Dropdown (Yes - Strict, Yes - Moderate, No - Open)

**Section B: SIEM (Q80-Q83)**

Q80 (SIEM_Deployed): Dropdown (Yes - Fully Operational, Yes - Partial, No)
Q81 (SIEM_Log_Sources): Number

  - Conditional Formatting: <20 red, 20-50 yellow, >50 green

Q82 (SIEM_Integration_Ticketing): Dropdown (Yes - Fully Automated, Yes - Semi-Automated, Manual, N/A)
Q83 (SIEM_Playbook_Automation): Dropdown (Yes - Extensive, Yes - Limited, No, N/A)

**Section C: Forensics (Q84-Q87)**

Q84 (Forensic_Tools_Available): Checkbox (Multiple)

  - Disk imaging, Memory acquisition, Memory analysis, Network forensics, Log analysis, Malware analysis, Mobile forensics, Cloud forensics, Commercial suites, None

Q85 (Forensic_Tool_Training): Dropdown (Yes - All Members, Yes - Specialized Roles, Limited, No)
Q86 (Forensic_Workstation): Dropdown (Yes - Dedicated Lab, Yes - Virtual, No)
Q87 (Evidence_Storage): Dropdown (Yes - Dedicated, Yes - General, No)

**Section D: Communication (Q88-Q90)**

Q88 (Internal_Communication_Tools): Checkbox

  - Email, Phone, IM (Slack/Teams), Video, War Room, IR Platform, Encrypted

Q89 (External_Communication_Secure): Dropdown (Yes, No)
Q90 (On_Call_Alerting): Dropdown (PagerDuty, VictorOps, Phone, SMS, Email, No System)

**Section E: Threat Intel (Q91-Q93)**

Q91 (Threat_Intel_Feeds): Dropdown (Yes - Multiple, Yes - Single, No)
Q92 (Threat_Intel_Integration_SIEM): Dropdown (Yes - Automated, Yes - Manual, No, N/A)
Q93 (Threat_Intel_Analyst_Role): Dropdown (Yes - Dedicated, Yes - Part-Time, No - CSIRT Handles)

**Section F: Automation (Q94-Q96)**

Q94 (IR_Automation): Dropdown (High (SOAR), Moderate (Some Playbooks), Low (Mostly Manual), None)
Q95 (Playbook_Count): Number
Q96 (Playbook_Maintenance): Dropdown (Yes - Annually, Yes - After Incidents, No, N/A)

**Section G: Gaps (Q97-Q99)**

Q97 (Critical_Tool_Gaps): Dropdown (Yes - Multiple, Yes - Some, No)
Q98 (Tool_Procurement_Planned): Dropdown (Yes - Funded, Proposed, No)
Q99 (Tool_Integration_Challenges): Dropdown (Yes - Significant, Yes - Moderate, No, N/A)

---

# Sheet 6: Integration Assessment

## Header Row (Row 4)

Same structure.

## Data Rows (Rows 5-35, 25 questions)

**Sections A-F as outlined in Part I:**

- Logging Integration (Q100-Q102)
- Monitoring Integration (Q103-Q105)
- User Reporting Integration (Q106-Q108)
- BC/DR Integration (Q109-Q111)
- Third-Party Coordination (Q112-Q114)
- Legal & Regulatory (Q115-Q117)


Each question follows dropdown or text pattern as defined in Part I.

---

# Sheet 7: Gap Analysis

## Header Row (Row 4)

| Column | Header | Width |
|--------|--------|-------|
| A | Gap_ID | 10 |
| B | Assessment_Section | 15 |
| C | Gap_Description | 40 |
| D | Risk_Level | 10 |
| E | Current_State | 25 |
| F | Target_State | 25 |
| G | Remediation_Action | 35 |
| H | Owner | 15 |
| I | Target_Date | 12 |
| J | Status | 10 |

## Data Rows (Rows 5-64, 60 gap capacity)

**Gap_ID:**

- Format: GAP-001, GAP-002, etc.
- Auto-populate: `="GAP-" & TEXT(ROW()-4, "000")`


**Assessment_Section:** Dropdown

- List: Governance, Structure, Training, Tools, Integration


**Gap_Description:** Text

- Wrap text enabled


**Risk_Level:** Dropdown

- List: Critical, High, Medium, Low
- Conditional Formatting:
  - Critical: Red background
  - High: Orange background
  - Medium: Yellow background
  - Low: Green background


**Current_State, Target_State:** Text

**Remediation_Action:** Text

- Wrap text enabled


**Owner:** Text

**Target_Date:** Date

- Format: DD.MM.YYYY
- Conditional Formatting: If past due, red text


**Status:** Dropdown

- List: Open, In Progress, Resolved, Accepted (risk acceptance)


## Gap Summary (Rows 70-80)

**By Risk Level:**
```
Row 70: Total Gaps:     =COUNTA(A5:A64)
Row 71: Critical:       =COUNTIF(D5:D64, "Critical")
Row 72: High:           =COUNTIF(D5:D64, "High")
Row 73: Medium:         =COUNTIF(D5:D64, "Medium")
Row 74: Low:            =COUNTIF(D5:D64, "Low")
```

**By Status:**
```
Row 76: Open:           =COUNTIF(J5:J64, "Open")
Row 77: In Progress:    =COUNTIF(J5:J64, "In Progress")
Row 78: Resolved:       =COUNTIF(J5:J64, "Resolved")
Row 79: Accepted:       =COUNTIF(J5:J64, "Accepted")
```

---

# Sheet 8: Evidence Register

## Header Row (Row 4)

| Column | Header | Width |
|--------|--------|-------|
| A | Evidence_ID | 12 |
| B | Evidence_Type | 15 |
| C | Description | 35 |
| D | Related_Section | 15 |
| E | Storage_Location | 30 |
| F | Date_Collected | 12 |
| G | Collected_By | 15 |
| H | Verification_Status | 15 |

## Data Rows (Rows 5-104, 100 evidence capacity)

**Evidence_ID:**

- Format: EV-001, EV-002, etc.
- Auto-populate: `="EV-" & TEXT(ROW()-4, "000")`


**Evidence_Type:** Dropdown

- List: Policy Document, Procedure, Org Chart, Job Description, RACI Matrix, Training Record, Exercise Report, Tool Screenshot, Contract/SLA, Metrics Report, Other


**Description:** Text

**Related_Section:** Dropdown

- List: Governance, Structure, Training, Tools, Integration, Multiple


**Storage_Location:** Text

- Format: Filepath or URL


**Date_Collected:** Date

**Collected_By:** Text

**Verification_Status:** Dropdown

- List: Verified, Pending, Needs Review
- Conditional Formatting: Verified = green, Pending = yellow


---

# Sheet 9: Dashboard

## Overall Maturity Score (Rows 6-15)

**Maturity Calculation Formula:**

```excel
Governance_Score (from Sheet2):  
  =COUNTIF(Sheet2!G:G, "No") / COUNTA(Sheet2!G:G) * 100
  (Inverted: 100% - gap percentage = compliance %)

Structure_Score (from Sheet3):
  Similar calculation

Training_Score (from Sheet4):
  Similar calculation

Tools_Score (from Sheet5):
  Similar calculation

Integration_Score (from Sheet6):
  Similar calculation

Overall_Maturity_Score:
  =(Governance*25% + Structure*20% + Training*20% + Tools*20% + Integration*15%)
```

**Maturity Level Determination:**

```excel
=IF(Overall_Score<40, "Level 1 (Initial)", 
  IF(Overall_Score<60, "Level 2 (Developing)",
    IF(Overall_Score<75, "Level 3 (Defined)",
      IF(Overall_Score<90, "Level 4 (Managed)", 
        "Level 5 (Optimizing)"))))
```

## Domain Scores (Rows 20-30)

Table format:
| Domain | Score (%) | Target | Status |
|--------|-----------|--------|--------|
| Governance | [Formula] | 90% | [Green/Yellow/Red] |
| Structure | [Formula] | 85% | [Light] |
| Training | [Formula] | 90% | [Light] |
| Tools | [Formula] | 80% | [Light] |
| Integration | [Formula] | 85% | [Light] |

**Conditional Formatting (Status Column):**

- Green: Score ≥ Target
- Yellow: Score 70-90% of Target
- Red: Score < 70% of Target


## Key Metrics (Rows 35-50)

```
CSIRT Staffing (FTE):              =Sheet3!D29
Coverage Model:                    =Sheet3!D28
Training Completion Rate:          =Sheet4!D8
Tabletop Exercise Frequency:       =Sheet4!D11
Tool Count:                        [Manual count from Sheet5]
Critical Gaps:                     =COUNTIF(Sheet7!D:D, "Critical")
High Gaps:                         =COUNTIF(Sheet7!D:D, "High")
```

## Top 10 Gaps (Rows 55-65)

Extract top 10 gaps by Risk_Level from Sheet 7:

- Sort by: Critical > High > Medium > Low
- Display: Gap_Description, Risk_Level, Owner, Target_Date


**Formula (using FILTER or manual reference):**
```excel
=FILTER(Sheet7!C5:C64, Sheet7!D5:D64="Critical")
```
(Adjust for Excel version if FILTER not available - use manual reference or VBA)

---

# Sheet 10: Approval Sign-Off

## Assessment Summary (Rows 5-20)

```
Assessment Period:          [Start Date] - [End Date]
Completed By:               [Name, Title]
Assessment Date:            [Date]
Overall Maturity Level:     =Sheet9!B10 (reference Dashboard calculation)
Overall Maturity Score:     =Sheet9!B8 (percentage)

Key Findings:
  Strengths:                [Text box, manually entered]
  Critical Gaps:            [Text box, reference Sheet 7]
  Remediation Priority:     [Text box, manually entered]
```

## Approval Workflow (Rows 25-35)

| Role | Name | Date | Signature | Status |
|------|------|------|-----------|--------|
| Assessor (CSIRT Manager) | [Input] | [Input] | [Digital or Manual] | Submitted / Pending |
| Reviewer (CISO) | [Input] | [Input] | [Digital or Manual] | Approved / Revisions Required |
| Next Review Date | - | [Assessment Date + 12 months] | - | - |

**Status Dropdown:**

- Assessor: Submitted / Pending
- Reviewer: Approved / Revisions Required


**Conditional Formatting:**

- Approved: Green highlight
- Revisions Required: Yellow highlight


---

# Cell Styling Reference

## Standard Styles

**User Input Cells:**

- Background: Yellow (255, 255, 200)
- Border: Thin black
- Protection: Unlocked


**Calculated Cells:**

- Background: Light green (200, 240, 200)
- Border: Thin black
- Protection: Locked


**Headers:**

- Background: Dark blue (0, 51, 102)
- Font: White, Bold, 11pt
- Border: White lines
- Alignment: Center, Middle


**Section Headers:**

- Background: Light blue (200, 220, 240)
- Font: Bold, 12pt
- Merge cells across row


**Conditional Formatting Colors:**

- Red (Risk/Gap): RGB 255, 200, 200
- Yellow (Warning): RGB 255, 255, 200
- Green (Good): RGB 200, 240, 200
- Orange (Medium): RGB 255, 220, 180


---

# Data Validation Rules

## Dropdown Lists

Store dropdown lists in a hidden sheet ("Lists"):
```
Sheet: Lists (Hidden)
Column A: Yes_No_Partial = Yes, No, Partial, N/A
Column B: Risk_Levels = Critical, High, Medium, Low
Column C: Status_Options = Open, In Progress, Resolved, Accepted
Column D: [Other dropdown lists as needed]
```

**Apply Named Ranges:**

- Define name "YesNoPartial" for Lists!A:A
- Define name "RiskLevels" for Lists!B:B
- etc.


**Data Validation Formula:**
```excel
=YesNoPartial
```

## Date Validation

**Rule:** Date must be ≤ TODAY()
**Error Message:** "Date cannot be in the future"

**Rule:** Date within reasonable range (e.g., 1990-2030)

## Number Validation

**Percentages:** 0-100, whole number or decimal
**FTE Count:** ≥0, whole number or decimal (0.5 acceptable)
**Tool Count:** ≥0, whole number

---

# Protection Settings

**Sheet Protection:**

- Enable for all sheets except "Instructions & Legend"
- Password: [Set organization-specific password]
- Allow: Select unlocked cells, Format cells (locked and unlocked)
- Disallow: Insert/delete rows, columns


**Unlocked Cells:**

- All yellow (user input) cells
- Evidence Register description cells


**Locked Cells:**

- All calculated cells
- Headers and labels
- Instructions


---

# Formula Examples

## Gap Identification

```excel
='Sheet2'!G5  (Gap_Identified column)
=IF(OR(D5="No", D5="Partial", D5="Informal"), "Yes", "No")
```

## Score Calculation

```excel
='Sheet9'!B8 (Overall Maturity Score)
=(Governance_Score*0.25 + Structure_Score*0.20 + Training_Score*0.20 + Tools_Score*0.20 + Integration_Score*0.15)

Where:
Governance_Score = 100 - (COUNTIF(Sheet2!G:G, "Yes") / COUNTA(Sheet2!G:G) * 100)
```

## Conditional Cell References

```excel
Next Review Date (Sheet10):
=IF(ISBLANK(Sheet10!B8), "", Sheet10!B8 + 365)
(If Assessment Date blank, leave blank; otherwise, add 365 days)
```

---

# File Naming Convention

**Format:** `ISMS-IMP-A.5.24-28.S1_Framework_Assessment_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.5.24-28.S1_Framework_Assessment_20260130.xlsx`

---

# Excel Version Compatibility

**Target Version:** Excel 2016 or later (Windows/Mac), Office 365

**Features Used:**

- Data Validation (dropdown lists)
- Conditional Formatting (color scales, rules)
- Named Ranges
- Cell Protection
- Basic formulas (IF, COUNTIF, COUNTA, FILTER if available)


**Compatibility Notes:**

- FILTER function (Excel 365): Provide alternative for Excel 2016 (manual reference or VBA)
- Conditional Formatting: Test in Excel 2016 to ensure compatibility
- No Power Query or Pivot Tables used (keep simple for broad compatibility)


---

# Workbook Generation Script Template

**Python Script:** `generate_a524_28_s1_framework_assessment.py`

**Libraries:**

- `openpyxl` (Excel file creation and manipulation)
- `datetime` (date handling)


**Script Structure:**
1. Create workbook
2. Create sheets (Instructions, Governance, Structure, Training, Tools, Integration, Gaps, Evidence, Dashboard, Approval)
3. Set column widths
4. Create headers with styling
5. Add data validation (dropdowns)
6. Add conditional formatting
7. Add formulas (gap identification, scoring)
8. Protect sheets (leave input cells unlocked)
9. Save workbook with timestamp

**Script Length:** ~400-500 lines (comprehensive header documentation + implementation)

---
**END OF SPECIFICATION**

---

*"I beg to introduce myself to you as a clerk in the Accounts Department... I have no university education... but I have been employing my spare time in mathematics."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-01 -->
