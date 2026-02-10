<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.1-7-18-19-S4-UG:framework:UG:a.8.1-7-18-19-s4 -->
**ISMS-IMP-A.8.1-7-18-19-S4-UG - Software Control Process**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.1: User Endpoint Devices

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S4-UG |
| **Version** | 1.0 |
| **Assessment Area** | Software Installation Controls and Application Whitelisting |
| **Related Policy** | ISMS-POL-A.8.1-7-18-19, Section 2.4 (Software Installation Controls) |
| **Purpose** | Document approved software list, assess unauthorized software, verify application control effectiveness across endpoint landscape |
| **Target Audience** | IT Operations, Security Engineers, Change Management, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Monthly (unauthorized software), Quarterly (full assessment) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guide for software control assessment | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.1-7-18-19-S4-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.1-7-18-19-S4 - Software Control Process Assessment

#### What This Assessment Covers

This assessment evaluates [Organization]'s software installation controls and application whitelisting effectiveness. This answers:

- What is the approved software list? (mandatory, role-specific, optional, prohibited)
- What software is actually installed on endpoints?
- What unauthorized software has been detected?
- Are application controls enforced? (AppLocker, whitelisting)
- What is the software approval process?
- How is patch compliance tracked?
- What gaps exist in software controls?

#### Key Principle

**Software control is PREVENTIVE, not detective-only:**

- ❌ Detective: "We scan for unauthorized software and remove it"
- ✅ Preventive: "Application controls prevent unauthorized installation, scanning validates"

This assessment verifies both preventive controls (application whitelisting) and detective controls (software inventory scanning).

#### What You'll Document

**Approved Software:**

- Master approved software list with categories
- Version requirements and exceptions
- Approval workflows and ownership

**Installed Software:**

- Per-endpoint software inventory
- Unauthorized software detections
- Software installation control status

**Application Control:**

- Application control technology deployed
- Enforcement mode (audit vs. enforce)
- Policy coverage and effectiveness

**Patch Compliance:**

- Software vulnerability status
- Patch deployment timelines
- Critical/high severity patch compliance

#### How This Relates to Other Assessments

| Assessment | Focus | Relationship to S4 |
|------------|-------|-------------------|
| S1 - Endpoint Discovery | Inventory | Provides endpoint list for S4 |
| S2 - Security Baselines | Configuration | Baseline includes application control |
| S3 - Malware Protection | Protection | Malware often arrives via unauthorized software |
| **S4 - Software Controls** | **Software Governance** | **What software allowed, what's installed** |
| S5 - Privileged Utilities | Access Control | Privileged tools are subset of software |
| S6 - Compliance Assessment | Consolidated View | Overall compliance |

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **IT Operations** - Software deployment and inventory
2. **Change Management** - Software approval workflow
3. **Security Engineering** - Application control policies
4. **Vulnerability Management** - Patch compliance tracking
5. **Compliance** - Audit readiness

#### Time Commitment

- **Initial assessment:** 10-15 hours (software inventory reconciliation is time-intensive)
- **Monthly updates:** 3-4 hours (unauthorized software scanning)
- **Quarterly updates:** 6-8 hours (full assessment with approval list review)

### Expected Outputs

Upon completion, you will have:

1. ✅ Master approved software list
2. ✅ Per-endpoint software inventory
3. ✅ Unauthorized software detections
4. ✅ Application control coverage and effectiveness
5. ✅ Patch compliance status
6. ✅ Software approval workflow documentation
7. ✅ Gap analysis with remediation plans
8. ✅ Evidence register for audit
9. ✅ Approved assessment

---

## Prerequisites

### Information You'll Need

#### 1. Endpoint Inventory

- **From S1:** Complete endpoint inventory
- Required: Device name, OS type, ownership model, criticality

#### 2. Software Inventory Tools Access

- Access to software inventory systems (Intune, Jamf, SCCM, third-party tools)
- Ability to export software inventory reports
- Access to application control consoles (AppLocker, allowlisting solutions)

#### 3. Documentation

- Approved software list (if exists)
- Software approval process/workflow
- Application control policies
- Change management procedures
- Patch management procedures

#### 4. Software Data

- Software inventory exports (all endpoints)
- Application control deployment status
- Patch compliance reports
- Software approval records (last 12 months)

### Tools You'll Use

**Software Inventory:**

- Microsoft Intune, Jamf Pro, SCCM, Kandji, or third-party inventory tools

**Application Control:**

- Windows AppLocker, macOS Gatekeeper, Linux SELinux/AppArmor, third-party allowlisting

**Vulnerability Management:**

- Qualys, Tenable, Rapid7, or endpoint protection with vulnerability scanning

**Change Management:**

- ServiceNow, Jira, or ticketing system with software approval workflow

### Access Requirements

- Read access to software inventory systems
- Read access to application control consoles
- Read access to vulnerability management platforms
- Read access to change management tickets
- Access to evidence repositories

---

## Assessment Workflow

### High-Level Process

```
1. IMPORT ENDPOINT INVENTORY (from S1)
2. DOCUMENT APPROVED SOFTWARE (Sheet 1)
3. COLLECT SOFTWARE INVENTORY (Sheet 2)
4. IDENTIFY UNAUTHORIZED SOFTWARE (Sheet 3)
5. ASSESS APPLICATION CONTROL (Sheet 4)
6. VERIFY PATCH COMPLIANCE (Sheet 5)
7. IDENTIFY SOFTWARE GAPS (Sheet 6)
8. REGISTER EVIDENCE (Sheet 7)
9. CALCULATE DASHBOARD METRICS (Sheet 8)
10. REVIEW & APPROVE
```

### Detailed Workflow

#### Phase 1: Preparation (1-2 hours)

**Steps:**
1. Read this entire User Guide
2. Gather all prerequisites
3. Review policy requirements (ISMS-POL-A.8.1-7-18-19, Section 2.4)
4. Export endpoint inventory from S1
5. Schedule time with SMEs (IT ops, change management)
6. Create working folder for evidence

**Deliverable:** Endpoint inventory, approved software list (if exists), SME availability

#### Phase 2: Approved Software List (3-4 hours)

**Objective:** Complete Sheet 1 - Approved Software

**Steps:**
1. Gather existing approved software lists (from IT, security, procurement)
2. Consolidate and categorize (mandatory, role-specific, optional, prohibited)
3. Document approval workflow
4. Identify software owners and approval authorities
5. Define version requirements

**Deliverable:** Complete Sheet 1 with master approved software list

#### Phase 3: Software Inventory Collection (4-6 hours)

**Objective:** Complete Sheet 2 - Installed Software

**Steps:**
1. Export software inventory from all endpoints
2. Normalize software names (different sources use different naming)
3. Identify software versions
4. Map to endpoints
5. Calculate software prevalence (how many endpoints have each software)

**Deliverable:** Complete Sheet 2 with comprehensive software inventory

#### Phase 4: Unauthorized Software Detection (2-3 hours)

**Objective:** Complete Sheet 3 - Unauthorized Software

**Steps:**
1. Compare installed software (Sheet 2) against approved list (Sheet 1)
2. Flag software not on approved list
3. Assess risk for each unauthorized software
4. Identify removal or approval path
5. Document exceptions

**Deliverable:** Complete Sheet 3 with unauthorized software list

#### Phase 5: Application Control Assessment (2-3 hours)

**Objective:** Complete Sheet 4 - Application Control

**Steps:**
1. Document application control technology deployed
2. Assess per-endpoint deployment status
3. Verify enforcement mode (audit vs. enforce)
4. Test effectiveness (can users install unauthorized software?)
5. Document policy coverage

**Deliverable:** Complete Sheet 4 with application control status

#### Phase 6: Patch Compliance Verification (2-3 hours)

**Objective:** Complete Sheet 5 - Patch Compliance

**Steps:**
1. Export vulnerability/patch data
2. Identify outdated software versions
3. Calculate patch compliance (critical ≤7 days, high ≤30 days)
4. Document patch deployment process
5. Identify patch compliance failures

**Deliverable:** Complete Sheet 5 with patch status

#### Phase 7: Gap Identification (1-2 hours)

**Objective:** Complete Sheet 6 - Software Control Gaps

**Steps:**
1. Consolidate gaps from all sheets
2. Assess risk levels
3. Develop remediation plans
4. Assign owners and target dates

**Deliverable:** Complete Sheet 6

#### Phase 8: Evidence Registry (1 hour)

**Objective:** Complete Sheet 7 - Evidence Registry

**Steps:**
1. List all evidence collected
2. Organize by category
3. Verify accessibility

**Deliverable:** Complete Sheet 7

#### Phase 9: Dashboard Metrics (1-2 hours)

**Objective:** Complete Sheet 8 - Software Control Dashboard

**Steps:**
1. Calculate overall metrics
2. Create executive summary
3. Document recommended actions

**Deliverable:** Complete Sheet 8

#### Phase 10: Review & Approval (2-3 hours)

**Steps:**
1. Self-review using quality checklist
2. Three-level approval process

**Deliverable:** Approved assessment

---

## Sheet-by-Sheet Completion Guide

### Sheet 1: Approved_Software

#### Purpose
Document the master approved software list with categories, versions, and approval workflow.

#### What to Document

- Approved software list (mandatory, role-specific, optional)
- Prohibited software list
- Version requirements
- Approval workflow and ownership
- Software categories and business justification

#### How to Complete

**Step 1: Gather Existing Lists**

Collect from multiple sources:

- IT Operations (standard software list)
- Security team (approved security tools)
- Procurement (licensed software)
- Department heads (role-specific software)
- Previous assessments or audits

**Step 2: Categorize Software**

**Software Categories:**
```
MANDATORY: Required for all endpoints (OS, security tools, productivity suite)
ROLE-SPECIFIC: Required for specific roles (development tools, design software)
OPTIONAL: Allowed but not required (browsers, communication tools)
PROHIBITED: Not allowed under any circumstances (P2P, unlicensed software, malware)
```

**Step 3: Document Each Software**

| Field | How to Complete |
|-------|-----------------|
| Software Name | Official product name |
| Vendor | Company name |
| Category | Mandatory/Role-Specific/Optional/Prohibited |
| Applicable Roles | If role-specific, which roles |
| Version Requirement | Specific version, latest, N-1, or "any supported" |
| License Type | Per-user, per-device, enterprise, open-source |
| Business Justification | Why approved |
| Security Review Date | When last security-reviewed |
| Approval Authority | Who can approve installation |
| Owner | Who maintains this software |

**Step 4: Document Approval Workflow**

**Approval Process:**
```
1. USER REQUEST (via ticket or form)
   ↓
2. MANAGER APPROVAL (business justification)
   ↓
3. SECURITY REVIEW (risk assessment)
   ↓
4. IT OPERATIONS REVIEW (compatibility, support)
   ↓
5. FINAL APPROVAL (CIO, CISO, or delegate)
   ↓
6. ADD TO APPROVED LIST (if approved)
   ↓
7. DEPLOY (if needed) or GRANT EXCEPTION
```

**Approval Authorities:**

- Mandatory software: CIO or CISO approval
- Role-specific software: Department head + security review
- Optional software: Manager + security review
- Prohibited software: Cannot be approved (exception requires CISO + legal)

**Step 5: Define Version Requirements**

**Version Strategies:**

- **Latest Only:** Security-critical software (browsers, security tools)
- **Latest or N-1:** Standard applications (Office, Adobe)
- **Specific Version:** Legacy systems, vendor-locked integrations
- **Any Supported:** Software with long support lifecycles

**Step 6: Document Prohibited Software**

**Common Prohibited Categories:**

- Peer-to-peer file sharing (BitTorrent, etc.)
- Remote access tools not approved (TeamViewer without approval)
- Personal cloud storage (Dropbox without approval - shadow IT)
- Unlicensed/pirated software
- Known malicious software
- Cryptocurrency miners
- Hacking/penetration tools (without authorized use)

#### Common Mistakes to Avoid

❌ **No approved list exists** - Creates "approved by default" situation  
❌ **Outdated list** - Last updated 3 years ago, irrelevant  
❌ **No version requirements** - "Adobe Reader approved" - which version?  
❌ **No approval workflow** - Ad-hoc approvals, no consistency  
❌ **Generic categories** - "Productivity software" too broad  
❌ **No prohibited list** - Can't enforce what's not defined  

#### Quality Checklist

- [ ] Approved software list comprehensive
- [ ] Categories clearly defined
- [ ] Version requirements specified
- [ ] Business justification documented
- [ ] Approval workflow defined
- [ ] Approval authorities identified
- [ ] Prohibited software list exists
- [ ] Software owners assigned
- [ ] Security review dates current (≤12 months)
- [ ] Role-specific software mapped to roles

---

### Sheet 2: Installed_Software

#### Purpose
Document actual software installed across all endpoints to enable comparison against approved list.

#### What to Document

For the organization as a whole:

- Complete software inventory across all endpoints
- Software prevalence (how many endpoints have each software)
- Version distribution
- Installation source/method

#### How to Complete

**Step 1: Export Software Inventory**

From software inventory tools:

- Microsoft Intune: Discovered Apps report
- Jamf Pro: Computer Inventory > Applications
- SCCM: Asset Intelligence or software inventory
- Third-party tools: Software inventory export

**Export should include:**

- Endpoint name
- Software name
- Software version
- Publisher/vendor
- Installation date
- Installation path

**Step 2: Normalize Software Names**

**Challenge:** Same software, different names:
```
"Google Chrome"
"Chrome"
"Google Chrome 120.0.6099.109"
"chrome.exe"
```

**Normalization:**
1. Standardize to official product name
2. Separate software name from version
3. Remove architecture/language designators (x64, en-US)
4. Handle variations (acronyms, abbreviations)

**Tool:** Use lookup table or scripted normalization

**Step 3: Aggregate Software Inventory**

**Create software summary:**

- Unique software list (deduplicated, normalized)
- Endpoint count per software (how many endpoints have it)
- Version distribution per software
- Most common version

**Example:**
```
Software: Google Chrome
Endpoints with this software: 847
Versions detected:

  - 120.0.6099.109: 623 endpoints (73.6%)
  - 119.0.6045.199: 198 endpoints (23.4%)
  - 118.0.5993.117: 26 endpoints (3.0%)

Most common version: 120.0.6099.109
```

**Step 4: Document Installation Methods**

How was software installed?

- Centrally deployed (SCCM, Intune, Jamf)
- User self-installed (download and install)
- Pre-installed (OEM image)
- Unknown

**Why it matters:** Centrally deployed = controlled, user self-installed = may be unauthorized

**Step 5: Flag High-Risk Software**

Automatically flag:

- Software with known vulnerabilities (check CVE databases)
- Software past end-of-life (EOL)
- Very old versions (>2 years outdated)
- Common shadow IT (Dropbox, TeamViewer, personal VPNs)
- Developer tools on non-dev endpoints

#### Common Mistakes to Avoid

❌ **Incomplete inventory** - Missing endpoints, missing software  
❌ **Not normalizing names** - Can't aggregate effectively  
❌ **No version tracking** - "Chrome installed" - which version?  
❌ **Ignoring BYOD** - BYOD needs inventory too (with privacy limits)  
❌ **Stale data** - Using 6-month-old inventory  
❌ **No installation method** - Can't tell controlled from uncontrolled  

#### Quality Checklist

- [ ] Software inventory from all endpoints
- [ ] Software names normalized
- [ ] Versions documented
- [ ] Prevalence calculated (endpoint counts)
- [ ] Installation methods identified
- [ ] High-risk software flagged
- [ ] Inventory is recent (≤30 days)
- [ ] BYOD handled appropriately (privacy-respecting)
- [ ] No missing endpoints from S1 inventory

---

### Sheet 3: Unauthorized_Software

#### Purpose
Identify software installed on endpoints that is not on the approved list.

#### What to Document

For each unauthorized software:

- Software name and version
- Endpoints where detected
- Risk assessment
- Approval path or removal plan

#### How to Complete

**Step 1: Compare Against Approved List**

**Logic:**
```
For each software in Sheet 2 (Installed_Software):
  If software NOT in Sheet 1 (Approved_Software):
    Flag as UNAUTHORIZED
  Else if version NOT approved:
    Flag as UNAPPROVED VERSION
```

**Step 2: Categorize Unauthorized Software**

**Categories:**

- **Unapproved but likely safe:** Common productivity tools, not yet reviewed
- **Shadow IT:** Cloud services, collaboration tools bypassing IT
- **High-risk:** Remote access, P2P, potentially malicious
- **Obsolete/EOL:** Old software past end-of-life
- **Unlicensed:** Commercial software without valid licenses
- **Development tools:** On non-developer endpoints

**Step 3: Assess Risk Per Software**

**Risk Factors:**
| Factor | Risk Level |
|--------|-----------|
| **Known vulnerabilities** | Critical/High |
| **No vendor support (EOL)** | High |
| **Remote access capability** | High |
| **Data exfiltration risk** | High |
| **Licensing violation** | Medium/Legal |
| **Productivity impact if removed** | Business risk |

**Risk Assessment:**
```
CRITICAL: Known malware, active exploits, severe licensing violation
HIGH: Unpatched vulnerabilities, EOL, shadow IT with data access
MEDIUM: Outdated versions, minor licensing issues
LOW: Common tools, low security impact, awaiting approval
```

**Step 4: Determine Action Path**

**For Each Unauthorized Software:**

**Option 1: Approve**

- Software is safe and useful
- Submit for approval workflow
- Add to approved list (Sheet 1)
- Document retroactive approval

**Option 2: Remove**

- Software is risky or unnecessary
- Create removal plan
- Notify affected users
- Execute removal
- Verify removal

**Option 3: Exception**

- Software needed for specific use case
- Cannot be approved broadly
- Grant time-limited exception
- Document compensating controls
- Periodic re-evaluation

**Option 4: Migrate**

- Functionality exists in approved alternative
- User training on approved alternative
- Remove unauthorized software
- Monitor for reinstallation

**Step 5: Document Per Unauthorized Software**

| Field | Details |
|-------|---------|
| Software Name | Full name |
| Version | Detected version |
| Vendor | Publisher |
| Endpoint Count | How many endpoints |
| Affected Endpoints | Device names |
| Category | Shadow IT, EOL, etc. |
| Risk Level | Critical/High/Medium/Low |
| Risk Justification | Why this risk level |
| Business Impact | If removed |
| Recommended Action | Approve/Remove/Exception/Migrate |
| Approval Status | Submitted/Approved/Denied |
| Removal Plan | How to remove |
| Alternative Software | If migrating |
| Owner | Responsible for action |
| Target Date | When resolved |

**Step 6: Calculate Metrics**

```
Total Unauthorized Software: Count of unique software
Total Affected Endpoints: Count of endpoints with ≥1 unauthorized
Unauthorized Software by Risk: Critical, High, Medium, Low
Unauthorized Software by Category: Shadow IT, EOL, etc.
```

#### Common Mistakes to Avoid

❌ **Blanket removal** - Removing without assessing business impact  
❌ **No risk assessment** - Treating all unauthorized equally  
❌ **No user notification** - Users surprised when software removed  
❌ **No alternative offered** - Remove without migration path  
❌ **Approving everything** - Defeats purpose of approved list  
❌ **No follow-up** - Identify but never remove  
❌ **Ignoring licensing** - Unauthorized ≠ unlicensed (separate issue)  

#### Quality Checklist

- [ ] All unauthorized software identified
- [ ] Risk assessment completed for each
- [ ] Business impact evaluated
- [ ] Action path determined (approve/remove/exception/migrate)
- [ ] Affected users/endpoints documented
- [ ] Removal plans specific
- [ ] Alternative software identified (if migrating)
- [ ] Owner assigned to each software
- [ ] Target dates realistic
- [ ] No blanket decisions without analysis

---

### Sheet 4: Application_Control

#### Purpose
Assess application control technology deployment and effectiveness.

#### What to Document

For each endpoint:

- Application control technology deployed
- Enforcement mode (audit vs. enforce)
- Policy coverage
- Effectiveness testing results

#### How to Complete

**Step 1: Identify Application Control Technologies**

**By Operating System:**

**Windows:**

- AppLocker (built-in)
- Windows Defender Application Control (WDAC)
- Third-party allowlisting (Carbon Black, Bit9, etc.)

**macOS:**

- Gatekeeper (built-in)
- XProtect (built-in)
- MDM application restrictions
- Third-party allowlisting

**Linux:**

- SELinux (Security-Enhanced Linux)
- AppArmor
- Third-party allowlisting

**Mobile (iOS/Android):**

- MDM application restrictions
- Enterprise app catalogs
- App store restrictions

**Step 2: Document Per-Endpoint Status**

| Field | Details |
|-------|---------|
| Device Name | From S1 |
| OS Type | Windows/macOS/Linux/iOS/Android |
| Application Control Tech | AppLocker, WDAC, Gatekeeper, etc. |
| Deployment Status | Deployed / Not Deployed / Partial |
| Enforcement Mode | Enforce / Audit / Disabled |
| Policy Type | Allowlist / Blocklist / Hybrid |
| Policy Coverage | What's controlled (executables, scripts, installers, DLLs) |
| Last Policy Update | When policy last updated |
| Exceptions Granted | Count of exceptions |
| Effectiveness Test Date | When last tested |
| Effectiveness Test Result | Pass / Fail / Not Tested |

**Step 3: Understand Enforcement Modes**

**Audit Mode:**

- Logs violations but doesn't block
- Good for testing before enforcement
- Provides visibility without business disruption
- **NOT compliant** for production

**Enforce Mode:**

- Blocks unauthorized software
- User cannot bypass (without admin)
- May cause legitimate application failures
- **Required** for compliance

**Step 4: Test Effectiveness**

**Testing Methodology:**
```
1. Select sample endpoints (5-10 per OS type)
2. Attempt to install unauthorized software

   - Use standard user account (not admin)
   - Try common software not on allowlist

3. Document results:

   - Blocked successfully? ✅
   - User received clear error message? ✅
   - Event logged? ✅
   - Installed despite controls? ❌ (FAIL)

```

**Common Test Software:**

- Firefox (if not approved, Chrome is)
- 7-Zip
- VLC Media Player
- Unauthorized browser extensions
- PowerShell scripts (if script control enabled)

**Step 5: Assess Policy Coverage**

**What Should Be Controlled:**

- ✅ Executables (.exe, .com)
- ✅ Scripts (.ps1, .vbs, .bat, .sh)
- ✅ Installers (.msi, .dmg, .pkg)
- ✅ Libraries (.dll, .dylib, .so)
- ✅ Browser extensions
- ✅ Mobile apps (on mobile devices)

**Common Coverage Gaps:**

- ❌ Scripts not controlled (users run PowerShell)
- ❌ Installers not controlled (users run .msi)
- ❌ Browser extensions not controlled (Chrome extensions installed freely)
- ❌ Portable apps not controlled (users run from USB)

**Step 6: Document Exceptions**

**Exception Categories:**

- Developer endpoints (need to compile/test code)
- Administrative workstations (need admin tools)
- Specialized workstations (CAD, video editing, etc.)
- Temporary exceptions (testing, troubleshooting)

**For Each Exception:**

- Justification
- Compensating controls
- Approval authority
- Time limit (if temporary)
- Re-evaluation date

**Step 7: Calculate Metrics**

```
Application Control Deployment %: (Endpoints with Controls / Total Endpoints) × 100
Enforcement Mode %: (Endpoints in Enforce / Endpoints with Controls) × 100
Effectiveness Rate: (Tests Passed / Tests Conducted) × 100

Targets:

- Deployment: ≥95%
- Enforcement: ≥90% (some audit mode acceptable for pilot)
- Effectiveness: 100% (all tests should pass)

```

#### Common Mistakes to Avoid

❌ **Audit mode forever** - Never moving to enforce  
❌ **No effectiveness testing** - Assuming it works  
❌ **Allowlist too broad** - "C:\Program Files\*" allows everything  
❌ **Blocklist only** - Easy to bypass, not effective  
❌ **No script control** - PowerShell/VBS bypass  
❌ **Exceptions not documented** - Ad-hoc exceptions, no tracking  
❌ **No user communication** - Users frustrated by blocks  

#### Quality Checklist

- [ ] Application control technology identified per endpoint
- [ ] Deployment status verified in console
- [ ] Enforcement mode documented (audit vs. enforce)
- [ ] Policy type identified (allowlist preferred)
- [ ] Policy coverage assessed (executables, scripts, etc.)
- [ ] Effectiveness testing conducted (sample endpoints)
- [ ] Test results documented (pass/fail)
- [ ] Exceptions documented with justifications
- [ ] Metrics calculated correctly
- [ ] Gaps identified (audit mode, coverage gaps)

---

### Sheet 5: Patch_Compliance

#### Purpose
Verify software is patched and up-to-date per policy requirements.

#### What to Document

For software inventory:

- Software versions vs. latest available
- Patch compliance status
- Vulnerability status (CVEs)
- Patch deployment timelines

#### How to Complete

**Step 1: Review Patch Requirements**

From policy:

- **Critical vulnerabilities:** Patch within 7 days
- **High vulnerabilities:** Patch within 30 days
- **Medium vulnerabilities:** Patch within 90 days
- **Low vulnerabilities:** Patch within 180 days or next maintenance window

**Step 2: Export Vulnerability Data**

From vulnerability management tools:

- Qualys, Tenable, Rapid7, or endpoint protection with vulnerability scanning
- Export should include: Software name, version, CVE IDs, severity, age

**Step 3: Map Software to Vulnerabilities**

**For Each Software in Inventory:**
1. Check latest version available from vendor
2. Compare installed version(s) to latest
3. Identify known vulnerabilities (CVE database)
4. Determine severity of unpatched vulnerabilities
5. Calculate days since patch available

**Step 4: Document Patch Compliance**

| Field | Details |
|-------|---------|
| Software Name | From inventory |
| Installed Version(s) | Versions detected |
| Latest Version | From vendor |
| Version Status | Current / Outdated / EOL |
| Known Vulnerabilities | CVE IDs |
| Highest Severity | Critical/High/Medium/Low |
| Patch Available Since | Date patch released |
| Days Overdue | Days since patch available minus SLA |
| Affected Endpoints | Count |
| Patch Status | Compliant / Warning / Overdue / Critical |
| Patch Plan | When/how patching |
| Blocker | What prevents patching (if any) |

**Step 5: Calculate Patch Compliance Metrics**

```
Critical Patch Compliance %: (Critical patched ≤7 days / Total Critical) × 100
High Patch Compliance %: (High patched ≤30 days / Total High) × 100
Overall Patch Compliance %: Weighted average

Targets:

- Critical: ≥95%
- High: ≥90%
- Medium: ≥80%

```

**Step 6: Identify Patch Blockers**

**Common Blockers:**

- Application compatibility (patch breaks critical application)
- Change freeze period (no changes during busy season)
- Testing requirements (patch must be tested before deployment)
- Vendor delay (patch not yet available)
- Resource constraints (no time to patch)
- Legacy systems (cannot be patched, compensating controls needed)

**For Each Blocker:**

- Document specific issue
- Identify compensating controls
- Set realistic timeline
- Get management approval if exceeding SLA

**Step 7: Track Patch Deployment**

**Patch Workflow:**
```
1. VULNERABILITY IDENTIFIED (scanner detects)
2. PATCH AVAILABLE (vendor releases)
3. TESTING (pilot group tests patch)
4. APPROVAL (change control approves)
5. DEPLOYMENT (patch deployed to production)
6. VERIFICATION (scanner confirms patched)
```

Document where each software is in this workflow.

#### Common Mistakes to Avoid

❌ **No vulnerability scanning** - Can't track what you don't detect  
❌ **Assuming latest = patched** - Version numbers don't tell full story  
❌ **Ignoring EOL software** - Can't patch, needs replacement  
❌ **No testing** - Patches break things, test first  
❌ **No patch metrics** - Can't measure compliance  
❌ **Manual patching** - Doesn't scale, automate  
❌ **No compensating controls** - Can't patch? Need mitigation  

#### Quality Checklist

- [ ] Vulnerability data current (≤7 days)
- [ ] Software versions mapped to vulnerabilities
- [ ] Severity levels accurate (from NVD/vendor)
- [ ] Patch compliance calculated per severity
- [ ] Days overdue calculated correctly
- [ ] Patch blockers documented
- [ ] Compensating controls for unpatchable
- [ ] Patch workflow documented
- [ ] EOL software identified
- [ ] Patch deployment automated (where possible)

---

### Sheet 6: Software_Control_Gaps

#### Purpose
Consolidate all gaps in software controls with prioritized remediation plans.

#### Gap Categories

1. No Approved Software List
2. Unauthorized Software Installed
3. Application Control Not Deployed
4. Application Control in Audit Mode
5. Patch Compliance Failures
6. EOL Software in Use
7. Licensing Compliance Issues

#### How to Complete

**Step 1: Consolidate Gaps from Previous Sheets**

- From Sheet 1: Missing approved list, outdated list
- From Sheet 3: Unauthorized software
- From Sheet 4: Application control gaps
- From Sheet 5: Patch compliance failures

**Step 2: Create Gap Register**

For EACH gap:

| Field | Details |
|-------|---------|
| Gap ID | GAP-A819-001 |
| Gap Category | Unauthorized/No Controls/Patch Failure/etc. |
| Gap Description | Specific description |
| Affected Items | Software or endpoints |
| Count | Number affected |
| Policy Requirement | Which violated |
| Risk Level | Critical/High/Medium/Low |
| Risk Justification | Why |
| Business Impact | What happens |
| Root Cause | Why exists |
| Remediation Plan | Steps to fix |
| Owner | Responsible |
| Target Date | When fixed |
| Resources Required | What's needed |
| Status | Open/In Progress/Resolved |

**Step 3: Assess Risk Level**

**Critical:**

- No application control deployed
- Critical vulnerabilities >30 days overdue
- High-risk unauthorized software (malware, remote access)
- EOL software with active exploits

**High:**

- Application control in audit mode only
- High vulnerabilities >60 days overdue
- Shadow IT with data access
- No approved software list

**Medium:**

- Unauthorized software (low risk)
- Medium vulnerabilities >120 days overdue
- Application control gaps (scripts not controlled)

**Low:**

- Minor version mismatches
- Low vulnerabilities >180 days overdue
- Process documentation gaps

**Step 4: Develop Remediation Plans**

**Example - No Application Control:**
```
Gap: 245 Windows endpoints without application control

Remediation Plan:
1. Deploy AppLocker policies to pilot group (20 endpoints) - Week 1-2
2. Test allowlist policy, adjust based on feedback - Week 3-4
3. Deploy to production in phases (50/week) - Week 5-9
4. Move from audit to enforce mode after 2 weeks audit - Week 11
5. Monitor and adjust exceptions - Ongoing

Owner: IT Operations Manager
Target Date: 11 weeks from now
Resources: AppLocker policy template, GPO deployment, help desk support
```

**Step 5: Prioritize Gaps**

Using risk/effort matrix similar to S3.

#### Common Mistakes to Avoid

❌ **Treating all gaps equally**  
❌ **No ownership**  
❌ **Unrealistic timelines**  
❌ **No resources allocated**  
❌ **Approving all unauthorized software**  

#### Quality Checklist

- [ ] All gaps consolidated
- [ ] Risk levels justified
- [ ] Remediation plans specific
- [ ] Owners assigned
- [ ] Target dates realistic
- [ ] Resources identified
- [ ] Priority assigned

---

### Sheet 7: Evidence_Register

#### Purpose
Centralized evidence repository for audit.

#### Evidence Categories

- Approved software list documentation
- Software inventory exports
- Unauthorized software reports
- Application control configurations
- Patch compliance reports
- Approval workflow records
- Effectiveness test results

#### How to Complete

Similar to S3, Sheet 7. Document all evidence collected.

#### Quality Checklist

- [ ] All evidence listed
- [ ] Storage locations documented
- [ ] Evidence current (≤30 days for operational data)
- [ ] Audit ready
- [ ] Sanitized

---

### Sheet 8: Software_Control_Dashboard

#### Purpose
Executive summary dashboard with key metrics.

#### What to Document

**Summary Metrics:**

- Approved software list completeness
- Unauthorized software count
- Application control deployment %
- Application control enforcement %
- Patch compliance %
- Critical gaps

#### How to Complete

**Metrics:**
```
Approved List Exists: Yes/No
Unauthorized Software Count: [X]
Unauthorized Software Risk: [X] Critical, [X] High
Application Control Deployment: [XX%]
Application Control Enforcement: [XX%]
Critical Patch Compliance: [XX%]
High Patch Compliance: [XX%]
Overall Status: Green/Yellow/Red
```

**Thresholds:**

**Green:**

- Approved list exists and current
- Unauthorized software ≤5% of total
- Application control deployed ≥95%
- Application control enforced ≥90%
- Critical patch compliance ≥95%

**Yellow:**

- Approved list outdated (>12 months)
- Unauthorized software 5-10%
- Application control deployed 85-94%
- Application control enforced 75-89%
- Critical patch compliance 85-94%

**Red:**

- No approved list
- Unauthorized software >10%
- Application control <85%
- Application control enforcement <75%
- Critical patch compliance <85%

#### Quality Checklist

- [ ] Metrics calculated correctly
- [ ] Thresholds applied
- [ ] Executive summary clear
- [ ] Recommended actions specific

---

### Sheet 9: Vulnerability_Management

#### Purpose
Track vulnerability status of deployed software and patch management effectiveness.

#### What to Document

**Software Vulnerabilities:**

- Software name and version
- CVE IDs associated with version
- Severity (Critical/High/Medium/Low)
- Patch available (Yes/No)
- Patch deployed (Yes/No)
- Days since patch release
- Risk level

**Patch Compliance:**

- Total software instances requiring patches
- Patched instances
- Unpatched instances with justification
- Patch deployment timeline
- Known exploits in wild

#### How to Complete

**Step 1: Identify Vulnerable Software**

From vulnerability scans (Nessus, Qualys):

- Software name and version: [name]
- CVE IDs: [list]
- Severity: [Critical/High/Medium/Low]
- Affected endpoint count: [count]

**Step 2: Determine Patch Status**

- Patch available? Yes/No
- Patch version: [version]
- Release date: [date]
- Days since release: [number]

**Step 3: Track Patch Deployment**

- Approved for deployment: Yes/No
- Deployment start date: [date]
- Target completion: [date]
- Deployed endpoint count: [count]
- Remaining unpatched: [count]
- Blocking issues: [if any]

**Step 4: Assign Risk Rating**

For unpatched vulnerabilities:

- Risk level: Critical/High/Medium/Low
- Known exploit? Yes/No
- Business impact if exploited: [description]
- Compensating controls: [if any]
- Remediation target: [date]

#### Common Mistakes to Avoid

❌ Not tracking vulnerability age
❌ Patches approved but not deployed
❌ No prioritization of critical issues
❌ Not investigating why patches blocked
❌ EOL software with known vulnerabilities

#### Quality Checklist

- [ ] All software scanned for vulnerabilities
- [ ] CVEs identified and linked
- [ ] Patch status current (<7 days)
- [ ] Unpatched instances justified
- [ ] Risk levels assigned
- [ ] Remediation dates realistic

---

### Sheet 10: Licensing_Compliance

#### Purpose
Ensure software licensing compliance and cost optimization.

#### What to Document

**License Status:**

- Software name and version
- License type (perpetual/subscription/trial)
- Licensed count (seats/devices)
- Deployed count (actual usage)
- License expiration date
- License cost per unit
- Total license cost
- Compliance status (over/under/compliant)

**Vendor Information:**

- Vendor name
- Support tier and expiration
- Renewal terms
- Cost optimization opportunities

#### How to Complete

**Step 1: Inventory Licensed Software**

For each approved software:

- Software name: [name]
- Version: [version]
- License type: [Perpetual/Annual/Monthly/Trial]
- Licensed count: [number]
- Deployed count: [number]

**Step 2: Verify License Compliance**

- Licensed ≥ Deployed? Yes/No
- If no, variance: [count] unlicensed instances
- Risk: Audit liability, vendor audit risk
- Remediation: Purchase additional licenses or remove

**Step 3: Track License Expiration**

- Expiration date: [date]
- Days until expiration: [number]
- Renewal process: [vendor-specific]
- Renewal cost: [amount]
- Budget approved? Yes/No

**Step 4: Calculate Licensing Costs**

- License cost per unit: [cost]
- Total licensed: [count] × [cost] = [total]
- Support costs: [amount]
- Annual cost: [total]

**Step 5: Identify Cost Optimization**

- Unused licenses: [count] (potential savings)
- Negotiated discount opportunity: Yes/No
- Alternative solution evaluation: Yes/No
- Consolidation opportunities: [if any]

#### Common Mistakes to Avoid

❌ Deployed > Licensed (audit risk)
❌ Not tracking license expiration
❌ No renewal planning
❌ Paying for unused licenses
❌ Mixed license agreement versions

#### Quality Checklist

- [ ] All software licenses inventoried
- [ ] Licensed vs. deployed verified
- [ ] Expiration dates tracked
- [ ] No over-deployment
- [ ] Renewal timeline established
- [ ] Cost optimization identified

---

### Sheet 11: Capability_Requirements

#### Purpose
Define and assess required software control capabilities vs. current deployment.

#### What to Document

**Required Capabilities:**

- Application whitelisting (required/desired)
- Application blacklisting (required/desired)
- Script execution control (required/desired)
- Privilege elevation control (required/desired)
- DLL injection prevention (required/desired)
- Unauthorized installation blocking (required/desired)
- License compliance enforcement (required/desired)

**Deployment Assessment:**

- Solution 1: Capabilities provided
- Coverage (% of endpoints)
- Configuration gaps
- Feature gaps

#### How to Complete

**Step 1: Define Required Capabilities**

For Corporate endpoints:

- Application control method: [Whitelist/Blacklist/Hybrid]
- Script execution control: [Required/Desired]
- Privilege elevation: [Restricted/Monitored/Allow]
- Unauthorized installation: [Block/Alert/Monitor]
- Performance acceptable: [Yes/No threshold]

For BYOD endpoints:

- Lighter control approach
- Mobile app restrictions
- Work container isolation

**Step 2: Assess Current Deployment**

- Solution deployed: [name and version]
- Capability 1: [Implemented/Partial/Not Implemented]
- Capability 2: [Implemented/Partial/Not Implemented]
- Coverage: [X% of endpoints]
- Configuration mode: [Enforce/Audit/Monitor]

**Step 3: Map Capability Gaps**

- Missing capability: [name]
- Endpoint impact: [count] ([%])
- Risk impact: Critical/High/Medium/Low
- Mitigation: Upgrade/Different solution/Accept

**Step 4: Plan Remediation**

- Upgrade existing solution: Timeline
- Deploy additional solution: Scope
- Accept gap with compensating control: Approval

#### Common Mistakes to Avoid

❌ Requirements too vague
❌ Over-specifying nice-to-have features
❌ No gap prioritization
❌ Outdated solution information
❌ No performance impact assessment

#### Quality Checklist

- [ ] All required capabilities defined
- [ ] Current capabilities documented
- [ ] Gaps clearly identified
- [ ] Risk levels assigned
- [ ] Performance acceptable
- [ ] Remediation plans assigned

---

## Evidence Collection

### Required Evidence Types

1. **Approved Software List** - Master document, approval records
2. **Software Inventory** - Exports from inventory tools
3. **Unauthorized Software** - Detection reports, risk assessments
4. **Application Control** - Policies, configurations, test results
5. **Patch Compliance** - Vulnerability scans, patch deployment records
6. **Approval Workflow** - Tickets, approval emails, process documentation

---

## Common Pitfalls

### Pitfall 1: No Approved Software List

**Mistake:** "We approve software as needed" (no master list)

**Why It Happens:** Never formalized, assumed everyone knows

**How to Avoid:** Create and maintain approved list, publish to users

### Pitfall 2: Audit Mode Forever

**Mistake:** Application control in audit mode for years

**Why It Happens:** Fear of breaking applications, never tested enforcement

**How to Avoid:** Pilot enforce mode, iterate, deploy

### Pitfall 3: Approving Everything

**Mistake:** Every unauthorized software gets retroactively approved

**Why It Happens:** Easier than saying no, avoiding conflict

**How to Avoid:** Have approval criteria, say no when appropriate

### Pitfall 4: No Patch Testing

**Mistake:** Deploy patches immediately without testing

**Why It Happens:** SLA pressure, "must patch within 7 days"

**How to Avoid:** Test on pilot group, balance speed and stability

### Pitfall 5: Ignoring BYOD Software

**Mistake:** Not inventorying BYOD software at all

**Why It Happens:** Privacy concerns

**How to Avoid:** Inventory containerized/work apps only, respect privacy

### Pitfall 6: Shadow IT Whack-a-Mole

**Mistake:** Remove unauthorized software, users reinstall, repeat

**Why It Happens:** No alternative provided, business need unmet

**How to Avoid:** Understand business need, provide approved alternative

### Pitfall 7: EOL Software Forever

**Mistake:** Software past end-of-life, never replaced

**Why It Happens:** "Business-critical", replacement is expensive/complex

**How to Avoid:** Roadmap for replacement, document compensating controls

### Pitfall 8: No User Communication

**Mistake:** Software removed without warning

**Why It Happens:** "They shouldn't have installed it anyway"

**How to Avoid:** Notify users, provide timeline, offer alternatives

### Pitfall 9: Version Chaos

**Mistake:** 47 different versions of the same software

**Why It Happens:** No standardization, user self-install

**How to Avoid:** Centralized deployment, version control

### Pitfall 10: Licensing Ignored

**Mistake:** Focusing only on security, ignoring licensing compliance

**Why It Happens:** Different team owns licensing

**How to Avoid:** Cross-check software inventory against licenses

---

## Quality Checklist

### Completeness (10 items)

- [ ] All sheets completed
- [ ] Approved software list exists
- [ ] Software inventory comprehensive
- [ ] Unauthorized software identified
- [ ] Application control assessed
- [ ] Patch compliance verified
- [ ] Gaps consolidated
- [ ] Evidence registered
- [ ] Dashboard calculated

### Accuracy (12 items)

- [ ] Software names normalized
- [ ] Versions accurate
- [ ] Prevalence counts correct
- [ ] Unauthorized software comparison accurate
- [ ] Application control status verified
- [ ] Patch data current (≤7 days)
- [ ] Risk assessments justified
- [ ] Metrics calculated correctly
- [ ] No copy-paste errors
- [ ] Dashboard matches source data

### Honesty (8 items)

- [ ] Approved list complete (not aspirational)
- [ ] Unauthorized software not hidden
- [ ] Application control mode accurate (audit vs enforce)
- [ ] Patch compliance honest
- [ ] Gaps documented honestly
- [ ] Risk levels realistic
- [ ] Remediation timelines realistic

### Evidence (6 items)

- [ ] Approved list documented
- [ ] Software inventory exports
- [ ] Application control configs
- [ ] Vulnerability scan reports
- [ ] Approval workflow records
- [ ] All evidence sanitized

### Remediation (6 items)

- [ ] All gaps have plans
- [ ] Plans are specific
- [ ] Owners assigned
- [ ] Target dates set
- [ ] Resources identified
- [ ] Priority assigned

### Integration (5 items)

- [ ] Change management integrated
- [ ] Vulnerability management integrated
- [ ] Patch management integrated
- [ ] Inventory tools verified working

### Stakeholder Input (4 items)

- [ ] IT operations reviewed
- [ ] Change management reviewed
- [ ] Security engineering reviewed
- [ ] Management reviewed

### Consistency (4 items)

- [ ] No contradictions
- [ ] Software names consistent
- [ ] Compliance status matches evidence
- [ ] Dashboard matches details

---

## Review & Approval

### Three-Level Approval Process

#### Level 1: Technical Review

**Reviewer:** IT Operations Lead or Change Manager

**Focus:**

- Software inventory accuracy
- Approved list completeness
- Application control verification
- Patch compliance data

**Checklist:**

- [ ] Software inventory comprehensive
- [ ] Approved list realistic
- [ ] Unauthorized software accurately identified
- [ ] Application control status verified
- [ ] Patch data current

**Outcome:** Approve → Level 2 / Request Changes

#### Level 2: Compliance Review

**Reviewer:** Information Security Manager or Compliance Officer

**Focus:**

- Policy compliance
- Risk assessments
- Evidence quality

**Checklist:**

- [ ] All requirements addressed
- [ ] Risk levels justified
- [ ] Gaps documented with plans
- [ ] Evidence audit-ready

**Outcome:** Approve → Level 3 / Request Changes

#### Level 3: Management Approval

**Reviewer:** CISO, IT Director, or CTO

**Focus:**

- Strategic alignment
- Resource allocation
- Risk acceptance

**Checklist:**

- [ ] Gap priorities acceptable
- [ ] Remediation funded
- [ ] Accepted risks documented
- [ ] Timelines realistic

**Outcome:** Approve / Request Changes / Escalate

### Post-Approval Actions

1. Lock assessment
2. Store in ISMS repository
3. Notify auditors
4. Begin remediation
5. Schedule quarterly reassessment

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
