---
# Test Comparison Report

*Generated on: 2026-02-10*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-10/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-10/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4103 | 4103 | 0 |
| IREE Compilation | 3442 | 3969 | +527 |
| Gold Inference | 3441 | 3968 | +527 |
| IREE Inference Invocation | 3327 | 3939 | +612 |
| Inference Comparison (PASS) | 3194 | 3651 | +457 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 4 | 4 | 0 |
| IREE Compilation | 661 | 134 | -527 |
| Gold Inference | 1 | 1 | 0 |
| IREE Inference Invocation | 114 | 29 | -85 |
| Inference Comparison | 133 | 288 | +155 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-09/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-10/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4098 | 4103 | +5 | ✅ IMPROVED |
| IREE Compilation | 3437 | 3442 | +5 | ✅ IMPROVED |
| Gold Inference | 3437 | 3441 | +4 | ✅ IMPROVED |
| IREE Inference Invocation | 3323 | 3327 | +4 | ✅ IMPROVED |
| Inference Comparison (PASS) | 3190 | 3194 | +4 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 9 | 4 | -5 | ✅ FEWER FAILURES |
| IREE Compilation | 661 | 661 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 1 | +1 | ⚠️ MORE FAILURES |
| IREE Inference Invocation | 114 | 114 | 0 | ➖ NO CHANGE |
| Inference Comparison | 133 | 133 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **Setup**: +5 more tests passing
- **IREE Compilation**: +5 more tests passing
- **Gold Inference**: +4 more tests passing
- **IREE Inference Invocation**: +4 more tests passing
- **Inference Comparison (PASS)**: +4 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| t5-decoder-with-lm-head-12 | PASS | native_inference |

**Total regressed models: 1**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| res2net50_26w_4s_Opset16_timm | setup | PASS |
| tf_efficientnet_b5_Opset16_timm | setup | PASS |
| tf_mixnet_s_Opset16_timm | setup | PASS |
| twins_svt_base_Opset17_timm | setup | PASS |
| xcit_tiny_24_p16_224_dist_Opset16_timm | setup | PASS |

**Total improved models: 5**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-09/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-10/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3969 | 3969 | 0 | ➖ NO CHANGE |
| Gold Inference | 3968 | 3968 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3941 | 3939 | -2 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3653 | 3651 | -2 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 134 | 134 | 0 | ➖ NO CHANGE |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 27 | 29 | +2 | ⚠️ MORE FAILURES |
| Inference Comparison | 288 | 288 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -2 fewer tests passing
- **Inference Comparison (PASS)**: -2 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| beit_large_patch16_384.in22k_ft_in22k_in1k | PASS | compiled_inference |
| convnext_xlarge.fb_in22k_ft_in1k | PASS | compiled_inference |
| deit3_large_patch16_384.fb_in1k | PASS | compiled_inference |
| eva_large_patch14_336.in22k_ft_in1k | PASS | compiled_inference |
| maxvit_large_tf_512.in1k | PASS | compiled_inference |

**Total regressed models: 5**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge_384_in22ft1k_Opset16_timm | compiled_inference | PASS |
| deit3_large_patch16_384_in21ft1k_Opset17_timm | compiled_inference | PASS |
| vit_large_patch16_384_Opset16_timm | compiled_inference | PASS |

**Total improved models: 3**


---

