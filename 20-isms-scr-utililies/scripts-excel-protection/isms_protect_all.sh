#!/bin/bash
################################################################################
# ISMS Production Scripts Protection - Simple Bash Wrapper
################################################################################
#
# Protects ONLY production scripts (10_generator_utf folders)
# Skips all backups, originals, and old versions
#
# USAGE:
#   ./protect_10_folders.sh              # Protect all production
#   ./protect_10_folders.sh --dry-run    # Preview only
#   ./protect_10_folders.sh --help       # Show help
#
################################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
DRY_RUN=false
VERBOSE=false

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -h|--help)
            cat << EOF
ISMS Production Scripts Protection

Protects ONLY scripts in "10_generator_utf" folders.
Skips: 99_originals/, 97_backup/, 98_claude_ai/, etc.

USAGE:
    ./protect_10_folders.sh              # Protect all production
    ./protect_10_folders.sh --dry-run    # Preview (no changes)
    ./protect_10_folders.sh -v           # Verbose output

REQUIREMENTS:
    - isms_add_protection.py must be in current directory
    - Python 3 must be installed
    - Must run from ISMS base directory

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
echo "================================================================================"
echo "ISMS Production Scripts Protection"
echo "================================================================================"
echo ""

# Check for isms_add_protection.py
if [[ ! -f "isms_add_protection.py" ]]; then
    echo -e "${RED}❌ Error: isms_add_protection.py not found${NC}"
    echo ""
    echo "Please copy isms_add_protection.py to the current directory:"
    echo "  cp /path/to/isms_add_protection.py ."
    echo ""
    exit 1
fi

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Error: python3 not found${NC}"
    echo "Please install Python 3"
    exit 1
fi

# Find all production scripts
echo "Scanning for production scripts..."
echo "Target: */10_generator_utf/generate_*.py"
echo ""

SCRIPTS=($(find . -path "*/10_generator_utf/generate_*.py" -type f 2>/dev/null | sort))
TOTAL=${#SCRIPTS[@]}

if [[ $TOTAL -eq 0 ]]; then
    echo -e "${YELLOW}⚠️  No production scripts found${NC}"
    echo ""
    echo "Make sure you're in the ISMS base directory:"
    echo "  cd /path/to/ISMS/10-ISMS-SCR-Base"
    echo ""
    exit 1
fi

echo -e "${GREEN}Found $TOTAL production scripts${NC}"
echo ""

# Dry run mode
if [[ "$DRY_RUN" == true ]]; then
    echo -e "${YELLOW}DRY RUN MODE - No changes will be made${NC}"
    echo "================================================================================"
    echo ""
    
    for script in "${SCRIPTS[@]}"; do
        echo "Would protect: $script"
    done
    
    echo ""
    echo "================================================================================"
    echo "To apply changes, run without --dry-run:"
    echo "  ./protect_10_folders.sh"
    echo "================================================================================"
    echo ""
    exit 0
fi

# Confirm before proceeding
echo -e "${YELLOW}This will modify $TOTAL scripts${NC}"
echo "Backups (.bak) will be created for each modified file"
echo ""
read -p "Continue? [y/N] " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled"
    exit 0
fi

# Protection statistics
PROTECTED=0
SKIPPED=0
FAILED=0

echo ""
echo "================================================================================"
echo "PROTECTING PRODUCTION SCRIPTS"
echo "================================================================================"
echo ""

# Process each script
for i in "${!SCRIPTS[@]}"; do
    SCRIPT="${SCRIPTS[$i]}"
    INDEX=$((i + 1))
    
    # Progress indicator
    printf "[%3d/%3d] " "$INDEX" "$TOTAL"
    
    # Run protection
    if OUTPUT=$(python3 isms_add_protection.py "$SCRIPT" 2>&1); then
        if echo "$OUTPUT" | grep -q "All functions already have sheet protection"; then
            echo -e "⊘  SKIP: $SCRIPT ${BLUE}(already protected)${NC}"
            ((SKIPPED++))
        elif echo "$OUTPUT" | grep -q "functions modified"; then
            COUNT=$(echo "$OUTPUT" | grep -oP '\d+(?= functions modified)' || echo "?")
            echo -e "✅ PROTECTED: $SCRIPT ${GREEN}($COUNT functions)${NC}"
            ((PROTECTED++))
        else
            echo -e "✅ PROTECTED: $SCRIPT"
            ((PROTECTED++))
        fi
        
        # Verbose output
        if [[ "$VERBOSE" == true ]]; then
            echo "$OUTPUT" | sed 's/^/    /'
        fi
    else
        echo -e "❌ FAILED: $SCRIPT"
        ((FAILED++))
        
        # Always show error details
        echo "$OUTPUT" | head -3 | sed 's/^/    /'
    fi
done

# Summary
echo ""
echo "================================================================================"
echo "SUMMARY"
echo "================================================================================"
echo ""
echo "Total Scripts Found:     $TOTAL"
echo -e "  ${GREEN}✅ Protected:          $PROTECTED${NC}"
echo -e "  ${BLUE}⊘  Skipped:            $SKIPPED${NC} (already protected)"
echo -e "  ${RED}❌ Failed:             $FAILED${NC}"
echo ""

if [[ $PROTECTED -gt 0 ]]; then
    echo -e "${GREEN}✅ Successfully protected $PROTECTED production scripts!${NC}"
    echo ""
    echo "Next Steps:"
    echo "  1. Verify protection:"
    echo "     python3 isms_scan_protection.py --report verification.txt"
    echo ""
    echo "  2. Test a workbook:"
    echo "     python3 ISMS-A.8.24-Cryptography/10_generator_utf/generate_a824_1_data_transmission.py"
    echo ""
elif [[ $SKIPPED -eq $TOTAL ]]; then
    echo -e "${GREEN}✅ All production scripts already protected!${NC}"
else
    echo -e "${YELLOW}⚠️  Some scripts could not be protected${NC}"
    echo "Check error messages above for details"
fi

echo ""
echo "================================================================================"
echo "✅ Complete"
echo "================================================================================"
echo ""
