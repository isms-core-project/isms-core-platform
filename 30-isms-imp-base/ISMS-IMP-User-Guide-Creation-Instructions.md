# IMP User Guide Creation Instructions
## Systematic Process for Adding User Completion Guides to Assessment Specifications

**Version:** 1.0  
**Date:** [Date]  
**Purpose:** Standardized methodology for converting technical IMP specifications into dual-audience documents with integrated user completion guides  
**Scope:** All ISO 27001:2022 Annex A control assessment specifications (ISMS-IMP-A.X.XX series)

---

## Background & Context

### The Problem Identified

Original IMP documents (ISMS-IMP-A.X.XX series) were written as **technical specifications** for workbook generation:
- **Target audience:** Python developers, Excel workbook builders
- **Content focus:** Sheet structure, column definitions, formulas, data validation rules
- **Use case:** Building/maintaining assessment workbooks programmatically

**Gap:** No guidance for **operational users** (Security Team, System Owners, Network Team) on HOW TO COMPLETE the assessments.

### The Solution

Transform IMPs into **dual-audience documents**:
- **Part I (User Completion Guide):** For assessment users - practical, step-by-step instructions **(COMES FIRST)**
- **Part II (Technical Specification):** For workbook developers - existing technical content from project files

**Key Decision:** User Guide comes FIRST because users are the primary audience. Technical specs are secondary/reference material.

**Output:** ONE combined document containing both parts with standardized Document Control section.

---

## Critical Prerequisites

### ALWAYS Use Project Documentation

**⚠️ CRITICAL:** All source materials exist in `/mnt/project/`. Do NOT recreate from memory or assumptions.

**Before starting ANY IMP update:**

```bash
# Step 1: List all files for the control
ls -la /mnt/project/ | grep "A_X_XX"

# Step 2: Verify you have the complete set
# Required files:
# - ISMS-IMP-A_X_XX_N_*.md (technical specs)
# - generate_aXXX_N_*.py (Python scripts)
# - ISMS-POL-A_X_XX*.md (policy documents)
```

**If ANY file is missing → STOP. Request missing files before proceeding.**

### Check for Script Updates

**⚠️ CRITICAL:** Python scripts may have been updated after original IMP was written.

**Validation process:**

1. **Open the Python script** (`generate_aXXX_N_[function].py`)
2. **Open the existing IMP** (ISMS-IMP-A_X_XX_N)
3. **Compare line-by-line:**
   - Sheet names (script line ~100-200)
   - Column/field names (script line ~300-500)
   - Dropdown options (script line ~400-600)
   - Validation rules (script line ~500-700)

4. **Document discrepancies** in a checklist:
   ```
   [ ] Sheet "XYZ" added in script, missing in IMP
   [ ] Field "ABC" renamed from "DEF" in script
   [ ] Dropdown option "GHI" added in script
   ```

5. **Update Part II (Technical Spec) FIRST** to match script
6. **Then create Part I (User Guide)** matching corrected spec

**If you skip this step, the User Guide will be wrong.**

---

## Document Structure Pattern

**MANDATORY structure for all IMPs:**

```markdown
# ISMS-IMP-A.X.XX - [Control Name] - [Assessment Area]

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.X.XX |
| **Version** | 1.0 |
| **Assessment Area** | [Specific aspect being assessed] |
| **Related Policy** | ISMS-POL-A.X.XX-SX.X ([Policy Section Names]) |
| **Purpose** | [One-sentence purpose of this assessment] |
| **Target Audience** | Security Engineers, [Other Roles], Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification | ISMS Implementation Team |

---

## PART I: USER COMPLETION GUIDE
**Audience:** [Roles who complete this assessment]

### 1. Assessment Overview
### 2. Prerequisites  
### 3. Assessment Workflow
### 4. Question-by-Question Guidance
### 5. Evidence Collection
### 6. Common Pitfalls
### 7. Quality Checklist
### 8. Review & Approval

---

## PART II: TECHNICAL SPECIFICATION
**Audience:** Workbook developers, Python script maintainers

**Note:** This section provides technical specifications for workbook generation and maintenance.  
Users completing the assessment should refer to Part I above.

[All technical content from existing IMP in /mnt/project/ - sheet structures, formulas, etc.]
```

**⚠️ CRITICAL STRUCTURE NOTES:**
- Document Control table comes FIRST with standardized format
- Version History shows evolution from v1.0 (technical spec only) to v2.0 (added User Guide)
- USER GUIDE (PART I) comes before Technical Spec (PART II)
- This creates ONE combined document with both audiences served

---

## Step-by-Step Creation Process

### STEP 1: Gather All Source Materials

**Run this command:**
```bash
cd /mnt/project
ls -la | grep "A_X_XX"  # Replace X_XX with actual control number
```

**Verify you have:**
- [ ] `ISMS-IMP-A_X_XX_N_*.md` - Existing technical specification(s)
- [ ] `generate_aXXX_N_*.py` - Workbook generation script(s)
- [ ] `ISMS-POL-A_X_XX.md` or policy sections - Policy requirements

**Read ALL files completely before proceeding.**

---

### STEP 2: Analyze Assessment Structure from Script

**Open:** `generate_aXXX_N_[function].py`

**Extract:**

1. **Sheet names** (look for `ws = wb.create_sheet(title="...")`)
   - List all sheets
   - Note which are templates vs single-instance

2. **Field/column names** (look for column definitions around line 200-400)
   - Extract exact field names (these go in User Guide)
   - Note data types (text, number, dropdown, date)
   - Note if required or optional

3. **Dropdown options** (look for data validation definitions around line 400-600)
   - List all dropdown menus
   - Extract exact option text
   - Note what each option means

4. **Evidence expectations** (look for Evidence/Attachments sheets)
   - What evidence is expected
   - How evidence is referenced

5. **Compliance logic** (look for calculation/scoring sections around line 700-900)
   - How compliance is calculated
   - What triggers gaps/findings

**Create a working document:**
```markdown
## Script Analysis - Control A.X.XX Assessment N

**Sheets:**
1. Sheet1: Instructions
2. Sheet2: [Main assessment]
3. Sheet3: [Evidence register]
...

**Key Fields (Sheet2):**
- Field1: [Type: Text, Required: Yes]
- Field2: [Type: Dropdown, Options: A/B/C, Required: Yes]
...

**Dropdowns:**
- Status: Deployed / Partial / Not Deployed / Planned / N/A
- Risk Level: Critical / High / Medium / Low
...

**Evidence Types:**
- Configuration exports
- Screenshots
- Documentation
...
```

---

### STEP 3: Read Existing Technical Spec from Project Files

**Open:** `ISMS-IMP-A_X_XX_N_*.md` from `/mnt/project/` (existing IMP)

**This will become Part II of your combined document.**

**Compare to script analysis:**
- [ ] Do sheet names match?
- [ ] Do field names match?
- [ ] Do dropdown options match?
- [ ] Do validation rules match?

**If NO → Update Part II (Technical Spec) to match script BEFORE creating User Guide.**

**Extract from Technical Spec:**
- Acceptable evidence examples
- Status legend meanings
- Any special instructions

**Note:** You will copy this entire technical specification into Part II of the new combined document.

---

### STEP 4: Understand Policy Requirements

**Open:** `ISMS-POL-A_X_XX.md` (shrunk policy)

**Extract:**
1. **Control objective** (Section 1.1) - What ISO requires
2. **Policy requirements** (Section 2.x) - What [Organization] mandates  
3. **Assessment reference** (Section 3.2 or similar) - How this assessment fits

**Use this to write:**
- Assessment Overview ("Why this matters")
- Quality Checklist (alignment with policy)
- Document Control table (Related Policy field)

---

### STEP 5: Create Document Control Section

**Template:**

```markdown
# ISMS-IMP-A.X.XX - [Control Name] - [Assessment Area]

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.X.XX |
| **Version** | 1.0 |
| **Assessment Area** | [Specific aspect - e.g., "Web Filtering Infrastructure & Technology Capabilities"] |
| **Related Policy** | ISMS-POL-A.X.XX-SX.X ([Policy Title]), ISMS-POL-A.X.XX-SX.X ([Other Policy Title if applicable]) |
| **Purpose** | [One clear sentence describing assessment purpose] |
| **Target Audience** | Security Engineers, [Role 1], [Role 2], Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original Date] | Initial technical specification | ISMS Implementation Team |

```

**Key fields to populate:**

- **Document ID:** Format is ISMS-IMP-A.X.XX (use actual control number)
- **Assessment Area:** Specific focus of this IMP (from policy or control scope)
- **Related Policy:** Reference all relevant policy sections (format: ISMS-POL-A.X.XX-SX.X)
- **Purpose:** Clear, single-sentence objective
- **Target Audience:** List all roles who use this assessment
- **Review Cycle:** Typically "Quarterly or After Major Infrastructure Changes"

---

### STEP 6: Write Part I - User Completion Guide

**Use templates below for each section. Adjust length based on assessment complexity:**

- Simple assessment (1-2 sheets): ~200-250 lines total
- Moderate assessment (3-5 sheets): ~250-350 lines total
- Complex assessment (6+ sheets): ~350-500 lines total

---

#### Section 1: Assessment Overview

**Template:**
```markdown
### 1. Assessment Overview

**What This Assessment Evaluates:**
[2-3 sentences explaining WHAT is being assessed - not HOW to do it]

**Why This Matters:**
This assessment verifies [Organization]'s compliance with:
- **ISO/IEC 27001:2022 Control A.X.XX:** [Control name and brief requirement]
- **[Organization] Policy:** ISMS-POL-A.X.XX Section X.X ([Requirement name])

**Assessment Scope:**
- [What's included]
- [What's included]
- [What's NOT included - if relevant]

**Completion Time:** [Estimated hours]  
**Frequency:** [How often this must be done]  
**Dependencies:** [Prerequisites or required access]
```

**Length:** 20-30 lines

**Content guidance:**
- Focus on "why this matters" - connect to business risk
- Be specific about scope (what's in, what's out)
- Set realistic time expectations
- List any required access/permissions upfront

---

#### Section 2: Prerequisites

**Template:**
```markdown
### 2. Prerequisites

**Before starting this assessment, ensure you have:**

**Access Requirements:**
- [ ] [System/tool] administrator access or read-only access
- [ ] [Dashboard/console] login credentials
- [ ] [Configuration repository] access

**Information You'll Need:**
- [ ] [Document/artifact 1] (Location: [where to find it])
- [ ] [Document/artifact 2] (Location: [where to find it])
- [ ] [Contact info] for [role] (for verification questions)

**Technical Knowledge:**
- Basic understanding of [technology/concept]
- Familiarity with [tool/system] interface
- Ability to [specific task - e.g., "export configuration files"]

**Estimated Preparation Time:** [X] hours
```

**Length:** 15-25 lines

**Content guidance:**
- Be very specific about required access levels
- Provide exact locations where information can be found
- Don't assume technical knowledge - state what's needed
- Include prep time so users can plan accordingly

---

#### Section 3: Assessment Workflow

**Template:**
```markdown
### 3. Assessment Workflow

**Step-by-step process:**

**Phase 1: Preparation (Est. [X] hours)**
1. Review this User Guide completely
2. Verify you have all prerequisites (Section 2)
3. Schedule time with [stakeholder] if needed
4. Open the assessment workbook

**Phase 2: Data Collection (Est. [X] hours)**
1. Complete Sheet: [Sheet Name]
   - Focus: [What this sheet captures]
   - Source: [Where to get the data]
   - Time: ~[X] minutes

2. Complete Sheet: [Sheet Name]
   - Focus: [What this sheet captures]
   - Source: [Where to get the data]
   - Time: ~[X] minutes

[Continue for each major sheet]

**Phase 3: Evidence Gathering (Est. [X] hours)**
1. Collect required evidence per Evidence Register
2. Name files using convention: [naming pattern]
3. Store in: [location]

**Phase 4: Quality Check (Est. [X] minutes)**
1. Run through Quality Checklist (Section 7)
2. Verify all required fields completed
3. Check evidence attachments

**Phase 5: Review & Submission (Est. [X] minutes)**
1. Submit to [reviewer role]
2. Address any feedback
3. Final approval by [approver role]

**Total Estimated Time:** [X] hours

**Parallel Work:** [Any tasks that can be done simultaneously]
```

**Length:** 30-50 lines

**Content guidance:**
- Break into logical phases
- Provide time estimates for each phase and step
- Specify WHO needs to be involved at each stage
- Note any tasks that can be parallelized
- Be realistic about total time

---

#### Section 4: Question-by-Question Guidance

**This is the LONGEST section - 50-70% of your User Guide.**

**Template for EACH question/field:**

```markdown
#### 4.X [Field Name]

**What We're Asking:**
[Plain English explanation of what this field is asking for]

**How to Answer:**
[Step-by-step instructions to find and provide the answer]

**Where to Find This Information:**
- **Option 1:** [Primary source with exact location]
  - Navigate to: [exact path]
  - Look for: [specific field/section]
  - Example value: `[actual example]`

- **Option 2:** [Alternative source]
  - [Instructions]

- **Option 3:** [Fallback if neither available]
  - [Instructions]

**Acceptable Answers:**
- `[Option 1]` - [What this means]
- `[Option 2]` - [What this means]
- `[Option 3]` - [What this means]
- `N/A` - Only if [specific condition]

**Examples:**

**Good Example:**
```
[Field]: [Actual realistic value]
[Explanation of why this is good]
```

**Poor Example:**
```
[Field]: [Common mistake value]
[Explanation of why this is wrong and how to fix it]
```

**Common Mistakes:**

1. **Mistake:** [Common error users make]
   - **Solution:** [How to avoid/fix it]

2. **Mistake:** [Another common error]
   - **Solution:** [How to avoid/fix it]

**Related Questions:**
- [Other field name] should align with this answer
- If you answered [X], make sure [related field] is [Y]

**Evidence Required:**
- [Type of evidence expected for this field]
- Naming convention: `[file naming pattern]`
- Example: `[actual example filename]`

**Policy Reference:**
- ISMS-POL-A.X.XX Section X.X: "[Quote relevant policy requirement]"

**Audit Verification:**
[What the auditor will check to verify this answer]
```

**Length per question:** 30-50 lines for complex questions, 15-20 for simple ones

**CRITICAL GUIDANCE:**

**Be EXTREMELY specific about "Where to Find This Information":**
- Don't say "Check your system" - say "Open Fortigate GUI → System → Status → Dashboard → Firmware Version"
- Don't say "Review documentation" - say "Open SharePoint → Security Docs → Web Filtering folder → Deployment_Guide.docx → Section 3.2"
- Provide actual CLI commands if relevant: `show system interface` not "run system commands"
- Include screenshots or ASCII diagrams if navigation is complex

**Provide REAL examples:**
- Use actual format: `fw-dmz-01.company.local` not `[Firewall Name]`
- Show realistic values: `FortiGate 200F v7.2.4` not `[Product Version]`
- Include edge cases: "If your firmware is older than 7.0, you'll find this under..."

**Address common mistakes proactively:**
- Think through what users will do wrong
- Explain WHY something is wrong, not just that it is
- Provide concrete solutions

**Link to policy requirements:**
- Quote exact policy text when relevant
- Explain how this field demonstrates compliance
- Connect to business risk/impact

---

#### Section 5: Evidence Collection

**Template:**
```markdown
### 5. Evidence Collection

**Evidence Register Sheet:**
All evidence must be documented in the "[Evidence Register]" sheet with:
- Evidence ID (auto-generated)
- Evidence Type
- File Name
- Description
- Collection Date
- Collected By

**Required Evidence Types:**

**1. [Evidence Type 1]**
- **Purpose:** [Why this evidence is needed]
- **Format:** [File format - e.g., PDF, CSV, Screenshot]
- **Source:** [Where to obtain this]
- **How to Collect:**
  1. [Step-by-step instructions]
  2. [Continue]
  3. [Continue]
- **Naming Convention:** `[pattern]`
- **Example:** `web-filter-config-export-20260115.xml`
- **Quality Check:** Ensure [specific requirements]

**2. [Evidence Type 2]**
[Same structure]

**3. [Evidence Type 3]**
[Same structure]

**Evidence Storage:**
- **Location:** [Where evidence files are stored]
- **Access:** [Who can access]
- **Retention:** [How long evidence is kept]

**File Naming Convention:**

All evidence files must follow this pattern:
```
[prefix]-[description]-[date].{ext}

Examples:
- web-filter-policy-export-20260115.pdf
- fortigate-screenshot-categories-20260115.png
- deployment-guide-v2.3-20260115.pdf
```

**Evidence Quality Checklist:**
- [ ] File name follows naming convention
- [ ] File is readable/not corrupted
- [ ] File contains required information
- [ ] Sensitive data redacted (if applicable)
- [ ] Date clearly visible in file or filename
- [ ] Evidence matches description in register

**Special Considerations:**

**Sensitive Data:**
- Redact: [list what to redact - IPs, passwords, personal info]
- Keep: [what to keep visible]
- Tool: Use [preferred redaction tool]

**Screenshots:**
- Resolution: Minimum 1920x1080 for readability
- Format: PNG preferred (JPEG acceptable)
- Content: Include full context (entire dialog, not just field)
- Date: System date/time must be visible

**Configuration Exports:**
- Format: [Expected format]
- Completeness: Full configuration, not partial
- Validation: [How to verify export is complete]
```

**Length:** 40-60 lines

**Content guidance:**
- Provide exact naming patterns with real examples
- Include quality checks for each evidence type
- Specify redaction requirements clearly
- Address format/technical requirements (resolution, file types, etc.)

---

#### Section 6: Common Pitfalls

**Template:**
```markdown
### 6. Common Pitfalls

**Avoid these frequent mistakes:**

**1. [Common Pitfall Category]**

**Problem:** [Description of what users often do wrong]

**Why It's Wrong:** [Explanation of the issue]

**How to Avoid:**
- [Specific action 1]
- [Specific action 2]
- [Specific action 3]

**Example:**
- **Wrong:** [Actual bad example]
- **Right:** [Corrected example]

---

**2. [Common Pitfall Category]**

[Same structure]

---

**3. [Common Pitfall Category]**

[Same structure]

---

**Quick Checklist - Before Submission:**

- [ ] [Critical check 1]
- [ ] [Critical check 2]
- [ ] [Critical check 3]
- [ ] [Critical check 4]
- [ ] [Critical check 5]

**If Any Check Fails:** [What to do]
```

**Length:** 30-40 lines

**Content guidance:**
- Focus on mistakes you've seen or can anticipate
- Explain WHY something is wrong, not just that it is
- Provide clear before/after examples
- Keep "Quick Checklist" to 5-7 most critical items

**Common pitfall categories to consider:**
- Misunderstanding the question
- Wrong evidence type
- Incomplete information
- Technical errors (wrong export format, etc.)
- Policy misalignment
- Missing required fields

---

#### Section 7: Quality Checklist

**Template:**
```markdown
### 7. Quality Checklist

**Before submitting your assessment, verify:**

**Completeness:**
- [ ] All required sheets completed
- [ ] No empty required fields
- [ ] All dropdowns selected (no blanks)
- [ ] Comments provided where marked "Required"
- [ ] Evidence register fully populated

**Accuracy:**
- [ ] All vendor/product names spelled correctly
- [ ] All version numbers match actual deployed versions
- [ ] All dates in correct format (DD.MM.YYYY)
- [ ] Status values reflect CURRENT state
- [ ] Numerical values are realistic (no placeholder "999")

**Evidence Quality:**
- [ ] All required evidence collected
- [ ] File names follow naming convention
- [ ] Files are readable and not corrupted
- [ ] Screenshots show full context and date
- [ ] Configuration exports are complete
- [ ] Sensitive data properly redacted
- [ ] Evidence descriptions match actual content

**Policy Alignment:**
- [ ] Answers align with ISMS-POL-A.X.XX Section X.X
- [ ] Gaps identified match policy requirements
- [ ] Remediation plans address policy mandates
- [ ] Risk ratings follow policy risk framework

**Technical Accuracy:**
- [ ] Technical terms used correctly
- [ ] Architecture diagrams match actual deployment
- [ ] Configuration details verified against live systems
- [ ] Integration points documented accurately

**Internal Consistency:**
- [ ] Related answers don't contradict each other
- [ ] Totals/calculations are correct
- [ ] Status in summary matches detailed assessment
- [ ] Evidence references point to actual evidence items

**Presentation:**
- [ ] No spelling/grammar errors in comments
- [ ] Professional tone maintained
- [ ] Clear and concise descriptions
- [ ] Abbreviations defined on first use

**Metadata:**
- [ ] Assessor name/contact filled in
- [ ] Assessment date is current
- [ ] Review date scheduled
- [ ] Approver identified

**If ANY item fails this checklist:**
1. Return to relevant section of this guide
2. Make corrections
3. Re-run this checklist
4. Do NOT submit until all items checked
```

**Length:** 40-50 lines

**Content guidance:**
- Organize by category (Completeness, Accuracy, Evidence, etc.)
- Make items specific and verifiable (not vague like "is good")
- Cover all aspects of quality
- Provide clear action if checklist fails

---

#### Section 8: Review & Approval

**Template:**
```markdown
### 8. Review & Approval

**Review Process:**

**Step 1: Self-Review**
- Complete Quality Checklist (Section 7)
- Allow 24 hours between completion and self-review (fresh eyes)
- Make corrections as needed

**Step 2: Peer Review (Optional but Recommended)**
- **Who:** Another [role with similar knowledge]
- **Focus:** Technical accuracy and evidence quality
- **Timeline:** 2-3 business days
- **Outcome:** Feedback document or inline comments

**Step 3: Security Team Review**
- **Reviewer:** [Specific role/person]
- **Contact:** [Email/Teams]
- **Submission:** Via [method/location]
- **Review Focus:**
  - Policy compliance
  - Evidence completeness
  - Risk identification
  - Remediation priorities
- **Timeline:** 5 business days
- **Possible Outcomes:**
  - **Approved:** Proceed to final approval
  - **Minor Revisions:** Address comments and resubmit
  - **Major Revisions:** Schedule meeting to discuss gaps

**Step 4: Final Approval**
- **Approver:** [Specific role - e.g., CISO, Security Manager]
- **Approval Criteria:**
  - Security Team review passed
  - All evidence attached and verified
  - Gaps identified with mitigation plans
  - Policy requirements met
- **Timeline:** 2-3 business days after Security Team approval
- **Documentation:** Approval logged in [system/location]

**Step 5: Archive & Schedule Next Assessment**
- Final approved version stored in: [location]
- Next assessment scheduled for: [frequency]
- Calendar reminder set for: [date]

**Common Review Feedback (and how to address it):**

**"Evidence is insufficient"**
- Review Section 5 (Evidence Collection)
- Verify each evidence item meets quality standards
- Add missing evidence types
- Resubmit

**"Technical details unclear"**
- Review Section 4 for that specific field
- Add clarifying comments
- Provide additional context
- Consider adding diagram/screenshot

**"Policy alignment not demonstrated"**
- Review relevant ISMS-POL-A.X.XX sections
- Explicitly state how answer meets policy
- Update risk identification if needed

**"Gaps not properly prioritized"**
- Review policy risk framework
- Reassess business impact
- Update remediation timeline
- Consult with [stakeholder] if unsure

**Escalation Path:**

If you disagree with review feedback or need clarification:
1. Schedule meeting with reviewer
2. Bring specific questions and references to this guide
3. Document agreed resolution
4. Update assessment accordingly

**Do NOT:**
- Bypass review process
- Submit without self-review
- Ignore feedback without discussion
- Make undocumented changes after approval
```

**Length:** 50-60 lines

**Content guidance:**
- Provide exact contacts and timelines
- Explain what each reviewer looks for
- Give concrete examples of common feedback
- Provide escalation path for disagreements
- Set expectations for timeline and outcomes

---

### STEP 7: Integrate Part II - Technical Specification

**Now add the technical specification from the existing IMP in `/mnt/project/`**

```markdown
---

## PART II: TECHNICAL SPECIFICATION
**Audience:** Workbook developers, Python script maintainers

**Note:** This section provides technical specifications for workbook generation and maintenance.  
Users completing the assessment should refer to Part I above.

[Copy the ENTIRE technical specification from the existing ISMS-IMP-A_X_XX_N_*.md file]
[This includes all sheets, columns, formulas, validation rules, etc.]
[Make sure it's updated to match the Python script if there were changes]
```

**Key points:**
- Copy ALL technical content from existing IMP
- Ensure it matches the current Python script (from your STEP 3 verification)
- Keep all formatting, tables, code blocks
- This is primarily for developers/maintainers, not assessment users

---

### STEP 8: Fix Markdown Formatting

**⚠️ CRITICAL FINAL STEP:** After creating the combined document, markdown formatting must be fixed for proper Pandoc/Word conversion.

**Process:**

1. **Save your completed IMP document** to your ISMS documentation directory

2. **Run the markdown fixer script:**

```bash
# Preview changes (dry-run mode)
python3 fix_isms_markdown.py /path/to/isms/docs --dry-run

# Apply fixes with automatic backup
python3 fix_isms_markdown.py /path/to/isms/docs

# Or process single file
python3 fix_isms_markdown.py /path/to/isms/docs/ISMS-IMP-A.X.XX.md
```

3. **What the script fixes:**
   - Title/subtitle converted to bold text (not headers)
   - Metadata sections (Document Control, Version History) as bold
   - Content headers demoted one level for proper Pandoc numbering
   - Manual numbering removed from headers
   - Proper blank lines before/after lists

4. **Verify the fixes:**
   - Open the fixed markdown file
   - Check Document Control table is intact
   - Verify Part I and Part II sections are properly formatted
   - Confirm headers are at correct levels

5. **Convert to Word:**

```bash
pandoc ISMS-IMP-A.X.XX.md \
    --from markdown+pipe_tables+grid_tables \
    --to docx \
    --number-sections \
    --reference-doc=bithawk-isms-reference.docx \
    --output ISMS-IMP-A.X.XX.docx
```

**Why This Matters:**
- Ensures consistent header levels throughout document
- Enables Pandoc to properly auto-number sections
- Creates professional Word documents with correct formatting
- Maintains proper hierarchy between Part I and Part II
- Fixes common markdown formatting issues that break Word conversion

**Backup Note:**
The script automatically creates timestamped backups (e.g., `ISMS-IMP-A.X.XX.20260115_143022.bak`) before making changes, but you should also maintain your own git repository or manual backups of the ISMS documentation.

---

## Section Length Guidelines

**Total Document Length (Including Both Parts):**

- **Simple Assessment:** 400-600 lines
  - Part I (User Guide): 200-250 lines
  - Part II (Technical Spec): 200-350 lines

- **Moderate Assessment:** 600-900 lines
  - Part I (User Guide): 250-350 lines
  - Part II (Technical Spec): 350-550 lines

- **Complex Assessment:** 900-1500 lines
  - Part I (User Guide): 350-500 lines
  - Part II (Technical Spec): 550-1000 lines

**Part I Section Breakdown:**

| Section | Lines | Notes |
|---------|-------|-------|
| Document Control | 20-25 | Standardized table |
| 1. Assessment Overview | 20-30 | Context and purpose |
| 2. Prerequisites | 15-25 | Access and prep |
| 3. Assessment Workflow | 30-50 | Step-by-step process |
| 4. Question Guidance | 100-300 | 50-70% of User Guide |
| 5. Evidence Collection | 40-60 | Detailed evidence specs |
| 6. Common Pitfalls | 30-40 | Proactive problem-solving |
| 7. Quality Checklist | 40-50 | Pre-submission verification |
| 8. Review & Approval | 50-60 | Process and escalation |

**Quality over brevity:** Better to be thorough than brief. Users appreciate detailed guidance.

---

## Question-by-Question Guidance - Detailed Example

**Here's a FULL example for one complex field to illustrate the level of detail needed:**

```markdown
#### 4.3 Vendor/Manufacturer Name

**What We're Asking:**
The company that manufactures or develops the web filtering solution you're assessing. This is NOT the reseller or value-added reseller (VAR) who sold it to you.

**How to Answer:**
1. Identify the actual product manufacturer:
   - Look at the product login screen
   - Check the product documentation cover page
   - Review your software license agreement
   - Check the "About" section in the product interface

2. Use the official company name:
   - Use the name as it appears on the manufacturer's website
   - Include "Inc.", "Ltd.", "AG", etc. if that's how they brand
   - Do NOT use product name here (that goes in next field)

3. Common formats:
   - Single word: Fortinet, Cisco, Palo Alto Networks
   - With suffix: Zscaler, Inc. or Infoblox Inc.
   - With geographic: Sophos Ltd., Check Point Software Technologies Ltd.

**Where to Find This Information:**

**Option 1: Product Interface**
- Log into the web filtering solution
- Navigate to: `Help → About` or `System → About`
- Look for: "Manufacturer", "Vendor", or copyright notice
- Example: "© 2025 Fortinet, Inc. All rights reserved."

**Option 2: Product Documentation**
- Open the product's admin guide or installation guide
- Check the cover page or first page
- Look for the publisher/copyright information
- Example: Cover shows "Fortinet FortiGate Administration Guide"

**Option 3: Licensing Portal**
- Log into your software licensing portal (where you activated the product)
- Check the vendor/manufacturer field
- This is usually accurate as it's tied to billing

**Option 4: Purchase Order / Invoice**
- Review your original purchase documentation
- Look for "Manufacturer" field (NOT "Sold By")
- WARNING: This may show the reseller, not the manufacturer
  - If you bought from a VAR/reseller, keep looking for actual manufacturer

**Acceptable Answers:**

- `Fortinet` - Manufacturer of FortiGate products ✅
- `Palo Alto Networks` - Manufacturer of Prisma Access, etc. ✅
- `Zscaler` - Manufacturer of Zscaler Internet Access ✅
- `Cisco Systems` - Manufacturer of Umbrella, WSA, etc. ✅
- `Sophos` - Manufacturer of Sophos Firewall, XG Firewall ✅
- `WatchGuard` - Manufacturer of Firebox appliances ✅

**Examples:**

**Good Example:**
```
Vendor/Manufacturer: Fortinet
Product/Service Name: FortiGate 200F
```
**Explanation:** Clear manufacturer name, matches actual maker of FortiGate products.

**Poor Example:**
```
Vendor/Manufacturer: Winet AG
Product/Service Name: FortiGate 200F
```
**Problem:** "Winet AG" is the Swiss reseller who sold the FortiGate, not the manufacturer.  
**Fix:** Change vendor to "Fortinet" (actual manufacturer of FortiGate).

**Poor Example:**
```
Vendor/Manufacturer: FortiGate
Product/Service Name: Fortinet 200F
```
**Problem:** Vendor and product are swapped. FortiGate is the product line, not the manufacturer.  
**Fix:** Vendor: "Fortinet", Product: "FortiGate 200F"

**Common Mistakes:**

1. **Mistake:** Listing the reseller/VAR instead of manufacturer
   - **How this happens:** You check your invoice and see "Winet AG" or "Bechtle AG"
   - **Why it's wrong:** These are resellers, not manufacturers
   - **Solution:** Check product documentation for actual manufacturer, not who sold it to you

2. **Mistake:** Confusing vendor with product (entering "FortiGate" instead of "Fortinet")
   - **Why it's wrong:** Vendor makes multiple products. We need the company name, not product name.
   - **Solution:** Vendor is the company (Fortinet), Product is what they make (FortiGate 200F)

3. **Mistake:** Using abbreviations or nicknames
   - **Example:** "PA Networks" instead of "Palo Alto Networks"
   - **Solution:** Use full official name as shown on vendor's website

4. **Mistake:** Including product category in vendor name
   - **Example:** "Fortinet Web Filters" instead of "Fortinet"
   - **Solution:** Vendor is just the company name. Product category is implicit.

**Related Questions:**
- **Product/Service Name** (next field) should be a product made by this vendor
  - If vendor is "Fortinet", product should be "FortiGate XXX" or similar
  - If these don't match, one is wrong
- **If you have multiple vendors:** Complete separate rows/sheets for each vendor

**Evidence Required:**
- Screenshot of product "About" page showing manufacturer name
- Naming convention: `web-filter-about-screen-[vendor]-20260115.png`
- Example: `web-filter-about-screen-fortinet-20260115.png`

**Policy Reference:**
- ISMS-POL-A.8.23 Section 2.1: "Organizations SHALL document deployed web filtering solutions including manufacturer/vendor information"
- This enables vendor risk assessment and supply chain management

**Audit Verification:**
Auditor will verify:
1. Vendor name matches evidence (About screen, documentation)
2. Vendor is the actual manufacturer, not reseller
3. Vendor is a legitimate manufacturer of security products (not a typo or fake)
4. Vendor matches product listed (internal consistency check)

**Tips:**
- When in doubt, check the manufacturer's official website
- The company that hosts the product documentation is usually the manufacturer
- For cloud services, the manufacturer is who runs the cloud service (e.g., Zscaler for ZIA)
- If you have both on-premise and cloud from same vendor, list vendor once with both products
```

**Why this example is comprehensive:**
- Crystal clear "What We're Asking"
- Multiple specific "Where to Find" options with exact navigation paths
- Real-world good and bad examples with explanations
- Addresses 4 common mistakes with solutions
- Links to related questions for consistency
- Specific evidence requirements with naming examples
- Policy context and audit verification criteria
- Practical tips at the end

**This is the level of detail needed for complex/critical fields.**

---

## Control-Specific Adaptations

Different control types need different emphasis:

### Technical Controls (A.8.x)
- Heavy emphasis on "where to find" (config files, dashboards, CLI commands)
- Include command-line examples where relevant
- Show actual system output examples
- Technical accuracy critical

### Organizational Controls (A.5.x)
- Emphasize documentation review
- Include interview guidance (how to verify with stakeholders)
- Focus on policy/procedure evidence
- Process verification important

### Physical Controls (A.7.x)
- Include site visit checklists
- Emphasize photo evidence
- Specify what constitutes acceptable physical evidence
- Safety considerations

### People Controls (A.6.x)
- Include HR documentation guidance
- Emphasize privacy and confidentiality
- Specify anonymization requirements for personnel data
- Compliance with labor laws

---

## Special Situations

### When Script Has Changed Since Original IMP

**CRITICAL:** Always check for script updates before creating User Guide.

**Process:**
1. Compare script to existing IMP (Part II)
2. Document all differences
3. Update Part II FIRST to match script
4. Then write Part I based on corrected Part II

**Common changes to look for:**
- New sheets added
- Fields renamed
- Dropdown options changed
- New validation rules
- Changed formulas
- New evidence requirements

**Update Version History:**
```markdown
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial technical specification |

```

---

### When Assessment is Complex (10+ Sheets)

For very complex assessments:

**Part I Strategy:**
- Keep Overview, Prerequisites, Workflow, Pitfalls, Checklist, Approval (standard length)
- Section 4 (Question Guidance) will be longest
- Consider grouping related questions
- Use sub-headers extensively for navigation

**Length management:**
- OK to have 500-600 line User Guide for complex assessment
- Don't sacrifice completeness for brevity
- But don't pad either - be concise within completeness

**Navigation aids:**
- Add mini table of contents for Section 4
- Use consistent formatting so users can scan
- Consider adding "Quick Start" subsection for experienced users

---

### When Creating German (DE) Versions

**Part I (User Guide):**
- Translate to German (Swiss conventions)
- Technical terms stay in English (follow A.8.24-DE pattern)
- Evidence naming stays in English
- Screenshots may need German UI

**Part II (Technical Spec):**
- Keep in English (technical/developer audience)
- Python scripts are English, specs should match

**Terminology:**
- Richtlinie = Policy
- Bewertung = Assessment  
- Nachweis = Evidence
- Anforderung = Requirement
- See A.8.24-DE for full terminology guide

---

## Success Metrics

**A well-written User Guide enables:**

1. **Autonomous Completion:** User completes assessment WITHOUT asking for help
2. **Consistent Results:** Different users produce similar quality assessments  
3. **Audit Readiness:** Evidence collected meets auditor requirements on first submission
4. **Time Efficiency:** Assessment completed within estimated timeline (±20%)
5. **Quality Assurance:** Self-check catches 90%+ of errors before review

**Signs of success:**
- Users say "The instructions were very clear"
- Internal reviews require minimal corrections
- Auditors accept evidence without questions
- Assessment completion time matches estimate
- Users complete assessment independently

**Red flags (indicates poor User Guide):**
- Users frequently ask "Where do I find this?"
- Assessments come back with wrong evidence type
- Internal reviews identify same mistakes across multiple assessors
- Users say "I wasn't sure what you wanted"
- Assessment takes 2-3x longer than estimated
- Fields completed incorrectly (misunderstanding question)

---

## Critical Reminders

### ALWAYS Use Project Documentation

⚠️ **THIS IS NOT OPTIONAL**

**Before touching ANY IMP:**
```bash
cd /mnt/project
ls -la | grep "A_X_XX"
```

**Verify you have:**
- The technical spec (ISMS-IMP-A_X_XX_N_*.md)
- The Python script (generate_aXXX_N_*.py)
- The policy (ISMS-POL-A_X_XX*.md)

**Read ALL files completely.**

Do NOT:
- Recreate from memory
- Assume structure
- Copy from similar control without verification
- Skip checking for script updates

---

### Script Changes MUST Be Reflected

**Before creating User Guide:**

1. **Compare script to existing IMP Part II**
2. **Document ALL differences**
3. **Update Part II to match script**
4. **Then write Part I based on corrected Part II**

**If you skip this:** User Guide will have wrong field names, wrong options, wrong evidence requirements. Assessment will be unusable.

---

### User Guide Comes FIRST in Combined Document

**Document structure:**
1. Document Control (table format)
2. **PART I: USER COMPLETION GUIDE** ← Comes first
3. PART II: TECHNICAL SPECIFICATION (from `/mnt/project/`) ← Comes second

**Rationale:**
- 95% of readers want the User Guide
- 5% of readers want the Technical Spec
- Primary audience first

**Output:** ONE document with both parts integrated

---

### Fix Markdown Before Final Conversion

**Final processing steps:**

1. Complete combined IMP document (Parts I & II)
2. **Run markdown fixer:** `python3 fix_isms_markdown.py /path/to/isms/docs`
3. Verify fixes were applied correctly
4. Convert to Word with Pandoc
5. Review Word document for proper formatting

**Do NOT skip the markdown fixing step** - it ensures:
- Proper header levels for Pandoc auto-numbering
- Clean Document Control table formatting
- Professional Word document output
- Consistent formatting across all IMPs

---

### Quality Over Speed

**Better to:**
- Spend extra hour making guidance crystal clear
- Provide 3 examples instead of 1
- Explain every dropdown option thoroughly
- Include detailed "where to find" instructions

**Than to:**
- Rush and leave gaps
- Provide vague "check your system" instructions
- Skip examples
- Assume user knowledge

**One well-written User Guide saves:**
- Hours of user confusion
- Multiple assessment rejections
- Audit findings from poor evidence
- Your time answering the same questions repeatedly

---

## Document Control

**This Instruction Document:**
- **ID:** IMP-USER-GUIDE-INSTRUCTIONS
- **Version:** 1.0
- **Date:** [Date]
- **Author:** ISMS Implementation Team
- **Purpose:** Standardized methodology for adding User Completion Guides to ISMS-IMP assessment specifications
- **Scope:** All 45 ISO 27001:2022 Annex A controls with assessment workbooks
- **Review Cycle:** After every 5 IMP updates (refine based on experience)

**Version History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISMS Implementation Team | Initial instruction document for IMP User Guide creation process |

---

**END OF INSTRUCTION DOCUMENT**

---

## Quick Start Checklist (For Your Reference)

When starting a new IMP update, use this checklist:

- [ ] Identify control number (A.X.XX)
- [ ] Run: `ls -la /mnt/project/ | grep "A_X_XX"`
- [ ] Open and read all project files for this control
- [ ] Compare Python script to existing IMP - note differences
- [ ] Update Part II (Technical Spec) if script changed
- [ ] Create Document Control section with standardized table
- [ ] Write Part I (User Guide) using templates in this document
- [ ] Integrate Part II (Technical Spec from project files)
- [ ] Run markdown fixer script on completed document
- [ ] Quality check: Verify formatting and structure
- [ ] Convert to Word and review
- [ ] Update version to 2.0 in Document Control table
- [ ] Submit for review