#!/usr/bin/env python3
"""
Extract GPU vs CPU comparison sections from all comparison reports
and combine them into a single summary file.
"""

import os
import sys
import re
from pathlib import Path


def extract_gpu_cpu_section(file_path):
    """Extract the GPU vs CPU Comparison section from a report file."""
    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as f:
        content = f.read()

    # Find the GPU vs CPU Comparison section
    # It starts with "# GPU vs CPU Comparison" and ends before the next "---" or "# " section
    pattern = r'# GPU vs CPU Comparison\n\n(.*?)(?=\n---\n|\n# [^#]|\Z)'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        return match.group(0)

    return None


def parse_section_to_table_format(section_content, report_type, date):
    """Parse the GPU vs CPU section and format it with side-by-side tables."""
    lines = section_content.split('\n')

    # Extract GPU and CPU status paths
    gpu_status = ""
    cpu_status = ""
    for line in lines:
        if line.startswith("**GPU Status:**"):
            gpu_status = line.replace("**GPU Status:**", "").strip()
        elif line.startswith("**CPU Status:**"):
            cpu_status = line.replace("**CPU Status:**", "").strip()

    # Extract Total Tests table
    total_tests_section = []
    in_total_tests = False
    for i, line in enumerate(lines):
        if line.strip() == "## Total Tests":
            in_total_tests = True
            continue
        if in_total_tests:
            if line.strip().startswith("##"):
                break
            if line.strip():
                total_tests_section.append(line)

    # Extract Passing Summary table
    passing_summary = []
    in_passing = False
    for i, line in enumerate(lines):
        if line.strip() == "## Passing Summary":
            in_passing = True
            continue
        if in_passing:
            if line.strip().startswith("##"):
                break
            if line.strip():
                passing_summary.append(line)

    # Extract Fail Summary table
    fail_summary = []
    in_fail = False
    for i, line in enumerate(lines):
        if line.strip() == "## Fail Summary":
            in_fail = True
            continue
        if in_fail:
            if line.strip().startswith("##") or line.strip() == "---":
                break
            if line.strip():
                fail_summary.append(line)

    # Build the output with side-by-side tables
    output = f"## {report_type} ({date})\n\n"
    output += f"**GPU Status:** {gpu_status}\n"
    output += f"**CPU Status:** {cpu_status}\n\n"

    # Add Total Tests table
    if total_tests_section:
        output += "### Total Tests\n\n"
        output += '\n'.join(total_tests_section) + "\n\n"

    # Convert tables to side-by-side format
    # Parse passing summary table
    passing_rows = []
    for line in passing_summary:
        if line.strip().startswith('|') and not line.strip().startswith('|---'):
            # Skip header row, we'll create our own
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if parts and parts[0] != 'Stage':
                passing_rows.append(parts)

    # Parse fail summary table
    fail_rows = []
    for line in fail_summary:
        if line.strip().startswith('|') and not line.strip().startswith('|---'):
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if parts and parts[0] != 'Stage':
                fail_rows.append(parts)

    # Create side-by-side tables
    output += '<div style="display: flex; gap: 20px;">\n'
    output += '<div style="flex: 1;">\n\n'
    output += '### Passing Summary\n\n'
    output += '| Stage | GPU | CPU |\n'
    output += '|-------|-----|-----|\n'
    for row in passing_rows:
        if len(row) >= 3:
            # Row format: [Stage, GPU (# Passing), CPU (# Passing), Change]
            # We only want Stage, GPU, CPU (skip Change)
            output += f'| {row[0]} | {row[1]} | {row[2]} |\n'
    output += '\n</div>\n'
    output += '<div style="flex: 1;">\n\n'
    output += '### Fail Summary\n\n'
    output += '| Stage | GPU | CPU |\n'
    output += '|-------|-----|-----|\n'
    for row in fail_rows:
        if len(row) >= 3:
            # Row format: [Stage, GPU (# Failed), CPU (# Failed), Change]
            # We only want Stage, GPU, CPU (skip Change)
            output += f'| {row[0]} | {row[1]} | {row[2]} |\n'
    output += '\n</div>\n'
    output += '</div>\n\n'
    output += '---\n\n'

    return output


def find_latest_report(report_file, current_date_dir):
    """Find the latest version of a report, searching backwards from current date."""
    # First check current date
    current_path = os.path.join(current_date_dir, "comparison_reports", report_file)
    if os.path.exists(current_path):
        return current_path, current_date_dir.split('/')[-1]

    # Get all date directories and sort in descending order
    parent_dir = os.path.dirname(current_date_dir) if '/' in current_date_dir else '.'
    all_dates = []

    for item in os.listdir(parent_dir if parent_dir != '.' else '.'):
        # Match YYYY-MM-DD pattern
        if re.match(r'\d{4}-\d{2}-\d{2}', item):
            all_dates.append(item)

    all_dates.sort(reverse=True)
    current_date = current_date_dir.split('/')[-1]

    # Search backwards from current date
    for date in all_dates:
        if date < current_date:
            prev_path = os.path.join(parent_dir if parent_dir != '.' else '.', date, "comparison_reports", report_file)
            if os.path.exists(prev_path):
                return prev_path, date

    return None, None


def main():
    if len(sys.argv) < 2:
        print("Usage: extract_gpu_cpu_comparison.py <date_dir> [output_file]")
        sys.exit(1)

    date_dir = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else f"{date_dir}/comparison_reports/gpu_vs_cpu_summary.md"

    comparison_reports_dir = f"{date_dir}/comparison_reports"

    if not os.path.exists(comparison_reports_dir):
        print(f"Error: Directory '{comparison_reports_dir}' does not exist")
        sys.exit(1)

    # Define the reports to look for
    report_types = [
        ("ci_reports_onnx_comparison_report.md", "CI Reports ONNX Comparison"),
        ("hf-model-top1k_comparison_report.md", "HuggingFace Model Top1K Comparison"),
        ("ci_reports_onnx_dup_comparison_report.md", "CI Reports ONNX Dup Comparison")
    ]

    # Start building the output
    output_content = "# GPU vs CPU Comparison Summary\n\n"
    output_content += f"*Compiled on: {date_dir}*\n\n"
    output_content += "---\n\n"

    sections_found = 0

    for report_file, report_name in report_types:
        # Find the latest version of this report
        report_path, report_date = find_latest_report(report_file, date_dir)

        if not report_path:
            print(f"Warning: Report '{report_file}' not found in current or previous dates. Skipping...")
            continue

        if report_date != date_dir:
            print(f"Processing: {report_file} (from {report_date})")
        else:
            print(f"Processing: {report_file}")

        section = extract_gpu_cpu_section(report_path)

        if section:
            formatted_section = parse_section_to_table_format(section, report_name, report_date)
            output_content += formatted_section
            sections_found += 1
        else:
            print(f"  Warning: Could not extract GPU vs CPU section from {report_file}")

    if sections_found == 0:
        print("Error: No GPU vs CPU comparison sections were found")
        sys.exit(1)

    # Write output file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(output_content)

    print(f"\nGPU vs CPU comparison summary generated: {output_file}")
    print(f"Sections included: {sections_found}")


if __name__ == "__main__":
    main()
