---
# Test Comparison Report

*Generated on: 2026-05-14*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-14/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-14/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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

**Previous Run:** `2026-05-13/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-14/hf-model-top1k/rocm/combined-reports_unique/summary.md`

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

**Previous Run:** `2026-05-13/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-14/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 443 | 443 | 0 | ➖ NO CHANGE |
| IREE Compilation | 373 | 387 | +14 | ✅ IMPROVED |
| Gold Inference | 357 | 371 | +14 | ✅ IMPROVED |
| IREE Inference Invocation | 353 | 366 | +13 | ✅ IMPROVED |
| Inference Comparison (PASS) | 339 | 348 | +9 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 64 | 64 | 0 | ➖ NO CHANGE |
| IREE Compilation | 70 | 56 | -14 | ✅ FEWER FAILURES |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 4 | 5 | +1 | ⚠️ MORE FAILURES |
| Inference Comparison | 14 | 18 | +4 | ⚠️ MORE FAILURES |

## Summary

### ✅ Improvements

- **IREE Compilation**: +14 more tests passing
- **Gold Inference**: +14 more tests passing
- **IREE Inference Invocation**: +13 more tests passing
- **Inference Comparison (PASS)**: +9 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_kda-albert-xxlarge-v2-race | PASS | compiled_inference |

**Total regressed models: 1**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_beit-base-patch16-224-pt22k | compilation | PASS |
| hf_beit-base-patch16-224-pt22k-ft22k | compilation | PASS |
| hf_beit_base_patch16_224.in22k_ft_in22k_in1k | compilation | PASS |
| hf_beitv2_base_patch16_224.in1k_ft_in22k | compilation | PASS |
| hf_cspdarknet53.ra_in1k | compilation | PASS |
| hf_densenet121.ra_in1k | compilation | PASS |
| hf_inception_resnet_v2.tf_in1k | compilation | PASS |
| hf_inception_v3.tf_adv_in1k | compilation | PASS |
| hf_inception_v3.tv_in1k | compilation | PASS |
| hf_pedestrian_gender_recognition | compilation | PASS |

**Total improved models: 10**


---

