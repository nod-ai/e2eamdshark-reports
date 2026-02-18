# Latest Comparison Reports

This folder contains the most recent versions of all GPU vs CPU comparison reports.

## Contents

This folder is automatically updated by the CI workflow and contains:

1. **ci_reports_onnx_comparison_report.md** - Latest ONNX test comparison between GPU (ROCm) and CPU (LLVM-CPU)
2. **hf-model-top1k_comparison_report.md** - Latest HuggingFace Top 1K models comparison
3. **ci_reports_onnx_dup_comparison_report.md** - Latest ONNX duplicate tests comparison
4. **gpu_vs_cpu_summary.md** - Combined summary of all three comparisons with side-by-side tables
5. **gpu_vs_cpu_email.html** - Email-friendly HTML version with inline CSS (ready to send via email)

## How It Works

- The CI workflow runs daily at 16:30 UTC
- After generating comparison reports, it copies the latest version of each report type to this folder
- If a report wasn't generated on the current date, the most recent previous version is copied
- Each file includes metadata showing:
  - **Generated on**: The date when the report was originally generated
  - **Copied to latest**: The date when it was copied to this folder

## Benefits

- **Easy Access**: Always find the most recent reports in one place
- **No Date Navigation**: No need to browse through date-specific folders
- **Clear Provenance**: Metadata shows exactly when each report was generated
- **Complete Picture**: Always includes all three comparison types

## File Updates

Each report in this folder shows when it was last generated. If you need historical data or want to see the progression over time, check the date-specific folders (e.g., `2026-02-18/comparison_reports/`).
