---
# Test Comparison Report

*Generated on: 2026-04-09*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-04-09/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-04-09/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 494 | 493 | -1 |
| IREE Compilation | 405 | 407 | +2 |
| Gold Inference | 402 | 404 | +2 |
| IREE Inference Invocation | 399 | 399 | 0 |
| Inference Comparison (PASS) | 383 | 381 | -2 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 13 | 14 | +1 |
| IREE Compilation | 89 | 86 | -3 |
| Gold Inference | 3 | 3 | 0 |
| IREE Inference Invocation | 3 | 5 | +2 |
| Inference Comparison | 16 | 18 | +2 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-04-08/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-04-09/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 494 | 494 | 0 | ➖ NO CHANGE |
| IREE Compilation | 399 | 405 | +6 | ✅ IMPROVED |
| Gold Inference | 397 | 402 | +5 | ✅ IMPROVED |
| IREE Inference Invocation | 394 | 399 | +5 | ✅ IMPROVED |
| Inference Comparison (PASS) | 380 | 383 | +3 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 13 | 13 | 0 | ➖ NO CHANGE |
| IREE Compilation | 95 | 89 | -6 | ✅ FEWER FAILURES |
| Gold Inference | 2 | 3 | +1 | ⚠️ MORE FAILURES |
| IREE Inference Invocation | 3 | 3 | 0 | ➖ NO CHANGE |
| Inference Comparison | 14 | 16 | +2 | ⚠️ MORE FAILURES |

## Summary

### ✅ Improvements

- **IREE Compilation**: +6 more tests passing
- **Gold Inference**: +5 more tests passing
- **IREE Inference Invocation**: +5 more tests passing
- **Inference Comparison (PASS)**: +3 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_convnext_base.fb_in22k_ft_in1k | compilation | PASS |
| hf_convnext_large_mlp.clip_laion2b_soup_ft_in12k_in1k_320 | compilation | PASS |
| hf_convnextv2_base.fcmae_ft_in22k_in1k | compilation | PASS |

**Total improved models: 3**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-04-08/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-04-09/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 403 | 407 | +4 | ✅ IMPROVED |
| Gold Inference | 401 | 404 | +3 | ✅ IMPROVED |
| IREE Inference Invocation | 397 | 399 | +2 | ✅ IMPROVED |
| Inference Comparison (PASS) | 381 | 381 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 90 | 86 | -4 | ✅ FEWER FAILURES |
| Gold Inference | 2 | 3 | +1 | ⚠️ MORE FAILURES |
| IREE Inference Invocation | 4 | 5 | +1 | ⚠️ MORE FAILURES |
| Inference Comparison | 16 | 18 | +2 | ⚠️ MORE FAILURES |

## Summary

### ✅ Improvements

- **IREE Compilation**: +4 more tests passing
- **Gold Inference**: +3 more tests passing
- **IREE Inference Invocation**: +2 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED


---

