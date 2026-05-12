---
# Test Comparison Report

*Generated on: 2026-05-12*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-12/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-12/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 493 | 492 | -1 |
| IREE Compilation | 0 | 422 | +422 |
| Gold Inference | 0 | 406 | +406 |
| IREE Inference Invocation | 0 | 402 | +402 |
| Inference Comparison (PASS) | 0 | 388 | +388 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 14 | 15 | +1 |
| IREE Compilation | 493 | 70 | -423 |
| Gold Inference | 0 | 16 | +16 |
| IREE Inference Invocation | 0 | 4 | +4 |
| Inference Comparison | 0 | 14 | +14 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-11/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-12/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 0 | 0 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 493 | 493 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison | 0 | 0 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-11/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-12/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 492 | 492 | 0 | ➖ NO CHANGE |
| IREE Compilation | 422 | 422 | 0 | ➖ NO CHANGE |
| Gold Inference | 406 | 406 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 401 | 402 | +1 | ✅ IMPROVED |
| Inference Comparison (PASS) | 387 | 388 | +1 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 15 | 15 | 0 | ➖ NO CHANGE |
| IREE Compilation | 70 | 70 | 0 | ➖ NO CHANGE |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 4 | -1 | ✅ FEWER FAILURES |
| Inference Comparison | 14 | 14 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Inference Invocation**: +1 more tests passing
- **Inference Comparison (PASS)**: +1 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_kda-albert-xxlarge-v2-race | compiled_inference | PASS |

**Total improved models: 1**


---

