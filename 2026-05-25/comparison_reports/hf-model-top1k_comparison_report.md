---
# Test Comparison Report

*Generated on: 2026-05-25*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-25/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-25/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 0 | 366 | +366 |
| Inference Comparison (PASS) | 0 | 348 | +348 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 63 | 64 | +1 |
| IREE Compilation | 444 | 56 | -388 |
| Gold Inference | 0 | 16 | +16 |
| IREE Inference Invocation | 0 | 5 | +5 |
| Inference Comparison | 0 | 18 | +18 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-23/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-25/hf-model-top1k/rocm/combined-reports_unique/summary.md`

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

**Previous Run:** `2026-05-23/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-25/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 442 | 443 | +1 | ✅ IMPROVED |
| IREE Compilation | 386 | 387 | +1 | ✅ IMPROVED |
| Gold Inference | 370 | 371 | +1 | ✅ IMPROVED |
| IREE Inference Invocation | 365 | 366 | +1 | ✅ IMPROVED |
| Inference Comparison (PASS) | 347 | 348 | +1 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 65 | 64 | -1 | ✅ FEWER FAILURES |
| IREE Compilation | 56 | 56 | 0 | ➖ NO CHANGE |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 5 | 0 | ➖ NO CHANGE |
| Inference Comparison | 18 | 18 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **Setup**: +1 more tests passing
- **IREE Compilation**: +1 more tests passing
- **Gold Inference**: +1 more tests passing
- **IREE Inference Invocation**: +1 more tests passing
- **Inference Comparison (PASS)**: +1 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_deit-base-patch16-224 | setup | PASS |

**Total improved models: 1**


---

