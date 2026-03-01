<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.32.3-UG:framework:UG:a.8.32.3 -->
**ISMS-IMP-A.8.32.3-UG - Environment Separation Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Environment Separation Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.32.3-UG |
| **Related Policy** | ISMS-POL-A.8.32 (Change Management) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.32 (Change Management) |
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

- ISMS-POL-A.8.32 (Change Management)
- ISMS-IMP-A.8.32.1 (Change Process Assessment)
- ISMS-IMP-A.8.32.2 (Change Types & Categories Assessment)
- ISMS-IMP-A.8.32.4 (Testing & Validation Assessment)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.32.3-TG.

---


**Audience:** Infrastructure Team, DevOps Engineers, System Administrators, Security Team

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Environment Inventory | Inventory of development, test and production environments |
| 3 | Access Controls | Assess access controls for each environment |
| 4 | Promotion Workflows | Document and assess code promotion workflows between environments |
| 5 | Data Protection | Evaluate protection of production data in non-production environments |
| 6 | Environment Config | Assess environment configuration standards and consistency |
| 7 | Separation Controls | Evaluate controls enforcing environment separation |
| 8 | Evidence Register | Store and reference evidence supporting assessments |
| 9 | Summary Dashboard | Compliance status and key metrics overview |
| 10 | Approval Sign-Off | Management review sign-off and certification |

---

## Assessment Overview

### What This Assessment Evaluates

This assessment documents HOW your organisation separates development, test, and production environments to ensure changes are properly validated before reaching production. It evaluates:

- **Environment Architecture:** Physical/logical separation of Dev/Test/Prod
- **Access Controls:** Who can access which environments
- **Promotion Workflows:** How code/changes move between environments
- **Data Protection:** How production data is protected in non-production
- **Environment Configuration:** How environments mirror production
- **Separation Enforcement:** Technical controls preventing unauthorised changes

### Why This Matters

This assessment verifies [Organisation]'s compliance with:

- ISO/IEC 27001:2022 Control A.8.32: Change Management (element d - testing)
- ISO/IEC 27001:2022 Control A.8.31: Separation of Development, Testing and Production
- ISMS-POL-A.8.32, Section 2.3 (Testing & Validation Requirements)

Testing changes in production is the #1 cause of production incidents. Proper environment separation ensures safe testing, prevents production contamination, and protects production data.

### Key Principle

This assessment is **technology-agnostic**. Whether you use physical servers, VMs, containers, cloud environments, or combinations - this evaluates separation effectiveness, not specific technology.

---

## Prerequisites

### Before Starting This Assessment

**Required:**

- [ ] Read ISMS-POL-A.8.32, Section 2.3 (Testing & Validation Requirements)
- [ ] Read ISO/IEC 27001:2022 Control 8.31 guidance
- [ ] Identify Infrastructure/DevOps lead (assessment owner)
- [ ] Access to network diagrams showing environment topology
- [ ] Access control documentation (who can access what)
- [ ] Deployment/promotion procedures
- [ ] Environment configuration documentation

**Recommended:**

- [ ] Interview DevOps team about deployment workflows
- [ ] Review access logs showing environment usage
- [ ] Gather incident reports involving environment issues
- [ ] Review data masking/anonymization procedures
- [ ] Identify environment monitoring dashboards

### Who Should Complete This Assessment

**Primary:** Infrastructure Manager or DevOps Lead

**Contributors:**

- Network Engineers (network separation, firewall rules)
- System Administrators (server/VM configuration)
- Security Team (access controls, data protection)
- DevOps Engineers (deployment pipelines, promotion workflows)
- Database Administrators (data protection in test)
- Application Owners (environment-specific configurations)

**Reviewers:**

- CISO (security controls validation)
- IT Operations Manager (operational readiness)

---

## Assessment Workflow

### Step-by-Step Process

**Step 1: Initial Setup (Day 1)**

- Assign assessment owner (Infrastructure/DevOps lead)
- Gather network diagrams and architecture documentation
- Review completion timeline (2-3 weeks)

**Step 2: Environment Inventory (Days 2-4)**

- Document all environments (Sheet 2: Environment_Inventory)
- Identify Dev, Test, Staging, Prod environments
- Document infrastructure type (physical/VM/container/cloud)
- Assess separation quality (physical vs logical)

**Step 3: Access Control Assessment (Days 3-6)**

- Document who can access each environment (Sheet 3: Access_Controls)
- Review access provisioning procedures
- Assess privileged access management
- Verify separation of duties (developers can't deploy to prod)

**Step 4: Promotion Workflow Documentation (Days 4-7)**

- Document how changes move between environments (Sheet 4: Promotion_Workflows)
- Map promotion checkpoints and approvals
- Assess automation level (manual vs automated)
- Review rollback capabilities

**Step 5: Data Protection Assessment (Days 5-8)**

- Assess production data usage in test (Sheet 5: Data_Protection)
- Review data masking/anonymization procedures
- Document synthetic data generation
- Verify no production credentials in non-prod

**Step 6: Environment Configuration (Days 6-9)**

- Compare environment configurations (Sheet 6: Environment_Config)
- Assess how closely test mirrors production
- Document configuration management approach
- Identify configuration drift issues

**Step 7: Separation Enforcement (Days 7-10)**

- Document technical controls enforcing separation (Sheet 7: Separation_Controls)
- Review network segmentation
- Assess deployment prevention controls
- Review monitoring and alerting

**Step 8: Evidence Collection (Days 8-11)**

- Compile supporting evidence (Sheet 8: Evidence_Register)
- Network diagrams, access logs, deployment logs

**Step 9: Summary Review (Days 9-12)**

- Review auto-calculated compliance (Sheet 9: Summary_Dashboard)
- Validate gap analysis

**Step 10: Quality Review (Days 10-13)**

- Self-review against checklist
- Peer review by Security Team

**Step 11: Final Approval (Days 11-15)**

- Infrastructure Manager approval
- CISO sign-off (Sheet 10: Approval_Sign_Off)

**Total Duration:** 2-3 weeks

---

## Completing Each Sheet

### Sheet 1: Instructions & Legend

**Pre-filled** - Read to understand status symbols, compliance levels, and evidence expectations.

### Sheet 2: Environment_Inventory

**What to document:**

- All environments used in change workflow
- Environment type (Dev/Test/Staging/Prod/DR)
- Infrastructure type (physical/VM/container/cloud)
- Separation method (physical, network, logical)
- Environment purpose and scope

**Tips:**

- Include ALL environments - personal dev environments, CI/CD agents, etc.
- If you only have Prod (no test), this is major gap - document honestly
- Staging/Pre-Prod environments are optional but recommended for high-risk systems
- Cloud environments (separate VPCs/VNets) count as logical separation

**Common Questions:**

- **Q:** "Is developer laptop a 'Dev environment'?"
  - **A:** Yes if used for development work. Document access controls for local dev.
- **Q:** "We have Dev and Prod but no Test - is that OK?"
  - **A:** Not compliant with policy. Mark as gap requiring remediation.
- **Q:** "Is Docker container separation adequate?"
  - **A:** Depends on isolation. Containers on same host = logical separation. Document honestly.

**Evidence to provide:**

- Network diagrams showing all environments
- Infrastructure documentation (cloud VPCs, VLANs, physical locations)
- Environment inventory list
- Architecture diagrams

### Sheet 3: Access_Controls

**What to document:**

- Who has access to each environment
- Access levels (read-only, deploy, admin)
- Access provisioning process (how access is granted)
- MFA requirements by environment
- Privileged access management
- Separation of duties enforcement

**Tips:**

- "Developers can't deploy to production" is key control - verify this
- Production access should be most restricted
- Break-glass emergency access is OK if logged and auditable
- Service accounts need same scrutiny as user accounts

**Common Questions:**

- **Q:** "Developers need production access for troubleshooting"
  - **A:** Read-only prod access for troubleshooting is acceptable. WRITE access for developers is policy violation.
- **Q:** "What about DevOps engineers?"
  - **A:** DevOps can have prod deploy rights IF they're not also developers on that system (separation of duties).
- **Q:** "We use shared credentials for deployment"
  - **A:** Major gap - individual accountability required. Document as finding.

**Evidence to provide:**

- Access control matrix (who can access what)
- Access provisioning procedures
- PAM system documentation
- Access logs showing who accessed what
- MFA configuration by environment

### Sheet 4: Promotion_Workflows

**What to document:**

- How changes move Dev -> Test -> Staging -> Prod
- Promotion checkpoints and approvals
- Automated vs manual promotion
- Deployment pipeline documentation
- Rollback procedures at each stage

**Tips:**

- Linear progression (Dev -> Test -> Prod) preferred over "wild west" deployment
- Automation reduces errors but doesn't eliminate need for checkpoints
- Skipping test and going Dev -> Prod should be rare (emergency only)
- Document ACTUAL workflow, not ideal workflow

**Common Questions:**

- **Q:** "Can we skip Test for small changes?"
  - **A:** Policy allows risk-based approaches. Document YOUR criteria for test skipping. Low-risk standard changes might skip full test cycle.
- **Q:** "We use CI/CD - does that count as controlled promotion?"
  - **A:** Yes IF pipeline has proper controls (automated testing, approvals, audit trail). Document pipeline stages.
- **Q:** "What if Test environment isn't available?"
  - **A:** Not an excuse to deploy untested. Document as process gap and remediation plan.

**Evidence to provide:**

- Promotion workflow diagrams
- CI/CD pipeline configurations
- Deployment logs showing progression
- Approval records at promotion checkpoints
- Rollback procedure documentation

### Sheet 5: Data_Protection

**What to document:**

- How production data is used (or not used) in non-production
- Data masking/anonymization procedures
- Synthetic test data generation
- Credential management (no prod credentials in test)
- Backup data protection

**Tips:**

- Production data in test is HIGH RISK - regulatory violation (GDPR, etc.)
- "We copy production to test" = policy violation unless properly masked
- Synthetic data is ideal but takes effort - masking is pragmatic middle ground
- Production credentials MUST NOT exist in non-production environments

**Common Questions:**

- **Q:** "We need real data for realistic testing"
  - **A:** Then MASK it properly. Real names, addresses, credit cards must be obfuscated.
- **Q:** "What about production-like data (similar but not real)?"
  - **A:** Synthetic data is best approach - document generation procedures.
- **Q:** "We have production database credentials in test for read-only queries"
  - **A:** Policy violation - test should NEVER have production credentials. Use test-specific accounts.

**Evidence to provide:**

- Data masking procedures and tools
- Sample test data (showing it's masked, not real)
- Synthetic data generation scripts
- Credential management documentation
- Data classification by environment

### Sheet 6: Environment_Config

**What to document:**

- How closely test/staging mirror production
- Configuration management approach (IaC, manual, hybrid)
- Environment-specific configuration handling
- Configuration drift detection and correction
- Infrastructure-as-Code usage

**Tips:**

- Test should closely mirror prod (OS, middleware, dependencies)
- Perfect mirror not always feasible (cost, scale) - document differences
- Configuration drift (test diverging from prod) causes "works in test, fails in prod"
- IaC (Terraform, CloudFormation, Ansible) helps maintain consistency

**Common Questions:**

- **Q:** "Test has older hardware than prod - is that OK?"
  - **A:** Hardware can differ. SOFTWARE stack should match (OS version, app version, middleware).
- **Q:** "Test has 1 server, Prod has 10 - does test need same scale?"
  - **A:** No - test can be smaller scale. But architecture should be similar (load balancer, DB, app tier).
- **Q:** "We manage environments manually"
  - **A:** Manual is higher risk (human error, drift). Document as improvement opportunity. IaC is recommended but not mandatory.

**Evidence to provide:**

- Environment configuration specifications
- IaC scripts (Terraform, CloudFormation, Ansible)
- Configuration management tool documentation
- Drift detection reports
- Environment comparison matrix

### Sheet 7: Separation_Controls

**What to document:**

- Technical controls enforcing separation
- Network segmentation (VLANs, firewalls, security groups)
- Deployment prevention (can't accidentally deploy to wrong environment)
- Monitoring and alerting for separation violations
- Automated controls vs manual procedures

**Tips:**

- Technical controls > manual procedures (humans make mistakes)
- Firewall rules between environments enforce network separation
- Deployment tools should require explicit environment selection
- "Accidentally deployed to prod" should be technically prevented, not just procedurally prohibited

**Common Questions:**

- **Q:** "What if all environments are on same network?"
  - **A:** Major gap - network segmentation required. Document as finding.
- **Q:** "We rely on developers not deploying to prod by accident"
  - **A:** Insufficient - need technical controls. Deployment tool should require explicit prod approval/MFA.
- **Q:** "Cloud environments in same VPC/VNet OK?"
  - **A:** Only if subnets and security groups properly segment. Flat network is violation.

**Evidence to provide:**

- Network diagrams showing segmentation
- Firewall rules between environments
- Deployment tool configuration (environment targeting)
- Monitoring dashboards for separation violations
- Access control lists

### Sheet 8: Evidence_Register

**What to document:**

- Evidence location for all requirements
- Evidence type and last verification
- Accessibility for auditors

**Tips:**

- Network diagrams are KEY evidence for this assessment
- Access logs prove who accessed what
- Deployment logs prove promotion workflow compliance

### Sheet 9: Summary_Dashboard

**Auto-calculated** - Review for accuracy:

- Overall compliance percentage
- Compliance by domain (inventory, access, promotion, data, config)
- Critical gaps requiring attention

### Sheet 10: Approval_Sign_Off

**What to complete:**

- Assessment completion date
- Infrastructure Manager sign-off
- CISO approval
- Next review date

---

## Evidence Collection

### Types of Evidence

**Architecture Evidence:**

- Network diagrams (all environments)
- Infrastructure topology documentation
- Cloud architecture diagrams (VPCs, VNets, subnets)
- Physical datacenter layouts (if applicable)

**Access Control Evidence:**

- Access control matrix
- IAM policies/role definitions
- Access provisioning audit logs
- MFA configuration documentation
- PAM system configuration

**Promotion Evidence:**

- CI/CD pipeline configurations
- Deployment logs showing environment progression
- Promotion approval records
- Rollback execution examples

**Data Protection Evidence:**

- Data masking tool configuration
- Sample test data (showing masking)
- Credential management procedures
- Data classification by environment

**Configuration Evidence:**

- IaC scripts (Terraform, CloudFormation, Ansible)
- Configuration management system documentation
- Environment comparison reports
- Drift detection alerts

**Control Evidence:**

- Firewall rules between environments
- Security group configurations
- Deployment tool access controls
- Monitoring dashboards and alerts

### Evidence Best Practices

**Do:**

- ? Include network diagrams with clear environment boundaries
- ? Provide access logs showing restricted prod access
- ? Show deployment logs proving Dev -> Test -> Prod progression
- ? Document automated controls (firewall rules, security groups)

**Don't:**

- ? Provide outdated network diagrams
- ? Hide the fact that developers have production access
- ? Claim "we have separation" without technical evidence
- ? Confuse logical separation with no separation

---

## Common Pitfalls

### Mistake #1: "We have Dev and Prod - that's good enough"

**Problem:** Policy requires separate TEST environment for validation before production.

**Solution:** Minimum: Dev + Test + Prod. Document gap if test is missing, with remediation plan.

### Mistake #2: "Developers need prod access to fix issues quickly"

**Problem:** Violates separation of duties. Developers with prod write access = uncontrolled changes.

**Solution:** Read-only prod access OK for troubleshooting. WRITE access only for designated deployers (DevOps, Ops).

### Mistake #3: "All environments on same network is fine"

**Problem:** No technical enforcement of separation. Accidental prod deployment is easy.

**Solution:** Network segmentation required (VLANs, firewalls, cloud security groups).

### Mistake #4: "We copy production database to test for realistic testing"

**Problem:** MAJOR data protection violation (GDPR, privacy regulations).

**Solution:** Mask/anonymize production data OR generate synthetic test data. NEVER use unprotected prod data in test.

### Mistake #5: "Test environment has older versions - saves money"

**Problem:** "Works in test" doesn't mean "works in prod" if versions differ.

**Solution:** Test should mirror prod software versions. Hardware can be smaller scale, but software stack must match.

### Mistake #6: "We only test in prod because test is always broken"

**Problem:** Test environment not maintained properly. Testing in prod is policy violation.

**Solution:** Fix test environment maintenance. Production is NOT a test environment.

### Mistake #7: "Configuration management is too complex, we do it manually"

**Problem:** Manual configuration leads to drift and inconsistencies.

**Solution:** Start simple - even scripted configs better than manual. Progress toward IaC over time.

### Mistake #8: "Shared service accounts are fine - we know who uses them"

**Problem:** No individual accountability. Can't prove who deployed what.

**Solution:** Individual accounts for deployment. Service accounts only for automated systems (CI/CD agents) with audit logging.

### Mistake #9: "Container isolation is the same as VM isolation"

**Problem:** Container escape vulnerabilities exist. Containers on same host share kernel.

**Solution:** Document container isolation model honestly. Additional controls for production containers.

### Mistake #10: "Cloud provider handles separation for us"

**Problem:** Cloud provides tools, but YOU configure them. Flat VPC/VNet = no separation.

**Solution:** Properly configure cloud security groups, VPC/VNet segmentation, IAM policies.

---

## Quality Checklist

### Assessment Completeness

**Environment Inventory:**

- [ ] All environments documented (Dev, Test, Staging, Prod, DR)
- [ ] Separation method documented for each
- [ ] Infrastructure type identified
- [ ] Minimum Dev + Test + Prod exists (or gap documented)

**Access Controls:**

- [ ] Access matrix complete (who can access what)
- [ ] Separation of duties verified (devs can't deploy to prod)
- [ ] Privileged access management documented
- [ ] MFA requirements by environment documented
- [ ] Access logs available as evidence

**Promotion Workflows:**

- [ ] Workflow documented (how changes progress)
- [ ] Checkpoints and approvals identified
- [ ] Automation level documented
- [ ] Rollback procedures defined
- [ ] Deployment logs available

**Data Protection:**

- [ ] Production data usage in test documented
- [ ] Data masking/anonymization procedures defined
- [ ] Credential management verified (no prod creds in test)
- [ ] Data protection evidence available

**Environment Configuration:**

- [ ] Test mirrors prod (or differences documented)
- [ ] Configuration management approach defined
- [ ] Drift detection mechanisms documented
- [ ] IaC usage documented (if applicable)

**Separation Controls:**

- [ ] Network segmentation documented
- [ ] Firewall rules/security groups documented
- [ ] Technical controls enforcing separation verified
- [ ] Monitoring and alerting defined

**Evidence:**

- [ ] Network diagrams current (<6 months)
- [ ] Access logs available
- [ ] Deployment logs available
- [ ] All evidence accessible to auditors

**Dashboard:**

- [ ] Compliance percentage validated
- [ ] Critical gaps identified
- [ ] Remediation priorities set

---

## Review & Approval

### Review Process

**Step 1: Self-Review (Infrastructure Manager)**

- Complete quality checklist
- Validate network diagrams current
- Verify access control matrix accurate

**Step 2: Peer Review (Security Team)**

- Review access controls for separation of duties
- Validate data protection procedures
- Assess technical control adequacy
- Typical turnaround: 3-5 days

**Step 3: Compliance Review (Compliance Officer)**

- Verify regulatory data protection compliance
- Check separation requirements met
- Typical turnaround: 2-3 days

**Step 4: CISO Approval**

- Overall separation effectiveness
- Data protection risk acceptance
- Critical gap remediation plans
- Typical turnaround: 2-3 days

**Step 5: Documentation & Communication**

- Set status to "Final"
- Set next review date (+3 months)
- File network diagrams and evidence
- Notify gap owners

**Approval Timeline:** 2-3 weeks

**Rejection Reasons:**

- Missing test environment (critical gap)
- Developers have production write access
- Production data in test without masking
- No network segmentation between environments
- Outdated or missing network diagrams

---

## Continuous Improvement

### Using Assessment Results

**Environment Maturity:**

- Only Dev+Prod -> Add Test environment
- Manual deployments -> Implement CI/CD automation
- No IaC -> Start with configuration scripts, progress to full IaC

**Access Control Refinement:**

- Review access logs - is prod access actually restricted?
- Implement PAM for privileged access
- Regular access reviews - remove unused access

---

**END OF USER GUIDE**

---

*"A change tested in the wrong environment is a change untested."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
