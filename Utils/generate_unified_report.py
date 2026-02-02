#!/usr/bin/env python3
"""
Generate a unified comparison report containing:
1. GPU vs CPU comparison
2. GPU regression (vs previous date)
3. CPU regression (vs previous date)
"""

import sys
import re
from pathlib import Path


def parse_summary_file(file_path):
    """
    Parse a summary.md file and extract passing and failing summary data.

    Returns:
        dict: Contains 'total_tests', 'passing_summary', 'fail_summary', 'test_results'
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {
        'total_tests': 0,
        'passing_summary': [],
        'fail_summary': [],
        'test_results': {}
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

    # Extract individual test results
    test_section = re.search(
        r'## Test Run Detail.*?\| Test \| Exit Status \|.*?\n\|--\|--\|.*?\n((?:\|.+?\n)+)',
        content,
        re.DOTALL
    )
    if test_section:
        lines = test_section.group(1).strip().split('\n')
        for line in lines:
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) >= 2:
                test_name = parts[0]
                exit_status = parts[1]
                data['test_results'][test_name] = exit_status

    return data


def generate_gpu_vs_cpu_section(gpu_data, cpu_data, gpu_path, cpu_path):
    """Generate GPU vs CPU comparison section."""
    report = []
    report.append("# GPU vs CPU Comparison\n\n")
    report.append(f"**GPU Status:** `{gpu_path}`\n")
    report.append(f"**CPU Status:** `{cpu_path}`\n\n")

    # Total tests comparison
    report.append("## Total Tests\n\n")
    report.append(f"| Platform | Total Tests | Change |\n")
    report.append(f"|----------|-------------|--------|\n")
    report.append(f"| GPU | {gpu_data['total_tests']} | - |\n")
    change = cpu_data['total_tests'] - gpu_data['total_tests']
    change_str = f"+{change}" if change > 0 else str(change)
    report.append(f"| CPU | {cpu_data['total_tests']} | {change_str} |\n\n")

    # Passing Summary Comparison
    report.append("## Passing Summary\n\n")
    report.append("| Stage | GPU (# Passing) | CPU (# Passing) | Change |\n")
    report.append("|-------|-----------------|-----------------|--------|\n")

    for stage_data in gpu_data['passing_summary']:
        stage = stage_data['stage']
        pass_gpu = int(stage_data['passing'])

        matching = next((s for s in cpu_data['passing_summary'] if s['stage'] == stage), None)
        if matching:
            pass_cpu = int(matching['passing'])
            change_count = pass_cpu - pass_gpu
            change_str = f"+{change_count}" if change_count > 0 else str(change_count)
            report.append(f"| {stage} | {pass_gpu} | {pass_cpu} | {change_str} |\n")

    # Fail Summary Comparison
    report.append("\n## Fail Summary\n\n")
    report.append("| Stage | GPU (# Failed) | CPU (# Failed) | Change |\n")
    report.append("|-------|----------------|----------------|--------|\n")

    for stage_data in gpu_data['fail_summary']:
        stage = stage_data['stage']
        fail_gpu = int(stage_data['failed'])

        matching = next((s for s in cpu_data['fail_summary'] if s['stage'] == stage), None)
        if matching:
            fail_cpu = int(matching['failed'])
            change_count = fail_cpu - fail_gpu
            change_str = f"+{change_count}" if change_count > 0 else str(change_count)
            report.append(f"| {stage} | {fail_gpu} | {fail_cpu} | {change_str} |\n")

    return ''.join(report)


def generate_regression_section(old_data, new_data, platform_name, old_path, new_path):
    """Generate regression comparison section."""
    report = []
    report.append(f"# {platform_name} - Regression Analysis\n\n")
    report.append(f"**Previous Run:** `{old_path}`\n")
    report.append(f"**Current Run:** `{new_path}`\n\n")

    # Total tests comparison
    report.append("## Total Tests\n\n")
    report.append(f"| Status | Total Tests | Change |\n")
    report.append(f"|--------|-------------|--------|\n")
    report.append(f"| Previous | {old_data['total_tests']} | - |\n")
    change = new_data['total_tests'] - old_data['total_tests']
    change_str = f"+{change}" if change > 0 else str(change)
    report.append(f"| Current | {new_data['total_tests']} | {change_str} |\n\n")

    # Passing Summary Comparison
    report.append("## Passing Tests - Change Analysis\n\n")
    report.append("| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |\n")
    report.append("|-------|---------------------|---------------------|--------|--------|\n")

    regressions = []
    improvements = []

    for stage_data in old_data['passing_summary']:
        stage = stage_data['stage']
        pass_old = int(stage_data['passing'])

        matching = next((s for s in new_data['passing_summary'] if s['stage'] == stage), None)
        if matching:
            pass_new = int(matching['passing'])
            change_count = pass_new - pass_old
            change_str = f"+{change_count}" if change_count > 0 else str(change_count)

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

    for stage_data in old_data['fail_summary']:
        stage = stage_data['stage']
        fail_old = int(stage_data['failed'])

        matching = next((s for s in new_data['fail_summary'] if s['stage'] == stage), None)
        if matching:
            fail_new = int(matching['failed'])
            change_count = fail_new - fail_old
            change_str = f"+{change_count}" if change_count > 0 else str(change_count)

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
        report.append(f"**Overall Status:** ⚠️ REGRESSION DETECTED\n\n")
    elif improvements:
        report.append(f"**Overall Status:** ✅ IMPROVEMENTS DETECTED\n\n")
    else:
        report.append(f"**Overall Status:** ➖ STABLE\n\n")

    # Detailed model-level regression analysis
    if old_data.get('test_results') and new_data.get('test_results'):
        regressed_models = []
        improved_models = []

        # Find tests that changed status
        for test_name, old_status in old_data['test_results'].items():
            new_status = new_data['test_results'].get(test_name)

            if new_status:
                # Regression: was PASS, now something else
                if old_status == 'PASS' and new_status != 'PASS':
                    regressed_models.append((test_name, old_status, new_status))
                # Improvement: was not PASS, now PASS
                elif old_status != 'PASS' and new_status == 'PASS':
                    improved_models.append((test_name, old_status, new_status))

        # Add new failures (tests that didn't exist before or were added)
        for test_name, new_status in new_data['test_results'].items():
            if test_name not in old_data['test_results'] and new_status != 'PASS':
                regressed_models.append((test_name, 'N/A', new_status))

        if regressed_models:
            report.append("### 🔍 Regressed Models\n\n")
            report.append("The following models regressed from PASS to FAIL/Numerics/other:\n\n")
            report.append("| Model Name | Previous Status | Current Status |\n")
            report.append("|------------|----------------|----------------|\n")
            for model, old_st, new_st in regressed_models[:50]:  # Limit to first 50
                report.append(f"| {model} | {old_st} | {new_st} |\n")

            if len(regressed_models) > 50:
                report.append(f"\n*... and {len(regressed_models) - 50} more regressed models*\n")

            report.append(f"\n**Total regressed models: {len(regressed_models)}**\n\n")

        if improved_models:
            report.append("### 🎉 Improved Models\n\n")
            report.append("The following models improved from FAIL/Numerics/other to PASS:\n\n")
            report.append("| Model Name | Previous Status | Current Status |\n")
            report.append("|------------|----------------|----------------|\n")
            for model, old_st, new_st in improved_models[:50]:  # Limit to first 50
                report.append(f"| {model} | {old_st} | {new_st} |\n")

            if len(improved_models) > 50:
                report.append(f"\n*... and {len(improved_models) - 50} more improved models*\n")

            report.append(f"\n**Total improved models: {len(improved_models)}**\n\n")

    return ''.join(report)


def generate_unified_report(gpu_current, cpu_current, gpu_previous, cpu_previous, output_path):
    """
    Generate a unified report with all comparisons.

    Args:
        gpu_current: Path to current GPU summary
        cpu_current: Path to current CPU summary
        gpu_previous: Path to previous GPU summary (can be None)
        cpu_previous: Path to previous CPU summary (can be None)
        output_path: Path to save the unified report
    """
    report = []
    report.append("---\n")
    report.append("# Test Comparison Report\n\n")
    report.append(f"*Generated on: {Path(gpu_current).parts[-5]}*\n\n")
    report.append("---\n\n")

    # Section 1: GPU vs CPU
    gpu_data = parse_summary_file(gpu_current)
    cpu_data = parse_summary_file(cpu_current)
    report.append(generate_gpu_vs_cpu_section(gpu_data, cpu_data, gpu_current, cpu_current))
    report.append("\n---\n\n")

    # Section 2: GPU Regression
    if gpu_previous:
        gpu_prev_data = parse_summary_file(gpu_previous)
        report.append(generate_regression_section(gpu_prev_data, gpu_data, "GPU (rocm)", gpu_previous, gpu_current))
        report.append("\n---\n\n")
    else:
        report.append("# GPU (rocm) - Regression Analysis\n\n")
        report.append("**Status:** No previous GPU data found for comparison.\n\n")
        report.append("---\n\n")

    # Section 3: CPU Regression
    if cpu_previous:
        cpu_prev_data = parse_summary_file(cpu_previous)
        report.append(generate_regression_section(cpu_prev_data, cpu_data, "CPU (llvm-cpu)", cpu_previous, cpu_current))
        report.append("\n---\n\n")
    else:
        report.append("# CPU (llvm-cpu) - Regression Analysis\n\n")
        report.append("**Status:** No previous CPU data found for comparison.\n\n")
        report.append("---\n\n")

    # Write the report
    report_text = ''.join(report)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report_text)

    print(f"Unified comparison report saved to: {output_path}")


def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) < 6:
        print("Usage: python generate_unified_report.py <gpu_current> <cpu_current> <gpu_previous> <cpu_previous> <output_file>")
        print("\nNote: Use 'none' for gpu_previous or cpu_previous if no previous data exists")
        print("\nExample:")
        print("  python generate_unified_report.py \\")
        print("    2026-01-31/rocm/combined-reports/summary.md \\")
        print("    2026-01-31/llvm-cpu/combined-reports/summary.md \\")
        print("    2026-01-30/rocm/combined-reports/summary.md \\")
        print("    2026-01-30/llvm-cpu/combined-reports/summary.md \\")
        print("    comparison_report.md")
        sys.exit(1)

    gpu_current = sys.argv[1]
    cpu_current = sys.argv[2]
    gpu_previous = sys.argv[3] if sys.argv[3] != 'none' else None
    cpu_previous = sys.argv[4] if sys.argv[4] != 'none' else None
    output = sys.argv[5]

    generate_unified_report(gpu_current, cpu_current, gpu_previous, cpu_previous, output)


if __name__ == "__main__":
    main()
