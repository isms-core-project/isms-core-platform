# ISMS UTILITIES - NORMALIZED SCRIPTS GUIDE

## 📋 Complete Script Collection

All ISMS utility scripts now follow consistent naming: `isms_<function>.py/sh`

### **Core Utilities:**

| Script | Purpose | Usage |
|--------|---------|-------|
| `isms_scan_protection.py` | Scan framework for protection status | Standalone or automated |
| `isms_add_protection.py` | Add protection to single/multiple scripts | Core protection engine |
| `isms_protect_production.py` | Protect production scripts only | Recommended for large frameworks |
| `isms_protect_all.sh` | Bash wrapper for production protection | Alternative to Python version |
| `isms_remove_protection.py` | Remove protection (create unlocked versions) | Development/testing |
| `isms_run_all.sh` | **Master orchestrator - runs everything** | **⭐ START HERE** |

---

## 🚀 Quick Start

### **Option 1: Full Automated Workflow** ⭐ RECOMMENDED

Run everything in one command:

```bash
# Make scripts executable
chmod +x isms_*.sh

# Run complete workflow (scan → protect → scan → compare)
./isms_run_all.sh
```

**What it does:**
1. ✅ Scans current protection status (before)
2. ✅ Protects all production scripts (`*/10_generator_utf/`)
3. ✅ Scans protection status again (after)
4. ✅ Generates comparison report

**Output files:**
- `isms_scan_before_TIMESTAMP.txt`
- `isms_scan_after_TIMESTAMP.txt`
- `isms_comparison_TIMESTAMP.txt`

---

### **Option 2: Individual Scripts**

Run utilities separately for more control:

```bash
# 1. Scan current status
python3 isms_scan_protection.py --dir . --report scan_before.txt

# 2. Protect production scripts
python3 isms_protect_production.py

# 3. Scan after protection
python3 isms_scan_protection.py --dir . --report scan_after.txt

# 4. Compare manually
diff scan_before.txt scan_after.txt
```

---

## 📚 Detailed Usage

### **1. isms_run_all.sh - Master Orchestrator**

**Full workflow:**
```bash
./isms_run_all.sh
```

**Preview mode (safe):**
```bash
./isms_run_all.sh --dry-run
```

**Scan only:**
```bash
./isms_run_all.sh --scan-only
```

**Protect only (skip scans):**
```bash
./isms_run_all.sh --protect-only
```

---

### **2. isms_scan_protection.py - Status Scanner**

Recursively scans your ISMS framework and reports protection status.

**Basic scan:**
```bash
python3 isms_scan_protection.py --dir /path/to/ISMS
```

**Generate report:**
```bash
python3 isms_scan_protection.py --dir . --report protection_status.txt
```

**JSON output:**
```bash
python3 isms_scan_protection.py --dir . --format json --report status.json
```

**Output includes:**
- Total scripts found
- Functions protected vs unprotected
- Protection rate percentage
- Per-control breakdown
- Per-script analysis

---

### **3. isms_add_protection.py - Core Protection Engine**

Adds `ws.protection.sheet = True` to all sheet creation functions.

**Single script:**
```bash
python3 isms_add_protection.py generate_a824_1.py
```

**Dry run (preview):**
```bash
python3 isms_add_protection.py --dry-run generate_a824_1.py
```

**All scripts in directory:**
```bash
python3 isms_add_protection.py --all
```

**Features:**
- ✅ Auto-detects all `def create_*(ws...)` functions
- ✅ Creates `.bak` backups automatically
- ✅ Skips already-protected functions
- ✅ Handles multiple patterns (A.5.9, A.8.24, etc.)

---

### **4. isms_protect_production.py - Production Focus**

Targets ONLY production scripts (`*/10_generator_utf/`).

**Protect all production:**
```bash
python3 isms_protect_production.py
```

**Preview mode:**
```bash
python3 isms_protect_production.py --dry-run
```

**Specific control:**
```bash
python3 isms_protect_production.py --control a824
```

**With before/after reports:**
```bash
python3 isms_protect_production.py --with-reports
```

**Why use this?**
- Reduces scope from 357 scripts → ~127 production scripts
- Skips: `99_originals/`, `97_backup/`, `98_claude_ai/`
- Faster execution (only protect what matters)

---

### **5. isms_protect_all.sh - Bash Alternative**

Bash wrapper around `isms_add_protection.py` for production scripts.

**Protect all:**
```bash
./isms_protect_all.sh
```

**Preview:**
```bash
./isms_protect_all.sh --dry-run
```

**Verbose output:**
```bash
./isms_protect_all.sh -v
```

**Features:**
- ✅ Color-coded output
- ✅ Progress indicators
- ✅ Confirmation prompt
- ✅ Error handling

---

### **6. isms_remove_protection.py - Unlock Generator**

Creates unlocked versions of scripts (removes protection code).

**Single script:**
```bash
python3 isms_remove_protection.py generate_a824_1.py output_unlocked.py
```

**Scan for protection:**
```bash
python3 isms_remove_protection.py --scan generate_a824_1.py
```

**Batch process:**
```bash
python3 isms_remove_protection.py --batch ./locked/ ./unlocked/
```

**Use cases:**
- Development/debugging
- Testing workbook structure
- Creating editable templates

---

## 🎯 Common Workflows

### **Workflow 1: Initial Framework Protection**

Protect a brand new ISMS framework:

```bash
cd /path/to/ISMS/10-ISMS-SCR-Base

# Full automated workflow
./isms_run_all.sh
```

**Expected result:**
- Before: 1.9% protected (38 functions)
- After: 50-55% protected (~1,000 functions in production)

---

### **Workflow 2: Verify Protection Status**

Check current protection without making changes:

```bash
./isms_run_all.sh --scan-only
```

Or:

```bash
python3 isms_scan_protection.py --dir . --report status.txt
cat status.txt
```

---

### **Workflow 3: Update After Adding New Scripts**

You've added new generator scripts:

```bash
# Protect just the new scripts
python3 isms_add_protection.py new_script_1.py
python3 isms_add_protection.py new_script_2.py

# Or protect entire directory again (skips already-protected)
./isms_run_all.sh --protect-only
```

---

### **Workflow 4: Create Unlocked Development Versions**

Need unlocked versions for testing:

```bash
# Create unlocked version of specific script
python3 isms_remove_protection.py \
    generate_a824_1_crypto.py \
    generate_a824_1_crypto_UNLOCKED.py

# Batch create unlocked versions
python3 isms_remove_protection.py --batch ./production/ ./unlocked/
```

---

## 📊 Understanding Output

### **Scan Report Structure:**

```
ISMS FRAMEWORK PROTECTION SCAN REPORT
=====================================

EXECUTIVE SUMMARY
-----------------
Total Scripts Found:         357
Total Functions Analyzed:    2,013
Functions Protected:         1,038  (51.6%)
Functions Unprotected:       975   (48.4%)

PROTECTION BY CONTROL
---------------------
Control A.5.9:  100% (38/38 functions)
Control A.8.24: 45% (87/194 functions)
...

DETAILED SCRIPT ANALYSIS
------------------------
./ISMS-A.5.9/10_generator_utf/generate_a59_1.py
  Functions: 8
  Protected: 8 (100%)
  Status: ✅ Fully Protected
```

### **Protection Rate Targets:**

| Rate | Status | Meaning |
|------|--------|---------|
| 0-25% | ❌ Low | Many scripts unprotected |
| 25-50% | ⚠️ Medium | Production likely protected |
| 50-75% | ✅ Good | Production protected, archives not |
| 75-100% | ✅✅ Excellent | Comprehensive protection |

**Note:** 50-55% is PERFECT if:
- ✅ All production scripts (10_generator_utf/) are protected
- ⊘ Archives (99_originals/, 97_backup/) are NOT protected (intentional)

---

## 🔧 Troubleshooting

### **"No scripts found"**

**Cause:** Not in ISMS base directory

**Fix:**
```bash
cd /path/to/ISMS/10-ISMS-SCR-Base
./isms_run_all.sh
```

---

### **"isms_add_protection.py not found"**

**Cause:** Scripts not in same directory

**Fix:**
```bash
# Copy all isms_* scripts to your ISMS base directory
cp /path/to/downloads/isms_*.* .
chmod +x isms_*.sh
```

---

### **"Permission denied"**

**Cause:** Scripts not executable

**Fix:**
```bash
chmod +x isms_*.sh
```

---

### **Protection rate didn't increase**

**Cause:** Scripts already protected

**Check:**
```bash
# Look for "SKIP" messages in output
./isms_run_all.sh --dry-run
```

If all scripts show "already protected" - you're done! ✅

---

## 🎓 Advanced Usage

### **Filter by Control**

Protect only A.8.24 scripts:

```bash
python3 isms_protect_production.py --control a824
```

---

### **Custom Directory**

Protect scripts in specific location:

```bash
python3 isms_protect_production.py --dir /custom/path
```

---

### **Batch Verification**

Check multiple controls:

```bash
for control in a59 a824 a84; do
    python3 isms_scan_protection.py --dir . | grep -A 5 "$control"
done
```

---

## 📁 File Organization

**Recommended structure:**

```
/your/ISMS/base/
├── isms_scan_protection.py       # Core utilities
├── isms_add_protection.py
├── isms_protect_production.py
├── isms_protect_all.sh
├── isms_remove_protection.py
├── isms_run_all.sh               # Master script
│
├── ISMS-A.5.9-Inventory/         # Your controls
│   ├── 10_generator_utf/         # Production (target)
│   ├── 99_originals/             # Archives (skip)
│   └── 97_backup/                # Backups (skip)
│
├── ISMS-A.8.24-Cryptography/
│   ├── 10_generator_utf/         # Production (target)
│   └── ...
│
└── reports/                       # Generated reports
    ├── isms_scan_before_*.txt
    ├── isms_scan_after_*.txt
    └── isms_comparison_*.txt
```

---

## ✅ Success Checklist

After running `./isms_run_all.sh`, verify:

- [ ] No error messages in output
- [ ] Protection rate increased (check comparison report)
- [ ] All production scripts show "✓ Protected" or "⊘ SKIP (already protected)"
- [ ] Backup `.bak` files created for modified scripts
- [ ] Generated reports exist (`isms_scan_*.txt`)
- [ ] Can generate test workbook (sheets are protected)

---

## 🎯 Quick Command Reference

```bash
# Full workflow
./isms_run_all.sh

# Preview mode (safe)
./isms_run_all.sh --dry-run

# Scan only
python3 isms_scan_protection.py --dir . --report status.txt

# Protect production only
python3 isms_protect_production.py

# Protect single script
python3 isms_add_protection.py generate_script.py

# Create unlocked version
python3 isms_remove_protection.py script.py unlocked_script.py

# Verify protection
grep "Overall Protection Rate" isms_scan_after_*.txt
```

---

## 📞 Support

**Need help?**

1. Check script help: `python3 isms_<script>.py --help`
2. Run in dry-run mode first: `./isms_run_all.sh --dry-run`
3. Check generated reports for detailed analysis
4. Verify you're in the correct directory: `pwd`

---

## 🎉 You're Ready!

**Everything is normalized and ready to use.**

**Next steps:**
1. Copy all `isms_*` scripts to your ISMS base directory
2. Make shell scripts executable: `chmod +x isms_*.sh`
3. Run the master script: `./isms_run_all.sh`
4. Check the comparison report
5. Done! ✅

**All scripts work together seamlessly!** 🚀
