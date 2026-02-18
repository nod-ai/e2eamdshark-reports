#!/usr/bin/env python3
"""
Generate email-friendly HTML versions of comparison reports.
Uses inline CSS and table-based layouts for maximum email client compatibility.
"""

import os
import sys
import re
from datetime import datetime


def parse_markdown_table(table_lines):
    """Parse markdown table into list of rows."""
    rows = []
    for line in table_lines:
        if '|---' in line or not line.strip():
            continue
        if line.strip().startswith('|'):
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            if cells:
                rows.append(cells)
    return rows


def extract_sections_from_report(file_path):
    """Extract necessary sections from a comparison report."""
    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as f:
        content = f.read()

    # Extract metadata
    date_match = re.search(r'\*Generated on: (.+?)\s*(?:\||\*)', content)
    report_date = date_match.group(1).strip() if date_match else "Unknown"

    # Find the GPU vs CPU Comparison section
    section_match = re.search(r'# GPU vs CPU Comparison\n\n(.*?)(?=\n---\n|\n# [^#]|\Z)', content, re.DOTALL)
    if not section_match:
        return None

    section_content = section_match.group(0)
    lines = section_content.split('\n')

    # Extract GPU and CPU status
    gpu_status = ""
    cpu_status = ""
    for line in lines:
        if line.startswith("**GPU Status:**"):
            gpu_status = re.sub(r'`([^`]+)`', r'\1', line.replace("**GPU Status:**", "").strip())
        elif line.startswith("**CPU Status:**"):
            cpu_status = re.sub(r'`([^`]+)`', r'\1', line.replace("**CPU Status:**", "").strip())

    # Extract tables
    in_total_tests = False
    in_passing = False
    in_fail = False

    total_tests_lines = []
    passing_lines = []
    fail_lines = []

    for line in lines:
        if line.strip() == "## Total Tests":
            in_total_tests = True
            in_passing = False
            in_fail = False
            continue
        elif line.strip() == "## Passing Summary":
            in_total_tests = False
            in_passing = True
            in_fail = False
            continue
        elif line.strip() == "## Fail Summary":
            in_total_tests = False
            in_passing = False
            in_fail = True
            continue
        elif line.strip().startswith("##") or line.strip() == "---":
            in_total_tests = False
            in_passing = False
            in_fail = False
            continue

        if in_total_tests and line.strip().startswith('|'):
            total_tests_lines.append(line)
        elif in_passing and line.strip().startswith('|'):
            passing_lines.append(line)
        elif in_fail and line.strip().startswith('|'):
            fail_lines.append(line)

    return {
        'date': report_date,
        'gpu_status': gpu_status,
        'cpu_status': cpu_status,
        'total_tests': parse_markdown_table(total_tests_lines),
        'passing': parse_markdown_table(passing_lines),
        'fail': parse_markdown_table(fail_lines)
    }


def generate_html_table(headers, rows, table_style="", cell_style=""):
    """Generate HTML table with inline styles."""
    html = f'<table style="border-collapse: collapse; width: 100%; {table_style}">\n'

    # Header row
    html += '  <tr style="background-color: #f0f0f0;">\n'
    for header in headers:
        html += f'    <th style="border: 1px solid #ddd; padding: 8px; text-align: left; font-weight: bold; {cell_style}">{header}</th>\n'
    html += '  </tr>\n'

    # Data rows
    for i, row in enumerate(rows):
        bg_color = '#ffffff' if i % 2 == 0 else '#f9f9f9'
        html += f'  <tr style="background-color: {bg_color};">\n'
        for cell in row:
            html += f'    <td style="border: 1px solid #ddd; padding: 8px; {cell_style}">{cell}</td>\n'
        html += '  </tr>\n'

    html += '</table>\n'
    return html


def generate_section_html(report_name, data):
    """Generate HTML for a single comparison section."""
    # Create clickable links for GPU and CPU status
    gpu_link = f'https://github.com/nod-ai/e2eamdshark-reports/blob/main/{data["gpu_status"]}'
    cpu_link = f'https://github.com/nod-ai/e2eamdshark-reports/blob/main/{data["cpu_status"]}'

    html = f'''
<div style="margin-bottom: 40px; font-family: Arial, sans-serif;">
  <div style="display: table; width: 100%; border-bottom: 2px solid #0066cc; padding-bottom: 10px;">
    <h2 style="display: table-cell; color: #333; margin: 0; vertical-align: middle;">{report_name}</h2>
    <div style="display: table-cell; text-align: right; vertical-align: middle; font-size: 11px; color: #666;">
      <em>Generated: {data['date']}</em>
    </div>
  </div>
  <p style="color: #666; font-size: 12px; margin: 10px 0;">
    <strong>GPU Status:</strong> <a href="{gpu_link}" style="color: #0066cc; text-decoration: none; background-color: #f5f5f5; padding: 2px 4px; font-size: 11px; font-family: monospace;">{data['gpu_status']}</a><br>
    <strong>CPU Status:</strong> <a href="{cpu_link}" style="color: #0066cc; text-decoration: none; background-color: #f5f5f5; padding: 2px 4px; font-size: 11px; font-family: monospace;">{data['cpu_status']}</a>
  </p>
'''

    # Total Tests - check if GPU and CPU have the same count
    if data['total_tests'] and len(data['total_tests']) > 1:
        html += '  <h3 style="color: #444; margin-top: 20px;">Total Tests</h3>\n'

        # Extract GPU and CPU rows
        gpu_row = None
        cpu_row = None
        for row in data['total_tests'][1:]:
            if row[0] == 'GPU':
                gpu_row = row
            elif row[0] == 'CPU':
                cpu_row = row

        # Check if both have the same total
        if gpu_row and cpu_row and gpu_row[1] == cpu_row[1]:
            html += f'  <p style="color: #555; margin: 5px 0;"><strong>Total Tests:</strong> {gpu_row[1]} (same for both GPU and CPU)</p>\n'
        else:
            # Show table without "Change" column
            headers = [data['total_tests'][0][0], data['total_tests'][0][1]]  # Platform, Total Tests
            rows = [[row[0], row[1]] for row in data['total_tests'][1:]]
            html += generate_html_table(headers, rows)

    # Side-by-side tables using HTML table layout
    html += '''
  <table style="width: 100%; margin-top: 20px;" cellpadding="0" cellspacing="0">
    <tr>
      <td style="width: 48%; vertical-align: top; padding-right: 2%;">
        <h3 style="color: #0d7c0d; margin-bottom: 10px;">✓ Passing Summary</h3>
'''

    # Passing table
    if data['passing'] and len(data['passing']) > 1:
        # Remove "Change" column if it exists
        headers = data['passing'][0][:3]  # Stage, GPU, CPU
        rows = [row[:3] for row in data['passing'][1:]]
        html += generate_html_table(headers, rows)

    html += '''
      </td>
      <td style="width: 48%; vertical-align: top; padding-left: 2%;">
        <h3 style="color: #cc3333; margin-bottom: 10px;">✗ Fail Summary</h3>
'''

    # Fail table
    if data['fail'] and len(data['fail']) > 1:
        # Remove "Change" column if it exists
        headers = data['fail'][0][:3]  # Stage, GPU, CPU
        rows = [row[:3] for row in data['fail'][1:]]
        html += generate_html_table(headers, rows)

    html += '''
      </td>
    </tr>
  </table>
</div>
<hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">
'''

    return html


def generate_email_html(date_dir, output_file=None):
    """Generate complete email-friendly HTML from all comparison reports."""
    if not output_file:
        output_file = f"{date_dir}/comparison_reports/gpu_vs_cpu_email.html"

    comparison_reports_dir = f"{date_dir}/comparison_reports"

    if not os.path.exists(comparison_reports_dir):
        print(f"Error: Directory '{comparison_reports_dir}' does not exist")
        return False

    # Define the reports to look for
    report_configs = [
        ("ci_reports_onnx_comparison_report.md", "CI Reports ONNX Comparison"),
        ("hf-model-top1k_comparison_report.md", "HuggingFace Model Top1K Comparison"),
        ("ci_reports_onnx_dup_comparison_report.md", "CI Reports ONNX Dup Comparison")
    ]

    # Find and parse all reports
    sections_html = []
    sections_found = 0

    # Import the find_latest_report function
    sys.path.insert(0, 'Utils')
    try:
        from extract_gpu_cpu_comparison import find_latest_report
    except ImportError:
        # Fallback: search only in current date
        def find_latest_report(report_file, current_date_dir):
            path = os.path.join(current_date_dir, "comparison_reports", report_file)
            if os.path.exists(path):
                return path, current_date_dir.split('/')[-1]
            return None, None

    for report_file, report_name in report_configs:
        report_path, report_date = find_latest_report(report_file, date_dir)

        if not report_path:
            print(f"Warning: Report '{report_file}' not found. Skipping...")
            continue

        if report_date != date_dir:
            print(f"Processing: {report_file} (from {report_date})")
            display_name = f"{report_name} ({report_date})"
        else:
            print(f"Processing: {report_file}")
            display_name = f"{report_name} ({report_date})"

        data = extract_sections_from_report(report_path)
        if data:
            sections_html.append(generate_section_html(display_name, data))
            sections_found += 1
        else:
            print(f"  Warning: Could not extract data from {report_file}")

    if sections_found == 0:
        print("Error: No sections were extracted")
        return False

    # Generate complete HTML document
    current_date = datetime.now().strftime("%Y-%m-%d")

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GPU vs CPU Comparison Summary</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 1200px; margin: 0 auto; padding: 20px; background-color: #f5f5f5;">
    <div style="background-color: #ffffff; padding: 30px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <div style="display: table; width: 100%; border-bottom: 3px solid #0066cc; padding-bottom: 15px; margin-top: 0;">
            <h1 style="display: table-cell; color: #0066cc; margin: 0; vertical-align: middle;">
                GPU vs CPU Comparison Summary
            </h1>
            <div style="display: table-cell; text-align: right; vertical-align: middle; font-size: 13px; color: #666;">
                <em>Compiled: {date_dir} | Generated: {current_date}</em>
            </div>
        </div>

        {chr(10).join(sections_html)}

        <div style="margin-top: 40px; padding: 20px; background-color: #f0f8ff; border-left: 4px solid #0066cc; font-size: 12px; color: #555;">
            <p style="margin: 0;"><strong>Note:</strong> This is an automated report generated from the e2eamdshark-reports repository.</p>
            <p style="margin: 10px 0 0 0;">For detailed information, visit the repository or check the date-specific folders.</p>
        </div>
    </div>
</body>
</html>
'''

    # Write output file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(html_content)

    print(f"\nEmail-friendly HTML generated: {output_file}")
    print(f"Sections included: {sections_found}")
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: generate_email_html.py <date_dir> [output_file]")
        sys.exit(1)

    date_dir = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    success = generate_email_html(date_dir, output_file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
