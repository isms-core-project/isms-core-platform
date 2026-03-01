<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.23.3-UG:framework:UG:a.8.23.3 -->
**ISMS-IMP-A.8.23.3-UG - Policy Configuration Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.23: Web Filtering

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Policy Configuration Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.23.3-UG |
| **Related Policy** | ISMS-POL-A.8.23 (Web Filtering) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.23 (Web Filtering) |
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

- ISMS-POL-A.8.23 (Web Filtering)
- ISMS-IMP-A.8.23.1 (Filtering Infrastructure Assessment)
- ISMS-IMP-A.8.23.2 (Network Coverage Assessment)
- ISMS-IMP-A.8.23.4 (Monitoring & Response Assessment)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.23.3-TG.

---

**Audience:** Security Team, Policy Owners, Network Team, Compliance Team

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Threat Protection | Assess threat protection policy configuration |
| 3 | Category Management | Manage URL category filtering rules |
| 4 | Custom Lists | Document custom allow and block lists |
| 5 | Policy Exceptions | Track and manage policy exceptions |
| 6 | User Group Policies | Document user group-specific filtering policies |
| 7 | Acceptable Use Alignment | Verify policy alignment with Acceptable Use Policy |
| 8 | Policy Review Process | Document policy review and update procedures |
| 9 | Evidence Register | Store and reference evidence supporting assessments |
| 10 | Gap Analysis | Identify policy configuration gaps |
| 11 | Summary Dashboard | Compliance status and key metrics overview |
| 12 | Approval Sign-Off | Management review sign-off and certification |

---

## Assessment Overview

### What This Assessment Evaluates

This assessment documents HOW web filtering solutions are configured. Unlike Assessment 1 (WHAT solutions you have) and Assessment 2 (WHERE they're deployed), this assessment focuses on POLICY CONFIGURATION - the rules, categories, exceptions, and user policies that determine what gets blocked or allowed.

### Why This Matters

This assessment verifies [Organisation]'s compliance with:

- ISO/IEC 27001:2022 Control A.8.23: Web Filtering
- ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements): Threat Protection Requirements
- ISMS-POL-A.8.23, Section 2.2 (Category Filtering Approach): Category Filtering Requirements
- ISMS-POL-A.8.23, Section 3.3 (Exception Management): Exception Management Requirements

Filtering technology without proper policy configuration provides little protection. This assessment ensures policies are properly configured, documented, regularly reviewed, and aligned with [Organisation]'s Acceptable Use Policy (AUP). It verifies that threat protection is mandatory, category filtering aligns with organisational risk tolerance, and exceptions are properly managed.

### What You'll Document

- Filtering philosophy (restrictive, trust-based, or hybrid)
- Threat protection policies (malware, phishing, ransomware, etc.)
- Category filtering policies (if used)
- Custom block/allow URL lists
- Policy exceptions and approval process
- User/group-based policies
- Alignment with Acceptable Use Policy
- Policy review process and frequency

**Key Principle:** This assessment is **approach-agnostic**. Whether you use restrictive filtering (block most things), trust-based filtering (block threats only), or hybrid (balanced), the framework adapts. You document YOUR policy philosophy and verify it's properly implemented and managed.

### The Three Filtering Philosophies

1. **Restrictive (Default Deny):** Block everything by default, allow only approved categories/URLs

   - Common in: Government, healthcare, education (CIPA compliance)
   - Pro: Maximum control
   - Con: High maintenance (many exception requests)

2. **Trust-Based (Default Allow):** Allow everything, block known threats only

   - Common in: Tech companies, creative industries, startups
   - Pro: Maximum productivity
   - Con: Relies heavily on user awareness

3. **Hybrid (Balanced):** Block threats + some high-risk categories, allow most business content

   - Common in: Most enterprises
   - Pro: Balance security and productivity
   - Con: Requires tuning

**All three are valid!** This assessment works for any approach.

### How This Relates to Other Assessments

- **ISMS-IMP-A.8.23.1** (Infrastructure): WHAT filtering solutions you have
- **ISMS-IMP-A.8.23.2** (Coverage): WHERE those solutions are deployed
- **ISMS-IMP-A.8.23.3** (THIS): HOW those solutions are configured
- **ISMS-IMP-A.8.23.4** (Monitoring): HOW you monitor filtering effectiveness

All four must align for complete web filtering compliance.

**Estimated Time:** 8-12 hours depending on policy complexity

---

## Prerequisites

Before starting this assessment, ensure you have:

**Access & Permissions:**

- Administrative access to filtering solutions (or coordinate with admins)
- Access to filtering policy configuration screens
- Access to category lists and custom URL lists
- Access to exception request/approval system
- Access to Acceptable Use Policy document
- Access to policy review meeting minutes/records

### Required Information

- Current filtering policies (exported or documented)
- List of blocked/allowed categories (if using category filtering)
- Custom block/allow URL lists
- Exception requests and approvals (past 12 months)
- User/group policy assignments
- Policy review schedule and records
- Acceptable Use Policy (current version)

**Completed Prerequisites:**

- ISMS-IMP-A.8.23.1 (Infrastructure Assessment) should be complete
- ISMS-IMP-A.8.23.2 (Coverage Assessment) should be complete
- You should know which filtering solutions you have and where they're deployed
- Acceptable Use Policy should exist and be current

**People to Consult:**

- Security Team (policy configuration, threat intelligence)
- Policy Owners (filtering policy decisions)
- Network Team (technical implementation)
- Compliance Team (regulatory requirements, AUP)
- HR (Acceptable Use Policy, user communications)
- Help Desk (exception requests, user complaints)
- Legal (policy language, liability considerations)

**Time Allocation:**

- Threat protection assessment: 2-3 hours
- Category filtering documentation: 2-4 hours (if used)
- Custom lists inventory: 1-2 hours
- Exception tracking: 2-3 hours
- User/group policies: 1-2 hours
- AUP alignment: 1-2 hours
- Policy review process: 1 hour
- Evidence collection: 1-2 hours

---

## Assessment Workflow

Follow this systematic approach to complete the assessment:

**Step 1: Initial Setup (30 minutes)**

1. Open the workbook: `ISMS-IMP-A.8.23.3_Policy_Configuration_[YYYYMMDD].xlsx`
2. Read the "Instructions & Legend" sheet completely
3. Fill in yellow highlighted fields in Document Information section
4. Gather policy documentation and configuration exports
5. Have Acceptable Use Policy document available
6. Determine your filtering philosophy (restrictive, trust-based, or hybrid)

**Step 2: Document Filtering Philosophy (15 minutes)**

Before diving into details, document your approach:

1. Review your organisation's filtering philosophy
2. Common indicators:

   - **Restrictive:** Many categories blocked, frequent exception requests, tight control
   - **Trust-Based:** Only threats blocked, minimal exceptions needed, user freedom
   - **Hybrid:** Threats blocked + some categories (adult, illegal, high-risk)

3. Document in workbook header
4. This determines which sheets are applicable:

   - Threat Protection: **ALWAYS applicable** (all approaches)
   - Category Management: **Skip if trust-based**
   - Custom Lists: Applicable to all
   - Exceptions: Applicable to all (but volume varies)
   - User/Group Policies: If using differentiated policies
   - AUP Alignment: **ALWAYS applicable**
   - Review Process: **ALWAYS applicable**

**Step 3: Threat Protection Assessment (2-3 hours)**

MANDATORY for all filtering approaches:

1. Go to "Threat_Protection" sheet
2. For each threat type (malicious URLs, phishing, malware, ransomware, exploits, C2, cryptojacking, zero-day):

   - Policy configured? (✅/⚠️/❌)
   - Blocking method (how does it work?)
   - Effectiveness (High/Medium/Low)
   - False positive rate (Rare/Occasional/Frequent)
   - Last tested date
   - Evidence location

3. Document threat intelligence feeds:

   - Which feeds are you using?
   - Update frequency
   - Last update date
   - Auto-update enabled?

4. Complete compliance checklist
5. Test critical protections:

   - Use EICAR test file (malware test)
   - Use PhishTank samples (phishing test)
   - Verify blocks are working

6. Collect evidence (screenshots, test results)

**Step 4: Category Filtering Documentation (2-4 hours, if applicable)**

Skip this step if trust-based approach:

1. Go to "Category_Management" sheet
2. Set filtering philosophy dropdown (will auto-mark N/A if trust-based)
3. If restrictive or hybrid:

   - Review all available categories (~30-40 typically)
   - For EACH category:
     - Policy action (Block/Allow/Warn/Monitor)
     - Applied to (All Users/Groups/etc.)
     - Business justification (why block or allow?)
     - Any exceptions?
     - Exception count
     - Last reviewed date
     - Evidence (config screenshot)

4. Common categories to address:

   - **Always block:** Adult content, illegal activities, hate, violence, weapons
   - **Often block:** Gambling, anonymous proxies/VPN, P2P file sharing
   - **Debate:** Social media, streaming, personal storage, shopping, games
   - **Usually allow:** News, education, business, technology

5. Document category summary (how many blocked vs. allowed)
6. Note: "Block" doesn't mean 100% blocked if exceptions exist

**Step 5: Custom Lists Inventory (1-2 hours)**

Document organisation-maintained URL lists:

1. Go to "Custom_Lists" sheet
2. For EACH custom list:

   - List name (descriptive)
   - List type (Block/Allow/Exception)
   - URL count (how many entries?)
   - Purpose (why does this list exist?)
   - Maintained by (who updates it?)
   - Last updated date
   - Review frequency
   - Evidence (export of list)

3. Common custom lists:

   - **Block lists:** Suspicious sites not in vendor database, sites violating AUP
   - **Allow lists:** Business-critical sites, partner sites, sites generating false positives
   - **Exception lists:** Approved exceptions to category rules

4. Document list management process:

   - How are URLs added?
   - Who approves additions?
   - How often are lists reviewed?
   - Where are changes documented?

**Step 6: Policy Exceptions Tracking (2-3 hours)**

Document ALL policy exceptions:

1. Go to "Policy_Exceptions" sheet
2. For EACH exception (review past 12 months):

   - Exception ID (EXC-001, EXC-002, etc.)
   - Exception type (URL/Category/User/Group/Temporary/Permanent)
   - What is being excepted?
   - Requestor (who requested?)
   - Business justification (why needed?)
   - Approved by (who approved?)
   - Approval date
   - Expiration date (if temporary)
   - Status (Active/Expired/Revoked)
   - Risk level (Critical/High/Medium/Low)
   - Compensating controls (what mitigates risk?)
   - Evidence (approval email/ticket)

3. Exception categories:

   - **URL Exception:** Specific URL allowed despite category block
   - **Category Exception:** User/group exempt from category rule
   - **User Exception:** Specific user gets different policy
   - **Group Exception:** Group gets different policy
   - **Temporary Exception:** Time-limited exception
   - **Permanent Exception:** Ongoing exception

4. Flag issues:

   - Expired exceptions still active
   - No approval documentation
   - Missing business justification
   - High-risk exceptions without compensating controls

5. Calculate exception metrics:

   - Total exceptions
   - Active vs. expired
   - High-risk exceptions
   - Average time to approval

**Step 7: User/Group Policies (1-2 hours, if applicable)**

If using differentiated policies:

1. Go to "User_Group_Policies" sheet
2. Document policy hierarchy:

   - Standard policy (applies to most users)
   - Restrictive policy (if any)
   - Relaxed policy (if any)
   - Executive policy (if any)
   - Guest policy (if any)
   - Contractor policy (if any)

3. For EACH policy type:

   - Policy name
   - Filtering level (High/Medium/Low)
   - HTTPS inspection (Yes/No/Selective)
   - Applied to (which groups?)
   - User count
   - Key differences from standard
   - Business justification
   - Evidence (policy config)

4. Common differentiation:

   - Executives: Less restrictive (more allow exceptions)
   - Finance/HR: More restrictive (handles sensitive data)
   - Contractors: Restrictive (limited access)
   - Guests: Very restrictive (minimal access)

5. Verify alignment:

   - Do policies match organisational hierarchy?
   - Are policies justified (not just "because they're execs")?
   - Is differentiation documented and approved?

**Step 8: Acceptable Use Policy Alignment (1-2 hours)**

Critical compliance requirement:

1. Go to "Acceptable_Use_Alignment" sheet
2. Obtain current AUP document
3. For EACH AUP requirement related to internet use:

   - AUP requirement text
   - Is it enforced by filtering? (✅/⚠️/❌)
   - If yes: How is it enforced?
   - If no/partial: What's the gap?
   - Evidence (AUP document + filtering config)

4. Common AUP requirements:

   - "No accessing adult content"
   - "No downloading illegal material"
   - "No excessive personal use during work hours"
   - "No bypassing security controls"
   - "No accessing prohibited categories"

5. Gap analysis:

   - AUP prohibits X, but filtering doesn't block X = GAP
   - Filtering blocks Y, but AUP doesn't mention Y = Policy drift

6. Document alignment percentage
7. Create action plan for gaps

**Step 9: Policy Review Process (1 hour)**

Document governance:

1. Go to "Policy_Review_Process" sheet
2. Document review schedule:

   - Review frequency (monthly/quarterly/annually?)
   - Who participates? (Security, Compliance, Network, HR, Legal)
   - What is reviewed? (Threat policies, categories, exceptions, AUP alignment)
   - Review criteria (effectiveness, false positives, business impact)

3. Document recent reviews (past 12 months):

   - Review date
   - Review type (Full/Partial/Ad-hoc/Incident-Driven)
   - Attendees
   - Changes made
   - Evidence (meeting minutes)

4. Document change management:

   - How are policy changes requested?
   - Who approves changes?
   - How are users notified?
   - Where are changes documented?

5. Verify compliance:

   - Is review happening on schedule?
   - Are reviews documented?
   - Are review findings addressed?

**Step 10: Gap Analysis (1-2 hours)**

Consolidate all gaps:

1. Go to "Gap_Analysis" sheet
2. Gather gaps from:

   - Threat Protection (unconfigured protections)
   - Category Management (inconsistent policies)
   - Custom Lists (outdated lists)
   - Policy Exceptions (expired, unapproved, high-risk)
   - User/Group Policies (unjustified differentiation)
   - AUP Alignment (filtering doesn't enforce AUP)
   - Review Process (reviews not happening)

3. For EACH gap:

   - Gap ID (GAP-001, etc.)
   - Policy area affected
   - Gap description
   - Risk level (Critical/High/Medium/Low)
   - Impact
   - Root cause
   - Remediation plan
   - Owner
   - Target date
   - Status (Open/In Progress/Resolved)

4. Prioritize:

   - Threat protection gaps = CRITICAL
   - AUP misalignment = HIGH
   - Expired exceptions = MEDIUM
   - Review process gaps = MEDIUM

**Step 11: Evidence Collection (1-2 hours)**

1. Go to "Evidence_Register" sheet
2. Collect evidence for ALL claims:

   - Policy configuration screenshots
   - Policy exports (if available)
   - Category lists
   - Custom URL lists
   - Exception approvals
   - AUP document
   - Policy review meeting minutes
   - Change management records
   - Test results
   - User communications

3. For each evidence item:

   - Evidence ID (EVD-001, etc.)
   - Evidence type
   - Description
   - Related sheet/section
   - Location/path
   - Date collected
   - Collected by
   - Verification status

**Step 12: Quality Check (1 hour)**

Before submitting for review, verify:

- [ ] Filtering philosophy documented
- [ ] All threat protections addressed
- [ ] Category policies documented (or N/A if trust-based)
- [ ] Custom lists inventoried
- [ ] All exceptions tracked (especially expired ones)
- [ ] User/group policies documented (if applicable)
- [ ] AUP alignment analysed
- [ ] Review process documented
- [ ] All gaps identified with remediation plans
- [ ] Evidence collected and referenced

**Step 13: Review & Approval (1-2 weeks)**

1. Go to "Approval_Sign_Off" sheet
2. Complete "Assessment Completed By" section
3. Submit to Policy Owner for policy review
4. Submit to Security Team for technical review
5. Submit to Compliance Team for AUP alignment review
6. Submit to Information Security Officer for final review
7. Address any review comments
8. Obtain CISO approval
9. Set next review date (typically +3 months)

---

## Question-by-Question Guidance

This section provides detailed guidance for completing each field in the assessment workbook.

### Threat_Protection Sheet

**Q: Threat Type - Policy Configured?**

- **Dropdown:** ✅ Configured / ⚠️ Partial / ❌ Not Configured / N/A
- **Choose "✅ Configured":** Threat protection active and operational
- **Choose "⚠️ Partial":** Partially configured (e.g., HTTP only, not HTTPS)
- **Choose "❌ Not Configured":** No protection for this threat
- **Choose "N/A":** Rare - threat type not applicable
- **Where to verify:** Admin console → Threat Protection settings
- **Test:** Use EICAR (malware), PhishTank samples (phishing)
- **Policy requirement:** ALL threat types SHOULD be configured (mandatory baseline)

**Q: Blocking Method**

- **What to enter:** How does your solution block this threat?
- **Examples:**
  - "URL reputation database (vendor-maintained)"
  - "Threat intelligence feeds (updated hourly)"
  - "Real-time cloud lookup"
  - "File hash matching"
  - "Behavioral analysis / sandboxing"
  - "DNS blackhole"
- **Where to find:** Product documentation, threat protection settings
- **Why it matters:** Different methods have different effectiveness

**Q: Effectiveness**

- **Dropdown:** High / Medium / Low / Unknown
- **Choose "High":** >95% catch rate, few false negatives
- **Choose "Medium":** 80-95% catch rate
- **Choose "Low":** <80% catch rate or significant gaps
- **Choose "Unknown":** Not measured/tested
- **How to assess:** Review block logs, incident data, test results
- **Evidence:** Block statistics, test results

**Q: False Positives**

- **Dropdown:** Rare / Occasional / Frequent / Unknown
- **Choose "Rare":** <1% of blocks are false positives
- **Choose "Occasional":** 1-5% false positives
- **Choose "Frequent":** >5% false positives (problematic!)
- **How to assess:** Review help desk tickets, unblock requests
- **Why it matters:** High false positive rate = user frustration, shadow IT

**Q: Last Tested**

- **What to enter:** When was this protection last verified?
- **Format:** DD.MM.YYYY
- **How to test:** Use safe test sites (EICAR, PhishTank)
- **Frequency:** Test critical protections quarterly minimum
- **Red flag:** Never tested = you don't know if it works

**Threat Intelligence Integration Section:**

- **Feed Sources:** Which threat intel feeds are you using?
- **Update Frequency:** How often are feeds updated?
- **Auto-Update:** Is automatic updating enabled?
- **Evidence:** Feed subscription confirmation, update logs

### Category_Management Sheet

**Q: Filtering Philosophy**

- **Dropdown:** Restrictive (Default Deny) / Trust-Based (Threats Only) / Hybrid (Balanced)
- **Choose carefully:** This determines rest of assessment
- **If "Trust-Based":** Category Management automatically marked N/A

**Q: Category - Policy Action**

- **Dropdown:** Block / Allow / Warn / Monitor Only / N/A
- **Choose "Block":** Category completely blocked
- **Choose "Allow":** Category explicitly allowed
- **Choose "Warn":** User warned but can proceed
- **Choose "Monitor Only":** Logged but not blocked
- **Choose "N/A":** Not applicable to this organisation
- **Example:** Adult Content = Block, News/Media = Allow

**Q: Applied To**

- **Dropdown:** All Users / Specific Groups / Specific Users / Network Segments / Device Type
- **Document scope:** Who does this policy apply to?
- **Examples:**
  - "All Users" (standard policy)
  - "Finance Group" (restrictive policy)
  - "Executive Group" (relaxed policy)
  - "Guest Network" (very restrictive)

**Q: Business Justification**

- **What to enter:** WHY is this category blocked or allowed?
- **Good examples:**
  - "Adult Content blocked: AUP violation, harassment risk, bandwidth"
  - "Social Media allowed: Marketing team requires for business"
  - "Streaming blocked: Bandwidth constraints, productivity concerns"
- **Bad examples:** "Policy says so" (not a justification)
- **Why it matters:** Audit defense, policy review decisions

**Q: Exceptions?**

- **Dropdown:** Yes / No
- **Choose "Yes":** Exceptions exist for this category
- **If Yes:** Document in Policy_Exceptions sheet

**Q: Exception Count**

- **What to enter:** How many exceptions exist?
- **Format:** Number
- **Cross-check:** Should match exceptions in Policy_Exceptions sheet
- **Red flag:** High exception count = policy not aligned with business needs

### Custom_Lists Sheet

**Q: List Name**

- **What to enter:** Descriptive name for this list
- **Examples:**
  - "Corporate Block List"
  - "Partner Allow List"
  - "Social Media Exceptions"
  - "Security Research Sites"

**Q: List Type**

- **Dropdown:** Block List / Allow List / Exception List
- **Block List:** URLs to block (beyond vendor categories)
- **Allow List:** URLs to explicitly allow (override blocks)
- **Exception List:** URLs exempt from rules

**Q: URL Count**

- **What to enter:** How many URLs in this list?
- **Format:** Number
- **Where to find:** List export, list management interface
- **Indicator:** Large lists (>1000 URLs) may indicate policy problem

**Q: Purpose**

- **What to enter:** Why does this list exist?
- **Examples:**
  - "Block malicious sites not in vendor database"
  - "Allow business-critical partner sites"
  - "Exception for marketing team social media"
- **Be specific:** Helps during policy reviews

**Q: Maintained By**

- **What to enter:** Who updates this list?
- **Format:** Name or role
- **Examples:** "Security Team", "Network Admin", "John Smith"
- **Should have:** Clear ownership for each list

**Q: Last Updated**

- **What to enter:** When was list last modified?
- **Format:** DD.MM.YYYY
- **Where to find:** List management logs, change management
- **Red flag:** Lists not updated in >90 days may be stale

**Q: Review Frequency**

- **Dropdown:** Daily / Weekly / Monthly / Quarterly / Annually / As-needed
- **Recommend:**
  - Block lists: Monthly review minimum
  - Allow lists: Quarterly review minimum
  - Exception lists: Monthly review (due to business changes)

### Policy_Exceptions Sheet

**Q: Exception Type**

- **Dropdown:** URL Exception / Category Exception / User Exception / Group Exception / Temporary Exception / Permanent Exception
- **Examples:**
  - URL Exception: "Allow facebook.com for Marketing despite Social Media block"
  - Category Exception: "Allow Streaming category for Video Production team"
  - User Exception: "CEO exempt from category filtering"
  - Temporary Exception: "Allow Recruitment sites during hiring period"

**Q: What is Being Excepted?**

- **What to enter:** Specific exception details
- **Examples:**
  - "URL: linkedin.com/recruiter"
  - "Category: Social Networking"
  - "User: john.smith@org.com"
  - "Group: Marketing_Team"

**Q: Business Justification**

- **What to enter:** WHY is this exception needed?
- **Good examples:**
  - "Marketing requires LinkedIn for lead generation campaigns"
  - "Engineering needs GitHub (File Sharing category) for code repositories"
  - "Executive travel requires booking sites (Shopping category)"
- **Bad examples:** "User requested it" (not sufficient)
- **Required:** Strong business case for audit defense

**Q: Approved By**

- **What to enter:** Who approved this exception?
- **Format:** Name + Date
- **Authority:** Should be appropriate for risk level
  - Low risk: Team lead OK
  - High risk: CISO approval required
- **Evidence:** Approval email/ticket required

**Q: Expiration Date**

- **What to enter:** When does exception expire?
- **Format:** DD.MM.YYYY or "Permanent"
- **For temporary:** Specific end date
- **For permanent:** "Permanent" (but still review annually)
- **Red flag:** Expired exceptions still active

**Q: Status**

- **Dropdown:** Active / Expired / Revoked / Under Review
- **Active:** Currently in effect
- **Expired:** Expiration date passed (needs renewal or removal)
- **Revoked:** Cancelled before expiration
- **Under Review:** Being re-evaluated

**Q: Risk Level**

- **Dropdown:** Critical / High / Medium / Low
- **Critical:** Exception bypasses critical security controls
- **High:** Significant security risk
- **Medium:** Moderate risk with compensating controls
- **Low:** Minimal risk

**Q: Compensating Controls**

- **What to enter:** What mitigates the risk?
- **Examples:**
  - "Enhanced logging and monitoring"
  - "Time-limited (30 days only)"
  - "Requires MFA for access"
  - "User trained on risks"
- **Required:** High/Critical exceptions MUST have compensating controls

### User_Group_Policies Sheet

**Q: Policy Name**

- **What to enter:** Descriptive name for this policy
- **Examples:**
  - "Standard User Policy"
  - "Executive Policy"
  - "Guest Network Policy"
  - "Contractor Policy"

**Q: Policy Type**

- **Dropdown:** Standard / Restrictive / Relaxed / Executive / Guest / Contractor
- **Standard:** Default policy for most users
- **Restrictive:** Tighter controls (finance, HR)
- **Relaxed:** Fewer restrictions (executives, senior management)
- **Guest:** Very restrictive (visitors)
- **Contractor:** Limited access

**Q: Filtering Level**

- **Dropdown:** High (Strict) / Medium (Balanced) / Low (Permissive)
- **High:** Many categories blocked, strict rules
- **Medium:** Balanced approach
- **Low:** Minimal blocking (threats only, mostly)

**Q: HTTPS Inspection**

- **Dropdown:** Yes / No / Selective
- **Yes:** All HTTPS traffic inspected
- **No:** HTTPS not inspected (domain/IP only)
- **Selective:** Some HTTPS inspected (e.g., skip financial sites)

**Q: Applied To**

- **What to enter:** Which groups/users get this policy?
- **Examples:**
  - "All_Employees AD group (2,500 users)"
  - "Executive_Team AD group (15 users)"
  - "Guest_WiFi VLAN (up to 100 concurrent)"

**Q: Key Differences from Standard**

- **What to enter:** How does this differ from standard policy?
- **Examples:**
  - "Executive: Social media allowed, streaming allowed"
  - "Guest: Only web browsing allowed, all categories blocked except basic business"
  - "Contractor: No file download, no streaming, restrictive categories"

**Q: Business Justification**

- **What to enter:** WHY does this group need different policy?
- **Good examples:**
  - "Executives require flexibility for business travel, partner communication"
  - "Guests are untrusted, need maximum restrictions"
  - "Finance handles sensitive data, needs restrictive policy"
- **Bad examples:** "They're executives" (not sufficient - need business reason)

### Acceptable_Use_Alignment Sheet

**Q: AUP Requirement Text**

- **What to enter:** Exact text from AUP related to internet use
- **Examples:**
  - "Employees shall not access adult content during work"
  - "Personal use of internet must be reasonable and not excessive"
  - "Prohibited: illegal activities, copyright infringement, harassment"

**Q: Enforced by Filtering?**

- **Dropdown:** ✅ Yes / ⚠️ Partial / ❌ No / N/A
- **✅ Yes:** AUP requirement enforced by filtering
- **⚠️ Partial:** Partially enforced (e.g., blocks some but not all)
- **❌ No:** AUP requirement not enforced by filtering
- **N/A:** AUP requirement not related to web filtering

**Q: How Enforced?**

- **What to enter:** If Yes/Partial, explain HOW filtering enforces this
- **Examples:**
  - "Adult Content category blocked for all users"
  - "Excessive use detected via monitoring (>2GB/day bandwidth)"
  - "Illegal Activities category blocked"
- **If No:** Explain why not (technical limitation, policy decision, etc.)

**Q: Gap?**

- **What to enter:** If No/Partial, what's the gap?
- **Examples:**
  - "AUP prohibits gambling, but Gambling category not blocked"
  - "AUP mentions 'excessive use' but no quantitative threshold configured"
  - "AUP prohibits bypassing controls, but VPN/proxy detection not enabled"

**Q: Evidence**

- **What to enter:** Reference to AUP document + filtering config
- **Format:** Evidence IDs
- **Examples:**
  - "EVD-050 (AUP v2.1), EVD-051 (Category config screenshot)"

### Policy_Review_Process Sheet

**Q: Review Frequency**

- **Dropdown:** Daily / Weekly / Monthly / Quarterly / Annually / As-needed
- **Recommend:**
  - Threat policies: Quarterly minimum
  - Category policies: Quarterly minimum
  - Exceptions: Monthly review
  - AUP alignment: Annually minimum
  - Full policy review: Annually

**Q: Review Type**

- **Dropdown:** Full Review / Partial Review / Ad-hoc / Incident-Driven / Regulatory Change
- **Full Review:** Complete review of all policies
- **Partial Review:** Specific area reviewed
- **Ad-hoc:** Unscheduled review (e.g., new threat)
- **Incident-Driven:** Review triggered by incident
- **Regulatory Change:** Review due to regulation change

**Q: Attendees**

- **What to enter:** Who participated in review?
- **Should include:** Security, Compliance, Network, HR, Legal (as needed)
- **Format:** "Security Manager (J. Smith), Compliance Lead (A. Jones), HR Rep (M. Davis)"

**Q: Changes Made**

- **What to enter:** What policy changes resulted?
- **Examples:**
  - "Added Cryptojacking to blocked threats"
  - "Removed Social Media block for Marketing group"
  - "Updated AUP to reflect filtering changes"
  - "No changes - policy still appropriate"

**Q: Evidence**

- **What to enter:** Where is review documented?
- **Format:** Evidence IDs
- **Examples:**
  - "EVD-080 (Meeting minutes 2025-10-15)"
  - "EVD-081 (Policy change request PCR-2025-042)"

### Gap_Analysis Sheet

**Q: Policy Area**

- **Dropdown:** Threat Protection / Category Filtering / Custom Lists / Exceptions / User Policies / AUP Alignment / Review Process
- **Categorize gaps** for tracking and reporting

**Q: Gap Description**

- **What to enter:** Clear, specific description
- **Good examples:**
  - "Cryptojacking protection not configured - emerging threat not covered"
  - "AUP prohibits gambling but Gambling category not blocked"
  - "50 exceptions expired >90 days ago, still active"
  - "Policy review not conducted in past 6 months (overdue)"
- **Bad examples:** "Policies need work" (too vague)

**Q: Risk Level**

- **Dropdown:** Critical / High / Medium / Low
- **Critical:** Immediate security risk, major policy violation
- **High:** Significant risk, should remediate soon
- **Medium:** Moderate risk, remediate within quarter
- **Low:** Minor issue, remediate when feasible

**Q: Remediation Plan**

- **What to enter:** How will you close this gap?
- **Good examples:**
  - "Enable cryptojacking protection in threat settings (1 hour task)"
  - "Add Gambling category to block list, communicate to users"
  - "Review all expired exceptions, renew or revoke within 30 days"
  - "Schedule quarterly policy review meetings starting Q2"
- **Include:** Specific actions, timelines

---

## Evidence Collection

### What Constitutes Acceptable Evidence

Auditors need to verify your policy configuration claims:

**Policy Configuration Evidence:**

- Screenshots of filtering policy settings
- Policy exports (XML, JSON, text)
- Category lists (blocked/allowed)
- Custom URL lists (exports)
- User/group policy assignments

**Exception Evidence:**

- Exception request forms/emails
- Approval emails/tickets
- Exception lists (current)
- Expiration tracking logs

**AUP Evidence:**

- Current Acceptable Use Policy document
- Alignment analysis document
- Gap remediation plans

**Review Process Evidence:**

- Policy review meeting minutes
- Review schedules/calendars
- Policy change requests
- User communications about policy changes

**Testing Evidence:**

- Threat protection test results
- Category block test screenshots
- False positive investigation records

**Organize Evidence:**
1. Folder: `Evidence/A.8.23.3_Policy_Configuration/`
2. Subfolders: `Threat_Protection/`, `Categories/`, `Custom_Lists/`, `Exceptions/`, `AUP/`, `Reviews/`
3. Naming: `EVD-001_Threat_Policy_Config_Screenshot.png`
4. Cross-reference: Link Evidence IDs to claims

---

## Common Pitfalls

**Pitfall 1: Confusing Infrastructure with Policy**

- **Problem:** Documenting capabilities instead of actual configured policies
- **Example:** "Solution CAN do HTTPS inspection" vs. "HTTPS inspection IS enabled"
- **Solution:** Document what IS configured, not what CAN be configured
- **Consequence:** Assessment doesn't reflect actual protection

**Pitfall 2: Expired Exceptions Still Active**

- **Problem:** Temporary exceptions expire but remain active
- **Solution:** Review exceptions monthly, revoke/renew expired ones
- **Common:** "30-day exception granted 6 months ago, still active"
- **Consequence:** Unmanaged risk, audit finding

**Pitfall 3: AUP-Filtering Misalignment**

- **Problem:** AUP says one thing, filtering does another
- **Example:** AUP prohibits gambling, but Gambling category not blocked
- **Solution:** Annual alignment review minimum
- **Consequence:** Policy isn't enforced, compliance gap

**Pitfall 4: Undocumented Filtering Philosophy**

- **Problem:** No clear policy approach documented
- **Result:** Inconsistent policies, unclear why categories blocked/allowed
- **Solution:** Document philosophy, align all policies to it
- **Consequence:** Policy drift, inconsistent enforcement

**Pitfall 5: Exception Approval Without Business Case**

- **Problem:** Exceptions approved with weak justifications
- **Example:** "User requested" instead of "Marketing requires LinkedIn for campaigns"
- **Solution:** Require strong business justification for all exceptions
- **Consequence:** Audit questions, unjustified risk

**Pitfall 6: Stale Custom Lists**

- **Problem:** Custom block/allow lists not reviewed regularly
- **Solution:** Monthly review minimum
- **Common:** Lists with 50% dead links, old partner sites, etc.
- **Consequence:** False positives, outdated controls

**Pitfall 7: No Policy Review Process**

- **Problem:** Policies set once, never reviewed
- **Solution:** Quarterly review minimum, document process
- **Consequence:** Policies become outdated, miss new threats

**Pitfall 8: Testing Threat Protection Only Once**

- **Problem:** Test at deployment, never again
- **Solution:** Quarterly testing minimum
- **Reality:** "We thought it was working but it's been broken for 3 months"
- **Consequence:** False confidence in protection

**Pitfall 9: Differentiated Policies Without Justification**

- **Problem:** Executives get relaxed policy "because they're executives"
- **Solution:** Document business justification for every policy difference
- **Consequence:** Audit finding, favoritism perception

**Pitfall 10: Category Blocking Without Exception Process**

- **Problem:** Block categories but no way to request exceptions
- **Result:** Shadow IT, VPN services, user frustration
- **Solution:** Clear exception request process, reasonable approval
- **Consequence:** Users bypass filtering entirely

---

## Quality Checklist

Before submitting for review, verify:

**Completeness:**

- [ ] Filtering philosophy documented
- [ ] All threat protections assessed
- [ ] Category policies documented (or N/A if trust-based)
- [ ] Custom lists inventoried
- [ ] All exceptions tracked and current
- [ ] User/group policies documented (if applicable)
- [ ] AUP alignment analysed
- [ ] Policy review process documented
- [ ] All gaps identified with remediation plans
- [ ] Evidence collected

**Accuracy:**

- [ ] Policy status reflects actual configuration (not capabilities)
- [ ] Exception approvals verified with documentation
- [ ] Expired exceptions flagged
- [ ] AUP alignment accurate (actually checked against current AUP)
- [ ] Review process matches actual practice

**Consistency:**

- [ ] Policies align with documented philosophy
- [ ] User/group policies justified
- [ ] Exception risk levels appropriate
- [ ] Evidence IDs cross-referenced correctly

**Policy Governance:**

- [ ] All exceptions have business justification
- [ ] All high/critical exceptions have approvals
- [ ] Policy review happening on schedule
- [ ] Changes documented
- [ ] Users notified of policy changes

**Evidence:**

- [ ] Evidence Register populated
- [ ] Evidence files organised
- [ ] Evidence IDs match references
- [ ] Screenshots show current date
- [ ] Approvals documented

---

## Review & Approval

**Step 1: Self-Review**

- Run through Quality Checklist
- Verify policy configuration accuracy
- Check exception approvals
- Ensure AUP alignment

**Step 2: Policy Owner Review**

- Policy Owner reviews policy decisions
- Verifies business justifications
- Confirms alignment with organisational goals
- Typical turnaround: 2-3 days

**Step 3: Security Team Technical Review**

- Verify technical accuracy
- Confirm threat protections configured
- Review exception risk assessments
- Typical turnaround: 3-5 days

**Step 4: Compliance Team Review**

- Verify AUP alignment
- Check regulatory compliance (if applicable)
- Review exception approvals
- Typical turnaround: 3-5 days

**Step 5: Information Security Officer Review**

- Complete "Assessment Completed By" in Approval_Sign_Off sheet
- Submit to ISO
- ISO reviews for:
  - Policy completeness
  - Exception management
  - AUP alignment
  - Review process adequacy
  - Gap remediation plans
- ISO recommendation: Approve / Approve with Conditions / Reject / Require Rework
- Typical turnaround: 3-5 days

**Step 6: Address Review Comments**

- Make requested corrections
- Update version/date
- Resubmit with change summary
- Typical turnaround: 2-3 days

**Step 7: CISO Approval**

- CISO reviews:
  - Overall policy posture
  - Exception risk acceptance
  - AUP enforcement
  - Gap remediation plans
- Decision: Approved / Approved with Conditions / Rejected
- Typical turnaround: 2-3 days

**Step 8: Documentation & Communication**

- Set assessment status to "Final"
- Set next review date (+3 months)
- File in document management
- Notify gap owners of assignments
- Communicate policy changes to users
- Create reminders for:
  - Exception expirations
  - Policy reviews
  - Gap remediation dates
  - Next quarterly assessment

**Approval Timeline:** 2-3 weeks from submission to final approval

**If Rejected:**

- Incomplete policy documentation
- Exceptions without proper approval
- AUP misalignment not addressed
- Missing evidence
- Review process not documented

---

**END OF USER GUIDE**

---

*"A policy is only as effective as its weakest rule."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
