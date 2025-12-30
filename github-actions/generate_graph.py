import pandas as pd
from pathlib import Path
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sys

#CSV_PATH = Path("track_test_data/passing_summary_daily.csv")
#OUTPUT_HTML = Path("track_test_data/passing_summary_last_30_days.html")
if len(sys.argv) != 3:
        print("Usage: python generate_graph.py <csv_path> <output_html>")
        sys.exit(1)

CSV_PATH = Path(sys.argv[1])
OUTPUT_HTML = Path(sys.argv[2])

# Read CSV
df = pd.read_csv(CSV_PATH, parse_dates=["date"])

# Sort & take last 30 days
df = df.sort_values("date").tail(30)

# Create 5-row subplot layout
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
    showlegend=False,
    xaxis_title="Date",
)

# Write single self-contained HTML
fig.write_html(OUTPUT_HTML, include_plotlyjs="cdn")

print(f"HTML report generated at: {OUTPUT_HTML}")

