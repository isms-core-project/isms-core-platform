#!/usr/bin/env python3
"""
ISMS Script: Rename Generator Folders (Underscore to Hyphen)
Purpose: Rename generator folders to use hyphens instead of underscores:
         10_generator_master → 10_generator-master
         20_generator_protected → 20_generator-protected

Usage:
    python3 isms_rename_generator_folders.py /path/to/10-ISMS-SCR-Base
         
Author: Gregory Griffin
Date: 2026-01-30
"""

import os
import sys
from pathlib import Path


def rename_generator_folders(base_path: str) -> None:
    """
    Recursively rename generator folders throughout the ISMS directory structure.
    Changes underscores to hyphens in folder names.
    
    Args:
        base_path: Root path to search for folders to rename
    """
    base_path_obj = Path(base_path).resolve()
    
    if not base_path_obj.exists():
        print(f"❌ Error: Base path does not exist: {base_path}")
        sys.exit(1)
    
    # Track changes
    renamed_master = []
    renamed_protected = []
    errors = []
    
    # Walk through all directories
    for root, dirs, _ in os.walk(base_path_obj):
        root_path = Path(root)
        
        # Check for 10_generator_master (underscore)
        if "10_generator_master" in dirs:
            old_path = root_path / "10_generator_master"
            new_path = root_path / "10_generator-master"
            
            try:
                if new_path.exists():
                    print(f"⚠️  Skipping: {new_path} already exists")
                else:
                    old_path.rename(new_path)
                    renamed_master.append(str(new_path.relative_to(base_path_obj)))
                    print(f"✅ Renamed: {old_path.relative_to(base_path_obj)} → 10_generator-master")
            except Exception as e:
                error_msg = f"Failed to rename {old_path}: {e}"
                errors.append(error_msg)
                print(f"❌ {error_msg}")
        
        # Check for 20_generator_protected (underscore)
        if "20_generator_protected" in dirs:
            old_path = root_path / "20_generator_protected"
            new_path = root_path / "20_generator-protected"
            
            try:
                if new_path.exists():
                    print(f"⚠️  Skipping: {new_path} already exists")
                else:
                    old_path.rename(new_path)
                    renamed_protected.append(str(new_path.relative_to(base_path_obj)))
                    print(f"✅ Renamed: {old_path.relative_to(base_path_obj)} → 20_generator-protected")
            except Exception as e:
                error_msg = f"Failed to rename {old_path}: {e}"
                errors.append(error_msg)
                print(f"❌ {error_msg}")
    
    # Summary
    print("\n" + "=" * 80)
    print("RENAME SUMMARY")
    print("=" * 80)
    print(f"10_generator_master → 10_generator-master:    {len(renamed_master)} folders renamed")
    print(f"20_generator_protected → 20_generator-protected: {len(renamed_protected)} folders renamed")
    print(f"Errors:                                        {len(errors)} errors")
    
    if errors:
        print("\n❌ ERRORS ENCOUNTERED:")
        for error in errors:
            print(f"  • {error}")
        sys.exit(1)
    elif renamed_master or renamed_protected:
        print("\n✅ All folders renamed successfully!")
        print("\n⚠️  IMPORTANT: Run 'git status' to see changes")
        print("   Then commit with: git add . && git commit -m 'Rename generator folders to use hyphens'")
    else:
        print("\n⚠️  No folders found to rename")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 isms_rename_generator_folders.py <base_path>")
        print("Example: python3 isms_rename_generator_folders.py /path/to/10-ISMS-SCR-Base")
        sys.exit(1)
    
    base_path = sys.argv[1]
    rename_generator_folders(base_path)