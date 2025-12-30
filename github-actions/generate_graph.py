# Copyright 2025 Advanced Micro Devices, Inc.
#
# Licensed under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

'''
Generates/Updates the graph for daily passing status tracking
'''

import pandas as pd
from pathlib import Path
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sys

if len(sys.argv) != 3:
        print("Usage: python generate_graph.py <csv_path> <output_html>")
        sys.exit(1)

CSV_PATH = Path(sys.argv[1])
OUTPUT_HTML = Path(sys.argv[2])

df = pd.read_csv(CSV_PATH, parse_dates=["date"])

df = df.sort_values("date").tail(30)

fig = make_subplots(
    rows=5,
    cols=1,
    shared_xaxes=True,
    subplot_titles=[
        "Setup",
        "IREE Compilation",
        "Gold Inference",
        "IREE Inference Invocation",
        "Inference Comparison (PASS)",
    ],
)

plots = [
    ("setup", 1),
    ("iree_compilation", 2),
    ("gold_inference", 3),
    ("iree_inference_invocation", 4),
    ("inference_comparison_pass", 5),
]

for column, row in plots:
    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df[column],
            mode="lines+markers",
            name=column,
        ),
        row=row,
        col=1,
    )

fig.update_layout(
    height=1400,
    title_text="Passing Summary – Last 30 Days",
    showlegend=True,
    xaxis_title="Date",
)

fig.write_html(OUTPUT_HTML, include_plotlyjs="cdn")

print(f"HTML report generated at: {OUTPUT_HTML}")

