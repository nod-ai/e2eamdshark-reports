# create_summary.py

## Purpose

This script generates an Excel summary report from markdown test report files. It parses test results, aggregates pass/fail statistics, and creates a detailed breakdown of failure reasons.

## Command Line Arguments

| Argument | Short | Type | Default | Description |
|----------|-------|------|---------|-------------|
| `--report-dir` | `-r` | Path | `./reports` | Directory containing markdown report files |
| `--report-file-list` | `-l` | Path | `None` | Optional file containing a list of specific report files to process |
| `--test-run-dir` | `-t` | Path | `./test-run` | Directory containing test run logs (for failure analysis) |
| `--output-file` | `-o` | str | `summary.xlsx` | Output Excel file name |

## Usage Examples

```bash
# Basic usage with defaults
python create_summary.py

# Specify custom report directory and output file
python create_summary.py -r ./my-reports -o my_summary.xlsx

# Use a file list to process specific reports
python create_summary.py -r ./reports -l report_list.txt -t ./test-run -o summary.xlsx
```
Note : If --report-file-list is not provided, then the script parses all the md files in --report-dir to prepare the summary report.  

## Input Format

The script expects markdown files with a table section like:

```markdown
## Test Run Detail
| Test | Exit Status | Mean Benchmark Time (ms) | Notes |
|------|-------------|--------------------------|-------|
| test1 | PASS | 100 | ... |
| test2 | compile | 200 | ... |
```

## Output Excel Structure

1. **Summary** sheet - Overview with test file names, total counts, and pass counts
2. **Per-file sheets** - Detailed test results with name, status, fail stage, and fail reason
3. **Reason_Histogram** sheet - Aggregated failure reasons by stage

## Dependencies

- `xlsxwriter`

Install with:

```bash
pip install xlsxwriter
```

