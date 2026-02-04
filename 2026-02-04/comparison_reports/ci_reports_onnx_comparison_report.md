---
# Test Comparison Report

*Generated on: 2026-02-04*

---

# GPU vs CPU Comparison

**GPU Status:** `2026-02-04/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**CPU Status:** `2026-02-04/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Platform | Total Tests | Change |
|----------|-------------|--------|
| GPU | 4107 | - |
| CPU | 4107 | 0 |

## Passing Summary

| Stage | GPU (# Passing) | CPU (# Passing) | Change |
|-------|-----------------|-----------------|--------|
| Setup | 4092 | 4103 | +11 |
| IREE Compilation | 3433 | 3969 | +536 |
| Gold Inference | 3433 | 3968 | +535 |
| IREE Inference Invocation | 3319 | 3952 | +633 |
| Inference Comparison (PASS) | 3165 | 3677 | +512 |

## Fail Summary

| Stage | GPU (# Failed) | CPU (# Failed) | Change |
|-------|----------------|----------------|--------|
| Setup | 15 | 4 | -11 |
| IREE Compilation | 659 | 134 | -525 |
| Gold Inference | 0 | 1 | +1 |
| IREE Inference Invocation | 114 | 16 | -98 |
| Inference Comparison | 154 | 275 | +121 |

---

# GPU (rocm) - Regression Analysis

**Previous Run:** `2026-02-03/ci_reports_onnx/rocm/combined-reports_unique/summary.md`
**Current Run:** `2026-02-04/ci_reports_onnx/rocm/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4092 | 4092 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3125 | 3433 | +308 | ✅ IMPROVED |
| Gold Inference | 3124 | 3433 | +309 | ✅ IMPROVED |
| IREE Inference Invocation | 2997 | 3319 | +322 | ✅ IMPROVED |
| Inference Comparison (PASS) | 2694 | 3165 | +471 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 15 | 15 | 0 | ➖ NO CHANGE |
| IREE Compilation | 967 | 659 | -308 | ✅ FEWER FAILURES |
| Gold Inference | 1 | 0 | -1 | ✅ FEWER FAILURES |
| IREE Inference Invocation | 127 | 114 | -13 | ✅ FEWER FAILURES |
| Inference Comparison | 303 | 154 | -149 | ✅ FEWER FAILURES |

## Summary

### ✅ Improvements

- **IREE Compilation**: +308 more tests passing
- **Gold Inference**: +309 more tests passing
- **IREE Inference Invocation**: +322 more tests passing
- **Inference Comparison (PASS)**: +471 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| cs3sedarknet_l_train_vaiq | PASS | compilation |
| cs3sedarknet_x_train_vaiq | PASS | compilation |
| dm_nfnet_f0.dm_in1k_train_vaiq | PASS | compilation |
| dm_nfnet_f0.dm_in1k_vaiq | PASS | compilation |
| dm_nfnet_f1.dm_in1k_train_vaiq | PASS | compilation |
| dm_nfnet_f1.dm_in1k_vaiq | PASS | compilation |
| eca_nfnet_l0.ra2_in1k_train_vaiq | PASS | compilation |
| eca_nfnet_l1.ra2_in1k_train_vaiq | PASS | compilation |
| eca_nfnet_l2.ra3_in1k_train_vaiq | PASS | compilation |
| eca_resnet33ts.ra2_in1k_train_vaiq | PASS | compilation |
| eca_resnext26ts.ch_in1k_train_vaiq | PASS | compilation |
| ecaresnet26t_train_vaiq | PASS | compilation |
| ecaresnet26t_vaiq | PASS | compilation |
| ecaresnet50t_train_vaiq | PASS | compilation |
| ecaresnet50t_vaiq | PASS | compilation |
| efficientnet_b1.ft_in1k_train_vaiq | PASS | compilation |
| efficientnet_b4.ra2_in1k_train_vaiq | PASS | compilation |
| gcresnet33ts.ra2_in1k_train_vaiq | PASS | compilation |
| nf_regnet_b1.ra2_in1k_train_vaiq | PASS | compilation |
| nfnet_l0.ra2_in1k_train_vaiq | PASS | compilation |
| regnetx_040.pycls_in1k_vaiq | PASS | compilation |
| regnetx_080.pycls_in1k_vaiq | PASS | compilation |
| regnetx_160.pycls_in1k_vaiq | PASS | compilation |
| regnety_040.pycls_in1k_vaiq | PASS | compilation |
| regnety_040.ra3_in1k_train_vaiq | PASS | compilation |
| regnety_040.ra3_in1k_vaiq | PASS | compilation |
| regnety_320.pycls_in1k_vaiq | PASS | compilation |
| regnety_320.seer_ft_in1k_vaiq | PASS | compilation |
| regnety_640.seer_ft_in1k_vaiq | PASS | compilation |
| regnetz_040.ra3_in1k_train_vaiq | PASS | compilation |
| regnetz_040.ra3_in1k_vaiq | PASS | compilation |
| regnetz_040_h.ra3_in1k_train_vaiq | PASS | compilation |
| regnetz_040_h.ra3_in1k_vaiq | PASS | compilation |
| regnetz_d32.ra3_in1k_train_vaiq | PASS | compilation |
| regnetz_d32.ra3_in1k_vaiq | PASS | compilation |
| regnetz_d8.ra3_in1k_train_vaiq | PASS | compilation |
| regnetz_d8.ra3_in1k_vaiq | PASS | compilation |
| regnetz_d8_evos.ch_in1k_train_vaiq | PASS | compilation |
| regnetz_d8_evos.ch_in1k_vaiq | PASS | compilation |
| regnetz_e8.ra3_in1k_train_vaiq | PASS | compilation |
| regnetz_e8.ra3_in1k_vaiq | PASS | compilation |
| repvgg_b1g4.rvgg_in1k_vaiq | PASS | compilation |
| repvgg_b2g4.rvgg_in1k_vaiq | PASS | compilation |
| resnest101e_vaiq | PASS | compilation |
| resnest14d_vaiq | PASS | compilation |
| resnest26d_vaiq | PASS | compilation |
| resnest50d_vaiq | PASS | compilation |
| resnet50_gn_vaiq | PASS | compilation |
| resnetrs101_train_vaiq | PASS | compilation |
| resnetrs152_train_vaiq | PASS | compilation |

*... and 55 more regressed models*

**Total regressed models: 105**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| cs3darknet_focus_l_vaiq | Numerics | PASS |
| cs3darknet_focus_m_train_vaiq | compilation | PASS |
| cs3darknet_focus_m_vaiq | compilation | PASS |
| cs3darknet_l_vaiq | Numerics | PASS |
| cs3darknet_m_train_vaiq | compilation | PASS |
| cs3darknet_m_vaiq | compilation | PASS |
| cs3darknet_x_vaiq | compilation | PASS |
| cs3edgenet_x_train_vaiq | compilation | PASS |
| cs3edgenet_x_vaiq | compilation | PASS |
| cs3sedarknet_l_vaiq | Numerics | PASS |
| cs3sedarknet_x_vaiq | compilation | PASS |
| densenet161_vaiq | compilation | PASS |
| dla102x2_vaiq | Numerics | PASS |
| dla102x_vaiq | Numerics | PASS |
| dla60_res2net_vaiq | compilation | PASS |
| dla60_res2next_vaiq | Numerics | PASS |
| dla60_vaiq | Numerics | PASS |
| dla60x_vaiq | Numerics | PASS |
| ecaresnet50d_pruned_test_vaiq | compilation | PASS |
| ecaresnet50d_pruned_vaiq | compilation | PASS |
| efficientnetv2_rw_t.ra2_in1k_train_vaiq | compilation | PASS |
| gluon_resnet18_v1b_vaiq | Numerics | PASS |
| regnetx_032.pycls_in1k_vaiq | compilation | PASS |
| regnetx_064.pycls_in1k_vaiq | compilation | PASS |
| regnetx_120.pycls_in1k_vaiq | compilation | PASS |
| regnety_080.pycls_in1k_vaiq | compilation | PASS |
| regnety_080.ra3_in1k_train_vaiq | compilation | PASS |
| regnety_080.ra3_in1k_vaiq | compilation | PASS |
| regnety_080_tv.tv2_in1k_vaiq | compilation | PASS |
| regnety_120.pycls_in1k_vaiq | compilation | PASS |
| regnety_120.sw_in12k_ft_in1k_train_vaiq | compilation | PASS |
| regnety_160.lion_in12k_ft_in1k_train_vaiq | compilation | PASS |
| regnety_160.pycls_in1k_vaiq | compilation | PASS |
| repvgg_b3g4.rvgg_in1k_vaiq | compilation | PASS |
| res2net50_48w_2s_vaiq | compilation | PASS |
| resmlp_12_224.fb_distilled_in1k_vaiq | compilation | PASS |
| resmlp_24_224.fb_distilled_in1k_vaiq | compilation | PASS |
| resmlp_36_224.fb_distilled_in1k_vaiq | compilation | PASS |
| resmlp_big_24_224.fb_distilled_in1k_vaiq | compilation | PASS |
| resnest50d_1s4x24d_vaiq | compilation | PASS |
| resnet10t_vaiq | Numerics | PASS |
| resnet18_test_vaiq | Numerics | PASS |
| resnet18d_test_vaiq | Numerics | PASS |
| resnet18d_vaiq | Numerics | PASS |
| resnet34_test_vaiq | Numerics | PASS |
| resnet34d_test_vaiq | Numerics | PASS |
| resnet34d_vaiq | Numerics | PASS |
| selecsls42b_vaiq | compilation | PASS |
| tf_efficientnet_el.in1k_vaiq | compilation | PASS |
| tf_efficientnet_em.in1k_vaiq | compilation | PASS |

*... and 526 more improved models*

**Total improved models: 576**


---

# CPU (llvm-cpu) - Regression Analysis

**Previous Run:** `2026-02-03/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`
**Current Run:** `2026-02-04/ci_reports_onnx/llvm-cpu/combined-reports_unique/summary.md`

## Total Tests

| Status | Total Tests | Change |
|--------|-------------|--------|
| Previous | 4107 | - |
| Current | 4107 | 0 |

## Passing Tests - Change Analysis

| Stage | Previous (# Passing) | Current (# Passing) | Change | Status |
|-------|---------------------|---------------------|--------|--------|
| Setup | 4103 | 4103 | 0 | ➖ NO CHANGE |
| IREE Compilation | 3832 | 3969 | +137 | ✅ IMPROVED |
| Gold Inference | 3831 | 3968 | +137 | ✅ IMPROVED |
| IREE Inference Invocation | 3803 | 3952 | +149 | ✅ IMPROVED |
| Inference Comparison (PASS) | 3651 | 3677 | +26 | ✅ IMPROVED |

## Failing Tests - Change Analysis

| Stage | Previous (# Failed) | Current (# Failed) | Change | Status |
|-------|--------------------|--------------------|--------|--------|
| Setup | 4 | 4 | 0 | ➖ NO CHANGE |
| IREE Compilation | 271 | 134 | -137 | ✅ FEWER FAILURES |
| Gold Inference | 1 | 1 | 0 | ➖ NO CHANGE |
| IREE Inference Invocation | 28 | 16 | -12 | ✅ FEWER FAILURES |
| Inference Comparison | 152 | 275 | +123 | ⚠️ MORE FAILURES |

## Summary

### ✅ Improvements

- **IREE Compilation**: +137 more tests passing
- **Gold Inference**: +137 more tests passing
- **IREE Inference Invocation**: +149 more tests passing
- **Inference Comparison (PASS)**: +26 more tests passing

**Overall Status:** ✅ IMPROVEMENTS DETECTED

### 🔍 Regressed Models

The following models regressed from PASS to FAIL/Numerics/other:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| model--s2t-medium-librispeech-asr--facebook | PASS | Numerics |
| regnetx_002_Opset17_timm | PASS | compiled_inference |
| regnety_002_Opset16_timm | PASS | compiled_inference |
| regnetz_c16_evos_Opset16_timm | PASS | Numerics |
| xception41p_Opset16_timm | PASS | compiled_inference |
| xception65p_Opset18_timm | PASS | compiled_inference |
| flaubert_Opset16 | PASS | Numerics |
| fcn-resnet101-11 | PASS | Numerics |
| fcn-resnet50-11 | PASS | Numerics |
| fcn-resnet50-12 | PASS | Numerics |

**Total regressed models: 10**

### 🎉 Improved Models

The following models improved from FAIL/Numerics/other to PASS:

| Model Name | Previous Status | Current Status |
|------------|----------------|----------------|
| beit_large_patch16_384.in22k_ft_in22k_in1k | compiled_inference | PASS |
| convnext_xlarge.fb_in22k_ft_in1k | compiled_inference | PASS |
| deit3_large_patch16_384.fb_in1k | compiled_inference | PASS |
| dm_nfnet_f4.dm_in1k | compiled_inference | PASS |
| xception41_Opset17_timm | compiled_inference | PASS |
| xception71_Opset17_timm | compiled_inference | PASS |
| t5_Opset16 | Numerics | PASS |
| t5_Opset17 | Numerics | PASS |
| tf_efficientnetv2_b0_Opset16 | compilation | PASS |
| tf_efficientnetv2_b0_Opset17 | compilation | PASS |
| tf_efficientnetv2_b1_Opset16 | compilation | PASS |
| tf_efficientnetv2_b1_Opset17 | compilation | PASS |
| tf_efficientnetv2_b2_Opset16 | compilation | PASS |
| tf_efficientnetv2_b2_Opset17 | compilation | PASS |
| tf_efficientnetv2_b3_Opset16 | compilation | PASS |
| tf_efficientnetv2_b3_Opset17 | compilation | PASS |
| tf_mobilenetv3_small_075_Opset16 | compilation | PASS |
| tf_mobilenetv3_small_075_Opset17 | compilation | PASS |
| tf_mobilenetv3_small_100_Opset16 | compilation | PASS |
| tf_mobilenetv3_small_100_Opset17 | compilation | PASS |
| tf_mobilenetv3_small_minimal_100_Opset16 | compilation | PASS |
| tf_mobilenetv3_small_minimal_100_Opset17 | compilation | PASS |
| tf_mobilenetv3_small_minimal_100_Opset18 | compilation | PASS |
| xlmroberta_Opset16 | Numerics | PASS |
| migraphx_pytorch-examples__wlang_lstm | compiled_inference | PASS |
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
| resnet50-v1-12-qdq | Numerics | PASS |

**Total improved models: 36**


---

