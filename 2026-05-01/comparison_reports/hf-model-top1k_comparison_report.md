---
# Test Comparison Report

*Generated on: 2026-05-01*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-01/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-01/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| Gold Inference | 418 | 404 | -14 |
| IREE Inference Invocation | 352 | 399 | +47 |
| Inference Comparison (PASS) | 336 | 397 | +61 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 14 | 15 | +1 |
| IREE Compilation | 59 | 72 | +13 |
| Gold Inference | 16 | 16 | 0 |
| IREE Inference Invocation | 66 | 5 | -61 |
| Inference Comparison | 16 | 2 | -14 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-04-30/hf-model-top1k/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-01/hf-model-top1k/rocm/combined-reports_unique/summary.md`

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
| Gold Inference | 418 | 418 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 415 | 352 | -63 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 399 | 336 | -63 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 14 | 14 | 0 | ➖ NO CHANGE |
| IREE Compilation | 59 | 59 | 0 | ➖ NO CHANGE |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3 | 66 | +63 | ⚠️ MORE FAILURES |
| Inference Comparison | 16 | 16 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -63 fewer tests passing
- **Inference Comparison (PASS)**: -63 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| hf_UL_base_classification | PASS | compiled_inference |
| hf_beit-base-patch16-224-pt22k | PASS | compiled_inference |
| hf_beit-base-patch16-224-pt22k-ft22k | PASS | compiled_inference |
| hf_beit_base_patch16_224.in22k_ft_in22k_in1k | PASS | compiled_inference |
| hf_beitv2_base_patch16_224.in1k_ft_in22k | PASS | compiled_inference |
| hf_convnext_base.fb_in22k_ft_in1k | PASS | compiled_inference |
| hf_convnext_large_mlp.clip_laion2b_soup_ft_in12k_in1k_320 | PASS | compiled_inference |
| hf_convnextv2_base.fcmae_ft_in22k_in1k | PASS | compiled_inference |
| hf_cspdarknet53.ra_in1k | PASS | compiled_inference |
| hf_deit-base-patch16-224 | PASS | compiled_inference |
| hf_deit-tiny-patch16-224 | PASS | compiled_inference |
| hf_deit_base_distilled_patch16_224.fb_in1k | PASS | compiled_inference |
| hf_densenet121.ra_in1k | PASS | compiled_inference |
| hf_efficientnet_b0.ra_in1k | PASS | compiled_inference |
| hf_efficientnet_b3.ra2_in1k | PASS | compiled_inference |
| hf_efficientnet_b4.ra2_in1k | PASS | compiled_inference |
| hf_ese_vovnet19b_dw.ra_in1k | PASS | compiled_inference |
| hf_gender-classification | PASS | compiled_inference |
| hf_hrnet_w18.ms_aug_in1k | PASS | compiled_inference |
| hf_inception_resnet_v2.tf_in1k | PASS | compiled_inference |
| hf_inception_v3.tf_adv_in1k | PASS | compiled_inference |
| hf_inception_v3.tv_in1k | PASS | compiled_inference |
| hf_lcnet_050.ra2_in1k | PASS | compiled_inference |
| hf_mit-b0 | PASS | compiled_inference |
| hf_mit-b5 | PASS | compiled_inference |
| hf_mobilenet_v2_1.0_224 | PASS | compiled_inference |
| hf_mobilenetv2_100.ra_in1k | PASS | compiled_inference |
| hf_mobilenetv3_large_100.miil_in21k_ft_in1k | PASS | compiled_inference |
| hf_mobilenetv3_large_100.ra_in1k | PASS | compiled_inference |
| hf_nfnet_l0.ra2_in1k | PASS | compiled_inference |
| hf_nsfw-classifier | PASS | compiled_inference |
| hf_nsfw_image_detection | PASS | compiled_inference |
| hf_pedestrian_gender_recognition | PASS | compiled_inference |
| hf_regnety_002.pycls_in1k | PASS | compiled_inference |
| hf_resnet-18 | PASS | compiled_inference |
| hf_resnet-50 | PASS | compiled_inference |
| hf_resnet101.a1h_in1k | PASS | compiled_inference |
| hf_resnet18.a1_in1k | PASS | compiled_inference |
| hf_resnet34.a1_in1k | PASS | compiled_inference |
| hf_resnet50.a1_in1k | PASS | compiled_inference |
| hf_resnext50_32x4d.fb_swsl_ig1b_ft_in1k | PASS | compiled_inference |
| hf_tf_efficientnet_b0.ns_jft_in1k | PASS | compiled_inference |
| hf_tf_efficientnetv2_s.in21k | PASS | compiled_inference |
| hf_tf_mobilenetv3_large_minimal_100.in1k | PASS | compiled_inference |
| hf_tf_mobilenetv3_small_minimal_100.in1k | PASS | compiled_inference |
| hf_vgg16.tv_in1k | PASS | compiled_inference |
| hf_vgg19.tv_in1k | PASS | compiled_inference |
| hf_vit-age-classifier | PASS | compiled_inference |
| hf_vit-base-patch16-224 | PASS | compiled_inference |
| hf_vit-base-uppercase-english-characters | PASS | compiled_inference |

*... and 13 more regressed models*

**Total regressed models: 63**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-04-30/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-01/hf-model-top1k/llvm-cpu/combined-reports_unique/summary.md`

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
| Gold Inference | 404 | 404 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 399 | 399 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 397 | 397 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 15 | 15 | 0 | ➖ NO CHANGE |
| IREE Compilation | 72 | 72 | 0 | ➖ NO CHANGE |
| Gold Inference | 16 | 16 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 5 | 0 | ➖ NO CHANGE |
| Inference Comparison | 2 | 2 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

