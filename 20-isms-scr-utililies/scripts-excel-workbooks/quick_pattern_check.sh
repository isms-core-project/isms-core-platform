#!/bin/bash
# ISMS CORE Quick Pattern Checker
# Purpose: Fast pattern analysis across Python scripts
# Usage: ./quick_pattern_check.sh /path/to/scripts/

SCRIPTS_DIR="${1:-.}"

if [ ! -d "$SCRIPTS_DIR" ]; then
    echo "❌ Error: Directory not found: $SCRIPTS_DIR"
    exit 1
fi

echo "🔍 ISMS CORE Quick Pattern Check"
echo "📁 Directory: $SCRIPTS_DIR"
echo ""

# Count total scripts
TOTAL=$(find "$SCRIPTS_DIR" -name "*.py" | wc -l)
echo "📊 Total Python scripts: $TOTAL"
echo ""

echo "=" | head -c 80 | tr -d '\n'; echo ""
echo "📦 IMPORT ANALYSIS"
echo "=" | head -c 80 | tr -d '\n'; echo ""

echo ""
echo "Most common imports:"
grep -h "^import\|^from" "$SCRIPTS_DIR"/**/*.py 2>/dev/null | \
    sort | uniq -c | sort -rn | head -10 | \
    awk '{printf "  %-5s %s\n", $1, substr($0, index($0,$2))}'

echo ""
echo "Rare imports (appears once):"
grep -h "^import\|^from" "$SCRIPTS_DIR"/**/*.py 2>/dev/null | \
    sort | uniq -c | sort -n | grep "^ *1 " | head -10 | \
    awk '{printf "  • %s\n", substr($0, index($0,$2))}'

echo ""
echo "=" | head -c 80 | tr -d '\n'; echo ""
echo "📄 WORKBOOK NAMING PATTERNS"
echo "=" | head -c 80 | tr -d '\n'; echo ""

echo ""
echo "Filename variable patterns:"
grep -h "workbook_name\|filename.*=" "$SCRIPTS_DIR"/**/*.py 2>/dev/null | \
    head -10 | sed 's/^/  • /'

echo ""
echo "=" | head -c 80 | tr -d '\n'; echo ""
echo "📅 DATE FORMAT PATTERNS"
echo "=" | head -c 80 | tr -d '\n'; echo ""

echo ""
DATE_PATTERNS=$(grep -h "strftime" "$SCRIPTS_DIR"/**/*.py 2>/dev/null | \
    grep -o "strftime(['\"][^'\"]*['\"])" | sort | uniq -c | sort -rn)

if [ -z "$DATE_PATTERNS" ]; then
    echo "  ℹ️  No date formatting patterns found"
else
    echo "$DATE_PATTERNS" | awk '{printf "  %-5s %s\n", $1, substr($0, index($0,$2))}'
fi

echo ""
echo "=" | head -c 80 | tr -d '\n'; echo ""
echo "⚠️  ERROR HANDLING"
echo "=" | head -c 80 | tr -d '\n'; echo ""

WITH_TRY=$(grep -l "try:" "$SCRIPTS_DIR"/**/*.py 2>/dev/null | wc -l)
WITH_LOGGING=$(grep -l "logging\." "$SCRIPTS_DIR"/**/*.py 2>/dev/null | wc -l)
WITHOUT_ERROR=$(find "$SCRIPTS_DIR" -name "*.py" -exec sh -c '
    ! grep -q "try:\|except\|logging\." "$1"
' _ {} \; -print 2>/dev/null | wc -l)

echo ""
echo "  Scripts with try/except:     $WITH_TRY / $TOTAL"
echo "  Scripts with logging:        $WITH_LOGGING / $TOTAL"
echo "  Scripts without error handling: $WITHOUT_ERROR / $TOTAL"

if [ "$WITHOUT_ERROR" -gt 0 ]; then
    echo ""
    echo "  Scripts without error handling:"
    find "$SCRIPTS_DIR" -name "*.py" -exec sh -c '
        if ! grep -q "try:\|except\|logging\." "$1"; then
            basename "$1"
        fi
    ' _ {} \; 2>/dev/null | head -10 | sed 's/^/     • /'
fi

echo ""
echo "=" | head -c 80 | tr -d '\n'; echo ""
echo "🔧 COMMON FUNCTION NAMES"
echo "=" | head -c 80 | tr -d '\n'; echo ""

echo ""
echo "Most common functions:"
grep -h "^def " "$SCRIPTS_DIR"/**/*.py 2>/dev/null | \
    sed 's/def \([a-zA-Z_]*\).*/\1/' | \
    sort | uniq -c | sort -rn | head -10 | \
    awk '{printf "  %-5s %s()\n", $1, $2}'

echo ""
echo "=" | head -c 80 | tr -d '\n'; echo ""
echo "📊 EXCEL SHEET PATTERNS"
echo "=" | head -c 80 | tr -d '\n'; echo ""

echo ""
SHEET_COUNT=$(grep -c "add_worksheet\|sheet_name=" "$SCRIPTS_DIR"/**/*.py 2>/dev/null)
echo "  Total sheet creations: $SHEET_COUNT"

echo ""
echo "Sheet naming samples:"
grep -h "add_worksheet\|sheet_name=" "$SCRIPTS_DIR"/**/*.py 2>/dev/null | \
    grep -o "['\"][^'\"]*['\"]" | head -10 | sed 's/^/  • /'

echo ""
echo "=" | head -c 80 | tr -d '\n'; echo ""
echo "💡 QUICK ASSESSMENT"
echo "=" | head -c 80 | tr -d '\n'; echo ""

echo ""

# Calculate error handling percentage
ERROR_PCT=$(awk "BEGIN {printf \"%.1f\", ($WITH_TRY / $TOTAL) * 100}")

if (( $(echo "$ERROR_PCT >= 85" | bc -l) )); then
    echo "  ✅ Error handling: Excellent ($ERROR_PCT%)"
elif (( $(echo "$ERROR_PCT >= 70" | bc -l) )); then
    echo "  ✅ Error handling: Good ($ERROR_PCT%)"
else
    echo "  ⚠️  Error handling: Needs improvement ($ERROR_PCT%)"
fi

# Check for variations
IMPORT_VARIATIONS=$(grep -h "^import\|^from" "$SCRIPTS_DIR"/**/*.py 2>/dev/null | \
    sort | uniq | wc -l)
echo "  📦 Unique import patterns: $IMPORT_VARIATIONS"

DATE_VARIATIONS=$(grep -h "strftime" "$SCRIPTS_DIR"/**/*.py 2>/dev/null | \
    grep -o "strftime(['\"][^'\"]*['\"])" | sort | uniq | wc -l)

if [ "$DATE_VARIATIONS" -gt 1 ]; then
    echo "  ⚠️  Multiple date formats detected: $DATE_VARIATIONS different patterns"
fi

echo ""
echo "🎋 Quick check complete! Built in Bamboo Land"
echo ""
