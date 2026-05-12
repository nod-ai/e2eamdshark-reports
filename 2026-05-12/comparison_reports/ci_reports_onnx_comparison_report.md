---
# Test Comparison Report

*Generated on: 2026-05-12*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-12/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-12/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4099 | 4103 | +4 |
| IREE Compilation | 0 | 3916 | +3916 |
| Gold Inference | 0 | 3915 | +3915 |
| IREE Inference Invocation | 0 | 3891 | +3891 |
| Inference Comparison (PASS) | 0 | 3624 | +3624 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 8 | 4 | -4 |
| IREE Compilation | 4099 | 187 | -3912 |
| Gold Inference | 0 | 1 | +1 |
| IREE Inference Invocation | 0 | 24 | +24 |
| Inference Comparison | 0 | 267 | +267 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-11/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-12/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4102 | 4099 | -3 | ⚠️ REGRESSION |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 0 | 0 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 5 | 8 | +3 | ⚠️ MORE FAILURES |
| IREE Compilation | 4102 | 4099 | -3 | ✅ FEWER FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison | 0 | 0 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -3 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-11/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-12/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3918 | 3916 | -2 | ⚠️ REGRESSION |
| Gold Inference | 3917 | 3915 | -2 | ⚠️ REGRESSION |
| IREE Inference Invocation | 3887 | 3891 | +4 | ✅ IMPROVED |
| Inference Comparison (PASS) | 3620 | 3624 | +4 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 185 | 187 | +2 | ⚠️ MORE FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 30 | 24 | -6 | ✅ FEWER FAILURES |
| Inference Comparison | 267 | 267 | 0 | ➖ NO CHANGE |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -2 fewer tests passing
- **Gold Inference**: -2 fewer tests passing

### ✅ Improvements

- **IREE Inference Invocation**: +4 more tests passing
- **Inference Comparison (PASS)**: +4 more tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| pit_b_224 | PASS | compilation |
| pit_b_distilled_224 | PASS | compilation |
| pit_s_distilled_224 | PASS | compilation |
| pit_ti_distilled_224 | PASS | compilation |
| pit_xs_distilled_224 | PASS | compilation |
| vit_base_patch8_224_Opset16 | PASS | compilation |
| vit_base_patch8_224_dino_Opset16 | PASS | compilation |
| vit_base_patch8_224_dino_Opset17 | PASS | compilation |
| vit_base_patch8_224_dino_Opset18 | PASS | compilation |
| vit_base_patch8_224_in21k_Opset16 | PASS | compilation |
| vit_base_patch8_224_in21k_Opset17 | PASS | compilation |
| vit_base_patch8_224_in21k_Opset18 | PASS | compilation |
| vit_small_patch8_224_dino_Opset16 | PASS | compilation |
| vit_small_patch8_224_dino_Opset17 | PASS | compilation |
| vit_small_patch8_224_dino_Opset18 | PASS | compilation |

**Total regressed models: 15**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| coat_lite_mini_Opset18_timm | compilation | PASS |
| coat_tiny_Opset16_timm | compilation | PASS |
| crossvit_18_240_Opset16_timm | compilation | PASS |
| crossvit_18_240_Opset17_timm | compilation | PASS |
| pit_b_distilled_224_Opset16_timm | compilation | PASS |
| pit_b_distilled_224_Opset18_timm | compilation | PASS |
| vit_base_patch8_224_dino_Opset16_timm | compilation | PASS |
| vit_base_patch8_224_dino_Opset18_timm | compilation | PASS |
| vit_base_patch8_224_in21k_Opset16_timm | compilation | PASS |
| vit_base_patch8_224_in21k_Opset17_timm | compilation | PASS |
| vit_small_patch8_224_dino_Opset16_timm | compilation | PASS |
| vit_small_patch8_224_dino_Opset18_timm | compilation | PASS |
| convnext_xlarge_384_in22ft1k_Opset18 | compiled_inference | PASS |
| vit_base_patch8_224_Opset17 | compilation | PASS |
| migx_bench_bert-large-uncased_1_256 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_1_384 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_2_128 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_2_256 | compiled_inference | PASS |
| migx_bench_bert-large-uncased_2_384 | compiled_inference | PASS |

**Total improved models: 19**


---

