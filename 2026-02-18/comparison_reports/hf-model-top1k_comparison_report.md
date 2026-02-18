---
# Test Comparison Report

*Generated on: 2026-02-18*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-18/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-18/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 494 | 493 | -1 |
| IREE Compilation | 398 | 403 | +5 |
| Gold Inference | 396 | 401 | +5 |
| IREE Inference Invocation | 394 | 397 | +3 |
| Inference Comparison (PASS) | 380 | 366 | -14 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 13 | 14 | +1 |
| IREE Compilation | 96 | 90 | -6 |
| Gold Inference | 2 | 2 | 0 |
| IREE Inference Invocation | 2 | 4 | +2 |
| Inference Comparison | 14 | 31 | +17 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-17/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-18/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 494 | 494 | 0 | ➖ NO CHANGE |
| IREE Compilation | 398 | 398 | 0 | ➖ NO CHANGE |
| Gold Inference | 396 | 396 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 394 | 394 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 380 | 380 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 13 | 13 | 0 | ➖ NO CHANGE |
| IREE Compilation | 96 | 96 | 0 | ➖ NO CHANGE |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 2 | 2 | 0 | ➖ NO CHANGE |
| Inference Comparison | 14 | 14 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-17/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-18/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 397 | 397 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 366 | 366 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 90 | 90 | 0 | ➖ NO CHANGE |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 4 | 4 | 0 | ➖ NO CHANGE |
| Inference Comparison | 31 | 31 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

