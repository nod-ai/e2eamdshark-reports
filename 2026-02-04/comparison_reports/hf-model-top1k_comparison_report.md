---
# Test Comparison Report

*Generated on: 2026-02-04*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-04/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-04/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 394 | 398 | +4 |
| Inference Comparison (PASS) | 380 | 367 | -13 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 13 | 14 | +1 |
| IREE Compilation | 96 | 90 | -6 |
| Gold Inference | 2 | 2 | 0 |
| IREE Inference Invocation | 2 | 3 | +1 |
| Inference Comparison | 14 | 31 | +17 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-03/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-04/hf-model-top1k/rocm/combined-reports_unique/summary.md`

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
| Inference Comparison (PASS) | 375 | 380 | +5 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 13 | 13 | 0 | ➖ NO CHANGE |
| IREE Compilation | 96 | 96 | 0 | ➖ NO CHANGE |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 2 | 2 | 0 | ➖ NO CHANGE |
| Inference Comparison | 19 | 14 | -5 | ✅ FEWER FAILURES |

## Summary

### ✅ Improvements

- **Inference Comparison (PASS)**: +5 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_efficientnet_b0.ra_in1k | Numerics | PASS |
| hf_efficientnet_b3.ra2_in1k | Numerics | PASS |
| hf_efficientnet_b4.ra2_in1k | Numerics | PASS |
| hf_resnet50.a1_in1k | Numerics | PASS |
| hf_tf_efficientnet_b0.ns_jft_in1k | Numerics | PASS |

**Total improved models: 5**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-03/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-04/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 397 | 398 | +1 | ✅ IMPROVED |
| Inference Comparison (PASS) | 381 | 367 | -14 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 90 | 90 | 0 | ➖ NO CHANGE |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 4 | 3 | -1 | ✅ FEWER FAILURES |
| Inference Comparison | 16 | 31 | +15 | ⚠️ MORE FAILURES |

## Summary

### ⚠️ Regressions Detected

- **Inference Comparison (PASS)**: -14 fewer tests passing

### ✅ Improvements

- **IREE Inference Invocation**: +1 more tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
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

**Total regressed models: 15**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_kda-albert-xxlarge-v2-race | compiled_inference | PASS |

**Total improved models: 1**


---

