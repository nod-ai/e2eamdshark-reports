---
# Test Comparison Report

*Generated on: 2026-05-26*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-26/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-26/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4103 | 4103 | 0 |
| IREE Compilation | 0 | 3960 | +3960 |
| Gold Inference | 0 | 3959 | +3959 |
| IREE Inference Invocation | 0 | 3935 | +3935 |
| Inference Comparison (PASS) | 0 | 3667 | +3667 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 4 | 4 | 0 |
| IREE Compilation | 4103 | 143 | -3960 |
| Gold Inference | 0 | 1 | +1 |
| IREE Inference Invocation | 0 | 24 | +24 |
| Inference Comparison | 0 | 268 | +268 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-25/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-26/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4102 | 4103 | +1 | ✅ IMPROVED |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 0 | 0 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 5 | 4 | -1 | ✅ FEWER FAILURES |
| IREE Compilation | 4102 | 4103 | +1 | ⚠️ MORE FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison | 0 | 0 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **Setup**: +1 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-25/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-26/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3960 | 3960 | 0 | ➖ NO CHANGE |
| Gold Inference | 3959 | 3959 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3947 | 3935 | -12 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3678 | 3667 | -11 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 143 | 143 | 0 | ➖ NO CHANGE |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 12 | 24 | +12 | ⚠️ MORE FAILURES |
| Inference Comparison | 269 | 268 | -1 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -12 fewer tests passing
- **Inference Comparison (PASS)**: -11 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| model--roberta_shared_bbc_xsum--patrickvonplaten | PASS | Numerics |
| migx_bench_bert-large-uncased_16_128 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_16_256 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_32_128 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_32_256 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_4_128 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_4_256 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_4_384 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_8_128 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_8_256 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_8_384 | PASS | compiled_inference |

**Total regressed models: 11**


---

