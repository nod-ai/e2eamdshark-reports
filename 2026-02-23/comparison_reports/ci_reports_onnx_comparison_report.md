---
# Test Comparison Report

*Generated on: 2026-02-23*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-23/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-23/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4103 | 4103 | 0 |
| IREE Compilation | 3441 | 3965 | +524 |
| Gold Inference | 3440 | 3964 | +524 |
| IREE Inference Invocation | 3326 | 3935 | +609 |
| Inference Comparison (PASS) | 3193 | 3640 | +447 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 4 | 4 | 0 |
| IREE Compilation | 662 | 138 | -524 |
| Gold Inference | 1 | 1 | 0 |
| IREE Inference Invocation | 114 | 29 | -85 |
| Inference Comparison | 133 | 295 | +162 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-20/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-23/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4102 | 4103 | +1 | ✅ IMPROVED |
| IREE Compilation | 3441 | 3441 | 0 | ➖ NO CHANGE |
| Gold Inference | 3440 | 3440 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3326 | 3326 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 3193 | 3193 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 5 | 4 | -1 | ✅ FEWER FAILURES |
| IREE Compilation | 661 | 662 | +1 | ⚠️ MORE FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 114 | 114 | 0 | ➖ NO CHANGE |
| Inference Comparison | 133 | 133 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **Setup**: +1 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| swsl_resnext101_32x8d_Opset16 | PASS | compilation |

**Total regressed models: 1**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| esm_Opset16_transformers | setup | PASS |

**Total improved models: 1**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-20/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-23/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3968 | 3965 | -3 | ⚠️ REGRESSION |
| Gold Inference | 3967 | 3964 | -3 | ⚠️ REGRESSION |
| IREE Inference Invocation | 3933 | 3935 | +2 | ✅ IMPROVED |
| Inference Comparison (PASS) | 3638 | 3640 | +2 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 135 | 138 | +3 | ⚠️ MORE FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 34 | 29 | -5 | ✅ FEWER FAILURES |
| Inference Comparison | 295 | 295 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -3 fewer tests passing
- **Gold Inference**: -3 fewer tests passing

### ✅ Improvements

- **IREE Inference Invocation**: +2 more tests passing
- **Inference Comparison (PASS)**: +2 more tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| beit_large_patch16_384.in22k_ft_in22k_in1k | PASS | compiled_inference |
| convnext_xlarge.fb_in22k_ft_in1k | PASS | compiled_inference |
| deit3_large_patch16_384.fb_in1k | PASS | compiled_inference |
| dm_nfnet_f4.dm_in1k | PASS | compiled_inference |

**Total regressed models: 4**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| vit_large_patch14_clip_336.laion2b_ft_in12k_in1k | compiled_inference | PASS |
| vit_large_patch16_384.augreg_in21k_ft_in1k | compiled_inference | PASS |
| deit3_large_patch16_384_Opset16 | compiled_inference | PASS |
| deit3_large_patch16_384_in21ft1k_Opset16 | compiled_inference | PASS |
| deit3_large_patch16_384_in21ft1k_Opset17 | compiled_inference | PASS |
| deit3_large_patch16_384_in21ft1k_Opset18 | compiled_inference | PASS |

**Total improved models: 6**


---

