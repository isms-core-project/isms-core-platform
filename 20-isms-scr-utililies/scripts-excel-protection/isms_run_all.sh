#!/bin/bash
################################################################################
# ISMS UTILITIES - MASTER ORCHESTRATION SCRIPT
################################################################################
#
# Runs all ISMS protection utilities in logical order:
#   1. Scan current protection status (before)
#   2. Protect all production scripts
#   3. Scan protection status again (after)
#   4. Generate comparison report
#
# USAGE:
#   ./isms_run_all.sh                    # Full workflow
#   ./isms_run_all.sh --scan-only        # Just scan, don't protect
#   ./isms_run_all.sh --protect-only     # Just protect, skip scans
#   ./isms_run_all.sh --dry-run          # Preview what would happen
#
# REQUIREMENTS:
#   - All isms_*.py and isms_*.sh scripts in same directory
#   - Python 3 installed
#   - Run from ISMS base directory
#
################################################################################

set -e  # Exit on error

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
DRY_RUN=false
SCAN_ONLY=false
PROTECT_ONLY=false
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --scan-only)
            SCAN_ONLY=true
            shift
            ;;
        --protect-only)
            PROTECT_ONLY=true
            shift
            ;;
        -h|--help)
            cat << EOF
ISMS Utilities - Master Orchestration Script

Runs complete protection workflow:
  1. Scan current status (before)
  2. Protect production scripts
  3. Scan status again (after)
  4. Generate comparison report

USAGE:
    ./isms_run_all.sh                    # Full workflow
    ./isms_run_all.sh --scan-only        # Scan only
    ./isms_run_all.sh --protect-only     # Protect only
    ./isms_run_all.sh --dry-run          # Preview mode

WORKFLOW STEPS:
    Step 1: Pre-protection scan
    Step 2: Protect production scripts (10_generator_utf folders)
    Step 3: Post-protection scan
    Step 4: Generate comparison report

REQUIREMENTS:
    - isms_scan_protection.py
    - isms_protect_production.py (or isms_protect_all.sh)
    - isms_add_protection.py
    - Python 3

OUTPUT:
    - isms_scan_before_TIMESTAMP.txt
    - isms_scan_after_TIMESTAMP.txt
    - isms_comparison_TIMESTAMP.txt

EOF
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

# Header
clear
echo "================================================================================"
echo -e "${CYAN}ISMS UTILITIES - MASTER ORCHESTRATION${NC}"
echo "================================================================================"
echo ""
echo "Timestamp: $TIMESTAMP"
echo "Directory: $(pwd)"
echo ""

if [[ "$DRY_RUN" == true ]]; then
    echo -e "${YELLOW}MODE: DRY RUN (preview only)${NC}"
elif [[ "$SCAN_ONLY" == true ]]; then
    echo -e "${BLUE}MODE: SCAN ONLY${NC}"
elif [[ "$PROTECT_ONLY" == true ]]; then
    echo -e "${BLUE}MODE: PROTECT ONLY${NC}"
else
    echo -e "${GREEN}MODE: FULL WORKFLOW${NC}"
fi
echo ""

# Check for required scripts
REQUIRED_SCRIPTS=("isms_scan_protection.py" "isms_add_protection.py")
MISSING=false

echo "Checking required scripts..."
for script in "${REQUIRED_SCRIPTS[@]}"; do
    if [[ -f "$script" ]]; then
        echo -e "  ${GREEN}✓${NC} $script"
    else
        echo -e "  ${RED}✗${NC} $script ${RED}(missing)${NC}"
        MISSING=true
    fi
done

# Check for protection script
if [[ -f "isms_protect_production.py" ]]; then
    echo -e "  ${GREEN}✓${NC} isms_protect_production.py"
    PROTECT_SCRIPT="python3 isms_protect_production.py"
elif [[ -f "isms_protect_all.sh" ]]; then
    echo -e "  ${GREEN}✓${NC} isms_protect_all.sh"
    PROTECT_SCRIPT="./isms_protect_all.sh"
else
    echo -e "  ${RED}✗${NC} isms_protect_production.py or isms_protect_all.sh ${RED}(missing)${NC}"
    MISSING=true
fi

echo ""

if [[ "$MISSING" == true ]]; then
    echo -e "${RED}✗ Missing required scripts${NC}"
    echo ""
    echo "Please ensure all ISMS utility scripts are in the current directory:"
    echo "  - isms_scan_protection.py"
    echo "  - isms_add_protection.py"
    echo "  - isms_protect_production.py (or isms_protect_all.sh)"
    echo ""
    exit 1
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✗ Python 3 not found${NC}"
    exit 1
fi

echo -e "${GREEN}✓ All requirements met${NC}"
echo ""

# Confirmation (unless dry-run or protect-only)
if [[ "$DRY_RUN" == false ]] && [[ "$SCAN_ONLY" == false ]]; then
    echo -e "${YELLOW}This will protect production scripts in:${NC}"
    echo "  $(pwd)"
    echo ""
    read -p "Continue? [y/N] " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Cancelled"
        exit 0
    fi
    echo ""
fi

################################################################################
# STEP 1: PRE-PROTECTION SCAN
################################################################################

if [[ "$PROTECT_ONLY" == false ]]; then
    echo "================================================================================"
    echo -e "${CYAN}STEP 1: PRE-PROTECTION SCAN${NC}"
    echo "================================================================================"
    echo ""
    
    SCAN_BEFORE="isms_scan_before_${TIMESTAMP}.txt"
    
    echo "Scanning current protection status..."
    echo "Output: $SCAN_BEFORE"
    echo ""
    
    if python3 isms_scan_protection.py --dir . --report "$SCAN_BEFORE" 2>&1 | tee /tmp/scan_before.log; then
        echo ""
        echo -e "${GREEN}✓ Pre-scan complete${NC}"
        
        # Extract key stats
        if [[ -f "$SCAN_BEFORE" ]]; then
            BEFORE_PROTECTED=$(grep "Functions Protected:" "$SCAN_BEFORE" | grep -oP '\d+' | head -1 || echo "?")
            BEFORE_RATE=$(grep "Overall Protection Rate:" "$SCAN_BEFORE" | grep -oP '[\d.]+%' || echo "?")
            echo ""
            echo "Current Status:"
            echo "  Protected Functions: $BEFORE_PROTECTED"
            echo "  Protection Rate: $BEFORE_RATE"
        fi
    else
        echo ""
        echo -e "${YELLOW}⚠ Pre-scan had issues (continuing anyway)${NC}"
    fi
    
    echo ""
    sleep 2
fi

################################################################################
# STEP 2: PROTECT PRODUCTION SCRIPTS
################################################################################

if [[ "$SCAN_ONLY" == false ]]; then
    echo "================================================================================"
    echo -e "${CYAN}STEP 2: PROTECT PRODUCTION SCRIPTS${NC}"
    echo "================================================================================"
    echo ""
    
    echo "Target: */10_generator_utf/generate_*.py"
    echo ""
    
    if [[ "$DRY_RUN" == true ]]; then
        echo -e "${YELLOW}DRY RUN MODE - Preview only${NC}"
        echo ""
        if [[ "$PROTECT_SCRIPT" == *".py" ]]; then
            python3 isms_protect_production.py --dry-run
        else
            ./isms_protect_all.sh --dry-run
        fi
    else
        if [[ "$PROTECT_SCRIPT" == *".py" ]]; then
            python3 isms_protect_production.py
        else
            ./isms_protect_all.sh
        fi
    fi
    
    PROTECT_STATUS=$?
    
    if [[ $PROTECT_STATUS -eq 0 ]]; then
        echo ""
        echo -e "${GREEN}✓ Protection complete${NC}"
    else
        echo ""
        echo -e "${RED}✗ Protection had errors (check output above)${NC}"
    fi
    
    echo ""
    sleep 2
fi

################################################################################
# STEP 3: POST-PROTECTION SCAN
################################################################################

if [[ "$PROTECT_ONLY" == false ]] && [[ "$DRY_RUN" == false ]]; then
    echo "================================================================================"
    echo -e "${CYAN}STEP 3: POST-PROTECTION SCAN${NC}"
    echo "================================================================================"
    echo ""
    
    SCAN_AFTER="isms_scan_after_${TIMESTAMP}.txt"
    
    echo "Scanning protection status after changes..."
    echo "Output: $SCAN_AFTER"
    echo ""
    
    if python3 isms_scan_protection.py --dir . --report "$SCAN_AFTER" 2>&1 | tee /tmp/scan_after.log; then
        echo ""
        echo -e "${GREEN}✓ Post-scan complete${NC}"
        
        # Extract key stats
        if [[ -f "$SCAN_AFTER" ]]; then
            AFTER_PROTECTED=$(grep "Functions Protected:" "$SCAN_AFTER" | grep -oP '\d+' | head -1 || echo "?")
            AFTER_RATE=$(grep "Overall Protection Rate:" "$SCAN_AFTER" | grep -oP '[\d.]+%' || echo "?")
            echo ""
            echo "New Status:"
            echo "  Protected Functions: $AFTER_PROTECTED"
            echo "  Protection Rate: $AFTER_RATE"
        fi
    else
        echo ""
        echo -e "${YELLOW}⚠ Post-scan had issues${NC}"
    fi
    
    echo ""
    sleep 2
fi

################################################################################
# STEP 4: GENERATE COMPARISON REPORT
################################################################################

if [[ "$PROTECT_ONLY" == false ]] && [[ "$SCAN_ONLY" == false ]] && [[ "$DRY_RUN" == false ]]; then
    echo "================================================================================"
    echo -e "${CYAN}STEP 4: COMPARISON REPORT${NC}"
    echo "================================================================================"
    echo ""
    
    COMPARISON_REPORT="isms_comparison_${TIMESTAMP}.txt"
    
    if [[ -f "$SCAN_BEFORE" ]] && [[ -f "$SCAN_AFTER" ]]; then
        echo "Generating comparison report..."
        echo "Output: $COMPARISON_REPORT"
        echo ""
        
        cat > "$COMPARISON_REPORT" << EOFCOMP
================================================================================
ISMS PROTECTION STATUS - BEFORE vs AFTER COMPARISON
================================================================================

Generated: $(date '+%Y-%m-%d %H:%M:%S')
Workflow Run: $TIMESTAMP

================================================================================
BEFORE PROTECTION
================================================================================

EOFCOMP
        
        grep -A 20 "EXECUTIVE SUMMARY" "$SCAN_BEFORE" >> "$COMPARISON_REPORT" 2>/dev/null || echo "  (Stats not available)" >> "$COMPARISON_REPORT"
        
        cat >> "$COMPARISON_REPORT" << EOFCOMP

================================================================================
AFTER PROTECTION
================================================================================

EOFCOMP
        
        grep -A 20 "EXECUTIVE SUMMARY" "$SCAN_AFTER" >> "$COMPARISON_REPORT" 2>/dev/null || echo "  (Stats not available)" >> "$COMPARISON_REPORT"
        
        cat >> "$COMPARISON_REPORT" << EOFCOMP

================================================================================
IMPROVEMENT
================================================================================

Protected Functions:
  Before: $BEFORE_PROTECTED
  After:  $AFTER_PROTECTED
  Change: +$((AFTER_PROTECTED - BEFORE_PROTECTED)) functions

Protection Rate:
  Before: $BEFORE_RATE
  After:  $AFTER_RATE

================================================================================
REPORT FILES
================================================================================

Pre-scan:      $SCAN_BEFORE
Post-scan:     $SCAN_AFTER
Comparison:    $COMPARISON_REPORT

================================================================================
EOFCOMP
        
        echo -e "${GREEN}✓ Comparison report generated${NC}"
        echo ""
        echo "View report: cat $COMPARISON_REPORT"
    else
        echo -e "${YELLOW}⚠ Cannot generate comparison (scan files missing)${NC}"
    fi
    
    echo ""
fi

################################################################################
# FINAL SUMMARY
################################################################################

echo "================================================================================"
echo -e "${CYAN}WORKFLOW COMPLETE${NC}"
echo "================================================================================"
echo ""

if [[ "$DRY_RUN" == true ]]; then
    echo -e "${YELLOW}DRY RUN MODE - No changes were made${NC}"
    echo ""
    echo "To apply changes, run without --dry-run:"
    echo "  ./isms_run_all.sh"
elif [[ "$SCAN_ONLY" == true ]]; then
    echo -e "${GREEN}✓ Scan complete${NC}"
    echo ""
    echo "Report generated: $SCAN_BEFORE"
elif [[ "$PROTECT_ONLY" == true ]]; then
    echo -e "${GREEN}✓ Protection applied${NC}"
    echo ""
    echo "Run full workflow to see before/after comparison:"
    echo "  ./isms_run_all.sh"
else
    echo -e "${GREEN}✓ Full workflow complete${NC}"
    echo ""
    echo "Generated Files:"
    [[ -f "$SCAN_BEFORE" ]] && echo "  📄 $SCAN_BEFORE"
    [[ -f "$SCAN_AFTER" ]] && echo "  📄 $SCAN_AFTER"
    [[ -f "$COMPARISON_REPORT" ]] && echo "  📊 $COMPARISON_REPORT"
    echo ""
    
    if [[ -f "$COMPARISON_REPORT" ]]; then
        echo "Quick View:"
        echo "----------------------------------------"
        grep -A 10 "IMPROVEMENT" "$COMPARISON_REPORT" 2>/dev/null || echo "(Comparison data not available)"
        echo "----------------------------------------"
        echo ""
        echo "Full report: cat $COMPARISON_REPORT"
    fi
fi

echo ""
echo "================================================================================"
echo -e "${GREEN}✅ Done${NC}"
echo "================================================================================"
echo ""

exit 0
