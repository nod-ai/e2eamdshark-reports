---
# Test Comparison Report

*Generated on: 2026-02-11*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-11/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-11/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4103 | 4103 | 0 |
| IREE Compilation | 3442 | 3966 | +524 |
| Gold Inference | 3441 | 3965 | +524 |
| IREE Inference Invocation | 3327 | 3939 | +612 |
| Inference Comparison (PASS) | 3194 | 3651 | +457 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 4 | 4 | 0 |
| IREE Compilation | 661 | 137 | -524 |
| Gold Inference | 1 | 1 | 0 |
| IREE Inference Invocation | 114 | 26 | -88 |
| Inference Comparison | 133 | 288 | +155 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-10/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-11/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

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
| Gold Inference | 3441 | 3441 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3327 | 3327 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 3194 | 3194 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 661 | 661 | 0 | ➖ NO CHANGE |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 114 | 114 | 0 | ➖ NO CHANGE |
| Inference Comparison | 133 | 133 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-10/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-11/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3969 | 3966 | -3 | ⚠️ REGRESSION |
| Gold Inference | 3968 | 3965 | -3 | ⚠️ REGRESSION |
| IREE Inference Invocation | 3939 | 3939 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 3651 | 3651 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 134 | 137 | +3 | ⚠️ MORE FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 29 | 26 | -3 | ✅ FEWER FAILURES |
| Inference Comparison | 288 | 288 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -3 fewer tests passing
- **Gold Inference**: -3 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| vit_large_patch14_clip_336.laion2b_ft_in12k_in1k | PASS | compiled_inference |
| vit_large_patch16_384.augreg_in21k_ft_in1k | PASS | compiled_inference |
| convnext_xlarge_384_in22ft1k_Opset16_timm | PASS | compiled_inference |
| deit3_large_patch16_384_Opset16_timm | PASS | compiled_inference |
| deit3_large_patch16_384_in21ft1k_Opset17_timm | PASS | compiled_inference |
| vit_large_patch16_384_Opset16_timm | PASS | compiled_inference |

**Total regressed models: 6**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| beit_large_patch16_384.in22k_ft_in22k_in1k | compiled_inference | PASS |
| convnext_xlarge.fb_in22k_ft_in1k | compiled_inference | PASS |
| deit3_large_patch16_384.fb_in1k | compiled_inference | PASS |
| eva_large_patch14_336.in22k_ft_in1k | compiled_inference | PASS |
| maxvit_large_tf_512.in1k | compiled_inference | PASS |
| model--albert-xxl-v2-finetuned-squad--anas-awadalla | compiled_inference | PASS |

**Total improved models: 6**


---

