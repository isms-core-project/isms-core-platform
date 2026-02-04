**ISMS-IMP-A.8.24.5 - Compliance Summary Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography

---

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.24.5 |
| **Version** | 1.0 |
| **Assessment Area** | Cryptography Compliance Summary Dashboard |
| **Related Policy** | ISMS-POL-A.8.24 (Use of Cryptography) |
| **Related Assessments** | ISMS-IMP-A.8.24.1 (Transmission), ISMS-IMP-A.8.24.2 (Storage), ISMS-IMP-A.8.24.3 (Authentication), ISMS-IMP-A.8.24.4 (Key Management) |
| **Purpose** | Provide consolidated view of cryptographic control compliance across all domains (transmission, storage, authentication, key management) with executive summary metrics and completion tracking |
| **Target Audience** | CISO, Security Managers, Compliance Officers, Auditors, Senior Management |
| **Assessment Type** | Summary Dashboard / Executive Overview |
| **Review Cycle** | Quarterly (Aligned with Individual Assessment Refresh) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial dashboard specification and user completion guide | CISO / Security Manager |

---

# PART I: USER COMPLETION GUIDE

**Target Audience:** CISO, Security Managers, Compliance Officers, Executive Management, Internal Auditors

**Purpose of This Guide:** Enable autonomous generation, interpretation, and utilization of the A.8.24 Cryptography Compliance Dashboard for executive reporting and risk management.

**What This Document Does:**

- Explains how to generate the dashboard from source assessments
- Guides interpretation of compliance metrics and KPIs
- Provides decision frameworks for executive action
- Defines maintenance and update procedures

**What This Document Does NOT Do:**

- Replace detailed technical assessment completion (see IMP-1/2/3/4 User Guides)
- Define cryptographic requirements (see ISMS-POL-A.8.24)
- Provide remediation implementation guidance (technical teams handle execution)

---

# Dashboard Overview

## Purpose and Scope

**Executive Problem Statement:**  
How do we answer "Are we cryptographically compliant with ISO 27001 Control A.8.24?" in **under 5 minutes** for board presentation?

**Dashboard Solution:**  
Single-page executive summary consolidating 4 detailed assessments (Data Transmission, Storage, Authentication, Key Management) into actionable compliance intelligence.

**Key Questions Answered:**
1. What is our overall cryptographic compliance percentage?
2. Where are the critical gaps requiring immediate CISO attention?
3. What is the risk exposure from non-compliance?
4. What remediation actions are in progress and on-track?
5. Are we improving or declining quarter-over-quarter?

**Data Sources (Input Workbooks):**

- `ISMS-IMP-A.8.24.1_Data_Transmission_[DATE].xlsx` - 13 transmission categories
- `ISMS-IMP-A.8.24.2_Data_Storage_[DATE].xlsx` - 7 storage categories
- `ISMS-IMP-A.8.24.3_Authentication_[DATE].xlsx` - 5 authentication methods
- `ISMS-IMP-A.8.24.4_Key_Management_[DATE].xlsx` - 5 key lifecycle stages

**Output:** `ISMS-IMP-A.8.24.5_Compliance_Dashboard_[DATE].xlsx` - 9-sheet executive dashboard

## Target Audience

**Primary Users:**

- **CISO / Information Security Manager** - Overall compliance posture, gap prioritization, resource allocation
- **Executive Management / Board** - High-level compliance status, risk exposure, budget requirements
- **Compliance Officers** - Audit readiness, regulatory alignment, evidence tracking
- **Internal Audit** - Control effectiveness, remediation progress, compliance trending

**Secondary Users:**

- **Security Team Leads** - Detailed gap analysis, remediation planning, evidence collection
- **IT Management** - Resource requirements, implementation timelines, technical dependencies
- **External Auditors** - ISO 27001 certification evidence, control maturity demonstration

## Dashboard Structure (9 Sheets)

| Sheet # | Sheet Name | Purpose | Primary Audience |
|---------|------------|---------|------------------|
| 1 | **Executive Dashboard** | One-page compliance overview | CISO, Board, Executives |
| 2 | **Gap Analysis** | Consolidated non-compliance items | CISO, Security Team |
| 3 | **Risk Register** | Security risks from gaps | CISO, Risk Management |
| 4 | **Remediation Roadmap** | Action plans with timelines | CISO, IT Management |
| 5 | **KPIs & Metrics** | Quantitative performance indicators | CISO, Compliance |
| 6 | **Evidence Register** | Consolidated compliance evidence | Auditors, Compliance |
| 7 | **Action Items & Follow-up** | Follow-up tasks and ownership | Security Team, IT |
| 8 | **Audit & Compliance Log** | Compliance review history | Auditors, Compliance |
| 9 | **Approval Sign-Off** | Formal sign-off and approvals | CISO, Management |

**Navigation Strategy:**

- **5-minute executive briefing:** Sheet 1 (Executive Dashboard) ONLY
- **CISO deep-dive (30 minutes):** Sheets 1-4 (Executive, Gaps, Risks, Remediation)
- **Audit preparation (2 hours):** All 9 sheets
- **Quarterly review meeting:** Sheets 1, 4, 8, 9

## Connection to Policy Framework

**Policy Hierarchy:**
```
ISMS-POL-A.8.24 (Use of Cryptography Policy)
    │
    ├─► ISMS-IMP-A.8.24.1 (Data Transmission Assessment)
    ├─► ISMS-IMP-A.8.24.2 (Data Storage Assessment)
    ├─► ISMS-IMP-A.8.24.3 (Authentication Assessment)
    ├─► ISMS-IMP-A.8.24.4 (Key Management Assessment)
    │
    └─► ISMS-IMP-A.8.24.5 (Compliance Dashboard) ◄── YOU ARE HERE
```

**Dashboard Role:**

- **Policy (POL)** defines WHAT must be done
- **Assessments (IMP-1/2/3/4)** verify HOW WELL it's being done
- **Dashboard (IMP-5)** answers "SO WHAT?" for executives

## Time Investment

**Dashboard Generation:**

- **Automated generation (Python script):** 2 minutes
- **Manual validation:** 15 minutes
- **Executive summary writing:** 30 minutes
- **Total:** ~45 minutes per quarter

**Dashboard Review (by role):**

- **Executive (Board presentation):** 5 minutes (Sheet 1 only)
- **CISO (management review):** 30 minutes (Sheets 1-4)
- **Security Team (remediation planning):** 2 hours (All sheets)
- **Auditor (certification review):** 4 hours (All sheets + source workbooks)

**Quarterly Maintenance:**

- **Data refresh:** 5 minutes (re-run Python script with new source workbooks)
- **Trend update:** 10 minutes (update quarterly comparison data)
- **Meeting log update:** 15 minutes (document review meeting outcomes)
- **Total:** ~30 minutes per quarter after initial setup

---

# Prerequisites

## Completed Source Assessments (MANDATORY)

**Before generating dashboard, you MUST have completed:**

✅ **IMP-1 (Data Transmission):**

- All 13 transmission categories assessed
- Status assigned (✅ Compliant / ⚠️ Partial / ❌ Non-Compliant) for each system
- Evidence documented
- Approval obtained

✅ **IMP-2 (Data Storage):**

- All 7 storage categories assessed
- Encryption status verified for all data-at-rest scenarios
- Key escrow confirmed
- Approval obtained

✅ **IMP-3 (Authentication):**

- All 5 authentication methods evaluated
- Password hash algorithms verified
- MFA enforcement confirmed
- Approval obtained

✅ **IMP-4 (Key Management):**

- All 5 key lifecycle stages assessed
- Key generation, storage, rotation, backup, certificate management documented
- Approval obtained

**Quality Check:** Each source workbook should have:

- Summary Dashboard sheet with compliance % calculated
- Evidence Register populated (minimum 10 evidence items per workbook)
- Approval Sign-Off completed with signatures
- No outstanding "TBD" or blank fields in critical columns

## File Naming Requirements

**Source workbooks MUST be named:**

- `ISMS-IMP-A.8.24.1_Data_Transmission_YYYYMMDD.xlsx`
- `ISMS-IMP-A.8.24.2_Data_Storage_YYYYMMDD.xlsx`
- `ISMS-IMP-A.8.24.3_Authentication_YYYYMMDD.xlsx`
- `ISMS-IMP-A.8.24.4_Key_Management_YYYYMMDD.xlsx`

**OR shortened names** (for external link compatibility):

- `ISMS-IMP-A.8.24.1.xlsx`
- `ISMS-IMP-A.8.24.2.xlsx`
- `ISMS-IMP-A.8.24.3.xlsx`
- `ISMS-IMP-A.8.24.4.xlsx`

**Dashboard normalization script** can auto-create short names if needed.

## Tools and Access

**Required Software:**

- Python 3.x with openpyxl library (for automated generation)
- Microsoft Excel or LibreOffice Calc (for manual review and presentation)
- Access to all 4 source assessment workbooks
- Write permission to output directory

**Required Skills:**

- Understanding of ISO 27001 Control A.8.24
- Basic Excel navigation (filtering, sorting, chart interpretation)
- Executive reporting experience
- Risk assessment fundamentals

**NOT Required:**

- Cryptography expertise (already assessed in IMP-1/2/3/4)
- Python coding skills (script is ready-to-use)
- Deep technical infrastructure knowledge

---

# Dashboard Generation Workflow

## Step-by-Step Generation Process

**Step 1: Verify Prerequisites (5 minutes)**
```bash
# Check all 4 source workbooks exist
ls -lh ISMS-IMP-A.8.24.{1,2,3,4}*.xlsx

# Verify file sizes (should be >500 KB each if populated)
# Empty templates are ~200 KB
```

**Action:** If any workbook missing or suspiciously small, STOP and complete that assessment first.

---

**Step 2: Run Dashboard Generation Script (2 minutes)**
```bash
python3 generate_a824_5_compliance_summary_dashboard.py
```

**Expected Output:**
```
================================================================================
ISMS-IMP-A.8.24.5 - Compliance Summary Dashboard Generator
================================================================================

[1/4] Loading source assessments...
    ✓ Data Transmission (ISMS-IMP-A.8.24.1.xlsx)
    ✓ Data Storage (ISMS-IMP-A.8.24.2.xlsx)
    ✓ Authentication (ISMS-IMP-A.8.24.3.xlsx)
    ✓ Key Management (ISMS-IMP-A.8.24.4.xlsx)

[2/4] Extracting compliance data...
    ✓ Overall compliance: 87.3%
    ✓ Total gaps identified: 23
    ✓ Critical gaps: 3
    ✓ High-risk gaps: 8

[3/4] Generating dashboard sheets...
    ✓ Sheet 1: Executive Dashboard
    ✓ Sheet 2: Gap Analysis
    ✓ Sheet 3: Risk Register
    ✓ Sheet 4: Remediation Roadmap
    ✓ Sheet 5: KPIs & Metrics
    ✓ Sheet 6: Evidence Register
    ✓ Sheet 7: Action Items & Follow-up
    ✓ Sheet 8: Audit & Compliance Log
    ✓ Sheet 9: Approval Sign-Off

[4/4] Saving dashboard...
    ✓ ISMS-IMP-A.8.24.5_Compliance_Dashboard_20260115.xlsx

================================================================================
✅ DASHBOARD GENERATION COMPLETE
================================================================================
```

**Troubleshooting Common Errors:**

- **"File not found"** → Check file naming (use short names or normalization script)
- **"Sheet 'Summary Dashboard' not found"** → Source workbook incomplete, complete assessment first
- **"External link error"** → Excel needs to "update links" when opening dashboard
- **"Empty Gap Analysis"** → No gaps found (all 100% compliant) OR source workbooks not properly populated

---

**Step 3: Open Dashboard in Excel (1 minute)**
```
Open: ISMS-IMP-A.8.24.5_Compliance_Dashboard_20260115.xlsx
```

**Excel will prompt:** "This workbook contains links to other files. Update now?"

- **Click "Update"** to pull latest data from source workbooks
- **Click "Don't Update"** only if source workbooks have moved (will show #REF! errors)

**First Validation Check:**

- Sheet 1 (Executive Dashboard) → Overall Compliance Rate shows percentage (e.g., 87.3%)
- Sheet 2 (Gap Analysis) → Gap count matches expected non-compliant items
- Sheet 3 (Risk Register) → Risks present if critical/high gaps exist
- Sheet 6 (Evidence Register) → Evidence documents listed

**If any sheet is blank or shows #REF! errors:**
1. Close Excel
2. Check source workbook filenames match exactly
3. Run script again
4. Click "Update Links" when reopening

---

**Step 4: Complete Executive Summary (30 minutes)**

Navigate to **Sheet 1: Executive Dashboard, Section "Executive Summary"** (approximately rows 77-90).

**Fill in these fields:**

**Assessment Period:**
```
Q4 2024 (October 1 - December 31, 2024)
```

**Overall Compliance Status:** (Auto-calculated based on %)

- ≥95% → "Excellent - Mature cryptographic controls"
- 85-94% → "Good - Minor gaps, remediation in progress"
- 75-84% → "Needs Improvement - Significant gaps requiring attention"
- <75% → "Critical - Immediate CISO action required"

**Security Posture:** (Auto-calculated based on risk score)

- Risk Score <3 → "Strong - Low risk exposure"
- Risk Score 3-5 → "Adequate - Manageable risk"
- Risk Score 5-7 → "Weak - Elevated risk requiring mitigation"
- Risk Score >7 → "Critical - Unacceptable risk exposure"

**Key Achievements This Period:** (Manual entry - 5 bullet points)
*Example:*
```
• Implemented TLS 1.3 across all external HTTPS endpoints (SC-081v3 compliance)
• Achieved 100% MFA enrollment for privileged accounts
• Completed key rotation for 47 certificate authorities
• Migrated 12 legacy systems from weak password hashing (MD5) to bcrypt
• Established automated certificate expiration monitoring (90-day alerts)
```

**Major Concerns:** (Manual entry - 3-5 critical issues)
*Example:*
```
• 3 production databases still using DES encryption (non-compliant, target: Q1 2026)
• Service account password rotation not automated (manual process, 127 accounts)
• Internal PKI certificate validity exceeds 825 days on 8 CAs (policy violation)
• 12% of mobile devices lack full-disk encryption enforcement via MDM
• VPN configuration allows TLS 1.1 as fallback (deprecated protocol)
```

**Recommended Executive Actions:** (Numbered list, 3-5 actions)
*Example:*
```
1. Approve budget for HSM procurement (CHF 45,000) for service account key management
2. Prioritize database re-encryption project (3 critical systems, Q1 2026 target)
3. Enforce mobile device compliance policy (12% non-compliant devices, 30-day deadline)
4. Review and approve TLS 1.1 removal plan (impacts 4 legacy integrations)
5. Assign dedicated resource for certificate lifecycle automation (0.5 FTE)
```

**Budget Impact:** (Financial summary)
```
Total Estimated Remediation Budget: CHF 127,500 (from Remediation Roadmap)
Approved Budget:                    CHF 100,000 (2025 fiscal year)
Budget Gap:                         CHF 27,500 (requires additional approval)
```

---

**Step 5: Validate Calculations (15 minutes)**

**Sheet 1 Validation:**

- [ ] Overall Compliance Rate between 0-100%
- [ ] Critical Gaps count ≥ 0
- [ ] High-Risk Items count ≥ 0
- [ ] Remediation Progress between 0-100%
- [ ] Compliance by Area shows 4 rows (Transmission, Storage, Authentication, Key Management)
- [ ] All 4 source document links working (no #REF! errors)

**Sheet 2 Validation:**

- [ ] Total gaps = Sum of (Critical + High + Medium + Low)
- [ ] Gap descriptions specific (not generic "non-compliant")
- [ ] Risk levels assigned (Critical/High/Medium/Low)
- [ ] Systems affected identified
- [ ] Target dates reasonable (not all "TBD")

**Sheet 3 Validation:**

- [ ] Risk Register populated if Critical or High gaps exist
- [ ] Risk scores calculated (Likelihood × Impact)
- [ ] Mitigation strategies documented
- [ ] Risk owners assigned

**Sheet 4 Validation:**

- [ ] Remediation actions correspond to identified gaps
- [ ] Timelines realistic (not all "1 week")
- [ ] Responsible persons named (not "TBD")
- [ ] Dependencies identified
- [ ] Budget estimates provided

**Sheet 6 Validation:**

- [ ] Evidence documents from all 4 source assessments
- [ ] Evidence types diverse (policies, configs, logs, reports, screenshots)
- [ ] Storage locations specified
- [ ] Collection dates recent

**Common Validation Failures:**
❌ **All gaps show "TBD" for target date** → Return to source assessments, complete remediation plans
❌ **Evidence Register empty** → Source workbooks not properly populated
❌ **Risk Register shows "No risks identified" but gaps exist** → Script issue, regenerate dashboard
❌ **Overall compliance >95% but critical gaps exist** → Logic error, check source workbook Summary Dashboards

---

## First-Time Setup (One-Time Activities)

**Activity 1: Establish Baseline (Quarter 0)**

When generating dashboard for the first time:
1. **Document "as-is" state** (current compliance %, gap count, risk score)
2. **Set realistic targets** (don't expect 100% immediately)
3. **Prioritize critical gaps** (focus on high-risk, quick-win items first)
4. **Define improvement trajectory** (e.g., +10% compliance per quarter)

**Example Baseline:**
```
Q4 2024 (Baseline):

- Overall Compliance: 78.5%
- Critical Gaps: 12
- High-Risk Items: 27
- Target by Q2 2025: 90% compliance, 0 critical gaps

```

**Activity 2: Configure Trend Tracking**

The dashboard tracks quarter-over-quarter changes:
1. **Save Q4 2024 dashboard** as `ISMS-IMP-A.8.24.5_Dashboard_Q4_2024.xlsx`
2. **Next quarter:** Generate new dashboard, manually enter "Last Quarter" values in KPI sheet
3. **Trend arrows** (↑↓→) will show improvement/decline

**Activity 3: Integrate with Governance**

Schedule recurring activities:

- **Quarterly Security Review Meeting** (2 hours, CISO + Security Team)
  - Review dashboard Sheet 1 (Executive Summary)
  - Discuss Sheet 3 (Risk Register) and Sheet 4 (Remediation Roadmap)
  - Update Sheet 9 (Approval Sign-Off)
  
- **Board Reporting** (Annual or Semi-Annual)
  - Present Sheet 1 (Executive Dashboard) to board
  - Highlight compliance trend (improving/stable/declining)
  - Justify budget requests with Sheet 4 (Remediation Roadmap)

- **Internal Audit Engagement** (Annual)
  - Provide full dashboard (all 9 sheets)
  - Provide source workbooks (IMP-1/2/3/4)
  - Demonstrate evidence traceability (Sheet 6 → Source workbooks → Actual evidence)

---

# Understanding Dashboard Sections

## Sheet 1: Executive Dashboard (THE CRITICAL SHEET)

**Purpose:** Answer "Are we cryptographically compliant?" in under 5 minutes.

**Key Metrics (Top Section):**

**Overall Compliance Rate**

- **What it measures:** Percentage of cryptographic controls fully implemented
- **Calculation:** Average of 4 assessment area compliance rates
- **Interpretation:**
  - **≥95%** (Green) → Excellent, audit-ready, mature ISMS
  - **85-94%** (Yellow) → Good, minor gaps, certification achievable with remediation plan
  - **75-84%** (Amber) → Needs improvement, systematic issues, requires CISO focus
  - **<75%** (Red) → Critical, certification at risk, immediate executive action required

**Example:**
```
Current: 87.3% (Yellow - Good)
Target: ≥95% (Green - Excellent)
Gap: 7.7 percentage points → ~15 additional controls to implement
```

**Critical Gaps**

- **What it measures:** Count of non-compliant controls affecting Restricted data or critical systems
- **Interpretation:**
  - **0** (Green) → No immediate security risks
  - **1-3** (Yellow) → Manageable, track in remediation roadmap
  - **4-10** (Red) → Concerning, requires prioritization
  - **>10** (Dark Red) → Crisis level, CISO escalation to executive management

**Example:**
```
Current: 3 critical gaps
    1. Production database using DES encryption (Restricted data)
    2. Service accounts with plaintext passwords stored in scripts
    3. VPN allowing TLS 1.0 (deprecated protocol, external access)
```

**High-Risk Items**

- **What it measures:** Count of gaps with high likelihood × high impact
- **Interpretation:**
  - **≤5** (Green) → Normal risk appetite
  - **6-15** (Yellow) → Elevated risk, monitor closely
  - **16-30** (Amber) → High risk exposure, requires mitigation strategy
  - **>30** (Red) → Unacceptable risk, immediate action required

**Remediation Progress**

- **What it measures:** Percentage of identified gaps with remediation in progress or completed
- **Calculation:** (Completed + In-Progress) / Total Gaps × 100%
- **Interpretation:**
  - **≥80%** (Green) → Active remediation culture
  - **50-79%** (Yellow) → Adequate but needs acceleration
  - **<50%** (Red) → Stalled remediation, accountability issue

**Compliance by Assessment Area (Middle Section):**

**Table Interpretation:**

| Assessment Area | Compliance % | Interpretation |
|-----------------|--------------|----------------|
| **Data Transmission** | 92.5% | Strong (TLS, VPN, SSH mostly compliant) |
| **Data Storage** | 78.4% | Weak (FDE/TDE gaps, focus here) |
| **Authentication** | 89.1% | Good (MFA strong, service accounts weak) |
| **Key Management** | 88.9% | Good (rotation automated, backup manual) |

**Action Priority:** Focus remediation on lowest-scoring area (Data Storage in this example).

**Trend Column:**

- **↑ (Green):** Improved from last quarter → Continue current approach
- **→ (Yellow):** No change → Investigate: lack of resources? blocked by dependencies?
- **↓ (Red):** Declined → Red flag! Why? New systems? policy violations? Immediate investigation required.

**Top 5 Critical Issues (Bottom Section):**

**Auto-populated from Gap Analysis, sorted by risk score.**

**Example Critical Issue:**
```
Rank 1: Production database "CustomerDB" using DES encryption
    Assessment Area: Data Storage
    Risk Level: Critical
    Systems Affected: 1 (but contains 50,000 customer records - Restricted data)
    Target Date: 31.03.2025
    Owner: Database Administrator (John Doe)
    Status: In Progress (re-encryption scheduled, 60% complete)
```

**CISO Question:** "Why is DES encryption still in use in 2025?"
**Answer (from Gap Analysis notes):** "Legacy system from 2012, vendor no longer supports. Migration to PostgreSQL with AES-256 TDE approved, Q1 2025 completion target."

**Executive Action:** "Approve CHF 15,000 budget for external consultant to accelerate migration by 2 weeks."

---

## Sheet 2: Gap Analysis (THE DETAIL SHEET)

**Purpose:** Comprehensive list of ALL non-compliant items across 4 assessments.

**Summary Statistics (Top Section):**

Provides gap distribution by severity:

| Assessment Area | Total Gaps | Critical | High | Medium | Low |
|-----------------|------------|----------|------|--------|-----|
| Data Transmission | 8 | 1 | 3 | 3 | 1 |
| Data Storage | 12 | 2 | 4 | 4 | 2 |
| Authentication | 5 | 0 | 2 | 2 | 1 |
| Key Management | 7 | 0 | 3 | 3 | 1 |

**Interpretation:**

- **Data Storage has most gaps (12)** → Priority area
- **Data Transmission has 1 critical gap** → Investigate immediately
- **Authentication has 0 critical** → Lower priority, can address in Q2

**Detailed Gap Register (Rows 12+):**

Each gap includes:

- **Gap ID:** Unique identifier (e.g., GAP-A824-001)
- **Description:** Specific issue (not "non-compliant", but "VPN using 1024-bit DH group")
- **Assessment Area:** Which workbook it came from
- **System/Service:** Affected asset
- **Risk Level:** Critical/High/Medium/Low
- **Data Classification:** Restricted/Confidential/Internal/Public
- **Current State:** What exists now (e.g., "TLS 1.1 enabled")
- **Required State:** What policy requires (e.g., "TLS 1.2 minimum")
- **Target Date:** Remediation deadline
- **Owner:** Responsible person
- **Status:** Not Started / In Progress / Completed / Blocked

**Filtering Strategy:**
1. **Filter by Risk Level = Critical** → Address these first (typically 0-3 items)
2. **Filter by Assessment Area = [Lowest scoring]** → Systematic improvement
3. **Filter by Status = Blocked** → Identify and resolve dependencies
4. **Filter by Owner = [Your team]** → Assign resources effectively

---

## Sheet 3: Risk Register (THE RISK SHEET)

**Purpose:** Translate technical gaps into business risks for executive understanding.

**Risk Scoring:**

- **Likelihood:** (1-5) How likely is exploitation/breach?
- **Impact:** (1-5) What's the damage if it occurs?
- **Risk Score:** Likelihood × Impact (max 25)

**Risk Interpretation:**

- **20-25 (Critical):** Unacceptable, immediate action, escalate to board
- **15-19 (High):** Requires CISO attention, remediate within quarter
- **10-14 (Medium):** Monitor closely, remediate within 6 months
- **5-9 (Low):** Acceptable with controls, annual review
- **1-4 (Minimal):** Track only, no immediate action

**Example Risk:**
```
Risk ID: RISK-A824-003
Gap ID: GAP-A824-015 (linked)
Description: Unencrypted customer database backup stored on network share
Likelihood: 4 (High - accessible by 50+ employees, no access logging)
Impact: 5 (Critical - 50,000 customer records, Restricted classification, GDPR breach)
Risk Score: 20 (CRITICAL)
Mitigation: Implement AES-256 encryption on backup files, restrict access to 3 DBAs only
Owner: Database Manager (Jane Smith)
Target: 15.02.2025 (30 days - URGENT)
```

**CISO Use Case:**

- Present Risk Register to Board: "We have 1 critical risk, 8 high risks. Here's our mitigation plan and budget request."

---

## Sheet 4: Remediation Roadmap (THE ACTION SHEET)

**Purpose:** Project plan view of gap remediation with timelines and dependencies.

**Columns:**

- **Action ID:** Unique identifier
- **Gap/Risk:** Linked to Sheet 2 or 3
- **Remediation Action:** Specific task (e.g., "Upgrade VPN to WireGuard")
- **Owner:** Person responsible
- **Start Date:** When work begins
- **Target Date:** Completion deadline
- **Status:** Not Started / In Progress / Completed / Blocked / Overdue
- **Dependencies:** What must happen first
- **Estimated Cost:** Budget requirement
- **Actual Cost:** Actual spend (track variances)
- **Progress %:** 0-100%

**Timeline View:**
Sort by Target Date to create Gantt-style view:
```
January 2025:

    - Action 1: Implement BitLocker on 50 laptops (Target: 15.01.2025)
    - Action 2: Migrate database to TDE (Target: 31.01.2025)

February 2025:

    - Action 3: Automate service account rotation (Target: 15.02.2025)
    - Action 4: Deploy MFA for all users (Target: 28.02.2025)

March 2025:

    - Action 5: Certificate automation (ACME) (Target: 15.03.2025) ← SC-081v3 deadline!

```

**Budget Rollup:**
```
Total Remediation Budget: CHF 127,500

    - Q1 2025: CHF 45,000 (HSM procurement, database migration)
    - Q2 2025: CHF 62,500 (service account automation, MFA licenses)
    - Q3 2025: CHF 20,000 (certificate automation, VPN upgrade)

```

**CISO Use Case:**

- Present to CFO: "Here's our cryptography remediation roadmap for 2025. Total investment CHF 127,500 over 3 quarters. Reduces cyber risk exposure by 65%."

---

## Sheet 5: KPIs & Metrics (THE MEASUREMENT SHEET)

**Purpose:** Quantitative performance indicators for trend analysis.

**KPI Examples:**

| KPI | Current | Target | Status | Last Quarter | Change |
|-----|---------|--------|--------|--------------|--------|
| **Cryptographic Controls Implemented** | 87.3% | ≥95% | Yellow | 78.5% | +8.8% ↑ |
| **Systems with Encryption at Rest** | 156/180 | 180/180 | Yellow | 142/180 | +14 ↑ |
| **Systems with Encryption in Transit** | 98/100 | 100/100 | Yellow | 95/100 | +3 ↑ |
| **MFA Coverage (All Users)** | 92% | 100% | Yellow | 87% | +5% ↑ |
| **MFA Coverage (Admins)** | 100% | 100% | Green | 100% | 0% → |
| **Certificate Expiry Compliance** | 94% | 100% | Yellow | 91% | +3% ↑ |
| **Key Rotation Compliance** | 88% | ≥95% | Yellow | 82% | +6% ↑ |
| **Service Accounts with Strong Auth** | 45% | ≥90% | Red | 38% | +7% ↑ |
| **Password Hashing Compliance** | 96% | 100% | Yellow | 89% | +7% ↑ |
| **SSO Coverage** | 78% | ≥80% | Yellow | 72% | +6% ↑ |
| **Open Critical Gaps** | 3 | 0 | Red | 5 | -2 ↑ |
| **Remediation On-Time %** | 76% | ≥90% | Yellow | 68% | +8% ↑ |

**Trend Analysis:**

- **All KPIs improving** (green arrows) → Healthy ISMS, effective remediation
- **Some KPIs declining** (red arrows) → Investigate root cause (new systems? policy violations?)
- **Stagnant KPIs** (yellow arrows) → Lack of resources? Blocked by dependencies?

**Executive Communication:**
```
"We've improved overall compliance from 78.5% to 87.3% over the past quarter (+8.8 percentage points).
Key wins: MFA coverage up 5%, critical gaps reduced from 5 to 3.
Remaining challenge: Service account authentication still at 45% (target 90%, requires automation project)."
```

---

## Sheets 6-9: Supporting Documentation

**Sheet 6: Evidence Register**

- **Purpose:** Consolidated list of all compliance evidence from 4 source assessments
- **Use Case:** Auditor asks "Show me evidence of TLS 1.3 enforcement" → Point to evidence ID, location, retrieval instructions
- **Maintenance:** Auto-populated from source workbooks, no manual updates needed

**Sheet 7: Action Items & Follow-up**

- **Purpose:** Track non-remediation tasks (e.g., "Schedule training on new VPN client")
- **Use Case:** Security team weekly standup, review open action items
- **Maintenance:** Update status weekly

**Sheet 8: Audit & Compliance Log**

- **Purpose:** Historical record of compliance reviews, audit findings, certification milestones
- **Use Case:** Demonstrate continuous improvement to auditors ("We've conducted quarterly reviews since Q4 2024")
- **Maintenance:** Update after each quarterly review or audit

**Sheet 9: Approval Sign-Off**

- **Purpose:** Formal sign-off and approval records for compliance assessments
- **Use Case:** Demonstrate management approval and accountability to auditors
- **Maintenance:** Update after each quarterly review or major compliance milestone

---

# Interpreting Results

## Compliance Percentage Ranges

**≥95% - EXCELLENT (Green)**

- **Meaning:** Mature cryptographic controls, audit-ready
- **Characteristics:**
  - 0-1 critical gaps
  - All Restricted data encrypted
  - Automated key rotation
  - Certificate lifecycle management
  - Comprehensive evidence
- **CISO Message:** "We have a strong cryptographic posture aligned with industry best practices."
- **Action:** Maintain current state, monitor for new threats (e.g., quantum computing)

**85-94% - GOOD (Yellow)**

- **Meaning:** Minor gaps, remediation in progress, certification achievable
- **Characteristics:**
  - 2-5 critical gaps
  - Most systems compliant
  - Some manual processes
  - Evidence mostly complete
- **CISO Message:** "We're on track for certification. Addressing remaining gaps in Q1 roadmap."
- **Action:** Execute remediation plan, target 95%+ within 1-2 quarters

**75-84% - NEEDS IMPROVEMENT (Amber)**

- **Meaning:** Significant gaps, systematic issues, requires CISO focus
- **Characteristics:**
  - 6-10 critical gaps
  - Inconsistent implementation
  - Weak areas (e.g., key management)
  - Evidence gaps
- **CISO Message:** "We have work to do. Prioritizing cryptographic controls as major initiative."
- **Action:** Dedicate resources (FTE, budget), create detailed remediation plan, monthly CISO reviews

**<75% - CRITICAL (Red)**

- **Meaning:** Certification at risk, immediate executive action required
- **Characteristics:**
  - >10 critical gaps
  - Unencrypted Restricted data
  - Deprecated algorithms in use
  - No key management
  - Major evidence gaps
- **CISO Message:** "We have a critical gap in our ISMS. Requesting emergency budget and resources."
- **Action:** Executive escalation, dedicated project team, external consultant, weekly executive updates

---

## Gap Severity Interpretation

**Critical Gaps (Immediate Action Required)**

- **Definition:** Non-compliance affecting Restricted data or critical systems
- **Examples:**
  - Unencrypted database with Restricted data
  - Plaintext passwords for privileged accounts
  - TLS 1.0 on external-facing service
  - No key backup for critical encryption keys
- **Response Time:** 30 days maximum, often 1-2 weeks
- **Escalation:** CISO → CIO/CEO if not resolved

**High Gaps (Requires CISO Attention)**

- **Definition:** Non-compliance affecting Confidential data or important systems
- **Examples:**
  - Weak password hashing (MD5/SHA-1)
  - Manual certificate renewal (high risk of expiration)
  - Service accounts without rotation
  - VPN using deprecated DH groups
- **Response Time:** 90 days
- **Escalation:** CISO review if not resolved

**Medium Gaps (Monitor Closely)**

- **Definition:** Non-compliance affecting Internal data or standard systems
- **Examples:**
  - Laptop without BitLocker (Internal data only)
  - Email without S/MIME (TLS-only)
  - Key rotation annual instead of quarterly
- **Response Time:** 6 months
- **Escalation:** Security team review

**Low Gaps (Track Only)**

- **Definition:** Minor deviations, no immediate risk
- **Examples:**
  - Documentation gaps
  - Non-critical systems not in scope
  - Planned future improvements
- **Response Time:** 12 months or next major change
- **Escalation:** None required

---

## Risk Scoring Decision Framework

**Risk Score = Likelihood × Impact (1-5 scale each, max 25)**

**Likelihood Assessment:**
1. **Very Low (1):** Extremely unlikely, theoretical only
2. **Low (2):** Unlikely, requires sophisticated attacker
3. **Medium (3):** Possible, moderate attacker skill required
4. **High (4):** Likely, accessible to many attackers
5. **Very High (5):** Almost certain, trivial to exploit

**Impact Assessment:**
1. **Very Low (1):** Public data, minimal business impact
2. **Low (2):** Internal data, minor business disruption
3. **Medium (3):** Confidential data, significant disruption
4. **High (4):** Restricted data, major financial/reputational damage
5. **Very High (5):** Critical data, existential threat to organization

**Decision Matrix:**

| Risk Score | Risk Level | CISO Action | Timeframe |
|------------|------------|-------------|-----------|
| 20-25 | **Critical** | Escalate to Board, emergency remediation | 1-2 weeks |
| 15-19 | **High** | CISO-led remediation project | 30-90 days |
| 10-14 | **Medium** | Security team-led remediation | 6 months |
| 5-9 | **Low** | Monitor, remediate opportunistically | 12 months |
| 1-4 | **Minimal** | Accept risk, annual review | No action |

**Example Risk Assessment:**

**Scenario:** Production database "HR_Payroll" using DES encryption

**Likelihood:** 4 (High)

- Database accessible on internal network
- 50 employees have network access
- No access logging
- Known DES vulnerabilities widely published

**Impact:** 5 (Very High)

- Contains 500 employee salary records (Restricted data)
- GDPR personal data breach = €20M fine potential
- Reputational damage if leaked
- Employee morale impact

**Risk Score:** 4 × 5 = 20 (CRITICAL)

**CISO Decision:** Emergency remediation within 2 weeks, escalate to CEO if resources not available.

---

# Common Questions

## Q1: Why don't the percentages match my expectations?

**Answer:** N/A (Not Applicable) items are excluded from compliance calculations.

**Example:**

- Assessment has 100 total checklist items
- 10 items marked "N/A" (e.g., "Do you use SSH?" → No)
- Compliance calculated on 90 applicable items only
- 80 compliant ÷ 90 applicable = 88.9% (not 80%)

**Verification:** Check source workbook Summary Dashboard, verify N/A count is reasonable.

---

## Q2: How often should the dashboard be updated?

**Answer:** Quarterly minimum, monthly recommended, real-time if automated.

**Quarterly (MINIMUM):**

- Coincides with ISO 27001 management review requirement
- Aligns with typical remediation timelines (30-90 days)
- Provides sufficient data for trend analysis

**Monthly (RECOMMENDED):**

- Faster feedback loop on remediation progress
- Early detection of declining trends
- More granular tracking for active projects

**Real-Time (ADVANCED):**

- Integrate dashboard with monitoring tools (SIEM, configuration management)
- Auto-refresh from live data sources
- Requires significant automation investment

**Trigger for Out-of-Cycle Update:**

- Major incident (e.g., cryptographic vulnerability disclosed)
- Significant infrastructure change (e.g., cloud migration)
- Audit preparation (update 2 weeks before audit)

---

## Q3: Can I drill down into specific gaps?

**Answer:** Yes, use Gap ID to reference source assessment workbooks.

**Workflow:**
1. **Dashboard → Sheet 2 (Gap Analysis)** → Identify gap of interest (e.g., GAP-A824-015)
2. **Note Assessment Area** → "Data Storage"
3. **Open source workbook** → `ISMS-IMP-A.8.24.2_Data_Storage_[DATE].xlsx`
4. **Find gap in assessment sheet** → Search for system/service name
5. **Review detailed notes** → Status, evidence, remediation plan

**Example:**
```
Gap ID: GAP-A824-015
Description: Database "HR_Payroll" using DES encryption
Assessment Area: Data Storage

→ Open ISMS-IMP-A.8.24.2_Data_Storage_[DATE].xlsx
→ Navigate to Sheet "4. Databases"
→ Find row: System/Service = "HR_Payroll"
→ Review columns: Encryption Algorithm, Key Length, Status, Gap Description, Remediation Plan
```

**This provides:**

- Full context (when was it assessed? who assessed it?)
- Detailed gap description (why is it non-compliant?)
- Evidence location (where is proof of current state?)
- Remediation plan (what's being done? when? by whom?)

---

## Q4: What do I present to executives/board?

**Answer:** Use Sheet 1 (Executive Dashboard) ONLY - Single page, 5-minute presentation.

**Board Presentation Structure (5 slides, 10 minutes):**

**Slide 1: Compliance Overview**
```
ISMS A.8.24 Cryptography Compliance Status
Q4 2024

Overall Compliance: 87.3% (Target: ≥95%)
Critical Gaps: 3 (Target: 0)
Status: GOOD - On track for ISO 27001 certification

[Show pie chart: 87.3% Compliant / 12.7% Gaps]
```

**Slide 2: Compliance by Area**
```
Assessment Area Breakdown

Data Transmission:   92.5% ✓ (Strong)
Authentication:      89.1% ✓ (Good)
Key Management:      88.9% ✓ (Good)
Data Storage:        78.4% ⚠  (Needs Focus)

[Show bar chart comparing 4 areas]
```

**Slide 3: Critical Issues (Top 3)**
```
Top 3 Critical Gaps Requiring Board Awareness

1. Production database using DES encryption

   - Risk: Data breach, GDPR violation
   - Action: Migration to AES-256 TDE
   - Investment: CHF 15,000
   - Timeline: Complete by 31.03.2025

2. Service account plaintext passwords

   - Risk: Privileged access compromise
   - Action: HSM implementation
   - Investment: CHF 45,000
   - Timeline: Complete by 30.04.2025

3. VPN TLS 1.0 fallback enabled

   - Risk: Man-in-the-middle attack
   - Action: Upgrade to WireGuard
   - Investment: CHF 8,000
   - Timeline: Complete by 28.02.2025

```

**Slide 4: Remediation Roadmap**
```
2025 Cryptographic Controls Roadmap

Q1 2025:

- Complete database encryption upgrades
- Implement HSM for key management
- TLS protocol enforcement

Q2 2025:

- Automate certificate lifecycle
- Service account rotation
- MFA universal rollout

Total Investment: CHF 127,500
Risk Reduction: 65%

[Show timeline Gantt chart]
```

**Slide 5: Recommendation**
```
Board Decision Required

Approve CHF 127,500 cybersecurity investment for:
1. Cryptographic control remediation (ISO 27001 certification)
2. Risk reduction (65% cyber risk exposure decrease)
3. Regulatory compliance (GDPR, nFADP alignment)

Expected Outcome:

- ISO 27001 certification by Q3 2025
- Mature cryptographic posture (≥95% compliance)
- Reduced cyber insurance premiums (~10% reduction)

[Motion: Approve budget / Request more info / Decline]
```

**Board Q&A Preparation:**

- **"Why so expensive?"** → HSM is CHF 45K (industry standard for key management, alternatives are non-compliant)
- **"What if we don't do this?"** → Certification failure, GDPR fines (up to €20M), increased breach risk
- **"Can we delay?"** → Some items urgent (DES encryption), others flexible (service account rotation)

---

## Q5: How do I maintain version control?

**Answer:** Use quarterly snapshots with standardized naming.

**File Naming Convention:**
```
ISMS-IMP-A.8.24.5_Compliance_Dashboard_Q[Quarter]_[Year].xlsx

Examples:
ISMS-IMP-A.8.24.5_Compliance_Dashboard_Q4_2024.xlsx
ISMS-IMP-A.8.24.5_Compliance_Dashboard_Q1_2025.xlsx
ISMS-IMP-A.8.24.5_Compliance_Dashboard_Q2_2025.xlsx
```

**Storage Location:**
```
/ISMS/A.8.24-Cryptography/Dashboards/
├── 2024/
│   ├── Q1/ (if exists)
│   ├── Q2/ (if exists)
│   ├── Q3/ (if exists)
│   └── Q4/
│       ├── ISMS-IMP-A.8.24.5_Compliance_Dashboard_Q4_2024.xlsx
│       ├── Source_Assessments/
│       │   ├── ISMS-IMP-A.8.24.1_Data_Transmission_20241231.xlsx
│       │   ├── ISMS-IMP-A.8.24.2_Data_Storage_20241231.xlsx
│       │   ├── ISMS-IMP-A.8.24.3_Authentication_20241231.xlsx
│       │   └── ISMS-IMP-A.8.24.4_Key_Management_20241231.xlsx
│       └── Evidence/
│           └── [All evidence documents referenced in assessments]
└── 2025/
    ├── Q1/
    │   └── [Same structure]
    └── Q2/
        └── [Same structure]
```

**Retention:**

- **Active quarter:** Current + previous 4 quarters (1 year rolling)
- **Archive:** Years 2-3 moved to archive storage
- **Permanent retention:** Certification year dashboards (ISO 27001 audit evidence)

**Change Log:**
Each quarterly dashboard should include version notes:
```
Version History:
Q4 2024 (v1.0): Baseline assessment
Q1 2025 (v1.1): Added 14 systems (cloud migration), closed 5 critical gaps
Q2 2025 (v1.2): HSM implemented, service account automation complete
```

---

# Dashboard Maintenance

## Quarterly Update Procedure

**Week 1 of New Quarter: Refresh Source Assessments**
1. **Re-run 4 assessment workbooks** (IMP-1/2/3/4)
2. **Update changed systems** (new servers, decommissioned systems, configuration changes)
3. **Verify remediation completions** (mark gaps as "Completed" if implemented)
4. **Collect new evidence** (configuration exports, compliance reports, screenshots)
5. **Obtain approvals** (technical reviewer, security reviewer, CISO)

**Week 2: Regenerate Dashboard**
1. **Run dashboard generation script** with Q[N] source workbooks
2. **Validate calculations** (compliance %, gap counts, risk scores)
3. **Update Executive Summary** (key achievements, concerns, actions)
4. **Complete trend data** (manually enter "Last Quarter" values in KPI sheet)
5. **Update Sheet 8 (Audit & Compliance Log)** with quarterly review date

**Week 3: Management Review**
1. **Schedule Quarterly Security Review Meeting** (2 hours)
2. **Present dashboard** to CISO, Security Team, IT Management
3. **Discuss:**

   - Compliance trends (improving/declining?)
   - Critical gaps status (on track for remediation?)
   - Resource constraints (budget/staff issues?)
   - New risks emerged (vulnerabilities, threats, changes?)

4. **Document meeting** in Sheet 9 (Approval Sign-Off)
5. **Assign action items** in Sheet 7 (Action Items & Follow-up)

**Week 4: Archive and Distribute**
1. **Save final version** as `ISMS-IMP-A.8.24.5_Compliance_Dashboard_Q[N]_[YEAR].xlsx`
2. **Move to quarterly folder** (version control)
3. **Distribute** to stakeholders (CISO, Compliance, Audit, Management)
4. **Update SharePoint/Document Management System** if used

---

## Between-Quarter Activities

**Monthly (Lightweight Check-In):**

- Review Remediation Roadmap (Sheet 4) for overdue items
- Update Action Items & Follow-up (Sheet 7) with progress
- No need to regenerate entire dashboard

**Ad-Hoc (As-Needed):**

- **Major incident:** If cryptographic vulnerability disclosed, regenerate dashboard to assess impact
- **Significant change:** If major system deployed/decommissioned, update affected assessment (IMP-1/2/3/4) only
- **Audit preparation:** Regenerate dashboard 2 weeks before audit with latest data

---

## Continuous Improvement

**After Each Quarterly Cycle, Ask:**
1. **Dashboard Utility:** Did executives find Sheet 1 useful? Too much/too little info?
2. **Gap Analysis Accuracy:** Did gaps identified reflect actual risks? False positives?
3. **Remediation Effectiveness:** Did roadmap timelines hold? What caused delays?
4. **Evidence Quality:** Did auditors accept evidence referenced? Gaps?
5. **Automation Opportunities:** Can any manual steps be automated?

**Examples of Improvements:**

- **Q1 → Q2:** Added trend arrows to Executive Dashboard (more visual)
- **Q2 → Q3:** Automated KPI calculation (was manual)
- **Q3 → Q4:** Integrated with SIEM for real-time certificate expiration monitoring

---

# Quality Checklist

## Before Presenting Dashboard to CISO/Executives

**Data Quality:**

- [ ] All 4 source workbooks dated within last 30 days
- [ ] No #REF! errors in any dashboard sheets
- [ ] Overall compliance % between 0-100%
- [ ] Gap count matches detailed Gap Analysis sheet
- [ ] Evidence Register has entries from all 4 assessments
- [ ] No "TBD" in critical fields (risk owners, target dates)

**Executive Summary:**

- [ ] Assessment period specified (e.g., "Q4 2024")
- [ ] Key achievements listed (3-5 bullets)
- [ ] Major concerns documented (3-5 critical issues)
- [ ] Recommended actions provided (3-5 items)
- [ ] Budget impact calculated (total remediation cost)
- [ ] Narrative is CISO-level (not too technical, not too vague)

**Gap Analysis:**

- [ ] All gaps have specific descriptions (not generic "non-compliant")
- [ ] Risk levels assigned based on likelihood × impact
- [ ] Target dates are realistic (not all "ASAP" or "TBD")
- [ ] Owners are named individuals (not "IT Team")
- [ ] Systems affected are specifically identified

**Risk Register:**

- [ ] Risk scores calculated correctly (Likelihood × Impact)
- [ ] Mitigation strategies documented for Critical/High risks
- [ ] Risk owners assigned (typically CISO for Critical, Security Manager for High)
- [ ] Target dates align with Remediation Roadmap

**Remediation Roadmap:**

- [ ] Actions correspond to gaps in Gap Analysis
- [ ] Timelines are sequenced logically (dependencies noted)
- [ ] Budget estimates provided (even if rough)
- [ ] Progress % reflects actual work done (not aspirational)
- [ ] Blocked items have explanations

**Evidence Register:**

- [ ] Evidence documents listed for all 4 assessment areas
- [ ] Storage locations specified (network path, SharePoint URL, etc.)
- [ ] Collection dates recent (within 90 days)
- [ ] Evidence types diverse (not just "screenshot")

**Approval & Sign-Off:**

- [ ] Prepared By field completed (your name, role, date)
- [ ] Reviewed By field completed (technical reviewer, date)
- [ ] Approved By field completed (CISO, date)
- [ ] Next Review Date specified (90 days from approval)

---

# Review & Approval

## Four-Level Review Process

**Level 1: Self-Review (Preparer)**

- **Who:** Person who generated dashboard (Security Analyst/Engineer)
- **Timeline:** 1 day
- **Focus:**
  - Data accuracy (spot-check source workbook links)
  - Calculation correctness (compliance %, risk scores)
  - Completeness (no blank critical fields)
  - Clarity (executive summary is understandable)
- **Deliverable:** Dashboard ready for technical review

**Level 2: Technical Review**

- **Who:** Security Team Lead or Senior Security Engineer
- **Timeline:** 2 days
- **Focus:**
  - Gap descriptions technically accurate
  - Risk assessments reasonable
  - Remediation plans feasible
  - Evidence sufficient
- **Deliverable:** Technical approval in Sheet 9 (Approval Sign-Off)

**Level 3: Security Management Review**

- **Who:** CISO or Information Security Manager
- **Timeline:** 3 days
- **Focus:**
  - Executive summary aligns with business priorities
  - Critical gaps appropriately prioritized
  - Budget estimates realistic
  - Board presentation-ready
- **Deliverable:** CISO approval signature

**Level 4: Executive Presentation (Optional)**

- **Who:** Board or Executive Management
- **Timeline:** 1 meeting (quarterly or semi-annual)
- **Focus:**
  - Compliance trend (improving/declining?)
  - Investment justification (ROI on budget request)
  - Risk appetite alignment (acceptable gaps?)
- **Deliverable:** Board decision on budget approval

---

## After Approval

**Immediate Actions:**
1. **Distribute dashboard** to stakeholders (Security Team, IT Management, Compliance, Audit)
2. **Archive quarterly version** in version control
3. **Update next review date** (90 days from approval)
4. **Communicate results** to assessment completers (thank them, share compliance %)

**Ongoing Tracking:**
1. **Monitor Remediation Roadmap** monthly (are we on track?)
2. **Update Action Items & Follow-up** weekly (security team standup)
3. **Prepare for next quarter** (identify upcoming assessments)

**Preparation for Audit:**

- **Stage 1 Audit (Documentation Review):** Provide dashboard as evidence of compliance monitoring
- **Stage 2 Audit (On-Site):** Demonstrate dashboard use in management review meeting
- **Surveillance Audits (Annual):** Show quarterly dashboard trend (continuous improvement)

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel dashboard workbook generation and maintenance. Users completing the dashboard should refer to Part I above.

---

# Instructions for Dashboard Development

## Workbook Generation

**Python Script:** `generate_a824_5_compliance_summary_dashboard.py`

**Critical Design Principle:**
This dashboard is a **CONSOLIDATION TOOL**, not a data entry workbook. It reads data FROM 4 source workbooks:

- ISMS-IMP-A.8.24.1 (Data Transmission)
- ISMS-IMP-A.8.24.2 (Data Storage)
- ISMS-IMP-A.8.24.3 (Authentication)
- ISMS-IMP-A.8.24.4 (Key Management)

**Data Extraction Approach:**
1. **External workbook links** (preferred) - Live data, auto-updates when source workbooks change
2. **Python-based extraction** (alternative) - Snapshot at generation time, requires regeneration for updates

**Current Implementation:** External workbook links (Excel formulas reference source workbooks)

## Schema Validation (CRITICAL)

**Before building consolidation logic, DOCUMENT the actual structure of each source workbook:**

```python
SOURCE_WORKBOOK_SCHEMAS = {
    'ISMS-IMP-A.8.24.1.xlsx': {
        'summary_sheet': 'Summary Dashboard',
        'key_cells': {
            'total_items': 'B9',
            'compliant': 'C9',
            'partial': 'D9',
            'non_compliant': 'E9',
            'na': 'F9',
            'compliance_pct': 'G9'
        },
        'assessment_sheets': [
            '1.1 External HTTPS-TLS',
            '1.2 Internal HTTPS-TLS',
            # ... 13 total sheets
        ],
        'evidence_sheet': 'Evidence Register',
        'gap_extraction': {
            'status_column': 'D',  # Status column in assessment sheets
            'non_compliant_value': '❌ Non-Compliant',
            'partial_value': '⚠️ Partial',
            'system_column': 'A',
            'gap_description_column': 'M',  # Or wherever gap descriptions are
            'remediation_column': 'N'
        }
    },
    'ISMS-IMP-A.8.24.2.xlsx': {
        'summary_sheet': 'Summary Dashboard',
        'key_cells': {
            'total_items': 'B9',
            'compliant': 'C9',
            'partial': 'D9',
            'non_compliant': 'E9',
            'na': 'F9',
            'compliance_pct': 'G9'
        },
        'assessment_sheets': [
            '1. Mobile Devices',
            '2. Laptops & Workstations',
            # ... 7 total sheets
        ],
        'evidence_sheet': 'Evidence Register',
        'gap_extraction': {
            'status_column': 'D',
            'non_compliant_value': '❌ Non-Compliant',
            'partial_value': '⚠️ Partial',
            'system_column': 'A',
            'gap_description_column': 'M',
            'remediation_column': 'N'
        }
    },
    'ISMS-IMP-A.8.24.3.xlsx': {
        'summary_sheet': 'Summary Dashboard',
        'key_cells': {
            'total_items': 'B9',
            'compliant': 'C9',
            'partial': 'D9',
            'non_compliant': 'E9',
            'na': 'F9',
            'compliance_pct': 'G9'
        },
        'assessment_sheets': [
            '1. Password Security',
            '2. Multi-Factor Authentication',
            # ... 5 total sheets
        ],
        'evidence_sheet': 'Evidence Register',
        'gap_extraction': {
            'status_column': 'D',
            'non_compliant_value': '❌ Non-Compliant',
            'partial_value': '⚠️ Partial',
            'system_column': 'A',
            'gap_description_column': 'M',
            'remediation_column': 'N'
        }
    },
    'ISMS-IMP-A.8.24.4.xlsx': {
        'summary_sheet': 'Summary Dashboard',
        'key_cells': {
            'total_items': 'B9',
            'compliant': 'C9',
            'partial': 'D9',
            'non_compliant': 'E9',
            'na': 'F9',
            'compliance_pct': 'G9'
        },
        'assessment_sheets': [
            '1. Key Generation',
            '2. Key Storage',
            # ... 5 total sheets
        ],
        'evidence_sheet': 'Evidence Register',
        'gap_extraction': {
            'status_column': 'D',
            'non_compliant_value': '❌ Non-Compliant',
            'partial_value': '⚠️ Partial',
            'system_column': 'A',
            'gap_description_column': 'M',
            'remediation_column': 'N'
        }
    }
}
```

**Why This Matters:**

- ❌ **DON'T ASSUME** all workbooks have same structure
- ❌ **DON'T COPY-PASTE** logic from other controls without verification
- ✅ **DO DOCUMENT** actual sheet names, column positions, cell addresses
- ✅ **DO VALIDATE** each workbook exists and matches expected schema before processing

---

# Common Dashboard Structure

## File Naming

**Output Filename:** `ISMS-IMP-A.8.24.5_Compliance_Dashboard_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.8.24.5_Compliance_Dashboard_20260115.xlsx`

## Sheet Order and Purpose

| Sheet # | Sheet Name | Rows (Est.) | Purpose |
|---------|------------|-------------|---------|
| 1 | Executive Dashboard | ~90 | One-page executive summary |
| 2 | Gap Analysis | Variable | All non-compliant items from 4 assessments |
| 3 | Risk Register | Variable | Security risks derived from critical/high gaps |
| 4 | Remediation Roadmap | Variable | Action plans with timelines and budget |
| 5 | KPIs & Metrics | ~25 | Quantitative performance indicators |
| 6 | Evidence Register | Variable | Consolidated evidence from 4 assessments |
| 7 | Action Items & Follow-up | Variable | Follow-up tasks and ownership |
| 8 | Audit & Compliance Log | Variable | Compliance review history |
| 9 | Approval Sign-Off | Variable | Formal sign-off and approvals |

**Total Sheets:** 9

---

# Sheet 1: Executive Dashboard

## Purpose
Single-page compliance overview for CISO, Board, Executive Management.

## Layout Specification

**Header Section (Rows 1-10)**

**Title (Row 1):**

- **Cell A1 (merged A1:I1):** "ISMS-IMP-A.8.24.5 – Cryptography Compliance Summary Dashboard"
- **Font:** Arial 20pt, Bold, White
- **Background:** Dark Blue (003366)
- **Height:** 50px
- **Alignment:** Center, Middle

**Subtitle (Row 2):**

- **Cell A2 (merged A2:I2):** "ISO/IEC 27001:2022 - Control A.8.24: Use of Cryptography - Executive Overview"
- **Font:** Arial 12pt, White
- **Background:** Dark Blue (003366)
- **Height:** 30px
- **Alignment:** Center, Middle

**Document Information Block (Rows 4-11):**

| Row | Label (Col A) | Value (Col B-C, merged) | Format |
|-----|---------------|-------------------------|--------|
| 4 | Document ID: | ISMS-IMP-A.8.24.5 | Static text |
| 5 | Report Type: | Compliance Summary Dashboard | Static text |
| 6 | Related Policy: | ISMS-POL-A.8.24 (Use of Cryptography) | Static text |
| 7 | Version: | 1.0 | Static text |
| 8 | Report Date: | [USER INPUT - yellow] | Date picker, DD.MM.YYYY |
| 9 | Reporting Period: | [USER INPUT - yellow] | Text input, e.g., "Q4 2024" |
| 10 | Prepared By: | [USER INPUT - yellow] | Text input |
| 11 | Organization: | [USER INPUT - yellow] | Text input |
| 12 | Review Cycle: | Quarterly | Static text |
| 13 | Last Updated: | [=TODAY()] | Formula, auto-updates |

**Column Widths:**

- Column A: 25
- Column B: 15
- Column C: 30
- Columns D-I: 12 (for visual spacing)

**Cell Styling:**

- Label column (A): Bold, Gray background (D9D9D9)
- Value column (B-C): Yellow background (FFFF00) for user input, White for static/formula
- Borders: Thin black border around information block

---

**Overall Compliance Summary (Rows 15-21)**

**Section Header (Row 15):**

- **Cell A15 (merged A15:I15):** "OVERALL CRYPTOGRAPHY COMPLIANCE STATUS"
- **Font:** Arial 14pt, Bold, White
- **Background:** Dark Blue (003366)
- **Height:** 35px
- **Alignment:** Center, Middle

**Compliance Scorecard (Rows 17-20):**

| Metric (Col A-B) | Score (Col C) | Target (Col D) | Status (Col E) | Description (Col F-I) |
|------------------|---------------|----------------|----------------|-----------------------|
| Overall Compliance Rate | [Formula] | ≥95% | [Traffic Light] | Average of 4 assessment areas |
| Critical Gaps | [Formula] | 0 | [Traffic Light] | Count of Critical severity gaps |
| High-Risk Items | [Formula] | ≤5 | [Traffic Light] | Count of High severity gaps |
| Remediation Progress | [Formula] | ≥80% | [Traffic Light] | % of gaps with remediation in progress/complete |

**Formula Specifications:**

**Overall Compliance Rate (Cell C17):**
```excel
=AVERAGE('[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$G$9,
         '[ISMS-IMP-A.8.24.2.xlsx]Summary Dashboard'!$G$9,
         '[ISMS-IMP-A.8.24.3.xlsx]Summary Dashboard'!$G$9,
         '[ISMS-IMP-A.8.24.4.xlsx]Summary Dashboard'!$G$9)
```

**Note:** External workbook links require workbooks to be in same directory or use full file paths.

**Critical Gaps (Cell C18):**
```excel
=COUNTIFS('2. Gap Analysis'!$D:$D,"Critical")
```

**High-Risk Items (Cell C19):**
```excel
=COUNTIFS('2. Gap Analysis'!$D:$D,"High")
```

**Remediation Progress (Cell C20):**
```excel
=COUNTIFS('4. Remediation Roadmap'!$H:$H,"In Progress",'4. Remediation Roadmap'!$H:$H,"Completed") 
 / COUNTA('4. Remediation Roadmap'!$A:$A) * 100
```

**Conditional Formatting (Status Column E):**

**Overall Compliance Rate:**

- Green (00B050): ≥95%
- Yellow (FFC000): 85-94%
- Red (FF0000): <85%

**Critical Gaps:**

- Green (00B050): 0
- Yellow (FFC000): 1-3
- Red (FF0000): ≥4

**High-Risk Items:**

- Green (00B050): ≤5
- Yellow (FFC000): 6-15
- Red (FF0000): >15

**Remediation Progress:**

- Green (00B050): ≥80%
- Yellow (FFC000): 50-79%
- Red (FF0000): <50%

**Implementation Note:**
Use Excel conditional formatting rules with icon sets or cell fill colors. Traffic light symbols (●) with appropriate colors provide visual impact.

---

**Compliance By Assessment Area (Rows 23-30)**

**Section Header (Row 23):**

- **Cell A23 (merged A23:I23):** "COMPLIANCE BY ASSESSMENT AREA"
- **Font:** Arial 12pt, Bold, White
- **Background:** Dark Blue (003366)
- **Height:** 30px

**Column Headers (Row 25):**

| Column | Header | Width | Alignment |
|--------|--------|-------|-----------|
| A | Assessment Area | 25 | Left |
| B | Source Document | 22 | Left |
| C | Total Items | 12 | Center |
| D | Compliant | 12 | Center |
| E | Partial | 12 | Center |
| F | Non-Compliant | 14 | Center |
| G | N/A | 10 | Center |
| H | Compliance % | 14 | Center |
| I | Trend | 10 | Center |

**Header Styling:**

- Font: Arial 10pt, Bold, White
- Background: Blue (0070C0)
- Borders: Thin black
- Alignment: Center, Middle

**Data Rows (26-29):**

**Row 26: Data Transmission**

- **Assessment Area (A26):** "Data Transmission"
- **Source Document (B26):** "ISMS-IMP-A.8.24.1"
- **Total Items (C26):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$B$9`
- **Compliant (D26):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$C$9`
- **Partial (E26):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$D$9`
- **Non-Compliant (F26):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$E$9`
- **N/A (G26):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$F$9`
- **Compliance % (H26):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$G$9`
- **Trend (I26):** [USER INPUT dropdown: ↑ / → / ↓]

**Row 27: Data Storage**

- **Assessment Area (A27):** "Data Storage"
- **Source Document (B27):** "ISMS-IMP-A.8.24.2"
- **Formulas (C27:H27):** Same pattern, reference `ISMS-IMP-A.8.24.2.xlsx`
- **Trend (I27):** [USER INPUT dropdown]

**Row 28: Authentication**

- **Assessment Area (A28):** "Authentication"
- **Source Document (B28):** "ISMS-IMP-A.8.24.3"
- **Formulas (C28:H28):** Same pattern, reference `ISMS-IMP-A.8.24.3.xlsx`
- **Trend (I28):** [USER INPUT dropdown]

**Row 29: Key Management**

- **Assessment Area (A29):** "Key Management"
- **Source Document (B29):** "ISMS-IMP-A.8.24.4"
- **Formulas (C29:H29):** Same pattern, reference `ISMS-IMP-A.8.24.4.xlsx`
- **Trend (I29):** [USER INPUT dropdown]

**TOTAL Row (30):**

- **Label (A30):** "TOTAL" (Bold)
- **Source Document (B30):** "All Assessments"
- **Total Items (C30):** `=SUM(C26:C29)`
- **Compliant (D30):** `=SUM(D26:D29)`
- **Partial (E30):** `=SUM(E26:E29)`
- **Non-Compliant (F30):** `=SUM(F26:F29)`
- **N/A (G30):** `=SUM(G26:G29)`
- **Compliance % (H30):** `=AVERAGE(H26:H29)` (weighted average)
- **Trend (I30):** Leave blank

**Data Validation (Trend Column I):**
```
List source: ↑, →, ↓
```

**Conditional Formatting (Trend Column I):**

- ↑ (Green): Improved
- → (Yellow): No change
- ↓ (Red): Declined

---

**Compliance Visualization (Rows 32-50)**

**Note:** Charts and graphs are inserted manually after workbook generation using Excel's chart tools.

**Recommended Charts:**

1. **Overall Compliance Gauge Chart (Rows 32-45, Cols A-D)**

   - Chart Type: Doughnut or Speedometer
   - Data Source: Cell C17 (Overall Compliance Rate)
   - Display: 0-100%, with target line at 95%
   - Colors: Green zone (95-100%), Yellow zone (85-95%), Red zone (0-85%)

2. **Compliance by Area Bar Chart (Rows 32-45, Cols E-I)**

   - Chart Type: Horizontal Bar Chart
   - Data Source: Rows 26-29, Column H (Compliance %)
   - X-Axis: 0-100%
   - Y-Axis: 4 assessment areas
   - Target line: 95% (vertical line)

3. **Gap Distribution Pie Chart (Rows 47-50, Cols A-D)**

   - Chart Type: Pie Chart
   - Data Source: Row 30, Columns D-F (Compliant, Partial, Non-Compliant)
   - Colors: Green (Compliant), Yellow (Partial), Red (Non-Compliant)
   - Show percentages on slices

4. **Risk Level Distribution (Rows 47-50, Cols E-I)**

   - Chart Type: Stacked Bar Chart
   - Data Source: Sheet '2. Gap Analysis', Summary Statistics (Rows 4-8, Columns C-F)
   - Categories: Critical, High, Medium, Low
   - Colors: Dark Red, Orange, Yellow, Light Yellow

**Chart Data Preparation:**

For Gauge Chart, create hidden calculation cells:

- Cell K32: Overall Compliance % (=C17)
- Cell K33: Remaining % (=100-C17)

For Pie Chart:

- Use Row 30 data directly (Compliant, Partial, Non-Compliant counts)

---

**Critical Metrics Summary (Rows 52-67)**

**Section Header (Row 52):**

- **Cell A52 (merged A52:I52):** "KEY PERFORMANCE INDICATORS (KPIs)"
- **Font:** Arial 12pt, Bold, White
- **Background:** Dark Blue (003366)

**Column Headers (Row 54):**

| Column | Header | Width |
|--------|--------|-------|
| A | KPI | 35 |
| B | Current Value | 15 |
| C | Target | 12 |
| D | Status | 12 |
| E | Last Quarter | 15 |
| F | Change | 12 |
| G | Trend | 10 |

**Data Rows (55-66):**

Each KPI includes:

- **Current Value:** Formula referencing source workbooks or calculated from Gap Analysis
- **Target:** Policy-defined threshold
- **Status:** Conditional formatting (Green/Yellow/Red traffic light)
- **Last Quarter:** Manual user input (from previous quarter's dashboard)
- **Change:** Formula `=B-E` (current minus last quarter)
- **Trend:** Formula `=IF(F>0,"↑",IF(F<0,"↓","→"))`

**Example KPI Rows:**

**Row 55: Cryptographic Controls Implemented**

- **KPI (A55):** "Cryptographic Controls Implemented"
- **Current Value (B55):** `=C17` (Overall Compliance %)
- **Target (C55):** "≥95%"
- **Status (D55):** [Conditional format based on B55 vs C55]
- **Last Quarter (E55):** [USER INPUT yellow]
- **Change (F55):** `=B55-E55`
- **Trend (G55):** `=IF(F55>0,"↑",IF(F55<0,"↓","→"))`

**Row 56: Systems with Encryption at Rest**

- **KPI (A56):** "Systems with Encryption at Rest"
- **Current Value (B56):** `='[ISMS-IMP-A.8.24.2.xlsx]Summary Dashboard'!$C$9` (Compliant count from Data Storage)
- **Target (C56):** `='[ISMS-IMP-A.8.24.2.xlsx]Summary Dashboard'!$B$9` (Total items from Data Storage)
- **Status (D56):** [Conditional format: Green if B56=C56]
- **Last Quarter (E56):** [USER INPUT]
- **Change (F56):** `=B56-E56`
- **Trend (G56):** `=IF(F56>0,"↑",IF(F56<0,"↓","→"))`

**Continue pattern for all 12 KPIs** (see User Guide Section 4.5 for full KPI list)

**Conditional Formatting (Status Column D):**

- Green (00B050): Met or exceeded target
- Yellow (FFC000): Within 5% of target
- Red (FF0000): Below target by >5%

---

**Top 5 Critical Issues (Rows 69-77)**

**Section Header (Row 69):**

- **Cell A69 (merged A69:I69):** "TOP 5 CRITICAL SECURITY GAPS"
- **Font:** Arial 12pt, Bold, White
- **Background:** Red (C00000)
- **Height:** 35px

**Column Headers (Row 71):**

| Column | Header | Width |
|--------|--------|-------|
| A | Rank | 8 |
| B | Issue Description | 40 |
| C | Assessment Area | 20 |
| D | Risk Level | 12 |
| E | Systems Affected | 18 |
| F | Target Date | 12 |
| G | Owner | 18 |
| H | Status | 15 |

**Data Rows (72-76):**

**Auto-populate from Sheet '2. Gap Analysis', sorted by Risk Score descending, top 5 only.**

**Formula Approach (Python script):**
1. Extract all gaps from Gap Analysis sheet
2. Sort by Risk Level (Critical > High > Medium > Low) then by Systems Affected count
3. Take top 5
4. Populate rows 72-76

**Alternatively (Excel approach):**
Use `INDEX-MATCH` or `XLOOKUP` to pull top 5 from Gap Analysis based on Risk Level and Gap ID.

**Example Row 72:**

- **Rank (A72):** 1
- **Issue Description (B72):** [Link to '2. Gap Analysis'!B[row] where Risk Level = Critical, rank 1]
- **Assessment Area (C72):** [Link to '2. Gap Analysis'!C[row]]
- **Risk Level (D72):** "Critical"
- **Systems Affected (E72):** [Link to '2. Gap Analysis'!F[row]]
- **Target Date (F72):** [Link to '2. Gap Analysis'!K[row]]
- **Owner (G72):** [Link to '2. Gap Analysis'!L[row]]
- **Status (H72):** [Link to '2. Gap Analysis'!M[row]]

**Styling:**

- Risk Level "Critical" → Dark Red background (C00000), White text
- Risk Level "High" → Orange background (FFC000), Black text

---

**Executive Summary (Rows 79-100)**

**Section Header (Row 79):**

- **Cell A79 (merged A79:I79):** "EXECUTIVE SUMMARY"
- **Font:** Arial 12pt, Bold, White
- **Background:** Dark Blue (003366)

**Summary Content (Rows 81-100):**

This section is primarily **USER INPUT** (large text cells) for qualitative executive narrative.

**Row 81-82: Assessment Period**

- **Label (A81):** "Assessment Period:"
- **Value (B81:I81 merged):** [USER INPUT - yellow] e.g., "Q4 2024 (October 1 - December 31, 2024)"

**Row 84-85: Overall Compliance Status**

- **Label (A84):** "Overall Compliance Status:"
- **Value (B84:I84 merged):** [AUTO-CALCULATED based on C17]
  - Formula: `=IF(C17>=95,"Excellent - Mature cryptographic controls",IF(C17>=85,"Good - Minor gaps, remediation in progress",IF(C17>=75,"Needs Improvement - Significant gaps requiring attention","Critical - Immediate CISO action required")))`

**Row 87-88: Security Posture**

- **Label (A87):** "Security Posture:"
- **Value (B87:I87 merged):** [AUTO-CALCULATED based on '3. Risk Register' average risk score]
  - Formula: `=IF(AVERAGE('3. Risk Register'!H:H)<3,"Strong - Low risk exposure",IF(AVERAGE('3. Risk Register'!H:H)<5,"Adequate - Manageable risk",IF(AVERAGE('3. Risk Register'!H:H)<7,"Weak - Elevated risk requiring mitigation","Critical - Unacceptable risk exposure")))`

**Row 90-94: Key Achievements This Period**

- **Label (A90):** "Key Achievements This Period:"
- **Value (A91:I94 merged):** [USER INPUT - yellow, 4 rows tall]
- **Format:** Multi-line text box, bullet points
- **Example content:**

  ```
  • Implemented TLS 1.3 across all external HTTPS endpoints
  • Achieved 100% MFA enrollment for privileged accounts
  • Completed key rotation for 47 certificate authorities
  • Migrated 12 legacy systems from MD5 to bcrypt
  ```

**Row 96-100: Major Concerns**

- **Label (A96):** "Major Concerns:"
- **Value (A97:I100 merged):** [USER INPUT - yellow, 4 rows tall]
- **Format:** Multi-line text box, bullet points

**Row 102-106: Recommended Executive Actions**

- **Label (A102):** "Recommended Executive Actions:"
- **Value (A103:I106 merged):** [USER INPUT - yellow, 4 rows tall]
- **Format:** Numbered list (1. 2. 3. etc.)

**Row 108-112: Budget Impact**

- **Label (A108):** "Budget Impact:"
- **Value block (A109:I112):**
  - Row 109: "Total Estimated Remediation Budget:" [Formula: `=SUM('4. Remediation Roadmap'!J:J)`] 
  - Row 110: "Approved Budget:" [USER INPUT - yellow]
  - Row 111: "Budget Gap:" [Formula: `=B109-B110`]
  - Row 112: Conditional formatting: Red if gap > 0, Green if gap ≤ 0

**Cell Formatting:**

- All USER INPUT cells: Yellow background (FFFF00), Arial 10pt
- All AUTO-CALCULATED cells: Light Blue background (DCE6F1), Arial 10pt
- Labels: Bold, Gray background (D9D9D9)

---

# Sheet 2: Gap Analysis

## Purpose
Comprehensive consolidated list of ALL non-compliant and partially-compliant items from all 4 source assessments.

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1, merged A1:N1):** "COMPREHENSIVE GAP ANALYSIS - CRYPTOGRAPHIC CONTROLS"
- **Subtitle (Row 2, merged A2:N2):** "Consolidated view of all compliance gaps across assessment areas"
- **Styling:** Dark Blue header (003366), White text, Arial 14pt Bold

**Summary Statistics (Rows 4-10):**

**Column Headers (Row 4):**

| Column | Header | Width |
|--------|--------|-------|
| A | Assessment Area | 25 |
| B | Total Gaps | 12 |
| C | Critical | 12 |
| D | High | 12 |
| E | Medium | 12 |
| F | Low | 12 |
| G | Compliance % | 14 |
| H | Risk Score | 12 |

**Data Rows (5-8):**

**Row 5: Data Transmission**

- **Assessment Area (A5):** "Data Transmission"
- **Total Gaps (B5):** `=COUNTIFS('[ISMS-IMP-A.8.24.1.xlsx]1.1 External HTTPS-TLS'!$D:$D,"❌",... )`
  - Note: Must count across all 13 transmission assessment sheets
- **Critical (C5):** Count gaps where Risk Level = Critical (from source workbook or inferred from data classification)
- **Compliance % (G5):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$G$9`
- **Risk Score (H5):** `=(C5*10 + D5*7 + E5*4 + F5*1) / B5` (weighted average)

**Continue pattern for rows 6-8** (Data Storage, Authentication, Key Management)

**TOTAL Row (9):**

- **Label (A9):** "TOTAL" (Bold)
- **Formulas (B9:H9):** SUM for counts, AVERAGE for percentages/scores

**Conditional Formatting (Risk Score Column H):**

- Red (FF0000): >7 (Critical risk exposure)
- Orange (FFC000): 5-7 (High risk)
- Yellow (FFFF00): 3-5 (Medium risk)
- Green (00B050): <3 (Low risk)

---

**Detailed Gap Register (Rows 12+)**

**Column Headers (Row 12):**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gap ID | 15 | Text | Auto-generated (GAP-A824-001) |
| B | Description | 40 | Text | From source workbooks |
| C | Assessment Area | 20 | Text | Dropdown: Transmission/Storage/Auth/KeyMgmt |
| D | Risk Level | 12 | Text | Dropdown: Critical/High/Medium/Low |
| E | System/Service | 25 | Text | From source workbooks |
| F | Data Classification | 15 | Text | Dropdown: Restricted/Confidential/Internal/Public |
| G | Current State | 30 | Text | What exists now |
| H | Required State | 30 | Text | What policy requires |
| I | Evidence Location | 25 | Text | Link to evidence |
| J | Source | 18 | Text | Source workbook + sheet |
| K | Target Date | 12 | Date | DD.MM.YYYY |
| L | Owner | 18 | Text | Person responsible |
| M | Status | 15 | Text | Dropdown: Not Started/In Progress/Completed/Blocked |
| N | Notes | 30 | Text | Additional details |

**Data Population Strategy (Python Script):**

1. **Iterate through all 4 source workbooks**
2. **For each assessment sheet** in each workbook:

   - Identify rows where Status column = "❌ Non-Compliant" or "⚠️ Partial"
   - Extract: System/Service name, Gap description, Evidence location

3. **Generate Gap ID** (sequential: GAP-A824-001, GAP-A824-002, ...)
4. **Assign Risk Level** based on:

   - Data Classification (Restricted = Critical/High, Confidential = High/Medium, Internal = Medium/Low)
   - System criticality (if indicated in source workbook)

5. **Populate Target Date and Owner** from source workbook remediation columns
6. **Set Status** based on source workbook (if remediation started)

**Example Data Row:**

| Gap ID | Description | Area | Risk | System | Class | Current | Required | Evidence | Source | Target | Owner | Status | Notes |
|--------|-------------|------|------|--------|-------|---------|----------|----------|--------|--------|-------|--------|-------|
| GAP-A824-001 | Database using DES encryption | Storage | Critical | HR_Payroll | Restricted | DES-56 | AES-256 TDE | DB config | IMP-2, Sheet 4 | 31.03.2025 | J. Smith | In Progress | Migration scheduled Q1 |

**Sorting:**

- Default: By Risk Level (Critical → High → Medium → Low), then by Target Date (earliest first)

**Filtering:**

- Provide filter dropdowns on all column headers
- Common filters: Risk Level, Assessment Area, Status, Owner

---

# Sheet 3: Risk Register

## Purpose
Translate technical gaps into business risks for executive risk management.

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1):** "CRYPTOGRAPHIC RISK REGISTER"
- **Subtitle (Row 2):** "Business risks derived from cryptographic control gaps"

**Column Headers (Row 4):**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Risk ID | 12 | Text (RISK-A824-001) |
| B | Gap ID | 15 | Text (Linked to Sheet 2) |
| C | Risk Description | 40 | Text |
| D | Assessment Area | 20 | Text |
| E | Likelihood (1-5) | 15 | Number, Dropdown |
| F | Impact (1-5) | 15 | Number, Dropdown |
| G | Risk Score (L×I) | 15 | Formula |
| H | Risk Level | 12 | Text (Auto: Critical/High/Medium/Low) |
| I | Affected Assets | 25 | Text |
| J | Potential Consequences | 35 | Text |
| K | Mitigation Strategy | 35 | Text |
| L | Mitigation Owner | 18 | Text |
| M | Target Resolution | 12 | Date |
| N | Current Status | 15 | Text |

**Data Population Strategy:**

**Risks are derived from Critical and High gaps in Sheet 2.**

**Risk Scoring Formula (Column G):**
```excel
=E[row] * F[row]
```

**Risk Level (Column H):**
```excel
=IF(G[row]>=20,"Critical",IF(G[row]>=15,"High",IF(G[row]>=10,"Medium","Low")))
```

**Example Risk:**

| Risk ID | Gap ID | Description | Area | L | I | Score | Level | Assets | Consequences | Mitigation | Owner | Target | Status |
|---------|--------|-------------|------|---|---|-------|-------|--------|--------------|------------|-------|--------|--------|
| RISK-A824-001 | GAP-A824-015 | Unencrypted database backup | Storage | 4 | 5 | 20 | Critical | HR_Payroll (500 records) | GDPR breach €20M fine, reputational damage | AES-256 encryption, access restriction | J. Smith | 15.02.2025 | In Progress |

**Likelihood Assessment Guidance (Column E):**
1. Very Low (1): Theoretical only
2. Low (2): Requires sophisticated attacker
3. Medium (3): Moderate attacker skill
4. High (4): Accessible to many attackers
5. Very High (5): Trivial to exploit

**Impact Assessment Guidance (Column F):**
1. Very Low (1): Public data, minimal impact
2. Low (2): Internal data, minor disruption
3. Medium (3): Confidential data, significant disruption
4. High (4): Restricted data, major financial/reputational damage
5. Very High (5): Critical data, existential threat

**Conditional Formatting (Risk Level Column H):**

- Critical (20-25): Dark Red (C00000), White text
- High (15-19): Orange (FFC000), Black text
- Medium (10-14): Yellow (FFFF00), Black text
- Low (5-9): Light Yellow (FFFFCC), Black text
- Minimal (1-4): White, Black text

**Risk Register Auto-Population:**
Only gaps with Risk Level = Critical or High from Sheet 2 generate risks here.

---

# Sheet 4: Remediation Roadmap

## Purpose
Project plan view of gap remediation with timelines, dependencies, and budget tracking.

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1):** "CRYPTOGRAPHIC CONTROLS REMEDIATION ROADMAP"
- **Subtitle (Row 2):** "Action plans, timelines, and budget for gap closure"

**Column Headers (Row 4):**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Action ID | 12 | Text (ACT-A824-001) |
| B | Gap/Risk ID | 15 | Text (Linked to Sheet 2 or 3) |
| C | Remediation Action | 40 | Text |
| D | Assessment Area | 20 | Text |
| E | Priority | 12 | Dropdown: P1/P2/P3 |
| F | Owner | 18 | Text |
| G | Start Date | 12 | Date |
| H | Target Date | 12 | Date |
| I | Status | 15 | Dropdown |
| J | Dependencies | 25 | Text |
| K | Estimated Cost (CHF) | 15 | Currency |
| L | Actual Cost (CHF) | 15 | Currency |
| M | Progress % | 12 | Number (0-100) |
| N | Completion Date | 12 | Date |
| O | Notes | 30 | Text |

**Data Population Strategy:**

**Each gap from Sheet 2 generates one or more remediation actions.**

**Priority Assignment:**

- **P1 (Urgent):** Critical risk, Restricted data, <30 days target
- **P2 (High):** High risk, Confidential data, 30-90 days target
- **P3 (Normal):** Medium/Low risk, Internal data, >90 days target

**Status Values:**

- Not Started
- In Progress (1-99%)
- Completed (100%)
- Blocked (dependencies unmet)
- Overdue (past target date, <100%)

**Example Action:**

| Action ID | Gap ID | Action | Area | Priority | Owner | Start | Target | Status | Dependencies | Est. Cost | Actual | Progress | Completion | Notes |
|-----------|--------|--------|------|----------|-------|-------|--------|--------|--------------|-----------|--------|----------|------------|-------|
| ACT-A824-001 | GAP-A824-015 | Migrate HR_Payroll to AES-256 TDE | Storage | P1 | J. Smith | 15.01.2025 | 31.03.2025 | In Progress | PostgreSQL 13+ installed | CHF 15,000 | CHF 8,500 | 60% | - | On track, schema migration complete |

**Conditional Formatting:**

**Status Column (I):**

- Green (00B050): Completed
- Yellow (FFFF00): In Progress
- Orange (FFC000): Blocked
- Red (FF0000): Overdue

**Progress Column (M):**

- Data bars (0-100%) with color gradient: Red (0%) → Yellow (50%) → Green (100%)

**Budget Summary (Bottom Section):**

**Row [Last Row + 2]: Budget Totals**

- **Label (A):** "TOTAL REMEDIATION BUDGET"
- **Estimated (K):** `=SUM(K:K)`
- **Actual (L):** `=SUM(L:L)`
- **Variance (M):** `=L-K` (negative = under budget, positive = over budget)

**Budget Breakdown by Quarter (if applicable):**

- Q1 2025: SUM of actions with Target Date in Q1
- Q2 2025: SUM of actions with Target Date in Q2
- Q3 2025: SUM of actions with Target Date in Q3
- Q4 2025: SUM of actions with Target Date in Q4

---

# Sheet 5: KPIs & Metrics

## Purpose
Quantitative performance indicators with historical trending.

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1):** "CRYPTOGRAPHIC CONTROLS - KEY PERFORMANCE INDICATORS"
- **Subtitle (Row 2):** "Quantitative metrics for compliance monitoring and trending"

**Column Headers (Row 4):**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | KPI Name | 35 | Text |
| B | Current Value | 15 | Number/% |
| C | Target | 12 | Number/% |
| D | Status | 12 | Traffic Light |
| E | Last Quarter | 15 | Number/% |
| F | Change (Δ) | 12 | Formula |
| G | Trend | 10 | Arrow (↑↓→) |
| H | Measurement Source | 30 | Text |

**Data Rows (Full KPI List):**

**Row 5: Overall Compliance Rate**

- **KPI (A5):** "Cryptographic Controls Implemented"
- **Current (B5):** `='1. Executive Dashboard'!C17` (Overall Compliance %)
- **Target (C5):** "≥95%"
- **Status (D5):** [Conditional: Green ≥95%, Yellow 85-94%, Red <85%]
- **Last Quarter (E5):** [USER INPUT yellow]
- **Change (F5):** `=B5-E5`
- **Trend (G5):** `=IF(F5>0,"↑",IF(F5<0,"↓","→"))`
- **Source (H5):** "Average of 4 assessment areas"

**Row 6: Systems with Encryption at Rest**

- **Current (B6):** `='[ISMS-IMP-A.8.24.2.xlsx]Summary Dashboard'!$C$9 & "/" & '[ISMS-IMP-A.8.24.2.xlsx]Summary Dashboard'!$B$9`
- **Target (C6):** "100%"
- **Source (H6):** "IMP-2 Data Storage Assessment"

**Row 7: Systems with Encryption in Transit**

- **Current (B7):** `='[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$C$9 & "/" & '[ISMS-IMP-A.8.24.1.xlsx]Summary Dashboard'!$B$9`
- **Target (C7):** "100%"
- **Source (H7):** "IMP-1 Data Transmission Assessment"

**Row 8: MFA Coverage (All Users)**

- **Current (B8):** [Extract from IMP-3, Sheet 2 (MFA), Enrollment %]
- **Target (C8):** "100%"
- **Source (H8):** "IMP-3 Authentication, MFA Enrollment"

**Row 9: MFA Coverage (Privileged Accounts)**

- **Current (B9):** [Extract from IMP-3, Sheet 2 (MFA), Admin MFA Enforcement %]
- **Target (C9):** "100%"
- **Source (H9):** "IMP-3 Authentication, Admin MFA"

**Row 10: Certificate Expiry Compliance**

- **Current (B10):** [Calculate: Certificates with >90 days validity / Total certificates × 100%]
- **Target (C10):** "100%"
- **Source (H10):** "IMP-4 Key Management, Certificate Management"

**Row 11: Key Rotation Compliance**

- **Current (B11):** [Calculate: Keys rotated within policy timeframe / Total keys × 100%]
- **Target (C11):** "≥95%"
- **Source (H11):** "IMP-4 Key Management, Key Rotation"

**Row 12: Service Accounts with Strong Auth**

- **Current (B12):** [Extract from IMP-3, Sheet 4 (Service Accounts), Compliant %]
- **Target (C12):** "≥90%"
- **Source (H12):** "IMP-3 Authentication, Service Accounts"

**Row 13: Password Hashing Compliance**

- **Current (B13):** [Extract from IMP-3, Sheet 1 (Passwords), Compliant %]
- **Target (C13):** "100%"
- **Source (H13):** "IMP-3 Authentication, Password Security"

**Row 14: SSO Coverage**

- **Current (B14):** [Extract from IMP-3, Sheet 5 (SSO), Coverage %]
- **Target (C14):** "≥80%"
- **Source (H14):** "IMP-3 Authentication, SSO & Federation"

**Row 15: Open Critical Gaps**

- **Current (B15):** `=COUNTIFS('2. Gap Analysis'!$D:$D,"Critical")`
- **Target (C15):** "0"
- **Source (H15):** "Sheet 2 Gap Analysis"

**Row 16: Remediation On-Time %**

- **Current (B16):** `=COUNTIFS('4. Remediation Roadmap'!$I:$I,"Completed",'4. Remediation Roadmap'!$H:$H,"<="&TODAY()) / COUNTA('4. Remediation Roadmap'!$A:$A) * 100`
- **Target (C16):** "≥90%"
- **Source (H16):** "Sheet 4 Remediation Roadmap"

**Conditional Formatting (Trend Column G):**

- ↑ (Green): Positive trend
- → (Yellow): No change
- ↓ (Red): Negative trend

---

# Sheet 6: Evidence Register

## Purpose
Consolidated list of all compliance evidence from 4 source assessments.

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1):** "CONSOLIDATED EVIDENCE REGISTER"
- **Subtitle (Row 2):** "All compliance evidence across cryptographic control assessments"

**Column Headers (Row 4):**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Evidence ID | 12 | Text (EVD-A824-001) |
| B | Evidence Title | 35 | Text |
| C | Evidence Type | 20 | Text |
| D | Assessment Area | 20 | Text |
| E | Related System | 25 | Text |
| F | Storage Location | 30 | Text |
| G | Collection Date | 12 | Date |
| H | Collected By | 18 | Text |
| I | Retention Period | 15 | Text |
| J | Current Status | 15 | Text |
| K | Notes | 30 | Text |

**Data Population Strategy:**

**Evidence is consolidated from Evidence Register sheets in all 4 source workbooks.**

**Python Script Approach:**
1. Open each source workbook (IMP-1/2/3/4)
2. Navigate to "Evidence Register" sheet
3. Extract all rows (skip header)
4. Assign unique Evidence ID (sequential)
5. Copy to consolidated register
6. Sort by Assessment Area, then by Evidence Type

**Evidence Types:**

- Configuration File (e.g., GPO export, network config)
- Compliance Report (e.g., SSL Labs report, MDM compliance)
- Audit Log (e.g., key rotation log, access log)
- Policy Document (e.g., password policy, encryption standard)
- Screenshot (e.g., TLS settings, BitLocker status)
- Certificate (e.g., TLS certificate, CA certificate)
- Architecture Diagram (e.g., PKI hierarchy, key management flow)
- Vendor Documentation (e.g., HSM datasheet, KMS manual)

**Retention Periods:**

- **3 years:** Compliance reports, audit logs, certificates
- **7 years:** Financial records, regulatory compliance (if applicable)
- **Permanent:** Policies, architecture diagrams, certification evidence

**Status Values:**

- Current (valid and available)
- Expired (outdated, needs refresh)
- Missing (cannot locate)
- Pending Collection (identified but not yet collected)

---

# Sheet 7: Action Items & Follow-up

## Purpose
Track non-remediation tasks (training, meetings, reviews, updates).

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1):** "ACTION ITEMS & FOLLOW-UP TASKS"
- **Subtitle (Row 2):** "Non-remediation activities supporting cryptographic compliance"

**Column Headers (Row 4):**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Action ID | 12 | Text (AI-A824-001) |
| B | Action Description | 40 | Text |
| C | Category | 20 | Dropdown |
| D | Priority | 12 | Dropdown: High/Medium/Low |
| E | Owner | 18 | Text |
| F | Due Date | 12 | Date |
| G | Status | 15 | Dropdown |
| H | Completion Date | 12 | Date |
| I | Notes | 30 | Text |

**Category Values:**

- Training & Awareness
- Policy Review & Update
- Tool/Technology Evaluation
- Meeting & Governance
- Documentation Update
- Vendor Management
- Audit Preparation
- Communication

**Example Actions:**

- "Schedule cryptography awareness training for IT staff" (Training)
- "Review and update ISMS-POL-A.8.24 for annual refresh" (Policy Review)
- "Evaluate HSM vendors for Q2 procurement" (Tool Evaluation)
- "Prepare dashboard presentation for Q2 Security Review Meeting" (Meeting)

---

# Sheet 8: Audit & Compliance Log

## Purpose
Historical record of compliance reviews, audit findings, certification milestones.

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1):** "AUDIT & COMPLIANCE LOG"
- **Subtitle (Row 2):** "Historical record of cryptographic control reviews and findings"

**Column Headers (Row 4):**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Log ID | 12 | Text (LOG-A824-001) |
| B | Review Date | 12 | Date |
| C | Review Type | 20 | Dropdown |
| D | Reviewer/Auditor | 25 | Text |
| E | Scope | 30 | Text |
| F | Overall Finding | 20 | Dropdown |
| G | Non-Conformities | 15 | Number |
| H | Observations | 15 | Number |
| I | Key Findings | 40 | Text |
| J | Corrective Actions | 40 | Text |
| K | Follow-up Date | 12 | Date |
| L | Status | 15 | Dropdown |

**Review Types:**

- Internal Audit
- External Audit (ISO 27001)
- Management Review (Quarterly)
- Self-Assessment
- Surveillance Audit
- Recertification Audit

**Overall Finding Values:**

- Conformant (no issues)
- Minor Non-Conformities (correctable)
- Major Non-Conformities (significant gaps)
- Observation (improvement opportunity)

**Example Log Entry:**

- **Date:** 15.12.2024
- **Type:** ISO 27001 Stage 1 Audit
- **Auditor:** Swiss Certification Body AG
- **Scope:** Control A.8.24 Use of Cryptography
- **Finding:** Minor Non-Conformities (2)
- **Non-Conformities:** 2 (DES encryption, manual certificate renewal)
- **Key Findings:** "Strong policy framework, minor implementation gaps"
- **Corrective Actions:** "Database re-encryption Q1 2025, certificate automation Q1 2025"
- **Follow-up:** 31.03.2025 (Stage 2 Audit)
- **Status:** Open (corrective actions in progress)

---

# Sheet 9: Approval Sign-Off

## Purpose
Record formal sign-offs and approvals from management for compliance assessments, remediation plans, and policy acknowledgments.

## Layout Specification

**Header (Rows 1-2):**

- **Title (Row 1):** "APPROVAL SIGN-OFF"
- **Subtitle (Row 2):** "Formal management approval and accountability records"

**Column Headers (Row 4):**

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Approval ID | 15 | Text (APR-A824-001) |
| B | Approval Date | 12 | Date |
| C | Approval Type | 25 | Dropdown |
| D | Document/Assessment | 35 | Text |
| E | Approver Name | 20 | Text |
| F | Approver Title | 25 | Text |
| G | Approval Status | 15 | Dropdown |
| H | Comments | 40 | Text |
| I | Next Review Date | 12 | Date |

**Approval Types:**

- Quarterly Assessment Approval
- Remediation Plan Approval
- Policy Acknowledgment
- Risk Acceptance
- Budget Approval
- Audit Response Approval

**Approval Status Options:**

- Approved
- Approved with Conditions
- Pending Review
- Rejected
- Deferred

**Example Approval Entry:**

- **Approval ID:** APR-A824-001
- **Date:** 15.01.2025
- **Type:** Quarterly Assessment Approval
- **Document:** Q4 2024 Cryptography Compliance Dashboard
- **Approver:** J. Smith, CISO
- **Status:** Approved
- **Comments:** "Overall compliance acceptable. Prioritize critical gaps per remediation roadmap."
- **Next Review:** 15.04.2025

---

# Appendix: Technical Notes for Developers

## Python Script Architecture

**Script:** `generate_a824_5_compliance_summary_dashboard.py`

**Core Functions:**

1. **validate_source_workbooks()**

   - Check all 4 source workbooks exist
   - Validate file names match expected patterns
   - Verify "Summary Dashboard" sheet exists in each
   - Extract key metrics (compliance %, gap counts)

2. **extract_gaps()**

   - Iterate through all assessment sheets in each source workbook
   - Identify rows with Status = "❌ Non-Compliant" or "⚠️ Partial"
   - Extract gap details (system, description, evidence, remediation)
   - Assign Gap ID, Risk Level, Assessment Area
   - Return consolidated gap list

3. **calculate_risks()**

   - Filter gaps where Risk Level = Critical or High
   - Generate Risk ID
   - Assign Likelihood and Impact (algorithm-based or manual input)
   - Calculate Risk Score (L × I)
   - Populate Risk Register sheet

4. **generate_remediation_roadmap()**

   - For each gap, create remediation action(s)
   - Assign Action ID, Priority, Owner
   - Extract timeline from source workbook remediation columns
   - Estimate cost (if available in source, otherwise placeholder)
   - Sort by Priority then Target Date

5. **consolidate_evidence()**

   - Extract all evidence entries from 4 source workbooks
   - Assign unique Evidence ID
   - Deduplicate (if same evidence referenced in multiple assessments)
   - Sort by Assessment Area then Evidence Type

6. **generate_executive_dashboard()**

   - Create Sheet 1 with formulas linking to other sheets and source workbooks
   - Set up external workbook references
   - Apply conditional formatting
   - Create placeholder text cells for user input

7. **create_kpi_sheet()**

   - Populate KPI list with formulas
   - Link Current Value to source workbooks or calculations
   - Set up Last Quarter as user input
   - Calculate Change and Trend

8. **create_audit_and_meeting_logs()**

   - Create empty templates with headers
   - User will populate manually

## External Workbook Link Management

**Challenge:** External links (`='[file.xlsx]Sheet'!Cell`) break if source workbooks move.

**Solution Approaches:**

**Approach 1: Absolute File Paths (Current)**
```python
link_formula = f"='C:\\ISMS\\A.8.24\\Assessments\\[{filename}]Summary Dashboard'!$G$9"
```
**Pros:** Works if directory structure is consistent
**Cons:** Breaks if files move

**Approach 2: Relative File Paths**
```python
link_formula = f"='[{filename}]Summary Dashboard'!$G$9"
```
**Pros:** Works if dashboard and source workbooks in same directory
**Cons:** Less flexible for complex directory structures

**Approach 3: Python-Based Extraction (No External Links)**
```python
# Extract data at generation time, store as values (not formulas)
compliance_pct = source_wb['Summary Dashboard']['G9'].value
dashboard_wb['1. Executive Dashboard']['C17'].value = compliance_pct
```
**Pros:** No broken links, dashboard is standalone
**Cons:** Dashboard doesn't auto-update when source workbooks change, must regenerate

**Current Implementation:** Approach 2 (Relative file paths) with normalization script to ensure source workbooks have short names.

## File Normalization

**Problem:** Source workbooks have long names with dates: `ISMS-IMP-A.8.24.1_Data_Transmission_20260115.xlsx`

**Solution:** Normalization script creates short-name copies: `ISMS-IMP-A.8.24.1.xlsx`

**Script:** `normalize_assessment_files_a824.py`

```python
import shutil

files = [
    'ISMS-IMP-A.8.24.1_Data_Transmission_20260115.xlsx',
    'ISMS-IMP-A.8.24.2_Data_Storage_20260115.xlsx',
    'ISMS-IMP-A.8.24.3_Authentication_20260115.xlsx',
    'ISMS-IMP-A.8.24.4_Key_Management_20260115.xlsx'
]

for f in files:
    short_name = f.split('_')[0] + '.xlsx'  # Extract ISMS-IMP-A.8.24.X.xlsx
    shutil.copy(f, short_name)
    print(f"Created: {short_name}")
```

**Result:** Dashboard references short names, external links work.

## Testing Checklist

**Before Releasing Dashboard Script:**

- [ ] All 4 source workbooks in same directory as dashboard
- [ ] Source workbooks have normalized short names
- [ ] External links resolve (no #REF! errors)
- [ ] Overall compliance % matches average of 4 source workbooks
- [ ] Gap Analysis populated with actual gaps (not empty)
- [ ] Risk Register has entries if critical/high gaps exist
- [ ] Remediation Roadmap has actions for all gaps
- [ ] KPIs calculate correctly
- [ ] Evidence Register consolidated from all 4 sources
- [ ] Charts and visualizations display data
- [ ] Conditional formatting works (traffic lights, data bars)

## Maintenance Notes

**Quarterly Update Procedure:**
1. Update source assessments (IMP-1/2/3/4) with current data
2. Save updated assessments with new date: `*_20260415.xlsx` (Q1 2025)
3. Run normalization script to create short-name copies
4. Run dashboard generation script
5. Open dashboard in Excel, click "Update Links" when prompted
6. Manually complete Executive Summary section (user input)
7. Save dashboard as `ISMS-IMP-A.8.24.5_Compliance_Dashboard_20260415.xlsx`
8. Archive previous quarter's dashboard

**Version Control Best Practice:**

- Keep quarterly snapshots: `Q4_2024/`, `Q1_2025/`, `Q2_2025/`
- Each folder contains: Dashboard + 4 source workbooks + Evidence files
- Enables historical trending and compliance demonstration to auditors

---

**Document Assembly Instructions:**

1. **Merge Order:**

   - Document Control block (from PART I file, lines 1-30)
   - PART I: USER COMPLETION GUIDE (from PART I file, lines 31-end)
   - PART II: TECHNICAL SPECIFICATION - File 1 (this file)
   - PART II: TECHNICAL SPECIFICATION - File 2 (next file)

2. **Final Document Structure:**
   ```
   ISMS-IMP-A.8.24.5 - Compliance Summary Dashboard v2.0
   
   ├── Document Control (Metadata, Version History)
   │
   ├── PART I: USER COMPLETION GUIDE (~300 lines)
   │   ├── 1. Dashboard Overview
   │   ├── 2. Prerequisites
   │   ├── 3. Dashboard Generation Workflow
   │   ├── 4. Understanding Dashboard Sections (9 sheets explained)
   │   ├── 5. Interpreting Results
   │   ├── 6. Common Questions
   │   ├── 7. Dashboard Maintenance
   │   ├── 8. Quality Checklist
   │   └── 9. Review & Approval
   │
   └── PART II: TECHNICAL SPECIFICATION (~400 lines)
       ├── Instructions for Dashboard Development
       ├── Common Dashboard Structure
       ├── Sheet 1: Executive Dashboard
       ├── Sheet 2: Gap Analysis
       ├── Sheet 3: Risk Register
       ├── Sheet 4: Remediation Roadmap
       ├── Sheet 5: KPIs & Metrics
       ├── Sheet 6: Evidence Register
       ├── Sheet 7: Action Items & Follow-up
       ├── Sheet 8: Audit & Compliance Log
       ├── Sheet 9: Approval Sign-Off
       └── Appendix: Technical Notes for Developers
   ```

3. **Quality Checks Before Finalizing:**

   - [ ] All merge instructions removed
   - [ ] Document Control version shows 2.0
   - [ ] Version History documents v1.0 → v2.0 changes
   - [ ] All dates in DD.MM.YYYY format
   - [ ] External workbook formulas use short filenames
   - [ ] Schema validation approach documented
   - [ ] Cross-references accurate (sheet numbers, policy references)
   - [ ] No placeholder text remains
   - [ ] Technical appendix matches Python script approach

---

**END OF PART II (TECHNICAL SPECIFICATION)**

**Total IMP-5 Length:** ~650-700 lines (PART I ~300 lines + PART II ~400 lines)

**Key Distinction from IMP-1/2/3/4:**

- IMP-5 is **CONSOLIDATION**, not data entry
- Lighter weight (~700 lines vs ~1,200 lines for others)
- Executive-focused (User Guide emphasizes interpretation, not completion)
- Reads FROM source workbooks, doesn't create new assessment data

**Document Status:** ✅ READY FOR PRODUCTION

*No Cargo Cult Engineering - Dashboard provides genuine executive decision support, not compliance theater* 🎯

---

**END OF SPECIFICATION**

---

*"Every positive integer is one of Ramanujan's personal friends."*
— J.E. Littlewood, on Ramanujan

<!-- QA_VERIFIED: 2026-01-31 -->
