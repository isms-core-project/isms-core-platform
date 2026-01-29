#!/usr/bin/env python3
"""
ISMS Script: Count Workbooks
Purpose: Count and list all Excel files in 90_workbooks folders
"""

import sys
from pathlib import Path


def count_workbooks(base_path: str) -> None:
    """Count Excel files in all 90_workbooks folders"""
    base_path_obj = Path(base_path).resolve()
    
    if not base_path_obj.exists():
        print(f"❌ Error: Base path does not exist: {base_path}")
        sys.exit(1)
    
    print("=" * 80)
    print("ISMS WORKBOOKS COUNT")
    print("=" * 80)
    print(f"Base path: {base_path_obj}\n")
    
    excel_extensions = {'.xlsx', '.xls', '.xlsm'}
    total_files = 0
    controls_with_workbooks = []
    controls_without_workbooks = []
    
    # Find all ISMS-A.* control folders
    control_folders = sorted([f for f in base_path_obj.iterdir() 
                              if f.is_dir() and f.name.startswith("ISMS-A.")])
    
    for control_path in control_folders:
        workbooks_path = control_path / "90_workbooks"
        
        if workbooks_path.exists():
            # Count Excel files
            excel_files = []
            for ext in excel_extensions:
                excel_files.extend(workbooks_path.glob(f"*{ext}"))
            
            if excel_files:
                print(f"📂 {control_path.name}")
                print(f"   📊 {len(excel_files)} workbook(s):")
                for f in sorted(excel_files):
                    size_kb = f.stat().st_size / 1024
                    print(f"      • {f.name} ({size_kb:.1f} KB)")
                total_files += len(excel_files)
                controls_with_workbooks.append(control_path.name)
            else:
                controls_without_workbooks.append(control_path.name)
        else:
            controls_without_workbooks.append(control_path.name)
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total controls:              {len(control_folders)}")
    print(f"Controls with workbooks:     {len(controls_with_workbooks)}")
    print(f"Controls without workbooks:  {len(controls_without_workbooks)}")
    print(f"Total workbooks:             {total_files}")
    
    if controls_without_workbooks:
        print(f"\n⚠️  Controls without workbooks ({len(controls_without_workbooks)}):")
        for control in controls_without_workbooks[:10]:
            print(f"   • {control}")
        if len(controls_without_workbooks) > 10:
            print(f"   ... and {len(controls_without_workbooks) - 10} more")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 isms_count_workbooks.py <base_path>")
        print("Example: python3 isms_count_workbooks.py /path/to/10-ISMS-SCR-Base")
        sys.exit(1)
    
    base_path = sys.argv[1]
    count_workbooks(base_path)
