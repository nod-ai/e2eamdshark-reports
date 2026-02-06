---
# Test Comparison Report

*Generated on: 2026-02-06*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-06/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-06/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 507 | - |
| CPU | 507 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 1 | 493 | +492 |
| IREE Compilation | 1 | 403 | +402 |
| Gold Inference | 0 | 401 | +401 |
| IREE Inference Invocation | 0 | 397 | +397 |
| Inference Comparison (PASS) | 0 | 381 | +381 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 506 | 14 | -492 |
| IREE Compilation | 0 | 90 | +90 |
| Gold Inference | 1 | 2 | +1 |
| IREE Inference Invocation | 0 | 4 | +4 |
| Inference Comparison | 0 | 16 | +16 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-05/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-06/hf-model-top1k/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 507 | - |
| Current | 507 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Compilation | 1 | 1 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 0 | 0 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 506 | 506 | 0 | ➖ NO CHANGE |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison | 0 | 0 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-05/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-06/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| Inference Comparison (PASS) | 366 | 381 | +15 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 90 | 90 | 0 | ➖ NO CHANGE |
| Gold Inference | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 4 | 4 | 0 | ➖ NO CHANGE |
| Inference Comparison | 31 | 16 | -15 | ✅ FEWER FAILURES |

## Summary

### ✅ Improvements

- **Inference Comparison (PASS)**: +15 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_densenet121.ra_in1k | Numerics | PASS |
| hf_ese_vovnet19b_dw.ra_in1k | Numerics | PASS |
| hf_inception_resnet_v2.tf_in1k | Numerics | PASS |
| hf_inception_v3.tf_adv_in1k | Numerics | PASS |
| hf_inception_v3.tv_in1k | Numerics | PASS |
| hf_resnet-18 | Numerics | PASS |
| hf_resnet-50 | Numerics | PASS |
| hf_resnet101.a1h_in1k | Numerics | PASS |
| hf_resnet18.a1_in1k | Numerics | PASS |
| hf_resnet34.a1_in1k | Numerics | PASS |
| hf_resnet50.a1_in1k | Numerics | PASS |
| hf_resnext50_32x4d.fb_swsl_ig1b_ft_in1k | Numerics | PASS |
| hf_vgg16.tv_in1k | Numerics | PASS |
| hf_vgg19.tv_in1k | Numerics | PASS |
| hf_wide_resnet50_2.racm_in1k | Numerics | PASS |

**Total improved models: 15**


---

