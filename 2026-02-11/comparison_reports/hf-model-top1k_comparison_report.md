---
# Test Comparison Report

*Generated on: 2026-02-11*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-11/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-11/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| Inference Comparison (PASS) | 380 | 381 | +1 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 13 | 14 | +1 |
| IREE Compilation | 96 | 90 | -6 |
| Gold Inference | 2 | 2 | 0 |
| IREE Inference Invocation | 2 | 4 | +2 |
| Inference Comparison | 14 | 16 | +2 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-10/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-11/hf-model-top1k/rocm/combined-reports_unique/summary.md`

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

**Previous Run:** `2026-02-10/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-11/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 401 | 403 | +2 | ✅ IMPROVED |
| Gold Inference | 399 | 401 | +2 | ✅ IMPROVED |
| IREE Inference Invocation | 395 | 397 | +2 | ✅ IMPROVED |
| Inference Comparison (PASS) | 379 | 381 | +2 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 92 | 90 | -2 | ✅ FEWER FAILURES |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 4 | 4 | 0 | ➖ NO CHANGE |
| Inference Comparison | 16 | 16 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Compilation**: +2 more tests passing
- **Gold Inference**: +2 more tests passing
- **IREE Inference Invocation**: +2 more tests passing
- **Inference Comparison (PASS)**: +2 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_beit_base_patch16_224.in22k_ft_in22k_in1k | compilation | PASS |
| hf_beitv2_base_patch16_224.in1k_ft_in22k | compilation | PASS |

**Total improved models: 2**


---

