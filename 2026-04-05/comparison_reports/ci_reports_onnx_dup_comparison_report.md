---
# Test Comparison Report

*Generated on: 2026-04-05*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-04-05/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-04-05/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 2358 | 1987 | -371 |
| IREE Compilation | 2224 | 1942 | -282 |
| Gold Inference | 2224 | 1942 | -282 |
| IREE Inference Invocation | 2217 | 1936 | -281 |
| Inference Comparison (PASS) | 2175 | 1906 | -269 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 3 | 374 | +371 |
| IREE Compilation | 134 | 45 | -89 |
| Gold Inference | 0 | 0 | 0 |
| IREE Inference Invocation | 7 | 6 | -1 |
| Inference Comparison | 42 | 30 | -12 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-03-29/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**Current Run:** `2026-04-05/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 2359 | 2358 | -1 | ⚠️ REGRESSION |
| IREE Compilation | 2190 | 2224 | +34 | ✅ IMPROVED |
| Gold Inference | 2190 | 2224 | +34 | ✅ IMPROVED |
| IREE Inference Invocation | 2183 | 2217 | +34 | ✅ IMPROVED |
| Inference Comparison (PASS) | 2164 | 2175 | +11 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 2 | 3 | +1 | ⚠️ MORE FAILURES |
| IREE Compilation | 169 | 134 | -35 | ✅ FEWER FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 7 | 7 | 0 | ➖ NO CHANGE |
| Inference Comparison | 19 | 42 | +23 | ⚠️ MORE FAILURES |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -1 fewer tests passing

### ✅ Improvements

- **IREE Compilation**: +34 more tests passing
- **Gold Inference**: +34 more tests passing
- **IREE Inference Invocation**: +34 more tests passing
- **Inference Comparison (PASS)**: +11 more tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| marian_Opset17_transformers | PASS | setup |
| markuplm_Opset17_transformers | PASS | setup |

**Total regressed models: 2**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| gluon_resnet34_v1b_vaiq | compilation | PASS |
| regnetx_032.tv2_in1k_vaiq | compilation | PASS |
| regnety_032.tv2_in1k_vaiq | compilation | PASS |
| regnety_160.sw_in12k_ft_in1k_train_vaiq | compilation | PASS |
| resnet18_vaiq | compilation | PASS |
| resnet34_vaiq | compilation | PASS |
| ssl_resnet18_vaiq | compilation | PASS |
| swsl_resnet18_vaiq | compilation | PASS |
| xception_vaiq | compilation | PASS |
| gcresnet33ts_Opset18_timm | compilation | PASS |
| gcresnet50t_Opset18_timm | compilation | PASS |
| gcresnext26ts_Opset17_timm | compilation | PASS |
| gcresnext50ts_Opset17_timm | compilation | PASS |

**Total improved models: 13**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-03-29/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`
**Current Run:** `2026-04-05/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

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
| IREE Inference Invocation | 1937 | 1936 | -1 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 1907 | 1906 | -1 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 374 | 374 | 0 | ➖ NO CHANGE |
| IREE Compilation | 45 | 45 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 6 | +1 | ⚠️ MORE FAILURES |
| Inference Comparison | 30 | 30 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -1 fewer tests passing
- **Inference Comparison (PASS)**: -1 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| vit_large_patch14_clip_336.laion2b_ft_in1k | PASS | compiled_inference |
| vit_large_patch14_clip_336.openai_ft_in12k_in1k | PASS | compiled_inference |
| deit3_large_patch16_384_in21ft1k_Opset18_timm | PASS | compiled_inference |

**Total regressed models: 3**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge.fb_in22k_ft_in1k_384 | compiled_inference | PASS |
| deit3_large_patch16_384.fb_in22k_ft_in1k | compiled_inference | PASS |

**Total improved models: 2**


---

