**ISMS-IMP-A.8.28.4**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.28.4 |
| **Version** | 1.0 |
| **Assessment Area** | Third-Party Dependencies & Open Source Software Management |
| **Related Policy** | ISMS-POL-A.8.28 Section 2.4 (Third-Party & OSS Management), Section 3 (Roles & Responsibilities) |
| **Purpose** | Evaluate supply chain security practices for third-party dependencies, open source software, vendor security, and license compliance |
| **Target Audience** | Application Security Team, Engineering Managers, Software Architects, Legal/Compliance Team, Procurement Team, Auditors |
| **Assessment Type** | Process, Technical & Legal |
| **Review Cycle** | Annually or After Major Supply Chain Security Incidents |
| **Date** | [Date] |

**Version History**:

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | [Date] | Initial assessment specification |

**Approvers**:

- Application Security Lead (Technical Review)
- Chief Information Security Officer (Final Approval)
- Legal Counsel (License Compliance Review)


**Related Documents**:

- ISMS-POL-A.8.28 - Secure Coding Policy (Master Policy)
- ISMS-POL-A.8.28-S2.4 - Third-Party & Open Source Software Management  
- ISMS-IMP-A.8.28.1 - SDLC Assessment
- ISMS-IMP-A.8.28.2 - Standards & Tools Assessment


---

# PART I: USER COMPLETION GUIDE

# Assessment Overview

## What This Assessment Does

This assessment evaluates your organization's management of **third-party dependencies, open source software (OSS), vendor-provided components, and external code integrations**.

**Core Question**: "Are we fooling ourselves about supply chain security?"

As Feynman said: *"The first principle is that you must not fool yourself—and you are the easiest person to fool."*

Having a vendor questionnaire ≠ Vendors are secure.  
Having an OSS policy ≠ OSS is managed.  
Scanning for vulnerabilities ≠ Vulnerabilities are fixed.

**What We're Assessing**:

- ✅ **Vendor Security Posture**: Are third-party vendors actually secure?
- ✅ **OSS Governance**: Do we know what OSS we're using?
- ✅ **Dependency Vulnerabilities**: Are we managing known security risks?
- ✅ **License Compliance**: Are we meeting legal obligations?
- ✅ **Supply Chain Security**: Are we protected against supply chain attacks?


**Why This Matters** (Real-World Incidents):

- **SolarWinds** (2020): Supply chain compromise affecting thousands of organizations
- **Log4Shell** (2021): Critical vulnerability in ubiquitous OSS library  
- **Codecov** (2021): CI/CD tool compromise exposing customer secrets
- **event-stream** (2018): Malicious code injected into npm package
- **ua-parser-js** (2021): Typosquatting and dependency confusion attacks


**Reality Check**: Modern applications are 80-90% third-party code. If you don't manage supply chain risk, you're not managing security.

## Who Should Complete This Assessment

**Primary Assessor**: Application Security Team or Senior Security Architect  
**Required Participants**:

- Engineering Managers (OSS usage and dependency management)
- Software Architects (design-level dependency decisions)
- Legal/Compliance Team (license compliance oversight)
- Procurement Team (vendor contracts and security requirements)
- DevOps Team (build pipeline and SCA tool integration)


**Time Estimate**: 12-16 hours for comprehensive assessment  
**Recommended Approach**: Phased assessment over 2-3 days with stakeholder interviews

## When to Use This Assessment

**Initial Assessment**: During Control A.8.28 implementation (Year 1)

**Recurring Assessments**:

- **Quarterly**: High-risk vendor reviews, critical dependency updates  
- **Annually**: Comprehensive assessment across all domains


**Triggered Assessments**:

- Following major supply chain incidents (e.g., Log4Shell-level events)
- After vendor security breach involving your data
- After license compliance violation discovery  
- New high-risk vendor integrations
- Significant changes to OSS policies or approval workflows
- Annual compliance audits


## Assessment Output

**Generated Workbook**: `ISMS-IMP-A.8.28.4_Third_Party_OSS_Assessment_YYYYMMDD.xlsx`  
**Python Generator**: `generate_a828_4_third_party_oss.py`

**Workbook Contains**:

- 11 sheets covering all supply chain security aspects
- 90 assessment questions across 5 domains
- Vendor risk registry
- OSS inventory (SBOM integration)
- Gap analysis and remediation planning  
- Executive summary with compliance metrics


---

# Prerequisites & Preparation

## Data You'll Need

**Vendor Information**:

- List of all third-party software vendors and service providers
- Vendor contracts with security clauses
- Vendor security questionnaires (completed)
- Vendor access logs (who has access to what)
- Vendor security review records (last 12 months)
- Vendor incident reports (if any breaches occurred)


**OSS Inventory Data**:

- Software Bill of Materials (SBOM) - CycloneDX or SPDX format
- OSS approval requests and decisions (last 12 months)
- Package manager manifests (package.json, requirements.txt, pom.xml, etc.)
- OSS policy documentation
- OSS contribution guidelines (if applicable)


**Dependency Vulnerability Data**:

- SCA tool scan reports (Snyk, Dependabot, WhiteSource, etc.)
- Vulnerability remediation tracking (JIRA, ServiceNow tickets)
- Patch management logs for dependencies
- SLA compliance metrics (time to remediate critical vulns)
- Lockfile examples (package-lock.json, Pipfile.lock, go.sum, etc.)


**License Compliance Data**:

- License scan reports
- Attribution files (LICENSE, NOTICE, THIRD_PARTY_LICENSES)
- Legal review records for restrictive licenses
- License compatibility assessments
- License violation remediation records


**Third-Party Integration Data**:

- Third-party API documentation and security reviews
- Container image scan reports (if using third-party images)
- Package integrity verification logs (signature checks, checksums)
- Integration security architecture diagrams


## Stakeholder Interviews Needed

**Before the assessment session**, conduct interviews:

**Engineering Managers** (20-30 minutes each):

- How do teams discover and approve new OSS?
- What's the process for updating dependencies?
- Are developers aware of OSS approval requirements?
- How are abandoned dependencies identified and replaced?


**Legal/Compliance Team** (30 minutes):

- What licenses are prohibited or require review?
- Have there been any license compliance violations?
- How are attribution requirements handled?
- What's the process for GPL or AGPL licenses?


**Procurement Team** (20 minutes):

- What security requirements are in vendor contracts?
- How are vendors assessed before engagement?
- What's the vendor review cadence?
- Have any vendors had security incidents?


**DevOps/Build Team** (20-30 minutes):

- How are SCA scans integrated into CI/CD?
- What happens when vulnerabilities are detected?
- Are builds blocked for critical vulnerabilities?
- How are package registries configured (internal vs. public)?


**Security Architects** (30 minutes):

- What's the architecture for third-party integrations?
- How are third-party APIs secured?
- What isolation/sandboxing is used for third-party code?
- How are supply chain attack risks mitigated?


## System Access Required

**Before Starting Assessment**:

1. **SCA Tool Access**:

   - Access to Snyk, Dependabot, WhiteSource, or equivalent
   - Review scan configurations and alert settings
   - Extract vulnerability metrics (last 3-6 months)


2. **Package Manager Configurations**:

   - Access to npm, pip, Maven, NuGet configurations
   - Review package source priorities (internal before public)
   - Check for dependency confusion protections


3. **SBOM Generation**:

   - Tools to generate SBOM (CycloneDX, SPDX)
   - Access to all application repositories
   - Ability to export complete dependency tree


4. **Vendor Management System**:

   - Access to vendor database/CRM
   - Vendor contract repository
   - Vendor security assessment records


5. **Legal Repository**:

   - Access to license scan reports
   - Legal review documentation
   - Attribution file templates


## Common Preparation Mistakes

❌ **Don't Do This**:

- Assessing based on policy documents alone (process ≠ reality)
- Accepting SBOM from 6 months ago (stale data useless)
- Reviewing only "approved" vendors (what about shadow IT?)
- Ignoring transitive dependencies (dependencies of dependencies)
- Skipping legal team engagement (license compliance is critical)


✅ **Do This Instead**:

- Generate fresh SBOM from current codebase
- Interview actual developers about OSS usage practices
- Review SCA tool findings from last week (real-time data)
- Sample actual vendor security assessments (not templates)
- Engage legal early for license compliance review
- Identify shadow IT and unapproved OSS usage


---

# Assessment Workflow (Step-by-Step)

## Step 1: Generate Assessment Workbook

```bash
# Generate fresh assessment workbook
python3 generate_a828_4_third_party_oss.py

# Output: ISMS-IMP-A.8.28.4_Third_Party_OSS_Assessment_20260125.xlsx
```

**What This Creates**:

- Empty assessment workbook with all sheets
- Pre-configured data validation dropdowns
- Assessment questions and evidence requirements
- Formula-driven compliance calculations
- Vendor risk registry template
- OSS inventory template


## Step 2: Review Instructions Sheet

**Open workbook → "Instructions" sheet**

Read the complete instructions including:

- Supply chain security assessment scope
- How to use dropdown menus
- Evidence documentation requirements
- Integration with SBOM and SCA tools
- Completion checklist


**Key Point**: This assessment measures ACTUAL supply chain security practices, not just policy compliance.

## Step 3-7: Complete All 5 Domain Assessments

Due to length constraints, I'll provide the essential workflow for each domain. See PART II for complete technical specifications.

**Domain 1: Vendor Security Assessment** (Sheet: `Vendor_Security_Assessment`)

- 18 requirements covering vendor due diligence, contracts, reviews
- Focus: Are vendors actually secure, or just claiming to be?
- Evidence: Questionnaires, contracts, access logs, review records


**Domain 2: OSS Management** (Sheet: `OSS_Management`)

- 18 requirements covering OSS approval, inventory (SBOM), governance
- Focus: Do we know what OSS we're using? Is it managed?
- Evidence: SBOM, approval records, policy compliance, abandoned dep reports


**Domain 3: Dependency Vulnerability Management** (Sheet: `Dependency_Vulnerability_Mgmt`)

- 18 requirements covering SCA scanning, remediation SLAs, patch management
- Focus: Are known vulnerabilities actually being fixed?
- Evidence: SCA reports, remediation metrics, lockfiles, SLA compliance


**Domain 4: Third-Party Code Review & Integration** (Sheet: `Third_Party_Code_Review`)

- 18 requirements covering vendor code review, API security, supply chain attacks
- Focus: Is third-party code treated as untrusted? Supply chain protections?
- Evidence: Code reviews, API assessments, integrity checks, container scans


**Domain 5: License Compliance** (Sheet: `License_Compliance`)

- 18 requirements covering license identification, compatibility, attribution
- Focus: Are we meeting legal obligations? Any GPL contamination?
- Evidence: License scans, legal reviews, attribution files, compatibility assessments


## Step 8: Review Summary Dashboard

**Sheet**: `Summary_Dashboard`  
**Auto-Calculated**: Based on all domain assessments

**Critical Analysis**:

- Overall compliance percentage
- Domain-by-domain breakdown
- Critical vendor risks highlighted
- OSS inventory completeness metric
- License compliance status


## Step 9: Populate Vendor Risk Registry

**Sheet**: `Vendor_Risk_Registry`

**For Each Vendor**:

- Risk classification (Critical/High/Medium/Low)
- Data access level
- Last security review date
- Security concerns or incidents
- Contract security terms compliance


## Step 10: Populate OSS Inventory

**Sheet**: `OSS_Inventory`

**SBOM Integration**:

- Import from CycloneDX or SPDX
- Or manually list key dependencies


**Critical**: Is this inventory complete and current?

## Step 11: Document Evidence

**Sheet**: `Evidence_Register`

**For Every "Implemented"**:

- Evidence type (SBOM, Contract, Scan Report, etc.)
- Location/link
- Collection date
- Verification status


## Step 12: Complete Gap Analysis

**Sheet**: `Gap_Analysis`

**For Every Gap**:

- Priority (Critical/High/Medium/Low)
- Owner and target date
- Remediation plan


**Priority Guidance**:

- **Critical**: No SBOM, no SCA tool, GPL contamination, critical vulns >30 days
- **High**: Incomplete SBOM, vendor access unmonitored, SLA breaches
- **Medium**: OSS approval gaps, attribution issues
- **Low**: Process improvements


## Step 13: Obtain Approvals

**Sheet**: `Approval_Sign_Off`

**Required Approvers**:
1. Assessment Completer (Application Security Analyst)
2. Application Security Lead (Technical Review)
3. Legal Counsel (License Compliance Validation)
4. Procurement Manager (Vendor Security Requirements)
5. CISO (Executive Approval)

---

# Common Pitfalls & How to Avoid Them

## Vendor Security Theater

❌ **Anti-Pattern**: Sending questionnaires but not validating answers
✅ **Good Practice**: Validate high-risk vendor answers, request evidence

## OSS Inventory Fiction

❌ **Anti-Pattern**: SBOM from 6 months ago, missing transitive deps
✅ **Good Practice**: Automated SBOM generation in CI/CD, includes all deps

## Vulnerability Management Theater

❌ **Anti-Pattern**: SCA alerts ignored, critical vulns unpatched for months
✅ **Good Practice**: SLA tracking, automated escalation, remediation metrics

## License Compliance Wishful Thinking

❌ **Anti-Pattern**: "Unknown" licenses, GPL contamination ignored
✅ **Good Practice**: 100% identification, automated blocking, legal approval

## Supply Chain Attack Naïveté

❌ **Anti-Pattern**: No package integrity verification, trust public registries
✅ **Good Practice**: Signature verification, internal registries, dependency confusion protections

---

# Interpreting Your Results

## Compliance Scoring

**Overall Compliance** = (Implemented / (Total - N/A)) × 100%

**Compliance Levels**:

- **90-100%**: Excellent
- **70-89%**: Good
- **50-69%**: Needs Improvement
- **<50%**: Critical


## Critical Requirements (Non-Negotiable)

These MUST be "Implemented":

- OSS inventory maintained (SBOM current)
- SCA scans automated
- Critical vulns <7 day SLA
- All licenses identified
- License compatibility assessed


**If any "Not Implemented"**: Escalate to CISO immediately.

## Effectiveness vs. Compliance

**Key Effectiveness Indicators**:
1. SBOM accuracy (matches actual deps?)
2. Vulnerability remediation (% within SLA?)
3. License compliance (any violations?)
4. Vendor security (reviews current?)

---

# Next Steps After Assessment

## Immediate Actions (Within 1 Week)

**Critical Gaps**:

- No SBOM → Generate immediately
- No SCA tool → Deploy and integrate
- GPL contamination → Legal review
- Critical vulns >30 days → Immediate patch


## Continuous Improvement

**Quarterly Reviews**:

- Refresh vendor risk classifications
- Update SBOM
- Analyze vulnerability remediation metrics
- Review license compliance


**Annual Reviews**:

- Comprehensive re-assessment
- Update policies
- Benchmark against standards (SLSA, NIST SSDF)
- Legal review of license guidance


---

# Quality Checklist

**Assessment Completeness**:

- [ ] All 90 requirements assessed
- [ ] Evidence for all "Implemented"
- [ ] Vendor Risk Registry populated
- [ ] OSS Inventory (SBOM) current
- [ ] Gaps have owners and dates


**Evidence Quality**:

- [ ] SBOM current (<30 days)
- [ ] SCA reports recent (<7 days)
- [ ] Vendor assessments current
- [ ] License scans from latest release


**Effectiveness Validation**:

- [ ] SBOM matches package manifests
- [ ] SCA alerts not just ignored
- [ ] Vendor answers validated
- [ ] License compliance tested


**Stakeholder Engagement**:

- [ ] Legal approved license compliance
- [ ] Procurement validated vendor security
- [ ] Engineering acknowledged OSS policy
- [ ] All approvers signed off


**Anti-Cargo-Cult Check**:

- [ ] SBOM is real (generated and tested)
- [ ] SCA tool working (alerts actionable)
- [ ] OSS policy followed (not just documented)
- [ ] License compliance real (attributions accurate)
- [ ] Honest about gaps


---

**END OF PART I: USER COMPLETION GUIDE**

---

*Remember: Modern applications are 80-90% third-party code. Supply chain risk is real—Log4Shell, SolarWinds, and Codecov prove it. Don't fool yourself—verify everything.*
# ISMS-IMP-A.8.28.4
# Secure Coding - Third-Party & Open Source Software Assessment

# PART II: TECHNICAL SPECIFICATION

# Excel Workbook Structure

## Workbook Overview

**File Name**: `ISMS-IMP-A.8.28.4_Third_Party_OSS_Assessment_YYYYMMDD.xlsx`  
**Total Sheets**: 11  
**Total Assessment Questions**: 90 (18 per domain × 5 domains)  
**Python Generator**: `generate_a828_4_third_party_oss.py`

**Sheet Structure**:
1. Instructions
2. Vendor_Security_Assessment (Domain 1)
3. OSS_Management (Domain 2)
4. Dependency_Vulnerability_Mgmt (Domain 3)
5. Third_Party_Code_Review (Domain 4)
6. License_Compliance (Domain 5)
7. Summary_Dashboard
8. Vendor_Risk_Registry
9. OSS_Inventory
10. Evidence_Register
11. Gap_Analysis
12. Approval_Sign_Off

---

# Sheet-by-Sheet Technical Specifications

## Sheet 1: Instructions

**Purpose**: Comprehensive assessment guidance

**Content**:

- Supply chain security assessment scope
- Domain-specific guidance
- Evidence requirements
- SBOM and SCA tool integration
- Quality checklist


**Formatting**:

- Header: Dark blue (#003366) white text
- Sections: Green (#70AD47) white text
- Body: Standard black on white


---

## Sheet 2: Vendor_Security_Assessment (Domain 1)

**Purpose**: Assess vendor security due diligence

**Column Structure**:
| Column | Header | Width | Type | Description |
|--------|--------|-------|------|-------------|
| A | Req ID | 8 | Text | V-01 to V-18 |
| B | Requirement | 60 | Text | Requirement description |
| C | Status | 15 | Dropdown | Implemented/Partial/Not Implemented/N/A |
| D | Evidence | 50 | Text | Evidence description |
| E | Notes | 40 | Text | Findings, observations |
| F | Score | 10 | Formula | Auto-calculated |

**Assessment Requirements** (18 total):

| ID | Requirement |
|----|-------------|
| V-01 | Vendor security questionnaire process documented and enforced |
| V-02 | Vendor risk classification system established |
| V-03 | Security requirements included in vendor contracts |
| V-04 | Vendor access controls documented and monitored |
| V-05 | High-risk vendors identified and tracked |
| V-06 | Vendor security reviews conducted per risk tier |
| V-07 | Vendor incident response procedures documented |
| V-08 | Vendor breach notification requirements in contracts |
| V-09 | Vendor data access segregated and logged |
| V-10 | Vendor SOC 2/ISO 27001 certifications reviewed |
| V-11 | Vendor questionnaire answers validated |
| V-12 | Vendor access reviews conducted quarterly |
| V-13 | Vendor security posture tracked over time |
| V-14 | Vendor exit procedures documented |
| V-15 | Vendor code escrow agreements (where applicable) |
| V-16 | Vendor penetration test results reviewed |
| V-17 | Vendor supply chain security assessed |
| V-18 | Vendor security incidents tracked and analyzed |

---

## Sheet 3: OSS_Management (Domain 2)

**Purpose**: Assess OSS approval, inventory, governance

**Assessment Requirements** (18 total):

| ID | Requirement |
|----|-------------|
| O-01 | OSS approval workflow documented and enforced |
| O-02 | OSS approval criteria defined (security, license, maintenance) |
| O-03 | OSS request system operational (JIRA, ServiceNow) |
| O-04 | OSS inventory maintained (SBOM - CycloneDX/SPDX) |
| O-05 | SBOM generated automatically in CI/CD |
| O-06 | SBOM includes transitive dependencies |
| O-07 | OSS policy communicated to development teams |
| O-08 | OSS license identification automated |
| O-09 | Abandoned OSS dependencies detected |
| O-10 | OSS update policy documented |
| O-11 | Critical OSS updates applied within SLA |
| O-12 | OSS contribution guidelines documented (if applicable) |
| O-13 | OSS security reviews conducted before approval |
| O-14 | OSS maintainer activity assessed |
| O-15 | Unapproved OSS usage detected and remediated |
| O-16 | OSS inventory accuracy verified quarterly |
| O-17 | OSS alternatives evaluated for abandoned projects |
| O-18 | OSS approval metrics tracked |

---

## Sheet 4: Dependency_Vulnerability_Mgmt (Domain 3)

**Purpose**: Assess vulnerability scanning and remediation

**Assessment Requirements** (18 total):

| ID | Requirement |
|----|-------------|
| D-01 | SCA tool deployed (Snyk, Dependabot, WhiteSource, etc.) |
| D-02 | SCA scans run automatically (daily/per-commit) |
| D-03 | SCA scan results accessible to development teams |
| D-04 | Vulnerability alerting configured |
| D-05 | Vulnerability remediation SLAs defined |
| D-06 | Critical vulnerabilities <7 day remediation SLA |
| D-07 | High vulnerabilities <30 day remediation SLA |
| D-08 | Vulnerability triage process documented |
| D-09 | Transitive dependencies scanned |
| D-10 | Dependency lockfiles used (package-lock.json, etc.) |
| D-11 | Lockfiles committed to version control |
| D-12 | Dependency pinning enforced |
| D-13 | Vulnerability remediation tracking automated |
| D-14 | SLA compliance measured and reported |
| D-15 | False positive handling process documented |
| D-16 | Vulnerability metrics tracked (MTTR, count, severity) |
| D-17 | Dependency update testing automated |
| D-18 | Emergency patching procedure documented |

---

## Sheet 5: Third_Party_Code_Review (Domain 4)

**Purpose**: Assess third-party integration security

**Assessment Requirements** (18 total):

| ID | Requirement |
|----|-------------|
| T-01 | Third-party code review requirements documented |
| T-02 | Vendor-provided code reviewed before integration |
| T-03 | Third-party API security assessments conducted |
| T-04 | API authentication mechanisms validated |
| T-05 | API rate limiting and abuse protections verified |
| T-06 | Third-party API error handling validated |
| T-07 | Package integrity verification implemented |
| T-08 | Package signatures verified (where available) |
| T-09 | Internal package registry configured |
| T-10 | Package source priority configured (internal first) |
| T-11 | Dependency confusion protections implemented |
| T-12 | Typosquatting protections implemented |
| T-13 | Container base images scanned for vulnerabilities |
| T-14 | Third-party containers from trusted registries only |
| T-15 | Third-party integration isolation/sandboxing implemented |
| T-16 | Third-party code behavioral analysis conducted |
| T-17 | Supply chain attack scenarios assessed |
| T-18 | Third-party integration security monitoring active |

---

## Sheet 6: License_Compliance (Domain 5)

**Purpose**: Assess license compliance and legal risk

**Assessment Requirements** (18 total):

| ID | Requirement |
|----|-------------|
| L-01 | License scanning tool deployed |
| L-02 | License scans run automatically per-build |
| L-03 | License scan results reviewed before release |
| L-04 | All dependency licenses identified (no "Unknown") |
| L-05 | Prohibited licenses defined (GPL, AGPL without approval) |
| L-06 | Prohibited licenses blocked automatically |
| L-07 | License compatibility assessed |
| L-08 | GPL/AGPL contamination prevented |
| L-09 | Legal review required for copyleft licenses |
| L-10 | License attribution files generated (LICENSE, NOTICE) |
| L-11 | Attribution files included in releases |
| L-12 | Attribution accuracy validated before release |
| L-13 | License violations remediated promptly |
| L-14 | License compliance metrics tracked |
| L-15 | Legal team engaged in OSS license decisions |
| L-16 | License policy communicated to developers |
| L-17 | License compliance training provided |
| L-18 | License compliance audits conducted annually |

---

## Sheet 7: Summary_Dashboard

**Purpose**: Executive summary with compliance metrics

**Content Structure**:

**Section 1: Overall Compliance**
| Metric | Value | Formula |
|--------|-------|---------|
| Overall Compliance % | XX% | Aggregate across domains |
| Total Requirements | 90 | Fixed |
| Implemented | XX | SUM(all "Implemented") |
| Partial | XX | SUM(all "Partial") |
| Not Implemented | XX | SUM(all "Not Implemented") |
| N/A | XX | SUM(all "N/A") |

**Section 2: Domain Compliance Breakdown**
| Domain | Compliance % | Status |
|--------|--------------|--------|
| 1. Vendor Security | XX% | 🟢/🟡/🔴 |
| 2. OSS Management | XX% | 🟢/🟡/🔴 |
| 3. Dependency Vuln Mgmt | XX% | 🟢/🟡/🔴 |
| 4. Third-Party Code Review | XX% | 🟢/🟡/🔴 |
| 5. License Compliance | XX% | 🟢/🟡/🔴 |

**Status Indicators**:

- 🟢 Green (90-100%): Excellent
- 🟡 Yellow (70-89%): Needs attention
- 🔴 Red (<70%): Critical gaps


**Section 3: Critical Findings**

- SBOM completeness (% dependencies tracked)
- Critical vulnerabilities unpatched >7 days
- License violations (count)
- High-risk vendors without recent reviews
- Supply chain attack protections status


---

## Sheet 8: Vendor_Risk_Registry

**Purpose**: Comprehensive vendor tracking

**Column Structure**:
| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Vendor ID | 10 | Auto-number |
| B | Vendor Name | 30 | Text |
| C | Vendor Type | 20 | Dropdown |
| D | Risk Classification | 15 | Dropdown |
| E | Product/Service | 40 | Text |
| F | Data Access Level | 20 | Dropdown |
| G | Last Review Date | 15 | Date (DD.MM.YYYY) |
| H | Next Review Due | 15 | Date (DD.MM.YYYY) |
| I | Security Concerns | 50 | Text |
| J | Contract Security Terms | 15 | Dropdown (Yes/No) |
| K | Contact Person | 25 | Text |

**Dropdowns**:

- Vendor Type: SaaS, Software License, Professional Services, Managed Service, Cloud Infrastructure
- Risk Classification: Critical, High, Medium, Low
- Data Access Level: Production Data, Sensitive Data, Internal Only, None


---

## Sheet 9: OSS_Inventory

**Purpose**: Complete OSS dependency tracking (SBOM)

**Column Structure**:
| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Component ID | 10 | Auto-number |
| B | Package Name | 30 | Text |
| C | Version | 15 | Text |
| D | Package Manager | 15 | Text |
| E | License | 20 | Text |
| F | Dependency Type | 15 | Dropdown |
| G | Last Updated | 15 | Date |
| H | Known Vulns | 15 | Number |
| I | Vuln Severity | 15 | Text |
| J | Approval Status | 15 | Dropdown |
| K | Maintainer Status | 15 | Dropdown |

**Dropdowns**:

- Dependency Type: Direct, Transitive
- Approval Status: Approved, Pending, Rejected, Legacy
- Maintainer Status: Active, Low Activity, Abandoned, Unknown


**SBOM Integration**:

- Import from CycloneDX XML/JSON
- Import from SPDX format
- Manual entry for edge cases


---

## Sheet 10: Evidence_Register

**Purpose**: Audit-ready evidence tracking

**Column Structure**:
| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Evidence ID | 12 | Auto-number |
| B | Req ID | 12 | Text |
| C | Domain | 20 | Text |
| D | Evidence Type | 20 | Dropdown |
| E | Description | 50 | Text |
| F | Location/Link | 40 | Text |
| G | Collection Date | 12 | Date |
| H | Collected By | 20 | Text |

**Evidence Type Dropdown**:

- SBOM Export
- Vendor Contract
- SCA Scan Report
- License Scan Report
- Security Questionnaire
- Review Meeting Notes
- Policy Document
- Configuration Screenshot
- Approval Record
- Other


---

## Sheet 11: Gap_Analysis

**Purpose**: Track remediation efforts

**Column Structure**:
| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Gap ID | 10 | Auto-number |
| B | Domain | 20 | Text |
| C | Req ID | 12 | Text |
| D | Gap Description | 50 | Text |
| E | Current State | 40 | Text |
| F | Target State | 40 | Text |
| G | Priority | 12 | Dropdown |
| H | Owner | 20 | Text |
| I | Target Date | 12 | Date |
| J | Status | 15 | Dropdown |

**Priority Dropdown**: Critical, High, Medium, Low  
**Status Dropdown**: Planned, In Progress, Complete, Blocked

**Conditional Formatting (Priority)**:

- Critical: Dark red (#C00000) white bold text
- High: Red (#FF6666)
- Medium: Yellow (#FFEB9C)
- Low: Green (#C6EFCE)


---

## Sheet 12: Approval_Sign_Off

**Purpose**: Formal approval by stakeholders

**Required Approvers**:
1. Assessment Completer (Application Security Analyst)
2. Application Security Lead (Technical Review)
3. Legal Counsel (License Compliance Review)
4. Procurement Manager (Vendor Security Requirements)
5. CISO (Executive Approval)

**Approval Criteria**:

- All 90 requirements assessed
- Vendor Risk Registry complete
- OSS Inventory (SBOM) documented
- Evidence for all "Implemented"
- Critical gaps have remediation plans
- Legal approval for license compliance


---

# Cell Styling Reference

## Color Palette

**Headers**:

- Main: #003366 (Dark blue) white text
- Sub: #4472C4 (Medium blue) white text
- Section: #70AD47 (Green) white text
- Column: #D9D9D9 (Light grey) black text


**Status Colors**:

- Implemented: #C6EFCE (Light green)
- Partial: #FFEB9C (Light yellow)
- Not Implemented: #FFC7CE (Light red)
- N/A: #E7E6E6 (Light grey)


**Priority Colors**:

- Critical: #C00000 (Dark red) white bold
- High: #FF6666 (Red)
- Medium: #FFEB9C (Yellow)
- Low: #C6EFCE (Green)


**Input Fields**: #FFFFCC (Light yellow)

## Font Standards

**Standard Font**: Calibri

- Headers: 14-16pt bold
- Subheaders: 11-12pt bold
- Body: 10pt regular
- Column headers: 10pt bold


---

# Python Script Integration Points

## Script: generate_a828_4_third_party_oss.py

**What the Script Does**:
1. Creates workbook with 12 sheets
2. Populates Instructions
3. Creates 5 assessment domain sheets (18 questions each)
4. Sets up data validation dropdowns
5. Applies conditional formatting
6. Creates Summary Dashboard with formulas
7. Creates Vendor Risk Registry template
8. Creates OSS Inventory template
9. Creates Evidence Register
10. Creates Gap Analysis
11. Creates Approval Sign-Off

**Output**: `ISMS-IMP-A.8.28.4_Third_Party_OSS_Assessment_YYYYMMDD.xlsx`

**Usage**:
```bash
python3 generate_a828_4_third_party_oss.py
```

**Requirements**:

- Python 3.x
- openpyxl library


## Data Validation Setup

**Status Dropdown**:
```python
status_validation = DataValidation(type="list", 
    formula1='"Implemented,Partial,Not Implemented,N/A"')
```

**Priority Dropdown**:
```python
priority_validation = DataValidation(type="list", 
    formula1='"Critical,High,Medium,Low"')
```

**Risk Classification Dropdown**:
```python
risk_validation = DataValidation(type="list", 
    formula1='"Critical,High,Medium,Low"')
```

## Formula Integration

**Domain Compliance Calculation**:
```excel
=COUNTIF(Vendor_Security!C:C,"Implemented")  // Count Implemented
=(B5 + 0.5*C5) / (18 - E5) * 100  // Compliance %
```

**Overall Compliance**:
```excel
=(Total_Implemented + 0.5*Total_Partial) / (90 - Total_NA) * 100
```

---

# Integration with IMP-A.8.28.5 (Compliance Dashboard)

## Data Export Schema

**Dashboard Consolidation Script Expected Schema**:

```python
WORKBOOK_4_SCHEMA = {
    'file': 'ISMS-IMP-A.8.28.4_Third_Party_OSS_Assessment_*.xlsx',
    'sheets': {
        'Summary_Dashboard': {
            'overall_compliance': 'B10',
            'total_requirements': 'B11',
            'implemented': 'B12',
            'partial': 'B13',
            'not_implemented': 'B14',
            'domain_breakdown': 'A16:C21',
        },
        'Vendor_Risk_Registry': {
            'total_vendors': "COUNTA(A:A)-1",
            'critical_vendors': "COUNTIF(D:D,'Critical')",
            'high_risk_vendors': "COUNTIF(D:D,'High')",
        },
        'OSS_Inventory': {
            'total_components': "COUNTA(A:A)-1",
            'components_with_vulns': "COUNTIF(H:H,'>0')",
            'critical_vulns': "COUNTIF(I:I,'Critical')",
        },
        'Gap_Analysis': {
            'critical_gaps': "COUNTIF(G:G,'Critical')",
            'high_gaps': "COUNTIF(G:G,'High')",
        }
    }
}
```

## Quarterly Update Process

**Every Quarter**:
1. Regenerate SBOM (fresh OSS inventory)
2. Update vendor risk classifications
3. Review SCA vulnerability metrics
4. Refresh license compliance status
5. Update gap remediation progress
6. Obtain fresh approvals
7. Export to Compliance Dashboard

---

# Supply Chain Security Best Practices

## SBOM Generation

**Tools**:

- CycloneDX: OWASP standard, widely supported
- SPDX: Linux Foundation standard, ISO/IEC 5962
- Syft: CLI tool for container and filesystem analysis
- OWASP Dependency-Track: SBOM analysis platform


**Integration**:

- Generate in CI/CD pipeline
- Store with release artifacts
- Version alongside code
- Include in release notes


## SCA Tool Selection Criteria

**Capabilities to Assess**:

- Vulnerability database coverage (NVD, GitHub Advisory, proprietary)
- False positive rate
- Transitive dependency support
- Package manager coverage
- License scanning
- Malware detection (beyond CVEs)
- CI/CD integration
- Remediation guidance


## Vendor Security Due Diligence

**Risk-Based Approach**:

- **Critical Vendors**: Annual review, SOC 2/ISO audit, penetration test results
- **High Vendors**: Annual questionnaire, contract security terms
- **Medium Vendors**: Biennial questionnaire
- **Low Vendors**: Basic security assessment at onboarding


## License Compliance Automation

**Automated Checks**:

- License scanning in CI/CD
- Prohibited license blocking
- Attribution file generation
- Legal approval workflow for copyleft licenses


**Legal Integration**:

- Pre-approved license list (MIT, Apache 2.0, BSD)
- Requires legal review (GPL, AGPL, LGPL, custom)
- Prohibited (unlicensed, restrictive commercial)


---

**END OF SPECIFICATION**

---

*"Complexity is the enemy of security."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-01-31 -->
