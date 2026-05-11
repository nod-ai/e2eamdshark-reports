---
# Test Comparison Report

*Generated on: 2026-05-11*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-11/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-11/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4102 | 4103 | +1 |
| IREE Compilation | 0 | 3918 | +3918 |
| Gold Inference | 0 | 3917 | +3917 |
| IREE Inference Invocation | 0 | 3887 | +3887 |
| Inference Comparison (PASS) | 0 | 3620 | +3620 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 5 | 4 | -1 |
| IREE Compilation | 4102 | 185 | -3917 |
| Gold Inference | 0 | 1 | +1 |
| IREE Inference Invocation | 0 | 30 | +30 |
| Inference Comparison | 0 | 267 | +267 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-09/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-11/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4097 | 4102 | +5 | ✅ IMPROVED |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 0 | 0 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 10 | 5 | -5 | ✅ FEWER FAILURES |
| IREE Compilation | 4097 | 4102 | +5 | ⚠️ MORE FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison | 0 | 0 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **Setup**: +5 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-09/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-11/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3915 | 3918 | +3 | ✅ IMPROVED |
| Gold Inference | 3914 | 3917 | +3 | ✅ IMPROVED |
| IREE Inference Invocation | 3891 | 3887 | -4 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3621 | 3620 | -1 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 188 | 185 | -3 | ✅ FEWER FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 23 | 30 | +7 | ⚠️ MORE FAILURES |
| Inference Comparison | 270 | 267 | -3 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -4 fewer tests passing
- **Inference Comparison (PASS)**: -1 fewer tests passing

### ✅ Improvements

- **IREE Compilation**: +3 more tests passing
- **Gold Inference**: +3 more tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| model--albert-xxl-v2-finetuned-squad--anas-awadalla | PASS | compiled_inference |
| coat_lite_mini_Opset18_timm | PASS | compilation |
| coat_tiny_Opset16_timm | PASS | compilation |
| crossvit_18_240_Opset16_timm | PASS | compilation |
| crossvit_18_240_Opset17_timm | PASS | compilation |
| pit_b_distilled_224_Opset16_timm | PASS | compilation |
| pit_b_distilled_224_Opset18_timm | PASS | compilation |
| vit_base_patch8_224_dino_Opset16_timm | PASS | compilation |
| vit_base_patch8_224_dino_Opset18_timm | PASS | compilation |
| vit_base_patch8_224_in21k_Opset16_timm | PASS | compilation |
| vit_base_patch8_224_in21k_Opset17_timm | PASS | compilation |
| vit_small_patch8_224_dino_Opset16_timm | PASS | compilation |
| vit_small_patch8_224_dino_Opset18_timm | PASS | compilation |
| convnext_xlarge_384_in22ft1k_Opset18 | PASS | compiled_inference |
| vit_base_patch8_224_Opset17 | PASS | compilation |
| migx_bench_bert-large-uncased_1_256 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_1_384 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_2_128 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_2_256 | PASS | compiled_inference |
| migx_bench_bert-large-uncased_2_384 | PASS | compiled_inference |
| resnet50-v1-12-qdq | PASS | Numerics |

**Total regressed models: 21**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| coat_lite_small_Opset17_timm | compilation | PASS |
| coat_lite_tiny_Opset17_timm | compilation | PASS |
| coat_tiny_Opset18_timm | compilation | PASS |
| pit_s_distilled_224_Opset17_timm | compilation | PASS |
| pit_ti_distilled_224_Opset16_timm | compilation | PASS |
| pit_ti_distilled_224_Opset17_timm | compilation | PASS |
| vit_base_patch8_224_Opset16 | compilation | PASS |
| vit_base_patch8_224_dino_Opset16 | compilation | PASS |
| vit_base_patch8_224_dino_Opset17 | compilation | PASS |
| vit_base_patch8_224_dino_Opset18 | compilation | PASS |
| vit_base_patch8_224_in21k_Opset16 | compilation | PASS |
| vit_base_patch8_224_in21k_Opset17 | compilation | PASS |
| vit_base_patch8_224_in21k_Opset18 | compilation | PASS |
| vit_small_patch8_224_dino_Opset16 | compilation | PASS |
| vit_small_patch8_224_dino_Opset17 | compilation | PASS |
| vit_small_patch8_224_dino_Opset18 | compilation | PASS |
| flaubert_Opset16_transformers | Numerics | PASS |
| flaubert_Opset17_transformers | Numerics | PASS |
| umt5_Opset16_transformers | Numerics | PASS |
| xlmroberta_Opset16_transformers | Numerics | PASS |

**Total improved models: 20**


---

