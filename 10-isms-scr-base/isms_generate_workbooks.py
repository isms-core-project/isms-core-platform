#!/usr/bin/env python3
"""
ISMS Script: Generate Workbooks (Final Version)
Purpose: Run generator scripts and create detailed error log
"""

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime


def run_generator_scripts(control_path: Path, generator_folder: str, error_log: list) -> dict:
    """
    Run all Python generator scripts in the specified folder.
    
    Returns dict with: scripts_run, scripts_failed
    """
    generator_path = control_path / generator_folder
    
    if not generator_path.exists():
        error_log.append({
            "control": control_path.name,
            "script": "N/A",
            "error": f"Generator folder not found: {generator_folder}"
        })
        return {"scripts_run": 0, "scripts_failed": 0}
    
    # Find all Python generator scripts (excluding .bak.py files)
    all_scripts = sorted(generator_path.glob("generate*.py"))
    generator_scripts = [s for s in all_scripts if not s.name.endswith('.bak.py')]
    
    if not generator_scripts:
        error_log.append({
            "control": control_path.name,
            "script": "N/A",
            "error": "No generator scripts found"
        })
        return {"scripts_run": 0, "scripts_failed": 0}
    
    print(f"\n📂 {control_path.name}")
    print(f"   Generator: {generator_folder}")
    print(f"   Scripts: {len(generator_scripts)}")
    
    completed = 0
    failed = 0
    
    # Run each generator script
    for script in generator_scripts:
        script_name = script.name
        
        try:
            # Run the script from its parent directory
            result = subprocess.run(
                ["python3", script.name],
                cwd=generator_path,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            if result.returncode != 0:
                # Log detailed error
                error_log.append({
                    "control": control_path.name,
                    "script": script_name,
                    "error": result.stderr.strip()
                })
                
                # Extract just the last line for console
                error_lines = result.stderr.strip().split('\n')
                error_msg = error_lines[-1] if error_lines else "Unknown error"
                print(f"   ❌ {script_name}")
                print(f"      {error_msg[:100]}")
                failed += 1
            else:
                completed += 1
                print(f"   ✅ {script_name}")
                
        except subprocess.TimeoutExpired:
            error_msg = "Timeout after 5 minutes"
            error_log.append({
                "control": control_path.name,
                "script": script_name,
                "error": error_msg
            })
            print(f"   ❌ {script_name}: {error_msg}")
            failed += 1
        except Exception as e:
            error_log.append({
                "control": control_path.name,
                "script": script_name,
                "error": str(e)
            })
            print(f"   ❌ {script_name}: {e}")
            failed += 1
    
    print(f"   📊 {completed} completed, {failed} failed")
    
    return {
        "scripts_run": completed,
        "scripts_failed": failed
    }


def write_error_log(error_log: list, base_path: Path) -> str:
    """Write detailed error log to file"""
    if not error_log:
        return None
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = base_path / f"isms_generation_errors_{timestamp}.log"
    
    with open(log_file, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("ISMS WORKBOOK GENERATION - ERROR LOG\n")
        f.write("=" * 80 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Errors: {len(error_log)}\n")
        f.write("=" * 80 + "\n\n")
        
        for i, error in enumerate(error_log, 1):
            f.write(f"\n{'=' * 80}\n")
            f.write(f"ERROR {i} of {len(error_log)}\n")
            f.write(f"{'=' * 80}\n")
            f.write(f"Control: {error['control']}\n")
            f.write(f"Script:  {error['script']}\n")
            f.write(f"\n{error['error']}\n")
    
    return str(log_file)


def generate_workbooks(base_path: str, generator_type: str, control_name: str = None) -> None:
    """
    Main function to generate workbooks.
    
    Args:
        base_path: Root path of ISMS structure
        generator_type: "10" for master or "20" for protected
        control_name: Optional specific control to process
    """
    base_path_obj = Path(base_path).resolve()
    
    if not base_path_obj.exists():
        print(f"❌ Error: Base path does not exist: {base_path}")
        sys.exit(1)
    
    if generator_type not in ["10", "20"]:
        print(f"❌ Error: Generator type must be '10' or '20', got '{generator_type}'")
        sys.exit(1)
    
    generator_name = "10_generator_master" if generator_type == "10" else "20_generator_protected"
    
    print("=" * 80)
    print("ISMS WORKBOOK GENERATION")
    print("=" * 80)
    print(f"Base path:  {base_path_obj}")
    print(f"Generator:  {generator_name}")
    print(f"Control:    {control_name if control_name else 'ALL'}")
    print("=" * 80)
    
    # Find control folders to process
    if control_name:
        # Process specific control
        control_path = base_path_obj / control_name
        if not control_path.exists():
            print(f"❌ Error: Control folder not found: {control_path}")
            sys.exit(1)
        control_paths = [control_path]
    else:
        # Find all control folders with the specified generator folder
        control_paths = []
        for item in base_path_obj.iterdir():
            if item.is_dir() and item.name.startswith("ISMS-A."):
                generator_path = item / generator_name
                if generator_path.exists():
                    control_paths.append(item)
        
        control_paths.sort()
    
    if not control_paths:
        print("⚠️  No control folders found with the specified generator")
        print(f"\nℹ️  Hint: Make sure you've run isms_rename_generator_folders.py first")
        print(f"    to rename folders to {generator_name}")
        sys.exit(0)
    
    print(f"\n🔍 Found {len(control_paths)} control(s) to process")
    
    # Process each control
    total_scripts = 0
    total_failed = 0
    error_log = []
    
    for control_path in control_paths:
        result = run_generator_scripts(control_path, generator_name, error_log)
        total_scripts += result["scripts_run"]
        total_failed += result["scripts_failed"]
    
    # Summary
    print("\n" + "=" * 80)
    print("GENERATION SUMMARY")
    print("=" * 80)
    print(f"Controls processed:   {len(control_paths)}")
    print(f"Scripts completed:    {total_scripts}")
    print(f"Scripts failed:       {total_failed}")
    print(f"Total errors:         {len(error_log)}")
    
    # Write detailed error log if there are errors
    if error_log:
        log_file = write_error_log(error_log, base_path_obj)
        print(f"\n📝 Detailed error log written to:")
        print(f"   {log_file}")
        print(f"\n❌ {len(error_log)} error(s) occurred during generation")
        
        # Show summary of errors
        print("\n📋 Error Summary:")
        error_counts = {}
        for error in error_log:
            control = error['control']
            if control not in error_counts:
                error_counts[control] = 0
            error_counts[control] += 1
        
        for control, count in sorted(error_counts.items()):
            print(f"   • {control}: {count} error(s)")
        
        sys.exit(1)
    else:
        print(f"\n✅ All {total_scripts} scripts completed successfully!")
        print(f"\n💡 Workbooks should now be in 90_workbooks/ folders")
        print(f"   Run this to verify:")
        print(f"   find {base_path_obj} -name '90_workbooks' -exec ls -lh {{}} \\;")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 isms_generate_workbooks.py <base_path> <generator_type> [control_name]")
        print()
        print("Arguments:")
        print("  base_path:      Path to 10-ISMS-SCR-Base folder")
        print("  generator_type: '10' for 10_generator_master or '20' for 20_generator_protected")
        print("  control_name:   (Optional) Specific control folder to process")
        print()
        print("Examples:")
        print("  # Generate all workbooks using master generator")
        print("  python3 isms_generate_workbooks.py ./ 10")
        print()
        print("  # Generate all workbooks using protected generator")
        print("  python3 isms_generate_workbooks.py ./ 20")
        print()
        print("  # Generate workbooks for specific control")
        print("  python3 isms_generate_workbooks.py ./ 10 ISMS-A.8.32-Change-Management")
        sys.exit(1)
    
    base_path = sys.argv[1]
    generator_type = sys.argv[2]
    control_name = sys.argv[3] if len(sys.argv) > 3 else None
    
    generate_workbooks(base_path, generator_type, control_name)
