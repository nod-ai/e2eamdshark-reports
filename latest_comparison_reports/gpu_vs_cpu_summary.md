# GPU vs CPU Comparison Summary

*Generated on: 2026-02-18 | Copied to latest: 2026-02-18*


*Compiled on: 2026-02-18*

---

## CI Reports ONNX Comparison (2026-02-18)

**GPU Status:** `2026-02-18/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-18/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

### Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

<div style="display: flex; gap: 20px;">
<div style="flex: 1;">

### Passing Summary

| Stage | GPU | CPU |
|-------|-----|-----|
| Setup | 4103 | 4103 |
| IREE Compilation | 3442 | 3969 |
| Gold Inference | 3442 | 3968 |
| IREE Inference Invocation | 3328 | 3934 |
| Inference Comparison (PASS) | 3195 | 3642 |

</div>
<div style="flex: 1;">

### Fail Summary

| Stage | GPU | CPU |
|-------|-----|-----|
| Setup | 4 | 4 |
| IREE Compilation | 661 | 134 |
| Gold Inference | 0 | 1 |
| IREE Inference Invocation | 114 | 34 |
| Inference Comparison | 133 | 292 |

</div>
</div>

---

## HuggingFace Model Top1K Comparison (2026-02-18)

**GPU Status:** `2026-02-18/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-18/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

### Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

<div style="display: flex; gap: 20px;">
<div style="flex: 1;">

### Passing Summary

| Stage | GPU | CPU |
|-------|-----|-----|
| Setup | 494 | 493 |
| IREE Compilation | 398 | 403 |
| Gold Inference | 396 | 401 |
| IREE Inference Invocation | 394 | 397 |
| Inference Comparison (PASS) | 380 | 366 |

</div>
<div style="flex: 1;">

### Fail Summary

| Stage | GPU | CPU |
|-------|-----|-----|
| Setup | 13 | 14 |
| IREE Compilation | 96 | 90 |
| Gold Inference | 2 | 2 |
| IREE Inference Invocation | 2 | 4 |
| Inference Comparison | 14 | 31 |

</div>
</div>

---

## CI Reports ONNX Dup Comparison (2026-02-15)

**GPU Status:** `2026-02-15/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-02-15/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

### Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

<div style="display: flex; gap: 20px;">
<div style="flex: 1;">

### Passing Summary

| Stage | GPU | CPU |
|-------|-----|-----|
| Setup | 2360 | 1987 |
| IREE Compilation | 2133 | 1942 |
| Gold Inference | 2133 | 1942 |
| IREE Inference Invocation | 2132 | 1940 |
| Inference Comparison (PASS) | 2111 | 1906 |

</div>
<div style="flex: 1;">

### Fail Summary

| Stage | GPU | CPU |
|-------|-----|-----|
| Setup | 1 | 374 |
| IREE Compilation | 227 | 45 |
| Gold Inference | 0 | 0 |
| IREE Inference Invocation | 1 | 2 |
| Inference Comparison | 21 | 34 |

</div>
</div>

---

