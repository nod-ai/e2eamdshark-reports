---
# Test Comparison Report

*Generated on: 2026-04-11*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-04-11/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-04-11/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 493 | 491 | -2 |
| IREE Compilation | 404 | 390 | -14 |
| Gold Inference | 401 | 387 | -14 |
| IREE Inference Invocation | 398 | 382 | -16 |
| Inference Comparison (PASS) | 382 | 380 | -2 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 14 | 16 | +2 |
| IREE Compilation | 89 | 101 | +12 |
| Gold Inference | 3 | 3 | 0 |
| IREE Inference Invocation | 3 | 5 | +2 |
| Inference Comparison | 16 | 2 | -14 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-04-10/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-04-11/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 404 | 404 | 0 | ➖ NO CHANGE |
| Gold Inference | 401 | 401 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 398 | 398 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 382 | 382 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 89 | 89 | 0 | ➖ NO CHANGE |
| Gold Inference | 3 | 3 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3 | 3 | 0 | ➖ NO CHANGE |
| Inference Comparison | 16 | 16 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-04-10/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-04-11/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 492 | 491 | -1 | ⚠️ REGRESSION |
| IREE Compilation | 390 | 390 | 0 | ➖ NO CHANGE |
| Gold Inference | 387 | 387 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 382 | 382 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 380 | 380 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 15 | 16 | +1 | ⚠️ MORE FAILURES |
| IREE Compilation | 102 | 101 | -1 | ✅ FEWER FAILURES |
| Gold Inference | 3 | 3 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 5 | 0 | ➖ NO CHANGE |
| Inference Comparison | 2 | 2 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -1 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED


---

