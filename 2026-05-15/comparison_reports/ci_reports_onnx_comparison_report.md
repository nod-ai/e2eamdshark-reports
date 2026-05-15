---
# Test Comparison Report

*Generated on: 2026-05-15*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-15/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-15/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4103 | 4103 | 0 |
| IREE Compilation | 0 | 3960 | +3960 |
| Gold Inference | 0 | 3959 | +3959 |
| IREE Inference Invocation | 0 | 3930 | +3930 |
| Inference Comparison (PASS) | 0 | 3655 | +3655 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 4 | 4 | 0 |
| IREE Compilation | 4103 | 143 | -3960 |
| Gold Inference | 0 | 1 | +1 |
| IREE Inference Invocation | 0 | 29 | +29 |
| Inference Comparison | 0 | 275 | +275 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-13/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-15/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 0 | 0 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 4103 | 4103 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison | 0 | 0 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-13/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-15/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3931 | 3960 | +29 | ✅ IMPROVED |
| Gold Inference | 3930 | 3959 | +29 | ✅ IMPROVED |
| IREE Inference Invocation | 3900 | 3930 | +30 | ✅ IMPROVED |
| Inference Comparison (PASS) | 3628 | 3655 | +27 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 172 | 143 | -29 | ✅ FEWER FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 30 | 29 | -1 | ✅ FEWER FAILURES |
| Inference Comparison | 272 | 275 | +3 | ⚠️ MORE FAILURES |

## Summary

### ✅ Improvements

- **IREE Compilation**: +29 more tests passing
- **Gold Inference**: +29 more tests passing
- **IREE Inference Invocation**: +30 more tests passing
- **Inference Comparison (PASS)**: +27 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| vit_large_patch14_clip_336.laion2b_ft_in12k_in1k | PASS | compiled_inference |
| vit_large_patch16_384.augreg_in21k_ft_in1k | PASS | compiled_inference |
| model--albert-xxl-v2-finetuned-squad--anas-awadalla | PASS | compiled_inference |
| beit_large_patch16_384_Opset16 | PASS | compiled_inference |
| beit_large_patch16_384_Opset17 | PASS | compiled_inference |
| convnext_xlarge_384_in22ft1k_Opset16 | PASS | compiled_inference |
| convnext_xlarge_384_in22ft1k_Opset17 | PASS | compiled_inference |
| resnet50-v1-12-qdq | PASS | Numerics |

**Total regressed models: 8**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge_384_in22ft1k_Opset16_timm | compiled_inference | PASS |
| deit3_large_patch16_384_in21ft1k_Opset17_timm | compiled_inference | PASS |
| dpn107_Opset16_timm | compilation | PASS |
| dpn107_Opset18_timm | compilation | PASS |
| dpn131_Opset18_timm | compilation | PASS |
| dpn68_Opset17_timm | compilation | PASS |
| dpn68b_Opset16_timm | compilation | PASS |
| dpn92_Opset17_timm | compilation | PASS |
| dpn98_Opset17_timm | compilation | PASS |
| vit_large_patch16_384_Opset16_timm | compiled_inference | PASS |
| deit3_large_patch16_384_Opset16 | compiled_inference | PASS |
| deit3_large_patch16_384_in21ft1k_Opset16 | compiled_inference | PASS |
| deit3_large_patch16_384_in21ft1k_Opset17 | compiled_inference | PASS |
| deit3_large_patch16_384_in21ft1k_Opset18 | compiled_inference | PASS |
| dpn107_Opset16 | compilation | PASS |
| dpn107_Opset17 | compilation | PASS |
| dpn107_Opset18 | compilation | PASS |
| dpn131_Opset16 | compilation | PASS |
| dpn131_Opset17 | compilation | PASS |
| dpn131_Opset18 | compilation | PASS |
| dpn68_Opset16 | compilation | PASS |
| dpn68_Opset17 | compilation | PASS |
| dpn68_Opset18 | compilation | PASS |
| dpn68b_Opset16 | compilation | PASS |
| dpn68b_Opset17 | compilation | PASS |
| dpn68b_Opset18 | compilation | PASS |
| dpn92_Opset16 | compilation | PASS |
| dpn92_Opset17 | compilation | PASS |
| dpn92_Opset18 | compilation | PASS |
| dpn98_Opset16 | compilation | PASS |
| dpn98_Opset17 | compilation | PASS |
| dpn98_Opset18 | compilation | PASS |
| migraphx_cadene__dpn92i1 | compilation | PASS |
| migraphx_cadene__inceptionv4i16 | compilation | PASS |
| migraphx_torchvision__densenet121i32 | compilation | PASS |

**Total improved models: 35**


---

