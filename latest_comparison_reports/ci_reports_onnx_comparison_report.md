---
# Test Comparison Report

*Generated on: 2026-02-18 | Copied to latest: 2026-02-18*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-18/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-18/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

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
| Gold Inference | 3442 | 3968 | +526 |
| IREE Inference Invocation | 3328 | 3934 | +606 |
| Inference Comparison (PASS) | 3195 | 3642 | +447 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 4 | 4 | 0 |
| IREE Compilation | 661 | 134 | -527 |
| Gold Inference | 0 | 1 | +1 |
| IREE Inference Invocation | 114 | 34 | -80 |
| Inference Comparison | 133 | 292 | +159 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-17/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-18/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3442 | 3442 | 0 | ➖ NO CHANGE |
| Gold Inference | 3441 | 3442 | +1 | ✅ IMPROVED |
| IREE Inference Invocation | 3327 | 3328 | +1 | ✅ IMPROVED |
| Inference Comparison (PASS) | 3194 | 3195 | +1 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 661 | 661 | 0 | ➖ NO CHANGE |
| Gold Inference | 1 | 0 | -1 | ✅ FEWER FAILURES |
| IREE Inference Invocation | 114 | 114 | 0 | ➖ NO CHANGE |
| Inference Comparison | 133 | 133 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **Gold Inference**: +1 more tests passing
- **IREE Inference Invocation**: +1 more tests passing
- **Inference Comparison (PASS)**: +1 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| t5-decoder-with-lm-head-12 | native_inference | PASS |

**Total improved models: 1**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-17/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-18/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 3939 | 3934 | -5 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3645 | 3642 | -3 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 134 | 134 | 0 | ➖ NO CHANGE |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 29 | 34 | +5 | ⚠️ MORE FAILURES |
| Inference Comparison | 294 | 292 | -2 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -5 fewer tests passing
- **Inference Comparison (PASS)**: -3 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| beit_large_patch16_384.in22k_ft_in22k_in1k | PASS | compiled_inference |
| convnext_xlarge.fb_in22k_ft_in1k | PASS | compiled_inference |
| deit3_large_patch16_384.fb_in1k | PASS | compiled_inference |
| dm_nfnet_f4.dm_in1k | PASS | compiled_inference |
| convnext_xlarge_384_in22ft1k_Opset16_timm | PASS | compiled_inference |
| deit3_large_patch16_384_in21ft1k_Opset17_timm | PASS | compiled_inference |
| regnetz_c16_evos_Opset16_timm | PASS | Numerics |
| vit_large_patch16_384_Opset16_timm | PASS | compiled_inference |
| deit3_large_patch16_384_Opset16 | PASS | compiled_inference |
| deit3_large_patch16_384_in21ft1k_Opset16 | PASS | compiled_inference |
| deit3_large_patch16_384_in21ft1k_Opset17 | PASS | compiled_inference |
| deit3_large_patch16_384_in21ft1k_Opset18 | PASS | compiled_inference |

**Total regressed models: 12**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| xception41_Opset17_timm | compiled_inference | PASS |
| xception65_Opset18_timm | compiled_inference | PASS |
| xception71_Opset17_timm | compiled_inference | PASS |
| deit3_large_patch16_384_Opset17 | compiled_inference | PASS |
| deit3_large_patch16_384_Opset18 | compiled_inference | PASS |
| regnetz_c16_evos_Opset16 | Numerics | PASS |
| regnetz_c16_evos_Opset17 | Numerics | PASS |
| regnetz_d8_evos_Opset16 | Numerics | PASS |
| regnetz_d8_evos_Opset17 | Numerics | PASS |

**Total improved models: 9**


---

