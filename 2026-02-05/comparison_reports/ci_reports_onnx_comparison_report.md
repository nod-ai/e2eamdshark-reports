---
# Test Comparison Report

*Generated on: 2026-02-05*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-05/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-05/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 0 | 4103 | +4103 |
| IREE Compilation | 0 | 3969 | +3969 |
| Gold Inference | 0 | 3968 | +3968 |
| IREE Inference Invocation | 0 | 3943 | +3943 |
| Inference Comparison (PASS) | 0 | 3669 | +3669 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 4107 | 4 | -4103 |
| IREE Compilation | 0 | 134 | +134 |
| Gold Inference | 0 | 1 | +1 |
| IREE Inference Invocation | 0 | 25 | +25 |
| Inference Comparison | 0 | 274 | +274 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-04/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-05/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4092 | 0 | -4092 | ⚠️ REGRESSION |
| IREE Compilation | 3433 | 0 | -3433 | ⚠️ REGRESSION |
| Gold Inference | 3433 | 0 | -3433 | ⚠️ REGRESSION |
| IREE Inference Invocation | 3319 | 0 | -3319 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3165 | 0 | -3165 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 15 | 4107 | +4092 | ⚠️ MORE FAILURES |
| IREE Compilation | 659 | 0 | -659 | ✅ FEWER FAILURES |
| Gold Inference | 0 | 0 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 114 | 0 | -114 | ✅ FEWER FAILURES |
| Inference Comparison | 154 | 0 | -154 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **Setup**: -4092 fewer tests passing
- **IREE Compilation**: -3433 fewer tests passing
- **Gold Inference**: -3433 fewer tests passing
- **IREE Inference Invocation**: -3319 fewer tests passing
- **Inference Comparison (PASS)**: -3165 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| cs3darknet_focus_l_train_vaiq | PASS | setup |
| cs3darknet_focus_l_vaiq | PASS | setup |
| cs3darknet_focus_m_train_vaiq | PASS | setup |
| cs3darknet_focus_m_vaiq | PASS | setup |
| cs3darknet_l_train_vaiq | PASS | setup |
| cs3darknet_l_vaiq | PASS | setup |
| cs3darknet_m_train_vaiq | PASS | setup |
| cs3darknet_m_vaiq | PASS | setup |
| cs3darknet_x_train_vaiq | PASS | setup |
| cs3darknet_x_vaiq | PASS | setup |
| cs3edgenet_x_train_vaiq | PASS | setup |
| cs3edgenet_x_vaiq | PASS | setup |
| cs3sedarknet_l_vaiq | PASS | setup |
| cs3sedarknet_x_vaiq | PASS | setup |
| cspdarknet53_vaiq | PASS | setup |
| cspresnet50_vaiq | PASS | setup |
| cspresnext50_vaiq | PASS | setup |
| densenet121_test_vaiq | PASS | setup |
| densenet161_vaiq | PASS | setup |
| densenet169_vaiq | PASS | setup |
| densenetblur121d_test_vaiq | PASS | setup |
| densenetblur121d_vaiq | PASS | setup |
| dla102x2_vaiq | PASS | setup |
| dla102x_vaiq | PASS | setup |
| dla60_res2net_vaiq | PASS | setup |
| dla60_res2next_vaiq | PASS | setup |
| dla60_vaiq | PASS | setup |
| dla60x_vaiq | PASS | setup |
| dpn107_vaiq | PASS | setup |
| dpn131_vaiq | PASS | setup |
| dpn68_vaiq | PASS | setup |
| eca_nfnet_l0.ra2_in1k_vaiq | PASS | setup |
| eca_nfnet_l1.ra2_in1k_vaiq | PASS | setup |
| eca_resnet33ts.ra2_in1k_vaiq | PASS | setup |
| eca_resnext26ts.ch_in1k_vaiq | PASS | setup |
| ecaresnet101d_pruned_test_vaiq | PASS | setup |
| ecaresnet101d_pruned_vaiq | PASS | setup |
| ecaresnet101d_test_vaiq | PASS | setup |
| ecaresnet101d_vaiq | PASS | setup |
| ecaresnet50d_pruned_test_vaiq | PASS | setup |
| ecaresnet50d_pruned_vaiq | PASS | setup |
| ecaresnet50d_test_vaiq | PASS | setup |
| ecaresnet50d_vaiq | PASS | setup |
| ecaresnetlight_test_vaiq | PASS | setup |
| ecaresnetlight_vaiq | PASS | setup |
| efficientnet_el_pruned.in1k_vaiq | PASS | setup |
| efficientnet_em.ra2_in1k_vaiq | PASS | setup |
| efficientnet_es_pruned.in1k_vaiq | PASS | setup |
| efficientnet_lite0.ra_in1k_vaiq | PASS | setup |
| efficientnetv2_rw_s.ra2_in1k_train_vaiq | PASS | setup |

*... and 3115 more regressed models*

**Total regressed models: 3165**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-04/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-05/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3969 | 3969 | 0 | ➖ NO CHANGE |
| Gold Inference | 3968 | 3968 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 3952 | 3943 | -9 | ⚠️ REGRESSION |
| Inference Comparison (PASS) | 3677 | 3669 | -8 | ⚠️ REGRESSION |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 134 | 134 | 0 | ➖ NO CHANGE |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 16 | 25 | +9 | ⚠️ MORE FAILURES |
| Inference Comparison | 275 | 274 | -1 | ✅ FEWER FAILURES |

## Summary

### ⚠️ Regressions Detected

- **IREE Inference Invocation**: -9 fewer tests passing
- **Inference Comparison (PASS)**: -8 fewer tests passing

**Overall Status:** ⚠️ REGRESSION DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| xception65_Opset18_timm | PASS | compiled_inference |
| t5_Opset16 | PASS | Numerics |
| t5_Opset17 | PASS | Numerics |
| xlmroberta_Opset16 | PASS | Numerics |
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
| flaubert_Opset16_transformers | PASS | Numerics |
| resnet50-v1-12-qdq | PASS | Numerics |

**Total regressed models: 16**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| regnetx_002_Opset17_timm | compiled_inference | PASS |
| regnety_002_Opset16_timm | compiled_inference | PASS |
| regnetz_d8_evos_Opset16_timm | Numerics | PASS |
| xception41p_Opset16_timm | compiled_inference | PASS |
| xception65p_Opset18_timm | compiled_inference | PASS |
| flaubert_Opset16 | Numerics | PASS |
| t5_Opset17_transformers | Numerics | PASS |
| xlmroberta_Opset16_transformers | Numerics | PASS |

**Total improved models: 8**


---

