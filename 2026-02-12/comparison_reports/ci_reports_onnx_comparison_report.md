---
# Test Comparison Report

*Generated on: 2026-02-12*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-12/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-12/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

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
| IREE Inference Invocation | 3327 | 3944 | +617 |
| Inference Comparison (PASS) | 3194 | 3654 | +460 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 4 | 4 | 0 |
| IREE Compilation | 661 | 134 | -527 |
| Gold Inference | 1 | 1 | 0 |
| IREE Inference Invocation | 114 | 24 | -90 |
| Inference Comparison | 133 | 290 | +157 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-11/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-12/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

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

**Previous Run:** `2026-02-11/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-12/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3966 | 3969 | +3 | ✅ IMPROVED |
| Gold Inference | 3965 | 3968 | +3 | ✅ IMPROVED |
| IREE Inference Invocation | 3939 | 3944 | +5 | ✅ IMPROVED |
| Inference Comparison (PASS) | 3651 | 3654 | +3 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 137 | 134 | -3 | ✅ FEWER FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 26 | 24 | -2 | ✅ FEWER FAILURES |
| Inference Comparison | 288 | 290 | +2 | ⚠️ MORE FAILURES |

## Summary

### ✅ Improvements

- **IREE Compilation**: +3 more tests passing
- **Gold Inference**: +3 more tests passing
- **IREE Inference Invocation**: +5 more tests passing
- **Inference Comparison (PASS)**: +3 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| beit_large_patch16_384.in22k_ft_in22k_in1k | PASS | compiled_inference |
| convnext_xlarge.fb_in22k_ft_in1k | PASS | compiled_inference |
| deit3_large_patch16_384.fb_in1k | PASS | compiled_inference |
| dm_nfnet_f4.dm_in1k | PASS | compiled_inference |
| eva_large_patch14_336.in22k_ft_in1k | PASS | compiled_inference |
| maxvit_large_tf_512.in1k | PASS | compiled_inference |
| model--albert-xxl-v2-finetuned-squad--anas-awadalla | PASS | compiled_inference |
| beit_large_patch16_384_Opset16_timm | PASS | compiled_inference |
| beit_large_patch16_384_Opset17_timm | PASS | compiled_inference |
| vit_large_patch16_384_Opset17_timm | PASS | compiled_inference |
| vit_large_patch16_384_Opset16 | PASS | compiled_inference |
| vit_large_patch16_384_Opset17 | PASS | compiled_inference |
| vit_large_patch16_384_Opset18 | PASS | compiled_inference |

**Total regressed models: 13**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| vit_large_patch14_clip_336.laion2b_ft_in12k_in1k | compiled_inference | PASS |
| vit_large_patch16_384.augreg_in21k_ft_in1k | compiled_inference | PASS |
| convnext_xlarge_384_in22ft1k_Opset16_timm | compiled_inference | PASS |
| deit3_large_patch16_384_Opset16_timm | compiled_inference | PASS |
| deit3_large_patch16_384_in21ft1k_Opset17_timm | compiled_inference | PASS |
| vit_large_patch16_384_Opset16_timm | compiled_inference | PASS |
| migx_bench_bert-large-uncased_16_128 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_16_256 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_32_128 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_32_256 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_4_128 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_4_256 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_4_384 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_8_128 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_8_256 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_8_384 | compiled_inference | PASS |

**Total improved models: 16**


---

