---
# Test Comparison Report

*Generated on: 2026-03-15*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-03-15/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-03-15/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 2359 | 1987 | -372 |
| IREE Compilation | 2188 | 1942 | -246 |
| Gold Inference | 2188 | 1942 | -246 |
| IREE Inference Invocation | 2181 | 1933 | -248 |
| Inference Comparison (PASS) | 2162 | 1903 | -259 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 2 | 374 | +372 |
| IREE Compilation | 171 | 45 | -126 |
| Gold Inference | 0 | 0 | 0 |
| IREE Inference Invocation | 7 | 9 | +2 |
| Inference Comparison | 19 | 30 | +11 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-03-08/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**Current Run:** `2026-03-15/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 2360 | 2359 | -1 | ⚠️ REGRESSION |
| IREE Compilation | 2189 | 2188 | -1 | ⚠️ REGRESSION |
| Gold Inference | 2189 | 2188 | -1 | ⚠️ REGRESSION |
| IREE Inference Invocation | 2182 | 2181 | -1 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 2163 | 2162 | -1 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 1 | 2 | +1 | ⚠️ MORE FAILURES |
| IREE Compilation | 171 | 171 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 7 | 7 | 0 | ➖ NO CHANGE |
| Inference Comparison | 19 | 19 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -1 fewer tests passing
- **IREE Compilation**: -1 fewer tests passing
- **Gold Inference**: -1 fewer tests passing
- **IREE Inference Invocation**: -1 fewer tests passing
- **Inference Comparison (PASS)**: -1 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| seresnext26tn_32x4d_Opset16_timm | PASS | setup |
| leconv_Opset18_graph_convolutions | PASS | setup |

**Total regressed models: 2**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| resnetv2_101_Opset17_timm | setup | PASS |

**Total improved models: 1**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-03-08/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`
**Current Run:** `2026-03-15/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

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
| IREE Inference Invocation | 1937 | 1933 | -4 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 1903 | 1903 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 374 | 374 | 0 | ➖ NO CHANGE |
| IREE Compilation | 45 | 45 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 9 | +4 | ⚠️ MORE FAILURES |
| Inference Comparison | 34 | 30 | -4 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -4 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| eva_large_patch14_336.in22k_ft_in22k_in1k | PASS | compiled_inference |
| maxvit_large_tf_512.in21k_ft_in1k | PASS | compiled_inference |
| convnext_xlarge_384_in22ft1k_Opset17_timm | PASS | compiled_inference |
| convnext_xlarge_384_in22ft1k_Opset18_timm | PASS | compiled_inference |
| deit3_large_patch16_384_Opset18_timm | PASS | compiled_inference |
| deit3_large_patch16_384_in21ft1k_Opset16_timm | PASS | compiled_inference |

**Total regressed models: 6**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge.fb_in22k_ft_in1k_384 | compiled_inference | PASS |
| deit3_large_patch16_384.fb_in22k_ft_in1k | compiled_inference | PASS |
| candy-8 | Numerics | PASS |
| mosaic-8 | Numerics | PASS |
| pointilism-8 | Numerics | PASS |
| udnie-8 | Numerics | PASS |

**Total improved models: 6**


---

