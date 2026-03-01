---
# Test Comparison Report

*Generated on: 2026-03-01*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-03-01/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-03-01/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 2359 | 1987 | -372 |
| IREE Compilation | 2131 | 1942 | -189 |
| Gold Inference | 2131 | 1942 | -189 |
| IREE Inference Invocation | 2130 | 1937 | -193 |
| Inference Comparison (PASS) | 2111 | 1903 | -208 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 2 | 374 | +372 |
| IREE Compilation | 228 | 45 | -183 |
| Gold Inference | 0 | 0 | 0 |
| IREE Inference Invocation | 1 | 5 | +4 |
| Inference Comparison | 19 | 34 | +15 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-23/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**Current Run:** `2026-03-01/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 2351 | 2359 | +8 | ✅ IMPROVED |
| IREE Compilation | 2128 | 2131 | +3 | ✅ IMPROVED |
| Gold Inference | 2128 | 2131 | +3 | ✅ IMPROVED |
| IREE Inference Invocation | 2127 | 2130 | +3 | ✅ IMPROVED |
| Inference Comparison (PASS) | 2106 | 2111 | +5 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 10 | 2 | -8 | ✅ FEWER FAILURES |
| IREE Compilation | 223 | 228 | +5 | ⚠️ MORE FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 1 | 1 | 0 | ➖ NO CHANGE |
| Inference Comparison | 21 | 19 | -2 | ✅ FEWER FAILURES |

## Summary

### ✅ Improvements

- **Setup**: +8 more tests passing
- **IREE Compilation**: +3 more tests passing
- **Gold Inference**: +3 more tests passing
- **IREE Inference Invocation**: +3 more tests passing
- **Inference Comparison (PASS)**: +5 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| regnetx_032.tv2_in1k_vaiq | PASS | compilation |
| regnety_032.tv2_in1k_vaiq | PASS | compilation |
| regnety_160.sw_in12k_ft_in1k_train_vaiq | PASS | compilation |
| mobilevitv2_125_Opset17_timm | PASS | setup |
| resnext101_32x4d_Opset16_timm | PASS | setup |

**Total regressed models: 5**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| model--mobilebert-uncased-finetuned-squadv2--mrm8488 | compilation | PASS |
| model--mobilebert_mrpc--Alireza1044 | compilation | PASS |
| model--mobilebert_rte--Alireza1044 | compilation | PASS |
| model--mobilebert_sst2--Alireza1044 | compilation | PASS |
| gluon_resnet50_v1b_Opset18_timm | setup | PASS |
| mobilenetv2_110d_Opset16_timm | setup | PASS |
| mobilenetv2_110d_Opset17_timm | setup | PASS |
| resnet152_Opset16_torch_hub | setup | PASS |
| vit_base_patch8_224_in21k_Opset18_timm | setup | PASS |
| vit_relpos_medium_patch16_cls_224_Opset18_timm | setup | PASS |

**Total improved models: 10**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-22/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`
**Current Run:** `2026-03-01/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

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
| IREE Inference Invocation | 1939 | 1937 | -2 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 1905 | 1903 | -2 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 374 | 374 | 0 | ➖ NO CHANGE |
| IREE Compilation | 45 | 45 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3 | 5 | +2 | ⚠️ MORE FAILURES |
| Inference Comparison | 34 | 34 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -2 fewer tests passing
- **Inference Comparison (PASS)**: -2 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge_384_in22ft1k_Opset18_timm | PASS | compiled_inference |
| deit3_large_patch16_384_Opset17_timm | PASS | compiled_inference |
| deit3_large_patch16_384_in21ft1k_Opset16_timm | PASS | compiled_inference |
| vit_large_patch16_384_Opset18_timm | PASS | compiled_inference |

**Total regressed models: 4**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| vit_large_patch14_clip_336.laion2b_ft_in1k | compiled_inference | PASS |
| vit_large_patch14_clip_336.openai_ft_in12k_in1k | compiled_inference | PASS |

**Total improved models: 2**


---

