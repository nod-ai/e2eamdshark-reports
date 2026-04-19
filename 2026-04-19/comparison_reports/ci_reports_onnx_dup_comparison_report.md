---
# Test Comparison Report

*Generated on: 2026-04-19*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-04-19/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-04-19/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 2359 | 1987 | -372 |
| IREE Compilation | 2274 | 1945 | -329 |
| Gold Inference | 2274 | 1945 | -329 |
| IREE Inference Invocation | 2273 | 1944 | -329 |
| Inference Comparison (PASS) | 2247 | 1913 | -334 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 2 | 374 | +372 |
| IREE Compilation | 85 | 42 | -43 |
| Gold Inference | 0 | 0 | 0 |
| IREE Inference Invocation | 1 | 1 | 0 |
| Inference Comparison | 26 | 31 | +5 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-04-12/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**Current Run:** `2026-04-19/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 2359 | 2359 | 0 | ➖ NO CHANGE |
| IREE Compilation | 2262 | 2274 | +12 | ✅ IMPROVED |
| Gold Inference | 2262 | 2274 | +12 | ✅ IMPROVED |
| IREE Inference Invocation | 2261 | 2273 | +12 | ✅ IMPROVED |
| Inference Comparison (PASS) | 2235 | 2247 | +12 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Compilation | 97 | 85 | -12 | ✅ FEWER FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 1 | 1 | 0 | ➖ NO CHANGE |
| Inference Comparison | 26 | 26 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Compilation**: +12 more tests passing
- **Gold Inference**: +12 more tests passing
- **IREE Inference Invocation**: +12 more tests passing
- **Inference Comparison (PASS)**: +12 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| resmlp_12_224.fb_in1k_vaiq | PASS | compilation |
| resmlp_24_224.fb_in1k_vaiq | PASS | compilation |
| resmlp_36_224.fb_in1k_vaiq | PASS | compilation |
| maxvit_base_tf_384.in21k_ft_in1k | PASS | compilation |
| maxvit_base_tf_512.in21k_ft_in1k | PASS | compilation |
| maxvit_large_tf_384.in21k_ft_in1k | PASS | compilation |
| tf_efficientnet_b8.ra_in1k | PASS | compilation |
| hrnet_w64_Opset17_timm | PASS | compilation |
| hrnet_w64_Opset18_timm | PASS | compilation |
| inception_v4_Opset18_timm | PASS | setup |
| resnetv2_101_Opset16_timm | PASS | compilation |
| resnetv2_101_Opset17_timm | PASS | compilation |
| resnetv2_50_Opset17_timm | PASS | compilation |
| resnetv2_50_Opset18_timm | PASS | compilation |
| tf_efficientnet_b8_Opset16_timm | PASS | compilation |
| tf_efficientnet_b8_Opset17_timm | PASS | compilation |
| tf_efficientnet_b8_ap_Opset16_timm | PASS | compilation |
| visformer_small_Opset16_timm | PASS | compilation |
| visformer_small_Opset18_timm | PASS | compilation |
| vit_l_16_Opset18_torch_hub | PASS | setup |
| xception41_Opset16_timm | PASS | compilation |
| xception41_Opset18_timm | PASS | compilation |
| xception65_Opset16_timm | PASS | compilation |
| xception65_Opset17_timm | PASS | compilation |
| xception71_Opset16_timm | PASS | compilation |
| xception71_Opset18_timm | PASS | compilation |
| squeezebert_Opset17_transformers | PASS | compilation |
| googlenet-3 | PASS | compilation |
| googlenet-6 | PASS | compilation |
| googlenet-8 | PASS | compilation |
| googlenet-9 | PASS | compilation |
| inception-v1-8 | PASS | compilation |
| inception-v1-9 | PASS | compilation |

**Total regressed models: 33**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| regnetx_080.tv2_in1k_vaiq | compilation | PASS |
| regnetx_320.tv2_in1k_vaiq | compilation | PASS |
| regnety_160.sw_in12k_ft_in1k_vaiq | compilation | PASS |
| regnety_320.tv2_in1k_vaiq | compilation | PASS |
| dm_nfnet_f0_Opset17_timm | compilation | PASS |
| dm_nfnet_f1_Opset17_timm | compilation | PASS |
| dm_nfnet_f3_Opset17_timm | compilation | PASS |
| regnet_x_16gf_Opset16_torch_hub | compilation | PASS |
| regnet_x_16gf_Opset17_torch_hub | compilation | PASS |
| regnet_x_32gf_Opset17_torch_hub | compilation | PASS |
| regnet_x_32gf_Opset18_torch_hub | compilation | PASS |
| regnet_x_3_2gf_Opset17_torch_hub | compilation | PASS |
| regnet_x_3_2gf_Opset18_torch_hub | setup | PASS |
| regnet_x_800mf_Opset18_torch_hub | setup | PASS |
| regnet_x_8gf_Opset16_torch_hub | compilation | PASS |
| regnet_x_8gf_Opset17_torch_hub | compilation | PASS |
| regnet_y_16gf_Opset16_torch_hub | compilation | PASS |
| regnet_y_16gf_Opset18_torch_hub | compilation | PASS |
| regnet_y_32gf_Opset16_torch_hub | compilation | PASS |
| regnet_y_32gf_Opset17_torch_hub | compilation | PASS |
| regnetx_032_Opset16_timm | compilation | PASS |
| regnetx_032_Opset17_timm | compilation | PASS |
| regnetx_080_Opset16_timm | compilation | PASS |
| regnetx_080_Opset18_timm | compilation | PASS |
| regnetx_120_Opset17_timm | compilation | PASS |
| regnetx_120_Opset18_timm | compilation | PASS |
| regnetx_160_Opset17_timm | compilation | PASS |
| regnetx_160_Opset18_timm | compilation | PASS |
| regnetx_320_Opset16_timm | compilation | PASS |
| regnetx_320_Opset18_timm | compilation | PASS |
| regnety_120_Opset16_timm | compilation | PASS |
| regnety_160_Opset16_timm | compilation | PASS |
| regnety_320_Opset16_timm | compilation | PASS |
| repvgg_b1g4_Opset16_timm | compilation | PASS |
| repvgg_b1g4_Opset18_timm | compilation | PASS |
| repvgg_b3g4_Opset17_timm | compilation | PASS |
| repvgg_b3g4_Opset18_timm | compilation | PASS |
| resnest14d_Opset16_timm | compilation | PASS |
| resnest200e_Opset16_timm | compilation | PASS |
| resnest269e_Opset16_timm | compilation | PASS |
| resnest26d_Opset16_timm | compilation | PASS |
| resnest50d_1s4x24d_Opset16_timm | compilation | PASS |
| resnest50d_Opset16_timm | compilation | PASS |
| bvlcalexnet-7 | compilation | PASS |
| bvlcalexnet-9 | compilation | PASS |

**Total improved models: 45**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-04-12/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`
**Current Run:** `2026-04-19/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 1987 | 1987 | 0 | ➖ NO CHANGE |
| IREE Compilation | 1946 | 1945 | -1 | ⚠️ REGRESSION |
| Gold Inference | 1946 | 1945 | -1 | ⚠️ REGRESSION |
| IREE Inference Invocation | 1945 | 1944 | -1 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 1914 | 1913 | -1 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 374 | 374 | 0 | ➖ NO CHANGE |
| IREE Compilation | 41 | 42 | +1 | ⚠️ MORE FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 1 | 1 | 0 | ➖ NO CHANGE |
| Inference Comparison | 31 | 31 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -1 fewer tests passing
- **Gold Inference**: -1 fewer tests passing
- **IREE Inference Invocation**: -1 fewer tests passing
- **Inference Comparison (PASS)**: -1 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| squeezebert_Opset17_transformers | PASS | compilation |

**Total regressed models: 1**


---

