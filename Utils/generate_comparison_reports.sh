#!/bin/bash
# CI script to generate comparison reports between GPU and CPU test results

set -e

# Use provided date or default to today's date
if [ -z "$1" ]; then
    DATE_DIR=$(date +%Y-%m-%d)
    echo "No date provided, using today's date: $DATE_DIR"
else
    DATE_DIR="$1"
fi

# Check if the date directory exists
if [ ! -d "$DATE_DIR" ]; then
    echo "Error: Directory '$DATE_DIR' does not exist"
    exit 1
fi

# Get all date directories sorted in descending order
ALL_DATES=$(ls -d [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9] 2>/dev/null | sort -r)

# Create output directory for comparison reports
OUTPUT_DIR="$DATE_DIR/comparison_reports"
mkdir -p "$OUTPUT_DIR"

echo "=== Generating Comparison Reports for $DATE_DIR ==="
echo ""

# List of possible report directories to check
POSSIBLE_DIRS=("ci_reports_onnx" "ci_reports_onnx_dup" "hf-model-top1k")

# Counter for reports generated
REPORTS_GENERATED=0

# Check each possible directory
for DIR_NAME in "${POSSIBLE_DIRS[@]}"; do
    CI_REPORTS_DIR="$DATE_DIR/$DIR_NAME"

    if [ ! -d "$CI_REPORTS_DIR" ]; then
        echo "Directory '$DIR_NAME' not found. Skipping..."
        continue
    fi

    echo "Found directory: $DIR_NAME"

    # Check for rocm directory (GPU)
    ROCM_DIR="$CI_REPORTS_DIR/rocm"
    LLVM_CPU_DIR="$CI_REPORTS_DIR/llvm-cpu"

    if [ ! -d "$ROCM_DIR" ]; then
        echo "  Warning: GPU directory 'rocm' not found in $DIR_NAME. Skipping..."
        continue
    fi

    if [ ! -d "$LLVM_CPU_DIR" ]; then
        echo "  Warning: CPU directory 'llvm-cpu' not found in $DIR_NAME. Skipping..."
        continue
    fi

    echo "  Found GPU directory: rocm"
    echo "  Found CPU directory: llvm-cpu"

    # Look for any directory starting with "combined-reports"
    GPU_COMBINED_DIR=$(find "$ROCM_DIR" -maxdepth 1 -type d -name "combined-reports*" | head -n 1)
    CPU_COMBINED_DIR=$(find "$LLVM_CPU_DIR" -maxdepth 1 -type d -name "combined-reports*" | head -n 1)

    if [ -z "$GPU_COMBINED_DIR" ]; then
        echo "  Warning: No combined-reports* directory found in rocm"
        continue
    fi

    if [ -z "$CPU_COMBINED_DIR" ]; then
        echo "  Warning: No combined-reports* directory found in llvm-cpu"
        continue
    fi

    GPU_SUMMARY="$GPU_COMBINED_DIR/summary.md"
    CPU_SUMMARY="$CPU_COMBINED_DIR/summary.md"

    echo "  Found GPU combined report: $(basename $GPU_COMBINED_DIR)"
    echo "  Found CPU combined report: $(basename $CPU_COMBINED_DIR)"

    # Check if both current summary files exist
    if [ ! -f "$GPU_SUMMARY" ] || [ ! -f "$CPU_SUMMARY" ]; then
        echo "  Warning: Missing current summary.md files in combined-reports directories"
        if [ ! -f "$GPU_SUMMARY" ]; then
            echo "    - Missing: $GPU_SUMMARY"
        fi
        if [ ! -f "$CPU_SUMMARY" ]; then
            echo "    - Missing: $CPU_SUMMARY"
        fi
        continue
    fi

    # Find previous GPU data
    PREV_GPU_SUMMARY="none"
    PREV_GPU_DATE=""

    echo "  Finding previous GPU data..."
    for PREV_DATE in $ALL_DATES; do
        if [[ "$PREV_DATE" < "$DATE_DIR" ]]; then
            PREV_ROCM_DIR="$PREV_DATE/$DIR_NAME/rocm"
            if [ -d "$PREV_ROCM_DIR" ]; then
                PREV_GPU_COMBINED_DIR=$(find "$PREV_ROCM_DIR" -maxdepth 1 -type d -name "combined-reports*" 2>/dev/null | head -n 1)
                if [ -n "$PREV_GPU_COMBINED_DIR" ]; then
                    PREV_SUMMARY="$PREV_GPU_COMBINED_DIR/summary.md"
                    if [ -f "$PREV_SUMMARY" ]; then
                        PREV_GPU_SUMMARY="$PREV_SUMMARY"
                        PREV_GPU_DATE="$PREV_DATE"
                        echo "    Found previous GPU data from: $PREV_GPU_DATE"
                        break
                    fi
                fi
            fi
        fi
    done

    if [ "$PREV_GPU_SUMMARY" == "none" ]; then
        echo "    Warning: No previous GPU data found for regression comparison"
    fi

    # Find previous CPU data
    PREV_CPU_SUMMARY="none"
    PREV_CPU_DATE=""

    echo "  Finding previous CPU data..."
    for PREV_DATE in $ALL_DATES; do
        if [[ "$PREV_DATE" < "$DATE_DIR" ]]; then
            PREV_LLVM_CPU_DIR="$PREV_DATE/$DIR_NAME/llvm-cpu"
            if [ -d "$PREV_LLVM_CPU_DIR" ]; then
                PREV_CPU_COMBINED_DIR=$(find "$PREV_LLVM_CPU_DIR" -maxdepth 1 -type d -name "combined-reports*" 2>/dev/null | head -n 1)
                if [ -n "$PREV_CPU_COMBINED_DIR" ]; then
                    PREV_SUMMARY="$PREV_CPU_COMBINED_DIR/summary.md"
                    if [ -f "$PREV_SUMMARY" ]; then
                        PREV_CPU_SUMMARY="$PREV_SUMMARY"
                        PREV_CPU_DATE="$PREV_DATE"
                        echo "    Found previous CPU data from: $PREV_CPU_DATE"
                        break
                    fi
                fi
            fi
        fi
    done

    if [ "$PREV_CPU_SUMMARY" == "none" ]; then
        echo "    Warning: No previous CPU data found for regression comparison"
    fi

    # Generate unified report
    OUTPUT_FILE="$OUTPUT_DIR/${DIR_NAME}_comparison_report.md"

    echo "  Generating unified comparison report for $DIR_NAME..."
    python3 Utils/generate_unified_report.py \
        "$GPU_SUMMARY" \
        "$CPU_SUMMARY" \
        "$PREV_GPU_SUMMARY" \
        "$PREV_CPU_SUMMARY" \
        "$OUTPUT_FILE"

    REPORTS_GENERATED=$((REPORTS_GENERATED + 1))

    echo ""
done

echo "=== Summary ==="
echo "Reports generated: $REPORTS_GENERATED"
echo "Output directory: $OUTPUT_DIR"

if [ $REPORTS_GENERATED -eq 0 ]; then
    echo ""
    echo "Warning: No comparison reports were generated"
    exit 1
fi
