---
# Test Comparison Report

*Generated on: 2026-05-13*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-13/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-13/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4103 | 4103 | 0 |
| IREE Compilation | 0 | 3931 | +3931 |
| Gold Inference | 0 | 3930 | +3930 |
| IREE Inference Invocation | 0 | 3900 | +3900 |
| Inference Comparison (PASS) | 0 | 3628 | +3628 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 4 | 4 | 0 |
| IREE Compilation | 4103 | 172 | -3931 |
| Gold Inference | 0 | 1 | +1 |
| IREE Inference Invocation | 0 | 30 | +30 |
| Inference Comparison | 0 | 272 | +272 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-12/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-13/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4099 | 4103 | +4 | ✅ IMPROVED |
| IREE Compilation | 0 | 0 | 0 | ➖ NO CHANGE |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison (PASS) | 0 | 0 | 0 | ➖ NO CHANGE |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 8 | 4 | -4 | ✅ FEWER FAILURES |
| IREE Compilation | 4099 | 4103 | +4 | ⚠️ MORE FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 0 | 0 | 0 | ➖ NO CHANGE |
| Inference Comparison | 0 | 0 | 0 | ➖ NO CHANGE |

## Summary

### ✅ Improvements

- **Setup**: +4 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-12/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-13/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3916 | 3931 | +15 | ✅ IMPROVED |
| Gold Inference | 3915 | 3930 | +15 | ✅ IMPROVED |
| IREE Inference Invocation | 3891 | 3900 | +9 | ✅ IMPROVED |
| Inference Comparison (PASS) | 3624 | 3628 | +4 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 187 | 172 | -15 | ✅ FEWER FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 24 | 30 | +6 | ⚠️ MORE FAILURES |
| Inference Comparison | 267 | 272 | +5 | ⚠️ MORE FAILURES |

## Summary

### ✅ Improvements

- **IREE Compilation**: +15 more tests passing
- **Gold Inference**: +15 more tests passing
- **IREE Inference Invocation**: +9 more tests passing
- **Inference Comparison (PASS)**: +4 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| convnext_xlarge_384_in22ft1k_Opset16_timm | PASS | compiled_inference |
| deit3_large_patch16_384_in21ft1k_Opset17_timm | PASS | compiled_inference |
| vit_large_patch16_384_Opset16_timm | PASS | compiled_inference |
| deit3_large_patch16_384_Opset16 | PASS | compiled_inference |
| deit3_large_patch16_384_in21ft1k_Opset16 | PASS | compiled_inference |
| deit3_large_patch16_384_in21ft1k_Opset17 | PASS | compiled_inference |
| deit3_large_patch16_384_in21ft1k_Opset18 | PASS | compiled_inference |
| flaubert_Opset16 | PASS | Numerics |
| flaubert_Opset17 | PASS | Numerics |
| flaubert_Opset18 | PASS | Numerics |
| umt5_Opset16 | PASS | Numerics |
| umt5_Opset17 | PASS | Numerics |
| xlmroberta_Opset16 | PASS | Numerics |

**Total regressed models: 13**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| pit_b_224 | compilation | PASS |
| pit_b_distilled_224 | compilation | PASS |
| pit_s_distilled_224 | compilation | PASS |
| pit_ti_distilled_224 | compilation | PASS |
| pit_xs_distilled_224 | compilation | PASS |
| model--albert-xxl-v2-finetuned-squad--anas-awadalla | compiled_inference | PASS |
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
| resnet50-v1-12-qdq | Numerics | PASS |

**Total improved models: 17**


---

