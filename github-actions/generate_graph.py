import pandas as pd
from pathlib import Path
import plotly.graph_objects as go
from plotly.subplots import make_subplots

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "track_test_data/passing_summary_daily.csv"
OUTPUT_HTML = ROOT / "track_test_data/passing_summary_last_30_days.html"

df = pd.read_csv(CSV_PATH, parse_dates=["date"])

numeric_cols = [
    "setup",
    "iree_compilation",
    "gold_inference",
    "iree_inference_invocation",
    "inference_comparison_pass",
]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

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
    showlegend=False,
    xaxis_title="Date",
)

fig.write_html(OUTPUT_HTML, include_plotlyjs=True)

print(f"HTML report generated at: {OUTPUT_HTML}")

