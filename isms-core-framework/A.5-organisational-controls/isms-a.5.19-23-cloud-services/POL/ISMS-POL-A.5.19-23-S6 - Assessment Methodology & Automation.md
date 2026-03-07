<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S6:framework:POL:a.5.19-23-s6 -->
**ISMS-POL-A.5.19-23-S6 — Assessment Methodology & Automation**
**Cloud Services Security - Systems Engineering Approach**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Assessment Methodology & Automation |
| **Document Type** | Policy Section |
| **Document ID** | ISMS-POL-A.5.19-23-S6 |
| **Document Creator** | Information Security Officer (ISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISO | Initial section covering Python-based assessment framework |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Information Security Officer (ISO)
- Technical: System Engineering Team Lead
- Quality: Quality Assurance Manager
- Final Authority: Executive Management (GL)

**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.19-23 (Parent Policy - Supplier & Cloud Services Security)
- All ISMS-IMP-A.5.19-23 implementation guidance documents
- ISMS-REF-A.5.23 (Cloud Service Provider Registry)
- Python generator scripts in 50_scripts-excel/
- ISO/IEC 27001:2022 Clause 9.2 (Internal audit)

---

# Executive Summary

## Purpose

This document defines the **Systems Engineering (SE) approach** for assessing cloud service security compliance. Instead of traditional checkbox audits, we use **Python-generated Excel workbooks** that enforce:

- **Repeatable** assessments (identical structure quarterly)
- **Quantitative** compliance metrics (87.3% compliant vs. "mostly compliant")
- **Evidence-based** verification (screenshots, configs, contracts)
- **Transparent** dashboards (auto-calculated from assessments)

## Critical Principle

**"If You Can't Generate It, You Can't Maintain It"**: Manual spreadsheets decay over time - formulas break, validations disappear, and inconsistencies emerge across assessment cycles. Copy-pasted templates drift as different stakeholders modify local versions without version control. Assessment tools must be generated programmatically to ensure consistency, repeatability, and systematic updates when requirements change. This policy uses Python generators to create Excel assessment workbooks, enabling rapid deployment, controlled modifications, and evidence-based compliance measurement with full audit trails.

**Systems Engineering Approach:**
```
1. Run Python generator → ISMS_REG_A523_1_Inventory.xlsx
2. Procurement completes service list with evidence
3. Dashboard auto-calculates: "45/78 services compliant (57.7%)"
4. Gap report identifies: "33 services missing MFA"
```

**Result:** Objective, quantitative assessment of actual compliance state, not subjective self-assessment.

---

# Framework Architecture

## Five-Layer Design

```
┌─────────────────────────────────────────────────────────────┐
│ LAYER 1: POLICY LAYER                                       │
│ • ISMS-POL-A.5.19-23 (Master Index)                         │
│ • ISMS-POL-A.5.19-23-S5 (Cloud Services Requirements)       │
│ • ISMS-POL-A.5.19-23-S6 (This document - Methodology)       │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 2: ASSESSMENT SPECIFICATIONS (Markdown)               │
│ • ISMS-IMP-A.5.19-23.S1.md - Inventory & Classification        │
│ • ISMS-IMP-A.5.19-23.S2.md - Vendor Due Diligence              │
│ • ISMS-IMP-A.5.19-23.S3.md - Secure Configuration              │
│ • ISMS-IMP-A.5.19-23.S4.md - Ongoing Governance                │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 3: IMPLEMENTATION (Python Scripts)                    │
│ • generate_reg_a523_1_inventory.py                          │
│ • generate_reg_a523_2_vendor_dd.py                          │
│ • generate_reg_a523_3_secure_config.py                      │
│ • generate_reg_a523_4_governance.py                         │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 4: REVIEW (Built-in Summary Dashboards)               │
│ • Each workbook contains its own Summary Dashboard sheet    │
│ • Review compliance metrics directly in each workbook       │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 5: SIGN-OFF (Approval & Audit Trail)                  │
│ • Approval Sign-Off sheet in each workbook                  │
│ • Evidence Register for audit traceability                  │
│ • Gap analysis and remediation planning per domain          │
└─────────────────────────────────────────────────────────────┘
```

## Assessment Workbook Structure

Each workbook follows this proven pattern:

| Sheet | Purpose | Filled By | Review Cycle |
|-------|---------|-----------|--------------|
| **Instructions & Legend** | How to use + status codes | Auto-generated | N/A |
| **Assessment Sheets (2-6)** | Domain-specific checklists | Stakeholders | Quarterly |
| **Summary Dashboard** | Compliance % per domain | Formula-driven | Auto |
| **Evidence Register** | Links to proof documents | Stakeholders | Quarterly |
| **Approval Sign-Off** | CISO approval + review dates | Management | Quarterly |

---

# Assessment Workbooks Specification

## Workbook 1: Cloud Service Inventory & Classification

**Document ID:** ISMS-IMP-A.5.19-23.S1  
**Filename:** `ISMS_REG_A523_1_Inventory_YYYYMMDD.xlsx`  
**Generated by:** `generate_reg_a523_1_inventory.py`  
**Stakeholder:** IT Operations, Procurement, Finance  
**Sheet Count:** 10 sheets

**Purpose:** Maintain authoritative inventory of all cloud services with criticality classification.

**Sheet Structure:**
1. Instructions & Legend
2. SaaS Services (Office 365, Salesforce, Zoom, etc.)
3. IaaS/PaaS Services (AWS, Azure, GCP, etc.)
4. Cloud Security Services (CrowdStrike, Zscaler, etc.)
5. Cloud Storage Services (Dropbox, Box, etc.)
6. Data Classification Mapping
7. Service Criticality Assessment
8. Summary Dashboard
9. Evidence Register
10. Approval Sign-Off

**Base Columns (17 standard A-Q):**

- A: Cloud Service Name
- B: Service Type (SaaS/IaaS/PaaS/Security/Storage)
- C: Vendor Name
- D: Service Criticality (Critical/High/Medium/Low)
- E: Data Classification (Restricted/Confidential/Internal/Public)
- F: Data Residency Region (Switzerland/EU/USA/Global)
- G: Contract Status (Active/Renewal Due/Expired)
- H: Status (✅ Compliant / ⚠️ Partial / ❌ Non-Compliant)
- I: Evidence Location
- J: Gap Description
- K: Remediation Needed (Yes/No)
- L: Exception ID
- M: Risk ID
- N: Compensating Controls
- O: Service Owner
- P: Target Remediation Date
- Q: Budget Impact (High/Medium/Low/None)

**Extended Columns (R-X for inventory-specific):**

- R: Monthly Cost (formula: validates numeric)
- S: Annual Contract Value
- T: Number of Licensed Users
- U: Integration Count (# of connected systems)
- V: Backup Service Available (Yes/No)
- W: Exit Feasibility (Easy/Medium/Hard/Unknown)
- X: Last Inventory Review Date

## Workbook 2: Vendor Due Diligence & Contracts

**Document ID:** ISMS-IMP-A.5.19-23.S2  
**Filename:** `ISMS_REG_A523_2_DueDiligence_YYYYMMDD.xlsx`  
**Generated by:** `generate_reg_a523_2_vendor_dd.py`  
**Stakeholder:** Legal, Procurement, Compliance, ISO  
**Sheet Count:** 10 sheets

**Purpose:** Track vendor security certifications, contract terms, SLAs, and audit rights.

**Sheets:**
1. Instructions & Legend
2. Vendor Security Certifications
3. Contract Terms Analysis
4. SLA Requirements & Performance
5. Data Sovereignty Compliance
6. Forensics & Incident Support
7. Right to Audit & Penetration Testing
8. Summary Dashboard
9. Evidence Register
10. Approval Sign-Off

**Extended Columns (R-X):**

- R: ISO 27001 Certified (Yes/No/Unknown + Cert #)
- S: SOC 2 Type II Report Available (Yes/No/Unknown)
- T: Contract Renewal Date
- U: SLA Availability % (99.9%, 99.95%, etc.)
- V: Right to Audit Clause (Yes/No)
- W: Data Portability Clause (Yes/No)
- X: Forensics/IR Support (Yes/No/Limited)

## Workbook 3: Secure Configuration & Deployment

**Document ID:** ISMS-IMP-A.5.19-23.S3  
**Filename:** `ISMS_REG_A523_3_Configuration_YYYYMMDD.xlsx`  
**Generated by:** `generate_reg_a523_3_secure_config.py`  
**Stakeholder:** IT Security, DevOps, System Administrators  
**Sheet Count:** 11 sheets

**Purpose:** Assess security configuration baseline compliance for deployed cloud services.

**Sheets:**
1. Instructions & Legend
2. Identity & Access Management
3. Data Encryption (At Rest & In Transit)
4. Network Security & Segmentation
5. Logging & Monitoring Configuration
6. Backup & Disaster Recovery
7. Data Classification Labeling
8. API Security & Integration
9. Summary Dashboard
10. Evidence Register
11. Approval Sign-Off

**Extended Columns (R-X):**

- R: MFA Enabled (Yes/No/Partial)
- S: Encryption at Rest (Yes/No/Unknown)
- T: Encryption in Transit (TLS 1.3/TLS 1.2/Weak)
- U: Centralized Logging (Yes/No/Partial)
- V: SSO Integration (Yes/No/Planned)
- W: Data Classification Labels Applied (Yes/No/Partial)
- X: Configuration Baseline Documented (Yes/No)

## Workbook 4: Ongoing Governance & Risk Management

**Document ID:** ISMS-IMP-A.5.19-23.S4  
**Filename:** `ISMS_REG_A523_4_Governance_YYYYMMDD.xlsx`  
**Generated by:** `generate_reg_a523_4_governance.py`  
**Stakeholder:** IT Management, Risk Management, ISO  
**Sheet Count:** 11 sheets

**Purpose:** Monitor ongoing governance, vendor risk, business continuity, and change management.

**Sheets:**
1. Instructions & Legend
2. Security Awareness & Training
3. Incident Response Procedures
4. Security Update Management
5. Vendor Lock-in Assessment
6. Vendor Lock-out Evaluation
7. Business Continuity Planning
8. Change Management Tracking
9. Summary Dashboard
10. Evidence Register
11. Approval Sign-Off

**Extended Columns (R-X):**

- R: Security Training Completed (Yes/No + Date)
- S: Last Security Review Date
- T: Incident Response Plan Tested (Yes/No/Planned)
- U: Vendor Lock-in Risk (High/Medium/Low)
- V: BC/DR Plan Exists (Yes/No)
- W: BC/DR Last Test Date
- X: Change Management Process (Yes/No)

---

# Python Generator Architecture

## Script Structure (Standard Pattern)

All generator scripts follow this modular architecture:

```python
# ============================================================================
# SECTION 1: WORKBOOK CREATION & STYLE DEFINITIONS
# ============================================================================
def create_workbook() -> Workbook:
    """Create all sheets matching specification."""
    
def setup_styles() -> dict:
    """Define colors, fonts, borders (NEW objects per cell!)."""

# ============================================================================
# SECTION 2: COLUMN DEFINITIONS (BASE + EXTENDED)
# ============================================================================
def get_base_cloud_columns() -> dict:
    """Returns 17 standard columns (A-Q) for ALL cloud assessments."""
    
def get_extended_columns_inventory() -> dict:
    """Returns domain-specific columns R-X for inventory."""

# ============================================================================
# SECTION 3: VALIDATION DEFINITIONS
# ============================================================================
def create_base_validations(ws) -> dict:
    """Create dropdown validations for standard fields."""
    
def create_extended_validations(ws, sheet_type) -> dict:
    """Create domain-specific dropdowns."""

# ============================================================================
# SECTION 4: CHECKLIST ITEM DEFINITIONS
# ============================================================================
def get_checklist_items(sheet_type) -> list:
    """Return domain-specific compliance checklist."""

# ============================================================================
# SECTION 5: REFERENCE TABLE DEFINITIONS
# ============================================================================
def get_reference_tables(sheet_type) -> dict:
    """Return lookup tables (vendors, regions, standards)."""

# ============================================================================
# SECTION 6: GENERIC ASSESSMENT SHEET BUILDER
# ============================================================================
def create_assessment_sheet(ws, styles, section_title, policy_ref, 
                           question, sheet_type):
    """Universal builder - ONE function creates ALL assessment sheets."""

# ============================================================================
# SECTION 7: SPECIALIZED SHEET CREATORS
# ============================================================================
def create_instructions_sheet(ws, styles):
def create_summary_dashboard(ws, styles):
def create_evidence_register(ws, styles):
def create_approval_signoff(ws, styles):

# ============================================================================
# SECTION 8: DOMAIN-SPECIFIC ASSESSMENT SHEETS
# ============================================================================
def create_1_saas_services(ws, styles):
def create_2_iaas_paas_services(ws, styles):
# etc

# ============================================================================
# SECTION 9: MAIN EXECUTION
# ============================================================================
def main():
    """Orchestrate workbook generation."""
```

## Critical Implementation Notes

**Style Object Best Practice:**
```python
# ❌ AVOID - Shared objects can cause Excel compatibility issues
border = Border(left=Side(style="thin"), ...)
cell1.border = border  # Reference 1
cell2.border = border  # Reference 2

# ✅ RECOMMENDED - New object per cell ensures compatibility
def apply_border(cell):
    cell.border = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin")
    )
```

**Implementation rationale:** Creating fresh style objects for each cell prevents potential Excel compatibility warnings and ensures clean workbook generation.

---

# Validation & Integration

## Processing Scripts

| Script | Purpose | When to Run |
|--------|---------|-------------|
| **generate_a523_1_inventory.py** | Generates S1 Cloud Service Inventory workbook | Before assessment cycle begins |
| **generate_a523_2_vendor_dd.py** | Generates S2 Vendor Due Diligence workbook | Before assessment cycle begins |
| **generate_a523_3_secure_config.py** | Generates S3 Secure Configuration workbook | Before assessment cycle begins |
| **generate_a523_4_governance.py** | Generates S4 Ongoing Governance workbook | Before assessment cycle begins |

## Processing Workflow

```
┌────────────────────────────────────────────────────────────┐
│ 1. Generate Workbook                                       │
│    $ python3 generate_reg_a523_1_inventory.py              │
│    Output: ISMS_REG_A523_1_Inventory_20260115.xlsx         │
└────────────────────────────────────────────────────────────┘
                         ↓
┌────────────────────────────────────────────────────────────┐
│ 2. Distribute to Stakeholders                              │
│    - Email to IT Ops, Procurement, Legal                   │
│    - Deadline: 2 weeks for completion                      │
└────────────────────────────────────────────────────────────┘
                         ↓
┌────────────────────────────────────────────────────────────┐
│ 3. Review Summary Dashboards                               │
│    Open each completed workbook and review the built-in    │
│    Summary Dashboard sheet for compliance metrics          │
└────────────────────────────────────────────────────────────┘
```

---

# Dashboard Integration

## Formula-Driven Aggregation

```excel
# Example: Count compliant services from Inventory workbook
=COUNTIF('[ISMS_REG_A523_1_Inventory_20260115.xlsx]2. SaaS Services'!$H$8:$H$50,"✅*")

# Example: Calculate compliance percentage
=IF((B4-F4)=0,"0%",ROUND(C4/(B4-F4)*100,1)&"%")
```

**Benefits:**

- **No manual updates** - change assessment → dashboard refreshes
- **Real-time metrics** - stakeholders see live compliance %
- **Audit trail** - formulas show exactly where data comes from

## Dashboard Visualizations

**Compliance Summary Table:**
| Assessment Area | Total | Compliant | Partial | Non-Compliant | N/A | Compliance % |
|-----------------|-------|-----------|---------|---------------|-----|--------------|
| Inventory       | 78    | 45        | 18      | 15            | 0   | 57.7%        |
| Vendor DD       | 78    | 62        | 10      | 6             | 0   | 79.5%        |
| Configuration   | 156   | 98        | 35      | 23            | 0   | 63.2%        |
| Governance      | 78    | 51        | 20      | 7             | 0   | 65.4%        |
| **TOTAL**       | **390** | **256** | **83** | **51**      | **0** | **65.6%** |

**Risk Heatmap:**

- High vendor lock-in + Low exit feasibility = 🔴 Critical risk
- Restricted data + Non-EU residency = 🔴 Sovereignty violation
- Critical service + No BC/DR test = 🟡 High risk

---

# Assessment Cycle & Workflow

## Quarterly Assessment Cycle

```
Week 1: GENERATION
├─ Security Engineering runs Python generators
├─ Quality review of generated workbooks
└─ Distribute to stakeholders with instructions

Weeks 2-3: ASSESSMENT
├─ IT Ops completes inventory & configuration
├─ Procurement updates vendor & contract data
├─ Legal reviews compliance & exit clauses
└─ Evidence collected (contracts, certs, screenshots)

Week 4: REVIEW
├─ ISO reviews completed assessments
├─ Gap analysis performed
├─ Remediation priorities assigned
└─ CISO approval obtained

Week 5: INTEGRATION
├─ Review Summary Dashboards
├─ Executive summary generated
└─ Board reporting package prepared
```

## Ad-Hoc Assessment Triggers

Run assessments outside quarterly cycle when:

- **New cloud service onboarding** (use Workbook 1 + 2)
- **Major configuration changes** (use Workbook 3)
- **Security incidents** (use Workbook 4 + 5)
- **Contract renewals** (use Workbook 2)
- **Audit preparation** (use all 5 workbooks)

---

# Stakeholder Guide

## Who Fills What

| Workbook | Primary | Secondary | Tertiary |
|----------|---------|-----------|----------|
| 1. Inventory | IT Operations | Procurement | Finance |
| 2. Vendor DD | Procurement | Legal | Compliance |
| 3. Configuration | IT Security | DevOps | Sys Admins |
| 4. Governance | Risk Mgmt | ISO | IT Mgmt |
| 5. Dashboard | ISO | (Auto-generated) | CISO |

## Completion Instructions

**For Each Assessment Sheet:**
1. Fill **yellow cells** with your data
2. Use **dropdown menus** (don't type freeform)
3. Provide **evidence location** (file path, link, doc ID)
4. If Status = Partial/Non-Compliant:

   - Complete **Gap Description**
   - Fill **Remediation Needed** = Yes
   - Assign **Responsible Person**
   - Set **Target Date**

5. Update **Evidence Register** with supporting docs

**Evidence Requirements:**

- ✅ Contract PDFs (vendor agreements, SLAs)
- ✅ Security certifications (ISO 27001, SOC 2 reports)
- ✅ Configuration screenshots (MFA settings, encryption)
- ✅ Audit reports (penetration tests, vulnerability scans)
- ✅ Training records (security awareness completion)
- ✅ BC/DR test results (last recovery drill report)
- ❌ "We have a process" (not acceptable without proof!)

## Assessment Sign-Off Criteria

An assessment is **ready for ISO/CISO sign-off** only when all of the following conditions are met:

| Criterion | Requirement |
|-----------|-------------|
| **Mandatory columns complete** | 100% of columns A–Q (base columns) filled for every row; N/A entries require a documented reason in the Gap Description field |
| **Evidence location specified** | Every non-N/A row has an evidence location (file path, SharePoint URL, document ID, or contract reference) — "to be provided" is not acceptable |
| **Gap descriptions specific** | All Partial or Non-Compliant rows have a Gap Description that names the specific missing control; generic text ("TBD", "under review", "in progress") is not accepted |
| **Remediation dates realistic** | Target Dates are calendar dates ≤12 months out; "ASAP" or blank are not accepted |
| **Responsible person assigned** | Every open gap has a named individual (not a team or role title), confirmed as aware of their assignment |
| **Regulatory fields complete** | If the service is DORA- or NIS2-applicable (per ISMS-POL-A.5.19-23 Section 12), the corresponding regulatory fields are filled |
| **Spot-check audit passed** | ISO performs a spot-check on a random sample of 10% of rows (minimum 5 rows) and confirms evidence is accessible and matches the stated status |

**Sign-Off Process:**

1. Assessor submits completed workbook to ISO via the document management system
2. ISO runs completeness check against all criteria above
3. Criteria met → ISO signs Approval Sign-Off sheet and records date
4. Criteria not met → ISO returns workbook with specific deficiency notes; assessor has 5 business days to remediate and resubmit
5. CISO signs off on all Level 1 supplier workbooks; ISO signs off on Level 2–4

**Minimum Acceptable Evidence Formats:**

| Evidence Type | Acceptable | Not Acceptable |
|---------------|-----------|----------------|
| Contract | Signed PDF, SharePoint link, contract ID in management system | Email thread, verbal confirmation |
| Certification | Current certificate PDF or direct public registry link | Expired certificate, vendor's self-declaration |
| Configuration | Screenshot with date and system name visible, or exported config file | Description without proof |
| Audit/pen test | Signed report from accredited/licensed body | Summary slide, executive deck |
| Training | LMS completion record with names and dates | "Training was conducted" |

---

# Continuous Improvement

## Framework Enhancement Process

**Improvement triggers:**

- Audit findings
- Stakeholder feedback
- New cloud service types
- Regulatory changes
- Technology evolution

**Process:**
1. Document issue in GitHub/Jira
2. Update markdown specification
3. Regenerate Python script
4. Test generated workbooks
5. Update this S6 document
6. Communicate changes to stakeholders

## Quality Metrics

**Framework health indicators:**

- ✅ <2 hours generation time (all 5 workbooks)
- ✅ >80% stakeholder completion rate (within 2 weeks)
- ✅ <5% error rate in completed assessments
- ✅ Zero critical findings in audit reviews
- ✅ Quarterly framework updates completed on schedule

---

# Reference Information

## Related Documents

**Policy Layer:**

- ISMS-POL-A.5.19-23 (Master Index)
- ISMS-POL-A.5.19-23-S5 (Cloud Services Security Requirements)

**Assessment Specifications:**

- ISMS-IMP-A.5.19-23.S1 - Inventory & Classification Spec
- ISMS-IMP-A.5.19-23.S2 - Vendor Due Diligence Spec
- ISMS-IMP-A.5.19-23.S3 - Secure Configuration Spec
- ISMS-IMP-A.5.19-23.S4 - Ongoing Governance Spec

**Generator Scripts:**

- generate_reg_a523_1_inventory.py
- generate_reg_a523_2_vendor_dd.py
- generate_reg_a523_3_secure_config.py
- generate_reg_a523_4_governance.py

## External Standards

- ISO/IEC 27001:2022 - Control A.5.23
- ISO/IEC 27002:2022 - Cloud security guidance
- ISO/IEC 27017:2015 - Cloud-specific controls
- ISO/IEC 27018:2019 - PII in public clouds
- NIST SP 800-144 - Guidelines on Security and Privacy in Public Cloud
- CSA Cloud Controls Matrix (CCM) v4

---

# Appendix A: Quick Reference

## Script Execution Cheat Sheet

```bash
# Generate all assessment workbooks
python3 generate_reg_a523_1_inventory.py
python3 generate_reg_a523_2_vendor_dd.py
python3 generate_reg_a523_3_secure_config.py
python3 generate_reg_a523_4_governance.py

# Review Summary Dashboards
```

---

**END OF DOCUMENT**

*"The first principle is that you must not fool yourself — and you are the easiest person to fool."*  
*— Richard Feynman*

**Translation for ISMS:** Evidence-based compliance prevents cloud washing! ☁️🔍
<!-- QA_VERIFIED: 2026-03-01 -->
