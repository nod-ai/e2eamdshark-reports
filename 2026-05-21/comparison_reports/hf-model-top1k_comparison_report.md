---
# Test Comparison Report

*Generated on: 2026-05-21*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-21/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-21/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 444 | 443 | -1 |
| IREE Compilation | 0 | 387 | +387 |
| Gold Inference | 0 | 371 | +371 |
| IREE Inference Invocation | 0 | 365 | +365 |
| Inference Comparison (PASS) | 0 | 347 | +347 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 63 | 64 | +1 |
| IREE Compilation | 444 | 56 | -388 |
| Gold Inference | 0 | 16 | +16 |
| IREE Inference Invocation | 0 | 6 | +6 |
| Inference Comparison | 0 | 18 | +18 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-20/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-21/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 444 | 444 | 0 | ➖ NO CHANGE |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 0 | 0 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 63 | 63 | 0 | ➖ NO CHANGE |
| IREE Compilation | 444 | 444 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison | 0 | 0 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-20/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-21/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 443 | 443 | 0 | ➖ NO CHANGE |
| IREE Compilation | 387 | 387 | 0 | ➖ NO CHANGE |
| Gold Inference | 371 | 371 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 366 | 365 | -1 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 348 | 347 | -1 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 64 | 64 | 0 | ➖ NO CHANGE |
| IREE Compilation | 56 | 56 | 0 | ➖ NO CHANGE |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 6 | +1 | ⚠️ MORE FAILURES |
| Inference Comparison | 18 | 18 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -1 fewer tests passing
- **Inference Comparison (PASS)**: -1 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_codebert-python | PASS | compiled_inference |

**Total regressed models: 1**


---

