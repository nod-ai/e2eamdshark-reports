---
# Test Comparison Report

*Generated on: 2026-05-24*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-24/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-05-24/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 2358 | 1987 | -371 |
| IREE Compilation | 0 | 1941 | +1941 |
| Gold Inference | 0 | 1941 | +1941 |
| IREE Inference Invocation | 0 | 1940 | +1940 |
| Inference Comparison (PASS) | 0 | 1915 | +1915 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 3 | 374 | +371 |
| IREE Compilation | 2358 | 46 | -2312 |
| Gold Inference | 0 | 0 | 0 |
| IREE Inference Invocation | 0 | 1 | +1 |
| Inference Comparison | 0 | 25 | +25 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-17/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**Current Run:** `2026-05-24/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 2359 | 2358 | -1 | ⚠️ REGRESSION |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 0 | 0 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 2 | 3 | +1 | ⚠️ MORE FAILURES |
| IREE Compilation | 2359 | 2358 | -1 | ✅ FEWER FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison | 0 | 0 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -1 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-17/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`
**Current Run:** `2026-05-24/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 1987 | 1987 | 0 | ➖ NO CHANGE |
| IREE Compilation | 1941 | 1941 | 0 | ➖ NO CHANGE |
| Gold Inference | 1941 | 1941 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 1940 | 1940 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 1915 | 1915 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 374 | 374 | 0 | ➖ NO CHANGE |
| IREE Compilation | 46 | 46 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 1 | 1 | 0 | ➖ NO CHANGE |
| Inference Comparison | 25 | 25 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

