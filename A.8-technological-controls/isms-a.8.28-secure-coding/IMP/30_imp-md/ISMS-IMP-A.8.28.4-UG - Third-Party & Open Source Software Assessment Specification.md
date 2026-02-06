**ISMS-IMP-A.8.28.4-UG - Third-Party & Open Source Software Assessment Specification**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.28.4-UG |
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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
