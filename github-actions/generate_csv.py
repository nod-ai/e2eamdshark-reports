# Copyright 2025 Advanced Micro Devices, Inc.
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

'''
Generates the csv file as a dataframe to track datewise pass status
'''

import csv
from datetime import date
from pathlib import Path
import sys


def extract_passing_summary(summary_text: str) -> dict:
    """
    Extract '# Passing' values ONLY from the Passing Summary table.
    """
    stage_map = {
        "Setup": "setup",
        "IREE Compilation": "iree_compilation",
        "Gold Inference": "gold_inference",
        "IREE Inference Invocation": "iree_inference_invocation",
        "Inference Comparison (PASS)": "inference_comparison_pass",
    }

    results = {}

    try:
        passing_block = summary_text.split("## Passing Summary", 1)[1]
        passing_block = passing_block.split("## Fail Summary", 1)[0]
    except IndexError:
        return results

    for line in passing_block.splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("|--"):
            continue

        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 4:
            continue

        stage, passing = cols[0], cols[1]

        if stage in stage_map and passing.isdigit():
            results[stage_map[stage]] = int(passing)

    return results


def append_daily_csv(summary_text: str, csv_path: Path):
    today = date.today().isoformat()

    data = extract_passing_summary(summary_text)
    data["date"] = today

    fieldnames = [
        "date",
        "setup",
        "iree_compilation",
        "gold_inference",
        "iree_inference_invocation",
        "inference_comparison_pass",
    ]

    for key in fieldnames:
        data.setdefault(key, "")

    csv_path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not csv_path.exists()

    with csv_path.open("a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(data)


if __name__ == "__main__":
    summary_path = Path(sys.argv[1])
    csv_path = Path(sys.argv[2])
    summary_text = summary_path.read_text()
    append_daily_csv(summary_text, csv_path)

