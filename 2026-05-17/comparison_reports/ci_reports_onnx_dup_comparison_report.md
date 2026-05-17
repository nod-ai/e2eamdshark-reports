---
# Test Comparison Report

*Generated on: 2026-05-17*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-17/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-05-17/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 2359 | 1987 | -372 |
| IREE Compilation | 0 | 1941 | +1941 |
| Gold Inference | 0 | 1941 | +1941 |
| IREE Inference Invocation | 0 | 1940 | +1940 |
| Inference Comparison (PASS) | 0 | 1915 | +1915 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 2 | 374 | +372 |
| IREE Compilation | 2359 | 46 | -2313 |
| Gold Inference | 0 | 0 | 0 |
| IREE Inference Invocation | 0 | 1 | +1 |
| Inference Comparison | 0 | 25 | +25 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-10/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**Current Run:** `2026-05-17/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 2356 | 2359 | +3 | ✅ IMPROVED |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 0 | 0 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 5 | 2 | -3 | ✅ FEWER FAILURES |
| IREE Compilation | 2356 | 2359 | +3 | ⚠️ MORE FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison | 0 | 0 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **Setup**: +3 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-10/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`
**Current Run:** `2026-05-17/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 1987 | 1987 | 0 | ➖ NO CHANGE |
| IREE Compilation | 1929 | 1941 | +12 | ✅ IMPROVED |
| Gold Inference | 1929 | 1941 | +12 | ✅ IMPROVED |
| IREE Inference Invocation | 1924 | 1940 | +16 | ✅ IMPROVED |
| Inference Comparison (PASS) | 1899 | 1915 | +16 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 374 | 374 | 0 | ➖ NO CHANGE |
| IREE Compilation | 58 | 46 | -12 | ✅ FEWER FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 1 | -4 | ✅ FEWER FAILURES |
| Inference Comparison | 25 | 25 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Compilation**: +12 more tests passing
- **Gold Inference**: +12 more tests passing
- **IREE Inference Invocation**: +16 more tests passing
- **Inference Comparison (PASS)**: +16 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge_384_in22ft1k_Opset18_timm | compiled_inference | PASS |
| deit3_large_patch16_384_Opset17_timm | compiled_inference | PASS |
| deit3_large_patch16_384_in21ft1k_Opset16_timm | compiled_inference | PASS |
| dpn107_Opset17_timm | compilation | PASS |
| dpn131_Opset16_timm | compilation | PASS |
| dpn131_Opset17_timm | compilation | PASS |
| dpn68_Opset16_timm | compilation | PASS |
| dpn68_Opset18_timm | compilation | PASS |
| dpn68b_Opset17_timm | compilation | PASS |
| dpn68b_Opset18_timm | compilation | PASS |
| dpn92_Opset16_timm | compilation | PASS |
| dpn92_Opset18_timm | compilation | PASS |
| dpn98_Opset16_timm | compilation | PASS |
| dpn98_Opset18_timm | compilation | PASS |
| vit_large_patch16_384_Opset18_timm | compiled_inference | PASS |
| migraphx_torchvision__inceptioni32 | compilation | PASS |

**Total improved models: 16**


---

