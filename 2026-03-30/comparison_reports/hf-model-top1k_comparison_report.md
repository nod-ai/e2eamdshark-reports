---
# Test Comparison Report

*Generated on: 2026-03-30*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-03-30/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-03-30/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 494 | 493 | -1 |
| IREE Compilation | 388 | 403 | +15 |
| Gold Inference | 386 | 401 | +15 |
| IREE Inference Invocation | 369 | 397 | +28 |
| Inference Comparison (PASS) | 369 | 381 | +12 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 13 | 14 | +1 |
| IREE Compilation | 106 | 90 | -16 |
| Gold Inference | 2 | 2 | 0 |
| IREE Inference Invocation | 17 | 4 | -13 |
| Inference Comparison | 0 | 16 | +16 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-03-28/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-03-30/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 494 | 494 | 0 | ➖ NO CHANGE |
| IREE Compilation | 388 | 388 | 0 | ➖ NO CHANGE |
| Gold Inference | 386 | 386 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 383 | 369 | -14 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 369 | 369 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 13 | 13 | 0 | ➖ NO CHANGE |
| IREE Compilation | 106 | 106 | 0 | ➖ NO CHANGE |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3 | 17 | +14 | ⚠️ MORE FAILURES |
| Inference Comparison | 14 | 0 | -14 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -14 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-03-28/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-03-30/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 403 | 403 | 0 | ➖ NO CHANGE |
| Gold Inference | 401 | 401 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 398 | 397 | -1 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 382 | 381 | -1 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 90 | 90 | 0 | ➖ NO CHANGE |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3 | 4 | +1 | ⚠️ MORE FAILURES |
| Inference Comparison | 16 | 16 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -1 fewer tests passing
- **Inference Comparison (PASS)**: -1 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_kda-albert-xxlarge-v2-race | PASS | compiled_inference |

**Total regressed models: 1**


---

