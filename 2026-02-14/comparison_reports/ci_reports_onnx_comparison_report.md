---
# Test Comparison Report

*Generated on: 2026-02-14*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-14/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-14/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 3327 | 3942 | +615 |
| Inference Comparison (PASS) | 3194 | 3647 | +453 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 4 | 4 | 0 |
| IREE Compilation | 661 | 134 | -527 |
| Gold Inference | 1 | 1 | 0 |
| IREE Inference Invocation | 114 | 26 | -88 |
| Inference Comparison | 133 | 295 | +162 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-13/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-14/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

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

**Previous Run:** `2026-02-13/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-14/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3968 | 3969 | +1 | ✅ IMPROVED |
| Gold Inference | 3967 | 3968 | +1 | ✅ IMPROVED |
| IREE Inference Invocation | 3938 | 3942 | +4 | ✅ IMPROVED |
| Inference Comparison (PASS) | 3643 | 3647 | +4 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 135 | 134 | -1 | ✅ FEWER FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 29 | 26 | -3 | ✅ FEWER FAILURES |
| Inference Comparison | 295 | 295 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **IREE Compilation**: +1 more tests passing
- **Gold Inference**: +1 more tests passing
- **IREE Inference Invocation**: +4 more tests passing
- **Inference Comparison (PASS)**: +4 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| gluon_xception65 | PASS | compiled_inference |

**Total regressed models: 1**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| eva_large_patch14_336.in22k_ft_in1k | compiled_inference | PASS |
| maxvit_large_tf_512.in1k | compiled_inference | PASS |
| vit_large_patch16_384_Opset16 | compiled_inference | PASS |
| vit_large_patch16_384_Opset17 | compiled_inference | PASS |
| vit_large_patch16_384_Opset18 | compiled_inference | PASS |

**Total improved models: 5**


---

