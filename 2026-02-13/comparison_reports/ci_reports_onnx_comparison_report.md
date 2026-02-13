---
# Test Comparison Report

*Generated on: 2026-02-13*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-13/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-13/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4103 | 4103 | 0 |
| IREE Compilation | 3442 | 3968 | +526 |
| Gold Inference | 3441 | 3967 | +526 |
| IREE Inference Invocation | 3327 | 3938 | +611 |
| Inference Comparison (PASS) | 3194 | 3643 | +449 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 4 | 4 | 0 |
| IREE Compilation | 661 | 135 | -526 |
| Gold Inference | 1 | 1 | 0 |
| IREE Inference Invocation | 114 | 29 | -85 |
| Inference Comparison | 133 | 295 | +162 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-12/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-13/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

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

**Previous Run:** `2026-02-12/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-13/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 3944 | 3938 | -6 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3654 | 3643 | -11 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 134 | 135 | +1 | ⚠️ MORE FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 24 | 29 | +5 | ⚠️ MORE FAILURES |
| Inference Comparison | 290 | 295 | +5 | ⚠️ MORE FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -1 fewer tests passing
- **Gold Inference**: -1 fewer tests passing
- **IREE Inference Invocation**: -6 fewer tests passing
- **Inference Comparison (PASS)**: -11 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| dm_nfnet_f0_Opset16 | PASS | Numerics |
| dm_nfnet_f0_Opset17 | PASS | Numerics |
| dm_nfnet_f1_Opset16 | PASS | Numerics |
| dm_nfnet_f2_Opset16 | PASS | Numerics |
| dm_nfnet_f2_Opset17 | PASS | Numerics |
| migx_bench_bert-large-uncased_16_128 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_16_256 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_32_128 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_32_256 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_4_128 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_4_256 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_4_384 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_8_128 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_8_256 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_8_384 | PASS | compiled_inference |
| fcn-resnet101-11 | PASS | Numerics |
| fcn-resnet50-11 | PASS | Numerics |
| fcn-resnet50-12 | PASS | Numerics |

**Total regressed models: 18**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| beit_large_patch16_384.in22k_ft_in22k_in1k | compiled_inference | PASS |
| convnext_xlarge.fb_in22k_ft_in1k | compiled_inference | PASS |
| deit3_large_patch16_384.fb_in1k | compiled_inference | PASS |
| dm_nfnet_f4.dm_in1k | compiled_inference | PASS |
| beit_large_patch16_384_Opset16_timm | compiled_inference | PASS |
| beit_large_patch16_384_Opset17_timm | compiled_inference | PASS |
| vit_large_patch16_384_Opset17_timm | compiled_inference | PASS |

**Total improved models: 7**


---

