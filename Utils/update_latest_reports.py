#!/usr/bin/env python3
"""
Update the latest_comparison_reports folder with the most recent versions
of all comparison reports, including generation date metadata.
"""

import os
import sys
import re
import shutil
from datetime import datetime


def find_all_dates():
    """Find all date directories in descending order."""
    all_dates = []
    for item in os.listdir('.'):
        if re.match(r'\d{4}-\d{2}-\d{2}$', item) and os.path.isdir(item):
            all_dates.append(item)
    all_dates.sort(reverse=True)
    return all_dates


def find_latest_report(report_filename, all_dates):
    """Find the most recent version of a specific report."""
    for date in all_dates:
        report_path = os.path.join(date, "comparison_reports", report_filename)
        if os.path.exists(report_path):
            return report_path, date
    return None, None


def add_generation_metadata(content, original_date, copied_date):
    """Add metadata to the report indicating when it was generated and copied."""
    # Find the first line with "Generated on:" and update it
    lines = content.split('\n')
    metadata_added = False

    for i, line in enumerate(lines):
        if '*Generated on:' in line:
            # Replace the existing generation date line
            lines[i] = f"*Generated on: {original_date} | Copied to latest: {copied_date}*"
            metadata_added = True
            break

    if not metadata_added:
        # If no generation date found, add it after the header
        for i, line in enumerate(lines):
            if line.startswith('# '):
                lines.insert(i + 1, f"\n*Generated on: {original_date} | Copied to latest: {copied_date}*\n")
                break

    return '\n'.join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: update_latest_reports.py <current_date>")
        sys.exit(1)

    current_date = sys.argv[1]
    latest_dir = "latest_comparison_reports"

    # Create latest directory if it doesn't exist
    os.makedirs(latest_dir, exist_ok=True)

    # Find all date directories
    all_dates = find_all_dates()

    if not all_dates:
        print("Error: No date directories found")
        sys.exit(1)

    print(f"Updating {latest_dir} folder...")
    print(f"Current date: {current_date}")
    print()

    # Define the reports to look for
    report_files = [
        "ci_reports_onnx_comparison_report.md",
        "hf-model-top1k_comparison_report.md",
        "ci_reports_onnx_dup_comparison_report.md",
        "gpu_vs_cpu_summary.md"
    ]

    copied_count = 0

    for report_file in report_files:
        # Find the latest version of this report
        source_path, source_date = find_latest_report(report_file, all_dates)

        if not source_path:
            print(f"⚠️  {report_file}: Not found in any date")
            continue

        # Read the source file
        with open(source_path, 'r') as f:
            content = f.read()

        # Add metadata
        updated_content = add_generation_metadata(content, source_date, current_date)

        # Write to latest directory
        dest_path = os.path.join(latest_dir, report_file)
        with open(dest_path, 'w') as f:
            f.write(updated_content)

        if source_date == current_date:
            print(f"✅ {report_file}: Copied from {source_date} (current)")
        else:
            print(f"📋 {report_file}: Copied from {source_date} (previous)")

        copied_count += 1

    print()
    print(f"Summary: {copied_count}/{len(report_files)} reports updated in {latest_dir}/")

    if copied_count == 0:
        print("Error: No reports were copied")
        sys.exit(1)


if __name__ == "__main__":
    main()
