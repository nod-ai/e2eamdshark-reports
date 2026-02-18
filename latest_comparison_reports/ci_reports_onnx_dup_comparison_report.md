---
# Test Comparison Report

*Generated on: 2026-02-15 | Copied to latest: 2026-02-18*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-15/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-02-15/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 2360 | 1987 | -373 |
| IREE Compilation | 2133 | 1942 | -191 |
| Gold Inference | 2133 | 1942 | -191 |
| IREE Inference Invocation | 2132 | 1940 | -192 |
| Inference Comparison (PASS) | 2111 | 1906 | -205 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 1 | 374 | +373 |
| IREE Compilation | 227 | 45 | -182 |
| Gold Inference | 0 | 0 | 0 |
| IREE Inference Invocation | 1 | 2 | +1 |
| Inference Comparison | 21 | 34 | +13 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-08/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**Current Run:** `2026-02-15/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 2343 | 2360 | +17 | ✅ IMPROVED |
| IREE Compilation | 2117 | 2133 | +16 | ✅ IMPROVED |
| Gold Inference | 2117 | 2133 | +16 | ✅ IMPROVED |
| IREE Inference Invocation | 2116 | 2132 | +16 | ✅ IMPROVED |
| Inference Comparison (PASS) | 2095 | 2111 | +16 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 18 | 1 | -17 | ✅ FEWER FAILURES |
| IREE Compilation | 226 | 227 | +1 | ⚠️ MORE FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 1 | 1 | 0 | ➖ NO CHANGE |
| Inference Comparison | 21 | 21 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **Setup**: +17 more tests passing
- **IREE Compilation**: +16 more tests passing
- **Gold Inference**: +16 more tests passing
- **IREE Inference Invocation**: +16 more tests passing
- **Inference Comparison (PASS)**: +16 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| deit_base_patch16_384_Opset18_timm | setup | PASS |
| dpn68_Opset16_timm | setup | PASS |
| eca_resnext26ts_Opset16_timm | setup | PASS |
| gluon_resnet101_v1s_Opset18_timm | setup | PASS |
| gluon_resnet152_v1d_Opset17_timm | setup | PASS |
| hrnet_w32_Opset18_timm | setup | PASS |
| resnet152_Opset17_torch_hub | setup | PASS |
| resnetv2_50d_gn_Opset18_timm | setup | PASS |
| ssl_resnet18_Opset18_timm | setup | PASS |
| tf_efficientnet_b5_Opset17_timm | setup | PASS |
| tf_efficientnetv2_b1_Opset17_timm | setup | PASS |
| tf_efficientnetv2_m_in21k_Opset17_timm | setup | PASS |
| visformer_small_Opset16_timm | setup | PASS |
| vit_large_patch32_384_Opset18_timm | setup | PASS |
| wide_resnet101_2_Opset17_timm | setup | PASS |
| umt5encoder_Opset17_transformers | setup | PASS |

**Total improved models: 16**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-08/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`
**Current Run:** `2026-02-15/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

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
| IREE Inference Invocation | 1937 | 1940 | +3 | ✅ IMPROVED |
| Inference Comparison (PASS) | 1903 | 1906 | +3 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 374 | 374 | 0 | ➖ NO CHANGE |
| IREE Compilation | 45 | 45 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 2 | -3 | ✅ FEWER FAILURES |
| Inference Comparison | 34 | 34 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Inference Invocation**: +3 more tests passing
- **Inference Comparison (PASS)**: +3 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| regnetx_002_Opset18_timm | PASS | compiled_inference |

**Total regressed models: 1**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge_384_in22ft1k_Opset17_timm | compiled_inference | PASS |
| convnext_xlarge_384_in22ft1k_Opset18_timm | compiled_inference | PASS |
| deit3_large_patch16_384_Opset18_timm | compiled_inference | PASS |
| deit3_large_patch16_384_in21ft1k_Opset16_timm | compiled_inference | PASS |

**Total improved models: 4**


---

