#!/bin/bash
#
# ISMS Project Analyzer Shell Wrapper
# Wraps the Python analyzer with proper error handling
#

# Get the directory where this script lives
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Python script location (same directory as this shell script)
PYTHON_SCRIPT="${SCRIPT_DIR}/analyze_isms_stack_file_detection.py"

# Check if Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "❌ Error: Python analyzer not found at: $PYTHON_SCRIPT"
    echo ""
    echo "Expected file: analyze_isms_stack_file_detection.py"
    echo "In directory: $SCRIPT_DIR"
    exit 1
fi

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 is not installed or not in PATH"
    exit 1
fi

# Get the target directory (default to current directory if not specified)
TARGET_DIR="${1:-.}"

# Check if target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "❌ Error: Directory does not exist: $TARGET_DIR"
    echo ""
    echo "Usage: $0 [directory]"
    echo "Example: $0 ."
    echo "Example: $0 /path/to/isms/project"
    exit 1
fi

# Run the Python analyzer
python3 "$PYTHON_SCRIPT" "$TARGET_DIR"

# Capture exit code
EXIT_CODE=$?

# Exit with the same code as the Python script
exit $EXIT_CODE