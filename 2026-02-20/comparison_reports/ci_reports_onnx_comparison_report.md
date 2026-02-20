---
# Test Comparison Report

*Generated on: 2026-02-20*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-20/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-20/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4102 | 4103 | +1 |
| IREE Compilation | 3441 | 3968 | +527 |
| Gold Inference | 3440 | 3967 | +527 |
| IREE Inference Invocation | 3326 | 3933 | +607 |
| Inference Comparison (PASS) | 3193 | 3638 | +445 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 5 | 4 | -1 |
| IREE Compilation | 661 | 135 | -526 |
| Gold Inference | 1 | 1 | 0 |
| IREE Inference Invocation | 114 | 34 | -80 |
| Inference Comparison | 133 | 295 | +162 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-18/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-20/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4102 | -1 | ⚠️ REGRESSION |
| IREE Compilation | 3442 | 3441 | -1 | ⚠️ REGRESSION |
| Gold Inference | 3442 | 3440 | -2 | ⚠️ REGRESSION |
| IREE Inference Invocation | 3328 | 3326 | -2 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3195 | 3193 | -2 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 5 | +1 | ⚠️ MORE FAILURES |
| IREE Compilation | 661 | 661 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 1 | +1 | ⚠️ MORE FAILURES |
| IREE Inference Invocation | 114 | 114 | 0 | ➖ NO CHANGE |
| Inference Comparison | 133 | 133 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -1 fewer tests passing
- **IREE Compilation**: -1 fewer tests passing
- **Gold Inference**: -2 fewer tests passing
- **IREE Inference Invocation**: -2 fewer tests passing
- **Inference Comparison (PASS)**: -2 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| esm_Opset16_transformers | PASS | setup |
| t5-decoder-with-lm-head-12 | PASS | native_inference |

**Total regressed models: 2**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-18/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-20/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3969 | 3968 | -1 | ⚠️ REGRESSION |
| Gold Inference | 3968 | 3967 | -1 | ⚠️ REGRESSION |
| IREE Inference Invocation | 3934 | 3933 | -1 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3642 | 3638 | -4 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 134 | 135 | +1 | ⚠️ MORE FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 34 | 34 | 0 | ➖ NO CHANGE |
| Inference Comparison | 292 | 295 | +3 | ⚠️ MORE FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -1 fewer tests passing
- **Gold Inference**: -1 fewer tests passing
- **IREE Inference Invocation**: -1 fewer tests passing
- **Inference Comparison (PASS)**: -4 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| vit_large_patch14_clip_336.laion2b_ft_in12k_in1k | PASS | compiled_inference |
| vit_large_patch16_384.augreg_in21k_ft_in1k | PASS | compiled_inference |
| regnetz_d8_evos_Opset16_timm | PASS | Numerics |
| beit_large_patch16_384_Opset16 | PASS | compiled_inference |
| beit_large_patch16_384_Opset17 | PASS | compiled_inference |
| convnext_xlarge_384_in22ft1k_Opset16 | PASS | compiled_inference |
| convnext_xlarge_384_in22ft1k_Opset17 | PASS | compiled_inference |
| regnetz_c16_evos_Opset16 | PASS | Numerics |
| regnetz_c16_evos_Opset17 | PASS | Numerics |
| regnetz_d8_evos_Opset16 | PASS | Numerics |
| regnetz_d8_evos_Opset17 | PASS | Numerics |

**Total regressed models: 11**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| beit_large_patch16_384.in22k_ft_in22k_in1k | compiled_inference | PASS |
| convnext_xlarge.fb_in22k_ft_in1k | compiled_inference | PASS |
| deit3_large_patch16_384.fb_in1k | compiled_inference | PASS |
| dm_nfnet_f4.dm_in1k | compiled_inference | PASS |
| convnext_xlarge_384_in22ft1k_Opset16_timm | compiled_inference | PASS |
| deit3_large_patch16_384_in21ft1k_Opset17_timm | compiled_inference | PASS |
| vit_large_patch16_384_Opset16_timm | compiled_inference | PASS |

**Total improved models: 7**


---

