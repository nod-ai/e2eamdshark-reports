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

    # Check if both summary files exist
    if [ -f "$GPU_SUMMARY" ] && [ -f "$CPU_SUMMARY" ]; then
        OUTPUT_FILE="$OUTPUT_DIR/${DIR_NAME}_gpu_vs_cpu_comparison.md"

        echo "  Generating comparison report for $DIR_NAME..."
        python3 Utils/compare_files.py "$GPU_SUMMARY" "$CPU_SUMMARY" "$OUTPUT_FILE"

        REPORTS_GENERATED=$((REPORTS_GENERATED + 1))
    else
        echo "  Warning: Missing summary.md files in combined-reports directories"
        if [ ! -f "$GPU_SUMMARY" ]; then
            echo "    - Missing: $GPU_SUMMARY"
        fi
        if [ ! -f "$CPU_SUMMARY" ]; then
            echo "    - Missing: $CPU_SUMMARY"
        fi
    fi

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
