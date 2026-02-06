---
# Test Comparison Report

*Generated on: 2026-02-06*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-06/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-06/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 0 | 4103 | +4103 |
| IREE Compilation | 0 | 3968 | +3968 |
| Gold Inference | 0 | 3967 | +3967 |
| IREE Inference Invocation | 0 | 3935 | +3935 |
| Inference Comparison (PASS) | 0 | 3667 | +3667 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 4107 | 4 | -4103 |
| IREE Compilation | 0 | 135 | +135 |
| Gold Inference | 0 | 1 | +1 |
| IREE Inference Invocation | 0 | 32 | +32 |
| Inference Comparison | 0 | 268 | +268 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-05/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-06/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 0 | 0 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4107 | 4107 | 0 | ➖ NO CHANGE |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison | 0 | 0 | 0 | ➖ NO CHANGE |

## Summary

### ➖ No Changes

No changes detected in passing tests.

**Overall Status:** ➖ STABLE


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-05/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-06/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 3943 | 3935 | -8 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3669 | 3667 | -2 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 134 | 135 | +1 | ⚠️ MORE FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 25 | 32 | +7 | ⚠️ MORE FAILURES |
| Inference Comparison | 274 | 268 | -6 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -1 fewer tests passing
- **Gold Inference**: -1 fewer tests passing
- **IREE Inference Invocation**: -8 fewer tests passing
- **Inference Comparison (PASS)**: -2 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge_384_in22ft1k_Opset16_timm | PASS | compiled_inference |
| convnext_xlarge_in22ft1k_Opset17_timm | PASS | import_model |
| deit3_large_patch16_384_in21ft1k_Opset17_timm | PASS | compiled_inference |
| regnetz_d8_evos_Opset16_timm | PASS | Numerics |
| vit_large_patch16_384_Opset16_timm | PASS | compiled_inference |
| migx_bench_bert-large-uncased_1_256 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_1_384 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_2_128 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_2_256 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_2_384 | PASS | compiled_inference |
| t5_Opset17_transformers | PASS | Numerics |
| xlmroberta_Opset16_transformers | PASS | Numerics |

**Total regressed models: 12**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| xception65_Opset18_timm | compiled_inference | PASS |
| dm_nfnet_f0_Opset16 | Numerics | PASS |
| dm_nfnet_f0_Opset17 | Numerics | PASS |
| dm_nfnet_f1_Opset16 | Numerics | PASS |
| dm_nfnet_f2_Opset16 | Numerics | PASS |
| dm_nfnet_f2_Opset17 | Numerics | PASS |
| flaubert_Opset16_transformers | Numerics | PASS |
| fcn-resnet101-11 | Numerics | PASS |
| fcn-resnet50-11 | Numerics | PASS |
| fcn-resnet50-12 | Numerics | PASS |

**Total improved models: 10**


---

