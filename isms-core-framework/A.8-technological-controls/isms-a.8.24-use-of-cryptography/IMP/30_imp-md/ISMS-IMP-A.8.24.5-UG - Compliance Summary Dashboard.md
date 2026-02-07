**ISMS-IMP-A.8.24.5-UG - Compliance Summary Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography

---

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.24.5-UG |
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


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
