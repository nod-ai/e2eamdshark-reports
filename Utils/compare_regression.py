#!/usr/bin/env python3
"""
Compare two summary.md files from different dates to detect regressions.
Shows changes in test pass/fail counts over time for the same platform.
"""

import sys
import re
from pathlib import Path


def parse_summary_file(file_path):
    """
    Parse a summary.md file and extract passing and failing summary data.

    Returns:
        dict: Contains 'total_tests', 'passing_summary', 'fail_summary'
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {
        'total_tests': 0,
        'passing_summary': [],
        'fail_summary': []
    }

    # Extract total tests from Passing Summary
    total_match = re.search(r'\*\*TOTAL TESTS = (\d+)\*\*', content)
    if total_match:
        data['total_tests'] = int(total_match.group(1))

    # Extract Passing Summary table
    passing_section = re.search(
        r'## Passing Summary.*?\*\*TOTAL TESTS = \d+\*\*\s*\|(.+?)\|(.+?)\n((?:\|.+?\n)+)',
        content,
        re.DOTALL
    )
    if passing_section:
        lines = passing_section.group(3).strip().split('\n')
        for line in lines:
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) >= 4 and parts[0] != '--':
                data['passing_summary'].append({
                    'stage': parts[0],
                    'passing': parts[1],
                    'pct_total': parts[2],
                    'pct_attempted': parts[3]
                })

    # Extract Fail Summary table
    fail_section = re.search(
        r'## Fail Summary.*?\*\*TOTAL TESTS = \d+\*\*\s*\|(.+?)\|(.+?)\n((?:\|.+?\n)+)',
        content,
        re.DOTALL
    )
    if fail_section:
        lines = fail_section.group(3).strip().split('\n')
        for line in lines:
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) >= 3 and parts[0] != '--':
                data['fail_summary'].append({
                    'stage': parts[0],
                    'failed': parts[1],
                    'pct_total': parts[2]
                })

    return data


def generate_regression_report(old_file_path, new_file_path, platform_name, output_path=None):
    """
    Compare two summary.md files from different dates to detect regressions.

    Args:
        old_file_path: Path to the older summary file (baseline)
        new_file_path: Path to the newer summary file (current)
        platform_name: Name of the platform (e.g., "GPU (rocm)", "CPU (llvm-cpu)")
        output_path: Optional path to save the report
    """
    data_old = parse_summary_file(old_file_path)
    data_new = parse_summary_file(new_file_path)

    report = []
    report.append(f"# Regression Report - {platform_name}\n\n")
    report.append(f"**Previous Run:** `{old_file_path}`\n")
    report.append(f"**Current Run:** `{new_file_path}`\n\n")

    # Total tests comparison
    report.append("## Total Tests\n\n")
    report.append(f"| Status | Total Tests | Change |\n")
    report.append(f"|--------|-------------|--------|\n")
    report.append(f"| Previous | {data_old['total_tests']} | - |\n")
    change = data_new['total_tests'] - data_old['total_tests']
    change_str = f"+{change}" if change > 0 else str(change)
    report.append(f"| Current | {data_new['total_tests']} | {change_str} |\n\n")

    # Passing Summary Comparison
    report.append("## Passing Tests - Change Analysis\n\n")
    report.append("| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |\n")
    report.append("|-------|---------------------|---------------------|--------|--------|\n")

    regressions = []
    improvements = []

    for i, stage_data in enumerate(data_old['passing_summary']):
        stage = stage_data['stage']
        pass_old = int(stage_data['passing'])

        # Find matching stage in new data
        matching = next((s for s in data_new['passing_summary'] if s['stage'] == stage), None)
        if matching:
            pass_new = int(matching['passing'])
            change_count = pass_new - pass_old
            change_str = f"+{change_count}" if change_count > 0 else str(change_count)

            # Determine status
            if change_count < 0:
                status = "⚠️ REGRESSION"
                regressions.append((stage, change_count))
            elif change_count > 0:
                status = "✅ IMPROVED"
                improvements.append((stage, change_count))
            else:
                status = "➖ NO CHANGE"

            report.append(f"| {stage} | {pass_old} | {pass_new} | {change_str} | {status} |\n")

    # Fail Summary Comparison
    report.append("\n## Failing Tests - Change Analysis\n\n")
    report.append("| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |\n")
    report.append("|-------|--------------------|--------------------|--------|--------|\n")

    for i, stage_data in enumerate(data_old['fail_summary']):
        stage = stage_data['stage']
        fail_old = int(stage_data['failed'])

        # Find matching stage in new data
        matching = next((s for s in data_new['fail_summary'] if s['stage'] == stage), None)
        if matching:
            fail_new = int(matching['failed'])
            change_count = fail_new - fail_old
            change_str = f"+{change_count}" if change_count > 0 else str(change_count)

            # Determine status (more failures = regression)
            if change_count > 0:
                status = "⚠️ MORE FAILURES"
            elif change_count < 0:
                status = "✅ FEWER FAILURES"
            else:
                status = "➖ NO CHANGE"

            report.append(f"| {stage} | {fail_old} | {fail_new} | {change_str} | {status} |\n")

    # Summary
    report.append("\n## Summary\n\n")

    if regressions:
        report.append("### ⚠️ Regressions Detected\n\n")
        for stage, change in regressions:
            report.append(f"- **{stage}**: {change} fewer tests passing\n")
        report.append("\n")

    if improvements:
        report.append("### ✅ Improvements\n\n")
        for stage, change in improvements:
            report.append(f"- **{stage}**: +{change} more tests passing\n")
        report.append("\n")

    if not regressions and not improvements:
        report.append("### ➖ No Changes\n\n")
        report.append("No changes detected in passing tests.\n\n")

    # Overall verdict
    if regressions:
        report.append(f"**Overall Status:** ⚠️ REGRESSION DETECTED - Action may be required\n")
    elif improvements:
        report.append(f"**Overall Status:** ✅ IMPROVEMENTS DETECTED - Good progress!\n")
    else:
        report.append(f"**Overall Status:** ➖ STABLE - No changes\n")

    report_text = ''.join(report)

    # Output the report
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report_text)
        print(f"Regression report saved to: {output_path}")
    else:
        print(report_text)


def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) < 4:
        print("Usage: python compare_regression.py <old_file> <new_file> <platform_name> [output_file]")
        print("\nExample:")
        print("  python compare_regression.py 2026-01-30/summary.md 2026-01-31/summary.md 'GPU (rocm)'")
        print("  python compare_regression.py 2026-01-30/summary.md 2026-01-31/summary.md 'GPU (rocm)' regression.md")
        sys.exit(1)

    old_file = sys.argv[1]
    new_file = sys.argv[2]
    platform_name = sys.argv[3]
    output = sys.argv[4] if len(sys.argv) > 4 else None

    generate_regression_report(old_file, new_file, platform_name, output)


if __name__ == "__main__":
    main()
