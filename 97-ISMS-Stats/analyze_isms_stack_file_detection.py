#!/usr/bin/env python3
"""
ISMS Project Comprehensive Analyzer v4.3 - FINAL
Properly handles split-base-folder structure:
- POL files in: 70-ISMS-POL-Base/ISMS-A.X.XX-.../
- IMP files in: 30-ISMS-IMP-Base/ISMS-A.X.XX-.../  
- SCR files in: 10-ISMS-SCR-Base/ISMS-A.X.XX-.../

Stacks recognized by matching folder names across all bases.
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# ANSI colors
class Color:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    MAGENTA = '\033[0;35m'
    RESET = '\033[0m'

# Exclusion patterns
EXCLUDE_PATTERNS = [
    '00-ISMS-POL-KB',
    '99_archive',
    '98_backup', 
    '99_originals',
    '_old',
    '10_pol-md_old',
    '.venv',
    '__pycache__',
    '.git'
]

def should_exclude(path_str):
    """Check if path should be excluded"""
    return any(pattern in path_str for pattern in EXCLUDE_PATTERNS)

def extract_control_folder_name(folder_name):
    """
    Extract the normalized control folder name.
    Examples:
      ISMS-A.5.15-16-18-Identity-Access-Management → A.5.15-16-18
      ISMS-A.8.24-Use-of-Cryptography → A.8.24
      ISMS-A.8.13-14-5.30-Business-Continuity → A.8.13-14-5.30
    """
    # Look for pattern: A.X.XX or A.X.XX-XX-XX or A.X.XX-XX-X.XX (cross-section)
    match = re.search(r'(A\.\d+\.\d+(?:-\d+(?:\.\d+)?)*)', folder_name)
    if match:
        return match.group(1)
    return None

def parse_control_spec(control_spec):
    """
    Parse control specification into individual controls.
    Examples:
      A.5.15-16-18 → [A.5.15, A.5.16, A.5.18]
      A.8.1-7-18-19 → [A.8.1, A.8.7, A.8.18, A.8.19]
      A.8.13-14-5.30 → [A.8.13, A.8.14, A.5.30] (cross-section)
      A.5.31 → [A.5.31]
    
    Returns: (is_stack, [controls])
    """
    controls = []
    
    # Split by dash to get parts
    parts = control_spec.split('-')
    
    # First part is always A.X.YY
    first_match = re.match(r'A\.(\d+)\.(\d+)', parts[0])
    if not first_match:
        return False, []
    
    first_section = first_match.group(1)
    first_number = first_match.group(2)
    controls.append(f"A.{first_section}.{first_number}")
    
    # Process remaining parts
    for part in parts[1:]:
        # Check if this part is a full control (e.g., "5.30" in "A.8.13-14-5.30")
        if '.' in part:
            section, number = part.split('.', 1)
            controls.append(f"A.{section}.{number}")
        else:
            # Same section as first control
            controls.append(f"A.{first_section}.{part}")
    
    # It's a stack if we have multiple controls
    is_stack = len(controls) > 1
    
    return is_stack, sorted(controls, key=lambda x: (int(x.split('.')[1]), int(x.split('.')[2])))

def control_to_compact(control):
    """Convert A.5.7 to a57"""
    match = re.match(r'A\.(\d+)\.(\d+)', control)
    if match:
        return f"a{match.group(1)}{match.group(2)}"
    return None

def is_script_for_control(filename, control):
    """
    Comprehensive check if a Python script belongs to a control.
    """
    if not filename.endswith('.py'):
        return False
    
    match = re.match(r'A\.(\d+)\.(\d+)', control)
    if not match:
        return False
    
    section = match.group(1)
    number = match.group(2)
    
    # Various control representations
    c_dot = control  # A.5.7
    c_dash = control.replace('.', '-')  # A-5-7
    c_under = control.replace('.', '_')  # A_5_7
    c_compact = f"a{section}{number}"  # a57
    c_number = f"{section}{number}"  # 57
    
    # Check all patterns
    patterns_to_check = [
        c_dot in filename,
        c_dash in filename,
        c_under in filename,
        f'generate_{c_compact}' in filename,
        f'_{c_compact}_' in filename,
        f'{c_compact}_' in filename.lower(),
        f'generate_{c_number}_' in filename,
        f'_{c_number}_' in filename,
        f'generate_{section}{number}' in filename,  # generate_531
        f'_{section}{number}_' in filename,  # _531_
        f'files_{section}{number}' in filename,  # files_531
    ]
    
    return any(patterns_to_check)

def analyze_project(project_path):
    """Main analysis function"""
    project_path = Path(project_path).resolve()
    
    print(f"{Color.BLUE}╔════════════════════════════════════════════════════════════╗{Color.RESET}")
    print(f"{Color.BLUE}║   ISMS Project Analyzer v4.3 - Split-Base-Aware FINAL    ║{Color.RESET}")
    print(f"{Color.BLUE}╚════════════════════════════════════════════════════════════╝{Color.RESET}\n")
    
    # ============================================================================
    # Step 1: Build control/stack registry by scanning folder names
    # ============================================================================
    print("Scanning for control folders across all bases...")
    
    # Map: control_spec → {pol_folder, imp_folder, scr_folder}
    control_folders = defaultdict(lambda: {'pol': None, 'imp': None, 'scr': None})
    
    # Map: control_spec → (is_stack, [individual_controls])
    control_info = {}
    
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if not should_exclude(d)]
        
        if should_exclude(root):
            continue
        
        for dirname in dirs:
            control_spec = extract_control_folder_name(dirname)
            
            if control_spec:
                full_path = os.path.join(root, dirname)
                
                # Determine which base this is in
                if '/70-ISMS-POL-Base/' in full_path or '\\70-ISMS-POL-Base\\' in full_path:
                    control_folders[control_spec]['pol'] = full_path
                elif '/30-ISMS-IMP-Base/' in full_path or '\\30-ISMS-IMP-Base\\' in full_path:
                    control_folders[control_spec]['imp'] = full_path
                elif '/10-ISMS-SCR-Base/' in full_path or '\\10-ISMS-SCR-Base\\' in full_path:
                    control_folders[control_spec]['scr'] = full_path
                
                # Parse control spec
                if control_spec not in control_info:
                    is_stack, controls = parse_control_spec(control_spec)
                    control_info[control_spec] = (is_stack, controls)
    
    # Deduplicate and organize
    all_controls = set()
    stacks = {}  # control_spec → (controls, folders)
    individual_controls_map = {}  # control → control_spec
    
    for control_spec, (is_stack, controls) in control_info.items():
        all_controls.update(controls)
        
        if is_stack:
            stacks[control_spec] = {
                'controls': controls,
                'folders': control_folders[control_spec],
                'files': {'pol': [], 'imp': [], 'scr': []}
            }
            for c in controls:
                individual_controls_map[c] = control_spec  # Mark as part of stack
        else:
            # Individual control
            individual_controls_map[controls[0]] = control_spec
    
    all_controls = sorted(all_controls, key=lambda x: (int(x.split('.')[1]), int(x.split('.')[2])))
    
    print(f"{Color.GREEN}✅ Found {len(all_controls)} controls{Color.RESET}")
    print(f"   📦 {len(stacks)} stacks detected")
    
    for stack_id, stack_data in sorted(stacks.items()):
        controls_str = ', '.join(stack_data['controls'])
        print(f"      {stack_id} → [{controls_str}]")
    
    print()
    
    # ============================================================================
    # Step 2: Find files for each control/stack
    # ============================================================================
    print("Finding files...")
    
    # For each control spec, find files in the appropriate folders
    files_by_spec = {}  # control_spec → {pol: [], imp: [], scr: []}
    
    for control_spec in control_folders.keys():
        files_by_spec[control_spec] = {'pol': [], 'imp': [], 'scr': []}
        folders = control_folders[control_spec]
        is_stack, controls = control_info[control_spec]
        
        # Find POL files
        if folders['pol']:
            for root, dirs, files in os.walk(folders['pol']):
                dirs[:] = [d for d in dirs if not should_exclude(d)]
                if should_exclude(root):
                    continue
                
                for filename in files:
                    if 'POL' in filename and filename.endswith('.md'):
                        files_by_spec[control_spec]['pol'].append(os.path.join(root, filename))
        
        # Find IMP files
        if folders['imp']:
            for root, dirs, files in os.walk(folders['imp']):
                dirs[:] = [d for d in dirs if not should_exclude(d)]
                if should_exclude(root):
                    continue
                
                for filename in files:
                    if 'IMP' in filename and filename.endswith('.md'):
                        # For stacks, check if filename contains stack spec
                        # (e.g., ISMS-IMP-A.8.13-14-5.30-S1.md)
                        matched = False
                        
                        if is_stack:
                            stack_patterns = [
                                control_spec.replace('.', '-'),  # A-8-13-14-5-30
                                control_spec.replace('.', '_'),  # A_8_13_14_5_30
                                control_spec,                     # A.8.13-14-5.30
                            ]
                            if any(pattern in filename for pattern in stack_patterns):
                                matched = True
                            
                            # Also check individual controls
                            if not matched:
                                for control in controls:
                                    c_dot = control
                                    c_dash = control.replace('.', '-')
                                    c_under = control.replace('.', '_')
                                    if c_dot in filename or c_dash in filename or c_under in filename:
                                        matched = True
                                        break
                        else:
                            # Individual control
                            c_dot = controls[0]
                            c_dash = controls[0].replace('.', '-')
                            c_under = controls[0].replace('.', '_')
                            if c_dot in filename or c_dash in filename or c_under in filename:
                                matched = True
                        
                        if matched:
                            files_by_spec[control_spec]['imp'].append(os.path.join(root, filename))
        
        # Find SCR files
        if folders['scr']:
            for root, dirs, files in os.walk(folders['scr']):
                dirs[:] = [d for d in dirs if not should_exclude(d)]
                if should_exclude(root):
                    continue
                
                for filename in files:
                    # For stacks, also check if filename contains the stack spec itself
                    # (e.g., "generate_a813_*.py" for stack A.8.13-14-5.30)
                    matched = False
                    
                    if is_stack:
                        # Check if it matches any control in this spec
                        for control in controls:
                            if is_script_for_control(filename, control):
                                matched = True
                                break
                        
                        # Also check if filename contains stack spec pattern
                        # (e.g., A.8.13-14-5.30 or A-8-13-14-5-30)
                        if not matched:
                            stack_patterns = [
                                control_spec.replace('.', '-'),  # A-8-13-14-5-30
                                control_spec.replace('.', '_'),  # A_8_13_14_5_30
                                control_spec,                     # A.8.13-14-5.30
                            ]
                            if any(pattern in filename for pattern in stack_patterns):
                                matched = True
                    else:
                        # For individual controls
                        if is_script_for_control(filename, controls[0]):
                            matched = True
                    
                    if matched:
                        files_by_spec[control_spec]['scr'].append(os.path.join(root, filename))
    
    # ============================================================================
    # Step 3: Calculate coverage per control
    # ============================================================================
    print("Calculating coverage...\n")
    
    coverage = {}
    full_count = 0
    partial_count = 0
    basic_count = 0
    ref_count = 0
    
    for control in all_controls:
        control_spec = individual_controls_map.get(control)
        
        if not control_spec or control_spec not in files_by_spec:
            # Control not found in any folder
            coverage[control] = {
                'pol': False,
                'imp': False,
                'scr': False,
                'pol_count': 0,
                'imp_count': 0,
                'scr_count': 0,
                'status': 'REFERENCE',
                'in_stack': None
            }
            ref_count += 1
            continue
        
        files = files_by_spec[control_spec]
        is_stack, controls_in_spec = control_info[control_spec]
        
        has_pol = len(files['pol']) > 0
        has_imp = len(files['imp']) > 0
        has_scr = len(files['scr']) > 0
        
        if has_pol and has_imp and has_scr:
            status = 'FULL'
            full_count += 1
        elif has_pol and has_imp:
            status = 'PARTIAL'
            partial_count += 1
        elif has_pol:
            status = 'BASIC'
            basic_count += 1
        else:
            status = 'REFERENCE'
            ref_count += 1
        
        coverage[control] = {
            'pol': has_pol,
            'imp': has_imp,
            'scr': has_scr,
            'pol_count': len(files['pol']),
            'imp_count': len(files['imp']),
            'scr_count': len(files['scr']),
            'status': status,
            'in_stack': control_spec if is_stack else None
        }
    
    # ============================================================================
    # Step 4: Display results
    # ============================================================================
    print("Implementation Depth:")
    print(f"  🟢 Full (POL+IMP+SCR):        {full_count} controls")
    print(f"  🟡 Partial (POL+IMP):         {partial_count} controls")
    print(f"  🔵 Basic (POL only):          {basic_count} controls")
    print(f"  ⚪ Reference:                 {ref_count} controls")
    print()
    
    # Display stacks
    if stacks:
        print(f"{Color.MAGENTA}📦 Stacked Controls:{Color.RESET}")
        for stack_id, stack_data in sorted(stacks.items()):
            controls_str = ', '.join(stack_data['controls'])
            files = files_by_spec.get(stack_id, {'pol': [], 'imp': [], 'scr': []})
            
            pol_count = len(files['pol'])
            imp_count = len(files['imp'])
            scr_count = len(files['scr'])
            
            # Get status from first control in stack
            first_control = stack_data['controls'][0]
            stack_status = coverage.get(first_control, {}).get('status', 'REFERENCE')
            
            if stack_status == 'FULL':
                symbol = '🟢'
            elif stack_status == 'PARTIAL':
                symbol = '🟡'
            elif stack_status == 'BASIC':
                symbol = '🔵'
            else:
                symbol = '⚪'
            
            print(f"  {symbol} {stack_id} → [{controls_str}]")
            print(f"     Shared: POL:{pol_count} IMP:{imp_count} SCR:{scr_count}")
        print()
    
    # Display full implementations
    if full_count > 0:
        print(f"{Color.GREEN}✅ Fully implemented controls:{Color.RESET}")
        for control, data in sorted(coverage.items()):
            if data['status'] == 'FULL':
                if data['in_stack']:
                    print(f"  {control} (in stack {data['in_stack']})")
                else:
                    print(f"  {control} (POL:{data['pol_count']} IMP:{data['imp_count']} SCR:{data['scr_count']})")
        print()
    
    if partial_count > 0:
        print(f"{Color.YELLOW}🟡 Partially implemented (no scripts):{Color.RESET}")
        for control, data in sorted(coverage.items()):
            if data['status'] == 'PARTIAL':
                if data['in_stack']:
                    print(f"  {control} (in stack {data['in_stack']})")
                else:
                    print(f"  {control} (POL:{data['pol_count']} IMP:{data['imp_count']})")
        print()
    
    if basic_count > 0:
        print(f"{Color.BLUE}🔵 Basic implementation (POL only):{Color.RESET}")
        for control, data in sorted(coverage.items()):
            if data['status'] == 'BASIC':
                if data['in_stack']:
                    print(f"  {control} (in stack {data['in_stack']})")
                else:
                    print(f"  {control} (POL:{data['pol_count']})")
        print()
    
    # ============================================================================
    # Step 5: Count files globally
    # ============================================================================
    print("Counting files globally...")
    
    pol_files = []
    imp_files = []
    scr_files = []
    xlsx_files = []
    
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if not should_exclude(d)]
        if should_exclude(root):
            continue
        
        for filename in files:
            full_path = os.path.join(root, filename)
            
            if 'POL' in filename and filename.endswith('.md'):
                pol_files.append(full_path)
            elif 'IMP' in filename and filename.endswith('.md'):
                imp_files.append(full_path)
            elif filename.endswith('.py'):
                scr_files.append(full_path)
            elif filename.endswith('.xlsx'):
                xlsx_files.append(full_path)
    
    total_docs = len(pol_files) + len(imp_files)
    total_files = total_docs + len(scr_files) + len(xlsx_files)
    
    # Count lines
    lines_code = 0
    for scr_file in scr_files:
        try:
            with open(scr_file, 'r', encoding='utf-8', errors='ignore') as f:
                lines_code += len(f.readlines())
        except:
            pass
    
    lines_docs = 0
    for doc_file in pol_files + imp_files:
        try:
            with open(doc_file, 'r', encoding='utf-8', errors='ignore') as f:
                lines_docs += len(f.readlines())
        except:
            pass
    
    total_lines = lines_code + lines_docs
    
    # ============================================================================
    # Section breakdown
    # ============================================================================
    print("\nControl breakdown by section:")
    section_totals = {5: 37, 6: 8, 7: 14, 8: 34}
    
    for section in [5, 6, 7, 8]:
        section_controls = [c for c in all_controls if c.startswith(f'A.{section}.')]
        count = len(section_controls)
        total = section_totals[section]
        pct = int((count / total) * 100) if total > 0 else 0
        print(f"  Section {section}: {count}/{total} ({pct}%)")
    print()
    
    # ============================================================================
    # Executive summary
    # ============================================================================
    completion_pct = round((len(all_controls) / 93) * 100, 1)
    controls_in_stacks = sum(len(s['controls']) for s in stacks.values())
    individual_count = len(all_controls) - controls_in_stacks
    
    print("╔══════════════════════════════════════════════════════════╗")
    print("║                   EXECUTIVE SUMMARY                      ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print(f"║ {'Controls Implemented:':<40} {f'{len(all_controls)} / 93 ({completion_pct}%)':<16} ║")
    print(f"║ {'Full Implementation (POL+IMP+SCR):':<40} {f'{full_count} controls':<16} ║")
    print(f"║ {'Partial Implementation (POL+IMP):':<40} {f'{partial_count} controls':<16} ║")
    print(f"║ {'Basic Implementation (POL):':<40} {f'{basic_count} controls':<16} ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print(f"║ {'Stacks Detected:':<40} {f'{len(stacks)}':<16} ║")
    print(f"║ {'Controls in Stacks:':<40} {f'{controls_in_stacks}':<16} ║")
    print(f"║ {'Individual Controls:':<40} {f'{individual_count}':<16} ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print(f"║ {'Total Files:':<40} {f'{total_files}':<16} ║")
    print(f"║ {'Documentation Files:':<40} {f'{total_docs}':<16} ║")
    print(f"║ {'Python Scripts:':<40} {f'{len(scr_files)}':<16} ║")
    print(f"║ {'Excel Workbooks:':<40} {f'{len(xlsx_files)}':<16} ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print(f"║ {'Lines of Code:':<40} {f'{lines_code:,}':<16} ║")
    print(f"║ {'Lines of Documentation:':<40} {f'{lines_docs:,}':<16} ║")
    print(f"║ {'Total Lines:':<40} {f'{total_lines:,}':<16} ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()
    
    # ============================================================================
    # Export results
    # ============================================================================
    print("Exporting results...")
    
    # CSV export
    csv_path = project_path / 'isms-coverage-detail.csv'
    with open(csv_path, 'w') as f:
        f.write("Control|POL|IMP|SCR|POL_Count|IMP_Count|SCR_Count|Status|Stack\n")
        for control in sorted(all_controls, key=lambda x: (int(x.split('.')[1]), int(x.split('.')[2]))):
            data = coverage[control]
            stack_info = data['in_stack'] if data['in_stack'] else ''
            f.write(f"{control}|{int(data['pol'])}|{int(data['imp'])}|{int(data['scr'])}|"
                   f"{data['pol_count']}|{data['imp_count']}|{data['scr_count']}|{data['status']}|{stack_info}\n")
    
    # JSON export
    json_path = project_path / 'isms-analysis-report.json'
    report = {
        "analysis_date": datetime.now().strftime("%Y-%m-%d"),
        "summary": {
            "total_controls": len(all_controls),
            "completion_percentage": completion_pct,
            "full_implementation": full_count,
            "partial_implementation": partial_count,
            "basic_implementation": basic_count,
            "reference_only": ref_count,
            "stacks_detected": len(stacks),
            "controls_in_stacks": controls_in_stacks,
            "individual_controls": individual_count
        },
        "stacks": {stack_id: {
            'controls': stack_data['controls'],
            'pol_count': len(files_by_spec.get(stack_id, {}).get('pol', [])),
            'imp_count': len(files_by_spec.get(stack_id, {}).get('imp', [])),
            'scr_count': len(files_by_spec.get(stack_id, {}).get('scr', []))
        } for stack_id, stack_data in stacks.items()},
        "files": {
            "total": total_files,
            "policy": len(pol_files),
            "implementation": len(imp_files),
            "scripts": len(scr_files),
            "workbooks": len(xlsx_files)
        },
        "code_statistics": {
            "python_lines": lines_code,
            "documentation_lines": lines_docs,
            "total_lines": total_lines
        }
    }
    
    with open(json_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    # Control list export
    list_path = project_path / 'isms-control-list.txt'
    with open(list_path, 'w') as f:
        for control in all_controls:
            f.write(f"{control}\n")
    
    print(f"{Color.GREEN}✅ Reports exported:{Color.RESET}")
    print(f"  📄 isms-coverage-detail.csv")
    print(f"  📄 isms-analysis-report.json") 
    print(f"  📄 isms-control-list.txt")
    print()
    
    print(f"{Color.GREEN}════════════════════════════════════════════════════════════{Color.RESET}")
    print(f"{Color.GREEN}Analysis Complete!{Color.RESET}")
    print(f"{Color.GREEN}════════════════════════════════════════════════════════════{Color.RESET}")
    
    return report

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 analyze_isms_stack_file_detection.py <project_directory>")
        sys.exit(1)
    
    project_dir = sys.argv[1]
    if not os.path.isdir(project_dir):
        print(f"Error: {project_dir} is not a valid directory")
        sys.exit(1)
    
    analyze_project(project_dir)