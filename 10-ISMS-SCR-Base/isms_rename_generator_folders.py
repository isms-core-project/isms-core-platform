#!/usr/bin/env python3
"""
ISMS Script: Rename Generator Folders
Purpose: Rename all 10_generator_utf to 10_generator_master and
         20_generator_ascii to 20_generator_protected

python3 isms_rename_generator_folders.py /path/to/10-ISMS-SCR-Base
         
"""

import os
import sys
from pathlib import Path


def rename_generator_folders(base_path: str) -> None:
    """
    Recursively rename generator folders throughout the ISMS directory structure.
    
    Args:
        base_path: Root path to search for folders to rename
    """
    base_path_obj = Path(base_path).resolve()
    
    if not base_path_obj.exists():
        print(f"❌ Error: Base path does not exist: {base_path}")
        sys.exit(1)
    
    # Track changes
    renamed_utf = []
    renamed_ascii = []
    errors = []
    
    # Walk through all directories
    for root, dirs, _ in os.walk(base_path_obj):
        root_path = Path(root)
        
        # Check for 10_generator_utf
        if "10_generator_utf" in dirs:
            old_path = root_path / "10_generator_utf"
            new_path = root_path / "10_generator_master"
            
            try:
                if new_path.exists():
                    print(f"⚠️  Skipping: {new_path} already exists")
                else:
                    old_path.rename(new_path)
                    renamed_utf.append(str(new_path.relative_to(base_path_obj)))
                    print(f"✅ Renamed: {old_path.relative_to(base_path_obj)} → 10_generator_master")
            except Exception as e:
                error_msg = f"Failed to rename {old_path}: {e}"
                errors.append(error_msg)
                print(f"❌ {error_msg}")
        
        # Check for 20_generator_ascii
        if "20_generator_ascii" in dirs:
            old_path = root_path / "20_generator_ascii"
            new_path = root_path / "20_generator_protected"
            
            try:
                if new_path.exists():
                    print(f"⚠️  Skipping: {new_path} already exists")
                else:
                    old_path.rename(new_path)
                    renamed_ascii.append(str(new_path.relative_to(base_path_obj)))
                    print(f"✅ Renamed: {old_path.relative_to(base_path_obj)} → 20_generator_protected")
            except Exception as e:
                error_msg = f"Failed to rename {old_path}: {e}"
                errors.append(error_msg)
                print(f"❌ {error_msg}")
    
    # Summary
    print("\n" + "=" * 80)
    print("RENAME SUMMARY")
    print("=" * 80)
    print(f"UTF→Master:    {len(renamed_utf)} folders renamed")
    print(f"ASCII→Protected: {len(renamed_ascii)} folders renamed")
    print(f"Errors:          {len(errors)} errors")
    
    if errors:
        print("\n❌ ERRORS ENCOUNTERED:")
        for error in errors:
            print(f"  • {error}")
        sys.exit(1)
    elif renamed_utf or renamed_ascii:
        print("\n✅ All folders renamed successfully!")
    else:
        print("\n⚠️  No folders found to rename")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 isms_rename_generator_folders.py <base_path>")
        print("Example: python3 isms_rename_generator_folders.py /path/to/10-ISMS-SCR-Base")
        sys.exit(1)
    
    base_path = sys.argv[1]
    rename_generator_folders(base_path)
