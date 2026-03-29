---
# Test Comparison Report

*Generated on: 2026-03-29*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-03-29/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-03-29/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 2359 | 1987 | -372 |
| IREE Compilation | 2190 | 1942 | -248 |
| Gold Inference | 2190 | 1942 | -248 |
| IREE Inference Invocation | 2183 | 1937 | -246 |
| Inference Comparison (PASS) | 2164 | 1907 | -257 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 2 | 374 | +372 |
| IREE Compilation | 169 | 45 | -124 |
| Gold Inference | 0 | 0 | 0 |
| IREE Inference Invocation | 7 | 5 | -2 |
| Inference Comparison | 19 | 30 | +11 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-03-15/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**Current Run:** `2026-03-29/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 2359 | 2359 | 0 | ➖ NO CHANGE |
| IREE Compilation | 2188 | 2190 | +2 | ✅ IMPROVED |
| Gold Inference | 2188 | 2190 | +2 | ✅ IMPROVED |
| IREE Inference Invocation | 2181 | 2183 | +2 | ✅ IMPROVED |
| Inference Comparison (PASS) | 2162 | 2164 | +2 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 2 | 2 | 0 | ➖ NO CHANGE |
| IREE Compilation | 171 | 169 | -2 | ✅ FEWER FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 7 | 7 | 0 | ➖ NO CHANGE |
| Inference Comparison | 19 | 19 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Compilation**: +2 more tests passing
- **Gold Inference**: +2 more tests passing
- **IREE Inference Invocation**: +2 more tests passing
- **Inference Comparison (PASS)**: +2 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| seresnext26tn_32x4d_Opset16_timm | setup | PASS |
| leconv_Opset18_graph_convolutions | setup | PASS |

**Total improved models: 2**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-03-15/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`
**Current Run:** `2026-03-29/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

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
| IREE Inference Invocation | 1933 | 1937 | +4 | ✅ IMPROVED |
| Inference Comparison (PASS) | 1903 | 1907 | +4 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 374 | 374 | 0 | ➖ NO CHANGE |
| IREE Compilation | 45 | 45 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 9 | 5 | -4 | ✅ FEWER FAILURES |
| Inference Comparison | 30 | 30 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Inference Invocation**: +4 more tests passing
- **Inference Comparison (PASS)**: +4 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge.fb_in22k_ft_in1k_384 | PASS | compiled_inference |
| deit3_large_patch16_384.fb_in22k_ft_in1k | PASS | compiled_inference |

**Total regressed models: 2**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| eva_large_patch14_336.in22k_ft_in22k_in1k | compiled_inference | PASS |
| maxvit_large_tf_512.in21k_ft_in1k | compiled_inference | PASS |
| vit_large_patch14_clip_336.laion2b_ft_in1k | compiled_inference | PASS |
| vit_large_patch14_clip_336.openai_ft_in12k_in1k | compiled_inference | PASS |
| convnext_xlarge_384_in22ft1k_Opset17_timm | compiled_inference | PASS |
| deit3_large_patch16_384_Opset18_timm | compiled_inference | PASS |

**Total improved models: 6**


---

