# A.8.12 DLP Dashboard Consolidation - Usage Guide

## Quick Start

```bash
# Step 1: Generate 4 assessment workbooks
python3 generate_a812_1_dlp_infrastructure.py
python3 generate_a812_2_data_classification.py
python3 generate_a812_3_channel_coverage.py
python3 generate_a812_4_monitoring_response.py

# Step 2: User fills in the 4 assessments (manual work)

# Step 3: Generate dashboard template
python3 generate_a812_5_compliance_dashboard.py

# Step 4: Run consolidation (populates detail sheets)
python3 consolidate_a812_dashboard.py ISMS-IMP-A.8.12.5_Compliance_Dashboard_20260117.xlsx

# Done! Complete dashboard ready for CISO presentation
```

---

## What the Consolidation Script Does

### 1. Extracts Gaps (from all 4 workbooks)
- Scans assessment sheets for `[!] Partial` and `[X] Non-Compliant` status
- Extracts: System, Gap Description, Severity
- Creates structured gap entries with Gap IDs

### 2. Extracts Evidence (from Evidence_Register sheets)
- Reads all evidence entries from each workbook
- Consolidates into master Evidence_Master_Index

### 3. Generates Risks (automatically from High severity gaps)
- Creates risk entries for all High severity gaps
- Assigns Risk IDs, calculates risk scores
- Links back to Gap IDs

### 4. Generates Remediation (automatically from all gaps)
- Creates remediation actions for every gap
- Calculates target dates:
  - Critical: 30 days
  - High: 60 days
  - Medium: 90 days
- Links back to Gap IDs

### 5. Populates Dashboard Sheets
- **Consolidated_Gap_Analysis** (starts row 6)
- **Risk_Register** (starts row 9 - skips example risks)
- **Remediation_Roadmap** (starts row 4)
- **Evidence_Master_Index** (starts row 4)

---

## File Requirements

**Must be in same directory:**
```
ISMS-IMP-A.8.12.1.xlsx    # Domain 1: Infrastructure
ISMS-IMP-A.8.12.2.xlsx    # Domain 2: Classification
ISMS-IMP-A.8.12.3.xlsx    # Domain 3: Channels
ISMS-IMP-A.8.12.4.xlsx    # Domain 4: Monitoring
ISMS-IMP-A.8.12.5_Compliance_Dashboard_YYYYMMDD.xlsx
```

---

## Output Structure

### Consolidated_Gap_Analysis
| Domain | Gap ID | Gap Description | Severity | Current State | Target State | Owner | Status |
|--------|--------|-----------------|----------|---------------|--------------|-------|--------|

### Risk_Register
| Risk ID | Domain | Risk Description | Category | Likelihood | Impact | Risk Score | Inherent | Residual | Status |
|---------|--------|------------------|----------|------------|--------|------------|----------|----------|--------|

### Remediation_Roadmap
| Action ID | Domain | Action Description | Priority | Owner | Start Date | Target Date | Actual Date | Budget | Status |
|-----------|--------|-------------------|----------|-------|------------|-------------|-------------|--------|--------|

### Evidence_Master_Index
| Evidence ID | Domain | Control/Requirement | Evidence Type | File Location | Collected Date | Verified By | Status |
|-------------|--------|---------------------|---------------|---------------|----------------|-------------|--------|

---

## Intelligence Built-In

### Automatic Risk Generation
- Only High severity gaps become risks
- Risk category: "Technical"
- Likelihood/Impact: High/High
- Status: Active

### Automatic Remediation Planning
- Priority mapping:
  - `[X] Non-Compliant` → Critical → 30 days
  - `[!] Partial` → High → 60 days
  - Other → Medium → 90 days
- Start date: Today
- Status: Planned

### Gap ID Format
```
GAP-1-001    # Domain 1, Gap #1
GAP-2-015    # Domain 2, Gap #15
GAP-3-007    # Domain 3, Gap #7
GAP-4-042    # Domain 4, Gap #42
```

---

## Differences from A.8.23/A.8.24

### Sheet Names
- A.8.12: `Consolidated_Gap_Analysis` (vs `Gap Analysis`)
- A.8.12: `Evidence_Master_Index` (vs `Evidence Register`)

### Domain Naming
- A.8.12: "Domain 1 - Infrastructure" (not "Data Transmission")
- Specific to DLP context

### Column Structure
- Gap Analysis: 8 columns (A-H)
- Risk Register: 10 columns (A-J)
- Remediation: 10 columns (A-J)
- Evidence: 8 columns (A-H)

---

## Notes

- **Executive Summary sheet:** Uses external formulas - NOT touched by consolidation
- **Example risks:** Rows 4-8 in Risk_Register have examples - consolidation starts at row 9
- **Pure ASCII:** All output uses ASCII tags ([OK], [X], [!]) instead of Unicode
- **Error handling:** Script validates source workbooks exist before processing

---

## Expected Output

```
================================================================================
A.8.12 DLP COMPREHENSIVE DASHBOARD POPULATION
================================================================================

[1/4] Extracting gaps from source workbooks...
  * Domain 1 - Infrastructure: 12 gaps
  * Domain 2 - Classification: 8 gaps
  * Domain 3 - Channels: 15 gaps
  * Domain 4 - Monitoring: 6 gaps

  Total gaps identified: 41

[2/4] Extracting evidence from source workbooks...
  * Domain 1 - Infrastructure: 5 evidence docs
  * Domain 2 - Classification: 3 evidence docs
  * Domain 3 - Channels: 7 evidence docs
  * Domain 4 - Monitoring: 4 evidence docs

  Total evidence collected: 19

[3/4] Generating risks and remediation...
  * Risks generated: 18
  * Remediation actions: 41

[4/4] Writing to dashboard...
  [OK] Consolidated_Gap_Analysis: 41 entries
  [OK] Risk_Register: 18 entries
  [OK] Remediation_Roadmap: 41 entries
  [OK] Evidence_Master_Index: 19 entries

[BACKUP] Saved: ISMS-IMP-A.8.12.5_Compliance_Dashboard_20260117.xlsx

================================================================================
[OK] A.8.12 DLP DASHBOARD POPULATION COMPLETE
================================================================================

Summary:
  * Consolidated Gap Analysis: 41 gaps identified
  * Risk Register: 18 risks documented
  * Remediation Roadmap: 41 actions planned
  * Evidence Master Index: 19 evidence documents

  Total Data Points: 119

[ROCKET] Dashboard is now CISO-presentation ready!
================================================================================
```

---

## Troubleshooting

**Error: Missing source workbooks**
- Ensure all 4 assessment files are in same directory
- Check filenames match exactly: `ISMS-IMP-A.8.12.X.xlsx`

**Error: Dashboard file not found**
- Generate dashboard first: `python3 generate_a812_5_compliance_dashboard.py`

**No gaps extracted**
- Check assessment workbooks have status markers: `[!] Partial` or `[X] Non-Compliant`
- Verify data is in rows 8-100 of assessment sheets

**Empty evidence**
- Check assessment workbooks have `Evidence_Register` sheet
- Verify evidence IDs start with "EVD-"

---

**Script ready for production use!** ✓
