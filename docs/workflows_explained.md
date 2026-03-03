# CI Workflow Documentation

This document explains how the CI workflows function across two repositories to test 2000+ ML models, track regressions, bisect commits to find the cause, and send daily reports via email.

---

## Overview

The CI pipeline spans **two repositories**:

| Repository | Purpose |
|------------|---------|
| [nod-ai/AMD-SHARK-TestSuite](https://github.com/nod-ai/AMD-SHARK-TestSuite) | Runs the actual E2E tests on models |
| [nod-ai/e2eamdshark-reports](https://github.com/nod-ai/e2eamdshark-reports) (this repo) | Stores reports, tracks regressions, bisects commits, sends emails |

---

## Workflow Execution Order

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    nod-ai/AMD-SHARK-TestSuite                               │
│                                                                             │
│  1. test_e2eamdshark.yml          - Daily ONNX model tests                  │
│  2. test_e2e_hf_top_1000.yml      - Daily HuggingFace Top 1K model tests    │
│  3. test_e2eamdshark_for_weekly.yml - Weekly comprehensive tests            │
│                                                                             │
│  Output: Test reports pushed to e2eamdshark-reports repo                    │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    nod-ai/e2eamdshark-reports (this repo)                   │
│                                                                             │
│  4. CI-tracker.yml                - Track daily pass rates, generate graphs │
│  5. CI-bisect.yml                 - Bisect ONNX model regressions           │
│  6. CI-bisect_hf.yml              - Bisect HuggingFace model regressions    │
│  7. generate-comparison-reports.yml - Generate comparison reports & email   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Upstream Workflows (nod-ai/AMD-SHARK-TestSuite)

### 1. `test_e2eamdshark.yml`
Runs E2E tests on ONNX models using the AMD-SHARK/IREE/MLIR infrastructure.

- **Trigger**: Daily scheduled run
- **Backends**: `llvm-cpu` (CPU) and `rocm` (GPU)
- **Output**: Creates dated folders with test reports in this repo

### 2. `test_e2e_hf_top_1000.yml`
Runs E2E tests on the top 1000 HuggingFace models.

- **Trigger**: Daily scheduled run
- **Categories tested**: feature-extraction, fill-mask, image-classification, image-segmentation, multiple-choice, object-detection, question-answering, semantic-segmentation, text-classification, token-classification
- **Output**: Reports stored in `YYYY-MM-DD/hf-model-top1k/` directories

### 3. `test_e2eamdshark_for_weekly.yml`
Extended weekly test run with additional coverage.

---

## This Repository's Workflows

### 4. `CI-tracker.yml` - Data Tracker

**Purpose**: Track daily pass rates and generate visual regression graphs.

**Schedule**: Daily at 22:18 UTC

**What it does**:
1. Reads today's `summary.md` files for both CPU and GPU backends
2. Extracts passing counts for each pipeline stage:
   - Setup
   - IREE Compilation
   - Gold Inference
   - IREE Inference Invocation
   - Inference Comparison (PASS)
3. Appends data to CSV files:
   - `track_test_data/llvm_cpu_passing_summary_daily.csv`
   - `track_test_data/rocm_passing_summary_daily.csv`
4. Generates an interactive HTML graph:
   - `track_test_data/regression_comparison_graph.html`
5. Commits and pushes the updated files

**View the graph**: [Regression Tracking Graph](https://nod-ai.github.io/e2eamdshark-reports/track_test_data/regression_comparison_graph.html)

---

### 5. `CI-bisect.yml` - ONNX Model Regression Bisect

**Purpose**: Find the exact IREE commit that caused a regression in ONNX models.

**Schedule**: Daily at 13:27 UTC

**Matrix**: Runs in parallel for both CPU and GPU

| Config | Device | Backend | Runner |
|--------|--------|---------|--------|
| CPU | CPU | llvm-cpu | nodai-cpu-x86-64 |
| GPU | GPU | rocm | linux-mi325-1gpu-ossci-nod-ai |

**Detailed Steps**:

```
┌────────────────────────────────────────────────────────────────────────────┐
│ Step 1: Extract Regression Models                                          │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Input:  YYYY-MM-DD/ci_reports_onnx/{backend}/combined-reports_unique/     │
│          yesterday_comparison.md                                           │
│                                                                            │
│  Process:                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ extract_model_old_new_status_from_md.py                             │   │
│  │ - Parses the "Regressions Found" section                            │   │
│  │ - Extracts model name, old status, new status                       │   │
│  │ - Outputs: github-actions/model_old_new_status.json                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                             │
│                              ▼                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ extract_regression_model_names.py                                   │   │
│  │ - Reads the JSON file                                               │   │
│  │ - Extracts just the model names                                     │   │
│  │ - Outputs: github-actions/regression_models.txt                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  Output: List of models that regressed from yesterday                      │
└────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────────┐
│ Step 2: Bisect Each Regression                                             │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  For each model in regression_models.txt:                                  │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ runbisect_for_model.sh                                              │   │
│  │                                                                     │   │
│  │ GOOD_COMMIT = 3rd most recent iree-3.X.0rc tag (known working)      │   │
│  │ BAD_COMMIT  = HEAD of IREE repo (currently broken)                  │   │
│  │                                                                     │   │
│  │ 1. git bisect start                                                 │   │
│  │ 2. git bisect bad $BAD_COMMIT                                       │   │
│  │ 3. git bisect good $GOOD_COMMIT                                     │   │
│  │ 4. git bisect run bisect_test.sh $MODEL $DEVICE                     │   │
│  │    └── Builds IREE at each commit and tests the model               │   │
│  │                                                                     │   │
│  │ 5. Verify the bisect result:                                        │   │
│  │    - Rebuild IREE at the identified bad commit                      │   │
│  │    - Re-run the model to confirm it fails                           │   │
│  │    - Compare with baseline to ensure regression is real             │   │
│  │                                                                     │   │
│  │ 6. Append to CSV: track_test_data/bisect_results_{DEVICE}.csv       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                            │
│  Output: CSV with Date, Model(Device), First Bad Commit                    │
└────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────────┐
│ Step 3: Push Artifacts                                                     │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  - Commits updated bisect_results_{DEVICE}.csv to main branch              │
│  - Cleans up temporary files (test-suite/, iree/, etc.)                    │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

---

### 6. `CI-bisect_hf.yml` - HuggingFace Model Regression Bisect

**Purpose**: Same as CI-bisect.yml but for HuggingFace Top 1K models.

**Schedule**: Daily at 11:45 UTC

**Key Differences from CI-bisect.yml**:
- Reads from: `YYYY-MM-DD/hf-model-top1k/{backend}/combined-reports_unique/yesterday_comparison.md`
- Installs additional HuggingFace requirements: `hf_requirements.txt`
- Outputs to: `track_test_data/bisect_results_{DEVICE}_HF.csv`
- Passes `"HF"` flag to `runbisect_for_model.sh`

---

### 7. `generate-comparison-reports.yml` - Report Generation & Email

**Purpose**: Generate GPU vs CPU comparison reports and send daily email notifications.

**Schedule**: Daily at 16:30 UTC

**Two Jobs**:

#### Job 1: `generate-comparison`

```
┌────────────────────────────────────────────────────────────────────────────┐
│ Generate Comparison Reports                                                │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  1. generate_comparison_reports.sh                                         │
│     └── Creates comparison reports between GPU and CPU test results        │
│                                                                            │
│  2. extract_gpu_cpu_comparison.py                                          │
│     └── Extracts summary data for GPU vs CPU comparison                    │
│                                                                            │
│  3. generate_email_html.py                                                 │
│     └── Creates email-friendly HTML with inline CSS                        │
│         Features:                                                          │
│         - Side-by-side tables (Passing vs Failing)                         │
│         - Color coding (green=pass, red=fail)                              │
│         - Mobile responsive design                                         │
│         - No external dependencies                                         │
│                                                                            │
│  4. update_latest_reports.py                                               │
│     └── Copies reports to latest_comparison_reports/                       │
│                                                                            │
│  Output Files:                                                             │
│  - YYYY-MM-DD/comparison_reports/                                          │
│  - latest_comparison_reports/gpu_vs_cpu_email.html                         │
│  - latest_comparison_reports/README.md                                     │
│  - latest_comparison_reports/EMAIL_INSTRUCTIONS.md                         │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

#### Job 2: `send-email`

```
┌────────────────────────────────────────────────────────────────────────────┐
│ Send Email                                                                 │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  Depends on: generate-comparison job                                       │
│  Runs on: self-hosted runner  ->  currently using yrathore's VDI machine   │
│  Only runs: On scheduled triggers (not workflow_dispatch)                  │
│                                                                            │
│  1. Downloads the latest-comparison-reports artifact                       │
│  2. Runs send_comparison_email.py                                          │
│     └── Sends HTML email with GPU vs CPU comparison                        │
│                                                                            │
│  Email Recipients: Defined in Utils/email_list.txt                         │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## Directory Structure

```
e2eamdshark-reports/
├── YYYY-MM-DD/                          # Daily test reports (one per day)
│   ├── ci_reports_onnx/                 # ONNX model test results
│   │   ├── llvm-cpu/                    # CPU backend results
│   │   │   └── combined-reports_unique/
│   │   │       ├── summary.md           # Overall pass/fail summary
│   │   │       ├── statusreport.md      # Per-model status
│   │   │       ├── timereport.md        # Per-model timing
│   │   │       └── yesterday_comparison.md  # Comparison with previous day
│   │   └── rocm/                        # GPU backend results
│   │       └── combined-reports_unique/
│   │           └── (same files as above)
│   ├── hf-model-top1k/                  # HuggingFace Top 1K test results
│   │   ├── llvm-cpu/
│   │   │   └── combined-reports_unique/
│   │   └── rocm/
│   │       └── combined-reports_unique/
│   └── comparison_reports/              # GPU vs CPU comparison
│
├── .github/workflows/                   # GitHub Actions workflows
│   ├── CI-bisect.yml                    # ONNX regression bisect
│   ├── CI-bisect_hf.yml                 # HuggingFace regression bisect
│   ├── CI-tracker.yml                   # Daily pass rate tracker
│   └── generate-comparison-reports.yml  # Comparison & email
│
├── github-actions/                      # Helper scripts for workflows
│   ├── bisect_test.sh                   # Test script for git bisect
│   ├── runbisect_for_model.sh           # Main bisect runner
│   ├── extract_model_old_new_status_from_md.py
│   ├── extract_regression_model_names.py
│   ├── check_model_status.py            # Verify bisect results
│   ├── generate_csv.py                  # Generate tracking CSVs
│   └── generate_graph.py                # Generate HTML graphs
│
├── Utils/                               # Utility scripts
│   ├── generate_comparison_reports.sh   # Create GPU vs CPU comparison
│   ├── extract_gpu_cpu_comparison.py    # Extract comparison data
│   ├── generate_email_html.py           # Create email-friendly HTML
│   ├── send_comparison_email.py         # Send email
│   ├── update_latest_reports.py         # Update latest_comparison_reports/
│   └── email_list.txt                   # Email recipients
│
├── track_test_data/                     # Historical tracking data
│   ├── llvm_cpu_passing_summary_daily.csv
│   ├── rocm_passing_summary_daily.csv
│   ├── regression_comparison_graph.html # Interactive graph
│   ├── bisect_results_CPU.csv           # ONNX CPU bisect results
│   ├── bisect_results_GPU.csv           # ONNX GPU bisect results
│   ├── bisect_results_CPU_HF.csv        # HF CPU bisect results
│   └── bisect_results_GPU_HF.csv        # HF GPU bisect results
│
└── latest_comparison_reports/           # Most recent comparison reports
    ├── gpu_vs_cpu_email.html            # Email-ready HTML
    ├── README.md
    └── EMAIL_INSTRUCTIONS.md            # How to send emails manually
```

---

## Report Types

### statusreport.md
Shows pass/fail status for each model across pipeline stages:
- Setup
- IREE Compilation
- Gold Inference
- IREE Inference Invocation
- Inference Comparison

### timereport.md
Shows execution time for each pipeline stage per model.

### summary.md
Aggregate statistics:
- Total models tested
- Pass/fail counts per stage
- Overall success rate

### yesterday_comparison.md
Compares today's results with yesterday's:
- **Regressions**: Models that passed yesterday but fail today
- **Progressions**: Models that failed yesterday but pass today

---

## How Bisect Works

When a regression is detected, the bisect process finds the exact IREE commit that caused it:

1. **Define boundaries**:
   - `GOOD_COMMIT`: 3rd most recent `iree-3.X.0rc` tag (known to work)
   - `BAD_COMMIT`: Current HEAD (known to fail)

2. **Binary search**:
   - Git bisect narrows down commits by testing the midpoint
   - At each step, IREE is built and the model is tested
   - Exit code 0 = good, non-zero = bad

3. **Verification**:
   - After bisect completes, the identified commit is verified
   - IREE is rebuilt at that commit
   - The model is re-tested to confirm the regression

4. **Output**:
   - Results appended to CSV: `Date, Model(Device), First Bad Commit`
   - Example: `2026-03-03, bert-base-uncased(GPU), a1b2c3d4e5f6`

---

## Schedule Summary

| Workflow | Schedule (UTC) | Purpose |
|----------|----------------|---------|
| CI-bisect_hf.yml | 11:45 daily | Bisect HuggingFace regressions |
| CI-bisect.yml | 13:27 daily | Bisect ONNX regressions |
| generate-comparison-reports.yml | 16:30 daily | Generate reports & send email |
| CI-tracker.yml | 22:18 daily | Track pass rates & update graphs |

---

## Manual Trigger

All workflows support `workflow_dispatch` for manual triggering:

1. Go to **Actions** tab in the repository
2. Select the desired workflow
3. Click **Run workflow**
4. Select branch and click **Run workflow**

---

## Secrets Required

| Secret | Purpose |
|--------|---------|
| `HF_TOKEN` | HuggingFace API token for model downloads |

---

## Key Links

- **Test Infrastructure**: [nod-ai/AMD-SHARK-TestSuite/e2eamdshark](https://github.com/nod-ai/AMD-SHARK-TestSuite/tree/main/e2eamdshark)
- **Regression Graph**: [Live Graph](https://nod-ai.github.io/e2eamdshark-reports/track_test_data/regression_comparison_graph.html)
- **IREE Repository**: [iree-org/iree](https://github.com/iree-org/iree)

---

## Troubleshooting

### Setup Failure
Occurs when running the tests, probably due to issues with CACHE_DIR.

### No report for today's date
The upstream test workflows may not have completed yet. Check the [AMD-SHARK-TestSuite Actions](https://github.com/nod-ai/AMD-SHARK-TestSuite/actions).

### Bisect not running
If no regressions are found in `yesterday_comparison.md`, the bisect step is skipped.

### Email not sent
- Check that the `generate-comparison` job succeeded
- Verify `gpu_vs_cpu_email.html` was created
- Check the self-hosted runner is online

### Graph not updating
- Verify `summary.md` exists for the current date
- Check that CSV files are being updated correctly

~
~
