# Script Variation Analysis Guide
## Finding Variations in Your 300 ISMS Scripts

**Built in Bamboo Land 🎋**

---

## 🎯 Purpose

**You have ~300 scripts. You suspect 10-20 have variations.**

**This guide helps you:**
1. **Identify** what varies
2. **Understand** if variations are intentional or accidental
3. **Decide** what (if anything) to standardize

---

## 🛠️ Two Tools Available

### **1. Python Analyzer (Comprehensive)**

**File:** `analyze_script_variations.py`

**Best for:**
- Deep analysis of patterns
- Statistical breakdown
- Consistency scoring
- Detailed recommendations

**Usage:**
```bash
python3 analyze_script_variations.py /path/to/scripts/folder/
```

---

### **2. Bash Quick Check (Fast)**

**File:** `quick_pattern_check.sh`

**Best for:**
- Quick overview
- Fast pattern checking
- No Python dependencies
- Simple output

**Usage:**
```bash
chmod +x quick_pattern_check.sh
./quick_pattern_check.sh /path/to/scripts/folder/
```

---

## 🔍 What Gets Analyzed

### **Import Patterns**
- Which libraries are used most
- Rare/unique imports (potential outliers)
- Import consistency across scripts

**Why it matters:** 
- Accidental variations: `import os` vs `from os import path`
- Intentional variations: Some controls need `requests`, others don't

---

### **Function Names**
- Common function patterns
- Unique function names
- Naming consistency

**Why it matters:**
- Accidental: `generate_workbook()` vs `create_workbook()` doing same thing
- Intentional: Different controls need different functions

---

### **Workbook Naming**
- Filename patterns
- Date format in filenames
- Naming conventions

**Why it matters:**
- Accidental: `assessment_A57.xlsx` vs `A.5.7_assessment.xlsx`
- Intentional: Different formats for different control types

---

### **Date Formatting**
- strftime patterns
- Date format consistency
- Timestamp usage

**Why it matters:**
- Accidental: `%Y-%m-%d` vs `%d-%m-%Y` randomly
- Intentional: Different date formats for different purposes

---

### **Error Handling**
- Scripts with try/except
- Scripts with logging
- Scripts without error handling

**Why it matters:**
- **This should be standardized** - all scripts should handle errors
- Missing error handling = potential bugs

---

### **Excel Sheet Patterns**
- Number of sheets per workbook
- Sheet naming patterns
- Sheet creation approach

**Why it matters:**
- Intentional: A.5.7 needs 5 sheets, A.6.3 needs 3 sheets
- This variation is CORRECT

---

## 📊 Interpreting Results

### **Consistency Score >= 85%**

✅ **EXCELLENT**

**What it means:**
- High standardization
- Variations are likely intentional
- Well-architected codebase

**Action:**
- Document why variations exist
- Continue building
- No refactoring needed

---

### **Consistency Score 70-84%**

✅ **GOOD**

**What it means:**
- Reasonable standardization
- Some variations exist
- Worth investigating outliers

**Action:**
- Review outliers (shown in report)
- Determine if accidental or intentional
- Add comments to explain variations
- Light refactoring if time permits

---

### **Consistency Score < 70%**

⚠️ **MODERATE**

**What it means:**
- Significant variations
- May be intentional (different control types)
- May be accidental (early scripts vs later scripts)

**Action:**
- Identify patterns vs chaos
- Document intentional variations
- Standardize accidental variations (low priority)
- Focus on error handling first

---

## 🎯 Decision Framework

**For each variation found, ask:**

### **1. Does it cause bugs?**
- **Yes** → Fix immediately
- **No** → Continue to #2

### **2. Is it confusing to maintain?**
- **Yes** → Document WHY it's different
- **No** → Continue to #3

### **3. Is the variation intentional?**
- **Yes** → Document and leave it
- **No** → Consider standardizing (low priority)

### **4. Would standardization break functionality?**
- **Yes** → DON'T standardize
- **No** → Consider standardizing (when convenient)

---

## 🛠️ One-Liner Bash Checks

**Don't want to run the full analysis? Here are quick commands:**

### **Find scripts without error handling:**
```bash
find /path/to/scripts -name "*.py" -exec sh -c \
  '! grep -q "try:\|except" "$1" && echo "$1"' _ {} \;
```

### **Count different date formats:**
```bash
grep -r "strftime" /path/to/scripts/*.py | \
  grep -o "strftime(['\"][^'\"]*['\"])" | \
  sort | uniq -c | sort -rn
```

### **Find different import patterns:**
```bash
grep -rh "^import\|^from" /path/to/scripts/*.py | \
  sort | uniq -c | sort -rn | head -20
```

### **Compare workbook naming:**
```bash
grep -rh "workbook_name\|filename.*=" /path/to/scripts/*.py | \
  grep -v "^#" | sort | uniq
```

### **Find functions used once (potential candidates for consolidation):**
```bash
grep -rh "^def " /path/to/scripts/*.py | \
  sed 's/def \([a-zA-Z_]*\).*/\1/' | \
  sort | uniq -c | grep "^ *1 "
```

---

## 💡 Example Analysis Session

**Scenario:** You run the Python analyzer

### **Sample Output:**
```
📊 Total Scripts Analyzed: 287

📦 IMPORT PATTERNS
  import pandas as pd                      285 scripts (99.3%)
  import xlsxwriter                        280 scripts (97.6%)
  import datetime                          275 scripts (95.8%)
  from pathlib import Path                 270 scripts (94.1%)
  import requests                           12 scripts (4.2%)   ← OUTLIER

⚠️  Rare imports (< 5 scripts):
     • import requests (12 scripts)
     • import json (8 scripts)
     • import yaml (3 scripts)
```

### **Interpretation:**

✅ **99% use pandas/xlsxwriter** - Excellent standardization

⚠️ **12 scripts use requests** - These are probably:
- A.5.7 (Threat Intelligence) - needs to fetch CTI feeds
- A.8.16 (Monitoring) - needs to query APIs
- A.5.23 (Cloud Services) - needs to check cloud APIs

**Conclusion:** This variation is INTENTIONAL and CORRECT.

**Action:** Add comment to those 12 scripts:
```python
import requests  # Required for API integration (A.5.7 CTI feeds)
```

---

### **Sample Output - Error Handling:**
```
⚠️  ERROR HANDLING APPROACHES
  try_except                               245 scripts (85.4%)
  logging                                   89 scripts (31.0%)
  sys_exit                                 267 scripts (93.0%)
  none                                      42 scripts (14.6%)

⚠️  Scripts without error handling:
     • generate_a534_assessment.py
     • generate_a636_assessment.py
     ... (40 more)
```

### **Interpretation:**

⚠️ **14.6% lack error handling** - This should be fixed

**Action:** Add try/except to those 42 scripts (2-3 hours work)

---

### **Sample Output - Date Formats:**
```
📅 DATE FORMAT PATTERNS
  %Y-%m-%d                                 245 scripts (85.4%)
  %d-%m-%Y                                  28 scripts (9.8%)
  %Y%m%d                                    14 scripts (4.9%)
```

### **Interpretation:**

✅ **85% use YYYY-MM-DD** - Good standardization

⚠️ **15% use other formats** - Probably accidental

**Action:** Consider standardizing to `%Y-%m-%d` when touching those scripts

---

## 📋 Recommended Workflow

### **Step 1: Run Analysis**
```bash
python3 analyze_script_variations.py /path/to/scripts/ > analysis_report.txt
```

### **Step 2: Review Report**
Open `analysis_report.txt` and look for:
- Consistency score
- Error handling gaps
- Obvious accidental variations

### **Step 3: Prioritize**
1. **HIGH**: Missing error handling → Add it
2. **MEDIUM**: Accidental date format variations → Document for future
3. **LOW**: Function name variations → Probably intentional

### **Step 4: Document**
Add comments to explain intentional variations:

```python
#!/usr/bin/env python3
"""
ISMS Assessment Generator: A.5.7 Threat Intelligence

NOTE: This script uses different imports than standard assessment scripts:
- requests: Required for CTI feed API integration
- json: Required for IOC parsing
This is INTENTIONAL due to control requirements.
"""
```

### **Step 5: Commit**
```bash
git add .
git commit -m "Add error handling to 42 scripts

- Added try/except blocks to all assessment generators
- Consistent error handling across platform
- Improved reliability"
git push
```

---

## 🎋 The Bamboo Principle

**Remember:**

**93% standardized = Excellent**  
**7% variations = Probably intentional**  

**Don't fool yourself that 100% uniformity is better.**

**Bamboo adapts to conditions.**  
**Your scripts should too.**

---

## 🎯 TL;DR

**Run this:**
```bash
python3 analyze_script_variations.py /path/to/your/scripts/
```

**Look for:**
- Consistency score (hope for >85%)
- Missing error handling (fix this)
- Outlier patterns (probably intentional)

**Do this:**
- Document WHY variations exist
- Add error handling where missing
- Don't refactor just to refactor

**Remember:**
- Variations aren't bad if intentional
- Over-standardization is cargo cult
- Focus on functionality, not uniformity

---

**Built in Bamboo Land 🎋**  
**Copyright © 2026 Gregory Griffin**

*Measure first, decide second.* 📊
