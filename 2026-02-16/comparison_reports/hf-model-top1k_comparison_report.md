---
# Test Comparison Report

*Generated on: 2026-02-16*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-16/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-16/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 494 | 493 | -1 |
| IREE Compilation | 398 | 401 | +3 |
| Gold Inference | 396 | 399 | +3 |
| IREE Inference Invocation | 394 | 396 | +2 |
| Inference Comparison (PASS) | 380 | 365 | -15 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 13 | 14 | +1 |
| IREE Compilation | 96 | 92 | -4 |
| Gold Inference | 2 | 2 | 0 |
| IREE Inference Invocation | 2 | 3 | +1 |
| Inference Comparison | 14 | 31 | +17 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-12/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-16/hf-model-top1k/rocm/combined-reports_unique/summary.md`

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

**Previous Run:** `2026-02-12/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-16/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 493 | 493 | 0 | ➖ NO CHANGE |
| IREE Compilation | 403 | 401 | -2 | ⚠️ REGRESSION |
| Gold Inference | 401 | 399 | -2 | ⚠️ REGRESSION |
| IREE Inference Invocation | 397 | 396 | -1 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 381 | 365 | -16 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 90 | 92 | +2 | ⚠️ MORE FAILURES |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 4 | 3 | -1 | ✅ FEWER FAILURES |
| Inference Comparison | 16 | 31 | +15 | ⚠️ MORE FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -2 fewer tests passing
- **Gold Inference**: -2 fewer tests passing
- **IREE Inference Invocation**: -1 fewer tests passing
- **Inference Comparison (PASS)**: -16 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_beit_base_patch16_224.in22k_ft_in22k_in1k | PASS | compilation |
| hf_beitv2_base_patch16_224.in1k_ft_in22k | PASS | compilation |
| hf_densenet121.ra_in1k | PASS | Numerics |
| hf_ese_vovnet19b_dw.ra_in1k | PASS | Numerics |
| hf_inception_resnet_v2.tf_in1k | PASS | Numerics |
| hf_inception_v3.tf_adv_in1k | PASS | Numerics |
| hf_inception_v3.tv_in1k | PASS | Numerics |
| hf_resnet-18 | PASS | Numerics |
| hf_resnet-50 | PASS | Numerics |
| hf_resnet101.a1h_in1k | PASS | Numerics |
| hf_resnet18.a1_in1k | PASS | Numerics |
| hf_resnet34.a1_in1k | PASS | Numerics |
| hf_resnet50.a1_in1k | PASS | Numerics |
| hf_resnext50_32x4d.fb_swsl_ig1b_ft_in1k | PASS | Numerics |
| hf_vgg16.tv_in1k | PASS | Numerics |
| hf_vgg19.tv_in1k | PASS | Numerics |
| hf_wide_resnet50_2.racm_in1k | PASS | Numerics |

**Total regressed models: 17**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_kda-albert-xxlarge-v2-race | compiled_inference | PASS |

**Total improved models: 1**


---

