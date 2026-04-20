---
# Test Comparison Report

*Generated on: 2026-04-20*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-04-20/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-04-20/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 493 | 492 | -1 |
| IREE Compilation | 434 | 420 | -14 |
| Gold Inference | 431 | 417 | -14 |
| IREE Inference Invocation | 428 | 412 | -16 |
| Inference Comparison (PASS) | 412 | 410 | -2 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 14 | 15 | +1 |
| IREE Compilation | 59 | 72 | +13 |
| Gold Inference | 3 | 3 | 0 |
| IREE Inference Invocation | 3 | 5 | +2 |
| Inference Comparison | 16 | 2 | -14 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-04-18/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-04-20/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 434 | 434 | 0 | ➖ NO CHANGE |
| Gold Inference | 431 | 431 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 428 | 428 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 412 | 412 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 59 | 59 | 0 | ➖ NO CHANGE |
| Gold Inference | 3 | 3 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3 | 3 | 0 | ➖ NO CHANGE |
| Inference Comparison | 16 | 16 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-04-18/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-04-20/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 492 | 492 | 0 | ➖ NO CHANGE |
| IREE Compilation | 420 | 420 | 0 | ➖ NO CHANGE |
| Gold Inference | 417 | 417 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 412 | 412 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 410 | 410 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 15 | 15 | 0 | ➖ NO CHANGE |
| IREE Compilation | 72 | 72 | 0 | ➖ NO CHANGE |
| Gold Inference | 3 | 3 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 5 | 0 | ➖ NO CHANGE |
| Inference Comparison | 2 | 2 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

