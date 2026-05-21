---
# Test Comparison Report

*Generated on: 2026-05-21*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-21/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-21/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4102 | 4103 | +1 |
| IREE Compilation | 0 | 3960 | +3960 |
| Gold Inference | 0 | 3959 | +3959 |
| IREE Inference Invocation | 0 | 3935 | +3935 |
| Inference Comparison (PASS) | 0 | 3667 | +3667 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 5 | 4 | -1 |
| IREE Compilation | 4102 | 143 | -3959 |
| Gold Inference | 0 | 1 | +1 |
| IREE Inference Invocation | 0 | 24 | +24 |
| Inference Comparison | 0 | 268 | +268 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-15/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-21/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4102 | -1 | ⚠️ REGRESSION |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 0 | 0 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 5 | +1 | ⚠️ MORE FAILURES |
| IREE Compilation | 4103 | 4102 | -1 | ✅ FEWER FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison | 0 | 0 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -1 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-15/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-21/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3960 | 3960 | 0 | ➖ NO CHANGE |
| Gold Inference | 3959 | 3959 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3930 | 3935 | +5 | ✅ IMPROVED |
| Inference Comparison (PASS) | 3655 | 3667 | +12 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 143 | 143 | 0 | ➖ NO CHANGE |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 29 | 24 | -5 | ✅ FEWER FAILURES |
| Inference Comparison | 275 | 268 | -7 | ✅ FEWER FAILURES |

## Summary

### ✅ Improvements

- **IREE Inference Invocation**: +5 more tests passing
- **Inference Comparison (PASS)**: +12 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| vit_large_patch14_clip_336.laion2b_ft_in12k_in1k | compiled_inference | PASS |
| vit_large_patch16_384.augreg_in21k_ft_in1k | compiled_inference | PASS |
| beit_large_patch16_384_Opset16 | compiled_inference | PASS |
| beit_large_patch16_384_Opset17 | compiled_inference | PASS |
| convnext_xlarge_384_in22ft1k_Opset16 | compiled_inference | PASS |
| convnext_xlarge_384_in22ft1k_Opset17 | compiled_inference | PASS |
| flaubert_Opset16 | Numerics | PASS |
| flaubert_Opset17 | Numerics | PASS |
| flaubert_Opset18 | Numerics | PASS |
| umt5_Opset16 | Numerics | PASS |
| umt5_Opset17 | Numerics | PASS |
| xlmroberta_Opset16 | Numerics | PASS |

**Total improved models: 12**


---

