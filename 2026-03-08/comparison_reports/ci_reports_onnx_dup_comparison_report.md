---
# Test Comparison Report

*Generated on: 2026-03-08*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-03-08/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-03-08/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 2360 | 1987 | -373 |
| IREE Compilation | 2189 | 1942 | -247 |
| Gold Inference | 2189 | 1942 | -247 |
| IREE Inference Invocation | 2182 | 1937 | -245 |
| Inference Comparison (PASS) | 2163 | 1903 | -260 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 1 | 374 | +373 |
| IREE Compilation | 171 | 45 | -126 |
| Gold Inference | 0 | 0 | 0 |
| IREE Inference Invocation | 7 | 5 | -2 |
| Inference Comparison | 19 | 34 | +15 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-03-01/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**Current Run:** `2026-03-08/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 2359 | 2360 | +1 | ✅ IMPROVED |
| IREE Compilation | 2131 | 2189 | +58 | ✅ IMPROVED |
| Gold Inference | 2131 | 2189 | +58 | ✅ IMPROVED |
| IREE Inference Invocation | 2130 | 2182 | +52 | ✅ IMPROVED |
| Inference Comparison (PASS) | 2111 | 2163 | +52 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 2 | 1 | -1 | ✅ FEWER FAILURES |
| IREE Compilation | 228 | 171 | -57 | ✅ FEWER FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 1 | 7 | +6 | ⚠️ MORE FAILURES |
| Inference Comparison | 19 | 19 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **Setup**: +1 more tests passing
- **IREE Compilation**: +58 more tests passing
- **Gold Inference**: +58 more tests passing
- **IREE Inference Invocation**: +52 more tests passing
- **Inference Comparison (PASS)**: +52 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| gluon_resnet101_v1b_vaiq | PASS | compilation |
| gluon_resnet152_v1b_vaiq | PASS | compilation |
| gluon_resnet34_v1b_vaiq | PASS | compilation |
| gluon_resnet50_v1b_vaiq | PASS | compilation |
| gluon_resnext50_32x4d_vaiq | PASS | compilation |
| ig_resnext101_32x32d_vaiq | PASS | compilation |
| ig_resnext101_32x8d_vaiq | PASS | compilation |
| resnet101_vaiq | PASS | compilation |
| resnet152_vaiq | PASS | compilation |
| resnet18_vaiq | PASS | compilation |
| resnet34_vaiq | PASS | compilation |
| resnet50_vaiq | PASS | compilation |
| resnext101_32x8d_vaiq | PASS | compilation |
| resnext50_32x4d_vaiq | PASS | compilation |
| seresnext50_32x4d_vaiq | PASS | compilation |
| ssl_resnet18_vaiq | PASS | compilation |
| ssl_resnet50_vaiq | PASS | compilation |
| ssl_resnext101_32x4d_vaiq | PASS | compilation |
| ssl_resnext101_32x8d_vaiq | PASS | compilation |
| ssl_resnext50_32x4d_vaiq | PASS | compilation |
| swsl_resnet18_vaiq | PASS | compilation |
| swsl_resnet50_vaiq | PASS | compilation |
| swsl_resnext101_32x16d_vaiq | PASS | compilation |
| swsl_resnext101_32x4d_vaiq | PASS | compilation |
| swsl_resnext101_32x8d_vaiq | PASS | compilation |
| swsl_resnext50_32x4d_vaiq | PASS | compilation |
| xception_vaiq | PASS | compilation |
| model--bart-base-cnn--ainize | PASS | compiled_inference |
| model--bart-base-samsum--philschmid | PASS | compiled_inference |
| model--bart-base-xsum--harouzie | PASS | compiled_inference |
| model--bart-base-xsum--morenolq | PASS | compiled_inference |
| model--bart-german--Shahm | PASS | compiled_inference |
| model--bart_lfqa_sqaud--Shubham09 | PASS | compiled_inference |
| resnetv2_101_Opset17_timm | PASS | setup |

**Total regressed models: 34**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| swinv2_base_window16_256.ms_in1k | compilation | PASS |
| xcit_large_24_p16_224_dist | compilation | PASS |
| xcit_large_24_p8_224_dist | compilation | PASS |
| xcit_medium_24_p16_224_dist | compilation | PASS |
| xcit_nano_12_p16_224_dist | compilation | PASS |
| xcit_nano_12_p8_224_dist | compilation | PASS |
| xcit_small_12_p16_224_dist | compilation | PASS |
| xcit_small_12_p8_224_dist | compilation | PASS |
| xcit_small_24_p16_224_dist | compilation | PASS |
| xcit_small_24_p8_224_dist | compilation | PASS |
| xcit_tiny_12_p16_224_dist | compilation | PASS |
| xcit_tiny_12_p8_224_dist | compilation | PASS |
| xcit_tiny_24_p16_224_dist | compilation | PASS |
| xcit_tiny_24_p8_224_dist | compilation | PASS |
| cait_m36_384_Opset18_timm | compilation | PASS |
| cait_s24_384_Opset17_timm | compilation | PASS |
| cait_s36_384_Opset18_timm | compilation | PASS |
| cait_xxs24_384_Opset17_timm | compilation | PASS |
| cait_xxs36_384_Opset17_timm | compilation | PASS |
| convnext_base_Opset17_timm | compilation | PASS |
| convnext_base_Opset18_timm | compilation | PASS |
| convnext_base_Opset18_torch_hub | compilation | PASS |
| convnext_base_in22ft1k_Opset18_timm | compilation | PASS |
| convnext_base_in22k_Opset18_timm | compilation | PASS |
| convnext_nano_Opset18_timm | compilation | PASS |
| convnext_nano_ols_Opset17_timm | compilation | PASS |
| convnext_small_Opset18_timm | compilation | PASS |
| convnext_small_in22ft1k_Opset17_timm | compilation | PASS |
| convnext_small_in22ft1k_Opset18_timm | compilation | PASS |
| convnext_small_in22k_Opset18_timm | compilation | PASS |
| convnext_tiny_Opset17_timm | compilation | PASS |
| convnext_tiny_Opset17_torch_hub | compilation | PASS |
| convnext_tiny_Opset18_timm | compilation | PASS |
| convnext_tiny_hnf_Opset17_timm | compilation | PASS |
| convnext_tiny_in22ft1k_Opset17_timm | compilation | PASS |
| convnext_tiny_in22k_Opset18_timm | compilation | PASS |
| edgenext_x_small_Opset18_timm | compilation | PASS |
| mobilevit_s_Opset17_timm | compilation | PASS |
| mobilevit_xxs_Opset17_timm | compilation | PASS |
| mobilevitv2_125_Opset17_timm | setup | PASS |
| resnext101_32x4d_Opset16_timm | setup | PASS |
| xcit_large_24_p16_224_Opset18_timm | compilation | PASS |
| xcit_large_24_p16_224_dist_Opset17_timm | compilation | PASS |
| xcit_large_24_p16_224_dist_Opset18_timm | compilation | PASS |
| xcit_large_24_p16_384_dist_Opset18_timm | compilation | PASS |
| xcit_large_24_p8_224_Opset18_timm | compilation | PASS |
| xcit_large_24_p8_224_dist_Opset17_timm | compilation | PASS |
| xcit_large_24_p8_224_dist_Opset18_timm | compilation | PASS |
| xcit_medium_24_p16_224_Opset17_timm | compilation | PASS |
| xcit_medium_24_p16_224_dist_Opset17_timm | compilation | PASS |

*... and 36 more improved models*

**Total improved models: 86**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-03-01/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`
**Current Run:** `2026-03-08/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 1987 | 1987 | 0 | ➖ NO CHANGE |
| IREE Compilation | 1942 | 1942 | 0 | ➖ NO CHANGE |
| Gold Inference | 1942 | 1942 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 1937 | 1937 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 1903 | 1903 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 374 | 374 | 0 | ➖ NO CHANGE |
| IREE Compilation | 45 | 45 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 5 | 0 | ➖ NO CHANGE |
| Inference Comparison | 34 | 34 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge.fb_in22k_ft_in1k_384 | PASS | compiled_inference |
| deit3_large_patch16_384.fb_in22k_ft_in1k | PASS | compiled_inference |
| vit_large_patch14_clip_336.laion2b_ft_in1k | PASS | compiled_inference |
| vit_large_patch14_clip_336.openai_ft_in12k_in1k | PASS | compiled_inference |

**Total regressed models: 4**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge_384_in22ft1k_Opset18_timm | compiled_inference | PASS |
| deit3_large_patch16_384_Opset17_timm | compiled_inference | PASS |
| deit3_large_patch16_384_in21ft1k_Opset16_timm | compiled_inference | PASS |
| vit_large_patch16_384_Opset18_timm | compiled_inference | PASS |

**Total improved models: 4**


---

