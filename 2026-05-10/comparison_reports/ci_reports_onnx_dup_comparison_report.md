---
# Test Comparison Report

*Generated on: 2026-05-10*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-10/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-05-10/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 2356 | 1987 | -369 |
| IREE Compilation | 0 | 1929 | +1929 |
| Gold Inference | 0 | 1929 | +1929 |
| IREE Inference Invocation | 0 | 1924 | +1924 |
| Inference Comparison (PASS) | 0 | 1899 | +1899 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 5 | 374 | +369 |
| IREE Compilation | 2356 | 58 | -2298 |
| Gold Inference | 0 | 0 | 0 |
| IREE Inference Invocation | 0 | 5 | +5 |
| Inference Comparison | 0 | 25 | +25 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-03/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**Current Run:** `2026-05-10/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 2361 | 2356 | -5 | ⚠️ REGRESSION |
| IREE Compilation | 2237 | 0 | -2237 | ⚠️ REGRESSION |
| Gold Inference | 2237 | 0 | -2237 | ⚠️ REGRESSION |
| IREE Inference Invocation | 2190 | 0 | -2190 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 2166 | 0 | -2166 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 0 | 5 | +5 | ⚠️ MORE FAILURES |
| IREE Compilation | 124 | 2356 | +2232 | ⚠️ MORE FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 47 | 0 | -47 | ✅ FEWER FAILURES |
| Inference Comparison | 24 | 0 | -24 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -5 fewer tests passing
- **IREE Compilation**: -2237 fewer tests passing
- **Gold Inference**: -2237 fewer tests passing
- **IREE Inference Invocation**: -2190 fewer tests passing
- **Inference Comparison (PASS)**: -2166 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| densenet121_vaiq | PASS | compilation |
| efficientnet_el.ra_in1k_vaiq | PASS | compilation |
| efficientnet_es.ra_in1k_vaiq | PASS | compilation |
| gluon_inception_v3_vaiq | PASS | compilation |
| gluon_resnet101_v1b_vaiq | PASS | compilation |
| gluon_resnet152_v1b_vaiq | PASS | compilation |
| gluon_resnet34_v1b_vaiq | PASS | compilation |
| gluon_resnet50_v1b_vaiq | PASS | compilation |
| gluon_resnext50_32x4d_vaiq | PASS | compilation |
| ig_resnext101_32x32d_vaiq | PASS | compilation |
| ig_resnext101_32x8d_vaiq | PASS | compilation |
| inception_v3_vaiq | PASS | compilation |
| mobilenetv3_large_100.miil_in21k_ft_in1k_vaiq | PASS | compilation |
| regnetx_008.tv2_in1k_vaiq | PASS | compilation |
| regnetx_032.tv2_in1k_vaiq | PASS | compilation |
| regnetx_080.tv2_in1k_vaiq | PASS | compilation |
| regnetx_320.tv2_in1k_vaiq | PASS | compilation |
| regnety_160.sw_in12k_ft_in1k_train_vaiq | PASS | compilation |
| regnety_160.sw_in12k_ft_in1k_vaiq | PASS | compilation |
| regnety_320.tv2_in1k_vaiq | PASS | compilation |
| resnet101_vaiq | PASS | compilation |
| resnet152_vaiq | PASS | compilation |
| resnet18_vaiq | PASS | compilation |
| resnet34_vaiq | PASS | compilation |
| resnet50_vaiq | PASS | compilation |
| resnet50d_vaiq | PASS | compilation |
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
| tf_efficientnetv2_b3.in21k_ft_in1k_train_vaiq | PASS | compilation |
| tf_efficientnetv2_b3.in21k_ft_in1k_vaiq | PASS | compilation |
| xception_vaiq | PASS | compilation |
| eva_large_patch14_196.in22k_ft_in22k_in1k | PASS | compilation |
| eva_large_patch14_336.in22k_ft_in22k_in1k | PASS | compilation |
| flexivit_base.300ep_in1k | PASS | compilation |
| flexivit_base.600ep_in1k | PASS | compilation |
| flexivit_large.300ep_in1k | PASS | compilation |
| flexivit_large.600ep_in1k | PASS | compilation |
| flexivit_small.300ep_in1k | PASS | compilation |

*... and 2116 more regressed models*

**Total regressed models: 2166**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-03/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`
**Current Run:** `2026-05-10/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 1987 | 1987 | 0 | ➖ NO CHANGE |
| IREE Compilation | 1941 | 1929 | -12 | ⚠️ REGRESSION |
| Gold Inference | 1941 | 1929 | -12 | ⚠️ REGRESSION |
| IREE Inference Invocation | 1940 | 1924 | -16 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 1915 | 1899 | -16 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 374 | 374 | 0 | ➖ NO CHANGE |
| IREE Compilation | 46 | 58 | +12 | ⚠️ MORE FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 1 | 5 | +4 | ⚠️ MORE FAILURES |
| Inference Comparison | 25 | 25 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -12 fewer tests passing
- **Gold Inference**: -12 fewer tests passing
- **IREE Inference Invocation**: -16 fewer tests passing
- **Inference Comparison (PASS)**: -16 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge_384_in22ft1k_Opset18_timm | PASS | compiled_inference |
| deit3_large_patch16_384_Opset17_timm | PASS | compiled_inference |
| deit3_large_patch16_384_in21ft1k_Opset16_timm | PASS | compiled_inference |
| dpn107_Opset17_timm | PASS | compilation |
| dpn131_Opset16_timm | PASS | compilation |
| dpn131_Opset17_timm | PASS | compilation |
| dpn68_Opset16_timm | PASS | compilation |
| dpn68_Opset18_timm | PASS | compilation |
| dpn68b_Opset17_timm | PASS | compilation |
| dpn68b_Opset18_timm | PASS | compilation |
| dpn92_Opset16_timm | PASS | compilation |
| dpn92_Opset18_timm | PASS | compilation |
| dpn98_Opset16_timm | PASS | compilation |
| dpn98_Opset18_timm | PASS | compilation |
| vit_large_patch16_384_Opset18_timm | PASS | compiled_inference |
| migraphx_torchvision__inceptioni32 | PASS | compilation |

**Total regressed models: 16**


---

