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

if len(sys.argv) != 4:
    print("Usage: python generate_graph.py <cpu_csv> <gpu_csv> <output_html>")
    sys.exit(1)

CPU_CSV = Path(sys.argv[1])
GPU_CSV = Path(sys.argv[2])
OUTPUT_HTML = Path(sys.argv[3])

# Read CSVs
cpu_df = pd.read_csv(CPU_CSV, parse_dates=["date"])
gpu_df = pd.read_csv(GPU_CSV, parse_dates=["date"])

# Sort & take last 30 days
cpu_df = cpu_df.sort_values("date").tail(30)
gpu_df = gpu_df.sort_values("date").tail(30)

# Create subplot layout (one row per stage)
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
    # CPU trace
    fig.add_trace(
        go.Scatter(
            x=cpu_df["date"],
            y=cpu_df[column],
            mode="lines+markers",
            name=f"{column} (CPU)",
        ),
        row=row,
        col=1,
    )

    # GPU trace
    fig.add_trace(
        go.Scatter(
            x=gpu_df["date"],
            y=gpu_df[column],
            mode="lines+markers",
            name=f"{column} (GPU)",
        ),
        row=row,
        col=1,
    )

fig.update_layout(
    height=1500,
    title_text="Passing Summary – CPU vs GPU (Last 30 Days)",
    showlegend=True,
    xaxis_title="Date",
)

fig.write_html(OUTPUT_HTML, include_plotlyjs="cdn")
print(f"HTML report generated at: {OUTPUT_HTML}")

