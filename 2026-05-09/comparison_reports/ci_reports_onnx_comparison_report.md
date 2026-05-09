---
# Test Comparison Report

*Generated on: 2026-05-09*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-05-09/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-05-09/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4097 | 4103 | +6 |
| IREE Compilation | 0 | 3915 | +3915 |
| Gold Inference | 0 | 3914 | +3914 |
| IREE Inference Invocation | 0 | 3891 | +3891 |
| Inference Comparison (PASS) | 0 | 3621 | +3621 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 10 | 4 | -6 |
| IREE Compilation | 4097 | 188 | -3909 |
| Gold Inference | 0 | 1 | +1 |
| IREE Inference Invocation | 0 | 23 | +23 |
| Inference Comparison | 0 | 270 | +270 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-05-06/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-05-09/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4102 | 4097 | -5 | ⚠️ REGRESSION |
| IREE Compilation | 3772 | 0 | -3772 | ⚠️ REGRESSION |
| Gold Inference | 3771 | 0 | -3771 | ⚠️ REGRESSION |
| IREE Inference Invocation | 3391 | 0 | -3391 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3193 | 0 | -3193 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 5 | 10 | +5 | ⚠️ MORE FAILURES |
| IREE Compilation | 330 | 4097 | +3767 | ⚠️ MORE FAILURES |
| Gold Inference | 1 | 0 | -1 | ✅ FEWER FAILURES |
| IREE Inference Invocation | 380 | 0 | -380 | ✅ FEWER FAILURES |
| Inference Comparison | 198 | 0 | -198 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -5 fewer tests passing
- **IREE Compilation**: -3772 fewer tests passing
- **Gold Inference**: -3771 fewer tests passing
- **IREE Inference Invocation**: -3391 fewer tests passing
- **Inference Comparison (PASS)**: -3193 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| cs3darknet_focus_l_train_vaiq | PASS | compilation |
| cs3darknet_focus_l_vaiq | PASS | compilation |
| cs3darknet_focus_m_train_vaiq | PASS | compilation |
| cs3darknet_focus_m_vaiq | PASS | compilation |
| cs3darknet_l_train_vaiq | PASS | compilation |
| cs3darknet_l_vaiq | PASS | compilation |
| cs3darknet_m_train_vaiq | PASS | compilation |
| cs3darknet_m_vaiq | PASS | compilation |
| cs3darknet_x_train_vaiq | PASS | compilation |
| cs3darknet_x_vaiq | PASS | compilation |
| cs3edgenet_x_train_vaiq | PASS | compilation |
| cs3edgenet_x_vaiq | PASS | compilation |
| cs3se_edgenet_x_train_vaiq | PASS | compilation |
| cs3se_edgenet_x_vaiq | PASS | compilation |
| cs3sedarknet_l_train_vaiq | PASS | compilation |
| cs3sedarknet_l_vaiq | PASS | compilation |
| cs3sedarknet_x_train_vaiq | PASS | compilation |
| cs3sedarknet_x_vaiq | PASS | compilation |
| cspdarknet53_vaiq | PASS | compilation |
| cspresnet50_vaiq | PASS | compilation |
| cspresnext50_vaiq | PASS | compilation |
| densenet121_test_vaiq | PASS | compilation |
| densenet161_vaiq | PASS | compilation |
| densenet169_vaiq | PASS | compilation |
| densenetblur121d_test_vaiq | PASS | compilation |
| densenetblur121d_vaiq | PASS | compilation |
| dla102x2_vaiq | PASS | compilation |
| dla102x_vaiq | PASS | compilation |
| dla60_res2net_vaiq | PASS | compilation |
| dla60_vaiq | PASS | compilation |
| dla60x_vaiq | PASS | compilation |
| dm_nfnet_f0.dm_in1k_train_vaiq | PASS | compilation |
| dm_nfnet_f0.dm_in1k_vaiq | PASS | compilation |
| dm_nfnet_f1.dm_in1k_train_vaiq | PASS | compilation |
| dm_nfnet_f1.dm_in1k_vaiq | PASS | compilation |
| dpn68_vaiq | PASS | compilation |
| dpn68b_test_vaiq | PASS | compilation |
| dpn68b_vaiq | PASS | compilation |
| eca_nfnet_l0.ra2_in1k_train_vaiq | PASS | compilation |
| eca_nfnet_l0.ra2_in1k_vaiq | PASS | compilation |
| eca_nfnet_l1.ra2_in1k_train_vaiq | PASS | compilation |
| eca_nfnet_l1.ra2_in1k_vaiq | PASS | compilation |
| eca_nfnet_l2.ra3_in1k_train_vaiq | PASS | compilation |
| eca_resnext26ts.ch_in1k_train_vaiq | PASS | compilation |
| eca_resnext26ts.ch_in1k_vaiq | PASS | compilation |
| ecaresnet101d_pruned_test_vaiq | PASS | compilation |
| ecaresnet101d_pruned_vaiq | PASS | compilation |
| ecaresnet101d_test_vaiq | PASS | compilation |
| ecaresnet101d_vaiq | PASS | compilation |
| ecaresnet26t_train_vaiq | PASS | compilation |

*... and 3143 more regressed models*

**Total regressed models: 3193**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-05-06/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-05-09/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3931 | 3915 | -16 | ⚠️ REGRESSION |
| Gold Inference | 3930 | 3914 | -16 | ⚠️ REGRESSION |
| IREE Inference Invocation | 3903 | 3891 | -12 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3636 | 3621 | -15 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 172 | 188 | +16 | ⚠️ MORE FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 27 | 23 | -4 | ✅ FEWER FAILURES |
| Inference Comparison | 267 | 270 | +3 | ⚠️ MORE FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Compilation**: -16 fewer tests passing
- **Gold Inference**: -16 fewer tests passing
- **IREE Inference Invocation**: -12 fewer tests passing
- **Inference Comparison (PASS)**: -15 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| coat_lite_small_Opset17_timm | PASS | compilation |
| coat_lite_tiny_Opset17_timm | PASS | compilation |
| coat_tiny_Opset18_timm | PASS | compilation |
| pit_s_distilled_224_Opset17_timm | PASS | compilation |
| pit_ti_distilled_224_Opset16_timm | PASS | compilation |
| pit_ti_distilled_224_Opset17_timm | PASS | compilation |
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
| flaubert_Opset16_transformers | PASS | Numerics |
| flaubert_Opset17_transformers | PASS | Numerics |
| umt5_Opset16_transformers | PASS | Numerics |
| xlmroberta_Opset16_transformers | PASS | Numerics |

**Total regressed models: 20**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| model--albert-xxl-v2-finetuned-squad--anas-awadalla | compiled_inference | PASS |
| beit_large_patch16_384_Opset16_timm | compiled_inference | PASS |
| beit_large_patch16_384_Opset17_timm | compiled_inference | PASS |
| vit_large_patch16_384_Opset17_timm | compiled_inference | PASS |
| resnet50-v1-12-qdq | Numerics | PASS |

**Total improved models: 5**


---

