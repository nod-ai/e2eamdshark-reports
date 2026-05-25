---
# Test Comparison Report

*Generated on: 2026-05-25*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-25/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-25/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4102 | 4103 | +1 |
| IREE Compilation | 0 | 3960 | +3960 |
| Gold Inference | 0 | 3959 | +3959 |
| IREE Inference Invocation | 0 | 3947 | +3947 |
| Inference Comparison (PASS) | 0 | 3678 | +3678 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 5 | 4 | -1 |
| IREE Compilation | 4102 | 143 | -3959 |
| Gold Inference | 0 | 1 | +1 |
| IREE Inference Invocation | 0 | 12 | +12 |
| Inference Comparison | 0 | 269 | +269 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-23/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-25/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4102 | -1 | ⚠️ REGRESSION |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 0 | 0 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 5 | +1 | ⚠️ MORE FAILURES |
| IREE Compilation | 4103 | 4102 | -1 | ✅ FEWER FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison | 0 | 0 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -1 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-23/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-25/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 3935 | 3947 | +12 | ✅ IMPROVED |
| Inference Comparison (PASS) | 3667 | 3678 | +11 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 143 | 143 | 0 | ➖ NO CHANGE |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 24 | 12 | -12 | ✅ FEWER FAILURES |
| Inference Comparison | 268 | 269 | +1 | ⚠️ MORE FAILURES |

## Summary

### ✅ Improvements

- **IREE Inference Invocation**: +12 more tests passing
- **Inference Comparison (PASS)**: +11 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| model--roberta_shared_bbc_xsum--patrickvonplaten | Numerics | PASS |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_32_128 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_32_256 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_4_128 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_4_256 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_4_384 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_8_128 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_8_256 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_8_384 | compiled_inference | PASS |

**Total improved models: 11**


---

