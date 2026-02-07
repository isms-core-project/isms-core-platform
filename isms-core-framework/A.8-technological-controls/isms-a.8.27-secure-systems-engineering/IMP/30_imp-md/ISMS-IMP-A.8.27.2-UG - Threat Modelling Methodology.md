**ISMS-IMP-A.8.27.2-UG - Threat Modelling Methodology**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Threat Modelling Methodology |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.2-UG |
| **Assessment Domain** | Domain 2 - Threat Analysis and Modelling |
| **Related Policy** | ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Security Architect / Threat Modelling Lead |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect | Initial threat modelling assessment specification |

**Review Cycle**: Annual (or after methodology changes)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles)
- ISMS-IMP-A.8.27.1 (Security Architecture Review Process)
- ISMS-IMP-A.8.27.3 (Secure Architecture Pattern Catalogue)
- ISMS-IMP-A.8.27.4 (Zero Trust Implementation Assessment)
- ISMS-POL-A.5.7 (Threat Intelligence)
- ISO/IEC 27002:2022 Control A.8.27
- MITRE ATT&CK Framework
- STRIDE Methodology (Microsoft)
- PASTA Threat Modelling Framework

---

# Assessment Overview

## Purpose

This assessment evaluates [Organisation]'s **threat modelling methodology and capabilities**, focusing on the systematic identification, analysis, and mitigation of threats as mandated by ISMS-POL-A.8.27.

**What This Assessment Covers:**

- Threat modelling methodology selection and adoption
- Threat identification techniques (STRIDE, PASTA, Attack Trees)
- MITRE ATT&CK integration and usage
- Threat model documentation standards
- Threat modelling tooling and automation
- Integration with architecture review process
- Threat model maintenance and updates
- Team competency and training

**What This Assessment Does NOT Cover:**

- Architecture review governance (see ISMS-IMP-A.8.27.1)
- Secure architecture patterns (see ISMS-IMP-A.8.27.3)
- Zero Trust implementation (see ISMS-IMP-A.8.27.4)
- Vulnerability management (see ISMS-IMP-A.8.8)

**Assessment Output:**

- Excel workbook documenting threat modelling capability maturity
- Methodology compliance assessment
- MITRE ATT&CK coverage analysis
- Tool effectiveness evaluation
- Training and competency gaps

## Why This Matters

**ISO/IEC 27001:2022 Control A.8.27 Requirement:**
> *"Principles for engineering secure systems should be established, documented, maintained and applied to any information system development activities."*

**NIST SP 800-160 Vol. 1 Rev. 1 Guidance:**
> *"Threat modelling identifies potential threats to a system and evaluates the system's susceptibility to those threats. It is a critical activity in understanding what needs to be protected and from what."*

**Business Impact of Inadequate Threat Modelling:**

- **Missed Threats:** Unidentified attack vectors lead to exploitable vulnerabilities
- **Misallocated Resources:** Security investments not aligned with actual threats
- **Compliance Gaps:** Auditors expect documented threat analysis
- **Design Flaws:** Architectural decisions made without threat context
- **Incident Response:** Unknown threats cannot be detected or responded to

**This Assessment Addresses:**

- Do we have a defined threat modelling methodology?
- Is MITRE ATT&CK integrated into threat analysis?
- Are threat models created for all new systems?
- Are threat models maintained as systems evolve?
- Do our teams have threat modelling competency?

## Who Should Complete This Assessment

**Primary Responsibility:** Security Architect or Threat Modelling Lead

**Required Knowledge:**

- [Organisation]'s threat modelling procedures
- STRIDE, PASTA, or other threat modelling methodologies
- MITRE ATT&CK Framework
- Threat modelling tools in use
- Integration with architecture review process

**Support Roles:**

- **CISO:** Methodology approval, resource allocation
- **Threat Intelligence Team:** Threat landscape input
- **Development Teams:** Threat model consumers
- **Security Operations:** Attack detection correlation
- **Red Team:** Adversary simulation perspective

**Collaboration Required:**

- Threat modelling practitioners
- Sample threat models
- Tool demonstrations

## Time Estimate

**Total Assessment Time:** 8-12 hours

**Breakdown:**

- **Information Gathering:** 3-4 hours
  - Review threat modelling methodology documentation
  - Collect sample threat models
  - Gather MITRE ATT&CK mapping evidence
  - Inventory threat modelling tools

- **Assessment Completion:** 3-4 hours
  - Document methodology compliance
  - Assess MITRE ATT&CK coverage
  - Evaluate tool effectiveness
  - Review training and competency

- **Evidence Collection:** 1-2 hours
  - Sample threat model documents
  - Tool screenshots
  - Training records
  - MITRE ATT&CK mappings

- **Quality Review:** 1-2 hours
  - Gap analysis
  - Remediation planning
  - Stakeholder review

## Connection to Policy

This assessment implements **ISMS-POL-A.8.27, Section 2.2 (Architecture Security Review)** which mandates:

**Review Process Requirements:**

1. **Threat modelling using structured methodology** (STRIDE, PASTA, or equivalent)
2. Security requirements validation against business requirements
3. Architecture pattern review against approved patterns
4. Control design review for defence in depth
5. Risk assessment and residual risk documentation

**Threat Model Expectations:**

- Threat identification aligned with MITRE ATT&CK
- Attack vector analysis for system boundaries
- Trust boundary identification
- Data flow threat analysis
- Countermeasure mapping

---

# Prerequisites

## Required Access

Before starting this assessment, ensure you have access to:

| System/Resource | Purpose | Who Can Provide |
|-----------------|---------|-----------------|
| Threat modelling methodology docs | Methodology definition | Security Architect |
| Sample threat models | Completed examples | Project teams |
| MITRE ATT&CK reference | Framework alignment | Threat Intelligence |
| Threat modelling tools | Tool assessment | Security Engineering |
| Training records | Competency evidence | HR/Training |

## Pre-Assessment Checklist

✅ Threat modelling methodology reviewed
✅ Access to sample threat models confirmed (minimum 3)
✅ MITRE ATT&CK Navigator access available
✅ Threat modelling tool access granted
✅ Practitioner interviews scheduled
✅ Assessment timeframe communicated

## Information Gathering Requirements

**Collect the following before completing the assessment:**

| Category | Required Information | Source |
|----------|---------------------|--------|
| **Methodology** | Methodology documentation, procedures | Security Architecture |
| **MITRE ATT&CK** | ATT&CK mappings, coverage analysis | Threat Intelligence |
| **Samples** | 3+ completed threat models | Project documentation |
| **Tools** | Tool inventory, licenses, usage data | Security Engineering |
| **Training** | Training materials, completion records | HR/Training |
| **Metrics** | Threat model counts, coverage, findings | ISMS dashboard |

---

# Completion Walkthrough

## Step 1: Review Instructions

1. Open the workbook and navigate to the **Instructions** sheet
2. Review STRIDE and PASTA methodology overviews
3. Understand MITRE ATT&CK framework basics
4. Note the rating scales and evidence requirements

## Step 2: Complete Methodology Assessment

**Navigate to the Methodology sheet**

For each methodology component:

1. **Identify Adoption:** Is this methodology component adopted?
2. **Check Documentation:** Is it documented in procedures?
3. **Rate Effectiveness:** How effective is the implementation? (1-5)
4. **Provide Evidence:** Reference supporting documentation
5. **Note Gaps:** What is missing or needs improvement?

**Methodology Components to Assess:**

| Component | Description |
|-----------|-------------|
| **Methodology Selection** | Which methodology(ies) adopted? |
| **Scope Definition** | How is threat model scope defined? |
| **Asset Identification** | How are assets identified? |
| **Threat Identification** | How are threats identified? (STRIDE?) |
| **Attack Surface Analysis** | How is attack surface mapped? |
| **Trust Boundaries** | How are trust boundaries identified? |
| **Data Flow Analysis** | How are data flows analysed? |
| **Threat Prioritisation** | How are threats prioritised? |
| **Countermeasure Mapping** | How are mitigations identified? |
| **Documentation Standards** | What documentation is required? |
| **Review Process** | How are threat models reviewed? |
| **Maintenance Process** | How are threat models updated? |

## Step 3: Complete MITRE ATT&CK Assessment

**Navigate to the MITRE_ATT&CK sheet**

For relevant ATT&CK techniques:

1. **Assess Relevance:** Is this technique relevant to [Organisation]?
2. **Check Coverage:** Is it included in threat models?
3. **Map Detection:** What detection capabilities exist?
4. **Note Gaps:** Where is coverage missing?

**Focus Areas:**

| Tactic | Priority Techniques |
|--------|-------------------|
| **Initial Access** | T1566 (Phishing), T1190 (Exploit Public-Facing App), T1133 (External Remote Services) |
| **Execution** | T1059 (Command and Scripting), T1204 (User Execution) |
| **Persistence** | T1078 (Valid Accounts), T1136 (Create Account) |
| **Privilege Escalation** | T1068 (Exploitation), T1548 (Abuse Elevation Control) |
| **Defense Evasion** | T1562 (Impair Defenses), T1070 (Indicator Removal) |
| **Credential Access** | T1110 (Brute Force), T1555 (Credentials from Password Stores) |
| **Lateral Movement** | T1021 (Remote Services), T1550 (Use Alternate Authentication) |
| **Collection** | T1005 (Data from Local System), T1114 (Email Collection) |
| **Exfiltration** | T1041 (Exfiltration Over C2), T1567 (Exfiltration Over Web Service) |
| **Impact** | T1486 (Data Encrypted for Impact), T1489 (Service Stop) |

## Step 4: Complete Threat Catalogue Assessment

**Navigate to the ThreatCatalogue sheet**

For each threat category:

1. **Define Threat Actors:** Who threatens [Organisation]?
2. **Assess Motivation:** What motivates each actor?
3. **Rate Capability:** How capable is each actor?
4. **Map to ATT&CK:** Which techniques do they use?
5. **Assess Likelihood:** How likely is an attack?
6. **Document Countermeasures:** What controls address this?

**Standard Threat Actor Categories:**

| Category | Examples |
|----------|----------|
| **Nation-State** | APT groups targeting industry |
| **Cybercriminal** | Ransomware operators, data thieves |
| **Hacktivist** | Ideologically motivated groups |
| **Insider** | Malicious or negligent employees |
| **Competitor** | Corporate espionage |
| **Script Kiddie** | Opportunistic attackers |

## Step 5: Complete Tools Assessment

**Navigate to the Tools sheet**

For each threat modelling tool:

1. **Inventory Tools:** What tools are available?
2. **Check Licensing:** Are licenses current?
3. **Count Users:** How many active users?
4. **Assess Integration:** How does it integrate with SDLC?
5. **Rate Effectiveness:** How effective is the tool? (1-5)
6. **Note Limitations:** What are tool gaps?

**Common Threat Modelling Tools:**

| Tool | Capability |
|------|------------|
| Microsoft Threat Modeling Tool | DFD-based, STRIDE analysis |
| OWASP Threat Dragon | Open source, DFD-based |
| IriusRisk | Commercial, automation |
| Threagile | Code-as-code, CI/CD integration |
| ThreatModeler | Enterprise, cloud integration |

## Step 6: Complete Competency Assessment

**Navigate to the Competency sheet**

For each role requiring threat modelling competency:

1. **Identify Roles:** Which roles need competency?
2. **Define Competencies:** What competencies are required?
3. **Check Training:** Is training available?
4. **Count Certified:** How many are trained/certified?
5. **Note Gaps:** Where are competency gaps?

**Required Competencies:**

| Competency | Target Roles |
|------------|-------------|
| **STRIDE Methodology** | Security Architects, Senior Developers |
| **PASTA Framework** | Security Architects |
| **MITRE ATT&CK** | Security Architects, SOC Analysts |
| **Data Flow Diagramming** | Architects, Senior Developers |
| **Attack Tree Analysis** | Security Architects, Red Team |
| **Risk Assessment** | Security Architects, Project Managers |

## Step 7: Complete Sample Review

**Navigate to the Samples sheet**

Review 3+ sample threat models:

1. **Identify Samples:** Select representative threat models
2. **Check Completeness:** Does it cover all required elements?
3. **Rate Quality:** Is analysis thorough and accurate?
4. **Verify ATT&CK Mapping:** Are techniques properly mapped?
5. **Count Findings:** How many threats identified?
6. **Count Mitigations:** How many mitigations documented?

**Quality Criteria:**

| Criterion | Expectation |
|-----------|-------------|
| Scope clearly defined | Yes |
| Assets identified | All critical assets |
| Data flows documented | Complete DFD |
| Trust boundaries marked | Clear boundaries |
| Threats systematic (STRIDE) | All STRIDE categories |
| ATT&CK techniques mapped | Relevant techniques |
| Prioritisation applied | Risk-based ranking |
| Mitigations documented | For high/critical threats |
| Residual risk stated | Explicitly documented |
| Review sign-off | Approved by Security Architect |

## Step 8: Complete Compliance Scoring

**Navigate to the Compliance sheet**

For each policy requirement:

1. **Map Requirements:** List requirements from ISMS-POL-A.8.27
2. **Assess Compliance:** Yes/Partial/No
3. **Document Evidence:** What proves compliance?
4. **Calculate Score:** Apply scoring formula

## Step 9: Document Gaps and Remediation

**Navigate to the GapRegister sheet**

For each identified gap:

1. **Consolidate Gaps:** Gather all gaps from previous sheets
2. **Rate Risk:** High/Medium/Low
3. **Plan Remediation:** Define specific actions
4. **Assign Ownership:** Identify responsible party
5. **Set Due Dates:** Establish realistic timelines
6. **Track Status:** Monitor progress

---

# Evidence Collection

## Required Evidence

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| **Methodology Doc** | Threat modelling methodology | ISMS Evidence Library |
| **Procedures** | Threat modelling procedures | ISMS Evidence Library |
| **Sample Models** | 3+ completed threat models | Project Documentation |
| **ATT&CK Mapping** | MITRE ATT&CK coverage matrix | Security Architecture |
| **Tool Evidence** | Tool screenshots, licenses | Security Engineering |
| **Training Records** | Practitioner training records | HR/Training |
| **Threat Catalogue** | Organisational threat catalogue | Threat Intelligence |

## Evidence Naming Convention

```
ISMS-IMP-A.8.27.2_[EvidenceType]_[Description]_YYYYMMDD.[ext]
```

**Examples:**

- `ISMS-IMP-A.8.27.2_Methodology_ThreatModellingProcedure_20260115.pdf`
- `ISMS-IMP-A.8.27.2_Sample_CustomerPortalTM_20260115.docx`
- `ISMS-IMP-A.8.27.2_ATT&CK_CoverageMatrix_20260115.xlsx`

---

# Common Pitfalls

Avoid these common mistakes when completing this assessment:

❌ **MISTAKE:** Adopting a methodology without documenting it
✅ **CORRECT:** Document methodology choices and rationale

❌ **MISTAKE:** Creating threat models without MITRE ATT&CK mapping
✅ **CORRECT:** Map threats to ATT&CK techniques for detection alignment

❌ **MISTAKE:** One-time threat models never updated
✅ **CORRECT:** Establish maintenance process for evolving systems

❌ **MISTAKE:** Treating threat modelling as a checkbox exercise
✅ **CORRECT:** Ensure threat models drive security decisions

❌ **MISTAKE:** Only security team creates threat models
✅ **CORRECT:** Train and involve development teams

❌ **MISTAKE:** Using tools without understanding methodology
✅ **CORRECT:** Tools support methodology, not replace it

❌ **MISTAKE:** Generic threat catalogues not tailored to organisation
✅ **CORRECT:** Develop organisation-specific threat landscape

❌ **MISTAKE:** Ignoring insider threat in threat models
✅ **CORRECT:** Include insider threat actors explicitly

❌ **MISTAKE:** Threat models without quantified risk
✅ **CORRECT:** Apply risk rating methodology consistently

❌ **MISTAKE:** No connection between threats and countermeasures
✅ **CORRECT:** Map every high-priority threat to mitigation controls

---

# Quality Checklist

Before submitting the assessment, verify:

**Completeness:**

- [ ] All methodology components assessed
- [ ] MITRE ATT&CK coverage evaluated
- [ ] Threat catalogue reviewed
- [ ] Tools inventory complete
- [ ] Competency assessment complete
- [ ] Sample reviews documented (minimum 3)
- [ ] Compliance scoring complete
- [ ] All gaps in register

**Evidence:**

- [ ] Sample threat models collected
- [ ] MITRE ATT&CK mapping documented
- [ ] Tool evidence gathered
- [ ] Training records compiled
- [ ] Evidence properly stored

**Quality:**

- [ ] Ratings justified
- [ ] Gaps have remediation plans
- [ ] Owners assigned
- [ ] Due dates realistic

---

# Review & Approval

## Approval Workflow

| Step | Reviewer | Focus | Timeline |
|------|----------|-------|----------|
| 1 | Assessor | Completeness | Before submission |
| 2 | Peer | Technical accuracy | 2 business days |
| 3 | Threat Intelligence | ATT&CK alignment | 2 business days |
| 4 | CISO | Final approval | 2 business days |

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
