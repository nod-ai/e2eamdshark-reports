#!/usr/bin/env python3
"""
Compare two summary.md files and generate a comparison report for passing and failing summaries.
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


def generate_comparison_report(file1_path, file2_path, output_path=None):
    """
    Compare two summary.md files and generate a comparison report.

    Args:
        file1_path: Path to the first (older) summary file
        file2_path: Path to the second (newer) summary file
        output_path: Optional path to save the report
    """
    data1 = parse_summary_file(file1_path)
    data2 = parse_summary_file(file2_path)

    report = []
    report.append("# Test Summary Comparison Report\n\n")
    report.append(f"**GPU Status:** `{file1_path}`\n")
    report.append(f"**CPU Status:** `{file2_path}`\n\n")

    # Total tests comparison
    report.append("## Total Tests\n\n")
    report.append(f"| Platform | Total Tests | Change |\n")
    report.append(f"|----------|-------------|--------|\n")
    report.append(f"| GPU | {data1['total_tests']} | - |\n")
    change = data2['total_tests'] - data1['total_tests']
    change_str = f"+{change}" if change > 0 else str(change)
    report.append(f"| CPU | {data2['total_tests']} | {change_str} |\n\n")

    # Passing Summary Comparison
    report.append("## Passing Summary Comparison\n\n")
    report.append("| Stage | GPU (# Passing) | CPU (# Passing) | Change |\n")
    report.append("|-------|-----------------|-----------------|--------|\n")

    for i, stage_data in enumerate(data1['passing_summary']):
        stage = stage_data['stage']
        pass1 = int(stage_data['passing'])

        # Find matching stage in data2
        matching = next((s for s in data2['passing_summary'] if s['stage'] == stage), None)
        if matching:
            pass2 = int(matching['passing'])
            change_count = pass2 - pass1
            change_str = f"+{change_count}" if change_count > 0 else str(change_count)

            report.append(f"| {stage} | {pass1} | {pass2} | {change_str} |\n")

    # Fail Summary Comparison
    report.append("\n## Fail Summary Comparison\n\n")
    report.append("| Stage | GPU (# Failed) | CPU (# Failed) | Change |\n")
    report.append("|-------|----------------|----------------|--------|\n")

    for i, stage_data in enumerate(data1['fail_summary']):
        stage = stage_data['stage']
        fail1 = int(stage_data['failed'])

        # Find matching stage in data2
        matching = next((s for s in data2['fail_summary'] if s['stage'] == stage), None)
        if matching:
            fail2 = int(matching['failed'])
            change_count = fail2 - fail1
            change_str = f"+{change_count}" if change_count > 0 else str(change_count)

            report.append(f"| {stage} | {fail1} | {fail2} | {change_str} |\n")

    # Summary
    report.append("\n## Summary\n\n")

    # Calculate key metrics
    if data1['passing_summary'] and data2['passing_summary']:
        final_pass1 = next((s for s in data1['passing_summary'] if 'Comparison' in s['stage']), None)
        final_pass2 = next((s for s in data2['passing_summary'] if 'Comparison' in s['stage']), None)

        if final_pass1 and final_pass2:
            pass1_count = int(final_pass1['passing'])
            pass2_count = int(final_pass2['passing'])
            improvement = pass2_count - pass1_count

            if improvement > 0:
                report.append(f"- CPU has +{improvement} more tests passing than GPU ({pass2_count} vs {pass1_count})\n")
            elif improvement < 0:
                report.append(f"- CPU has {improvement} fewer tests passing than GPU ({pass2_count} vs {pass1_count})\n")
            else:
                report.append(f"- No difference in passing tests between CPU and GPU ({pass2_count})\n")

    report_text = ''.join(report)

    # Output the report
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report_text)
        print(f"Comparison report saved to: {output_path}")
    else:
        print(report_text)


def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) < 3:
        print("Usage: python compare_files.py <file1> <file2> [output_file]")
        print("\nExample:")
        print("  python compare_files.py 2025-12-12/summary.md 2026-01-31/summary.md")
        print("  python compare_files.py 2025-12-12/summary.md 2026-01-31/summary.md comparison_report.md")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) > 3 else None

    generate_comparison_report(file1, file2, output)


if __name__ == "__main__":
    main()
