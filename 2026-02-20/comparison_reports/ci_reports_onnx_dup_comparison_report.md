---
# Test Comparison Report

*Generated on: 2026-02-20*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-20/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-02-20/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 2361 | 1987 | -374 |
| IREE Compilation | 2134 | 1942 | -192 |
| Gold Inference | 2134 | 1942 | -192 |
| IREE Inference Invocation | 2133 | 1937 | -196 |
| Inference Comparison (PASS) | 2112 | 1903 | -209 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 0 | 374 | +374 |
| IREE Compilation | 227 | 45 | -182 |
| Gold Inference | 0 | 0 | 0 |
| IREE Inference Invocation | 1 | 5 | +4 |
| Inference Comparison | 21 | 34 | +13 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-19/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**Current Run:** `2026-02-20/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 2356 | 2361 | +5 | ✅ IMPROVED |
| IREE Compilation | 2132 | 2134 | +2 | ✅ IMPROVED |
| Gold Inference | 2132 | 2134 | +2 | ✅ IMPROVED |
| IREE Inference Invocation | 2131 | 2133 | +2 | ✅ IMPROVED |
| Inference Comparison (PASS) | 2110 | 2112 | +2 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 5 | 0 | -5 | ✅ FEWER FAILURES |
| IREE Compilation | 224 | 227 | +3 | ⚠️ MORE FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 1 | 1 | 0 | ➖ NO CHANGE |
| Inference Comparison | 21 | 21 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **Setup**: +5 more tests passing
- **IREE Compilation**: +2 more tests passing
- **Gold Inference**: +2 more tests passing
- **IREE Inference Invocation**: +2 more tests passing
- **Inference Comparison (PASS)**: +2 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| resnet152d_Opset18_timm | setup | PASS |
| resnetrs101_Opset16_timm | setup | PASS |

**Total improved models: 2**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-19/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`
**Current Run:** `2026-02-20/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

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
| vit_large_patch14_clip_336.laion2b_ft_in1k | PASS | compiled_inference |
| vit_large_patch14_clip_336.openai_ft_in12k_in1k | PASS | compiled_inference |
| convnext_xlarge_384_in22ft1k_Opset17_timm | PASS | compiled_inference |
| deit3_large_patch16_384_Opset18_timm | PASS | compiled_inference |

**Total regressed models: 4**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge.fb_in22k_ft_in1k_384 | compiled_inference | PASS |
| deit3_large_patch16_384.fb_in22k_ft_in1k | compiled_inference | PASS |
| deit3_large_patch16_384_Opset17_timm | compiled_inference | PASS |
| vit_large_patch16_384_Opset18_timm | compiled_inference | PASS |

**Total improved models: 4**


---

