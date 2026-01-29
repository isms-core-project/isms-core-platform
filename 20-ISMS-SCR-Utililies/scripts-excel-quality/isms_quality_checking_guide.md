# ISMS QUALITY CHECKING UTILITIES

## 📋 New Quality Checking Scripts

| Script | Purpose | Tests |
|--------|---------|-------|
| `isms_check_circular_refs.py` | Detect circular references in Excel workbooks | Generated workbooks |
| `isms_check_formula_quality.py` | Check generator scripts for formula quality issues | Python scripts |

---

## 🎯 isms_check_circular_refs.py

**Purpose:** Automatically detect circular reference errors in generated Excel workbooks.

### **What It Checks:**

1. ✅ **Direct self-references** - Cell A1 references itself
2. ✅ **Range inclusion errors** - Cell A5 is in range A1:A10 (circular)
3. ✅ **Sheet-by-sheet analysis** - Tests every sheet in workbook
4. ✅ **Multi-file testing** - Test multiple workbooks at once

### **Usage:**

**Single workbook:**
```bash
python3 isms_check_circular_refs.py dashboard.xlsx
```

**Multiple workbooks:**
```bash
python3 isms_check_circular_refs.py *.xlsx
```

**Specific pattern:**
```bash
python3 isms_check_circular_refs.py ISMS-IMP-A.5.9.*.xlsx
```

### **Example Output:**

**Clean workbook:**
```
================================================================================
SCANNING: ISMS-IMP-A.5.9.1_Asset_Discovery_20260125.xlsx
================================================================================
✅ Instructions & Legend: Clean
✅ Information Assets Discovery: Clean
✅ IT Infrastructure Discovery: Clean
✅ Applications Discovery: Clean
✅ Physical Assets Discovery: Clean
✅ Personnel Assets Discovery: Clean
✅ Discovery Metrics & Summary: Clean
✅ Evidence Register: Clean

================================================================================
✅ NO CIRCULAR REFERENCES DETECTED
================================================================================
```

**Workbook with issues:**
```
================================================================================
SCANNING: problem_workbook.xlsx
================================================================================

❌ Summary Dashboard:
  DIRECT CIRCULAR: D10 references itself
  Formula: =D10*100

  RANGE CIRCULAR: B5 is within range B1:B10
  Formula: =SUM(B1:B10)

================================================================================
❌ FOUND 2 CIRCULAR REFERENCE(S)
================================================================================
```

**Multiple files:**
```
Testing 4 file(s)...

✅ ISMS-IMP-A.5.9.1_Asset_Discovery_20260125.xlsx: Clean
✅ ISMS-IMP-A.5.9.2_Inventory_Maintenance_20260125.xlsx: Clean
❌ ISMS-IMP-A.5.9.3_Quality_Compliance_20260125.xlsx: 2 issue(s)
✅ ISMS-IMP-A.5.9.4_Owner_Accountability_20260125.xlsx: Clean

================================================================================
SUMMARY: 3/4 passed

Failed files:
  - ISMS-IMP-A.5.9.3_Quality_Compliance_20260125.xlsx
================================================================================
```

### **Exit Codes:**

- **0** = No circular references found (all passed)
- **1** = Circular references detected (failed)

### **Integration with CI/CD:**

```bash
# In your test script
python3 isms_check_circular_refs.py generated_workbooks/*.xlsx
if [ $? -ne 0 ]; then
    echo "ERROR: Circular references detected!"
    exit 1
fi
```

### **When to Use:**

✅ **After generating workbooks** - Verify no formula errors  
✅ **Before deployment** - Quality gate  
✅ **CI/CD pipeline** - Automated testing  
✅ **Debugging** - Find formula issues quickly

---

## 🔍 isms_check_formula_quality.py

**Purpose:** Analyze Python generator scripts for formula quality issues and best practices.

### **What It Checks:**

#### **🔴 ISSUES (Must Fix):**

1. **Off-by-one errors** - Range includes formula cell itself
2. **Unmatched parentheses** - Formula syntax errors
3. **TODO/FIXME comments** - Unfinished code
4. **Formula syntax errors** - Potential Excel errors

#### **🟡 WARNINGS (Review Recommended):**

1. **Hardcoded dates** - Should use TODAY()/NOW()
2. **Volatile functions** - NOW(), RAND(), OFFSET(), INDIRECT()
3. **Inconsistent date formats** - Multiple formats in same script
4. **Missing data validation** - Input cells without validation
5. **Large hardcoded ranges** - A1:Z1000 (might need dynamic)
6. **Inconsistent percentage formatting** - Mixed methods
7. **External references** - Verify source files exist
8. **Sheet naming inconsistency** - Spaces vs underscores
9. **Missing approval sheets** - ISO 27001 requirement

### **Usage:**

**Single script:**
```bash
python3 isms_check_formula_quality.py generate_a824_1.py
```

**Multiple scripts:**
```bash
python3 isms_check_formula_quality.py generate_a824_*.py
```

**All generators:**
```bash
python3 isms_check_formula_quality.py generate_*.py
```

### **Example Output:**

**Clean script:**
```
================================================================================
QUALITY CHECK: generate_a59_1_asset_discovery_UPDATED.py
================================================================================
✅ No issues or warnings found
```

**Script with issues:**
```
================================================================================
QUALITY CHECK: generate_a824_5_dashboard.py
================================================================================

❌ ISSUES (Should Fix):
--------------------------------------------------------------------------------

TODO COMMENTS:
  Line 42: TODO comment found
    # TODO: Add validation for date ranges

  Line 156: FIXME comment found
    # FIXME: This formula might have off-by-one error

FORMULA SYNTAX:
  Line 234: Unmatched parentheses: 3 open, 2 close
    value = "=SUM(A1:A10+(B1:B10"

⚠️  WARNINGS (Review Recommended):
--------------------------------------------------------------------------------

VOLATILE FUNCTIONS:
  Line 89: NOW()
    Volatile - recalculates constantly (use TODAY() if time not needed)

  Line 123: OFFSET(
    Volatile - consider INDEX/MATCH alternative

HARDCODED DATES:
  Line 67: "2024-01-01"
    Hardcoded date (YYYY-MM-DD) - use TODAY() or NOW()

LARGE RANGES:
  Line 201: A1:Z1000
    Large hardcoded range (1000 rows) - consider if dynamic range needed

================================================================================
SUMMARY: 4 issue(s), 3 warning(s)
================================================================================
```

### **Exit Codes:**

- **0** = No issues found (warnings OK)
- **1** = Issues detected

### **Integration with Development:**

```bash
# Pre-commit hook
python3 isms_check_formula_quality.py generate_*.py
if [ $? -ne 0 ]; then
    echo "ERROR: Formula quality issues detected!"
    echo "Fix issues before committing"
    exit 1
fi
```

### **When to Use:**

✅ **Before committing code** - Catch issues early  
✅ **Code review** - Quality checklist  
✅ **Refactoring** - Identify improvement areas  
✅ **Debugging** - Find formula problems

---

## 🔄 Common Workflows

### **Workflow 1: Test New Generator Script**

Verify script quality before generating workbooks:

```bash
# Step 1: Check script quality
python3 isms_check_formula_quality.py generate_new_script.py

# Step 2: Generate workbook
python3 generate_new_script.py

# Step 3: Check for circular references
python3 isms_check_circular_refs.py ISMS-*.xlsx
```

---

### **Workflow 2: Batch Test All A.5.9 Scripts**

Quality check entire control:

```bash
# Check all generator scripts
python3 isms_check_formula_quality.py generate_a59_*.py

# Generate all workbooks
for script in generate_a59_*.py; do
    python3 "$script"
done

# Test all workbooks
python3 isms_check_circular_refs.py ISMS-IMP-A.5.9.*.xlsx
```

---

### **Workflow 3: CI/CD Pipeline Integration**

Add to automated testing:

```bash
#!/bin/bash
# test_isms_quality.sh

echo "Step 1: Check generator script quality..."
python3 isms_check_formula_quality.py generate_*.py
if [ $? -ne 0 ]; then
    echo "FAILED: Formula quality issues"
    exit 1
fi

echo "Step 2: Generate workbooks..."
for script in generate_*.py; do
    python3 "$script"
done

echo "Step 3: Check for circular references..."
python3 isms_check_circular_refs.py *.xlsx
if [ $? -ne 0 ]; then
    echo "FAILED: Circular references detected"
    exit 1
fi

echo "✅ ALL QUALITY CHECKS PASSED"
```

---

### **Workflow 4: Fix Issues Found**

Use checker output to guide fixes:

```bash
# Run quality check
python3 isms_check_formula_quality.py problematic_script.py > issues.txt

# Review issues
cat issues.txt

# Fix issues in editor
# ...

# Re-test
python3 isms_check_formula_quality.py problematic_script.py
```

---

## 🎓 Understanding Issues

### **Circular Reference Examples:**

**❌ Bad - Direct self-reference:**
```python
ws['D10'].value = "=D10*100"  # D10 references itself!
```

**✅ Good - Reference other cell:**
```python
ws['D10'].value = "=D9*100"  # D10 references D9
```

**❌ Bad - Range includes self:**
```python
ws['B5'].value = "=SUM(B1:B10)"  # B5 is in range B1:B10!
```

**✅ Good - Range excludes self:**
```python
ws['B5'].value = "=SUM(B1:B4)"  # B5 sums B1-B4 only
```

---

### **Formula Quality Examples:**

**❌ Bad - Hardcoded date:**
```python
ws.value = "='2024-01-01'"
```

**✅ Good - Dynamic date:**
```python
ws.value = "=TODAY()"
```

**❌ Bad - Volatile function:**
```python
ws.value = "=NOW()"  # Recalculates constantly
```

**✅ Good - Non-volatile alternative:**
```python
ws.value = "=TODAY()"  # Only recalculates once per day
```

**❌ Bad - No validation on input:**
```python
ws['A1'].fill = input_fill  # User can enter anything
```

**✅ Good - Validated input:**
```python
ws['A1'].fill = input_fill
dv = DataValidation(type="list", formula1='"Option1,Option2,Option3"')
dv.add('A1')
ws.add_data_validation(dv)
```

---

## 📊 Quality Metrics

### **Clean Script Standards:**

| Metric | Target | Status |
|--------|--------|--------|
| TODO/FIXME comments | 0 | ❌ Must fix |
| Formula syntax errors | 0 | ❌ Must fix |
| Off-by-one errors | 0 | ❌ Must fix |
| Hardcoded dates | 0 | ⚠️ Should fix |
| Volatile functions | <3 | ⚠️ Review usage |
| Data validation | On all inputs | ⚠️ Recommended |

### **Production Readiness:**

✅ **Ready for production:**
- 0 issues
- 0-2 warnings (documented)

⚠️ **Review needed:**
- 0 issues
- 3+ warnings

❌ **Not production ready:**
- Any issues present

---

## 🔧 Troubleshooting

### **isms_check_circular_refs.py Issues:**

**"Could not load workbook"**
- Workbook is corrupted
- File is password-protected
- File is open in Excel

**Fix:**
```bash
# Close file in Excel
# Try opening with Excel to verify it's not corrupted
# Remove password protection if present
```

**"No circular references but Excel shows error"**
- Script checks common patterns
- May miss complex indirect references
- Manually verify in Excel

---

### **isms_check_formula_quality.py Issues:**

**"File not found"**
- Check file path
- Use tab completion
- Verify current directory

**False positives on hardcoded dates**
- Some dates are intentional (audit periods, etc.)
- Review each case
- Add comment explaining if needed

**Too many warnings**
- Review warnings, not all require fixes
- Focus on issues first
- Document intentional choices

---

## 📁 Integration with ISMS Utilities

These quality checkers complement the protection utilities:

```
ISMS Utilities Ecosystem:
│
├── Protection (what we did before)
│   ├── isms_scan_protection.py
│   ├── isms_add_protection.py
│   ├── isms_protect_production.py
│   └── isms_run_all.sh
│
└── Quality Checking (NEW)
    ├── isms_check_circular_refs.py  ← Test generated workbooks
    └── isms_check_formula_quality.py ← Test generator scripts
```

---

## ✅ Testing Checklist

Before deploying a new generator script:

### **Script Quality:**
- [ ] Run `isms_check_formula_quality.py`
- [ ] Fix all issues (red)
- [ ] Review all warnings (yellow)
- [ ] Document intentional choices

### **Workbook Quality:**
- [ ] Generate test workbook
- [ ] Run `isms_check_circular_refs.py`
- [ ] Open in Excel and verify
- [ ] Test all formulas manually

### **Protection:**
- [ ] Run `isms_add_protection.py`
- [ ] Verify sheets are protected
- [ ] Test input cells are editable

---

## 🎯 Quick Command Reference

```bash
# Check generator script quality
python3 isms_check_formula_quality.py <script.py>

# Check workbook for circular references
python3 isms_check_circular_refs.py <workbook.xlsx>

# Batch test multiple scripts
python3 isms_check_formula_quality.py generate_*.py

# Batch test multiple workbooks
python3 isms_check_circular_refs.py *.xlsx

# CI/CD integration (exit code 0 = pass)
python3 isms_check_circular_refs.py *.xlsx && echo "PASSED" || echo "FAILED"
```

---

## 🎉 Benefits

### **Catch Errors Early:**
✅ Find circular references before deployment  
✅ Detect formula issues during development  
✅ Automated quality gates

### **Improve Code Quality:**
✅ Follow best practices  
✅ Consistent formula patterns  
✅ Better maintainability

### **Save Time:**
✅ No manual testing needed  
✅ Instant feedback  
✅ Automated workflows

---

## 📚 Complete Utility Suite

**All ISMS utilities now available:**

1. ✅ `isms_scan_protection.py` - Scan protection status
2. ✅ `isms_add_protection.py` - Add sheet protection
3. ✅ `isms_protect_production.py` - Protect production scripts
4. ✅ `isms_protect_all.sh` - Bash wrapper
5. ✅ `isms_remove_protection.py` - Remove protection
6. ✅ `isms_run_all.sh` - Master orchestrator
7. ✅ **`isms_check_circular_refs.py`** - NEW: Check workbooks
8. ✅ **`isms_check_formula_quality.py`** - NEW: Check scripts

**Complete workflow support from development to deployment!** 🚀
