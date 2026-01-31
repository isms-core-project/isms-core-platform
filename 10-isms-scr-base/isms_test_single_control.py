#!/usr/bin/env python3
"""
ISMS Diagnostic: Test single control to see where files are generated
"""

import os
import sys
import subprocess
from pathlib import Path
import time


def find_all_excel_files(root_path: Path) -> dict:
    """Find all Excel files and organize by location"""
    excel_files = {}
    excel_extensions = {'.xlsx', '.xls', '.xlsm'}
    
    for root, dirs, files in os.walk(root_path):
        # Skip hidden dirs
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for filename in files:
            if Path(filename).suffix.lower() in excel_extensions:
                rel_path = Path(root).relative_to(root_path)
                if str(rel_path) not in excel_files:
                    excel_files[str(rel_path)] = []
                excel_files[str(rel_path)].append(filename)
    
    return excel_files


if len(sys.argv) != 3:
    print("Usage: python3 isms_test_single_control.py <control_path> <generator_type>")
    print("Example: python3 isms_test_single_control.py ./ISMS-A.8.32-Change-Management 10")
    sys.exit(1)

control_path = Path(sys.argv[1]).resolve()
generator_type = sys.argv[2]

if not control_path.exists():
    print(f"❌ Control path not found: {control_path}")
    sys.exit(1)

generator_folder = f"{generator_type}_generator_master" if generator_type == "10" else f"{generator_type}_generator_protected"
generator_path = control_path / generator_folder

if not generator_path.exists():
    print(f"❌ Generator folder not found: {generator_path}")
    sys.exit(1)

print("=" * 80)
print("DIAGNOSTIC TEST - SINGLE CONTROL")
print("=" * 80)
print(f"Control: {control_path.name}")
print(f"Generator: {generator_folder}")
print("=" * 80)

# Find first generator script
generator_scripts = sorted([f for f in generator_path.glob("generate*.py") if not f.name.endswith('.bak.py')])

if not generator_scripts:
    print("❌ No generator scripts found")
    sys.exit(1)

test_script = generator_scripts[0]
print(f"\n📝 Test script: {test_script.name}\n")

# Get BEFORE snapshot
print("📸 Taking BEFORE snapshot...")
before_files = find_all_excel_files(control_path)
print(f"   Found {sum(len(files) for files in before_files.values())} Excel files")
for location, files in sorted(before_files.items()):
    print(f"   • {location}: {len(files)} files")

# Run the script
print(f"\n▶️  Running {test_script.name}...")
try:
    result = subprocess.run(
        ["python3", test_script.name],
        cwd=generator_path,
        capture_output=True,
        text=True,
        timeout=60
    )
    
    if result.returncode != 0:
        print(f"❌ Script failed:")
        print(result.stderr)
        sys.exit(1)
    else:
        print("✅ Script completed successfully")
        if result.stdout:
            print("\nScript output:")
            print(result.stdout[-500:])  # Last 500 chars
        
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

# Small delay
time.sleep(0.5)

# Get AFTER snapshot
print(f"\n📸 Taking AFTER snapshot...")
after_files = find_all_excel_files(control_path)
print(f"   Found {sum(len(files) for files in after_files.values())} Excel files")
for location, files in sorted(after_files.items()):
    print(f"   • {location}: {len(files)} files")

# Compare
print("\n" + "=" * 80)
print("ANALYSIS")
print("=" * 80)

new_locations = set(after_files.keys()) - set(before_files.keys())
if new_locations:
    print("✅ New directories with Excel files:")
    for loc in sorted(new_locations):
        print(f"   • {loc}: {after_files[loc]}")

changed_locations = []
for location in after_files.keys():
    if location in before_files:
        before_count = len(before_files[location])
        after_count = len(after_files[location])
        if after_count > before_count:
            changed_locations.append(location)
            new_files = set(after_files[location]) - set(before_files[location])
            print(f"✅ New files in {location}:")
            for f in sorted(new_files):
                print(f"   • {f}")

if not new_locations and not changed_locations:
    print("⚠️  No new Excel files detected!")
    print("\nThis could mean:")
    print("1. The script doesn't create files")
    print("2. The script failed silently")
    print("3. Files were created outside the control folder")
    print("4. Script creates files with different extensions")
