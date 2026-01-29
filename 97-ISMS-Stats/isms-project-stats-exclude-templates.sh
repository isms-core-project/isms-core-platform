#!/bin/bash

# ISMS Project Statistics Generator (macOS Compatible - Excludes Templates)
# Analyzes the ISMS framework implementation and generates comprehensive statistics
# Compatible with bash 3.2+ (macOS default)
# Automatically excludes template/base folders to avoid duplicate counting

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║        ISMS Project Statistics Generator                   ║${NC}"
echo -e "${BLUE}║        ISO 27001:2022 Implementation Analysis              ║${NC}"
echo -e "${BLUE}║        (Excludes Template/Base Folders)                    ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo

# Folders to exclude (only knowledge base templates)
EXCLUDE_PATTERNS=(
    "00-ISMS-POL-KB"
)

# Get project root directory
if [ -z "$1" ]; then
    echo -e "${YELLOW}Usage: $0 <project_directory>${NC}"
    echo "Example: $0 /path/to/isms-project"
    exit 1
fi

PROJECT_DIR="$1"

if [ ! -d "$PROJECT_DIR" ]; then
    echo -e "${RED}Error: Directory $PROJECT_DIR does not exist${NC}"
    exit 1
fi

cd "$PROJECT_DIR"

echo -e "${GREEN}Analyzing project in: ${PROJECT_DIR}${NC}"
echo -e "${YELLOW}Excluding template/base folders:${NC}"
for pattern in "${EXCLUDE_PATTERNS[@]}"; do
    echo "  - $pattern"
done
echo

# Build find exclude arguments
FIND_EXCLUDE_ARGS=""
for pattern in "${EXCLUDE_PATTERNS[@]}"; do
    FIND_EXCLUDE_ARGS="$FIND_EXCLUDE_ARGS -path ./$pattern -prune -o"
done

# Initialize counters
TOTAL_FILES=0
TOTAL_DIRS=0
TOTAL_POL_FILES=0
TOTAL_IMP_FILES=0
TOTAL_SCR_FILES=0
TOTAL_WORKBOOKS=0
TOTAL_MD_FILES=0
TOTAL_PY_FILES=0
TOTAL_LINES_CODE=0
TOTAL_LINES_DOCS=0

# Control tracking using temp files (bash 3.2 compatible)
TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

CONTROLS_FILE="$TEMP_DIR/controls_found.txt"
CONTROL_FOLDERS_FILE="$TEMP_DIR/control_folders.txt"
touch "$CONTROLS_FILE"
touch "$CONTROL_FOLDERS_FILE"

echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}FILE STATISTICS${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}\n"

# Count total files and directories (excluding patterns)
TOTAL_FILES=$(eval "find . $FIND_EXCLUDE_ARGS -type f -print" | wc -l | tr -d ' ')
TOTAL_DIRS=$(eval "find . $FIND_EXCLUDE_ARGS -type d -print" | wc -l | tr -d ' ')

echo "📁 Total Directories:          $TOTAL_DIRS"
echo "📄 Total Files:                $TOTAL_FILES"
echo

# Count by file type (excluding patterns)
TOTAL_MD_FILES=$(eval "find . $FIND_EXCLUDE_ARGS -name '*.md' -type f -print" 2>/dev/null | wc -l | tr -d ' ')
TOTAL_PY_FILES=$(eval "find . $FIND_EXCLUDE_ARGS -name '*.py' -type f -print" 2>/dev/null | wc -l | tr -d ' ')
TOTAL_WORKBOOKS=$(eval "find . $FIND_EXCLUDE_ARGS -name '*.xlsx' -type f -print" 2>/dev/null | wc -l | tr -d ' ')

# Count POL/IMP/SCR files (excluding patterns)
TOTAL_POL_FILES=$(eval "find . $FIND_EXCLUDE_ARGS -type f \( -name '*POL*.md' -o -name '*Policy*.md' \) -print" 2>/dev/null | wc -l | tr -d ' ')
TOTAL_IMP_FILES=$(eval "find . $FIND_EXCLUDE_ARGS -type f \( -name '*IMP*.md' -o -name '*Implementation*.md' \) -print" 2>/dev/null | wc -l | tr -d ' ')
TOTAL_SCR_FILES=$(eval "find . $FIND_EXCLUDE_ARGS -type f \( -name '*SCR*.py' -o -name '*Script*.py' -o -path '*/scripts/*.py' \) -print" 2>/dev/null | wc -l | tr -d ' ')

echo "📝 Markdown Documents:         $TOTAL_MD_FILES"
echo "🐍 Python Scripts:             $TOTAL_PY_FILES"
echo "📊 Excel Workbooks:            $TOTAL_WORKBOOKS"
echo
echo "Document Breakdown:"
echo "  • POL (Policy) Files:        $TOTAL_POL_FILES"
echo "  • IMP (Implementation):      $TOTAL_IMP_FILES"
echo "  • SCR (Scripts):             $TOTAL_SCR_FILES"
echo

# Count lines of code
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}CODE STATISTICS${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}\n"

if [ "$TOTAL_PY_FILES" -gt 0 ]; then
    echo "Counting Python lines of code..."
    TOTAL_LINES_CODE=$(eval "find . $FIND_EXCLUDE_ARGS -name '*.py' -type f -print" 2>/dev/null | xargs cat 2>/dev/null | wc -l | tr -d ' ')
    echo "🐍 Total Python Lines:         $TOTAL_LINES_CODE"
fi

if [ "$TOTAL_MD_FILES" -gt 0 ]; then
    echo "Counting Markdown documentation lines..."
    TOTAL_LINES_DOCS=$(eval "find . $FIND_EXCLUDE_ARGS -name '*.md' -type f -print" 2>/dev/null | xargs cat 2>/dev/null | wc -l | tr -d ' ')
    echo "📝 Total Markdown Lines:       $TOTAL_LINES_DOCS"
fi

TOTAL_LINES=$((TOTAL_LINES_CODE + TOTAL_LINES_DOCS))
echo "📏 Total Lines (Code + Docs):  $TOTAL_LINES"
echo

# Identify controls implemented
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}CONTROL ANALYSIS${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}\n"

echo "Scanning for ISO 27001:2022 Annex A controls (excluding templates)..."

# Pattern matching for controls (A.5.1 through A.8.34)
for section in 5 6 7 8; do
    for control in {1..34}; do
        control_id="A.${section}.${control}"
        
        # Search for control references in files and directories (excluding patterns)
        if eval "find . $FIND_EXCLUDE_ARGS -type f -name '*${control_id}*' -print" 2>/dev/null | grep -q .; then
            echo "$control_id" >> "$CONTROLS_FILE"
        elif eval "find . $FIND_EXCLUDE_ARGS -type d -name '*${control_id}*' -print" 2>/dev/null | grep -q .; then
            echo "$control_id" >> "$CONTROLS_FILE"
            # Store folder name
            folder=$(eval "find . $FIND_EXCLUDE_ARGS -type d -name '*${control_id}*' -print" 2>/dev/null | head -1)
            echo "$control_id|$folder" >> "$CONTROL_FOLDERS_FILE"
        fi
    done
done

# Remove duplicates and count
sort -u "$CONTROLS_FILE" > "$TEMP_DIR/controls_unique.txt"
TOTAL_CONTROLS_FOUND=$(wc -l < "$TEMP_DIR/controls_unique.txt" | tr -d ' ')

echo "✅ Controls Identified:        $TOTAL_CONTROLS_FOUND"
echo

# List controls by section
for section in 5 6 7 8; do
    SECTION_CONTROLS=$(grep "^A\.${section}\." "$TEMP_DIR/controls_unique.txt" 2>/dev/null || true)
    SECTION_COUNT=$(echo "$SECTION_CONTROLS" | grep -c "A\.${section}\." 2>/dev/null || echo "0")
    
    if [ "$SECTION_COUNT" -gt 0 ]; then
        echo -e "${GREEN}Section ${section}: ${SECTION_COUNT} controls${NC}"
        echo "  $SECTION_CONTROLS" | tr '\n' ' '
        echo
        echo
    fi
done

# Check for control stacking
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}CONTROL STACKING ANALYSIS${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}\n"

STACKED_FOLDERS=0
TOTAL_CONTROL_FOLDERS=0

# Find folders that contain multiple control references
echo "Analyzing control folder organization..."

if [ -s "$CONTROL_FOLDERS_FILE" ]; then
    TOTAL_CONTROL_FOLDERS=$(wc -l < "$CONTROL_FOLDERS_FILE" | tr -d ' ')
    
    while IFS='|' read -r control_id folder_path; do
        if [ -n "$folder_path" ] && [ -d "$folder_path" ]; then
            folder_name=$(basename "$folder_path")
            
            # Count how many control IDs are in the folder name
            control_count=$(echo "$folder_name" | grep -o "A\.[5-8]\.[0-9][0-9]*" | wc -l | tr -d ' ')
            
            if [ "$control_count" -gt 1 ]; then
                STACKED_FOLDERS=$((STACKED_FOLDERS + 1))
            fi
        fi
    done < "$CONTROL_FOLDERS_FILE"
    
    # Remove duplicates for accurate count
    STACKED_FOLDERS=$(sort -u -t'|' -k2 "$CONTROL_FOLDERS_FILE" | \
        while IFS='|' read -r _ folder_path; do
            basename "$folder_path"
        done | \
        while read folder_name; do
            echo "$folder_name" | grep -o "A\.[5-8]\.[0-9][0-9]*" | wc -l
        done | \
        awk '$1 > 1' | wc -l | tr -d ' ')
fi

echo "📂 Control Folders:            $TOTAL_CONTROL_FOLDERS"
echo "🔗 Stacked Folders:            $STACKED_FOLDERS"
echo "   (Folders containing multiple controls)"
echo

# Calculate efficiency
if [ "$TOTAL_CONTROL_FOLDERS" -gt 0 ] && [ "$TOTAL_CONTROLS_FOUND" -gt 0 ]; then
    REDUCTION=$((TOTAL_CONTROLS_FOUND - TOTAL_CONTROL_FOLDERS))
    STACKING_EFFICIENCY=$(awk "BEGIN {printf \"%.1f\", ($REDUCTION / $TOTAL_CONTROLS_FOUND) * 100}")
    echo "📊 Stacking Efficiency:        ${STACKING_EFFICIENCY}%"
    echo "   (Reduction in folder count through stacking)"
    echo
fi

# Project timeline estimation
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}PROJECT METRICS${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}\n"

# Get date range from git if available
if [ -d ".git" ]; then
    echo "📅 Git Repository Timeline:"
    FIRST_COMMIT=$(git log --reverse --format="%ai" 2>/dev/null | head -1 | cut -d' ' -f1)
    LAST_COMMIT=$(git log --format="%ai" 2>/dev/null | head -1 | cut -d' ' -f1)
    TOTAL_COMMITS=$(git rev-list --count HEAD 2>/dev/null || echo "N/A")
    
    if [ -n "$FIRST_COMMIT" ]; then
        echo "   First Commit:               $FIRST_COMMIT"
        echo "   Last Commit:                $LAST_COMMIT"
        echo "   Total Commits:              $TOTAL_COMMITS"
        echo
    fi
fi

# Estimate effort based on typical metrics
if [ "$TOTAL_CONTROLS_FOUND" -gt 0 ]; then
    echo "⏱️  Estimated Effort Metrics:"
    
    # Average 3 hours per control for SSE approach
    EST_HOURS_SSE=$((TOTAL_CONTROLS_FOUND * 3))
    
    # Traditional consulting: 50 hours per control
    EST_HOURS_TRAD=$((TOTAL_CONTROLS_FOUND * 50))
    
    echo "   SSE Approach (~3h/control):  ${EST_HOURS_SSE} hours"
    echo "   Traditional (~50h/control):  ${EST_HOURS_TRAD} hours"
    
    if [ "$EST_HOURS_TRAD" -gt 0 ]; then
        EFFICIENCY_FACTOR=$(awk "BEGIN {printf \"%.1f\", $EST_HOURS_TRAD / $EST_HOURS_SSE}")
        echo "   Efficiency Multiplier:       ${EFFICIENCY_FACTOR}x faster"
    fi
    echo
fi

# File size analysis
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}STORAGE METRICS${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}\n"

TOTAL_SIZE=$(du -sh . 2>/dev/null | cut -f1)
CODE_SIZE=$(eval "find . $FIND_EXCLUDE_ARGS -name '*.py' -type f -print" 2>/dev/null | xargs du -ch 2>/dev/null | tail -1 | cut -f1 || echo "0")
DOCS_SIZE=$(eval "find . $FIND_EXCLUDE_ARGS -name '*.md' -type f -print" 2>/dev/null | xargs du -ch 2>/dev/null | tail -1 | cut -f1 || echo "0")

echo "💾 Total Project Size:         $TOTAL_SIZE"
echo "🐍 Python Scripts Size:        $CODE_SIZE"
echo "📝 Markdown Docs Size:         $DOCS_SIZE"
echo

# Generate summary report
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}SUMMARY STATISTICS${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}\n"

echo "╔══════════════════════════════════════════════════════════╗"
echo "║                    PROJECT SUMMARY                       ║"
echo "╠══════════════════════════════════════════════════════════╣"
printf "║ Controls Implemented:       %-30s║\n" "$TOTAL_CONTROLS_FOUND / 93"
printf "║ Total Files:                %-30s║\n" "$TOTAL_FILES"
printf "║ Python Scripts:             %-30s║\n" "$TOTAL_PY_FILES"
printf "║ Documentation Files:        %-30s║\n" "$TOTAL_MD_FILES"
printf "║ Lines of Code:              %-30s║\n" "$TOTAL_LINES_CODE"
printf "║ Lines of Documentation:     %-30s║\n" "$TOTAL_LINES_DOCS"
printf "║ Excel Workbooks:            %-30s║\n" "$TOTAL_WORKBOOKS"
printf "║ Control Folders:            %-30s║\n" "$TOTAL_CONTROL_FOLDERS"
echo "╚══════════════════════════════════════════════════════════╝"
echo

# Calculate completion percentage
COMPLETION_PCT=$(awk "BEGIN {printf \"%.2f\", ($TOTAL_CONTROLS_FOUND / 93) * 100}")

# Export to JSON for programmatic access
JSON_OUTPUT="${PROJECT_DIR}/project-stats.json"

cat > "$JSON_OUTPUT" << EOF
{
  "project_name": "ISO 27001:2022 ISMS Implementation",
  "analysis_date": "$(date +%Y-%m-%d)",
  "excludes_templates": true,
  "excluded_folders": [
$(printf '    "%s",\n' "${EXCLUDE_PATTERNS[@]}" | sed '$ s/,$//')
  ],
  "statistics": {
    "controls": {
      "total_identified": $TOTAL_CONTROLS_FOUND,
      "total_possible": 93,
      "completion_percentage": $COMPLETION_PCT
    },
    "files": {
      "total": $TOTAL_FILES,
      "directories": $TOTAL_DIRS,
      "markdown": $TOTAL_MD_FILES,
      "python": $TOTAL_PY_FILES,
      "excel": $TOTAL_WORKBOOKS,
      "policy": $TOTAL_POL_FILES,
      "implementation": $TOTAL_IMP_FILES,
      "scripts": $TOTAL_SCR_FILES
    },
    "lines_of_code": {
      "python": $TOTAL_LINES_CODE,
      "markdown": $TOTAL_LINES_DOCS,
      "total": $TOTAL_LINES
    },
    "organization": {
      "control_folders": $TOTAL_CONTROL_FOLDERS,
      "stacked_folders": $STACKED_FOLDERS
    },
    "project_size": {
      "total": "$TOTAL_SIZE",
      "code": "$CODE_SIZE",
      "docs": "$DOCS_SIZE"
    }
  }
}
EOF

echo -e "${GREEN}✅ Statistics exported to: ${JSON_OUTPUT}${NC}"
echo

# Generate markdown summary for easy inclusion in documents
MD_OUTPUT="${PROJECT_DIR}/project-stats-summary.md"

cat > "$MD_OUTPUT" << 'EOF'
# ISMS Project Statistics Summary

## Overview

EOF

cat >> "$MD_OUTPUT" << EOF
- **Total Controls Implemented**: ${TOTAL_CONTROLS_FOUND} of 93 ISO 27001:2022 Annex A controls
- **Completion Rate**: ${COMPLETION_PCT}%
- **Total Documentation Files**: ${TOTAL_FILES}
- **Python Automation Scripts**: ${TOTAL_PY_FILES}
- **Lines of Code**: ${TOTAL_LINES_CODE} lines
- **Excel Assessment Workbooks**: ${TOTAL_WORKBOOKS}

**Note**: Statistics exclude template/base folders to avoid duplicate counting.

## File Breakdown

| Category | Count |
|----------|-------|
| Total Files | ${TOTAL_FILES} |
| Directories | ${TOTAL_DIRS} |
| Markdown Documents | ${TOTAL_MD_FILES} |
| Python Scripts | ${TOTAL_PY_FILES} |
| Excel Workbooks | ${TOTAL_WORKBOOKS} |
| Policy (POL) Files | ${TOTAL_POL_FILES} |
| Implementation (IMP) Files | ${TOTAL_IMP_FILES} |
| Script (SCR) Files | ${TOTAL_SCR_FILES} |

## Code Statistics

| Metric | Value |
|--------|-------|
| Python Lines of Code | ${TOTAL_LINES_CODE} |
| Markdown Lines | ${TOTAL_LINES_DOCS} |
| Total Lines | ${TOTAL_LINES} |

## Control Implementation

**Total Controls Identified**: ${TOTAL_CONTROLS_FOUND}

EOF

# Add control breakdown by section
for section in 5 6 7 8; do
    SECTION_CONTROLS=$(grep "^A\.${section}\." "$TEMP_DIR/controls_unique.txt" 2>/dev/null || true)
    SECTION_COUNT=$(echo "$SECTION_CONTROLS" | grep -c "A\.${section}\." 2>/dev/null || echo "0")
    
    if [ "$SECTION_COUNT" -gt 0 ]; then
        echo "- **Section ${section}**: ${SECTION_COUNT} controls" >> "$MD_OUTPUT"
    fi
done

cat >> "$MD_OUTPUT" << EOF

## Project Organization

- **Control Folders**: ${TOTAL_CONTROL_FOLDERS}
- **Stacked Folders**: ${STACKED_FOLDERS}
- **Stacking Efficiency**: Reduced folder count by $((TOTAL_CONTROLS_FOUND - TOTAL_CONTROL_FOLDERS)) through intelligent control grouping

## Project Size

- **Total Size**: ${TOTAL_SIZE}
- **Code Size**: ${CODE_SIZE}
- **Documentation Size**: ${DOCS_SIZE}

---

*Statistics generated on $(date)*  
*Analysis performed on: ${PROJECT_DIR}*  
*Template/base folders excluded from analysis*
EOF

echo -e "${GREEN}✅ Markdown summary exported to: ${MD_OUTPUT}${NC}"
echo

echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}Analysis Complete!${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"
