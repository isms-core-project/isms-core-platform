#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
ISMS A.8.23 Web Filtering Assessment - Complete Workflow Orchestrator
================================================================================

ISO/IEC 27001:2022 Control A.8.23: Web Filtering
End-to-End Assessment Workflow Automation

--------------------------------------------------------------------------------
WORKFLOW ORCHESTRATION SCRIPT - AUTOMATION UTILITY
--------------------------------------------------------------------------------

This is a workflow orchestration script that automates the complete A.8.23 Web
Filtering assessment lifecycle from workbook generation through data
consolidation and dashboard creation.

**Purpose:**
Simplifies the multi-step A.8.23 assessment process by providing a single
entry point for generating assessment workbooks, creating the compliance
dashboard, and consolidating user-entered data into executive reporting.

**Why Workflow Orchestration:**
- Manual execution of 6+ separate scripts is error-prone
- Easy to forget steps or run them in wrong order
- Automation ensures consistency and repeatability
- Reduces learning curve for new team members
- Enables one-command assessment generation for stakeholders

**What This Script Does:**
Orchestrates execution of the complete A.8.23 assessment workflow:

1. **Assessment Workbook Generation** (Phase 1)
   - Generates A.8.23.1: Filtering Infrastructure Assessment
   - Generates A.8.23.2: Network Coverage Assessment
   - Generates A.8.23.3: Policy Configuration Assessment
   - Generates A.8.23.4: Monitoring & Response Assessment

2. **Dashboard Generation** (Phase 2)
   - Generates A.8.23.5: Compliance Summary Dashboard
   - Automatically normalizes file names for consolidation
   - Creates executive reporting framework

3. **Data Consolidation** (Phase 3)
   - Consolidates user-entered gaps from all 4 workbooks
   - Consolidates evidence entries into unified register
   - Consolidates risk items and audit logs
   - Populates executive dashboard with actual data

**Workflow Modes:**
This script supports three operational modes for different use cases:

**Mode 1: Full Workflow (Interactive)**
- Generates all 4 assessment workbooks
- Pauses for users to fill out workbooks
- Generates dashboard and consolidates data
- Use Case: Complete end-to-end assessment from scratch

**Mode 2: Workbooks Only**
- Generates only the 4 assessment workbooks
- Does NOT generate dashboard or consolidate
- Use Case: Initial deployment, distribute workbooks to teams

**Mode 3: Dashboard + Consolidation**
- Assumes workbooks already completed
- Generates dashboard and consolidates user data
- Use Case: After teams have filled out assessment workbooks

**Mode 4: Consolidation Only**
- Assumes dashboard already exists
- Re-consolidates data from workbooks
- Use Case: After users update workbook data, refresh dashboard

**Integration with Manual Workflow:**
This orchestrator can be used alongside manual execution of individual scripts:

Manual Approach:
```bash
python3 generate_a823_1_filtering_infrastructure.py
python3 generate_a823_2_network_coverage.py
python3 generate_a823_3_policy_configuration.py
python3 generate_a823_4_monitoring_response.py
# Users fill out workbooks
python3 generate_a823_5_compliance_dashboard.py
python3 consolidate_a823_dashboard.py ISMS-IMP-A.8.23.5_*.xlsx
```

Orchestrated Approach:
```bash
python3 complete_workflow_a823.py
# Select appropriate mode
```

Both approaches produce identical results; orchestration just simplifies execution.

--------------------------------------------------------------------------------
USAGE
--------------------------------------------------------------------------------

Interactive Mode (Recommended for First Use):
    python3 complete_workflow_a823.py
    
    # Interactive prompts guide you through options:
    # - Full workflow (with pause for user data entry)
    # - Workbooks only
    # - Dashboard + consolidation
    # - Consolidation only
    # - Quit

Non-Interactive Mode (Automation/Scripting):
    # Full workflow with user interaction
    python3 complete_workflow_a823.py
    # Type 'y' at prompt for full workflow
    
    # Or use environment variable to skip prompts (future enhancement)
    # A823_WORKFLOW_MODE=workbooks python3 complete_workflow_a823.py

Typical Usage Scenarios:

**Scenario 1: New Assessment (First Time)**
```bash
# Step 1: Generate workbooks for teams to fill out
python3 complete_workflow_a823.py
# Select option: 1 - Generate workbooks only

# Step 2: Distribute workbooks to teams
# - Infrastructure team completes A.8.23.1
# - Network team completes A.8.23.2
# - Security team completes A.8.23.3
# - SOC team completes A.8.23.4

# Step 3: After teams complete workbooks, generate dashboard
python3 complete_workflow_a823.py
# Select option: 2 - Generate dashboard + consolidate
```

**Scenario 2: Updating Existing Assessment**
```bash
# Teams update their workbooks with current data
# Then refresh dashboard with updated data
python3 complete_workflow_a823.py
# Select option: 3 - Consolidate only
```

**Scenario 3: Demo/Testing (Full Workflow)**
```bash
# Generate everything, manually fill workbooks during pause
python3 complete_workflow_a823.py
# Select: y (full workflow)
# Fill out workbooks during interactive pause
# Press ENTER to continue with dashboard generation
```

Output:
    Generated Files:
    - ISMS-IMP-A.8.23.1_Filtering_Infrastructure_YYYYMMDD.xlsx
    - ISMS-IMP-A.8.23.2_Network_Coverage_YYYYMMDD.xlsx
    - ISMS-IMP-A.8.23.3_Policy_Configuration_YYYYMMDD.xlsx
    - ISMS-IMP-A.8.23.4_Monitoring_Response_YYYYMMDD.xlsx
    - ISMS-IMP-A.8.23.5_Compliance_Summary_Dashboard_YYYYMMDD.xlsx

    Console Output:
    - Progress indicators for each generation step
    - Success/failure status for each phase
    - Final summary with next steps

Exit Codes:
    0 = Workflow completed successfully
    1 = Workflow failed at some step (see console output)

--------------------------------------------------------------------------------
REQUIREMENTS
--------------------------------------------------------------------------------

System Requirements:
    - Python 3.8 or higher
    - openpyxl library (for all generator scripts)
    - All A.8.23 generator scripts in same directory

Installation:
    Ubuntu/Debian:
        sudo apt install python3-openpyxl
    
    Or via pip:
        pip3 install openpyxl

Required Scripts (Must Be Present):
    - generate_a823_1_filtering_infrastructure.py
    - generate_a823_2_network_coverage.py
    - generate_a823_3_policy_configuration.py
    - generate_a823_4_monitoring_response.py
    - generate_a823_5_compliance_dashboard.py
    - consolidate_a823_dashboard.py

Optional Scripts (Recommended for QA):
    - sanity_check_a823_dashboard.py (pre-flight validation)
    - excel_sanity_check_a823.py (workbook validation)
    - normalize_assessment_files_a823.py (file normalization)

Dependencies:
    - subprocess (standard library - command execution)
    - sys (standard library - exit codes)
    - os (standard library - file operations)
    - datetime (standard library - timestamps)
    - glob (standard library - file pattern matching)

--------------------------------------------------------------------------------
WORKFLOW PHASES
--------------------------------------------------------------------------------

**Phase 1: Assessment Workbook Generation**
Duration: 30-60 seconds total (all 4 workbooks)
Steps:
1. Executes generate_a823_1_filtering_infrastructure.py
2. Executes generate_a823_2_network_coverage.py
3. Executes generate_a823_3_policy_configuration.py
4. Executes generate_a823_4_monitoring_response.py

Output: 4 Excel workbooks ready for user data entry

**Phase 2: User Data Entry** (Manual - Not Automated)
Duration: Varies (hours to days depending on organization)
Steps:
1. Infrastructure team completes A.8.23.1 workbook
2. Network team completes A.8.23.2 workbook
3. Security policy team completes A.8.23.3 workbook
4. Security operations team completes A.8.23.4 workbook

Note: This script can pause at this phase (Mode 1) or be run after completion (Mode 2)

**Phase 3: Dashboard Generation**
Duration: 15-30 seconds
Steps:
1. Executes generate_a823_5_compliance_dashboard.py
2. Automatically normalizes file names
3. Creates executive summary framework

Output: Compliance dashboard workbook with formulas and structure

**Phase 4: Data Consolidation**
Duration: 5-10 seconds
Steps:
1. Executes consolidate_a823_dashboard.py
2. Reads user-entered data from all 4 workbooks
3. Populates dashboard with consolidated information
4. Updates executive summary with actual compliance status

Output: Complete dashboard with all user data consolidated

--------------------------------------------------------------------------------
ERROR HANDLING
--------------------------------------------------------------------------------

**Script Execution Failures:**
If any generator script fails, the workflow:
- Stops immediately (fail-fast approach)
- Displays error output from failed script
- Returns exit code 1
- Requires manual investigation before retry

**Missing Files:**
If required generator scripts are missing:
- Error occurs when attempting to execute missing script
- Clear error message indicates which script is missing
- Workflow aborts with exit code 1

**Partial Generation:**
If workflow stops mid-execution:
- Already-generated files remain valid
- Can restart workflow (will regenerate with new timestamps)
- Or manually complete remaining steps

**Consolidation Failures:**
If consolidation fails (dashboard not found, workbooks incomplete):
- Error message indicates specific issue
- Dashboard may be partially populated
- Can retry consolidation after fixing issue (Mode 4)

--------------------------------------------------------------------------------
INTEGRATION WITH A.8.23 FRAMEWORK
--------------------------------------------------------------------------------

This orchestration script is the recommended entry point for A.8.23 assessments:

**Standard Assessment Lifecycle:**
```
New Assessment:
  complete_workflow_a823.py (Mode 1: Workbooks Only)
       ↓
  Distribute to Teams
       ↓
  Teams Fill Out Workbooks
       ↓
  complete_workflow_a823.py (Mode 2: Dashboard + Consolidate)
       ↓
  Review Dashboard
       ↓
  Present to Stakeholders

Update Existing Assessment:
  Teams Update Workbooks
       ↓
  complete_workflow_a823.py (Mode 3: Consolidate Only)
       ↓
  Review Updated Dashboard
```

**Related Scripts:**
Generator Scripts:
- generate_a823_1_filtering_infrastructure.py
- generate_a823_2_network_coverage.py
- generate_a823_3_policy_configuration.py
- generate_a823_4_monitoring_response.py
- generate_a823_5_compliance_dashboard.py

Consolidation Scripts:
- consolidate_a823_dashboard.py

Quality Assurance Scripts:
- sanity_check_a823_dashboard.py (pre-flight check)
- excel_sanity_check_a823.py (workbook validation)

Utility Scripts:
- normalize_assessment_files_a823.py (file normalization)

**Position in Workflow:**
This orchestrator sits at the TOP level, calling all other scripts as needed.
It does not replace individual scripts - those can still be run manually.

--------------------------------------------------------------------------------
METADATA
--------------------------------------------------------------------------------

Control Reference:    ISO/IEC 27001:2022 Annex A Control A.8.23
Script Type:          Workflow Orchestration / Automation Utility
Framework Component:  A.8.23 Complete Assessment Lifecycle
Framework Version:    1.0
Script Version:       1.0
Author:               [Developer Name / Organisation]
Date:                 [Date to be set]
Last Modified:        [Date to be set]
Python Version:       3.8+
License:              [Organisation License/Terms]

Orchestrates:
    - ISMS-IMP-A.8.23.1: Filtering Infrastructure Assessment
    - ISMS-IMP-A.8.23.2: Network Coverage Assessment
    - ISMS-IMP-A.8.23.3: Policy Configuration Assessment
    - ISMS-IMP-A.8.23.4: Monitoring & Response Assessment
    - ISMS-IMP-A.8.23.5: Compliance Dashboard
    - consolidate_a823_dashboard.py: Data consolidation

Related Documentation:
    - ISMS-POL-A.8.23: Web Filtering Policy
    - ISMS-IMP-A.8.23.1 through A.8.23.5: Implementation Guides
    - All generator script documentation

--------------------------------------------------------------------------------
CHANGE HISTORY
--------------------------------------------------------------------------------

Version 1.0 - [Date to be set]
    - Initial release
    - Implements three workflow modes (workbooks, dashboard, consolidate)
    - Interactive mode with user prompts
    - Full error handling and status reporting
    - Support for partial workflow execution

[Future changes to be documented here]

Future Enhancements:
    - Environment variable support for non-interactive automation
    - Pre-flight quality checks (call sanity_check_a823_dashboard.py)
    - Post-generation validation (call excel_sanity_check_a823.py)
    - Parallel workbook generation for faster execution
    - Email notifications on completion
    - Progress bars for long-running operations
    - Configuration file for customizing workflow steps

--------------------------------------------------------------------------------
IMPORTANT NOTES
--------------------------------------------------------------------------------

**Not a Replacement for Individual Scripts:**
This orchestrator provides convenience, not replacement. Individual generator
scripts can and should still be run manually when needed for:
- Regenerating single workbook after script updates
- Testing individual generator modifications
- Debugging specific workbook generation issues

**Interactive Pause in Full Workflow:**
The full workflow (Mode 1) includes an interactive pause between workbook
generation and dashboard creation. This allows users to fill out workbooks
before consolidation. For fully automated workflows, use Mode 1 (workbooks)
then Mode 2 (dashboard) in separate executions.

**File Naming and Timestamps:**
Each execution generates files with new timestamps (YYYYMMDD). This means:
- Running workflow multiple times creates multiple file sets
- Latest files sorted alphabetically are newest
- Consider cleaning up old assessment files periodically

**Error Recovery:**
If workflow fails mid-execution:
- Already-generated files are valid and can be used
- Fix the issue causing failure
- Re-run workflow from beginning OR
- Complete remaining steps manually

**Consolidation Data Source:**
Consolidation reads from the 4 assessment workbooks that users fill out.
Ensure users save their workbooks before running consolidation, otherwise
dashboard will show empty or default data.

**Quality Assurance Integration:**
For production use, consider adding QA steps:
```bash
# Pre-flight check before dashboard generation
python3 sanity_check_a823_dashboard.py || exit 1

# Workbook validation after generation
python3 excel_sanity_check_a823.py ISMS-IMP-A.8.23.1_*.xlsx
python3 excel_sanity_check_a823.py ISMS-IMP-A.8.23.2_*.xlsx
python3 excel_sanity_check_a823.py ISMS-IMP-A.8.23.3_*.xlsx
python3 excel_sanity_check_a823.py ISMS-IMP-A.8.23.4_*.xlsx
python3 excel_sanity_check_a823.py ISMS-IMP-A.8.23.5_*.xlsx
```

**Best Practices:**
- Use Mode 1 (workbooks only) for initial deployment
- Distribute workbooks to appropriate teams/SMEs
- Allow sufficient time for data entry (days/weeks)
- Use Mode 2 (dashboard + consolidate) after data entry complete
- Use Mode 3 (consolidate only) for dashboard refreshes
- Keep all generated files in same directory for consolidation
- Archive completed assessments with date stamps

**Audit Considerations:**
This workflow automation provides audit evidence of systematic, repeatable
assessment processes. Maintain logs of workflow executions and keep all
generated files for audit trail.

**Performance:**
- Workbook generation: ~30-60 seconds total
- Dashboard generation: ~15-30 seconds
- Data consolidation: ~5-10 seconds
- Total workflow: ~1-2 minutes (excluding user data entry)

**Customization:**
To customize workflow steps, edit this script or call individual generator
scripts directly. This orchestrator is designed for the standard workflow;
variations may require manual execution.

--------------------------------------------------------------------------------
TROUBLESHOOTING
--------------------------------------------------------------------------------

**Problem: "Command not found" or script execution fails**
Solution: Ensure all generator scripts are in same directory and are executable

**Problem: "Workbooks already exist" or timestamp conflicts**
Solution: Generated files include timestamps, so multiple runs create new files.
Delete old files or move to archive directory.

**Problem: Consolidation shows empty dashboard**
Solution: Users must save workbooks after filling them out. Check that workbook
files contain actual user data, not just empty templates.

**Problem: Dashboard not found during consolidation**
Solution: Ensure dashboard generation completed successfully before attempting
consolidation. Check for ISMS-IMP-A.8.23.5_*.xlsx file in directory.

**Problem: Want to skip interactive prompts**
Solution: Currently requires manual interaction. Future enhancement will support
environment variables for automation. For now, use individual scripts for
fully automated workflows.

**Problem: One workbook generation fails, others succeed**
Solution: Workflow uses fail-fast approach. Fix failing script and re-run
entire workflow. Already-generated files will be regenerated with new timestamps.

**Problem: Need to regenerate only one workbook**
Solution: Run individual generator script directly rather than using workflow
orchestrator:
```bash
python3 generate_a823_3_policy_configuration.py
```

**Problem: Consolidation fails with "file not found"**
Solution: Ensure all 4 assessment workbooks exist in current directory with
expected naming pattern: ISMS-IMP-A.8.23.N_*_YYYYMMDD.xlsx

================================================================================
END OF HEADER - SCRIPT CODE FOLLOWS
================================================================================
"""

import subprocess
import sys
import os
from datetime import datetime

def run_command(cmd, description):
    """Run a command and report status"""
    print(f"\n{'='*80}")
    print(f"{description}")
    print(f"{'='*80}")
    print(f"Command: {' '.join(cmd)}")
    print()
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        # Show last 15 lines of output
        lines = result.stdout.strip().split('\n')
        for line in lines[-15:]:
            print(line)
        print(f"\n✅ {description} - SUCCESS")
        return True
    else:
        print(f"\n❌ {description} - FAILED")
        print(result.stderr)
        return False

def main():
    print("="*80)
    print("ISMS A.8.23 WEB FILTERING ASSESSMENT - COMPLETE WORKFLOW")
    print("="*80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    print("This workflow will:")
    print("  1. Generate 4 assessment workbooks (for users to fill out)")
    print("  2. Generate consolidated dashboard (with auto-normalization)")
    print("  3. Consolidate all user-entered data into dashboard")
    print()
    print("NOTE: After Step 1, users should fill out the 4 workbooks")
    print("      before running Steps 2-3.")
    print()
    print("="*80)
    
    choice = input("\nRun full workflow now? (y/n): ")
    if choice.lower() != 'y':
        print("\nWorkflow options:")
        print("  1 - Generate workbooks only")
        print("  2 - Generate dashboard + consolidate (assumes workbooks filled)")
        print("  3 - Consolidate only (assumes dashboard exists)")
        print("  q - Quit")
        
        option = input("\nSelect option: ")
        
        if option == '1':
            # Generate workbooks only
            generate_workbooks_only()
        elif option == '2':
            # Generate dashboard and consolidate
            generate_dashboard_and_consolidate()
        elif option == '3':
            # Consolidate only
            consolidate_only()
        else:
            print("\nAborted.")
        return
    
    # Full workflow
    run_full_workflow()

def generate_workbooks_only():
    """Generate the 4 assessment workbooks only"""
    print("\n\n" + "🔷"*40)
    print("PHASE 1: GENERATING ASSESSMENT WORKBOOKS")
    print("🔷"*40)
    
    workbooks = [
        ("generate_a823_1_filtering_infrastructure.py", "Filtering Infrastructure Workbook"),
        ("generate_a823_2_network_coverage.py", "Network Coverage Workbook"),
        ("generate_a823_3_policy_configuration.py", "Policy Configuration Workbook"),
        ("generate_a823_4_monitoring_response.py", "Monitoring & Response Workbook"),
    ]
    
    for script, name in workbooks:
        if not run_command([sys.executable, script], f"Generating {name}"):
            print("\n❌ Workflow failed. Aborting.")
            return 1
    
    print("\n" + "="*80)
    print("✅ WORKBOOKS GENERATED")
    print("="*80)
    print("\n📋 Next Steps:")
    print("  1. Users fill out the 4 generated workbooks:")
    print("     - ISMS-IMP-A.8.23.1_Filtering_Infrastructure_YYYYMMDD.xlsx")
    print("     - ISMS-IMP-A.8.23.2_Network_Coverage_YYYYMMDD.xlsx")
    print("     - ISMS-IMP-A.8.23.3_Policy_Configuration_YYYYMMDD.xlsx")
    print("     - ISMS-IMP-A.8.23.4_Monitoring_Response_YYYYMMDD.xlsx")
    print("\n  2. After filling out workbooks, run:")
    print("     python3 workflow_a823.py")
    print("     Select option 2 to generate dashboard and consolidate")
    print("="*80 + "\n")
    return 0

def generate_dashboard_and_consolidate():
    """Generate dashboard and consolidate data"""
    print("\n\n" + "🔶"*40)
    print("PHASE 1: GENERATING DASHBOARD (Auto-Normalizing)")
    print("🔶"*40)
    
    if not run_command([sys.executable, "generate_a823_5_compliance_dashboard.py"], "Generating Dashboard"):
        print("\n❌ Workflow failed. Aborting.")
        return 1
    
    # Find the generated dashboard file
    import glob
    dashboard_files = glob.glob("ISMS-IMP-A.8.23.5_Compliance_Summary_Dashboard_*.xlsx")
    if not dashboard_files:
        print("\n❌ ERROR: Dashboard file not found after generation")
        return 1
    
    dashboard_file = sorted(dashboard_files)[-1]  # Most recent
    
    print("\n\n" + "🔷"*40)
    print("PHASE 2: CONSOLIDATING DATA FROM WORKBOOKS")
    print("🔷"*40)
    
    if not run_command([sys.executable, "consolidate_a823_dashboard.py", dashboard_file], "Consolidating Dashboard"):
        print("\n❌ Workflow failed. Aborting.")
        return 1
    
    print("\n" + "="*80)
    print("🎉 WORKFLOW COMPLETE!")
    print("="*80)
    print(f"\n✅ Dashboard ready: {dashboard_file}")
    print("\n📊 Dashboard contains:")
    print("  • All gaps from 4 assessment workbooks")
    print("  • All evidence entries")
    print("  • All risk items")
    print("  • All audit logs")
    print("  • Executive Dashboard with live formulas")
    print("\n🎯 Ready for CISO presentation!")
    print("="*80 + "\n")
    return 0

def consolidate_only():
    """Consolidate data into existing dashboard"""
    import glob
    
    dashboard_files = glob.glob("ISMS-IMP-A.8.23.5_Compliance_Summary_Dashboard_*.xlsx")
    if not dashboard_files:
        print("\n❌ ERROR: No dashboard file found")
        print("   Run option 2 first to generate dashboard")
        return 1
    
    dashboard_file = sorted(dashboard_files)[-1]
    
    print(f"\n📊 Using dashboard: {dashboard_file}")
    
    if not run_command([sys.executable, "consolidate_a823_dashboard.py", dashboard_file], "Consolidating Dashboard"):
        print("\n❌ Consolidation failed.")
        return 1
    
    print("\n" + "="*80)
    print("✅ CONSOLIDATION COMPLETE")
    print("="*80 + "\n")
    return 0

def run_full_workflow():
    """Run the complete end-to-end workflow"""
    
    # Step 1: Generate workbooks
    result = generate_workbooks_only()
    if result != 0:
        return result
    
    # Step 2: Generate dashboard and consolidate
    input("\n⚠️  PAUSE: Users should now fill out the 4 workbooks.\n   Press ENTER when ready to continue with dashboard generation...")
    
    result = generate_dashboard_and_consolidate()
    return result

if __name__ == "__main__":
    sys.exit(main())
