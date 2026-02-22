---
# Test Comparison Report

*Generated on: 2026-02-22*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-22/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**CPU Status:** `2026-02-22/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 2361 | - |
| CPU | 2361 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 2351 | 1987 | -364 |
| IREE Compilation | 2128 | 1942 | -186 |
| Gold Inference | 2128 | 1942 | -186 |
| IREE Inference Invocation | 2127 | 1939 | -188 |
| Inference Comparison (PASS) | 2106 | 1905 | -201 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 10 | 374 | +364 |
| IREE Compilation | 223 | 45 | -178 |
| Gold Inference | 0 | 0 | 0 |
| IREE Inference Invocation | 1 | 3 | +2 |
| Inference Comparison | 21 | 34 | +13 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-20/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`
**Current Run:** `2026-02-22/ci_reports_onnx_dup/rocm/combined-reports_others/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 2361 | - |
| Current | 2361 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 2361 | 2351 | -10 | ⚠️ REGRESSION |
| IREE Compilation | 2134 | 2128 | -6 | ⚠️ REGRESSION |
| Gold Inference | 2134 | 2128 | -6 | ⚠️ REGRESSION |
| IREE Inference Invocation | 2133 | 2127 | -6 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 2112 | 2106 | -6 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 0 | 10 | +10 | ⚠️ MORE FAILURES |
| IREE Compilation | 227 | 223 | -4 | ✅ FEWER FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 1 | 1 | 0 | ➖ NO CHANGE |
| Inference Comparison | 21 | 21 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -10 fewer tests passing
- **IREE Compilation**: -6 fewer tests passing
- **Gold Inference**: -6 fewer tests passing
- **IREE Inference Invocation**: -6 fewer tests passing
- **Inference Comparison (PASS)**: -6 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| gluon_resnet50_v1b_Opset18_timm | PASS | setup |
| mobilenetv2_110d_Opset16_timm | PASS | setup |
| mobilenetv2_110d_Opset17_timm | PASS | setup |
| resnet152_Opset16_torch_hub | PASS | setup |
| vit_base_patch8_224_in21k_Opset18_timm | PASS | setup |
| vit_relpos_medium_patch16_cls_224_Opset18_timm | PASS | setup |

**Total regressed models: 6**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-20/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`
**Current Run:** `2026-02-22/ci_reports_onnx_dup/llvm-cpu/combined-reports_others/summary.md`

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
| IREE Inference Invocation | 1937 | 1939 | +2 | ✅ IMPROVED |
| Inference Comparison (PASS) | 1903 | 1905 | +2 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 374 | 374 | 0 | ➖ NO CHANGE |
| IREE Compilation | 45 | 45 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 5 | 3 | -2 | ✅ FEWER FAILURES |
| Inference Comparison | 34 | 34 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Inference Invocation**: +2 more tests passing
- **Inference Comparison (PASS)**: +2 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge_384_in22ft1k_Opset17_timm | compiled_inference | PASS |
| deit3_large_patch16_384_Opset18_timm | compiled_inference | PASS |

**Total improved models: 2**


---

