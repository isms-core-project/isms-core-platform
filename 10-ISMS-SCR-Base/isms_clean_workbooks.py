#!/usr/bin/env python3
"""
ISMS Script: Clean Workbooks
Purpose: Delete all Excel files (.xlsx, .xls, .xlsm) in 90_workbooks folders

# Dry run (shows what would be deleted without deleting)
python3 isms_clean_workbooks.py /path/to/10-ISMS-SCR-Base --dry-run

# Actually delete files
python3 isms_clean_workbooks.py /path/to/10-ISMS-SCR-Base

"""

import os
import sys
from pathlib import Path


def delete_excel_files(base_path: str, dry_run: bool = False) -> None:
    """
    Recursively find all 90_workbooks folders and delete Excel files.
    
    Args:
        base_path: Root path to search for 90_workbooks folders
        dry_run: If True, only show what would be deleted without actually deleting
    """
    base_path_obj = Path(base_path).resolve()
    
    if not base_path_obj.exists():
        print(f"❌ Error: Base path does not exist: {base_path}")
        sys.exit(1)
    
    # Excel file extensions
    excel_extensions = {'.xlsx', '.xls', '.xlsm'}
    
    # Track changes
    deleted_files = []
    workbooks_folders = []
    errors = []
    
    # Walk through all directories
    for root, dirs, files in os.walk(base_path_obj):
        # Check if current directory is 90_workbooks
        if os.path.basename(root) == "90_workbooks":
            root_path = Path(root)
            workbooks_folders.append(str(root_path.relative_to(base_path_obj)))
            
            # Find all Excel files in this folder
            excel_files = [f for f in files if Path(f).suffix.lower() in excel_extensions]
            
            if excel_files:
                print(f"\n📁 Processing: {root_path.relative_to(base_path_obj)}")
                
                for filename in excel_files:
                    file_path = root_path / filename
                    
                    try:
                        if dry_run:
                            print(f"  🔍 Would delete: {filename}")
                            deleted_files.append(str(file_path.relative_to(base_path_obj)))
                        else:
                            file_path.unlink()
                            deleted_files.append(str(file_path.relative_to(base_path_obj)))
                            print(f"  ✅ Deleted: {filename}")
                    except Exception as e:
                        error_msg = f"Failed to delete {file_path}: {e}"
                        errors.append(error_msg)
                        print(f"  ❌ {error_msg}")
            else:
                print(f"📁 {root_path.relative_to(base_path_obj)}: No Excel files found")
    
    # Summary
    print("\n" + "=" * 80)
    print("DELETE SUMMARY")
    print("=" * 80)
    print(f"Mode:              {'DRY RUN' if dry_run else 'LIVE DELETE'}")
    print(f"Workbooks folders: {len(workbooks_folders)} found")
    print(f"Excel files:       {len(deleted_files)} {'would be deleted' if dry_run else 'deleted'}")
    print(f"Errors:            {len(errors)} errors")
    
    if errors:
        print("\n❌ ERRORS ENCOUNTERED:")
        for error in errors:
            print(f"  • {error}")
        sys.exit(1)
    elif deleted_files:
        if dry_run:
            print(f"\n🔍 Dry run complete. Run without --dry-run to actually delete {len(deleted_files)} files.")
        else:
            print(f"\n✅ Successfully deleted {len(deleted_files)} Excel files!")
    else:
        print("\n⚠️  No Excel files found to delete")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 isms_clean_workbooks.py <base_path> [--dry-run]")
        print("Example: python3 isms_clean_workbooks.py /path/to/10-ISMS-SCR-Base")
        print("         python3 isms_clean_workbooks.py /path/to/10-ISMS-SCR-Base --dry-run")
        sys.exit(1)
    
    base_path = sys.argv[1]
    dry_run = "--dry-run" in sys.argv
    
    if dry_run:
        print("🔍 DRY RUN MODE - No files will be deleted")
        print("=" * 80)
    
    delete_excel_files(base_path, dry_run)
