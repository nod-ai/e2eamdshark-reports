---
# Test Comparison Report

*Generated on: 2026-02-08*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-08/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-02-08/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 2343 | 1987 | -356 |
| IREE Compilation | 2117 | 1942 | -175 |
| Gold Inference | 2117 | 1942 | -175 |
| IREE Inference Invocation | 2116 | 1937 | -179 |
| Inference Comparison (PASS) | 2095 | 1903 | -192 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 18 | 374 | +356 |
| IREE Compilation | 226 | 45 | -181 |
| Gold Inference | 0 | 0 | 0 |
| IREE Inference Invocation | 1 | 5 | +4 |
| Inference Comparison | 21 | 34 | +13 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-01/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**Current Run:** `2026-02-08/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 2350 | 2343 | -7 | ⚠️ REGRESSION |
| IREE Compilation | 2124 | 2117 | -7 | ⚠️ REGRESSION |
| Gold Inference | 2124 | 2117 | -7 | ⚠️ REGRESSION |
| IREE Inference Invocation | 2123 | 2116 | -7 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 2099 | 2095 | -4 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 11 | 18 | +7 | ⚠️ MORE FAILURES |
| IREE Compilation | 226 | 226 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 1 | 1 | 0 | ➖ NO CHANGE |
| Inference Comparison | 24 | 21 | -3 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -7 fewer tests passing
- **IREE Compilation**: -7 fewer tests passing
- **Gold Inference**: -7 fewer tests passing
- **IREE Inference Invocation**: -7 fewer tests passing
- **Inference Comparison (PASS)**: -4 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| deit_base_patch16_384_Opset18_timm | PASS | setup |
| dpn68_Opset16_timm | PASS | setup |
| eca_resnext26ts_Opset16_timm | PASS | setup |
| gluon_resnet101_v1s_Opset18_timm | PASS | setup |
| gluon_resnet152_v1d_Opset17_timm | PASS | setup |
| hrnet_w32_Opset18_timm | PASS | setup |
| mixer_l16_224_Opset16_timm | PASS | setup |
| resnet152_Opset17_torch_hub | PASS | setup |
| resnetv2_50d_gn_Opset18_timm | PASS | setup |
| ssl_resnet18_Opset18_timm | PASS | setup |
| tf_efficientnet_b5_Opset17_timm | PASS | setup |
| tf_efficientnetv2_b1_Opset17_timm | PASS | setup |
| tf_efficientnetv2_m_in21k_Opset17_timm | PASS | setup |
| visformer_small_Opset16_timm | PASS | setup |
| vit_large_patch32_384_Opset18_timm | PASS | setup |
| wide_resnet101_2_Opset17_timm | PASS | setup |
| umt5encoder_Opset17_transformers | PASS | setup |

**Total regressed models: 17**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| densenet121_vaiq | setup | PASS |
| resnet34_vaiq | setup | PASS |
| beitv2_large_patch16_224.in1k_ft_in22k_in1k | setup | PASS |
| model--bert-base-uncased-finetuned-squad--harveyagraphcore | setup | PASS |
| model--finetuning-sentiment-model-3000-samples--nachowdh | setup | PASS |
| inception_v4_Opset17_timm | Numerics | PASS |
| inception_v4_Opset18_timm | Numerics | PASS |
| regnetx_064_Opset18_timm | setup | PASS |
| vit_l_16_Opset18_torch_hub | setup | PASS |
| yolov8n_vaiq_int8 | Numerics | PASS |
| Yolov8n_vaiq | Numerics | PASS |
| migraphx_cadene__resnext101_64x4di16 | setup | PASS |
| migraphx_torchvision__inceptioni32 | setup | PASS |

**Total improved models: 13**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-01/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`
**Current Run:** `2026-02-08/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

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
| IREE Inference Invocation | 1941 | 1937 | -4 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 1917 | 1903 | -14 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 374 | 374 | 0 | ➖ NO CHANGE |
| IREE Compilation | 45 | 45 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 1 | 5 | +4 | ⚠️ MORE FAILURES |
| Inference Comparison | 24 | 34 | +10 | ⚠️ MORE FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -4 fewer tests passing
- **Inference Comparison (PASS)**: -14 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| mobilevitv2_150_384_in22ft1k | PASS | Numerics |
| mobilevitv2_175_384_in22ft1k | PASS | Numerics |
| mobilevitv2_200_384_in22ft1k | PASS | Numerics |
| model--bart-large-cnn--facebook | PASS | Numerics |
| convnext_xlarge_384_in22ft1k_Opset17_timm | PASS | compiled_inference |
| convnext_xlarge_384_in22ft1k_Opset18_timm | PASS | compiled_inference |
| deit3_large_patch16_384_Opset18_timm | PASS | compiled_inference |
| deit3_large_patch16_384_in21ft1k_Opset16_timm | PASS | compiled_inference |
| mobilevitv2_150_384_in22ft1k_Opset17_timm | PASS | Numerics |
| mobilevitv2_150_384_in22ft1k_Opset18_timm | PASS | Numerics |
| mobilevitv2_175_384_in22ft1k_Opset16_timm | PASS | Numerics |
| mobilevitv2_175_384_in22ft1k_Opset18_timm | PASS | Numerics |
| mobilevitv2_200_384_in22ft1k_Opset16_timm | PASS | Numerics |
| mobilevitv2_200_384_in22ft1k_Opset17_timm | PASS | Numerics |

**Total regressed models: 14**


---

